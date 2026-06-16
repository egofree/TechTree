# Traction Motor Design

> **Node ID**: transport.electric-railways.traction-motor-design
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.electric-railways`](electric-railways.md)
> **Timeline**: Years 25-50+
> **Outputs**: traction_motors
> **Critical**: No

Railway traction motors are electric machines optimized for high starting torque, wide speed range, and survival in a hostile environment (shock, dust, moisture, 30+ year life). The fundamental electromagnetic theory is covered in [Electric Motors](../energy/electricity.motor.md); this process covers only the railway-specific design choices.

## Motor Types

- **DC series motor** (1890s-1980s): high starting torque and a drooping speed-torque curve that suits traction. Limited by the commutator and brushes (voltage ceiling ~3 kV, brush replacement every 200,000-400,000 km). Classic resistance- and chopper-controlled locomotives.
- **AC induction motor with VVVF inverter** (modern standard): rugged, brushless, cheap. Requires on-board rectification then a PWM inverter synthesizing variable-frequency three-phase AC. Enabled by GTO thyristors (1980s) and IGBTs (1990s). Used by the Siemens Eurosprinter and Bombardier TRAXX families.
- **Permanent-magnet synchronous motor (PMSM)**: highest efficiency (96-97%) and power density, but uses rare-earth magnets and needs rotor-position sensing. Appearing on newest platforms; not yet universal.

## Mounting and Cooling

- **Axle-hung, nose-suspended**: motor bolted to axle bearings — cheap but fully unsprung mass, increasing track damage at speed. Used on freight and low-speed locomotives.
- **Frame-mounted**: motor bolted to the bogie frame, drives axle through a flexible coupling. All mass is sprung — required for high-speed (TGV, Shinkansen).
- **Cooling**: forced-air from blowers, ducted through the machine, filtered to exclude abrasive ballast dust. Fully enclosed (TEFC) motors for dusty environments.

## Prerequisites

- [Electric Railways](electric-railways.md) — parent capability
- [Electric Motors](../energy/electricity.motor.md) — fundamental electromagnetic theory
- [Machine Tools](../machine-tools/index.md) — precision machining of shafts, laminations, commutators

## See Also

- [Electric Railways](electric-railways.md) — parent capability
- [Overhead Electrification](electric-railways.overhead-electrification.md) — the power source for the motors
- [Regenerative Braking](electric-railways.regenerative-braking.md) — motors run in reverse as generators

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
