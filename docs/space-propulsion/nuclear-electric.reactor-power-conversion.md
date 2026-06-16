# Reactor Power Conversion

> **Node ID**: space-propulsion.nuclear-electric.reactor-power-conversion
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.nuclear-electric`](./nuclear-electric.md)
> **Enables**: nep_systems
> **Timeline**: Years 40-200+
> **Outputs**: nep_systems
> **Critical**: No

Reactor-to-electric power conversion is what turns a fission reactor's thermal output into the 100-1000 kWe of electricity that an NEP vehicle's thrusters need. The reactor itself is documented under [Nuclear Fission Power](../energy/nuclear-fission.md); this process covers the converter — Brayton, Stirling, or thermoelectric — that sits between the reactor heat source and the radiator heat sink. This process is part of the [Nuclear Electric Propulsion](./nuclear-electric.md) capability.

## Converter Technologies

Three converter families have been ground-tested for space reactors:

- **Closed-loop Brayton cycle** — He-Xe working fluid, 25-30% efficiency, baseline for 10-1000 kWe. Heritage: SP-100, JIMO, ISS Brayton experiments
- **Free-piston Stirling cycle** — helium in a sealed cylinder, 25-35% efficiency, best for 1-100 kWe. Heritage: Kilopower / KRUSTY 1 kWe 2018 test
- **Thermoelectric (Seebeck)** — solid-state, 5-8% efficiency, low power. Heritage: RTGs, SNAP-10A 500 We (1965)

## Key Parameters

| Parameter | Brayton | Stirling | Thermoelectric |
|-----------|---------|----------|----------------|
| Efficiency | 25-30% | 25-35% | 5-8% |
| Hot-side temp | 1100 K | 850 K | 800 K |
| Cold-side temp | 350 K | 300 K | 400 K |
| Scaling limit | 1 MWe | 100 kWe | 10 kWe |
| TRL | 5 | 6 | 9 |

## Prerequisites

- [Nuclear Fission Power](../energy/nuclear-fission.md) — the reactor that produces the heat
- Turbomachinery fabrication from [metals](../metals/index.md)
- Power semiconductors for conversion from [silicon](../silicon/index.md)

## See Also

- [Nuclear Electric Propulsion](./nuclear-electric.md) — the parent capability
- [Heat Radiator Design](./nuclear-electric.heat-radiator-design.md) — rejects the waste heat

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md) • [All Domains](../index.md)*
