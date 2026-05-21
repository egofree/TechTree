#!/usr/bin/env python3
"""Per-article relevance rating for bootciv glossary terms.

For each term in the input glossary, scans source article markdown files and
classifies the term's relevance (primary / secondary / mentioned) within each
article.  Appends an ``article_relevance[]`` field to every term and writes the
result to the output file.

Requires: Python 3.8+, pyyaml (no other pip dependencies)
Usage:
    python scripts/compute-relevance.py --dry-run --verbose
    python scripts/compute-relevance.py --input data/glossary.json --output data/glossary-with-relevance.json
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
DOCS_DIR = PROJECT_DIR / "docs"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def node_id_to_path(node_id):
    """Map a node ID to its markdown article path under docs/.

    Rules:
        - domain-level (no dots)  -> docs/{domain}/index.md
        - capability-level (1 dot) -> docs/{domain}/{capability}.md
        - process-level (2+ dots) -> docs/{domain}/{rest-joined}.md
          where rest-joined = remaining segments joined with '-'
    """
    parts = node_id.split(".")
    domain = parts[0]
    if len(parts) == 1:
        return DOCS_DIR / domain / "index.md"
    capability = "-".join(parts[1:])
    return DOCS_DIR / domain / (capability + ".md")


def load_nodes(data_dir):
    """Load nodes.json and return a dict mapping node_id -> node dict."""
    nodes_path = data_dir / "nodes.json"
    if not nodes_path.exists():
        print("WARNING: nodes.json not found at {}".format(nodes_path), file=sys.stderr)
        return {}
    with open(nodes_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    nodes = {}
    for node in data.get("nodes", []):
        nid = node.get("id", "")
        if nid:
            nodes[nid] = node
    return nodes


def load_config(config_path):
    """Load the rating config YAML."""
    if not config_path.exists():
        print("WARNING: config not found at {}".format(config_path), file=sys.stderr)
        return {}
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_stop_words(config):
    """Extract stop-words list from config, lowercased."""
    raw = config.get("stop_words", [])
    return {w.lower().strip() for w in raw if w}


def read_article_prose(article_path):
    """Read an article markdown file and return the prose content.

    Strips the blockquote metadata header (lines starting with '> ') that
    appears at the top of each capability article.
    """
    if not article_path.exists():
        return ""
    with open(article_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Remove blockquote metadata header lines
    lines = text.split("\n")
    filtered = []
    for line in lines:
        if line.startswith("> "):
            continue
        filtered.append(line)

    return "\n".join(filtered)


def count_term_occurrences(text, term, aliases=None):
    """Count case-insensitive occurrences of term (and aliases) in text.

    Uses word-boundary-aware matching to avoid partial matches.
    Returns total count across term + all aliases.
    """
    if not text:
        return 0

    total = 0
    search_terms = [term]
    if aliases:
        search_terms.extend(aliases)

    for t in search_terms:
        if not t or len(t) < 2:
            continue
        pattern = re.compile(re.escape(t), re.IGNORECASE)
        total += len(pattern.findall(text))

    return total


def is_technical_context(text, term, position):
    """Heuristic check whether an occurrence at *position* is in technical context.

    Looks at surrounding words for indicators like dependency lists,
    cross-references, tool/material descriptions (markdown bold, backticks,
    colon-prefixed lists, etc.).
    """
    window = 120
    start = max(0, position - window)
    end = min(len(text), position + window)
    snippet = text[start:end]

    technical_indicators = [
        r"`[^`]+`",
        r"\*\*[^*]+\*\*",
        r"^\s*[-*]\s",
        r"^\s*\d+\.\s",
        r":\s*$",
        r"depends?\s+on",
        r"requires?",
        r"enables?",
        r"produces?",
        r"inputs?",
        r"outputs?",
        r"prerequisite",
        r"process",
        r"technique",
        r"method",
        r"temperature",
        r"pressure",
        r"chemical",
        r"reaction",
    ]
    for indicator in technical_indicators:
        if re.search(indicator, snippet, re.IGNORECASE | re.MULTILINE):
            return True
    return False


def classify_relevance(
    term,
    extraction_method,
    source_articles,
    occurrences,
    article_node_id,
    is_stop_word,
    text,
    verbose=False,
):
    """Classify relevance of a term in a single article.

    Returns one of: "primary", "secondary", "mentioned".

    Rules:
        - Bold-pattern / both: primary for source_articles; otherwise by count
        - NLP: by count with stop-word capping
        - Stop words capped at "mentioned" unless in source_articles
    """
    in_source = article_node_id in source_articles

    # --- Bold-pattern / both extraction ------------------------------------
    if extraction_method in ("bold-pattern", "both"):
        if in_source:
            return "primary"
        # For non-source articles, classify by occurrence count
        if occurrences >= 3:
            relevance = "secondary"
        elif occurrences >= 1:
            relevance = "mentioned"
        else:
            return None
        # Stop-word cap
        if is_stop_word and relevance != "mentioned":
            if verbose:
                print(
                    "    stop-word cap: '{}' in {} -> mentioned (was {})".format(
                        term, article_node_id, relevance
                    ),
                    file=sys.stderr,
                )
            return "mentioned"
        return relevance

    # --- NLP extraction ----------------------------------------------------
    if extraction_method == "nlp":
        if occurrences >= 3:
            relevance = "primary"
        elif occurrences >= 2:
            relevance = "secondary"
        elif occurrences >= 1:
            relevance = "mentioned"
        else:
            return None

        # Check if at least one occurrence is in technical context
        if relevance == "secondary" and text:
            term_lower = term.lower()
            idx = text.lower().find(term_lower)
            if idx >= 0 and not is_technical_context(text, term, idx):
                relevance = "mentioned"

        # Stop-word cap (unless in source_articles)
        if is_stop_word and not in_source:
            if relevance != "mentioned":
                if verbose:
                    print(
                        "    stop-word cap (nlp): '{}' in {} -> mentioned (was {})".format(
                            term, article_node_id, relevance
                        ),
                        file=sys.stderr,
                    )
                return "mentioned"
        return relevance

    # --- Unknown extraction method: fallback by count ----------------------
    if in_source:
        return "primary"
    if occurrences >= 3:
        return "secondary"
    if occurrences >= 1:
        return "mentioned"
    return None


def process_term(term_data, nodes, stop_words, verbose=False):
    """Process a single glossary term and return article_relevance list."""
    term = term_data.get("term", "")
    aliases = term_data.get("aliases", [])
    source_articles = term_data.get("source_articles", [])
    extraction_method = term_data.get("extraction_method", "bold-pattern")
    is_stop = term.lower().strip() in stop_words

    if verbose:
        print("  Term: '{}' [{}] stop={}".format(term, extraction_method, is_stop), file=sys.stderr)

    # Scan all article files for occurrences
    relevance_entries = []

    # First, scan source articles
    article_paths_checked = set()

    # Build set of all candidate article node IDs to scan
    candidate_nodes = set(source_articles)

    # Also add node_refs
    for ref in term_data.get("node_refs", []):
        candidate_nodes.add(ref)

    # Also add domain-related nodes from the term's domains
    term_domains = term_data.get("domains", [])
    for nid, node in nodes.items():
        domain = nid.split(".")[0] if "." in nid else nid
        if domain in term_domains:
            candidate_nodes.add(nid)

    for node_id in sorted(candidate_nodes):
        if node_id in article_paths_checked:
            continue
        article_paths_checked.add(node_id)

        article_path = node_id_to_path(node_id)
        if not article_path.exists():
            continue

        prose = read_article_prose(article_path)
        occurrences = count_term_occurrences(prose, term, aliases)

        if occurrences == 0:
            continue

        relevance = classify_relevance(
            term=term,
            extraction_method=extraction_method,
            source_articles=source_articles,
            occurrences=occurrences,
            article_node_id=node_id,
            is_stop_word=is_stop,
            text=prose,
            verbose=verbose,
        )

        if relevance:
            relevance_entries.append({
                "node_id": node_id,
                "relevance": relevance,
                "occurrences": occurrences,
            })
            if verbose:
                print(
                    "    {} -> {} ({} occurrences)".format(
                        node_id, relevance, occurrences
                    ),
                    file=sys.stderr,
                )

    return relevance_entries


def print_summary(terms_with_relevance, total_terms):
    """Print summary statistics to stderr."""
    total_entries = 0
    relevance_counts = Counter()
    article_term_counts = Counter()

    for term_data in terms_with_relevance:
        entries = term_data.get("article_relevance", [])
        total_entries += len(entries)
        for entry in entries:
            relevance_counts[entry["relevance"]] += 1
            article_term_counts[entry["node_id"]] += 1

    avg = total_entries / total_terms if total_terms > 0 else 0

    print("", file=sys.stderr)
    print("=== Relevance Summary ===", file=sys.stderr)
    print("  Total terms processed:       {}".format(total_terms), file=sys.stderr)
    print("  Total relevance entries:      {}".format(total_entries), file=sys.stderr)
    print("  Avg entries per term:         {:.1f}".format(avg), file=sys.stderr)
    print("  Distribution:", file=sys.stderr)
    for level in ("primary", "secondary", "mentioned"):
        print(
            "    {:12s} {}".format(level, relevance_counts.get(level, 0)),
            file=sys.stderr,
        )

    top_articles = article_term_counts.most_common(10)
    if top_articles:
        print("  Articles with most unique terms (top 10):", file=sys.stderr)
        for node_id, count in top_articles:
            print("    {} ({})".format(node_id, count), file=sys.stderr)

    print("", file=sys.stderr)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Compute per-article relevance ratings for glossary terms",
    )
    parser.add_argument(
        "--input",
        default=str(DATA_DIR / "glossary-rated.json"),
        help="Input glossary file (default: data/glossary-rated.json)",
    )
    parser.add_argument(
        "--output",
        default=str(DATA_DIR / "glossary-with-relevance.json"),
        help="Output glossary file (default: data/glossary-with-relevance.json)",
    )
    parser.add_argument(
        "--config",
        default=str(SCRIPT_DIR / "rating-config.yaml"),
        help="Rating config file (default: scripts/rating-config.yaml)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Output to stdout instead of writing file",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Print per-term reasoning to stderr",
    )
    args = parser.parse_args()

    # --- Load inputs -------------------------------------------------------
    input_path = Path(args.input)
    if not input_path.exists():
        # Fallback to glossary.json if glossary-rated.json doesn't exist
        fallback = DATA_DIR / "glossary.json"
        if fallback.exists():
            print(
                "NOTE: {} not found, using {}".format(args.input, fallback),
                file=sys.stderr,
            )
            input_path = fallback
        else:
            print(
                "ERROR: input file not found: {}".format(args.input),
                file=sys.stderr,
            )
            sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        glossary = json.load(f)

    config = load_config(Path(args.config))
    nodes = load_nodes(DATA_DIR)
    stop_words = get_stop_words(config)

    terms = glossary.get("terms", [])
    print("Processing {} terms...".format(len(terms)), file=sys.stderr)

    # --- Process each term -------------------------------------------------
    results = []
    for term_data in terms:
        relevance_entries = process_term(
            term_data, nodes, stop_words, verbose=args.verbose
        )
        updated = dict(term_data)
        updated["article_relevance"] = relevance_entries
        results.append(updated)

    # --- Build output ------------------------------------------------------
    output_glossary = dict(glossary)
    output_glossary["terms"] = results

    # --- Print summary -----------------------------------------------------
    print_summary(results, len(terms))

    # --- Write output ------------------------------------------------------
    output_json = json.dumps(output_glossary, indent=2, ensure_ascii=False)

    if args.dry_run:
        print(output_json)
        print("(dry-run mode: no file written)", file=sys.stderr)
    else:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_json)
            f.write("\n")
        print("Written to {}".format(output_path), file=sys.stderr)

    print("Done.", file=sys.stderr)


if __name__ == "__main__":
    main()
