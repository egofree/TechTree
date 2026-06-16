# Atmosphere Management

> **Node ID**: human-spaceflight.eclss.atmosphere-management
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.eclss`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: eclss_systems
> **Critical**: Yes

Atmosphere management maintains a breathable cabin environment for crewed spacecraft by controlling total pressure (97.9-102.7 kPa), oxygen partial pressure (19.5-23.1 kPa), carbon dioxide partial pressure (< 0.7 kPa daily mean), and a suite of trace contaminants within their SMAC limits. The subsystem encompasses nitrogen ballast makeup, oxygen generation via water electrolysis, regenerable CO2 removal via zeolite molecular sieves, and activated-charcoal polishing of trace volatile organics.

For a 6-crew vehicle the OGS produces up to 5.4 kg of O2 per day from 4.9 kg of water, while the CDRA scrubs approximately 6 kg of CO2 per day across two paired zeolite beds cycling between cabin-air adsorption and space-vacuum desorption. Hydrogen from electrolysis is reacted with waste CO2 in the Sabatier reactor (CO2 + 4 H2 → CH4 + 2 H2O) to recover roughly half of the hydrogen as water.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Total cabin pressure | 97.9-102.7 kPa | Sea-level 101.3 kPa reference |
| O2 partial pressure | 19.5-23.1 kPa | Below 16 kPa hypoxic; above 32 kPa fire hazard |
| CO2 partial pressure | < 0.7 kPa daily mean | Symptoms > 2 kPa |
| O2 generation rate | 5.4 kg/day (6 crew) | Via water electrolysis |
| CDRA CO2 removal | 0.18 kg/hr per assembly | Power 200-400 W |
| Sabatier water recovery | 50% of H2 loop | Methane vented |
| Charcoal bed lifetime | 1-2 years | 5-15 kg activated carbon |

## Prerequisites

- [Chemistry](../chemistry/index.md) — Sabatier and electrolysis reactions
- [Gas Handling](../gas-handling/index.md) — O2/N2 storage and distribution
- [Environmental Control & Life Support](./eclss.md) — parent capability

## See Also

- [ECLSS](./eclss.md) — parent capability
- [Thermal & Humidity Control](./eclss.thermal-humidity-control.md) — sibling process
- [Water Recovery](./eclss.water-recovery.md) — supplies OGS feed water
