#!/usr/bin/env python3
"""Extract significant nouns and verbs from article prose via spaCy NLP.

Supplements bold-pattern extraction by finding technical terms in prose that
were NOT captured by bold patterns. Uses POS tagging, noun-phrase chunking,
and named entity recognition.

Requires: Python 3.8+, spacy, en_core_web_sm model
Usage:
    python3 scripts/extract-nlp-terms.py --dry-run
    python3 scripts/extract-nlp-terms.py --domain foundations --verbose
    python3 scripts/extract-nlp-terms.py --bold-output data/glossary-raw.json
"""

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

try:
    import spacy
except ImportError:
    print(
        "ERROR: spaCy is not installed. Install with:\n"
        "  pip install spacy\n"
        "  python3 -m spacy download en_core_web_sm",
        file=sys.stderr,
    )
    sys.exit(1)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DOCS_DIR = PROJECT_DIR / "docs"
DATA_DIR = PROJECT_DIR / "data"
DEFAULT_OUTPUT = DATA_DIR / "glossary-nlp-raw.json"

NODE_ID_RE = re.compile(r">\s*\*\*Node ID\*\*:\s*(.+)")
SKIP_DIRS = {"images", "supporting"}

# ---------------------------------------------------------------------------
# Markdown stripping patterns
# ---------------------------------------------------------------------------

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
MD_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
MD_ITALIC_RE = re.compile(r"\*([^*]+)\*")
MD_CODE_RE = re.compile(r"`([^`]+)`")
MD_HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)
MD_BLOCKQUOTE_RE = re.compile(r"^>\s*", re.MULTILINE)
MD_TABLE_SEP_RE = re.compile(r"^\|[-:| ]+\|$", re.MULTILINE)
MD_LIST_PREFIX_RE = re.compile(r"^(\s*)([-*+]|\d+[\.\)])\s+", re.MULTILINE)
MD_HTML_TAG_RE = re.compile(r"<[^>]+>")
MD_HR_RE = re.compile(r"^---+$", re.MULTILINE)
UNICODE_SUBSCRIPT_RE = re.compile(r"[₀₁₂₃₄₅₆₇₈₉]")
FOOTER_RE = re.compile(r"^\[←.*$", re.MULTILINE)
PART_OF_RE = re.compile(r"^\*Part of the.*$", re.MULTILINE)
BACK_TO_RE = re.compile(r"^\*?\[Back to.*$", re.MULTILINE)

# ---------------------------------------------------------------------------
# Domain-specific stop words
# ---------------------------------------------------------------------------

DOMAIN_STOP_WORDS = frozenset({
    "area", "base", "body", "case", "center", "change", "chapter",
    "close", "common", "contact", "content", "control", "corner",
    "couple", "course", "current", "day", "detail", "difference",
    "different", "direction", "distance", "effect", "end", "example",
    "fact", "family", "figure", "first", "form", "general", "ground",
    "group", "half", "hand", "head", "high", "hour", "idea", "inch",
    "instance", "kind", "large", "last", "late", "later", "left",
    "level", "line", "long", "lot", "low", "major", "make", "manner",
    "means", "middle", "might", "minute", "moment", "name", "natural",
    "near", "need", "new", "next", "note", "number", "occasion",
    "once", "one", "order", "original", "others", "outside", "overall",
    "own", "part", "particular", "past", "pattern", "people", "period",
    "piece", "place", "plan", "point", "position", "possible", "process",
    "product", "purpose", "quantity", "question", "range", "rate",
    "reach", "reason", "record", "result", "right", "room", "round",
    "scale", "second", "section", "set", "short", "side", "similar",
    "single", "size", "small", "source", "special", "stage", "stand",
    "start", "state", "step", "structure", "surface", "system", "thing",
    "third", "time", "today", "top", "total", "turn", "type", "use",
    "used", "way", "week", "work", "world", "year",
    "allow", "appear", "become", "begin", "build", "carry", "come",
    "consider", "continue", "create", "develop", "does", "done",
    "ensure", "feel", "find", "get", "give", "go", "going", "got",
    "grow", "happen", "keep", "know", "leave", "let", "like", "look",
    "made", "makes", "may", "might", "move", "must", "need", "pay",
    "put", "run", "said", "say", "see", "seem", "set", "should",
    "show", "take", "tell", "think", "try", "turn", "want", "watch",
    "work", "would",
    "able", "also", "back", "best", "better", "certain", "clear",
    "early", "easy", "either", "enough", "even", "every", "far",
    "few", "full", "great", "hard", "important", "just", "least",
    "less", "local", "main", "many", "more", "much", "must", "often",
    "old", "own", "particular", "per", "quite", "rather", "real",
    "same", "several", "simple", "since", "still", "such", "sure",
    "true", "usually", "well", "whole", "yet",
    "material", "method", "technique", "approach", "procedure",
    "requirement", "component", "element", "factor", "condition",
    "property", "value", "standard", "application", "requirement",
    "function", "unit", "device", "equipment", "instrument",
    "operation", "action", "practice", "result",
    "performance", "quality", "amount", "supply", "demand",
    "production", "output", "input",
})

EXTRA_SINGLE_WORD_STOPS = frozenset({
    "weight", "width", "length", "height", "depth", "size", "speed",
    "rate", "ratio", "range", "level", "degree", "amount", "volume",
    "pressure", "temperature", "density", "capacity", "force", "power",
    "energy", "heat", "light", "water", "air", "gas", "oil", "iron",
    "steel", "copper", "carbon", "oxygen", "hydrogen", "nitrogen",
    "metal", "glass", "stone", "wood", "sand", "clay", "rock",
    "earth", "fire", "food", "soil", "salt", "acid", "milk", "blood",
    "dust", "smoke", "steam", "vapor", "wax", "fat", "bone", "hair",
    "skin", "root", "leaf", "seed", "fruit", "bark", "flower",
    "man", "woman", "child", "person", "people", "hand", "foot",
    "head", "eye", "arm", "leg", "back", "face", "mouth", "tooth",
    "finger", "neck", "chest", "knee", "heart",
    "end", "edge", "side", "wall", "floor", "door", "window",
    "roof", "ceiling", "step", "layer", "surface", "bottom", "middle",
    "center", "core", "inner", "outer", "upper", "lower",
    "tree", "grass", "plant", "branch", "trunk", "stem",
    "horse", "dog", "cat", "fish", "bird", "cow", "sheep", "goat",
    "pig", "chicken", "animal", "insect", "worm", "egg",
    "sun", "moon", "star", "rain", "snow", "wind", "ice", "storm",
    "summer", "winter", "spring", "autumn", "morning", "night",
    "day", "week", "month", "year", "age", "era",
    "road", "path", "river", "hill", "valley", "lake", "sea",
    "ocean", "island", "mountain", "forest", "field", "garden",
    "house", "room", "bed", "table", "chair", "box", "bag", "pot",
    "cup", "bowl", "knife", "axe", "hammer", "saw", "drill",
    "rope", "wire", "thread", "cord", "chain", "belt", "strap",
    "wheel", "gear", "shaft", "lever", "spring", "valve", "pipe",
    "tube", "hole", "slot", "groove", "notch", "gap",
    "blade", "tip", "point", "hook", "ring", "nut", "bolt",
    "nail", "screw", "pin", "peg", "wedge", "block", "plate",
    "sheet", "strip", "bar", "rod", "stick", "log", "board",
    "panel", "frame", "beam", "post", "pole", "stake",
    "vessel", "container", "tank", "barrel", "jug",
    "bottle", "jar", "basin", "trough", "mold",
    "tonne", "tonnes", "kilogram", "grams", "liter", "liters",
    "meter", "meters", "centimeter", "millimeter", "mm", "cm",
    "hours", "hour", "minutes", "minute", "seconds",
    "years", "months", "weeks", "days",
    "percent", "percentage", "proportion", "fraction",
    "zero", "two", "three", "four", "five", "six",
    "seven", "eight", "nine", "ten", "hundred", "thousand",
    "annual", "daily", "weekly", "monthly", "average",
    "maximum", "minimum", "approximately", "roughly", "about",
    "samples", "sample", "specimen", "specimens",
    "fiber", "fibers", "cloth", "cloth",
    "shellac", "tonne", "load",
})

LEADING_DETERMINERS = frozenset({
    "the", "a", "an", "this", "that", "these", "those",
    "some", "any", "each", "every", "no", "its", "his", "her",
    "their", "our", "my", "your",
})

PUNCT_STRIP = '.,;:!?"\'()`{}[]<>«»""''–—–…·•†‡§¶'


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def strip_markdown(text: str) -> str:
    """Strip markdown formatting to produce clean prose for NLP."""
    text = MD_IMAGE_RE.sub("", text)
    text = MD_LINK_RE.sub(r"\1", text)
    text = MD_BOLD_RE.sub(r"\1", text)
    text = MD_ITALIC_RE.sub(r"\1", text)
    text = MD_CODE_RE.sub(r"\1", text)
    text = MD_HEADING_RE.sub("", text)
    text = MD_BLOCKQUOTE_RE.sub("", text)
    text = MD_TABLE_SEP_RE.sub("", text)
    text = MD_LIST_PREFIX_RE.sub(r"\1", text)
    text = MD_HTML_TAG_RE.sub("", text)
    text = MD_HR_RE.sub("", text)
    text = FOOTER_RE.sub("", text)
    text = PART_OF_RE.sub("", text)
    text = BACK_TO_RE.sub("", text)
    text = re.sub(r"\|", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def enumerate_markdown_files(
    docs_dir: Path, domain_filter: str | None = None
) -> list[Path]:
    """Walk docs/ and return sorted list of .md files to process."""
    results = []
    for md_file in sorted(docs_dir.rglob("*.md")):
        rel = md_file.relative_to(docs_dir)
        parts = rel.parts
        if parts[0] in SKIP_DIRS:
            continue
        if md_file.name == "index.md":
            continue
        if domain_filter and parts[0] != domain_filter:
            continue
        results.append(md_file)
    return results


def load_bold_terms(path: str | Path) -> set[str]:
    """Load terms from bold-pattern extraction output for dedup."""
    bold_path = Path(path)
    if not bold_path.exists():
        return set()
    try:
        with open(bold_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return set()
    terms = data.get("terms", [])
    return {t["term"].lower().strip() for t in terms if "term" in t}


def extract_node_id(content: str) -> str:
    """Extract Node ID from blockquote header."""
    match = NODE_ID_RE.search(content)
    return match.group(1).strip() if match else ""


def clean_chunk(text: str) -> str:
    """Strip leading determiners and surrounding punctuation from a noun chunk."""
    words = text.split()
    while words and words[0].lower().strip(PUNCT_STRIP) in LEADING_DETERMINERS:
        words.pop(0)
    if not words:
        return ""
    cleaned = " ".join(words).strip(PUNCT_STRIP)
    return cleaned


def is_significant_noun_phrase(text: str, nlp_stopwords: set[str]) -> bool:
    """Check if a noun phrase is likely a significant technical term."""
    words = text.lower().split()
    if not words:
        return False
    if all(w in nlp_stopwords for w in words):
        return False
    if len(words) == 1 and words[0] in nlp_stopwords:
        return False
    if len(words) == 1 and words[0] in EXTRA_SINGLE_WORD_STOPS:
        return False
    return True


def _extract_context(span, doc) -> str:
    """Extract the first sentence containing the given span."""
    sent = span.sent
    if sent is None:
        start = max(0, span.start_char - 100)
        end = min(len(doc.text), span.end_char + 100)
        context = doc.text[start:end].strip()
    else:
        context = sent.text.strip()
    context = re.sub(r"\s+", " ", context)
    if len(context) > 300:
        context = context[:297] + "..."
    return context


def apply_corpus_filters(
    file_results: list[list[dict]],
    min_freq: int = 2,
    min_length: int = 3,
    single_word_min_freq: int = 10,
    verbose: bool = False,
) -> list[dict]:
    """Apply corpus-level frequency and specificity filters.

    Single-word: freq >= single_word_min_freq
    2-3 words: freq >= min_freq
    4+ words: freq >= min_freq
    Deduplicates by term_lower globally.
    """
    term_freq: Counter = Counter()
    for file_terms in file_results:
        for entry in file_terms:
            term_freq[entry["term"].lower()] += entry["count"]

    if verbose:
        top_terms = term_freq.most_common(20)
        print("  Top 20 terms by frequency:")
        for term, freq in top_terms:
            print("    {} ({})".format(term, freq))

    output_terms = []
    seen_terms = set()

    for file_terms in file_results:
        for entry in file_terms:
            term_lower = entry["term"].lower()
            word_count = len(term_lower.split())
            freq = term_freq[term_lower]

            if word_count == 1:
                if freq < single_word_min_freq:
                    continue
            else:
                if freq < min_freq:
                    continue

            if len(term_lower) < min_length:
                continue

            if term_lower in seen_terms:
                continue
            seen_terms.add(term_lower)

            output_terms.append({
                "term": entry["term"],
                "definition": entry["context"],
                "source_file": entry["source_file"],
                "source_node_id": entry["source_node_id"],
                "source_domain": entry["source_domain"],
                "context_type": "prose",
                "is_chemical_formula": entry["is_chemical"],
                "extraction_method": "nlp",
                "frequency": freq,
            })

    return output_terms


def _process_candidates(doc, fd, bold_terms, nlp_stopwords):
    """Extract candidate terms from a single spaCy Doc."""
    candidates: dict[str, dict] = {}

    for chunk in doc.noun_chunks:
        chunk_text = clean_chunk(chunk.text)
        if not chunk_text:
            continue
        chunk_lower = chunk_text.lower().strip()

        if len(chunk_lower) < 3:
            continue
        if not chunk_lower[0].isalpha():
            continue
        if not is_significant_noun_phrase(chunk_lower, nlp_stopwords):
            continue
        if chunk_lower in bold_terms:
            continue

        alpha_count = sum(1 for c in chunk_lower if c.isalpha())
        if alpha_count < 2:
            continue

        word_count = len(chunk_lower.split())
        if word_count > 8:
            continue
        if word_count == 1 and chunk_lower in EXTRA_SINGLE_WORD_STOPS:
            continue

        is_chemical = bool(UNICODE_SUBSCRIPT_RE.search(chunk_text))
        context = _extract_context(chunk, doc)

        if chunk_lower in candidates:
            candidates[chunk_lower]["count"] += 1
        else:
            candidates[chunk_lower] = {
                "term": chunk_text,
                "count": 1,
                "context": context,
                "is_chemical": is_chemical,
                "source_file": fd["source_file"],
                "source_node_id": fd["source_node_id"],
                "source_domain": fd["source_domain"],
            }

    for ent in doc.ents:
        ent_text = ent.text.strip().strip(PUNCT_STRIP)
        ent_lower = ent_text.lower().strip()

        if len(ent_lower) < 3:
            continue
        if not ent_lower[0].isalpha():
            continue
        if ent_lower in bold_terms:
            continue
        if not is_significant_noun_phrase(ent_lower, nlp_stopwords):
            continue

        word_count = len(ent_lower.split())
        if word_count > 8:
            continue
        if word_count == 1 and ent_lower in EXTRA_SINGLE_WORD_STOPS:
            continue

        is_chemical = bool(UNICODE_SUBSCRIPT_RE.search(ent_text))
        context = _extract_context(ent, doc)

        if ent_lower in candidates:
            candidates[ent_lower]["count"] += 1
        else:
            candidates[ent_lower] = {
                "term": ent_text,
                "count": 1,
                "context": context,
                "is_chemical": is_chemical,
                "source_file": fd["source_file"],
                "source_node_id": fd["source_node_id"],
                "source_domain": fd["source_domain"],
            }

    return candidates


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Extract significant nouns and verbs from article prose "
            "via spaCy NLP (supplements bold-pattern extraction)"
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Output to stdout as JSON instead of writing file",
    )
    parser.add_argument(
        "--domain",
        default=None,
        help="Process only a specific domain (e.g. 'chemistry')",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Progress reporting",
    )
    parser.add_argument(
        "--bold-output",
        default=None,
        help=(
            "Path to bold-pattern extraction output (for dedup). "
            "Default: data/glossary-raw.json"
        ),
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Output file path (default: data/glossary-nlp-raw.json)",
    )
    parser.add_argument(
        "--min-freq",
        type=int,
        default=2,
        help="Minimum corpus-wide frequency for multi-word terms (default: 2)",
    )
    args = parser.parse_args()

    # --- Check spaCy model availability ------------------------------------
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print(
            "ERROR: spaCy model 'en_core_web_sm' not found. Install with:\n"
            "  python3 -m spacy download en_core_web_sm",
            file=sys.stderr,
        )
        sys.exit(1)

    # --- Load bold terms for dedup -----------------------------------------
    bold_path = args.bold_output or str(DATA_DIR / "glossary-raw.json")
    bold_terms = load_bold_terms(bold_path)
    if args.verbose:
        print("Loaded {} bold-pattern terms for dedup from {}".format(
            len(bold_terms), bold_path
        ))

    # --- Combine spaCy stopwords with domain stop words --------------------
    nlp_stopwords = set(DOMAIN_STOP_WORDS)
    for word in nlp.Defaults.stop_words:
        nlp_stopwords.add(word.lower())

    # --- Enumerate files ---------------------------------------------------
    docs_dir = DOCS_DIR
    if not docs_dir.is_dir():
        print("ERROR: docs directory not found: {}".format(docs_dir), file=sys.stderr)
        sys.exit(1)

    md_files = enumerate_markdown_files(docs_dir, domain_filter=args.domain)
    if not md_files:
        print("No markdown files found.", file=sys.stderr)
        sys.exit(1)

    if args.verbose:
        print("Processing {} files...".format(len(md_files)))
        if args.domain:
            print("  Domain filter: {}".format(args.domain))

    # --- Read and clean files ----------------------------------------------
    file_data = []
    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        rel = md_file.relative_to(docs_dir)
        parts = rel.parts

        clean_text = strip_markdown(content)
        if len(clean_text) < 100:
            continue

        file_data.append({
            "rel": rel,
            "clean_text": clean_text,
            "source_file": str(rel),
            "source_domain": parts[0] if len(parts) > 1 else "",
            "source_node_id": extract_node_id(content),
        })

    if args.verbose:
        print("  {} files have sufficient content for NLP".format(len(file_data)))

    # --- Process through spaCy via pipe ------------------------------------
    texts = [fd["clean_text"] for fd in file_data]
    file_results: list[list[dict]] = []

    for doc, fd in zip(nlp.pipe(texts, batch_size=20, disable=["textcat"]), file_data):
        candidates = _process_candidates(doc, fd, bold_terms, nlp_stopwords)
        if candidates:
            file_results.append(list(candidates.values()))
            if args.verbose:
                print("  {} candidates from {}".format(
                    len(candidates), fd["source_file"]
                ))

    # --- Apply corpus-level filters ----------------------------------------
    if args.verbose:
        print("Applying corpus-level filters (min_freq={})...".format(args.min_freq))

    output_terms = apply_corpus_filters(
        file_results,
        min_freq=args.min_freq,
        verbose=args.verbose,
    )

    output_terms.sort(key=lambda t: (-t["frequency"], t["term"].lower()))

    domains_seen = {t["source_domain"] for t in output_terms if t["source_domain"]}

    output = {
        "terms": output_terms,
        "stats": {
            "total_terms": len(output_terms),
            "domains_covered": len(domains_seen),
            "articles_processed": len(md_files),
            "bold_terms_excluded": len(bold_terms),
            "generated": datetime.now(timezone.utc).isoformat(),
        },
    }

    if args.dry_run:
        json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    else:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print("Wrote {} terms to {}".format(len(output_terms), output_path))

    if args.verbose:
        print("Total terms: {}".format(len(output_terms)))
        print("Domains covered: {}".format(len(domains_seen)))
        print("Articles processed: {}".format(len(md_files)))


if __name__ == "__main__":
    main()
