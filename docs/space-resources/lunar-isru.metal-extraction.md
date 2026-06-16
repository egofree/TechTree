# Metal Extraction

> **Node ID**: `space-resources.lunar-isru.metal-extraction`
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.lunar-isru`](./lunar-isru.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: lunar_oxygen
> **Critical**: No

## Overview

Lunar regolith contains iron (FeO 5–25%), aluminum (Al₂O₃ up to 31% in highlands), and titanium (TiO₂ up to 18% in Ti-rich maria) — the structural metals needed to build surface infrastructure without importing finished stock from Earth. Extraction uses **molten oxide electrolysis**, **carbothermal reduction**, and the **carbonyl process** to win Fe, Al, and Ti from oxides.

See the parent capability [Lunar ISRU](lunar-isru.md) for per-metal routes, energy budgets, and feedstock beneficiation.

## Process Description

1. **Iron**: Co-produced by H₂ reduction of ilmenite, or won by molten oxide electrolysis of FeO-rich melt, or refined via the carbonyl process (Fe + 5CO → Fe(CO)₅ → Fe + 5CO at ~200°C).
2. **Aluminum**: Molten oxide electrolysis of Al₂O₃ at ~2000°C, or carbothermal reduction (Al₂O₃ + 3C → 2Al + 3CO).
3. **Titanium**: FFC Cambridge process — direct electrolysis of TiO₂ in molten CaCl₂, after ilmenite reduction yields the TiO₂ feed.

## Key Parameters

| Metal | Feedstock | Route | Energy |
|-------|-----------|-------|--------|
| Fe | FeO / ilmenite | Carbonyl / electrolysis | 5–10 kWh/kg |
| Al | Al₂O₃ (highlands) | Molten oxide electrolysis | 45–60 kWh/kg |
| Ti | TiO₂ (from ilmenite) | FFC Cambridge (molten salt) | 20–40 kWh/kg |

## Safety

Carbonyl processes produce **iron pentacarbonyl Fe(CO)₅** — highly toxic and flammable. Aluminum electrolysis at 2000°C and molten-salt titanium reduction both present severe thermal and chemical burn hazards; vacuum offers no convective cooling.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md) • [Lunar ISRU](lunar-isru.md)*
