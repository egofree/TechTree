# Bootciv Tech Tree

> A complete dependency chain for bootstrapping industrial civilization from stone-age materials to semiconductor manufacturing (GPUs, solar cells, ICs).

The tree maps every technology, material, and process needed to go from fire and stone tools to integrated circuit fabrication. It assumes a knowledgeable group starting in a resource-rich area with access to quartz, iron ore, coal, and limestone, but no pre-existing tools or infrastructure.

## How to Read This Tree

Three levels, top to bottom:

**Domain** — a broad technology area like metals, energy, or silicon. Each domain is a self-contained world of related processes. Domains are the navigation units for this tree.

**Capability** — a specific achievement within a domain, like iron smelting or crystal growth. Capabilities have dotted IDs showing their parent: `metals.iron-steel`, `silicon.crystal-growth`.

**Process** — a detailed method or operation, like Czochralski pulling or blast furnace operation. These carry two dots: `silicon.crystal-growth.cz-pulling`.

Dependencies use these dotted IDs. When photolithography requires silicon, the edge reads `{from: "photolithography", to: "silicon"}`. The full graph lives in [edges.json](../data/edges.json).

## Quick Start Path

The critical path through the tree, in rough chronological order. These domains form the spine: each depends on those before it.

1. **[Foundations](foundations/)** — fire, charcoal, food surplus, stone tools
2. **[Mining](mining/)** — ore access for every metallurgical process
3. **[Metals](metals/)** — copper, bronze, iron, steel
4. **[Machine Tools](machine-tools/)** — the master enabler: lathe, shaper, mill, grinder
5. **[Energy](energy/)** — water/wind power, steam engines, electricity, arc furnaces
6. **[Ceramics](ceramics/)** — refractories, kilns, pottery, lime
7. **[Chemistry](chemistry/)** — mineral acids, alkalis, distillation, oils & grease
8. **[Glass](glass/)** — basic and advanced glass production, crucibles
9. **[Gas Handling](gas-handling/)** — vacuum pumps, gas compression, purification
10. **[Measurement](measurement/)** — precision metrology, measurement standards
11. **[Silicon](silicon/)** — MG-Si production, crystal growth, solar cells
12. **[Photolithography](photolithography/)** — cleanrooms, lithography, IC fabrication
13. **[VLSI Scaling](vlsi-scaling/)** — continuous improvement toward GPUs and advanced solar

Several capabilities in other domains are also critical because their absence blocks downstream work: [knowledge](knowledge/) (writing, education), [textiles](textiles/) (cordage, drive belts), [chemistry.lubricants](chemistry/) (oils, grease, cutting fluid), [optics](optics/) (microscopes, lens grinding).

## Domain Listing

| Domain | Capabilities | Critical? | Key Outputs |
|--------|:------------:|:---------:|-------------|
| [Foundations](foundations/) | 4 | Yes | food surplus, fire, stone tools, agriculture |
| [Animals](animals/) | 7 | | draft power, wool, leather, dairy, eggs, meat, hunting |
| [Plants & Botany](plants/) | 5 | | food crops, medicine, timber, fiber, natural dyes |
| [Mining](mining/) | 5 | Yes | copper ore, iron ore, coal, quartz, sulfur |
| [Metals](metals/) | 9 | | copper, iron, steel |
| [Machine Tools](machine-tools/) | 6 | Yes | lathe, mill, grinder, bearings |
| [Energy](energy/) | 9 | | steam engines, electricity, arc furnaces, charcoal, coke |
| [Ceramics](ceramics/) | 4 | | refractories, kilns, lime, pottery, crucibles |
| [Chemistry](chemistry/) | 18 | | mineral acids, alkalis, electrolysis, distillation, oils & grease |
| [Glass](glass/) | 3 | | basic glass, borosilicate glass, fused silica, quartz crucibles |
| [Gas Handling](gas-handling/) | 2 | | vacuum pumps, gas compression, purification |
| [Measurement](measurement/) | 4 | | precision instruments, gauge blocks, calibration |
| [Silicon](silicon/) | 5 | | MG-Si, wafers, solar cells, transistors |
| [Photolithography](photolithography/) | 3 | | cleanrooms, lithography, ICs |
| [VLSI Scaling](vlsi-scaling/) | 4 | | GPUs, advanced solar, EDA tools |
| [Knowledge](knowledge/) | 4 | Yes | writing, printing, education, libraries |
| [Textiles](textiles/) | 7 | Yes | cordage, cloth, rope, drive belts |
| [Transport](transport/) | 5 | | roads, railways, aviation, logistics |
| [Computing](computing/) | 5 | | slide rules, calculators, automation |
| [Health](health/) | 5 | | clean water, sanitation, pharmaceuticals |
| [Polymers](polymers/) | 4 | | rubber, FR-4, PTFE, fiberglass |
| [Optics](optics/) | 2 | | lenses, microscopes, optical comparators |

## Dependency Overview

See the [full dependency diagram](../diagrams/mermaid/overview.mmd) for the complete directed acyclic graph of all domain-level dependencies.

## Parallel Opportunities

These domains and capabilities can begin early, independent of the main critical path. Starting them in parallel accelerates the whole effort.

- **[Knowledge](knowledge/)** (`knowledge.writing`) — writing, printing, education. Start Day 1. The 50-200 year bootstrapping effort dies with the first generation without knowledge transmission.
- **[Textiles](textiles/)** (`textiles`) — fiber, spinning, rope. Start Day 1. Cordage and cloth underpin mining hoists, tool hafting, and power transmission.
- **[Chemistry](chemistry/) lubricants** (`chemistry.lubricants`) — oils from animal fats and vegetable sources. Start Day 1. Without lubrication, every bearing and slide seizes.
- **[Chemistry](chemistry/) petroleum alternatives** (`chemistry.petroleum-alternatives`) — fermentation produces ethanol, acetone, and acetic acid without petroleum. Start Day 1.
- **[Computing](computing/)** (`computing.mechanical`) — mechanical calculation with slide rules and nomograms. Start as soon as marking tools exist.
- **[Health](health/)** (`health.sanitation`) — sanitation, water purification, quarantine protocols. Start Day 1. Skilled workers are the scarcest resource.
- **[Transport](transport/)** (`transport.roads`) — road construction and basic bridges expand the reachable resource base early on.
- **[Machine Tools](machine-tools/) precision metrology** → now in **[Measurement](measurement/)** (`measurement.precision-metrology`) — base unit standards and basic measuring instruments. Start alongside early toolmaking.
- **[Optics](optics/)** (`optics.inspection`) — lens grinding, microscopes, optical comparators. Start once glass production is established.

## Data Layer

Structured data files backing this tree:

- [nodes.json](../data/nodes.json) — complete node definitions (domains, capabilities, processes)
- [edges.json](../data/edges.json) — dependency graph (directed, acyclic)
- [glossary.json](../data/glossary.json) — glossary terms with relevance ratings and cross-references
- [checklist.yaml](../data/checklist.yaml) — milestone checklist with progression tracking
- [resources.json](../data/resources.json) — raw material catalog with criticality ratings

## Supporting Docs

- [Minimum Viable Civilization Checklist](supporting/minimum-viable-checklist.md)
- [Dependencies & Resources](supporting/dependencies.md)
- [Resource Catalog](supporting/resources.md)

## Contributing

See [AGENTS.md](../../AGENTS.md) for project conventions and file structure.
