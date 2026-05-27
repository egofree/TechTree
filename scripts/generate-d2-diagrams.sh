#!/usr/bin/env bash
# Wrapper: delegates to the unified Python diagram generator.
# Original bash+jq implementation preserved in generate-d2-diagrams.sh.bak
set -euo pipefail
python3 "$(dirname "$0")/generate-diagrams.py" --format d2
