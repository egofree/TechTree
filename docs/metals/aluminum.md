# Aluminum Production

> **Node ID**: metals.aluminum
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`chemistry.alkalis`](../chemistry/alkalis.md), [`chemistry.electrolysis`](../chemistry/electrolysis.md), [`energy.electricity`](../energy/electricity.md), `mining`
> **Enables**: [`electrochemistry.anodizing`](../electrochemistry/anodizing.md), `metals.aluminum.semiconductor-grade`, [`metals.forming`](forming.md), [`transport.aviation`](../transport/aviation.md)
> **Timeline**: Years 20-40
> **Outputs**: aluminum ingots, extrusions, castings, sheet

### Overview

Aluminum is the most abundant metal in Earth's crust (8.1% by weight) but never occurs natively — it is always chemically bound, most commonly as aluminum silicates in clays and feldspars. The metal remained unknown until 1825 (isolated by Ørsted as an impure powder) and was more valuable than gold until the Hall-Héroult process (1886) made bulk production possible. Modern civilization depends on aluminum for electrical conductors, structural components, packaging, transportation, and as the primary structural metal for aerospace.

Aluminum production is a two-stage process: the Bayer process converts bauxite ore to pure alumina (Al₂O₃), and the Hall-Héroult process electrolytically reduces alumina to metallic aluminum. The overall energy intensity is 13-15 kWh/kg — aluminum production consumes ~3-4% of global electricity. Recycling requires only 5% of that energy, making secondary aluminum one of the most economically valuable recycled materials.

### Bayer Process — Bauxite to Alumina

The Bayer process (1887) extracts pure alumina from bauxite ore via selective dissolution in hot sodium hydroxide. Bauxite typically contains 30-55% Al₂O₃ as gibbsite (Al(OH)₃), boehmite (AlO(OH)), or diaspore (AlO(OH)), along with iron oxides (the red color), silica, and titania as impurities.

**Digestion**:
- Crushed bauxite (ground to <150 μm) is fed into a pressure vessel (digester) with concentrated NaOH solution (caustic concentration 140-250 g/L Na₂O equivalent).
- **Temperature/pressure depend on mineralogy**: Gibbsite (trihydrate) digests at 140-150°C, atmospheric or low pressure (0.3-0.5 MPa). Boehmite (monohydrate) requires 200-250°C at 2-4 MPa. Diaspore requires the harshest conditions: 250-280°C at 4-6 MPa. Most industrial bauxites contain a mix.
- **Reaction**: Al₂O₃·nH₂O + 2NaOH → 2NaAlO₂ + (n+1)H₂O. Aluminum dissolves as sodium aluminate; iron oxides, silica, and titania remain insoluble.
- **Desilication**: Reactive silica (clay minerals) co-dissolves and re-precipitates as sodium aluminosilicate (sodalite), consuming NaOH and Al₂O₃. High-silica bauxites (>5% SiO₂) have significantly lower process efficiency. Typical NaOH loss: 30-100 kg per tonne Al₂O₃ depending on silica content.
- Digestion time: 0.5-4 hours depending on mineralogy and temperature.

**Clarification**:
- The digested slurry is diluted with wash water and settled in large thickeners (40-60 m diameter). The red mud residue (iron oxides, silica, titania, undigested minerals) settles to the bottom.
- Red mud is washed in counter-current decantation (3-5 stages) to recover entrained sodium aluminate solution. Final mud is pumped to disposal areas — this is a major environmental challenge. Global red mud stockpile: >4 billion tonnes, growing at ~150 million tonnes/year. pH 10-13. Disposal methods: dry stacking (preferred — dewatered to 65-75% solids), seawater discharge (neutralized), or repurposing (cement feed, iron recovery, building material).
- Overflow (sodium aluminate liquor, "green liquor") is filtered through pressure leaf filters with diatomaceous earth pre-coat to remove fine suspended solids (<5 mg/L suspended solids required).

**Precipitation**:
- Cooled to 50-65°C and seeded with fine aluminum hydroxide crystals (hydrate seed, ~50-200 g/L seed charge). The supersaturated aluminate solution precipitates Al(OH)₃ onto the seed surfaces.
- **[Agglomeration phase](../glossary/agglomeration-phase.md)** (first 6-8 hours): Fine seed particles agglomerate into larger clusters. **[Growth phase](../glossary/growth-phase.md)** (20-40 hours): Al(OH)₃ crystallizes on agglomerate surfaces. Total precipitation time: 30-60 hours.
- Yield: ~50-55 g/L Al₂O₃ precipitated per pass (from initial ~120-150 g/L in green liquor). The remaining liquor ("spent liquor") is recycled to digestion after concentration in evaporators.
- Product size control: Coarse product (60-100 μm) for smelter-grade alumina, fine product (<40 μm) for specialty applications. Particle morphology affects downstream calcination and dissolution rates.

**Calcination**:
- Al(OH)₃ is calcined in rotary kilns or (modern preference) gas-suspension calciners / fluidized-bed calciners at 1000-1200°C.
- **Reaction sequence**: Al(OH)₃ → AlO(OH) (boehmite) → γ-Al₂O₃ → α-Al₂O₃ (corundum). The α-phase is the target — fully dehydrated, chemically stable, low surface area.
- Rotary kiln: 3-4 m diameter, 50-100 m long, 2-4 hour residence time, 3.5-4.5 GJ per tonne Al₂O₃.
- Gas-suspension calciner ( flash calciner): Higher energy efficiency (2.8-3.2 GJ/tonne), shorter residence time (<1 second in the hot zone), smaller footprint. Products fine, highly reactive alumina (higher surface area → dissolves faster in cryolite bath).
- Product specification: Smelter-grade alumina (SGA) is >99.5% Al₂O₃, typically 99.6-99.8%. Key impurities: SiO₂ (<0.015%), Fe₂O₃ (<0.015%), Na₂O (<0.4%), LOI (loss on ignition, <1.0%).

### Hall-Héroult Process — Electrolytic Reduction

The Hall-Héroult process dissolves alumina in molten cryolite (Na₃AlF₆) and electrolyzes it to produce aluminum metal and CO/CO₂ gas. Invented independently by Charles Hall (US) and Paul Héroult (France) in 1886 — the foundational process unchanged in principle for 140 years.

**Cell chemistry**:
- **Overall reaction**: 2Al₂O₃ + 3C → 4Al + 3CO₂ (simplified). In practice, both CO₂ and CO are produced; CO₂ dominates (>80% at normal operating conditions).
- **Electrolyte**: Molten cryolite (Na₃AlF₆, melting point 1009°C) with excess AlF₃ (cryolite ratio 2.0-2.5, where ratio = NaF/AlF₃ molar ratio; pure cryolite = 3.0). The AlF₃ addition lowers the liquidus temperature to 940-970°C and improves current efficiency.
- **Bath additives**: CaF₂ (4-8%, reduces liquidus), LiF (0-5%, increases conductivity, reduces temperature), MgF₂ (0-3%, reduces sodium penetration into cathode). Each addition is a trade-off between operating temperature, electrical conductivity, alumina solubility, and density (bath must be less dense than liquid aluminum — 2.1 vs. 2.3 g/cm³).
- **Operating temperature**: 960-980°C. The liquid aluminum pools beneath the electrolyte (density difference provides natural separation).
- **Alumina feed**: 2-4% Al₂O₃ dissolved in the bath. Alumina is fed in controlled batches via point feeders (1-2 kg per feed, every 1-5 minutes) to maintain concentration. Underfeeding triggers anode effect; overfeeding causes sludge formation beneath the metal pad.

**Cryolite supply — natural vs synthetic**:
- **Natural cryolite** (Na₃AlF₆, monoclinic): The only commercially significant deposit was at Ivigtut, Greenland — mined from 1854 to 1987, now essentially depleted. Natural cryolite has the advantage of lower impurity levels (particularly lower SiO₂ and Fe₂O₃) but is no longer available in industrial quantities. Historical availability of natural cryolite was a key factor in the early aluminum industry's location decisions.
- **Synthetic cryolite production**: All modern smelters use synthetically produced cryolite. The primary route: HF is reacted with Al(OH)₃ to form H₃AlF₆ (hexafluoroaluminic acid) or AlF₃, which is then combined with NaOH or Na₂CO₃ to precipitate Na₃AlF₆. A second route uses fluosilicic acid (H₂SiF₆, a byproduct of phosphate fertilizer production) reacted with aluminum hydroxide and sodium aluminate. Synthetic cryolite purity: >97% Na₃AlF₆, with controlled moisture (<0.3%) and low SiO₂ (<0.3%).
- **Bath ratio management**: The cryolite ratio (NaF/AlF₃ molar) is the single most important bath chemistry parameter. Industrial practice targets 2.2-2.4 (excess AlF₃ relative to stoichiometric cryolite at 3.0). Lower ratio → lower operating temperature but higher bath resistivity and lower alumina solubility. AlF₃ is continuously consumed by sodium uptake into the cathode lining (NaF + C → intercalation compounds), moisture ingress (AlF₃ + 3H₂O → Al₂O₃ + 6HF), and operational losses. AlF₃ addition rates: 15-25 kg per tonne Al produced. Bath chemistry is monitored by XRD or wet chemistry analysis every 1-4 hours in modern smelters.
- **LiF and CaF₂ modifiers**: LiF (0-5%) increases bath conductivity by 15-25% (reducing cell voltage and energy consumption) and lowers liquidus temperature, but is expensive ($5-15/kg) and increases lithium contamination of the metal. CaF₂ (4-8%) occurs naturally from CaO impurity in alumina (dissolves as CaF₂) and is sometimes added deliberately — it lowers liquidus and reduces sodium penetration into cathodes but increases bath density. KF is avoided — potassium intercalates aggressively into cathode carbon, causing rapid swelling and cathode failure.

**Electrolytic cell (pot) design**:
- **Anode**: Carbon, 400-600 mm above the cathode. Consumed at ~400-450 kg carbon per tonne Al. Prebaked or Söderberg (see Anode Production below).
- **Cathode**: Carbon lining of the steel shell, with steel current collector bars embedded in the bottom. The liquid aluminum layer itself acts as the effective cathode surface.
- **Anode-cathode distance (ACD)**: 30-50 mm. Critical parameter: too close → short circuits; too far → excessive voltage drop and energy waste. Modern automated cells maintain ACD within ±2 mm.
- **Shell**: Steel rectangualar box (8-15 m long, 3-5 m wide), lined with refractory bricks and carbon cathode blocks. Thermal design balances heat retention (to maintain bath temperature) with sidewall cooling (to freeze a protective ledge of cryolite/bath on the interior walls — the "freeze ledge" protects the sidewall lining from chemical attack).

**Electrical parameters**:
- **Cell voltage**: 3.8-4.5 V (theoretical minimum: 1.2 V at 960°C for the overall reaction; the excess is ohmic losses in bath, anodes, cathode, external buswork, and overvoltages).
- **Amperage**: Modern cells operate at 300-500 kA (some reach 600 kA). Higher amperage increases production per pot but requires larger anodes and more robust buswork.
- **Current efficiency**: 92-96% (the deficit is caused by re-oxidation of aluminum by CO₂ at the anode — "back reaction" — and electronic short-circuiting through the bath).
- **Energy consumption**: 13-15 kWh per kg Al (best modern cells: 12.5-13.0 kWh/kg; older technologies: 15-17 kWh/kg). Approximately 40% of energy input is heat lost to the surroundings.
- **Production per pot**: 1.8-3.5 tonnes Al per day at 300-500 kA.

**Potline configuration**:
- 200-300 pots connected in series (same current flows through all pots; voltage adds — a 300-pot potline at 4.0 V/pot requires ~1,200 V DC total).
- Power supply: Rectiformers (silicon-controlled rectifiers) converting grid AC to high-current DC. A single potline drawing 400 kA at 1,200 V consumes ~480 MW — a smelter is typically the largest electricity consumer in its region.
- Potline operation is continuous — shutting down causes the bath to freeze in the pots, destroying the cathode linings (a "freeze-up" costs millions in reconstruction). Automatic bypass switches allow individual pots to be cut out for maintenance without interrupting the series current.
- Aluminum is tapped from each pot every 24-48 hours by siphoning or vacuum crucible. A 500 kA pot produces ~3.7 tonnes per day.

### Anode Production

Carbon anodes are consumed at ~400-450 kg per tonne of aluminum produced. Anode quality directly affects metal purity, energy consumption, and emissions.

**[Prebaked anodes](../glossary/prebaked-anodes.md)** (dominant technology, ~90% of production):
- **Raw materials**: Petroleum coke (60-65% of anode mass, calcined at 1200-1300°C to remove volatiles and develop crystalline structure), coal tar pitch (13-16% as binder), recycled anode butts (20-25%, remaining carbon from consumed anodes, crushed and re-used).
- **Manufacturing process**:
  1. **Dry aggregate**: Crush, grind, and size petroleum coke to a defined particle size distribution (coarse 3-10 mm, medium 0.5-3 mm, fines <0.5 mm, ball-mill fines <75 μm). The packing density and porosity of the final anode depend critically on this blend.
  2. **Mixing**: Heat dry aggregate to 140-170°C, add molten pitch (160-180°C). Mix in heated kneaders or intensive mixers for 15-30 minutes. Pitch coats and fills voids between coke particles.
  3. **Forming**: Press or vibrate the green paste into blocks (typically 1400-1600 mm × 600-800 mm × 500-600 mm) at 40-60 MPa. Vibrating compactors are standard for prebaked anodes.
  4. **Baking**: Fire in ring furnaces or pit furnaces at 1050-1200°C for 10-20 days (slow heating rate to avoid cracking — volatiles from pitch decomposition escape gradually). The pitch carbonizes into coke, binding the aggregate into a monolithic carbon block. Baking increases density (1.55-1.65 g/cm³ baked) and electrical conductivity.
  5. **Rodding**: Attach a steel stub (conical or threaded) to the baked anode with cast iron or carbonaceous paste. The stub connects to the anode busbar.
- **Properties**: Electrical resistivity 50-60 μΩ·m, compressive strength 30-45 MPa, air permeability <2 nPm. Low sulfur coke (<3% S) is preferred to minimize SO₂ emissions and metal contamination.

**[Söderberg anodes](../glossary/sderberg-anodes.md)** (self-baking, older technology):
- A single continuous carbon anode is formed in place above the cell. Green paste (petroleum coke + pitch) is added at the top; as it descends toward the hot bath, the pitch bakes in-situ from the cell's own heat. No separate baking furnace required.
- **Advantages**: Lower capital cost, no anode change interruptions, simpler logistics.
- **Disadvantages**: Higher electrical resistivity (pot voltage 0.2-0.5 V higher → more energy per kg Al), higher emissions (PAH, tar fumes), lower current density, lower metal purity. Being phased out globally.
- Horizontal stud (HS) and vertical stud (VS) Söderberg designs exist; vertical stud is more common.

**Anode effect**:
- When alumina concentration drops below ~1.5%, the bath no longer wets the anode surface. A gas film (predominantly CO, CF₄, C₂F₆) forms under the anode, cell voltage spikes from 4V to 20-40V, and arcing occurs.
- **CF₄ emissions**: Carbon tetrafluoride has a global warming potential (GWP-100) of 6,620 — a single anode effect event can release kg of CF₄. Modern smelters target <0.1 anode effects per pot-day (some achieve <0.01) through automated feed control and rapid alumina feeding on voltage rise detection.
- **Quenching**: Feed alumina rapidly, lower the anode to break the gas film, or short-circuit the cell briefly. Automated systems handle most anode effects within 1-3 minutes.

### Aluminum Alloys

Pure aluminum (99.0-99.99%) is soft (tensile strength 40-50 MPa) and has limited structural use. Alloying with small quantities of other elements dramatically improves mechanical properties — alloyed aluminum reaches 500-600 MPa tensile strength.

**[Alloy designation system](../glossary/alloy-designation-system.md)** (AA — Aluminum Association):

| Series | Primary Alloying Element | Key Characteristics |
|--------|-------------------------|---------------------|
| 1xxx | ≥99.0% Al (no alloying) | Excellent corrosion resistance, high conductivity, low strength. Electrical applications. |
| 2xxx | Copper (2-6%) | High strength, poor corrosion resistance. Aerospace (2024). |
| 3xxx | Manganese (0.5-1.5%) | Moderate strength, excellent formability. Beverage cans, cooking utensils. |
| 4xxx | Silicon (4-13%) | Low melting point, good fluidity. Filler wire for welding, casting alloys. |
| 5xxx | Magnesium (1-5%) | Good strength, excellent corrosion resistance (marine). Shipbuilding, pressure vessels. |
| 6xxx | Mg + Si (0.5-1.5% each) | Medium strength, excellent extrudability, heat-treatable. Structural profiles (6061, 6063). |
| 7xxx | Zinc (3-8%) + Mg + Cu | Highest strength, stress corrosion susceptible. Aerospace (7075). |
| 8xxx | Other (Li, Sn, etc.) | Specialty. Al-Li alloys for aerospace weight reduction. |

**[Heat treatment tempers](../glossary/heat-treatment-tempers.md)** (for heat-treatable alloys — 2xxx, 6xxx, 7xxx):
- **T4**: Solution heat-treated, naturally aged. Solution treatment at 480-540°C (dissolve alloying elements into solid solution), quench in water, age at room temperature. Moderate strength, high formability.
- **T6**: Solution heat-treated and artificially aged. After quenching, age at 120-180°C for 4-24 hours. Peak hardness — the standard structural temper. 6061-T6: 310 MPa yield, 7075-T6: 503 MPa yield.
- **T7**: Solution heat-treated and over-aged. Age beyond peak hardness to improve corrosion resistance and dimensional stability at some strength sacrifice. Used for critical aerospace forgings.

**Key engineering alloys**:
- **6061-T6**: The workhorse structural alloy. 1.0% Mg, 0.6% Si, 0.25% Cu, 0.2% Cr. Good strength (310 MPa UTS), excellent corrosion resistance, weldable, machinable, affordable. Used for frames, brackets, structural profiles.
- **7075-T6**: High-strength aerospace alloy. 5.6% Zn, 2.5% Mg, 1.6% Cu. UTS 572 MPa — comparable to many steels at 1/3 the density. Difficult to weld (use 7xxx filler or friction stir welding). Used for aircraft frames, gears, high-stress components.
- **356-T6**: Casting alloy (Al-7% Si-0.3% Mg). Excellent castability (silicon provides fluidity), heat-treatable to 228 MPa UTS. Used for engine blocks, cylinder heads, complex cast shapes.
- **3003-H14**: Non-heat-treatable, work-hardened. 1.2% Mn. Good formability, moderate strength (130 MPa UTS). Used for sheet metal work, chemical equipment, signage.

**Alloy composition table** (wt%, balance Al):

| Element | 1100 | 3003 | 6061 | 7075 |
|---------|------|------|------|------|
| Si | ≤0.95 (Si+Fe) | ≤0.6 | 0.40-0.80 | ≤0.40 |
| Fe | (included above) | ≤0.7 | ≤0.70 | ≤0.50 |
| Cu | 0.05-0.20 | 0.05-0.20 | 0.15-0.40 | 1.2-2.0 |
| Mn | ≤0.05 | 1.0-1.5 | ≤0.15 | ≤0.30 |
| Mg | — | — | 0.80-1.20 | 2.1-2.9 |
| Cr | — | — | 0.04-0.35 | 0.18-0.28 |
| Zn | ≤0.10 | ≤0.10 | ≤0.25 | 5.1-6.1 |
| Ti | — | — | ≤0.15 | ≤0.20 |
| Al (min) | 99.00% | Balance | Balance | Balance |

**Mechanical properties table**:

| Property | 1100-O | 1100-H14 | 3003-H14 | 6061-T6 | 7075-T6 |
|----------|--------|----------|----------|---------|---------|
| Yield Strength (MPa) | 35 | 110 | 145 | 276 | 503 |
| UTS (MPa) | 90 | 130 | 200 | 310 | 572 |
| Elongation (%) | 35 | 9 | 8 | 12 | 11 |
| Hardness (Brinell) | 23 | 32 | 45 | 95 | 150 |
| Density (g/cm³) | 2.71 | 2.71 | 2.73 | 2.70 | 2.81 |
| Thermal Conductivity (W/m·K) | 222 | 218 | 163 | 167 | 130 |
| Electrical Conductivity (% IACS) | 59 | 57 | 41 | 43 | 33 |

**Aluminum for semiconductor equipment frames**:
- **6061-T6 for vacuum chambers**: The most common alloy for vacuum chamber construction. Low outgassing rate after bake-out (<10⁻⁹ Torr·L/s·cm² at 150°C), good machinability to achieve O-ring sealing surfaces (Ra <0.8 μm), weldable for complex chamber geometries. Typical chamber wall thickness: 10-25 mm for structural rigidity. Anodized surface (20-50 μm hard coat) provides wear resistance for sealing surfaces. Used for: sputter deposition chambers, evaporator bell jars, load-lock chambers, and plasma etch chambers.
- **6061-T6 for optical tables**: Extruded 6061-T6 profiles form the internal honeycomb structure of vibration-isolation optical tables. Low density (2.70 g/cm³) reduces table mass while maintaining stiffness (E = 68.9 GPa). Surface plates are typically stainless steel or aluminum tooling plate (cast Al with precision-machined flat surface, ±0.05 mm flatness over 1 m²). Magnetic permeability near zero — essential near electron optics and charged-particle beams.
- **7075-T6 for high-stress structural components**: Used for wafer transport robot arms (high stiffness-to-weight ratio enables rapid wafer handling with minimal vibration), lithography stage structural members, and precision equipment mounts. Elastic modulus 71.7 GPa, fatigue endurance limit 159 MPa (R=-1, 5×10⁸ cycles). Not suitable for vacuum chamber walls — higher Zn content increases outgassing and makes welding unreliable.
- **1100-O for chemical equipment**: ≥99.0% purity provides excellent corrosion resistance to many chemicals (not alkalis — Al dissolves in NaOH). Used for acid handling tanks, heat exchanger tubing in wet processing stations, and chemical distribution piping. Low strength limits use to non-structural applications. Easily formed — deep drawn into tanks and vessels.

### Semiconductor-Grade Aluminum

Ultra-high-purity aluminum (≥99.999%, "5N") is essential for semiconductor metallization — the conductive interconnect layers on integrated circuits. The purity requirements far exceed those of structural aluminum and demand dedicated refining processes.

**Purity levels and applications**:

| Grade | Purity | Nines | Primary Application |
|-------|--------|-------|---------------------|
| 3N | 99.9% | 3 | Not suitable for semiconductor use — impurity levels too high |
| 3N5 | 99.95% | 3.5 | Capacitor foil (electrolytic capacitors) |
| 4N | 99.99% | 4 | Sputtering targets for display panel metallization |
| 4N5 | 99.995% | 4.5 | General-purpose semiconductor metallization |
| 5N | 99.999% | 5 | IC interconnect metallization, bonding wire |
| 6N | 99.9999% | 6 | Advanced node interconnects, gate electrodes |

**Critical impurity limits for 5N aluminum** (maximum ppm by weight): Fe <3, Si <3, Cu <2, Zn <1, Mg <1, Ti <1, Mn <1, Cr <1, Ni <1, Ga <1, total metallic impurities <10 ppm. Uranium and thorium content must be <1 ppb each — alpha particles from U/Th decay cause soft errors in DRAM and logic devices.

**Purification methods**:
- **Three-layer electrolysis (Hoopes process)**: The primary industrial method for producing 4N-5N aluminum. A molten salt cell with three liquid layers: bottom anode layer (impure Al + Cu, density ~3.0 g/cm³), middle electrolyte (BaCl₂-NaF-AlF₃ molten salt, density ~2.7 g/cm³), top cathode layer (pure Al, density ~2.3 g/cm³). Current passes from the impure anode through the electrolyte to the cathode. Only aluminum dissolves at the anode and deposits at the cathode — impurities (Fe, Si, Cu) remain in the anode layer. Operating temperature: 720-780°C. Energy consumption: 14-18 kWh/kg for 4N5 purity. A single pass produces 99.995% from 99.7% primary aluminum.
- **Zone refining**: A traveling molten zone passes along an aluminum bar, sweeping impurities toward one end by fractional crystallization (partition coefficient k < 1 for most impurities in Al). Multiple passes (10-30) progressively concentrate impurities at the bar ends. Used to upgrade 4N5 aluminum to 5N-6N purity. Very slow (1-10 mm/min zone travel speed) and low throughput — a bar is typically 30-50 mm diameter × 500-1000 mm long. Segregation coefficients: Fe (k=0.03), Si (k=0.13), Cu (k=0.15) — these are highly effectively removed. Cr (k=0.9) and Mn (k=0.9) are poorly removed by zone refining and must be controlled at earlier stages.
- **Directional solidification**: Similar principle to zone refining but the entire bar is solidified directionally from one end. Less effective per pass but higher throughput. Often used as a pre-purification step before zone refining.

**Contamination control**:
- All melting and handling of high-purity aluminum must avoid contact with refractory materials (Al₂O₃, SiO₂) that can dissolve and re-contaminate. Graphite or BN-coated graphite crucibles are used.
- Atmosphere control: Melting under high-purity argon or vacuum to prevent oxidation and gas pickup. Dissolved hydrogen causes porosity in sputtering targets.
- Sputtering target production: 5N aluminum is cast into cylindrical targets (200-400 mm diameter × 6-12 mm thickness for semiconductor tools, up to 3000 mm × 250 mm for display tools), then machined to ±0.05 mm flatness and bonded to copper backing plates using indium or epoxy thermal interface material. Target grain size <100 μm ensures uniform sputtering rate. Typical target life: 500-2000 kWh of sputtering power before replacement.
- **Metallization applications**: Physical vapor deposition (PVD sputtering) of 5N Al produces 0.3-2.0 μm thick interconnect layers. Al-Si (1% Si) and Al-Cu (0.5% Cu) alloy targets suppress electromigration and spiking. The Al layer is patterned by photolithography and plasma etching (Cl₂/BCl₃ chemistry) to form interconnect lines. Al metallization is being replaced by Cu (Damascene process) at nodes below 130 nm but remains in use for upper metal layers, bond pads, and power distribution.

### Aluminum Casting

**Melting and melt treatment**:
- Primary melting in reverberatory furnaces (natural gas or oil fired, 30-100 tonne capacity) or induction furnaces (cleaner, more precise temperature control, smaller capacity). Melt temperature: 700-750°C.
- **Fluxing**: Add chloride-based fluxes (NaCl-KCl eutectic + fluorides) to absorb oxides and non-metallic inclusions from the melt. Flux floats as a separate liquid phase on the metal surface and is skimmed off.
- **Degassing**: Dissolved hydrogen (from moisture reacting with molten Al: 2Al + 3H₂O → Al₂O₃ + 3H₂) causes porosity in castings. Remove by bubbling inert gas (Ar, N₂) or chlorine (1-5% in N₂) through the melt. Rotary degassing (spinning impeller) is most effective — creates fine bubbles with maximum gas-metal contact. Target: <0.1 mL H₂/100g Al.
- **Grain refinement**: Add Al-Ti-B master alloy (typically Al-5%Ti-1%B in rod form) to the melt. TiB₂ particles nucleate fine equiaxed grains during solidification. Grain size: 100-300 μm with refinement vs. 1-5 mm without. Fine grain improves mechanical properties, reduces hot tearing, and improves feeding during solidification.

**Casting processes**:

**Sand casting**: Green sand (silica sand + clay + water) or chemically bonded sand (furanyl, phenolic urethane) molds. Largest castings possible (up to several tonnes). Surface finish rough (Ra 12-25 μm). Minimum wall thickness ~3 mm. Low tooling cost — suitable for prototyping and low-volume production. Risers and gating designed to feed shrinkage during solidification.

**Permanent mold (gravity die) casting**: Reusable metal molds (cast iron or steel) with coatings (silica-based wash) to prevent sticking. Better surface finish and dimensional accuracy than sand casting. Wall thickness to ~3 mm. Mold life: 5,000-50,000 parts depending on complexity. Higher tooling cost amortized over larger volumes. Used for cylinder heads, pistons, manifolds.

**[Die casting](../glossary/die-casting.md)** (high-pressure):
- Molten aluminum forced into steel die at 20-100 MPa. Two types: **[hot chamber](../glossary/hot-chamber.md)** (limited to lower-melting alloys, rarely used for aluminum due to attack on gooseneck components) and **[cold chamber](../glossary/cold-chamber.md)** (molten Al ladled into shot sleeve, then injected — standard for aluminum).
- Very high production rates (100-1,000 shots/hour). Excellent surface finish (Ra 0.8-3.2 μm). Wall thickness to 0.8 mm. Tolerances ±0.1-0.3 mm.
- Die life: 50,000-200,000 shots depending on alloy and die complexity. Dies made from H13 tool steel, heat-treated to 44-48 HRC.
- Alloys: Typically 380 (Al-8.5%Si-3.5%Cu), 383, A384, 413 (Al-12%Si). High silicon for fluidity.
- Limitations: High porosity from entrapped air (reduced by vacuum-assisted die casting). Retained compressive stress in surface but internal porosity limits fatigue life. Not heat-treatable (bloating of internal porosity). Structural die casting (high-integrity) uses squeeze casting or semi-solid molding to address this.

**[Direct chill (DC) casting](../glossary/direct-chill-dc-casting.md)** (for wrought products — ingots for rolling/extrusion):
- Semi-continuous vertical casting. Molten Al flows into a water-cooled mold with a moving bottom block. As metal solidifies, the bottom block descends.
- Produces rectangular ingots (for rolling to sheet/plate) or cylindrical billets (for extrusion). Ingot size: up to 9 m long, 0.5 × 1.5 m cross-section. Billet diameter: 150-800 mm.
- Water spray directly onto the solidifying shell provides intense cooling (solidification rate 10-100 mm/min). Fine dendrite arm spacing → homogeneous microstructure.
- Critical issues: Shell tearing, center cracks, bleed-out. Controlled by mold design, water flow rate, casting speed, and metal level control.

### Aluminum Extrusion

Extrusion forces a heated aluminum billet through a steel die to produce profiles of constant cross-section — the most efficient way to make complex shapes from aluminum.

**Process**:
- **Billet preparation**: DC-cast cylindrical billet, 150-300 mm diameter, 400-1000 mm long. Homogenized at 540-580°C for 2-8 hours to dissolve intermetallic phases and eliminate segregation. Scalped (surface machined) to remove inverse segregation layer.
- **Preheating**: 450-500°C (for 6xxx alloys — below solution treatment temperature so that deformation heating brings the alloy into the solution treatment range during extrusion). Gas-fired or induction log heaters, ±5°C uniformity.
- **Extrusion**: Heated billet loaded into a container (slightly smaller diameter than billet → upsets billet to fill container). Hydraulic ram pushes billet through die at 10-40 MPa ram pressure. Metal flows through die orifice, emerging as a continuous profile.
- **Speed**: 1-50 m/min depending on alloy and profile complexity. 6xxx alloys extrude at 5-30 m/min; 7xxx and 2xxx are much slower (0.5-5 m/min) and harder to extrude.
- **Direct vs indirect extrusion**: Direct (forward) — die is stationary, billet moves relative to container. Higher friction (~30% of force overcomes billet-container friction). Indirect (backward) — die moves with the ram inside the hollow container; billet is stationary. No billet-container friction → 25-30% lower extrusion force, more uniform flow. Indirect requires a hollow ram (limits die size) and more complex tooling.

**Die design**:
- Flat dies (solid profiles): Single-piece tool steel die (H13, heat-treated to 48-52 HRC) with the profile aperture machined by wire EDM. Bearing length (the parallel land that the metal flows through) controls flow velocity — longer bearings provide more resistance.
- Porthole/bridge dies (hollow profiles): Mandrel forming the interior cavity is supported by legs bridging across the die. Metal flows around the legs and welds together under pressure in the welding chamber before exiting the die aperture. Weld quality depends on extrusion pressure, temperature, and die design.
- Profile size: Up to ~500 mm circumscribing circle diameter on large presses. Press capacity: 1,000-12,000 tonnes (largest presses: 14,000+ tonnes). Wall thickness down to 0.8 mm.

**Post-extrusion processing**:
- **Quenching**: Profile is air-blasted or water-sprayed immediately after exiting the die to cool rapidly from the solution treatment temperature. For 6xxx alloys, this retains Si and Mg in solid solution for subsequent aging.
- **Stretching**: Profile is gripped at both ends and stretched 0.5-3% to straighten and relieve residual stresses.
- **Artificial aging**: Heat to 160-200°C for 4-12 hours (T5 temper — press-quenched + aged). For higher properties, full T6 treatment (separate solution treat + quench + age) is used.

### Aluminum Recycling

Recycling is integral to the aluminum industry — not an afterthought. The energy savings are enormous: remelting requires only 5% of the energy of primary production (~0.6-0.8 kWh/kg vs. 13-15 kWh/kg). Approximately 75% of all aluminum ever produced (over 1 billion tonnes cumulative) is still in productive use.

**Scrap categories**:
- **New (pre-consumer) scrap**: Offcuts, trimmings, defective products from manufacturing. Known composition, low contamination — directly remelted. ~40% of recycled aluminum.
- **Old (post-consumer) scrap**: Used beverage cans, window frames, automotive parts, packaging. Variable composition, contaminated with coatings, lacquers, other metals — requires sorting and cleaning. ~60% of recycled aluminum.
- **Wrought vs cast**: Critical distinction — wrought alloys (1xxx-7xxx) diluted with alloying elements; cast alloys (3xx, 4xx) contain high Si and other elements that limit recycling into wrought products. Cross-contamination of wrought scrap with cast scrap degrades quality.

**Scrap processing**:
- **Sorting**: Hand-sorting (basic), sink-float separation (density-based in heavy media), X-ray transmission (XRT — sorts by atomic density), laser-induced breakdown spectroscopy (LIBS — identifies alloy composition in real-time at >10 pieces/second). Sorting wrought from cast and separating by alloy series is the key technical challenge.
- **Decoating**: Paint, lacquer, and organic coatings are removed by thermal delacquering (rotary kiln at 400-500°C — pyrolysis of organics) or by centrifugation/crushing. Organics contribute ~5-10 MJ/kg of heating value during thermal decoating — partially offsetting process energy.
- **Shredding**: Large scrap (cars, appliances) is shredded to 20-50 mm pieces for sorting and melting efficiency.

**Melting**:
- **[Side-well reverberatory furnace](../glossary/side-well-reverberatory-furnace.md)** (most common for scrap): Main bath chamber connected to an open well by an underflow passage. Scrap is fed into the side well and pushed under the molten metal surface (submerged charging — minimizes oxidation and dross formation). Main chamber provides settling time for inclusions and temperature control. Capacity: 20-80 tonnes.
- **Rotary furnace**: Tilting rotary drum with refractory lining. Salt flux (NaCl-KCl + cryolite) covers the melt, protecting aluminum from oxidation and absorbing oxides. Salt slag is a byproduct requiring disposal. Good for light, oxidized scrap (turnings, foil).
- **Induction furnace**: Coreless induction for clean scrap — electromagnetic stirring homogenizes melt. No combustion gases → minimal oxidation, low gas pickup. More expensive per tonne for large volumes.

**Dross processing**: Dross (skimmed from the melt surface — a mixture of Al metal, Al₂O₃, salt, and impurities) contains 30-70% metallic aluminum. Processed in rotary salt furnaces or plasma arc furnaces to recover metal. Residual oxide residue (NMP — non-metallic product) goes to landfill or is reprocessed for alumina recovery.

**Recycling rates**: Beverage cans: ~70% globally (Brazil >95%, US ~45%). Automotive aluminum: ~90%. Building and construction: ~95%. The closed-loop can-to-can recycling cycle takes as little as 60 days.

### Safety & Hazards

**Hall-Héroult cell hazards**:
- Molten cryolite bath at 960-980°C causes severe burns on skin contact. Molten aluminum at ~960°C — any moisture contacting the bath or metal causes violent steam explosions. All tools and materials must be thoroughly preheated and dry before contacting the melt.
- Magnetic fields around potlines at 300-500 kA are extreme — ferromagnetic tools can be pulled from workers' hands. Cardiac pacemaker wearers must maintain distance from busbars and pots. Steel structures near potlines experience induced currents and forces.
- HF (hydrogen fluoride) and SO₂ emissions from bath. Potroom fluoride emissions historically caused skeletal fluorosis in workers. Modern gas collection (hooded pots) and dry scrubbing (alumina absorbs HF — the "reacted alumina" is then fed to the pots, recycling captured fluoride) reduce emissions to <0.5 kg F per tonne Al. Potroom workers require respiratory protection during specific operations.

**Anode baking furnace**:
- Coal tar pitch contains polycyclic aromatic hydrocarbons (PAHs), including benzo[a]pyrene — a known carcinogen. Fume extraction and PPE (respirators, gloves) are mandatory during green anode production and baking operations. Pitch burns at ~250°C on contact with hot surfaces.

**Molten aluminum handling**:
- Aluminum melt at 700-750°C (casting temperature) — standard foundry hazards. Moisture in molds, tools, or charge materials causes explosive spattering. Preheat all tools to 150°C+ before immersion. Wear face shield, aluminized apron, leather gloves, and safety glasses.
- Dross handling: Hot dross can contain unreacted aluminum and generates fine particulate. Handle in ventilated areas. Dross fires (aluminum burning) are difficult to extinguish — smother with dry sand or Class D extinguisher. Do NOT use water.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Metals](./index.md) • [All Domains](../index.md)*
