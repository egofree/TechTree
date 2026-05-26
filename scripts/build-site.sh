#!/usr/bin/env bash
# Build offline HTML browser site from tech-tree-bootstrap data
# Requires: python3, markdown-it-py (pip install markdown-it-py)
# Optional: mmdc (npm i -g @mermaid-js/mermaid-cli) for SVG rendering
# Usage: ./scripts/build-site.sh [--no-svg] [--clean] [--verbose]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$PROJECT_DIR/data"
DOCS_DIR="$PROJECT_DIR/docs"
MERMAID_DIR="$PROJECT_DIR/diagrams/mermaid"
SITE_DIR="$PROJECT_DIR/site"

NODES_FILE="$DATA_DIR/nodes.json"

# --- Flags ---
NO_SVG=false
CLEAN=false
VERBOSE=false
WARNINGS=0

for arg in "$@"; do
    case "$arg" in
        --no-svg)   NO_SVG=true ;;
        --clean)    CLEAN=true ;;
        --verbose)  VERBOSE=true ;;
        *)          echo "Unknown flag: $arg" >&2; exit 1 ;;
    esac
done

# --- Helpers ---

log() {
    if $VERBOSE; then
        echo "  $1"
    fi
}

warn() {
    echo "  WARNING: $1" >&2
    WARNINGS=$((WARNINGS + 1))
}

# --- Dependency checks ---

command -v python3 &>/dev/null || {
    echo "ERROR: python3 is required but not found in PATH" >&2
    exit 1
}

python3 -c "import markdown_it" 2>/dev/null || {
    echo "ERROR: markdown-it-py is required (pip install markdown-it-py)" >&2
    exit 1
}

command -v jq &>/dev/null || {
    echo "ERROR: jq is required but not found in PATH" >&2
    exit 1
}

if ! $NO_SVG && ! command -v mmdc &>/dev/null; then
    warn "mmdc not found — SVG rendering skipped (install: npm i -g @mermaid-js/mermaid-cli)"
    NO_SVG=true
fi

# --- Data validation ---

if [[ ! -f "$NODES_FILE" ]]; then
    echo "ERROR: $NODES_FILE not found" >&2
    exit 1
fi

# --- Clean ---

if [[ -d "$SITE_DIR" ]]; then
    log "Removing old site/ directory..."
    rm -rf "$SITE_DIR"
fi

# --- Create directory structure ---

log "Creating site directory structure..."
mkdir -p "$SITE_DIR"

DOMAIN_IDS=$(jq -r '.nodes[] | select(.level == "domain") | .id' "$NODES_FILE")
DOMAIN_COUNT=0

while IFS= read -r domain_id; do
    [[ -z "$domain_id" ]] && continue
    mkdir -p "$SITE_DIR/docs/$domain_id"
    DOMAIN_COUNT=$((DOMAIN_COUNT + 1))
done <<< "$DOMAIN_IDS"

mkdir -p "$SITE_DIR/diagrams"
mkdir -p "$SITE_DIR/assets"

# --- Copy CSS ---

log "Copying CSS..."
cp "$SCRIPT_DIR/assets/style.css" "$SITE_DIR/assets/style.css"

# --- Copy JS assets ---

log "Copying JS assets..."
cp "$SCRIPT_DIR/assets/mermaid.min.js" "$SITE_DIR/assets/mermaid.min.js"
cp "$SCRIPT_DIR/assets/fuse.min.js" "$SITE_DIR/assets/fuse.min.js"
cp "$SCRIPT_DIR/assets/search.js" "$SITE_DIR/assets/search.js"
cp "$SCRIPT_DIR/assets/main.js" "$SITE_DIR/assets/main.js"

# --- Copy mermaid diagrams ---

MMD_COPIED=0
if [[ -d "$MERMAID_DIR" ]]; then
    while IFS= read -r mmd_file; do
        [[ -z "$mmd_file" ]] && continue
        cp "$mmd_file" "$SITE_DIR/diagrams/"
        MMD_COPIED=$((MMD_COPIED + 1))
    done < <(find "$MERMAID_DIR" -maxdepth 1 -name "*.mmd" -type f)
    log "Copied $MMD_COPIED mermaid diagrams"
else
    warn "diagrams/mermaid/ not found — run generate-diagrams.sh first"
fi

# --- Render SVGs ---

SVG_COUNT=0
if ! $NO_SVG && [[ -d "$SITE_DIR/diagrams" ]]; then
    log "Rendering SVGs with mmdc..."
    while IFS= read -r mmd_file; do
        [[ -z "$mmd_file" ]] && continue
        local_name=$(basename "$mmd_file" .mmd)
        svg_out="$SITE_DIR/diagrams/${local_name}.svg"
        if mmdc -i "$mmd_file" -o "$svg_out" -b white 2>/dev/null; then
            SVG_COUNT=$((SVG_COUNT + 1))
            log "Rendered ${local_name}.svg"
        else
            warn "Failed to render ${local_name}.svg"
        fi
    done < <(find "$SITE_DIR/diagrams" -maxdepth 1 -name "*.mmd" -type f)
fi

# --- Generate all HTML pages ---

log "Generating HTML pages..."
HTML_COUNT=0

python3 -c "import yaml" 2>/dev/null || {
    echo "ERROR: PyYAML is required (pip install pyyaml)" >&2
    exit 1
}

python3 "$SCRIPT_DIR/generate-pages.py" \
    "$PROJECT_DIR" \
    "$SITE_DIR" \
    "$SITE_DIR/diagrams" \
    "$VERBOSE" \
    "false"

# --- Generate glossary pages ---

log "Generating glossary pages..."

mkdir -p "$SITE_DIR/glossary"

python3 "$SCRIPT_DIR/generate-glossary-pages.py" \
    "$PROJECT_DIR" \
    "$SITE_DIR" \
    "$VERBOSE"

GLOSSARY_COUNT=$(find "$SITE_DIR/glossary" -name "*.html" -type f 2>/dev/null | wc -l)

# --- Add glossary entries to search index ---

log "Adding glossary entries to search index..."

python3 - "$DATA_DIR/glossary.json" "$SITE_DIR/assets/search-index.js" "$VERBOSE" <<'PYEOF'
import json, sys

glossary_path = sys.argv[1]
search_index_path = sys.argv[2]
verbose = sys.argv[3] == "true"

try:
    glossary_data = json.loads(open(glossary_path, encoding="utf-8").read())
except FileNotFoundError:
    sys.exit(0)

glossary_entries = []
for term in glossary_data.get("terms", []):
    slug = term["slug"]
    if term.get("created"):
        url = "glossary/" + slug + ".html"
    else:
        url = "glossary/index.html"
    glossary_entries.append({
        "title": term["term"],
        "url": url,
        "content": term.get("definition", ""),
    })

if not glossary_entries:
    sys.exit(0)

with open(search_index_path, "r", encoding="utf-8") as f:
    content = f.read()

json_str = content[len("window.SEARCH_INDEX = "):-len(";")]
existing = json.loads(json_str)
existing.extend(glossary_entries)

with open(search_index_path, "w", encoding="utf-8") as f:
    f.write("window.SEARCH_INDEX = " + json.dumps(existing, ensure_ascii=False) + ";")

if verbose:
    print(f"  Added {len(glossary_entries)} glossary entries to search index")
PYEOF

# --- Linkify glossary terms ---

log "Adding glossary hyperlinks..."

python3 "$SCRIPT_DIR/link-glossary.py" \
    --site-dir "$SITE_DIR" \
    --glossary "$DATA_DIR/glossary.json" \
    $([ "$VERBOSE" = true ] && echo "--verbose")

HTML_COUNT=$(find "$SITE_DIR" -name "*.html" -type f | wc -l)

# --- Summary ---

echo ""
echo "=== Build Summary ==="
echo "  Domain directories: $DOMAIN_COUNT"
echo "  HTML pages:         $HTML_COUNT"
echo "  Glossary pages:     $GLOSSARY_COUNT"
echo "  Mermaid diagrams:   $MMD_COPIED"
if $NO_SVG; then
    echo "  SVG renders:        skipped (--no-svg or mmdc unavailable)"
else
    echo "  SVG renders:        $SVG_COUNT"
fi
echo "  Warnings:           $WARNINGS"
echo "  Output:             $SITE_DIR"
echo ""
if [[ "$WARNINGS" -gt 0 ]]; then
    echo "  Build completed with warnings."
else
    echo "  Build completed successfully."
fi
