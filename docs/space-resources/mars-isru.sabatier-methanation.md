# Sabatier Methanation

> **Node ID**: `space-resources.mars-isru.sabatier-methanation`
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.mars-isru`](./mars-isru.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: mars_propellant
> **Critical**: No

## Overview

The Sabatier reaction produces methane fuel from atmospheric CO₂ and hydrogen: **CO₂ + 4H₂ → CH₄ + 2H₂O** over a ruthenium-on-alumina catalyst at 300–400°C. The reaction is exothermic (self-sustaining once started) and reaches >98% per-pass CO₂ conversion when run at a 5:1 H₂:CO₂ feed ratio. The water byproduct is electrolyzed to close the hydrogen loop.

See the parent capability [Mars ISRU](mars-isru.md) for full stoichiometry, reactor design, and integration with the ISPP plant.

## Process Description

1. **Feed mixing**: CO₂ (from atmosphere collection) and H₂ (from water electrolysis) are mixed at a 5:1 H₂:CO₂ ratio.
2. **Reaction**: The mixture passes over the Ru/Al₂O₃ catalyst bed at 300–400°C; exothermic heat must be removed to hold temperature.
3. **Separation**: Product methane is separated from water and unreacted gases (cryogenic condensation or membrane separation).
4. **Loop closure**: Water is sent to the electrolyzer; excess H₂ is recycled to the reactor inlet.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Catalyst | Ruthenium on alumina (Ru/Al₂O₃) |
| Temperature | 300–400°C |
| H₂:CO₂ feed ratio | 5:1 |
| Per-pass CO₂ conversion | > 98% |
| Methane selectivity | > 99% |
| Byproduct | H₂O (recycled) |

## Safety

Hydrogen is flammable over 4–75% in air; the Sabatier loop operates in a sealed module with H₂ leak detectors and inert-purge capability. Methane is flammable and an asphyxiant; the product stream requires the same cryogenic handling care as terrestrial LNG.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md) • [Mars ISRU](mars-isru.md)*
