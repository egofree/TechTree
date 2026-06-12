# Magnetic Materials

> **Node ID**: metals.magnetic-materials
> **Domain**: [Metals](./index.md)
> **Enables**: [`energy.electricity`](../energy/electricity.md)
> **Timeline**: Years 15-25
> **Outputs**: silicon_steel_laminations, grain_oriented_strip, alnico_magnets, ferrite_magnets
> **Critical**: false — enables electromagnetic devices but is downstream of steel production

This article covers the metallurgy and processing of magnetic materials. For electromagnetic devices that use these materials, see [Electric Motor](../energy/electric-motor.md), [Generator](../energy/generator.md), and [Power Distribution](../energy/power-distribution.md).

## Overview

Magnetic materials split into two functional classes: **soft magnetic materials** that magnetize and demagnetize easily (low coercivity), used in transformer cores, motor laminations, and relay armatures; and **permanent magnet materials** that resist demagnetization (high coercivity), used as field sources in motors, generators, and holding devices. Both classes derive their properties from composition and heat treatment — the same alloy can shift from soft to semi-hard depending on the cooling rate through the Curie point and the subsequent tempering cycle.

The performance ceiling of every electromagnetic machine is set by its magnetic circuit. A transformer built from plain low-carbon steel laminations loses 3-5 W/kg to hysteresis and eddy currents at 50 Hz; replacing those with grain-oriented 3% silicon steel cuts core loss to 0.8-1.2 W/kg — a 3× to 4× reduction in waste heat. Permanent magnets determine the air-gap flux density in motors and generators: alnico 5 at 1.25 T remanence versus ferrite at 0.35-0.4 T, with the gap between them determining machine size and weight for a given power output.

Magnetic material production sits downstream of [Iron & Steel Production](iron-steel.md) and [Steelmaking](steelmaking.md). It requires controlled-atmosphere or vacuum heat treatment furnaces, rolling mills capable of producing strip below 0.5 mm thickness, and stamping dies for lamination production. The critical process control point is grain orientation in silicon steel — achieved by a combination of composition, heavy cold reduction (~80-90%), and a multi-step recrystallization anneal.

## Prerequisites

**Materials**:
- [Low-carbon steel](iron-steel.md) or [electric furnace steel](steelmaking.md) as the base for soft magnetic grades
- Ferrosilicon alloy (75-90% Si) for silicon steel alloying — from [Steelmaking](steelmaking.md)
- Aluminum, nickel, cobalt, titanium, copper for alnico alloys — from [Non-Ferrous Metals](non-ferrous.md) and [Specialty Alloys](alloys.md)
- Iron oxide (Fe₂O₃) and barium/strontium carbonate for ferrite magnets — from [Mining](../mining/index.md)
- Insulating varnish or oxide coating for lamination stacking

**Tools and equipment**:
- [Rolling mill](forming.md) capable of cold-rolling strip to 0.25-0.50 mm thickness with precise thickness control (±0.02 mm)
- Controlled-atmosphere annealing furnace (hydrogen or vacuum, 800-1200°C range)
- Stamping press with progressive dies for lamination cutting
- Grinding and polishing equipment for metallographic preparation
- Magnetic property test equipment (permeameter, hysteresisgraph, Gauss meter)

**Knowledge**:
- Understanding of iron-carbon phase diagram and heat treatment ([Iron & Steel](iron-steel.md))
- Magnetic domain theory: domains, domain walls, magnetocrystalline anisotropy, magnetostriction
- B-H curve interpretation: saturation flux density, coercivity, remanence, permeability
- Rolling texture development and secondary recrystallization (Goss texture)

**Infrastructure**:
- Electrical power for furnace operation (50-500 kW depending on scale)
- Hydrogen gas supply (for decarburizing and annealing atmosphere) or vacuum pumping system
- Crane or hoist for handling heavy annealing furnace loads (100-5000 kg batches)

## Bill of Materials

### Silicon Electrical Steel (Non-Oriented, 3% Si)

| Material | Quantity per tonne finished strip | Source | Alternatives |
|----------|-----------------------------------|--------|-------------|
| Low-carbon steel scrap/pig iron | 960-980 kg | [Steelmaking](steelmaking.md) | Direct-reduced iron (DRI) |
| Ferrosilicon (75% Si grade) | 40-45 kg | [Steelmaking](steelmaking.md) | Pure silicon metal (more expensive) |
| Manganese (as Fe-Mn) | 5-10 kg | [Non-Ferrous Metals](non-ferrous.md) | Omit if scrap Mn sufficient |
| Aluminum (deoxidizer) | 1-2 kg | [Aluminum Production](aluminum.md) | Silicon-killed practice instead |
| Insulating coating varnish | 2-5 kg per tonne laminations | [Polymers](../polymers/index.md) | Phosphate/oxide coating |
| Annealing atmosphere (H₂ + N₂) | 5-20 m³ per tonne | [Chemistry](../chemistry/index.md) | Vacuum annealing (slower cycle) |

### Alnico Permanent Magnet (Alnico 5)

| Material | Quantity per kg cast magnets | Source | Alternatives |
|----------|------------------------------|--------|-------------|
| Iron | 510 g | [Iron & Steel](iron-steel.md) | Steel scrap (monitor C content) |
| Nickel | 140 g | [Non-Ferrous Metals](non-ferrous.md) | No substitute — defines coercivity |
| Cobalt | 240 g | [Non-Ferrous Metals](non-ferrous.md) | Alnico 2 (no Co) — lower performance |
| Aluminum | 80 g | [Aluminum Production](aluminum.md) | No substitute |
| Copper | 30 g | [Copper](copper.md) and [Bronze](bronze.md) | Omit for simpler grades |
| Titanium (Alnico 8/9 variants) | 5-8 g | [Non-Ferrous Metals](non-ferrous.md) | Omit for Alnico 5 |

### Ferrite (Barium Hexaferrite) Permanent Magnet

| Material | Quantity per kg sintered magnet | Source | Alternatives |
|----------|---------------------------------|--------|-------------|
| Iron oxide (Fe₂O₃, >99% purity) | 800-820 g | [Mining](../mining/index.md) — hematite ore or mill scale | Synthetic Fe₂O₃ from pickling liquor |
| Barium carbonate (BaCO₃) | 380-400 g | [Mining](../mining/index.md) — witherite ore | Strontium carbonate (SrCO₃) for Sr-ferrite — higher performance |

## Process Description

### Soft Magnetic Silicon Steel

Silicon steel is iron alloyed with 1-4.5% silicon. Silicon increases electrical resistivity (reducing eddy current losses), reduces magnetostriction (reducing transformer noise), and eliminates the γ-loop (preventing austenite formation, enabling large grain growth). The penalty: silicon reduces ductility above ~4.5% Si, making hot rolling the only viable forming method for higher grades.

**Non-oriented silicon steel (motor and small transformer grade)**:

1. **Melt and cast**: Charge electric arc or induction furnace with low-carbon steel scrap + ferrosilicon to achieve 1.0-3.5% Si, <0.06% C, 0.2-0.5% Mn. Tap at 1600-1650°C. Continuous cast into slabs (150-250 mm thick) or cast into ingots.
2. **Hot rolling**: Reheat slabs to 1150-1250°C. Hot roll to 2.0-3.0 mm strip in 5-8 passes. Finishing temperature above 850°C to avoid edge cracking in higher-Si grades.
3. **Pickling**: Remove oxide scale in 15-20% hydrochloric acid at 60-80°C. Rinse and dry.
4. **Cold rolling**: Roll to final gauge (0.35-0.65 mm) in a single pass or tandem mill. Total reduction 70-85%. This establishes the deformation structure for subsequent recrystallization.
5. **Decarburizing anneal**: Heat cold-rolled strip to 780-830°C in wet hydrogen/nitrogen atmosphere (dew point 30-50°C). Hold 2-5 minutes in continuous furnace. Carbon reduces to <0.005%. Water vapor in the atmosphere oxidizes carbon to CO/CO₂ and carries it away. This step is critical — residual carbon causes magnetic aging (increased hysteresis loss over time).
6. **Stress-relief anneal** (if stamped into laminations after step 5): Heat laminations to 750-800°C in dry hydrogen or vacuum for 1-2 hours. Cool at ≤50°C/hour through 600°C to avoid thermal stress. Stamping introduces plastic strain that degrades permeability by 20-40%; annealing restores it.

**Grain-oriented silicon steel (power transformer grade, 3% Si)**:

The goal is to develop the Goss texture — grains aligned with their [001] easy magnetization axis within 3-7° of the rolling direction. Grain-oriented strip has ~10× lower core loss in the rolling direction than non-oriented grades of the same thickness.

1. **Melt and cast**: Same as non-oriented, targeting 2.8-3.3% Si, 0.03-0.05% C, plus inhibitors (MnS at 0.05-0.10% S, or AlN at 0.02-0.03% Al + 0.005-0.01% N). Inhibitor particles pin grain boundaries during primary recrystallization, forcing abnormal grain growth of Goss-oriented grains during secondary recrystallization.
2. **Hot rolling**: Reheat to 1300-1380°C (dissolves inhibitors). Hot roll to 1.8-2.5 mm. Finish above 900°C.
3. **Normalization anneal** (optional): Heat to 1100-1150°C, hold 1-3 minutes, cool rapidly. Refines grain structure and precipitates fine inhibitor particles.
4. **First cold reduction**: Cold roll to ~0.55-0.70 mm (60-75% reduction). Heavy deformation stores strain energy that drives recrystallization.
5. **Intermediate anneal**: Heat to 800-900°C in N₂/H₂, hold 1-3 minutes. Primary recrystallization produces fine equiaxed grains (~15-25 μm) with a spread of orientations including a small fraction of Goss-oriented grains at the surface.
6. **Second cold reduction**: Cold roll to final gauge of 0.23-0.35 mm (50-65% reduction). This further sharpens the texture precursor.
7. **Decarburizing anneal**: Heat to 780-830°C in wet H₂/N₂ for 2-5 minutes. Reduce carbon to <0.003%.
8. **High-temperature anneal (secondary recrystallization)**: Heat to 1100-1200°C in dry hydrogen (dew point < -40°C). Hold 10-30 hours in batch furnace. Goss-oriented grains consume all others — final grain size 5-20 mm (visible to the naked eye). Inhibitor particles dissolve into the matrix. Hydrogen atmosphere removes sulfur and nitrogen.
9. **Insulating coating**: Apply magnesium silicate (forsterite) glass film or phosphate-based coating. Bake at 500-700°C. Coating provides interlaminar insulation and imparts tension to the strip, which reduces core loss by 5-10% (tensile stress suppresses domain wall motion losses).

### Alnico Permanent Magnets

Alnico alloys are iron-aluminum-nickel-cobalt compositions hardened by spinodal decomposition — a mechanism distinct from the martensitic hardening used in steel. No quenching is required; the magnetic hardness comes from a fine two-phase microstructure (α + α') that develops during controlled cooling.

**Alnico 5 casting process** (composition: 8% Al, 14% Ni, 24% Co, 3% Cu, balance Fe):

1. **Melt**: Charge induction furnace with iron, nickel, cobalt, copper, and aluminum (add Al last — it oxidizes readily). Melt under reducing conditions. Tap at 1550-1650°C. Aluminum additions lower the melting point to ~1450°C.
2. **Cast**: Pour into preheated sand or investment molds. Shell molds produce better surface finish and tighter tolerances. Design mold with gates that direct metal smoothly to avoid turbulence (aluminum oxidizes to Al₂O₃ inclusions that weaken the magnet).
3. **Fettling**: Remove gates and risers by grinding or abrasive cutoff. Magnets are cast to near-net shape — grinding serves only to clean up flash and achieve mating-surface flatness.
4. **Homogenizing treatment**: Heat to 1200-1250°C in hydrogen or vacuum. Hold 20-40 minutes to dissolve all phases into single-phase α (BCC). This is above the Curie point (~860°C for Alnico 5).
5. **Controlled cooling (spinodal decomposition)**: Cool from 1250°C to ~600°C at a controlled rate of 0.5-2.0°C/minute. Apply a magnetic field of ≥160 kA/m (2000 Oe) during cooling through the 900-600°C range — this aligns the elongated α' precipitates parallel to the field direction, producing uniaxial magnetic anisotropy. Field-aligned Alnico 5 achieves remanence of 1.25-1.35 T; non-aligned only 0.7-0.8 T.
6. **Tempering (precipitation hardening)**: Reheat to 600-650°C and hold for 2-6 hours, then cool to ~550°C and hold another 6-10 hours. This coarsens the α' phase slightly, sharpening the composition difference between α and α' and increasing coercivity. Total temper cycle: 8-16 hours.
7. **Magnetic testing**: Measure B-H curve on a hysteresisgraph. Accept Alnico 5 at: Br ≥ 1.25 T, Hc ≥ 48 kA/m (600 Oe), (BH)max ≥ 40 kJ/m³ (5 MGOe).

**Alnico 8/9 (high-coercivity variants)**: Add 5-8% titanium, increase cobalt to 34-36%, reduce aluminum to 6-7%. Titanium forms TiC precipitates that increase coercivity to 120-160 kA/m but reduce remanence to 0.8-0.9 T. The higher coercivity makes these grades resistant to demagnetization in motor applications.

### Ferrite (Ceramic) Permanent Magnets

Barium hexaferrite (BaFe₁₂O₁₉) and strontium hexaferrite (SrFe₁₂O₁₉) are oxide ceramics, not metals. They are included here because they are the most widely produced permanent magnets by tonnage — cheap, chemically inert, and operable up to ~250°C without irreversible demagnetization. Their magnetic hardness arises from the magnetoplumbite crystal structure with strong uniaxial magnetocrystalline anisotropy.

**Wet process for anisotropic ferrite magnets**:

1. **Mix**: Blend iron oxide (Fe₂O₃) and barium carbonate (BaCO₃) in a 5.5:1 to 6.0:1 molar ratio (slight excess Fe₂O₃). Mill together in a ball mill with water for 4-8 hours to achieve particle size <5 μm.
2. **Calcine**: Dry the mixture, then fire in a rotary kiln or periodic kiln at 1200-1300°C for 1-3 hours. Reaction: BaCO₃ + 6Fe₂O₃ → BaFe₁₂O₁₉ + CO₂. The resulting hexaferrite powder is hard and partially sintered.
3. **Coarse crush**: Jaw crush or ball mill the calcined cake back to powder.
4. **Fine milling**: Wet ball mill in water for 10-20 hours to achieve 0.5-1.5 μm particle size. This is critical — single-domain particle size for hexaferrite is ~0.5-1.0 μm. Particles below this size are single-domain and contribute maximum coercivity.
5. **Wet press in magnetic field**: De-water the slurry to a paste. Press in a steel die at 30-60 MPa while applying a magnetic field of ≥400 kA/m (5000 Oe) perpendicular to the pressing direction. The field aligns the platelike hexaferrite particles with their c-axes parallel. This produces anisotropic magnets (preferred direction). Pressing without a field produces isotropic magnets with 40-50% lower (BH)max.
6. **Sinter**: Fire pressed compacts in air at 1100-1250°C for 1-4 hours. Shrinkage is 12-18% linear. Density reaches 4.8-5.0 g/cm³ (95-98% theoretical). Sintering develops the magnetic properties — grain growth above the single-domain size reduces coercivity, so temperature and time must be controlled.
7. **Grind to tolerance**: Diamond grind mating surfaces to ±0.05 mm flatness. Ferrite is brittle — grinding is the only practical machining method.
8. **Magnetize**: Impulse magnetize in a capacitive discharge fixture at ≥1600 kA/m (20 kOe) to saturate.

## Quantitative Parameters

### Silicon Steel Magnetic Properties

| Grade | Si (%) | Thickness (mm) | Core Loss at 1.5 T, 50 Hz (W/kg) | B₅₀ (T) | Resistivity (μΩ·cm) | Application |
|-------|--------|-----------------|-----------------------------------|----------|----------------------|-------------|
| Non-oriented, 1% Si | 0.8-1.5 | 0.50 | 4.5-6.0 | 1.65-1.72 | 25-30 | Small motors, relays |
| Non-oriented, 2.5% Si | 2.0-3.0 | 0.50 | 3.0-4.0 | 1.58-1.65 | 40-50 | Industrial motors |
| Non-oriented, 3.2% Si | 3.0-3.5 | 0.35 | 2.0-2.8 | 1.55-1.62 | 50-58 | Large motors, generators |
| Grain-oriented, regular | 2.9-3.3 | 0.30 | 0.80-1.00 (at 1.7 T, 50 Hz) | 1.82-1.88 (in RD) | 45-50 | Power transformers |
| Grain-oriented, high B | 2.9-3.3 | 0.23 | 0.70-0.85 (at 1.7 T, 50 Hz) | 1.88-1.92 (in RD) | 45-50 | High-efficiency transformers |

### Permanent Magnet Properties

| Type | Br (T) | Hc (kA/m) | (BH)max (kJ/m³) | Max operating temp (°C) | Density (g/cm³) |
|------|--------|-----------|------------------|-------------------------|------------------|
| Alnico 2 | 0.70-0.75 | 45-50 | 10-13 | 450 | 7.0 |
| Alnico 5 (anisotropic) | 1.25-1.35 | 48-55 | 40-45 | 525 | 7.3 |
| Alnico 8 | 0.80-0.90 | 120-160 | 32-44 | 550 | 7.3 |
| Ba-ferrite (anisotropic) | 0.35-0.42 | 180-240 | 24-32 | 250 | 4.9 |
| Sr-ferrite (anisotropic) | 0.38-0.45 | 200-280 | 28-36 | 250 | 4.9 |

### Lamination Processing Parameters

| Parameter | Non-oriented | Grain-oriented |
|-----------|-------------|----------------|
| Strip thickness | 0.35-0.65 mm | 0.23-0.35 mm |
| Stamping tolerance | ±0.03 mm | ±0.02 mm |
| Burr height (max) | 0.03 mm | 0.02 mm |
| Interlaminar resistance | ≥5 Ω·cm² | ≥5 Ω·cm² |
| Annealing temperature (post-stamp) | 750-800°C | 780-830°C |
| Annealing atmosphere | N₂/H₂ or vacuum | Dry H₂ |
| Stacking factor | 0.95-0.97 | 0.95-0.97 |

### Alnico Heat Treatment Cycle

| Step | Temperature (°C) | Duration | Atmosphere | Cooling Rate |
|------|-------------------|----------|------------|-------------|
| Homogenize | 1200-1250 | 20-40 min | H₂ or vacuum | — |
| Spinodal decomposition | 1250→600 | 8-12 hours | Air or inert | 0.5-2.0 °C/min (field applied 900→600°C) |
| Temper stage 1 | 600-650 | 2-6 hours | Air | — |
| Temper stage 2 | 540-560 | 6-10 hours | Air | — |

## Scaling Notes

**Minimum viable scale**: A single induction furnace (50-100 kg capacity) can produce enough silicon steel for small motor and transformer laminations. Post-stamping annealing in a 10-50 kg batch furnace is adequate for pilot-scale production of 100-500 motors per year.

**Scaling to industrial output**: Power transformer core production (grain-oriented steel) requires continuous cold-rolling mills (strip width 800-1200 mm), continuous annealing lines running at 20-80 m/min, and coil weights of 5-20 tonnes. This represents a capital investment comparable to a small [steelmaking](steelmaking.md) minimill — justified only when regional demand for transformers and large motors exceeds ~10 MVA/year.

**Ferrite magnet scaling**: The calcination step is the bottleneck. Rotary kilns with 500-2000 kg/hour throughput serve most regional demand. Fine milling in continuous ball mills scales linearly — add more mills in parallel. Pressing and sintering use the same equipment as [technical ceramics](../ceramics/advanced-ceramics.md), so shared infrastructure reduces capital cost.

**Key scale breakpoints**:

| Scale | Annual Output | Capital Equipment | Notes |
|-------|---------------|-------------------|-------|
| Workshop | 100-500 kg/yr silicon steel, 10-50 kg/yr magnets | Induction furnace, small rolling mill, batch furnace | Enough for experimental motors, prototype transformers |
| Small factory | 50-500 tonnes/yr silicon steel, 5-50 tonnes/yr magnets | Continuous caster, Sendzimir mill, continuous anneal line | Regional motor/generator production |
| Industrial | 5000+ tonnes/yr grain-oriented strip | Full steel mill + specialty annealing | Power grid transformer cores |

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Core loss 30-50% above spec in silicon steel laminations | Incomplete decarburization — residual C >0.005% causes magnetic aging | Extend decarburizing anneal by 2-5 min; increase dew point of H₂/N₂ atmosphere to 40-50°C to accelerate C removal |
| Grain-oriented strip fails to develop Goss texture (grain size <1 mm after HT anneal) | Inhibitor content too low (MnS <0.05%) or normalization omitted | Verify S content ≥0.05% in melt; ensure normalization at 1100-1150°C precipitates fine MnS particles |
| Alnico 5 coercivity below 40 kA/m (spec: ≥48 kA/m) | Cooling rate too fast through spinodal range, or magnetic field not applied during cooling | Reduce cooling rate to 0.5-1.0°C/min from 1250→600°C; verify field strength ≥160 kA/m during 900→600°C range |
| Alnico casting shows porosity and shrinkage cavities | Pour temperature too low (<1500°C) or insufficient riser volume | Increase pour temperature to 1550-1600°C; add risers above thick sections to feed shrinkage |
| Ferrite magnet (BH)max <20 kJ/m³ (spec: ≥28 kJ/m³) | Particle size after fine milling >2 μm — particles are multi-domain | Extend wet ball milling to 15-20 hours; target 0.8-1.2 μm median particle size |
| Laminations short electrically after stacking | Burr height exceeds 0.03 mm, or insulating coating damaged during stamping | Sharpen or replace stamping die; add varnish coating to stamped laminations before stacking |
| Transformer core hum exceeds 60 dB at rated flux | Magnetostriction too high — wrong grade or insufficient stress-relief anneal | Use grain-oriented steel; verify post-stamping anneal at 780-830°C removes stamping strain |
| Alnico magnet partially demagnetized after machining | Excessive heat during grinding (>500°C) or mechanical shock to thin sections | Use light grinding passes with coolant; avoid impact during handling; remagnetize after machining if needed |

## Safety & Hazards

- **Hydrogen atmosphere furnaces**: Decarburizing and high-temperature annealing use H₂/N₂ mixtures. Hydrogen ignites at 4-75% concentration in air — explosive. Leak detection with thermal conductivity sensors mandatory. Purge furnace with N₂ before introducing H₂ on heat-up and before opening on cool-down. Maintain furnace shell at positive pressure to prevent air ingress. Flashback arrestors on all hydrogen supply lines.
- **Cobalt and nickel dust (alnico grinding)**: Inhalation of cobalt dust causes hard metal lung disease (pulmonary fibrosis). Nickel dust is a sensitizer and carcinogen (IARC Group 1). Local exhaust ventilation at all grinding stations. Respiratory protection (P100 filters) when maintaining grinding equipment. Air monitoring to keep Co below 0.02 mg/m³ TWA (OSHA PEL).
- **Ferrite powder inhalation**: Fine iron oxide and barium carbonate dust (<10 μm) during milling and pressing. Barium compounds are toxic (soluble Ba²⁺ affects cardiac muscle). Use enclosed milling systems with dust collection. Wash hands before eating. Maintain barium compound exposure below 0.5 mg/m³ TWA (ACGIH TLV).
- **Hot stamping and burr handling**: Silicon steel laminations at stamping press speed produce sharp burrs that cut skin. Anti-puncture gloves (Kevlar or equivalent) mandatory for handling stamped laminations. Deburr or tumble laminations before assembly.
- **High magnetic fields during alnico field-treating**: The solenoids used to apply the aligning field during spinodal cooling produce fields of 160-320 kA/m. Keep ferromagnetic objects (tools, watches, implants) at least 1 m from the coil. Pacemaker wearers must not approach. Secure the workpiece — loose steel tools become projectiles in the fringing field.

## Quality Control

**Silicon steel laminations**:
- **Core loss test**: Epstein frame (25 cm) or single-sheet tester. Measure W/kg at 1.5 T and 50 Hz for non-oriented, 1.7 T and 50 Hz for grain-oriented. Accept/reject against grade specification (e.g., ≤1.0 W/kg for M0H-30 grain-oriented at 1.7 T/50 Hz).
- **Coating resistance**: Measure interlaminar resistance per ASTM A717. Minimum 5 Ω·cm² for standard coatings. Low resistance → eddy currents between laminations → overheating.
- **Burr height**: Measure stamped edge with dial indicator or optical comparator. Maximum 0.03 mm for non-oriented, 0.02 mm for grain-oriented. Excess burr shorts laminations in the stack.
- **Dimensional tolerance**: Thickness ±0.02 mm on strip; flatness <2 mm/m on annealed laminations.

**Alnico magnets**:
- **B-H hysteresis loop**: Full loop measurement on permeameter or hysteresisgraph per ASTM A977. Verify Br, Hc, and (BH)max meet grade minimums. Test 5% of production batch, minimum 3 magnets.
- **Dimensional inspection**: Grind surfaces to ±0.05 mm flatness. Overall dimensions ±0.10 mm. Air-gap faces must be parallel within 0.05 mm over the full face.
- **Brinell hardness**: 300-400 HBW for Alnico 5. Lower hardness indicates incomplete spinodal decomposition (under-tempered).

**Ferrite magnets**:
- **Density measurement**: Weigh and measure volume. Accept 4.7-5.0 g/cm³ (95-98% theoretical). Low density indicates incomplete sintering → low Br.
- **B-H measurement**: Same as alnico. Verify (BH)max ≥28 kJ/m³ for standard anisotropic Ba-ferrite.
- **Visual inspection**: No cracks visible at 5× magnification. Ferrite is brittle — cracks propagate to fracture under magnetic cycling stress.

## Variations and Alternatives

**Soft magnetic alternatives to silicon steel**:

| Material | Max permeability | Saturation (T) | Core loss (W/kg at 1.5 T/50 Hz) | Complexity | Use case |
|----------|-----------------|----------------|----------------------------------|------------|----------|
| Pure iron (ARMCO) | 5,000-10,000 | 2.15 | 8-12 | Lowest | DC electromagnets, relays |
| Low-carbon steel (1020) | 2,000-4,000 | 2.10 | 10-15 | Lowest | Non-critical magnetic circuits |
| Non-oriented Si steel (3%) | 5,000-8,000 | 1.95 | 2.0-2.8 | Medium | AC motors, generators |
| Grain-oriented Si steel | 30,000-60,000 (RD) | 2.03 | 0.8-1.0 | High | Power transformers |
| Permalloy (80Ni-20Fe) | 100,000+ | 0.80 | <0.5 at low B | Very high | Instrument transformers, sensors |
| Amorphous metal (Fe-B-Si) | ~30,000 | 1.56 | 0.2-0.4 | Very high | High-efficiency distribution transformers |

**Permanent magnet alternatives to alnico and ferrite**:

| Type | (BH)max (kJ/m³) | Cost/complexity | Temperature stability | Bootstrap availability |
|------|------------------|-----------------|----------------------|----------------------|
| Alnico 5 | 40-45 | Medium | Excellent (to 525°C) | Industrial era |
| Ba/Sr ferrite | 24-36 | Low | Good (to 250°C) | Industrial era |
| SmCo (samarium-cobalt) | 120-200 | Very high | Excellent (to 300°C) | Requires rare earth separation |
| NdFeB (neodymium-iron-boron) | 200-400 | Very high | Poor (to 80-150°C without Co) | Requires rare earth separation + advanced processing |

For bootstrap purposes, alnico and ferrite are the practical choices. Rare-earth magnets (SmCo, NdFeB) offer superior performance but require solvent extraction of rare earth elements from ore — a capability that demands extensive chemical infrastructure well beyond basic metallurgy.

**Historical note**: Before silicon steel, transformer cores were made from soft iron wire bundles (1880s-1900s). The wire form broke up eddy currents without the need for thin laminations. Silicon steel replaced wire cores when rolling mills capable of producing thin gauge strip became available (1900-1910). Early permanent magnets were hardened steel (tungsten steel, 6% W, or chrome steel, 3-6% Cr) — replaced by alnico from the 1930s onward due to vastly superior coercivity.

## See Also

- [Iron & Steel Production](iron-steel.md) — base material for all ferromagnetic alloys
- [Steelmaking](steelmaking.md) — electric furnace steel and alloy production
- [Specialty Alloys](alloys.md) — nickel and cobalt alloy processing
- [Metal Forming](forming.md) — cold rolling and strip production
- [Metal Casting](casting.md) — investment casting for alnico magnets
- [Ceramics](../ceramics/advanced-ceramics.md) — shared sintering infrastructure for ferrite magnets
- [Electric Motor](../energy/electric-motor.md) — primary consumer of magnetic laminations and magnets
- [Generator](../energy/generator.md) — stator and rotor magnetic materials
- [Power Distribution](../energy/power-distribution.md) — transformer core materials

*Part of the [Bootciv Tech Tree](../../index.md) • [Metals](./index.md) • [All Domains](../../index.md)*
