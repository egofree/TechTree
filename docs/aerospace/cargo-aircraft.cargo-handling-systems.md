# Cargo Handling Systems

> **Node ID**: aerospace.cargo-aircraft.cargo-handling-systems
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.cargo-aircraft`](cargo-aircraft.md)
> **Timeline**: Years 30-50+
> **Outputs**: cargo_loading_systems
> **Critical**: No

The interior cargo handling system is what turns a reinforced tube into a working freighter. Without rollers, guides, drive units, and locking fittings, every pallet would have to be manhandled into position — a process that takes hours and injures workers. A modern freighter's handling system moves a 5-tonne pallet from the door to its locked position in under 60 seconds, using powered rollers and ball-transfer units set into the floor at 254 mm intervals.

## System Components

**Roller conveyors:**
- Cylindrical aluminum or steel rollers (50 mm diameter) set flush with the floor surface, spaced 125-254 mm apart. Each roller rotates on sealed ball bearings. Pallets slide across the rollers with minimal friction (coefficient ~0.02 vs. 0.4 for a pallet dragging on bare metal).
- Roller tracks run the full length of the main deck, aligned with each pallet position. Cross-transfer rollers at the door allow pallets to move laterally into their lane.

**Power drive units (PDUs):**
- Electrically driven rollers or belt drives embedded in the floor that propel pallets forward. Each PDU is rated at 0.5-1.5 kW and drives a 1-2 metre section of roller track. The loadmaster controls PDUs from panels at each door station, moving pallets forward or aft in sequence.
- PDU power: 28V DC or 270V DC, drawing from the aircraft's electrical bus. A 747F main deck has 30-40 PDUs; a 777F has 27.

**Ball transfer units:**
- Omni-directional load-bearing spheres set into the floor at door thresholds and turning zones. Allow pallets to rotate and translate in any direction during positioning. Each unit carries 500-1,000 kg.

## Prerequisites

- [Cargo Aircraft](cargo-aircraft.md) — reinforced floor structure and door geometry
- [Machine Tools](../machine-tools/index.md) — precision rollers, bearings, actuator machining
- [Electronics](../electronics/index.md) — PDU control systems and loadmaster panels

## See Also

- [Cargo Aircraft](cargo-aircraft.md) — parent capability overview
- [Machine Tools](../machine-tools/index.md) — roller and bearing manufacturing

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
