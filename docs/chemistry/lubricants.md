# Lubricants, Oils & Fluid Mechanics

> **Node ID**: chemistry.lubricants
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`animals.animal-materials`](../animals/animal-materials.md), [`chemistry.petroleum-alternatives`](petroleum-alternatives.md), [`foundations.tools-basic`](../foundations/tools-basic.md)
> **Enables**: [`energy.gravity`](../energy/gravity.md), [`energy.wind`](../energy/wind.md), [`machine-tools.machining`](../machine-tools/machining.md)
> **Timeline**: Years 0-200+
> **Outputs**: lubricating_oil, grease, cutting_fluid, hydraulic_fluid, vacuum_oil
> **Critical**: No — lubricants extend machine life and reduce friction but are not prerequisites for core capabilities

## Problem

Every machine with moving parts generates friction and heat. Two metal surfaces pressed together under load touch only at microscopic peaks called asperities. At those contact points, pressures exceed the yield strength of the metal. The surfaces weld together instantaneously, then tear apart as the parts move relative to each other. Each weld-and-tear cycle removes material, generates heat, and creates wear debris that grinds between the surfaces and accelerates further destruction. A plain steel-on-steel bearing running dry has a friction coefficient around 0.8. At moderate speed and load, it generates enough heat to discolor the metal within minutes and seize within hours.

Lubrication interrupts this destructive cycle by interposing a film of material between the surfaces. That film can be a molecular layer of adsorbed fatty acids (boundary lubrication), a thick cushion of fluid oil (hydrodynamic lubrication), a smear of semi-solid grease, or a coating of solid material that shears easily under load. Each approach works best for different combinations of speed, load, temperature, and environment. The friction coefficient drops from 0.8 (dry) to 0.1 (boundary) to 0.001 (hydrodynamic), a factor of 800 improvement that transforms a machine from self-destructing to long-lived.

A civilization rebuilding its industrial base needs lubricants from day one. The first cart axle, the first treadle lathe, the first water pump all need something to reduce friction. The progression runs from animal fats (available immediately) through vegetable oils (first year harvest) to refined mineral oils (once petroleum distillation is established) and finally synthetic fluids (requiring advanced chemical synthesis). Each tier enables more demanding machinery: animal fats suffice for slow, lightly loaded bearings, but high-speed engines, precision machine tools, and vacuum systems require progressively more sophisticated lubricants.

The economic case is straightforward. A well-lubricated bearing lasts years; a dry one lasts hours. A properly oiled gear train transmits power efficiently; an unlubricated one wastes energy as heat and wears out rapidly. Cutting tools with proper cutting fluid achieve good surface finish and long tool life; without it, the tool welds to the workpiece and both are ruined. Hydraulic systems that maintain clean, stable fluid run for decades; contaminated or degraded fluid causes pumps to fail and valves to stick. The cost of lubrication is trivial compared to the cost of replacing machinery that failed for want of it.

Beyond simple friction reduction, lubricants serve several secondary functions. They carry heat away from bearings and gears. They seal clearances against contamination (oil films fill microscopic gaps). They prevent corrosion (oil coats metal surfaces and excludes air and moisture). They flush wear debris from contact zones. In cutting fluids, they also cool the tool and workpiece while washing away chips. Each of these functions matters, and a lubricant that fails at any of them can cause equipment failure.

This article covers lubricants in four tiers of increasing technological complexity. Each tier builds on the materials and capabilities established by the ones before it, and each enables new classes of machinery that were impractical or impossible with the lubricants available at the previous tier.

## Lubrication Regimes

### Boundary Lubrication

Thin molecular film (1-10 nm) of polar molecules adsorbed on metal surfaces. Fatty acids (from animal/vegetable fats) have a polar head that attaches to the metal oxide surface and a non-polar tail (hydrocarbon chain). The molecules orient perpendicular to the surface, forming a packed monolayer that prevents metal-to-metal contact. This regime dominates at low speed, high load, and intermittent motion, the conditions found in slow-moving machinery, sliding surfaces, and startup/shutdown of faster equipment.

**Effectiveness**: Reduces friction coefficient from ~0.8 (dry steel-on-steel) to ~0.1-0.15. Prevents galling and seizing. The film breaks down above ~150°C (fatty acids desorb and oxidize), which sets the temperature ceiling for organic boundary lubricants.

### Hydrodynamic Lubrication

A full fluid film separates the surfaces. No metal contact occurs. Friction is entirely viscous drag of the fluid. This regime requires three conditions: correct viscosity (thick enough to maintain the film under load, thin enough to flow), adequate speed (generates pressure in the converging wedge of lubricant), and proper bearing geometry (correct clearance and alignment).

**[Reynolds equation](../glossary/reynolds-equation.md)** governs the film pressure distribution. Simplified for a plain journal bearing: minimum film thickness h_min ≈ (μ × U × d²) / (4 × W), where μ = viscosity, U = surface speed, d = bearing diameter, W = load. Maintain h_min > 3× surface roughness for full film separation.

**Friction coefficient**: ~0.001-0.01 (10-100x lower than boundary). This is why well-lubricated bearings run cool and last years.

**[Oil viscosity grades](../glossary/oil-viscosity-grades.md)** (ISO VG system): ISO VG 32 = kinematic viscosity 32 cSt at 40°C (light spindle oil). ISO VG 68 = 68 cSt (general machine oil). ISO VG 220 = 220 cSt (gear oil). ISO VG 460 = 460 cSt (heavy gear oil). Higher viscosity means thicker oil, more load capacity, but also more viscous friction and heat generation.

### Elastohydrodynamic Lubrication (EHL)

Occurs in rolling element bearings and gear teeth where contact pressures reach 1-3 GPa. The extreme pressure elastically deforms the metal surfaces and compresses the lubricant, dramatically increasing its viscosity (the pressure-viscosity effect). The result is a thin but extremely stiff film, 0.1-1 μm thick, that separates the surfaces. EHL requires a lubricant with a good pressure-viscosity coefficient. Mineral oils perform well in this regime; water-based lubricants perform poorly.

---

## Tier 1: Natural Lubricants (Years 0-5)

### Animal Fats (Tallow & Lard)

**Composition**: Triglycerides of saturated and monounsaturated fatty acids. Solid or semi-solid at room temperature. Polar fatty acid chains adsorb strongly to metal oxide surfaces, providing effective boundary lubrication.

**Prerequisites**:
- Animal fat supply (beef, mutton, or pig fat from [animal processing](../animals/animal-materials.md))
- Iron pot or kettle for heating
- Water supply for rendering and clarification
- Cloth for filtering
- Screw press (optional, for pressing cracklings)

**Materials**:
- Raw animal fat (suet, leaf fat, or trimmings)
- Water

**Production**:

**[Tallow](../glossary/tallow.md)** (beef/mutton fat):
1. Cut fat into small pieces (1-2 cm). Smaller pieces render faster and more completely.
2. Heat in iron pot with water (prevents scorching) at 80-100°C for 2-4 hours. Fat melts out and floats on water.
3. Skim off the melted fat. Filter through cloth to remove solids.
4. Press the cracklings (solid residue) in a screw press to extract remaining fat.
5. Yield: 70-85% of raw fat weight. Melting point: 40-45°C. At room temperature: semi-solid, waxy.

**[Lard](../glossary/lard.md)** (pig fat):
1. Same rendering process as tallow.
2. Lower melting point (33-40°C). Softer, more fluid at room temperature. Preferred for lighter lubrication duties.

**Clarification** (essential for lubricant use):
1. Re-melt fat, add water, boil, then cool.
2. Impurities settle or float. Skim clean fat from the surface.
3. Repeat until clear. Impurities in lubricant fat are abrasive and accelerate wear.

**Properties**: Melting point 33-45°C (tallow higher, lard lower). Semi-solid to soft at room temperature. Effective boundary lubricant due to polar molecules that adsorb to metal surfaces. Viscosity drops sharply above melting point. Oxidizes over time (rancidity), becoming acidic and gummy. Shelf life: 6-12 months at room temperature, up to 2 years refrigerated.

**Safety & Handling**:

> **Safety warning**: Hot fat at 80-100°C causes severe splash burns. Never add water to hot fat, which causes violent spattering and steam eruption. Wear long gloves and face shield when handling hot oil. Pour slowly to minimize splashing.

Rancid fat has an unpleasant odor but is not hazardous for lubricant use. The acidity increases slightly, which can promote corrosion on ferrous metals. Store in sealed containers in a cool, dark place to delay rancidity. If fat smells strongly of decomposition or has visible mold, discard it.

**Applications**: Slow-speed plain bearings, slides and ways on early machine tools, cart and wagon wheel hubs, leather gasket lubrication, thread cutting lubricant for hand tapping. Tallow is the traditional lubricant for clocks and precision instruments in pre-industrial contexts.

**Strengths**:
- Available from day one with no industrial infrastructure
- Excellent boundary lubrication from polar fatty acid molecules
- Simple rendering process requires only a pot, water, and heat
- Can be thickened with lime to make basic grease

**Weaknesses**:
- Limited temperature range: melts at 33-45°C, so bearings that run warm will thin the fat excessively
- Oxidizes and becomes rancid within 6-12 months
- Low viscosity when melted limits use to slow-speed, light-load applications
- Not suitable for high-speed bearings or continuous operation at elevated temperature
- Attracts vermin and insects in storage

---

### Vegetable Oils

**Composition**: Triglycerides (glycerol + 3 fatty acid chains). Good lubricity from polar molecules that adhere to metal surfaces. Viscosity varies significantly by oil type. All vegetable oils oxidize over time (rancidity), becoming acidic and gummy. Store cool, dark, and sealed. Add antioxidants if available.

**Prerequisites**:
- Oilseed crops (flax, rapeseed, castor, olive, sunflower) or nut/seed supply
- Screw press or wedge press for oil extraction
- Filter cloth for straining
- Storage containers (sealed, opaque preferred)

**Materials**:
- Oilseeds (varies by oil type, see below)
- Water for washing

**Production**:

**Cold pressing**:
1. Crush oilseeds in screw press or wedge press at room temperature.
2. Oil is expressed and collected. Cake (pressed seed residue) may be re-pressed warm for additional yield.
3. Filter through cloth to remove solids.
4. Cold pressing produces lighter, higher-quality oil with fewer free fatty acids.

**Hot pressing**:
1. Heat seeds to 80-100°C before pressing.
2. Higher yield (more oil released from heat-softened cells) but darker oil with more free fatty acids, lower quality, shorter shelf life.

**Key vegetable oils**:

- **Castor oil**: Press castor beans. Very high viscosity (~250 cSt at 40°C, roughly 100x olive oil). Excellent for high-speed, high-temperature applications. The ricinoleic acid content gives superior film strength. Used as engine lubricant in early aviation and racing (Castrol originally stood for "castor oil").
- **Rapeseed oil (canola)**: Moderate viscosity (~35 cSt at 40°C). Good general-purpose lubricant. Widely available in temperate climates. The basis for many biodegradable hydraulic fluids.
- **Olive oil**: Moderate viscosity (~40 cSt at 40°C). Good lubricity. Available in Mediterranean climates. One of the earliest lubricants used in antiquity.
- **[Linseed oil](../glossary/linseed-oil.md)** (flax seed oil): Drying oil. Polymerizes on exposure to air (oxidation cross-links fatty acid chains into a solid film). NOT suitable for lubrication (it hardens). Used for: paint binder (oil paint = linseed oil + pigment), wood finishing, putty (linseed oil + chalk), protective coatings on metal (thin film inhibits rust). Boiled linseed oil (heated with metallic driers such as manganese or cobalt salts) dries faster, in hours instead of days.
- **Sunflower oil**: Moderate viscosity (~30 cSt at 40°C). Similar to rapeseed. Available from a widely grown crop.

**Properties**: Vegetable oils have higher viscosity index than mineral oils (viscosity changes less with temperature). Good lubricity from polar ester groups. Flash point typically 250-320°C. Pour point typically -10 to -20°C (castor oil much higher, around -20 to -10°C). Oxidative stability is the primary weakness: double bonds in unsaturated fatty acids react with oxygen, producing acids, peroxides, and polymers that thicken the oil and deposit gum.

**Safety & Handling**:

> **Safety warning**: Vegetable oil fires burn vigorously. Use sand, fire blanket, or smother with lid. NEVER use water on an oil fire. Press cake residue from hot pressing can spontaneously combust if stored in large piles while warm. Spread thin to cool before storing.

Rancid vegetable oil develops a characteristic sharp odor. For lubricant use, rancidity increases acidity (promotes corrosion) and viscosity (oil thickens). Check acidity before using old oil. Store in sealed, opaque containers away from heat and sunlight.

**Applications**: Moderate-speed plain bearings, cutting fluid base, hydraulic fluid base (rapeseed), high-speed bearings (castor oil), leather lubrication, rust preventative coatings.

**Strengths**:
- Good boundary lubrication from polar fatty acid molecules
- Higher viscosity index than mineral oils (more stable viscosity across temperature range)
- Castor oil provides exceptional film strength for high-speed applications
- Renewable resource, biodegradable
- Available from first harvest of oilseed crops

**Weaknesses**:
- Poor oxidative stability: rancidity limits shelf life to 1-2 years
- Acidic breakdown products corrode metals
- Polymerization (especially linseed) makes some oils unsuitable for lubrication
- Limited low-temperature performance compared to mineral oils
- Viscosity range is narrower than what mineral oils offer

---

## Tier 2: Processed Lubricants (Years 5-20)

### Grease Production

**Composition**: Base oil (70-90%) + thickener (5-25%) + additives (0-10%). The thickener turns liquid oil into a semi-solid that stays in place and does not drain out of bearings.

**Prerequisites**:
- Base oil (mineral oil, vegetable oil, or animal fat)
- Alkali for saponification: NaOH (sodium hydroxide), Ca(OH)₂ (calcium hydroxide, slaked lime), or LiOH (lithium hydroxide)
- Heated vessel with stirrer (iron or steel)
- Roller mill or colloid mill for homogenizing
- [Soap making](../glossary/soap-making.md) capability (saponification: fat/oil + alkali → soap + glycerol)

**Materials**:
- Base oil (mineral or vegetable)
- Fat (tallow, lard, or vegetable oil) for saponification
- Alkali (NaOH, Ca(OH)₂, or LiOH)
- Additives (optional): graphite, molybdenum disulfide (MoS₂), zinc dialkyldithiophosphate (ZDDP)

**Manufacture**:

**Soap thickeners**:

- **Sodium soap (NaOH + fat)**: Sodium stearate. Water-soluble grease. NOT water-resistant. For general-purpose applications and open gears where low cost matters. Melts at ~150°C.
- **Calcium soap (Ca(OH)₂ + fat)**: Calcium stearate. Water-resistant (insoluble). The most common grease thickener historically. "Lime soap" grease. Dropping point ~90°C (relatively low; grease softens and runs at high temperature). For wheel bearings, water pumps, and marine applications.
- **Lithium soap (LiOH + fat)**: Lithium stearate. Water-resistant AND higher dropping point (~190°C). Multi-purpose grease: a single grease type covers most applications. The modern standard. Requires LiOH (from lithium ore: lepidolite or spodumene, roasted with CaO, leached with water, electrolyzed to produce LiOH). Lithium is less common than sodium or calcium, so save lithium grease for applications requiring both water resistance and high temperature.

**Grease making process**:
1. Heat base oil to 80-100°C in a heated vessel.
2. Add alkali (NaOH, Ca(OH)₂, or LiOH) and fat simultaneously. Saponification occurs.
3. Stir and heat to 150-200°C (depending on soap type) to complete saponification and drive off water.
4. Cool slowly while stirring. Mill the product (pass through roller mill or colloid mill) to homogenize texture and break up soap fibers.
5. Add additives (graphite, MoS₂, ZDDP) if required. Mix thoroughly.
6. Test: penetration (cone penetration test measures how far a standardized cone sinks into grease at 25°C, giving the NLGI grade: 000 = very soft, 2 = typical bearing grease, 6 = very hard). Dropping point (heat until grease melts and drips, giving the maximum usable temperature).

**[Clay-thickened grease](../glossary/clay-thickened-grease.md)** (non-soap):
- Bentonite clay (organically modified with quaternary ammonium salts to make it oil-compatible) + base oil. No dropping point (clay does not melt), usable to 250°C+. For high-temperature applications where soap grease fails. Simpler to make than lithium grease if bentonite clay is available.

**Properties**: NLGI grades from 000 (fluid) to 6 (hard block). Dropping point ranges from 90°C (calcium soap) to 190°C (lithium soap) to 250°C+ (clay). Grease stays in place in bearings that would drain oil, provides sealing against contamination, and allows simplified housing design (no oil reservoir needed).

**Safety & Handling**:

> **Safety warning**: Caustic soda (NaOH and KOH) causes severe chemical burns and permanent eye damage. Wear chemical splash goggles, rubber gloves, and a rubber apron when handling caustics. Have an eye wash station within 10 seconds of the work area. If caustic contacts skin, flush immediately with copious water for at least 15 minutes.

The saponification reaction is exothermic. Add alkali gradually to avoid violent foaming and splashing of hot caustic. Work in a well-ventilated area. Molten grease at 150-200°C causes severe burns. Use appropriate heat protection when handling hot vessels.

**Applications**: Rolling element bearings (grease-packed), wheel bearings, open gears, chassis lubrication points, water pump bearings, marine equipment (calcium or lithium soap), high-temperature bearings (clay-thickened).

**Strengths**:
- Stays in place; does not drain from bearings like liquid oil
- Lithium grease is multi-purpose, covering most applications with a single product
- Calcium soap provides water resistance for marine and pump applications
- Additives (MoS₂, graphite) extend performance into extreme pressure and temperature regimes
- Simplifies bearing housing design (no oil reservoir, seals, or return plumbing needed)

**Weaknesses**:
- Lithium supply chain depends on rare ore (spodumene/lepidolite)
- Dropping point limits soap greases to ~190°C maximum (calcium only ~90°C)
- Over-greasing bearings causes churning and overheating
- Grease cannot be filtered and reused like oil; it is consumed and replaced
- Additives are consumed during service; grease gradually degrades in use

---

### Solid Lubricants

**Principle**: Solid materials with layered crystal structures or low-shear-strength surfaces provide lubrication by allowing easy sliding between atomic layers. Used where liquid lubricants fail: extreme temperatures, vacuum, radiation, or environments where oil would contaminate the product.

**Prerequisites**:
- Varies by material (see individual entries below)

**Materials**:
- Graphite (natural or synthetic)
- Molybdenum disulfide (MoS₂, mined or synthesized)
- PTFE (polytetrafluoroethylene, synthesized from tetrafluoroethylene)
- Polymer stock (acetal, nylon, UHMWPE)

**Individual materials**:

**Graphite**: Layered carbon structure. Weak van der Waals forces between layers allow easy shear. Effective in air (adsorbed water film aids layer sliding) but poor in vacuum or dry environments. Withstands temperatures to 450°C in air (oxidizes above this). Used in packings, gaskets, high-temperature bearings, lock mechanisms, and mold release agents. Applied as powder, dispersion in oil or grease ("graphited grease"), or bonded coating (graphite + sodium silicate binder).

**Molybdenum disulfide (MoS₂)**: Similar layered structure to graphite but effective in vacuum and dry environments, making it the dominant solid lubricant for space applications. Coefficient of friction: 0.02-0.1. Temperature range: -180 to +350°C in air (oxidizes to MoO₃ above 350°C), up to 800°C in vacuum. Applied by burnishing (rubbing powder into the surface), sputtering (PVD thin film 0.5-2 μm), or bonded coating (MoS₂ + epoxy/phenolic binder + solvent). MoS₂ coatings are standard for spacecraft mechanisms, satellite deployment hinges, and vacuum-chamber bearings.

**PTFE (Teflon)**: Polytetrafluoroethylene. Ultra-low coefficient of friction (0.04-0.10). Chemically inert. Temperature range -200 to +260°C. Used as bearing liners, sliding plates (bridge expansion bearings), piston rings (non-lubricated compressors), and tape (thread sealing). Limitations: poor wear resistance (filled with glass fiber, bronze, or carbon to improve), creep under load ("cold flow"), and cannot be melt-processed like typical plastics (must be sintered from powder).

**Polymer bearings**: Acetal (Delrin), nylon, and ultra-high-molecular-weight polyethylene (UHMWPE) are self-lubricating, requiring no external lubricant. UHMWPE is used in artificial hip joints, conveyor wear strips, and marine bearings (water-lubricated). Nylon suits gear wheels, low-load bearings, and sprockets. Acetal serves in precision gears, valve seats, and food-processing bearings (no lubricant contamination of product).

**Safety & Handling**:

> **Safety warning**: MoS₂ and graphite dust are respiratory irritants. Use dust masks when handling fine powders. PTFE decomposes above 350°C, releasing toxic fumes including hydrogen fluoride and perfluoroisobutylene. Never heat PTFE above 260°C. Use local exhaust ventilation if PTFE components are machined or heated.

**Applications**: High-temperature bearings, vacuum mechanisms, space applications, lock mechanisms, food processing (polymer bearings), bridge bearings (PTFE sliding plates), mold release (graphite).

**Strengths**:
- Effective at extreme temperatures where liquid lubricants fail
- MoS₂ works in vacuum (unlike graphite)
- PTFE and polymer bearings need no external lubricant supply
- Solid lubricants do not evaporate, drip, or drain away
- Compatible with cleanroom and food-contact applications

**Weaknesses**:
- Limited replenishment: solid films wear through and must be reapplied
- Graphite ineffective in vacuum or dry environments
- PTFE has poor wear resistance and cold-flows under load
- Polymer bearings limited to low PV values (see Bearing Design Parameters)
- MoS₂ and PTFE require industrial synthesis (not available at early bootstrap stages)

---

### Cutting Fluids

**Principle**: Cutting fluids serve four functions simultaneously: lubricate the chip-tool interface (reduce cutting force, improve surface finish), cool the tool and workpiece (remove heat, the primary function), flush chips from the cutting zone, and prevent rust on the workpiece and machine.

**Prerequisites**:
- Base oil (mineral, lard, or vegetable) or chemical lubricant base
- Emulsifier (for soluble oil): sulfonate or soap
- Biocide (for emulsions): prevents bacterial growth
- Pump, sump tank, hose, and nozzle (for flood coolant)
- Filter (mesh or paper) for chip removal

**Materials**:
- Mineral oil or lard oil (for straight oil)
- Mineral oil + emulsifier (for soluble oil)
- Chemical lubricants (for synthetic fluid)
- Water (for emulsion and synthetic types)

**Types and Production**:

**Straight cutting oil**: Mineral oil or lard oil, undiluted. Best lubrication, poorest cooling (low heat capacity). Used for tapping, threading, broaching, and heavy turning where lubrication matters more than cooling. Can be enhanced with sulfur or chlorine compounds (extreme pressure additives that react with the metal surface at high temperature to form a solid lubricating film, preventing welding of chip to tool).

**Soluble oil (emulsion)**: Mineral oil + emulsifier (sulfonate or soap) + water. Mix 5-10% oil in water by volume. Milky white emulsion. Water provides excellent cooling (high heat capacity); oil provides lubrication and rust protection. This is the most common cutting fluid for general machining. Replace regularly because bacteria grow in the emulsion, causing a rancid smell and skin irritation. Add biocide to extend sump life.

**Synthetic cutting fluid**: Water + chemical lubricants (no mineral oil). Clear or tinted. Best cooling, good rust protection, longest sump life. More expensive. Used for grinding (where maximum cooling and clean fluid are needed) and high-speed machining.

**Application methods**:

- **Flood coolant**: Pump fluid from sump tank through hose/nozzle, direct at cutting zone. Flow rate 5-20 liters/minute. Most common method. Filter fluid (mesh or paper filter) to remove chips and fines. Settle tank allows chips to settle before recirculation.
- **Mist coolant**: Atomize fluid into fine spray using compressed air. Lower volume, less mess. For operations where flood is impractical.
- **Manual application**: Brush or squeeze bottle. For intermittent cutting, hand operations, and small jobs.

**Properties**: Straight oil: excellent lubricity, flash point 150-200°C, poor cooling. Emulsion: good balance of cooling and lubrication, 5-10% concentration, milky appearance, limited sump life (3-6 months with biocide). Synthetic: best cooling, clear appearance, longest sump life, highest cost.

**Safety & Handling**:

> **Safety warning**: Oil mist from mist coolant systems is a respiratory hazard. Inhaled oil mist can cause lipoid pneumonia and chronic respiratory irritation. Use mist coolant only with adequate ventilation or enclosure with mist extraction. Bacteria in soluble oil emulsions cause skin irritation and rancid odors. Monitor emulsion pH weekly; a drop below 8.5 indicates bacterial growth. Sulfureted (sulfurized) cutting oils cause skin irritation with prolonged contact.

**Applications**: General machining (emulsion), tapping and threading (straight oil), grinding (synthetic), broaching (straight oil with EP additives), hand operations (manual application).

**Strengths**:
- Soluble oil emulsion provides the best balance of cooling and lubrication for general machining
- Straight oil excels at lubrication for difficult cutting operations
- Synthetic fluids offer the longest sump life and best cooling for grinding
- Flood coolant is simple to implement and effective for most operations

**Weaknesses**:
- Emulsions require regular maintenance (biocide addition, pH monitoring, periodic replacement)
- Oil mist from coolant systems is a respiratory hazard
- Straight oil creates slippery floors and fire risk
- Disposal of used cutting fluid requires treatment (break emulsion, separate oil and water phases)
- Bacterial growth in emulsions limits practical sump life to 3-6 months

---

## Tier 3: Industrial Fluids (Years 20-50)

### Mineral Oil Lubricants

**Composition**: Refined petroleum oil from fractional distillation. Hydrocarbon mixtures (paraffinic, naphthenic, or aromatic) selected and treated for lubricant service. The workhorse of industrial lubrication, displacing animal and vegetable oils for most applications due to better oxidation stability, wider viscosity range, and consistent quality.

**Prerequisites**:
- [Petroleum distillation](petroleum-alternatives.md) capability
- Solvent refining or acid treating for quality improvement
- Additive manufacturing capability (ZDDP, antioxidants, rust inhibitors)

**Materials**:
- Crude petroleum or oil shale
- Solvents for refining (if available)

**Production**:

1. **Distill** crude petroleum to collect lubricant boiling range fractions (typically 350-500°C boiling range, heavier than diesel and lighter than bitumen).
2. **Refine** the distillate to remove aromatics, sulfur, and nitrogen compounds. Methods include solvent extraction (furfural or phenol removes aromatics), acid treating (sulfuric acid removes unstable compounds), and hydrofinishing (hydrogenation removes sulfur and nitrogen, saturates aromatics).
3. **Dewax** (if paraffinic base) to lower the pour point. Mix with methyl ethyl ketone (MEK) solvent, chill to -20°C, filter wax crystals. The wax-free oil has a lower pour point and flows at colder temperatures.
4. **Blend** to target viscosity by mixing distillate fractions. Add viscosity index improvers (polymer additives that thicken oil more at high temperature than at low temperature) for multi-grade oils.
5. **Add additives**: anti-wear agents (ZDDP: zinc dialkyldithiophosphate, forms protective film on metal surfaces under boundary conditions), antioxidants (prevent oxidation, extend oil life), rust inhibitors (form protective film on metal, prevent corrosion from moisture), anti-foam agents (silicone compounds that prevent foam formation in circulating systems), and detergents/dispersants (keep sludge and varnish suspended in the oil so they drain out with oil changes rather than depositing on surfaces).

**Viscosity grading**:

**ISO VG system** (industrial oils, viscosity at 40°C): ISO VG 32 (32 cSt, light spindle oil), ISO VG 46 (46 cSt, general hydraulic oil), ISO VG 68 (68 cSt, general machine oil), ISO VG 100 (100 cSt, light gear oil), ISO VG 150 (150 cSt, medium gear oil), ISO VG 220 (220 cSt, gear oil), ISO VG 320 (320 cSt, heavy gear oil), ISO VG 460 (460 cSt, extra-heavy gear oil). Each grade has ±10% tolerance.

**SAE viscosity grades** (engine oils, viscosity at 100°C): SAE 30 (9.3-12.5 cSt at 100°C, general-purpose engine oil for moderate climate), SAE 40 (12.5-16.3 cSt at 100°C, heavy-duty engine oil for hot climate). Multi-grade oils: SAE 10W-30 has a 10W winter rating (meets cold-cranking requirements at -25°C) and SAE 30 hot rating. Higher viscosity grades provide thicker films for heavier loads but increase viscous friction and heat generation. Select the lowest viscosity that maintains adequate film thickness under operating conditions.

**Properties**: Flash point typically 180-240°C (varies with grade). Pour point -10 to -30°C (paraffinic oils) or -40°C (naphthenic oils). Viscosity index 95-105 (conventional mineral oil) to 130+ (with VI improvers). Good oxidation stability (2-5x better than vegetable oils). Compatible with most seal materials (nitrile rubber, viton). Shelf life: 5+ years if uncontaminated and sealed.

**Safety & Handling**:

> **Safety warning**: Mineral oil at operating temperature (60-80°C in running machinery) can cause burns. Oil fires burn vigorously. NEVER use water on an oil fire; use sand, fire blanket, or smother with lid. Used mineral oil is an environmental contaminant and must not be dumped on ground or in waterways.

**Applications**: Every industrial application that needs lubrication: bearings, gears, hydraulic systems, engines, compressors, turbines. ISO VG 32 and 46 dominate general machinery. ISO VG 68-220 cover gear applications. SAE grades cover internal combustion engines.

**Strengths**:
- Better oxidation stability than animal or vegetable oils (longer service life)
- Available in a wide range of viscosity grades for every application
- Compatible with standard seal and bearing materials
- Can be re-refined (vacuum distillation removes contaminants, additives replenished)
- Additive technology tailors performance for specific applications

**Weaknesses**:
- Requires petroleum distillation infrastructure
- Petroleum is a finite resource
- Some additive compounds (ZDDP) contain heavy metals with environmental concerns
- Mineral oils are not biodegradable; spills persist in the environment
- Pour point limits cold-weather use without heaters or low-viscosity grades

---

### Hydraulic Fluids

**Principle**: Hydraulic systems transmit force through incompressible fluid. The fluid must transmit force efficiently (incompressible), flow readily through valves and pumps (correct viscosity), resist chemical degradation (no oxidation, no corrosion), and be compatible with seals (does not swell or shrink rubber or leather). Fire resistance is desirable but not always achievable.

**Prerequisites**:
- Fluid supply (vegetable oil, mineral oil, or water-glycol mixture)
- Seals compatible with the chosen fluid (rubber, leather, or polymeric)
- Filtration capability (10-25 μm absolute for return line)

**Materials**:
- Varies by fluid type (see below)

**Fluid types**:

**Vegetable oil-based**: Rapeseed or castor oil. Biodegradable with good lubricity. Limited temperature range: thickens when cold, thins when hot. Oxidizes over time. Suitable for the Metallurgy-Machine Tools stage transition hydraulic presses, where petroleum is not yet available.

**Mineral oil-based**: Refined petroleum oil (see [Petrochemicals](petroleum-alternatives.md)). ISO VG 32 or 46 most common. Contains anti-wear agents (ZDDP), antioxidants, rust inhibitors, and anti-foam agents. Operating temperature range -10°C to +70°C. The most common hydraulic fluid in industrial use.

**[Water-glycol](../glossary/water-glycol.md)** (fire-resistant): Water + glycol (40-60%) + thickener + additives. Fire-resistant due to water content. Lower lubricity than oil, so harder pump and valve materials are needed. Used in locations with fire risk (furnaces, welding areas, foundries).

**Hydraulic system design**:

Pump (gear pump: 10-200 bar, or piston pump: 200-400 bar) feeds control valves (directional, pressure relief, flow control), which direct fluid to actuators (cylinder for linear motion, motor for rotary). Return line carries fluid back to reservoir. A filter in the return line (10-25 μm absolute) removes contaminants, the primary cause of hydraulic system failure. The reservoir holds 2-3x the pump flow rate capacity, allowing fluid time to de-aerate and settle.

**Properties**: Mineral oil hydraulic fluid: ISO VG 32-46, flash point 180-200°C, operating range -10°C to +70°C. Vegetable oil: similar viscosity but narrower temperature range and shorter service life. Water-glycol: non-flammable, lower lubricity, limited to moderate pressure systems.

**Safety & Handling**:

> **Safety warning**: High-pressure hydraulic fluid (200-400 bar) can inject through skin from a pinhole leak, causing catastrophic tissue damage that may require amputation. Never search for leaks with bare hands; use a piece of cardboard or paper. Mineral oil hydraulic fluid is flammable; a leak onto a hot surface can ignite. Water-glycol fluids reduce fire risk but are toxic if ingested.

**Applications**: Hydraulic presses for metalworking, machine tool hydraulics, hydraulic jacks and lifts, construction equipment, aircraft hydraulic systems.

**Strengths**:
- Mineral oil fluid provides excellent lubrication, corrosion protection, and wide temperature range
- Vegetable oil fluid is biodegradable and available before petroleum
- Water-glycol provides fire resistance for hazardous locations
- Hydraulic systems deliver high force with precise control

**Weaknesses**:
- Contamination is the primary failure mode; filtration is critical and often neglected
- Mineral oil fluid is flammable; leaks onto hot surfaces can ignite
- High-pressure injection injuries are severe and often underestimated
- Vegetable oil fluid oxidizes and has a short service life
- Water-glycol has poor lubricity, requiring harder pump components

---

### Bearing Lubrication Methods

**Principle**: The method of delivering lubricant to a bearing is as important as the lubricant itself. Different bearing types and operating conditions require different lubrication approaches, ranging from simple self-contained systems to complex forced-circulation designs.

**Prerequisites**:
- Appropriate lubricant (oil or grease, matched to bearing type and speed)
- Bearing housing with lubricant reservoir or grease cavity
- For forced systems: pump, filter, and plumbing

**Lubrication methods**:

**Plain (journal) bearings**:

- **Oil-ring lubrication**: A brass or steel ring (20-40 mm diameter) rides on the shaft and dips into an oil reservoir below the bearing. Shaft rotation carries the ring, which drags oil up to the shaft top. Oil flows along the shaft into the bearing. Continuous, automatic, and self-contained. For horizontal shafts at moderate speed (100-3000 RPM).
- **Wick lubrication**: A felt or cotton wick submerged in an oil reservoir contacts the shaft or bearing surface. Capillary action draws oil to the bearing. Low flow rate, suitable for light-duty bearings. Quiet and simple.
- **Splash lubrication**: A gear or rotating element in an oil bath throws oil onto the bearing. Common in gearboxes where no separate oiling system is needed. Oil level: gears dip 1-2 tooth depths.
- **Forced lubrication**: A gear pump draws oil from a reservoir, forces it through a filter, and delivers it to the bearing under pressure (0.1-0.5 MPa). Oil flows through the bearing and drains back to the reservoir. Provides positive, controlled oil supply regardless of speed. Essential for high-speed or heavily loaded bearings such as steam turbine bearings and large generators.

**Rolling element bearings**:

- **Grease-packed**: Fill bearing cavity 30-50% with grease (do not overfill; churning generates heat). Grease lasts months to years depending on speed and temperature. Sealed bearings (rubber seals) retain grease for life. Shielded bearings (metal shields) allow some grease exchange.
- **Oil mist lubrication**: Atomize oil with compressed air and pipe the mist to the bearing. Provides continuous fine lubrication. Excellent for high-speed spindle bearings. Requires clean, dry compressed air.

#### Bearing Design Parameters for Bootstrap Machinery

**Bearing PV limits**: The product of bearing pressure P (MPa) and surface velocity V (m/s) determines the heat generation rate in plain bearings. Each bearing material has a maximum PV rating: bronze (phosphor bronze) 1.75 MPa·m/s, Babbitt metal 1.05 MPa·m/s, PTFE (unfilled) 0.35 MPa·m/s, acetal (Delrin) 0.15 MPa·m/s, nylon 0.10 MPa·m/s. Exceeding the PV limit causes rapid temperature rise, lubricant breakdown, and bearing failure. For applications above the PV limit, use rolling element bearings (which have much higher speed/load capability) or provide forced lubrication with external cooling.

**Bearing clearance design**: Journal bearing radial clearance (difference between housing bore and shaft diameter) must accommodate thermal expansion, lubricant film thickness, and manufacturing tolerances. Rule of thumb: 0.001 × shaft diameter (e.g., 50 mm shaft = 0.05 mm radial clearance). Tight clearance reduces vibration and improves positional accuracy but increases friction and risk of seizure if temperature rises. Loose clearance allows more oil flow and better cooling, tolerates misalignment, but permits vibration. Length-to-diameter ratio (L/D) of 0.5-1.5 is typical. Shorter bearings (L/D < 1) run cooler and tolerate misalignment; longer bearings (L/D > 1) carry more load.

**Oil selection for bootstrap machinery**: For a bootstrap workshop without access to refined petroleum products, the practical lubricant sequence is: (1) rendered animal fat (tallow/lard) for slow-speed plain bearings and sliding surfaces; (2) vegetable oil (rapeseed, castor) for moderate-speed bearings and cutting fluid base; (3) clarified tallow + lime soap grease for wheel bearings and open gears. As refining capability develops, mineral oil from petroleum distillation replaces vegetable and animal oils for most applications due to better oxidation stability and wider viscosity range. The viscosity grade is selected by the Sommerfeld number calculation: for a 50 mm shaft at 1500 RPM carrying 500 N radial load, ISO VG 32 provides adequate film; for the same shaft at 300 RPM, ISO VG 68 is needed. In cold climates (below -10°C startup), use the lowest viscosity that still provides adequate film at operating temperature, or pre-heat the oil with a waste-heat system before starting machinery.

**Safety & Handling**:

> **Safety warning**: Oil mist lubrication systems generate airborne oil particles that are a respiratory hazard. Enclose mist-lubricated bearings where possible and provide local exhaust ventilation. Forced lubrication systems operate under pressure; check fittings and lines for leaks before each shift.

**Applications**: Every rotating and sliding machine element. Oil-ring for horizontal shafts in pumps and fans. Wick for light-duty instrument bearings. Splash for enclosed gearboxes. Forced for turbines and large generators. Grease-packed for rolling element bearings in motors, wheels, and machine tools. Oil mist for high-speed spindle bearings.

**Strengths**:
- Oil-ring and wick systems are self-contained and require no external pump
- Forced lubrication provides reliable oil supply at any speed
- Grease-packed bearings simplify housing design and maintenance
- Splash lubrication is the simplest approach for gearboxes

**Weaknesses**:
- Oil-ring and wick systems fail at very low speeds (not enough oil delivery) and very high speeds (ring cannot keep up)
- Forced lubrication adds complexity (pump, filter, plumbing) and a potential failure point
- Grease-packed bearings have limited speed capability due to churning heat
- Oil mist requires clean, dry compressed air and creates a respiratory hazard

---

## Tier 4: Advanced & Specialty Lubricants (Years 50-200+)

### Synthetic Lubricants

**Composition**: Engineered hydrocarbon or non-hydrocarbon molecules with uniform structure, produced by chemical synthesis rather than petroleum distillation. The uniform molecular weight distribution (no light or heavy fractions) gives synthetics advantages in temperature range, oxidation stability, and consistency.

**Prerequisites**:
- Advanced chemical synthesis capability
- Specific precursor chemicals (varies by type)
- Controlled reaction conditions (temperature, pressure, catalysts)

**Materials**:
- Varies by synthetic type (see below)

**Types and Manufacture**:

**Polyalphaolefin (PAO)**: Hydrocarbon synthetic made by oligomerizing α-olefins (primarily decene, C₁₀) with BF₃ catalyst, then hydrogenating. Uniform molecular weight distribution gives: better low-temperature fluidity (pour point -50 to -65°C vs -15°C for mineral oil), higher viscosity index (130-150 vs 95-105), and better oxidation stability (2-3x longer oil life). Used in jet engine oils, Arctic machinery, and long-drain automotive oils.

**Ester oils**: Diesters and polyol esters, synthesized from organic acids and alcohols. Excellent lubricity (polar ester groups adsorb strongly to metal surfaces), good thermal stability (200-250°C continuous), and biodegradable. Used in jet engine oils (MIL-PRF-23699), compressor oils, biodegradable hydraulic fluids (forestry, marine), and two-stroke engine oils.

**Silicone oils**: Polydimethylsiloxane (PDMS), made from silicon + methyl chloride chemistry. Extremely wide temperature range (-70 to +250°C), chemically inert, and excellent dielectric properties. Poor lubricity for metal-on-metal (low load-carrying capacity). Used where temperature stability or chemical inertness matters more than extreme pressure performance: diffusion pump fluids, dashpot dampers, electrical insulation, mold release, and medical devices.

**Perfluoropolyether (PFPE)**: Fluorinated synthetic, the most chemically resistant lubricant. Inert to oxygen, fuels, solvents, acids, and bases. Temperature range: -80 to +300°C. Ultra-low vapor pressure, meaning no outgassing in vacuum. Used in spacecraft mechanisms, semiconductor manufacturing equipment, oxygen compressors (mineral oil + high-pressure O₂ = explosion risk), and chemical processing valves.

**Properties**: PAO: pour point -50 to -65°C, VI 130-150, 2-3x mineral oil oxidation life. Ester: 200-250°C thermal stability, biodegradable. Silicone: -70 to +250°C, chemically inert, poor metal-on-metal lubricity. PFPE: -80 to +300°C, chemically inert, ultra-low vapor pressure.

**Safety & Handling**:

> **Safety warning**: PFPE decomposes above 300°C, releasing toxic fluorinated compounds. Silicone oils are not readily biodegradable. PAO and ester oils have good fire safety profiles (high flash points). Handle all synthetic lubricants according to the manufacturer's safety data, which varies significantly by chemistry.

**Applications**: Jet engines (PAO, ester), Arctic machinery (PAO), biodegradable hydraulic systems (ester), diffusion pumps (silicone), spacecraft mechanisms (PFPE), semiconductor equipment (PFPE), oxygen service (PFPE), electrical insulation (silicone).

**Strengths**:
- Wider operating temperature range than mineral oils
- Better oxidation stability and longer service life
- PAO and ester oils provide excellent lubrication for demanding applications
- PFPE is chemically inert, critical for oxygen service and reactive chemical environments
- Ester oils are biodegradable, suitable for environmentally sensitive applications

**Weaknesses**:
- Significantly more expensive than mineral oils (3-10x cost)
- Require advanced chemical synthesis infrastructure
- Silicone oils have poor load-carrying capacity for metal-on-metal applications
- PFPE requires fluorine chemistry (hazardous, specialized)
- Some synthetics are incompatible with seals and paints designed for mineral oil

---

### Vacuum Oils

**Principle**: Vacuum pump oils must have extremely low vapor pressure (<10⁻⁴ Pa at operating temperature). If the oil has high vapor pressure, it evaporates into the vacuum chamber, contaminating the vacuum and preventing the system from reaching low pressure. The oils must also lubricate pump bearings and seals adequately, resist oxidation, and not react with pumped gases.

**Prerequisites**:
- Vacuum pump system (rotary vane, piston, or diffusion pump)
- Oil with appropriate vapor pressure for the target vacuum level

**Materials**:
- Highly refined mineral oil, silicone oil, or synthetic hydrocarbon (PAO)

**Types**:

**Mineral vacuum oil**: Highly refined, distilled mineral oil with narrow boiling range. Achieves ultimate vacuum ~10⁻² to 10⁻³ Pa. Used in mechanical roughing pumps (rotary vane, piston).

**Silicone vacuum oil**: Polydimethylsiloxane (PDMS), from silicon + methyl chloride chemistry. Very low vapor pressure (~10⁻⁶ Pa at 25°C). Chemically inert. Used in diffusion pumps (see Vacuum & Optics), achieving ultimate vacuum ~10⁻⁶ to 10⁻⁸ Pa.

**Synthetic hydrocarbon oil**: Polyalphaolefin (PAO). Low vapor pressure, excellent lubricity, wide temperature range. Used in high-performance mechanical pumps.

**[Oil purification](../glossary/oil-purification.md)** (for extending vacuum oil life):
- **Filtration**: Pass oil through 1-5 μm filter to remove particulates.
- **Degassing**: Heat oil under vacuum to remove dissolved gases and volatile contaminants.
- **Adsorption**: Pass through activated alumina or molecular sieve to remove acidic and polar contaminants.

**Properties**: Mineral vacuum oil: vapor pressure 10⁻² to 10⁻³ Pa at 25°C. Silicone vacuum oil: vapor pressure ~10⁻⁶ Pa at 25°C. PAO: intermediate vapor pressure, excellent lubricity.

**Safety & Handling**:

> **Safety warning**: Vacuum pump oil that has been exposed to reactive gases (solvents, acids, oxidizers) may be contaminated and hazardous. Drain and replace oil after pumping reactive or corrosive gases. Used vacuum oil may contain dissolved process chemicals. Handle with gloves and eye protection.

**Applications**: Mechanical roughing pumps (mineral or PAO oil), diffusion pumps (silicone oil), vacuum distillation systems, vacuum drying ovens, semiconductor process equipment.

**Strengths**:
- Silicone vacuum oil achieves the lowest pressures for diffusion pumps
- Mineral vacuum oil is relatively inexpensive for roughing pump applications
- Oil purification extends service life and reduces operating costs
- PAO combines low vapor pressure with excellent lubrication

**Weaknesses**:
- Silicone oil has poor lubricity for mechanical pump bearings under heavy load
- All vacuum oils degrade with exposure to reactive gases and require periodic replacement
- Vacuum oil contamination is a common cause of vacuum system performance problems
- Silicone oil cannot be used in some applications because it contaminates surfaces (difficult to remove)

---

### Semiconductor/Cleanroom Lubricants

**Principle**: Equipment used in semiconductor fabrication requires lubricants that do not contaminate cleanroom air or wafer surfaces. The lubricants must exhibit low outgassing (minimal evaporation into the cleanroom environment), non-particulating behavior (no shedding of particles), and vacuum compatibility (for equipment inside vacuum chambers such as load locks and wafer transfer robots).

**Prerequisites**:
- Semiconductor chemistry capability
- Cleanroom manufacturing environment
- PFPE synthesis or procurement

**Materials**:
- Perfluoropolyether (PFPE) base stock
- Specialized thickener systems

**Production**:

[Cleanroom-compatible lubricants](../glossary/cleanroom-compatible-lubricants.md) are based on PFPE (perfluoropolyether) chemistry. PFPE greases use fluorinated thickeners compatible with cleanroom requirements. The synthesis requires HF + olefins under controlled conditions (semiconductor chemistry infrastructure). The result is an extremely inert lubricant with wide temperature range and ultra-low vapor pressure.

**Properties**: PFPE greases are chemically inert, electrically insulating, and compatible with most process gases. Ultra-low outgassing rates. Temperature range -80 to +300°C. Vapor pressure <10⁻¹⁰ Pa.

**Safety & Handling**:

> **Safety warning**: PFPE decomposes above 300°C, releasing toxic fluorinated decomposition products including hydrogen fluoride. Do not use PFPE lubricants on surfaces that may reach high temperatures during processing. Disposal of PFPE waste requires special handling due to persistence in the environment.

**Applications**: Crystal puller bearings, wafer handling robots, load lock mechanisms, photolithography stage bearings, vacuum chamber manipulators, and any mechanism operating inside a semiconductor cleanroom.

**Strengths**:
- Ultra-low outgassing protects wafer surfaces from contamination
- Chemically inert to all process gases used in semiconductor fabrication
- Wide temperature range suits diverse equipment
- Does not generate particles that would contaminate cleanroom air

**Weaknesses**:
- Extremely expensive (10-100x mineral oil lubricants)
- Requires semiconductor-grade chemistry infrastructure to produce
- Cannot be replaced with cheaper alternatives without risking contamination
- PFPE decomposition products are highly toxic

---

## Selection Guide

| Lubricant Type | Viscosity Range (cSt at 40°C) | Temperature Range | Load Capacity | Best Use |
|----------------|-------------------------------|-------------------|---------------|----------|
| Animal fat (tallow/lard) | Semi-solid to ~30 cSt (melted) | 10-60°C | Low to moderate | Slow-speed plain bearings, slides, cart wheels |
| Vegetable oil (rapeseed) | 30-40 cSt | -10 to +80°C | Low to moderate | General-purpose bearings, cutting fluid base |
| Castor oil | ~250 cSt | -10 to +120°C | Moderate to high | High-speed bearings, racing engines |
| Calcium soap grease | NLGI 1-3 | -20 to +90°C | Moderate | Wheel bearings, water pumps, marine equipment |
| Lithium soap grease | NLGI 1-3 | -30 to +190°C | Moderate to high | Multi-purpose: bearings, gears, chassis |
| Clay-thickened grease | NLGI 1-3 | -20 to +250°C | Moderate to high | High-temperature bearings, ovens, kilns |
| Straight cutting oil | 20-50 cSt | Ambient (recirculated) | High (chip-tool) | Tapping, threading, broaching |
| Soluble oil emulsion (5-10%) | ~1-5 cSt (mixed) | Ambient (recirculated) | Low to moderate | General machining, turning, milling |
| Mineral oil (ISO VG 32) | 32 cSt | -10 to +80°C | Moderate | Spindle oils, hydraulic fluid, general bearings |
| Mineral oil (ISO VG 68) | 68 cSt | -10 to +80°C | Moderate to high | General machine oil, moderate-speed gears |
| Mineral oil (ISO VG 220) | 220 cSt | 0 to +90°C | High | Gear oils, heavy-duty gearboxes |
| Hydraulic fluid (mineral) | 32-46 cSt | -10 to +70°C | Moderate to high | Hydraulic presses, machine tools |
| Water-glycol hydraulic fluid | 32-46 cSt | -20 to +60°C | Low to moderate | Fire-risk environments, foundries |
| PAO synthetic | 32-460 cSt | -50 to +175°C | High | Jet engines, Arctic machinery, long-drain oils |
| Ester synthetic | 32-100 cSt | -40 to +200°C | High | Jet engines, compressor oils, biodegradable hydraulics |
| Silicone oil | 10-100,000 cSt | -70 to +250°C | Low | Diffusion pumps, dampers, electrical insulation |
| PFPE | 20-500 cSt | -80 to +300°C | Moderate | Vacuum, semiconductor, oxygen service, spacecraft |
| MoS₂ (solid) | N/A | -180 to +350°C (air) | High (boundary) | Vacuum bearings, space mechanisms, extreme temperature |
| Graphite (solid) | N/A | Up to +450°C (air) | Moderate | High-temperature bearings, gaskets, mold release |
| PTFE (solid) | N/A | -200 to +260°C | Low | Bearing liners, bridge bearings, thread sealing |

---

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Foundations | Animal fat collection and rendering, basic axle grease for carts and simple machines |
| Metallurgy | Tallow-lubricated bearings for treadle lathes and bellows, vegetable oil extraction |
| Machine Tools | Cutting fluids and machine oils for precision machine tools, grease production |
| Energy | Cylinder oils for steam engines, high-temperature bearing lubrication, hydraulic fluid for presses |
| Chemistry | Chemical processing of oils, soap thickeners for grease, mineral oil refining, synthetic additives |
| Vacuum & Optics | Low-vapor-pressure oils for vacuum pump seals and diffusion pumps |
| Silicon | Ultraclean lubricants for crystal pullers and wafer handling equipment |
| Photolithography | Cleanroom-compatible lubricants and hydraulic fluids for fab equipment, PFPE greases |

---

## Key Deliverables

- **Tier 1** (Years 0-5): Rendered animal fat (tallow and lard) for slow-speed bearings and slides. Vegetable oil extraction from oilseed crops (rapeseed, castor, olive) for moderate-speed bearings. Linseed oil for protective coatings and paint binder. Basic lubrication practices: regular application, keeping lubricant clean, avoiding abrasive contamination. These natural lubricants suffice for the first workshops, treadle lathes, water wheels, and cart transport.

- **Tier 2** (Years 5-20): Grease production from saponification of fats with alkali (sodium, calcium, lithium soap thickeners). Cutting fluid formulations: soluble oil emulsion for general machining, straight oil for threading and tapping. Solid lubricants (graphite, MoS₂) for machine tool applications where liquid oil is impractical. These processed lubricants enable precision machine tools, threaded fastener production, and bearings that must operate under load for extended periods.

- **Tier 3** (Years 20-50): Mineral oil refining and viscosity grading (ISO VG system). Hydraulic fluid supply for presses and machine tools, transitioning from vegetable oil to mineral oil. Bearing lubrication engineering: PV limits, clearance design, and oil selection by Sommerfeld number. Additive technology (ZDDP, antioxidants, rust inhibitors) that tailors mineral oil performance for specific applications. These industrial fluids enable steam engines, high-speed machinery, hydraulic presses, and continuous-process equipment.

- **Tier 4** (Years 50-200+): Synthetic lubricants (PAO, ester, silicone) for demanding applications in aerospace and extreme environments. Vacuum-compatible oils (mineral for roughing pumps, silicone for diffusion pumps). Cleanroom-compatible PFPE lubricants for semiconductor manufacturing equipment. Oil analysis and condition monitoring programs for predictive maintenance. These advanced lubricants enable jet engines, vacuum systems, semiconductor fabrication, and space applications.

---

## General Safety & Hazards

- **Hot oil burns**: Lubricating oil at operating temperature can exceed 200°C. Severe splash burns result from contact. Wear face shields and long gloves when handling hot oil. Pour slowly to minimize splashing.
- **Oil fires**: NEVER use water on an oil fire. Water flashes to steam and scatters burning oil. Extinguish with sand, fire blanket, or smothering with a lid. Keep fire extinguishing materials near oil heating operations.
- **Oil mists**: Oil mist from machining operations and mist lubrication systems is a respiratory irritant. Prolonged inhalation can cause lipoid pneumonia. Use ventilation, mist extraction, or enclosures to control airborne oil.
- **Environmental disposal**: Used oil and grease must not be dumped on ground or in waterways. Collect in sealed containers. Re-refine mineral oils (vacuum distillation removes contaminants, additives are replenished). Animal and vegetable oils can be composted in small quantities. Used cutting fluid emulsions require treatment (break emulsion with acid or flocculant, separate oil phase, treat water phase before discharge). Even in a bootstrap economy, contaminating water supplies with oil has long-term consequences for agriculture and drinking water.

### Oil Analysis and Condition Monitoring

Industrial plants monitor lubricant condition to schedule oil changes based on actual condition rather than fixed intervals. Key tests:

1. **Viscosity**: Change >10% indicates oxidation, contamination, or wrong oil grade.
2. **Acid number**: Increase indicates oxidation. Acidic byproducts corrode bearings.
3. **Particle count**: ISO 4406 cleanliness code. Critical for hydraulic systems (target: 16/14/11 for servo valves).
4. **Spectrometric analysis**: ICP or atomic absorption detects wear metals (Fe, Cu, Pb, Sn, Cr) at ppm levels. Trending indicates which component is wearing.
5. **Water content**: Karl Fischer titration. Water causes rust, reduces film strength, and promotes microbial growth. Limits: <0.1% for most systems, <0.03% for turbine oils.

**Sampling**: Always sample from a live oil stream (not from the drain plug or static reservoir). Use clean sample bottles. Sample frequency: monthly for critical equipment (turbines, large gearboxes), quarterly for general plant equipment.

---

## Limitations

- **Oxidation stability**: Natural oils (animal and vegetable) oxidize much faster than mineral oils. Vegetable oils last 1-2 years in storage; animal fats last 6-12 months. Rancidity increases acidity (corrosion risk) and viscosity (pumping problems). Antioxidants extend shelf life but add cost and complexity.
- **Temperature range**: Every lubricant has a temperature window. Below the pour point, the lubricant is too thick to flow. Above the dropping point (grease) or flash point (oil), the lubricant fails catastrophically. No single lubricant covers the full range from Arctic cold to furnace heat. Equipment designers must select lubricants appropriate to their operating environment.
- **Material compatibility**: Lubricants interact with seals, paints, plastics, and elastomers. Mineral oil swells natural rubber and degrades some plastics. Silicone oil contaminates surfaces and prevents paint adhesion. Synthetic oils can shrink or swell seals designed for mineral oil. Always verify compatibility between lubricant and all materials it contacts.
- **Shelf life**: Store all lubricants in sealed, labeled containers away from heat, sunlight, and moisture. Mineral oils: 5+ year shelf life if uncontaminated. Vegetable oils: 1-2 years (oxidize and become acidic; check acid number before use). Animal fats: 6-12 months (rancidity; refrigeration extends to 2 years). Grease: 2-3 years in sealed containers (oil separation is the primary failure mode; if more than 10% free oil on the surface, discard). Cutting fluid concentrates: 2-5 years. Mixed emulsions: 3-6 months (biological growth is the limiting factor; add biocide and monitor pH weekly).
- **Lubricant degradation in service**: All lubricants degrade during use. Oxidation thickens the oil and deposits varnish. Thermal breakdown at high temperatures produces sludge. Contamination with wear particles, water, and process chemicals reduces lubrication effectiveness. Regular oil analysis and timely replacement are essential for equipment reliability.

---

## See Also

- **[Animal Materials](../animals/animal-materials.md)**: Fat and tallow supply for early lubricants
- **[Petrochemicals](petroleum-alternatives.md)**: Petroleum distillation for mineral oil production
- **[Acids](acids.md)**: Acid production for oil refining
- **[Machine Tools](../machine-tools/machining.md)**: Cutting fluid applications in machining
- **[Soap Making](../glossary/soap-making.md)**: Saponification chemistry for grease thickeners

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
