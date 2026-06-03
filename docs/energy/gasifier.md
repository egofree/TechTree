# Biomass Gasifier

> **Node ID**: energy.biomass-energy.gasifier
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.biomass-energy`](biomass-energy.md), [`metals.iron-steel`](../metals/iron-steel.md), [`ceramics.kilns`](../ceramics/kilns.md)
> **Enables**: [`energy.electricity`](electricity.md), [`energy.engine`](engine.md)
> **Timeline**: Years 10-25
> **Outputs**: producer_gas, wood_gas
> **Critical**: No — gasifiers enable engine-grade fuel from solid biomass, but diesel or gasoline engines can use petroleum fuels directly

## Principle

A biomass gasifier converts solid fuel (wood chips, charcoal, agricultural residues) into a combustible gas (producer gas or wood gas) through partial combustion in a restricted-air environment. The gasifier is a vertical shaft reactor with four distinct thermal zones stacked top to bottom: **drying** (50-150°C, moisture evaporates), **pyrolysis** (200-600°C, volatile matter released), **combustion** (800-1200°C, partial oxidation provides heat), and **reduction** (700-1000°C, CO₂ and H₂O are reduced by hot char to CO and H₂).

The key reduction reactions are: CO₂ + C → 2CO (Boudouard reaction, endothermic) and H₂O + C → CO + H₂ (water-gas reaction, endothermic). The heat for these endothermic reactions comes from the exothermic combustion zone above. The product gas composition is approximately: 18-25% CO, 12-20% H₂, 2-4% CH₄, 8-12% CO₂, 50-55% N₂. Heating value: 4.5-6.0 MJ/m³ (wood chips) — about one-sixth that of natural gas.

The downdraft (Imbert) design forces all gas through a constricted throat at the hottest part of the reactor, cracking tars into lighter gases. This produces cleaner gas suitable for internal combustion engines, unlike updraft designs that produce tar-laden gas only fit for direct combustion.

## Prerequisites

- [Steel plate and pipe](../metals/iron-steel.md) — for gasifier body, air nozzles, gas outlet
- [Firebrick or castable refractory](../ceramics/kilns.md) — for combustion zone lining
- [Welding capability](../machine-tools/joining.md) — for gasifier fabrication
- [Dry biomass fuel](biomass-energy.md) — wood chips (20-80 mm, <20% moisture) or charcoal (10-40 mm)
- [Engine-generator](engine.md) — to consume the producer gas

## Materials

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

## Construction Steps

1. **Fabricate the gasifier body**: Roll 6-10 mm steel plate into a cylindrical shell, 300-600 mm diameter (matching engine power). Weld the longitudinal seam. Weld a flat bottom plate. The shell height is 1.0-1.5 m. For the Imbert design, include a conical throat restriction (constriction ring) at the combustion zone — throat diameter is 60-75% of the body diameter.

2. **Line the combustion zone** with firebrick from the air nozzle level down through the reduction zone. The lining reduces heat loss from the hottest zone (800-1200°C) and protects the steel shell from oxidation. Mortar firebrick with refractory cement. Leave the upper portion (drying and pyrolysis zones) unlined — the steel shell acts as a heat exchanger, preheating incoming fuel.

3. **Install air nozzles (tuyeres)**: Weld 4-8 steel pipe nozzles (50 mm OD) through the shell wall at the throat level, pointing inward and slightly downward. Each nozzle has a removable cap for cleaning. The total nozzle area determines the maximum gas throughput — undersized nozzles restrict output, oversized nozzles cause channeling. Calculate nozzle area: approximately 5-10 cm² per 10 kW of engine output.

4. **Install the grate** at the bottom of the reduction zone. A grid of 15 mm square steel bars at 20 mm spacing supports the fuel bed while allowing ash to fall through. Make the grate removable for cleaning and ash removal.

5. **Build the fuel hopper**: Weld a conical steel top section (2-3 mm plate) above the main body. The hopper holds enough fuel for 1-4 hours of operation. Install a tight-fitting lid with a gasket seal — the gasifier operates under slight negative pressure (induced draft), and an unsealed hopper lid allows air ingress that dilutes the gas and creates explosion risk.

6. **Fabricate the cyclone separator**: Build a cylindrical sheet-metal vessel (200-400 mm diameter, 400-600 mm tall) with a tangential gas inlet near the top, a clean gas outlet at the top center, and a dust collection pot at the bottom. The cyclone removes >90% of particles larger than 10 μm by centrifugal force.

7. **Build the gas cooling and cleaning train**: Route the raw gas (exiting at 400-600°C) through a finned cooling pipe (reduce to <30°C — cooler gas is denser, improves engine volumetric efficiency). Then pass through a sawdust filter (200 liter drum filled with 100-200 mm of dry sawdust) for final tar and particulate removal. Target: <50 mg/m³ tar content for engine operation.

8. **Install the blower**: Connect an induced-draft blower on the gas outlet side (downstream of the gasifier, upstream of the engine). The blower pulls air through the fuel bed, maintaining negative pressure in the gasifier. For engine-coupled operation, engine suction alone provides draft — the blower is needed only for starting.

9. **Install an ignition port** in the combustion zone — a 50 mm diameter opening with a threaded plug, used for lighting the kindling during startup.

10. **Pressure-test the entire system**: Seal all openings, pressurize to 0.3 bar with compressed air. Apply soapy water to every weld, fitting, and gasket joint. Zero bubbles acceptable — any air leak in operation admits excess air, reducing gas quality and creating explosion hazard.

## Calibration and Verification

1. **Gas quality test (flare test)**: After lighting and reaching steady operation (10-20 minutes), open the gas outlet to a flare nozzle. Producer gas should burn with a stable blue-yellow flame. Sooty orange flame indicates excessive tars — improve throat design or add secondary air injection.

2. **Tar content measurement**: Pass a known volume of gas through a filter, weigh the deposit. Target: <50 mg/m³ for engine use. Above 100 mg/m³ — engine fouls within hours. Solutions: increase throat temperature, improve cooling, add secondary air.

3. **Gas composition**: Sample gas with an Orsat analyzer or gas chromatograph. Target: 18-25% CO, 12-20% H₂, 2-4% CH₄. Low CO indicates insufficient reduction zone temperature — the char bed may be too short.

4. **Cold gas efficiency**: Measure energy in product gas vs. energy in fuel input. Target: 65-75% for wood chips, 70-80% for charcoal. Low efficiency indicates excessive heat loss or incomplete reduction.

5. **Temperature profile**: Measure temperature at the combustion zone (target: 800-1200°C), reduction zone outlet (target: 600-800°C), and gas outlet (target: 400-600°C before cooling). Low combustion zone temperature indicates insufficient draft or wet fuel.

## Expected Performance

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

## Safety

- **Carbon monoxide poisoning**: Producer gas contains 18-32% CO — lethal at 0.1% (1000 ppm) in air. Operate gasifiers outdoors or in well-ventilated areas. Install CO detectors in any enclosed space where gas piping runs.
- **Gas explosion**: Producer gas is flammable at 15-70% concentration in air. Gas leaks into enclosed spaces create explosion risk. Install a flame arrestor (water seal or fine mesh screen) on the gas line between gasifier and engine.
- **Flashback**: Never open the fuel hopper lid while the gasifier is running — flashback can ignite fuel in the hopper. Install a double-lid interlock or water seal.
- **High temperature**: Gasifier combustion zone reaches 1000-1200°C. Outer shell may reach 200-400°C without insulation. Install firebrick lining and wear heat-resistant gloves when operating valves or ports.

## See Also

- [Biomass Energy](biomass-energy.md) — full coverage of biomass conversion pathways, biogas, and direct combustion
- [Heat Engines](engine.md) — internal combustion engines modified for producer gas fuel
- [Electricity Generation](electricity.md) — engine-generator sets
- [Charcoal Production](charcoal.md) — charcoal as premium gasifier fuel
- [Ceramics](../ceramics/kilns.md) — firebrick for combustion zone lining
- [Iron & Steel](../metals/iron-steel.md) — steel plate and pipe for gasifier construction

---

*Part of the [Bootciv Tech Tree](../index.md) · [Energy](./index.md) · [All Domains](../index.md)*
