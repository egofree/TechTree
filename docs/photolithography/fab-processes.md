# Core Fab Processes

> **Node ID**: photolithography.fab-processes
> **Domain**: [Photolithography & IC Fabrication](./)
> **Dependencies**: [`chemistry.dopant-etch-gases`](../chemistry/dopant-etch-gases.md), [`gas-handling.vacuum`](../gas-handling/vacuum.md)
> **Enables**: [`chemistry.packaging-testing`](../chemistry/packaging-testing.md), [`vlsi-scaling.advanced-processes`](../vlsi-scaling/advanced-processes.md), [`vlsi-scaling.continuous-scaling`](../vlsi-scaling/continuous-scaling.md)
> **Timeline**: Years 40-70
> **Outputs**: fab_processes, early_ics, msi, patterned_oxide, doped_regions, metal_interconnects

### Core Fab Processes

#### Thermal Oxidation
- Grow SiO₂ on silicon wafer in high-temperature furnace (900-1200°C)
- Dry oxidation: Si + O₂ → SiO₂ (slower, denser)
- Wet oxidation: Si + H₂O → SiO₂ (faster, used for thick layers)
- Oxide serves as: insulator, mask for doping, gate dielectric

**[Deal-Grove oxidation model](../glossary/deal-grove-oxidation-model.html)** (predicts oxide thickness as a function of time and temperature):
- Linear-parabolic rate equation: x² + Ax = B(t + τ), where x = oxide thickness, t = time, A and B are temperature-dependent rate constants, τ is the time offset accounting for initial oxide.
- **[Linear regime](../glossary/linear-regime.html)** (thin oxide, surface-reaction limited): x ≈ (B/A)·t. B/A is the linear rate constant.
- **[Parabolic regime](../glossary/parabolic-regime.html)** (thick oxide, diffusion limited): x ≈ √(B·t). B is the parabolic rate constant.
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
- **[Ion implantation](../glossary/ion-implantation.html)** (later, more precise): Accelerate dopant ions into wafer
  - Requires: high-voltage accelerator, vacuum, mass separator (magnets), beam scanning

#### Metallization
- Aluminum (or later copper) interconnects
- Vacuum evaporation or sputtering of metal
- Photolithographic patterning of metal lines
- Multiple metal layers with inter-layer dielectrics (later)

### Process Metrology
Every process step must be measured. "If you can't measure it, you can't control it."

- **[Ellipsometry](../glossary/ellipsometry.html)** (film thickness): Monochromatic or spectroscopic light (632.8 nm HeNe laser, or broad spectrum 250-1000 nm) reflects off the thin film surface at a known angle (70-75°). Measures change in polarization (Ψ, Δ) upon reflection. Fits to optical model (Cauchy or Sellmeier dispersion) to extract film thickness and refractive index. Accuracy: ±0.5 nm for oxides, ±2 nm for thicker films. Measures: SiO₂, SiNₓ, photoresist, poly-Si, metals (with appropriate model). Non-destructive, fast (~1 sec per site). Maps wafer uniformity (49-point or 121-point contour map).
- **[Four-point probe](../glossary/four-point-probe.html)** (sheet resistance): Four collinear tungsten probes (1 mm spacing) contact the wafer surface. Outer two probes pass constant current I (1 μA-100 mA), inner two measure voltage V. Sheet resistance Rs = (π/ln 2)·(V/I) ≈ 4.532·(V/I) Ω/sq. Measures doped layers (diffused or implanted), metal films, poly-Si. Corrects for wafer diameter with geometric correction factors. Accuracy ±1%. For metal film thickness: t = ρ/Rs where ρ is bulk resistivity.
- **[Dektak / profilometer](../glossary/dektak-profilometer.html)** (step height): Diamond-tipped stylus (12.5-50 μm radius, 1-15 mg force) scans across a step in the film surface (e.g., where resist or oxide was etched away). Measures vertical displacement with sub-nm resolution (typically ±1-5 nm over 1 μm step range). Used for: etch depth verification, film thickness (after patterning a step), planarization uniformity. Trade-off: higher stylus force = better surface contact but risks scratching soft films (photoresist, aluminum). Also measures surface roughness (Ra, Rq).
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
- **Forming gas (N₂/H₂ 90/10)**: The forming gas mixture contains 10 % hydrogen — above the lower explosive limit (LEL = 4 % in air). While the nitrogen diluent raises the minimum ignition energy, leaks in confined spaces can create an explosive H₂/air mixture (4-75 % in air). Use hydrogen gas detectors in furnace areas; ensure ventilation rates prevent accumulation. Never use forming gas near ignition sources.
- **Furnace temperatures (800-1200 °C)**: Severe burn hazard. Use heat-resistant gloves (Kevlar, rated to 1000 °C) and face shield when loading/unloading wafer boats. Quartz furnace tubes are fragile when hot — avoid thermal shock (push/pull boats slowly, <5 cm/min). Allow furnaces to cool below 200 °C before maintenance.
- **Plasma/RIE gases**: SF₆ (GWP 23,900× CO₂), CF₄ (GWP 6,630× CO₂), and NF₃ (GWP 17,200× CO₂) are potent greenhouse gases. Install point-of-use abatement (burn boxes or plasma destruct units, >99 % destruction efficiency) on all exhaust lines. NF₃ and CF₄ also produce toxic byproducts (HF, COF₂) in plasma — downstream scrubbing required.

### Wet Etch Processes

**Silicon dioxide etching**:
- **Buffered HF (BHF)**: NH₄F:HF 7:1 mixture. Etch rate 70-100 nm/min for thermal SiO₂. The ammonium fluoride buffers the HF concentration, maintaining a stable etch rate over time. Selectivity to photoresist ~5:1. Selectivity to silicon >100:1 (HF does not attack crystalline silicon). Temperature: room temperature (20-25°C). Used for: contact hole opens, gate oxide removal, general oxide patterning.
- **Dilute HF (DHF)**: HF:H₂O at 1:10 to 1:100. Etch rate 20-30 nm/min for 1:10 dilution. Used for: thin oxide stripping, native oxide removal, pre-deposition cleaning. Lower attack rate on photoresist than BHF.
- **Vapor HF**: HF vapor etches SiO₂ without liquid contact. Useful for stiction-sensitive MEMS structures and for etching under suspended structures where liquid cannot penetrate.

**Silicon nitride etching**:
- **Hot phosphoric acid**: H₃PO₄ at 155-180°C in a reflux system (condenser returns evaporated acid). Etch rate: 5-10 nm/min for Si₃N₄. Selectivity to SiO₂: 10:1 (phosphoric attacks nitride much faster than oxide). Selectivity to silicon: >50:1. The high temperature requires a reflux condenser to prevent acid evaporation and maintain constant concentration. Silicon nitride is used as a hard mask and as a selective etch stop because it resists most silicon and oxide etchants.

**Silicon anisotropic wet etching**:
- **KOH (potassium hydroxide)**: 30-45% KOH in water at 70-85°C. Etch rate for Si <100>: ~1.1 μm/min (at 30%, 80°C). Etch rate ratio <100>:<111> ≈ 100:1. The {111} crystal planes etch ~100× slower than {100} planes, producing precise V-grooves, pyramidal pits, and thin membranes bounded by {111} sidewalls. Alignment of mask features to the <110> flat is critical: a 1° misalignment produces significant undercut.
- **TMAH (tetramethylammonium hydroxide)**: 5-25% in water at 70-90°C. Etch rate ~0.6 μm/min at 25%, 80°C. CMOS-compatible (TMAH is an organic base — no alkali metal contamination). Selectivity to SiO₂: ~20:1 (lower than KOH's ~50:1). Smoother sidewalls than KOH but slower etch rate.

### Dry Etch Processes

**Reactive Ion Etching (RIE)**:
- **Principle**: RF plasma (typically 13.56 MHz) generates reactive species (ions, radicals) from feed gases. A DC self-bias develops on the powered electrode (cathode), accelerating positive ions into the wafer surface. This combines chemical etching (neutral radicals react with the material) with physical sputtering (ion bombardment removes material and reaction products). The result: anisotropic etching (vertical sidewalls) because ions bombard vertically while chemical etching would be isotropic.
- **Operating parameters**: Pressure 10-100 mTorr. RF power 50-500 W. Gas flow 10-200 sccm. Wafer temperature: 20-80°C (cooled by helium backside cooling for uniform temperature). Lower pressure → more anisotropic (longer mean free path, more directional ions). Higher power → faster etch but less selective (more physical sputtering damages mask and select materials).

**Silicon dioxide RIE**:
- **Chemistry**: CF₄/O₂ or CHF₃/CF₄. Fluorocarbon plasma generates CFₓ radicals that etch SiO₂ by forming volatile SiF₄. Oxygen addition controls fluorine concentration (O₂ reacts with free F to form CO, CO₂, and COF₂, moderating the etch). CHF₃ provides more polymer deposition (carbon-rich), which protects sidewalls and improves anisotropy.
- **Etch rate**: 50-200 nm/min depending on power, pressure, and gas ratio.
- **Selectivity to resist**: 5-10:1 (resist erodes during etch). Selectivity to silicon: 10-20:1 (fluorocarbon polymer passivates silicon surface). These selectivities determine how much resist is needed and how aggressively underlying silicon is attacked at the etch endpoint.

**Deep Reactive Ion Etching (DRIE) — Bosch process**:
- **Principle**: Alternating cycles of isotropic etching (SF₈ plasma) and polymer passivation (C₄F₈ plasma). Each etch cycle removes silicon isotropically for a few seconds. Each passivation cycle deposits a thin fluorocarbon polymer on all surfaces. In the next etch cycle, directional ion bombardment clears the polymer from horizontal surfaces, allowing etching to continue vertically while the polymer on sidewalls protects them.
- **Result**: Very deep, high-aspect-ratio features. Aspect ratios >20:1 achievable (e.g., 100 μm deep trenches that are 5 μm wide). Etch rate: 2-5 μm/min for silicon. Sidewall scalloping: each etch-passivation cycle creates a small notch on the sidewall, producing a characteristic scalloped texture with 50-200 nm amplitude.
- **Applications**: MEMS devices (accelerometers, gyroscopes, microfluidic channels), through-silicon vias (TSVs for 3D IC stacking), silicon trench isolation, deep trench capacitors.

### Deposition Processes

**Thermal oxidation in detail**:
- **Dry oxidation**: Si + O₂ → SiO₂ at 900-1200°C in pure O₂ atmosphere. Growth rate: ~1-5 nm/min in the linear regime, slowing as oxide thickens (parabolic regime). Produces the highest-quality oxide: dense, uniform, low defect density, breakdown field >10 MV/cm. Used exclusively for gate oxides (where quality is paramount) and thin screening oxides.
- **Wet oxidation**: Si + 2H₂O → SiO₂ at 900-1200°C. Water vapor introduced by passing O₂ through a heated water bubbler (95-98°C) or by burning H₂ and O₂ directly in the furnace tube (torch ignition, producing H₂O in situ). Growth rate: 5-25 nm/min, roughly 5-10× faster than dry oxidation. The resulting oxide contains more OH bonds (water-related defects), making it slightly lower quality but adequate for field oxide, masking oxide, and passivation layers.

**LPCVD (Low Pressure CVD)**:
- **Operating conditions**: 25-250 Pa (0.2-2 Torr), 550-900°C. Hot-wall reactor: resistance-heated quartz tube, wafers stand vertically in a slotted quartz boat. The low pressure increases mean free path, improving gas-phase uniformity across all wafers in the batch (50-200 wafers per run).
- **Poly-Si**: SiH₄ at 620°C. Deposition rate ~10 nm/min. Amorphous below ~580°C, polycrystalline above. Grain size: 50-200 nm. Used for gate electrodes, structural layers in MEMS, and interconnects.
- **Si₃N₄**: SiH₂Cl₂ + NH₃ at 750-850°C. Deposition rate ~3-5 nm/min. Stoichiometric silicon nitride is an excellent diffusion barrier (blocks Na, K, water) and oxidation mask. Used for LOCOS (local oxidation of silicon) isolation, passivation, and etch masks.
- **SiO₂**: SiH₄ + O₂ at 450°C, or TEOS (tetraethyl orthosilicate) at 650-750°C. TEOS provides better step coverage and gap fill than silane-based oxide. Used for interlayer dielectric (ILD) between metal layers.

**PECVD (Plasma-Enhanced CVD)**:
- **Operating conditions**: 100-1000 Pa (1-10 Torr), 200-400°C. RF plasma (13.56 MHz or 2.45 GHz microwave) provides reaction energy, allowing deposition at temperatures low enough to avoid damaging existing metal interconnects (aluminum melts at 660°C).
- **SiNₓ**: SiH₄ + NH₃ + N₂ at 300-400°C. Deposition rate 5-50 nm/min. Hydrogen content: 15-30 at% (more than LPCVD nitride). Used for final passivation layer and anti-reflection coating on solar cells.
- **SiO₂**: SiH₄ + N₂O at 300-400°C. Lower quality than thermal or LPCVD oxide (more hydrogen, lower density) but can be deposited on top of metal layers without melting them.

**Metallization detail**:
- **Sputtering**: Ar⁺ ions at 3-5 mTorr, accelerated by 100-500 W RF (for insulating targets) or DC (for conducting targets). Sputter yield: 0.5-3 atoms per incident ion depending on target material. Deposition rate: 5-30 nm/min. Film properties depend on Ar pressure, power, and substrate temperature. Step coverage: moderate (better than evaporation, worse than CVD). Alloys (Al-Si 1%, Al-Cu 0.5%) sputtered from alloy targets.
- **Evaporation**: Thermal evaporation (resistive heating of W or Mo boat) or electron-beam evaporation (focused e-beam heats source material in water-cooled copper crucible). Chamber pressure: 10⁻⁶ Torr. Atoms travel in straight lines from source to substrate (line-of-sight deposition). Deposition rate: 5-100 nm/min. Film purity depends on source purity and vacuum quality. Poor step coverage (shadowing at step edges) limits use for advanced multi-level metallization.

### Chemical-Mechanical Planarization (CMP)

**Process principle**: Simultaneous chemical and mechanical removal of material to create a flat surface. The wafer is pressed face-down against a rotating polishing pad while slurry flows between wafer and pad. The slurry chemistry attacks the material; the mechanical action of the pad and slurry particles removes the reaction products.

**Oxide CMP**:
- **Slurry**: Colloidal silica (SiO₂ particles, 20-100 nm diameter) suspended in KOH or ammonium hydroxide solution, pH 10-11. The alkaline slurry softens the SiO₂ surface by forming a hydrated layer; the silica particles mechanically abrade this softened layer. Removal rate: 100-300 nm/min. Downforce: 2-5 psi.
- **Endpoint detection**: Motor current monitoring (removal rate changes when the oxide layer is cleared and the underlying material is exposed). Optical endpoint (interference fringes from the thinning oxide layer change periodically; the endpoint corresponds to the last fringe). Both methods provide ~10 nm accuracy.
- **Post-CMP cleaning**: Scrub with PVA brush and dilute (0.5%) HF to remove slurry particles and chemical residues. DI water rinse. Spin dry. Particle count target: <50 adders ≥0.16 μm.

### Tungsten (W) Plug Process

**Problem**: Contact holes and via holes between metal layers must be filled with a conductive material. Aluminum does not fill high-aspect-ratio holes well (it bulges at the top and leaves voids).

**Tungsten CVD fill**:
- **Adhesion/barrier layer**: Deposit 20-50 nm TiN (titanium nitride) by sputtering or CVD as a diffusion barrier and adhesion layer. TiN prevents WF₆ (tungsten hexafluoride, the tungsten source gas) from reacting with the underlying SiO₂ or silicon.
- **Tungsten deposition**: WF₆ + 3H₂ → W + 6HF at 300-400°C, 1-10 Torr, in a cold-wall CVD reactor. Tungsten nucleates on the TiN and grows from the bottom and sidewalls of the contact hole simultaneously, filling without voids. Deposition rate: 50-200 nm/min.
- **Etchback**: After filling the holes, excess tungsten on the flat field areas is removed by CMP (tungsten CMP using Fe(NO₃)₃ or H₂O₂-based slurry with Al₂O₃ abrasive). Etchback continues until only tungsten plugs remain in the holes, flush with the surrounding oxide surface.
- **Selectivity**: Tungsten CMP removal rate: 200-400 nm/min. Oxide removal rate during W CMP: <20 nm/min. Selectivity >10:1.

### Process Integration

**Process sequence for a two-level metal CMOS IC**:
1. Isolation (LOCOS or shallow trench isolation)
2. Well formation (n-well and p-well implants)
3. Gate oxidation, polysilicon gate deposition and patterning
4. Source/drain implant and anneal
5. Contact hole patterning and tungsten plug fill
6. Metal 1 (Al or Al-Cu) deposition and patterning
7. Inter-layer dielectric (SiO₂) deposition and CMP planarization
8. Via hole patterning and tungsten plug fill
9. Metal 2 deposition and patterning
10. Passivation (SiNₓ) deposition and bond pad opening
11. Electrical testing, dicing, packaging

**Thermal budget management**: Total thermal exposure after source/drain implant must be limited to prevent excessive dopant diffusion. Each high-temperature step (>800°C) widens the junctions. A typical thermal budget allows no more than 2-3 hours cumulative exposure above 900°C after implant. This constraint drives the adoption of low-temperature processes (PECVD at <400°C, sputtering at <300°C) for back-end-of-line (BEOL) steps.

---

*Part of the [Bootciv Tech Tree](../) • [Photolithography](./) • [All Domains](../)*
