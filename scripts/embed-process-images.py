#!/usr/bin/env python3
"""Embed process images into article markdown files.

Scans docs/images/{domain}/ for image files, maps each to its corresponding
docs/{domain}/{article}.md file, and inserts the image + attribution after
the ## Overview heading.

Usage:
    python3 scripts/embed-process-images.py [--dry-run]
"""

import json
import os
import re
import sys

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
IMAGES_DIR = os.path.join(DOCS_DIR, "images")

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
EXT_PRIORITY = {".jpg": 0, ".jpeg": 1, ".png": 2, ".webp": 3}

# Stats
embedded = 0
skipped_no_doc = 0
skipped_has_image = 0
errors = 0
dry_run = "--dry-run" in sys.argv


def find_doc_for_image(domain: str, rest: str) -> str | None:
    """Given domain and rest-of-filename (after stripping domain prefix),
    find the corresponding .md doc file. Returns the path or None."""
    
    candidates = []
    
    # 1. Full rest as filename: docs/{domain}/{rest}.md
    candidates.append(os.path.join(DOCS_DIR, domain, f"{rest}.md"))
    
    # 2. Full rest with underscores→hyphens: docs/{domain}/{rest-hyphen}.md
    rest_hyphen = rest.replace("_", "-")
    if rest_hyphen != rest:
        candidates.append(os.path.join(DOCS_DIR, domain, f"{rest_hyphen}.md"))
    
    # 3. Split on underscores and try subdirectory paths
    # e.g., for "pottery_kiln-firing", try:
    #   docs/{domain}/pottery/kiln-firing.md
    #   docs/{domain}/pottery-kiln-firing.md (with hyphens)
    parts = rest.split("_")
    if len(parts) >= 2:
        # Try each split point for subdirectory structure
        for i in range(1, len(parts)):
            sub = "_".join(parts[:i])
            article = "_".join(parts[i:])
            sub_hyphen = sub.replace("_", "-")
            article_hyphen = article.replace("_", "-")
            
            # subdir/article
            candidates.append(os.path.join(DOCS_DIR, domain, sub, f"{article}.md"))
            # subdir-hyphen/article-hyphen
            candidates.append(os.path.join(DOCS_DIR, domain, sub_hyphen, f"{article_hyphen}.md"))
            # subdir/article-hyphen
            if article_hyphen != article:
                candidates.append(os.path.join(DOCS_DIR, domain, sub, f"{article_hyphen}.md"))
            # subdir-hyphen/article
            if sub_hyphen != sub:
                candidates.append(os.path.join(DOCS_DIR, domain, sub_hyphen, f"{article}.md"))
    
    # 4. Just the last segment
    last_part = parts[-1]
    candidates.append(os.path.join(DOCS_DIR, domain, f"{last_part}.md"))
    last_hyphen = last_part.replace("_", "-")
    if last_hyphen != last_part:
        candidates.append(os.path.join(DOCS_DIR, domain, f"{last_hyphen}.md"))
    
    # Return first candidate that exists
    for c in candidates:
        if os.path.isfile(c):
            return c
    
    return None


def read_attribution(attribution_path: str) -> dict:
    """Read attribution sidecar JSON, returns empty dict if missing."""
    try:
        with open(attribution_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def build_image_block(domain: str, filename: str, title: str, attr: dict) -> str:
    """Build the markdown image + attribution block."""
    img_path = f"../images/{domain}/{filename}"
    author = attr.get("author", "Unknown")
    license_name = attr.get("license", "Unknown")
    license_tier = attr.get("license_tier", "libre")
    
    if license_tier == "nc":
        attr_filename = os.path.splitext(filename)[0] + ".attribution.json"
        block = (
            f"![{title}]({img_path})\n"
            f"\n"
            f"> *Image: [NC-licensed — see attribution](../images/{domain}/{attr_filename}). {author}, {license_name}*\n"
        )
    else:
        block = (
            f"![{title}]({img_path})\n"
            f"\n"
            f"> *Image: {author}, {license_name}*\n"
        )
    
    return block


def insert_image_after_heading(content: str, image_block: str) -> str | None:
    """Insert image_block after ## Overview heading, or first ## heading.
    Returns new content or None if no heading found."""
    
    lines = content.split("\n")
    
    # Find ## Overview first
    heading_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## Overview":
            heading_idx = i
            break
    
    # Fallback: first ## heading (but not the title # heading)
    if heading_idx is None:
        for i, line in enumerate(lines):
            if line.startswith("## ") and not line.startswith("### "):
                heading_idx = i
                break
    
    if heading_idx is None:
        return None
    
    # Find where to insert: after the heading and any blank lines immediately following
    insert_idx = heading_idx + 1
    
    # Skip blank lines right after heading
    while insert_idx < len(lines) and lines[insert_idx].strip() == "":
        insert_idx += 1
    
    # Insert the image block before the first content line after heading
    # The image block already has newlines
    image_lines = image_block.rstrip("\n").split("\n")
    
    # Build new content
    new_lines = lines[:heading_idx + 1]
    new_lines.append("")  # blank line after heading
    new_lines.extend(image_lines)
    new_lines.append("")  # blank line after attribution
    new_lines.extend(lines[insert_idx:])
    
    return "\n".join(new_lines)


def process_images():
    """Main processing loop."""
    global embedded, skipped_no_doc, skipped_has_image, errors
    
    # Collect all image files grouped by (domain, article_key)
    # article_key = filename without extension, after stripping domain prefix
    # We prefer .jpg > .jpeg > .png > .webp
    
    image_map = {}  # (domain, rest) -> (full_path, ext)
    
    for domain in sorted(os.listdir(IMAGES_DIR)):
        domain_img_dir = os.path.join(IMAGES_DIR, domain)
        if not os.path.isdir(domain_img_dir):
            continue
        if domain == "plants":
            continue
        
        prefix = domain + "_"
        
        for fname in sorted(os.listdir(domain_img_dir)):
            ext = os.path.splitext(fname)[1].lower()
            if ext not in IMAGE_EXTENSIONS:
                continue
            
            # Strip domain prefix
            base = os.path.splitext(fname)[0]
            if not base.startswith(prefix):
                # Domain-level overview image (e.g., energy.jpg) — skip
                continue
            
            rest = base[len(prefix):]
            if not rest:
                # Domain-level overview image — skip
                skipped_no_doc += 1
                continue
            
            key = (domain, rest)
            full_path = os.path.join(domain_img_dir, fname)
            
            if key not in image_map or EXT_PRIORITY.get(ext, 99) < EXT_PRIORITY.get(image_map[key][1], 99):
                image_map[key] = (full_path, ext)
    
    # Track docs already processed in this run to avoid duplicate images
    processed_docs = set()
    
    # Process each image→doc mapping
    for (domain, rest), (img_path, ext) in sorted(image_map.items()):
        fname = os.path.basename(img_path)
        
        # Find corresponding doc
        doc_path = find_doc_for_image(domain, rest)
        if doc_path is None:
            skipped_no_doc += 1
            print(f"  SKIP (no doc): {img_path}")
            continue
        
        # Skip if we already embedded an image for this doc in this run
        doc_abs = os.path.abspath(doc_path)
        if doc_abs in processed_docs:
            skipped_has_image += 1
            continue
        
        # Read doc content
        try:
            with open(doc_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            errors += 1
            print(f"  ERROR reading {doc_path}: {e}")
            continue
        
        # Check if already has image embed (pre-existing in file)
        if re.search(r"!\[", content):
            skipped_has_image += 1
            processed_docs.add(doc_abs)
            continue
        
        # Read attribution
        attr_path = os.path.splitext(img_path)[0] + ".attribution.json"
        attr = read_attribution(attr_path)
        
        title = attr.get("title", os.path.splitext(fname)[0])
        
        # Build image block
        image_block = build_image_block(domain, fname, title, attr)
        
        # Insert after heading
        new_content = insert_image_after_heading(content, image_block)
        if new_content is None:
            errors += 1
            print(f"  ERROR (no heading in {doc_path})")
            continue
        
        if dry_run:
            print(f"  WOULD EMBED: {fname} -> {os.path.relpath(doc_path, DOCS_DIR)}")
        else:
            with open(doc_path, "w", encoding="utf-8") as f:
                f.write(new_content)
        
        embedded += 1
        processed_docs.add(doc_abs)
    
    # Print summary
    print()
    print("=" * 60)
    print(f"  Embedded: {embedded}")
    print(f"  Skipped (no doc): {skipped_no_doc}")
    print(f"  Skipped (already has image): {skipped_has_image}")
    print(f"  Errors: {errors}")
    print("=" * 60)
    
    if dry_run:
        print("  (DRY RUN - no files were modified)")


if __name__ == "__main__":
    process_images()
