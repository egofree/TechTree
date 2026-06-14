# Industrial Control

> **Node ID**: electronics.industrial-control
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`computing.embedded-systems`](../computing/embedded-systems.md)
> **Timeline**: Years 30-55
> **Outputs**: industrial-control-system
> **Critical**: No — industrial-control architecture integrates existing computing and control-circuit capabilities into system-level platforms (PLC/SCADA/HMI); it organizes integration knowledge rather than gating a primary bootstrap dependency

Industrial control is the system-architecture layer that orchestrates factories and process plants: programmable logic controllers (PLCs) execute control logic, supervisory control and data acquisition (SCADA) systems aggregate and supervise across sites, and human-machine interfaces (HMIs) give operators visibility and command. This capability is the **design pedagogy** layer for integrating these platforms into a coherent control architecture — progressing from the single PLC up to distributed supervisory systems.

## Scope and Progression

This capability is a **hub** for process articles covering the industrial-control stack, taught from the controller upward:

1. **PLC (Programmable Logic Controller)** — The rack-mounted industrial computer that replaces relay panels: I/O modules, scan-cycle execution, ladder-logic (and the other IEC 61131-3 languages), and the trade-off of development speed against per-channel cost. The PLC is the packaged embedded system that executes the control logic from [`electronics.control-circuits`](control-circuits.md). *(Process article: [PLC](industrial-control.plc.md))*
2. **SCADA and HMI** — The supervisory and operator-facing layers: SCADA aggregates data from PLCs across a site or region over industrial networks, while HMIs provide local operator screens, alarms, and trending. Together they turn isolated controllers into a supervised, observable system. *(Process articles: [SCADA](industrial-control.scada.md), [HMI](industrial-control.hmi.md))*
3. **Control architecture** — The integration tier: how to partition a plant into controller zones, wire field I/O, select communication protocols (Modbus, PROFIBUS, EtherNet/IP), engineer redundancy and fail-safe behavior, and structure the hierarchy from sensor to enterprise. *(Process article: [industrial-control-architecture](industrial-control.industrial-control-architecture.md))*

## Boundary With Computing

This capability owns the **industrial-control platform and architecture** as an electronics-systems discipline. It does **not** re-teach the embedded-computing substrate those platforms are built on:

- **Embedded-system hardware (MCU/RTOS/FPGA selection, sensor interfacing, interrupt handling, watchdogs)** lives in [`computing.embedded-systems`](../computing/embedded-systems.md), which already covers PLCs as one embedded-system option. This capability cross-links there and focuses on the *industrial-control* concerns: PLC programming models, SCADA topology, HMI design, and plant-wide architecture.
- **Boolean algebra, HDL, and FPGA design** live in [`computing.digital-logic`](../computing/digital-logic.md) and [`computing.logic-design`](../computing/logic-design.md). Cross-link only.
- **Control-circuit logic (relay/ladder/discrete/sequential)** lives in [`electronics.control-circuits`](control-circuits.md) — the logic the PLC executes; this capability covers the controller itself.

## Prerequisites

- **Embedded-systems platform knowledge** from [`computing.embedded-systems`](../computing/embedded-systems.md) — the MCU/PLC/FPGA substrate and the decision framework for choosing among them.
- **Control-circuit logic** from [`electronics.control-circuits`](control-circuits.md) — ladder logic and relay logic that PLCs execute.

## Why It Matters

Industrial control is what turns isolated machines and embedded controllers into a coordinated, observable, operable plant. From the first relay panel through the modern SCADA-supervised factory, the recurring challenge is the same: execute deterministic control logic, give operators visibility, and fail safely. This capability preserves the integration and architecture pedagogy that connects embedded controllers to plant-wide automation — the bridge between electronics design and the automation domain.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](./index.md)*
