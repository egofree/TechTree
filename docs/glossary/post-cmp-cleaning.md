# Post-CMP Cleaning

> **Type**: process | **Tier**: critical | **Domains**: silicon, vlsi-scaling

After chemical-mechanical polishing (CMP), the wafer surface is contaminated with slurry particles and metal ions that must be completely removed before further processing. The cleaning sequence combines PVA brush scrubbing with dilute NH₄OH, megasonic cleaning (0.8-1.6 MHz), and Marangoni drying to produce a particle-free, water-mark-free surface.

## Context in the Tech Tree

Post-CMP cleaning is a critical step in semiconductor wafer processing within [Silicon Wafer Production](../silicon/wafering.md) and [Advanced Processes](../vlsi-scaling/advanced-processes.md). CMP produces a planar surface but leaves behind abrasive particles (silica or alumina from the slurry), pad debris, and dissolved metal contaminants. If not removed, these particles cause killer defects in subsequent lithography and etching steps — a single sub-micron particle can short-circuit transistor gates or break metal interconnect lines.

## Technical Details

The standard post-CMP cleaning sequence has three stages. First, PVA (polyvinyl alcohol) brush scrubbing with dilute ammonium hydroxide (1-2% NH₄OH) at 20-40°C physically removes particles while the alkaline pH prevents particle re-adhesion by maintaining zeta potential repulsion. Second, megasonic cleaning applies 0.8-1.6 MHz acoustic energy in deionized water, creating cavitation bubbles that dislodge sub-micron particles from the surface — ultrasonic frequencies (20-40 kHz) are avoided because they can damage delicate circuit features. Third, Marangoni drying uses isopropanol vapor that condenses on the wafer surface, creating a surface tension gradient that pulls water off the surface without leaving residues or water marks.

The process must be validated by particle counting (laser surface scanning) — specification is typically <50 particles per wafer at ≥0.12 μm size for advanced nodes. Metal contamination is measured by TXRF (total reflection X-ray fluorescence) with limits typically <10¹⁰ atoms/cm² for critical metals (Fe, Cu, Ni).

## Related Terms

- [Purity](./purity.md) — the cleanliness standard that post-CMP cleaning must achieve
- [Contamination](./contamination.md) — the particles and metals that post-CMP cleaning removes
- [Procedure](./procedure.md) — standardized cleaning protocols

## Appears In

- [Silicon Wafer Production](../silicon/wafering.md)
- [Advanced Processes](../vlsi-scaling/advanced-processes.md)
