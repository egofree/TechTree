# Bootciv Tech Tree

> A complete dependency chain for bootstrapping industrial civilization from stone-age materials to semiconductor manufacturing (GPUs, solar cells, ICs).

The tree maps every technology, material, and process needed to go from fire and stone tools to integrated circuit fabrication. It assumes a knowledgeable group starting in a resource-rich area with access to quartz, iron ore, coal, and limestone, but no pre-existing tools or infrastructure.

## How to Read This Tree

Three levels, top to bottom:

**Domain** — a broad technology area like metals, energy, or silicon. Each domain is a self-contained world of related processes. Domains are the navigation units for this tree.

**Capability** — a specific achievement within a domain, like iron smelting or crystal growth. Capabilities have dotted IDs showing their parent: `metals.iron-steel`, `silicon.crystal-growth`.

**Process** — a detailed method or operation, like Czochralski pulling or blast furnace operation. These carry two dots: `silicon.crystal-growth.cz-pulling`.

Dependencies use these dotted IDs. When photolithography requires silicon, the edge is stored as a per-entity file: `data/entities/_edges/silicon__photolithography.jsonld`. Each edge specifies `edgeType` (`"material"` or `"tool"`) and `flow` (`"primary"`, `"byproduct-reuse"`, `"waste-recovery"`, or `"recycling-loop"`).

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
10. **[Cryogenics](cryogenics/)** — refrigeration, cryogenic air separation, gas liquefaction & storage
11. **[Measurement](measurement/)** — precision metrology, measurement standards
12. **[Silicon](silicon/)** — MG-Si production, crystal growth, solar cells
13. **[Photolithography](photolithography/)** — cleanrooms, lithography, IC fabrication
14. **[Electronics](electronics/)** — PCB fabrication, soldering, power distribution, connectors
15. **[Computing](computing/)** — slide rules, calculators, automation
16. **[VLSI Scaling](vlsi-scaling/)** — continuous improvement toward GPUs and advanced solar
17. **[Software Bootstrapping](software-bootstrapping/)** — assemblers, compilers, operating systems, self-hosting toolchains

Several capabilities in other domains are also critical because their absence blocks downstream work: [knowledge](knowledge/) (writing, education), [textiles](textiles/) (cordage, drive belts), [chemistry.lubricants](chemistry/) (oils, grease, cutting fluid), [optics](optics/) (microscopes, lens grinding).

## Domain Listing

| Domain | Capabilities | Critical? | Key Outputs |
|--------|:------------:|:---------:|-------------|
| [Agriculture](agriculture/) | 10 | Yes | mechanized farming, soil science, hydroponics, greenhouses |
| [Animals](animals/) | 26 | | draft power, wool, leather, dairy, eggs, meat, hunting |
| [Automation & Robotics](automation/) | 4 | | SECS/GEM protocols, wafer robots, FOUP transport, process control |
| [Ceramics](ceramics/) | 8 | | refractories, kilns, lime, pottery, crucibles |
| [Clean Room Technology](cleanrooms/) | 3 | | HEPA/ULPA filtration, contamination control, facility design & HVAC |
| [Chemistry](chemistry/) | 59 | | mineral acids, alkalis, electrolysis, distillation, oils & grease |
| [Cryogenics](cryogenics/) | 3 | | refrigeration cycles, cryogenic air separation, gas liquefaction & storage |
| [Computing](computing/) | 8 | | slide rules, calculators, automation |
| [Electronics](electronics/) | 51 | | PCB fabrication, soldering, power distribution, connectors, transformers |
| [Electrochemistry & Plating](electrochemistry/) | 4 | | electroplating, anodizing, electropolishing, electroless plating, electroforming |
| [Construction](construction/) | 3 | | structural engineering, concrete, dams, tunnels |
| [Defense & Military](defense/) | 4 | | weapons progression, fortifications, armor, siege engineering, military logistics |
| [Economics & Organization](economics-organization/) | 7 | | division of labor, trade, currency, accounting, supply chains, governance |
| [Energy](energy/) | 43 | | steam engines, electricity, arc furnaces, charcoal, coke |
| [EHS](ehs/) | 7 | | chemical safety, ventilation, PPE, emergency response, waste management |
| [Food Processing](food-processing/) | 10 | | milling, canning, pasteurization, preservation, dairy, brewing |
| [Foundations](foundations/) | 5 | Yes | food surplus, fire, stone tools, agriculture |
| [Gas Handling](gas-handling/) | 5 | | vacuum pumps, gas compression, purification |
| [Glass](glass/) | 7 | | basic glass, borosilicate glass, fused silica, quartz crucibles |
| [Health](health/) | 11 | | clean water, sanitation, pharmaceuticals |
| [Knowledge](knowledge/) | 10 | Yes | writing, printing, education, libraries |
| [Mathematics & Formal Sciences](mathematics/) | 3 | | arithmetic, calculus, Boolean algebra, information theory, computation theory |
| [Machine Tools](machine-tools/) | 25 | Yes | lathe, mill, grinder, bearings |
| [Marine & Naval](marine/) | 4 | | shipbuilding, navigation, propulsion, maritime infrastructure, submarine cables |
| [Measurement](measurement/) | 10 | | precision instruments, gauge blocks, calibration |
| [Metals](metals/) | 26 | | copper, iron, steel |
| [Mining](mining/) | 9 | Yes | copper ore, iron ore, coal, quartz, sulfur |
| [Petroleum Extraction & Refining](petroleum/) | 8 | | crude oil extraction, refining, petrochemical feedstocks |
| [Optics](optics/) | 3 | | lenses, microscopes, optical comparators |
| [Photolithography](photolithography/) | 8 | | cleanrooms, lithography, ICs |
| [Precision Motion Control](precision-motion/) | 4 | | nanometer positioning, wafer stages, vibration isolation, precision encoders |
| [Plants & Botany](plants/) | 18 | | food crops, medicine, timber, fiber, natural dyes |
| [Polymers](polymers/) | 11 | | rubber, FR-4, PTFE, fiberglass |
| [Quality Control](quality-control/) | 3 | | statistical process control, inspection & sampling, defect analysis & yield modeling |
| [Silicon](silicon/) | 8 | | MG-Si, wafers, solar cells, transistors |
| [Software Bootstrapping](software-bootstrapping/) | 6 | | assemblers, compilers, operating systems, development tools, self-hosting |
| [Telecommunications](telecom/) | 5 | | pre-electric signaling, telegraph networks, telephone, submarine cables, radio |
| [Textiles](textiles/) | 11 | Yes | cordage, cloth, rope, drive belts |
| [Transport](transport/) | 5 | | roads, railways, aviation, logistics |
| [VLSI Scaling](vlsi-scaling/) | 4 | | GPUs, advanced solar, EDA tools |
| [Vacuum Technology](vacuum/) | 6 | | vacuum pumps, chambers, measurement, leak detection |
| [Water Infrastructure](water/) | 5 | | water treatment, desalination, distribution, sewage |
| [Ultra-Pure Materials](ultra-pure/) | 3 | | 18.2 MΩ·cm water, 9N chemicals, ppt-level analysis |

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

Structured data files backing this tree, all in JSON-LD format:

- [data/entities/](../data/entities/) — per-entity JSON-LD files organized by domain (`data/entities/{domain}/` for capabilities and processes)
- [data/entities/_edges/](../data/entities/_edges/) — dependency edges as individual `{from}__{to}.jsonld` files (1,194 edges)
- [data/context.jsonld](../data/context.jsonld) — shared JSON-LD `@context` with all term → IRI mappings
- [data/schema/](../data/schema/) — JSON Schema files (entity, domain, capability, process, product, dependency)
- [data/glossary.json](../data/glossary.json) — 11,966 glossary terms with relevance ratings and cross-references
- [data/checklist.yaml](../data/checklist.yaml) — milestone checklist with progression tracking
- [data/resources.json](../data/resources.json) — raw material catalog with criticality ratings

## Supporting Docs

- [Minimum Viable Civilization Checklist](supporting/minimum-viable-checklist.md)
- [Dependencies & Resources](supporting/dependencies.md)
- [Resource Catalog](supporting/resources.md)

## Contributing

See [AGENTS.md](../AGENTS.md) for project conventions and file structure.
