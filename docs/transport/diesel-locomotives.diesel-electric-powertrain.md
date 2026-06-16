# Diesel-Electric Powertrain

> **Node ID**: transport.diesel-locomotives.diesel-electric-powertrain
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.diesel-locomotives`](./diesel-locomotives.md)
> **Timeline**: Years 20-50+
> **Outputs**: diesel_electric_generators
> **Critical**: No

The diesel-electric powertrain transmits power from the diesel engine to the driving axles through an electrical path rather than a mechanical one. The engine drives a generator (DC) or alternator (AC with rectifier); the electrical output feeds traction motors geared to the axles. The electrical link acts as a continuously variable transmission, allowing full engine torque at zero axle speed without a clutch or gearbox.

## Why Electrical Transmission

A 3,000 HP locomotive starting a 5,000-tonne train from standstill must deliver 250-350 kN of tractive effort at the rail, at wheel speeds near zero. A mechanical gearbox sized for this torque would need to handle 1.5-2.5 MN·m at the input shaft, with a ratio range exceeding 20:1 — beyond any practical multi-speed transmission. The diesel-electric transmission replaces this with copper and steel: the generator produces current proportional to torque, and the traction motor produces torque proportional to current. No gears to shift, no clutch to slip, no synchronization to fail.

## Components

- **Diesel engine**: V8, V12, or V16, 1,000-4,500 HP continuous. Runs at constant governed speed (900-1,050 RPM) regardless of train speed.
- **Generator or alternator**: 800-3,000 kW. DC generator (with commutator and brushes) on early units; brushless alternator with rotating rectifier on modern units.
- **Traction motors**: One per powered axle. Series-wound DC (early) or AC induction (modern). Geared to the axle at 60:15 to 85:19 ratio.
- **Load regulator**: Matches generator load to engine power at each throttle notch. Mechanical (cam and rheostat) or electronic (microprocessor-controlled exciter).
- **Control system**: Contactors, relays (or solid-state controllers) that connect the traction motors in series, series-parallel, or parallel depending on speed and power demand.

## Prerequisites

- [Diesel-Electric Locomotives](./diesel-locomotives.md) — parent capability and integration
- [Internal Combustion Engines](../energy/internal-combustion.md) — the diesel prime mover
- [Electricity](../energy/electricity.md) — generator and traction motor fundamentals
- [Iron and Steel](../metals/iron-steel.md) — laminations, shafts, gears, frames

## See Also

- [Diesel-Electric Locomotives](./diesel-locomotives.md) — parent capability
- [Road-Switcher Design](./diesel-locomotives.road-switcher-design.md) — locomotive layout
- [Dynamic Braking](./diesel-locomotives.dynamic-braking.md) — reverse energy flow

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transport](./index.md) • [All Domains](../index.md)*
