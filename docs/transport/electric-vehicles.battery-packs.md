# EV Battery Packs

> **Node ID**: transport.electric-vehicles.battery-packs
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.electric-vehicles`](electric-vehicles.md)
> **Timeline**: Years 40-55
> **Outputs**: ev_battery_packs
> **Critical**: No

The battery pack is the energy storage system of an electric vehicle — the single heaviest and most expensive component. Cell electrochemistry (cathode/anode reactions, electrolyte, intercalation) is covered in the [Chemistry](../chemistry/index.md) domain. This process addresses cell format selection, module and pack-level assembly, the battery management system, and thermal management.

## Cell Formats

**Cylindrical (18650, 21700, 4680)**: Standardized metal cans (18mm×65mm, 21mm×70mm, 46mm×80mm). High mechanical robustness, easy to mass-produce, excellent thermal dissipation per cell. Used by Tesla (thousands of cells per pack). The 4680 format with tabless electrodes reduces internal resistance and improves fast-charge capability.

**Pouch**: Flat, flexible polymer-aluminum foil envelope. Highest packaging efficiency (no rigid can), lightest weight. Requires external mechanical support (module frame). Used by LG Chem, CATL, Hyundai.

**Prismatic**: Rigid aluminum or steel rectangular can. Good mechanical protection, fewer cells per pack (simplifies BMS and assembly). Used by CATL, BYD Blade battery.

## Battery Management System (BMS)

The BMS monitors every cell's voltage (±1 mV), temperature (±1°C), and current. It enforces charge/discharge limits to prevent overvoltage (>4.2V/cell), undervoltage (<2.5V/cell), overcurrent, and overtemperature. Cell balancing redistributes charge from higher to lower cells to keep the pack in step — passive balancing bleeds excess as heat through resistors; active balancing shuttles charge between cells (more efficient, more complex). State of charge (SOC) and state of health (SOH) are estimated from voltage, coulomb counting, and impedance measurements.

## Thermal Management

Liquid cooling is standard for performance and long-range packs. Glycol-water coolant circulates through cold plates between cell rows, connecting to the vehicle's refrigerant loop for active cooling and a PTC heater for cold-weather warming. The pack is maintained at 15-35°C for optimal life and performance.

## Prerequisites

- [Electric Vehicles](electric-vehicles.md) — parent capability
- [Chemistry](../chemistry/index.md) — lithium-ion cell electrochemistry
- [Electronics](../electronics/index.md) — BMS integrated circuits

## See Also

- [Electric Vehicles](electric-vehicles.md) — parent capability
- [EV Traction Motors](electric-vehicles.ev-traction-motors.md) — pack drives the motor
- [EV Charging Systems](electric-vehicles.charging-systems.md) — charging the pack

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
