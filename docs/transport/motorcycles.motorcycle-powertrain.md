# Motorcycle Powertrain Integration

> **Node ID**: transport.motorcycles.motorcycle-powertrain
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.motorcycles`](motorcycles.md)
> **Timeline**: Years 20-40+
> **Outputs**: motorcycles
> **Critical**: No

Motorcycle powertrain integration covers the engine, clutch, gearbox, and final drive — the systems that convert fuel (or battery energy) into rotation at the rear wheel. Engine fundamentals belong to [internal combustion](../energy/internal-combustion.md); this process covers motorcycle-specific packaging and drive choices.

## Engine Configurations

**Single cylinder** (250-650 cc): Light, narrow, cheap, thumping power pulse. Used on dual-sport, budget commuters, entry-level machines.

**Parallel twin** (300-800 cc): Two cylinders side by side, sharing a crankpin (360°) or offset (180°, 270°). Narrower than a four, smoother than a single. Dominant in modern middleweights (Yamaha MT-07, Kawasaki Ninja 400).

**Inline-four** (600-1000 cc): The classic sport-bike engine since the Honda CB750 (1969). Smooth, high-revving (12,000-15,000 rpm), wide but compact fore-aft. Power: 80-200 HP.

**V-twin** (600-1900 cc): Two cylinders in a V (45° Harley, 90° Ducati "L-twin", 60-75° Moto Guzzi). Strong low-end torque, characterful exhaust note.

**Boxer twin** (BMW R series since 1923): Horizontally opposed cylinders, air-cooled, shaft drive. Low center of gravity. Longest-produced motorcycle engine configuration still in series production.

## Clutch, Gearbox, and Final Drive

**Wet multi-plate clutch**: Multiple friction and steel plates bathed in engine oil — compact, self-cooling. Standard on nearly all motorcycles.

**Sequential constant-mesh gearbox**: One gear at a time through a shift drum — 1 down, 4-6 up. No skip-shifting. Prevents missed shifts at high rpm.

**Final drive**: Chain (lightest, ~96% efficient, needs lube every 500-1000 km); Belt (quieter, ~80,000 km life — Harley, scooters); Shaft (maintenance-free, heavier, torque reaction — BMW, Gold Wing).

## Electric Powertrains

Hub motor or mid-drive motor with single-speed reduction — no clutch, no gearbox. Instant torque from zero rpm. See [Electricity](../energy/electricity.md).

## Prerequisites

- [Internal Combustion](../energy/internal-combustion.md) — engine fundamentals
- [Electricity](../energy/electricity.md) — electric motorcycle motors
- [Machine Tools](../machine-tools/index.md) — crankshaft, gearbox, cylinder machining
- [Motorcycles](motorcycles.md) — parent capability

## See Also

- [Motorcycles](motorcycles.md) — parent capability and engine as stressed member
- [Internal Combustion](../energy/internal-combustion.md) — Otto-cycle fundamentals

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
