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
Contamination is the enemy of yield. A single 1 μm particle on a wafer can kill an entire chip. Cleanroom class determines minimum feature size achievable: Class 1000 (ISO 6) for >5 μm features, Class 100 (ISO 5) for 1-5 μm, Class 10 (ISO 4) for sub-micron.

**Cleanroom construction**:
- **Structure**: Enclosed room with smooth, non-shedding walls (epoxy-painted steel, aluminum, or plastic laminate). Flush surfaces, rounded corners, no horizontal surfaces that collect dust. Positive pressure (10-20 Pa above ambient) so air leaks OUT, not in. Airlock entry (personnel and materials enter through separate airlocks with interlocked doors).
- **Air filtration**: HEPA filters (99.97% efficient at 0.3 μm) in ceiling. Laminar flow (air flows in parallel streamlines from ceiling to floor perforations). 20-60 air changes per hour for Class 100. ULPA filters (99.999% at 0.12 μm) for Class 10 and below.
- **Flooring**: Vinyl or raised perforated floor panels (air return). Sticky mats at entrances (tacky surface pulls particles off shoe covers). Anti-static treatment.
- **Lighting**: Tear-drop or flush-mounted fixtures (no horizontal surfaces). UV-blocking if photoresist is light-sensitive.
- **Gowning**: Cleanroom garments (Tyvek, polyester, or polypropylene — non-linting) cover head, body, and shoes. Gloves (nitrile or latex — powder-free). Face mask. Gowning room with sticky mat and air shower.
- **Ultra-pure water (UPW) system**:
  - **Pre-treatment**: Sand filter → carbon filter → water softener
  - **RO (reverse osmosis)**: Semi-permeable membrane removes 95-99% of dissolved ions and organics. Pressure 10-60 bar.
  - **DI (deionization)**: Ion exchange resin beds remove remaining ions. Resistivity target >18 MΩ·cm.
  - **UV sterilization**: 254 nm UV lamp kills bacteria and algae.
  - **Final filtration**: 0.05-0.2 μm membrane filter removes particles.
  - **Distribution**: PVDF or PFA piping (no leaching). Continuous recirculation (no dead legs where bacteria grow).
  - **Quality testing**: Online resistivity monitoring, particle counting, TOC (total organic carbon) analysis

### Photoresists

**Bitumen resist** (simplest, historical — Niépce, 1826):
- Dissolve bitumen of Judea (natural asphalt) in lavender oil or turpentine. Coat on substrate. Expose to UV through mask (hours of exposure — very slow). Exposed areas harden (polymerize), unexposed areas dissolve in solvent. Low resolution (~100 μm+), very slow, but requires zero chemistry infrastructure.

**Dichromated gelatin** (mid-19th century):
- Mix gelatin (from animal collagen) with ammonium dichromate ((NH₄)₂Cr₂O₇, ~5-10%). Coat on substrate. UV exposure causes Cr(VI) → Cr(III) reduction, cross-linking gelatin (insoluble). Unexposed gelatin washes away in warm water. Resolution ~10-50 μm. Chromium compounds are toxic and carcinogenic — handle with care.

**Novolac + DNQ resist** (standard positive-tone photoresist, requires Phase 5 organic chemistry):
- **Novolac resin**: Phenol + formaldehyde condensation polymer (m-cresol variant for photoresist). See [SQ 14](../side-quests/sq-14-polymers-composites.md) for production. Molecular weight ~2000-5000. Dissolves in aqueous base (NaOH or TMAH).
- **DNQ sensitizer**: Diazonaphthoquinone sulfonate (from naphthol + diazotization). ~20-30% by weight in resist. Function: DNQ acts as dissolution inhibitor — unexposed resist does NOT dissolve in developer. UV exposure → DNQ undergoes Wolff rearrangement → forms indene carboxylic acid → actually ENHANCES dissolution in aqueous base. This is the positive-tone mechanism.
- **Solvent**: Ethyl lactate or propylene glycol monomethyl ether acetate (PGMEA). ~60-80% of resist formulation.
- **Spin coating**: Dispense ~2-5 ml resist on wafer center. Spin at 1000-6000 RPM for 30-60 seconds. Centrifugal force spreads resist uniformly. Thickness: 0.5-3 μm (depends on viscosity and spin speed — roughly t ∝ 1/√ω). Edge bead removal (EBR): spray solvent at wafer edge while spinning to remove thick bead that forms at edge.
- **Soft bake (pre-bake)**: 90-110°C for 60-90 seconds on hot plate. Drives off solvent. Residual solvent <3%.
- **Exposure**: UV light (365 nm i-line, 405 nm h-line, or 436 nm g-line from mercury lamp). Dose: 50-200 mJ/cm². Exposed regions become soluble.
- **Post-exposure bake (PEB)**: 110-130°C for 60-90 seconds. Improves pattern definition by reducing standing wave effects.
- **Development**: Aqueous base — 2.38% TMAH (tetramethylammonium hydroxide) for 30-90 seconds with gentle agitation. TMAH preferred over NaOH (metal-ion-free developer — sodium contamination degrades MOS devices).
- **Hard bake**: 120-150°C for 60-120 seconds. Cross-links resist for etch resistance. Not always needed.

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

### Planar Process & Integration
- The fundamental IC manufacturing method: sequential layers of patterned oxide, doped regions, and metal on a flat silicon surface
- **Start simple**: Single-layer metal, large features (10+ μm), few mask layers
- **Progress to**: Multiple layers, smaller features, more complex circuits
- **Early targets**: Simple logic gates, flip-flops, small counters (SSI → MSI)

**Example: NMOS transistor fabrication flow** (7 mask layers):
1. **Starting wafer**: p-type <100> Si, 5-20 Ω·cm, cleaned (RCA)
2. **Mask 1 — Active area**: Grow 500 nm SiO₂ (wet oxidation, 1000°C, ~2 hours). Spin photoresist. Expose through Mask 1 (active areas = where transistors will be). Develop. Etch SiO₂ in buffered HF (BHF: NH₄F:HF 7:1, ~700 nm/min). Strip resist. Result: oxide islands defining transistor regions.
3. **Mask 2 — Gate oxidation**: Grow 50-100 nm gate oxide (dry oxidation, 900-1000°C, 30-60 min — thin, high-quality oxide). This is the MOST CRITICAL step — gate oxide quality determines transistor performance. Target: breakdown voltage >8 MV/cm.
4. **Mask 3 — Polysilicon gate**: Deposit 300-500 nm poly-Si by LPCVD (SiH₄ at 620°C, ~10 nm/min). Dope n+ (POCl₃ diffusion or ion implant). Spin resist, expose Mask 3, develop, dry etch poly-Si (CF₄/O₂ plasma). Strip resist. Result: polysilicon gate electrodes, self-aligned to source/drain.
5. **Source/drain implant**: Ion implant phosphorus (dose 10¹⁵/cm², 50-100 keV) or POCl₃ pre-deposition + drive-in (900°C, 30 min). Polysilicon gate acts as self-aligned mask — source/drain automatically aligned to gate edges.
6. **Mask 4 — Contact holes**: Deposit 500 nm SiO₂ (CVD). Spin resist, expose Mask 4 (contact openings over source, drain, gate). Etch oxide in BHF. Strip resist.
7. **Mask 5 — Metal**: Deposit 1 μm aluminum (evaporation or sputtering). Spin resist, expose Mask 5 (interconnect pattern). Wet etch Al (H₃PO₄:CH₃COOH:HNO₃ at 40-50°C, ~1 μm/min). Strip resist.
8. **Mask 6 — Passivation**: Deposit 1 μm SiO₂ or SiNₓ (CVD). Expose Mask 6 (bond pad openings). Etch. Strip resist.
9. **Alloy/anneal**: 400-450°C in forming gas (N₂/H₂ 90/10) for 30 min. Improves Al-Si contact, passivates dangling bonds with hydrogen.
10. **Test, dice, package, wire bond**: See [SQ 6](../side-quests/sq-06-gases-packaging-testing.md).

**Yield expectations**: First IC runs will have <1% yield. Iteration is essential. Defect density, contamination control, and process uniformity all improve with practice. A mature process might achieve 50-90% yield on simple circuits.

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
