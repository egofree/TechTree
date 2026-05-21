# Cleaning

> **Type**: noun | **Tier**: critical | **Domains**: animals, chemistry, gas-handling, health, machine-tools, photolithography

New and re-used vacuum components are cleaned in a two-step solvent wash. First, wash with acetone to dissolve organic residues (oils, greases, flux). Acetone is a strong organic solvent that evaporates quickly and leaves minimal residue. Second, rinse with isopropyl alcohol (IPA) to remove the acetone and any remaining water. IPA displaces water and evaporates cleanly. Blow dry with clean, oil-free nitrogen. Do not use compressed shop air (contains oil mist from the compressor).

## Context in the Tech Tree

Cleaning — removing contaminants from surfaces to meet process requirements — is a critical procedure at multiple tech-tree stages. In [Vacuum Technology](../gas-handling/vacuum.md), component cleaning determines ultimate vacuum level. In [Photoresists & Masks](../photolithography/resists-masks.md), wafer cleaning prevents defects that destroy semiconductor devices. In [Medicine](../health/medicine.md), sterilization prevents infection. In [Sericulture](../animals/sericulture.md), cleaning prevents contamination of silk. The required cleanliness level escalates from "visibly clean" to "molecularly clean" as the tech tree progresses.

## Technical Details

The standard two-step solvent wash for vacuum and semiconductor components uses acetone followed by isopropyl alcohol (IPA). Acetone dissolves organic residues — oils, greases, soldering flux, and fingerprints — and evaporates rapidly. IPA removes the acetone film and any remaining water, displacing moisture and leaving a residue-free surface. The final step is blow-drying with clean, oil-free nitrogen (never compressed shop air, which carries oil mist from the compressor).

In vacuum system preparation, cleaning directly affects outgassing rates. A fingerprint on a stainless steel surface outgasses hydrocarbons for days at vacuum, preventing the system from reaching its base pressure. Electropolished and baked stainless steel achieves outgassing rates of ~10⁻⁸ Pa·m³/s·m², while contaminated surfaces can be 100-1000× higher.

In semiconductor processing, cleaning escalates to the RCA clean sequence: SC-1 (NH₄OH:H₂O₂:H₂O removes organic and particle contamination), SC-2 (HCl:H₂O₂:H₂O removes metallic contamination), and HF dip (removes native oxide). The requirement is sub-monolayer surface cleanliness — a single particle can destroy a transistor gate.

The progression from basic solvent cleaning to RCA cleaning mirrors the tech tree's escalation from mechanical to chemical to semiconductor-grade process control.

## Related Terms

- [Construction](./construction.md) — building cleaning apparatus and facilities
- [Principle](./principle.md) — the chemical principles behind solvent cleaning
- [Applications](./applications.md) — when and where different cleaning protocols are used
- [Limitations](./limitations.md) — what cleaning cannot remove and failure modes

## Appears In

- [Vacuum Technology](../gas-handling/vacuum.md)
- [Photoresists & Masks](../photolithography/resists-masks.md)
- [Medicine](../health/medicine.md)
- [Sericulture](../animals/sericulture.md)
- [Casting](../machine-tools/casting.md)
