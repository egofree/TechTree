# Ore Processing

> **Node ID**: mining.processing
> **Domain**: [Mining](./index.md)
> **Dependencies**: [`energy.fuels`](../energy/fuels.md), [`mining.extraction`](extraction.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 0-20
> **Outputs**: concentrated_ore
> **Critical**: No

### Ore Dressing (processing raw rock to concentrated ore)

**Crushing**:
- **Hand crushing**: Strike ore with hammer on stone anvil. Slow but effective for small quantities.
- **[Stamp mill](../glossary/stamp-mill.md)** (the Metallurgy-Machine Tools stage transition): Vertical iron-shod wooden stamps (50-200 kg each) lifted by cam on rotating shaft, dropped by gravity. 6-12 stamps in battery. Crush ore to 1-5 mm. Water flows through battery, carries fines away. Powered by water wheel. Capacity: 1-5 tonnes/day.
- **[Jaw crusher](../glossary/jaw-crusher.md)** (Machine Tools): Two jaw plates (cast iron or manganese steel), one fixed, one oscillating. Ore fed in top, crushed between jaws. Gap adjustable for output size (10-50 mm). Powered by water wheel or steam engine. 5-50 tonnes/day.

**Classification equipment**:
- **Vibrating screens**: Perforated plate or wire mesh on vibrating frame. Classify crushed ore into size fractions. Inclined deck, eccentric drive mechanism. Screen aperture 1-50 mm. Oversize returns to crusher, undersize proceeds to next stage.
- **Hydrocyclones**: Cone-shaped vessel. Pulp fed tangentially under pressure — centrifugal force throws coarse particles to wall (underflow), fine particles exit center (overflow). Cut point 5-250 μm, adjustable by feed pressure and vortex finder diameter. No moving parts. Compact and high-capacity.
- **Spiral classifiers**: Wide inclined trough with rotating spiral blade. Pulp flows in at lower end. Coarse particles settle and are screw-conveyed uphill (sands product). Fine particles remain suspended and overflow the weir (slimes product). Settling velocity separation by particle size and density.

**Gravity separation**:
- **Hand sorting**: Pick out visible ore pieces from waste rock on picking belt or table. Labor-intensive but effective for coarse ore.
- **Sluicing**: Wash crushed ore through inclined trough with riffles. Heavy ore minerals settle behind riffles, light gangue washes away. For heavy minerals (gold, cassiterite, wolframite).
- **Buddling**: Circular pit with central rotating arm. Crushed ore mixed with water flows inward. Heavy particles settle near center, light particles at periphery. Continuous process.
- **Panning**: Final concentration. Same technique as placer mining.
- **Jig**: Piston-driven water pulsation through a screen bed of ore. Stroke 2-6 mm, 100-300 cycles/min. Upstroke lifts bed, particles settle by specific gravity on downstroke. Heavy ore collects through screen into hutch, light gangue overflows. Suitable for coarse ore 2-20 mm. Recovery 85-95% for dense minerals.

**Flotation**:
- Crush and grind ore to 50-200 μm. Mix with water to form slurry (25-40% solids). Add collector chemicals — xanthates for sulfide minerals (attach to mineral surface, make it hydrophobic). Add frother (pine oil or MIBC) to stabilize bubbles. Inject air — bubbles carry hydrophobic mineral particles to surface, forming mineralized froth. Skim froth as concentrate. Gangue remains in slurry (tailings). Recovery rates 85-95% for sulfide ores (copper, lead, zinc). Requires multiple cleaning stages for high grade. pH control with lime critical for selectivity.

**Leaching methods**:
- **Heap leaching**: Stack crushed ore (5-25 mm) on impermeable pad (clay + plastic membrane). Drip cyanide solution (0.01-0.05% NaCN) for gold, or sulfuric acid for copper oxide ores. Solution percolates through heap over weeks to months. Pregnant solution collected at base. Recovery 70-85%. Low capital cost, slow processing.
- **Tank leaching**: Agitated tanks (pachuca or mechanical agitator) with finely ground ore. Faster kinetics — hours to days vs weeks. Higher recovery 85-90% but more expensive (grinding, tank construction, agitator power). Carbon adsorption (activated carbon) or solvent extraction to recover dissolved metals.

**Magnetic separation**: Magnetite (Fe₃O₄) is naturally magnetic. Pass crushed ore past electromagnet or permanent magnet — magnetic particles deflect, non-magnetic waste continues straight. Effective for iron ore beneficiation.

**Tailings management**:
- Tailings pond: Excavated or dammed basin downstream of processing plant. Fine waste slurry pumped in, solids settle, clarified water decanted and recycled. Dam construction from compacted earth or mine waste — engineered for stability. Water recycling critical — processing uses 2-10 m³ water per tonne ore.
- Environmental: Tailings may contain residual chemicals (cyanide, flotation reagents, heavy metals). Neutralize before discharge — cyanide destroyed by oxidation (hydrogen peroxide or natural UV degradation). Monitor groundwater. Re-vegetate completed tailings areas.

**Strengths**:
- Gravity separation (jigs, sluices) recovers 85-95% of dense minerals with no chemical reagents
- Flotation achieves 85-95% recovery for sulfide ores (copper, lead, zinc) at industrial scale
- Multiple methods (gravity, magnetic, flotation, leaching) can be combined to process complex ores

**Weaknesses**:
- Crushing and grinding consume 50-70% of total plant energy (10-30 kWh/tonne for ball milling alone)
- Flotation requires ongoing reagent supply (xanthates, frothers, lime) that must be manufactured
- Cyanide leaching demands pH >10 at all times — acidic conditions release lethal HCN gas

### Common Ore Flowsheets

- **Copper sulfide**: Crush → grind → flotation (rougher + cleaner stages) → copper concentrate (20-30% Cu) → smelt → blister copper. By-product: molybdenum from Cu-Mo porphyry ores.
- **Iron ore**: Crush → magnetic separation (for magnetite) or gravity concentration (for hematite) → pelletize (roll fines into 10-15 mm balls with bentonite binder, fire at 1250°C) → feed blast furnace.
- **Gold**: Crush → grind → cyanide leach (tank or heap) → carbon adsorption → desorption with hot caustic solution → electrowinning (plate gold onto steel wool cathodes) → smelt to doré bullion.
- **Tin (cassiterite)**: Crush → gravity separation (jigs, sluices) → concentrate (60-70% Sn) → smelt with charcoal at 1200-1300°C.

### Grinding Circuits

**Ball mill**: Rotating cylinder (1-3 m diameter, 2-5 m length) loaded with steel or cast iron balls (25-100 mm diameter). Ore fed at one end, discharged at the other. Rotation speed: 60-80% of critical speed (speed at which centrifugal force holds balls against shell — calculated as 42.3/√D RPM where D = diameter in meters). Impact and attrition grind ore to 50-200 μm. Power consumption: 10-30 kWh per tonne. Operate in closed circuit with classifier — oversize returns to mill, undersize proceeds to concentration.

**Rod mill**: Similar to ball mill but uses long steel rods instead of balls. Produces less slime (over-ground fines) than ball mills. Preferred for coarse grinding (feed 5-20 mm, product 0.5-5 mm). Rods cascade rather than cataract, giving more uniform grinding with less over-grinding of already-fine particles.

### Electrostatic Separation

- Used for separating minerals with different electrical conductivity or surface charge behavior. Feed dry, sized ore (75-500 μm) onto rotating drum charged to 20-40 kV. Conductive minerals (ilmenite, rutile, magnetite) acquire charge, repelled from drum surface and follow a different trajectory than non-conductive minerals (quartz, feldspar, zircon). Splitter plate divides the two streams. Effective for heavy mineral sand deposits (ilmenite, rutile, zircon, monazite). Multiple passes required for clean separation. Requires dry feed — moisture interferes with charging.

### Safety & Hazards

- **Cyanide (NaCN/KCN)**: Lethal dose ~200-300 mg oral. Blocks cellular respiration. Symptoms: headache, dizziness, seizures, cardiac arrest in 15-30 min. ANTIDOTE: Hydroxocobalamin or sodium thiosulfate + sodium nitrite. MUST have antidote available before handling. NEVER allow acid contact with cyanide (generates lethal HCN gas at 100 ppm). Keep process pH above 10.
- **Mercury (Hg)**: Cumulative neurotoxin from amalgamation. Vaporizes at room temperature. Use in sealed retort. Never heat in open air.
- **Silica dust**: Crushing/grinding ore generates crystalline silica dust causing silicosis. Respirators required. Wet methods preferred.

### Comminution (Crushing and Grinding) Detail

**Jaw crusher**: The primary crushing stage reduces run-of-mine ore (up to 300 mm) to a manageable size. Two jaw plates — one fixed, one oscillating — crush ore between them. The gap setting is adjustable from 20-100 mm, controlling the maximum output particle size. A tighter gap produces finer output but reduces throughput. Capacity: 1-50 tonnes/hour depending on crusher size and ore hardness. Jaw crusher frame is cast iron or fabricated steel plate. Jaw plates are manganese steel (Mn12-14%), which work-hardens under impact to resist abrasion. Replace jaw plates when worn to 50% of original thickness.

**Ball mill**: The standard fine-grinding machine. A rotating steel cylinder (1-3 m diameter, 2-5 m length) loaded with steel or cast iron grinding balls (25-100 mm diameter, total ball charge 30-45% of mill volume). Ore and water fed at one end, discharge at the other (overflow or grate discharge). Rotation speed: 60-80% of critical speed. The critical speed formula is Nc = 42.3/√D, where Nc is in RPM and D is the mill internal diameter in meters. A 2 m diameter mill has Nc = 42.3/√2 = 29.9 RPM; operating speed would be 18-24 RPM. Below 60% of critical speed, the balls tumble (insufficient grinding). Above 80%, centrifugal force holds the balls against the shell (no grinding at all — "centrifuging"). Product size: 50-200 μm. Power consumption: 10-30 kWh per tonne of ore. Operate in closed circuit with a classifier — oversize material returns to the mill, undersize proceeds to concentration. This closed-circuit arrangement prevents over-grinding (wasting energy on already-fine particles) and ensures a uniform product size.

**[Stamp mill](../glossary/stamp-mill.md)** (bootstrap-appropriate): Vertical stamps (50-500 kg each) lifted by cams on a rotating horizontal shaft, dropped by gravity onto a die plate. 5-10 stamps in a battery. Ore fed onto the die, water carries crushed fines away through a screen. Capacity: 5-10 tonnes/day for a 5-stamp battery with 100 kg stamps. Powered by water wheel. Each stamp lifts 15-25 cm and drops at 30-90 blows per minute. The stamp mill was the standard ore crushing technology from the 16th century through the early 20th century. No precision manufacturing required — the cams and tappets can be made from hardwood shod with iron. The main limitation is throughput: a 10-stamp mill processes roughly 15-20 tonnes/day, versus 50+ tonnes/hour for a jaw crusher.

### Gravity Concentration

**Sluice box**: An inclined wooden or metal trough (2-5 m long, 30-50 cm wide) with riffles (cross-bars) on the bottom. Riffle spacing: 5-10 cm. Water flow: 50-100 liters/minute. Sluice angle: 1-3° from horizontal. Crushed ore is shoveled into the head of the sluice. Water carries material downstream. Heavy minerals (gold at SG 19.3, cassiterite at SG 7.0) settle behind the riffles where turbulence creates eddies. Light gangue minerals (quartz SG 2.65, feldspar SG 2.6) wash over the riffles and out the tail. Clean riffles every 4-8 hours by stopping water flow and scooping out the concentrate. Recovery: 70-90% for gold in the 0.1-5 mm size range. Very poor recovery for fine gold (<0.1 mm) — use a mercury amalgamation plate or cyanide leach for fines.

**Jig**: A mechanical device that uses pulsating water to separate minerals by density. Pulsation: 200-300 strokes/minute, 5-15 mm amplitude. On the upstroke, the bed of crushed ore lifts and particles begin to separate by density (heavy minerals sink faster through the fluidized bed). On the downstroke, heavy particles settle to the bottom and pass through a screen into the hutch (collection chamber), while light gangue remains on top and is swept away by the cross-flow. Effective separation requires a specific gravity difference of at least 1.5 between the valuable mineral and the gangue. Best for coarse particles (2-20 mm). Recovery: 85-95% for dense minerals like cassiterite, wolframite, and gold.

**Shaking table**: A sloped, riffled table (1.2 × 2.4 m typical) that oscillates longitudinally at 200-300 strokes/minute with a 10-20 mm stroke length. A thin film of water flows across the table at right angles to the oscillation. Particles separate by density and size: heavy minerals ride the riffles uphill toward the concentrate discharge, light minerals wash across the riffles to the tailings discharge. Very effective for fine-grained ores (0.05-2 mm). Produces a visible fan-shaped product distribution: concentrate at one end, middlings in the center, tailings at the other. One table processes 0.5-2 tonnes/hour depending on feed size.

**Strengths**:
- Sluice boxes recover 70-90% of gold >0.1 mm with no chemical reagents — only water and gravity
- Jigs achieve 85-95% recovery for dense minerals at 2-20 mm feed size with simple mechanics
- Shaking tables produce visible product separation — operator can adjust in real time

**Weaknesses**:
- Gravity methods require a specific gravity difference ≥1.5 between ore and gangue
- Fine gold (<0.1 mm) passes through sluice riffles — needs amalgamation or cyanide for recovery
- Shaking tables process only 0.5-2 tonnes/hour each — many tables needed for high throughput

### Magnetic Separation

**[Low-intensity magnetic separators](../glossary/low-intensity-magnetic-separators.md)** (0.1-0.3 Tesla): Capture strongly magnetic minerals — primarily magnetite (Fe₃O₄). A rotating drum with internal permanent magnets or electromagnets attracts magnetic particles, which cling to the drum surface and are carried to a separate discharge point. Non-magnetic gangue falls straight through. Used for iron ore beneficiation (magnetite ores) and for removing tramp iron from process streams. Throughput: 10-100 tonnes/hour.

**[High-intensity magnetic separators](../glossary/high-intensity-magnetic-separators.md)** (1-2 Tesla): Capture weakly magnetic minerals — hematite (Fe₂O₃), ilmenite (FeTiO₃), garnet, monazite. These minerals have much lower magnetic susceptibility than magnetite and require strong fields to deflect them. Electromagnetic coils (copper windings on iron cores) generate the field. Used for cleaning industrial minerals (removing iron-bearing impurities from kaolin, silica sand, feldspar) and for concentrating weakly magnetic ores. Throughput: 5-50 tonnes/hour.

### Leaching Detail

**Cyanide leaching for gold**: The dominant gold extraction method worldwide. Dissolve gold in a dilute sodium cyanide solution in the presence of oxygen: 4Au + 8NaCN + O₂ + 2H₂O → 4Na[Au(CN)₂] + 4NaOH.
- Cyanide concentration: 0.01-0.05% NaCN (100-500 ppm). Higher concentrations dissolve gold faster but increase cost and environmental risk.
- pH: maintained at 10-11 with lime (CaO) or sodium hydroxide. Below pH 10, cyanide converts to HCN gas (hydrogen cyanide, lethal at 100 ppm). This is the critical safety requirement: never allow cyanide solutions to become acidic.
- Leach time: 24-72 hours for tank leaching, 30-180 days for heap leaching. Temperature: ambient (15-30°C). Dissolved oxygen required: typically 5-8 ppm. Aeration may be needed in tank leaching.
- Recovery: 85-95% of contained gold for typical ores. Gold is recovered from solution by adsorption onto activated carbon (carbon-in-pulp or carbon-in-leach), then stripped from carbon with hot caustic solution and electrowon onto steel wool cathodes.

**Strengths**:
- Dissolves gold at low reagent concentration (0.01-0.05% NaCN) — cost-effective per ounce recovered
- Tank leaching completes in 24-72 hours; heap leaching handles large volumes at low capital cost
- Carbon adsorption selectively loads gold from solution, simplifying downstream recovery

**Weaknesses**:
- Cyanide is acutely lethal (200-300 mg oral dose) — requires strict pH control >10 and emergency antidote on site
- Heap leach cycles run 30-180 days — slow cash flow return on leach pad investment
- Dissolved oxygen must be maintained at 5-8 ppm — aeration adds energy cost to tank leaching

### Smelting Preparation

**Roasting**: Sulfide ores must be roasted before smelting to remove sulfur and convert metal sulfides to oxides. Heat crushed ore to 500-700°C in air. Sulfur burns off as SO₂ gas (capture for sulfuric acid production if possible — SO₂ + H₂O + catalyst → H₂SO₄). Roasting reactions: 2ZnS + 3O₂ → 2ZnO + 2SO₂, 2PbS + 3O₂ → 2PbO + 2SO₂. Temperature must be controlled: below 500°C the reaction is too slow, above 800°C the ore sinters into a solid mass that blocks air flow. Multiple hearth roasters or fluidized bed roasters provide the best gas-solid contact.

**Sintering**: Fine ore particles (too fine for direct smelting — they would blow out of the furnace) are agglomerated by sintering. Mix fine ore with 5-10% coke breeze (fine coke) and moisture. Feed onto a moving grate (Dwight-Lloyd sinter machine). Ignite the coke with a gas flame. A suction fan pulls air downward through the bed. The burning coke raises the temperature to 1300-1400°C, partially fusing the ore particles into a porous, coherent cake. The sinter cake is crushed and screened to 20-50 mm lumps suitable for blast furnace feed. Sintering also drives off additional sulfur and volatile impurities. A sinter machine processes 20-50 tonnes/hour of fine ore.

---

### Amalgamation

**Mercury amalgamation for gold**: An ancient method for recovering fine gold from concentrates. Mercury (Hg, liquid at room temperature, density 13.5 g/cm³) forms an alloy (amalgam) with gold on contact.

- **Process**: Mix gold-bearing concentrate with liquid mercury in a copper pan or amalgamation barrel (rotating drum lined with copper). Mercury wets gold particles, forming a silver-colored amalgam paste. Amalgamation time: 30-60 minutes with agitation. Recovery: 60-80% of free gold (does not recover gold locked inside sulfide mineral grains).
- **Separation**: Squeeze the amalgam through damp chamois leather. Excess mercury passes through the leather; the gold-rich amalgam (30-50% Au) remains as a stiff paste.
- **Retorting**: Heat the amalgam in a sealed iron retort to 400-500°C. Mercury vaporizes (boiling point 357°C) and condenses in a water-cooled condenser for reuse. Gold remains in the retort as a porous sponge (sponge gold), which is then melted into a doré button. Mercury recovery rate: 95-98% with a good condenser.
- **Environmental hazard**: Mercury vapor is a cumulative neurotoxin. Retort in a well-ventilated area with a gas-tight system. Never heat mercury in an open vessel — the vapor is invisible, odorless, and extremely dangerous. Historical gold mining released vast quantities of mercury into watersheds, contaminating food chains for centuries.

**Strengths**:
- Recovers 60-80% of free gold from concentrate without chemical reagents — only mercury and heat
- Retorting recovers 95-98% of mercury for reuse, keeping operating costs low
- Works on coarse and fine gold alike, unlike sluice boxes which lose fine gold

**Weaknesses**:
- Mercury is a cumulative neurotoxin — vapor exposure causes irreversible neurological damage
- Does not recover gold locked inside sulfide grains (requires cyanide or pressure oxidation first)
- Environmental contamination from mercury spills persists for centuries in watersheds

### Flotation Detail

**[Froth flotation](../glossary/froth-flotation.md)** is the most important concentration method for sulfide ores (copper, lead, zinc, nickel). It exploits differences in surface chemistry between sulfide minerals and silicate gangue:

- **Grinding**: Grind ore to 50-200 μm. Particles must be fine enough to liberate (separate) sulfide mineral grains from the surrounding gangue. Insufficient grinding leaves sulfide grains locked inside gangue particles, unavailable for flotation. Over-grinding produces ultrafine particles (<10 μm) that float poorly.
- **Reagents**: Three categories. (1) **[Collector](../glossary/collector.md)** (xanthate, 20-100 g/tonne): Adsorbs on sulfide mineral surfaces, making them hydrophobic (water-repellent). Sodium ethyl xanthate is the most common. (2) **[Frother](../glossary/frother.md)** (MIBC or pine oil, 20-50 g/tonne): Stabilizes air bubbles into a persistent froth. Without frother, bubbles coalesce and pop too quickly. (3) **[Modifier](../glossary/modifier.md)** (lime, cyanide, zinc sulfate): Adjusts pH and suppresses unwanted minerals. Lime raises pH to 9-11 (depresses pyrite). Cyanide depresses sphalerite (zinc sulfide) in copper-zinc ores.
- **Mechanism**: In the flotation cell, air bubbles rise through the agitated slurry. Hydrophobic sulfide particles attach to bubble surfaces and are carried upward into the froth layer. Hydrophilic gangue particles remain in the slurry. The froth overflows into a launder as concentrate.
- **Circuit design**: A flotation circuit includes rougher cells (initial separation), scavenger cells (recover remaining values from rougher tailings), and cleaner cells (upgrade rougher concentrate to final grade). A copper flotation circuit typically produces concentrate at 20-30% Cu from ore containing 0.5-2% Cu. Recovery: 85-95%.

**Strengths**:
- Achieves 85-95% recovery for sulfide ores — the dominant concentration method worldwide
- Selective: different collectors and pH modifiers separate copper from zinc, lead from iron
- Handles low-grade feed (0.5-2% Cu) and upgrades to smelter-grade concentrate (20-30% Cu)

**Weaknesses**:
- Requires grinding to 50-200 μm for mineral liberation — energy-intensive comminution
- Reagent supply (xanthates, MIBC, lime) must be continuously manufactured and dosed
- Over-grinding produces ultra-fine particles (<10 μm) that float poorly, reducing recovery

### Thickening and Filtration

After flotation or leaching, the concentrate must be dewatered:

**Thickener**: A large circular tank (10-30 m diameter) with a slowly rotating rake mechanism. Slurry (25-35% solids) is fed into the center. Solids settle to the bottom, where the rake pushes them to a central discharge. Clear water overflows the perimeter weir. Thickened underflow: 50-70% solids. Thickener area required: 0.5-5 m² per tonne of dry solids per day depending on particle size. The settled solids are easier and cheaper to filter than dilute slurry.

**Filter**: Vacuum drum filter (rotating cylindrical drum covered with filter cloth, partially submerged in thickener underflow). Vacuum draws water through the cloth, leaving a filter cake of moist concentrate (8-15% moisture). Filter cake is discharged by a scraper blade. Alternative: pressure filter (plate-and-frame) for finer particles that do not filter well on a drum. Filter cake moisture must be low enough for the next processing step: 8-12% for smelter feed, below 15% for shipping.

### Tailings Management Detail

**Tailings dam construction**: The most common method is upstream construction — the dam is built incrementally by depositing coarse tailings on the downstream face and raising the dam crest as the tailings pond fills. Dam height: 20-100+ m for large mines. The dam must be engineered for stability (slope angle, drainage, seismic resistance). Tailings dam failures are catastrophic — they release massive volumes of water and mud downstream. The 2019 Brumadinho dam failure in Brazil killed 270 people.

**Water recycling**: Process water from the tailings pond is pumped back to the plant for reuse. Recycling reduces fresh water consumption by 70-90%. A typical copper flotation circuit uses 2-3 m³ water per tonne of ore. Without recycling, a 50,000 tonne/day operation would consume 100,000-150,000 m³/day of fresh water — impractical in most mining locations.

**Acid rock drainage**: Sulfide-bearing tailings exposed to air and water generate sulfuric acid (pyrite oxidation: FeS₂ + O₂ + H₂O → Fe(OH)₃ + H₂SO₄). The acidic water dissolves heavy metals from the tailings, creating a toxic effluent. Prevention: submerge sulfide tailings under water (limits oxygen access), or blend with limestone to neutralize acid as it forms. Monitor discharge water pH and metal concentrations continuously.

### Sampling and Assay

Accurate sampling is the foundation of ore processing. The process plant can only recover what it is fed, and the feed composition must be known to control the circuit:

**Sampling methods**:
- **Grab sampling**: Take small pieces (50-200 g) from random locations in the ore pile or conveyor belt. Quick but unreliable — biased toward easily visible material. Use only for rough estimates.
- **Cut sampling**: Pass a cutter (bucket or scoop) through the full width of a falling ore stream at regular intervals (every 15-30 minutes). Collects a representative cross-section. The industry standard for conveyor belt and chute sampling.
- **Core sampling**: Split diamond drill core lengthwise (half for assay, half for geological archive). Provides the most systematic subsurface data. Core logging and assay data together define the ore body model and mine plan.

**Assay methods**:
- **[Fire assay](../glossary/fire-assay.md)** (gold, silver): The definitive method for precious metals. Mix 15-30 g of pulverized ore sample with lead oxide (litharge), flour (reducing agent), and flux (borax, silica, soda ash). Heat in a crucible at 1000-1100°C for 45-60 minutes. Lead oxide reduces to metallic lead, which collects gold and silver into a lead button. Cupel the button (heat on a porous bone-ash cupel at 950°C) — lead oxidizes and absorbs into the cupel, leaving a precious metal bead. Weigh the bead. Accuracy: ±1-5% for gold above 1 g/tonne. The oldest and most reliable assay method, in use since ancient Egypt.
- **[Wet chemical assay](../glossary/wet-chemical-assay.md)** (copper, zinc, lead): Dissolve a weighed sample in acid (aqua regia for gold, nitric acid for base metals). Titrate with standard solutions or measure concentration by atomic absorption spectroscopy. Accuracy: ±0.5-2%. Faster than fire assay for base metals.
- **X-ray fluorescence (XRF)**: Irradiate the sample with X-rays, measure the fluorescent X-rays emitted by each element. Non-destructive, multi-element analysis in minutes. Accuracy: ±1-5% depending on element and matrix. Portable XRF analyzers allow real-time grade control at the mine face.

### Process Control

Running a concentrator efficiently requires continuous monitoring and adjustment:

**Key measurements**:
- **Feed grade**: Assay the ore entering the plant (samples every 1-4 hours). Grade variations of ±30% are normal in many ore bodies. The flotation circuit must be adjusted (reagent dosages, pH) to match the current feed composition.
- **Concentrate grade**: Assay the final concentrate. Too low → smelter penalties (pay for impurities). Too high → may indicate you are losing recovery (rejecting middlings that contain values). Target: copper concentrate at 25-30% Cu for most smelters.
- **Tailings grade**: Assay the tailings (waste stream). This is the most important control metric. Rising tailings grade means the circuit is losing recovery — investigate immediately (reagent starvation, worn flotation cells, incorrect pH).
- **Recovery**: Calculated from feed, concentrate, and tailings assays by mass balance. Recovery = (feed grade - tailings grade) / feed grade × concentrate grade × 100%. Target: 85-95% for most flotation circuits. Recovery below 80% indicates a significant process problem.

**Mass balance**: The fundamental accounting of an ore processing plant. Every tonne of ore entering must leave as either concentrate, tailings, or water. Track the mass flow at each stage: crusher feed, mill discharge, flotation concentrate, and final tailings. Use belt scales (load cell on a conveyor idler), flow meters (magnetic or ultrasonic on slurry lines), and density gauges (nuclear or vibrating tube). A consistent mass balance confirms the plant is operating correctly; discrepancies indicate measurement errors or material losses (spills, leaks, incorrect sampling).

### Ore Sorting and Pre-Concentration

Before the main processing circuit, pre-concentration removes waste rock early, reducing downstream grinding and processing costs:

**Hand sorting**: Workers pick visible waste rock from a moving belt or picking table. Effective for coarse ore (>25 mm) with visible mineralization (malachite green in copper ore, red hematite in iron ore). Typically 2-5 workers per belt, each processing 1-3 tonnes/hour. Removes 15-30% of the feed as waste. Labor-intensive but requires no equipment beyond a conveyor belt and good lighting.

**[Optical sorting](../glossary/optical-sorting.md)** (requires electronic sensors): Cameras or laser scanners measure the color, reflectance, or fluorescence of each rock particle on a fast conveyor. Air jets deflect waste particles into a reject stream. Processing rate: 50-200 tonnes/hour per machine. Effective for ores with visual contrast between mineralized and barren rock. Requires electronic controls and compressed air — not available at the earliest bootstrap stages but feasible once basic electrical and pneumatic systems exist.

**Density-based pre-concentration**: Use heavy media separation (HMS) to float off light waste rock. Prepare a heavy medium by suspending fine magnetite or ferrosilicon in water at a controlled specific gravity (2.6-3.3). Feed coarse ore (5-50 mm) into the medium. Light rock (gangue, SG 2.5-2.7) floats and is skimmed off. Heavy ore minerals (SG 3.0+) sink and are recovered from the bottom. The magnetite medium is recovered magnetically and reused. HMS removes 20-40% of the feed as waste before grinding, significantly reducing energy consumption in the downstream circuit.

### Process Water Quality

Water chemistry affects every stage of ore processing, and poor water quality causes cascading problems:

- **[Hard water](../glossary/hard-water.md)** (high Ca²⁺/Mg²⁺): Calcium ions interfere with flotation reagent adsorption on mineral surfaces, reducing selectivity and recovery. Calcium also precipitates with xanthate collectors, wasting reagent. Treat hard water with lime softening (add Ca(OH)₂ to precipitate CaCO₃) or ion exchange before use in flotation circuits.
- **pH control**: Most flotation circuits operate at pH 8-11 (maintained with lime or NaOH). Low pH (<7) decomposes xanthate collectors and corrodes steel equipment. High pH (>12) depresses some target minerals along with the waste, reducing selectivity. Monitor pH continuously at the rougher feed, cleaner feed, and tailings discharge.
- **Recycled water**: Process water recycled from tailings ponds contains residual reagents (xanthates, frothers, lime), dissolved ions (Cu²⁺, Fe³⁺, SO₄²⁻), and fine suspended solids. These can cause unpredictable flotation behavior if concentrations build up. Treatment options: settling (removes solids), neutralization (adjusts pH), activated carbon (removes organic reagents), or biological treatment (degrades residual organics). Monitor recycled water quality weekly and adjust fresh water make-up rate accordingly.

### Conveyor and Material Transport

Moving ore between processing stages efficiently is critical for plant throughput:

- **Belt conveyor**: The standard material transport for crushed ore and concentrate. Rubber belt (500-1500 mm wide) on idler rollers, driven by an electric motor at the head pulley. Capacity: 100-5,000 tonnes/hour depending on belt width, speed (1-5 m/s), and material density. Angle of inclination: up to 18° for most ores (steeper angles cause material rollback). Cover the belt to control dust in dry climates.
- **Slurry pipeline**: Transport finely ground ore as a slurry (30-50% solids by weight) through steel or HDPE pipes. Pumps: centrifugal slurry pumps with hardened impellers. Velocity: 1.5-3.0 m/s (too slow → particles settle and block the pipe; too fast → excessive wear). Used for long-distance transport (1-100+ km) between mine and concentrator or between concentrator and smelter. The Bougainville copper slurry pipeline transported concentrate 27 km.
- **Bucket elevator**: Vertical transport of coarse material. Steel buckets attached to a chain or belt, running between sprockets at top and bottom. Lift height: 10-30 m. Capacity: 10-200 tonnes/hour. Used for elevating crushed ore from below-ground crushers to surface processing. Enclose in a steel casing for dust control.

### Concentrate Handling and Transport

The final concentrate product requires careful handling to preserve its value:

- **Dewatering**: Filter cake from the drum filter contains 8-15% moisture. For smelter delivery, moisture must be below 10-12% (higher moisture causes steam explosions in the smelter). Additional drying in a rotary dryer (hot air at 200-300°C, 10-20 min residence time) reduces moisture to 5-8%. The dried concentrate is less prone to freezing in winter transport and generates less dust.
- **Bagging and storage**: Fill woven polypropylene bags (500-1000 kg each, called "bulk bags" or "FIBCs") with dried concentrate. Stack on pallets under cover. Concentrate is dense (copper concentrate ~2.0-2.5 t/m³, iron ore pellets ~2.0 t/m³). A standard shipping container holds 20-25 tonnes of bagged concentrate.
- **Sampling for payment**: Smelters pay based on the metal content of the concentrate. The final payment sample is taken during loading: an automatic sampler cuts a representative portion (0.1-0.5% of the total) from the loading stream. Split the sample into three portions: one for the mine assay, one for the smelter assay, and one held in reserve for umpire assay (independent laboratory) if the mine and smelter disagree on the grade. Payment disputes are common — accurate sampling protects both parties.

### Processing Plant Layout

The physical arrangement of the processing plant follows the ore flow from ROM (run-of-mine) pad to concentrate storage:

- **Primary crushing**: Located at the mine mouth, close to the ROM pad. Output: -150 mm. Feed directly from trucks or a primary feeder.
- **Grinding circuit**: Downhill or at the same elevation as primary crushing. The ball mill is the heaviest piece of equipment (5-50 tonnes for a medium plant) and requires a reinforced concrete foundation to absorb vibration.
- **Concentration circuit**: Adjacent to the grinding circuit. Flotation cells are arranged in a cascade — rougher cells at the highest elevation, cleaner cells below, with gravity flow between stages wherever possible (reduces pumping costs).
- **Tailings and concentrate**: Tailings line runs downhill to the tailings pond. Concentrate thickener and filter are at the lowest point of the plant, with concentrate storage at grade for easy truck loading.

### Process Energy Balance

Ore processing is energy intensive. The comminution stage (crushing and grinding) alone consumes 50-70% of the total plant energy:

- **Specific energy for grinding**: 10-30 kWh per tonne of ore for ball milling to 80% passing 75 μm. Harder ores (high Bond work index, >20 kWh/t) consume more energy than softer ores (<10 kWh/t). The Bond work index is determined by a standard locked-cycle grindability test: grind a known mass of ore in a standard ball mill, measure the product size distribution, and calculate the energy required per tonne.
- **Crushing energy**: 0.5-2 kWh per tonne for primary and secondary crushing combined (jaw crusher → cone crusher to <20 mm). Much less than grinding because breaking large rocks is more energy-efficient than grinding fine particles (fracture mechanics favor breaking along existing flaws, which are abundant in coarse material).
- **Flotation energy**: 2-5 kWh per tonne for agitation and aeration. Agitator motors: 5-15 kW per 10 m³ cell. Air blowers: 20-50 kW for a 100-cell circuit.
- **Pumping**: 1-3 kWh per tonne for slurry transport between stages. Pumping slurries is less efficient than pumping water because the abrasive particles wear impellers and the higher slurry viscosity increases friction losses.
- **Water consumption**: 2-5 m³ per tonne of ore processed (not evaporated, but circulating through the circuit with losses to tailings moisture and evaporation). In arid regions, water availability can be the binding constraint on plant capacity, not ore reserves or energy supply.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Mining](./index.md) • [All Domains](../index.md)*
