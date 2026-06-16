# Post-Mission Disposal

> **Node ID**: spacecraft-systems.debris-management.post-mission-disposal
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.debris-management`](./debris-management.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: disposal_plans
> **Critical**: No

Post-mission disposal is the removal of a defunct spacecraft from its operational orbit at end of mission, in compliance with IADC guidelines. LEO spacecraft must de-orbit within 25 years (controlled re-entry or natural decay); GEO spacecraft must re-orbit to a graveyard orbit 300+ km above the geostationary ring. Compliance prevents the Kessler cascade — the cascading collision scenario that could render orbital regimes unusable. See [Debris Management](./debris-management.md) for the full IADC guideline framework.

## Overview

Disposal planning begins at mission design — the propellant budget must reserve sufficient delta-v for the disposal maneuver. For LEO, controlled de-orbit targets a re-entry over the South Pacific Ocean Uninhabited Area; for GEO, the graveyard altitude is computed from the IADC formula: ΔH = 235 km + (1000 × Cr × A/m). Passivation (venting residual propellant and discharging batteries) prevents on-orbit fragmentation after disposal.

## Key Parameters

| Disposal Mode | Orbit | Required Δv | Compliance |
|--------------|-------|-------------|------------|
| Controlled de-orbit | LEO 400–600 km | 100–300 m/s | Targeted re-entry |
| Natural decay | LEO <600 km | 0–50 m/s | 25-year rule |
| Accelerated decay | LEO 600–900 km | 30–200 m/s | Lowers perigee |
| GEO graveyard | GEO → GEO+300 km | 11 m/s | IADC formula |

## Prerequisites

- Disposal trajectory computation ([computing](../computing/))
- Orbit determination for maneuver targeting ([measurement](../measurement/))
- Passivation electronics design ([electronics](../electronics/))

## See Also

- [Debris Management](./debris-management.md) — parent capability
- [Debris Tracking](./debris-management.debris-tracking.md) — catalogue maintenance
- [Collision Avoidance](./debris-management.collision-avoidance.md) — operational conjunction management

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
