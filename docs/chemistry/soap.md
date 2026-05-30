# Soap & Detergents

> **Node ID**: chemistry.soap
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.alkalis`](alkalis.md), [`chemistry.petroleum-alternatives`](petroleum-alternatives.md), [`metals.non-ferrous`](../metals/non-ferrous.md)
> **Enables**: [`health.occupational-health`](../health/occupational-health.md)
> **Timeline**: Years 5-30
> **Outputs**: soap, glycerol, detergent
> **Critical**: No — soap and detergents improve sanitation but are not prerequisites for core industrial capabilities


Saponification — the reaction of fats or oils with alkali — is arguably the oldest chemical reaction performed at industrial scale. Soap has been manufactured for at least 4,500 years (Babylonian clay tablets circa 2800 BCE describe fat + ash mixtures). The chemistry is deceptively simple: triglyceride + alkali → soap salt + glycerol. Yet this reaction underpins hygiene, public health, textile manufacturing, metalworking, and — via glycerol recovery — explosives production.

Beyond hygiene, soap and its derivatives are critical for textile processing (wool scouring, cotton preparation), metal degreasing (before plating, painting, heat treatment), emulsion polymerization (PVC, synthetic rubber), and as feedstock for glycerol recovery (which feeds explosives production via nitroglycerin). Synthetic detergents extend soap's functionality into hard water and acidic conditions where conventional soap precipitates as insoluble calcium salts.

## Prerequisites

- [Alkalis](alkalis.md) — NaOH and KOH production for saponification
- [Petroleum alternatives](petroleum-alternatives.md) — feedstocks for synthetic detergents
- [Non-ferrous metals](../metals/non-ferrous.md) — copper and zinc equipment for processing
- [Animals / fats](../animals/index.md) — tallow and lard as soap feedstocks
- [Plants / oils](../plants/index.md) — vegetable oils as soap feedstocks

## Saponification Chemistry

**Core reaction**: Triglyceride (fat/oil) + 3 NaOH → 3 soap molecules + glycerol (glycerin)

- **Triglyceride structure**: Three fatty acid chains ester-bonded to a glycerol backbone. Hydrolysis of each ester bond releases one fatty acid as a sodium (or potassium) salt — the soap molecule.
- **[Fatty acid profiles](../glossary/fatty-acid-profiles.md)** determine soap properties:
  - **Lauric acid (C12)**: Coconut oil, palm kernel oil. Quick lather, hard bar, dissolves easily. 45-50% in coconut oil.
  - **Myristic acid (C14)**: Coconut, nutmeg. Adds lather stability.
  - **Palmitic acid (C16)**: Palm oil, tallow. Hardens bar, contributes stable lather. 25-30% in tallow.
  - **Stearic acid (C18)**: Tallow, shea butter. Very hard, long-lasting bar. 15-25% in tallow.
  - **Oleic acid (C18:1)**: Olive oil, tallow. Conditioning, contributes to low-temperature lather. 40-45% in tallow.
  - **Linoleic acid (C18:2)**: Soybean, sunflower. Conditioning but reduces bar hardness and accelerates rancidity. Keep below 15% in bar formulations.
- **[NaOH → hard soap](../glossary/naoh-hard-soap.md)** (bar soap, sodium salts of fatty acids). Melting point 50-70°C.
- **[KOH → soft soap](../glossary/koh-soft-soap.md)** (potassium salts, liquid or paste). Lower melting point, more soluble. Used for liquid soaps, shaving cream, and textile scouring.
- **Superfatting**: Using 3-8% less alkali than stoichiometric leaves unreacted fat in the finished soap. Improves skin feel and reduces irritation. Measured as "lye discount" — a 5% superfat formula uses 95% of the calculated NaOH.
- **Saponification value (SV)**: Milligrams of KOH required to saponify 1 gram of fat. Coconut oil: SV 250-260. Olive oil: SV 185-196. Tallow: SV 190-200. Palm oil: SV 195-205. These values determine exact lye quantities for complete reaction.

## Traditional Soap Making

All traditional methods share the same chemistry: fat + alkali → soap + glycerol. The differences are in temperature, curing time, and whether glycerol is retained or recovered.

**Fat rendering and oil extraction**:
- **Tallow**: Render beef suet (kidney fat) by cutting into small pieces, heating slowly in water at 70-80°C for 4-6 hours. Strain through cloth. Yield: 70-80% of raw suet weight. Tallow produces hard, long-lasting soap with stable lather. For large-scale rendering, use steam-jacketed tanks (500-5000 L) with mechanical agitation. Skim rendered fat from water surface, filter through coarse screen then fine cloth.
- **Lard**: Render pig fat similarly. Softer than tallow soap, better skin feel. Often blended 50:50 with tallow for balanced bar properties.
- **Plant oils**: Press oilseeds (coconut, palm, olive, sunflower) using screw press or hydraulic press. Coconut oil (high lauric acid) produces the hardest bar with the most lather. Olive oil produces "Castile soap" — mild, conditioning, slower to lather. Palm oil offers balanced profile similar to tallow and is the primary plant-based alternative to animal fats in commercial soap.
- **Recovered fats**: Restaurant fryer oil, waste cooking grease, and animal processing waste are all viable soap feedstocks after filtering and water removal. Waste grease requires pre-treatment: heat to 80-90°C to melt, filter through 50-100 µm screen, settle to remove water and food particles. Free fatty acid (FFA) content determines lye quantity — high-FFA waste oils require more lye (each gram of FFA consumes NaOH: RCOOH + NaOH → RCOONa + H₂O).
- **Blend for balanced bar**: 40% tallow (hardness, lather stability) + 30% coconut oil (quick lather, cleaning power) + 30% olive oil (conditioning, mildness). This approximates the classic "three-oil" formulation.

**[Cold process](../glossary/cold-process.md)** (simplest, longest cure):
- Heat fats and oils to 38-43°C (100-110°F). Separately dissolve NaOH in cold water (exothermic — solution reaches 80-90°C; cool to 38-43°C). Pour lye solution into fats with constant stirring (stick blender accelerates emulsification). Stir to "trace" — mixture thickens so that drips leave visible marks on the surface (indicates emulsion stability). Add fragrance or colorants at trace. Pour into insulated molds. Gel phase: 24-48 hours (internal temperature reaches 60-70°C as saponification completes). Unmold after 48-72 hours. Cure 4-6 weeks (water evaporates, bar hardens, residual saponification completes, pH drops from ~11 to ~9.5).

**Strengths**: Simplest soap-making method — no external heating after initial melt; retains all glycerol in the bar (moisturizing); easily customized with fragrances, colors, and additives; low equipment cost (<$500 for small-scale); produces hard, long-lasting bar soap.

**Weaknesses**: 4-6 week cure time before bar is ready to use; NaOH handling required (caustic burns risk); exact lye calculation critical (excess lye = harsh soap, insufficient lye = greasy bar); superfatting must be calculated precisely; not suitable for glycerol recovery (glycerol is trapped in the bar).
- **Lye calculation**: Weight of oil × SV ÷ 1000 × 0.713 (ratio of NaOH molecular weight to KOH) = grams NaOH needed. Apply superfat discount (typically 5%).
- **Water amount**: Typically 30-40% of oil weight. Less water → faster trace, harder bar sooner, but higher risk of lye pockets. More water → slower trace (more working time), longer cure. "Water as percent of lye" method: 2:1 to 3:1 water:lye ratio by weight.
- **Mold insulation**: Wrap molds in towels or blankets during gel phase. Full gel (entire batch reaches translucent gel state) produces uniform texture. Partial gel (center gels, edges don't) causes uneven texture — cosmetic issue only, does not affect soap quality.

**[Hot process](../glossary/hot-process.md)** (faster cure, used with KOH for soft soap):
- Heat fat to 70-80°C. Add KOH solution (from [Alkalis](alkalis.md)) gradually with constant stirring. Maintain temperature for 2-4 hours with periodic stirring until mixture reaches "trace" and then thickens further into a translucent paste (KOH soaps remain paste-like). The extended cooking accelerates saponification — soap is usable within days rather than weeks. KOH soap (soft soap) is stored in containers rather than molded into bars.
- Hot process with NaOH is also possible: cook the traced soap in a slow cooker or double boiler at 75-85°C for 1-2 hours until it reaches a translucent, vaseline-like consistency. This forces saponification to complete rapidly. Soap is usable immediately after cooling (no 4-6 week cure needed), though an additional 1-2 weeks of drying improves bar hardness.

**Strengths**: Soap usable within 1-3 days (no 4-6 week cure); heat drives saponification to completion — no risk of unreacted fat; works with KOH to produce soft/liquid soap for textile scouring and cleaning; more forgiving of imprecise lye measurements than cold process.

**Weaknesses**: Requires sustained external heat source (fuel cost); KOH soap is paste/liquid — cannot form hard bars; constant stirring needed to prevent scorching; glycerol retained in soap (no recovery); higher energy input than cold process.

**[Kettle process (graining out)](../glossary/kettle-process-graining-out.md)** — the traditional batch method for glycerol recovery:
- Heat fat to 38°C in a large kettle (iron or steel, 1-5 tonne capacity). Add concentrated NaOH solution (or KOH for soft soap) gradually with constant stirring. Continue heating and stirring for 2-3 hours until saponification is complete (mixture thickens, no free fat remains — test by dissolving a sample in hot alcohol; cloudiness indicates unsaponified fat).
- **Graining out**: Add NaCl (common salt, ~100-150 g per kg of original fat) to the completed saponification mixture. Salt causes the soap to separate and float to top as curds ("graining") while glycerol, excess lye, and salt remain in the lower aqueous layer ("spent lye" or "soap waste liquor"). Remove soap curds, wash with brine to remove residual glycerol and lye, press to remove excess liquid, mold into bars, and dry.
- **Spent lye**: Contains glycerol (8-15%), salt, and residual NaOH — the primary feedstock for glycerol recovery.
- **Kettle construction**: Wrought iron or steel, riveted or welded, with a firebox beneath and a draw-off valve near the bottom. Capacity: 5-20 tonnes of batch material. Steam coils or jacket for temperature control preferred over direct fire (more uniform heating, less scorching).

**Strengths**: Recovers glycerol as valuable co-product (enables explosives production); salt separation produces harder, purer soap than cold/hot process; scalable to 5-20 tonne batches; well-established industrial method for 200+ years.

**Weaknesses**: Requires large iron/steel kettle and salt supply; multi-step process (saponify, grain, wash, press, dry); glycerol recovery needs separate evaporation/distillation equipment; spent lye disposal if glycerol not recovered.

**Lye from wood ash (pre-industrial)**:
- Hardwood ash (oak, beech, maple) leached with water produces KOH solution. Boil to concentrate. Test concentration: float a fresh egg — if it bobs with ~2 cm (dime-sized area) exposed, concentration is approximately 10% KOH, suitable for soap making. This method produces soft soap (potassium-based). See [Alkalis](alkalis.md) for potash production details.
- Once [Alkalis](alkalis.md) production is established (Leblanc or Solvay process), NaOH from the lime-soda process or chlor-alkali electrolysis replaces wood-ash lye, enabling hard bar soap.

## Industrial Soap Production

**[Continuous saponification](../glossary/continuous-saponification.md)** (modern, large-scale):
- Fat and concentrated NaOH solution (30-50%) fed continuously into a saponification reactor at controlled ratio. The Sharples or Mazzoni continuous process uses a high-shear mixing column — fat and lye enter at bottom, react during upward flow, and fully saponified soap exits at top. Residence time: 15-30 minutes. Temperature: 70-80°C. Throughput: 1-10 tonnes/hour.
- The key engineering challenge is maintaining exact stoichiometric ratio: excess lye produces harsh, alkaline soap; excess fat leaves unsaponified grease. Inline conductivity or pH measurement controls lye feed rate automatically.
- Soap exits the reactor as a homogeneous hot mass (soap base, ~30% water). Feed directly into a vacuum spray dryer — atomize soap into a vacuum chamber, water flashes off. Soap emerges as dry flakes or "noodles" (extruded strands, 10-13% moisture). These soap noodles are the intermediate commodity traded between soap manufacturers.

**Strengths**: Highest throughput (1-10 tonnes/hour); consistent product quality via automated ratio control; continuous operation — no batch turnaround time; soap noodles are storable/tradeable intermediate commodity.

**Weaknesses**: High capital cost ($1-10M for full line); requires precise instrumentation (pH/conductivity control); not economical below ~100 tonnes/day; vacuum spray dryer adds complexity and energy cost.

**[Bar finishing](../glossary/bar-finishing.md)** (from soap noodles to finished bar):
- **Mixing**: Soap noodles + additives (fragrance, color, titanium dioxide whitener, antibacterial agents, moisturizers) mixed in an amalgamator (screw mixer) at 40-50°C.
- **Milling**: Pass soap through 3-5 roller mills (refining mills) to homogenize texture and eliminate air pockets. Rollers rotate at different speeds — shearing action refines the soap mass.
- **Plodding**: Extrude milled soap through a die (plodder/extruder) as a continuous bar. Air is vacuum-pumped from the extruder chamber to prevent air bubbles.
- **Cutting and stamping**: Cut extruded bar to length. Stamp with brand name or design in a soap press (hydraulic or pneumatic, 50-200 tonnes force). Package.
- **Quality control**: Test finished bars for total fatty matter (TFM, minimum 60% for grade 1 soap), free alkali (maximum 0.1% — higher causes skin irritation), moisture content (10-15%), and lather volume. pH test: dissolve 1 g soap in 100 mL distilled water, measure pH. Acceptable range: 9.0-10.5.

**[Semi-boiled process](../glossary/semi-boiled-process.md)** (intermediate between cold and kettle):
- Heat fat to 60-70°C. Add full-strength NaOH solution (30-40%). Stir continuously while maintaining temperature for 1-2 hours. Soap forms as a thick paste (does not grain out — no salt added). Pour into frames. Cures in 2-3 weeks. Retains all glycerol in the soap (no recovery). Simpler than kettle process, but glycerol is wasted in the product. Common for small-scale industrial soap production.

**Soap powder and flakes**:
- Spray-dry liquid soap base to powder. Alternatively, grind dried soap to flakes. Used for laundry applications before synthetic detergents. Soap powders perform poorly in hard water (calcium soap scum forms).

**[Detergent formulation](../glossary/detergent-formulation.md)** (complete laundry powder):
- LAS (surfactant): 8-15%. Sodium tripolyphosphate or zeolite (builder — softens water, suspends dirt): 20-35%. Sodium silicate (corrosion inhibitor, alkalinity): 5-10%. Sodium carbonate (alkalinity booster): 10-20%. Sodium perborate or sodium percarbonate (bleach): 10-20%. Enzymes (protease, lipase, amylase — protein, fat, starch stain removal): 0.5-2%. Optical brighteners: 0.1-0.3%. Sodium sulfate (filler/bulking agent): balance to 100%. The builder is critical — without it, surfactant efficiency drops dramatically in hard water. Phosphate builders (STPP) are most effective but cause eutrophication in waterways — zeolite A is the modern replacement.

## Glycerol Recovery

Glycerol (C₃H₈O₃, 1,2,3-propanetriol) is the critical byproduct of saponification. Before synthetic glycerol, soap making was the only source — and wartime demand for nitroglycerin explosives made glycerol recovery strategically essential.

**From soap waste liquor (spent lye)**:
- **Filtration**: Remove residual soap from spent lye by acidification (add dilute H₂SO₄ to pH 4-5 — free fatty acids precipitate) or by adding excess salt to "salt out" remaining soap. Filter.
- **Neutralization**: Add NaOH or Na₂CO₃ to neutralize residual acid. Filter precipitated salts.
- **Evaporation**: Concentrate the filtrate in multiple-effect vacuum evaporators to ~80% glycerol. Salt crystallizes out during evaporation (salt solubility decreases as glycerol concentration increases) — filter and recycle salt to soap graining process.
- **Distillation**: Distill crude glycerol under vacuum (12-15 mmHg) at 160-180°C. Glycerol boils at 290°C at atmospheric pressure — vacuum distillation prevents thermal decomposition. Collect purified glycerol (95-98%). Redistill or treat with activated carbon for higher purity (99.5%+).
- **Bleaching**: Pass distilled glycerol through activated carbon beds to remove color bodies. For pharmaceutical grade, redistill under high vacuum (5-8 mmHg) and treat with ion exchange resins to remove trace metal ions.
- **Yield**: ~10% glycerol by weight of fat saponified (tallow yields ~9-10%, coconut oil ~12-13%).
- **Energy cost**: Glycerol recovery from spent lye consumes ~3-5 tonnes steam per tonne of glycerol (primarily for multiple-effect evaporation). The vacuum distillation step adds another 0.5-1 tonne steam per tonne glycerol. Total energy: roughly 2-4 GJ per tonne of refined glycerol.

**Strengths**: Converts waste byproduct into high-value chemical feedstock; glycerol enables nitroglycerin explosives production (strategic); salt recycles back to graining process; pharmaceutical-grade glycerol commands premium price.

**Weaknesses**: Energy-intensive (2-4 GJ/tonne glycerol); requires multiple-effect evaporators and vacuum distillation equipment; acrolein formation at distillation temperatures is a serious hazard; 90% of output is CaCl₂ waste stream with limited market.

**[Alternative glycerol sources](../glossary/alternative-glycerol-sources.md)** (post-petroleum):
- **Hydrolysis of fats (not saponification)**: Fat + water (at 250-260°C, 40-50 bar, in an autoclave) → fatty acids + glycerol. No alkali consumed. The "Twitchell process" uses sulfuric acid + aromatic sulfonic acid catalyst. The "Colgate-Emery process" uses continuous high-pressure hydrolysis without catalyst. Fatty acids separated by distillation. Glycerol recovered from aqueous phase by evaporation and distillation. This route produces fatty acids for further chemical processing rather than soap directly.
- **Fermentation**: Certain yeasts and bacteria produce glycerol during fermentation of sugars. The "neutral sulfite process" (adding Na₂SO₃ to yeast fermentation) diverts ethanol fermentation toward glycerol production. Yields: 20-30% of sugar weight as glycerol. Historically important during World War I when German glycerol supplies were blockaded. Not economically competitive with soap-waste glycerol under normal conditions.

**Applications of glycerol**:
- **Nitroglycerin**: Glycerol + nitric acid + sulfuric acid → nitroglycerin (see [Explosives](explosives.md)). The military demand for explosives drove industrial glycerol recovery in the 19th century.
- **Food and pharmaceuticals**: Humectant, sweetener (60% as sweet as sucrose), solvent, preservative. Used in toothpaste, cough syrup, baked goods.
- **Chemical intermediate**: Produce allyl chloride (for epoxy resins), acrolein, and other compounds.
- **Cosmetics**: Moisturizer, skin protectant in soaps, lotions, and shaving products.
- **Dynamite**: Nitroglycerin absorbed onto diatomaceous earth or other porous material produces dynamite — safer to handle than liquid nitroglycerin. Glycerol supply chain directly determines explosives manufacturing capacity.

## Synthetic Detergents

Soap has a critical limitation: in hard water, calcium and magnesium ions precipitate soap as insoluble "soap scum" (calcium/magnesium salts of fatty acids). Synthetic detergents — surfactants derived from petroleum or oleochemical feedstocks — resist hard water precipitation and function across a wider pH range.

**[Linear alkylbenzene sulfonate (LAS)](../glossary/linear-alkylbenzene-sulfonate-las.md)** — the workhorse synthetic detergent:
- **Feedstock**: Linear alkenes (C10-C14) from petroleum cracking (see [Petroleum](petroleum-alternatives.md)) or linear paraffins from Fischer-Tropsch synthesis. Benzene from coal tar or petroleum refining.
- **Alkylation**: React linear alkene with benzene using HF or AlCl₃ catalyst → linear alkylbenzene (LAB).
- **Sulfonation**: React LAB with SO₃ (or concentrated H₂SO₄, or oleum) → linear alkylbenzene sulfonic acid (LABSA). SO₃ sulfonation is preferred — higher yield, less waste. SO₃ produced by catalytic oxidation of sulfur (vanadium pentoxide catalyst, see sulfuric acid production in [Acids](acids.md)).
- **Neutralization**: LABSA + NaOH → sodium linear alkylbenzene sulfonate (LAS). Water-soluble anionic surfactant. Biodegradable (the linear alkyl chain differentiates LAS from the older, environmentally persistent branched alkylbenzene sulfonate — ABS).
- **Application**: Primary surfactant in laundry detergents, dish liquids, all-purpose cleaners. Typical concentration: 10-25% in liquid detergent, 8-15% in powder.

**Strengths**: Functions in hard water without precipitation (unlike soap); effective across wide pH range (acidic to alkaline); biodegradable linear chain; 60+ years of proven industrial-scale production; versatile across laundry, dish, and industrial cleaning.

**Weaknesses**: Requires petroleum cracking or Fischer-Tropsch feedstock; benzene is a confirmed carcinogen (handling risk in alkylation unit); SO₃ sulfonation is extremely corrosive and hazardous; phosphate builders needed for full performance (eutrophication concern).

**Alkyl sulfates**:
- **Sodium lauryl sulfate (SLS)**: Coconut or palm kernel fatty alcohol (C12-C14) + SO₃ or chlorosulfonic acid → alkyl sulfate. Excellent foaming and cleaning, used in shampoos, toothpaste, and bubble bath. Produced from oleochemical feedstocks (renewable route) or from petrochemical ethylene (Ziegler alcohol process).
- **Sodium laureth sulfate (SLES)**: Ethoxylated derivative of SLS (add 1-3 ethylene oxide units). Less irritating than SLS, better foam stability. Dominant surfactant in personal care products.

**Nonionic surfactants**:
- **Alcohol ethoxylates**: Fatty alcohol (C12-C15) + ethylene oxide (2-20 EO units). No ionic charge — effective in hard water and at low concentrations. Used as low-sudsing detergents, wetting agents, and emulsifiers.
- **Alkylphenol ethoxylates (APEOs)**: Historically important but now restricted due to endocrine-disrupting breakdown products (nonylphenol). Replaced by alcohol ethoxylates in most applications.

**Soap-based grease thickeners**:
- Alkali soaps (lithium, calcium, sodium, aluminum stearate) thicken mineral oil into lubricating grease. Lithium 12-hydroxystearate is the most common multipurpose grease thickener. See [Lubricants](lubricants.md).

**[Builder chemistry](../glossary/builder-chemistry.md)** (critical detergent component):
- Detergents cannot function effectively without builders — chemicals that sequester calcium and magnesium ions, preventing them from interfering with the surfactant. Builder choice determines detergent performance in hard water.
- **Sodium tripolyphosphate (STPP)**: Most effective builder. Sequesters Ca²⁺ and Mg²⁺, disperses soil particles, provides alkalinity. Produced from phosphoric acid + NaOH. Environmental concern: phosphate discharged to waterways causes algal blooms and eutrophication. Phosphates banned in laundry detergents in many jurisdictions.
- **Zeolite A (sodium aluminosilicate)**: Primary phosphate replacement. Ion-exchange builder — swaps Na⁺ for Ca²⁺ in its crystal structure. Produced from sodium silicate + sodium aluminate. Insoluble — suspended in wash water, rinsed away. Effective but slower than STPP. Often combined with polycarboxylate co-builder (polyacrylic acid) for performance matching STPP.
- **Sodium citrate**: Mild builder, biodegradable. Used in "eco" formulations. Less effective than STPP or zeolite at high water hardness.
- **Sodium carbonate (washing soda)**: Provides alkalinity and precipitates calcium as CaCO₃. Cheap but produces insoluble precipitate (deposits on fabrics and machine parts). Best as co-builder rather than primary.

## Specialty Soaps

**Textile scouring soap**:
- Raw wool contains 30-50% impurities: lanolin (wool wax), suint (dried sweat, water-soluble), dirt, vegetable matter. Scouring removes these before carding, spinning, and dyeing. Use warm (45-55°C) aqueous solution of KOH soft soap or nonionic surfactant (0.5-2% concentration). Multiple wash stages: first scour (heavy soil removal), second scour (residual wax), rinse. Recover lanitin from spent scouring liquor by acidification and centrifugation — lanolin is a valuable byproduct used in cosmetics and corrosion inhibitors. Cotton scouring removes natural waxes and pectins using NaOH solution (1-3% at 90-100°C under pressure) — not soap but related alkaline cleaning.

**Metal cleaning and degreasing**:
- Alkaline soap solutions (2-5% NaOH + sodium stearate) remove drawing compounds, machining oils, and forming lubricants from metal surfaces before heat treatment, plating, or painting. Heat to 60-80°C, immerse parts for 5-30 minutes, rinse. For heavy grease, use emulsion cleaners (soap + petroleum solvent blend). Electrolytic cleaning: make the workpiece the cathode in an alkaline soap solution — hydrogen evolution at the surface mechanically lifts contaminants.

**Medicinal soaps**:
- **Carbolic soap**: Contains phenol (carbolic acid, 1-3%). Antiseptic. Historically significant (Lister's antiseptic surgery). Phenol produced from coal tar (see [Distillation](distillation.md)).
- **Chlorhexidine soap**: Surgical scrub and hand wash. Broad-spectrum antimicrobial. Chlorhexidine is a synthetic biguanide antiseptic.
- **Povidone-iodine soap**: Iodine complexed with polyvinylpyrrolidone. Antiseptic scrub for preoperative skin preparation.

**Floating soap and translucent soap**:
- Floating soap: whip air into the soap mass before molding. Reduces density to ~0.9 g/cm³ — soap floats in water. Historically an accidental discovery during over-mixing, later commercialized. Translucent soap: dissolve soap in alcohol, let alcohol evaporate slowly — slow recrystallization produces transparent or translucent bars. Both are novelty products with no functional advantage but significant commercial history.

## Applications Table

| Application | Product Type | Key Properties | Notes |
|-------------|-------------|----------------|-------|
| Personal hygiene | Bar soap, liquid soap | Mild pH (~9-10), lather, skin cleaning | NaOH bar soap most common |
| Laundry (soft water) | Soap powder, soap flakes | Good cleaning, biodegradable | Replaced by LAS in hard water regions |
| Laundry (all water) | LAS-based detergent | Hard water tolerant, effective cleaning | Requires petroleum or FT feedstock |
| Textile scouring | KOH soft soap, nonionic surfactant | Removes spinning oils, wax, dirt | Critical step before dyeing and bleaching |
| Metal degreasing | Alkaline soap solution, solvent-soap blend | Removes machining oils, drawing compounds | Often combined with NaOH soak |
| Emulsion polymerization | Sodium stearate, SLS | Stabilizes monomer droplets in water | Used for PVC, polystyrene, synthetic rubber |
| Food processing | Potassium soap, food-grade glycerol | Equipment cleaning, humectant | Strict purity requirements |
| Medical/hygiene | Antimicrobial soap (chlorhexidine, PCMX) | Broad-spectrum antimicrobial | Additive to soap base |
| Explosives feedstock | Glycerol (from spent lye) | Nitration to nitroglycerin | Strategic wartime material |

## Safety

- **NaOH and KOH handling**: Concentrated lye solutions (30-50%) cause severe chemical burns. Dissolve lye pellets in water slowly — the dissolution is strongly exothermic (solution temperature can exceed 90°C). Always add lye to water, never the reverse (prevents violent spattering). Wear chemical splash goggles, nitrile or neoprene gloves, and long sleeves. If skin contact occurs, flush with copious cool water for 15+ minutes.
- **Exothermic saponification**: The fat + lye reaction releases heat. In cold process, this is moderate (internal temperature 60-70°C during gel phase). In hot process and kettle process, the combination of external heating plus reaction heat can cause boiling and splattering. Add lye to fat gradually with continuous stirring.
- **SO₃ sulfonation** (synthetic detergents): Sulfur trioxide is extremely corrosive and reacts violently with water. Sulfonation reactors must be water-free. SO₃ fumes cause severe respiratory damage. Full respiratory protection, acid-resistant clothing, and emergency shower required.
- **Glycerol distillation**: Vacuum distillation at 160-180°C. Glycerol decomposition products (acrolein) are potent lachrymators and lung irritants. Maintain vacuum integrity. Acrolein detection and ventilation required.
- **Nitroglycerin production from glycerol**: See [Explosives](explosives.md) — nitroglycerin is shock-sensitive and extremely dangerous to manufacture.
- **Benzene exposure** (LAS production): Benzene is a confirmed human carcinogen (leukemia). Alkylation units handling benzene require closed systems, vapor recovery, and exposure monitoring. Occupational exposure limit: 0.5-1 ppm (8-hour TWA). Any detectable benzene in air warrants investigation.
- **Ethylene oxide** (ethoxylated surfactants): Ethylene oxide is a flammable gas (explosive range 3-100% in air), a confirmed carcinogen, and a reproductive toxin. Ethoxylation reactors operate under nitrogen atmosphere at 10-20 bar, 120-180°C. Strict containment, continuous gas monitoring, and emergency scrubbers required.

## Scale and Economics

- **Small-scale (cold process)**: 5-50 kg/batch. Equipment: stainless steel or enamel pot, stick blender, silicone molds, scale. Capital cost: <$500. Throughput limited by curing time (4-6 weeks). Suitable for community-scale production.
- **Medium-scale (kettle process)**: 1-5 tonnes/batch. Equipment: iron or steel kettle (2-5 m³), steam heating, mechanical stirrer, salt supply, pressing frames. Capital cost: $5,000-20,000. Batch cycle: 1-2 days saponification + graining, plus pressing and drying. Glycerol recovery adds distillation equipment ($10,000-50,000). Suitable for regional production.
- **Industrial (continuous saponification)**: 10-100+ tonnes/day. Equipment: continuous reactor, vacuum spray dryer, soap noodle line, bar finishing line. Capital cost: $1-10 million. Soap noodle production is highly automated. Marginal cost dominated by fat/oil feedstock price (60-70% of production cost).
- **Detergent plant (LAS)**: 20,000-100,000 tonnes/year. Requires sulfonation unit, spray-drying tower, and blending/packaging lines. Capital cost: $10-50 million. Feedstock cost dominates (petroleum-derived alkenes, benzene). Co-located with petroleum refinery or chemical complex for feedstock access.
- **[Fat/oil feedstock is the primary cost driver](../glossary/fatoil-feedstock-is-the-primary-cost-driver.md)** for all soap production. Tallow prices track beef production. Coconut oil and palm oil prices track tropical agriculture. A tonne of finished bar soap requires ~750-800 kg of fat/oil feedstock. Synthetic detergents are less dependent on agricultural commodities but tie to petroleum markets.

## Bootstrap Sequence

Soap production scales with the alkali supply chain. The progression is:

1. **[Wood-ash lye (KOH) + rendered fat → soft soap](../glossary/wood-ash-lye-koh-rendered-fat-soft-soap.md)** (Years 5-10). No industrial infrastructure needed. Hardwood ash, water, a kettle, and animal fat. Produces soft, paste-like potassium soap adequate for basic hygiene and wool scouring. Glycerol remains in the soap (no recovery).
2. **[NaOH from lime-soda or Leblanc process → hard bar soap](../glossary/naoh-from-lime-soda-or-leblanc-process-hard-bar-soap.md)** (Years 10-20). Once [Alkalis](alkalis.md) production is established, NaOH replaces KOH for hard, long-lasting bar soap. Kettle process with salt graining enables glycerol recovery.
3. **[Glycerol recovery and distillation](../glossary/glycerol-recovery-and-distillation.md)** (Years 15-25). Multiple-effect evaporators and vacuum distillation produce refined glycerol from spent lye. Enables [Explosives](explosives.md) production (nitroglycerin) and pharmaceutical glycerol supply.
4. **[Continuous saponification and industrial finishing](../glossary/continuous-saponification-and-industrial-finishing.md)** (Years 20-30). Continuous reactors, spray drying, soap noodles, and automated bar finishing lines. Throughput: 10-100 tonnes/day. Co-located with fat rendering and glycerol recovery.
5. **[Synthetic detergents](../glossary/synthetic-detergents.md)** (Years 25-30+). Requires petroleum cracking or Fischer-Tropsch synthesis for linear alkenes (see [Petroleum](petroleum-alternatives.md)), benzene, and SO₃ sulfonation capability. LAS-based detergents replace soap in hard-water regions and industrial applications.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Soap not setting (stays liquid) | Insufficient NaOH or too much water | Check lye concentration with hydrometer (target 30-35% NaOH); increase lye amount by 5% |
| Soap separating (oil layer on top) | Incomplete saponification — lye too weak or temperature too low | Heat to 80-85°C with stirring; verify lye concentration; extend cook time |
| Soap too harsh (dries skin) | Excess lye (superfat too low) | Increase fat by 5-8% (superfat); check lye weight carefully; re-batch with added fat |
| Glycerol recovery low | Spent lye not properly settled or salt contamination | Allow 24-48 hours settling; skim soap from surface; distill under vacuum |
| Detergent powder caking | Moisture absorption during storage | Add sodium sulfate anti-caking agent; improve packaging (plastic-lined bags); store dry |
| Hard water soap scum | Calcium/magnesium ions precipitating soap | Switch to synthetic detergent (LAS); add chelating agent (EDTA, citric acid) |

## See Also

- [Alkalis](alkalis.md) — NaOH and KOH production
- [Explosives](explosives.md) — glycerol feeds nitroglycerin production
- [Petroleum Alternatives](petroleum-alternatives.md) — feedstocks for synthetic detergents
- [Textiles / Fibers](../textiles/fibers.md) — wool scouring with soap
- [Occupational Health](../health/occupational-health.md) — hygiene and sanitation
- [Metal Finishing](../metals/finishing.md) — degreasing before plating and coating
- [Oil & Fat Processing](../food-processing/oil-processing.md) — tallow and vegetable oil as soap feedstock

[← Back to Chemistry](index.md)
