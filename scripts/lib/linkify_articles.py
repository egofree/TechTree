#!/usr/bin/env python3
"""Scan Markdown articles for bold terms matching node IDs or glossary entries.

Identifies ``**bold text**`` patterns in article .md files under docs/,
matches them against a closed vocabulary built from nodes.json and
glossary.json, and converts qualifying matches into relative Markdown
hyperlinks: ``**[term](relative/path.md)**``.

Nine exclusion rules prevent false positives from metadata headers,
section labels, code blocks, already-linked text, and generic headings.

Usage::

    python scripts/lib/linkify_articles.py --dry-run
    python scripts/lib/linkify_articles.py --execute
    python scripts/lib/linkify_articles.py --dry-run --report linkify-report.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Exclusion rule 7: generic label blocklist (case-insensitive)
GENERIC_LABEL_BLOCKLIST: frozenset[str] = frozenset({
    "Construction", "Operation", "Use", "Principle", "Raw materials",
    "Properties", "Composition", "Overview", "Materials", "Equipment",
    "Process", "Safety", "Applications", "Notes", "Description",
    "Design", "Assembly", "Installation", "Maintenance",
    "Troubleshooting", "Advantages", "Disadvantages", "Limitations",
    "Variants", "History",
})

# Exclusion rule 9: metadata labels (case-insensitive)
METADATA_LABELS: frozenset[str] = frozenset({
    "Node ID", "Domain", "Dependencies", "Enables", "Timeline",
    "Outputs", "Era", "Parent", "Status", "Level",
})

# Combined blocklist (lowercase for comparison)
BLOCKLIST_LOWER: frozenset[str] = frozenset(
    t.lower() for t in GENERIC_LABEL_BLOCKLIST | METADATA_LABELS
)

# Regex: match **bold text** (not already inside a link)
# Captures the bold content between ** markers, excluding surrounding whitespace
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")

# Regex: detect already-hyperlinked bold — **[text](url)**
ALREADY_LINKED_RE = re.compile(r"\*\*\[.*?\]\(.*?\)\*\*")

# Regex: label pattern — **Term**: description  (colon immediately after closing **)
LABEL_PATTERN_RE = re.compile(r"\*\*.+?\*\*:")

# Section headings that trigger skip zones
SAFETY_HEADING_RE = re.compile(r"^###\s+Safety\b", re.IGNORECASE)
CROSS_DOMAIN_HEADING_RE = re.compile(
    r"^###\s+(Cross-Domain Links|Cross-References)\b", re.IGNORECASE
)
HEADING_RE = re.compile(r"^#{1,6}\s+")


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def _node_id_to_md_path(node_id: str) -> str:
    """Convert a dotted node ID to its expected .md file path.

    ``metals.copper-bronze`` -> ``docs/metals/copper-bronze.md``
    ``metals``               -> ``docs/metals/index.md``
    """
    segments = node_id.split(".")
    if len(segments) == 1:
        return f"docs/{segments[0]}/index.md"
    return f"docs/{segments[0]}/{'-'.join(segments[1:])}.md"


def load_nodes(nodes_path: str) -> dict:
    """Load nodes.json and build lookup structures.

    Returns dict with:
        - ``id_to_name``: {node_id_lower: node_name}
        - ``id_to_path``: {node_id: absolute_md_path_str}
        - ``name_to_id``: {name_lower: node_id}
        - ``slug_to_id``: {slug_lower: node_id}  (slug = part after domain dot)
    """
    with open(nodes_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    id_to_name: dict[str, str] = {}
    id_to_path: dict[str, str] = {}
    name_to_id: dict[str, str] = {}
    slug_to_id: dict[str, str] = {}

    for node in data.get("nodes", []):
        nid = node["id"]
        name = node.get("name", "")
        id_to_name[nid.lower()] = name
        id_to_path[nid] = _node_id_to_md_path(nid)
        if name:
            name_to_id[name.lower()] = nid
        # Also index the slug part (everything after the first dot)
        parts = nid.split(".", 1)
        if len(parts) == 2:
            slug = parts[1]
            slug_to_id[slug.lower()] = nid
            # Also index slug with spaces instead of hyphens
            slug_spaced = slug.replace("-", " ")
            slug_to_id[slug_spaced.lower()] = nid

    return {
        "id_to_name": id_to_name,
        "id_to_path": id_to_path,
        "name_to_id": name_to_id,
        "slug_to_id": slug_to_id,
    }


def load_glossary(glossary_path: str) -> dict[str, str]:
    """Load glossary.json and return {term_lower: slug} for terms with definitions."""
    with open(glossary_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    term_to_slug: dict[str, str] = {}
    for item in data.get("terms", []):
        definition = item.get("definition", "")
        if not definition.strip():
            continue
        term = item["term"]
        slug = item["slug"]
        term_to_slug[term.lower()] = slug
        # Also index aliases
        for alias in item.get("aliases", []):
            if alias.strip():
                term_to_slug[alias.lower().strip()] = slug

    return term_to_slug


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

def find_article_files(docs_dir: str) -> list[Path]:
    """Find all .md files under docs/, excluding supporting/, images/, glossary/."""
    docs_path = Path(docs_dir)
    exclude_dirs = {"supporting", "images", "glossary"}
    results: list[Path] = []

    for md_file in sorted(docs_path.rglob("*.md")):
        rel = md_file.relative_to(docs_path)
        if rel.parts[0] in exclude_dirs:
            continue
        results.append(md_file)

    return results


# ---------------------------------------------------------------------------
# Matching logic
# ---------------------------------------------------------------------------

def _compute_relative_path(source_file: Path, target_md_path: str, base_dir: str) -> str:
    """Compute relative path from source file to target using os.path.relpath."""
    target_abs = os.path.normpath(os.path.join(base_dir, target_md_path))
    source_dir = str(source_file.parent)
    return os.path.relpath(target_abs, source_dir)


def _compute_glossary_relative_path(source_file: Path, slug: str) -> str:
    """Compute relative path from source file to glossary HTML page.

    Glossary pages live at docs/glossary/{slug}.html, built as HTML.
    From docs/{domain}/file.md, the path is ../glossary/{slug}.html.
    """
    # source_file is under docs/{domain}/, so relative to that: ../glossary/slug.html
    source_dir = source_file.parent
    glossary_dir = source_dir.parent / "glossary"
    try:
        rel = os.path.relpath(str(glossary_dir / f"{slug}.html"), str(source_dir))
    except ValueError:
        # On Windows, relpath can fail across drives
        rel = f"../glossary/{slug}.html"
    return rel


def match_bold_term(
    bold_text: str,
    nodes_data: dict,
    glossary_terms: dict[str, str],
) -> tuple[str, str | None, str | None]:
    """Try to match a bold text against the closed vocabulary.

    Returns (confidence, target_path_or_none, match_type).
    - confidence: "HIGH", "MEDIUM", or ""
    - target_path: relative path for linking (or None if no match)
    - match_type: "node" or "glossary"
    """
    bt_lower = bold_text.lower().strip()

    if not bt_lower:
        return ("", None, None)

    # Priority 1: Exact node ID match
    if bt_lower in nodes_data["id_to_name"]:
        node_id = None
        for nid in nodes_data["id_to_path"]:
            if nid.lower() == bt_lower:
                node_id = nid
                break
        if node_id:
            return ("HIGH", node_id, "node")

    # Priority 2: Node name match (from name field)
    if bt_lower in nodes_data["name_to_id"]:
        node_id = nodes_data["name_to_id"][bt_lower]
        return ("HIGH", node_id, "node")

    # Priority 3: Node slug match (part after domain dot)
    if bt_lower in nodes_data["slug_to_id"]:
        node_id = nodes_data["slug_to_id"][bt_lower]
        return ("HIGH", node_id, "node")

    # Priority 4: Glossary term match
    if bt_lower in glossary_terms:
        slug = glossary_terms[bt_lower]
        return ("MEDIUM", slug, "glossary")

    return ("", None, None)


# ---------------------------------------------------------------------------
# Core processing
# ---------------------------------------------------------------------------

def process_file(
    file_path: Path,
    base_dir: str,
    nodes_data: dict,
    glossary_terms: dict[str, str],
) -> dict:
    """Process a single .md file and return match/exclusion report.

    Returns dict with:
        - ``file``: relative path string
        - ``high_matches``: list of match dicts
        - ``medium_matches``: list of match dicts
        - ``excluded``: list of exclusion dicts
        - ``new_content``: modified content (or original if dry-run)
        - ``stats``: per-rule exclusion counts
    """
    content = file_path.read_text(encoding="utf-8")
    lines = content.split("\n")

    high_matches: list[dict] = []
    medium_matches: list[dict] = []
    excluded: list[dict] = []

    # Per-rule exclusion counters
    stats = {
        "blockquote_metadata": 0,
        "already_linked": 0,
        "label_pattern": 0,
        "code_block": 0,
        "safety_section": 0,
        "cross_domain_section": 0,
        "blocklist": 0,
        "single_char": 0,
        "metadata_label": 0,
    }

    in_code_block = False
    in_safety_section = False
    in_cross_domain_section = False
    modified_lines: list[str] = []

    for line_num_0, line in enumerate(lines):
        line_num = line_num_0 + 1

        # Track code block fences (rule 4)
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            modified_lines.append(line)
            continue

        if in_code_block:
            # Still scan for bold inside code blocks to record exclusions
            for m in BOLD_RE.finditer(line):
                bold_text = m.group(1)
                excluded.append({
                    "term": bold_text,
                    "file": str(file_path.relative_to(base_dir)),
                    "reason": "code_block",
                    "line": line_num,
                })
                stats["code_block"] += 1
            modified_lines.append(line)
            continue

        # Track section context (rules 5, 6)
        if HEADING_RE.match(line):
            if SAFETY_HEADING_RE.match(line):
                in_safety_section = True
                in_cross_domain_section = False
            elif CROSS_DOMAIN_HEADING_RE.match(line):
                in_cross_domain_section = True
                in_safety_section = False
            else:
                # Any other heading resets both skip zones
                in_safety_section = False
                in_cross_domain_section = False
            modified_lines.append(line)
            continue

        # Rule 1: Blockquote metadata — lines starting with "> "
        if line.lstrip().startswith("> "):
            for m in BOLD_RE.finditer(line):
                bold_text = m.group(1)
                excluded.append({
                    "term": bold_text,
                    "file": str(file_path.relative_to(base_dir)),
                    "reason": "blockquote_metadata",
                    "line": line_num,
                })
                stats["blockquote_metadata"] += 1
            modified_lines.append(line)
            continue

        # Rule 2: Already-hyperlinked bold
        if ALREADY_LINKED_RE.search(line):
            for m in BOLD_RE.finditer(line):
                full_match = m.group(0)
                # Check if this specific bold instance contains a link
                if re.match(r"\*\*\[.*?\]\(.*?\)\*\*", full_match):
                    excluded.append({
                        "term": m.group(1),
                        "file": str(file_path.relative_to(base_dir)),
                        "reason": "already_linked",
                        "line": line_num,
                    })
                    stats["already_linked"] += 1
            modified_lines.append(line)
            continue

        # Rule 3: Label pattern **Term**: description
        # Check for **text**: pattern on this line
        has_label_pattern = bool(LABEL_PATTERN_RE.search(line))

        # Process bold instances on this line
        new_line = line
        # We need to process bold instances in order, handling replacements carefully
        # Find all bold instances
        bold_instances = list(BOLD_RE.finditer(line))

        if not bold_instances:
            modified_lines.append(line)
            continue

        # Process each bold instance
        # Work backwards to preserve positions
        replacements: list[tuple[int, int, str, str]] = []  # (start, end, replacement, reason_or_empty)

        for m in bold_instances:
            bold_text = m.group(1)
            full_start = m.start()
            full_end = m.end()

            # Rule 8: Single-character bold
            if len(bold_text.strip()) <= 1:
                excluded.append({
                    "term": bold_text,
                    "file": str(file_path.relative_to(base_dir)),
                    "reason": "single_char",
                    "line": line_num,
                })
                stats["single_char"] += 1
                continue

            # Rule 7 & 9: Blocklist and metadata labels
            if bold_text.lower().strip() in BLOCKLIST_LOWER:
                reason = "metadata_label" if bold_text in METADATA_LABELS or bold_text.lower() in (t.lower() for t in METADATA_LABELS) else "blocklist"
                excluded.append({
                    "term": bold_text,
                    "file": str(file_path.relative_to(base_dir)),
                    "reason": reason,
                    "line": line_num,
                })
                if reason == "metadata_label":
                    stats["metadata_label"] += 1
                else:
                    stats["blocklist"] += 1
                continue

            # Rule 3: Label pattern (bold followed by colon)
            if has_label_pattern:
                # Check if THIS bold instance is followed by a colon
                after = line[full_end:full_end + 2].lstrip()
                # Check if the closing ** is followed by :
                close_pos = line.find("**", full_start + 2)
                if close_pos != -1 and close_pos < full_end:
                    pass  # shouldn't happen since regex matched
                # Simpler: check if the text right after this bold match starts with :
                rest_of_line = line[full_end:]
                if rest_of_line.lstrip().startswith(":"):
                    excluded.append({
                        "term": bold_text,
                        "file": str(file_path.relative_to(base_dir)),
                        "reason": "label_pattern",
                        "line": line_num,
                    })
                    stats["label_pattern"] += 1
                    continue

            # Rule 2: Already-hyperlinked bold (check this specific instance)
            if bold_text.startswith("[") and "](" in bold_text:
                excluded.append({
                    "term": bold_text,
                    "file": str(file_path.relative_to(base_dir)),
                    "reason": "already_linked",
                    "line": line_num,
                })
                stats["already_linked"] += 1
                continue

            # Rule 5: Safety section
            if in_safety_section:
                excluded.append({
                    "term": bold_text,
                    "file": str(file_path.relative_to(base_dir)),
                    "reason": "safety_section",
                    "line": line_num,
                })
                stats["safety_section"] += 1
                continue

            # Rule 6: Cross-domain links section
            if in_cross_domain_section:
                excluded.append({
                    "term": bold_text,
                    "file": str(file_path.relative_to(base_dir)),
                    "reason": "cross_domain_section",
                    "line": line_num,
                })
                stats["cross_domain_section"] += 1
                continue

            # Attempt match against closed vocabulary
            confidence, target, match_type = match_bold_term(
                bold_text, nodes_data, glossary_terms
            )

            if not confidence:
                # No match — leave as-is
                continue

            # Compute relative path
            if match_type == "node" and target:
                # target is a node_id, need to compute relative path
                target_md = nodes_data["id_to_path"].get(target)
                if not target_md:
                    continue
                rel_path = _compute_relative_path(file_path, target_md, base_dir)
                match_entry = {
                    "term": bold_text,
                    "file": str(file_path.relative_to(base_dir)),
                    "target": target_md,
                    "node_id": target,
                    "relative_path": rel_path,
                    "line": line_num,
                    "confidence": confidence,
                }
                if confidence == "HIGH":
                    high_matches.append(match_entry)
                else:
                    medium_matches.append(match_entry)

                # Prepare replacement
                replacement = f"**[{bold_text}]({rel_path})**"
                replacements.append((full_start, full_end, replacement, ""))

            elif match_type == "glossary" and target:
                # target is a glossary slug
                rel_path = _compute_glossary_relative_path(file_path, target)
                match_entry = {
                    "term": bold_text,
                    "file": str(file_path.relative_to(base_dir)),
                    "target": f"../glossary/{target}.html",
                    "slug": target,
                    "relative_path": rel_path,
                    "line": line_num,
                    "confidence": confidence,
                }
                medium_matches.append(match_entry)

                replacement = f"**[{bold_text}]({rel_path})**"
                replacements.append((full_start, full_end, replacement, ""))

        # Apply replacements in reverse order to preserve positions
        if replacements:
            for start, end, replacement, _ in sorted(replacements, key=lambda r: r[0], reverse=True):
                new_line = new_line[:start] + replacement + new_line[end:]

        modified_lines.append(new_line)

    return {
        "file": str(file_path.relative_to(base_dir)),
        "high_matches": high_matches,
        "medium_matches": medium_matches,
        "excluded": excluded,
        "new_content": "\n".join(modified_lines),
        "stats": stats,
    }


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def print_report(
    results: list[dict],
    total_bold: int,
    total_excluded_by_rule: dict[str, int],
) -> None:
    """Print the human-readable linkification report."""
    total_high = sum(len(r["high_matches"]) for r in results)
    total_medium = sum(len(r["medium_matches"]) for r in results)
    total_excluded = sum(total_excluded_by_rule.values())

    print("\n=== Linkification Report ===")
    print(f"Total files scanned: {len(results)}")
    print(f"Total bold instances found: {total_bold}")
    print(f"  EXCLUDED (blockquote metadata): {total_excluded_by_rule.get('blockquote_metadata', 0)}")
    print(f"  EXCLUDED (already linked): {total_excluded_by_rule.get('already_linked', 0)}")
    print(f"  EXCLUDED (label pattern): {total_excluded_by_rule.get('label_pattern', 0)}")
    print(f"  EXCLUDED (code block): {total_excluded_by_rule.get('code_block', 0)}")
    print(f"  EXCLUDED (safety section): {total_excluded_by_rule.get('safety_section', 0)}")
    print(f"  EXCLUDED (cross-domain section): {total_excluded_by_rule.get('cross_domain_section', 0)}")
    print(f"  EXCLUDED (blocklist): {total_excluded_by_rule.get('blocklist', 0)}")
    print(f"  EXCLUDED (single char): {total_excluded_by_rule.get('single_char', 0)}")
    print(f"  EXCLUDED (metadata label): {total_excluded_by_rule.get('metadata_label', 0)}")
    print(f"  HIGH confidence (auto-apply): {total_high}")
    print(f"  MEDIUM confidence (review needed): {total_medium}")

    # Sample HIGH matches (up to 10)
    if total_high:
        print("\nSample HIGH matches:")
        shown = 0
        for r in results:
            for m in r["high_matches"]:
                print(f'  - "{m["term"]}" in {m["file"]} -> {m["target"]}')
                shown += 1
                if shown >= 10:
                    break
            if shown >= 10:
                break

    # Sample MEDIUM matches (up to 10)
    if total_medium:
        print("\nSample MEDIUM matches:")
        shown = 0
        for r in results:
            for m in r["medium_matches"]:
                print(f'  - "{m["term"]}" in {m["file"]} -> {m["target"]}')
                shown += 1
                if shown >= 10:
                    break
            if shown >= 10:
                break


def write_json_report(results: list[dict], report_path: str) -> None:
    """Write JSON report of all matches for agent review."""
    report = {
        "high_matches": [],
        "medium_matches": [],
        "excluded": [],
    }
    for r in results:
        report["high_matches"].extend(r["high_matches"])
        report["medium_matches"].extend(r["medium_matches"])
        report["excluded"].extend(r["excluded"])

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nJSON report written to {report_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Linkify bold terms in Markdown articles against node/glossary vocabulary.",
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--dry-run", action="store_true",
        help="Report matches without modifying files.",
    )
    mode.add_argument(
        "--execute", action="store_true",
        help="Apply linkifications to source files.",
    )
    parser.add_argument(
        "--report", default=None,
        help="Path to write JSON report file.",
    )
    parser.add_argument(
        "--base-dir", default=None,
        help="Base directory (tech-tree-bootstrap root). Auto-detected if omitted.",
    )
    parser.add_argument(
        "--nodes", default=None,
        help="Path to nodes.json (default: data/nodes.json).",
    )
    parser.add_argument(
        "--glossary", default=None,
        help="Path to glossary.json (default: data/glossary.json).",
    )
    parser.add_argument(
        "--docs", default=None,
        help="Path to docs directory (default: docs/).",
    )
    args = parser.parse_args()

    # Resolve base directory
    base_dir = args.base_dir
    if not base_dir:
        # Auto-detect: this script lives in scripts/lib/
        script_dir = Path(__file__).resolve().parent
        base_dir = str(script_dir.parent.parent)  # up from lib/ and scripts/
    base_dir = os.path.abspath(base_dir)

    nodes_path = args.nodes or os.path.join(base_dir, "data", "nodes.json")
    glossary_path = args.glossary or os.path.join(base_dir, "data", "glossary.json")
    docs_dir = args.docs or os.path.join(base_dir, "docs")

    # Validate paths
    for path, label in [(nodes_path, "nodes.json"), (glossary_path, "glossary.json")]:
        if not os.path.exists(path):
            print(f"Error: {label} not found at {path}", file=sys.stderr)
            sys.exit(1)
    if not os.path.isdir(docs_dir):
        print(f"Error: docs directory not found at {docs_dir}", file=sys.stderr)
        sys.exit(1)

    # Load data
    print(f"Loading nodes from {nodes_path} ...")
    nodes_data = load_nodes(nodes_path)
    print(f"  {len(nodes_data['id_to_path'])} nodes loaded")
    print(f"  {len(nodes_data['name_to_id'])} node names indexed")

    print(f"Loading glossary from {glossary_path} ...")
    glossary_terms = load_glossary(glossary_path)
    print(f"  {len(glossary_terms)} glossary terms with definitions indexed")

    # Find article files
    article_files = find_article_files(docs_dir)
    print(f"Found {len(article_files)} article files under {docs_dir}")

    # Process each file
    results: list[dict] = []
    total_bold = 0
    total_excluded_by_rule: dict[str, int] = {
        "blockquote_metadata": 0,
        "already_linked": 0,
        "label_pattern": 0,
        "code_block": 0,
        "safety_section": 0,
        "cross_domain_section": 0,
        "blocklist": 0,
        "single_char": 0,
        "metadata_label": 0,
    }

    for file_path in article_files:
        # Count total bold instances in file
        content = file_path.read_text(encoding="utf-8")
        bold_count = len(BOLD_RE.findall(content))
        total_bold += bold_count

        result = process_file(file_path, base_dir, nodes_data, glossary_terms)
        results.append(result)

        # Aggregate exclusion stats
        for key in total_excluded_by_rule:
            total_excluded_by_rule[key] += result["stats"].get(key, 0)

    # Print report
    print_report(results, total_bold, total_excluded_by_rule)

    # Write JSON report if requested
    if args.report:
        report_abs = os.path.join(base_dir, args.report) if not os.path.isabs(args.report) else args.report
        write_json_report(results, report_abs)

    # Execute mode: write modified files
    if args.execute:
        files_modified = 0
        for r in results:
            if r["high_matches"] or r["medium_matches"]:
                file_path = Path(base_dir) / r["file"]
                file_path.write_text(r["new_content"], encoding="utf-8")
                files_modified += 1
        print(f"\nModified {files_modified} file(s)")

    if args.dry_run:
        print("\n[DRY RUN] No files were modified.")


if __name__ == "__main__":
    main()
