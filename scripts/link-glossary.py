#!/usr/bin/env python3
"""Post-process rendered HTML pages to add first-occurrence glossary hyperlinks.

Runs AFTER linkify_node_ids() in the build pipeline.  Uses html.parser (stdlib)
to safely navigate HTML structure and insert glossary links only in appropriate
text nodes — never inside <a>, <code>, headings, blockquotes, metadata cards,
safety sections, or structural chrome.

Performance: Uses Aho-Corasick automaton (pyahocorasick) for O(text_length +
matches) per text node instead of O(terms × text_length) regex matching.

Usage:
    python3 scripts/link-glossary.py --dry-run --site-dir site/
    python3 scripts/link-glossary.py --site-dir site/ --verbose
"""

from __future__ import annotations

import argparse
import html as _html_mod
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

try:
    import ahocorasick
    _HAS_AHOCORASICK = True
except ImportError:
    _HAS_AHOCORASICK = False

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SKIP_TAGS = frozenset({
    "a", "code", "title",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "blockquote", "script", "style", "nav", "footer", "header",
})

HEADING_TAGS = frozenset({"h1", "h2", "h3", "h4", "h5", "h6"})

SAFETY_KEYWORDS = ("hazard", "safety", "warning")

# Generic section-heading-like terms that should never be linkified.
GENERIC_TERMS = frozenset({
    "advantages", "disadvantages", "construction", "design",
    "process steps", "step 1", "step 2", "step 3", "step 4",
    "step 5", "step 6", "step 7", "step 8", "step 9",
    "overview", "introduction", "background", "summary",
    "materials", "tools", "equipment", "safety",
    "applications", "properties", "uses",
    # Metadata field labels — should never be linked
    "node id", "parent", "enables", "dependencies", "domain",
    "timeline", "outputs", "tags", "era",
})

# Minimum/maximum pattern lengths for inclusion.
MIN_TERM_LEN = 3
MAX_TERM_LEN = 60


# ---------------------------------------------------------------------------
# Glossary loader (with filtering)
# ---------------------------------------------------------------------------

def _is_valid_term(term: str, definition: str, slug: str) -> bool:
    """Return True if term should be included in linkification automaton."""
    # Length checks
    if len(term) < MIN_TERM_LEN or len(term) > MAX_TERM_LEN:
        return False
    # Must have a non-empty definition
    if not definition.strip():
        return False
    # Skip purely numeric terms
    if term.strip().isdigit():
        return False
    # Skip generic section headings
    if term.lower().strip() in GENERIC_TERMS:
        return False
    return True


def load_glossary(glossary_path: str) -> list[dict]:
    """Load glossary terms + aliases, filtered and sorted longest-first."""
    with open(glossary_path, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    entries: list[dict] = []
    for item in data.get("terms", []):
        term = item["term"]
        slug = item["slug"]
        definition = item.get("definition", "")

        if not _is_valid_term(term, definition, slug):
            continue

        entries.append({
            "pattern": term,
            "slug": slug,
            "definition": definition,
        })
        for alias in item.get("aliases", []):
            if _is_valid_term(alias, definition, slug):
                entries.append({
                    "pattern": alias,
                    "slug": slug,
                    "definition": definition,
                })

    # Sort longest-first (for overlap resolution)
    entries.sort(key=lambda e: len(e["pattern"]), reverse=True)
    return entries


# ---------------------------------------------------------------------------
# Aho-Corasick automaton builder
# ---------------------------------------------------------------------------

def _build_automaton(entries: list[dict]) -> 'ahocorasick.Automaton | None':
    """Build case-insensitive Aho-Corasick automaton from glossary entries.

    Strategy: store lowercase patterns, map lowercase pattern -> list of entries.
    At match time, lowercase the text and verify word boundaries.
    """
    if not _HAS_AHOCORASICK:
        return None

    auto = ahocorasick.Automaton()
    # Deduplicate: same lowercase pattern can map to multiple entries (aliases)
    pattern_map: dict[str, list[int]] = {}

    for idx, entry in enumerate(entries):
        key = entry["pattern"].lower()
        if key not in pattern_map:
            pattern_map[key] = []
        pattern_map[key].append(idx)

    for key, indices in pattern_map.items():
        # Store the list of entry indices as value
        auto.add_word(key, (key, indices))

    auto.make_automaton()
    return auto


def _is_word_boundary(text: str, pos: int, end: int) -> bool:
    """Check if text[pos:end] has word boundaries on both sides."""
    # Left boundary
    if pos > 0:
        ch = text[pos - 1]
        if ch.isalnum() or ch == '_':
            return False
    # Right boundary
    if end < len(text):
        ch = text[end]
        if ch.isalnum() or ch == '_':
            return False
    return True


# ---------------------------------------------------------------------------
# HTML-aware glossary linker
# ---------------------------------------------------------------------------

class GlossaryLinker(HTMLParser):
    """Walk HTML, insert glossary links into eligible text nodes."""

    def __init__(
        self,
        glossary_entries: list[dict],
        automaton: 'ahocorasick.Automaton | None' = None,
        glossary_prefix: str = "../glossary/",
        *,
        verbose: bool = False,
        dry_run: bool = False,
    ):
        super().__init__(convert_charrefs=False)
        self.glossary_entries = glossary_entries
        self.automaton = automaton
        self.glossary_prefix = glossary_prefix
        self.verbose = verbose
        self.dry_run = dry_run
        self._reset_per_page()

    # -- per-page state ---------------------------------------------------

    def _reset_per_page(self) -> None:
        self.out: list[str] = []
        self.tag_stack: list[str] = []
        self.linked_slugs: set[str] = set()
        self.in_safety_section: bool = False
        self._heading_buf: list[str] = []
        self._in_heading: bool = False
        self._meta_card_depth: int = 0
        self.stats: dict = {
            "linked": [],
            "skipped_tags": 0,
            "skipped_safety": 0,
            "skipped_meta": 0,
        }

    def reset(self) -> None:  # noqa: D401 – overrides HTMLParser.reset
        self._reset_per_page()
        super().reset()

    # -- helpers ----------------------------------------------------------

    def _skip_depth(self) -> int:
        return sum(1 for t in self.tag_stack if t in SKIP_TAGS)

    def _should_skip(self) -> bool:
        return (
            self._skip_depth() > 0
            or self._meta_card_depth > 0
        )

    @staticmethod
    def _attrs_str(attrs: list[tuple[str, str | None]]) -> str:
        parts: list[str] = []
        for name, value in attrs:
            if value is None:
                parts.append(f" {name}")
            else:
                parts.append(f' {name}="{value}"')
        return "".join(parts)

    # -- parser callbacks -------------------------------------------------

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tag_stack.append(tag)
        attr_s = self._attrs_str(attrs)

        # track heading entry
        if tag in HEADING_TAGS:
            self._in_heading = True
            self._heading_buf = []

        # If a new heading appears while in a safety section, the safety
        # section may end — but only after we see the heading text.  We
        # tentatively clear the flag; handle_endtag will re-set it if the
        # heading itself is a safety heading.
        if tag in HEADING_TAGS and self.in_safety_section:
            self.in_safety_section = False

        # track metadata-card div nesting
        if tag == "div":
            for name, value in attrs:
                if name == "class" and value and "metadata-card" in value.split():
                    self._meta_card_depth += 1
                    break

        self.out.append(f"<{tag}{attr_s}>")

    def handle_endtag(self, tag: str) -> None:
        # metadata-card tracking
        if tag == "div" and self._meta_card_depth > 0:
            pass  # handled below after stack pop

        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()

        # metadata-card depth
        if tag == "div" and self._meta_card_depth > 0:
            self._meta_card_depth -= 1

        # heading exit — check for safety keywords
        if tag in HEADING_TAGS:
            heading_text = " ".join(self._heading_buf).lower()
            if any(kw in heading_text for kw in SAFETY_KEYWORDS):
                self.in_safety_section = True
            self._in_heading = False
            self._heading_buf = []

        self.out.append(f"</{tag}>")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.out.append(f"<{tag}{self._attrs_str(attrs)} />")

    def handle_data(self, data: str) -> None:
        # accumulate heading text for safety-keyword detection
        if self._in_heading:
            self._heading_buf.append(data)

        if self._meta_card_depth > 0:
            self.stats["skipped_meta"] += 1
            self.out.append(data)
            return

        if self._skip_depth() > 0:
            self.stats["skipped_tags"] += 1
            self.out.append(data)
            return

        if self.in_safety_section:
            self.stats["skipped_safety"] += 1
            self.out.append(data)
            return

        self.out.append(self._link_text(data))

    def handle_entityref(self, name: str) -> None:
        self.out.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        self.out.append(f"&#{name};")

    def handle_comment(self, data: str) -> None:
        self.out.append(f"<!--{data}-->")

    def handle_decl(self, decl: str) -> None:
        self.out.append(f"<!{decl}>")

    def handle_pi(self, data: str) -> None:
        self.out.append(f"<?{data}>")

    # -- glossary matching ------------------------------------------------

    def _link_text(self, text: str) -> str:
        """Find and wrap first-occurrence glossary terms in *text*."""
        if not text or not text.strip():
            return text

        # Use Aho-Corasick if available, else regex fallback
        if self.automaton is not None:
            candidates = self._find_matches_ahocorasick(text)
        else:
            candidates = self._find_matches_regex(text)

        if not candidates:
            return text

        # Resolve overlaps: sort by position, prefer longer at same start
        candidates.sort(key=lambda c: (c["start"], -(c["end"] - c["start"])))

        selected: list[dict] = []
        for cand in candidates:
            if cand["slug"] in self.linked_slugs:
                continue
            # overlap check
            overlaps = False
            for sel in selected:
                if cand["start"] < sel["end"] and sel["start"] < cand["end"]:
                    overlaps = True
                    break
            if not overlaps:
                selected.append(cand)
                self.linked_slugs.add(cand["slug"])

        if not selected:
            return text

        selected.sort(key=lambda c: c["start"])

        # Rebuild text with links
        parts: list[str] = []
        last = 0
        for match in selected:
            parts.append(text[last:match["start"]])

            truncated = match["definition"][:100]
            if len(match["definition"]) > 100:
                # truncate at last word boundary before 100 chars
                cut = truncated.rfind(" ")
                if cut > 0:
                    truncated = truncated[:cut]
                truncated += "\u2026"
            title_attr = _html_mod.escape(truncated, quote=True)

            parts.append(
                f'<a class="glossary-ref" '
                f'href="{self.glossary_prefix}{match["slug"]}.html" '
                f'title="{title_attr}">'
                f'{match["matched_text"]}</a>'
            )
            last = match["end"]

            self.stats["linked"].append({
                "term": match["matched_text"],
                "slug": match["slug"],
                "context": text[max(0, match["start"] - 30):match["end"] + 30].strip(),
            })

        parts.append(text[last:])
        return "".join(parts)

    def _find_matches_ahocorasick(self, text: str) -> list[dict]:
        """Find all glossary matches in text using Aho-Corasick automaton.

        Single pass through the text. Returns list of candidate match dicts.
        """
        text_lower = text.lower()
        raw_matches: list[dict] = []

        for end_pos, (pattern_key, entry_indices) in self.automaton.iter(text_lower):
            start_pos = end_pos - len(pattern_key) + 1

            # Verify word boundaries in the ORIGINAL text
            if not _is_word_boundary(text, start_pos, end_pos + 1):
                continue

            # Take the first entry index (entries are sorted longest-first,
            # so the first index for this pattern key is the canonical one)
            entry_idx = entry_indices[0]
            entry = self.glossary_entries[entry_idx]
            slug = entry["slug"]

            if slug in self.linked_slugs:
                continue

            raw_matches.append({
                "start": start_pos,
                "end": end_pos + 1,
                "slug": slug,
                "definition": entry["definition"],
                "matched_text": text[start_pos:end_pos + 1],
            })

        return raw_matches

    def _find_matches_regex(self, text: str) -> list[dict]:
        """Fallback: find matches using per-term regex (slow, original method)."""
        candidates: list[dict] = []
        for entry in self.glossary_entries:
            slug = entry["slug"]
            if slug in self.linked_slugs:
                continue
            escaped = re.escape(entry["pattern"])
            regex = re.compile(r"\b" + escaped + r"\b", re.IGNORECASE)
            m = regex.search(text)
            if m:
                candidates.append({
                    "start": m.start(),
                    "end": m.end(),
                    "slug": slug,
                    "definition": entry["definition"],
                    "matched_text": m.group(),
                })
        return candidates

    # -- output -----------------------------------------------------------

    def get_output(self) -> str:
        return "".join(self.out)


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

def _glossary_prefix_for(page_path: Path, site_dir: Path) -> str:
    """Compute relative path prefix from *page_path* to site-root/glossary/."""
    rel = page_path.relative_to(site_dir)
    depth = len(rel.parts) - 1  # filename doesn't count
    if depth <= 0:
        return "glossary/"
    return "../" * depth + "glossary/"


def find_html_pages(site_dir: str, exclude_domains: list[str] | None = None) -> list[Path]:
    """Find all .html pages under *site_dir*, optionally excluding domains."""
    site_path = Path(site_dir)
    exclude = set(exclude_domains or [])
    pages: list[Path] = []
    for html_file in sorted(site_path.rglob("*.html")):
        if exclude:
            rel = html_file.relative_to(site_path)
            parts = rel.parts
            if len(parts) >= 2 and parts[0] == "docs" and parts[1] in exclude:
                continue
        pages.append(html_file)
    return pages


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Add first-occurrence glossary hyperlinks to rendered HTML pages.",
    )
    ap.add_argument("--dry-run", action="store_true",
                    help="Report what would be linked without modifying files.")
    ap.add_argument("--verbose", action="store_true",
                    help="Show per-term match details.")
    ap.add_argument("--site-dir", default="site/",
                    help="Path to rendered site directory (default: site/).")
    ap.add_argument("--glossary", default="data/glossary.json",
                    help="Path to glossary.json (default: data/glossary.json).")
    ap.add_argument("--exclude-domains", nargs="*", default=[],
                    help="Skip certain domains during processing.")
    args = ap.parse_args()

    glossary_path = Path(args.glossary)
    if not glossary_path.exists():
        print(f"Error: glossary file not found: {glossary_path}", file=sys.stderr)
        sys.exit(1)

    site_path = Path(args.site_dir)
    if not site_path.is_dir():
        print(f"Error: site directory not found: {site_path}", file=sys.stderr)
        sys.exit(1)

    glossary_entries = load_glossary(str(glossary_path))
    unique_slugs = len({e["slug"] for e in glossary_entries})
    print(f"Loaded {len(glossary_entries)} glossary patterns from {unique_slugs} terms")

    # Build Aho-Corasick automaton
    automaton = _build_automaton(glossary_entries)
    if automaton is not None:
        print(f"Aho-Corasick automaton built ({len(glossary_entries)} patterns)")
    else:
        print("WARNING: pyahocorasick not available, using regex fallback (slow)")

    pages = find_html_pages(args.site_dir, args.exclude_domains)
    if not pages:
        print(f"No HTML pages found in {args.site_dir}")
        sys.exit(0)

    print(f"Processing {len(pages)} HTML pages ...")

    total_linked = 0
    total_pages_touched = 0

    for page_path in pages:
        html = page_path.read_text(encoding="utf-8")
        prefix = _glossary_prefix_for(page_path, site_path)

        linker = GlossaryLinker(
            glossary_entries,
            automaton=automaton,
            glossary_prefix=prefix,
            verbose=args.verbose,
            dry_run=args.dry_run,
        )
        linker.feed(html)
        modified = linker.get_output()
        stats = linker.stats

        if stats["linked"]:
            total_linked += len(stats["linked"])
            total_pages_touched += 1

            rel = page_path.relative_to(site_path)
            if args.verbose or args.dry_run:
                for info in stats["linked"]:
                    tag = "WOULD LINK" if args.dry_run else "LINKED"
                    print(f"  [{tag}] {rel}: '{info['term']}' -> {info['slug']}")
                    if args.verbose:
                        print(f"         context: ...{info['context']}...")

        if not args.dry_run and stats["linked"]:
            page_path.write_text(modified, encoding="utf-8")

    verb = "Would link" if args.dry_run else "Linked"
    unchanged = len(pages) - total_pages_touched
    print(f"\n{verb} {total_linked} term(s) across {total_pages_touched} page(s) "
          f"({unchanged} unchanged)")


if __name__ == "__main__":
    main()
