#!/usr/bin/env python3
"""Dry-run TechTree to openLCA schema mapping.

Reads TechTree JSON-LD entities and produces the equivalent
openLCA-compatible JSON-LD output (Process, Flow, Exchange objects).

Usage:
    python3 scripts/tt-to-openlca.py --sample 5 --dry-run
    python3 scripts/tt-to-openlca.py --entity metals.iron-steel --dry-run
    python3 scripts/tt-to-openlca.py --all --dry-run

Does NOT write files, does NOT require olca-schema package.
Pure structural mapping proof-of-concept.
"""

import argparse
import hashlib
import json
import os
import random
import sys
import uuid

# ---------------------------------------------------------------------------
# Bootstrap import path for scripts/lib/
# ---------------------------------------------------------------------------

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.dirname(_SCRIPTS_DIR)
sys.path.insert(0, _SCRIPTS_DIR)

from lib.tt_data import (  # noqa: E402
    ENTITIES_DIR,
    EDGES_DIR,
    load_all_entities,
    load_dependencies_for,
    load_entity,
    load_product,
    load_all_products,
)

# ---------------------------------------------------------------------------
# Constants — well-known openLCA reference UUIDs
# ---------------------------------------------------------------------------

# Mass flow property (standard openLCA)
MASS_FLOW_PROPERTY_REF = {
    "@type": "FlowProperty",
    "@id": "93a60a56-a3c8-11da-a746-0800200b9a66",
    "name": "Mass",
}

# kg unit (standard openLCA)
KG_UNIT_REF = {
    "@type": "Unit",
    "@id": "20aadc24-a391-41cf-b340-3e4529f44bde",
    "name": "kg",
}

# Namespace UUID for deterministic UUID v5 generation
TECHTREE_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_URL, "techtree:")


# ---------------------------------------------------------------------------
# ID generation
# ---------------------------------------------------------------------------

def techtree_to_uuid(entity_id: str) -> str:
    """Generate a deterministic UUID v5 from a TechTree entity ID."""
    return str(uuid.uuid5(TECHTREE_NAMESPACE, entity_id))


# ---------------------------------------------------------------------------
# Mapping functions
# ---------------------------------------------------------------------------

def map_entity_to_process(entity: dict) -> dict:
    """Map a TechTree entity (Domain/Capability/Process) to an openLCA Process."""
    eid = entity.get("id") or entity.get("@id", "unknown")
    tags = entity.get("tags", {})

    # Category path: TechTree/{era}/{domain}
    era = tags.get("era", "unknown")
    domain = eid.split(".")[0] if "." in eid else eid
    category = f"TechTree/{era}/{domain}"

    # Tag list from material, capability, lifecycle
    tag_list = list(tags.get("material", []))
    tag_list.extend(tags.get("capability", []))
    tag_list.extend(tags.get("lifecycle", []))

    # Output exchanges
    exchanges = []
    outputs = entity.get("outputs", [])
    for idx, output_token in enumerate(outputs):
        flow_uuid = techtree_to_uuid(f"flow:{output_token}")
        exchanges.append({
            "@type": "Exchange",
            "internalId": idx + 1,
            "amount": 1.0,
            "isInput": False,
            "isQuantitativeReference": idx == 0,
            "isAvoidedProduct": False,
            "flow": {
                "@type": "Flow",
                "@id": flow_uuid,
                "name": output_token,
            },
            "unit": KG_UNIT_REF,
            "flowProperty": MASS_FLOW_PROPERTY_REF,
        })

    # Input exchanges from dependency edges
    input_id = len(exchanges) + 1
    for edge in load_dependencies_for(eid):
        if edge.get("from") != eid:
            continue
        to_id = edge.get("to", "unknown")
        to_entity = load_entity(to_id)
        to_name = to_entity.get("name", to_id) if to_entity else to_id

        exchanges.append({
            "@type": "Exchange",
            "internalId": input_id,
            "amount": 1.0,
            "isInput": True,
            "isQuantitativeReference": False,
            "isAvoidedProduct": False,
            "flow": {
                "@type": "Flow",
                "@id": techtree_to_uuid(to_id),
                "name": to_name,
            },
            "unit": KG_UNIT_REF,
            "flowProperty": MASS_FLOW_PROPERTY_REF,
            "otherProperties": {
                "edgeType": edge.get("edgeType", "unknown"),
                "flowQualifier": edge.get("flow", "primary"),
            },
        })
        input_id += 1

    process = {
        "@type": "Process",
        "@id": techtree_to_uuid(eid),
        "name": entity.get("name", eid),
        "description": entity.get("description", ""),
        "category": category,
        "processType": "UNIT_PROCESS",
        "lastInternalId": max(input_id - 1, len(outputs)),
        "exchanges": exchanges,
        "otherProperties": {
            "techtreeId": eid,
            "techtreeLevel": entity.get("level", "unknown"),
            "techtreeParent": entity.get("parent", ""),
            "critical": entity.get("critical", False),
            "earlyWin": entity.get("early_win", False),
            "pinnacle": entity.get("pinnacle", False),
            "timeline": entity.get("timeline", ""),
        },
    }

    if tag_list:
        process["tags"] = tag_list

    return process


def map_product_to_flow(product: dict) -> dict:
    """Map a TechTree Product entity to an openLCA Flow."""
    pid = product.get("id") or product.get("@id", "unknown")
    tags = product.get("tags", {})

    materials = tags.get("material", [])
    source = product.get("source", "unknown")
    material_cat = materials[0] if materials else "unknown"

    flow = {
        "@type": "Flow",
        "@id": techtree_to_uuid(f"product:{pid}"),
        "name": product.get("name", pid),
        "category": f"TechTree/{material_cat}/{source}",
        "flowType": "PRODUCT_FLOW",
        "flowProperties": [
            {
                "@type": "FlowPropertyFactor",
                "isRefFlowProperty": True,
                "conversionFactor": 1.0,
                "flowProperty": MASS_FLOW_PROPERTY_REF,
            }
        ],
        "otherProperties": {
            "techtreeId": pid,
            "techtreeSource": source,
        },
    }

    lifecycle = tags.get("lifecycle", [])
    if lifecycle:
        flow["otherProperties"]["lifecycle"] = lifecycle

    return flow


def map_edge_to_exchange(edge: dict) -> dict:
    """Map a TechTree Dependency edge to an openLCA Exchange description.

    Returns a dict showing the Exchange that would be added to the
    'from' entity's Process as an input.
    """
    from_id = edge.get("from", "unknown")
    to_id = edge.get("to", "unknown")
    to_entity = load_entity(to_id)
    to_name = to_entity.get("name", to_id) if to_entity else to_id

    return {
        "@type": "Exchange",
        "internalId": "(auto-assigned)",
        "amount": 1.0,
        "isInput": True,
        "isQuantitativeReference": False,
        "isAvoidedProduct": False,
        "flow": {
            "@type": "Flow",
            "@id": techtree_to_uuid(to_id),
            "name": to_name,
        },
        "unit": KG_UNIT_REF,
        "flowProperty": MASS_FLOW_PROPERTY_REF,
        "_meta": {
            "parentProcess": from_id,
            "edgeType": edge.get("edgeType", "unknown"),
            "flowQualifier": edge.get("flow", "primary"),
            "label": edge.get("label", ""),
        },
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="TechTree to openLCA dry-run mapping"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--sample", type=int, metavar="N",
        help="Map N random entities",
    )
    group.add_argument(
        "--entity", type=str, metavar="ID",
        help="Map a specific entity by TechTree ID",
    )
    group.add_argument(
        "--all", action="store_true",
        help="Map all entities",
    )
    parser.add_argument(
        "--dry-run", action="store_true", default=True,
        help="Print output without writing files (always true)",
    )
    parser.add_argument(
        "--show-edges", action="store_true",
        help="Also show dependency edges as Exchanges",
    )
    parser.add_argument(
        "--show-products", action="store_true",
        help="Also show Product → Flow mappings",
    )

    args = parser.parse_args()

    # Load entities
    if args.entity:
        entities = []
        e = load_entity(args.entity)
        if e is None:
            print(f"ERROR: Entity not found: {args.entity}", file=sys.stderr)
            sys.exit(1)
        entities.append(e)
    elif args.all:
        entities = load_all_entities()
    else:
        all_entities = load_all_entities()
        if args.sample > len(all_entities):
            args.sample = len(all_entities)
        entities = random.sample(all_entities, args.sample)

    print(f"# TechTree → openLCA dry-run mapping")
    print(f"# Entities: {len(entities)}")
    print(f"# Mode: dry-run (no files written)")
    print(f"# {'=' * 60}")
    print()

    for entity in entities:
        eid = entity.get("id") or entity.get("@id", "unknown")
        name = entity.get("name", eid)
        level = entity.get("level", "unknown")

        print(f"## Process: {name} ({eid}) [level={level}]")
        print()

        process = map_entity_to_process(entity)
        print(json.dumps(process, indent=2, ensure_ascii=False))
        print()

        # Show dependency edges for this entity
        if args.show_edges:
            deps = load_dependencies_for(eid)
            if deps:
                print(f"### Input Exchanges (dependencies): {len(deps)}")
                for dep in deps:
                    exchange = map_edge_to_exchange(dep)
                    print(json.dumps(exchange, indent=2, ensure_ascii=False))
                    print()

        # Show product flows
        if args.show_products:
            outputs = entity.get("outputs", [])
            if outputs:
                print(f"### Product Flows (from outputs): {len(outputs)}")
                for output_token in outputs:
                    product = load_product(output_token)
                    if product:
                        flow = map_product_to_flow(product)
                        print(json.dumps(flow, indent=2, ensure_ascii=False))
                    else:
                        # Synthesize a minimal flow
                        flow = {
                            "@type": "Flow",
                            "@id": techtree_to_uuid(f"flow:{output_token}"),
                            "name": output_token,
                            "flowType": "PRODUCT_FLOW",
                            "note": "Synthesized from output token (no product file)",
                        }
                        print(json.dumps(flow, indent=2, ensure_ascii=False))
                    print()

    # Summary
    print(f"# {'=' * 60}")
    print(f"# Total processes mapped: {len(entities)}")
    total_exchanges = sum(
        len(map_entity_to_process(e).get("exchanges", []))
        for e in entities
    )
    print(f"# Total exchanges generated: {total_exchanges}")


if __name__ == "__main__":
    main()
