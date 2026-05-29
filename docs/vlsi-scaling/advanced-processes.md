# Advanced Processes

> **Node ID**: vlsi-scaling.advanced-processes
> **Domain**: [VLSI Scaling & Advanced Semiconductor](./index.md)
> **Dependencies**: [`photolithography.fab-processes`](../photolithography/fab-processes.md)
> **Enables**: [`metals.specialty-semiconductor`](../metals/specialty-semiconductor.md)
> **Timeline**: Years 70-200+
> **Outputs**: ion_implantation, ald_films, copper_interconnects, cmp_planarization, high_end_solar
> **Cross-references**: [EDA, GPU Design & Advanced Packaging](eda-design.md) (summary-level coverage of these processes); [Core Fab Processes](../photolithography/fab-processes.md) (prerequisite baseline processes)

These processes represent the transition from baseline IC fabrication ([Core Fab Processes](../photolithography/fab-processes.md)) to sub-micron manufacturing. Each enables a capability impossible with diffusion doping, wet etching, or simple CVD alone. They are developed incrementally — ion implantation replaces diffusion first, then plasma etching replaces wet etching, then ALD and CMP enable multi-level metallization, and finally copper damascene replaces aluminum interconnects.

### Ion Implantation

Replaces thermal diffusion ([Core Fab Processes — Doping](../photolithography/fab-processes.md)) with precise, low-temperature doping control.

**Equipment chain**:
- **Ion source**: Gas feed (BF₃, AsH₃, PH₃) or solid source (Sb, In) heated to produce dopant vapor. Ionization via electron bombardment or RF plasma creates P⁺, As⁺, B⁺, BF₂⁺ ions.
- **Mass analyzer**: Magnetic sector (90° or 120° bend) separates ions by mass-to-charge ratio. Selects single dopant species — critical for preventing contamination. Resolution m/Δm > 100 required.
- **Acceleration column**: 10-300 keV electrostatic acceleration (high-current implanters: 10-100 keV; high-energy implanters: 200 keV - several MeV). Energy determines implant depth via LSS theory.
- **Beam scanning**: Electrostatic deflection plates raster the beam across the wafer. Uniformity target: ±1% across 300 mm wafer.
- **End station**: Wafer handling, cooling (ion beam deposits significant heat — 0.1-10 W/cm²), dose measurement via Faraday cup.

**Process parameters**:
- **Dose range**: 10¹¹-10¹⁶ cm⁻² (threshold adjust: 10¹¹-10¹²; source/drain: 10¹⁵-10¹⁶; buried layer: 10¹³-10¹⁴)
- **Implant depth**: 10-1000 nm depending on energy and species. Heavier ions (As) stop shallower than lighter ions (B) at same energy.
- **Channeling suppression**: Tilt wafer 7° off-axis, or grow 10-30 nm screen oxide, to prevent ions from channeling along crystal planes.

**[Annealing](../glossary/annealing.md)** (damage recovery + dopant activation):
- Implantation amorphizes the crystal lattice. Anneal restores crystallinity and moves dopants to substitutional sites.
- **Furnace anneal**: 900-1050°C, 30-60 min in N₂. Simple but causes significant dopant diffusion (redistributes the carefully controlled profile).
- **Rapid thermal anneal (RTA)**: Ramp to 1000-1100°C in seconds (halogen lamps), hold 10-30 sec, cool. Minimizes dopant redistribution. Preferred for sub-micron processes.
- **Spike anneal**: Ramp to peak temperature (~1080°C), immediately cool. Minimal diffusion. Used for ultra-shallow junctions.

**Strengths**:
- Ion implantation provides ±1% dose uniformity across 300 mm wafers — far more precise than thermal diffusion
- Energy selection (10-300 keV) independently controls junction depth, decoupling dose from profile

**Weaknesses**:
- Implantation amorphizes the crystal lattice — requires annealing step that partially redistributes dopants
- Beam scanning of large 300 mm wafers is slow — high-current implanters process only 10-30 wafers/hour

### Reactive Ion Etching (RIE) and Deep RIE (DRIE)

Replaces wet etching ([Core Fab Processes — Etching](../photolithography/fab-processes.md)) with anisotropic, high-fidelity pattern transfer.

**RIE fundamentals**:
- RF plasma at 13.56 MHz generates reactive ions and radicals. The ions bombard the surface vertically while radicals react chemically — combined chemical + physical etching yields anisotropic profiles.
- **Etch gases by material**: Si and SiO₂: CF₄/O₂, CHF₃/Ar; Al: Cl₂/BCl₃; Si (polysilicon gates): HBr/Cl₂/O₂; Si₃N₄: CHF₃/O₂.
- **Operating pressure**: 1-100 mTorr. Lower pressure → more anisotropic (longer mean free path, more directional ions).
- **Selectivity**: Etch rate ratio of target vs. mask material. Typical 5:1 to 50:1. Photoresist selectivity limits etch depth.
- **DC bias**: 100-500 V on the powered electrode accelerates ions into the wafer. Higher bias → more physical (sputter) component.

**Deep RIE (DRIE) — Bosch Process**:
- Alternating etch/passivation cycles create vertical sidewalls in deep silicon trenches:
  1. **Etch step**: SF₆ plasma, 5-15 sec. Fluorine radicals etch silicon isotropically (~1-3 μm/min etch rate).
  2. **Passivation step**: C₄F₈ plasma, 3-10 sec. Fluorocarbon polymer deposits on all surfaces (sidewalls and bottom).
  3. **Repeat**: 10-1000 cycles. Each cycle removes passivation from horizontal surfaces (ion bombardment) while sidewall polymer remains, producing near-vertical profiles.
- **Aspect ratios**: 10:1 to 30:1 (depth:width). Depths of 100-500 μm achievable.
- **Scalloping**: Small isotropic undulations on sidewalls (~50-200 nm per cycle). Reduced by minimizing etch step duration or using cryogenic DRIE variants.
- **Applications**: MEMS structures, through-silicon vias (TSVs), microfluidic channels, inkjet nozzles.

**Strengths**:
- RIE produces anisotropic (vertical) sidewalls essential for sub-micron pattern fidelity — impossible with isotropic wet etching
- Bosch DRIE achieves 10:1 to 30:1 aspect ratios at 100-500 μm depth — enables TSVs and MEMS structures

**Weaknesses**:
- Photoresist selectivity of only 5:1 to 50:1 limits etch depth per mask — deep etches require hard masks
- Bosch DRIE scalloping (50-200 nm per cycle) degrades sidewall smoothness — problematic for optical MEMS

### Atomic Layer Deposition (ALD)

Angstrom-level thickness control for ultra-thin conformal films. Unlike CVD ([Core Fab Processes — Deposition](../photolithography/fab-processes.md)), ALD is self-limiting — each cycle deposits exactly one atomic layer regardless of substrate geometry.

**Binary cycle mechanism**:
1. **Pulse precursor A**: Introduce first precursor, which chemisorbs onto the surface until all reactive sites are occupied (self-limiting saturation). Exposure: 0.1-2 sec.
2. **Purge**: Inert gas (N₂ or Ar) removes excess precursor and byproducts. 1-10 sec.
3. **Pulse precursor B**: Second precursor reacts with the adsorbed layer, forming one atomic layer of the desired material. 0.1-2 sec.
4. **Purge**: Remove reaction byproducts. 1-10 sec.
- **Cycle time**: 2-15 sec total. **Growth per cycle**: ~0.5-1.5 Å (material dependent).

**Material systems and precursors**:
- **Al₂O₃**: Trimethylaluminum (TMA) + H₂O. Temperature: 150-350°C. Growth: ~1.1 Å/cycle. Excellent conformality, high dielectric strength.
- **HfO₂** (high-k gate dielectric): Tetrakis(dimethylamido)hafnium (TDMAH) + H₂O. Temperature: 200-300°C. Growth: ~1.0 Å/cycle. Replaces SiO₂ gate oxide at sub-45 nm nodes.
- **TiO₂**: TiCl₄ + H₂O. Temperature: 150-400°C. Growth: ~0.6 Å/cycle. Used for DRAM capacitor dielectrics.
- **TiN**: TiCl₄ + NH₃. Temperature: 300-400°C. Growth: ~0.5 Å/cycle. Diffusion barrier, electrode material.
- **ZnO**: Diethylzinc (DEZ) + H₂O. Temperature: 100-250°C. Growth: ~1.6 Å/cycle. Transparent conductor.

**Trade-offs**: Extremely slow for thick films (100 nm = ~1000 cycles = ~1 hour). Unmatched for ultra-thin (1-20 nm), conformal coatings on high-aspect-ratio structures. Used where CVD cannot reach: inside deep trenches, around nanowire gates, as gate spacers.

**Strengths**:
- Self-limiting surface reaction deposits exactly one atomic layer per cycle — angstrom-level thickness control without complex flow calibration
- Conformal coating inside high-aspect-ratio structures (10:1+) — fills trenches and wraps nanowires uniformly

**Weaknesses**:
- 100 nm film requires ~1000 cycles (~1 hour) — far too slow for bulk films where CVD is preferred
- Precursor chemistries (TMA, TDMAH, TiCl₄) are pyrophoric or corrosive — dedicated gas handling required

### Chemical Mechanical Polishing (CMP)

Global planarization enabling multi-level metallization. Without CMP, topography accumulates with each deposited layer, making subsequent lithography impossible at sub-micron feature sizes.

**Process**:
- Rotating wafer pressed face-down against rotating polishing pad, with slurry flowing between them. Chemical reaction weakens surface layer; mechanical abrasion removes it.
- **Downforce**: 2-5 psi (higher pressure → faster removal but more defects).
- **Platen speed**: 30-80 rpm. **Carrier speed**: 30-80 rpm (counter-rotation for uniformity).
- **Removal rate**: 100-500 nm/min depending on slurry and material.

**Slurry formulations**:
- **SiO₂ removal**: Colloidal silica (30-50 nm particles) + KOH (pH 10-11). Removal rate: 100-300 nm/min.
- **Cu removal**: Alumina (50-100 nm) + H₂O₂ oxidizer + benzotriazole (BTA) corrosion inhibitor. Removal rate: 200-500 nm/min.
- **W (tungsten) removal**: Alumina + KIO₃ oxidizer. Removal rate: 150-300 nm/min.
- **STI (shallow trench isolation)**: Two-step — bulk SiO₂ removal with high-selectivity slurry, then high-selectivity slurry that stops on Si₃N₄ (selectivity > 20:1).

**Process control**:
- **Endpoint detection**: Motor current or friction changes when polishing reaches underlying layer.
- **In-situ thickness monitoring**: Optical interferometry during polish.
- **Post-CMP cleaning**: Double-sided brush scrubbing with dilute SC-1 (NH₄OH/H₂O₂/H₂O) to remove slurry particles and pad debris.

**Strengths**:
- CMP provides global planarization — enables multi-level metallization by eliminating accumulated topography
- STI two-step slurry achieves >20:1 selectivity (SiO₂:Si₃N₄) — stops precisely on nitride

**Weaknesses**:
- Slurry particles (30-100 nm) embed in wafer surface — require aggressive post-CMP brush scrubbing
- Downforce at 2-5 psi can cause dishing (over-polishing of soft copper in wide features) and erosion

### Copper Damascene Interconnects

Replaces aluminum metallization ([Core Fab Processes — Metallization](../photolithography/fab-processes.md)) with lower-resistance copper interconnects (ρ_Cu = 1.68 μΩ·cm vs ρ_Al = 2.65 μΩ·cm). Copper cannot be dry-etched with available chemistries, so a damascene (inlaid) process is used instead.

**[Dual damascene process](../glossary/dual-damascene-process.md)** (7 steps per metal layer):
1. **Dielectric deposition**: Deposit inter-layer dielectric (SiO₂ or low-k material). CVD or spin-on. 500-1000 nm thick.
2. **Lithography + etch**: Pattern trenches (wires) and vias (vertical connections) in the dielectric using two lithography steps + RIE. Dual damascene patterns both in one etch sequence.
3. **Barrier/seed deposition**: Deposit Ta/TaN barrier layer (5-20 nm by PVD or ALD) to prevent Cu diffusion into SiO₂. Deposit Cu seed layer (50-100 nm by PVD) for electroplating nucleation.
4. **Copper electroplating**: Electrochemical deposition fills trenches and vias with Cu. Suppressor, accelerator, and leveler additives control plating uniformity and prevent voids in narrow features. Bath: CuSO₄ + H₂SO₄ + Cl⁻ + organic additives.
5. **CMP**: Remove excess Cu and barrier material. Polish down to dielectric surface. Leaves Cu only in trenches and vias.
6. **Cap layer**: Deposit SiNₓ or SiCₓNᵧ cap (30-50 nm by PECVD) to seal Cu surface and act as etch stop for next layer.
7. **Repeat**: Stack 4-15 metal layers for complex logic ICs. Lower layers: fine pitch (50-100 nm wires). Upper layers: thick, coarse (power distribution).

**Low-k dielectrics**: Replace SiO₂ (k ≈ 4.0) to reduce interconnect capacitance:
- Organosilicate glass (OSG/SiCOH): k ≈ 2.5-3.0, deposited by PECVD.
- Porous OSG: k ≈ 2.0-2.5, introduced pores reduce dielectric constant but weaken mechanical strength.
- Air gap (ultimate low-k): k ≈ 1.0, selective removal of sacrificial material leaves air gaps between wires. Research/early production.

**Strengths**:
- Copper resistivity (1.68 μΩ·cm) is 37% lower than aluminum — reduces RC delay and power dissipation in interconnects
- Damascene process avoids Cu dry etch entirely — fills trenches by electroplating, then CMP removes excess

**Weaknesses**:
- Ta/TaN barrier layer (5-20 nm) consumes ~10-30% of trench cross-section at fine pitches, negating some of Cu's resistivity advantage
- Porous low-k dielectrics (k ≈ 2.0-2.5) have poor mechanical strength — crack during CMP and packaging

### High-End Solar Cells

Advanced processes enable significant efficiency gains over baseline screen-printed solar cells.

**PERC (Passivated Emitter and Rear Cell)**:
- Rear surface passivation with Al₂O₃ (10-30 nm, deposited by ALD or PECVD) + SiNₓ capping layer. Al₂O₃ provides excellent p-type surface passivation via negative fixed charges that repel electrons from the rear surface.
- Localized rear contacts opened by laser (laser contact opening, LCO). Reduces rear surface recombination.
- Module efficiency: 20-22%, up from 17-19% for standard Al-BSF cells.

**Bifacial cells**:
- Transparent rear side (grid pattern instead of full aluminum coverage). Captures ground-reflected and diffuse light on the rear surface.
- Additional energy yield: 5-20% depending on ground albedo and mounting geometry (bifaciality factor > 0.7).
- Requires: rear surface passivation (PERC architecture), fine-line rear metallization.

**Advanced metallization**:
- Fine-line screen printing: 30-50 μm finger width, 80-120 contacts per cell. Reduces shading losses.
- Plated contacts (Ni/Cu/Ag stack): Lower contact resistance than screen-printed Ag paste. Ni barrier prevents Cu diffusion into Si. Cu provides low bulk resistance. Thin Ag capping enables solderability.
- Multi-busbar designs (5-12 busbars): Shorter finger length reduces series resistance. Round wire busbars (0.2-0.4 mm diameter) capture some reflected light.

**Passivation stacks**: Thermal SiO₂ + SiNₓ (front, SiNₓ also serves as anti-reflection coating). Al₂O₃ for p-type surfaces (surface recombination velocity < 10 cm/s achievable). Hydrogen passivation from SiNₓ anneal passivates bulk defects.

**Strengths**:
- PERC achieves 20-22% module efficiency (up from 17-19% Al-BSF) with ALD Al₂O₃ rear passivation — surface recombination velocity < 10 cm/s
- Bifacial architecture adds 5-20% energy yield from ground-reflected rear irradiance with no additional processing cost

**Weaknesses**:
- Ni/Cu/Ag plated contacts require dedicated plating line and careful Cu contamination control — more complex than screen-printed Ag paste
- Porous low-k dielectrics in PERC rear stacks introduce mechanical fragility during module lamination

### Hazards & Safety

- **CMP slurry hazards**: Slurries combine fine abrasive particles (silica 30-50 nm, alumina 50-100 nm) with aggressive chemistry (KOH at pH 10-11, H₂O₂ oxidizer, KIO₃). Skin contact causes chemical burns and abrasive irritation; inhalation of dried slurry dust damages lungs. Wear chemical-resistant gloves, splash goggles, and apron during slurry handling and CMP operation. Slurry waste is hazardous — collect for treatment (neutralization + filtration) before disposal; do not drain.
- **Copper contamination concerns**: Copper is a fast diffuser in silicon and SiO₂ — even trace contamination (ppb levels) poisons minority-carrier lifetime in devices, causing leakage and yield loss. Dedicated Cu processing areas must be physically separated from front-end (FEOL) process areas. Cu tools, wafer carriers, and cleaning equipment must never be shared with non-Cu processes. Implement copper cross-contamination monitoring (surface wipe tests, TXRF analysis) on all wafers entering FEOL zones.
- **Ion implantation and RIE gases**: Dopant gases (AsH₃, PH₃, BF₃) are immediately dangerous to life at ppm concentrations. RIE gases (SF₆, CF₄, NF₃) are potent greenhouse gases requiring point-of-use abatement. Full hazard details and emergency procedures are documented in [EDA & GPU Design](eda-design.md).



### Rapid Thermal Processing (RTP)

RTP replaces batch furnace processing for temperature-sensitive steps where precise ramp rates and short dwell times are critical. A single wafer is heated by an array of high-intensity halogen lamps (tungsten-halogen, 1-2 kW each, typically 100-300 lamps) to 600-1200°C in seconds, held for 1-120 seconds, then cooled rapidly.

**Temperature control**:
- Pyrometer measurement (two-color ratio pyrometer, 0.8-1.1 μm wavelength) monitors wafer temperature non-contact with ±1-2°C accuracy. Thermocouple (type K or type S) embedded in the susceptor provides a secondary reference. Closed-loop PID control adjusts lamp power in <100 ms response time.
- Ramp rate: 50-250°C/s (compared to 5-15°C/min for batch furnaces). Rapid ramp minimizes dopant diffusion during annealing — at 1050°C spike anneal, total time at temperature above 900°C is <5 seconds, limiting dopant diffusion to <2 nm.
- Uniformity: ±2-5°C across 300 mm wafer, achieved by zonally controlled lamp arrays (inner/outer ring control) and shaped reflectors that compensate for edge heat loss. Non-uniformity causes spatial variation in sheet resistance, oxide thickness, or silicide phase.

**RTP applications**:
- **Spike anneal for ultra-shallow junctions**: Ramp to 1050-1100°C in ~1 second, immediately cool. Activates implanted dopants while limiting diffusion to <1-2 nm. Essential for source/drain extension formation at 65 nm and below where junction depth must be <20 nm.
- **Silicide formation**: Reaction of deposited metal (Ti, Co, or Ni) with silicon to form low-resistance silicide contacts (TiSi₂, CoSi₂, NiSi). RTP at 400-750°C for 30-60 seconds in N₂ ambient. NiSi (nickel silicide) is preferred at 45 nm and below: lower formation temperature (~300-400°C), lower Si consumption (~1 nm Ni → ~2 nm NiSi), and less sensitive to narrow line widths than TiSi₂ or CoSi₂.
- **Gate reoxidation**: Thin (~1-3 nm) oxide regrowth on gate sidewalls after RIE etching to repair plasma damage. RTP at 800-900°C in O₂ for 30-60 seconds.
- **Stress engineering**: strained silicon through rapid thermal chemical vapor deposition (RTCVD) of SiGe source/drain epitaxy at 600-800°C.

**Strengths**:
- Ramp rates of 50-250°C/s limit dopant diffusion to <2 nm during spike anneal — enables ultra-shallow junctions at 65 nm and below
- Single-wafer processing provides better wafer-to-wafer uniformity (±2-5°C) than batch furnaces

**Weaknesses**:
- Halogen lamp arrays (100-300 lamps) have non-uniform aging — requires frequent zonal recalibration to maintain ±2-5°C across 300 mm
- Pyrometer accuracy depends on wafer emissivity — patterned wafers with varying film stacks cause ±5-10°C measurement error

### Plasma-Enhanced CVD (PECVD)

PECVD deposits dielectric and passivation films at temperatures 200-400°C — far below the 600-900°C required for thermal CVD or LPCVD — by using plasma energy instead of thermal energy to drive film-forming reactions. This enables deposition on wafers with aluminum or copper metallization already in place.

**Equipment and parameters**:
- Parallel plate reactor: 200-300 mm electrode diameter, 10-30 mm electrode gap. RF power at 13.56 MHz, 100-600 W. Gas flow: 100-2000 sccm depending on film. Pressure: 0.5-10 Torr.
- Wafer temperature: 200-400°C (heated by resistive heater or lamp-heated chuck). Lower temperature than LPCVD preserves metal interconnect integrity.
- Deposition rate: 100-500 nm/min (much faster than ALD's ~0.1 nm/cycle).

**PECVD film properties**:
| Film | Precursor Gases | Temperature | Rate | Refractive Index |
|------|----------------|-------------|------|------------------|
| SiO₂ | SiH₄ + N₂O | 300-400°C | 200-400 nm/min | 1.45-1.47 |
| SiNₓ | SiH₄ + NH₃ + N₂ | 300-400°C | 100-200 nm/min | 1.9-2.2 |
| SiOₓNᵧ | SiH₄ + N₂O + NH₃ | 300-350°C | 150-300 nm/min | 1.5-1.8 |
| a-Si:H | SiH₄ | 200-300°C | 50-150 nm/min | 3.5-4.0 |
| α-C:F (low-k) | C₄F₈ + CH₄ | 200-350°C | 100-300 nm/min | 1.4-1.5 |

**SiNₓ stress engineering**: PECVD silicon nitride film stress is tunable from -500 MPa (compressive) to +200 MPa (tensile) by adjusting RF frequency (low frequency → more compressive), gas ratio (SiH₄:NH₃), and deposition temperature. Tensile SiNₓ on NMOS channel regions enhances electron mobility by ~5-15%. Compressive SiNₓ on PMOS enhances hole mobility. This "stress memorization technique" is a key performance booster at 45 nm and below.

**Strengths**:
- 200-400°C deposition temperature enables films on wafers with aluminum/copper metallization already in place — impossible with 600-900°C LPCVD
- Deposition rates of 100-500 nm/min are 100-1000× faster than ALD for bulk dielectric films

**Weaknesses**:
- Plasma damage to underlying layers (ion bombardment at 100-500 eV) degrades gate oxide quality — PECVD cannot be used directly on thin gate dielectrics
- Film stoichiometry is less pure than LPCVD — higher hydrogen content (10-25 at%) degrades electrical stability under bias temperature stress

### Thin Film Stress Management

Every deposited film carries intrinsic stress (from the deposition process) and thermal stress (from CTE mismatch during cooling). Uncontrolled stress causes wafer bow, film cracking, delamination, and device parameter shifts.

**Stress sources**:
- **Intrinsic stress**: Determined by deposition conditions (temperature, rate, ion bombardment). PECVD SiNₓ: -500 to +200 MPa depending on parameters. Sputtered metals: -200 to +500 MPa. LPCVD poly-Si: -200 to +50 MPa (compressive to slight tensile depending on doping). ALD Al₂O₃: +100 to +300 MPa (tensile).
- **Thermal stress**: σ_thermal = E_f/(1-ν_f) × (α_s - α_f) × (T_dep - T_room), where E_f is film Young's modulus, ν_f is Poisson's ratio, α_f and α_s are CTE of film and substrate. For Al on Si: α_Al = 23×10⁻⁶/°C vs α_Si = 2.6×10⁻⁶/°C → significant tensile stress in Al films deposited at >200°C and cooled to room temperature.
- **Wafer bow**: Stoney's equation relates film stress to wafer curvature: σ = (E_s × t_s²)/(6(1-ν_s) × t_f × R), where t_s and t_f are substrate and film thickness, R is radius of curvature. A 100 nm SiNₓ film with 300 MPa stress on a 775 μm Si wafer causes ~20 μm bow across 300 mm diameter. Excessive bow (>100 μm) prevents wafer chucking in lithography scanners.

**Stress measurement**: Laser scanning (measures wafer curvature before and after deposition). Accuracy: ±5 MPa. Measured at multiple points across the wafer to map stress uniformity.

**Strengths**:
- Stoney's equation provides a straightforward, non-destructive way to quantify film stress from wafer bow — laser scanning achieves ±5 MPa accuracy
- PECVD SiNₓ stress is tunable from -500 to +200 MPa by adjusting RF frequency and gas ratio — enables stress engineering for mobility enhancement

**Weaknesses**:
- Cumulative stress from 10+ deposited layers is difficult to predict — each new film changes the bow and affects subsequent lithography focus
- Porous low-k dielectrics have low elastic modulus (~5-10 GPa vs 70 GPa for SiO₂) — vulnerable to cracking under tensile stress during CMP

### Process Integration: 65 nm CMOS Flow

A representative 65 nm CMOS process flow shows how the individual unit processes combine into a complete manufacturing sequence. The full flow requires 35-45 mask layers and 400-600 individual process steps over 6-8 weeks of factory time.

**Front-end-of-line (FEOL)** — transistor formation:
1. Shallow trench isolation (STI): Pads SiO₂ (10 nm) + SiNₓ (100 nm) litho/etch → DRIE Si trenches (300-400 nm deep) → LPCVD SiO₂ fill (400 nm) → CMP planarize → SiNₓ strip
2. Well formation: Triple ion implant (triple-well for noise isolation): deep n-well (MeV P, 2-4 μm depth), p-well (300-800 keV B), n-well (300-800 keV P) → furnace anneal 1000-1050°C, 30-60 min
3. Gate oxide: Thermal SiO₂ (1.2-1.5 nm) or SiON (1.5-2.0 nm equivalent oxide thickness) at 900-1000°C
4. Polysilicon gate: LPCVD poly-Si deposition (150-200 nm) → gate lithography → RIE etch (HBr/Cl₂/O₂ chemistry, selectivity > 50:1 to gate oxide)
5. Offset spacer: Deposit SiNₓ (10-15 nm) by PECVD → anisotropic RIE → sidewall spacer defines source/drain extension implant region
6. Source/drain extension: Low-dose implant (As for NMOS, BF₂ for PMOS, 5-30 keV) → spike anneal (1050-1080°C, <1 s) → junction depth 15-30 nm
7. Main spacer: Deposit SiNₓ (30-50 nm) → RIE → defines deep source/drain region
8. Deep source/drain: High-dose implant (As for NMOS, BF₂ for PMOS, 10-60 keV, 10¹⁵ cm⁻²) → rapid thermal anneal (1000-1050°C, 10-30 s)
9. Salicide: Wet clean (dilute HF) → sputter Ni (10-20 nm) → RTP 300-400°C first anneal → wet strip unreacted Ni → RTP 400-500°C second anneal → NiSi on gate/source/drain (sheet resistance 5-15 Ω/sq)

**Back-end-of-line (BEOL)** — interconnect stack:
10. Contact (CA) layer: PECVD SiO₂ (300-500 nm) → lithography → RIE (CF₄/CHF₃/Ar) through oxide to source/drain/gate → Ti/TaN barrier (5-10 nm PVD) → W fill (CVD, 200-500 nm) → CMP → W plugs (contact resistance <50 Ω per contact)
11. Metal 1 (M1): PECVD SiO₂ or low-k dielectric (300-500 nm) → lithography → RIE trenches → Ta/TaN barrier (3-5 nm) → Cu seed (50-100 nm PVD) → Cu electroplate → CMP → damascene Cu lines (minimum pitch ~180 nm at 65 nm node)
12. Via 1 (V1) + Metal 2 (M2): Dual damascene process — two lithography steps (via-first or trench-first) → etch → barrier/seed → Cu electroplate → CMP
13. Repeat V+M layers: M2-M6 fine-pitch (180-280 nm pitch) → M7-M8 intermediate (400-800 nm pitch) → M9+ thick metal (1-4 μm pitch for power distribution)
14. Pad opening: Final passivation SiNₓ (500-800 nm) → lithography → RIE open bond pads → probe test

**Parametric targets** (65 nm generic):
- NMOS drive current: ~800-1000 μA/μm (I_dsat at Vdd = 1.0V)
- PMOS drive current: ~400-500 μA/μm
- Gate leakage: <50 pA/μm (SiON gate dielectric)
- Gate delay (FO4): ~12-15 ps
- SRAM cell size: 0.5-0.6 μm² (6T cell)

**Strengths**:
- 35-45 mask layers produce complete functional ICs with NMOS drive current ~800-1000 μA/μm — demonstrates that all unit processes integrate into a viable manufacturing flow
- Dual damascene BEOL with 4-15 metal layers provides both fine-pitch signal routing and thick power distribution in one stack

**Weaknesses**:
- 400-600 individual process steps over 6-8 weeks means a single particle defect at any step can kill the die — yield is multiplicative across all steps
- Spike anneal at 1050-1080°C must limit junction diffusion to <2 nm — equipment failure during ramp destroys the entire wafer


---
*Part of the [Bootciv Tech Tree](../index.md) • [VLSI Scaling](./index.md) • [All Domains](../index.md)*
