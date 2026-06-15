# Battery & Electrochemical Storage

> **Node ID**: energy.batteries
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`electrochemistry.electroplating`](../electrochemistry/electroplating.md)
> **Enables**: None
> **Timeline**: Years 15-50
> **Outputs**: lead_acid_batteries
> **Critical**: Yes — rechargeable batteries enable off-grid power, telecom backup, vehicle starting, and portable electronics; lead-acid is the bootstrappable early win.

## Overview

Electrochemical batteries store energy in chemical form and release it as DC electricity through reversible reduction-oxidation reactions at two electrodes separated by an electrolyte. They are the only practical way to store electrical energy at the point of use without mechanical intermediaries (pumped hydro, flywheels). Three chemistries span the bootstrap timeline, each demanding progressively more materials purity and process control.

**Lead-acid (Planté 1859)** is the bootstrappable first battery. Pb anode, PbO₂ cathode, 37% H₂SO₄ electrolyte. 2.0 V/cell nominal, 30-50 Wh/kg, 300-1500 cycles. Robust, tolerant of abuse, >95% recyclable. A 12 V bank is six cells in series. It needs only lead, sulfuric acid, and basic electrode casting — all available once a civilization has [lead smelting](../metals/non-ferrous.md) and [contact-process acid](../chemistry/acids.md).

**Nickel-iron (Edison 1901)** uses Fe anode, NiOOH cathode, 20-30% KOH electrolyte. 1.2 V/cell, 30-50 Wh/kg, 2000-4000 cycles. Survives deep discharge, overcharge, and neglect — but high self-discharge (1-2%/day) and poor low-temperature performance limit its uses. Useful where longevity matters more than energy density.

**Lithium-ion** (graphite anode, layered metal-oxide cathode, non-aqueous electrolyte) arrives late. 3.2-3.7 V/cell, 120-250 Wh/kg, 1000-5000 cycles. Requires high-purity lithium compounds, dry-room assembly (<1% RH), and precise thermal management. The dominant modern chemistry but demands a mature chemical industry.

Batteries are the enabling technology for off-grid [photovoltaic](./photovoltaics.md) systems, [telecom](../telecom/index.md) backup, vehicle starting and traction, and portable electronics. Without them, intermittent renewables cannot firm their output and mobile electrical applications are impossible. The [energy storage](./storage.md) overview covers complementary mechanical storage (pumped hydro, flywheels, compressed air).

## Prerequisites

### Materials

- [Lead](../metals/non-ferrous.md) — grid and active material for lead-acid (99.9% Pb, alloyed with 4-6% Sb for mechanical strength)
- [Sulfuric acid](../chemistry/acids.md) — lead-acid electrolyte, 37% w/w (1.28 specific gravity)
- Antimony (Sb) — grid hardening agent, 4-6% of alloy
- [Nickel and iron](../metals/index.md) — Edison cell electrodes
- Potassium hydroxide (KOH) — Ni-Fe electrolyte, 20-30% w/w
- [Lithium compounds](../chemistry/lithium-separation.md) — Li-ion cathode (Li₂CO₃ or LiOH precursor)
- Graphite — Li-ion anode (natural flake, 99.9% C, or synthetic)
- Cobalt, nickel, manganese, iron, phosphate — Li-ion cathode active materials depending on chemistry (LCO, NMC, LFP)
- Separator material — microporous polyethylene (PE) or rubber for lead-acid; polyolefin for Li-ion
- Battery casing — polypropylene (lead-acid), steel can (Ni-Fe), aluminium-polymer pouch (Li-ion)

### Tools and Equipment

- [Electroplating capability](../electrochemistry/electroplating.md) — electrode preparation and paste curing know-how
- [DC power supply](./electricity.md) — for formation charging (2.15-2.40 V/cell, 5-50 A depending on cell size)
- Cast iron or lead-alloy grid molds with slot geometry matched to plate thickness (1.5-4 mm)
- Paste mixer (ribbon or sigma-blade) for PbO + H₂SO₄ + water slurry
- Curing chamber with temperature (40-65°C) and humidity (>95% RH) control
- Formation tank — acid-resistant (lead-lined or PP) with individual cell voltage monitoring
- Dry room (<1% RH, -40°C dew point) — Li-ion assembly only, requires [desiccant systems](./cooling.md)
- Hydraulic press — plate stacking and terminal welding (5-20 tonne)

### Knowledge

- Electrode paste rheology: the ratio of PbO : H₂SO₄ : H₂O determines paste density (3.8-4.2 g/cm³), porosity (40-55%), and final cured strength. Too dry → paste flakes off grid; too wet → paste slumps and shorts.
- Formation chemistry: the conversion of cured PbO paste to active Pb (negative) and PbO₂ (positive) by controlled charging. Negative: PbO + H₂SO₄ → PbSO₄ + H₂O, then PbSO₄ + 2H⁺ + 2e⁻ → Pb + H₂SO₄. Positive: PbSO₄ + 2H₂O → PbO₂ + H₂SO₄ + 2H⁺ + 2e⁻.
- Gas recombination chemistry in VRLA (valve-regulated lead-acid): oxygen generated at the positive plate diffuses to the negative and recombines to water, making the battery maintenance-free.
- Thermal runaway in Li-ion: if internal temperature exceeds 150-180°C, the separator melts and cathode decomposition releases oxygen, driving exothermic decomposition.一旦 started, cannot be extinguished by normal means.

### Infrastructure

- Ventilated battery formation room — hydrogen gas evolves during charging (4-75% explosive range in air). Forced ventilation to <1% H₂ concentration mandatory.
- Acid-resistant flooring and drainage — spills of 37% H₂SO₄ attack concrete. Epoxy-coated floors with acid-neutralisation sumps.
- Eyewash and emergency shower within 10 m of all acid-handling stations.
- For Li-ion: clean, dry assembly area (Class 100,000 cleanroom or better, <1% RH).

## Bill of Materials

### Lead-Acid Battery (12 V, 100 Ah — typical starter/backup unit)

| Material | Quantity per battery | Source | Alternatives |
|----------|----------------------|--------|--------------|
| Lead (Pb) | 22-28 kg | [Non-ferrous metals](../metals/non-ferrous.md) — primary smelting or recycled battery lead | — (lead is essential to this chemistry) |
| Antimony (Sb) | 0.9-1.5 kg | [Non-ferrous metals](../metals/non-ferrous.md) — Sb from stibnite ore | Ca (0.03-0.08%) for low-maintenance grids; Sn (0.3-1%) for VRLA |
| Sulphuric acid (H₂SO₄, 37%) | 4-6 L (electrolyte fill) | [Chemistry — acids](../chemistry/acids.md) — contact process | — (no alternative electrolyte for lead-acid) |
| Separator (microporous PE or rubber) | 11-13 sheets (150 × 180 mm) | [Polymers](../polymers/index.md) — extruded PE sheet | Porous rubber, glass fibre mat (AGM for VRLA) |
| Polypropylene casing | 1 unit (170 × 220 × 230 mm) | [Polymers](../polymers/index.md) — injection moulded | Hard rubber (historical, heavier, brittle) |
| Lead-alloy terminal posts | 2 (M8 or M10) | [Non-ferrous metals](../metals/non-ferrous.md) | Brass inserts for corrosion resistance |

### Lithium-Ion Cell (LFP, 3.2 V, 100 Ah — prismatic)

| Material | Quantity per cell | Source | Alternatives |
|----------|-------------------|--------|--------------|
| Lithium iron phosphate (LiFePO₄) | 0.30-0.35 kg | [Chemistry](../chemistry/index.md) — solid-state synthesis from Li₂CO₃ + Fe₃O₄ + NH₄H₂PO₄ | NMC (LiNi₀.₃₃Mn₀.₃₃Co₀.₃₃O₂), LCO (LiCoO₂) |
| Graphite (anode, 99.9% C) | 0.15-0.20 kg | [Mining](../mining/index.md) — natural flake or synthetic from pitch | Hard carbon (lower energy density), Li metal (experimental, dendrite risk) |
| Copper foil (anode current collector, 8-12 μm) | 0.05-0.08 kg | [Metals — copper](../metals/copper-refining.md) | — (copper is standard for anode) |
| Aluminium foil (cathode collector, 15-20 μm) | 0.02-0.03 kg | [Metals — aluminium](../metals/aluminum.md) | — (aluminium is standard for cathode) |
| Electrolyte (LiPF₆ in EC:DMC 1:1) | 0.10-0.15 kg | [Chemistry](../chemistry/index.md) — requires LiPF₆ salt and high-purity organic solvents | LiTFSI (lower conductivity), ionic liquids (expensive) |
| Separator (polyolefin, 16-25 μm) | 1 sheet | [Polymers](../polymers/index.md) — PE/PP bilayer | — (critical safety component) |
| Prismatic casing (Al-polymer pouch or hard can) | 1 unit | [Metals — aluminium](../metals/aluminum.md) | Steel can (heavier) |

## Process Description

### Lead-Acid Cell Fabrication

1. **Cast grids**: Melt lead (327°C) with 4-6% antimony. Pour into preheated (150-200°C) cast iron book molds with grid slot geometry. Cool 30-60 seconds. Eject and trim flashing. Grid thickness 1.5-4.0 mm depending on application (thin = high power, thick = deep cycle).
2. **Mix paste**: Combine litharge (PbO, tetragonal) with 6-8% H₂SO₄ by weight and water in a sigma-blade mixer. Mix 15-30 minutes until paste density reaches 3.8-4.2 g/cm³. Paste should hold a ball shape when squeezed but flow under pressure. Too dry → paste flakes off grid; too wet → paste slumps and shorts.
3. **Past grids**: Apply paste to grids with a belt paster or by hand with a squeegee. Target paste weight 70-120 g per plate (varies with grid size). Inspect for complete grid coverage and uniform thickness.
4. **Cure pasted plates**: Stack plates in a curing chamber at 40-65°C, >95% RH for 24-48 hours. The curing process converts PbO to tribasic lead sulfate (3PbO·PbSO₄·H₂O) which bonds the paste to the grid. Plates should achieve 40-55% porosity and green strength sufficient for handling.
5. **Assemble cell**: Stack alternating positive and negative plates with microporous separators between each pair. Negative plates typically outnumber positive by one per cell (n+1 negative, n positive) to balance capacity. Weld positive plates to positive strap, negatives to negative strap with lead-burning (gas torch and lead rod).
6. **Fill with electrolyte**: Fill the assembled cell with 37% H₂SO₄ (1.28 specific gravity) to cover plate tops by 10-15 mm. Allow 1-2 hours for electrolyte absorption.
7. **Formation charge**: Apply 2.15-2.35 V/cell at 1-5 A per 100 Ah capacity for 24-72 hours. The paste converts to active material: negative plates become spongy grey Pb, positive plates become dark brown PbO₂. Monitor electrolyte temperature — keep below 55°C to prevent paste softening.
8. **Finish**: After formation, top up electrolyte, fit cell caps (vented or VRLA recombination), wash exterior, and test. A 12 V battery is six cells in series, connected by inter-cell welds.

### Nickel-Iron (Edison) Cell Fabrication

1. Prepare nickel hydroxide cathode: mix Ni(OH)₂ with graphite (10-15%) and cobalt additive, pocket in perforated nickel-plated steel tubes.
2. Prepare iron anode: mix Fe powder with small amounts of Cd or Hg (historically) to suppress hydrogen evolution, pocket in perforated steel.
3. Assemble alternating pockets with alkali-resistant separators, immerse in 20-30% KOH electrolyte.
4. Formation charge: 1.6-1.8 V/cell for 24 hours to activate electrode surfaces.

### Lithium-Ion Cell Assembly (LFP, industrial)

1. Mix cathode slurry: LiFePO₄ (88%), carbon black (4%, conductivity enhancer), PVDF binder (8%) in NMP solvent.
2. Coat Al foil with slurry to 100-200 μm wet thickness, dry at 80-120°C, calender (roll-press) to 60-150 μm final density (2.0-2.4 g/cm³).
3. Mix anode slurry: graphite (92%), CMC/SBR binder (8%) in water.
4. Coat Cu foil, dry, calender to 50-120 μm.
5. Cut electrodes to size, weld tabs (Al cathode, Ni or Cu anode).
6. Stack with separator (Z-fold or wound jelly-roll), insert into pouch or can.
7. Fill with electrolyte (LiPF₆ in EC:DMC) under vacuum, seal.
8. Formation: 3-5 charge-discharge cycles at 0.1C, then age 7-14 days to stabilise SEI layer.

## Quantitative Parameters

| Parameter | Lead-Acid (SLI) | Lead-Acid (Deep) | Ni-Fe | Li-ion (LFP) | Li-ion (NMC) |
|-----------|-----------------|-------------------|-------|--------------|--------------|
| Nominal voltage | 2.0 V/cell | 2.0 V/cell | 1.2 V/cell | 3.2 V/cell | 3.6-3.7 V/cell |
| Energy density | 30-50 Wh/kg | 25-35 Wh/kg | 30-50 Wh/kg | 120-160 Wh/kg | 200-250 Wh/kg |
| Volumetric density | 50-90 Wh/L | 50-80 Wh/L | 50-100 Wh/L | 250-350 Wh/L | 400-600 Wh/L |
| Cycle life (80% DoD) | 300-500 | 800-1500 | 2000-4000 | 2000-5000 | 1000-2000 |
| Self-discharge | 3-5%/month | 3-5%/month | 15-30%/month | 2-3%/month | 2-5%/month |
| Charge efficiency | 75-85% | 80-90% | 60-80% | 95-99% | 95-99% |
| Operating temp (charge) | -20 to 50°C | -20 to 50°C | 0 to 45°C | 0 to 45°C | 0 to 45°C |
| Operating temp (discharge) | -30 to 60°C | -30 to 60°C | -20 to 45°C | -20 to 60°C | -20 to 60°C |
| Max charge rate | 0.1-0.3C | 0.1-0.2C | 0.2-0.5C | 0.5-1C | 0.5-1C |
| Max discharge rate | 5-10C (burst) | 1-3C | 1-2C | 2-5C | 2-5C |
| Calendar life | 3-5 years | 5-10 years | 20+ years | 8-15 years | 8-12 years |
| Cycle cost | $0.05-0.15/kWh | $0.05-0.15/kWh | $0.03-0.10/kWh | $0.10-0.30/kWh | $0.10-0.25/kWh |
| Formation energy | 5-10 × capacity | 5-10 × capacity | 3-5 × capacity | 0.3-0.5 × capacity | 0.3-0.5 × capacity |
| Electrolyte | 37% H₂SO₄ | 37% H₂SO₄ | 20-30% KOH | 1 M LiPF₆ / EC:DMC | 1 M LiPF₆ / EC:DMC |

## Scaling Notes

- **Bench scale** (laboratory): Single cell, 2-10 Ah. Cast 1-2 plates by hand, form in small glass tank. Demonstrates the chemistry and validates paste formulation. Total lead inventory <1 kg.
- **Workshop scale**: 12 V, 50-100 Ah battery. 50-100 kg lead inventory, manual pasting and assembly, one battery per day. Sufficient for vehicle starting, small off-grid systems, telecom backup.
- **Production scale**: 100-1000 batteries/day. Automated grid casting (rotary or continuous strip), belt pasting, automated stacking and inter-cell welding. 5-50 tonnes/day lead throughput. Requires acid recirculation, hydrogen ventilation, and lead dust collection.

Key scaling challenges: heat management during formation (each cell generates 5-10 × its capacity in heat during formation — a 100-cell formation tank dissipates 5-15 kW); hydrogen gas evolution requires room ventilation of 10+ air changes/hour; lead dust control is a persistent occupational health challenge (Pb IDLH 100 mg/m³); grid casting throughput limits overall production rate.

For Li-ion, scaling from pouch to prismatic to cylindrical formats involves different winding/stacking equipment but similar slurry and coating processes. The dominant cost at scale is the cathode active material (40-50% of cell cost), making [lithium source](../chemistry/lithium-separation.md) and transition metal supply the strategic bottleneck.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Battery will not hold charge (rapid voltage sag after charging) | Internal short circuit from separator failure, plate growth, or paste shedding bridging plates | Discharge battery fully; open and inspect; replace shorted cells; check separator integrity; if widespread, battery is scrap — recycle lead |
| Low capacity (<70% rated) | Sulfation (hard PbSO₄ crystals on plates from prolonged undercharge), electrolyte stratification, or active material loss | Equalise charge at 2.4-2.45 V/cell for 2-4 hours to break sulfation; if sulfation is advanced (>2 months), recovery unlikely; replace electrolyte if stratified |
| Excessive water loss (electrolyte below plate tops in 2-3 months) | Overcharging (charge voltage >2.40 V/cell), high operating temperature (>50°C), or overfilling | Reduce charge voltage to 2.25-2.30 V/cell float; improve battery room ventilation; maintain electrolyte 10-15 mm above plate tops |
| Positive plate growth (plates touch casing, short to ground) | Antimony content too high (>8%), cycling at high temperature, or end-of-life grid corrosion | Reduce Sb to 4-6%; install temperature compensation on charger; replace battery if plate growth >3-5% |
| Hydrogen gas detected in battery room (>1% in air) | Overcharging or inadequate ventilation; blocked cell vents | Reduce charge rate immediately; increase ventilation to >10 ACH; check and clear all cell vent caps; never allow >4% H₂ (explosive) |
| Cell voltage reversal (cell <0 V under load) | One cell weaker than others, driven into reverse by series current during deep discharge | Check individual cell voltages; remove or bypass reversed cell; prevent by using low-voltage disconnect (LVD) at 1.75 V/cell |
| Li-ion cell swelling (pouch bulging) | Gas generation from electrolyte decomposition, overcharge, or internal contamination (moisture) | Stop use immediately — swelling precedes thermal runaway; inspect for overcharge protection circuit failure; manufacture under <1% RH to prevent moisture contamination |
| Li-ion thermal runaway | Internal short from dendrite penetration of separator, overcharge beyond 4.2-4.3 V/cell, or external heat >150°C | Quench with large volume of water (only effective method); isolate from other cells; cannot be stopped once cathode decomposition begins — focus on preventing spread to adjacent cells |

## Safety

- **Hydrogen gas**: Lead-acid batteries evolve hydrogen during charging. 4-75% explosive range in air. Ventilate battery rooms to <1% H₂; ban open flames, sparks, and smoking; use explosion-proof fans and electrical fittings.
- **Sulphuric acid (H₂SO₄, 37%)**: Severe chemical burns. pH <1. Corrodes organic tissue on contact. Mandatory: chemical splash goggles, face shield, acid-resistant gloves (neoprene or nitrile), acid apron. Eyewash station within 10 m. Immediate first aid: flush with copious water for 15 minutes.
- **Lead toxicity**: Airborne Pb IDLH 100 mg/m³ (NIOSH). Cumulative neurotoxin. Wet-process paste; local exhaust ventilation on pasting machines; respiratory protection (P100 respirator) during grid casting and pasting. Blood-lead monitoring for workers (action level: 20 μg/dL).
- **Electrical hazard**: A 12 V 100 Ah battery stores 1.2 kWh — short-circuit current exceeds 1000 A. Explosive arc flash and wire vaporisation. Use insulated tools; install fuses within 20 cm of battery terminal; never short terminals to "test" a battery.
- **Lithium fire (Li-ion only)**: Thermal runaway reaches 600-1000°C. Cannot be extinguished by smothering — the cathode releases oxygen. Flood with water (large volume) to absorb heat and prevent propagation to adjacent cells. Do NOT use CO₂ or dry powder extinguishers. Class D extinguishers are ineffective for Li-ion electrolyte fires.
- **Electrolyte toxicity (Li-ion)**: LiPF₆ decomposes in moisture to form HF (hydrogen fluoride, IDLH 30 ppm). Assembly under <1% RH prevents exposure. HF burns require immediate calcium gluconate gel treatment.

### Emergency Procedures

- Acid splash: flush 15 minutes with water; remove contaminated clothing; seek medical attention for eye contact
- Lead ingestion: seek medical attention; chelation therapy for blood-lead >40 μg/dL
- Battery fire: disconnect charger; evacuate area; use water fog on adjacent cells to prevent spread
- Li-ion thermal runaway: evacuate, isolate area 15 m minimum, flood with water from safe distance

## Quality Control

### Acceptance Criteria

- **Lead-acid capacity**: Rated capacity at 20-hour discharge rate (e.g., 100 Ah battery delivers 5 A for 20 hours to 1.75 V/cell). Accept: ≥90% of rated capacity on first cycle, ≥100% after 3 formation cycles.
- **Cold cranking amps (CCA)**: At -18°C, deliver rated current for 30 seconds to ≥7.2 V (12 V battery). Accept: ≥ rated CCA.
- **Internal resistance**: 12 V 100 Ah starter battery: 3-8 mΩ. Rising resistance indicates grid corrosion or paste shedding.
- **Electrolyte specific gravity**: Fully charged: 1.265-1.285 (37% H₂SO₄). Discharged: 1.120-1.150. SG variation between cells <0.025.
- **Li-ion cell consistency**: Voltage match within ±0.02 V across cells in a pack. Internal resistance within ±5%. Capacity within ±3%.

### Testing Methods

- Load bank test: discharge at 0.1C to 1.75 V/cell (lead-acid) or 2.5 V/cell (LFP); measure delivered Ah
- Hydrometer (lead-acid): measure electrolyte SG per cell — immediate state-of-charge indicator
- AC milliohmmeter: measure internal resistance — trending indicates aging
- Cycle life test: repeated charge/discharge at 0.5C to 80% DoD until capacity <80% of rated
- Thermal abuse test (Li-ion): heat cell at 5°C/min to 150°C; must not ignite (UL 1642 standard)

### Sampling Protocol

- 100% voltage and internal resistance check at end of formation
- 1-2% of production units to full capacity and cycle life testing
- Weekly teardown of one production cell for visual plate inspection (paste adhesion, grid corrosion, separator condition)

## Variations and Alternatives

### Lead-Acid Variants

- **Flooded (SLI)**: Traditional vented battery for vehicle starting. Cheap, reliable, 300-500 cycles to 80% depth of discharge (DoD).
- **Deep cycle (golf cart, solar)**: Thicker plates (3-4 mm), higher antimony (5-6%), 800-1500 cycles. Designed for regular deep discharge.
- **VRLA (Valve-Regulated Lead-Acid)**: AGM (absorbent glass mat) or gel electrolyte immobilises acid. Oxygen recombination makes them maintenance-free. 300-500 cycles. Used in UPS and telecom.
- **Tubular plate (OpzS)**: Positive plate is lead rods in porous tubes. Excellent deep cycle life (1500+ cycles). Industrial backup and solar.

### Alternative Battery Chemistries

| Chemistry | Voltage | Energy density | Cycle life | Bootstrappability | Key trade-off |
|-----------|---------|----------------|------------|-------------------|---------------|
| Lead-acid | 2.0 V | 30-50 Wh/kg | 300-1500 | High (lead + acid only) | Heavy, moderate cycle life |
| Nickel-iron | 1.2 V | 30-50 Wh/kg | 2000-4000 | Medium (Ni, Fe, KOH) | High self-discharge, low efficiency |
| Nickel-cadmium | 1.2 V | 40-60 Wh/kg | 1500-3000 | Medium (Cd is toxic) | Environmental hazard |
| Li-ion (LFP) | 3.2 V | 120-160 Wh/kg | 2000-5000 | Low (dry room, high purity) | Safe Li chemistry, lower energy |
| Li-ion (NMC) | 3.7 V | 200-250 Wh/kg | 1000-2000 | Low | Highest energy density |
| Sodium-sulphur | 2.0 V | 150-240 Wh/kg | 2000-4500 | Very low (350°C operation) | High-temperature, molten electrodes |
| Flow battery (vanadium) | 1.4 V | 15-50 Wh/kg | 10,000+ | Medium | See [redox flow battery](./redox-flow-battery.md) |

### Mechanical Storage Alternatives

Where batteries are unavailable or impractical: [pumped hydro](./pumped-hydro.md) (70-85% round-trip, site-dependent), compressed air energy storage (40-55%), flywheels (85-95%, short duration). These complement rather than replace electrochemical batteries — batteries excel at small-scale, mobile, and short-duration applications.

## References

- [Electroplating](../electrochemistry/electroplating.md) — electrode fabrication basis, the upstream capability for all battery types
- [Energy storage overview](./storage.md) — parent capability covering all storage modalities
- [Electricity generation](./electricity.md) — charging source and electrical infrastructure
- [Redox flow battery](./redox-flow-battery.md) — grid-scale alternative with liquid electrolytes
- [Photovoltaics](./photovoltaics.md) — primary pairing with batteries for off-grid solar systems
- [Non-ferrous metals](../metals/non-ferrous.md) — lead, nickel supply for electrode materials
- [Acids](../chemistry/acids.md) — sulphuric acid production for lead-acid electrolyte

---
*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
