# Heat Radiator Design

> **Node ID**: space-propulsion.nuclear-electric.heat-radiator-design
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.nuclear-electric`](./nuclear-electric.md)
> **Enables**: nep_systems
> **Timeline**: Years 40-200+
> **Outputs**: nep_systems
> **Critical**: No

The heat radiator is the subsystem that rejects the 70-85% of reactor thermal power that does not become electricity. Because there is no convection in vacuum, all heat must be radiated to space as thermal photons, with radiated power scaling as P = ε × σ × A × T⁴. At the radiator temperatures a spacecraft can tolerate (300-700 K), this requires tens to thousands of square metres of panel area — and the radiator is the dominant mass term in any NEP vehicle, exceeding the reactor itself at scales above ~50 kWe. This process is part of the [Nuclear Electric Propulsion](./nuclear-electric.md) capability.

## Radiator Architectures

Three concepts have been studied for NEP:

- **Pumped-loop** — NaK or water coolant through aluminum or titanium-polymer finned panels. TRL 9 (ISS radiator). Mass: 3-5 kg/m²
- **Heat-pipe** — sealed tubes with two-phase working fluid. TRL 6. Mass: 4-7 kg/m²
- **Liquid-droplet** — sprayed molten metal recaptured in flight. TRL 3. Mass: 0.5-1.5 kg/m²

## Key Parameters

| Reactor Power | Waste Heat | Radiator Area (T=350 K) | Mass |
|---------------|------------|--------------------------|------|
| 10 kWe | 30 kW | 40 m² | 150 kg |
| 100 kWe | 233 kW | 320 m² | 1-1.5 t |
| 1 MWe | 2.3 MW | 2750 m² | 8-14 t |
| 10 MWe | 23 MW | 27500 m² | 80-140 t |

## Prerequisites

- Aluminum, titanium, refractory fabrication from [metals](../metals/index.md)
- Polymer films and composites (polymers)
- Two-phase heat-pipe working fluids (chemistry)

## See Also

- [Nuclear Electric Propulsion](./nuclear-electric.md) — the parent capability
- [Reactor Power Conversion](./nuclear-electric.reactor-power-conversion.md) — what produces the waste heat

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md) • [All Domains](../index.md)*
