# Radiator Design

> **Node ID**: spacecraft-systems.thermal-control.radiator-design
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: `spacecraft-systems.thermal-control`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 40-200+
> **Outputs**: thermal_hardware
> **Critical**: Yes

Radiator design is the process of sizing, surfacing, and orienting the panels that reject spacecraft waste heat to deep space. The radiator is the ultimate heat sink for all thermal dissipation — every watt generated internally must ultimately be radiated away as infrared radiation from a surface at a known temperature and emissivity.

Radiator area is determined by the Stefan-Boltzmann law: Q = ε·σ·A·T⁴. A 1 kW heat rejection at +30°C (303 K) with ε = 0.88 requires 1.18 m² of double-sided panel facing deep space. If the radiator faces the sun, solar input (α·S·A, where S = 1361 W/m²) must be subtracted from the net rejection, driving radiator orientation perpendicular to the sun line or behind sun-shielding solar arrays.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Heat rejection (body-mounted) | 100-200 W/m² | Small satellites |
| Heat rejection (double-sided) | 350-700 W/m² | GEO commsats |
| OSR α/ε | 0.08/0.80 | Silvered Teflon |
| Radiator temperature | +20 to +40°C | Typical |
| Solar constant | 1361 W/m² | At 1 AU |
| Stefan-Boltzmann σ | 5.67×10⁻⁸ W/m²·K⁴ | — |

## Radiator Sizing Steps

1. Determine total heat rejection requirement (W) from power budget
2. Select radiator surface coating (target α/ε ≈ 0.10 for sun-facing, high ε for shadowed)
3. Calculate gross area: A = Q / (2·ε·σ·T⁴) for double-sided, neglecting solar input
4. Subtract environmental input: Q_net = Q_rejected - α·S·A (for sun-facing surfaces)
5. Add margin factor (1.25×) for end-of-life coating degradation
6. Orient radiator to minimise solar incidence; use solar arrays as sun shields
7. Route heat pipe or LHP to distribute heat uniformly across radiator area
8. Verify in thermal-vacuum balance test; correlate TMM to ±10°C

## Prerequisites

- [Aluminium](../metals/index.md) — radiator substrate, heat pipe envelopes
- [Polymers](../polymers/index.md) — silvered Teflon coating application
- [Vacuum](../vacuum/index.md) — thermal-vacuum balance test facility

## See Also

- [Thermal Control](./thermal-control.md) — parent capability
- [Passive Thermal Control](./thermal-control.passive-thermal.md) — sibling process
- [Active Thermal Control](./thermal-control.active-thermal.md) — sibling process
