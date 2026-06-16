# Portable Life Support System

> **Node ID**: `human-spaceflight.space-suits.plss-design`
> **Domain**: [Human Spaceflight](./index.md)
> **Parent**: [Space Suits](./space-suits.md)
> **Dependencies**: [`human-spaceflight.space-suits`](./space-suits.md)
> **Outputs**: portable_life_support_systems, oxygen_loops, thermal_rejection_packs
> **Timeline**: Years 50-200+

## Overview

The Portable Life Support System (PLSS) is the backpack that turns a pressure garment into a
self-contained spacecraft. It carries every consumable needed to keep a human alive for a full
EVA: oxygen, CO2 scrubber, humidity and thermal control, power, and communications. The EMU
PLSS delivers 8.4 hours of autonomous life support at 4.3 psi pure O2.

## Components

| Component | Function | Spec (EMU) |
|-----------|----------|------------|
| Primary O2 tank | Breathing gas, pressurisation | 0.55 kg @ 20.7 MPa |
| Contingency O2 | Emergency 30-min backup | 0.5 kg @ 41.4 MPa |
| LiOH canister | CO2 scrubber | Keeps pCO2 < 0.5 kPa for 8 hr |
| Sublimator | Heat rejection to vacuum | 730 W peak |
| Heat exchanger | Dehumidifies loop | Removes 0.2-0.5 kg H2O/EVA |
| Ventilation fan | O2 circulation | 0.17 m3/min |
| Battery | Fan, pumps, radios | 11.6 Ah silver-zinc |

## Oxygen Loop

The O2 loop is partially open: pure O2 is metered from the tank, breathed once, scrubbed of
CO2, dehumidified, and recirculated. Leakage and metabolic consumption require continuous
make-up; the primary tank lasts ~8.4 hours at nominal load.

## Thermal Loop

Closed-loop water through the LCVG picks up body heat, runs through the sublimator (where
feedwater freezes to ice and sublimes to vacuum, carrying heat away), and returns chilled.
Handles 100-300 W metabolic load, peak 500 W short.

## See Also

- [Space Suits](./space-suits.md) — parent capability
- [Pressure Garment Design](./space-suits.pressure-garment.md) — suit shell
- [Thermal Control Suit](./space-suits.thermal-control-suit.md) — LCVG interface

---

*Part of the [Bootciv Tech Tree](../index.md) • [Human Spaceflight](./index.md) • [All Domains](../index.md)*
