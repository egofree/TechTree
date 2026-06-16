# Simulators

> **Node ID**: human-spaceflight.crew-training.simulators
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.crew-training`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 60+
> **Outputs**: trained_crew
> **Critical**: No

Simulators are the primary training tools for spacecraft procedures, spanning a fidelity spectrum from software-only part-task trainers to full-motion cockpit replicas with hydraulic 6-DOF hexapod platforms. The Space Mission Simulator (SMS) complex at JSC includes fixed-base and motion-base trainers for Crew Dragon, Starliner, Soyuz, and Orion, plus integrated ISS mockups with full system functionality. Modern VR headsets (Varjo XR-3 at 2,800 x 2,800 pixels per eye) supplement physical trainers for EVA pre-briefing, robotics operations, and emergency egress rehearsals. The simulation software injects hundreds of scripted failure scenarios to train crew on contingency response under realistic time pressure.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Motion-base DOF | 6 (hexapod) | Surge, sway, heave, roll, pitch, yaw |
| Peak acceleration | +/- 1.5 g per axis | Launch/entry simulation |
| Motion cueing latency | < 25 ms | Real-time cueing algorithm |
| VR headset resolution | 2,800 x 2,800 per eye | Varjo XR-3 |
| Full mission simulator cost | $20-100M | SMS complex class |
| Training hours in sims (ISS crew) | 400-500 | Over 30-month flow |

## Prerequisites

- [Crew Training](./crew-training.md) — parent capability

## See Also

- [Crew Training](./crew-training.md) — parent capability
- [Neutral Buoyancy](./crew-training.neutral-buoyancy.md) — physical EVA training
- [Crewed Spacecraft](./crewed-spacecraft.md) — vehicles being simulated
