# Combustion Chamber

> **Node ID**: launch-vehicles.liquid-propulsion.combustion-chamber
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.liquid-propulsion`](./liquid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: liquid_engines
> **Critical**: No

The combustion chamber contains the propellant reaction at 5-25 MPa and 3000-3500°C. No structural metal survives these conditions unprotected — the chamber wall is actively cooled by routing propellant through channels machined in the wall before it reaches the injector. See [Liquid Propulsion](./liquid-propulsion.md) for the integrated engine context.

## Regenerative Cooling

The chamber inner wall is constructed with internal channels (1-3 mm wide, 2-5 mm deep). Fuel flows from the nozzle end toward the injector, absorbing heat flux of 10-160 MW/m² (peak at the throat where gas velocity is sonic and boundary layer is thinnest). The fuel gains 200-400°C across the channels, improving subsequent combustion efficiency.

## Key Parameters

- **Chamber pressure**: 5-25 MPa (gas-generator cycle: 7-15; staged combustion: 20-30)
- **Combustion temperature**: 3000-3500°C (propellant-dependent)
- **Wall heat flux**: 10-160 MW/m² (throat peak)
- **Inner wall material**: Narloy-Z (Cu-Ag-Zr alloy) for maximum thermal conductivity
- **Inner wall thickness**: 0.5-2.0 mm at throat
- **Outer jacket**: Inconel 718 or steel (structural reinforcement)
- **Characteristic length (L\*)**: 0.8-1.5 m (chamber volume / throat area)

## Film Cooling

A thin film of propellant is injected along the inner wall surface, reducing gas-side wall temperature by 200-500°C at a small Isp penalty. Extends chamber life from seconds (uncooled) to minutes (regen + film).

## See Also

- [Liquid Propulsion](./liquid-propulsion.md) — parent capability
- [Nozzle Design](./liquid-propulsion.nozzle-design.md) — downstream extension of chamber
- [Injector Design](./liquid-propulsion.injector-design.md) — upstream component

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md)*
