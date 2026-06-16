# Hypersonic Thermal Protection

> **Node ID**: `aerospace.supersonic-flight.hypersonic-thermal`
> **Domain**: [Aerospace](./index.md)
> **Parent**: [Supersonic & Hypersonic Flight](./supersonic-flight.md)
> **Dependencies**: [`aerospace.supersonic-flight`](supersonic-flight.md)
> **Outputs**: thermal_protection_system, hot_structure
> **Timeline**: Years 50-120
> **Critical**: No

## Overview

Aerodynamic heating scales with stagnation temperature: T₀ = T(1 + 0.2M²). At Mach 3 in the stratosphere the stagnation temperature is 335 °C — too hot for aluminum, which loses half its strength above 130 °C. At Mach 5 it reaches 1,029 °C. At Mach 10 the air itself dissociates into a plasma. This process produces the materials and systems that keep the airframe intact under those conditions: refractory leading edges, insulation blankets, ablators, and actively fuel-cooled structures.

Four material strategies span the Mach range. For Mach 2–3, **heat-treated aluminum** (Hiduminium RR58, used on Concorde) survives at 130 °C skin temperature. For Mach 3–3.5, **titanium alloys** (Ti-6Al-4V, B-120) take over — the SR-71 was 85% titanium and cruised at 280–430 °C skin temperature. For Mach 5–7, **nickel superalloys** (Inconel X-750) and **carbon-carbon composites** carry the structure hot — the X-15's Inconel skin peaked at 650 °C, its carbon-carbon leading edges higher. For re-entry (Mach 20+), **reinforced carbon-carbon** (Shuttle nose cap, rated 1,650 °C) and **silica tile insulation** (LI-900, 93% air by volume) protect an aluminum airframe that would otherwise melt.

See the parent [Supersonic & Hypersonic Flight](./supersonic-flight.md) article for the stagnation-temperature derivation, the materials temperature table, and the per-aircraft material breakdowns.

## Key Systems

- **Carbon-carbon (C/C) leading edges** — processed by repeated CVI cycles at 1,000–1,500 °C; oxidation-protected with SiC conversion coating.
- **Reinforced carbon-carbon (RCC)** — C/C with a tougher matrix; Shuttle nose cap rated 1,650 °C.
- **Silica tile insulation** — LI-900, 9 lb/ft³ density, bonded to airframe; 24,300 tiles on the Shuttle Orbiter.
- **Ablative TPS** — PICA (phenolic-impregnated carbon ablator); pyrolyzes and chars, carrying heat away.
- **Active cooling** — fuel circulated through leading-edge channels; couples airframe thermal design to propulsion.

## Prerequisites

- **[Ceramics](../ceramics/index.md)** — silica, alumina, zirconia refractory supply; carbon-carbon composite processing.
- **[Metals / Aluminum](../metals/aluminum.md)** — titanium (Kroll process), nickel superalloys (Inconel).
- **[Supersonic & Hypersonic Flight](./supersonic-flight.md)** — parent capability.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md)*
