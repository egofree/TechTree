#!/usr/bin/env python3
"""
validate-images.py - Image integrity validator for tech-tree-bootstrap.

9 validation checks for image files, attribution sidecars, license compliance,
markdown embeds, orphan detection, manifest synchronization, and image relevance.

Usage:
    python3 scripts/validate-images.py [--fix] [--verbose]
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

# --- Paths ---

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DOCS_DIR = PROJECT_DIR / "docs"
IMAGES_DIR = DOCS_DIR / "images"
DATA_DIR = PROJECT_DIR / "data"
IMAGES_JSON = DATA_DIR / "images.json"

IMAGE_EXTENSIONS = frozenset({".jpg", ".jpeg", ".png", ".webp"})
ATTRIBUTION_SUFFIX = ".attribution.json"
REQUIRED_ATTR_FIELDS = [
    "title", "author", "license", "license_url",
    "source_url", "attribution_md", "license_tier",
]
VALID_LICENSE_TIERS = frozenset({"libre", "nc"})
BAD_FORMATS = frozenset({".tiff", ".tif", ".bmp"})

GENERIC_WORDS = frozenset({
    "file", "image", "photo", "commons", "wikimedia", "upload", "default",
    "thumbnail", "icon", "logo", "banner", "placeholder", "dummy",
    "the", "and", "with", "from", "this", "that", "for",
})

RELEVANCE_THRESHOLD = -5


# --- Helpers ---

def find_images(images_dir):
    """Return list of image file Paths under docs/images/."""
    if not images_dir.exists():
        return []
    result = []
    for fpath in sorted(images_dir.rglob("*")):
        if fpath.is_file() and fpath.suffix.lower() in IMAGE_EXTENSIONS:
            result.append(fpath)
    return result


def find_attribution_files(images_dir):
    """Return list of .attribution.json Paths under docs/images/."""
    if not images_dir.exists():
        return []
    result = []
    for fpath in sorted(images_dir.rglob("*")):
        if fpath.is_file() and fpath.name.endswith(ATTRIBUTION_SUFFIX):
            result.append(fpath)
    return result


def image_base_name(fpath):
    """Get the base name for matching (e.g. 'foundations_fire')."""
    return fpath.stem


def attr_base_name(fpath):
    """Get base name from attribution file (strip .attribution.json suffix)."""
    name = fpath.name
    if name.endswith(ATTRIBUTION_SUFFIX):
        return name[: -len(ATTRIBUTION_SUFFIX)]
    return fpath.stem


def find_image_for_attr(attr_path, images):
    """Find an image file matching an attribution file's base name in same dir."""
    base = attr_base_name(attr_path)
    parent = attr_path.parent
    for img in images:
        if img.parent == parent and img.stem == base:
            return img
    return None


def find_attr_for_image(img_path, attr_files):
    """Find an attribution file matching an image file's base name in same dir."""
    base = img_path.stem
    parent = img_path.parent
    expected = parent / (base + ATTRIBUTION_SUFFIX)
    return expected if expected in attr_files else None


def load_json(path):
    """Load JSON file, return dict or None on error."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        return None


def collect_md_image_refs(docs_dir):
    """Scan all .md files under docs/ for ![alt](path) references.

    Returns:
        dict mapping resolved absolute image Path -> list of (md_path, line_number)
    """
    refs = {}
    pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

    for md_path in sorted(docs_dir.rglob("*.md")):
        try:
            text = md_path.read_text(encoding="utf-8")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for match in pattern.finditer(line):
                rel_path = match.group(2).strip()
                # Skip URLs
                if rel_path.startswith(("http://", "https://", "//")):
                    continue
                # Resolve relative to .md file's directory
                resolved = (md_path.parent / rel_path).resolve()
                refs.setdefault(resolved, []).append((md_path, lineno))

    return refs


def check_nc_marking_in_md(image_filename, docs_dir):
    """Check if any .md file references this image AND has NC-licensed or ⚠️ nearby."""
    pattern = re.compile(
        r"(!\[.*?\].*?" + re.escape(image_filename) + r".*?"
        r"(?:NC-licensed|⚠️))",
        re.DOTALL,
    )
    # Also check: image filename mentioned anywhere with NC-licensed or ⚠️
    # within 5 lines of each other
    for md_path in sorted(docs_dir.rglob("*.md")):
        try:
            text = md_path.read_text(encoding="utf-8")
        except OSError:
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if image_filename not in line:
                continue
            # Check surrounding context (±5 lines)
            start = max(0, i - 5)
            end = min(len(lines), i + 6)
            context = "\n".join(lines[start:end])
            if "NC-licensed" in context or "⚠️" in context:
                return True
    return False


# --- Validator ---

class ImageValidator:
    def __init__(self, fix=False, verbose=False):
        self.fix = fix
        self.verbose = verbose
        self.errors = []       # list of (check_num, message)
        self.warnings = []     # list of (check_num, message)
        self.fixes_applied = []

        # Loaded data
        self.images = []           # list of image Paths
        self.attr_files = set()    # set of attribution Paths
        self.images_manifest = {}  # images.json nodes dict

    def load_data(self):
        self.images = find_images(IMAGES_DIR)
        attr_list = find_attribution_files(IMAGES_DIR)
        self.attr_files = set(attr_list)

        if IMAGES_JSON.exists():
            data = load_json(IMAGES_JSON)
            if data and isinstance(data, dict):
                self.images_manifest = data.get("nodes", {})

    # --- Check runners ---

    def _result(self, check_num, name, errors, warnings):
        """Print result for a check."""
        passed = len(errors) == 0
        if passed and len(warnings) == 0:
            print(f"✓ Check {check_num}: {name} — PASS")
        elif passed:
            for w in warnings:
                print(f"⚠ WARNING Check {check_num}: {name} — {w}")
                self.warnings.append((check_num, w))
            print(f"✓ Check {check_num}: {name} — PASS (with warnings)")
        else:
            for e in errors:
                print(f"✗ ERROR Check {check_num}: {name} — {e}")
                self.errors.append((check_num, e))
            for w in warnings:
                print(f"⚠ WARNING Check {check_num}: {name} — {w}")
                self.warnings.append((check_num, w))

        if self.verbose and not passed:
            for e in errors[:10]:
                print(f"    {e}", file=sys.stderr)
            if len(errors) > 10:
                print(
                    f"    ... and {len(errors) - 10} more",
                    file=sys.stderr,
                )

    def check_1_image_existence(self):
        """For every .attribution.json, verify a matching image exists."""
        errors = []
        attr_list = sorted(self.attr_files)
        for attr_path in attr_list:
            img = find_image_for_attr(attr_path, self.images)
            if img is None:
                base = attr_base_name(attr_path)
                rel = attr_path.relative_to(PROJECT_DIR)
                errors.append(f"No image for attribution: {rel} (expected {base}.jpg/png/webp)")
        self._result(1, "Image existence", errors, [])
        return errors

    def check_2_attribution_completeness(self):
        """Every .attribution.json must have required fields."""
        errors = []
        for attr_path in sorted(self.attr_files):
            data = load_json(attr_path)
            if data is None:
                rel = attr_path.relative_to(PROJECT_DIR)
                errors.append(f"Cannot parse: {rel}")
                continue
            missing = [f for f in REQUIRED_ATTR_FIELDS if not data.get(f)]
            if missing:
                rel = attr_path.relative_to(PROJECT_DIR)
                errors.append(f"{rel}: missing fields: {', '.join(missing)}")
        self._result(2, "Attribution completeness", errors, [])
        return errors

    def check_3_license_compliance(self):
        """license_tier must be 'libre' or 'nc'."""
        errors = []
        for attr_path in sorted(self.attr_files):
            data = load_json(attr_path)
            if data is None:
                continue
            tier = data.get("license_tier", "")
            if tier and tier not in VALID_LICENSE_TIERS:
                rel = attr_path.relative_to(PROJECT_DIR)
                errors.append(f"{rel}: invalid license_tier '{tier}'")
        self._result(3, "License compliance", errors, [])
        return errors

    def check_4_nc_marking(self):
        """If license_tier is 'nc', verify NC-licensed or ⚠️ in nearby .md."""
        errors = []
        warnings = []
        for attr_path in sorted(self.attr_files):
            data = load_json(attr_path)
            if data is None:
                continue
            tier = data.get("license_tier", "")
            if tier != "nc":
                continue
            # Find the image filename to search for
            img = find_image_for_attr(attr_path, self.images)
            if img is None:
                # No image yet, can't check marking — skip
                continue
            img_filename = img.name
            if not check_nc_marking_in_md(img_filename, DOCS_DIR):
                rel = attr_path.relative_to(PROJECT_DIR)
                warnings.append(
                    f"{rel}: NC-licensed image '{img_filename}' not marked "
                    f"with 'NC-licensed' or '⚠️' in any .md file"
                )
        self._result(4, "NC marking", errors, warnings)
        return errors

    def check_5_web_formats_only(self):
        """Warn if any .tiff/.bmp files found in docs/images/."""
        warnings = []
        bad_files = []
        if IMAGES_DIR.exists():
            for fpath in sorted(IMAGES_DIR.rglob("*")):
                if fpath.is_file() and fpath.suffix.lower() in BAD_FORMATS:
                    rel = fpath.relative_to(PROJECT_DIR)
                    bad_files.append(str(rel))
        if bad_files:
            for bf in bad_files:
                warnings.append(f"Non-web format: {bf}")
        self._result(5, "Web formats only", [], warnings)
        return []

    def check_6_markdown_embed_resolution(self):
        """For every ![](path) in .md files, verify the image exists."""
        errors = []
        refs = collect_md_image_refs(DOCS_DIR)
        for resolved_path, sources in sorted(refs.items()):
            if not resolved_path.exists():
                for md_path, lineno in sources:
                    md_rel = md_path.relative_to(PROJECT_DIR)
                    errors.append(
                        f"{md_rel}:{lineno}: image not found: {resolved_path}"
                    )
        self._result(6, "Markdown embed resolution", errors, [])
        return errors

    def check_7_orphan_detection(self):
        """Warn if any image has no ![]() reference in any .md file."""
        warnings = []
        refs = collect_md_image_refs(DOCS_DIR)
        referenced_images = set(refs.keys())

        for img_path in self.images:
            resolved = img_path.resolve()
            if resolved not in referenced_images:
                rel = img_path.relative_to(PROJECT_DIR)
                warnings.append(f"Orphan image (no markdown embed): {rel}")
        self._result(7, "Orphan detection", [], warnings)
        return []

    def check_8_manifest_sync(self):
        """Every image should have an entry in data/images.json."""
        errors = []
        warnings = []
        manifest_keys = set(self.images_manifest.keys())

        for img_path in self.images:
            # Convert image filename to manifest key
            # e.g. foundations_fire.jpg -> foundations.fire or foundations_fire
            base = img_path.stem
            # Try dotted version (foundations_fire -> foundations.fire)
            dotted = base.replace("_", ".", 1) if "_" in base else base
            # Also try as-is
            found = base in manifest_keys or dotted in manifest_keys
            if not found:
                # Try domain_sub_sub pattern -> domain.sub.sub
                parts = base.split("_")
                for i in range(1, len(parts)):
                    candidate = parts[0] + "." + "_".join(parts[1:i]) + ("." + "_".join(parts[i:]) if i < len(parts) - 1 else "")
                    # Actually, let's just try common patterns
                    pass
                # Try all possible dot placements
                for i in range(1, len(parts)):
                    candidate = ".".join(["_".join(parts[:i]), "_".join(parts[i:])])
                    if candidate in manifest_keys:
                        found = True
                        break
                    # Also try single dot: first_part.rest
                    if i == 1:
                        candidate2 = parts[0] + "." + "_".join(parts[1:])
                        if candidate2 in manifest_keys:
                            found = True
                            break

            if not found:
                rel = img_path.relative_to(PROJECT_DIR)
                warnings.append(f"Image not in manifest: {rel}")

                if self.fix:
                    # Add stub entry to manifest
                    domain_dir = img_path.parent.name
                    new_key = base.replace("_", ".", 1) if "_" in base else base
                    if new_key not in self.images_manifest:
                        self.images_manifest[new_key] = {
                            "node_name": base.replace("-", " ").replace("_", " "),
                            "domain": domain_dir,
                            "search_queries": [],
                            "status": "untracked",
                            "candidates": [],
                        }
                        self.fixes_applied.append(
                            f"Added to manifest: {new_key}"
                        )

        self._result(8, "Manifest sync", errors, warnings)

        if self.fix and any(
            "Image not in manifest" in w for _, w in self.warnings
            if _ == 8
        ):
            # Save updated manifest
            if IMAGES_JSON.exists():
                data = load_json(IMAGES_JSON)
                if data:
                    data["nodes"] = self.images_manifest
                    with open(IMAGES_JSON, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                        f.write("\n")
                    self.fixes_applied.append("Updated data/images.json")

        return errors

    def _score_relevance(self, article_name, image_title):
        """Score image-title relevance to article name using word-overlap logic.

        Adapted from scripts/source-commons-images.py:score_relevance().
        """
        # Clean image title
        title = image_title
        if title.startswith("File:"):
            title = title[5:]
        title = re.sub(r"\.\w{1,5}$", "", title)
        title_lower = title.lower().replace("_", " ")

        # Tokenize article name and title
        name_lower = article_name.lower()
        name_words = set(re.findall(r"[a-z0-9]+", name_lower))
        title_words = re.findall(r"[a-z0-9]+", title_lower)
        title_word_set = set(title_words)

        score = 0.0

        # +2 per name word found in title; +1 for stem overlap (prefix >= 4 chars)
        for word in name_words:
            if word in title_word_set:
                score += 2.0
            else:
                for tw in title_word_set:
                    overlap = 0
                    for a, b in zip(word, tw):
                        if a == b:
                            overlap += 1
                        else:
                            break
                    if overlap >= 4:
                        score += 1.0
                        break

        # +5 bonus for full name in title
        if name_lower in title_lower:
            score += 5.0

        # -1 per generic word in title
        for word in title_word_set:
            if word in GENERIC_WORDS:
                score -= 1.0

        # -3 for very short titles
        if len(title_words) < 3:
            score -= 3.0

        return score

    def check_9_image_relevance(self):
        """Score image-to-article relevance using word-overlap logic.

        For each .md file with an embedded image, compare the article's H1
        heading against the attribution sidecar's title field. Low scores
        indicate the image may be unrelated to the article content.
        """
        warnings = []
        refs = collect_md_image_refs(DOCS_DIR)

        # Group refs by md_path so we process each article once
        md_to_images = {}
        for resolved_path, sources in refs.items():
            for md_path, lineno in sources:
                md_to_images.setdefault(md_path, []).append(resolved_path)

        for md_path, image_paths in sorted(md_to_images.items()):
            # Extract article name from H1 heading
            try:
                text = md_path.read_text(encoding="utf-8")
            except OSError:
                continue

            h1_match = re.search(r"^#\s+(.+)", text)
            if not h1_match:
                continue
            article_name = h1_match.group(1).strip()

            for img_path in image_paths:
                if not img_path.exists():
                    continue

                # Find attribution sidecar
                attr_path = find_attr_for_image(img_path, self.attr_files)
                if attr_path is None:
                    continue

                attr_data = load_json(attr_path)
                if attr_data is None:
                    continue

                image_title = attr_data.get("title", "")
                if not image_title:
                    continue

                score = self._score_relevance(article_name, image_title)
                if score <= RELEVANCE_THRESHOLD:
                    md_rel = md_path.relative_to(PROJECT_DIR)
                    img_rel = img_path.relative_to(PROJECT_DIR)
                    warnings.append(
                        f"{md_rel}: low relevance score ({score:.0f}) "
                        f"for '{img_rel.name}' (title: '{image_title}')"
                    )

        self._result(9, "Image Relevance", [], warnings)
        return []

    def apply_fixes(self):
        """Apply --fix actions: create stub attribution files."""
        if not self.fix:
            return

        # Create stub .attribution.json for images missing them
        for img_path in self.images:
            attr_path = find_attr_for_image(img_path, self.attr_files)
            if attr_path is None:
                expected_path = img_path.parent / (img_path.stem + ATTRIBUTION_SUFFIX)
                if not expected_path.exists():
                    stub = {field: "" for field in REQUIRED_ATTR_FIELDS}
                    stub["description"] = ""
                    stub["original_url"] = ""
                    with open(expected_path, "w", encoding="utf-8") as f:
                        json.dump(stub, f, indent=2, ensure_ascii=False)
                        f.write("\n")
                    rel = expected_path.relative_to(PROJECT_DIR)
                    self.fixes_applied.append(f"Created stub: {rel}")

    # --- Main runner ---

    def run(self):
        t0 = time.time()

        self.load_data()

        if self.verbose:
            print(
                f"Loaded {len(self.images)} images, "
                f"{len(self.attr_files)} attribution files, "
                f"{len(self.images_manifest)} manifest entries"
            )

        print("=== Image Validation ===")
        print()

        # Apply fixes first (create stubs before checking)
        if self.fix:
            self.apply_fixes()
            # Reload after fixes
            self.load_data()

        # Run 9 checks
        self.check_1_image_existence()
        self.check_2_attribution_completeness()
        self.check_3_license_compliance()
        self.check_4_nc_marking()
        self.check_5_web_formats_only()
        self.check_6_markdown_embed_resolution()
        self.check_7_orphan_detection()
        self.check_8_manifest_sync()
        self.check_9_image_relevance()

        # ---- Summary ----
        print()

        all_errors = self.errors
        all_warnings = self.warnings

        if all_errors:
            print(
                f"Result: {len(all_errors)} ERROR"
                f"{'S' if len(all_errors) != 1 else ''}"
            )
            for check_num, msg in all_errors[:10]:
                print(f"  ✗ [Check {check_num}] {msg}")
            if len(all_errors) > 10:
                print(f"  ... and {len(all_errors) - 10} more")
        else:
            print(f"Result: ALL PASS (0 errors)")

        if all_warnings:
            print(
                f"Warnings: {len(all_warnings)}"
            )
            if self.verbose:
                for check_num, msg in all_warnings[:10]:
                    print(f"  ⚠ [Check {check_num}] {msg}")

        if self.fixes_applied:
            print()
            print(f"Fixes applied ({len(self.fixes_applied)}):")
            for fix in self.fixes_applied:
                print(f"  + {fix}")

        elapsed = time.time() - t0
        if self.verbose:
            print(f"\nCompleted in {elapsed:.1f}s")

        return 1 if all_errors else 0


def main():
    parser = argparse.ArgumentParser(
        description="Validate image integrity for tech-tree-bootstrap"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Create stub attribution files and update manifest for untracked images",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show per-check detail",
    )
    args = parser.parse_args()

    validator = ImageValidator(fix=args.fix, verbose=args.verbose)
    sys.exit(validator.run())


if __name__ == "__main__":
    main()
