# Neutralizer Design

> **Node ID**: space-propulsion.electric-ion.neutralizer-design
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.electric-ion`](./electric-ion.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: ion_thrusters
> **Critical**: No

The neutralizer prevents spacecraft charging by emitting electrons into the ion beam, maintaining charge neutrality as positively-charged ions leave the thruster. Without a neutralizer, the spacecraft would accumulate a positive charge until the beam decelerates and returns — a condition that would halt thrust production within milliseconds. See [Electric Propulsion — Ion](./electric-ion.md) for the integrated context.

## Process Description

1. **Emitter preparation**: a porous tungsten cylinder (3–6 mm OD, 10–25 mm length) is impregnated with a BaO-CaO-Al₂O₃ mixture (the "B-type" insert).
2. **Assembly**: the emitter insert is placed inside a hollow cathode tube with a tungsten orifice plate (0.5–2.0 mm aperture).
3. **Heater integration**: a coiled tungsten or refractory wire heater wraps the cathode body, providing 3–8 A at 4–10 V for preheating.
4. **Ignition sequence**: the heater warms the emitter to 1100–1300°C; xenon flows through the insert; a keeper electrode strikes the discharge.
5. **Steady-state operation**: BaO thermionically emits electrons at 1–7 A, matching the ion beam current. The keeper sustains the cathode plasma at 10–25 V.
6. **Coupling to beam**: emitted electrons drift into the ion beam downstream, neutralizing the positive space charge.

## Key Parameters

- **Emission current**: 1–7 A (must equal the ion beam current)
- **Emitter temperature**: 1100–1300°C (BaO thermionic regime)
- **Keeper voltage**: 10–25 V DC (sustains cathode discharge)
- **Heater power**: 12–80 W (preheat only; off during steady-state)
- **Propellant flow**: 0.2–1.0 mg/s xenon through cathode
- **Orifice diameter**: 0.5–2.0 mm (tungsten)
- **Lifetime**: 20,000–30,000 hr (BaO depletion-limited)

## Prerequisites

- Hollow cathode technology (BaO impregnated porous tungsten)
- Tungsten orifice plate machining (μm tolerance)
- Keeper electrode and heater wire manufacturing

## See Also

- [Electric Propulsion — Ion](./electric-ion.md) — parent capability
- [Ionization Chamber](./electric-ion.ionization-chamber.md) — discharge cathode (similar design)
- [Power Processing Unit](./electric-ion.power-processing-unit.md) — provides keeper/heater power

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
