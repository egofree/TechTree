# LOX Production

> **Node ID**: `launch-vehicles.propellant-production.lox-production`
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.propellant-production`](./propellant-production.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: lox
> **Critical**: No

## Overview

Liquid oxygen (LOX) is the oxidizer for the majority of orbital launch vehicles, used with RP-1 (kerosene), LH2 (hydrogen), and CH4 (methane) fuel combinations. LOX is produced by cryogenic air separation — cooling atmospheric air to liquefaction and distilling the oxygen from nitrogen using their 13°C boiling point difference. The product is stored at -183°C (90.2 K) at near-ambient pressure.

See the parent capability [Propellant Production](propellant-production.md) for full production specifications, boil-off rates, and production scale figures.

## Process Description

1. **Air compression**: Filtered atmospheric air is compressed to 5-6 bar in a multi-stage centrifugal or reciprocating compressor with intercooling.
2. **Purification**: Compressed air passes through molecular sieve adsorbers (13X zeolite) that remove water vapor, CO₂, and trace hydrocarbons to PPB levels. This prevents freezing in the cold box and explosive acetylene accumulation in the LOX bath.
3. **Cooling**: The purified air is cooled against returning cold product streams in brazed aluminum plate-fin heat exchangers, approaching the liquefaction temperature.
4. **Expansion and liquefaction**: Part of the air stream is expanded through a Claude-cycle expansion turbine (20,000-80,000 RPM), extracting work and dropping temperature. The remainder is throttled through a Joule-Thomson valve.
5. **Double-column distillation**: The liquefied air enters the lower column (5 bar). Crude nitrogen is drawn from the top; oxygen-rich liquid (38-40% O₂) from the bottom is fed to the upper column (1.3 bar) for final separation to 99.5%+ O₂ purity.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Purity | 99.5%+ O₂ (rocket grade) |
| Storage temperature | -183°C (90.2 K) |
| Density | 1141 kg/m³ |
| Boil-off rate | 0.5-2.0%/day (tank dependent) |
| Energy cost | 200-400 kWh/tonne LOX (air separation) |

## Safety

LOX causes organic materials (oil, grease, asphalt, clothing) to become explosively combustible. All LOX-contact surfaces must be degreased and certified "LOX-clean." Concrete (not asphalt) flooring is mandatory in LOX handling areas.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [Propellant Production](propellant-production.md)*
