# Propeller Integration

> **Node ID**: aerospace.turboprop.propeller-integration
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.turboprop`](turboprop.md)
> **Timeline**: Years 30-50+
> **Outputs**: turboprop_engines
> **Critical**: No

The propeller integration process covers the coupling of a gas turbine power turbine to a propeller through a reduction gearbox, along with the constant-speed governor, torque metering, and propeller control systems that make the combination controllable across the flight envelope. This is the defining engineering step that converts a turboshaft gas generator into a turboprop engine.

The central challenge is the speed mismatch: the power turbine runs at 20,000-40,000 RPM for peak aerodynamic efficiency, while the propeller must stay below 1,200-2,500 RPM to avoid tip supersonic conditions. A reduction ratio of 10:1 to 25:1 must be achieved in one or two gear stages while transmitting 500 to 15,000 shaft horsepower. Planetary (epicyclic), double-planetary, and offset helical gear configurations are used depending on engine size and whether a coaxial propeller mounting is required.

## Key Subsystems

- **Reduction gearbox** — gear train, bearings, independent oil system with pressure pump, scavenge pump, cooler, and filter
- **Constant-speed governor** — centrifugal flyweight device that varies blade pitch to hold propeller RPM constant across power settings
- **Beta and reverse range** — ground-mode pitch control below the flight fine-pitch stop, enabling taxi speed control and reverse thrust
- **Torque meter** — hydraulic or strain-gauge sensor measuring shaft torque for engine trend monitoring and automatic power management
- **Propeller synchronization** — electronic or mechanical interlink on multi-engine aircraft to phase propeller blades and reduce cabin beat frequency noise

## Prerequisites

- [Turboprop Engines](turboprop.md) — parent capability providing the gas generator core
- [Gas Turbines](../energy/gas-turbine.md) — turbomachinery foundation for the power turbine
- [Machine Tools](../machine-tools/index.md) — precision gear hobbing and grinding capability
- [Aluminum](../metals/aluminum.md) — gearbox housings and structural components

## See Also

- [Turboprop Engines](turboprop.md) — parent capability overview
- [Jet Propulsion](jet-propulsion.md) — Brayton cycle turbomachinery heritage
- [Gas Turbines](../energy/gas-turbine.md) — turbomachinery foundation

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
