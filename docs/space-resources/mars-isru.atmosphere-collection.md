# Atmosphere Collection

> **Node ID**: `space-resources.mars-isru.atmosphere-collection`
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.mars-isru`](./mars-isru.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: mars_propellant
> **Critical**: No

## Overview

The Martian atmosphere is 95.3% CO₂ but at only 6–10 mbar surface pressure — so ISRU begins by compressing the atmosphere roughly 100× to reach reactor pressure (~1 bar). The CO₂ is then split by **solid-oxide electrolysis (SOXE)** at 800°C: 2CO₂ → 2CO + O₂. The MOXIE flight demonstration produced ~10 g/hr O₂ from atmospheric CO₂ at this rate.

See the parent capability [Mars ISRU](mars-isru.md) for atmosphere composition, MOXIE specifications, and integration with Sabatier methanation.

## Process Description

1. **Intake**: Dust-filtered Martian atmosphere is drawn into a sorption pump (zeolite 13X bed).
2. **Adsorption/release**: The bed captures CO₂ during the cold night, then releases concentrated CO₂ when warmed during the day.
3. **Compression**: A scroll or diaphragm compressor boosts CO₂ to 1–30 bar.
4. **Electrolysis**: The SOXE stack (ScSZ electrolyte, 800°C) splits CO₂ into O₂ (product) and CO (byproduct/recycled).

## Key Parameters

| Parameter | Value |
|-----------|-------|
| CO₂ content | 95.3% of atmosphere |
| Surface pressure | 6–10 mbar |
| Compression ratio | ~100× to 1 bar |
| SOXE temperature | 800°C |
| O₂ production (MOXIE) | ~10 g/hr |
| Byproduct | CO (2:1 vs O₂) |

## Safety

Carbon monoxide (CO) is the major byproduct — odorless and lethal at 400 ppm over 1 hour. SOXE reactors vent to the Martian atmosphere (not the habitat) and are monitored with electrochemical CO sensors.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md) • [Mars ISRU](mars-isru.md)*
