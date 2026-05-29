# Modern Steelmaking

> **Node ID**: metals.steelmaking
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`chemistry.refractories`](../chemistry/refractories.md), [`energy.fuels`](../energy/fuels.md), [`metals.iron-steel`](iron-steel.md), [`metals.iron-steel.blast-furnace`](blast-furnace.md)
> **Enables**: [`metals.alloys`](alloys.md), [`metals.forming`](forming.md)
> **Timeline**: Years 15-30
> **Outputs**: steel billets, slabs, blooms, flat products, long products
> **Critical**: Yes — steel is the structural material of industrial civilization; no modern manufacturing without it

## Problem

Steelmaking is the refining of pig iron — 3.5-4.5% carbon, 1-3% silicon, 0.5-1.5% manganese, plus sulfur and phosphorus — into steel containing 0.02-1.5% carbon with tightly controlled residual elements. The fundamental chemistry is oxidation: dissolved carbon, silicon, manganese, and phosphorus are oxidized by blowing oxygen through or over the molten metal. The oxidized impurities either escape as gas (CO, CO₂) or partition into a basic slag (SiO₂, MnO, P₂O₅ as calcium compounds). Modern steelmaking produces ~1.9 billion tonnes annually, split between basic oxygen furnaces (~70%) and electric arc furnaces (~30%).

The transition from pig iron to steel is the single most important metallurgical refinement. Pig iron is brittle (cast iron) and limited to cast shapes. Steel combines high strength with ductility, enabling structural sections, pressure vessels, wire, sheet, and every mechanical component of industrial civilization.

## Prerequisites

- [Iron and steel fundamentals](iron-steel.md) — ore types, reduction chemistry, wrought iron
- [Blast furnace](blast-furnace.md) — pig iron production (primary feedstock)
- [Refractories](../chemistry/refractories.md) — basic and acid refractory linings for vessels
- [Fuels](../energy/fuels.md) — coke, gas, and energy for heating
- [Air separation](../chemistry/air-separation.md) — tonnage oxygen for BOF steelmaking

### Bessemer Process

The Bessemer process (patented 1856) was the first mass-production method for steel. By blowing air through molten pig iron, Bessemer harnessed the exothermic oxidation of impurities to both refine the metal and maintain its temperature without external fuel.

**Principle**: Air blown upward through 15-30 tonnes of molten pig iron oxidizes silicon first (generating the most heat per unit mass), then manganese, then carbon. The "blow" is self-sustaining — once started, the oxidation heat maintains metal temperature at 1600-1650°C without any external fuel input.

**Vessel**: A Bessemer converter is a pear-shaped refractory-lined steel vessel, 4-6 m tall, mounted on trunnions so it can be tilted for charging and pouring. The bottom contains 100-200 tuyeres (6-10 mm diameter holes) through which air is forced at 1.5-2.5 bar. Typical capacity: 15-30 tonnes per heat.

**Operating sequence**:
1. Tilt converter horizontal. Charge molten pig iron (1200-1300°C) from a ladle. Add scrap steel (coolant, 5-15% of charge) to absorb excess exothermic heat.
2. Return converter to vertical position. Start air blast (30,000-60,000 Nm³/hour depending on vessel size).
3. **[Silicon blow](../glossary/silicon-blow.md)** (first 3-5 minutes): Si + O₂ → SiO₂. Temperature rises rapidly (silicon oxidation releases ~32 MJ/kg Si). Bright flame at the mouth.
4. **[Carbon blow](../glossary/carbon-blow.md)** (next 10-12 minutes): C + ½O₂ → CO. The CO burns at the converter mouth with spectacular flame — "the blow" is visually dramatic. Carbon drops from ~4% to ~0.05%. Metal temperature reaches 1600-1650°C.
5. **End-point detection**: Flame at the mouth drops sharply when carbon is depleted. Experienced operators judged by eye; later installations used optical pyrometers and gas analysis.
6. Stop blast. Tilt converter. Deoxidize with ferromanganese or aluminum (the blow removes all carbon including the desired amount — steel must be recarburized to specification). Tap into ladle.

**Acidic vs Basic Bessemer (Thomas process)**:
- **Acidic Bessemer**: Silica (SiO₂) refractory lining. Cannot remove phosphorus — the P₂O₅ is acidic and would attack the acidic lining. Requires low-phosphorus pig iron (<0.05% P), limiting it to certain ores. Used in Britain with hematite pig iron.
- **Basic (Thomas) process**: Dolomite (MgO·CaO) or magnesite (MgO) refractory lining. Add burned lime (CaO, 10-15% of metal weight) as flux. P₂O₅ is captured as stable calcium phosphate (3CaO·P₂O₅) in the basic slag. This enabled use of high-phosphorus pig iron (1.5-2.0% P) from the Minette ores of Lorraine and Luxembourg. The phosphorus-rich Thomas slag was sold as fertilizer (16-20% P₂O₅). Dominated Continental European steelmaking 1880-1930.

**Limitations**: Nitrogen pickup from the air blast (0.010-0.020% N) caused strain aging and reduced ductility. Inability to precisely control final chemistry. Excessive dissolved oxygen. The Bessemer process was superseded by the basic oxygen furnace by the 1960s, which uses pure oxygen instead of air and avoids nitrogen contamination.

### Open-Hearth Furnace

The Siemens-Martin open-hearth process dominated world steel production from 1890 to 1960. It used regenerative heat exchangers to achieve 1600-1650°C — hot enough to melt steel in a shallow bath, with precise control over composition.

**Principle**: A gas-fired reverberatory furnace melts a shallow bath of pig iron and scrap on a hearth. The flame burns over the metal surface (not through it as in Bessemer). Regenerative brick checker chambers preheat incoming air and fuel gas using exhaust heat, achieving flame temperatures of 1700-1800°C.

**Regenerative system**: Four checker chambers (two for air, two for fuel gas) filled with refractory brick checkerwork. Hot exhaust gases pass through one pair, heating the bricks to 1200-1300°C. Every 15-20 minutes, reversing valves switch flow direction — incoming cold air and fuel gas now pass through the hot checkers, absorbing stored heat. This cycle cuts fuel consumption by 60-70% compared to non-regenerative furnaces.

**Furnace construction**: Rectangular hearth, 12-15 m long × 4-6 m wide, lined with basic refractory (magnesite or dolomite). Bath depth only 300-500 mm — shallow to maximize surface area for flame heating and oxidation reactions. Capacity: 100-300 tonnes per heat. Fuel: producer gas, natural gas, or heavy fuel oil.

**Operating cycle** (6-10 hours per heat):
1. **[Charging](../glossary/charging.md)** (1-2 hours): Load scrap steel (40-60% of charge) and limestone (flux, 5-8% of metal weight) through side doors using charging machines. Pour molten pig iron (the "hot metal," 40-60% of charge) onto the hearth.
2. **[Melt-down](../glossary/melt-down.md)** (2-4 hours): Burner flame melts scrap and heats the combined bath to 1500-1550°C. Silicon oxidizes first, then manganese.
3. **[Ore washing /沸腾 (boil)](../glossary/ore-washing-boil.md)** (1-2 hours): Add iron ore (Fe₂O₃) to the bath to provide oxygen for decarburization. Fe₂O₃ + 3C → 2Fe + 3CO. The CO evolution causes the bath to "boil" — stirring the metal and floating out inclusions. Carbon drops 0.3-0.5% per hour. The boil also homogenizes temperature and composition throughout the shallow bath.
4. **[Deoxidation and finishing](../glossary/deoxidation-and-finishing.md)** (30-60 min): Stop ore additions when target carbon is reached. Add ferromanganese (Mn 70-80%, 8-12 kg/tonne steel) and aluminum (0.3-0.8 kg/tonne) to deoxidize. Take samples, adjust composition with ferroalloys.
5. **Tapping**: Tilt the furnace or open the tap hole. Steel flows into a ladle. Tap-to-tap time: 6-10 hours. Heat size: 100-300 tonnes.

**Advantages over Bessemer**: Precise composition control (slow process allows sampling and adjustment). Flexible charge (any ratio of scrap to pig iron). Low nitrogen (no air blowing through the metal). Better quality steel for critical applications (ship plate, boiler plate, rails).

**Disadvantages**: Slow (6-10 hours vs. Bessemer's 20 minutes). High fuel consumption (2-3 GJ/tonne steel). Large, expensive furnace. Superseded by BOF in the 1960s-70s due to poor productivity — one BOF vessel produces more steel per day than an entire open-hearth shop with 6-10 furnaces.

### Basic Oxygen Furnace (BOF)

The basic oxygen furnace (also called LD converter, after Linz and Donawitz, Austria, where it was developed 1949-1952) produces ~70% of the world's steel. It refines molten pig iron by blowing high-purity oxygen (>99.5%) at supersonic velocity onto the metal surface through a water-cooled lance.

**Principle**: Pure oxygen eliminates the nitrogen problem of the Bessemer process (no N₂ diluent) while providing a much more intense and controllable oxidation reaction. The BOF operates in under 20 minutes, handles 250-350 tonne heats, and requires no external fuel — the exothermic oxidation of C, Si, Mn, and P supplies all necessary heat.

**Vessel**: Cylindrical vessel with a truncated cone bottom, 6-8 m diameter, 8-10 m tall, lined with magnesite-carbon refractory (MgO + 10-20% graphite for thermal shock resistance). Mounted on trunnion ring for tilting. Capacity: 100-350 tonnes (modern vessels are 250-350 t). Refractory life: 15,000-25,000 heats before relining (campaign life of 1-3 years).

**Oxygen lance**: A triple-walled water-cooled copper pipe, 200-300 mm outer diameter, with 3-6 nozzle exits at the tip designed for supersonic flow (Mach 1.5-2.5). Oxygen flow rate: 15,000-25,000 Nm³/hour at 8-15 bar. The lance is positioned 1-3 m above the bath surface — the supersonic oxygen jets penetrate the slag layer and impinge on the metal, creating a vigorous reaction zone.

**[Operating sequence](../glossary/operating-sequence.md)** (total cycle: 30-45 min, blowing time: 15-20 min):
1. **[Charge scrap](../glossary/charge-scrap.md)** (20-30% of total charge, 50-100 tonnes). Scrap acts as coolant — the exothermic reactions generate more heat than needed, and scrap absorbs the excess. Larger scrap pieces are placed at the bottom; light scrap on top.
2. **[Charge hot metal](../glossary/charge-hot-metal.md)** (70-80% of charge). Pour molten pig iron from blast furnace torpedo car or hot metal ladle at 1300-1350°C. Typical hot metal composition: 4.0-4.5% C, 0.3-0.8% Si, 0.3-0.8% Mn, 0.05-0.15% P, 0.02-0.05% S.
3. **Add fluxes**: Burned lime (CaO, 30-70 kg/tonne steel) and dolomite (CaO·MgO, 5-15 kg/tonne). Flux creates a basic slag (V-ratio = CaO/SiO₂ = 2.5-4.0) that absorbs SiO₂, MnO, and P₂O₅. Fluorspar (CaF₂, 2-5 kg/tonne) may be added to improve slag fluidity.
4. **Lower lance and start blow**. First 3-5 minutes: rapid oxidation of Si and Mn. Temperature rises 50-100°C/min. Slag foams from CO evolution. At ~5 minutes, silicon is largely gone and carbon oxidation dominates.
5. **[Main blow](../glossary/main-blow.md)** (minutes 5-15): C + ½O₂ → CO (with some secondary combustion CO + ½O₂ → CO₂ above the bath). Carbon drops from ~4% to the target 0.03-0.10%. Massive CO generation — BOF off-gas is 70-85% CO with a calorific value of ~8 MJ/Nm³, collected and used as fuel gas in the steelworks.
6. **End-point control**: Sublance measurement (temperature + carbon by liquidus method) at 80-90% of expected blow time. Target: 1600-1650°C and 0.03-0.08% C. If temperature is high and carbon is low, stop the blow. If adjustments needed, continue blowing or add coolants. Modern BOFs achieve target within ±5°C and ±0.01% C on >90% of heats.
7. **Sampling and tapping**: Raise lance, tilt vessel, take a metal sample for analysis. Tap steel into ladle (with deoxidizer additions — Al wire, FeMn, FeSi). Separate slag carefully — BOF slag contains 15-25% total iron and is recycled to sinter plants or used as aggregate.

**Yield**: 88-93% of metallic charge reports as liquid steel. Losses are primarily iron oxidized into the slag (slag FeO = 10-25%).

**Energy balance**: The BOF is a net energy producer. The exothermic heat of oxidation exceeds the heat needed to melt the scrap charge and raise the bath temperature. Excess heat: ~30-50 MJ/tonne steel, manifest as BOF gas (CO) and sensible heat in off-gas. Total oxygen consumption: 45-60 Nm³ per tonne of steel.

### Electric Arc Furnace (EAF)

The electric arc furnace produces ~30% of world steel, predominantly from 100% scrap charge. Graphite electrodes carry three-phase AC current (or DC in modern designs), creating electric arcs that transfer heat directly to the scrap and molten steel.

**Principle**: Three graphite electrodes (AC furnace) or a single bottom electrode (DC furnace) descend into the furnace. Arc temperature: 3,000-3,500°C. The arc radiates heat to the charge, melting scrap in stages. No combustion gases — the heat source is entirely electrical, so the furnace atmosphere can be controlled (reducing or oxidizing as needed).

**Furnace construction**: Cylindrical shell, 5-8 m diameter, lined with water-cooled panels (upper sidewalls and roof) and magnesite-carbon refractory (lower walls and hearth). The water-cooled panels enable much faster melting rates than all-refractory designs. Eccentric bottom tapping (EBT) separates clean steel from slag during tapping. Capacity: 50-200 tonnes (modern: 100-150 t typical).

**Operating cycle** (total tap-to-tap: 30-50 min):
1. **[Charge scrap](../glossary/charge-scrap.md)** (2-3 buckets, 100% scrap charge). First bucket: 50-60% of total charge. Heavy scrap at bottom, light scrap on top. Electrodes bore through light scrap into heavy scrap, establishing the arc.
2. **Melt-down** (15-25 min): Lower electrodes, strike arcs, melt scrap in stages. Power input: 40-80 MW (150-250 kVA/tonne). During boring-in phase (first 5-8 min), voltage is low and current is high to penetrate the scrap without electrode breakage. During main melting, voltage increases for maximum power. Oxygen lancing (1,500-3,000 Nm³ O₂ per heat) accelerates melting and provides additional chemical heat from scrap contamination (oil, rubber) combustion.
3. **Refining** (5-10 min): Once flat-bath (all scrap melted), refine by injecting oxygen (burning carbon and phosphorus) and adding lime for basic slag. Remove phosphorus early while temperature is still moderate (<1600°C) — phosphorus partition to slag is favored at lower temperatures.
4. **Tapping**: Tilt furnace, tap steel into ladle through EBT spout. Add deoxidizers and alloy additions in the ladle during tapping (tap alloying). Leave slag in the furnace (slag-free tapping is critical for clean steel).

**Energy consumption**: 350-500 kWh/tonne steel (modern UHP furnaces with oxygen lancing and scrap preheating approach 300-350 kWh/t). Older furnaces: 550-700 kWh/t. Auxiliary fuel (natural gas burners, 3-5 MW) supplements arc heating during cold spots. Total energy (including oxygen and fuel): ~1.5-2.5 GJ/tonne.

**Electrode consumption**: 1.0-3.0 kg graphite per tonne of steel. Electrodes are consumed by oxidation, sublimation (at arc tip temperatures), and breakage. Electrode diameter: 500-750 mm. Cost: electrodes represent 5-10% of EAF operating cost.

**Scrap quality challenge**: EAF steel inherits the residual element content of the scrap charge. Copper, tin, nickel, chromium, and molybdenum accumulate over multiple recycling loops ("recycling drift"). Copper is particularly problematic — it is not oxidized in the EAF (less noble than iron... actually copper is more noble, so it remains in the steel), and above ~0.15-0.20% Cu causes surface hot shortness during rolling. EAF steel is therefore limited to applications tolerant of residual elements, or requires high-quality (low-residual) scrap such as direct-reduced iron (DRI) or pig iron as a diluent.

**Advantages over BOF**: Low capital cost (~$100-150/annual tonne vs. BOF ~$200-300). Flexible — can start and stop daily to match electricity pricing. Uses 100% scrap (no blast furnace required). Compact footprint. The EAF route is the primary path for steel recycling.

### Ladle Metallurgy

Secondary steelmaking (ladle metallurgy, ladle refining) occurs after tapping from the BOF or EAF and before casting. The ladle furnace is not a primary melting unit — it adjusts chemistry, temperature, and cleanliness to the precise specification required for continuous casting.

**Deoxidation**: Dissolved oxygen in liquid steel (~200-600 ppm after BOF, ~50-200 ppm after EAF) must be reduced to <10 ppm (ideally <5 ppm) to prevent blowholes and inclusion formation during solidification. Deoxidizers: aluminum (most common, 0.3-1.0 kg/t, forms Al₂O₃ clusters), silicon (as FeSi, 1-3 kg/t), manganese (as FeMn, 5-15 kg/t). Aluminum-killed steel (Al ≥ 0.02%) is the dominant practice — Al₂O₃ inclusions are removed by argon stirring and slag absorption. Silicon-killed steel is used for certain grades where aluminum is undesirable.

**Desulfurization**: Sulfur causes hot shortness (FeS low-melting-point grain boundary films) and reduces ductility and toughness. Target: <0.010% S for structural grades, <0.005% S for high-quality plate, <0.001% S for ultra-clean steels (line pipe, offshore). Method: treat steel in the ladle with synthetic slag (CaO + CaF₂ + Al₂O₃, basicity CaO/SiO₂ > 4) and inject calcium-silicide powder (CaSi, 1-3 kg/t) or magnesium granules. Desulfurization efficiency: 50-80% per treatment. Argon stirring through a porous plug in the ladle bottom mixes slag and metal, accelerating the reaction.

**[Degassing](../glossary/degassing.md)** — dissolved hydrogen and nitrogen removal:
- **RH (Ruhrstahl-Heraeus) degasser**: A vacuum chamber with two snorkel tubes immersed in the ladle. Argon injected into one snorkel drives circulation (lift gas) — steel rises into the vacuum chamber, dissolved gases (H₂, N₂) flash out under vacuum (0.5-5 mbar). Steel cycles through the chamber 3-5 times over 15-25 min. Hydrogen reduced from 4-6 ppm to <2 ppm (critical for heavy sections where H causes cracking — rail, forging, plate). Nitrogen reduced from 60-80 ppm to 30-50 ppm. Also enables vacuum decarburization for ultra-low carbon steels (<0.003% C).
- **VD (vacuum degassing)**: Entire ladle placed in a vacuum tank. Argon stirring through bottom porous plug. Simpler than RH but less efficient — longer treatment time, less effective for decarburization. Typical hydrogen reduction: 4-6 ppm → 1.5-2.5 ppm.
- **VOD (vacuum oxygen decarburization)**: For stainless steel — oxygen blown under vacuum to selectively remove carbon while preserving chromium (Cr has lower affinity for oxygen at low pressure). Used after EAF melting of stainless scrap.

**Inclusion modification — calcium treatment**: Inject Ca (as CaSi wire, 0.3-1.5 kg/t) to transform hard, solid Al₂O₃ clusters (which clog continuous caster nozzles and cause fatigue failure in finished steel) into liquid calcium aluminates (12CaO·7Al₂O₃) that remain spherical during rolling and are less harmful to mechanical properties. Calcium also modifies MnS stringers (which cause anisotropic toughness) into globular CaS + (Ca,Mn)S inclusions. Essential for clean steel production.

**Alloy trimming**: Add ferroalloys in the ladle to achieve final chemistry: FeMn (manganese, 0.3-1.5%), FeSi (silicon, 0.1-0.4%), FeCr (chromium for alloy grades), FeV, FeNb, FeTi as required. Aluminum wire for fine-tuning dissolved Al to 0.02-0.06%. The ladle furnace arc reheats steel to compensate for temperature losses during treatment (typical target: 20-40°C above liquidus for continuous casting, adjusted for time-in-ladle before casting).

**Ladle furnace (LF)**: A three-electrode arc furnace designed to hold and reheat steel in the ladle. Arc power: 10-25 MW. Temperature increase rate: 3-5°C/min. The LF provides time and thermal headroom for the ladle metallurgy operations — without it, steel would cool below the casting temperature window during extended refining treatments.

### Continuous Casting

Continuous casting converts liquid steel into semi-finished solid sections (billets, blooms, slabs) in a single continuous operation, eliminating the ingot-soaking-rolling sequence. It is the single most important improvement in steelmaking since the Bessemer process — yielding 95-98% of liquid steel as salable product versus 80-85% for ingot casting. Over 95% of world steel is now continuously cast.

**Principle**: Liquid steel flows from a ladle into a tundish (an intermediate refractory-lined reservoir that ensures steady, controlled flow), then through a submerged entry nozzle (SEN) into a water-cooled copper mold. The mold oscillates vertically (2-6 mm stroke at 100-300 cycles/min) to prevent the solidifying shell from sticking. A thin solid shell forms at the mold walls within seconds. The strand exits the mold with a solid shell thickness of 10-15 mm and a still-liquid core. It is guided through a curved or vertical machine, cooled by water sprays, until fully solidified (metallurgical length: 15-35 m depending on section size and casting speed). The solid strand is straightened (if curved machine) and cut to length by traveling torches.

**Tundish**: Rectangular or T-shaped refractory-lined vessel, 5-15 tonne capacity. Functions: distribute steel to multiple mold strands (a single caster may have 2-8 strands for billets), stabilize flow (acts as a buffer between ladle and mold), promote inclusion flotation (steel residence time of 3-7 min allows large inclusions to float out), and serve as an emergency reservoir if ladle flow is interrupted. Tundish furniture (dams, weirs, impact pads) controls flow patterns to maximize inclusion removal.

**Mold**: Water-cooled copper alloy (Cu-Ag or Cu-Cr-Zr) tube, 700-900 mm long for slabs, 700-800 mm for billets. Water velocity in mold cooling channels: 6-12 m/s (higher velocity prevents nucleate boiling and ensures uniform heat extraction). Heat flux: 1-3 MW/m² in the meniscus region. Mold powder (flux) added to the meniscus — it melts, forming a liquid slag layer that lubricates the strand-mold interface (reducing friction and preventing breakout) and absorbs inclusions from the steel surface. Mold level control: critical ±2 mm — eddy current or radioactive level sensors feed back to the stopper rod or slide gate controlling flow from the tundish.

**Casting speeds**: Slabs (200-250 mm thick × 800-2100 mm wide): 1.0-2.5 m/min. Blooms (200-400 mm square): 0.5-1.5 m/min. Billets (100-200 mm square): 2.0-5.0 m/min. Throughput: a single-strand slab caster produces 0.5-1.5 million tonnes/year.

**Spray cooling**: Secondary cooling zone below the mold. Water sprays (and air-mist sprays for uniform cooling) extract heat to complete solidification. Cooling intensity: 0.5-2.5 L water per kg steel. Spray pattern must be uniform — uneven cooling causes thermal stress, transverse cracking (particularly at the straightening point where the strand is bent from curved to straight), and surface defects.

**Product types**:
- **Slabs**: 200-250 mm thick × 800-2100 mm wide × 4-12 m long. Feedstock for flat products (plate, hot-rolled strip, cold-rolled sheet).
- **Blooms**: 200-400 mm square (or rectangular up to 400×600 mm). Feedstock for structural shapes (I-beams, channels, rails) and seamless tube rounds.
- **Billets**: 100-200 mm square. Feedstock for bar, rod, wire, and seamless tube production.

**Breakout**: The catastrophic failure mode — the solid shell ruptures, releasing liquid steel into the machine. Caused by sticker (shell sticking in mold), thin shell from insufficient mold cooling, or mold level fluctuation. Prevented by mold level control, mold thermal monitoring (detecting hot spots indicating thin shell), and breakout prediction systems using mold thermocouple data. Consequences: production stoppage of 4-12 hours, equipment damage, safety hazard.

### Ingot Casting

Before continuous casting (and still for certain specialty grades), steel was cast as ingots — individual molds filled from a ladle, each producing a single block of steel weighing 5-30 tonnes. Ingot casting remains necessary for forgings (turbine rotors, pressure vessels, nuclear components) where the cross-section exceeds continuous caster capability.

**Teeming**: Pouring liquid steel from a bottom-poured ladle into cast iron ingot molds standing on a stool (flat base plate). Bottom pouring (steel enters the mold from the base through a central runner) is preferred for clean steel — the steel rises gently through the mold without splashing, minimizing reoxidation and surface defects. Top pouring is simpler (steel poured directly into the open mold top) but generates more surface defects and reoxidation inclusions.

**[Killing practice](../glossary/killing-practice.md)** — controlling the solidification reaction:
- **Rimmed steel**: Incompletely deoxidized. Dissolved oxygen and carbon react during solidification (C + O → CO), generating CO gas that causes a pronounced rim of gas bubbles at the ingot surface. The rim zone is very low in carbon and impurities ( segregation pushes them inward). Produces excellent surface quality — historically important for automotive body sheet. No longer produced in significant quantities.
- **Capped steel**: Partially deoxidized. A short period of rimming action produces a clean surface, then a metal cap (or bottle-top mold) seals the mold top, building pressure that suppresses further gas evolution. Intermediate between rimmed and semi-killed.
- **Semi-killed steel**: Partially deoxidized (some O remains). Minimal gas evolution during solidification. Used for structural shapes and plate where moderate cleanliness is acceptable. Falling out of use as continuous casting replaces ingots.
- **Killed steel**: Fully deoxidized (Al, Si, or both). No gas evolution during solidification. Large pipe shrinkage cavity at the top (5-10% of ingot volume), which is cropped off before rolling. Produces the cleanest, most homogeneous steel. Almost all modern steel is killed — required for continuous casting (rimming action would disrupt the mold process).

**Soaking pits and primary rolling**: Ingots are not rolled directly — the as-cast structure is coarse, brittle, and non-uniform. Ingots are heated in soaking pits (gas-fired or electric reheating furnaces) to 1200-1300°C and held for several hours to homogenize temperature and dissolve segregation. They are then rolled on a blooming mill (large two-high reversing mill) into blooms or slabs. This first rolling pass breaks the as-cast grain structure and consolidates any internal porosity. Soaking pit fuel: 0.5-1.0 GJ/tonne.

### Steel Product Forms

Steel products are classified by the shape of the semi-finished input and the rolling process applied:

**[Flat products](../glossary/flat-products.md)** (from slabs):
- **Hot-rolled strip**: Slab reheated to 1200-1300°C, rolled in a continuous hot strip mill (roughing stands + 5-7 finishing stands) to 1.5-12 mm thickness at 850-950°C exit temperature. Coil weight: 20-30 tonnes. The dominant steel product by volume — used for automotive, construction, pipe, tube, and as feedstock for cold rolling.
- **Cold-rolled sheet**: Hot-rolled strip pickled (acid-cleaned to remove scale) and cold-rolled to 0.15-3 mm thickness at room temperature. Higher dimensional accuracy and better surface finish than hot-rolled. Subsequently annealed (650-750°C to restore ductility lost during cold work) and temper-rolled (0.5-2% cold reduction for flatness and surface finish).
- **Plate**: Slab rolled to 5-150 mm thickness on a plate mill (single-stand four-high or reversing mill). Used for shipbuilding, pressure vessels, bridges, storage tanks, and line pipe. Quality requirements: through-thickness ductility (Z-direction testing), ultrasonic testing for internal defects, and impact testing at design temperature.
- **Coated sheet**: Galvanized (Zn coating, 20-275 g/m²), galvannealed (Zn-Fe alloy), or prepainted (organic coating on galvanized substrate). Automotive and construction applications.

**[Long products](../glossary/long-products.md)** (from billets and blooms):
- **Bar**: Round, square, hexagonal, or flat cross-sections, 8-100 mm diameter, rolled on bar mills (10-18 stands in continuous train). Used for shafts, fasteners, reinforcing bar, and machining stock. Reinforcing bar (rebar) is the largest single long product by volume.
- **Rod**: 5.5-20 mm diameter, coiled at high speed (wire rod mill, finishing speeds up to 100-120 m/s). Feedstock for wire drawing (fences, cables, springs, tire cord). Requires tight control of surface quality and internal defects (any surface seam becomes a wire break during drawing).
- **Structural shapes**: I-beams (H-beams), channels, angles, tees. Rolled from blooms on structural mills (universal mills with horizontal and vertical rolls). Used for construction, bridges, and machinery frames.
- **Rail**: 50-75 kg/m, rolled from blooms. Premium grade: head-hardened (selectively heat-treated rail head for wear resistance). Railway infrastructure.

**Tubular products**:
- **Seamless tube**: Pierced from a heated round billet on a rotary piercing mill (Mannesmann process). The billet is rotated and pushed over a pointed mandrel — tensile stresses at the center cause a cavity, and the mandrel shapes the bore. Further rolled on a plug mill or mandrel mill to final wall thickness. Diameter range: 20-700 mm. Used for oil and gas drilling (OCTG — oil country tubular goods), boiler tubes, hydraulic cylinders, and mechanical tubing. Seamless tube has no weld seam — superior for high-pressure and corrosive service.
- **Welded tube**: Flat strip or plate formed into a cylindrical shape on a roll-forming line and welded longitudinally (ERW — electric resistance welding, for 10-600 mm diameter) or spirally (SAW — submerged arc welding, for 300-2500 mm diameter). Lower cost than seamless. Used for line pipe, structural piling, mechanical tubing, and plumbing. ERW weld quality has improved dramatically — modern ERW pipe is suitable for many sour service and high-pressure applications that formerly required seamless.

### Safety & Hazards

**Molten metal and slag**: Steel at 1600-1650°C and slag at 1500-1600°C cause instantaneous third-degree burns on contact. Full PPE: aluminized heat-resistant coat, safety glasses with side shields, face shield, heat-resistant gloves, metatarsal boots. Never stand over or walk across ladle paths. Molten metal and moisture cause violent steam explosions — all tools, refractories, alloys, and scrap must be thoroughly dry before contact with liquid steel. Even a few drops of water trapped under slag can produce an explosion large enough to tip a ladle.

**BOF and EAF gas hazards**: BOF off-gas is 70-85% CO (toxic, flammable, explosive range 12.5-74% in air). EAF off-gas contains CO and metallic fumes. Gas collection and cleaning systems (wet scrubbers, baghouses) are mandatory. CO monitors in all operator areas. Evacuation alarm if CO exceeds 50 ppm. Confined space entry near furnace off-gas systems requires SCBA.

**Dust and fumes**: EAF steelmaking generates 10-20 kg dust per tonne of steel (containing Fe₂O₃, ZnO from galvanized scrap, Pb, Cr, Ni). Dust is collected in baghouses and either recycled (zinc recovery via Waelz kiln) or landfilled as hazardous waste. Hexavalent chromium (Cr⁶⁺) fume from stainless steel melting is a confirmed carcinogen — local exhaust ventilation and respiratory protection required during stainless steelmaking.

**Electrical hazards (EAF)**: 40-80 MW at 300-800 V through graphite electrodes. Arc flash hazard. Ground fault detection mandatory. Water-cooled panels carry both high-voltage electrical connections and cooling water — a water leak into the furnace causes a violent steam explosion. Water flow monitoring with automatic power trip on flow deviation.

**Caster breakout**: Liquid steel escaping the solidifying shell is a catastrophic event. Operators in the caster area must be trained in breakout response: evacuate the strand, cut power to the mold oscillation and spray systems, contain the spill with sand or damming. Breakout alarms (mold thermocouple deviation) give 30-60 seconds warning — sufficient to reduce casting speed and prevent full breakout in many cases.

**Refractory collapse**: Furnace and ladle refractories fail under thermal cycling and chemical attack. Refractory fragments falling into molten steel cause splashing. Regular gunning (refractory spray repair) and scheduled relining prevent unexpected failures. Never tap a vessel with known refractory damage in the impact zone.

**Noise**: Arc furnaces exceed 120 dB during melt-down. Continuous caster mold oscillation and spray chambers produce sustained 95-105 dB. Hearing protection mandatory in all steelmaking areas. Communication by radio or hand signals.

### Bootstrap Sequence

Steelmaking capability builds in stages, each requiring progressively more infrastructure:

**[Stage 1: Puddled steel from pig iron](../glossary/stage-1-puddled-steel-from-pig-iron.md)** (Years 10-15)
- Finery and chafery, or puddling furnace, refines pig iron by stirring molten iron in a reverberatory furnace with an iron bar, burning out carbon and silicon by exposure to air. Labor-intensive (one puddler per 100-200 kg heat) but requires no special equipment beyond the furnace and a strong back. Produces wrought iron with variable carbon content — early "steel" was made this way for tools and springs. See [Iron & Steel](iron-steel.md) for puddling detail.
- Production: 1-5 tonnes/day per furnace. Quality is inconsistent — relies on the puddler's judgment of carbon level by the appearance of the metal ("bright heat," "dead melt").

**[Stage 2: Bessemer or early open-hearth](../glossary/stage-2-bessemer-or-early-open-hearth.md)** (Years 15-20)
- Requires: pig iron from blast furnace (>5 t/day), reliable air supply (steam-driven blower), basic refractories (dolomite, magnesite). Bessemer converter is mechanically simpler — tilting vessel, bottom tuyeres, blower. Open-hearth requires regenerative checker chambers and gas producer but gives better quality.
- Production: 50-200 tonnes/day per vessel (Bessemer), 100-300 tonnes per heat (open-hearth, one heat per 8 hours). Enables consistent steel for rails, structural sections, ship plate.
- The choice between Bessemer and open-hearth depends on ore chemistry: low-phosphorus ores suit acidic Bessemer; high-phosphorus ores require the Thomas (basic) variant or open-hearth.

**[Stage 3: BOF and continuous casting](../glossary/stage-3-bof-and-continuous-casting.md)** (Years 20-25)
- Requires: tonnage oxygen plant (air separation, see [Air Separation](../chemistry/air-separation.md)), water-cooled copper molds, precision hydraulics for caster. The BOF replaces Bessemer with faster cycles (20 min vs. 20 min, but 250+ tonnes per heat vs. 15-30 t) and vastly better quality (no nitrogen pickup).
- Continuous casting eliminates ingot soaking and blooming mill — direct slab/billet production with 95-98% yield. Capital-intensive but transforms steelworks productivity.
- Production: 2,000-10,000 tonnes/day per BOF vessel + caster combination.

**[Stage 4: EAF and ladle metallurgy](../glossary/stage-4-eaf-and-ladle-metallurgy.md)** (Years 25-30)
- Requires: reliable electricity (30-50 MW per furnace), graphite electrode manufacturing, ladle furnace with vacuum degassing capability. The EAF route bypasses the blast furnace entirely — 100% scrap steel recycling. Essential for regions without coking coal or iron ore.
- Ladle metallurgy (Ca treatment, RH degassing) enables ultra-clean steel for critical applications: line pipe, offshore structures, pressure vessels, bearing steel. Without secondary metallurgy, steel is limited to commodity grades.
- Production: 500-2,000 tonnes/day per EAF (depending on tap-to-tap time and furnace size).

**Why steelmaking matters for bootstrapping**: Steel is the structural material of industrial civilization. Without it: no rails, no bridges, no pressure vessels, no machine tools, no automobiles, no ships, no high-rise buildings, no pipelines. Each stage of steelmaking development unlocks progressively more demanding applications — puddled steel for hand tools, Bessemer steel for rails and boilers, BOF + continuous casting for mass production, EAF + ladle refining for clean specialty grades. The steel plant is the heart of any industrial economy.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Steel too high in carbon | Blow stopped too early (Bessemer/BOF) | Continue oxygen blow; sample with spoon and test fracture; target endpoint carbon by calculation |
| Excessive phosphorus in steel | Acidic slag not removing P, or high-P pig iron | Switch to basic process (Thomas/Gilchrist-Thomas); increase lime addition; verify ore source |
| Nitrogen embrittlement | Air blow (Bessemer) dissolves N₂ in steel | Switch to oxygen blow (BOF); use bottom-blown or combined blowing; add aluminum to tie up nitrogen |
| Blistering in continuous casting | Dissolved gas (H₂, N₂) forming bubbles during solidification | Degas in ladle furnace; reduce moisture in refractories and alloys; use vacuum degassing for critical grades |
| Surface cracks on slabs | Uneven cooling or mold misalignment | Optimize spray cooling pattern; check mold taper and alignment; adjust casting speed |
| Ingot pipe (shrinkage cavity) | Insufficient hot topping or poor feeding | Use exothermic hot tops; increase pouring temperature; apply sufficient保温 (insulating) cap |

## See Also

- [Iron and Steel](iron-steel.md) — fundamentals, ore types, bloomery smelting
- [Blast Furnace](blast-furnace.md) — pig iron production
- [Alloys](alloys.md) — steel alloy design and heat treatment
- [Forming](forming.md) — rolling, forging, and shaping steel products
- [Refractories](../chemistry/refractories.md) — furnace linings
- [Machine Tools](../machine-tools/index.md) — steel as the primary structural material for tools

[← Back to Metals](index.md)
