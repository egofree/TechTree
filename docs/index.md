# From Stone to Silicon: Overview

## What Is This?

This project maps the complete dependency chain for bootstrapping modern semiconductor technology (GPUs, solar cells, integrated circuits) from stone-age materials. It assumes a knowledgeable group with documentation, starting in a resource-rich area with access to quartz, iron ore, coal/wood, limestone, etc., but no pre-existing tools or infrastructure.

The sequence draws from:
- Historical development patterns (metallurgy → steam/electricity → chemistry → semiconductors)
- Practical bootstrapping examples (Dave Gingery's machine-shop-from-scrap series)
- Early silicon production methods
- Realities of semiconductor fabrication

## Why This Matters

The bootstrap sequence demonstrates that advanced technology cannot be created in isolation — it requires a vast web of supporting infrastructure, materials, knowledge, and energy. Understanding this dependency chain reveals:

1. Why civilizations develop certain technologies in predictable order
2. What the minimum viable infrastructure looks like for each capability level
3. Where the critical bottlenecks and highest-leverage investments are
4. How parallel development tracks accelerate overall progress

## The Tech Tree at a Glance

| Phase | Name | Timeline | Key Output |
|-------|------|----------|------------|
| 1 | Foundations | Years 0–10 | Food surplus, charcoal, basic tools, kilns |
| 2 | Early Metallurgy | Years 5–15 | Copper, bronze, iron, steel, basic glass |
| 3 | Machine Tools | Years 10–25 | Lathe, shaper, mill, drill press, metrology |
| 4 | Energy Revolution | Years 15–30 | Steam engines, electricity, arc furnaces |
| 5 | Chemical Industry | Years 20–35 | Acids, alkalis, electrolysis, gases |
| 6 | Vacuum & Optics | Years 25–40 | Vacuum pumps, glass apparatus, microscopes |
| 7 | Silicon & Basic Devices | Years 30–50 | MG-Si, crystal growth, solar cells, diodes |
| 8 | Photolithography & ICs | Years 40–70 | Cleanrooms, lithography, basic integrated circuits |
| 9 | VLSI & GPUs | Years 70–200+ | Complex chips, advanced solar, design automation |

**Note**: Timelines overlap significantly. Phases 2–4 run partially in parallel; Phases 5–6 overlap; Phases 7–9 are iterative.

## Core Principles

1. **Iterative bootstrapping**: Crude tools → better tools → precision tools. Every stage improves on the last.
2. **Machine tools as master key**: Precision manufacturing (especially lathes) unlocks everything downstream.
3. **Energy abundance**: Silicon processing and fabrication are extremely energy-intensive. Power must come first.
4. **Parallel tracks**: Agriculture, energy, mechanics, and chemistry develop simultaneously where possible.
5. **Start simple, then scale**: Large-geometry devices before complex logic. Solar-grade silicon before electronic-grade.
6. **Purity escalation**: Trace impurities destroy semiconductor performance. Cleanrooms, pure reagents, and metrology improve iteratively.

## Critical Path

```
Foundations → Metallurgy + Machine Tools (parallel)
Machine Tools + Energy → Chemical Scale + Vacuum/Optics
All above → Silicon Production + Basic Devices (solar cells early)
Silicon + Chemistry + Precision + Cleanrooms → Photolithography + ICs
ICs + Iteration + Compute → VLSI/GPUs + Advanced Solar
```

## Side Quests

The core tech tree is necessary but not sufficient. Nine parallel "side quest" tracks provide the supporting infrastructure that prevents the effort from collapsing:

1. [Knowledge Preservation &amp; Education](side-quests/sq-01-knowledge-preservation.md)
2. [Measurement, Timekeeping &amp; Metrology](side-quests/sq-02-measurement-metrology.md)
3. [Transportation, Logistics &amp; Communication](side-quests/sq-03-transport-logistics.md)
4. [Mechanical Computing &amp; Automation](side-quests/sq-04-mechanical-computing.md)
5. [Public Health &amp; Medicine](side-quests/sq-05-public-health.md)
6. [Specialty Gases, Consumables &amp; Packaging](side-quests/sq-06-gases-packaging-testing.md)
7. [Energy Storage &amp; Diversification](side-quests/sq-07-energy-storage.md)
8. [Advanced Materials](side-quests/sq-08-advanced-materials.md)
9. [Mining Engineering &amp; Extractive Metallurgy](side-quests/sq-11-mining-engineering.md)

## Navigation

- [Core Tech Tree Overview →](core-tech-tree/overview.md)
- [Side Quests Index →](side-quests/index.md)
- [Minimum Viable Civilization Checklist →](supporting/minimum-viable-checklist.md)
- [Dependencies &amp; Resources →](supporting/dependencies.md)
- [Diagram Gallery →](../diagrams/mermaid/)
