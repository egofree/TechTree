# Regenerative Braking

> **Node ID**: transport.electric-railways.regenerative-braking
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.electric-railways`](electric-railways.md)
> **Timeline**: Years 25-50+
> **Outputs**: electric_locomotives
> **Critical**: No

Regenerative braking converts the train's kinetic energy back into electrical energy by reconnecting the traction motors as generators during deceleration. The recovered energy is either returned to the catenary (if another train is drawing power at that instant), stored in on-board batteries or supercapacitors, or dissipated as heat in roof-mounted rheostatic resistor grids. Suburban stop-start services recover 10-25% of traction energy; high-speed and long-distance freight recover far less because they brake infrequently.

## How It Works

During braking, the inverter that normally feeds AC to the traction motors is reconfigured so the motor's back-EMF drives current back through the inverter into the DC link. On AC catenary systems, a second inverter (or the same one run in reverse) feeds the energy back into the overhead line at the line frequency. On DC systems, a chopper boosts the regenerated voltage slightly above the catenary voltage so current flows out of the train. The braking effort is **blended** with the friction (pneumatic) brakes by a brake controller that prioritizes regenerative torque and tops up with friction only when the regenerative limit is reached or at very low speed.

## Line Receptivity

Energy can only return to the catenary if something nearby is consuming it (another accelerating train) or if the substation can accept reverse power. Classic diode substations cannot; modern reversible (regenerative) substations or trackside energy storage (supercapacitor banks, flywheels) solve this. When the line is not receptive, the train falls back to **rheostatic braking** — dumping the energy into on-board resistor grids — and finally to friction brakes.

## Prerequisites

- [Electric Railways](electric-railways.md) — parent capability
- [Electric Motors](../energy/electricity.motor.md) — motor-as-generator operation
- [Electricity](../energy/electricity.md) — grid and substation infrastructure

## See Also

- [Electric Railways](electric-railways.md) — parent capability
- [Traction Motor Design](electric-railways.traction-motor-design.md) — the motors that become generators
- [Overhead Electrification](electric-railways.overhead-electrification.md) — the return path for regenerated energy

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
