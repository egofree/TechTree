# openLCA Mapping Strategy

**Status:** Draft
**Last updated:** 2026-05-27

## 1. Overview

This document defines how TechTree JSON-LD entities map to [openLCA schema](https://greendelta.github.io/olca-schema/) types. Both systems use JSON-LD natively, so the mapping is structural (field-to-field) rather than format conversion.

### TechTree Data Model

TechTree is a directed acyclic graph of industrial technology capabilities. Entity types:

| Type | Description | Count | ID pattern |
|------|-------------|-------|------------|
| Domain | Top-level category (e.g., "metals") | 24 | `metals` |
| Capability | Technology area within a domain | ~130 | `metals.iron-steel` |
| Process | Specific technique/operation | ~200 | `metals.iron-steel.blast-furnace` |
| Product | Material/substance produced | 100+ | `steel_plate` |
| Dependency | Directed edge (A depends on B) | 432 | `from__to` |

### openLCA Data Model

openLCA is a life cycle assessment (LCA) framework. Core types:

| Type | Description |
|------|-------------|
| Process | Unit operation with inputs/outputs (Exchanges) |
| Flow | Anything entering or leaving a process (product, waste, elementary) |
| Exchange | An input or output of a Flow in a Process |
| FlowProperty | A quantity (e.g., Mass, Energy) for expressing amounts |
| UnitGroup | Units of measure for a FlowProperty |

## 2. Entity-by-Entity Mapping

### 2.1 TechTree Entity (Domain/Capability/Process) → openLCA Process

Every TechTree node maps to an openLCA `Process`. The node hierarchy (Domain > Capability > Process) is expressed via openLCA's `category` path.

| TechTree Field | openLCA Field | Notes |
|----------------|---------------|-------|
| `id` / `@id` | `@id` | Generate UUID v5 from `techtree:` IRI namespace |
| — | `@type` | Always `"Process"` |
| `name` | `name` | Direct copy |
| `description` | `description` | Direct copy |
| `level` | `category` | Encoded as category path: `"TechTree/{domain}"`, `"TechTree/{domain}/{capability}"` |
| `parent` | `category` | Parent ID becomes category path |
| `tags.era` | `category` prefix | Prepended: `"TechTree/{era}/{domain}/..."` |
| `tags.material[]` | `tags` | Joined list |
| `tags.capability[]` | `tags` | Appended to tags list |
| `tags.lifecycle[]` | `tags` | Appended to tags list |
| `critical` | `otherProperties.critical` | Custom extension |
| `early_win` | `otherProperties.earlyWin` | Custom extension |
| `pinnacle` | `otherProperties.pinnacle` | Custom extension |
| `timeline` | `otherProperties.timeline` | Custom extension |
| `outputs[]` | `exchanges[]` (output) | Each output token → Product Flow + Exchange |
| (inferred from edges) | `exchanges[]` (input) | Dependency edges with `to == this node` → input Exchanges |
| — | `processType` | Always `"UNIT_PROCESS"` |

### 2.2 TechTree Product → openLCA Flow

Each TechTree `Product` entity maps to an openLCA `Flow` of type `PRODUCT_FLOW`.

| TechTree Field | openLCA Field | Notes |
|----------------|---------------|-------|
| `id` / `@id` | `@id` | Generate UUID v5 from `techtree:` IRI namespace |
| — | `@type` | Always `"Flow"` |
| `name` | `name` | Direct copy |
| `source` | `category` | `"TechTree/{source}"` |
| `tags.material[]` | `category` prefix | `"TechTree/{material}/{source}"` |
| — | `flowType` | Always `"PRODUCT_FLOW"` |
| — | `flowProperties[]` | Reference shared `"Mass"` FlowProperty |
| `tags.lifecycle[]` | `otherProperties.lifecycle` | Custom extension |

### 2.3 TechTree Dependency → openLCA Exchange

Each TechTree edge maps to an openLCA `Exchange` within the dependent (source) Process.

| TechTree Field | openLCA Field | Notes |
|----------------|---------------|-------|
| — | `@type` | Always `"Exchange"` |
| — | `isInput` | Always `true` (the dependent process *consumes* the prerequisite) |
| — | `isQuantitativeReference` | `false` (only the primary output is QRef) |
| — | `amount` | `1.0` (default; TechTree has no quantities) |
| `from` | (parent Process) | Exchange belongs to the `from` entity's Process |
| `to` | `flow` (Ref) | References the Flow created from the `to` entity's outputs |
| `edgeType` | `otherProperties.edgeType` | `"material"` or `"tool"` — custom extension |
| `flow` | `otherProperties.flowQualifier` | `"primary"`, `"byproduct-reuse"`, etc. — custom extension |
| `label` | `description` | Human-readable edge description |
| — | `unit` (Ref) | References shared `"item"` or `"kg"` unit |
| — | `flowProperty` (Ref) | References shared `"Mass"` or `"Items"` FlowProperty |

### 2.4 Output Tokens → openLCA Exchanges

TechTree's `outputs[]` array lists product tokens. Each becomes an output Exchange on the entity's Process:

| TechTree | openLCA Exchange |
|----------|------------------|
| First output token | `isQuantitativeReference: true`, `isInput: false` |
| Remaining tokens | `isQuantitativeReference: false`, `isInput: false` |
| Output name | `flow.name` (or lookup from products/) |
| — | `amount: 1.0` (default) |

## 3. Field-by-Field Mapping with JSON-LD Property Names

### TechTree JSON-LD → openLCA JSON-LD

```
techtree:id               →  @id (UUID v5 from techtree: namespace)
techtree:name             →  name
techtree:description      →  description
@type (Process|Capability|Domain)  →  @type = "Process"
techtree:level            →  category path segment
techtree:hasParent        →  category path segment
techtree:hasOutput        →  exchanges[].flow (PRODUCT_FLOW)
techtree:era              →  category prefix + tags[]
techtree:materialTag      →  tags[]
techtree:capabilityTag    →  tags[]
techtree:lifecycle        →  tags[] + otherProperties
techtree:critical         →  otherProperties.critical
techtree:earlyWin         →  otherProperties.earlyWin
techtree:pinnacle         →  otherProperties.pinnacle
techtree:timeline         →  otherProperties.timeline

# Edge fields
techtree:from             →  (parent Process of the Exchange)
techtree:to               →  exchanges[].flow (Ref to Flow)
techtree:edgeType         →  otherProperties.edgeType
techtree:flow             →  otherProperties.flowQualifier
techtree:label            →  exchanges[].description
```

## 4. Example: Full Mapping of `metals.iron-steel`

### Source: TechTree JSON-LD

```json
{
  "@context": "../../context.jsonld",
  "@type": "Capability",
  "critical": true,
  "critical_note": "Iron and steel are essential for machine tool beds...",
  "description": "Bloomery smelting of iron ore at 1200-1400°C...",
  "early_win": false,
  "id": "metals.iron-steel",
  "level": "capability",
  "name": "Iron & Steel Production",
  "outputs": ["wrought_iron", "steel", "iron_bloom", "heat_treated_steel"],
  "parent": "metals",
  "pinnacle": false,
  "tags": {
    "capability": [],
    "critical": true,
    "early-win": false,
    "era": "iron-age",
    "lifecycle": ["waste-source", "recyclable"],
    "material": ["metals"],
    "pinnacle": false
  },
  "timeline": "Years 5-15"
}
```

### Mapped: openLCA Process JSON-LD

```json
{
  "@type": "Process",
  "@id": "a7c8e2f1-3b4d-5e6f-9a0b-1c2d3e4f5a6b",
  "name": "Iron & Steel Production",
  "description": "Bloomery smelting of iron ore at 1200-1400°C producing wrought iron, carburization for steel, and crucible steel (Wootz method). Heat treatment: annealing, quenching, and tempering. This is the critical metallurgical capability that enables all subsequent domains.",
  "category": "TechTree/iron-age/metals",
  "processType": "UNIT_PROCESS",
  "tags": ["metals", "waste-source", "recyclable"],
  "lastInternalId": 4,
  "exchanges": [
    {
      "@type": "Exchange",
      "internalId": 1,
      "amount": 1.0,
      "isInput": false,
      "isQuantitativeReference": true,
      "isAvoidedProduct": false,
      "flow": {
        "@type": "Flow",
        "@id": "b1d2e3f4-5a6b-7c8d-9e0f-1a2b3c4d5e6f",
        "name": "wrought_iron"
      },
      "unit": {
        "@type": "Unit",
        "@id": "de6b8c7a-1b2c-3d4e-5f6a-7b8c9d0e1f2a",
        "name": "kg"
      },
      "flowProperty": {
        "@type": "FlowProperty",
        "@id": "93a60a56-a3c8-11da-a746-0800200b9a66",
        "name": "Mass"
      }
    },
    {
      "@type": "Exchange",
      "internalId": 2,
      "amount": 1.0,
      "isInput": false,
      "isQuantitativeReference": false,
      "isAvoidedProduct": false,
      "flow": {
        "@type": "Flow",
        "@id": "c2e3f4a5-6b7c-8d9e-0f1a-2b3c4d5e6f7a",
        "name": "steel"
      },
      "unit": {
        "@type": "Unit",
        "@id": "de6b8c7a-1b2c-3d4e-5f6a-7b8c9d0e1f2a",
        "name": "kg"
      },
      "flowProperty": {
        "@type": "FlowProperty",
        "@id": "93a60a56-a3c8-11da-a746-0800200b9a66",
        "name": "Mass"
      }
    },
    {
      "@type": "Exchange",
      "internalId": 3,
      "amount": 1.0,
      "isInput": false,
      "isQuantitativeReference": false,
      "isAvoidedProduct": false,
      "flow": {
        "@type": "Flow",
        "@id": "d3f4a5b6-7c8d-9e0f-1a2b-3c4d5e6f7a8b",
        "name": "iron_bloom"
      },
      "unit": {
        "@type": "Unit",
        "@id": "de6b8c7a-1b2c-3d4e-5f6a-7b8c9d0e1f2a",
        "name": "kg"
      },
      "flowProperty": {
        "@type": "FlowProperty",
        "@id": "93a60a56-a3c8-11da-a746-0800200b9a66",
        "name": "Mass"
      }
    },
    {
      "@type": "Exchange",
      "internalId": 4,
      "amount": 1.0,
      "isInput": false,
      "isQuantitativeReference": false,
      "isAvoidedProduct": false,
      "flow": {
        "@type": "Flow",
        "@id": "e4a5b6c7-8d9e-0f1a-2b3c-4d5e6f7a8b9c",
        "name": "heat_treated_steel"
      },
      "unit": {
        "@type": "Unit",
        "@id": "de6b8c7a-1b2c-3d4e-5f6a-7b8c9d0e1f2a",
        "name": "kg"
      },
      "flowProperty": {
        "@type": "FlowProperty",
        "@id": "93a60a56-a3c8-11da-a746-0800200b9a66",
        "name": "Mass"
      }
    }
  ],
  "otherProperties": {
    "techtreeId": "metals.iron-steel",
    "techtreeLevel": "capability",
    "techtreeParent": "metals",
    "critical": true,
    "criticalNote": "Iron and steel are essential for machine tool beds, cutting tools, boilers, generators, and all precision machinery",
    "earlyWin": false,
    "pinnacle": false,
    "timeline": "Years 5-15"
  }
}
```

### Mapped: Dependency Edge as Input Exchange

Edge: `transport.railways` depends on `metals.iron-steel` (material, primary flow).
This becomes an input Exchange on the `transport.railways` Process:

```json
{
  "@type": "Exchange",
  "internalId": 1,
  "amount": 1.0,
  "isInput": true,
  "isQuantitativeReference": false,
  "isAvoidedProduct": false,
  "flow": {
    "@type": "Flow",
    "@id": "a7c8e2f1-3b4d-5e6f-9a0b-1c2d3e4f5a6b",
    "name": "Iron & Steel Production"
  },
  "unit": {
    "@type": "Unit",
    "@id": "de6b8c7a-1b2c-3d4e-5f6a-7b8c9d0e1f2a",
    "name": "kg"
  },
  "flowProperty": {
    "@type": "FlowProperty",
    "@id": "93a60a56-a3c8-11da-a746-0800200b9a66",
    "name": "Mass"
  },
  "otherProperties": {
    "edgeType": "material",
    "flowQualifier": "primary"
  }
}
```

### Mapped: Product as Flow

Product `steel_plate` from `data/products/steel_plate.jsonld`:

```json
{
  "@type": "Flow",
  "@id": "f5b6c7d8-9e0f-1a2b-3c4d-5e6f7a8b9c0d",
  "name": "Steel Plate",
  "category": "TechTree/metals/metals.forming",
  "flowType": "PRODUCT_FLOW",
  "flowProperties": [
    {
      "@type": "FlowPropertyFactor",
      "isRefFlowProperty": true,
      "conversionFactor": 1.0,
      "flowProperty": {
        "@type": "FlowProperty",
        "@id": "93a60a56-a3c8-11da-a746-0800200b9a66",
        "name": "Mass"
      }
    }
  ],
  "otherProperties": {
    "techtreeId": "steel_plate",
    "techtreeSource": "metals.forming",
    "lifecycle": ["waste-source", "recyclable"]
  }
}
```

## 5. Required Setup Entities

Before importing TechTree data, the following openLCA entities must exist in the target database:

### 5.1 UnitGroups

| Name | Default Unit | Purpose |
|------|-------------|---------|
| Units of mass | kg | Physical quantities for materials |
| Units of items | item | Count-based flows for non-mass outputs |
| Units of energy | MJ | Energy-related flows (optional) |

### 5.2 FlowProperties

| Name | Type | UnitGroup | openLCA @id |
|------|------|-----------|-------------|
| Mass | PHYSICAL_QUANTITY | Units of mass | `93a60a56-a3c8-11da-a746-0800200b9a66` |
| Items | OTHER_QUANTITY | Units of items | (generate new) |
| Energy | PHYSICAL_QUANTITY | Units of energy | (optional) |

### 5.3 Categories

The following category tree must be created:

```
TechTree/
├── stone-age/
│   ├── foundations/
│   └── ...
├── copper-age/
│   └── ...
├── bronze-age/
│   └── ...
├── iron-age/
│   ├── metals/
│   └── ...
├── industrial/
│   └── ...
├── electronic/
│   └── ...
├── semiconductor/
│   └── ...
└── advanced/
    └── ...
```

### 5.4 ID Generation Strategy

TechTree uses semantic IDs (e.g., `metals.iron-steel`). openLCA requires UUIDs. Strategy:

- Use **UUID v5** with namespace `techtree:` to generate deterministic UUIDs
- `uuid.uuid5(uuid.NAMESPACE_URL, "techtree:metals.iron-steel")` → deterministic, reproducible
- Preserve original TechTree ID in `otherProperties.techtreeId` for traceability

## 6. Limitations and Follow-Up Work

### 6.1 Current Limitations

1. **No quantities**: TechTree has no mass/energy amounts. All exchanges default to `amount: 1.0`. Real LCA requires actual quantities.
2. **No elementary flows**: TechTree has no environmental exchanges (CO2 emissions, water consumption, etc.). These must be added separately for LCA.
3. **Single unit**: All flows use "kg" by default. Some outputs are better measured in "items", "MJ", or "m³".
4. **No allocation**: Multiple outputs from a single process require allocation factors. Not modeled in TechTree.
5. **No geographic data**: TechTree is technology-agnostic (no locations). openLCA `Location` references are omitted.
6. **Category vs. hierarchy**: TechTree's three-level hierarchy (Domain/Capability/Process) is flattened into openLCA category paths, losing the semantic `parent` link.
7. **Edge directionality**: TechTree edges express dependency (A needs B), not physical flow direction. The mapping assumes the dependency target provides a product input.

### 6.2 Follow-Up Work

| Task | Description | Priority |
|------|-------------|----------|
| Full import bridge | Python script using `olca-schema` package to write `.zolca` files | High |
| Quantity enrichment | Add mass/energy/volume amounts to TechTree nodes | High |
| Elementary flow mapping | Map TechTree environmental interactions to ecoinvent elementary flows | Medium |
| Bidirectional sync | Round-trip: openLCA → TechTree updates | Low |
| Allocation modeling | Multi-output process allocation strategies | Medium |
| Unit inference | Automatic unit selection based on material tags | Low |

### 6.3 References

- [openLCA schema documentation](https://greendelta.github.io/olca-schema/)
- [olca-schema Python package](https://pypi.org/project/olca-schema/)
- TechTree context: `data/context.jsonld`
- TechTree schemas: `data/schema/*.schema.json`
