# Additive Manufacturing

> **Node ID**: space-resources.microgravity-manufacturing.additive-manufacturing
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.microgravity-manufacturing`](./microgravity-manufacturing.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: space_products
> **Critical**: No

Fused-filament additive manufacturing of polymer parts aboard pressurized orbital platforms, leveraging microgravity to print 30+ polymer feedstocks without the sag and support constraints of terrestrial printing. See [Microgravity Manufacturing](./microgravity-manufacturing.md) for the integrated capability context.

## Overview

The Made In Space Additive Manufacturing Facility (AMF), operational aboard the ISS from 2016, was the first commercial 3D printer in orbit. It extrudes polymer filament (ABS, Ultem/PEI, HDPE, polycarbonate, and 30+ other feedstocks) through a heated head at 160-300 C, depositing layers onto a build plate. In microgravity the printed strand holds its shape by surface tension, eliminating the need for support scaffolding on overhangs and enabling 20-40% mass reduction versus terrestrial prints. The Refabricator (2019) extended this with closed-loop recycling of printed Ultem back into filament, with <10% property loss per cycle.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| AMF build volume | 100 x 100 x 100 mm |
| Feedstocks demonstrated | 30+ polymers |
| Extrusion temperature | 160-300 C |
| Mass saving (support-free) | 20-40% |
| Recycling property loss | <10% per cycle |
| Notable prints | 200+ parts, tools, brackets |

## Prerequisites

- Polymer filament feedstock ([polymers](../polymers/))
- Pressurized orbital platform ([spacecraft systems](../spacecraft-systems/))
- Thermal control and power ([energy](../energy/))

## See Also

- [Microgravity Manufacturing](./microgravity-manufacturing.md) — parent capability
- [ZBLAN Fiber Pulling](./microgravity-manufacturing.fiber-pulling.md) — glass processing
- [Crystal Growth](./microgravity-manufacturing.crystal-growth.md) — crystal processing

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md)*
