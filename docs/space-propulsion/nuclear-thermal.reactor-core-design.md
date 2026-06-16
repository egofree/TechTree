# Reactor Core Design

> **Node ID**: space-propulsion.nuclear-thermal.reactor-core-design
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.nuclear-thermal`](./nuclear-thermal.md)
> **Enables**: ntp_engines
> **Timeline**: Years 40-200+
> **Outputs**: ntp_engines
> **Critical**: No

The NTP reactor core is a compact fission reactor optimised to heat hydrogen propellant directly to 2500-3000 K. Unlike stationary power reactors (see [Nuclear Fission Power](../energy/nuclear-fission.md)) that prioritise decades of operation at modest temperature, an NTP core prioritises minutes of operation at extreme temperature with hydrogen as the coolant. This process is part of the [Nuclear Thermal Propulsion](./nuclear-thermal.md) capability.

## Fuel Classes

Three fuel families have been ground-tested for NTP service:

- **Graphite-matrix UC** — the NERVA baseline; coated in ZrC or NbC to resist hydrogen attack
- **CERMET (W-UO₂ or Mo-UO₂)** — ceramic fuel in refractory metal matrix; higher temperature (3000 K)
- **TRISO coated particle** — UN or UC kernels in pyrocarbon/SiC multilayer shells; modern approach

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Thermal power | 0.5-4 GW |
| Power density | 0.1-0.25 GW/m³ |
| Fuel temperature | 2500-3000 K |
| Propellant exit temperature | ~2700 K |
| Hydrogen flow rate | 10-40 kg/s |
| Enrichment | 20-93% U-235 |
| Burn duration | 30-120 min/burn |

## Prerequisites

- [Nuclear Fission Power](../energy/nuclear-fission.md) — reactor neutronics and fuel-cycle chemistry
- Refractory-metal fabrication (tungsten, molybdenum, niobium) from [metals](../metals/index.md)
- Hydrogen-compatible CVD coatings (ZrC, NbC) from [ceramics](../metals/index.md)

## See Also

- [Nuclear Thermal Propulsion](./nuclear-thermal.md) — the parent capability
- [Propellant Feed](./nuclear-thermal.propellant-feed.md) — LH2 delivery to the core

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md) • [All Domains](../index.md)*
