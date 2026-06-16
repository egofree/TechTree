# IMU & Gyroscopes

> **Node ID**: spacecraft-systems.adcs.imu-gyros
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.adcs`](./adcs.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: adcs_hardware
> **Critical**: No

Inertial Measurement Units (IMUs) provide high-bandwidth angular rate data that bridges the temporal gap between star tracker updates. The critical parameter is **drift** — the slow accumulation of angular error when the spacecraft is nearly stationary. See [ADCS](./adcs.md) for the integrated control system context.

## Overview

Three gyroscope technologies dominate spacecraft IMUs:

**MEMS (Micro-Electro-Mechanical Systems)** gyroscopes use a vibrating silicon structure. Rotation induces a Coriolis force that displaces the vibrating mass perpendicular to the drive axis. The displacement is sensed capacitively. MEMS gyros are small (50–200 g), cheap, and rugged, but have the highest drift (0.01–1 deg/hr). Radiation degrades the resonator electronics over the mission life.

**Fiber-Optic Gyros (FOG)** use two counter-propagating light beams in a fiber coil. Rotation causes a Sagnac phase shift between the beams proportional to angular rate. FOGs have no moving parts, excellent lifetime, and drift of 0.001–0.01 deg/hr. They are the standard choice for medium and large satellites.

**Ring Laser Gyros (RLG)** use two counter-propagating laser beams in a triangular or square ring cavity. Rotation causes a frequency difference (beat frequency) proportional to rate. RLGs achieve the highest precision (0.0001–0.001 deg/hr) but require high-voltage ignition and dither motors to prevent lock-in at low rates.

## Key Parameters

| Gyro Type | Drift | Mass | Bandwidth | Notes |
|-----------|-------|------|-----------|-------|
| MEMS | 0.01–1 deg/hr | 50–200 g | 100–1000 Hz | Radiation-sensitive |
| FOG | 0.001–0.01 deg/hr | 0.5–2 kg | 100–1000 Hz | No moving parts |
| RLG | 0.0001–0.001 deg/hr | 1–3 kg | 100–1000 Hz | High voltage, dither |

## Prerequisites

- Silicon microfabrication for MEMS ([silicon](../silicon/))
- Fiber optic coil winding and laser diodes for FOG
- Precision optical cavity machining for RLG
- Radiation-hardened readout electronics

## See Also

- [ADCS](./adcs.md) — parent capability
- [Star Trackers](./adcs.star-trackers.md) — drift correction via absolute reference
- [Reaction Wheels](./adcs.reaction-wheels.md) — actuator driven by rate feedback

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
