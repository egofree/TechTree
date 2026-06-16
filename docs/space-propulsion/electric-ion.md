# Electric Propulsion — Ion

> **Node ID**: space-propulsion.electric-ion
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`electronics.power-electronics`](../electronics/power-electronics.md),
> [`vacuum.chambers`](../vacuum/chambers.md),
> [`metals.refractory-specialty`](../metals/refractory-specialty.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: ion_thrusters
> **Critical**: No — gridded ion thrusters sit at the apex of the in-space propulsion hierarchy, requiring high-voltage power electronics, refractory-metal grid machining, and long-duration vacuum test facilities that arrive only after the full semiconductor, vacuum, and precision-machining base is established

Gridded ion thrusters are the highest-specific-impulse propulsion systems ever flown. A 30 cm [ionization chamber](./electric-ion.ionization-chamber.md) generates a low-temperature xenon plasma at 5–10 eV; a pair of precisely machined [acceleration grids](./electric-ion.acceleration-grids.md) then extracts ions from this plasma and electrostatically accelerates them to exhaust velocities of 30,000 m/s — ten times faster than the best chemical rocket exhaust. The [power processing unit](./electric-ion.power-processing-unit.md) converts spacecraft bus power (28–100 V DC) into the precisely regulated high voltages (300–2000 V) needed for plasma generation and beam extraction, while the [neutralizer](./electric-ion.neutralizer-design.md) injects electrons into the ion beam to prevent spacecraft charging.

The defining trade of ion propulsion is thrust versus efficiency. An ion thruster produces only 20–250 mN of thrust — the weight of a sheet of paper — but sustains it for tens of thousands of hours. Over a mission this integrates to a velocity change (Δv) of 10 km/s or more, far beyond what chemical propulsion can deliver for the same propellant mass. Deep Space 1 used 74 kg of xenon to achieve 4.3 km/s Δv; Dawn used 425 kg across 7 years to rendezvous with Vesta and Ceres. No chemical system could match these mission profiles within a feasible launch mass.

## Overview

A gridded ion thruster operates on the principle of electrostatic acceleration: ions are created in a discharge chamber, extracted through a set of perforated grids held at different potentials, and accelerated by the electric field between the grids. The beam current, grid voltage, and propellant flow together determine the thrust and specific impulse. Because the acceleration is purely electrostatic (no nozzle, no combustion), the exhaust velocity is set by the voltage and ion mass alone — it is decoupled from the energy source, allowing solar or nuclear power to substitute for chemical bond energy.

The propellant of choice is **xenon** (atomic mass 131.3 g/mol), a noble gas that is inert, easily ionized (first ionization potential 12.1 eV), and condensed to a liquid for storage at room temperature under modest pressure (~60 bar). Alternatives — krypton (83.8 g/mol), argon (39.9 g/mol), and bismuth (209 g/mol, vaporized) — trade storage density, ionization cost, and Isp. Xenon dominates because its high mass gives good Isp at moderate voltages and its inertness eliminates material compatibility concerns.

The [power electronics](../electronics/power-electronics.md) heritage is central to ion thruster viability: the PPU must switch hundreds of watts to kilowatts at 90%+ efficiency while surviving radiation, thermal cycling, and vacuum. The [vacuum chambers](../vacuum/chambers.md) needed for ground qualification must sustain pressures below 10⁻⁵ Pa while ingesting the full propellant throughput — a 5 kW thruster expels 20 mg/s of xenon, requiring cryopump speeds exceeding 100,000 L/s to maintain test pressure. Refractory metals — [molybdenum](../metals/refractory-specialty.md) for grids, tungsten for cathode orifices — survive the 1000+ V ion bombardment and 2000 K emitter temperatures that no other material can endure.

## Physics of Electrostatic Acceleration

The fundamental equation for ion exhaust velocity is derived from energy conservation: an ion of charge `q` falling through a potential `V` gains kinetic energy `qV`, giving velocity:

- `v = sqrt(2 * q * V / m)`

For a singly-charged xenon ion (q = 1.6×10⁻¹⁹ C, m = 2.18×10⁻²⁵ kg) accelerated through 1000 V:

- `v = sqrt(2 * 1.6e-19 * 1000 / 2.18e-25) = 38,300 m/s`

This corresponds to Isp = v/g₀ = 3900 seconds — within the operating range of NEXT-class thrusters. The thrust is simply the ion mass flow rate times this exhaust velocity:

- `F = ṁ_ion * v = (I_beam / q) * m_ion * sqrt(2qV/m)`

For NSTAR at full power (I_beam = 3.3 A, V = 1100 V): F = 92 mN — exactly the measured value.

Key implications of the electrostatic acceleration physics:

- **Isp scales with sqrt(V)**: doubling grid voltage increases Isp by √2 (41%), not 2×. Pushing beyond 2000 V yields diminishing returns — insulation and grid gap tolerances become prohibitive.
- **Thrust scales with beam current**: to double thrust at fixed Isp, double the beam current (i.e., double the grid area or the plasma density).
- **Isp scales with sqrt(1/m_ion)**: lighter propellants give higher exhaust velocity at the same voltage. Hydrogen would give 10× the Isp of xenon at 1000 V, but its storage density and ionization cost make it impractical.
- **Beam power = 0.5 × I_beam × V_beam**: a 5 kW beam at 1100 V (4.5 A) delivers 2.5 kW to the exhaust stream.
- **Total efficiency = beam power / input power**: typically 55–65% for flight thrusters when discharge, neutralizer, and PPU losses are included.
- **Child-Langmuir limit**: the maximum current density that can be extracted from the plasma is `j = (4/9) * ε₀ * sqrt(2q/m) * V^(3/2) / d²`, where d is the grid gap. This sets the maximum thrust per unit grid area.

## Mission Heritage

The following table summarizes the ion thrusters that have flown on operational space missions, from the first deep-space demonstration to modern commercial GEO satellites. Every parameter is a design trade: higher power enables higher thrust but demands larger solar arrays; higher Isp extends mission life but requires higher grid voltage and tighter ion optics.

| Thruster | Mission | Power | Isp (s) | Thrust (mN) | Propellant | Beam Current | Qualification |
|----------|---------|-------|---------|-------------|------------|--------------|---------------|
| NSTAR | Deep Space 1, Dawn | 0.5–2.3 kW | 1900–3100 | 19–92 | Xenon | 1.1–3.3 A | 30,000+ hr |
| NEXT | (Flight demonstrator) | 0.5–6.9 kW | 1900–4190 | 23–236 | Xenon | 3.4–12.5 A | 48,000+ hr |
| T6 (QinetiQ) | BepiColombo | 0.5–4.5 kW | 1700–4200 | 16–145 | Xenon | 3.3–12 A | 17,000+ hr |
| XIPS-13 | GEO commsats | 0.5 kW | 2500 | 18 | Xenon | 0.8 A | 15,000+ hr |
| XIPS-25 | GEO commsats (702 bus) | 4.5 kW | 3500 | 165 | Xenon | 4.2 A | 20,000+ hr |
| µ10 | Hayabusa, Hayabusa2 | 0.35 kW | 1200–3200 | 5–9 | Xenon | 0.14 A | 20,000+ hr |
| NEXT-Long Life | Life test | 6.9 kW | 4190 | 236 | Xenon | — | 51,000 hr |

The NSTAR thruster on Deep Space 1 was the first ion thruster used for primary propulsion on an interplanetary spacecraft. Operating at 2.3 kW with an Isp of 3100 s, it delivered 92 mN of thrust and accumulated 16,226 hr of operation, processing 74 kg of xenon to achieve 4.3 km/s of Δv. The Dawn mission extended this: two NSTAR-derived thrusters fired cumulatively for 5.9 years, consuming 425 kg of xenon across 7 years of interplanetary transit to reach and orbit both Vesta and Ceres — a mission impossible with chemical propulsion.

NEXT (NASA's Evolutionary Xenon Thruster) pushed the envelope further: 6.9 kW, 236 mN thrust, Isp 4190 s — the highest Isp ever demonstrated for a gridded ion thruster at meaningful thrust levels. Its 36 cm beam diameter and 7 A beam current represent the practical upper bound for single-stage grid technology. The 51,000-hour life test confirmed that the wear-limited components (acceleration grids, discharge cathode) could survive a 30-year mission with margin.

## Ionization Mechanisms

Three methods are used to generate the plasma inside the discharge chamber, each trading power consumption, complexity, and lifetime:

### Electron Bombardment (DC Discharge)

A thermionic hollow cathode emits electrons into the discharge chamber; a magnetic field (typically a multi-cusp arrangement of samarium-cobalt permanent magnets) confines the electrons in helical trajectories, increasing their path length and probability of ionizing xenon atoms via collision. The discharge voltage is 25–40 V DC at 5–20 A. This is the simplest and most flight-proven approach — NSTAR, NEXT, and XIPS all use DC discharge. The discharge cathode lifetime is the limiting factor, typically 20,000–30,000 hr before the BaO emitter is depleted.

Key characteristics of DC discharge ionization:

- **Discharge voltage**: 25–40 V DC (optimized for xenon ionization cross-section)
- **Discharge current**: 5–20 A (scales with thruster power class)
- **Discharge loss**: 100–300 W per amp of beam current (ionization energy cost)
- **Magnetic confinement**: SmCo multi-cusp array, 100–500 Gauss at chamber wall
- **Cathode type**: BaO-impregnated porous tungsten hollow cathode, 1100–1300°C emitter
- **Propellant utilization**: 85–90% (fraction of xenon atoms ionized per pass)
- **Double-ion fraction**: 5–15% (Xe²⁺/Xe⁺ ratio — higher at high discharge currents)

### Radio-Frequency (RF) Ionization

A radio-frequency coil wound around the dielectric discharge chamber (quartz or alumina) inductively couples energy into the gas, creating and sustaining the plasma without a discharge cathode. RF thrusters (e.g., RIT-10, RIT-XT from ArianeGroup) operate at 1–4 MHz and eliminate the discharge cathode entirely — the only cathode is the neutralizer, which carries far less current. This trades PPU complexity (RF oscillator vs DC supply) for longer wear life, since the discharge-side cathode is removed.

### Electron Cyclotron Resonance (ECR)

Microwave power (typically 4.2 GHz) is fed into the discharge chamber where electrons are heated by resonance with a magnetic field (875 Gauss for 4.2 GHz). ECR thrusters (e.g., the µ10 on Hayabusa) require no cathode at all in the discharge chamber — the plasma is sustained entirely by microwave absorption. This eliminates a second wear item, extending mission life indefinitely on paper, but at the cost of very low thrust efficiency at low power levels.

## Acceleration Grids

The ion optics assembly is the heart of the thruster — two or three precisely aligned perforated plates that extract and accelerate ions from the discharge chamber. See [Acceleration Grids](./electric-ion.acceleration-grids.md) for the dedicated process article.

The grid set consists of:

- **Screen grid** (innermost): held at discharge chamber potential (+1000 to +2000 V), defines the plasma boundary and sets the beam current density. Aperture diameter 1–3 mm.
- **Accelerator grid** (middle): held at a negative potential (−100 to −500 V) to prevent electron backstreaming from the beam plasma. Aperture slightly smaller than screen grid.
- **Decelerator grid** (optional, outermost): held at ground potential in three-grid designs; reduces beam divergence and protects the accelerator grid from direct ion impingement.

The grid gap — the distance between screen and accelerator grids — is typically 0.5–1.0 mm, set by insulating standoffs machined to micron tolerance. Too small and the grids risk short-circuiting due to thermal expansion or launch vibration; too large and the electric field weakens, reducing beam current and thrust.

Grid materials and their properties:

| Material | Density (g/cm³) | Max Temp (°C) | Sputter Yield (Xe at 300 eV) | Status |
|----------|-----------------|---------------|------------------------------|--------|
| Molybdenum | 10.2 | 2600 | 0.3 atoms/ion | Flight-proven (NSTAR, NEXT) |
| Titanium | 4.5 | 1700 | 0.5 atoms/ion | Tested (alternatives study) |
| Carbon-carbon | 1.8 | 3500 | 0.1 atoms/ion | Experimental (NEXT-LL) |
| Graphite | 2.1 | 3500 | 0.2 atoms/ion | Ground-tested |
| Tungsten | 19.3 | 3400 | 0.2 atoms/ion | Cathode orifice only |

Grid erosion is the primary lifetime-limiting mechanism. Charge-exchange ions — created when fast beam ions collide with slow neutral xenon atoms — are accelerated into the accelerator grid apertures, sputtering material away grain by grain. Over 30,000 hr, the aperture diameter grows by 10–30%, eventually causing electron backstreaming or structural failure. Grid lifetime models predict erosion rates from first principles using ion trajectory simulation (PIC codes) and validated against long-duration wear tests.

## Power Processing Unit

The PPU converts spacecraft bus power into the multiple isolated, regulated outputs the thruster requires. See [Power Processing Unit](./electric-ion.power-processing-unit.md) for the dedicated process article. Key outputs:

- **Beam supply**: 300–2000 V DC, 1–7 A — the dominant power consumer (70–80% of total input)
- **Discharge supply**: 25–40 V DC, 5–20 A — sustains the discharge chamber plasma
- **Accelerator supply**: −100 to −500 V DC, 1–10 mA — prevents electron backstreaming
- **Neutralizer keeper**: 10–20 V DC, 1–3 A — sustains neutralizer hollow cathode
- **Cathode heater**: 4–10 V DC, 3–8 A — pre-heats cathode emitter before ignition
- **Magnet supply**: 0.5–2 A at 5–20 V — powers electromagnets in variable-thrust designs
- **Inner/outer magnet supplies**: independent current control for beam shaping in advanced designs

PPU efficiency must exceed 90% to avoid dissipating hundreds of watts of waste heat in vacuum, where the only heat rejection path is radiation. The [power electronics](../electronics/power-electronics.md) heritage is directly leveraged: DC-DC converters using radiation-hardened MOSFETs and high-frequency transformers (50–200 kHz) achieve 92–95% efficiency at output voltages above 1000 V. Insulation is critical — the beam supply must hold off 3000 V DC between primary and secondary windings, requiring vacuum-impregnated transformer potting and careful creepage/clearance design.

PPU mass typically accounts for 30–50% of total thruster system mass:

- NSTAR PPU: 4.5 kg for 2.3 kW thruster — power density 0.5 kW/kg
- NEXT PPU: 14 kg for 6.9 kW thruster — power density 0.5 kW/kg
- XIPS-25 PPU: 6.3 kg for 4.5 kW thruster — power density 0.7 kW/kg
- Advanced target: 1 kW/kg (requires wide-bandgap SiC power devices)

## Neutralizer

The neutralizer prevents the spacecraft from accumulating a positive charge as ions leave the thruster. A hollow cathode emits electrons into the ion beam, neutralizing it to prevent beam spreading and spacecraft charging. See [Neutralizer Design](./electric-ion.neutralizer-design.md) for the dedicated process article.

The neutralizer is a small hollow cathode — a tungsten orifice plate with a BaO impregnated emitter insert — that thermionically emits electrons when heated to 1100–1300°C. A keeper electrode sustains the discharge with 10–20 V at 1–3 A. The neutralizer must emit a current equal to the beam current (1–7 A for modern thrusters) to maintain charge neutrality. Neutralizer lifetime is typically the second limiting factor after grid erosion: the BaO emitter depletes over time, and the cathode orifice erodes from ion bombardment.

Neutralizer failure modes:

- **BaO depletion**: emitter insert loses barium over 20,000–30,000 hr, requiring higher keeper voltage
- **Orifice erosion**: ion bombardment widens the tungsten orifice, increasing propellant flow needed
- **Heater failure**: tungsten heater wire degrades from thermal cycling (1000+ on/off cycles)
- **Encapsulation failure**: porous tungsten insert crumbles from vibration or thermal stress
- **Contamination**: propellant impurities (H₂O, O₂ at ppm levels) poison the BaO surface

## Xenon Storage and Feed System

The xenon propellant system stores the gas at high pressure and delivers it to the thruster at a precisely regulated low pressure with flow control to 1% accuracy:

- **Tank**: titanium or composite overwrap pressure vessel, 60–200 bar operating, 20–800 kg xenon capacity
- **Pressure regulator**: mechanical bang-bang or electronic proportional valve, reduces tank pressure to 2–5 bar
- **Flow controller**: thermal mass flow controller or fixed sonic orifice, delivers 1–20 mg/s xenon at ±1% accuracy
- **Isolation latching valves**: pyrotechnic or motorized, isolate tank before and after thruster operation
- **Cross-strapping manifold**: allows either tank to feed either thruster (redundancy for failure tolerance)
- **Fill and drain valve**: ground support equipment interface for loading xenon before launch

Xenon is extracted from liquid air distillation (0.087 ppm in atmosphere), purified to 99.999%, and compressed into flight tanks at $2000–5000/kg. The atmospheric rarity of xenon is the dominant cost driver — global production is approximately 50 tonnes per year. For a Dawn-class mission consuming 425 kg, the xenon alone costs $1–2M.

## Performance Comparison

The following table compares the performance of ion thrusters with other electric propulsion technologies and chemical reference points:

| Technology | Isp (s) | Thrust (mN) | Power (kW) | Efficiency (%) | TRL |
|-----------|---------|-------------|------------|----------------|-----|
| Chemical (bipropellant) | 300–320 | 1–500,000 | — | 85–95 (of chemical) | 9 |
| Chemical (LOX/LH2) | 450–465 | 1–2,500,000 | — | 90–95 (of chemical) | 9 |
| Ion (NSTAR class) | 2500–3100 | 20–92 | 0.5–2.3 | 55–65 | 9 |
| Ion (NEXT class) | 3000–4190 | 50–236 | 1–6.9 | 60–70 | 6 |
| Hall (SPT-100) | 1500–1600 | 40–83 | 0.7–1.35 | 35–45 | 9 |
| Hall (BPT-4000) | 1800–2100 | 168–252 | 3–4.5 | 45–55 | 8 |
| Arcjet (hydrazine) | 500–600 | 110–230 | 0.3–2 | 25–35 | 9 |
| VASIMR (VX-200) | 3000–5000 | 1000–5000 | 30–200 | 50–60 | 5 |
| MPD (pulsed) | 2000–4000 | 1000–10,000 | 100–1000 | 20–40 | 4 |

Ion thrusters occupy the high-Isp, low-thrust corner of this trade space. Their 3000–5000 s Isp enables Δv budgets that no chemical system can match — Dawn's 11 km/s total Δv would require 30,000 kg of chemical bipropellant, but was achieved with 425 kg of xenon. The penalty is thrust: at 92 mN, NSTAR took 1.8 years to spiral Dawn from Vesta to Ceres. For missions where time-to-target is flexible, ion propulsion wins decisively.

## Mission Applications

### North-South Station Keeping (NSSK)

GEO communication satellites use ion thrusters (XIPS-13, XIPS-25, or comparable Hall thrusters) for daily north-south station-keeping maneuvers to counter lunar/solar gravitational perturbations. A typical GEO satellite fires its ion thrusters for 30 minutes per day, consuming 2–5 kg of xenon per year. Over a 15-year mission, this saves 300–500 kg of chemical bipropellant mass — directly translated to additional transponder revenue.

### Orbit Raising

All-electric GEO satellites (e.g., Boeing 702SP, Airbus Eurostar Neo) use ion or Hall thrusters for orbit raising from the transfer orbit to GEO, replacing the 500 kg apogee motor with 50 kg of xenon and a longer transfer time (4–6 months vs 1 week). The 450 kg mass saving translates to additional payload or reduced launch vehicle class.

### Interplanetary Transit

Deep Space 1, Dawn, Hayabusa, Hayabusa2, and BepiColombo all use ion thrusters for primary interplanetary propulsion. The high Isp enables missions to multiple targets (Dawn: Vesta + Ceres), sample return from asteroids (Hayabusa), and missions to Mercury (BepiColombo, where chemical propulsion would require impractical propellant mass). SMART-1 reached lunar orbit using a Hall thruster — 82 kg of xenon for a 17-month spiral from GTO to the Moon.

## Lifetime and Qualification

Ion thruster qualification requires demonstrating the design can survive the mission duration with margin. Key qualification tests:

- **Long-duration wear test**: operate a flight-representative thruster for 1.5× the mission life (e.g., 30,000 hr for a 20,000-hr mission) in a high-vacuum chamber, monitoring thrust, Isp, grid currents, and optical erosion
- **Thermal-vacuum cycling**: subject the thruster to the full thermal range (−100°C to +200°C for typical interplanetary missions) for 100+ cycles
- **Vibration and shock**: sine and random vibration at qualification levels (14 Grms) plus pyrotechnic shock to verify grid structural integrity through launch
- **EMI/EMC**: verify that the high-voltage PPU switching does not interfere with spacecraft communications or science instruments
- **Plume characterization**: measure ion beam profile, charge-exchange plasma density, and sputtered contaminant flux at representative operating conditions
- **Cycling qualification**: demonstrate 1000+ on/off cycles to verify cathode heater and grid thermal cycling fatigue margins

The longest ion thruster life test is the NEXT 51,000-hour demonstration, which processed 800 kg of xenon — the equivalent of a 30-year mission to the outer solar system. Grid erosion was the limiting factor: the accelerator grid aperture grew from 1.14 mm to 1.65 mm (45% increase), with the thruster still operational at test termination. This data directly validates grid lifetime models used to set qualification margins.

### Troubleshooting Guide

| Symptom | Likely Cause | Diagnostic | Remedy |
|---------|-------------|------------|--------|
| Beam current 20%+ below setpoint | Discharge cathode degradation | Monitor discharge voltage trend | Increase discharge current within limits |
| High accel grid current | Grid misalignment or direct ion impingement | Measure perveance margin | Reduce beam voltage or adjust grid spacing |
| Neutralizer keeper voltage rising | BaO emitter depletion or contamination | Track keeper voltage vs. operating hours | Switch to redundant neutralizer |
| Recurring HV breakdown | Grid short from debris or conductive coating | Inspect via optical scope | Increase xenon flow to flush, or cycle HV |
| High discharge pressure | Propellant tank depletion or regulator drift | Check upstream pressure | Switch to backup flow path |
| PPU over-temperature | Converter degradation or radiator contamination | Monitor PPU baseplate temp | Reduce duty cycle or switch to backup PPU |

## Key Parameters Summary

- **Specific impulse**: 1500–5000 s (typical operating range for xenon)
- **Thrust**: 10–250 mN per thruster (scales with beam current and grid area)
- **Total efficiency**: 35–65% (ratio of kinetic beam power to electrical input power)
- **Beam voltage**: 300–2000 V (sets exhaust velocity and Isp)
- **Beam current**: 0.1–12 A (sets thrust)
- **Propellant**: xenon (131.3 g/mol), 2–20 mg/s flow rate
- **Grid gap**: 0.5–1.0 mm (screen to accelerator)
- **Grid material**: molybdenum (primary), carbon-carbon (experimental)
- **Discharge cathode**: BaO hollow cathode, 1100–1300°C, 20,000–30,000 hr life
- **Neutralizer**: BaO hollow cathode, 1–7 A emission, 30,000+ hr life
- **PPU efficiency**: 90–95% (DC-DC conversion, 28–100 V to 300–2000 V)
- **Cycle life**: 1000+ on/off cycles demonstrated
- **Thrust-to-power ratio**: 25–50 mN/kW (improves with scale)
- **Throttle range**: 5:1 demonstrated (NSTAR 0.5–2.3 kW; NEXT 0.5–6.9 kW)
- **Beam divergence**: 10–20° half-angle (95% of beam current within cone)
- **System dry mass**: 8–20 kg per thruster + PPU (scales with power class)
- **Radiation tolerance**: 25–100 krad TID for typical GEO mission doses

## See Also

- [Electric Propulsion — Hall](./electric-hall.md) — the competing electrostatic technology
- [Electric Propulsion — Advanced](./electric-advanced.md) — VASIMR, arcjet, MPD concepts
- [Power Electronics](../electronics/power-electronics.md) — PPU heritage
- [Vacuum Chambers](../vacuum/chambers.md) — ground test infrastructure
- [Refractory Specialty Metals](../metals/refractory-specialty.md) — grid and cathode materials

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
