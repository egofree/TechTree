# Extraction Methods

> **Node ID**: space-resources.asteroid-mining.extraction-methods
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.asteroid-mining`](./asteroid-mining.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: asteroid_materials
> **Critical**: No

Recovery of metals and minerals from asteroid regolith via thermal volatilization, magnetic separation of free metal grains, and chemical leaching of the silicate matrix. See [Asteroid Mining](./asteroid-mining.md) for the integrated capability context.

## Overview

Three complementary techniques cover the resource range. **Thermal volatilization** heats regolith to 1200-2000 C under vacuum, vaporizing volatile metals and sulfur that recondense on a graded cold trap, fractionally separating elements by vapor pressure. **Magnetic separation** pulls free Fe-Ni metal grains (kamacite, taenite) from comminuted regolith using a rotating drum or superconducting separator — the lowest-energy beneficiation step. **Chemical leaching** dissolves platinum-group metals and rare earths from the silicate matrix using imported acid, then electrochemically plates them out; reserved for high-value, low-concentration recovery.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Volatilization temperature | 1200-2000 C |
| Magnetic separation energy | 1-5 kWh/tonne |
| PGM grade (iron meteorites) | 10-100 ppm |
| Kamacite Ni content | 5-7% |
| Taenite Ni content | 30-60% |
| Comminution energy | 10-30 kWh/tonne |

## Prerequisites

- Solar concentrators for thermal process heat ([energy](../energy/))
- Comminution and beneficiation equipment ([mining](../mining/))
- Autonomous excavation and handling ([automation](../automation/))

## See Also

- [Asteroid Mining](./asteroid-mining.md) — parent capability
- [Asteroid Prospecting](./asteroid-mining.prospecting.md) — target characterization
- [Water Extraction](./asteroid-mining.water-extraction-asteroid.md) — volatile recovery

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md)*
