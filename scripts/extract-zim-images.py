#!/usr/bin/env python3
"""Extract plant images from edibleplantdb.zim with EXACT MATCH ONLY safety.

Reads data/plants.json species list, matches to ZIM entries by exact slug
match (id field), parses HTML for image metadata, applies tiered license
filtering, and extracts images via zimdump subprocess.

Requires: Python 3.8+ (stdlib only), zimdump binary on PATH
Usage:
    python scripts/extract-zim-images.py --dry-run
    python scripts/extract-zim-images.py --node wheat
    python scripts/extract-zim-images.py --zim /path/to/edibleplantdb.zim
"""

import argparse
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
PLANTS_FILE = DATA_DIR / "plants.json"
NAME_MAP_FILE = DATA_DIR / "plant-name-map.json"
IMAGES_DIR = PROJECT_DIR / "docs" / "images" / "plants"
EVIDENCE_DIR = PROJECT_DIR / ".omo" / "evidence"

DEFAULT_ZIM = Path.home() / "Downloads" / "edibleplantdb.zim"

LIBRE_LICENSES = {"cc0", "public domain", "cc by", "cc by-sa"}
NC_LICENSES = {"cc by-nc", "cc by-nc-sa", "cc by-nd", "cc by-nc-nd"}

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


# ---------------------------------------------------------------------------
# ZIM helpers
# ---------------------------------------------------------------------------

def zim_list(zim_path):
    """List all entries in the ZIM file, return stdout text."""
    result = subprocess.run(
        ["zimdump", "list", str(zim_path)],
        capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        print("ERROR: zimdump list failed: {}".format(result.stderr.strip()),
              file=sys.stderr)
        sys.exit(1)
    return result.stdout


def zim_show(zim_path, url):
    """Fetch a single entry from the ZIM file, return raw bytes."""
    result = subprocess.run(
        ["zimdump", "show", "--url={}".format(url), str(zim_path)],
        capture_output=True, timeout=60,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def build_slug_map(zim_path):
    """Build mapping from slug -> full ZIM URL for plant pages."""
    raw = zim_list(zim_path)
    slug_map = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line.startswith("plants/"):
            continue
        parts = line.split("/")
        if len(parts) != 3:
            continue
        slug = parts[2]
        if slug not in slug_map:
            slug_map[slug] = line
    return slug_map


# ---------------------------------------------------------------------------
# HTML parsing
# ---------------------------------------------------------------------------

class PhotoGridParser(HTMLParser):
    """Parse ZIM plant pages to extract image metadata from photo-grid."""

    def __init__(self):
        super().__init__()
        self.title_text = ""
        self.h1_text = ""
        self.in_title = False
        self.in_h1 = False
        self.images = []  # list of dicts: {filename, license, author, source}
        self._in_photo_grid = False
        self._current_img_src = None
        self._in_caption = False
        self._caption_text = ""
        self._in_span_in_caption = False
        self._span_text = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "title":
            self.in_title = True
            return
        if tag == "h1":
            self.in_h1 = True
            return
        cls = attrs_dict.get("class", "")
        if "photo-grid" in cls:
            self._in_photo_grid = True
            return
        if self._in_photo_grid and tag == "img":
            src = attrs_dict.get("src", "")
            # src is like ../../images/filename.jpg
            filename = src.rsplit("/", 1)[-1] if "/" in src else src
            self._current_img_src = filename
            return
        if self._in_photo_grid and tag == "div" and "caption" in cls:
            self._in_caption = True
            self._caption_text = ""
            return
        if self._in_caption and tag == "span":
            self._in_span_in_caption = True
            self._span_text = ""
            return

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
            return
        if tag == "h1":
            self.in_h1 = False
            return
        if tag == "span" and self._in_span_in_caption:
            self._in_span_in_caption = False
            self._caption_text += self._span_text
            return
        if tag == "div" and self._in_caption:
            self._in_caption = False
            if self._current_img_src:
                img_info = parse_caption(
                    self._current_img_src, self._caption_text
                )
                if img_info:
                    self.images.append(img_info)
            self._current_img_src = None
            self._caption_text = ""
            return

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data
        if self.in_h1:
            self.h1_text += data
        if self._in_span_in_caption:
            self._span_text += data
        elif self._in_caption:
            self._caption_text += data


def parse_caption(filename, caption_text):
    """Parse caption text to extract license, author, source.

    Caption format examples:
      iNaturalist · CC-BY-NC-SA
      (c) Reiner Richter, some rights reserved (CC BY-NC-SA), uploaded by Reiner Richter
      GBIF · CC-BY
      Wikimedia Commons · CC-BY-SA
    """
    caption_lower = caption_text.lower().strip()

    source = ""
    for s in ("inaturalist", "gbif", "wikimedia commons"):
        if s in caption_lower:
            if s == "inaturalist":
                source = "iNaturalist"
            elif s == "gbif":
                source = "GBIF"
            else:
                source = "Wikimedia Commons"
            break

    license_str = ""
    cc_match = re.search(
        r"(cc[- ]by(?:[- ](?:nc|sa|nd|nc[- ]sa|nc[- ]nd))?"
        r"(?:\s*\d\.\d)?"
        r"|cc0|public[- ]domain)",
        caption_lower,
    )
    if cc_match:
        raw = cc_match.group(0)
        license_str = normalize_license(raw)

    if not license_str:
        return None

    author = ""
    author_match = re.search(
        r"\(c\)\s*([^,<(]+?)(?:\s*,\s*some rights reserved|\s*\(|\s*$)",
        caption_text,
    )
    if author_match:
        author = author_match.group(1).strip()

    return {
        "filename": filename,
        "license": license_str,
        "author": author,
        "source": source,
    }


def normalize_license(raw):
    """Normalize a raw license string to canonical form like 'CC BY-NC 4.0'."""
    low = raw.lower().replace("-", " ").strip()
    if low in ("cc0", "public domain"):
        return low.upper() if low == "cc0" else "Public Domain"

    version_suffix = ""
    ver_match = re.search(r"(\d\.\d)$", low)
    if ver_match:
        version_suffix = " " + ver_match.group(1)
        low = low[: ver_match.start()].strip()
    else:
        version_suffix = " 4.0"

    parts = low.replace("  ", " ").split(" ")
    modifiers = []
    i = 2
    while i < len(parts):
        p = parts[i].strip()
        if p in ("nc", "sa", "nd"):
            modifiers.append(p.upper())
        i += 1

    if modifiers:
        return "CC BY-{}{}".format("-".join(modifiers), version_suffix)
    return "CC BY{}".format(version_suffix)


def parse_zim_page(html_bytes):
    """Parse ZIM HTML page, return (title, h1, images_list)."""
    try:
        html_text = html_bytes.decode("utf-8", errors="replace")
    except (AttributeError, UnicodeDecodeError):
        return "", "", []

    parser = PhotoGridParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass

    return parser.title_text, parser.h1_text, parser.images


# ---------------------------------------------------------------------------
# License tier classification
# ---------------------------------------------------------------------------

def license_tier(license_str):
    """Return 'libre', 'nc', or None based on license string."""
    if not license_str:
        return None
    low = license_str.lower()
    if low.startswith("cc0") or "public domain" in low:
        return "libre"
    if low.startswith("cc by-nc") or low.startswith("cc by-nd"):
        return "nc"
    if low.startswith("cc by-sa") or low.startswith("cc by "):
        return "libre"
    return None


def license_url(license_str):
    """Generate Creative Commons license URL from canonical name."""
    low = license_str.lower()
    if low.startswith("cc0"):
        return "https://creativecommons.org/publicdomain/zero/1.0"
    if "public domain" in low:
        return "https://creativecommons.org/publicdomain/mark/1.0"

    m = re.match(r"cc by(-[\w-]+)?\s+(\d\.\d)", low)
    if m:
        modifier = m.group(1) or ""
        version = m.group(2)
        if modifier:
            return "https://creativecommons.org/licenses/by{}/{}".format(
                modifier, version
            )
        return "https://creativecommons.org/licenses/by/{}".format(version)

    m = re.match(r"cc by(-[\w-]+)?$", low)
    if m:
        modifier = m.group(1) or ""
        if modifier:
            return "https://creativecommons.org/licenses/by{}/4.0".format(
                modifier
            )
        return "https://creativecommons.org/licenses/by/4.0"
    return ""


def select_best_image(images):
    """Select best image using tiered license preference.

    Returns (image_dict, tier_str) or (None, None).
    """
    libre_imgs = []
    nc_imgs = []

    for img in images:
        ext = Path(img["filename"]).suffix.lower()
        if ext not in ALLOWED_EXTENSIONS:
            continue
        tier = license_tier(img["license"])
        if tier == "libre":
            libre_imgs.append(img)
        elif tier == "nc":
            nc_imgs.append(img)

    if libre_imgs:
        return libre_imgs[0], "libre"
    if nc_imgs:
        return nc_imgs[0], "nc"
    return None, None


# ---------------------------------------------------------------------------
# Title verification (safety check)
# ---------------------------------------------------------------------------

def title_matches(expected_title, zim_title, zim_h1, species_id="", zim_slug=""):
    """Verify ZIM page title is consistent with expected species.

    Checks that words from the expected title OR the species id (scientific
    name slug) OR the mapped ZIM slug appear in the ZIM <title> or <h1>.
    This handles both cases: title="Agrimonia pilosa" (scientific) and
    title="Scots Pine" (common) where id="pinus-sylvestris" maps to
    ZIM h1="Pinus sylvestris", and also name-mapped entries like
    "wheat" → zim_slug="triticum-aestivum".
    """
    combined = (zim_title + " " + zim_h1).lower()

    title_words = set(re.findall(r"[a-zA-Z]+", expected_title.lower()))
    id_words = set(re.findall(r"[a-zA-Z]+", species_id.lower()))
    slug_words = set(re.findall(r"[a-zA-Z]+", zim_slug.lower()))
    all_words = title_words | id_words | slug_words

    if not all_words:
        return False

    matched = sum(1 for w in all_words if w in combined)
    # Require at least half the words to match, minimum 1
    threshold = max(1, len(all_words) // 2)
    return matched >= threshold


# ---------------------------------------------------------------------------
# Name map (manual overrides)
# ---------------------------------------------------------------------------

def load_name_map():
    """Load plant-name-map.json if it exists, return flat {id: zim_slug} dict."""
    if not NAME_MAP_FILE.exists():
        return {}
    try:
        data = json.loads(NAME_MAP_FILE.read_text(encoding="utf-8"))
        return {m["plants_json_id"]: m["zim_species_name"]
                for m in data.get("mappings", [])}
    except (json.JSONDecodeError, OSError):
        return {}


# ---------------------------------------------------------------------------
# Existing images check
# ---------------------------------------------------------------------------

def find_existing_images():
    """Return set of species IDs that already have images in docs/images/plants/."""
    existing = set()
    if not IMAGES_DIR.exists():
        return existing
    for p in IMAGES_DIR.iterdir():
        name = p.name
        # Match both plants_{id}.{ext} and plants_{category}_{id}.{ext}
        # Strip prefix and extension
        if name.startswith("plants_"):
            stem = p.stem  # plants_{id} or plants_{category}_{id}
            # Remove 'plants_' prefix
            rest = stem[len("plants_"):]
            ext = p.suffix.lower()
            if ext in ALLOWED_EXTENSIONS or ext == ".json":
                # Could be "edible-plants_agave" or just "agave"
                parts = rest.rsplit("_", 1)
                if len(parts) == 2:
                    # Last part is the species id if it doesn't look like a category
                    candidate = parts[1]
                    # Check if it looks like a species id (lowercase, no "-plants" suffix)
                    if not candidate.endswith("-plants"):
                        existing.add(candidate)
                else:
                    existing.add(rest)
    return existing


# ---------------------------------------------------------------------------
# Attribution
# ---------------------------------------------------------------------------

def build_attribution(species, img, tier_str):
    """Build attribution sidecar dict."""
    license_str = img.get("license", "")
    lurl = license_url(license_str)
    author = img.get("author", "")
    source = img.get("source", "")
    species_title = species.get("title", species["id"])

    # Build source_url from source type
    source_url = ""
    filename = img.get("filename", "")
    if source == "iNaturalist":
        source_url = "https://www.inaturalist.org"
    elif source == "GBIF":
        source_url = "https://www.gbif.org"
    elif source == "Wikimedia Commons":
        slug = Path(filename).stem.replace("-", "_")
        source_url = "https://commons.wikimedia.org/wiki/File:{}".format(
            slug + Path(filename).suffix
        )

    # Build attribution markdown
    attr_lines = []
    attr_lines.append(species_title)
    attr_lines.append("")
    if author and source_url:
        attr_lines.append(
            "Image: {} ([source]({}))".format(author, source_url)
        )
    elif source_url:
        attr_lines.append("Image: [{}]({})".format(source, source_url))
    if license_str:
        if lurl:
            attr_lines.append(
                "License: [{}]({})".format(license_str, lurl)
            )
        else:
            attr_lines.append("License: {}".format(license_str))
    attribution_md = "\n".join(attr_lines)

    return {
        "title": species_title,
        "description": "",
        "author": author,
        "license": license_str,
        "license_url": lurl,
        "source_url": source_url,
        "original_url": "",
        "attribution_md": attribution_md,
        "license_tier": tier_str,
    }


def write_attribution(attr, image_path):
    """Write attribution sidecar JSON file."""
    attr_path = image_path.with_suffix(".attribution.json")
    attr_path.write_text(
        json.dumps(attr, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return attr_path


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def process_species(species, zim_path, slug_map, name_map, existing_ids,
                    dry_run, stats):
    """Process one species from plants.json.

    Returns status string for dry-run reporting.
    """
    species_id = species["id"]
    species_title = species.get("title", species_id)

    # Check for existing image (any extension)
    if species_id in existing_ids:
        stats["skip_existing"] += 1
        return "SKIP", "image already exists"

    # Resolve ZIM slug: check name_map first, then direct id match
    zim_slug = name_map.get(species_id, species_id)
    zim_url = slug_map.get(zim_slug)
    if zim_url is None:
        # Try direct id as-is
        zim_url = slug_map.get(species_id)
    if zim_url is None:
        stats["no_match"] += 1
        return "SKIP", "no ZIM page found for '{}'".format(zim_slug)

    # Fetch ZIM page
    html_bytes = zim_show(zim_path, zim_url)
    if html_bytes is None:
        stats["no_match"] += 1
        return "SKIP", "ZIM page read failed for '{}'".format(zim_url)

    # Parse HTML
    page_title, page_h1, images = parse_zim_page(html_bytes)

    # Safety: verify title contains expected words
    if not title_matches(species_title, page_title, page_h1, species_id, zim_slug):
        stats["mismatch"] += 1
        return "MISMATCH", "ZIM title mismatch: expected '{}', got '{}'".format(
            species_title, page_title
        )

    if not images:
        stats["no_images"] += 1
        return "SKIP", "no images on ZIM page"

    # Select best image by license tier
    best_img, tier_str = select_best_image(images)
    if best_img is None:
        stats["no_images"] += 1
        return "SKIP", "no images with recognized license"

    # Count tiers for reporting
    for img in images:
        t = license_tier(img.get("license", ""))
        if t == "libre":
            stats["libre_count"] += 1
        elif t == "nc":
            stats["nc_count"] += 1

    if dry_run:
        stats["matched"] += 1
        if tier_str == "libre":
            stats["libre_selected"] += 1
        else:
            stats["nc_selected"] += 1
        return "MATCH", "{} ({})".format(zim_url, tier_str)

    # Extract image
    img_filename = best_img["filename"]
    img_zim_url = "images/{}".format(img_filename)
    img_bytes = zim_show(zim_path, img_zim_url)
    if img_bytes is None:
        stats["no_images"] += 1
        return "SKIP", "image extraction failed for '{}'".format(img_zim_url)

    # Determine output path
    ext = Path(img_filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        stats["no_images"] += 1
        return "SKIP", "disallowed image format '{}'".format(ext)

    out_name = "plants_{}{}".format(species_id, ext)
    out_path = IMAGES_DIR / out_name

    # Double-check no overwrite
    if out_path.exists():
        stats["skip_existing"] += 1
        return "SKIP", "output file already exists"

    # Write image
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(img_bytes)

    # Write attribution sidecar
    attr = build_attribution(species, best_img, tier_str)
    write_attribution(attr, out_path)

    stats["extracted"] += 1
    return "EXTRACTED", out_name


def main():
    parser = argparse.ArgumentParser(
        description="Extract plant images from edibleplantdb.zim "
                    "with EXACT MATCH ONLY safety"
    )
    parser.add_argument(
        "--dry-run", action="store_true", default=False,
        help="Report matches only, do not extract images",
    )
    parser.add_argument(
        "--node", dest="node_id", default=None,
        help="Process only one species by id field",
    )
    parser.add_argument(
        "--zim", type=str, default=None,
        help="Path to edibleplantdb.zim (default: ~/Downloads/edibleplantdb.zim)",
    )
    args = parser.parse_args()

    zim_path = Path(args.zim) if args.zim else DEFAULT_ZIM
    if not zim_path.exists():
        print("ERROR: ZIM file not found: {}".format(zim_path), file=sys.stderr)
        sys.exit(1)

    if not PLANTS_FILE.exists():
        print("ERROR: plants.json not found: {}".format(PLANTS_FILE),
              file=sys.stderr)
        sys.exit(1)

    # Load data
    plants_data = json.loads(PLANTS_FILE.read_text(encoding="utf-8"))
    all_species = plants_data.get("species", [])
    name_map = load_name_map()

    # Filter to single node if requested
    if args.node_id:
        species_list = [s for s in all_species if s["id"] == args.node_id]
        if not species_list:
            print("ERROR: Species '{}' not found in plants.json".format(
                args.node_id), file=sys.stderr)
            sys.exit(1)
    else:
        species_list = all_species

    total = len(species_list)

    print("Building ZIM slug map...")
    slug_map = build_slug_map(zim_path)
    print("  ZIM plant pages: {}".format(len(slug_map)))

    existing_ids = find_existing_images()
    print("  Existing images: {}".format(len(existing_ids)))

    print()
    print("Processing {} species...".format(total))
    if args.dry_run:
        print("  (dry-run mode: no extractions)")
    print()

    stats = {
        "matched": 0, "no_match": 0, "no_images": 0,
        "skip_existing": 0, "mismatch": 0,
        "libre_count": 0, "nc_count": 0,
        "libre_selected": 0, "nc_selected": 0,
        "extracted": 0,
    }

    output_lines = []

    for i, species in enumerate(species_list, 1):
        species_id = species["id"]
        species_title = species.get("title", species_id)

        status, detail = process_species(
            species, zim_path, slug_map, name_map,
            existing_ids, args.dry_run, stats,
        )

        if status == "MATCH":
            tier = detail.rsplit("(", 1)[-1].rstrip(")") if "(" in detail else "?"
            zim_part = detail.split(" (")[0]
            line = "MATCH: {} -> {} ({})".format(species_id, zim_part, tier)
        elif status == "MISMATCH":
            line = "MISMATCH: {} -- {}".format(species_id, detail)
        else:
            line = "SKIP: {} -- {}".format(species_id, detail)

        output_lines.append(line)
        if not args.dry_run and status == "EXTRACTED":
            print("  [{}/{}] {} -> {}".format(
                i, total, species_id, detail))
        elif not args.dry_run:
            print("  [{}/{}] {}".format(i, total, line))

    # Print dry-run report
    if args.dry_run:
        for line in output_lines:
            print(line)
        print()

        matched = stats["matched"]
        coverage_pct = (matched / total * 100) if total else 0
        print("COVERAGE: {}/{} ({:.0f}%)".format(matched, total, coverage_pct))
        print("TIER_SUMMARY: {} libre, {} NC, {} no images".format(
            stats["libre_selected"], stats["nc_selected"],
            stats["no_images"] + stats["no_match"],
        ))

        # Save evidence
        evidence_path = EVIDENCE_DIR / "task-3-dry-run.txt"
        evidence_path.parent.mkdir(parents=True, exist_ok=True)
        report = "\n".join(output_lines) + "\n\n"
        report += "COVERAGE: {}/{} ({:.0f}%)\n".format(
            matched, total, coverage_pct)
        report += "TIER_SUMMARY: {} libre, {} NC, {} no images\n".format(
            stats["libre_selected"], stats["nc_selected"],
            stats["no_images"] + stats["no_match"],
        )
        report += "\n--- Stats ---\n"
        for k, v in sorted(stats.items()):
            report += "{}: {}\n".format(k, v)
        evidence_path.write_text(report, encoding="utf-8")
        print("\nEvidence saved to {}".format(evidence_path))
    else:
        # Summary for extraction mode
        print()
        print("=== Summary ===")
        print("  Total species:     {}".format(total))
        print("  Extracted:         {}".format(stats["extracted"]))
        print("  Skipped (existing): {}".format(stats["skip_existing"]))
        print("  Skipped (no match): {}".format(stats["no_match"]))
        print("  Skipped (no images): {}".format(stats["no_images"]))
        print("  Mismatch:          {}".format(stats["mismatch"]))
        print("  Output dir:        {}".format(IMAGES_DIR))


if __name__ == "__main__":
    main()
