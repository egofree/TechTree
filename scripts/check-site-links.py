#!/usr/bin/env python3
"""Fast site link checker — validates every internal href in the built site.

This is the performance-optimized equivalent of the bash check_no_broken_links()
in validate-site.sh.  The original forks a realpath(1) subprocess per href which
becomes intractable once the site exceeds ~1 M links (the glossary alone adds
millions).  This implementation builds an in-memory set of existing paths once
and performs pure lexical normalisation per link, reducing O(links × fork_cost)
to O(links).

Exit codes:  0 = no broken links,  1 = broken links found.
Broken links are printed to stderr in ``BROKEN:file:href`` format.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

SITE_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("site")
HREF_RE = re.compile(rb'href="([^"#]*)"')


def build_existing_set(root: Path) -> set[str]:
    """Return the set of all existing file/dir paths relative to *root*."""
    existing: set[str] = set()
    existing.add("")  # site root
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        if rel_dir == ".":
            rel_dir = ""
        if rel_dir:
            existing.add(rel_dir)
        for name in dirnames:
            p = os.path.join(rel_dir, name) if rel_dir else name
            existing.add(p)
        for name in filenames:
            p = os.path.join(rel_dir, name) if rel_dir else name
            existing.add(p)
    return existing


def normalise(file_rel_dir: str, href: str) -> str | None:
    """Resolve *href* relative to the HTML file's directory, lexically.

    Returns the normalised path relative to SITE_DIR, or None if the href
    is external / unsupported and should be skipped.
    """
    if not href:
        return None
    # Skip non-file schemes
    if href.startswith(("mailto:", "tel:", "javascript:", "data:", "#")):
        return None
    # Skip absolute external URLs
    if "://" in href:
        return None
    if href.startswith("//"):
        return None

    # Absolute path from site root
    if href.startswith("/"):
        combined = href[1:]
    else:
        if file_rel_dir:
            combined = file_rel_dir + "/" + href
        else:
            combined = href

    # Lexical normalisation of . and ..
    parts: list[str] = []
    for segment in combined.split("/"):
        if segment == "" or segment == ".":
            continue
        if segment == "..":
            if parts:
                parts.pop()
            continue
        parts.append(segment)
    return "/".join(parts) if parts else ""


def main() -> int:
    site = SITE_DIR.resolve()
    if not site.is_dir():
        print(f"ERROR: site directory not found: {site}", file=sys.stderr)
        return 2

    existing = build_existing_set(site)
    broken: list[str] = []
    files_checked = 0
    links_checked = 0

    for dirpath, _dirnames, filenames in os.walk(site):
        rel_dir = os.path.relpath(dirpath, site)
        if rel_dir == ".":
            rel_dir = ""
        for name in filenames:
            if not name.endswith(".html"):
                continue
            files_checked += 1
            file_rel = os.path.join(rel_dir, name) if rel_dir else name
            try:
                data = Path(dirpath, name).read_bytes()
            except OSError:
                continue
            for m in HREF_RE.finditer(data):
                href = m.group(1).decode("utf-8", errors="replace")
                links_checked += 1
                norm = normalise(rel_dir, href)
                if norm is None:
                    continue
                if norm not in existing:
                    broken.append(f"BROKEN:{file_rel}:{href}")

    print(f"Files checked: {files_checked}", file=sys.stderr)
    print(f"Links checked: {links_checked}", file=sys.stderr)
    print(f"Broken links:  {len(broken)}", file=sys.stderr)
    for b in broken[:100]:
        print(f"  {b}", file=sys.stderr)
    if len(broken) > 100:
        print(f"  ... and {len(broken) - 100} more", file=sys.stderr)

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
