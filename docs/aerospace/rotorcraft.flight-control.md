# Flight Control

> **Node ID**: aerospace.rotorcraft.flight-control
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.rotorcraft`](rotorcraft.md)
> **Timeline**: Years 30-50+
> **Outputs**: swashplates
> **Critical**: No

Helicopter flight control has no ailerons or elevators. Instead, the pilot tilts and modulates the entire rotor lift vector through the **swashplate** — a pair of plates (one stationary, one rotating) joined by a bearing that translates fixed-frame control inputs into per-blade pitch changes. The collective lever raises all blades' pitch equally (climb/descend); the cyclic stick tilts the swashplate so each blade gets more pitch on one side of the disc and less on the other, tilting the disc and translating the aircraft.

A second control problem is torque reaction: every single-rotor helicopter needs an anti-torque system at the tail. Four solutions are in production use — conventional tail rotor (Bell UH-1, Robinson R44), shrouded Fenestron fan (Airbus H135/H160), NOTAR pressure thrust (MD Explorer), and coaxial counter-rotation (Kamov Ka-52). Each trades power cost, noise, ground safety, and mechanical complexity differently.

## Key Parameters

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Control phase lag | ~90° | Disc responds ~90° after cyclic input |
| Anti-torque power | 4-10% total | Tail rotor; 0% coaxial |
| Boost pressure | 1000-3000 psi | Hydraulic servo assist |
| Pedal authority | Full travel in <1 s | Yaw rate control |

## Prerequisites

- [Rotorcraft](rotorcraft.md) — parent capability overview
- [Rotor Systems](rotorcraft.rotor-systems.md) — the blades the swashplate pitches
- [Precision machine tools](../machine-tools/index.md) — swashplate bearing manufacture

## See Also

- [Rotorcraft](rotorcraft.md) — parent capability overview
- [Rotor Systems](rotorcraft.rotor-systems.md) — blades that receive pitch commands
- [Autorotation](rotorcraft.autorotation.md) — power-off flight control demands

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
