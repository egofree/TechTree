#!/usr/bin/env python3
"""Verify zero data loss from JSON-LD migration.

Compares original data/nodes.json + data/edges.json against migrated
data/entities/**/*.jsonld, data/entities/_edges/*.jsonld, and
data/products/*.jsonld.  Uses only stdlib (json, os, glob).

Exit 0 only if every field is accounted for.
"""

import json
import os
import sys
from collections import Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")


# ── helpers ──────────────────────────────────────────────────────────

def _node_path(node_id: str) -> str:
    """Map node ID to entity file path.

    foundations              -> data/entities/foundations/foundations.jsonld
    foundations.fire         -> data/entities/foundations/fire.jsonld
    machine-tools.joining.tig-welding -> data/entities/machine-tools/joining.tig-welding.jsonld
    """
    parts = node_id.split(".", 1)
    domain = parts[0]
    rest = parts[1] if len(parts) > 1 else domain
    return os.path.join(DATA, "entities", domain, f"{rest}.jsonld")


def _edge_filename(edge: dict) -> str:
    """Map edge to expected filename (dots→hyphens, optional @flow suffix)."""
    from_d = edge["from"].replace(".", "-")
    to_d = edge["to"].replace(".", "-")
    base = f"{from_d}__{to_d}"
    # Collision edges get @flow suffix
    return f"{base}@{edge['flow']}.jsonld"


def _edge_fallback_filename(edge: dict) -> str:
    """Non-collision filename (no @flow suffix)."""
    from_d = edge["from"].replace(".", "-")
    to_d = edge["to"].replace(".", "-")
    return f"{from_d}__{to_d}.jsonld"


# ── node fidelity ────────────────────────────────────────────────────

FIELDS_TO_CHECK = [
    "id", "name", "level", "parent", "description",
    "timeline", "outputs", "critical", "early_win", "pinnacle",
]

OPTIONAL_NOTE_FIELDS = [
    "critical_note", "early_win_note", "pinnacle_note", "taxonomy",
]

OBJECT_FIELDS = {"tags"}  # compared recursively


def verify_node(src: dict, migrated: dict) -> list[str]:
    """Return list of mismatches for a single node."""
    issues = []

    for field in FIELDS_TO_CHECK:
        sv = src.get(field)
        mv = migrated.get(field)
        if sv != mv:
            issues.append(f"  {field}: src={sv!r} migrated={mv!r}")

    # tags — deep comparison
    src_tags = src.get("tags", {})
    mig_tags = migrated.get("tags", {})
    if src_tags != mig_tags:
        issues.append(f"  tags: src={src_tags!r} migrated={mig_tags!r}")

    # Optional fields — only flag if present in source but missing/different in migrated
    for field in OPTIONAL_NOTE_FIELDS:
        if field in src:
            sv = src[field]
            mv = migrated.get(field)
            if sv != mv:
                issues.append(f"  {field}: src={sv!r} migrated={mv!r}")

    return issues


def check_nodes(nodes: list[dict]) -> tuple[int, int, list[str]]:
    """Verify all nodes. Returns (ok_count, total, issues)."""
    total = len(nodes)
    ok = 0
    issues = []

    for node in nodes:
        nid = node["id"]
        path = _node_path(nid)

        if not os.path.exists(path):
            issues.append(f"NODE MISSING FILE: {nid} -> {path}")
            continue

        with open(path) as f:
            migrated = json.load(f)

        node_issues = verify_node(node, migrated)
        if node_issues:
            issues.append(f"NODE {nid}:")
            issues.extend(node_issues)
        else:
            ok += 1

    return ok, total, issues


# ── edge fidelity ────────────────────────────────────────────────────

EDGE_FIELDS = ["from", "to", "flow"]
EDGE_RENAMED = {"type": "edgeType"}  # src key -> migrated key
EDGE_OPTIONAL = ["label"]


def check_edges(edges: list[dict]) -> tuple[int, int, list[str]]:
    """Verify all edges. Returns (ok_count, total, issues)."""
    total = len(edges)
    ok = 0
    issues = []
    edges_dir = os.path.join(DATA, "entities", "_edges")

    # Build lookup of available edge files
    available = set(os.listdir(edges_dir))

    for edge in edges:
        # Try collision filename first, then fallback
        fname_col = _edge_filename(edge)
        fname_plain = _edge_fallback_filename(edge)

        if fname_col in available:
            path = os.path.join(edges_dir, fname_col)
        elif fname_plain in available:
            path = os.path.join(edges_dir, fname_plain)
        else:
            issues.append(
                f"EDGE MISSING FILE: {edge['from']} -> {edge['to']} "
                f"(tried {fname_col} and {fname_plain})"
            )
            continue

        with open(path) as f:
            migrated = json.load(f)

        edge_issues = []

        for field in EDGE_FIELDS:
            sv = edge.get(field)
            mv = migrated.get(field)
            if sv != mv:
                edge_issues.append(
                    f"  {field}: src={sv!r} migrated={mv!r}"
                )

        # Renamed fields: type -> edgeType
        for src_key, mig_key in EDGE_RENAMED.items():
            sv = edge.get(src_key)
            mv = migrated.get(mig_key)
            if sv != mv:
                edge_issues.append(
                    f"  {src_key}->{mig_key}: src={sv!r} migrated={mv!r}"
                )

        # Optional fields
        for field in EDGE_OPTIONAL:
            if field in edge:
                sv = edge[field]
                mv = migrated.get(field)
                if sv != mv:
                    edge_issues.append(
                        f"  {field}: src={sv!r} migrated={mv!r}"
                    )

        if edge_issues:
            issues.append(
                f"EDGE {edge['from']} -> {edge['to']}:"
            )
            issues.extend(edge_issues)
        else:
            ok += 1

    return ok, total, issues


# ── product fidelity ─────────────────────────────────────────────────

def check_products(nodes: list[dict]) -> tuple[int, int, list[str]]:
    """Collect all unique output tokens and verify product files exist."""
    # Collect tokens -> source node mapping
    token_sources: dict[str, list[str]] = {}
    for node in nodes:
        for token in node.get("outputs", []):
            token_sources.setdefault(token, []).append(node["id"])

    total = len(token_sources)
    ok = 0
    issues = []
    products_dir = os.path.join(DATA, "products")

    for token, sources in sorted(token_sources.items()):
        path = os.path.join(products_dir, f"{token}.jsonld")

        if not os.path.exists(path):
            issues.append(f"PRODUCT MISSING FILE: {token}")
            continue

        with open(path) as f:
            migrated = json.load(f)

        prod_issues = []

        # @id must equal the token
        at_id = migrated.get("@id")
        if at_id != token:
            prod_issues.append(f"  @id: expected={token!r} got={at_id!r}")

        # source must reference a valid node
        source = migrated.get("source")
        if source not in sources:
            prod_issues.append(
                f"  source: {source!r} not in expected sources {sources}"
            )

        if prod_issues:
            issues.append(f"PRODUCT {token}:")
            issues.extend(prod_issues)
        else:
            ok += 1

    return ok, total, issues


# ── main ─────────────────────────────────────────────────────────────

def main() -> int:
    # Load source data
    with open(os.path.join(DATA, "nodes.json")) as f:
        nodes_data = json.load(f)
    nodes = nodes_data["nodes"]

    with open(os.path.join(DATA, "edges.json")) as f:
        edges_data = json.load(f)
    edges = edges_data["edges"]

    all_issues: list[str] = []

    n_ok, n_total, n_issues = check_nodes(nodes)
    all_issues.extend(n_issues)

    e_ok, e_total, e_issues = check_edges(edges)
    all_issues.extend(e_issues)

    p_ok, p_total, p_issues = check_products(nodes)
    all_issues.extend(p_issues)

    # Report
    print("=== Data Fidelity Verification ===")

    n_sym = "✓" if n_ok == n_total else "✗"
    e_sym = "✓" if e_ok == e_total else "✗"
    p_sym = "✓" if p_ok == p_total else "✗"

    print(f"Nodes: {n_ok}/{n_total} {n_sym}")
    print(f"Edges: {e_ok}/{e_total} {e_sym}")
    print(f"Products: {p_ok}/{p_total} {p_sym}")
    print(f"Missing fields: {len(all_issues)}")

    if all_issues:
        print()
        for line in all_issues:
            print(line)

    if n_ok == n_total and e_ok == e_total and p_ok == p_total:
        print("Result: ALL PASS")
        return 0
    else:
        print("Result: FAIL")
        return 1


if __name__ == "__main__":
    sys.exit(main())
