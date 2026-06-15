# Traditional Preservation (Drying, Salting, Smoking)

> **Node ID**: food-processing.traditional-preservation
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: `ceramics`, [`health.sanitation`](../health/sanitation.md),
> [`mining.salt`](../mining/salt.md)
> **Enables**: None
> **Critical**: No — traditional preservation extends storage life but requires no industrial infrastructure
> **Timeline**: Years 0+
> **Outputs**: dried_food, salted_food, smoked_food

## Overview

Traditional preservation methods — drying, salting/curing, smoking, sugaring, and oil packing — are the oldest food preservation techniques, achievable with stone-age technology. Each method either removes water (drying, sugaring) or creates hostile chemistry (salt osmotic pressure, smoke antimicrobial compounds, oil oxygen barrier) to inhibit microbial growth. These methods eliminate seasonal starvation cycles and enable food transport and storage without any industrial infrastructure.

Drying reduces water activity (aw) below 0.60, where no microorganism can grow. Salting at 20-30% NaCl draws water from microbial cells via osmosis, creating aw 0.65-0.75 that inhibits most bacteria. Smoking deposits phenolic antimicrobial compounds (guaiacol, syringol) and simultaneously dries the food surface. Sugaring at >60% sugar concentration creates osmotic pressure equivalent to heavy salting. Oil packing excludes oxygen, preventing oxidative rancidity and aerobic microbial growth. Fermentation — covered in [Food Fermentation](fermentation.md) — uses lactic acid bacteria to drop pH below 4.6.

These methods appear at Year 0 of the bootstrap chain because they require only basic materials: sunlight, salt, wood, and ceramic vessels. They depend on [ceramics](../ceramics/index.md) for storage vessels, [mining](../mining/salt.md) for salt, and [health sanitation](../health/sanitation.md) knowledge of basic hygiene to prevent re-contamination. For other preservation methods, see [Canning & Thermal Sterilization](canning.md), [Food Fermentation](fermentation.md), [Pasteurization](pasteurization.md), and [Refrigeration](refrigeration.md).

## Prerequisites

### Materials

- **Fresh produce or meat** — from [agriculture](../foundations/food-agriculture.md) or wild forage
- **Salt (NaCl)** — 20-30 kg per 100 kg food for heavy cure; 10-15 kg for light cure. From [mining](../mining/salt.md) (rock salt) or solar evaporation of seawater
- **Fuel wood** — hardwoods (oak, hickory, apple, cherry) for smoking; any dry wood for kiln drying. From [forestry](../plants/index.md) or [energy](../energy/index.md)
- **Curing salts** — potassium nitrate (KNO₃, saltpeter) at 0.1-0.2% or sodium nitrite (NaNO₂) at 120-200 ppm for botulism prevention in cured meats. From [mining](../mining/index.md) or [chemistry](../chemistry/index.md)
- **Sugar** — 60%+ concentration for sugaring preserves. From [agriculture](../foundations/food-agriculture.md) (sugar cane, sugar beet) or [chemistry](../chemistry/index.md)
- **Oil** — olive, vegetable, or animal fat for oil packing. From [Oil & Fat Processing](oil-processing.md)

### Equipment

- [Ceramic vessels](../ceramics/index.md) — storage jars, crocks, pots for salting and fermentation
- Drying racks — wood/bamboo frames, 2-4 m² surface area per 10 kg fresh food
- Smokehouse — enclosed chamber with firebox, smoke channel, and ventilation control
- Sealed containers — glass jars, ceramic crocks with lids, for dried and oiled goods
- Knife, cutting board — for preparing uniform pieces

### Knowledge

- Water activity (aw) concept — drying must reduce aw below 0.60 for full microbial stability; salting reduces aw to 0.65-0.75
- Curing chemistry — nitrates prevent botulism by inhibiting *C. botulinum* growth in anaerobic conditions; nitrites fix myoglobin for red color
- [Basic sanitation](../health/sanitation.md) — clean equipment, clean hands, clean storage vessels prevent post-preservation contamination

### Infrastructure

- Dry, well-ventilated space for drying (relative humidity below 60%)
- Fuel supply for smoking and kiln drying
- Cool, dark storage area for finished preserved goods (10-20°C ideal)

## Bill of Materials

### Drying Materials

| Material | Quantity per 100 kg fresh food | Source | Alternatives |
|----------|:------------------------------:|--------|--------------|
| Fresh produce or meat | 100 kg | [Agriculture](../foundations/food-agriculture.md) | Wild foraged foods |
| Drying racks (wood/bamboo) | 2-4 m² surface area per 10 kg | [Forestry](../plants/index.md) | Clean flat stones, concrete surface |
| Fuel (for kiln drying) | 5-15 kg wood per 10 kg food | [Energy](../energy/index.md) | Solar drying (climate dependent) |
| Storage containers (sealed) | As needed | [Ceramics](../ceramics/index.md) | Glass jars, metal tins |

### Salting and Curing Materials

| Material | Quantity per 100 kg meat/fish | Source | Alternatives |
|----------|:----------------------------:|--------|--------------|
| Salt (NaCl) | 20-30 kg (heavy cure) or 10-15 kg (light) | [Mining](../mining/salt.md) | Sea salt (solar evaporated) |
| Potassium nitrate (KNO₃) | 100-200 g (0.1-0.2%) | [Mining](../mining/index.md) or [Chemistry](../chemistry/index.md) | Sodium nitrite (120-200 ppm, more effective) |
| Barrels or crocks | 5-10 per 100 kg | [Ceramics](../ceramics/index.md) or [Forestry](../plants/index.md) | Food-grade containers |
| Sugar (for sweet cure) | 5-10 kg | [Agriculture](../foundations/food-agriculture.md) | Honey (equivalent osmotic effect) |

## Process Description

### Drying

The oldest and simplest preservation method. Reduces water activity (aw) below 0.60, inhibiting virtually all microbial growth.

1. **Prepare food**: Wash, peel (if applicable), and slice to uniform thin pieces (<5 mm for rapid drying). Non-uniform pieces dry at different rates — the wettest piece can spoil the batch.
2. **Blanch vegetables** (optional): Immerse in boiling water for 1-5 minutes to deactivate enzymes that cause off-flavors and color loss during storage.
3. **Arrange on drying surface**: Spread in single layer on clean racks, screens, or flat stones. Do not overlap pieces — overlapping traps moisture and creates mold spots.
4. **Sun drying**: Place racks in direct sun with good airflow. Cover with fine mesh to exclude insects. Turn every few hours. Duration: 2-5 days depending on temperature and humidity. Works best below 60% relative humidity.
5. **Air drying**: Hang whole items (herbs, sausages, whole fish) in warm (20-35°C), dry (RH <50%), well-ventilated area. Duration: 1-4 weeks.
6. **Kiln drying** (faster, fuel-dependent): Build a small fire or stove beneath the drying rack. Maintain 50-70°C air temperature with good airflow. Duration: 6-24 hours. Do not exceed 70°C — case hardening seals moisture inside.
7. **Test for dryness**: Vegetables/fruits should reach 10-20% moisture (leathery, no moisture when squeezed). Meat jerky: 5-10% moisture (brittle, snaps when bent). Target aw <0.60.
8. **Package**: Pack immediately into sealed containers with desiccant. Keep in dry, dark, cool storage. Dried food keeps 6-12 months at room temperature.
9. **Reconstitution** (before cooking): Soak in water for 2-12 hours. Expect 10-30% vitamin C loss from the drying process.

### Salting and Curing

Salt (NaCl) creates osmotic pressure that kills or inhibits bacteria and molds by drawing water out of microbial cells. Two main methods: dry salting and brining.

1. **Prepare food**: Wash meat or fish. Cut into uniform pieces (1-5 kg each for dry salting; smaller pieces for faster brine penetration). Trim visible fat if long storage is intended (fat oxidizes faster than lean).
2. **Dry salting**: Rub salt thoroughly into all surfaces of the food. Use 20-30% salt by weight for heavy cure (6-18 month storage) or 10-15% for light cure (flavor + moderate preservation). Pack pieces in a barrel or crock, layering with salt between each layer. Place a weight on top to keep food submerged in the brine that forms as salt draws out moisture.
3. **Brining**: Prepare saturated salt solution — dissolve NaCl in water until no more dissolves (26.4% NaCl at 20°C is the saturation point). Submerge food completely in the brine. Brining penetrates faster than dry salting. Duration: 1-7 days depending on thickness.
4. **Add curing salts**: Dissolve potassium nitrate (0.1-0.2% by weight) or sodium nitrite (120-200 ppm) into the brine or rub. This prevents botulism in low-temperature curing and maintains red meat color.
5. **Cure duration**: Whole fish: 2-8 weeks. Meat cuts: 1-4 weeks. Check periodically — the brine should remain clear; cloudy brine indicates spoilage.
6. **Remove and dry**: After curing, remove food from brine. Rinse off excess salt. Air-dry or smoke for additional preservation and surface dryness.
7. **Storage**: Store salted food in a cool (10-15°C), dark place. Shelf life: 6-18 months for heavy cure. Heavily salted cod (bacalao) stores for years.

### Smoking

Smoke contains antimicrobial compounds (phenols, formaldehyde, acetic acid) and deposits a preservative layer. Smoking is always combined with partial drying — it does not work alone.

1. **Pre-salt or brine**: Smoking alone is insufficient for preservation. Always salt or brine the food first (see above) to reduce water activity.
2. **Cold smoking** (20-30°C, 12-48 hours): Hang salted food in smokehouse. Burn hardwood (oak, hickory, apple, cherry — never softwood/pine, which produces bitter resinous smoke). Maintain temperature below 30°C to avoid creating anaerobic botulism conditions. Duration: 12-48 hours. Produces preserved-but-raw food (requires cooking before eating).
3. **Hot smoking** (60-80°C, 4-12 hours): Increase fire intensity to raise smokehouse temperature to 60-80°C. This both smokes and cooks the food. Internal temperature must reach 63°C for meat safety. Safer than cold smoking — cooking temperature kills most pathogens. Duration: 4-12 hours.
4. **Control smoke density**: Smoke should be thin and blue-white, not thick and white. Dense smoke deposits bitter creosote. Adjust airflow to keep smoke moving — stagnant smoke produces acrid flavors.
5. **Cool and store**: After smoking, cool food to room temperature. The surface should be dry and glossy. Shelf life: 1-4 weeks without refrigeration for cold-smoked; 2-6 months refrigerated for hot-smoked. Final water activity: 0.75-0.85.

### Sugaring

Sugar at concentrations above 60% creates osmotic pressure that inhibits microbial growth — same mechanism as salting but sweeter.

1. Prepare fruit by washing, peeling, and cutting.
2. Cook fruit with sugar to ≥60% sugar concentration (by weight). This produces jams, jellies, and preserves.
3. Pour hot into sterilized jars. Seal immediately.
4. Shelf life: 6-12 months at room temperature in sealed jars.

### Oil Packing

Oil excludes oxygen, preventing oxidative rancidity and aerobic microbial growth. Used for cheese in oil, dried tomatoes in oil, cured meats.

1. Fully dry or cure the food first — oil packing does not dehydrate.
2. Pack food into a clean glass or ceramic container.
3. Cover completely with food-grade oil (olive, vegetable). No part of the food may protrude above the oil surface.
4. Seal container. Shelf life: 3-6 months at cool room temperature.

## Quantitative Parameters

### Preservation Method Comparison

| Method | Water Activity (aw) | Temperature | Processing Time | Shelf Life | Energy Required |
|--------|:-------------------:|:-----------:|:---------------:|:----------:|:---------------:|
| Sun drying | <0.60 | Ambient (25-40°C) | 2-5 days | 6-12 months | None (solar) |
| Kiln drying | <0.60 | 50-70°C | 6-24 hours | 6-12 months | 2-5 MJ/kg |
| Salting (heavy) | 0.65-0.75 | Ambient | 2-8 weeks | 6-18 months | Minimal |
| Smoking (cold) | 0.75-0.85 | 20-30°C | 12-48 hours | 1-4 weeks | 1-3 MJ/kg (wood) |
| Smoking (hot) | 0.70-0.80 | 60-80°C | 4-12 hours | 2-6 months (refrigerated) | 2-5 MJ/kg |
| Sugaring | <0.70 | 100°C (cook) | 1-2 hours | 6-12 months | 1-2 MJ/kg |
| Oil packing | — | Ambient | 1 hour | 3-6 months | None |

### Drying Parameters by Method

| Parameter | Sun Drying | Air Drying | Kiln Drying |
|-----------|:----------:|:---------:|:-----------:|
| Temperature | 25-40°C (ambient) | 20-35°C | 50-70°C |
| Relative humidity | <60% required | <50% required | Any (controlled) |
| Duration | 2-5 days | 1-4 weeks | 6-24 hours |
| Final moisture | 10-20% (fruit), 5-10% (meat) | 10-20% | 5-15% |
| Weight reduction | 70-90% | 70-90% | 70-90% |
| Climate dependency | High (needs dry sunny weather) | High (needs dry climate) | None (controlled) |
| Fuel required | None | None | 5-15 kg wood / 10 kg food |

### Curing Salt Concentrations

| Additive | Concentration | Purpose | Regulatory Limit |
|----------|:------------:|---------|:----------------:|
| NaCl (salt) | 10-30% by weight | Osmotic dehydration, flavor | No limit |
| KNO₃ (saltpeter) | 0.1-0.2% by weight | Botulism prevention, color fix | 500 ppm max (as nitrite) |
| NaNO₂ (sodium nitrite) | 120-200 ppm | Botulism prevention, color fix | 200 ppm max (ingoing) |
| Sugar | 5-10% by weight | Flavor, browning, osmotic effect | No limit |

## Scaling Notes

- **Household preservation** (family of 4-8): Sun drying on racks, small-batch salting in crocks. Throughput: 5-20 kg per batch. Labor: 4-8 hours per batch. Equipment: minimal (pots, jars, racks).
- **Community preservation** (50-200 people): Dedicated drying shed, barrel salting operation, small smokehouse. Throughput: 100-500 kg per batch. 2-3 workers per session. Requires dedicated building with ventilation and water supply.
- **Industrial preservation** (10,000+ people): Continuous drying tunnels, automated salting lines, large smokehouses. Throughput: 1-50 tonnes/day. 20-100 workers. Requires steam supply, electrical power, and transportation infrastructure.
- **Salt consumption scaling**: Preserving 1 tonne of meat by heavy salting requires 200-300 kg salt. A community of 500 people preserving meat for winter needs 5-10 tonnes of salt per year — a significant logistics burden. Salt production must be planned alongside food preservation infrastructure (see [Mining: Salt](../mining/salt.md)).
- **Weight reduction**: All drying methods reduce food weight by 70-90% (water removal). This dramatically reduces transport and storage costs — 100 kg of fresh vegetables becomes 10-30 kg of dried product with equivalent nutritional value (minus vitamin losses).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Mold on dried food | Insufficient drying (aw >0.70), storage humidity too high, poor packaging | Dry to <10% moisture. Store in sealed containers with desiccant. Keep below 60% RH |
| Dried food won't rehydrate | Over-dried (<3% moisture), case hardening from too-hot drying | Dry to 10-20% moisture, not lower. Use lower temperature (50-60°C) for initial drying, increase gradually |
| Rancid salted meat | Fat oxidation, temperature too high during storage, insufficient salt | Store below 15°C. Increase salt concentration. Trim visible fat before salting (fat oxidizes faster than lean) |
| Cloudy brine during curing | Bacterial growth in brine (spoilage) | Discard batch. Check salt concentration is ≥20%. Maintain temperature below 10°C during cure. Ensure food is fully submerged |
| Smoked food spoils quickly | Insufficient salting before smoking, temperature too low during hot smoking | Salt or brine before smoking. Hot smoke at 60-80°C. Ensure internal temperature reaches 63°C |
| Bitter smoked flavor | Dense white smoke, softwood (pine) fuel, creosote buildup | Use thin blue-white smoke only. Use hardwoods (oak, hickory, apple). Increase airflow to prevent creosote condensation |
| Nitrite burn (green color in cured meat) | Excess sodium nitrite (>200 ppm) | Reduce nitrite to 120-150 ppm. Trim affected areas — green-gray color is harmless but unappetizing |

## Safety

Botulism is the primary hazard in smoking and curing. *Clostridium botulinum* spores germinate in anaerobic, low-acid (pH >4.6), moist conditions at 20-30°C — exactly the conditions inside a cold smokehouse or a barrel of improperly salted meat. The toxin is lethal at approximately 1 ng/kg body weight (ingested).

- **Cold smoking at 20-30°C is dangerous** without prior curing. The 20-30°C temperature range in anaerobic conditions (inside a thick meat piece) is the ideal growth zone for *C. botulinum*. Always salt or brine food to reduce water activity below 0.92 before cold smoking. Add nitrites (120-200 ppm) for additional botulism protection.
- **Curing salt safety**: Potassium nitrate and sodium nitrite are toxic in concentrated form. Wear gloves when handling pure curing salts. At food-grade concentrations (120-200 ppm) they are safe, but at gram quantities they are acutely toxic. Label and store curing salts separately from table salt.
- **Nitrosamines**: Nitrate-cured meats form nitrosamines (carcinogenic) when cooked at high temperatures (frying bacon at >200°C). Fry cured meats at moderate temperature only.
- **Salt and health**: Heavy salt consumption (>5 g NaCl per day) increases blood pressure and cardiovascular risk in the workforce. A diet based heavily on salt-preserved foods should be balanced with fresh foods when available.
- **Smoke inhalation**: Wood smoke contains polycyclic aromatic hydrocarbons (PAHs), some carcinogenic. Smokehouses require ventilation. Do not stand in smoke for extended periods. Chronic exposure increases lung cancer risk.
- **Phosphine fumigation** (for stored dried grain): Aluminum phosphide tablets release phosphine gas (PH₃) — lethal at 0.01% in air. Apply only to sealed storage. Aerate for 48+ hours before re-entry. Phosphine is heavier than air — evacuate from bottom up.

### Personal Protective Equipment

- Gloves when handling curing salts (KNO₃ and NaNO₂ are toxic in concentrated form)
- Respirator or work upwind when operating smokehouse (PAH exposure)
- Sharp knives and cutting boards (dull knives cause more accidents than sharp ones)

## Quality Control

### Acceptance Criteria

- **Dried foods**: Final moisture content 10-20% for vegetables/fruits, 5-10% for meat jerky. Water activity aw <0.60. No visible mold. Characteristic color (not scorched brown or case-hardened).
- **Salted/cured foods**: Salt content 10-30% by weight. pH below 5.5 (cured meat). Brine remains clear during curing — cloudy brine indicates spoilage. Red color in nitrite-cured meat confirms proper cure.
- **Smoked foods**: Surface dry and glossy. Water activity 0.75-0.85. Characteristic smoke aroma, not bitter or creosote-heavy. Internal temperature reached 63°C for hot-smoked meat.

### Testing Methods

- **Moisture content (dried foods)**: Weigh sample, dry at 105°C for 24 hours, weigh again. Weight loss = moisture content. Low-tech alternative: bend test — properly dried jerky snaps rather than bends.
- **Water activity**: Electronic hygrometer (aw meter), accuracy ±0.02. Field alternative: no mold growth within 2 weeks at room temperature in sealed container indicates aw <0.70.
- **Salt content (cured foods)**: Titration method (Mohr) with silver nitrate. Low-tech: taste test — properly salted meat tastes distinctly salty but not inedible.
- **Visual inspection**: Mold growth (white, green, black spots), color change, gas bubbles, slimy texture all indicate spoilage. Discard entire batch if widespread.
- **Smell test**: Off-odors (sulfurous, putrid, ammonia) indicate spoilage. Do not taste-test suspect food.

### Sampling Procedure

- Inspect dried goods weekly during first month of storage for mold or insect activity.
- Check brine clarity every 2-3 days during curing period.
- Monitor smokehouse temperature every 1-2 hours during operation.

## Variations and Alternatives

### Regional Adaptations

- **Humid tropical climates** (RH >60%): Sun drying fails — food molds before it dries. Use fermentation, salting, or smoking. Cassava fermentation (to remove cyanogenic glycosides) is a tropical staple. Fish sauce (fermented fish in brine) is the Southeast Asian solution to preserving fish in humid climates.
- **Arid climates**: Sun drying is optimal. Grapes → raisins, plums → prunes, apricots, tomatoes, dates all sun-dry efficiently. Middle Eastern and Mediterranean cuisines are built around sun-dried ingredients.
- **Cold temperate climates**: Natural freezing in winter supplements drying and salting. Sauerkraut (fermented cabbage) and salted fish are Northern European traditional preservation staples.

### Historical Methods

- **Pemmican** (Native American): Dried meat pounded into powder, mixed with rendered fat at 50:50 ratio. Shelf-stable for 1-2 years. Highest calorie density of any traditional preserved food. Combines drying (aw reduction) and fat encapsulation (oxygen barrier).
- **Bacalao** (salt cod, European): Heavy-salted dried cod. Shelf life 2+ years. Was the protein that enabled trans-Atlantic exploration — ships carried bacalao as non-perishable protein.
- **Garum** (Roman): Fermented fish sauce. Brine-fermented fish parts, 2-3 months. Liquid umami concentrate that keeps indefinitely.

### Method Selection Trade-offs

| Criterion | Drying | Salting | Smoking | Sugaring |
|-----------|:------:|:-------:|:-------:|:--------:|
| Shelf life | 6-12 months | 6-18 months | 1-6 months | 6-12 months |
| Energy input | None (sun) | None | Fuel required | Fuel (cooking) |
| Equipment cost | Lowest | Low | Medium | Low |
| Nutritional loss | 10-30% vit C | Minimal | Minimal | Minimal |
| Taste change | Large (concentrated) | Large (salty) | Large (smoky) | Large (sweet) |
| Best for | Fruit, vegetables, lean meat | Meat, fish | Meat, fish | Fruit |
| Climate dependent | Yes (needs dry air) | No | No | No |

## References

- [Food Preservation](preservation.md) — overview hub for all preservation methods
- [Canning & Thermal Sterilization](canning.md) — pressure canning and water bath canning for shelf-stable preserves
- [Food Fermentation](fermentation.md) — biological preservation via lactic acid bacteria and yeasts
- [Pasteurization](pasteurization.md) — heat treatment for liquid foods
- [Refrigeration](refrigeration.md) — mechanical cooling and cold chain
- [Ceramics](../ceramics/index.md) — storage vessels, jars, pots for salting and storage
- [Mining: Salt](../mining/salt.md) — salt production for curing
- [Energy](../energy/index.md) — fuel for kiln drying and smoking
- [Health & Sanitation](../health/sanitation.md) — hygiene to prevent post-preservation contamination
- [Oil & Fat Processing](oil-processing.md) — oil production for oil-packing preservation

---

*Part of the [Bootciv Tech Tree](../index.md) • [Food Processing](./index.md) • [All Domains](../index.md)*
