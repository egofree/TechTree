# Thermal Control

> **Node ID**: spacecraft-systems.thermal-control
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: `metals`, `polymers`, `vacuum`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 40-200+
> **Outputs**: thermal_hardware
> **Critical**: Yes

Spacecraft thermal control is the discipline of maintaining every component — batteries, electronics, propellant lines, optical sensors — within its survival and operating temperature range while the spacecraft experiences solar flux of 1361 W/m² on one side and deep-space radiative cooling to 3 K on the other. In vacuum, there is no convective heat transfer: every watt of dissipated heat must be conducted through solid paths to radiator surfaces and radiated to space. This single constraint — the impossibility of convective cooling — shapes the entire thermal architecture.

This article covers spacecraft thermal control across three process areas: [passive thermal control](./thermal-control.passive-thermal.md) (MLI, coatings, heat pipes), [active thermal control](./thermal-control.active-thermal.md) (heaters, louvers, loop heat pipes, fluid loops), and [radiator design](./thermal-control.radiator-design.md) (radiator sizing, surface finishes, deployable radiators). Together they maintain spacecraft equipment within typical ranges of -20°C to +50°C for electronics, 0°C to +20°C for batteries, and ±0.1°C for precision optical benches.

## Overview

The spacecraft thermal environment is governed by three external heat sources and one internal source. External sources are direct solar radiation (1361 W/m² at 1 AU, the solar constant), solar energy reflected from Earth (albedo, typically 0.30-0.35 of the solar constant), and Earth infrared emission (220-280 W/m² for LEO). Internal heat comes from electronics dissipation — a 5 kW communications satellite generates 3-4 kW of waste heat that must be rejected to space.

The thermal balance equation for any surface element is:

```
Q_absorbed_solar + Q_absorbed_albedo + Q_absorbed_earth_IR + Q_internal_dissipation = Q_radiated + Q_conducted + Q_stored
```

Where Q_radiated = ε·σ·A·T⁴ (Stefan-Boltzmann law, σ = 5.67×10⁻⁸ W/m²·K⁴). The thermal control subsystem manipulates the absorptivity (α) and emissivity (ε) of surfaces, the conductive paths between components and radiators, and — when passive means are insufficient — actively transports heat via pumped fluid loops or heat pipes.

## Multi-Layer Insulation (MLI)

MLI is the primary passive thermal control element on virtually every spacecraft. It consists of multiple layers of reflective foil separated by spacer material, forming a blanket that blocks radiative heat transfer between the spacecraft and the space environment.

### MLI Construction

| Layer | Material | Thickness | Function |
|-------|----------|-----------|----------|
| Outer cover | Beta cloth (fibreglass) | 0.10 mm | Handling protection, grounding |
| Reflector (×30) | Aluminised Kapton | 0.0076 mm (7.6 µm) | Reflect IR radiation |
| Separator (×30) | Dacron net | 0.15 mm | Prevent reflector contact |
| Inner cover | Aluminised Kapton | 0.013 mm | Containment, grounding |
| Velcro / snaps | — | — | Attachment to spacecraft |

A 30-layer MLI blanket achieves an effective emissivity (ε_eff) of less than 0.02, meaning it transmits less than 2% of the blackbody radiation that a single surface would emit. The radiative heat transfer through 30-layer MLI at a 100 K temperature differential is approximately 1.5 W/m², compared to 550 W/m² for a bare black surface — a 99.7% reduction.

### MLI Performance by Layer Count

| Layers | Effective emissivity (ε_eff) | Heat leak at 100 K ΔT (W/m²) | Typical use |
|--------|------------------------------|-----------------------------|------------|
| 5 | 0.020 | 1.1 | Internal partitions |
| 10 | 0.012 | 0.7 | Cryogenic lines |
| 20 | 0.008 | 0.4 | Standard external blanket |
| 30 | 0.005 | 0.3 | Primary external blanket |
| 40 | 0.004 | 0.2 | Cryogenic tank wrap |

Diminishing returns set in after approximately 20-30 layers: each additional layer adds mass and assembly complexity while providing progressively less insulation benefit. The layer count is chosen by trading blanket mass against acceptable heat leak for the specific application.

## Surface Coatings and Finishes

The optical properties of external surfaces determine how much solar energy the spacecraft absorbs and how efficiently it radiates heat to space. The key parameters are solar absorptivity (α, typically 0.05-0.95) and infrared emissivity (ε, typically 0.02-0.90).

### Coating Properties Table

| Coating | Solar α | IR ε | α/ε ratio | Notes |
|---------|---------|------|-----------|-------|
| White paint (Z93P) | 0.25 | 0.88 | 0.28 | Stable, high ε; silicate-based |
| Black paint (Chemglaze Z306) | 0.97 | 0.89 | 1.09 | Internal or high-α areas |
| Aluminised Kapton | 0.14 | 0.05 | 2.80 | Outer MLI cover; sun-facing |
| Silvered Teflon (FEP) | 0.08 | 0.80 | 0.10 | Low α/ε, stable; radiators |
| Polished aluminium | 0.15 | 0.05 | 3.00 | Bare metal; conductive surfaces |
| Anodised aluminium | 0.25-0.85 | 0.60-0.90 | varies | Tunable α by dye colour |
| OSR (optical solar reflector) | 0.08 | 0.80 | 0.10 | Silvered quartz tiles; radiators |

The ratio α/ε determines equilibrium temperature: a surface with α/ε < 1 cools in sunlight (emits more than it absorbs), while α/ε > 1 heats up. A silvered Teflon radiator facing the sun reaches approximately -40°C at equilibrium because it absorbs very little solar energy (α = 0.08) while radiating efficiently (ε = 0.80). A black paint surface in the same orientation reaches +120°C.

### Coating Selection Criteria

- **Sun-facing radiators**: Silvered Teflon or OSR (α/ε ≈ 0.10) — rejects solar input while radiating efficiently
- **Sun-facing insulation**: Aluminised Kapton (α = 0.14, ε = 0.05) — minimises both solar absorption and radiative loss
- **Shadowed radiators**: White paint (α = 0.25, ε = 0.88) — high emissivity, modest solar tolerance
- **Internal surfaces**: Black paint (α = 0.97, ε = 0.89) — maximises radiative coupling between adjacent surfaces
- **Anti-sun surfaces**: White paint or black paint — either works since no solar input

## Heat Pipes

Heat pipes are passive, two-phase heat transfer devices that transport heat from a heat source to a heat sink with minimal temperature drop. They are the workhorse of spacecraft thermal management, moving heat from dissipating electronics to radiator surfaces with effective thermal conductivities 100-1000× that of solid copper.

### Heat Pipe Operating Principles

A heat pipe is a sealed tube containing a working fluid at its saturation pressure. Heat applied at the evaporator end vaporises the fluid; the vapour flows to the condenser end where it condenses, releasing heat; capillary action in a wick structure returns the liquid to the evaporator. The process is entirely passive — no pumps, no moving parts.

### Heat Pipe Parameters

| Parameter | Typical value | Range |
|-----------|--------------|-------|
| Working fluid | Ammonia (NH₃) | Methane, water, methanol |
| Envelope material | Aluminium 6061 | Stainless steel, copper |
| Wick structure | Axial grooves | Screen mesh, sintered powder |
| Operating temperature | -50 to +50°C | Fluid-dependent |
| Heat transport capacity | 50-500 W | Per pipe, length-dependent |
| Effective conductivity | 10,000-50,000 W/m·K | 100-1000× copper |
| Temperature drop (evap→cond) | 2-5°C | Over 1 m length |

Ammonia is the dominant working fluid for spacecraft heat pipes because its operating temperature range (-50 to +50°C) aligns with typical spacecraft equipment temperatures, and its latent heat of vaporisation (1370 kJ/kg) is among the highest of any fluid at these conditions.

## Loop Heat Pipes (LHP)

A loop heat pipe is a more sophisticated two-phase device that separates the liquid and vapour lines into distinct parallel paths, enabling heat transport over longer distances (up to 10+ metres) and against gravitational heads (relevant for ground testing). LHPs are used on large communications satellites and interplanetary probes to move 100-1000 W of heat from payload electronics to deployable radiators.

### LHP Characteristics

| Parameter | Value |
|-----------|-------|
| Heat transport | 100-1000 W |
| Transport distance | 1-15 m |
| Operating temperature | -40 to +80°C |
| Working fluid | Ammonia, propylene |
| Evaporator material | Aluminium, stainless steel |
| Condenser | Tube-on-radiator panel |
| Passive start-up | Yes (no external priming) |

The LHP evaporator contains a capillary wick (sintered nickel or PTFE) that separates the liquid and vapour phases. Vapour generated at the evaporator exits through a vapour line to the condenser; condensed liquid returns through a liquid line, passing through a compensation chamber that regulates the loop's fluid inventory. The entire loop is passive — capillary action in the wick drives circulation without any pump.

## Active Thermal Control

When passive elements (MLI, coatings, heat pipes) cannot maintain equipment within limits, active thermal control elements are introduced. These include heaters, louvers, fluid loops, and thermoelectric coolers.

### Heater Zones

Electric heaters are used to maintain minimum temperatures on components that generate little internal heat but must not freeze — batteries, propellant lines, propulsion valves, and cold-soaked electronics during eclipse. A typical spacecraft has 20-100 independently controlled heater zones.

| Zone type | Setpoint | Deadband | Power per zone | Control |
|-----------|---------|----------|---------------|---------|
| Battery | +5°C | ±3°C | 5-20 W | Thermostat / software |
| Propellant line | +10°C | ±5°C | 2-10 W | Thermostat |
| Catalyst bed | +150°C | ±10°C | 10-50 W | Software PID |
| Survive-safe | -10°C | ±10°C | 5-30 W | Hardwired thermostat |

### Louvers

Louvers are mechanical shutters that modulate the effective emissivity of a radiator surface. A bimetallic spring or actuator-driven blade opens to expose the high-emissivity radiator surface when hot and closes to cover it with a low-emissivity blade when cold.

- **Blade open position**: Radiator ε_eff ≈ 0.85 (exposed surface radiates to space)
- **Blade closed position**: Radiator ε_eff ≈ 0.15 (blade blocks radiation)
- **Transition range**: Typically 15-30°C blade-open to blade-close
- **Modulation ratio**: 5:1 to 6:1 (ratio of hot to cold radiative heat rejection)

The louver transition is not linear: blades begin to open at a set temperature and reach full open over a 5-15°C range. The sharp transition provides effective temperature regulation without electrical control input — the bimetallic actuator responds directly to radiator temperature.

## Radiator Sizing

The radiator is the ultimate heat sink for all spacecraft thermal dissipation. Its required area is determined by the heat rejection requirement, radiator temperature, surface optical properties, and environmental heat input (solar, albedo, Earth IR).

### Radiator Area Calculation

For a flat-plate radiator with both surfaces radiating to deep space (neglecting environmental input):

```
A = Q / (2 · ε · σ · T⁴)
```

Where Q is the heat to reject (W), ε is surface emissivity, σ is the Stefan-Boltzmann constant, and T is radiator absolute temperature (K). For a 1 kW heat rejection at +30°C (303 K) with ε = 0.88:

```
A = 1000 / (2 · 0.88 · 5.67×10⁻⁸ · 303⁴) = 1000 / 851 = 1.18 m²
```

A double-sided radiator needs 1.18 m² to reject 1 kW at 30°C. If the radiator faces the sun, solar input must be subtracted from the net rejection:

```
Q_net = 2 · ε · σ · A · T⁴ - α · S · A
```

Where S is the solar constant (1361 W/m²) and α is solar absorptivity. For a silvered Teflon radiator (α = 0.08, ε = 0.80) facing the sun:

```
Q_net = 2 · 0.80 · 5.67×10⁻⁸ · A · 303⁴ - 0.08 · 1361 · A = 768·A - 109·A = 659·A
```

The same 1.18 m² radiator facing the sun rejects only 659 × 1.18 = 778 W — 22% less than the shadowed case. This is why radiators are oriented perpendicular to the sun line wherever possible, or shielded by solar arrays that double as sun shields.

### Radiator Types

| Type | Heat rejection | Mass/area | Complexity | Typical use |
|------|---------------|-----------|-----------|------------|
| Body-mounted | 100-200 W/m² | 3-5 kg/m² | Low | Small satellites |
| Single-sided panel | 200-350 W/m² | 4-7 kg/m² | Low | LEO spacecraft |
| Double-sided panel | 350-700 W/m² | 5-9 kg/m² | Medium | GEO commsats |
| Deployable (rigid) | 350-700 W/m² | 6-10 kg/m² | Medium | Large commsats |
| Deployable (flexible) | 200-400 W/m² | 4-7 kg/m² | High | Crewed vehicles |
| Loop heat pipe radiator | 300-600 W/m² | 5-9 kg/m² | High | Interplanetary probes |

## Thermal Modelling

Spacecraft thermal design is validated using a thermal mathematical model (TMM) — a lumped-parameter network of nodes connected by conductive and radiative conductances. The model is solved as a time-dependent energy balance at each node.

### Model Structure

A typical spacecraft TMM contains 500-5000 nodes. Each node represents a thermal mass (component, panel section, bracket) characterised by its mass, specific heat, and temperature. Conductances between nodes represent:

- **Solid conduction**: G = k·A/L (Fourier's law, k = thermal conductivity)
- **Contact conduction**: G = h_c·A (interface conductance, h_c ≈ 200-2000 W/m²·K)
- **Radiation**: G_rad = ε·σ·A·(T₁² + T₂²)(T₁ + T₂) (linearised radiative conductance)
- **Fluid convection**: G = h·A (forced or natural convection coefficient)
- **Heat pipe**: G_eff ≈ 10,000-50,000 W/K (effective conductance)

The model is exercised through worst-case hot and cold orbital cases (maximum and minimum solar flux, full eclipse, worst payload dissipations) to verify that every node remains within its qualification temperature range. Model predictions are correlated against thermal-vacuum test data with a target accuracy of ±10°C.

## Fluid Loops

For high-power spacecraft (communications satellites with 10-20 kW payloads, crewed vehicles with 30+ kW), passive heat pipes cannot transport the required heat loads over the required distances. Pumped fluid loops circulate a coolant (typically ammonia-water solution or HFC-218) through cold plates mounted on high-dissipation electronics, transporting heat to remote radiators.

### Fluid Loop Sizing

| Parameter | Value |
|-----------|-------|
| Working fluid | Ammonia, HFC-218, Freon-21 |
| Flow rate | 0.5-5.0 L/min per loop |
| Pump power | 5-50 W |
| Heat transport | 500-5000 W per loop |
| Temperature range | -40 to +40°C |
| Loop length | 2-20 m |
| Pump type | Centrifugal (DC motor) |

The International Space Station uses an internal water loop (20°C setpoint) coupled through an interface heat exchanger to an external ammonia loop, which transports heat to the station's deployable radiators. Each of the four main radiators rejects approximately 7.5 kW, for a total rejection capability of 30 kW.

## Thermal-Vacuum Test Environment

All thermal control hardware is qualified in thermal-vacuum chambers that simulate the orbital environment. The chamber combines:

- Vacuum (< 10⁻³ Pa, achieved by turbomolecular pumps)
- Cold wall (liquid nitrogen shroud at -180°C simulating deep space)
- Solar simulator (xenon arc lamp, 1 solar constant intensity)
- Heat rejection (cold plates simulating spacecraft radiators)
- Data acquisition (hundreds of thermocouples to ±0.5°C accuracy)

Thermal balance tests measure the spacecraft's actual thermal performance against model predictions; thermal cycle tests exercise the spacecraft through 20-200 hot/cold cycles to verify workmanship and fatigue margins.

## Troubleshooting

| Symptom | Likely cause | Diagnostic | Fix |
|---------|-------------|-----------|-----|
| Component overheats | MLI gap at heat source | IR camera survey | Patch MLI gap |
| Component too cold | Heater thermostat stuck open | Measure resistance | Replace thermostat |
| Heat pipe dry-out | Non-condensable gas in pipe | Adiabatic section temperature | Replace pipe |
| LHP fails to start | Evaporator superheat insufficient | Monitor temperatures | Apply pre-heat |
| Radiator underperformance | Contamination of surface | Measure α/ε with spectrometer | Clean or recoat |
| Battery zone hunting | Deadband too narrow | Review temperature trace | Widen deadband to ±5°C |

## Glossary

- **MLI**: Multi-Layer Insulation — stacked reflective foils that block radiative heat transfer
- **α (absorptivity)**: Fraction of incident solar radiation absorbed by a surface (0 to 1)
- **ε (emissivity)**: Fraction of blackbody radiation emitted by a surface at its temperature (0 to 1)
- **OSR**: Optical Solar Reflector — silvered quartz tile providing low α and high ε for radiator surfaces
- **Heat pipe**: Sealed two-phase device that transports heat via evaporation/condensation of a working fluid
- **LHP**: Loop Heat Pipe — two-phase device with separate liquid and vapour lines for long-distance heat transport
- **Louver**: Mechanical shutter that modulates radiator emissivity in response to temperature
- **TMM**: Thermal Mathematical Model — lumped-parameter network solved to predict spacecraft temperatures
