# Docking Systems

> **Node ID**: `human-spaceflight.crewed-spacecraft.docking-systems`
> **Domain**: [Human Spaceflight](./index.md)
> **Parent**: [Crewed Spacecraft](./crewed-spacecraft.md)
> **Dependencies**: [`human-spaceflight.crewed-spacecraft`](./crewed-spacecraft.md)
> **Outputs**: docking_systems, docking_mechanisms, capture_latches
> **Timeline**: Years 50-200+

## Overview

Docking joins two spacecraft in orbit: soft capture (initial contact, damping relative
velocity), structural hard capture (locking rings together), and pressure-tight seal for
hatch opening and crew transfer. The approach closes the final metres at 1-5 cm/s.

## System Types

| System | Type | Used by |
|--------|------|---------|
| Probe-and-drogue | active probe / passive cone | Soyuz, Progress, Apollo CSM-LEM |
| APAS-95 | androgynous peripheral | Shuttle-ISS, Crew Dragon |
| IDA / NDS | androgynous, international | Crew Dragon, Starliner, Orion |
| CBM | common berthing (robot arm) | ISS modules, Cargo Dragon |

## APAS / IDA

Androgynous Peripheral Attach System and its successor IDA (International Docking Adapter)
are androgynous: either vehicle can be the active partner. The interface is a ring of capture
latches surrounded by 12 structural hooks. Soft capture on contact via spring-loaded petals,
then motorised hooks pull together for hard capture. Crew Dragon and Starliner dock
autonomously to IDA ports.

## Probe-and-Drogue (Soyuz)

Non-androgynous: the Soyuz carries a spring-loaded probe that seats into a cone on the
station, damps approach velocity, then a drive pulls the two together for hard-latch. The
probe retracts after docking.

## Sensors and Navigation

Relative navigation closes from 30 km (GPS differential) to 100 m (star trackers, LIDAR) to
contact. The final 100 m approaches along a keep-out safety corridor at 1-10 cm/s with
hold-and-retreat capability.

## See Also

- [Crewed Spacecraft](./crewed-spacecraft.md) — parent capability
- [Crew Cabin Design](./crewed-spacecraft.crew-cabin.md) — forward docking hatch
- [Computing](../computing/index.md) — autonomous docking flight software

---

*Part of the [Bootciv Tech Tree](../index.md) • [Human Spaceflight](./index.md) • [All Domains](../index.md)*
