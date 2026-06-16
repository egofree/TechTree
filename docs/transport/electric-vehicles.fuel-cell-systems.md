# Fuel Cell Systems

> **Node ID**: transport.electric-vehicles.fuel-cell-systems
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.electric-vehicles`](electric-vehicles.md)
> **Timeline**: Years 45-60+
> **Outputs**: ev_powertrains
> **Critical**: No

The fuel cell vehicle (FCEV) uses a proton exchange membrane (PEM) fuel cell stack to generate electricity on-board from compressed hydrogen and atmospheric oxygen. The electricity drives a conventional electric traction motor. A small buffer battery (1.5-5 kWh) handles peak loads and regenerative braking. Hydrogen production and distribution infrastructure is covered in the [Energy](../energy/index.md) domain and is the primary deployment bottleneck.

## PEM Fuel Cell Stack

The stack consists of 300-400 individual cells in series. Each cell has a membrane electrode assembly (MEA): a proton-conducting polymer membrane (Nafion) sandwiched between a platinum-catalyzed anode and cathode. Hydrogen oxidizes at the anode (H₂ → 2H⁺ + 2e⁻); oxygen reduces at the cathode (½O₂ + 2H⁺ + 2e⁻ → H₂O). The electrons flow through the external circuit (the motor), the protons through the membrane. Product water exits the cathode side. Per-cell voltage: 0.6-0.8V at load. Stack output: 300-400V DC.

## Hydrogen Storage

Compressed hydrogen gas stored in Type IV composite tanks (carbon fiber overwrap on HDPE liner) at 350 bar (commercial vehicles) or 700 bar (passenger cars). Two or three tanks are packaged in the vehicle chassis. A tank system stores 5-6 kg of hydrogen for 500-650 km range. Refueling takes 3-5 minutes at a high-pressure hydrogen station.

## Balance of Plant

- **Air compressor**: Pressurizes atmospheric air to 1.5-2.5 bar for the cathode. The single largest parasitic load (5-15% of stack output).
- **Humidifier**: The PEM membrane requires humidification to conduct protons. Exhaust cathode air humidifies incoming air via a membrane exchanger.
- **Cooling system**: The stack operates at 60-80°C. A dedicated deionized coolant loop removes waste heat (40-50% of the hydrogen energy becomes heat). The radiator is significantly larger than an ICE vehicle's.
- **Hydrogen recirculation**: Unconsumed anode hydrogen is pumped back to the stack inlet. A water separator removes product water from the anode loop.

## Prerequisites

- [Electric Vehicles](electric-vehicles.md) — parent capability
- [Chemistry](../chemistry/index.md) — electrochemistry, hydrogen production
- [Energy](../energy/index.md) — hydrogen infrastructure

## See Also

- [Electric Vehicles](electric-vehicles.md) — parent capability
- [EV Traction Motors](electric-vehicles.ev-traction-motors.md) — shared motor/inverter hardware
- [Battery Packs](electric-vehicles.battery-packs.md) — buffer battery

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
