# Staging Design

> **Node ID**: `launch-vehicles.vehicle-architecture.staging-design`
> **Domain**: [Launch Vehicles](./index.md)
> **Parent**: [Vehicle Architecture](./vehicle-architecture.md)
> **Outputs**: stage_separators, interstages
> **Timeline**: Years 30-200+

## Overview

Staging design partitions a launch vehicle's total delta-v budget across two or more propulsive
stages, each discarded after its propellant is depleted. The fundamental driver is the Tsiolkovsky
rocket equation: no single chemical stage can carry both the propellant and structure needed to
reach orbit from Earth's surface in one piece, because the required mass ratio (~10:1) exceeds what
any achievable structure can deliver.

## Serial vs Parallel Staging

**Serial staging** stacks stages end-to-end. The first stage ignites at liftoff, burns to depletion,
separates, and the second stage ignites. The optimum delta-v split for a two-stage LOX/RP-1 vehicle
to LEO is approximately 3.5-4.0 km/s for the first stage and 4.5-5.5 km/s for the upper stage —
placing most of the work on the higher-Isp upper stage while the first stage absorbs gravity and
drag losses.

**Parallel staging** ("stage-and-a-half") straps boosters alongside a sustainer core that burns from
liftoff. The Space Shuttle, Ariane 5, Falcon Heavy, and SLS all use this architecture. Parallel
staging avoids the need to start an upper-stage engine in vacuum (which can be challenging for
pressure-fed engines) and delivers high thrust at liftoff from the combined booster + core engines.

## Separation Systems

- **Spring thrusters**: compression springs in the interstage joint provide 2-5 kN separation
  impulse for several milliseconds. Used on Atlas, Delta, and Falcon 9. Simple and reliable.
- **Pneumatic pushers**: compressed-gas pistons provide higher impulse; used where spring force is
  insufficient for heavier stages.
- **Solid separation motors**: small solid rocket motors on the spent stage fire retrograde to pull
  it clear. Used on Titan, Ariane 5 booster separation, and Shuttle SRB separation.

The interstage must transmit full upper-stage thrust through to the booster during first-stage
burn, then release cleanly at separation. Explosive bolts or pneumatic latches release the joint;
the separation impulse ensures a clean break before the upper-stage engine ignites.

## Key Parameters

| Parameter | Typical range |
|-----------|--------------|
| Stage mass ratio (m₀/m_f) | 8-14 per stage |
| Interstage mass fraction | 1-3% of stage dry mass |
| Separation clearance | 0.5-2.0 m in <1 s |
| Post-separation collision avoidance | Cold-gas thrusters + tumbling |

## See Also

- [Vehicle Architecture](./vehicle-architecture.md) — parent capability
- [Structural Design](./vehicle-architecture.structural-design.md) — interstage and tank design
- [GNC Integration](./vehicle-architecture.gvnc-integration.md) — stage separation sequencing

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
