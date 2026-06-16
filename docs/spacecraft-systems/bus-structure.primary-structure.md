# Primary Structure Fabrication

> **Node ID**: spacecraft-systems.bus-structure.primary-structure
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: `spacecraft-systems.bus-structure`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 40-200+
> **Outputs**: satellite_structures
> **Critical**: Yes

Primary structure fabrication encompasses the design and manufacture of the spacecraft bus skeleton: honeycomb sandwich panels, isogrid plates, central thrust tubes, and equipment brackets. These elements carry the launch interface load through ascent and then support all subsystems in orbit with the lowest possible mass fraction — typically 15-25% of dry bus mass.

The dominant structural element is the aluminium honeycomb sandwich panel: two 0.3 mm faceskins bonded to a 25 mm aluminium core, yielding a panel with high bending stiffness at approximately 2.5 kg/m². Isogrid plates machined from solid aluminium stock provide an alternative where through-thickness loads or attachment density make honeycomb impractical. Both approaches require [machine tools](../machine-tools/index.md) capable of 0.05 mm tolerances over metre-scale parts.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Honeycomb core thickness | 25 mm | Range 10-50 mm |
| Faceskin thickness | 0.30 mm | Al 6061-T6 or CFRP |
| Panel areal density | 2.5 kg/m² | Range 1.5-8.0 |
| Isogrid rib spacing | 70-100 mm | Equilateral triangle |
| Tolerance (machined) | ±0.05 mm | 5-axis CNC |
| Structure mass fraction | 15-25% | Of dry bus mass |

## Fabrication Steps

1. Cut facesheets from coil stock; flatten and solvent-clean
2. Machine honeycomb core to panel footprint; expand to nominal cell geometry
3. Pot core inserts at fastener locations with epoxy filler
4. Lay up adhesive film on inner faceskin; position core; add second faceskin
5. Vacuum-bag and autoclave cure at 120-180°C, 0.3-0.6 MPa, 90-120 min
6. Trim to final dimensions; machine edge close-outs
7. Ultrasonic C-scan for bondline voids (reject >10 mm diameter)
8. Install potted inserts; verify pull-out strength ≥2 kN

## Prerequisites

- [Machine tools](../machine-tools/index.md) — 5-axis CNC for isogrid machining
- [Aluminium](../metals/aluminum.md) — 6061-T6, 7075-T6 stock
- [Composites](../polymers/composites.md) — CFRP facesheets for high-stiffness panels
- Autoclave with vacuum bagging capability

## See Also

- [Bus Structure + Deployables](./bus-structure.md) — parent capability
- [Deployable Structures](./bus-structure.deployable-structures.md) — sibling process
- [Mechanisms and Release Devices](./bus-structure.mechanisms.md) — sibling process
