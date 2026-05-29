# Kiln Firing Protocols

> **Node ID**: ceramics.pottery.kiln-firing
> **Domain**: [Ceramics & Refractories](./index.md)
> **Dependencies**: [`energy.fuels.charcoal`](../energy/charcoal.md), [`ceramics.pottery`](pottery.md)
> **Enables**: [`ceramics.kilns`](kilns.md) (firing validates kiln construction), [`chemistry.refractories`](../chemistry/refractories.md) (refractory brick firing), [`metals.iron-steel`](../metals/iron-steel.md) (refractories enable smelting furnaces)
> **Timeline**: Years 0-10
> **Outputs**: fired_ceramics
> **Critical**: Yes — kiln firing produces refractory ceramics, which enable all high-temperature metallurgy; without fired refractories, no furnace holds molten metal, and no civilization progresses beyond the stone age

Controlled firing transforms clay from a water-soluble mineral mass into a permanent, hardened ceramic. The schedule — ramp rates, peak temperature, hold times, and cooling — determines whether ware survives, vitrifies properly, or cracks. See [kilns.md](./kilns.md) for kiln construction and [pottery.md](./pottery.md) for clay preparation and forming.


Clay is useless without firing. Green (unfired) clay dissolves in water, crumbles under load, and cannot hold liquids. Controlled firing transforms clay into a permanent, hardened ceramic — the first synthetic material humans ever created. But firing is not simply "make it hot." The temperature schedule — ramp rates, soak times, atmosphere, and cooling — determines whether the ware survives, vitrifies properly, or cracks. A kiln is not a bonfire; it is a precision thermal instrument.

Without controlled kiln firing: no refractory bricks (furnaces for smelting, glass melting, and ceramics themselves all require firebrick), no tableware or storage vessels (fired pottery is the first airtight, waterproof container), no electrical insulators (porcelain insulators for power transmission), no crucibles for metal melting, no kiln furniture (shelves and posts that make higher-temperature firing possible). The entire chain from pottery to metallurgy to electronics starts with controlled firing.

Ceramics cannot be welded, machined, or repaired after firing. Every defect formed during the firing cycle is permanent. A cracked kiln load is a total loss — the time and materials invested in forming, drying, and loading are wasted. This is why firing schedules exist: they manage the irreversible physical transformations (dehydration, quartz inversion, sintering, vitrification) that turn clay into ceramic, and they do it without cracking the ware.

## Prerequisites

- **Materials**: [Prepared clay body](./pottery.md) (wedged, de-aired, formed and dried to leather-hard then bone-dry), [glaze materials](./pottery.md) (feldspar, silica, whiting, kaolin, colorant oxides), [fuel](../energy/charcoal.md) (hardwood 20-120 kg per firing, or charcoal 15-40 kg), [kiln furniture](./kilns.md) (cordierite or fireclay shelves, posts, stilts), [pyrometric cones](../glossary/pyrometric-cones.md) (Orton/Seger cones matching target temperature)
- **Tools**: [Kiln](./kilns.md) (wood, charcoal, or gas-fired — updraft, downdraft, or bottle design), [stoking tools](./kilns.md) (firing forks, pokers, dampers), [thermocouple or optical pyrometer](../measurement/index.md) for temperature monitoring, [tongs and heat-resistant gloves](../ehs/ppe.md) for raku and hot kiln access, [loading tools](./kilns.md) (shelf lifters, wadding tongs)
- **Knowledge**: Clay mineralogy (kaolinite decomposition at 450-600°C, quartz inversion at 573°C), glaze chemistry (unity formula, limit formulas, flux-alumina-silica balance), atmosphere control (oxidation vs reduction firing), thermal shock mechanics, fuel management and draft control
- **Infrastructure**: Covered drying area (greenware must dry 1-2 weeks before firing — rain protection essential), fuel storage (seasoned hardwood or charcoal kept dry), kiln shelter (protects kiln and firer from weather), ventilated firing area (CO and SO₂ from fuel and clay — outdoor firing or forced ventilation)

## Bill of Materials — Stoneware Glaze Firing (0.5 m³ kiln)

| Item | Specification | Quantity | Notes |
|------|--------------|----------|-------|
| Stoneware greenware (bisqued) | Bone-dry, Cone 06-04 bisque fired | 30-80 pieces | Must be fully dry — 1-2 weeks air drying for thick pieces |
| Glaze | Mixed from raw materials to target unity formula | 2-5 liters (dip consistency, SG 1.4-1.6) | Apply by dipping, pouring, or brushing; leave 3-5 mm bare foot |
| Hardwood fuel | Oak, ash, maple — seasoned, split to 5-10 cm × 30-50 cm | 40-80 kg | Softwood acceptable but burns faster; charcoal (15-25 kg) for more control |
| Pyrometric cones | Orton cone pack: 1 below, target, 1 above | 3-6 cones | Place at top, middle, bottom of kiln |
| Kiln shelves | Cordierite or fireclay, 30×30 cm to 40×40 cm | 3-5 shelves | Must be flat — warped shelves cause pieces to slide |
| Kiln posts | Fireclay or cordierite, 5-15 cm tall | 12-20 posts | Support shelves at even height |
| Stilts (for glazed ware) | Metal or clay, 3-point | As needed | Prevent glazed base from sticking to shelf |
| Kiln wash | Alumina hydrate + kaolin (50:50) slurry | Applied to shelves | Prevents glaze drips from bonding to shelves; reapply every 3-5 firings |

## Temperature Indicators

Without pyrometric instruments, fire by visual observation of kiln interior glow:

- **Dark red / barely visible glow**: ~525-550°C
- **Dark cherry red**: ~650-700°C
- **Cherry red**: ~800°C
- **Bright cherry / light red**: ~900°C
- **Orange**: ~950-1050°C
- **Dark yellow**: ~1050-1150°C
- **Light yellow**: ~1200°C
- **White (dazzling)**: ~1300-1400°C+

**[Pyrometric cones](../glossary/pyrometric-cones.md)** (Orton/Seger system) provide more precise temperature measurement. Cones are small pyramids of calibrated ceramic composition that soften and slump at a known temperature when heated at a standard rate (150°C/hour):

- **Cone 022**: ~600°C (very low-fire, decorative lusters)
- **Cone 08**: ~945°C (low bisque for earthenware)
- **Cone 06**: ~999°C (standard earthenware bisque)
- **Cone 04**: ~1060°C (earthenware glaze fire)
- **Cone 02**: ~1100°C (mid-range earthenware)
- **Cone 4**: ~1186°C (mid-temperature stoneware)
- **Cone 6**: ~1222°C (standard stoneware glaze fire)
- **Cone 8**: ~1252°C (high stoneware)
- **Cone 10**: ~1285°C (high-fire stoneware and porcelain)

Place cone packs at multiple levels inside the kiln. Read through spy holes — when the cone tip bends to touch the shelf, target temperature is reached.

## Firing Atmospheres

- **Oxidation**: Excess air in kiln. Clean flame, clear exhaust. Iron oxides remain Fe₂O₃ (red/orange). Standard for earthenware, most glazes, and refractory firing.
- **Reduction**: Restricted air (partially close dampers, add wet fuel). Oxygen-starved flame seeks oxygen from iron and copper in the clay and glaze. Iron converts to FeO (produces celadon greens, tenmoku blacks). Copper converts to Cu₂O (produces copper reds). Requires experience — over-reduction causes bloating, carbon coring, and weak ware.
- **Neutral**: Balanced air. Difficult to maintain consistently. Not deliberately targeted in early firing.

## Bisque Firing (800-900°C)

Bisque firing converts unfired (green) clay to a porous, permanent ceramic body. Bisqued ware is strong enough to handle but porous enough to absorb glaze.

**Target**: Cone 06-08 (~945-999°C) for earthenware; Cone 04-02 (~1060-1100°C) for stoneware bisque.

**Schedule**:
1. **[Candle / water-smoke phase](../glossary/candle-water-smoke-phase.md)** (ambient → 150°C): Ramp ~60°C/hour. Hold 1-2 hours. Drives off residual mechanical water. Rapid heating causes steam explosions. Ware may audibly "pop" if rushed.
2. **[Slow ramp](../glossary/slow-ramp.md)** (150-600°C): Ramp ~100°C/hour. Chemically combined water evaporates (clay minerals dehydrate ~450-600°C). Organic matter (temper debris, carbon) begins burning out. Smoke from chimney is normal.
3. **[Quartz inversion](../glossary/quartz-inversion.md)** (~573°C): Pass through this zone at ≤100°C/hour. α-β quartz inversion causes sudden 0.8% volume expansion. Rapid temperature change through this zone cracks ware.
4. **[Fast ramp](../glossary/fast-ramp.md)** (600°C → peak): Ramp ~150°C/hour. Organic burnout completes. Clay minerals begin to decompose and sinter.
5. **Soak at peak**: Hold 20-30 minutes. Ensures even temperature throughout kiln. Cone should bend to 3 o'clock position.
6. **Cooling**: Close all dampers and vents. Cool naturally (do not open kiln). 4-8 hours for small kilns, 12-24 hours for large. Rapid cooling through quartz inversion (~573°C) causes dunting (cracking).

## Glaze Firing (1000-1300°C)

Glaze firing melts the applied glaze into a glassy coating and completes vitrification of the clay body.

**[Earthenware glaze fire](../glossary/earthenware-glaze-fire.md)** (target Cone 04-02, ~1060-1100°C):
1. Ramp 100°C/hour to 600°C
2. Ramp 150°C/hour to peak (~1060°C)
3. Soak 10-15 minutes
4. Cool naturally, 6-12 hours

**[Stoneware glaze fire](../glossary/stoneware-glaze-fire.md)** (target Cone 6-10, ~1222-1285°C):
1. Ramp 100°C/hour to 600°C (water smoke + quartz inversion care)
2. Ramp 150-200°C/hour to 1100°C
3. Ramp 100°C/hour to peak (e.g., Cone 6 = 1222°C)
4. Soak 15-20 minutes at peak
5. Controlled cool: 100°C/hour through 600°C zone, then natural cool
6. Total firing time: 8-14 hours depending on kiln size

**Key precautions**:
- Do not stack glazed pieces touching each other — they will fuse together. Use kiln furniture (stilts, shelves, posts).
- Glaze runs on vertical surfaces — leave 3-5 mm bare foot at base. Wipe glaze off bottom before loading.
- Vent kiln during first 400°C of glaze fire to allow sulfur and carbon gases to escape (prevents glaze defects: pinholing, blisters, crawling).

## Refractory Firing (1200-1400°C+)

Refractory ceramics (firebrick, kiln furniture, crucibles) require high temperatures to achieve the dense, heat-resistant structure needed for furnace construction.

**Target**: Cone 8-12 (~1252-1325°C) for fireclay refractories; 1400-1600°C for high-alumina and specialty refractories.

**Schedule for fireclay brick**:
1. Ramp 50°C/hour to 200°C (very slow — refractory pieces are thick and dense)
2. Ramp 80°C/hour to 600°C (quartz inversion zone — must be gradual)
3. Ramp 100°C/hour to peak (~1300-1400°C)
4. Soak 1-2 hours at peak (ensures complete vitrification throughout thick sections)
5. Cool at 50°C/hour to 600°C, then natural cool. Total cycle: 24-48 hours including cooling.

**[High-alumina refractories](../glossary/high-alumina-refractories.md)** (1500-1700°C):
1. Ramp 30-50°C/hour to 200°C
2. Ramp 60-80°C/hour to 1000°C
3. Ramp 100°C/hour to peak
4. Soak 2-4 hours (mullite formation requires extended hold above 1400°C)
5. Controlled cool at 30-50°C/hour through 600°C

## Cooling Protocols

Cooling is as critical as heating. All ceramics undergo a reverse quartz inversion (~573°C on cooling) where the crystal structure contracts. Key rules:

- **Never open a hot kiln**: Below ~200°C only. Opening above 300°C causes thermal shock and cracking.
- **Slow cool through 650-500°C**: The quartz inversion zone. Large or thick pieces are most vulnerable. Close all dampers and let the kiln cool by its own thermal mass.
- **Crack prevention**: Even wall thickness, proper drying before firing, and controlled cooling eliminate 90%+ of firing failures.
- **Crazing vs. shivering**: If glaze cools with fine crackle lines (crazing), the glaze contracts more than the body — adjust glaze recipe (increase silica, decrease flux). If glaze flakes off (shivering), the body contracts more — decrease silica in glaze or increase in body.

## Safety & Hazards

- **Thermal burns (600-1700°C)**: Kiln interiors reach extreme temperatures during all firing cycles. Wear heat-resistant gloves (leather or Kevlar) and a face shield when loading, adjusting dampers, or checking cones through spy holes. Assume all kiln surfaces are hot until confirmed otherwise.
- **Thermal shock cracking**: Rapid temperature changes through the quartz inversion zone (~573°C) cause catastrophic cracking of ware and kiln furniture. Follow controlled heating and cooling schedules strictly — never rush the ramp through 500-650°C.
- **Kiln gases (CO, SO₂, fluorine)**: Fuel-burning kilns produce carbon monoxide — odorless, colorless, and lethal at sustained concentrations above 400 ppm. Sulfur-bearing clays and glazes release SO₂ (respiratory irritant). Some clays release fluorine compounds. Fire kilns in well-ventilated spaces or outdoors; never in enclosed unventilated rooms. A CO detector near the firing area is strongly recommended.
- **Kiln structural failure**: Poorly constructed kilns (inadequate mortar, insufficient wall thickness, missing expansion joints) can collapse under thermal cycling. Inspect kiln structure before each firing campaign. Never stand on or lean against a kiln during firing.
- **Steam explosions from greenware**: Incompletely dried clay contains residual mechanical water. If heated too rapidly during the water-smoke phase (ambient → 150°C), trapped water flashes to steam and violently shatters the piece — potentially ejecting sharp ceramic fragments. Ensure greenware is fully air-dried (1-2 weeks minimum for thick pieces) before loading, and never skip the slow candle phase.

## Detailed Firing Schedules by Ware Type

**[Earthenware bisque](../glossary/earthenware-bisque.md)** (Cone 06-04, 980-1000°C):
- Total firing time: 6-8 hours. Fuel: 15-30 kg hardwood.
- Ramp: 60°C/hr to 150°C, 100°C/hr to 600°C, 150°C/hr to peak. Soak 20 min.
- This is the most forgiving schedule. Earthenware bodies have wide vitrification ranges and tolerate imprecise temperature control. Target a temperature where the body rings when tapped (not a dull thud) but remains porous enough to absorb glaze.

**[Stoneware bisque](../glossary/stoneware-bisque.md)** (Cone 08-06, 950-1000°C):
- Total firing time: 8-10 hours. Fuel: 25-50 kg hardwood.
- Ramp: 50°C/hr to 200°C, 80°C/hr to 600°C, 120°C/hr to peak. Soak 30 min.
- Bisque to a lower temperature than the final glaze fire. This leaves the body porous for glaze absorption while still developing enough strength to survive handling and glaze application without chipping.

**[Stoneware glaze fire](../glossary/stoneware-glaze-fire.md)** (Cone 8-10, 1220-1280°C):
- Total firing time: 10-14 hours. Fuel: 40-80 kg hardwood (or 15-25 kg charcoal for more controllable heat). 30-minute soak at peak temperature is critical for glaze maturation and body vitrification.
- Ramp: 60°C/hr to 200°C, 100°C/hr to 600°C, 150°C/hr to 1100°C, 100°C/hr to peak. Soak 30 min.
- Reduction firing: Begin reducing at 1000°C by dampering down (restricting air intake). The kiln atmosphere shifts from clear exhaust to smoky. Maintain reduction through peak. Reduction affects glaze color dramatically: iron-bearing glazes turn celadon green or tenmoku black instead of amber brown.

**[Porcelain](../glossary/porcelain.md)** (Cone 10-12, 1280-1300°C):
- Total firing time: 12-16 hours. Fuel: 60-120 kg hardwood or 25-40 kg charcoal.
- Ramp: 40°C/hr to 200°C, 60°C/hr to 600°C, 100°C/hr to 1100°C, 80°C/hr to peak. Soak 45-60 min.
- Porcelain demands the most precise temperature control. Under-firing leaves the body opaque and porous. Over-firing causes bloating, slumping, and warping. The body vitrifies within a narrow range of ~30°C. Pyrometric cones are essential — do not fire porcelain by visual estimate alone.

## Glaze Chemistry

**[Unity formula](../glossary/unity-formula.md)** (Seger formula): The standard method for expressing glaze composition. Recalculates raw material percentages into molar ratios of three component groups: fluxes (RO/R₂O), alumina (Al₂O₃), and silica (SiO₂). The flux sum is normalized to 1.0. This allows direct comparison of glazes regardless of which raw materials supply the oxides.

**[Limit formulas](../glossary/limit-formulas.md)** per temperature range define the safe working zone for glaze composition:
- **Earthenware (Cone 06-04)**: Flux 1.0, Al₂O₃ 0.1-0.4, SiO₂ 1.5-3.0. Low alumina and silica because the glaze must melt at relatively low temperature. Leaching risk if silica is too low (glaze dissolves slowly in acidic liquids).
- **Stoneware (Cone 8-10)**: Flux 1.0, Al₂O₃ 0.3-0.7, SiO₂ 3.0-6.0. Higher alumina and silica create a more viscous, durable melt. Well-formulated stoneware glazes resist scratching and chemical attack.
- **Porcelain (Cone 10-12)**: Flux 1.0, Al₂O₃ 0.4-0.8, SiO₂ 4.0-8.0. The highest silica levels produce a hard, glassy surface. The high firing temperature ensures complete melting even with these refractory proportions.

## Glaze Defects and Corrections

**Crawling**: Glaze pulls back from the surface during firing, leaving bare patches. Causes: glaze applied too thick, dusty or oily bisque surface, glaze shrinkage too high during drying. Fix: thin the glaze (lower SG to 1.3-1.4), clean bisque with a damp sponge before glazing, ensure bisque is fully fired (underfired bisque is dusty).

**Pinholing**: Small holes in the glaze surface where gas bubbles formed and burst but the glaze was too viscous to heal. Causes: trapped gas from decomposing impurities in the body, glaze applied over dusty bisque, firing too fast through the glaze maturation range. Fix: fire slower through the final 100°C to peak, extend the soak time, ensure bisque is clean and fully fired.

**Crazing**: Fine network of crackle lines in the glaze after cooling. The glaze has a higher thermal expansion coefficient than the body, so it contracts more on cooling and cracks. Fix: increase silica in the glaze recipe (lowers thermal expansion), decrease feldspar, or add a small amount of boron (B₂O₃ acts as a flux that also reduces expansion). Crazing weakens the glaze-body bond and allows moisture penetration, though it is sometimes desirable as a decorative effect.

**Shivering**: Glaze flakes off the body in chips. Opposite of crazing — the body contracts more than the glaze on cooling, putting the glaze in compression until it pops off. Fix: decrease silica in the glaze, or increase it in the body. Also check that the glaze is not applied too thick.

## Troubleshooting — Firing Problems

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Ware cracked during bisque firing | Too-fast ramp through quartz inversion (573°C); insufficient drying before firing; uneven wall thickness | Ramp ≤100°C/hr through 500-650°C zone; dry greenware 1-2 weeks minimum; design pieces with uniform wall thickness |
| Kiln temperature uneven (top vs bottom >2 cone numbers) | Poor draft; blocked flue; uneven fuel distribution; kiln design flaw | Clear flue and spy holes; distribute fuel evenly across firebox; consider adding a bag wall (baffle) to redirect heat flow; check door and damper seals |
| Kiln won't reach target temperature | Insufficient fuel; wet or green wood; inadequate draft; kiln too heavily loaded | Increase fuel rate; use dry, seasoned hardwood; open dampers to increase draft; reduce ware density for better gas flow |
| Glaze crawling (pulls back from surface in patches) | Glaze applied too thick; dusty or oily bisque surface; high glaze shrinkage during drying | Thin glaze to SG 1.3-1.4; wipe bisque with damp sponge before glazing; bisque fire to proper maturity (underfired bisque is dusty) |
| Glaze pinholing (small holes in glaze surface) | Trapped gas from body impurities; firing too fast through glaze melt range; dusty bisque | Extend soak time 10-15 min at peak; fire slower through final 100°C to peak; ensure bisque is fully fired and clean |
| Glaze running off pieces onto shelves | Glaze applied too thick; glaze formula too fluid at peak temperature; over-fired (cone past target) | Apply thinner glaze coat; increase alumina in glaze recipe; watch cones carefully — stop firing when target cone bends |
| Ware bloated or blistered | Over-firing (temperature exceeded); reduction too heavy (carbon trapped in body); sulfates or organics not burned out | Fire to correct cone (do not overshoot); reduce only above 1000°C; ensure bisque firing burned out all organics (good ventilation below 600°C) |
| Dunting (cracks appearing after cooling) | Too-fast cooling through quartz inversion zone on cooling (~573°C); kiln opened while too hot | Close all dampers during cooling; never open kiln below 200°C; slow cool through 500-650°C zone (50-100°C/hr) |
| Kiln shelves stuck to ware | Glaze ran onto shelf; missing or worn kiln wash; stilts failed | Apply fresh kiln wash (alumina-kaolin) to shelves before each firing; use stilts for fully glazed pieces; leave 3-5 mm bare foot on all pieces |
| Refractory cracking in kiln structure | Thermal cycling; inadequate expansion joints; moisture in refractory before first firing | Add expansion joints in kiln walls; dry-fire new kiln slowly (first firing: ramp 30°C/hr to peak with no ware); repair cracks with refractory mortar before they propagate |

## Raku Firing

Raku is a rapid, dramatic firing technique that produces unique surface effects:

- **Process**: Heat glazed ware rapidly to 950-1000°C in a small kiln (typically gas-fired, 15-20 minutes to temperature). When the glaze melts and appears glossy, remove the piece with tongs while still glowing hot. Place immediately into a metal container filled with combustible material (sawdust, newspaper, dried leaves). Cover the container. The combustibles ignite from the hot pottery and then smolder in an oxygen-starved atmosphere (post-fire reduction).
- **Effects**: The reduction atmosphere causes metallic lusters, copper flash (metallic red patches from copper glazes), and carbon trapping in the glaze crackle pattern. Unglazed areas turn black from absorbed carbon. Each piece is unique and unpredictable.
- **Safety**: Raku involves handling pottery at 1000°C with tongs. Serious burn risk. Wear full heat protection: Kevlar gloves, face shield, long sleeves. The rapid thermal shock destroys most pots that are not specifically formulated for raku (use a grogged, open body with 20-30% grog to resist thermal shock). Fire outdoors only — the reduction smoke is copious and contains CO. Never use raku-fired vessels for food or drink.

## Kiln Loading Best Practices

How ware is placed in the kiln affects heat distribution, air flow, and the final result:

- **Kiln furniture**: Use stilts, posts, and shelves made from the same refractory material as the kiln lining. Cordierite shelves (thermal shock resistant) are standard for stoneware. For basic operations, fireclay slabs supported on firebrick posts work.
- **Spacing**: Leave 1-2 cm between pieces for hot gas circulation. Pieces placed too close together shield each other from heat, producing underfired spots. Stack bowls and cups using bisque wads (small balls of fired clay, 5-8 mm) at 3 points to separate nesting pieces. Wads leave small scars on the glaze — place them where the mark will not show.
- **Height distribution**: Place large, thick pieces near the bottom of the kiln (hotter zone in an updraft kiln). Place small, thin pieces higher. Glazed pieces must not touch each other or the shelves — fused pieces are total losses.
- **Witness cones**: Place cone packs (3 cones: one below target, one at target, one above) at top, middle, and bottom of the kiln. Read through spy holes during firing to monitor temperature distribution. A difference of more than 2 cone numbers between top and bottom indicates uneven heating — adjust damper settings, fuel distribution, or kiln design.

## Glaze Calculation

Developing a glaze recipe from raw materials requires understanding the unity (Seger) formula:

- **Step 1**: Choose a target unity formula appropriate for the firing temperature and desired surface (glossy, matte, satin). Published limit formulas provide safe starting ranges.
- **Step 2**: Select raw materials to supply each oxide. Common sources: feldspar (K₂O, Na₂O, Al₂O₃, SiO₂), whiting (CaO from CaCO₃), talc (MgO from Mg₃Si₄O₁₀(OH)₂), kaolin (Al₂O₃, SiO₂), silica (SiO₂), and bone ash (Ca₃(PO₄)₂ for calcium phosphate glazes).
- **Step 3**: Calculate the batch recipe by converting the unity formula molar proportions to raw material weights. Use a spreadsheet or glaze calculation software. The calculation iterates: assign each oxide to a raw material, check that the totals match the target formula, adjust.
- **Step 4**: Test fire the glaze on small test tiles (2 × 5 cm bisque tiles dipped in glaze). Evaluate at 3 different temperatures (below, at, and above target) to determine the melting range. Adjust the recipe based on results: too runny → increase alumina; too matte → decrease alumina or increase flux; crawling → thin the glaze or clean the bisque surface.

## Kiln Thermometry

Accurate temperature measurement transforms firing from guesswork into a repeatable process:

**[Pyrometric cones](../glossary/pyrometric-cones.md)** (Seger cones): The most reliable indicator for ceramics firing. Each cone is a small pyramid (25 mm tall) made from a specific ceramic composition calibrated to deform at a known temperature when heated at a standard rate (150°C/hour). The cone bends as it softens: tip bending to 3 o'clock = temperature reached; tip touching the base = temperature exceeded by ~10-15°C. Use three cones per pack: one grade below target, target, and one above. This shows whether the kiln has reached, is at, or has exceeded the desired temperature.

**Thermocouple (Type K)**: Chromel-alumel thermocouple generates a voltage proportional to temperature (41 μV/°C). Read with a millivoltmeter or digital pyrometer. Range: -200°C to +1260°C. Insert the junction into the kiln through a protective ceramic sheath. Thermocouples are more precise than cones but can drift over time (calibrate periodically against cones). Type K is the standard for kiln use. Type S (platinum-rhodium) extends the range to 1450°C for porcelain and refractory firing.

**Optical pyrometer**: Measures temperature by comparing the color of the kiln interior to a calibrated filament. No contact with the kiln required — read from outside through the spy hole. Range: 700-3000°C. Accuracy: ±10-20°C. Good for high-temperature refractory firing where thermocouple life is limited. Requires a clear line of sight to the hot zone.

## Firing Fuel Consumption

Estimating fuel requirements before a firing prevents running out mid-fire:

- **[Wood-fired updraft kiln](../glossary/wood-fired-updraft-kiln.md)** (0.5 m³ chamber): 20-50 kg hardwood per bisque firing, 40-80 kg for stoneware glaze. Softwoods burn faster and produce less heat per kg — use hardwood (oak, ash, maple) for sustained high temperatures.
- **Charcoal-fired kiln**: 15-40 kg for stoneware temperatures. Charcoal burns hotter and cleaner than wood but costs more (wood → charcoal conversion loses 60-70% of the energy content). Charcoal is preferred for reduction firing because the fuel-to-air ratio is easier to control.
- **Gas-fired kiln**: Propane or natural gas. Consumption: 2-5 kg propane per hour for a 0.5 m³ kiln at stoneware temperatures. Gas provides the most precise temperature control and is easiest to regulate for reduction/oxidation atmosphere switching.

## See Also

- [Kilns](kilns.md) — kiln construction, updraft, downdraft, and bottle designs
- [Pottery](pottery.md) — clay preparation, forming, and drying before firing
- [Lime](lime.md) — lime calcination, another kiln-fired process
- [Charcoal](../energy/charcoal.md) — charcoal production for kiln fuel
- [Fuels](../energy/fuels.md) — wood, charcoal, and gas fuels for firing
- [Refractories](../chemistry/refractories.md) — refractory brick and mortar for kiln linings
- [Iron & Steel](../metals/iron-steel.md) — smelting requires refractories produced by kiln firing
- [Measurement](../measurement/index.md) — thermocouples and pyrometers for kiln thermometry
- [PPE](../ehs/ppe.md) — heat-resistant gloves, face shields, and foundry safety equipment
- [Glass: Basic](../glass/basic.md) — glass melting requires kilns with refractory linings
- [Chemistry: Glazes](../chemistry/index.md) — glaze chemistry and raw materials



[← Back to Ceramics & Refractories](index.md)
