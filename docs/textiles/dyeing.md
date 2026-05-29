# Dyeing

> **Node ID**: textiles.dyeing
> **Domain**: [Textiles](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md)
> **Enables**: [`plants.dye-plants`](../plants/dye-plants.md), [`textiles.weaving`](weaving.md)
> **Timeline**: Years 5-10
> **Outputs**: dyed_cloth
> **Critical**: No

## Problem

Dyeing transforms undyed cloth and yarn into colored textiles using natural pigments extracted from plants, minerals, and insects. Color-fast results depend on proper mordanting (fixing dye to fiber), the right dye plants for the target hue, and careful control of bath temperature, pH, and duration. Protein fibers (wool, silk) take dye far more readily than cellulose fibers (linen, cotton) — a critical distinction that shapes the entire dyeing workflow.

### Prerequisites

- [Chemistry](../chemistry/index.md) — mordant chemistry, pH control, and extraction
- [Textiles / Fibers](fibers.md) — fiber preparation and properties
- [Plants / Dye Plants](../plants/dye-plants.md) — plant sources for dye pigments
- [Ceramics / Lime](../ceramics/lime.md) — calcium compounds for mordanting

## Mordant Preparation

Mordants are chemical intermediaries that bond dye molecules to fiber. Without a mordant, most natural dyes wash out within a few laundering cycles.

- **Alum (potassium aluminum sulfate, KAl(SO₄)₂)**: The universal mordant. Source alunite stone (KAl(SO₄)₂(OH)₆) by roasting and leaching, or collect stypteria (naturally occurring alum deposits) from volcanic soils. Dissolve 10-20% of fiber weight in hot water (60-80°C). Soak fiber for 1 hour. Works on both protein and cellulose fibers, though cellulose benefits from a tannin pre-mordant.
- **Iron (ferrous sulfate, FeSO₄)**: Darkens and "saddens" colors — turns yellow to olive, blue to gray-black. Make by dissolving iron scraps in vinegar (acetic acid) or stale urine. Use 2-5% of fiber weight. Overuse embrittles protein fibers — iron catalyzes oxidative degradation in wool and silk, causing progressive weakening and brittleness over months to years. Keep iron mordant concentrations below 5% for protein fibers.
- **Copper (copper sulfate, CuSO₄)**: Brightens greens and shifts yellows toward green. Use 2-5% of fiber weight. Toxic in high concentrations — handle with care. Copper mordant also improves light fastness of many yellow and green dyes by forming stable copper-dye complexes.
- **Tannin (from oak galls, sumac, chestnut, pomegranate rind)**: Essential pre-mordant for cellulose fibers. Boil 20-30% of fiber weight of tannin-rich material, strain, soak fiber 2-4 hours before alum mordanting. Tannins form hydrogen bonds with cellulose hydroxyl groups and provide sites for alum attachment. Oak galls contain 50-70% tannin by weight — the most concentrated natural source. Sumac leaves contain 20-30% tannin. Pomegranate rind contains 25-28% tannin.

**Strengths**:
- Alum mordant works on both protein and cellulose fibers at 10-20% WOF — universal applicability
- Tannin pre-mordant enables cellulose fibers to accept dye nearly as well as protein fibers
- Iron and copper mordants shift hues predictably (darkening or greening) without additional dye

**Weaknesses**:
- Iron mordant above 5% WOF embrittles protein fibers through oxidative degradation over months
- Copper sulfate is toxic if ingested — requires careful handling and waste disposal
- Chrome mordant (K₂Cr₂O₇) is a known carcinogen — health risk may outweigh color benefits

**Mordant chemistry**: Alum forms aluminum hydroxide complexes that bridge between fiber hydroxyl groups and dye carbonyl/hydroxyl groups. The aluminum ion (Al³⁺) coordinates with both the fiber surface and the dye molecule, creating a stable three-way bond. This coordination chemistry is why alum-mordanted fiber retains color through dozens of wash cycles while unmordanted fiber fades in 2-3 washes. Iron (Fe²⁺) and copper (Cu²⁺) function similarly but also form dark-colored metal-dye complexes that shift the hue.

### Dye Plant Cultivation

Growing dye plants ensures a reliable, renewable color supply. Most dye plants are undemanding perennials or self-seeding annuals:

- **[Madder](../glossary/madder.md)** (*Rubia tinctorum*): Perennial, hardy to Zone 5. Plant root cuttings in spring, spaced 30-40 cm apart in rows 50 cm apart. Requires 2-3 years for roots to reach harvestable dye concentration. Prefers deep, well-drained loam — roots penetrate 60-100 cm. Harvest in autumn of the second or third year. Dry roots thoroughly before storage. Yield: ~2-4 kg dried root per 10 m². Contains 1-3% alizarin by dry weight.
- **[Woad](../glossary/woad.md)** (*Isatis tinctoria*): Biennial (flowers in second year, then dies). Sow seed in early spring, 1 cm deep, 30 cm between plants. First-year leaves harvested 2-3 times per season. Prefers rich, alkaline soil. Yield: ~3-5 kg fresh leaf per 10 m² per cutting. Each kg fresh leaf yields ~2-4 g indigotin pigment. Grows throughout temperate Europe — was the primary blue dye source before imported indigo.
- **[Weld](../glossary/weld.md)** (*Reseda luteola*): Biennial or annual. Sow in spring, thin to 20 cm spacing. Harvest entire above-ground plant at flowering (peak luteolin concentration). Very easy to grow — tolerates poor soil. Yield: ~2-3 kg dried plant per 10 m². The most light-fast natural yellow dye.
- **[Dyer's coreopsis](../glossary/dyers-coreopsis.md)** (*Coreopsis tinctoria*): Annual, easy from seed. 60-90 cm tall, covered with red-orange-yellow flowers. Harvest flowers as they open. Rich in flavonoid dyes (luteolin, apigenin, coreopsin). Self-seeds prolifically.
- **[Japanese indigo](../glossary/japanese-indigo.md)** (*Persicaria tinctoria*): Annual in temperate zones. Higher indigotin yield than woad — 5-10× per kg of fresh leaf. Requires rich, moist soil and warm growing season. Harvest leaves 2-3 times per season. Best choice for blue where climate permits (USDA Zone 6+).

### Dye Plants & Color Range

- **Red**: Madder root (*Rubia tinctorum*) — harvest 3-year-old roots, dry, chop, extract at 70-80°C (higher temperatures degrade the alizarin pigment). Yields turkey red on alum-mordanted wool. Use 50-100% of fiber weight.
- **Blue**: Woad leaves (*Isatis tinctoria*) or true indigo (*Indigofera tinctoria*). Unlike other dyes, indigo requires no mordant — it bonds directly through reduction.
- **Yellow**: Weld (*Reseda luteola*) — whole plant above root, harvest at flowering. Bright clear yellow on alum-mordanted wool. Use 100-200% of fiber weight. Also: dyer's broom, goldenrod, onion skins (gold shades).
- **Brown/Black**: Walnut hulls (rich brown, no mordant needed). Oak bark, cutch (from acacia). For true black, overdye: indigo base + iron-tannin saddening, or madder + iron.
- **Orange**: Coreopsis, dyer's chamomile, or madder at lower concentrations with a tin mordant.

### Indigo Vat Process

Indigo pigment (indigotin) is insoluble in water. It must be chemically reduced to leuco-indigo (water-soluble, colorless) for dyeing. The fiber absorbs leuco-indigo; exposure to air re-oxidizes it back to insoluble blue pigment trapped inside the fiber.

1. **[Fermentation vat](../glossary/fermentation-vat.md)** (traditional): Fill a tall narrow vessel with warm water (40-50°C). Add woad or indigo powder (50-100 g/L), wheat bran (nutrient for bacteria), and wood ash lye (pH 9-10). Maintain 35-45°C for 3-7 days until the liquor turns yellow-green and a coppery scum forms. Stir gently, wait for sediment to settle.
2. **Dipping**: Wet fiber thoroughly, squeeze out excess water. Submerge in vat for 5-15 minutes. Squeeze gently — do not wring. Expose to air. Color develops from yellow-green → blue as indigo oxidizes. Repeat dips for darker shades (each dip adds a layer). Rinse after final dip.
3. **Troubleshooting**: Vat too cold → slow/failed reduction. Too hot (>55°C) → kills bacteria. pH too low → incomplete reduction. Stale vat (not used regularly) → add fresh bran and re-warm.

**Strengths**:
- Indigo bonds directly to fiber through oxidation — no mordant required for any fiber type
- Multiple dips build color intensity progressively from pale blue to deep navy
- Fermentation vat uses only plant materials (woad, bran, wood ash lye) — no industrial chemicals

**Weaknesses**:
- Fermentation vat requires 3-7 days to develop and must be kept at 35-45°C continuously
- Indigotin is insoluble in water — requires careful reduction chemistry to make a working dye bath
- Vat is sensitive to temperature and pH excursions; a failed vat wastes all ingredients

### Protein vs Cellulose Fiber Differences

| Property | Protein (wool, silk) | Cellulose (linen, cotton) |
|----------|---------------------|--------------------------|
| Dye affinity | High — scales and amino groups bond readily | Low — smooth crystalline surface resists bonding |
| Mordanting | Alum alone sufficient | Tannin pre-mordant → then alum |
| Bath temperature | 80-90°C (simmer, do not boil — felting risk) | 90-100°C (can boil, long soaks) |
| Typical uptake | Strong color at lower dye concentrations | Requires 2-3× more dye for equivalent shade |
| Indigo | Excellent — no mordant needed | Good — no mordant needed |

### Dye Bath Preparation & Calculations

Quantities scale with fiber weight. All percentages are **weight of dye material as a percentage of dry fiber weight** (WOF).

1. **Extract dye**: Chop/bruise plant material. Cover with soft water (rainwater preferred — hard water contains calcium that interferes with some dyes, particularly madder which shifts toward brown in hard water). Simmer 1-2 hours. Strain through cloth.
2. **Prepare bath**: Add enough water to submerge fiber freely — minimum 10:1 water-to-fiber ratio by weight (e.g., 10 liters water per 1 kg fiber). Less water produces uneven dyeing; more water wastes fuel. Dissolve mordant (if applying in same bath — "one-bath" method) or use pre-mordanted fiber.
3. **Enter fiber**: Wet fiber thoroughly first (pre-wetting ensures even uptake — dry spots resist dye). Add to dye bath at 40°C, raise slowly to target temperature over 30 minutes.
4. **Maintain**: Hold at temperature for 1-2 hours, stirring occasionally (every 10-15 minutes). Remove heat and let cool in bath overnight for deeper shades (exhaust dyeing — fiber continues absorbing as bath cools).
5. **Rinse**: Rinse in progressively cooler water until rinse water runs clear. Dry away from direct sunlight (UV degrades some dyes, particularly weld yellow).

**Sample calculations for 1 kg of wool yarn**:
- Madder red: 500 g dried madder root (50% WOF), 150 g alum (15% WOF), 100 liters water. Simmer at 75°C for 1.5 hours.
- Weld yellow: 1,500 g dried weld (150% WOF), 150 g alum (15% WOF), 100 liters water. Simmer at 85°C for 1 hour.
- Walnut brown: 1,000 g walnut hulls (100% WOF), no mordant needed, 100 liters water. Simmer at 90°C for 2 hours.

### Color Mixing & Overdyeing

Complex colors are built by layering dyes in sequence. Overdyeing follows the subtractive color model — each dye layer subtracts wavelengths from the reflected light:

- **Green**: Yellow base (weld) + blue overdye (indigo). Alternatively, weld + indigo in a single vat produces a range of greens depending on relative concentrations. Fresh indigo vat → bright chartreuse; 2 dips → medium green; 4+ dips → dark forest green.
- **Purple**: Red base (madder) + blue overdye (indigo). Madder at 30% WOF for pink, then 1-2 indigo dips for purple. Madder concentration controls warmth (more madder → warmer purple).
- **Black**: The hardest natural color to achieve. Most reliable sequence: (1) Tannin pre-mordant (oak galls, 25% WOF), (2) Iron after-treatment (5% WOF) → gray-black base, (3) Indigo overdye (2-3 dips) → deep blue-black. Alternative: madder (50% WOF) + logwood (30% WOF) + iron (3% WOF).
- **Teal**: Indigo base (2-3 dips for medium blue) + weld overdye (100% WOF) → blue-green. The weld yellow combines with the indigo blue to produce teal.
- **Orange-red**: Madder at high concentration (80-100% WOF) with tin mordant (2% WOF) shifts the hue toward orange. Alternatively, coreopsis (100% WOF) produces a clear orange directly.

**Overdyeing procedure**: Complete the first dye bath fully (dye, rinse, dry). Then mordant again if needed for the second dye, and enter the second dye bath. The second dye must be a different chemical class or applied at a different pH to avoid simply stripping the first color. Indigo is ideal as an overdye because it does not require a mordant and bonds through a completely different mechanism (oxidation vs. coordination chemistry).

### Resist Dyeing

Resist dyeing creates patterns by blocking dye from reaching selected areas of the cloth. Three principal methods:

**Tie-dye (bound resist)**:
- Bind sections of cloth tightly with waxed cord or sinew. The bindings compress the fabric, preventing dye penetration. Tighter and more wraps = larger undyed area.
- Dye the bound cloth in any dye bath (indigo works well because multiple dips build intensity without saturating the resisted areas). Remove bindings after dyeing and rinsing.
- Patterns: concentric circles (pinch fabric at a point, bind in a spiral), stripes (accordion-fold, bind at intervals), random spots (pinch and bind individual points).
- Results are geometric and somewhat unpredictable — the charm of the technique.

**Batik (wax resist)**:
- Apply molten wax (beeswax, melting point 62-65°C; or paraffin wax, mp 46-68°C; or a 50/50 blend — beeswax adheres better, paraffin cracks more for the characteristic "crackle" effect) to cloth using a tjanting tool (copper spout on wooden handle — wax flows through the spout by gravity) or brushes. Wax penetrates the fabric and blocks dye.
- Dye the waxed cloth in a cold or warm dye bath (hot dye melts the wax — indigo vats at 30-40°C are ideal). After dyeing, remove wax by ironing between absorbent paper or boiling in water (wax floats and can be skimmed and reused).
- Multiple colors require multiple wax-and-dye cycles. Lightest color first, darkest last. Each cycle adds wax to preserve the previous colors.
- Batik is the most precise resist method — fine lines and detailed imagery are possible with a skilled hand and a fine tjanting.

**Paste resist (flour paste, rice paste)**:
- Mix flour or rice paste to a thick consistency. Apply to cloth through a stencil or freehand. Allow to dry completely (12-24 hours). The dried paste forms a hard crust that resists dye.
- Dye the cloth by dipping or brushing. Paste-resisted areas remain undyed. Remove paste by washing in warm water.
- Japanese katazome uses rice paste (komon nori) applied through stencils cut from mulberry paper waterproofed with persimmon tannin. Produces sharp, repeatable patterns suitable for production work.

### Fastness Testing

- **Wash fastness**: Wash dyed sample in warm water with mild soap (5 min, 40°C). Compare color loss against unwashed control. Acceptable: minimal fading after 5 washes. Rate on 1-5 scale (5 = no change).
- **Light fastness**: Expose half the sample to direct sunlight for 1-2 weeks (cover the other half). Compare. Rate on 1-8 Blue Wool scale. Weld yellow and indigo blue rate 6-7 (excellent); many berry dyes rate 1-2 (poor — fade rapidly).
- **Rub fastness (crocking)**: Rub dyed fabric against white undyed cloth. Transfer indicates poor bonding — re-mordant and re-dye. Wet and dry rub tests are both performed. Acceptable: no visible transfer on dry rub, minimal on wet rub.

### Equipment

- Large non-reactive vessels: earthenware, ceramic, or stainless steel pots (iron pots act as a mordant and shift colors; copper pots brighten greens; avoid aluminum which corrodes in acid dye baths). Volume: 20-50 liters for cloth production.
- Heat source: wood fire with grate, or charcoal brazier. Temperature control by adjusting fuel and distance.
- Stirring sticks: wooden, long-handled.
- Drying racks: wooden frames with line.
- Protective gloves: leather or thick cloth — mordants and some dyes irritate skin.
- Tjanting tools for batik: copper spout (1-3 mm opening) on a wooden or bamboo handle. Wax melting pot (small iron or ceramic vessel with direct heat).
- pH testing: litmus paper or pH indicator solution. Critical for indigo vat management and mordant bath preparation.

---

*Dependencies: [Spinning](spinning.md) for yarn, [Weaving](weaving.md) for cloth, [Chemistry](../chemistry/index.md) for alum and iron sulfate production at scale*

### Safety & Hazards

- **Toxic mordants**: Alum (aluminum potassium sulfate) is relatively safe. Iron sulfate is a mild irritant. Copper sulfate is toxic if ingested. Chrome mordant (potassium dichromate, K₂Cr₂O₇) is a known carcinogen and must be handled with gloves. Tin chloride is toxic. Wear gloves when handling mordants.
- **Dye chemical hazards**: Some natural dyes contain toxic compounds. Logwood contains hematoxylin (moderately toxic). Indigo processing uses strong alkalis (slaked lime, NaOH). Weld and other plant dyes are generally safe.
- **Hot liquid burns**: Dye vats are heated to near-boiling (80-100°C). Splashes cause scald burns. Use long stirring sticks. Face protection when adding materials to hot vats.
- **Urine fermentation**: Historical indigo vats use fermented urine (ammonia source). Unpleasant odor, ammonia fumes irritating to eyes and respiratory tract. Ventilate dye work areas.
- **Wax burns (batik)**: Molten wax at 60-80°C causes burns. Use double-boiler heating to prevent overheating and flash fire. Never heat wax over open flame — risk of ignition at ~200°C. Keep a lid nearby to smother wax fires.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Textiles](./index.md) • [All Domains](../index.md)*

### Mordant Chemistry Detail

**Alum (Al₂(SO₄)₃ or KAl(SO₄)₂)**: The workhorse mordant for both protein and cellulose fibers.
- **Protein fibers** (wool, silk): Apply at 10-25% of fiber weight (owf). Dissolve in warm water at 60-80°C. Enter fiber, bring to 80-90°C over 30 minutes, hold 45-60 minutes. Wool and silk have amino and carboxyl groups in their protein structure that readily form coordination bonds with the aluminum ion (Al³⁺). The aluminum acts as a bridge: one coordination bond to the fiber surface, one to the dye molecule's hydroxyl or carbonyl groups. This three-way bond is the basis of color fastness. Higher alum concentrations produce deeper color but risk stiffening the fiber — stay below 25% for wool.
- **Cellulose fibers** (cotton, linen): Apply at 5-15% owf, but always after a tannin pre-mordant. Cellulose hydroxyl groups bond less readily with aluminum than protein amino groups. The tannin pre-treatment provides phenolic groups that bond strongly with both cellulose and alum, effectively extending the bonding sites on the fiber surface.

**Iron (FeSO₄)**: Darkens and "saddens" colors at 2-5% owf. Iron shifts yellow dyes to olive-green, shifts blue dyes to gray-blue, and combined with tannin produces gray-black. Iron forms colored complexes with dye molecules (iron-gall black from tannin + iron is the classic ink formula). Warning: iron catalyzes oxidative degradation of protein fibers. Wool mordanted with >5% iron gradually weakens and becomes brittle over months. Limit iron to 2-3% for wool, or use only on cellulose fibers where the degradation risk is lower.

**Copper (CuSO₄)**: Shifts colors toward green at 3-5% owf. Yellow dyes become brighter green, blue dyes become teal. Copper also improves light fastness by forming photostable copper-dye complexes that resist UV degradation. Handle copper sulfate with gloves: it is toxic by ingestion (causes GI distress, liver damage at higher doses) and irritating to skin and eyes. Dispose of spent copper dye bath in a designated waste container, not down the drain.

**Chrome (K₂Cr₂O₇, potassium dichromate)**: Brightens and deepens colors at 1-3% owf. Produces especially rich reds and yellows on wool. Chrome mordanting was standard in professional dyeing for centuries. However, hexavalent chromium (Cr⁶⁺) is a known carcinogen, causes skin ulcers on contact, and damages kidneys and liver. Handle with nitrile gloves in a well-ventilated area. Avoid generating dust when weighing. Spent chrome baths are hazardous waste — collect and treat with reducing agent (sodium bisulfite) to convert Cr⁶⁺ to less toxic Cr³⁺ before disposal. Consider whether the color result justifies the health risk; alum and tin are safer alternatives for most colors.

### Dye Bath Calculations

**Dyebath ratio**: The ratio of water to fiber by weight. Standard range: 20:1 to 40:1 (e.g., 20 liters water per 1 kg fiber). A lower ratio concentrates the dye and exhausts faster but risks uneven dyeing because the fiber cannot move freely. A higher ratio produces more even results but wastes fuel heating excess water. For immersion dyeing of cloth, 30:1 is a practical compromise.

**Temperature ramping**: Raise the dye bath temperature at 1-2°C/minute (60-120°C per hour). Faster heating causes uneven dyeing because the outer layers of the fiber absorb dye at the higher temperature before the interior reaches equilibrium. This is especially critical for cellulose fibers, which have lower dye affinity — the bath must be hot enough throughout the fiber cross-section for the dye to penetrate. Wool is more forgiving but risks felting above 85°C (agitate gently, do not boil).

**Hold time**: Maintain peak temperature for 30-60 minutes, depending on the dye and fiber type. Short holds (30 min) suit high-affinity combinations (wool + madder). Long holds (60 min) suit low-affinity combinations (cotton + weld). For the deepest shades, turn off the heat after the hold and let the fiber cool in the bath overnight (exhaust dyeing). The fiber continues to absorb dye as the bath cools.

### Overdyeing Procedure

Layering dyes to create compound colors follows a reliable workflow:

- **Blue + yellow → green**: Dye the fiber with weld yellow first (100-150% WOF, alum mordant, 85°C, 60 min). Rinse, dry. Then overdye in an indigo vat (1-3 dips depending on desired green depth). The indigo deposits blue over the yellow base, producing green. More indigo dips → darker, cooler green. Fewer dips → brighter chartreuse.
- **Red + blue → purple**: Dye with madder at 30-50% WOF for a pink-red base. Rinse, dry. Overdye in indigo (1-2 dips). The combination produces purple, with the exact shade determined by the relative strength of the red base and the blue overdye. More madder → warmer purple. More indigo → cooler purple.
- **General rule**: Always dye the lighter shade first. A light color cannot cover a dark one. If the first dye bath is red and the second is yellow, the result will look orange-yellow, not green. Plan the sequence based on which dye has the stronger affinity and which contributes the dominant hue.

### Resist Dyeing Detail

**[Tie-dye](../glossary/tie-dye.md)** (bound resist): Bind sections of pre-wetted cloth tightly with waxed linen thread or sinew. Wrap 5-10 times at each binding point, pulling very tight to compress the fabric through its full thickness. The compressed areas resist dye penetration. Immersion dyeing for 30+ minutes in a warm dye bath gives the best penetration. Multiple binding patterns: concentric circles (pinch a point, spiral the fabric around it, bind at intervals), parallel stripes (accordion-fold the cloth, bind at regular intervals), and random patterns (pinch individual points, bind tightly). After dyeing and rinsing, snip the bindings and unfold. The resisted areas show the original cloth color against the dyed background.

**[Batik](../glossary/batik.md)** (wax resist): Apply molten wax at 60-70°C (beeswax melts at 62-65°C, paraffin at 46-68°C). A 50/50 blend of beeswax and paraffin gives good adhesion (from the beeswax) and crackle texture (from the paraffin). Use a tjanting tool (copper spout, 1-3 mm opening, on a bamboo handle) for fine lines. Use a flat brush for broad areas. The wax must fully penetrate the cloth — hold it up to the light and check that no pinholes remain in the waxed areas. Dye in a cool-to-warm bath (indigo at 30-40°C is ideal; hot baths melt the wax). For multiple colors, repeat the wax-and-dye cycle: apply wax to preserve the first color, then dye in the second color. Boil the finished cloth in water to melt out the wax (skim and reuse). Three to four color cycles are practical before the wax buildup becomes unmanageable.

**Paste resist (flour/rice paste)**: Mix flour or rice paste with water to a thick, creamy consistency (like cake batter). Apply through a stencil cut from waterproofed paper or thin sheet metal. Let dry completely (12-24 hours) until the paste forms a hard, crack-resistant crust. Dye by dipping or brushing. The paste blocks dye from reaching the covered areas. Remove the paste by washing in warm water. Japanese katazome uses rice paste (komon nori) applied through mulberry paper stencils waterproofed with persimmon tannin, producing sharp, repeatable patterns suitable for production-scale work.

### Dye Bath Temperature Control

Temperature management is the single most important factor in consistent dyeing. The target temperature determines dye uptake rate, color development, and fiber integrity:

- **Wool**: Never exceed 90°C (simmer, not boil). Boiling causes felting — the wool fibers' scales interlock irreversibly, shrinking and matting the cloth. Maintain 80-85°C for most wool dyeing. Use a thermometer or visual cue: steam rising, small bubbles on the vessel wall, but no rolling boil.
- **Cotton and linen**: Can tolerate 95-100°C (full boil). Cellulose fibers require higher temperatures and longer dyeing times than protein fibers because dye penetration into the crystalline cellulose structure is slower. A 60-minute hold at 95°C is typical for cotton.
- **Indigo vat**: 30-40°C (hand-warm). The bacterial fermentation in a traditional vat is killed above 55°C. A chemical reduction vat (using sodium dithionite or thiourea dioxide) can operate at 50-60°C, but higher temperatures risk over-reduction and unstable color.
- **Temperature ramp**: Raise the bath at 1-2°C/minute. Faster heating produces temperature gradients within the fiber — the outer layers absorb dye at a higher rate than the interior, producing ring-dyeing (color on the surface only, pale core). This is the most common cause of uneven dyeing.

### Mordant Bath Reuse

Mordant baths can be reused for multiple batches, reducing chemical consumption:

- After removing the first batch of fiber, test the remaining bath for alum concentration. A simple test: add a few drops of the spent bath to a solution of ammonium phosphate. A white precipitate indicates residual aluminum. If precipitate forms, the bath still has mordanting capacity.
- Replenish the bath by adding 50-75% of the original mordant quantity before the next batch. The fiber absorbs roughly 50-80% of the dissolved alum during a standard mordanting session, depending on fiber type and duration.
- A well-maintained mordant bath can process 5-10 batches before the accumulation of impurities (dissolved organics from the fiber, hardness minerals from the water) requires the bath to be discarded. Discarded alum baths are not highly toxic (alum is used in water purification) but should be diluted before discharge.

### Color Fastness Standards

Quantifying dye permanence allows consistent quality control across batches:

**Wash fastness (1-5 scale)**: Wash a dyed sample in warm water with mild soap (5 min, 40°C, mechanical agitation). Compare the washed sample and the wash water against a grey scale. Grade 5 = no color change, no staining of adjacent fabric in the wash. Grade 1 = severe fading or bleeding. Acceptable minimum for garment textiles: Grade 3-4. Indigo rates 4-5 (excellent). Most berry dyes rate 1-2 (poor — fades in 2-3 washes).

**Light fastness (1-8 Blue Wool scale)**: Expose half the dyed sample to direct sunlight for 100-200 hours (or use a UV lamp for accelerated testing). Cover the other half. Compare the exposed and unexposed halves against the Blue Wool reference cards (8 strips of wool dyed with standard dyes of known lightfastness, each one twice as fast as the previous). Grade 8 = no perceptible change (permanent). Grade 1 = large change after minimal exposure. Weld yellow: 6-7 (very good). Madder red: 4-5 (good). Onion skin yellow: 2-3 (poor). Blackberry purple: 1 (very poor — fades in days of sun exposure).

**Rub fastness (crocking)**: Mount the dyed sample on a flat surface. Rub with a standard white cotton cloth under controlled pressure (9 N, 10 strokes). Assess the degree of color transfer to the white cloth on a 1-5 grey scale. Wet and dry tests are both performed. Acceptable: Grade 4 dry, Grade 3 wet. Poor rub fastness indicates insufficient mordanting or incompletely fixed dye.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Dye washes out after first laundering | Insufficient mordanting or wrong mordant for fiber | Increase alum to 15-20% of fiber weight; add tannin pre-mordant for cotton/linen; verify bath temperature 60-80°C |
| Uneven color (patchy) | Fiber not properly scoured or dye bath too concentrated | Scour fiber thoroughly before dyeing; dilute dye bath; ensure even temperature distribution |
| Color too pale | Not enough dye material or bath exhausted | Increase dye plant material (target 50-100% WOF); simmer longer; extract dye in multiple batches |
| Fiber damaged (brittle wool) | Iron mordant overdose or bath too hot | Reduce iron to <5% of fiber weight; keep protein fiber baths below 90°C; use alum instead |
| Brown spots on dyed cloth | Iron contamination from pot or water | Use stainless steel or enamel dye pot; test water for iron; add a chelating agent (citric acid) |
| Color shifts after drying | pH-sensitive dye reacting to rinse water | Use neutral pH rinse water; add a vinegar rinse for acid-sensitive dyes; dry in shade |

## See Also

- [Fibers](fibers.md) — fiber preparation, scouring, and properties
- [Weaving](weaving.md) — weaving dyed yarn into cloth
- [Dye Plants](../plants/dye-plants.md) — plant sources for natural pigments
- [Chemistry](../chemistry/index.md) — mordant chemistry and pH control
- [Coatings](../chemistry/coatings.md) — related pigment and coating chemistry
- [Finishing](finishing.md) — post-dye textile finishing processes

[← Back to Textiles](index.md)
