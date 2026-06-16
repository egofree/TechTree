# Launch Abort Systems

> **Node ID**: `human-spaceflight.crewed-spacecraft.launch-abort-systems`
> **Domain**: [Human Spaceflight](./index.md)
> **Parent**: [Crewed Spacecraft](./crewed-spacecraft.md)
> **Dependencies**: [`human-spaceflight.crewed-spacecraft`](./crewed-spacecraft.md)
> **Outputs**: launch_abort_systems, escape_towers, abort_motors
> **Timeline**: Years 50-200+

## Overview

A launch abort system (LAS) pulls the crew capsule clear of a failing launch vehicle within
1-2 seconds — before the rocket explodes — while imposing 6-15 g on the crew for 2-6 seconds.
It must work from the pad (zero velocity) through Max-Q (maximum dynamic pressure) to orbit
insertion.

## Architectures

| LAS | Type | Thrust | Peak g |
|-----|------|--------|--------|
| Apollo LES | solid escape tower | 680 kN | ~7 g |
| Soyuz SAS | solid escape tower | 730 kN | 10-14 g (ballistic) |
| Crew Dragon | integrated pusher (SuperDraco) | 8 x 73 kN = 584 kN | 4-6 g |
| Orion LAS | solid escape tower | 1,800 kN | ~7-10 g |

**Escape-tower LAS**: solid motor on a tower above the capsule, pulls up and away, jettisoned
after Max-Q. **Pusher LAS**: engines integrated into the capsule sidewall, push the capsule
off the booster — no tower to jettison, engines reusable, abort-to-orbit possible.

## Load Path

The abort thrust transmits through the capsule's structural frame into the crew couches. The
couches are reclined to take g-load along the spine (eyeballs-in), the tolerable direction.
Couch foam and restraint straps absorb peak spikes.

## Heritage

Soyuz T-10-4 (1983) pad abort: rocket caught fire, SAS fired, capsule thrown 2 km clear, crew
survived. Crew Dragon in-flight abort test (2020): Falcon 9 destroyed deliberately, capsule
recovered intact under parachutes.

## See Also

- [Crewed Spacecraft](./crewed-spacecraft.md) — parent capability
- [Crew Cabin Design](./crewed-spacecraft.crew-cabin.md) — cabin structural load path
- [Launch Vehicles](../launch-vehicles/index.md) — booster interface

---

*Part of the [Bootciv Tech Tree](../index.md) • [Human Spaceflight](./index.md) • [All Domains](../index.md)*
