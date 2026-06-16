# Storm Shelters

> **Node ID**: human-spaceflight.radiation-protection.storm-shelters
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.radiation-protection`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 60+
> **Outputs**: radiation_protection
> **Critical**: No

Storm shelters are compact, heavily shielded volumes within a spacecraft where the crew retreats during major solar particle events (SPE). The design principle is to maximise areal density — grams per square centimetre of projected shielding area — using hydrogen-rich materials (water, polyethylene) rather than dense metals, because high-Z materials produce problematic secondary radiation when struck by high-energy particles. A target areal density of 5-10 g/cm² reduces SPE dose by 90-98%. The standard approach is configurational: arrange existing consumables (water tanks, food stores, waste) around a central refuge to avoid carrying dedicated dead-weight shielding.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Target areal density | 5-10 g/cm² | NASA HRP recommendation |
| SPE dose reduction (at 10 g/cm²) | ~ 98% | Water/polyethylene shield |
| GCR dose reduction (at 10 g/cm²) | ~ 25-30% | Limited by secondaries |
| Best practical material | Water / polyethylene | High hydrogen fraction |
| SPE warning time | 10-60 minutes | Coronagraph to particle arrival |
| Unshielded extreme SPE dose | 1,000-10,000 mSv | Carrington-class event |
| Sheltered extreme SPE dose | 20-200 mSv | Same event with 10 g/cm² |

## Prerequisites

- [Radiation Protection](./radiation-protection.md) — parent capability

## See Also

- [Radiation Protection](./radiation-protection.md) — parent capability
- [Dosimetry & Monitoring](./radiation-protection.dosimetry-monitoring.md) — SPE detection and alert
- [ECLSS](./eclss.md) — water tanks as configurational shielding
