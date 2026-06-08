# Water Electrolysis

> **Node ID**: chemistry.water-electrolysis
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`Electrolysis`](electrolysis.md)
> **Enables**: [`E-Methanol Synthesis`](e-methanol.md), [`Fuel Cell`](../energy/fuel-cell.md)
> **Timeline**: Years 20-40
> **Outputs**: hydrogen, oxygen
> **Critical**: No

## Overview

![AEM water electrolysis working principle with HER and OER](../images/chemistry/chemistry_water-electrolysis.png)

> *Image: Kavin Teenakul, CC BY-SA 4.0*

Electrolytic splitting of water into hydrogen and oxygen using PEM or alkaline electrolyzers. Provides high-purity hydrogen for ammonia synthesis, metal refining, and fuel cells without fossil fuel inputs.

The reaction is simple: 2H₂O → 2H₂ + O₂. The engineering is not. Three electrolyzer technologies compete. Alkaline electrolysis (KOH electrolyte, 60-90°C, nickel electrodes) is the mature, cheap route that avoids precious metal catalysts. PEM electrolysis (proton exchange membrane, 50-80°C, platinum and iridium catalysts) is more compact and responds faster to variable power input. Solid oxide electrolysis (ceramic oxide electrolyte, 700-850°C) has the highest theoretical efficiency but faces severe materials degradation from thermal cycling.

Primary outputs: `hydrogen`, `oxygen`. The hydrogen (green hydrogen when powered by renewables) feeds ammonia synthesis, e-methanol production, and fuel cells. The oxygen byproduct, once vented as waste, is now valued for steelmaking, wastewater treatment, and medical use. Both gases emerge at high purity from the cell, requiring only catalytic recombination (for trace O₂ removal from H₂) and drying.

Hydrogen from electrolysis costs roughly 5-10 times more per kilogram than hydrogen from natural gas steam reforming. The price gap closes when electricity is cheap (below $0.02/kWh) or when carbon pricing makes fossil-derived hydrogen expensive. For a bootstrapping civilization, the tradeoff is different: electrolysis requires no petroleum, no natural gas, no coal. It needs only water and electricity, making it the route to hydrogen that bypasses fossil fuel dependence entirely.

The efficiency bottleneck is the oxygen evolution reaction (OER) at the anode. Breaking the strong O-H bond and forming the O-O bond has a significant kinetic barrier. The hydrogen evolution reaction (HER) at the cathode is relatively fast with nickel or platinum catalysts. The OER overpotential is the largest single contributor to excess cell voltage, consuming 3% of total energy input for every 100 mV of overpotential. Developing better OER catalysts (mixed metal oxides, nickel-iron hydroxides) directly affects the economic viability of green hydrogen.

## Prerequisites

### Materials

- Deionized water (resistivity above 1 MΩ·cm; impurities poison electrodes and degrade membranes)
- Potassium hydroxide (KOH, 25-30% by weight) for alkaline electrolysis
- Nickel electrodes or nickel-coated steel for alkaline cells
- Perfluorinated sulfonic acid membrane (Nafion or equivalent) for PEM cells
- Platinum catalyst (cathode) and iridium or ruthenium oxide catalyst (anode) for PEM cells

### Equipment

- [Electrolysis](electrolysis.md) — tool dependency (DC power supply, cell frames, bus bars)

### Knowledge

- Faraday's law applied to hydrogen production rate calculations (1 Faraday = 96,485 C produces 1 gram-equivalent of H₂)
- Cell voltage decomposition: thermodynamic minimum (1.23V at 25°C) plus anode overpotential, cathode overpotential, electrolyte resistance, and membrane resistance
- Hydrogen gas handling: purging, leak testing, flashback arrestor operation
- KOH electrolyte management: concentration monitoring, impurity accumulation, replacement schedules

### Infrastructure

- DC power supply sized for the electrolyzer stack (voltage and current per cell design)
- Hydrogen collection and storage system (gas holder, compressor, or low-pressure buffer tank)
- Ventilation adequate for hydrogen (lighter than air, accumulates at ceiling level) and oxygen (accelerates fire)
- Deionized water supply (distillation or reverse osmosis, minimum 1 MΩ·cm)

## Process Description

In an alkaline electrolyzer, concentrated KOH solution (25-30% by weight, specific gravity 1.23-1.28) fills the cell. At the cathode, water molecules accept electrons and split into hydrogen gas and hydroxide ions: 2H₂O + 2e⁻ → H₂ + 2OH⁻. At the anode, hydroxide ions release electrons to form oxygen and water: 2OH⁻ → ½O₂ + H₂O + 2e⁻. A diaphragm (asbestos, polypropylene, or polysulfone fabric) separates the two electrode compartments to prevent the hydrogen and oxygen from mixing.

The cell voltage at operating conditions is 1.8-2.2V, significantly above the thermodynamic minimum of 1.23V. The difference is lost as heat: anode overpotential (the oxygen evolution reaction is kinetically sluggish), cathode overpotential (smaller, hydrogen evolves readily on nickel), electrolyte resistance (proportional to KOH concentration and gap between electrodes), and diaphragm resistance. Every 100 mV of excess voltage above the thermoneutral voltage (1.48V) represents roughly 3% additional energy consumption.

PEM electrolyzers replace the liquid KOH with a solid polymer membrane that conducts protons (H⁺). Water feeds the anode, where it oxidizes to oxygen, protons, and electrons. Protons migrate through the membrane to the cathode and reduce to hydrogen. The membrane itself is the separator, electrolyte, and gas barrier in one layer. PEM cells run at higher current density (5-20 kA/m² vs. 2-4 kA/m² for alkaline), making them more compact for the same production rate. They also respond to power changes in seconds rather than minutes, matching intermittent renewable generation better.

Solid oxide electrolysis cells (SOEC) operate at 700-850°C using a ceramic yttria-stabilized zirconia (YSZ) electrolyte that conducts oxide ions (O²⁻). Steam feeds the cathode, where it reduces to hydrogen and oxide ions. The oxide ions migrate through the ceramic to the anode and release as oxygen. The high temperature means part of the energy to split water comes as heat rather than electricity, pushing theoretical efficiency above 100% of hydrogen's lower heating value. The catch is materials: thermal cycling cracks the ceramic, seals fail at high temperature, and electrode delamination limits cell life to 10,000-20,000 hours.

Alkaline electrolyzers have a key advantage for bootstrapping: they do not require precious metal catalysts. Nickel electrodes are adequate for both anode and cathode. PEM electrolyzers, by contrast, need platinum (cathode) and iridium or ruthenium (anode), all scarce and expensive. PEM technology becomes attractive later when higher current density and faster dynamic response are needed for coupling with intermittent renewable electricity. The starting point for any civilization without an established precious metals supply chain is alkaline.

The hydrogen from electrolysis is born pure. The only impurities are traces of oxygen (from crossover through the diaphragm or membrane) and water vapor. For most chemical applications (ammonia synthesis, methanol production), simple catalytic recombination (trace O₂ + H₂ → H₂O over a platinum catalyst) and drying produce gas of adequate quality. For fuel cell applications, even trace carbon monoxide (which can form from carbon contamination on electrodes) must be removed because it poisons the platinum catalyst in PEM fuel cells at concentrations above 10 ppm.

Hydrogen storage options vary by scale and pressure requirement. Small operations can use low-pressure gas holders (an inverted bell in a water seal, atmospheric pressure, simple but bulky). Larger systems use steel cylinders at 200 bar or composite overwrap pressure vessels at 350-700 bar. Compression from atmospheric to 200 bar consumes 10-15% of the hydrogen's energy content. Storage at intermediate pressure (30-50 bar) in steel vessels is a reasonable compromise for many applications. Cryogenic liquid hydrogen storage (at -253°C) is energy-intensive (30-40% of the hydrogen's energy content for liquefaction) and is used only where maximum energy density is required (rocket fuel, long-range transport).

Oxygen, the byproduct, is often undervalued. In a chemical complex, electrolytic oxygen feeds steelmaking (basic oxygen furnace), wastewater treatment (activated sludge aeration), and medical applications. Where oxygen demand exists, it offsets part of the electrolysis cost. Where it does not, oxygen is vented to atmosphere with no environmental harm.

### Step-by-Step Procedure

1. Prepare KOH electrolyte by dissolving potassium hydroxide pellets in deionized water to 25-30% concentration. Verify specific gravity with a hydrometer (target 1.23-1.28 at 25°C). Allow the solution to cool; dissolution is exothermic.
2. Assemble the electrolyzer stack: install electrodes, diaphragms, and gaskets in the cell frame. Tighten bolts evenly in a cross pattern to avoid warping. Pressure test with nitrogen at 1.5× operating pressure to verify leak-tightness.
3. Fill the electrolyte circuit with KOH solution. Purge both gas compartments with nitrogen for 10 minutes to displace air. Never energize the cell with air present; the hydrogen-air mixture is explosive.
4. Apply DC current at a low initial value (25% of rated). Monitor cell voltage, gas production rate, and gas purity. Ramp current to rated value over 30-60 minutes while watching for voltage instability (indicates gas accumulation or poor electrolyte circulation).
5. At steady state, verify hydrogen purity with a portable analyzer (target >99.5% H₂). Check for oxygen crossover (trace O₂ in the hydrogen stream indicates diaphragm degradation). Record cell voltage, current, and temperature every hour.
6. For shutdown, reduce current to zero over 10 minutes. Continue nitrogen purge for 15 minutes after current stops to flush residual hydrogen. Never open the cell to air while hydrogen is present. After cooling, inspect the diaphragm for damage and the electrodes for discoloration or pitting that would indicate impurity buildup in the electrolyte.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Cell voltage (alkaline) | 1.8-2.2V | Below 1.6V indicates internal short circuit; above 2.5V signals fouling or electrode failure |
| Current density (alkaline) | 2-4 kA/m² | Higher density increases production rate but also voltage and heat generation |
| Current density (PEM) | 5-20 kA/m² | PEM handles much higher density due to thinner electrolyte layer |
| Operating temperature | 60-90°C (alkaline), 50-80°C (PEM), 700-850°C (SOEC) | Higher temperature reduces thermodynamic voltage but accelerates corrosion and membrane degradation |
| KOH concentration | 25-30% by weight | Below 20% increases resistance; above 35% promotes crystallization and clogging |
| H₂ production rate | ~0.4-0.5 Nm³/kWh (alkaline) | Energy consumption: 50-55 kWh/kg H₂ (thermodynamic minimum is 33 kWh/kg) |
| Stack lifetime | 60,000-80,000 hours | Membrane/diaphragm degradation is the primary limit. Electrodes last longer. |

## Safety Considerations

Hydrogen is the most dangerous gas handled in most chemical plants. Its flammability range in air is extraordinarily wide (4-75%), its ignition energy is tiny (0.017 mJ, less than a static spark), and its flame is nearly invisible in daylight. Hydrogen fires are often detected by the heat they radiate rather than by visible flame. The gas is lighter than air and accumulates at the ceiling, making ceiling-level gas detectors mandatory.

Oxygen enrichment from electrolysis leaks turns ordinary combustible materials into fierce fire hazards. Clothing that barely smolders in normal air (21% O₂) burns vigorously at 30% oxygen. Oil on a wrench handle can ignite spontaneously in oxygen-enriched atmospheres. Keep all hydrocarbon materials (lubricants, gaskets, cleaning solvents) away from the oxygen gas handling system.

- **Hydrogen explosion**: The primary risk. Every joint, valve, and fitting in the hydrogen system is a potential leak point. Use welded or brazed connections wherever possible. Install flashback arrestors on all hydrogen lines. Purge with nitrogen before introducing hydrogen and after shutdown.
- **KOH chemical burns**: Concentrated potassium hydroxide (25-30%) causes severe skin and eye damage. KOH burns are insidious because the pain is delayed while tissue damage continues. Emergency flushing within seconds is essential for eye exposure. KOH is also slippery on floors; clean spills promptly to prevent slips.
- **Electrical hazards**: Electrolyzer stacks operate at 100-400V DC with currents of 2-20 kA. Both voltage and current are in the lethal range. Insulate all bus bars and cell terminals. Lockout/tagout during maintenance. Wet electrolyte on surfaces creates conductive paths.
- **Oxygen enrichment hazards**: Electrolysis produces pure oxygen at the anode. Leaks in the oxygen system raise local O₂ concentration. Materials that barely smolder in normal air (21% O₂) burn vigorously at 30% oxygen. Oil on a wrench handle can ignite spontaneously in oxygen-enriched atmospheres. Keep all hydrocarbon materials away from oxygen gas handling.

### Personal Protective Equipment

- Chemical splash goggles and face shield for electrolyte handling and cell maintenance
- Neoprene or butyl rubber gloves (KOH penetrates nitrile and latex)
- Flame-retardant clothing when working near operating hydrogen systems
- Hydrogen gas detector badge or portable monitor when entering the electrolyzer room
- Insulated tools for any work near bus bars or cell terminals

### Emergency Procedures

- **Hydrogen leak detected**: Shut off DC power. Do not operate electrical switches (arcing ignites hydrogen). Open ventilation dampers. Evacuate and let the gas disperse. Re-enter with a hydrogen detector to locate the leak. Hydrogen rises; check ceiling-level fittings and vents first.
- **Hydrogen fire**: Shut off hydrogen supply if possible. Do not attempt to extinguish a hydrogen flame unless the supply can be isolated; extinguishing the flame while gas flows creates an explosion hazard. Let it burn if the supply cannot be stopped. Cool surrounding equipment with water spray. The hydrogen flame is nearly invisible in daylight; look for heat ripples and listen for a roaring sound.
- **KOH splash**: Flush immediately with water for 15 minutes minimum. For eye contact, use the eyewash station continuously and seek medical attention. Remove contaminated clothing while flushing. Do not neutralize with acid (the neutralization reaction generates heat).
- **Electrical shock**: De-energize the rectifier before approaching the victim. Do not touch the victim until the circuit is broken. Administer first aid for electrical burns and cardiac arrest.

## Quality Control

### Acceptance Criteria

- **Hydrogen**: Purity >99.5% by volume (alkaline) or >99.99% (PEM). Oxygen content below 0.2% (alkaline) or 0.01% (PEM). Moisture below 10 ppm (after drying). Carbon monoxide below 1 ppm for fuel cell applications.
- **Oxygen**: Purity >99.0% by volume. Hydrogen content below 2%. Moisture below 50 ppm after drying.

### Testing Methods

- **Gas chromatography**: The standard method for H₂ and O₂ purity measurement. Detects H₂, O₂, N₂, CH₄, CO, and CO₂ in a single analysis. Requires calibration with certified gas standards.
- **Catalytic recombination efficiency**: Pass product hydrogen over a platinum catalyst bed. Any trace oxygen recombines with hydrogen to form water. Measure oxygen content before and after to verify the recombination unit is working.
- **Current efficiency**: Calculate from hydrogen production rate vs. Faraday's law prediction. Current efficiency = (actual H₂ produced / theoretical H₂ from current × time) × 100. Values below 95% indicate current leakage, gas crossover, or parasitic reactions.
- **Cell voltage monitoring**: Track voltage per cell over time. A cell whose voltage deviates more than 0.1V from its neighbors needs investigation (electrode degradation, diaphragm fouling, or electrolyte flow blockage).

### Sampling Protocol

- Continuous hydrogen purity monitoring with an in-line thermal conductivity detector (TCD) or paramagnetic oxygen analyzer
- Weekly gas chromatography verification of product hydrogen
- Daily current efficiency calculation from hydrogen production rate and current reading
- Monthly diaphragm integrity check: shut down the cell and measure gas crossover rate with nitrogen pressure test

## Scaling Notes

- **Bench scale (single cell, 10-100 cm², 1-10 A)**: Laboratory power supply, glass or acrylic cell, hand-cut diaphragm. Produces milliliters of H₂ per minute. Demonstrates the principle and measures electrode overpotentials. Useful for testing new electrode materials or diaphragm fabrics.
- **Pilot scale (5-50 cells, 0.1-0.5 m² each, 100-1000 A)**: Purpose-built electrolyzer stack, dedicated rectifier, gas collection and purification. Produces kilograms of H₂ per day. Reveals issues with electrolyte circulation, gas-liquid separation, and heat management that don't appear at bench scale.
- **Production scale (100-200 cells, 1-4 m² each, 5-30 kA)**: Industrial filter-press stack, HVDC rectifier, hydrogen compression and storage, oxygen venting or capture. Produces tonnes of H₂ per day. Requires full-time operation and a maintenance schedule for electrode inspection, electrolyte replacement, and diaphragm changes.

Alkaline electrolyzers scale more easily because the electrodes and diaphragms are made from common materials (nickel, steel, polypropylene fabric). PEM electrolyzers scale with difficulty because the catalysts (Pt, Ir) are scarce and expensive, and the membrane fabrication requires specialized fluoropolymer chemistry. A bootstrapping civilization should start with alkaline and add PEM only when the materials supply chain can support it.

Stack lifetime is determined by diaphragm or membrane degradation. Alkaline diaphragms last 5-10 years. PEM membranes last 40,000-80,000 operating hours (5-10 years at continuous operation). Electrodes degrade more slowly (nickel electrodes in alkaline cells last 10+ years; PEM catalysts lose activity through dissolution and agglomeration over 5-8 years).

The energy economics of water electrolysis are dominated by the cell voltage. Every 100 mV of excess voltage above the thermoneutral voltage (1.48V at 25°C) adds roughly 3% to energy consumption. A cell running at 2.0V uses 35% more electricity per kg of H₂ than the thermodynamic minimum. Reducing voltage through better electrodes (lower overpotential), thinner electrolyte gaps (lower resistance), and improved membrane conductivity directly translates to lower hydrogen production cost. This is why electrode materials research (nickel-molybdenum alloys for HER, nickel-iron hydroxides for OER) has such economic significance.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| H₂ purity below 99.5% | Trace O₂ leaking through degraded diaphragm; or KOH mist carryover in gas stream | Replace diaphragm. Install or repair gas-liquid separator. Add catalytic recombination unit to convert trace O₂ + H₂ → H₂O. |
| Cell voltage rising above 2.5V per cell | Electrode fouling (mineral deposits from impure water); electrolyte concentration drift; or diaphragm clogging | Switch to deionized water feed. Check KOH concentration (target 25-30%). Replace or clean diaphragm. |
| Electrolyte level dropping despite water feed | Leak in cell body or gasket; or excessive evaporation from overheating | Inspect cell for leaks (check floor for alkaline residue). Verify cell temperature is within range (60-90°C for alkaline). Replace failed gaskets. |
| Current efficiency below 90% | Significant gas crossover through diaphragm; parasitic reactions from impurities in electrolyte; or electrical short circuit between cells | Replace diaphragm. Replace contaminated electrolyte. Check for metallic debris bridging electrode gaps. |
| Hydrogen detected in oxygen stream | Diaphragm breach allowing H₂ to cross to anode compartment. Dangerous: H₂/O₂ mixture is explosive above 4% H₂. | Shut down immediately. Replace diaphragm. Verify gasket compression is even. Pressure test new diaphragm before restarting. |
| KOH concentration rising over time | Water consumption by electrolysis not fully replaced by feed water; or feed water rate too low | Increase deionized water feed rate. Monitor KOH specific gravity weekly. Dilute with DI water when concentration exceeds 30%. |

## Variations and Alternatives

- **Solid oxide electrolysis (SOEC)**: Operates at 700-850°C with a ceramic oxide electrolyte. Highest theoretical efficiency because heat supplies part of the splitting energy. Limited by thermal cycling degradation, seal failure, and electrode delamination. Best suited for continuous baseload operation with steady heat source (nuclear or concentrated solar).
- **Anion exchange membrane (AEM) electrolysis**: Combines the non-precious-metal advantage of alkaline with the compactness of PEM. Uses a membrane that conducts OH⁻ instead of H⁺. Still in development; membrane stability in alkaline conditions is the main challenge.
- **Steam methane reforming (SMR)**: CH₄ + H₂O → CO + 3H₂ at 700-1000°C over a nickel catalyst. The dominant industrial route to hydrogen (95% of production). Cheaper than electrolysis by a factor of 5-10. Requires natural gas and produces CO₂. Not viable without fossil fuel feedstock.
- **Coal gasification**: C + H₂O → CO + H₂ at 900-1000°C. Another fossil route to hydrogen. Higher CO₂ emissions than SMR. Relevant where coal is abundant and natural gas is not.

## References

- [Chemistry](index.md) — parent capability
- [Chemistry Domain](./index.md) — domain overview and related capabilities
- [Electrolysis](electrolysis.md) — upstream dependency (tool)
- [E-Methanol Synthesis](e-methanol.md) — downstream capability
- [Fuel Cell](../energy/fuel-cell.md) — downstream capability

### Material Handling

Hydrogen storage requires pressure vessels rated for the operating pressure. Small operations can use low-pressure gas holders (inverted bell in a water seal, atmospheric pressure, bulky but simple). Larger systems use steel cylinders (200 bar) or composite overwrap pressure vessels (350-700 bar). Never store hydrogen in unvented indoor spaces; it accumulates at the ceiling and forms explosive mixtures.

KOH electrolyte is corrosive and reacts with skin, aluminum, zinc, and many organic materials. Store in HDPE or steel containers. KOH absorbs CO₂ from air to form potassium carbonate, which precipitates and clogs the electrolyte circuit. Keep electrolyte tanks covered. Monitor carbonate buildup; when it interferes with circulation or raises cell voltage, replace the electrolyte.

Deionized water quality directly affects electrolyzer life. Calcium and magnesium in feed water precipitate as hydroxides in the alkaline electrolyte, clogging diaphragms and coating electrodes. Silica deposits on electrode surfaces and increases overpotential. Feed water resistivity should be above 1 MΩ·cm (preferably above 10 MΩ·cm for PEM cells).

Nickel electrodes should be stored dry before installation. Once wetted with KOH, they should remain in electrolyte or be rinsed and dried promptly. Nickel surfaces that have been in alkaline service develop a beneficial oxide layer; do not acid-clean this off.

The energy economics of water electrolysis set hard constraints on where and when it makes sense. At $0.05/kWh (typical grid electricity in many regions), hydrogen costs $2.50-2.75/kg from alkaline electrolysis. At $0.02/kWh (cheap hydroelectric or optimal solar), the cost drops to $1.00-1.10/kg, approaching parity with steam methane reforming ($1.00-1.50/kg depending on natural gas prices). For a civilization with abundant renewable electricity and no fossil fuel infrastructure, water electrolysis is not just the clean option, it is the only option for large-scale hydrogen production.

Electrolyte management in alkaline systems deserves attention. KOH is not consumed by the electrolysis reaction; only water is split. The electrolyte circulates in a closed loop, with deionized water added continuously to replace what is consumed. Over time, impurities accumulate: iron from corrosion of steel components, calcium and magnesium from imperfect feed water, and carbonate from CO₂ absorption from the air. These impurities increase electrolyte resistance (raising cell voltage) and can deposit on electrodes and diaphragms (reducing active area and blocking flow). Electrolyte replacement every 5-10 years, depending on feed water quality, is standard practice. The spent electrolyte is neutralized with acid and disposed of as salt solution.

The stack design for alkaline electrolyzers uses a filter-press configuration: flat bipolar plates separate individual cells, with electrolyte flowing through the gap between plates and gas collecting at the top of each cell. The bipolar plate is the electrical connection between cells: one side acts as the cathode of one cell, the other side acts as the anode of the adjacent cell. Gaskets between plates seal the electrolyte and gas compartments. The entire stack is clamped together by tie rods under tension. A typical stack has 50-200 cells in series, with an active area of 0.5-4 m² per cell. The electrolyte circulates through the stack by thermal convection or a small circulation pump.

PEM electrolyzers use a different stack architecture. The membrane-electrode assembly (MEA) consists of the proton exchange membrane with catalyst layers coated directly on both surfaces, sandwiched between porous titanium current collectors (anode side) and carbon paper or cloth (cathode side). The entire assembly is compressed between flow field plates that distribute water to the anode and collect hydrogen from the cathode. The compact cell design (no liquid electrolyte gap) is what allows the higher current density. But every component must be made from materials compatible with the acidic environment inside the cell: titanium on the anode side, carbon or platinum-coated titanium on the cathode side. No steel or copper can contact the membrane.

The power supply for water electrolysis must deliver DC at the voltage and current required by the stack. A 100-cell alkaline stack at 2.0V per cell needs 200V DC. At 5 kA, this is 1 MW of electrical input, producing roughly 100 kg H₂ per hour. Silicon diode rectifiers converting 3-phase AC to DC are standard. For a civilization without semiconductor manufacturing, alternatives include rotary converters (AC motor mechanically driving a DC generator), mercury arc rectifiers (historical, 1920s-1960s technology), or simply a DC generator driven by a steam engine or water wheel. The rectifier efficiency matters: a 95% efficient rectifier wastes 50 kW as heat at 1 MW input, requiring water-cooled heat sinks.

The oxygen byproduct is often overlooked in planning but has real economic value. Electrolytic oxygen is pure (above 99%) and dry, suitable for steelmaking (basic oxygen furnace), medical use (hospital oxygen supply), wastewater treatment (activated sludge aeration), and chemical synthesis (partial oxidation reactions). In a chemical complex, the oxygen from a water electrolysis plant can supply multiple downstream processes, offsetting 5-15% of the electrolysis electricity cost. Where no oxygen demand exists, it is vented harmlessly to atmosphere.

Hydrogen can also be used directly as a reducing agent in metallurgy. Iron ore reduction with hydrogen (direct reduction iron, DRI) produces steel without coke and without CO₂ emissions, replacing the blast furnace route. This application requires enormous hydrogen volumes: roughly 60 kg H₂ per tonne of steel. A single DRI plant producing 1 million tonnes of steel per year would consume 60,000 tonnes of hydrogen, requiring roughly 3 GW of electrolyzer capacity running continuously. This scale of green hydrogen demand is what drives the push for cheaper, more efficient electrolysis technology.

---
*Part of the [Bootciv Tech Tree](../index.md) · [Chemistry](./index.md) · [All Domains](../index.md)*
