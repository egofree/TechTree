# Oil & Fat Processing

> **Node ID**: food-processing.oil-processing
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: [`foundations.food-agriculture`](../foundations/food-agriculture.md), [`ceramics`](../ceramics/index.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`chemistry.soap`](../chemistry/soap.md), [`food-processing.preservation`](preservation.md)
> **Timeline**: Years 0-20
> **Outputs**: vegetable_oil, tallow, lard, olive_oil, linseed_oil, soap_stock, oilseed_meal, rendered_fat
> **Critical**: No — oil processing enhances food quality and enables soap, but basic nutrition and hygiene have alternatives


Oil and fat processing extracts edible and industrial lipids from plant seeds, fruit pulp, and animal tissues. Cooking oils triple the caloric density of meals and enable high-temperature cooking methods (frying, sautéing) that inactivate foodborne pathogens. Rendered animal fats (tallow, lard) serve triple duty as cooking fat, soap-making feedstock (see [Chemistry: Soap](../chemistry/soap.md)), and candle fuel. Industrial oils (linseed, tung) become paints, varnishes, and wood preservatives.

Without processed fats, cooking relies on boiling and roasting — methods that cannot achieve temperatures above 100°C (boiling) or require constant attention (roasting). Frying oil reaches 170-190°C, creating Maillard browning that makes food palatable and digestible. A workforce fed on fat-supplemented diets has 20-30% higher caloric intake than one eating only boiled grains and vegetables.

The extraction progression moves from simple pressing (stone-age, 40-60% yield) to expeller pressing (iron-age, 70-80% yield) to solvent extraction (industrial, 95%+ yield). Rendering animal fat requires only fire and containers — achievable from Year 0.


## Materials

- **Oilseeds**: Sunflower, rapeseed (canola), sesame, flax (linseed), cottonseed, peanut, or hemp seed. Oil content varies 20-50% by weight. Source: [Agriculture](../foundations/food-agriculture.md).
- **Olives**: 15-30% oil by weight. Source: [Agriculture](../foundations/food-agriculture.md) — requires Mediterranean or similar climate.
- **Animal fat**: Beef suet, pork fatback, sheep tail fat, poultry fat. Source: [Agriculture](../foundations/food-agriculture.md) or hunting.
- **Water**: For olive oil washing and animal fat rendering. Source: [Water Supply](../water/basic-treatment.md).
- **Heat source**: Charcoal, wood fire, or steam for pressing temperature control. Source: [Energy](../energy/engine.md).

## Tools and Equipment

- **Seed press**: Stone mortar and pestle (simplest), wedge press (wooden), screw press (iron), or expeller (steel). See Equipment section for construction details.
- **Rendering vessels**: Iron or ceramic pots, 10-100 L capacity. Source: [Ceramics](../ceramics/index.md), [Metals](../metals/index.md).
- **Filtering cloth**: Linen, cotton, or fine mesh. Removes solid particles from pressed oil.
- **Settling tanks**: Ceramic or wooden containers for gravity separation of oil from water and sediment.
- **Screw press or hydraulic press**: For seed pressing. Iron construction required for pressures above 50 bar. Source: [Machine Tools](../machine-tools/index.md).

## Knowledge

- Identification of oil-bearing seeds and their oil content
- Understanding of temperature thresholds for oil quality (smoke point, rancidity)
- Basic grasp of pressing mechanics and pressure application

## Bill of Materials

| Material | Quantity per L oil | Source | Alternatives |
|----------|:------------------:|--------|-------------|
| Sunflower seed | 2.5-4.0 kg | [Agriculture](../foundations/food-agriculture.md) | Rapeseed (2.0-3.0 kg), sesame (2.5-3.5 kg) |
| Olives (fruit) | 4.0-7.0 kg | [Agriculture](../foundations/food-agriculture.md) | No practical alternative for olive oil |
| Flaxseed (linseed) | 2.5-4.0 kg | [Agriculture](../foundations/food-agriculture.md) | Hemp seed (3.0-4.5 kg) |
| Beef suet (raw) | 1.1-1.3 kg | [Agriculture](../foundations/food-agriculture.md) | Pork fatback (1.1-1.2 kg), sheep fat |
| Water (for rendering) | 0.5-1.0 L per kg fat | [Water](../water/index.md) | Not substitutable |
| Firewood or charcoal | 0.5-1.0 kg per kg fat rendered | [Energy](../energy/charcoal.md) | Any heat source |

## Oilseed Yields and Properties

| Seed | Oil Content | Press Yield | Smoke Point | Primary Use |
|------|:-----------:|:-----------:|:-----------:|:-----------:|
| Olive (pressed fruit) | 15-30% | 80-90% of available | 190-210°C (virgin) | Cooking, salads |
| Sunflower | 40-50% | 60-75% | 227°C (refined) | Frying, cooking |
| Rapeseed (canola) | 38-45% | 65-80% | 204°C (refined) | General cooking |
| Sesame | 45-55% | 50-65% | 210°C (unrefined) | Cooking, flavor |
| Peanut | 45-55% | 65-80% | 227°C (refined) | Frying, cooking |
| Flax (linseed) | 35-45% | 55-70% | 107°C (unrefined) | Industrial, paint |
| Coconut (copra) | 60-70% | 60-75% | 177°C (refined) | Cooking, soap |
| Palm fruit | 20-25% (fruit), 45-55% (kernel) | 70-85% | 232°C (refined) | Cooking, soap, industrial |


## Olive Oil Production (Cold Press)

Olive oil is unique among vegetable oils because it is extracted from the fruit pulp rather than the seed. Cold pressing below 27°C preserves flavor compounds and antioxidants:

1. **Harvesting**: Pick olives at the correct ripeness — green-to-purple yields the best oil. Overripe olives produce higher yield but lower quality oil with higher acidity. Process within 24 hours of harvest — olives begin oxidizing immediately after picking.
2. **Washing**: Remove leaves, twigs, and dirt with water spray. Leaves impart bitter flavors if left in.
3. **Crushing**: Grind olives (flesh, skin, and pit) into a paste using stone mill (traditional) or hammer mill (industrial). Pit fragments aid oil release by creating channels in the paste. Paste temperature must stay below 27°C for "cold pressed" designation.
4. **Malaxation (mixing)**: Slowly stir paste for 20-45 minutes at 25-27°C. Oil droplets coalesce into larger drops that separate more easily. This is the critical step — too short = low yield, too long = oxidation and flavor loss.
5. **Pressing or centrifugation**:
   - **Press method**: Spread paste on fiber disks (esparto grass or synthetic), stack in press, apply 200-400 bar pressure. Oil and vegetation water flow out; solid pomace remains on disks. Yield: 70-85% of oil in paste.
   - **Centrifugation (industrial)**: Horizontal decanter centrifuge at 3,000-4,000 RPM separates paste into oil, water, and pomace. Then vertical disc centrifuge separates oil from water.
6. **Settling**: Allow oil to settle 1-3 weeks in stainless steel or glass containers. Sediment falls to bottom. Rack (decant) clear oil off sediment.
7. **Storage**: Dark glass bottles or stainless steel containers, 14-18°C, away from light and heat. Olive oil oxidizes when exposed to light — rancidity develops in weeks in clear bottles.

**Strengths**:
- Cold pressing below 27°C preserves polyphenols, tocopherols, and flavor compounds — extra virgin olive oil has the highest antioxidant content of any cooking oil
- Olive trees produce fruit for 100+ years with minimal maintenance — a permanent oil-producing asset once established
- Pit fragments in the paste create channels that aid oil release without any chemical processing

**Weaknesses**:
- Olives must be processed within 24 hours of harvest — oxidation begins immediately after picking, requiring proximity of press to grove
- Cold pressing extracts only 70-85% of available oil — the remaining pomace requires solvent extraction or is wasted
- Olive trees take 5-8 years to reach productive maturity and require Mediterranean climate (hot dry summers, mild winters)

## Seed Oil Pressing (Expeller Method)

1. **Seed preparation**: Clean seeds to remove chaff, stones, and stems. Dry to 8-10% moisture. Moist seeds clog the press; overly dry seeds produce dusty meal and lower yield.
2. **Dehulling** (optional): Remove seed coats for sunflower and cottonseed. Hulls absorb oil and reduce yield by 5-10%. Dehull with roller mill or attrition mill.
3. **Flaking**: Pass seeds through smooth rollers to create flakes 0.2-0.4 mm thick. Flaking ruptures cell walls, making oil accessible.
4. **Conditioning**: Heat flakes to 60-90°C using steam or direct-fired conditioning kettle. Heating reduces oil viscosity (flows more easily) and denatures proteins that bind oil in cells. Temperature control is critical — above 120°C, oil darkens and develops off-flavors.
5. **Pressing**: Feed conditioned flakes into expeller press. A rotating screw shaft forces material through a cage of bars with progressively narrowing gaps. Pressure increases to 50-150 bar. Oil flows out through cage bar gaps; compressed meal (press cake) exits at the discharge end.
6. **Filtration**: Filter pressed oil through cloth or plate filter to remove fine particles. Raw oil is cloudy — filtering produces clear oil.
7. **Refining** (optional, industrial):
   - **Degumming**: Add 1-3% water at 60-70°C. Phospholipids hydrate and precipitate. Centrifuge to remove.
   - **Neutralization**: Add 12-16% NaOH solution to neutralize free fatty acids. Soap stock forms and settles. Centrifuge.
   - **Bleaching**: Add 1-3% activated bleaching earth at 90-110°C under vacuum. Removes pigments and residual soap.
   - **Deodorization**: Steam distillation at 230-260°C under high vacuum (1-5 mmHg) for 30-60 minutes. Removes volatile flavor compounds and free fatty acids. Produces neutral-flavored, high smoke-point oil.

**Strengths**:
- Expeller pressing handles multiple seed types (sunflower, rapeseed, peanut, sesame) with the same equipment — one press serves all oilseeds
- Press cake byproduct contains 30-45% protein and is valuable as animal feed — dual revenue stream from single input
- Conditioning at 60-90°C doubles yield vs. cold pressing while maintaining acceptable oil quality

**Weaknesses**:
- Expeller screw and cage bars require hardened steel to withstand 50-150 bar pressure and abrasive seed particles — demands industrial metallurgy
- Hot pressing above 80°C degrades heat-sensitive nutrients (vitamin E, polyphenols) and requires refining to remove off-flavors
- Refining sequence (degumming, neutralization, bleaching, deodorization) requires 4 separate processing steps with chemical inputs (NaOH, bleaching earth)

## Animal Fat Rendering

Rendering melts fat from animal tissues by heating. Two methods:

**Wet rendering** (simplest, lower quality):

1. **Preparation**: Cut fat into 2-5 cm pieces. Remove as much lean meat as possible — meat imparts flavor and promotes spoilage. Use a sharp knife on a clean cutting board.
2. **Add water**: Place fat pieces in pot. Add water to cover 50-75% of the fat. Water prevents fat from scorching before it melts and provides steam to help release fat from connective tissue.
3. **Heat slowly**: Bring to a gentle simmer (90-95°C). Do not boil vigorously — vigorous boiling emulsifies fat and water, producing a cloudy, lower-quality product. Maintain simmer for 2-4 hours, stirring occasionally.
4. **Strain**: Pour through fine mesh strainer or cloth into a clean container. Solid pieces (cracklings) are pressed to extract remaining fat. Cracklings are edible (high protein) or used as animal feed.
5. **Cool and separate**: Fat rises to the top and solidifies as it cools. Remove solid fat layer from water. Water remaining at the bottom (stickwater) contains dissolved protein — can be reduced to make glue stock.
6. **Clarify** (optional): Reheat strained fat to 110-120°C to evaporate residual water. Clear, water-free fat stores much longer (6-12 months vs. 2-4 weeks for water-containing fat).

**Dry rendering** (higher quality, industrial):

1. **Preparation**: Cut fat into 1-3 cm pieces.
2. **Heat without water**: Place fat in heavy-bottomed pot or rendering tank. Heat slowly to 110-130°C. Fat melts out of the tissue. Higher temperature than wet rendering, but no water means clearer fat.
3. **Duration**: 2-6 hours depending on batch size and temperature. Stir occasionally to prevent sticking.
4. **Strain and cool**: Same as wet rendering step 4-6.

**Strengths (Wet Rendering)**:
- Wet rendering requires only a pot, water, and fire — achievable from Year 0 with ceramic or iron vessels
- Water prevents scorching at 90-95°C simmer, producing cleaner fat than dry rendering
- Cracklings (pressed solids) are high-protein food or animal feed — 60-70% protein by dry weight

**Weaknesses (Wet Rendering)**:
- Wet-rendered fat contains residual water (1-3%) that limits shelf life to 2-4 months unless clarified by reheating to 110-120°C
- Emulsification risk if boiled vigorously — fat and water form a cloudy mixture that does not separate on cooling
- Duration of 2-4 hours of simmering per batch requires constant attention and significant fuel

**Strengths (Dry Rendering)**:
- Dry rendering produces clearer fat with no emulsification risk and longer shelf life (6-12 months)
- Higher rendering temperature (110-130°C) extracts fat more completely — yield 0.70-0.85 kg fat per kg raw beef suet
- No water addition means no separate clarification step needed

**Weaknesses (Dry Rendering)**:
- Requires heavier pot (cast iron preferred) to distribute heat evenly without water as a temperature buffer
- Higher temperature (110-130°C) increases fire risk and burn hazard compared to wet rendering's 90-95°C simmer
- Fat can scorch if not stirred regularly — scorched fat has off-flavors and reduced shelf life


## Pressing Parameters by Oilseed

| Seed | Press Temperature | Pressure (bar) | Yield (%) | Oil Flow Rate |
|------|:-----------------:|:--------------:|:---------:|:-------------:|
| Sunflower | 70-90°C | 80-120 | 60-75 | 8-15 kg/h (small expeller) |
| Rapeseed | 60-80°C | 70-100 | 65-80 | 10-20 kg/h |
| Sesame | 50-70°C | 50-80 | 50-65 | 6-12 kg/h |
| Peanut | 70-90°C | 80-120 | 65-80 | 8-15 kg/h |
| Flax | 50-70°C | 60-90 | 55-70 | 6-12 kg/h |
| Coconut (copra) | 80-100°C | 80-130 | 60-75 | 8-15 kg/h |

## Fat Rendering Parameters

| Fat Type | Rendering Temp | Duration | Yield (kg fat/kg raw) | Smoke Point |
|----------|:--------------:|:--------:|:---------------------:|:-----------:|
| Beef tallow | 110-130°C | 3-6 hours | 0.70-0.85 | 205-210°C |
| Pork lard | 100-120°C | 2-4 hours | 0.75-0.90 | 182-190°C |
| Sheep fat | 110-130°C | 3-5 hours | 0.65-0.80 | 200-210°C |
| Chicken fat (schmaltz) | 90-110°C | 2-3 hours | 0.60-0.75 | 185-195°C |
| Duck fat | 90-110°C | 2-3 hours | 0.65-0.80 | 190°C |

## Oil Stability and Shelf Life

| Oil Type | Free Fatty Acid % | Peroxide Value (meq/kg) | Shelf Life | Storage |
|----------|:-----------------:|:-----------------------:|:----------:|:-------:|
| Extra virgin olive | <0.8 | <20 | 12-18 months | Cool, dark, sealed |
| Refined sunflower | <0.05 | <10 | 18-24 months | Sealed, ambient |
| Refined rapeseed | <0.05 | <10 | 18-24 months | Sealed, ambient |
| Unrefined sesame | 1.0-3.0 | <10 | 6-12 months | Cool, dark |
| Beef tallow | <1.0 | <10 | 6-12 months | Cool, dry |
| Pork lard | <0.5 | <10 | 4-6 months | Cool, refrigerated |

## Scaling Notes

- **Household scale** (1-5 L oil/day): Manual screw press or stone mortar. One person can press 5-10 kg seed/day yielding 2-4 L oil. Rendering 5 kg fat takes 2-3 hours over a fire.
- **Village scale** (10-50 L oil/day): Animal-powered or water-powered edge runner for crushing, wooden wedge press or iron screw press. 2-3 workers produce 20-50 L oil/day from 50-100 kg seed.
- **Industrial scale** (1-10 tonnes oil/day): Steam-heated conditioning, continuous expeller press (50-200 kW motor), solvent extraction plant for residual oil from press cake. Expeller throughput: 1-10 tonnes seed/day per unit. Solvent extraction adds 15-25% yield over pressing alone. Requires hexane (petroleum-derived) — not available in early bootstrap.
- **Press cake utilization**: After pressing, seed meal contains 8-20% residual oil and 30-45% protein. High-protein meals (soybean, peanut, sunflower) are valuable animal feed. Low-protein meals (flax, sesame) are used as fertilizer or boiler fuel.
- **Bottleneck at scale**: Filtering is the rate-limiting step. Press cloth clogs with fine particles. Industrial operations use plate-and-frame filter presses with diatomaceous earth filter aid. At village scale, settling tanks with 24-48 hour gravity clarification are simpler but slower.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low oil yield from seeds | Seeds too dry, too wet, or insufficient pressing pressure | Adjust moisture to 8-10%. Increase press pressure. Ensure proper conditioning temperature |
| Cloudy oil | Fine particles or water in oil | Filter through finer cloth. Settle longer. Heat to 105°C to evaporate water |
| Dark oil color | Excessive pressing temperature or seed hull contamination | Reduce conditioning temperature below 90°C. Dehull seeds before pressing |
| Rancid smell | Oxidation from air, light, or heat exposure | Store in dark, sealed containers at cool temperature. Add antioxidants (vitamin E at 200-500 ppm) |
| Emulsified fat (wet render) | Boiling too vigorously or stirring too aggressively | Simmer gently, do not boil. Stir minimally. Reheat to 120°C to break emulsion |
| Fat with meaty flavor | Insufficient trimming of lean tissue | Trim fat more carefully before rendering. Increase rendering temperature to 130°C to cook off volatile flavors |
| Press cake too oily (>20% residual) | Insufficient pressure or seeds not properly conditioned | Increase press pressure. Ensure conditioning at 70-90°C before pressing |
| Oil foaming during use | Water contamination in oil | Heat oil to 110°C before use to evaporate residual water. Foam subsides when water is gone |

## Safety

- **Fire hazard**: All oils are flammable. Oil fires burn at 300-400°C and cannot be extinguished with water (water causes flaming spatter). Keep a lid or fire blanket nearby — smothering is the correct suppression method. Oil flash points: olive oil 210°C, sunflower 227°C. Never leave heating oil unattended.
- **Press cake self-heating**: Pressed seed meal retains moisture and oil. Stacked in bulk, microbial respiration generates heat. Temperatures above 70°C can lead to spontaneous combustion. Store press cake in thin layers (<1 m depth) with ventilation. Process within 1-2 weeks of pressing.
- **Hexane hazard (industrial)**: Solvent extraction uses hexane (flash point -22°C, TLV 50 ppm). Hexane vapor is heavier than air, accumulates in low points, and forms explosive mixtures at 1.1-7.5% in air. Not relevant for bootstrap-stage pressing operations.
- **Handling hot fat**: Rendering involves 100-130°C fat. Splashes cause severe burns. Wear heavy leather gloves and long sleeves. Use ladles with long handles. Never add water to hot fat — violent steam explosion results.
- **Peroxide value**: Oxidized oil contains peroxides that are toxic and carcinogenic. Discard oil that smells rancid (cardboard, paint, or metallic odor). Peroxide value above 20 meq/kg indicates rancidity — do not consume.

## Quality Control

- **Free fatty acid (FFA) test**: Dissolve oil sample in neutralized alcohol, titrate with 0.1 N NaOH using phenolphthalein indicator. FFA as oleic acid % = (mL NaOH × 0.0282 / g sample) × 100. Extra virgin olive oil: FFA <0.8%. Refined oils: FFA <0.05%. High FFA indicates poor fruit quality or improper processing.
- **Peroxide value**: Measures primary oxidation. Mix oil sample with acetic acid-chloroform, add potassium iodide, titrate liberated iodine with sodium thiosulfate. PV >20 meq/kg indicates rancidity onset.
- **Moisture content**: Oil must contain <0.1% water for long-term storage. Higher moisture promotes hydrolysis (FFA increase) and microbial growth. Test by heating 10 g sample to 105°C for 30 minutes — weight loss = moisture.
- **Color**: Lighter color indicates better refinement. Compare against standard color slides or measure with Lovibond tintometer. Unrefined oils are naturally darker.
- **Smoke point test**: Heat oil in a dark-bottomed vessel. The temperature at which continuous blue smoke appears is the smoke point. Refined oils should match specification (see Parameters table). Low smoke point indicates residual water, free fatty acids, or impurities.

## Variations and Alternatives

| Method | Yield | Complexity | Equipment | Best For |
|--------|:-----:|:----------:|:---------:|:--------:|
| Stone mortar + hand pressing | 30-50% | Low | Stone mortar, cloth | Olives, soft seeds |
| Wooden wedge press | 40-60% | Medium | Timber frame, wedges | All seeds, olives |
| Iron screw press | 60-80% | Medium | Cast/forge iron | All seeds |
| Hydraulic press | 70-85% | High | Hydraulic cylinder | Seeds, olive paste |
| Expeller (continuous) | 65-80% | High | Steel screw + cage | Industrial seed pressing |
| Solvent extraction | 95-98% | Very high | Hexane plant + refinery | Industrial (post-petroleum) |

**Cold press vs. hot press**: Cold pressing (below 50°C for seeds, 27°C for olives) produces premium oil with full flavor and antioxidant content but lower yield (40-60%). Hot pressing (70-100°C) doubles yield but degrades heat-sensitive compounds and requires refining to remove off-flavors. For bootstrap, cold press is simpler and requires no refining equipment.

**Animal fat vs. vegetable oil**: Animal fats are simpler to produce (rendering requires only heat and a pot) and were historically more available than vegetable oils in temperate climates. Vegetable oils require specialized pressing equipment. However, vegetable oils have higher smoke points (better for frying) and contain essential fatty acids (linoleic acid) absent in animal fats.

**Nut oils**: Walnuts, hazelnuts, and almonds produce flavorful oils but pressing requires low temperature to prevent bitterness. Nut oils are premium products with limited yield — 1 kg nuts yields 300-600 mL oil.

## See Also

- [Brewing & Distilling](brewing.md) — uses grain oils and fats as byproducts
- [Dairy Processing](dairy.md) — butter and ghee as alternative cooking fats
- [Food Preservation](preservation.md) — oil as a preservation medium (confit, oil-packed foods)
- [Ceramics](../ceramics/index.md) — storage vessels and pressing equipment
- [Metals](../metals/index.md) — iron and steel for press construction
- [Chemistry: Soap](../chemistry/soap.md) — tallow and vegetable oil as soap feedstock
- [Machine Tools](../machine-tools/index.md) — precision machining for expeller screws



[← Back to Food Processing](index.md)
