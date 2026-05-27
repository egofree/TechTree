# Process Knowledge Standard

**Version:** 1.0.0-draft
**Status:** Draft
**Date:** 2026-05-27
**URI:** `https://egofree.github.io/TechTree/spec/process-knowledge-standard/v1.0`

> Formal specification for representing process knowledge as a directed acyclic graph of industrial capabilities, their material flows, and the dependencies between them. This document IS the standard. The TechTree data files (`nodes.json`, `edges.json`, `context.jsonld`) are its reference implementation.

---

## 1. Introduction

### 1.1 Problem Statement

Industrial processes form deep dependency chains. Making a GPU requires photolithography, which requires precision optics, which requires glass, which requires mining, which requires tools, which requires fire. These chains span hundreds of nodes and thousands of edges, yet no existing standard captures them as a single queryable graph with typed dependencies.

Life cycle assessment databases (openLCA, ecoinvent) model individual process inputs and outputs but lack the cross-domain dependency graph. Materials ontologies (EMMO, GPO) define what materials *are* but not how to *bootstrap* them from scratch. Standards like STEP handle product geometry but not process sequencing. None of these tools answer the question: "What is the minimum set of capabilities needed to produce X, starting from nothing?"

### 1.2 What This Standard Defines

This standard defines a data model for representing industrial process knowledge as a typed, tagged, hierarchical directed acyclic graph (DAG). Specifically:

- **Entity types**: Domain, Capability, Process, Product, and Dependency
- **Tag vocabularies**: Closed sets for materials, capabilities, eras, and lifecycle roles
- **Edge semantics**: Typed dependencies (material vs. tool) with circular economy flow qualifiers
- **Validation rules**: DAG constraint, cross-reference integrity, SIK Placement Test for domain boundaries
- **Serialization**: JSON-LD using a custom `techtree:` URI scheme

### 1.3 What This Standard Does Not Define

This is not an OWL ontology. It does not define formal axioms, inference rules, or class hierarchies in the Description Logic sense. It does not attempt OWL imports from EMMO, GPO, or any other ontology. The relationship to these ontologies is vocabulary-level alignment (shared concept IRIs) only.

This is also not an API specification. It defines a data format, not a transport protocol.

### 1.4 Relationship to Existing Standards

| Standard | Relationship |
|----------|-------------|
| **EMMO** (Elementary Multiperspective Material Ontology) | Vocabulary alignment. `techtree:Process` aligns with `EMMO_43e9a05d` (Process), `techtree:Product` with `EMMO_ec7464a9` (ManufacturedObject), `techtree:hasOutput` with `EMMO_c4bace1d` (hasOutput). No OWL imports. |
| **GPO** (Battery Data Ontology, EMMO domain) | Structural inspiration for domain-specific extensions within a general ontology framework. |
| **openLCA schema** | JSON-LD serialization compatibility. openLCA uses `@type` and `@id` annotations natively. Full round-trip (TechTree to openLCA and back) is a design goal. |
| **OPTIMADE** | Structural inspiration. OPTIMADE defines conformance levels (MUST/SHOULD) and closed property vocabularies with extensible provider-specific prefixes. This standard adopts similar conformance language. |
| **STEP** (ISO 10303) | Complementary. STEP handles product geometry and tolerances; this standard handles process dependencies and material flows. |
| **CEON** (Circular Economy Ontology Network) | Conceptual overlap in lifecycle tags and circular material flows. `techtree:lifecycle` tags and `flow` qualifiers address similar concerns at a coarser granularity. |

### 1.5 Audience

This specification is written for:

- Data engineers building tools that consume TechTree data
- Domain experts adding new nodes or edges to the graph
- Ontology engineers mapping TechTree concepts to other formalisms

No prior knowledge of OWL or formal ontology is required. Familiarity with JSON, directed graphs, and basic materials science is assumed.

---

## 2. Conformance

This section defines what it means for a data file to conform to this standard. Conformance language follows RFC 2119 conventions.

### 2.1 Conformance Levels

**MUST** (required): The data file violates the standard if it does not satisfy this requirement. Validators MUST report an error.

**SHOULD** (recommended): The data file satisfies best practice if it meets this requirement. Validators SHOULD report a warning if it is not met.

### 2.2 Conformance Criteria

A data file **conforms** to this standard if and only if all of the following hold:

1. **Entity structure**: Every entity has the required fields defined in Section 5 for its entity type. (MUST)
2. **Tag vocabulary**: Every tag value belongs to the closed vocabulary defined in Section 7. (MUST)
3. **Edge types**: Every edge has `type` equal to `"material"` or `"tool"`. No other values are valid. (MUST)
4. **Flow qualifiers**: Every edge has `flow` equal to one of the four defined values. (MUST)
5. **DAG constraint**: The subgraph formed by edges with `flow: "primary"` is acyclic. (MUST)
6. **Cross-reference integrity**: Every `from` and `to` value in edges references an existing entity ID. Every `parent` value (when non-null) references an existing entity ID. (MUST)
7. **ID format**: Every entity ID uses dotted hierarchical kebab-case as specified in Section 4. (MUST)
8. **SIK Placement**: Every domain boundary can be justified by the SIK Placement Test (Section 10). (SHOULD)
9. **Lifecycle tag consistency**: Nodes with lifecycle tags SHOULD have corresponding circular economy edges. (SHOULD)

### 2.3 Partial Conformance

A data file that satisfies all MUST requirements but misses one or more SHOULD requirements is **partially conforming**. It is usable but should be improved.

A data file that fails any MUST requirement is **non-conforming** and should be corrected before use.

---

## 3. Document Structure

### 3.1 File Organization

A conforming dataset consists of:

```
data/
  context.jsonld          # JSON-LD context defining all terms
  nodes.json              # All entity records (Domain, Capability, Process, Product)
  edges.json              # All dependency records (Dependency entities)
```

### 3.2 Per-Entity File Layout (Future)

The standard anticipates a per-entity file layout for larger datasets:

```
data/
  context.jsonld
  entities/
    foundations.jsonld             # Domain entity
    metals.jsonld                  # Domain entity
    metals/
      iron-steel.jsonld            # Capability entity
      copper-bronze.jsonld         # Capability entity
  products/
    wrought-iron.jsonld            # Product entity
    steel.jsonld                   # Product entity
    copper.jsonld                  # Product entity
```

Each file contains a single JSON-LD entity. The filename matches the final segment of the entity ID. Directory nesting matches the dotted hierarchy.

The monolithic `nodes.json` / `edges.json` format is the current reference implementation. Per-entity files are a valid alternative serialization that preserves all semantics.

### 3.3 Naming Conventions

- **Entity IDs**: Dotted hierarchical kebab-case: `domain`, `domain.capability`, `domain.capability.process`
- **Domain names**: Single kebab-case segment: `foundations`, `machine-tools`, `gas-handling`
- **Product IDs**: Keccak-case tokens matching `outputs` values: `wrought_iron`, `cast_iron_parts`
- **File names**: Match the final ID segment with `.jsonld` extension

---

## 4. Entity Types

The data model defines five entity types. Each corresponds to a distinct concept in the process knowledge graph.

### 4.1 Domain

A Domain is a top-level technology area. It groups capabilities that share physical infrastructure, knowledge base, and practitioner profile (as determined by the SIK Placement Test, Section 10).

- **ID format**: Single segment, no dots (e.g., `metals`, `silicon`, `energy`)
- **Level**: `"domain"`
- **Parent**: `null`
- **Role**: Container for capabilities; inherits the union of children's tags

**Example:**

```json
{
  "@context": "context.jsonld",
  "id": "metals",
  "type": "Domain",
  "name": "Metals",
  "level": "domain",
  "parent": null,
  "description": "Extraction and working of metals from ore. Spans copper, bronze, iron, and steel production with increasingly complex smelting.",
  "timeline": "Years 5-15",
  "outputs": ["copper", "bronze", "wrought_iron", "steel", "metal_tools"],
  "critical": false,
  "early_win": false,
  "pinnacle": false,
  "tags": {
    "material": ["metals"],
    "capability": [],
    "era": "copper-age",
    "critical": false,
    "early-win": false,
    "pinnacle": false
  }
}
```

### 4.2 Capability

A Capability is a major skill or process family within a Domain. It represents a coherent group of related processes that produce a distinct set of outputs.

- **ID format**: Two segments, one dot (e.g., `metals.iron-steel`, `silicon.purification`)
- **Level**: `"capability"`
- **Parent**: Domain ID
- **Role**: Functional grouping within a domain; the primary unit of dependency analysis

**Example:**

```json
{
  "@context": "context.jsonld",
  "id": "metals.iron-steel",
  "type": "Capability",
  "name": "Iron & Steel Production",
  "level": "capability",
  "parent": "metals",
  "description": "Bloomery smelting of iron ore at 1200-1400C producing wrought iron, carburization for steel, and crucible steel (Wootz method). Heat treatment: annealing, quenching, and tempering.",
  "timeline": "Years 5-15",
  "outputs": ["wrought_iron", "steel", "iron_bloom", "heat_treated_steel"],
  "critical": true,
  "critical_note": "Iron and steel are essential for machine tool beds, cutting tools, boilers, generators, and all precision machinery",
  "early_win": false,
  "pinnacle": false,
  "tags": {
    "material": ["metals"],
    "capability": [],
    "era": "iron-age",
    "lifecycle": ["waste-source", "recyclable"],
    "critical": true,
    "early-win": false,
    "pinnacle": false
  }
}
```

### 4.3 Process

A Process is a specific technique or operation within a Capability. It represents the finest level of granularity in the dependency graph.

- **ID format**: Three or more segments, two or more dots (e.g., `silicon.crystal-growth.cz-pulling`)
- **Level**: `"process"`
- **Parent**: Everything before the last dot
- **Role**: Atomic operation; the finest unit of dependency analysis
- **Depth**: Arbitrary. `domain.capability.process.sub-process` is valid. All nodes with 2+ dots have level `"process"`.

### 4.4 Product

A Product is a first-class entity representing a physical material, component, or artifact produced by a Process or Capability. Products are extracted from the `outputs` field of parent entities.

- **ID format**: Keccak-case token matching an `outputs` value (e.g., `wrought_iron`, `steel`)
- **Role**: Connects producing and consuming entities through dependency edges
- **Source**: The `outputs` array on Domain, Capability, or Process entities lists Product tokens

Products are implicit in the current monolithic serialization. They become explicit first-class entities in the per-entity file layout (Section 3.2).

### 4.5 Dependency

A Dependency is a directed edge representing a requirement relationship between two entities. The dependent entity (`from`) cannot be built until the prerequisite entity (`to`) is available.

- **Fields**: `from`, `to`, `type`, `flow`
- **Direction convention**: `from` depends on `to`
- **Role**: Encodes the prerequisite structure of the technology tree

**Example:**

```json
{
  "from": "machine-tools.casting",
  "to": "metals.iron-steel",
  "type": "material",
  "flow": "primary"
}
```

---

## 5. Properties

This section defines every property in the data model. For each property, the following information is provided: the JSON key name, the JSON-LD term it maps to (via `context.jsonld`), the value type, whether it is required, and any constraints.

### 5.1 Core Properties

These properties appear on all entity types (Domain, Capability, Process).

| Property | JSON-LD Term | Type | Required | Constraints |
|----------|-------------|------|----------|-------------|
| `id` | `@id` | string | MUST | Dotted hierarchical kebab-case. See Section 3.3. |
| `type` | `@type` | string | MUST | One of: `"Domain"`, `"Capability"`, `"Process"`, `"Product"`, `"Dependency"` |
| `name` | `techtree:name` | string | MUST | Human-readable display name. Non-empty. |
| `level` | `techtree:level` | string | MUST* | One of: `"domain"`, `"capability"`, `"process"`. Auto-derived from ID dot count. |
| `parent` | `techtree:hasParent` | string or null | MUST* | ID of parent entity. `null` for domains. Auto-derived from ID. |
| `description` | `techtree:description` | string | MUST | 1-3 sentence summary. Non-empty. |
| `timeline` | `techtree:timeline` | string | MUST | Estimated time range (e.g., `"Years 0-10"`). |
| `outputs` | `techtree:hasOutput` | array of strings | MUST | Product/material/capability tokens produced. May be empty. |

* The `level` and `parent` fields are auto-derived from the entity ID and MUST be consistent with the derivation rules. They are stored explicitly for query convenience.

#### Auto-derivation rules:

**`level`:**
- 0 dots in ID: `"domain"`
- 1 dot in ID: `"capability"`
- 2+ dots in ID: `"process"`

**`parent`:**
- For domain entities: `null`
- For all others: everything before the last dot

Examples:
- `metals` becomes `level: "domain"`, `parent: null`
- `metals.iron-steel` becomes `level: "capability"`, `parent: "metals"`
- `silicon.crystal-growth.cz-pulling` becomes `level: "process"`, `parent: "silicon.crystal-growth"`

### 5.2 Significance Properties

These boolean flags mark entities of particular strategic importance.

| Property | JSON-LD Term | Type | Required | Constraints |
|----------|-------------|------|----------|-------------|
| `critical` | `techtree:critical` | boolean | MUST | True if critical-path enabler |
| `critical_note` | `techtree:criticalNote` | string | Conditional | Present only when `critical=true` |
| `early_win` | `techtree:earlyWin` | boolean | MUST | True if high-value early feedback loop |
| `early_win_note` | `techtree:earlyWinNote` | string | Conditional | Present only when `early_win=true` |
| `pinnacle` | `techtree:pinnacle` | boolean | MUST | True if end-goal requiring mature ecosystem |
| `pinnacle_note` | `techtree:pinnacleNote` | string | Conditional | Present only when `pinnacle=true` |

**Definitions:**

- **Critical**: Downstream capabilities are blocked without this. The entire chain stops if this node is unavailable.
- **Early win**: Produces high-value output early, creating a positive feedback loop (better tools yield more surplus yields better tools).
- **Pinnacle**: An end-goal that requires the mature ecosystem plus generational refinement. Not a stepping stone; an endpoint.

### 5.3 Tag Properties

The `tags` object (JSON-LD term: `techtree:TagSet`) groups classification dimensions. See Section 7 for complete vocabulary definitions.

| Property | JSON-LD Term | Type | Required | Constraints |
|----------|-------------|------|----------|-------------|
| `tags` | `techtree:TagSet` | object | MUST | Contains the following sub-properties |
| `tags.material` | `techtree:materialTag` | array of strings | MUST | Values from Section 7.1. May be empty. |
| `tags.capability` | `techtree:capabilityTag` | array of strings | MUST | Values from Section 7.2. May be empty. |
| `tags.era` | `techtree:era` | string | MUST | Exactly one value from Section 7.3. |
| `tags.lifecycle` | `techtree:lifecycle` | array of strings | SHOULD | Values from Section 7.4. Optional. |
| `tags.critical` | (duplicate of `techtree:critical`) | boolean | MUST | Must match top-level `critical` field. |
| `tags.early-win` | `techtree:earlyWinTag` | boolean | MUST | Must match top-level `early_win` field. |
| `tags.pinnacle` | (duplicate of `techtree:pinnacle`) | boolean | MUST | Must match top-level `pinnacle` field. |

The boolean tags are duplicated between the top-level fields and the `tags` object for backward compatibility and query convenience. Both locations MUST contain the same values.

### 5.4 Taxonomy Property

| Property | JSON-LD Term | Type | Required | Constraints |
|----------|-------------|------|----------|-------------|
| `taxonomy` | `techtree:taxonomy` | array of strings | Optional | See Section 6. |

### 5.5 Edge Properties

These properties appear on Dependency entities only.

| Property | JSON-LD Term | Type | Required | Constraints |
|----------|-------------|------|----------|-------------|
| `from` | `techtree:from` | string | MUST | Entity ID of the dependent. Must reference an existing entity. |
| `to` | `techtree:to` | string | MUST | Entity ID of the prerequisite. Must reference an existing entity. |
| `type` | `techtree:edgeType` | string | MUST | One of: `"material"`, `"tool"`. See Section 8. |
| `flow` | `techtree:flow` | string | MUST | One of: `"primary"`, `"byproduct-reuse"`, `"waste-recovery"`, `"recycling-loop"`. See Section 9. |

### 5.6 Auxiliary Properties

| Property | JSON-LD Term | Type | Required | Constraints |
|----------|-------------|------|----------|-------------|
| `wikidataId` | `techtree:wikidataId` | string | Optional | Wikidata entity identifier (e.g., `"Q877"` for steel) |
| `label` | `techtree:label` | string | Optional | Short label for diagram rendering |

---

## 6. Taxonomy Field

### 6.1 Purpose

The `taxonomy` field provides hierarchical classification by material origin, complementary to the flat tag system. Where tags use closed vocabularies with fixed values, taxonomy uses an open dotted notation that supports deeper categorization within material families.

### 6.2 Format

```json
{
  "taxonomy": ["biomass.plant.wood", "mineral.ore.iron"]
}
```

**Structural rules:**

- Each value is a dot-separated string of two or more segments: `root.branch`, `root.branch.leaf`, etc.
- Segments use kebab-case: lowercase letters, digits, and hyphens. No uppercase, no underscores.
- The first segment (root) must be one of three defined roots.
- Depth is unbounded.
- No duplicate values within a single entity's array.

### 6.3 Root Vocabulary

| Root | Definition | Examples |
|------|-----------|----------|
| `biomass` | Materials derived from living organisms | `biomass.plant.wood`, `biomass.animal.meat`, `biomass.plant.fiber` |
| `mineral` | Inorganic materials extracted from the earth | `mineral.ore.iron`, `mineral.stone.flint`, `mineral.clay.kaolin` |
| `synthetic` | Materials produced through industrial processing | `synthetic.alloy.steel`, `synthetic.polymer.thermoset`, `synthetic.semiconductor.silicon` |

The root vocabulary is a closed set. Branches beneath existing roots may be created as needed without a spec update.

### 6.4 Relationship to Tags

Taxonomy and tags are independent. A node may have `tags.material: ["wood"]` and `taxonomy: ["biomass.plant.wood"]`. Taxonomy values are NOT validated against tag values. Taxonomy does not replace or deprecate any tag.

---

## 7. Tag Vocabularies

All tag dimensions use **closed vocabularies**. Only the values listed below are valid. No other values are permitted.

### 7.1 Material Tags

Classifies the primary physical substances an entity produces or transforms. Assign tags for substances the entity **primarily produces**, not all substances it touches.

| Tag | Definition | Example Entities |
|-----|-----------|-----------------|
| `metals` | Metallic elements and alloys | `metals.copper-bronze`, `metals.iron-steel` |
| `silicon` | Silicon and silicon compounds | `silicon.mg-si-production`, `silicon.purification` |
| `glass` | Amorphous silica-based materials | `glass.basic`, `glass.advanced` |
| `ceramics` | Crystalline inorganic non-metals | `ceramics`, `ceramics.pottery` |
| `polymers` | Organic macromolecular materials | `polymers`, `polymers.thermosets` |
| `chemicals` | Industrial chemicals, acids, alkalis | `chemistry.acids`, `chemistry.alkalis` |
| `wood` | Lumber, timber, wooden implements | `foundations.tools-basic` |
| `stone` | Stone and mineral materials | `foundations.tools-basic` |
| `clay` | Clay and earthen materials | `ceramics.pottery` |
| `fibers` | Natural and synthetic fibers | `textiles`, `polymers.composites` |
| `gases` | Industrial and specialty gases | `gas-handling`, `chemistry.air-separation` |
| `water` | Water supply, purification, hydraulic systems | `health` |
| `biomass` | Plant and animal-derived materials | `foundations.food-agriculture`, `chemistry` |

**Rules:**
- 0-3 material tags per entity. Most have exactly one.
- Domain-level entities inherit the union of their children's material tags.

### 7.2 Capability Tags

Classifies the primary functional capability an entity provides. Assign for the entity's **primary functional output**, not secondary benefits.

| Tag | Definition | Example Entities |
|-----|-----------|-----------------|
| `energy` | Power generation, conversion, distribution | `energy`, `energy.steam-power`, `energy.electricity` |
| `precision` | Precision manufacturing, metrology | `machine-tools`, `measurement.precision-metrology` |
| `computing` | Calculation, automation, data processing | `computing`, `vlsi-scaling.eda-design` |
| `transport` | Movement of materials, people, information | `transport`, `transport.aviation` |
| `health` | Medical, sanitation, safety | `health` |
| `measurement` | Sensors, instruments, calibration | `measurement`, `optics.inspection` |
| `cooling` | Refrigeration, thermal management | `energy.storage` |
| `vacuum` | Vacuum systems, controlled atmospheres | `gas-handling.vacuum` |
| `optics` | Lenses, microscopy, lithographic imaging | `optics.inspection`, `vlsi-scaling.advanced-lithography` |
| `construction` | Building, structural engineering | `chemistry.cement`, `transport` |

**Rules:**
- 0-2 capability tags per entity.
- Domain-level entities may have multiple capability tags reflecting breadth.

### 7.3 Era Tags

Classifies the historical era an entity first becomes achievable. Each entity has exactly one era tag.

| Tag | Approximate Period | Characteristic Technologies |
|-----|-------------------|----------------------------|
| `stone-age` | Years 0-5 | Stone tools, fire, charcoal, basic pottery |
| `copper-age` | Years 5-10 | Copper smelting, simple casting |
| `bronze-age` | Years 5-15 | Bronze alloying, improved casting |
| `iron-age` | Years 5-25 | Iron smelting, steel, forge welding |
| `industrial` | Years 15-40 | Steam power, machine tools, bulk chemistry |
| `electronic` | Years 30-70 | Electricity, silicon, basic semiconductors |
| `semiconductor` | Years 40-100 | Photolithography, IC fabrication, VLSI |
| `advanced` | Years 70-200+ | EUV lithography, GPUs, advanced packaging |

**Rules:**
- Each entity has exactly one era tag: the earliest era in which it becomes achievable.
- Era tags are assigned at the capability/process level. Domain entities take the earliest era among their children.
- Era boundaries are approximate, not hard cutoffs.

### 7.4 Lifecycle Tags

Classifies the material lifecycle role of an entity. Optional on all entities.

| Tag | Definition | Example Entities |
|-----|-----------|-----------------|
| `waste-source` | Primary output is a waste or byproduct stream | Blast furnace (slag), combustion (ash) |
| `waste-sink` | Accepts waste/byproduct streams as input | `chemistry.cement` (accepts slag), `chemistry.alkalis` (accepts wood ash) |
| `recyclable` | Output material can be recovered and reprocessed | `glass.basic` (glass cullet), `metals.iron-steel` (scrap steel) |
| `recycled-feedstock` | Specifically processes reclaimed/recycled material | Electric arc furnace (scrap steel feed) |
| `closed-loop` | Output material returns to the same process chain | Aluminum recycling, solvent recovery |

**Rules:**
- 0-5 lifecycle tags per entity. Having none is valid.
- `waste-source` and `waste-sink` may coexist on the same entity.
- `recyclable` and `recycled-feedstock` are complementary: recyclable marks what CAN be recovered; recycled-feedstock marks what IS recovered.
- `closed-loop` implies `recyclable`. If `closed-loop` is present, `recyclable` SHOULD also be present.
- Domain-level entities inherit the union of their children's lifecycle tags.

---

## 8. Edge Semantics

### 8.1 Direction Convention

Edges use `from`/`to` naming: `from` is the dependent (the thing that needs something), `to` is the prerequisite (the thing needed first).

```
from ──depends on──▶ to
```

Example: `{ "from": "metals", "to": "foundations" }` means metals requires foundations.

### 8.2 Edge Types

Every edge carries a `type` field with exactly one of two values:

#### `material`

The prerequisite provides a physical substance consumed or transformed by the dependent. The substance is used up, incorporated into a product, or chemically altered.

**Test:** Does the prerequisite produce a substance that the dependent consumes as feedstock, fuel, or reagent?

| Edge | Why `material` |
|------|---------------|
| `silicon.mg-si-production` → `mining` | Quartz is consumed in carbothermic reduction |
| `machine-tools.casting` → `metals.iron-steel` | Iron/steel is melted and cast, consumed |
| `chemistry.acids` → `silicon.basic-devices` | Acid chemically reacts during etching |

#### `tool`

The prerequisite provides reusable equipment, infrastructure, or capability that the dependent employs without consuming it.

**Test:** Does the prerequisite provide a reusable apparatus or enabling capability?

| Edge | Why `tool` |
|------|-----------|
| `machine-tools` → `metals` | Lathes and mills persist, reusable |
| `energy.electricity` → `chemistry.distillation` | Electric motors persist |
| `gas-handling.vacuum` → `silicon.basic-devices` | Vacuum chamber is reusable infrastructure |

### 8.3 Ambiguity Rule

Some edges fit both categories. Steel is consumed to build a boiler (material), but the boiler becomes reusable infrastructure (tool).

**Rule: When an edge could be both `material` and `tool`, classify it as `tool`.**

Rationale: The enduring infrastructure aspect dominates in dependency analysis. The existence of a forge, lathe, or kiln matters more than the consumable inputs, which are tracked through the `outputs` field.

---

## 9. Product Model

### 9.1 Outputs as Product Tokens

Every entity's `outputs` array lists tokens representing the materials, components, and capabilities it produces. These tokens are Product references.

```json
{
  "id": "metals.iron-steel",
  "outputs": ["wrought_iron", "steel", "iron_bloom", "heat_treated_steel"]
}
```

### 9.2 Product Entity Extraction

In the per-entity file layout (Section 3.2), each output token becomes a first-class Product entity:

```json
{
  "@context": "context.jsonld",
  "id": "steel",
  "type": "Product",
  "name": "Steel",
  "producedBy": "metals.iron-steel"
}
```

### 9.3 Product-Dependency Linkage

Dependency edges connect entities, not products directly. A `material` edge from entity A to entity B indicates that A consumes one or more products from B's `outputs`. The specific product is implicit: if A depends on `metals.iron-steel` via a `material` edge, A consumes `wrought_iron`, `steel`, or another output from that entity.

Future versions of this standard may introduce explicit `consumes`/`produces` properties on edges to link specific products.

### 9.4 Product Lifecycle

Products inherit lifecycle characteristics from their producing entity. If `metals.iron-steel` has `lifecycle: ["recyclable"]`, then the products `wrought_iron` and `steel` are recyclable.

---

## 10. Validation Rules

### 10.1 DAG Constraint

The subgraph formed by edges where `flow` is `"primary"` must be a directed acyclic graph. A cycle would mean entity A requires B which requires A, which is physically impossible in a bootstrap scenario.

Edges with `flow` values `"byproduct-reuse"`, `"waste-recovery"`, or `"recycling-loop"` are **exempt** from the DAG constraint. These represent circular material feedback loops (e.g., scrap steel feeding back into steel production), not dependency cycles. The recycling pathway exists only after initial production.

### 10.2 Cross-Reference Integrity

- Every `from` value in edges MUST reference an existing entity ID.
- Every `to` value in edges MUST reference an existing entity ID.
- Every `parent` value (when non-null) MUST reference an existing entity ID.
- No self-loops: `from` must differ from `to`.
- No duplicate edges: each (`from`, `to`) pair must be unique.

### 10.3 Tag Validation

- Every entity MUST have a `tags` object.
- `tags.material` values MUST come from the closed vocabulary (Section 7.1).
- `tags.capability` values MUST come from the closed vocabulary (Section 7.2).
- `tags.era` MUST be exactly one value from the closed vocabulary (Section 7.3).
- `tags.lifecycle` values, if present, MUST come from the closed vocabulary (Section 7.4).
- Boolean tags in `tags` MUST match the top-level boolean fields.

### 10.4 Edge Type Validation

- Every edge MUST have a `type` field.
- `type` MUST be `"material"` or `"tool"`.
- The value `"required"` is retired and invalid.

### 10.5 Flow Validation

- Every edge MUST have a `flow` field.
- `flow` MUST be one of: `"primary"`, `"byproduct-reuse"`, `"waste-recovery"`, `"recycling-loop"`.
- Edges with `flow: "byproduct-reuse"` SHOULD reference a `from` entity with `lifecycle: ["waste-sink"]` and a `to` entity with `lifecycle: ["waste-source"]`. This is advisory (SHOULD), not enforced.
- Edges with `flow: "waste-recovery"` or `"recycling-loop"` SHOULD reference entities with appropriate lifecycle tags. Advisory.

### 10.6 Taxonomy Validation

- `taxonomy` is optional. Entities without it are valid.
- If present, `taxonomy` MUST be a non-empty array of strings.
- Each string MUST contain at least one dot (two or more segments).
- Each segment MUST match `[a-z][a-z0-9-]*` (kebab-case, lowercase).
- The first segment MUST be one of: `biomass`, `mineral`, `synthetic`.
- No duplicate values within a single entity's `taxonomy` array.

### 10.7 SIK Placement Test (Governance Rule)

The **SIK** (Shared Infrastructure & Knowledge) test determines domain boundaries. It is a governance rule, not an automated validation check.

A set of technologies belongs in the same domain if and only if **all three** conditions hold:

1. **Physical Infrastructure Overlap >50%**: The technologies share more than half their physical infrastructure (buildings, equipment, utilities, supply chains).
2. **Knowledge Base Overlap >50%**: Practitioners share more than half their theoretical and practical knowledge.
3. **Practitioner Profile Overlap >50%**: Skills, training, and working methods are substantially the same. A practitioner trained in one sub-area could transition to another with reasonable retraining (under one year).

**Split Rule:** When identifiable subgroups share less than 50% infrastructure with the rest, consider splitting. The subgroup must be large enough to form its own domain (minimum: 2-3 capabilities with at least 1 process each).

**Override Conditions:**
1. **Inter-domain coupling override**: If splitting would create tight circular dependencies between domains, keep them together despite low SIK overlap.
2. **Bootstrap stage override**: Technologies tightly coupled in the bootstrap sequence may be grouped despite moderate SIK divergence.

Both overrides must be documented with justification when applied.

**Worked Example:** Should glass production stay in `metals`?
- Infrastructure overlap: ~60% (kilns, furnaces)
- Knowledge overlap: ~30% (glass chemistry is distinct from smelting)
- Practitioner overlap: ~20% (glass blowers and smelters are different trades)
- Result: Below 50% on two of three dimensions. Glass is a split candidate. Promoted to its own domain when it accumulated enough capabilities.

---

## 11. JSON-LD Context

### 11.1 Purpose

The `context.jsonld` file maps every JSON key to a formal IRI under the `techtree:` URI scheme. This gives the data machine-readable semantics without requiring OWL imports or external ontology resolution.

### 11.2 The `techtree:` Scheme

`techtree:` is a custom URI scheme. It does not resolve to HTTP URLs. It serves as a namespace for all terms defined by this standard.

```
techtree:Domain          → Entity type: Domain
techtree:Process         → Entity type: Process
techtree:hasOutput       → Property: links entity to its products
techtree:dependsOn       → Property: links dependent to prerequisite
techtree:materialTag     → Property: material classification tag
techtree:era             → Property: historical era classification
```

### 11.3 Context Structure

The context file defines:

1. **`@base`**: `techtree:` - all relative IRIs resolve against this base
2. **`@vocab`**: `techtree:` - unmapped terms default to this vocabulary
3. **Type mappings**: `"Domain": "techtree:Domain"`, etc.
4. **Property mappings**: Each JSON key maps to a `techtree:` IRI with a specified datatype
5. **ID and type**: `"id": "@id"`, `"type": "@type"` - standard JSON-LD keywords

### 11.4 EMMO Alignment

The context file documents vocabulary-level alignments with EMMO:

```
techtree:hasInput  ~ EMMO hasInput   (EMMO_36e69413...)
techtree:hasOutput ~ EMMO hasOutput  (EMMO_c4bace1d...)
techtree:Process   ~ EMMO Process    (EMMO_43e9a05d...)
techtree:Product   ~ EMMO ManufacturedObject (EMMO_ec7464a9...)
```

These are NOT OWL imports. No ontologies are imported. The alignments exist as documentation for engineers who want to map TechTree concepts into EMMO-based toolchains.

### 11.5 openLCA Compatibility

openLCA uses JSON-LD natively with `@type` and `@id` annotations. The TechTree context is compatible with openLCA's serialization conventions. A conforming TechTree dataset can be transformed into openLCA's `Process` entity format by mapping:

- `techtree:Process` → openLCA `Process`
- `techtree:hasOutput` → openLCA `Exchange` (output)
- `techtree:dependsOn` → openLCA `ProcessLink`

Full round-trip fidelity is a design goal.

---

## 12. Extensibility

### 12.1 Adding New Domains

New domains can be added without modifying this standard, provided they pass the SIK Placement Test (Section 10.7). Steps:

1. Define the domain entity with a new single-segment kebab-case ID.
2. Add at least 2-3 capabilities, each with at least 1 process.
3. Classify all entities using existing tag vocabularies.
4. Run validation to confirm DAG integrity and cross-reference consistency.
5. Document the SIK test justification.

### 12.2 Adding New Properties

New properties can be added as optional fields without breaking conformance. Conforming implementations MUST ignore properties they do not recognize.

To add a property that affects conformance (i.e., becomes a MUST requirement), a new version of this standard is required (see Section 13).

### 12.3 Adding New Tag Values

Tag vocabularies are **closed sets**. Adding new values requires a standard version update. The process is intentionally heavyweight to prevent vocabulary drift.

To propose a new tag value:
1. Document the value, its definition, and example entities.
2. Demonstrate that existing tag values do not adequately cover the use case.
3. Submit as a minor version update (see Section 13).

### 12.4 Provider-Specific Extensions

Following OPTIMADE's model, implementations MAY define provider-specific properties using namespaced prefixes:

```json
{
  "id": "metals.iron-steel",
  "acme:customField": "value"
}
```

Providers MUST use a prefix that identifies them (e.g., `acme:`). The prefix MUST NOT conflict with `techtree:` or `xsd:`. Conforming validators MUST ignore unrecognized prefixed properties.

### 12.5 Taxonomy Extensions

New branches beneath existing taxonomy roots (`biomass`, `mineral`, `synthetic`) may be created freely without a spec update. New root values require a standard version update.

---

## 13. Versioning

### 13.1 Semantic Versioning

This standard uses semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes. A conforming file under version N is not conforming under version N+1 without modification. Examples: removing a required property, changing a closed vocabulary, altering edge semantics.
- **MINOR**: Additive changes. New optional properties, new tag values, new entity types. A conforming file under version N remains conforming under version N+1. Example: adding a new era tag.
- **PATCH**: Clarifications, error corrections, documentation improvements. No changes to data semantics.

### 13.2 Version Identifier

The standard version is identified by:

1. A human-readable version string in this document's header (e.g., `1.0.0-draft`)
2. A `$schema` field in data files referencing the standard version (e.g., `"bootciv-nodes-v1"`)

### 13.3 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0-draft | 2026-05-27 | Initial specification. Extracted and restructured from schema-spec.md (710 lines). Added conformance, entity types, JSON-LD context, prior art, versioning sections. |

---

## 14. Prior Art

### 14.1 EMMO (Elementary Multiperspective Material Ontology)

EMMO is an ontology created by the European Materials Modelling Council (EMMC) that provides a formal way to describe the fundamental concepts of physics, chemistry, and materials science. It is structured in shells extending from fundamental concepts to application domains, with a taxonomy that is itself a rooted directed acyclic graph.

EMMO introduces the concept of direct parthood, a non-transitive mereological relation that enables multi-scale granularity descriptions. This is relevant to the TechTree because industrial processes span multiple scales, from atomic (silicon crystal growth) to macroscopic (bridge construction).

**Key lesson for this standard:** EMMO demonstrates that a materials ontology can be both formally rigorous and practically useful. TechTree's vocabulary-level alignment with EMMO concepts (Process, ManufacturedObject, hasInput, hasOutput) allows engineers to map TechTree data into EMMO-based toolchains without committing to full OWL reasoning.

### 14.2 GPO (Battery Data Ontology)

GPO is an EMMO domain ontology for battery data. It demonstrates how a general-purpose materials ontology can be extended for a specific domain. TechTree uses a similar pattern: the core standard defines general entity types and tag vocabularies, while individual domains (metals, silicon, energy) provide specific content.

### 14.3 CEON (Circular Economy Ontology Network)

CEON addresses circular economy concepts: waste streams, recycling pathways, material recovery. TechTree's lifecycle tags (`waste-source`, `waste-sink`, `recyclable`, `recycled-feedstock`, `closed-loop`) and flow qualifiers (`byproduct-reuse`, `waste-recovery`, `recycling-loop`) address similar concerns at a coarser granularity. Where CEON might model the specific chemical composition of a waste stream, TechTree tags the process that generates it.

### 14.4 openLCA

openLCA is a life cycle assessment (LCA) software tool that uses JSON-LD as its native data exchange format. The openLCA schema defines entity types like `Process`, `Flow`, `Exchange`, and `ProductSystem`, stored as per-entity JSON files in a zip archive.

TechTree's serialization is designed for openLCA compatibility. The per-entity file layout (Section 3.2) mirrors openLCA's folder structure. The JSON-LD context (Section 11) uses the same `@type`/`@id` annotations. Full round-trip conversion between TechTree entities and openLCA processes is a design goal.

### 14.5 OPTIMADE

OPTIMADE is an API specification for materials science databases. It defines conformance levels (MUST for required properties, SHOULD for recommended ones), closed property vocabularies, and a provider-specific extension mechanism using namespaced prefixes.

TechTree borrows three structural ideas from OPTIMADE:
1. **Conformance levels**: MUST/SHOULD language for data validation.
2. **Closed vocabularies**: Tag values are fixed sets, not free text.
3. **Provider-specific extensions**: Namespaced properties for implementation-specific metadata.

### 14.6 STEP (ISO 10303)

STEP is a family of ISO standards for product data exchange, particularly 3D geometry and tolerances. STEP handles the *shape* of products; TechTree handles the *process* of making them. A complete digital twin of an industrial supply chain would need both: STEP for what the product looks like, TechTree for what capabilities are needed to produce it.

---

## Appendix A: Complete Entity Example

This appendix shows a complete entity record with all populated fields, drawn from the reference implementation.

```json
{
  "@context": "context.jsonld",
  "id": "metals.iron-steel",
  "type": "Capability",
  "name": "Iron & Steel Production",
  "level": "capability",
  "parent": "metals",
  "description": "Bloomery smelting of iron ore at 1200-1400C producing wrought iron, carburization for steel, and crucible steel (Wootz method). Heat treatment: annealing, quenching, and tempering. This is the critical metallurgical capability that enables all subsequent domains.",
  "timeline": "Years 5-15",
  "outputs": ["wrought_iron", "steel", "iron_bloom", "heat_treated_steel"],
  "critical": true,
  "critical_note": "Iron and steel are essential for machine tool beds, cutting tools, boilers, generators, and all precision machinery",
  "early_win": false,
  "pinnacle": false,
  "taxonomy": ["mineral.ore.iron", "synthetic.alloy.steel"],
  "tags": {
    "material": ["metals"],
    "capability": [],
    "era": "iron-age",
    "lifecycle": ["waste-source", "recyclable"],
    "critical": true,
    "early-win": false,
    "pinnacle": false
  }
}
```

---

## Appendix B: Complete Edge Examples

### B.1 Material Edge (Primary Flow)

```json
{
  "from": "machine-tools.casting",
  "to": "metals.iron-steel",
  "type": "material",
  "flow": "primary"
}
```

The casting foundry consumes iron/steel as raw material. Standard forward supply chain.

### B.2 Tool Edge (Primary Flow)

```json
{
  "from": "energy.steam-power",
  "to": "machine-tools",
  "type": "tool",
  "flow": "primary"
}
```

Steam power needs machine tools to build cylinders and pistons. Machine tools are reusable infrastructure.

### B.3 Material Edge (Byproduct Reuse)

```json
{
  "from": "chemistry.cement",
  "to": "metals.iron-steel.blast-furnace",
  "type": "material",
  "flow": "byproduct-reuse"
}
```

Cement production uses blast furnace slag, a secondary output of iron smelting. Without this edge, the slag would be landfilled.

### B.4 Material Edge (Recycling Loop)

```json
{
  "from": "metals.aluminum",
  "to": "metals.aluminum",
  "type": "material",
  "flow": "recycling-loop"
}
```

Aluminum scrap is melted and recast into the same alloy specification. The DAG constraint does not apply to this edge because the recycling pathway exists only after initial aluminum production.

---

## Appendix C: Glossary

| Term | Definition |
|------|-----------|
| **Capability** | Major skill or process family within a Domain. One dot in ID. |
| **Closed vocabulary** | A fixed set of permitted values. No other values are valid. |
| **Critical** | Boolean flag. True if downstream capabilities are blocked without this entity. |
| **DAG** | Directed Acyclic Graph. The primary edges must form a DAG. |
| **Dependency** | A directed edge representing a requirement relationship. |
| **Domain** | Top-level technology area. Zero dots in ID. Determined by the SIK test. |
| **Early win** | Boolean flag. True if the entity produces high-value output early, creating a feedback loop. |
| **Edge type** | Either `material` (consumed substance) or `tool` (reusable infrastructure). |
| **Entity** | A node in the graph. One of: Domain, Capability, Process, Product. |
| **Era tag** | Historical era classification. Exactly one per entity. |
| **Flow qualifier** | Circular economy role of an edge: `primary`, `byproduct-reuse`, `waste-recovery`, or `recycling-loop`. |
| **Lifecycle tag** | Optional classification of an entity's role in circular material flows. |
| **Material tag** | Classification of the primary physical substances an entity produces. |
| **Organizing axis** | The principle by which capabilities are arranged within a domain (chronological, process chain, functional, etc.). |
| **Pinnacle** | Boolean flag. True if the entity is an end-goal requiring a mature ecosystem. |
| **Process** | Specific technique or operation. Two or more dots in ID. |
| **Product** | Physical material or artifact produced by an entity. Extracted from `outputs`. |
| **SIK test** | Shared Infrastructure & Knowledge test. Determines domain boundaries. |
| **Taxonomy** | Optional hierarchical classification by material origin using dotted strings. |
| **techtree:** | Custom URI scheme for all terms defined by this standard. |
| **Tool edge** | Dependency where the prerequisite provides reusable equipment or infrastructure. |

---

## Appendix D: Validation Checklist

A summary of all validation rules for quick reference. Each rule maps to a section in this specification.

| # | Rule | Level | Section |
|---|------|-------|---------|
| 1 | Every entity has required fields for its type | MUST | 5.1 |
| 2 | `level` is consistent with dot count in ID | MUST | 5.1 |
| 3 | `parent` is consistent with ID | MUST | 5.1 |
| 4 | `parent` references an existing entity | MUST | 10.2 |
| 5 | `tags.material` values from closed vocabulary | MUST | 7.1 |
| 6 | `tags.capability` values from closed vocabulary | MUST | 7.2 |
| 7 | `tags.era` is exactly one value from closed vocabulary | MUST | 7.3 |
| 8 | `tags.lifecycle` values from closed vocabulary | MUST | 7.4 |
| 9 | Boolean tags match top-level fields | MUST | 5.3 |
| 10 | Every edge has `type` as `"material"` or `"tool"` | MUST | 8.2 |
| 11 | Every edge has `flow` from defined set | MUST | 5.5 |
| 12 | Primary-edge subgraph is a DAG | MUST | 10.1 |
| 13 | Edge `from`/`to` reference existing entities | MUST | 10.2 |
| 14 | No self-loops in edges | MUST | 10.2 |
| 15 | No duplicate edges | MUST | 10.2 |
| 16 | `taxonomy` segments are valid kebab-case | MUST | 10.6 |
| 17 | `taxonomy` roots from closed set | MUST | 6.3 |
| 18 | `closed-loop` implies `recyclable` in lifecycle | SHOULD | 7.4 |
| 19 | Circular edges reference appropriate lifecycle tags | SHOULD | 10.5 |
| 20 | Domain boundaries pass SIK test | SHOULD | 10.7 |
