# Robotic Manipulator Arms

> **Node ID**: human-spaceflight.space-stations.robotic-arms
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.space-stations`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: robotic_manipulator_arms, space_stations
> **Critical**: Yes

Robotic manipulator arms perform module berthing, EVA crew positioning, payload handling, and external inspection on a space station. The reference system is Canadarm2 (SSRMS) — a 17.6 m, 7-degree-of-freedom arm with Latching End Effectors at both tips, enabling end-over-end "walking" across the station's surface by relocating its base from one grapple fixture to another.

Each arm joint uses brushless DC motors with harmonic drive reduction, providing backlash-free torque transmission with high reduction ratio in a compact package. The joint controllers, motor drives, and teleoperation interfaces draw directly from the [automation](../automation/index.md) domain.

## Key Parameters

| Parameter | Canadarm2 (SSRMS) | Dextre (SPDM) | ERA |
|-----------|-------------------|---------------|-----|
| Length | 17.6 m | 3.5 m | 11.3 m |
| Mass | 1,800 kg | 1,662 kg | 630 kg |
| Degrees of freedom | 7 | 15 (7 per arm + body) | 7 |
| Lift capacity | 116,000 kg | 600 kg (per arm) | 8,000 kg |
| Tip accuracy | ±45 mm | ±6 mm | ±50 mm |
| End effectors | LEE × 2 | OTCM × 2 | EEC × 2 |

## Joint Actuator Architecture

1. Brushless DC motor (200 W nominal per joint)
2. Harmonic drive reduction (160:1 typical ratio)
3. Joint position resolver (0.01° resolution)
4. Torque sensor ( overload protection)
5. Brake (fail-safe hold on power loss)

## Prerequisites

- [Space Stations](./space-stations.md) — parent capability
- [Automation](../automation/index.md) — motor controllers and teleoperation
- [Machine tools](../machine-tools/index.md) — joint machining
- [Spacecraft bus structure](../spacecraft-systems/bus-structure.md) — arm attachment points

## See Also

- [Space Stations](./space-stations.md) — parent capability
- [Structural Docking + Berthing](./space-stations.structural-docking.md) — arm positions modules for berthing
- [EVA Procedures](./eva.eva-procedures.md) — arm carries foot restraint for crew positioning
