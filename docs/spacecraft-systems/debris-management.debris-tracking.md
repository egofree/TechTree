# Debris Tracking

> **Node ID**: spacecraft-systems.debris-management.debris-tracking
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.debris-management`](./debris-management.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: debris_services
> **Critical**: No

Debris tracking is the process of detecting, cataloguing, and maintaining orbital element sets for the 36,500+ tracked objects larger than 10 cm. The U.S. Space Surveillance Network uses phased-array radar for LEO and optical telescopes for GEO, producing daily catalogue updates distributed as Two-Line Elements (TLEs) and Conjunction Data Messages. See [Debris Management](./debris-management.md) for the full catalogue statistics.

## Overview

Each tracked object must be revisited every 3–30 days or its orbit prediction degrades beyond usefulness. The SSN collects 30,000–80,000 observations daily and processes them through a batch orbit determination pipeline that updates the catalogue. Objects that are not re-acquired within their tracking window are declared "lost" and must be rediscovered through all-sky search — a process that can take weeks.

## Key Parameters

| Sensor Type | Sensitivity (LEO) | Coverage | Catalogue Objects |
|-------------|-------------------|----------|-------------------|
| Phased-array radar | ~5 cm at 1000 km | LEO 400–2000 km | ~25,000 |
| Mechanically-steered radar | ~10 cm at 1000 km | LEO 400–1500 km | ~10,000 |
| Optical telescope | ~1 m at GEO | GEO + deep space | ~1,500 |
| Space-based optical | ~30 cm at GEO | GEO + high LEO | ~500 |

## Prerequisites

- Catalogue processing pipeline ([computing](../computing/))
- Radar and optical tracking sensors ([measurement](../measurement/))
- Radar transmitters and detector electronics ([electronics](../electronics/))

## See Also

- [Debris Management](./debris-management.md) — parent capability
- [Collision Avoidance](./debris-management.collision-avoidance.md) — uses catalogue data
- [Post-Mission Disposal](./debris-management.post-mission-disposal.md) — reduces future catalogue growth

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
