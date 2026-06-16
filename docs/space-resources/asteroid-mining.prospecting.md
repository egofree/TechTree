# Asteroid Prospecting

> **Node ID**: space-resources.asteroid-mining.prospecting
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.asteroid-mining`](./asteroid-mining.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: asteroid_prospect_data
> **Critical**: No

Spectral survey of near-Earth asteroids using near-infrared reflectance spectroscopy to identify composition, hydration state, and metal content before committing a mining mission. See [Asteroid Mining](./asteroid-mining.md) for the integrated capability context.

## Overview

The workhorse technique is near-infrared reflectance spectroscopy across the 1-2.5 micron range, where diagnostic absorption bands reveal mineralogy. The 2.7 micron O-H stretch identifies hydrated phyllosilicates in carbonaceous chondrites; the 1.0 and 2.0 micron Fe2+ bands discriminate pyroxene and olivine in S-types; and the red spectral slope at 0.5-0.7 micron flags free Ni-Fe metal in M-types. Space-based survey telescopes (NEO Surveyor, 4-10 micron thermal IR) discover and categorize the population; rendezvous spacecraft then measure density, thermal inertia, and surface roughness up close.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| NIR survey range | 1.0-2.5 micron |
| O-H hydration band | 2.7-2.9 micron |
| Fe2+ pyroxene bands | 1.0, 2.0 micron |
| Organic C-H feature | 3.4 micron |
| Thermal inertia (regolith) | 30-100 J m^-2 K^-1 s^-1/2 |
| Thermal inertia (rock) | 500-2500 J m^-2 K^-1 s^-1/2 |

## Prerequisites

- Multispectral and hyperspectral imaging payloads ([optics](../optics/))
- Spacecraft rendezvous and proximity operations ([spacecraft systems](../spacecraft-systems/))
- Spectral libraries of meteorite analogs ([chemistry](../chemistry/))

## See Also

- [Asteroid Mining](./asteroid-mining.md) — parent capability
- [Extraction Methods](./asteroid-mining.extraction-methods.md) — downstream processing
- [Water Extraction](./asteroid-mining.water-extraction-asteroid.md) — hydration recovery

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md)*
