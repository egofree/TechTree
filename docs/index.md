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

1. **[Foundations](foundations/index.md)** — fire, charcoal, food surplus, stone tools
2. **[Mining](mining/index.md)** — ore access for every metallurgical process
3. **[Metals](metals/index.md)** — copper, bronze, iron, steel
4. **[Machine Tools](machine-tools/index.md)** — the master enabler: lathe, shaper, mill, grinder
5. **[Energy](energy/index.md)** — water/wind power, steam engines, electricity, arc furnaces
6. **[Ceramics](ceramics/index.md)** — refractories, kilns, pottery, lime
7. **[Chemistry](chemistry/index.md)** — mineral acids, alkalis, distillation, oils & grease
8. **[Glass](glass/index.md)** — basic and advanced glass production, crucibles
9. **[Gas Handling](gas-handling/index.md)** — vacuum pumps, gas compression, purification
10. **[Cryogenics](cryogenics/index.md)** — refrigeration, cryogenic air separation, gas liquefaction & storage
11. **[Measurement](measurement/index.md)** — precision metrology, measurement standards
12. **[Silicon](silicon/index.md)** — MG-Si production, crystal growth, solar cells
13. **[Photolithography](photolithography/index.md)** — cleanrooms, lithography, IC fabrication
14. **[VLSI Scaling](vlsi-scaling/index.md)** — continuous improvement toward GPUs and advanced solar

Several capabilities in other domains are also critical because their absence blocks downstream work: [knowledge](knowledge/index.md) (writing, education), [textiles](textiles/index.md) (cordage, drive belts), [chemistry.lubricants](chemistry/index.md) (oils, grease, cutting fluid), [optics](optics/index.md) (microscopes, lens grinding).

## Domain Listing

| Domain | Capabilities | Critical? | Key Outputs |
|--------|:------------:|:---------:|-------------|
| [Agriculture](agriculture/index.md) | — | Yes | mechanized farming, soil science, hydroponics, greenhouses |
| [Animals](animals/index.md) | 7 | | draft power, wool, leather, dairy, eggs, meat, hunting |
| [Automation & Robotics](automation/index.md) | 4 | | SECS/GEM protocols, wafer robots, FOUP transport, process control |
| [Ceramics](ceramics/index.md) | 4 | | refractories, kilns, lime, pottery, crucibles |
| [Chemistry](chemistry/index.md) | 18 | | mineral acids, alkalis, electrolysis, distillation, oils & grease |
| [Cryogenics](cryogenics/index.md) | 3 | | refrigeration cycles, cryogenic air separation, gas liquefaction & storage |
| [Computing](computing/index.md) | 5 | | slide rules, calculators, automation |
| [Construction](construction/index.md) | 3 | | structural engineering, concrete, dams, tunnels |
| [Defense & Military](defense/index.md) | 4 | | weapons progression, fortifications, armor, siege engineering, military logistics |
| [Energy](energy/index.md) | 9 | | steam engines, electricity, arc furnaces, charcoal, coke |
| [EHS](ehs/index.md) | 5 | | chemical safety, ventilation, PPE, emergency response, waste management |
| [Food Processing](food-processing/index.md) | 4 | | milling, canning, pasteurization, preservation, dairy, brewing |
| [Foundations](foundations/index.md) | 4 | Yes | food surplus, fire, stone tools, agriculture |
| [Gas Handling](gas-handling/index.md) | 2 | | vacuum pumps, gas compression, purification |
| [Glass](glass/index.md) | 3 | | basic glass, borosilicate glass, fused silica, quartz crucibles |
| [Health](health/index.md) | 5 | | clean water, sanitation, pharmaceuticals |
| [Knowledge](knowledge/index.md) | 4 | Yes | writing, printing, education, libraries |
| [Machine Tools](machine-tools/index.md) | 6 | Yes | lathe, mill, grinder, bearings |
| [Marine & Naval](marine/index.md) | 4 | | shipbuilding, navigation, propulsion, maritime infrastructure, submarine cables |
| [Measurement](measurement/index.md) | 4 | | precision instruments, gauge blocks, calibration |
| [Metals](metals/index.md) | 9 | | copper, iron, steel |
| [Mining](mining/index.md) | 5 | Yes | copper ore, iron ore, coal, quartz, sulfur |
| [Optics](optics/index.md) | 2 | | lenses, microscopes, optical comparators |
| [Photolithography](photolithography/index.md) | 3 | | cleanrooms, lithography, ICs |
| [Plants & Botany](plants/index.md) | 5 | | food crops, medicine, timber, fiber, natural dyes |
| [Polymers](polymers/index.md) | 4 | | rubber, FR-4, PTFE, fiberglass |
| [Silicon](silicon/index.md) | 5 | | MG-Si, wafers, solar cells, transistors |
| [Telecommunications](telecom/index.md) | 5 | | pre-electric signaling, telegraph networks, telephone, submarine cables, radio |
| [Textiles](textiles/index.md) | 7 | Yes | cordage, cloth, rope, drive belts |
| [Transport](transport/index.md) | 5 | | roads, railways, aviation, logistics |
| [VLSI Scaling](vlsi-scaling/index.md) | 4 | | GPUs, advanced solar, EDA tools |
| [Vacuum Technology](vacuum/index.md) | 3 | | vacuum pumps, chambers, measurement, leak detection |
| [Water Infrastructure](water/index.md) | — | | water treatment, desalination, distribution, sewage |
| [Ultra-Pure Materials](ultra-pure/index.md) | 3 | | 18.2 MΩ·cm water, 9N chemicals, ppt-level analysis |

## Dependency Overview

See the [full dependency diagram](../diagrams/mermaid/overview.mmd) for the complete directed acyclic graph of all domain-level dependencies.

## Parallel Opportunities

These domains and capabilities can begin early, independent of the main critical path. Starting them in parallel accelerates the whole effort.

- **[Knowledge](knowledge/index.md)** (`knowledge.writing`) — writing, printing, education. Start Day 1. The 50-200 year bootstrapping effort dies with the first generation without knowledge transmission.
- **[Textiles](textiles/index.md)** (`textiles`) — fiber, spinning, rope. Start Day 1. Cordage and cloth underpin mining hoists, tool hafting, and power transmission.
- **[Chemistry](chemistry/index.md) lubricants** (`chemistry.lubricants`) — oils from animal fats and vegetable sources. Start Day 1. Without lubrication, every bearing and slide seizes.
- **[Chemistry](chemistry/index.md) petroleum alternatives** (`chemistry.petroleum-alternatives`) — fermentation produces ethanol, acetone, and acetic acid without petroleum. Start Day 1.
- **[Computing](computing/index.md)** (`computing.mechanical`) — mechanical calculation with slide rules and nomograms. Start as soon as marking tools exist.
- **[Health](health/index.md)** (`health.sanitation`) — sanitation, water purification, quarantine protocols. Start Day 1. Skilled workers are the scarcest resource.
- **[Transport](transport/index.md)** (`transport.roads`) — road construction and basic bridges expand the reachable resource base early on.
- **[Machine Tools](machine-tools/index.md) precision metrology** → now in **[Measurement](measurement/index.md)** (`measurement.precision-metrology`) — base unit standards and basic measuring instruments. Start alongside early toolmaking.
- **[Optics](optics/index.md)** (`optics.inspection`) — lens grinding, microscopes, optical comparators. Start once glass production is established.

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

See [AGENTS.md](../AGENTS.md) for project conventions and file structure.
