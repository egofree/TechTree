# Crystal Growth

> **Node ID**: space-resources.microgravity-manufacturing.crystal-growth
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.microgravity-manufacturing`](./microgravity-manufacturing.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: space_grown_crystals
> **Critical**: No

Growth of large, low-defect protein crystals (lysozyme, insulin) for pharmaceutical structure determination and higher-purity semiconductor crystals free of buoyancy-driven dopant striations. See [Microgravity Manufacturing](./microgravity-manufacturing.md) for the integrated capability context.

## Overview

In microgravity, the absence of buoyancy-driven convection simplifies crystal growth to pure diffusion. Protein crystals (lysozyme, insulin, membrane proteins) grow up to 10-50x larger in volume with lower mosaic spread, enabling higher-resolution X-ray crystallography for structure-based drug design — over 50 distinct proteins have been grown on the Shuttle and ISS. Semiconductor crystals (silicon, germanium) benefit from striation-free dopant distribution: terrestrial Czochralski Si shows +/- 5-10% radial resistivity variation, while microgravity-grown Si achieves +/- 1-2%. Float-zone growth in microgravity reaches oxygen concentrations below 10^15 atoms/cm^3, two orders of magnitude below crucible-grown material.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Protein crystal size gain | up to 10-50x volume |
| Lysozyme resolution gain | ~0.5 angstrom |
| Microgravity level | 10^-6 to 10^-3 g |
| Si radial resistivity (1 g) | +/- 5-10% |
| Si radial resistivity (micro-g) | +/- 1-2% |
| Float-zone Si oxygen | <10^15 atoms/cm^3 |

## Prerequisites

- High-purity melt stock and seed crystals ([silicon](../silicon/))
- X-ray diffraction analysis for structure ([optics](../optics/))
- Pressurized orbital platform ([spacecraft systems](../spacecraft-systems/))

## See Also

- [Microgravity Manufacturing](./microgravity-manufacturing.md) — parent capability
- [ZBLAN Fiber Pulling](./microgravity-manufacturing.fiber-pulling.md) — glass melt processing
- [Additive Manufacturing](./microgravity-manufacturing.additive-manufacturing.md) — polymer processing

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md)*
