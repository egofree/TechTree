# Reentry Systems

> **Node ID**: `human-spaceflight.crewed-spacecraft.reentry-systems`
> **Domain**: [Human Spaceflight](./index.md)
> **Parent**: [Crewed Spacecraft](./crewed-spacecraft.md)
> **Dependencies**: [`human-spaceflight.crewed-spacecraft`](./crewed-spacecraft.md)
> **Outputs**: reentry_systems, crew_heat_shields, recovery_systems
> **Timeline**: Years 50-200+

## Overview

Reentry systems return a crew capsule from orbital or lunar return velocity to a survivable
landing. The challenge is energy management: a capsule returning from LEO at 7.8 km/s carries
30 MJ of kinetic energy per kilogram; lunar return at 11 km/s carries 60 MJ/kg. That energy
must be dissipated as heat into the atmosphere or the thermal protection system.

## Heat Shield Materials

| Shield | Type | Used on | Heat flux |
|--------|------|---------|-----------|
| Avcoat | ablative (epoxy-phenolic honeycomb) | Apollo CM, Orion | ~2,500 W/cm2 (lunar) |
| PICA-X | ablative (phenolic-impregnated carbon) | Crew Dragon, Stardust | ~2,500 W/cm2 (lunar-rated) |
| Soyuz ablator | ablative (phenolic-asbestos) | Soyuz | ~1,500 W/cm2 (LEO) |
| Hex tiles | reusable ceramic | Starship (in development) | Target: 10+ flights (PICA-X, in qualification) |

## Trajectory and G-Load

A **lifting** reentry (capsule generates lift by offset centre of mass) is shallow, long, and
gentle (3-4 g from LEO, 4-5 g from lunar return). A **ballistic** reentry (no lift) is steep,
short, and violent (8-9 g from LEO). The Soyuz ballistic fallback spikes to 8-9 g —
uncomfortable but survivable.

## Recovery

- **Parachutes**: Crew Dragon uses 4 Mark 3 nylon ringsails (two-out redundancy); Soyuz uses
  1 drogue + 1 main with solid retrorockets firing 0.8 m above ground for 1-2 m/s touchdown.
- **Propulsive**: Starship (in development) lands propulsively on its own engines — no
  parachutes, no ocean splashdown.
- **Couches**: custom-moulded to distribute g-load along the spine (eyeballs-in).

## See Also

- [Crewed Spacecraft](./crewed-spacecraft.md) — parent capability
- [Launch Vehicles EDL](../launch-vehicles/edl.md) — shared reentry heritage
- [Crew Cabin Design](./crewed-spacecraft.crew-cabin.md) — couch load path

---

*Part of the [Bootciv Tech Tree](../index.md) • [Human Spaceflight](./index.md) • [All Domains](../index.md)*
