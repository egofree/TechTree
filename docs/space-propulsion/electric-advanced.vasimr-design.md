# VASIMR Design

> **Node ID**: space-propulsion.electric-advanced.vasimir-design
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.electric-advanced`](./electric-advanced.md)
> **Enables**: None
> **Timeline**: Years 50-200+
> **Outputs**: advanced_thrusters
> **Critical**: No

VASIMR (Variable Specific Impulse Magnetoplasma Rocket) is an electrodeless plasma thruster that uses RF power to generate, heat, and accelerate an argon plasma through a magnetic nozzle. Its defining feature is **variable Isp** — the ability to trade thrust for Isp in real time by adjusting the power split between the helicon plasma generation stage and the ion cyclotron heating (ICH) stage. The VX-200 prototype demonstrated 5 N thrust at 200 kW input power, the highest thrust of any electric propulsion device tested in vacuum. See [Electric Propulsion — Advanced](./electric-advanced.md) for the integrated context.

## Process Description

1. **Helicon plasma generation**: a 30 MHz RF helicon antenna wraps the dielectric tube (quartz) and ionizes argon gas to a dense plasma (10¹⁸–10¹⁹ m⁻³) — no electrodes contact the plasma.
2. **Superconducting magnet assembly**: high-temperature superconducting (HTS) coils (YBCO or Bi-2212) generate a 0.5 T axial field that confines the plasma column and shapes the magnetic nozzle.
3. **Ion cyclotron heating (ICH)**: a second RF antenna at 0.5–3 MHz excites ions at their cyclotron resonance in the magnetic field, transferring perpendicular thermal energy to the ion population.
4. **Magnetic nozzle acceleration**: the heated plasma expands adiabatically along the diverging magnetic field lines, converting thermal energy to directed kinetic energy. The "nozzle" is purely magnetic — no material surface contacts the plasma.
5. **Variable Isp control**: adjusting the power split between helicon (thrust) and ICH (Isp) stages tunes the exhaust velocity from 3000 s (high thrust) to 5000 s (high Isp).

## Key Parameters

- **Input power**: 30–200 kW (VX-200 demonstrator)
- **Helicon frequency**: 30 MHz (plasma generation, 30 kW)
- **ICH frequency**: 0.5–3 MHz (ion heating, 170 kW)
- **Propellant**: argon (39.9 g/mol), 50–100 mg/s
- **Thrust**: 0.5–5 N (variable)
- **Isp**: 3000–5000 s (variable in flight)
- **Efficiency**: 50–60% (RF input to thrust power)
- **Magnetic field**: 0.5 T throat (superconducting magnet)
- **Plasma density**: 10¹⁸–10¹⁹ m⁻³

## Prerequisites

- High-power RF generation (30 MHz and 0.5–3 MHz)
- Superconducting magnet technology (HTS coils, cryogenic cooling)
- High-vacuum test facility (>100 kW propellant throughput)

## See Also

- [Electric Propulsion — Advanced](./electric-advanced.md) — parent capability
- [Arcjet Design](./electric-advanced.arcjet-design.md) — competing electrothermal concept
- [Magnetoplasmadynamic](./electric-advanced.magnetoplasmadynamic.md) — competing electromagnetic concept

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
