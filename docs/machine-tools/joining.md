# Metal Joining

> **Node ID**: machine-tools.joining
> **Domain**: Machine Tools Bootstrap
> **Timeline**: Years 5-70
> **Outputs**: forge_welds, brazed_joints, soldered_joints, riveted_joints, welded_joints, acetylene, tig_welds, mig_welds, resistance_welds, electron_beam_welds, ultrasonic_bonds, friction_stir_welds, laser_welds, diffusion_bonds, hermetic_seals, wire_bonds

## Overview

Metal joining is the capability that makes machinery possible. Individual forged or cast parts are rarely useful alone — they must be assembled into structures, mechanisms, pressure vessels, and frames. This file covers the full spectrum of joining methods in bootstrap order: forge welding (earliest, requires only a forge and hammer), brazing and soldering (require filler alloys), riveting (mechanical joining requiring no heat at the joint), oxy-acetylene welding (requires gas production infrastructure), and arc welding/SMAW (requires electrical power). The advanced sections cover TIG, MIG, resistance, electron beam, ultrasonic, friction stir, laser, and diffusion bonding — techniques essential for vacuum chamber fabrication, semiconductor equipment, and hermetic sealing.

Each method occupies a specific niche defined by temperature, joint strength, equipment requirements, and the materials it can join. No single method replaces all others — a complete industrial shop needs all six.

For the metallurgy of producing iron and steel stock to be joined, see [Iron & Steel](../metals/iron-steel.md). For the electrical infrastructure needed by arc welding, see [Electricity](../energy/electricity.md).

## Forge Welding

The oldest solid-state welding method, achievable as soon as wrought iron is produced in a bloomery forge. No filler metal required — the base metal itself fuses under heat and pressure.

**Principle**: Heat iron or low-carbon steel to a temperature where the surface becomes pasty (~1200-1300°C). Place the pieces together and strike firmly with a hammer. Heat and pressure cause atomic diffusion across the interface, producing a solid-state weld with no melted zone.

**[Fluxes](../glossary/fluxes.md)** (essential — without flux, surface oxide prevents metal-to-metal contact):
- **Silica sand (SiO₂)**: The simplest flux. Sprinkle on joint surfaces before heating. Melts at ~1710°C but dissolves iron oxide (wüstite, FeO) at forge welding temperatures, forming a fluid iron silicate slag that flows out of the joint under hammering.
- **Borax (sodium borate, Na₂B₄O₇)**: More effective than sand. Melts at ~743°C, actively dissolves iron oxide. Apply as powder or paste (borax mixed with water). The standard forge welding flux for iron and steel.
- **Clean scale technique**: On very clean wrought iron (low carbon), an experienced smith can weld without flux by hammering through the thin oxide layer. Unreliable — flux is always preferred.

**Joint preparation and design**:
- **Scarf joint**: The strongest joint for bar-to-bar welding. Taper both pieces to a long diagonal (scarf angle ~10-15°, overlap length ~2-3× bar thickness). The long taper distributes the forge weld over a large area. Position the scarfs offset so the thin ends overlap — this prevents a cold shut (unwelded gap) at the edges.
- **Lap joint**: Two flat pieces overlapped 15-25 mm. Simplest joint. Used for sheet and plate. Weaker than scarf in tension because the weld area is limited to the overlap.
- **Butt weld**: Two bars joined end-to-end. Upset (thicken) both ends before welding to ensure adequate material. Difficult — requires precise temperature control. Often reinforced by ferrule (a band shrunk over the joint).
- **Faggot weld**: Bundle of bars or strips welded together into a single billet. Used for pattern-welded (Damascus) steel — alternate layers of high- and low-carbon steel, welded and folded repeatedly to create 100+ layer composite. Also used to build up larger stock from smaller pieces.
- **T-joint and cross weld**: One bar welded perpendicular to another. Requires careful fluxing on the contact surfaces and firm hammering to close the joint at the intersection.

**Procedure**:
1. Clean joint surfaces to bare metal (wire brush or file).
2. Apply flux to both surfaces.
3. Heat evenly in forge (charcoal or coal, forced air from bellows) to bright yellow-white (~1250-1300°C). The surface should appear to shimmer or "sweat" — scale flakes away exposing bright metal.
4. Remove from forge quickly. Position pieces on anvil face.
5. Strike immediately with firm, rapid blows — first a light tap to set alignment, then heavy hammering to expel slag and consolidate the weld. Work from the center outward to squeeze flux and scale out of the joint.
6. Reheat and re-strike if the joint is longer than one hammering session allows (metal cools below welding temperature in ~10-20 seconds).

**Quality testing**: Bend the welded bar in a vise or over the anvil horn. A sound weld bends without opening. A poor weld cracks at the seam — caused by oxide inclusion, insufficient heat, or insufficient flux.

**Limitations**: Only joins iron and low-carbon steel (wrought iron welds most reliably). High-carbon steel and cast iron cannot be forge welded by conventional methods. Joint strength is 80-95% of parent metal for a skilled smith.

## Brazing

Brazing joins metals using a filler alloy that melts above 450°C but below the melting point of the base metal. Capillary action draws molten filler into the joint gap. The base metal never melts, which means dissimilar metals can be joined and heat distortion is minimal.

**Brass brazing (spelter brazing)**:
- **Filler alloy**: Brass (copper-zinc). Typical composition: 60% Cu / 40% Zn (melts ~900°C, flows at ~950°C). Produce by alloying copper and zinc in a crucible — see [Iron & Steel](../metals/iron-steel.md) for copper and zinc sourcing.
- **Flux**: Borax paste (borax + water). Melts at ~743°C, dissolves oxides, allows filler to wet and flow.
- **Joint clearance**: 0.05-0.20 mm (total gap). Too tight — filler cannot enter. Too wide — capillary action fails, filler pools. Precision matters.
- **Heating method**: Forge or torch. Heat entire joint area uniformly to bright red (~950°C). Apply brazing rod — brass melts on contact, flows into joint by capillary action. The joint should fill completely — visible as a continuous fillet at both ends.
- **Joint strength**: Shear strength ~150-250 MPa in the filler. Stronger than soft solder by 5-10×.
- **Applications**: Bicycle frames, tool handles, pipe fittings, tank seams, cast iron repairs (cast iron is difficult to forge weld but braze-joins well), joining dissimilar metals (steel to copper, steel to brass).

**Silver brazing (silver soldering, hard soldering)**:
- **Filler alloy**: Silver-copper-zinc ternary. Compositions and melting ranges:
  - Easy-flo: 50% Ag / 15% Cu / 35% Zn — melts 620-690°C. Lowest temperature, flows easily.
  - Medium: 45% Ag / 30% Cu / 25% Zn — melts 670-740°C. Good general-purpose.
  - Hard: 75% Ag / 20% Cu / 5% Zn — melts 740-780°C. Highest strength, highest cost.
- **Flux**: Borax-based or fluoride-based paste. Fluoride fluxes are more aggressive at dissolving stubborn oxides (stainless steel, nickel alloys) but produce toxic fumes — use with ventilation.
- **Advantages over brass brazing**: Lower temperature (less thermal distortion), narrower joint gap capability, stronger joints in thin-wall assemblies. Critical for instrument work, jewelry, and fine mechanisms.
- **Cost consideration**: Silver is expensive. Reserve silver brazing for applications where the lower temperature or higher strength justifies the cost.

## Soft Soldering

The lowest-temperature joining method. Soldering fills joints with a low-melting alloy (below 450°C, typically 180-250°C). The resulting joint is mechanically weaker than brazing or welding but sufficient for electrical connections, plumbing, and sheet metal seams.

**Solder alloys**:
- **Tin-lead (Sn-Pb)**: The classic solder. 60/40 Sn/Pb melts at 183-190°C (eutectic 63/37 melts sharply at 183°C). 50/50 melts at 183-215°C (pasty range). Produce by melting tin and lead together in an iron ladle. Tin from cassiterite (SnO₂) reduction; lead from galena (PbS) roasting and smelting.
- **Lead-free alternatives**: Tin-silver (Sn-3.5% Ag, melts ~221°C), tin-copper (Sn-0.7% Cu, melts ~227°C), tin-bismuth (Sn-42% Bi, melts ~139°C — low-temperature applications). These require sourcing silver, copper, or bismuth.

**Flux types**:
- **Rosin (colophony)**: Purified pine resin. Dissolves thin oxide layers at soldering temperature. Non-corrosive, non-conductive — safe for electronics. Does NOT clean heavily oxidized or dirty surfaces.
- **Zinc chloride (killed spirits)**: Dissolve zinc metal in hydrochloric acid until bubbling stops. Aggressive flux — removes heavy oxidation. MUST be washed off after soldering or it corrodes the joint. Used for plumbing and sheet metal work.
- **Plumbing flux (tallow + sal ammoniac)**: Rendered fat mixed with ammonium chloride. Greasy paste that sticks to pipe surfaces, cleans oxides, and displaces water. Standard for copper pipe soldering.

**Procedure**:
1. Clean joint surfaces to bright metal (abrasive cloth, file, or wire brush).
2. Apply flux to both surfaces.
3. Heat the joint (not the solder) with a copper soldering iron or direct flame. Copper bit: 50-200 g copper block on iron shank, heated in flame or on stove. Tip temperature ~300-400°C.
4. Touch solder to the heated joint — solder melts on contact and flows by capillary action into the gap. The solder should flow smoothly; if it balls up, the surface is dirty or too cold.
5. Remove heat, hold parts still until solder solidifies (2-5 seconds). Movement during solidification produces a weak, crystalline ("cold") joint.

## Riveting

Mechanical joining with no heat applied to the joint itself. Rivets are installed hot or cold through holes in overlapping plates, then the second head is formed by hammering. Riveted joints dominated structural steel construction (bridges, ships, boilers) from ~1840 until arc welding replaced them after ~1940.

**Rivet types and materials**:
- **Material**: Wrought iron or mild steel rivets (matching the structure being joined). Copper rivets for copper structures. For boilers and pressure vessels, steel rivets of known composition.
- **Sizes**: Shank diameter 6-25 mm for structural work. Length = grip thickness (total plate thickness) + 1.5× shank diameter (to form the second head).
- **Hot riveting**: Heat rivet to bright red (~900-1000°C). Insert into hole. Hold manufactured head with a dolly (heavy steel bar held by helper). Hammer the protruding shank to form the second head (use a snap — a shaped tool that forms a hemispherical head). As the rivet cools, it contracts, clamping the plates together with enormous force. This contraction-induced clamping is the key advantage of hot riveting — produces a preload that makes the joint leak-tight and resistant to vibration loosening.
- **Cold riveting**: Drive rivet at room temperature with hammer or hydraulic riveter. No contraction clamping. Weaker joint. Used for small rivets (<10 mm) and non-critical applications. Aluminum and copper rivets are typically driven cold.

**Joint configurations**:
- **Lap joint**: Two plates overlap, single row of rivets through both. Simplest. Used for thin sheet and non-structural work.
- **Butt joint with cover plates**: Two plates butted edge-to-edge, with a cover plate (gusset) on one or both sides, riveted through. Double-cover butt joint is the strongest riveted configuration — used for bridge chords and boiler seams.
- **Rivet patterns**: Chain riveting (rivets in straight lines), zig-zag riveting (staggered — stronger, less tendency to tear along a line of holes). Pitch (rivet spacing): typically 3-5× rivet diameter. Edge distance: minimum 1.5× rivet diameter from center of hole to plate edge.
- **Boiler joints**: Longitudinal seams use double-riveted double-cover butt joints. Circumferential seams use single-riveted lap joints (lower stress on circumferential seam — hoop stress is double longitudinal stress, so the longitudinal seam must be stronger).

## Oxy-Acetylene Welding

The first practical gas welding method, enabled by the ability to produce calcium carbide in an electric arc furnace (see [Electricity](../energy/electricity.md)) and generate oxygen by air separation or chemical means. Produces a 3100°C flame — hot enough to melt steel.

**Gas production**:
- **Acetylene (C₂H₂)**: Calcium carbide (CaC₂) + water → C₂H₂ + Ca(OH)₂. Generate on demand in a gas generator: water dripped onto carbide in a closed vessel. Output pressure 0.01-0.15 MPa. NEVER store acetylene above 0.15 MPa — it detonates spontaneously under pressure. For portable use, dissolve acetylene in acetone inside a porous-filled steel cylinder (safe at ~1.5 MPa).
- **Oxygen**: Cryogenic air separation (distill liquid air — O₂ boils at -183°C, N₂ at -196°C) or chemical generation (barium oxide cycle: heat BaO in air to form BaO₂ at ~550°C, then heat BaO₂ to decompose at ~900°C, releasing O₂). Compress into steel cylinders at 15-20 MPa.

**Equipment**:
- **Torch body**: Brass or bronze, two control valves (oxygen and acetylene), mixing chamber (gases mix before tip), swappable tips (copper, orifice 0.5-3 mm — smaller tips for thin metal, larger for thick).
- **Regulators**: One on each cylinder. Reduce cylinder pressure to working pressure (acetylene: 0.01-0.1 MPa, oxygen: 0.1-0.5 MPa). Each regulator has two gauges (cylinder pressure and working pressure). Diaphragm-type regulators with adjustment screw.
- **Hoses**: Rubber with fabric reinforcement. Color-coded: red = fuel gas, blue or green = oxygen. Different thread connections to prevent cross-connection (left-hand thread for fuel, right-hand for oxygen).
- **Filler rod**: Mild steel wire, 1.5-3 mm diameter, matching base metal composition. Coat with thin flux for some applications.

**Flame types and adjustment**:
- **Neutral flame**: Equal O₂ and C₂H₂ flow. Inner cone ~2-5 mm, blue-white, sharp-edged. Outer envelope pale blue. Temperature ~3100°C. The standard flame for welding steel — neither adds nor removes carbon from the weld pool.
- **Carburizing (reducing) flame**: Excess acetylene. Longer, feathered inner cone with a distinct secondary feather. Adds carbon to the weld pool. Used for brazing, welding aluminum alloys, and soft soldering (with low heat).
- **Oxidizing flame**: Excess oxygen. Shorter inner cone, noisy, pale. Adds oxygen to weld pool — causes porosity in steel but useful for brazing brass and copper (the oxide layer helps filler wet the surface).

**Welding technique**: Open acetylene valve, ignite (sooty orange flame). Gradually open oxygen until neutral flame is achieved. Hold torch at ~45° angle to work. Move steadily along joint at 2-5 mm/second. Dip filler rod into leading edge of the molten puddle — rod melts and adds metal to the joint. Joint types: butt (square or beveled for plate >3 mm), lap, fillet, and corner.

**Cutting**: Fitted with a cutting attachment (additional oxygen lever and preheat flames). Heat steel to bright red (~900°C) with preheat flames, then press the oxygen lever — a jet of pure O₂ reacts exothermically with hot steel (iron burns). Molten iron oxide is blown through the cut by the oxygen jet. Kerf width 1-3 mm. Cuts steel up to 300+ mm thick. Cannot cut copper, aluminum, or stainless steel (they conduct heat away too fast or form refractory oxides).

## Arc Welding (SMAW / Stick Welding)

Shielded Metal Arc Welding uses an electric arc to melt both the consumable electrode and the base metal. The electrode's flux coating generates shielding gas and protective slag, making it the simplest arc welding process — no external gas supply required. SMAW is the dominant field welding method once electrical power is available.

**Power supply**:
- **DC (direct current)**: Generator or rectified AC. Smoother arc, easier to strike, directional heat control. Two polarity options: DCEN (electrode negative / straight polarity) — 70% heat in workpiece, deeper penetration. DCEP (electrode positive / reverse polarity) — 70% heat in electrode, faster deposition, shallower penetration. Typical: 50-200 A, 20-30 V arc voltage.
- **AC (alternating current)**: Transformer-type power supply (no rectifier needed). Arc extinguishes and reignites 50-60 times per second. Less stable than DC but simpler equipment. Handles magnetized workpieces (DC can suffer arc blow — deflection by magnetic fields). Typical: 50-300 A.
- **Open circuit voltage**: 50-80 V (for arc striking). Arc voltage (while welding): 20-30 V. Duty cycle: typically 60% (weld 6 minutes, cool 4 minutes in every 10). Heavy industrial machines: 100% duty cycle.

**Electrode classification (AWS system)**:
- **E6010**: Deep penetration, cellulose-based coating (generates CO/CO₂/H₂O shielding gas). Fast-freeze slag — excellent for root passes and vertical/downhill welding. DC only. The pipeline welder's electrode.
- **E6011**: Similar to E6010 but with potassium salts in coating — usable on AC. Universal-purpose electrode, good for dirty/rusty steel.
- **E6013**: Rutile (TiO₂) coating. Medium penetration, smooth bead, easy to strike and re-strike. The most forgiving electrode for beginners. Slag is easy to chip. Good for sheet metal, light fabrication, and repair. AC or DC.
- **E7018**: Low-hydrogen coating (limestone/CaCO₃ base). Iron powder in coating increases deposition rate. High tensile strength (70 ksi / 480 MPa minimum). The structural welding electrode — required for bridges, buildings, pressure vessels. Resists hydrogen-induced cracking. MUST be stored dry (bake at 120-200°C if exposed to humidity). DC preferred, AC usable.
- **Electrode size selection**: 2.5 mm for sheet metal and light work (60-90 A). 3.2 mm for general fabrication (90-130 A). 4.0 mm for heavy structural work (130-170 A). 5.0 mm for thick plate (170-250 A).

**Procedure**:
1. Clean joint to bare metal (grind or file — remove rust, paint, oil, moisture).
2. Prepare edges: bevel plates >6 mm thick to 30-60° included angle, 1-3 mm root gap, 1-2 mm root face.
3. Clamp workpiece to grounded steel welding table. Connect return lead (ground clamp) to workpiece.
4. Insert electrode in insulated holder. Set amperage on power supply (start at manufacturer's recommendation, adjust by sound — correct arc sounds like frying bacon; too high sounds like loud buzzing with excessive spatter; too low produces a sticky, irregular arc).
5. Strike arc by tapping or scraping electrode on work (like a match), then lifting to maintain 2-4 mm arc length (~1× electrode diameter). Maintain this distance as electrode melts and you move along the joint.
6. Travel speed: 2-5 mm/second. Angle: 10-15° from vertical in the direction of travel (drag angle). The molten pool should be 10-15 mm long and slightly wider than the electrode.
7. Multi-pass technique for thick joints: stringer beads (no weave) for root pass, weave beads (oscillate electrode side-to-side 2-3× electrode diameter) for fill and cap passes. Clean slag between each pass (chip with hammer, wire brush).
8. Slag removal: After each pass, chip slag with chipping hammer. Wire brush the bead. Inspect for porosity, undercut, and slag inclusion before the next pass.

**Safety** (non-negotiable):
- **Eye protection**: Welding helmet with shade #10-#14 filter lens. UV radiation from the arc causes "welder's flash" (photokeratitis — sunburn of the cornea, 24-48 hours of extreme pain and temporary blindness). Auto-darkening helmets are a modern luxury — fixed-shade helmets with flip-up filter are the bootstrap standard.
- **Skin protection**: Leather gloves (gauntlet length), leather apron or heavy cotton jacket (no synthetic fabrics — they melt onto skin). Arc UV burns exposed skin exactly like sunburn, in seconds.
- **Ventilation**: Welding fumes contain metal oxides (iron, manganese, chromium, zinc). Galvanized steel produces zinc oxide fume — causes "metal fume fever" (flu-like symptoms for 24 hours). ALWAYS weld in well-ventilated areas. Forced ventilation or fume extraction for confined spaces.
- **Fire hazard**: Sparks travel 5-10 m. Clear combustibles 10+ m from work area. Have fire extinguisher present. Hot slag can smolder in cracks and clothing for hours.
- **Electrical safety**: Dry gloves, dry clothing, insulated electrode holder. Never weld in wet conditions. Secondary voltage (20-80 V) can be lethal in damp environments.

## Method Selection Guide

| Method | Temp Range | Joint Strength | Equipment | Best For |
|--------|-----------|---------------|-----------|----------|
| Soft soldering | 180-250°C | 20-50 MPa | Soldering iron, flux | Electrical connections, plumbing, sheet metal seams |
| Silver brazing | 620-780°C | 150-300 MPa | Torch, silver alloy, flux | Fine mechanisms, instruments, dissimilar metals |
| Brass brazing | 870-950°C | 150-250 MPa | Forge/torch, brass rod, borax | Structural joints, cast iron, pipe fittings |
| Riveting | Cold or 900°C | 80-150 MPa (shear) | Hammer, dolly, rivet snap | Structural steel, boilers, bridges, ship hulls |
| Forge welding | 1200-1300°C | 250-400 MPa | Forge, anvil, hammer, flux | Iron/low-carbon steel bars, chains, composite billets |
| Oxy-acetylene | ~3100°C | 300-450 MPa | Torch, gas cylinders, regulators | Sheet metal, repair, cutting, general fabrication |
| SMAW (arc) | ~6000°C (arc) | 350-480 MPa | Power supply, electrodes | Structural steel, heavy fabrication, pressure vessels |

## Safety Common to All Methods

- **Eye protection**: Safety glasses at all times in the shop. Goggles or face shield for grinding, chipping, and wire brushing. Full welding helmet for arc and oxy-acetylene work.
- **Fire prevention**: Hot metal, sparks, and slag are ignition sources. Clear the area. Have water bucket, sand, and fire extinguisher ready. Hot work permits for industrial settings.
- **Burns**: All joining methods involve temperatures above 180°C. Use pliers, tongs, and leather gloves to handle hot work. Assume all metal in the shop is hot until confirmed otherwise.
- **Fumes and ventilation**: Soldering fumes (lead, flux acids), brazing fumes (zinc oxide from brass), welding fumes (metal oxides, ozone). Work in well-ventilated areas. Respirators for confined-space work.
- **Hearing protection**: Hammering (forge welding, riveting) produces impulse noise >100 dB. Chipping slag is similarly loud. Earplugs or earmuffs.

## Weld Quality Inspection

Weld inspection ensures structural integrity in pressure vessels, load-bearing structures, and critical machinery. Five methods, in order of increasing complexity and detection capability:

**Visual inspection (VT)**: The first and most important inspection method. Examine every weld visually (with 5-10× magnification where needed) before applying any other technique. Check for: undercut (groove melted into base metal at the toe of the weld, reducing cross-section), porosity (visible surface pores from gas trapped during solidification), cracking (hot cracks at the weld centerline or cold cracks in the heat-affected zone), incomplete penetration (root not fully fused), excessive reinforcement (weld bead too high above the base metal surface, creating stress concentration), and spatter (metal droplets adhering to base metal surface). Visual inspection catches 80-90% of weld defects when performed by a trained inspector. Requires adequate lighting (500+ lux at the weld surface) and clean weld surfaces (remove slag and spatter first).

**Dye penetrant testing (PT)**: Detects surface-breaking cracks, porosity, and seams that are too fine for unaided visual inspection. Procedure: (1) Clean the weld surface thoroughly (solvent wipe). (2) Apply red penetrant dye (fluorescent or visible red dye with low surface tension) to the surface. Allow 10-30 minutes dwell time for the dye to seep into surface defects by capillary action. (3) Remove excess penetrant from the surface with solvent or water rinse. (4) Apply white developer (chalk suspension in solvent) — the developer draws the red dye back out of any defects, producing a bright red indication against the white background. Detection capability: surface cracks as narrow as 0.5 mm deep and 1 μm wide. Works on any non-porous material — ferrous and non-ferrous metals, ceramics, plastics. Does NOT detect subsurface defects.

**Magnetic particle testing (MT)**: For ferromagnetic materials only (carbon steel, alloy steel, cast iron). Magnetize the weld area using a portable electromagnetic yoke (AC or DC) or permanent magnets. Spray the surface with fine iron particles (dry powder, or wet suspension in oil/water with fluorescent coating). Magnetic flux leakage at surface and near-surface cracks attracts the iron particles, forming a visible indication that outlines the defect. Detects surface cracks and near-surface flaws to a depth of ~2-6 mm below the surface (depending on flaw size and orientation). Fluorescent magnetic particle testing under UV light is the most sensitive variation, detecting cracks as fine as 0.025 mm wide. Faster and more sensitive than dye penetrant for steel, but limited to ferromagnetic materials.

**Radiographic testing (RT)**: X-ray or gamma-ray imaging reveals internal defects that no surface method can detect. Procedure: Place a radiation source (X-ray tube, 100-300 kV for steel up to 50 mm thick; or iridium-192 gamma source for field work) on one side of the weld. Place photographic film or a digital detector on the opposite side. Radiation passes through the weld; internal defects (porosity, slag inclusions, incomplete fusion, cracking) absorb less radiation than solid metal and appear as dark spots or lines on the radiograph. Exposure time: 1-10 minutes for film, seconds for digital. Interpretation requires training — the radiograph is a 2D projection of a 3D object, so flaw depth is indeterminate without multiple exposures at different angles. RT detects volumetric defects (porosity >1-2% of wall thickness, slag inclusions >2% of wall thickness) reliably. Does not detect tight, planar cracks oriented perpendicular to the radiation beam.

**Ultrasonic testing (UT)**: A piezoelectric transducer (1-10 MHz probe, typically 2-5 MHz for steel welds) sends high-frequency sound waves into the weld. Sound reflects from internal boundaries (cracks, lack of fusion, porosity) and returns to the transducer. The time-of-flight and amplitude of reflected signals reveal flaw depth, size, and orientation. UT detects planar defects (cracks, lack of sidewall fusion) that radiography misses, and provides depth information that RT cannot. Requires: calibration blocks (IIW V1 block or DIN block) of the same material and thickness as the weld, couplant gel (water, oil, or glycerin to transmit sound between probe and workpiece), and a trained operator to interpret the A-scan display. Surface must be smooth (grind weld cap flush for best contact). UT is the most versatile single technique for weld inspection but requires the most operator skill. Combining RT and UT provides complementary detection of both volumetric and planar defects for critical welds.

**Acceptance criteria**: Define defect acceptance limits before inspection begins. Common standards: porosity shall not exceed 2% of weld cross-sectional area; any single pore shall not exceed 3 mm diameter; cracks are unacceptable in structural welds; incomplete penetration limited to 10% of weld depth for non-critical joints, zero for pressure-containing welds. slag inclusions shall not exceed 10 mm length or 2 mm width. For pressure vessels and structural steel, follow established codes (ASME Section IX for pressure vessels, AWS D1.1 for structural steel) which specify permitted defect sizes by weld joint category and inspection method.

**Inspection sequence**: For a critical structural weld, apply methods in order: (1) visual inspection of every weld, no exceptions; (2) magnetic particle or dye penetrant for all surface-breaking defect detection on steel; (3) radiographic or ultrasonic testing for internal defects on designated critical joints (pressure vessel seams, structural column splices, crane hook welds). Document all inspection results in the weld map — a drawing showing every weld joint, its inspection method, acceptance status, and inspector's initials. Rejects are marked for repair (gouge out defective weld metal, re-weld, re-inspect using the same method that detected the defect). Repair welds are limited to two attempts; if the defect persists after two repairs, the joint must be cut out and rewelded entirely, and the welding procedure re-evaluated. Non-critical welds (shop fixtures, non-structural brackets, temporary jigs) require only visual inspection, freeing inspection resources for the joints where failure would be consequential.
- **Welder qualification**: Each welder performs a qualification test coupon (welding sample) that is destructively tested (bend test and macro-etch) to verify their technique before they are authorized to weld production joints. Qualification records document the process (SMAW, GTAW, etc.), position (flat, horizontal, vertical, overhead), material thickness range, and electrode type. A welder qualified in the flat position is not authorized to weld overhead without separate qualification testing.

## TIG Welding (GTAW — Gas Tungsten Arc Welding)

> **Node ID**: machine-tools.joining.tig-welding

Tungsten Inert Gas welding uses a non-consumable tungsten electrode to establish the arc, with inert shielding gas (argon or helium) protecting the weld pool. A separate filler rod is added manually or automatically. TIG produces the highest-quality welds of any arc process — clean, precise, and free of spatter. It is the preferred process for stainless steel, aluminum, titanium, and all thin-wall work where appearance and integrity matter.

**Principle**: A DC or AC arc melts the base metal between a sharp tungsten electrode (Ø 1.0-4.8 mm, 2% thoriated or lanthanated tungsten) and the workpiece. The inert gas shield prevents oxidation of the molten pool. Filler metal, when required, is fed separately into the leading edge of the pool.

**Shielding gases**:
- **Argon**: The standard TIG shielding gas for all materials. Flow rate 8-15 L/min for manual welding, 15-25 L/min for automated. Argon provides stable arc initiation and a quiet, controllable weld pool. Suitable for steel, stainless steel, aluminum (AC), copper, and titanium.
- **Helium**: Higher ionization potential produces a hotter, wider arc — deeper penetration on thick aluminum and copper. Flow rate 15-25 L/min. More expensive than argon. Often used as Ar/He mix (50/50 or 70/30) for heavy aluminum.
- **Argon-hydrogen (H₂ 2-5%)**: Reduces surface oxides on stainless steel, increases travel speed. ONLY for austenitic stainless steel — hydrogen causes cracking in ferritic/martensitic steels and porosity in aluminum.

**Power supply parameters by material**:

| Material | Thickness | Current (A) | Voltage (V) | Polarity | Electrode Ø | Filler Ø | Gas |
|----------|-----------|-------------|-------------|----------|-------------|----------|-----|
| Mild steel | 1.5 mm | 60-90 | 10-13 | DCEN | 1.6 mm | 1.6 mm | Ar |
| Mild steel | 3 mm | 90-130 | 12-15 | DCEN | 2.4 mm | 2.4 mm | Ar |
| Mild steel | 6 mm | 130-200 | 13-17 | DCEN | 3.2 mm | 3.2 mm | Ar |
| Stainless 304 | 1.5 mm | 50-80 | 10-12 | DCEN | 1.6 mm | 1.6 mm | Ar |
| Stainless 304 | 3 mm | 80-120 | 11-14 | DCEN | 2.4 mm | 2.4 mm | Ar |
| Aluminum 6061 | 1.5 mm | 50-80 | 12-16 | AC | 1.6 mm | 1.6 mm | Ar |
| Aluminum 6061 | 3 mm | 100-150 | 14-18 | AC | 2.4 mm | 2.4 mm | Ar |
| Aluminum 6061 | 6 mm | 150-220 | 16-22 | AC | 3.2 mm | 3.2 mm | Ar/He |
| Titanium Gr.2 | 1.5 mm | 50-80 | 10-13 | DCEN | 1.6 mm | 1.6 mm | Ar |
| Titanium Gr.2 | 3 mm | 80-130 | 11-15 | DCEN | 2.4 mm | 2.4 mm | Ar |

**DCEN (electrode negative)**: 70% heat in workpiece — deeper penetration. Used for steel, stainless, titanium, copper, nickel alloys.

**AC**: Alternates between DCEP (electrode positive half-cycle — cleans aluminum oxide surface) and DCEN (workpiece positive half-cycle — penetration). Required for aluminum and magnesium. Modern inverter power supplies provide adjustable AC balance (60-90% EN) to control cleaning vs. penetration.

**Titanium welding — critical precautions**: Titanium absorbs oxygen, nitrogen, and hydrogen at temperatures above 500°C, causing severe embrittlement. The entire heat-affected zone (HAZ) and root side must be shielded. Use a trailing gas shield (a cup or shoe extending 25-50 mm behind the torch) and back-purge the root with argon. Discoloration indicates contamination: silver = good, straw = acceptable, blue/purple = marginal, white/gray = reject.

**Applications for semiconductor equipment**: Orbital TIG welding of stainless steel tubing for gas distribution systems (orbital weld heads rotate the torch 360° around the tube joint automatically — produces repeatable, X-ray-quality welds). Vacuum chamber internal corners and penetrations. Titanium process tube welding with trailing shields.

**Orbital TIG for tube welding**: Automated orbital welding uses a enclosed weld head that clamps around the tube, with the tungsten electrode and gas cup rotating around the joint. Parameters: tube OD 6-76 mm, wall thickness 0.5-3 mm, current 30-150 A depending on wall thickness. Produces consistent, repeatable welds with full penetration and minimal oxidation — essential for high-purity gas distribution in semiconductor fabs. Computer-controlled power supplies store weld programs (pulse/sync frequency, current levels, rotation speed) for each tube size.

## MIG Welding (GMAW — Gas Metal Arc Welding)

> **Node ID**: machine-tools.joining.mig-welding

Gas Metal Arc Welding uses a continuously fed consumable wire electrode, melted by the arc and deposited into the joint. Shielding gas protects the weld pool. MIG is faster than TIG or SMAW — deposition rates of 2-8 kg/hour vs. 1-3 kg/hour for SMAW. The tradeoff is slightly lower weld quality and less control over the weld pool compared to TIG.

**Principle**: Wire feed mechanism (push or pull type) feeds solid wire electrode (Ø 0.6-1.6 mm) through the contact tip in the welding gun. The arc melts the wire tip and base metal simultaneously. Droplets transfer from wire to weld pool. Shielding gas flows through the gun nozzle, displacing air from the arc zone.

**Shielding gases by material**:
- **Mild steel**: 75% Ar / 25% CO₂ (C25 mix — most common, good penetration and bead appearance). Pure CO₂ is cheaper but produces more spatter and a harsher arc. Flow rate 12-20 L/min.
- **Stainless steel**: 98% Ar / 2% O₂ or 90% He / 7.5% Ar / 2.5% CO₂ (tri-mix). The small O₂ or CO₂ addition stabilizes the arc and improves wetting.
- **Aluminum**: 100% Ar (always). Flow rate 20-30 L/min — aluminum requires higher flow due to its high thermal conductivity.
- **Copper alloys**: 100% Ar or Ar/He mix. High preheat (200-400°C) required for thick sections.

**Transfer modes** (determined by current, voltage, and wire diameter):

- **Short-circuit transfer (dip transfer)**: Low voltage (16-20 V), low current (100-180 A for 0.8 mm wire). Wire touches the weld pool, creating a short circuit. Pinch force detaches the droplet. Works in all positions (flat, horizontal, vertical, overhead). Lowest heat input — suitable for thin sheet metal (0.8-3 mm). Some spatter.
- **Globular transfer**: Medium voltage (22-26 V), medium current (180-250 A). Large droplets form at wire tip and detach by gravity. Restricted to flat and horizontal positions. Moderate spatter. Rarely used in production — a transition mode between short-circuit and spray.
- **Spray transfer**: High voltage (26-32 V), high current (220-350 A for 0.8-1.0 mm wire). Fine droplets stream across the arc in a conical spray pattern. Very stable, virtually spatter-free. Restricted to flat and horizontal positions. High deposition rate (3-6 kg/hour). Requires >80% argon in shielding gas.
- **Pulsed spray transfer**: Inverter power supply alternates between a high peak current (spray transfer) and a low background current (no transfer). Provides spray-transfer quality in all positions at lower average heat input. The most versatile MIG mode — requires a synergic (programmed) power supply.

**Typical parameters**:

| Wire Ø | Material | Current (A) | Voltage (V) | Wire Feed (m/min) | Transfer Mode | Gas |
|--------|----------|-------------|-------------|-------------------|---------------|-----|
| 0.8 mm | Mild steel | 100-180 | 16-20 | 5-10 | Short-circuit | 75Ar/25CO₂ |
| 0.8 mm | Mild steel | 220-280 | 26-30 | 10-15 | Spray | 75Ar/25CO₂ |
| 1.0 mm | Mild steel | 180-300 | 20-28 | 5-12 | Short/spray | 75Ar/25CO₂ |
| 1.2 mm | Mild steel | 250-380 | 26-32 | 6-12 | Spray | 75Ar/25CO₂ |
| 1.0 mm | Al 5356 | 150-250 | 20-26 | 7-14 | Spray/pulse | Ar |
| 1.2 mm | SS 308L | 180-280 | 22-28 | 5-10 | Short/pulse | 98Ar/2O₂ |

**Advantages over SMAW**: 2-4× faster deposition rate, no slag removal (flux-core MIG has slag, solid wire MIG does not), continuous welding without stopping to change electrodes, better suitability for automation and robotics.

**Limitations**: Equipment is more complex (wire feeder, gas supply), less portable than SMAW, wind disrupts gas shielding (outdoor use impractical), and weld quality is sensitive to parameter settings (voltage, wire feed speed, stick-out length must be matched).

## Resistance Welding (Spot & Seam)

> **Node ID**: machine-tools.joining.resistance-welding

Resistance welding generates heat by passing high current through the workpieces held together under pressure between two electrodes. No filler metal, no shielding gas, no flux — the process uses the electrical resistance of the workpieces themselves to produce the weld. Extremely fast (cycle times measured in cycles of AC mains — 0.02-0.5 seconds) and easily automated.

**Principle**: Two copper alloy electrodes clamp the overlapping workpieces. A high current (typically 5,000-20,000 A) flows through the stack. The highest resistance in the circuit is at the interface between the two workpieces (sheet-to-sheet contact resistance), generating a molten nugget. Electrode force (1-10 kN) maintains contact and consolidates the nugget as it solidifies.

**Spot welding parameters**:

| Sheet Thickness (each) | Electrode Force (kN) | Current (kA) | Squeeze Time (cycles) | Weld Time (cycles) | Hold Time (cycles) |
|------------------------|---------------------|-------------|----------------------|--------------------|--------------------|
| 0.5 mm | 1.0-1.5 | 5-7 | 5-10 | 5-8 | 5-10 |
| 0.8 mm | 1.5-2.5 | 6-9 | 8-15 | 8-12 | 8-15 |
| 1.0 mm | 2.0-3.5 | 7-10 | 10-20 | 10-15 | 10-20 |
| 1.5 mm | 3.0-5.0 | 9-13 | 15-30 | 15-25 | 15-25 |
| 2.0 mm | 4.0-7.0 | 11-16 | 20-40 | 20-30 | 20-30 |
| 3.0 mm | 6.0-10.0 | 14-20 | 30-60 | 30-50 | 30-50 |

*Note: 1 cycle at 50 Hz = 20 ms; at 60 Hz = 16.7 ms*

**Electrode materials**: Class 2 copper-chromium-zirconium (CuCrZr) electrodes — high conductivity (≥75% IACS), hardness 130-150 HV, maintained tip diameter by periodic dressing (machining the tip face flat). RWMA (Resistance Welder Manufacturers Association) standardized electrode shapes: pointed (Type A), dome (Type B), flat (Type C), offset (Type D).

**Seam welding**: Roller electrodes replace stationary tips. The rollers rotate continuously, producing a series of overlapping spot welds that form a continuous gas-tight or liquid-tight seam. Used for fuel tanks, radiators, drums, and container bodies. Wheel width 5-12 mm, current 8-15 kA, speed 0.5-5 m/min. Overlap between spots: 30-50% of nugget diameter.

**Projection welding**: Small embossed projections (dimples) stamped into one workpiece concentrate current at discrete points. Multiple projections welded simultaneously — ideal for nuts, bolts, and brackets welded to sheet metal. The projection collapses during welding, providing a self-aligning joint.

**Applications**: Automotive body assembly (4,000-6,000 spot welds per car), appliance cabinets, battery tab welding (resistance welding of thin nickel tabs to lithium-ion cell terminals — 0.5-2 kA, 5-20 ms), and electrical contacts.

## Electron Beam Welding (EBW)

> **Node ID**: machine-tools.joining.electron-beam

Electron beam welding uses a focused beam of high-velocity electrons to melt and fuse metals in a vacuum chamber. The beam produces an extremely deep, narrow weld (depth-to-width ratio 10:1 to 30:1) with minimal heat input, minimal distortion, and no oxidation. EBW is the premier process for joining refractory metals, dissimilar metals, and precision components that must maintain dimensional stability — including vacuum chambers and semiconductor equipment.

**Principle**: A heated tungsten or lanthanum hexaboride (LaB₆) cathode emits electrons (thermionic emission). An accelerating voltage of 30-150 kV accelerates the electrons to 0.3-0.6 times the speed of light. Electromagnetic focusing coils (magnetic lenses) focus the beam to a spot diameter of 0.1-1.0 mm on the workpiece. Kinetic energy converts to heat on impact, producing a deep keyhole that penetrates the full thickness of the joint. The workpiece is mounted on a CNC-controlled motion stage inside a vacuum chamber.

**Equipment parameters**:

| Parameter | Range | Notes |
|-----------|-------|-------|
| Accelerating voltage | 30-60 kV (low-voltage), 60-150 kV (high-voltage) | Higher voltage = deeper penetration, smaller spot |
| Beam current | 10-100 mA (low-voltage), 1-50 mA (high-voltage) | Beam power = voltage × current |
| Beam power | 0.3-30 kW (typical), up to 100 kW (heavy section) | Penetration depth proportional to power |
| Vacuum level | 10⁻² to 10⁻⁴ mbar (medium vacuum), 10⁻⁴ to 10⁻⁶ mbar (high vacuum) | Better vacuum = less beam scattering = deeper penetration |
| Travel speed | 5-100 mm/s | Higher speed = narrower weld, lower penetration |
| Spot size | 0.1-1.0 mm | Focused by electromagnetic lenses |
| Penetration depth | Up to 200 mm in steel, 300 mm in aluminum | Single-pass, full penetration |

**Penetration capability by material and power**:

| Material | 5 kW | 10 kW | 20 kW | 50 kW |
|----------|------|-------|-------|-------|
| Steel | 12 mm | 20 mm | 35 mm | 60 mm |
| Aluminum | 18 mm | 30 mm | 50 mm | 80 mm |
| Titanium | 15 mm | 25 mm | 40 mm | 70 mm |
| Copper | 8 mm | 14 mm | 22 mm | 40 mm |

**Vacuum chamber requirements**: The workpiece chamber must be evacuated before each weld cycle. Chamber sizes range from 0.01 m³ (small parts) to 100+ m³ (large aerospace structures). Pumping time: 1-10 minutes for medium vacuum (rotary vane + roots blower), 5-30 minutes for high vacuum (rotary vane + turbomolecular). Chamber construction: stainless steel (304L or 316L), water-cooled, with viewing ports and sealed feedthroughs for electrical connections and motion stages.

**Non-vacuum EBW**: The beam exits the vacuum through a series of differential pressure stages. No vacuum chamber needed for the workpiece, but beam scattering limits penetration to ~25 mm in steel and working distance to 10-25 mm. Used for high-speed welding of automotive components.

**Critical for vacuum chamber fabrication**: EBW produces welds with zero porosity and zero contamination — the vacuum environment prevents oxidation and the deep narrow penetration eliminates the need for multiple passes on thick sections. For UHV (ultra-high vacuum) chambers, EB welds have significantly lower outgassing rates than TIG welds because the narrow heat-affected zone minimizes the volume of material that absorbs and later releases gases. Leak rates at EB welds: ≤10⁻¹⁰ mbar·L/s (measured by helium mass spectrometer leak detector), compared to 10⁻⁸ to 10⁻⁹ mbar·L/s for TIG welds.

## Ultrasonic Welding & Wire Bonding

> **Node ID**: machine-tools.joining.ultrasonic-bonding

Ultrasonic welding joins metals by applying high-frequency mechanical vibration under pressure — no melting, no filler, no flux. The ultrasonic vibration breaks surface oxides and brings the clean metal surfaces into intimate contact, forming a solid-state metallurgical bond. This is the dominant process for wire bonding in semiconductor packaging, as well as for joining thin foils, wires, and dissimilar metal combinations.

**Principle**: A piezoelectric transducer (typically PZT — lead zirconate titanate) converts electrical energy at 20-60 kHz into mechanical vibration. A booster amplifies the vibration amplitude (typically 2-30 μm peak-to-peak at the tool tip). A sonotrode (wedge or capillary tip) applies the vibration to the workpiece under clamping force (0.5-50 N). The cyclic shear stress at the interface breaks oxide layers and creates metal-to-metal contact at asperities. Bonding occurs through diffusion and micro-welding at the contact points.

**Wire bonding parameters (semiconductor packaging)**:

| Parameter | Gold Ball Bonding | Aluminum Wedge Bonding |
|-----------|------------------|----------------------|
| Wire diameter | 18-50 μm (25 μm typical) | 18-50 μm (25 μm typical) |
| Wire material | 99.99% Au (softened) | 99.99% Al, Al-1% Si |
| Frequency | 60-120 kHz | 40-80 kHz |
| Ultrasonic power | 0.1-2.0 W | 0.3-3.0 W |
| Bonding force | 0.1-0.5 N | 0.2-1.0 N |
| Bonding time | 10-50 ms | 20-100 ms |
| Temperature | 150-250°C (thermosonic) or 25°C (room temp) | 25°C (room temperature) |
| Bond shape | Ball (first bond) + wedge (second bond) | Wedge-wedge |
| Pull strength (25μm Au) | 40-80 mN | — |
| Pull strength (25μm Al) | — | 30-60 mN |

**Gold ball bonding (thermosonic)**: A small spark (EFO — electronic flame-off) melts the end of the gold wire, forming a free-air ball (1.5-2.5× wire diameter). The capillary descends, pressing the ball onto the bond pad while applying ultrasonic energy and heat (150-250°C). The ball deforms into a "nail head" shape. The capillary then rises, feeding wire to the second bond position, where it forms a stitch (wedge) bond. Wire is then clamped and broken. Typical throughput: 8-15 bonds/second. For gold wire, thermosonic bonding (heat + ultrasonic) produces the strongest bonds.

**Aluminum wedge bonding (ultrasonic)**: A wedge tool presses the aluminum wire against the bond pad while applying ultrasonic vibration. No heat required — room-temperature bonding. The second bond is formed similarly. Aluminum wire is preferred for high-reliability applications (avoiding gold-aluminum intermetallic "purple plague" formation at elevated temperatures). Also used for heavy aluminum ribbon (0.5-2.0 mm × 0.1-0.3 mm) for power semiconductor packaging.

**Larger-scale ultrasonic metal welding**: For joining sheet metal, foils, and battery tabs. Parameters: 20 kHz frequency, amplitude 30-50 μm, clamping force 0.5-5 kN, weld time 0.1-1.0 seconds. Joins aluminum to copper (battery interconnects), copper to copper (bus bars), and multiple layers of thin foil (lithium battery electrode tabs). No melting — the solid-state bond preserves the metallurgical structure and avoids brittle intermetallic phases that form when dissimilar metals are melted together.

**Applications in semiconductor equipment**: Wire bonding is the most common interconnection method in IC packaging (>10 trillion wire bonds produced annually worldwide). Also used for sensor packaging, MEMS device interconnection, and hybrid microcircuit assembly.

## Friction Stir Welding (FSW)

> **Node ID**: machine-tools.joining.friction-stir

Friction stir welding is a solid-state joining process — the metal is heated to a plasticized state but never melted. A rotating cylindrical tool with a profiled probe pin is plunged into the joint line between two abutting workpieces and traversed along the seam. Frictional heat from the rotating tool softens the metal, and the tool's pin stirs the plasticized material from both sides together, creating a consolidated joint on cooling. No filler metal, no shielding gas, no consumables beyond the tool itself.

**Principle**: The tool consists of a shoulder (typically Ø 10-25 mm) and a probe pin (Ø 3-10 mm, length matching workpiece thickness). The rotating tool (500-1500 RPM) generates frictional heat at the shoulder-workpiece interface (primary heat source) and the pin-workpiece interface. Material temperature rises to 70-90% of melting point but does not melt. The rotating pin stirs the plasticized material, and the shoulder's forging action consolidates the weld nugget behind the pin.

**Parameters**:

| Parameter | Range | Notes |
|-----------|-------|-------|
| Tool rotation speed | 500-1500 RPM | Higher RPM = more heat input |
| Traverse (feed) speed | 50-200 mm/min (steel), 100-1000 mm/min (aluminum) | Lower speed = more heat per unit length |
| Tool tilt angle | 1-3° from vertical | Ensures shoulder contact at trailing edge |
| Plunge depth | Shoulder penetrates 0.1-0.3 mm below surface | Controls forging force |
| Downward force | 5-50 kN | Machine rigidity essential |
| Tool material (for Al) | H13 tool steel, MP159 (nickel-cobalt alloy) | Good to 600°C surface temperature |
| Tool material (for steel) | PCBN (polycrystalline cubic boron nitride), tungsten-rhenium | Must withstand 1000°C+ |

**Key advantages**: No porosity (no solidification from liquid), no cracking (no melt), lower distortion than fusion welding (lower peak temperature), ability to join unweldable aluminum alloys (2xxx, 7xxx series — aerospace alloys that are hot-crack susceptible in fusion welding), and dissimilar metal joints (aluminum to steel, aluminum to copper) without brittle intermetallic layers.

**Aluminum welding by alloy and thickness**:

| Alloy Series | Thickness Range | Rotation (RPM) | Feed (mm/min) | Application |
|--------------|----------------|----------------|----------------|-------------|
| 2xxx (e.g., 2024) | 3-12 mm | 800-1200 | 100-400 | Aerospace fuselage panels |
| 5xxx (e.g., 5083) | 3-25 mm | 500-1000 | 100-600 | Marine, cryogenic tanks |
| 6xxx (e.g., 6061) | 3-15 mm | 800-1500 | 200-800 | Structural, general fabrication |
| 7xxx (e.g., 7075) | 3-12 mm | 800-1200 | 80-300 | Aerospace wing spars |

**Limitations**: Keyhole at tool exit point (must be filled or trimmed), requires rigid clamping and backing bar, limited to straight or gently curved joints (tool must access both sides), and tool wear in steel welding (PCBN tools cost $2,000-10,000 each).

## Laser Welding

> **Node ID**: machine-tools.joining.laser-welding

Laser welding uses a focused high-power laser beam to melt and fuse metal. The process offers extremely high power density (10⁴-10⁷ W/cm²), producing deep narrow welds with minimal heat input and minimal thermal distortion. Laser welding is easily automated and can weld at high speeds with precise control of penetration depth.

**Laser types for welding**:

- **CO₂ laser**: Gas laser, wavelength 10.6 μm (far infrared). Power range 100 W to 20 kW. Cannot be delivered through fiber optic — must use mirror beam delivery. High absorption in non-metals, moderate absorption in metals (reflectivity issue with copper and aluminum at 10.6 μm). Wall-plug efficiency 5-10%. Used for steel, stainless steel, and polymer welding.
- **Fiber laser**: Solid-state laser, wavelength 1.06-1.09 μm (near infrared). Power range 100 W to 30 kW. Delivered through flexible fiber optic cable — easily integrated with robots and CNC machines. Higher absorption in metals than CO₂. Wall-plug efficiency 25-35%. The dominant choice for modern industrial laser welding. Ytterbium-doped fiber.
- **Disk laser**: Solid-state laser, wavelength 1.03 μm. Power range 100 W to 16 kW. Similar to fiber laser but with a thin disk crystal gain medium. Excellent beam quality at high power.
- **Pulsed Nd:YAG laser**: Wavelength 1.064 μm. Peak power up to 20 kW in pulsed mode, average power 100-500 W. Used for spot welding, seam welding of thin materials, and micro-welding (medical devices, electronics). Pulse duration 0.1-20 ms.

**Welding modes**:

- **Conduction mode**: Low power density (10⁴-10⁵ W/cm²). Laser heats the surface; heat conducts into the workpiece. Shallow, wide weld profile. Depth-to-width ratio ~1:1. Used for thin materials (<1 mm), spot welding, and aesthetic welds. Power: 100-500 W. Speed: 0.5-10 m/min.
- **Keyhole mode**: High power density (10⁶-10⁷ W/cm²). Laser vaporizes a narrow channel (keyhole) through the workpiece thickness. The keyhole is stabilized by the balance between vapor pressure (opening) and surface tension/molten metal hydrostatic pressure (closing). Deep, narrow weld. Depth-to-width ratio 5:1 to 15:1. Power: 1-20 kW. Speed: 1-20 m/min. The standard mode for industrial laser welding.

**Parameters by material and thickness (fiber laser, keyhole mode)**:

| Material | Thickness | Power (kW) | Speed (m/min) | Shield Gas | Notes |
|----------|-----------|-----------|----------------|------------|-------|
| Mild steel | 2 mm | 2-3 | 3-6 | Ar or N₂ | High-speed sheet welding |
| Mild steel | 5 mm | 4-6 | 1.5-3 | Ar | Full penetration, square butt |
| Mild steel | 10 mm | 8-12 | 0.8-1.5 | Ar | Deep keyhole welding |
| Stainless 304 | 2 mm | 2-3 | 3-8 | Ar or He | Excellent results |
| Stainless 304 | 5 mm | 4-6 | 1-3 | Ar | High-quality, low distortion |
| Aluminum 6061 | 2 mm | 3-4 | 4-8 | Ar | High reflectivity — need high power density |
| Aluminum 6061 | 5 mm | 5-8 | 1.5-4 | Ar/He | He addition improves coupling |
| Copper C110 | 2 mm | 4-6 | 2-5 | Ar | Very high reflectivity at 1 μm — challenging |
| Titanium Gr.2 | 2 mm | 2-3 | 3-6 | Ar + trailing shield | Must shield HAZ from oxygen |

**Advantages**: Very high welding speed (5-20× faster than TIG for thin materials), minimal distortion (narrow HAZ), easy automation (no contact, no electrode wear), ability to weld difficult geometries (line-of-sight access only), and clean welds (no slag, no spatter in keyhole mode with proper parameters).

**Limitations**: High capital cost ($50,000-500,000 for laser + optics), high reflectivity of copper and gold at common laser wavelengths (requires high power density to initiate keyhole), strict joint fit-up requirements (gap tolerance typically <0.15× material thickness), and safety requirements (Class IV laser — enclosed work cell with interlocked doors, laser safety eyewear rated for the wavelength).

## Diffusion Bonding (Hot Isostatic Press Joining)

> **Node ID**: machine-tools.joining.diffusion-bonding

Diffusion bonding is a solid-state joining process where two atomically clean metal surfaces are brought into intimate contact under pressure at elevated temperature. Atomic diffusion across the interface eliminates the joint line, producing a bond indistinguishable from the parent metal. No melting, no filler, no cast microstructure — the process preserves the wrought microstructure and properties of the base metal.

**Principle**: Three conditions are required simultaneously:
1. **Temperature**: 50-80% of the absolute melting point (Kelvin). At this temperature, atomic mobility is sufficient for diffusion across the interface within practical timescales.
2. **Pressure**: 1-10 MPa (uniaxial) or 50-200 MPa (isostatic, via hot isostatic pressing — HIP). Pressure ensures intimate surface contact by plastically deforming surface asperities (microscopic peaks).
3. **Time**: 30-120 minutes at temperature. Sufficient time for diffusion to eliminate the interface porosity.

**Surface preparation**: Critical — surfaces must be flat and clean. Machine to ≤0.4 μm Ra surface finish, degrease in acetone or alcohol, and assemble immediately. Surface oxide films must be broken by the applied pressure or dissolved by the elevated temperature. Some material combinations benefit from a thin interlayer (e.g., nickel foil between steel and titanium).

**Parameters by material combination**:

| Material Pair | Temperature (°C) | Pressure (MPa) | Time (min) | Atmosphere | Joint Strength |
|---------------|------------------|----------------|------------|------------|----------------|
| Ti-Ti (CP Ti) | 850-950 | 2-5 | 60-120 | Vacuum (<10⁻³ mbar) | 100% parent |
| Ti-6Al-4V to itself | 900-950 | 2-10 | 60-180 | Vacuum | 95-100% parent |
| SS 316L to itself | 1000-1100 | 3-10 | 60-120 | Vacuum or H₂ | 90-95% parent |
| Cu-Cu (OFHC) | 800-900 | 3-8 | 30-90 | Vacuum | 95-100% parent |
| Al 6061 to itself | 450-525 | 5-15 | 60-180 | Vacuum | 85-95% parent |
| Ti to SS 304 (with Ni interlayer) | 850-950 | 5-10 | 60-120 | Vacuum | 80-90% weaker |
| Cu to Al (with Ni interlayer) | 450-525 | 5-15 | 60-180 | Vacuum | 80-90% weaker |

**Dissimilar metal joining**: Diffusion bonding excels at joining metals that cannot be fusion-welded together due to formation of brittle intermetallic compounds. The solid-state process limits intermetallic growth to a thin diffusion zone (1-10 μm) rather than the thick, brittle intermetallic layers that form in fusion welding. With appropriate interlayers (Ni, Ag, or Cu foils 1-10 μm thick), joints between titanium/steel, copper/steel, aluminum/steel, and other difficult pairs achieve 80-95% of the weaker parent metal's strength.

**Hot Isostatic Pressing (HIP) bonding**: Instead of uniaxial press, the assembly is placed in a HIP vessel. Argon gas pressure (50-200 MPa) is applied isostatically at elevated temperature. The uniform pressure bonds complex internal surfaces that cannot be reached by uniaxial loading. Used for bonding honeycomb core sandwich panels, internal cooling channels in turbine blades, and complex hollow structures.

**Applications for semiconductor equipment**: Diffusion bonding creates ultra-high vacuum (UHV) chamber joints with zero internal voids and no outgassing weld metal. Used for bonding copper heat sinks to silicon carbide substrates in power electronics, creating hermetic feedthrough assemblies, and fabricating complex internal-channel heat exchangers for laser and power semiconductor cooling.

## Vacuum-Specific Welding Applications

Advanced joining processes are critical enablers for vacuum technology and semiconductor equipment manufacturing. Vacuum chambers, gas distribution manifolds, and process tools require welds that are not merely strong but hermetically sealed, clean (low outgassing), and free of trapped volumes (virtual leaks).

**Hermetic sealing**: A hermetic seal prevents gas penetration. In vacuum applications, hermeticity is quantified by helium leak rate. Acceptable leak rates by application:

| Application | Max Leak Rate (mbar·L/s) | Test Method |
|-------------|--------------------------|-------------|
| Rough vacuum systems | ≤10⁻⁵ | Bubble test, pressure decay |
| High vacuum systems | ≤10⁻⁸ | Helium leak detector (MSLD) |
| UHV systems | ≤10⁻⁹ | Helium leak detector (MSLD) |
| Semiconductor process chambers | ≤10⁻⁹ | Helium leak detector (MSLD) |
| Hermetic IC packages | ≤10⁻⁸ (MIL-STD-883) | Helium bomb + leak detect |
| Cryogenic vessels | ≤10⁻⁸ | Helium leak detector (MSLD) |

**Helium mass spectrometer leak detection (MSLD)**: The most sensitive leak detection method. A mass spectrometer tuned to helium (mass 4) detects helium leaking into or out of the test volume. Two modes:
- **Vacuum mode (outside-in)**: Evacuate the test volume. Spray helium on the exterior. The MSLD samples the interior — any helium detected indicates a leak path. Sensitivity: 10⁻¹² mbar·L/s.
- **Sniffer mode (inside-out)**: Pressurize the test volume with helium. Scan the exterior with a sniffer probe connected to the MSLD. Sensitivity: 10⁻⁷ mbar·L/s. Used for large vessels where evacuation is impractical.

**Virtual leaks**: Trapped volumes inside a vacuum chamber that slowly release gas, preventing the chamber from reaching its ultimate pressure. Caused by: unvented threaded holes (blind holes with screws — always drill a vent hole through the screw or use vented screws), gaps between overlapping surfaces (diffusion-bond or weld continuously), and porous weld metal (use EB welding or high-quality TIG with proper shielding).

**Internal bore welding**: Many vacuum chambers require welding on internal surfaces (e.g., welding a fitting to the inside of a tube). TIG with a specialized bore welding torch — a long, slender torch body with a 90° or 180° head that reaches inside tubes ≥50 mm diameter. Orbital bore weld heads are available for automated internal welds.

**Stainless steel for vacuum chambers**: Type 304L or 316L stainless steel (the "L" designates low carbon ≤0.03%, which prevents sensitization and intergranular corrosion in the heat-affected zone). For UHV: electropolished internal surfaces (Ra ≤0.1 μm) reduce outgassing by removing the amorphous surface layer and creating a thin, protective chromium oxide passive layer. All internal welds must be full-penetration with backpurge shielding.

**Dissimilar metal joining for vacuum**: Vacuum feedthroughs require joining ceramic (alumina) insulators to metal flanges (stainless steel or Kovar). Methods: active metal brazing (using Ti-containing braze alloy that wets both ceramic and metal), or diffusion bonding. For glass-to-metal seals, matched expansion coefficient glasses and metals (e.g., borosilicate glass with Kovar alloy, both ~5×10⁻⁶/°C expansion). See [Glass — Advanced](../glass/advanced.md) for glass-to-metal seal techniques.

## Expanded Method Selection Guide

The table below expands the earlier selection guide to include all joining methods covered in this file.

| Method | Temp Range | Joint Strength | Equipment | Best For |
|--------|-----------|---------------|-----------|----------|
| Soft soldering | 180-250°C | 20-50 MPa | Soldering iron, flux | Electrical connections, plumbing, sheet metal seams |
| Silver brazing | 620-780°C | 150-300 MPa | Torch, silver alloy, flux | Fine mechanisms, instruments, dissimilar metals |
| Brass brazing | 870-950°C | 150-250 MPa | Forge/torch, brass rod, borax | Structural joints, cast iron, pipe fittings |
| Riveting | Cold or 900°C | 80-150 MPa (shear) | Hammer, dolly, rivet snap | Structural steel, boilers, bridges, ship hulls |
| Forge welding | 1200-1300°C | 250-400 MPa | Forge, anvil, hammer, flux | Iron/low-carbon steel bars, chains, composite billets |
| Oxy-acetylene | ~3100°C | 300-450 MPa | Torch, gas cylinders, regulators | Sheet metal, repair, cutting, general fabrication |
| SMAW (stick) | ~6000°C (arc) | 350-480 MPa | Power supply, electrodes | Structural steel, heavy fabrication, pressure vessels |
| TIG (GTAW) | ~6000°C (arc) | 350-520 MPa | Power supply, tungsten electrode, gas | Stainless steel, aluminum, titanium, thin-wall tubing |
| MIG (GMAW) | ~6000°C (arc) | 350-500 MPa | Wire feed, power supply, gas | High-deposition fabrication, sheet metal, automotive |
| Resistance (spot) | N/A (resistance) | 200-400 MPa (shear) | Spot welder, copper electrodes | Sheet metal lap joints, automotive, appliance panels |
| Electron beam | N/A (KE→heat) | 350-550 MPa | Vacuum chamber, EB gun, CNC stage | Vacuum chambers, aerospace, refractory metals, precision |
| Ultrasonic | N/A (solid-state) | 30-80 mN (25μm wire) | Ultrasonic transducer, capillary/wedge | Wire bonding (IC packaging), foil joining, battery tabs |
| Friction stir | N/A (solid-state) | 300-500 MPa | FSW machine, rotating tool | Aluminum alloys (2xxx, 7xxx), dissimilar metal joints |
| Laser | N/A (photon→heat) | 350-520 MPa | Laser, optics, shielding gas | High-speed welding, precision, automation |
| Diffusion bonding | 50-80% Tm | 80-100% parent | Hot press or HIP, vacuum furnace | Dissimilar metals, UHV components, complex internals |

---

*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*
