# Autorotation

> **Node ID**: aerospace.rotorcraft.autorotation
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.rotorcraft`](rotorcraft.md)
> **Timeline**: Years 30-50+
> **Outputs**: rotorcraft
> **Critical**: No

Autorotation is the maneuver that makes a helicopter survivable after total engine failure. With the engine dead, the pilot lowers the collective to minimum pitch and noses down, letting upward airflow through the rotor drive the blades like a windmill. The rotor keeps spinning, storing kinetic energy in the blade mass. Near the ground, the pilot flares — pulling collective and nose-up — converting that stored rotor energy into a brief burst of lift to arrest descent for a survivable touchdown.

The enabler is the **freewheeling (sprag) clutch** between engine and gearbox: when the engine stops driving the rotor, the clutch releases so the rotor is not dragged down by a seized engine. Without it, engine seizure would stop the rotor in seconds. Every certified helicopter must demonstrate a safe power-off autorotation and landing to a defined area.

## Key Parameters

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Rotor RPM (autorotation) | 90-110% normal | Stored energy target |
| Rate of descent | 1200-2400 ft/min | Steep glide angle |
| Flare height | 10-50 ft AGL | Energy conversion window |
| Touchdown speed | 0-20 kt | Near-vertical landing |

## Prerequisites

- [Rotorcraft](rotorcraft.md) — parent capability overview
- [Rotor Systems](rotorcraft.rotor-systems.md) — rotor inertia stores the energy
- [Flight Control](rotorcraft.flight-control.md) — collective control for the flare

## See Also

- [Rotorcraft](rotorcraft.md) — parent capability overview
- [Rotor Systems](rotorcraft.rotor-systems.md) — rotor kinetic energy storage
- [Flight Control](rotorcraft.flight-control.md) — collective input for flare

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
