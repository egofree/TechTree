# Control Circuits

> **Node ID**: electronics.control-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.electrical-systems`](electrical-systems.md)
> **Timeline**: Years 15-35
> **Outputs**: control-circuit-design
> **Critical**: No — control-circuit design pedagogy builds on electrical systems and computing logic; it organizes relay/ladder/discrete-logic knowledge rather than gating a primary bootstrap dependency

Control circuits are the electromechanical and discrete-logic layer that sequences industrial machinery — starting and stopping motors, interlocking guards, timing operations, and implementing AND/OR/NOT decisions in hardware before programmable controllers existed. This capability is the **design pedagogy** layer: how to read, draw, and reason about these circuits from first principles, starting from the Edison-era relay and progressing to the discrete/sequential logic that bridged electromechanics and semiconductors.

## Scope and Progression

This capability is a **hub** for three process articles, taught in historical and conceptual order:

1. **Relay logic** — The hardware foundation. Relays and contactors implement Boolean functions physically: normally-open (NO) contacts in series perform AND, in parallel perform OR, normally-closed (NC) contacts perform NOT. Seal-in (latching) circuits give memory. Timer relays give sequencing. This is the Edison-era control paradigm and the direct ancestor of every programmable controller. *(Process article: [relay-logic](control-circuits.relay-logic.md))*
2. **Ladder logic** — The diagram *notation* and methodology for relay-logic circuits: the rung/rail form, contact/coil symbols (XIC/XIO/OTE), latch/timer/counter rungs, and the scan-cycle concept that later carried over to PLCs. Ladder logic is how control engineers document and debug relay panels. *(Process article: [ladder-logic](control-circuits.ladder-logic.md))*
3. **Discrete and sequential logic** — The circuit-level bridge from relays to semiconductors: building gates, flip-flops, counters, and state machines from discrete transistors and early ICs to implement the same control functions electromechanically, at higher speed and reliability. *(Process articles: [discrete-logic-circuits](control-circuits.discrete-logic-circuits.md), [sequential-logic-circuits](control-circuits.sequential-logic-circuits.md))*

## Boundary With Computing

This capability owns circuit-level control **hardware and notation**. It does **not** re-teach the computing-domain abstractions built on top of these circuits:

- **Boolean algebra, HDL, and FPGA design** live in [`computing.digital-logic`](../computing/digital-logic.md) and [`computing.logic-design`](../computing/logic-design.md). Cross-link there; do not duplicate.
- **Programmable controllers (PLC hardware architecture, SCADA, HMI)** live in [`electronics.industrial-control`](industrial-control.md) and are previewed in [`computing.embedded-systems`](../computing/embedded-systems.md). This capability teaches the *logic* those controllers execute; the controller *platform* is the industrial-control capability.

## Prerequisites

- **Relays, contactors, and wiring** from [`electronics.electrical-systems`](electrical-systems.md) — the physical components relay logic is built from.
- **DC circuit fundamentals** (Ohm's law, series/parallel, contact ratings) — covered in the circuit-fundamentals track.
- Relay history and electromechanical context in [`computing.electromechanical`](../computing/electromechanical.md) (cross-link only).

## Why It Matters

Every automated factory line, motor-control panel, and safety interlock system descends from relay-logic design practice. Understanding how to compose NO/NC contacts into seal-in circuits, interlocks, and timed sequences is the prerequisite to programming PLCs (which still execute ladder logic today, via IEC 61131-3) and to designing the discrete-logic hardware that preceded microcontrollers. This capability preserves the design pedagogy that connects physical switchgear to programmable control.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](./index.md)*
