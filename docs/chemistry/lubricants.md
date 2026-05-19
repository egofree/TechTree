# Lubricants, Oils & Fluid Mechanics

> **Node ID**: chemistry.lubricants
> **Domain**: [Lubricants, Oils & Fluid Mechanics](./)
> **Dependencies**: `foundations`, `chemistry.petroleum-alternatives`
> **Enables**: `machine-tools`, `energy.gravity`
> **Timeline**: Years 0-200+
> **Outputs**: lubricating_oil, grease, cutting_fluid, hydraulic_fluid, vacuum_oil

## Problem

Every machine with moving parts generates friction and heat. Without lubrication, bearings gall, slides bind, gears wear out in hours, and cutting tools destroy both themselves and the workpiece. A civilization rebuilding its industrial base needs lubricants from day one, starting with animal fats and evolving toward refined mineral oils and synthetic hydraulic fluids.

## Technologies & Systems

### Animal Fats & Vegetable Oils

**Rendering animal fat**:
- **Tallow** (beef/mutton fat): Cut fat into small pieces. Heat in iron pot with water (prevents scorching) at 80-100°C for 2-4 hours. Fat melts out, floats on water. Skim off, filter through cloth. Repeat pressing of cracklings (solid residue) in screw press to extract remaining fat. Yield: 70-85% of raw fat weight. Melting point: 40-45°C. At room temperature: semi-solid, waxy.
- **Lard** (pig fat): Same rendering process. Lower melting point (33-40°C). Softer, more fluid at room temperature. Preferred for lighter lubrication duties.
- **Clarification**: Re-melt fat, add water, boil, cool. Impurities settle or float. Skim clean fat. Repeat until clear. This is critical for lubricant use — impurities are abrasive.

**Vegetable oil extraction**:
- **Cold pressing**: Crush oilseeds (flax, rapeseed, castor, olive, sunflower) in screw press or wedge press at room temperature. Oil expressed, collected. Cake (pressed seed) may be re-pressed warm for additional yield. Castor oil: press castor beans. Very high viscosity (100x olive oil) — excellent for high-speed, high-temperature applications.
- **Hot pressing**: Heat seeds to 80-100°C before pressing. Higher yield (more oil released) but darker oil with more free fatty acids (lower quality, shorter shelf life).
- **Properties**: Vegetable oils are triglycerides (glycerol + 3 fatty acid chains). Good lubricity (polar molecules adhere to metal surfaces). Viscosity varies with oil type (castor: 250 cSt at 40°C; olive: 40 cSt; linseed: 25 cSt). Oxidize over time (rancidity) — become acidic and gummy. Store cool, dark, in sealed containers. Add antioxidants if available.

**Linseed oil** (flax seed oil): Drying oil — polymerizes on exposure to air (oxidation cross-links fatty acid chains → solid film). Not for lubrication (it hardens). Used for: paint binder (oil paint = linseed oil + pigment), wood finishing, putty (linseed oil + chalk), protective coatings on metal (thin film inhibits rust). Boiled linseed oil (heated with metallic driers — manganese or cobalt salts) dries faster (hours instead of days).

### Lubrication Regimes

**Boundary lubrication**:
- Thin molecular film (1-10 nm) of polar molecules adsorbed on metal surfaces. Fatty acids (from animal/vegetable fats) have polar head (attaches to metal oxide surface) and non-polar tail (hydrocarbon chain). Molecules orient perpendicular to surface → packed monolayer prevents metal-to-metal contact. Works at low speed, high load, intermittent motion.
- **Effectiveness**: Reduces friction coefficient from ~0.8 (dry steel-on-steel) to ~0.1-0.15. Prevents galling and seizing. Film breaks down above ~150°C (fatty acids desorb/oxidize) → limit for organic boundary lubricants.

**Hydrodynamic lubrication**:
- Full fluid film separates surfaces. No metal contact. Friction is entirely viscous drag of fluid. Requires: correct viscosity (thick enough to maintain film under load, thin enough to flow), adequate speed (generates pressure in converging wedge of lubricant), proper bearing geometry (clearance, alignment).
- **Reynolds equation** governs film pressure distribution. Simplified: for a plain journal bearing, minimum film thickness h_min ≈ (μ × U × d²) / (4 × W), where μ = viscosity, U = surface speed, d = bearing diameter, W = load. Maintain h_min > 3× surface roughness for full film separation.
- **Friction coefficient**: ~0.001-0.01 (10-100x lower than boundary). This is why well-lubricated bearings run cool and last years.
- **Oil viscosity grades** (ISO VG system): ISO VG 32 = kinematic viscosity 32 cSt at 40°C (light spindle oil). ISO VG 68 = 68 cSt (general machine oil). ISO VG 220 = 220 cSt (gear oil). ISO VG 460 = 460 cSt (heavy gear oil). Higher viscosity = thicker oil = more load capacity but more viscous friction (heat).

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
- **Soap making** (saponification): Fat/oil + alkali → soap + glycerol. Specific soaps:
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

**Clay-thickened grease** (non-soap):
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
- **Water-glycol** (fire-resistant): Water + glycol (40-60%) + thickener + additives. Fire-resistant (water content). Lower lubricity than oil — need harder pump and valve materials. For locations with fire risk (furnaces, welding areas).

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

**Oil purification** (for extending vacuum oil life):
- **Filtration**: Pass oil through 1-5 μm filter to remove particulates.
- **Degassing**: Heat oil under vacuum to remove dissolved gases and volatile contaminants.
- **Adsorption**: Pass through activated alumina or molecular sieve to remove acidic and polar contaminants.

### Lubrication for Semiconductor Equipment

**Cleanroom-compatible lubricants** (Photolithography):
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

### Safety & Hazards

- **Hot oil (200°C+)**: Severe splash burns. Face shield, long gloves. Pour slowly.
- **Caustic soda (NaOH/KOH)**: Chemical burns, eye damage. Goggles, gloves. Eye wash station.
- **Oil fires**: NEVER use water. Sand, fire blanket, or smother with lid.
- **Oil mists**: Respiratory irritant. Ventilation required.
---

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
