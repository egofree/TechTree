# Heat Shield Design

> **Node ID**: `launch-vehicles.edl.heat-shield-design`
> **Domain**: [Launch Vehicles](./index.md)
> **Parent**: [Entry, Descent & Landing](./edl.md)
> **Outputs**: heat_shields, ablative_tps, reusable_tiles
> **Timeline**: Years 30-200+

## Overview

The heat shield — more formally the Thermal Protection System (TPS) — is the barrier between the
vehicle structure and the extreme aerothermal environment of atmospheric entry. Peak heat fluxes
range from 100 W/cm² (LEO return) to 3,000 W/cm² (lunar return); surface temperatures reach
1,200-2,900°C. The TPS must absorb, reradiate, or ablate this energy while keeping the underlying
structure below its thermal limit (~175°C for aluminium, ~350°C for titanium).

## Ablative TPS: PICA

**PICA (Phenolic Impregnated Carbon Ablator)** is the leading high-energy ablative. It is a
low-density carbon-fibre substrate (Precarbon felt) impregnated with phenolic resin. As the surface
heats, the resin pyrolyses — decomposing into a porous char and releasing pyrolysis gases that
blow into the boundary layer, thickening it and reducing convective heating. The char layer
recedes (ablates) at typically 0.1-0.5 mm/s, carrying heat away with the ablated material.

| Parameter | PICA | PICA-X (SpaceX) | Apollo AVcoat |
|-----------|------|-----------------|---------------|
| Density | 0.27 g/cm³ | 0.27 g/cm³ | 0.50 g/cm³ |
| Max temperature | 2,900°C | 2,900°C | ~2,800°C |
| Reuse target | Single-use | 10+ flights | Single-use |

PICA flew on Stardust (12.9 km/s comet-sample return) and Mars Science Laboratory. SpaceX's
PICA-X is a higher-performance, lower-cost variant engineered for multiple reuses on the Dragon
capsule.

## Reusable TPS: Shuttle Tiles

The Space Shuttle used **LI-900 silica tiles** — 90% porous amorphous silica, density 0.14 g/cm³.
The surface is coated with a high-emissivity borosilicate glass (RCG) that radiates 85-90% of
incident heat back to the atmosphere. Tiles are extremely effective thermal insulators (surface
glows at 1,260°C while the aluminium airframe stays below 175°C) but are mechanically fragile
(compressive strength 0.6 MPa — cracked by rain or debris impact). Starship uses hexagonal tiles
bonded to a transpiration-cooled backing for a more robust reusable TPS.

## Selection Criteria

The TPS material is selected by matching the entry environment to the material's capability:

| Environment | Peak q̇ (W/cm²) | Recommended TPS |
|-------------|----------------|-----------------|
| LEO return | 100-300 | PICA, PICA-X, or reusable tiles |
| Lunar return | 500-1,000 | PICA, AVcoat |
| Mars entry | 200-500 | PICA, SLA-561V |
| Reusable LEO (Shuttle/Starship) | 100-200 | Silica tiles, metallic TPS |

## See Also

- [Entry, Descent & Landing](./edl.md) — parent capability
- [Ceramics](../ceramics/index.md) — PICA substrate, silica tiles
- [Polymers](../polymers/index.md) — phenolic resin binders

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
