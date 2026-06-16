# Chassis & Frame Construction

> **Node ID**: transport.motor-vehicles.chassis-frame-construction
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.motor-vehicles`](./motor-vehicles.md)
> **Timeline**: Years 20-40+
> **Outputs**: vehicle_chassis, wheel_assemblies
> **Critical**: No

The chassis is the load-carrying skeleton of a vehicle — every component (engine, body, suspension, payload) ultimately mounts to it. Three architectures cover the full design space, each a different trade between simplicity, weight, and manufacturing complexity.

## Frame Architectures

**Ladder frame**: Two longitudinal side rails (channel or box section steel, 100–200 mm deep, 3–6 mm wall) joined by 3–6 cross members. Mild steel (yield 250–350 MPa) or HSLA steel (yield 450–550 MPa). The simplest and strongest design — used on all early cars, and on trucks and SUVs today. High load capacity (1–40 tonnes) but heavy (150–400 kg) and low torsional stiffness (1,000–3,000 Nm/degree).

**Unibody (monocoque)**: 20–50 stamped steel panels spot-welded into a single shell (3,000–5,000 welds) that carries all loads. Torsional rigidity 8,000–25,000 Nm/degree. 30–40% lighter than ladder frame. Standard for passenger cars since the 1960s.

**Space frame**: Triangulated tube framework (steel or aluminum, 25–60 mm diameter) with non-structural body panels. Highest rigidity per unit weight; slow to build — suited to low-volume sports cars and racing.

## Materials

- **Steel**: Deep-draw sheet (0.6–2.0 mm) for unibody panels; HSS and boron-alloy martensitic steel (yield 800–1500 MPa) for pillars and crash structures.
- **Aluminum**: 5000/6000-series sheet for lightweight bodies; extruded sections for space frames (Lotus Elise bonded-aluminum tub).
- **Composites**: Carbon-fibre-reinforced polymer monocoques for racing and high-end sports cars — 40–60% lighter than steel but require autoclave curing and remain expensive.

## Wheel Assemblies

Wheel assemblies combine the hub (machined steel or aluminum casting), tapered roller bearings, the rim (steel stamping or aluminum casting, 5.5–8.0 J × 14–18 inch), and mounting hardware. The hub bolts to the steering knuckle (front) or axle (rear). Tire manufacturing is covered separately.

## Prerequisites

- [Iron & Steel](../metals/iron-steel.md) — structural sheet and sections
- [Machine Tools](../machine-tools/index.md) — press forming, CNC cutting, welding fixtures

## See Also

- [Motor Vehicle Fundamentals](./motor-vehicles.md) — parent capability overview
- [Suspension Systems](./motor-vehicles.suspension-systems.md) — mounts to the chassis
- [Body Panel Stamping](./motor-vehicles.body-panel-stamping.md) — unibody panel forming

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
