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

**Zones** (top to bottom):
1. **Fuel hopper** (top): Wood chips or charcoal loaded here. Dries as it descends. Seal against air ingress (gas must flow down, not out the top).
2. **Drying zone**: 100-200°C. Moisture evaporates from fuel. Downward gas flow provides heat.
3. **Pyrolysis zone**: 200-500°C. Volatile matter driven off as wood gas (tars, methane, other hydrocarbons). Char remains.
4. **Combustion zone** (around tuyeres): 800-1200°C. Limited air blown in through nozzles. Char partially combusts — provides heat for upper zones.
5. **Reduction zone** (below tuyeres): 800-1000°C. Hot char reacts with CO₂ and H₂O to produce CO and H₂. This is where the useful fuel gas is generated.
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

**Earth kiln** (simpler, lower technology): Stack wood in mound, cover with earth and straw, light through air vents at base. Controlled burn with limited oxygen. Quench by sealing vents when done. Yield: 15-25% charcoal. Lower quality control than retort but no steel vessel required.

### Gasification Chemistry

Wood gas (producer gas) is generated by partial combustion of biomass in a restricted air supply. The gasifier is a chemical reactor performing multiple simultaneous reactions:

**Drying zone** (100-200°C): Moisture evaporates from wood. Fresh wood (30-60% moisture) should be dried below 20% for efficient gasification — otherwise combustion energy wastes on evaporation. Air-dried wood reaches ~15-20% moisture.

**Pyrolysis zone** (200-500°C): Thermal decomposition of wood in the absence of oxygen. Produces: charcoal (solid carbon, 20-30% of dry wood mass), tar vapors (condensable organics — methanol, acetic acid, acetone, creosote), and non-condensable gases (CO, CO₂, CH₄, H₂). Tar is the primary operational problem in gasifiers — condenses in downstream piping, fouls engines. Tar content in raw producer gas: 10-100 g/Nm³ (must be reduced to <0.1 g/Nm³ for internal combustion engines).

**Combustion zone** (800-1200°C): Char and volatile gases react with limited oxygen (sub-stoichiometric air supply, typically 20-40% of full combustion air). C + O₂ → CO₂ (exothermic, provides heat for endothermic reactions). Some char: CO₂ + C → 2CO (Boudouard reaction). Water-gas reaction: C + H₂O → CO + H₂ (endothermic). Water-gas shift: CO + H₂O → CO₂ + H₂ (exothermic). Methanation: C + 2H₂ → CH₄ (exothermic, minor at atmospheric pressure).

**Reduction zone** (700-1000°C): CO₂ and H₂O from combustion zone react with hot charcoal: CO₂ + C → 2CO (endothermic, requires hot charcoal bed). H₂O + C → CO + H₂ (endothermic). These are the key producer-gas-forming reactions. Gas quality depends on: temperature (higher → more CO, less tar), charcoal bed depth (longer residence time → more complete reduction), and moisture content of fuel (some steam benefits gas quality via water-gas reaction; too much cools the bed).

**Typical producer gas composition** (downdraft gasifier, dry wood): CO 18-22%, H₂ 15-20%, CH₄ 2-4%, CO₂ 8-12%, N₂ 45-55% (from air), trace tars. Heating value: 4.5-6.0 MJ/Nm³ (vs 35-40 MJ/Nm³ for natural gas — producer gas is low-energy but adequate for internal combustion engines).

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

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
