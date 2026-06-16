# Station-Keeping

> **Node ID**: spacecraft-systems.orbital-mechanics.station-keeping
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.orbital-mechanics`](./orbital-mechanics.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: station_keeping_schedules
> **Critical**: No

Station-keeping is the periodic correction of orbital perturbations to maintain a spacecraft within its operational slot or ground track. GEO satellites require North-South station-keeping (~50 m/s/yr against luni-solar inclination drift) and East-West station-keeping (~2 m/s/yr against solar radiation pressure). LEO satellites require drag makeup maneuvers proportional to atmospheric density. See [Orbital Mechanics](./orbital-mechanics.md) for full perturbation budgets.

## Overview

GEO station-keeping maintains the satellite within a ±0.05° longitude slot (±75 km). NSSK maneuvers correct inclination drift every 2–4 weeks; EWSK maneuvers correct longitude drift every 1–2 weeks. LEO station-keeping maintains ground track repeat cycles — a Sun-synchronous Earth observation satellite must hold its equatorial crossing time within ±10 minutes, requiring drag makeup burns every 1–4 weeks depending on altitude and solar activity.

## Key Parameters

| Regime | Maneuver Type | Annual Δv | Frequency | Tolerance |
|--------|-------------|-----------|-----------|-----------|
| GEO NSSK | Inclination correction | 45–55 m/s | Bi-weekly | ±0.05° inclination |
| GEO EWSK | Longitude correction | 1.5–3 m/s | Weekly | ±0.05° longitude |
| LEO 400 km (drag) | Altitude maintenance | 50–1,000 m/s | Weekly | ±1 km altitude |
| LEO 800 km (drag) | Phase maintenance | <15 m/s | Monthly | ±10 min phase |

## Prerequisites

- Orbit propagation and force modelling ([mathematics](../mathematics/))
- Maneuver planning software ([computing](../computing/))
- Orbit determination tracking data ([measurement](../measurement/))

## See Also

- [Orbital Mechanics](./orbital-mechanics.md) — parent capability
- [Orbit Determination](./orbital-mechanics.orbit-determination.md) — measures orbit drift
- [Maneuver Design](./orbital-mechanics.maneuver-design.md) — burn planning

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
