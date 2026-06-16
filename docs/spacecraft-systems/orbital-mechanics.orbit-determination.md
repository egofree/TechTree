# Orbit Determination

> **Node ID**: spacecraft-systems.orbital-mechanics.orbit-determination
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.orbital-mechanics`](./orbital-mechanics.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: orbit_solutions
> **Critical**: No

Orbit determination is the process of estimating a spacecraft's position and velocity (its state vector) from a set of noisy tracking measurements. Ground-based radar provides range and range-rate; GNSS receivers on LEO spacecraft provide centimetre-level position; satellite laser ranging provides millimetre accuracy. See [Orbital Mechanics](./orbital-mechanics.md) for the integrated operations cycle.

## Overview

The state vector is estimated using either batch least-squares (processing 3–7 days of observations as a batch) or sequential estimation (an Extended Kalman Filter that updates the state with each new measurement). Both methods require a force model — the set of gravitational and non-gravitational forces that propagate the state between measurements. The force model includes Earth's gravity (EGM2008, 2190×2159 spherical harmonics), atmospheric drag (NRLMSISE-00 density model), solar radiation pressure, and third-body gravity from the Moon and Sun.

## Key Parameters

| Parameter | LEO (GNSS) | GEO (Radiometric) | Precision (SLR) |
|-----------|-----------|-------------------|-----------------|
| Position accuracy | 1–10 m | 10–100 m | 0.001–0.01 m |
| Velocity accuracy | 1–10 mm/s | 1–10 mm/s | 0.1 mm/s |
| Update latency | Real-time | 3–12 hours | Days |
| State vector dimension | 6 + empirical | 6 + empirical | 6 + empirical |

## Prerequisites

- Numerical integration and linear algebra ([mathematics](../mathematics/))
- High-performance computing for batch processing ([computing](../computing/))
- Ground-based radar, GNSS, and SLR sensors ([measurement](../measurement/))

## See Also

- [Orbital Mechanics](./orbital-mechanics.md) — parent capability
- [Maneuver Design](./orbital-mechanics.maneuver-design.md) — uses OD state vectors
- [Station-Keeping](./orbital-mechanics.station-keeping.md) — orbit maintenance

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
