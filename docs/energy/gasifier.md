# Biomass Gasifier

> **Node ID**: energy.biomass-energy.gasifier
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.biomass-energy`](biomass-energy.md), [`metals.iron-steel`](../metals/iron-steel.md), [`ceramics.kilns`](../ceramics/kilns.md)
> **Enables**: [`energy.electricity`](electricity.md), [`energy.engine`](engine.md)
> **Timeline**: Years 10-25
> **Outputs**: producer_gas, wood_gas
> **Critical**: No — gasifiers enable engine-grade fuel from solid biomass, but diesel or gasoline engines can use petroleum fuels directly

## Overview

A biomass gasifier converts solid fuel (wood chips, charcoal, agricultural residues) into a combustible gas (producer gas or wood gas) through partial combustion in a restricted-air environment. The gasifier is a vertical shaft reactor with four distinct thermal zones stacked top to bottom: **drying** (50-150°C, moisture evaporates), **pyrolysis** (200-600°C, volatile matter released), **combustion** (800-1200°C, partial oxidation provides heat), and **reduction** (700-1000°C, CO₂ and H₂O are reduced by hot char to CO and H₂).

The key reduction reactions are: CO₂ + C → 2CO (Boudouard reaction, endothermic) and H₂O + C → CO + H₂ (water-gas reaction, endothermic). The heat for these endothermic reactions comes from the exothermic combustion zone above. The product gas composition is approximately: 18-25% CO, 12-20% H₂, 2-4% CH₄, 8-12% CO₂, 50-55% N₂. Heating value: 4.5-6.0 MJ/m³ (wood chips) — about one-sixth that of natural gas.

The downdraft (Imbert) design forces all gas through a constricted throat at the hottest part of the reactor, cracking tars into lighter gases. This produces cleaner gas suitable for internal combustion engines, unlike updraft designs that produce tar-laden gas only fit for direct combustion. Gasifiers become available once basic steel fabrication ([Iron & Steel](../metals/iron-steel.md)) and [refractory](../ceramics/kilns.md) construction are established — typically years before petroleum refining, making them the primary route to engine-grade gaseous fuel in the bootstrap sequence. Cross-reference: [Charcoal Production](charcoal.md) for charcoal feedstock; [Heat Engines](engine.md) for engine modifications to burn producer gas.

## Prerequisites

- [Steel plate and pipe](../metals/iron-steel.md) — for gasifier body, air nozzles, gas outlet
- [Firebrick or castable refractory](../ceramics/kilns.md) — for combustion zone lining
- [Welding capability](../machine-tools/joining.md) — for gasifier fabrication
- [Dry biomass fuel](biomass-energy.md) — wood chips (20-80 mm, <20% moisture) or charcoal (10-40 mm)
- [Engine-generator](engine.md) — to consume the producer gas

## Bill of Materials

### Downdraft Gasifier (Imbert type, 10-50 kW engine output)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate (body)](../metals/iron-steel.md) | 150-300 kg | 6-10 mm thick, A36 or equivalent | [Iron & Steel](../metals/iron-steel.md) | Used propane tank (limited size) |
| [Firebrick](../ceramics/kilns.md) | 30-60 pcs | 230 × 115 × 65 mm, rated to 1200°C | [Ceramics](../ceramics/kilns.md) | Castable refractory (easier to form) |
| [Steel pipe (air nozzles)](../metals/iron-steel.md) | 3-5 m | 50 mm OD, standard wall | [Iron & Steel](../metals/iron-steel.md) | Stainless steel (longer life) |
| [Steel grate bars](../metals/iron-steel.md) | 1 unit | 15 mm square bars at 20 mm spacing | [Iron & Steel](../metals/iron-steel.md) | Cast iron grate |
| [Steel plate (cyclone separator)](../metals/iron-steel.md) | 10-20 kg | 1.5-3 mm sheet steel | [Iron & Steel](../metals/iron-steel.md) | Fabric filter (higher pressure drop) |
| [200 liter drum (sawdust filter)](../metals/index.md) | 1 unit | Steel drum with inlet/outlet fittings | [Metals](../metals/index.md) | Cloth bag filter |
| [Steel pipe (gas outlet)](../metals/iron-steel.md) | 3-5 m | 50 mm OD, finned for cooling | [Iron & Steel](../metals/iron-steel.md) | Plain pipe in water bath |
| [Blower or suction fan](steam-power.md) | 1 unit | Induced-draft, 100-500 m³/hour | [Energy](./index.md) | Engine suction (natural draft) |
| [Welding consumables](../machine-tools/joining.md) | 5-10 kg | E6013 or E7018 electrodes | [Joining](../machine-tools/joining.md) | Bolted flanges |

## Process Description

1. **Fabricate the gasifier body**: Roll 6-10 mm steel plate into a cylindrical shell, 300-600 mm diameter (matching engine power). Weld the longitudinal seam. Weld a flat bottom plate. The shell height is 1.0-1.5 m. For the Imbert design, include a conical throat restriction (constriction ring) at the combustion zone — throat diameter is 60-75% of the body diameter.

2. **Line the combustion zone** with firebrick from the air nozzle level down through the reduction zone. The lining reduces heat loss from the hottest zone (800-1200°C) and protects the steel shell from oxidation. Mortar firebrick with refractory cement. Leave the upper portion (drying and pyrolysis zones) unlined — the steel shell acts as a heat exchanger, preheating incoming fuel.

3. **Install air nozzles (tuyeres)**: Weld 4-8 steel pipe nozzles (50 mm OD) through the shell wall at the throat level, pointing inward and slightly downward. Each nozzle has a removable cap for cleaning. The total nozzle area determines the maximum gas throughput — undersized nozzles restrict output, oversized nozzles cause channeling. Calculate nozzle area: approximately 5-10 cm² per 10 kW of engine output.

4. **Install the grate** at the bottom of the reduction zone. A grid of 15 mm square steel bars at 20 mm spacing supports the fuel bed while allowing ash to fall through. Make the grate removable for cleaning and ash removal.

5. **Build the fuel hopper**: Weld a conical steel top section (2-3 mm plate) above the main body. The hopper holds enough fuel for 1-4 hours of operation. Install a tight-fitting lid with a gasket seal — the gasifier operates under slight negative pressure (induced draft), and an unsealed hopper lid allows air ingress that dilutes the gas and creates explosion risk.

6. **Fabricate the cyclone separator**: Build a cylindrical sheet-metal vessel (200-400 mm diameter, 400-600 mm tall) with a tangential gas inlet near the top, a clean gas outlet at the top center, and a dust collection pot at the bottom. The cyclone removes >90% of particles larger than 10 μm by centrifugal force.

7. **Build the gas cooling and cleaning train**: Route the raw gas (exiting at 400-600°C) through a finned cooling pipe (reduce to <30°C — cooler gas is denser, improves engine volumetric efficiency). Then pass through a sawdust filter (200 liter drum filled with 100-200 mm of dry sawdust) for final tar and particulate removal. Target: <50 mg/m³ tar content for engine operation.

The cooling and cleaning train is the most labor-intensive part of gasifier operation. Raw gas from a downdraft wood gasifier contains 100-500 mg/m³ of tars even after throat cracking. The cooling pipe condenses heavy tars and water, which collect in the condensate trap. The sawdust filter captures remaining light tars and particulates. Sawdust filter media must be replaced every 20-50 operating hours (depending on tar load) — the spent sawdust is saturated with tars and should be burned as fuel in the gasifier startup phase.

8. **Install the blower**: Connect an induced-draft blower on the gas outlet side (downstream of the gasifier, upstream of the engine). The blower pulls air through the fuel bed, maintaining negative pressure in the gasifier. For engine-coupled operation, engine suction alone provides draft — the blower is needed only for starting.

9. **Install an ignition port** in the combustion zone — a 50 mm diameter opening with a threaded plug, used for lighting the kindling during startup.

10. **Pressure-test the entire system**: Seal all openings, pressurize to 0.3 bar with compressed air. Apply soapy water to every weld, fitting, and gasket joint. Zero bubbles acceptable — any air leak in operation admits excess air, reducing gas quality and creating explosion hazard.

11. **Install a condensate trap** at the lowest point of the cooling pipe: a small steel vessel (100-200 mm diameter × 150 mm tall) with a drain valve at the bottom and gas inlet/outlet near the top. Condensate (water, tars, and creosote) collects here rather than flowing into the sawdust filter or engine. Drain daily during operation.

## Calibration and Verification

1. **Gas quality test (flare test)**: After lighting and reaching steady operation (10-20 minutes), open the gas outlet to a flare nozzle. Producer gas should burn with a stable blue-yellow flame. Sooty orange flame indicates excessive tars — improve throat design or add secondary air injection.

2. **Tar content measurement**: Pass a known volume of gas through a filter, weigh the deposit. Target: <50 mg/m³ for engine use. Above 100 mg/m³ — engine fouls within hours. Solutions: increase throat temperature, improve cooling, add secondary air.

3. **Gas composition**: Sample gas with an Orsat analyzer or gas chromatograph. Target: 18-25% CO, 12-20% H₂, 2-4% CH₄. Low CO indicates insufficient reduction zone temperature — the char bed may be too short.

4. **Cold gas efficiency**: Measure energy in product gas vs. energy in fuel input. Target: 65-75% for wood chips, 70-80% for charcoal. Low efficiency indicates excessive heat loss or incomplete reduction.

5. **Temperature profile**: Measure temperature at the combustion zone (target: 800-1200°C), reduction zone outlet (target: 600-800°C), and gas outlet (target: 400-600°C before cooling). Low combustion zone temperature indicates insufficient draft or wet fuel.

## Quantitative Parameters

| Parameter | Value |
|-----------|-------|
| Gas heating value (wood chips) | 4.5-6.0 MJ/m³ |
| Gas heating value (charcoal) | 4.0-5.5 MJ/m³ |
| Cold gas efficiency | 65-75% (wood), 70-80% (charcoal) |
| Fuel consumption | 1.0-1.5 kg wood chips per kWh electrical |
| Tar content after cleaning | <50 mg/m³ |
| Engine power derating | 40-60% of gasoline rating |
| Gasifier throughput | 15-50 kg fuel/hour (10-50 kW systems) |
| Fuel moisture limit | <20% (wood), <5% (charcoal) |
| Start-up time | 10-20 minutes |
| Continuous run time | 2-8 hours per fuel loading |

## Strengths

- Converts locally available solid biomass into engine-grade gaseous fuel — no petroleum required
- Works with wood chips, charcoal, agricultural residues, nut shells, briquettes
- Charcoal gasification produces very clean gas (<50 mg/m³ tar)
- Can power existing internal combustion engines with intake modification (gas-air mixer replaces carburetor)
- Proven technology — widely used during WWII fuel shortages

## Weaknesses

- Wood gasification produces high tar loads (500-5000 mg/m³ raw) requiring extensive cleaning
- Engine power derated to 40-60% of gasoline rating due to low gas energy density
- Requires consistent fuel moisture (<20%) — wet fuel causes tar spikes and unstable operation
- Gas cannot be stored at pressure — must be consumed immediately or flared
- Gasifier requires regular ash removal and periodic throat cleaning (every 4-8 hours)

## Gasifier Design Comparison

| Design | Gas Flow | Tar Content (raw) | Best Fuel | Complexity | Best Application |
|--------|----------|--------------------|-----------|------------|------------------|
| Updraft (countercurrent) | Upward through bed | High (5,000-10,000 mg/m³) | Dry biomass, <30% moisture | Low | Direct combustion (furnace, kiln) — tar makes it unsuitable for engines |
| Downdraft (Imbert) | Downward through throat | Low (50-500 mg/m³) | Wood chips, charcoal, 10-40 mm | Medium | Engine fuel — tar cracked in hot throat zone |
| Cross-draft | Horizontal | Medium (1,000-3,000 mg/m³) | Charcoal only | Low | Small engines, vehicle gasifiers (WWII era) |
| Fluidized bed | Upward, bubbling air | Medium (500-2,000 mg/m³) | Any biomass, 0-50 mm particle size | High | Medium-scale power generation (100 kW - 5 MW) |
| Entrained flow | Co-flow with oxygen | Very low (<50 mg/m³) | Pulverized coal or biomass | Very high | Large-scale syngas production for chemical synthesis |

The downdraft Imbert design is the most practical for engine fuel because the gas passes through the hottest combustion zone (800-1200°C) where tars are thermally cracked into CO and H₂. Updraft gasifiers are simpler to build but produce tar-laden gas only suitable for direct combustion in furnaces and kilns.

### Updraft Gasifier

In an updraft gasifier, air enters at the bottom and moves upward through the fuel bed, counter to the downward fuel movement. The combustion zone is at the bottom, with reduction, pyrolysis, and drying zones stacked above. Product gas exits at the top at 200-400°C — cool enough that tars condense in the gas. This tar contamination makes updraft gas unsuitable for engines but acceptable for direct combustion where tars burn in the furnace. Advantages: high thermal efficiency (80-90% cold gas), tolerant of fuel moisture up to 30%, and simple construction (no throat restriction). Build an updraft gasifier for furnace and kiln fuel; build a downdraft for engine fuel.

### Fluidized Bed Gasifier

Air is blown upward through a bed of sand or ash at sufficient velocity (0.5-2.0 m/s) to suspend the particles in a turbulent, fluid-like state. Biomass fuel (0-50 mm particle size) is fed into this bed where it mixes rapidly with hot sand, achieving uniform temperature (700-900°C) and fast reaction rates. Advantages: handles diverse and variable fuels, excellent temperature control, scalable to multi-MW. Disadvantages: requires a forced-draft blower of significant capacity, bed material (sand) carries over into the gas requiring cyclone cleanup, and the system is more complex to start and control. Suitable for community-scale power (100 kW-5 MW) where fuel consistency is a problem.

### Engine Conversion for Producer Gas

Internal combustion engines require modification to run on producer gas. The gas has lower energy density than gasoline (4-6 MJ/m³ vs. 3.5 MJ/m³ for gasoline vapor at stoichiometric mixture), so the engine produces 40-60% of its gasoline-rated power. Key modifications: replace the carburetor with a gas-air mixer valve (a simple T-fitting with adjustable air and gas throttles), advance ignition timing by 10-15° (producer gas burns slower than gasoline), and install a second throttle body for gas-air mixture control. Diesel engines can be converted to dual-fuel operation: producer gas replaces 60-80% of the diesel fuel, with a pilot injection of diesel to initiate combustion. See [Heat Engines](engine.md) for detailed conversion procedures.

## Gas Composition by Fuel Type

| Component | Wood Chips (downdraft) | Charcoal (downdraft) | Wood Pellets (updraft) |
|-----------|----------------------|---------------------|----------------------|
| CO | 18-25% | 28-32% | 15-22% |
| H₂ | 12-20% | 8-15% | 10-18% |
| CH₄ | 2-4% | 1-3% | 3-5% |
| CO₂ | 8-12% | 3-6% | 8-14% |
| N₂ | 50-55% | 50-60% | 45-55% |
| Heating value | 4.5-6.0 MJ/m³ | 4.0-5.5 MJ/m³ | 5.0-6.5 MJ/m³ |
| Tar (raw) | 100-500 mg/m³ | <50 mg/m³ | 2,000-8,000 mg/m³ |

Charcoal gasification produces the cleanest gas (virtually no tars) because all volatile matter has already been driven off during charcoal production. The trade-off: charcoal requires an extra processing step (see [Charcoal Production](charcoal.md)), reducing overall system efficiency. For bootstrap contexts where tar management is difficult, charcoal-fed gasifiers are strongly preferred despite the additional processing — the elimination of tar-related engine fouling and filter maintenance outweighs the energy cost of charcoal production.

## Scaling Notes

| Scale | Fuel Input | Gas Output | Engine Power | Typical Design | Application |
|-------|-----------|------------|-------------|----------------|-------------|
| Small (5-10 kW) | 3-8 kg/h | 8-20 m³/h | 3-8 kW engine | Imbert downdraft, 200-300 mm throat | Farm machinery, small generator |
| Medium (20-50 kW) | 15-40 kg/h | 40-100 m³/h | 15-40 kW engine | Imbert downdraft, 300-500 mm throat | Workshop power, irrigation pump |
| Large (100-500 kW) | 60-300 kg/h | 150-800 m³/h | 80-400 kW engine | Fluidized bed or large Imbert | Village electrification, sawmill |
| Industrial (1-5 MW) | 500-3000 kg/h | 1300-8000 m³/h | 0.8-4 MW engine/turbine | Circulating fluidized bed | District power, industrial CHP |

Gasifier throughput scales approximately with throat area (for downdraft) or bed cross-section (for fluidized bed). A downdraft gasifier with a 300 mm throat diameter processes ~15-25 kg/h of wood chips. To double throughput, increase throat diameter to ~425 mm (area doubles). Multiple gasifiers can feed a single engine through a common gas manifold — this is often simpler than building one very large gasifier.

Minimum economic scale: an Imbert downdraft gasifier with 200 mm throat diameter, consuming 3-8 kg/h wood chips, powering a 3-8 kW engine-generator. Below this, the labor of fuel preparation and gasifier operation exceeds the value of electricity produced. A single operator can manage a gasifier up to ~50 kW output; larger systems require a dedicated fuel preparation and feeding system.

Gasifier-engine systems require more daily maintenance than diesel generators: grate cleaning every 4-8 hours, sawdust filter replacement every 20-50 operating hours, and ash disposal every 8-12 hours. This labor burden makes gasifiers most economical where fuel is free (sawmill waste, forest residues) and labor is inexpensive.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Gas will not ignite | Combustion zone not hot enough | Run the blower for 5-10 more minutes to raise throat temperature; check that fuel is dry (<20% moisture); add charcoal to the combustion zone for faster startup |
| Gas ignites but flame is orange/sooty | High tar content in gas | Check throat temperature (must be >800°C); increase air flow to raise temperature; verify fuel is not oversized (>80 mm blocks the throat); ensure throat constriction is not eroded |
| Engine runs rough or loses power | Tar fouling in engine intake | Clean gas filter and cooling train; replace sawdust filter media; check that gas temperature entering engine is <30°C (hot gas is less dense, reducing engine volumetric efficiency) |
| Gasifier burns too fast (high fuel consumption) | Excessive air flow through nozzles | Reduce blower speed or partially close air nozzle caps; recalculate nozzle area for engine displacement |
| Channeling (gas finds path through fuel without proper reaction) | Uneven fuel size or bridging | Use uniform fuel size (20-60 mm for wood chips); stir the fuel bed from the top periodically to break bridges; install a mechanical agitator for continuous operation |
| Excessive ash buildup blocking grate | High-ash fuel (agricultural residues) | Clean grate every 2-4 hours (install a shaking grate mechanism); blend high-ash fuel with wood to reduce ash fraction; consider switching to charcoal for low-ash operation |
| Gasifier extinguishes during operation | Fuel hopper empty or bridged | Install a visual fuel level indicator; stir the hopper to break bridges; never let the fuel level drop below the top of the pyrolysis zone |
| Condensate in gas line (water dripping from filter) | Wet fuel (>20% moisture) | Pre-dry fuel to <20% moisture; install a condensate trap with drain valve at the low point of the cooling pipe |
| Gasifier refractory cracking | Thermal cycling stress on firebrick lining | Replace cracked bricks; use castable refractory with better thermal shock resistance for future relining; limit temperature cycling by maintaining a low fire during idle periods rather than full cooldown and restart |
| Excessive smoke from gasifier during startup | Incomplete combustion during cold-start phase | Normal during first 5-10 minutes; continue running the blower until combustion zone reaches >600°C (gas flare burns clean). If smoke persists after 15 minutes, check that air nozzles are not blocked and fuel is dry |

## Quality Control

- **Gas flare test**: At every startup, route gas to a flare nozzle. A clean blue-yellow flame with no smoke indicates acceptable tar levels. Orange, smoky flame — do not route gas to engine; continue running the gasifier at higher temperature or check fuel quality.
- **Tar content**: Periodically pass a measured gas volume through a glass fiber filter. Weigh the filter before and after. Target: <50 mg/m³ for engine operation. Above 100 mg/m³ — engine will foul within 10-50 hours. This test requires a gas pump and precision balance but should be performed weekly during continuous operation.
- **Gas temperature**: Install thermocouples at the combustion zone (target: 800-1200°C) and gas outlet before cooling (target: 400-600°C). Low combustion zone temperature is the primary cause of high tar gas. Log temperatures during each operating session.
- **Fuel moisture**: Test each batch of fuel with a moisture meter or by oven-drying a 100 g sample at 105°C for 24 hours. Moisture = (initial weight - dry weight) / initial weight × 100%. Maximum acceptable: 20% for wood chips, 5% for charcoal. Wet fuel produces steam in the combustion zone, lowering temperature and increasing tar production.
- **Fuel size grading**: Pass fuel through mesh screens. Acceptable range: 20-60 mm for downdraft gasifiers (below 20 mm blocks airflow; above 60 mm causes channeling and bridging). Reject oversized pieces (re-chip) and undersized (reserve for briquetting or direct combustion).
- **Cold gas efficiency**: Measure fuel energy input (fuel mass × HHV) vs. gas energy output (gas volume × gas heating value). Target: 65-75% for wood chips, 70-80% for charcoal. Low efficiency indicates excessive heat loss (poor insulation) or incomplete reduction (short char bed).

## Safety

- **Carbon monoxide poisoning**: Producer gas contains 18-32% CO — lethal at 0.1% (1000 ppm) in air for 1 hour. Operate gasifiers outdoors or in well-ventilated areas. Install CO detectors in any enclosed space where gas piping runs. CO is odorless — you cannot smell it. Symptoms of CO poisoning: headache, dizziness, nausea, confusion. Evacuate immediately if anyone shows symptoms.
- **Gas explosion**: Producer gas is flammable at 15-70% concentration in air. Gas leaks into enclosed spaces create explosion risk. Install a flame arrestor (water seal or fine mesh screen) on the gas line between gasifier and engine. Pressure-test the entire gas system before each operating period. Never operate a gasifier with a known gas leak.
- **Flashback**: Never open the fuel hopper lid while the gasifier is running — flashback can ignite fuel in the hopper. Install a double-lid interlock or water seal. If the hopper must be opened, shut down the blower and wait 2 minutes for gas flow to stop.
- **High temperature**: Gasifier combustion zone reaches 1000-1200°C. Outer shell may reach 200-400°C without insulation. Install firebrick lining in the combustion zone and a metal guard around the shell. Wear heat-resistant gloves (leather, minimum) when operating valves, cleaning the grate, or handling ash.
- **Ash disposal**: Hot ash can reignite. Cool ash in a metal container with a lid before disposal. Do not dump hot ash near combustible materials.
- **Engine damage from tar**: If gas cleaning is inadequate, tar deposits build up on engine valves, piston rings, and intake manifolds. This causes progressive power loss and eventual engine seizure. Monitor engine oil for tar contamination (oil becomes thick and dark). Change oil every 100-200 operating hours when running on producer gas, versus 250-500 hours for gasoline operation.

## References

- [Biomass Energy](biomass-energy.md) — full coverage of biomass conversion pathways, biogas, and direct combustion
- [Heat Engines](engine.md) — internal combustion engines modified for producer gas fuel
- [Electricity Generation](electricity.md) — engine-generator sets
- [Charcoal Production](charcoal.md) — charcoal as premium gasifier fuel
- [Ceramics](../ceramics/kilns.md) — firebrick for combustion zone lining
- [Iron & Steel](../metals/iron-steel.md) — steel plate and pipe for gasifier construction
- [Fuels](fuels.md) — comparative fuel properties and energy densities
- [Wood Gasification](../chemistry/wood-gasification.md) — chemical reactions and gas composition details
- [Joining](../machine-tools/joining.md) — welding for gasifier fabrication
- [Water Treatment](../water/basic-treatment.md) — gas cooling water management

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*

