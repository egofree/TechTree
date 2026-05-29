# Fabric Finishing

> **Node ID**: textiles.finishing
> **Domain**: [Textiles](./index.md)
> **Dependencies**: [`chemistry.alkalis`](../chemistry/alkalis.md), [`textiles`](./index.md), [`textiles.weaving`](weaving.md)
> **Enables**: [`textiles.dyeing`](dyeing.md), [`polymers.rubber`](../polymers/rubber.md)
> **Timeline**: Years 8-14
> **Outputs**: finished_cloth, waterproof_fabric, fireproofed_textiles
> **Critical**: No

Fabric finishing transforms raw woven cloth into functional textiles: denser wool through fulling, smoother surfaces through calendering, whiter fabric through bleaching, stronger cotton through mercerization, and water-resistant or fire-resistant cloth through chemical treatments. Each finishing process alters specific cloth properties without changing the underlying fiber or weave structure.

## Prerequisites

- [Alkalis](../chemistry/alkalis.md) — caustic soda for mercerization and bleaching
- [Weaving](weaving.md) — woven cloth as input material
- [Dyeing](dyeing.md) — color processes that interact with finishing

## Fulling

Fulling cleans, shrinks, and felts woven cloth. The process transforms a loose, open weave into a compact, dense fabric by matting the fiber scales together. Wool is the primary candidate because its scaly fiber structure felts readily under moisture, heat, and mechanical action. Cotton and linen can also be fulled, but the effect is less pronounced because these fibers lack the scales that drive wool felting.

**Fulling process**:
- Cloth is soaked in warm water (40-50°C) with a fulling agent. Fuller's earth (a clay rich in aluminum silicate, also called kaolin or bentonite) is the traditional agent. Alternatively, aged urine (source of ammonia, NH₃) or soap acts as the detergent. The alkaline environment softens the wool fiber scales, allowing them to interlock more readily.
- Mechanical agitation drives felting. The traditional fulling stock is a water-powered hammer with rounded wooden heads that pounds the wet cloth in a trough. The pounding causes fibers to migrate and interlock. Later, rotary fulling mills (two large wooden rollers that compress and rotate the cloth) replaced stocks in larger operations.
- Duration: 2-8 hours depending on desired shrinkage. Wool cloth shrinks 10-20% in length and width during fulling. This shrinkage is planned: cloth is woven wider and longer than the finished dimension.
- Result: fabric becomes denser, thicker, more wind-resistant, and more water-repellent. The interlocked fiber scales create a surface that sheds light rain. Broadcloth, kersey, and melton are all heavily fulled wool fabrics.
- Weight gain: fulling increases fabric weight per unit area by 10-30% (the same amount of fiber compressed into a smaller area). This is a measure of how tightly the fabric has been fulled and is checked by weighing a measured area before and after.

**Fuller's earth preparation**:
- Dig clay from deposits (often found near chalk or limestone formations). Dry, crush, and sieve to fine powder (< 0.5 mm particle size). Mix with water to form a slurry at 50-100 g/liter concentration.
- After fulling, rinse the cloth thoroughly in clean water to remove residual clay. Incomplete rinsing leaves a chalky residue that stiffens the fabric and attracts dirt. The rinse water should run clear before the cloth is removed from the rinse bath.

**Fulling machinery construction**:
- Fulling stocks: two wooden hammers (each 15-25 kg, elm or oak) mounted on a cam shaft driven by a water wheel or later a steam engine. The hammers alternately pound the cloth in a wooden trough (1.5-2 m long, 0.5-0.8 m wide). The cam lifts each hammer 0.3-0.5 m, then drops it. Cycle rate: 30-60 blows per minute per hammer. The cloth is folded in the trough and slowly turned by hand between hammering sessions.
- Rotary fulling mill: two large wooden rollers (0.3-0.5 m diameter, 1-2 m long) mounted in a heavy timber frame. The cloth passes between the rollers under pressure (adjusted by adding weights to the top roller bearing). The rollers compress and stretch the cloth alternately, driving felting without the violent impact of stocks. Throughput: 50-100 m of cloth per batch, compared to 10-20 m for stocks.

**Strengths**:
- Fulling increases fabric density 10-30% without adding material — same fiber in smaller area
- Wool felting creates natural water repellency from interlocked fiber scales
- Rotary fulling mill processes 5-10× more cloth per batch than hammer stocks

**Weaknesses**:
- Wool shrinks 10-20% during fulling — cloth must be woven oversize to compensate
- Fulling stocks require water wheel or steam power for the cam shaft
- Incomplete rinsing leaves chalky residue that stiffens fabric and attracts dirt

## Napping (Raising)

Napping pulls fiber ends to the surface of the cloth, creating a soft, fuzzy pile. This improves insulation (trapped air in the nap) and gives the fabric a warmer hand feel.

**[Teazle raising](../glossary/teazle-raising.md)** (traditional):
- The dried flower head of the teasel plant (Dipsacus fullonum) has stiff, hooked bracts that catch and lift fiber ends without breaking them. Teazles are mounted in rows on a large cylindrical frame (teazle gig, 1-2 m wide, 1-1.5 m diameter). The cloth is held against the rotating teazle cylinder, and the hooks gently pull fibers upward.
- Multiple passes (4-8) gradually build the nap. Each pass raises more fiber. The cloth is brushed between passes to align the nap in one direction. The raised nap is then sheared to a uniform height with heavy shears.
- Teazles wear out and break during use. A fulling gig frame holds 15,000-30,000 teazle heads, which are replaced in sections as they wear. Teazles were grown as a crop specifically for textile finishing in 18th and 19th century England, occupying thousands of acres.

**[Wire card raising](../glossary/wire-card-raising.md)** (mechanized):
- Steel wire cards (hooked wire teeth set in a rubber or canvas backing) replace teazles. More durable and consistent than teazles, but harsher on fibers. Wire raising can break delicate fibers if the wire angle or pressure is set incorrectly.
- Wire raising is standard in modern finishing. Card clothing with 20-40 wire points per cm² in various wire profiles (straight, curved, sawtooth) for different fabric types and nap heights.

## Calendering

Calendering presses cloth between heavy rollers under heat and pressure to produce a smooth, polished surface. The rollers compress the fabric, flatten yarn irregularities, and create a sheen.

**Calender construction**:
- A calender is a stack of 2-5 rollers (bows), arranged vertically. Alternating hard rollers (chilled cast iron or polished steel) and soft rollers (compressed cotton or paper, sometimes called "bowl" rollers) create high-pressure nips. The soft roller deforms slightly under load, distributing pressure evenly across the full fabric width.
- Roller dimensions: 300-600 mm diameter, 1.5-3 m wide (matching fabric width). Pressure at the nip: 50-200 kN per roller, applied by hydraulic rams or screw-down mechanisms. The frame is heavy cast iron to resist deflection under these loads.
- Temperature: rollers heated to 100-150°C by internal steam pipes (steam at 200-400 kPa supplied to the roller interior via rotary joints) or gas burners. The heat sets the flattened fibers in place, making the finish more durable through subsequent handling.
- Drive: the rollers are driven by a gear train or individual motors synchronized to run at controlled speed differential. The friction nip (where the hard roller runs 2-5% faster than the fabric speed) is what produces the glazing effect.

**Calender finishes**:
- **Glazing**: high pressure + heat + friction (hard roller driven slightly faster than fabric speed, producing a rubbing action) creates a high-gloss surface on one side. Used for dress fabrics, book cloth, and decorative linings.
- **Chintz**: wax or resin applied before calendering. The calender burnishes the coating into a glass-like shine. The finish is not permanent; it diminishes with washing but can be renewed by re-calendering.
- **Embossing**: an engraved steel roller presses a pattern into the heated fabric. The pattern holds until the fabric is wetted and relaxed. Used for decorative effects on tablecloths and upholstery.
- **Schreiner calendering**: fine engraved lines (200-500 per cm) on a steel roller produce a subtle, silk-like luster without changing the fabric surface structure. Used on cotton to simulate the appearance of more expensive fabrics.
- **Friction calendering**: a single hard roller running 50-300% faster than fabric speed creates an intense glaze on one side. The high friction generates localized heating that partially melts and re-orients surface fibers. Produces the characteristic glazed surface on chintz and polished cotton.

**Strengths**:
- Calendering produces polished, professional fabric surfaces from rough loomstate cloth
- Multiple finish types (glazing, embossing, Schreiner) from the same machine with different roller setups
- Heated rollers at 100-150°C set the finish so it survives normal handling

**Weaknesses**:
- Heavy cast iron frame and 50-200 kN hydraulic rams require significant industrial investment
- Calender finishes are not permanent — washing and wear diminish glazed and embossed effects
- Roller temperature must be uniform across full width or finish is uneven edge-to-edge

## Singeing

Loose fiber ends on the cloth surface create a fuzzy appearance that accepts dye unevenly and attracts dirt. Singeing burns these protruding fibers off by passing the fabric rapidly over a gas flame or between heated plates. The process reduces surface hairiness by 70-90%, producing a cleaner, smoother surface.

**Gas flame singeing**:
- Cloth passes over a row of gas burners at 100-200 m/min. The flames (natural gas or propane, 800-1000°C) burn off protruding fibers in a fraction of a second. The fabric itself does not ignite because the exposure time is too short and the woven structure has too much thermal mass to heat to ignition temperature.
- Burner types: direct flame (cloth passes over open flame), tangential (flame contacts cloth at a shallow angle for lighter singeing), or cylinder (cloth wraps around a heated perforated cylinder with gas flames inside).
- After singeing, the cloth is quenched in water or passed through steam to extinguish any smoldering fibers. Skipping this step has caused warehouse fires from cloth that appeared extinguished but reignited hours later in storage.

**[Plate singeing](../glossary/plate-singeing.md)** (alternative):
- Cloth passes over heated copper or cast iron plates at 400-600°C. Slower than gas singeing, but useful where gas is unavailable. Plate temperature must be uniform across the full fabric width or singeing will be uneven (lighter in the center, heavier at the edges).

**[Desizing](../glossary/desizing.md)** (usually follows singeing):
- Warp yarns are coated with size (starch, PVA, or other adhesive) during weaving to strengthen them. After weaving, the size must be removed so the fabric can absorb dyes and finishing chemicals. Desizing dissolves or degrades the size by enzymatic action (amylase enzyme for starch, 60-70°C, pH 6-7, 4-8 hours), acid hydrolysis (dilute H₂SO₄, 0.5-1%, 50-60°C), or oxidation (hydrogen peroxide).

## Mercerization

Mercerization treats cotton with concentrated sodium hydroxide (NaOH) solution under tension. The treatment swells the cotton fibers, changing their cross-section from kidney-shaped to round. This increases luster, tensile strength (20-30% improvement), and dye affinity (dyes penetrate more readily and produce deeper shades).

**Process parameters**:
- Caustic concentration: 20-25% NaOH by weight (200-250 g/L). Temperature: 15-20°C (cold mercerizing gives best results; higher temperatures reduce the swelling effect significantly).
- Fabric is immersed in the caustic solution for 30-60 seconds while held under tension (stenter frame clamps the fabric edges and stretches it to its original dimensions). Without tension, the fabric shrinks 20-25% and becomes weaker (this is called slack mercerization and produces stretch fabrics, not standard mercerized cotton).
- After treatment, the fabric is washed thoroughly with hot water (60-80°C) to remove residual NaOH, then neutralized in dilute acetic acid (1-2% solution) and rinsed again. Caustic recovery: the wash water is collected and evaporated to recover NaOH for reuse (economic at industrial scale, where caustic consumption is 100-200 kg per ton of fabric).

**[Caustic soda production](../glossary/caustic-soda-production.md)** (bootstrap path):
- Sodium hydroxide is produced by the chlor-alkali process (electrolysis of brine: 2NaCl + 2H₂O → 2NaOH + H₂ + Cl₂). This requires electricity and a membrane or diaphragm cell.
- Lower-tech alternative: lime causticization. Sodium carbonate (Na₂CO₃, from the Solvay process) is reacted with calcium hydroxide (slaked lime): Na₂CO₃ + Ca(OH)₂ → 2NaOH + CaCO₃. The calcium carbonate precipitates, leaving NaOH solution. Less concentrated than electrolysis product (10-15% vs. 50%), but works without electricity.

**Mercerizing equipment**:
- A chain mercerizing range consists of: a padding mangle (two rubber-covered rollers that impregnate the fabric with caustic), a chain stenter (clips the fabric edges and stretches it to width under controlled tension while the caustic reacts), a washing zone (hot water sprays and squeeze rollers remove caustic), and a neutralizing bath (acetic acid dip, then final rinse). Total length: 20-40 m. Fabric speed: 20-50 m/min.
- The chain stenter is the critical component. It must hold the fabric at its target width (typically 10-15% wider than the gray fabric width) against the strong shrinkage force of the caustic-treated cotton. The clips grip the selvedge without marking the fabric surface. Chain tension and clip timing must be synchronized to prevent the fabric from bagging (loose) or overstretching (narrow).

**Strengths**:
- Mercerization increases cotton tensile strength 20-30% and dye affinity in a single treatment
- Treated fibers accept deeper, more vibrant dye shades — improves value of dyed cloth
- Caustic soda recoverable from wash water by evaporation — reduces ongoing reagent cost

**Weaknesses**:
- Requires 20-25% NaOH solution (200-250 g/L) — chlor-alkali or lime causticization needed
- Must treat fabric under tension at 15-20°C — chain stenter is a 20-40 m long machine
- Without tension, fabric shrinks 20-25% and becomes weaker (slack mercerization)

## Waterproofing

Wool and cotton absorb water readily (cotton holds up to 25% of its weight in water). Waterproofing treatments prevent water penetration while allowing the fabric to flex and breathe to varying degrees.

**Wax proofing**:
- Beeswax or paraffin wax applied at 50-100 g/m². The wax is melted (beeswax melts at 62-65°C, paraffin at 46-68°C) and either rolled into the fabric with heated rollers or brushed on by hand. The wax fills the interstices between yarns, creating a hydrophobic barrier.
- Reapplication needed every few months with heavy use. Wax coating stiffens in cold weather and softens or melts in hot weather. Not suitable for tropical climates where ambient temperature exceeds the wax melting point.
- Traditional application: sailor's canvas clothing and tents were waxed with a mixture of 2 parts beeswax to 1 part linseed oil, melted together and brushed onto the fabric while hot. The linseed oil polymerizes over several days, creating a more durable coating than wax alone. This "tin cloth" or "waxed cotton" was the standard waterproof fabric for outdoor work from the 18th century through the mid-20th century, when synthetic waterproof fabrics (Gore-Tex, polyurethane-coated nylon) replaced it.

**[Oil proofing](../glossary/oil-proofing.md)** (oilcloth):
- Linseed oil applied at 100-200 g/m² in multiple thin coats. Each coat is allowed to dry (oxidize and polymerize) for 3-7 days before the next coat. A finished oilcloth has 4-8 coats and takes 2-6 weeks to complete.
- Linseed oil polymerizes through oxidation. The polymerized film is flexible, waterproof, and reasonably durable (6-12 months of outdoor service before cracking and peeling). Adding a drying agent (cobalt or manganese salts, 0.01-0.05% by weight of oil) accelerates drying to 1-2 days per coat.
- Oilcloth production was a major industry in the 18th and 19th centuries. It produced waterproof tarps, table covers, and floor coverings (the precursor to linoleum).

**Rubber coating**:
- Natural rubber (latex) dissolved in naphtha (a petroleum fraction boiling at 80-120°C) to make a spreadable solution. Applied to fabric with a knife coater (a blade set at a controlled gap above the fabric surface, spreading a uniform rubber layer 0.1-0.5 mm thick). The coated fabric is heated in an oven at 100-130°C to evaporate the solvent and vulcanize the rubber.
- Vulcanization (adding sulfur, 2-4% by weight of rubber, plus heat at 140-160°C) cross-links the rubber polymer chains, improving elasticity, strength, and temperature resistance. Unvulcanized rubber becomes sticky in heat and brittle in cold.
- Mackintosh rainwear (1823) used rubber-coated fabric sandwiched between two layers of wool. The rubber layer made it fully waterproof but the early unvulcanized rubber deteriorated quickly. Vulcanized rubber coatings (post-1840) were far more durable.

## Fireproofing

Cellulose fibers (cotton, linen) and protein fibers (wool, silk) burn. Fireproofing treatments retard ignition and slow flame spread, buying time for escape. No treatment makes fabric completely fireproof; they make it flame-resistant.

**Boron salt treatment**:
- A solution of borax (sodium borate, 10% by weight in water) and boric acid (5%) is applied by soaking or spraying. Fabric is immersed for 15-30 minutes, wrung to 80-100% wet pick-up, and dried at 100-120°C. The boron salts remain in the fiber after drying.
- Borax melts at 743°C and forms a glassy layer on the fiber surface when heated, blocking oxygen access. Boric acid decomposes at 300°C, releasing water vapor that dilutes flammable gases. Together, they raise the ignition temperature and suppress afterglow.
- Effectiveness: increases ignition time from 3-5 seconds to 15-30 seconds for cotton. Reduces afterglow (smoldering) significantly. Durable through 3-5 washes; re-treatment required after that.

**[Phosphate salt treatment](../glossary/phosphate-salt-treatment.md)** (more durable):
- Diammonium phosphate (DAP, 10-15% solution) applied by padding (immersion and squeeze rollers). The phosphate promotes char formation rather than flaming. Char acts as an insulating barrier that slows heat transfer to the underlying fabric.
- DAP treatment is durable through 10-15 washes. It does not affect fabric hand (feel) significantly. Cost is low (DAP is a common fertilizer ingredient).
- Not suitable for fabrics that contact skin for long periods (slight skin irritation from residual phosphate). Used for curtains, upholstery, stage curtains, and tentage.

## Finishing Sequence Summary

The typical finishing sequence differs for each fiber type, because each fiber responds differently to the various processes. Getting the sequence right is critical: many finishing steps are irreversible.

**Cotton finishing sequence** (most complex):
1. Singeing → removes surface fuzz
2. Desizing → removes warp size (starch or PVA)
3. Scouring → removes natural waxes and spinning oils (boiling in NaOH 1-3% for 1-3 hours)
4. Bleaching → removes natural yellow pigment (H₂O₂ process)
5. Mercerizing → swells fibers, improves strength and dye affinity
6. Dyeing or printing → applies color
7. Finishing → calendering, stentering, and any special finishes (waterproofing, fireproofing)

**Wool finishing sequence**:
1. Fulling → shrinks and felts the fabric
2. Rinsing and drying → removes fulling agents
3. Carbonizing → removes vegetable matter (burrs, seeds) by impregnating with dilute H₂SO₄ (3-5%), drying, then baking at 100-120°C. The acid carbonizes the cellulose (vegetable matter) which is then removed by mechanical beating. The wool (protein fiber) is resistant to dilute acid and is not damaged.
4. Bleaching (optional) → removes natural cream color
5. Dyeing → applies color (wool takes acid and chrome dyes well)
6. Napping → raises fiber surface for insulation and hand
7. Decating → sets the surface with steam
8. Shearing → trims nap to uniform height
9. Calendering or pressing → produces final surface finish

## Dyeing Interaction with Finishing

The finishing sequence interacts with dyeing in important ways. Getting the order wrong wastes both time and materials. A typical finishing sequence for cotton is: singe → desize → scour → bleach → mercerize → dye → finish (calender, stenter). For wool: full → bleach → dye → finish (napping, calender).

- **Singe before dyeing**: singeing removes surface fibers that would accept dye unevenly, producing a patchy appearance. If dyed first and then singed, the burned fibers leave dark spots on the colored surface.
- **Full before dyeing** (for wool): fulling shrinks and felts the fabric, which changes the surface character. Dyeing after fulling produces a more uniform color on the denser surface.
- **Mercerize before dyeing** (for cotton): mercerization increases dye affinity by 20-40%. Mercerized cotton accepts dye more deeply and produces brighter shades from the same dye concentration. The savings in dye cost alone can justify the expense of mercerization for fabrics destined for deep or bright colors.
- **Bleach before dyeing**: bleaching removes natural pigments that would shift the final dye shade. Even dark-colored fabrics benefit from bleaching because residual yellow pigments in unbleached cotton shift blue dyes toward green and red dyes toward brown.

## Bleaching

Bleaching removes the natural color of fibers (yellowish in cotton, brownish in linen, creamy in wool) to produce a white base that accepts dyes more predictably. Even fabrics destined for dark colors benefit from bleaching because residual natural pigments can shift the final shade unpredictably.

**Cotton bleaching (hydrogen peroxide)**:
- Fabric is padded (immersed and squeezed between rollers to achieve 80-100% wet pick-up) in a solution of hydrogen peroxide (H₂O₂, 1-3% concentration), sodium silicate (stabilizer, 1-2%, prevents peroxide from decomposing too fast by sequesting metal ions that catalyze decomposition), and sodium hydroxide (pH adjuster, to pH 10-11). The alkaline environment activates the peroxide by converting it to the perhydroxyl anion (HOO⁻), the active bleaching species.
- The padded fabric is steamed at 95-100°C for 30-60 minutes in a J-box (a J-shaped heated chamber where fabric accumulates and dwells for the required reaction time without tension). The peroxide oxidizes the natural cotton pigments (yellow-brown flavonoid compounds) to colorless products.
- After steaming, the fabric is rinsed thoroughly in hot water (70-80°C) to remove residual chemicals. A well-bleached cotton fabric reaches a whiteness index of 85-95 (on a 0-100 scale where 100 is perfect white).

**Wool bleaching**:
- Wool is more sensitive to alkali than cotton (alkali dissolves the cystine cross-links in wool keratin, weakening the fiber), so hydrogen peroxide is used at lower temperature (50-60°C) and near-neutral pH (8-9) with a reduced dwell time (30-45 minutes). Over-bleaching degrades the wool fiber, causing yellowing and loss of tensile strength (10-20% strength loss is the maximum acceptable penalty).
- Alternative: sulfur dioxide (SO₂) gas stoving. Wool is exposed to SO₂ gas in a sealed chamber for 4-12 hours. The sulfur dioxide reduces colored impurities (a reductive bleach, as opposed to peroxide which is oxidative). Less damaging than peroxide but requires gas handling (SO₂ is toxic, TLV 2 ppm, and produces sulfurous acid on contact with moist mucous membranes) and produces a less permanent white (the yellowing returns over months with light exposure).

## Stentering and Heat Setting

After wet processing (fulling, bleaching, dyeing, mercerization), fabric is tensioned and dried to its final dimensions. Stentering pins the fabric edge to a chain that travels through a heated chamber, holding the fabric flat and at the correct width while moisture evaporates. This is the step that sets the final fabric width and length, preventing later shrinkage in washing or wear.

**Stenter frame**:
- Two parallel chains carrying pins (sharp steel pins, 3-5 mm long, spaced 5-10 mm apart) grip the fabric selvedge on each side. The chains are adjustable in width (typically 1.0-2.0 m) to set the finished fabric width. The chains carry the fabric through a heated chamber (150-200°C for cotton, 180-210°C for synthetics like polyester and nylon) over a dwell time of 15-30 seconds.
- Overfeed: the fabric is fed into the stenter 2-5% faster than the chain speed, allowing it to relax lengthwise while being held at width. This reduces residual tension and minimizes later shrinkage in washing. A fabric that is stentered without overfeed will shrink 3-5% in the first wash; with proper overfeed, shrinkage is reduced to 1-2%.
- Heat setting (for synthetic fabrics like polyester and nylon): heating above the glass transition temperature (polyester Tg ~70°C, Nylon Tg ~50°C) but below the melting point (polyester Tm ~260°C, Nylon Tm ~220°C) allows the polymer chains to relax into a stable configuration. The fabric "remembers" the dimensions it held during cooling, resisting shrinkage and wrinkling in subsequent use and washing.

## Decating

Decating is a finishing process for wool fabrics that sets the surface and improves luster and handle. The fabric is wound under tension onto a perforated drum, and steam is passed through the fabric layer for 5-15 minutes. The combination of moisture, heat, and pressure sets the nap direction and gives the fabric a smooth, stable surface that resists wrinkling and holds its shape during wear.

- Continuous decating: fabric passes between a heated cylinder (200-250°C, 300-500 mm diameter) and a pressing belt (endless felt or rubber belt, 3-5 mm thick). Steam is injected at the nip point. Speed: 10-30 m/min. Used for worsted suitings and dress fabrics where a permanent set is required.
- Batch decating: fabric is wound onto a perforated stainless steel drum (400-600 mm diameter) and steamed in a pressure vessel at 100-120°C for 10-20 minutes. More effective than continuous decating for heavy fabrics because the longer steam exposure penetrates the full fabric thickness. Produces a permanent set because the wool fibers are plasticized by steam and re-form disulfide bonds in their new configuration as they cool and dry.

## Key Deliverables

- Fulling and napping for wool fabric densification and insulation
- Calendering for smooth, finished surfaces (glazing, embossing, Schreiner)
- Singeing for clean fabric surfaces prior to dyeing
- Bleaching (peroxide and sulfur dioxide) for white base fabric
- Mercerization for improved cotton strength and dye affinity
- Waterproofing (wax, oil, rubber) for outdoor and marine textiles
- Fireproofing treatments (boron salts, phosphate salts) for safety-critical fabrics
- Stentering and heat setting for dimensional stability
- Decating for wool fabric surface setting
- Understanding of finishing sequence and dyeing interactions

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Uneven fulling (patchy density) | Inconsistent agitation or temperature across cloth | Ensure even mechanical action; maintain uniform temperature (40-50°C); rotate cloth regularly during process |
| Fabric yellowing after bleaching | Insufficient rinsing or peroxide residue | Rinse thoroughly after bleaching; neutralize with mild acid rinse (dilute acetic acid); reduce peroxide concentration |
| Mercerization uneven (patchy sheen) | Uneven tension or incomplete caustic penetration | Maintain uniform tension on cloth frame; ensure full immersion in 20-25% NaOH; increase dwell time |
| Waterproofing washing out | Insufficient wax/oil penetration or no heat set | Heat-set wax treatment at 150-170°C; increase number of coating passes; verify fabric is clean before coating |
| Calender glazing uneven | Roll pressure not uniform or fabric moisture inconsistent | Adjust roll pressure across width; dry fabric to uniform moisture before calendering; check roll parallelism |
| Fireproofing ineffective | Inadequate boron/phosphate concentration or insufficient curing | Increase chemical concentration; extend cure time at specified temperature; verify salt penetration into fiber |

## See Also

- [Weaving](weaving.md) — woven cloth as input to finishing
- [Dyeing](dyeing.md) — color processes that interact with finishing
- [Alkalis](../chemistry/alkalis.md) — caustic soda for mercerization and bleaching
- [Rubber](../polymers/rubber.md) — rubber coating for waterproof textiles
- [Fibers](fibers.md) — fiber properties that determine finishing behavior
- [Sewing & Tailoring](sewing-tailoring.md) — finished cloth goes to garment construction

[← Back to Textiles](index.md)
