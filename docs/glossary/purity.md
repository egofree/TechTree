# Purity

> **Type**: noun | **Tier**: critical | **Domains**: silicon, chemistry

Distill from reaction mixture (PH₃ bp -87.7°C). Dilute in H₂ or N₂ to ppm-level concentrations for semiconductor use. Use commercially-supplied cylinders with 100-1000 ppm PH₃ in H₂ (dramatically safer than handling pure phosphine). In silicon: solar grade requires 5-7N, electronic grade requires 9-11N purity.

## Context in the Tech Tree

Purity — the degree to which a substance is free of contaminants — is a defining requirement that escalates dramatically through the technology chain. In [Silicon Purification](../silicon/purification.md), purity specifications span four orders of magnitude: metallurgical-grade silicon is 98-99% pure, solar-grade is 99.999-99.99999% (5-7N), and electronic-grade is 99.999999999%+ (11N). In [Hydrogen & Silane Production](../chemistry/hydrogen-silane.md), hydrogen for semiconductor processing must reach 5N+ (99.999%) purity. Even trace metallic impurities at parts-per-billion levels can destroy semiconductor device performance.

## Technical Details

Purity requirements differ radically by application. MG-Si at 98.5% is perfectly adequate for aluminum alloying, where silicon is a minor additive. But the same material, when used as feedstock for semiconductor silicon, requires extensive purification because electrically active impurities (boron, phosphorus, iron, copper) at concentrations as low as 10¹⁰ atoms/cm³ shift resistivity and create recombination centers that destroy carrier lifetime in solar cells and transistors.

The purity cascade in silicon production illustrates the bootstrapping challenge: 98% MG-Si → 99.9999% solar grade (directional solidification or lower-purity Siemens) → 99.999999999% electronic grade (high-purity Siemens + CZ or FZ crystal growth). Each purity level enables the next technology tier but requires its own purification infrastructure.

For hazardous gases like phosphine (PH₃), purity is handled by dilution: 100-1000 ppm PH₃ in H₂ is dramatically safer than pure phosphine (which is pyrophoric and extremely toxic at 50 ppm TLV). The dilute mixture provides the dopant atoms needed for semiconductor processing while keeping the concentration below immediately dangerous levels.

## Related Terms

- [Purification](./purification.md) — the processes that achieve target purity levels
- [Contamination](./contamination.md) — impurities that degrade purity
- [Quality Testing](./quality-testing.md) — verification of purity specifications

## Appears In

- [Silicon Purification](../silicon/purification.md)
- [Hydrogen & Silane Production](../chemistry/hydrogen-silane.md)
