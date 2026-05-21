#!/usr/bin/env python3
"""Extract bold-pattern terms from all content articles.

Scans docs/ for markdown files (excluding images/, supporting/, and index.md)
and extracts terms defined with bold patterns like **Term**: definition.

Usage:
    python3 scripts/extract-terms.py
    python3 scripts/extract-terms.py --dry-run
    python3 scripts/extract-terms.py --domain chemistry --verbose
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DOCS_DIR = PROJECT_DIR / "docs"
DATA_DIR = PROJECT_DIR / "data"
DEFAULT_OUTPUT = DATA_DIR / "glossary-raw.json"

# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------

# Blockquote header: > **Node ID**: some.node.id
NODE_ID_RE = re.compile(r">\s*\*\*Node ID\*\*:\s*(.+)")

# Bold pattern: **Term** followed by :, -, (, or whitespace
BOLD_TERM_RE = re.compile(r"\*\*([^*]+)\*\*[:\-(\s]")

# Heading pattern (ATX style)
HEADING_RE = re.compile(r"^(#{1,6}\s+.+)$", re.MULTILINE)

# Unicode subscript characters (chemical formulas)
UNICODE_SUBSCRIPT_RE = re.compile(r"[₀₁₂₃₄₅₆₇₈₉]")

# Directories and files to skip
SKIP_DIRS = {"images", "supporting"}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def enumerate_markdown_files(docs_dir: Path, domain_filter: str | None = None) -> list[Path]:
    """Walk docs/ and return sorted list of .md files to process.

    Skips: images/, supporting/, index.md files.
    Optionally filters by domain directory name.
    """
    results = []
    for md_file in sorted(docs_dir.rglob("*.md")):
        rel = md_file.relative_to(docs_dir)
        parts = rel.parts

        # Skip excluded directories
        if parts[0] in SKIP_DIRS:
            continue

        # Skip all index.md files
        if md_file.name == "index.md":
            continue

        # Domain filter
        if domain_filter and parts[0] != domain_filter:
            continue

        results.append(md_file)

    return results


def extract_node_id(content: str) -> str:
    """Extract Node ID from blockquote header."""
    match = NODE_ID_RE.search(content)
    if match:
        return match.group(1).strip()
    return ""


def determine_context(line: str) -> str:
    """Determine where the bold pattern appeared.

    Returns "list_item", "heading", or "paragraph".
    """
    stripped = line.lstrip()
    if stripped.startswith(("- ", "* ", "+ ")):
        return "list_item"
    if re.match(r"^#{1,6}\s", stripped):
        return "heading"
    # Also check numbered list
    if re.match(r"^\d+[\.\)]\s", stripped):
        return "list_item"
    return "paragraph"


BLOCKQUOTE_HEADER_RE = re.compile(r"^>\s*\*\*[^*]+\*\*[:\s].*$", re.MULTILINE)


def _strip_blockquote_headers(content: str) -> str:
    return BLOCKQUOTE_HEADER_RE.sub("", content)


def extract_terms_from_file(
    md_path: Path, docs_dir: Path, verbose: bool = False
) -> list[dict]:
    """Extract all bold-pattern terms from a single markdown file.

    For each match, captures: term, definition, source_file, source_node_id,
    source_domain, context_type, is_chemical_formula, extraction_method.
    """
    raw_content = md_path.read_text(encoding="utf-8")
    rel = md_path.relative_to(docs_dir)
    parts = rel.parts

    source_file = str(rel)
    source_domain = parts[0] if len(parts) > 1 else ""
    source_node_id = extract_node_id(raw_content)

    # Strip blockquote header lines (metadata) from content used for matching
    content = _strip_blockquote_headers(raw_content)

    lines = content.split("\n")

    line_offsets = []
    offset = 0
    for line in lines:
        line_offsets.append(offset)
        offset += len(line) + 1

    terms = []
    seen = set()

    for match in BOLD_TERM_RE.finditer(content):
        term = match.group(1).strip()

        # Skip very short terms (likely formatting artifacts)
        if len(term) < 2:
            continue

        # Deduplicate within same file
        dedup_key = (term, source_file)
        if dedup_key in seen:
            continue
        seen.add(dedup_key)

        # Find which line this match is on
        match_start = match.start()
        line_idx = 0
        for i, off in enumerate(line_offsets):
            if off > match_start:
                break
            line_idx = i

        context_type = determine_context(lines[line_idx])

        # Extract definition: text after the bold pattern until next
        # bold pattern, heading, or blank line
        def_start = match.end()
        definition = _extract_definition(content, def_start)

        is_chemical = bool(UNICODE_SUBSCRIPT_RE.search(term))

        terms.append({
            "term": term,
            "definition": definition,
            "source_file": source_file,
            "source_node_id": source_node_id,
            "source_domain": source_domain,
            "context_type": context_type,
            "is_chemical_formula": is_chemical,
            "extraction_method": "bold-pattern",
        })

    if verbose and terms:
        print("  {} terms from {}".format(len(terms), source_file))

    return terms


def _extract_definition(content: str, start_pos: int) -> str:
    """Extract definition text following a bold-pattern match.

    Continues until encountering another bold pattern, a heading,
    or a blank line (end of paragraph/list item).
    """
    # Work with remaining content from match end
    remaining = content[start_pos:]
    lines = remaining.split("\n")

    def_parts = []

    for line in lines:
        stripped = line.strip()

        # Stop at blank line
        if not stripped:
            break

        # Stop at heading
        if re.match(r"^#{1,6}\s", stripped):
            break

        # Stop at another bold pattern that looks like a definition
        # (bold text followed by separator)
        if BOLD_TERM_RE.match(stripped) or BOLD_TERM_RE.search(stripped):
            # But only if it's at the start of the line (new definition)
            if BOLD_TERM_RE.match(stripped):
                break

        def_parts.append(stripped)

        # For list items or single-line definitions, stop after first line
        # unless the next line is a continuation (starts without bullet/heading)
        # Heuristic: if this line ends mid-sentence, continue; else stop
        if len(def_parts) == 1:
            # Check if the line seems complete (ends with period or is long)
            if stripped.endswith(".") and len(stripped) > 20:
                break

    definition = " ".join(def_parts).strip()

    # Truncate very long definitions
    if len(definition) > 500:
        definition = definition[:497] + "..."

    return definition


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Extract bold-pattern terms from content articles",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Output to stdout as JSON instead of writing file",
    )
    parser.add_argument(
        "--domain",
        default=None,
        help="Process only a specific domain (e.g. 'chemistry')",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Progress reporting",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Output file path (default: data/glossary-raw.json)",
    )
    args = parser.parse_args()

    docs_dir = DOCS_DIR
    if not docs_dir.is_dir():
        print("ERROR: docs directory not found: {}".format(docs_dir), file=sys.stderr)
        sys.exit(1)

    md_files = enumerate_markdown_files(docs_dir, domain_filter=args.domain)

    if not md_files:
        print("No markdown files found.", file=sys.stderr)
        sys.exit(1)

    if args.verbose:
        print("Processing {} files...".format(len(md_files)))
        if args.domain:
            print("  Domain filter: {}".format(args.domain))

    all_terms = []
    domains_seen = set()

    for md_file in md_files:
        terms = extract_terms_from_file(md_file, docs_dir, verbose=args.verbose)
        all_terms.extend(terms)
        if terms:
            rel = md_file.relative_to(docs_dir)
            domains_seen.add(rel.parts[0])

    output = {
        "terms": all_terms,
        "stats": {
            "total_terms": len(all_terms),
            "domains_covered": len(domains_seen),
            "articles_processed": len(md_files),
            "generated": datetime.now(timezone.utc).isoformat(),
        },
    }

    if args.dry_run:
        json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    else:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print("Wrote {} terms to {}".format(len(all_terms), output_path))

    if args.verbose:
        print("Total terms: {}".format(len(all_terms)))
        print("Domains covered: {}".format(len(domains_seen)))
        print("Articles processed: {}".format(len(md_files)))


if __name__ == "__main__":
    main()
