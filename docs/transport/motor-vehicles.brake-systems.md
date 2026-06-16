# Brake Systems

> **Node ID**: transport.motor-vehicles.brake-systems
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.motor-vehicles`](./motor-vehicles.md)
> **Timeline**: Years 20-40+
> **Outputs**: brake_systems
> **Critical**: No

Brakes convert a vehicle's kinetic energy into heat (or, in regenerative systems, recovered electrical energy), providing controlled deceleration and holding force. A passenger car braking from 100 km/h to a stop dissipates roughly 300–500 kJ in 3–4 seconds — a peak power of 100–200 kW, far exceeding engine output. The brake system must absorb this repeatedly without fade.

## Brake Types

**Drum brake**: Brake shoes (curved steel with friction material) press outward against the inner surface of a rotating drum (cast iron, 200–280 mm diameter). Internal expanding design. Advantages: cheap, self-energizing (the leading shoe is pulled into the drum by rotation, amplifying the applied force). Disadvantages: poor heat dissipation (enclosed drum retains heat), fade under hard use, susceptible to water ingress. Used on rear brakes of economy cars and on heavy vehicles.

**Disc brake**: A flat cast-iron rotor (250–350 mm diameter, 12–28 mm thick) is squeezed by a caliper holding friction pads on both sides. Open design — the rotor sheds heat to passing air. Advantages: superior fade resistance, consistent wet performance, self-adjusting pad clearance. Disadvantages: higher pedal effort (no self-energizing), requires power assist. Standard on front axles of all modern cars and on all four wheels of performance vehicles.

## Hydraulic Actuation

Driver pedal force acts on a **master cylinder** (piston in a bore) pressurizing the brake fluid (DOT 4 glycol-ether, boiling point 230°C+). Fluid pressure transmits equally to all four wheel cylinders or caliper pistons through steel tubing and flexible rubber hoses. The system is split into two independent circuits (front/rear or diagonal) so a leak in one circuit leaves half the brakes functional. A **vacuum servo** (brake booster) uses engine intake vacuum to amplify pedal force 3–5×, reducing driver effort.

## Anti-Lock Braking (ABS)

Wheel speed sensors detect impending lockup. The ABS modulator rapidly pulses hydraulic pressure (5–20 Hz) to each wheel — releasing and reapplying the brake — keeping the tire at the threshold of adhesion rather than a full skid. Benefits: maintains steering control during hard braking, shortens stopping distance on most surfaces (10–20% on wet roads). Standard equipment on all passenger cars since 2004 (EU) and 2012 (US).

## Regenerative Braking Interface

In hybrid and electric vehicles, the electric motor reverses to act as a generator during braking, recovering kinetic energy into the battery. This reduces friction brake wear and recovers 10–30% of urban driving energy. The vehicle's controller blends regenerative and friction braking seamlessly — the driver feels normal pedal response while the system shifts load between the two. The friction brakes remain essential for hard stops, low-speed final stop, and fail-safe backup.

## See Also

- [Motor Vehicle Fundamentals](./motor-vehicles.md) — parent capability overview
- [Chassis & Frame Construction](./motor-vehicles.chassis-frame-construction.md) — brake calipers mount to the steering knuckle or axle
- [Suspension Systems](./motor-vehicles.suspension-systems.md) — wheel hubs carry the brake rotors

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
