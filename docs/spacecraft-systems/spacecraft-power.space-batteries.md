# Space Batteries

> **Node ID**: spacecraft-systems.spacecraft-power.space-batteries
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.spacecraft-power`](./spacecraft-power.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: space_batteries
> **Critical**: No

Spacecraft rechargeable batteries provide electrical energy during eclipse periods when solar arrays produce no output. Three chemistries dominate: lithium-ion (150-200 Wh/kg, 3.6V/cell, the modern standard), nickel-hydrogen (45-65 Wh/kg, 1.2V, exceptional 35,000-cycle LEO life), and nickel-cadmium (40-60 Wh/kg, legacy heritage). Battery sizing follows the eclipse energy budget: a GEO commsat requires 6-12 kWh capacity, while a LEO earth-observation satellite needs 300-1200 Wh.

## Key Parameters

| Parameter | Li-ion | NiH₂ | NiCd |
|-----------|--------|------|------|
| Cell voltage | 3.6-3.7V | 1.2V | 1.2V |
| Energy density | 150-200 Wh/kg | 45-65 Wh/kg | 40-60 Wh/kg |
| Cycle life (50% DoD) | 20,000-30,000 | 30,000-35,000 | 10,000-20,000 |
| Operating temp | 0 to +30°C | -10 to +20°C | -5 to +25°C |

## Process Overview

1. **Cell screening**: Screening for capacity matching (±2%), internal resistance, and cycle life
2. **Pack assembly**: Series-parallel cell grouping, busbar welding, thermal rail mounting
3. **Battery management electronics**: Per-cell voltage monitoring, temperature sensing, charge balancing
4. **Thermal integration**: Mounting on dedicated radiator panel with heat pipes or conductive doublers
5. **Qualification**: Vibration, thermal vacuum cycling, charge-discharge profile validation

## Prerequisites

- Energy.batteries capability (electrochemical storage fundamentals)
- Thermal control subsystem for battery temperature regulation
- Vacuum-qualified cell packaging (hermetic seals for NiH₂ pressure vessels)

## See Also

- [Spacecraft Power Systems](./spacecraft-power.md) — parent capability
- [Power Management and Distribution](./spacecraft-power.power-management-distribution.md) — battery charge control
- [Battery & Electrochemical Storage](../energy/batteries.md) — terrestrial battery heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
