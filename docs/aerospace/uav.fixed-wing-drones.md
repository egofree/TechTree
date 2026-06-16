# Fixed-Wing Drones

> **Node ID**: aerospace.uav.fixed-wing-drones
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.uav`](uav.md)
> **Timeline**: Years 40-55+
> **Outputs**: unmanned_aerial_vehicles
> **Critical**: No

Fixed-wing UAVs generate lift from wing surfaces, enabling longer endurance and higher range than multirotors. They require forward speed or a catapult launch to stay airborne and cannot hover — a runway, bungee launcher, or vertical-takeoff hybrid mechanism is needed. The trade-off favors range and endurance over maneuverability and VTOL capability.

## Airframe Design

Typical fixed-wing drone configurations: conventional tail (wing + empennage), flying wing (no tail, elevons for control), or twin-boom (fuselage pod between two tail booms). Wingspan ranges from 0.8 m (Class I) to 3+ m (Class IV). Airfoils: flat-bottom (Clark Y) for easy construction, or reflexed (for flying wings). Construction materials: EPO foam (beginner), balsa and film (traditional RC), or carbon fiber composite and fiberglass mold (professional).

## Propulsion

Electric motor (brushless outrunner, 1000-3000 KV) driving a folding propeller (8-12 inch, folding blades reduce drag when motor stops for gliding). Battery: 3S-6S LiPo (11.1-22.2 V). Endurance: 20-60 minutes electric. For Class IV-V endurance (4+ hours), small gasoline or heavy-fuel two-stroke engines (10-50 cc) replace electric power.

## Launch and Recovery

Hand-launch (throw forward at 10-15 m/s), bungee catapult (elastic cord accelerates UAV to flying speed on a rail), or wheeled takeoff from a runway. Recovery: belly landing (skid on belly — foam airframe tolerates this), parachute deployment, or arrestment net. VTOL hybrids (tilt-rotor or quad-plane) combine multirotor launch with fixed-wing cruise.

## Prerequisites

- [UAV capability](uav.md) — parent capability
- [Aviation aerodynamics](aviation.md) — wing design, lift, drag, stability
- [Brushless motors](../energy/index.md) — electric propulsion
- [Flight controller](uav.autonomous-navigation.md) — stabilization and navigation

## See Also

- [Unmanned Aerial Vehicles](uav.md) — parent capability overview
- [Multirotor Drones](uav.multirotor-drones.md) — VTOL alternative
- [Autonomous Navigation](uav.autonomous-navigation.md) — flight control systems

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
