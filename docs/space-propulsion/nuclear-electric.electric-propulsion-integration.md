# Electric Propulsion Integration

> **Node ID**: space-propulsion.nuclear-electric.electric-propulsion-integration
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.nuclear-electric`](./nuclear-electric.md)
> **Enables**: nep_systems
> **Timeline**: Years 40-200+
> **Outputs**: nep_systems
> **Critical**: No

Electric propulsion integration is the engineering of coupling the reactor's electrical output to a cluster of ion or Hall thrusters — the power conditioning, distribution, gimballing, and xenon feed that turns kilowatts of bus power into millinewtons to newtons of thrust at 3000-7000 s Isp. A 100 kWe NEP vehicle carries 8-15 ion thrusters (or 5-8 Hall thrusters), each with its own power-processing unit (PPU) and gimbal, ganged in parallel to share the reactor bus. This process is part of the [Nuclear Electric Propulsion](./nuclear-electric.md) capability.

## Thruster Families

- **Ion thrusters** — xenon ionised and accelerated through electrostatic grids at 20-40 kV. Isp 3000-7000 s, thrust 0.05-0.5 N per thruster. Heritage: NSTAR (Deep Space 1), NEXT (Dawn)
- **Hall thrusters** — xenon ionised in radial magnetic field, accelerated through Hall current at 150-400 V. Isp 1500-3000 s, thrust 0.1-1 N. Heritage: SPT-100, AEPS (Gateway PPE)

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Bus voltage | 100-1000 V DC |
| PPU efficiency | 90-95% |
| PPU specific mass | 3-5 kg/kWe (target 1-2 kg/kWe with SiC) |
| Thruster array mass | 8-12 kg/kWe total |
| Xenon tankage fraction | 6% of propellant mass |
| Total system Isp | 3000-7000 s (thruster-limited) |

## Prerequisites

- [Silicon](../silicon/index.md) — power semiconductors (SiC MOSFETs, diodes) for high-voltage PPUs
- [Metals](../metals/index.md) — thruster structures, gimbals, cabling
- Xenon or krypton propellant (chemistry)

## See Also

- [Nuclear Electric Propulsion](./nuclear-electric.md) — the parent capability
- [Reactor Power Conversion](./nuclear-electric.reactor-power-conversion.md) — the source of the bus power

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md) • [All Domains](../index.md)*
