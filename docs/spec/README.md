# TechTree Process Knowledge Standard

Getting-started guide for the [formal specification](process-knowledge-standard.md).

## What Is This?

A JSON-LD data format for representing industrial process knowledge as a directed acyclic graph. Every node is a manufacturing capability (smelting iron, growing silicon crystals, assembling circuit boards), and every edge is a typed dependency: what materials and tools one process needs from another.

The standard aligns vocabulary with EMMO (European Materials Modelling Ontology) and is designed for round-trip compatibility with openLCA's JSON-LD schema. It is not an OWL ontology. There are no imports, no inference rules, just a clean data model with closed tag vocabularies and schema validation.

## Quick Start

A conforming entity file looks like this:

```json
{
  "@context": "../../context.jsonld",
  "@type": "Capability",
  "id": "metals.iron-steel",
  "name": "Iron & Steel Production",
  "level": "capability",
  "parent": "metals",
  "description": "Bloomery smelting of iron ore at 1200-1400C producing wrought iron.",
  "timeline": "Years 5-15",
  "outputs": ["wrought_iron", "steel", "iron_bloom", "heat_treated_steel"],
  "critical": true,
  "early_win": false,
  "pinnacle": false,
  "tags": {
    "material": ["metals"],
    "capability": [],
    "era": "iron-age",
    "critical": true,
    "early-win": false,
    "pinnacle": false
  }
}
```

Key points:

- Every file references `context.jsonld`, which maps all field names to `techtree:` IRIs.
- Entity types are `Domain`, `Capability`, `Process`, `Product`, or `Dependency`.
- IDs use dotted hierarchical kebab-case: `domain.capability.process`.
- Tag values come from closed vocabularies (see the schemas in `data/schema/`).

Edges live in `data/entities/_edges/` and are named `{from}__{to}.jsonld`:

```json
{
  "@context": "../../context.jsonld",
  "@id": "edge/energy__metals",
  "@type": "Dependency",
  "from": "energy",
  "to": "metals",
  "edgeType": "tool",
  "flow": "primary"
}
```

`edgeType` is either `"material"` (consumed substance) or `"tool"` (reusable infrastructure). `flow` is one of `primary`, `byproduct-reuse`, `waste-recovery`, or `recycling-loop`.

## Directory Structure

```
data/
  context.jsonld                # JSON-LD @context (all term definitions)
  schema/
    entity.schema.json          # Base entity schema
    process.schema.json         # Process nodes (2+ dots in ID)
    product.schema.json         # Product entities
    dependency.schema.json      # Edge/dependency entities
    tag-set.schema.json         # Tag vocabulary constraints
  entities/
    {domain}/                   # One directory per domain
      {id}.jsonld               # Capability and process entities
    _edges/                     # Dependency edges
      {from}__{to}.jsonld       # One file per edge
  products/
    {id}.jsonld                 # Product entities
  archive/
    nodes.json                  # Original monolithic node data
    edges.json                  # Original monolithic edge data
tests/                          # 60 conformance tests (valid/ + invalid/)
docs/spec/
  process-knowledge-standard.md # The formal spec (950+ lines)
  README.md                     # This file
```

## Validating Data

Two validation paths, both run from the repo root:

```bash
# Schema + data integrity (19 checks: DAG, cross-refs, tag vocab, edge types)
make validate

# Conformance test suite (60 pytest cases against valid/ and invalid/ fixtures)
make test

# Full pipeline: validate, generate diagrams, build site, validate site
make all
```

`make validate` catches structural problems: broken cross-references, cycles in the primary-flow graph, tags outside the closed vocabulary, wrong entity levels.

`make test` checks that valid files pass schema validation and that invalid files are correctly rejected.

## Extending the Standard

**Adding a new entity.** Create a `.jsonld` file in the right `data/entities/{domain}/` directory. Follow the schema for your entity type. Run `make validate` to check conformance.

**Adding a new edge.** Create `{from}__{to}.jsonld` in `data/entities/_edges/`. Set `edgeType` to `"material"` or `"tool"`, and `flow` to one of the four qualifiers.

**Adding a new domain.** Domains have their own entity schema rules (parent is null, level is "domain"). New domains should pass the SIK Placement Test described in the formal spec (Section 10), which checks that the domain boundary is justified by shared infrastructure, knowledge, and practitioner overlap.

**Adding new tag values.** Tag vocabularies are closed sets defined in the schemas. To add a value, update the relevant `*.schema.json` enum and the formal spec, then run `make test` to confirm nothing breaks.

## Relationships

| Standard | How It Connects |
|----------|----------------|
| **EMMO** | Vocabulary alignment at the IRI level. `techtree:Process` maps to `EMMO_43e9a05d` (Process), `techtree:Product` to `EMMO_ec7464a9` (ManufacturedObject). No OWL imports. |
| **openLCA** | JSON-LD serialization compatibility. Both use `@type` and `@id`. Round-trip conversion is a design goal. |
| **Wikidata** | Entity files can include `wikidataId` (e.g., `"Q362"` for steel) for linking to the broader knowledge graph. |

## License

CC0 1.0 Universal. Public domain. No attribution required.
