#!/usr/bin/env python3
"""Deduplicate glossary terms from a combined extraction JSON file.

Applies four strategies to find duplicate/variant terms:
  1. Case-insensitive matching (keep most-capitalized variant)
  2. Plural/singular normalization (keep singular)
  3. Hyphen/space normalization (keep hyphenated variant)
  4. Alias detection: >=80% char overlap + same domain → flag for review

Usage:
    python scripts/deduplicate-terms.py --input data/glossary-combined.json --output data/glossary-deduped.json
    cat data/glossary-combined.json | python scripts/deduplicate-terms.py --dry-run
    echo '{"terms":[...]}' | python scripts/deduplicate-terms.py --dry-run --verbose
"""

import argparse
import json
import sys
from difflib import SequenceMatcher
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"

# ---------------------------------------------------------------------------
# Normalization helpers
# ---------------------------------------------------------------------------


def normalize_case_insensitive(term):
    """Return lowercase version for grouping."""
    return term.lower().strip()


def normalize_plural(term):
    """Return singular-ish form using simple rules.

    Rules (applied in order):
      - trailing 'ies' → 'y'  (e.g. 'Crucibles' -> nah, but 'calories' -> 'calory')
      - trailing 'ses', 'xes', 'zes', 'ches', 'shes' → strip 'es'
      - trailing 's' (but not 'ss') → strip 's'
    """
    t = term.strip()
    if t.endswith("ies") and len(t) > 3:
        return t[:-3] + "y"
    if t.endswith(("ses", "xes", "zes", "ches", "shes")) and len(t) > 2:
        return t[:-2]
    if t.endswith("s") and not t.endswith("ss") and len(t) > 1:
        return t[:-1]
    return t


def normalize_hyphen_space(term):
    """Replace hyphens with spaces (and vice-versa) for comparison.

    Returns a canonical form with spaces only, for grouping.
    """
    return term.replace("-", " ").replace("  ", " ").strip().lower()


def is_more_capitalized(candidate, reference):
    """Return True if candidate has more uppercase letters than reference."""
    c_upper = sum(1 for c in candidate if c.isupper())
    r_upper = sum(1 for c in reference if c.isupper())
    return c_upper > r_upper


def char_overlap_ratio(a, b):
    """Return similarity ratio between two strings (0.0–1.0)."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


# ---------------------------------------------------------------------------
# Merge logic
# ---------------------------------------------------------------------------


def merge_terms(primary, secondary, verbose=False):
    """Merge secondary into primary, returning the merged entry.

    Rules:
      - Combine source_articles[] (union)
      - Combine domains[] (union)
      - Keep the longer definition
      - Add the shorter variant to aliases[]
      - Combine node_refs[] (union)
      - extraction_method: "both" if both have one, else keep whichever has one
    """
    merged = dict(primary)

    sa = set(merged.get("source_articles", []))
    sa.update(secondary.get("source_articles", []))
    merged["source_articles"] = sorted(sa)

    dom = set(merged.get("domains", []))
    dom.update(secondary.get("domains", []))
    merged["domains"] = sorted(dom)

    p_def = merged.get("definition", "") or ""
    s_def = secondary.get("definition", "") or ""
    if len(s_def) > len(p_def):
        merged["definition"] = s_def

    aliases = set(merged.get("aliases", []))
    aliases.add(secondary["term"])
    for a in secondary.get("aliases", []):
        aliases.add(a)
    merged["aliases"] = sorted(aliases)

    nr = set(merged.get("node_refs", []))
    nr.update(secondary.get("node_refs", []))
    merged["node_refs"] = sorted(nr)

    p_em = merged.get("extraction_method")
    s_em = secondary.get("extraction_method")
    if p_em and s_em:
        merged["extraction_method"] = "both"
    elif s_em:
        merged["extraction_method"] = s_em

    if verbose:
        print("  MERGE: '{}' <-- '{}'".format(primary["term"], secondary["term"]))

    return merged


# ---------------------------------------------------------------------------
# Canonical variant selection
# ---------------------------------------------------------------------------


def pick_canonical(terms_in_group, strategy):
    """Pick the canonical term from a group of duplicates.

    Strategies:
      - case: keep the most-capitalized variant
      - plural: keep the singular form (prefer shorter, non-plural)
      - hyphen: keep the hyphenated variant
    """
    if len(terms_in_group) == 1:
        return terms_in_group[0], []

    if strategy == "case":
        ranked = sorted(terms_in_group, key=lambda t: -sum(1 for c in t if c.isupper()))
    elif strategy == "plural":
        def singular_score(t):
            n = normalize_plural(t.lower())
            return 0 if t.lower().strip() == n else 1
        ranked = sorted(terms_in_group, key=singular_score)
    elif strategy == "hyphen":
        def hyphen_score(t):
            return 0 if "-" in t else 1
        ranked = sorted(terms_in_group, key=hyphen_score)
    else:
        ranked = terms_in_group

    return ranked[0], ranked[1:]


# ---------------------------------------------------------------------------
# Main deduplication engine
# ---------------------------------------------------------------------------


def deduplicate(terms, verbose=False):
    """Run deduplication pipeline on a list of term entries.

    Returns (merged_list, flagged_list, stats_dict).
    """
    raw_count = len(terms)
    if raw_count == 0:
        return [], [], {
            "raw_count": 0,
            "unique_count": 0,
            "merged_count": 0,
            "flagged_count": 0,
        }

    # Phase 1: Case-insensitive merge
    if verbose:
        print("--- Phase 1: Case-insensitive matching ---")

    case_groups = {}
    term_to_entry = {}

    for entry in terms:
        t = entry["term"]
        key = normalize_case_insensitive(t)
        case_groups.setdefault(key, []).append(t)
        term_to_entry[t] = entry

    merged_entries = []
    merged_term_set = set()

    for key, group_terms in case_groups.items():
        canonical_str, variant_strs = pick_canonical(group_terms, "case")
        canonical_entry = dict(term_to_entry[canonical_str])

        for vs in variant_strs:
            secondary = term_to_entry[vs]
            canonical_entry = merge_terms(canonical_entry, secondary, verbose=verbose)
            merged_term_set.add(vs)

        canonical_entry["term"] = canonical_str
        merged_entries.append(canonical_entry)

    case_merged_count = len(merged_term_set)
    if verbose:
        print("  Case merges: {} terms merged into {} unique".format(
            case_merged_count, len(merged_entries)
        ))

    # --- Phase 2: Plural/singular merge ---
    if verbose:
        print("--- Phase 2: Plural/singular normalization ---")

    plural_groups = {}
    for entry in merged_entries:
        t = entry["term"]
        key = normalize_plural(normalize_case_insensitive(t))
        plural_groups.setdefault(key, []).append(entry)

    phase2_entries = []
    phase2_merged = 0

    for key, group in plural_groups.items():
        if len(group) == 1:
            phase2_entries.append(group[0])
            continue

        group_terms = [e["term"] for e in group]
        canonical_str, variant_strs = pick_canonical(group_terms, "plural")

        canonical_entry = None
        for e in group:
            if e["term"] == canonical_str:
                canonical_entry = dict(e)
                break
        if canonical_entry is None:
            canonical_entry = dict(group[0])

        for vs in variant_strs:
            secondary = None
            for e in group:
                if e["term"] == vs:
                    secondary = e
                    break
            if secondary:
                canonical_entry = merge_terms(canonical_entry, secondary, verbose=verbose)
                phase2_merged += 1

        canonical_entry["term"] = canonical_str
        phase2_entries.append(canonical_entry)

    if verbose:
        print("  Plural merges: {} terms merged, {} unique remaining".format(
            phase2_merged, len(phase2_entries)
        ))

    # --- Phase 3: Hyphen/space merge ---
    if verbose:
        print("--- Phase 3: Hyphen/space normalization ---")

    hyphen_groups = {}
    for entry in phase2_entries:
        t = entry["term"]
        key = normalize_hyphen_space(t)
        hyphen_groups.setdefault(key, []).append(entry)

    phase3_entries = []
    phase3_merged = 0

    for key, group in hyphen_groups.items():
        if len(group) == 1:
            phase3_entries.append(group[0])
            continue

        group_terms = [e["term"] for e in group]
        canonical_str, variant_strs = pick_canonical(group_terms, "hyphen")

        canonical_entry = None
        for e in group:
            if e["term"] == canonical_str:
                canonical_entry = dict(e)
                break
        if canonical_entry is None:
            canonical_entry = dict(group[0])

        for vs in variant_strs:
            secondary = None
            for e in group:
                if e["term"] == vs:
                    secondary = e
                    break
            if secondary:
                canonical_entry = merge_terms(canonical_entry, secondary, verbose=verbose)
                phase3_merged += 1

        canonical_entry["term"] = canonical_str
        phase3_entries.append(canonical_entry)

    if verbose:
        print("  Hyphen merges: {} terms merged, {} unique remaining".format(
            phase3_merged, len(phase3_entries)
        ))

    # --- Phase 4: Alias detection (>=80% overlap, same domain) → flag ---
    if verbose:
        print("--- Phase 4: Alias detection (>=80% char overlap, same domain) ---")

    flagged = []
    flagged_indices = set()

    entries_list = phase3_entries
    n = len(entries_list)

    for i in range(n):
        if i in flagged_indices:
            continue
        for j in range(i + 1, n):
            if j in flagged_indices:
                continue
            a = entries_list[i]
            b = entries_list[j]
            ratio = char_overlap_ratio(a["term"], b["term"])
            if ratio >= 0.80:
                a_domains = set(a.get("domains", []))
                b_domains = set(b.get("domains", []))
                if a_domains & b_domains:
                    flagged.append({
                        "term_a": a["term"],
                        "term_b": b["term"],
                        "overlap_ratio": round(ratio, 3),
                        "shared_domains": sorted(a_domains & b_domains),
                        "reason": "potential alias",
                    })
                    if verbose:
                        print("  FLAG: '{}' <-> '{}' (overlap={:.1%}, domains={})".format(
                            a["term"], b["term"], ratio, sorted(a_domains & b_domains)
                        ))

    total_merged = case_merged_count + phase2_merged + phase3_merged
    unique_count = len(phase3_entries)

    stats = {
        "raw_count": raw_count,
        "unique_count": unique_count,
        "merged_count": total_merged,
        "flagged_count": len(flagged),
    }

    if verbose:
        print()
        print("--- Summary ---")
        print("  Raw terms:     {}".format(stats["raw_count"]))
        print("  Unique terms:  {}".format(stats["unique_count"]))
        print("  Total merged:  {}".format(stats["merged_count"]))
        print("  Flagged:       {}".format(stats["flagged_count"]))

    return phase3_entries, flagged, stats


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Deduplicate glossary terms from a combined extraction JSON file",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Output results to stdout (no file written)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Log all merges with before/after details",
    )
    parser.add_argument(
        "--input",
        default=None,
        help="Input file path (default: stdin, or data/glossary-combined.json)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output file path (default: stdout)",
    )
    args = parser.parse_args()

    # Read input
    input_path = args.input
    if input_path is None:
        if not sys.stdin.isatty():
            raw = sys.stdin.read()
        else:
            default_path = DATA_DIR / "glossary-combined.json"
            if not default_path.exists():
                print(
                    "ERROR: no input provided and {} not found".format(default_path),
                    file=sys.stderr,
                )
                sys.exit(1)
            input_path = str(default_path)

    if input_path:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.loads(raw)

    if "terms" not in data:
        print("ERROR: input JSON must contain a 'terms' array", file=sys.stderr)
        sys.exit(1)

    terms = data["terms"]
    if not isinstance(terms, list):
        print("ERROR: 'terms' must be an array", file=sys.stderr)
        sys.exit(1)

    merged, flagged, stats = deduplicate(terms, verbose=args.verbose)

    result = {
        "merged": merged,
        "flagged_for_review": flagged,
        "stats": stats,
    }

    output_json = json.dumps(result, indent=2, ensure_ascii=False)

    if args.dry_run or args.output is None:
        print(output_json)
    else:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_json)
            f.write("\n")
        if args.verbose:
            print("Written to: {}".format(output_path))

    if stats["flagged_count"] > 0:
        print(
            "\nNOTE: {} potential alias(es) flagged for manual review.".format(
                stats["flagged_count"]
            ),
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
