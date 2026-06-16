# Habitat Module Fabrication

> **Node ID**: human-spaceflight.space-stations.habitat-modules
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.space-stations`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: habitat_modules, space_stations
> **Critical**: Yes

Habitat module fabrication encompasses the design, construction, and integration of pressurised cylindrical shells that form the habitable volume of a space station. Each module is a human-rated pressure vessel: a 4.2-4.5 m diameter cylinder with end domes, welded from 2219-T87 aluminium alloy at 3.0-4.8 mm wall thickness, wrapped in meteoroid shielding, and fitted with internal rack rails, utility distribution, and subsystem hardware.

The dominant material is [aluminium](../metals/aluminum.md) alloy 2219-T87 — selected for weldability, fracture toughness, and heritage from the Saturn V programme. Modules integrate to the station via the Common Berthing Mechanism or APAS docking system, requiring precision-machined interface rings held to ±0.05 mm flatness across a 1.8 m diameter flange.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Module diameter | 4.2-4.5 m | ISS standard |
| Wall material | Al 2219-T87 | 3.0-4.8 mm |
| End dome shape | Hemispherical or ellipsoidal | |
| Design pressure | 135 kPa (1.33 atm) | 1.33× MEOP |
| Meteoroid shield | Modified Whipple | Nextel-Kevlar stuffed |
| Internal rack | ISPR (1.05 × 1.90 × 0.86 m) | 700 kg capacity |

## Fabrication Steps

1. Machine barrel panels and forge end domes from 2219 plate
2. Friction stir weld barrel panels into cylinder (full penetration)
3. Weld end domes to barrel; X-ray inspect all welds
4. Machine CBM/APAS interface ring to ±0.05 mm flatness
5. Install internal standoffs and rack rails
6. Apply multilayer insulation and meteoroid shield standoffs
7. Pressure test to 1.33× MEOP; leak test with helium mass spectrometer

## Prerequisites

- [Aluminium](../metals/aluminum.md) — 2219-T87 plate stock
- [Machine tools](../machine-tools/index.md) — precision ring machining
- [Construction](../construction/index.md) — structural assembly techniques
- Friction stir welding capability

## See Also

- [Space Stations](./space-stations.md) — parent capability
- [Structural Docking + Berthing](./space-stations.structural-docking.md) — sibling process
- [Robotic Manipulator Arms](./space-stations.robotic-arms.md) — sibling process
