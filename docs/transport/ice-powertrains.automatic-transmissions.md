# Automatic Transmissions

> **Node ID**: transport.ice-powertrains.automatic-transmissions
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.ice-powertrains`](./ice-powertrains.md)
> **Timeline**: Years 25-40+
> **Outputs**: transmissions
> **Critical**: No

The automatic transmission shifts ratios without driver action using one or more **epicyclic (planetary) gearsets**. A planetary set has three elements — sun gear, planet carrier, ring gear — and holding any one stationary produces a different ratio between the other two. All gears stay in constant mesh; ratios are selected by hydraulically applying **multidisc clutches** (to lock elements together) and **brake bands** (to hold elements to the case). A hydraulic **valve body** (or electronic control unit) sequences these elements based on governor pressure, throttle position, and vehicle speed.

The **torque converter** — a three-element fluid coupling (impeller, turbine, stator) between engine and gearbox — multiplies engine torque **2.0-2.5×** at stall and lets the vehicle idle in gear. A **lock-up clutch** mechanically bridges the converter above 30-50 km/h, recovering 3-5% fuel economy. The reference modern units are the **ZF 8HP** (8-speed, ~7.0:1 spread, BMW/Audi/Chrysler) and **Aisin AWF8** (Toyota, Volvo), which achieve 88-93% efficiency.

Historical efficiency penalty versus manuals (5-12%) has largely closed with lock-up converters, more ratios, and electronic control. The trade-offs are complexity, cost, and parasitic hydraulic-pump load.

## Prerequisites

- [ICE Powertrains](./ice-powertrains.md) — parent capability, torque multiplication math
- [Manual Transmissions](./ice-powertrains.manual-transmissions.md) — predecessor, gear fundamentals
- [Gears & Gear Manufacturing](../machine-tools/gears.md) — precision planetary gearsets
- [Iron & Steel](../metals/iron-steel.md) — friction plates, hydraulic valve body, pump gears

## See Also

- [ICE Powertrains](./ice-powertrains.md) — parent capability overview
- [Manual Transmissions](./ice-powertrains.manual-transmissions.md) — simpler, more efficient alternative
- [Drivetrain Architecture](./ice-powertrains.drivetrain-architecture.md) — downstream driveline

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
