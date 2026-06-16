# Power Management and Distribution

> **Node ID**: spacecraft-systems.spacecraft-power.power-management-distribution
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.spacecraft-power`](./spacecraft-power.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: spacecraft_power
> **Critical**: No

The Power Conditioning and Distribution Unit (PCDU) regulates, protects, and distributes all electrical power on the spacecraft. It manages solar array output via shunt regulation, controls battery charge and discharge, and provides switched and fused outputs to subsystem loads. Bus architectures range from 28V unregulated (small satellites under 1 kW) to 100V fully regulated (large GEO commsats above 5 kW), trading harness mass against conversion complexity.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Bus voltage (small sats) | 28V unregulated |
| Bus voltage (large GEO) | 100V regulated |
| Shunt dissipation capacity | 50-100% of array output |
| Battery charge current range | C/10 to C/2 |
| Overcurrent protection | Latching current limiters, foldback |
| Conversion efficiency (DC-DC) | 90-96% |

## Process Overview

1. **Bus regulation design**: Select voltage (28/50/100V), regulation topology (DET vs MPPT)
2. **Shunt regulator implementation**: Sequential section shunting or PWM dissipation
3. **Battery charge controller**: Constant-current/constant-voltage profile with thermal cutoff
4. **Load switch design**: Solid-state latching switches with current limiting and telemetry
5. **Harness sizing**: Power cable gauge, routing, connector selection for bus voltage and current
6. **Qualification**: Overcurrent injection, bus transient testing, single-event-upset characterization

## Prerequisites

- Electronics capability (power semiconductor devices, DC-DC converter design)
- Solar array source characteristics and battery charge profile specifications

## See Also

- [Spacecraft Power Systems](./spacecraft-power.md) — parent capability
- [Solar Arrays](./spacecraft-power.solar-arrays.md) — power source sizing
- [Space Batteries](./spacecraft-power.space-batteries.md) — charge management target
- [Electronics](../electronics/index.md) — power conditioning heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
