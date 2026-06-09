#!/usr/bin/env python3
"""Process flow diagram generator for TechTree data.

Reads data/process-flows.json and generates Mermaid (.mmd) and D2 (.d2)
flowchart diagrams in diagrams/mermaid/ and diagrams/d2/ respectively.

Each flow becomes a separate diagram file:
  diagrams/mermaid/{domain}-process-flow-{slug}.mmd
  diagrams/d2/{domain}-process-flow-{slug}.d2

Usage:
    python3 scripts/generate-process-flows.py --format mermaid
    python3 scripts/generate-process-flows.py --format d2
    python3 scripts/generate-process-flows.py --format both   # default
"""

import argparse
import json
import os
import sys

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
LIB_DIR = os.path.join(SCRIPT_DIR, "lib")
sys.path.insert(0, LIB_DIR)

MERMAID_DIR = os.path.join(PROJECT_DIR, "diagrams", "mermaid")
D2_DIR = os.path.join(PROJECT_DIR, "diagrams", "d2")
DATA_FILE = os.path.join(PROJECT_DIR, "data", "process-flows.json")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MERMAID_INIT = '%%{init: {"flowchart": {"defaultRenderer": "elk", "htmlLabels": true}}}%%'

MAX_STEPS = 10

# Mermaid node shape syntax by step type
MERMAID_SHAPES = {
    "process": ("[", "]"),       # rectangle:   A["label"]
    "input": ("[/", "/]"),       # parallelogram: A[/"label"/]
    "output": ("[/", "/]"),      # parallelogram: A[/"label"/]
    "decision": ("{", "}"),      # diamond:      A{"label"}
}

# D2 shape names by step type
D2_SHAPES = {
    "process": "rectangle",
    "input": "parallelogram",
    "output": "parallelogram",
    "decision": "diamond",
}

# Mermaid classDef colors
MERMAID_CLASSDEFS = """\
    classDef processStep fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef inputStep fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef outputStep fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    classDef decisionStep fill:#fce4ec,stroke:#c62828,stroke-width:2px"""

# D2 classes for step types
D2_CLASSES = """\
classes: {
  processStep: {
    style: {
      fill: "#fff3e0"
      stroke: "#f57c00"
      stroke-width: 2
    }
  }
  inputStep: {
    style: {
      fill: "#e3f2fd"
      stroke: "#1976d2"
      stroke-width: 2
    }
  }
  outputStep: {
    style: {
      fill: "#e8f5e9"
      stroke: "#388e3c"
      stroke-width: 2
    }
  }
  decisionStep: {
    style: {
      fill: "#fce4ec"
      stroke: "#c62828"
      stroke-width: 2
    }
  }
  flow-edge: {
    style: {
      stroke: "#333333"
      stroke-width: 2
    }
  }
  feedback-edge: {
    style: {
      stroke: "#666666"
      stroke-dash: 3
    }
  }
}"""


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------


def load_flows():
    """Load process-flows.json and return the flows dict."""
    with open(DATA_FILE, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    schema = data.get("schema", "")
    if not schema.startswith("bootciv-process-flows"):
        print(f"WARNING: Unexpected schema version: {schema}")

    return data["flows"]


def validate_flow(flow_id, flow):
    """Validate a single flow's structure. Returns list of error strings."""
    errors = []
    steps = flow.get("steps", [])
    connections = flow.get("connections", [])

    if len(steps) > MAX_STEPS:
        errors.append(f"Flow '{flow_id}' has {len(steps)} steps (max {MAX_STEPS})")

    step_ids = {s["id"] for s in steps}

    # Check for duplicate step IDs
    if len(step_ids) != len(steps):
        errors.append(f"Flow '{flow_id}' has duplicate step IDs")

    # Validate step types
    valid_types = {"process", "input", "output", "decision"}
    for step in steps:
        if step.get("type") not in valid_types:
            errors.append(
                f"Flow '{flow_id}' step '{step['id']}' has invalid type: "
                f"'{step.get('type')}'"
            )

    # Validate connections reference valid step IDs
    for i, conn in enumerate(connections):
        if conn.get("from") not in step_ids:
            errors.append(
                f"Flow '{flow_id}' connection {i}: 'from'={conn.get('from')} "
                f"not in step IDs"
            )
        if conn.get("to") not in step_ids:
            errors.append(
                f"Flow '{flow_id}' connection {i}: 'to'={conn.get('to')} "
                f"not in step IDs"
            )

    return errors


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def is_feedback_connection(conn, steps):
    """Determine if a connection goes backwards (feedback loop).

    A feedback connection is one where the 'to' step has an earlier index
    than the 'from' step, indicating a loop back in the process.
    """
    from_id = conn["from"]
    to_id = conn["to"]
    # Simple heuristic: if target step index < source step index
    from_idx = None
    to_idx = None
    for i, step in enumerate(steps):
        if step["id"] == from_id:
            from_idx = i
        if step["id"] == to_id:
            to_idx = i
    return to_idx is not None and from_idx is not None and to_idx < from_idx


def sanitize_d2_label(label):
    """Quote a D2 label if it contains special characters."""
    if any(c in label for c in ("&", ",", "(", ")", ":", "{", "}", '"')):
        return '"{}"'.format(label.replace('"', '\\"'))
    return label


# ---------------------------------------------------------------------------
# Mermaid generation
# ---------------------------------------------------------------------------


def generate_mermaid(flow_id, flow):
    """Generate a Mermaid flowchart for a single process flow."""
    steps = flow["steps"]
    connections = flow["connections"]

    lines = [MERMAID_INIT, "graph TD"]
    lines.append(f"    %% {flow['title']}")
    lines.append("")

    # --- Nodes ---
    lines.append("    %% ==================== STEPS ====================")
    for step in steps:
        sid = step["id"]
        label = step["label"]
        stype = step["type"]
        open_br, close_br = MERMAID_SHAPES.get(stype, ("[", "]"))
        lines.append(f"    {sid}{open_br}\"{label}\"{close_br}")

    # --- Connections ---
    lines.append("")
    lines.append("    %% ==================== CONNECTIONS ====================")
    for conn in connections:
        from_id = conn["from"]
        to_id = conn["to"]
        label = conn.get("label", "")
        feedback = is_feedback_connection(conn, steps)

        arrow = "-.->" if feedback else "-->"
        if label:
            lines.append(f"    {from_id} {arrow}|{label}| {to_id}")
        else:
            lines.append(f"    {from_id} {arrow} {to_id}")

    # --- Styling ---
    lines.append("")
    lines.append("    %% ==================== STYLING ====================")
    lines.append(MERMAID_CLASSDEFS)

    # Assign classes
    for step in steps:
        cls = f"{step['type']}Step"
        lines.append(f"    class {step['id']} {cls}")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# D2 generation
# ---------------------------------------------------------------------------


def generate_d2(flow_id, flow):
    """Generate a D2 diagram for a single process flow."""
    steps = flow["steps"]
    connections = flow["connections"]

    lines = [
        "vars: {",
        "  d2-config: {",
        "    layout-engine: elk",
        "    pad: 20",
        "    center: true",
        "  }",
        "}",
        "",
        "direction: down",
        "",
        D2_CLASSES,
    ]

    # --- Nodes ---
    lines.append("")
    lines.append(f"# {flow['title']}")
    for step in steps:
        sid = step["id"]
        label = sanitize_d2_label(step["label"])
        shape = D2_SHAPES.get(step["type"], "rectangle")
        cls = f"{step['type']}Step"
        lines.append(f"{sid}: {label} {{")
        lines.append(f"  shape: {shape}")
        lines.append(f"  class: {cls}")
        lines.append("}")

    # --- Connections ---
    lines.append("")
    lines.append("# ==================== CONNECTIONS ====================")
    for conn in connections:
        from_id = conn["from"]
        to_id = conn["to"]
        label = conn.get("label", "")
        feedback = is_feedback_connection(conn, steps)
        edge_cls = "feedback-edge" if feedback else "flow-edge"

        if label:
            lines.append(
                f"{from_id} -> {to_id}: {sanitize_d2_label(label)} {{"
                f" class: {edge_cls} }}"
            )
        else:
            lines.append(f"{from_id} -> {to_id}: {{ class: {edge_cls} }}")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Generate process flow diagrams from data/process-flows.json"
    )
    parser.add_argument(
        "--format",
        choices=["mermaid", "d2", "both"],
        default="both",
        help="Diagram format to generate (default: both)",
    )
    args = parser.parse_args()

    do_mermaid = args.format in ("mermaid", "both")
    do_d2 = args.format in ("d2", "both")

    # Load and validate
    flows = load_flows()

    all_errors = []
    for fid, flow in flows.items():
        errs = validate_flow(fid, flow)
        all_errors.extend(errs)

    if all_errors:
        print("Validation errors:")
        for e in all_errors:
            print(f"  ERROR: {e}")
        sys.exit(1)

    # Create output dirs
    if do_mermaid:
        os.makedirs(MERMAID_DIR, exist_ok=True)
    if do_d2:
        os.makedirs(D2_DIR, exist_ok=True)

    print(f"Generating process flow diagrams from {DATA_FILE}")
    count = 0

    for flow_id, flow in flows.items():
        domain = flow["domain"]
        # Flow ID format: {domain}-{descriptive-slug}, where domain may contain hyphens
        # Strip the known domain prefix to get the slug
        prefix = domain + "-"
        if flow_id.startswith(prefix):
            slug = flow_id[len(prefix):]
        else:
            slug = flow_id
        base_name = f"{domain}-process-flow-{slug}"

        if do_mermaid:
            path = os.path.join(MERMAID_DIR, f"{base_name}.mmd")
            print(f"  Generating {base_name}.mmd")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(generate_mermaid(flow_id, flow))

        if do_d2:
            path = os.path.join(D2_DIR, f"{base_name}.d2")
            print(f"  Generating {base_name}.d2")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(generate_d2(flow_id, flow))

        count += 1

    fmt_list = []
    if do_mermaid:
        fmt_list.append(f"Mermaid → {MERMAID_DIR}")
    if do_d2:
        fmt_list.append(f"D2 → {D2_DIR}")

    print(f"\nDone. Generated {count} process flow diagram(s).")
    for f in fmt_list:
        print(f"  {f}")


if __name__ == "__main__":
    main()
