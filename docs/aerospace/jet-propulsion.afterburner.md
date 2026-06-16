# Afterburners

> **Node ID**: aerospace.jet-propulsion.afterburner
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.jet-propulsion`](jet-propulsion.md)
> **Timeline**: Years 35-55+
> **Outputs**: afterburners
> **Critical**: No

An afterburner is a duct mounted downstream of the turbine exhaust that injects and burns additional fuel in the hot, oxygen-rich gas stream. The turbine exhaust still contains 70-75% of the original air's oxygen (the combustor burns at a very lean fuel-air ratio of 1:50 to 1:100, far below stoichiometric). Injecting more fuel and burning it raises the exhaust temperature dramatically — from 700°C at turbine exit to 1,600-1,700°C at the nozzle — increasing exhaust velocity and thrust by 40-70% for short durations.

Afterburners are used for takeoff, transonic acceleration (punching through the Mach 1 drag rise), aerial combat maneuvering, and short-field launch from aircraft carriers. The thrust augmentation comes at a severe fuel cost: specific fuel consumption rises from 0.8 to 2.5-3.5 kg/daN·h in afterburner, limiting sustained afterburner use to minutes. The F-22's F119 engines can supercruise (sustained supersonic flight without afterburner), reducing afterburner dependency, but most fighters still rely on afterburner for combat thrust.

## Variable-Area Nozzle

Afterburner operation increases the exhaust gas temperature (and thus volume by 60-80%) and mass flow (added fuel mass). If the nozzle throat area does not increase, the upstream turbine sees a back-pressure rise that chokes the compressor and causes surge. A **variable-area exhaust nozzle** — typically an iris or "turkey feather" arrangement of overlapping petals that slide radially — increases the throat area by 50-100% when afterburner is engaged, matching the mass flow to the nozzle and keeping the engine operating line stable. The nozzle closes down for dry (non-afterburning) operation to maintain exhaust velocity and thrust.

## Prerequisites

- [Turbojet or turbofan engine](jet-propulsion.turbojet.md) — hot gas source with residual oxygen
- [Variable-area nozzle mechanism](../machine-tools/index.md) — sliding petal nozzle, hydraulic actuators
- [Superalloy flame holders and liners](../metals/aluminum.md) — Inconel 718 spray bars, Hastelloy liner
- [Additional fuel pump capacity](../chemistry/petroleum-alternatives.md) — 3-6× dry fuel flow during afterburner
- [Ignition system](jet-propulsion.md) — hot-streak or spark ignition for sustained flame

## See Also

- [Jet Propulsion](jet-propulsion.md) — parent capability overview
- [Turbofan Engines](jet-propulsion.turbofan.md) — low-bypass military platforms
- [Gas Turbines](../energy/gas-turbine.md) — turbomachinery foundation

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
