# Parachute Systems

> **Node ID**: `launch-vehicles.edl.parachute-systems`
> **Domain**: [Launch Vehicles](./index.md)
> **Parent**: [Entry, Descent & Landing](./edl.md)
> **Outputs**: parachutes, drogue_chutes, canopy_deployment_systems
> **Timeline**: Years 30-200+

## Overview

Parachutes provide terminal deceleration for payloads and capsules, converting kinetic energy to
drag work. They are extraordinarily mass-efficient — a 50 kg canopy can decelerate a 5-tonne
payload from 200 m/s to 8 m/s — but are limited by supersonic opening shock and canopy stability
in turbulent flow. For Earth landing from subsonic speeds, parachutes are the dominant EDL
technology; for supersonic or high-mass landings, they are paired with retropropulsion.

## Parachute Types

| Type | Application | Diameter | Deploy speed | Fabric |
|------|-------------|----------|--------------|--------|
| Disk-Gap-Band (DGB) | Apollo CM main | 25.5 m | Subsonic | Nylon |
| Ringsail | Orion MPS main | 33.5 m | Subsonic | Kevlar/Nylon |
| Supersonic DGB | Mars Science Laboratory | 21.5 m | Mach 2.0 | Nylon |

**Disk-Gap-Band (DGB)**: The canonical planetary parachute. A flat disk with an annular gap and a
cylindrical band at the periphery. The gap vents high-pressure air from under the canopy, improving
stability and reducing oscillation. Used on Apollo, Viking, Pathfinder, and MSL. The Apollo CM
used three 25.5 m DGB mains to slow the 5,300 kg capsule to 8 m/s for splashdown.

**Ringsail**: Concentric fabric rings with protruding sails create a vented, cambered profile
with higher drag coefficient (Cd ≈ 0.55 vs 0.45 for DGB). Orion uses three 33.5 m ringsails for
its 9,000 kg capsule.

**Supersonic DGB**: Deployed at Mach 1.5-2.5, the canopy inflates violently — opening shock can
reach 100,000 N peak. The MSL parachute deployed at **Mach 2.0** at 10 km altitude on Mars,
generating 65,000 N peak drag. A mortar (pyrotechnic cannon) fires the packed canopy into the
slipstream at 30-50 m/s to ensure clean inflation.

## Reefing

Large parachutes are **reefed** to stage-in drag area and limit opening shock. A circumferential
reefing line restricts initial inflation to a fraction of full diameter. After the initial shock
dissipates (6-10 s), a pyrotechnic cutter severs the line and the canopy inflates fully. A typical
crewed main uses three reef stages: 25% → 50% → 100% drag area.

## Fabric Materials

- **Nylon** (polyamide): workhorse fabric, 500-800 MPa tensile strength, limit ~120°C.
- **Kevlar** (para-aramid): 5× stronger than nylon by weight, heat-resistant to 400°C. Used for
  riser lines and high-load canopies.
- **Zylon** (PBO): 1.5× stronger than Kevlar; used for MSL suspension lines.

## See Also

- [Entry, Descent & Landing](./edl.md) — parent capability
- [Polymers](../polymers/index.md) — parachute fabric materials
- [Retropropulsion](./edl.retropropulsion.md) — complementary propulsive landing

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
