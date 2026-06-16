# EV Traction Motors

> **Node ID**: transport.electric-vehicles.ev-traction-motors
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.electric-vehicles`](electric-vehicles.md)
> **Timeline**: Years 40-55
> **Outputs**: ev_powertrains, regenerative_braking_systems
> **Critical**: No

The traction motor converts electrical energy from the battery into mechanical torque at the wheels, and reverses to recover kinetic energy during braking. Motor fundamentals — stator windings, rotor design, rotating magnetic fields, electromagnetic force — are covered in [Electric Motors](../energy/electricity.motor.md). This process addresses EV-specific motor selection, the inverter, motor controller, and single-speed drivetrain integration.

## Motor Types

**PMSM (Permanent Magnet Synchronous Motor)**: Highest efficiency (94-97%), compact, excellent low-speed torque. Uses neodymium-iron-boron magnets. Dominant in modern EVs. Limitation: rare-earth supply and back-EMF management at high speed.

**AC Induction**: No rare-earth magnets. Squirrel-cage rotor. Lower efficiency (90-93%) but cheaper and inherently safe in fault conditions. Used as secondary (front) motor in AWD configurations where it can be de-energized for cruising.

**Axial Flux**: Disc-shaped rotor between two stator discs. Very high torque density, short axial length. Emerging technology for performance and in-wheel applications.

## Inverter and Motor Controller

The inverter converts battery DC (350-800V) to 3-phase AC at variable frequency and voltage. Silicon IGBT switches are standard; silicon carbide (SiC) MOSFETs reduce switching losses 50-70% and enable 800V architectures. The motor controller implements field-oriented control (FOC): it decomposes the 3-phase current into torque-producing (q-axis) and flux-producing (d-axis) components, controlling each independently for maximum efficiency across the full speed range. Flux weakening at high RPM extends the constant-power region beyond base speed.

## Drivetrain

A single-speed reduction gear (9:1 to 10:1) replaces the multi-speed transmission. The motor's wide RPM range (0-16,000+) and instant torque eliminate gear changes. A differential distributes torque between left and right wheels. No clutch is needed — the motor provides full torque at zero speed.

## Regenerative Braking

The motor acts as a generator during deceleration, recovering 10-30% of kinetic energy in urban driving. The BMS controls how much current the battery can accept — cold or full batteries limit regen. One-pedal driving modulates regen via accelerator position.

## Prerequisites

- [Electric Vehicles](electric-vehicles.md) — parent capability
- [Electric Motors](../energy/electricity.motor.md) — motor fundamentals
- [Electronics](../electronics/index.md) — inverter power semiconductors

## See Also

- [Electric Vehicles](electric-vehicles.md) — parent capability
- [Battery Packs](electric-vehicles.battery-packs.md) — energy source for the motor
- [Charging Systems](electric-vehicles.charging-systems.md) — replenishing the pack

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
