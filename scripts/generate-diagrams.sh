#!/usr/bin/env bash
# Generate all Mermaid diagrams from data/nodes.json + data/edges.json
# Requires: jq
# Usage: ./scripts/generate-diagrams.sh [--list]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$PROJECT_DIR/data"
OUTPUT_DIR="$PROJECT_DIR/diagrams/mermaid"

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

# Sanitize a node ID for use as a Mermaid node ID (replace dots with underscores)
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

# --- Diagram generators ---

generate_overview() {
    cat <<'HEADER'
%%{init: {"flowchart": {"defaultRenderer": "elk", "htmlLabels": true}}}%%
graph TD
HEADER

    echo "    %% ==================== DOMAIN NODES ===================="

    # Collect all domain IDs
    local domain_ids
    domain_ids=$(jq -r '.nodes[] | select(.level == "domain") | .id' "$NODES_FILE")

    # Emit domain node declarations
    while IFS= read -r did; do
        local safe_id
        safe_id=$(sanitize_id "$did")
        local name
        name=$(get_name "$did")
        local domain_line="    ${safe_id}[\"${name}\"]"
        echo "$domain_line"
    done <<< "$domain_ids"

    echo ""
    echo "    %% ==================== DOMAIN-LEVEL EDGES ===================="

    # Collect edges where both from and to are domain-level nodes
    # Use edge type: material → solid (-->)  tool → dashed (-.->)
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
        local arrow="-->"
        if [[ "$etype" == "tool" ]]; then
            arrow="-.->"
        fi
        echo "    ${safe_from} ${arrow} ${safe_to}"
    done

    # Also collect edges where from is a capability/process but to is a domain,
    # or from is a domain but to is a capability/process.
    # These represent cross-domain dependencies visible at the overview level.
    # Exclude pairs that already have a direct domain-to-domain edge.
    echo ""
    echo "    %% ==================== CROSS-DOMAIN EDGES ===================="

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
            echo "    ${safe_from} -.-> ${safe_to}"
        fi
    done

    rm -f "$domain_edges_raw"

    echo ""
    echo "    %% ==================== STYLING ===================="

    # Build class assignments for domains
    local all_domain_safe_ids=""
    while IFS= read -r did; do
        local safe_id
        safe_id=$(sanitize_id "$did")
        if [[ -n "$all_domain_safe_ids" ]]; then
            all_domain_safe_ids="${all_domain_safe_ids},${safe_id}"
        else
            all_domain_safe_ids="${safe_id}"
        fi
    done <<< "$domain_ids"

    echo "    classDef domain fill:#e3f2fd,stroke:#1976d2,stroke-width:2px"
    echo "    classDef critical fill:#fff3e0,stroke:#f57c00,stroke-width:3px"
    echo "    classDef earlyWin fill:#e8f5e9,stroke:#388e3c,stroke-width:3px"
    echo "    classDef pinnacle fill:#fce4ec,stroke:#c62828,stroke-width:3px"

    # Apply critical/early_win/pinnacle styling
    while IFS= read -r did; do
        local safe_id
        safe_id=$(sanitize_id "$did")
        local crit early pin
        crit=$(is_critical "$did")
        early=$(is_early_win "$did")
        pin=$(is_pinnacle "$did")
        if [[ "$pin" == "true" ]]; then
            echo "    class ${safe_id} pinnacle"
        elif [[ "$early" == "true" ]]; then
            echo "    class ${safe_id} earlyWin"
        elif [[ "$crit" == "true" ]]; then
            echo "    class ${safe_id} critical"
        fi
    done <<< "$domain_ids"

    echo ""
    echo "    %% ==================== LEGEND ===================="
    echo "    Legend[\"Legend and Key Insights\"]"
    echo "    Legend --> Note0[\"──▶ Solid arrows = material prerequisites (physical inputs consumed)\"]"
    echo "    Legend --> Note0b[\"- - ▶ Dashed arrows = tool prerequisites (equipment/infrastructure needed)\"]"
    echo "    Legend --> Note1[\"Machine Tools is the master enabler: every later stage depends on precision parts\"]"
    echo "    Legend --> Note2[\"Iteration is everywhere: tools make better tools, crude silicon enables purer silicon\"]"
    echo "    Legend --> Note3[\"Solar cells create a critical power feedback loop — the most important positive feedback in the tree\"]"
    echo "    Legend --> Note4[\"High-end GPUs are the long-term pinnacle: requires the entire mature ecosystem + generations of refinement\"]"
    echo "    Legend --> Note5[\"Realistic timeline: basic solar cells in decades. Full GPU capability: 50 to 200+ years\"]"
    echo "    class Legend,Note0,Note0b,Note1,Note2,Note3,Note4,Note5 domain"
}

generate_domain_diagram() {
    local domain_id="$1"
    local domain_name
    domain_name=$(get_name "$domain_id")
    local safe_domain_id
    safe_domain_id=$(sanitize_id "$domain_id")

    cat <<HEADER
%%{init: {"flowchart": {"defaultRenderer": "elk", "htmlLabels": true}}}%%
graph TD
    %% Domain: ${domain_name}

HEADER

    local children
    children=$(jq -r --arg domain "$domain_id" '
        .nodes[] | select(.id != $domain and (.id | startswith($domain + ".")))
        | .id
    ' "$NODES_FILE")

    echo "    %% ==================== INTERNAL NODES ===================="
    echo "    subgraph ${safe_domain_id}_internal [\"${domain_name} — Internal Structure\"]"
    echo "        direction TB"

    while IFS= read -r child_id; do
        [[ -z "$child_id" ]] && continue
        local safe_child
        safe_child=$(sanitize_id "$child_id")
        local child_name
        child_name=$(get_name "$child_id")
        echo "        ${safe_child}[\"${child_name}\"]"
    done <<< "$children"

    echo "    end"

    echo ""
    echo "    %% ==================== DOMAIN NODE ===================="
    echo "    ${safe_domain_id}[\"${domain_name}\"]"

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
    echo "    %% ==================== EXTERNAL DEPENDENCIES ===================="

    while IFS= read -r ext_id; do
        [[ -z "$ext_id" ]] && continue
        local safe_ext
        safe_ext=$(sanitize_id "$ext_id")
        local ext_name
        ext_name=$(get_name "$ext_id")
        echo "    ${safe_ext}(\"${ext_name}\")"
    done <<< "$external_ids"

    echo ""
    echo "    %% ==================== EDGES ===================="

    # Internal edges — typed: material -->  tool -.->
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
        local arrow="-->"
        if [[ "$etype" == "tool" ]]; then
            arrow="-.->"
        fi
        echo "    ${safe_from} ${arrow} ${safe_to}"
    done

    # External edges — typed: material -->  tool -.->
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
        local arrow="-->"
        if [[ "$etype" == "tool" ]]; then
            arrow="-.->"
        fi
        echo "    ${safe_from} ${arrow} ${safe_to}"
    done

    rm -f "$temp_edges"

    echo ""
    echo "    %% ==================== EDGE TYPE LEGEND ===================="
    echo "    EdgeLegend[\"Edge Types\"]"
    echo "    EdgeLegend --> MatNote[\"──▶ Solid = material prerequisite (physical input consumed)\"]"
    echo "    EdgeLegend --> ToolNote[\"- - ▶ Dashed = tool prerequisite (equipment/infrastructure needed)\"]"

    # --- Styling ---
    echo ""
    echo "    %% ==================== STYLING ===================="
    echo "    classDef domain fill:#e3f2fd,stroke:#1976d2,stroke-width:2px"
    echo "    classDef capability fill:#e8f5e9,stroke:#388e3c,stroke-width:2px"
    echo "    classDef process fill:#fff3e0,stroke:#f57c00,stroke-width:2px"
    echo "    classDef critical fill:#fff3e0,stroke:#f57c00,stroke-width:3px"
    echo "    classDef earlyWin fill:#e8f5e9,stroke:#388e3c,stroke-width:3px"
    echo "    classDef pinnacle fill:#fce4ec,stroke:#c62828,stroke-width:3px"
    echo "    classDef external fill:#f5f5f5,stroke:#9e9e9e,stroke-width:1px"
    echo "    classDef legend fill:#fafafa,stroke:#bdbdbd,stroke-width:1px"

    echo "    class ${safe_domain_id} domain"

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
            echo "    class ${safe_child} pinnacle"
        elif [[ "$early" == "true" ]]; then
            echo "    class ${safe_child} earlyWin"
        elif [[ "$crit" == "true" ]]; then
            echo "    class ${safe_child} critical"
        elif [[ "$child_level" == "process" ]]; then
            echo "    class ${safe_child} process"
        else
            echo "    class ${safe_child} capability"
        fi
    done <<< "$children"

    while IFS= read -r ext_id; do
        [[ -z "$ext_id" ]] && continue
        local safe_ext
        safe_ext=$(sanitize_id "$ext_id")
        echo "    class ${safe_ext} external"
    done <<< "$external_ids"

    echo "    class EdgeLegend,MatNote,ToolNote legend"
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
    echo "  $OUTPUT_DIR/overview.mmd  (all domain-level nodes with dependency edges)"
    while IFS= read -r did; do
        safe_id=$(sanitize_id "$did")
        echo "  $OUTPUT_DIR/${safe_id}.mmd  (domain: $(get_name "$did"))"
    done <<< "$domain_ids"
    exit 0
fi

echo "Generating diagrams..."
echo "  Data: $DATA_DIR"
echo "  Output: $OUTPUT_DIR"
echo

# Generate overview
echo "  Generating overview.mmd..."
generate_overview > "$OUTPUT_DIR/overview.mmd"

# Generate per-domain diagrams
while IFS= read -r did; do
    safe_id=$(sanitize_id "$did")
    dname=$(get_name "$did")
    echo "  Generating ${safe_id}.mmd  ($dname)..."
    generate_domain_diagram "$did" > "$OUTPUT_DIR/${safe_id}.mmd"
done <<< "$domain_ids"

echo
echo "Done. Generated 1 overview + $(echo "$domain_ids" | wc -l) domain diagrams."
echo "Output in: $OUTPUT_DIR"
