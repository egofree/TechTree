#!/usr/bin/env python3
"""Source technical diagrams, cutaway views, and process flow illustrations.

Searches Wikimedia Commons, US Patent databases, and OpenStax for technical
diagrams suitable for the tech-tree-bootstrap project. Reads entity data via
scripts/lib/tt_data.py (per-entity JSON-LD), NOT the retired nodes.json.

Creates attribution sidecars with all 7 required fields and updates
data/images.json with new entries.

Usage:
    python3 scripts/source-diagrams.py --dry-run
    python3 scripts/source-diagrams.py --source wikimedia --domain chemistry
    python3 scripts/source-diagrams.py --type cutaway --limit 20
"""

import argparse
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.tt_data import load_all_entities, get_nodes_by_domain
from lib.wiki_client import WikiClient

# --- Paths ---

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
MANIFEST_FILE = DATA_DIR / "images.json"
IMAGES_DIR = PROJECT_DIR / "docs" / "images"
NOTEPAD_DIR = PROJECT_DIR / ".omo" / "notepads" / "image-expansion"

# --- Constants ---

RATE_LIMIT_SECONDS = 1.5

MAX_WIDTH = 1200
MAX_FILE_SIZE = 500 * 1024  # 500 KB

# Diagram-specific search terms appended to entity names
DIAGRAM_SUFFIXES = [
    "diagram",
    "cutaway",
    "cross-section",
    "schematic",
    "technical drawing",
    "patent drawing",
    "process flow",
    "blueprint",
]

# Terms that signal a diagram/technical image (used for relevance scoring)
DIAGRAM_KEYWORDS = frozenset({
    "diagram", "schematic", "cross-section", "cross section",
    "cutaway", "cut-away", "technical drawing", "blueprint",
    "patent", "process flow", "flowchart", "exploded view",
    "section", "elevation", "plan view", "orthographic",
    "isometric", "engineering drawing", "working drawing",
    "schematic diagram", "wiring diagram", "block diagram",
    "circuit diagram", "piping", "layout", "assembly drawing",
})

# License definitions — mirrors source-commons-images.py
LIBRE_LICENSES = {
    "cc0", "public domain", "public domain mark", "pd-old-70", "pd-old-100",
    "pd-art", "pd-us", "pd-user", "pd", "pd-self",
    "cc by 1.0", "cc by 2.0", "cc by 2.5", "cc by 3.0", "cc by 4.0",
    "cc by-sa 1.0", "cc by-sa 2.0", "cc by-sa 2.5", "cc by-sa 3.0",
    "cc by-sa 4.0",
}

# NC licenses accepted only when explicitly allowed
NC_LICENSES = {
    "cc by-nc 1.0", "cc by-nc 2.0", "cc by-nc 2.5", "cc by-nc 3.0",
    "cc by-nc 4.0",
    "cc by-nc-sa 1.0", "cc by-nc-sa 2.0", "cc by-nc-sa 2.5",
    "cc by-nc-sa 3.0", "cc by-nc-sa 4.0",
}

# ND licenses always rejected
ND_LICENSES = {
    "cc by-nd 1.0", "cc by-nd 2.0", "cc by-nd 2.5", "cc by-nd 3.0",
    "cc by-nd 4.0",
    "cc by-nc-nd 1.0", "cc by-nc-nd 2.0", "cc by-nc-nd 2.5",
    "cc by-nc-nd 3.0", "cc by-nc-nd 4.0",
}

# Accepted MIME types (SVG handled via conversion)
MIME_EXT = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/webp": ".webp",
}

# Fallback license URLs for common license types without explicit URL
FALLBACK_LICENSE_URLS = {
    "public domain": "https://creativecommons.org/publicdomain/mark/1.0/",
    "public domain mark": "https://creativecommons.org/publicdomain/mark/1.0/",
    "pd": "https://creativecommons.org/publicdomain/mark/1.0/",
    "pd-old-70": "https://creativecommons.org/publicdomain/mark/1.0/",
    "pd-old-100": "https://creativecommons.org/publicdomain/mark/1.0/",
    "pd-art": "https://creativecommons.org/publicdomain/mark/1.0/",
    "pd-us": "https://creativecommons.org/publicdomain/mark/1.0/",
    "pd-user": "https://creativecommons.org/publicdomain/mark/1.0/",
    "cc0": "https://creativecommons.org/publicdomain/zero/1.0/",
}

# Generic words that indicate poor-quality image titles
GENERIC_WORDS = frozenset({
    "file", "image", "photo", "commons", "wikimedia", "upload", "default",
    "thumbnail", "icon", "logo", "banner", "placeholder", "dummy",
})

# OpenStax textbook search (CC BY 4.0)
OPENSTAX_API = "https://openstax.org/api/v1/pages"

wiki = None  # Initialized in main()


# ---------------------------------------------------------------------------
# License helpers
# ---------------------------------------------------------------------------

def classify_license_tier(license_short):
    """Return 'libre' or 'nc' for acceptable licenses, or None."""
    if not license_short:
        return None
    normalized = license_short.strip().lower()
    for lic in ND_LICENSES:
        if normalized == lic or normalized.startswith(lic):
            return None  # ND always rejected
    for lic in LIBRE_LICENSES:
        if normalized == lic or normalized.startswith(lic):
            return "libre"
    for lic in NC_LICENSES:
        if normalized == lic or normalized.startswith(lic):
            return "nc"
    return None


def get_license_url_with_fallback(license_short, license_url):
    """Return license URL, falling back to known URL templates."""
    if license_url:
        return license_url
    normalized = (license_short or "").strip().lower()
    for key, url in FALLBACK_LICENSE_URLS.items():
        if normalized == key or normalized.startswith(key):
            return url
    return "https://commons.wikimedia.org/wiki/Commons:Licensing"


# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------

def strip_html(text):
    """Remove HTML tags from text."""
    return re.sub(r"<[^>]+>", "", text).strip()


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_relevance(name, search_queries, candidate_title):
    """Score how relevant a candidate image title is. Higher = more relevant.

    Adapted from source-commons-images.py with diagram-specific bonuses.
    """
    title = candidate_title
    if title.startswith("File:"):
        title = title[5:]
    title = re.sub(r"\.\w{1,5}$", "", title)
    title_lower = title.lower().replace("_", " ")

    name_lower = name.lower()
    name_words = set(re.findall(r"[a-z0-9]+", name_lower))

    query_words = set()
    for q in search_queries:
        query_words.update(re.findall(r"[a-z0-9]+", q.lower()))

    title_words = re.findall(r"[a-z0-9]+", title_lower)
    title_word_set = set(title_words)

    score = 0.0

    # +2 per name word found in title
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

    # +3 for query-specific words found in title
    query_only_words = query_words - name_words
    query_matches = sum(1 for w in query_only_words if w in title_word_set)
    score += query_matches * 3.0

    # -10 penalty if NO query-only words match
    if query_only_words and query_matches == 0:
        score -= 10.0

    # +4 bonus for diagram keywords in title (key differentiator for diagrams)
    diagram_matches = sum(1 for w in title_word_set if w in DIAGRAM_KEYWORDS)
    score += diagram_matches * 4.0

    # -1 per generic word
    for word in title_word_set:
        if word in GENERIC_WORDS:
            score -= 1.0

    # -3 for very short titles
    if len(title_words) < 3:
        score -= 3.0

    return score


# ---------------------------------------------------------------------------
# Wikimedia Commons search
# ---------------------------------------------------------------------------

def search_commons_diagrams(query, limit=10):
    """Search Wikimedia Commons for diagram-type images matching query.

    Returns list of candidate dicts with license tier info.
    """
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrnamespace": "6",  # File namespace
        "gsrsearch": query,
        "gsrlimit": str(limit),
        "prop": "imageinfo",
        "iiprop": "url|size|extmetadata|mime",
        "iiextmetadatafilter": (
            "LicenseShortName|License|LicenseUrl|Artist|"
            "ImageDescription|ObjectName|Categories"
        ),
        "iiurlwidth": str(MAX_WIDTH),
    }
    data = wiki.get_json(params=params)
    if not data or "query" not in data:
        return []

    candidates = []
    pages = data["query"].get("pages", {})
    for page_id in sorted(pages.keys()):
        info_list = pages[page_id].get("imageinfo", [])
        if not info_list:
            continue
        info = info_list[0]
        ext = info.get("extmetadata", {})
        license_short = (ext.get("LicenseShortName", {}).get("value", "") or "").strip()

        tier = classify_license_tier(license_short)
        if tier is None:
            continue

        mime = info.get("mime", "")
        file_title = pages[page_id].get("title", "")

        # Accept SVG (will convert), plus normal raster formats
        if mime not in MIME_EXT and mime != "image/svg+xml":
            continue

        # Skip PDF files
        if ".pdf" in file_title.lower():
            continue

        description_html = (ext.get("ImageDescription", {}).get("value", "") or "").strip()
        object_name = (ext.get("ObjectName", {}).get("value", "") or "").strip()
        categories_html = (ext.get("Categories", {}).get("value", "") or "").strip()

        width = info.get("width", 0)
        height = info.get("height", 0)

        # Skip very small images
        if width and height and (width < 200 or height < 200):
            continue

        is_svg = mime == "image/svg+xml"

        candidates.append({
            "file_title": file_title,
            "url": info.get("url", ""),
            "thumbnail_url": info.get("thumburl", "") or info.get("url", ""),
            "width": width,
            "height": height,
            "mime": mime,
            "is_svg": is_svg,
            "description": strip_html(description_html),
            "object_name": strip_html(object_name) if object_name else "",
            "categories": strip_html(categories_html),
            "license": license_short,
            "license_url": (ext.get("LicenseUrl", {}).get("value", "") or "").strip(),
            "author": strip_html((ext.get("Artist", {}).get("value", "") or "").strip()),
            "author_html": (ext.get("Artist", {}).get("value", "") or "").strip(),
            "page_url": info.get("descriptionurl", ""),
            "license_tier": tier,
            "source_type": "wikimedia",
        })

    return candidates


# ---------------------------------------------------------------------------
# US Patent search (public domain)
# ---------------------------------------------------------------------------

def search_patent_diagrams(entity_name, domain, limit=5):
    """Search for US Patent technical drawings via Google Patents Public Datasets.

    Patent drawings are public domain (US government work).
    Returns candidate dicts in the same format as Wikimedia candidates.

    Note: Google Patents does not have a public image API, so we construct
    candidate entries pointing to the patent page for manual review.
    The actual image sourcing happens via Wikimedia Commons where patent
    drawings are often re-hosted.
    """
    # Search Wikimedia Commons for patent drawings specifically
    patent_queries = [
        '"{} patent" diagram'.format(entity_name),
        '"{}" "patent drawing" technical'.format(entity_name),
    ]

    candidates = []
    seen_titles = set()
    for query in patent_queries:
        results = search_commons_diagrams(query, limit=limit)
        for c in results:
            if c["file_title"] not in seen_titles:
                seen_titles.add(c["file_title"])
                c["source_type"] = "patent"
                candidates.append(c)
        time.sleep(RATE_LIMIT_SECONDS)

    return candidates


# ---------------------------------------------------------------------------
# OpenStax search (CC BY 4.0)
# ---------------------------------------------------------------------------

def search_openstax_diagrams(entity_name, limit=5):
    """Search OpenStax textbook figures for technical diagrams.

    OpenStax textbooks are CC BY 4.0 licensed. This searches Wikimedia Commons
    for images sourced from OpenStax, which are commonly uploaded there.
    """
    openstax_queries = [
        '"{}" OpenStax diagram'.format(entity_name),
        '"{}" "OpenStax" technical illustration'.format(entity_name),
    ]

    candidates = []
    seen_titles = set()
    for query in openstax_queries:
        results = search_commons_diagrams(query, limit=limit)
        for c in results:
            if c["file_title"] not in seen_titles:
                seen_titles.add(c["file_title"])
                c["source_type"] = "openstax"
                candidates.append(c)
        time.sleep(RATE_LIMIT_SECONDS)

    return candidates


# ---------------------------------------------------------------------------
# SVG → PNG conversion
# ---------------------------------------------------------------------------

def convert_svg_to_png(svg_data, max_width=MAX_WIDTH):
    """Convert SVG bytes to PNG bytes, respecting max_width.

    Tries cairosvg first, then rsvg-convert. Returns None if neither works.
    """
    # Try cairosvg (Python package)
    try:
        import cairosvg
        png_data = cairosvg.svg2png(
            bytestring=svg_data,
            scale=max_width / 800.0 if max_width else 1.0,
        )
        return png_data
    except ImportError:
        pass
    except Exception as exc:
        print("    cairosvg conversion failed: {}".format(exc))

    # Try rsvg-convert (CLI tool)
    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        try:
            result = subprocess.run(
                [rsvg, "--width", str(max_width), "-f", "png", "-"],
                input=svg_data,
                capture_output=True,
                timeout=30,
            )
            if result.returncode == 0 and result.stdout:
                return result.stdout
        except (subprocess.TimeoutExpired, OSError) as exc:
            print("    rsvg-convert failed: {}".format(exc))

    return None


# ---------------------------------------------------------------------------
# Image download and processing
# ---------------------------------------------------------------------------

def download_and_process_image(candidate, dest_path):
    """Download image, convert SVG→PNG if needed, resize if oversized.

    Returns True on success. Enforces MAX_WIDTH and MAX_FILE_SIZE constraints.
    """
    if dest_path.exists():
        return True

    dest_path.parent.mkdir(parents=True, exist_ok=True)

    is_svg = candidate.get("is_svg", False)
    url = candidate.get("thumbnail_url") or candidate.get("url", "")

    if not url:
        return False

    raw_data = wiki.get(url=url)
    if raw_data is None:
        return False

    # SVG conversion
    if is_svg:
        png_data = convert_svg_to_png(raw_data, max_width=MAX_WIDTH)
        if png_data is None:
            print("    Skipping SVG (no converter available): {}".format(
                candidate["file_title"]
            ))
            return False
        raw_data = png_data
        # Update destination extension to .png
        dest_path = dest_path.with_suffix(".png")

    # Check file size constraint
    if len(raw_data) > MAX_FILE_SIZE:
        print("    Skipping (too large: {}KB > {}KB): {}".format(
            len(raw_data) // 1024, MAX_FILE_SIZE // 1024,
            candidate["file_title"],
        ))
        return False

    # Resize if wider than MAX_WIDTH (using stdlib only — check Pillow)
    try:
        from PIL import Image
        img = Image.open(io.BytesIO(raw_data))
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_height = int(img.height * ratio)
            img = img.resize((MAX_WIDTH, new_height), Image.LANCZOS)
            buf = io.BytesIO()
            fmt = img.format or "PNG"
            if dest_path.suffix == ".jpg":
                fmt = "JPEG"
            img.save(buf, format=fmt, quality=85)
            raw_data = buf.getvalue()
    except ImportError:
        # No Pillow — skip resizing, but check existing width from metadata
        if candidate.get("width", 0) > MAX_WIDTH * 1.5:
            print("    Skipping (too wide, no resizer): {}".format(
                candidate["file_title"]
            ))
            return False
    except Exception:
        pass  # Use as-is

    # Final size check after potential resize
    if len(raw_data) > MAX_FILE_SIZE:
        print("    Skipping (still too large after resize): {}".format(
            candidate["file_title"]
        ))
        return False

    dest_path.write_bytes(raw_data)
    return True


# ---------------------------------------------------------------------------
# Attribution
# ---------------------------------------------------------------------------

def build_attribution_md(candidate):
    """Build attribution markdown string from candidate data."""
    author = candidate.get("author", "") or "Wikimedia Commons contributor"
    license_name = candidate.get("license", "")
    license_url = get_license_url_with_fallback(
        license_name, candidate.get("license_url", "")
    )
    page_url = candidate.get("page_url", "")
    description = candidate.get("description", "")
    object_name = candidate.get("object_name", "")
    title = object_name or candidate.get("file_title", "").replace(
        "File:", ""
    ).replace("_", " ")

    lines = []
    if title:
        lines.append(title)
    if description:
        lines.append(description)
    lines.append("")
    if author and page_url:
        lines.append("Image: {} ([source]({}))".format(author, page_url))
    elif page_url:
        lines.append("Image: [Wikimedia Commons]({})".format(page_url))
    if license_name:
        if license_url:
            lines.append("License: [{}]({})".format(license_name, license_url))
        else:
            lines.append("License: {}".format(license_name))
    return "\n".join(lines)


def write_attribution_file(candidate, image_path):
    """Write .attribution.json sidecar with all 7 required fields.

    Required fields: title, author, license, license_url, source_url,
    attribution_md, license_tier.
    """
    author = candidate.get("author", "") or "Wikimedia Commons contributor"
    license_name = candidate.get("license", "")
    license_url = get_license_url_with_fallback(
        license_name, candidate.get("license_url", "")
    )
    title = candidate.get("object_name", "") or candidate.get(
        "file_title", ""
    ).replace("File:", "").replace("_", " ")
    source_url = candidate.get("page_url", "")
    tier = candidate.get("license_tier", "")

    attr = {
        "title": title or "Wikimedia Commons diagram",
        "description": candidate.get("description", ""),
        "author": author,
        "license": license_name,
        "license_url": license_url,
        "source_url": source_url,
        "original_url": candidate.get("url", ""),
        "attribution_md": build_attribution_md(candidate),
        "license_tier": tier,
    }
    attr_path = image_path.with_suffix(".attribution.json")
    attr_path.write_text(
        json.dumps(attr, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return attr_path


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

def load_manifest():
    """Load data/images.json manifest."""
    if MANIFEST_FILE.exists():
        try:
            return json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {"$schema": "bootciv-images-v1", "nodes": {}}


def save_manifest(manifest):
    """Save data/images.json manifest."""
    MANIFEST_FILE.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Entity iteration via tt_data.py
# ---------------------------------------------------------------------------

def collect_entities(domain=None):
    """Collect Capability entities from tt_data.py, optionally filtered by domain.

    Returns list of dicts with 'id', 'name', 'domain' keys.
    """
    if domain:
        raw_entities = get_nodes_by_domain(domain)
    else:
        raw_entities = load_all_entities(entity_type="Capability")

    entities = []
    for ent in raw_entities:
        ent_id = ent.get("id") or ent.get("@id", "")
        ent_name = ent.get("name", ent_id)
        # Extract domain from ID (e.g. "metals.iron-steel" -> "metals")
        ent_domain = ent_id.split(".")[0] if "." in ent_id else ent_id

        # Skip domain-level entities (they have level="domain")
        if ent.get("level") == "domain" or ent.get("@type") == "Domain":
            continue

        entities.append({
            "id": ent_id,
            "name": ent_name,
            "domain": ent_domain,
        })

    return entities


def entity_to_image_slug(entity_id):
    """Convert entity ID to image filename slug.

    'metals.iron-steel' -> 'metals_iron-steel'
    'agriculture.soil-management.vermiculture' -> 'agriculture_soil-management-vermiculture'
    """
    parts = entity_id.split(".")
    if len(parts) > 2:
        domain = parts[0]
        rest = "-".join(parts[1:])
        return "{}_{}".format(domain, rest)
    return entity_id.replace(".", "_")


# ---------------------------------------------------------------------------
# Search query building
# ---------------------------------------------------------------------------

def build_diagram_queries(entity, image_type="all"):
    """Build diagram-specific search queries for an entity.

    Args:
        entity: Dict with 'id', 'name', 'domain'.
        image_type: 'diagram', 'cutaway', 'flowchart', or 'all'.

    Returns:
        List of search query strings.
    """
    name = entity["name"]
    domain = entity["domain"]

    type_suffixes = {
        "diagram": ["diagram", "schematic", "technical drawing"],
        "cutaway": ["cutaway", "cross-section", "section view"],
        "flowchart": ["process flow", "flowchart", "block diagram"],
        "all": DIAGRAM_SUFFIXES[:6],  # Top 6 most useful
    }

    suffixes = type_suffixes.get(image_type, type_suffixes["all"])

    queries = []
    # Primary: entity name + diagram suffixes
    for suffix in suffixes[:3]:
        queries.append("{} {}".format(name, suffix))

    # Domain-level query for broader diagrams
    queries.append("{} {} diagram".format(domain, name))

    return queries[:5]


# ---------------------------------------------------------------------------
# Core processing
# ---------------------------------------------------------------------------

def pick_best_candidate(name, queries, candidates):
    """Select the best candidate with tiered preference: libre > nc."""
    libre = [c for c in candidates if c["license_tier"] == "libre"]
    nc = [c for c in candidates if c["license_tier"] == "nc"]

    for pool in (libre, nc):
        if not pool:
            continue
        for c in pool:
            c["_score"] = score_relevance(name, queries, c["file_title"])
        pool.sort(key=lambda c: c["_score"], reverse=True)
        best = pool[0]
        if best["_score"] > -5:
            return best
    return None


def process_entity(entity, manifest, args, index, total):
    """Process a single entity for diagram sourcing. Returns status string."""
    ent_id = entity["id"]
    ent_name = entity["name"]
    domain = entity["domain"]

    # Build manifest key: "diagram:{entity_id}"
    manifest_key = "diagram:{}".format(ent_id)
    slug = entity_to_image_slug(ent_id)
    domain_dir = IMAGES_DIR / domain

    # Check if already processed
    already_exists = False
    for ext in (".jpg", ".png", ".webp"):
        if (domain_dir / (slug + ext)).exists():
            already_exists = True
            break

    if not args.force and manifest_key in manifest["nodes"]:
        existing = manifest["nodes"][manifest_key]
        if existing.get("status") in ("downloaded",) or already_exists:
            return "skipped"

    print("[{}/{}] Searching diagrams: {} ({})...".format(
        index, total, ent_id, ent_name
    ))

    queries = build_diagram_queries(entity, args.type)

    all_candidates = []
    seen_titles = set()

    # Wikimedia Commons search
    if args.source in ("wikimedia", "all"):
        for query in queries:
            candidates = search_commons_diagrams(query, limit=args.search_limit)
            for c in candidates:
                if c["file_title"] not in seen_titles:
                    seen_titles.add(c["file_title"])
                    all_candidates.append(c)
            time.sleep(RATE_LIMIT_SECONDS)

    # US Patent search (via Wikimedia re-hosted patent drawings)
    if args.source in ("patents", "all"):
        patent_results = search_patent_diagrams(ent_name, domain, limit=3)
        for c in patent_results:
            if c["file_title"] not in seen_titles:
                seen_titles.add(c["file_title"])
                all_candidates.append(c)
        time.sleep(RATE_LIMIT_SECONDS)

    # OpenStax search (via Wikimedia re-hosted OpenStax figures)
    if args.source in ("openstax", "all"):
        openstax_results = search_openstax_diagrams(ent_name, limit=3)
        for c in openstax_results:
            if c["file_title"] not in seen_titles:
                seen_titles.add(c["file_title"])
                all_candidates.append(c)
        time.sleep(RATE_LIMIT_SECONDS)

    if not all_candidates:
        manifest["nodes"][manifest_key] = {
            "node_name": ent_name,
            "domain": domain,
            "search_queries": queries,
            "status": "no_results",
            "source_type": args.source,
            "image_type": args.type,
            "candidates": [],
            "local_path": None,
            "attribution": None,
        }
        return "no_results"

    best = pick_best_candidate(ent_name, queries, all_candidates)

    if best is None:
        manifest["nodes"][manifest_key] = {
            "node_name": ent_name,
            "domain": domain,
            "search_queries": queries,
            "status": "no_suitable",
            "source_type": args.source,
            "image_type": args.type,
            "candidates": [],
            "local_path": None,
            "attribution": None,
        }
        return "no_suitable"

    if args.dry_run:
        manifest["nodes"][manifest_key] = {
            "node_name": ent_name,
            "domain": domain,
            "search_queries": queries,
            "status": "has_candidate",
            "source_type": best.get("source_type", "wikimedia"),
            "image_type": args.type,
            "candidates": [{
                "file_title": best["file_title"],
                "license": best["license"],
                "license_tier": best["license_tier"],
                "width": best["width"],
                "height": best["height"],
                "is_svg": best.get("is_svg", False),
                "source_type": best.get("source_type", "wikimedia"),
            }],
            "local_path": None,
            "attribution": None,
        }
        return "has_candidate"

    # Determine output extension
    is_svg = best.get("is_svg", False)
    if is_svg:
        ext = ".png"  # Will convert SVG → PNG
    else:
        mime = best.get("mime", "image/jpeg")
        ext = MIME_EXT.get(mime, ".jpg")

    fname = slug + ext
    dest = domain_dir / fname

    if not download_and_process_image(best, dest):
        # Re-check with potentially changed extension (SVG → PNG)
        actual_dest = domain_dir / (slug + ".png") if is_svg else dest
        if not actual_dest.exists():
            manifest["nodes"][manifest_key] = {
                "node_name": ent_name,
                "domain": domain,
                "search_queries": queries,
                "status": "download_failed",
                "source_type": args.source,
                "image_type": args.type,
                "candidates": [],
                "local_path": None,
                "attribution": None,
            }
            return "download_failed"

    # Write attribution sidecar
    actual_fname = dest.name
    actual_dest = dest
    if is_svg and not dest.exists():
        actual_dest = domain_dir / (slug + ".png")
        actual_fname = actual_dest.name
    write_attribution_file(best, actual_dest)

    local_rel = "docs/images/{}/{}".format(domain, actual_fname)
    manifest["nodes"][manifest_key] = {
        "node_name": ent_name,
        "domain": domain,
        "search_queries": queries,
        "status": "downloaded",
        "source_type": best.get("source_type", "wikimedia"),
        "image_type": args.type,
        "candidates": [],
        "local_path": local_rel,
        "attribution": {
            "title": best.get("object_name", "") or best.get(
                "file_title", ""
            ).replace("File:", "").replace("_", " "),
            "description": best.get("description", ""),
            "author": best.get("author", ""),
            "license": best.get("license", ""),
            "license_url": best.get("license_url", ""),
            "source_url": best.get("page_url", ""),
            "license_tier": best.get("license_tier", ""),
            "attribution_md": build_attribution_md(best),
        },
    }

    print("    -> Downloaded: {} [{}] from {}".format(
        actual_fname, best["license_tier"],
        best.get("source_type", "wikimedia"),
    ))
    return "downloaded"


# ---------------------------------------------------------------------------
# Notepad logging
# ---------------------------------------------------------------------------

def append_to_notepad(message):
    """Append findings to .omo/notepads/image-expansion/learnings.md."""
    if not NOTEPAD_DIR.exists():
        NOTEPAD_DIR.mkdir(parents=True, exist_ok=True)

    notepad_file = NOTEPAD_DIR / "learnings.md"
    if not notepad_file.exists():
        notepad_file.write_text(
            "# Image Expansion Learnings\n\n"
            "Auto-generated notes from diagram sourcing runs.\n\n",
            encoding="utf-8",
        )

    timestamp = time.strftime("%Y-%m-%d %H:%M")
    with open(notepad_file, "a", encoding="utf-8") as f:
        f.write("\n## {} — source-diagrams.py\n\n{}\n".format(timestamp, message))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Source technical diagrams, cutaway views, and process flow "
            "illustrations from Wikimedia Commons, US Patents, and OpenStax"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  %(prog)s --dry-run\n"
            "  %(prog)s --source wikimedia --domain chemistry\n"
            "  %(prog)s --type cutaway --limit 10\n"
            "  %(prog)s --source all --domain metals --force\n"
        ),
    )
    parser.add_argument(
        "--dry-run", action="store_true", default=False,
        help="Search only, list candidates without downloading",
    )
    parser.add_argument(
        "--source", default="all",
        choices=["wikimedia", "patents", "openstax", "all"],
        help="Image source to search (default: all)",
    )
    parser.add_argument(
        "--type", dest="image_type", default="all",
        choices=["diagram", "cutaway", "flowchart", "all"],
        help="Type of diagram to search for (default: all)",
    )
    parser.add_argument(
        "--domain", default=None,
        help="Process only one domain's entities (e.g. 'metals', 'chemistry')",
    )
    parser.add_argument(
        "--limit", type=int, default=0,
        help="Max entities to process (0 = all)",
    )
    parser.add_argument(
        "--search-limit", type=int, default=10,
        help="Max search results per query (default: 10)",
    )
    parser.add_argument(
        "--node", dest="node_id", default=None,
        help="Process only one specific entity (e.g. metals.iron-steel)",
    )
    parser.add_argument(
        "--force", action="store_true", default=False,
        help="Re-search even if entity already has a diagram",
    )
    args = parser.parse_args()
    # Store type in args for process_entity
    args.type = args.image_type

    global wiki
    wiki = WikiClient(max_retries=2, retry_delay=5)

    # Collect entities via tt_data.py
    entities = collect_entities(domain=args.domain)

    # Single entity filter
    if args.node_id:
        entities = [e for e in entities if e["id"] == args.node_id]
        if not entities:
            print("ERROR: Entity '{}' not found".format(args.node_id), file=sys.stderr)
            sys.exit(1)

    # Limit filter
    if args.limit > 0:
        entities = entities[:args.limit]

    manifest = load_manifest()
    total = len(entities)

    print("=== Technical Diagram Sourcing ===")
    print("  Source:          {}".format(args.source))
    print("  Image type:      {}".format(args.type))
    print("  Entities:        {}".format(total))
    print("  Domain filter:   {}".format(args.domain or "none"))
    if args.dry_run:
        print("  (dry-run mode: no downloads)")
    print()

    stats = {
        "searched": 0,
        "skipped": 0,
        "downloaded": 0,
        "has_candidate": 0,
        "no_results": 0,
        "no_suitable": 0,
        "download_failed": 0,
    }

    t0 = time.time()
    checkpoint_interval = 25

    for i, entity in enumerate(entities, 1):
        status = process_entity(entity, manifest, args, i, total)
        if status == "skipped":
            stats["skipped"] += 1
        else:
            stats["searched"] += 1
            stats.setdefault(status, 0)
            stats[status] = stats.get(status, 0) + 1
        if i % checkpoint_interval == 0:
            save_manifest(manifest)
            print("  [checkpoint: {} entities processed, manifest saved]".format(i))

    # Save manifest
    save_manifest(manifest)

    elapsed = time.time() - t0

    print()
    print("=== Summary ===")
    print("  Total entities:     {}".format(total))
    print("  Searched:           {}".format(stats["searched"]))
    print("  Skipped (cached):   {}".format(stats["skipped"]))
    print("  Downloaded:         {}".format(stats.get("downloaded", 0)))
    print("  Has candidate:      {}".format(stats.get("has_candidate", 0)))
    print("  No results:         {}".format(stats.get("no_results", 0)))
    print("  No suitable:        {}".format(stats.get("no_suitable", 0)))
    print("  Download failed:    {}".format(stats.get("download_failed", 0)))
    print("  Elapsed:            {:.1f}s".format(elapsed))
    print("  Manifest:           {}".format(MANIFEST_FILE))

    # Append to notepad
    notepad_msg = (
        "Run: source={}, type={}, domain={}\n"
        "Results: {} searched, {} downloaded, {} no_results, "
        "{} no_suitable, {} failed\n"
        "Elapsed: {:.1f}s".format(
            args.source, args.type, args.domain or "all",
            stats["searched"], stats.get("downloaded", 0),
            stats.get("no_results", 0), stats.get("no_suitable", 0),
            stats.get("download_failed", 0), elapsed,
        )
    )
    append_to_notepad(notepad_msg)


if __name__ == "__main__":
    main()
