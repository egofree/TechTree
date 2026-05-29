# High-Purity Chemicals: 9N+ Purification

> **Node ID**: ultra-pure.high-purity-chemicals
> **Domain**: [Ultra-Pure Materials](./index.md)
> **Dependencies**: [Chemistry / Acids](../chemistry/acids.md), [Solvents](../chemistry/solvents.md), [Ultra-Pure Water](upw.md), [Polymers](../polymers/index.md)
> **Enables**: [`silicon.purification`](../silicon/purification.md), [`photolithography.fab-processes`](../photolithography/fab-processes.md)
> **Timeline**: Years 40-80
> **Outputs**: high_purity_acids, high_purity_solvents, high_purity_gases
> **Tags**: materials=[chemicals], era=semiconductor, critical


Semiconductor fabrication uses dozens of chemicals at purity levels 6-9 orders of magnitude above standard reagent grade. Electronic-grade hydrofluoric acid (HF) must contain less than 100 ppt (parts per trillion) of each metallic impurity — Fe, Cu, Ni, Cr, Zn, Na, K, Ca, and dozens of others. Standard ACS reagent-grade HF typically contains 0.5-5 ppm of metallic impurities — 5,000-50,000× too contaminated for wafer processing.

The transition from industrial-grade (95-99.5%, or 2-3N purity) to electronic-grade (9N+ purity) is not incremental improvement. It requires fundamentally different equipment, materials, environments, and analytical capabilities. Standard distillation in glass apparatus introduces trace metals from the glass itself. Sub-boiling distillation in PTFE or quartz apparatus is the minimum entry point for electronic-grade production.

## Prerequisites

- [Acids](../chemistry/acids.md) — bulk acid production as starting material
- [Solvents](../chemistry/solvents.md) — industrial solvent production
- [Ultra-Pure Water](upw.md) — 18.2 MΩ·cm water for rinsing and dilution
- [Polymers](../polymers/index.md) — PTFE and PFA for contamination-free equipment

## Purity Grades

| Grade | Purity | Metallic Impurities | Use Case |
|-------|--------|-------------------|----------|
| **Technical** | 95-99% (2N) | 100-10,000 ppm | Industrial processing, cleaning |
| **ACS Reagent** | 99.5-99.9% (3N) | 1-100 ppm | Laboratory analysis |
| **Semiconductor Grade (SEMI C1)** | 99.99% (4N) | <1 ppm | Wafer cleaning (RCA SC-1/SC-2) |
| **Electronic Grade (SEMI C35)** | 99.9999% (6N) | <1 ppb | Etching, deposition |
| **Ultra-High Purity (SEMI C7/C8)** | 99.99999%+ (7-8N) | <100 ppt | Critical etch, gate oxide |
| **Tru-Electronic / Ultra-Trace** | 99.9999999% (9N) | <10 ppt | Advanced node (<28 nm) processing |


## Sub-Boiling Distillation

The foundational technique for electronic-grade chemical production. Unlike conventional distillation (which boils the liquid, aerosolizing impurities that contaminate the distillate), sub-boiling distillation operates below the boiling point using infrared radiation or heated surfaces.

**Strengths**:
- Removes 99.99%+ of metallic impurities — single pass produces 6-7N purity from 3N feedstock
- No aerosol formation prevents non-volatile impurity carryover
- Applicable to wide range of acids: HF, HNO₃, HCl, H₂SO₄, CH₃COOH

**Weaknesses**:
- Low throughput: 50-500 mL/hr per unit — production scale requires massive parallel arrays
- Requires PTFE or quartz equipment (borosilicate glass leaches Na, K, Ca)
- Temperature control critical for H₂O₂ (decomposes above 70°C)

## Isothermal Distillation

**Principle**: A heated surface (quartz or PTFE) creates a thin film of evaporating liquid at 5-15°C below the normal boiling point. Vapor condenses on a cooled surface without entraining non-volatile impurities (metals, particulates). The gentle evaporation prevents aerosol formation and bumping.

**Equipment**:
- Vessel: High-purity quartz or PTFE (PFA) — no glass (leaches Na, K, Ca)
- Heater: Infrared lamps or encapsulated heating elements (no exposed metal)
- Condenser: Quartz or PTFE — continuous slope prevents reflux contamination
- Collection vessel: PFA or quartz, sealed from atmosphere

**Performance**: Removes 99.99%+ of metallic impurities. Starting with 3N ACS reagent-grade material, a single sub-boiling pass produces 6-7N purity. Two passes achieve 8-9N.

**Throughput**: Low — typically 50-500 mL/hr for a single unit. Production-scale sub-boiling systems use multiple parallel units. A 10 L/day production system requires 20-40 sub-boiling stills.

**Applicable chemicals**: Hydrofluoric acid (HF), nitric acid (HNO₃), hydrochloric acid (HCl), sulfuric acid (H₂SO₄), acetic acid (CH₃COOH), ammonium hydroxide (NH₄OH), hydrogen peroxide (H₂O₂).

## Isothermal Distillation

For acids that cannot be sub-boiled (e.g., HF is too hazardous at elevated temperatures, HCl forms an azeotrope), isothermal (or "isopiestic") distillation purifies without heating.

**Strengths**:
- No heating above ambient — prevents thermal decomposition of sensitive chemicals
- Produces 7-8N purity acids, particularly effective for HCl and HF
- Simple equipment: sealed PTFE vessel with two compartments

**Weaknesses**:
- Slower than sub-boiling distillation — equilibration takes hours to days
- Limited to volatile acids (HCl, HF) — not applicable to non-volatile chemicals
- Lower throughput per unit volume of equipment

**Principle**: Place the impure acid and high-purity water in separate containers within a sealed vessel at constant temperature. The volatile component (e.g., HCl gas, HF vapor) equilibrates between the two containers via the vapor phase. The water absorbs the purified volatile component. Non-volatile impurities (metals) remain in the source container.

**Equipment**: Sealed PTFE or PFA vessel with two compartments. Temperature control at 25-40°C. No heating above ambient — prevents decomposition.

**Performance**: Produces 7-8N purity acids. Particularly effective for HCl (which readily transfers as gas) and HF.

## Zone Refining

Originally developed for semiconductor silicon purification (see [Silicon Purification](../silicon/purification.md)), zone refining also purifies solid chemicals by passing a narrow molten zone through a solid rod.

**Principle**: A molten zone traverses a solid ingot. Impurities that lower the melting point segregate into the molten zone and are swept to one end. Impurities that raise the melting point are left behind. Multiple passes (10-50+) concentrate impurities at the ends; the middle section is cut out as the purified product.

**Applicable chemicals**: Organic solvents that can be frozen (benzene, toluene, naphthalene). Solid acids (oxalic acid, benzoic acid). Limited applicability to most semiconductor chemicals.

**Performance**: Can achieve 10-11N purity on suitable materials. Extremely slow — days per pass.

## Ion Exchange Purification

Ion exchange resins remove trace ionic contaminants from chemical solutions. Unlike the ion exchange used in UPW (see [Ultra-Pure Water](upw.md)), chemical purification ion exchange must be compatible with aggressive chemical environments.

**Resin selection**:
- For acids: Strongly acidic cation exchange resin in hydrogen form (removes metal cations from acid solutions)
- For bases: Strongly basic anion exchange resin in hydroxide form (removes anionic contaminants)
- For solvents: Mixed-bed ion exchange with solvent-compatible resin matrices

**Equipment**: PTFE or PFA columns. Acid-washed quartz media support. All-wetted surfaces are fluoropolymer.

**Performance**: Reduces metallic impurities from ppm to sub-ppb levels. Must be combined with sub-boiling distillation for ppt-level purity (ion exchange alone cannot reach below ~0.1 ppb due to resin leaching).

## Membrane Purification

Nanofiltration and ultrafiltration membranes remove particles, colloids, and high-molecular-weight organic contaminants from chemical solutions.

**Applications**: Particle removal from concentrated acids. Colloidal silica removal from HF. Organic removal from solvents.

**Membrane materials**: PTFE, PFA, or PVDF membranes in fluoropolymer housings. Cellulose and polyamide membranes dissolve in many semiconductor chemicals.

## Absorption and Adsorption

**Gas-phase purification**: For electronic-grade gases (H₂, N₂, O₂, Ar), purification uses:
- Catalytic getters (Pd, Zr-V-Fe alloys) to remove O₂, H₂O, CO, CO₂
- Molecular sieves (zeolite 3Å, 4Å, 13X) for H₂O and CO₂ removal
- Activated carbon for hydrocarbon removal
- Palladium membrane diffusion for ultra-pure hydrogen (only H₂ permeates Pd at 300-400°C)

**Liquid-phase adsorption**: Activated carbon (acid-washed, ultra-pure grade) removes organic contaminants from acids and solvents.


## Electronic-Grade Hydrofluoric Acid (HF)

HF is the single most critical chemical in semiconductor fabrication — used for SiO₂ etching, wafer cleaning, and oxide stripping. Electronic-grade HF must contain <100 ppt of each metallic impurity.

**Feedstock**: 49% HF (technical grade, ~2N purity, ~50 ppm total metals).

**Purification sequence**:
1. **Pre-filtration**: 0.2 μm PTFE membrane filter removes particulates.
2. **Cation exchange**: Strongly acidic cation resin in PTFE column removes >99% of metal cations (Fe, Cu, Ni, Cr, Na, K, Ca, Mg). Reduces metals to <1 ppb each.
3. **Sub-boiling distillation**: PTFE sub-boiling still at 80-90°C (HF bp 112°C at 49%). Produces 7-8N HF. Non-volatile impurities (metals, particulates) remain in the boiling flask.
4. **Second sub-boiling pass** (for 9N+): Second distillation in a fresh PTFE still. Achieves <10 ppt per metallic impurity.
5. **Final filtration**: 0.05 μm PTFE membrane filter in PFA housing.
6. **Bottling**: Under cleanroom conditions (ISO 4) into pre-cleaned PFA bottles. Each bottle is leached with electronic-grade HF before filling.

**Safety**: HF is extremely hazardous — penetrates skin, binds calcium, causes deep tissue necrosis and potentially fatal hypocalcemia. All HF handling requires: calcium gluconate gel on-site, full PPE (face shield, HF-resistant gloves, apron), dedicated fume hood with HF-rated scrubber, and emergency shower within 10 seconds travel distance.

## Electronic-Grade Hydrogen Peroxide (H₂O₂)

H₂O₂ is a key reagent in RCA wafer cleaning (SC-1 and SC-2, see [Solvents](../chemistry/solvents.md)). Electronic-grade H₂O₂ must contain <100 ppt metals.

**Feedstock**: 30-35% H₂O₂ (industrial grade, ~3N purity).

**Purification sequence**:
1. **Stabilizer removal**: Industrial H₂O₂ contains stannate and phosphonate stabilizers. Pass through ion exchange resin (anion form) to remove stabilizer anions.
2. **Cation exchange**: Remove metal cations to <1 ppb.
3. **Sub-boiling distillation**: PTFE or quartz still at 50-60°C under vacuum (H₂O₂ decomposes above 70°C — temperature control is critical). Vacuum of 30-50 mbar reduces boiling point to safe range.
4. **Concentration adjustment**: Dilute with ultra-pure water to target concentration (30% or 35%).
5. **Final filtration**: 0.05 μm PES membrane filter.
6. **Storage**: PFA containers, refrigerated (4-10°C) to slow decomposition. Shelf life: 3-6 months.

**Decomposition hazard**: H₂O₂ decomposes to water and oxygen (exothermic). Trace metals (Fe, Cu, Mn) catalyze rapid decomposition. Electronic-grade H₂O₂, paradoxically, is MORE stable than industrial grade because metallic catalysts have been removed.

## Electronic-Grade Isopropyl Alcohol (IPA)

IPA is used for wafer drying after rinsing (Marangoni drying) and as a cleaning solvent. Electronic-grade IPA requires <1 ppb metals, <1 ppb TOC.

**Feedstock**: 99.5% IPA (ACS grade, ~3N purity).

**Purification sequence**:
1. **Distillation**: Fractional distillation in quartz column (30 theoretical plates). Removes water, organic impurities, and most metals.
2. **Molecular sieve drying**: Zeolite 3Å column removes residual water to <50 ppm. IPA-water azeotrope (87.7% IPA) must be broken.
3. **Sub-boiling distillation**: Quartz still for final metal removal to ppt levels.
4. **Final filtration**: 0.05 μm PTFE membrane filter.
5. **Storage**: Nitrogen-purged PFA containers.

## Electronic-Grade Acids (HCl, HNO₃, H₂SO₄)

**Hydrochloric acid**: Isothermal distillation of ACS-grade 37% HCl. HCl gas transfers to UPW in sealed PTFE vessel. Produces 8-9N HCl. Used for RCA SC-2 clean and pre-diffusion clean.

**Nitric acid**: Sub-boiling distillation of ACS-grade 70% HNO₃ in quartz still. Two passes achieve 8N. Used for metal stripping and wafer cleaning.

**Sulfuric acid**: Sub-boiling distillation of ACS-grade 96% H₂SO₄ in quartz still. Extremely aggressive — requires all-quartz equipment (H₂SO₄ attacks PTFE above 150°C). Used for photoresist stripping (piranha clean: H₂SO₄ + H₂O₂).

## Cleanroom Packaging and Handling

Electronic-grade chemicals must be packaged and handled under contamination-controlled conditions to prevent recontamination after purification.

**Container materials**: PFA (perfluoroalkoxy) bottles for HF and aggressive acids. HDPE (high-density polyethylene) for less aggressive chemicals (H₂O₂, IPA, NH₄OH). All containers pre-cleaned by leaching with electronic-grade acid and rinsing with UPW.

**Filling environment**: ISO Class 4 (Class 10) cleanroom or better. Personnel in full cleanroom garments. Filling equipment with laminar flow HEPA filtration.

**Quality control**: Each batch is tested for metallic impurities (ICP-MS, see [Analytical Verification](analytical-verification.md)), TOC, particles, and concentration before release. Certificate of analysis (CoA) accompanies each lot.

**Shelf life**: Electronic-grade acids degrade over time as they leach trace contaminants from container walls and absorb atmospheric impurities. Typical shelf life: 6-12 months for acids in sealed PFA containers, 3-6 months for H₂O₂.

## Materials of Construction

All wetted surfaces in purification and storage equipment must be evaluated for trace metal leaching.

| Component | Electronic-Grade Material | Comments |
|-----------|--------------------------|----------|
| Still vessels | Quartz (fused silica), PFA | No borosilicate glass (leaches B, Na) |
| Columns | PTFE, PFA | No PVC, steel |
| Tubing | PFA, PTFE | Electropolished 316L SS acceptable for some acids |
| Valves | PTFE diaphragm | No metal-contact valves |
| Filters | PTFE, PES membranes | In PFA housings |
| Storage | PFA, HDPE (H₂O₂ only) | No glass, no metal |
| Gaskets | PTFE, Kalrez (FFKM) | No EPDM, Viton |

## Cross-Domain Dependencies

- **[Chemistry / Acids](../chemistry/acids.md)**: Produces bulk industrial-grade acids (2-3N) that serve as feedstock for electronic-grade purification.
- **[Solvents](../chemistry/solvents.md)**: Industrial solvents as feedstock; H₂O₂ via anthraquinone process.
- **[Ultra-Pure Water](upw.md)**: UPW is used for dilution, rinsing, and isothermal distillation in electronic-grade chemical production.
- **[Polymers](../polymers/index.md)**: PFA, PTFE, PES, PVDF for all wetted surfaces.
- **[Photolithography / Cleanrooms](../photolithography/cleanrooms.md)**: Packaging and bottling under cleanroom conditions.
- **[Analytical Verification](analytical-verification.md)**: ICP-MS, TOC analysis, particle counting for quality control.

## Limitations

- **Low throughput**: Sub-boiling distillation produces 50-500 mL/hr per unit. Scaling to industrial production (thousands of liters per day) requires massive parallel arrays of distillation units.
- **High cost**: Electronic-grade chemicals cost 10-100× more than ACS reagent grade. Electronic-grade HF: ~$50-100/L vs. ACS grade ~$5/L. The purification cost is dominated by the sub-boiling distillation energy and the expensive PTFE/quartz equipment.
- **Shelf life**: Electronic-grade purity degrades over time. Even in PFA containers, trace metals slowly leach from container walls. Must use within manufacturer's specified shelf life.
- **Safety**: The chemicals involved (HF, concentrated H₂SO₄, fuming HNO₃) are extremely hazardous even without considering their ultra-pure handling requirements. The combination of extreme toxicity and extreme purity demands creates a unique safety management challenge.
- **Single-source risk**: Many electronic-grade chemicals are produced by only 2-3 suppliers worldwide. Supply disruption is a significant risk for semiconductor fabrication.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Metallic contamination above spec | Leaching from container walls or transfer lines | Use PFA or PTFE containers only; replace stainless fittings with PFA; test container leach rate |
| Purity degrading during storage | Container surface leaching or seal contamination | Rotate stock within shelf life; verify container material compatibility; store in cleanroom conditions |
| Sub-boiling distillation too slow | Heat input too low or condenser too warm | Increase heater to just below boiling point; verify condenser coolant flow; do NOT increase to full boil |
| Particle count exceeding spec | Dust ingress or equipment shedding | Process in ISO Class 4 cleanroom; install 0.05 μm point-of-use filter; clean all surfaces before use |
| Inconsistent ICP-MS results | Sample contamination during collection | Use dedicated PFA sampling bottles; handle with powder-free gloves; run blanks alongside samples |
| Organic contamination (high TOC) | Solvent residues or atmospheric organics | Install activated carbon polish; process under N₂ blanket; verify cleaning procedures for apparatus |

## See Also

- [Ultra-Pure Water](upw.md) — 18.2 MΩ·cm water for wafer rinsing
- [Analytical Verification](analytical-verification.md) — PPT-level analysis for quality control
- [Solvents](../chemistry/solvents.md) — industrial solvent production and H₂O₂ via anthraquinone process
- [Chemistry / Acids](../chemistry/acids.md) — bulk acid production
- [Silicon Purification](../silicon/purification.md) — Siemens process and zone refining for semiconductor-grade silicon
- [Photolithography Fab Processes](../photolithography/fab-processes.md) — the processes consuming these chemicals

[← Back to Ultra-Pure Materials](index.md)
