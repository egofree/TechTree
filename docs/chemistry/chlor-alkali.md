# Chlor-Alkali Process

> **Node ID**: chemistry.electrolysis.chlor-alkali
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`Electrolysis`](electrolysis.md)
> **Enables**: Various downstream capabilities
> **Timeline**: Years 20-35
> **Outputs**: chlor_alkali_chlorine, chlor_alkali_caustic, chlor_alkali_hydrogen
> **Critical**: No

## Overview

Electrolytic production of chlorine, sodium hydroxide (caustic soda), and hydrogen from brine (NaCl solution). Three cell types: diaphragm (asbestos separator), membrane (ion-exchange membrane, modern standard), and mercury cathode (historical, phased out due to toxicity). Chlor-alkali is the foundation of the chlor-chemical industry.

The chlor-alkali process becomes feasible once a civilization can produce purified brine, fabricate ion-exchange membranes or porous diaphragms, and supply multi-kilowatt DC power continuously. It is one of the highest-volume electrochemical operations in industry, consuming tens of megawatts at production scale. The three co-products, chlorine gas, 30-50% sodium hydroxide solution, and hydrogen gas, feed into dozens of downstream processes from PVC manufacturing to water treatment to ammonia synthesis.

The three outputs each enter distinct industrial chains: chlorine for PVC, solvents, and disinfection; caustic soda for the Bayer process (aluminum), pulp digestion, and soap; hydrogen as chemical feedstock or fuel. No single process produces more industrial chemical tonnage than chlor-alkali.

The chlor-alkali process is one of the largest-volume electrochemical processes in industry. A modern membrane cell plant consumes tens of megawatts of electricity and produces hundreds of tonnes per day of chlorine, caustic soda, and hydrogen. The products feed into an enormous range of downstream processes: chlorine for PVC plastic, solvents, and water treatment; caustic soda for pulp processing, soap manufacture, and aluminum production; hydrogen as fuel or chemical feedstock.

The three cell types represent different engineering solutions to the same fundamental challenge: how to keep the anode product (chlorine) separate from the cathode product (hydroxide and hydrogen). If chlorine contacts hydroxide, it immediately reacts to form hypochlorite and chlorate — wasting both products and creating a difficult-to-separate mixture. The diaphragm cell uses a porous barrier to slow mixing. The membrane cell uses an ion-selective polymer membrane that allows sodium ions through but blocks chloride and hydroxide. The mercury cell used an entirely different electrochemical pathway where sodium dissolved in mercury rather than forming hydroxide directly.

## Prerequisites

### Materials

- Chemicals — purified sodium chloride (salt), water for brine preparation
- Ion exchange membranes (cation exchange for membrane cells)
- Electrode materials (dimensionally stable anodes, steel or nickel cathodes)
- Brine treatment chemicals (sodium carbonate, sodium hydroxide, barium chloride)

### Equipment

- [Electrolysis](electrolysis.md) — material dependency
- DC rectifier (sized for cell current and voltage)
- Chlorine drying and compression system
- Brine purification and recirculation system
- Caustic evaporation system (for 50% concentration)

### Knowledge

- Brine electrolysis electrochemistry: the half-reactions at anode (2Cl⁻ → Cl₂ + 2e⁻) and cathode (2H₂O + 2e⁻ → H₂ + 2OH⁻), and why the separator is necessary to prevent Cl₂ + OH⁻ → ClO⁻ + Cl⁻ + H₂O
- Ion-exchange membrane selectivity: how perfluorinated cation exchange membranes pass Na⁺ while blocking Cl⁻ and OH⁻ transport
- Brine purification chemistry: precipitation of Ca²⁺ and Mg²⁺ with soda ash and caustic, sulfate removal with barium chloride, and why parts-per-million hardness levels destroy membranes
- Cell voltage monitoring as a diagnostic tool: rising voltage signals membrane fouling, electrode degradation, or gas blinding

### Infrastructure

- Workspace with ventilation appropriate to the process — cell rooms require hydrogen gas detection and forced ventilation
- Power supply matching equipment requirements — large DC rectifier (megawatt scale for production plants)
- Water supply and drainage where applicable — high-purity water for brine makeup and caustic dilution
- Waste handling and disposal facilities for process outputs — brine treatment sludge and spent membranes

## Process Description

The Chlor-Alkali process splits sodium chloride and water electrochemically. The overall reaction is 2 NaCl + 2 H₂O → Cl₂ + H₂ + 2 NaOH. The central engineering problem is keeping the anode product (chlorine) separated from the cathode product (hydroxide), because they react immediately on contact to form hypochlorite and chlorate, wasting both streams.

The overall cell reaction splits sodium chloride and water: 2 NaCl + 2 H₂O → Cl₂ + H₂ + 2 NaOH. At the anode, chloride ions oxidize to molecular chlorine gas. At the cathode, water reduces to hydrogen gas and hydroxide ions. The sodium ions migrate through the separator (membrane or diaphragm) to combine with hydroxide, forming sodium hydroxide solution. The separator prevents the chlorine and hydroxide from mixing, which would produce unwanted hypochlorite and chlorate.

### Step-by-Step Procedure

1. Prepare saturated brine from purified salt. Remove calcium, magnesium, and sulfate ions by chemical precipitation (soda ash and caustic for hardness, barium chloride for sulfate). Hardness ions destroy ion-exchange membranes; sulfate increases oxygen evolution at the anode.
2. Heat brine to operating temperature and feed to the electrolysis cell. In a membrane cell, brine flows through the anode compartment while dilute caustic flows through the cathode compartment.
3. Apply DC current to the cell. Monitor individual cell voltages — rising voltage indicates membrane fouling, electrode coating degradation, or gas blinding.
4. Collect wet chlorine gas from the anode outlet. Cool, dry with concentrated sulfuric acid, and compress for storage or pipeline transport.
5. Collect hydrogen gas from the cathode outlet. Cool and wash to remove entrained caustic. Store or use as fuel gas.
6. Withdraw concentrated caustic soda solution (typically 30-33% for membrane cells, 50% with further evaporation) from the cathode compartment.
7. Dechlorinate the depleted brine by acidification and air stripping, then resaturate with fresh salt and recycle.

### Process Parameters

| Parameter | Membrane Cell | Diaphragm Cell | Notes |
|-----------|--------------|----------------|-------|
| Current density | 20-40 mA/cm² | 15-25 mA/cm² | Higher density increases production but reduces current efficiency and electrode life |
| Cell voltage | 2.9-3.5 V | 3.0-4.0 V | Rises with membrane age, electrode wear, and gas blinding |
| Operating temperature | 80-90°C | 85-95°C | Higher temps improve conductivity (~2%/°C) but shorten membrane life |
| Current efficiency | 93-97% | 90-95% | Decreases as membrane degrades; monitor by chlorine production vs. theoretical |
| Brine purity (Ca+Mg) | <20 ppb (membrane) | <5 ppm (diaphragm) | Parts-per-billion hardness required for membrane cells; parts-per-million for diaphragm |
| Brine NaCl concentration | 300-320 g/L (saturated) | 280-310 g/L | Depleted brine from anode is resaturated and recycled |
| Caustic product strength | 30-33% (direct), 50% (evaporated) | 10-12% (direct), 50% (evaporated) | Membrane cells produce more concentrated caustic directly |
| Chlorine gas purity | >97% Cl₂ | >95% Cl₂ | Main impurities: O₂, H₂, CO₂, N₂ |
| Hydrogen purity | >99.9% H₂ | >99.5% H₂ | Trace O₂ and NaOH carryover |
| Energy consumption | 2,100-2,400 kWh/tonne Cl₂ | 2,400-2,800 kWh/tonne Cl₂ | Membrane cells are 10-15% more energy-efficient |
| Electrode life (anode) | 5-8 years (DSA coating) | 3-5 years | DSA = dimensionally stable anode (Ti/RuO₂-IrO₂) |
| Membrane life | 3-5 years | N/A (diaphragm) | Perfluorinated cation exchange membranes |

## Safety Considerations

Running thousands of amperes through brine while producing explosive hydrogen and lethal chlorine gas demands rigorous safety discipline:

- **Chlorine gas**: Extremely toxic by inhalation. Destroys lung tissue on contact with moist mucous membranes. Even brief exposure to moderate concentrations causes severe respiratory distress. Production areas must have chlorine gas detection, forced ventilation, and emergency scrubbing systems.
- **Hydrogen gas**: Explosive when mixed with air (4-75% concentration range). Cathode compartments must be continuously purged or kept under positive inert gas pressure. Ground all equipment to prevent static ignition.
- **Caustic soda**: 30-50% sodium hydroxide causes severe chemical burns. Contact with eyes can cause blindness. Full-length chemical splash protection required when handling concentrated caustic.
- **Electrical hazards**: Industrial chlor-alkali cells operate at thousands of amperes DC. Arc flash hazard is severe. All maintenance requires lockout/tagout and cell disconnection.
- **Mercury (historical cells only)**: Decontamination of legacy mercury cathode cells requires specialized hazmat procedures. Mercury vapor is a cumulative neurotoxin.

### Personal Protective Equipment

- Chemical splash goggles and face shield in all production areas
- Rubber or neoprene gloves and chemical-resistant aprons for caustic handling
- Self-contained breathing apparatus for chlorine emergency response
- Arc-rated electrical PPE for cell room maintenance
- Chlorine-rated gas masks at each exit from cell rooms

### Emergency Procedures

- Chlorine leak: evacuate downwind, activate scrubbing system, isolate leak source remotely
- Hydrogen fire: shut off hydrogen source; do not extinguish burning hydrogen until source is isolated (re-ignition risk)
- Caustic splash: flush with water for 15 minutes minimum; remove contaminated clothing immediately
- Install emergency chlorine scrubbers (caustic circulation) capable of absorbing the full chlorine inventory

## Quality Control

### Acceptance Criteria

- **Chlor Alkali Chlorine**: Must meet dryness specification (moisture below threshold for steel pipeline transport). Purity above specification with hydrogen below safety limits in the chlorine stream.
- **Chlor Alkali Caustic**: Concentration within target range (30-33% for membrane cell output, 50% after evaporation). Chlorate and chloride impurities below specification.
- **Chlor Alkali Hydrogen**: Purity adequate for intended use. Oxygen content below flammability threshold if the hydrogen is to be stored or transported.

### Testing Methods

- Gas chromatography for chlorine and hydrogen purity analysis
- Titration for caustic concentration and impurity quantification
- Conductivity and pH for on-line process monitoring of caustic product
- Moisture analysis (dew point or electrolytic) for dry chlorine gas

### Sampling Protocol

- Continuous on-line monitoring of cell voltage and current efficiency
- Periodic gas analysis from each electrolyzer to detect membrane failures early
- Caustic product sampling at each shift for concentration and impurity checks

## Scaling Notes

Moving from a laboratory H-cell to an industrial membrane electrolyzer involves these stages:

- **Bench scale**: Small H-type divided cell with laboratory membrane. Produces milliliters of chlorine and dilute caustic per hour. Demonstrates the principle and allows membrane testing.
- **Pilot scale**: Single industrial-size membrane cell or small stack (5-10 cells). Produces kilograms of chlorine per day. Validates brine purification scheme and long-term membrane performance.
- **Production scale**: Multiple electrolyzers in parallel, each containing dozens of cells. Continuous operation with automated brine recirculation, chlorine drying, and caustic concentration. Produces tonnes of chlorine per day.

Key scaling challenges: brine purification becomes the dominant cost and complexity driver at production scale. Membrane lifetime (2-5 years) determines maintenance scheduling. Current distribution across large cell areas must be uniform to prevent localized overloading and premature membrane failure.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Rising cell voltage (>0.3 V above baseline) | Membrane fouling from Ca/Mg scale, electrode coating degradation, or gas blinding (bubbles trapped at electrode surface) | Analyze brine for hardness (target <20 ppb Ca+Mg for membrane cells); clean electrodes with dilute HCl; check brine flow rate to flush gas bubbles |
| Low current efficiency (<90%) | Membrane damage allowing hydroxide back-migration from cathode to anode compartment | Test individual membranes by shutting down one cell and checking chlorine output; replace membranes with efficiency <85% |
| Chlorine detected in caustic product | Membrane pinhole failure or excessive current density causing membrane distortion | Reduce current density by 10-20%; inspect membrane with backlight for pinholes; replace damaged membrane immediately |
| Hydrogen detected in chlorine stream (>0.4% H₂) | Membrane rupture allowing hydrogen to cross to anode side — explosive hazard | Shut down affected cell immediately (>0.5% H₂ in Cl₂ is explosive); replace membrane; check for pressure differential across membrane |
| Caustic strength below target (30% for membrane cells) | Excess water in cathode compartment from seal leaks, or membrane damage allowing excessive water transport | Check gasket seals for internal leakage; adjust catholyte feed rate; verify membrane water transport number (should be 3-5 mol H₂O/mol Na⁺) |
| Anode coating wearing fast (<3 year life) | High current density (>40 mA/cm²), brine impurities (fluoride, bromide), or frequent shutdown/startup cycles | Reduce current density to 20-30 mA/cm²; improve brine purification; minimize thermal cycling of cells |
| Chlorine gas wet (moisture >50 ppm) | Insufficient drying tower capacity or concentrated H₂SO₄ exhausted in drying column | Increase H₂SO₄ circulation rate in drying tower; replace or regenerate spent acid (target <20 ppm H₂O in dry Cl₂) |
| Brine hardness spikes | Failure in brine purification system: ion exchange resin exhausted or precipitation chemicals dosed incorrectly | Regenerate or replace ion exchange resin; verify Na₂CO₃ and NaOH dosing rates (target: Ca²⁺ + Mg²⁺ <20 ppb); backflush brine filters |
| Cell room hydrogen detected in air (>1% H₂) | Cathode compartment vent blocked, or hydrogen seal leak at cell gasket | Increase cell room ventilation to 10+ air changes per hour; check cathode gas outlet for blockages; verify gasket integrity on hydrogen collection manifold |

## Variations and Alternatives

- **Membrane cell (modern standard)**: Ion-exchange membrane separator produces high-purity caustic with minimal salt contamination. Most energy-efficient of the three cell types. Requires high-purity brine.
- **Diaphragm cell**: Asbestos or polymer diaphragm separator. Lower purity caustic (contains salt). More tolerant of brine impurities. Historically dominant before membrane technology matured.
- **Mercury cathode cell (historical)**: Flowing mercury cathode forms sodium amalgam, which is decomposed separately. Produced very pure caustic but caused severe mercury contamination. Phased out globally.
- **Bipolar membrane electrolysis**: Can directly produce acid and base from salt without separate chlorine and caustic streams. Emerging technology for niche applications.

The choice of cell technology has significant implications for downstream processing. Membrane cells produce the purest caustic (essentially salt-free) and are the most energy-efficient, making them the standard for new installations. Diaphragm cells remain in service where older infrastructure exists and where the slightly lower capital cost justifies the tradeoff in caustic purity. The mercury cell is being phased out globally due to environmental contamination — mercury accumulates in the food chain and causes severe neurological damage at low concentrations.

## References

- [Electrolysis](electrolysis.md) — parent capability
- [Chemistry Domain](./index.md) — domain overview and related capabilities
- [Electrolysis](electrolysis.md) — upstream dependency (material)

The chlor-alkali process is a specific application of electrolysis technology applied to brine feedstock. It is one of the highest-volume electrochemical processes and a cornerstone of the industrial chemical industry. The chlorine, caustic soda, and hydrogen it produces feed into dozens of downstream processes across multiple technology domains.

The interdependence between chlor-alkali and other industries is extensive. Chlorine feeds PVC production (construction), pulp bleaching (paper), water treatment (public health), and solvents (chemistry). Caustic soda is essential for aluminum production (Bayer process), soap manufacturing, petroleum refining, and chemical processing. The hydrogen byproduct, once vented or flared, is increasingly captured as a fuel or chemical feedstock, improving the overall economics of the process.

Brine purification is the unsung challenge of chlor-alkali operation. Feed brine must meet stringent purity standards — calcium and magnesium levels must be reduced to parts-per-million for membrane cells, because these ions precipitate as hydroxides on the membrane surface, blocking ion transport and raising cell voltage. Sulfate must be controlled to prevent oxygen evolution at the anode, which reduces chlorine current efficiency. The purification process involves chemical precipitation, settling, and ion exchange polishing — a chemical plant in its own right, nearly as complex as the electrolysis cells it serves.

The electrode technology in chlor-alkali cells has evolved significantly. Early cells used graphite anodes, which slowly eroded during operation, contaminating the product and requiring frequent replacement. Modern cells use dimensionally stable anodes (DSA) — titanium substrates coated with mixed metal oxides (ruthenium oxide, iridium oxide) that catalyze the chlorine evolution reaction without being consumed. These anodes last for years under proper operating conditions. The cathode is typically steel or nickel, sometimes with catalytic coatings to reduce the hydrogen overpotential and lower the cell voltage.

The ion exchange membrane is the heart of a modern chlor-alkali cell. It must be highly selective for sodium ions while blocking chloride and hydroxide transport, chemically resistant to both the anolyte (acidic, chlorinated) and catholyte (strongly basic) environments, and mechanically strong enough to withstand the hydraulic pressure of the cell. Perfluorinated polymer membranes (similar to Nafion) are the standard. These membranes are expensive but long-lasting (3-5 years) and are responsible for the superior energy efficiency and product purity of membrane cells compared to older cell types.

The hydrogen byproduct of chlor-alkali is increasingly valued as a clean fuel and chemical feedstock. In the past, hydrogen was often vented or burned as waste fuel. With growing demand for hydrogen in refining, ammonia synthesis, and fuel cell applications, the chlor-alkali hydrogen stream represents a significant co-product value. The hydrogen from membrane cells is relatively pure (containing traces of oxygen and caustic), and simple catalytic purification can raise it to chemical-grade quality. This co-product credit significantly improves the overall economics of chlor-alkali operation, especially as hydrogen demand grows.

The environmental legacy of mercury cell chlor-alkali plants is a cautionary tale for industrial development. Mercury cells released mercury into waterways and the atmosphere over decades of operation, contaminating sediments and accumulating in the food chain. Even decades after closure, mercury contamination persists in the ecosystems around former plant sites. This experience illustrates the principle that process technology choices have environmental consequences lasting far longer than the economic life of the equipment. The transition to membrane technology was driven by environmental regulation, not by performance advantages — though membrane cells do offer superior energy efficiency and product purity as well.

The energy intensity of chlor-alkali production makes it sensitive to electricity pricing and availability. A large chlor-alkali plant drawing 100 MW of electricity represents a significant fraction of a small grid's total generating capacity. The process runs continuously (24/7/365) because shutting down and restarting the electrolysis cells is costly and stresses the membranes. This means the plant requires a reliable baseload power supply — intermittent renewable sources alone are not sufficient without substantial energy storage. Locating chlor-alkali plants near hydroelectric or nuclear power sources has historically been common practice for this reason.

The co-location of chlor-alkali plants with downstream chlorine consumers (PVC plants, pulp mills, water treatment facilities) reduces the need for chlorine transportation, which is desirable because chlorine gas transport carries significant risk. Pipeline delivery of chlorine between co-located plants is common in major chemical complexes. For stand-alone operations, chlorine is liquefied by compression and cooling, then shipped in insulated tank cars or cylinders. Caustic soda is typically shipped as 50% solution in insulated tank cars (to prevent freezing) or as solid flakes in bags.

For a bootstrapping civilization, the simplest chlor-alkali approach is an undivided electrolysis cell that directly produces sodium hypochlorite solution (bleach) without attempting to separate the products. This avoids the need for membrane or diaphragm fabrication at the cost of producing a mixed product. For applications requiring pure chlorine or pure caustic, the divided cell becomes necessary, but the undivided cell provides immediate value for water disinfection and textile bleaching using relatively simple equipment.


### Material Handling

Proper handling of input materials and products is essential for consistent results:

- Keep chlorine gas dry in storage and transport; trace moisture corrodes steel piping and valves rapidly, producing ferric chloride contamination and leaks
- Store 50% caustic soda in heated tanks with steam-traced piping (it freezes at 12°C); avoid contact with aluminum, zinc, and galvanized steel, which dissolve exothermically in strong base
- Purge hydrogen lines continuously and never allow accumulation; hydrogen detonates in air at concentrations as low as 4%
- Dechlorinate depleted brine by acidification and air stripping before resaturation; residual dissolved chlorine attacks ion-exchange membranes and creates hazardous fumes during brine treatment
- Track individual cell voltages daily across the electrolyzer; a cell running 0.3V above average signals imminent membrane failure

Chlorine gas must be kept dry in storage and transport — even trace moisture corrodes steel piping and valves. Caustic soda (50% solution) freezes at moderate temperatures, requiring heated storage tanks and steam-traced piping in cold climates. Hydrogen should be stored in approved pressure vessels away from ignition sources and oxidizers. Depleted brine from the cell must be dechlorinated before resaturation and recycling — residual dissolved chlorine damages ion-exchange membranes and creates hazardous working conditions during brine treatment.

Power consumption is the dominant operating cost in chlor-alkali production. The theoretical minimum energy for brine electrolysis is modest, but practical cell voltages are higher due to overpotentials at the electrodes, resistance of the electrolyte, and resistance of the membrane or diaphragm. Modern membrane cells operate close to the practical minimum, but older diaphragm cells consume substantially more electricity. Any civilization operating chlor-alkali at industrial scale must have reliable, affordable electricity generation. The process is typically located near cheap power sources and near salt supplies (salt mines, solar salt pans, or seawater).
The membrane cell has become the global standard for new chlor-alkali construction, representing the best balance of energy efficiency, product purity, and environmental performance.
The cost of perfluorinated membranes has decreased steadily as production volumes have increased, making membrane cells economically competitive even in developing regions.


---
*Part of the [Bootciv Tech Tree](../index.md) · [Chemistry](./index.md) · [All Domains](../index.md)*
