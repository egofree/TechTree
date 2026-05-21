# Purification

> **Type**: process | **Tier**: critical | **Domains**: silicon, chemistry, health

Pass through palladium membrane (Pd tube heated to 300-400°C — only H₂ diffuses through Pd lattice, all other gases excluded). Or catalytic recombination (remove O₂ traces by reacting with H₂ over platinum catalyst → water, remove water with desiccant). Achieve 99.999%+ purity.

## Context in the Tech Tree

Purification — removing impurities to meet specification — is a rate-limiting step in many technology chains. In [Hydrogen & Silane Production](../chemistry/hydrogen-silane.md), hydrogen must reach 99.999%+ purity for semiconductor use, achieved through palladium membrane diffusion or catalytic recombination. In [Silicon Purification](../silicon/purification.md), metallurgical-grade silicon (98-99% Si) is purified to 9N-11N (99.999999999%) through chlorosilane distillation and CVD deposition — a multi-step process where each stage removes specific impurities. In [Pharmacology](../health/pharmacology.md), drug purification by recrystallization removes biologically active contaminants that could cause adverse effects.

## Technical Details

Purification methods exploit differences in physical or chemical properties between the target substance and impurities. Distillation separates by boiling point — the Siemens process uses fractional distillation of chlorosilanes (SiHCl₃ at 31.8°C, SiCl₄ at 57.6°C, BCl₃ at 12.5°C) with columns up to 30 m tall and reflux ratios exceeding 50:1 to achieve the demanding separations required for electronic-grade silicon.

Palladium membrane purification exploits a unique property: hydrogen atoms dissolve into the palladium metal lattice, diffuse through it, and desorb on the far side, while all other gases are excluded. The membrane (a Pd or Pd-alloy tube heated to 300-400°C) produces hydrogen of exceptional purity — limited only by the absence of defects in the membrane. The process is simple but expensive (palladium is a precious metal) and the membranes are fragile.

Pressure Swing Adsorption (PSA) is an alternative for bulk hydrogen purification: multiple adsorber beds packed with molecular sieves, activated carbon, and silica gel cycle through adsorption, depressurization, purge, and repressurization to produce 99.99%+ pure hydrogen at industrial scale.

Recrystallization, the workhorse of pharmaceutical purification, relies on differential solubility: dissolve crude material in hot solvent, cool slowly, and collect the purified crystals that form first while impurities remain in solution.

## Related Terms

- [Purity](./purity.md) — the quantitative measure of purification success
- [Filtration](./filtration.md) — physical separation of solids from liquids
- [Distillation](./evaporation.md) — thermal purification by boiling point difference

## Appears In

- [Hydrogen & Silane Production](../chemistry/hydrogen-silane.md)
- [Silicon Purification](../silicon/purification.md)
- [Pharmacology](../health/pharmacology.md)
