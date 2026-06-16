# Radiation Shielding

> **Node ID**: space-propulsion.nuclear-thermal.radiation-shielding-engine
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.nuclear-thermal`](./nuclear-thermal.md)
> **Enables**: ntp_engines
> **Timeline**: Years 40-200+
> **Outputs**: ntp_engines
> **Critical**: No

The NTP shadow shield is a directional radiation barrier placed between the reactor and the crew compartment. Unlike ground reactors that surround the core with full biological shielding (see [Nuclear Fission Power](../energy/nuclear-fission.md)), an NTP vehicle shields only a cone behind the reactor, letting radiation radiate freely into space in every other direction. This minimises shield mass, which is critical because every kilogram of shield mass displaces payload. This process is part of the [Nuclear Thermal Propulsion](./nuclear-thermal.md) capability.

## Shield Materials

A typical shadow shield is a sandwich of layers:

- **Lithium hydride (LiH)** — 0.5-1.5 m thick; moderates and captures fast neutrons (Li-6 captures thermal neutrons via Li-6(n,α)H-3)
- **Tungsten or depleted uranium** — 5-10 cm thick; attenuates gamma rays by photoelectric absorption
- **Optional polyethylene or water** — additional neutron moderation at lower temperature than LiH

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Shield mass | 1-3 tonnes |
| Crew dose target | <5 rem/year |
| Reactor-shield separation | 10-50 m |
| Unshielded dose at 10 m | 10^4 rem/h (lethal in minutes) |
| Shielded dose at 10 m, 2 t | 0.5 mrem/h (~4 rem/year) |

## Prerequisites

- Tungsten and depleted-uranium fabrication from [metals](../metals/index.md)
- LiH synthesis and pressing (chemistry)
- Radiation transport analysis (computing)

## See Also

- [Nuclear Thermal Propulsion](./nuclear-thermal.md) — the parent capability
- [Reactor Core Design](./nuclear-thermal.reactor-core-design.md) — the reactor the shield protects against

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md) • [All Domains](../index.md)*
