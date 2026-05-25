# From Stone to Silicon: Civilization Bootstrap Tech Tree

A structured, visual guide to bootstrapping modern industrial civilization, starting from stone-age materials and reaching high-end semiconductors (GPUs) and solar cells.

This project documents the complete dependency chain from fire and stone tools through metallurgy, machine tools, chemistry, and silicon fabrication to advanced integrated circuits. It includes parallel "side quest" tracks for the supporting infrastructure that makes long-term technological development sustainable across generations.

## Stats

| Metric | Count |
|--------|-------|
| Technology domains | 41 |
| Capability nodes | 317 |
| Dependency edges | 637 |
| Content articles | 257+ |
| Mermaid diagrams | 41 |
| D2 diagrams | 41 |
| Glossary terms | 7,000+ |

## Quick Navigation

- [Overview & Introduction](docs/index.md)
- **Core Path** — stone to GPU:
  - [Foundations](docs/foundations/) · [Metals](docs/metals/) · [Mining](docs/mining/) · [Energy](docs/energy/) · [Machine Tools](docs/machine-tools/) · [Chemistry](docs/chemistry/) · [Silicon](docs/silicon/) · [Photolithography](docs/photolithography/) · [VLSI Scaling](docs/vlsi-scaling/) · [Computing](docs/computing/) · [Electronics](docs/electronics/)
- **Materials**:
  - [Ceramics](docs/ceramics/) · [Glass](docs/glass/) · [Polymers](docs/polymers/) · [Textiles](docs/textiles/) · [Animals](docs/animals/) · [Plants](docs/plants/) · [Petroleum](docs/petroleum/)
- **Process & Precision**:
  - [Vacuum Technology](docs/vacuum/) · [Cryogenics](docs/cryogenics/) · [Cleanrooms](docs/cleanrooms/) · [Ultra-Pure Materials](docs/ultra-pure/) · [Precision Motion](docs/precision-motion/) · [Optics](docs/optics/) · [Measurement](docs/measurement/) · [Quality Control](docs/quality-control/) · [Electrochemistry](docs/electrochemistry/)
- **Infrastructure & Safety**:
  - [Construction](docs/construction/) · [Gas Handling](docs/gas-handling/) · [Water](docs/water/) · [Health](docs/health/) · [EHS](docs/ehs/) · [Automation & Robotics](docs/automation/) · [Mathematics](docs/mathematics/) · [Knowledge](docs/knowledge/)
- **Transport & Communication**:
  - [Transport](docs/transport/) · [Marine](docs/marine/) · [Telecommunications](docs/telecom/)
- **Civilization Sustaining**:
  - [Agriculture](docs/agriculture/) · [Food Processing](docs/food-processing/) · [Defense](docs/defense/)
- [Minimum Viable Civilization Checklist](docs/supporting/minimum-viable-checklist.md)
- [Dependencies & Resources](docs/supporting/dependencies.md)
- [All Mermaid Diagrams](diagrams/mermaid/) · [All D2 Diagrams](diagrams/d2/)

## How to Use

1. Start with the [Overview](docs/index.md) to understand the full scope
2. Explore domains in dependency order (see [overview diagram](diagrams/mermaid/overview.mmd))
3. Use the Mermaid diagrams for visual understanding (render at [mermaid.live](https://mermaid.live))
4. Check the [Checklist](docs/supporting/minimum-viable-checklist.md) for prioritization

## Core Principles

- **Iterative bootstrapping everywhere**: Crude tools make better tools. Each generation improves the last.
- **Precision mechanics as the master key**: Machine tools (especially lathes) unlock everything downstream.
- **Energy abundance is non-negotiable**: Silicon reduction, crystal growth, and fabs are energy-intensive.
- **Parallel tracks with feedback**: Develop agriculture/energy/mechanics/chemistry simultaneously where possible.
- **Start simple and scale**: Large-geometry devices before complex logic. Solar-grade silicon before electronic-grade.
- **Purity and control escalate relentlessly**: Trace impurities destroy semiconductor performance.

## Timeline Perspective

Basic solar cells are achievable within decades of establishing solid machine tools + electricity + chemistry. Full high-end GPU capability (advanced nodes, billions of transistors) likely requires **50–200+ years** even with perfect knowledge, due to purity demands, scale, and ecosystem complexity.

## Project Structure

```
tech-tree-bootstrap/
├── docs/               # Domain-organized content (Markdown prose)
│   ├── index.md        # Unified entry point
│   ├── {domain}/       # One directory per technology domain
│   ├── glossary/       # 7,000+ auto-generated glossary entries
│   ├── images/         # Wikimedia-sourced per-domain images
│   └── supporting/     # Schema spec, checklist, resources
├── data/               # Structured data (JSON/YAML)
│   ├── nodes.json      # 317 technology nodes
│   ├── edges.json      # 637 dependency edges
│   └── glossary.json   # Glossary with relevance ratings
├── diagrams/           # Auto-generated (DO NOT hand-edit)
│   ├── mermaid/        # .mmd flowcharts (41 domains)
│   └── d2/             # .d2 flowcharts (41 domains)
└── scripts/            # Validation, generation, and build tools
```

## Validation

```bash
bash scripts/validate.sh            # 17 checks: DAG, cross-refs, tags, schema
bash scripts/generate-diagrams.sh   # Regenerate Mermaid from data
bash scripts/generate-d2-diagrams.sh # Regenerate D2 from data
```

## License

[CC0 1.0 Universal](LICENSE), a Public Domain dedication.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
