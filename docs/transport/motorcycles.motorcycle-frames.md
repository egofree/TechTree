# Motorcycle Frame Design

> **Node ID**: transport.motorcycles.motorcycle-frames
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.motorcycles`](motorcycles.md)
> **Timeline**: Years 20-40+
> **Outputs**: scooter_frames
> **Critical**: No

The motorcycle frame is the structural chassis that ties the steering head, engine, swingarm pivot, and rider into a single load-bearing system. Frame design determines stiffness, weight distribution, and the feedback the rider feels through the handlebars.

## Frame Architectures

**Cradle frame**: One or two loops of steel tube (25-35 mm diameter, 1.5-2.5 mm wall) run from the steering head down and under the engine, cradling it. The classic design — Triumph Bonneville, Royal Enfield Bullet, Harley-Davidson Sportster. Inexpensive, repairable, forgiving. The double cradle adds a second tube each side for stiffness on larger engines.

**Backbone frame**: A single large-section spine (box-section steel or cast aluminum) from steering head to swingarm pivot, engine suspended below. Lighter than a cradle. The Honda Super Cub's pressed-steel backbone is mass-produced by stamping sheet steel and welding — the lowest-cost frame for small-displacement machines.

**Perimeter (twin-spar) frame**: Two aluminum beams (cast A356-T6 or extruded 6061-T6) flank the engine from steering head to swingarm pivot. The engine bolts in as a stressed member. Dominant on sport bikes since the 1980s. Maximum torsional stiffness for aggressive cornering. Manufacturing requires casting or extrusion capability plus precision CNC machining of the steering head and swingarm pivot bores.

**Trellis frame**: A triangulated lattice of short steel tubes (12-20 mm diameter, AISI 4130 CrMo), TIG-welded at nodes. Associated with Ducati since the Pantah (1979). Highest stiffness-to-weight ratio of the tubular designs. Many welds (30-60 per frame) require skilled labor and consistent quality control — each weld is a potential failure point.

## Materials

- **Steel tube** (4130 CrMo or mild steel): weldable, ductile, fatigue-resistant, low cost
- **Cast aluminum** (A356-T6): light, stiff, requires foundry and CNC machining
- **Carbon fiber** (premium, niche): lightest and stiffest, requires autoclave — beyond early bootstrap

## Prerequisites

- [Iron & Steel](../metals/iron-steel.md) — tubing, sheet, and plate
- [Machine Tools](../machine-tools/index.md) — mandrel bender, TIG/MIG welding, CNC machining
- [Motorcycles](motorcycles.md) — parent capability

## See Also

- [Motorcycles](motorcycles.md) — parent capability
- [Motorcycle Suspension](motorcycles.motorcycle-suspension.md) — fork and shock design

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
