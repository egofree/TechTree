# Dependencies and Resource Requirements

## Cross-Domain Dependency Matrix

Key domain-to-domain dependencies derived from [edges.json](../../data/edges.json). Each row shows a dependent domain and the prerequisite it requires.

| From Domain | To Domain | Key Dependency |
|------------|-----------|---------------|
| Metals | Foundations | Fire, food surplus, stone tools |
| Metals | Mining | Copper ore, iron ore, quartz |
| Machine Tools | Metals | Iron/steel for machine beds and cutting tools |
| Machine Tools | Textiles | Cordage and cloth for power transmission |
| Energy | Metals | Iron/steel for boilers, generators |
| Ceramics | Foundations | Clay, fire for kilns |
| Ceramics | Metals | Metal tools for kiln construction |
| Chemistry | Metals | Metal vessels, piping |
| Chemistry | Energy | Electricity for electrolysis, heat for reactions |
| Glass | Machine Tools | Precision-machined parts |
| Glass | Chemistry | Glass feedstock, chemical processing |
| Glass | Energy | Furnace power |
| Gas Handling | Machine Tools | Precision-machined parts |
| Gas Handling | Energy | Compressor power |
| Gas Handling | Chemistry | Gas purification chemicals |
| Measurement | Machine Tools | Precision instruments |
| Measurement | Metals | Standard artifacts |
| Optics | Machine Tools | Precision lens grinding |
| Optics | Glass | Optical glass |
| Silicon | Machine Tools | Precision-machined equipment |
| Silicon | Energy | Electric arc furnaces, process power |
| Silicon | Chemistry | Acids, gases, purification chemicals |
| Silicon | Glass | Quartz crucibles |
| Silicon | Gas Handling | Vacuum systems, inert atmosphere |
| Silicon | Measurement | Precision metrology |
| Photolithography | Machine Tools | Precision equipment |
| Photolithography | Chemistry | Photoresists, etchants, solvents |
| Photolithography | Gas Handling | Vacuum systems |
| Photolithography | Optics | Alignment optics |
| Photolithography | Silicon | Wafers |
| Photolithography | Ceramics | Cleanroom construction materials |
| VLSI Scaling | Photolithography | Working ICs and fab processes |
| Knowledge | Foundations | Writing media, surplus labor |
| Textiles | Foundations | Natural fibers, spinning tools |
| Mining | Foundations | Stone tools, fire-setting |
| Health | Foundations | Basic hygiene, shelter |
| Health | Chemistry | Pharmaceuticals, water treatment chemicals |
| Transport | Metals | Iron/steel for vehicles, rails |
| Transport | Energy | Steam, fuel, electricity |
| Transport | Mining | Iron ore, coal |
| Transport | Machine Tools | Precision-machined parts |
| Computing | Machine Tools | Gears, precision mechanisms |
| Polymers | Foundations | Natural rubber, basic chemistry |

## Critical Capability Dependencies

Capabilities whose outputs are hard prerequisites for downstream work.

| Capability | Depends On | Enables | Edge Type |
|-----------|-----------|---------|-----------|
| `metals.iron-steel` | `mining`, `foundations` | `machine-tools`, `energy`, `chemistry`, `transport` | material |
| `machine-tools.iterative-bootstrap` | `machine-tools.casting` | `silicon`, `glass`, `gas-handling`, `photolithography` | tool |
| `energy.electricity` | `metals`, `machine-tools` | `chemistry.electrolysis`, `energy.electric-furnaces`, `silicon` | material |
| `chemistry.acids` | `mining`, `energy` | `silicon.basic-devices`, `glass.basic`, `chemistry.dopant-etch-gases` | material |
| `chemistry.air-separation` | `energy.electricity`, `chemistry.distillation` | `silicon.crystal-growth` (argon) | material |
| `silicon.crystal-growth` | `glass.advanced`, `chemistry.air-separation`, `measurement.precision-metrology` | `silicon.basic-devices` | material, tool |
| `photolithography.fab-processes` | `chemistry.dopant-etch-gases`, `gas-handling.vacuum` | `chemistry.packaging-testing`, `vlsi-scaling` | material, tool |
| `chemistry.lubricants` | `foundations`, `chemistry.petroleum-alternatives` | `machine-tools`, `energy` (bearing and machine operation) | material |

## Critical Raw Materials

| Material | Source | Used In | Criticality |
|----------|--------|---------|-------------|
| Quartz (SiO₂) | Mining | `silicon.mg-si-production`, `glass.advanced` | Critical |
| Iron ore | Mining | `metals.iron-steel`, all downstream domains | Critical |
| Copper ore | Mining | `metals.copper-bronze`, `energy.electricity` (wire) | Critical |
| Carbon (charcoal/coke) | `energy.fuels` | Reducing agent and fuel for metals through silicon | Critical |
| Coal | Mining | `energy.fuels.coal`, `energy.fuels.coke` (electrodes) | High |
| Limestone | Mining | `metals` (flux), `chemistry.alkalis` (Solvay) | High |
| Sulfur/pyrite | Mining | `chemistry.acids` (sulfuric acid) | Critical |
| Fluorite (CaF₂) | Mining | `chemistry.acids` (HF production) | Critical |
| Tin ore (cassiterite) | Mining | `metals.copper-bronze` (bronze) | Medium |
| Clay | Mining | `ceramics.pottery`, `ceramics.kilns` | High |
| Aluminum ore (bauxite) | Mining | `chemistry.electrolysis`, `machine-tools.casting` | Medium |

## Parallel Domain Dependency Table

Domains and capabilities that can begin independently of the main critical path, with their key dependencies and bottlenecks.

| Domain/Capability | Key Dependencies | Critical Resources | Main Bottleneck |
|-------------------|-----------------|-------------------|-----------------|
| `knowledge` | `foundations` | Scribes, durable media, storage | Time and specialists |
| `measurement.precision-metrology` | `machine-tools.casting`, `metals` | Stable references, skilled craftsmen | Precision machining |
| `transport` | `metals`, `energy`, `machine-tools` | Wood, iron, later copper and fuel | Scale of construction |
| `computing.mechanical` | `machine-tools` (high precision) | Gears, springs, clockmaking skills | Extreme precision early on |
| `health.sanitation` | `chemistry` | Clean water, soap, basic drugs | Cultural adoption |
| `chemistry.air-separation` | `chemistry.distillation`, `energy.electricity` | Gas plants, cleanrooms, chemicals | High purity and capital |
| `energy.storage` | `energy`, `chemistry`, `metals` | Lead, acids, mechanical components | Material availability |
| `ceramics` | `foundations`, `metals` | High-purity clays/silica, organics | High-temperature processing |
| `textiles` | `foundations`, water power | Flax, hemp, wool, cotton | Belt and rope supply for power transmission |
| `chemistry.lubricants` | `foundations`, `chemistry.petroleum-alternatives` | Animal fats, oil seeds, petroleum | Bearing and cutting fluid supply |
| `mining` | `foundations`, `machine-tools` | Timber, iron, pumps, ventilation | Deep drainage drives steam engine development |
| `chemistry.petroleum-alternatives` | `foundations`, `chemistry.distillation` | Coal tar, petroleum, fermentation substrates | Feedstock availability and dual-path planning |
| `transport.aviation` | `machine-tools`, `textiles`, `chemistry.petroleum-alternatives` | Steel tube/wood, fabric, precision engine parts | Power-to-weight ratio and precision machining |
| `polymers` | `chemistry`, `machine-tools` | Phenol, formaldehyde, ethylene, propylene | Polymerization, curing, composite layup |

## General Resource Themes

- **Human**: Specialists and training systems (biggest long-term constraint)
- **Material**: High-purity inputs and recycling loops
- **Energy**: Redundant and stored power
- **Infrastructure**: Transportation and clean environments
- **Knowledge**: Documentation and education feedback

[← Back to Docs](../index.md)
