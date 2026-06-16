# Propellant Transfer

> **Node ID**: space-propulsion.propellant-storage.propellant-transfer
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.propellant-storage`](./propellant-storage.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: None
> **Critical**: No

Propellant transfer is the process of moving cryogenic liquid between two docked vehicles in orbit. It requires coupling a sealed fluid line, settling the liquid over the drain port in microgravity, and chilling down the transfer line to prevent two-phase flashing. See [Cryogenic Propellant Storage & Transfer](./propellant-storage.md) for the integrated depot context.

## Overview

Transfer is the most operationally complex phase of depot operations. Unlike storage (a steady-state thermal problem), transfer involves transients: line chill-down, flow start/stop, and ullage pressure management. The three sub-problems — coupling, settling, and chill-down — are solved by different mechanisms and have different failure modes.

## Key Parameters

| Parameter | Typical Value | Notes |
|-----------|--------------|-------|
| Transfer flow rate | 1-100 kg/s | Depends on line diameter and pump pressure |
| Line diameter | 5-25 cm | Larger = faster transfer, harder to seal |
| Settling acceleration | 0.001-0.01 g | Via thrusters or centrifuge |
| Chill-down loss | 5-15% of transfer mass | First propellant flashes to cool the line |
| Coupling seal leak rate | <1×10⁻⁶ scc/s helium | Metal C-ring or PTFE seal |

## Prerequisites

- Rendezvous and docking capability (probe/drogue or QD coupler)
- Settling thruster system or capillary propellant management device
- Transfer line with chill-down venting capability
- Cryogenic-rated valves and quick-disconnect coupler

## See Also

- [Cryogenic Propellant Storage & Transfer](./propellant-storage.md) — parent capability
- [Zero Boil-Off Systems](./propellant-storage.zero-boiloff-systems.md) — post-transfer storage
- [Vehicle Architecture](../launch-vehicles/vehicle-architecture.md) — docking interface heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
