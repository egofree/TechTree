# Suspension Systems

> **Node ID**: transport.motor-vehicles.suspension-systems
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.motor-vehicles`](./motor-vehicles.md)
> **Timeline**: Years 20-40+
> **Outputs**: suspension_systems
> **Critical**: No

The suspension couples the chassis to the wheels, serving two conflicting goals: absorbing road irregularities for ride comfort, and keeping the tires in contact with the road for grip and control. Every suspension is a compromise between these goals, tuned for the vehicle's intended use.

## Spring Types

- **Leaf spring**: Multiple curved steel strips (leaves) clamped together. The oldest type — used on carts and wagons for centuries. Progressive friction between leaves provides inherent damping. Rugged and cheap; still used on trucks and heavy vehicles.
- **Coil spring**: Helical spring of spring steel (SAE 9254, Si-Cr alloy, yield >1400 MPa, shot-peened for fatigue life). Lighter and more compact than leaf; allows independent wheel movement. Dominant on passenger cars since the 1930s.
- **Air spring**: A rubber airbag pressurized with compressed air. Constant ride height regardless of load (adjustable pressure). Used on luxury cars, buses, and heavy trucks.

## Suspension Geometries

**MacPherson strut**: A coil spring and damper assembled as one unit, pivoting at the top mount and steering at the bottom. Only one lateral link per wheel. Simple, cheap, compact — the dominant front suspension on front-drive cars since the 1970s. Disadvantage: the strut tower takes up space otherwise usable for a wide engine.

**Double wishbone**: Two A-shaped lateral arms (upper and lower) locate the wheel. The steering axis (kingpin) is defined by the ball joints at the arm ends. Superior camber control through the full wheel travel — the wheel stays more perpendicular to the road in corners. Used on sports cars and racing. Requires more space and components than MacPherson.

**Multi-link**: 3–5 individual links locating each wheel, replacing the rigid arms. Each link carries one force component (lateral, longitudinal, braking). Allows independent tuning of camber, caster, and toe curves through wheel travel. The modern standard for premium cars.

## Dampers (Shock Absorbers)

Hydraulic telescopic dampers control spring oscillation by forcing oil through valved orifices. Without dampers, a spring would bounce indefinitely after each bump. The damper resists velocity — slow movements (body roll in corners) meet low resistance; fast movements (sharp bumps) meet high resistance. Gas-charged dampers (nitrogen pressurized) prevent oil cavitation and fade under hard use.

## Anti-Roll Bars

A transverse steel torsion bar connecting the left and right suspension. In a corner, the outer suspension compresses and twists the bar, which lifts the inner wheel — reducing body roll. Stiffer bars sharpen handling but increase load transfer to the outer tire (which can reduce total grip on rough surfaces).

## See Also

- [Motor Vehicle Fundamentals](./motor-vehicles.md) — parent capability overview
- [Chassis & Frame Construction](./motor-vehicles.chassis-frame-construction.md) — suspension mounts to the chassis
- [Steering Systems](./motor-vehicles.steering-systems.md) — works with front suspension geometry

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
