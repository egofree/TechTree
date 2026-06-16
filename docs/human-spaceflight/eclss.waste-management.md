# Waste Management

> **Node ID**: human-spaceflight.eclss.waste-management
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.eclss`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: eclss_systems
> **Critical**: Yes

Waste management collects, stabilises, and contains the solid and liquid metabolic output of the crew — feces (0.11-0.15 kg/day per crew), urine (1.0-1.5 kg/day per crew), and trash (1.0-1.5 kg/day per crew of food packaging, used clothing, hygiene wipes, and experiment residues). The Waste Management Facility (WMF) uses a vacuum toilet that air-entrains feces into a storage bag and routes urine through a centrifugal fan separator to the Water Recovery System. Fecal waste is vacuum-dried, bagged, and stored in sealed canisters for disposal by destructive atmospheric reentry in a cargo vehicle.

Trash is compacted by a factor of 3-5 and either loaded into cargo vehicles for reentry or returned to Earth for analysis. Beyond LEO, where reentry disposal is unavailable, long-duration missions will require in-situ waste processing such as incineration, pyrolysis, or wet-air oxidation to reduce volume and stabilise biological hazards.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Feces per crew | 0.11-0.15 kg/day | Vacuum-dried, bagged |
| Urine per crew | 1.0-1.5 kg/day | To WRS |
| Trash per crew | 1.0-1.5 kg/day | Packaging, wipes, clothing |
| Compaction ratio | 3-5× volume reduction | Manual or powered compactor |
| WMF urine separator | centrifugal fan | Air-liquid separation |
| Fecal storage | sealed canister | Loaded into Cygnus/Progress for reentry |
| Canister capacity | ~30 crew-days | Replaced as needed |

## Prerequisites

- [Environmental Control & Life Support](./eclss.md) — parent capability
- [Water Recovery](./eclss.water-recovery.md) — receives urine for processing

## See Also

- [ECLSS](./eclss.md) — parent capability
- [Water Recovery](./eclss.water-recovery.md) — urine feedstock consumer
- [Fire Detection & Suppression](./eclss.fire-detection-suppression.md) — waste storage fire risk
