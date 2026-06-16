# Oxygen Extraction

> **Node ID**: `space-resources.lunar-isru.oxygen-extraction`
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.lunar-isru`](./lunar-isru.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: lunar_oxygen
> **Critical**: No

## Overview

Lunar oxygen extraction liberates the 42–45% oxygen by mass locked in regolith oxides. Two principal routes: **molten regolith electrolysis (MRE)** at 1600°C yielding up to ~900 kg O₂ per metric ton regolith (theoretical), and **hydrogen reduction of ilmenite** (FeTiO₃ + H₂) at 1000°C. Both exploit the fact that oxygen is the single most abundant element in lunar soil.

See the parent capability [Lunar ISRU](lunar-isru.md) for full reaction stoichiometry, yields, and energy budgets.

## Process Description

1. **Feed**: Beneficiated regolith (or ilmenite concentrate) is metered into the reactor.
2. **MRE route**: Regolith is melted at 1600°C; electrolysis splits the molten oxide, releasing O₂ at the anode and metal slag at the cathode.
3. **Ilmenite route**: H₂ gas is passed through heated ilmenite at 1000°C; the reaction FeTiO₃ + H₂ → Fe + TiO₂ + H₂O produces water vapor, which is electrolyzed to recover H₂ and yield O₂.
4. **Collection**: O₂ is purified, compressed, and stored as gas or cryogenic LOX.

## Key Parameters

| Parameter | MRE | H₂ Reduction |
|-----------|-----|--------------|
| Temperature | 1600°C | 1000°C |
| O₂ yield | ~250–450 kg/ton (plant) | 3.5–10.5 kg/ton (raw regolith) |
| Energy | 20–30 kWh/kg O₂ | 10–15 kWh/kg O₂ |
| Byproduct | Metal-silicon slag | Iron, TiO₂ |

## Safety

MRE reactors operate at 1600°C with no convective cooling in vacuum — exterior surfaces radiate to space and cause severe burns on contact. The closed-loop H₂ in the ilmenite process is flammable over 4–75% in residual oxygen, requiring leak detection and inerting.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md) • [Lunar ISRU](lunar-isru.md)*
