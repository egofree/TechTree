# Propellant Production (Mars)

> **Node ID**: `space-resources.mars-isru.propellant-production-mars`
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.mars-isru`](./mars-isru.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: mars_propellant
> **Critical**: No

## Overview

The integrated **In-Situ Propellant Production (ISPP) plant** combines atmosphere collection, water electrolysis, Sabatier methanation, and cryogenic liquefaction into a single propellant factory. The target is **~7 metric tons of CH₄ and ~5.5 tons of O₂ per Sol campaign** — enough to fuel a crewed ascent vehicle. Stoichiometrically, 1 metric ton of CH₄ requires roughly 17.7 tons of combined H₂O (mined) and atmospheric CO₂ feedstock.

See the parent capability [Mars ISRU](mars-isru.md) for the full mass balance, campaign timing, and power budget.

## Process Description

1. **CO₂ feed**: Sorption pump + compressor deliver 1–30 bar CO₂ from the atmosphere.
2. **SOXE electrolysis**: Part of the CO₂ is split to O₂ (product) and CO (recycled).
3. **Water mining**: Subsurface ice is excavated, melted, and purified.
4. **Water electrolysis**: H₂O → H₂ (Sabatier feed) + O₂ (product).
5. **Sabatier reactor**: CO₂ + 4H₂ → CH₄ + 2H₂O; water returns to electrolyzer.
6. **Liquefaction**: CH₄ (-162°C) and O₂ (-183°C) are liquefied and transferred to the ascent vehicle tanks.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| CH₄ target | ~7 metric tons |
| O₂ target | ~5.5 metric tons |
| CH₄ per feedstock | 1 t CH₄ per ~17.7 t H₂O + CO₂ |
| Power required | 25–40 kWe continuous |
| Production window | ~500 Sols |

## Safety

LOX at -183°C and liquid CH₄ at -162°C cause cryogenic burns and, on mixing, form a detonable gel. Storage tanks are double-walled vacuum vessels with pressure relief. Cryogenic boil-off of 0.1–1.0%/day on Mars means the plant must over-produce to fill tanks before launch.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md) • [Mars ISRU](mars-isru.md)*
