# LH2 Production

> **Node ID**: `launch-vehicles.propellant-production.lh2-production`
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.propellant-production`](./propellant-production.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: lh2
> **Critical**: No

## Overview

Liquid hydrogen (LH2) is the highest-specific-impulse chemical rocket fuel (Isp ~450 s with LOX). It is produced by generating gaseous hydrogen, purifying it to 99.999%, and liquefying it to -253°C (20.3 K). The production chain is the most energy-intensive in the propellant family — approximately 50 kWh/kg total from natural gas, or 65-75 kWh/kg from electrolysis.

See the parent capability [Propellant Production](propellant-production.md) for full specifications, para-ortho conversion details, and storage challenges.

## Process Description

1. **Hydrogen generation (SMR route)**: Methane and steam react over a nickel catalyst at 700-1000°C: CH₄ + H₂O → CO + 3H₂. The syngas undergoes water-gas shift (CO + H₂O → CO₂ + H₂) to maximize H₂ yield.
2. **Hydrogen generation (electrolysis route)**: Water is split by electricity in an alkaline (KOH) or PEM electrolyzer: 2H₂O → 2H₂ + O₂. Energy cost: 50-80 kWh/kg H₂.
3. **Purification**: Hydrogen gas is purified to 99.999% via pressure swing adsorption (PSA), removing CO₂, CO, CH₄, and H₂O.
4. **Pre-cooling**: Hydrogen gas is cooled to ~80 K using liquid nitrogen heat exchange.
5. **Liquefaction**: A multi-stage Claude cycle (helium or hydrogen working fluid) cools the gas to 20.3 K. Expansion turbines provide the final temperature drop. Energy cost: ~13 kWh/kg.
6. **Para-ortho conversion**: An iron(III) hydroxide or chromia catalyst bed converts ortho-hydrogen to para-hydrogen during cooling, reaching >95% para at 20 K. This prevents the exothermic conversion that would otherwise boil off ~6%/day of stored LH2.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Storage temperature | -253°C (20.3 K) |
| Density | 70.8 kg/m³ |
| Para-hydrogen content | >95% (required for stable storage) |
| Boil-off rate | 0.1-1.0%/day (tank dependent) |
| Energy cost (SMR route) | ~50 kWh/kg |
| Energy cost (electrolysis) | ~65-75 kWh/kg |

## Safety

Hydrogen burns with a nearly invisible flame in daylight. The flammability range in air is 4-75% — the widest of any common fuel. Tanks and lines must be austenitic stainless steel (304L/316L) or aluminum to prevent hydrogen embrittlement.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [Propellant Production](propellant-production.md)*
