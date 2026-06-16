# Cathode Design

> **Node ID**: space-propulsion.electric-hall.cathode-design
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.electric-hall`](./electric-hall.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: hall_thrusters
> **Critical**: No

The hollow cathode in a Hall thruster serves double duty: it provides the electrons that ionize xenon in the discharge channel and also neutralizes the ion beam to prevent spacecraft charging. Unlike ion thrusters that use separate discharge and neutralizer cathodes, a Hall thruster typically uses a single cathode mounted externally that does both jobs simultaneously. The cathode must emit 2–15 A continuously — matching the discharge current — with a lifetime of 15,000–25,000 hr. See [Electric Propulsion — Hall](./electric-hall.md) for the integrated context.

## Process Description

1. **Emitter fabrication**: porous tungsten is sintered and machined to a cylindrical insert (3–6 mm OD, 10–25 mm length), then impregnated with BaO-CaO-Al₂O₃ (B-type emitter).
2. **Orifice plate machining**: a tungsten disc with a precision-bored 0.5–2.0 mm aperture is electron-beam welded to the cathode tube, setting the internal xenon pressure.
3. **Heater installation**: a coiled tungsten or refractory metal wire heater is wound around the cathode body, insulated with alumina.
4. **Keeper assembly**: a molybdenum keeper electrode ring is positioned 1–3 mm downstream of the orifice plate.
5. **Vacuum brazing and leak check**: the assembled cathode is vacuum-brazed and helium leak-checked to <10⁻⁹ Pa·m³/s.
6. **Conditioning**: the cathode is activated by heating under vacuum to drive off absorbed gases and initiate BaO migration to the emitter surface.

## Key Parameters

- **Emission current**: 2–15 A (equals the Hall thruster discharge current)
- **Emitter temperature**: 1100–1300°C (BaO thermionic emission regime)
- **Keeper voltage**: 10–25 V DC (sustains cathode plasma)
- **Heater power**: 12–80 W (preheat only)
- **Propellant flow**: 0.3–2.0 mg/s xenon through cathode insert (5–10% of total flow)
- **Orifice diameter**: 0.5–2.0 mm (tungsten, precision-bored)
- **Coupling voltage**: 10–30 V drop between cathode plasma and beam plasma
- **Lifetime**: 15,000–25,000 hr (BaO depletion-limited)

## Prerequisites

- Porous tungsten sintering and BaO impregnation
- Tungsten orifice electron-beam welding
- Vacuum brazing and helium leak detection

## See Also

- [Electric Propulsion — Hall](./electric-hall.md) — parent capability
- [Hall Thruster Design](./electric-hall.hall-thruster-design.md) — cathode integration
- [Neutralizer Design](./electric-ion.neutralizer-design.md) — analogous ion thruster cathode

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
