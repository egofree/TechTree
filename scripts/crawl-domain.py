#!/usr/bin/env python3
"""Config-driven Wikipedia crawler for bootciv tech tree domains.

Reads a domain config YAML (e.g. domains/plants.yaml), then runs a 6-stage
pipeline: discover → fetch → extract → classify → write_catalog → generate_patch.

Requires: Python 3.8+, pyyaml (no other pip dependencies)
Usage:
    python scripts/crawl-domain.py --domain plants --dry-run --limit 3
    python scripts/crawl-domain.py --domain plants
    python scripts/crawl-domain.py --domain nonexistent  (exits non-zero)
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.wiki_client import WikiClient
from lib.rate_limiter import RateLimiter
from lib.data_utils import (
    load_manifest,
    save_manifest,
    generate_node_patch,
    create_checkpoint,
    rollback,
    rollback_on_failure,
    list_checkpoints,
)

# ---------------------------------------------------------------------------
# Imports for extraction modules
# ---------------------------------------------------------------------------

try:
    from lib.article_extractor import extract_plant_data
except ImportError:
    def extract_plant_data(html, title, config=None):
        """Fallback stub: returns minimal extracted data."""
        return {
            "common_names": [title] if title else [],
            "extraction_quality": "stub",
            "needs_research": True,
        }

try:
    from lib.sparql_client import SparqlClient
except ImportError:
    SparqlClient = None

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
DOMAINS_DIR = SCRIPT_DIR / "domains"

WIKI_API_BASE = "https://en.wikipedia.org/w/api.php"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def title_from_url(url):
    """Extract a Wikipedia article title from a full URL.

    Handles URLs like:
        https://en.wikipedia.org/wiki/Plant
        https://en.wikipedia.org/wiki/Cereal
    Returns the title portion (URL-decoded), or the original string if it
    doesn't look like a Wikipedia URL.
    """
    match = re.match(
        r"https?://\w+\.wikipedia\.org/wiki/(.+)$", url.strip()
    )
    if match:
        return match.group(1).replace("_", " ")
    return url


def kebab(text):
    """Convert text to kebab-case for node IDs."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


# ---------------------------------------------------------------------------
# Stage 1: Discover
# ---------------------------------------------------------------------------


def _fetch_category_members(categories, client, limiter, max_per_category=50):
    """Query Wikipedia API for members of each category.

    Uses the MediaWiki `categorymembers` API to enumerate pages that belong
    to the given categories. Filters out non-article namespaces (Category:,
    File:, Template:, etc.) and disambiguation pages.

    Args:
        categories: List of category strings (e.g. ["Category:Edible plants"]).
        client: WikiClient instance for HTTP transport.
        limiter: RateLimiter instance.
        max_per_category: Max members to fetch per category.

    Returns:
        List of dicts: {"title": str, "url": str}
    """
    members = []
    seen = set()

    for category in categories:
        cat_title = category.strip()
        if not cat_title.startswith("Category:"):
            cat_title = "Category:{}".format(cat_title)

        limiter.wait()
        print("    Querying category: {}".format(cat_title))

        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": cat_title,
            "cmlimit": str(min(max_per_category, 50)),
            "cmtype": "page",
            "format": "json",
        }
        data = client.get_json(params=params)

        if not data or "query" not in data:
            print("      WARNING: no data for category '{}'".format(cat_title))
            continue

        raw_members = data.get("query", {}).get("categorymembers", [])
        for m in raw_members:
            title = m.get("title", "")
            if not title:
                continue
            # Skip non-main-namespace pages
            if any(title.startswith(prefix) for prefix in (
                "Category:", "File:", "Template:", "Wikipedia:",
                "Help:", "Portal:", "Draft:", "Module:",
            )):
                continue
            if title in seen:
                continue
            seen.add(title)
            encoded = title.replace(" ", "_")
            url = "https://en.wikipedia.org/wiki/{}".format(encoded)
            members.append({"title": title, "url": url})

        print("      Found {} members (total so far: {})".format(
            len([m for m in raw_members if m.get("title", "") in seen]),
            len(members),
        ))

    return members


def _check_external_source(source):
    """Test connectivity to an external_api source.

    Attempts a HEAD request to the source URL. Returns (accessible, status_msg).
    """
    url = source.get("url", "")
    if not url:
        return False, "no URL configured"

    try:
        req = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "bootciv-crawler/1.0"},
        )
        resp = urllib.request.urlopen(req, timeout=10)
        return True, "HTTP {}".format(resp.status)
    except urllib.error.HTTPError as exc:
        return False, "HTTP {} (blocked)".format(exc.code)
    except urllib.error.URLError as exc:
        return False, "URL error: {}".format(exc.reason)
    except Exception as exc:
        return False, str(exc)


def discover(config, source_filter=None, limit=None, client=None, limiter=None):
    """Read seeds, categories, and SPARQL sources. Return article candidates.

    Each candidate is a dict:
        {"title": str, "url": str, "source_name": str, "source_type": str}

    Args:
        config: Parsed domain config dict (from YAML).
        source_filter: If set, only use sources whose name matches.
        limit: Max number of candidates to return (None = unlimited).
        client: WikiClient instance (needed for category member fetching).
        limiter: RateLimiter instance (needed for category member fetching).

    Returns:
        List of candidate dicts.
    """
    candidates = []
    seen_titles = set()
    sources = config.get("sources", [])

    for source in sources:
        name = source.get("name", "")
        stype = source.get("type", "")

        if source_filter and name != source_filter:
            continue

        if stype == "external_api":
            accessible, status_msg = _check_external_source(source)
            if not accessible:
                fallback = source.get("fallback", "")
                print("    Source '{}' ({}) unavailable: {}".format(
                    name, source.get("url", ""), status_msg,
                ))
                print("    Flagging as unavailable. Fallback: {}".format(
                    fallback or "none",
                ))
                source["status"] = "unavailable"
                source["status_detail"] = status_msg
                continue
            print("    Source '{}' ({}) accessible: {}".format(
                name, source.get("url", ""), status_msg,
            ))
            print("    NOTE: no fetcher implemented for '{}' yet".format(name))
            continue

        for seed_url in source.get("seeds", []):
            title = title_from_url(seed_url)
            if title and title not in seen_titles:
                seen_titles.add(title)
                candidates.append({
                    "title": title,
                    "url": seed_url,
                    "source_name": name,
                    "source_type": stype,
                })

        categories = source.get("follow_categories", [])
        if categories and client and limiter:
            cat_members = _fetch_category_members(
                categories, client, limiter,
                max_per_category=limit or 50,
            )
            for m in cat_members:
                if m["title"] not in seen_titles:
                    seen_titles.add(m["title"])
                    candidates.append({
                        "title": m["title"],
                        "url": m["url"],
                        "source_name": name,
                        "source_type": "category_member",
                    })

        if stype == "sparql" and SparqlClient is not None:
            try:
                sparql = SparqlClient(
                    client=client or WikiClient(),
                    limiter=limiter or RateLimiter(requests_per_second=1),
                )
                species = sparql.get_plant_species(
                    limit=limit or 100,
                    config=config,
                )
                for sp in species:
                    sp_title = sp.get("label", sp.get("scientific_name", ""))
                    if sp_title and sp_title not in seen_titles:
                        seen_titles.add(sp_title)
                        candidates.append({
                            "title": sp_title,
                            "url": "",
                            "source_name": name,
                            "source_type": stype,
                        })
            except Exception as exc:
                print("    WARNING: SPARQL query failed: {}".format(exc))

    if limit is not None:
        candidates = candidates[:limit]

    return candidates


# ---------------------------------------------------------------------------
# Stage 2: Fetch
# ---------------------------------------------------------------------------


def fetch(candidates, config, client, limiter):
    """Download article content via WikiClient, rate-limited.

    Skips category entries (no article to fetch). Uses the MediaWiki parse
    API to retrieve page HTML.

    Args:
        candidates: List of candidate dicts from discover().
        config: Domain config dict.
        client: WikiClient instance.
        limiter: RateLimiter instance.

    Returns:
        List of article dicts: {"title": str, "html": str, "source_name": str}
    """
    articles = []
    limits = config.get("limits", {})
    max_species = limits.get("max_species", 100)

    for candidate in candidates:
        title = candidate["title"]
        source_name = candidate["source_name"]

        # Skip category placeholders — they aren't real articles
        if title.startswith("Category:"):
            continue

        if len(articles) >= max_species:
            break

        limiter.wait()

        print("  Fetching: {}".format(title))
        params = {
            "action": "parse",
            "page": title,
            "prop": "text",
            "formatversion": "2",
            "format": "json",
            "redirects": "1",
        }
        data = client.get_json(params=params)

        if data and "parse" in data:
            html = data["parse"].get("text", "")
            resolved_title = data["parse"].get("title", title)
            articles.append({
                "title": resolved_title,
                "html": html,
                "source_name": source_name,
            })
        else:
            print("    WARNING: no data returned for '{}'".format(title))

    return articles


# ---------------------------------------------------------------------------
# Stage 3: Extract
# ---------------------------------------------------------------------------


def extract(articles, config):
    """Call article_extractor to parse article HTML into structured data.

    Args:
        articles: List of article dicts from fetch().
        config: Domain config dict (passed to extractor for patterns).

    Returns:
        List of entry dicts with extracted fields.
    """
    entries = []
    for article in articles:
        title = article["title"]
        html = article["html"]
        source_name = article["source_name"]

        extracted = extract_plant_data(html, title, config=config)

        entries.append({
            "title": title,
            "source_name": source_name,
            "extracted": extracted,
        })

    print("  Extracted {} entries".format(len(entries)))
    return entries


# ---------------------------------------------------------------------------
# Stage 4: Classify
# ---------------------------------------------------------------------------


def classify(entries, config):
    """Map extracted data to use_categories via keyword matching from config.

    Each entry gets a ``use_category`` field based on the first matching
    category whose keywords appear in the article's extracted text/title.

    Args:
        entries: List of entry dicts from extract().
        config: Domain config dict with ``extraction.use_categories``.

    Returns:
        List of entry dicts with added ``use_category`` and ``category_tags``.
    """
    use_categories = config.get("extraction", {}).get("use_categories", [])
    classified = 0

    for entry in entries:
        title = entry["title"].lower()
        extracted = entry.get("extracted", {})

        # Build searchable text from title + extracted fields
        text_parts = [title]
        if isinstance(extracted, dict):
            for key in ("common_names", "uses", "description"):
                val = extracted.get(key)
                if isinstance(val, list):
                    text_parts.extend(str(v).lower() for v in val)
                elif isinstance(val, str):
                    text_parts.append(val.lower())
        searchable = " ".join(text_parts)

        matched_category = None
        matched_tags = {}

        for cat in use_categories:
            cat_id = cat.get("id", "")
            keywords = cat.get("keywords", [])
            for kw in keywords:
                if kw.lower() in searchable:
                    matched_category = cat_id
                    matched_tags = cat.get("tags", {})
                    break
            if matched_category:
                break

        if matched_category:
            entry["use_category"] = matched_category
            entry["category_tags"] = matched_tags
            classified += 1
        else:
            entry["use_category"] = "uncategorized"
            entry["category_tags"] = {}

    print("  Classified: {}/{} matched a category".format(
        classified, len(entries)
    ))
    return entries


# ---------------------------------------------------------------------------
# Stage 5: Write catalog
# ---------------------------------------------------------------------------


def write_catalog(entries, config, output_dir=None, force=False):
    """Write species entries to catalog JSON.

    Produces a catalog with species array and needs_research list matching
    the bootciv-plants-catalog-v1 schema.

    Args:
        entries: List of classified entry dicts.
        config: Domain config dict with ``output.catalog`` path.
        output_dir: Override output directory (replaces data/ prefix).
        force: Re-write even if entry already exists in catalog.

    Returns:
        Tuple of (catalog_path, written_count, skipped_count).
    """
    output_config = config.get("output", {})
    catalog_rel = output_config.get("catalog", "data/{}.json".format(
        config.get("domain", "unknown")
    ))

    if output_dir:
        catalog_path = Path(output_dir) / Path(catalog_rel).name
    else:
        catalog_path = PROJECT_DIR / catalog_rel

    existing_catalog = load_manifest(str(catalog_path))
    existing_ids = set()
    if existing_catalog and "species" in existing_catalog:
        existing_ids = {s.get("id", "") for s in existing_catalog["species"]}

    species_list = list(existing_catalog.get("species", [])) if existing_catalog else []
    needs_research_ids = list(existing_catalog.get("needs_research", [])) if existing_catalog else []
    needs_research_set = set(needs_research_ids)

    written = 0
    skipped = 0

    for entry in entries:
        title = entry["title"]
        entry_id = kebab(title)
        extracted = entry.get("extracted", {})

        if not force and entry_id in existing_ids:
            skipped += 1
            continue

        species_entry = {
            "id": entry_id,
            "title": title,
            "common_names": extracted.get("common_names", [title] if title else []),
            "scientific_name": extracted.get("scientific_name", ""),
            "primary_use": entry.get("use_category", "uncategorized"),
            "family": extracted.get("family", ""),
            "order": extracted.get("order", ""),
            "native_region": extracted.get("native_region", ""),
            "uses": extracted.get("uses", []),
            "description": extracted.get("description", ""),
            "source_url": extracted.get("source_url", ""),
            "extraction_quality": extracted.get("extraction_quality", "minimal"),
            "needs_research": bool(extracted.get("needs_research", True)),
            "source": entry.get("source_name", ""),
        }

        species_list.append(species_entry)
        written += 1

        if species_entry["needs_research"]:
            needs_research_set.add(entry_id)
        elif entry_id in needs_research_set:
            needs_research_set.discard(entry_id)

    source_stats = {}
    for sp in species_list:
        src = sp.get("source", "unknown")
        source_stats[src] = source_stats.get(src, 0) + 1

    catalog = {
        "$schema": "bootciv-plants-catalog-v1",
        "domain": config.get("domain", ""),
        "generated": datetime.now(timezone.utc).isoformat(),
        "source_stats": source_stats,
        "species": species_list,
        "needs_research": sorted(needs_research_set),
    }

    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    save_manifest(str(catalog_path), catalog)

    print("  Catalog: {} written, {} skipped → {}".format(
        written, skipped, catalog_path
    ))
    return str(catalog_path), written, skipped


# ---------------------------------------------------------------------------
# Stage 6: Generate patch
# ---------------------------------------------------------------------------


def generate_patch(entries, config, output_dir=None):
    """Generate proposed nodes.json/edges.json patches using data_utils.

    Uses the ``node_mapping`` config section to build node IDs from the
    classified entries, then calls ``generate_node_patch`` to diff against
    existing data.

    Args:
        entries: List of classified entry dicts.
        config: Domain config dict with ``node_mapping`` and ``output``.
        output_dir: Override output directory.

    Returns:
        Tuple of (patch_path, patch_dict) or (None, {}) if no new nodes.
    """
    output_config = config.get("output", {})
    mapping = config.get("node_mapping", {})
    defaults = config.get("defaults", {})

    group_by = mapping.get("group_by", "use_category")
    cap_template = mapping.get("capability_template", "{category}-plants")
    proc_template = mapping.get("process_template", "{category}-plants.{species}")
    domain = config.get("domain", "unknown")

    new_nodes = []
    new_edges = []

    # Group entries by the classification field
    groups = {}
    for entry in entries:
        cat = entry.get(group_by, "uncategorized")
        groups.setdefault(cat, []).append(entry)

    for cat, cat_entries in sorted(groups.items()):
        cap_id = cap_template.format(category=cat)

        # Capability-level node (one per category)
        cap_node = {
            "id": cap_id,
            "name": "{} plants".format(cat.capitalize()),
            "level": "capability",
            "parent": domain,
            "description": "{} plants used in bootstrapping".format(cat),
            "timeline": defaults.get("era", "stone-age"),
            "outputs": [],
            "critical": defaults.get("critical", False),
            "early_win": defaults.get("early_win", True),
            "pinnacle": defaults.get("pinnacle", False),
            "tags": {
                "material": [],
                "capability": [],
            },
        }
        # Merge category-level tags
        if cat_entries and cat_entries[0].get("category_tags"):
            tags = cat_entries[0]["category_tags"]
            if "material" in tags:
                cap_node["tags"]["material"] = (
                    [tags["material"]] if isinstance(tags["material"], str)
                    else tags["material"]
                )
            if "capability" in tags:
                cap_node["tags"]["capability"] = (
                    [tags["capability"]] if isinstance(tags["capability"], str)
                    else tags["capability"]
                )
        new_nodes.append(cap_node)

        # Edge: domain → capability
        new_edges.append({
            "from": domain,
            "to": cap_id,
            "type": "material",
        })

        # Process-level nodes (one per species)
        for entry in cat_entries:
            species_kebab = kebab(entry["title"])
            proc_id = proc_template.format(
                category=cat,
                species=species_kebab,
            )
            proc_node = {
                "id": proc_id,
                "name": entry["title"],
                "level": "process",
                "parent": cap_id,
                "description": "{} ({})".format(entry["title"], cat),
                "timeline": defaults.get("era", "stone-age"),
                "outputs": [],
                "critical": defaults.get("critical", False),
                "early_win": defaults.get("early_win", True),
                "pinnacle": defaults.get("pinnacle", False),
                "tags": cap_node["tags"],
            }
            new_nodes.append(proc_node)

            new_edges.append({
                "from": cap_id,
                "to": proc_id,
                "type": "tool",
            })

    if not new_nodes:
        print("  No new nodes to patch.")
        return None, {}

    # Diff against existing data
    nodes_path = str(DATA_DIR / "nodes.json")
    edges_path = str(DATA_DIR / "edges.json")
    patch = generate_node_patch(new_nodes, new_edges, nodes_path, edges_path)

    # Write patch file
    patch_rel = output_config.get(
        "nodes_patch",
        "data/patches/{}-nodes-patch.json".format(domain),
    )
    if output_dir:
        patch_path = Path(output_dir) / Path(patch_rel).name
    else:
        patch_path = PROJECT_DIR / patch_rel

    save_manifest(str(patch_path), patch)

    print("  Patch: {} nodes added, {} modified, {} edges → {}".format(
        len(patch.get("nodes_added", [])),
        len(patch.get("nodes_modified", [])),
        len(patch.get("edges_added", [])),
        patch_path,
    ))
    return str(patch_path), patch


# ---------------------------------------------------------------------------
# Dry-run report
# ---------------------------------------------------------------------------


def dry_run_report(config, candidates, source_filter=None, limit=None):
    """Print a summary of what would be crawled without making any requests."""
    domain = config.get("domain", "unknown")
    name = config.get("name", domain)
    sources = config.get("sources", [])

    print("=== Dry-run: {} ({}) ===".format(name, domain))
    print()

    for source in sources:
        sname = source.get("name", "")
        stype = source.get("type", "")
        if source_filter and sname != source_filter:
            continue

        seeds = source.get("seeds", [])
        categories = source.get("follow_categories", [])

        print("  Source: {} (type: {})".format(sname, stype))
        print("    Seeds ({}):".format(len(seeds)))
        for seed in seeds:
            title = title_from_url(seed)
            print("      - {} [{}]".format(title, seed))
        if categories:
            print("    Categories ({}):".format(len(categories)))
            for cat in categories:
                print("      - {}".format(cat))
        print()

    actual_candidates = [c for c in candidates if not c["title"].startswith("Category:")]
    effective_limit = limit or config.get("limits", {}).get("max_species", 100)
    print("  Candidates to fetch: {} (limit: {})".format(
        len(actual_candidates), effective_limit
    ))
    print()
    print("  (dry-run mode: no network requests, no file writes)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Config-driven Wikipedia crawler for bootciv tech tree domains",
    )
    parser.add_argument(
        "--domain",
        default=None,
        help="Domain config to crawl (e.g. 'plants' reads domains/plants.yaml)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Show what would be crawled without making network requests",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Max number of articles to process (default: from config limits)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        default=False,
        help="Re-process even if entries already exist in catalog",
    )
    parser.add_argument(
        "--source",
        default=None,
        help="Only use the named source from the config (e.g. 'wikipedia')",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Write output to this directory instead of project data/",
    )
    parser.add_argument(
        "--rollback",
        default=None,
        metavar="CHECKPOINT",
        help="Rollback to a named checkpoint (timestamp dir name in data/.backups/)",
    )
    parser.add_argument(
        "--list-checkpoints",
        action="store_true",
        default=False,
        help="List available checkpoints and exit",
    )
    args = parser.parse_args()

    # --- Handle --list-checkpoints early exit --------------------------------
    if args.list_checkpoints:
        checkpoints = list_checkpoints()
        if not checkpoints:
            print("No checkpoints found in data/.backups/")
        else:
            print("Available checkpoints (newest first):")
            for cp in checkpoints:
                print("  {} ({} files) {}".format(
                    cp["name"], cp["files"], cp["path"]
                ))
        return

    # --- Handle --rollback early exit ----------------------------------------
    if args.rollback:
        backup_dir = DATA_DIR / ".backups" / args.rollback
        if not backup_dir.is_dir():
            print(
                "ERROR: checkpoint not found: {}".format(args.rollback),
                file=sys.stderr,
            )
            checkpoints = list_checkpoints()
            if checkpoints:
                print("  Available:", file=sys.stderr)
                for cp in checkpoints:
                    print("    {}".format(cp["name"]), file=sys.stderr)
            sys.exit(1)
        success = rollback_on_failure(str(backup_dir))
        sys.exit(0 if success else 1)

    if not args.domain:
        parser.error("--domain is required unless using --list-checkpoints or --rollback")

    # --- Load domain config -------------------------------------------------
    config_path = DOMAINS_DIR / "{}.yaml".format(args.domain)
    if not config_path.exists():
        print(
            "ERROR: domain config not found: {}".format(config_path),
            file=sys.stderr,
        )
        print(
            "  Available domains: {}".format(
                ", ".join(
                    sorted(p.stem for p in DOMAINS_DIR.glob("*.yaml"))
                ) if DOMAINS_DIR.exists() else "(none)"
            ),
            file=sys.stderr,
        )
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    domain = config.get("domain", args.domain)
    name = config.get("name", domain)
    limits = config.get("limits", {})
    effective_limit = args.limit or limits.get("max_species", 100)

    print("=== Crawling: {} ({}) ===".format(name, domain))
    print()

    wiki_client = WikiClient(
        base_url=WIKI_API_BASE,
        max_retries=2,
        retry_delay=3,
    )
    limiter = RateLimiter(
        requests_per_second=limits.get("rate_limit_rps", 1),
        burst=3,
    )

    # --- Stage 1: Discover --------------------------------------------------
    print("[1/6] Discovering candidates...")
    candidates = discover(
        config, source_filter=args.source, limit=effective_limit,
        client=wiki_client, limiter=limiter,
    )
    seed_count = len([c for c in candidates if not c["title"].startswith("Category:")])
    cat_count = len(candidates) - seed_count
    print("  Found {} seeds, {} categories ({} total)".format(
        seed_count, cat_count, len(candidates)
    ))

    if args.dry_run:
        print()
        dry_run_report(config, candidates, source_filter=args.source, limit=args.limit)
        return

    if not candidates:
        unavailable = [
            s for s in config.get("sources", [])
            if s.get("status") == "unavailable"
        ]
        if unavailable and args.source:
            print("Source '{}' unavailable, skipping.".format(args.source))
            for s in unavailable:
                print("  - {}: {}".format(
                    s.get("name", "?"), s.get("status_detail", "unknown"),
                ))
            print()
            print("Done (source unavailable, graceful skip).")
            return
        print("ERROR: no candidates discovered. Check config seeds.", file=sys.stderr)
        sys.exit(1)

    # --- Stage 2: Fetch -----------------------------------------------------
    print()
    print("[2/6] Fetching articles...")
    articles = fetch(candidates, config, wiki_client, limiter)
    print("  Fetched {} articles".format(len(articles)))

    if not articles:
        print("ERROR: no articles fetched. Check seeds and network.", file=sys.stderr)
        sys.exit(1)

    # --- Stage 3: Extract ---------------------------------------------------
    print()
    print("[3/6] Extracting data...")
    entries = extract(articles, config)

    # --- Stage 4: Classify --------------------------------------------------
    print()
    print("[4/6] Classifying entries...")
    entries = classify(entries, config)

    # --- Checkpoint before writes -------------------------------------------
    print()
    print("[checkpoint] Creating data backup before writes...")
    checkpoint_path = None
    try:
        nodes_path = str(DATA_DIR / "nodes.json")
        edges_path = str(DATA_DIR / "edges.json")
        if Path(nodes_path).exists():
            checkpoint_path = create_checkpoint(nodes_path, edges_path)
        else:
            print("  (no existing nodes.json — skipping checkpoint)")
    except Exception as exc:
        print("  WARNING: checkpoint failed: {}".format(exc))

    # --- Stage 5: Write catalog ---------------------------------------------
    print()
    print("[5/6] Writing catalog...")
    try:
        catalog_path, written, skipped = write_catalog(
            entries, config, output_dir=args.output_dir, force=args.force,
        )
    except Exception as exc:
        print("ERROR writing catalog: {}".format(exc), file=sys.stderr)
        if checkpoint_path:
            print("  Attempting rollback from: {}".format(checkpoint_path))
            rollback(checkpoint_path)
        sys.exit(1)

    # --- Stage 6: Generate patch --------------------------------------------
    print()
    print("[6/6] Generating patch...")
    try:
        patch_path, patch = generate_patch(
            entries, config, output_dir=args.output_dir,
        )
    except Exception as exc:
        print("ERROR generating patch: {}".format(exc), file=sys.stderr)
        if checkpoint_path:
            print("  Attempting rollback from: {}".format(checkpoint_path))
            rollback(checkpoint_path)
        sys.exit(1)

    # --- Summary ------------------------------------------------------------
    print()
    print("=== Summary ===")
    print("  Domain:           {}".format(domain))
    print("  Candidates:       {}".format(len(candidates)))
    print("  Articles fetched: {}".format(len(articles)))
    print("  Entries extracted: {}".format(len(entries)))
    classified = len([e for e in entries if e.get("use_category") != "uncategorized"])
    print("  Classified:       {}/{}".format(classified, len(entries)))
    print("  Catalog entries:  {} written, {} skipped".format(written, skipped))
    if patch_path:
        print("  Patch file:       {}".format(patch_path))
    else:
        print("  Patch file:       (none — no new nodes)")
    if checkpoint_path:
        print("  Checkpoint:       {}".format(checkpoint_path))
    print()
    print("Done.")


if __name__ == "__main__":
    main()
