# Lightning Protection Systems

> **Node ID**: space-ground-ops.launch-complex.lightning-protection
> **Domain**: [Space Ground Operations](./index.md)
> **Dependencies**: [`space-ground-ops.launch-complex`](./launch-complex.md)
> **Enables**: None
> **Timeline**: Years 50+
> **Outputs**: launch_pads
> **Critical**: No

The lightning protection system intercepts cloud-to-ground strikes before they reach the launch vehicle. At LC-39A/B, three 181m-tall fiberglass lattice towers (north, south, west of the pad) support a catenary network of 2.5cm stainless steel cables forming a 2:1 sag-to-span catenary 60m above the pad deck. The fiberglass towers are non-conductive, forcing any descending stepped leader to attach to the catenary instead of the metallic gantry or vehicle. Each tower's down conductor is a 4/0 AWG copper cable bonded to a 400m-circumference buried counterpoise ring with 24 driven ground rods (8m deep each), achieving ≤5 Ω ground resistance. The system is designed for the 98th-percentile strike (200 kA peak current). NASA's lightning launch commit criteria, developed after Apollo 12 was struck in flight (November 14, 1969), prohibit launch if any cloud-to-ground strike occurs within 10 nautical miles in the prior 30 minutes or if the electric field exceeds 1,000 V/m within 5 nautical miles.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Tower height (LC-39A/B) | 181 m (fiberglass lattice) |
| Tower material | Non-conductive fiberglass |
| Catenary cable diameter | 25 mm stainless steel |
| Catenary height above pad deck | ~60 m |
| Cone of protection radius | ~150 m |
| Down conductor | 4/0 AWG copper, 4 parallel per tower |
| Ground counterpoise | 400m circumference, #2/0 copper ring |
| Ground rods | 24 × 8m deep per tower |
| Ground resistance | ≤ 5 Ω |
| Design strike current | 200 kA (98th percentile) |
| Launch commit distance | 10 nautical miles (any CG strike, 30 min) |

## Process Overview

1. **Foundation**: Pour tower bases; install counterpoise ring with 24 ground rods per tower
2. **Tower erection**: Stack 181m fiberglass lattice sections; tension guy wires
3. **Catenary stringing**: Hoist 2.5cm stainless cable between tower tops; set 2:1 sag
4. **Bonding**: Connect catenary to down conductors; verify ≤5 Ω to ground
5. **Field mill network**: Install 30+ electric field mills within 5 nmi; integrate with LCC

## Prerequisites

- Launch Complex capability (parent)
- Tall-tower construction and high-voltage grounding expertise
- Fiberglass structural fabrication (non-conductive towers)

## See Also

- [Launch Complex](./launch-complex.md) — parent capability
- [Construction](../construction/index.md) — foundation and tower erection heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Ground Operations](./index.md)*
