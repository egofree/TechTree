# Nozzle Integration

> **Node ID**: space-propulsion.nuclear-thermal.nozzle-integration
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.nuclear-thermal`](./nuclear-thermal.md)
> **Enables**: ntp_engines
> **Timeline**: Years 40-200+
> **Outputs**: ntp_engines
> **Critical**: No

The NTP nozzle is a convergent-divergent nozzle that expands hot hydrogen from the reactor core to produce thrust at 850-1000 s specific impulse. Because the engine operates in vacuum and uses the lowest-molecular-weight propellant available, NTP nozzles use very high expansion ratios (80:1 to 300:1) to maximise exhaust velocity. This process is part of the [Nuclear Thermal Propulsion](./nuclear-thermal.md) capability.

## Nozzle Architectures

Two designs have been ground-tested:

- **Refractory nozzle** (NERVA): graphite or carbon-carbon with Nb/Ta/W liners, radiatively cooled. Heavy but simple; survives 2700 K hydrogen for tens of minutes.
- **Regen-cooled nozzle** (modern designs): LH2 is pumped through channel walls before entering the reactor. Cools the nozzle metal to 300 K while pre-heating propellant; identical in principle to chemical-engine regen nozzles.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Chamber temperature | 2500-3000 K |
| Expansion ratio | 80:1 to 300:1 |
| Exit Mach number | 5-7 |
| Specific impulse | 850-1000 s |
| Wall material | C-C, Nb-C103, SiC composite, GlidCop |

## Prerequisites

- Refractory-metal and carbon-carbon fabrication from [metals](../metals/index.md)
- Regen-cooled nozzle design heritage from [Liquid Propulsion](../launch-vehicles/liquid-propulsion.md)
- [Ceramics](../metals/index.md) for SiC composite nozzles

## See Also

- [Nuclear Thermal Propulsion](./nuclear-thermal.md) — the parent capability
- [Reactor Core Design](./nuclear-thermal.reactor-core-design.md) — what feeds hot hydrogen to the nozzle

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md) • [All Domains](../index.md)*
