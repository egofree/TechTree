# Maneuver Design

> **Node ID**: spacecraft-systems.orbital-mechanics.maneuver-design
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.orbital-mechanics`](./orbital-mechanics.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: maneuver_plans
> **Critical**: No

Maneuver design computes the delta-v (magnitude, direction, and timing) required to transfer a spacecraft from its current orbit to a target orbit. The Hohmann transfer is the most efficient two-impulse coplanar transfer; bi-elliptic and low-thrust spiral transfers offer alternatives for large orbit ratios or electric propulsion. See [Orbital Mechanics](./orbital-mechanics.md) for the Tsiolkovsky equation and delta-v budgeting.

## Overview

A maneuver plan specifies the burn timing (inertial time), the delta-v vector (inertial direction and magnitude), and the expected post-burn orbit. For chemical propulsion, burns are impulsive (seconds to minutes); for electric propulsion, thrust is applied continuously over hours to months. The plan must account for thrust-vector misalignment, burn-duration uncertainty, and propellant tank conditions.

## Key Parameters

| Transfer Type | Typical Δv | Duration | Propulsion |
|--------------|-----------|----------|------------|
| LEO→GEO Hohmann (coplanar) | 3.89 km/s | 5 hours | Bipropellant |
| Plane change (28.5° at LEO) | 3.77 km/s | Impulsive | Bipropellant |
| LEO phase adjust | 1–50 m/s | Impulsive | Monopropellant |
| Low-thrust LEO→GEO spiral | 4.0 km/s | 4–8 months | Hall / Ion |

## Prerequisites

- Orbital mechanics theory and optimal control ([mathematics](../mathematics/))
- Trajectory optimisation software ([computing](../computing/))
- Orbit determination state vectors ([measurement](../measurement/))

## See Also

- [Orbital Mechanics](./orbital-mechanics.md) — parent capability
- [Orbit Determination](./orbital-mechanics.orbit-determination.md) — provides current state
- [Station-Keeping](./orbital-mechanics.station-keeping.md) — routine maneuvers

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
