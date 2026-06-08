#!/usr/bin/env python3
"""Source Wikimedia Commons images for procedural articles and unmatched plant species.

Reads data/procedural-articles.json for articles needing images and
data/plant-name-map.json for unmatched plant species that need fallback images.
Downloads thumbnails, creates attribution sidecars, updates data/images.json.

Usage:
    python3 scripts/source-commons-images.py [--dry-run] [--domain DOMAIN] [--limit N]
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.wiki_client import WikiClient

# --- Paths ---

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
PROCEDURAL_FILE = DATA_DIR / "procedural-articles.json"
PLANT_MAP_FILE = DATA_DIR / "plant-name-map.json"
MANIFEST_FILE = DATA_DIR / "images.json"
IMAGES_DIR = PROJECT_DIR / "docs" / "images"

# --- License definitions ---

LIBRE_LICENSES = {
    "cc0", "public domain", "public domain mark", "pd-old-70", "pd-old-100",
    "pd-art", "pd-us", "pd-user", "pd", "pd-self",
    "cc by 1.0", "cc by 2.0", "cc by 2.5", "cc by 3.0", "cc by 4.0",
    "cc by-sa 1.0", "cc by-sa 2.0", "cc by-sa 2.5", "cc by-sa 3.0", "cc by-sa 4.0",
}

NC_LICENSES = {
    "cc by-nc 1.0", "cc by-nc 2.0", "cc by-nc 2.5", "cc by-nc 3.0", "cc by-nc 4.0",
    "cc by-nc-sa 1.0", "cc by-nc-sa 2.0", "cc by-nc-sa 2.5", "cc by-nc-sa 3.0",
    "cc by-nc-sa 4.0",
    "cc by-nc-nd 1.0", "cc by-nc-nd 2.0", "cc by-nc-nd 2.5", "cc by-nc-nd 3.0",
    "cc by-nc-nd 4.0",
}

ALL_ACCEPTABLE = LIBRE_LICENSES | NC_LICENSES

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

# Words that indicate a poor-quality/generic image
GENERIC_WORDS = frozenset({
    "file", "image", "photo", "commons", "wikimedia", "upload", "default",
    "thumbnail", "icon", "logo", "banner", "placeholder", "dummy",
})

RATE_LIMIT_SECONDS = 1.0

wiki = None  # Initialized in main()


def classify_license_tier(license_short):
    """Return 'libre' or 'nc' for acceptable licenses, or None."""
    if not license_short:
        return None
    normalized = license_short.strip().lower()
    for lic in LIBRE_LICENSES:
        if normalized == lic or normalized.startswith(lic):
            return "libre"
    for lic in NC_LICENSES:
        if normalized == lic or normalized.startswith(lic):
            return "nc"
    return None


def strip_html(text):
    """Remove HTML tags from text."""
    return re.sub(r"<[^>]+>", "", text).strip()


def score_relevance(name, search_queries, candidate_title):
    """Score how relevant a candidate image title is. Higher = more relevant."""
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
            # Stem matching (prefix overlap >= 4 chars)
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

    # +0.5 for query words beyond name words
    for word in query_words:
        if word in title_word_set and word not in name_words:
            score += 0.5

    # -1 per generic word
    for word in title_word_set:
        if word in GENERIC_WORDS:
            score -= 1.0

    # -3 for very short titles
    if len(title_words) < 3:
        score -= 3.0

    return score


def search_commons(query, limit=10):
    """Search Wikimedia Commons for images matching query.

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
        "iiextmetadatafilter": "LicenseShortName|License|LicenseUrl|Artist|ImageDescription|ObjectName|Categories",
        "iiurlwidth": "800",
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

        # Classify license tier
        tier = classify_license_tier(license_short)
        if tier is None:
            continue  # Unacceptable license

        mime = info.get("mime", "")
        if mime not in MIME_EXT:
            continue

        description_html = (ext.get("ImageDescription", {}).get("value", "") or "").strip()
        object_name = (ext.get("ObjectName", {}).get("value", "") or "").strip()
        categories_html = (ext.get("Categories", {}).get("value", "") or "").strip()

        width = info.get("width", 0)
        height = info.get("height", 0)

        # Skip very small images
        if width and height and (width < 200 or height < 200):
            continue

        # Skip PDF files
        file_title = pages[page_id].get("title", "")
        if ".pdf" in file_title.lower():
            continue

        candidates.append({
            "file_title": file_title,
            "url": info.get("url", ""),
            "thumbnail_url": info.get("thumburl", "") or info.get("url", ""),
            "width": width,
            "height": height,
            "mime": mime,
            "description": strip_html(description_html),
            "object_name": strip_html(object_name) if object_name else "",
            "categories": strip_html(categories_html),
            "license": license_short,
            "license_url": (ext.get("LicenseUrl", {}).get("value", "") or "").strip(),
            "author": strip_html((ext.get("Artist", {}).get("value", "") or "").strip()),
            "author_html": (ext.get("Artist", {}).get("value", "") or "").strip(),
            "page_url": info.get("descriptionurl", ""),
            "license_tier": tier,
        })

    return candidates


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
        if best["_score"] > -5:  # Not completely irrelevant
            return best
    return None


def build_attribution_md(candidate):
    author = candidate.get("author", "") or "Wikimedia Commons contributor"
    license_name = candidate.get("license", "")
    license_url = get_license_url_with_fallback(license_name, candidate.get("license_url", ""))
    page_url = candidate.get("page_url", "")
    description = candidate.get("description", "")
    object_name = candidate.get("object_name", "")
    title = object_name or candidate.get("file_title", "").replace("File:", "").replace("_", " ")

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


def get_license_url_with_fallback(license_short, license_url):
    if license_url:
        return license_url
    normalized = (license_short or "").strip().lower()
    for key, url in FALLBACK_LICENSE_URLS.items():
        if normalized == key or normalized.startswith(key):
            return url
    return "https://commons.wikimedia.org/wiki/Commons:Licensing"


def write_attribution_file(candidate, image_path):
    author = candidate.get("author", "") or "Wikimedia Commons contributor"
    license_name = candidate.get("license", "")
    license_url = get_license_url_with_fallback(license_name, candidate.get("license_url", ""))
    title = candidate.get("object_name", "") or candidate.get("file_title", "").replace("File:", "").replace("_", " ")
    source_url = candidate.get("page_url", "")
    tier = candidate.get("license_tier", "")

    attr = {
        "title": title or "Wikimedia Commons image",
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


def download_image(url, dest_path):
    """Download image to dest_path. Returns True on success."""
    if dest_path.exists():
        return True
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    data = wiki.get(url=url)
    if data is None:
        return False
    dest_path.write_bytes(data)
    return True


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


def article_slug(article_id):
    """Convert article id to filename slug.

    'agriculture.crop-rotation' -> 'agriculture_crop-rotation'
    'agriculture.soil-management.vermiculture' -> 'agriculture_soil-management-vermiculture'
    """
    return article_id.replace(".", "_")


def process_article(article, manifest, args, index, total):
    """Process a single procedural article. Returns status string."""
    art_id = article["id"]
    title = article["title"]
    domain = article["domain"]
    queries = article.get("search_queries", [title])

    # Skip if already downloaded (check manifest AND filesystem)
    slug = article_slug(art_id)
    domain_dir = IMAGES_DIR / domain
    already_exists = False
    for ext in (".jpg", ".png", ".webp", ".gif"):
        if (domain_dir / (slug + ext)).exists():
            already_exists = True
            break

    if not args.force and art_id in manifest["nodes"]:
        existing = manifest["nodes"][art_id]
        if existing.get("status") in ("downloaded",) or already_exists:
            return "skipped"

    print("[{}/{}] Searching: {} ({})...".format(index, total, art_id, title))

    # Search Wikimedia Commons using provided queries
    all_candidates = []
    seen_titles = set()
    for query in queries:
        candidates = search_commons(query, limit=args.search_limit)
        for c in candidates:
            if c["file_title"] not in seen_titles:
                seen_titles.add(c["file_title"])
                all_candidates.append(c)
        time.sleep(RATE_LIMIT_SECONDS)

    if not all_candidates:
        manifest["nodes"][art_id] = {
            "node_name": title,
            "domain": domain,
            "search_queries": queries,
            "status": "no_results",
            "candidates": [],
            "local_path": None,
            "attribution": None,
        }
        return "no_results"

    # Pick best candidate with tiered license preference
    best = pick_best_candidate(title, queries, all_candidates)

    if best is None:
        manifest["nodes"][art_id] = {
            "node_name": title,
            "domain": domain,
            "search_queries": queries,
            "status": "no_suitable",
            "candidates": [],
            "local_path": None,
            "attribution": None,
        }
        return "no_suitable"

    if args.dry_run:
        manifest["nodes"][art_id] = {
            "node_name": title,
            "domain": domain,
            "search_queries": queries,
            "status": "has_candidate",
            "candidates": [{
                "file_title": best["file_title"],
                "license": best["license"],
                "license_tier": best["license_tier"],
                "width": best["width"],
                "height": best["height"],
            }],
            "local_path": None,
            "attribution": None,
        }
        return "has_candidate"

    # Download the image
    thumb_url = best.get("thumbnail_url") or best.get("url", "")
    if not thumb_url:
        return "no_results"

    mime = best.get("mime", "image/jpeg")
    ext = MIME_EXT.get(mime, ".jpg")
    fname = slug + ext
    dest = domain_dir / fname

    if not download_image(thumb_url, dest):
        manifest["nodes"][art_id] = {
            "node_name": title,
            "domain": domain,
            "search_queries": queries,
            "status": "download_failed",
            "candidates": [],
            "local_path": None,
            "attribution": None,
        }
        return "download_failed"

    # Write attribution sidecar
    write_attribution_file(best, dest)

    local_rel = "docs/images/{}/{}".format(domain, fname)
    manifest["nodes"][art_id] = {
        "node_name": title,
        "domain": domain,
        "search_queries": queries,
        "status": "downloaded",
        "candidates": [],
        "local_path": local_rel,
        "attribution": {
            "title": best.get("object_name", "") or best.get("file_title", "").replace("File:", "").replace("_", " "),
            "description": best.get("description", ""),
            "author": best.get("author", ""),
            "license": best.get("license", ""),
            "license_url": best.get("license_url", ""),
            "source_url": best.get("page_url", ""),
            "license_tier": best.get("license_tier", ""),
            "attribution_md": build_attribution_md(best),
        },
    }

    print("    -> Downloaded: {} [{}]".format(fname, best["license_tier"]))
    return "downloaded"


def process_plant_fallback(species, manifest, args, index, total):
    """Process an unmatched plant species for Wikimedia fallback image."""
    plant_id = species["plants_json_id"]
    sci_name = species["scientific_name"]

    slug = "plants_{}".format(plant_id)
    plants_dir = IMAGES_DIR / "plants"

    # Check if already exists
    already_exists = False
    for ext in (".jpg", ".png", ".webp", ".gif"):
        if (plants_dir / (slug + ext)).exists():
            already_exists = True
            break

    key = "plants.{}".format(plant_id)
    if key in manifest["nodes"]:
        existing = manifest["nodes"][key]
        if existing.get("status") == "downloaded" or already_exists:
            return "skipped"

    print("[{}/{}] Plant fallback: {} ({})...".format(index, total, plant_id, sci_name))

    # Search using scientific name
    queries = [sci_name, "{} plant".format(sci_name)]
    all_candidates = []
    seen_titles = set()
    for query in queries:
        candidates = search_commons(query, limit=args.search_limit)
        for c in candidates:
            if c["file_title"] not in seen_titles:
                seen_titles.add(c["file_title"])
                all_candidates.append(c)
        time.sleep(RATE_LIMIT_SECONDS)

    if not all_candidates:
        manifest["nodes"][key] = {
            "node_name": sci_name,
            "domain": "plants",
            "search_queries": queries,
            "status": "no_results",
            "candidates": [],
            "local_path": None,
            "attribution": None,
        }
        return "no_results"

    best = pick_best_candidate(sci_name, queries, all_candidates)
    if best is None:
        manifest["nodes"][key] = {
            "node_name": sci_name,
            "domain": "plants",
            "search_queries": queries,
            "status": "no_suitable",
            "candidates": [],
            "local_path": None,
            "attribution": None,
        }
        return "no_suitable"

    if args.dry_run:
        manifest["nodes"][key] = {
            "node_name": sci_name,
            "domain": "plants",
            "search_queries": queries,
            "status": "has_candidate",
            "candidates": [{
                "file_title": best["file_title"],
                "license": best["license"],
                "license_tier": best["license_tier"],
            }],
            "local_path": None,
            "attribution": None,
        }
        return "has_candidate"

    thumb_url = best.get("thumbnail_url") or best.get("url", "")
    if not thumb_url:
        return "no_results"

    mime = best.get("mime", "image/jpeg")
    ext = MIME_EXT.get(mime, ".jpg")
    fname = slug + ext
    dest = plants_dir / fname

    if not download_image(thumb_url, dest):
        manifest["nodes"][key] = {
            "node_name": sci_name,
            "domain": "plants",
            "search_queries": queries,
            "status": "download_failed",
            "candidates": [],
            "local_path": None,
            "attribution": None,
        }
        return "download_failed"

    write_attribution_file(best, dest)

    local_rel = "docs/images/plants/{}".format(fname)
    manifest["nodes"][key] = {
        "node_name": sci_name,
        "domain": "plants",
        "search_queries": queries,
        "status": "downloaded",
        "candidates": [],
        "local_path": local_rel,
        "attribution": {
            "title": best.get("object_name", "") or best.get("file_title", "").replace("File:", "").replace("_", " "),
            "description": best.get("description", ""),
            "author": best.get("author", ""),
            "license": best.get("license", ""),
            "license_url": best.get("license_url", ""),
            "source_url": best.get("page_url", ""),
            "license_tier": best.get("license_tier", ""),
            "attribution_md": build_attribution_md(best),
        },
    }

    print("    -> Downloaded: {} [{}]".format(fname, best["license_tier"]))
    return "downloaded"


def main():
    parser = argparse.ArgumentParser(
        description="Source Wikimedia Commons images for procedural articles and plant fallbacks"
    )
    parser.add_argument("--dry-run", action="store_true", default=False,
                        help="Search only, don't download")
    parser.add_argument("--domain", default=None,
                        help="Process only one domain's articles")
    parser.add_argument("--limit", type=int, default=0,
                        help="Max articles to process (0 = all)")
    parser.add_argument("--search-limit", type=int, default=10,
                        help="Max search results per query (default: 10)")
    parser.add_argument("--node", dest="node_id", default=None,
                        help="Process only one specific article (e.g., machine-tools.joining)")
    parser.add_argument("--force", action="store_true", default=False,
                        help="Re-search even if article already downloaded")
    args = parser.parse_args()

    global wiki
    wiki = WikiClient(max_retries=2, retry_delay=5)

    # Load procedural articles
    if not PROCEDURAL_FILE.exists():
        print("ERROR: {} not found".format(PROCEDURAL_FILE), file=sys.stderr)
        sys.exit(1)
    proc_data = json.loads(PROCEDURAL_FILE.read_text(encoding="utf-8"))
    all_articles = proc_data.get("articles", [])

    # Filter to articles needing images
    articles = [a for a in all_articles if not a.get("has_existing_image", False)]

    # Node filter (single article by id)
    if args.node_id:
        articles = [a for a in articles if a["id"] == args.node_id]
        if not articles:
            # Also try against all_articles (may have has_existing_image=True)
            articles = [a for a in all_articles if a["id"] == args.node_id]
        if not articles:
            print("ERROR: Article '{}' not found".format(args.node_id), file=sys.stderr)
            sys.exit(1)

    # Domain filter
    if args.domain:
        articles = [a for a in articles if a["domain"] == args.domain]
        if not articles:
            print("ERROR: No articles found for domain '{}'".format(args.domain), file=sys.stderr)
            sys.exit(1)

    # Limit filter
    if args.limit > 0:
        articles = articles[:args.limit]

    # Load plant fallbacks
    plant_fallbacks = []
    if PLANT_MAP_FILE.exists():
        plant_data = json.loads(PLANT_MAP_FILE.read_text(encoding="utf-8"))
        plant_fallbacks = plant_data.get("unmatched_species", [])
        # Domain filter also applies to plants
        if args.domain and args.domain != "plants":
            plant_fallbacks = []
        if args.limit > 0:
            plant_fallbacks = plant_fallbacks[:max(0, args.limit - len(articles))]

    manifest = load_manifest()
    total_articles = len(articles)
    total_plants = len(plant_fallbacks)
    total = total_articles + total_plants

    print("=== Wikimedia Commons Image Sourcing ===")
    print("  Articles to process: {}".format(total_articles))
    print("  Plant fallbacks:     {}".format(total_plants))
    print("  Total items:         {}".format(total))
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
    checkpoint_interval = 50  # Save manifest every N items

    # Process procedural articles
    for i, article in enumerate(articles, 1):
        status = process_article(article, manifest, args, i, total)
        if status == "skipped":
            stats["skipped"] += 1
        else:
            stats["searched"] += 1
            stats.setdefault(status, 0)
            stats[status] = stats.get(status, 0) + 1
        if i % checkpoint_interval == 0:
            save_manifest(manifest)
            print("  [checkpoint: {} articles processed, manifest saved]".format(i))

    # Process plant fallbacks
    for j, species in enumerate(plant_fallbacks, total_articles + 1):
        status = process_plant_fallback(species, manifest, args, j, total)
        if status == "skipped":
            stats["skipped"] += 1
        else:
            stats["searched"] += 1
            stats.setdefault(status, 0)
            stats[status] = stats.get(status, 0) + 1
        if j % checkpoint_interval == 0:
            save_manifest(manifest)
            print("  [checkpoint: manifest saved]")

    # Save manifest
    save_manifest(manifest)

    elapsed = time.time() - t0

    print()
    print("=== Summary ===")
    print("  Total items:       {}".format(total))
    print("  Searched:          {}".format(stats["searched"]))
    print("  Skipped (cached):  {}".format(stats["skipped"]))
    print("  Downloaded:        {}".format(stats.get("downloaded", 0)))
    print("  Has candidate:     {}".format(stats.get("has_candidate", 0)))
    print("  No results:        {}".format(stats.get("no_results", 0)))
    print("  No suitable:       {}".format(stats.get("no_suitable", 0)))
    print("  Download failed:   {}".format(stats.get("download_failed", 0)))
    print("  Elapsed:           {:.1f}s".format(elapsed))
    print("  Manifest:          {}".format(MANIFEST_FILE))

    # Calculate coverage
    proc_all = json.loads(PROCEDURAL_FILE.read_text(encoding="utf-8")).get("articles", [])
    proc_with_img = sum(1 for a in proc_all if a.get("has_existing_image", False))
    proc_downloaded = sum(
        1 for a in proc_all
        if not a.get("has_existing_image", False)
        and a["id"] in manifest["nodes"]
        and manifest["nodes"][a["id"]].get("status") == "downloaded"
    )
    total_with_img = proc_with_img + proc_downloaded
    coverage_pct = (total_with_img / len(proc_all) * 100) if proc_all else 0
    print()
    print("  Coverage: {}/{} ({:.1f}%)".format(total_with_img, len(proc_all), coverage_pct))


if __name__ == "__main__":
    main()
