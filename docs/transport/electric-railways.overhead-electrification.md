# Overhead Electrification

> **Node ID**: transport.electric-railways.overhead-electrification
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.electric-railways`](electric-railways.md)
> **Timeline**: Years 25-50+
> **Outputs**: catenary_systems
> **Critical**: No

Overhead electrification supplies electric power to moving rail vehicles through a **contact wire** suspended above the track, touched by a spring-loaded **pantograph** on the locomotive or multiple-unit roof. It is the only practical collection method above ~160 km/h and the standard for mainline and high-speed electric railways worldwide.

## Catenary Geometry

The contact wire does not hang directly from supports — it is held nearly horizontal by a **messenger (catenary) wire** suspended in a natural curve, with short **dropper wires** connecting messenger to contact wire at 5-12 m intervals. This keeps the contact wire at constant height (±5 mm between droppers) so the pantograph does not bounce. **Steady arms** push the contact wire into a ±200-300 mm zig-zag ("stagger") so the pantograph wear band wears evenly instead of grooving.

## DC vs AC Choice

- **DC (600-3000 V)**: simple, feeds DC motors directly, but high current limits substation spacing to 7-15 km and wire cross-sections are heavy.
- **AC (15 kV/16.7 Hz or 25 kV/50-60 Hz)**: high voltage, low current, locomotive transformer steps voltage down. Substations every 40-60 km on 25 kV. The post-1950 standard for mainline electrification.

## Wave Mechanics Limit

The contact wire is a tensioned string. A pantograph disturbance propagates at `v = √(T/μ)`. For 25 kV high-speed catenary at 20-27 kN tension with low-mass wire, this reaches 400-560 km/h. Above ~70% of wave speed, the wire cannot follow the pantograph and collection fails. This is the hard physical ceiling on pantograph-catenary current collection.

## Prerequisites

- [Electric Railways](electric-railways.md) — parent capability and system context
- [Electricity](../energy/electricity.md) — grid supply and substations
- [Iron & Steel](../metals/iron-steel.md) — masts, structures, conductor rail
- [Railways](railways.md) — the track this electrification is built over

## See Also

- [Electric Railways](electric-railways.md) — parent capability
- [Traction Motor Design](electric-railways.traction-motor-design.md) — what the power feeds
- [Regenerative Braking](electric-railways.regenerative-braking.md) — reverse power flow

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
