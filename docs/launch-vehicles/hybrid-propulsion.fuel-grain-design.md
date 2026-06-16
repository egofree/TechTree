# Fuel Grain Design

> **Node ID**: launch-vehicles.hybrid-propulsion.fuel-grain-design
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.hybrid-propulsion`](./hybrid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: hybrid_fuel_grains
> **Critical**: No

Fuel grain design is the formulation and geometry engineering of the solid fuel grain for hybrid rocket engines. The fuel's regression rate, port shape, and mechanical properties set the engine's thrust, mixture ratio, and burn duration. This process is part of the [Hybrid Propulsion](./hybrid-propulsion.md) capability.

## Fuel Options

| Fuel | Regression (mm/s) | Vac Isp (s) | Notes |
|------|-------------------|--------------|-------|
| HTPB rubber | 0.5-1.0 | 250-310 | Heritage; SpaceShipOne/Two. Mechanically robust. |
| Paraffin wax | 2.0-5.0 | 300-350 | High regression via melt-layer entrainment. Brittle when cold. |
| Cross-linked SHPB | 0.8-1.5 | 300-320 | Higher strength for high-thrust applications. |
| Polyethylene (HDPE) | 0.3-0.6 | 280-300 | Cheap; low regression. Lab-scale. |

## Regression Rate Law

Hybrid fuel regression is governed by oxidizer mass flux, not chamber pressure:

**r = a · G_ox^n**

where `G_ox` is oxidizer mass flux (kg/m²·s) and `n` is typically **0.5-0.8**. Typical rates are **0.5-2.0 mm/s** for HTPB at moderate flux. Paraffin's 3-5× higher rate comes from melt-layer droplet entrainment — a convective fuel-transfer path that bypasses the slow pyrolysis limit.

## Port Geometry

As the fuel regresses, the port diameter grows and `G_ox` falls (flux = flow/area), shifting the O/F ratio oxidizer-rich. Mitigations:
- **Single-port**: simple, but requires high-regression fuel (paraffin) for adequate flow at large diameters.
- **Multi-port (wagon-wheel, star)**: 4-12 narrow ports keep `G_ox` high. Thin webs between ports risk cracking; residual sliver 2-10% of fuel mass.

## Fabrication

HTPB: blend with isocyanate cure agent (+ optional metal powder), cast onto/in a mandrel, cure at 50-60°C for 3-5 days. Paraffin: melt at 70-90°C, pour into a structural shell (composite or metal), solidify on cooling. X-ray for voids; bore-gauge the port.

See [Oxidizer Feed Systems](./hybrid-propulsion.oxidizer-feed-systems.md) for the oxidizer side and [Hybrid Propulsion](./hybrid-propulsion.md) for the full capability.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
