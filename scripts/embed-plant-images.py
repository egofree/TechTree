#!/usr/bin/env python3
"""Embed plant images into species-level markdown articles.

For each species article in docs/plants/ (skipping category articles and index.md),
insert the corresponding image and attribution line after the ## Overview heading.

Usage:
    python3 scripts/embed-plant-images.py
"""

import json
import os
import re
import sys

# Paths relative to project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTS_MD_DIR = os.path.join(PROJECT_ROOT, "docs", "plants")
IMAGES_DIR = os.path.join(PROJECT_ROOT, "docs", "images", "plants")

# Files to skip (category pages + index)
SKIP_FILES = {
    "index.md",
    "edible-plants.md",
    "medicinal-plants.md",
    "fiber-plants.md",
    "structural-plants.md",
    "dye-plants.md",
}

# Preferred extension order
EXT_PRIORITY = [".jpg", ".jpeg", ".png"]


def find_image(slug: str) -> str | None:
    """Find the best image file for a given plant slug. Prefer .jpg > .jpeg > .png."""
    for ext in EXT_PRIORITY:
        path = os.path.join(IMAGES_DIR, f"plants_{slug}{ext}")
        if os.path.isfile(path):
            return f"plants_{slug}{ext}"
    return None


def read_attribution(slug: str) -> dict | None:
    """Read the attribution sidecar JSON for a plant slug."""
    attr_path = os.path.join(IMAGES_DIR, f"plants_{slug}.attribution.json")
    if os.path.isfile(attr_path):
        with open(attr_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def build_attribution_line(attribution: dict, image_filename: str) -> str:
    """Build the markdown attribution line based on license tier."""
    author = attribution.get("author", "Unknown")
    license_name = attribution.get("license", "Unknown")
    tier = attribution.get("license_tier", "libre")

    if tier == "nc":
        slug = image_filename.rsplit(".", 1)[0]  # plants_{slug}
        return (
            f"> *Image: [NC-licensed — see attribution](../images/plants/{slug}.attribution.json). "
            f"{author}, {license_name}*"
        )
    else:
        return f"> *Image: {author}, {license_name}*"


def get_display_name(slug: str, content: str) -> str:
    """Get the display name for alt text from the H1 heading."""
    match = re.search(r"^# (.+)$", content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return slug.replace("-", " ").title()


def embed_image(filepath: str, slug: str) -> tuple[str, str]:
    """Embed image into a plant markdown file.

    Returns: (status, message)
      status: "embedded", "skipped_has_image", "skipped_no_image", "skipped_no_overview", "error"
    """
    # Find image
    image_filename = find_image(slug)
    if not image_filename:
        return "skipped_no_image", f"No image file found for {slug}"

    # Read attribution
    attribution = read_attribution(slug)
    if not attribution:
        return "skipped_no_image", f"No attribution sidecar for {slug}"

    # Read markdown content
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already has an image embed
    if "![" in content:
        return "skipped_has_image", f"{slug} already has an image embed"

    overview_match = re.search(r"^## Overview[ \t]*\n(\n*)", content, re.MULTILINE)
    if not overview_match:
        return "skipped_no_overview", f"{slug} has no ## Overview heading"

    display_name = get_display_name(slug, content)
    image_line = f"![{display_name}](../images/plants/{image_filename})"
    attr_line = build_attribution_line(attribution, image_filename)

    insert_pos = overview_match.end()
    insertion = f"\n{image_line}\n\n{attr_line}\n\n"

    new_content = content[:overview_match.start()] + f"## Overview\n" + insertion + content[insert_pos:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return "embedded", f"Embedded {image_filename} in {slug}.md"


def main():
    stats = {
        "embedded": 0,
        "skipped_has_image": 0,
        "skipped_no_image": 0,
        "skipped_no_overview": 0,
        "error": 0,
        "skipped_category": 0,
    }

    md_files = sorted(f for f in os.listdir(PLANTS_MD_DIR) if f.endswith(".md"))

    for filename in md_files:
        if filename in SKIP_FILES:
            stats["skipped_category"] += 1
            continue

        slug = filename[:-3]  # strip .md
        filepath = os.path.join(PLANTS_MD_DIR, filename)

        status, message = embed_image(filepath, slug)
        stats[status] += 1
        print(f"  [{status}] {message}")

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Embedded:              {stats['embedded']}")
    print(f"  Skipped (has image):   {stats['skipped_has_image']}")
    print(f"  Skipped (no image):    {stats['skipped_no_image']}")
    print(f"  Skipped (no overview): {stats['skipped_no_overview']}")
    print(f"  Skipped (category):    {stats['skipped_category']}")
    print(f"  Errors:                {stats['error']}")
    print(f"  Total files:           {len(md_files)}")

    return 0 if stats["error"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
