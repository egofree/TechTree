# Structural Design

> **Node ID**: `launch-vehicles.vehicle-architecture.structural-design`
> **Domain**: [Launch Vehicles](./index.md)
> **Parent**: [Vehicle Architecture](./vehicle-architecture.md)
> **Outputs**: propellant_tanks, thrust_structures, isogrid_panels
> **Timeline**: Years 30-200+

## Overview

Launch vehicle structural design integrates three load-bearing subsystems: propellant tanks (the
primary airframe), interstages (cylinders connecting stages), and the thrust structure (distributes
engine force into the aft dome). The dominant material is **Aluminium-Lithium 2195 (Al-Li 2195)**,
developed for the Space Shuttle Super Lightweight Tank, which remains the benchmark for
cryogenic-tank alloys.

## Al-Li 2195 Properties

| Property | Al-Li 2195 | Al 2219 (legacy) |
|----------|-----------|------------------|
| Density | 2.70 g/cm³ | 2.84 g/cm³ |
| Ultimate tensile strength | 550 MPa | 430 MPa |
| Yield strength | 460 MPa | 290 MPa |
| Cryogenic toughness | Excellent | Good |

The 1.0-1.3% lithium addition reduces density by approximately 5% versus Al 2219 while increasing
stiffness and yield strength. This translates directly to payload: every kilogram of tank mass
saved becomes a kilogram of additional payload.

## Isogrid and Orthogrid Patterns

Tank walls are machined from thick plate to remove unnecessary material, leaving a stiffening grid:

- **Isogrid**: triangular cell pattern providing near-isotropic stiffness (equal in all directions).
  The triangular cells distribute load uniformly under combined axial compression, bending, and
  torsion. Machined on 3-5 axis CNC mills from 20-40 mm plate, leaving 1.5-3 mm skins with 5-8 mm
  ribs. Used on Delta IV, SLS, and many spacecraft bus structures.
- **Orthogrid**: rectangular cell pattern, easier to machine and better for directional load paths.
  Used on Falcon 9 tanks and the Shuttle External Tank. Slightly less mass-efficient than isogrid
  for uniform loads but cheaper to produce.

## Friction Stir Welding

Tank cylinders and domes are joined by **friction stir welding (FSW)** — a solid-state process
where a rotating pin tool plastically stirs the metal across the joint line without melting it.
FSW joints on Al-Li 2195 achieve 85-90% of parent-metal strength, versus 60-70% for TIG welding,
with no porosity and minimal distortion. The process is critical for cryogenic tanks that must
contain liquid oxygen (-183°C) and liquid hydrogen (-253°C) without leakage.

## Thrust Structure

The thrust structure transmits the full engine thrust load into the tank aft dome. For a Falcon 9
with nine Merlin engines producing 7,607 kN, this structure weighs under 2 tonnes — a
thrust-to-weight ratio of nearly 400:1. Designs include conical adaptors (Atlas V), cruciform
beams (Saturn V S-IC), and the SpaceX Octaweb (a single machined ring with nine engine pockets).

## See Also

- [Vehicle Architecture](./vehicle-architecture.md) — parent capability
- [Staging Design](./vehicle-architecture.staging-design.md) — interstage design
- [Aluminum](../metals/aluminum.md) — Al-Li 2195 alloy source

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
