# Core Fab Processes

> **Node ID**: `photolithography.fab-processes`
> **Domain**: [Photolithography & IC Fabrication](./)
> **Dependencies**: `specialty-gases.dopant-etch-gases`, `gas-handling.vacuum`
> **Enables**: `specialty-gases.packaging-testing`, `vlsi-scaling.advanced-processes`, `vlsi-scaling.continuous-scaling`
> **Timeline**: Years 40-70
> **Outputs**: fab_processes, early_ics, msi, patterned_oxide, doped_regions, metal_interconnects

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
- **Physical Vapor Deposition (PVD)**: Sputtering, evaporation (from the Silicon stage)
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
10. **Test, dice, package, wire bond**: See [Specialty Gases](../chemistry/packaging-testing.md).

**Yield expectations**: First IC runs will have <1% yield. Iteration is essential. Defect density, contamination control, and process uniformity all improve with practice. A mature process might achieve 50-90% yield on simple circuits.
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
