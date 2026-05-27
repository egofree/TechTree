#!/usr/bin/env python3
"""Unified diagram generator for TechTree data.

Replaces generate-diagrams.sh (Mermaid) and generate-d2-diagrams.sh (D2).
Uses tt_data.py for data access instead of jq against nodes.json/edges.json.

Usage:
    python3 scripts/generate-diagrams.py --format mermaid
    python3 scripts/generate-diagrams.py --format d2
    python3 scripts/generate-diagrams.py --format both   # default
"""

import argparse
import os
import sys

# ---------------------------------------------------------------------------
# Path setup — add lib/ so tt_data is importable
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_DIR = os.path.join(SCRIPT_DIR, "lib")
sys.path.insert(0, LIB_DIR)

from tt_data import (  # noqa: E402
    EDGES_DIR,
    _load_json,
    get_nodes_by_domain,
    load_all_entities,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
MERMAID_DIR = os.path.join(PROJECT_DIR, "diagrams", "mermaid")
D2_DIR = os.path.join(PROJECT_DIR, "diagrams", "d2")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def sanitize_id(node_id):
    """Replace dots with underscores for Mermaid/D2 node IDs."""
    return node_id.replace(".", "_")


def quote_d2_label(label):
    """Quote a D2 label if it contains special characters (& , ( ))."""
    if any(c in label for c in ("&", ",", "(", ")")):
        return '"{}"'.format(label)
    return label


def get_domain(entity_id):
    """Extract domain (first dotted segment) from entity ID."""
    return entity_id.split(".")[0]


def is_domain_level(entity_id):
    """True if entity_id has no dots (is a domain-level node)."""
    return "." not in entity_id


def in_subtree(entity_id, domain_id):
    """True if entity_id belongs to domain_id's subtree (or is the domain)."""
    return entity_id == domain_id or entity_id.startswith(domain_id + ".")


def load_all_edges():
    """Load every edge file from data/entities/_edges/."""
    edges = []
    if not os.path.isdir(EDGES_DIR):
        return edges
    for filename in sorted(os.listdir(EDGES_DIR)):
        if not filename.endswith(".jsonld"):
            continue
        edge = _load_json(os.path.join(EDGES_DIR, filename))
        if edge is not None:
            edges.append(edge)
    return edges


# ---------------------------------------------------------------------------
# Data container
# ---------------------------------------------------------------------------


def load_data():
    """Load all data needed for diagram generation.

    Returns (entity_map, domain_ids, all_edges) where:
      entity_map  — dict mapping entity ID -> entity dict
      domain_ids  — list of domain IDs in sorted order
      all_edges   — list of edge dicts sorted by filename
    """
    all_entities = load_all_entities()
    entity_map = {e["id"]: e for e in all_entities}

    domain_ids = sorted(
        e["id"] for e in all_entities if e.get("level") == "domain"
    )
    all_edges = load_all_edges()

    return entity_map, domain_ids, all_edges


# ---------------------------------------------------------------------------
# Shared styling helpers
# ---------------------------------------------------------------------------


def node_class(entity):
    """Determine the display class for a child entity.

    Priority: pinnacle > early_win > critical > (level-based).
    """
    if entity.get("pinnacle"):
        return "pinnacle"
    if entity.get("early_win"):
        return "earlyWin"
    if entity.get("critical"):
        return "critical"
    if entity.get("level") == "process":
        return "process"
    return "capability"


def domain_class(entity):
    """Determine the display class for a domain entity (no fallback)."""
    if entity.get("pinnacle"):
        return "pinnacle"
    if entity.get("early_win"):
        return "earlyWin"
    if entity.get("critical"):
        return "critical"
    return None


# ---------------------------------------------------------------------------
# Mermaid generation
# ---------------------------------------------------------------------------

MERMAID_INIT = '%%{init: {"flowchart": {"defaultRenderer": "elk", "htmlLabels": true}}}%%'

MERMAID_OVERVIEW_CLASSDEFS = """\
    classDef domain fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef critical fill:#fff3e0,stroke:#f57c00,stroke-width:3px
    classDef earlyWin fill:#e8f5e9,stroke:#388e3c,stroke-width:3px
    classDef pinnacle fill:#fce4ec,stroke:#c62828,stroke-width:3px"""

MERMAID_DOMAIN_CLASSDEFS = """\
    classDef domain fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef capability fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    classDef process fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef critical fill:#fff3e0,stroke:#f57c00,stroke-width:3px
    classDef earlyWin fill:#e8f5e9,stroke:#388e3c,stroke-width:3px
    classDef pinnacle fill:#fce4ec,stroke:#c62828,stroke-width:3px
    classDef external fill:#f5f5f5,stroke:#9e9e9e,stroke-width:1px
    classDef legend fill:#fafafa,stroke:#bdbdbd,stroke-width:1px"""


def mermaid_overview(entity_map, domain_ids, all_edges):
    """Generate the overview Mermaid diagram."""
    lines = [MERMAID_INIT, "graph TD"]

    # --- Domain nodes ---
    lines.append("    %% ==================== DOMAIN NODES ====================")
    for did in domain_ids:
        safe = sanitize_id(did)
        name = entity_map[did]["name"]
        lines.append('    {}["{}"]'.format(safe, name))

    # --- Domain-level edges ---
    lines.append("")
    lines.append("    %% ==================== DOMAIN-LEVEL EDGES ====================")
    domain_edge_pairs = set()
    for edge in all_edges:
        f, t = edge["from"], edge["to"]
        if is_domain_level(f) and is_domain_level(t):
            domain_edge_pairs.add((f, t))
            arrow = "-.->" if edge.get("edgeType") == "tool" else "-->"
            lines.append("    {} {} {}".format(sanitize_id(f), arrow, sanitize_id(t)))

    # --- Cross-domain edges ---
    lines.append("")
    lines.append("    %% ==================== CROSS-DOMAIN EDGES ====================")
    cross_pairs = set()
    for edge in all_edges:
        f, t = edge["from"], edge["to"]
        fd, td = get_domain(f), get_domain(t)
        if fd != td and (not is_domain_level(f) or not is_domain_level(t)):
            cross_pairs.add((fd, td))
    for fd, td in sorted(cross_pairs):
        if (fd, td) not in domain_edge_pairs:
            lines.append("    {} -.-> {}".format(sanitize_id(fd), sanitize_id(td)))

    # --- Styling ---
    lines.append("")
    lines.append("    %% ==================== STYLING ====================")
    lines.append(MERMAID_OVERVIEW_CLASSDEFS)
    for did in domain_ids:
        cls = domain_class(entity_map[did])
        if cls:
            lines.append("    class {} {}".format(sanitize_id(did), cls))

    # --- Legend ---
    lines.append("")
    lines.append("    %% ==================== LEGEND ====================")
    lines.append('    Legend["Legend and Key Insights"]')
    lines.append(
        '    Legend --> Note0["\u2500\u2500\u25b6 Solid arrows = material '
        'prerequisites (physical inputs consumed)"]'
    )
    lines.append(
        '    Legend --> Note0b["- - \u25b6 Dashed arrows = tool '
        'prerequisites (equipment/infrastructure needed)"]'
    )
    lines.append(
        '    Legend --> Note1["Machine Tools is the master enabler: '
        "every later stage depends on precision parts\"]"
    )
    lines.append(
        '    Legend --> Note2["Iteration is everywhere: tools make '
        'better tools, crude silicon enables purer silicon"]'
    )
    lines.append(
        '    Legend --> Note3["Solar cells create a critical power '
        "feedback loop \u2014 the most important positive feedback "
        'in the tree"]'
    )
    lines.append(
        '    Legend --> Note4["High-end GPUs are the long-term pinnacle: '
        'requires the entire mature ecosystem + generations of refinement"]'
    )
    lines.append(
        '    Legend --> Note5["Realistic timeline: basic solar cells in '
        'decades. Full GPU capability: 50 to 200+ years"]'
    )
    lines.append(
        "    class Legend,Note0,Note0b,Note1,Note2,Note3,Note4,Note5 domain"
    )

    return "\n".join(lines) + "\n"


def mermaid_domain(entity_map, domain_id, all_edges):
    """Generate a per-domain Mermaid diagram."""
    domain_entity = entity_map[domain_id]
    domain_name = domain_entity["name"]
    safe_domain = sanitize_id(domain_id)

    lines = [MERMAID_INIT, "graph TD"]
    lines.append("    %% Domain: {}".format(domain_name))
    lines.append("")

    # --- Internal nodes ---
    children = [
        e for e in get_nodes_by_domain(domain_id) if e["id"] != domain_id
    ]
    lines.append("    %% ==================== INTERNAL NODES ====================")
    lines.append(
        '    subgraph {}_internal ["{} \u2014 Internal Structure"]'.format(
            safe_domain, domain_name
        )
    )
    lines.append("        direction TB")
    for child in children:
        safe = sanitize_id(child["id"])
        lines.append('        {}["{}"]'.format(safe, child["name"]))
    lines.append("    end")

    # --- Domain node ---
    lines.append("")
    lines.append("    %% ==================== DOMAIN NODE ====================")
    lines.append('    {}["{}"]'.format(safe_domain, domain_name))

    # --- Collect edges touching this domain ---
    domain_edges = [
        e
        for e in all_edges
        if in_subtree(e["from"], domain_id) or in_subtree(e["to"], domain_id)
    ]

    # --- External dependencies ---
    ext_ids = sorted(
        {
            eid
            for edge in domain_edges
            for eid in (edge["from"], edge["to"])
            if not in_subtree(eid, domain_id)
        }
    )

    lines.append("")
    lines.append(
        "    %% ==================== EXTERNAL DEPENDENCIES ===================="
    )
    for ext_id in ext_ids:
        safe = sanitize_id(ext_id)
        ext_name = entity_map[ext_id]["name"]
        lines.append('    {}("{}")'.format(safe, ext_name))

    # --- Edges ---
    lines.append("")
    lines.append("    %% ==================== EDGES ====================")

    # Internal edges
    for edge in domain_edges:
        f, t = edge["from"], edge["to"]
        if in_subtree(f, domain_id) and in_subtree(t, domain_id):
            arrow = "-.->" if edge.get("edgeType") == "tool" else "-->"
            lines.append(
                "    {} {} {}".format(sanitize_id(f), arrow, sanitize_id(t))
            )

    # External edges
    for edge in domain_edges:
        f, t = edge["from"], edge["to"]
        f_in = in_subtree(f, domain_id)
        t_in = in_subtree(t, domain_id)
        if f_in != t_in:  # exactly one endpoint is internal
            arrow = "-.->" if edge.get("edgeType") == "tool" else "-->"
            lines.append(
                "    {} {} {}".format(sanitize_id(f), arrow, sanitize_id(t))
            )

    # --- Edge type legend ---
    lines.append("")
    lines.append("    %% ==================== EDGE TYPE LEGEND ====================")
    lines.append('    EdgeLegend["Edge Types"]')
    lines.append(
        '    EdgeLegend --> MatNote["\u2500\u2500\u25b6 Solid = material '
        'prerequisite (physical input consumed)"]'
    )
    lines.append(
        '    EdgeLegend --> ToolNote["- - \u25b6 Dashed = tool '
        'prerequisite (equipment/infrastructure needed)"]'
    )

    # --- Styling ---
    lines.append("")
    lines.append("    %% ==================== STYLING ====================")
    lines.append(MERMAID_DOMAIN_CLASSDEFS)
    lines.append("    class {} domain".format(safe_domain))

    for child in children:
        safe = sanitize_id(child["id"])
        cls = node_class(child)
        lines.append("    class {} {}".format(safe, cls))

    for ext_id in ext_ids:
        lines.append("    class {} external".format(sanitize_id(ext_id)))

    lines.append("    class EdgeLegend,MatNote,ToolNote legend")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# D2 generation
# ---------------------------------------------------------------------------

D2_HEADER = """\
vars: {
  d2-config: {
    layout-engine: elk
    pad: 20
    center: true
  }
}

direction: down"""

D2_CLASSES = """\
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
}"""

D2_OVERVIEW_LEGEND = """\
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
  note3: "Solar cells create a critical power feedback loop \u2014 the most important positive feedback in the tree"
  note4: "High-end GPUs are the long-term pinnacle: requires the entire mature ecosystem + generations of refinement"
  note5: "Realistic timeline: basic solar cells in decades. Full GPU capability: 50 to 200+ years"
}"""

D2_DOMAIN_LEGEND = """\
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
}"""


def d2_overview(entity_map, domain_ids, all_edges):
    """Generate the overview D2 diagram."""
    lines = [D2_HEADER, "", D2_CLASSES]

    # --- Domain nodes ---
    lines.append("")
    lines.append("# ==================== DOMAIN NODES ====================")
    for did in domain_ids:
        safe = sanitize_id(did)
        name = quote_d2_label(entity_map[did]["name"])
        lines.append("{}: {}".format(safe, name))

    # --- Domain-level edges ---
    lines.append("")
    lines.append("# ==================== DOMAIN-LEVEL EDGES ====================")
    domain_edge_pairs = set()
    for edge in all_edges:
        f, t = edge["from"], edge["to"]
        if is_domain_level(f) and is_domain_level(t):
            domain_edge_pairs.add((f, t))
            edge_class = (
                "tool-edge" if edge.get("edgeType") == "tool" else "material-edge"
            )
            lines.append(
                "{} -> {}: {{ class: {} }}".format(
                    sanitize_id(f), sanitize_id(t), edge_class
                )
            )

    # --- Cross-domain edges ---
    lines.append("")
    lines.append("# ==================== CROSS-DOMAIN EDGES ====================")
    cross_pairs = set()
    for edge in all_edges:
        f, t = edge["from"], edge["to"]
        fd, td = get_domain(f), get_domain(t)
        if fd != td and (not is_domain_level(f) or not is_domain_level(t)):
            cross_pairs.add((fd, td))
    for fd, td in sorted(cross_pairs):
        if (fd, td) not in domain_edge_pairs:
            lines.append(
                "{} -> {}: {{ class: tool-edge }}".format(
                    sanitize_id(fd), sanitize_id(td)
                )
            )

    # --- Styling ---
    lines.append("")
    lines.append("# ==================== STYLING ====================")
    for did in domain_ids:
        safe = sanitize_id(did)
        cls = domain_class(entity_map[did]) or "domain"
        lines.append("{}.class: {}".format(safe, cls))

    # --- Legend ---
    lines.append("")
    lines.append("# ==================== LEGEND ====================")
    lines.append(D2_OVERVIEW_LEGEND)

    return "\n".join(lines) + "\n"


def d2_domain(entity_map, domain_id, all_edges):
    """Generate a per-domain D2 diagram."""
    domain_entity = entity_map[domain_id]
    domain_name = domain_entity["name"]
    safe_domain = sanitize_id(domain_id)

    lines = [D2_HEADER, "", D2_CLASSES]

    # --- Internal nodes ---
    children = [
        e for e in get_nodes_by_domain(domain_id) if e["id"] != domain_id
    ]

    lines.append("")
    lines.append("# ==================== INTERNAL NODES ====================")
    lines.append(
        '{}_internal: "{} \u2014 Internal Structure" {{'.format(
            safe_domain, domain_name
        )
    )
    for child in children:
        safe = sanitize_id(child["id"])
        name = quote_d2_label(child["name"])
        lines.append("  {}: {}".format(safe, name))
    lines.append("}")

    # --- Domain node ---
    lines.append("")
    lines.append("# ==================== DOMAIN NODE ====================")
    lines.append(
        "{}: {}".format(safe_domain, quote_d2_label(domain_name))
    )

    # --- Collect edges touching this domain ---
    domain_edges = [
        e
        for e in all_edges
        if in_subtree(e["from"], domain_id) or in_subtree(e["to"], domain_id)
    ]

    # --- External dependencies ---
    ext_ids = sorted(
        {
            eid
            for edge in domain_edges
            for eid in (edge["from"], edge["to"])
            if not in_subtree(eid, domain_id)
        }
    )

    lines.append("")
    lines.append("# ==================== EXTERNAL DEPENDENCIES ====================")
    for ext_id in ext_ids:
        safe = sanitize_id(ext_id)
        ext_name = quote_d2_label(entity_map[ext_id]["name"])
        lines.append("{}: {} {{".format(safe, ext_name))
        lines.append("  shape: rectangle")
        lines.append("}")

    # --- Edges ---
    lines.append("")
    lines.append("# ==================== EDGES ====================")

    # Internal edges
    for edge in domain_edges:
        f, t = edge["from"], edge["to"]
        if in_subtree(f, domain_id) and in_subtree(t, domain_id):
            edge_class = (
                "tool-edge" if edge.get("edgeType") == "tool" else "material-edge"
            )
            lines.append(
                "{} -> {}: {{ class: {} }}".format(
                    sanitize_id(f), sanitize_id(t), edge_class
                )
            )

    # External edges
    for edge in domain_edges:
        f, t = edge["from"], edge["to"]
        f_in = in_subtree(f, domain_id)
        t_in = in_subtree(t, domain_id)
        if f_in != t_in:
            edge_class = (
                "tool-edge" if edge.get("edgeType") == "tool" else "material-edge"
            )
            lines.append(
                "{} -> {}: {{ class: {} }}".format(
                    sanitize_id(f), sanitize_id(t), edge_class
                )
            )

    # --- Styling ---
    lines.append("")
    lines.append("# ==================== STYLING ====================")
    lines.append("{}.class: domain".format(safe_domain))

    for child in children:
        safe = sanitize_id(child["id"])
        cls = node_class(child)
        lines.append("{}.class: {}".format(safe, cls))

    for ext_id in ext_ids:
        lines.append("{}.class: external".format(sanitize_id(ext_id)))

    # --- Legend ---
    lines.append("")
    lines.append("# ==================== LEGEND ====================")
    lines.append(D2_DOMAIN_LEGEND)

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def generate_all(entity_map, domain_ids, all_edges, fmt):
    """Generate diagrams for the requested format(s)."""
    do_mermaid = fmt in ("mermaid", "both")
    do_d2 = fmt in ("d2", "both")

    if do_mermaid:
        os.makedirs(MERMAID_DIR, exist_ok=True)
    if do_d2:
        os.makedirs(D2_DIR, exist_ok=True)

    print("Generating diagrams...")
    print("  Data: {}".format(os.path.join(PROJECT_DIR, "data")))

    # Overview
    if do_mermaid:
        print("  Generating overview.mmd...")
        path = os.path.join(MERMAID_DIR, "overview.mmd")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(mermaid_overview(entity_map, domain_ids, all_edges))

    if do_d2:
        print("  Generating overview.d2...")
        path = os.path.join(D2_DIR, "overview.d2")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(d2_overview(entity_map, domain_ids, all_edges))

    # Per-domain
    for did in domain_ids:
        safe = sanitize_id(did)
        dname = entity_map[did]["name"]

        if do_mermaid:
            print("  Generating {}.mmd  ({})...".format(safe, dname))
            path = os.path.join(MERMAID_DIR, "{}.mmd".format(safe))
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(mermaid_domain(entity_map, did, all_edges))

        if do_d2:
            print("  Generating {}.d2  ({})...".format(safe, dname))
            path = os.path.join(D2_DIR, "{}.d2".format(safe))
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(d2_domain(entity_map, did, all_edges))

    print("")
    print(
        "Done. Generated 1 overview + {} domain diagrams.".format(
            len(domain_ids)
        )
    )
    if do_mermaid:
        print("Mermaid output in: {}".format(MERMAID_DIR))
    if do_d2:
        print("D2 output in: {}".format(D2_DIR))


def main():
    parser = argparse.ArgumentParser(
        description="Generate Mermaid and/or D2 diagrams from TechTree data"
    )
    parser.add_argument(
        "--format",
        choices=["mermaid", "d2", "both"],
        default="both",
        help="Diagram format to generate (default: both)",
    )
    args = parser.parse_args()

    entity_map, domain_ids, all_edges = load_data()
    generate_all(entity_map, domain_ids, all_edges, args.format)


if __name__ == "__main__":
    main()
