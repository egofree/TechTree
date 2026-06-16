# Manual Transmissions

> **Node ID**: transport.ice-powertrains.manual-transmissions
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.ice-powertrains`](./ice-powertrains.md)
> **Timeline**: Years 20-30
> **Outputs**: transmissions
> **Critical**: No

The driver-shifted manual transmission is the simplest efficient multispeed gearbox. A **countershaft (layshaft)** carries a cluster of gears in constant mesh with the mainshaft gears; the driver selects a ratio by sliding a dog clutch to lock the desired gear to the output shaft. Ratios are changed by a floor-mounted shift lever acting through selector forks.

Three generations of engagement: **sliding-mesh** (1890s, gears slide into mesh — double-clutch required, brutal on teeth), **constant-mesh** (1920s, gears always engaged; dog clutches slide — still needs double-clutching), and **synchromesh** (1928 Cadillac, cone friction clutch matches gear speeds before dog engagement — modern manual shifting without double-clutching).

A typical 5-speed uses ratios 3.5 / 2.1 / 1.4 / 1.0 / 0.85 with a 3.7 : 1 final drive. Mechanical efficiency is **94-98%** in direct (1:1) gear — the most efficient transmission type. The trade-off is driver workload in traffic and no creep at idle without clutch slip.

## Prerequisites

- [ICE Powertrains](./ice-powertrains.md) — parent capability, gear ratio math
- [Gears & Gear Manufacturing](../machine-tools/gears.md) — hobbed, shaved, carburized gear teeth (8620/9310 steel, 58-62 HRC case)
- [Internal Combustion Engines](../energy/internal-combustion.md) — provides flywheel input torque
- [Iron & Steel](../metals/iron-steel.md) — case-hardening-grade steel, cast iron/aluminum housing

## See Also

- [ICE Powertrains](./ice-powertrains.md) — parent capability overview
- [Automatic Transmissions](./ice-powertrains.automatic-transmissions.md) — self-shifting alternative
- [Drivetrain Architecture](./ice-powertrains.drivetrain-architecture.md) — where the torque goes next

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
