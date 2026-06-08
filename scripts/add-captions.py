#!/usr/bin/env python3
"""Add visible captions to embedded article images from attribution sidecars.

For each .md file with an image embed, reads the .attribution.json sidecar's
description field and inserts a caption line between the image and attribution.

Usage:
    python3 scripts/add-captions.py [OPTIONS] [FILE ...]
    python3 scripts/add-captions.py --dry-run docs/machine-tools/laser-welding.md
    python3 scripts/add-captions.py --domain machine-tools
    python3 scripts/add-captions.py   # all docs
"""

import argparse
import json
import re
import sys
from pathlib import Path

RE_IMAGE = re.compile(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$')
RE_ATTRIBUTION = re.compile(r'^>\s*\*Image:')
RE_CAPTION = re.compile(r'^>\s*\*(?!Image:)[^*]+\*\s*$')

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"


def find_attribution_sidecar(image_path: str, md_file: Path) -> Path | None:
    """Locate the .attribution.json sidecar for an image referenced from an .md file.

    image_path is relative to the .md file (e.g. '../images/machine-tools/foo.jpg').
    """
    resolved = (md_file.parent / image_path).resolve()
    if not resolved.exists():
        return None
    stem = resolved.stem
    sidecar = resolved.parent / f"{stem}.attribution.json"
    if sidecar.exists():
        return sidecar
    return None


def load_caption(sidecar: Path) -> str | None:
    """Read description (or title fallback) from attribution sidecar.

    Returns None if both are empty. Flattens multi-line descriptions to a single line.
    """
    try:
        data = json.loads(sidecar.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None

    desc = data.get("description", "").strip()
    if not desc:
        desc = data.get("title", "").strip()
    if not desc:
        return None
    desc = " ".join(desc.split())
    return desc


def process_file(md_path: Path, dry_run: bool = False) -> str:
    """Process a single .md file. Returns status: 'added', 'skipped', 'empty'."""
    try:
        content = md_path.read_text(encoding="utf-8")
    except OSError:
        print(f"  ERROR: Cannot read {md_path}", file=sys.stderr)
        return "skipped"

    lines = content.split("\n")
    insertions = []
    has_empty = False

    i = 0
    while i < len(lines):
        m = RE_IMAGE.match(lines[i])
        if not m:
            i += 1
            continue

        image_path = m.group(2)

        attr_idx = None
        for j in range(i + 1, min(i + 7, len(lines))):
            if RE_ATTRIBUTION.match(lines[j]):
                attr_idx = j
                break

        if attr_idx is None:
            i += 1
            continue

        # Check if a caption already exists between image line and attribution line
        has_caption = False
        for j in range(i + 1, attr_idx):
            stripped = lines[j].strip()
            if stripped == "":
                continue
            if RE_CAPTION.match(lines[j]):
                has_caption = True
                break
            break

        if has_caption:
            i = attr_idx + 1
            continue

        sidecar = find_attribution_sidecar(image_path, md_path)
        if sidecar is None:
            i = attr_idx + 1
            continue

        caption = load_caption(sidecar)
        if caption is None:
            has_empty = True
            i = attr_idx + 1
            continue

        insertions.append((attr_idx, caption))
        i = attr_idx + 1

    if not insertions:
        return "empty" if has_empty else "skipped"

    for attr_idx, caption in reversed(insertions):
        lines.insert(attr_idx, "")
        lines.insert(attr_idx, f"> *{caption}*")

    new_content = "\n".join(lines)
    if dry_run:
        print(f"  [DRY RUN] Would add {len(insertions)} caption(s) to {md_path}")
    else:
        md_path.write_text(new_content, encoding="utf-8")
        print(f"  Added {len(insertions)} caption(s) to {md_path}")

    return "added"


def collect_files(domain: str | None = None) -> list[Path]:
    """Collect .md files to process, optionally filtered by domain."""
    if domain:
        domain_dir = DOCS_DIR / domain
        if not domain_dir.is_dir():
            print(f"ERROR: Domain directory not found: {domain_dir}", file=sys.stderr)
            sys.exit(1)
        return sorted(domain_dir.glob("*.md"))
    else:
        return sorted(DOCS_DIR.rglob("*.md"))


def main():
    parser = argparse.ArgumentParser(
        description="Add visible captions to article images from attribution sidecars"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files",
    )
    parser.add_argument(
        "--domain",
        metavar="DOMAIN",
        help="Only process files in docs/{DOMAIN}/",
    )
    parser.add_argument(
        "files",
        nargs="*",
        metavar="FILE",
        help="Specific .md files to process",
    )
    args = parser.parse_args()

    if args.files:
        files = [Path(f).resolve() for f in args.files]
        for f in files:
            if not f.is_file():
                print(f"ERROR: File not found: {f}", file=sys.stderr)
                sys.exit(1)
    else:
        files = collect_files(args.domain)

    if not files:
        print("No .md files found to process.")
        sys.exit(0)

    print(f"Processing {len(files)} file(s)...\n")

    added = 0
    skipped = 0
    empty = 0

    for f in files:
        result = process_file(f, dry_run=args.dry_run)
        if result == "added":
            added += 1
        elif result == "empty":
            empty += 1
        else:
            skipped += 1

    total_with_images = added + skipped + empty
    print(f"\nAdded captions to {added}/{total_with_images} articles "
          f"({skipped} skipped, {empty} empty description)")


if __name__ == "__main__":
    main()
