#!/usr/bin/env bash
# Data-driven validator for tech-tree-bootstrap
# Reads all structure from data files — no hardcoded filenames
# Checks: 15 validation passes covering data integrity, DAG, cross-refs, terminology, diagrams, tags, edge types, hierarchy

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$PROJECT_DIR/data"
DOCS_DIR="$PROJECT_DIR/docs"
DIAGRAMS_DIR="$PROJECT_DIR/diagrams/mermaid"

PASSED=0
FAILED=0
TOTAL=0

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
    fi
}

# --- Data extraction helpers ---

# All node IDs (newline-separated)
all_node_ids() {
    jq -r '.nodes[].id' "$DATA_DIR/nodes.json"
}

# Domain-level node IDs only
domain_node_ids() {
    jq -r '.nodes[] | select(.level == "domain") | .id' "$DATA_DIR/nodes.json"
}

# Non-domain node IDs
non_domain_node_ids() {
    jq -r '.nodes[] | select(.level != "domain") | .id' "$DATA_DIR/nodes.json"
}

# --- Check 1: Data files exist and are valid JSON/YAML ---

check_data_files_valid() {
    local ok=true

    # JSON files — validate with jq
    for f in nodes.json edges.json resources.json; do
        if [[ ! -f "$DATA_DIR/$f" ]]; then
            echo "" >&2
            echo "    MISSING: data/$f" >&2
            ok=false
        elif ! jq empty "$DATA_DIR/$f" 2>/dev/null; then
            echo "" >&2
            echo "    INVALID JSON: data/$f" >&2
            ok=false
        fi
    done

    # YAML file — validate with python3
    if [[ ! -f "$DATA_DIR/checklist.yaml" ]]; then
        echo "" >&2
        echo "    MISSING: data/checklist.yaml" >&2
        ok=false
    elif ! python3 -c "import yaml; yaml.safe_load(open('$DATA_DIR/checklist.yaml'))" 2>/dev/null; then
        echo "" >&2
        echo "    INVALID YAML: data/checklist.yaml" >&2
        ok=false
    fi

    $ok
}

# --- Check 2: DAG is acyclic ---

check_dag_acyclic() {
    python3 -c "
import json, sys

with open('$DATA_DIR/nodes.json') as f:
    nodes = json.load(f)['nodes']
with open('$DATA_DIR/edges.json') as f:
    edges = json.load(f)['edges']

node_ids = {n['id'] for n in nodes}
adj = {nid: [] for nid in node_ids}
for e in edges:
    adj.setdefault(e['from'], []).append(e['to'])

# DFS cycle detection with white/gray/black coloring
WHITE, GRAY, BLACK = 0, 1, 2
color = {nid: WHITE for nid in node_ids}

def dfs(node):
    color[node] = GRAY
    for neighbor in adj.get(node, []):
        if neighbor not in color:
            continue  # dangling ref — caught by check 4
        if color[neighbor] == GRAY:
            print(f'    Cycle detected involving: {node} -> {neighbor}', file=sys.stderr)
            return True
        if color[neighbor] == WHITE:
            if dfs(neighbor):
                return True
    color[node] = BLACK
    return False

for nid in node_ids:
    if color[nid] == WHITE:
        if dfs(nid):
            sys.exit(1)

sys.exit(0)
"
}

# --- Check 3: Node-doc correspondence ---

check_node_doc_correspondence() {
    local ok=true
    local tmpfile
    tmpfile=$(mktemp)
    local domains_file
    domains_file=$(mktemp)

    domain_node_ids > "$tmpfile"

    # Collect all unique domain segments from ALL node IDs
    all_node_ids | cut -d'.' -f1 | sort -u > "$domains_file"

    # 3a: Each domain node should have a docs/{domain}/ directory
    while IFS= read -r domain_id; do
        [[ -z "$domain_id" ]] && continue
        if [[ ! -d "$DOCS_DIR/$domain_id" ]]; then
            echo "    No docs dir for domain node: $domain_id (check for alias dirs)" >&2
        fi
    done < "$tmpfile"

    # 3b: Each docs subdirectory (excluding supporting) should map to a domain segment
    while IFS= read -r docdir; do
        [[ -z "$docdir" ]] && continue
        local dirname
        dirname=$(basename "$docdir")
        [[ "$dirname" == "supporting" ]] && continue
        if ! grep -qx "$dirname" "$domains_file"; then
            echo "    WARNING: docs/$dirname/ has no matching domain node (may be aliased)" >&2
        fi
    done < <(find "$DOCS_DIR" -mindepth 1 -maxdepth 1 -type d)

    # 3c: Each non-domain node must have at least one .md file in its domain directory
    while IFS= read -r node_id; do
        [[ -z "$node_id" ]] && continue
        local domain
        domain=$(echo "$node_id" | cut -d'.' -f1)
        if [[ ! -d "$DOCS_DIR/$domain" ]]; then
            echo "    No docs dir for node: $node_id (domain: $domain)" >&2
            ok=false
            continue
        fi
        local md_count
        md_count=$(find "$DOCS_DIR/$domain" -maxdepth 1 -name "*.md" -type f | wc -l)
        if [[ "$md_count" -eq 0 ]]; then
            echo "    Domain $domain has no .md files (needed by node $node_id)" >&2
            ok=false
        fi
    done < <(non_domain_node_ids)

    rm -f "$tmpfile" "$domains_file"
    $ok
}

# --- Check 4: Edge references valid ---

check_edge_references() {
    local ok=true
    local node_ids_file
    node_ids_file=$(mktemp)
    all_node_ids > "$node_ids_file"

    # Check 'from' references
    local dangling_from
    dangling_from=$(jq -r '.edges[].from' "$DATA_DIR/edges.json" | sort -u | while IFS= read -r fid; do
        if ! grep -qx "$fid" "$node_ids_file"; then
            echo "$fid"
        fi
    done)

    if [[ -n "$dangling_from" ]]; then
        echo "$dangling_from" | while IFS= read -r ref; do
            echo "    Dangling edge 'from': $ref" >&2
        done
        ok=false
    fi

    # Check 'to' references
    local dangling_to
    dangling_to=$(jq -r '.edges[].to' "$DATA_DIR/edges.json" | sort -u | while IFS= read -r tid; do
        if ! grep -qx "$tid" "$node_ids_file"; then
            echo "$tid"
        fi
    done)

    if [[ -n "$dangling_to" ]]; then
        echo "$dangling_to" | while IFS= read -r ref; do
            echo "    Dangling edge 'to': $ref" >&2
        done
        ok=false
    fi

    rm -f "$node_ids_file"
    $ok
}

# --- Check 5: Resources references valid ---

check_resource_references() {
    local ok=true
    local node_ids_file
    node_ids_file=$(mktemp)
    all_node_ids > "$node_ids_file"

    local dangling
    dangling=$(jq -r '.raw_materials[].used_in[]' "$DATA_DIR/resources.json" | sort -u | while IFS= read -r ref; do
        if ! grep -qx "$ref" "$node_ids_file"; then
            echo "$ref"
        fi
    done)

    if [[ -n "$dangling" ]]; then
        echo "$dangling" | while IFS= read -r ref; do
            echo "    Dangling resource 'used_in': $ref" >&2
        done
        ok=false
    fi

    rm -f "$node_ids_file"
    $ok
}

# --- Check 6: Checklist references valid ---

check_checklist_references() {
    local ok=true
    local node_ids_file
    node_ids_file=$(mktemp)
    all_node_ids > "$node_ids_file"

    # Extract all checklist item IDs using python3 (YAML-aware)
    local checklist_ids
    checklist_ids=$(python3 -c "
import yaml, sys

with open('$DATA_DIR/checklist.yaml') as f:
    data = yaml.safe_load(f)

# Collect all item IDs (skip _schema_docs)
for key, value in data.items():
    if key.startswith('_'):
        continue
    if isinstance(value, dict) and 'items' in value:
        for item in value['items']:
            if isinstance(item, dict) and 'id' in item:
                print(item['id'])
")

    while IFS= read -r cid; do
        [[ -z "$cid" ]] && continue
        if ! grep -qx "$cid" "$node_ids_file"; then
            echo "    Dangling checklist ref: $cid" >&2
            ok=false
        fi
    done <<< "$checklist_ids"

    rm -f "$node_ids_file"
    $ok
}

# --- Check 7: No phase/SQ terminology in data files ---

check_no_legacy_terminology() {
    local ok=true
    local patterns=("phase-[0-9]" "sq-[0-9]" "main.quest" "side.quest")

    for f in nodes.json edges.json resources.json; do
        for pat in "${patterns[@]}"; do
            # Strip _schema_docs blocks before checking
            local matches
            matches=$(jq -r 'del(._schema_docs) | .. | strings | select(test("'"$pat"'"))' "$DATA_DIR/$f" 2>/dev/null || true)
            if [[ -n "$matches" ]]; then
                echo "    Legacy term '$pat' found in data/$f" >&2
                echo "$matches" | head -3 | while IFS= read -r line; do
                    echo "      $line" >&2
                done
                ok=false
            fi
        done
    done

    # Check YAML file
    for pat in "${patterns[@]}"; do
        local yaml_matches
        yaml_matches=$(python3 -c "
import yaml, re, sys

with open('$DATA_DIR/checklist.yaml') as f:
    content = f.read()

# Remove _schema_docs block
data = yaml.safe_load(content)
# Check only the data portion by re-serializing without _schema_docs
for key in list(data.keys()):
    if key.startswith('_'):
        del data[key]

clean = yaml.dump(data)
pattern = re.compile(r'$pat')
for line in clean.splitlines():
    if pattern.search(line):
        print(line)
" 2>/dev/null || true)
        if [[ -n "$yaml_matches" ]]; then
            echo "    Legacy term '$pat' found in data/checklist.yaml" >&2
            ok=false
        fi
    done

    $ok
}

# --- Check 8: Diagrams generated ---

check_diagrams_generated() {
    local ok=true

    # Build expected diagram list from generate-diagrams.sh --list
    local expected_files
    expected_files=$(bash "$SCRIPT_DIR/generate-diagrams.sh" --list 2>/dev/null | grep -oP '\S+\.mmd' || true)

    if [[ -z "$expected_files" ]]; then
        echo "    generate-diagrams.sh --list returned no diagrams" >&2
        ok=false
    fi

    while IFS= read -r expected; do
        [[ -z "$expected" ]] && continue
        if [[ ! -f "$expected" ]]; then
            echo "    Missing diagram: $expected" >&2
            ok=false
        fi
    done <<< "$expected_files"

    $ok
}

# --- Check 9: Mermaid syntax basic check ---

check_mermaid_syntax() {
    local ok=true

    if [[ ! -d "$DIAGRAMS_DIR" ]]; then
        echo "    diagrams/mermaid/ directory not found" >&2
        return 1
    fi

    local mmd_files
    mmd_files=$(find "$DIAGRAMS_DIR" -name "*.mmd" -type f)

    if [[ -z "$mmd_files" ]]; then
        echo "    No .mmd files found in diagrams/mermaid/" >&2
        return 1
    fi

    while IFS= read -r mmd; do
        [[ -z "$mmd" ]] && continue
        local basename_f
        basename_f=$(basename "$mmd")

        # Check 9a: Starts with %%{init:
        if ! head -1 "$mmd" | grep -q '^%%{init:'; then
            echo "    $basename_f: missing %%{init: header" >&2
            ok=false
        fi

        # Check 9b: Contains 'graph TD'
        if ! grep -q 'graph TD' "$mmd"; then
            echo "    $basename_f: missing 'graph TD' directive" >&2
            ok=false
        fi

        # Check 9c: Has node declarations (lines with brackets like ["text"] or ("text"))
        local node_count
        node_count=$(grep -cE '\["[^"]+"\]|\("[^"]+"\)' "$mmd" || true)
        if [[ "$node_count" -eq 0 ]]; then
            echo "    $basename_f: no node declarations found" >&2
            ok=false
        fi

        # Check 9d: Has edges (--> or -.->)
        local edge_count
        edge_count=$(grep -cE '\-\->|-\.\->' "$mmd" || true)
        if [[ "$edge_count" -eq 0 ]]; then
            echo "    $basename_f: no edges found" >&2
            ok=false
        fi
    done <<< "$mmd_files"

    $ok
}

# --- Check 10: Tag completeness ---

check_tag_completeness() {
    local ok=true
    local violations

    # Every node must have a tags object
    violations=$(jq -r '.nodes[] | select(.tags == null or (.tags | type) != "object") | .id' "$DATA_DIR/nodes.json")
    if [[ -n "$violations" ]]; then
        echo "$violations" | while IFS= read -r nid; do
            echo "    Missing or non-object 'tags' on node: $nid" >&2
        done
        ok=false
    fi

    # Every node must have tags.material (array)
    violations=$(jq -r '.nodes[] | select(.tags.material == null or (.tags.material | type) != "array") | .id' "$DATA_DIR/nodes.json")
    if [[ -n "$violations" ]]; then
        echo "$violations" | while IFS= read -r nid; do
            echo "    Missing or non-array 'tags.material' on node: $nid" >&2
        done
        ok=false
    fi

    # Every node must have tags.era (string, non-null)
    violations=$(jq -r '.nodes[] | select(.tags.era == null or (.tags.era | type) != "string") | .id' "$DATA_DIR/nodes.json")
    if [[ -n "$violations" ]]; then
        echo "$violations" | while IFS= read -r nid; do
            echo "    Missing or non-string 'tags.era' on node: $nid" >&2
        done
        ok=false
    fi

    # Every node must have tags.critical, tags."early-win", tags.pinnacle as booleans
    local bool_fields=("critical" "early-win" "pinnacle")
    for field in "${bool_fields[@]}"; do
        violations=$(jq -r --arg f "$field" '.nodes[] | select(.tags[$f] == null or (.tags[$f] | type) != "boolean") | .id' "$DATA_DIR/nodes.json")
        if [[ -n "$violations" ]]; then
            echo "$violations" | while IFS= read -r nid; do
                echo "    Missing or non-boolean 'tags.$field' on node: $nid" >&2
            done
            ok=false
        fi
    done

    $ok
}

# --- Check 11: Tag value validity ---

check_tag_value_validity() {
    local ok=true
    local invalid

    local valid_materials='["metals","silicon","glass","ceramics","polymers","chemicals","wood","stone","clay","fibers","gases","water","biomass"]'
    local valid_capabilities='["energy","precision","computing","transport","health","measurement","cooling","vacuum","optics","construction"]'
    local valid_eras='["stone-age","copper-age","bronze-age","iron-age","industrial","electronic","semiconductor","advanced"]'

    # tags.material values must be from allowed list
    invalid=$(jq -r --argjson valid "$valid_materials" '
        .nodes[] | .id as $nid | .tags.material[] | select(. as $v | $valid | index($v) | not) | "\($nid): \(.): invalid material tag"
    ' "$DATA_DIR/nodes.json")
    if [[ -n "$invalid" ]]; then
        echo "$invalid" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    # tags.capability values must be from allowed list
    invalid=$(jq -r --argjson valid "$valid_capabilities" '
        .nodes[] | .id as $nid | .tags.capability[]? | select(. as $v | $valid | index($v) | not) | "\($nid): \(.): invalid capability tag"
    ' "$DATA_DIR/nodes.json")
    if [[ -n "$invalid" ]]; then
        echo "$invalid" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    # tags.era must be from allowed list
    invalid=$(jq -r --argjson valid "$valid_eras" '
        .nodes[] | select(.tags.era as $v | $valid | index($v) | not) | "\(.id): \(.tags.era): invalid era tag"
    ' "$DATA_DIR/nodes.json")
    if [[ -n "$invalid" ]]; then
        echo "$invalid" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    $ok
}

# --- Check 12: Edge type validity ---

check_edge_type_validity() {
    local ok=true
    local invalid

    # Every edge must have a type field
    invalid=$(jq -r '.edges[] | select(.type == null) | "\(.from) -> \(.to): missing type field"' "$DATA_DIR/edges.json")
    if [[ -n "$invalid" ]]; then
        echo "$invalid" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    # type must be "material" or "tool" (not "required" or anything else)
    invalid=$(jq -r '.edges[] | select(.type != null and .type != "material" and .type != "tool") | "\(.from) -> \(.to): invalid type " + .type' "$DATA_DIR/edges.json")
    if [[ -n "$invalid" ]]; then
        echo "$invalid" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    # Specifically flag "required" as retired
    invalid=$(jq -r '.edges[] | select(.type == "required") | "\(.from) -> \(.to): type=required is retired, use material or tool"' "$DATA_DIR/edges.json")
    if [[ -n "$invalid" ]]; then
        echo "$invalid" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    $ok
}

# --- Check 13: Parent chain consistency ---

check_parent_chain() {
    local ok=true
    local violations

    # Every non-null parent must reference an existing node ID
    violations=$(jq -r '
        (.nodes | map(.id)) as $ids |
        .nodes[] | select(.parent != null) | select(.parent as $p | $ids | index($p) | not) |
        "\(.id): parent=" + .parent + " does not exist"
    ' "$DATA_DIR/nodes.json")
    if [[ -n "$violations" ]]; then
        echo "$violations" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    # Full chain must resolve to a domain node (no orphan chains)
    violations=$(python3 -c "
import json, sys

with open('$DATA_DIR/nodes.json') as f:
    nodes = json.load(f)['nodes']

node_map = {n['id']: n for n in nodes}

for node in nodes:
    nid = node['id']
    parent = node.get('parent')
    visited = set()
    current = nid
    while current in node_map and node_map[current].get('parent') is not None:
        if current in visited:
            print(f'    {nid}: circular parent chain detected at {current}', file=sys.stderr)
            break
        visited.add(current)
        current = node_map[current]['parent']
    else:
        # Chain ended — check it ended at a domain (no parent) or dangling
        if current not in node_map:
            if current is not None:
                print(f'    {nid}: parent chain ends at non-existent node {current}', file=sys.stderr)
        elif node_map[current].get('parent') is not None:
            # This shouldn't happen if loop exited normally, but just in case
            pass
")
    if [[ -n "$violations" ]]; then
        ok=false
    fi

    $ok
}

# --- Check 14: Level-dot depth consistency ---

check_level_dot_depth() {
    local ok=true
    local invalid

    # 0 dots in ID -> level must be "domain"
    invalid=$(jq -r '.nodes[] | select((.id | split(".") | length) == 1 and .level != "domain") | "\(.id): has 0 dots but level=" + .level + " (expected domain)"' "$DATA_DIR/nodes.json")
    if [[ -n "$invalid" ]]; then
        echo "$invalid" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    # 1 dot in ID -> level must be "capability" (2 segments)
    invalid=$(jq -r '.nodes[] | select((.id | split(".") | length) == 2 and .level != "capability") | "\(.id): has 1 dot but level=" + .level + " (expected capability)"' "$DATA_DIR/nodes.json")
    if [[ -n "$invalid" ]]; then
        echo "$invalid" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    # 2+ dots in ID -> level must be "process" (3+ segments)
    invalid=$(jq -r '.nodes[] | select((.id | split(".") | length) >= 3 and .level != "process") | "\(.id): has 2+ dots but level=" + .level + " (expected process)"' "$DATA_DIR/nodes.json")
    if [[ -n "$invalid" ]]; then
        echo "$invalid" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    $ok
}

# --- Check 15: Boolean consistency (tags vs top-level) ---

check_boolean_consistency() {
    local ok=true
    local mismatches

    # tags.critical must match top-level critical
    mismatches=$(jq -r '.nodes[] | select(.tags.critical != .critical) | "\(.id): tags.critical=\(.tags.critical) but critical=\(.critical)"' "$DATA_DIR/nodes.json")
    if [[ -n "$mismatches" ]]; then
        echo "$mismatches" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    # tags."early-win" must match top-level early_win
    mismatches=$(jq -r '.nodes[] | select(.tags["early-win"] != .early_win) | "\(.id): tags.early-win=\(.tags["early-win"]) but early_win=\(.early_win)"' "$DATA_DIR/nodes.json")
    if [[ -n "$mismatches" ]]; then
        echo "$mismatches" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    # tags.pinnacle must match top-level pinnacle
    mismatches=$(jq -r '.nodes[] | select(.tags.pinnacle != .pinnacle) | "\(.id): tags.pinnacle=\(.tags.pinnacle) but pinnacle=\(.pinnacle)"' "$DATA_DIR/nodes.json")
    if [[ -n "$mismatches" ]]; then
        echo "$mismatches" | while IFS= read -r line; do
            echo "    $line" >&2
        done
        ok=false
    fi

    $ok
}

# ============================================================
# Main
# ============================================================

echo "=== Validating tech-tree-bootstrap (data-driven) ==="
echo ""

# Verify dependencies
if ! command -v jq &>/dev/null; then
    echo "ERROR: jq is required but not found in PATH" >&2
    exit 1
fi
if ! command -v python3 &>/dev/null; then
    echo "ERROR: python3 is required but not found in PATH" >&2
    exit 1
fi
python3 -c "import yaml" 2>/dev/null || {
    echo "ERROR: python3 yaml module required (pip install pyyaml)" >&2
    exit 1
}

echo "--- Data integrity ---"
check "Data files exist and are valid JSON/YAML" check_data_files_valid

echo ""
echo "--- DAG structure ---"
check "DAG is acyclic (no cycles)" check_dag_acyclic

echo ""
echo "--- Cross-references ---"
check "Node-doc correspondence" check_node_doc_correspondence
check "Edge references valid" check_edge_references
check "Resources references valid" check_resource_references
check "Checklist references valid" check_checklist_references

echo ""
echo "--- Terminology ---"
check "No phase/SQ legacy terminology" check_no_legacy_terminology

echo ""
echo "--- Diagrams ---"
check "Diagrams generated and present" check_diagrams_generated
check "Mermaid syntax valid (basic)" check_mermaid_syntax

echo ""
echo "--- Schema: Tags ---"
check "Tag completeness (tags object, material, era, booleans)" check_tag_completeness
check "Tag value validity (material, capability, era vocabularies)" check_tag_value_validity

echo ""
echo "--- Schema: Edge types ---"
check "Edge type validity (material/tool only, no 'required')" check_edge_type_validity

echo ""
echo "--- Schema: Hierarchy ---"
check "Parent chain consistency (all parents exist, chain resolves)" check_parent_chain
check "Level-dot depth consistency (0 dots=domain, 1=capability, 2+=process)" check_level_dot_depth
check "Boolean consistency (tags booleans match top-level fields)" check_boolean_consistency

echo ""
echo "=== Results: $PASSED/$TOTAL passed, $FAILED failed ==="
[ "$FAILED" -eq 0 ]
