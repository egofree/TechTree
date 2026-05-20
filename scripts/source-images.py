#!/usr/bin/env python3
# Search Wikimedia Commons for open-licensed images for each node in the bootciv tech tree.
# Downloads thumbnails and creates a structured manifest at data/images.json.
# Requires: Python 3.8+ (stdlib only, no pip dependencies)
# Usage: python scripts/source-images.py [--dry-run] [--node NODE_ID] [--domain DOMAIN] [--limit N] [--force]

import argparse
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.wiki_client import WikiClient

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
NODES_FILE = DATA_DIR / "nodes.json"
MANIFEST_FILE = DATA_DIR / "images.json"
IMAGES_DIR = PROJECT_DIR / "docs" / "images"

wiki = WikiClient()


SAFE_LICENSES = {
    "cc0", "public domain", "public domain mark", "pd-old-70", "pd-old-100",
    "pd-art", "pd-us", "pd-user",
    "cc by 1.0", "cc by 2.0", "cc by 2.5", "cc by 3.0", "cc by 4.0",
    "cc by-sa 1.0", "cc by-sa 2.0", "cc by-sa 2.5", "cc by-sa 3.0", "cc by-sa 4.0",
}

MIME_EXT = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/gif": ".gif",
    "image/svg+xml": ".svg",
    "image/webp": ".webp",
    "image/tiff": ".tiff",
}


def license_is_safe(license_short):
    if not license_short:
        return False
    normalized = license_short.strip().lower()
    for safe in SAFE_LICENSES:
        if normalized == safe or normalized.startswith(safe):
            return True
    return False


def clean_query_term(text):
    cleaned = re.sub(r"[&,.'\-()]", " ", text)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def build_search_queries(node):
    name = node.get("name", "")
    tags = node.get("tags", {})
    domain = node["id"].split(".")[0]

    name_terms = clean_query_term(name)
    material_terms = " ".join(tags.get("material", []))
    capability_terms = " ".join(tags.get("capability", []))

    queries = []
    if name_terms:
        queries.append(name_terms)
    tag_combined = "{} {}".format(material_terms, capability_terms).strip()
    if tag_combined and tag_combined != name_terms.lower():
        queries.append(tag_combined)
    if not queries:
        queries.append(domain)
    return queries[:2]


def parse_candidates(data, limit):
    candidates = []
    if not data or "query" not in data:
        return candidates
    pages = data["query"].get("pages", {})
    for page_id in sorted(pages.keys()):
        info_list = pages[page_id].get("imageinfo", [])
        if not info_list:
            continue
        info = info_list[0]
        ext = info.get("extmetadata", {})
        license_short = (ext.get("LicenseShortName", {}).get("value", "") or "").strip()
        if not license_is_safe(license_short):
            continue
        mime = info.get("mime", "")
        if mime == "image/svg+xml":
            continue
        description_html = (ext.get("ImageDescription", {}).get("value", "") or "").strip()
        object_name = (ext.get("ObjectName", {}).get("value", "") or "").strip()
        categories_html = (ext.get("Categories", {}).get("value", "") or "").strip()
        candidates.append({
            "file_title": pages[page_id].get("title", ""),
            "url": info.get("url", ""),
            "thumbnail_url": info.get("thumburl", ""),
            "width": info.get("width", 0),
            "height": info.get("height", 0),
            "mime": info.get("mime", "image/jpeg"),
            "description": strip_html(description_html),
            "object_name": strip_html(object_name) if object_name else "",
            "categories": strip_html(categories_html),
            "license": license_short,
            "license_url": (ext.get("LicenseUrl", {}).get("value", "") or "").strip(),
            "author": (ext.get("Artist", {}).get("value", "") or "").strip(),
            "author_html": (ext.get("Artist", {}).get("value", "") or "").strip(),
            "page_url": info.get("descriptionurl", ""),
        })
        if len(candidates) >= limit:
            break
    return candidates


def strip_html(text):
    return re.sub(r"<[^>]+>", "", text).strip()


def sanitize_filename(node_id):
    return node_id.replace(".", "_")


def load_manifest():
    if MANIFEST_FILE.exists():
        try:
            return json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {"$schema": "bootciv-images-v1", "nodes": {}}


def save_manifest(manifest):
    MANIFEST_FILE.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def download_image(url, dest_path):
    if dest_path.exists():
        return True
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    data = wiki.get(url=url)
    if data is None:
        return False
    dest_path.write_bytes(data)
    return True


def build_attribution_md(candidate):
    author = strip_html(candidate.get("author", ""))
    license_name = candidate.get("license", "")
    license_url = candidate.get("license_url", "")
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


def write_attribution_file(candidate, image_path):
    attr = {
        "title": candidate.get("object_name", "") or candidate.get("file_title", "").replace("File:", "").replace("_", " "),
        "description": candidate.get("description", ""),
        "author": strip_html(candidate.get("author", "")),
        "license": candidate.get("license", ""),
        "license_url": candidate.get("license_url", ""),
        "source_url": candidate.get("page_url", ""),
        "original_url": candidate.get("url", ""),
        "attribution_md": build_attribution_md(candidate),
    }
    attr_path = image_path.with_suffix(".attribution.json")
    attr_path.write_text(
        json.dumps(attr, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return attr_path


def process_node(node, manifest, args, index, total):
    node_id = node["id"]
    node_name = node.get("name", node_id)
    domain = node_id.split(".")[0]

    if not args.force and node_id in manifest["nodes"]:
        existing = manifest["nodes"][node_id]
        if existing.get("status") in ("has_candidates", "downloaded", "no_results"):
            return "skipped"

    queries = build_search_queries(node)
    print("Searching: {} ({}/{})...".format(node_id, index, total))

    all_candidates = []
    seen_titles = set()
    for query in queries:
        params = {
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrnamespace": "6",
            "gsrsearch": query,
            "gsrlimit": str(args.limit),
            "prop": "imageinfo",
            "iiprop": "url|size|extmetadata|mime",
            "iiextmetadatafilter": "LicenseShortName|License|LicenseUrl|Artist|ImageDescription|ObjectName|Categories",
            "iiurlwidth": "800",
        }
        data = wiki.get_json(params=params)
        candidates = parse_candidates(data, args.limit)
        for c in candidates:
            if c["file_title"] not in seen_titles:
                seen_titles.add(c["file_title"])
                all_candidates.append(c)
        time.sleep(1)

    clean_candidates = []
    for c in all_candidates:
        clean_candidates.append({
            "file_title": c["file_title"],
            "url": c["url"],
            "thumbnail_url": c["thumbnail_url"],
            "width": c["width"],
            "height": c["height"],
            "mime": c.get("mime", "image/jpeg"),
            "description": c.get("description", ""),
            "object_name": c.get("object_name", ""),
            "categories": c.get("categories", ""),
            "license": c["license"],
            "license_url": c["license_url"],
            "author": strip_html(c["author"]),
            "author_html": c.get("author_html", ""),
            "page_url": c["page_url"],
        })

    if not clean_candidates:
        status = "no_results"
    else:
        status = "has_candidates"

    entry = {
        "node_name": node_name,
        "domain": domain,
        "search_queries": queries,
        "status": status,
        "candidates": clean_candidates,
        "selected": None,
        "local_path": None,
        "attribution": None,
    }

    if not args.dry_run and clean_candidates:
        best = all_candidates[0] if all_candidates else None
        if best:
            thumb_url = best.get("thumbnail_url") or best.get("url", "")
            mime = best.get("mime", "image/jpeg")
            if thumb_url:
                ext = MIME_EXT.get(mime, ".jpg")
                fname = sanitize_filename(node_id) + ext
                local_rel = "docs/images/{}/{}".format(domain, fname)
                dest = PROJECT_DIR / "docs" / "images" / domain / fname

                if download_image(thumb_url, dest):
                    entry["status"] = "downloaded"
                    entry["local_path"] = local_rel
                    write_attribution_file(best, dest)
                    entry["attribution"] = {
                        "title": best.get("object_name", "") or best.get("file_title", "").replace("File:", "").replace("_", " "),
                        "description": best.get("description", ""),
                        "author": strip_html(best.get("author", "")),
                        "license": best.get("license", ""),
                        "license_url": best.get("license_url", ""),
                        "source_url": best.get("page_url", ""),
                        "attribution_md": build_attribution_md(best),
                    }

    manifest["nodes"][node_id] = entry
    return entry["status"]


def main():
    parser = argparse.ArgumentParser(
        description="Search Wikimedia Commons for open-licensed images for bootciv nodes"
    )
    parser.add_argument("--dry-run", action="store_true", default=False,
                        help="Search only, don't download")
    parser.add_argument("--node", dest="node_id", default=None,
                        help="Process only one specific node")
    parser.add_argument("--domain", default=None,
                        help="Process only one domain's nodes")
    parser.add_argument("--limit", type=int, default=10,
                        help="Max search results per node (default: 10)")
    parser.add_argument("--force", action="store_true", default=False,
                        help="Re-search even if node already has candidates")
    args = parser.parse_args()

    if not NODES_FILE.exists():
        print("ERROR: {} not found".format(NODES_FILE), file=sys.stderr)
        sys.exit(1)

    nodes_data = json.loads(NODES_FILE.read_text(encoding="utf-8"))
    all_nodes = nodes_data.get("nodes", [])

    if args.node_id:
        nodes = [n for n in all_nodes if n["id"] == args.node_id]
        if not nodes:
            print("ERROR: Node '{}' not found".format(args.node_id), file=sys.stderr)
            sys.exit(1)
    elif args.domain:
        nodes = [n for n in all_nodes if n["id"].split(".")[0] == args.domain]
        if not nodes:
            print("ERROR: Domain '{}' not found".format(args.domain), file=sys.stderr)
            sys.exit(1)
    else:
        nodes = all_nodes

    manifest = load_manifest()
    total = len(nodes)

    print("Processing {} nodes...".format(total))
    if args.dry_run:
        print("  (dry-run mode: no downloads)")
    print()

    stats = {"searched": 0, "skipped": 0, "has_candidates": 0,
             "no_results": 0, "downloaded": 0}

    for i, node in enumerate(nodes, 1):
        status = process_node(node, manifest, args, i, total)
        if status == "skipped":
            stats["skipped"] += 1
        else:
            stats["searched"] += 1
            if status == "downloaded":
                stats["downloaded"] += 1
            elif status == "has_candidates":
                stats["has_candidates"] += 1
            elif status == "no_results":
                stats["no_results"] += 1

    save_manifest(manifest)

    print()
    print("=== Summary ===")
    print("  Total nodes:      {}".format(total))
    print("  Searched:         {}".format(stats["searched"]))
    print("  Skipped (cached): {}".format(stats["skipped"]))
    print("  Has candidates:   {}".format(stats["has_candidates"]))
    print("  No results:       {}".format(stats["no_results"]))
    print("  Downloaded:       {}".format(stats["downloaded"]))
    print("  Manifest:         {}".format(MANIFEST_FILE))


if __name__ == "__main__":
    main()
