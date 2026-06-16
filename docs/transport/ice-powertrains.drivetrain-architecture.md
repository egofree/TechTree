# Drivetrain Architecture

> **Node ID**: transport.ice-powertrains.drivetrain-architecture
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.ice-powertrains`](./ice-powertrains.md)
> **Timeline**: Years 20-35
> **Outputs**: drivetrains, differentials
> **Critical**: No

This process covers the layout and packaging of the engine, transmission, driveshafts, and driven axles into a complete vehicle. The three primary configurations are **front-wheel-drive (FWD)** — engine transverse, transaxle driving front wheels, no driveshaft, compact packaging; **rear-wheel-drive (RWD)** — engine longitudinal, driveshaft to a live-axle or independent rear differential, separates steering and acceleration loads; and **all-wheel-drive (AWD)** — torque to all four wheels through a center coupling (Haldex, Torsen, or planetary center differential) with bias and slip control.

The **differential** splits torque between the left and right driven wheels while permitting them to rotate at different speeds in corners (the outside wheel traces a longer arc). An **open differential** sends all torque to the wheel with least traction — useless on ice. **Limited-slip** variants (clutch-type Eaton, gear-type Torsen) bias torque to the gripping wheel; **locking** differentials rigidly tie both shafts together for off-road use. Dana and Eaton are the reference suppliers for production differentials.

Driveline geometry must handle articulation: **universal joints (Cardan)** allow driveshaft angle but are non-constant-velocity (vibrate at angle), so they are phased in pairs; **constant-velocity (CV) joints** (Rzeppa, tripod) are required for the large steering angles of FWD half-shafts. GKN is the dominant CV-joint supplier.

## Prerequisites

- [ICE Powertrains](./ice-powertrains.md) — parent capability, layout comparison
- [Internal Combustion Engines](../energy/internal-combustion.md) — engine torque and packaging
- [Gears & Gear Manufacturing](../machine-tools/gears.md) — ring-and-pinion, bevel gears
- [Iron & Steel](../metals/iron-steel.md) — axle shafts, carrier housings, bearings

## See Also

- [ICE Powertrains](./ice-powertrains.md) — parent capability overview
- [Manual Transmissions](./ice-powertrains.manual-transmissions.md) — torque source
- [Fuel & Exhaust Systems](./ice-powertrains.fuel-and-exhaust-systems.md) — complementary powertrain subsystem

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
