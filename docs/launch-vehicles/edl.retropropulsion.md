# Retropropulsion

> **Node ID**: `launch-vehicles.edl.retropropulsion`
> **Domain**: [Launch Vehicles](./index.md)
> **Parent**: [Entry, Descent & Landing](./edl.md)
> **Outputs**: landing_burn_profiles, recovered_boosters
> **Timeline**: Years 30-200+

## Overview

Retropropulsion uses rocket engines firing opposite to the velocity vector to decelerate a vehicle
for landing. It is the only EDL technique that functions in vacuum (no atmosphere for parachutes)
and is essential for high-mass landings where parachute canopies would be impractically large.
Retropropulsive landing was demonstrated at scale by SpaceX starting in 2015 and is now the
baseline for reusable first stages and large planetary landers.

## Falcon 9 Booster Recovery

The Falcon 9 first-stage recovery sequence uses three propulsive burns:

1. **Boost-back burn** (~70 km altitude): Three Merlin engines reignite to cancel downrange
   velocity and steer the stage back toward the landing zone. Cold-gas nitrogen thrusters flip
   the stage to engines-first orientation.
2. **Entry burn** (~40 km altitude): Three engines reignite for ~20 s, dissipating kinetic energy.
   The supersonic exhaust plume acts as a heat shield — deflecting the bow shock and reducing
   aft-end heating by 80-90%.
3. **Landing burn** (~4 km altitude): A single centre engine reignites for final deceleration.
   The guidance system commands a variable-thrust "hoverslam" — throttling to reach exactly zero
   velocity at zero altitude. Grid fins (titanium lattice control surfaces) provide aerodynamic
   steering during descent to sub-metre landing accuracy.

The stage touches down on four deployable carbon-fibre legs at 1-2 m/s vertical velocity on a
landing pad or autonomous droneship.

## Supersonic Retropropulsion: Starship

Starship extends retropropulsion to the full vehicle — both Super Heavy booster and Starship upper
stage recover propulsively. The EDL profile is unique: the vehicle enters **belly-first**
(horizontal) to maximise aerodynamic drag, using four body flaps for pitch/roll control during
hypersonic and supersonic flight. At ~1-2 km altitude, the vehicle performs a **belly-flip
manoeuvre** — rotating from horizontal to vertical in ~20 seconds via differential engine ignition
and RCS. Raptor engines then ignite for the landing burn.

Supersonic retropropulsion (firing engines into a supersonic freestream) was previously considered
infeasible — plume-shock interactions were expected to destabilise the vehicle. SpaceX's test
campaign (Grasshopper 2012 → Falcon 9 booster recoveries 2015-present) demonstrated that the plume
creates a stable aerodynamic wake, opening a new EDL regime for heavy vehicles.

## Key Parameters

| Parameter | Falcon 9 booster | Starship (target) |
|-----------|-----------------|-------------------|
| Entry burn engines | 3 × Merlin | 6 × Raptor |
| Landing burn engines | 1 × Merlin | 3 × Raptor |
| Landing accuracy | <1 m | <1 m |
| Stage mass at touchdown | ~25 t | ~120 t (booster) |

## See Also

- [Entry, Descent & Landing](./edl.md) — parent capability
- [Precision Landing](./edl.precision-landing.md) — navigation for landing burns
- [Liquid Propulsion](../launch-vehicles/index.md) — Merlin/Raptor engines

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
