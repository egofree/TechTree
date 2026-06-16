# Hypergolic Synthesis

> **Node ID**: `launch-vehicles.propellant-production.hypergolic-synthesis`
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.propellant-production`](./propellant-production.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: hypergolic_propellants
> **Critical**: No

## Overview

Hypergolic propellants ignite spontaneously on contact with each other — no ignition system is required. This reliability makes them the standard choice for spacecraft attitude control thrusters, orbital maneuvering engines, and launch abort systems. The two dominant hypergolic combinations are MMH/N₂O₄ (monomethylhydrazine with dinitrogen tetroxide) and Aerozine 50/N₂O₄ (50/50 hydrazine-UDMH blend). All hypergolics are extremely toxic and require specialized handling infrastructure.

See the parent capability [Propellant Production](propellant-production.md) for the full properties table, handling procedures, and toxicity limits.

## Process Description

### Monomethylhydrazine (MMH) Synthesis

1. **Hydrazine production**: Ammonia (NH₃) is oxidized with sodium hypochlorite (NaOCl) in the Raschig process: 2NH₃ + NaOCl → N₂H₄ + NaCl + H₂O. The hydrazine yield is improved by using a ketone catalyst (Raschig-Schering process with MEK).
2. **Methylation**: Hydrazine reacts with methanol or formaldehyde under acid catalysis to produce monomethylhydrazine: N₂H₄ + CH₂O → CH₃NHNH₂ + H₂O.
3. **Distillation**: MMH is purified by fractional distillation (boiling point 87°C) to >99% purity.

### Dinitrogen Tetroxide (N₂O₄) Synthesis

1. **Ammonia oxidation**: Ammonia is passed over a platinum-rhodium catalyst at 800-900°C: 4NH₃ + 5O₂ → 4NO + 6H₂O.
2. **Oxidation**: Nitric oxide is cooled and oxidized with excess air: 2NO + O₂ → 2NO₂. The NO₂ dimerizes to N₂O₄ at low temperatures.
3. **Liquefaction**: N₂O₄ is condensed to a liquid (boiling point 21°C) and stored in pressurized, passivated stainless steel tanks.

## Key Parameters

| Property | MMH | N₂O₄ |
|----------|-----|------|
| Density (@20°C) | 0.876 g/cm³ | 1.45 g/cm³ |
| Freezing point | -52°C | -11°C |
| Boiling point | 87°C | 21°C |
| Ignition delay (paired) | < 10 ms | — |

## Safety

Both propellants are extremely toxic. MMH is carcinogenic (PEL 0.01 ppm). N₂O₄ decomposes to NO₂, a pulmonary toxin (PEL 5 ppm). All handling requires SCAPE suits (pressure-positive, supplied-air). Fuel and oxidizer storage magazines are separated by intraline distance to prevent propagation.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [Propellant Production](propellant-production.md)*
