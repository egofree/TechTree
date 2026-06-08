#!/usr/bin/env python3
"""Remove image embeds and attribution blockquotes from markdown articles.

For each specified .md file, finds the ![...]() image line and the
> *Image: ...* attribution line (within ±5 lines), then removes both
plus any blank lines between them.

Usage:
    python3 scripts/unembed-images.py [FILE ...]
    python3 scripts/unembed-images.py --list bad-images.json
    python3 scripts/unembed-images.py --dry-run docs/machine-tools/laser-welding.md
"""

import argparse
import json
import os
import re
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Regex for the image embed line: ![alt](../images/...)
RE_IMAGE = re.compile(r"^!\[.*?\]\(\.\./images/.*\)\s*$")

# Regex for the attribution blockquote line (both libre and NC formats)
RE_ATTR = re.compile(r"^> \*Image:.*\*\s*$")


def unembed_file(filepath: str, dry_run: bool = False) -> tuple[str, str]:
    """Remove image embed + attribution from a single markdown file.

    Returns: (status, message)
      status: "unembedded", "skipped_no_image", "error"
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, IOError) as e:
        return "error", f"Cannot read {filepath}: {e}"

    lines = content.split("\n")

    # Find the image line
    image_idx = None
    for i, line in enumerate(lines):
        if RE_IMAGE.match(line):
            image_idx = i
            break

    if image_idx is None:
        return "skipped_no_image", f"No image embed found in {filepath}"

    # Find the attribution line within ±5 lines of the image
    attr_idx = None
    search_start = max(0, image_idx - 5)
    search_end = min(len(lines), image_idx + 6)  # +6 to include 5 lines after
    for i in range(search_start, search_end):
        if RE_ATTR.match(lines[i]):
            attr_idx = i
            break

    if attr_idx is None:
        return "skipped_no_image", f"No attribution blockquote found near image in {filepath}"

    # Determine the range of lines to remove (image + attribution + blank lines between)
    start = min(image_idx, attr_idx)
    end = max(image_idx, attr_idx)

    # Extend to include blank lines immediately before/after the block
    while start > 0 and lines[start - 1].strip() == "":
        start -= 1
    while end < len(lines) - 1 and lines[end + 1].strip() == "":
        end += 1

    # Remove the lines
    removed = lines[start : end + 1]
    new_lines = lines[:start] + lines[end + 1 :]
    new_content = "\n".join(new_lines)

    if dry_run:
        print(f"  [dry-run] Would remove {end - start + 1} lines from {filepath}:")
        for r in removed:
            print(f"    | {r}" if r.strip() else "    | <blank>")
        return "unembedded", f"[dry-run] {filepath}"

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
    except (OSError, IOError) as e:
        return "error", f"Cannot write {filepath}: {e}"

    return "unembedded", f"Unembedded {filepath}"


def collect_files(args: argparse.Namespace) -> list[str]:
    """Collect file paths from positional args and/or --list file."""
    files = []

    for path in args.files:
        abspath = os.path.abspath(path)
        if not os.path.isfile(abspath):
            print(f"Warning: {path} not found, skipping", file=sys.stderr)
            continue
        files.append(abspath)

    if args.list:
        list_path = os.path.abspath(args.list)
        if not os.path.isfile(list_path):
            print(f"Error: --list file {args.list} not found", file=sys.stderr)
            sys.exit(1)
        try:
            with open(list_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Error reading --list file: {e}", file=sys.stderr)
            sys.exit(1)

        # Support multiple formats:
        # - plain list of paths: ["path1.md", "path2.md"]
        # - {"files": [...]}: explicit file list
        # - {"bad_images": [{doc_path: "..."}, ...]}: bad-images.json manifest format
        if isinstance(data, list):
            paths = data
        elif isinstance(data, dict) and "files" in data:
            paths = data["files"]
        elif isinstance(data, dict) and "bad_images" in data:
            paths = [e["doc_path"] for e in data["bad_images"]]
        else:
            print("Error: --list file must be a JSON array, {\"files\": [...]}, or {\"bad_images\": [...]}", file=sys.stderr)
            sys.exit(1)

        for p in paths:
            # Paths may be relative to project root
            abs_p = os.path.join(PROJECT_ROOT, p) if not os.path.isabs(p) else p
            if os.path.isfile(abs_p):
                files.append(abs_p)
            else:
                print(f"Warning: {p} from list not found, skipping", file=sys.stderr)

    return files


def main():
    parser = argparse.ArgumentParser(
        description="Remove image embeds and attribution blockquotes from markdown files."
    )
    parser.add_argument("files", nargs="*", help="Markdown files to process")
    parser.add_argument("--list", metavar="FILE",
                        help="JSON file with list of paths to process")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be removed without modifying files")
    args = parser.parse_args()

    if not args.files and not args.list:
        parser.error("No files specified. Provide file paths or --list FILE.")

    files = collect_files(args)
    if not files:
        print("No valid files to process.", file=sys.stderr)
        return 1

    stats = {"unembedded": 0, "skipped_no_image": 0, "error": 0}

    for filepath in files:
        status, message = unembed_file(filepath, dry_run=args.dry_run)
        stats[status] += 1
        label = "dry-run" if args.dry_run and status == "unembedded" else status
        print(f"  [{label}] {message}")

    total = len(files)
    unembedded = stats["unembedded"]
    print()
    print(f"Unembedded {unembedded}/{total} articles")

    return 0 if stats["error"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
