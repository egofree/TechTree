# Copper Refining

> **Node ID**: metals.copper-refining
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`Electronics`](../electronics/index.md), [`Electricity Generation & Distribution`](../energy/electricity.md)
> **Enables**: [`Electrolysis`](../chemistry/electrolysis.md), [`Copper & Bronze Production`](copper-bronze.md)
> **Timeline**: Years 15-25
> **Outputs**: refined-copper, electrolytic-copper, copper-cathodes
> **Critical**: No

## Overview

Purification of copper to high conductivity grades through fire refining and electrolytic refining. Fire refining removes bulk impurities by controlled oxidation in an anode furnace. Electrolytic refining produces 99.99% pure copper cathodes suitable for electrical wire and electronic components. Without electrolytic refining, copper cannot reach the purity needed for efficient electrical conductors.

Copper refining is a two-stage process. Fire refining (also called poling) takes blister copper from the smelter and removes sulfur, iron, and other impurities by oxidation in a reverberatory or rotary anode furnace. The molten copper is then "poled" by plunging green wood poles into the bath. The steam and hydrocarbon gases from the burning wood reduce excess oxygen. This produces tough-pitch copper suitable for general applications. The name "tough-pitch" comes from the fracture surface appearance of properly poled copper, which shows a columnar structure.

Electrolytic refining takes fire-refined copper anodes and dissolves them in an acidified copper sulfate solution (CuSO₄ + H₂SO₄), depositing pure copper onto starter cathodes at 0.25-0.4V and 200-300 A/m². Impurities either remain in solution or fall to the bottom as anode slimes, which are recovered for their precious metal content (gold, silver, platinum group metals). The resulting cathodes are 99.99% pure copper.

The resistance penalty from trace impurities in non-refined copper makes it unsuitable for motor windings, power transmission, and electronic interconnects. Even 0.1% impurity in copper reduces electrical conductivity by several percent. This makes copper refining a gating technology for the electrical age.

The anode slimes recovered from electrolytic refining are a significant source of precious metals. In many refineries, the value of recovered gold, silver, and platinum group metals from slimes covers a substantial portion of the refining operating cost. This economic factor makes copper refining self-sustaining once operating at production scale.

Primary outputs: `refined-copper`, `electrolytic-copper`, `copper-cathodes`.

## Prerequisites

### Materials

- Blister copper from smelting (typically 97-99% Cu with sulfur, iron, arsenic, antimony, and other impurities)
- Sulfuric acid (H₂SO₄) for electrolyte make-up
- Copper sulfate (CuSO₄) for initial electrolyte charge
- Green wood poles (for fire refining poling stage)
- Silica flux for slag formation during fire refining
- Starter cathode sheets (thin copper sheets or stainless steel blanks)
- Guar gum or similar organic additive (to improve cathode deposit smoothness in electrolytic cells)
- Refractory materials for furnace lining and anode casting molds

### Equipment

- [Electronics](../electronics/index.md) — material dependency
- [Electricity Generation & Distribution](../energy/electricity.md) — material dependency
- Reverberatory furnace or rotary anode furnace for fire refining, with fume collection hood
- Anode casting wheel or molds for casting fire-refined anodes
- Electrolytic tank house with polymeric or concrete tanks lined with lead or polymer
- DC power supply (rectifier) capable of delivering 200-300 A/m² at 0.25-0.4V per cell
- Bus bar system for connecting cells in series
- Crane or overhead lifting for handling heavy anodes and cathodes
- Cathode washing and stripping equipment
- Electrolyte circulation pumps, filters, and heating system
- Anode slime collection and storage tanks with secure, labeled containment

### Knowledge

- Oxidation-reduction chemistry: how air blowing oxidizes impurities in the fire refining stage, and how poling (green wood) reduces excess oxygen
- Electrochemical principles: Faraday's laws, current efficiency, cell voltage, and how copper dissolves at the anode and plates at the cathode
- Electrolyte chemistry management: copper concentration, acid concentration, temperature, and impurity buildup control
- Anode slime handling and precious metals recovery (gold, silver, platinum group metals collect in the slimes)
- Cell inspection and short circuit detection (dendritic growth or bent electrodes cause short circuits between anode and cathode)
- Casting technique for producing flat, straight anodes with uniform thickness

### Infrastructure

- Reverberatory furnace with fume collection system (SO₂ and particulate capture)
- Electrolytic tank house with acid-resistant flooring, drainage, and ventilation
- DC power supply sized for the number of cells (each cell runs at 0.25-0.4V, cells in series)
- Electrolyte circulation and temperature control system (50-60°C operating range)
- Anode casting area with molds and cooling
- Cathode washing, inspection, and bundling area
- Anode slime collection and secure storage (contains valuable precious metals)
- Waste acid neutralization system
- Laboratory with spectroscopic analysis capability (OES, XRF) for quick turnaround on anode and cathode composition checks

## Process Description

### Step-by-Step Procedure (Fire Refining)

1. Charge blister copper into the reverberatory or rotary anode furnace. Preheat the furnace and melt the charge to a fully liquid state (~1150-1200°C).
2. Begin the oxidation phase. Insert an air lance or turn on the tuyeres and blow air through the molten copper bath. Sulfur volatilizes as SO₂. Iron, lead, zinc, and tin oxidize and float as slag. Add silica flux to form a fluid slag layer. Skim the slag off periodically.
3. Monitor the oxidation progress by taking samples. The copper gradually loses impurities but gains dissolved oxygen. The bath surface changes appearance as impurity levels drop.
4. When oxidation is complete, begin the poling (reduction) phase. Plunge green wood poles (typically 150-200 mm diameter, 3-4 m long) into the molten copper. The wood burns fiercely, generating hydrogen, carbon monoxide, and hydrocarbon gases that reduce the dissolved copper oxide back to metallic copper.
5. Judge the endpoint by examining a fractured sample. Tough-pitch copper shows a characteristic columnar fracture pattern with a rosette appearance when the oxygen content is in the 0.03-0.05% range. Over-poled copper has a flat, silky fracture; under-poled copper has a brick-red, crystalline fracture.
6. Cast the refined copper into anode shapes (flat slabs with lugs for hanging in the electrolytic cells). Anodes are typically 0.9-1.0 m square, 30-50 mm thick, weighing 250-400 kg each. The anodes must be flat and uniform in thickness. Warped or uneven anodes cause uneven current distribution in the electrolytic cells, leading to rough cathode deposits and short circuits.

### Step-by-Step Procedure (Electrolytic Refining)

1. Prepare the electrolytic cells. Fill with acidified copper sulfate electrolyte (typically 35-45 g/L Cu, 150-200 g/L H₂SO₄). Heat to 50-60°C using steam coils or electric heaters.
2. Hang fire-refined copper anodes and pure copper starter cathodes alternately in the tanks. Typical spacing: 80-100 mm between anode and cathode faces. Anodes and cathodes must hang vertically and parallel.
3. Connect the DC power supply. Current flows from the anode (where copper dissolves) through the electrolyte to the cathode (where pure copper plates). Typical operating parameters: 0.25-0.4V per cell, 200-300 A/m² current density.
4. Monitor the cells continuously. Copper dissolves from the anode, impurities fall as anode slime or stay in solution, and pure copper plates onto the cathode. The plating cycle takes 10-28 days depending on current density and desired cathode thickness.
5. Inspect cells daily for short circuits. A short circuit occurs when a growing dendrite or a bent electrode bridges the gap between anode and cathode, bypassing current without doing useful work. Detect shorts by infrared scanning (hot spots) or voltage monitoring. Clear by physically separating the electrodes.
6. Harvest cathodes when they reach target thickness (typically 8-15 kg per cathode). Lift from the cell, wash with hot water to remove electrolyte, and inspect for surface quality.
7. Collect anode slimes from the tank bottom. Slimes contain gold, silver, selenium, tellurium, and platinum group metals. These are processed separately for precious metals recovery. Slime yield is typically 5-15 kg per tonne of anode copper, depending on the impurity content of the blister copper feed.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Fire refining temperature | 1150-1200°C | Must maintain fluid bath for air blowing and poling |
| Oxygen content after poling | 0.03-0.05% | Judged by fracture appearance (tough-pitch) |
| Electrolyte Cu concentration | 35-45 g/L | Too low: rough deposits. Too high: anode passivation |
| Electrolyte H₂SO₄ | 150-200 g/L | Provides conductivity; too much attacks anodes |
| Electrolyte temperature | 50-60°C | Higher temperature improves conductivity but increases evaporation |
| Cell voltage | 0.25-0.4V | Higher voltage wastes energy and risks impurity co-deposition |
| Current density | 200-300 A/m² | Higher density increases throughput but produces rougher deposits |
| Plating cycle | 10-28 days | Depends on current density and desired cathode weight |
| Energy consumption | 250-350 kWh/tonne cathode | Modest compared to smelting energy but significant at scale |

The energy consumption of electrolytic refining is roughly 250-350 kWh per tonne of cathode copper. This is modest compared to the energy used in smelting, but it adds up at production scale. A tank house producing 500 tonnes per day of cathode copper draws 10-15 MW of electrical power continuously. The cost of this electricity is a significant operating expense.

### Current Efficiency and Faraday's Law

The theoretical copper deposition rate follows Faraday's law: 1 gram of copper requires 2.98 ampere-hours (equivalent weight of Cu = 31.77 g/eq, Faraday constant = 96,485 C/eq). In practice, current efficiency is 85-95% because some current is lost to side reactions (hydrogen evolution, impurity dissolution) and short circuits.

| Parameter | Value | Notes |
|-----------|-------|-------|
| Cu deposited per kAh | 1.186 kg (theoretical) | Faraday's law: mass = (I × t × M) / (n × F) |
| Cu deposited per kAh (practical) | 1.01-1.13 kg | At 85-95% current efficiency |
| Anode consumption rate | 1.01-1.05× cathode weight | Anode dissolves slightly faster due to impurity mass |
| Cathode weight at harvest | 8-15 kg per plate | Depends on cycle length and current density |
| Typical cycle time | 14-21 days | At 220-280 A/m² current density |
| Slime yield | 5-15 kg per tonne anode | Higher for impure blister copper |
| Precious metal in slimes | Au: 10-1000 g/t, Ag: 500-50,000 g/t | Varies widely with ore source |

**Why current efficiency matters**: A 1% drop in current efficiency (e.g., from 92% to 91%) on a 100,000 tonne/year tank house wastes roughly 75,000 kWh/year and reduces copper production by 1,000 tonnes/year. The two main causes of current efficiency loss are short circuits (detectable by infrared scanning) and stray current leakage through grounded tank hardware (detectable by measuring current balance across the circuit).

### Anode Composition Specifications

| Impurity | Maximum in Anode (%) | Behavior in Cell |
|----------|----------------------|------------------|
| Oxygen | 0.1-0.3% | Dissolves as Cu₂O; helps anode dissolution |
| Nickel | 0.1-0.5% | Dissolves into electrolyte; must be bled off |
| Arsenic | 0.01-0.2% | Partially dissolves; must be controlled to prevent co-deposition |
| Antimony | 0.01-0.1% | Forms floating slimes; can cause cathode contamination |
| Bismuth | 0.001-0.01% | Most harmful; co-deposits at ppb levels degrade conductivity |
| Lead | 0.05-0.2% | Forms PbSO₄ slimes; generally benign |
| Selenium | 0.01-0.1% | Reports to slimes as Cu₂Se, Ag₂Se |
| Tellurium | 0.001-0.01% | Reports to slimes; toxic in electrolyte |
| Sulfur | 0.001-0.01% | Dissolves as sulfate; controlled by electrolyte bleed |
| Silver | Variable | Reports to slimes (valuable recovery) |
| Gold | Variable | Reports to slimes (valuable recovery) |

Anodes with Bi >0.01% or As + Sb + Bi >0.3% require special electrolyte treatment or modified current density to prevent cathode contamination.

## Safety Considerations

- **SO₂ gas**: The fire refining stage produces sulfur dioxide when air is blown through blister copper. SO₂ is a respiratory irritant. The furnace must have a fume collection system with appropriate gas handling.
- **Sulfuric acid burns**: The electrolyte is a concentrated acid solution. Skin contact causes chemical burns. Eye contact can cause permanent damage. Acid-resistant gloves, apron, and face shield are mandatory in the tank house.
- **Electrical hazard**: The tank house carries high DC current through bus bars and electrodes. Although the voltage per cell is low, the total voltage across a long series of cells can be lethal. Proper grounding, insulated tools, and dry conditions are mandatory.
- **Molten metal**: The anode furnace contains molten copper at 1150-1200°C. Spillage or splash causes severe burns. Moisture in the charge causes violent steam explosions.
- **Heavy lifting**: Anodes and cathodes are heavy (250-400 kg per anode). Mechanical lifting equipment is required. Manual handling causes crush injuries and back injuries.

### Personal Protective Equipment

- Face shield when working near the anode furnace or molten copper
- Heat-resistant gloves and leather apron in the casting area
- Acid-resistant gloves (nitrile or neoprene), rubber apron, and face shield in the tank house
- Rubber boots with non-slip soles in the tank house area where electrolyte spills occur
- Safety glasses with side shields at all times in the plant
- Respiratory protection when handling dry chemicals or during furnace operations with fume exposure

### Emergency Procedures

- For acid contact: flush with water for at least 15 minutes. Remove contaminated clothing. Seek medical attention.
- For molten metal splash: cool the burn under running water. Do not attempt to remove adhered metal. Seek immediate medical attention.
- For SO₂ exposure: move the affected person to fresh air. Provide oxygen if available. Seek medical attention if breathing difficulty persists.
- For electrical contact in the tank house: de-energize the circuit before touching the affected person. Do not grab a person who is in contact with live conductors.

## Quality Control

### Acceptance Criteria

- **Fire-Refined Copper (Tough-Pitch)**: Oxygen content 0.03-0.05%. Fracture test shows columnar structure. Suitable for casting and general fabrication.
- **Electrolytic Copper Cathodes**: Minimum 99.99% Cu. Surface smooth, dense, free of nodules, dendritic growth, or anode slime inclusions. No electrolyte residue after washing.
- **Anode Slimes**: Collected and stored for precious metals recovery. Weight and composition tracked per batch.

### Testing Methods

- **Electrical conductivity**: Refined copper must meet international conductivity standards (IACS). Electrolytic cathode copper should exceed 100% IACS (the standard is based on pure copper conductivity). Even small impurity levels reduce conductivity measurably.
- **Fracture test**: Snap a small sample of fire-refined copper and examine the fracture surface. Columnar structure with rosette appearance indicates correct oxygen content (tough-pitch). Brick-red crystalline fracture means under-poled (too much oxygen). Silky flat fracture means over-poled (too little oxygen).
- **Chemical analysis**: Drill samples from cathodes at multiple positions. Analyze for impurity elements by spectroscopy (Se, Te, Bi, Sb, As, Pb, Ni, Ag are the critical ones). Each must be below specified limits for the copper grade.
- **Density measurement**: High-purity copper has a characteristic density of 8.96 g/cm³. Deviations indicate porosity or inclusions.
- **Visual inspection**: Cathodes must be free of edge growth, nodules, slime inclusions, and surface roughness. Reject any cathode with visible defects.

### Sampling Protocol

- Drill cathode samples from at least five positions per cathode (four corners and center) for chemical analysis
- Test electrolyte chemistry daily: Cu²⁺ concentration, H₂SO₄ concentration, temperature, and trace impurity levels
- Monitor anode slime weight and composition per cell cycle
- Track current efficiency (actual copper deposited vs. theoretical from Faraday's law) as a key process metric
- Reject and investigate any cathode that fails chemical or visual standards

## Scaling Notes

- **Bench scale**: Small crucible furnace for fire refining. Single electrolytic cell in a glass or polymeric container. DC bench power supply. Grams to kilograms of refined copper. Useful for proving the process and training.
- **Pilot scale**: Small reverberatory or rotary furnace. 10-50 electrolytic cells. Hundreds of kilograms per batch. Validates current density, electrolyte management, and anode casting.
- **Production scale**: Large anode furnace (100+ tonnes per charge). Full tank house with hundreds of cells in series. Automated anode casting, cathode stripping, and handling. Tonnes per day.

Key scaling challenges: electrolytic refining requires large DC power supplies (a tank house with 500 cells at 0.3V draws ~150V total at thousands of amps). Anode casting and cathode handling are labor-intensive at any scale. Acid management, electrolyte purification, and anode slime recovery add complexity and environmental controls. The tank house floor area scales with production volume and is a significant capital investment.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Rough cathode deposit (granular, nodular) | Current density too high (>300 A/m²); contaminated electrolyte (suspended solids >10 mg/L); low Cu²⁺ (<30 g/L) | Reduce current density to 220-260 A/m²; filter electrolyte through 5-10 μm cartridge filters; add CuSO₄ to bring Cu²⁺ to 35-45 g/L |
| Anode passivation (cell voltage rises >0.5V) | Impurity buildup (PbO₂, SnO₂, Sb₂O₅) forming insulating layer on anode surface; slime layer too thick | Reduce current density by 10-20%; brush anode surfaces between cycles; check anode purity (Pb <0.2%, Sn <0.05%) |
| Short circuits in tank house (>5 per day per 100 cells) | Dendritic growth bridging 80-100 mm electrode gap; bent electrodes; fallen anode pieces | Detect by infrared scan (hot spots on bus bars) every 4-8 hours; physically separate electrodes with insulated rods; replace bent hardware; add guar gum (100-300 g/t Cu) to suppress dendrites |
| Low current efficiency (<85%) | Short circuits wasting 5-10% of current; stray current leakage through grounded tanks; impurity side reactions (Ni²⁺, As³⁺) | Clear shorts daily; check insulation on tanks and bus bars (resistance to ground >1 MΩ); treat electrolyte bleed for Ni and As removal |
| Nodules on cathode (localized bumps) | Particulate in electrolyte (anode slime fragments >1 mm); rough or pitted starter cathode surface | Filter electrolyte; improve anode slime settling (allow 4-6 hours settling after anode change); use smooth, polished starter cathodes |
| High impurity in cathode (As >5 ppm, Sb >3 ppm, Bi >0.5 ppm) | Contaminated electrolyte; impurity buildup past solubility limits (As >20 g/L in electrolyte) | Bleed and purify electrolyte (10-20% daily bleed rate); add fresh CuSO₄ and acid; check anode composition (reject anodes with As + Sb + Bi >0.3%); consider electrowinning the bleed stream for As/Sb removal |
| Over-poled fire-refined copper (flat silky fracture, O₂ <0.02%) | Poling too long or too intense; excessive hydrogen in the melt | Take frequent fracture samples during poling (every 5-10 min in the final stage); stop poling as soon as columnar rosette appears; if over-poled, re-oxidize briefly with air blast and re-pole |
| Under-poled fire-refined copper (brick-red crystalline fracture, O₂ >0.07%) | Insufficient poling time; green wood poles too wet (reduced gas generation) | Extend poling time; use dry green wood (fresh-cut hardwood, 150-200 mm diameter); monitor fracture surface every 5 min during final poling stage |
| Electrolyte temperature drifts outside 50-60°C | Steam coil leaks; heat exchanger fouling; seasonal ambient changes | Check steam coils for leaks (copper in condensate indicates leak); clean heat exchangers monthly; add supplementary electric heaters for cold climates |
| Anode slime floating rather than settling | Slime density too close to electrolyte density; gas bubbles attached to slime particles | Increase electrolyte density by raising H₂SO₄ to 180-200 g/L; add a few drops of surfactant to break gas-slime bonds; allow longer settling time before cathode harvest |

## Variations and Alternatives

- **Fire refining only**: Produces tough-pitch copper (99.5-99.7% Cu) adequate for casting, roofing, and general purposes. Insufficient purity for electrical wire (too much resistance from residual impurities).
- **Electrolytic refining**: Required for wire-grade copper (99.99% Cu). Adds significant cost and complexity but produces the purity needed for electrical applications. The gold, silver, and PGM recovered from anode slimes often offsets much of the operating cost.
- **SX-EW (solvent extraction - electrowinning)**: Alternative route for oxide ores that bypasses smelting entirely. Leaches copper from ore with sulfuric acid, extracts into organic solvent, strips with strong acid, and electroplates cathode copper. Lower capital cost but limited to oxide ore deposits. Produces cathode copper of comparable quality.
- **Hydrometallurgical pre-treatment**: Leaching and precipitation methods for removing specific impurities (arsenic, antimony) before electrolysis. Useful when feedstock has unusual contamination profiles that would poison the electrolytic cells.

### Material Handling

Copper cathodes should be stored clean and dry to prevent surface oxidation that affects downstream wire drawing. Anode slimes containing precious metals should be secured and processed promptly. Electrolyte should be stored in acid-resistant containers with proper labeling. Waste acid must be neutralized before disposal in accordance with environmental regulations.

Fire-refined anodes that are not immediately consumed in the electrolytic tank house should be stored under cover. Anodes oxidize slowly in air, forming a surface scale that increases the initial voltage when they are placed in service. Minimizing storage time between anode casting and cell loading improves cell performance.

## References

- [Metals](index.md) — parent capability
- [Metals Domain](./index.md) — domain overview and related capabilities
- [Electronics](../electronics/index.md) — upstream dependency (material)
- [Electricity Generation & Distribution](../energy/electricity.md) — upstream dependency (material)
- [Electrolysis](../chemistry/electrolysis.md) — downstream capability
- [Copper & Bronze Production](copper-bronze.md) — downstream capability

---
*Part of the [Bootciv Tech Tree](../index.md) · [Metals](./index.md) · [All Domains](../index.md)*