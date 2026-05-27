#!/usr/bin/env bash
# Conformance test suite runner for tech-tree-bootstrap JSON-LD schemas.
# Validates test entity files against their corresponding JSON Schema definitions.
# Exit 0 only if ALL tests pass.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
SCHEMA_DIR="$ROOT_DIR/data/schema"
VALID_DIR="$ROOT_DIR/tests/valid"
INVALID_DIR="$ROOT_DIR/tests/invalid"

# Counters
valid_pass=0
valid_fail=0
invalid_pass=0
invalid_fail=0
failures=()

# Map filename prefix to schema file
schema_for() {
    local basename="$1"
    local prefix="${basename%%-*}"
    case "$prefix" in
        domain)     echo "$SCHEMA_DIR/domain.schema.json" ;;
        capability) echo "$SCHEMA_DIR/capability.schema.json" ;;
        process)    echo "$SCHEMA_DIR/process.schema.json" ;;
        product)    echo "$SCHEMA_DIR/product.schema.json" ;;
        dep)        echo "$SCHEMA_DIR/dependency.schema.json" ;;
        *)          echo "" ;;
    esac
}

# Validate a single file against a schema using python3 + jsonschema.
# Returns 0 if validation passes, 1 if validation fails (including parse errors).
validate() {
    local schema_file="$1"
    local test_file="$2"

    python3 -c "
import sys, json
from jsonschema import validate, ValidationError

schema_file = sys.argv[1]
test_file = sys.argv[2]

with open(schema_file) as f:
    schema = json.load(f)
with open(test_file) as f:
    instance = json.load(f)

try:
    validate(instance=instance, schema=schema)
    sys.exit(0)
except ValidationError:
    sys.exit(1)
except json.JSONDecodeError:
    sys.exit(1)
" "$schema_file" "$test_file" 2>/dev/null
}

echo "========================================="
echo " Conformance Test Suite"
echo "========================================="
echo ""

# --- Valid tests: must PASS validation ---
echo "--- Valid test files (expect PASS) ---"
if [ -d "$VALID_DIR" ]; then
    for test_file in "$VALID_DIR"/*.json; do
        [ -f "$test_file" ] || continue
        basename=$(basename "$test_file")
        schema_file=$(schema_for "$basename")

        if [ -z "$schema_file" ] || [ ! -f "$schema_file" ]; then
            echo "  SKIP $basename (no schema mapping)"
            valid_fail=$((valid_fail + 1))
            failures+=("VALID:$basename:no_schema")
            continue
        fi

        if validate "$schema_file" "$test_file"; then
            echo "  PASS $basename"
            valid_pass=$((valid_pass + 1))
        else
            echo "  FAIL $basename (expected PASS, got validation error)"
            valid_fail=$((valid_fail + 1))
            failures+=("VALID:$basename:unexpected_failure")
        fi
    done
fi

echo ""

# --- Invalid tests: must FAIL validation ---
echo "--- Invalid test files (expect FAIL) ---"
if [ -d "$INVALID_DIR" ]; then
    for test_file in "$INVALID_DIR"/*.json; do
        [ -f "$test_file" ] || continue
        basename=$(basename "$test_file")
        schema_file=$(schema_for "$basename")

        if [ -z "$schema_file" ] || [ ! -f "$schema_file" ]; then
            echo "  SKIP $basename (no schema mapping)"
            invalid_fail=$((invalid_fail + 1))
            failures+=("INVALID:$basename:no_schema")
            continue
        fi

        if validate "$schema_file" "$test_file"; then
            echo "  FAIL $basename (expected FAIL, got PASS)"
            invalid_pass=$((invalid_pass + 1))
            failures+=("INVALID:$basename:unexpected_pass")
        else
            echo "  PASS $basename (correctly rejected)"
            invalid_fail=$((invalid_fail + 1))
        fi
    done
fi

echo ""
echo "========================================="
echo " Summary"
echo "========================================="

valid_total=$((valid_pass + valid_fail))
invalid_total=$((invalid_pass + invalid_fail))
total=$((valid_total + invalid_total))
total_pass=$((valid_pass + invalid_fail))

echo "  VALID   [$valid_pass/$valid_total pass]"
echo "  INVALID [$invalid_fail/$invalid_total reject]"
echo "  TOTAL   [$total_pass/$total]"
echo ""

if [ ${#failures[@]} -gt 0 ]; then
    echo "  Failures:"
    for f in "${failures[@]}"; do
        echo "    - $f"
    done
    echo ""
fi

if [ "$total_pass" -eq "$total" ] && [ "$total" -ge 50 ]; then
    echo "  Result: ALL PASS"
    exit 0
else
    echo "  Result: FAILURES DETECTED"
    exit 1
fi
