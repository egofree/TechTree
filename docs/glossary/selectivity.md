# Selectivity

> **Type**: material | **Tier**: critical | **Domains**: chemistry, photolithography, vlsi-scaling

The ratio of etch rate of the target material to the etch rate of the mask or underlying layer during etching processes. High selectivity ensures the desired material is removed while protecting everything else.

## Context in the Tech Tree

Selectivity is critical in [Fab Processes](../photolithography/fab-processes.md) where patterned layers must be etched without damaging underlying structures. In [Dopant & Etch Gases](../chemistry/dopant-etch-gases.md), gas chemistry determines selectivity ratios. In [Advanced Processes](../vlsi-scaling/advanced-processes.md), atomic layer deposition and etching achieve near-perfect selectivity through self-limiting surface reactions.

## Technical Details

Critical selectivity values: SiO₂-to-photoresist selectivity 3-6:1 in fluorocarbon plasma (resist erodes, limiting etch depth). Si-to-SiO₂ selectivity 10-50:1 in fluorine-based plasma. Si₃N₄-to-SiO₂ selectivity 3-10:1 in hot phosphoric acid (wet etch). Metal-to-resist selectivity 2-5:1 in chlorine-based plasma.

Wet etching typically offers higher selectivity but is isotropic (etches equally in all directions), undercutting mask edges. Dry (plasma) etching offers directional (anisotropic) profiles but lower selectivity. The etch engineer must balance selectivity, directionality, and throughput.

In chemical separations, selectivity also refers to the ability of a solvent, catalyst, or membrane to preferentially dissolve, react with, or pass one component over another — for example, extracting gold selectively from a solution containing copper and iron.

## Related Terms

- [End-Point Detection](./end-point-detection.md) — knowing when to stop etching
- [Post-CMP Cleaning](./post-cmp-cleaning.md) — cleaning after planarization
- [Hydrofluoric Acid (HF)](./hydrofluoric-acid-hf.md) — selective SiO₂ etchant
- [Applications](./applications.md) — etching applications

## Appears In

- [Dopant & Etch Gases](../chemistry/dopant-etch-gases.md)
- [Fab Processes](../photolithography/fab-processes.md)
- [Advanced Processes](../vlsi-scaling/advanced-processes.md)
