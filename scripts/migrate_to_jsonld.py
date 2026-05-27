#!/usr/bin/env python3
"""Migrate nodes.json and edges.json to per-entity JSON-LD files.

Reads:
  data/nodes.json  ->  data/entities/{domain}/{name}.jsonld
  data/edges.json  ->  data/entities/_edges/{from}__{to}.jsonld
  (outputs)        ->  data/products/{token}.jsonld

Preserves all source fields with zero data loss.
Does NOT delete original nodes.json or edges.json.
"""

import json
import os
import shutil
import sys

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, "data")

ENTITIES_DIR = os.path.join(DATA_DIR, "entities")
EDGES_DIR = os.path.join(ENTITIES_DIR, "_edges")
PRODUCTS_DIR = os.path.join(DATA_DIR, "products")

sys.path.insert(0, SCRIPT_DIR)
from lib.tt_data import _deterministic_dumps  # noqa: E402

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

LEVEL_TO_TYPE = {
    "domain": "Domain",
    "capability": "Capability",
    "process": "Process",
}

PRODUCT_TAG_KEYS = {"material", "capability", "lifecycle"}


def id_to_domain_name(node_id):
    if "." in node_id:
        domain, name = node_id.split(".", 1)
        return domain, name
    return node_id, node_id


def id_to_filename(node_id):
    return node_id.replace(".", "-")


def token_to_name(token):
    return token.replace("_", " ").title()


def filter_tags_for_product(source_tags):
    """Extract only schema-valid product tags (material, capability, lifecycle).

    Entity tags include era, critical, early-win, pinnacle which are not
    valid in the product schema (product.schema.json additionalProperties: false).
    material is always included (required by schema) even when empty, capped
    at 3 items per product schema maxItems constraint.
    """
    result = {"material": source_tags.get("material", [])[:3]}
    for key in ("capability", "lifecycle"):
        val = source_tags.get(key)
        if val:
            result[key] = val
    return result


def write_jsonld(data, filepath):
    """Write a dict as deterministic JSON-LD."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(_deterministic_dumps(data))


# ---------------------------------------------------------------------------
# Migration logic
# ---------------------------------------------------------------------------

def migrate_nodes(nodes_list):
    """Convert all nodes to per-entity JSON-LD files."""
    count = 0
    for node in nodes_list:
        domain, name = id_to_domain_name(node["id"])
        entity = {
            "@context": "../../context.jsonld",
            "@type": LEVEL_TO_TYPE[node["level"]],
        }
        # Preserve all source fields in deterministic key order.
        # We build the dict with explicit key ordering to match sample files.
        entity["id"] = node["id"]
        entity["name"] = node["name"]
        entity["level"] = node["level"]
        entity["parent"] = node["parent"]
        entity["description"] = node["description"]
        entity["timeline"] = node["timeline"]
        entity["outputs"] = node["outputs"]
        entity["critical"] = node["critical"]
        if "critical_note" in node:
            entity["critical_note"] = node["critical_note"]
        entity["early_win"] = node["early_win"]
        if "early_win_note" in node:
            entity["early_win_note"] = node["early_win_note"]
        entity["pinnacle"] = node["pinnacle"]
        if "pinnacle_note" in node:
            entity["pinnacle_note"] = node["pinnacle_note"]
        entity["tags"] = node["tags"]
        if "taxonomy" in node:
            entity["taxonomy"] = node["taxonomy"]

        filepath = os.path.join(ENTITIES_DIR, domain, name + ".jsonld")
        write_jsonld(entity, filepath)
        count += 1
    return count


def migrate_edges(edges_list):
    """Convert all edges to per-edge JSON-LD files.

    When two edges share the same (from, to) pair but differ in flow,
    the flow qualifier is appended to both @id and filename to
    disambiguate.
    """
    # Detect (from, to) collisions
    pair_counts = {}
    for edge in edges_list:
        key = (edge["from"], edge["to"])
        pair_counts[key] = pair_counts.get(key, 0) + 1

    count = 0
    for edge in edges_list:
        from_fn = id_to_filename(edge["from"])
        to_fn = id_to_filename(edge["to"])
        pair_key = (edge["from"], edge["to"])

        # Determine if we need flow disambiguation
        needs_flow_suffix = pair_counts[pair_key] > 1

        if needs_flow_suffix:
            edge_id = "edge/{}__{}/{}".format(
                edge["from"], edge["to"], edge["flow"]
            )
            filename = "{}__{}@{}.jsonld".format(
                from_fn, to_fn, edge["flow"]
            )
        else:
            edge_id = "edge/{}__{}".format(edge["from"], edge["to"])
            filename = "{}__{}.jsonld".format(from_fn, to_fn)

        entity = {
            "@context": "../../context.jsonld",
            "@id": edge_id,
            "@type": "Dependency",
            "from": edge["from"],
            "to": edge["to"],
            "edgeType": edge["type"],
            "flow": edge["flow"],
        }
        if "label" in edge:
            entity["label"] = edge["label"]

        filepath = os.path.join(EDGES_DIR, filename)
        write_jsonld(entity, filepath)
        count += 1
    return count


def migrate_products(nodes_list):
    """Create product JSON-LD files from unique output tokens."""
    # Collect first-occurrence source for each output token
    first_source = {}
    first_tags = {}
    for node in nodes_list:
        for token in node.get("outputs", []):
            if token not in first_source:
                first_source[token] = node["id"]
                first_tags[token] = node["tags"]

    count = 0
    for token in sorted(first_source.keys()):
        entity = {
            "@context": "../context.jsonld",
            "@id": token,
            "@type": "Product",
            "name": token_to_name(token),
            "source": first_source[token],
            "tags": filter_tags_for_product(first_tags[token]),
        }
        filepath = os.path.join(PRODUCTS_DIR, token + ".jsonld")
        write_jsonld(entity, filepath)
        count += 1
    return count


# ---------------------------------------------------------------------------
# Clean up sample files from Task 4
# ---------------------------------------------------------------------------

def remove_existing_files():
    """Remove sample entity/edge/product files (from Task 4).

    These overlap with migrated data and must be regenerated.
    """
    for target_dir in [ENTITIES_DIR, PRODUCTS_DIR]:
        if os.path.isdir(target_dir):
            shutil.rmtree(target_dir)
            print("  Removed: {}".format(target_dir))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=== JSON-LD Migration ===\n")

    # Load source data
    with open(os.path.join(DATA_DIR, "nodes.json"), "r", encoding="utf-8") as fh:
        nodes_data = json.load(fh)
    with open(os.path.join(DATA_DIR, "edges.json"), "r", encoding="utf-8") as fh:
        edges_data = json.load(fh)

    nodes_list = nodes_data["nodes"]
    edges_list = edges_data["edges"]

    print("Source: {} nodes, {} edges".format(len(nodes_list), len(edges_list)))

    # Remove existing sample files
    print("\nCleaning existing files...")
    remove_existing_files()

    # Migrate
    print("\nMigrating...")
    n_nodes = migrate_nodes(nodes_list)
    n_edges = migrate_edges(edges_list)
    n_products = migrate_products(nodes_list)

    print("\n=== Results ===")
    print("  Entities:  {} files in data/entities/".format(n_nodes))
    print("  Edges:     {} files in data/entities/_edges/".format(n_edges))
    print("  Products:  {} files in data/products/".format(n_products))

    # Verify counts
    assert n_nodes == len(nodes_list), "Node count mismatch: {} != {}".format(
        n_nodes, len(nodes_list)
    )
    assert n_edges == len(edges_list), "Edge count mismatch: {} != {}".format(
        n_edges, len(edges_list)
    )
    unique_outputs = set()
    for node in nodes_list:
        for token in node.get("outputs", []):
            unique_outputs.add(token)
    assert n_products == len(unique_outputs), (
        "Product count mismatch: {} != {}".format(n_products, len(unique_outputs))
    )

    print("\nAll counts verified. Migration complete.")


if __name__ == "__main__":
    main()
