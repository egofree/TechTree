# TECH-TREE-BOOTSTRAP KNOWLEDGE BASE

**Generated:** 2026-05-22
**Commit:** latest
**Branch:** main

**Stats:** 207 nodes | 432 edges | 24 domains | 25 Mermaid diagrams | 25 D2 diagrams | 7,097 glossary terms

## OVERVIEW

Unified hierarchical ontology for bootstrapping industrial civilization from stone tools to GPU manufacturing. Content is Markdown prose + Mermaid flowcharts (auto-generated) + structured JSON/YAML data.

## STRUCTURE

```
tech-tree-bootstrap/
├── docs/
│   ├── index.md            # Unified entry point
│   ├── {domain}/           # domain directories with capability .md files
│   └── supporting/         # Schema spec, dependencies, checklist, resources
├── diagrams/mermaid/
│   ├── overview.mmd        # Master dependency graph
│   └── {domain}.mmd        # domain flowcharts (auto-generated)
├── data/                   # nodes.json, edges.json, glossary.json, checklist.yaml, resources.json
├── scripts/                # Shell + Python toolchain (see COMMANDS)
└── site/                   # Generated static site (HTML, tracked in git)
```

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Domain content | `docs/{domain}/` | domains with capability .md files |
| Mermaid diagrams | `diagrams/mermaid/` | Auto-generated from data, DO NOT hand-edit |
| Structured data | `data/` | nodes.json, edges.json, checklist.yaml, resources.json, plants.json, glossary.json |
| Diagram generator | `scripts/generate-diagrams.sh` | Auto-generates all .mmd from data |
| Data validation | `scripts/validate.sh` | 17 checks: DAG, cross-refs, tags, edge types, hierarchy, taxonomy, glossary |
| Site builder | `scripts/build-site.sh` | Generates `site/` from docs + data |
| Site validation | `scripts/validate-site.sh` | Checks links, offline-first compliance |
| Schema reference | `docs/supporting/schema-spec.md` | Normative spec for tags, edge types, SIK test |

## CONVENTIONS

- Node IDs use dotted hierarchical format: `domain.capability.process`
- Edge types: `material` (consumed substance) or `tool` (reusable infrastructure). No other values
- Tags: `material[]`, `capability[]`, `era`, `critical`, `early-win`, `pinnacle` on every node
- Tag vocabularies are closed sets (12 materials, 10 capabilities, 8 eras — see schema-spec.md)
- Diagrams are auto-generated. Run `generate-diagrams.sh` after data changes, never hand-edit .mmd files
- Domain directories and file names: lowercase, hyphenated (kebab-case)
- Data format: JSON (machine data) + YAML (human config)
- Content metadata: blockquote headers (`> **Field**: value`), NOT YAML frontmatter
- Domain index.md template: H1 + "Capabilities in this domain:" + bullet list + back link
- All links between docs are relative Markdown links
- Prose style: clear, direct, avoid jargon, include dependency chains and safety concerns
- Site is offline-first: no external URLs, no fetch(), no ES modules (enforced by validate-site.sh)
- Mermaid init block: `%%{init: {"flowchart": {"defaultRenderer": "elk", "htmlLabels": true}}}%%`
- Edge rendering: material=solid (`-->`), tool=dashed (`-.->`)

## ANTI-PATTERNS (THIS PROJECT)

- **DO NOT** hand-edit `.mmd` files. Regenerate with `generate-diagrams.sh`
- **DO NOT** add phase/SQ terminology (old naming scheme, no longer used)
- **DO NOT** modify `supporting/` without updating corresponding data files
- **DO NOT** commit to `diagrams/rendered/` (gitignored)
- **DO NOT** use `type: "required"` in edges.json — retired, use `"material"` or `"tool"`
- **DO NOT** add tags outside the controlled vocabulary defined in schema-spec.md
- **DO NOT** create new domains without passing the SIK Placement Test (schema-spec.md §5)

## COMMANDS

```bash
# Auto-generate all Mermaid diagrams from data layer
bash scripts/generate-diagrams.sh

# Validate repo structure (data-driven, 17 checks including glossary)
bash scripts/validate.sh

# Build static site to site/
bash scripts/build-site.sh

# Validate site build (links, offline-first)
bash scripts/validate-site.sh

# Render all diagrams to SVG (requires: npm i -g @mermaid-js/mermaid-cli)
bash scripts/render-mermaid.sh svg
```

## NOTES

- Data files in `data/` define the complete node graph, edges, glossary, and supporting catalogs.
- Plants domain added via config-driven Wikipedia crawler: 86 species catalog, 19 tech-tree nodes, 21 edges
- All diagrams auto-generated from `data/nodes.json` + `data/edges.json`
- `validate.sh` is data-driven. Reads nodes/edges to check cross-references and DAG integrity
- Schema specification: `docs/supporting/schema-spec.md` defines tag taxonomy, edge type rules, SIK placement test
- SIK Placement Test determines domain boundaries (infrastructure/knowledge/practitioner overlap >50%)
- `site/` is generated output (gitignored in inner repo since commit 8322222)
- `tech-tree-bootstrap/` has its own `.git/` — independent repo, NOT a submodule of parent
- Scripts use bash (`set -euo pipefail`) + Python (generate-pages.py with lib/build_utils.py)
- No CI/CD. Inner repo has public GitHub remote. Manual workflow.
