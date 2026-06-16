# Zero Boil-Off Systems

> **Node ID**: space-propulsion.propellant-storage.zero-boiloff-systems
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.propellant-storage`](./propellant-storage.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: orbital_cryogenic_storage
> **Critical**: No

Zero boil-off (ZBO) eliminates cryogenic propellant loss by actively removing heat leak with a cryocooler. The cooler maintains the tank wall at or below the propellant boiling point, so no liquid evaporates. See [Cryogenic Propellant Storage & Transfer](./propellant-storage.md) for the full context.

## Overview

A ZBO system consists of a cryocooler (Stirling, pulse-tube, or Brayton cycle), a thermal interface coupling the cooler cold head to the tank wall, and a radiator that rejects the waste heat to deep space. The cryocooler input power and radiator area scale directly with the residual heat leak through the tank's MLI insulation.

## Key Parameters

| Parameter | LOX (90 K) | LH2 (20 K) |
|-----------|-----------|------------|
| Cooling power needed | 0.5-5 W | 1-10 W (large tanks: 50-500 W) |
| Cryocooler type | Stirling / Pulse-tube | Pulse-tube / Brayton |
| Carnot efficiency | 15-30% | 5-15% |
| Electrical input | 10-100 W | 100 W - 26 kW |
| Achievable boil-off | <0.1% / day | <0.1% / day |

## Prerequisites

- [Cryogenics — Liquefaction & Storage](../cryogenics/liquefaction-storage.md) for cryocooler heritage
- MLI insulation system installed and qualified
- Solar power system sized for cryocooler continuous load
- Radiator surface area for heat rejection at ~300 K

## See Also

- [Cryogenic Propellant Storage & Transfer](./propellant-storage.md) — parent capability
- [Long-Duration Storage](./propellant-storage.long-duration-storage.md) — depot architecture
- [Propellant Transfer](./propellant-storage.propellant-transfer.md) — transfer operations

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
