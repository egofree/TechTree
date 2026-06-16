# Water Recovery

> **Node ID**: human-spaceflight.eclss.water-recovery
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.eclss`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: water_recovery_systems
> **Critical**: Yes

Water recovery reclaims potable water from cabin humidity condensate, urine, and hygiene waste streams, achieving 93% overall loop closure on the ISS — roughly 6,000 kg of water per year for a 6-crew complement. The process train consists of a particulate prefilter, sequential multifiltration beds of activated carbon and ion-exchange resins, a catalytic Volatile Removal Assembly oxidising trace organics at 130°C, a final ion-exchange polish, and iodine dosing at 0.5-2.0 mg/L for microbial control.

Product water meets EPA and WHO potable standards: total organic carbon below 0.5 mg/L, conductivity below 10 µS/cm, and microbial counts below 1 CFU/100 mL. Closing the loop on water breaks the resupply dependency: every kilogram reclaimed is one less kilogram launched from Earth, and on a 6-crew 180-day mission the WRS saves 2,400-3,200 kg of launch mass.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Overall loop closure | 93% | Urine 85% + condensate 99% |
| Annual reclamation | ~6,000 kg/yr (6 crew) | Eliminates ~6 resupply flights |
| Product water TOC | < 0.5 mg/L | EPA potable standard |
| Product water microbes | < 1 CFU/100 mL | WHO potable standard |
| Iodine residual | 0.5-2.0 mg/L | Microbial check valve |
| VRA oxidiser temp | 130°C | Catalytic oxidation of organics |
| MF bed replacement | 30-90 days | Conductivity-triggered |
| Brine purge | 15% of urine volume | Unrecovered water |

## Prerequisites

- [Water](../water/index.md) — filtration, ion-exchange, purification heritage
- [Environmental Control & Life Support](./eclss.md) — parent capability

## See Also

- [ECLSS](./eclss.md) — parent capability
- [Atmosphere Management](./eclss.atmosphere-management.md) — OGS consumes product water
- [Waste Management](./eclss.waste-management.md) — supplies urine feedstock
