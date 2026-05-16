#!/usr/bin/env bash
# Render all Mermaid diagram files to SVG/PNG
# Requires: npm install -g @mermaid-js/mermaid-cli
# Usage: ./scripts/render-mermaid.sh [format]

set -euo pipefail

FORMAT="${1:-svg}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
SOURCE_DIR="$PROJECT_DIR/diagrams/mermaid"
OUTPUT_DIR="$PROJECT_DIR/diagrams/rendered"

# Create output directory
mkdir -p "$OUTPUT_DIR"

echo "Rendering Mermaid diagrams..."
echo "  Source: $SOURCE_DIR"
echo "  Output: $OUTPUT_DIR"
echo "  Format: $FORMAT"
echo

# Find and render all .mmd files
count=0
failed=0

find "$SOURCE_DIR" -name "*.mmd" -type f | while read -r file; do
    # Get relative path from source dir
    relpath="${file#$SOURCE_DIR/}"
    # Change extension
    outfile="${relpath%.mmd}.$FORMAT"
    # Full output path
    outfull="$OUTPUT_DIR/$outfile"

    # Create subdirectory if needed
    mkdir -p "$(dirname "$outfull")"

    echo "  Rendering: $relpath -> $outfile"
    if mmdc -i "$file" -o "$outfull" -t default; then
        count=$((count + 1))
    else
        echo "    FAILED: $relpath"
        failed=$((failed + 1))
    fi
done

echo
echo "Done. Rendered $count diagrams, $failed failures."
echo "Output in: $OUTPUT_DIR"
