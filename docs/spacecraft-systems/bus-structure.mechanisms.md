# Mechanisms and Release Devices

> **Node ID**: spacecraft-systems.bus-structure.mechanisms
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: `spacecraft-systems.bus-structure`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 40-200+
> **Outputs**: satellite_structures, deployable_arrays
> **Critical**: Yes

Mechanisms and release devices are the moving components that hold deployables in their stowed configuration through launch and then actuate on command in orbit. They include non-explosive release devices (Frangibolt, HDRM), pyrotechnic release devices (explosive bolt cutters, separation nuts), and the hinge and appropriation actuators that drive and control deployment.

Release devices trade hold-off load, actuation shock, resetability, and flight heritage. The Frangibolt uses a shape-memory alloy collar to fracture a notched bolt with minimal shock (300g at 12"), while paraffin-actuated HDRMs achieve even lower shock (under 100g at 12"). Pyrotechnic devices remain indispensable for high-load separations (up to 200 kN hold-off) despite generating pyroshock transients of up to 3000g near the source.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Frangibolt hold-off load | 5-45 kN | SMA actuated |
| HDRM hold-off load | 5-25 kN | Paraffin actuated |
| Pyrotechnic hold-off load | 10-200 kN | Single-shot |
| Frangibolt shock | 300g @ 12" | Very low |
| HDRM shock | <100g @ 12" | Lowest available |
| Pyro shock | 3000g @ 12" | High |
| Deployment damper | 10-30°/s | Silicone oil |

## Mechanism Selection Steps

1. Determine hold-off load from coupled load analysis of stowed configuration
2. Identify pyroshock-sensitive components; map standoff distances
3. If hold-off <25 kN and shock-sensitive components nearby: select HDRM
4. If hold-off <45 kN and resetability required: select Frangibolt
5. If hold-off >45 kN or heritage required: select pyrotechnic device
6. Verify release command path redundancy (dual ignition circuits)
7. Design deployment damping: torsion spring + viscous damper
8. Qualify in thermal-vacuum at hot, cold, and ambient temperature points

## Prerequisites

- [Machine tools](../machine-tools/index.md) — precision machining of notched bolts, hinges
- [Aluminium](../metals/aluminum.md) — structural fittings, brackets
- Shape-memory alloy stock (NiTi) for Frangibolt collars
- [Vacuum](../vacuum/index.md) chamber for release qualification testing

## See Also

- [Bus Structure + Deployables](./bus-structure.md) — parent capability
- [Primary Structure Fabrication](./bus-structure.primary-structure.md) — sibling process
- [Deployable Structures](./bus-structure.deployable-structures.md) — sibling process
