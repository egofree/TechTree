# Ramjet and Scramjet Engines

> **Node ID**: aerospace.jet-propulsion.ramjet-scramjet
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.jet-propulsion`](jet-propulsion.md)
> **Timeline**: Years 50-80+
> **Outputs**: ramjet_engines
> **Critical**: No

The ramjet eliminates all rotating turbomachinery — no compressor, no turbine. Instead, forward speed rams air into the inlet, where a series of shock waves (oblique shocks from the inlet cone or ramp, terminating in a normal shock) decelerates the air from supersonic flight speed to subsonic velocity, raising its pressure and temperature. This aerodynamic compression substitutes for the mechanical compressor. Fuel is injected, mixed, and burned in a subsonic combustor at constant pressure; the hot gas expands through a convergent-divergent nozzle, producing thrust.

A ramjet produces **no static thrust** — it cannot start or accelerate from rest. It must be boosted to Mach 3-4 by a rocket, turbojet, or launch platform before the inlet compression is sufficient to sustain combustion. The ramjet's advantage is simplicity (few moving parts) and high specific thrust at Mach 3-6, where turbojets are limited by turbine inlet temperature and compressors are stressed by high inlet temperatures.

A **scramjet** (supersonic combustion ramjet) eliminates the normal shock in the inlet — air remains supersonic throughout the combustor. Fuel must mix and burn in a supersonic flow stream in milliseconds (residence time 1-2 ms before the gas exits the combustor). This is extraordinarily difficult: hydrogen (very fast flame speed, wide flammability limits) is the fuel of choice for most scramjet demonstrators, though hydrocarbon scramjets have been tested. Scramjets operate from Mach 4-5 to Mach 12-15, filling the gap between turbojets (Mach <3) and rockets.

## Prerequisites

- [Supersonic inlet design](../energy/gas-turbine.md) — shock system management, variable geometry
- [High-temperature structures](../metals/aluminum.md) — refractory alloys, actively cooled walls
- [Ceramic thermal protection](jet-propulsion.md) — TBC on combustor and nozzle surfaces
- [Rocket or turbojet booster](jet-propulsion.turbojet.md) — acceleration to ignition Mach number
- [Supersonic fuel injection](../chemistry/petroleum-alternatives.md) — fast-mixing hydrogen or hydrocarbon injectors

## See Also

- [Jet Propulsion](jet-propulsion.md) — parent capability overview
- [Turbojet Engines](jet-propulsion.turbojet.md) — boost-phase engine
- [Gas Turbines](../energy/gas-turbine.md) — Brayton cycle thermodynamics

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
