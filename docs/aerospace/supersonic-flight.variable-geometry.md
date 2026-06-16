# Variable-Geometry Flight Surfaces

> **Node ID**: `aerospace.supersonic-flight.variable-geometry`
> **Domain**: [Aerospace](./index.md)
> **Parent**: [Supersonic & Hypersonic Flight](./supersonic-flight.md)
> **Dependencies**: [`aerospace.supersonic-flight`](supersonic-flight.md)
> **Outputs**: swing_wing_mechanism, variable_inlet, adjustable_nozzle
> **Timeline**: Years 35-90
> **Critical**: No

## Overview

A wing optimized for Mach 2 cruise is a poor wing for takeoff and landing. The variable-geometry process solves this by building flight surfaces that reconfigure in flight: swing-wings that pivot aft for supersonic dash and forward for low-speed handling, variable supersonic inlets that reposition their terminal shock as Mach number changes, and convergent-divergent nozzles with adjustable throat area to match exhaust pressure to ambient.

Three mechanisms define the field. The **swing-wing** (F-111 Aardvark, F-14 Tomcat, Panavia Tornado, MiG-23, B-1B Lancer) pivots the outer wing panels on a massive titanium forging — the F-14 pivot weighed 1,100 kg per side and was fatigue-critical. The **variable inlet** uses translating spikes (SR-71) or hinged ramps (F-15, Concorde) to keep the terminal normal shock positioned for efficient compression across the flight envelope; the SR-71's axisymmetric spikes translated up to 66 cm aft. The **adjustable nozzle** (convergent-divergent, with variable throat and exit area) matches the engine exhaust to ambient pressure, critical for afterburner operation and efficient supersonic expansion.

See the parent [Supersonic & Hypersonic Flight](./supersonic-flight.md) article for the trade-offs that drove these mechanisms, and for why Concorde chose a fixed delta instead.

## Key Mechanisms

- **Swing-wing pivot** — titanium forging carrying full wing bending load; 20–68° sweep range.
- **Mixed-compression inlet** — 4–5 hinged ramps producing oblique shocks; computer-controlled shock positioning.
- **Variable C-D nozzle** — iris or translating-flap mechanism adjusting throat area 3:1.
- **Engine inlet unstart recovery** — automatic detection and re-positioning when the terminal shock is expelled forward.

## Prerequisites

- **[Aviation](./aviation.md)** — hydraulic and mechanical actuator heritage, structural fatigue practice.
- **[Jet Propulsion](./jet-propulsion.md)** — variable-cycle engine and inlet matching.
- **[Supersonic & Hypersonic Flight](./supersonic-flight.md)** — parent capability.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md)*
