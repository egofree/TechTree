# Solar Arrays

> **Node ID**: spacecraft-systems.spacecraft-power.solar-arrays
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.spacecraft-power`](./spacecraft-power.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: solar_arrays
> **Critical**: No

Spacecraft solar arrays convert sunlight directly to electrical power using III-V compound semiconductor multi-junction cells. Unlike terrestrial [photovoltaic](../energy/photovoltaics.md) panels, space cells use GaInP/GaAs/Ge triple-junction structures grown on germanium substrates to maximize efficiency per unit mass and survive the radiation environment. The Azur Space 3G30C achieves 29.5% BOL efficiency at AM0 conditions, degrading to approximately 26.6% after 15 years in GEO.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Cell BOL efficiency (3G30C) | 29.5% |
| Cell EOL efficiency (15yr GEO) | 26.6% |
| Panel-level specific power | 80-150 W/kg |
| Panel areal density | 2-5 kg/m² |
| Coverglass thickness | 100-300 μm |
| Cell thickness | 140 μm |
| Bus voltage | 28V-100V |

## Process Overview

1. **Cell growth**: MOVPE deposition of GaInP/GaAs/Ge junctions on germanium wafer substrates
2. **Cell processing**: Anti-reflection coating (TiO₂/Al₂O₃), grid metallization, coverglass bonding
3. **Panel assembly**: Cell-to-cell interconnect welding on carbon-fiber substrate
4. **Integration**: Shunt diode installation, harness attachment, hinge mounting
5. **Test**: Air-mass-zero flash testing, vibration qualification, deployment verification

## Prerequisites

- Energy.photovoltaics capability (p-n junction fundamentals and cell fabrication heritage)
- Silicon/germanium semiconductor substrates for III-V epitaxial growth
- Vacuum environment compatibility (no outgassing materials in panel stack)

## See Also

- [Spacecraft Power Systems](./spacecraft-power.md) — parent capability
- [Space Batteries](./spacecraft-power.space-batteries.md) — eclipse energy storage
- [Photovoltaic Solar Power](../energy/photovoltaics.md) — terrestrial PV heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
