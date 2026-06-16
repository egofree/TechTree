# Water Ice Mining

> **Node ID**: `space-resources.lunar-isru.water-ice-mining`
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.lunar-isru`](./lunar-isru.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: lunar_oxygen
> **Critical**: No

## Overview

Permanently shadowed regions (PSRs) at the lunar poles trap water ice at **-240°C (33 K)**, where it is stable over geological timescales. LCROSS impact data confirmed **5–8% water by mass** in the PSR regolith of Cabeus crater. Shackleton crater (south pole) is the prime resource, pairing a permanently sunlit rim (for power) with a shadowed, ice-rich floor.

See the parent capability [Lunar ISRU](lunar-isru.md) for volatile composition, LCROSS results, and the Shackleton resource estimate.

## Process Description

1. **Descent**: A rover descends into the PSR carrying radioisotope heater units (RHUs) to stay warm at -240°C.
2. **Excavation**: Heated augers or buckets scrape icy regolith into a sealed, cold-trapped hopper.
3. **Transfer**: The sealed hopper is moved to a warmed reactor, where the ice sublimes/melts under controlled pressure.
4. **Purification**: Raw water is decontaminated (Hg, Ag removal via ion exchange) before electrolysis or crew use.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| PSR temperature | -240°C |
| Water content | 5–8% by mass (LCROSS) |
| Target crater | Shackleton (south pole) |
| Contaminants | Hg, Ag, NH₃, H₂S |
| Power source | RTG / beamed from sunlit rim |

## Safety

PSR volatiles contain **mercury and silver** — severe neurotoxins. Electrolysis of raw PSR water releases Hg vapor, so water must be purified before use. Lubricants freeze at -240°C; all mechanisms use dry-film lubrication (MoS₂) and active heating.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md) • [Lunar ISRU](lunar-isru.md)*
