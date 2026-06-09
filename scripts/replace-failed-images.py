#!/usr/bin/env python3
"""Batch replace failed images from vision-audit.json with better Wikimedia Commons images.

Reads vision-audit.json for entries with verdict="replace", searches Commons
for better alternatives using the article_title as basis for search queries,
downloads the best candidate, creates attribution sidecars, and updates
both vision-audit.json and images.json.

Usage:
    python3 scripts/replace-failed-images.py [--domain DOMAIN] [--dry-run] [--limit N] [--force] [--delay SECONDS]
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
AUDIT_FILE = DATA_DIR / "vision-audit.json"
MANIFEST_FILE = DATA_DIR / "images.json"
IMAGES_DIR = PROJECT_DIR / "docs" / "images"

# --- License definitions ---

LIBRE_LICENSES = {
    "cc0", "public domain", "public domain mark", "pd-old-70", "pd-old-100",
    "pd-art", "pd-us", "pd-user", "pd", "pd-self",
    "cc by 1.0", "cc by 2.0", "cc by 2.5", "cc by 3.0", "cc by 4.0",
    "cc by-sa 1.0", "cc by-sa 2.0", "cc by-sa 2.5", "cc by-sa 3.0", "cc by-sa 4.0",
}

MIME_EXT = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/webp": ".webp",
}

GENERIC_WORDS = frozenset({
    "file", "image", "photo", "commons", "wikimedia", "upload", "default",
    "thumbnail", "icon", "logo", "banner", "placeholder", "dummy",
})

RATE_LIMIT_SECONDS = 1.0
MAX_QUERY_ATTEMPTS = 3

wiki = None


def strip_html(text):
    return re.sub(r"<[^>]+>", "", text).strip()


def license_is_libre(license_short):
    if not license_short:
        return False
    normalized = license_short.strip().lower()
    for lic in LIBRE_LICENSES:
        if normalized == lic or normalized.startswith(lic):
            return True
    return False


# Domain-specific search enhancers: add context terms when article_title is too generic
DOMAIN_ENHANCERS = {
    "defense": "military weapons armor fortification",
    "marine": "ship boat naval maritime sailing",
    "telecom": "telecommunication radio signal antenna",
    "cleanrooms": "cleanroom contamination controlled environment",
    "cryogenics": "cryogenic cold liquid nitrogen helium",
    "economics-organization": "economics organization trade commerce",
    "software-bootstrapping": "software programming computer code",
    "precision-motion": "precision positioning motion control nanopositioning",
    "quality-control": "quality control inspection metrology testing",
    "ultra-pure": "ultra pure water purification semiconductor",
    "vacuum": "vacuum chamber pump low pressure",
    "agriculture": "agriculture farming crop soil",
    "animals": "animal livestock husbandry domesticated",
    "automation": "automation robotic industrial control",
    "ceramics": "ceramic pottery kiln fired clay",
    "chemistry": "chemistry chemical reaction laboratory",
    "computing": "computing computer calculation processor",
    "construction": "construction building concrete crane",
    "ehs": "safety environment hazardous protection",
    "electrochemistry": "electrochemistry electrolysis battery galvanic",
    "electronics": "electronics circuit board transistor",
    "energy": "energy power electricity generator",
    "food-processing": "food processing preservation milling",
    "foundations": "fire stone tool primitive",
    "gas-handling": "gas cylinder handling valve pressure",
    "glass": "glass melting furnace blowing",
    "health": "health medicine hygiene sanitation",
    "knowledge": "knowledge printing book library",
    "machine-tools": "machine tool lathe milling drill",
    "measurement": "measurement instrument gauge caliper",
    "metals": "metal smelting furnace alloy steel",
    "mining": "mining ore extraction tunnel shaft",
    "optics": "optics lens prism light refraction",
    "petroleum": "petroleum oil drilling refinery",
    "photolithography": "photolithography wafer lithography semiconductor",
    "plants": "plant botanical agriculture crop",
    "polymers": "polymer plastic resin synthetic",
    "silicon": "silicon crystal semiconductor wafer",
    "textiles": "textile weaving fabric loom fiber",
    "transport": "transport vehicle wheel railway",
    "vlsi-scaling": "VLSI integrated circuit chip microprocessor",
    "water": "water treatment filtration purification",
}


def slug_to_readable(slug):
    """Convert a capability slug like 'contamination-control' to 'contamination control'."""
    return slug.replace("-", " ").replace("_", " ")


def is_likely_file_title(article_title, filename):
    """Check if article_title looks like a file title rather than a descriptive topic."""
    # If title matches the filename (without extension), it's a file title
    base = Path(filename).stem
    slug_from_file = base.split("_", 1)[-1] if "_" in base else base
    title_normalized = article_title.lower().strip()
    slug_normalized = slug_to_readable(slug_from_file).lower()
    
    # If the title is very close to the slug, it's probably just the slug
    if title_normalized == slug_normalized:
        return True
    
    # If title contains file-like patterns (numbers/dates, "from YYYY", etc.)
    if re.search(r'\bfrom\s+\d{4}\b', title_normalized):
        return True
    if re.search(r'^\d{4}', title_normalized):
        return True
    
    # If title is a non-English phrase (no common English words)
    english_words = {"the", "and", "of", "for", "in", "with", "from", "a", "an", "is", "are"}
    words = set(re.findall(r'[a-zA-Z]+', title_normalized))
    if words and not words.intersection(english_words) and len(words) <= 3:
        return True
    
    return False


def build_search_queries(article_title, domain="", reason="", filename=""):
    """Build 2-3 search queries from article title, domain, and failure reason."""
    title = article_title.strip()
    
    has_latin = bool(re.search(r'[a-zA-Z]{3,}', title))
    is_file_title = is_likely_file_title(title, filename) if filename else False
    
    queries = []
    filler = {"the", "a", "an", "of", "in", "for", "and", "or", "to", "with", "from", "by", "at", "is", "are", "its"}
    
    # If article_title looks like a file title, derive query from the filename slug instead
    if is_file_title and filename:
        base = Path(filename).stem
        slug = base.split("_", 1)[-1] if "_" in base else base
        if slug == "hero":
            slug = domain
        readable_slug = slug_to_readable(slug)
        words = [w for w in re.findall(r"[a-zA-Z0-9]+", readable_slug) if w.lower() not in filler]
        if words:
            title = readable_slug + " " + domain
            has_latin = True
    
    words = [w for w in re.findall(r"[a-zA-Z0-9]+", title) if w.lower() not in filler]
    enhance = DOMAIN_ENHANCERS.get(domain, "")
    
    if has_latin and len(words) >= 2:
        queries.append(" ".join(words[:5]))
        if enhance:
            enhanced = " ".join(words[:3]) + " " + enhance.split()[0]
            queries.append(enhanced)
        if len(words) >= 3:
            queries.append(" ".join(words[:2]) + " " + domain)
    elif has_latin and len(words) == 1:
        word = words[0]
        if enhance:
            queries.append(word + " " + " ".join(enhance.split()[:3]))
        else:
            queries.append(word)
        queries.append(word + " " + domain)
    else:
        if enhance:
            enhance_words = enhance.split()
            if len(enhance_words) >= 2:
                queries.append(enhance_words[0] + " " + enhance_words[1])
            queries.append(enhance)
        else:
            queries.append(domain)
    
    seen = set()
    unique = []
    for q in queries:
        if q.lower() not in seen:
            seen.add(q.lower())
            unique.append(q)
    
    return unique[:MAX_QUERY_ATTEMPTS]


def search_commons(query, limit=10):
    """Search Wikimedia Commons for images matching query."""
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrnamespace": "6",
        "gsrsearch": query,
        "gsrlimit": str(limit),
        "prop": "imageinfo",
        "iiprop": "url|size|extmetadata|mime",
        "iiextmetadatafilter": "LicenseShortName|License|LicenseUrl|Artist|ImageDescription|ObjectName|Categories",
        "iiurlwidth": "1200",
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
        
        if not license_is_libre(license_short):
            continue
        
        mime = info.get("mime", "")
        if mime not in MIME_EXT:
            continue
        
        width = info.get("width", 0)
        height = info.get("height", 0)
        if width < 200 or height < 200:
            continue
        
        description_html = (ext.get("ImageDescription", {}).get("value", "") or "").strip()
        object_name = (ext.get("ObjectName", {}).get("value", "") or "").strip()
        
        # Skip PDFs and SVGs (already filtered by MIME_EXT but double-check)
        file_title = pages[page_id].get("title", "")
        if ".pdf" in file_title.lower():
            continue
        
        candidates.append({
            "file_title": file_title,
            "url": info.get("url", ""),
            "thumbnail_url": info.get("thumburl", ""),
            "width": width,
            "height": height,
            "mime": mime,
            "description": strip_html(description_html),
            "object_name": strip_html(object_name) if object_name else "",
            "license": license_short,
            "license_url": (ext.get("LicenseUrl", {}).get("value", "") or "").strip(),
            "author": strip_html((ext.get("Artist", {}).get("value", "") or "").strip()),
            "page_url": info.get("descriptionurl", ""),
        })
    
    return candidates


def score_relevance(article_title, candidate):
    """Score how relevant a candidate image is to the article topic."""
    title = candidate.get("file_title", "")
    if title.startswith("File:"):
        title = title[5:]
    title = re.sub(r"\.\w{1,5}$", "", title)
    title_lower = title.lower().replace("_", " ")
    
    name_lower = article_title.lower()
    name_words = set(re.findall(r"[a-z0-9]+", name_lower))
    
    title_words = re.findall(r"[a-z0-9]+", title_lower)
    title_word_set = set(title_words)
    
    score = 0.0
    
    # +2 per name word found in title
    for word in name_words:
        if word in title_word_set:
            score += 2.0
        else:
            # Stem matching
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
    
    # -1 per generic word
    for word in title_word_set:
        if word in GENERIC_WORDS:
            score -= 1.0
    
    # -3 for very short titles
    if len(title_words) < 3:
        score -= 3.0
    
    # Prefer reasonable aspect ratios (not too tall, not too wide)
    w = candidate.get("width", 1)
    h = candidate.get("height", 1)
    if w and h:
        ratio = w / h
        if ratio < 0.3 or ratio > 5:
            score -= 2.0
    
    # Prefer larger images
    if w < 400:
        score -= 1.0
    
    return score


def download_image(url, dest_path):
    """Download image from URL to dest_path."""
    if dest_path.exists():
        return True
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    data_bytes = wiki.get(url=url)
    if data_bytes is None:
        return False
    dest_path.write_bytes(data_bytes)
    return True


def write_attribution_sidecar(candidate, image_path, old_file=None):
    """Write .attribution.json sidecar with 7 required fields."""
    file_title = candidate.get("file_title", "").replace("File:", "").replace("_", " ")
    title = candidate.get("object_name", "") or file_title
    
    # Build license_url fallback
    license_name = candidate.get("license", "")
    license_url = candidate.get("license_url", "")
    if not license_url:
        fallbacks = {
            "public domain": "https://creativecommons.org/publicdomain/mark/1.0/",
            "public domain mark": "https://creativecommons.org/publicdomain/mark/1.0/",
            "pd": "https://creativecommons.org/publicdomain/mark/1.0/",
            "pd-old-70": "https://creativecommons.org/publicdomain/mark/1.0/",
            "pd-old-100": "https://creativecommons.org/publicdomain/mark/1.0/",
            "pd-art": "https://creativecommons.org/publicdomain/mark/1.0/",
            "pd-us": "https://creativecommons.org/publicdomain/mark/1.0/",
            "cc0": "https://creativecommons.org/publicdomain/zero/1.0/",
        }
        for k, v in fallbacks.items():
            if license_name.lower().startswith(k):
                license_url = v
                break
    
    attr = {
        "title": title,
        "description": candidate.get("description", ""),
        "author": candidate.get("author", ""),
        "license": license_name,
        "license_url": license_url,
        "source_url": candidate.get("page_url", ""),
        "original_url": candidate.get("url", ""),
    }
    
    attr_path = image_path.with_suffix(".attribution.json")
    attr_path.write_text(
        json.dumps(attr, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return attr, attr_path


def resize_if_needed(image_path, max_width=1200):
    """Resize image if wider than max_width using Pillow."""
    try:
        from PIL import Image
        img = Image.open(image_path)
        w, h = img.size
        if w > max_width:
            new_h = int(h * max_width / w)
            img = img.resize((max_width, new_h), Image.LANCZOS)
            img.save(image_path)
            print(f"    Resized from {w}x{h} to {max_width}x{new_h}")
            return True
    except ImportError:
        pass
    except Exception as e:
        print(f"    Resize skipped: {e}")
    return False


def load_audit():
    """Load vision-audit.json."""
    return json.loads(AUDIT_FILE.read_text(encoding="utf-8"))


def save_audit(audit):
    """Save vision-audit.json."""
    AUDIT_FILE.write_text(
        json.dumps(audit, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def load_manifest():
    """Load images.json."""
    if MANIFEST_FILE.exists():
        try:
            return json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {"$schema": "bootciv-images-v1", "nodes": {}}


def save_manifest(manifest):
    """Save images.json."""
    MANIFEST_FILE.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def process_entry(key, entry, audit, manifest, args, index, total):
    """Process a single replace entry."""
    domain = entry.get("domain")
    file_name = entry.get("file", "")
    article_title = entry.get("article_title", "")
    reason = entry.get("reason", "")
    
    # Skip old hero entries (domain=None)
    if domain is None:
        # Check if already replaced in replacements section
        path_parts = key.split("/")
        domain_name = path_parts[0] if len(path_parts) == 2 else None
        replacements = audit.get("replacements", {})
        if domain_name and domain_name in replacements:
            entry["verdict"] = "replaced"
            entry["replacement_note"] = "Hero image already replaced in Task 5"
            return "already_replaced"
        elif domain_name:
            # Energy and measurement were kept
            entry["verdict"] = "kept-original"
            entry["replacement_note"] = "Hero image kept (scored above threshold)"
            return "kept_original"
        return "skipped"
    
    domain_dir = IMAGES_DIR / domain
    current_image = domain_dir / file_name
    
    if not current_image.exists():
        print(f"  [{index}/{total}] SKIP {key}: file not found at {current_image}")
        entry["verdict"] = "kept-original"
        entry["replacement_note"] = f"Original file missing, cannot verify replacement"
        return "file_missing"
    
    # Build search queries
    queries = build_search_queries(article_title, domain, reason, file_name)
    print(f"  [{index}/{total}] {key}")
    print(f"    Title: {article_title}")
    print(f"    Queries: {queries}")
    
    best_candidate = None
    best_score = -999
    
    # Get the current file's Commons title to exclude it from results
    current_attr_path = (domain_dir / file_name).with_suffix(".attribution.json")
    current_source = ""
    if current_attr_path.exists():
        try:
            current_attr = json.loads(current_attr_path.read_text(encoding="utf-8"))
            current_source = current_attr.get("original_url", "")
        except (json.JSONDecodeError, OSError):
            pass
    
    for qi, query in enumerate(queries):
        if qi > 0:
            time.sleep(RATE_LIMIT_SECONDS)
        
        print(f"    Query {qi+1}/{len(queries)}: '{query}'")
        candidates = search_commons(query, limit=15)
        
        if not candidates:
            print(f"      No results")
            continue
        
        # Filter out the current image (same source URL or same file title)
        if current_source:
            candidates = [c for c in candidates if c.get("url", "") != current_source]
        
        # Score and rank candidates
        for c in candidates:
            c["_score"] = score_relevance(article_title, c)
        
        candidates.sort(key=lambda c: c["_score"], reverse=True)
        
        if not candidates:
            print(f"      No suitable candidates after filtering")
            continue
        
        top = candidates[0]
        print(f"      Best: {top['file_title']} (score={top['_score']:.1f}, {top['width']}x{top['height']}, {top['license']})")
        
        if top["_score"] > best_score:
            best_score = top["_score"]
            best_candidate = top
    
    if best_candidate is None or best_score < 2.0:
        print(f"    NO suitable replacement found after {len(queries)} queries")
        entry["verdict"] = "kept-original"
        entry["replacement_note"] = f"No suitable replacement found after {len(queries)} queries (best_score={best_score:.1f})"
        return "no_suitable"
    
    if args.dry_run:
        print(f"    DRY-RUN: Would download {best_candidate['file_title']}")
        return "dry_run"
    
    # Download replacement
    thumb_url = best_candidate.get("thumbnail_url") or best_candidate.get("url", "")
    if not thumb_url:
        print(f"    No download URL available")
        entry["verdict"] = "kept-original"
        entry["replacement_note"] = "No download URL for best candidate"
        return "no_url"
    
    mime = best_candidate.get("mime", "image/jpeg")
    new_ext = MIME_EXT.get(mime, ".jpg")
    
    # Keep the same base filename but possibly change extension
    base_name = Path(file_name).stem
    new_file_name = base_name + new_ext
    new_image_path = domain_dir / new_file_name
    
    print(f"    Downloading to {new_image_path}")
    if not download_image(thumb_url, new_image_path):
        print(f"    Download FAILED")
        entry["verdict"] = "kept-original"
        entry["replacement_note"] = f"Download failed for {best_candidate['file_title']}"
        return "download_failed"
    
    # Resize if needed
    resize_if_needed(new_image_path)
    
    # Remove old file if extension changed
    if new_file_name != file_name:
        old_path = domain_dir / file_name
        if old_path.exists() and old_path != new_image_path:
            old_path.unlink()
            print(f"    Removed old file: {file_name}")
            # Also remove old attribution if exists
            old_attr = old_path.with_suffix(".attribution.json")
            if old_attr.exists():
                old_attr.unlink()
    
    # Write attribution sidecar
    attr, attr_path = write_attribution_sidecar(best_candidate, new_image_path, file_name)
    
    # Update vision-audit.json entry
    entry["verdict"] = "replaced"
    entry["replacement"] = {
        "new_file": new_file_name,
        "source": best_candidate["file_title"],
        "author": best_candidate.get("author", ""),
        "license": best_candidate.get("license", ""),
        "width": best_candidate.get("width", 0),
        "height": best_candidate.get("height", 0),
        "score": round(best_score, 1),
    }
    if new_file_name != file_name:
        entry["replacement"]["old_file"] = file_name
        entry["replacement"]["extension_changed"] = True
    
    # Update images.json
    # Find the node entry that corresponds to this image
    node_id = f"{domain}.{base_name.replace(domain + '_', '')}"
    if node_id in manifest["nodes"]:
        node_entry = manifest["nodes"][node_id]
        node_entry["status"] = "downloaded"
        node_entry["local_path"] = f"docs/images/{domain}/{new_file_name}"
        node_entry["attribution"] = {
            "title": attr["title"],
            "description": attr["description"],
            "author": attr["author"],
            "license": attr["license"],
            "license_url": attr["license_url"],
            "source_url": attr["source_url"],
        }
        # Add new candidate at top
        if "candidates" not in node_entry:
            node_entry["candidates"] = []
        node_entry["candidates"].insert(0, {
            "file_title": best_candidate["file_title"],
            "url": best_candidate.get("url", ""),
            "thumbnail_url": best_candidate.get("thumbnail_url", ""),
            "width": best_candidate.get("width", 0),
            "height": best_candidate.get("height", 0),
            "mime": mime,
            "description": best_candidate.get("description", ""),
            "license": best_candidate.get("license", ""),
            "license_url": best_candidate.get("license_url", ""),
            "author": best_candidate.get("author", ""),
            "page_url": best_candidate.get("page_url", ""),
        })
    
    print(f"    OK: replaced with {best_candidate['file_title']}")
    return "replaced"


def main():
    global wiki
    
    parser = argparse.ArgumentParser(
        description="Batch replace failed images from vision-audit.json with Wikimedia Commons images"
    )
    parser.add_argument("--domain", default=None,
                        help="Process only one domain's images")
    parser.add_argument("--dry-run", action="store_true", default=False,
                        help="Search only, don't download")
    parser.add_argument("--limit", type=int, default=0,
                        help="Max images to process (0 = all)")
    parser.add_argument("--force", action="store_true", default=False,
                        help="Re-process entries already marked as replaced/kept-original")
    parser.add_argument("--delay", type=float, default=1.0,
                        help="Delay between API calls in seconds (default: 1.0)")
    args = parser.parse_args()
    
    global RATE_LIMIT_SECONDS
    RATE_LIMIT_SECONDS = args.delay
    
    wiki = WikiClient()
    
    audit = load_audit()
    manifest = load_manifest()
    results = audit["results"]
    
    # Collect entries to process
    to_process = []
    for key, entry in results.items():
        if entry.get("verdict") != "replace":
            if not args.force:
                continue
        
        domain = entry.get("domain")
        if args.domain and domain != args.domain:
            continue
        
        # Skip old hero entries unless explicitly requested
        if domain is None and args.domain is None:
            to_process.append((key, entry))
            continue
        
        to_process.append((key, entry))
    
    total = len(to_process)
    print(f"Found {total} entries to process")
    if args.domain:
        print(f"  Filtered to domain: {args.domain}")
    if args.dry_run:
        print(f"  DRY-RUN mode: no downloads")
    print()
    
    stats = {"replaced": 0, "no_suitable": 0, "download_failed": 0,
             "no_url": 0, "file_missing": 0, "already_replaced": 0,
             "kept_original": 0, "skipped": 0, "dry_run": 0}
    
    checkpoint_interval = 10
    
    for i, (key, entry) in enumerate(to_process, 1):
        if args.limit > 0 and i > args.limit:
            print(f"  Limit reached ({args.limit})")
            break
        
        status = process_entry(key, entry, audit, manifest, args, i, total)
        stats[status] = stats.get(status, 0) + 1
        
        # Checkpoint
        if i % checkpoint_interval == 0:
            save_audit(audit)
            save_manifest(manifest)
            print(f"\n  [checkpoint: {i}/{total} processed]\n")
    
    # Final save
    save_audit(audit)
    save_manifest(manifest)
    
    # Update summary counts
    new_replace_count = sum(1 for e in results.values() if e.get("verdict") == "replace")
    new_replaced_count = sum(1 for e in results.values() if e.get("verdict") == "replaced")
    new_kept_count = sum(1 for e in results.values() if e.get("verdict") == "kept-original")
    
    audit["flagged_count"] = new_replace_count
    if "replacement_count" not in audit:
        audit["replacement_count"] = 0
    audit["replacement_count"] += stats.get("replaced", 0)
    save_audit(audit)
    
    elapsed = 0  # Not tracking in this version
    print()
    print("=== Summary ===")
    print(f"  Total processed:   {total}")
    print(f"  Replaced:          {stats.get('replaced', 0)}")
    print(f"  Kept original:     {stats.get('kept_original', 0)}")
    print(f"  No suitable:       {stats.get('no_suitable', 0)}")
    print(f"  Download failed:   {stats.get('download_failed', 0)}")
    print(f"  File missing:      {stats.get('file_missing', 0)}")
    print(f"  Already replaced:  {stats.get('already_replaced', 0)}")
    print(f"  Dry run:           {stats.get('dry_run', 0)}")
    print()
    print(f"  Remaining 'replace' verdicts: {new_replace_count}")
    print(f"  Total 'replaced': {new_replaced_count}")
    print(f"  Total 'kept-original': {new_kept_count}")


if __name__ == "__main__":
    main()
