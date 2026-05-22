# Advanced Processes

> **Node ID**: vlsi-scaling.advanced-processes
> **Domain**: [VLSI Scaling & Advanced Semiconductor](./index.md)
> **Dependencies**: [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`chemistry.dopant-etch-gases`](../chemistry/dopant-etch-gases.md), [`gas-handling.vacuum`](../gas-handling/vacuum.md)
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

**[Annealing](../glossary/annealing.html)** (damage recovery + dopant activation):
- Implantation amorphizes the crystal lattice. Anneal restores crystallinity and moves dopants to substitutional sites.
- **Furnace anneal**: 900-1050°C, 30-60 min in N₂. Simple but causes significant dopant diffusion (redistributes the carefully controlled profile).
- **Rapid thermal anneal (RTA)**: Ramp to 1000-1100°C in seconds (halogen lamps), hold 10-30 sec, cool. Minimizes dopant redistribution. Preferred for sub-micron processes.
- **Spike anneal**: Ramp to peak temperature (~1080°C), immediately cool. Minimal diffusion. Used for ultra-shallow junctions.

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

### Copper Damascene Interconnects

Replaces aluminum metallization ([Core Fab Processes — Metallization](../photolithography/fab-processes.md)) with lower-resistance copper interconnects (ρ_Cu = 1.68 μΩ·cm vs ρ_Al = 2.65 μΩ·cm). Copper cannot be dry-etched with available chemistries, so a damascene (inlaid) process is used instead.

**[Dual damascene process](../glossary/dual-damascene-process.html)** (7 steps per metal layer):
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

### Hazards & Safety

- **CMP slurry hazards**: Slurries combine fine abrasive particles (silica 30-50 nm, alumina 50-100 nm) with aggressive chemistry (KOH at pH 10-11, H₂O₂ oxidizer, KIO₃). Skin contact causes chemical burns and abrasive irritation; inhalation of dried slurry dust damages lungs. Wear chemical-resistant gloves, splash goggles, and apron during slurry handling and CMP operation. Slurry waste is hazardous — collect for treatment (neutralization + filtration) before disposal; do not drain.
- **Copper contamination concerns**: Copper is a fast diffuser in silicon and SiO₂ — even trace contamination (ppb levels) poisons minority-carrier lifetime in devices, causing leakage and yield loss. Dedicated Cu processing areas must be physically separated from front-end (FEOL) process areas. Cu tools, wafer carriers, and cleaning equipment must never be shared with non-Cu processes. Implement copper cross-contamination monitoring (surface wipe tests, TXRF analysis) on all wafers entering FEOL zones.
- **Ion implantation and RIE gases**: Dopant gases (AsH₃, PH₃, BF₃) are immediately dangerous to life at ppm concentrations. RIE gases (SF₆, CF₄, NF₃) are potent greenhouse gases requiring point-of-use abatement. Full hazard details and emergency procedures are documented in [EDA & GPU Design](eda-design.md).

---
*Part of the [Bootciv Tech Tree](../index.md) • [VLSI Scaling](./index.md) • [All Domains](../index.md)*
