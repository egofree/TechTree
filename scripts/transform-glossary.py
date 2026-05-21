#!/usr/bin/env python3
"""Transform glossary-raw.json from per-occurrence to grouped format.

Reads data/glossary-raw.json (per-occurrence entries) and writes
data/glossary-combined.json (per-term grouped entries) compatible
with deduplicate-terms.py.

Usage:
    python3 scripts/transform-glossary.py
    python3 scripts/transform-glossary.py --input data/glossary-raw.json --output data/glossary-combined.json
"""

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"


def slugify(term: str) -> str:
    """Convert term to kebab-case slug.

    lowercase, spaces→hyphens, strip special chars (keep alphanumeric + hyphens).
    """
    s = term.lower().strip()
    # Replace spaces with hyphens
    s = s.replace(" ", "-")
    # Remove anything that's not alphanumeric or hyphen
    s = re.sub(r"[^a-z0-9-]", "", s)
    # Collapse multiple hyphens
    s = re.sub(r"-{2,}", "-", s)
    # Strip leading/trailing hyphens
    s = s.strip("-")
    return s


def capitalization_score(term: str) -> int:
    """Count uppercase letters in term."""
    return sum(1 for c in term if c.isupper())


def main():
    parser = argparse.ArgumentParser(description="Transform raw glossary to grouped format")
    parser.add_argument("--input", default=str(DATA_DIR / "glossary-raw.json"))
    parser.add_argument("--output", default=str(DATA_DIR / "glossary-combined.json"))
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        raw = json.load(f)

    raw_terms = raw["terms"]
    raw_count = len(raw_terms)

    groups: dict[str, list] = defaultdict(list)
    for entry in raw_terms:
        key = entry["term"].lower().strip()
        groups[key].append(entry)

    grouped = []
    for key, entries in groups.items():
        best_term = max(entries, key=lambda e: capitalization_score(e["term"]))["term"]
        best_def = max(entries, key=lambda e: len(e.get("definition", "") or ""))["definition"]
        source_articles = sorted(set(e["source_node_id"] for e in entries))
        domains = sorted(set(e["source_domain"] for e in entries))

        grouped.append({
            "term": best_term,
            "slug": slugify(best_term),
            "definition": best_def,
            "source_articles": source_articles,
            "domains": domains,
            "extraction_method": "bold-pattern",
            "aliases": [],
            "see_also": [],
            "node_refs": list(source_articles),
            "needs_image": False,
            "needs_diagram": False,
            "created": False,
        })

    grouped.sort(key=lambda e: e["term"].lower())

    result = {
        "$schema": "bootciv-glossary-v1",
        "terms": grouped,
        "stats": {
            "source": "bold-pattern",
            "raw_count": raw_count,
            "grouped_count": len(grouped),
            "domains": len(set(d for e in grouped for d in e["domains"])),
            "articles": len(set(a for e in grouped for a in e["source_articles"])),
            "empty_definitions": sum(1 for e in grouped if not e["definition"].strip()),
        },
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Raw entries:     {raw_count}")
    print(f"Grouped terms:   {len(grouped)}")
    print(f"Domains:         {result['stats']['domains']}")
    print(f"Articles:        {result['stats']['articles']}")
    print(f"Empty defs:      {result['stats']['empty_definitions']}")
    print(f"Output:          {output_path}")


if __name__ == "__main__":
    main()
