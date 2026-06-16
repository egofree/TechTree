# Solid Propellant Mixing

> **Node ID**: `launch-vehicles.propellant-production.solid-propellant-mixing`
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.propellant-production`](./propellant-production.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: solid_propellant_grains
> **Critical**: No

## Overview

Composite solid propellants are mechanical mixtures of oxidizer, fuel, and binder cast as a single grain inside a rocket motor casing. The standard formulation is AP/Al/HTPB: ammonium perchlorate (AP, 65-70% by mass) as oxidizer, aluminum powder (Al, 14-18%) as fuel, and hydroxyl-terminated polybutadiene (HTPB, 10-14%) as binder. Solid motors deliver high thrust immediately upon ignition, making them ideal for strap-on boosters and strategic missiles.

See the parent capability [Propellant Production](propellant-production.md) for hazard classification, TNT equivalence, and quality control defect types.

## Process Description

1. **Raw material preparation**: AP is ground and classified by particle size (typically bimodal: 200 µm coarse and 5-10 µm fine for burning rate control). Aluminum powder (spherical, 5-30 µm) is screened. HTPB binder, plasticizer (DOA or IDP), and curative (IPDI) are mixed as the binder prep.
2. **Mixing**: AP, aluminum, and binder prep are combined in a vertical planetary mixer under vacuum (<5 mbar). Vacuum eliminates trapped air bubbles that would create combustion voids. Mixing time: 60-120 minutes. The mixer is operated remotely from behind a blast wall.
3. **Casting**: The mixed propellant (now a viscous slurry) is poured or vacuum-injected into the motor casing, which is pre-lined with insulation and fitted with a mandrel that shapes the internal grain geometry (core pattern controls burn area vs. time).
4. **Curing**: The cast grain is heated to 50-60°C for 3-7 days. The curative crosslinks the HTPB polymer, transforming the slurry into a rubbery solid.
5. **Mandrel removal and inspection**: The mandrel is extracted. The grain is X-ray inspected for voids, ultrasonically scanned for bond integrity, and the surface is inspected for cracks.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| AP content | 65-70% by mass |
| Aluminum content | 14-18% by mass |
| HTPB binder + additives | 10-14% by mass |
| Theoretical Isp (sea level) | 250-285 s |
| Burning rate (typical) | 6-15 mm/s at 7 MPa |
| Hazard class | 1.1 (mass detonation) or 1.3 (mass fire) |

## Safety

Solid propellant mixing is the most dangerous operation in launch vehicle manufacturing. The propellant is ignitable by friction, spark, or impact throughout the mixing and casting process. All equipment is conductive and grounded. Personnel wear static-dissipative clothing and footwear. The mixer and cast rooms are designed with blowout panels that vent upward to prevent propagation to adjacent areas.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [Propellant Production](propellant-production.md)*
