# Phase 4: Energy Revolution — Steam, Electricity & Scale

**Timeline**: Years 15–30  
**Goal**: Abundant, controllable power.  
**Dependencies**: [Phase 2](phase-02-metallurgy.md) (iron/steel), [Phase 3](phase-03-machine-tools.md) (precision cylinders, machining)

## Objectives

- Produce coke from coal for superior high-temperature processes
- Build steam engines for mechanical power
- Generate electricity via electromagnetic induction
- Create electric arc and submerged arc furnaces for high-temperature work

## Key Technologies

### Coal & Coke
- Coal mining (if coal deposits available)
- Coke production: destructive distillation of coal in beehive ovens
- Coke provides higher temperatures and more consistent heat than charcoal

### Steam Engines
- **Newcomen-style**: Atmospheric engine for pumping water from mines
- **Watt-style**: Separate condenser, double-acting, rotary output
- **Critical dependency**: Precision cylinder boring (Wilkinson boring machine from Phase 3)
- Boilers: riveted iron/steel plate construction
- Applications: mine pumping, factory power, later locomotives

### Electricity Generation
- Voltaic piles / batteries: zinc + copper + electrolyte (early experimentation)
- Wire drawing: copper through steel dies (from Phase 3) → insulated wire
- **Generators**: Faraday induction principle — rotating coils in magnetic fields
  - Powered by steam engines or water wheels
  - Electromagnets (iron core + wire coil) for stronger fields
- **Motors**: Reverse of generators — electrical input → mechanical output
- **Transformers**: Voltage step-up/step-down for power distribution
- Power distribution: insulated cables (rubber, varnished cloth, or gutta-percha insulation)

### Electric Furnaces
- **Electric arc furnace**: Carbon electrodes, temperatures up to 3500°C
  - Critical for: steelmaking, silicon reduction (Phase 7), carbide production
- **Submerged arc furnace**: Used for silicon production from quartz + carbon
- **Resistance heating**: For furnaces, ovens, crystal growth heaters

### Electrolysis Foundations
- Electrolytic cells for: chlorine, caustic soda, hydrogen, oxygen
- Later: aluminum (Hall-Héroult process), magnesium, sodium

### Wire Drawing Bootstrap
- **Chicken-and-egg problem**: you need wire for generators, but hardened steel dies for drawing that wire require decent steel, which itself needs powered machinery
- First wire: hammered or swaged copper rod pulled through hand-punched holes in hardened steel plates, iterating through successively smaller die openings
- Lubrication is critical at every pass (tallow or soap solution; see [SQ 10](../side-quests/sq-10-lubricants-oils.md)); without it the wire galls and snaps
- Wire annealing between passes restores ductility lost from cold working
- Insulation (rubber, varnished cloth, gutta-percha) is applied after drawing, not during

### Permanent Magnets
- **Lodestone** (naturally magnetized magnetite) for early compasses and basic magnetic experiments
- **Magnetized iron/steel bars**: stroking with lodestone or placing in Earth's magnetic field yields magnets for early generator field poles and galvanometers
- **Later materials** (Alnico, ferrite) arrive with Phase 5 chemistry and alloy development

## Enables (Downstream)

| Output | Used By |
|--------|---------|
| Steam power | Phase 5 (chemical plant machinery), Phase 7 (silicon furnace) |
| Electricity | ALL downstream phases |
| Arc furnaces | Phase 7 (MG-Si production), Phase 5 (steel, carbides) |
| Electrolysis | Phase 5 (chlorine, alkalis, metals) |
| Electric motors | Phase 5 (mixers, pumps), Phase 7 (crystal pullers), Phase 8 (fab equipment) |
| Wire/cables | Phase 4 (distribution), Phase 6 (coils), Phase 8 (interconnects concept) |

## Key Feedback Loop

```
Electricity → powers better machine tools → better generators → more electricity
Electricity → powers arc furnaces → better steel → better machines
```

## Practical Bottlenecks

- **Cylinder boring precision**: Without accurate boring, steam engines leak and lose efficiency
- **Copper wire production**: Drawing long, consistent wire requires good dies and lubrication
- **Insulation**: Finding adequate wire insulation materials (natural rubber, varnished cloth)
- **Scale**: Moving from laboratory demos to industrial-scale power generation

## Safety Concerns

- Boiler explosions (catastrophic)
- Electrical shock and electrocution
- Coal mine hazards (collapse, gas, flooding)
- Arc furnace UV radiation and high temperatures

## Side Quest Dependencies

- **Lubricants & Oils ([SQ 10](../side-quests/sq-10-lubricants-oils.md))** — critical for wire drawing (soap/tallow lubrication) and cylinder lubrication in steam engines

[← Phase 3](phase-03-machine-tools.md) | [Overview](overview.md) | [Phase 5: Chemistry →](phase-05-chemistry.md)
