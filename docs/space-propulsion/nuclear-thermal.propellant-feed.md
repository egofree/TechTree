# Propellant Feed System

> **Node ID**: space-propulsion.nuclear-thermal.propellant-feed
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.nuclear-thermal`](./nuclear-thermal.md)
> **Enables**: ntp_engines
> **Timeline**: Years 40-200+
> **Outputs**: ntp_engines
> **Critical**: No

The NTP propellant feed system stores liquid hydrogen (LH2) at 20 K, pressurises it through a turbopump, routes it through the reactor core cooling channels, and delivers superheated hydrogen to the nozzle inlet. This process is part of the [Nuclear Thermal Propulsion](./nuclear-thermal.md) capability.

## Expander Cycle

NTP uses a self-driving **expander cycle** with no preburner or gas generator:

1. LH2 at 20 K is drawn from the tank at 0.3 MPa by the turbopump inducer
2. The pump raises the hydrogen to 5-7 MPa
3. High-pressure LH2 flows through the nozzle cooling jacket and reactor support structure, vaporising to 280-300 K
4. The vaporised hydrogen drives the turbopump turbine
5. Turbine exhaust is routed into the top of the reactor core, where it is superheated to 2700 K
6. Hot hydrogen exits the core and expands through the nozzle

## Key Parameters

| Parameter | Value |
|-----------|-------|
| LH2 tank temperature | 20 K |
| Pump inlet pressure | 0.3 MPa |
| Pump outlet pressure | 5-7 MPa |
| Mass flow rate | 10-40 kg/s |
| Turbine inlet temperature | 280-300 K |
| Boil-off rate (zero-boiloff target) | <0.1%/day |

## Prerequisites

- [Cryogenic Liquefaction & Storage](../cryogenics/liquefaction-storage.md) — LH2 tankage and transfer
- Turbopump design heritage from [Liquid Propulsion](../launch-vehicles/liquid-propulsion.md)
- Hydrogen-embrittlement-resistant refractory metals from [metals](../metals/index.md)

## See Also

- [Nuclear Thermal Propulsion](./nuclear-thermal.md) — the parent capability
- [Reactor Core Design](./nuclear-thermal.reactor-core-design.md) — what the LH2 feeds into

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md) • [All Domains](../index.md)*
