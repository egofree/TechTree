# Synthetic Polymers & Elastomers

> **Node ID**: polymers.rubber.synthetic
> **Domain**: [Polymers & Composites](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`chemistry.petroleum-alternatives`](../chemistry/petroleum-alternatives.md), [`machine-tools`](../machine-tools/index.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 20-50
> **Outputs**: nitrile_rubber, neoprene, silicone_elastomers, polyurethane
> **Critical**: No — synthetic elastomers expand capability beyond natural rubber but are not on the critical path

## Overview

Synthetic polymers fill gaps natural rubber cannot: oil resistance (NBR), flame retardancy (neoprene), extreme-temperature service (silicone, -60 to +250°C), and tunable hardness (polyurethane, Shore A 70 to Shore D 75). Each requires specific monomer feedstocks and controlled polymerization conditions.

The synthetic polymers in this article span from semi-synthetic materials achievable at moderate technology level (celluloid, casein plastic) through fully synthetic thermoplastics requiring petrochemical infrastructure (nylon, PET, SBR) to specialty elastomers for extreme environments (fluoroelastomers). Feedstocks derive from [petrochemical cracking](../chemistry/petroleum-alternatives.md) or, for bootstrap contexts, from ethanol fermentation (Lebedev process for butadiene) and coal tar distillation.

See [Rubber Production](./rubber.md) for natural rubber vulcanization and compounding recipes shared across all elastomers. See [Thermoplastics](./thermoplastics.md) for melt-processing methods (injection molding, extrusion, blow molding).

## Prerequisites

## Materials
- [Petrochemical monomers](../chemistry/petroleum-alternatives.md): ethylene, propylene, butadiene, styrene, acrylonitrile from steam cracking of naphtha (750-900°C, 0.1-0.5 s residence)
- [Chlorine](../chemistry/electrolysis.md) (for neoprene, PVC — from chlor-alkali electrolysis)
- [MG-Silicon](../silicon/mg-si-production.md) (for silicone elastomers — quartz + carbon reduction)
- [Phosgene](../chemistry/electrolysis.md) (CO + Cl₂ over activated carbon at 200-300°C — for polycarbonate and isocyanate production)
- Formaldehyde (from methanol oxidation over silver catalyst at 600-700°C)
- Phenol (from coal tar distillation or cumene process)

## Tools and Equipment
- [Stirred tank reactors](../machine-tools/casting.md) (glass-lined or stainless steel, 5-50 m³, jacketed for temperature control)
- [Two-roll mills](../machine-tools/machining.md) (for compounding)
- Compression or injection molding presses (for vulcanization)
- Distillation columns (for monomer purification)

## Infrastructure
- Steam supply (for reactor heating and distillation)
- Cooling water (for exothermic polymerization control)
- Ventilation and gas scrubbing (for toxic monomer handling)
- Nitrogen inerting system (for moisture-sensitive polymerizations)

## Bill of Materials

## Nitrile Rubber (NBR) — per 100 kg polymer

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Butadiene (C₄H₆) | 55-75 kg | [Petrochemicals](../chemistry/petroleum-alternatives.md) — steam cracking naphtha | Lebedev process from ethanol (2 mol ethanol → 1 mol butadiene, ZnO/Al₂O₃ catalyst, 400-450°C) |
| Acrylonitrile (CH₂=CHCN) | 25-45 kg | [Petrochemicals](../chemistry/petroleum-alternatives.md) — propylene ammoxidation | None — acrylonitrile has no practical non-petrochemical route |
| Sodium dodecyl sulfate (emulsifier) | 2-5 kg | Organic synthesis | Fatty acid soaps |
| Potassium persulfate (initiator) | 0.3-1.0 kg | Chemical synthesis | Redox initiator (FeSO₄ + hydroperoxide) |
| Tertiary dodecyl mercaptan (chain transfer) | 0.3-0.5 kg | Organic synthesis | None — controls molecular weight |

## Neoprene (CR) — per 100 kg polymer

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Chloroprene (CH₂=CCl-CH=CH₂) | 105-110 kg | [Chemistry](../chemistry/electrolysis.md) — acetylene + HCl route or butadiene + Cl₂ route | Acetylene route when CaC₂ → C₂H₂ available; butadiene route when petrochemicals available |
| Sodium dodecyl sulfate (emulsifier) | 2-5 kg | Organic synthesis | Fatty acid soaps |
| N-dodecyl mercaptan (chain transfer) | 0.3-0.5 kg | Organic synthesis | None — controls MW |
| Zinc oxide (cure agent) | 5 kg | [Chemistry](../chemistry/alkalis.md) | None |
| Magnesium oxide (acid scavenger) | 4 kg | [Chemistry](../chemistry/alkalis.md) | None — scavenges HCl |

## Polyurethane Rigid Foam — per m³ (35 kg/m³ density)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Polyether polyol (MW ~400, 4-8 OH groups) | 23-25 kg | [Petrochemicals](../chemistry/petroleum-alternatives.md) — propylene oxide + ethylene oxide | Polyester polyol from adipic acid + ethylene glycol |
| Polymeric MDI (isocyanate) | 30-35 kg | [Chemistry](../chemistry/petroleum-alternatives.md) — aniline + formaldehyde → phosgenation | TDI (less suitable for rigid foam) |
| Cyclopentane (blowing agent) | 2-4 kg | Petroleum refining | HCFC-141b (ozone-depleting), water (generates CO₂, less insulation) |
| Silicone surfactant | 0.5-1.0 kg | [Silicon](../silicon/mg-si-production.md) | None — stabilizes foam cells |
| Amine catalyst | 0.3-0.5 kg | Organic synthesis | None — controls reaction timing |

## Process Description

## 4.1 Nitrile Rubber (NBR, Buna-N)

**Principle**: Emulsion copolymerization of butadiene (55-75 parts) with acrylonitrile (25-45 parts) produces a random copolymer with polar nitrile groups (—C≡N) along the chain. The nitrile groups provide oil and fuel resistance by increasing polymer polarity, making the rubber less soluble in non-polar hydrocarbons. Higher acrylonitrile content → better oil resistance but higher glass transition temperature (less flexible at low temperature).

**Prerequisites**: Butadiene (from [steam cracking](../chemistry/petroleum-alternatives.md) or Lebedev ethanol process). Acrylonitrile (from propylene ammoxidation, requiring propylene + ammonia + air). Glass-lined or stainless steel stirred tank reactor (5-50 m³) with jacket cooling. Centrifuge or screen for rubber recovery.

**Materials**:
- Butadiene (C₄H₆, >99% purity, inhibited with TBC): 55-75 parts
- Acrylonitrile (CH₂=CHCN, >99% purity): 25-45 parts
- Water (deionized): 200 parts (continuous phase)
- Sodium dodecyl sulfate (emulsifier): 2-5 parts
- Potassium persulfate or redox initiator (FeSO₄ + hydroperoxide): 0.3-1.0 parts
- Tertiary dodecyl mercaptan (chain transfer agent): 0.3-0.5 parts
- Hydroquinone (short-stop): 0.1-0.3 parts (stops reaction at target conversion)

**Procedure**:
1. Charge reactor with deionized water, emulsifier, and chain transfer agent. Purge with nitrogen to remove oxygen (oxygen inhibits free-radical polymerization).
2. Add butadiene and acrylonitrile monomers. Stir to form stable emulsion.
3. Add initiator. For cold NBR (preferred — superior properties): maintain 30-50°C via jacket cooling. Polymerization is exothermic (~60-80 kJ/mol) — cooling capacity must match heat generation rate.
4. React for 6-12 hours, monitoring conversion by solids content measurement (gravimetric sampling every 2 hours).
5. Stop reaction at 70-80% conversion by adding hydroquinone short-stop. Do NOT exceed 85% conversion — higher conversion produces cross-linked microgel particles that degrade properties.
6. Coagulate latex by adding CaCl₂ (1-2%) and dilute sulfuric acid (0.5-1.0%) with stirring. Rubber precipitates as crumb.
7. Wash crumb rubber 3× with water to remove emulsifier, salts, and residual monomer.
8. Dry on hot-roll dryer at 80-100°C to <0.5% moisture. Bale at 33-35 kg per bale.

**Calibration/Verification**:
- Conversion check: Gravimetric solids test. Weigh 10 g emulsion, dry at 105°C for 2 hours, weigh residue. Conversion = (solids% — initial solids%) / (monomer charge%). Target: 70-80%.
- Bound acrylonitrile content: Nitrogen analysis (Kjeldahl or Dumas). Low-ACN: 18-22%. Medium-ACN: 30-35%. High-ACN: 40-50%. Deviation >2% from target indicates inaccurate monomer charge.
- Mooney viscosity (ML 1+4 at 100°C): 50-90 for cold NBR. Higher viscosity = higher molecular weight. Below 40 indicates excessive chain transfer; above 100 indicates insufficient chain transfer or excessive conversion.

**Expected Performance**:
- Tensile strength: 15-28 MPa (with 30-50 phr carbon black reinforcement)
- Elongation at break: 300-600%
- Oil swell (IRM 903, 70 hours at 100°C): <10% for High-ACN, 10-30% for Medium-ACN, >30% for Low-ACN
- Tg: -50°C (Low-ACN) to -15°C (High-ACN)
- Service temperature: -40°C to +120°C

**Strengths**:
- Best oil and fuel resistance of any moderate-cost elastomer — NBR swells <10% in IRM 903 oil at 100°C for High-ACN grades (vs. >50% for natural rubber)
- Wide range of acrylonitrile content allows tuning of oil resistance vs. low-temperature flexibility
- HF resistance — NBR gloves provide >8 hours breakthrough time against 48% hydrofluoric acid (used in semiconductor cleanroom gloves)

**Weaknesses**:
- Poor ozone and weather resistance — the carbon-carbon double bonds in the butadiene segments are attacked by ozone, causing cracking in outdoor service
- Limited high-temperature capability — continuous service limited to 120°C; above this, nitrile groups begin to cross-link and embrittle
- Acrylonitrile monomer is toxic and flammable — flash point -1°C, IARC Group 2B (possible carcinogen), OSHA PEL 2 ppm

## 4.2 Neoprene (Polychloroprene, CR)

**Principle**: Chloroprene (CH₂=CCl-CH=CH₂) polymerizes via free-radical emulsion polymerization to produce polychloroprene. The chlorine atom on the polymer backbone provides inherent UV stability, ozone resistance, and flame retardancy (LOI ~26%, self-extinguishing in normal air at 21% oxygen).

**Prerequisites**: Chloroprene monomer from either (a) acetylene + HCl route (CaC₂ → C₂H₂ + 2 HCl → 1,1-dichloroethane → dehydrochlorination at 450-550°C → chloroprene, ~70% overall yield) or (b) butadiene + Cl₂ route (butadiene + Cl₂ → 3,4-dichloro-1-butene → isomerization → 1,4-dichloro-2-butene + NaOH → chloroprene + NaCl, 95% yield at 60-80°C). Jacketed stirred tank reactor (40-50°C). Stainless steel or glass-lined construction.

**Materials**:
- Chloroprene (inhibited with phenothiazine at 0-5°C, >99% purity): 100 parts
- Water (deionized): 200 parts
- Sodium dodecyl sulfate (emulsifier): 2-5 parts
- N-dodecyl mercaptan (chain transfer): 0.3-0.5 parts
- Potassium persulfate (initiator): 0.2-0.5 parts
- Hydroquinone (short-stop): 0.1-0.3 parts
- For sulfur-modified grades: elemental sulfur 0.5-1.5 parts (copolymerized for improved processing)

**Procedure**:
1. Store chloroprene at 0-5°C with phenothiazine inhibitor until use. Chloroprene polymerizes spontaneously at room temperature without inhibitor.
2. Charge reactor with water, emulsifier, and chain transfer agent. Purge with nitrogen.
3. Add chloroprene monomer. Stir to form emulsion.
4. Add initiator. Maintain 40°C via jacket cooling (exothermic polymerization).
5. React for 2-8 hours, monitoring conversion. Stop at 70-80% conversion by adding hydroquinone short-stop. Do NOT exceed 80% — chloroprene is highly reactive and higher conversion causes excessive branching and gel.
6. Coagulate with CaCl₂ or Al₂(SO₄)₃ + dilute acid. Wash crumb 3× with water.
7. Dry on hot-roll dryer at 80-100°C. Bale.

**Calibration/Verification**:
- Conversion: Gravimetric solids test. Target: 70-80%. Above 80% = gel formation risk.
- Mooney viscosity (ML 1+4 at 100°C): 30-90. Sulfur-modified grades are softer (30-60). Gel grades contain crosslinked domains for dimensional stability.
- Chlorine content: ~40% by weight (from polymer structure). Verify by elemental analysis. Deviations indicate contamination or incorrect monomer.

**Expected Performance**:
- Tensile strength: 10-25 MPa (unfilled to reinforced)
- Elongation at break: 300-600%
- Tg ≈ -45°C
- Flame resistance: LOI ~26% (self-extinguishing in air)
- Oil swell (IRM 903, 70 hours at 100°C): 50-100% (inferior to NBR but adequate for intermittent contact)
- Service temperature: -40°C to +120°C

**Strengths**:
- Self-extinguishing — flame retardant without additives (the chlorine atom provides inherent flame resistance, LOI 26%)
- Excellent ozone, UV, and weather resistance — does not crack in outdoor exposure (unlike NR and SBR)
- Versatile adhesive — neoprene contact cement bonds wood, metal, laminate, and shoe soles with 2-5 MPa instant contact strength

**Weaknesses**:
- Inferior oil resistance compared to NBR — swells 50-100% in IRM 903 oil (vs. <20% for NBR)
- Chloroprene monomer is highly reactive and requires refrigerated storage (0-5°C) with inhibitor to prevent spontaneous polymerization
- HCl release during aging at elevated temperatures — MgO (4 phr) must be included as acid scavenger to prevent autocatalytic degradation

## 4.3 Silicone Elastomers (PDMS)

**Principle**: Polydimethylsiloxane (PDMS) is polymerized from cyclic siloxanes (D₃ or D₄, produced by hydrolysis of dimethyl dichlorosilane). Cross-linking via peroxide (free radical), platinum-catalyzed addition (hydrosilylation), or moisture cure produces a thermally stable elastomer with the widest service temperature range of any rubber (-60 to +250°C).

**Prerequisites**: [MG-silicon](../silicon/mg-si-production.md) (98-99% Si, from quartz + carbon at 1800-2000°C). Methyl chloride (CH₃Cl, from methanol + HCl). Copper catalyst (for Rochow-Müller process: MG-Si + CH₃Cl → dimethyl dichlorosilane at 250-300°C). Two-roll mill for compounding. Curing oven or heated mold.

**Materials**:
- PDMS gum (high molecular weight, ~500,000 g/mol): 100 parts
- Fumed silica (7-40 nm SiO₂ particles, from flame hydrolysis of SiCl₄): 10-40 phr
- Dicumyl peroxide (for peroxide cure HTV grades): 0.5-2 phr
- OR: Platinum catalyst (~10 ppm) + Si-H crosslinker (1-3%) for addition cure (LSR)
- OR: Acetoxy silane crosslinker (for RTV-1 moisture cure)
- Extending filler (ground quartz, optional, 50-200 phr for cost reduction in non-critical applications)

**Procedure (Peroxide Cure — HTV)**:
1. Compound PDMS gum with fumed silica on two-roll mill. Add silica gradually (4-5 portions) to ensure dispersion. Mill generates shear heat — keep roll temperature below 80°C to prevent premature peroxide decomposition.
2. Add dicumyl peroxide (0.5-2%). Mix 2-3 minutes. Keep temperature below 80°C.
3. Sheet off compound at 2-3 mm thickness.
4. Preform to mold cavity shape. Place in heated mold.
5. Cure at 150-175°C for 5-15 minutes under pressure (5-10 MPa in compression mold).
6. Post-cure at 200°C for 2-4 hours in circulating air oven. This step is mandatory — peroxide decomposition leaves volatile byproducts (acetophenone, cumyl alcohol) that cause outgassing and dimensional instability if not removed.

**Calibration/Verification**:
- Hardness (Shore A): Measure at 3 points. Target per grade specification (typically 40-80 Shore A). Unfilled gum is ~20 Shore A; 10-40 phr fumed silica raises to 40-80.
- Tensile test: ASTM D412. Target: 6-10 MPa (with 10-40 phr fumed silica). Below 4 MPa indicates poor silica dispersion or insufficient filler.
- Outgassing test (post-cure verification): Heat sample at 150°C for 1 hour. Weigh before and after. Weight loss should be <0.5%. Above 1% indicates insufficient post-cure.
- Compression set (22 hours at 175°C): Target <25%. Above 35% indicates incomplete cure or degraded peroxide.

**Expected Performance**:
- Tensile strength: 6-10 MPa (filled)
- Elongation at break: 200-500%
- Service temperature range: -60°C to +250°C (widest of any elastomer)
- Dielectric constant: ε ≈ 3 (excellent electrical insulation)
- Dissipation factor: tan δ ≈ 0.001

**Strengths**:
- Widest service temperature range of any elastomer: -60°C to +250°C continuous (natural rubber: -50°C to +100°C; nitrile: -40°C to +120°C)
- Biocompatible — medical grades meet USP Class VI and ISO 10993; used for catheters, seals, and food-contact items
- Excellent dielectric properties (ε ≈ 3, tan δ ≈ 0.001) — used for electronic potting and encapsulation

**Weaknesses**:
- Low mechanical strength — unfilled PDMS tensile is <0.5 MPa (essentially a weak gum); even filled, only 6-10 MPa (vs. 20-30 MPa for natural rubber)
- Expensive — MG-Si precursor chain (quartz → silicon → methylchlorosilanes → PDMS) is energy-intensive and requires multiple chemical processing steps
- Poor hydrocarbon resistance — silicone swells in non-polar solvents (gasoline, toluene); not suitable for fuel contact applications

## 4.4 Polyurethane (PU) — Rigid Foam

**Principle**: Polyol (hydroxyl-terminated polymer) reacts with isocyanate (NCO-terminated) to form a urethane linkage (—NH—CO—O—). In foam production, water reacts with excess isocyanate to generate CO₂ gas (H₂O + NCO → urea linkage + CO₂), which inflates the reacting mixture. The blowing agent (cyclopentane, boiling point 36°C) provides most of the expansion in rigid foam, creating closed cells with low thermal conductivity (0.020-0.025 W/(m·K)).

**Prerequisites**: Polymeric MDI (isocyanate component — from aniline + formaldehyde → MDA → phosgenation with COCl₂). Polyether polyol (from propylene oxide + ethylene oxide polymerization initiated by glycerol or sucrose). Cyclopentane blowing agent. Mixing/dispensing equipment (hand mix or machine dispense).

**Materials**:
- Polyether polyol (MW ~400, 4-8 hydroxyl groups per molecule): 100 parts
- Polymeric MDI (pMDI, isocyanate index 130-180): 130-180 parts
- Water (generates CO₂): 1-2 parts
- Cyclopentane (primary blowing agent, bp 36°C): 10-20 parts
- Silicone surfactant (stabilizes rising foam cells): 2 parts
- Amine catalyst (blowing reaction): 1 part

**Procedure**:
1. Mix polyol, water, cyclopentane, surfactant, and amine catalyst in a plastic or metal container (Component A). Stir 30 seconds to homogenize. Cyclopentane is flammable (LEL 1.1%) — mix in ventilated area away from ignition sources.
2. Add polymeric MDI (Component B) to the mixture. Stir vigorously for 10-15 seconds with a mechanical mixer (500-1000 RPM). The reaction begins immediately.
3. Pour the reacting mixture into the mold or cavity within 20 seconds of adding MDI (cream time is 10-15 seconds — initial foaming begins).
4. Foam rises to full height in 60-90 seconds (rise time). Do NOT disturb during rise — movement causes cell collapse.
5. Foam becomes tack-free (surface no longer sticky) in 120-180 seconds. Allow to cure in mold for 10-30 minutes before demolding.
6. Post-cure at room temperature for 24 hours for complete reaction and dimensional stability.
7. Trim excess foam flush with mold edges using a serrated knife or hot wire cutter.

**Calibration/Verification**:
- Density: Cut a 100 mm cube from the foam center. Weigh and calculate density. Target: 28-50 kg/m³ for rigid insulation foam. Below 25 kg/m³ = insufficient strength; above 55 kg/m³ = wasted material.
- Thermal conductivity: Measure with heat flow meter (ASTM C518). Target: 0.020-0.025 W/(m·K). Above 0.030 W/(m·K) indicates open cells or poor blowing agent retention.
- Compressive strength (ASTM D1621): Target: 100-400 kPa at 10% deformation (parallel to rise direction). Below 100 kPa indicates poor cell structure or insufficient cross-link density.
- Dimensional stability (ASTM D2126): Measure dimensions before and after 72 hours at 70°C, 90% RH. Dimensional change should be <3%. Above 5% indicates incomplete cure or poor cell structure.

**Expected Performance**:
- Density: 28-50 kg/m³
- Thermal conductivity: 0.020-0.025 W/(m·K) — best insulation among common materials (fiberglass: 0.035-0.040, EPS: 0.030-0.040)
- Compressive strength: 100-400 kPa
- R-value: ~3.5 per 25 mm thickness (vs. ~2.5 for fiberglass, ~2.0 for softwood)
- Maximum service temperature: 80-100°C (above this, foam begins to soften and lose dimensional stability)

**Strengths**:
- Highest insulation performance at moderate technology level — 50 mm rigid PU foam (R-value ~3.5) equals 100 mm fiberglass or 150 mm softwood
- On-site production — two liquid components mixed and poured in place; spray PU foam can insulate an entire building in a day
- Closed-cell structure provides both thermal insulation and moisture barrier — eliminates need for separate vapor barrier in building construction

**Weaknesses**:
- Isocyanate (MDI) is a respiratory sensitizer — repeated inhalation causes permanent occupational asthma. Spray application generates respirable aerosol requiring supplied-air respirator
- Requires phosgene for isocyanate production — phosgene is a WWI chemical weapon, lethal at 1 ppm; sealed, leak-tested systems with caustic scrubbers are mandatory
- Flammable — rigid PU foam ignites readily and produces toxic smoke (hydrogen cyanide, CO). Building codes require thermal barriers (drywall) over exposed foam

## 4.5 Styrene-Butadiene Rubber (SBR)

**Principle**: Emulsion copolymerization of styrene (23-25%) with butadiene (75-77%) produces a random copolymer. SBR is the highest-volume synthetic rubber (~6 million tonnes/year globally, ~40% of all synthetic rubber). Cold polymerization (5°C) produces superior properties — more linear chains, less branching, higher molecular weight than hot polymerization (50°C).

**Prerequisites**: Styrene (from ethylbenzene dehydrogenation). Butadiene (from [steam cracking](../chemistry/petroleum-alternatives.md) or Lebedev ethanol process). Refrigerated reactor (5°C for cold SBR). Jacketed stirred tank reactor.

**Materials**:
- Styrene (C₆H₅CH=CH₂, >99%): 23-25 parts
- Butadiene (C₄H₆, >99%): 75-77 parts
- Water (deionized): 200 parts
- Fatty acid soap (emulsifier): 2-5 parts
- Redox initiator (FeSO₄ + cumene hydroperoxide) for cold process: 0.2-0.5 parts
- Tertiary dodecyl mercaptan (chain transfer): 0.2-0.5 parts
- Hydroquinone (short-stop): 0.1-0.3 parts

**Procedure**:
1. Charge reactor with water, emulsifier, and chain transfer agent. Purge with nitrogen.
2. Add styrene and butadiene monomers. Stir to form emulsion.
3. Add redox initiator. For cold SBR: maintain 5°C via refrigerated jacket (ice brine or ammonia refrigeration). React for 8-12 hours.
4. Monitor conversion. Stop at 60-70% by adding hydroquinone short-stop.
5. Coagulate with salt/acid (NaCl + H₂SO₄). Wash crumb. Dry on hot drum dryer at 80-100°C.
6. Bale at 33-35 kg.

**Calibration/Verification**:
- Conversion: Gravimetric solids test. Target: 60-70%. Cold SBR is stopped earlier than NBR to prevent branching.
- Bound styrene: 23-25% (verified by UV spectroscopy or refractive index). Deviations affect Tg and properties.
- Mooney viscosity (ML 1+4 at 100°C): 45-55 for oil-extended SBR (most common form — extended with 37.5 phr aromatic oil).

**Expected Performance** (oil-extended SBR with 50 phr carbon black):
- Tensile strength: 17-25 MPa (unfilled SBR is ~2 MPa — carbon black reinforcement is essential)
- Elongation at break: 400-600%
- Tg ≈ -55°C (better low-temperature flexibility than natural rubber)
- Abrasion resistance: Comparable to natural rubber when properly compounded
- Not oil-resistant — swells significantly in hydrocarbon solvents

**Strengths**:
- Lower cost than natural rubber — monomers from abundant petrochemical feedstocks; SBR production is not limited by tropical growing conditions
- Better aging resistance than natural rubber — fewer reactive double bonds per chain segment than NR
- Good abrasion resistance when compounded with carbon black — standard tire tread material (typically 50% SBR + 50% NR blend)

**Weaknesses**:
- Requires carbon black reinforcement — unfilled SBR has negligible tensile strength (~2 MPa); cannot achieve useful properties without reinforcing filler
- Poor oil resistance — SBR swells in all hydrocarbon solvents; use NBR for oil/fuel contact
- Lower green strength (unvulcanized) than natural rubber — SBR is tacky and weak before cure, making tire building more difficult than with NR

## Quantitative Parameters

## Synthetic Polymer Development Timeline

| Year | Polymer | Type | Key Innovation |
|------|---------|------|---------------|
| 1869 | Celluloid | Semi-synthetic thermoplastic | First practical plastic (nitrocellulose + camphor) |
| 1897 | Casein (Galalith) | Semi-synthetic thermoset | Protein-formaldehyde cross-linking |
| 1907 | [Bakelite](./thermosets.md) | Fully synthetic thermoset | First fully synthetic plastic (phenol-formaldehyde) |
| 1912 | Cellophane | Regenerated cellulose | First transparent film (viscose process) |
| 1935 | [Nylon 66](./thermoplastics.md) | Fully synthetic thermoplastic | First synthetic fiber (polyamide condensation) |
| 1941 | [PET (polyester)](./thermoplastics.md) | Fully synthetic thermoplastic | Highest-volume synthetic fiber |
| 1943 | Polyurethane | Synthetic elastomer/foam | Tunable from rigid foam to cast elastomer |

## Monomer Source Chain Comparison

| Polymer | Primary Monomers | Feedstock Origin | Bootstrap Route |
|---------|-----------------|------------------|-----------------|
| NBR | Butadiene + acrylonitrile | Petrochemical | Lebedev process for butadiene from ethanol; acrylonitrile requires petrochemicals |
| Neoprene | Chloroprene | Acetylene + HCl or butadiene + Cl₂ | Calcium carbide → acetylene route feasible at moderate tech level |
| Silicone | Dimethyl dichlorosilane | MG-Si + CH₃Cl | [MG-Si](../silicon/mg-si-production.md) from quartz + carbon; methyl chloride from methanol + HCl |
| PU foam | Polyol + MDI | Petrochemical | MDI requires phosgene (CO + Cl₂); polyol from propylene oxide |
| SBR | Styrene + butadiene | Petrochemical | Lebedev process for butadiene; styrene from ethylbenzene dehydrogenation |

## Elastomer Property Comparison

| Property | NR | NBR (Med-ACN) | Neoprene | Silicone | PU Cast | EPDM |
|----------|-----|---------------|----------|----------|---------|------|
| Tensile (MPa) | 20-30 | 15-28 | 10-25 | 6-10 | 30-55 | 7-21 |
| Elongation (%) | 400-650 | 300-600 | 300-600 | 200-500 | 300-600 | 150-600 |
| Tg (°C) | -70 | -35 | -45 | -120 | -40 to -20 | -50 |
| Service max (°C) | 100 | 120 | 120 | 250 | 80-120 | 150 |
| Oil resistance | Poor | Excellent | Moderate | Poor | Good | Poor |
| Ozone resistance | Poor | Poor | Excellent | Excellent | Good | Excellent |
| Flame resistance | Poor | Poor | Self-extinguishing | Fair | Poor | Poor |

## Scaling Notes

- **NBR**: Batch emulsion polymerization in 5-50 m³ reactors. A 20 m³ reactor produces 5-8 tonnes NBR per batch (8-12 hour cycle). Scaling adds reactors; polymerization time does not decrease with scale.
- **Neoprene**: Similar batch scale to NBR. DuPont's Louisville plant operated at ~100,000 tonnes/year capacity.
- **PU foam**: Continuous dispensing machines produce 50-200 kg/minute of mixed foam. Rigid foam panel production lines run at 5-15 m/minute (1.2 m wide, 25-100 mm thick). Hand-mixing (bucket and stirrer) produces 1-10 kg batches — adequate for insulation of small equipment.
- **SBR**: Largest synthetic rubber plants produce 100,000+ tonnes/year. A 30 m³ reactor produces 8-12 tonnes per batch.
- **Minimum bootstrap scale**: PU rigid foam is achievable at the smallest scale — hand-mix two liquid components in a bucket and pour in place. No reactor required. NBR and neoprene require sealed, jacketed reactors for emulsion polymerization.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| NBR gel formation (grainy texture, poor processing) | Conversion exceeded 85%; excessive branching | Stop polymerization earlier (60-75%); add chain transfer agent; check short-stop timing |
| Neoprene spontaneous polymerization in storage | Temperature too high; inhibitor depleted | Store chloroprene at 0-5°C; verify phenothiazine inhibitor concentration; use within 3 months |
| Silicone foam bubbles or voids | Moisture contamination in PDMS gum or filler; trapped air | Dry all materials before compounding (105°C, 2 hours); deaerate under vacuum before molding |
| PU foam collapse (no rise, dense slab) | Insufficient catalyst; contaminated polyol (moisture); incorrect isocyanate:polyol ratio | Verify amine catalyst added; check polyol for water contamination (Karl Fischer titration); verify MDI dispensed by weight |
| PU foam brittle or friable | Isocyanate index too high; insufficient post-cure | Reduce MDI to 130-150 parts; verify 24-hour room temperature cure before handling |
| SBR low tensile strength | Insufficient carbon black; poor dispersion | Increase carbon black to 50 phr; extend mixing time on mill; check for 100% dispersion by stretching thin film (no visible white streaks) |

## Safety

- **Phosgene (COCl₂) for polycarbonate and isocyanate production**: Odorless at low concentrations or faintly smells of newly mown hay. Causes delayed pulmonary edema — symptoms may not appear for 2-24 hours after exposure. Lethal at 1 ppm sustained exposure. Sealed, leak-tested systems with NaOH gas scrubbers mandatory. Continuous monitoring at 0.1 ppm with audible alarms. Emergency: evacuate immediately on any leak, administer oxygen, seek medical care regardless of symptoms.
- **Isocyanates (TDI, MDI) for polyurethane**: Potent respiratory sensitizers — repeated inhalation causes permanent occupational asthma. TDI: OSHA PEL 0.02 ppm (ceiling). MDI is less volatile (lower vapor pressure) but spray application generates respirable aerosol. Full-face respirator with organic vapor/P100 cartridge or supplied air. Do not return to isocyanate work if sensitized.
- **Acrylonitrile for NBR**: Flash point -1°C (flammable). IARC Group 2B (possible carcinogen). Cyanide release on combustion — fires produce HCN gas. OSHA PEL 2 ppm (8-hour TWA). Handle in closed systems with leak detection. Large spill: evacuate 100+ m radius.
- **Vinyl chloride monomer (VCM)**: IARC Group 1 carcinogen causing angiosarcoma of the liver (latency 10-40 years). LEL 3.6%, UEL 33% in air. Closed systems, continuous air monitoring, explosion-proof equipment. See [Thermoplastics](./thermoplastics.md) for full VCM hazard data.
- **Styrene**: Flash point 31°C. IARC Group 2A (probable carcinogen). CNS depressant at 100+ ppm. OSHA PEL 50 ppm TWA. Odor detectable at 0.1 ppm but causes odor fatigue — use direct-reading instruments, not smell, as warning.

## Quality Control

## NBR Quality Tests
- **Bound acrylonitrile**: Nitrogen analysis (Kjeldahl). Target ±2% of specification for grade.
- **Mooney viscosity**: ML 1+4 at 100°C. Target range per grade specification. Out-of-range viscosity indicates MW control issues.
- **Oil swell**: Immerse 25 × 50 × 2 mm sample in IRM 903 oil at 100°C for 70 hours. Weigh before/after. Volume swell <10% for High-ACN, <25% for Medium-ACN.
- **Gel content**: Dissolve 0.5 g NBR in 100 ml MEK. Filter through 200-mesh screen. Gel content should be <5%. Above 10% indicates excessive cross-linking during polymerization.

## PU Foam Quality Tests
- **Density**: Cut 100 mm cube, weigh. Target ±10% of specification.
- **Thermal conductivity**: Heat flow meter (ASTM C518). Target <0.025 W/(m·K).
- **Compressive strength**: ASTM D1621. Target >100 kPa at 10% deformation.

## General Elastomer Tests
- **Tensile/elongation**: ASTM D412 dumbbell specimen. All elastomers.
- **Hardness**: Shore A durometer (ASTM D2240). Measure at 3 points, ±2 units agreement.
- **Compression set**: ASTM D395 Method B. 22 hours at 70°C, 25% deflection.

## Variations and Alternatives

## Semi-Synthetic Polymers (Lower Technology Level)

- **Celluloid (1869)**: Nitrocellulose (cellulose + HNO₃/H₂SO₄, 10-13% N) plasticized with camphor (20-30%). Thermoplastic at 80-130°C. Autoignition at 150-170°C — extremely flammable. Used for photographic film, billiard balls, combs. Precursors: [cellulose](./natural.md) (cotton linters or wood pulp), [nitric acid](../chemistry/acids.md), camphor. Achievable at moderate technology level.
- **Casein plastic (Galalith, 1897)**: Milk protein (casein) precipitated from skim milk by acid, hardened in 40% formalin (2-7 days at room temperature or several hours at 50-60°C). Non-flammable, takes dye well, but swells in water (5-15% water absorption). Used for buttons, knitting needles. Precursors: skim milk (dairy by-product — 10 liters yields ~300 g casein), formaldehyde. Producible in home workshops.
- **Bakelite (1907)**: Phenol-formaldehyde thermoset — the first fully synthetic plastic. Phenol from [coal tar](../chemistry/petroleum-alternatives.md) or cumene process. Excellent electrical insulation (10¹²-10¹⁴ Ω·cm), heat resistant to 200°C. See [Thermosets](./thermosets.md) for full details.

## Bootstrap Feedstock Routes

- **Butadiene from ethanol** (Lebedev process): 2 C₂H₅OH → C₄H₆ + 2 H₂O + H₂ over ZnO/Al₂O₃ at 400-450°C. The USSR produced ~100,000 tonnes/year during WWII from grain ethanol. Enables NBR, SBR, and neoprene (via butadiene route) without petrochemical infrastructure.
- **Coal tar monomers**: Coal carbonization at 1000-1200°C produces phenol, benzene, toluene, and xylene. Historically the primary source of aromatic monomers before petroleum. Enables Bakelite (phenol) and nylon (benzene → cyclohexane → adipic acid).

## Specialty Elastomers

- **EPDM**: Saturated terpolymer of ethylene/propylene/diene. Outstanding ozone resistance (20-30 year outdoor service). Used for automotive weatherstripping, roofing membranes, radiator hoses. See Section 4.5 above and [Rubber Production](./rubber.md) for vulcanization details.
- **Fluoroelastomers (FKM, Viton)**: Copolymer of vinylidene fluoride + hexafluoropropylene. Service to 200°C, resistant to concentrated H₂SO₄ and HNO₃. Cost: 20-50× natural rubber. Requires [fluorine chemistry](../chemistry/electrolysis.md) (HF from fluorspar CaF₂ + H₂SO₄). Used for semiconductor wet bench O-rings, aerospace fuel seals.
- **Polybutadiene (BR)**: Second most-produced synthetic rubber. Tg ≈ -100°C (lowest of any common rubber). Exceptional resilience (70-85% rebound). Used as blending component in tire treads (25-50% BR + SBR). Nd-based Ziegler-Natta catalyst gives >97% cis-1,4 content.
- **Butyl rubber (IIR)**: Copolymer of isobutylene (97-99%) + isoprene (1-3%). 10-20× less gas-permeable than NR — the only practical material for tire inner liners and inner tubes. Polymerized at -80 to -100°C in methyl chloride with AlCl₃ catalyst. Halobutyl (CIIR, BIIR) enables covulcanization with NR/SBR for tubeless tire inner liners.
- **Thermoplastic elastomers (TPE)**: SBS, SEBS, TPU — rubber-like elasticity with thermoplastic processability (no vulcanization). Hard domains (physical cross-links that melt above Tg) dispersed in soft matrix. Used for shoe soles, soft-touch grips, cable jacketing.

## References

- **[Natural Polymers](natural.md)**: Natural rubber tapping, processing, and vulcanization
- **[Thermoplastics](thermoplastics.md)**: Melt-processable polymers (PE, PVC, nylon, PS, PTFE, polycarbonate)
- **[Thermosets](thermosets.md)**: Crosslinked polymers (phenolic, epoxy, polyester)
- **[Composites](composites.md)**: Fiber-reinforced polymer matrix materials
- **[Rubber Production](rubber.md)**: Natural rubber compounding, vulcanization, and molding methods
- **[Petrochemicals](../chemistry/petroleum-alternatives.md)**: Monomer feedstock production
- **[MG-Si Production](../silicon/mg-si-production.md)**: Metallurgical-grade silicon for silicone elastomers
- **[Chlor-Alkali Electrolysis](../chemistry/electrolysis.md)**: Chlorine and NaOH production for PVC, neoprene, and phosgene
- **[Coatings](../chemistry/coatings.md)**: Polyurethane and neoprene-based coatings


[← Back to Polymers & Composites](index.md)
