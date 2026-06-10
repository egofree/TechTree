# TECH-TREE-BOOTSTRAP

Unified hierarchical ontology for bootstrapping industrial civilization from stone tools to GPU manufacturing. Content is Markdown prose + auto-generated Mermaid/D2 flowcharts + structured JSON-LD data.

## STRUCTURE

```
tech-tree-bootstrap/
├── data/
│   ├── context.jsonld         # JSON-LD @context (all term → IRI mappings)
│   ├── schema/                # JSON Schema files (6: entity, domain, capability, process, product, dependency)
│   ├── entities/
│   │   ├── {domain}/          # Per-domain entity .jsonld files (capabilities, processes)
│   │   └── _edges/            # Dependency edges: {from}__{to}.jsonld
│   ├── products/              # Product/material entity .jsonld files
│   ├── archive/               # Old monolithic nodes.json / edges.json (retired)
│   ├── glossary.json          # Auto-generated glossary
│   └── plants.json, resources.json, checklist.yaml
├── docs/
│   ├── index.md               # Entry point
│   ├── {domain}/              # 43 domain directories with capability .md files
│   ├── glossary/              # Auto-generated glossary pages
│   ├── spec/                  # Formal spec (process-knowledge-standard.md) + getting-started guide
│   └── supporting/            # Schema spec, content template, checklists, resources
├── diagrams/
│   ├── mermaid/               # Auto-generated .mmd (DO NOT hand-edit)
│   └── d2/                    # Auto-generated .d2 (DO NOT hand-edit)
├── scripts/                   # Python + bash toolchain (see COMMANDS)
│   └── lib/                   # tt_data.py (data access layer), build_utils.py, templates, etc.
├── tests/                     # Conformance tests: tests/valid/ + tests/invalid/ (50+ fixtures)
├── site/                      # Generated static site (gitignored)
└── Makefile                   # Primary command interface
```

## COMMANDS (use Makefile)

```bash
make validate          # Schema + data integrity (19 checks: DAG, cross-refs, tag vocab, edge types, hierarchy)
make diagrams          # Generate Mermaid diagrams from data
make d2-diagrams       # Generate D2 diagrams from data
make build             # Build offline-first static site to site/
make validate-site     # Validate built site (10 checks: links, offline-first compliance)
make test              # Run conformance test suite (valid/invalid fixtures vs JSON Schema)
make all               # Full pipeline: validate → diagrams → build → validate-site
make wikidata-search   # Search Wikidata for entity Q-IDs, output scored TSV
make wikidata-apply    # Apply approved Q-IDs from reviewed TSV to entity files
make wikidata-enrich   # Build multilingual enrichment cache from Wikidata
```

**Key gotcha:** `make validate` and `make test` require `jsonschema` (`pip install jsonschema`), but it is **not** in `requirements.txt`. The listed deps are `markdown-it-py` and `pyyaml` only.

## DATA MODEL

- **Format:** Per-entity JSON-LD files (not monolithic JSON). Each file references `../../context.jsonld`.
- **Entity types:** `Domain`, `Capability`, `Process`, `Product`, `Dependency`
- **IDs:** Dotted hierarchical kebab-case: `domain.capability.process`
- **Edges:** Individual files in `data/entities/_edges/` named `{from}__{to}.jsonld`
  - `edgeType`: `"material"` (consumed substance) or `"tool"` (reusable infrastructure) — no other values
  - `flow`: `"primary"`, `"byproduct-reuse"`, `"waste-recovery"`, or `"recycling-loop"`
- **Tags:** Closed vocabularies defined in the formal spec §7 (`docs/spec/process-knowledge-standard.md`)
- **Old monolithic files** (`data/archive/nodes.json`, `data/archive/edges.json`) are retired. All scripts now read from per-entity files via `scripts/lib/tt_data.py`.

## CONVENTIONS

- Domain directories and file names: lowercase, hyphenated (kebab-case)
- Data format: JSON-LD per-entity files + YAML for human config (checklist.yaml)
- Content metadata in docs: blockquote headers (`> **Field**: value`), NOT YAML frontmatter
- Domain index.md template: H1 + "Capabilities in this domain:" + bullet list + back link
- All links between docs are relative Markdown links
- Site is offline-first: no external URLs, no fetch(), no ES modules (enforced by validate-site.sh)
- Mermaid init block: `%%{init: {"flowchart": {"defaultRenderer": "elk", "htmlLabels": true}}}%%`
- Edge rendering: material=solid (`-->`), tool=dashed (`-.->`)

## ANTI-PATTERNS

- **DO NOT** hand-edit `.mmd` or `.d2` files. Regenerate with `make diagrams` or `make d2-diagrams`
- **DO NOT** use old monolithic `data/archive/nodes.json` or `edges.json` — they are retired
- **DO NOT** use `type: "required"` in edges — retired, use `"material"` or `"tool"`
- **DO NOT** add tags outside the closed vocabulary defined in the formal spec §7 (`docs/spec/process-knowledge-standard.md`)
- **DO NOT** create new domains without passing the SIK Placement Test (formal spec §10)
- **DO NOT** commit to `site/` or `diagrams/rendered/` (both gitignored)
- **DO NOT** add phase/SQ terminology (old naming scheme, no longer used)

## CI

Manual-trigger only: `.github/workflows/validate.yml` (`workflow_dispatch`). Runs `make validate` + `build-site.sh --no-svg` + `validate-site.sh`. Uses Makefile targets as the entry points.

## WHERE TO LOOK

| Task | Location |
|------|----------|
| Entity data | `data/entities/{domain}/` — per-entity `.jsonld` files |
| Dependency edges | `data/entities/_edges/` — `{from}__{to}.jsonld` |
| JSON Schema | `data/schema/` — 6 schema files for validation |
| Formal spec | `docs/spec/process-knowledge-standard.md` — normative data model spec |
| Getting started | `docs/spec/README.md` — quick-start guide for the data format |
| Domain content | `docs/{domain}/` — Markdown prose with capability `.md` files |
| Schema spec (legacy) | `docs/supporting/schema-spec.md` — older tag taxonomy reference |
| Diagram generator | `scripts/generate-diagrams.py` — Python, reads via `lib/tt_data.py` |
| Data access layer | `scripts/lib/tt_data.py` — used by all Python scripts |
| Conformance tests | `tests/valid/` + `tests/invalid/` — fixture files for schema validation |
