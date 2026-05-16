# Phase 8: Photolithography, Cleanrooms &amp; Integrated Circuits

**Timeline**: Years 40–70  
**Goal**: Patterned devices and early integrated circuits. This is where complexity explodes.  
**Dependencies**: [Phase 3](phase-03-machine-tools.md) (stages, aligners), [Phase 5](phase-05-chemistry.md) (resists, etchants, gases), [Phase 6](phase-06-vacuum-optics.md) (vacuum, optics), [Phase 7](phase-07-silicon.md) (wafers, basic processes)
Specialty Gases, Consumables & Packaging ([Side Quest 6](../side-quests/sq-06-gases-packaging-testing.md)) — the fab cannot operate without ultra-pure gases, cleanroom consumables, and packaging/test infrastructure

## Objectives

- Build progressively cleaner environments for fabrication
- Develop photoresist chemistry and application methods
- Create mask-making and lithography exposure tools
- Implement core fab processes (etch, deposition, doping, metallization)
- Produce basic integrated circuits using the planar process

## Key Technologies

### Cleanrooms
Contamination is the enemy of yield. Even microscopic particles destroy chips.

- **Level 1**: Gloveboxes and clean benches — simple filtered enclosures
- **Level 2**: Laminar flow cleanrooms — HEPA-filtered air, positive pressure
- **Level 3**: Full protocol cleanrooms — gowning, airlocks, sticky mats, ultra-pure water
- **Ultra-pure water (UPW)**: Multi-stage filtration, deionization, distillation
  - Resistivity >18 MΩ·cm target
  - Removes particles, ions, organics, bacteria

### Photoresists
- **Early/simple resists**: Bitumen (bitumen of Judea — hardens under UV), dichromated gelatin
- **Modern-type resists**: Novolac resin + diazonaphthoquinone (DNQ) sensitizer
  - Requires organic chemistry capability (novolac = phenol + formaldehyde resin)
  - Positive-tone (exposed regions dissolve) or negative-tone
- **Application**: Spin coating for uniform thin films
- **Development**: Aqueous base developer (TMAH or NaOH solution)

### Polymer Packaging Materials
- **Epoxy encapsulation**: Two-part epoxy for die attach and hermetic sealing — see [SQ 14](../side-quests/sq-14-polymers-composites.md) and [SQ 06](sq-06-gases-packaging-testing.md)
- **Plastic substrates and lead frames**: Molded plastic packages for integrated circuits
- **Phenolic laminate (FR-4)**: PCB substrate material from phenolic or epoxy resin impregnated glass fabric — see [SQ 14](../side-quests/sq-14-polymers-composites.md)
- **Photoresist dependency**: Novolac resin (phenol + formaldehyde condensation polymer) production path documented in [SQ 14](../side-quests/sq-14-polymers-composites.md), with monomer feedstocks from [SQ 12](sq-12-petrochemicals.md)

### Mask Making
- **Pattern generation**: Large-scale drawings → optical reduction onto photosensitive plates
- **Mask substrates**: Glass (or fused silica for UV transmission) + chrome or emulsion layer
- **Pattern transfer**: Photoreduction using precision optics
- **Alignment marks**: For multi-layer registration

### Lithography Tools
- **Contact/proximity printing**: Mask touches (or nearly touches) wafer → UV exposure
  - Simple but damages mask and wafer
- **Projection printing**: Lens projects mask image onto wafer
  - Requires good optics (from Phase 6)
- **Exposure sources**: Mercury arc lamps in quartz envelopes (g, h, i-line UV)
- **Precision stages**: From machine shop — micrometer-precision X-Y-θ stages for alignment
- **Alignment microscopes**: For overlay registration between layers

### Core Fab Processes

#### Thermal Oxidation
- Grow SiO₂ on silicon wafer in high-temperature furnace (900-1200°C)
- Dry oxidation: Si + O₂ → SiO₂ (slower, denser)
- Wet oxidation: Si + H₂O → SiO₂ (faster, used for thick layers)
- Oxide serves as: insulator, mask for doping, gate dielectric

#### Etching
- **Wet etching**: HF for SiO₂, KOH or TMAH for anisotropic Si etching, H₃PO₄ for Si₃N₄
- **Dry/plasma etching** (later): Reactive ion etching (RIE) with fluorine or chlorine plasmas
  - Better pattern fidelity, anisotropic profiles

#### Deposition
- **Chemical Vapor Deposition (CVD)**: Gas-phase reaction deposits thin films
  - Poly-Si: SiH₄ decomposition
  - SiO₂: SiH₄ + O₂ or TEOS decomposition
  - Si₃N₄: SiH₄ + NH₃
  - Requires: gas handling, temperature control, vacuum/flow control
- **Physical Vapor Deposition (PVD)**: Sputtering, evaporation (from Phase 7)
- **Epitaxy**: Growing single-crystal layer on single-crystal substrate

#### Doping
- **Diffusion**: Expose wafer to dopant source at high temperature
  - n-type: phosphorus (POCl₃ gas, or solid P₂O₅)
  - p-type: boron (BBr₃ gas, or solid B₂O₃)
  - Dopant atoms diffuse into silicon from surface
- **Ion implantation** (later, more precise): Accelerate dopant ions into wafer
  - Requires: high-voltage accelerator, vacuum, mass separator (magnets), beam scanning

#### Metallization
- Aluminum (or later copper) interconnects
- Vacuum evaporation or sputtering of metal
- Photolithographic patterning of metal lines
- Multiple metal layers with inter-layer dielectrics (later)

### Planar Process &amp; Integration
- The fundamental IC manufacturing method: sequential layers of patterned oxide, doped regions, and metal on a flat silicon surface
- **Start simple**: Single-layer metal, large features (10+ μm), few mask layers
- **Progress to**: Multiple layers, smaller features, more complex circuits
- **Early targets**: Simple logic gates, flip-flops, small counters (SSI → MSI)

## Enables (Downstream)

| Output | Used By |
|--------|---------|
| Working ICs | Phase 9 (complexity scaling) |
| Lithography capability | Phase 9 (finer features) |
| Cleanroom protocols | Phase 9 (yield improvement) |
| Fab process knowledge | Phase 9 (new materials, structures) |
| Early computers/controllers | Design automation, process control, testing |

## Practical Bottlenecks

- **Overlay registration**: Aligning multiple mask layers to sub-micron accuracy
- **Defect density**: Single particles can kill entire chips — cleanrooms must improve continuously
- **Photoresist chemistry**: Requires sophisticated organic chemistry
- **Yield**: Expect very low yields initially — iteration is essential
- **Process integration**: Making all steps (litho, etch, deposit, dope, metal) work together consistently

## Safety Concerns

- HF acid for etching: Full safety protocols, calcium gluconate on-site
- Silane (SiH₄) for CVD: Pyrophoric — auto-ignites in air
- Arsine, phosphine (dopant gases): Extremely toxic — ppb-level lethal
- High-temperature furnaces: Burn hazards
- Vacuum systems: Implosion risk

## Side Quest Dependencies

- **Specialty Gases, Consumables & Packaging** ([SQ 6](../side-quests/sq-06-gases-packaging-testing.md)) — THE critical side quest dependency. Photoresist solvents, dopant gases (PH₃, AsH₃, B₂H₆), etch gases (CF₄, SF₆, Cl₂), CVD precursors (SiH₄, TEOS), cleanroom consumables (garments, wipes, gloves), die packaging, and wafer testing all depend on this supply chain. This is the one side quest that is a hard blocker, not merely a supporting track.
- **[SQ 14: Polymers & Composites](../side-quests/sq-14-polymers-composites.md)** — photoresist binders (novolac), packaging materials (epoxy, FR-4), cleanroom consumables

[← Phase 7](phase-07-silicon.md) | [Overview](overview.md) | [Phase 9: VLSI →](phase-09-scaling.md)
