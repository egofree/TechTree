# Turbopump Design

> **Node ID**: launch-vehicles.liquid-propulsion.turbopump-design
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.liquid-propulsion`](./liquid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: turbopumps
> **Critical**: No

The turbopump pressurizes liquid propellant from tank pressure (0.2-0.5 MPa) to injector inlet pressure (15-40 MPa) — a 50-200× pressure ratio at flow rates of tens to hundreds of kilograms per second. It is the most highly stressed rotating machine in any industrial system. See [Liquid Propulsion](./liquid-propulsion.md) for the integrated engine context.

## Architecture

A turbopump consists of three sections on a common shaft: the **inducer** (an axial-flow stage that raises inlet pressure to prevent cavitation at the impeller eye), the **centrifugal impeller** (which delivers the bulk pressure rise), and the **turbine** (driven by hot gas from the engine cycle's gas generator or preburner).

## Key Parameters

- **Speed**: 30,000-100,000 RPM depending on engine thrust class
- **Impeller tip speed**: 300-600 m/s (centrifugal stress 500-1500 MPa at hub)
- **Pressure ratio**: 50-200× (tank inlet to chamber injector)
- **Flow rate**: 5-500 kg/s per propellant (engine-dependent)
- **Bearing type**: Ball bearings, LOX/fuel-lubricated (no oil), Si3N4 ceramic balls on 440C races
- **Shaft runout**: <5 μm total indicated reading

## Materials

- **LOX impeller**: Ti-6Al-4V (950 MPa yield, oxygen-compatible, cryogenic tough)
- **Fuel impeller**: Inconel 718 (1030 MPa yield, 650°C capability)
- **Turbine blades**: CMSX-4 single-crystal nickel superalloy (1100°C)
- **Shaft**: Maraging 300 / Aermet 100 (1900-2400 MPa tensile)

## See Also

- [Liquid Propulsion](./liquid-propulsion.md) — parent capability
- [Combustion Chamber](./liquid-propulsion.combustion-chamber.md) — downstream consumer
- [Gas Turbines](../energy/gas-turbine.md) — turbomachinery heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md)*
