# Turbofan Engines

> **Node ID**: aerospace.jet-propulsion.turbofan
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.jet-propulsion`](jet-propulsion.md)
> **Timeline**: Years 35-55+
> **Outputs**: turbofan_engines
> **Critical**: No

The turbofan adds a front fan — a large low-pressure compressor that moves a stream of bypass air around the engine core. The bypass air does not pass through the combustor or turbine; it exits directly through a separate nozzle at moderate velocity, producing additional thrust with high propulsive efficiency. The core (gas generator) operates as a turbojet, but its turbine extracts extra work to drive the fan via a separate shaft.

The **bypass ratio** (BPR) — the ratio of bypass air mass flow to core air mass flow — is the defining parameter. Propulsive efficiency η_p = 2v / (v + v_e) improves as bypass ratio increases because the average exhaust velocity drops closer to the flight speed. High-bypass turbofans (BPR 5:1 to 12:1) dominate commercial aviation: they are quieter (exhaust noise ∝ v⁸), more fuel-efficient (SFC 0.35-0.55 kg/daN·h), and produce more thrust at takeoff and low speed. Low-bypass turbofans (BPR 0.3:1 to 1:1) serve military fighters, trading efficiency for compact frontal area and high specific thrust for supersonic performance.

## Shaft Architecture

Modern turbofans use two or three concentric shafts (spools), each connecting a turbine to a compressor or fan running at its optimal speed. A **two-spool** layout (low-pressure spool: fan + LPT; high-pressure spool: HPC + HPT) is standard. A **three-spool** layout (Rolls-Royce Trent, RB211) adds an intermediate-pressure spool, allowing each component to rotate at its aerodynamic optimum but adding mechanical complexity. Geared turbofans (Pratt & Whitney GTF) introduce a reduction gearbox between the LP turbine and the fan, letting the fan turn slower (3,000 RPM) while the turbine runs faster (10,000+ RPM), each at peak efficiency.

## Prerequisites

- [Turbojet](jet-propulsion.turbojet.md) — core gas generator technology
- [Large-diameter fan blades](../metals/aluminum.md) — hollow titanium or composite fan blades
- [Multi-spool shaft design](../machine-tools/index.md) — concentric bearing systems, intershaft seals
- [Composite fan casing](jet-propulsion.md) — containment for blade-off failure modes
- [Kerosene jet fuel](../chemistry/petroleum-alternatives.md) — Jet A-1 supply for commercial operations

## See Also

- [Jet Propulsion](jet-propulsion.md) — parent capability overview
- [Turbojet Engines](jet-propulsion.turbojet.md) — core cycle
- [Afterburners](jet-propulsion.afterburner.md) — low-bypass military augmentation
- [Gas Turbines](../energy/gas-turbine.md) — turbomachinery foundation

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
