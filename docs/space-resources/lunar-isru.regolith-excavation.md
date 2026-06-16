# Regolith Excavation

> **Node ID**: `space-resources.lunar-isru.regolith-excavation`
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`space-resources.lunar-isru`](./lunar-isru.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: lunar_oxygen
> **Critical**: No

## Overview

Lunar regolith excavation is the front-end of every ISRU process chain: loosening, collecting, and transporting the abrasive, electrostatically charged surface material that feeds oxygen, water, and metal extraction. The challenge is doing this in vacuum, at 1/6 g, against a feedstock that wears terrestrial machinery 3–10× faster than sand.

See the parent capability [Lunar ISRU](lunar-isru.md) for regolith composition, excavation targets, and integration with downstream processing.

## Process Description

1. **Site preparation**: Rovers grade and compact the dig face; dust curtains are deployed to contain electrostatic ejecta.
2. **Excavation**: A RASSOR-class dual bucket-drum excavator counter-rotates its drums to fill against its own mass, targeting 30–50 kg/h sustained feed.
3. **Conveyance**: Regolith is pneumatically or mechanically conveyed to the beneficiation/reactor hopper.
4. **Beneficiation** (where required): Magnetic separation concentrates ilmenite; sieving removes >1 cm rock fragments.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Feed rate | 30–50 kg/h |
| Excavator mass | < 100 kg |
| Regolith bulk density | 1.5–1.9 g/cm³ |
| Gravity | 1.62 m/s² (1/6 g) |
| Bearing strength | 30–70 kPa (top 10 cm) |

## Safety

Lunar dust sub-10 µm particles are a silicosis and "lunar hay fever" hazard. Excavator service requires airlock dust mitigation: electrostatic precipitators, suit-port design, and sealed bearings with magnetic-fluid or bellows seals.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md) • [Lunar ISRU](lunar-isru.md)*
