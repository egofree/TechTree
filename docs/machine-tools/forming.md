# Metal Forming

> **Node ID**: machine-tools.forming
> **Domain**: Machine Tools Bootstrap
> **Timeline**: Years 5-15
> **Outputs**: formed_metal_parts, bar_stock, sheet_metal, wire, plate, rod

### Overview

Metal forming reshapes solid metal through plastic deformation — applying force at controlled temperatures to change cross-section, bend, or elongate stock without removing material. Forming retains nearly 100% of the workpiece mass and produces the bar stock, sheet, wire, and shaped blanks that feed every downstream process: machine tools, construction, electrical wiring, and mechanisms.

The critical variables are **temperature** (hot vs cold working), **[force](../glossary/force.html)** (hammer, press, or roll), and **[reduction ratio](../glossary/reduction-ratio.html)** (how much cross-section changes per pass). Metals deform more easily when hot — yield strength drops by 60-80% above recrystallization temperature.

### Forging Temperatures by Metal

Every metal has a forging range — hot enough to be plastic, cool enough to avoid burning or crumbling.

| Metal | Forging Range | Color (approx.) | Notes |
|-------|--------------|-----------------|-------|
| Copper | 700–900°C | Dark cherry to orange | Very forgiving, wide working range. Oxidizes green. |
| Bronze (90/10 Cu/Sn) | 650–800°C | Dark red to cherry | Narrower range than copper — cracks if too cold, crumbles if too hot. |
| Wrought iron | 1000–1200°C | Bright orange to yellow | Must reheat frequently — loses heat fast. Sparks when hammered (slag). |
| Low-carbon steel (0.1–0.3% C) | 800–1150°C | Cherry to bright yellow | The workhorse forging metal. Wide range. |
| Medium-carbon steel (0.3–0.5% C) | 800–1100°C | Cherry to orange | Stronger but less ductile — avoid working below 800°C. |
| High-carbon steel (0.6–1.0% C) | 800–1050°C | Cherry to orange | Narrow range. Overheating causes burning (grain boundary melting). |

Below these ranges, metal work-hardens rapidly and may crack. Above them, the metal burns (grain boundaries oxidize, producing a crumbly, ruined forging that cannot be salvaged).

### Forge Work

**[Open-die forging](../glossary/open-die-forging.html)** (hand forging): Smith heats stock in a charcoal forge, positions on anvil, strikes with hammers or sledges. Shape controlled by hammer placement, stock rotation, and tooling (swages, fullers, flatters).
- **Drawing out**: Hammer along the length to reduce cross-section and elongate. Rotate 90° every few blows for square section.
- **Upsetting**: Hammer on end to thicken cross-section. Risk of buckling if length > 3× diameter.
- **Bending**: Heat bend zone, hammer over anvil horn. Minimum radius ~2× stock thickness.
- **Punching and drifting**: Drive punch through hot metal, enlarge with drift. Punch from both sides to meet in middle for cleaner holes.

**[Closed-die forging](../glossary/closed-die-forging.html)** (impression forging): Metal compressed between shaped dies containing the negative of the desired part. Flash (excess) squeezes out at parting line and is trimmed. Requires dies machined to tolerance (see [Iterative Bootstrap](./iterative-bootstrap.md)). Advantages: repeatable parts, good grain flow, near-net shape. Used for connecting rods, gear blanks, wrenches.

### Hammer Forming

**[Sledge hammer](../glossary/sledge-hammer.html)** (4–8 kg, two-handed): The fundamental heavy forging tool. One person holds work with tongs; a striker delivers sledge blows. Effective for drawing out bars 25–75 mm square, upsetting ends, driving punches. Blow force: ~10–25 kN.

**[Power hammer](../glossary/power-hammer.html)** (mechanized forging):
- **Helve hammer**: Beam pivoted at one end, hammer head at the other. Raised by cam on water-wheel shaft, falls by gravity. Stroke 30–60 cm, 50–150 kg blow equivalent. The first mechanized forging tool.
- **Tilt hammer**: Similar but tail is lifted. 80–200 blows/minute in early water-powered forges.
- **[Spring helve hammer](../glossary/spring-helve-hammer.html)** (intermediate build): Heavy timber frame, 15–40 kg head on leaf spring. Crank-driven, 150–300 blows/minute. Constructable with basic machine tools.
- **[Steam or air hammer](../glossary/steam-or-air-hammer.html)** (later): 500–5000 kg capacity. Requires [Steam Power](../energy/steam-power.md).

### Rolling Mill

Rolling reduces cross-section of heated metal by passing it between counter-rotating rolls. Each pass reduces thickness 10–30% and elongates proportionally.

**[Hand-operated rolling mill](../glossary/hand-operated-rolling-mill.html)** (the bootstrap starting point):
- Two hardened steel or cast iron rolls, 75–150 mm diameter, 150–300 mm face length. Mounted in a cast iron or fabricated steel frame with adjustable gap (screw-down mechanism).
- Drive: hand crank or foot treadle through gear reduction (3:1 to 6:1). Two operators — one cranks, one feeds stock.
- Capacity: hot rolling of copper, bronze, and soft iron bar up to ~10 mm thick. Cold rolling of copper and brass sheet to ~1 mm.
- Roll pressure: 50–150 kN for hot steel at 15–20% reduction.

**[Powered rolling mill](../glossary/powered-rolling-mill.html)** (water wheel or engine):
- Rolls 200–400 mm diameter, 400–800 mm face. Drive via gears or belt from water wheel (3–10 HP minimum).
- Can roll iron bar from 50 mm square bloom down to 10 mm round in 6–10 passes, reheating between passes.
- **Reduction per pass**: 15–25% for hot steel. Greater reduction causes excessive roll force and uneven deformation.
- **Roll material**: Cast iron for copper/brass. Forged or cast steel for iron/steel. Rolls must be harder than the workpiece.

**[Sheet rolling](../glossary/sheet-rolling.html)** (flat sheet from ingot):
1. Cast ingot (copper, brass, or steel) 20–40 mm thick. Soak at forging temperature 30–60 min.
2. Pass through rolls, reduce 2–3 mm per pass. Rotate 180° between passes for even reduction.
3. Reheat every 4–6 passes. Anneal at 500–700°C when reduction exceeds 40–50% from last anneal.
4. Target: copper sheet to 0.5 mm (hand mill) or 0.1 mm (powered mill).

### Wire Drawing

Wire drawing pulls metal rod through progressively smaller dies, reducing diameter and increasing length. Unlike rolling, wire drawing is done cold.

**[Draw plate](../glossary/draw-plate.html)** (the bootstrap tool): Hardened high-carbon steel (0.8–1.0% C) plate, 10–25 mm thick, with tapered holes graduating in size (e.g., 8.0 mm down to 1.0 mm in 0.5 mm steps). Each hole: ~30° included angle entrance, short straight bearing section (~1× diameter), back-relief.

**Procedure**:
1. **Point the rod**: File one end to a taper that fits through the first die.
2. **Lubricate**: Apply tallow, beeswax, or soap solution. Without lubrication, rod galls and sticks in die.
3. **[Pull through die](../glossary/pull-through-die.html)** with tongs or draw bench hook (chain drive with 0.5–1 m lever arm for wire > 2 mm). Pull force: 5–30 kN.
4. **Anneal** every 3–5 passes at 500–700°C for copper, 650–800°C for iron. Work hardening makes wire brittle without annealing.
5. **Reduction per pass**: 15–25% area reduction. Total from rod to finished wire: 80–95% area reduction.

**[Fine wire](../glossary/fine-wire.html)** (< 1 mm): Use draw bench with capstan (rotating drum). Speed 30–100 m/min for copper. Dies are tungsten carbide inserts. Copper wire down to 0.1 mm achievable — the wire for [electromagnetic coils](../energy/electricity.md).

### Sheet Metal Forming

**Bending**: Clamp sheet in vise or bending brake (hinged leaf brake — constructable from flat bar and angle iron). Minimum bend radius = 1× sheet thickness for soft metals, 2–3× for harder alloys.

**Seaming**: Fold edges of two sheets together and hammer flat (Pittsburgh seam, double seam). Produces airtight and watertight joints for ductwork and containers. No heat required.

**Raising and sinking**: Shape sheet into bowls and domes by hammering over stakes (shaped anvils). Raising = hammering outside (thins and curves). Sinking = hammering into a hollow. Copper and brass raise cold; iron requires heating.

**Spinning**: Clamp sheet against a form on a lathe. Apply pressure with a rounded tool while the mandrel rotates. Used for bowls, cups, reflectors. Requires a lathe (see [Iterative Bootstrap](./iterative-bootstrap.md)).

### Annealing Between Operations

Cold working accumulates strain, increasing hardness and reducing ductility. Annealing restores ductility by allowing recrystallization. **Rule of thumb**: anneal when cross-section has been reduced 40–50% from last anneal, or every 3–5 wire drawing passes.

| Metal | Anneal Temperature | Time | Cooling |
|-------|-------------------|------|---------|
| Copper | 500–700°C | 30–60 min | Air cool or water quench |
| Brass (70/30) | 400–600°C | 30–60 min | Air cool |
| Bronze | 600–700°C | 30–60 min | Air cool |
| Wrought iron | 700–900°C | 30–60 min | Air cool |
| Steel (low carbon) | 700–900°C | 30–60 min | Furnace cool (slow) |

### Safety Concerns

- **Flying sparks and scale**: Forge work produces hot metal fragments. Leather apron, safety glasses, and face shield for bloom consolidation. Keep fire extinguishing sand nearby.
- **Burns**: Metal at forging temperature (700–1200°C) causes instant deep burns on contact. Use properly fitting tongs — if stock slips from tongs, it flies. Test tongs by clamping cold stock and shaking hard before using on hot work.
- **Pinch points**: Rolling mills and draw benches produce crushing forces. Never place hands between rolls or near draw chain.
- **Repetitive strain**: Hammer forging limits productive hours to 4–6/day. Power hammers reduce this.
- **Carbon monoxide**: Charcoal and coal forges produce CO in enclosed spaces. Ventilate smithies — work outdoors or with open doors and roof vents.

### Press Brake Forming

**[Tonnage calculation](../glossary/tonnage-calculation.html)** for V-die bending: P = 650 × S² × L / V, where P = bending force (kN), S = sheet thickness (mm), L = bend length (mm), V = V-die opening width (mm). For example, bending 3 mm mild steel sheet 1000 mm long in a 24 mm V-die requires P = 650 × 9 × 1000 / 24 = 243.75 kN (~25 tonnes). The V-die opening is selected as V = 6-12 × S for mild steel; wider openings reduce tonnage but increase the inside bend radius.

**Springback compensation**: After bending, elastic recovery causes the actual bend angle to spring back 2-5° from the formed angle in mild steel and 5-10° in aluminum alloys. Compensate by overbending past the target angle. For a 90° bend in aluminum, set the ram to approximately 97°. Higher yield strength materials exhibit more springback; the effect decreases with larger bend radius relative to sheet thickness.

**Minimum bend radius**: Mild steel bends to approximately 1× sheet thickness (1t) without cracking on the outer surface. Aluminum requires 2-3t depending on alloy and temper: 5052-O soft temper bends to 1t, while 6061-T6 hardened temper needs 3t minimum. Bending below these limits causes grain boundary cracking along the outer fiber. Stainless steel, with its higher work-hardening rate, typically requires 2-2.5t even in the annealed condition.

**Press brake tooling**: The upper punch (V-blade) and lower V-die determine the bend geometry. Acute-angle punches (30° or 60° tip) allow bends tighter than 90°. Gooseneck punches clear previously-formed flanges on complex parts. Die shoulders should be polished to prevent marking the workpiece surface. Standard V-die widths range from 6 mm (for thin sheet) to 100 mm (for thick plate). A complete tooling set for a general shop includes punches and dies covering V = 6×, 8×, 10×, and 12× the maximum sheet thickness processed.

### Roll Forming

**[Progressive roll forming](../glossary/progressive-roll-forming.html)** produces long, continuous profiles from flat strip stock. The strip passes through 3-20 paired roller stations arranged in line, each station making a small incremental bend of 10-20°. Line speed: 1-2 m/min for heavy gauge material, up to 30 m/min for light gauge. The process suits high-volume production of uniform cross-sections: C-channels, hat sections, corrugated roofing panel profiles. Tooling cost is high (each station requires a matched pair of profiled rolls machined to match the incremental bend angle), but per-part cost drops rapidly once the line is set up and running.

**Roll design considerations**: Each station pair consists of a top roll and bottom roll with matching profile contours. The strip enters flat at station 1 and exits fully formed at the last station. Roll material is hardened tool steel (D2 or equivalent) for wear resistance on long production runs. Roller alignment is critical: lateral misalignment exceeding 0.1 mm per station accumulates through the line and produces a twisted profile at exit. Straightening rolls at the end of the line correct minor angular and curvature deviations in the finished section.

### Stamping Press Types

**[Mechanical press](../glossary/mechanical-press.html)** (crank or eccentric drive): A flywheel stores rotational energy, and a crank mechanism converts it to a linear ram stroke. Tonnage range: 10-2,000 tons. Stroke rate: 30-600 strokes per minute for progressive die work. The crank press delivers peak force at bottom dead center; the eccentric gear press provides a more uniform force curve through the stroke. Mechanical presses suit blanking, piercing, bending, and shallow drawing where cycle speed is more important than full-stroke force control.

**Hydraulic press**: Oil at 100-300 bar drives one or more pistons. Tonnage range: 20-10,000 tons. Full rated tonnage is available at any point in the stroke, not just at bottom dead center. Ram speed is adjustable from 0.5-50 mm/s. Slower cycle times than mechanical presses but superior for deep drawing and forming operations that require controlled force over a long distance. The hydraulic system provides inherent overload protection: a relief valve opens at a set pressure, preventing die damage from accidental overload.

**Die materials matched to production volume**:
- **[A2 tool steel](../glossary/a2-tool-steel.html)** (air-hardening, 5% chromium): Balanced toughness and wear resistance. Die life approximately 50,000 parts. Suitable for medium production runs where the cost of higher-grade tool steel is not justified. Air hardening minimizes distortion during heat treatment, simplifying post-hardening finishing.
- **[D2 tool steel](../glossary/d2-tool-steel.html)** (high-carbon, high-chromium: 1.5% C, 12% Cr): Hard chromium carbides provide excellent abrasive wear resistance. Hardened to 58-62 HRC after austenitizing at 1010-980°C and air quenching. Die life 100,000+ parts. The standard choice for most production stamping dies. Machining is difficult in the hardened state; all shaping is done before heat treatment, with only grinding and lapping after hardening.
- **Tungsten carbide inserts**: Used for high-wear die components (punch tips, die bushings). Hardness 85-92 HRA, far exceeding any steel. Die life 1,000,000+ parts. Carbide is brittle and requires steel backup plates to absorb shock. The high material cost and grinding-intensive fabrication justify carbide tooling only at production volumes above 500,000 parts.

### Deep Drawing

**Draw ratio**: The ratio of blank diameter to cup diameter must not exceed 2:1 in a single drawing stage. Attempting greater reduction in one pass causes tensile tearing at the punch nose radius. For cups deeper than a 2:1 ratio, use multiple redraw stages, each reducing diameter 20-35%, with annealing between stages to restore ductility lost from work hardening.

**Blank holder force**: Applied at 10-30% of the drawing force by a hydraulic cushion, pneumatic cushion, or die spring mechanism. The blank holder prevents wrinkling of the flange as it draws inward through the die opening. Too little force and circumferential compressive stress buckles the flange into wrinkles. Too much force and the material stretches thin and tears at the punch nose. Optimal force is found empirically for each material thickness and geometry combination.

**Drawing force estimate**: F = π × D × t × σ_y × (D/d − 0.7), where D = blank diameter, d = punch diameter, t = sheet thickness, σ_y = yield strength. Example: a 100 mm blank drawn to a 60 mm cup from 1 mm mild steel (σ_y = 250 MPa) requires F = π × 100 × 1 × 250 × (100/60 − 0.7) ≈ 78.5 kN (~8 tonnes).

**Punch and die clearance**: The gap between punch and die is set to 1.1-1.3× sheet thickness for mild steel drawing. Tighter clearance increases friction and tearing risk; wider clearance produces a thicker, less controlled cup wall with a pronounced die radius mark. The die entry radius (the rounded edge at the top of the die opening) is set to 4-10× sheet thickness: too small and the material tears at the radius, too large and the blank holder cannot control the flange.

**Redrawing for deeper cups**: A first draw at 2:1 ratio produces a shallow cup. A second draw reduces diameter another 20-35%. A three-stage redraw sequence achieves overall reduction ratios of 5:1 to 8:1. Anneal between draws when the accumulated work hardening raises yield strength beyond the draw tooling capacity. Reverse redrawing (flipping the cup inside-out in the second stage) produces smoother walls than same-direction redrawing because the bend direction reverses at the die lip.

**Ironing**: After initial drawing, the cup wall thickness can be reduced and uniformized by forcing the cup through a die slightly smaller than the cup outer diameter, with a tightly-fitted punch inside. Each ironing pass reduces wall thickness 15-30%. Beverage cans undergo 2-3 ironing passes to thin the walls to 0.1 mm from an initial draw thickness of 0.3 mm. Ironing requires good lubrication (chlorinated oil or phosphate coating) to prevent galling between the die and the cup wall.

### Metal Spinning

**Process**: A flat sheet metal disc is clamped against a shaped mandrel mounted on a lathe spindle. The mandrel rotates at 300-1,000 RPM. A rounded roller tool (hardened steel, mounted on a lever arm or hydraulically controlled) presses the spinning disc against the mandrel, progressively forming it to the mandrel profile through a series of sweeping passes from center to rim. The operator applies the roller in smooth, overlapping sweeps, starting near the center and working outward. Each pass moves more material into conformity with the mandrel.

**Suitable parts**: Axisymmetric shapes, meaning parts symmetric around a central axis: cones, cylinders, domes, hemispheres, parabolic reflectors, bell shapes, and nozzle contours. Spinning is economical for low-to-medium production volumes (10-1,000 pieces) where the tooling cost of matched stamping dies cannot be justified. The only tooling is the mandrel itself, which can be turned from hardwood for prototyping or machined from steel for production runs.

**Material range**: Manual spinning handles sheet thicknesses of 0.5-6 mm (softer metals like copper and aluminum toward the thicker end, steel toward the thinner). Power spinning with hydraulic assistance extends the range to 25 mm in steel. Wall thickness remains approximately constant in conventional spinning because the metal flows rather than stretches. In shear spinning, the roller deliberately thins the wall: t_final = t_initial × sin(α), where α is the cone half-angle. Shear spinning produces dimensionally precise, work-hardened parts with higher strength than the original sheet, at the cost of reduced ductility.

**Lubrication and finish**: Apply beeswax, tallow, or bar soap to the disc surface before spinning to reduce friction between the roller and workpiece. Without lubrication, galling produces surface tears and the required forming force increases sharply. Spun parts show helical tool marks from the roller passes; these can be removed by polishing or, for tighter tolerances, by a final skim cut on the lathe with the part still mounted on the mandrel.

### Extrusion

**Process**: A heated billet is forced through a die opening of the desired cross-section by a ram in a container. The metal flows under pressure through the die, emerging as a continuous profile. Aluminum extrudes at 350-500°C; steel requires 1100-1250°C and much higher pressures (800-1200 MPa). Extrusion produces complex cross-sections that would be difficult or impossible to roll: I-beams, T-sections, hollow tubes (using a mandrel inside the die), and custom structural shapes.

**Extrusion force**: F = A × σ × ln(A₀/A_f), where A = billet cross-section area, σ = flow stress at extrusion temperature, A₀ = billet area, A_f = die opening area. The extrusion ratio A₀/A_f typically ranges from 10:1 to 100:1. Higher ratios produce finer grain structure through more severe deformation but require greater force. For aluminum at 450°C with a 30:1 extrusion ratio, the flow stress is approximately 40-60 MPa, and a 150 mm diameter billet requires roughly 5-8 MN (500-800 ton) press capacity.

**Hot vs. cold extrusion**: Hot extrusion (aluminum above 350°C, steel above 1100°C) reduces required force and allows larger reductions but produces oxide scale on the surface and tighter dimensional tolerances of ±0.5-1.0 mm. Cold extrusion (room temperature or slightly warmed) produces parts with better surface finish (±0.1-0.3 mm tolerance) and work-hardened strength but is limited to softer metals (aluminum, copper, low-carbon steel) and lower extrusion ratios (5:1 to 20:1).

### Coining and Embossing

**Coining**: A closed-die striking operation that forces metal to flow into fine die details under pressures of 800-1,500 MPa. Both sides of the workpiece are confined by the dies, so metal cannot escape laterally. Used for coins, medals, and precision-flat parts. Die life is limited by the extreme pressures: steel dies last 100,000-500,000 impressions before detail degradation. The blank is typically struck at 1-5% of its thickness as pure compression, with no flash.

**Embossing**: A shallow relief pattern formed by matching male and female dies that thin the sheet locally without significant stretching. The material thickness changes little overall; the pattern is created by redistribution. Used for decorative panels, tread plate, and stiffening ribs on sheet metal enclosures. Embossing pressures are modest (50-200 MPa) compared to coining because the deformation is shallow.

### High-Energy Rate Forming

**Explosive forming**: Place a sheet metal blank over a die cavity and seal the edges. Submerge the assembly in water. Detonate an explosive charge at a calculated standoff distance. The shock wave traveling through the water forces the blank into the die cavity at velocities of 100-300 m/s. Used for large, one-of-a-kind parts (rocket domes, ship hull sections up to 10 m diameter) where conventional press capacity is insufficient. Die material can be concrete or epoxy for single parts, since the forming pressure is brief. The standoff distance and charge weight control forming pressure: a 1 kg TNT charge at 1 m standoff produces approximately 30 MPa peak pressure on the blank.

**Electromagnetic forming**: A capacitor bank discharges through a coil positioned near the workpiece. The transient magnetic field induces eddy currents in the conductive workpiece, and the resulting Lorentz force repels the metal away from the coil at velocities up to 300 m/s. Used for joining dissimilar metals (aluminum tube crimped onto steel fitting) without heat or contact. The process works only on electrically conductive materials: aluminum, copper, and steel respond well; titanium and high-resistivity alloys require higher energy. Peak current: 100-500 kA, discharged in 10-50 microseconds.

**Electrohydraulic forming**: Similar to explosive forming but uses an electric arc discharge between two submerged electrodes instead of chemical explosive. The arc vaporizes water, creating a shock wave that forms the blank into the die. Energy input is controlled by capacitor voltage (5-20 kV) and electrode gap (10-50 mm), offering better repeatability than explosive charges. Energy range: 10-200 kJ per discharge. Suitable for medium-sized parts (up to 1 m diameter) in a workshop environment where explosive storage is impractical. The discharge chamber must be robust (forged steel or thick-walled cast iron) to withstand repeated shock loading without fatigue cracking.

### Forming Process Selection Guide

The choice of forming method depends on production volume, part geometry, material, and available equipment. Forging produces the strongest parts with favorable grain flow. Rolling is fastest for uniform cross-sections in bar, rod, and sheet. Deep drawing suits cup-shaped parts in high volume. Spinning wins for low-volume axisymmetric shapes where die cost must be minimal. Extrusion creates complex profiles impossible by rolling. Stamping with progressive dies is the most productive method for flat or shallow-formed parts at volumes above 10,000 pieces, but demands the highest tooling investment.

### Rubber Pad Forming (Guerin Process)

**Process**: A thick rubber pad (150-250 mm, typically natural rubber or polyurethane of Shore A 60-80 hardness) sits in a steel container on the press bed. Sheet metal blank is placed over a single male die (form block). The press ram descends, pressing the rubber pad against the blank and form block. The rubber flows around the die, applying uniform hydrostatic pressure that forces the sheet into conformity with the die contour. Forming pressure: 7-14 MPa depending on material thickness and complexity.

**Advantages**: Only one die half needed (the male form block) — the rubber acts as a universal female die. Tooling cost is roughly 1/10 of matched press tooling because only one shaped die requires machining. Form blocks can be made from wood, plastic, or cast metal for prototyping. Quick changeover between parts — swap the form block, keep the rubber pad.

**Limitations**: Minimum bend radius approximately 3× sheet thickness (rubber cannot concentrate force sharply enough for tight bends). Suitable for aluminum and soft steel up to ~2 mm thickness. Not practical for high-strength alloys or thick plate. Dimensional tolerance ±0.5-1.0 mm — adequate for aircraft skins, bezels, and ductwork but not precision parts.

**Typical applications**: Low-volume production of complex shallow shapes: aircraft panel segments, lighting reflectors, decorative architectural metal, prototype enclosures. Production quantity range: 10-1,000 pieces where dedicated tooling cannot be justified.

### Cross-References

- [Iron & Steel](../metals/iron-steel.md) — bloom smelting, carburization, heat treatment
- [Iterative Bootstrap](./iterative-bootstrap.md) — building the rolling mill and draw bench from castings
- [Bearings & Abrasives](./bearings-abrasives.md) — grinding and finishing formed parts
- [Electricity](../energy/electricity.md) — drawn copper wire for generators and motors

---

*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*
