# Decompression Illness

> **Node ID**: human-spaceflight.space-medicine.decompression-illness
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.space-medicine`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 60+
> **Outputs**: crew_medical
> **Critical**: No

Decompression illness (DCS) prevention and treatment addresses the risk of nitrogen bubble formation during pressure transitions, primarily before EVA when cabin pressure drops from 14.7 psi to the 4.3 psi (29.6 kPa) suit pressure. The ISS prebreath protocol involves 240 minutes of 100% oxygen breathing — including 50 minutes of exercise at 75% VO2max — to wash out dissolved nitrogen. Treatment protocols follow USN hyperbaric tables: Table 6 (18 msw, 285 min) for Type II DCS and arterial gas embolism, and Table 9 (14 msw, 35 min) for mild Type I cases.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Cabin pressure (nominal) | 14.7 psi (101.3 kPa) | Standard ISS |
| Intermediate cabin pressure | 10.2 psi (70.3 kPa) | 24 hr pre-EVA campout |
| Suit pressure (EMU) | 4.3 psi (29.6 kPa) | 100% O2 |
| Prebreath duration (total) | ~ 240 min | Mask + exercise + ISLE |
| Exercise prebreath load | 75% VO2max | 50 min on CEVIS |
| DCS incidence (ISS EVAs) | < 0.5% symptomatic | NASA medical records |
| USN Table 6 depth | 18 msw (2.8 ATA) | 285 min total |

## Prerequisites

- [Space Medicine](./space-medicine.md) — parent capability

## See Also

- [Space Medicine](./space-medicine.md) — parent capability
- [EVA](./eva.md) — procedures requiring prebreath
- [Space Suits](./space-suits.md) — EMU pressure garment
