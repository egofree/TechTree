# Dynamic Braking

> **Node ID**: transport.diesel-locomotives.dynamic-braking
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.diesel-locomotives`](./diesel-locomotives.md)
> **Timeline**: Years 20-50+
> **Outputs**: diesel_locomotives
> **Critical**: No

Dynamic braking uses the traction motors as generators during deceleration, converting the train's kinetic energy into electrical energy and dissipating it as heat. This preserves friction brakes for low-speed stopping and emergency use, preventing thermal fade on long downgrades.

## Principle

In power mode, current flows from the generator to the traction motors, producing torque that drives the wheels. In dynamic brake mode, the current path reverses: the wheels drive the traction motors (now acting as generators), and the generated current flows to a resistor grid on the locomotive roof, where it is dissipated as heat. The resistance of the grid creates a counter-torque that slows the train.

The dynamic brake is engaged by a separate handle in the cab (independent of the throttle and the automatic air brake). Notches 1-8 provide progressively more braking effort. At full dynamic brake, a 3,000 HP locomotive can dissipate 2,000-3,000 kW continuously — enough to hold a 3,000-tonne train at constant speed on a 2.0-2.5% downgrade without touching the friction brakes.

## Rheostatic vs Regenerative

- **Rheostatic braking** (standard on diesel-electric locomotives): The generated power is dumped into a resistor grid. The energy is lost as heat. This is the only option on a non-electrified railway, because there is no external circuit to absorb the power.
- **Regenerative braking** (on electric locomotives only): The generated power is fed back into the overhead catenary or third rail, where it can be used by other trains. Energy recovery of 15-25% is possible on electrified lines with heavy traffic. Diesel-electric locomotives cannot regenerate — they have no connection to an external grid.

## Limitations

- Dynamic braking is ineffective below 15-20 km/h: the traction motors cannot generate sufficient voltage at low wheel speeds. Friction brakes must take over for final stopping.
- The resistor grid reaches 200-600°C during operation. Cooling fans (1-3 roof-mounted axial fans) must run continuously. Grid fan failure forces immediate reduction of braking effort to prevent grid burnout.
- Dynamic braking does not replace the air brake for holding a stopped train or for emergency stops — it is a supplementary system for speed control on grades.

## Prerequisites

- [Diesel-Electric Locomotives](./diesel-locomotives.md) — parent capability with traction motors and generator
- [Electricity](../energy/electricity.md) — generator/motor reversibility principle

## See Also

- [Diesel-Electric Locomotives](./diesel-locomotives.md) — parent capability
- [Diesel-Electric Powertrain](./diesel-locomotives.diesel-electric-powertrain.md) — the traction motors in power mode
- [Railways](./railways.md) — grade profiles and brake systems

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transport](./index.md) • [All Domains](../index.md)*
