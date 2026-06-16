# Thruster Control

> **Node ID**: spacecraft-systems.adcs.thruster-control
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.adcs`](./adcs.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: adcs_hardware
> **Critical**: No

Thrusters provide the highest-authority attitude control torque, but consume finite propellant. They are used for momentum dumping when magnetorquers are unavailable, large-angle slew manoeuvres, and orbit-adjust burns where attitude must be maintained during thrusting. See [ADCS](./adcs.md) for the integrated control system context.

## Overview

Two propellant systems dominate spacecraft attitude thrusters:

**Cold gas (N₂)**: Stored nitrogen is released through a solenoid valve and nozzle. Specific impulse is ~65 seconds. Thrust ranges from 0.1–10 N. The system is simple, non-toxic, and non-reactive — ideal for cubesats and cost-sensitive LEO constellations. Cold gas thrusters also serve as backup attitude control when reaction wheels fail.

**Monopropellant (hydrazine, N₂H₄)**: Liquid hydrazine is sprayed onto a hot iridium catalyst bed, decomposing exothermically into hot nitrogen and hydrogen gas. Specific impulse is ~220 seconds. Thrust ranges from 1–500 N. Hydrazine is the workhorse for medium and large satellites but is highly toxic, requiring sealed handling facilities and contamination controls.

Attitude thrusters fire in short pulses (10–100 ms) to approximate continuous torque via pulse-width modulation. The **minimum impulse bit** (MIB) — the smallest torque-time product the thruster can deliver — sets the pointing resolution. A 1 N thruster with a 10 ms MIB produces a 0.01 N·s impulse, which is 3 orders of magnitude coarser than a reaction wheel. For this reason, thrusters are used for coarse control and momentum dumping, not fine pointing.

## Key Parameters

| Parameter | Cold Gas (N₂) | Monopropellant (N₂H₄) |
|-----------|---------------|----------------------|
| Specific impulse | ~65 s | ~220 s |
| Thrust range | 0.1–10 N | 1–500 N |
| Minimum impulse bit | 0.001–0.01 N·s | 0.01–0.1 N·s |
| Valve cycle life | >100,000 | >100,000 |
| Propellant toxicity | None | High (TLV 0.01 ppm) |

## Prerequisites

- Propellant storage and feed system manufacturing
- Solenoid valve design and qualification
- Catalyst bed (for monopropellant hydrazine)
- Pulse-width modulation control electronics

## See Also

- [ADCS](./adcs.md) — parent capability and momentum management
- [Reaction Wheels](./adcs.reaction-wheels.md) — primary fine-pointing actuator
- [Magnetorquers](./adcs.magnetorquers.md) — propellant-free momentum dumping

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
