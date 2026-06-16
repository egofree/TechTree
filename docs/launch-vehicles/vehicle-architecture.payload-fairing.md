# Payload Fairing

> **Node ID**: `launch-vehicles.vehicle-architecture.payload-fairing`
> **Domain**: [Launch Vehicles](./index.md)
> **Parent**: [Vehicle Architecture](./vehicle-architecture.md)
> **Outputs**: payload_fairings, fairing_jettison_systems
> **Timeline**: Years 30-200+

## Overview

The payload fairing (PLF) is the aerodynamic nose shroud that protects the payload from acoustic
vibration, aerodynamic heating, and aerodynamic loads during ascent through the atmosphere. It is
jettisoned once the vehicle climbs above the sensible atmosphere — typically at **~110 km altitude**
— where dynamic pressure drops below 0.1 kPa and aerodynamic heating ceases. Carrying the fairing
beyond this point wastes payload capacity on dead mass.

## Acoustic and Thermal Protection

**Acoustic blanket**: A 25-50 mm layer of open-cell polyimide foam (or fiberglass acoustic
insulation) lines the fairing interior. At liftoff, engine exhaust reflecting off the flame trench
generates 140-145 dB sound pressure levels. Without the blanket, this acoustic energy would vibrate
payload solar arrays, optics, and electronics destructively. The foam attenuates 10-15 dB at the
payload plane, bringing levels within qualification limits (typically 126-132 dB).

**Thermal coating**: The fairing exterior reaches 150-200°C during Max-Q (T+60-90 s). A
cork-based ablative coating (cork particles in a silicone binder, 0.5-2.0 mm thick) protects the
composite shell. The acoustic foam doubles as thermal insulation, keeping the payload bay below
40-60°C.

## Jettison Mechanism

At jettison altitude, the fairing splits longitudinally into two clamshell halves along a
frangible joint. The joint is released by:

1. **Explosive bolts**: traditional; each bolt contains a pyrotechnic charge that shears the bolt
   at a calibrated load. Simple but generates shock and debris.
2. **Pneumatic latches**: compressed-gas-actuated latches release the joint without pyrotechnic
   shock. Used on Falcon 9 to reduce payload shock environment.
3. **Hoop strap / zip cord**: a tensioned circumferential fibre strap is cut by a thermal knife,
   releasing the hoop compression that holds the halves together.

After joint release, spring thrusters or pneumatic pistons push the halves clear of the vehicle.
Hinges on one side (or yo-yo masses) control the pivot trajectory. A failed jettison is
catastrophic — the extra mass and drag prevent orbital insertion.

## Fairing Dimensions

| Vehicle | Fairing diameter | Fairing length | Fairing mass |
|---------|-----------------|----------------|--------------|
| Falcon 9 | 5.2 m | 13.1 m | ~1,900 kg |
| Atlas V (4-m) | 4.2 m | 12.2 m | ~1,500 kg |
| Ariane 5 | 5.4 m | 17.0 m | ~2,200 kg |
| SLS | 8.4 m | 27.4 m | ~6,500 kg |

## See Also

- [Vehicle Architecture](./vehicle-architecture.md) — parent capability
- [Structural Design](./vehicle-architecture.structural-design.md) — composite shell design
- [Composites](../polymers/composites.md) — carbon-fibre fairing material

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
