# Core Fab Processes

> **Node ID**: photolithography.fab-processes
> **Domain**: [Photolithography & IC Fabrication](./)
> **Dependencies**: `chemistry.dopant-etch-gases`, `gas-handling.vacuum`
> **Enables**: `chemistry.packaging-testing`, `vlsi-scaling.advanced-processes`, `vlsi-scaling.continuous-scaling`
> **Timeline**: Years 40-70
> **Outputs**: fab_processes, early_ics, msi, patterned_oxide, doped_regions, metal_interconnects

### Core Fab Processes

#### Thermal Oxidation
- Grow SiO₂ on silicon wafer in high-temperature furnace (900-1200°C)
- Dry oxidation: Si + O₂ → SiO₂ (slower, denser)
- Wet oxidation: Si + H₂O → SiO₂ (faster, used for thick layers)
- Oxide serves as: insulator, mask for doping, gate dielectric

**Deal-Grove oxidation model** (predicts oxide thickness as a function of time and temperature):
- Linear-parabolic rate equation: x² + Ax = B(t + τ), where x = oxide thickness, t = time, A and B are temperature-dependent rate constants, τ is the time offset accounting for initial oxide.
- **Linear regime** (thin oxide, surface-reaction limited): x ≈ (B/A)·t. B/A is the linear rate constant.
- **Parabolic regime** (thick oxide, diffusion limited): x ≈ √(B·t). B is the parabolic rate constant.
- **Typical growth rates at 1000°C**:
  - Dry O₂: ~2 nm/min (linear regime), slows dramatically in parabolic regime. 100 nm gate oxide takes ~2 hours. Dense, high-quality oxide (breakdown >10 MV/cm).
  - Wet O₂ (steam): ~10 nm/min. 500 nm field oxide takes ~1 hour. Contains more OH bonds, slightly lower quality, but acceptable for masking and insulation.
- **Furnace design**: Horizontal or vertical quartz tube furnace, 3-zone resistive heating (±1°C uniformity over 150 mm zone). O₂ or H₂O (bubbler at 95-98°C) flows through tube at 1-10 L/min. Boat holds 25-200 wafers. Push/pull rate <5 cm/min to avoid thermal stress (warp).

**Oxide uses and target thicknesses**:
- Gate oxide: 5-100 nm (dry O₂, highest quality)
- Field oxide (isolation): 300-1000 nm (wet O₂)
- Masking oxide (for ion implant or diffusion): 50-200 nm (dry or wet)
- Passivation: 500-1000 nm (CVD SiO₂ or SiNₓ, not thermal)

#### Etching
- **Wet etching**: HF for SiO₂, KOH or TMAH for anisotropic Si etching, H₃PO₄ for Si₃N₄
- **Dry/plasma etching** (later): Reactive ion etching (RIE) with fluorine or chlorine plasmas
  - Better pattern fidelity, anisotropic profiles

**Etch rates and selectivities** (typical values at process temperature):
| Material | Etchant | Rate | Selectivity vs. photoresist | Notes |
|---|---|---|---|---|
| SiO₂ | Buffered HF (BHF 7:1) | 70-100 nm/min | ~5:1 (SiO₂:PR) | Isotropic, controlled etch |
| SiO₂ | Concentrated HF (49%) | 1-2 μm/min | ~1:1 | Fast, aggressive — hard to control |
| Si | KOH (30%, 80°C) | ~1.1 μm/min (100) | ~50:1 (Si:SiO₂) | Anisotropic — stops on {111} planes |
| Si | TMAH (25%, 80°C) | ~0.6 μm/min | ~20:1 (Si:SiO₂) | CMOS-compatible (no alkali metals) |
| Si₃N₄ | H₃PO₄ (85%, 155°C) | ~5-10 nm/min | ~10:1 (Si₃N₄:SiO₂) | Hot phosphoric acid — reflux system needed |
| Al | H₃PO₄:CH₃COOH:HNO₃ (16:3:1, 50°C) | ~0.5-1.0 μm/min | ~5:1 (Al:PR) | Standard Al wet etch |
| Poly-Si | CF₄/O₂ plasma (RIE) | ~50-100 nm/min | ~5:1 (poly-Si:SiO₂) | Anisotropic with sidewall passivation |
| Si | SF₆ or CF₄ plasma (RIE) | ~100-500 nm/min | Variable | Selectivity depends on chemistry and bias |

#### Deposition
- **Chemical Vapor Deposition (CVD)**: Gas-phase reaction deposits thin films
  - Poly-Si: SiH₄ decomposition
  - SiO₂: SiH₄ + O₂ or TEOS decomposition
  - Si₃N₄: SiH₄ + NH₃
  - Requires: gas handling, temperature control, vacuum/flow control
- **Physical Vapor Deposition (PVD)**: Sputtering, evaporation (from the Silicon stage)
- **Epitaxy**: Growing single-crystal layer on single-crystal substrate

**CVD equipment types**:
| Type | Pressure | Temperature | Deposition rate | Uniformity | Notes |
|---|---|---|---|---|---|
| APCVD (Atmospheric Pressure) | 760 Torr | 350-500°C | 10-100 nm/min | ±5-10% | Simple, fast, high throughput. Poor step coverage. Used for SiO₂ (TEOS or SiH₄+O₂), doped oxides (BSG, PSG). Belt or conveyor furnace. |
| LPCVD (Low Pressure) | 0.1-1 Torr | 550-900°C | 2-10 nm/min | ±2-5% | Excellent uniformity and conformality. Hot-wall batch process (50-200 wafers). Used for poly-Si (SiH₄ at 620°C), Si₃N₄ (SiH₂Cl₂+NH₃ at 750-850°C), undoped SiO₂ (SiH₄+O₂ at 450°C). Slow but high quality. |
| PECVD (Plasma-Enhanced) | 0.5-5 Torr | 200-400°C | 5-50 nm/min | ±3-7% | Plasma provides reaction energy → low temperature compatible with metallized wafers. Used for SiNₓ passivation (SiH₄+NH₃+N₂ at 300-400°C), SiO₂ interlayer dielectric. Parallel plate reactor, RF (13.56 MHz) or HF (100-400 kHz) excitation. Slightly higher hydrogen content in films. |

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

### Process Metrology
Every process step must be measured. "If you can't measure it, you can't control it."

- **Ellipsometry** (film thickness): Monochromatic or spectroscopic light (632.8 nm HeNe laser, or broad spectrum 250-1000 nm) reflects off the thin film surface at a known angle (70-75°). Measures change in polarization (Ψ, Δ) upon reflection. Fits to optical model (Cauchy or Sellmeier dispersion) to extract film thickness and refractive index. Accuracy: ±0.5 nm for oxides, ±2 nm for thicker films. Measures: SiO₂, SiNₓ, photoresist, poly-Si, metals (with appropriate model). Non-destructive, fast (~1 sec per site). Maps wafer uniformity (49-point or 121-point contour map).
- **Four-point probe** (sheet resistance): Four collinear tungsten probes (1 mm spacing) contact the wafer surface. Outer two probes pass constant current I (1 μA-100 mA), inner two measure voltage V. Sheet resistance Rs = (π/ln 2)·(V/I) ≈ 4.532·(V/I) Ω/sq. Measures doped layers (diffused or implanted), metal films, poly-Si. Corrects for wafer diameter with geometric correction factors. Accuracy ±1%. For metal film thickness: t = ρ/Rs where ρ is bulk resistivity.
- **Dektak / profilometer** (step height): Diamond-tipped stylus (12.5-50 μm radius, 1-15 mg force) scans across a step in the film surface (e.g., where resist or oxide was etched away). Measures vertical displacement with sub-nm resolution (typically ±1-5 nm over 1 μm step range). Used for: etch depth verification, film thickness (after patterning a step), planarization uniformity. Trade-off: higher stylus force = better surface contact but risks scratching soft films (photoresist, aluminum). Also measures surface roughness (Ra, Rq).
- **Optical microscope inspection**: Brightfield and darkfield illumination. Detects pattern defects (missing features, bridges, particles), alignment errors, etch completeness. Magnification 50×-1000×. Essential for yield troubleshooting. Operators visually inspect sample wafers from each lot.
- **Particle counting**: Laser scattering particle counters measure airborne particles (in cleanroom monitoring) or on wafer surfaces (bare wafer or patterned wafer inspection). Defect density (particles/cm² per process step) directly predicts yield: Yield = (1 - D·A)ⁿ where D = defect density, A = die area, n = process steps.

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

### Hazards & Safety

- **Hydrofluoric acid (HF)** — CRITICAL: HF at 5-49 % concentration causes severe, deep-tissue burns that may not be immediately painful — pain onset can be delayed hours while fluoride ions destroy bone and tissue. **Always have calcium gluconate gel (2.5 %) immediately available at every HF station.** Apply to any skin contact immediately, then seek emergency medical care. Wear heavy-duty acid gloves (Neoprene or thick nitrile), face shield, acid apron, and work only in a fume hood. HF burns can be fatal at body surface area exposures as small as 2-5 %.
- **POCl₃ doping**: Phosphorus oxychloride reacts violently with moisture to produce phosphoric acid and HCl gas (corrosive, toxic). Use in enclosed, gas-cabinet-fed furnace tubes with toxic-gas monitoring (HCl detector). Exhaust gas scrubbers (caustic wet scrubber) mandatory. Leak protocol: evacuate area, wear self-contained breathing apparatus (SCBA).
- **Forming gas (N₂/H₂ 90/10)**: Hydrogen concentration (10 %) is below the lower explosive limit (LEL = 4 %) in this mixture, but leaks in confined spaces can concentrate H₂ into the explosive range (4-75 % in air). Use hydrogen gas detectors in furnace areas; ensure ventilation rates prevent accumulation. Never use forming gas near ignition sources.
- **Furnace temperatures (800-1200 °C)**: Severe burn hazard. Use heat-resistant gloves (Kevlar, rated to 1000 °C) and face shield when loading/unloading wafer boats. Quartz furnace tubes are fragile when hot — avoid thermal shock (push/pull boats slowly, <5 cm/min). Allow furnaces to cool below 200 °C before maintenance.
- **Plasma/RIE gases**: SF₆ (GWP 23,900× CO₂), CF₄ (GWP 6,630× CO₂), and NF₃ (GWP 17,200× CO₂) are potent greenhouse gases. Install point-of-use abatement (burn boxes or plasma destruct units, >99 % destruction efficiency) on all exhaust lines. NF₃ and CF₄ also produce toxic byproducts (HF, COF₂) in plasma — downstream scrubbing required.

---

*Part of the [Bootciv Tech Tree](../) • [Photolithography](./) • [All Domains](../)*
