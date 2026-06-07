# Chemical Vapor Deposition

> **Node ID**: photolithography.cvd
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Dependencies**: [`gas-handling`](../gas-handling/index.md), [`vacuum`](../vacuum/index.md), [`energy.electricity`](../energy/electricity.md)
> **Parent**: [`photolithography.fab-processes`](fab-processes.md)
> **Timeline**: Years 45-70
> **Outputs**: cvd_thin_films, deposited_oxide, deposited_nitride, polysilicon_layers, tungsten_plugs
> **Critical**: No — CVD is important but thermal oxidation and sputtering provide fallback deposition paths for early devices

Chemical vapor deposition (CVD) grows thin solid films on a substrate by decomposing or reacting gas-phase precursors at or near the substrate surface. Unlike physical vapor deposition (sputtering, evaporation) which transports pre-formed material, CVD creates new solid material from chemical reactions — enabling highly conformal coatings that cover steps, fill trenches, and coat complex geometries uniformly. CVD is the workhorse deposition technique in semiconductor manufacturing, producing gate electrodes (polysilicon), interlayer dielectrics (SiO₂), diffusion barriers (Si₃N₄), and contact fills (tungsten).

## CVD Variants

Three major CVD variants cover the full temperature and film-quality spectrum needed in IC fabrication:

| Type | Pressure | Temperature | Deposition rate | Uniformity | Primary use |
|---|---|---|---|---|---|
| APCVD (Atmospheric Pressure) | 760 Torr | 350-500°C | 10-100 nm/min | ±5-10% | SiO₂ (TEOS or SiH₄+O₂), doped oxides (BSG, PSG) |
| LPCVD (Low Pressure) | 0.1-1 Torr | 550-900°C | 2-10 nm/min | ±2-5% | Poly-Si, Si₃N₄, undoped SiO₂ — highest quality |
| PECVD (Plasma-Enhanced) | 0.5-5 Torr | 200-400°C | 5-50 nm/min | ±3-7% | SiNₓ passivation, SiO₂ interlayer dielectric on metallized wafers |

## APCVD — Atmospheric Pressure CVD

APCVD operates at ambient pressure in a conveyor-belt or open-tube reactor. Precursor gases flow over heated wafers, reacting at the surface to deposit film. The simplicity of the reactor (no vacuum system required) makes APCVD the easiest CVD variant to implement first.

**Reactor design**: Horizontal open-tube furnace or conveyor belt furnace. Wafers travel on a moving belt through heated zones where gases are injected from overhead nozzles. Temperature: 350-500°C. Gas flows: SiH₄ + O₂ for SiO₂, or TEOS (tetraethyl orthosilicate, Si(OC₂H₅)₄) carried by N₂ bubbler.

**SiO₂ deposition (SiH₄ + O₂)**:
- SiH₄ + O₂ → SiO₂ + 2H₂ at 350-450°C
- Deposition rate: 10-100 nm/min depending on silane concentration and temperature
- Film properties: density ~2.1 g/cm³ (vs. 2.2 g/cm³ for thermal oxide), refractive index ~1.44-1.46
- Step coverage: poor — conformality is limited by gas-phase nucleation at atmospheric pressure

**Doped oxides (PSG, BSG)**:
- Phosphosilicate glass (PSG): add PH₃ to SiH₄ + O₂ flow → SiO₂:P₂O₅. Used as interlayer dielectric and getter for mobile ion contamination (Na⁺). P content 2-8 wt%.
- Borophosphosilicate glass (BSG): add both B₂H₆ and PH₃ → reflows at 850-950°C to planarize surface.

**Limitations**: poor step coverage, particle generation from gas-phase homogeneous nucleation, limited uniformity (±5-10%). Suitable for thick films where conformality is not critical.

## LPCVD — Low Pressure CVD

LPCVD operates at 0.1-1 Torr in a hot-wall resistance-heated quartz tube furnace. The low pressure increases mean free path (from ~70 nm at 760 Torr to ~50 mm at 1 Torr), dramatically improving gas-phase uniformity across a batch of 50-200 wafers standing vertically in a slotted quartz boat. LPCVD produces the highest-quality CVD films with excellent conformality and ±2-5% uniformity.

**Reactor design**: Horizontal or vertical quartz tube furnace, 3-zone resistive heating (±1°C uniformity). Wafers stand vertically on edge in a slotted quartz boat, spaced 5-10 mm apart. Vacuum system: mechanical roughing pump (rotary vane) pulls the tube down to 0.1-1 Torr. Gas injection at one end, pumping at the other. Load lock for wafer introduction without venting the hot tube.

**Polysilicon deposition**:
- SiH₄ → Si + 2H₂ at 620°C, 0.2-0.5 Torr
- Deposition rate: ~10 nm/min
- Film structure: amorphous below ~580°C, polycrystalline above. Grain size 50-200 nm at 620°C
- Doping: in-situ by adding PH₃ (n+) or B₂H₆ (p+), or post-deposition by POCl₃ diffusion or ion implant
- Used for: gate electrodes (most critical application), structural MEMS layers, high-value resistors, interconnects

**Silicon nitride (Si₃N₄) deposition**:
- 3SiH₂Cl₂ + 4NH₃ → Si₃N₄ + 6HCl + 6H₂ at 750-850°C, 0.2-0.5 Torr
- Deposition rate: 3-5 nm/min
- Film properties: near-stoichiometric Si₃N₄ (n=2.01, density 3.1-3.2 g/cm³), excellent diffusion barrier blocking Na, K, water vapor. Stress: ~1 GPa tensile (inherent in LPCVD nitride)
- Used for: LOCOS oxidation mask, passivation, etch stop, diffusion barrier

**SiO₂ deposition**:
- SiH₄ + O₂ at 450°C: ~5 nm/min. Lower quality than thermal oxide but deposited at much lower temperature
- TEOS (Si(OC₂H₅)₄) at 650-750°C: ~5-10 nm/min. Superior step coverage and gap fill due to higher surface mobility of TEOS-derived species. The go-to process for interlayer dielectric in multi-level metal schemes

## PECVD — Plasma-Enhanced CVD

PECVD uses RF plasma (13.56 MHz, or 2.45 GHz microwave) to provide the reaction energy that would otherwise require high temperature. This decouples deposition temperature from reaction chemistry, enabling film deposition at 200-400°C — low enough to avoid damaging aluminum interconnects (Al melts at 660°C) and preserving existing dopant profiles.

**Reactor design**: Parallel-plate cold-wall reactor. RF power applied to the upper electrode (showerhead gas distributor), wafer sits on the grounded lower electrode (heated to 200-400°C). Chamber pressure: 0.5-5 Torr. The plasma generates ions, radicals, and energetic electrons that drive surface reactions at substrate temperatures far below the thermal activation energy.

**SiNₓ (silicon nitride) deposition**:
- SiH₄ + NH₃ + N₂ at 300-400°C, 0.5-2 Torr, RF power 20-600 W
- Deposition rate: 5-50 nm/min (rate increases with RF power and silane flow)
- Film properties: SiNₓ (non-stoichiometric, x < 4/3), refractive index 1.9-2.3 (tunable by SiH₄:NH₃ ratio), hydrogen content 15-30 at% (significantly higher than LPCVD Si₃N₄ which has <5 at% H). Stress can be tuned from tensile to compressive by adjusting RF frequency (low frequency 100-400 kHz → compressive; high frequency 13.56 MHz → tensile)
- Used for: final passivation layer (moisture and scratch protection), anti-reflection coating on solar cells, interlayer dielectric on metallized wafers

**SiO₂ deposition**:
- SiH₄ + N₂O at 300-400°C, RF 13.56 MHz
- Lower density (2.0-2.1 g/cm³) and higher hydrogen content than thermal oxide, but adequate for interlayer dielectric where thermal oxide is not feasible
- Used for: interlayer dielectric between metal layers, planarization fill

## Tungsten CVD for Contact and Via Fill

Tungsten (W) CVD fills contact holes and via holes between metal layers with a conductive plug. Aluminum sputtering cannot fill high-aspect-ratio holes (it bridges the top, leaving voids). Tungsten nucleates from the bottom and sidewalls, filling void-free.

**Process**:
1. **Barrier/adhesion layer**: Deposit 20-50 nm TiN by sputtering or CVD. TiN prevents WF₆ from reacting with SiO₂ or silicon beneath.
2. **Tungsten deposition**: WF₆ + 3H₂ → W + 6HF at 300-400°C, 1-10 Torr, in a cold-wall single-wafer reactor. Deposition rate: 50-200 nm/min.
3. **Etchback**: Remove excess W on the flat field by CMP (tungsten CMP with Fe(NO₃)₃ or H₂O₂-based slurry, Al₂O₃ abrasive). Selectivity W:SiO₂ >10:1.

## Gas Handling Requirements

CVD processes demand precise, safe handling of hazardous precursor gases:

**Key precursor gases**:
| Gas | Formula | Hazards | Use |
|---|---|---|---|
| Silane | SiH₄ | **Pyrophoric** — ignites spontaneously in air. Explosive at 0.5-90% concentration in air. | Poly-Si, SiO₂, SiNₓ source |
| Dichlorosilane | SiH₂Cl₂ | Flammable, corrosive (HCl decomposition product) | LPCVD Si₃N₄ source |
| Ammonia | NH₃ | Toxic (corrosive to eyes, lungs). IDLH 300 ppm | Si₃Nₓ and Si₃N₄ nitrogen source |
| Tungsten hexafluoride | WF₆ | Corrosive, reacts with moisture to form HF. Stainless steel gas lines must be electropolished, passivated | Tungsten CVD source |
| TEOS | Si(OC₂H₅)₄ | Low hazard (liquid at room temperature, bp 168°C) | SiO₂ source (liquid precursor, N₂ bubbler) |
| Phosphine | PH₃ | **Extremely toxic** (TLV 0.3 ppm), pyrophoric. IDLH 50 ppm | In-situ doped poly-Si and PSG |
| Diborane | B₂H₆ | **Extremely toxic** (TLV 0.1 ppm), pyrophoric, explosive | In-situ doped p+ poly-Si and BSG |

**Gas delivery system**: Mass flow controllers (MFCs) with 1% accuracy, stainless steel tubing (electropolished 316L), gas cabinets with exhaust monitoring, automatic shut-off valves, and point-of-use purifiers. Silane lines must be continuously purged with N₂ when not in use — residual SiH₄ in dead volumes can accumulate and detonate.

## Temperature Ranges and Film Properties

Film properties vary dramatically with deposition temperature:

**Polysilicon** (LPCVD SiH₄):
- 550-580°C: amorphous, smooth surface (Ra < 2 nm), high resistivity
- 580-620°C: fine-grained poly-Si, grain size 50-100 nm, moderate resistivity
- 620-650°C: columnar poly-Si, grain size 100-200 nm, lower resistivity
- >650°C: large-grain poly-Si, rougher surface (Ra > 5 nm), lowest resistivity

**SiO₂ quality comparison**:
| Property | Thermal (dry O₂) | LPCVD SiH₄+O₂ | PECVD SiH₄+N₂O | APCVD SiH₄+O₂ |
|---|---|---|---|---|
| Density (g/cm³) | 2.20 | 2.15-2.20 | 2.00-2.10 | 2.10-2.15 |
| Refractive index | 1.462 | 1.44-1.46 | 1.44-1.48 | 1.44-1.46 |
| H content (at%) | <1 | 2-4 | 5-15 | 2-5 |
| Breakdown (MV/cm) | >10 | 6-8 | 4-6 | 5-7 |
| Step coverage | N/A (grown) | Good | Moderate | Poor |

**Silicon nitride quality comparison**:
| Property | LPCVD Si₃N₄ | PECVD SiNₓ |
|---|---|---|
| Density (g/cm³) | 3.1-3.2 | 2.5-2.9 |
| Refractive index | 2.01 | 1.9-2.3 |
| H content (at%) | <5 | 15-30 |
| Stress | ~1 GPa tensile | Tunable (tensile ↔ compressive) |
| Water permeation | Excellent barrier | Moderate barrier |
| Temperature limit on substrate | >700°C | 200-400°C |

## Uniformity and Process Control

Film uniformity directly impacts circuit performance — threshold voltage (Vt) depends on gate oxide thickness, and poly-Si gate resistance depends on poly-Si thickness. Target: ±2-5% across the wafer, ±5% wafer-to-wafer within a batch.

**Uniformity control knobs**:
- **Gas flow distribution**: injector design (showerhead vs. edge injection), total flow rate, pressure
- **Temperature uniformity**: 3-zone furnace control ±1°C for LPCVD, heated platen ±2°C for PECVD
- **Pressure control**: capacitance manometer + throttle valve feedback loop, ±0.01 Torr stability
- **Wafer spacing**: 5-10 mm in LPCVD boat (closer spacing → gas depletion effects)

**In-situ monitoring**: mass spectrometer on exhaust gas detects endpoint (e.g., WF₆ breakthrough indicates complete tungsten fill). Optical emission spectroscopy on PECVD plasma monitors radical concentrations (SiH*, N₂*, NH*) for real-time process control.

## Safety

**Silane (SiH₄) — pyrophoric hazard**: Silane ignites spontaneously on contact with air above ~2% concentration (lower flammability limit ~0.5% with ignition source). A silane leak in a gas cabinet or within the furnace exhaust system can produce a detonation. Safety measures:
- Double-contained gas lines (stainless steel inner tube, sealed outer tube with N₂ purge and H₂ sensor)
- Gas cabinet with continuous exhaust and silane-specific gas detector (catalytic bead or infrared)
- Automatic shut-off valve closes on detection of silane in cabinet exhaust, loss of cabinet exhaust flow, or seismic event
- Silane cylinders must be secured and connected through a check valve to prevent backflow
- Exhaust gas must pass through a burn box (electrically heated to 400°C) to decompose unreacted SiH₄ before venting

**Tungsten hexafluoride (WF₆) — corrosive/HF hazard**: WF₆ reacts with atmospheric moisture to produce HF (hydrofluoric acid vapor) and WO₃ (tungsten oxide particulate). Even trace moisture in WF₆ lines causes corrosion and particle generation. All WF₆ tubing must be electropolished 316L stainless steel, passivated, and heated (60-80°C) to prevent condensation. Exhaust gases (WF₆, HF, SiF₄) require wet scrubbing (caustic scrubber, NaOH solution) before release.

**Phosphine (PH₃) and diborane (B₂H₆) — extreme toxicity**: Both gases are fatal at concentrations undetectable by smell. TLV-TWA: PH₃ 0.3 ppm, B₂H₆ 0.1 ppm. Gas cabinets must have continuous toxic gas monitoring (electrochemical sensors), automatic valve closure on alarm, and ventilation that prevents any gas from reaching occupied areas. Use only in dedicated, interlocked gas cabinets with emergency purge capability.

## Process Integration Context

CVD steps in a typical IC fabrication sequence:
1. **LOCOS isolation**: LPCVD Si₃N₄ at 800°C as oxidation mask → wet oxidation → strip nitride
2. **Gate electrode**: LPCVD poly-Si at 620°C → dope n+ → pattern
3. **Interlayer dielectric**: LPCVD TEOS SiO₂ at 700°C or PECVD SiO₂ at 350°C → CMP planarize
4. **Contact fill**: CVD tungsten (WF₆ + H₂ at 350°C) → CMP etchback
5. **Passivation**: PECVD SiNₓ at 350°C as final protective layer

**Thermal budget constraint**: After source/drain implantation, total thermal exposure above 800°C must be limited to <2-3 hours cumulative to prevent excessive dopant diffusion. This drives the adoption of PECVD (200-400°C) and other low-temperature processes for all back-end-of-line (BEOL) steps after transistor formation.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Poly-Si film ±10% non-uniform across batch | Gas depletion in LPCVD tube — wafers near gas inlet see higher SiH₄ concentration | Reduce SiH₄ flow or pressure; rotate wafer positions between runs; consider vertical LPCVD furnace |
| PECVD SiNₓ hydrogen content >30 at% — film cracks during anneal | Temperature too low (<300°C); excess NH₃ flow; RF power insufficient | Raise temperature to 350-400°C; reduce NH₃:SiH₄ ratio; increase RF power toward 400-600 W |
| Tungsten plug voids — open contacts | TiN barrier non-conformal; WF₆:H₂ ratio wrong; contact aspect ratio exceeds tool limit | Increase TiN to 50 nm; optimize WF₆:H₂ at 350°C, 5 Torr; verify contact holes <5:1 aspect ratio |
| LPCVD Si₃N₄ film peeling from wafer | Excessive tensile stress (~1 GPa inherent); poor surface prep (moisture on wafer) | Reduce deposition rate (lower SiH₂Cl₂ flow); add in-situ N₂ plasma clean before deposition; ensure wafer bake at 150°C before loading |
| Silane gas detector alarm, no visible leak | SiH₄ accumulating in exhaust line (dead volume) or permeating through fitting seal | Close silane cylinder valve; purge line with N₂; check all VCR fittings with helium leak detector; replace copper gaskets on suspect fittings |

## See Also

- [Core Fab Processes](fab-processes.md) — parent capability with full fab process integration
- [Resists & Masks](resists-masks.md) — photoresist for patterning CVD films
- [Gas Handling](../gas-handling/index.md) — gas delivery infrastructure for CVD precursors
- [Vacuum Technology](../vacuum/index.md) — vacuum systems for LPCVD and PECVD reactors
- [Electricity](../energy/electricity.md) — power for furnace heaters and RF plasma generators
- [Dopant & Etch Gases](../chemistry/dopant-etch-gases.md) — process gas chemistry and supply chain
- [Cleanrooms](cleanrooms.md) — contamination-controlled environments for CVD processing

CVD process control relies on real-time monitoring of temperature, pressure, gas flows, and film thickness. In-situ ellipsometry measures film growth rate and optical properties during deposition, enabling closed-loop thickness control. Mass spectrometry of the exhaust gas provides information about reaction completeness and byproduct formation. Quadrupole mass spectrometers (QMS) are commonly used as residual gas analyzers to monitor the vacuum environment and detect contamination. These monitoring capabilities are essential for process reproducibility and for diagnosing problems when film quality deviates from specifications.
CVD process control relies on real-time monitoring of temperature, pressure, gas flows, and
film thickness. In-situ ellipsometry measures film growth rate and optical properties during
deposition, enabling closed-loop thickness control. Mass spectrometry of the exhaust gas
provides information about reaction completeness and byproduct formation. These monitoring
capabilities are essential for process reproducibility and for diagnosing problems when film
quality deviates from specifications.

The choice of precursor chemistry defines the CVD process for any given material. For silicon
dioxide, silane or TEOS (tetraethyl orthosilicate) are common precursors. For silicon nitride,
dichlorosilane and ammonia are used. Metal CVD for tungsten plugs uses tungsten hexafluoride.
Each precursor has different decomposition temperatures, byproduct profiles, and safety
requirements that shape the process design.

[← Back to Photolithography](index.md)
