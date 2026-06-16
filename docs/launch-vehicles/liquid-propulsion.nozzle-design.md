# Nozzle Design

> **Node ID**: launch-vehicles.liquid-propulsion.nozzle-design
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.liquid-propulsion`](./liquid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: regen_nozzles
> **Critical**: No

The nozzle converts high-pressure combustion gas into high-velocity exhaust, producing thrust. Efficiency depends on the **area ratio** (exit area / throat area): higher ratios extract more energy in vacuum. See [Liquid Propulsion](./liquid-propulsion.md) for the integrated engine context.

## Bell Nozzle and Rao Optimum Contour

Modern rocket nozzles use a bell-shaped contour rather than a simple cone. The **Rao optimum contour** (G.V.R. Rao, NASA 1958) minimizes divergence losses by computing the wall shape that turns the flow from throat to exit angle with maximum thrust. A bell nozzle is 20-30% shorter than a conical nozzle of the same area ratio. The contour is a parabolic arc from the throat radius (initial angle 20-40°) to the exit radius (exit angle 5-15°).

## Area Ratio Optimization

- **Sea-level nozzle**: 10:1 area ratio (exhaust exits near atmospheric pressure, avoids flow separation)
- **Vacuum nozzle**: 40:1 to 150:1 area ratio (gas expands to near-vacuum pressure)
- **Flow separation**: If chamber pressure drops below ~0.4× ambient at the exit, the flow separates from the wall, producing asymmetric side forces that can destroy the nozzle

## Key Parameters

- **Area ratio (sea-level)**: 10:1 to 25:1
- **Area ratio (vacuum)**: 40:1 to 150:1
- **Bell length**: 70-85% of equivalent 15° cone
- **Throat diameter**: 100-500 mm (engine-dependent)
- **Nozzle material**: Regeneratively cooled copper-alloy (Narloy-Z) or radiatively cooled niobium C-103 (extension)

## Aerospike

An aerospike inverts the bell — the ramp is internal, with exhaust flowing outward. The atmosphere provides the outer wall, so effective area ratio adapts to ambient pressure. Promises 10-15% Isp improvement for SSTO but has never flown operationally.

## See Also

- [Liquid Propulsion](./liquid-propulsion.md) — parent capability
- [Combustion Chamber](./liquid-propulsion.combustion-chamber.md) — upstream of nozzle

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md)*
