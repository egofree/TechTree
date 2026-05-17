# Bootciv Tech Tree

> A complete dependency chain for bootstrapping industrial civilization from stone-age materials to semiconductor manufacturing (GPUs, solar cells, ICs).

The tree maps every technology, material, and process needed to go from fire and stone tools to integrated circuit fabrication. It assumes a knowledgeable group starting in a resource-rich area with access to quartz, iron ore, coal, and limestone, but no pre-existing tools or infrastructure.

## How to Read This Tree

Three levels, top to bottom:

**Domain** — a broad technology area like metallurgy, energy, or silicon. Each domain is a self-contained world of related processes. Domains are the navigation units for this tree.

**Capability** — a specific achievement within a domain, like iron smelting or crystal growth. Capabilities have dotted IDs showing their parent: `metallurgy.iron-steel`, `silicon.crystal-growth`.

**Process** — a detailed method or operation, like Czochralski pulling or blast furnace operation. These carry two dots: `silicon.crystal-growth.cz-pulling`.

Dependencies use these dotted IDs. When photolithography requires silicon, the edge reads `{from: "photolithography", to: "silicon"}`. The full graph lives in [edges.json](../data/edges.json).

## Quick Start Path

The critical path through the tree, in rough chronological order. These domains form the spine: each depends on those before it.

1. **[Foundations](foundations/)** — fire, charcoal, food surplus, kilns, pottery
2. **[Mining](mining/)** — ore access for every metallurgical process
3. **[Metallurgy](metallurgy/)** — copper, bronze, iron, steel, basic glass
4. **[Machine Tools](machine-tools/)** — the master enabler: lathe, shaper, mill, grinder
5. **[Energy](energy/)** — coal, coke, steam engines, electricity, arc furnaces
6. **[Chemistry](chemistry/)** — mineral acids, alkalis, distillation, gas handling
7. **[Vacuum & Optics](vacuum-optics/)** — vacuum pumps, advanced glass, microscopes
8. **[Silicon](silicon/)** — MG-Si production, crystal growth, solar cells
9. **[Photolithography](photolithography/)** — cleanrooms, lithography, IC fabrication
10. **[VLSI Scaling](vlsi-scaling/)** — continuous improvement toward GPUs and advanced solar

Several other domains are also marked critical because their absence blocks downstream work: [knowledge](knowledge/), [textiles](textiles/), [lubricants](lubricants/), [specialty gases](specialty-gases/).

## Domain Listing

| Domain | Capabilities | Critical? | Key Outputs |
|--------|:------------:|:---------:|-------------|
| [Foundations](foundations/) | 4 | Yes | food surplus, charcoal, kilns, pottery |
| [Mining](mining/) | 0 | Yes | copper ore, iron ore, coal, quartz |
| [Metallurgy](metallurgy/) | 5 | | copper, iron, steel, glass, lime |
| [Machine Tools](machine-tools/) | 4 | Yes | lathe, mill, grinder, precision metrology |
| [Energy](energy/) | 7 | | steam engines, electricity, arc furnaces |
| [Chemistry](chemistry/) | 4 | | mineral acids, alkalis, cement, gas handling |
| [Vacuum & Optics](vacuum-optics/) | 3 | | vacuum pumps, fused silica, microscopes |
| [Silicon](silicon/) | 4 | | MG-Si, wafers, solar cells, transistors |
| [Photolithography](photolithography/) | 3 | | cleanrooms, lithography, ICs |
| [VLSI Scaling](vlsi-scaling/) | 4 | | GPUs, advanced solar, EDA tools |
| [Knowledge](knowledge/) | 0 | Yes | writing, printing, education, libraries |
| [Metrology](metrology/) | 0 | | length standards, timekeeping, calibration |
| [Textiles](textiles/) | 0 | Yes | cordage, cloth, rope, drive belts |
| [Lubricants](lubricants/) | 0 | Yes | oils, grease, cutting fluid, vacuum oil |
| [Petrochemicals](petrochemicals/) | 0 | | fuels, solvents, ethanol, coal tar |
| [Computing](computing/) | 0 | | slide rules, calculators, automation |
| [Health](health/) | 0 | | clean water, sanitation, pharmaceuticals |
| [Transport](transport/) | 0 | | roads, railways, telegraph, logistics |
| [Specialty Gases](specialty-gases/) | 4 | Yes | argon, silane, dopant gases, etch gases |
| [Energy Storage](energy-storage/) | 0 | | batteries, grid infrastructure, UPS |
| [Advanced Materials](ceramics/) | 0 | | refractories, technical ceramics |
| [Aircraft](aircraft/) | 0 | | engines, airframes, propellers |
| [Polymers](polymers/) | 5 | | rubber, FR-4, PTFE, fiberglass |

## Dependency Overview

See the [full dependency diagram](../diagrams/mermaid/overview.mmd) for the complete directed acyclic graph of all domain-level dependencies.

## Parallel Opportunities

These domains can begin early, independent of the main critical path. Starting them in parallel accelerates the whole effort.

- **[Knowledge](knowledge/)** — writing, printing, education. Start Day 1. The 50-200 year bootstrapping effort dies with the first generation without knowledge transmission.
- **[Textiles](textiles/)** — fiber, spinning, rope. Start Day 1. Cordage and cloth underpin mining hoists, tool hafting, and power transmission.
- **[Lubricants](lubricants/)** — oils from animal fats and vegetable sources. Start Day 1. Without lubrication, every bearing and slide seizes.
- **[Petrochemicals](petrochemicals/)** — fermentation produces ethanol, acetone, and acetic acid without petroleum. Start Day 1.
- **[Computing](computing/)** — mechanical calculation with slide rules and nomograms. Start as soon as marking tools exist.
- **[Health](health/)** — sanitation, water purification, quarantine protocols. Start Day 1. Skilled workers are the scarcest resource.
- **[Transport](transport/)** — road construction and basic bridges expand the reachable resource base early on.
- **[Metrology](metrology/)** — base unit standards and basic measuring instruments. Start alongside early toolmaking.

## Data Layer

Structured data files backing this tree:

- [nodes.json](../data/nodes.json) — complete node definitions (23 domains, 47 capabilities, 1 process)
- [edges.json](../data/edges.json) — dependency graph (directed, acyclic)
- [checklist.yaml](../data/checklist.yaml) — milestone checklist with progression tracking
- [resources.json](../data/resources.json) — raw material catalog with criticality ratings
- [dependencies.json](../data/dependencies.json) — legacy dependency matrix

## Supporting Docs

- [Minimum Viable Civilization Checklist](supporting/minimum-viable-checklist.md)
- [Dependencies & Resources](supporting/dependencies.md)
- [Resource Catalog](supporting/resources.md)

## Contributing

See [AGENTS.md](../../AGENTS.md) for project conventions and file structure.
