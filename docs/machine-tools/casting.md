# Metal Casting

> **Node ID**: machine-tools.casting
> **Domain**: Machine Tools Bootstrap
> **Timeline**: Years 10-15
> **Outputs**: cast_iron_parts, cast_aluminum_parts, sand_molds, cast_bronze_parts

## Overview

The foundry is step zero of the machine tool bootstrap. Every machine tool starts as a sand-cast iron or aluminum casting — machine beds, column frames, bearing housings, gear blanks, pulleys, and slideway bases all begin as molten metal poured into shaped cavities in sand. Casting is the only practical method for producing complex three-dimensional metal parts before machining capability exists. Without casting, there are no machine tools; without machine tools, there is no precision industry.

This document covers the full range of casting methods available in the bootstrap sequence, from basic green sand casting (the workhorse) through investment casting (for precision parts), with quality control and defect analysis essential for producing usable castings reliably.

## Crucible Furnace for Aluminum

Aluminum is the easiest structural metal to cast — low melting point (660°C), fluid when molten, forgiving of minor impurities.

- **Crucible**: Steel pipe with welded bottom plate, or fired clay-graphite crucible. 5-15 kg capacity for startup. Larger crucibles (25-50 kg) for production work.
- **Fuel**: Charcoal + forced air (electric blower or hand-cranked fan). Temperature needed: ~660°C (aluminum melts at 660°C, need ~750°C for fluidity). Any charcoal-burning furnace that can reach dull red heat can melt aluminum.
- **Melting time**: 20-40 minutes for 5 kg charge. Skim dross (aluminum oxide skin) before pouring — dross inclusions are the most common defect in aluminum castings.
- **Aluminum sourcing**: Scrap aluminum (post-collapse salvage — beverage cans, window frames, engine parts), or primary aluminum from bauxite smelting (Hall-Héroult process — much harder, requires substantial electrical energy and chemistry infrastructure). For bootstrap purposes, scrap or salvage is assumed available.
- **Degassing**: Dissolved hydrogen causes porosity in aluminum castings. Degassing methods: bubble dry nitrogen or chlorine gas through the melt (removes H₂ as it diffuses into bubbles); or let the melt stand at temperature for 10-15 minutes (hydrogen diffuses out slowly). Simple test: pour a small test bar, break it — if the fracture surface shows bright, rounded pores, the melt is gassy and needs degassing.

## Crucible Furnace for Cast Iron

Cast iron (machine beds, gear blanks, flywheels, and heavy structural parts) requires significantly higher temperatures:

- **Temperature needed**: ~1200-1400°C (cast iron melts ~1150-1250°C depending on carbon content). Requires significant forced air and good insulation.
- **Charge**: Pig iron, scrap iron, or iron bloom + 2-4% carbon (coke/charcoal). Add limestone flux (CaCO₃) to form slag from impurities.
- **Crucible**: Clay-graphite (withstands higher temps, available from ceramics production). Silicon carbide crucible if available (longer life, higher temperature capability). Steel crucibles are NOT suitable for cast iron — steel melts at 1370-1510°C, dangerously close to the pouring temperature.
- **Furnace design**: Cupola furnace (vertical shaft furnace, similar to a small blast furnace) for continuous cast iron production. Or reverberatory furnace for batch melting. The cupola is more fuel-efficient for sustained production; the reverberatory is simpler for batch work.
- **Pouring**: Preheat molds to 200-400°C (prevents premature freezing and reduces thermal shock). Pour steadily, keep sprue full to prevent shrinkage defects. Pouring temperature: 1300-1400°C for gray cast iron, 1350-1450°C for ductile iron.

## Cupola Furnace (Continuous Cast Iron Melting)

The standard furnace for cast iron melting in the bootstrap sequence. A small, simple, and efficient vertical shaft furnace:

- **Construction**: Cylindrical steel shell (5-10 mm plate), lined with fireclay refractory brick. Internal diameter 30-60 cm, height 2-4 m. Open top for charging, tap hole at bottom for molten iron, separate slag notch slightly above iron tap. Wind box with tuyeres (air nozzles, 2-4 openings at 20-30 cm above the bottom) connected to blower.
- **Charging**: Alternate layers of coke (fuel), iron (pig iron, scrap, or bloom), and limestone (flux). Charge ratios by weight: 1 part coke to 8-10 parts iron, 0.3-0.5 parts limestone. Load from top.
- **Operation**: Ignite bed of coke at tuyere level. Turn on blower (forced air at 5-15 kPa). As coke burns, it melts the iron above. Molten iron and slag drip down through the coke bed. Iron collects in the well (bottom). Slag (lighter) floats on the iron and overflows through the slag notch. Tap iron every 10-20 minutes through the tap hole (clay plug is opened, iron flows into ladle, plug is re-sealed).
- **Capacity**: A 40 cm bore cupola melts 500-1500 kg/hour of iron. Temperature: 1350-1500°C. Continuous operation for 4-12 hours per campaign.
- **Advantages**: Continuous melting (not batch). High throughput. Simple construction. Self-fluxing (slag separates naturally).

## Bronze and Copper Casting

- **Bronze** (copper-tin alloy, typically 88-92% Cu, 8-12% Sn): Melts at ~950°C. Easier to cast than iron — lower temperature, more fluid, less shrinkage. Ideal for bearings, bushings, gears, decorative hardware, and marine fittings. Very low shrinkage (~1%) reduces casting defects.
- **Brass** (copper-zinc alloy, typically 60-70% Cu, 30-40% Zn): Melts at ~900-940°C. Zinc boils at 907°C — generates zinc vapor (toxic, causes "brass founder's ague"). Requires forced ventilation. Used for valves, fittings, decorative hardware.
- **Copper**: Melts at 1085°C. Used for electrical components, heat exchangers, and roofing. More difficult to cast than bronze (higher melting point, more reactive with oxygen — forms Cu₂O inclusions). Use charcoal cover on melt to prevent oxidation.

## Sand Molding (Green Sand)

Green sand casting is the workhorse method — "green" means the sand is moist (not dried), held together by clay binder. Accounts for >90% of all castings by weight.

### Sand Preparation

- **Sand**: Fine silica sand (60-120 mesh, 90-95% SiO₂). River sand works if clean and fine. Avoid sand with organic matter, clay lumps, or excessive fines.
- **Binder**: Bentonite clay (8-12% by weight). Western bentonite (sodium) provides high green strength; southern bentonite (calcium) provides better flowability. If not available naturally, use any clay that provides adequate bond strength.
- **Water**: 3-6% by weight. Too much = steam explosions, gas porosity, and soft molds. Too little = sand crumbles, won't hold shape.
- **Additives**: Coal dust (2-5%, "sea coal") improves surface finish by generating a reducing atmosphere at the mold-metal interface. Cereal binder (1-2%, wheat flour) improves green strength for deep pockets.
- **Mixing**: Mull (knead) sand thoroughly — a muller is a heavy wheel that grinds clay onto each sand grain, coating them uniformly. Can be done by foot-treading for small batches. Mechanical muller for production.
- **Test**: Squeeze sand in hand — should form a coherent cylinder that doesn't crumble when handled, but breaks cleanly when snapped. Breathe on the surface — it should hold the impression of your breath (moisture present but not wet).

### Pattern Making

The pattern is the master shape that creates the cavity in the sand. Pattern quality directly determines casting quality.

- **Material**: Wood (pine or mahogany, sealed with shellac or varnish to prevent moisture absorption). Metal patterns (aluminum or cast iron) for high-volume production — more durable, more accurate.
- **Shrinkage allowance**: Make pattern 1-2% oversize. Cast iron shrinks ~1%, aluminum ~1.3%, bronze ~1.5%. The pattern must be larger than the finished part by this amount.
- **Draft angles**: 1-3° taper on all vertical surfaces so the pattern releases from sand without tearing the mold cavity. Without draft, the pattern binds and destroys the mold on extraction.
- **Fillets**: Round all internal corners (2-5 mm radius). Sharp corners cause stress concentrations in the casting and promote shrinkage cracking. Use leather or wax fillets pressed into the pattern.
- **Core prints**: If the part has internal passages (hollow sections), include locating surfaces (core prints) on the pattern where the sand core will be supported.
- **Parting line**: Design pattern so it splits at the mold parting line (cope/drag boundary). One-piece patterns work for simple shapes; split patterns (two halves joined by dowel pins) for complex shapes.

### Mold Making Process

1. **Place pattern** on the drag (bottom flask half) with the parting face down.
2. **Ram sand** around pattern — firm but not rock-hard. Use peen end of rammer near pattern (concentrates force), flat end elsewhere (uniform compaction). Add sand in layers, ram each layer.
3. **Strike off** excess sand level with the top of the flask.
4. **Flip drag** over. The pattern face is now facing up.
5. **Apply parting compound** (dry silica flour or talc) to prevent cope sand from sticking to drag sand.
6. **Place cope** (top flask half) on the drag. Align with locating pins.
7. **Set sprue pin** (vertical round stick, 20-30 mm diameter) where you want the pouring hole. Set riser pins (slightly smaller) at the highest points of the casting to feed shrinkage.
8. **Ram sand** in cope around pattern, sprue, and risers.
9. **Remove sprue and riser pins**. Cut a pouring basin (funnel shape) at the top of the sprue.
10. **Separate flask halves** (lift cope off drag carefully).
11. **Remove pattern**: Rap (tap gently) to loosen, then lift straight up with draw screws or lifting hooks. Do not tilt or drag — it tears the mold cavity.
12. **Cut gates**: Carve channels in the drag connecting the sprue base to the mold cavity. Gate should enter the cavity at the thickest section. Gate cross-section should be smaller than the sprue to ensure the gate freezes first (prevents back-feeding of shrinkage).
13. **Place cores** (if any) in the mold cavity, supported by core prints.
14. **Close mold**: Place cope back on drag. Weight down or clamp — the buoyant force of molten metal on a large core can lift the cope off (a "floating" or "runout" disaster).
15. **Pour**.

### Gating System Design

The gating system (sprue, runners, gates, and risers) controls how molten metal flows into the mold cavity. Poor gating causes most casting defects:

- **Sprue**: Vertical channel from pouring basin to runner. Tapered (wider at top, narrower at bottom) to prevent air aspiration — a straight sprue draws in air as the metal stream accelerates downward.
- **Runner**: Horizontal channel at the parting line distributing metal from sprue to gates. Should be in the drag (bottom) so metal fills from the bottom up.
- **Gates**: Connections from runner to mold cavity. Should enter at thick sections of the casting. Multiple gates for large or thin-walled castings to fill uniformly.
- **Risers** (feeders): Vertical reservoirs of molten metal connected to the casting at the top. As the casting solidifies and shrinks, the riser supplies liquid metal to compensate. Risers must be larger than the casting section they feed (so they freeze last). Top risers are most common; side risers for horizontal sections.
- **Chills**: Metal inserts (cast iron or copper) placed in the mold at thick sections to accelerate local solidification. Direct solidification toward the riser. Prevents shrinkage porosity in heavy sections.

## Investment Casting (Lost-Wax)

For parts requiring finer detail and smoother surfaces than green sand can provide. Investment casting produces near-net-shape parts with minimal machining — critical for complex geometries like turbine blades, valve bodies, and instrument components.

### Wax Pattern Making

- **Injection dies**: Carve or machine aluminum dies. Inject molten wax (paraffin-microcrystalline blend, melts at 60-80°C) at 0.1-0.3 MPa. For simple shapes, hand-carve patterns directly from wax blocks.
- **Pattern assembly (tree construction)**: Attach individual patterns to a central wax sprue using a heated spatula. Typical tree: 5-50 patterns depending on part size. Gate connections must be ~3-6 mm thick to feed metal without freezing off.
- **Runner/gate design**: Bottom-gating minimizes turbulence. Gates should enter the thickest casting section. Total gate cross-sectional area ≥ sprue area to ensure complete fill.

### Ceramic Shell Building

1. **Prime coat**: Dip pattern tree in fine slurry (colloidal silica binder + zircon flour, 200-325 mesh). Drain excess, stucco with fine zircon sand (80-120 mesh). Dry 2-4 hours at 40-60% relative humidity.
2. **Backup coats**: 3-5 additional coats with coarser slurry (colloidal silica + molochite flour). Stucco with progressively coarser grain (30-80 mesh). Each coat dries 2-4 hours. Total shell: 6-12 mm thick (5-7 coats).
3. **Dewaxing**: Heat shell to 100-200°C in oven or autoclave. Wax melts and drains through sprue opening. Collect and reuse wax. Flash-fire alternative: heat rapidly to 800-900°C (wax burns out, produces smoke — requires ventilation).
4. **Burnout**: Heat to 800-1000°C, hold 1-2 hours. Removes all residual wax and organics, sinters ceramic shell to full strength.
5. **Pouring**: While shell is still hot (600-900°C), pour molten metal. Preheated shell prevents premature freezing and thermal shock cracking. Pour steadily, keep sprue full.
6. **Shell removal and finishing**: Once cooled, break ceramic shell with hammer or vibratory knock-off. Cut parts from tree with abrasive wheel. Grind gate stubs flush. Sandblast or machine critical surfaces as needed.

### Applications

- **Turbine blades**: Complex internal cooling passages produced by a ceramic core inside the investment shell
- **Valve bodies**: Smooth internal passages, no parting line flash
- **Instrument components**: Fine detail, thin walls, excellent surface finish
- **Jewelry and dental**: Precious metals, high detail
- **Small batch production**: Where pattern cost is justified by reduced machining

## Casting Alloys Reference

| Alloy | Melting Range | Shrinkage | Fluidity | Primary Use |
|-------|-------------|-----------|----------|-------------|
| Gray cast iron (3-4% C) | 1150-1250°C | ~1% | Excellent | Machine beds, frames, flywheels |
| Ductile iron | 1120-1200°C | ~1.2% | Good | Gear blanks, crankshafts |
| Aluminum (pure) | 660°C | ~1.3% | Fair | Lightweight housings, covers |
| Al-Si alloy (A356) | 555-615°C | ~1.1% | Excellent | Complex thin-wall castings |
| Bronze (88/12 Cu/Sn) | ~850-950°C | ~1.5% | Very good | Bearings, gears, marine fittings |
| Brass (70/30 Cu/Zn) | 900-940°C | ~1.3% | Very good | Valves, fittings, decorative |
| Copper (pure) | 1085°C | ~2% | Poor | Electrical, heat exchange |

## Quality Control and Defect Analysis

Casting defects are the primary yield loss in foundry work. Identifying and correcting them is essential — a foundry that cannot consistently produce sound castings cannot support machine tool production.

### Common Defects

- **Gas porosity**: Round, scattered bubbles from dissolved gas (hydrogen in aluminum, nitrogen in iron) or moisture in sand/mold. Fix: degas aluminum melts with chlorine or nitrogen purge, dry molds thoroughly, control sand moisture to 3-6%. Gas porosity appears as bright, rounded pits on fracture surfaces.
- **Shrinkage porosity**: Irregular angular voids in thick sections where metal contracts without adequate feed metal. Fix: increase riser volume, use chills (metal inserts) to direct solidification toward risers, ensure continuous feed path from riser to thick section.
- **Cold shuts and misruns**: Metal freezes before mold fills completely. Cold shut = visible seam where two metal streams meet without fusing. Misrun = missing sections. Fix: increase pouring temperature 20-50°C, widen gates, reduce pour distance, preheat molds.
- **Inclusions**: Sand grains, slag, or dross trapped in the casting body. Fix: skim dross before pouring, use ceramic foam filters in gating system, control sand compaction to prevent mold erosion, use a slag trap in the runner (a well before the gate that catches heavy slag).
- **Cracking**: Hot tears during solidification (differential shrinkage against rigid mold) or cold cracks from residual stress after cooling. Fix: increase fillet radii at corners, design uniform wall thickness, improve mold collapsibility (sand should yield as casting shrinks).
- **Sand adherence**: Metal penetrates into sand pores, producing a rough, sandy surface. Fix: use finer sand, apply mold wash (zircon flour slurry) to mold cavity surfaces, increase sand compaction.
- **Blowholes**: Large gas cavities from mold reactions (moisture, binders, core gases). Fix: increase sand permeability (coarser sand), vent the mold (poke vent holes through cope sand to atmosphere), use clean, dry sand.

### Inspection Methods

- **Visual**: Check every casting for surface defects (cracks, sand inclusions, cold shuts, short pours). First line of defense.
- **Dimensional**: Verify critical dimensions against pattern with calipers, gauges, and straight edges. Check for warpage and twist.
- **Sound test**: Suspend casting on a wire, tap with a hammer. A clear ring indicates a sound casting. A dull thud indicates internal cracks or large porosity.
- **Fracture test**: Break a test bar from the same pour. Examine fracture surface for grain structure, gas porosity, and inclusions.
- **X-ray radiography**: For critical castings (machine tool beds, pressure-containing parts) — requires [Electricity](../energy/electricity.md) infrastructure. Reveals internal porosity, inclusions, and cracks non-destructively.
- **Pressure test**: For castings intended to hold fluid (valve bodies, cylinder blocks). Pressurize with water at 1.5× working pressure and check for leaks.

## Finishing Operations

- **Shakeout**: Break the sand mold away from the casting. Manual for small castings; vibratory or rotary shakeout for production. Reclaim sand for reuse (screen to remove lumps, re-mull with water and clay).
- **Gate and riser removal**: Cut off with abrasive wheel, bandsaw, or pneumatic chisel. Grind stubs flush with surrounding surface.
- **Cleaning**: Shot blasting or sandblasting removes residual sand and oxide scale. Wire brushing for smaller parts. Pickling (acid dip) for clean surfaces.
- **Heat treatment**: Some castings require heat treatment after casting. Gray iron is typically used as-cast. Ductile iron may be annealed (heat to 900°C, slow cool) to improve machinability. Aluminum alloys are often solution-treated and aged for improved strength.
- **Machining**: Cast surfaces are not dimensionally accurate enough for precision fits. Machine mating surfaces (bearing bores, slideway faces, flange faces) to final tolerance. See [Machining](./machining.md).

## Safety

Foundry work involves the highest temperatures in the machine shop. Safety discipline is non-negotiable.

- **Molten metal hazards**: Cast iron at 1300-1400°C and steel at 1500-1600°C cause catastrophic burns on contact. Metal flows like water and adheres to skin. Aluminum at 700-750°C is less dramatic but equally dangerous — it can wet and stick to clothing, causing deep burns that are difficult to remove.
- **Protective equipment**: Full face shield (not just safety glasses — splashes go over glasses), leather foundry apron, heat-resistant gloves, steel-toed foundry boots with metatarsal guards, long sleeves with no exposed skin. Preheat and inspect all tools (ladles, skimmers, tongs) that will contact molten metal — cold or damp tools cause violent splatter.
- **Ventilation**: Metal fumes (zinc oxide from brass — causes "metal fume fever," manganese from steel — neurological damage, aluminum oxide) require forced ventilation or outdoor work. Charcoal furnaces produce carbon monoxide. Work outdoors or with forced ventilation. P100 respirator for enclosed foundries.
- **Moisture explosions**: The most lethal foundry hazard. Any moisture — damp sand, wet molds, condensation on tools, sweat on the floor — in contact with molten metal produces a steam explosion that launches metal in all directions. 1 gram of water → 1.7 liters of steam at 100°C, expanding to 3000+ liters at iron temperatures. Preheat molds to 200-400°C before pouring. Preheat ladles and crucibles. NEVER pour on concrete — use dry sand bed or metal drip tray.
- **Fire risk**: Foundry work involves open flames, molten metal, and combustible materials. Keep fire extinguishing equipment (dry sand, Class D extinguisher for metal fires) immediately accessible. No water on metal fires — water causes steam explosions.

## Cross-References

- [Iron & Steel](../metals/iron-steel.md) — bloom smelting, crucible steel, heat treatment of cast parts
- [Forming](./forming.md) — forging, rolling, and wire drawing of cast ingots
- [Iterative Bootstrap](./iterative-bootstrap.md) — building machine tools from castings
- [Bearings & Abrasives](./bearings-abrasives.md) — cutting tools and finishing operations for cast parts
- [Ceramics](../ceramics/) — crucibles, refractory linings, and kiln furniture for foundry use

## Shell Molding

Shell molding produces castings with superior surface finish and tighter dimensional tolerances than green sand, using resin-coated sand that forms a thin, rigid shell around a heated metal pattern.

- **Sand preparation**: Coat fine silica sand (AFS 90-140) with thermosetting phenolic resin (2-4% by weight) and hexamine catalyst (10-15% of resin weight). The resin-coated sand is free-flowing and dry at room temperature.
- **Shell building**: Heat the metal pattern (cast iron or steel) to 200-260°C. Invert the pattern box over a dump box filled with resin-coated sand. Flip the assembly so sand covers the hot pattern for 15-30 seconds. The resin cures on contact, forming a shell 5-15 mm thick on the pattern surface. Return the dump box to upright position — uncured sand falls away, leaving only the cured shell on the pattern. Cure the shell for an additional 30-90 seconds on the heated pattern to develop full strength.
- **Shell removal and assembly**: Eject the completed shell half from the pattern (the resin's shrinkage on curing provides natural draft). Glue two shell halves together with thermosetting adhesive or mechanical clips. Back the assembled shell mold with steel shot or gravel in a flask for support during pouring.
- **Advantages**: Dimensional accuracy ±0.15 mm (vs. ±0.5-1.0 mm for green sand). Surface finish 3-6 μm Ra (vs. 12-25 μm for green sand). Smooth shell cavity produces excellent detail reproduction. Shell sand is reclaimable by mechanical reclamation (grinding to break resin bonds, re-coating with fresh resin).
- **Limitations**: Requires metal patterns (expensive, but durable for 50,000+ cycles). Phenolic resin requires petrochemical or coal-tar feedstock. Shell thickness limits casting weight — practical for parts under 20 kg. Best suited for medium-volume production of precision castings: small gears, valve bodies, compressor housings, and lever arms.

---

*Part of the [Bootciv Tech Tree](../) • [Machine Tools](./) • [All Domains](../)*
