# Crop Rotation & Nutrient Cycling

> **Node ID**: agriculture.crop-rotation
> **Domain**: [Agriculture](./index.md)
> **Dependencies**: [`agriculture`](./index.md), [`agriculture.soil-management`](soil-management.md), [`foundations.food-agriculture`](../foundations/food-agriculture.md)
> **Enables**: [`food-processing`](../food-processing/index.md), [`chemistry.ammonia`](../chemistry/ammonia.md)
> **Timeline**: Years 0-10+
> **Outputs**: sustained_soil_fertility, nitrogen_fixation, diversified_crops
> **Critical**: Yes — without rotation, continuous cropping depletes soil in 3-5 years, making long-term agriculture impossible

## 1. Overview

Crop rotation is the practice of growing a planned sequence of different crop species on the same land across successive growing seasons. The fundamental principle is that different crops have different nutrient demands, root depths, pest associations, and growth habits. By alternating crops, the farmer exploits these differences to break pest cycles, replenish soil nutrients, manage soil structure, and reduce weed pressure — all without external chemical inputs.

Without crop rotation, growing the same crop repeatedly on the same land (monoculture) depletes specific nutrients, builds up crop-specific pathogens and pests, and degrades soil structure. Historical data is unambiguous: continuous wheat cropping on temperate soils without fertilizer inputs yields 1.5-2.0 tonnes/ha in year one, declining to 0.5-0.8 tonnes/ha by year five and 0.2-0.4 tonnes/ha by year ten. The same land under a well-managed rotation sustains 1.5-3.0 tonnes/ha indefinitely.

The most powerful element of rotation is nitrogen fixation by legumes. Leguminous crops (beans, peas, clover, vetch, lentils, alfalfa) host Rhizobium bacteria in root nodules that convert atmospheric N₂ to plant-available ammonium (NH₄⁺). A good legume stand fixes 40-200 kg N/ha per season — enough to supply the nitrogen needs of the following grain crop without any synthetic fertilizer. This biological nitrogen fixation is the primary nitrogen source for agriculture in a bootstrapping civilization and remains relevant even after [Ammonia Production](../chemistry/ammonia.md) is established, as a free, low-energy supplement.

## 2. Prerequisites

**Materials**:
- Diverse seed stock: at minimum one grain, one legume, and one root/brassica crop
- Compost or manure for supplemental fertility (see [Soil Management](soil-management.md))
- Legume seed inoculated with appropriate Rhizobium strain (for new land — established soils usually have native populations)

**Tools and equipment**:
- [Hoes and digging sticks](../foundations/tools-basic.md) for bed preparation
- [Plow](../foundations/tools-basic.md) or [draft animal](../animals/draft-power.md) for larger areas
- [Sickle or scythe](../foundations/tools-basic.md) for harvesting
- [Storage infrastructure](../foundations/food-agriculture.md) (granary, root cellar) for multiple crop types

**Knowledge**:
- Identification of crop families (legumes, brassicas, grasses, roots) — rotate between families, not within
- Legume nodulation assessment (dig up roots, check for pink nodules = active N fixation)
- Basic soil observation: color, texture, earthworm count, compaction
- Seasonal timing for each crop in the rotation sequence

**Infrastructure**:
- Sufficient land to divide into at least 3 sections (rotation requires fallow or alternate crop sections)
- [Irrigation](irrigation.md) or adequate rainfall (500+ mm during growing season)
- Record-keeping system (even simple tally marks) to track what was planted where and when

## 3. Bill of Materials

### Three-Field Rotation (1 Hectare per Field, 3 Hectare Total)

| Material | Quantity per Cycle | Source | Alternatives |
|----------|-------------------|--------|-------------|
| Grain seed (wheat, rye, or barley) | 50-100 kg | [Seed Saving](seed-saving.md) or [Foundations → Agriculture](../foundations/food-agriculture.md) | Oats, triticale |
| Legume seed (beans, peas, or clover) | 30-80 kg | [Seed Saving](seed-saving.md) | Vetch, lentils, alfalfa |
| Compost or manure (top-dressing) | 3-5 tonnes/ha for grain field | [Soil Management](soil-management.md) | Green manure (plow-under legume crop) |
| Wood ash (pH amendment) | 200-500 kg if pH <6.0 | [Fire-Making](../foundations/fire.md) | Lime (requires [Chemistry → Lime](../ceramics/lime.md)) |
| Legume inoculant (if new land) | 100-200 g Rhizobium culture | Purchase or soil from established legume field | Native soil transfer from nearby legume plots |

### Four-Field Norfolk Rotation (1 Hectare per Field, 4 Hectare Total)

| Material | Quantity per Cycle | Source | Alternatives |
|----------|-------------------|--------|-------------|
| Wheat seed | 50-100 kg | [Seed Saving](seed-saving.md) | Rye, barley |
| Turnip or root crop seed | 1-3 kg | [Seed Saving](seed-saving.md) | Radish, beet, carrot |
| Barley or oat seed | 50-80 kg | [Seed Saving](seed-saving.md) | Rye |
| Clover seed | 8-15 kg | [Seed Saving](seed-saving.md) | Alfalfa, vetch |

## 4. Process Description

### 4.1 Three-Field Rotation (Medieval Standard)

The simplest effective rotation. Divide available land into three equal sections.

**Year 1 — Field A: Grain / Field B: Legume / Field C: Fallow**
1. **Field A (grain)**: Prepare seedbed in spring (or autumn for winter wheat). Sow grain at 50-100 kg/ha. Weed every 2-3 weeks. Harvest in late summer. Yield target: 1.0-2.0 tonnes/ha. This field depletes nitrogen (removes 40-60 kg N/ha in grain).
2. **Field B (legume)**: Sow beans, peas, or clover in spring. Legumes fix 40-80 kg N/ha through root nodules. Harvest grain from beans/peas or use clover as green manure (plow under before flowering). The legume crop restores nitrogen to the soil.
3. **Field C (fallow)**: Leave unplanted. Cultivate (hoe or shallow-plow) 2-3 times during the season to control weeds and break soil surface crusting. Fallow year allows soil moisture recovery and organic matter decomposition.

**Year 2 — Rotate: Field A → Legume / Field B → Fallow / Field C → Grain**

**Year 3 — Rotate: Field A → Fallow / Field B → Grain / Field C → Legume**

 After three years, each field has been through one cycle of grain (depletes N), legume (restores N), and fallow (recovers structure). The cycle repeats indefinitely.

**Strengths**:
- Simple to plan and execute — only 3 fields and 3 phases to track
- Requires no additional inputs beyond seed — the legume phase generates nitrogen biologically
- Fallow year allows soil moisture recovery in semi-arid climates (saves 50-100 mm of water)

**Weaknesses**:
- 33% of land is unproductive (fallow) each year — reduces total output by one-third
- Nitrogen balance is marginal — net balance of -2 to +5 kg N/ha/year means slow fertility building
- No livestock integration — animal manure, a major fertility source, is not part of the system

### 4.2 Four-Field Norfolk Rotation

Eliminates the unproductive fallow year by substituting a root crop that cleans the land (intensive weeding during root crop cultivation) and a clover ley that fixes nitrogen while providing animal fodder.

**Year 1: Wheat** — Heavy nitrogen feeder. Produces grain for human consumption.
**Year 2: Turnips (or other root crop)** — Light nitrogen feeder. Intensive hand-weeding of root crop cleans the field of weeds. Turnip tops and roots provide winter animal feed. Roots break up deep soil compaction.
**Year 3: Barley or oats** — Moderate nitrogen feeder. Straw used for animal bedding and thatch.
**Year 4: Clover** — Nitrogen fixer (80-150 kg N/ha). Grazed by animals (manure deposited directly on field) or cut for hay, then plowed under as green manure before autumn wheat sowing.

 The Norfolk rotation doubled agricultural output per hectare compared to the three-field system by eliminating fallow and integrating livestock. It was the agricultural foundation of the British Agricultural Revolution (18th century).

**Strengths**:
- 100% of land is productive every year — no fallow period wastes space
- Root crop phase provides intensive weed control through hand-weeding, cleaning the field for subsequent crops
- Integrates livestock through clover grazing — manure deposited directly on the field recycles nutrients

**Weaknesses**:
- Requires 4 distinct crop types and sufficient seed stock for all 4 — higher seed management complexity
- Root crops (turnips) have lower market value than grain in many economies
- Demands more labor than the three-field system, particularly during the root crop weeding phase (10-20 person-hours/ha)

### 4.3 Legume Planting and Nodulation Check

1. **Inoculate seed** (if needed): If planting legumes on land that has not grown legumes in 3+ years, coat seed with appropriate Rhizobium inoculant. Mix inoculant powder with seed at planting using a sticky solution (milk or sugar water) to adhere bacteria to seed coat.
2. **Plant at correct depth**: Beans 3-5 cm, peas 2-4 cm, clover 0.5-1.5 cm. Legume seeds are sensitive to planting depth — too deep and they cannot emerge.
3. **Check nodulation** (4-6 weeks after emergence): Carefully dig up 5-10 plants across the field. Examine roots for nodules (small round bumps 1-5 mm diameter). Cut open a nodule: pink/red interior = active N fixation (leghemoglobin indicates functioning). Green/white interior = inactive or ineffective Rhizobium strain.
 4. **If nodulation is poor** (<5 nodules per plant, or white interior): The soil may lack the correct Rhizobium strain. Re-inoculate by applying Rhizobium culture in solution to the soil surface, or transfer soil from a field where the same legume species nodulated successfully.

**Strengths**:
- Biological nitrogen fixation provides 40-200 kg N/ha per season at zero energy cost
- Nodulation check is a simple visual test (dig, inspect, cut open) requiring no instruments
- Rhizobium inoculant, once established, persists in soil for years without re-application

**Weaknesses**:
- Rhizobium strains are species-specific — the wrong strain produces white, ineffective nodules
- Acidic soils (pH <5.5) inhibit Rhizobium survival — pH correction with lime is required before legumes will nodulate
- Inoculant may not be available in a bootstrap scenario — relies on transferring soil from existing legume fields

### 4.4 Green Manure Management

1. **Sow the green manure crop**: After grain harvest, broadcast clover, vetch, or rye seed onto the field. Lightly rake to cover seed. Target seeding rate: 10-20 kg/ha for clover, 15-25 kg/ha for vetch, 80-120 kg/ha for rye.
2. **Allow growth**: Green manure grows through the fallow period, protecting soil from erosion, suppressing weeds, and (if legume) fixing nitrogen.
3. **Terminate at the right time**: For legumes, plow under at early flowering (maximum N content in biomass). For rye, terminate before seed set to prevent volunteering. Cut or mow the stand, then incorporate into the top 15-20 cm of soil with a plow or heavy hoe.
 4. **Wait 2-4 weeks before planting**: Green manure biomass needs time to decompose. Fresh green material can tie up nitrogen temporarily as soil microbes consume it. After decomposition, the nitrogen is released in plant-available form.

**Strengths**:
- Legume green manures fix 40-120 kg N/ha while protecting soil from erosion
- Cover crops suppress weeds physically (canopy competition) and chemically (rye allelopathy)
- Increases soil organic matter by 0.2-0.5% per year with regular cover cropping

**Weaknesses**:
- 2-4 week waiting period between incorporation and planting delays the next crop
- Fresh green material causes temporary nitrogen tie-up as soil microbes decompose it
- Rye cover crop must be terminated before seed set or it volunteers as a weed in the next crop

## 5. Quantitative Parameters

### Nitrogen Budget by Rotation System (kg N/ha/year)

| Rotation | Year 1 | Year 2 | Year 3 | Year 4 | Average N Balance |
|----------|--------|--------|--------|--------|-------------------|
| Continuous wheat | -50 to -70 | -50 to -70 | -50 to -70 | — | -55 to -70 (depleting) |
| 3-field (grain/legume/fallow) | -55 (wheat) | +50 (beans) | 0 (fallow) | — | -2 to +5 (near balance) |
| 4-field Norfolk | -55 (wheat) | -20 (turnips) | -40 (barley) | +100 (clover) | — | -4 to +5 (sustainable) |
| Grain/clover (2-field) | -55 (wheat) | +120 (clover) | — | — | +32 (surplus) |

### Legume Nitrogen Fixation Rates

| Legume Species | N Fixed (kg/ha/season) | Growing Season | Biomass Yield (tonnes/ha) | Best Use |
|---------------|------------------------|---------------|--------------------------|----------|
| Alfalfa (lucerne) | 150-250 | Perennial, 3-5 years | 8-15 | Hay, green manure, multi-year ley |
| Clovers (red/white) | 80-200 | Annual to perennial | 4-10 | Green manure, grazing, hay |
| Vetch (hairy) | 60-120 | Annual, winter or spring | 3-6 | Winter cover, green manure |
| Peas (field) | 50-90 | Annual, 90-120 days | 2-4 | Grain harvest + residue |
| Beans (fava/broad) | 40-80 | Annual, 90-150 days | 2-5 | Grain harvest + residue |
| Lentils | 30-60 | Annual, 80-110 days | 1-2 | Grain harvest + residue |
| Soybeans | 50-120 | Annual, 100-150 days | 2-4 | Grain + oil + residue |
| Lupins | 60-130 | Annual, 120-180 days | 3-6 | Grain + green manure |

### Yield Impact of Rotation vs. Monoculture

| System | Wheat Yield (tonnes/ha) | Year 1 | Year 5 | Year 10 | Trend |
|--------|------------------------|--------|--------|---------|-------|
| Continuous wheat, no inputs | — | 1.8 | 0.7 | 0.3 | Declining to failure |
| Continuous wheat, compost only (5 t/ha/yr) | — | 1.8 | 1.2 | 1.0 | Declining, stabilizing at low level |
| 3-field rotation, no compost | — | 1.5 | 1.3 | 1.4 | Stable |
| 4-field Norfolk, no compost | — | 1.8 | 1.6 | 1.7 | Stable-slightly increasing |
| 4-field Norfolk + 5 t/ha/yr compost | — | 2.0 | 2.2 | 2.5 | Increasing (building organic matter) |

### Soil Organic Matter Targets

| Soil Management Level | Organic Matter (%) | Water Holding Capacity (L/m³) | Earthworms per m² | Crop Yield Index |
|-----------------------|--------------------|------------------------------|--------------------|-----------------|
| Degraded (continuous monoculture) | 0.5-1.5 | 100-150 | 0-5 | 0.3-0.5 |
| Minimum rotation (3-field) | 1.5-2.5 | 150-200 | 10-30 | 0.7-0.9 |
| Good rotation + compost (4-field) | 2.5-4.0 | 200-300 | 30-100 | 1.0-1.3 |
| Excellent rotation + compost + cover crops | 4.0-6.0 | 300-400 | 100-300 | 1.3-1.8 |

### Cover Crop Seeding Rates and Biomass Production

| Cover Crop | Seeding Rate (kg/ha) | Biomass in 90 days (tonnes/ha) | N Content of Biomass (kg/ha) | Winter Kill? |
|------------|---------------------|-------------------------------|------------------------------|-------------|
| Winter rye | 80-120 | 3-6 | 30-60 | No (very hardy) |
| Crimson clover | 15-25 | 2-4 | 50-100 | Partial (to -10°C) |
| Hairy vetch | 20-35 | 3-5 | 60-120 | Partial (to -15°C) |
| Field peas | 60-100 | 2-4 | 40-80 | Yes (below -5°C) |
| Buckwheat | 40-60 | 2-4 | 20-40 | Yes (frost sensitive) |
| Radish (daikon) | 8-15 | 3-6 | 25-50 | Yes (below -5°C) |

## 6. Scaling Notes

**Household garden (0.05-0.1 ha)**: Rotate crops within a single garden by moving crop families between beds each season. No formal division needed. Even simple rotation (beans → greens → roots) provides noticeable benefit. Record-keeping: draw a sketch map each season.

**Family farm (1-3 ha)**: Divide land into 3-4 physical sections with permanent paths or markers. Apply 3-field or 4-field rotation at the section level. One person manages the rotation with seasonal planning. The key challenge is maintaining discipline: it is tempting to plant the most profitable crop on every section every year.

**Village agriculture (10-50 ha)**: Rotation scheduling becomes a communal activity. Common fields rotate as a unit. Open-field systems (historical England, continental Europe) enforced rotation through communal agreement — all farmers in a field section planted the same rotation phase. This prevented free-riding (one farmer growing grain while neighbors grow legumes to restore the shared soil).

**Regional agriculture (100+ ha)**: Multiple rotation blocks, each at a different phase. Crop diversity increases: 6-8 year rotations incorporating multi-year ley (grass/clover pasture grazed by livestock for 2-3 years). Livestock integration becomes essential for cycling nutrients through manure. This is the scale where [Draft Power](../animals/draft-power.md) becomes mandatory for timely field operations.

**Key bottleneck**: Legume seed supply. Every rotation system requires large volumes of legume seed. Save 10-20% of the legume harvest for seed (see [Seed Saving](seed-saving.md)). Without sufficient legume seed, the rotation collapses back to continuous grain cropping.

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Legumes not fixing nitrogen (poor growth, yellow leaves) | No nodulation (wrong Rhizobium strain or acidic soil pH <5.5) | Check nodulation at 6 weeks; apply inoculant; test and correct soil pH with lime or wood ash to 6.0-7.0 |
| Crop yields declining despite rotation | Rotation too short (2-field with grain/legume), or legume phase not long enough | Extend to 3- or 4-field rotation; add compost at 3-5 t/ha/yr; include a cover crop phase |
| Weed pressure increasing in legume phase | Legume canopy not closing (low seeding rate or poor establishment) | Increase legume seeding rate 20-30%; broadcast more thickly; interplant with a nurse crop (oats at 20 kg/ha) |
| Root crops failing in rotation | Soil compaction from previous grain crop; insufficient phosphorus | Deep-dig or plow before root crop phase; apply bone meal or rock phosphate if available; ensure soil is loose to 25-30 cm |
| Clover ley not establishing | Poor seed-to-soil contact, drought during establishment, or incorrect planting depth | Broadcast seed, then roll or tread to press seed into soil; plant before rain; clover seed should be 0.5-1.5 cm deep |
| Fields uneven in productivity | Inherent soil variation (slope, drainage, texture) not accounted for in rotation | Sub-divide fields into management zones based on soil type; adjust rotation by zone (longer legume phase on poorer sections) |
| Volunteers from previous crop contaminating current crop | Grain or seed dropped during harvest germinates in next crop | Clean-harvest the field (collect all grain); hand-pull volunteers in first 4 weeks; increase crop contrast between rotation phases |

## 8. Safety

- **Legume toxicity**: Some legume species contain toxins that require processing. Raw fava beans cause favism (hemolytic anemia) in susceptible individuals. Raw kidney beans contain phytohaemagglutinin — always boil for 10+ minutes. Lupin beans contain bitter alkaloids — soak in running water for days or select sweet varieties.
- **Moldy hay and silage**: Spoiled legume hay (clover, alfalfa) can contain mycotoxins and botulism spores. Do not feed moldy hay to livestock. Store hay under cover, off the ground, with ventilation.
- **Nitrate accumulation in stressed crops**: Drought-stressed or frost-damaged annual ryegrass, oats, and sorghum can accumulate nitrates to toxic levels. Test suspect forage before feeding to livestock. Dilute with low-nitrate feed.
- **Sweet clover poisoning**: Moldy sweet clover (Melilotus) hay contains dicoumarol, an anticoagulant. Animals hemorrhage internally. Do not feed moldy sweet clover hay.
- **Physical injury during field operations**: Plowing, hoeing, and harvesting involve repetitive strain and sharp tools. Rotate tasks between workers. Use ergonomic tool handles (straight, not curved, for hoes). Sharpen tools regularly — dull tools require more force and cause more accidents.

## 9. Quality Control

### Rotation Effectiveness Indicators

| Indicator | Measurement Method | Target | Warning Threshold |
|-----------|-------------------|--------|-------------------|
| Legume nodulation (6 weeks after planting) | Dig 10 plants, count pink nodules per plant | >10 pink nodules/plant | <5 nodules or all white |
| Soil organic matter | Loss-on-ignition test (dry soil, weigh, burn at 400°C, re-weigh) | >2.5% | <1.5% |
| Grain yield trend | Record yield per field per year | Stable or increasing | >15% decline over 3 years |
| Weed seed bank | Germination test: sample soil, spread on moist surface, count seedlings | <50 seedlings/m² | >200 seedlings/m² |
| Earthworm count | Dig 30×30×30 cm soil block, hand-sort, count earthworms | >30 per block | <10 per block |
| Post-harvest nitrate level | Soil test (colorimetric test strip) | 10-30 mg N/kg | <5 mg/kg (deficient) or >50 mg/kg (excess leaching risk) |

### Crop Performance Benchmarks

| Crop in Rotation | Yield Target (tonnes/ha) | N Removed in Harvest (kg/ha) | Residue Returned to Soil (kg N/ha) |
|-----------------|-------------------------|------------------------------|-----------------------------------|
| Wheat (grain only) | 1.5-2.5 | 35-55 | 15-25 (in straw if plowed under) |
| Barley (grain only) | 1.5-2.5 | 30-45 | 12-20 |
| Beans (grain harvested) | 1.0-2.0 | 25-45 | 20-40 (in leaves + stems) |
| Clover (green manure, plowed) | 3-6 biomass | 0 (all returned) | 80-200 (total biomass N) |
| Turnips (roots harvested) | 3-5 roots | 20-35 | 10-20 (in tops if returned) |

## 10. Variations and Alternatives

### Rotation Systems Comparison

| System | Fields | Fallow Years | N Balance (kg/ha/yr) | Annual Productivity | Complexity |
|--------|--------|-------------|----------------------|--------------------|-----------|
| 2-field (grain/fallow) | 2 | 50% | -25 to -35 | 50% of land producing | Lowest |
| 3-field (grain/legume/fallow) | 3 | 33% | -2 to +5 | 67% of land producing | Low |
| 4-field Norfolk | 4 | 0% | -4 to +5 | 100% of land producing | Medium |
| 6-field diversified | 6 | 0% | +5 to +15 | 100% of land producing | Higher |
| Perennial ley (3 yr grass/2 yr crops) | 5 | 0% | +10 to +30 | 40% in crops, 60% in pasture | Higher |

### Climate-Adapted Rotations

| Climate | Rotation Pattern | Key Adaptation |
|---------|-----------------|---------------|
| Temperate, adequate rainfall | Wheat → clover → oats → turnips | Standard Norfolk, 4-year cycle |
| Mediterranean (winter rain) | Wheat → chickpeas → barley → fallow | Legumes planted in autumn with first rains; fallow conserves moisture |
| Semi-arid (300-500 mm) | Wheat → fallow → wheat → legume | Extended fallow to conserve moisture; legume when soil moisture permits |
| Tropical wet-dry | Rice → legume (cowpea/mung bean) → rice → fallow | Rice in wet season; legume in dry season using residual moisture |
| Boreal/short season | Oats → peas → barley → undersown clover | Fast-maturing varieties; clover frost-seeded into grain in spring |
| Subtropical (monsoon) | Rice → wheat → mung bean | Three crops per year on same land with irrigation; extremely productive |

### Historical Crop Rotation Systems

- **Ancient Egypt (Nile basin)**: No formal rotation — annual Nile flooding deposited fresh silt, naturally restoring fertility. The closest thing to a "rotation-free" system, but dependent on a unique geological cycle.
- **Roman 2-field**: Grain → fallow. Half the land unproductive each year. Sustained Roman agriculture for centuries but limited carrying capacity.
- **Medieval 3-field**: Grain → legume → fallow. Introduced legume phase (beans, peas). The first systematic rotation. Increased carrying capacity by 30-50% over 2-field.
- **Norfolk 4-field** (18th century): Wheat → turnips → barley → clover. Eliminated fallow, integrated livestock, doubled output per hectare. The agricultural basis for the Industrial Revolution's freed labor.

## 11. References

- [Foundations → Agriculture & Food Production](../foundations/food-agriculture.md) — basic cultivation methods, grain yields, food preservation
- [Agriculture → Soil Management](soil-management.md) — composting, biochar, pH management, organic matter building
- [Agriculture → Seed Saving](seed-saving.md) — legume seed production and storage for rotation continuity
- [Agriculture → Irrigation](irrigation.md) — water supply for cover crop and green manure establishment
- [Chemistry → Ammonia Production](../chemistry/ammonia.md) — synthetic nitrogen fertilizer (the industrial replacement for biological fixation)
- [Food Processing](../food-processing/index.md) — processing of diverse rotation crops (grains, legumes, oilseeds)
- [Animals → Draft Power](../animals/draft-power.md) — animal-powered plowing for rotation field operations
- [Plants → Edible Plants](../plants/edible-plants.md) — crop species selection for regional conditions

---

*Part of the [Bootciv Tech Tree](../index.md) • [Agriculture](./index.md) • [All Domains](../index.md)*
