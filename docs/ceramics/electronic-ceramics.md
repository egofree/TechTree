# Electronic Ceramics

> **Node ID**: ceramics.electronic-ceramics
> **Domain**: [Ceramics & Refractories](./index.md)
> **Dependencies**: [`ceramics.advanced-ceramics`](advanced-ceramics.md), [`chemistry`](../chemistry/index.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 25-70+
> **Outputs**: MLCC capacitors, ferrite cores, PZT actuators, getter materials, ceramic substrates, varistors, thermistors
> **Critical**: Yes — passive components (capacitors, inductors, varistors) required for every semiconductor device and power supply

## Overview

Electronic ceramics are a specialized class of ceramics whose useful properties are electrical, magnetic, or electromechanical rather than structural. While [Advanced Ceramics & Refractories](advanced-ceramics.md) covers structural alumina, zirconia, SiC, and Si₃N₄, this capability addresses the functional ceramics that enable capacitors, inductors, piezoelectric actuators, varistors, thermistors, and vacuum tube maintenance. Without electronic ceramics, semiconductor devices lack the passive components they need to function, and vacuum systems cannot maintain the ultra-high purity environments that fabrication demands.

The critical electronic ceramic families:

- **Barium titanate (BaTiO₃)** — dielectric for multilayer ceramic capacitors (MLCCs)
- **Ferrites (MnZn, NiZn)** — magnetic cores for inductors, transformers, and EMI suppression
- **Lead zirconate titanate (PZT)** — piezoelectric actuators, sensors, and transducers
- **Getters (Zr-V-Fe, Ba)** — chemically active materials that maintain vacuum in sealed devices
- **Alumina substrates** — 96% Al₂O₃ base for thick-film hybrid circuits and IC packaging

## Prerequisites

### Materials

- **Barium carbonate** (BaCO₃, ≥99% purity) — from [Chemistry](../chemistry/acids-bases.md) (barite ore processing)
- **Titanium dioxide** (TiO₂, rutile or anatase, ≥99% purity) — from [Mining](../mining/processing.md) (ilmenite or rutile sands)
- **Iron oxide** (Fe₂O₃, ≥99%) — from [Mining](../mining/processing.md) (hematite)
- **Manganese carbonate** (MnCO₃) or MnO — from [Mining](../mining/processing.md)
- **Zinc oxide** (ZnO, ≥99.5%) — from [Chemistry](../chemistry/acids-bases.md)
- **Lead oxide** (PbO or Pb₃O₄, ≥99.5%) — from [Mining](../mining/processing.md) (galena processing)
- **Zirconia** (ZrO₂, ≥99%) — from [Advanced Ceramics](advanced-ceramics.md)
- **Nickel powder** (for MLCC electrodes) — from [Metals](../metals/iron-steel.md)
- **Alumina substrate** (96% Al₂O₃) — from [Advanced Ceramics](advanced-ceramics.md)

### Tools and Equipment

- **Ball mill** (zirconia or alumina media) — see [Machine Tools](../machine-tools/index.md)
- **Tape casting machine** (doctor blade, 5-20 μm gap) — see [Machine Tools](../machine-tools/index.md)
- **Screen printer** (for electrode deposition) — see [Machine Tools](../machine-tools/index.md)
- **Kiln** capable of 1200-1400°C with atmosphere control (air, N₂/H₂ reducing) — [Kiln Construction](kilns.md)
- **Hydraulic press** (50-100 MPa) — see [Machine Tools](../machine-tools/index.md)
- **DC power supply** (for poling PZT, 2-4 kV/mm) — [Electricity](../energy/electricity.md)

### Infrastructure

- **Clean processing environment** (dust control critical — contaminant particles cause short circuits in MLCCs)
- **Controlled atmosphere furnace** (N₂/H₂ reducing atmosphere for Ni-electrode MLCCs) — [Gas Handling](../gas-handling/index.md)
- **Ventilation** with HEPA filtration — mandatory for PbO powder handling
- **Electrical testing equipment** (LCR meter, insulation tester, oscilloscope)

## Bill of Materials

| Material | Quantity per 10,000 MLCCs (0402 X7R 100nF) | Source | Alternatives |
|----------|---------------------------------------------|--------|-------------|
| BaTiO₃ powder (doped, X7R formulation) | 5-15 g | [Chemistry](../chemistry/acids-bases.md) — BaCO₃ + TiO₂ calcined | Pre-synthesized BaTiO₃ from suppliers |
| Ni electrode paste | 3-8 g | [Metals](../metals/iron-steel.md) | Pd/Ag paste (air-fireable, higher cost) |
| PVB binder + plasticizer + solvent (slurry) | 5-10 g | [Polymers](../polymers/index.md) | Acrylic binder systems |
| Cu termination paste | 2-5 g | [Metals](../metals/iron-steel.md) | Ni termination paste |
| Sn plating (electroplating) | 0.5-2 g | [Metals](../metals/iron-steel.md) | None — solder termination required |

| Material | Quantity per kg MnZn ferrite cores | Source | Alternatives |
|----------|-------------------------------------|--------|-------------|
| Fe₂O₃ (hematite, ≥99%) | 650-720 g | [Mining](../mining/processing.md) | Regenerated iron oxide from steel pickling |
| MnCO₃ or MnO (≥99%) | 150-200 g | [Mining](../mining/processing.md) | MnO₂ (requires reduction during calcination) |
| ZnO (≥99.5%) | 120-170 g | [Chemistry](../chemistry/acids-bases.md) | No substitute — composition controls permeability |
| PVA binder | 30-50 g | [Polymers](../polymers/index.md) | PEG, methylcellulose |

## Process Description

### 4.1 Barium Titanate (BaTiO₃) — MLCC Capacitors

#### Principle

Barium titanate crystallizes in the perovskite structure (ABO₃). Above the Curie temperature (~120°C for pure BaTiO₃), the structure is cubic and paraelectric. Below 120°C, the Ti⁴⁺ ion displaces from the body center, producing tetragonal distortion and spontaneous polarization (ferroelectric). The dielectric constant peaks at ~10,000-15,000 at the Curie point and is ~2,000-5,000 at room temperature. This high permittivity, combined with thin-layer multilayer construction, enables enormous capacitance in tiny packages — over one trillion MLCCs are produced annually worldwide.

#### Prerequisites

- [Barium carbonate](../chemistry/index.md) (BaCO₃, ≥99%, powder <5 μm)
- [Titanium dioxide](../mining/index.md) (TiO₂, rutile or anatase, ≥99%, powder <2 μm)
- Dopant oxides: SrCO₃, CaCO₃, ZrO₂, MgO, Nb₂O₅ (≥99.5% each)
- [Nickel electrode paste](../metals/index.md) (Ni powder + organic vehicle)
- [Ball mill](../machine-tools/index.md) with zirconia media
- [Kiln](kilns.md) capable of 1200-1350°C with N₂/H₂ reducing atmosphere (pO₂ < 10⁻¹² atm)
- [Tape casting machine](../machine-tools/index.md) with doctor blade (5-20 μm gap)

#### Materials

- BaCO₃ + TiO₂ in 1:1 molar ratio (primary reactants)
- Dopants for X7R formulation: SrCO₃ (2-8 mol%), CaCO₃ (1-3 mol%), MgO (0.5-2 mol%)
- Solvent system: toluene/ethanol (60/40 weight ratio) or water-based with dispersant
- Binder: PVB (polyvinyl butyral) or acrylic, 5-12% of slurry solids
- Plasticizer: dibutyl phthalate or PEG, 2-5% of slurry solids
- Ni electrode paste: Ni powder (0.5-2 μm) + organic vehicle

#### Procedure: BaTiO₃ Powder Synthesis (Solid-State Reaction)

1. **Weigh** BaCO₃ and TiO₂ in exact 1:1 molar ratio. Add dopant oxides for desired formulation (e.g., X7R: SrCO₃ 3-6 mol%, CaCO₃ 1-2 mol%, MgO 0.5-1 mol%). Total batch: 1-10 kg typical.
2. **Ball mill** 12-24 hours with zirconia media in deionized water or alcohol. Target: <1 μm particle size after milling. Wet milling prevents agglomeration.
3. **Calcine** at 1100-1200°C for 2-4 hours in air. Reaction: BaCO₃ + TiO₂ → BaTiO₃ + CO₂ (g). Confirm complete reaction by X-ray diffraction — no residual BaCO₃ peaks.
4. **Re-mill** calcined powder 8-16 hours to break agglomerates and reduce to 0.5-1.0 μm. This step controls final grain size and dielectric properties.
5. **Test** dielectric constant of pressed and sintered test pellet: target εᵣ = 2500-4000 for X7R at 25°C.

#### Procedure: MLCC Manufacturing

1. **Prepare slurry**: Mix BaTiO₃ powder (doped formulation) with solvent (toluene/ethanol or water), binder (PVB or acrylic, 5-12%), dispersant (0.5-2%), and plasticizer (2-5%). Target viscosity: 500-2000 cP for tape casting.
2. **Tape cast**: Doctor blade spreads slurry onto carrier film (PET or silicone-coated steel). Blade gap 5-20 μm. Dry at 60-80°C. Result: flexible green tape, 3-15 μm thick for modern MLCCs (state of art: 0.5-1.0 μm).
3. **Print electrodes**: Screen print Ni electrode paste onto tape in alternating pattern (left-side for odd layers, right-side for even layers). Dry at 80-100°C.
4. **Stack and laminate**: Stack 200-1000+ printed tape layers with offset electrodes. Apply 10-30 MPa at 60-80°C to laminate into monolithic block.
5. **Cut**: Dice laminated block into individual capacitors. Standard case sizes: 0402 (1.0 × 0.5 mm), 0603 (1.6 × 0.8 mm), 0805 (2.0 × 1.25 mm).
6. **Burn out binder**: Heat to 300-500°C at 0.1-0.5°C/minute. Critical step — rapid binder decomposition causes delamination. Hold at 300°C for 4-8 hours, then at 500°C for 2-4 hours. Total burnout cycle: 24-72 hours.
7. **Sinter**: Heat to 1200-1350°C for 2-4 hours in reducing atmosphere (N₂ + 1-3% H₂, pO₂ < 10⁻¹² atm) to prevent Ni electrode oxidation. Shrinkage 15-20%. Cool in controlled atmosphere.
8. **Terminate**: Apply Cu or Ni termination paste to exposed electrode ends. Sinter or cure at 800-900°C in reducing atmosphere.
9. **Plate**: Electroplate Ni barrier layer (2-5 μm), then Sn solder finish (matte tin, 2-5 μm) on terminations.

#### Calibration and Verification

1. **Capacitance measurement**: Test with LCR meter at 1 kHz, 1 Vrms, 25°C. Target: within ±10% of nominal value for X7R. Check at -55°C, 25°C, and 125°C — capacitance change must be ≤±15% per X7R specification.
2. **Dissipation factor (DF)**: Measure at 1 kHz. Target: <2.5% for X7R.
3. **Insulation resistance**: Apply rated voltage for 60 seconds. Target: >10 GΩ·μF (IR × C product).
4. **Dielectric breakdown**: Apply increasing voltage until failure. Target breakdown strength: 20-50 kV/mm of dielectric thickness.
5. **Visual inspection**: No visible cracks, delamination, or electrode exposure. X-ray inspection for hidden defects in critical applications.

#### Expected Performance

| Parameter | Typical Value |
|-----------|--------------|
| Capacitance range | 1 pF to 100 μF |
| Rated voltage | 4V to 2500V |
| Dielectric constant (X7R) | 2500-4000 |
| Dielectric constant (Y5V) | 8000-15,000 |
| Dissipation factor (X7R at 1 kHz) | <2.5% |
| Insulation resistance | >10 GΩ·μF |
| Breakdown strength | 20-50 kV/mm |
| Layer thickness (state of art) | 0.5-1.0 μm |

#### Strengths

- Highest volumetric efficiency of any capacitor technology — trillion-per-year production volume confirms manufacturability at scale
- X7R formulations provide stable capacitance (±15%) over -55°C to +125°C — suitable for most electronic circuits
- Ni-electrode MLCCs eliminated expensive Pd/Ag electrodes — cost per unit dropped below $0.001 in high volume
- Ceramic construction provides reliability: no liquid electrolyte to dry out, expected lifetime >10 years at rated conditions

#### Weaknesses

- Fragile — ceramic body cracks under mechanical stress, thermal shock, or board flexure. Cracked MLCCs are a leading cause of field failures in electronics
- Capacitance decreases with applied DC voltage (DC bias effect) — a 100 nF X5R MLCC may lose 30-50% capacitance at rated voltage
- Microphonics — BaTiO₃'s piezoelectric response converts mechanical vibration into electrical noise
- Sintering Ni-electrode MLCCs requires precise oxygen partial pressure control (pO₂ < 10⁻¹² atm) — atmosphere control failure ruins the entire batch

### 4.2 Ferrites — Magnetic Ceramics

#### Principle

Ferrites are ceramic magnetic materials based on iron oxide (Fe₂O₃) combined with divalent metal oxides (MnO, ZnO, NiO, BaO, SrO). Unlike metallic magnetic materials, ferrites are electrically insulating — they operate at high frequencies without eddy current losses. Soft ferrites (MnZn, NiZn) have low coercivity for inductors and transformers; hard ferrites (Ba, Sr hexaferrite) have high coercivity for permanent magnets.

#### Prerequisites

- [Iron oxide](../mining/index.md) (Fe₂O₃, hematite, ≥99%, powder <5 μm)
- [Manganese carbonate](../mining/index.md) (MnCO₃) or MnO (≥99%)
- [Zinc oxide](../chemistry/index.md) (ZnO, ≥99.5%, powder <3 μm)
- [Nickel oxide](../mining/index.md) (NiO, ≥99%, for NiZn ferrite)
- [Ball mill](../machine-tools/index.md) with steel or zirconia media
- [Hydraulic press](../machine-tools/index.md) (50-100 MPa for core pressing)
- [Kiln](kilns.md) capable of 1100-1400°C with atmosphere control

#### Materials

- Fe₂O₃ (hematite, ≥99%, 0.5-2 μm particle size)
- MnCO₃ or MnO (≥99%)
- ZnO (≥99.5%)
- NiO (for NiZn ferrite, ≥99%)
- PVA binder (5-10% by weight)
- Deionized water (for wet milling)

#### Procedure: Soft Ferrite (MnZn) Core Manufacturing

1. **Weigh** raw materials precisely — composition controls magnetic properties within ±0.5 mol%. MnZn formulation: 25-35 mol% MnO, 15-25 mol% ZnO, 45-55 mol% Fe₂O₃.
2. **Ball mill** 4-12 hours with deionized water and steel or zirconia media. Target particle size: ~1 μm after milling.
3. **Calcine** (presinter) at 800-1000°C for 2-4 hours in air. Partial solid-state reaction forms spinel phase (Mn,Zn)Fe₂O₄. This step controls shrinkage uniformity and reaction completeness.
4. **Second milling**: Grind calcined powder to 0.5-1.5 μm. Add PVA binder (5-10%). Granulate for pressing.
5. **Press**: Fill steel die with granulated powder. Apply 50-100 MPa uniaxial pressure. Core geometries: toroids, E-cores, pot cores, RM cores, rods. Green density ~55-60% theoretical.
6. **Sinter**: Critical step. Heat to 1200-1400°C for 2-8 hours in controlled atmosphere. For MnZn: N₂ with controlled pO₂ (1-5% O₂ at 1200-1300°C). Too much O₂ → Fe²⁺ oxidizes to Fe³⁺, resistivity drops, core loss increases. Too little O₂ → Zn volatilizes. Cool slowly in controlled atmosphere. Density reaches 95-98% theoretical (~4.8-5.0 g/cm³).
7. **Grind** (if required): Flat mating surfaces for E-core halves require diamond grinding to minimize air gaps. Tolerance: ±0.02 mm on mating surfaces.

#### Procedure: Hard Ferrite (Ba Hexaferrite) Magnet Manufacturing

1. **Weigh** BaCO₃ or SrCO₃ with Fe₂O₃ in 1:6 molar ratio (BaO·6Fe₂O₃).
2. **Calcine** at 1200-1300°C for 2-4 hours. BaCO₃ + 6Fe₂O₃ → BaFe₁₂O₁₉ + CO₂.
3. **Ball mill** to sub-micron particle size. Single-domain particles ~1 μm give maximum coercivity — this is the most critical parameter.
4. **Press in magnetic field** (1-2 T applied) to align platelet-shaped particles along the easy axis. Produces anisotropic magnets with higher energy product. 50-100 MPa pressure. Alternatively, press without field for isotropic magnets (lower performance, simpler tooling).
5. **Sinter** at 1100-1250°C for 1-2 hours in air. Shrinkage 10-15%.

#### Calibration and Verification

1. **Permeability measurement** (soft ferrites): Wind test coil on toroid (N=20-50 turns). Measure inductance at 10 kHz with LCR meter. Calculate initial permeability: μᵢ = L × l / (μ₀ × N² × A). MnZn target: 1000-15,000. NiZn target: 10-2000.
2. **Core loss measurement**: Drive toroid with sinusoidal field at operating frequency (100 kHz typical). Measure power input with wattmeter. Core loss target: <500 kW/m³ at 100 kHz, 200 mT for MnZn power ferrite.
3. **Saturation flux density**: B-H tracer measurement. MnZn target: 0.35-0.5 T. NiZn target: 0.25-0.4 T.
4. **Coercivity** (hard ferrites): B-H tracer. Ba ferrite target: 150-300 kA/m. Sr ferrite target: 200-400 kA/m.
5. **Density**: Archimedes method. Soft ferrite target: 95-98% theoretical. Hard ferrite target: 90-95%.

#### Expected Performance

| Parameter | MnZn Soft Ferrite | NiZn Soft Ferrite | Sr Hard Ferrite |
|-----------|-------------------|-------------------|-----------------|
| Initial permeability | 1000-15,000 | 10-2000 | 1.05-1.10 (relative) |
| Saturation flux density | 0.35-0.5 T | 0.25-0.4 T | 0.25-0.45 T (remanence) |
| Coercivity | 10-100 A/m | 50-500 A/m | 200-400 kA/m |
| Operating frequency | 10 kHz - 2 MHz | 1 MHz - 500 MHz | DC / static |
| Resistivity | 0.1-10 Ω·m | 10⁴-10⁸ Ω·m | 10⁴-10⁸ Ω·m |
| Curie temperature | 100-250°C | 100-400°C | ~460°C |

#### Strengths

- Electrically insulating — no eddy current losses at high frequency, unlike iron or silicon steel cores
- Compositional tunability — permeability, loss, and frequency response are adjustable over wide ranges by varying Mn/Zn/Ni ratios and dopants
- Low cost — iron oxide is abundant and cheap; raw material cost for ferrite cores is dominated by processing, not materials
- Hard ferrite permanent magnets require no rare earth elements — barium and strontium are abundant

#### Weaknesses

- Lower saturation flux density (0.35-0.5 T) than silicon steel (1.5-2.0 T) — ferrite cores are larger for equivalent power handling
- MnZn ferrites require precise oxygen partial pressure control during sintering — atmosphere control errors cause dramatic property variation
- Ferrites are brittle — mechanical shock and thermal shock cause cracking. Cannot be machined with standard cutting tools (diamond grinding only)
- Curie temperature is relatively low (100-250°C for MnZn) — magnetic properties collapse above Curie temperature

### 4.3 PZT — Lead Zirconate Titanate (Piezoelectric Ceramics)

#### Principle

PZT (Pb[ZrₓTi₁₋ₓ]O₃) is the dominant piezoelectric ceramic. Near the morphotropic phase boundary (MPB) at x ≈ 0.52, the tetragonal and rhombohedral phases coexist, allowing easy polarization rotation and maximizing the piezoelectric response. When mechanical stress is applied to a poled PZT element, crystal lattice distortion generates a voltage (direct effect — sensor mode). When voltage is applied, the crystal deforms (converse effect — actuator mode).

#### Prerequisites

- [Lead oxide](../mining/index.md) (Pb₃O₄ or PbO, ≥99.5% purity) — handle with full respiratory protection (PbO is highly toxic)
- [Zirconia](advanced-ceramics.md) (ZrO₂, ≥99.5%)
- [Titanium dioxide](../mining/index.md) (TiO₂, ≥99.5%)
- Dopant oxides: Nb₂O₅, Ta₂O₅, Fe₂O₃, MnO₂ (≥99.5%)
- [Ball mill](../machine-tools/index.md) with zirconia media
- [Kiln](kilns.md) capable of 1200-1300°C with PbO-rich atmosphere control
- [DC power supply](../energy/electricity.md) (2-4 kV/mm for poling)
- Silicone oil bath (for poling, rated to 200°C)
- Silver paste (for electrodes)

#### Materials

- Pb₃O₄ (lead oxide, ≥99.5%) — use 1-5% excess to compensate for lead volatility
- ZrO₂ (zirconia, ≥99.5%)
- TiO₂ (titanium dioxide, ≥99.5%)
- Dopants: Nb₂O₅ (0.5-2% for "soft" PZT), Fe₂O₃ or MnO₂ (0.5-2% for "hard" PZT)
- PVA binder (3-8%)
- Ag paste (for electrodes, fired at 600-700°C)

#### Procedure: PZT Powder Synthesis

1. **Weigh** raw materials precisely for MPB composition: Pb(Zr₀.₅₂Ti₀.₄₈)O₃. Add 1-5% excess PbO to compensate for lead volatility during sintering. Add dopants (e.g., 1% Nb₂O₅ for soft PZT or 0.5% Fe₂O₃ for hard PZT).
2. **Ball mill** 12-24 hours with zirconia media in deionized water to homogenize and reduce particle size.
3. **Calcine** at 750-900°C for 2-4 hours in covered alumina crucible. Solid-state reaction forms perovskite PZT. Lead oxide is volatile above 800°C — use covered crucible with PbZrO₃ "sacrificial packing" to maintain PbO-rich atmosphere.
4. **Second milling**: Grind calcined powder to 0.5-2.0 μm. Add 3-8% PVA binder.

#### Procedure: PZT Forming, Sintering, and Poling

1. **Form**: Dry press at 50-100 MPa for simple shapes (discs, plates, rings). Tape cast for thin sheets (<0.5 mm). Green density ~55-60%.
2. **Burn out binder**: Heat to 500°C at 0.5-2°C/minute. Hold 2 hours.
3. **Sinter** at 1200-1300°C for 1-3 hours in sealed alumina crucible with PbZrO₃ packing powder to maintain PbO-rich atmosphere. Lead loss must be minimized — PZT with >2% Pb deficiency shows degraded piezoelectric properties. Density target: >95% theoretical (~7.5-8.0 g/cm³). Shrinkage: 12-18%.
4. **Machine** to final dimensions with diamond grinding. Standard tolerance: ±25-50 μm. Precision: ±5-10 μm.
5. **Apply electrodes**: Screen print Ag paste on both faces. Fire at 600-700°C for 10-30 minutes.
6. **Pole**: Heat PZT element to 100-150°C in silicone oil bath. Apply DC field of 2-4 kV/mm across electrodes. Hold 10-30 minutes. Cool to room temperature **under applied field**. Remove field — domains remain locked in alignment.

#### Calibration and Verification

1. **Piezoelectric coefficient d₃₃**: Measure with d₃₃ meter (Berlincourt meter). Apply known force, measure charge. Soft PZT target: 350-600 pC/N. Hard PZT target: 250-350 pC/N.
2. **Coupling coefficient k₃₃**: Measure from resonance/antiresonance frequency spectrum using impedance analyzer. Soft PZT target: 0.65-0.75.
3. **Density**: Archimedes method. Target: >95% theoretical (≥7.5 g/cm³).
4. **Curie temperature**: Measure dielectric constant vs temperature. Peak in εᵣ identifies Curie point. Soft PZT target: 250-365°C. Hard PZT target: 280-350°C.
5. **Depoling test**: Heat sample to 250°C for 1 hour, remeasure d₃₃. Loss should be <10%.

#### Expected Performance

| Property | "Soft" PZT (PZT-5A) | "Hard" PZT (PZT-4) |
|----------|----------------------|---------------------|
| d₃₃ (piezoelectric coefficient) | 350-600 pC/N | 250-350 pC/N |
| Relative permittivity (ε₃₃/ε₀) | 1500-3500 | 1000-1500 |
| Coupling coefficient k₃₃ | 0.65-0.75 | 0.60-0.70 |
| Mechanical Qm | 50-100 | 500-1000 |
| Curie temperature | 250-365°C | 280-350°C |
| Maximum continuous operating temp | 150-250°C | 175-250°C |

#### Strengths

- Highest piezoelectric coefficients of any lead-free alternative — d₃₃ of 350-600 pC/N vs <100 pC/N for most non-lead piezoceramics
- MPB composition provides strong electromechanical coupling — efficient conversion between electrical and mechanical energy
- Tunable via dopants: soft PZT for sensitive sensors/actuators, hard PZT for high-power ultrasonics/sonar
- Mature manufacturing process — PZT has been produced industrially since the 1950s with well-characterized processing-property relationships

#### Weaknesses

- Contains lead (Pb) — PZT manufacturing requires full respiratory protection, sealed sintering, HEPA-filtered exhaust, and blood lead monitoring for workers. PZT waste is hazardous (RCRA)
- Depoles above Curie temperature (250-365°C) — maximum continuous operating temperature is typically half the Curie point
- Brittle — PZT ceramics crack under tensile stress, impact, or rapid thermal cycling. Cannot be used in bending without pre-compression
- Lead volatility during sintering (PbO vapor pressure exceeds 1 mmHg above 800°C) causes compositional drift if atmosphere control is imperfect

### 4.4 Getter Materials — Vacuum Maintenance

#### Principle

Getters are chemically active materials that sorb (absorb or adsorb) residual gases in sealed vacuum or gas-filled devices. Non-evaporable getters (NEG, Zr-V-Fe alloys) are heated to activate a reactive surface that pumps gases at room temperature. Evaporable getters (Ba, Ti) are flashed to deposit a reactive metal film that permanently binds gas molecules. Without getters, vacuum tubes, CRTs, x-ray tubes, and semiconductor vacuum systems cannot maintain the required pressure over their operational lifetime.

#### Prerequisites

- [Zirconium](../mining/index.md) metal (≥99% purity, for NEG alloys)
- [Vanadium](../mining/index.md) (≥99%, for NEG alloys)
- [Iron](../metals/index.md) (≥99%, for NEG alloys)
- [Barium](../mining/index.md) (metallic Ba or BaAl₄ alloy, for evaporable getters)
- [Titanium](../mining/index.md) wire (for sublimation pumps)
- Arc melting furnace (for alloy preparation) — see [Metals](../metals/iron-steel.md)
- [Vacuum system](../vacuum/index.md) for getter activation and testing

#### Materials

- Zr-V-Fe alloy (St 707: 70% Zr, 24.6% V, 5.4% Fe by weight) — arc-melted and rolled to strip or wire
- BaAl₄ (barium-aluminum alloy) + Fe₂O₃ powder mixture (for flash getters)
- Titanium wire (≥99.7% Ti, 0.5-2.0 mm diameter, for sublimation pumps)

#### Procedure: Non-Evaporable Getter (NEG) Activation

1. **Install** NEG strip or cartridge in vacuum chamber. NEG material is passive at room temperature (surface protected by thin oxide layer).
2. **Evacuate** chamber to <10⁻⁶ Torr using primary vacuum pump.
3. **Activate** by heating NEG to 400-450°C for 30-60 minutes under vacuum. This desorbs the passive oxide layer, exposing fresh reactive Zr and V surfaces. Monitor chamber pressure — a pressure spike followed by drop confirms activation.
4. **Cool** to room temperature. Activated NEG now pumps H₂, CO, CO₂, N₂, O₂, H₂O at room temperature. Pumping speed: 5-50 L/(s·cm²) for H₂, 1-10 L/(s·cm²) for CO.
5. **Re-activate** as needed when pumping speed degrades (typically every 6-12 months in active systems) by repeating step 3.

#### Procedure: Evaporable Barium Getter (Vacuum Tube)

1. **Install** getter assembly (ring or trough containing BaAl₄ + Fe₂O₃ powder) in vacuum tube before sealing.
2. **Seal** tube after evacuation to <10⁻⁵ Torr.
3. **Flash getter**: After sealing, inductively heat getter assembly to 800-900°C from outside the tube. Exothermic reaction: 3 BaAl₄ + 4 Fe₂O₃ → 3 Ba + 4 Fe + 6 Al₂O₃ (simplified). Ba metal vapor deposits as mirror-like film on tube envelope interior.
4. **Verify**: Shiny Ba mirror = good vacuum. White/cloudy mirror = air leak, tube is compromised. The mirror serves as visual vacuum indicator for the lifetime of the tube.
5. **Result**: Fresh Ba film actively sorbs O₂, N₂, H₂, CO, CO₂, H₂O — any residual gas molecules that strike it are permanently bound.

#### Calibration and Verification

1. **Pumping speed test** (NEG): Measure throughput Q = S × P where S = pumping speed, P = pressure. Introduce known gas flow, measure steady-state pressure. Calculate S. Target: 5-50 L/(s·cm²) for H₂.
2. **Sorption capacity**: Expose activated NEG to measured gas quantity until saturated. H₂ capacity: up to 4 Torr·liters per gram.
3. **Visual inspection** (Ba getters): Mirror quality assessment — shiny silver = active, white/cloudy = failed, dark = exhausted.
4. **Vacuum integrity**: Monitor chamber/tube pressure over time. Getter-equipped tubes should maintain <10⁻⁵ Torr for rated lifetime (10,000+ hours for receiving tubes).

#### Expected Performance

| Getter Type | Activation Temp | Pumping Speed (H₂) | Capacity | Re-activatable |
|-------------|----------------|---------------------|----------|----------------|
| Zr-V-Fe NEG (St 707) | 400-450°C, 30-60 min | 5-50 L/(s·cm²) | 4 Torr·L/g (H₂) | Yes |
| Zr-Fe NEG (St 101) | 500-700°C, 30-60 min | 2-20 L/(s·cm²) | 2 Torr·L/g (H₂) | Yes |
| Ti-Zr-V coating | 180-250°C, 24 h | 10-100 L/(s·cm²) | Surface-limited | Yes |
| Ba evaporable | 800-900°C flash | N/A (one-time) | ~0.5 Torr·L/cm² | No |
| Ti sublimation pump | 1500-1700°C sublimation | ~10 L/(s·cm²) for N₂ | Film-limited | Yes (re-sublime) |

#### Strengths

- NEG getters provide continuous, power-free vacuum pumping at room temperature after one-time activation — no moving parts, no noise, no power consumption
- Ba evaporable getters provide visual vacuum indicator (mirror quality) — easy to assess tube health without instruments
- Ti sublimation pumps achieve very high pumping speeds for active gases — supplement ion pumps in UHV systems (10⁻⁸ to 10⁻¹¹ Torr)
- NEG cartridges can be re-activated multiple times, extending service life to years

#### Weaknesses

- NEG activation requires heating to 400-450°C under vacuum — requires external heater and power supply; cannot activate in sealed, unheated devices
- NEG does not pump noble gases (He, Ar, Ne) — must be combined with ion pump for complete UHV
- Ba evaporable getters are single-use — once flashed, they cannot be re-activated. If Ba film saturates before tube end-of-life, vacuum degrades
- Ti sublimation pumps consume titanium wire — finite filament lifetime (10-100 sublimation cycles per filament)

### 4.5 Ceramic Substrates for Electronics

#### Principle

Alumina substrates (96% Al₂O₃) provide the mechanical base and electrical insulation for thick-film hybrid circuits and cofired ceramic IC packages. The combination of moderate thermal conductivity (18-25 W/(m·K)), high dielectric strength, and compatibility with refractory metallization (W, Mo) makes alumina the default substrate material for power electronics, RF circuits, and high-reliability IC packages.

#### Prerequisites

- [Alumina powder](advanced-ceramics.md) (96% Al₂O₃ formulation, 1-3 μm particle size)
- [Tungsten](../mining/index.md) or [molybdenum](../mining/index.md) powder (for cofired metallization)
- [Silver-palladium](../mining/index.md) or [gold](../mining/index.md) paste (for thick-film conductors)
- [Ruthenium oxide](../mining/index.md) (RuO₂, for thick-film resistors)
- Screen printing equipment — see [Machine Tools](../machine-tools/index.md)
- [Kiln](kilns.md) capable of 850-950°C (thick-film) or 1600°C in H₂/N₂ (cofired ceramic)

#### Materials

- Alumina substrate: 96% Al₂O₃, 0.25-1.5 mm thick, laser-cut to size
- Conductor pastes: Ag-Pd (70/30), Au, or Cu
- Resistor paste: RuO₂-based (10 Ω/sq to 10 MΩ/sq sheet resistance)
- Dielectric paste: glass-ceramic, screen printable
- W or Mo paste (for cofired ceramic internal traces)

#### Procedure: Thick-Film Hybrid Circuit Fabrication

1. **Start** with 96% Al₂O₃ substrate (tape-cast, laser-cut to final dimensions). Clean with isopropanol.
2. **Screen print** conductor pattern (Ag-Pd, Au, or Cu paste) onto substrate using 200-325 mesh screen. Dry at 120-150°C for 10-15 minutes.
3. **Fire** at 850-950°C for 10-30 minutes (peak temperature, 60-minute total cycle). Only the paste sinters — the alumina substrate is already fully fired.
4. **Print additional layers**: Resistors (RuO₂-based paste), dielectrics (glass-ceramic paste), and additional conductor layers as required. Fire each layer at 850-950°C.
5. **Trim resistors**: Laser trim resistor values to target tolerance (±1% typical, ±0.1% achievable).
6. **Mount components**: Solder or conductive-epoxy attach SMD components. Wire bond ICs (Au ball bond or Al wedge bond).
7. **Encapsulate**: Dip coat or pot with silicone, epoxy, or glass for environmental protection.

#### Procedure: Cofired Ceramic IC Package

1. **Cast** green alumina tape layers (96% Al₂O₃, 0.1-0.5 mm thick).
2. **Punch vias** in each tape layer. Fill vias with W (tungsten) paste for interlayer connections.
3. **Screen print** W or Mo metallization patterns on each layer for signal routing.
4. **Stack and laminate** printed tape layers at 10-20 MPa, 70-80°C.
5. **Cofire** at 1600°C in reducing atmosphere (H₂/N₂) — W and Mo would oxidize in air at this temperature. The alumina sinters and metallization bonds simultaneously. Shrinkage: 15-20%.
6. **Post-fire**: Apply Ni/Au plating to external contacts. Braze metal leads (Fe-Ni-Co alloy "Kovar") using Ag-Cu eutectic braze at 779°C.
7. **Seal**: Lid seal with Au-Sn solder (eutectic 280°C) for hermetic package. Leak test: <10⁻⁸ atm·cc/s He.

#### Calibration and Verification

1. **Dielectric strength test**: Apply increasing voltage across substrate between two electrodes. Target breakdown: >15 kV/mm. Typical 1 mm substrate withstands >15 kV.
2. **Insulation resistance**: 500V DC between isolated traces. Target: >10¹² Ω.
3. **Thermal conductivity**: Laser flash method. 96% Al₂O₃ target: 18-25 W/(m·K).
4. **Hermeticity** (cofired packages): Helium leak test. Target: <10⁻⁸ atm·cc/s He leak rate.
5. **Wire bond pull test**: Pull Au or Al wire bond. Target pull strength: >5 gf for 25 μm Au wire.

#### Expected Performance

| Parameter | 96% Al₂O₃ | 99.6% Al₂O₃ |
|-----------|-----------|-------------|
| Dielectric constant (1 MHz) | 9.4-9.8 | 9.9 |
| Dielectric loss (tan δ, 1 MHz) | 0.0002-0.0004 | 0.0001-0.0002 |
| Volume resistivity | >10¹⁴ Ω·cm | >10¹⁴ Ω·cm |
| Thermal conductivity | 18-25 W/(m·K) | 30-35 W/(m·K) |
| CTE (25-300°C) | 6.5-7.5 × 10⁻⁶/°C | 6.5-7.0 × 10⁻⁶/°C |
| Flexural strength | 300-350 MPa | 350-400 MPa |
| Substrate thickness | 0.25-1.5 mm | 0.25-1.0 mm |

#### Strengths

- Excellent dimensional stability — fired alumina does not warp or creep under thermal cycling
- Compatible with refractory metallization (W, Mo) for high-temperature cofired processing
- Hermetic sealing possible with cofired ceramic packages — superior to plastic for moisture-sensitive devices
- Good thermal conductivity (18-25 W/(m·K)) enables power dissipation in hybrid circuits

#### Weaknesses

- Limited thermal conductivity compared to BeO (250-300 W/(m·K)) or AlN (140-200 W/(m·K)) — insufficient for high-power RF devices without additional heat sinking
- Cofired processing requires 1600°C in reducing atmosphere — expensive infrastructure (H₂/N₂ furnace)
- Alumina CTE (6.5-7.5 × 10⁻⁶/°C) does not match silicon (4.5 × 10⁻⁶/°C) — thermal stress on large dies in cofired packages
- Thick-film resistors have limited precision (±1% after trimming) compared to thin-film (±0.01%)

### 4.6 Varistors and Thermistors

#### Principle

ZnO varistors protect circuits from voltage transients. Grain boundaries in polycrystalline ZnO form back-to-back Schottky barriers that are insulating at low voltage but become conductive above a threshold. NTC thermistors (Mn-Co-Ni-O spinel) decrease resistance exponentially with temperature for sensing and compensation.

#### Prerequisites

- [Zinc oxide](../chemistry/index.md) (ZnO, ≥99.5%, for varistors)
- Bi₂O₃ (bismuth oxide, 0.5-5%), Sb₂O₃ (antimony trioxide, 0.5-3%), CoO, MnO, Cr₂O₃ (each 0.1-1%)
- MnO₂, Co₃O₄, NiO (≥99%, for NTC thermistors)
- [Ball mill](../machine-tools/index.md), [hydraulic press](../machine-tools/index.md), [kiln](kilns.md) (1100-1350°C)

#### Materials

- ZnO powder (≥99.5%, particle size 0.5-2 μm)
- Bi₂O₃, Sb₂O₃, CoO, MnO, Cr₂O₃ (varistor dopants)
- MnO₂, Co₃O₄, NiO (thermistor materials)
- Ag paste or flame-sprayed Al (for electrodes)
- Epoxy or phenolic resin (for encapsulation)

#### Procedure: ZnO Varistor Manufacturing

1. **Mix** ZnO powder with Bi₂O₃ (0.5-5%), Sb₂O₃ (0.5-3%), CoO (0.1-1%), MnO (0.1-1%), Cr₂O₃ (0.1-1%).
2. **Ball mill** 4-12 hours to homogenize.
3. **Press** into discs (5-40 mm diameter, 1-5 mm thick) at 50-80 MPa.
4. **Sinter** at 1100-1350°C for 1-4 hours. Bi₂O₃ forms liquid phase during sintering, segregating to grain boundaries → creates nonlinear I-V characteristic. Shrinkage 15-20%.
5. **Apply electrodes**: Ag paste fired at 600-700°C, or flame-sprayed Al.
6. **Test**: Apply increasing voltage, measure current. Nonlinear exponent α = 25-50 (V ∝ I^1/α). Clamp voltage tightly defined.

#### Procedure: NTC Thermistor Manufacturing

1. **Mix** MnO₂, Co₃O₄, NiO in desired molar ratios (e.g., Mn:Co:Ni = 1:1:1 for 3kΩ at 25°C).
2. **Calcine** at 800-1000°C for 2-4 hours. Spinel phase forms.
3. **Ball mill** to 1-3 μm. Add binder (PVA, 5-8%).
4. **Press** into beads, discs, or chips (2-10 mm) at 50-100 MPa.
5. **Sinter** at 1100-1300°C in air for 1-3 hours. Density target: >95% theoretical.
6. **Attach leads** with Ag paste. Encapsulate in epoxy or glass.
7. **Age** at 150°C for 24-48 hours to stabilize resistance value.

#### Calibration and Verification

1. **Varistor voltage**: Measure voltage at 1 mA DC. This is the nominal varistor voltage (V₁mA). Must be within ±10% of rated value.
2. **Nonlinear exponent α**: Measure voltage at 1 mA and 10 mA. Calculate α = log(I₂/I₁) / log(V₂/V₁). Target: 25-50.
3. **NTC resistance**: Measure at 25°C with precision ohmmeter. Target: within ±5% of nominal value.
4. **Beta parameter**: Measure resistance at 25°C and 85°C. Calculate β = ln(R₁/R₂) × T₁×T₂/(T₂-T₁). Target: 3000-4500 K.
5. **Thermal response time**: Immerse thermistor from 25°C air to 85°C oil bath. Measure time to reach 63% of final resistance. Target: 1-15 seconds depending on package size.

#### Expected Performance

| Parameter | ZnO Varistor | NTC Thermistor |
|-----------|-------------|----------------|
| Operating voltage range | 10-1000V RMS | N/A (passive sensor) |
| Clamp voltage ratio (V at 100A / V at 1mA) | 1.5-2.5 | N/A |
| Nonlinear exponent α | 25-50 | N/A |
| Response time (transient) | <25 ns | 1-15 s (thermal) |
| Resistance (NTC at 25°C) | N/A | 100 Ω to 1 MΩ |
| Beta parameter (NTC) | N/A | 3000-4500 K |
| Operating temperature | -40 to +85°C | -55 to +300°C |

#### Strengths

- ZnO varistors clamp transient voltages in nanoseconds — protect semiconductors from ESD and lightning surges
- NTC thermistors provide high sensitivity (3-5% resistance change per °C) — more sensitive than RTDs or thermocouples for small temperature changes
- Simple manufacturing — dry pressing and sintering, no atmosphere control required
- Low cost per unit — both varistors and NTC thermistors cost <$0.10 in high volume

#### Weaknesses

- ZnO varistors degrade with repeated surges — clamp voltage drifts upward with accumulated energy. Must be oversized for expected surge lifetime
- NTC thermistors have nonlinear response — require lookup table or Steinhart-Hart equation for accurate temperature conversion
- Self-heating in NTC thermistors (power dissipation causes temperature rise above ambient) limits minimum measurable temperature difference
- Varistor capacitance (100-10,000 pF) can interfere with high-frequency circuits

## Quantitative Parameters

### Electronic Ceramic Property Comparison

| Property | BaTiO₃ (X7R) | MnZn Ferrite | PZT-5A | 96% Al₂O₃ Substrate |
|----------|-------------|-------------|--------|---------------------|
| Dielectric constant | 2500-4000 | 12-15 (at 1 MHz) | 1500-3500 | 9.4-9.8 |
| Dissipation factor | <2.5% (1 kHz) | Core loss <500 kW/m³ (100 kHz) | tan δ <2% | 0.0002-0.0004 |
| Operating frequency | DC - 1 GHz | 10 kHz - 2 MHz | DC - 10 MHz | DC - 10 GHz |
| Max processing temp | 1350°C (sinter) | 1400°C (sinter) | 1300°C (sinter) | 1600°C (cofire) |
| Density | 5.5-6.0 g/cm³ | 4.8-5.0 g/cm³ | 7.5-8.0 g/cm³ | 3.65-3.75 g/cm³ |

### Sintering Parameters by Ceramic Type

| Ceramic | Sintering Temp | Atmosphere | Soak Time | Shrinkage |
|---------|---------------|------------|-----------|-----------|
| BaTiO₃ (MLCC) | 1200-1350°C | N₂/H₂ (reducing) | 2-4 h | 15-20% |
| MnZn ferrite | 1200-1400°C | N₂ + controlled O₂ | 2-8 h | 15-20% |
| NiZn ferrite | 1150-1350°C | Air | 4-8 h | 15-18% |
| PZT | 1200-1300°C | Sealed (PbO atmosphere) | 1-3 h | 12-18% |
| ZnO varistor | 1100-1350°C | Air | 1-4 h | 15-20% |
| NTC thermistor | 1100-1300°C | Air | 1-3 h | 15-18% |

## Scaling Notes

### MLCC Scale

- **Bench scale**: Tape cast 100-500 layers by hand. Fire in small box kiln. Produces 100-1000 MLCCs per batch. Suitable for prototyping and material development.
- **Production scale**: Automated tape casting, stacking (1000+ layers), and dicing. A single production line produces 1-10 million MLCCs per day. Layer thickness drives capacitance density — state of art: 0.5 μm dielectric layers.

### Ferrite Core Scale

- **Small batch**: Manual pressing, 50-200 cores per kiln load. Laboratory or small production.
- **Industrial**: Automated presses (10-20 parts/minute), tunnel kiln firing. 10,000-100,000 cores per day.

### Key Bottleneck: PbO Handling

PZT manufacturing at any scale requires lead oxide handling infrastructure: ventilated enclosures, HEPA-filtered exhaust, dedicated worker protection, and hazardous waste disposal. This regulatory and safety burden makes PZT production a bottleneck that does not scale easily from bench to factory.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| MLCC delamination (layer separation) | Too-fast binder burnout, uneven lamination pressure | Reduce burnout ramp to 0.1-0.3°C/minute; verify laminator pressure uniformity (±5% across platen) |
| MLCC low capacitance | Underfired dielectric, insufficient layer count, or Ni oxidation | Increase sintering temperature 25-50°C; verify pO₂ < 10⁻¹² in reducing atmosphere; check layer count by cross-section |
| Ferrite core high loss | Wrong sintering atmosphere (excess O₂ for MnZn), under-density | Adjust O₂ level in sintering atmosphere; increase sintering temperature or time to achieve >95% density |
| PZT low d₃₃ after poling | Insufficient poling field, lead loss during sintering, or depoling | Increase poling field to 3-4 kV/mm; verify PbO packing in crucible; check d₃₃ vs poling time curve to find optimum |
| PZT dark discoloration | Carbon contamination from binder or reducing atmosphere | Ensure complete binder burnout before sintering; use clean crucibles and packing powder |
| Varistor low α (poor nonlinearity) | Insufficient Bi₂O₃ at grain boundaries, non-uniform microstructure | Verify Bi₂O₃ content (0.5-5%); improve mixing uniformity; increase sintering temperature to ensure liquid-phase distribution |
| NTC thermistor resistance drift | Incomplete sintering, residual stress in encapsulation | Increase sintering temperature or time; age at 150°C for 48+ hours; verify encapsulation does not stress element |
| NEG won't activate | Surface contamination, insufficient activation temperature | Clean NEG surface before installation; increase activation temperature to 450°C; verify chamber reaches <10⁻⁶ Torr before activation |

## Safety

### Lead Compounds

PZT manufacturing involves PbO (lead oxide), which is highly toxic:

- **Exposure limits**: 50 μg/m³ (OSHA PEL for lead in air). Blood lead level <5 μg/dL (CDC reference).
- **Routes of entry**: Inhalation of PbO dust, ingestion from contaminated hands. PbO is readily absorbed through lungs and GI tract.
- **Controls**: All PbO powder handling in ventilated enclosures (fume hoods or glove boxes). Wet processing wherever possible. Dedicated clothing and laundering. No eating/drinking in work areas. Regular blood lead monitoring for workers.
- **Sintering**: PbO is volatile above 800°C (vapor pressure >1 mmHg). Sealed crucibles with sacrificial PbO packing essential. Exhaust gas must pass through HEPA filters and wet scrubbers.
- **Disposal**: PZT waste is hazardous waste (RCRA). Cannot be landfilled. Recycling processes recover lead.

### Barium Compounds

BaCO₃ (used in BaTiO₃ synthesis) is toxic if ingested — soluble barium compounds cause cardiac arrhythmia and muscle paralysis. BaCO₃ is soluble in stomach acid (solubility in HCl: ~20 g/L). Keep away from food/food areas. Wash hands thoroughly after handling.

### Beryllium Oxide

BeO substrates are safe in fired, monolithic form but **extremely hazardous as powder or dust**. Chronic beryllium disease (CBD, berylliosis) is a disabling granulomatous lung disease caused by inhaling BeO particles <10 μm. Sensitization can occur at very low exposure levels (<0.2 μg/m³). Machining, grinding, or breaking BeO ceramics must be done with wet methods and full respiratory protection (P100). Most applications now substitute AlN (aluminum nitride).

## Quality Control

### Incoming Raw Material Checks

- **BaCO₃ purity**: Test by XRF or wet chemistry. Target: ≥99%. Sr and Ca impurities shift Curie temperature.
- **Fe₂O₃ purity**: Test for SiO₂ and Al₂O₃ contaminants. Target: ≥99%. Silica contamination reduces permeability in ferrites.
- **PbO purity**: Test for Fe, Cu, and Ag contaminants. Target: ≥99.5%. Metallic impurities degrade PZT resistivity.
- **TiO₂ polymorph check**: XRD to confirm rutile or anatase phase. Target: >99% one polymorph. Mixed phases cause inconsistent reactivity.

### In-Process Checks

- **Calcination completeness**: XRD on calcined BaTiO₃ — no residual BaCO₃ peaks (peak at 2θ ≈ 24°C must be absent).
- **Green density**: Measure pressed compact mass and volume. Target: 55-65% theoretical.
- **Tape thickness**: Measure with micrometer at 5+ locations. Target: ±5% of nominal across the web.

### Final Product Acceptance

- **MLCC**: Capacitance within ±10% (X7R) or ±20% (Y5V). DF <2.5%. IR >10 GΩ·μF. Visual: no cracks.
- **Ferrite cores**: Permeability within ±20% of specification. Core loss < specification at rated frequency and flux density.
- **PZT elements**: d₃₃ within ±15% of target. Coupling coefficient k₃₃ within ±10%. Density >95% theoretical.
- **Varistors**: V₁mA within ±10%. α >25. Surge current test: survive 8/20 μs impulse at rated current without degradation.

## Variations and Alternatives

### Passive Component Technology Selection

| Application | Primary Technology | Alternative | Reason for Primary |
|-------------|-------------------|-------------|-------------------|
| Decoupling capacitor (digital ICs) | MLCC (X7R) | Tantalum electrolytic | MLCC: lower ESR, no polarity, higher reliability |
| High-voltage capacitor (1-6 kV) | Disc ceramic (BaTiO₃) | Film capacitor | Disc ceramic: smaller, cheaper at HV ratings |
| Power inductor (SMPS) | MnZn ferrite toroid | Iron powder core | MnZn: lower core loss at 50-500 kHz switching frequency |
| RF inductor (10-500 MHz) | NiZn ferrite bead | Air core | NiZn: higher permeability reduces turns count |
| Precision positioning | PZT stack actuator | Voice coil motor | PZT: sub-nm resolution, higher stiffness, no magnetic field |
| Voltage surge protection | ZnO varistor (MOV) | Gas discharge tube | MOV: faster response (<25 ns vs >1 μs), smaller |
| Temperature sensing (±0.1°C) | NTC thermistor | Pt RTD | NTC: higher sensitivity, lower cost, smaller package |
| Hermetic IC package | Cofired alumina | Plastic (epoxy molding) | Alumina: hermetic seal, >150°C operation, lower moisture ingress |

### Lead-Free Piezoelectric Alternatives

- **KNN** (potassium sodium niobate): d₃₃ ≈ 100-200 pC/N. Lead-free but lower performance and more difficult to process than PZT.
- **BNT-BT** (bismuth sodium titanate - barium titanate): d₃₃ ≈ 150-200 pC/N. Lead-free but depolarization temperature is low (~200°C).
- **Quartz** (single crystal SiO₂): d₁₁ ≈ 2.3 pC/N. Very low piezoelectric response but excellent stability and no poling required. Used for timing crystals, not actuators.

## References

- [Advanced Ceramics & Refractories](advanced-ceramics.md) — structural alumina, zirconia, SiC, Si₃N₄ processing
- [Kiln Construction](kilns.md) — kiln design for ceramic firing
- [Kiln Firing Protocols](kiln-firing.md) — temperature schedules and atmosphere control
- [Chemistry](../chemistry/acids-bases.md) — raw material synthesis (BaCO₃, ZnO, NaOH)
- [Mining](../mining/processing.md) — raw material extraction (TiO₂, Fe₂O₃, Mn ores, Pb ores)
- [Metals](../metals/iron-steel.md) — Ni, W, Mo for electrodes and metallization
- [Gas Handling](../gas-handling/index.md) — N₂/H₂ atmosphere supply for reducing sintering
- [Vacuum Systems](../vacuum/index.md) — getter integration in vacuum equipment
- [Electricity](../energy/electricity.md) — power supply for kilns, poling, and testing
- [Machine Tools](../machine-tools/index.md) — pressing, grinding, screen printing equipment
- [Photolithography](../photolithography/index.md) — downstream use of ceramic substrates and PZT actuators

---

*Part of the [Bootciv Tech Tree](../index.md) • [Ceramics & Refractories](./index.md) • [All Domains](../index.md)*
