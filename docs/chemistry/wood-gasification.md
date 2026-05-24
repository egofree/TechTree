# Wood Gasification

> **Node ID**: chemistry.petroleum-alternatives.wood-gasification
> **Domain**: Chemistry
> **Timeline**: Years 10-30
> **Outputs**: producer_gas, charcoal, wood_tar

### Producer Gas

**Composition**: ~25% CO (carbon monoxide), ~10% H₂ (hydrogen), ~60% N₂ (nitrogen from air), ~5% CO₂. Heating value ~5-6 MJ/m³ (low compared to natural gas at ~35 MJ/m³, but usable for engines and furnaces). The gas is a product of incomplete combustion — carbon reacts with limited oxygen to form CO rather than CO₂.

**Partial combustion chemistry**:
- C + ½O₂ → CO + heat (exothermic — provides the thermal energy for gasification)
- C + H₂O → CO + H₂ (endothermic water-gas reaction — add steam to enrich gas with hydrogen and increase heating value)
- C + CO₂ → 2CO (Boudouard reaction — shifts equilibrium at high temperatures)
- The net result is a combustible gas mixture that can power internal combustion engines and furnaces.

### Shaft Gasifier (Imbert-type downdraft)

**Construction**: Cylindrical steel shaft, 0.3-1.0 m diameter × 1-3 m tall. Lined with refractory brick (withstand 1000-1200°C internal temperatures). Steel outer shell with air inlet nozzles (tuyeres) near the middle. Gas outlet at bottom. Ash grate at very bottom (cast iron, replaceable).

**[Zones](../glossary/zones.md)** (top to bottom):
1. **[Fuel hopper](../glossary/fuel-hopper.md)** (top): Wood chips or charcoal loaded here. Dries as it descends. Seal against air ingress (gas must flow down, not out the top).
2. **Drying zone**: 100-200°C. Moisture evaporates from fuel. Downward gas flow provides heat.
3. **Pyrolysis zone**: 200-500°C. Volatile matter driven off as wood gas (tars, methane, other hydrocarbons). Char remains.
4. **[Combustion zone](../glossary/combustion-zone.md)** (around tuyeres): 800-1200°C. Limited air blown in through nozzles. Char partially combusts — provides heat for upper zones.
5. **[Reduction zone](../glossary/reduction-zone.md)** (below tuyeres): 800-1000°C. Hot char reacts with CO₂ and H₂O to produce CO and H₂. This is where the useful fuel gas is generated.
6. **Ash grate**: Charcoal and ash collect here. Periodically shake or rotate grate to drop ash into ash pit. Maintain gas flow through bed.

**Fuel requirements**: Hardwood chips (2-5 cm pieces), charcoal, or coke. Moisture content <20% (wet fuel produces steam, cools the bed, reduces gas quality). Fuel consumption: ~1-2 kg wood per kWh of engine output. Gas production: ~2-3 m³ gas per kg of dry wood.

### Gas Cleaning System

Producer gas contains tars, particulates, and water that will destroy engines quickly. Multi-stage cleaning required:

1. **Cyclone separator**: Gas enters tangential cyclone chamber. Centrifugal force throws heavy particles (ash, char dust) to outer wall. Particles slide down to collection hopper. Removes particles >10 μm. No moving parts, no consumable media.
2. **Water scrubber**: Gas bubbled through water tank (or sprayed with water in packed column). Dissolves water-soluble tars and ammonia. Cools gas to near-ambient temperature. Removes fine particulates. Water must be circulated and periodically replaced (tar-laden water is a disposal issue — contains phenols and creosotes).
3. **Sawdust or charcoal filter**: Gas passes through packed bed of fine sawdust or activated charcoal. Final polishing — removes remaining tars, fine particulates, and mist. Filter media replaced when saturated (color changes, pressure drop increases). Typically 30-60 cm deep bed in sealed steel container.
4. **Water trap / drip leg**: Low point in gas line where condensed moisture collects. Drain periodically. Essential to prevent water from entering engine carburetor.

### Engine Conversion

Internal combustion engines can run on producer gas with modifications:

- **Compression ratio reduction**: Producer gas has octane equivalent ~70-100 (high anti-knock). BUT gas has lower energy density than gasoline — engine produces ~40-60% of rated gasoline power. Enrich fuel-air mixture (larger carburetor jet or gas mixer). Common approach: dual-fuel system (start on gasoline, switch to producer gas once gasifier is hot and producing clean gas).
- **Gas-air mixer**: Replace carburetor with gas-air mixing valve. Simple butterfly valve controls gas flow into air intake. Adjustable to achieve correct air-fuel ratio (lean mixture for producer gas — ~1.1:1 air-to-gas ratio by volume for best power).
- **Ignition timing**: Advance ignition timing 5-10° (producer gas burns slower than gasoline — needs more advance for optimal combustion). Adjust by trial — advance until light knocking, then retard 2-3°.
- **Valves**: Producer gas contains no liquid fuel to lubricate valves. Install hardened exhaust valve seats (stellite or equivalent). More frequent valve maintenance.
- **Power output**: Expect 40-60% of gasoline-rated power. Derate vehicle payload and speed accordingly. A 40 HP gasoline engine produces ~16-24 HP on producer gas.

### WWII Applications

- **Vehicle gasifiers**: Over 500,000 vehicles in Europe converted to wood gas during WWII petroleum shortages. Gasifier mounted on trailer or vehicle rear. Typical range: 50-100 km per fueling (wood load). Refueling: 20-30 minutes to load wood and restart gasifier.
- **Stationary power**: Generator sets, water pumps, and industrial machinery converted to producer gas. Wood gasification extended industrial output despite fuel embargo.
- **Lessons**: Reliability requires disciplined maintenance (clean gas filter, drain water traps, shake ash grate). Startup time: 10-20 minutes to get clean gas from cold start. Carry gasoline for cold-start assistance. Cold weather operation difficult — gas quality suffers below -10°C.

### Charcoal Production

**Batch retort**: Iron or steel cylinder (1-2 m diameter × 2-4 m long), loaded with hardwood billets. Seal. Heat externally (burn wood waste or previous batch gas). Internal wood pyrolyzes: releases volatile gases (burned to heat retort — self-sustaining after initial heating), leaves charcoal. Temperature 400-600°C. Time: 12-24 hours. Cool before opening (charcoal ignites spontaneously when hot and exposed to air). Yield: 25-35% charcoal by weight.

**[Earth kiln](../glossary/earth-kiln.md)** (simpler, lower technology): Stack wood in mound, cover with earth and straw, light through air vents at base. Controlled burn with limited oxygen. Quench by sealing vents when done. Yield: 15-25% charcoal. Lower quality control than retort but no steel vessel required.

### Gasification Chemistry

Wood gas (producer gas) is generated by partial combustion of biomass in a restricted air supply. The gasifier is a chemical reactor performing multiple simultaneous reactions:

**[Drying zone](../glossary/drying-zone.md)** (100-200°C): Moisture evaporates from wood. Fresh wood (30-60% moisture) should be dried below 20% for efficient gasification — otherwise combustion energy wastes on evaporation. Air-dried wood reaches ~15-20% moisture.

**[Pyrolysis zone](../glossary/pyrolysis-zone.md)** (200-500°C): Thermal decomposition of wood in the absence of oxygen. Produces: charcoal (solid carbon, 20-30% of dry wood mass), tar vapors (condensable organics — methanol, acetic acid, acetone, creosote), and non-condensable gases (CO, CO₂, CH₄, H₂). Tar is the primary operational problem in gasifiers — condenses in downstream piping, fouls engines. Tar content in raw producer gas: 10-100 g/Nm³ (must be reduced to <0.1 g/Nm³ for internal combustion engines).

**[Combustion zone](../glossary/combustion-zone.md)** (800-1200°C): Char and volatile gases react with limited oxygen (sub-stoichiometric air supply, typically 20-40% of full combustion air). C + O₂ → CO₂ (exothermic, provides heat for endothermic reactions). Some char: CO₂ + C → 2CO (Boudouard reaction). Water-gas reaction: C + H₂O → CO + H₂ (endothermic). Water-gas shift: CO + H₂O → CO₂ + H₂ (exothermic). Methanation: C + 2H₂ → CH₄ (exothermic, minor at atmospheric pressure).

**[Reduction zone](../glossary/reduction-zone.md)** (700-1000°C): CO₂ and H₂O from combustion zone react with hot charcoal: CO₂ + C → 2CO (endothermic, requires hot charcoal bed). H₂O + C → CO + H₂ (endothermic). These are the key producer-gas-forming reactions. Gas quality depends on: temperature (higher → more CO, less tar), charcoal bed depth (longer residence time → more complete reduction), and moisture content of fuel (some steam benefits gas quality via water-gas reaction; too much cools the bed).

**[Typical producer gas composition](../glossary/typical-producer-gas-composition.md)** (downdraft gasifier, dry wood): CO 18-22%, H₂ 15-20%, CH₄ 2-4%, CO₂ 8-12%, N₂ 45-55% (from air), trace tars. Heating value: 4.5-6.0 MJ/Nm³ (vs 35-40 MJ/Nm³ for natural gas — producer gas is low-energy but adequate for internal combustion engines).

### Gas Cleaning — Detailed Design

**Cyclone separator**: First stage — removes particles >5 µm by centrifugal force. Gas enters tangentially at 10-20 m/s, particles flung to wall and collected in hopper. Efficiency: 80-95% for >10 µm particles. Must be well-insulated to prevent tar condensation inside — tar-laden dust forms hard deposits that are extremely difficult to remove.

**Wet scrubber (packed tower)**: Gas flows upward through a bed of packing material (ceramic saddles or plastic rings) while water flows downward. Removes particles <5 µm and some water-soluble tars. Water-gas contact area: 100-200 m² per m³ of packing. Water circulation rate: 5-10 L/Nm³ gas. Effluent water contaminated with tars, phenols, and fine char — requires treatment before discharge (biological oxidation or activated carbon).

**Fabric filter (baghouse)**: Fine particulate filtration through woven or felted fabric bags (polypropylene, PTFE, or fiberglass depending on temperature). Filtration efficiency: >99% for particles >1 µm. Must operate above tar dew point (~150-200°C) to prevent blinding. Pulse-jet cleaning: compressed air pulses inflate bags in reverse, dislodging dust cake.

**Electrostatic precipitator (ESP)**: Best tar removal — ionizes gas with high-voltage electrodes (10-30 kV), charged tar droplets migrate to grounded collection plates. Tar removal: >99%. Requires corrosion-resistant construction (316L stainless steel) — tar condensate is acidic. Some designs use wet ESP with water wash. ESP is the most effective but also most expensive gas cleaning approach.

### Engine Conversion Detail

**Spark-ignition engine**: Producer gas replaces gasoline or works in dual-fuel mode. Engine modifications: (1) Carburetor replaced with gas-air mixer (venturi-type or electronically controlled). (2) Compression ratio may be increased from 8:1 to 10-12:1 — producer gas has higher octane rating (resists knock) than gasoline. (3) Ignition timing advanced 5-15° — producer gas burns slower than gasoline. (4) Larger engine displacement needed — producer gas has ~40% the energy per volume of gasoline-air mixture, so engine produces 40-60% of rated gasoline power. A 100 kW gasoline engine produces 40-60 kW on producer gas.

**Dual-fuel diesel engine**: Diesel pilot injection (5-15% of full-load fuel) ignites the producer gas-air mixture. No spark plugs needed. Higher compression ratio (14-20:1) than spark-ignition. Efficiency: 30-38% (vs 25-30% for spark-ignition on producer gas). The gold standard for producer gas power generation — widely used in WWII and in modern biomass power plants (1-5 MW range).

### Charcoal Production (Byproduct)

Charcoal yield from wood pyrolysis: 20-35% by weight (higher with slower heating rate and lower peak temperature). Charcoal properties: fixed carbon 75-90%, volatile matter 10-25%, ash 1-5%. Higher heating value: 28-33 MJ/kg (vs 16-18 MJ/kg for dry wood). Uses: steelmaking (historically — before coke replaced it in blast furnaces), cooking fuel (developing world), water filtration (activated carbon after steam activation at 800-900°C), soil amendment (biochar — carbon sequestration), artist material, metallurgical reductant (ferrosilicon, silicon metal production).

**Charcoal kiln designs**: (1) Earth kiln (traditional): stack wood in dome, cover with earth/sod, ignite at bottom, control air entry. Yield: 20-25%, cycle: 5-10 days. (2) Concrete block kiln (semi-portable): walls of stacked concrete blocks with air inlet ports. Yield: 25-30%, cycle: 2-5 days. (3) Retort (industrial): steel vessel heated externally — wood pyrolyzes without combustion air, pyrolysis gases burned to provide heat. Yield: 30-35%, cycle: 12-24 hours. Retort captures and uses pyrolysis gases — significantly higher efficiency. (4) Continuous retort (Lambiotte): wood moves through heated zones on a conveyor — continuous production.

### Safety & Hazards

- **Carbon monoxide**: Producer gas is ~25% CO — odorless, colorless, lethal. CO binds to hemoglobin 200x more strongly than oxygen. Symptoms: headache, dizziness, nausea → unconsciousness → death. Concentrations >1000 ppm are immediately dangerous. NEVER operate gasifier indoors or in enclosed spaces. CO detector mandatory. Vent all exhaust to atmosphere.
- **Gasifier fire**: Operating temperature 800-1200°C. Touching gasifier shell causes severe burns. Maintain thermal insulation. Allow full cooling before maintenance.
- **Explosion**: Producer gas mixed with air in the right proportions (20-75% gas in air) is explosive. Gasifier must produce gas under slight suction (engine draws gas through — negative pressure prevents gas leaks). NEVER introduce air into hot gasifier (backfire through open nozzle = explosion in fuel hopper).
- **Tar and creosote exposure**: Wood tar contains phenols, cresols, and polycyclic aromatic hydrocarbons — skin irritants and suspected carcinogens. Wear gloves when handling scrubber water and filters. Wash skin immediately after contact.
- **Ash disposal**: Wood ash is alkaline (pH 10-12). Irritating to skin and eyes. Handle with gloves. Ash from treated or painted wood may contain heavy metals — dispose of at designated waste site, not in gardens.

 *Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*

## Gasifier Types and Selection

**Updraft gasifier**: Air enters below the grate and flows upward through the fuel bed. Gas exits at the top. Temperature gradient: ambient at top (drying zone), 200-500°C in the middle (pyrolysis), 800-1200°C at the bottom (combustion/reduction). High thermal efficiency (80-90% of fuel energy in the gas) because outgoing gas preheats incoming fuel. However, tar content is very high (10-50 g/m³) because pyrolysis vapors pass through the cool upper fuel bed without cracking. Updraft gasifiers are suitable for direct combustion (furnaces, boilers, kilns) where tar is burned along with the gas. Not suitable for engines without extensive gas cleaning.

**Downdraft gasifier (Imbert type)**: Air enters at the throat (restricted middle section) and gas flows downward. Pyrolysis vapors must pass through the hot combustion zone (1000-1200°C) before exiting, thermally cracking most tars. Tar content typically <1 g/m³, often <0.1 g/m³ with good design. This makes downdraft gasifiers the preferred type for engine applications. Limitations: fuel must be uniformly sized (2-5 cm chips), moisture content <20%, and throughput is limited to 10-500 kW thermal output. Larger sizes suffer from inconsistent airflow across the throat.

**Fluidized bed gasifier**: Air or oxygen blown upward through a bed of fine inert particles (sand, dolomite, or alumina) at sufficient velocity to fluidize the bed (suspends particles in upward gas flow). Biomass fed into the hot bed (700-900°C) gasifies rapidly due to excellent heat transfer. Advantages: handles varied feedstock sizes and moisture contents, scales well to 10-100 MW thermal, good temperature control. Disadvantages: high tar content (5-20 g/m³, intermediate between updraft and downdraft), high particulate carryover (bed material entrained in gas), and complex control (bed temperature, fluidization velocity, feed rate must be balanced).

## Gas Composition and Properties

**Producer gas (air-blown)**: CO 20-25%, H₂ 10-15%, CH₄ 2-3%, CO₂ 8-12%, N₂ 50-55%, water vapor 5-15%, tar 0.01-50 g/m³ depending on gasifier type. Calorific value 4-6 MJ/Nm³ (dry). This is a low-energy gas because nitrogen from the air dilutes the combustible components. Stoichiometric air-gas ratio for combustion: 1.0-1.5:1 by volume (much less air needed than for natural gas at 10:1).

**Syngas (oxygen-blown)**: When pure oxygen replaces air as the gasifying agent, nitrogen dilution is eliminated. Composition: CO 35-45%, H₂ 25-35%, CO₂ 15-25%, CH₄ 0-5%, small amounts of H₂O and trace contaminants. Calorific value 10-15 MJ/Nm³, comparable to low-quality natural gas. Oxygen-blown gasification requires an air separation unit (ASU, significant capital and energy cost) but produces a much more versatile synthesis gas suitable for Fischer-Tropsch liquids, methanol synthesis, and hydrogen production via water-gas shift.

## Gas Cleaning Systems

**Cyclone separator design**: Gas enters tangentially at 10-20 m/s inlet velocity, creating a vortex. Centrifugal acceleration 100-1000× gravity forces particles to the wall. Collection efficiency follows the "50% cut diameter" (d₅₀): the particle size captured at 50% efficiency. For a well-designed cyclone: d₅₀ = 5-10 μm. Particles >20 μm captured at >95%. Pressure drop 0.5-2.0 kPa. Design parameters: barrel diameter 0.2-2.0 m (scaled to gas flow), cone length 1.5-2.5× barrel diameter, inlet area = 0.1-0.2× barrel cross-section. Must be insulated or heated above 200°C to prevent tar condensation inside.

**Fabric filter (baghouse)**: Woven or felted fabric bags (1-5 m long, 0.15-0.3 m diameter) filter gas at face velocity 0.5-2.0 m/min. Particles form a dust cake on the bag surface that enhances filtration. Efficiency >99% for particles >1 μm, 90-99% for 0.5-1 μm. Operating temperature limited by fabric: polypropylene to 90°C, PTFE to 260°C, fiberglass to 280°C. Must operate above tar dew point (150-200°C) to prevent blinding. Pulse-jet cleaning: compressed air (0.4-0.7 MPa) pulses inject into bags in reverse, dislodging dust cake into collection hopper.

**Venturi scrubber**: Gas accelerated through a narrow throat (50-100 m/s velocity) where scrubbing liquid (water) is injected. High-velocity gas atomizes the water into fine droplets (10-100 μm). Particles collide with and are captured by droplets. Collection efficiency for 0.5-5 μm particles: 90-99%. Pressure drop: 5-25 kPa (high energy consumption). Liquid-to-gas ratio: 1-5 L/m³. Excellent for tar aerosol and fine particulate removal. Effluent water requires treatment for tar and phenol removal before discharge.

**Tar cracking (thermal and catalytic)**: At 1000-1100°C, tar molecules decompose to smaller, non-condensable gases (CO, H₂, CH₄). Thermal cracking requires high temperature and 1-3 seconds residence time. Catalytic cracking uses dolomite (CaMg(CO₃)₂), olivine (Mg₂SiO₄), or nickel-based catalysts at 800-900°C to achieve >95% tar destruction. Dolomite is cheap but erodes in fluidized beds. Nickel catalysts are more effective but deactivate due to carbon deposition and sulfur poisoning. Tar cracking eliminates the tar problem at its source rather than capturing it downstream.

## Engine Conversion Parameters

**Spark-ignition engine on producer gas**: Timing advance must be increased to 15-25° BTDC (before top dead center) because producer gas burns slower than gasoline (laminar flame speed ~0.4 m/s vs ~0.8 m/s for gasoline-air). Compression ratio can be increased to 10-12:1 (producer gas has high octane equivalent, resists knock) to partially compensate for the lower energy density. Derating: engine produces 30-50% less power than on gasoline due to the low heating value of producer gas (4-6 MJ/m³ vs 3.5-3.7 MJ/m³ for stoichiometric gasoline-air mixture). A 100 kW gasoline engine delivers 50-70 kW on producer gas.

**Diesel dual-fuel operation**: Producer gas replaces 80-95% of the diesel fuel. Pilot diesel injection (5-20% of full-load fuel) provides ignition, and the producer gas-air mixture burns as a lean premixed charge. Compression ratio 14-20:1 (standard diesel). Thermal efficiency 30-38%, higher than spark-ignition on producer gas because the higher compression ratio extracts more work. Advantages: no ignition system modification needed, can revert to 100% diesel operation instantly if gasifier is unavailable. The most practical engine option for producer gas power generation.

## Gasifier Sizing and Performance

**Sizing calculation**: Gasifier thermal output (kW) determines the physical dimensions. A 100 kW (thermal) downdraft gasifier processes ~30-40 kg/hour of dry wood (energy content 16-18 MJ/kg). Gasifier hearth diameter: ~300 mm for 100 kW, scaling roughly with the square root of throughput. Overall height 1.5-2.5 m. Fuel hopper volume: sufficient for 1-4 hours of operation (20-160 kg wood). Grate area: 0.07-0.1 m² per 100 kW. Air supply: 2.5-3.5 kg air per kg dry wood (sub-stoichiometric, ~30% of stoichiometric air for complete combustion).

**Cold gas efficiency**: Chemical energy in the product gas / energy in the fuel input. Downdraft gasifier: 65-75%. Updraft gasifier: 70-80% (higher because more of the fuel's energy stays in the gas as tar and hydrocarbons). Fluidized bed: 70-80%. The remaining 20-35% is lost as sensible heat in the gas, radiation from the gasifier shell, and unburned carbon in the ash.

**Startup procedure**: Load hopper with dry wood chips or charcoal. Open air inlet. Light kindling at the grate or ignite charcoal bed through the ignition port. Allow 10-20 minutes for the combustion zone to establish and the reduction zone to reach operating temperature (700-900°C, indicated by gas flare burning with clear blue flame rather than yellow smokey flame). Connect to engine only after gas quality is verified (flare test: gas burns cleanly at the flare stack). Cold weather increases startup time significantly.

## Producer Gas Applications Beyond Engines

**Direct combustion**: Producer gas burned in furnaces, kilns, boilers, and dryers without gas cleaning (tar tolerance is higher because the gas is burned immediately). Glass melting furnaces, brick kilns, lime kilns, and grain dryers have all been operated on producer gas. Thermal efficiency of direct combustion: 70-85%. The gas can substitute for natural gas or fuel oil in most burner designs with modified orifices and air-fuel ratio adjustments.

**Heat for buildings and greenhouses**: Gasifier connected to a heat exchanger provides clean hot air or hot water. The gas burns in a dedicated combustion chamber, and the flue gases pass through a heat exchanger (never mix raw producer gas with breathing air). Greenhouse heating: gasifier + heat exchanger + CO₂ enrichment (clean flue gas from efficient combustion contains 10-15% CO₂ that can be fed to the greenhouse to boost plant growth, provided CO and NOx are below toxic levels).

**Cogeneration (CHP)**: Combined heat and power. Gas engine-generator produces electricity (25-30% electrical efficiency). Engine jacket cooling water and exhaust heat recovered for space heating, drying, or process heat. Overall CHP efficiency: 70-85%. Small-scale biomass CHP (50-500 kWe) is economically attractive in locations with reliable biomass supply and high electricity prices. District heating systems in Scandinavian communities commonly use biomass gasification CHP.

## Biomass Feedstock Properties

**Wood composition**: Dry hardwood contains approximately 48-50% cellulose, 20-25% hemicellulose, 20-25% lignin, and 1-5% extractives (resins, terpenes, tannins). Softwoods have similar cellulose content but higher lignin (25-30%) and different hemicellulose composition (more mannose, less xylose than hardwoods). Higher heating value (HHV) of dry wood: 18-20 MJ/kg (slight variation by species; resinous softwoods are marginally higher due to hydrocarbon extractives).

**Moisture content effects**: Fresh-cut wood contains 30-60% moisture (wet basis). Air-dried wood reaches equilibrium at 15-20% moisture depending on climate. Each percentage point of moisture above 20% reduces gasifier efficiency by roughly 1% because combustion energy is wasted evaporating water instead of driving gasification reactions. At 50% moisture, roughly 15% of the wood's energy content goes to water evaporation. For this reason, many gasifier designs include a separate drying stage (flue gas or solar drying of fuel before gasification).

**Briquetting**: Loose biomass (sawdust, agricultural residues, wood chips) can be compacted into dense briquettes (40-80 mm diameter × 50-150 mm long, density 0.8-1.2 g/cm³) using a piston press or screw extruder at 100-200 MPa without binder (lignin softens at ~100°C under pressure, acting as a natural binder). Briquettes have uniform size, low moisture (<10%), and higher energy density than loose biomass. Suitable for gasifiers requiring consistent fuel dimensions.

**Alternative feedstocks**: Beyond wood, gasifiers can process agricultural residues (rice husk, corn stover, coconut shells, sugarcane bagasse), but these feedstocks have different ash compositions that can cause slagging and fouling. Rice husk ash (15-20% silica) forms glassy deposits. Wheat straw has high potassium content that lowers ash fusion temperature, causing clinker formation in the gasifier hearth. These feedstocks often require modified gasifier designs (grate spacing, ash removal systems) and sometimes lower operating temperatures to manage ash behavior.

## Producer Gas Safety Systems

**CO monitoring**: Producer gas contains 20-25% CO, making CO detectors mandatory in any gasification facility. Electrochemical CO sensors (0-500 ppm range, alarm at 50 ppm TLV-TWA and 100 ppm TLV-STEL). Sensors placed at breathing height (1.5 m) and at low points (CO density 0.97× air, nearly neutral but tends to accumulate in low areas). Multi-sensor array: monitor at the gasifier, near the engine, and at the operator station. If CO exceeds 200 ppm, automatic ventilation fans activate and alarm sounds. Personnel must evacuate immediately and re-enter only with SCBA (self-contained breathing apparatus).

**Gas flare system**: A properly designed flare is essential for safe gasifier operation during startup, shutdown, and emergencies. The flare must burn all producer gas whenever it cannot be used by the engine. Stack height: minimum 3 m above the gasifier roofline, with spark arrestor. Flare ignition: continuous pilot flame or automatic spark igniter. Flame monitoring: UV sensor confirms pilot flame is lit. If flame is lost, gas diversion valve switches from flare to a vent stack (taller, open-top pipe) to prevent unburned gas accumulation.

**Backfire prevention**: The greatest explosion risk in gasifier-engine systems. Backfire occurs when a flame front travels backward through the gas line from the engine into the gasifier. Prevention: (1) flame trap (fine mesh screen or packed gravel section in the gas line that quenches flame propagation, similar to a Davy lamp principle), (2) water seal (gas line dips below water level, creating a liquid barrier that flame cannot pass), (3) one-way check valve in the gas line, (4) maintain the gasifier under slight vacuum (engine suction mode) rather than positive pressure (blower mode) so any leak draws air in rather than pushing gas out.

## Gasifier Material Selection

**Refractory lining**: The combustion and reduction zones of the gasifier operate at 800-1200°C, requiring refractory lining. Fireclay brick (Al₂O₃ 30-40%, service to 1300-1400°C) is adequate for most gasifier designs. Brick thickness: 50-100 mm on the inside of the steel shell, with an air gap or insulating blanket between the brick and shell. The throat area of downdraft gasifiers experiences the highest temperatures and most chemical attack (reducing atmosphere with CO, H₂, and alkali vapors from wood ash), and may need higher-grade refractory (high-alumina or silicon carbide) for extended life.

**Steel shell construction**: The outer gasifier shell is mild steel plate (4-8 mm thick), welded cylindrical construction with bolted top and bottom caps. The shell must be airtight (all seams welded or gasketed). Access doors for fuel loading, ash removal, and grate maintenance are bolted with high-temperature gaskets (ceramic fiber or compressed mineral wool). Air inlet nozzles (tuyeres) are stainless steel or high-alumina ceramic, projecting 30-50 mm into the combustion zone to avoid overheating the steel shell. Water jacket cooling around the throat area is an alternative to refractory lining: water absorbs heat, reducing shell temperature and providing hot water as a byproduct.

**Grate design**: The grate supports the fuel bed and allows ash to fall through while maintaining gas flow. Cast iron grates are standard (withstand 600-800°C in the reduction zone). Rotating or shaking grates (manually operated lever or automated cam mechanism) break up clinker formations and clear ash blockages. Grate open area: 10-20% of total cross-section (too much open area and the bed collapses; too little and gas flow is restricted). Ash pit below the grate: sized for 4-8 hours of ash accumulation before emptying is required.

## Gasifier Performance Benchmarks

**Downdraft gasifier benchmarks**: For a 100 kW thermal output Imbert-type gasifier processing dry hardwood chips (moisture <20%), typical performance parameters are: fuel consumption 30-35 kg/hour, gas production 60-90 m³/hour, gas heating value 4.5-5.5 MJ/m³, cold gas efficiency 65-75%, hot gas efficiency (including sensible heat) 80-85%. Startup time from cold: 15-25 minutes. Maximum continuous runtime before ash grate cleaning: 4-8 hours. Engine power output on gas: 15-25 kWe (from 100 kWth gasifier, at 15-25% electrical efficiency).

**Large-scale gasification**: Fluidized bed gasifiers at 5-50 MWth scale achieve better economics than small downdraft units but require more complex operation. Biomass feed rate: 1-10 tonnes/hour. Gas production: 2000-20,000 m³/hour. Applications: district heating, industrial process heat, and power generation (1-10 MWe via gas engine or gas turbine). Capital cost: $1,000-3,000 per kWth installed. Operating cost: $10-30/MWhth (dominated by biomass feedstock at $30-80/tonne dry). Biomass gasification is competitive with natural gas at gas prices above $6-8/GJ.

**Comparison with direct combustion**: Burning wood directly in a boiler achieves 75-85% thermal efficiency (higher than gasification at 65-75% cold gas efficiency). However, gasification provides cleaner combustion (gas burns more completely than solid fuel), better load following (gas flow responds faster than solid fuel feed), and the ability to run engines for power generation (impossible with direct combustion). For heat-only applications, direct combustion is simpler and more efficient. For combined heat and power, gasification is the appropriate technology at small-medium scale (50 kWe - 5 MWe). Above 5 MWe, combustion with steam turbine is typically more economical.

## Gasification Historical Development

**Early development**: Gasification of solid fuels dates to the 1660s (Thomas Shirley produced "flammable air" from coal), but practical gasifiers emerged in the 1870s for town gas production. By 1900, producer gas engines powered thousands of industrial facilities in Europe and America. The technology declined in the petroleum age but was revived during WWII when over 1 million vehicles in Europe were converted to wood gas. Post-war, cheap gasoline eliminated wood gas vehicles, but the oil crises of the 1970s triggered renewed research into biomass gasification for energy independence.

**Modern development**: Since the 1980s, fluidized bed gasification has been scaled to 50-100 MWth capacity for combined heat and power in Scandinavian countries with abundant forestry residues. Integrated gasification combined cycle (IGCC) power plants using coal gasification at 250-600 MWe scale have been demonstrated (Tampa Electric Polk Power Station, 250 MWe, operated 1996-2016), but high capital costs and reliability challenges have limited adoption. Small-scale gasification (10-500 kWe) continues to serve off-grid communities and agricultural processing facilities in developing countries, where petroleum fuels are expensive or unavailable.

## Tar Properties and Handling

**Tar composition**: Wood gasifier tar is a complex mixture of >100 organic compounds. Major components: benzene (5-15%), toluene (3-8%), naphthalene (2-10%), phenol (1-5%), cresols (1-3%), polycyclic aromatic hydrocarbons (PAHs: pyrene, anthracene, fluorene, 0.1-1%), and oxygenated aromatics (guaiacol, syringol from lignin depolymerization, 1-5%). Tar dew point: 150-350°C depending on composition and water content. Below the dew point, tar condenses as a sticky brown-black liquid that blocks pipes, fouls valves, and adheres to engine components.

**Tar disposal**: Tar-laden water from scrubbers and filters is classified as hazardous waste in most jurisdictions (contains phenols, PAHs, and benzene derivatives). Treatment options: (1) thermal oxidation (burn in a dedicated furnace at 900-1200°C, destroys organics but requires fuel if water content is high), (2) biological treatment (acclimatized bacteria degrade phenols and light aromatics, but PAHs persist), (3) chemical oxidation (Fenton's reagent: H₂O₂ + Fe²⁺ generates hydroxyl radicals that oxidize organics, effective but costly), (4) separation and recycling (extract tars with solvent, recover phenol as a chemical product). The tar disposal problem is a significant environmental and economic challenge for gasification technology.

Wood gasification technology occupies a pragmatic niche in the energy landscape: not suitable as a primary energy source for industrial civilization, but invaluable as a backup, supplementary, and distributed energy technology when petroleum is unavailable or unaffordable.

## Limitations

- **Tar production**: All gasifiers produce tar (complex aromatic hydrocarbons) that condenses in cool downstream equipment. Tar is the single greatest operational problem — it blocks pipes, fouls valves, and contaminates engines. Tar cracking (thermal or catalytic) adds complexity and reduces net efficiency by 5-15%.
- **Low energy density of producer gas**: Wood gas has a heating value of only 4-7 MJ/Nm³ (vs 35-40 MJ/Nm³ for natural gas). This means gas pipes, compressors, and burners must be 5-10× larger for equivalent energy throughput. Wood gas is practical only for on-site or short-distance use — long-distance pipeline transport is uneconomical.
- **Feedstock variability**: Wood moisture content (15-60% depending on seasoning), species density, and piece size all affect gasifier performance. Gasifiers must be derated for wet fuel (10-30% capacity loss). Consistent fuel preparation (drying, chipping to uniform size) adds cost and complexity.
- **Scale limitations**: Wood gasification is practical up to ~10 MW thermal output. Above this scale, fuel supply logistics (gathering, transporting, and drying wood for a 10+ MW plant consuming 2-5 tonnes/hour of dry wood) become prohibitive. Coal or natural gas gasification is preferred for large-scale syngas production.

## See Also

- **[Petroleum Alternatives](petroleum-alternatives.md)**: Fossil fuel substitutes including biomass
- **[Distillation](distillation.md)**: Fractional distillation of wood tar and creosote
- **[Solvents](solvents.md)**: Turpentine and methanol from wood pyrolysis
- **[Explosives](explosives.md)**: Charcoal as a component of black powder
- **[Energy](../energy/index.md)**: Power generation from producer gas
