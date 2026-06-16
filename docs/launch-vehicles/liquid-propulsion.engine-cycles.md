# Engine Cycles

> **Node ID**: launch-vehicles.liquid-propulsion.engine-cycles
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.liquid-propulsion`](./liquid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: liquid_engines
> **Critical**: No

The power cycle determines how the turbopumps are driven, which sets the maximum chamber pressure, engine Isp, and overall complexity. The trade space spans from dead-simple pressure-fed systems to the most complex full-flow staged combustion engines. See [Liquid Propulsion](./liquid-propulsion.md) for the integrated engine context.

## Cycle Comparison

- **Pressure-fed**: No turbopump. Tanks pressurized to 0.3-3 MPa with helium or nitrogen, feeding the chamber directly. Limited to small engines because tank mass scales with pressure and volume. Simplest, most reliable.
- **Gas-generator**: 3-5% of propellant burned in a separate gas generator (fuel-rich, <750°C) to drive the turbine, then dumped overboard. Chamber pressure capped at 10-15 MPa. Used by Merlin 1D, F-1, Vulcain. Simplest turbopump cycle.
- **Expander**: No preburner. Fuel picks up heat in regenerative cooling channels, expands through turbine, enters chamber. Limited by wall heat transfer (caps thrust at ~100-200 kN for LOX/LH2). Used by RL10, Vinci.
- **Staged combustion (FRSC)**: All fuel (+ part of oxidizer) flows through preburner and turbine before entering chamber. Chamber pressure 20-26 MPa. Used by RS-25 (fuel-rich).
- **Staged combustion (ORSC)**: All oxidizer flows through preburner and turbine. Demands oxygen-compatible turbine metallurgy. Chamber pressure 25-30 MPa. Used by RD-180 (developed by USSR, unmatched in West until 2000s).
- **Full-flow staged**: Two preburners (fuel-rich + oxidizer-rich), two independent turbopump shafts. Every propellant molecule passes through a turbine. Highest chamber pressure (30-40+ MPa). Used by Raptor.

## Key Parameters

| Cycle | Chamber Pressure | Relative Isp | Complexity |
|-------|-----------------|-------------|-----------|
| Pressure-fed | 0.5-3 MPa | Baseline | Very low |
| Gas-generator | 7-15 MPa | +15-30s | Moderate |
| Expander | 4-10 MPa | +25-40s | Moderate |
| Staged combustion | 20-30 MPa | +40-70s | High |
| Full-flow staged | 30-40+ MPa | +50-90s | Very high |

## See Also

- [Liquid Propulsion](./liquid-propulsion.md) — parent capability
- [Turbopump Design](./liquid-propulsion.turbopump-design.md) — the driven component
- [Gas Turbines](../energy/gas-turbine.md) — turbomachinery heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md)*
