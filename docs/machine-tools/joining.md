# Metal Joining

> **Node ID**: machine-tools.joining
> **Domain**: Machine Tools Bootstrap
> **Timeline**: Years 5-30
> **Outputs**: forge_welds, brazed_joints, soldered_joints, riveted_joints, welded_joints, acetylene

## Overview

Metal joining is the capability that makes machinery possible. Individual forged or cast parts are rarely useful alone — they must be assembled into structures, mechanisms, pressure vessels, and frames. This file covers the six primary joining methods in bootstrap order: forge welding (earliest, requires only a forge and hammer), brazing and soldering (require filler alloys), riveting (mechanical joining requiring no heat at the joint), oxy-acetylene welding (requires gas production infrastructure), and arc welding/SMAW (requires electrical power).

Each method occupies a specific niche defined by temperature, joint strength, equipment requirements, and the materials it can join. No single method replaces all others — a complete industrial shop needs all six.

For the metallurgy of producing iron and steel stock to be joined, see [Iron & Steel](../metals/iron-steel.md). For the electrical infrastructure needed by arc welding, see [Electricity](../energy/electricity.md).

## Forge Welding

The oldest solid-state welding method, achievable as soon as wrought iron is produced in a bloomery forge. No filler metal required — the base metal itself fuses under heat and pressure.

**Principle**: Heat iron or low-carbon steel to a temperature where the surface becomes pasty (~1200-1300°C). Place the pieces together and strike firmly with a hammer. Heat and pressure cause atomic diffusion across the interface, producing a solid-state weld with no melted zone.

**Fluxes** (essential — without flux, surface oxide prevents metal-to-metal contact):
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

---

*Part of the [Bootciv Tech Tree](../) • [Machine Tools](./) • [All Domains](../)*
