# Solvents

> **Node ID**: chemistry.solvents
> **Domain**: Chemistry
> **Dependencies**: [`chemistry.petroleum-alternatives`](petroleum-alternatives.md), [`chemistry.distillation`](distillation.md), [`chemistry.petroleum-alternatives.fermentation`](fermentation.md)
> **Enables**: [`health`](../health/index.md)
> **Timeline**: Years 15-40
> **Outputs**: ethanol, methanol, ether, turpentine, hydrogen_peroxide

### Overview

Solvents dissolve, extract, clean, and transport chemical species. They are the workhorses of pharmaceutical synthesis (extract active compounds, crystallize products), semiconductor manufacturing (RCA clean, photoresist stripping), industrial degreasing, and chemical analysis. No chemical industry operates without them. This page catalogs the solvents accessible at each stage of bootstrap development — from ethanol and turpentine (organic, low-technology) to chlorinated solvents and hydrogen peroxide (industrial chemistry).

### Ethanol

Ethanol (C₂H₅OH, bp 78.3°C) is the first industrial solvent available. Production is covered in detail in [Fermentation](fermentation.md).

**Solvent properties**:
- Polar protic solvent — dissolves polar organics, resins, oils, many salts. Miscible with water in all proportions.
- Moderate volatility (bp 78.3°C). Evaporates readily but not so fast as to be impractical.
- Relatively low toxicity (LD₅₀ oral rat ~7 g/kg) compared to most industrial solvents.

**[Dehydration to anhydrous ethanol](../glossary/dehydration-to-anhydrous-ethanol.md)** (>99%):
- The ethanol-water azeotrope limits simple [Distillation](distillation.md) to 95.6%. Breaking it requires:
  - **[Molecular sieves](../glossary/molecular-sieves.md)** (zeolite 3Å): Adsorb water selectively. Two-bed system alternates adsorption and thermal regeneration. Produces 99.5-99.9% ethanol. Preferred method when zeolites are available.
  - **Quicklime (CaO)**: Add to 95% ethanol, stir, CaO reacts with water to form Ca(OH)₂, then decant or distill the dried ethanol. Simple but labor-intensive, generates lime sludge waste.
  - **Extractive distillation**: Glycerol or ethylene glycol as entrainer (see [Distillation](distillation.md) for detailed column design).

**Applications**: Pharmaceutical extraction and tincture preparation. Fuel (anhydrous ethanol blends). Feedstock for diethyl ether synthesis. Cleaning/degreasing where water-based cleaners are insufficient. Preservative (70% ethanol is bactericidal — denatures proteins).

### Methanol

Methanol (CH₃OH, bp 64.7°C) is the simplest alcohol and a critical feedstock. Production routes are described in [Fermentation](fermentation.md) (wood pyrolysis) and [Petroleum](petroleum-alternatives.md) (synthesis gas).

**Solvent properties**:
- Lighter and more volatile than ethanol. Polar protic — dissolves many of the same classes of compounds.
- Excellent solvent for many synthetic reactions (Grignard formation, esterification, transesterification for biodiesel).

**[Synthetic methanol](../glossary/synthetic-methanol.md)** (preferred at scale):
- React CO + 2H₂ over Cu/ZnO/Al₂O₃ catalyst at 250°C, 50-100 bar. Synthesis gas from coal gasification or natural gas reforming (see [Petroleum](petroleum-alternatives.md)).
- Yield: nearly quantitative at proper conditions. Single-pass conversion 15-25%, recycle unreacted gas.
- Older technology: ZnO/Cr₂O₃ catalyst at 300-400°C, 20-30 MPa — harsher conditions but robust.

**Applications**: Formaldehyde production (oxidation over silver or iron-molybdenum catalyst at 500-600°C — feedstock for resins). Biodiesel (transesterification of vegetable oils with methanol). Fuel (blended or neat in modified engines). Solvent for paints, inks, and chemical synthesis. Denaturant for ethanol (renders industrial ethanol unfit for drinking).

**Toxicity**: Methanol is metabolized to formaldehyde then formic acid. As little as 10 mL causes permanent blindness; 30 mL can be fatal. Handle in ventilated areas. Never use containers that could be confused with food or water vessels.

### Diethyl Ether

Diethyl ether (C₂H₅OC₂H₅, bp 34.6°C) is the simplest practical ether and one of the most volatile common solvents.

**Synthesis**:
- **Sulfuric acid dehydration of ethanol**: Add ethanol to concentrated H₂SO₄ at 130-140°C. The acid protonates ethanol, promoting nucleophilic substitution by a second ethanol molecule. Product: diethyl ether + water.
  - C₂H₅OH + H₂SO₄ → C₂H₅OSO₃H + H₂O (ethyl hydrogen sulfate intermediate, ~100°C)
  - C₂H₅OSO₃H + C₂H₅OH → (C₂H₅)₂O + H₂SO₄ (ether formation, 130-140°C)
  - Temperature control is critical: below 130°C the reaction is too slow; above 170°C ethylene forms preferentially (C₂H₅OH → C₂H₄ + H₂O).
  - Distill ether continuously as it forms (bp 34.6°C). The low boiling point separates it from ethanol (bp 78.3°C) and water.
- **Yield**: ~60-70% based on ethanol consumed. Sulfuric acid is regenerated and recycled, though dilution and charring gradually degrade it.

**Solvent properties**:
- Very low boiling point (34.6°C) — highly volatile. Excellent for extractions where easy removal by evaporation is desired.
- Slightly polar, immiscible with water (6.9 g/100 mL at 20°C). Good solvent for fats, oils, alkaloids, and organic reaction products.
- Low density (0.713 g/cm³) — floats on water.

**Extreme fire hazard**: Diethyl ether vapor is heavier than air (vapor density 2.6 vs. air = 1). It flows along surfaces and can accumulate in low spots, igniting from distant ignition sources. Flash point: -45°C. Autoignition temperature: 180°C — surprisingly low (hot steam pipes can ignite it). Explosive range in air: 1.9-36%. Never use near open flames, electrical equipment that sparks, or hot surfaces above 180°C. Store in tightly sealed containers in cool, well-ventilated areas away from all ignition sources.

**Peroxide hazard**: Ether slowly reacts with atmospheric oxygen to form organic peroxides (explosive upon concentration or mechanical shock). Test for peroxides with potassium iodide-starch paper before distilling old ether. Add iron wire or BHT inhibitor to storage containers. Discard ether older than 6 months if uninhibited.

**Applications**: Extraction solvent (alkaloids from plant material — critical for [Pharmacology](../health/pharmacology.md)). Anesthetic (historically). Starting fluid for diesel and gasoline engines (high volatility aids cold-start ignition). Reaction solvent for Grignard reactions and lithium aluminum hydride reductions.

### Turpentine

Turpentine (C₁₀H₁₆ mixture, primarily α-pinene and β-pinene, bp 156-180°C) is the oldest organic solvent available without chemical synthesis. Produced by steam [Distillation](distillation.md) of pine resin (oleoresin).

**Production**:
- Tap living pine trees (slash pine, longleaf pine, maritime pine) by cutting bark streaks. Resin exudes, collected in cups. Yield: 2-5 kg resin/tree/year.
- Steam-distill resin: turpentine (volatile, ~20% by weight) distills at ~96°C with steam (see steam distillation in [Distillation](distillation.md)). Residual rosin (colophony, ~80%) remains in the pot.
- World production historically exceeded 300,000 tonnes/year (US naval stores industry, 1900s).

**Solvent properties**:
- Non-polar, miscible with oils and most organic solvents. Immiscible with water.
- Strong pine odor. Good solvent for oils, fats, waxes, resins, and rubber.
- Evaporation rate moderate (bp 156°C). Slower than petroleum solvents like hexane (bp 69°C).

**Applications**: Paint thinner and brush cleaner (historically the primary use before mineral spirits). Feedstock for terpene chemistry (camphor, synthetic pine oil, terpin hydrate). Rubber solvent and plasticizer. Degreasing of metal parts. Starting material for synthesis of fragrances (linalool, geraniol) and pharmaceuticals.

### Benzene, Toluene, Xylene (BTX)

BTX aromatics are powerful solvents and feedstocks derived from coal tar or petroleum catalytic reforming (see [Petroleum](petroleum-alternatives.md)).

**[Benzene](../glossary/benzene.md)** (C₆H₆, bp 80.1°C):
- Excellent solvent for non-polar organics, fats, and resins. Used historically for degreasing and chemical synthesis.
- **[Carcinogen](../glossary/carcinogen.md)** — causes leukemia (AML) with chronic exposure. Industrial use has been largely phased out in developed countries. Substitute with toluene or xylene wherever possible.
- Feedstock for styrene (polystyrene), nylon, phenol, and synthetic rubber (SBR). Difficult to replace as a feedstock even if eliminated as a solvent.

**[Toluene](../glossary/toluene.md)** (C₇H₈, bp 110.6°C):
- Good general-purpose aromatic solvent. Similar dissolving power to benzene but significantly less carcinogenic (not classified as a human carcinogen — metabolized to benzoic acid rather than benzene oxide).
- Applications: paint thinner, coating solvent, gasoline octane booster, feedstock for toluene diisocyanate (TDI → polyurethane foam), TNT explosive synthesis.
- Preferred substitute for benzene in most solvent applications.

**[Xylene](../glossary/xylene.md)** (C₈H₁₀, mixture of ortho-, meta-, para- isomers, bp ~140°C):
- Higher-boiling aromatic solvent. Used where slower evaporation is desired (paints, coatings, cleaning).
- Applications: histology staining solvent, paint and coating formulations, cleaning agent for silicon wafers in semiconductor processing.
- Toxicity: moderate — irritant and nervous system depressant at high concentrations. Less hazardous than benzene.

**Source**: Coal tar distillation (4-8% BTX in coal tar) or petroleum catalytic reforming (platforming — Pt/Al₂O₃ catalyst at 500°C, 15-30 bar, converts naphtha to aromatics + hydrogen). See [Petroleum](petroleum-alternatives.md) for production details.

### Hydrogen Peroxide

Hydrogen peroxide (H₂O₂) is not a solvent in the traditional sense but plays critical roles as an oxidizer, bleaching agent, and cleaning chemical essential for semiconductor manufacturing and pharmaceutical production.

**Concentrations by application**:
- 3%: Disinfectant, wound cleaning (drugstore peroxide)
- 6-12%: Hair bleaching, textile bleaching
- 30-35%: Industrial bleaching, wastewater treatment
- 50-70%: Semiconductor RCA clean, rocket propellant oxidizer
- 90%+ (rare): Rocket oxidizer (concentrated peroxide decomposes explosively with trace contamination)

**[Anthraquinone autoxidation process](../glossary/anthraquinone-autoxidation-process.md)** (industrial standard):
1. Dissolve 2-ethylanthraquinone in a mixed organic solvent (typically C₉-C₁₀ aromatics + trioctyl phosphate). The "working solution."
2. Hydrogenate the working solution over Pd or Ni catalyst at 40-60°C, 1-3 bar H₂. Anthraquinone reduces to anthrahydroquinone.
3. Filter out the catalyst. Oxidize the filtered solution with compressed air at 30-50°C. Anthrahydroquinone re-oxidizes to anthraquinone, producing H₂O₂.
4. Extract H₂O₂ from the working solution with deionized water (counter-current extraction). Produces 25-35% H₂O₂ aqueous solution.
5. Concentrate by vacuum distillation to 50-70% as needed.
6. The working solution (now regenerated to anthraquinone) returns to step 2. The cycle runs continuously.

**Concentration by vacuum distillation**: H₂O₂ boils at 150°C (100%) but decomposes above ~70°C. Concentrate under vacuum (30-50 mbar) to keep temperatures below 50°C. Equipment must be scrupulously clean — trace metals (Fe, Cu, Mn) catalyze violent decomposition. Storage vessels: aluminum or high-density polyethylene (never plain steel or copper).

**Semiconductor RCA clean**: Standard wafer cleaning sequence uses H₂O₂ as a critical reagent:
- **[SC-1](../glossary/sc-1.md)** (Standard Clean 1): NH₄OH:H₂O₂:H₂O = 1:1:5 at 75-80°C. Removes organic contamination and particles. H₂O₂ oxidizes surface silicon to SiO₂, NH₄OH provides particle repulsion via zeta potential.
- **[SC-2](../glossary/sc-2.md)** (Standard Clean 2): HCl:H₂O₂:H₂O = 1:1:6 at 75-80°C. Removes metallic contamination. H₂O₂ keeps metal ions in solution as soluble complexes.
- H₂O₂ concentration must be maintained above the depletion threshold — replace baths every 20-30 minutes of use.

**Applications**: Bleaching (paper pulp, textiles — the largest single use). Wastewater oxidation (destroys organic contaminants). Rocket oxidizer (concentrated H₂O₂ + catalyst → steam + O₂ + heat; monopropellant or bipropellant with kerosene). Disinfectant and sterilization. Etching (copper PCB manufacturing). Semiconductor cleaning (RCA clean).

### Chlorinated Solvents

Carbon tetrachloride (CCl₄, bp 76.7°C), trichloroethylene (TCE, bp 87°C), and perchloroethylene (perc, tetrachloroethylene, bp 121°C) are powerful non-flammable degreasing solvents — but carry serious health and environmental hazards.

**Production** (from methane or ethylene + chlorine):
- **CCl₄**: Chlorinate methane at 400-500°C or carbon disulfide with chlorine (CS₂ + 3Cl₂ → CCl₄ + S₂Cl₂). Sequential substitution: CH₄ → CH₃Cl → CH₂Cl₂ → CHCl₃ → CCl₄. Fractionate to separate the chloromethanes.
- **TCE**: From acetylene + Cl₂ → tetrachloroethane, then dehydrochlorination with Ca(OH)₂ or thermal cracking. Or from ethylene via perchloroethylene + HCl.
- **Perc**: Oxychlorination of C₂H₄ or direct chlorination of C₂Cl₄ precursors. Also from C₁-C₂ hydrocarbon high-temperature chlorination.

**Properties and applications**:
- Non-flammable — the chlorine atoms suppress combustion. This is their primary advantage over hydrocarbon solvents for vapor degreasing.
- Excellent solvency for oils, greases, and fats. Dense liquids (CCl₄: 1.59 g/cm³, perc: 1.62 g/cm³).
- **Vapor degreasing**: Heat solvent in a sump, vapor rises to a condensing coil zone. Suspend dirty parts in the vapor zone. Solvent condenses on cool parts, dissolves oils, drips back to sump. Continuous and effective — standard industrial cleaning for machined parts and electronics.
- CCl₄ was once the standard dry-cleaning solvent (replaced by perc, now being replaced by supercritical CO₂ and hydrocarbon solvents).

**Hazards**:
- **CCl₄**: Causes liver and kidney damage. Ozone-depleting substance (Montreal Protocol phase-out). Toxic metabolites (trichloromethyl radical). Lethal at relatively low doses (LD₅₀ ~2.8 g/kg).
- **TCE**: Probable human carcinogen (kidney cancer). Groundwater contaminant (dense non-aqueous phase liquid — DNAPL — sinks to aquifer bottom, persists for decades). Degreasing applications being phased out.
- **Perc**: Probable carcinogen. The dominant dry-cleaning solvent globally but under regulatory pressure. Less acutely toxic than CCl₄ or TCE but still a chronic hazard.

**Environmental persistence**: All chlorinated solvents resist biodegradation. They contaminate groundwater at µg/L levels detectable by taste and smell. Soil and groundwater remediation is enormously expensive (pump-and-treat, air stripping, activated carbon). Prevention is far cheaper than cleanup.

### Carbon Disulfide

Carbon disulfide (CS₂, bp 46.3°C) is a volatile, highly flammable, and toxic solvent essential for viscose rayon production and rubber vulcanization.

**Production**:
- Methane + sulfur at 600-800°C in a heated tube reactor (no catalyst): CH₄ + 4S → CS₂ + 2H₂S.
- Alternatively, charcoal + sulfur at 800-1000°C: C + 2S → CS₂ (older, less efficient).
- Purify by distillation (bp 46.3°C). H₂S byproduct is toxic gas — scrub with NaOH solution.

**Properties**: Very low flash point (-30°C). Autoignition at 90°C — the lowest of any common industrial solvent. Hot steam pipes or even light bulbs can ignite CS₂ vapor. Vapor is 2.6× denser than air. Nearly insoluble in water. Excellent solvent for sulfur, phosphorus, rubber, fats, and resins.

**Applications**: Viscose rayon (cellulose dissolved in CS₂/NaOH → extruded into acid bath → regenerated cellulose fibers — see [Polymers](../polymers/index.md)). Rubber vulcanization accelerator (dissolves sulfur and accelerators). Carbon tetrachloride feedstock (CS₂ + 3Cl₂ → CCl₄ + S₂Cl₂).

**Toxicity**: Chronic exposure causes neurological damage (parkinsonism, psychosis). Acute poisoning at 1000+ ppm. Threshold limit value: 1 ppm (very low — stricter than most solvents). Use only in enclosed systems with local exhaust ventilation.

### Solvent Selection Guide

No single solvent is ideal for every application. Selection balances solvency power, boiling point, toxicity, flammability, cost, and availability.

| Solvent | Polarity | bp (°C) | Flash pt (°C) | Toxicity | Best For |
|---------|----------|---------|---------------|----------|----------|
| Ethanol | Protic polar | 78 | 13 | Low | Pharma extraction, cleaning, fuel |
| Methanol | Protic polar | 65 | 11 | High (blindness) | Formaldehyde, biodiesel, synthesis |
| Diethyl ether | Low polar | 35 | -45 | Moderate | Alkaloid extraction, Grignard |
| Turpentine | Non-polar | 156-180 | 35 | Low-moderate | Paint thinner, terpene chemistry |
| Benzene | Non-polar | 80 | -11 | **[Carcinogen](../glossary/carcinogen.md)** | Feedstock only; avoid as solvent |
| Toluene | Non-polar | 111 | 4 | Moderate | Coatings, general solvent |
| Xylene | Non-polar | 140 | 27 | Moderate | Histology, coatings, slow evap |
| CCl₄ | Non-polar | 77 | None | High | Phase-out; historical degreasing |
| TCE | Non-polar | 87 | None | High | Vapor degreasing (phase-out) |
| Perc | Non-polar | 121 | None | Moderate-high | Dry cleaning (declining) |
| CS₂ | Low polar | 46 | -30 | Very high | Viscose rayon, vulcanization |
| H₂O₂ (30%) | Protic polar | — | — | Moderate | Bleaching, RCA clean, oxidation |

**Decision framework**:
1. **[Can water do the job?](../glossary/can-water-do-the-job.md)** Use water-based cleaning or extraction first. Cheapest, safest, most available.
2. **[Need polar organic dissolution?](../glossary/need-polar-organic-dissolution.md)** Ethanol for extraction and pharma. Methanol for synthesis and biodiesel.
3. **[Need non-polar dissolution?](../glossary/need-non-polar-dissolution.md)** Turpentine (early stage) or toluene/xylene (petroleum available). Avoid benzene.
4. **[Need non-flammable degreasing?](../glossary/need-non-flammable-degreasing.md)** Perc or TCE — but invest in closed-loop equipment and ventilation. Plan for eventual phase-out.
5. **[Need a volatile extraction solvent?](../glossary/need-a-volatile-extraction-solvent.md)** Diethyl ether — with extreme fire safety precautions. Never use near flames or sparks.
6. **[Need an oxidizer/cleaner?](../glossary/need-an-oxidizercleaner.md)** H₂O₂ for semiconductor RCA clean, bleaching, wastewater treatment.

### Recovery and Recycling

Discharging spent solvents is both wasteful and environmentally destructive. Recovery is standard practice.

**Distillation recovery**: The primary method. Fractionally distill spent solvent to separate it from dissolved oils, water, and contaminants. Simple pot still for gross separation; packed column for high-purity recovery. See [Distillation](distillation.md) for column design. Energy cost: 2-5 MJ per kg of recovered solvent.

**Activated carbon adsorption**: Pass solvent vapor or liquid through activated carbon beds. Carbon adsorbs organic contaminants. Regenerate carbon by steam stripping (desorbs contaminants) or thermal reactivation (heating to 800-900°C in absence of air). Used for dilute solvent recovery from air emissions (paint booths, printing) and wastewater.

**Liquid-liquid extraction**: Separate water-miscible solvents from aqueous waste streams by adding a non-miscible solvent (e.g., extract acetone from water with toluene). Then distill the extractant to recover the target solvent.

**Incineration**: Last resort for solvents that cannot be recovered economically. Burn in a high-temperature incinerator (>1000°C, 2-second residence time) with afterburner to ensure complete destruction. Waste solvents with adequate heating value (>20 MJ/kg) support combustion without supplemental fuel. Flue gas must be scrubbed (chlorinated solvents produce HCl; sulfur-containing solvents produce SO₂).

**Environmental regulations**: Even in bootstrap conditions, solvent contamination of soil and groundwater creates long-term liabilities. Chlorinated solvents (CCl₄, TCE, perc) persist for decades in groundwater. Heavy metals from spent catalysts never degrade. Design solvent systems with containment, recovery, and recycling from the start — remediation is 10-100× more expensive than prevention.

**Solvent losses and minimization**: Covered vessels reduce evaporation. Closed-loop vapor degreasers lose <5% per year vs. >50% for open-top units. Water-based alternatives (alkaline degreasing, aqueous parts washing) should replace organic solvents wherever technically feasible. Process design should minimize solvent inventory — smaller baths, counter-current washing, and cascaded use (clean solvent for final rinse, partially contaminated solvent for initial wash).

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
