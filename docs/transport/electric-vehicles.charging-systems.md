# EV Charging Systems

> **Node ID**: transport.electric-vehicles.charging-systems
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.electric-vehicles`](electric-vehicles.md)
> **Timeline**: Years 42-58
> **Outputs**: ev_charging_systems
> **Critical**: No

Charging systems deliver electrical energy from the grid to the vehicle battery. AC charging uses the vehicle's onboard charger to convert AC to DC; DC fast charging bypasses the onboard charger and feeds DC directly to the battery at high power. Grid-side power electronics and electrical distribution are covered in the [Electricity](../energy/electricity.md) domain.

## Charging Levels

**Level 1 (120V AC, 1.4-1.9 kW)**: Standard household outlet. 8-16 km of range per hour. Suitable only for PHEVs or overnight top-ups. No special installation.

**Level 2 (240V AC, 7.2-19.2 kW)**: Dedicated 32-80A circuit. 30-60 km of range per hour. The dominant residential and workplace standard. Requires a wall-mounted EVSE (Electric Vehicle Supply Equipment).

**DC Fast Charging (50-350 kW)**: Station-side DC directly to battery. 80% charge in 15-40 minutes. Peak power delivered only in the 10-60% SOC band — the charging curve tapers above this to protect cells. Requires 400V or 800V battery architecture.

## Connector Standards

- **NACS (SAE J3400)**: Tesla-originated, now the North American standard. Compact, bidirectional. Adopted by Ford, GM, Rivian, and most manufacturers.
- **CCS (Combined Charging System)**: European and legacy North American standard. AC and DC pins in one connector.
- **CHAdeMO**: Japanese DC-only standard. Being phased out globally.
- **GB/T**: Chinese standard (AC and DC variants).

## Charging Curve and Thermal Management

The battery accepts maximum power only at intermediate state of charge. Below 10%, current is limited to protect cold/deep cells. Above 60-80%, constant-voltage tapering slows the charge dramatically. Hot batteries are derated above 40°C; the thermal management system may pre-cool the pack when navigation is set to a fast charger.

## Bidirectional Charging (V2G/V2L)

**V2G (Vehicle-to-Grid)**: The vehicle exports power back to the grid during peak demand. Requires a bidirectional inverter in the EVSE and utility coordination. Turns the fleet into distributed grid storage. **V2L (Vehicle-to-Load)**: 1.5-3.6 kW AC output to power tools or appliances — simpler, available on many EVs.

## Prerequisites

- [Electric Vehicles](electric-vehicles.md) — parent capability
- [Electricity](../energy/electricity.md) — grid power supply
- [Battery Packs](electric-vehicles.battery-packs.md) — the charging target

## See Also

- [Electric Vehicles](electric-vehicles.md) — parent capability
- [Battery Packs](electric-vehicles.battery-packs.md) — what gets charged
- [EV Traction Motors](electric-vehicles.ev-traction-motors.md) — what the pack powers

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
