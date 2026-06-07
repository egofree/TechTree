# Semiconductor-Grade Aluminum Production

> **Node ID**: metals.aluminum.semiconductor-grade
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`Basic Semiconductor Devices`](../silicon/basic-devices.md), [`Core Fab Processes`](../photolithography/fab-processes.md)
> **Enables**: [`Electricity Generation & Distribution`](../energy/electricity.md), [`Aluminum Production`](aluminum.md)
> **Timeline**: Years 40-70
> **Outputs**: semiconductor_grade_aluminum, sputtering_targets, high_purity_aluminum
> **Critical**: No

## Overview

Ultra-high-purity aluminum (5N-6N, 99.999-99.9999%) for semiconductor metallization via three-layer electrolysis (Hoopes process) and zone refining. Produces sputtering targets and evaporation sources for IC interconnect layers, bond pads, and display panel metallization. Critical impurity limits: Fe, Si below 3 ppm; uranium and thorium below 1 ppb (alpha particle emission from U/Th contamination causes soft errors in DRAM and logic devices).

The Hoopes process (three-layer electrolysis) is the primary method for producing 5N aluminum. It uses a molten salt electrolyte with three liquid layers: the bottom layer is a heavy aluminum-copper alloy anode (containing impure aluminum), the middle layer is a molten salt electrolyte (BaCl₂-NaCl-AlF₃ or similar), and the top layer is pure liquid aluminum cathode that floats on the electrolyte. Current causes aluminum to dissolve from the bottom anode layer, migrate through the salt, and deposit as pure aluminum in the top cathode layer. Impurities stay behind in the anode alloy or the salt. The three-layer density stratification is the key engineering principle: the heavy anode alloy (density ~3.0-3.5) stays at the bottom, the molten salt (density ~2.5) sits in the middle, and the pure aluminum (density ~2.3) floats on top.

Zone refining then takes the 5N aluminum to 6N purity by progressively sweeping a narrow molten zone along a long bar. Impurities that lower the melting point (most metallic impurities in aluminum) migrate with the molten zone to one end of the bar, which is cut off and recycled. Multiple passes increase purity progressively. The segregation coefficient k describes how an impurity partitions between the solid and liquid phases: impurities with k < 1 concentrate in the liquid zone and migrate to the tail end of the bar.

### Segregation Coefficients for Impurities in Aluminum

The segregation coefficient k = C_solid / C_liquid determines how effectively zone refining removes each impurity. Values well below 1.0 are easily removed; values near 1.0 are very difficult to separate.

| Impurity | Segregation Coefficient (k) | Ease of Removal | Typical Smelter Grade (ppm) | Target (5N/6N) |
|----------|------------------------------|-----------------|-----------------------------|----------------|
| Fe | 0.03 | Easy | 500-2000 ppm | <3 ppm / <0.1 ppm |
| Si | 0.12 | Easy | 300-1000 ppm | <3 ppm / <0.1 ppm |
| Cu | 0.14 | Easy | 5-50 ppm | <1 ppm / <0.1 ppm |
| Zn | 0.40 | Moderate | 20-100 ppm | <1 ppm / <0.1 ppm |
| Mg | 0.40 | Moderate | 10-50 ppm | <1 ppm / <0.1 ppm |
| Mn | 0.60 | Moderate | 5-30 ppm | <1 ppm / <0.1 ppm |
| Ni | 0.007 | Very easy | 5-20 ppm | <0.5 ppm / <0.05 ppm |
| Cr | 0.20 | Easy | 2-10 ppm | <0.5 ppm / <0.05 ppm |
| Ti | 0.50 | Moderate | 5-20 ppm | <0.5 ppm / <0.05 ppm |
| Ga | 0.14 | Easy | 30-100 ppm | <0.5 ppm / <0.05 ppm |
| U | ~0.01 | Very easy | 0.01-0.1 ppm | <0.001 ppm (1 ppb) |
| Th | ~0.01 | Very easy | 0.01-0.05 ppm | <0.001 ppm (1 ppb) |

**Why zone refining works**: After n passes with a zone length z along a bar of length L, the impurity concentration at position x follows the Pfann equation. For k = 0.1 and 10 passes, the impurity concentration at the front 70% of the bar is reduced by roughly 10³ to 10⁴ times from the starting concentration. This is why 5 passes reduce smelter-grade aluminum (0.1-0.5% Fe) to below 3 ppm Fe, and 10-20 passes achieve sub-ppb U/Th.

### Hoopes Cell Operating Parameters in Detail

| Parameter | Value | Significance |
|-----------|-------|--------------|
| Cell temperature | 720-800°C | Must keep all three layers liquid; density stratification breaks down if temperature varies >±20°C |
| Anode alloy composition | Al-Cu 30-50% Cu | Density 3.0-3.5 g/cm³ (heaviest layer) |
| Electrolyte composition | BaCl₂ 50-60%, NaCl 20-30%, AlF₃ 10-20% | Density ~2.5 g/cm³ (middle layer); melting point ~650°C |
| Cathode layer density | ~2.3 g/cm³ (pure Al) | Lightest layer, floats on electrolyte |
| Current density | 0.3-0.6 A/cm² | Higher density increases throughput but risks impurity transfer through the electrolyte |
| Cell voltage | 5-7V total | Rising voltage (>8V) signals anode passivation or electrolyte contamination |
| Current efficiency | 85-95% | Loss from side reactions and electronic short circuits between layers |
| Production rate | 0.5-2 kg Al per kAh | Depends on cell geometry and current efficiency |
| Electrolyte lifetime | 6-12 months | Degraded by impurity accumulation; reconstituted by partial replacement |

### Energy Consumption by Process Step

| Process Step | Energy (kWh/kg 5N Al) | Cumulative Energy |
|-------------|----------------------|-------------------|
| Hall-Heroult (smelter grade) | 13-15 | 13-15 kWh/kg |
| Hoopes three-layer electrolysis | 5-8 | 18-23 kWh/kg |
| Zone refining (10 passes) | 1-3 | 19-26 kWh/kg |
| Vacuum melting + target fabrication | 1-2 | 20-28 kWh/kg |

Total energy from bauxite to 5N sputtering target: approximately 20-28 kWh/kg. This is roughly 1.5-2× the energy to produce smelter-grade aluminum, with the Hoopes process being the largest additional energy consumer.

The uranium and thorium limits (below 1 ppb) deserve special attention. These radioactive elements are present in smelter-grade aluminum at trace levels. If they contaminate semiconductor metallization, alpha particle emission from the U/Th decay chains can flip bits in DRAM cells and logic devices (soft errors). Meeting the sub-ppb U/Th specification requires careful source selection and the inherent purification of the Hoopes process and zone refining.

Primary outputs: `semiconductor_grade_aluminum`, `sputtering_targets`, `high_purity_aluminum`.

The sputtering target is the end product that delivers the ultra-pure aluminum to the semiconductor fabrication process. In a sputtering system, argon ions bombard the aluminum target surface, ejecting aluminum atoms that deposit as a thin film on the silicon wafer. Any impurity in the target becomes an impurity in the thin film, which is why the 5N-6N purity specification is so strict. A single grain of dust or a trace of iron from handling tools can ruin an entire batch of integrated circuits.

## Prerequisites

### Materials

- Primary aluminum (smelter grade, 99.5-99.8% Al) from Hall-Heroult reduction
- Copper (for alloying with aluminum to form the dense bottom anode layer in the Hoopes cell)
- Barium chloride, sodium chloride, aluminum fluoride (for molten salt electrolyte)
- Graphite or carbon electrodes and cell lining materials
- Argon or nitrogen cover gas (to prevent oxidation during zone refining)
- High-purity graphite or boron nitride crucibles for zone refining and casting
- Ultrapure acids (HCl, HNO₃) for dissolving samples during ICP-MS analysis

### Equipment

- [Basic Semiconductor Devices](../silicon/basic-devices.md) — material dependency
- [Core Fab Processes](../photolithography/fab-processes.md) — material dependency
- Hoopes electrolytic cell: refractory-lined steel vessel with internal heating, three-layer configuration
- DC power supply for the Hoopes cell (low voltage, high current)
- Zone refining apparatus: RF induction or resistance heating coil on a movable carriage, with a mechanism to traverse the coil along the aluminum bar at controlled speed
- Clean casting and forming equipment for producing sputtering targets (vacuum melting, hot pressing, or rolling)
- ICP-MS (inductively coupled plasma mass spectrometry) for trace impurity analysis down to parts-per-trillion levels
- Glove box or clean room environment for handling high-purity aluminum during zone refining and target fabrication
- Die casting or continuous casting equipment for producing aluminum bar stock for zone refining

### Knowledge

- Three-layer electrolysis principles: density stratification of the three liquid layers, cell temperature control, current density optimization for smooth deposit
- Molten salt chemistry: electrolyte composition, melting point, density, conductivity, and resistance to attack by the aluminum alloy anode
- Zone refining theory: segregation coefficient (k), zone length, traverse speed, number of passes, and their effect on final impurity distribution
- Trace contamination control: how contact with crucible walls, furnace atmosphere, and handling tools introduces impurities at the ppm and ppb level
- Sputtering target fabrication: grain structure, texture, and uniformity requirements for semiconductor metallization
- GDMS (glow discharge mass spectrometry) and ICP-MS analytical methods for certifying ultra-high purity
- Clean room protocols for handling ultra-pure materials without contamination
- Understanding of grain structure and texture control in sputtering target fabrication
- Vacuum melting and casting technique for producing contamination-free aluminum slabs

### Infrastructure

- Hoopes cell installation with high-current DC supply (thousands of amps), cooling water, and fume extraction
- Zone refining room with temperature and humidity control, inert atmosphere capability, and vibration isolation
- Clean room or glove box for handling ultra-pure aluminum (any exposure to ordinary air and surfaces introduces contamination)
- Analytical laboratory with ICP-MS and/or GDMS for trace impurity certification
- Vacuum melting and casting equipment for producing sputtering targets without atmospheric contamination
- Vacuum melting and casting equipment for producing sputtering targets without atmospheric contamination
- Argon or nitrogen supply system with purifiers (oxygen and moisture below 1 ppm)
- Clean room (Class 1000 or better) for final handling, inspection, and packaging of sputtering targets
- Metallographic sample preparation equipment for grain structure analysis of targets
- Particle analysis equipment (for detecting inclusions in sputtering targets)

## Process Description

### Step-by-Step Procedure (Three-Layer Electrolysis / Hoopes Process)

1. Prepare the bottom anode layer. Melt primary aluminum and alloy with copper to form an Al-Cu alloy (typically 30-50% Cu). The high copper content makes this layer the densest of the three (density ~3.0-3.5 g/cm³). It sinks to the bottom of the cell.
2. Add the molten salt electrolyte on top of the anode alloy. The electrolyte (typically BaCl₂-NaCl-AlF₃ mixture) is formulated to have a density between the anode alloy and pure aluminum (~2.5 g/cm³). It forms the middle layer. Temperature is maintained at 720-800°C to keep all three layers liquid.
3. Add pure aluminum (from a previous run or a pure starting charge) as the top cathode layer. Pure aluminum is the lightest layer (~2.3 g/cm³) and floats on the electrolyte.
4. Apply DC current. The cell operates at low voltage (typically 5-7V total) and high current density. Aluminum dissolves from the anode alloy at the bottom, migrates through the molten salt electrolyte, and deposits as pure aluminum in the cathode layer at the top. Impurities (Fe, Si, Cu, Zn, etc.) remain in the anode alloy or dissolve into the salt.
5. Run the electrolysis for the required duration (typically 12-24 hours depending on cell size and current). Monitor cell voltage and temperature continuously. Rising voltage indicates electrolyte contamination or anode passivation.
6. Tap the pure aluminum cathode layer from the top of the cell. Cast into bars or billets for further processing (zone refining or direct target fabrication). The tapping must be done carefully to avoid disturbing the electrolyte layer and entraining salt inclusions in the product aluminum.

### Step-by-Step Procedure (Zone Refining)

1. Cast the 5N aluminum from the Hoopes process into a long bar (typically 30-80 mm diameter, 500-1500 mm long). The bar must be straight and free of surface contamination. Handle only with clean gloves in an inert atmosphere.
2. Load the bar horizontally into the zone refiner. The bar sits in a boat or cradle inside a quartz or stainless steel tube. Purge the tube with argon or nitrogen to prevent oxidation during the molten zone passes.
3. Start the molten zone heater (RF induction coil or resistance heater). A narrow band of the bar (~20-40 mm zone length) melts while the rest remains solid. The molten zone is held in place by surface tension.
4. Traverse the heater slowly along the bar (typically 10-50 mm/hour). As the zone moves, aluminum solidifies at the trailing edge and melts at the leading edge. Impurities with a segregation coefficient less than 1 (most metallic impurities in aluminum) concentrate in the molten zone and are carried to the trailing end of the bar.
5. Complete the pass and return the heater to the starting position. Repeat for multiple passes (5-20 passes depending on the required purity). Each pass increases the impurity concentration at the tail end and purifies the rest of the bar.
6. Cut off the contaminated tail end (typically 10-20% of the bar length) and recycle it. The remaining bar is now 5N-6N pure aluminum.
7. Analyze samples from the bar by ICP-MS to verify impurity levels meet the specification. Critical elements: Fe, Si, Cu, Zn, Mg, Mn, Cr, Ni, Ti, U, Th.

8. If the aluminum is destined for sputtering target production, vacuum melt the zone-refined bar and cast into a slab. Hot press, roll, or forge the slab to the target shape. Machine to final dimensions. The entire forming sequence must avoid contamination from tooling, atmosphere, and handling.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Hoopes cell temperature | 720-800°C | Must keep all three layers liquid and density-stratified |
| Hoopes cell current density | 0.3-0.6 A/cm² | Higher density increases throughput but risks impurity transfer |
| Hoopes cell voltage | 5-7V total | Rising voltage signals problems (anode passivation, electrolyte degradation) |
| Zone refining zone length | 20-40 mm | Shorter zone gives sharper separation but slower processing |
| Zone refining traverse speed | 10-50 mm/hour | Slower speed gives better separation; faster speed for less critical grades |
| Number of zone passes | 5-20 | More passes give higher purity but longer processing time |
| Crucible material | High-purity graphite, BN, or Si₃N₄ | Must not contaminate the aluminum at the ppb level |

## Safety Considerations

- **Molten salt and molten aluminum**: The Hoopes cell operates at 720-800°C with molten salt and liquid aluminum. Contact causes severe burns. Moisture in the charge causes violent steam explosions. All charge materials must be dry.
- **Barium compounds**: The electrolyte contains barium chloride. Barium compounds are toxic if ingested or inhaled as dust. Handle with gloves and avoid generating dust during electrolyte make-up.
- **Fluoride compounds**: Aluminum fluoride in the electrolyte releases hydrogen fluoride gas if exposed to moisture. HF causes severe, delayed chemical burns that may not be immediately painful. Calcium gluconate gel must be available as first aid for HF exposure.
- **High current DC**: The Hoopes cell draws thousands of amps. Accidental short circuits or ground faults can cause arc flash, fire, and electrocution.
- **Inert gas asphyxiation**: Zone refining operates under argon or nitrogen atmosphere. Argon is heavier than air and can pool in low areas, displacing oxygen. Nitrogen asphyxiation is a risk in enclosed spaces. Ensure adequate ventilation and oxygen monitoring in the zone refining room.

### Personal Protective Equipment

- Face shield and heat-resistant gloves when working near the Hoopes cell or molten aluminum
- Respiratory protection when handling barium chloride or aluminum fluoride powder (dust mask minimum, supplied air preferred for fluoride compounds)
- Safety glasses with side shields at all times
- Calcium gluconate gel readily available when handling fluoride-containing electrolyte
- Long sleeves, long pants, and leather apron in the cell area
- Heat-resistant footwear with metatarsal protection

### Emergency Procedures

- For molten aluminum or salt splash: cool the burn under running water for at least 20 minutes. Do not attempt to remove adhered metal. Seek immediate medical attention.
- For HF exposure: apply calcium gluconate gel immediately to the affected area while flushing with water. Seek emergency medical attention even if the burn appears minor. HF burns penetrate deep tissue and can cause systemic fluoride poisoning.
- For barium compound ingestion or inhalation: seek medical attention immediately. Inform medical staff of barium exposure.
- For argon or nitrogen asphyxiation: do not enter the area without supplied air. Remove the affected person to fresh air and provide CPR if needed.

## Quality Control

### Acceptance Criteria

- **Semiconductor Grade Aluminum (5N)**: Total metallic impurities below 10 ppm. Fe, Si each below 3 ppm. U and Th each below 1 ppb. Surface must be clean, smooth, and free of oxide contamination.
- **Semiconductor Grade Aluminum (6N)**: Total metallic impurities below 1 ppm. All individual trace elements below 0.1 ppm. U and Th each below 0.1 ppb.
- **Sputtering Targets**: Grain size uniform, texture controlled (for consistent sputtering rate). Surface finish meets specification. No inclusions or porosity.

### Testing Methods

- **ICP-MS (inductively coupled plasma mass spectrometry)**: The primary method for trace impurity analysis. Can detect most elements down to parts-per-trillion (ppt) levels. Dissolve a sample of the aluminum in high-purity acid (ultrapure HCl or HNO₃) and analyze. This is the certification method for semiconductor-grade material.
- **GDMS (glow discharge mass spectrometry)**: Direct solid analysis without dissolution. Can measure impurity levels down to ppb in solid aluminum. Useful for surveying many elements quickly.
- **Resistivity measurement**: High-purity aluminum has a characteristic resistivity (2.65 micro-ohm-cm at 20°C for 6N Al). Deviations indicate impurity content. A quick screening method but not definitive.
- **Hall effect and carrier lifetime measurement**: For the highest purity grades, electrical measurements can detect impurity levels below the detection limit of chemical analysis.
- **Visual inspection**: Sputtering targets must be free of surface scratches, inclusions, and discoloration. Inspect under clean room lighting.

### Sampling Protocol

- Take samples from multiple positions along each zone-refined bar (head, middle, tail) by ICP-MS
- Analyze every Hoopes cell run for impurity transfer efficiency
- Certify each sputtering target batch by GDMS or ICP-MS before shipment
- Track electrolyte composition and impurity buildup in the Hoopes cell weekly
- Maintain chain-of-custody documentation from raw material to finished product for semiconductor customers

## Scaling Notes

- **Bench scale**: Small Hoopes cell (a few kg capacity) in a laboratory. Single-bar zone refiner. Produces grams to hundreds of grams of 5N-6N aluminum. Useful for process development and analytical method validation.
- **Pilot scale**: Hoopes cell with 50-200 kg capacity. Multi-bar zone refiner with automated traverse. Produces kilograms of 5N-6N aluminum. Sufficient for small-volume specialty targets.
- **Production scale**: Large Hoopes cell (1-5 tonnes per charge). Automated multi-bar zone refiner with dozens of bars processed simultaneously. Vacuum melting and forming line for target fabrication. Produces tonnes per year of 5N-6N aluminum.

Key scaling challenges: contamination control becomes harder at larger scale. Every surface the aluminum touches (crucible, casting mold, rolling mill, handling tools) is a potential source of impurity introduction. The Hoopes cell must be operated and maintained to prevent anode alloy and electrolyte from mixing into the cathode layer during tapping. Zone refining is inherently slow (the traverse speed is limited to tens of mm/hour), so throughput scales by running many bars in parallel rather than speeding up a single bar.

Sputtering target fabrication adds another layer of complexity. The zone-refined aluminum must be formed into a disc or rectangle of specified dimensions with controlled grain structure. This typically involves vacuum melting and casting into a mold, followed by hot pressing, rolling, or forging, then machining to final dimensions. Each step must be done without introducing contamination. The grain structure of the target affects the sputtering deposition rate and uniformity, so the forming process must produce consistent, fine-grained material.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| High impurity in Hoopes cathode aluminum (>10 ppm total) | Electrolyte contaminated or degraded; anode alloy impurity buildup after multiple runs; accidental layer mixing during tapping | Replace or purify electrolyte (fresh BaCl₂-NaCl-AlF₃ mix); refresh anode alloy charge with fresh primary aluminum; tap cathode layer slowly, leaving 1-2 cm clearance above electrolyte interface |
| Anode passivation in Hoopes cell (voltage >8V) | Impurity buildup (Fe, Si oxides) on anode surface forming insulating layer; electrolyte temperature too low (<700°C) | Reduce current density by 20-30%; clean anode surface between runs by scraping oxide layer; verify cell temperature at 720-800°C with immersed thermocouple |
| Cell voltage rising progressively (>0.5V increase over 4 hours) | Electrolyte composition drift (AlF₃ depletion); short circuit between layers (entrained droplets bridging density layers) | Analyze electrolyte by XRF and adjust composition; check for turbulent mixing (reduce gas evolution by lowering current density); ensure cell is level within 2 mm over its length |
| Contamination from crucible during zone refining (Fe, C pickup) | Crucible material dissolving into the molten zone; graphite crucible at >800°C reacts with aluminum | Use higher purity crucible (99.99% graphite, or boron nitride for the highest grades); reduce zone temperature to minimum needed for melting (~660°C for Al); use boatless (floating zone) refining for 6N+ grades |
| Non-uniform purity along zone-refined bar (purity varies >3× from head to tail before cut) | Too-fast traverse speed (>50 mm/hour); inconsistent zone length (heater power fluctuations) | Slow the traverse speed to 10-30 mm/hour; stabilize heater power to ±1% (use PID controller); verify zone length is consistent (20-40 mm) with optical observation |
| Oxide inclusions in final product (detected by particle analysis >5 μm) | Air exposure during casting or handling; oxide skin on melt surface stirred in during pouring | Improve inert atmosphere control (O₂ <5 ppm in glove box); cast in vacuum (10⁻³ mbar) or high-purity argon; use bottom-pour crucible to avoid skimming oxide skin |
| Sputtering target grain structure non-uniform (grain size varies >2× across target) | Incorrect forming or heat treatment parameters; uneven deformation during rolling | Adjust hot pressing temperature to 400-500°C at 50-100 MPa; modify annealing cycle (300-400°C for 2-4 hours for recrystallization); use cross-rolling to ensure uniform deformation |
| U or Th above 1 ppb in final product | Source aluminum from smelter with high U/Th feedstock; insufficient zone passes; contaminated crucible or handling tools | Select primary aluminum from low-U/Th sources (some smelters produce <0.01 ppm U/Th); increase zone refining passes to 15-20; dedicate crucibles and tools to one purity grade only |
| Aluminum bar cracks during zone refining | Thermal stress from too-fast heating or cooling; bar too large diameter (>80 mm); insufficient support | Limit bar diameter to 30-60 mm for zone refining; heat and cool the bar gradually (pre-heat to 200°C before starting zone passes); support bar at multiple points to prevent sagging |
| Cathode layer contamination in Hoopes cell (Cu >5 ppm in product) | Tapping too deep (pulling electrolyte or anode alloy with cathode); electrolyte density shift from temperature change | Leave 5-10 mm of cathode layer above the tapping point; verify density stratification at operating temperature with test samples; tap only the top 70-80% of the cathode layer |

## Variations and Alternatives

- **Hoopes process (three-layer electrolysis)**: The standard method for 5N aluminum. Good throughput and well-established. Requires careful density management of the three liquid layers. The electrolyte must be formulated to have a density between the heavy anode alloy and the light pure aluminum, and the temperature must be held steady to maintain this density stratification.
- **Zone refining alone**: Can purify aluminum from 4N to 5N-6N without Hoopes electrolysis, but requires more passes and gives lower throughput. Suitable when a Hoopes cell is not available or for small batches of ultra-high-purity material.
- **Fractional crystallization**: An alternative to zone refining. Slowly solidify a large melt; the first solid to form is purer than the remaining liquid. Lower equipment complexity but less effective than zone refining for achieving 6N.
- **Vacuum distillation**: Aluminum can be purified by distillation under vacuum (aluminum boils at 2470°C but significant vapor pressure develops at lower temperatures under vacuum). Very high purity but energy-intensive and limited to small batches.
- **Organic electrolysis**: Aluminum can be refined by electrolysis in organic electrolytes (alkyl aluminum compounds) at low temperature. Used by some producers for the highest purity grades. The chemistry is hazardous (pyrophoric organoaluminum compounds).

### Material Handling

All handling of ultra-high-purity aluminum must avoid contamination at the ppm and ppb level. Use only clean room gloves and tools that have been validated for the purity grade being produced. Store finished bars and targets in sealed bags under inert atmosphere to prevent surface oxidation. Raw materials (primary aluminum, electrolyte salts) must be stored in dry conditions and handled with dedicated tools to prevent cross-contamination. Crucibles and casting molds must be dedicated to a single purity grade.

## References

- [Aluminum Production](aluminum.md) — parent capability
- [Metals Domain](./index.md) — domain overview and related capabilities
- [Basic Semiconductor Devices](../silicon/basic-devices.md) — upstream dependency (material)
- [Core Fab Processes](../photolithography/fab-processes.md) — upstream dependency (material)
- [Electricity Generation & Distribution](../energy/electricity.md) — downstream capability
- [Aluminum Production](aluminum.md) — downstream capability

---
*Part of the [Bootciv Tech Tree](../index.md) · [Metals](./index.md) · [All Domains](../index.md)*