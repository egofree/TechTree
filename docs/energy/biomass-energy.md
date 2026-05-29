# Biomass Energy

> **Node ID**: energy.biomass-energy
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.fuels.charcoal`](charcoal.md), [`chemistry.fermentation`](../chemistry/fermentation.md), [`energy.engine`](engine.md)
> **Enables**: [`energy.electricity`](electricity.md), [`energy.steam-power`](steam-power.md)
> **Timeline**: Years 0-30
> **Outputs**: biogas, producer_gas, biofuel, biomass_heat, biomass_electricity
> **Critical**: No — biomass supplements other energy sources and provides fuel security when petroleum and coal are unavailable


Biomass energy converts organic material — wood, agricultural residues, animal manure, food waste, and purpose-grown energy crops — into useful heat, combustible gas, or liquid fuels. It is the oldest energy source (fire) and remains relevant at every stage of industrial development: from simple wood fires for heating, through biogas digesters for gas production, to biomass gasification powering internal combustion engines for electricity generation.

In the bootstrap context, biomass energy fills a critical gap: it is the only renewable energy source that can be stored indefinitely (as solid fuel) and dispatched on demand. Unlike wind or solar, biomass produces energy when needed, not when the weather permits. A wood gasifier connected to an engine-generator delivers 10-500 kW of electricity 24 hours per day, consuming locally available fuel that requires no mining, no drilling, and no imported technology.

Three primary conversion pathways are covered here: direct combustion for heat, anaerobic digestion for biogas, and thermochemical gasification for producer gas. Each has distinct feedstock requirements, outputs, and scale characteristics. Liquid biofuel production (ethanol, biodiesel) is mentioned but detailed in [Chemistry](../chemistry/index.md) since the primary processes are chemical rather than energy-focused.

## Prerequisites

## Materials

- **Biomass feedstock** — Wood chips, agricultural residues (straw, husks, stalks), animal manure, food waste, energy crops (miscanthus, switchgrass). See [Plants](../plants/structural-plants.md).
- **Steel plate and pipe** — For gasifier construction, digester tanks, and piping. See [Iron & Steel](../metals/iron-steel.md).
- **Refractory lining** — Firebrick or castable refractory for gasifier combustion zones. See [Ceramics](../ceramics/kilns.md).
- **Sealing materials** — Clay, tar, or rubber gaskets for digester gas-tightness.
- **Water** — For digester slurry mixing and gas scrubbing. See [Water](../water/basic-treatment.md).

## Tools and Equipment

- **Welding equipment** — For gasifier and digester construction. See [Joining](../machine-tools/joining.md).
- **Engine-generator set** — For converting gas to electricity. See [Heat Engines](engine.md) and [Electricity](electricity.md).
- **Gas storage** — Gasometer (floating bell gas holder) or pressurized tank for biogas storage.
- **Pumps** — For circulating digester slurry and feeding gasifiers.

## Knowledge

- Anaerobic digestion biology (methanogenic archaea, temperature ranges, C:N ratio)
- Gasification chemistry (partial combustion, reduction zone, tar cracking)
- Engine modification for gaseous fuel (carburetor replacement, air-fuel ratio control)

## Bill of Materials

## Small Biogas Digester (6 m³, family-scale)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Brick or concrete (walls) | 2,000-3,000 bricks or 3 m³ concrete | [Ceramics](../ceramics/kilns.md) | Ferrocement (thinner walls, less material) |
| Steel plate (3 mm, gas holder dome) | 15-25 kg | [Iron & Steel](../metals/iron-steel.md) | Flexible membrane (PVC/HDPE, limited lifespan) |
| PVC pipe (110 mm, inlet/outlet) | 6-10 m | [Polymers](../polymers/index.md) | Clay pipe (more leakage risk) |
| Gas pipe (25 mm galvanized steel) | 5-10 m | [Iron & Steel](../metals/iron-steel.md) | PVC pipe (lower pressure rating) |
| Valve (brass or steel, 25 mm) | 2-3 pcs | [Metals](../metals/index.md) | Plug valve from wood and clay |
| Cement and sand (mortar) | 500 kg cement, 1,500 kg sand | [Chemistry](../chemistry/index.md) | Clay mortar (higher leakage) |

## Downdraft Gasifier (10-50 kW, wood-chip fueled)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Steel plate (6-10 mm, gasifier body) | 150-300 kg | [Iron & Steel](../metals/iron-steel.md) | Used propane tank (limited size) |
| Firebrick (230 × 115 × 65 mm) | 30-60 pcs | [Ceramics](../ceramics/kilns.md) | Castable refractory (easier to form complex shapes) |
| Steel pipe (50 mm, air nozzles) | 3-5 m | [Iron & Steel](../metals/iron-steel.md) | Stainless steel (longer life in oxidation zone) |
| Steel grate (15 mm bar, 20 mm spacing) | 1 unit | [Iron & Steel](../metals/iron-steel.md) | Cast iron grate |
| Cyclone separator (sheet steel) | 1 unit | [Iron & Steel](../metals/iron-steel.md) | Fabric filter (higher pressure drop) |
| Sawdust filter drum (200 liter) | 1 unit | [Forestry](../plants/index.md) | Cloth bag filter |
| Gas cooling pipe (finned, 50 mm) | 3-5 m | [Iron & Steel](../metals/iron-steel.md) | Steel pipe in water bath |

## Process Description

## 4.1 Anaerobic Digestion (Biogas Production)

1. **Build the digester**: Construct a cylindrical or rectangular underground tank (6-10 m³ volume for family scale, 50-500 m³ for village scale). Inlet pipe near the bottom for fresh feed, outlet pipe at the opposite end for spent slurry. Gas collection dome at the top — either a fixed dome (gas pressure varies) or a floating bell (gas holder rises as gas accumulates, maintains constant low pressure).

2. **Prepare the feedstock**: Mix animal manure (cattle, pig, poultry) with water to form a slurry of 8-12% total solids. Add crop residues (chopped to <50 mm) at 10-20% of total feed by weight. Maintain carbon-to-nitrogen (C:N) ratio of 20-30:1. Pure manure: C:N ~15-20 (too nitrogen-rich, add carbonaceous material like straw). Pure straw: C:N ~70-100 (too carbon-rich, add manure or urea).

3. **Inoculate**: Seed the digester with active digesting slurry from an existing digester, or with cow dung (naturally contains methanogenic bacteria). Fill the digester 80-90% full with slurry.

4. **Maintain temperature**: Mesophilic digestion: 30-40°C (most common). Thermophilic digestion: 50-60°C (faster, higher gas yield, but harder to maintain). In temperate climates, insulate the digester and/or compost around it to maintain temperature. In cold climates, solar water heating or engine waste heat can warm the digester.

5. **Feed daily**: Add fresh slurry daily (2-5% of digester volume per day). Hydraulic retention time: 20-40 days (mesophilic). Each m³ of digester volume produces 0.3-0.6 m³ biogas per day at steady state.

6. **Collect and use the biogas**: Biogas (~60% CH₄, ~35-40% CO₂, trace H₂S) rises to the gas holder. Calorific value: 21-24 MJ/m³ (60% of natural gas). Pipe to burners for cooking, lamps, or an engine-generator. Remove H₂S with iron oxide chips (iron sponge) in a filter before the engine — H₂S corrodes engine parts and produces sulfuric acid in crankcase oil.

 7. **Utilize the digestate**: The spent slurry exiting the digester is a nitrogen-rich organic fertilizer (higher plant-available nitrogen than raw manure, since anaerobic digestion mineralizes organic nitrogen). Apply to fields or compost further.

**Materials**:
- [Brick or concrete](../ceramics/index.md) (2,000-3,000 bricks or 3 m³ concrete for 6 m³ digester walls)
- [Steel plate](../metals/iron-steel.md) (3 mm thick, 15-25 kg for gas holder dome)
- [PVC pipe](../polymers/index.md) (110 mm OD, 6-10 m for inlet/outlet)
- [Galvanized steel pipe](../metals/iron-steel.md) (25 mm, 5-10 m for gas delivery)
- [Cement and sand](../chemistry/index.md) (500 kg cement + 1,500 kg sand for mortar)
- [Iron oxide chips](../chemistry/index.md) (5-10 kg for H₂S filter, replaced monthly)

**Calibration / Verification**:
1. Check digester temperature daily with a thermometer inserted 30 cm into the slurry (target: 30-40°C for mesophilic, 50-60°C for thermophilic).
2. Measure pH of digester slurry weekly (target: 6.8-7.5). pH below 6.5 indicates acid accumulation — stop feeding and add lime.
3. Test biogas composition with a portable analyzer or flame test: stable blue flame indicates >50% methane. Below 45% methane — check temperature, C:N ratio, and retention time.
4. Monitor daily gas production volume with a gas meter or by measuring gas holder displacement (target: 0.3-0.6 m³ biogas per m³ digester volume per day).
5. Measure hydraulic retention time: add a tracer dye to the inlet, measure time until it appears at outlet (target: 20-40 days for mesophilic).

**Expected Performance**:
- Biogas yield: 0.3-0.6 m³ per m³ digester volume per day at steady state
- Methane content: 55-70% of biogas by volume
- Calorific value of biogas: 21-24 MJ/m³
- Daily gas production per cattle: 0.5-1.0 m³ biogas per 500 kg animal
- Hydraulic retention time: 20-40 days (mesophilic), 10-20 days (thermophilic)

**Strengths**:
- Converts waste (manure, food scraps) into useful energy and fertilizer simultaneously
- Continuous process — daily feeding produces steady gas output, no batch downtime
- Simple construction with low-tech materials (brick, concrete, steel plate)
- Digestate has higher plant-available nitrogen than raw manure due to mineralization

**Weaknesses**:
- Requires consistent daily feeding — interrupted feeding causes process instability
- Temperature-sensitive — below 20°C, methanogenic bacteria become inactive
- Biogas has low energy density (21-24 MJ/m³) compared to natural gas (36-40 MJ/m³)
- Slow process — 20-40 day retention time means slow response to increased demand

## 4.2 Biomass Gasification (Producer Gas)

1. **Construct the gasifier**: Build a downdraft (Imbert-type) gasifier — a vertical cylindrical reactor with a throated combustion zone. The throat (constriction) forces all gas through the hottest zone, cracking tars. Diameter: 300-600 mm for 10-50 kW engines. Height: 1.0-1.5 m. Air enters through tuyeres (nozzles) at the throat.

2. **Load fuel**: Fill the hopper with dry wood chips (20-80 mm size, moisture <20%) or charcoal (10-40 mm). Charcoal gasification produces cleaner gas with negligible tars; wood gasification produces more gas but requires extensive tar cracking and filtering.

3. **Ignite**: Place kindling in the combustion zone, light through the ignition port. Once the fuel bed is burning, close the port and start the induced-draft blower (or engine suction). The gasifier reaches stable operation in 10-20 minutes.

4. **Gas production zones** (top to bottom):
   - **Drying zone** (50-150°C): Moisture evaporates from fuel.
   - **Pyrolysis zone** (200-600°C): Volatile matter released (tars, light hydrocarbons).
   - **Combustion zone** (800-1,200°C): Partial combustion of volatiles and char with limited air. Reactions: C + O₂ → CO₂ (exothermic), provides heat for endothermic reactions.
   - **Reduction zone** (700-1,000°C): Hot gases pass through char bed. Key reactions: CO₂ + C → 2CO (endothermic), H₂O + C → CO + H₂ (endothermic, water-gas reaction).

5. **Clean and cool the gas**: Raw gas exits at 400-600°C containing ash, soot, tars, and water vapor. Clean with: (a) cyclone separator (removes >90% of particles >10 μm), (b) cooling tube (reduce to <30°C — cooler gas is denser, improves engine volumetric efficiency), (c) sawdust or fabric filter (final particulate removal to <50 mg/m³).

 6. **Feed to engine**: Connect the cleaned, cooled gas to the engine intake via a gas-air mixer. Adjust air-to-gas ratio (stoichiometric: ~1.0:1.2 for producer gas, compared to ~1.0:6.5 for gasoline). Engine power output on producer gas: 40-60% of gasoline rating due to lower energy density and slower combustion.

**Materials**:
- [Steel plate](../metals/iron-steel.md) (6-10 mm thick, 150-300 kg for gasifier body)
- [Firebrick](../ceramics/index.md) (230 × 115 × 65 mm, 30-60 pieces, rated to 1,200°C)
- [Steel pipe](../metals/iron-steel.md) (50 mm OD, 3-5 m for air nozzles and gas outlet)
- [Steel grate bars](../metals/iron-steel.md) (15 mm square, 20 mm spacing)
- [Cyclone separator](../metals/iron-steel.md) (sheet steel, 1.5-3 mm thick, 200-400 mm diameter)
- [Sawdust filter](../plants/index.md) (200 liter drum filled with dry sawdust, 100-200 mm bed depth)

**Calibration / Verification**:
1. After lighting and reaching steady operation (10-20 minutes), measure gas temperature at the gasifier outlet (target: 400-600°C raw, <30°C after cooling).
2. Test gas quality by connecting to a test flare: producer gas should burn with a stable blue-yellow flame. Sooty orange flame indicates excessive tars — improve throat design or add secondary air.
3. Measure tar content by passing a known volume of gas through a filter and weighing the deposit (target: <50 mg/m³ for engine use, >100 mg/m³ fouls engine within hours).
4. Verify gas composition with an Orsat analyzer or gas chromatograph (target: 18-25% CO, 12-20% H₂, 2-4% CH₄).
5. Measure cold gas efficiency: energy in product gas / energy in fuel input (target: 65-75% for wood chips).

**Expected Performance**:
- Gas heating value: 4.5-6.0 MJ/m³ (wood chips), 4.0-5.5 MJ/m³ (charcoal)
- Cold gas efficiency: 65-75% (wood), 70-80% (charcoal)
- Fuel consumption: 1.0-1.5 kg wood chips per kWh electrical output
- Tar content after cleaning: <50 mg/m³ for engine operation
- Engine power derating: 40-60% of gasoline rating on producer gas
- Gasifier throughput: 15-50 kg fuel per hour for 10-50 kW systems

**Strengths**:
- Converts solid biomass (wood chips, agricultural residues) into combustible gas for engines
- Works with locally available fuels — no petroleum or coal required
- Charcoal gasification produces very clean gas (<50 mg/m³ tar)
- Can power existing internal combustion engines with intake modification

**Weaknesses**:
- Wood gasification produces high tar loads (500-5,000 mg/m³) requiring extensive cleaning
- Engine power derated to 40-60% of gasoline rating due to low gas energy density
- Requires consistent fuel moisture (<20%) — wet fuel causes tar spikes and unstable operation
- Gas cannot be stored at pressure — must be consumed immediately or flared

## 4.3 Direct Combustion for Heat

1. **Prepare fuel**: Air-dry biomass to <20% moisture content. Green wood (>50% moisture) wastes 30-50% of combustion energy evaporating water. Chip or cut to uniform size for consistent feeding.

2. **Combust in furnace or boiler**: Grate-fired furnace for chunky biomass (wood pieces, briquettes). Fluidized bed combustor for fine material (sawdust, rice husks) — air blown upward through a sand bed suspends and burns fine particles uniformly.

 3. **Recover heat**: Boiler tubes in the combustion chamber generate steam. Flue gas exits at 150-250°C (below this, condensation causes corrosion). Overall combustion efficiency: 60-75% for well-designed grate furnaces, 80-90% for fluidized bed combustors.

**Materials**:
- [Seasoned firewood](../plants/index.md) (moisture <20%, 14-16 MJ/kg, hardwood preferred)
- [Steel boiler tubes](../metals/iron-steel.md) (50-80 mm OD, 3-5 mm wall, seamless, 50-200 m total length)
- [Refractory lining](../ceramics/index.md) (firebrick, 230 × 115 × 65 mm, rated to 1,400°C)
- [Steel grate bars](../metals/iron-steel.md) (25 mm square, 30 mm spacing for wood pieces)
- [Insulation](../chemistry/index.md) (mineral wool, 100 mm thick, 500 kg/m³ density around boiler shell)
- [Flue damper and chimney](../metals/iron-steel.md) (steel plate, 3 mm thick, chimney height 5-15 m for natural draft)

**Calibration / Verification**:
1. Measure flue gas temperature with a thermocouple in the exhaust stack (target: 150-250°C). Below 150°C risks acid condensation; above 300°C wastes heat.
2. Measure flue gas oxygen content with a zirconia sensor or Orsat analyzer (target: 4-8% O₂ indicates optimal excess air). Below 2% O₂ = incomplete combustion (CO production). Above 12% O₂ = too much excess air (heat wasted up chimney).
3. Measure steam pressure and temperature at boiler outlet — compare to design specification (target: 2-10 bar, 120-180°C for low-pressure heating boilers).
4. Weigh a known quantity of fuel and measure heat output over a timed period. Calculate combustion efficiency: η = heat output / (fuel mass × HHV). Target: >65% for grate furnace, >80% for fluidized bed.
5. Inspect ash residue — white/light gray indicates complete combustion. Black, unburned chunks indicate poor air distribution or oversized fuel.

**Expected Performance**:
- Combustion efficiency: 60-75% (grate furnace), 80-90% (fluidized bed)
- Steam output: 5-15 kg steam per kg of dry wood at 2-10 bar
- Flue gas temperature: 150-250°C (optimal range)
- Firebox temperature: 800-1,100°C with natural draft
- Fuel consumption rate: 5-20 kg/hour per 100 kW thermal output

**Strengths**:
- Simplest biomass conversion — direct fire with minimal processing
- Works with any dry biomass (wood, straw, husks, briquettes)
- Grate furnaces are buildable with basic metalworking skills
- No chemical processing or gas cleaning required

**Weaknesses**:
- Low combustion efficiency (60-75%) compared to gasification or oil burning
- Requires continuous fuel feeding — manual labor for small systems
- High particulate emissions without electrostatic precipitators or bag filters
- Moisture content directly reduces usable heat — green wood wastes 30-50% of combustion energy evaporating water

## Quantitative Parameters

## 5.1 Biogas Yield by Feedstock

| Feedstock | Biogas Yield (m³/kg VS added) | Methane Content (%) | C:N Ratio | Notes |
|-----------|-------------------------------|---------------------|-----------|-------|
| Cattle manure | 0.15-0.30 | 55-60 | 15-20 | Reliable, widely available |
| Pig manure | 0.30-0.50 | 60-65 | 10-15 | High nitrogen, may need carbon supplement |
| Poultry manure | 0.30-0.50 | 55-60 | 8-10 | Very high nitrogen — dilute or mix with straw |
| Food waste | 0.40-0.70 | 60-70 | 15-20 | High yield, easy to digest |
| Crop residues (straw) | 0.15-0.30 | 50-55 | 70-100 | Low nitrogen, slow to digest, needs pre-treatment |
| Grass / energy crops | 0.30-0.50 | 55-60 | 20-30 | Good C:N balance |
| Sewage sludge | 0.30-0.50 | 60-70 | 6-10 | Requires pathogen control |

VS = volatile solids (organic matter). Actual biogas yield depends on temperature, retention time, and C:N ratio.

## 5.2 Gasifier Performance by Fuel Type

| Parameter | Wood Chips | Charcoal | Agricultural Residues |
|-----------|-----------|----------|----------------------|
| Gas heating value (MJ/m³) | 4.5-6.0 | 4.0-5.5 | 3.5-5.0 |
| Gas composition (CO%) | 18-25 | 28-32 | 15-22 |
| Gas composition (H₂%) | 12-20 | 10-15 | 8-15 |
| Gas composition (CH₄%) | 2-4 | 1-3 | 1-3 |
| Cold gas efficiency (%) | 65-75 | 70-80 | 55-70 |
| Tar content (mg/m³) | 500-5,000 | <50 | 1,000-10,000 |
| Fuel consumption (kg/kWh_e) | 1.0-1.5 | 0.8-1.2 | 1.2-2.0 |
| Moisture limit (%) | <20 | <5 | <15 |

Cold gas efficiency = energy in product gas / energy in fuel input. Overall electrical efficiency (fuel to electricity) = cold gas efficiency × engine efficiency × generator efficiency ≈ 15-25%.

## 5.3 Biomass Heating Values

| Fuel | Higher Heating Value (MJ/kg) | Bulk Density (kg/m³) | Energy Density (GJ/m³) |
|------|------------------------------|----------------------|----------------------|
| seasoned firewood (20% MC) | 14-16 | 350-500 | 5-8 |
| Wood pellets (8% MC) | 17-18 | 600-700 | 10-13 |
| Wood chips (25% MC) | 12-14 | 250-350 | 3-5 |
| Charcoal | 28-32 | 180-250 | 5-8 |
| Straw / hay | 14-16 | 80-150 | 1-2 |
| Rice husks | 13-15 | 100-130 | 1-2 |
| Biogas (per m³) | 21-24 | 0.85-1.1 | 0.02 |
| Producer gas (per m³) | 4.5-6.0 | 0.9-1.2 | 0.005 |

## Scaling Notes

## Family Scale (1-5 kW thermal / 0.5-2 kW electric)

A 6 m³ biogas digester fed with manure from 5-10 cattle produces 1-3 m³ biogas per day (6-18 kWh thermal). Sufficient for a family's cooking needs. A small gasifier (10 cm diameter throat) consuming 2-5 kg/hour wood chips powers a 1-3 kW engine-generator. Construction: brick or concrete digester, steel gasifier, simple gas cleaning. Build time: 1-4 weeks.

## Village Scale (20-100 kW thermal / 10-50 kW electric)

A 50-100 m³ digester processes waste from 50-100 cattle or equivalent food waste, producing 15-50 m³ biogas/day (90-300 kWh thermal). A 30 cm diameter gasifier consuming 15-30 kg/hour wood chips drives a 10-30 kW engine-generator, providing electricity for 50-200 households. Requires: steel tank construction, gas piping network, engine maintenance skills. Build time: 2-6 months.

## Industrial Scale (500+ kW electric)

A 100 cm diameter gasifier consuming 100-300 kg/hour fuel drives a 100-500 kW engine-generator set. Alternatively, a biomass-fired steam boiler (2-10 tonnes steam/hour) drives a steam turbine at 20-35% thermal efficiency. Requires: consistent fuel supply chain (1,000-5,000 tonnes/year), mechanical fuel handling, water treatment for boiler, and skilled operators.

## Minimum Economic Scale

- **Biogas digester**: 6 m³ (family) is break-even. Below this, gas production is too low to justify construction effort.
- **Gasifier**: 10 kW electrical output. Below this, the gas cleaning complexity per unit power is excessive.
- **Biomass boiler**: 50 kW thermal. Below this, simple direct combustion in a stove is more practical.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low biogas production (<50% of expected) | Temperature too low (<20°C), or C:N imbalance, or toxic input (antibiotics in manure, pesticides) | Insulate and heat digester; adjust feedstock C:N ratio; avoid contaminated inputs |
| Digester pH drops below 6.5 (sour digester) | Overfeeding (excessive volatile acids), or low alkalinity | Stop feeding for 3-5 days; add lime (CaCO₃) or bicarbonate to raise pH to 7.0-7.5; resume feeding at reduced rate |
| Biogas has low methane content (<50%) | Short hydraulic retention time, or low temperature, or excessive water dilution | Increase retention time (reduce daily feeding); check temperature is 30-40°C; reduce water content of slurry |
| Gasifier produces tar-laden gas (engine fouling) | Insufficient throat temperature, or wet fuel, or channeling in fuel bed | Preheat combustion air; dry fuel to <20% moisture; ensure uniform fuel size to prevent channeling; add secondary air injection above throat |
| Engine power loss on producer gas | Gas too hot (>40°C at intake), or restricted gas flow, or incorrect air-fuel ratio | Cool gas further; check and clean filters; adjust mixer valve — optimize by monitoring exhaust oxygen |
| Gasifier bridge formation (fuel stops flowing) | Irregular fuel size, or high moisture causing swelling and bridging | Screen fuel to uniform size; dry fuel thoroughly; install mechanical agitator or stirrer in hopper |
| Flame burn-back into gasifier | Insufficient gas velocity through reactor, or air leak on gas line | Maintain minimum gas flow rate; check all gas connections for air ingress; install flame arrestor (water seal or fine mesh) on gas line |

## Safety

## Carbon Monoxide Poisoning

Producer gas contains 18-32% CO — lethal at 0.1% (1,000 ppm) concentration in air for 1 hour exposure. Biogas from the digester contains minimal CO, but any incomplete combustion of biogas in a confined space produces CO. Operate gasifiers and gas engines only in well-ventilated areas or outdoors. Install CO detectors in any enclosed space where gas equipment operates. Symptoms of CO poisoning: headache, dizziness, nausea, confusion. Evacuate immediately and ventilate if CO is suspected.

## Biogas Explosion

Biogas (60% CH₄) is explosive at 5-15% concentration in air. The digester gas holder stores gas at low pressure (10-50 mbar) — a leak into an enclosed space creates explosion risk. Install gas detectors in the vicinity of digesters. No open flames, welding, or spark sources near gas holders and piping. Ground all metal gas piping to prevent static discharge ignition.

## Gasifier High Temperature

Gasifier combustion zone reaches 1,000-1,200°C. The outer shell may reach 200-400°C without insulation. Install firebrick lining and outer insulation. Wear heat-resistant gloves when operating any valve or port on a running gasifier. Never open the fuel hopper lid while the gasifier is running — flash-back can ignite fuel in the hopper.

## Digestate Pathogens

Anaerobic digestion reduces pathogens significantly but does not eliminate them completely (especially at mesophilic temperatures). Treat digestate as potentially infectious material. Wear gloves when handling. Apply to fields with a minimum 30-day interval before harvest of crops consumed raw. Thermophilic digestion (50-60°C) achieves better pathogen kill (>99%).

## Gas Cleaning Chemicals

Iron sponge (iron oxide chips used for H₂S removal) generates iron sulfide, which is pyrophoric — it can spontaneously ignite when exposed to air after becoming saturated with H₂S. Replace iron sponge in a well-ventilated area away from ignition sources. Moisten spent iron sponge with water before disposal to prevent spontaneous combustion.

## Quality Control

## Biogas Composition

Measure methane content with a portable biogas analyzer (infrared methane sensor) or by simple combustion test (biogas that supports a stable blue flame has >50% methane). Target: 55-70% CH₄. Below 50%: digester is underperforming — check temperature, pH, and feedstock balance.

## Producer Gas Quality

- **Tar content**: <50 mg/m³ for engine use (higher tar fouls engine valves and piston rings within hours). Test: pass a known volume of gas through a filter, weigh tar deposit. If tar >100 mg/m³: improve throat design, add secondary air, or improve cooling/filtering.
- **Gas heating value**: 4-6 MJ/m³ for wood producer gas. Measure with a gas calorimeter or estimate from gas composition (measured by gas chromatography or Orsat apparatus).
- **Particulate content**: <50 mg/m³ for engine use. Test: filter sample, weigh deposit.

## Digestate Fertilizer Quality

Measure pH (target 7.0-8.0), total nitrogen content (target 1.5-3.0% on dry basis), and heavy metals (if industrial waste is co-digested). Compare to raw manure: digestate should have 10-20% higher plant-available nitrogen due to mineralization during digestion.

## Variations and Alternatives

## Comparison of Biomass Conversion Pathways

| Pathway | Output | Efficiency (fuel-to-useful) | Complexity | Scale | Best For |
|---------|--------|---------------------------|------------|-------|----------|
| Direct combustion | Heat | 60-75% | Low | Any | Heating, cooking, steam generation |
| Anaerobic digestion | Biogas (heat/electricity) | 30-50% (fuel-to-biogas) | Low-Medium | 6 m³ to 5,000 m³ | Wet waste (manure, food waste); cooking gas |
| Gasification (downdraft) | Producer gas → engine | 15-25% (fuel-to-electric) | Medium | 10-500 kW | Small-scale electricity from dry biomass |
| Gasification (updraft) | Producer gas → boiler | 65-80% (fuel-to-heat) | Medium | 100 kW-10 MW | Industrial heat from high-ash fuels |
| Pyrolysis (slow) | Char + bio-oil + gas | 30-50% (char yield) | Medium | Any | Charcoal production with liquid fuel co-product |
| Ethanol fermentation | Liquid fuel | 30-45% (sugar-to-ethanol) | High | 1,000+ L/batch | Transport fuel from sugar/starch crops |

## Updraft vs Downdraft Gasification

Downdraft gasifiers pass gas downward through the combustion zone, cracking tars at high temperature. This produces clean gas suitable for engines. However, downdraft gasifiers require uniform, low-ash fuel and have limited throughput per unit cross-section.

Updraft gasifiers pass gas upward through the fuel bed. The gas exits through the pyrolysis and drying zones, picking up tars. Gas tar content: 10,000-50,000 mg/m³ — unsuitable for engines without extensive cleaning. However, updraft gasifiers handle higher moisture and ash content, and achieve higher cold gas efficiency (70-85%). Best for direct combustion of the gas in boilers or kilns where tar is not a problem.

## Liquid Biofuels

- **Ethanol**: Ferment sugar or starch crops (sugarcane, corn, cassava), distill to 95% (azeotrope) or 99.5% (with molecular sieve dehydration). See [Fermentation](../chemistry/fermentation.md). Energy density: 23-24 MJ/kg (about 65% of gasoline). Used as gasoline substitute or blend component.
- **Biodiesel**: Transesterification of vegetable oils or animal fats with methanol and NaOH catalyst. Energy density: 37-38 MJ/kg (similar to diesel). Used as diesel substitute or blend. Requires oilseed press and methanol production (chemistry-dependent).
- **Wood diesel (Fischer-Tropsch)**: Catalytic conversion of syngas (from gasification) to liquid hydrocarbons. Complex catalyst system (iron or cobalt-based). Efficiency: 30-45% (fuel-to-liquid). Requires advanced chemical engineering — late bootstrap technology.

## See Also

- **[Charcoal Production](charcoal.md)** — Charcoal as gasifier fuel, pyrolysis chemistry
- **[Heat Engines](engine.md)** — Internal combustion engines modified for gas fuel
- **[Electricity Generation](electricity.md)** — Engine-generator sets, grid connection
- **[Chemistry / Fermentation](../chemistry/fermentation.md)** — Ethanol production chemistry
- **[Steam Power](steam-power.md)** — Biomass-fired steam boilers
- **[Energy Storage](storage.md)** — Gas storage systems
- **[Plants](../plants/structural-plants.md)** — Energy crop species and yields
- **[Fuel Production](fuels.md)** — Comparative fuel properties



[← Back to Energy](index.md)
