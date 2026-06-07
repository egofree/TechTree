# Welding

> **Node ID**: machine-tools.joining.welding
> **Domain**: [Machine Tools Bootstrap](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`energy.electricity`](../energy/electricity.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`energy.steam-power`](../energy/steam-power.md), [`machine-tools.joining.diffusion-bonding`](./joining.md), [`machine-tools.joining.electron-beam`](./joining.md), [`machine-tools.joining.friction-stir`](./joining.md), [`machine-tools.joining.laser-welding`](./joining.md), [`machine-tools.joining.mig-welding`](./joining.md), [`machine-tools.joining.resistance-welding`](./joining.md), [`machine-tools.joining.tig-welding`](./joining.md), [`machine-tools.joining.ultrasonic-bonding`](./joining.md)
> **Timeline**: Years 5-70
> **Outputs**: forge_welds, welded_joints, acetylene, tig_welds, mig_welds, resistance_welds, electron_beam_welds, friction_stir_welds, laser_welds, diffusion_bonds, hermetic_seals
> **Critical**: Yes — fusion and solid-state welding processes for assembling structural, pressure-bearing, and vacuum-tight metal assemblies


Welding covers all fusion and solid-state welding processes from the earliest forge welding through advanced electron beam and laser welding. For filler-alloy joining methods (brazing and soldering), see [Brazing & Soldering](./brazing-soldering.md). For mechanical fastening with rivets, see [Riveting](./riveting.md). For the parent overview of all joining methods, see [Metal Joining](./joining.md).

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

**Construction steps (scarf joint)**:
1. Taper both bar ends to a scarf angle of 10-15°. Overlap length: 2-3× bar thickness (for 20 mm bar, scarf length 40-60 mm). Shape the scarf so the thin edges of each piece will overlap the thick body of the other.
2. Clean both scarf surfaces to bare metal with a wire brush or file. Remove all scale and dirt.
3. Apply borax flux as a dry powder to both scarf surfaces. Coat evenly — any unfluxed area will not weld.
4. Heat both pieces simultaneously in a charcoal or coal forge with forced air from bellows. Bring to bright yellow-white (~1250-1300°C). The surface should appear to shimmer or "sweat" — scale flakes away exposing bright metal. Do not exceed 1300°C (metal burns).
5. Remove from forge. Position pieces on the anvil face with the scarfs overlapping in the correct orientation.
6. Strike immediately with firm, rapid blows — first a light tap to set alignment, then heavy hammering to expel slag and consolidate the weld. Work from the center outward to squeeze flux and scale out of the joint. Complete the weld within 10-20 seconds before the metal cools below welding temperature.
7. Reheat and re-strike if the joint is longer than one hammering session allows.

**Calibration**: Bend the welded bar in a vise or over the anvil horn through 90°. A sound weld bends without opening at the seam. A poor weld cracks at the seam — caused by oxide inclusion, insufficient heat, or insufficient flux. For critical applications (chains, tools), test a sample weld to destruction: clamp one end and hammer the other until it breaks. The weld should fail in the parent metal, not at the seam.

**Expected performance**: Joint strength: 80-95% of parent metal for a skilled smith on wrought iron or low-carbon steel. Scarf joint tensile strength: 250-350 MPa. Weld time: 10-20 seconds of hammering per joint (after heating). Forge cycle: 5-15 minutes including heating.

**Materials specifications**: Wrought iron or low-carbon steel bar stock (0.05-0.3% C), borax flux (Na₂B₄O₇, commercial grade), charcoal or coal forge fuel, 2-4 kg blacksmith's hammer.

**Strengths**:
- Requires only a forge, anvil, and hammer — no industrial infrastructure needed
- Produces a solid-state weld with no melted zone — no cast metal microstructure, no porosity
- Can join wrought iron and low-carbon steel without any filler material

**Weaknesses**:
- Only joins iron and low-carbon steel — high-carbon steel, cast iron, and non-ferrous metals cannot be forge welded by conventional methods
- Operator skill is critical — temperature judgment and hammer timing determine weld quality
- Joint strength is 80-95% of parent metal at best — not suitable for the highest-strength applications

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

**Construction steps for oxy-acetylene welding setup**:
1. Secure both cylinders upright in a cart or chained to a wall. Install regulators — oxygen first (right-hand thread), then acetylene (left-hand thread). Tighten connections with a wrench — do not over-tighten (brass fittings deform).
2. Connect hoses: green/blue hose to oxygen regulator outlet, red hose to acetylene regulator outlet. Connect torch end — verify correct hose-to-valve matching before proceeding.
3. Set regulator pressures: open oxygen cylinder valve fully, then adjust regulator screw to set working pressure to 0.2-0.3 MPa (for 1.6 mm tip, 2 mm steel plate). Open acetylene cylinder valve 1/2 turn only, set working pressure to 0.03-0.05 MPa.
4. Open torch acetylene valve 1/4 turn. Ignite with a spark lighter (not a match or lighter — keep hands away from the tip). Adjust to a soft, sooty flame ~50 mm long.
5. Gradually open torch oxygen valve until the flame becomes neutral: sharp inner cone 2-5 mm long, blue-white, with a pale blue outer envelope. This is the welding flame (~3100°C).

**Calibration**: Check flame type — neutral flame has a sharp, well-defined inner cone with no feather. A carburizing flame shows a distinct secondary feather beyond the inner cone (excess acetylene). An oxidizing flame has a shorter, noisier inner cone (excess oxygen). For most steel welding, use a neutral flame. Test by welding a bead on scrap plate — the bead should be smooth, convex, and uniform width with no porosity, spatter, or undercut.

**Expected performance**: Welding speed: 2-5 mm/second. Penetration: 1-3 mm per pass on steel (full penetration up to 3 mm in single pass, bevel for thicker plate). Tensile strength: 300-450 MPa (matching mild steel base metal). Cutting speed: 200-500 mm/min on 6 mm plate.

**Materials specifications**: Oxygen cylinder (40 L, 15 MPa, rated for gas service), acetylene cylinder (40 L, 1.5 MPa, acetone-filled with porous mass), welding torch (brass body, 0.5-3 mm tips), regulators (diaphragm type, dual gauge), hoses (rubber, reinforced, 3-5 m length), mild steel filler rod (1.5-3 mm diameter).

**Flame types and adjustment**:
- **Neutral flame**: Equal O₂ and C₂H₂ flow. Inner cone ~2-5 mm, blue-white, sharp-edged. Outer envelope pale blue. Temperature ~3100°C. The standard flame for welding steel.
- **Carburizing (reducing) flame**: Excess acetylene. Longer, feathered inner cone with a distinct secondary feather. Adds carbon to the weld pool. Used for brazing and welding aluminum alloys.
- **Oxidizing flame**: Excess oxygen. Shorter inner cone, noisy, pale. Adds oxygen to weld pool — causes porosity in steel but useful for brazing brass and copper.

**Welding technique**: Hold torch at ~45° angle to work. Move steadily along joint at 2-5 mm/second. Dip filler rod into leading edge of the molten puddle — rod melts and adds metal to the joint.

**Cutting**: Fitted with a cutting attachment (additional oxygen lever and preheat flames). Heat steel to bright red (~900°C) with preheat flames, then press the oxygen lever — a jet of pure O₂ reacts exothermically with hot steel. Molten iron oxide is blown through the cut by the oxygen jet. Kerf width 1-3 mm. Cuts steel up to 300+ mm thick. Cannot cut copper, aluminum, or stainless steel.

**Strengths**:
- Portable — gas cylinders can be brought to any work site without electrical power
- Dual-purpose: welds and cuts steel with the same equipment (torch + cutting attachment)
- Flame temperature (3100°C) is easily controlled by adjusting gas ratios

**Weaknesses**:
- Acetylene generation requires calcium carbide, which requires an electric arc furnace — not available at the earliest bootstrap stage
- Wide heat-affected zone (5-15 mm) causes significant distortion in thin sheet metal
- Oxygen and acetylene cylinders are heavy and require careful handling — acetylene can detonate under pressure

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

**Construction steps for a SMAW butt weld (mild steel, 6 mm plate)**:
1. Clean joint to bare metal (grind or file — remove rust, paint, oil, moisture). Clean at least 25 mm back from each edge.
2. Prepare edges: bevel plates to 30° included angle (60° total), 2 mm root gap, 1.5 mm root face. Clamp in position with a backing bar if available.
3. Clamp workpiece to grounded steel welding table. Connect return lead (ground clamp) to workpiece, ensuring clean metal-to-metal contact.
4. Insert electrode in insulated holder. Set amperage to 100-120 A for 3.2 mm E7018 electrode (start at manufacturer's recommendation, adjust by sound — correct arc sounds like frying bacon; too high sounds like loud buzzing with excessive spatter; too low produces a sticky, irregular arc).
5. Strike arc by tapping or scraping electrode on work (like a match), then lifting to maintain 2-4 mm arc length (~1× electrode diameter). Maintain this distance as electrode melts and you move along the joint.
6. Travel speed: 2-5 mm/second. Angle: 10-15° from vertical in the direction of travel (drag angle). The molten pool should be 10-15 mm long and slightly wider than the electrode.
7. Multi-pass technique for 6 mm plate: root pass (stringer bead, no weave), fill passes (weave beads, oscillate electrode side-to-side 2-3× electrode diameter), cap pass (slight weave for uniform bead appearance). Clean slag between each pass (chip with chipping hammer, wire brush).
8. Slag removal: After each pass, chip slag with chipping hammer. Wire brush the bead. Inspect for porosity, undercut, and slag inclusion before the next pass.

**Calibration**: Run a test bead on scrap plate of the same material and thickness. Check: bead width should be 2-3× electrode diameter. Penetration: break the test coupon and examine the cross-section — root penetration must be full through the plate thickness. Hardness: file test the weld metal and heat-affected zone — both should resist a standard file equally. Visual: bead should be uniform, convex, with smooth transition to base metal (no undercut >0.5 mm).

**Expected performance**: Weld tensile strength: 350-480 MPa (E7018 on mild steel). Deposition rate: 1-3 kg/hour. Duty cycle: 60% at rated current (weld 6 minutes, cool 4). Electrode consumption: ~0.5-1.0 electrodes per 100 mm of weld (3.2 mm, 6 mm plate).

**Materials specifications**: Mild steel plate (0.15-0.25% C, 6 mm thickness), E7018 electrodes (3.2 mm diameter, stored dry at 80-120°C in electrode oven), angle grinder with grinding disc, wire brush, chipping hammer, welding table (steel, grounded).

**Strengths**:
- Simple equipment — power supply, electrode holder, and electrodes suffice; no gas supply needed
- Works outdoors in wind (unlike MIG/TIG where wind disrupts gas shielding)
- Electrode selection covers all positions (flat, horizontal, vertical, overhead) and material conditions (clean, rusty, painted)

**Weaknesses**:
- Slow deposition rate (1-3 kg/hour) compared to MIG (2-8 kg/hour)
- Slag must be chipped and brushed between passes — adds time and labor
- Requires stopping to change electrodes every 250-350 mm of weld (electrode consumption)

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

**AC**: Alternates between DCEP (electrode positive half-cycle — cleans aluminum oxide surface) and DCEN (workpiece positive half-cycle — penetration). Required for aluminum and magnesium.

**Titanium welding — critical precautions**: Titanium absorbs oxygen, nitrogen, and hydrogen at temperatures above 500°C, causing severe embrittlement. The entire heat-affected zone (HAZ) and root side must be shielded. Use a trailing gas shield (a cup or shoe extending 25-50 mm behind the torch) and back-purge the root with argon. Discoloration indicates contamination: silver = good, straw = acceptable, blue/purple = marginal, white/gray = reject.

**Strengths**:
- Highest weld quality of any arc process — no spatter, no slag, precise heat control
- Works on all metals including stainless steel, aluminum, titanium, copper, and nickel alloys
- AC mode provides oxide cleaning on aluminum — no mechanical cleaning needed during welding

**Weaknesses**:
- Slow deposition rate (0.5-2 kg/hour) — 2-4× slower than MIG
- Requires external shielding gas supply (argon cylinders) — not portable for field work
- Higher operator skill required — both hands are occupied (torch + filler rod), and foot pedal amperage control adds complexity

## MIG Welding (GMAW — Gas Metal Arc Welding)

> **Node ID**: machine-tools.joining.mig-welding

Gas Metal Arc Welding uses a continuously fed consumable wire electrode, melted by the arc and deposited into the joint. Shielding gas protects the weld pool. MIG is faster than TIG or SMAW — deposition rates of 2-8 kg/hour vs. 1-3 kg/hour for SMAW. The tradeoff is slightly lower weld quality and less control over the weld pool compared to TIG.

**Principle**: Wire feed mechanism (push or pull type) feeds solid wire electrode (Ø 0.6-1.6 mm) through the contact tip in the welding gun. The arc melts the wire tip and base metal simultaneously. Droplets transfer from wire to weld pool. Shielding gas flows through the gun nozzle, displacing air from the arc zone.

**Shielding gases by material**:
- **Mild steel**: 75% Ar / 25% CO₂ (C25 mix — most common, good penetration and bead appearance). Pure CO₂ is cheaper but produces more spatter and a harsher arc. Flow rate 12-20 L/min.
- **Stainless steel**: 98% Ar / 2% O₂ or 90% He / 7.5% Ar / 2.5% CO₂ (tri-mix).
- **Aluminum**: 100% Ar (always). Flow rate 20-30 L/min — aluminum requires higher flow due to its high thermal conductivity.
- **Copper alloys**: 100% Ar or Ar/He mix. High preheat (200-400°C) required for thick sections.

**Typical parameters**:

| Wire Ø | Material | Current (A) | Voltage (V) | Wire Feed (m/min) | Transfer Mode | Gas |
|--------|----------|-------------|-------------|-------------------|---------------|-----|
| 0.8 mm | Mild steel | 100-180 | 16-20 | 5-10 | Short-circuit | 75Ar/25CO₂ |
| 0.8 mm | Mild steel | 220-280 | 26-30 | 10-15 | Spray | 75Ar/25CO₂ |
| 1.0 mm | Mild steel | 180-300 | 20-28 | 5-12 | Short/spray | 75Ar/25CO₂ |
| 1.2 mm | Mild steel | 250-380 | 26-32 | 6-12 | Spray | 75Ar/25CO₂ |
| 1.0 mm | Al 5356 | 150-250 | 20-26 | 7-14 | Spray/pulse | Ar |
| 1.2 mm | SS 308L | 180-280 | 22-28 | 5-10 | Short/pulse | 98Ar/2O₂ |

**Strengths**:
- 2-4× faster deposition rate than SMAW — continuous wire feed eliminates electrode changes
- No slag to remove (solid wire MIG) — cleaner finished welds
- Easy to learn — single-hand operation, no filler rod manipulation needed

**Weaknesses**:
- Wind disrupts gas shielding — outdoor use impractical without wind screens
- Equipment is more complex (wire feeder, gas supply) and less portable than SMAW
- Weld quality is sensitive to parameter settings — voltage, wire feed speed, and stick-out length must be matched

## Resistance Welding (Spot & Seam)

> **Node ID**: machine-tools.joining.resistance-welding

Resistance welding generates heat by passing high current through the workpieces held together under pressure between two electrodes. No filler metal, no shielding gas, no flux. Extremely fast (cycle times 0.02-0.5 seconds) and easily automated.

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

**Strengths**:
- Extremely fast — cycle times of 0.02-0.5 seconds per weld
- No consumables (no filler metal, no shielding gas, no flux)
- Easily automated — consistent weld quality at high production rates (4,000-6,000 spot welds per car)

**Weaknesses**:
- Limited to overlapping sheet metal joints — cannot join plates edge-to-edge
- Electrode tips wear and require periodic dressing (machining flat) to maintain weld quality
- No non-destructive inspection method for internal nugget quality — peel testing or destructive cross-sectioning required for process qualification

## Electron Beam Welding (EBW)

> **Node ID**: machine-tools.joining.electron-beam

Electron beam welding uses a focused beam of high-velocity electrons to melt and fuse metals in a vacuum chamber. The beam produces an extremely deep, narrow weld (depth-to-width ratio 10:1 to 30:1) with minimal heat input, minimal distortion, and no oxidation.

**Equipment parameters**:

| Parameter | Range | Notes |
|-----------|-------|-------|
| Accelerating voltage | 30-60 kV (low-voltage), 60-150 kV (high-voltage) | Higher voltage = deeper penetration, smaller spot |
| Beam current | 10-100 mA (low-voltage), 1-50 mA (high-voltage) | Beam power = voltage × current |
| Beam power | 0.3-30 kW (typical), up to 100 kW (heavy section) | Penetration depth proportional to power |
| Vacuum level | 10⁻² to 10⁻⁴ mbar (medium vacuum), 10⁻⁴ to 10⁻⁶ mbar (high vacuum) | Better vacuum = less beam scattering |
| Travel speed | 5-100 mm/s | Higher speed = narrower weld, lower penetration |
| Spot size | 0.1-1.0 mm | Focused by electromagnetic lenses |
| Penetration depth | Up to 200 mm in steel, 300 mm in aluminum | Single-pass, full penetration |

**Strengths**:
- Deep, narrow welds with depth-to-width ratio 10:1 to 30:1 — minimal heat input and distortion
- Vacuum environment eliminates all oxidation — critical for reactive metals (titanium, zirconium)
- Single-pass welding of thick sections (up to 200 mm steel) — no multi-pass requirement

**Weaknesses**:
- Requires a vacuum chamber — chamber sizes limited, pump-down time 1-30 minutes per cycle
- Very high capital cost — $200,000-2,000,000 for EB welding systems
- X-ray generation at high voltages requires lead shielding and radiation safety protocols

## Ultrasonic Welding & Wire Bonding

> **Node ID**: machine-tools.joining.ultrasonic-bonding

Ultrasonic welding joins metals by applying high-frequency mechanical vibration under pressure — no melting, no filler, no flux. The ultrasonic vibration breaks surface oxides and brings the clean metal surfaces into intimate contact, forming a solid-state metallurgical bond.

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
| Pull strength (25μm Au) | 40-80 mN | — |
| Pull strength (25μm Al) | — | 30-60 mN |

**Strengths**:
- Solid-state bond — no melting, no intermetallic formation, no thermal damage to nearby components
- Room-temperature aluminum bonding requires no heat — compatible with temperature-sensitive devices
- Extremely fast: 8-15 bonds/second for gold ball bonding

**Weaknesses**:
- Limited to thin wires and foils — cannot join structural metal thicknesses (>0.5 mm)
- Gold-aluminum bonds can develop "purple plague" (AuAl₂ intermetallic) at elevated temperatures — reliability concern
- Requires precise control of bonding force, power, and time — parameter windows are narrow (±10-20%)

## Friction Stir Welding (FSW)

> **Node ID**: machine-tools.joining.friction-stir

Friction stir welding is a solid-state joining process — the metal is heated to a plasticized state but never melted. A rotating cylindrical tool with a profiled probe pin is plunged into the joint line between two abutting workpieces and traversed along the seam.

**Parameters**:

| Parameter | Range | Notes |
|-----------|-------|-------|
| Tool rotation speed | 500-1500 RPM | Higher RPM = more heat input |
| Traverse (feed) speed | 50-200 mm/min (steel), 100-1000 mm/min (aluminum) | Lower speed = more heat per unit length |
| Tool tilt angle | 1-3° from vertical | Ensures shoulder contact at trailing edge |
| Plunge depth | Shoulder penetrates 0.1-0.3 mm below surface | Controls forging force |
| Downward force | 5-50 kN | Machine rigidity essential |

**Strengths**:
- No porosity (no solidification from liquid), no cracking (no melt)
- Can join unweldable aluminum alloys (2xxx, 7xxx series — aerospace alloys)
- Dissimilar metal joints (aluminum to steel, aluminum to copper) without brittle intermetallic layers

**Weaknesses**:
- Keyhole at tool exit point — must be filled or trimmed in finished parts
- Requires rigid clamping and backing bar — the tool applies 5-50 kN downward force
- Tool wear in steel welding: PCBN tools cost $2,000-10,000 each

## Laser Welding

> **Node ID**: machine-tools.joining.laser-welding

Laser welding uses a focused high-power laser beam to melt and fuse metal. The process offers extremely high power density (10⁴-10⁷ W/cm²), producing deep narrow welds with minimal heat input and minimal thermal distortion.

**Parameters by material and thickness (fiber laser, keyhole mode)**:

| Material | Thickness | Power (kW) | Speed (m/min) | Shield Gas | Notes |
|----------|-----------|-----------|----------------|------------|-------|
| Mild steel | 2 mm | 2-3 | 3-6 | Ar or N₂ | High-speed sheet welding |
| Mild steel | 5 mm | 4-6 | 1.5-3 | Ar | Full penetration, square butt |
| Mild steel | 10 mm | 8-12 | 0.8-1.5 | Ar | Deep keyhole welding |
| Stainless 304 | 2 mm | 2-3 | 3-8 | Ar or He | Excellent results |
| Aluminum 6061 | 2 mm | 3-4 | 4-8 | Ar | High reflectivity — need high power density |
| Copper C110 | 2 mm | 4-6 | 2-5 | Ar | Very high reflectivity at 1 μm |
| Titanium Gr.2 | 2 mm | 2-3 | 3-6 | Ar + trailing shield | Must shield HAZ from oxygen |

**Strengths**:
- Very high welding speed (5-20× faster than TIG for thin materials)
- Minimal distortion — narrow HAZ and low total heat input
- Easy automation — no contact, no electrode wear, programmable beam path

**Weaknesses**:
- High capital cost ($50,000-500,000 for laser + optics)
- Strict joint fit-up requirements (gap tolerance typically <0.15× material thickness)
- Class IV laser safety requirements — enclosed work cell with interlocked doors, laser safety eyewear rated for the wavelength

## Diffusion Bonding (Hot Isostatic Press Joining)

> **Node ID**: machine-tools.joining.diffusion-bonding

Diffusion bonding is a solid-state joining process where two atomically clean metal surfaces are brought into intimate contact under pressure at elevated temperature. Atomic diffusion across the interface eliminates the joint line, producing a bond indistinguishable from the parent metal.

**Parameters by material combination**:

| Material Pair | Temperature (°C) | Pressure (MPa) | Time (min) | Atmosphere | Joint Strength |
|---------------|------------------|----------------|------------|------------|----------------|
| Ti-Ti (CP Ti) | 850-950 | 2-5 | 60-120 | Vacuum (<10⁻³ mbar) | 100% parent |
| Ti-6Al-4V to itself | 900-950 | 2-10 | 60-180 | Vacuum | 95-100% parent |
| SS 316L to itself | 1000-1100 | 3-10 | 60-120 | Vacuum or H₂ | 90-95% parent |
| Cu-Cu (OFHC) | 800-900 | 3-8 | 30-90 | Vacuum | 95-100% parent |
| Al 6061 to itself | 450-525 | 5-15 | 60-180 | Vacuum | 85-95% parent |
| Ti to SS 304 (with Ni interlayer) | 850-950 | 5-10 | 60-120 | Vacuum | 80-90% weaker |

**Strengths**:
- Joint strength approaches 100% of parent metal — no cast microstructure, no porosity
- Can join dissimilar metals that are impossible to fusion-weld (titanium to steel, copper to aluminum)
- Produces zero-distortion joints — no thermal stresses, no warping

**Weaknesses**:
- Requires vacuum furnace or HIP vessel — major capital equipment
- Surface preparation is critical — surfaces must be machined to ≤0.4 μm Ra and kept scrupulously clean
- Long cycle times (30-180 minutes at temperature) — not suitable for high-volume production

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

**Dissimilar metal joining for vacuum**: Vacuum feedthroughs require joining ceramic (alumina) insulators to metal flanges (stainless steel or Kovar). Methods: active metal brazing (using Ti-containing braze alloy that wets both ceramic and metal), or diffusion bonding. For glass-to-metal seals, matched expansion coefficient glasses and metals (e.g., borosilicate glass with Kovar alloy, both ~5×10⁻⁶/°C expansion). See [Glass — Advanced](../glass/advanced.md) for glass-to-metal seal techniques.

## Weld Quality Inspection

Weld inspection ensures structural integrity in pressure vessels, load-bearing structures, and critical machinery. Five methods, in order of increasing complexity and detection capability:

**Visual inspection (VT)**: The first and most important inspection method. Examine every weld visually (with 5-10× magnification where needed) before applying any other technique. Check for: undercut (groove melted into base metal at the toe of the weld, reducing cross-section), porosity (visible surface pores from gas trapped during solidification), cracking (hot cracks at the weld centerline or cold cracks in the heat-affected zone), incomplete penetration (root not fully fused), excessive reinforcement (weld bead too high above the base metal surface, creating stress concentration), and spatter (metal droplets adhering to base metal surface). Visual inspection catches 80-90% of weld defects when performed by a trained inspector. Requires adequate lighting (500+ lux at the weld surface) and clean weld surfaces (remove slag and spatter first).

**Dye penetrant testing (PT)**: Detects surface-breaking cracks, porosity, and seams that are too fine for unaided visual inspection. Procedure: (1) Clean the weld surface thoroughly (solvent wipe). (2) Apply red penetrant dye (fluorescent or visible red dye with low surface tension) to the surface. Allow 10-30 minutes dwell time for the dye to seep into surface defects by capillary action. (3) Remove excess penetrant from the surface with solvent or water rinse. (4) Apply white developer (chalk suspension in solvent) — the developer draws the red dye back out of any defects, producing a bright red indication against the white background. Detection capability: surface cracks as narrow as 0.5 mm deep and 1 μm wide. Works on any non-porous material — ferrous and non-ferrous metals, ceramics, plastics. Does NOT detect subsurface defects.

**Magnetic particle testing (MT)**: For ferromagnetic materials only (carbon steel, alloy steel, cast iron). Magnetize the weld area using a portable electromagnetic yoke (AC or DC) or permanent magnets. Spray the surface with fine iron particles (dry powder, or wet suspension in oil/water with fluorescent coating). Magnetic flux leakage at surface and near-surface cracks attracts the iron particles, forming a visible indication that outlines the defect. Detects surface cracks and near-surface flaws to a depth of ~2-6 mm below the surface (depending on flaw size and orientation). Fluorescent magnetic particle testing under UV light is the most sensitive variation, detecting cracks as fine as 0.025 mm wide. Faster and more sensitive than dye penetrant for steel, but limited to ferromagnetic materials.

**Radiographic testing (RT)**: X-ray or gamma-ray imaging reveals internal defects that no surface method can detect. Procedure: Place a radiation source (X-ray tube, 100-300 kV for steel up to 50 mm thick; or iridium-192 gamma source for field work) on one side of the weld. Place photographic film or a digital detector on the opposite side. Radiation passes through the weld; internal defects (porosity, slag inclusions, incomplete fusion, cracking) absorb less radiation than solid metal and appear as dark spots or lines on the radiograph. Exposure time: 1-10 minutes for film, seconds for digital. Interpretation requires training — the radiograph is a 2D projection of a 3D object, so flaw depth is indeterminate without multiple exposures at different angles.

**Ultrasonic testing (UT)**: A piezoelectric transducer (1-10 MHz probe, typically 2-5 MHz for steel welds) sends high-frequency sound waves into the weld. Sound reflects from internal boundaries (cracks, lack of fusion, porosity) and returns to the transducer. The time-of-flight and amplitude of reflected signals reveal flaw depth, size, and orientation. UT detects planar defects (cracks, lack of sidewall fusion) that radiography misses, and provides depth information that RT cannot. Requires: calibration blocks (IIW V1 block or DIN block) of the same material and thickness as the weld, couplant gel (water, oil, or glycerin to transmit sound between probe and workpiece), and a trained operator to interpret the A-scan display.

**Acceptance criteria**: Define defect acceptance limits before inspection begins. Common standards: porosity shall not exceed 2% of weld cross-sectional area; any single pore shall not exceed 3 mm diameter; cracks are unacceptable in structural welds; incomplete penetration limited to 10% of weld depth for non-critical joints, zero for pressure-containing welds. Slag inclusions shall not exceed 10 mm length or 2 mm width. For pressure vessels and structural steel, follow established codes (ASME Section IX for pressure vessels, AWS D1.1 for structural steel).

**Welder qualification**: Each welder performs a qualification test coupon (welding sample) that is destructively tested (bend test and macro-etch) to verify their technique before they are authorized to weld production joints. Qualification records document the process (SMAW, GTAW, etc.), position (flat, horizontal, vertical, overhead), material thickness range, and electrode type.

**Strengths**:
- Visual + PT/MT + RT/UT covers surface, near-surface, and internal defects comprehensively
- VT alone catches 80-90% of defects when performed by a trained inspector
- UT provides depth information on internal flaws that no other method can

**Weaknesses**:
- Radiographic testing requires radiation sources (X-ray tube or gamma isotope) — significant safety infrastructure
- UT interpretation requires extensive training — 40-80 hours minimum for basic certification
- No single method detects all defect types — multiple methods must be combined for critical welds

## Method Selection Guide

| Method | Temp Range | Joint Strength | Equipment | Best For |
|--------|-----------|---------------|-----------|----------|
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

## Safety

- **Eye protection**: Full welding helmet with shade #10-#14 filter lens for arc and oxy-acetylene work. UV radiation from the arc causes "welder's flash" (photokeratitis — sunburn of the cornea, 24-48 hours of extreme pain and temporary blindness).
- **Fire prevention**: Hot metal, sparks, and slag are ignition sources. Clear the area 10+ m of combustibles. Have water bucket, sand, and fire extinguisher ready. Sparks travel 5-10 m from welding and cutting operations.
- **Burns**: Use pliers, tongs, and leather gloves to handle hot work. Leather gloves (gauntlet length) for arc welding; leather apron or heavy cotton jacket (no synthetic fabrics — they melt onto skin).
- **Fumes and ventilation**: Welding fumes (metal oxides, ozone). Work in well-ventilated areas. Respirators (N95 minimum) for confined-space work. Forced ventilation or fume extraction for enclosed spaces.
- **Hearing protection**: Hammering (forge welding) produces impulse noise >100 dB. Earplugs or earmuffs rated NRR 25+.
- **Electrical safety**: Dry gloves, dry clothing, insulated electrode holder for arc welding. Secondary voltage (20-80 V open circuit) can be lethal in damp environments. Never weld in wet conditions.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Forge weld seam cracks open during 90° bend test | Insufficient heat (<1200°C), oxide inclusion from missing flux, or hammering started before welding temperature reached | Heat to bright yellow-white (1250-1300°C) until surface "sweats"; apply borax flux (Na₂B₄O₇) evenly to both scarf surfaces; complete hammering within 10-20 seconds before metal cools below welding temperature |
| Oxy-acetylene weld bead shows porosity and spatter on 2 mm mild steel | Flame is oxidizing (excess O₂ — short, noisy inner cone) instead of neutral, or working pressure incorrect | Adjust to neutral flame: sharp inner cone 2-5 mm, blue-white, with pale blue outer envelope; set oxygen to 0.2-0.3 MPa and acetylene to 0.03-0.05 MPa for 1.6 mm tip |
| SMAW weld has undercut >0.5 mm at bead toe on 6 mm plate (E7018, 3.2 mm) | Amperage too high (>130 A for 3.2 mm electrode), or travel speed too slow producing excessive weld pool | Reduce amperage to 100-120 A; increase travel speed to 2-5 mm/second; correct arc sounds like frying bacon (loud buzzing = too high; sticky irregular arc = too low) |
| TIG weld on titanium shows blue/purple discoloration (acceptable = silver/straw) | Insufficient shielding — HAZ exposed to oxygen/nitrogen above 500°C on trailing edge or root side | Add trailing gas shield extending 25-50 mm behind torch; back-purge root side with argon; wait 10-15 seconds after arc stops before moving torch away; reject white/gray discoloration |
| MIG weld has irregular, spatter-heavy bead on mild steel with 75Ar/25CO₂ | Wire feed speed mismatched to voltage, or contact tip-to-work distance (stick-out) too long (>12 mm) | Match parameters: 0.8 mm wire at 100-180 A / 16-20 V for short-circuit transfer; maintain stick-out at 6-10 mm; verify gas flow at 12-20 L/min |
| Resistance spot weld nugget too small or missing on 1.0 mm sheet (should use 7-10 kA, 2.0-3.5 kN) | Electrode tips worn/mushroomed, reducing current density, or squeeze time insufficient (<10 cycles at 50 Hz) | Dress electrode tips to original flat diameter; increase squeeze time to 10-20 cycles (200-400 ms at 50 Hz); verify electrode force at 2.0-3.5 kN with calibrated gauge |
| Friction stir weld shows tunnel defect or surface lack of fill | Traverse speed too high (>200 mm/min for steel) or plunge depth insufficient (shoulder <0.1 mm below surface) | Reduce traverse speed to 50-200 mm/min for steel (100-1000 mm/min for aluminum); set shoulder penetration to 0.1-0.3 mm below surface; increase downward force to 5-50 kN range |

## Cross-References

- [Brazing & Soldering](./brazing-soldering.md) — filler alloy joining at lower temperatures
- [Riveting](./riveting.md) — mechanical fastening with rivets
- [Metal Joining](./joining.md) — parent overview of all joining methods
- [Iron & Steel](../metals/iron-steel.md) — primary metals for welding
- [Specialty Alloys](../metals/alloys.md) — alloy weldability and filler metals
- [Electricity](../energy/electricity.md) — power for arc welding processes
- [Chemistry Index](../chemistry/index.md) — flux chemistry and shielding gases
- [Steam Power](../energy/steam-power.md) — boiler fabrication with welded joints
- [Metal Forming](../metals/forming.md) — shaping before joining
- [Machining](machining.md) — post-weld finishing and repair

---

*Part of the [Bootciv Tech Tree](../index.md) · [Machine Tools Bootstrap](./index.md) · [All Domains](../index.md)*