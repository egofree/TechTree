# Fuel Production

> **Node ID**: energy.fuels
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`foundations.fire`](../foundations/fire.md)
> **Enables**: [`energy.engine`](engine.md), [`energy.fuels.charcoal`](charcoal.md), [`energy.fuels.coal`](coal.md), [`energy.fuels.coke`](coke.md), [`glass.advanced.glassblowing`](../glass/advanced-glassblowing.md), [`machine-tools.forming`](../machine-tools/forming.md), [`metals.alloys`](../metals/alloys.md), [`metals.steelmaking`](../metals/steelmaking.md), [`mining.processing`](../mining/processing.md), `plants`, `transport`
> **Timeline**: Years 0-25
> **Outputs**: solid_fuels, liquid_fuels, gaseous_fuels
> **Critical**: Yes — every industrial process requires fuel matched to its temperature and energy-density requirements; no fuels means no smelting, no steam, no engines

## Why Fuels Matter

**Strengths** (wood as fuel):
- Universally available — grows on every continent except Antarctica
- Renewable — trees regrow in 20-80 years
- Burns at 700-900°C with natural draft — sufficient for pottery, copper smelting, space heating

**Weaknesses** (wood as fuel):
- Low energy density (14-16 MJ/kg) — large volumes needed for industrial processes
- Seasonal supply — green wood requires 6-12 months of air drying before use
- Deforestation risk — industrial-scale consumption can deplete local forests faster than regrowth
- Inadequate for iron smelting without charcoal conversion (temperature and atmosphere control)

Fuels are the energy carriers that convert stored chemical energy into heat, motion, and light. Every industrial process — smelting iron, firing ceramics, generating electricity, powering engines — requires a fuel matched to its temperature, cleanliness, and energy-density requirements. Selecting the wrong fuel wastes effort and limits output; selecting the right one unlocks the next capability tier.

The bootstrap sequence progresses through fuels in rough order of refinement: wood → charcoal → coal → coke → petroleum fractions → synthetic gases and liquids. Each step increases energy density, burns hotter or cleaner, and enables processes the previous fuel could not sustain. The chain is also a dependency chain: charcoal requires wood pyrolysis knowledge; coke requires coal mining and oven construction; petroleum fractions require drilling and distillation. The bootstrap cannot skip steps — you cannot run a blast furnace on wood any more than you can distill gasoline without first building a still.

## Prerequisites

- **Materials**: [Wood](../glossary/wood.md) (hardwood, seasoned 6-12 months to <20% moisture), [coal](coal.md) (bituminous or anthracite — requires mining), [limestone](../ceramics/lime.md) (flux for coking), [petroleum crude](../chemistry/petroleum-alternatives.md) (requires drilling and pumping), [vegetable oil](../plants/fiber-plants.md) (pressed from oil seeds), [methanol or ethanol](../chemistry/petroleum-alternatives.md) (for biodiesel transesterification)
- **Tools**: [Axe and saw](../machine-tools/index.md) for wood harvesting, [charcoal kiln or pit](charcoal.md) for pyrolysis, [coke oven](coke.md) (beehive or by-product), [distillation column](../chemistry/petroleum-alternatives.md) for petroleum fractions, [gasifier](./index.md) (for producer gas generation), [press](../machine-tools/index.md) for vegetable oil extraction
- **Knowledge**: Combustion chemistry (stoichiometric air-fuel ratios, incomplete combustion, CO formation), pyrolysis and carbonization, fractional distillation (boiling point separation), calorimetry (measuring fuel energy content), flash point and auto-ignition temperature
- **Infrastructure**: Fuel storage (dry, ventilated, separated from ignition sources), transport (carts, barrels, pipelines for liquid/gaseous fuels), ventilation for enclosed combustion spaces, CO detectors for all fuel-burning installations

## Bill of Materials — Charcoal Production (1-tonne batch, earth kiln)

| Item | Specification | Quantity | Notes |
|------|--------------|----------|-------|
| Hardwood logs | 20-40 cm diameter, 1-1.5 m long, seasoned | 4-6 tonnes (yield: 20-40% by weight) | Oak, ash, maple preferred; avoid softwoods (low density → fragile charcoal) |
| Earth kiln site | Level ground, 3-4 m diameter cleared area | 1 site | Clay soil preferred for sealing; away from structures and dry vegetation |
| Kindling and dry brush | Small branches, straw | 20-30 kg | For initial ignition at center of stack |
| Covering material | Clay soil, sod, or wet leaves | Sufficient to cover 3-4 m diameter × 1.5 m high stack | Must seal completely — air leaks cause combustion instead of pyrolysis |
| Vent holes | 8-12 holes at base, 1-2 at top | Poke through covering | Base holes control air intake; top holes allow smoke/tar venting |
| Monitoring tools | Long stick or iron rod | 1 | Poke into stack to check carbonization progress — charcoal feels crumbly, wood feels firm |
| Tools for unloading | Shovel, rake, buckets, water | As needed | Quench hot charcoal with water or earth if combustion starts during unloading |

## Solid Fuels

## Wood

- **Seasoned hardwood**: ~16-18 MJ/kg, 15-25% moisture. The universal starting fuel. Burns at 700-900°C with natural draft. Adequate for space heating, cooking, brick firing, and small-scale copper/bronze smelting.
- **Softwood**: ~15-17 MJ/kg. Burns faster and produces more creosote in chimneys. Acceptable for heating but less suitable for industrial use.
- **Limitations**: Low energy density per unit mass. High moisture content in green wood reduces effective heat output by 20-40%. Bulk — transporting enough wood for industrial operations requires enormous logistical effort.
- **Wood as industrial fuel**: Used for pottery kilns, brick kilns, lime burning, and copper/bronze smelting. Not adequate for iron smelting (temperature too low without forced draft, and wood's volatiles contaminate the metal).

## Charcoal

Produced by pyrolysis of hardwood in earth-covered pits or simple kilns. The first high-grade fuel for metallurgy:

- **Properties**: Burns at ~1100°C unforced, up to ~1300°C with bellows. Calorific value: ~29 MJ/kg. Nearly pure carbon.
- **Yield**: 20-40% by weight from wood. Energy loss during pyrolysis is significant — roughly half the wood's energy content is lost as volatile gases and tar.
- **Critical role**: Essential for all early iron smelting. The only solid fuel that can sustain the reducing atmosphere and temperature needed for bloomery iron production before coke is available.
- **Production detail**: [Charcoal](charcoal.md)

## Coal

Mined bituminous and anthracite coal. The transition fuel that enables steam power and coke production:

- **Bituminous coal**: 24-35 MJ/kg, widely available, good for steam boilers and coking. Contains 15-30% volatile matter. Burns with long, smoky flame.
- **Anthracite**: 32-36 MJ/kg, highest carbon coal, cleanest burn (very low volatiles), but harder and less common. Burns with short, blue flame. Difficult to ignite but burns very hot once established.
- **Lignite (brown coal)**: 10-20 MJ/kg, high moisture (20-45%), high ash. Lowest rank coal. Burns with heavy smoke. Acceptable for power generation near the mine but poor for transport or metallurgy.
- **Coal mining and selection**: [Coal](coal.md)

## Coke

Distilled from bituminous coal in beehive or by-product ovens. Hard, porous, nearly pure carbon:

- **Properties**: Burns at 1800-2100°C with forced air — the only solid fuel hot enough for blast furnaces and silicon reduction. Calorific value: ~28-31 MJ/kg.
- **By-products**: By-product ovens also yield coal gas, coal tar, ammonia, benzol, and sulfur — each a valuable chemical feedstock.
- **Production detail**: [Coke](coke.md)

## Peat

An intermediate fuel between wood and coal, formed from partially decomposed plant matter in wetlands:

- **Properties**: ~6-14 MJ/kg (air-dried). Burns at lower temperature than coal. High ash content.
- **Use**: Fuel for heating and small boilers where coal is not available. Historically important in Ireland, Scotland, Scandinavia, and Russia.
- **Processing**: Cut from bogs, air-dry 4-8 weeks, stack and further dry. Can be compressed into briquettes for higher density.

## Liquid Fuels

Petroleum distillation yields a spectrum of liquid fuels, each tuned to a boiling range and application. See [Petroleum & Alternative Chemistry](../chemistry/petroleum-alternatives.md) for refining processes.

## Petroleum-Derived Fuels

- **[Gasoline](../glossary/gasoline.md)** (30-150°C fraction): ~46 MJ/kg. Spark-ignition engines, the highest energy-density liquid fuel commonly available. Highly volatile, low flash point (-40°C). Vapors form explosive mixtures with air.
- **[Kerosene](../glossary/kerosene.md)** (150-250°C fraction): ~43-46 MJ/kg. Lamp fuel, heating, jet engine precursor. Higher flash point (37-65°C) — safer to store and handle than gasoline. The first petroleum product widely commercialized (illumination).
- **[Diesel / gas oil](../glossary/dieselgas-oil.md)** (250-350°C fraction): ~45 MJ/kg. Compression-ignition engines, industrial heating. Flash point >52°C. Lubricating and stable.
- **[Fuel oil / residual](../glossary/fuel-oil-residual.md)** (>350°C): ~40-42 MJ/kg. Boiler fuel, large-scale industrial heat. Viscous — may require preheating for atomization in burners.

## Bio-Derived Liquid Fuels

- **[Ethanol](../glossary/ethanol.md)** (C₂H₅OH): ~26 MJ/kg. Fermented from grain, sugar, or starch feedstocks and distilled to 95%+ purity. Burns cleanly in lamps, stoves, and modified engines. Independent of petroleum — producible from agriculture alone. Production: [Fermentation Chemistry](../chemistry/petroleum-alternatives.md).
- **[Methanol](../glossary/methanol.md)** (CH₃OH): ~20 MJ/kg. Obtained from wood pyrolysis (low yield, ~1-2%) or synthesized from CO + H₂ over catalyst. Solvent and fuel extender. Highly toxic if ingested — causes blindness.
- **Vegetable oil**: ~37-40 MJ/kg. Pressed from oil seeds (rapeseed, sunflower, palm). Can be used directly in diesel engines (with preheating and filtration) or transesterified to biodiesel. Also used for lamps in the absence of kerosene.

## Liquid Fuel Comparison

| Fuel | Energy Density | Flash Point | Auto-Ignition | Primary Engine |
|------|---------------|-------------|---------------|----------------|
| Gasoline | ~46 MJ/kg | -40°C | ~280°C | Spark-ignition |
| Kerosene | ~43-46 MJ/kg | 37-65°C | ~210°C | Jet turbine |
| Diesel | ~45 MJ/kg | >52°C | ~250°C | Compression-ignition |
| Ethanol | ~26 MJ/kg | 13°C | ~365°C | Modified spark-ignition |
| Vegetable oil | ~37-40 MJ/kg | ~315°C | — | Modified diesel |
| Fuel oil (heavy) | ~40-42 MJ/kg | >65°C | — | Boiler |

## Gaseous Fuels

## Producer Gas / Wood Gas

- **Composition**: CO + H₂ + N₂. Approximate: ~25% CO, ~10% H₂, ~60% N₂, ~5% CO₂.
- **Energy density**: ~5-6 MJ/m³ (low — about 1/6 of natural gas). Bulkier per unit energy than any other fuel.
- **Generation**: Pass limited air through a hot bed of charcoal or coke. The partial combustion produces CO (carbon monoxide, combustible). Add steam to the air blast to increase H₂ yield (water-gas reaction: C + H₂O → CO + H₂).
- **Engine use**: Can fuel internal combustion engines and furnaces directly. Powered vehicles during WWII petroleum shortages (wood gas generators on cars and trucks). Must be scrubbed of tars and particulates before engine use — tar deposits destroy engine valves and cylinders.
- **Advantage**: Producible from any solid carbon fuel (charcoal, coke, coal, even wood). Independent of petroleum or natural gas.

## Coal Gas

- **Source**: From coke ovens (by-product of coke production).
- **Composition**: ~50-60% H₂, 20-30% CH₄, 5-8% CO, balance N₂ and CO₂.
- **Energy density**: ~18 MJ/m³ (richer than producer gas due to high H₂ and CH₄ content).
- **Uses**: Coke oven heating, steelworks furnaces, town gas (lighting and heating). Must be cooled and scrubbed of tar and naphthalene before distribution.

## Natural Gas

- **Composition**: Primarily methane (CH₄), with minor ethane, propane, and butane.
- **Energy density**: ~35-40 MJ/m³ (highest of common gaseous fuels).
- **Requires**: Gas well drilling and pipeline infrastructure. Not available in the early bootstrap. When available, it is the most convenient and cleanest-burning gaseous fuel.

## Calorific Value Comparison

| Fuel | Form | Energy Density | Flame Temp (forced air) | Key Use |
|------|------|---------------|------------------------|---------|
| Peat (air-dried) | Solid | ~6-14 MJ/kg | ~500-700°C | Heating, small boilers |
| Wood (seasoned hardwood) | Solid | ~16-18 MJ/kg | ~700-900°C | Heating, early smelting |
| Charcoal | Solid | ~29 MJ/kg | ~1100-1300°C | Iron smelting, forging |
| Bituminous coal | Solid | ~24-35 MJ/kg | ~1200-1400°C | Steam boilers, coking |
| Anthracite | Solid | ~32-36 MJ/kg | ~1400-1600°C | Clean heating, smithing |
| Coke | Solid | ~28-31 MJ/kg | ~1800-2100°C | Blast furnaces, silicon |
| Ethanol | Liquid | ~26 MJ/kg | ~900°C | Lamps, stoves, engines |
| Methanol | Liquid | ~20 MJ/kg | ~800°C | Solvent, fuel extender |
| Gasoline | Liquid | ~46 MJ/kg | ~1900°C (in engine) | Spark-ignition engines |
| Kerosene | Liquid | ~43-46 MJ/kg | ~1800°C (in engine) | Lamps, jets, heating |
| Diesel | Liquid | ~45 MJ/kg | ~1800°C (in engine) | Compression-ignition engines |
| Fuel oil (heavy) | Liquid | ~40-42 MJ/kg | ~1700°C | Boilers, industrial heat |
| Producer gas | Gas | ~5-6 MJ/m³ | ~800-1000°C | Engines, furnace heat |
| Coal gas | Gas | ~18 MJ/m³ | ~1800°C | Lighting, oven fuel |
| Natural gas | Gas | ~35-40 MJ/m³ | ~1900°C | Heating, electricity |

## Fuel Selection by Application

| Application | Best Fuel | Acceptable Alternative |
|-------------|-----------|----------------------|
| Forge / smithing | Charcoal or coal | Coke (overkill for small forge) |
| Blast furnace iron | Coke (required) | Charcoal (early, lower output) |
| Silicon reduction | Coke (required) | None — needs >1800°C |
| Steam boiler | Bituminous coal | Fuel oil, wood, coke breeze |
| Spark-ignition engine | Gasoline | Ethanol (modified carb), producer gas |
| Diesel engine | Diesel | Vegetable oil (filtered), fuel oil |
| Lamp / lighting | Kerosene | Ethanol, coal gas, vegetable oil |
| Furnace heating | Producer gas, fuel oil | Coal, charcoal |
| Ceramics / brick kiln | Coal, charcoal | Wood, producer gas |
| Lime burning | Wood, charcoal | Coal, coke |
| Domestic heating | Wood, coal | Peat, charcoal |

## Progression Logic

The fuel chain is a dependency chain, and each fuel unlocks higher temperatures and cleaner combustion:

1. **[Wood](../glossary/wood.md)** → heating, cooking, pottery (600-900°C)
2. **[Charcoal](../glossary/charcoal.md)** → copper/bronze smelting, iron smelting (1100-1300°C)
3. **[Coal](../glossary/coal.md)** → steam boilers, coking feedstock (1200-1400°C)
4. **[Coke](../glossary/coke.md)** → blast furnace iron, silicon reduction (1800-2100°C)
5. **[Petroleum fractions](../glossary/petroleum-fractions.md)** → internal combustion engines, high-energy-density transport
6. **[Synthetic gases](../glossary/synthetic-gases.md)** → chemical feedstock, flexible fuel supply

The bootstrap cannot skip steps. Each fuel requires the infrastructure of the previous stage: you need kilns to make charcoal before you can smelt iron; you need iron tools to mine coal before you can make coke; you need coke-fired furnaces before you can reduce silicon.

## See Also

- [Charcoal Production](charcoal.md) — pyrolysis of wood to charcoal
- [Coal Mining & Selection](coal.md) — bituminous and anthracite coal
- [Coke Production](coke.md) — coking ovens and by-products
- [Steam Power](steam-power.md) — major coal consumer for boilers
- [Internal Combustion Engine](engine.md) — gasoline, diesel, and gas engines
- [Petroleum Alternatives](../chemistry/petroleum-alternatives.md) — refining, distillation, synthetic fuels
- [Mining: Extraction](../mining/extraction.md) — coal and petroleum drilling
- [Iron & Steel](../metals/iron-steel.md) — smelting fuel requirements
- [Steelmaking](../metals/steelmaking.md) — coke for blast furnaces
- [Ceramics: Kiln Firing](../ceramics/kiln-firing.md) — kiln fuel requirements
- [Glass: Basic](../glass/basic.md) — glass melting fuel requirements
- [Machine Tools: Casting](../machine-tools/casting.md) — foundry fuel requirements
- [Transport](../transport/index.md) — fuel for vehicles and railways

## Safety & Hazards

- **Flammability and explosion**: All liquid and gaseous fuels form explosive mixtures with air. Gasoline vapor ignites at 1.4-7.6% concentration. Natural gas (methane) at 5-15%. Never store fuels near ignition sources. Use in well-ventilated areas. Bond and ground containers during transfer to prevent static discharge ignition.
- **Carbon monoxide (CO)**: Incomplete combustion of any carbon fuel produces CO — odorless, colorless, lethal at 400 ppm sustained concentration. Symptoms: headache (mild), nausea and dizziness (moderate), unconsciousness and death (severe). Never burn fuels in enclosed spaces without ventilation. CO detectors where fuel-burning equipment operates.
- **Fuel storage**: Store liquid fuels in approved containers away from heat and ignition sources. Gasoline and light fractions have very low flash points — vapors ignite from distant sparks. Store gaseous fuels in pressure-rated cylinders with pressure relief valves. Separate fuel storage from oxidizer storage (never store fuels and oxidizers together).
- **Wood/coal dust**: Suspended dust at sufficient concentration (>20-60 g/m³ for coal dust) is explosive. Ventilation in fuel storage and handling areas. No smoking, open flames, or spark sources in dusty environments. Wet down coal piles to suppress dust.

## Troubleshooting — Fuel Production and Combustion Problems

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Charcoal is mostly ash (over-burned) | Too much air entered the kiln; burning instead of pyrolysis; opened too late | Seal all cracks in earth covering immediately when smoke appears; reduce vent hole size; monitor color of smoke (gray/white = pyrolysis OK, clear = combustion — seal vents) |
| Charcoal contains uncarbonized wood centers | Insufficient burn time; kiln too large for fuel load; uneven heat distribution | Extend burn time 2-4 hours; ensure tight stacking with vertical channels for heat flow; add more kindling at center for even ignition |
| Coal fire keeps going out in boiler | Coal too fine (fines block airflow); wet coal; insufficient draft | Screen coal to remove fines below 10 mm; use dry coal (<8% moisture); check chimney draft and open dampers; increase undergrate air supply |
| Blast furnace coke too weak (crumbling under burden) | Coke oven temperature too low; insufficient coking time; wrong coal blend | Increase oven temperature to 1000-1100°C; extend coking time to 16-18 hours; test coal blend — need >25% volatile matter for proper coking |
| Wood gas engine losing power | Tar buildup in gasifier or filters; wet wood (high moisture); gas too hot entering engine | Clean gasifier and replace filter media; use dry wood below 20% moisture; check cooling radiator — gas must be below 40°C before engine intake |
| Diesel engine knocking on vegetable oil | Oil too viscous (cold); poor atomization; carbon buildup on injectors | Preheat oil to 70-90°C before injection; install secondary fuel filter (5 μm); blend with 20-30% petroleum diesel for cold starts |
| Gasoline engine flooding (won't start) | Carburetor float stuck; choke left on too long; fuel vapor lock in hot weather | Tap carburetor bowl to free float; turn off choke and crank with throttle wide open; cool fuel line with wet rag to relieve vapor lock |
| Kerosene lamp smoking | Wick too high; impure kerosene; insufficient air at flame | Trim wick to 5-8 mm above burner; use filtered kerosene; clean burner air vents; do not use diesel or fuel oil in kerosene lamps |
| Producer gas has low heating value | Too much air (combustion instead of gasification); charcoal bed too shallow; gasifier overheating | Reduce air intake (close primary air valve slightly); increase fuel bed depth to >30 cm; add steam to air blast for water-gas reaction |
| Fuel oil won't atomize in burner | Oil too viscous (cold); preheater failure; nozzle clogged with sediment | Preheat oil to 80-100°C for heavy fuel oil; clean or replace burner nozzle; filter oil through 100-mesh screen before storage tank |

## Fuel Energy Density Comparison

Energy density determines how much energy a given mass or volume of fuel delivers. This affects storage, transport, and engine design throughout the bootstrap:

| Fuel | Energy Density | Form | Notes |
|------|---------------|------|-------|
| Wood (seasoned hardwood) | 15-20 MJ/kg | Solid | Baseline fuel, widely available |
| Charcoal | 28-33 MJ/kg | Solid | Nearly pure carbon, low ash |
| Bituminous coal | 24-35 MJ/kg | Solid | Variable by rank and ash content |
| Coke | 28-31 MJ/kg | Solid | Hard, porous, high-temperature fuel |
| Fuel oil (heavy) | 40-45 MJ/kg | Liquid | Residual petroleum fraction |
| Natural gas | 38-50 MJ/m³ | Gas | Highest energy density gaseous fuel |
| Hydrogen | 120 MJ/kg | Gas | By mass; only 3 MJ/m³ by volume at STP |

Cost per delivered MJ depends on production method, transport distance, and conversion efficiency. A rough comparison at early bootstrap costs: wood at 15 MJ/kg and local sourcing delivers energy at the lowest cost per MJ despite its lower energy density, because no processing is required. Coke at 28-31 MJ/kg costs more per MJ when the capital cost of coke ovens is amortized, but enables processes (blast furnaces, silicon reduction) that no amount of cheap wood can achieve.

## Wood Gas as Petroleum Substitute

Producer gas (wood gas) enables internal combustion engines to run without liquid petroleum. Gasification of 1 kg of dry wood yields approximately 2.5 m³ of producer gas at 5-6 MJ/m³, for a total of 12.5-15 MJ of gaseous fuel per kg of wood input. This is less than the 15-18 MJ/kg available from direct combustion, because gasification is inherently a partial combustion process.

A wood gas generator consists of a fuel hopper, a reaction chamber (fire tube) where limited air passes through a hot charcoal bed, a crude cleaning section (cyclone separator and fabric filter for tar and particulate removal), and a cooling radiator to bring the gas below 40°C before it enters the engine intake. The gas must be scrubbed below 50 mg/m³ tar content to protect engine valves and cylinder walls. Typical wood consumption: 1-1.5 kg of wood per kWh of electricity generated via gas engine.

Wood gas was used extensively during WWII petroleum shortages. Sweden operated over 70,000 wood gas vehicles. The technology requires dry wood (below 20% moisture) and regular maintenance (ash removal, filter cleaning every 8-12 hours of operation), but needs no petroleum infrastructure whatsoever.

## Vegetable Oil as Diesel Substitute

Straight vegetable oil (SVO) can run in modified diesel engines, but its high viscosity (30-40 cSt at 40°C vs. 2-4 cSt for diesel fuel) causes poor atomization, carbon buildup on injectors, and ring sticking. Preheating SVO to 70-90°C reduces viscosity to near-diesel levels, enabling short-term operation in unmodified engines.

Transesterification produces biodiesel with properties much closer to petroleum diesel. The reaction uses 1 kg of vegetable oil (triglyceride), 100-200 g of methanol (6:1 molar ratio, excess drives reaction to completion), and 3-8 g of sodium hydroxide (NaOH) or potassium hydroxide (KOH) as catalyst. The reaction proceeds at 50-65°C for 1-3 hours with continuous stirring. Products separate into two layers: biodiesel (methyl esters, upper layer, ~95% yield) and glycerol (lower layer, byproduct with value as a chemical feedstock). Biodiesel cetane number: 48-65 (vs. 40-55 for petroleum diesel). Viscosity: 4-5 cSt at 40°C (close to diesel). Energy density: 37-40 MJ/kg (about 8-10% lower than petroleum diesel). Biodiesel can be blended with petroleum diesel at any ratio or used neat (B100) in compatible engines.



[← Back to Energy](index.md)
