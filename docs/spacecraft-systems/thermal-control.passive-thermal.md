# Passive Thermal Control

> **Node ID**: spacecraft-systems.thermal-control.passive-thermal
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: `spacecraft-systems.thermal-control`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 40-200+
> **Outputs**: thermal_hardware
> **Critical**: Yes

Passive thermal control uses materials and geometry — not powered actuators — to maintain spacecraft temperatures within limits. The three primary passive elements are multi-layer insulation (MLI) for radiative insulation, surface coatings (paints, films, treatments) for controlling solar absorption and infrared emission, and constant-conductance heat pipes for passive heat transport between source and radiator.

MLI blankets of 20-30 aluminised Kapton layers separated by Dacron net achieve effective emissivity below 0.02, blocking over 99% of radiative heat transfer. Surface coatings span solar absorptivity (α) from 0.08 (silvered Teflon) to 0.97 (black paint) and infrared emissivity (ε) from 0.05 (aluminised Kapton) to 0.89 (black paint). Heat pipes using ammonia as the working fluid transport 50-500 W per pipe with effective conductivity 100-1000× that of solid copper.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| MLI effective emissivity | <0.02 | 30-layer blanket |
| MLI layer count | 30 | Range 5-40 |
| White paint α/ε | 0.25/0.88 | Z93P silicate |
| Silvered Teflon α/ε | 0.08/0.80 | Radiator surface |
| Heat pipe capacity | 50-500 W | Ammonia, grooved wick |
| Heat pipe conductivity | 10,000-50,000 W/m·K | Effective |

## Passive Design Steps

1. Define worst-case hot and cold orbital environments (solar flux, albedo, Earth IR)
2. Map component dissipation profiles over orbit (including eclipse periods)
3. Select external coating α/ε to achieve radiator equilibrium temperature near target
4. Wrap non-radiator surfaces in MLI (30 layers for external, 5-10 for internal)
5. Place heat pipes between high-dissipation electronics and radiator surfaces
6. Size radiator area from Q = ε·σ·A·T⁴ (Stefan-Boltzmann)
7. Build thermal mathematical model (TMM); iterate coating selection
8. Verify margins in thermal-vacuum balance test (model correlation ±10°C)

## Prerequisites

- [Aluminium](../metals/index.md) — heat pipe envelopes, radiator substrates
- [Polymers](../polymers/index.md) — Kapton, Dacron net, MLI materials
- [Vacuum](../vacuum/index.md) — thermal-vacuum test chamber for qualification

## See Also

- [Thermal Control](./thermal-control.md) — parent capability
- [Active Thermal Control](./thermal-control.active-thermal.md) — sibling process
- [Radiator Design](./thermal-control.radiator-design.md) — sibling process
