# High-Speed Track Geometry

> **Node ID**: transport.high-speed-rail.track-geometry
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.high-speed-rail`](high-speed-rail.md)
> **Timeline**: Years 40-60+
> **Outputs**: high_speed_trains
> **Critical**: No

The track geometry process designs and builds the dedicated alignment that makes 300+ km/h cruising dynamically stable. At those speeds, a track misalignment of a few millimeters — invisible to the eye and unremarkable on conventional track — excites violent wheel-rail hunting and threatens derailment. The process trades construction cost for geometric precision: slab track costs 2–3× ballasted track but holds tolerance to ±1–2 mm over 10 m chords for 60 years.

## Alignment Standards (300 km/h Design Speed)

- **Curve radius**: Minimum 5,000 m (7,000–10,000 m for 350 km/h). Curves of 15,000 m radius are preferred where terrain allows. Lateral acceleration capped at 1.0 m/s² at design speed.
- **Gradient**: Maximum 2.0–2.5% (TGV Paris–Lyon holds <1.5%). Steeper grades demand disproportionate tractive power and braking capacity.
- **Superelevation (cant)**: 150–180 mm maximum (200 mm in special cases). Cant deficiency (felt as passenger lateral force) capped at 90–130 mm.
- **Transition spirals**: Clothoid (linear-curvature-ramp) spirals 200–400 m long so lateral acceleration builds gradually. Spiral length scales with speed cubed.

## Construction Types

- **Ballastless (slab) track**: Continuously reinforced concrete slab (C40/50 grade, 5–6 m wide) supports rails directly on elastic pads. Shinkansen precast slabs (5 m × 2.4 m × 0.6 m) on cement-asphalt mortar bed; Rheda cast-in-situ variant. Holds ±1–2 mm geometric tolerance over 10 m chords.
- **Ballasted track**: Crushed stone ballast (31.5–50 mm graded granite or basalt, 300–350 mm depth) supports timber or concrete sleepers. Used on 200–250 km/h segments for lower cost; requires ballast bonding (polyurethane) to prevent particle flight at speed.
- **Continuous welded rail (CWR)**: Rails welded into 1–2 km strings by flash-butt or thermite welding. No bolted joints. Tensioned to neutral temperature (20–25°C) to prevent summer buckling and winter fracture.

## Measurement and Maintenance

Track geometry is recorded by a track recording car at 200+ km/h every 1–4 weeks: gauge, cross-level, alignment, twist, and longitudinal profile are sampled every 0.25 m. Tolerances: gauge ±2 mm on tangent, cross-level ±3 mm, alignment ±2 mm over 10 m chord. Out-of-tolerance sections are tamped (ballasted) or ground/shimmed (slab) within 24–48 hours. Rail surface is ground every 30–100 MGT (million gross tonnes) to remove rolling-contact-fatigue cracks before they propagate beyond 3 mm depth.

## Prerequisites

- [High-Speed Rail](high-speed-rail.md) — parent capability
- [Railways](./railways.md) — conventional track construction fundamentals
- [Iron & Steel](../metals/iron-steel.md) — rail and structural steel
- [Construction](../construction/index.md) — earthworks, tunnels, viaducts

## See Also

- [High-Speed Rail](high-speed-rail.md) — parent capability overview
- [Aerodynamic Trainset Design](high-speed-rail.aerodynamic-design.md) — vehicle-side complement
- [Railways](./railways.md) — conventional track foundations

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
