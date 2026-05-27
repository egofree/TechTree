#!/usr/bin/env python3
"""Wikidata crawler for TechTree — search, enrichment, apply, and stub modes.

Modes:
    search  — search Wikidata for entities, output scored TSV for review
    enrich  — build multilingual alias/description cache for entities with Q-IDs
    apply   — write approved Q-IDs from reviewed TSV into entity files
    stub    — pre-fill descriptions from enrichment cache

Usage (run from scripts/ directory):
    python wikidata-crawler.py search --output ../data/wikidata-matches.tsv
    python wikidata-crawler.py enrich
    python wikidata-crawler.py apply ../data/wikidata-matches-reviewed.tsv
    python wikidata-crawler.py stub [--entity <id>] [--dry-run]

Workflow:
    1. Search:  python wikidata-crawler.py search --output ../data/wikidata-matches.tsv
    2. Review:  Open TSV in spreadsheet, set status to 'approved' or 'rejected'
    3. Apply:   python wikidata-crawler.py apply ../data/wikidata-matches-reviewed.tsv
    4. Enrich:  python wikidata-crawler.py enrich
    5. Stub:    python wikidata-crawler.py stub [--entity <id>]

Scoring weights:
    W_NAME = 0.4  (token overlap between entity name and candidate label)
    W_DESC = 0.3  (keyword overlap between entity and candidate descriptions)
    W_TAG  = 0.3  (tag tokens found in candidate description)

TSV columns:
    entity_id, entity_name, domain, candidate_qid, candidate_label,
    candidate_description, confidence_score, match_reason, status

Status values:
    existing  — entity already has a wikidataId
    pending   — awaiting human review
    approved  — human-confirmed match (apply mode will write it)
    rejected  — human-rejected match
    no_match  — Wikidata search returned zero results
"""

import argparse
import csv
import datetime
import json
import os
import re
import sys

from lib.tt_data import load_all_entities, load_entity, save_entity
from lib.wikidata_client import WikidataClient


# --- Path constants ---

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.dirname(_SCRIPTS_DIR)
_DATA_DIR = os.path.join(_PROJECT_DIR, "data")

ENRICHMENT_PATH = os.path.join(_DATA_DIR, "wikidata-enrichment.json")

LANGUAGES = ["en", "es", "fr", "de", "zh"]

# TSV output columns
TSV_COLUMNS = [
    "entity_id",
    "entity_name",
    "domain",
    "candidate_qid",
    "candidate_label",
    "candidate_description",
    "confidence_score",
    "match_reason",
    "status",
]

# Scoring weights
W_NAME = 0.4
W_DESC = 0.3
W_TAG = 0.3


# ---------------------------------------------------------------------------
# Tokenization
# ---------------------------------------------------------------------------

def tokenize(text):
    """Lowercase and split text into word tokens."""
    if not text:
        return []
    return re.findall(r"[a-z0-9]+(?:[-][a-z0-9]+)*", text.lower())


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_name_similarity(entity_name, candidate_label):
    """Token overlap ratio between entity name and candidate label."""
    name_tokens = set(tokenize(entity_name))
    label_tokens = set(tokenize(candidate_label))
    if not name_tokens:
        return 0.0
    return len(name_tokens & label_tokens) / len(name_tokens)


def score_description_overlap(entity_description, candidate_description):
    """Keyword overlap ratio between entity and candidate descriptions."""
    desc_tokens = set(tokenize(entity_description))
    cand_tokens = set(tokenize(candidate_description))
    if not desc_tokens:
        return 0.0
    return len(desc_tokens & cand_tokens) / len(desc_tokens)


def score_tag_match(tags, candidate_description):
    """Ratio of material/capability tags appearing in candidate description."""
    if not tags:
        return 0.0
    tag_tokens = set()
    for tag_list in (tags.get("material", []), tags.get("capability", [])):
        for tag in tag_list:
            tag_tokens.update(tokenize(tag))
    if not tag_tokens:
        return 0.0
    cand_tokens = set(tokenize(candidate_description))
    return len(tag_tokens & cand_tokens) / len(tag_tokens)


def compute_score(entity_name, entity_description, tags, candidate):
    """Compute weighted confidence score for a candidate match.

    Weights: name 0.4, description 0.3, tags 0.3.
    Returns (score, reason_string).
    """
    name_sim = score_name_similarity(entity_name, candidate.get("label", ""))
    desc_sim = score_description_overlap(entity_description, candidate.get("description", ""))
    tag_sim = score_tag_match(tags, candidate.get("description", ""))

    score = W_NAME * name_sim + W_DESC * desc_sim + W_TAG * tag_sim

    parts = []
    if name_sim > 0:
        parts.append("name={:.2f}".format(name_sim))
    if desc_sim > 0:
        parts.append("desc={:.2f}".format(desc_sim))
    if tag_sim > 0:
        parts.append("tag={:.2f}".format(tag_sim))

    reason = " ".join(parts) if parts else "no_match_components"
    return round(score, 4), reason


# ---------------------------------------------------------------------------
# Search query building
# ---------------------------------------------------------------------------

def build_search_query(entity):
    """Build a Wikidata search query from entity name + tags."""
    name = entity.get("name", "")
    tags = entity.get("tags", {})

    parts = [tokenize(name)]
    for tag_key in ("material", "capability"):
        for tag in tags.get(tag_key, []):
            parts.append(tokenize(tag))

    # Deduplicate while preserving order
    seen = set()
    unique_tokens = []
    for token_list in parts:
        for token in token_list:
            if token not in seen:
                seen.add(token)
                unique_tokens.append(token)

    return " ".join(unique_tokens)


# ---------------------------------------------------------------------------
# Enrich mode
# ---------------------------------------------------------------------------

def run_enrich(client=None):
    """Build enrichment cache of aliases + descriptions for all entities with wikidataId."""
    if client is None:
        client = WikidataClient()

    entities = load_all_entities()
    candidates = [e for e in entities if "wikidataId" in e]

    print(f"Found {len(candidates)} entities with wikidataId", file=sys.stderr)

    cache_entities = {}
    errors = 0

    for entity in candidates:
        qid = entity["wikidataId"]
        eid = entity.get("id") or entity.get("@id") or qid

        try:
            data = client.get_entity_data(qid, languages=LANGUAGES)
        except Exception as exc:
            print(f"  ERROR {eid} ({qid}): {exc}", file=sys.stderr)
            errors += 1
            continue

        if not data:
            print(f"  SKIP {eid} ({qid}): no data returned", file=sys.stderr)
            errors += 1
            continue

        cache_entities[eid] = {
            "wikidataId": qid,
            "name": entity.get("name", ""),
            "labels": data.get("labels", {}),
            "descriptions": data.get("descriptions", {}),
            "aliases": data.get("aliases", {}),
        }

    cache = {
        "version": "1.0",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "languages": LANGUAGES,
        "entities": cache_entities,
    }

    # Atomic write
    tmp_path = ENRICHMENT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(cache, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    os.replace(tmp_path, ENRICHMENT_PATH)

    print(
        f"Enriched {len(cache_entities)} entities with data in {len(LANGUAGES)} languages",
        file=sys.stderr,
    )
    if errors:
        print(f"  ({errors} entities skipped due to errors)", file=sys.stderr)

    return len(cache_entities)


# ---------------------------------------------------------------------------
# Search mode
# ---------------------------------------------------------------------------

def run_search(args):
    """Search Wikidata for all entities and write scored TSV."""
    entities = load_all_entities()
    total = len(entities)
    client = WikidataClient()

    print("Loaded {} entities".format(total), file=sys.stderr)

    stats = {
        "existing": 0,
        "pending": 0,
        "no_match": 0,
    }

    rows = []

    for i, entity in enumerate(entities, 1):
        entity_id = entity.get("id", "")
        entity_name = entity.get("name", entity_id)
        domain = entity_id.split(".")[0] if "." in entity_id else entity_id
        description = entity.get("description", "")
        tags = entity.get("tags", {})
        wikidata_id = entity.get("wikidataId")

        # --- Entity already has a wikidataId ---
        if wikidata_id:
            rows.append({
                "entity_id": entity_id,
                "entity_name": entity_name,
                "domain": domain,
                "candidate_qid": wikidata_id,
                "candidate_label": entity_name,
                "candidate_description": "",
                "confidence_score": "1.0",
                "match_reason": "existing_wikidataId",
                "status": "existing",
            })
            stats["existing"] += 1
            print("[{}/{}] {} — existing ({})".format(
                i, total, entity_id, wikidata_id), file=sys.stderr)
            continue

        # --- Search Wikidata ---
        query = build_search_query(entity)
        print("[{}/{}] {} — searching: {}".format(
            i, total, entity_id, query[:80]), file=sys.stderr)

        try:
            candidates = client.search_entities(query, language="en", limit=3)
        except Exception as exc:
            print("  ERROR: {}".format(exc), file=sys.stderr)
            candidates = []

        if not candidates:
            rows.append({
                "entity_id": entity_id,
                "entity_name": entity_name,
                "domain": domain,
                "candidate_qid": "",
                "candidate_label": "",
                "candidate_description": "",
                "confidence_score": "0.0",
                "match_reason": "zero_results",
                "status": "no_match",
            })
            stats["no_match"] += 1
            continue

        # --- Score each candidate ---
        scored = []
        for cand in candidates:
            score, reason = compute_score(entity_name, description, tags, cand)
            scored.append((score, reason, cand))

        scored.sort(key=lambda x: x[0], reverse=True)

        for score, reason, cand in scored:
            rows.append({
                "entity_id": entity_id,
                "entity_name": entity_name,
                "domain": domain,
                "candidate_qid": cand.get("qid", ""),
                "candidate_label": cand.get("label", ""),
                "candidate_description": cand.get("description", ""),
                "confidence_score": "{:.4f}".format(score),
                "match_reason": reason,
                "status": "pending",
            })
        stats["pending"] += 1

    # --- Write TSV (atomic) ---
    tmp_path = args.output + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=TSV_COLUMNS, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    os.replace(tmp_path, args.output)

    # --- Summary ---
    unique_entities = len(set(r["entity_id"] for r in rows))
    pending_entities = sum(1 for r in rows if r["status"] == "pending")
    print("", file=sys.stderr)
    print("=== Summary ===", file=sys.stderr)
    print("  Total entities:    {}".format(total), file=sys.stderr)
    print("  Unique in TSV:     {}".format(unique_entities), file=sys.stderr)
    print("  Existing (has ID): {}".format(stats["existing"]), file=sys.stderr)
    print("  With candidates:   {}".format(stats["pending"]), file=sys.stderr)
    print("  Candidate rows:    {}".format(pending_entities), file=sys.stderr)
    print("  No match:          {}".format(stats["no_match"]), file=sys.stderr)
    print("  Output:            {}".format(args.output), file=sys.stderr)

    if unique_entities < total:
        print("WARNING: TSV has {} unique entities, expected {}".format(
            unique_entities, total), file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Apply mode
# ---------------------------------------------------------------------------

def run_apply(args):
    """Read approved TSV and write wikidataId to entity files."""
    tsv_path = args.tsv_path
    dry_run = args.dry_run

    if not os.path.isfile(tsv_path):
        print("ERROR: TSV file not found: {}".format(tsv_path), file=sys.stderr)
        sys.exit(1)

    applied = 0
    skipped_has_id = 0
    skipped_status = 0
    errors = 0

    with open(tsv_path, "r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t", fieldnames=TSV_COLUMNS)

        header = next(reader, None)
        if header and header.get("entity_id") == "entity_id":
            pass
        elif header:
            fh.seek(0)
            reader = csv.DictReader(fh, delimiter="\t", fieldnames=TSV_COLUMNS)

        for row in reader:
            entity_id = row.get("entity_id", "")
            status = row.get("status", "")
            candidate_qid = row.get("candidate_qid", "")

            # Only process approved rows
            if status != "approved":
                skipped_status += 1
                continue

            # Validate Q-ID format
            if not re.match(r"^Q[0-9]+$", candidate_qid):
                print("  ERROR: invalid Q-ID '{}' for {}".format(
                    candidate_qid, entity_id), file=sys.stderr)
                errors += 1
                continue

            # Load entity
            entity = load_entity(entity_id)
            if entity is None:
                print("  ERROR: entity not found: {}".format(entity_id), file=sys.stderr)
                errors += 1
                continue

            # Guard against overwrite
            if "wikidataId" in entity:
                print("  SKIP {} — already has wikidataId ({})".format(
                    entity_id, entity["wikidataId"]), file=sys.stderr)
                skipped_has_id += 1
                continue

            if dry_run:
                print("  [DRY-RUN] Would set {} wikidataId = {}".format(
                    entity_id, candidate_qid), file=sys.stderr)
            else:
                entity["wikidataId"] = candidate_qid
                save_entity(entity)
                print("  APPLIED {} wikidataId = {}".format(
                    entity_id, candidate_qid), file=sys.stderr)

            applied += 1

    # --- Summary ---
    print("", file=sys.stderr)
    print("=== Apply Summary ===", file=sys.stderr)
    print("  Applied:          {}".format(applied), file=sys.stderr)
    print("  Skipped (status): {}".format(skipped_status), file=sys.stderr)
    print("  Skipped (has ID): {}".format(skipped_has_id), file=sys.stderr)
    print("  Errors:           {}".format(errors), file=sys.stderr)
    if dry_run:
        print("  (dry-run mode — no files modified)", file=sys.stderr)


# ---------------------------------------------------------------------------
# Stub mode
# ---------------------------------------------------------------------------

def run_stub(args):
    """Pre-fill descriptions from enrichment cache for entities without descriptions."""
    dry_run = args.dry_run
    entity_filter = args.entity

    # Load enrichment cache
    if not os.path.isfile(ENRICHMENT_PATH):
        print("ERROR: enrichment cache not found: {}".format(ENRICHMENT_PATH), file=sys.stderr)
        sys.exit(1)

    with open(ENRICHMENT_PATH, "r", encoding="utf-8") as fh:
        cache = json.load(fh)

    cache_entities = cache.get("entities", {})

    # Determine which entities to process
    if entity_filter:
        target_ids = [entity_filter]
    else:
        # All entity IDs in cache that have a wikidataId
        target_ids = [
            eid for eid, data in cache_entities.items()
            if "wikidataId" in data
        ]

    filled = 0
    skipped_has_desc = 0
    not_found = 0

    for eid in target_ids:
        cache_entry = cache_entities.get(eid)
        if cache_entry is None:
            print("  SKIP {} — not in enrichment cache".format(eid), file=sys.stderr)
            not_found += 1
            continue

        # Get English description from cache
        en_desc = cache_entry.get("descriptions", {}).get("en", "")
        if not en_desc:
            print("  SKIP {} — no English description in cache".format(eid), file=sys.stderr)
            not_found += 1
            continue

        # Load entity
        entity = load_entity(eid)
        if entity is None:
            print("  SKIP {} — entity file not found".format(eid), file=sys.stderr)
            not_found += 1
            continue

        # Skip entities that already have a description
        if "description" in entity and entity["description"]:
            print("  SKIP {} — already has description".format(eid), file=sys.stderr)
            skipped_has_desc += 1
            continue

        if dry_run:
            print("  [DRY-RUN] Would set {} description = {}".format(
                eid, en_desc[:80]), file=sys.stderr)
        else:
            entity["description"] = en_desc
            save_entity(entity)
            print("  FILLED {} description = {}".format(
                eid, en_desc[:80]), file=sys.stderr)

        filled += 1

    # --- Summary ---
    print("", file=sys.stderr)
    print("=== Stub Summary ===", file=sys.stderr)
    print("  Filled:                 {}".format(filled), file=sys.stderr)
    print("  Skipped (has desc):     {}".format(skipped_has_desc), file=sys.stderr)
    print("  Not found / no en desc: {}".format(not_found), file=sys.stderr)
    if dry_run:
        print("  (dry-run mode — no files modified)", file=sys.stderr)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Wikidata crawler for TechTree"
    )
    subparsers = parser.add_subparsers(dest="mode")

    # enrich subcommand
    subparsers.add_parser("enrich", help="Build multilingual enrichment cache")

    # search subcommand
    search_parser = subparsers.add_parser(
        "search", help="Search Wikidata for entity Q-IDs and output scored TSV",
    )
    search_parser.add_argument(
        "--output", required=True,
        help="Output TSV file path",
    )

    # apply subcommand
    apply_parser = subparsers.add_parser(
        "apply", help="Apply approved Q-IDs from reviewed TSV to entity files",
    )
    apply_parser.add_argument(
        "tsv_path",
        help="Path to reviewed TSV file",
    )
    apply_parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would be done without modifying files",
    )

    # stub subcommand
    stub_parser = subparsers.add_parser(
        "stub", help="Pre-fill descriptions from enrichment cache",
    )
    stub_parser.add_argument(
        "--entity",
        help="Process a single entity by ID (default: all entities in cache)",
    )
    stub_parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would be done without modifying files",
    )

    args = parser.parse_args()

    if args.mode == "enrich":
        run_enrich()
    elif args.mode == "search":
        run_search(args)
    elif args.mode == "apply":
        run_apply(args)
    elif args.mode == "stub":
        run_stub(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
