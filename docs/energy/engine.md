# Heat Engines

> **Node ID**: energy.engine
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.fuels`](fuels.md), `metals`, [`petroleum.refining`](../petroleum/refining.md)
> **Enables**: [`energy.electricity.power-systems`](electricity.md), [`marine.propulsion`](../marine/propulsion.md), `transport`, [`transport.aviation`](../transport/aviation.md)
> **Timeline**: Years 15-50+
> **Outputs**: mechanical_power, internal_combustion_engines, gas_turbine_power
> **Critical**: No — engines enable motorized transport and portable power but are not on the critical path to semiconductor manufacturing


Converting chemical energy stored in fuel into mechanical work is the transformation that powers industrial civilization. Before heat engines, the only practical sources of mechanical power were human and animal muscle, water wheels, and windmills, each limited by geography, weather, and modest power output. Heat engines broke this constraint by unlocking the energy density of solid, liquid, and gaseous fuels. A liter of gasoline contains roughly 34 MJ of energy, equivalent to a day of hard manual labor compressed into a few minutes of combustion.

Four engine types form a natural progression, each building on the capabilities established by its predecessors. The [Stirling engine](stirling-engine.md), an external combustion design with closed-cycle operation, serves as a bridge from steam technology. The [Otto cycle](internal-combustion.md) gasoline engine introduces internal combustion with spark ignition. The [Diesel cycle](internal-combustion.md) pushes compression higher for better efficiency. [Gas turbines](gas-turbine.md), the most demanding to manufacture, achieve the highest power density and enable jet aviation. [Steam engines](steam-engine.md), external combustion predecessors, launched the Industrial Revolution but carry inherent weight limitations.

## Focused Articles

Each engine type has a dedicated article with full detail:

- [Stirling Engine](stirling-engine.md) — Closed-cycle external combustion. Any heat source works (solar, biomass, waste heat). Achievable with lathe and basic foundry.
- [Internal Combustion Engines](internal-combustion.md) — Otto cycle (gasoline, spark ignition) and Diesel cycle (compression ignition). Precision machining at 10-25 μm tolerances. The backbone of motorized transport and stationary power.
- [Gas Turbines](gas-turbine.md) — Brayton cycle continuous-flow engines. Highest power-to-weight ratio. Combined cycle achieves 55-60%+ efficiency. Requires nickel superalloys and investment casting.
- [Steam Engine](steam-engine.md) — Reciprocating steam engines. External combustion, any boiler fuel. The first practical mechanical prime mover independent of geography.

## Selection Guide

| Engine Type | Thermal Efficiency | Power/Weight (kW/kg) | Fuel | Best Use |
|------------|-------------------|---------------------|------|----------|
| Stirling | 5-40% | 0.001-0.05 | Any heat source | Small-scale power from solar, biomass, waste heat |
| Otto (gasoline) | 25-35% | 0.5-5 | Gasoline, producer gas | Road vehicles, small aircraft, portable generators |
| Diesel | 35-45% (up to 50% marine) | 0.1-1 | Diesel, biodiesel | Trucks, ships, generators, locomotives |
| Gas turbine (simple cycle) | 20-40% | 2-10 | Kerosene, natural gas | Aviation, peaking power, mechanical drive |
| Gas turbine (combined cycle) | 55-60% | 0.5-2 | Natural gas | Baseload power generation |

**Selection guidance**: For a bootstrap economy, the choice of engine type is driven primarily by what fuel and manufacturing capability are available, not by theoretical efficiency. If only biomass and basic foundry work are available, the Stirling engine is the only option. If petroleum distillation exists and machine tools can grind to 10 μm tolerance, the Otto cycle gasoline engine becomes feasible. If the additional precision for fuel injection nozzles can be achieved, the diesel engine is preferred for all stationary and heavy transport applications due to higher efficiency and longer life. Gas turbines should be pursued only after substantial experience with piston engines.

## Key Deliverables

- **Tier 1** (Years 15-25): Stirling engines for small-scale power generation from any heat source. Achievable with lathe and basic foundry work. Power output in the tens of watts to a few kilowatts.
- **Tier 2** (Years 20-30): Gasoline (Otto cycle) engines for road vehicles, small aircraft, and portable generators. 25-35% thermal efficiency, 0.5-5 kW/kg. Requires full machine tool chain and petroleum distillation.
- **Tier 3** (Years 25-40): Diesel engines for trucks, ships, industrial generators, and locomotives. 35-45% thermal efficiency. Requires precision fuel injection (0.1-0.3 mm nozzle orifices at 1000-2000 bar).
- **Tier 4** (Years 35-50+): Gas turbines for aviation and combined-cycle power generation at 55-60%+ efficiency. Requires nickel superalloys, investment casting, single-crystal blade technology.

## Efficiency Comparison

| Engine Type | Compression Ratio | Peak Pressure (bar) | Thermal Efficiency | Exhaust Temp (°C) |
|------------|-------------------|---------------------|-------------------|-------------------|
| Stirling | N/A (external) | 50-200 (working gas) | 5-40% | 100-300 |
| Otto (gasoline) | 8:1 to 12:1 | 50-80 | 25-35% | 600-900 |
| Diesel | 14:1 to 24:1 | 80-200 | 35-45% | 400-700 |
| Marine diesel | 14:1 to 24:1 | 80-150 | 45-50% | 250-400 |
| Gas turbine (simple) | 10:1 to 30:1 (pressure) | N/A (continuous flow) | 25-40% | 450-600 |
| Gas turbine (combined) | 10:1 to 30:1 (pressure) | N/A (continuous flow) | 55-60% | 80-120 |

## General Safety & Hazards

- **Exhaust carbon monoxide (CO)**: Colorless, odorless, lethal gas. Gasoline engines produce 1-10% CO in exhaust. Diesel engines produce 0.05-0.5% CO. Always operate in well-ventilated areas or route exhaust outside.
- **Noise**: Unmuffled engines produce 100-120 dB. Hearing protection required for extended operation.
- **Rotating machinery guards**: Install guards over all rotating components. Maintenance only with engine stopped.
- **Hot surfaces**: Exhaust manifolds reach 300-600°C. Allow 30+ minutes cooling before touching.
- **Fuel fires**: Gasoline ignites easily (flash point -43°C). Diesel is safer but atomized spray ignites readily. Fire extinguisher required near all operating engines.
- **Battery hazards**: Lead-acid batteries produce hydrogen gas during charging. Connect and disconnect with loads off.

## Engine Glossary

- **Bore**: Cylinder internal diameter. Typical range 60-120 mm for automotive engines, up to 960 mm for marine diesels.
- **Stroke**: Distance the piston travels from TDC to BDC.
- **Displacement**: Total swept volume of all cylinders. Calculated as π/4 × bore² × stroke × number of cylinders.
- **Compression ratio**: Ratio of cylinder volume at BDC to volume at TDC. Higher ratios yield higher efficiency but require stronger construction and (for gasoline) higher octane fuel.
- **TDC/BDC**: Top dead center (piston at highest position) / Bottom dead center (piston at lowest position).
- **BSFC**: Brake specific fuel consumption. Fuel consumed per unit of mechanical energy produced. Typical values: gasoline 250-350 g/kWh, diesel 190-240 g/kWh.
- **Volumetric efficiency**: Ratio of actual air mass drawn into the cylinder to the theoretical maximum. Naturally aspirated engines achieve 75-95%. Turbocharged engines exceed 100%.
- **Mean effective pressure (MEP)**: Theoretical constant pressure that would produce the same work as the actual pressure cycle. Typical: gasoline 8-12 bar, turbocharged diesel 15-25 bar.
- **Detonation (knock)**: Abnormal combustion where unburned mixture auto-ignites explosively. Causes rapid engine damage.
- **Supercharging**: Compressing intake air above atmospheric pressure. Mechanically driven (supercharger) or exhaust-driven (turbocharger).
- **Intercooler**: Heat exchanger cooling compressed air from turbocharger before it enters the engine.

## See Also

- [Stirling Engine](stirling-engine.md) — closed-cycle external combustion
- [Internal Combustion Engines](internal-combustion.md) — Otto and Diesel cycle engines
- [Gas Turbines](gas-turbine.md) — Brayton cycle engines
- [Steam Engine](steam-engine.md) — reciprocating steam engines
- [Fuels](fuels.md) — Liquid fuel properties and alternatives
- [Steam Power](steam-power.md) — External combustion predecessor
- [Electricity Generation](electricity.md) — Generators driven by engines
- [Railways](../transport/railways.md) — Diesel locomotive applications
- [Aviation](../transport/aviation.md) — Aircraft engine requirements
- [Lubricants](../chemistry/lubricants.md) — Engine oil and lubrication
- [Machining](../machine-tools/machining.md) — Precision machining for engine components

---

*Part of the [Bootciv Tech Tree](../index.md) · [Energy](./index.md) · [All Domains](../index.md)*
