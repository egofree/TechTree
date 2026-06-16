# Turbojet Engines

> **Node ID**: aerospace.jet-propulsion.turbojet
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.jet-propulsion`](jet-propulsion.md)
> **Timeline**: Years 30-50+
> **Outputs**: turbojet_engines
> **Critical**: No

The turbojet is the simplest jet engine: air enters a compressor (centrifugal or axial), is compressed to 5-50 times atmospheric pressure, mixed with fuel and burned in a combustor at constant pressure, then expanded through an axial turbine that extracts just enough work to drive the compressor. The remaining hot gas exits through a propelling nozzle at high velocity, producing thrust.

All air passes through the engine core — there is no bypass stream. This gives the turbojet a high exhaust velocity (600-900 m/s) and high specific thrust (thrust per unit mass flow), making it suitable for high-speed flight where its propulsive efficiency improves. At subsonic speeds, however, the high exhaust velocity wastes kinetic energy: most of the jet's kinetic energy is left in the exhaust plume rather than transferred to useful thrust. Specific fuel consumption is correspondingly high (0.90-1.10 kg/daN·h vs. 0.35-0.55 for modern turbofans).

## Compressor Configurations

**Centrifugal compressor** (Whittle, 1930s): Single-stage impeller achieves 4:1 to 8:1 pressure ratio. Simple, rugged, short, but large frontal area (high drag). Used on early British engines (Welland, Nene) and still common on APUs and small turboshafts.

**Axial compressor** (von Ohain / Griffith, 1930s-40s): 8-17 stages of alternating rotor and stator blade rows, each contributing 1.2:1 to 1.5:1. Small frontal area, scalable to high mass flow. Requires variable inlet guide vanes (VIGVs) and intermediate-stage bleed valves to prevent stall at low speeds. Dominant configuration since the 1950s.

## Prerequisites

- [Gas turbine turbomachinery](../energy/gas-turbine.md) — compressor, combustor, and turbine stage design
- [Superalloy casting](../metals/aluminum.md) — nickel-base alloy turbine blades and discs
- [Kerosene jet fuel](../chemistry/petroleum-alternatives.md) — Jet A-1 / JP-8 supply chain
- [Precision machine tools](../machine-tools/index.md) — compressor blade profiling, disc boring, shaft grinding
- [Combustor design](jet-propulsion.md) — fuel atomization, flame stabilization, liner cooling

## See Also

- [Jet Propulsion](jet-propulsion.md) — parent capability overview
- [Turbofan Engines](jet-propulsion.turbofan.md) — bypass-air derivative
- [Gas Turbines](../energy/gas-turbine.md) — turbomachinery foundation

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
