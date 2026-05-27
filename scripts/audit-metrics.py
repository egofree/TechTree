#!/usr/bin/env python3
"""Compute dependency graph health metrics for the tech-tree-bootstrap project.

Reads data/nodes.json and data/edges.json from the current working directory.
Run from tech-tree-bootstrap/ root.
"""

import json
from collections import defaultdict


def load_data():
    with open("data/nodes.json") as f:
        nodes = json.load(f)["nodes"]
    with open("data/edges.json") as f:
        edges = json.load(f)["edges"]
    return nodes, edges


def get_domain(node_id):
    return node_id.split(".")[0]


def main():
    nodes, edges = load_data()

    node_ids = {n["id"] for n in nodes}
    node_by_id = {n["id"]: n for n in nodes}

    # --- 1. Total nodes and edges ---
    total_nodes = len(nodes)
    total_edges = len(edges)

    # Sets of all node IDs appearing in edges
    from_ids = {e["from"] for e in edges}
    to_ids = {e["to"] for e in edges}
    all_edge_ids = from_ids | to_ids

    # --- 2. Orphans: nodes in zero edges (neither from nor to) ---
    orphans = node_ids - all_edge_ids
    orphan_count = len(orphans)

    # --- 3. Zero-incoming: nodes that appear in no edge's `from` field ---
    # (no dependencies listed = nothing the node depends on)
    zero_incoming = node_ids - from_ids
    zero_incoming_count = len(zero_incoming)

    # --- 4. Zero-outgoing: nodes that appear in no edge's `to` field ---
    # (nothing depends on them)
    zero_outgoing = node_ids - to_ids
    zero_outgoing_count = len(zero_outgoing)

    # --- 5. Edge density ---
    edge_density = total_edges / total_nodes if total_nodes else 0

    # --- 6 & 7. Empty tags on non-domain nodes ---
    non_domain_nodes = [n for n in nodes if n.get("level") != "domain"]
    empty_material = sum(
        1 for n in non_domain_nodes
        if not n.get("tags", {}).get("material")
    )
    empty_capability = sum(
        1 for n in non_domain_nodes
        if not n.get("tags", {}).get("capability")
    )

    # --- 8. Disconnected domains ---
    # A domain is disconnected if NO edge has a node from another domain
    # targeting it as `to` (i.e., no external node depends on any node in that domain)
    domains = set()
    for n in nodes:
        domains.add(get_domain(n["id"]))

    # For each domain, collect nodes belonging to it
    domain_nodes = defaultdict(set)
    for n in nodes:
        domain_nodes[get_domain(n["id"])].add(n["id"])

    # incoming_edges_to_domain: edges where `to` is in the domain
    # outgoing_edges_from_domain: edges where `from` is in the domain
    domain_incoming = defaultdict(list)
    domain_outgoing = defaultdict(list)
    for e in edges:
        d_from = get_domain(e["from"])
        d_to = get_domain(e["to"])
        if d_from != d_to:
            domain_incoming[d_to].append(e)
            domain_outgoing[d_from].append(e)

    disconnected_domains = []
    for d in sorted(domains):
        if not domain_incoming[d]:
            disconnected_domains.append(d)

    disconnected_count = len(disconnected_domains)

    # --- 9. Per-domain breakdown ---
    # Count nodes, incoming cross-domain edges, outgoing cross-domain edges per domain
    domain_node_count = defaultdict(int)
    for n in nodes:
        domain_node_count[get_domain(n["id"])] += 1

    # Also count total incoming/outgoing (including intra-domain)
    domain_total_incoming = defaultdict(int)
    domain_total_outgoing = defaultdict(int)
    for e in edges:
        domain_total_outgoing[get_domain(e["from"])] += 1
        domain_total_incoming[get_domain(e["to"])] += 1

    # --- Print results ---
    print("=" * 60)
    print("TECH-TREE DEPENDENCY GRAPH HEALTH METRICS")
    print("=" * 60)
    print()
    print("--- SUMMARY ---")
    print(f"Total nodes:            {total_nodes}")
    print(f"Total edges:            {total_edges}")
    print(f"Orphan nodes:           {orphan_count}  (zero edges in either direction)")
    print(f"Zero-incoming nodes:    {zero_incoming_count}  (appear in no edge's 'from')")
    print(f"Zero-outgoing nodes:    {zero_outgoing_count}  (appear in no edge's 'to')")
    print(f"Edge density:           {edge_density:.2f}  (edges / nodes)")
    print(f"Empty material[] tags:  {empty_material}  (non-domain nodes)")
    print(f"Empty capability[] tags:{empty_capability}  (non-domain nodes)")
    print(f"Disconnected domains:   {disconnected_count}  (no cross-domain incoming edges)")
    print()

    print("--- DISCONNECTED DOMAINS ---")
    for d in disconnected_domains:
        print(f"  {d} ({domain_node_count[d]} nodes)")
    print()

    print("--- PER-DOMAIN BREAKDOWN ---")
    print(f"{'Domain':<25} {'Nodes':>5} {'EdgesOut':>8} {'EdgesIn':>7} {'CrossIn':>7} {'CrossOut':>8}")
    print("-" * 65)
    for d in sorted(domains):
        nc = domain_node_count[d]
        eo = domain_total_outgoing[d]
        ei = domain_total_incoming[d]
        ci = len(domain_incoming[d])
        co = len(domain_outgoing[d])
        print(f"{d:<25} {nc:>5} {eo:>8} {ei:>7} {ci:>7} {co:>8}")

    print()

    # --- Orphan node details ---
    if orphans:
        print("--- ORPHAN NODES (no edges) ---")
        for oid in sorted(orphans):
            n = node_by_id.get(oid)
            level = n.get("level", "?") if n else "?"
            print(f"  {oid}  (level: {level})")
        print()


if __name__ == "__main__":
    main()
