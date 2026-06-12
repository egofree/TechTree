# Electricity Generation & Distribution

> **Node ID**: energy.electricity
> **Also covers**: `chemistry.electrolysis`, `machine-tools.joining`, `energy.power-systems`
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`electronics.wire-insulation`](../electronics/wire-insulation.md),
> [`energy.steam-power`](./steam-power.md),
> [`metals.copper-refining`](../metals/copper-refining.md),
> [`metals.magnetic-materials`](../metals/magnetic-materials.md),
> [`metals.wire-drawing`](../metals/wire-drawing.md)
> **Enables**: [`chemistry.air-separation`](../chemistry/air-separation.md),
> [`computing.electromechanical`](../computing/electromechanical.md),
> [`construction.industrial-buildings`](../construction/industrial-buildings.md),
> `cryogenics`, `electrochemistry`,
> [`electronics.electrical-systems`](../electronics/electrical-systems.md),
> [`energy.electricity.power-systems`](./electricity.power-systems.md),
> [`energy.geothermal`](./geothermal.md),
> [`energy.power-distribution`](./power-distribution.md),
> [`energy.storage.pumped-hydro`](./storage.pumped-hydro.md),
> [`machine-tools.edm-cnc`](../machine-tools/edm-cnc.md),
> [`machine-tools.joining.electron-beam`](../machine-tools/joining.electron-beam.md),
> [`machine-tools.joining.laser-welding`](../machine-tools/joining.laser-welding.md),
> [`machine-tools.joining.mig-welding`](../machine-tools/joining.mig-welding.md),
> [`machine-tools.joining.resistance-welding`](../machine-tools/joining.resistance-welding.md),
> [`machine-tools.joining.tig-welding`](../machine-tools/joining.tig-welding.md),
> [`machine-tools.joining.ultrasonic-bonding`](../machine-tools/joining.ultrasonic-bonding.md),
> [`machine-tools.joining.welding`](../machine-tools/joining.welding.md),
> [`measurement.electrical-instruments`](../measurement/electrical-instruments.md),
> [`measurement.temperature-pressure`](../measurement/temperature-pressure.md),
> [`metals.aluminum.semiconductor-grade`](../metals/aluminum.semiconductor-grade.md),
> [`photolithography.fab-processes.ion-implantation`](../photolithography/fab-processes.ion-implantation.md),
> [`precision-motion.nanometer-positioning`](../precision-motion/nanometer-positioning.md),
> [`silicon.purification`](../silicon/purification.md), `telecom`,
> [`telecom.electric-telegraph`](../telecom/electric-telegraph.md),
> [`telecom.radio`](../telecom/radio.md),
> [`telecom.telephone`](../telecom/telephone.md),
> [`transport.telegraph`](../transport/telegraph.md)
> **Critical**: Yes — electricity is the universal energy carrier required for electrolysis, electric furnaces, electric motors, electronics, and every semiconductor process
> **Timeline**: Years 15-30
> **Outputs**: generators, motors, transformers, wire_cables, electricity, insulated_wire, clean_power_systems, ups_systems, backup_generators, power_distribution_units, electric_arc_furnaces, resistance_heaters, eaf_steel, internal_combustion_engines

## Overview

Electricity is the most versatile energy carrier — it converts to heat, light, mechanical work, and chemical reactions with high efficiency. No alternative exists for industrial electrification: electrolysis, electric furnaces, motors, electronics, and every semiconductor process require electrical power.

## Dedicated Articles

Detailed construction and operation guides have their own articles:

- **[Generator](generator.md)** — Faraday magneto through self-exciting dynamo to three-phase alternator. Full BOM, winding procedures, commutator construction, calibration, and troubleshooting for DC and AC generators.
- **[Electric Motor](electric-motor.md)** — DC motors (series, shunt, compound) and AC induction motors (squirrel-cage). Construction, winding patterns, bearing selection, speed control, and quality control.
- **[Electric Furnaces](electric-furnaces.md)** — Electric arc furnace (EAF) for steelmaking and silicon reduction, submerged arc furnace (SAF) for continuous smelting, and resistance heating furnaces (Nichrome, Kanthal, SiC, MoSi₂ elements).
- **[Heat Engines](engine.md)** — Otto cycle, Diesel, gas turbine, Stirling, and steam engines. Selection guide, efficiency comparison, and bootstrap progression.
- **[Transformer & Power Distribution](power-distribution.md)** — Transformer construction, core and winding manufacturing, substation layout, switchgear, and distribution panels for AC power transmission.
- **[Advanced Welding](../machine-tools/joining.md)** — Oxy-acetylene, arc welding (SMAW), joint preparation, and welding safety.

## Voltaic Piles & Early Batteries

The first electrical source, requiring no moving parts: stack alternating disks of copper plate → cardboard soaked in brine (or sulfuric acid) → zinc plate → repeat. 10-20 cells produce 10-20V DC at ~50-100 mA — sufficient for early electroplating, telegraph operation, and electrochemistry exploration, but not industrial power.

The **Daniell cell** (copper electrode in CuSO₄, separated by porous pot from zinc electrode in ZnSO₄ or dilute H₂SO₄) produces a stable 1.1V with longer life, and became the standard for telegraph systems. Batteries have low energy density (lead-acid: 25-35 Wh/kg) and are not practical for industrial power — generators are essential.

## Wire Drawing Bootstrap

Wire drawing is a chicken-and-egg problem: you need wire for generators, but hardened steel dies for drawing wire require powered machinery. First wire is made by hammering or swaging copper rod, then pulling through hand-punched holes in hardened steel plates, iterating through successively smaller die openings. Each pass reduces diameter ~20-30%. Annealing between passes (heat to 400-600°C) restores ductility lost from cold work. Lubrication (tallow or soap solution) is critical at every pass — without it the wire galls and snaps. Insulation (rubber solution, cotton thread, varnish, or gutta-percha) is applied after drawing. Common gauges: 1 mm diameter for winding (~18 AWG), 0.1 mm for fine coils (~38 AWG).

## Copper Wire Gauge Reference

| Diameter (mm) | Cross-section (mm²) | Resistance (Ω/km) | Max current (A) | Typical use |
|---------------|---------------------|--------------------|-----------------|-------------|
| 0.1 | 0.008 | 2,200 | 0.05 | Fine coils, instruments |
| 0.5 | 0.20 | 88 | 1.0 | Small transformers |
| 1.0 | 0.79 | 22 | 5 | Motor windings, generator coils |
| 1.5 | 1.8 | 12 | 10 | Lighting circuits |
| 2.5 | 4.9 | 4.5 | 20 | Branch circuits |
| 4.0 | 12.6 | 1.7 | 40 | Sub-main feeds |
| 6.0 | 28.3 | 0.77 | 70 | Main distribution |
| 10.0 | 78.5 | 0.28 | 130 | Service entrance, bus bars |

Max current assumes 3-5 A/mm² for enclosed wiring. Voltage drop: ΔV = I × (ρ × L / A), where ρ = 0.0175 Ω·mm²/m for copper.

## Electrolysis Foundations

Passing DC current through ionic solutions or molten salts decomposes compounds at electrodes (anode: oxidation, cathode: reduction). Power: 2-5V per cell, 100-10,000+ A for industrial scale. Key applications: chlor-alkali (NaCl brine → Cl₂ + H₂ + NaOH, ~3.5-4V), water electrolysis (H₂O → H₂ + ½O₂ in 25-30% KOH, ~1.8-2.2V), [aluminum smelting](../metals/aluminum.md) (Hall-Héroult: Al₂O₃ in molten cryolite at 950-1000°C, 4-5V, 100,000+ A, ~13-15 kWh/kg), and copper refining (impure anode → 99.99% pure cathode in CuSO₄/H₂SO₄, ~0.3V; gold, silver, platinum recovered from anode slimes).

## Permanent Magnets

**Lodestone** (naturally magnetized magnetite) serves for early compasses and basic experiments. **Magnetized iron/steel bars** (stroked with lodestone or placed in Earth's field) provide field poles for early generators and galvanometers. For stronger magnets: place steel bar inside a coil and pass DC current — steel retains magnetism after current is removed. Store magnets with a soft iron keeper across poles to prevent demagnetization. Later materials (Alnico, ferrite) arrive with chemistry-stage alloy development.

## Elastomer Processing

Natural rubber vulcanization (latex + 1.5-3 phr sulfur + zinc oxide, heat-cured at 140-180°C) produces shaft seals, gaskets, belts, hoses, and wire insulation. [Synthetic rubbers](../polymers/synthetic.md) require [petrochemical feedstocks](../chemistry/petroleum-alternatives.md).

## Safety & Hazards

- **Electrocution**: 100 mA across the chest causes ventricular fibrillation. Even 50V+ can be lethal wet. De-energize and lock-out/tag-out. One-hand rule near live circuits.
- **Arc flash**: Short circuits produce arcs reaching 20,000°C. Arc-rated PPE for energized panel work.
- **Fire risk**: Electrical faults cause industrial fires. Proper fusing and circuit breakers on all circuits.
- **Mechanical**: Guard all rotating shafts and belts. No loose clothing near running machinery.

## Electrical Insulation Classes

| Insulation Class | Max Temperature | Common Materials |
|-----------------|----------------|------------------|
| Class A | 105°C | Cotton, silk, paper, varnish |
| Class B | 130°C | Mica, glass fiber, polyester |
| Class F | 155°C | Mica, glass fiber, silicone resin |
| Class H | 180°C | Silicone elastomer, mica, glass |

Every 8-10°C above rated temperature approximately halves insulation life (the "10-degree rule").

## Three-Phase Power & Power Factor

Three-phase AC is the industrial standard: three conductors carry voltage waveforms offset by 120°, delivering 1.5× the power of single-phase for the same conductor material with constant instantaneous power. Line-to-line voltage = √3 × line-to-neutral voltage (e.g., 400V/231V).

Power factor (PF) is the ratio of real power (watts) to apparent power (VA). Inductive loads (motors, transformers) have PF = 0.6-0.85, wasting 15-40% of current capacity on reactive power. Correction: install capacitor banks to cancel lagging reactive current. Target PF = 0.90-0.95.

## Semiconductor Fab Power Systems

Semiconductor fabrication demands power quality far exceeding general industrial requirements. A voltage sag of just 10% lasting <1 cycle can abort lithography exposures and destroy wafer lots worth millions. This requires:

- **Clean power**: Voltage ±5%, THD <3%, frequency ±0.1 Hz, phase imbalance <1%. Achieved through isolation transformers (K-13 to K-20 rated), cascaded surge protection, and active harmonic filters.
- **Online double-conversion UPS**: All power flows rectifier → DC bus → inverter continuously, providing complete input isolation. Zero transfer time. Efficiency 90-94%. Battery runtime: 10-30 minutes to bridge to generator start.
- **Backup diesel generators**: 2-4 units of 1-3 MW each for a 30,000 WSPM fab. Start and accept load within 10-15 seconds. Fuel storage for 24-72 hours. Target >98% start reliability.
- **Power distribution architecture**: Dedicated feeders → medium-voltage switchgear → step-down transformers → UPS systems → K-rated PDUs → individual tools. Redundancy: N+1 for general loads, 2N for critical lithography and implant tools.
- **Grounding**: Safety ground (equipment frames to earth, <5 Ω) plus signal reference ground (equipotential grid under raised floor for noise reduction at DC to >10 MHz).

## Limitations

- **Bootstrapping challenge**: Wire drawing needs hardened steel dies requiring powered machinery — resolved by starting with hammered wire through hand-punched holes.
- **Copper demand**: A 100 kW generator requires ~50-100 kg copper wire. Aluminum substitutes at 60% conductivity per unit area.
- **Energy storage gap**: Electricity cannot be stored directly at scale — batteries are heavy (lead-acid: 25-35 Wh/kg), pumped hydro requires specific geography.
- **Transmission losses**: 1-13% over long distances, requiring higher voltages and larger conductors.
- **Insulation degradation**: Every 8-10°C above rated temperature halves insulation life.

## See Also

- [Generator](generator.md) — DC and AC generator construction
- [Electric Motor](electric-motor.md) — DC and AC motor construction
- [Electric Furnaces](electric-furnaces.md) — EAF, SAF, resistance furnaces
- [Transformer & Power Distribution](power-distribution.md) — Transformers, substations, switchgear
- [Energy Storage](storage.md) — Batteries, pumped hydro, UPS battery sizing
- [Heat Engines](engine.md) — Diesel engines for backup generators
- [Electrode Manufacturing](electrode-manufacturing.md) — Carbon electrode production
- [Electrolysis](../chemistry/electrolysis.md) — Chlor-alkali, aluminum, copper refining
- [Steam Power](steam-power.md) — Prime movers for generators
- [Measurement](../measurement/index.md) — Power quality monitoring instruments
---
*Part of the [Bootciv Tech Tree](../../index.md) • [Energy](./index.md) • [All Domains](../../index.md)*
