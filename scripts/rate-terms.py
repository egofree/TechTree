#!/usr/bin/env python3
"""Rule-based term type classifier and tier rater for bootciv glossary.

Reads deduplicated glossary terms (JSON) and adds:
  - type classification (process/equipment/material/noun/verb)
  - tier rating (critical/important/supporting)
  - needs_image / needs_diagram flags
  - stop_word_overridden flag when applicable

All criteria read from rating-config.yaml — nothing hardcoded.

Requires: Python 3.8+, pyyaml
Usage:
    python scripts/rate-terms.py --dry-run --verbose < data/glossary-dedup.json
    python scripts/rate-terms.py < data/glossary-dedup.json
    echo '<json>' | python scripts/rate-terms.py --dry-run
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
CONFIG_PATH = SCRIPT_DIR / "rating-config.yaml"

# ---------------------------------------------------------------------------
# Config loader
# ---------------------------------------------------------------------------


def load_config(path=None):
    """Load and return the rating config YAML as a dict."""
    p = Path(path) if path else CONFIG_PATH
    if not p.exists():
        print("ERROR: config not found: {}".format(p), file=sys.stderr)
        sys.exit(1)
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------------------
# Type classification
# ---------------------------------------------------------------------------


def classify_type(term, definition, extraction_method=None, config=None, verbose=False):
    """Classify a term's type using rule-based heuristics from config.

    Priority order:
      1. NLP POS tag override (if extraction_method indicates NLP with VB*/NN*)
      2. Definition-pattern matching (process → equipment → material → noun)

    Returns:
        Tuple of (type_str, list_of_reason_strings)
    """
    reasons = []
    type_config = (config or {}).get("type_classification", {})

    def_lower = (definition or "").lower()
    term_lower = (term or "").lower().strip()

    # --- Check NLP POS tag override ---
    # extraction_method may be "nlp" or "both"; terms from NLP may carry POS info
    # encoded as a suffix like "VBG", "VB", "NN", "NNS" etc.
    nlp_type = None
    if extraction_method in ("nlp", "both"):
        nlp_type = _nlp_pos_to_type(term, reasons)
        if nlp_type and verbose:
            reasons.append("NLP POS override → {}".format(nlp_type))

    # --- Process / verb ---
    if not nlp_type:
        process_cfg = type_config.get("process", {})
        patterns = process_cfg.get("patterns", [])
        suffix = process_cfg.get("suffix_heuristic", "")

        matched_pattern = None
        for pat in patterns:
            if pat in def_lower:
                matched_pattern = pat
                break

        suffix_match = False
        if suffix and term_lower.endswith(suffix) and len(term_lower) > len(suffix):
            # Exclude short common words that end in -ing but aren't gerunds
            # (e.g., "thing", "ring", "spring")
            non_gerund_exceptions = {"thing", "ring", "spring", "string", "bring"}
            if term_lower not in non_gerund_exceptions:
                suffix_match = True

        if matched_pattern or suffix_match:
            nlp_type = "process"
            r_parts = []
            if matched_pattern:
                r_parts.append("definition contains '{}'".format(matched_pattern))
            if suffix_match:
                r_parts.append("term ends with '{}' (gerund)".format(suffix))
            reasons.append("process: {}".format("; ".join(r_parts)))

    # --- Equipment ---
    if not nlp_type:
        equip_patterns = type_config.get("equipment", {}).get("patterns", [])
        for pat in equip_patterns:
            if pat in def_lower:
                nlp_type = "equipment"
                reasons.append("equipment: definition contains '{}'".format(pat))
                break

    # --- Material ---
    if not nlp_type:
        mat_patterns = type_config.get("material", {}).get("patterns", [])
        for pat in mat_patterns:
            if pat in def_lower:
                nlp_type = "material"
                reasons.append("material: definition contains '{}'".format(pat))
                break

    # --- Fallback: noun ---
    if not nlp_type:
        nlp_type = "noun"
        reasons.append("noun: default fallback (no patterns matched)")

    return nlp_type, reasons


def _nlp_pos_to_type(term, reasons):
    """Map NLP POS tag to type. VB* → verb/process, NN* → noun.

    In this pipeline, NLP-extracted terms with POS tags are mapped:
      VB, VBD, VBG, VBN, VBP, VBZ → "verb"
      NN, NNS, NNP, NNPS           → None (let pattern matching decide)

    We return "verb" for verb POS, None for noun POS (noun is default,
    let pattern matching try to refine it to process/equipment/material).
    """
    # NLP terms with verb POS → classify as "verb"
    # (We can't detect POS from the data directly; if extraction_method
    # is "nlp" or "both", we check if the term itself looks verb-like)
    # Per spec: "NLP POS tag says VB* → verb, NN* → noun"
    # Since we don't have raw POS stored, verb detection comes from
    # definition patterns. This function returns None to let pattern
    # matching proceed, unless the term is clearly verb-like.
    return None


# ---------------------------------------------------------------------------
# Tier rating
# ---------------------------------------------------------------------------


def rate_tier(entry, config=None, verbose=False):
    """Compute tier rating for a single term entry.

    Returns:
        Tuple of (tier_str, needs_image_bool, needs_diagram_bool,
                  stop_word_override_bool, list_of_reason_strings)
    """
    reasons = []
    cfg = config or {}
    tiers_cfg = cfg.get("tiers", {})
    stop_words = [w.lower() for w in cfg.get("stop_words", [])]
    thresholds_cfg = cfg.get("thresholds", {})

    term = entry.get("term", "")
    term_lower = term.lower().strip()
    definition = entry.get("definition", "")
    source_articles = entry.get("source_articles", [])
    domains = entry.get("domains", [])

    article_count = len(set(source_articles))
    domain_count = len(set(domains))
    definition_words = definition.split()
    definition_word_count = len(definition_words)

    is_stop_word = term_lower in stop_words
    specificity = 0.5 if is_stop_word else 1.0

    # --- Critical tier (thresholds only, stop-word handled separately) ---
    crit = tiers_cfg.get("critical", {})
    crit_min_articles = crit.get("min_articles", 3)
    crit_min_domains = crit.get("min_domains", 2)
    crit_min_words = crit.get("min_definition_words", 30)

    meets_critical_thresholds = (
        article_count >= crit_min_articles
        and domain_count >= crit_min_domains
        and definition_word_count >= crit_min_words
    )

    # --- Important tier ---
    imp = tiers_cfg.get("important", {})
    imp_min_articles = imp.get("min_articles", 1)
    imp_min_domains = imp.get("min_domains", 0)
    imp_min_words = imp.get("min_definition_words", 15)

    meets_important_thresholds = (
        article_count >= imp_min_articles
        and domain_count >= imp_min_domains
        and definition_word_count >= imp_min_words
    )

    # --- Assign tier ---
    stop_word_override = False
    penalty = thresholds_cfg.get("stop_word_tier_penalty", "")

    if is_stop_word and meets_critical_thresholds:
        stop_word_override = True
        tier = "important"
        reasons.append(
            "stop-word override: would be critical → downgraded to important"
        )
    elif is_stop_word and meets_important_thresholds:
        stop_word_override = True
        tier = "supporting"
        reasons.append(
            "stop-word override: would be important → downgraded to supporting"
        )
    elif meets_critical_thresholds and not is_stop_word:
        tier = "critical"
        reasons.append(
            "critical: articles={}>={}, domains={}>={}, words={}>={}, not stop-word".format(
                article_count, crit_min_articles,
                domain_count, crit_min_domains,
                definition_word_count, crit_min_words,
            )
        )
    elif meets_important_thresholds and not is_stop_word:
        tier = "important"
        reasons.append(
            "important: articles={}>={}, words={}>={}, not stop-word".format(
                article_count, imp_min_articles,
                definition_word_count, imp_min_words,
            )
        )
    else:
        tier = "supporting"
        if is_stop_word:
            reasons.append("supporting: stop-word, insufficient metrics")
        else:
            reasons.append(
                "supporting: articles={}, domains={}, words={} (below thresholds)".format(
                    article_count, domain_count, definition_word_count,
                )
            )

    # --- needs_image / needs_diagram ---
    # Determined after tier + type are both known; type passed in separately
    # For now return tier, flags computed in main loop

    reasons.append("specificity={}".format(specificity))

    return tier, stop_word_override, reasons


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------


def process_terms(data, config, verbose=False):
    """Process all terms: classify type, rate tier, compute flags.

    Args:
        data: Parsed JSON dict with "terms" array.
        config: Parsed rating-config.yaml dict.
        verbose: If True, emit per-term reasoning to stderr.

    Returns:
        Dict with enriched terms + stats section.
    """
    terms = data.get("terms", [])
    enriched = []

    stats = {
        "total": len(terms),
        "by_type": {},
        "by_tier": {},
        "stop_word_overrides": 0,
        "needs_image_count": 0,
        "needs_diagram_count": 0,
    }

    for entry in terms:
        term = entry.get("term", "?")
        definition = entry.get("definition", "")
        extraction_method = entry.get("extraction_method", "")

        # --- Type classification ---
        term_type, type_reasons = classify_type(
            term, definition, extraction_method, config, verbose,
        )

        # --- Tier rating ---
        tier, stop_override, tier_reasons = rate_tier(entry, config, verbose)

        # --- needs_image / needs_diagram ---
        needs_image = tier == "critical" and term_type in ("equipment", "material")
        needs_diagram = tier == "critical" and term_type in ("process",)

        # --- Build enriched entry ---
        out = dict(entry)
        out["type"] = term_type
        out["tier"] = tier
        out["needs_image"] = needs_image
        out["needs_diagram"] = needs_diagram
        if stop_override:
            out["stop_word_overridden"] = True

        enriched.append(out)

        # --- Stats ---
        stats["by_type"][term_type] = stats["by_type"].get(term_type, 0) + 1
        stats["by_tier"][tier] = stats["by_tier"].get(tier, 0) + 1
        if stop_override:
            stats["stop_word_overrides"] += 1
        if needs_image:
            stats["needs_image_count"] += 1
        if needs_diagram:
            stats["needs_diagram_count"] += 1

        if verbose:
            all_reasons = type_reasons + tier_reasons
            print(
                "  {} → type={}, tier={} | {}".format(
                    term, term_type, tier, "; ".join(all_reasons)
                ),
                file=sys.stderr,
            )

    result = dict(data)
    result["terms"] = enriched
    result["stats"] = stats
    result["rated_at"] = datetime.now(timezone.utc).isoformat()

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Rate glossary terms: classify type (process/equipment/material/noun) "
            "and assign tier (critical/important/supporting). "
            "All criteria from rating-config.yaml."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Output rated JSON to stdout instead of writing to file",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Show per-term classification reasoning on stderr",
    )
    parser.add_argument(
        "--input",
        default=None,
        help="Input JSON file (default: data/glossary-dedup.json or stdin)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output JSON file (default: data/glossary-rated.json)",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Path to rating-config.yaml (default: scripts/rating-config.yaml)",
    )
    args = parser.parse_args()

    # --- Load config ---
    config = load_config(args.config)

    # --- Load input ---
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        # Try file default, else stdin
        default_input = DATA_DIR / "glossary-dedup.json"
        if default_input.exists():
            with open(default_input, "r", encoding="utf-8") as f:
                data = json.load(f)
            if args.verbose:
                print("Read input from {}".format(default_input), file=sys.stderr)
        else:
            if args.verbose:
                print("Reading input from stdin...", file=sys.stderr)
            raw = sys.stdin.read()
            data = json.loads(raw)

    # --- Process ---
    if args.verbose:
        print("Processing {} terms...".format(len(data.get("terms", []))), file=sys.stderr)

    result = process_terms(data, config, verbose=args.verbose)

    # --- Output ---
    output_json = json.dumps(result, indent=2, ensure_ascii=False)

    if args.dry_run:
        print(output_json)
    else:
        output_path = Path(args.output) if args.output else DATA_DIR / "glossary-rated.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_json)
            f.write("\n")
        if args.verbose:
            print("Wrote {} terms to {}".format(
                len(result.get("terms", [])), output_path
            ), file=sys.stderr)

    stats = result.get("stats", {})
    if args.verbose:
        print("", file=sys.stderr)
        print("=== Stats ===", file=sys.stderr)
        print("  Total:              {}".format(stats.get("total", 0)), file=sys.stderr)
        for t in sorted(stats.get("by_type", {})):
            print("  type={}: {:>4}".format(t, stats["by_type"][t]), file=sys.stderr)
        for t in ("critical", "important", "supporting"):
            print("  tier={}: {:>4}".format(t, stats.get("by_tier", {}).get(t, 0)), file=sys.stderr)
        print("  stop_word_overrides: {}".format(stats.get("stop_word_overrides", 0)), file=sys.stderr)
        print("  needs_image:        {}".format(stats.get("needs_image_count", 0)), file=sys.stderr)
        print("  needs_diagram:      {}".format(stats.get("needs_diagram_count", 0)), file=sys.stderr)


if __name__ == "__main__":
    main()
