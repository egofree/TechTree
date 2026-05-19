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

### Safety & Hazards

- **Carbon monoxide**: Producer gas is ~25% CO — odorless, colorless, lethal. CO binds to hemoglobin 200x more strongly than oxygen. Symptoms: headache, dizziness, nausea → unconsciousness → death. Concentrations >1000 ppm are immediately dangerous. NEVER operate gasifier indoors or in enclosed spaces. CO detector mandatory. Vent all exhaust to atmosphere.
- **Gasifier fire**: Operating temperature 800-1200°C. Touching gasifier shell causes severe burns. Maintain thermal insulation. Allow full cooling before maintenance.
- **Explosion**: Producer gas mixed with air in the right proportions (20-75% gas in air) is explosive. Gasifier must produce gas under slight suction (engine draws gas through — negative pressure prevents gas leaks). NEVER introduce air into hot gasifier (backfire through open nozzle = explosion in fuel hopper).
- **Tar and creosote exposure**: Wood tar contains phenols, cresols, and polycyclic aromatic hydrocarbons — skin irritants and suspected carcinogens. Wear gloves when handling scrubber water and filters. Wash skin immediately after contact.
- **Ash disposal**: Wood ash is alkaline (pH 10-12). Irritating to skin and eyes. Handle with gloves. Ash from treated or painted wood may contain heavy metals — dispose of at designated waste site, not in gardens.

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
