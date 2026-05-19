#!/usr/bin/env bash
# Generate all D2 diagrams from data/nodes.json + data/edges.json
# Requires: jq, d2 (https://d2lang.com)
# Usage: ./scripts/generate-d2-diagrams.sh [--list]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$PROJECT_DIR/data"
OUTPUT_DIR="$PROJECT_DIR/diagrams/d2"

NODES_FILE="$DATA_DIR/nodes.json"
EDGES_FILE="$DATA_DIR/edges.json"

# --- Helpers ---

# Check dependencies
if ! command -v jq &>/dev/null; then
    echo "ERROR: jq is required but not found in PATH" >&2
    exit 1
fi

if [[ ! -f "$NODES_FILE" ]]; then
    echo "ERROR: $NODES_FILE not found" >&2
    exit 1
fi

if [[ ! -f "$EDGES_FILE" ]]; then
    echo "ERROR: $EDGES_FILE not found" >&2
    exit 1
fi

# Sanitize a node ID for use as a D2 key (replace dots with underscores)
sanitize_id() {
    echo "$1" | tr '.' '_'
}

# Get the human-readable name for a node ID
get_name() {
    local node_id="$1"
    jq -r --arg id "$node_id" '.nodes[] | select(.id == $id) | .name' "$NODES_FILE"
}

# Get the level for a node ID
get_level() {
    local node_id="$1"
    jq -r --arg id "$node_id" '.nodes[] | select(.id == $id) | .level' "$NODES_FILE"
}

# Get the parent for a node ID
get_parent() {
    local node_id="$1"
    jq -r --arg id "$node_id" '.nodes[] | select(.id == $id) | .parent // ""' "$NODES_FILE"
}

# Get the domain (top-level) for a node ID
get_domain() {
    local node_id="$1"
    echo "$node_id" | cut -d'.' -f1
}

# Check if a node is critical
is_critical() {
    local node_id="$1"
    jq -r --arg id "$node_id" '.nodes[] | select(.id == $id) | .critical // false' "$NODES_FILE"
}

# Check if a node is an early win
is_early_win() {
    local node_id="$1"
    jq -r --arg id "$node_id" '.nodes[] | select(.id == $id) | .early_win // false' "$NODES_FILE"
}

# Check if a node is a pinnacle
is_pinnacle() {
    local node_id="$1"
    jq -r --arg id "$node_id" '.nodes[] | select(.id == $id) | .pinnacle // false' "$NODES_FILE"
}

# Quote a label if it contains special characters
quote_label() {
    local label="$1"
    if [[ "$label" == *"&"* || "$label" == *","* || "$label" == *"("* || "$label" == *")"* ]]; then
        echo "\"${label}\""
    else
        echo "${label}"
    fi
}

# Emit the shared config header
emit_header() {
    cat <<'HEADER'
vars: {
  d2-config: {
    layout-engine: elk
    pad: 20
    center: true
  }
}

direction: down
HEADER
}

# Emit the shared classes block
emit_classes() {
    cat <<'CLASSES'

classes: {
  domain: {
    style: {
      fill: "#e3f2fd"
      stroke: "#1976d2"
      stroke-width: 2
      border-radius: 4
    }
  }
  capability: {
    style: {
      fill: "#e8f5e9"
      stroke: "#388e3c"
      stroke-width: 2
    }
  }
  process: {
    style: {
      fill: "#fff3e0"
      stroke: "#f57c00"
      stroke-width: 2
    }
  }
  critical: {
    style: {
      fill: "#fff3e0"
      stroke: "#f57c00"
      stroke-width: 3
      bold: true
    }
  }
  earlyWin: {
    style: {
      fill: "#e8f5e9"
      stroke: "#388e3c"
      stroke-width: 3
    }
  }
  pinnacle: {
    style: {
      fill: "#fce4ec"
      stroke: "#c62828"
      stroke-width: 3
      bold: true
    }
  }
  external: {
    style: {
      fill: "#f5f5f5"
      stroke: "#9e9e9e"
      stroke-width: 1
    }
  }
  legend: {
    style: {
      fill: "#fafafa"
      stroke: "#bdbdbd"
      stroke-width: 1
      font-size: 13
    }
  }
  material-edge: {
    style: {
      stroke: "#333333"
      stroke-width: 2
    }
  }
  tool-edge: {
    style: {
      stroke: "#666666"
      stroke-width: 1
      stroke-dash: 3
    }
  }
}
CLASSES
}

# --- Diagram generators ---

generate_overview() {
    emit_header
    emit_classes

    echo ""
    echo "# ==================== DOMAIN NODES ===================="

    # Collect all domain IDs
    local domain_ids
    domain_ids=$(jq -r '.nodes[] | select(.level == "domain") | .id' "$NODES_FILE")

    # Emit domain node declarations
    while IFS= read -r did; do
        local safe_id
        safe_id=$(sanitize_id "$did")
        local name
        name=$(get_name "$did")
        local quoted_name
        quoted_name=$(quote_label "$name")
        echo "${safe_id}: ${quoted_name}"
    done <<< "$domain_ids"

    echo ""
    echo "# ==================== DOMAIN-LEVEL EDGES ===================="

    # Collect edges where both from and to are domain-level nodes
    jq -r '
        .edges[] |
        .from as $f | .to as $t |
        ($f | split(".")[0]) as $fd |
        ($t | split(".")[0]) as $td |
        select(
            (($fd == $f) and ($td == $t))
        ) |
        "\($f)|\($t)|\(.type)"
    ' "$EDGES_FILE" | while IFS='|' read -r from to etype; do
        local safe_from safe_to
        safe_from=$(sanitize_id "$from")
        safe_to=$(sanitize_id "$to")
        local edge_class="material-edge"
        if [[ "$etype" == "tool" ]]; then
            edge_class="tool-edge"
        fi
        echo "${safe_from} -> ${safe_to}: { class: ${edge_class} }"
    done

    # Cross-domain inferred edges
    echo ""
    echo "# ==================== CROSS-DOMAIN EDGES ===================="

    local domain_edges_raw
    domain_edges_raw=$(mktemp)
    jq -r '
        .edges[] |
        .from as $f | .to as $t |
        select(
            (($f | split(".")[0]) == $f) and (($t | split(".")[0]) == $t)
        ) |
        "\($f)|\($t)"
    ' "$EDGES_FILE" | sort -u > "$domain_edges_raw"

    jq -r '
        .edges[] |
        .from as $f | .to as $t |
        ($f | split(".")[0]) as $fd |
        ($t | split(".")[0]) as $td |
        select(
            ($fd != $td) and
            (($fd != $f) or ($td != $t))
        ) |
        "\($fd)|\($td)"
    ' "$EDGES_FILE" | sort -u | while IFS='|' read -r from_domain to_domain; do
        if ! grep -q "^${from_domain}|${to_domain}$" "$domain_edges_raw"; then
            local safe_from safe_to
            safe_from=$(sanitize_id "$from_domain")
            safe_to=$(sanitize_id "$to_domain")
            echo "${safe_from} -> ${safe_to}: { class: tool-edge }"
        fi
    done

    rm -f "$domain_edges_raw"

    # Apply class assignments for domains
    echo ""
    echo "# ==================== STYLING ===================="

    while IFS= read -r did; do
        local safe_id
        safe_id=$(sanitize_id "$did")
        local crit early pin
        crit=$(is_critical "$did")
        early=$(is_early_win "$did")
        pin=$(is_pinnacle "$did")
        if [[ "$pin" == "true" ]]; then
            echo "${safe_id}.class: pinnacle"
        elif [[ "$early" == "true" ]]; then
            echo "${safe_id}.class: earlyWin"
        elif [[ "$crit" == "true" ]]; then
            echo "${safe_id}.class: critical"
        else
            echo "${safe_id}.class: domain"
        fi
    done <<< "$domain_ids"

    echo ""
    echo "# ==================== LEGEND ===================="
    cat <<'LEGEND'
d2-legend: "Legend and Key Insights" {
  class: legend
  mat: "Solid arrow = material prerequisite (physical input consumed)" {
    style: {
      stroke: "#333333"
      stroke-width: 2
    }
  }
  tool: "Dashed arrow = tool prerequisite (equipment/infrastructure needed)" {
    style: {
      stroke: "#666666"
      stroke-dash: 3
    }
  }
  note1: "Machine Tools is the master enabler: every later stage depends on precision parts"
  note2: "Iteration is everywhere: tools make better tools, crude silicon enables purer silicon"
  note3: "Solar cells create a critical power feedback loop — the most important positive feedback in the tree"
  note4: "High-end GPUs are the long-term pinnacle: requires the entire mature ecosystem + generations of refinement"
  note5: "Realistic timeline: basic solar cells in decades. Full GPU capability: 50 to 200+ years"
}
LEGEND
}

generate_domain_diagram() {
    local domain_id="$1"
    local domain_name
    domain_name=$(get_name "$domain_id")
    local safe_domain_id
    safe_domain_id=$(sanitize_id "$domain_id")

    emit_header
    emit_classes

    local children
    children=$(jq -r --arg domain "$domain_id" '
        .nodes[] | select(.id != $domain and (.id | startswith($domain + ".")))
        | .id
    ' "$NODES_FILE")

    echo ""
    echo "# ==================== INTERNAL NODES ===================="

    # Build internal container
    local quoted_domain_name
    quoted_domain_name=$(quote_label "$domain_name")
    echo "${safe_domain_id}_internal: \"${domain_name} — Internal Structure\" {"

    while IFS= read -r child_id; do
        [[ -z "$child_id" ]] && continue
        local safe_child
        safe_child=$(sanitize_id "$child_id")
        local child_name
        child_name=$(get_name "$child_id")
        local quoted_name
        quoted_name=$(quote_label "$child_name")
        echo "  ${safe_child}: ${quoted_name}"
    done <<< "$children"

    echo "}"

    echo ""
    echo "# ==================== DOMAIN NODE ===================="
    local quoted_dname
    quoted_dname=$(quote_label "$domain_name")
    echo "${safe_domain_id}: ${quoted_dname}"

    # Extract relevant edges into a temp file (edges touching this domain or its children)
    local temp_edges
    temp_edges=$(mktemp)
    jq --arg domain "$domain_id" '
        [.edges[] |
            select(
                (.from == $domain) or (.to == $domain) or
                (.from | startswith($domain + ".")) or
                (.to | startswith($domain + "."))
            )
        ]
    ' "$EDGES_FILE" > "$temp_edges"

    # External node IDs: endpoints not in this domain's subtree
    local external_ids
    external_ids=$(jq -r --arg domain "$domain_id" '
        [.[].from, .[].to] | unique | .[]
        | select((. != $domain) and ((. | startswith($domain + ".")) | not))
    ' "$temp_edges")

    echo ""
    echo "# ==================== EXTERNAL DEPENDENCIES ===================="

    while IFS= read -r ext_id; do
        [[ -z "$ext_id" ]] && continue
        local safe_ext
        safe_ext=$(sanitize_id "$ext_id")
        local ext_name
        ext_name=$(get_name "$ext_id")
        local quoted_name
        quoted_name=$(quote_label "$ext_name")
        echo "${safe_ext}: ${quoted_name} {"
        echo "  shape: rectangle"
        echo "}"
    done <<< "$external_ids"

    echo ""
    echo "# ==================== EDGES ===================="

    # Internal edges — typed
    jq -r --arg domain "$domain_id" '
        .[] |
        select(
            ((.from == $domain) or (.from | startswith($domain + "."))) and
            ((.to == $domain) or (.to | startswith($domain + ".")))
        ) |
        "\(.from)|\(.to)|\(.type)"
    ' "$temp_edges" | while IFS='|' read -r from to etype; do
        local safe_from safe_to
        safe_from=$(sanitize_id "$from")
        safe_to=$(sanitize_id "$to")
        local edge_class="material-edge"
        if [[ "$etype" == "tool" ]]; then
            edge_class="tool-edge"
        fi
        echo "${safe_from} -> ${safe_to}: { class: ${edge_class} }"
    done

    # External edges — typed
    jq -r --arg domain "$domain_id" '
        .[] |
        select(
            (((.from == $domain) or (.from | startswith($domain + "."))) and
             (.to != $domain) and ((.to | startswith($domain + ".")) | not))
            or
            (((.to == $domain) or (.to | startswith($domain + "."))) and
             (.from != $domain) and ((.from | startswith($domain + ".")) | not))
        ) |
        "\(.from)|\(.to)|\(.type)"
    ' "$temp_edges" | while IFS='|' read -r from to etype; do
        local safe_from safe_to
        safe_from=$(sanitize_id "$from")
        safe_to=$(sanitize_id "$to")
        local edge_class="material-edge"
        if [[ "$etype" == "tool" ]]; then
            edge_class="tool-edge"
        fi
        echo "${safe_from} -> ${safe_to}: { class: ${edge_class} }"
    done

    rm -f "$temp_edges"

    # --- Styling ---
    echo ""
    echo "# ==================== STYLING ===================="

    echo "${safe_domain_id}.class: domain"

    while IFS= read -r child_id; do
        [[ -z "$child_id" ]] && continue
        local safe_child
        safe_child=$(sanitize_id "$child_id")
        local child_level
        child_level=$(get_level "$child_id")
        local crit early pin
        crit=$(is_critical "$child_id")
        early=$(is_early_win "$child_id")
        pin=$(is_pinnacle "$child_id")
        if [[ "$pin" == "true" ]]; then
            echo "${safe_child}.class: pinnacle"
        elif [[ "$early" == "true" ]]; then
            echo "${safe_child}.class: earlyWin"
        elif [[ "$crit" == "true" ]]; then
            echo "${safe_child}.class: critical"
        elif [[ "$child_level" == "process" ]]; then
            echo "${safe_child}.class: process"
        else
            echo "${safe_child}.class: capability"
        fi
    done <<< "$children"

    while IFS= read -r ext_id; do
        [[ -z "$ext_id" ]] && continue
        local safe_ext
        safe_ext=$(sanitize_id "$ext_id")
        echo "${safe_ext}.class: external"
    done <<< "$external_ids"

    echo ""
    echo "# ==================== LEGEND ===================="
    cat <<'LEGEND'
d2-legend: "Edge Types" {
  class: legend
  mat: "Solid arrow = material prerequisite (physical input consumed)" {
    style: {
      stroke: "#333333"
      stroke-width: 2
    }
  }
  tool: "Dashed arrow = tool prerequisite (equipment/infrastructure needed)" {
    style: {
      stroke: "#666666"
      stroke-dash: 3
    }
  }
}
LEGEND
}

# --- Main ---

LIST_ONLY=false
if [[ "${1:-}" == "--list" ]]; then
    LIST_ONLY=true
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Determine what to generate
domain_ids=$(jq -r '.nodes[] | select(.level == "domain") | .id' "$NODES_FILE")

# List mode
if $LIST_ONLY; then
    echo "Diagrams to generate:"
    echo "  $OUTPUT_DIR/overview.d2  (all domain-level nodes with dependency edges)"
    while IFS= read -r did; do
        safe_id=$(sanitize_id "$did")
        echo "  $OUTPUT_DIR/${safe_id}.d2  (domain: $(get_name "$did"))"
    done <<< "$domain_ids"
    exit 0
fi

echo "Generating D2 diagrams..."
echo "  Data: $DATA_DIR"
echo "  Output: $OUTPUT_DIR"
echo

# Generate overview
echo "  Generating overview.d2..."
generate_overview > "$OUTPUT_DIR/overview.d2"

# Generate per-domain diagrams
while IFS= read -r did; do
    safe_id=$(sanitize_id "$did")
    dname=$(get_name "$did")
    echo "  Generating ${safe_id}.d2  ($dname)..."
    generate_domain_diagram "$did" > "$OUTPUT_DIR/${safe_id}.d2"
done <<< "$domain_ids"

echo
echo "Done. Generated 1 overview + $(echo "$domain_ids" | wc -l) domain diagrams."
echo "Output in: $OUTPUT_DIR"
