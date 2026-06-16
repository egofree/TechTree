# Reaction Wheels

> **Node ID**: spacecraft-systems.adcs.reaction-wheels
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.adcs`](./adcs.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: reaction_wheels
> **Critical**: No

Reaction wheels are the primary actuator for precision spacecraft pointing. A flywheel is accelerated or decelerated by a brushless DC motor, producing a reaction torque on the spacecraft body. They deliver smooth, continuous, electrically powered torque — but they saturate when they reach maximum speed and must be periodically "dumped." See [ADCS](./adcs.md) for the integrated control system context.

## Overview

A reaction wheel assembly consists of a rotating inertia (the flywheel rotor), a brushless DC motor, ball or magnetic bearings, a housing with vacuum-compatible lubricant, and drive electronics. Accelerating the wheel by Δω produces a spacecraft torque τ = I_wheel × (dω/dt) in the opposite direction (Newton's third law for rotating systems). Most spacecraft carry three orthogonal wheels plus a fourth skewed wheel for redundancy and singularity avoidance.

The flywheel rotor is typically a solid steel or tungsten alloy disc balanced to <0.1–0.5 g·cm. Bearing lubrication is the critical lifetime limiter: oil or dry-film lubricants degrade in vacuum, and the qualified MTBF is 7–10 years. Magnetic bearings eliminate contact wear entirely but are heavier and require active control electronics.

Wheel imbalance at the spin frequency introduces micro-vibration jitter that propagates through the spacecraft structure into the payload. For sub-arcsecond imaging missions, active isolation or very low imbalance (<0.1 g·cm) is mandatory.

## Key Parameters

| Parameter | Small Sat | Medium Sat | Large Sat |
|-----------|-----------|------------|-----------|
| Angular momentum | 0.1–1 Nms | 1–10 Nms | 10–50 Nms |
| Max torque | 0.01–0.05 Nm | 0.05–0.2 Nm | 0.2–0.5 Nm |
| Max speed | 6,000 RPM | 6,000 RPM | 6,000–10,000 |
| Bearing MTBF | >5 years | >7 years | >10 years |
| Wheel imbalance | <0.5 g·cm | <0.5 g·cm | <0.1 g·cm |

## Prerequisites

- Precision bearing manufacturing ([precision-motion](../precision-motion/))
- Rotational balancing to sub-gram-centimetre precision ([machine-tools](../machine-tools/))
- Brushless DC motor and drive electronics
- Vacuum-compatible lubricant qualification

## See Also

- [ADCS](./adcs.md) — parent capability and momentum management
- [Magnetorquers](./adcs.magnetorquers.md) — momentum dumping actuator
- [Thruster Control](./adcs.thruster-control.md) — backup momentum dumping

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
