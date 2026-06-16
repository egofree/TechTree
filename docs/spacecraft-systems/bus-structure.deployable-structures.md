# Deployable Structures

> **Node ID**: spacecraft-systems.bus-structure.deployable-structures
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: `spacecraft-systems.bus-structure`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 40-200+
> **Outputs**: deployable_arrays
> **Critical**: Yes

Deployable structures are appendages that fold or roll into a compact stowed volume for launch and then extend on orbit to their operational configuration: solar arrays, antenna reflectors, magnetometer booms, and instrument radiators. The deployment mechanism must achieve reliable, single-shot extension in vacuum without ground intervention, with deployment ratios of 5:1 to 50:1 between stowed and deployed states.

The dominant deployable types are rigid-panel solar arrays (Z-fold, 5:1 stowed ratio), flexible-blanket arrays on CoilABLE booms (10:1 to 20:1), and STEM (Storable Tubular Extendible Member) booms for instruments and antennas (30:1). Each trades stowed-volume efficiency against deployment complexity and structural stiffness in the deployed state. All deployment designs require [vacuum](../vacuum/index.md) chamber testing to verify reliable actuation in the absence of atmospheric damping.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Rigid panel stowed ratio | 5:1 | Z-fold |
| CoilABLE boom stowed ratio | 20:1 | 10-50 m length |
| STEM stowed ratio | 30:1 | Magnetometer booms |
| Deployed natural frequency | 0.1-0.5 Hz | First bending mode |
| Deployment velocity | 10-30°/s | Damped spring |
| Deployment time | 10-60 s | Rigid panels |

## Deployment Sequence Steps

1. Confirm spacecraft attitude stabilised within 5° of sun-pointing
2. Command release devices (HDRM or Frangibolt) to actuate
3. Release springs push yoke outward; yoke rotates 90° to deployed position
4. Panel deployment begins; torsion springs drive panels open
5. Viscous damper limits velocity to 10-30°/s throughout stroke
6. First panel pair latches; microswitch confirms engagement
7. Second panel pair latches; deployment complete
8. Solar array drive actuator rotates array to sun-tracking position

## Prerequisites

- [Machine tools](../machine-tools/index.md) — precision hinge machining
- [Aluminium](../metals/aluminum.md) — longerons, battens, hinges
- [Composites](../polymers/composites.md) — CFRP boom longerons, panel substrates
- Vacuum chamber for thermal-vacuum deployment testing

## See Also

- [Bus Structure + Deployables](./bus-structure.md) — parent capability
- [Primary Structure Fabrication](./bus-structure.primary-structure.md) — sibling process
- [Mechanisms and Release Devices](./bus-structure.mechanisms.md) — sibling process
