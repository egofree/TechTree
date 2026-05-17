# TECH-TREE-BOOTSTRAP KNOWLEDGE BASE

**Generated:** 2026-05-16
**Commit:** ef4ee29
**Branch:** master

## OVERVIEW

Unified hierarchical ontology for bootstrapping industrial civilization from stone tools to GPU manufacturing. Content is Markdown prose + Mermaid flowcharts (auto-generated) + structured JSON/YAML data.

## STRUCTURE

```
tech-tree-bootstrap/
├── docs/
│   ├── index.md            # Unified entry point
│   ├── {domain}/           # 23 domain directories with capability .md files
│   └── supporting/         # Reference materials (checklist, dependencies, resources)
├── diagrams/mermaid/
│   ├── overview.mmd        # Master dependency graph
│   └── {domain}.mmd        # 23 domain flowcharts (auto-generated)
├── data/                   # nodes.json, edges.json, checklist.yaml, resources.json
└── scripts/                # generate-diagrams.sh, validate.sh, render-mermaid.sh
```

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Domain content | `docs/{domain}/` | 23 domains, each with capability .md files |
| Mermaid diagrams | `diagrams/mermaid/` | Auto-generated from data, DO NOT hand-edit |
| Structured data | `data/` | nodes.json (71 nodes), edges.json (115 edges), checklist.yaml, resources.json |
| Diagram generator | `scripts/generate-diagrams.sh` | Auto-generates all .mmd from data |
| Validation | `scripts/validate.sh` | Data-driven, checks cross-refs and DAG integrity |

## CONVENTIONS

- Node IDs use dotted hierarchical format: `domain.capability.process`
- Diagrams are auto-generated. Run `generate-diagrams.sh` after data changes, never hand-edit .mmd files
- Domain directories and file names: lowercase, hyphenated
- Data format: JSON (machine data) + YAML (human config)
- Mermaid init block: `%%{init: {"flowchart": {"defaultRenderer": "elk", "htmlLabels": true}}}%%`
- All links between docs are relative Markdown links
- Prose style: clear, direct, avoid jargon, include dependency chains and safety concerns

## ANTI-PATTERNS (THIS PROJECT)

- **DO NOT** hand-edit `.mmd` files. Regenerate with `generate-diagrams.sh`
- **DO NOT** add phase/SQ terminology (old naming scheme, no longer used)
- **DO NOT** modify `supporting/` without updating corresponding data files
- **DO NOT** commit to `diagrams/rendered/` (gitignored)

## COMMANDS

```bash
# Auto-generate all Mermaid diagrams from data layer
bash scripts/generate-diagrams.sh

# Validate repo structure (data-driven)
bash scripts/validate.sh

# Render all diagrams to SVG (requires: npm i -g @mermaid-js/mermaid-cli)
bash scripts/render-mermaid.sh svg
```

## NOTES

- All diagrams auto-generated from `data/nodes.json` + `data/edges.json`
- `validate.sh` is data-driven. Reads nodes/edges to check cross-references and DAG integrity
- Old `dependencies.json` superseded by `nodes.json` + `edges.json`
- No CI/CD, no remote configured. Purely manual workflow
