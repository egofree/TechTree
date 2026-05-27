#!/usr/bin/env python3
"""Wikidata crawler for TechTree — search and enrichment modes.

Searches Wikidata for entities matching bootciv capabilities/processes,
scores candidates, and outputs a TSV file for human review.  Also provides
an enrichment mode for building a multilingual alias/description cache.

Usage (run from scripts/ directory):
    python wikidata-crawler.py search --output /tmp/wikidata-results.tsv
    python wikidata-crawler.py enrich
"""

import argparse
import csv
import datetime
import json
import os
import re
import sys

from lib.tt_data import load_all_entities
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

    # --- Write TSV ---
    with open(args.output, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=TSV_COLUMNS, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

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

    # (apply, stub subcommands added in later tasks)

    args = parser.parse_args()

    if args.mode == "enrich":
        run_enrich()
    elif args.mode == "search":
        run_search(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
