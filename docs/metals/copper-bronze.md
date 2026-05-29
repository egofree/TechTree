# Copper & Bronze Production

> **Node ID**: metals.copper-bronze
> **Domain**: [Metallurgy](./index.md)
> **Dependencies**: [`animals.beekeeping`](../animals/beekeeping.md), [`foundations.fire`](../foundations/fire.md), [`mining`](../mining/index.md)
> **Enables**: [`health.medical-instruments`](../health/medical-instruments.md), [`metals.iron-steel`](iron-steel.md), [`metals.non-ferrous`](non-ferrous.md), [`textiles.sewing-tailoring`](../textiles/sewing-tailoring.md)
> **Timeline**: Years 5-10
> **Outputs**: copper, bronze, castings, ingots
> **Critical**: No

## Overview

Copper was the first metal smelted (~5000 BCE) and remains the backbone of electrical infrastructure worldwide. This article covers the full chain: primitive copper smelting from carbonate and sulfide ores, bronze alloying, casting methods, work-hardening, electrolytic refining, brass production, and industrial-scale copper smelting. Copper's combination of conductivity (58.0 MS/m at 20 °C for pure annealed copper), corrosion resistance, and ductility makes it irreplaceable for electrical, marine, and structural applications.

## Prerequisites

- [Fire management](../foundations/fire.md) — controlled combustion for furnace operation
- [Charcoal production](../energy/charcoal.md) — fuel achieving 1100-1300 °C in forced-draft furnaces
- [Mining](../mining/index.md) — ore extraction and beneficiation
- [Beekeeping](../animals/beekeeping.md) — beeswax for lost-wax casting patterns
- [Pottery](../ceramics/pottery.md) — clay working skills for furnace and crucible construction

## Materials

| Material | Specification | Source |
|----------|--------------|--------|
| Malachite ore | Cu₂CO₃(OH)₂, green, 20-57% Cu by mass | [Mining](../mining/extraction.md) |
| Azurite ore | Cu₃(CO₃)₂(OH)₂, blue, 55% Cu by mass | [Mining](../mining/extraction.md) |
| Chalcopyrite ore | CuFeS₂, brass-yellow, 35% Cu by mass | [Mining](../mining/extraction.md) |
| Charcoal | Hardwood, lump grade, >20 mm pieces, >85% fixed carbon | [Charcoal](../energy/charcoal.md) |
| Fire clay | Al₂O₃ content >25%, plasticity index 15-30% | [Ceramics](../ceramics/pottery.md) |
| Tin metal | >95% Sn, from cassiterite (SnO₂) | [Non-ferrous metals](non-ferrous.md) |
| Beeswax | Pure, melting point 62-65 °C | [Beekeeping](../animals/beekeeping.md) |
| Silica sand | >95% SiO₂, grain size 0.1-0.5 mm, for molding | [Mining](../mining/processing.md) |

## Process Description

## 4.1 Copper Smelting

Copper smelting reduces copper oxide ores to metallic copper at temperatures above 1085 °C (copper melting point) in a forced-draft charcoal furnace. Carbonate ores (malachite, azurite) decompose directly to oxide at 300-400 °C, then reduce. Sulfide ores (chalcopyrite) require roasting first.

**Prerequisites**: [charcoal production](../energy/charcoal.md), [fire](../foundations/fire.md), [clay working](../ceramics/pottery.md)

**Materials**: fire clay (Al₂O₃ >25%), sand/grog temper, hardwood charcoal (lump, >20 mm pieces), crushed ore (1-3 cm pieces)

**Ore preparation**:
- **Primary ores**: Malachite (Cu₂CO₃(OH)₂, green), azurite (Cu₃(CO₃)₂(OH)₂, blue), chalcopyrite (CuFeS₂, brass-yellow)
- **Beneficiation**: Hand-sort ore from gangue (waste rock). Crush with stone hammer on stone anvil to 1-3 cm pieces. Wash to remove clay and fines. Roast sulfide ores in open fire (400-600 °C, 4-8 hours) to convert sulfides to oxides and drive off sulfur — essential step for chalcopyrite.
- **[Carbonate ores](../glossary/carbonate-ores.md)** (malachite, azurite) need no roasting — they decompose directly in the furnace.

**Furnace construction (shaft furnace / bloomery-type)**:
1. **Foundation**: Level a dry, fireproof base (stone slab or compacted earth, 60-80 cm diameter ±5 cm).
2. **Walls**: Build clay (fire clay if available) + sand/grog temper in layers 10-15 cm thick. Cylindrical or slightly tapered, 30-60 cm internal diameter ±3 cm, 40-80 cm tall ±5 cm. Wall thickness 10-15 cm ±2 cm. Allow each layer to dry leather-hard before adding the next to prevent wall slump.
3. **Tuyere**: Form a clay tube (2-4 cm bore ±0.5 cm) and insert 10-15 cm above furnace base, angled slightly downward toward the center. Seal around the exterior with clay.
4. **Crucible or hearth**: Form a bowl-shaped depression at furnace base, or make a separate crucible (fired fire clay, 10 cm dia × 12 cm tall ±1 cm) to collect molten copper.
5. **Drying**: Air-dry the furnace 2-5 days, then preheat with a gentle charcoal fire for 15-30 minutes to drive off residual moisture before the first smelt.

**Smelting process**:
1. **Preheat**: Light charcoal in furnace, gentle air blast for 15-30 minutes to dry and preheat walls.
2. **Charge**: Layer crushed ore (2-5 cm depth) and charcoal in alternating layers. Ratio: 3-5 kg charcoal per kg ore.
3. **Increase blast**: Full bellows operation. Temperature rises to 1100-1300 °C. Reaction: 2CuO + C → 2Cu + CO₂ (simplified; actual carbonate ores decompose to oxide first at ~300-400 °C, then reduce).
4. **Duration**: 1-3 hours for small batch (~5-20 kg ore). Maintain charcoal charge throughout.
5. **Tapping or recovery**: Copper collects in crucible/hearth. Break open furnace (destructive for early furnaces) or tilt/tap molten copper into mold. Slag (iron silicate, calcium silicate) floats on top — skim off before pouring.
6. **Yield**: 20-40% copper by weight from good malachite ore. Lower from sulfide ores (8-15%).

**Crucible design**: Clay-graphite crucibles (~60% fire clay + ~40% powdered graphite or charcoal dust) resist thermal shock and last through many heats. Form over a core, dry slowly, fire to harden. A 10 cm dia × 12 cm tall crucible holds ~2-3 kg molten copper. Always preheat crucibles before adding metal — a cold crucible in molten copper may shatter.

**Verification**: Break open a small recovered copper button and examine the fracture surface. Metallic copper shows a distinctive salmon-pink color with no visible gangue inclusions. If the surface is dark, spongy, or contains slag fragments, the furnace did not reach sufficient temperature or the charge ratio was wrong — increase charcoal ratio to 5:1 and extend the blast by 30 minutes.

**Expected performance**: Shaft furnace reaches 1100-1300 °C with forced-draft bellows. Copper recovery: 20-40% of ore mass from carbonate ores, 8-15% from sulfide ores. Furnace lining lasts 3-10 smelts before requiring rebuild.

**Strengths**:
- Achievable with stone-age tools and natural draft or simple bellows
- Carbonate ores (malachite, azurite) require no pre-roasting — single-step process
- Furnace construction uses only clay, sand, and charcoal — no imported materials

**Weaknesses**:
- Furnace must be destroyed (for early shaft designs) or extensively rebuilt after each smelt
- Sulfide ores (chalcopyrite) require a separate roasting step, doubling labor
- Yield is sensitive to charcoal quality and air blast consistency — poor bellows technique wastes fuel

## 4.2 Casting

Molten copper and bronze are poured into molds to produce ingots, tools, and complex shapes. Three mold types serve different purposes; lost-wax casting enables the most intricate forms.

**Prerequisites**: [copper smelting](#41-copper-smelting) (above), [beekeeping](../animals/beekeeping.md) for wax, [clay working](../ceramics/pottery.md)

**Materials**: silica sand (>95% SiO₂, grain 0.1-0.5 mm), fire clay, beeswax (mp 62-65 °C), soapstone or fine-grained stone for reusable molds

**Mold types**:
- **Sand molds**: Fine, damp silica sand packed around wooden pattern. Pattern removed, copper poured into cavity. Good for simple shapes (ingots, flat tools). Withstands single pour.
- **Clay molds**: Fired clay investment around wax model (lost-wax method) or carved directly. More durable, reusable 1-3 times. Better detail than sand.
- **Stone molds**: Carved soapstone or fine-grained stone. Reusable dozens of times. Best for standardized items (axe heads, ingots).
- **Pouring temperature**: 1150-1250 °C (copper melts at 1085 °C, needs superheat for fluidity). Preheat molds to 200-400 °C to prevent thermal shock and improve fill.

**[Lost-wax casting](../glossary/lost-wax-casting.md)** (complex shapes — tools, ornaments):
1. **Wax model**: Sculpt in beeswax or tallow. Attach wax sprue (5-10 mm dia ±2 mm) and vent wires.
2. **Clay investment**: Coat in thin clay slip, build up 2-4 layers of clay + grog (1-3 cm thick ±0.5 cm). Dry thoroughly (2-4 days at ambient temperature).
3. **Burnout**: Heat to 400-600 °C to melt and drain wax. Raise to 800-900 °C to fire clay hard and burn residual wax.
4. **Pour**: Pour molten copper/bronze at 1080-1150 °C into hot mold (improves flow, reduces defects).
5. **Finish**: Cool slowly (2-4 hours), break away investment, cut sprues, file and polish.

**Verification**: Inspect the cast surface for porosity, cold shuts (unfilled areas), and shrinkage cavities. A well-cast bronze tool shows smooth surface finish with no visible gas porosity on the fracture face. Test the mold fill by weighing the casting against the expected volume (copper density: 8.96 g/cm³, bronze: 8.8 g/cm³) — a shortfall >5% indicates incomplete fill.

**Expected performance**: Sand mold: single use, surface finish ~0.5-1 mm roughness. Stone mold: 20-50 pours before mold degrades, best dimensional accuracy ±1 mm. Lost-wax: finest detail (sub-mm features possible), one use per investment.

**Strengths**:
- Stone molds produce identical items repeatedly with tight dimensional control (±1 mm)
- Lost-wax casting enables complex, undercut shapes impossible with two-part molds
- Casting eliminates the labor of hammering each tool to shape from raw stock

**Weaknesses**:
- Pouring at >1100 °C into cold or damp molds causes violent steam explosions
- Shrinkage on solidification (copper shrinks ~2%) can cause internal cavities in thick sections
- Sand molds are single-use; lost-wax investment is destroyed per casting — high material consumption

## 4.3 Work-Hardening & Annealing

Pure copper in annealed state is ~50 Vickers hardness — too soft for tools. Cold hammering work-hardens it to ~150 HV (comparable to mild steel) but reduces ductility. Heavily work-hardened copper cracks if bent further.

**[Annealing](../glossary/annealing.md)** (restores ductility): Heat to 400-650 °C (dull to cherry red), hold 30-60 min. Cool in air or quench — unlike steel, quenching does not harden copper. The work-harden → anneal cycle repeats indefinitely.

**[Temperature estimation by color](../glossary/temperature-estimation-by-color.md)** (no instruments): Dark red ~550 °C, cherry red ~650 °C, bright cherry ~750 °C, dark orange ~850 °C, orange ~950 °C, light yellow ~1050 °C, white ~1150 °C+.

**Verification**: Test hardness by pressing a steel file against the workpiece. Annealed copper yields to the file (cuts easily); work-hardened copper at ~150 HV resists the file (slides without cutting). Compare to known reference: a copper coin (annealed) vs. a hammered copper chisel edge.

**Expected performance**: Annealed pure copper: ~50 HV, elongation 50-60%. Cold-worked (50% reduction): ~130-150 HV, elongation 2-5%. The anneal cycle restores >90% of original ductility.

**Strengths**:
- Annealing temperature (400-650 °C) is well below the melting point — low risk of accidentally melting the workpiece
- Work-harden → anneal cycle can repeat indefinitely without cumulative degradation
- No special tools required beyond a heat source and hammer

**Weaknesses**:
- Repeated heating oxidizes the surface, requiring pickling (acid bath) or filing to remove scale
- Temperature estimation by eye has ±50 °C uncertainty at the 400-650 °C range
- Over-annealing grain growth at >700 °C reduces subsequent work-hardening response

## 4.4 Forging & Forming Copper

Copper and bronze can be hot-forged like [iron and steel](iron-steel.md), but at lower temperatures.

**Prerequisites**: [copper smelting](#41-copper-smelting), [fire](../foundations/fire.md), anvil (stone or iron)

**Materials**: copper or bronze billets, charcoal forge, anvil (hardened steel or stone), hammers (1-3 kg cross-peen and ball-peen)

**Hot forging**:
- Heat billet to 700-900 °C (dark orange range). Copper is very malleable at this temperature.
- **Drawing out**: Hammer along the length to stretch and thin the stock. Rotate 90° between passes to keep section roughly square.
- **Upsetting**: Heat end, stand vertically on anvil, hammer the top to thicken and shorten.
- **Bending**: Hot copper bends easily over anvil edge or in a forked fixture. For sharp bends, use a bending jig.

**Wire and sheet production**:
- **Wire**: Start with a square rod (~1 cm section ±2 mm). Swage (hammer) corners down to round. Anneal. Draw through successively smaller holes in a steel or hardened bronze draw plate. Anneal every 2-3 passes. Target: wire down to 1-2 mm diameter for electrical use.
- **Sheet**: Begin with a thick slab. Hammer flat with overlapping blows, working from center outward. Anneal frequently (every few minutes of hammering). Target: sheet of 0.5-2 mm thickness ±0.2 mm. Thinner sheet requires more annealing cycles. Support on a flat anvil or stake while planishing (smooth hammering for flat, uniform surface).

**Verification**: Measure wire diameter with a notch gauge (notches cut at 0.5 mm intervals in a steel plate). Sheet thickness: check with a caliper or by flexing — 0.5 mm copper sheet flexes easily by hand; 2 mm sheet resists bending. Confirm absence of cracks by bending a sample 90° and back — cracking indicates insufficient annealing.

**Expected performance**: Wire drawing reduces diameter by 15-25% per pass. Drawing force: F = σᵧ × A × ln(A₀/A₁), where σᵧ is yield stress (~200 MPa for half-hard copper). Sheet planishing achieves ±0.2 mm thickness uniformity over a 200 mm span.

**Strengths**:
- Copper forgings at 700-900 °C require less force than iron at equivalent temperature (lower yield stress)
- Wire drawing produces continuous lengths with consistent cross-section
- Sheet forming enables lightweight containers, sheathing, and heat exchanger surfaces

**Weaknesses**:
- Copper work-hardens faster than iron — requires more frequent annealing cycles
- Wire drawing below 1 mm diameter needs a precision draw plate and careful tension control (breakage rate increases)
- Sheet thinner than 0.5 mm tears during planishing if annealing is insufficient

## 4.5 Bronze Alloying

Adding tin to copper produces bronze: harder, lower melting point (~950 °C for 10% tin), better castability (flows into fine mold details), and more corrosion-resistant than pure copper.

**Prerequisites**: [copper smelting](#41-copper-smelting), [tin metal](non-ferrous.md) (from cassiterite SnO₂)

**Materials**: copper ingots (>99% Cu), tin metal (>95% Sn, from cassiterite), clay-graphite crucible, green stick for stirring

**Alloy composition**: 88-95% copper + 5-12% tin. 10% tin is standard "classic" bronze. More tin = harder but more brittle.

| Property | 5% Sn bronze | 10% Sn bronze | 12% Sn bronze |
|----------|-------------|--------------|--------------|
| Melting range | 1020-1060 °C | 920-950 °C | 880-920 °C |
| Hardness (as-cast) | 80-100 HV | 120-150 HV | 150-180 HV |
| Tensile strength | 220-260 MPa | 280-340 MPa | 260-300 MPa (brittle) |
| Elongation | 15-25% | 5-15% | 1-5% |
| Density | 8.8 g/cm³ | 8.8 g/cm³ | 8.7 g/cm³ |

**Process**:
1. Melt copper in crucible (reaches ~1100 °C).
2. Add tin metal (melts at 232 °C, dissolves rapidly in molten copper). Stir with green stick (reduces oxide formation).
3. Skim dross (oxides) from surface.
4. Pour into preheated mold immediately — bronze fluidity degrades with time as it oxidizes.

**Verification**: Break a small test button from the pour. Fracture surface of 10% tin bronze is fine-grained and grey-pink. A coarse, crystalline fracture indicates excessive tin or contamination. Weigh the test button to check density (8.8 g/cm³ ±0.1 for 10% Sn) — low density indicates gas porosity.

**Expected performance**: 10% tin bronze casts at 950-1050 °C, flows into mold features down to 1 mm width. Hardness: 120-150 HV as-cast, work-hardens to 200-250 HV. Corrosion rate in seawater: <0.025 mm/year.

**Tin sourcing challenge**: Cassiterite (SnO₂) is geologically rare. If unavailable locally, copper-only tools (softer, need frequent work-hardening by hammering) or arsenical bronze (copper + arsenic-bearing ores, ~1-5% As — effective but toxic during smelting) are alternatives. See [non-ferrous metal production](non-ferrous.md) for tin smelting.

**Strengths**:
- Lower melting point than pure copper — easier to melt with charcoal furnaces
- Superior castability — flows into fine mold details that pure copper cannot fill
- Harder and more corrosion-resistant than pure copper — better for tools and marine hardware

**Weaknesses**:
- Tin (cassiterite) is geologically rare — many regions lack local tin deposits entirely
- Arsenical bronze alternative is toxic during smelting (arsenic trioxide fumes)
- High-tin bronzes (>10% Sn) become brittle — limited working range

## 4.6 Electrolytic Copper Refining

Fire-refined ("tough pitch") copper is ~99.5% pure — adequate for structural and decorative use but insufficient for electrical conductivity. Electrolytic refining produces 99.99% Cu by dissolving impure anodes and plating pure copper onto cathodes.

**Prerequisites**: [electricity](../energy/electricity.md), [sulfuric acid](../chemistry/acids.md), [fire refining](#49-industrial-copper-smelting) (anode production)

**Materials**: impure copper anodes (99.0-99.5% Cu, 250-400 kg each), pure copper starter sheets (~1 mm thick), CuSO₄·5H₂O (35-50 g/L Cu²⁺), H₂SO₄ (150-220 g/L), DC power supply (0.25-0.40 V per cell)

**Principle**: An impure copper anode and a pure copper starter sheet (cathode) are immersed in an acidic copper sulfate electrolyte. Applied DC potential (~0.3 V per cell) oxidizes copper at the anode (Cu → Cu²⁺ + 2e⁻) and reduces it at the cathode (Cu²⁺ + 2e⁻ → Cu). Metals less noble than copper (Fe, Ni, Zn, Pb) dissolve into the electrolyte but do not plate out at 0.3 V. Metals more noble (Ag, Au, Pt, Pd) do not dissolve and fall to the tank bottom as **anode slime**.

**Electrolyte**: CuSO₄·5H₂O (35-50 g/L Cu²⁺) + H₂SO₄ (150-220 g/L) in water. Sulfuric acid increases conductivity and prevents CuSO₄ hydrolysis. Operating temperature: 50-65 °C (reduces electrolyte resistance, improves ion migration). Continuous filtration removes suspended solids.

**Operating parameters**:

| Parameter | Value | Unit |
|-----------|-------|------|
| Current density | 200-300 | A/m² of cathode surface |
| Cell voltage | 0.25-0.40 | V per cell |
| Energy consumption | 250-350 | kWh per tonne refined Cu |
| Cathode cycle | 7-14 | days per harvest |
| Cathode mass at harvest | 100-150 | kg |
| Anode life | 21-28 | days |
| Electrode spacing | 80-120 | mm center-to-center |
| Electrolyte temperature | 50-65 | °C |

**Tankhouse design**: Rows of concrete or polymer-lined tanks, each ~4-5 m long × 1 m wide × 1.3-1.5 m deep. Each tank holds 30-50 anode-cathode pairs interleaved at 80-120 mm spacing. Tanks are connected electrically in series; electrodes within a tank are in parallel. A tankhouse processing 200,000 tonnes/year copper operates 500-1,000 cells.

**Anode slime recovery**: Slime accumulates at tank bottoms (0.2-0.8% of anode mass). Typical composition: 10-30% Ag, 0.5-2% Au, trace Pt, Pd, Se, Te. Slime is collected, roasted, leached, and electrolytically refined to recover [precious metals](precious-metals.md) — a critical economic co-product that often pays for the entire refining operation. A smelter processing 1 million tonnes of copper anode per year recovers ~3,000 tonnes of silver and ~30 tonnes of gold from anode slime.

**Purity verification**: Refined cathode copper tests at 99.99% Cu minimum. Electrical conductivity: ≥101% IACS (International Annealed Copper Standard). Impurity limits (ppm by weight): Ag <25, As <5, Bi <1, Fe <10, Ni <10, Pb <5, S <15, Se <2, Te <2, Sb <4. Bismuth is the most damaging trace impurity — even 2-3 ppm Bi causes hot shortness (intergranular cracking during hot rolling) by segregating to grain boundaries.

**Starter sheet preparation**: Thin copper sheets (~1 mm thick) serve as cathode starter sheets. Produced by stripping the deposited copper from titanium or stainless steel blank cathodes after a short (12-24 hour) plating cycle, or by rolling strip stock to gauge. Starter sheet dimensions match anode dimensions. Mechanically straightened and masked at the top edge to prevent edge growth bridging to adjacent anodes.

**Verification procedure**:
1. Test cathode conductivity: measure resistivity of a 100 mm strip — must be ≤1.7241 μΩ·cm (101% IACS).
2. Spectrographic analysis: Ag <25 ppm, Bi <1 ppm, Pb <5 ppm (send sample to lab or use portable XRF).
3. Visual: cathode surface should be smooth, dense, and free of nodules or dendritic growth (indicates excessive current density).

**Expected performance**: 99.99% Cu purity at ≥101% IACS conductivity. Energy consumption: 250-350 kWh per tonne. Anode slime recovery: 0.2-0.8% of anode mass as precious metal-bearing slime.

**Strengths**:
- Produces 99.99% Cu — the purity required for electrical conductors
- Recovers precious metals (Au, Ag) from anode slime as a high-value co-product
- Process is self-sustaining once running — anode dissolution and cathode deposition balance

**Weaknesses**:
- Requires continuous DC power and sulfuric acid — not feasible at primitive technology levels
- Tankhouse is capital-intensive (500-1,000 cells for a 200 kt/yr plant)
- Electrolyte management (temperature, filtration, impurity buildup) requires constant attention

## 4.7 Brass Production

Brass is a copper-zinc alloy. Zinc lowers melting point, increases ductility, and produces a gold-colored alloy valued for decorative, mechanical, and marine applications. Unlike bronze (Cu-Sn), brass is easier to cast, more malleable at room temperature, and has superior machinability — but lower hardness and less corrosion resistance in seawater.

**Prerequisites**: [copper smelting](#41-copper-smelting), [zinc metal](non-ferrous.md) or calamine (zinc carbonate)

**Materials**: copper ingots, zinc metal or calamine (ZnCO₃/ZnO), charcoal (reducing cover), clay-graphite crucible

**Common compositions**:
- **[Yellow brass](../glossary/yellow-brass.md)** (60% Cu / 40% Zn): Melting range 880-920 °C. Tensile strength ~340 MPa (as-cast). Good castability, moderate strength, golden color. Used for fittings, valves, hardware, decorative castings.
- **[Cartridge brass](../glossary/cartridge-brass.md)** (70% Cu / 30% Zn): Melting range 915-955 °C. Tensile strength ~320 MPa (annealed), up to 520 MPa (work-hardened). Excellent deep-drawing capability — the standard alloy for ammunition casings, radiator cores, lamp fixtures. Up to 70% cold reduction before annealing required.
- **[Muntz metal](../glossary/muntz-metal.md)** (60% Cu / 40% Zn with trace Fe): Hot-workable, used for structural bolts, condenser tubes.
- **[Admiralty brass](../glossary/admiralty-brass.md)** (70% Cu / 29% Zn / 1% Sn): Tin addition improves seawater corrosion resistance. Condenser and heat-exchanger tubing.
- **[Free-cutting brass](../glossary/free-cutting-brass.md)** (61.5% Cu / 35.5% Zn / 3% Pb): Lead particles act as chip breakers during machining. Machining speed 3-5× higher than plain brass.

**[Calamine cementation process](../glossary/calamine-cementation-process.md)** (pre-industrial): Before metallic zinc was available (zinc boils at 907 °C, below its melting point of 419 °C, making it difficult to produce as a free metal), brass was made by cementation. Ground calamine (zinc carbonate, ZnCO₃, or zinc oxide, ZnO) is mixed with crushed charcoal and heated with molten copper in a closed crucible at 900-1000 °C. Carbon reduces the calamine to zinc vapor, which dissolves directly into the molten copper. Repeated charges of calamine increase zinc content to ~28-33%. This process cannot exceed ~33% Zn — above this, zinc vapor escapes faster than it dissolves. Yield: ~85-90% of theoretical zinc uptake.

**[Direct zinc alloying](../glossary/direct-zinc-alloying.md)** (post-zinc-smelting): Once metallic zinc is available, brass production simplifies. Melt copper in crucible at ~1100 °C. Add zinc metal (melts at 419 °C, boils at 907 °C). Cover crucible with a lid or charcoal layer to minimize zinc vapor loss (zinc volatility is the primary loss mechanism — 3-8% Zn lost as vapor per melt). Stir with a carbon rod. Pour at 950-1050 °C depending on alloy. Zinc recovery: 92-97%.

**Properties vs. bronze**: Brass (70/30) density 8.5 g/cm³ vs. bronze (90/10) 8.8 g/cm³. Brass tensile strength 320 MPa (annealed) vs. bronze 240-310 MPa. Bronze superior for bearings (lower friction), marine hardware (resists dezincification), and tools (higher hardness after work-hardening). Brass superior for decorative work (gold color, takes polish), musical instruments (acoustic properties), and machined fittings. See [specialty alloys](alloys.md) for detailed alloy design principles.

**Verification**: Weigh a casting of known volume — density should be 8.4-8.5 g/cm³ for 70/30 brass. File test: brass cuts more easily than bronze (softer, gummier chips). Color: brass is distinctly gold-yellow; if the casting is reddish, zinc content is too low.

**Expected performance**: Casting temperature: 950-1050 °C. Zinc loss: 3-8% as vapor per melt. Machinability: 3-5× free-cutting brass vs. plain brass. Tensile strength: 320-520 MPa depending on composition and work-hardening.

**Strengths**:
- Lower melting point than copper or bronze — easier to cast in charcoal furnaces
- Gold-colored appearance — valued for decorative hardware without precious metal cost
- Superior machinability — brass cuts cleanly at high speed with simple tooling

**Weaknesses**:
- Dezincification in seawater — zinc leaches out, leaving weak, porous copper residue
- Zinc vapor is toxic — oxide fumes cause "metal fume fever" (flu-like symptoms)
- Cementation process limited to ~33% Zn — higher-zinc brasses require metallic zinc

## 4.8 Copper for Electrical Use

Copper is the dominant electrical conductor worldwide. Its combination of high conductivity (58.0 MS/m at 20 °C for annealed pure copper), ductility (enables wire drawing to fine gauges), solderability, and moderate cost make it irreplaceable in power generation, transmission, motors, and electronics.

**Prerequisites**: [electrolytic copper refining](#46-electrolytic-copper-refining), [wire drawing](#44-forging--forming-copper), [electricity](../energy/electricity.md)

**Materials**: electrolytic copper cathodes (99.99% Cu), tungsten carbide or diamond drawing dies, soap solution or oil-based lubricant, enamel or insulation materials

**IACS conductivity standard**: The International Annealed Copper Standard defines 100% IACS = 58.0 MS/m (mega-siemens per meter) volumetric electrical conductivity at 20 °C. This corresponds to a resistivity of 1.7241 μΩ·cm. Commercial electrolytic tough-pitch copper (C11000) tests at 100-101% IACS. All copper alloys are rated as percentages of this standard. Phosphorus is a potent conductivity reducer — as little as 0.02% P drops conductivity to ~85% IACS.

**[OFHC copper](../glossary/ofhc-copper.md)** (Oxygen-Free High Conductivity, C10100/C10200): Produced by melting and casting copper under a reducing (CO/N₂) atmosphere or in a vacuum induction furnace, eliminating dissolved oxygen (which forms Cu₂O inclusions in tough-pitch copper). OFHC copper achieves 101% IACS (58.5 MS/m) minimum. Superior ductility, weldability, and hydrogen embrittlement resistance compared to tough-pitch. Essential for vacuum tube components, bus bar for plating cells, and high-reliability electronic connectors. Oxygen content <10 ppm (vs. 200-500 ppm in tough-pitch).

**Wire drawing at scale**:
1. **Rod stock**: Continuously cast and rolled 8-12 mm diameter copper rod (Southwire or Properzi process). Rod is coiled into 2-5 tonne pay-off packs.
2. **Multi-die drawing**: Rod passes through a series of tungsten carbide or diamond drawing dies of decreasing bore diameter. Each die reduces cross-section by 15-25%. Lubrication: soap solution or oil-based drawing compound. A 12-die machine draws 8 mm rod to 1.6 mm wire at ~30 m/s.
3. **Intermediate annealing**: Work-hardened wire is annealed in a continuous strand annealer (resistive heating to 400-600 °C under inert atmosphere) between draw passes. This restores conductivity and ductility. Without annealing, conductivity drops to ~97% IACS due to dislocation scattering.
4. **Fine wire**: Down to 0.05-0.10 mm diameter for winding wire. 20+ draw passes from 8 mm rod. Breakage rate increases below 0.1 mm — precision tension control required.
5. **Yield**: 95-98% of rod mass becomes finished wire (2-5% lost to oxide scale, trimming, breakage).

**Drawing forces and die design**: Draw force F = σᵧ × A × ln(A₀/A₁) where σᵧ is yield stress, A₀ and A₁ are initial and final cross-sectional areas. Approach angle of the die cone: 12-18° (steeper angles increase redundant work, shallower angles increase friction). Bearing length: 0.3-0.8× wire diameter. Die wear rate: 1-5 μm bore enlargement per tonne of wire drawn through tungsten carbide dies; diamond dies last 10-50× longer for fine wire.

**Continuous casting rod systems**: The Southwire process casts 8-12 mm rod continuously through a graphite-coated copper wheel mold, then hot-rolls it through 8-14 rolling stands to final rod diameter. Line speed: 5-15 m/min. Annual output per line: 50,000-200,000 tonnes. The Properzi process uses a rotating ring mold instead of a wheel. Both produce rod with <0.04% oxygen (tough-pitch grade) suitable for direct wire drawing without additional processing.

**Insulation**:
- **Enamel (magnet wire)**: Polyurethane, polyester, or polyimide coatings applied by repeated dipping and curing cycles. Film builds of 0.02-0.10 mm. Polyurethane solderable at 380 °C (no strip needed). Polyimide (class 220, 220 °C continuous rating) for motors and transformers.
- **PVC insulation**: Extruded polyvinyl chloride jacket, rated to 70 °C or 105 °C. General-purpose building wire and cable.
- **XLPE insulation**: Cross-linked polyethylene, rated to 90 °C continuous, 130 °C emergency. Power cable for distribution and transmission.
- **Paper-oil insulation**: Kraft paper tape wound in overlapping layers, vacuum-impregnated with mineral oil. High-voltage cable (up to 500 kV). Obsolescent for new installation but widely installed.

**Major product forms**:
- **Bus bar**: Flat rectangular copper bar (6-12 mm thick × 25-100 mm wide) for low-resistance power distribution in switchgear, plating plants, substations. Carries 500-5,000 A depending on cross-section. Surface-tinned at connections to prevent oxide buildup.
- **Power cable**: Stranded copper conductors (19-127 strands, 1-4 mm each) insulated and sheathed. 1 kV to 500 kV ratings. Underground and submarine applications.
- **Winding wire (magnet wire)**: Round or rectangular enameled copper wire for electric motor stators, transformer coils, generator windings, electromagnets. Sizes from 0.05 mm (AWG 44) to 5 mm (AWG 4). A large power transformer contains 50-200 tonnes of winding wire.

**Verification**: Measure wire resistance with a Kelvin (4-wire) bridge. Resistance per meter at 20 °C for 1 mm² cross-section: 0.01724 Ω/m (corresponds to 100% IACS). Deviation >2% indicates impure copper or insufficient annealing.

**Expected performance**: Conductivity: 58.0-58.5 MS/m (100-101% IACS). Wire drawing: 15-25% area reduction per die pass. Die wear: 1-5 μm/tonne for WC dies. Overall yield: 95-98% from rod to finished wire.

**Strengths**:
- Highest conductivity of any engineering metal (excluding silver, which costs 80× more)
- Ductile enough for wire drawing to 0.05 mm diameter without intermediate annealing
- Solderable, weldable, and recyclable without loss of conductivity

**Weaknesses**:
- Requires 99.99% purity (electrolytic refining) for full conductivity — fire-refined copper is inadequate
- Wire drawing below 0.1 mm diameter has high breakage rates — needs precision tension control
- Copper is dense (8.96 g/cm³) — aluminum is preferred for overhead transmission lines where weight matters

## 4.9 Industrial Copper Smelting

At industrial scale, copper smelting processes sulfide concentrates (20-35% Cu) through a multi-stage pyrometallurgical route: concentrate → matte → blister copper → fire-refined copper → electrolytic copper. Modern smelters process 100,000 to 1,000,000+ tonnes of concentrate per year. See [primary metal forming](forming.md) for downstream processing of refined copper.

**Prerequisites**: [mining and ore processing](../mining/processing.md), [electricity](../energy/electricity.md), [sulfuric acid production](../chemistry/acids.md)

**Materials**: copper sulfide concentrate (20-35% Cu, primarily chalcopyrite CuFeS₂), silica flux, oxygen-enriched air, refractory brick (magnesite-chrome)

**Concentrate preparation**: Mined ore (0.5-2% Cu) is crushed, ground to 50-100 μm, and concentrated by froth flotation to 20-35% Cu as a sulfide concentrate (primarily chalcopyrite CuFeS₂, chalcocite Cu₂S, bornite Cu₅FeS₄). Concentrate is filtered to 8-10% moisture and transported to the smelter.

**[Reverberatory furnace](../glossary/reverberatory-furnace.md)** (traditional, 1900s-1970s): A long, shallow hearth furnace (30 m × 10 m) with a refractory roof. Coal, oil, or gas flame heats the roof, which radiates heat onto the charge. Concentrate + flux (silica sand) fed at one end; matte (Cu-Fe-S melt, 30-45% Cu) and slag (iron silicate) separate by density. Operating temperature: 1500-1600 °C. Off-gas: 1-2% SO₂ — too dilute for acid plant, historically vented (major pollution source). Matte tapped from furnace bottom, slag skimmed. Fuel consumption: 4-6 GJ per tonne of concentrate. Mostly superseded by flash smelting.

**[Flash smelting](../glossary/flash-smelting.md)** (Outokumpu process, dominant since 1970s): Dry concentrate (moisture <0.3%) is blown with preheated air or oxygen-enriched air (30-95% O₂) through a burner into a tall furnace shaft. The sulfide particles ignite and self-roast in flight — the exothermic oxidation of iron sulfides (2FeS + 3O₂ → 2FeO + 2SO₂) supplies 40-70% of the process heat. Matte (50-70% Cu) collects in the furnace hearth; slag (FeO-SiO₂) floats above. Off-gas: 10-30% SO₂ — strong enough for sulfuric acid production (contact process). Oxygen enrichment increases SO₂ concentration and reduces off-gas volume. Capacity: 1,000-3,000 tonnes concentrate/day per furnace. Fuel consumption: 0.5-2 GJ/tonne (far less than reverberatory due to autogenous heat).

**[Peirce-Smith converter](../glossary/peirce-smith-converter.md)** (matte → blister copper): A horizontal cylindrical vessel (3-5 m dia × 9-12 m long), lined with basic refractory (magnesite-chrome), mounted on trunnions for rotation. Molten matte (50-70% Cu) is charged, and air is blown through submerged tuyeres (30-60 mm dia, 40-50 tuyeres along the cylinder length) at 1-2 bar.

Two-stage blow cycle:
1. **Slag blow**: Air oxidizes FeS in the matte to FeO + SO₂. Silica flux added to form fayalite slag (2FeO·SiO₂). Slag is poured off by tilting the converter. Duration: 2-6 hours depending on iron content. This stage removes most iron and sulfur.
2. **Copper blow**: Remaining Cu₂S is oxidized: 2Cu₂S + 3O₂ → 2Cu₂O + 2SO₂, then Cu₂S + 2Cu₂O → 6Cu + SO₂. The product is **[blister copper](../glossary/blister-copper.md)** (98-99% Cu, named for SO₂ blisters trapped during solidification). Duration: 1-3 hours. Temperature: 1150-1250 °C.

**[Fire refining](../glossary/fire-refining.md)** (blister → tough pitch): Blister copper is melted in a reverberatory or rotary anode furnace at 1150-1200 °C. Two stages:
1. **Oxidation**: Air blown through or over the melt oxidizes impurities (Fe, Zn, Pb, Sn) to slag. Some Cu oxidizes to Cu₂O (dissolved oxygen rises to 0.6-0.9%).
2. **Poling**: Green tree trunks (historically) or natural gas/reductant gas bubbled through the melt reduces dissolved Cu₂O back to Cu, lowering oxygen to 0.03-0.05%. "Tough pitch" copper at ~99.5% Cu is cast into anodes (800-1000 mm × 800-1000 mm × 40-50 mm, ~250-400 kg each) for electrolytic refining.

**Sulfuric acid co-production**: Flash smelter and Peirce-Smith converter off-gases are combined, cooled, cleaned (electrostatic precipitators, wet scrubbers), and fed to a double-contact double-absorption (DCDA) sulfuric acid plant. Conversion efficiency: 99.5-99.9% of SO₂ to H₂SO₄. A smelter processing 1 million tonnes/year of 30% Cu concentrate produces ~1.0-1.2 million tonnes of sulfuric acid (100% H₂SO₄ basis). This acid is sold for leaching, fertilizer production, or chemical manufacture — a major revenue stream. Smelters without acid plants cannot operate in jurisdictions with modern emission regulations.

**[Hydrometallurgical alternative](../glossary/hydrometallurgical-alternative.md)** (SX-EW): Oxide ores (malachite, chrysocolla) unsuitable for froth flotation are leached with dilute sulfuric acid (50-100 g/L) in heap or dump leaching operations. Pregnant leach solution (1-6 g/L Cu²⁺) is concentrated by solvent extraction (LIX reagents in kerosene diluent) to 35-50 g/L Cu, then electrowon directly to cathode copper (99.99% Cu) in electrowinning cells at 180-250 A/m² and 1.8-2.2 V per cell. Energy consumption: 2,200-2,800 kWh per tonne Cu (higher than electrorefining due to higher cell voltage). SX-EW accounts for ~15-20% of world copper production, predominantly from Chile and the southwestern United States. No SO₂ emissions — the only pyrometallurgical copper route with inherently zero sulfur gas output.

**Verification**: Blister copper sampled by drilling 3-4 holes per anode, analyzing drillings by XRF or wet chemistry. Target: 98-99% Cu. Electrolytic cathode tested for conductivity (≥101% IACS) and impurity levels (Bi <1 ppm).

**Expected performance**: Flash smelter: 1,000-3,000 tonnes concentrate/day, matte grade 50-70% Cu. Converter: blister copper 98-99% Cu. Fire refining: 99.5% Cu anodes. Overall recovery: 95-98% of copper in concentrate becomes refined cathode.

**Strengths**:
- Flash smelting is largely autogenous — sulfide oxidation supplies 40-70% of process heat
- Sulfuric acid co-product from SO₂ capture pays for a significant portion of operating costs
- SX-EW route avoids all SO₂ emissions — suitable for oxide ore bodies without smelters

**Weaknesses**:
- Massive capital investment (smelter + acid plant + tankhouse: $1-5 billion)
- SO₂ emissions from legacy reverberatory furnaces caused severe environmental damage
- Peirce-Smith converter refractory lining lasts only 6-12 months between rebuilds

## 4.10 Copper-Nickel Alloys

Copper and nickel are fully soluble in each other in all proportions (complete solid solution), enabling a continuous range of alloys with properties tailored between the two elements. Nickel strengthens copper (solid-solution hardening), dramatically improves corrosion resistance (especially in seawater), and modifies electrical resistivity.

**Prerequisites**: [copper refining](#46-electrolytic-copper-refining), [nickel metal](non-ferrous.md), induction furnace

**Materials**: electrolytic copper (99.99% Cu), nickel cathode (>99.9% Ni), manganese (0.5-1% addition), iron (0.5-2% addition), charcoal cover

**Cupronickel (copper-nickel)**: The premier marine alloy family. Nickel content 10-30% with small additions of iron (0.5-2%) and manganese (0.5-1%) for improved impingement corrosion resistance and deoxidation.

- **[90/10 cupronickel](../glossary/9010-cupronickel.md)** (C70600: 88.5% Cu, 10% Ni, 1.5% Fe, 0.5% Mn): Tensile strength ~320 MPa (annealed), ~440 MPa (cold-worked). Excellent resistance to seawater corrosion, biofouling, and stress corrosion cracking. Used for seawater piping, condenser tubes, heat exchangers, desalination plant tubing. Service life: 20-40 years in flowing seawater. Thermal conductivity: 45 W/m·K (vs. 52 for brass, 390 for pure copper).
- **[70/30 cupronickel](../glossary/7030-cupronickel.md)** (C71500: 69% Cu, 30% Ni, 0.7% Fe, 0.5% Mn): Higher strength (~380 MPa annealed, ~520 MPa cold-worked) and superior corrosion resistance in high-velocity seawater (up to 3.5 m/s). Used for naval ship hulls, submarine pipework, offshore platform systems. More expensive (higher Ni content) but lasts longer in severe service. Added chromium (C71900, 30% Ni + 2.8% Cr) for weldability and localized corrosion resistance.

**[Constantan](../glossary/constantan.md)** (55% Cu / 45% Ni, also called Eureka wire, Cupronickel 45): Electrical resistivity ~49 μΩ·cm (vs. 1.7 for pure copper) — among the highest of any copper alloy. Resistivity is nearly constant over a wide temperature range (temperature coefficient of resistance ~±0.00002/°C from 0-100 °C, vs. 0.00393/°C for pure copper). This stability makes constantan the standard resistor alloy for precision instruments, strain gauges, and shunt resistors.

**Thermocouple use**: Type J (iron-constantan, 0-760 °C), Type T (copper-constantan, -200 to 370 °C), and Type E (chromel-constantan, -200 to 900 °C) thermocouples all use constantan as one leg. Seebeck coefficient: ~50-60 μV/°C for Cu-Constantan pair. Calibration tables standardized (NIST ITS-90). Thermocouple wire is drawn to 0.1-1.0 mm diameter, insulated with fiberglass or ceramic fiber. Junction formed by twisting and welding (gas or resistance weld).

**Melting and casting**: Cupronickel alloys melt at 1170-1240 °C (range depends on Ni content). Melted in coreless induction furnaces under charcoal cover to prevent oxidation. Deoxidized with magnesium or lithium before pouring. Cast in graphite or metal molds (permanent mold casting). Nickel increases the tendency for inverse segregation (Ni-enriched surface layer) — controlled by mold preheat (200-400 °C) and moderate pour speed. Hot-working range: 800-950 °C. Cold-working: up to 50% reduction before annealing required (anneal at 650-800 °C).

**[Nickel silver](../glossary/nickel-silver.md)** (German silver, 55-65% Cu / 10-30% Ni / 20-30% Zn): Contains no silver — named for its silvery appearance. Resistivity ~25-30 μΩ·cm. Used for tableware, musical instrument bodies (flutes, saxophones), resistor wire, and decorative hardware. The Zn addition lowers cost and improves castability but reduces seawater corrosion resistance compared to binary cupronickel. Melting range: 960-1120 °C. Density: 8.4-8.7 g/cm³ depending on composition. Machinability rating: 30-40% of free-cutting brass (the Ni content work-hardens rapidly during cutting, increasing tool wear).

**Verification**: Measure alloy density (cupranickel range 8.4-8.9 g/cm³). Test corrosion resistance by salt spray exposure (ASTM B117) — 90/10 cupronickel shows <0.025 mm/year weight loss after 30 days in 3.5% NaCl spray. Thermocouple calibration: compare Type T (Cu-Constantan) readings against a NIST-traceable reference at 0 °C (ice point) and 100 °C (boiling water) — tolerance ±1 °C.

**Expected performance**: 90/10 cupronickel: 320 MPa tensile (annealed), 20-40 year service life in flowing seawater. 70/30 cupronickel: 380 MPa tensile (annealed), withstands 3.5 m/s seawater flow. Constantan: resistivity 49 μΩ·cm, TCR ±0.00002/°C.

**Strengths**:
- Cupronickel resists seawater corrosion, biofouling, and stress corrosion cracking — no other copper alloy family matches its marine performance
- Constantan provides near-zero temperature coefficient of resistance — ideal for precision resistors and thermocouples
- Copper and nickel form a complete solid solution — no brittle intermetallic phases at any ratio

**Weaknesses**:
- Nickel is expensive and geopolitically concentrated (Indonesia, Philippines, Russia supply >50%)
- Cupronickel is difficult to machine (work-hardens rapidly, 30-40% of free-cutting brass machinability)
- Thermocouple wire (constantan) requires calibration against reference standards — not plug-and-play

## Safety & Hazards

- **Molten metal burns**: Copper and bronze melt at 1085-1200 °C and cause devastating deep-tissue burns on skin contact. Molten metal splashes readily when poured into damp or cold molds. Wear heavy leather apron, gauntlet gloves, face shield, and closed-toe boots. Preheat all molds and crucibles to 200-400 °C before contact with molten metal — a cold or damp crucible may shatter violently, spraying molten copper. Never pour molten metal into wet molds; trapped moisture flashes to steam and ejects metal explosively.
- **Toxic fumes from arsenical ores**: Arsenic-bearing copper ores (ennargite Cu₃AsS₄, tennantite Cu₁₂As₄S₁₃) release arsenic trioxide (As₂O₃) vapor during roasting (400-600 °C) and smelting. Arsenic fumes cause nausea, vomiting, abdominal pain, and long-term nerve and organ damage. OSHA PEL for As₂O₃: 0.01 mg/m³ as an 8-hour TWA. Arsenical bronze production (~1-5% As) is particularly hazardous. Smelt in well-ventilated areas or under a hood. Respiratory protection (P100 particulate filter or better) required when roasting sulfide or arsenic-bearing ores. Lead, often present as a trace impurity in copper ores, vaporizes above 500 °C — lead fume inhalation causes cumulative neurological damage. OSHA PEL for Pb: 0.05 mg/m³.
- **Carbon monoxide poisoning**: Charcoal-fueled shaft furnaces produce substantial carbon monoxide (CO), especially during the full-blast smelting phase (1100-1300 °C). CO is odorless, colorless, and causes headache at 100 ppm, dizziness at 200 ppm, confusion at 400 ppm, and death at >1,000 ppm with 1-2 hours exposure. NIOSH IDLH: 1,200 ppm. Never operate furnaces in enclosed spaces. Ensure through-draft ventilation. Operators showing confusion or dizziness should be moved to fresh air immediately.
- **Zinc oxide fume (metal fume fever)**: Brass melting and zinc alloying generate zinc oxide (ZnO) fume when zinc vaporizes at 907 °C and re-oxidizes in air. Inhalation causes "metal fume fever" — flu-like symptoms (chills, fever, muscle aches, metallic taste) beginning 4-8 hours after exposure. OSHA PEL for ZnO fume: 5 mg/m³ as an 8-hour TWA. Prevention: local exhaust ventilation at the crucible, or work upwind of the pour.
- **Slag and spark injuries**: During hot forging and slag skimming, hot slag and metal particles spray out as bright sparks at 700-900 °C. Eye protection (safety glasses rated ANSI Z87.1 or face shield) is essential when hammering hot metal. Slag skimmed from molten copper retains dangerous heat for extended periods — set aside on dry sand or refractory surface, never on combustible material.


[← Back to Metals](index.md)
