# Road-Switcher Design

> **Node ID**: transport.diesel-locomotives.road-switcher-design
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.diesel-locomotives`](./diesel-locomotives.md)
> **Timeline**: Years 20-50+
> **Outputs**: diesel_locomotives
> **Critical**: No

The road-switcher is the defining locomotive layout of the diesel era: a single hood covering the engine and generator, a cab at one or both ends, and a full-length walkway along the outside. The design combines the visibility of a switcher (for yard work) with the power and speed of a road locomotive (for mainline service).

## Layout Rationale

Early diesel switchers (1930s-1940s) were built as boxcabs — a fully enclosed body with the cab at one end. This worked for yard service but offered poor rearward visibility and made mainline operation difficult. The road-switcher (EMD GP7, 1949) solved this with:
- **Hood body**: Engine and generator under a low hood (1.5-2.0 m high), with a walkway on each side at platform level. The engineer can walk the full length of the locomotive to inspect equipment or reach the trailing unit.
- **Cab placement**: At one end (for a single-cab A-unit) or offset from center. The cab has windows on all sides, giving 360° visibility.
- **Bi-directional capability**: The locomotive can operate at full power in either direction. No turntable needed at terminals — the engineer simply walks to the other end of the cab (on dual-cab units) or reverses the controls (on single-cab units, with a long hood forward configuration).

## Wheel Arrangements

The Whyte notation used for steam (e.g., 4-6-2) is replaced by the **UIC/AAR axle notation** for diesel-electrics:
- **B-B**: Two 2-axle trucks, all axles powered. 1,000-2,000 HP. Light road and switching. Example: EMD GP7, GP9, GP38-2.
- **C-C**: Two 3-axle trucks, all axles powered. 3,000-4,500 HP. Heavy road freight. Example: EMD SD40-2, GE Dash 9, AC4400CW.
- **A1A-A1A**: Two 3-axle trucks, center axle unpowered. Passenger service with lighter axle loads.

## Prerequisites

- [Diesel-Electric Locomotives](./diesel-locomotives.md) — parent capability
- [Railways](./railways.md) — gauge, loading gauge, track structure
- [Iron and Steel](../metals/iron-steel.md) — truck frame castings, wheelsets, frames

## See Also

- [Diesel-Electric Locomotives](./diesel-locomotives.md) — parent capability
- [Diesel-Electric Powertrain](./diesel-locomotives.diesel-electric-powertrain.md) — transmission
- [Railways](./railways.md) — track and operations

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transport](./index.md) • [All Domains](../index.md)*
