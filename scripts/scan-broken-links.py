#!/usr/bin/env python3
"""
scan-broken-links.py - Scan docs/ markdown files for broken relative internal links.

Finds all relative Markdown links ([text](../path)) in .md files under docs/,
resolves each path relative to the source file, and checks if the target exists.
Reports broken links with suggested fixes when the target filename exists elsewhere.

Usage:
    python3 scripts/scan-broken-links.py [--verbose] [--output FILE] [--include-glossary]
    python3 scripts/scan-broken-links.py --help
"""

import argparse
import os
import sys
import time
from pathlib import Path
from urllib.parse import unquote

from markdown_it import MarkdownIt

# --- Paths ---

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DOCS_DIR = PROJECT_DIR / "docs"

# --- Markdown link extraction via markdown_it ---

# Enable HTML and source line tracking so we get map data on tokens
md_parser = MarkdownIt("commonmark", {"html": True}).enable("link")


def text_to_slug(text: str) -> str:
    """
    Convert heading text to a GitHub-compatible slug.
    Lowercase, strip formatting, replace spaces/non-alnum with -,
    collapse dashes, strip leading/trailing dashes.
    """
    slug = text.lower().strip()
    slug_chars = []
    for ch in slug:
        if ch.isalnum() or ch == "-":
            slug_chars.append(ch)
        elif ch in (" ", "_", "\t"):
            slug_chars.append("-")
        else:
            slug_chars.append("-")
    slug = "".join(slug_chars)
    while "--" in slug:
        slug = slug.replace("--", "-")
    slug = slug.strip("-")
    return slug


def normalize_anchor(anchor: str) -> str:
    """
    Normalize an anchor from a link href for comparison with heading slugs.
    URL-decodes percent-encoded chars, lowercases, and strips leading #.
    """
    # URL-decode (handles %E2%82%82 etc.)
    decoded = unquote(anchor)
    # Apply same slug generation as headings
    return text_to_slug(decoded)


def extract_links_from_file(filepath: Path):
    """
    Parse a markdown file and yield (line_number, link_text, target_href) tuples.
    Uses markdown_it for proper AST-based extraction — no regex.
    """
    text = filepath.read_text(encoding="utf-8")
    tokens = md_parser.parse(text)

    for token in tokens:
        if token.type == "inline" and token.children:
            # Parent inline token has the line map; child link_open does not
            parent_line = (token.map[0] + 1) if token.map else 0
            children = token.children
            i = 0
            while i < len(children):
                child = children[i]
                if child.type == "link_open":
                    href = child.attrGet("href")
                    if href is None:
                        i += 1
                        continue

                    # Collect link text between link_open and link_close
                    link_parts = []
                    j = i + 1
                    while j < len(children) and children[j].type != "link_close":
                        link_parts.append(children[j].content)
                        j += 1

                    link_text = "".join(link_parts).strip()
                    yield (parent_line, link_text, href)
                    i = j + 1
                else:
                    i += 1


def extract_headings_from_tokens(tokens) -> set:
    """Extract heading slugs from pre-parsed tokens."""
    headings = set()
    for i, token in enumerate(tokens):
        if token.type == "heading_open":
            if i + 1 < len(tokens) and tokens[i + 1].type == "inline":
                heading_text = tokens[i + 1].content
                slug = text_to_slug(heading_text)
                if slug:
                    headings.add(slug)
    return headings


def is_external_link(href: str) -> bool:
    """Check if href is an external or non-file link."""
    if not href:
        return True
    # Explicit schemes
    if href.startswith(("http://", "https://", "mailto:", "tel:", "ftp://", "data:", "javascript:")):
        return True
    # Absolute paths (not our concern for relative link checking)
    if href.startswith("/"):
        return True
    return False


def build_file_index(docs_dir: Path, exclude_glossary: bool = True) -> dict:
    """Build filename -> list of full paths index for suggestion lookup."""
    index = {}
    for fpath in docs_dir.rglob("*.md"):
        if exclude_glossary and "glossary" in fpath.parts:
            continue
        fname = fpath.name
        if fname not in index:
            index[fname] = []
        index[fname].append(fpath)
    return index


def find_suggestions(resolved_name: str, file_index: dict, source_dir: Path) -> list:
    """
    Search for a file with the given basename somewhere under docs/.
    Returns list of relative paths from source_dir, sorted by relevance.
    """
    if not resolved_name:
        return []

    suggestions = []

    # Direct filename match
    for candidate_path in file_index.get(resolved_name, []):
        try:
            rel = os.path.relpath(candidate_path, source_dir)
            suggestions.append(rel)
        except ValueError:
            pass

    # If target looks like a domain directory (no .md), try <name>/index.md
    if not resolved_name.endswith(".md") and resolved_name:
        for candidate_path in file_index.get("index.md", []):
            if candidate_path.parent.name == resolved_name:
                try:
                    rel = os.path.relpath(candidate_path, source_dir)
                    suggestions.append(rel)
                except ValueError:
                    pass

    # If target was <name>.md and not found, try <name>/index.md
    if resolved_name.endswith(".md") and not suggestions:
        base_stem = resolved_name[:-3]
        for candidate_path in file_index.get("index.md", []):
            if candidate_path.parent.name == base_stem:
                try:
                    rel = os.path.relpath(candidate_path, source_dir)
                    suggestions.append(rel)
                except ValueError:
                    pass

    # Deduplicate, sort by relevance (fewer ../ is better)
    seen = set()
    unique = []
    for s in suggestions:
        if s not in seen:
            seen.add(s)
            unique.append(s)

    def sort_key(path):
        parts = Path(path).parts
        ups = sum(1 for p in parts if p == "..")
        return (ups, len(path))

    unique.sort(key=sort_key)
    return unique[:3]


def main():
    parser = argparse.ArgumentParser(
        description="Scan docs/ for broken relative internal links in markdown files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Output columns:
  source_file | line_number | link_text | target_path | resolved_path | status | suggested_fix

Exit codes:
  0  Scan completed successfully (broken links were found but scan ran OK)
  1  Error during execution
""",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="Show all links (OK + broken) in report; default shows only broken"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Write report to file instead of stdout",
    )
    parser.add_argument(
        "--include-glossary",
        action="store_true",
        default=False,
        help="Include glossary files in the scan (excluded by default)",
    )
    args = parser.parse_args()

    verbose = args.verbose
    exclude_glossary = not args.include_glossary

    if not DOCS_DIR.exists():
        print(f"ERROR: docs directory not found: {DOCS_DIR}", file=sys.stderr)
        sys.exit(1)

    t0 = time.time()

    # Collect all markdown files
    all_md_files = sorted(DOCS_DIR.rglob("*.md"))
    if exclude_glossary:
        all_md_files = [
            f for f in all_md_files if "glossary" not in f.parts
        ]

    if verbose:
        print(f"Scanning {len(all_md_files)} markdown files under {DOCS_DIR}",
              file=sys.stderr)

    # Build file index for suggestions
    file_index = build_file_index(DOCS_DIR, exclude_glossary)

    # Counters
    ok_count = 0
    broken_count = 0
    anchor_broken_count = 0
    skipped_count = 0
    broken_files = set()

    # Heading cache: filepath -> set of slugs
    heading_cache = {}

    def get_headings(fpath: Path) -> set:
        if fpath not in heading_cache:
            try:
                text = fpath.read_text(encoding="utf-8")
                tokens = md_parser.parse(text)
                heading_cache[fpath] = extract_headings_from_tokens(tokens)
            except Exception:
                heading_cache[fpath] = set()
        return heading_cache[fpath]

    # Collect broken link rows for the report
    broken_rows = []
    ok_rows = []

    for filepath in all_md_files:
        rel_source = filepath.relative_to(PROJECT_DIR)
        source_dir = filepath.parent

        try:
            links = list(extract_links_from_file(filepath))
        except Exception as exc:
            if verbose:
                print(f"  ERROR parsing {rel_source}: {exc}", file=sys.stderr)
            continue

        for line_num, link_text, href in links:
            # Skip external/absolute links
            if is_external_link(href):
                skipped_count += 1
                continue

            # Parse href into path + anchor parts
            if "#" in href:
                path_part, raw_anchor = href.split("#", 1)
            else:
                path_part = href
                raw_anchor = ""

            # Resolve the path
            if path_part:
                resolved = (source_dir / path_part).resolve()
                resolved_display = (
                    str(resolved.relative_to(PROJECT_DIR))
                    if resolved.is_relative_to(PROJECT_DIR)
                    else str(resolved)
                )
            else:
                # Anchor-only link (#section) — references current file
                resolved = filepath
                resolved_display = str(rel_source)

            # Check file existence
            if path_part:
                target_exists = resolved.exists()
            else:
                target_exists = True  # self-reference

            # Normalize anchor for comparison
            anchor_slug = normalize_anchor(raw_anchor) if raw_anchor else ""

            # Check anchor validity
            anchor_valid = True
            if anchor_slug and target_exists:
                if path_part:
                    target_file = resolved if resolved.is_file() else resolved / "index.md"
                else:
                    target_file = filepath

                if target_file.suffix == ".md" and target_file.exists():
                    target_headings = get_headings(target_file)
                    if anchor_slug not in target_headings:
                        anchor_valid = False

            # Determine status
            if not target_exists:
                status = "BROKEN"
                suggested_fix = find_suggestions(resolved.name, file_index, source_dir)
                fix_str = " | ".join(suggested_fix) if suggested_fix else "NOT FOUND"
                broken_count += 1
                broken_files.add(str(rel_source))
                row = (str(rel_source), line_num, link_text, href,
                       resolved_display, status, fix_str)
                broken_rows.append(row)

            elif not anchor_valid:
                status = "BROKEN_ANCHOR"
                fix_str = f"Anchor '#{raw_anchor}' not found"
                anchor_broken_count += 1
                broken_count += 1
                broken_files.add(str(rel_source))
                row = (str(rel_source), line_num, link_text, href,
                       resolved_display, status, fix_str)
                broken_rows.append(row)

            else:
                ok_count += 1
                if verbose:
                    ok_rows.append((
                        str(rel_source), line_num, link_text, href,
                        resolved_display, "OK", ""
                    ))

    # --- Build report ---
    output_lines = []
    output_lines.append("=" * 100)
    output_lines.append("BROKEN LINK AUDIT REPORT")
    output_lines.append(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    output_lines.append(f"Scanned: {len(all_md_files)} markdown files under docs/")
    output_lines.append(f"Exclusions: {'glossary/' if exclude_glossary else 'none'}")
    output_lines.append("=" * 100)
    output_lines.append("")

    # Column headers
    col_header = (
        f"{'source_file':<50} {'line':>5} {'link_text':<40} "
        f"{'target':<40} {'resolved':<50} {'status':<15} {'suggested_fix'}"
    )
    output_lines.append(col_header)
    output_lines.append("-" * 200)

    # Broken links (always shown)
    for src, line, text, target, resolved, status, fix in broken_rows:
        display_text = text[:38] + ".." if len(text) > 40 else text
        display_target = target[:38] + ".." if len(target) > 40 else target
        display_resolved = resolved[:48] + ".." if len(resolved) > 50 else resolved
        display_fix = fix[:60] + ".." if len(fix) > 60 else fix
        output_lines.append(
            f"{src:<50} {line:>5} {display_text:<40} "
            f"{display_target:<40} {display_resolved:<50} {status:<15} {display_fix}"
        )

    if verbose:
        output_lines.append("")
        output_lines.append("--- OK LINKS (verbose mode) ---")
        output_lines.append("-" * 200)
        for src, line, text, target, resolved, status, fix in ok_rows:
            display_text = text[:38] + ".." if len(text) > 40 else text
            display_target = target[:38] + ".." if len(target) > 40 else target
            display_resolved = resolved[:48] + ".." if len(resolved) > 50 else resolved
            output_lines.append(
                f"{src:<50} {line:>5} {display_text:<40} "
                f"{display_target:<40} {display_resolved:<50} {status:<15}"
            )

    # Summary
    total_relative = ok_count + broken_count
    output_lines.append("")
    output_lines.append("=" * 100)
    output_lines.append("SUMMARY")
    output_lines.append("=" * 100)
    output_lines.append(f"  Total internal links scanned: {total_relative + skipped_count}")
    output_lines.append(f"    Relative links:             {total_relative}")
    output_lines.append(f"      OK:                       {ok_count}")
    output_lines.append(f"      BROKEN (missing target):  {broken_count - anchor_broken_count}")
    output_lines.append(f"      BROKEN (missing anchor):  {anchor_broken_count}")
    output_lines.append(f"      Total broken:             {broken_count}")
    output_lines.append(f"    Skipped (external/abs):     {skipped_count}")
    output_lines.append(f"  Files with broken links:      {len(broken_files)}")
    output_lines.append(f"  Files scanned:                {len(all_md_files)}")
    output_lines.append("")

    # Per-file breakdown of broken links
    if broken_files:
        output_lines.append("BROKEN LINKS BY FILE:")
        output_lines.append("-" * 60)
        file_counts = {}
        for src, line, text, target, resolved, status, fix in broken_rows:
            file_counts[src] = file_counts.get(src, 0) + 1
        for src, count in sorted(file_counts.items(), key=lambda x: -x[1]):
            output_lines.append(f"  {count:>4} broken  {src}")
        output_lines.append("")

    elapsed = time.time() - t0
    output_lines.append(f"Scan completed in {elapsed:.1f}s")

    report = "\n".join(output_lines)

    # Write output
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report + "\n", encoding="utf-8")
        # Also print summary to stderr for immediate feedback
        print(f"Report written to {args.output}", file=sys.stderr)
        print(
            f"Found {broken_count} broken links across {len(broken_files)} files "
            f"({total_relative} total relative links, {len(all_md_files)} files scanned)",
            file=sys.stderr,
        )
    else:
        print(report)

    # Exit code: 0 on success (audit ran OK; broken links are the expected output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
