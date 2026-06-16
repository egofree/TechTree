# Multirotor Drones

> **Node ID**: aerospace.uav.multirotor-drones
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.uav`](uav.md)
> **Timeline**: Years 40-55+
> **Outputs**: drone_airframes
> **Critical**: No

Multirotor UAVs use four or more vertically-oriented propellers to generate lift and control attitude through differential motor speed. Unlike helicopters (which use a mechanically complex swashplate for cyclic control), multirotors have no moving parts in their control system — all control is achieved electronically by adjusting individual motor speeds 400-8000 times per second. This simplicity of mechanism trades for complexity of electronics: a multirotor is unflyable without its flight controller.

## Configurations

**Quadcopter (4 motors)**: The most common configuration. X-frame (motors at corners) or H-frame (motors on arms extending from a central body). Minimum for stable flight with yaw authority. Motor layout: CW-CCW-CW-CCW to cancel torque.

**Hexacopter (6 motors)**: Higher payload capacity (~50% more thrust than quadcopter). Can survive single motor failure with degenerated performance (5-motor flight mode). Used for professional photography and heavy payloads.

**Octocopter (8 motors)**: Maximum payload and redundancy. Can survive two motor failures. DJI Inspire and Matrice series. Used for cinema cameras (RED, ARRI) and industrial inspection.

## Frame Construction

Carbon fiber plate-and-arm construction: a central body plate (2-3 mm carbon fiber) holds the flight controller, battery, and PDB (power distribution board). Aluminum or carbon tube arms (10-16 mm diameter) extend to motor mounts. Motors bolt to arm ends. ESCs mounted on arms or integrated into the body. This modular design allows easy arm replacement after crashes.

## Propulsion Matching

Motor KV (RPM/volt) × battery voltage = no-load RPM. Propeller pitch and diameter must match motor thrust capability. Undersized prop: motor over-revs, low thrust. Oversized prop: motor bogs down, excessive current draw, ESC burnout. Common pairings: 2300 KV motor + 5-inch prop (racing), 920 KV motor + 10-inch prop (Class II camera drone), 350 KV motor + 15-inch prop (Class III professional).

## Prerequisites

- [UAV capability](uav.md) — parent capability
- [Autonomous Navigation](uav.autonomous-navigation.md) — flight controller (mandatory)
- [Brushless motors](../energy/index.md) — propulsion and ESCs
- [Polymers](../polymers/index.md) — injection-molded components

## See Also

- [Unmanned Aerial Vehicles](uav.md) — parent capability overview
- [Fixed-Wing Drones](uav.fixed-wing-drones.md) — long-endurance alternative
- [Autonomous Navigation](uav.autonomous-navigation.md) — flight control systems

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
