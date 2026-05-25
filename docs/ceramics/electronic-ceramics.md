# Electronic Ceramics

> **Node ID**: ceramics.electronic-ceramics
> **Domain**: Ceramics & Refractories
> **Dependencies**: [`ceramics.advanced-ceramics`](advanced-ceramics.md), `chemistry`
> **Enables**: None (leaf capability)
> **Timeline**: Years 25-70+
> **Outputs**: MLCC capacitors, ferrite cores, PZT actuators, getter materials, ceramic substrates, varistors, thermistors

## Overview

Electronic ceramics are a specialized class of ceramics whose useful properties are electrical, magnetic, or electromechanical rather than structural. While [Advanced Ceramics & Refractories](advanced-ceramics.md) covers structural alumina, zirconia, SiC, and Si₃N₄, this capability addresses the functional ceramics that enable capacitors, inductors, piezoelectric actuators, varistors, thermistors, and vacuum tube maintenance. Without electronic ceramics, semiconductor devices lack the passive components they need to function, and vacuum systems cannot maintain the ultra-high purity environments that fabrication demands.

The critical electronic ceramic families:

- **Barium titanate (BaTiO₃)** — dielectric for multilayer ceramic capacitors (MLCCs)
- **Ferrites (MnZn, NiZn)** — magnetic cores for inductors, transformers, and EMI suppression
- **Lead zirconate titanate (PZT)** — piezoelectric actuators, sensors, and transducers
- **Getters (Zr-V-Fe, Ba)** — chemically active materials that maintain vacuum in sealed devices
- **Alumina substrates** — 96% Al₂O₃ base for thick-film hybrid circuits and IC packaging

## Barium Titanate (BaTiO₃) — MLCC Capacitors

Barium titanate is the dielectric workhorse of the electronics industry. Over one trillion MLCCs are produced annually — every smartphone contains 800-1000 of them. The perovskite crystal structure (ABO₃) gives BaTiO₃ an extraordinarily high dielectric constant near its Curie temperature.

### Crystal Structure and Ferroelectricity

BaTiO₃ crystallizes in the perovskite structure: Ba²⁺ at cube corners, O²⁻ at face centers, Ti⁴⁺ at the body center. Above the Curie temperature (~120°C), the structure is cubic (paraelectric, centrosymmetric). Below 120°C, the Ti⁴⁺ ion displaces from the center along a body diagonal → tetragonal distortion → spontaneous polarization (ferroelectric).

**Key temperatures** (pure BaTiO₃):

| Transition | Temperature | Structure Change |
|-----------|-------------|-----------------|
| Cubic → Tetragonal | ~120°C (Curie point) | Ferroelectric onset |
| Tetragonal → Orthorhombic | ~5°C | Polarization axis rotates |
| Orthorhombic → Rhombohedral | ~-90°C | Polarization axis rotates again |

The dielectric constant peaks at ~10,000-15,000 at the Curie temperature and is ~2000-5000 at room temperature (depending on grain size, dopants, and processing).

### Powder Synthesis

**Solid-state reaction** (industrial standard):
1. Mix BaCO₃ (barium carbonate) with TiO₂ (titanium dioxide, rutile or anatase) in 1:1 molar ratio
2. Ball mill 12-24 hours with deionized water or alcohol to ~1 μm particle size
3. Calcine at 1100-1200°C for 2-4 hours: BaCO₃ + TiO₂ → BaTiO₃ + CO₂
4. Re-mill the calcined powder to break agglomerates and reduce to 0.5-1.0 μm
5. Add dopants during milling (see below)

**Chemical routes** (finer powder, more expensive):
- **Oxalate method**: Precipitate barium titanyl oxalate from BaCl₂ + TiCl₄ + H₂C₂O₄, then calcine at 800-900°C. Produces 0.1-0.5 μm powder.
- **Hydrothermal synthesis**: React Ba(OH)₂ + TiO₂ in water at 150-200°C under pressure. Produces sub-micron BaTiO₃ directly without high-temperature calcination.

### Dopants and Curie Temperature Engineering

The Curie temperature and dielectric properties are tuned by substituting ions on the A-site (Ba²⁺), B-site (Ti⁴⁺), or both:

| Dopant | Site | Effect on Curie Temp | Purpose |
|--------|------|---------------------|---------|
| Sr²⁺ (strontium) | A-site (replaces Ba) | Lowers ~-4°C per mol% Sr | Shift Curie peak to room temperature for X7R formulations |
| Pb²⁺ (lead) | A-site (replaces Ba) | Raises ~+4°C per mol% Pb | High-temperature dielectrics |
| Ca²⁺ (calcium) | A-site (replaces Ba) | Minimal shift | Improves dielectric stability, reduces capacitance aging |
| Zr⁴⁺ (zirconium) | B-site (replaces Ti) | Lowers ~-6°C per mol% Zr | Broadens Curie peak, improves temperature stability |
| Nb⁵⁺ (niobium) | B-site (replaces Ti) | Slight shift | Donor dopant — reduces dielectric loss, improves insulation resistance |
| Mg²⁺ (magnesium) | B-site (replaces Ti) | Lowers Curie temp | Acceptor dopant — used in X7R formulations for flat temperature response |
| Y³⁺ (yttrium) | Either site | Variable | Amphoteric — occupies A or B site depending on stoichiometry |

**X7R specification** (EIA standard): Capacitance change ≤±15% over -55°C to +125°C. Achieved by broadening the Curie peak through Sr and Ca substitution plus controlled grain size (0.5-1.0 μm). The most common MLCC formulation.

**Y5V specification**: Capacitance change ≤+22%/-82% over -30°C to +85°C. Higher dielectric constant (~10,000-15,000 at room temp) but poor temperature stability. Used where maximum capacitance per volume matters more than stability.

### MLCC Manufacturing

Multilayer ceramic capacitors are the highest-volume application of BaTiO₃:

1. **Slurry preparation**: BaTiO₃ powder + solvent (toluene/ethanol or water) + binder (PVB or acrylic) + dispersant + plasticizer. Target viscosity 500-2000 cP for tape casting.

2. **Tape casting**: Doctor blade spreads slurry onto carrier film (PET or silicone-coated steel). Blade gap 5-20 μm. Dry at 60-80°C. Result: flexible green tape, 3-15 μm thick for modern MLCCs.

3. **Electrode printing**: Screen print Ni (nickel) or Pd/Ag (palladium-silver) electrode paste onto tape. Ni electrodes require sintering in reducing atmosphere (N₂/H₂) to prevent oxidation — now standard for cost reduction. Pd/Ag allows air sintering but is expensive.

4. **Stacking and laminating**: Stack 200-1000+ printed tape layers with offset electrodes (alternating left/right for termination). Apply 10-30 MPa at 60-80°C to laminate.

5. **Cutting**: Dice laminated block into individual capacitors (0201, 0402, 0603, 0805 case sizes — e.g., 0402 = 0.04 × 0.02 inches).

6. **Binder burnout**: Heat to 300-500°C at 0.1-0.5°C/minute. Slow ramp critical — rapid binder decomposition causes delamination. Holds at 300°C and 500°C for 2-8 hours each.

7. **Sintering**: Heat to 1200-1350°C for 2-4 hours. For Ni-electrode MLCCs: reducing atmosphere (N₂ + 1-3% H₂, pO₂ < 10⁻¹² atm) to prevent Ni oxidation. Cool in controlled atmosphere. Shrinkage 15-20%.

8. **Termination**: Apply Cu or Ni termination paste to exposed electrode ends. Sinter or cure.

9. **Plating**: Electroplate Ni barrier layer, then Sn solder finish (matte tin) on terminations.

### MLCC Properties and Specifications

| Parameter | Typical Value |
|-----------|--------------|
| Capacitance range | 1 pF to 100 μF |
| Rated voltage | 4V to 2500V |
| Dielectric constant (X7R) | 2500-4000 |
| Dielectric constant (Y5V) | 8000-15,000 |
| Dissipation factor (DF) | <2.5% (X7R at 1 kHz) |
| Insulation resistance | >10 GΩ·μF |
| Breakdown strength | 20-50 kV/mm |
| Layer thickness (state of art) | 0.5-1.0 μm |

### Disc and Tubular Capacitors

Before MLCCs dominated, single-layer disc capacitors were standard:

1. Press BaTiO₃ powder (with binders) into discs 5-25 mm diameter, 0.5-3 mm thick
2. Sinter at 1300-1350°C for 1-2 hours
3. Apply Ag paste electrodes to both faces, fire at 600-800°C
4. Attach leads, dip-coat in epoxy or phenolic resin

Lower capacitance per volume than MLCCs but simpler manufacturing. Still used for high-voltage applications (1-6 kV) and EMI filtering.

## Ferrites — Magnetic Ceramics

Ferrites are ceramic magnetic materials based on iron oxide (Fe₂O₃) combined with divalent metal oxides (MnO, ZnO, NiO, BaO, SrO). Unlike metallic magnetic materials, ferrites are electrically insulating — they operate at high frequencies without eddy current losses that plague iron cores.

### Soft Ferrites: MnZn and NiZn

"Soft" means easily magnetized and demagnetized (low coercivity). Used for inductors, transformers, and EMI suppression where the magnetic field reverses direction repeatedly.

**MnZn ferrite** (MnO-ZnO-Fe₂O₃ system):
- Composition: ~25-35 mol% MnO, 15-25 mol% ZnO, 45-55 mol% Fe₂O₃
- Initial permeability: 1000-15,000 (very high)
- Saturation flux density: 0.35-0.5 T
- Resistivity: 0.1-10 Ω·m (relatively low for a ceramic — limits frequency to ~1-2 MHz)
- Operating frequency: 10 kHz - 2 MHz
- Curie temperature: 100-250°C (composition-dependent)
- Applications: Power transformers, pulse transformers, common-mode chokes, broadband transformers

**NiZn ferrite** (NiO-ZnO-Fe₂O₃ system):
- Composition: ~15-30 mol% NiO, 15-30 mol% ZnO, 45-55 mol% Fe₂O₃
- Initial permeability: 10-2000 (lower than MnZn)
- Saturation flux density: 0.25-0.4 T
- Resistivity: 10⁴-10⁸ Ω·m (excellent — enables high-frequency operation)
- Operating frequency: 1 MHz - 500 MHz
- Curie temperature: 100-400°C
- Applications: RF inductors, EMI suppression beads, antenna rods, high-frequency transformers

### Soft Ferrite Manufacturing

1. **Raw material mixing**: Blend Fe₂O₃ (iron oxide, hematite), MnCO₃ or MnO, ZnO. Weigh precisely — composition controls properties within ±0.5 mol%.

2. **Ball milling**: Wet mill 4-12 hours with steel or zirconia media to ~1 μm.

3. **Calcination / presintering**: Heat to 800-1000°C for 2-4 hours in air. Partial solid-state reaction forms spinel phase (Mn,Zn)Fe₂O₄. This step controls shrinkage and reaction uniformity.

4. **Second milling**: Grind calcined powder to 0.5-1.5 μm. Add PVA binder (5-10%).

5. **Forming**:
   - **Dry pressing**: 50-100 MPa in steel dies for cores (toroids, E-cores, pot cores, RM cores)
   - **Extrusion**: For rods and tubes (antenna rods, bead-on-lead EMI suppressors)

6. **Sintering**: Critical step. Heat to 1100-1400°C (MnZn) or 1150-1350°C (NiZn) for 2-8 hours in controlled atmosphere.
   - **MnZn ferrites**: Sinter in N₂ with controlled pO₂ (oxygen partial pressure). At 1200-1300°C, equilibrium oxygen pressure is ~1-5% O₂. Too much oxygen → Fe²⁺ oxidizes to Fe³⁺, resistivity drops, core loss increases. Too little oxygen → zinc volatilizes. Cool slowly in controlled atmosphere. Density reaches 95-98% theoretical (~4.8-5.0 g/cm³).
   - **NiZn ferrites**: Sinter in air (more forgiving atmosphere control). 1150-1300°C for 4-8 hours. Density 95-97% theoretical.

7. **Machining** (if needed): Sintered ferrite is brittle but can be ground with diamond wheels. Flat mating surfaces for E-core halves require grinding to minimize air gaps.

### Core Geometries and Applications

| Core Type | Shape | Application |
|-----------|-------|-------------|
| Toroid | Donut | Inductors, common-mode chokes (no air gap, closed magnetic path) |
| E-core / EI | E-shaped | Power transformers, forward converters |
| Pot core | Cylinder with center post | High-Q inductors, adjustable via air gap |
| RM core | Square pot core | Compact inductors for PCB mounting |
| Rod | Cylinder | Antenna rods, simple inductors |
| Bead | Small cylinder with hole | EMI suppression (slip onto wire/cable) |

### Hard Ferrites (Permanent Magnets)

"Hard" ferrites have high coercivity — once magnetized, they resist demagnetization. BaFe₁₂O₁₉ (barium hexaferrite) and SrFe₁₂O₁₉ (strontium hexaferrite).

**Manufacturing**:
1. Mix BaCO₃ or SrCO₃ with Fe₂O₃ in 1:6 molar ratio (e.g., BaO·6Fe₂O₃)
2. Calcine at 1200-1300°C for 2-4 hours
3. Ball mill to sub-micron particle size (critical — single-domain particles ~1 μm give maximum coercivity)
4. Press in magnetic field (1-2 T) to align platelet-shaped particles along the easy axis → anisotropic magnets with higher energy product
5. Sinter at 1100-1250°C for 1-2 hours

**Properties**:

| Property | Ba Ferrite | Sr Ferrite |
|----------|-----------|------------|
| Remanence (Br) | 0.2-0.4 T | 0.25-0.45 T |
| Coercivity (Hc) | 150-300 kA/m | 200-400 kA/m |
| Energy product (BH)max | 7-12 kJ/m³ | 10-30 kJ/m³ |
| Curie temperature | ~450°C | ~460°C |
| Resistivity | 10⁴-10⁸ Ω·m | 10⁴-10⁸ Ω·m |

Applications: DC motors, loudspeakers, magnetic separators, refrigerator door seals, holding magnets. Lower performance than rare-earth magnets (NdFeB) but much cheaper and chemically stable.

## PZT — Lead Zirconate Titanate (Piezoelectric Ceramics)

PZT (Pb[ZrₓTi₁₋ₓ]O₃) is the dominant piezoelectric ceramic. Near the morphotropic phase boundary (MPB) at x ≈ 0.52 (52% Zr, 48% Ti), the piezoelectric response is maximized because the tetragonal and rhombohedral phases coexist, allowing easy polarization rotation.

### Piezoelectric Effect

When mechanical stress is applied to a poled PZT element, the crystal lattice distortion generates a voltage (direct effect — sensor mode). When a voltage is applied, the crystal deforms (converse effect — actuator mode). The coupling between mechanical and electrical energy is quantified by piezoelectric coefficients.

### PZT Powder Synthesis

1. **Raw materials**: Pb₃O₄ (lead oxide, PbO), ZrO₂ (zirconia), TiO₂ (titanium dioxide). All must be high purity (>99.5%).

2. **Weighing**: Precise stoichiometric weighing critical. Typical MPB composition: Pb(Zr₀.₅₂Ti₀.₄₈)O₃. Add 1-5% excess PbO to compensate for lead volatility during sintering.

3. **Ball milling**: Wet mill 12-24 hours to homogenize and reduce particle size.

4. **Calcination**: Heat to 750-900°C for 2-4 hours in covered alumina crucible. Solid-state reaction forms perovskite PZT. Lead oxide is volatile above 800°C — covered crucible with PbO-rich atmosphere ( PbZrO₃ "sacrificial packing") minimizes lead loss.

5. **Second milling**: Grind calcined powder to 0.5-2.0 μm.

### Dopant Systems

PZT properties are tuned by dopants:

| Dopant | Type | Effect |
|--------|------|--------|
| Nb⁵⁺, Ta⁵⁺, W⁶⁺ | Donor (replace Zr⁴⁺/Ti⁴⁺) | "Soft" PZT: higher d₃₃, higher permittivity, lower Qm. Easier to pole and depole. Used for sensors and actuators. |
| Fe³⁺, Mn²⁺, Cr³⁺ | Acceptor (replace Zr⁴⁺/Ti⁴⁺) | "Hard" PZT: lower d₃₃, higher Qm, higher coercive field. Stable under high drive. Used for sonar transducers, high-power ultrasonics. |
| La³⁺ | Donor on A-site (replaces Pb²⁺) | PLZT — transparent electro-optic ceramic for optical shutters and modulators |

### Forming and Sintering

1. **Binder addition**: Add 3-8% PVA binder to powder
2. **Forming**: Dry press at 50-100 MPa for simple shapes (discs, plates, rings). Tape cast for thin sheets (<0.5 mm).
3. **Binder burnout**: Slow heat to 500°C at 0.5-2°C/minute
4. **Sintering**: 1200-1300°C for 1-3 hours in PbO-rich atmosphere (sealed alumina crucible with PbZrO₃ packing powder). Lead loss must be minimized — PZT with >2% Pb deficiency shows degraded properties. Density >95% theoretical (~7.5-8.0 g/cm³).
5. **Machining**: Diamond grinding to final dimensions. PZT is brittle — standard tolerances ±25-50 μm, precision grinding ±5-10 μm.

### Poling

As-sintered PZT has randomly oriented domains — macroscopically non-piezoelectric. Poling aligns the domains:

1. Heat PZT element to 100-150°C in silicone oil bath (above Curie temperature of doped compositions is not required; elevated temperature reduces coercive field)
2. Apply DC electric field of 2-4 kV/mm across the electrodes (Ag paste fired at 600-700°C)
3. Hold for 10-30 minutes
4. Cool to room temperature **under applied field**
5. Remove field — domains remain locked in alignment

**Caution**: PZT depoles above its Curie temperature (typically 250-350°C depending on composition). Maximum continuous operating temperature is typically 150-250°C (half the Curie temperature).

### PZT Properties

| Property | "Soft" PZT (e.g., PZT-5A) | "Hard" PZT (e.g., PZT-4) |
|----------|---------------------------|--------------------------|
| Piezoelectric coefficient d₃₃ | 350-600 pC/N | 250-350 pC/N |
| Piezoelectric coefficient d₃₁ | -170 to -250 pC/N | -100 to -150 pC/N |
| Relative permittivity (ε₃₃/ε₀) | 1500-3500 | 1000-1500 |
| Coupling coefficient k₃₃ | 0.65-0.75 | 0.60-0.70 |
| Mechanical Qm | 50-100 | 500-1000 |
| Curie temperature | 250-365°C | 280-350°C |
| Coercive field | 10-12 kV/cm | 15-25 kV/cm |

### PZT Applications in Semiconductor Equipment

- **Nano-positioning stages**: Piezo stacks (many thin PZT layers in series, ~100 μm each) for wafer stage fine positioning in lithography tools. Sub-nanometer resolution. Stroke 10-100 μm.
- **Inkjet printheads**: PZT-driven drop-on-demand heads (also used for photoresist dispensing in advanced packaging)
- **Ultrasonic wire bonding**: PZT transducer drives capillary tool at 60-140 kHz for Au wire bonding in IC packaging
- **Vibration sensors**: Accelerometers in semiconductor fab equipment for monitoring and active vibration isolation

## Getter Materials — Vacuum Maintenance

Getters are chemically active materials that sorb (absorb or adsorb) residual gases in sealed vacuum or gas-filled devices. They maintain the vacuum integrity of CRTs, vacuum tubes, x-ray tubes, particle accelerators, and vacuum-insulated cryogenic vessels. In semiconductor manufacturing, getters maintain ultra-high vacuum in sputtering systems, ion implantation chambers, and analytical equipment.

### Non-Evaporable Getters (NEG)

**Zr-V-Fe alloys** (St 707 alloy: 70% Zr, 24.6% V, 5.4% Fe by weight):
- Most common NEG for modern vacuum systems
- Activation: Heat to 400-450°C for 30-60 minutes under vacuum. This desorbs the passive oxide layer, exposing fresh reactive Zr and V surfaces.
- Once activated, sorbs H₂, CO, CO₂, N₂, O₂, H₂O at room temperature
- Hydrogen absorption: Up to 4 torr·liters per gram of getter. H₂ diffuses into bulk metal (reversible if heated above 400°C).
- CO, CO₂, N₂, O₂: Chemisorbed on surface (irreversible). Sorption capacity limited by available surface area.
- Pumping speed after activation: 5-50 L/(s·cm²) for H₂, 1-10 L/(s·cm²) for CO
- Can be re-activated multiple times by heating

**Zr-Fe alloys** (St 101): Less common, requires higher activation temperature (500-700°C).

**Ti-Zr-V coatings**: Thin films (~1-5 μm) deposited by sputtering onto vacuum chamber walls. Extremely high surface area. Activation at 180-250°C (much lower than bulk NEG). Used in particle accelerators (LHC) and advanced vacuum chambers.

### Evaporable Getters

**Barium (Ba) getters** — classic vacuum tube getters:
1. Small ring or trough containing BaAl₄ (barium-aluminum alloy) + Fe₂O₃ (iron oxide) powder mixture
2. After tube is sealed and evacuated, inductively heat the getter assembly to 800-900°C
3. Exothermic "getter flash" reaction: 3 BaAl₄ + 4 Fe₂O₃ → 3 Ba + 4 Fe + 6 Al₂O₃ (simplified)
4. Ba metal vapor deposits as a mirror-like film on the tube envelope interior
5. Fresh Ba film actively sorbs O₂, N₂, H₂, CO, CO₂, H₂O — any residual gas molecules that strike it are permanently bound
6. The Ba mirror also serves as a visual indicator: shiny mirror = good vacuum, white/cloudy = air leak, tube is compromised

**Titanium sublimation pumps**:
- Titanium wire or ball fed into vacuum chamber
- Resistively heated to 1500-1700°C — Ti sublimes and deposits on chamber walls
- Fresh Ti film sorbs active gases (O₂, N₂, H₂, CO, CO₂, H₂O)
- Pumping speed: ~10 L/(s·cm²) for N₂
- Used as supplement to ion pumps in UHV systems (10⁻⁸ to 10⁻¹¹ Torr)
- Repeated sublimation cycles maintain clean surfaces

### Getter Integration in Vacuum Systems

| Application | Getter Type | Operating Temp | Activation |
|------------|-------------|---------------|------------|
| CRT displays | Ba evaporable | Room temp (after flash) | 800-900°C flash during manufacturing |
| Vacuum tubes (receiving) | Ba evaporable | Room temp | Flash during exhaust |
| Power tubes (transmitting) | Zr or Ta non-evaporable | 400-800°C (heated during operation) | Self-activating at operating temp |
| X-ray tubes | Ba + Zr-V-Fe NEG | Room + heated | Combined flash + NEG |
| Sputtering systems | Ti sublimation | Room (Ti film) | Periodic sublimation |
| Ion implanters | NEG (Zr-V-Fe) | Room temp | 400-450°C bake |
| Analytical equipment (SIMS, AES) | NEG + Ti sublimation | Room temp | Periodic activation |
| Particle accelerators | NEG coating (Ti-Zr-V) | Room temp | 180-250°C bake |

## Ceramic Substrates for Electronics

### 96% Alumina Substrates

While [Advanced Ceramics](advanced-ceramics.md) covers alumina in structural applications, the electronics-specific substrate variant deserves separate treatment:

**Specifications**:

| Property | 96% Al₂O₃ | 99.6% Al₂O₃ |
|----------|-----------|-------------|
| Alumina content | 96% | 99.6% |
| Density | 3.65-3.75 g/cm³ | 3.85-3.90 g/cm³ |
| Dielectric constant (1 MHz) | 9.4-9.8 | 9.9 |
| Dielectric loss (tan δ, 1 MHz) | 0.0002-0.0004 | 0.0001-0.0002 |
| Volume resistivity | >10¹⁴ Ω·cm | >10¹⁴ Ω·cm |
| Thermal conductivity | 18-25 W/(m·K) | 30-35 W/(m·K) |
| CTE (25-300°C) | 6.5-7.5 × 10⁻⁶/°C | 6.5-7.0 × 10⁻⁶/°C |
| Flexural strength | 300-350 MPa | 350-400 MPa |
| Substrate thickness | 0.25-1.5 mm | 0.25-1.0 mm |

**Thick-film hybrid circuit process**:
1. Start with 96% Al₂O₃ substrate (tape-cast, laser-cut to size)
2. Screen print conductors (Ag-Pd, Au, or Cu paste), resistors (RuO₂-based), and dielectrics (glass-ceramic paste)
3. Fire each layer at 850-950°C (much lower than substrate sintering temperature — only the paste sinters)
4. Mount SMD components with solder or conductive epoxy
5. Wire bond ICs (Au ball bond or Al wedge bond)
6. Encapsulate with silicone or epoxy for environmental protection

**Ceramic IC packages** (cofired ceramic):
- Green alumina tape layers with patterned W (tungsten) or Mo (molybdenum) metallization
- Laminated and cofired at 1600°C in reducing atmosphere (H₂/N₂) — W and Mo would oxidize in air at this temperature
- Hermetic package: <10⁻⁸ atm·cc/s He leak rate
- Superior to plastic packages for: high-reliability (military, space), high-temperature operation (>150°C), high-frequency (lower dielectric loss), hermetic seal requirements

### Other Electronic Substrates

**Beryllia (BeO)**: Thermal conductivity 250-300 W/(m·K) — close to aluminum. Used for high-power RF transistors and laser diode mounts. **Toxic**: BeO dust causes chronic beryllium disease (CBD). Manufacture requires stringent dust control.

**Aluminum nitride (AlN)**: Thermal conductivity 140-200 W/(m·K). CTE matches silicon (4.5 × 10⁻⁶/°C) better than alumina. Non-toxic alternative to BeO. Requires non-oxide sintering aids (Y₂O₃ or CaO, 2-5%) and N₂ atmosphere sintering at 1800-1900°C. Surface oxidation above 700°C in air degrades thermal conductivity.

## Varistors and Thermistors

### ZnO Varistors (Voltage-Dependent Resistors)

ZnO varistors protect circuits from voltage transients. The grain boundaries in polycrystalline ZnO form back-to-back Schottky barriers that are insulating at low voltage but become conductive above a threshold ("varistor voltage").

**Manufacturing**:
1. Mix ZnO powder with small amounts of Bi₂O₃ (0.5-5%), Sb₂O₃ (0.5-3%), CoO, MnO, Cr₂O₃ (each 0.1-1%)
2. Ball mill, dry, press into discs
3. Sinter at 1100-1350°C for 1-4 hours
4. Apply electrodes (Ag paste or flame-sprayed Al)
5. The Bi₂O₃ forms a liquid phase during sintering, segregating to grain boundaries → creating the nonlinear I-V characteristic

**Key property**: Nonlinear exponent α = 25-50 (V ∝ I^1/α, so a 10× increase in current causes only ~20-40% increase in voltage). Clamp voltage is tightly defined.

### NTC Thermistors

Negative temperature coefficient thermistors for temperature sensing and compensation:

**Composition**: Spinel-structure transition metal manganites — Mn-Co-Ni-O system. Typical: (Mn₁₋ₓCoₓ)₂O₄ or (Mn₁₋ₓ₋ᵧCoₓNiᵧ)₂O₃.

**Manufacturing**:
1. Mix MnO₂, Co₃O₄, NiO in desired ratios
2. Calcine at 800-1000°C
3. Ball mill, add binder, press into beads, discs, or chips
4. Sinter at 1100-1300°C in air
5. Attach leads, encapsulate in epoxy or glass

**Properties**: Resistance decreases exponentially with temperature. β parameter (characteristic temperature) typically 3000-4500 K. Resistance at 25°C ranges from 100 Ω to 1 MΩ.

## Safety

### Lead Compounds

PZT manufacturing involves PbO (lead oxide), which is highly toxic:

- **Exposure limits**: 50 μg/m³ (OSHA PEL for lead in air). Blood lead level <5 μg/dL (CDC reference).
- **Routes of entry**: Inhalation of PbO dust, ingestion from contaminated hands. PbO is readily absorbed.
- **Controls**: All PbO powder handling in ventilated enclosures (fume hoods or glove boxes). Wet processing wherever possible. Dedicated clothing and laundering. No eating/drinking in work areas. Regular blood lead monitoring for workers.
- **Sintering**: PbO is volatile above 800°C. Sealed crucibles with sacrificial PbO packing essential. Exhaust gas must pass through HEPA filters and wet scrubbers.
- **Disposal**: PZT waste is hazardous waste (RCRA). Cannot be landfilled. Recycling processes recover lead.

### Barium Compounds

BaCO₃ (used in BaTiO₃ synthesis) is toxic if ingested — soluble barium compounds cause cardiac arrhythmia and muscle paralysis. BaCO₃ is soluble in stomach acid. Keep away from food/food areas. Wash hands thoroughly after handling.

### Beryllium Oxide

BeO substrates are safe in fired, monolithic form but **extremely hazardous as powder or dust**. Chronic beryllium disease (CBD, berylliosis) is a disabling granulomatous lung disease caused by inhaling BeO particles <10 μm. Sensitization can occur at very low exposure levels (<0.2 μg/m³). Machining, grinding, or breaking BeO ceramics must be done with wet methods and full respiratory protection. Most applications now substitute AlN.

## Integration Points

| Stage | Contribution |
|-------|-------------|
| Silicon | MLCCs for power supply bypassing, decoupling; ferrite beads for EMI filtering on PCBs |
| Photolithography | PZT actuators for nano-positioning in lithography tools; alumina substrates for hybrid circuits |
| Gas-Handling / Vacuum | NEG getters for maintaining UHV in sputtering and ion implant systems; Ti sublimation pumps |
| Energy | Ferrite transformers for switch-mode power supplies; MnZn cores for power conversion |
| Computing | MLCC decoupling capacitors (thousands per CPU); ferrite EMI suppression on high-speed interconnects |

## Key Deliverables

- BaTiO₃ dielectric powder synthesis and MLCC manufacturing capability
- MnZn and NiZn soft ferrite core production for inductors and transformers
- PZT piezoelectric ceramic synthesis, sintering, and poling for actuators and sensors
- Non-evaporable getter (Zr-V-Fe) and evaporable getter (Ba) production for vacuum maintenance
- 96% Al₂O₃ substrates for thick-film hybrid circuits and cofired ceramic IC packages
- ZnO varistors for circuit protection and NTC thermistors for temperature sensing

---

*Part of the [Bootciv Tech Tree](../index.md) · [Ceramics & Refractories](./index.md) · [All Domains](../index.md)*
