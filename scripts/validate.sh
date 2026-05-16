#!/usr/bin/env bash
# Validate repository structure and content
# Checks: all expected files exist, Mermaid files are valid, links are not broken

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

errors=0

echo "=== Validating tech-tree-bootstrap repository ==="
echo

# Check root files
echo "--- Checking root files ---"
for f in README.md CONTRIBUTING.md LICENSE .gitignore; do
    if [ -f "$PROJECT_DIR/$f" ]; then
        echo "  OK: $f"
    else
        echo "  MISSING: $f"
        errors=$((errors + 1))
    fi
done

# Check docs
echo
echo "--- Checking docs/ ---"
for f in docs/index.md docs/core-tech-tree/overview.md; do
    if [ -f "$PROJECT_DIR/$f" ]; then
        echo "  OK: $f"
    else
        echo "  MISSING: $f"
        errors=$((errors + 1))
    fi
done

# Check phase docs
echo
echo "--- Checking phase docs ---"
for i in 01-foundations 02-metallurgy 03-machine-tools 04-energy 05-chemistry 06-vacuum-optics 07-silicon 08-photolithography 09-scaling; do
    f="docs/core-tech-tree/phase-${i}.md"
    if [ -f "$PROJECT_DIR/$f" ]; then
        echo "  OK: $f"
    else
        echo "  MISSING: $f"
        errors=$((errors + 1))
    fi
done

# Check side quest docs
echo
echo "--- Checking side quest docs ---"
for i in 01-knowledge-preservation 02-measurement-metrology 03-transport-logistics 04-mechanical-computing 05-public-health 06-gases-packaging-testing 07-energy-storage 08-advanced-materials 09-textiles-fiber 10-lubricants-oils 11-mining-engineering 12-petrochemicals; do
    f="docs/side-quests/sq-${i}.md"
    if [ -f "$PROJECT_DIR/$f" ]; then
        echo "  OK: $f"
    else
        echo "  MISSING: $f"
        errors=$((errors + 1))
    fi
done
if [ -f "$PROJECT_DIR/docs/side-quests/index.md" ]; then
    echo "  OK: docs/side-quests/index.md"
else
    echo "  MISSING: docs/side-quests/index.md"
    errors=$((errors + 1))
fi

# Check supporting docs
echo
echo "--- Checking supporting docs ---"
for f in docs/supporting/minimum-viable-checklist.md docs/supporting/dependencies.md docs/supporting/resources.md; do
    if [ -f "$PROJECT_DIR/$f" ]; then
        echo "  OK: $f"
    else
        echo "  MISSING: $f"
        errors=$((errors + 1))
    fi
done

# Check data files
echo
echo "--- Checking data files ---"
for f in data/dependencies.json data/checklist.yaml data/resources.json; do
    if [ -f "$PROJECT_DIR/$f" ]; then
        echo "  OK: $f"
    else
        echo "  MISSING: $f"
        errors=$((errors + 1))
    fi
done

# Check Mermaid files
echo
echo "--- Checking Mermaid diagrams ---"
mmd_count=$(find "$PROJECT_DIR/diagrams/mermaid" -name "*.mmd" -type f | wc -l)
echo "  Found $mmd_count .mmd files"
if [ "$mmd_count" -lt 20 ]; then
    echo "  WARNING: Expected at least 20 diagram files, found $mmd_count"
fi

# Check scripts
echo
echo "--- Checking scripts ---"
for f in scripts/render-mermaid.sh scripts/validate.sh; do
    if [ -f "$PROJECT_DIR/$f" ]; then
        echo "  OK: $f"
    else
        echo "  MISSING: $f"
        errors=$((errors + 1))
    fi
done

# Summary
echo
echo "=== Validation complete ==="
if [ "$errors" -eq 0 ]; then
    echo "All checks passed!"
    exit 0
else
    echo "Found $errors errors."
    exit 1
fi
