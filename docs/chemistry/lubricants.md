# Lubricants, Oils & Fluid Mechanics

> **Node ID**: chemistry.lubricants
> **Domain**: [Lubricants, Oils & Fluid Mechanics](./index.md)
> **Dependencies**: [`foundations`](../foundations/index.md), [`chemistry.petroleum-alternatives`](petroleum-alternatives.md)
> **Enables**: [`machine-tools`](../machine-tools/index.md), [`energy.gravity`](../energy/gravity.md)
> **Timeline**: Years 0-200+
> **Outputs**: lubricating_oil, grease, cutting_fluid, hydraulic_fluid, vacuum_oil

## Problem

Every machine with moving parts generates friction and heat. Without lubrication, bearings gall, slides bind, gears wear out in hours, and cutting tools destroy both themselves and the workpiece. A civilization rebuilding its industrial base needs lubricants from day one, starting with animal fats and evolving toward refined mineral oils and synthetic hydraulic fluids.

## Technologies & Systems

### Animal Fats & Vegetable Oils

**Rendering animal fat**:
- **[Tallow](../glossary/tallow.html)** (beef/mutton fat): Cut fat into small pieces. Heat in iron pot with water (prevents scorching) at 80-100°C for 2-4 hours. Fat melts out, floats on water. Skim off, filter through cloth. Repeat pressing of cracklings (solid residue) in screw press to extract remaining fat. Yield: 70-85% of raw fat weight. Melting point: 40-45°C. At room temperature: semi-solid, waxy.
- **[Lard](../glossary/lard.html)** (pig fat): Same rendering process. Lower melting point (33-40°C). Softer, more fluid at room temperature. Preferred for lighter lubrication duties.
- **Clarification**: Re-melt fat, add water, boil, cool. Impurities settle or float. Skim clean fat. Repeat until clear. This is critical for lubricant use — impurities are abrasive.

**Vegetable oil extraction**:
- **Cold pressing**: Crush oilseeds (flax, rapeseed, castor, olive, sunflower) in screw press or wedge press at room temperature. Oil expressed, collected. Cake (pressed seed) may be re-pressed warm for additional yield. Castor oil: press castor beans. Very high viscosity (100x olive oil) — excellent for high-speed, high-temperature applications.
- **Hot pressing**: Heat seeds to 80-100°C before pressing. Higher yield (more oil released) but darker oil with more free fatty acids (lower quality, shorter shelf life).
- **Properties**: Vegetable oils are triglycerides (glycerol + 3 fatty acid chains). Good lubricity (polar molecules adhere to metal surfaces). Viscosity varies with oil type (castor: 250 cSt at 40°C; olive: 40 cSt; linseed: 25 cSt). Oxidize over time (rancidity) — become acidic and gummy. Store cool, dark, in sealed containers. Add antioxidants if available.

**[Linseed oil](../glossary/linseed-oil.html)** (flax seed oil): Drying oil — polymerizes on exposure to air (oxidation cross-links fatty acid chains → solid film). Not for lubrication (it hardens). Used for: paint binder (oil paint = linseed oil + pigment), wood finishing, putty (linseed oil + chalk), protective coatings on metal (thin film inhibits rust). Boiled linseed oil (heated with metallic driers — manganese or cobalt salts) dries faster (hours instead of days).

### Lubrication Regimes

**Boundary lubrication**:
- Thin molecular film (1-10 nm) of polar molecules adsorbed on metal surfaces. Fatty acids (from animal/vegetable fats) have polar head (attaches to metal oxide surface) and non-polar tail (hydrocarbon chain). Molecules orient perpendicular to surface → packed monolayer prevents metal-to-metal contact. Works at low speed, high load, intermittent motion.
- **Effectiveness**: Reduces friction coefficient from ~0.8 (dry steel-on-steel) to ~0.1-0.15. Prevents galling and seizing. Film breaks down above ~150°C (fatty acids desorb/oxidize) → limit for organic boundary lubricants.

**Hydrodynamic lubrication**:
- Full fluid film separates surfaces. No metal contact. Friction is entirely viscous drag of fluid. Requires: correct viscosity (thick enough to maintain film under load, thin enough to flow), adequate speed (generates pressure in converging wedge of lubricant), proper bearing geometry (clearance, alignment).
- **[Reynolds equation](../glossary/reynolds-equation.html)** governs film pressure distribution. Simplified: for a plain journal bearing, minimum film thickness h_min ≈ (μ × U × d²) / (4 × W), where μ = viscosity, U = surface speed, d = bearing diameter, W = load. Maintain h_min > 3× surface roughness for full film separation.
- **Friction coefficient**: ~0.001-0.01 (10-100x lower than boundary). This is why well-lubricated bearings run cool and last years.
- **[Oil viscosity grades](../glossary/oil-viscosity-grades.html)** (ISO VG system): ISO VG 32 = kinematic viscosity 32 cSt at 40°C (light spindle oil). ISO VG 68 = 68 cSt (general machine oil). ISO VG 220 = 220 cSt (gear oil). ISO VG 460 = 460 cSt (heavy gear oil). Higher viscosity = thicker oil = more load capacity but more viscous friction (heat).

**Elastohydrodynamic lubrication (EHL)**:
- Occurs in rolling element bearings and gear teeth (high contact pressure — 1-3 GPa). Pressure elastically deforms metal surfaces and compresses lubricant → viscosity increases dramatically (pressure-viscosity effect) → thin but extremely stiff film separates surfaces. Film thickness 0.1-1 μm. Requires lubricant with good pressure-viscosity coefficient (mineral oils better than water-based).

### Cutting Fluids

**Function**: Lubricate chip-tool interface (reduce cutting force, improve surface finish), cool tool and workpiece (remove heat — primary function), flush chips from cutting zone, prevent rust on workpiece and machine.

**Types**:
- **Straight cutting oil**: Mineral oil or lard oil, undiluted. Best lubrication, poorest cooling (low heat capacity). For: tapping, threading, broaching, heavy turning (where lubrication matters more than cooling). Add sulfur or chlorine compounds (extreme pressure additives — react with metal surface at high temperature → solid lubricating film that prevents welding of chip to tool).
- **Soluble oil (emulsion)**: Mineral oil + emulsifier (sulfonate or soap) + water. Mix 5-10% oil in water by volume. Milky white emulsion. Water provides excellent cooling (high heat capacity). Oil provides lubrication and rust protection. THE most common cutting fluid for general machining. Replace regularly (bacteria grow in emulsion → rancid smell, skin irritation — add biocide).
- **Synthetic cutting fluid**: Water + chemical lubricants (no mineral oil). Clear or tinted. Best cooling, good rust protection, longest sump life. More expensive. For grinding (need maximum cooling and clean fluid) and high-speed machining.

**Application methods**:
- **Flood coolant**: Pump fluid from sump tank through hose/nozzle, direct at cutting zone. Flow rate 5-20 liters/minute. Most common method. Filter fluid (mesh or paper filter) to remove chips and fines. Settle tank allows chips to settle before recirculation.
- **Mist coolant**: Atomize fluid into fine spray (compressed air + fluid). Lower volume, less mess. For operations where flood is impractical. Respiratory hazard (inhaled oil mist) — use only with ventilation.
- **Manual application**: Brush or squeeze bottle. For intermittent cutting, hand operations, small jobs.

### Grease Production

**Composition**: Base oil (70-90%) + thickener (5-25%) + additives (0-10%). Thickener turns liquid oil into semi-solid that stays in place (doesn't drain out of bearings).

**Soap thickeners**:
- **[Soap making](../glossary/soap-making.html)** (saponification): Fat/oil + alkali → soap + glycerol. Specific soaps:
  - **Sodium soap (NaOH + fat)**: Sodium stearate. Water-soluble grease. NOT water-resistant. For: general-purpose applications, open gears (cheap). Melts at ~150°C.
  - **Calcium soap (Ca(OH)₂ + fat)**: Calcium stearate. Water-resistant (insoluble). THE most common grease thickener. "Lime soap" grease. Dropping point ~90°C (relatively low — grease softens and runs at high temperature). For: wheel bearings, water pumps, marine applications.
  - **Lithium soap (LiOH + fat)**: Lithium stearate. Water-resistant AND higher dropping point (~190°C). Multi-purpose grease — single grease type for most applications. THE modern standard. Requires LiOH (from lithium ore — lepidolite or spodumene, roasted with CaO, leached with water, electrolyzed → LiOH). Lithium is less common than sodium/calcium — save for applications requiring both water resistance and high temperature.
- **Grease making process**:
  1. Heat base oil to 80-100°C in heated vessel.
  2. Add alkali (NaOH, Ca(OH)₂, or LiOH) and fat simultaneously. Saponification occurs.
  3. Stir and heat to 150-200°C (depending on soap type) to complete saponification and dehydrate.
  4. Cool slowly while stirring. Mill (pass through roller mill or colloid mill) to homogenize texture and break up soap fibers.
  5. Add additives (graphite, molybdenum disulfide (MoS₂), zinc dialkyldithiophosphate (ZDDP — anti-wear/antioxidant)) if required. Mix thoroughly.
  6. Test: penetration (cone penetration test — measure how far standardized cone sinks into grease at 25°C → NLGI grade: 000 = very soft, 2 = typical bearing grease, 6 = very hard). Dropping point (heat until grease melts and drips → maximum usable temperature).

**[Clay-thickened grease](../glossary/clay-thickened-grease.html)** (non-soap):
- Bentonite clay (organically modified — treated with quaternary ammonium salts to make it oil-compatible) + base oil. No dropping point (clay doesn't melt) → usable to 250°C+. For high-temperature applications where soap grease fails. Simpler to make than lithium grease if bentonite clay is available.

### Bearing Lubrication Methods

**Plain (journal) bearings**:
- **Oil-ring lubrication**: Brass or steel ring (20-40 mm diameter) rides on shaft, dips into oil reservoir below bearing. Shaft rotation carries ring → ring drags oil up to shaft top → oil flows along shaft into bearing. Continuous, automatic, self-contained. For horizontal shafts at moderate speed (100-3000 RPM).
- **Wick lubrication**: Felt or cotton wick submerged in oil reservoir, other end contacts shaft or bearing surface. Capillary action draws oil to bearing. Low flow rate — for light-duty bearings. Quiet, simple.
- **Splash lubrication**: Gear or rotating element in oil bath throws oil onto bearing. Common in gearboxes — no separate oiling system needed. Oil level: gears dip 1-2 tooth depths.
- **Forced lubrication**: Gear pump draws oil from reservoir, forces through filter, delivers to bearing under pressure (0.1-0.5 MPa). Oil flows through bearing, drains back to reservoir. Provides positive, controlled oil supply regardless of speed. Essential for high-speed or heavily loaded bearings (steam turbine bearings, large generators).

**Rolling element bearings**:
- **Grease-packed**: Fill bearing cavity 30-50% with grease (do not overfill — churning generates heat). Grease lasts months-years depending on speed and temperature. Sealed bearings (rubber seals) retain grease for life. Shielded bearings (metal shields) allow some grease exchange.
- **Oil mist lubrication**: Atomize oil with compressed air, pipe mist to bearing. Continuous fine lubrication. Excellent for high-speed spindle bearings. Requires clean, dry compressed air.

### Hydraulic Fluids

**Requirements**: Incompressible (transmit force efficiently), proper viscosity (flow through valves and pumps, maintain lubricating film), chemically stable (no oxidation, no corrosion), compatible with seals (does not swell or shrink rubber/leather). Fire resistance desirable but not always achievable.

**Fluid types**:
- **Vegetable oil-based**: Rapeseed or castor oil. Biodegradable, good lubricity. Limited temperature range (thickens when cold, thins when hot). Oxidizes over time. For the Metallurgy-Machine Tools stage transition hydraulic presses.
- **Mineral oil-based**: Refined petroleum oil (see Petrochemicals — distillation). ISO VG 32 or 46 most common. Add anti-wear agents (ZDDP), antioxidants, rust inhibitors, anti-foam agents. Operating temperature range -10°C to +70°C. Most common hydraulic fluid.
- **[Water-glycol](../glossary/water-glycol.html)** (fire-resistant): Water + glycol (40-60%) + thickener + additives. Fire-resistant (water content). Lower lubricity than oil — need harder pump and valve materials. For locations with fire risk (furnaces, welding areas).

**Hydraulic system**:
- Pump (gear pump: 10-200 bar, or piston pump: 200-400 bar) → control valves (directional, pressure relief, flow control) → actuator (cylinder for linear motion, motor for rotary) → return line → reservoir. Filter in return line (10-25 μm absolute) to remove contaminants (primary cause of hydraulic system failure). Reservoir: 2-3× pump flow rate capacity (allows fluid to de-aerate and settle).

### Vacuum Oils

**Requirements for vacuum pump oils**:
- Low vapor pressure (<10⁻⁴ Pa at operating temperature) — if oil has high vapor pressure, it evaporates into vacuum → contaminates vacuum, prevents reaching low pressure.
- Good lubricity for pump bearings and seals.
- Chemical stability (resist oxidation, do not form sludge).
- Compatible with pumped gases (do not react with solvents, acids, or other process gases).

**Types**:
- **Mineral vacuum oil**: Highly refined, distilled mineral oil with narrow boiling range. Achieves ultimate vacuum ~10⁻² to 10⁻³ Pa. For mechanical roughing pumps (rotary vane, piston).
- **Silicone vacuum oil**: Polydimethylsiloxane (PDMS) — from silicon + methyl chloride chemistry. Very low vapor pressure (~10⁻⁶ Pa at 25°C). Chemically inert. For diffusion pumps (see Vacuum & Optics) — achieves ultimate vacuum ~10⁻⁶ to 10⁻⁸ Pa.
- **Synthetic hydrocarbon oil**: Polyalphaolefin (PAO). Low vapor pressure, excellent lubricity, wide temperature range. For high-performance mechanical pumps.

**[Oil purification](../glossary/oil-purification.html)** (for extending vacuum oil life):
- **Filtration**: Pass oil through 1-5 μm filter to remove particulates.
- **Degassing**: Heat oil under vacuum to remove dissolved gases and volatile contaminants.
- **Adsorption**: Pass through activated alumina or molecular sieve to remove acidic and polar contaminants.

### Lubrication for Semiconductor Equipment

**[Cleanroom-compatible lubricants](../glossary/cleanroom-compatible-lubricants.html)** (Photolithography):
- Low outgassing (do not contaminate cleanroom air or wafer surfaces).
- Non-particulating (do not shed particles into cleanroom).
- Vacuum-compatible (for equipment inside vacuum chambers — load locks, wafer transfer robots).
- Specialty perfluoropolyether (PFPE) greases — extremely inert, wide temperature range, ultra-low vapor pressure. Synthesized from HF + olefins under controlled conditions (semiconductor chemistry).

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

## Key Deliverables

- Reliable supply chain for animal and vegetable lubricants (tallow, lard, castor oil)
- Cutting fluid formulations: soluble oil emulsion for general machining, straight oil for threading/tapping
- Grease production capability: calcium soap (water-resistant), sodium soap (general), lithium soap (multi-purpose)
- Hydraulic fluid supply for presses and machine tools (vegetable oil → mineral oil)
- Vacuum-compatible oils for vacuum pump systems (mineral → silicone)
- Bearing lubrication protocols for plain and rolling-element bearings
- Lubrication schedules and maintenance procedures for all machinery

### Solid Lubricants

**Graphite**: Layered carbon structure — weak van der Waals forces between layers allow easy shear. Effective in air (adsorbed water film aids layer sliding) but poor in vacuum or dry environments. Withstands temperatures to 450°C in air (oxidizes above this). Used in: packings, gaskets, high-temperature bearings, lock mechanisms, mold release agents. Applied as powder, dispersion in oil/grease ("graphited grease"), or bonded coating (graphite + sodium silicate binder).

**Molybdenum disulfide (MoS₂)**: Similar layered structure to graphite but effective in vacuum and dry environments — the dominant solid lubricant for space applications. Coefficient of friction: 0.02-0.1. Temperature range: -180 to +350°C in air (oxidizes to MoO₃ above 350°C), up to 800°C in vacuum. Applied by: burnishing (rubbing powder into surface), sputtering (PVD thin film 0.5-2 µm), or bonded coating (MoS₂ + epoxy/phenolic binder + solvent). MoS₂ coatings are standard for spacecraft mechanisms, satellite deployment hinges, and vacuum-chamber bearings.

**PTFE (Teflon)**: Polytetrafluoroethylene — ultra-low coefficient of friction (0.04-0.10). Chemically inert, temperature range -200 to +260°C. Used as: bearing liners, sliding plates (bridge expansion bearings), piston rings (non-lubricated compressors), tape (thread sealing). Limitations: poor wear resistance (filled with glass fiber, bronze, or carbon to improve), creep under load ("cold flow"), cannot be melt-processed like typical plastics (sintered from powder).

**Polymer bearings**: Acetal (Delrin), nylon, ultra-high-molecular-weight polyethylene (UHMWPE) — self-lubricating, no external lubricant needed. UHMWPE: used in artificial hip joints, conveyor wear strips, marine bearings (water-lubricated). Nylon: gear wheels, low-load bearings, sprockets. Acetal: precision gears, valve seats, food-processing bearings (no lubricant contamination).

### Synthetic Lubricants

**Polyalphaolefin (PAO)**: Hydrocarbon synthetic — made by oligomerizing α-olefins (primarily decene, C₁₀) with BF₃ catalyst, then hydrogenating. Uniform molecular weight distribution (no light or heavy fractions) gives: better low-temperature fluidity (pour point -50 to -65°C vs -15°C for mineral oil), higher viscosity index (130-150 vs 95-105), better oxidation stability (2-3× longer oil life). Used in: jet engine oils, Arctic machinery, long-drain automotive oils.

**Ester oils**: Diesters and polyol esters — synthesized from organic acids and alcohols. Excellent lubricity (polar ester groups adsorb strongly to metal surfaces), good thermal stability (200-250°C continuous), biodegradable. Used in: jet engine oils (MIL-PRF-23699), compressor oils, biodegradable hydraulic fluids (forestry, marine), two-stroke engine oils.

**Silicone oils**: Polydimethylsiloxane (PDMS) — extremely wide temperature range (-70 to +250°C), chemically inert, excellent dielectric properties. Poor lubricity for metal-on-metal (low load-carrying capacity) — used where temperature stability or chemical inertness matters more than extreme pressure performance: diffusion pump fluids, dashpot dampers, electrical insulation, mold release, medical devices.

**Perfluoropolyether (PFPE)**: Fluorinated synthetic — the most chemically resistant lubricant. Inert to oxygen, fuels, solvents, acids, and bases. Temperature range: -80 to +300°C. Ultra-low vapor pressure — no outgassing in vacuum. Used in: spacecraft mechanisms, semiconductor manufacturing equipment, oxygen compressors (mineral oil + high-pressure O₂ = explosion), chemical processing valves.

### Oil Analysis and Condition Monitoring

**Regime**: Industrial plants monitor lubricant condition to schedule oil changes based on actual condition, not fixed intervals. Key tests: (1) **Viscosity**: Change >10% indicates oxidation, contamination, or wrong oil grade. (2) **Acid number**: Increase indicates oxidation — acidic byproducts corrode bearings. (3) **Particle count**: ISO 4406 cleanliness code — critical for hydraulic systems (target: 16/14/11 for servo valves). (4) **Spectrometric analysis**: ICP or atomic absorption detects wear metals (Fe, Cu, Pb, Sn, Cr) at ppm levels — trending indicates which component is wearing. (5) **Water content**: Karl Fischer titration — water causes rust, reduces film strength, promotes microbial growth. Limits: <0.1% for most systems, <0.03% for turbine oils.

**Sampling**: Always sample from live oil stream (not from drain plug or static reservoir). Use clean sample bottles. Sample frequency: monthly for critical equipment (turbines, large gearboxes), quarterly for general plant equipment.

### Safety & Hazards

- **Hot oil (200°C+)**: Severe splash burns. Face shield, long gloves. Pour slowly.
- **Caustic soda (NaOH/KOH)**: Chemical burns, eye damage. Goggles, gloves. Eye wash station.
- **Oil fires**: NEVER use water. Sand, fire blanket, or smother with lid.
- **Oil mists**: Respiratory irritant. Ventilation required.

**Environmental disposal**: Used oil and grease must not be dumped on ground or in waterways. Collect in sealed containers. Re-refine mineral oils (vacuum distillation removes contaminants, additives are replenished). Animal and vegetable oils can be composted in small quantities. Used cutting fluid emulsions require treatment (break emulsion with acid or flocculant, separate oil phase, treat water phase before discharge). Even in a bootstrap economy, contaminating water supplies with oil has long-term consequences for agriculture and drinking water.

### Bearing Design Parameters for Bootstrap Machinery

**SAE viscosity grades**: The Society of Automotive Engineers classifies engine oil viscosity by kinematic viscosity at 100°C. SAE 30: 9.3-12.5 cSt at 100°C (general-purpose engine oil, moderate climate). SAE 40: 12.5-16.3 cSt (heavy-duty engine oil, hot climate). SAE 10W-30: multi-grade oil with 10W winter rating (meets cold-cranking requirements at -25°C) and SAE 30 hot rating. Higher viscosity grades provide thicker films for heavier loads but increase viscous friction and heat generation. Select the lowest viscosity that maintains adequate film thickness under operating conditions.

**Bearing PV limits**: The product of bearing pressure P (MPa) and surface velocity V (m/s) determines the heat generation rate in plain bearings. Each bearing material has a maximum PV rating: bronze (phosphor bronze) 1.75 MPa·m/s, Babbitt metal 1.05 MPa·m/s, PTFE (unfilled) 0.35 MPa·m/s, acetal (Delrin) 0.15 MPa·m/s, nylon 0.10 MPa·m/s. Exceeding the PV limit causes rapid temperature rise, lubricant breakdown, and bearing failure. For applications above the PV limit, use rolling element bearings (which have much higher speed/load capability) or provide forced lubrication with external cooling.

**Bearing clearance design**: Journal bearing radial clearance (difference between housing bore and shaft diameter) must accommodate thermal expansion, lubricant film thickness, and manufacturing tolerances. Rule of thumb: 0.001 × shaft diameter (e.g., 50 mm shaft = 0.05 mm radial clearance). Tight clearance reduces vibration and improves positional accuracy but increases friction and risk of seizure if temperature rises. Loose clearance allows more oil flow and better cooling, tolerates misalignment, but permits vibration. Length-to-diameter ratio (L/D) of 0.5-1.5 is typical. Shorter bearings (L/D < 1) run cooler and tolerate misalignment; longer bearings (L/D > 1) carry more load.

**Oil selection for bootstrap machinery**: For a bootstrap workshop without access to refined petroleum products, the practical lubricant sequence is: (1) rendered animal fat (tallow/lard) for slow-speed plain bearings and sliding surfaces; (2) vegetable oil (rapeseed, castor) for moderate-speed bearings and cutting fluid base; (3) clarified tallow + lime soap grease for wheel bearings and open gears. As refining capability develops, mineral oil from petroleum distillation replaces vegetable and animal oils for most applications due to better oxidation stability and wider viscosity range. The viscosity grade is selected by the Somerfeld number calculation: for a 50 mm shaft at 1500 RPM carrying 500 N radial load, ISO VG 32 provides adequate film; for the same shaft at 300 RPM, ISO VG 68 is needed. In cold climates (below -10°C startup), use the lowest viscosity that still provides adequate film at operating temperature, or pre-heat the oil with a waste-heat system before starting machinery.

**Lubricant storage and shelf life**: Store all lubricants in sealed, labeled containers away from heat, sunlight, and moisture. Mineral oils: 5+ year shelf life if uncontaminated. Vegetable oils: 1-2 years (oxidize and become acidic — check acid number before use). Animal fats: 6-12 months (rancidity — refrigeration extends to 2 years). Grease: 2-3 years in sealed containers (oil separation is the primary failure mode — if more than 10% free oil on the surface, discard). Cutting fluid concentrates: 2-5 years. Mixed emulsions: 3-6 months (biological growth is the limiting factor — add biocide and monitor pH weekly).

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
