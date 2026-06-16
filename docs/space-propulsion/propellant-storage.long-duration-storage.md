# Long-Duration Storage

> **Node ID**: space-propulsion.propellant-storage.long-duration-storage
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.propellant-storage`](./propellant-storage.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: propellant_depot
> **Critical**: No

Long-duration storage is the architecture and insulation strategy that allows cryogenic propellant to be aggregated and held over months to years — the foundation of any orbital propellant depot. See [Cryogenic Propellant Storage & Transfer](./propellant-storage.md) for the full thermal analysis.

## Overview

Long-duration storage integrates MLI insulation, tank material selection, vapor-cooled shields, and (optionally) ZBO cryocoolers into a unified thermal architecture. The goal is to minimize the boil-off floor — the rate below which the depot cannot operate economically. A depot that loses propellant faster than tankers can deliver it will never accumulate enough fuel for a Mars mission.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Tank diameter | 4-10 m | Larger tanks have lower surface-area-to-volume ratio |
| MLI layers | 30-60 | Diminishing returns past 40 layers |
| MLI heat leak | 0.5-5 W/m² | Realistic with seams and penetrations |
| Tank material | Al-Li 2195, COPV, 304L SS | Trades mass, cost, fracture toughness |
| Ullage pressure | 0.2-0.5 MPa | Set by vent relief valve cracking pressure |

## Prerequisites

- [Cryogenics — Liquefaction & Storage](../cryogenics/liquefaction-storage.md) for Dewar tank heritage
- [Metals](../metals/index.md) for Al-Li and steel tank fabrication
- [Vacuum](../vacuum/index.md) technology for MLI vacuum jackets
- Thermal math model correlated to ground-test data

## See Also

- [Cryogenic Propellant Storage & Transfer](./propellant-storage.md) — parent capability
- [Zero Boil-Off Systems](./propellant-storage.zero-boiloff-systems.md) — active cooling integration
- [Liquid Propulsion](../launch-vehicles/liquid-propulsion.md) — propellant consumer

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
