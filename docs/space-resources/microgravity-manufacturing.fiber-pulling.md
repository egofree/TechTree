# ZBLAN Fiber Pulling

> **Node ID**: space-resources.microgravity-manufacturing.fiber-pulling
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.microgravity-manufacturing`](./microgravity-manufacturing.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: zblan_fiber
> **Critical**: No

Pulling of heavy-metal fluoride glass optical fiber (ZBLAN) in microgravity, suppressing the convection-seeded crystallization that limits terrestrial fiber to 10-100x higher attenuation than the 0.0011 dB/km theoretical minimum. See [Microgravity Manufacturing](./microgravity-manufacturing.md) for the integrated capability context.

## Overview

ZBLAN (ZrF4-BaF2-LaF3-AlF3-NaF) is transparent from ~250 nm to ~7 micron, far beyond silica's ~2 micron window. Its theoretical minimum attenuation is 0.0011 dB/km at 2.5 micron, versus 0.16 dB/km for silica at 1.55 micron. Terrestrial ZBLAN never reaches this floor because buoyancy-driven convection in the melt seeds microcrystallites that scatter light. In microgravity, the melt is quiescent and the drawn fiber approaches the theoretical limit. A preform (10-30 mm diameter) is heated to its ~300-400 C softening point and drawn through a die into 125 micron fiber, immediately coated with UV-cured acrylate.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| ZBLAN theoretical attenuation | 0.0011 dB/km @ 2.5 micron |
| Silica attenuation (comparison) | 0.16 dB/km @ 1.55 micron |
| Draw temperature | 300-400 C |
| Fiber diameter | 125 micron |
| Transmission window | ~250 nm to ~7 micron |
| Improvement factor | 10-100x over silica |

## Prerequisites

- High-purity ZBLAN glass preforms ([glass](../glass/))
- Pressurized orbital platform ([spacecraft systems](../spacecraft-systems/))
- Precision draw tower and tension control ([precision-motion](../precision-motion/))

## See Also

- [Microgravity Manufacturing](./microgravity-manufacturing.md) — parent capability
- [Crystal Growth](./microgravity-manufacturing.crystal-growth.md) — melt solidification
- [Additive Manufacturing](./microgravity-manufacturing.additive-manufacturing.md) — polymer processing

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md)*
