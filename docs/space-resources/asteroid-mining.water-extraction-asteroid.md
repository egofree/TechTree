# Asteroid Water Extraction

> **Node ID**: space-resources.asteroid-mining.water-extraction-asteroid
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.asteroid-mining`](./asteroid-mining.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: asteroid_water
> **Critical**: No

Water harvesting from hydrated minerals in carbonaceous chondrites (CI/CM class, 5-20% structural water) by stepwise heating to 150-800 C to drive off adsorbed, interlayer, and structurally bound H2O. See [Asteroid Mining](./asteroid-mining.md) for the integrated capability context.

## Overview

Carbonaceous chondrites hold water in three reservoirs, released at progressively higher temperatures. Adsorbed water desorbs at 100-150 C; interlayer water bound between phyllosilicate sheets is driven off at 150-300 C; and structural hydroxyl chemically bound in the mineral lattice requires dehydroxylation at 300-800 C. Crushed regolith is heated in a sealed, solar-concentrator-heated retort; released vapor is captured on a cold finger, purified, and stored as ice or electrolyzed into H2 and O2 propellant. Heating one tonne of CI-chondrite to 800 C requires ~600 MJ of thermal energy.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| C-type (CI/CM) water content | 5-20% by mass |
| Adsorbed water release | 100-150 C |
| Interlayer water release | 150-300 C |
| Structural OH release | 300-800 C |
| Energy to 800 C | ~600 MJ/tonne |
| Electrolysis energy (practical) | ~50 MJ/kg water |

## Prerequisites

- Solar concentrator for retort heating ([energy](../energy/))
- Cryogenic storage and electrolysis ([cryogenics](../cryogenics/))
- Autonomous process control ([automation](../automation/))

## See Also

- [Asteroid Mining](./asteroid-mining.md) — parent capability
- [Extraction Methods](./asteroid-mining.extraction-methods.md) — metal recovery
- [Asteroid Prospecting](./asteroid-mining.prospecting.md) — hydration mapping

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md)*
