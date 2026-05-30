# Silicon Purification

> **Node ID**: silicon.purification
> **Domain**: [Silicon](./index.md)
> **Dependencies**: [`chemistry.distillation`](../chemistry/distillation.md), [`chemistry.hydrogen-silane`](../chemistry/hydrogen-silane.md), [`gas-handling.basic`](../gas-handling/basic.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 30-50
> **Outputs**: purified_silicon, polysilicon, chlorosilanes
> **Critical**: Yes — 9N+ purity polysilicon is required for all electronic-grade semiconductor devices

## Purification Pathways

### Option A: Chemical Purification (Siemens-like Process)

This is the standard industrial route to semiconductor-grade polysilicon (99.9999999%+ purity).

**Step 1: Hydrochlorination** — Convert MG-Si powder to trichlorosilane:
- **Reaction**: Si + 3HCl → SiHCl₃ + H₂ (exothermic, ~300°C, Cu catalyst). Also produces SiCl₄, SiH₂Cl₂ as byproducts.
- **Equipment**: Fluidized bed reactor (Si powder suspended in HCl/H₂ gas stream). Copper catalyst (~1% Cu in Si powder). Temperature 280-350°C. Pressure 1-5 bar.
- **Product**: Mixed chlorosilane gases + H₂. Condense at -30 to 0°C to separate liquid chlorosilanes from H₂ gas.

**Step 2: Fractional distillation** — Purify SiHCl₃:
- **Principle**: SiHCl₃ boils at 31.8°C, SiCl₄ at 57.6°C, SiH₂Cl₂ at 8.2°C. Multiple distillation columns separate these. Purity requirement: impurities <1 ppb for electronic grade.
- **Columns**: 10-30 m tall, packed with structured packing or sieve trays. Reflux ratio 10-50:1. Multiple columns in series for progressive purification.
- **Key separations**: Remove boron (BCl₃, bp 12.5°C — very close to SiHCl₃, requires many theoretical plates), phosphorus (PCl₃, bp 76°C), metal chlorides.
- **Number of distillation passes**: 2-5 for solar grade, 5-10+ for electronic grade.

**Step 3: Chemical vapor deposition (CVD)** — Decompose purified SiHCl₃ on heated silicon rods:
- **Reaction**: SiHCl₃ + H₂ → Si (solid) + 3HCl (gas). Temperature 1050-1150°C.
- **Reactor**: Bell jar (quartz or stainless steel) containing inverted-U silicon seed rods (~5 mm diameter). Resistance-heated to ~1100°C by passing current through rods (rods are conductive when hot). H₂ + SiHCl₃ gas flows around rods.
- **Deposition rate**: ~5-10 μm/min. Rods grow from 5 mm to 100-200 mm diameter over 50-100 hours. Final rods weigh 50-200 kg each.
- **Energy**: ~100-200 kWh/kg polysilicon (electricity for heating + H₂ production).
- **Purity**: 9N-11N (99.9999999% - 99.999999999% Si). Electronic grade.

**Strengths**:
- Achieves 9N-11N purity — the only route to electronic-grade silicon required for all integrated circuits
- Closed-loop TCS recycling recovers >98% of chlorosilane feedstock, reducing raw material waste

**Weaknesses**:
- Three-step process (hydrochlorination → distillation → CVD) with 100-200 kWh/kg energy consumption — the most energy-intensive step in the silicon chain
- BCl₃/SiHCl₃ separation requires distillation columns >30 m tall with >50 theoretical plates at reflux ratio >50:1

### Option B: Physical Purification (Zone Refining / Directional Solidification)

Lower purity than Siemens, but much simpler chemistry. Sufficient for solar cells (~5-7N).

**Directional solidification**:
- **Principle**: Impurities preferentially stay in liquid phase. Slowly cool silicon melt from one end → impurities segregate to last-to-freeze region (Segregation coefficient k < 1 for most impurities in Si). Cut off and discard impure tail.
- **Process**: Melt MG-Si in coated quartz or graphite crucible. Cool from bottom at ~1 cm/hour. Total time 10-30 hours depending on ingot size. Ingot diameter 150-300 mm.
- **Effective segregation coefficients**: B: 0.8 (hard to remove — close to 1), P: 0.35, Al: 0.002, Fe: 6.4×10⁻⁶ (easy to remove). Boron is the problematic impurity — it barely segregates.
- **Result**: Solar-grade silicon (~5-6N). Multiple passes improve purity. Not sufficient for electronic devices.

**[Zone refining](../glossary/zone-refining.md)** (for highest purity physical route):
- **Process**: Pass molten zone (narrow band of liquid) along solid silicon rod, repeatedly. Each pass sweeps impurities toward one end. 10-20 passes achieve ~8-9N purity.
- **Equipment**: RF induction coil or focused IR lamp creates moving molten zone. Rod rotates slowly. Under inert atmosphere (Ar) or vacuum. Very slow — ~1-5 cm/hour travel speed.
- **Limitation**: Still cannot remove boron effectively (k ≈ 0.8). Combine with another boron removal step (slag treatment: add CaO-Na₂O flux to molten Si, B partitions into slag).

**Strengths**:
- Directional solidification requires only melting and controlled cooling — no complex chemistry or hazardous gases
- Zone refining achieves ~8-9N purity with 10-20 passes, sufficient for many specialty applications

**Weaknesses**:
- Boron segregation coefficient k ≈ 0.8 makes segregation-based methods nearly useless for boron removal
- Zone refining is extremely slow at 1-5 cm/hour — throughput is orders of magnitude below Siemens process

### Boron Removal via Slag Treatment

Directional solidification and zone refining effectively remove most metallic impurities (Fe, Al, Ca — segregation coefficients << 1), but **[boron](../glossary/boron.md)** is uniquely difficult because its segregation coefficient in silicon is ~0.8 (close to 1.0). This means boron distributes almost equally between solid and liquid phases during crystallization, making segregation-based methods nearly useless for boron. Since boron is a compensating dopant that degrades solar cell efficiency, dedicated removal is essential for solar-grade silicon.

**Method**: Oxidizing slag treatment — boron is oxidized to B₂O₃ at the silicon–slag interface and dissolves into the slag phase.

**Slag systems**:
- **CaO-SiO₂**: Most common. Weight ratio CaO:SiO₂ = 40:60 to 60:40. Basicity (CaO/SiO₂) ~0.7-1.5. Additives of CaF₂ (5-15 wt%) reduce slag viscosity and improve kinetics. This system requires only lime and silica — both available early in the bootstrap chain.
- **Na₂O-SiO₂**: Alternative. Weight ratio Na₂O:SiO₂ = 20:80 to 40:60. Lower operating temperature but more aggressive toward refractory linings. Requires soda ash (Na₂CO₃), which adds a supply-chain dependency.

**Process**:
- **Temperature**: 1450-1600°C (above silicon melting point of 1414°C). Higher temperature increases boron oxidation rate and slag fluidity but also accelerates refractory erosion.
- **Slag-to-silicon ratio**: 0.5:1 to 2:1 by weight. Higher ratios increase removal but also silicon losses and energy consumption.
- **Atmosphere**: Argon or Ar/O₂ mix (0-5% O₂). Small oxygen partial pressure accelerates boron oxidation. Pure inert atmosphere relies on SiO₂ in the slag as the oxidant.
- **Contact time**: 1-4 hours with stirring (mechanical or gas bubbling). Without stirring, diffusion-limited times extend to 6+ hours.
- **Equipment**: Graphite crucible with SiC coating (resists slag corrosion) or alumina crucible. Induction heating preferred for stirring via electromagnetic forces.

**Reaction**: 4[B in Si] + 3(SiO₂ in slag) → 3Si + 2(B₂O₃ in slag). Boron partitions into slag as B₂O₃. The distribution ratio L_B = (wt% B in slag)/(wt% B in Si) typically reaches 2-5 under optimal conditions.

**Expected removal efficiency**: 70-90% per pass for CaO-SiO₂ systems. Multiple passes (2-3) can reduce boron from ~15-40 ppm in MG-Si to <1 ppm, sufficient for solar-grade silicon. Silicon yield loss to slag entrainment is typically 3-8% per pass.

**Integration with directional solidification**: Slag treatment is performed first on molten MG-Si to remove boron, followed by directional solidification to remove remaining metallic impurities. This two-step sequence produces solar-grade silicon (~5-6N) without requiring the energy-intensive Siemens chemical route.

**Strengths**:
- CaO-SiO₂ slag uses only lime and silica — both available early in the bootstrap chain with no exotic reagents
- 70-90% boron removal per pass achieves <1 ppm B from 15-40 ppm MG-Si in 2-3 passes

**Weaknesses**:
- 3-8% silicon yield loss per pass from slag entrainment — direct product waste
- Boron distribution ratio L_B of only 2-5 requires multiple passes and high slag-to-silicon ratios (up to 2:1 by weight)

## Czochralski (CZ) Crystal Growth

See [Crystal Growth & Wafering](crystal-growth.md) for CZ pulling details.

## Hydrogen Sourcing for Trichlorosilane Route

The Siemens process requires large volumes of H₂ for both the hydrochlorination step and the CVD deposition:
- **Electrolysis of water**: H₂O → H₂ + ½O₂. Most common source for high-purity H₂. Requires ~4.5-5.5 kWh per Nm³ H₂ (alkaline electrolysis at 70-80% efficiency). A polysilicon plant producing 1000 tonnes/year needs ~3,000-5,000 Nm³ H₂/hour — a dedicated electrolysis plant.
- **Chlor-alkali byproduct**: 2NaCl + 2H₂O → Cl₂ + H₂ + 2NaOH. The H₂ is a co-product. If a chlor-alkali plant exists (needed for HCl production anyway), its H₂ output can feed the silicon purification line. Synergy: Cl₂ from chlor-alkali is burned with H₂ to make HCl → HCl reacts with MG-Si → trichlorosilane.
- **Storage and delivery**: H₂ stored as compressed gas (200-350 bar) or cryogenic liquid (-253°C). Piping must be stainless steel (H₂ embrittlement of carbon steel is a long-term failure risk).

**Strengths**:
- Chlor-alkali byproduct synergy: Cl₂ → HCl → trichlorosilane, while H₂ feeds the CVD reactor — one plant supplies both key inputs
- Water electrolysis produces H₂ at 99.999%+ purity suitable for semiconductor processes

**Weaknesses**:
- A 1000 t/yr polysilicon plant needs 3,000-5,000 Nm³ H₂/hour — a dedicated electrolysis plant consuming 15-25 MW
- H₂ storage at 200-350 bar or -253°C requires specialized pressure vessels or cryogenic infrastructure

## SiCl₄ Byproduct Management

The Siemens process generates ~3-5 kg SiCl₄ per kg of polysilicon. This is a significant waste stream that must be managed:
- **Recycle to trichlorosilane**: React SiCl₄ with MG-Si powder and H₂ in a fluidized bed (hydrogenation): 3SiCl₄ + Si + 2H₂ → 4SiHCl₃. Converts low-value SiCl₄ back to useful trichlorosilane. This is the preferred route — most modern plants are closed-loop.
- **Convert to fumed silica**: Burn SiCl₄ in H₂/O₂ flame: SiCl₄ + 2H₂ + O₂ → SiO₂ + 4HCl. Produces fumed silica (Aerosil) — extremely fine amorphous SiO₂ particles (7-40 nm). Used as thickening agent, desiccant, and CMP slurry component. Valuable co-product.
- **Sell as feedstock**: SiCl₄ is used in optical fiber production (SiO₂ deposition) and as a raw material for other silicon chemicals.

**Strengths**:
- Closed-loop hydrogenation (3SiCl₄ + Si + 2H₂ → 4SiHCl₃) recycles 3-5 kg SiCl₄ per kg polysilicon back into useful feedstock
- Fumed silica co-product (Aerosil, 7-40 nm particles) commands $5-15/kg as a specialty additive

**Weaknesses**:
- SiCl₄ is produced in large volumes — a 1000 t/yr polysilicon plant generates 3,000-5,000 t/yr SiCl₄ requiring dedicated handling
- Fumed silica conversion requires H₂/O₂ flame at high temperature, adding energy cost and combustion complexity

## Waste Handling

The chlorosilane purification process generates several hazardous waste streams:
- **HCl neutralization**: Scrubber systems (packed column, caustic recirculation) neutralize HCl gas from CVD reactor exhaust. NaOH or Ca(OH)₂ scrubbing solution absorbs HCl → NaCl or CaCl₂ brine. Brine is disposed as industrial wastewater or evaporated to dry salt.
- **Chlorosilane disposal**: Unreacted or off-spec chlorosilanes cannot be dumped — they react violently with water. Controlled hydrolysis in a dedicated treatment system: spray chlorosilane into a controlled excess of water in a sealed, vented vessel. Products: SiO₂ sludge + HCl solution. Neutralize HCl, filter and dispose SiO₂ sludge as non-hazardous waste.
- **Heavy metal chlorides**: Distillation bottoms contain FeCl₃, AlCl₃, CuCl₂ collected from impurity removal. These are hazardous — treat with caustic to precipitate metal hydroxides, then dispose as hazardous waste. Recover copper from CuCl₂ if economically viable.

**Strengths**:
- NaOH scrubbing converts hazardous HCl gas to harmless NaCl brine — simple, well-established chemistry
- Controlled hydrolysis converts reactive chlorosilanes to inert SiO₂ sludge + HCl, eliminating pyrophoric hazard

**Weaknesses**:
- Chlorosilane hydrolysis generates large volumes of acidic wastewater requiring neutralization before discharge
- Heavy metal chloride distillation bottoms classify as hazardous waste, incurring $200-500/tonne disposal costs

## Energy Comparison

Energy consumption varies dramatically across the silicon processing chain. Approximate values per kg of product:

| Process | Product | Energy (kWh/kg) | Notes |
|---------|---------|-----------------|-------|
| Submerged arc furnace | MG-Si (97-99%) | 11-13 | See [mg-si-production.md](mg-si-production.md) |
| Directional solidification | Solar-grade Si (~6N) | 15-25 | Includes melting + controlled cooling |
| Zone refining | High-purity Si (~8-9N) | 50-100 | Many slow passes, low throughput |
| Siemens CVD | Polysilicon (9-11N) | 100-200 | Dominated by rod heating + H₂ production |
| Czochralski pulling | Single crystal ingot | 200-400 | From polysilicon to crystal (see [crystal-growth.md](crystal-growth.md)) |
| Float zone (FZ) | Single crystal ingot | 300-500 | RF heating, slower but no crucible contamination |

The energy intensification from MG-Si to single-crystal wafers is roughly 20-40×. A polysilicon plant is fundamentally an energy conversion facility — cheap, abundant electricity is the primary siting requirement.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Low TCS conversion (<80% Si→SiHCl₃) | Insufficient Cu catalyst or temperature too low in fluidized bed | Increase copper catalyst loading to 1-2% of Si charge; raise reactor temperature to 320-350°C; ensure Si powder is 100-500 μm for proper fluidization |
| Boron contamination persists after distillation (>1 ppb B) | BCl₃/SiHCl₃ separation inadequate — boiling points too close (12.5°C vs 31.8°C) | Increase distillation column height or add additional column in series; increase reflux ratio to >50:1; verify column packing is not channeled or flooded |
| CVD rod fracture during deposition | Non-uniform temperature along rod causing thermal stress | Check power supply stability (±1%); verify rod seed alignment — misalignment causes uneven heating; reduce deposition rate (lower TCS flow) for more uniform growth |
| Polysilicon purity below 9N | Leaks in bell jar introducing air/moisture, or contaminated TCS feed | Perform helium leak check on bell jar seals (target <10⁻⁶ mbar·L/s); re-distill TCS feed; check H₂ purity (>99.999%) |
| High SiCl₄ accumulation (closed loop not recycling) | Hydrogenation reactor not converting SiCl₄ back to SiHCl₃ | Increase hydrogenation temperature to 500-550°C; verify MG-Si powder is fresh (surface-passivated powder reacts poorly); check H₂ flow rate is sufficient |
| Zone refining unstable (molten zone drips) | FZ travel speed too fast or rod diameter exceeds surface tension stability | Reduce zone pass speed to 1-2 mm/min; verify rod diameter is ≤200 mm; check RF coil alignment — off-center coil creates asymmetric heating |
| Slag treatment poor boron removal (<50% per pass) | Slag basicity wrong, insufficient stirring, or temperature too low | Adjust CaO:SiO₂ ratio to 1:1 (basicity ~1.0); add mechanical stirring or gas bubbling; raise temperature to 1550-1600°C; increase slag-to-silicon ratio to 1.5:1 |

## Safety Hazards

Silicon purification involves some of the most dangerous chemicals in semiconductor manufacturing:
- **Pyrophoric SiHCl₃**: Trichlorosilane ignites spontaneously on contact with air (autoignition ~185°C, but can flash at room temperature if warm or in fine mist). All handling must be under inert atmosphere (N₂ or Ar) in sealed systems. Leaks produce dense white HCl/SiO₂ smoke and fire. Firefighting: CO₂ or dry chemical. Do NOT use water — it accelerates decomposition and generates HCl.
- **HCl gas**: Corrosive, causes severe respiratory burns. Concentrations >50 ppm are immediately dangerous. Scrubber systems on all vent lines. HCl monitors with automatic ventilation shutdown. Full-face respirator with acid gas cartridge for emergency entry.
- **H₂ explosion risk**: Hydrogen has an extremely wide flammable range (4-75% in air) and very low ignition energy (0.017 mJ — a static spark is sufficient). All H₂ piping must be purged with N₂ before opening. Explosion-proof electrical equipment in H₂ areas. Hydrogen detectors with automatic shutdown and ventilation.
- **Chlorosilane water reactivity**: All chlorosilanes (SiHCl₃, SiCl₄, SiH₂Cl₂) react violently with water, producing HCl gas and heat. The reaction can be explosive if water contacts bulk liquid chlorosilane. Strict segregation of water lines from chlorosilane lines. Double-walled piping for chlorosilane transfer. Secondary containment for storage tanks.
- **Personal protective equipment**: Chemical splash suit (PVC or butyl rubber), face shield, chemical-resistant gloves, self-contained breathing apparatus (SCBA) for emergency response. Standard PPE is insufficient for a major chlorosilane release — SCBA is mandatory.

## Siemens Process Detail

**Reactor construction**:
- **Bell jar**: Quartz (fused silica) or stainless steel cylindrical vessel, 500-1000 mm diameter, 1-2 m tall. Quartz is preferred for purity (no metal contamination) but is fragile and expensive. The jar must withstand atmospheric pressure on the outside when evacuated, then contain inert gas at slightly above atmospheric pressure during deposition.
- **Silicon rod assembly**: Thin silicon seed rods (~5 mm diameter, inverted U-shape) mounted on electrode feedthroughs at the base of the bell jar. Typical configurations: 2-12 rods per reactor. Each rod pair forms a U-shape with the base of the U at the top. Electrical current passes through the rods to heat them.
- **Power supply**: Direct current supply, 50-200 kW per reactor. Current passes through the silicon rods, heating them by resistive heating. As rods grow thicker, resistance decreases and current must increase to maintain temperature. Power control: ±1% stability required for uniform deposition.
- **Gas distribution**: TCS (SiHCl₃) mixed with H₂ enters the bell jar through inlet ports at the base. Gas flows upward around the heated rods. Unreacted gas and HCl byproduct exit through ports at the top. Flow rate: 50-200 g/h TCS per rod, with H₂ carrier at 2-10× stoichiometric excess.

**Deposition parameters**:
- **Temperature**: 1100-1200°C rod surface temperature. Temperature must be uniform along the rod length — hot spots grow faster (thicker), cold spots grow slower (thinner). Non-uniform growth leads to stress and potential rod fracture.
- **Deposition rate**: 5-8 μm/min. Rods grow from ~5 mm to 100-200 mm diameter over 50-100 hours. Total deposition time depends on target rod diameter and power availability. Longer runs produce larger rods but with increasing risk of fracture as the rod becomes heavier.
- **Energy consumption**: 100-200 kWh/kg polysilicon. This is the highest energy consumption step in the entire silicon production chain. The electricity heats the rods and drives the chemical reaction. A single reactor producing 50-200 kg per run (50-100 hours) draws 50-200 kW continuously.
- **Gas conversion efficiency**: ~20-30% of TCS fed to the reactor deposits as silicon on the rods. The remainder exits as unreacted TCS and intermediate species. Exhaust gas is recovered, condensed, and recycled through the distillation columns for purification and reuse. Closed-loop operation recovers >98% of the TCS.

**Strengths**:
- Produces 9N-11N purity polysilicon — the gold standard for all electronic-grade semiconductor devices
- Closed-loop TCS recycling achieves >98% feedstock recovery, keeping raw material costs manageable

**Weaknesses**:
- 100-200 kWh/kg energy consumption is the highest in the entire silicon chain — dominated by resistive rod heating
- Only 20-30% gas conversion efficiency per pass means 70-80% of TCS must be recycled through distillation columns

## Alternative Purification Methods

**Fluidized bed reactor (FBR)**:
- **Principle**: Silicon seed particles (100-500 μm diameter) are suspended in an upward gas flow of silane (SiH₄) or TCS + H₂. Silane decomposes on the heated particle surfaces, depositing silicon. Particles grow larger over time, eventually becoming too heavy for the gas flow and falling to the product collection zone. New seed particles are added continuously.
- **Energy**: 30-50 kWh/kg polysilicon, roughly 3-5× lower than Siemens process. The fluidized bed is more thermally efficient because individual particles have high surface-area-to-volume ratio, and the reactor operates as a continuous process rather than batch.
- **Product form**: Granular polysilicon (0.5-2 mm beads) rather than rods. Easier to handle and load into CZ crucibles (beads pack more densely than crushed rod chunks, reducing voids in the melt charge). But higher surface area means more potential for surface contamination.
- **Challenges**: Fine silicon dust generation (silane pyrolysis produces silicon fines that escape the reactor and plug filters). Particle agglomeration (particles stick together when they collide at high temperature). Process control is more complex than Siemens.

**Upgraded metallurgical grade (UMG-Si)**:
- **Goal**: Produce solar-grade silicon (~4N, 99.99%) at lower cost than the Siemens chemical route, using physical and chemical refining steps applied directly to MG-Si.
- **Acid leaching**: Crush MG-Si to 50-200 μm powder. Treat with HCl (hydrochloric acid) at 60-80°C for 2-6 hours. Acid dissolves metallic impurities (Fe, Al, Ca) from the grain boundaries and inclusions in the silicon particles. Filter, wash with water, dry. Removes 60-80% of Fe, 40-60% of Al, 70-90% of Ca. Multiple leach cycles improve removal.
- **Directional solidification**: Melt leached MG-Si and directionally solidify (see Option B above). Most remaining metallic impurities segregate to the last-to-freeze region (segregation coefficient k << 1 for Fe, Al, Ca). Cut off and discard the impure tail. Multiple passes improve purity.
- **Plasma refining**: Pass argon-oxygen plasma over molten silicon. The reactive plasma oxidizes boron and phosphorus (the two most difficult impurities to remove by solidification, since k ≈ 0.8 and 0.35 respectively). Boron oxidizes to B₂O₃ and evaporates; phosphorus oxidizes to P₂O₅ and evaporates. Removal efficiency: 50-80% per pass for B and P. Requires plasma torch equipment (RF or DC arc, 10-50 kW).
- **Result**: 99.99% (4N) silicon at roughly half the cost of Siemens polysilicon, sufficient for standard-efficiency solar cells (14-16%). Not pure enough for semiconductor devices.

**Strengths**:
- FBR uses 30-50 kWh/kg — 3-5× less energy than Siemens process, with continuous rather than batch operation
- UMG-Si achieves solar-grade purity at ~50% of Siemens cost, using only physical/chemical refining without complex chlorosilane chemistry

**Weaknesses**:
- FBR granular product has higher surface contamination than Siemens rods due to greater surface-area-to-volume ratio
- UMG-Si limited to 4N purity — insufficient for semiconductor devices or high-efficiency (>20%) solar cells

## Analytical Methods for Silicon Purity

**ICP-MS (Inductively Coupled Plasma Mass Spectrometry)**:
- **Principle**: Dissolve a silicon sample in HF/HNO₃ mixture. Introduce the solution into an argon plasma (~7000°C) that ionizes all elements. Ions pass through a mass spectrometer that separates them by mass-to-charge ratio. Count individual ions.
- **Detection limits**: 0.1-10 parts per billion (ppb) for most metallic impurities (Fe, Al, Ca, Cu, Ni, Na, K). The workhorse technique for monitoring impurity levels at every stage of the silicon purification chain.
- **Sample preparation**: Critical. Silicon dissolution is slow and hazardous (HF + HNO₃). Contamination from reagents, containers, and the laboratory environment is a constant concern. Use ultra-pure acids, PTFE containers, and cleanroom conditions for sample prep.

**FTIR (Fourier Transform Infrared Spectroscopy)**:
- **Principle**: Infrared light transmitted through a silicon wafer. Impurities absorb at characteristic infrared frequencies. Measure absorption peak intensities to determine impurity concentrations.
- **Interstitial oxygen**: Absorption peak at 1107 cm⁻¹. Measures dissolved oxygen (from CZ crucible dissolution) with detection limit ~10¹⁵ atoms/cm³ (0.01 ppma). Essential for characterizing CZ-grown wafers.
- **Substitutional carbon**: Absorption peak at 605 cm⁻¹. Detection limit ~5×10¹⁵ atoms/cm³. Carbon from graphite furnace components is a persistent concern in crystal growth.

**Four-point probe (resistivity and doping)**:
- **Measurement**: Four collinear tungsten probes contact the silicon surface. Outer probes pass constant current I; inner probes measure voltage V. Sheet resistance Rs ≈ 4.532 × (V/I) Ω/sq. For bulk silicon: resistivity ρ = Rs × t (wafer thickness).
- **Accuracy**: ±2% for uniform samples. Doping concentration calculated from resistivity: N ≈ 1/(q·μ·ρ), where μ is carrier mobility. Maps wafer uniformity (49 or 121 point contour maps reveal doping variations across the ingot cross-section).
- **Doping type test**: Hot probe (heated probe at one contact point, cold at another) generates a thermoelectric voltage whose polarity indicates n-type (negative voltage at hot probe) or p-type (positive voltage at hot probe).

**Glow discharge mass spectrometry (GDMS)**:
- **Principle**: Argon plasma sputters atoms directly from a solid silicon sample. Sputtered atoms ionized in the plasma and analyzed by mass spectrometer. Measures bulk impurity content without dissolution.
- **Detection limits**: 1-100 ppb for most elements. Broader elemental coverage than ICP-MS (measures everything simultaneously). Used for certification of polysilicon purity grades (6N, 9N, 11N).

## Purity Requirements by Application

**Solar grade silicon (5-7N)**:
- **Metals**: Total metallic impurities <1 ppm (Fe <0.1 ppm, Al <0.1 ppm, Ti <0.01 ppm). Metallic impurities form recombination centers that reduce minority carrier lifetime and solar cell efficiency.
- **Boron**: <0.3 ppm. Boron is a p-type dopant; excess boron compensates the intended doping and reduces cell voltage.
- **Phosphorus**: <0.5 ppm. Phosphorus is an n-type dopant with the same compensating effect as boron.
- **Carbon**: <3 ppm. Excess carbon forms SiC precipitates that disrupt crystal growth and act as recombination centers.
- **Oxygen**: <10 ppm (from CZ crystal growth). Oxygen can form thermal donors that shift resistivity, but is managed by wafer annealing.
- **Source**: Directional solidification of MG-Si (with slag treatment for boron removal), or lower-grade Siemens polysilicon.

**Electronic grade silicon (9-11N)**:
- **Total impurities**: <1 ppb for all metallic species. Individual element limits: Fe <0.1 ppb, Cu <0.1 ppb, Na <0.05 ppb, Ni <0.1 ppb, Cr <0.1 ppb. These metals diffuse rapidly in silicon and contaminate device junctions even at ppb levels.
- **Boron and phosphorus**: Each <0.1 ppb. Electrically active at concentrations far below metals (one boron atom per 10¹⁰ silicon atoms shifts resistivity measurably).
- **Carbon**: <0.5 ppm. Carbon forms SiC precipitates that act as nucleation sites for oxidation-induced stacking faults.
- **Oxygen**: 10-20 ppma for CZ-grown (inherent from crucible dissolution). For FZ-grown: <1 ppma.
- **Source**: Siemens process polysilicon only, followed by CZ or FZ crystal growth.

## Chlorosilane Chemistry

**Key compounds and properties**:

| Compound | Formula | Boiling Point | Key Property |
|----------|---------|---------------|--------------|
| Silane | SiH₄ | -112°C | Pyrophoric (ignites on air contact), used in FBR and epitaxy |
| Dichlorosilane | SiH₂Cl₂ | 8.2°C | Pyrophoric, used in LPCVD epitaxy and SiO₂ deposition |
| Trichlorosilane | SiHCl₃ | 31.8°C | Main feedstock for Siemens CVD, pyrophoric |
| Silicon tetrachloride | SiCl₄ | 57.6°C | Byproduct, recycled or sold, reacts violently with water |

**Distillation challenges**:
- **SiHCl₃ / BCl₃ separation**: BCl₃ boils at 12.5°C, only 19.3°C below SiHCl₃ at 31.8°C. This close boiling point difference requires a distillation column with many theoretical plates (>50) and high reflux ratio (>50:1) to achieve the separation needed for electronic-grade purity. The column height for this separation alone can exceed 30 m.
- **SiHCl₃ / PCl₃ separation**: PCl₃ boils at 76°C, 44°C above SiHCl₃. Easier separation but still requires careful fractionation.
- **SiHCl₃ / SiCl₄ separation**: 25.8°C boiling point difference. Straightforward separation in a moderate-height column.


## See Also

- [Distillation](../chemistry/distillation.md) — chlorosilane fractional distillation
- [Hydrogen & Silane](../chemistry/hydrogen-silane.md) — precursor gases for CVD
- [Gas Handling Basic](../gas-handling/basic.md) — gas piping and containment
- [Crystal Growth](crystal-growth.md) — single-crystal silicon from purified feedstock
- [MG-Si Production](mg-si-production.md) — metallurgical-grade silicon upstream
- [Silicon Index](index.md) — silicon production chain overview

[← Back to Silicon](index.md)
