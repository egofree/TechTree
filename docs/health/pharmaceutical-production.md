# Pharmaceutical Production

> **Node ID**: health.pharmaceutical-production
> **Domain**: [Health](./index.md)
> **Dependencies**: [`health.pharmacology`](pharmacology.md), [`chemistry.distillation`](../chemistry/distillation.md), [`health.sanitation`](sanitation.md)
> **Enables**: [`health.medicine`](medicine.md), [`health.surgery-basics`](surgery-basics.md)
> **Timeline**: Years 15-100+
> **Outputs**: pharmaceuticals, dosage_forms, quality_controlled_drugs, sterile_pharmaceuticals
> **Critical**: Yes — without reliable pharmaceutical production, disease treatment depends on variable plant preparations and infection mortality remains high

## Overview

Pharmaceutical production covers the scaled manufacture of drugs from extraction through final dosage form, with quality control at each stage. This capability extends [pharmacology](pharmacology.md) — which covers drug sources and basic preparation — into reproducible, quality-controlled production suitable for treating an entire community. The transition from compounding individual doses to batch manufacturing is the inflection point where pharmaceutical capability becomes a public health infrastructure rather than a cottage craft.

The key challenge in bootstrap pharmaceutical production is quality assurance. Without modern analytical instruments (HPLC, mass spectrometry), drug potency and purity must be verified through simpler methods: melting point determination, thin-layer chromatography, microbial limit testing, and dissolution testing. These methods are adequate for the drug classes available in a bootstrap setting: analgesics, antimalarials, antiseptics, anesthetics, and basic antibiotics (sulfonamides).

## Prerequisites

### Materials

- Active pharmaceutical ingredients (APIs): extracted from plants or synthesized (see [pharmacology](pharmacology.md))
- Excipients: starch, lactose, sucrose, gelatin, talc, magnesium stearate
- Solvents: ethanol (95%), purified water, glycerol
- Packaging: amber glass bottles, cork or glass stoppers, wax for sealing, paper labels

### Tools and Equipment

- Tablet press: single-punch or rotary (see [machine-tools](../machine-tools/index.md))
- Capsule filling machine (manual or semi-automatic)
- Mixing equipment: V-blender or mortar and pestle for small batches
- Drying oven: 40-105°C with temperature control
- Sieve set: mesh sizes 20-100 (840-150 μm)
- Analytical balance: 0.1-0.01 g sensitivity
- Autoclave: for sterile product preparation
- Glassware: flasks, beakers, graduated cylinders, volumetric flasks

### Knowledge

- Pharmaceutical calculations: dosage calculations, dilution formulas, yield calculations
- Good Manufacturing Practices (GMP) fundamentals: documentation, cross-contamination prevention, cleaning validation
- Stability testing protocols and shelf-life estimation
- Quality control testing methods: TLC, melting point, dissolution, microbial limits

### Infrastructure

- Clean production area (not necessarily cleanroom, but separate from dusty/noisy work)
- Temperature-controlled storage (cool, dry location; refrigeration for some products)
- Purified water supply (distilled or deionized)

## Bill of Materials

| Material | Quantity per 1000 Tablets | Source | Alternatives |
|----------|--------------------------|--------|-------------|
| Active ingredient (e.g., aspirin powder) | 300-900 g | [Chemistry](../chemistry/index.md) — Kolbe-Schmitt synthesis | Ground willow bark (variable potency) |
| Binder (starch paste, 10% w/v) | 50-100 g dry starch | [Agriculture](../agriculture/index.md) — grain processing | Acacia gum, gelatin solution, honey |
| Filler/diluent (lactose or dicalcium phosphate) | 200-500 g | Dairy processing or mining | Starch, sucrose, calcium carbonate |
| Disintegrant (starch or microcrystalline cellulose) | 20-50 g | Grain processing | No disintegrant (slower dissolution) |
| Lubricant (talc or magnesium stearate) | 5-15 g | Mining or chemical synthesis | Steric acid, sodium benzoate |
| Glaze/coating (sugar solution or shellac) | 50-100 g | Sugar refining or [beekeeping](../animals/beekeeping.md) | None (uncoated tablets) |

## Process Description

### Tablet Manufacturing

1. **Weigh ingredients**: Weigh API and all excipients on analytical balance. Record each weight in batch record. Verify calculations: target tablet weight × number of tablets = total batch weight. Check: all ingredients must total to target batch weight.
2. **Mix dry powders**: Add API, filler, and disintegrant to mixing vessel. Mix for 10-15 minutes until uniform. For potent drugs (API <50 mg per tablet), use geometric dilution: mix API with equal weight of filler, then double mixture with more filler, repeat until all filler incorporated. This prevents dose variation from poor mixing.
3. **Add binder**: Prepare starch paste (10% starch in water, heated to 70-80°C with stirring until translucent). Add binder solution gradually to dry mix while stirring. Continue mixing until uniform wet mass forms. Test: squeeze a handful — it should form a coherent ball that breaks cleanly when pressed (not too wet, not too dry).
4. **Granulate**: Pass wet mass through a #12 sieve (1.7 mm openings) to form granules. Spread granules on trays. Dry in oven at 50-60°C for 4-12 hours. Turn granules periodically for uniform drying. Test: moisture content <3% (compare weight before and after further drying at 105°C for 2 hours).
5. **Size granules**: Pass dried granules through a #20 sieve (840 μm). Collect fines (particles passing #40 sieve, 420 μm) and recycle them into the next batch. Add lubricant (talc, 1% by weight) and mix gently for 3-5 minutes. Over-mixing with lubricant reduces tablet strength.
6. **Compress tablets**: Set tablet press to target weight (e.g., 500 mg ±5%). Compress first 20 tablets. Weigh each individually. All must be within ±5% of target weight. Measure hardness with a tablet hardness tester (target: 4-8 kgf). Adjust compression force as needed. Test disintegration: drop one tablet into 37°C water — should disintegrate within 15 minutes.
7. **Inspect and package**: Visually inspect every tablet for defects (chipping, capping, lamination, discoloration). Reject defective tablets (>2% defect rate triggers process investigation). Package in amber glass bottles with desiccant. Label with: drug name, strength, batch number, manufacture date, expiry date, storage conditions.

### Tincture Production (Batch)

1. **Prepare plant material**: Dry plant material at 40-60°C to constant weight. Grind to coarse powder (passes #20 sieve). Record starting weight.
2. **Macerate**: Add plant material to glass vessel. Add 45-70% ethanol at 1:5 ratio (1 g plant per 5 mL solvent). Seal vessel. Label with: plant name, date, solvent, ratio.
3. **Extract**: Shake daily for 14-28 days at room temperature. Store in dark location. Longer extraction = higher yield, but diminishing returns after 21 days.
4. **Filter and press**: Decant supernatant. Press residue in cloth to recover trapped solvent. Combine all liquid. Filter through filter paper or fine cloth.
5. **Standardize**: Measure specific gravity with hydrometer (indicates ethanol content). Perform TLC to verify active compound presence (compare to reference standard). If reference standard available, adjust concentration by dilution or further extraction.
6. **Package**: Fill amber glass bottles. Seal with cork or glass stopper. Label with: plant name (botanical), preparation date, solvent concentration, batch number, dosage range, warnings.

### Sterile Liquid Production (for Injections)

1. **Prepare solution**: Dissolve drug in Water for Injection (WFI — water distilled and filtered through 0.22 μm filter). Add preservative if multi-dose vial (benzyl alcohol 0.9% or phenol 0.5%). Adjust pH to physiological range (pH 4.5-7.0 for most drugs).
2. **Filter sterilize**: Pass solution through 0.22 μm membrane filter into sterile container. This removes bacteria but not viruses or pyrogens (bacterial endotoxins).
3. **Fill aseptically**: In a clean environment, fill sterile glass vials or ampoules. Seal immediately — flame-seal ampoules, crimp rubber stoppers on vials with aluminum caps.
4. **Terminal sterilize**: Autoclave at 121°C for 15 minutes (if drug is heat-stable). For heat-labile drugs, rely on aseptic processing and filter sterilization only (higher sterility risk).
5. **Test sterility**: Incubate samples in thioglycollate broth (bacteria) and soybean-casein digest broth (fungi) at 30-35°C and 20-25°C respectively for 14 days. No growth = passes sterility test.

## Quantitative Parameters

### Tablet Manufacturing Parameters

| Parameter | Target Range | Test Method | Out-of-Spec Action |
|-----------|-------------|-------------|-------------------|
| Tablet weight | ±5% of target | Individual weighing (n=20 per batch) | Adjust fill depth on press |
| Hardness | 4-8 kgf | Tablet hardness tester | Adjust compression force |
| Disintegration time | <15 min (uncoated), <30 min (coated) | USP disintegration apparatus or warm water | Increase disintegrant; check lubricant level |
| Friability (resistance to chipping) | <1% weight loss | Rotate 20 tablets in drum at 25 RPM for 4 min | Increase binder or compression force |
| Assay (drug content) | 90-110% of label claim | TLC densitometry or titration | Recalculate batch; reject if <85% or >115% |
| Dose uniformity | 85-115% of label, RSD <6% | Weigh 10 tablets individually | Improve mixing; check geometric dilution |
| Moisture content | <3% | Loss on drying at 105°C for 2 hr | Extend drying time; add desiccant to packaging |

### Extraction Yield Benchmarks

| Plant Source | Active Compound | Solvent | Typical Yield | Purity After Recrystallization |
|-------------|----------------|---------|--------------|-------------------------------|
| Willow bark | Salicin (→ salicylic acid) | Ethanol 50% | 1.5-3% of dry bark weight | 85-95% |
| Cinchona bark | Quinine | Hot water → alkali precipitation | 2-7% total alkaloids | 90-98% as quinine sulfate |
| Opium poppy latex | Morphine | Water → NaOH precipitation → HCl recrystallization | 8-14% of dry opium | 95-99% as morphine HCl |
| Ephedra stems | Ephedrine | Water → organic solvent extraction | 0.5-2% of dry plant | 90-95% |
| Iodine from kelp | Iodine | Ash → acid extraction → sublimation | 0.1-0.5% of dry seaweed | 95-99% |

### Purity Requirements by Dosage Form

| Dosage Form | Minimum API Purity | Key Impurity Limits | Critical QC Test |
|-------------|-------------------|--------------------|-----------------| 
| Oral tablets | >95% | Heavy metals <20 ppm, residual solvent <5000 ppm | Assay (90-110%) |
| Oral liquids/tinctures | >90% | Microbial count <10⁵ CFU/g | Microbial limits, ethanol content |
| Topical preparations | >90% | Microbial count <10² CFU/g (sterile if broken skin) | Microbial limits |
| Sterile injectables | >98% | Pyrogens <5 EU/kg, sterility assured, particles <10 per mL | Sterility test, pyrogen test |
| Ophthalmic (eye) preparations | >98% | Sterility assured, particles <50 per mL | Sterility test, pH (6.5-7.5) |

## Scaling Notes

- **Apothecary scale (1-10 doses/day)**: Compounding individual prescriptions using mortar and pestle, manual capsule filling, simple molding. No tablet press needed. Quality controlled by individual practitioner. Appropriate for early bootstrap.
- **Small manufacturing (100-1000 doses/day)**: Single-punch tablet press, manual capsule filling machine, small drying oven. One production room, 2-3 workers. Quality testing with TLC, melting point, and basic microbial tests. This scale serves a community of 500-5,000 people.
- **Industrial scale (10,000+ doses/day)**: Rotary tablet press (20-40 stations, 50,000-100,000 tablets/hour), automated mixing, fluid bed dryer, automated packaging. Requires dedicated facility with HVAC, multiple production rooms. Quality control laboratory with multiple analysts. This scale requires full industrial chemistry and machine tools capability.
- **Bottleneck at every scale**: Mixing uniformity. Poor mixing produces tablets with varying doses — some too weak, some toxic. Always use geometric dilution for potent drugs. Verify mixing quality by testing tablets from beginning, middle, and end of each batch.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Capping (tablet splits horizontally) | Air entrapment, insufficient binder, excessive compression force | Pre-compress lightly before full compression; increase binder; reduce compression speed |
| Lamination (tablet splits in layers) | Same as capping, often worse with fine powders | Granulate before compression; coarser granules compress more uniformly |
| Sticking (material adheres to punch faces) | Moisture in granules, insufficient lubricant, worn punch faces | Dry granules further; increase lubricant to 2%; polish punch faces |
| Weight variation >5% | Uneven fill, granule size too variable | Improve granule size uniformity (sieve more carefully); check feed frame operation |
| Poor disintegration (>15 min) | Excessive compression force, too much binder, insufficient disintegrant | Reduce compression force; increase disintegrant to 10%; check starch paste concentration |
| Content uniformity failure | Poor mixing, large API particle size | Use geometric dilution; mill API to <150 μm before mixing; extend mixing time |
| Microbial contamination | Non-sterile water, contaminated raw materials, poor hygiene | Use purified water; test incoming raw materials; enforce hand-washing and clean clothing |
| Tablet discoloration | API degradation (oxidation, hydrolysis), moisture | Add antioxidant (ascorbic acid 0.1%); improve packaging (desiccant, amber glass); reduce moisture |

## Safety

> **WARNING**: Pharmaceutical production involves biologically active compounds that can cause serious harm if improperly manufactured, dosed, or administered. All dosing must be supervised by someone with medical training. The following safety measures are mandatory.

- **Drug-specific hazards**: Morphine and opium derivatives are potent respiratory depressants. Ether is explosive. Phenol (carbolic acid) causes chemical burns at >5% concentration. Handle all APIs with gloves in a well-ventilated area. Have specific antidotes available where they exist (e.g., calcium gluconate for HF exposure in pharmaceutical synthesis, naloxone for opioid overdose if available).
- **Cross-contamination prevention**: Produce only one drug product at a time in a given area. Clean all equipment thoroughly between products. Verify cleaning by swab testing (wipe equipment surface, test swab for API residue — must be below 10 ppm of previous product). Cross-contamination between potent drugs (e.g., morphine contamination of an aspirin batch) can cause fatal overdose.
- **Dust control**: Pharmaceutical powders form explosive dust clouds. Use local exhaust ventilation when handling dry powders. No open flames or ignition sources in production areas. Wear dust masks when weighing and mixing. Dust explosions are a real risk with starch, lactose, and other organic powders.
- **Solvent safety**: Ethanol is flammable (flash point 13°C). Use in well-ventilated areas away from ignition sources. Methanol (if used as solvent) is toxic via skin absorption and ingestion — 10 mL can cause blindness, 30 mL can be fatal. Diethyl ether forms explosive peroxides on storage — test with starch-iodide paper before use.
- **Labeling accuracy**: Every container must be labeled immediately upon filling. Mislabeled drugs kill. Use standardized label format: drug name, strength, batch number, expiry, storage conditions, warnings. Verify label against batch record before applying.

## Quality Control

- **In-process controls**: Check granule moisture (target <3%) before compression. Monitor tablet weight every 15 minutes during production run. Record compression force and tablet hardness at start, midpoint, and end of batch.
- **Finished product testing**: Every batch receives: identity test (TLC or color reaction), assay (90-110% of label claim), disintegration (<15 min), weight uniformity (n=20, RSD <3%), hardness (4-8 kgf). Sterile products additionally receive: sterility test (14-day incubation), pyrogen test (rabbit test or LAL assay if available), particulate matter count.
- **Stability testing**: Retain samples from each batch. Store at 25°C/60% RH (long-term) and 40°C/75% RH (accelerated). Test at 0, 1, 3, 6, 12 months. If product remains within specification at 40°C for 6 months → estimate 2-year shelf life at room temperature. Assign expiry dates conservatively — expired drugs may be toxic (e.g., degraded tetracycline causes Fanconi syndrome).
- **Documentation**: Batch records must include: starting material weights and lot numbers, process parameters at each step, in-process test results, yield calculations, deviations from standard procedure, final QC results, release decision with signature. Retain all batch records for minimum 2 years past product expiry date.

## Variations and Alternatives

### Dosage Form Options

| Form | Advantages | Disadvantages | Best For |
|------|-----------|---------------|---------|
| Tablets | Accurate dose, stable, easy to transport | Requires tablet press, limited drug palette | Stable APIs, community-scale production |
| Capsules | Easy to fill, masks taste, no compression heat | Requires gelatin, limited moisture protection | Heat-sensitive APIs, small batches |
| Tinctures | Simple production, stable (ethanol preserves), flexible dosing | Variable potency, ethanol content, liquid | Plant-derived drugs, early-stage production |
| Powders (sachets) | Simplest production, accurate if geometric dilution used | Unpleasant taste, moisture-sensitive | Single-dose treatments, pediatric dosing |
| Ointments/salves | Easy production, topical application | Messy, limited to surface conditions | Wound treatment, skin conditions |
| Suppositories | Alternative route when oral not possible | Temperature-sensitive manufacturing | Rectal/vaginal drug delivery, pediatric, vomiting patients |

### Historical Manufacturing Methods

- **Manual pill rolling** (pre-1800): Mix drug with honey, gum, or breadcrumb dough. Roll into pea-sized spheres by hand on a pill tile. Dry. Coat with talc or sugar. Each pill must be weighed individually — extremely labor-intensive and dose-variable. Predecessor to tablet compression.
- **Compression molding** (early 1800s): Pack moist drug-binder mixture into a mold, apply pressure by hand screw, eject, dry. Produces more uniform doses than hand-rolling. Requires only a screw press and metal dies — achievable at lower technology than a tablet press.
- **Percolation extraction** (standard 19th century method): Pack ground drug in a conical percolator. Slowly drip solvent through from top. Collect percolate. Continuous fresh solvent contact maintains concentration gradient, achieving more complete extraction than maceration. Produces a "percolate" that is then adjusted to standard strength.

### Kolbe-Schmitt Aspirin Synthesis

The synthesis of aspirin (acetylsalicylic acid) from phenol is the canonical example of moving from plant-derived medicine (willow bark → salicin) to a pure, standardized synthetic drug:

1. **Sodium phenoxide**: React phenol with NaOH to form sodium phenoxide (C₆H₅ONa). Dry the product.
2. **Kolbe-Schmitt carboxylation**: Heat sodium phenoxide with CO₂ under pressure (100-125°C, 7-10 atm). Forms sodium salicylate. The regiochemistry is critical — ortho-carboxylation gives salicylate; para-carboxylation gives parasalicylate (less desired). Temperature control: higher temperature favors para-isomer.
3. **Acidification**: Dissolve sodium salicylate in water. Add H₂SO₄ to precipitate salicylic acid. Filter. Recrystallize from hot water. Salicylic acid: white needles, melting point 159°C.
4. **Acetylation**: React salicylic acid with acetic anhydride at 85°C for 15 minutes with catalytic H₂SO₄ (2-3 drops). Cool. Crystals of acetylsalicylic acid (aspirin) precipitate. Filter. Recrystallize from water-ethanol mixture. Melting point: 135°C (sharp — confirms purity).
5. **Quality test**: Add FeCl₃ solution to dissolved sample. Purple color = salicylic acid impurity (unreacted starting material). Pure aspirin gives no color change. If positive, recrystallize again.

Yield: typically 70-85% of theoretical. Each 500 mg aspirin tablet requires ~0.52 g aspirin powder + excipients.

### Packaging and Storage Requirements

| Dosage Form | Container | Storage Temperature | Shelf Life (estimated) | Special Requirements |
|-------------|-----------|--------------------|-----------------------|---------------------|
| Tablets (uncoated) | Amber glass bottle with desiccant | <25°C, dry | 2-3 years | Protect from moisture — humidity causes disintegration |
| Tablets (coated) | Amber glass bottle | <25°C, dry | 3-5 years | Sugar-coated: protect from humidity; film-coated: more moisture-resistant |
| Capsules | Amber glass bottle with desiccant | <25°C, dry | 2-3 years | Gelatin softens above 30°C; becomes brittle below 5°C |
| Tinctures | Amber glass, sealed | 15-25°C | 2-5 years | Ethanol preserves; keep sealed to prevent evaporation |
| Ointments | Opaque jar, sealed | <25°C | 1-2 years | Protect from heat (melts) and contamination (finger contact) |
| Sterile injectables | Glass ampoule or sealed vial | 2-8°C (refrigerated) or room temp | 1-2 years | Never freeze; protect from light; single-use once opened |

## References

- [Pharmacology](pharmacology.md) — drug sources, extraction methods, dosage forms reference
- [Surgery Basics](surgery-basics.md) — anesthetic and antiseptic use in surgery
- [Diagnostics](diagnostics.md) — laboratory testing for drug quality monitoring
- [Sanitation](sanitation.md) — clean water, sterile technique, cleanroom fundamentals
- [Chemistry](../chemistry/index.md) — solvent production, acid synthesis, distillation
- [Chemical Safety](../ehs/chemical-safety.md) — handling hazardous pharmaceutical chemicals
- [Toxicology](../ehs/toxicology.md) — drug toxicity and overdose management

---

*Part of the [Bootciv Tech Tree](../index.md) • [Health](./index.md) • [All Domains](../index.md)*
