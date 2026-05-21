# Contamination

> **Type**: noun | **Tier**: critical | **Domains**: health, photolithography, polymers

Mixed polymer types (PE + PP + PVC in waste stream) are incompatible — even 2-5% PVC contamination in a PE recycle stream causes dark specks and degraded properties. Sorting by resin identification code (1-7) is essential. Density separation (float-sink tanks: PE/PP float in water, PVC/PET sink) is the most practical automated sorting method.

## Context in the Tech Tree

Contamination control is a threshold capability that gates progress in multiple domains. In polymer recycling, cross-contamination between resin types destroys product quality. In semiconductor fabrication, even trace metallic contamination (sodium, potassium) shifts transistor threshold voltages and kills device yield. In pharmaceutical production, microbial or particulate contamination renders drugs dangerous rather than therapeutic.

## Technical Details

In polymer processing, the resin identification codes (1-7) exist precisely because cross-contamination is so destructive. PVC contamination in a PE stream introduces chlorine that generates HCl during melt processing, corroding equipment and degrading the polymer. Density separation exploits the fact that PE (0.92-0.96 g/cm³) and PP (0.90-0.91 g/cm³) float in water while PVC (1.30-1.58 g/cm³) and PET (1.33-1.39 g/cm³) sink — a simple water bath becomes an effective sorting stage.

In photolithography, mobile ion contamination (sodium, potassium) in gate oxides shifts MOS threshold voltages unpredictably. This is why TMAH developer is preferred over NaOH — the organic tetramethylammonium cation leaves no metallic residue. Yield models show an exponential relationship: Yield = (1 - D·A)ⁿ, where defect density D must be driven to fractions of a defect per cm² per layer.

In pharmaceutical work, contamination sources include unclean equipment, environmental microbes, and heavy metals from soil or processing equipment. Sterilization of containers and workspace, combined with purity testing (colorimetric methods for heavy metals), mitigates these risks.

## Related Terms

- [Efficiency](./efficiency.md) — contamination reduces process efficiency
- [Dust Inhalation](./dust-inhalation.md) — particulate contamination as health hazard

## Appears In

- [Pharmacology](../health/pharmacology.md)
- [Resists & Masks](../photolithography/resists-masks.md)
- [Thermoplastics](../polymers/thermoplastics.md)
