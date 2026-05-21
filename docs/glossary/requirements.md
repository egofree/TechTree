# Requirements

> **Type**: noun | **Tier**: critical | **Domains**: health, silicon, energy, chemistry

Water must have low turbidity (<1 NTU) for UV light to penetrate effectively. Pre-filtration is mandatory. Low-pressure mercury vapor lamps produce UV-C at 254 nm. Lamp life: 8,000-12,000 hours. Dose: 30-40 mJ/cm² for most pathogens. No residual disinfectant remains in treated water.

## Context in the Tech Tree

Requirements define the minimum acceptable specifications for materials, processes, and products. They are the contract between design intent and practical execution. In [Water Treatment](../health/water-treatment.md), requirements specify turbidity limits, UV dose, and contact time for effective disinfection. In [Silicon Purification](../silicon/purification.md), purity requirements define acceptable impurity levels by application (5-7N for solar, 9-11N for electronic). In [Energy Storage](../energy/storage.md), battery room requirements specify floor loading, temperature range, ventilation rates, and acid-resistant flooring.

## Technical Details

Well-specified requirements share key attributes: they are measurable (with a clear test method), achievable (with available technology and resources), and relevant (tied to a functional need). The UV water treatment requirements illustrate this: turbidity <1 NTU is measurable with a nephelometer, achievable with standard sand filtration, and necessary because suspended particles scatter UV light and shield microorganisms from the germicidal dose.

In semiconductor silicon, the purity requirements cascade by application: solar-grade silicon tolerates metallic impurities up to 1 ppm because recombination centers at this concentration reduce solar cell efficiency by only a few percent; electronic-grade silicon requires <1 ppb because the same impurities at ppm levels would short-circuit transistor junctions. Boron and phosphorus limits are especially stringent (<0.1 ppb for electronic grade) because these elements are electrically active at concentrations far below metals — one boron atom per 10¹⁰ silicon atoms measurably shifts resistivity.

Battery room requirements combine structural (floor loading 500-1500 kg/m²), environmental (20-25°C temperature, forced ventilation for hydrogen removal), and safety (acid-resistant flooring, no open flames) specifications. Each exists because of a specific failure mode: inadequate floor loading causes collapse, high temperature halves battery life, and accumulated hydrogen explodes.

## Related Terms

- [Performance](./performance.md) — the capability that requirements define
- [Quality Testing](./quality-testing.md) — verification that requirements are met
- [Purity](./purity.md) — a common requirement in semiconductor and pharmaceutical contexts

## Appears In

- [Water Treatment](../health/water-treatment.md)
- [Silicon Purification](../silicon/purification.md)
- [Energy Storage](../energy/storage.md)
