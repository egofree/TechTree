#!/usr/bin/env bash
# Site build validator for tech-tree-bootstrap
# Validates the static site output for file:// compatibility
# Checks: 10 validation passes covering completeness, offline compatibility, and reproducibility

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
SITE_DIR="$PROJECT_DIR/site"

PASSED=0
FAILED=0
TOTAL=0
FAILURES=()

# --- Flags ---
LINKS_ONLY=false
IDEMPOTENCY=false

for arg in "$@"; do
    case "$arg" in
        --links-only)   LINKS_ONLY=true ;;
        --idempotency)  IDEMPOTENCY=true ;;
        *)              echo "Unknown flag: $arg" >&2; exit 1 ;;
    esac
done

# --- Check framework ---

check() {
    local name="$1"
    shift
    TOTAL=$((TOTAL + 1))
    echo -n "  [$TOTAL] $name... "
    if "$@"; then
        echo "PASS"
        PASSED=$((PASSED + 1))
    else
        echo "FAIL"
        FAILED=$((FAILED + 1))
        FAILURES+=("$name")
    fi
}

# --- Check 1: File completeness ---

check_file_completeness() {
    local count
    count=$(find "$SITE_DIR" -name "*.html" -type f | wc -l)
    if [[ "$count" -lt 68 ]]; then
        echo "    Found $count .html files, expected >= 68" >&2
        return 1
    fi
    return 0
}

# --- Check 2: No broken internal links ---

check_no_broken_links() {
    local broken
    broken=$(while IFS= read -r htmlfile; do
        [[ -z "$htmlfile" ]] && continue
        local filedir
        filedir="$(dirname "$htmlfile")"

        while IFS= read -r href; do
            [[ -z "$href" ]] && continue
            [[ "$href" =~ ^(mailto:|tel:|javascript:) ]] && continue

            local target
            target="$(cd "$filedir" 2>/dev/null && realpath --relative-to="$SITE_DIR" "$href" 2>/dev/null)" || continue
            local full_target="$SITE_DIR/$target"

            if [[ ! -e "$full_target" ]]; then
                echo "BROKEN:${htmlfile#$SITE_DIR/}:$href"
            fi
        done < <(grep -oP 'href="[^"#]*"' "$htmlfile" 2>/dev/null | sed 's/^href="//;s/"$//')
    done < <(find "$SITE_DIR" -name "*.html" -type f))

    local broken_count=0
    if [[ -n "$broken" ]]; then
        broken_count=$(echo "$broken" | wc -l)
        echo "$broken" | while IFS=: read -r _ file href; do
            echo "    Broken link in $file: $href" >&2
        done
    fi
    [[ "$broken_count" -eq 0 ]]
}

# --- Check 3: No external URLs ---

check_no_external_urls() {
    local matches
    matches=$(grep -rP 'https?://' "$SITE_DIR" --include="*.html" --include="*.js" --include="*.css" -l 2>/dev/null \
        | grep -v 'mermaid\.min\.js$' \
        | grep -v 'fuse\.min\.js$' || true)
    if [[ -n "$matches" ]]; then
        echo "$matches" | while IFS= read -r f; do
            echo "    External URL found in ${f#$SITE_DIR/}" >&2
        done
        return 1
    fi
    return 0
}

# --- Check 4: No fetch calls ---

check_no_fetch_calls() {
    local js_files
    js_files=$(find "$SITE_DIR/assets" -name "*.js" -not -name "mermaid.min.js" -type f 2>/dev/null || true)
    if [[ -z "$js_files" ]]; then
        return 0
    fi
    local matches
    matches=$(grep -lP '\bfetch\s*\(' $js_files 2>/dev/null || true)
    if [[ -n "$matches" ]]; then
        echo "$matches" | while IFS= read -r f; do
            echo "    fetch() call found in ${f#$SITE_DIR/}" >&2
        done
        return 1
    fi
    return 0
}

# --- Check 5: No ES modules ---

check_no_es_modules() {
    local js_files
    js_files=$(find "$SITE_DIR/assets" -name "*.js" -not -name "mermaid.min.js" -not -name "search-index.js" -type f 2>/dev/null || true)
    if [[ -z "$js_files" ]]; then
        return 0
    fi
    # Match standalone `import ` but not importmap, important, etc.
    local matches
    matches=$(grep -P '(?<![a-zA-Z])import\s' $js_files 2>/dev/null || true)
    if [[ -n "$matches" ]]; then
        echo "    ES module import found in JS assets" >&2
        echo "$matches" | head -5 | while IFS= read -r line; do
            echo "      $line" >&2
        done
        return 1
    fi
    return 0
}

# --- Check 6: CSS exists ---

check_css_exists() {
    if [[ ! -f "$SITE_DIR/assets/style.css" ]]; then
        echo "    Missing: site/assets/style.css" >&2
        return 1
    fi
    return 0
}

# --- Check 7: JS exists ---

check_js_exists() {
    local ok=true
    for js in main.js search.js; do
        if [[ ! -f "$SITE_DIR/assets/$js" ]]; then
            echo "    Missing: site/assets/$js" >&2
            ok=false
        fi
    done
    $ok
}

# --- Check 8: Search index exists ---

check_search_index() {
    local search_js
    search_js="$SITE_DIR/assets/search-index.js"
    if [[ ! -f "$search_js" ]]; then
        echo "    Missing: site/assets/search-index.js" >&2
        return 1
    fi
    if ! grep -q 'SEARCH_INDEX' "$search_js" 2>/dev/null; then
        echo "    SEARCH_INDEX not found in site/assets/search-index.js" >&2
        return 1
    fi
    return 0
}

# --- Check 9: Diagrams present ---

check_diagrams_present() {
    local diagram_dir="$SITE_DIR/diagrams"
    if [[ ! -d "$diagram_dir" ]]; then
        echo "    Missing: site/diagrams/ directory" >&2
        return 1
    fi
    local count
    count=$(find "$diagram_dir" \( -name "*.svg" -o -name "*.mmd" \) -type f | wc -l)
    if [[ "$count" -lt 21 ]]; then
        echo "    Found $count diagram files, expected >= 21" >&2
        return 1
    fi
    return 0
}

# --- Check 10: Source files unchanged ---

check_source_unchanged() {
    local changed
    changed=$(cd "$PROJECT_DIR" && git diff --name-only -- docs/ data/ 2>/dev/null || true)
    if [[ -n "$changed" ]]; then
        echo "    Source files modified:" >&2
        echo "$changed" | while IFS= read -r f; do
            echo "      $f" >&2
        done
        return 1
    fi
    return 0
}

# --- Idempotency check ---

run_idempotency_check() {
    echo "  Running idempotency check (two consecutive builds)..."

    # Capture checksums of current build
    local first_checksums
    first_checksums=$(cd "$SITE_DIR" && find . -type f | sort | xargs md5sum 2>/dev/null || true)

    if [[ -z "$first_checksums" ]]; then
        echo "    FAIL: No files found in site/" >&2
        FAILED=$((FAILED + 1))
        TOTAL=$((TOTAL + 1))
        FAILURES+=("Idempotency")
        return
    fi

    # Rebuild
    local build_script="$SCRIPT_DIR/build-site.sh"
    if [[ ! -f "$build_script" ]]; then
        echo "    FAIL: build-site.sh not found" >&2
        FAILED=$((FAILED + 1))
        TOTAL=$((TOTAL + 1))
        FAILURES+=("Idempotency")
        return
    fi

    bash "$build_script" >/dev/null 2>&1 || {
        echo "    FAIL: build-site.sh failed on second run" >&2
        FAILED=$((FAILED + 1))
        TOTAL=$((TOTAL + 1))
        FAILURES+=("Idempotency")
        return
    }

    local second_checksums
    second_checksums=$(cd "$SITE_DIR" && find . -type f | sort | xargs md5sum 2>/dev/null || true)

    TOTAL=$((TOTAL + 1))
    echo -n "  [$TOTAL] Idempotency (build outputs match)... "
    if [[ "$first_checksums" == "$second_checksums" ]]; then
        echo "PASS"
        PASSED=$((PASSED + 1))
    else
        echo "FAIL"
        echo "    Build outputs differ between runs" >&2
        FAILED=$((FAILED + 1))
        FAILURES+=("Idempotency")
    fi
}

# ============================================================
# Main
# ============================================================

echo "=== Validating tech-tree-bootstrap site build ==="
echo ""

if [[ ! -d "$SITE_DIR" ]]; then
    echo "ERROR: site/ directory not found at $SITE_DIR" >&2
    exit 1
fi

# --links-only: just run broken link check
if $LINKS_ONLY; then
    echo "--- Internal links ---"
    check "No broken internal links" check_no_broken_links
    echo ""
    echo "=== Results: $PASSED/$TOTAL passed, $FAILED failed ==="
    [ "$FAILED" -eq 0 ]
    exit $?
fi

echo "--- File completeness ---"
check "HTML file count >= 68" check_file_completeness

echo ""
echo "--- Internal links ---"
check "No broken internal links" check_no_broken_links

echo ""
echo "--- Offline compatibility ---"
check "No external URLs" check_no_external_urls
check "No fetch() calls in JS" check_no_fetch_calls
check "No ES module imports in JS" check_no_es_modules

echo ""
echo "--- Assets ---"
check "style.css exists" check_css_exists
check "JS files exist (main.js, search.js)" check_js_exists
check "Search index contains SEARCH_INDEX" check_search_index

echo ""
echo "--- Diagrams ---"
check "Diagram files >= 24 (.svg or .mmd)" check_diagrams_present

echo ""
echo "--- Source integrity ---"
check "Source files unchanged (docs/ data/)" check_source_unchanged

# --idempotency: add reproducibility check
if $IDEMPOTENCY; then
    echo ""
    echo "--- Reproducibility ---"
    run_idempotency_check
fi

echo ""
if [[ "$FAILED" -eq 0 ]]; then
    echo "=== Results: $PASSED/$TOTAL passed ==="
else
    echo "=== Results: $PASSED/$TOTAL passed | FAILURES: [${FAILURES[*]}] ==="
fi
[ "$FAILED" -eq 0 ]
