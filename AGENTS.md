# TECH-TREE-BOOTSTRAP KNOWLEDGE BASE

**Generated:** 2026-05-16
**Commit:** ef4ee29
**Branch:** master

## OVERVIEW

9-phase core tech tree + 14 parallel side quests documenting civilization bootstrap from stone tools to GPU manufacturing. Content is Markdown prose + Mermaid flowcharts + structured JSON/YAML data.

## STRUCTURE

```
tech-tree-bootstrap/
├── docs/
│   ├── core-tech-tree/     # 9 phases: phase-01-foundations.md → phase-09-scaling.md
│   ├── side-quests/        # 14 SQs: sq-01-knowledge-preservation.md → sq-14-polymers-composites.md
│   └── supporting/         # checklist, dependencies, resources, polymer deep-dives
├── diagrams/mermaid/
│   ├── phases/             # 9 .mmd flowcharts (one per phase)
│   ├── side-quests/        # 19 .mmd flowcharts (SQ overview + per-SQ + polymer sub-diagrams)
│   └── overview.mmd        # Master dependency graph
├── data/                   # dependencies.json, checklist.yaml, resources.json
└── scripts/                # validate.sh, render-mermaid.sh
```

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Add/edit a phase doc | `docs/core-tech-tree/phase-XX-name.md` | Must also update corresponding `.mmd` in `diagrams/mermaid/phases/` |
| Add/edit a side quest | `docs/side-quests/sq-XX-name.md` | Must also update `.mmd` in `diagrams/mermaid/side-quests/` |
| Add a new side quest | `docs/side-quests/` + `validate.sh` loop | Must manually add filename to validate.sh line 54 |
| Update dependency graph | `data/dependencies.json` + `diagrams/mermaid/overview.mmd` | Keep in sync |
| Edit structured checklist | `data/checklist.yaml` + `docs/supporting/minimum-viable-checklist.md` | Keep in sync |
| Cross-phase dependencies | `docs/supporting/dependencies.md` | Matrix of all phase-to-phase deps |
| Resource catalog | `data/resources.json` + `docs/supporting/resources.md` | Raw materials with criticality |

## CONVENTIONS

- File naming: `phase-XX-name.md` / `sq-XX-name.md` (kebab-case, zero-padded numbers)
- Diagram naming matches doc naming (except phase-08: doc=photolithography, diagram=ic-fabrication)
- Mermaid init block: `%%{init: {"flowchart": {"defaultRenderer": "elk", "htmlLabels": true}}}%%`
- Data IDs: `phase-XX` and `sq-XX` in JSON/YAML
- Priority values: `critical`, `critical_for_fab`, `high`, `medium-high`, `medium`
- All links between docs are relative Markdown links
- Prose style: clear, direct, avoid jargon, include dependency chains and safety concerns

## ANTI-PATTERNS (THIS PROJECT)

- **DO NOT** modify docs without updating the matching diagram (and vice versa)
- **DO NOT** commit to `diagrams/rendered/` — it's gitignored
- **DO NOT** forget to update `validate.sh` when adding a new side quest file
- **DO NOT** use absolute links between docs — always relative

## COMMANDS

```bash
# Validate structure (checks all expected files exist, counts .mmd files)
bash scripts/validate.sh

# Render all diagrams to SVG (requires: npm i -g @mermaid-js/mermaid-cli)
bash scripts/render-mermaid.sh svg
```

## NOTES

- Phase 08 naming mismatch: doc=`phase-08-photolithography.md`, diagram=`phase-08-ic-fabrication.mmd`
- `validate.sh` side-quest loop (line 54) is hardcoded — new entries need manual addition
- `checklist.yaml` is 404 lines with tier-based progression tracking (all items `completed: false`)
- Safety directives (NEVER/ALWAYS) scattered across 8+ docs for hazardous materials (HF acid, acetylene, silane, etc.)
- 1 open TODO: `docs/supporting/polymer-thermosets.md:76` — verify non-phosgene isocyanate routes
