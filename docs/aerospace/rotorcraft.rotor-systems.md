# Rotor Systems

> **Node ID**: aerospace.rotorcraft.rotor-systems
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.rotorcraft`](rotorcraft.md)
> **Timeline**: Years 30-50+
> **Outputs**: helicopter_rotors
> **Critical**: No

The rotor system is the defining component of any helicopter: a spinning assembly of hub and blades that must simultaneously generate lift, accept collective and cyclic pitch commands, absorb the dissymmetry of forward flight through flapping, and survive millions of fatigue cycles. The hub architecture — fully articulated, semi-rigid (teetering), or rigid — sets the aircraft's whole character, from two-bladed Bell simplicity to eight-bladed Mi-26 heavy lift.

Each blade is a wing with three coupled degrees of freedom: feathering (pitch control via the swashplate), flapping (vertical bending to balance lift across the disc), and lead-lag (in-plane motion absorbing Coriolis effects). Blade construction evolved from all-aluminum spars and skins to modern composite spar/skin designs with foam or honeycomb cores, giving the tailored stiffness distribution needed for hingeless hubs.

## Key Parameters

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Tip speed | 200-220 m/s | Subsonic to avoid compressibility losses |
| Blade count | 2 (teetering) to 8 (heavy-lift) | More blades = smoother, heavier hub |
| Disc loading | 6-40 kg/m² | Lower = more efficient hover |
| Hub type | Articulated / semi-rigid / rigid | Sets vibration, agility, complexity |
| Coning angle | 3-7° | Upward flex from lift |

## Prerequisites

- [Rotorcraft](rotorcraft.md) — parent capability overview
- [Aluminum](../metals/aluminum.md) — blade spars and skins
- [Precision machine tools](../machine-tools/index.md) — hub bearings, pitch links

## See Also

- [Rotorcraft](rotorcraft.md) — parent capability overview
- [Flight Control](rotorcraft.flight-control.md) — swashplate that drives blade pitch
- [Autorotation](rotorcraft.autorotation.md) — rotor behavior in power-off flight

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
