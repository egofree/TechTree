# Rubber & Elastomers

> **Node ID**: polymers.rubber
> **Domain**: [Polymers & Composites](./index.md)
> **Dependencies**: None (root capability)
> **Enables**: [`energy.storage`](../energy/storage.md), [`health`](../health/index.md), [`polymers.rubber.gutta-percha`](gutta-percha.md), [`polymers.rubber.shellac`](shellac.md)
> **Timeline**: Years 5-50
> **Outputs**: rubber, elastomers, gaskets, seals
> **Critical**: Yes — flexible seals and vibration isolation required for all mechanical systems, pneumatic tires, and chemical-resistant barriers


Elastomers are polymers that recover shape after large deformation (elongation 400-650% with full recovery). They fill roles no rigid material can: flexible seals, vibration dampers, tires, hoses, chemical-resistant gloves, electrical insulation, and adhesives. The rubber family divides into two branches — natural rubber (from latex) and synthetic elastomers (from petrochemical or fermentation monomers) — with different feedstocks and property profiles.

Rubber is unique among engineering materials — it combines high elasticity with useful tensile strength (17-28 MPa when vulcanized). Before vulcanized rubber, seals required precisely machined metal-to-metal fits, hoses were rigid, and pneumatic tires did not exist. The discovery of vulcanization (Goodyear, 1839) transformed raw natural rubber from a temperature-sensitive curiosity into one of the most important industrial materials. Cross-linking polyisoprene chains with sulfur converts the material from a thermoplastic into a durable elastomer with stable properties across a useful temperature range (-50 to +100°C).

See [Synthetic Polymers & Elastomers](./synthetic.md) for synthetic rubber types (NBR, neoprene, silicone, PU), [Thermoplastics](./thermoplastics.md) for melt-processable polymers, and [Thermosets](./thermosets.md) for crosslinked plastics.

## Prerequisites

## Materials
- [Latex](../glossary/guayule.md) from *Hevea brasiliensis* (tropical) or guayule/Russian dandelion (temperate)
- [Sulfur](../chemistry/alkalis.md) (2-4 phr, cross-linking agent)
- [Carbon black](../energy/charcoal.md) (20-50 phr, reinforcing filler from partial combustion of hydrocarbons)
- [Zinc oxide](../chemistry/alkalis.md) (3-5 phr, activator)
- Stearic acid (1-2 phr, co-activator — from animal fat or vegetable oil hydrolysis)
- Formic acid or acetic acid (0.5% concentration for latex coagulation)

## Tools and Equipment
- [Two-roll mill](../machine-tools/machining.md) or Banbury internal mixer (for compounding)
- [Hydraulic press](../machine-tools/forming.md) (10-50 tons, for compression molding)
- Autoclave or steam-heated mold (140-160°C, for vulcanization)
- Sheeting mill (series of counter-rotating steel rollers)

## Infrastructure
- Smokehouse or drying oven (40-70°C)
- Coagulation tanks (aluminum or ceramic-lined)
- Ventilation for mixing and milling areas (dust and fume extraction)

## Bill of Materials

## Vulcanized Rubber Compound (per 100 kg rubber)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Natural rubber (SMR 20 grade) | 100 kg | [Rubber tapping](./natural.md) — Hevea plantation | Guayule rubber (500-1000 kg/ha/year), Russian dandelion root rubber |
| Sulfur (powder, 99%+) | 2-3 kg | [Chemistry](../chemistry/alkalis.md) — Frasch process or H₂S oxidation | None — sulfur is the primary cross-linking agent |
| Carbon black (N330) | 40-50 kg | [Charcoal/Petroleum](../energy/charcoal.md) — furnace black process | Precipitated silica (10-30 phr) with silane coupling agent |
| Zinc oxide (ZnO, 99%) | 5 kg | [Chemistry](../chemistry/alkalis.md) — zinc metal oxidation | None — activator function is specific |
| Stearic acid (C₁₈H₃₆O₂) | 2 kg | Fat hydrolysis — animal or vegetable fat | Oleic acid (less effective) |
| CBS accelerator (N-cyclohexyl-2-benzothiazole sulfenamide) | 0.5-1.5 kg | [Petrochemicals](../chemistry/petroleum-alternatives.md) — organic synthesis | MBT (0.5-2 phr, faster cure, less processing safety) |
| Antioxidant (TMQ) | 1-2 kg | [Petrochemicals](../chemistry/petroleum-alternatives.md) — amine synthesis | PPD derivatives (staining), phenolic antioxidants (less effective) |

## Latex Coagulation (per 100 kg dry rubber)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Fresh latex (30-40% rubber) | 250-335 kg | [Hevea tapping](./natural.md) | Guayule slurry, dandelion root extract |
| Formic acid (HCOOH, 85%) | 1.5-2.0 kg | [Chemistry](../chemistry/fermentation.md) — methanol + CO oxidation | Acetic acid (white vinegar, slower coagulation), alum |

## Process Description

## Hevea Latex Tapping

**Principle**: Latex is a colloidal emulsion of rubber particles (30-40% cis-1,4-polyisoprene) in water, stabilized by protein surface charges. Tapping makes a controlled cut through the bark to the cambium layer, allowing latex to flow out under natural turgor pressure.

**Prerequisites**: Mature rubber trees (*Hevea brasiliensis*, 5-7 years old, trunk diameter 30-50 cm at 1 m height). Plantation spacing 500-600 trees/ha (4-5 m between trees, 7-8 m between rows). Annual rainfall 1800-2500 mm.

**Materials**:
- Tapping knife (curved blade, sharpened to 15-20° bevel angle)
- Collection cups (coconut shells or plastic cups, 200-500 ml capacity)
- Wire or nail for cup attachment
- Spout (galvanized iron or aluminum, 5 cm long, inserted into bark at base of cut)

**Procedure**:
1. Select tapping panel on tree trunk. First cut starts at 1.5-1.7 m height on the tree (measured from ground to cut starting point).
2. Make a spiral cut descending from upper-left to lower-right at 30° from horizontal. Cut depth: 1.5-2.0 mm — just reaching but NOT penetrating the cambium layer. Cut width: 1.5-2.0 mm (a thin shaving of bark removed with each tap).
3. Insert metal spout at the lower end of the cut. Hang collection cup below spout.
4. Latex flows for 2-4 hours. Flow rate is highest in the first 30 minutes and declines exponentially as the wound seals via latex coagulation at the cut surface.
5. Collect latex from cups after 4-6 hours. Transfer to centralized collection tank. Add ammonia (0.3-0.7% by weight) to prevent premature coagulation during storage.
6. On subsequent tapping days (every 2-3 days), make a new shaving (1-2 mm) from the lower edge of the previous cut on the same panel, moving the cut gradually downward.

**Calibration/Verification**:
- Cut depth check: A correct cut produces a thin, even line of bark removal. If wood fibers (light colored, fibrous) appear in the shaving, the cut is too deep and has penetrated the cambium — raise the knife angle. If the shaving is paper-thin and latex flow is minimal, the cut is too shallow.
- Yield check: A productive tree yields 30-100 ml latex per tapping (measured in collection cup). If yield drops below 20 ml consistently, the panel may need a rest period (skip tapping for 2-4 weeks).

**Expected Performance**:
- Per-tree yield: 30-100 ml latex per tapping (20-50 g dry rubber)
- Annual yield: 2-5 kg dry rubber per tree (200-300 tapping days/year)
- Per-hectare yield: 1000-1500 kg dry rubber/year at 500 trees/ha
- Productive lifespan: 20-30 years per tree

**Strengths**:
- Renewable resource — trees produce latex continuously for decades
- Low energy input — tapping requires only hand tools
- High rubber quality — Hevea natural rubber (cis-1,4-polyisoprene >95%) produces the strongest vulcanizates of any source

**Weaknesses**:
- Geographic restriction — *Hevea brasiliensis* requires tropical conditions (annual rainfall 1800-2500 mm, altitude below 200 m, no frost)
- Labor-intensive — tapping requires skilled manual workers; a tapper processes 200-300 trees per 3-4 hour morning shift; labor represents 50-60% of production cost
- Slow startup — trees require 5-7 years from planting to first latex production

## Coagulation and Sheet Processing

**Principle**: Formic acid or acetic acid neutralizes the negatively charged protein layer surrounding each rubber particle in the latex emulsion (pH drops from ~6.5 to ~4.5-5.0), destabilizing the colloid. Rubber particles agglomerate into a coherent soft mass (coagulum) that is then mechanically dewatered and dried.

**Prerequisites**: Fresh latex (collected same day, 30-40% rubber content, preserved with 0.3-0.7% ammonia). Coagulation tanks (aluminum or ceramic-lined, rectangular, 1-3 m long). Sheeting mill (2-4 pairs of counter-rotating steel rollers). Smokehouse (wood-fired, temperature-controlled).

**Materials**:
- Formic acid (HCOOH, 85% concentration) — 0.5% by weight of latex, or acetic acid (CH₃COOH, white vinegar) at equivalent concentration
- Fresh latex (30-40% rubber hydrocarbon)
- Firewood for smokehouse (hardwood preferred — produces creosote with antifungal properties)

**Procedure**:
1. Pour latex into coagulation tanks. Dilute to 15-20% rubber content if necessary (high-concentration latex coagulates unevenly).
2. Add formic acid at 0.5% by weight of the latex. Stir briefly (30-60 seconds) to distribute acid evenly throughout the tank.
3. Let stand 4-6 hours (accelerated method) or 12-16 hours (traditional overnight method). The coagulum floats as a solid slab above the serum (yellow liquid).
4. Remove coagulum slab from tank. Drain excess serum.
5. Pass coagulum through sheeting mill — a series of 2-4 pairs of counter-rotating steel rollers with progressively narrower gaps. Final roller pair has ribbed surfaces that imprint a pattern (ribbed smoked sheet, RSS). Final sheet thickness: ~3 mm (±0.5 mm).
6. Hang sheets on bamboo poles in smokehouse. Maintain temperature 60-70°C (±5°C). Duration: 2-4 weeks. Ensure consistent smoke density throughout — too hot (>80°C) causes surface oxidation, too cool (<50°C) allows mold growth.
7. Remove dried sheets from smokehouse. Inspect and grade (RSS 1-5 by visual quality).

**Calibration/Verification**:
- Coagulation pH: Test serum pH after acid addition. Target pH 4.5-5.0 for complete coagulation. If pH >5.5, coagulation is incomplete (add more acid in 0.1% increments).
- Dryness test: Properly dried RSS contains <0.5% moisture. Weigh a sample sheet, dry in oven at 105°C for 2 hours, reweigh. Weight loss should be <0.5%.
- Grade verification against RSS standard: RSS 1 (highest) = uniform amber color, no mold, no oxidized spots, minimal bark fragments. RSS 5 (lowest) = dark, oxidized, possible mold spots, bark inclusions. Price differential between grades: 15-25%.

**Expected Performance**:
- Coagulation yield: ~95% of rubber hydrocarbon in latex recovered as coagulum
- Sheet output: ~30 kg dry RSS per 100 liters of fresh latex (at 35% rubber content)
- Drying time: 2-4 weeks in smokehouse at 60-70°C
- Throughput: A sheeting mill processes 50-100 kg dry rubber per hour

**Strengths**:
- Simple, low-technology process — requires only tanks, rollers, and a smokehouse
- Long shelf life — properly dried and smoked RSS stores for years without degradation
- Multiple coagulant options — formic acid (fastest), acetic acid (most available), alum (alternative)

**Weaknesses**:
- Slow drying — 2-4 weeks in smokehouse limits throughput
- Grade variability — visual grading is subjective; RSS quality depends on latex freshness, acid dosage, and smokehouse conditions
- Labor-intensive sheet handling — each sheet is hung, turned, and inspected manually

## Vulcanization

**Principle**: Sulfur forms polysulfide bridges (—Sₓ—, where x = 1-8) between adjacent polyisoprene chains at the allylic carbon positions. These covalent cross-links create a three-dimensional network that prevents permanent chain slippage. Raw rubber (tensile ~1 MPa, thermoplastic, sticky) becomes a durable elastomer (tensile 20-30 MPa, elastic recovery, non-tacky).

**Prerequisites**: Masticated rubber (passed through two-roll mill at 40-80°C to soften and reduce molecular weight). Compounding ingredients measured to ±0.5% accuracy by weight. Compression mold or autoclave capable of 140-160°C and 5-20 MPa pressure.

**Materials**:
- Natural rubber (SMR 20 grade or RSS 1-3): 100 phr (parts per hundred rubber)
- Sulfur (powder, 99%+): 2-3 phr (cross-linking agent)
- CBS accelerator (N-cyclohexyl-2-benzothiazole sulfenamide): 0.5-1.5 phr (delayed-action — provides safe processing time before cure begins)
- Zinc oxide (ZnO, 99%): 5 phr (activator — forms zinc-accelerator complex)
- Stearic acid (C₁₈H₃₆O₂): 2 phr (co-activator — solubilizes ZnO in rubber matrix)
- Carbon black (N330, particle size 26-30 nm): 40-50 phr (reinforcing filler — increases tensile from ~1 MPa raw to 20-30 MPa vulcanized)
- Antioxidant (TMQ): 1-2 phr (prevents oxidative chain scission)

**Procedure**:
1. Masticate rubber on two-roll mill (roll gap 1-2 mm, temperature 40-60°C) for 5-10 minutes until rubber is soft and plastic (Mooney viscosity reduced by 20-40% from original).
2. Add stearic acid and zinc oxide. Mix 2-3 minutes on mill until uniformly dispersed.
3. Add carbon black gradually (in 4-5 portions) to prevent dusting and ensure even dispersion. Mix 5-8 minutes total. Band the rubber on the front roll and cut/fold 6-8 times to distribute filler.
4. Add antioxidant and accelerator. Mix 2 minutes. Keep mill temperature below 80°C to prevent premature cure (scorch).
5. Add sulfur last. Mix 2 minutes. Sulfur added last to minimize scorch risk during mixing.
6. Sheet off compound from mill at 3-5 mm thickness. Allow to rest 4-24 hours at room temperature (maturation period improves processing consistency).
7. Cut preform to fit mold cavity (preform weight = part weight + 5-10% for flash). Place in heated compression mold.
8. Close mold under hydraulic pressure (10-20 MPa). Cure at 140-160°C for 15-60 minutes depending on part thickness (cure time approximately doubles for every 10°C decrease in temperature). Typical cure times: 3 mm section = 15-20 min; 10 mm section = 30-40 min; 25 mm section = 50-60 min.
9. Open mold. Remove part. Trim flash at mold parting line with scissors or die trimmer.

**Calibration/Verification**:
- Cure check (simple): Cut a sample strip 100 mm × 10 mm × 2 mm from the cured part. Stretch to 300% elongation. Correctly cured rubber springs back to within 5% of original length. Undercured rubber stays permanently stretched. Overcured rubber snaps or cracks.
- Cure check (rheometer): Oscillating Disc Rheometer (ODR) measures torque vs. time at cure temperature. Target: torque reaches 90% of maximum (t90) within the specified cure time. Undercure = torque <90% of max. Overcure = torque declining after peak (reversion).
- Hardness check: Shore A durometer. Target: 60 ±5 for a typical tire compound. Measure at 3 points on the part surface; readings must agree within ±2 Shore A units.
- Tensile test: Dumbbell specimen (ASTM D412 die C). Expected tensile: 20-30 MPa. Elongation at break: 400-650%. If tensile <17 MPa, suspect undercure, poor carbon black dispersion, or contamination.

**Expected Performance**:
- Tensile strength: 17-28 MPa (vulcanized with carbon black)
- Elongation at break: 400-650%
- Shore A hardness: 40-90 (controlled by cross-link density and filler loading)
- Service temperature range: -50°C to +100°C (continuous)
- Compression set (22 hours at 70°C): 15-35%

**Strengths**:
- Predictable, controllable process — cure time and properties adjustable via sulfur and accelerator ratios
- Versatile — same basic process produces soft gaskets (Shore A 40) to hard ebonite (Shore D 80)
- Good mechanical properties — natural rubber vulcanizates have the highest tensile and tear strength of any elastomer at room temperature

**Weaknesses**:
- Temperature-sensitive cure — undercure at low temperature, reversion (network degradation) at excessive temperature or extended time
- Irreversible — once cross-linked, rubber cannot be remelted or reprocessed (must devulcanize for recycling)
- Sulfur and accelerator are skin sensitizers — handling requires gloves and ventilation

## Latex-Dipped Goods

**Principle**: Formers (shaped like the finished product — hand, cylinder, balloon) are immersed in compounded latex. On withdrawal, a liquid latex film coats the former. Drying, leaching, and curing produce a thin, strong, elastic film with superior properties to dry-mixed vulcanized rubber (tensile 20-30 MPa, elongation 700-900%).

**Prerequisites**: Compounded prevulcanized latex (sulfur-vulcanized in latex form, 60% total solids, viscosity 20-40 mPa·s at 25°C). Ceramic, glass, or aluminum formers (smooth, clean surface). Hot-air curing oven (90-110°C).

**Materials**:
- Compounded latex (60% total solids): 100 parts
- Sulfur (in latex form): 1-2 phr (dry weight basis)
- Zinc diethyldithiocarbamate (ZDEC, ultra-accelerator): 0.5-1.5 phr
- Zinc oxide dispersion: 0.5-1.0 phr
- Casein or synthetic stabilizer: 0.2-0.5 phr (prevents premature coagulation in dip bath)

**Procedure**:
1. Clean and preheat formers to 50-60°C (warm formers promote even wetting and faster initial drying).
2. Immerse formers into compounded latex bath (temperature 25-30°C). Dip time: 10-30 seconds depending on desired wall thickness.
3. Withdraw formers at controlled speed: 10-30 cm/minute. Withdrawal speed controls film thickness — faster withdrawal = thicker film due to more latex entrained. Target: 0.1-0.5 mm per dip.
4. For thicker walls (0.3-1.0 mm per dip), use coagulant dipping: pre-dip the former in calcium nitrate solution (10-20% in water/ethanol), then dip into latex. Calcium ions coagulate latex on contact, producing thicker, denser film.
5. Air-dry partially: 5-10 minutes at 50-60°C (water evaporates, rubber particles coalesce).
6. Leach in water at 50-60°C for 5-15 minutes to remove water-soluble impurities (proteins, residual ammonia — reduces latex allergy risk).
7. Cure in hot-air oven at 90-110°C for 20-40 minutes (sulfur cross-linking occurs in dried film).
8. Cool to room temperature. Strip from formers. Inspect for defects (thin spots, tears, bubbles).
9. For powder-free gloves: rinse in chlorine solution to remove surface proteins, then coat with polymer donning agent.

**Calibration/Verification**:
- Wall thickness: Measure with micrometer at 5 points around the product. Surgical gloves: 0.15-0.25 mm (±0.03 mm). Household gloves: 0.5-0.8 mm (±0.1 mm). Condoms: 0.03-0.08 mm (±0.01 mm).
- Pinhole test: Inflate gloves with 1 liter of air, submerge in water, check for bubbles (indicating pinholes). Acceptable defect rate: <1.5% for surgical gloves (AQL 1.5 per ISO 2859-1).
- Tensile test (ASTM D412): Dumbbell specimen from film. Expected tensile: 20-30 MPa. Elongation: 700-900% (higher than dry-mixed rubber due to film formation process).

**Expected Performance**:
- Tensile strength: 20-30 MPa
- Elongation at break: 700-900%
- Wall thickness: 0.03-1.0 mm (controlled by dip time, withdrawal speed, and coagulant)
- Production rate: 3000-5000 gloves/hour on a continuous dipping line (rotary machine with 30-60 formers)

**Strengths**:
- Thinnest elastic films achievable — 0.03 mm for condoms, impossible by any other rubber process
- Superior elongation (700-900%) vs. dry-mixed rubber (400-650%) due to optimal polymer chain orientation in latex film
- Low hysteresis — thin latex films generate minimal heat on repeated flexing
- Continuous, high-volume production on rotary dipping machines

**Weaknesses**:
- Latex allergy — natural rubber latex proteins sensitize 1-6% of general population, up to 17% of healthcare workers with chronic exposure
- Limited to hollow, thin-walled shapes (gloves, condoms, balloons, tubing)
- Precise viscosity control required — bath viscosity changes with temperature, evaporation, and ammonia loss; must be monitored and adjusted continuously
- Prevulcanized latex has limited shelf life (2-6 months with ammonia preservation)

## Reclaimed Rubber

**Principle**: Partially reverse sulfur cross-links in vulcanized scrap rubber to create a reusable material. Heat and chemical agents break polysulfide cross-links (—Sₓ—, where x > 2) while preserving the carbon backbone of the polymer chains. The resulting "reclaim" is a soft, plastic material blended with virgin rubber at 10-30% loading.

**Prerequisites**: Scrap rubber (tires, factory waste) — sorted and cleaned. Reclaimator or heated pan mill (150-200°C). Reclaiming agents: aryl disulfides, pine tar, or petroleum-based softeners.

**Materials**:
- Scrap rubber (vulcanized), ground to 0.5-2 mm crumb
- Aryl disulfide reclaiming agent: 2-5 phr (breaks polysulfide cross-links)
- Pine tar or petroleum softener: 5-10 phr (plasticizes the reclaimed rubber)
- Water (for cooling and washing)

**Procedure**:
1. Sort scrap rubber by type (tire tread, sidewall, inner liner — different formulations). Remove fabric and steel cord (mechanical separation — shredder, granulator, magnetic separator for steel).
2. Grind sorted scrap to 0.5-2 mm crumb using a granulator (rotary knife granulator, screen size 1-2 mm).
3. Feed crumb into heated pan mill or reclaimator at 150-200°C with reclaiming agents (aryl disulfides 2-5 phr, pine tar 5-10 phr). Processing time: 4-8 hours under mechanical shear and heat. The combination breaks polysulfide cross-links while preserving polymer backbone.
4. Discharge softened reclaim. Cool on a conveyor or cooling mill.
5. Refine on a two-roll mill (roll gap 0.1-0.3 mm) to remove remaining hard particles and produce a uniform, sheet-like product.
6. Test reclaim properties. Bale and store for blending with virgin rubber.

**Calibration/Verification**:
- Plasticity test (Williams plastometer): Compress a 2 cm³ sample between parallel plates at 70°C under 49 N load for 3 minutes. Measure final height. Reclaim plasticity should be 30-50 (lower = softer, more processing aids). Virgin rubber plasticity: 80-120.
- Tensile test: Prepare a compound of 70% virgin rubber + 30% reclaim. Cure and test. Tensile should be ≥80% of virgin-only compound. If <70%, reclaim quality is poor (insufficient devulcanization or excessive chain degradation).
- Visual: Reclaim should be homogeneous, free of hard particles and unmixed chunks. Dark brown to black color is normal.

**Expected Performance**:
- Reclaimed rubber tensile strength: 60-80% of virgin compound
- Cost: 30-50% of virgin rubber price
- Blend loading: 10-30% reclaim in virgin compound without major property loss
- Processing benefit: Reduces mixing energy by 10-20% (reclaim is softer than virgin rubber)

**Strengths**:
- Reduces waste — diverts scrap rubber from landfill (over 1 billion waste tires generated annually worldwide)
- Cost reduction — reclaim sells for 30-50% of virgin rubber price
- Processing aid — reclaim softens the compound, reducing mixing energy and improving flow in molds
- Extends rubber supply in resource-constrained environments

**Weaknesses**:
- Property degradation — reclaimed rubber has 60-80% of virgin tensile strength, reduced cross-link density after re-vulcanization
- Not equivalent to virgin rubber — cannot fully replace virgin rubber in critical applications (tire treads, high-pressure seals)
- Energy-intensive — grinding and heating to 150-200°C for 4-8 hours requires significant energy input

## Quantitative Parameters

## Vulcanization Parameters by Rubber Type

| Parameter | Natural Rubber (NR) | Nitrile (NBR) | Neoprene (CR) | EPDM |
|-----------|--------------------|-----------------|-----------------|------|
| Cure temperature (°C) | 140-160 | 150-170 | 150-180 | 150-170 |
| Cure time at temp (min) | 15-60 | 10-30 | 5-20 | 10-30 |
| Sulfur (phr) | 2-3 | 1-2 | 0 (metal oxide) | 1-2 |
| Accelerator (phr) | 0.5-1.5 | 0.5-2.0 | 0 (ZnO/MgO) | 0.5-1.5 |
| Tensile strength (MPa) | 20-30 | 15-28 | 10-25 | 7-21 |
| Elongation at break (%) | 400-650 | 300-600 | 300-600 | 150-600 |
| Service temp range (°C) | -50 to +100 | -40 to +120 | -40 to +120 | -50 to +150 |
| Shore A hardness range | 40-90 | 40-90 | 40-80 | 40-80 |

## Molding Methods Comparison

| Method | Pressure (MPa) | Temp (°C) | Cycle Time | Best For |
|--------|----------------|-----------|------------|----------|
| Compression molding | 5-20 | 140-160 | 15-60 min | Seals, gaskets, simple parts |
| Transfer molding | 5-15 | 140-160 | 10-30 min | Complex seals, bonded parts |
| Injection molding | 50-200 | 140-170 | 2-10 min | High-volume O-rings, bushings |

## Rubber Grades and Specifications

| Grade | Dirt Content | Ash | Source | Primary Use |
|-------|-------------|-----|--------|-------------|
| SMR 5 | ≤0.05% | ≤0.6% | [Hevea](./natural.md) | Critical applications |
| SMR 20 | ≤0.10% | ≤0.6% | [Hevea](./natural.md) | Standard tire grade |
| SMR 50 | ≤0.20% | ≤0.8% | [Hevea](./natural.md) | General purpose |
| RSS 1 | Visual | Visual | [Hevea](./natural.md) | Premium rubber |
| RSS 5 | Visual | Visual | [Hevea](./natural.md) | General purpose |

## Scaling Notes

- **Single tree**: 2-5 kg/year — sufficient for small-scale sealing and gasket production
- **Small plantation (5 ha, 2500 trees)**: 5,000-7,500 kg/year — supports local tire repair, hose manufacturing, and seal production
- **Industrial plantation (100+ ha)**: 100,000-150,000 kg/year — supports tire manufacturing, large-scale molded goods
- **Labor bottleneck**: Tapping resists mechanization — each tree requires a skilled worker making a precision cut. A tapper processes 200-300 trees in a 3-4 hour morning shift. Scaling beyond ~500 trees requires additional tappers, not faster tapping.
- **Smokehouse scaling**: A 2 × 3 × 2 m smokehouse dries ~200 kg RSS in 2-4 weeks. Larger operations use multiple smokehouses or continuous tunnel driers.
- **Molding scaling**: Compression molding is manual and slow (15-60 min cycle). Transfer and injection molding reduce cycle times to 2-10 minutes but require more complex tooling ($5,000-50,000 for injection molds vs. $500-5,000 for compression molds).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Porous or blistered vulcanizate | Moisture in compound, insufficient mold venting | Dry compound before molding (80°C for 2 hours); add vent channels to mold |
| Undercure (soft, tacky surface) | Insufficient cure time or temperature; dead accelerator | Increase cure time 5-10 min; verify mold temperature with thermocouple; check accelerator shelf life |
| Overcure/reversion (brittle, darkened) | Excessive cure time or temperature for natural rubber | Reduce cure time; lower mold temperature; switch to EV (efficient vulcanization) system: lower sulfur (0.4-0.8 phr), higher accelerator (2-5 phr) |
| Poor carbon black dispersion (visible streaks) | Insufficient mixing time on mill or in Banbury | Increase mixing time; add carbon black in smaller portions; check mill roll gap (1-2 mm) |
| Sticking to mold | Insufficient mold release or mold surface degraded | Apply silicone or zinc stearate mold release; polish mold surface; chrome-plate mold cavity |
| Flash too thick | Insufficient clamp pressure or excess material in preform | Increase press pressure; reduce preform weight to part weight + 5-8% |
| Latex coagulation too fast or uneven | Acid concentration too high; latex diluted incorrectly | Reduce acid to 0.3-0.4%; dilute latex to 15-20% rubber before adding acid |
| Mold growth on RSS sheets | Smokehouse temperature too low (<50°C) or humidity too high | Increase smokehouse temperature to 60-70°C; improve ventilation; check fire is producing adequate smoke |

## Safety

- **Latex allergies**: Natural rubber latex proteins sensitize some individuals, causing reactions from contact dermatitis to anaphylactic shock (Type I hypersensitivity in 1-6% of general population, up to 17% of healthcare workers with chronic exposure). Use [nitrile alternatives](./synthetic.md) for allergic workers. Powdered latex gloves aerosolize proteins — use powder-free.
- **Vulcanization accelerators**: Mercaptobenzothiazole (MBT), thiurams (TMTD), and CBS are skin sensitizers causing occupational dermatitis. Handle compounding ingredients with nitrile gloves (not latex). Use local exhaust ventilation during weighing and mixing.
- **Dust explosion risk**: Fine rubber crumb, carbon black, and sulfur powder form explosive dust-air mixtures. Carbon black dust MEC: ~50 g/m³. Sulfur dust MEC: ~35 g/m³. Use local exhaust ventilation during mixing and milling. Ground all equipment to prevent static ignition. No open flames in mixing areas.
- **Vulcanization burns**: Autoclave steam at 3-10 bar (144-180°C saturation temperature) and press platens at 140-180°C cause severe scalds and thermal burns. Use thermal gloves rated to 200°C and face shields when handling hot molds. Never open autoclave door under pressure — verify pressure gauge reads 0 bar before opening.
- **Ammonia fumes** (latex preservation): Latex preserved with 0.3-0.7% ammonia releases NH₃ vapor. Irritating to eyes and respiratory tract above 25 ppm. OSHA PEL: 50 ppm (8-hour TWA). Use local exhaust ventilation in latex storage and processing areas.

## Quality Control

## Incoming Rubber
- **Moisture content**: Weigh 10 g sample, dry at 105°C for 2 hours, reweigh. Accept: <0.5% moisture loss.
- **Dirt content**: Dissolve 10 g rubber in toluene, filter through 44 μm sieve, weigh residue. SMR 20: ≤0.10% dirt.
- **Plasticity Retention Index (PRI)**: Measure Wallace plasticity at 100°C before and after aging at 140°C for 30 minutes. PRI = (P30/P0) × 100. SMR 20: PRI ≥60. Low PRI indicates oxidative degradation during processing.

## Vulcanizate Testing
- **Tensile strength**: ASTM D412 dumbbell specimen. Target: 17-28 MPa for NR with 40-50 phr N330 carbon black.
- **Elongation at break**: Same specimen as tensile test. Target: 400-650%.
- **Hardness**: Shore A durometer (ASTM D2240). Measure at 3 points; ±2 units agreement required.
- **Compression set**: ASTM D395, Method B. 22 hours at 70°C, 25% deflection. Target: <30% (lower = better elastic recovery).

## Field Tests (No Lab Equipment)
- **Cure test**: Stretch a 100 mm strip to 300% elongation. Good cure springs back within 5% of original length. Undercure = permanent stretch. Overcure = cracking/snapping.
- **Hardness thumb test**: Press thumbnail firmly into surface. Shore A 40-60 rubber indents slightly. Shore A 70-90 resists indentation. Not precise but useful for quick checks.

## Variations and Alternatives

## Alternative Rubber Sources (Non-Tropical)

| Source | Yield (kg/ha/year) | Climate | Rubber Quality | Notes |
|--------|-------------------|---------|---------------|-------|
| [Guayule](../glossary/guayule.md) | 500-1000 | Arid, temperate | Near-identical to Hevea (cis-1,4-polyisoprene >95%) | Whole shrub harvested every 2-3 years; flotation extraction |
| [Russian dandelion](../glossary/russian-dandelion.md) | 150-500 | Temperate | Similar to Hevea | Root extraction; annual crop; USSR produced 3000 tonnes/year during WWII |
| *Hevea brasiliensis* | 1000-1500 | Tropical only | Benchmark standard | Requires 1800-2500 mm annual rainfall, no frost |

## Alternative Cross-Linking Systems

- **Efficient vulcanization (EV)**: Lower sulfur (0.4-0.8 phr), higher accelerator (2-5 phr). Produces mono- and disulfide cross-links (more thermally stable than polysulfide). Better reversion resistance. Tradeoff: lower tear strength and fatigue resistance. Use for thick sections and high-temperature service.
- **Peroxide cure**: Dicumyl peroxide (1-3 phr) creates carbon-carbon cross-links. No sulfur needed. Superior heat aging. Used for silicone and EPDM. Not effective for natural rubber (causes chain scission at allylic positions).
- **Metal oxide cure** (for neoprene): ZnO (5 phr) + MgO (4 phr). No sulfur. MgO scavenges HCl released during aging. See [Synthetic Polymers](./synthetic.md) for details.

## Synthetic Elastomers

When natural rubber properties are insufficient, synthetic elastomers fill specific niches. See [Synthetic Polymers](./synthetic.md) for complete details:
- **Nitrile (NBR)**: Oil and fuel resistance
- **Neoprene (CR)**: Flame retardant, ozone resistant
- **Silicone (PDMS)**: -60 to +250°C service range
- **Polyurethane (PU)**: Tunable from rigid foam to abrasion-resistant elastomer
- **EPDM**: Ozone and weather resistant, roofing and automotive seals

## See Also

- **[Natural Rubber & Vulcanization](natural.md)**: Detailed tapping techniques, latex chemistry, and cure control
- **[Vulcanization & Hardness Scales](rubber.vulcanization.md)**: Cure systems (CV, EV, SEV), Shore A/D hardness scales, compounding ingredients
- **[Synthetic Polymers](synthetic.md)**: Synthetic elastomers (NBR, neoprene, silicone, PU, SBR)
- **[Semiconductor Applications](rubber.semiconductor-apps.md)**: Elastomers in semiconductor equipment, chemical resistance table
- **[Gutta-Percha](gutta-percha.md)**: Non-elastomeric natural polyisoprene (trans-1,4)
- **[Shellac](shellac.md)**: Natural resin from lac bug
- **[Composites](composites.md)**: Rubber-modified composites and impact-resistant laminates
- **[Carbon Black](../energy/charcoal.md)**: Production of carbon black reinforcing filler
- **[Alkalis](../chemistry/alkalis.md)**: Zinc oxide and sulfur production
- **[Gas Handling](../gas-handling/basic.md)**: Rubber seals, gaskets, and O-rings for gas systems
- **[Coatings](../chemistry/coatings.md)**: Rubber-based coatings and sealants
- **[Machine Tools](../machine-tools/joining.md)**: Equipment for rubber processing machinery


[← Back to Polymers & Composites](index.md)
