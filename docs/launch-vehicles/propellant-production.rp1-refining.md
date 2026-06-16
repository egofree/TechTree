# RP-1 Refining

> **Node ID**: `launch-vehicles.propellant-production.rp1-refining`
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.propellant-production`](./propellant-production.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: rp1
> **Critical**: No

## Overview

RP-1 (Rocket Propellant-1) is a highly refined kerosene developed in the 1950s for use in regeneratively cooled rocket engines. It is denser and far easier to store than LH2, making it the practical choice for large first-stage engines (Merlin, RD-180, F-1). RP-1 is produced by fractionating petroleum distillate and subjecting it to catalytic hydrotreating to reduce sulfur below 30 ppm and aromatics below 1% — preventing coking in engine cooling channels.

See the parent capability [Propellant Production](propellant-production.md) for the full specification table and comparison with jet fuel and diesel.

## Process Description

1. **Crude distillation**: Petroleum crude is fractionally distilled. The kerosene cut (190-270°C boiling range) is drawn off as the RP-1 precursor.
2. **Hydrotreating**: The kerosene cut is mixed with hydrogen and passed over a cobalt-molybdenum (Co-Mo) or nickel-molybdenum (Ni-Mo) catalyst bed at 300-400°C and 30-80 bar. This saturates olefins and aromatics, converting them to stable paraffins.
3. **Hydrodesulfurization**: Sulfur-containing compounds (mercaptans, thiophenes) react with hydrogen over the catalyst to form H₂S, which is removed in an amine scrubber. Target: <30 ppm sulfur.
4. **Clay treating or solvent extraction**: Residual aromatics and polar compounds are removed by percolation through activated bauxite or clay, or by furfural extraction.
5. **Quality testing**: Each batch is tested for density (0.80-0.82 g/cm³), sulfur (<30 ppm), aromatics (<1%), flash point (>60°C), and freezing point (<-47°C) before release.

## Key Parameters

| Parameter | Specification |
|-----------|---------------|
| Density (@15°C) | 0.81 g/cm³ (range 0.80-0.82) |
| Freezing point | ≤ -47°C |
| Flash point | ≥ 60°C |
| Sulfur content | < 30 ppm |
| Aromatics | < 1% by volume |
| Net heat of combustion | ≥ 43.4 MJ/kg |
| Distillation range | 195-275°C |

## Safety

RP-1 is a combustible liquid with a flash point above ambient temperature (60°C), making it safer to handle than gasoline. Standard petroleum fire precautions apply: bonded and grounded transfer equipment, no ignition sources, foam or dry chemical extinguishers.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [Propellant Production](propellant-production.md)*
