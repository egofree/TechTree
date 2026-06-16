# Scramjet-Airframe Integration

> **Node ID**: `aerospace.supersonic-flight.scramjet-integration`
> **Domain**: [Aerospace](./index.md)
> **Parent**: [Supersonic & Hypersonic Flight](./supersonic-flight.md)
> **Dependencies**: [`aerospace.supersonic-flight`](supersonic-flight.md)
> **Outputs**: waverider_airframe, integrated_scramjet_vehicle
> **Timeline**: Years 60-150
> **Critical**: No

## Overview

At Mach 5+, no turbine survives the inlet temperature. The **scramjet** (supersonic-combustion ramjet) dispenses with rotating machinery — air is compressed only by the vehicle's own forebody shock system, fuel is injected into the supersonic stream, and combustion completes in milliseconds as the mixture traverses the combustor. The defining constraint is that *the scramjet cannot be separated from the airframe*: the vehicle's lower forebody is the inlet, its aft lower surface is the nozzle, and only the combustor resembles a conventional engine.

The **waverider** configuration exploits this coupling. The vehicle is shaped so its bow shock stays attached to the leading edges, "riding" the shock. The shock-compressed underbody flow is at high pressure and generates lift with minimal lateral spillage — a far more efficient hypersonic lifting body than a blunt capsule. The X-51A Waverider (Mach 5.1 for 210 seconds, 2010) and the cancelled HTV-2 (Mach 20 boost-glide target) both used waverider planforms. Because the scramjet only operates above Mach 4, every vehicle needs a boost phase — the X-43A used a Pegasus rocket, the X-51A a modified ATACMS missile. Combined-cycle engines (turbojet → ramjet → scramjet) that transition modes in flight remain experimental.

This process deliberately does *not* cover scramjet engine internals (combustor geometry, fuel injection, flameholding) — those belong to [jet-propulsion.ramjet-scramjet](./jet-propulsion.ramjet-scramjet.md). Here we cover only the airframe-propulsion *coupling*: forebody compression, aftbody nozzle, waverider shaping.

## Key Techniques

- **Waverider planform** — bow shock attached to leading edges; underbody flow shock-compressed for lift.
- **Forebody compression** — vehicle underside shapes the inlet shock system; 8–12° forebody angle typical.
- **Aftbody nozzle** — vehicle aft lower surface forms the divergent nozzle; expansion ratio set by vehicle length.
- **Boost-phase integration** — rocket or turbojet boost to Mach 4+ before scramjet ignition.
- **Combined-cycle (TBCC/RBCC)** — turbine-based or rocket-based combined cycle transitioning to scramjet.

## Prerequisites

- **[Jet Propulsion](./jet-propulsion.md)** — scramjet combustor design and fuel injection.
- **[Hypersonic Thermal Protection](./supersonic-flight.hypersonic-thermal.md)** — leading-edge materials for Mach 5+ shock-layer heating.
- **[Ceramics](../ceramics/index.md)** — refractory leading-edge and combustor materials.
- **[Supersonic & Hypersonic Flight](./supersonic-flight.md)** — parent capability.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md)*
