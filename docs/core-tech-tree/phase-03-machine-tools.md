# Phase 3: Machine Tools Bootstrap ★ CRITICAL

**Timeline**: Years 10–25
**Goal**: Precision manufacturing capability — the single most important parallel track.
**Dependencies**: [Phase 2](phase-02-metallurgy.md) (metals, casting, hand tools)

> **This phase is the master enabler.** Without precision machine tools, you cannot build the equipment for silicon processing, crystal pullers, vacuum pumps, lithography stages, or any semiconductor fabrication equipment. Everything from Phase 4 onward depends on this capability.

## Philosophy: Gingery-Style Iterative Bootstrap

The approach follows Dave Gingery's proven method: build a crude foundry, cast a lathe, use the lathe to build better machines, and iterate. Each generation of machines produces parts for the next.

```
Hand tools → Foundry → Crude Lathe → Better Lathe → Shaper → Mill → Full Shop
```

## Key Technologies

### Charcoal Foundry (Scale-up from Phase 2)

The foundry is step zero. Every machine tool starts as a sand-cast iron or aluminum casting.

**Crucible furnace for aluminum**:
- **Crucible**: Steel pipe with welded bottom, or fired clay-graphite crucible. 5-15 kg capacity for startup.
- **Fuel**: Charcoal + forced air (electric blower or hand-cranked fan). Temperature needed: ~660°C (aluminum melts at 660°C, need ~750°C for fluidity).
- **Melting time**: 20-40 minutes for 5 kg charge. Skim dross (aluminum oxide skin) before pouring.
- **Aluminum sourcing**: Scrap aluminum (post-collapse salvage), or bauxite smelting (Phase 5, Hall-Héroult — much harder). For bootstrap purposes, scrap or salvage is assumed available.

**Crucible furnace for cast iron** (for machine beds and heavy parts):
- **Temperature needed**: ~1200-1400°C (cast iron melts ~1150-1250°C depending on carbon content). Requires significant forced air and good insulation.
- **Charge**: Pig iron, scrap iron, or iron bloom + 2-4% carbon (coke/charcoal). Add limestone flux (CaCO₃) to form slag.
- **Crucible**: Clay-graphite (withstands higher temps). Silicon carbide crucible if available.
- **Pouring**: Preheat molds to 200-400°C. Pour steadily, keep sprue full to prevent shrinkage defects.

**Sand molding (green sand)**:
- **Sand**: Fine silica sand (60-120 mesh, 90-95% SiO₂). River sand works if clean and fine.
- **Binder**: Bentonite clay (8-12% by weight). If not available naturally, use any clay that provides bond strength.
- **Water**: 3-6% by weight. Too much = steam explosions, gas porosity. Too little = sand crumbles, won't hold shape.
- **Mixing**: Mull (knead) sand thoroughly — muller is a heavy wheel that grinds clay onto sand grains. Can be done by foot-treading for small batches. Test: squeeze sand in hand — should form a coherent cylinder that doesn't crumble, but breaks cleanly when snapped.
- **Mold boxes (flasks)**: Two-part wooden frames (cope = top, drag = bottom). Sizes: 20×20 cm to 60×60 cm for startup work.
- **Pattern making**: Carve wooden patterns ~1-2% oversize (shrinkage allowance — cast iron shrinks ~1%, aluminum ~1.3%). Add draft angles (1-3°) on vertical surfaces so pattern releases from sand. Include cores for internal passages (sand shapes held in place during pour).
- **Molding process**: Place pattern in drag, ram sand around it (firm but not rock-hard — use peen end of rammer near pattern, flat end elsewhere). Flip drag, place cope on top, ram sand. Cut sprue (pouring channel) and risers (vent/feeding channels). Separate flasks, remove pattern carefully, close mold, pour.

### The First Lathe (Gingery Lathe)

The first lathe is built from castings and hand-scraped flat surfaces. It doesn't need to be precise — it needs to exist.

**Bed**: Cast iron (or aluminum for very first version, though it flexes more). Length 60-90 cm, cross-section I-beam or box. Cast in sand mold, hand-scrape the top surfaces flat using:
- **Surface plate** (first reference flat): Three plates, scraped alternately against each other (Whitworth's three-plate method). Start with a known-flat granite surface plate if available, or generate flats from scratch:
  1. Scrape plate A against plate B until they show even bearing (red marking compound shows contact points).
  2. Scrape plate C against A.
  3. Scrape B against C.
  4. Repeat. After 3-5 iterations, all three converge to truly flat.
- **Scraping technique**: Use hand scraper (hardened steel blade, 15-25° cutting edge). Remove high spots identified by marking compound. Target: 20-30 contact points per 25×25 mm area. A skilled scraper covers ~0.5 m²/hour.

**Headstock**: Cast iron housing containing spindle. Spindle turned between centers on the lathe itself (bootstrap!). Or use a pre-made steel shaft, carefully aligned.
- **Spindle bearing**: Initially plain bronze bushings (cast from Phase 2 copper + tin). Bore to fit spindle using adjustable reamer.
- **Bearing clearance**: 0.02-0.05 mm for smooth rotation without excessive play.

**Tailstock**: Cast iron body with sliding barrel (MT2 or MT3 taper for center/drill chuck). Locks to bed via clamp plate. Align tailstock center with headstock center by turning a test bar between centers — if diameter varies, adjust tailstock laterally.

**Carriage/Toolpost**: Initially a simple sliding rest (hand-fed). Leadscrew arrives later.
- **Tool post**: Clamp-type holds square high-speed steel or carbon steel tool bits.
- **Cross slide**: Screw-driven, perpendicular to spindle axis. Enables facing cuts and diameter control.

**Power source**: Foot treadle (bicycle-style mechanism via crank and flywheel) or water wheel via belt drive. Minimum 0.25 HP for useful work.

### Iterative Self-Bootstrap Sequence

This is the heart of Phase 3. Each machine enables the next:

**Step 1: Crude lathe** (tolerance ~0.5 mm)
- Capable of: turning shafts, boring holes, facing flanges
- Use it to make: better bearings, true-running pulleys, leadscrew nuts

**Step 2: Improved lathe with leadscrew** (tolerance ~0.1 mm)
- **Leadscrew**: First leadscrew is hand-cut (file or chisel into round bar, using thread gauge for checking). Not precise, but functional.
- **Half-nut mechanism**: Split nut that engages/disengages leadscrew for threading.
- **Thread cutting**: Mount change gears between spindle and leadscrew. Gear ratio determines thread pitch. Start with standard metric or imperial pitches.
- Use it to make: leadscrew for shaper, accurate threaded fasteners, taps and dies

**Step 3: Shaper** (tolerance ~0.05 mm)
- **Function**: Single-point cutting tool reciprocates horizontally while work feeds laterally. Produces flat surfaces, keyways, slots, dovetails.
- **Construction**: Cast iron body, ram driven by slotted crank (adjustable stroke length), automatic table feed (ratchet and pawl).
- **Key operation**: Machining the flat ways for the mill, planing mating surfaces for machine slides.
- **Cutting speed**: 10-30 m/min for cast iron with HSS tool. Stroke rate 20-60 per minute.

**Step 4: Milling machine** (tolerance ~0.025 mm)
- **Function**: Rotating multi-tooth cutter removes material. More versatile than shaper — handles pockets, profiles, helical surfaces (gears).
- **Spindle**: Driven by belt or gear from motor/line shaft. Speed 50-2000 RPM (adjustable via pulley changes).
- **Table**: X-Y movement via leadscrews with graduated dials (0.025 mm divisions = "one thou").
- **Use it to make**: gear blanks, slots, flat reference surfaces, precision holes via boring head.

**Step 5: Drill press** (tolerance ~0.1 mm for hole location)
- **Spindle**: Vertical, driven by belt. Morse taper (MT2) for drill chucks.
- **Table**: Adjustable height. Angle plate for angled holes.
- **Speed range**: 200-3000 RPM via step pulleys.
- **Critical for**: Every subsequent machine and mechanism needs holes.

**Step 6: Surface grinder** (tolerance ~0.005 mm, surface finish ~0.4 μm Ra)
- **Requires**: Abrasive wheel (aluminum oxide or silicon carbide — Phase 4 electric arc furnace needed for synthetic abrasives, or use natural emery/quartz wheels for cruder work).
- **Function**: Spinning abrasive wheel removes microscopic amounts of material. Produces optically flat surfaces.
- **Essential for**: Gauge blocks, machine ways, precision sealing surfaces (vacuum flanges, cylinder bores).

### Precision Metrology

This is NOT optional — you cannot build what you cannot measure.

**Surface plates** (master reference flat):
- Cast iron (heavily ribbed underside to prevent warpage), aged 6+ months to relieve casting stresses before finishing. Hand-scraped to flatness ~0.005 mm over 300 mm length.
- OR granite (naturally stable, doesn't rust). Needs diamond abrasive to flatten — harder to produce from scratch but superior once made.

**Straight edges** (reference for checking flatness):
- Cast iron, 300-1000 mm long, I-beam cross-section. Scraped flat against surface plate.
- Test by placing on workpiece, checking light gap (0.01 mm gap visible as light line against dark background), or using marking compound.

**Squares** (reference for checking perpendicularity):
- Cast iron or steel. Blade and beam. Check by: place square against straight edge on surface plate, flip 180°, check if gap appears. If gap doubles, square is out by half the gap.

**Calipers and dividers**:
- **Outside calipers**: Bow-shaped steel, adjustable via knurled nut. Transfer dimensions from workpiece to rule.
- **Inside calipers**: Reverse bow for measuring bores.
- **Vernier calipers**: Steel rule with sliding jaw and vernier scale (reads to 0.02 mm). Requires engraved graduations — use dividing head on mill.
- **Dividers**: Two-legged steel tool for scribing circles and transferring distances.

**Micrometers** (iterative improvement):
- **Principle**: Threaded spindle advances 0.5 mm per revolution. Thimble divided into 50 divisions = 0.01 mm resolution.
- **First micrometer**: Make screw thread as accurately as possible on lathe. Lap the thread (run nut back and forth with grinding compound) to smooth errors. Calibrate against gauge blocks.
- **Frame**: Steel or cast iron C-frame, rigid enough that 1 kg hand pressure doesn't deflect more than 0.001 mm.
- **Accuracy**: First attempts ~0.05 mm. Iterate to ~0.01 mm. Production micrometers: 0.005 mm.

**Gauge blocks (Jo-blocks)**:
- **Material**: Hardened and ground tool steel (or tungsten carbide for ultimate stability).
- **Manufacturing**: Surface grind to rough size, then lap (rub against flat cast iron lap with fine abrasive paste) to final dimension. Requires temperature-controlled room (20°C ±0.5°C).
- **Accuracy grades**: Workshop grade ±0.5 μm, inspection grade ±0.2 μm, master grade ±0.1 μm.
- **Wringing**: Gauge blocks adhere when slid together (molecular attraction of ultra-flat surfaces). Stack to create any dimension.

**Thread standards and gauges**:
- **Go/No-Go gauges**: Two-end gauge — "Go" end fits into proper thread (minimum material), "No-Go" end does not (maximum material). Verifies thread is within tolerance.
- **Thread pitch gauge**: Set of toothed blades matching standard pitches. Identify unknown threads by matching.

### Abrasives & Grinding Media

**Natural abrasives (available immediately)**:
- **Emery**: Natural aluminum oxide (50-80% Al₂O₃) + iron oxide. Found in Greece, Turkey. Grit grades: coarse (24-60), medium (80-120), fine (150-240). For grinding and polishing.
- **Pumice**: Volcanic glass, porous. Fine polishing.
- **Sandstone**: Natural grinding wheels. Dress to shape with iron dresser.
- **Quartz sand**: Ground to powder, sieved. Lapping and grinding compound.
- **Jeweler's rouge** (iron oxide, Fe₂O₃): Fine polishing compound. Heat steel wool or iron filings in open air until red-hot. Grind resulting oxide to fine powder.
- **Tripoli**: Silica-based polishing compound. Fine finish on soft metals.

**Grit grading**: Sieve abrasive through woven wire screens. Screen mesh number = grit number (60 mesh = 60 grit, particles ~250 μm). Stack sieves coarse to fine, shake, weigh fractions.

**Synthetic abrasives (require Phase 4 electric arc furnace)**:
- **Silicon carbide (SiC)** — Acheson process: Silica sand + petroleum coke, heat in electric furnace to 2200-2500°C for 36-48 hours. SiO₂ + 3C → SiC + 2CO. Green to black crystalline mass. Crush, grade. Harder than aluminum oxide, sharp fracture.
- **Aluminum oxide (Al₂O₃)** — Bauxite fused in electric arc furnace at 2000-2200°C. Cool, crush, grade. Tougher than SiC, better for steel grinding.

**Lapping**: Mix graded abrasive (600-1200 grit, ~5-25 μm) with oil or water into slurry. Place slurry between two flat surfaces, rub in figure-8 pattern. Removes ~0.001-0.01 mm per hour. Produces optically flat surfaces. Essential for gauge blocks, valve seats, bearing surfaces.

### Thread Standards &amp; Fastener Production

**Thread profile standard** (choose ONE system and standardize immediately):
- **Metric (ISO)**: 60° thread angle, flat crests and roots. Designated M×pitch (e.g., M8×1.25 = 8 mm major diameter, 1.25 mm pitch). Coarse pitch series is default (M8 coarse = 1.25 mm pitch).
- **Unified (UNC/UNF)**: 60° thread angle, flat crests, rounded roots. Designated by diameter + TPI (e.g., 5/16-18 UNC = 5/16" diameter, 18 threads per inch, coarse series).
- **CRITICAL**: Pick metric OR unified and commit. Mixing thread standards is a disaster for interchangeable parts. All taps, dies, gauges, and screws must match.

**Thread cutting on lathe**:
- **Setup**: Mount workpiece in chuck. Install correct change gears between spindle and leadscrew for desired pitch. Gear ratio = (pitch to cut / leadscrew pitch) × (stud gear teeth / lead gear teeth).
- **Procedure**: Engage half-nut on leadscrew. First pass at 0.1-0.2 mm depth. Disengage half-nut at end of cut, return carriage to start. Re-engage on SAME thread (use thread dial indicator). Increase depth 0.1-0.2 mm per pass. Total depth for 60° thread = 0.614 × pitch. Final pass at full depth with light cut for smooth finish.

**Tap and die production**:
- **Taps** (cut internal threads): Turn HSS rod to diameter, cut 3-4 flutes with mill, thread between flutes on lathe, harden and temper. Three-tap set: taper tap (starts easily), plug tap (general use), bottoming tap (threads to bottom of blind hole).
- **Dies** (cut external threads): Hardened steel plate with threaded hole and 3-4 cutting edges, split by adjustable slot. Die stock holds die and provides leverage.

**Bolt making**: Heat rod end, upset in heading tool to form hex/square head. Turn shank to diameter, cut threads with die. Heat treatment for high-strength bolts: harden at 820°C, quench in oil, temper at 400-500°C (~800 MPa tensile).

### Bearing Design &amp; Production

**Plain (journal) bearings**:
- **Construction**: Cylindrical housing with removable babbitt liner. Babbitt metal: Sn-Sb-Cu alloy (88/8/4 typical) — soft, embeds dirt, conforms to shaft. Pour molten babbitt into shell around mandrel.
- **Clearance**: 0.001-0.002 × shaft diameter (50 mm shaft = 0.05-0.10 mm radial clearance). Too tight → seizure. Too loose → vibration.
- **Load capacity**: Allowable bearing pressure 2-8 MPa for babbitt on steel.

**Rolling element bearings** (Phase 3+ precision):
- **Ball bearing**: Inner ring, outer ring (hardened 52100 steel, 1% C, 1.5% Cr), balls, cage (brass or stamped steel). Standard 6200 series (light): e.g., 6205 = 25 mm bore × 52 mm OD × 15 mm width.
- **Ball production**: Cut wire → cold head into rough spheres → grind between grooved ring plates → lap to 1-5 μm variation. Harden 820-860°C, oil quench, temper 150-200°C.
- **Ring production**: Forge from bearing steel → turn → heat treat (58-62 HRC) → grind raceways → super-finish to 0.05 μm Ra.
- **Assembly**: Press balls into cage between races, rivet cage, pack with grease.

### Lubrication &amp; Coolants

- **Tallow and lard**: Grease plain bearings (apply by hand or oil cup). Lard oil as cutting fluid for turning and threading — reduces friction, improves finish.
- **Vegetable oil** (linseed, castor): Cutting fluid for brass and aluminum. Not ideal for steel (polymerizes and gums).
- **Water with soluble oil**: Best for heavy machining (grinding, milling). 20:1 water-to-emulsifiable-oil ratio. Cools AND lubricates.
- **Sulfurized cutting oil**: For heavy turning and gear cutting. Add flowers of sulfur (5-10%) to mineral oil or lard oil. Extreme pressure lubrication.
- See [SQ 10](../side-quests/sq-10-lubricants-oils.md) for the full production chain.

### Cutting Tool Materials

**Carbon steel tool bits** (first available, Phase 2 steel):
- Composition: 0.8-1.3% carbon steel. Harden by heating to 780-820°C and quenching, temper at 200-250°C.
- Cutting speed: 5-10 m/min for steel, 15-30 m/min for cast iron and brass.
- Loses hardness above ~200°C — limited to light cuts and slow speeds.

**High-speed steel (HSS)** (Phase 4-5, needs alloy elements):
- Composition: Tungsten (18%), chromium (4%), vanadium (1%), carbon (0.7-0.8%) — classic T1 grade. M2 grade: 6% W, 5% Mo, 4% Cr, 2% V.
- Hardness retained to ~600°C — 3-5x faster cutting than carbon steel.
- Manufacturing: Melt alloy in electric furnace (Phase 4), cast, forge, heat treat (austenitize at 1250-1300°C, quench in oil, triple temper at 540-570°C).

**Tool grinding**: Grind tool bits on abrasive wheel to correct geometry:
- **Rake angle**: Positive (5-15°) for aluminum/brass, neutral to negative for steel/heavy cuts.
- **Relief/clearance angle**: 6-12° below cutting edge.
- **Nose radius**: 0.5-2 mm for finishing, sharp for roughing.

## Enables (Downstream)

| Output | Used By |
|--------|---------|
| Precision cylinders (bored true) | Phase 4 (steam engine cylinders — the critical part) |
| Screws, gears, bearings | Phase 4 (generators, motors), Phase 5 (pumps, valves, reactors) |
| Flat surfaces (scraped/lapped) | Phase 6 (optical benches, vacuum seals, gauge blocks) |
| Wire drawing dies | Phase 4 (wire for generators, motors, transformers) |
| Crystal puller mechanics | Phase 7 (Czochralski growth — precision leadscrew for pull mechanism) |
| Wafer saws, polishers | Phase 7 (wafer slicing and CMP) |
| Lithography stages/aligners | Phase 8 (X-Y-θ stages with μm precision) |
| Vacuum pump parts | Phase 6 (precision cylinders, vanes, valves for rotary pumps) |
| Thread standards | ALL subsequent manufacturing (every bolt, screw, pipe fitting) |

## The Iteration Loop

```
Lathe → makes parts for Shaper
Shaper → makes flat surfaces for Mill
Mill → makes parts for better Lathe
Better Lathe → makes parts for Grinder
Grinder → makes parts for everything better
```

This compounding improvement is the most powerful feedback loop in the entire tech tree. Each machine roughly doubles the precision achievable with the previous generation.

## Precision Achievement Milestones

| Generation | Best Tolerance | Surface Finish | Achievable With |
|------------|---------------|---------------|-----------------|
| 0 (hand tools) | ~1 mm | Rough | File, scraper |
| 1 (crude lathe) | ~0.5 mm | 10 μm Ra | Hand-fed, no leadscrew |
| 2 (leadscrew lathe) | ~0.1 mm | 3 μm Ra | Screw-driven feed |
| 3 (shaper + mill) | ~0.05 mm | 1.5 μm Ra | Rigid machines, HSS tools |
| 4 (surface grinder) | ~0.005 mm | 0.4 μm Ra | Abrasive wheel, solid base |
| 5 (lapped/gauge block) | ~0.001 mm | 0.1 μm Ra | Hand lapping, temperature control |

## Practical Bottlenecks

- **First precision**: The gap between "hand-made" and "machine-made" is the hardest to bridge. Expect weeks of scraping to get the first truly flat surface.
- **Flatness and straightness**: Surface plate scraping is tedious (50-100 hours for a 300×450 mm plate) but essential. No shortcut exists.
- **Thread cutting**: Accurate leadscrews require patience and iterative improvement. First leadscrew may have 0.1-0.2 mm pitch error. Use it to make a better one. Each generation halves the error.
- **Materials**: Need consistent cast iron for beds and slideways. Cast iron machines well, absorbs vibration, holds dimension. Aluminum is too flexible for precision machines.
- **Flat belt slipping**: Leather belts slip under heavy load. Keep belts clean, apply belt dressing (rosin/beeswax mixture). Tighten adequately. Toothed belts arrive much later.

## Safety Concerns

- **Rotating machinery**: Entanglement hazard — no loose clothing, tie back hair, remove rings and jewelry. Lathe chucks can grab and pull in entire arm.
- **Hot metal and burns**: Casting involves 660°C (aluminum) to 1250°C (cast iron) metal. Use tongs, leather aprons, face shields. Preheat molds to prevent steam explosions.
- **Metal chips and eye protection**: Turning produces sharp, hot chips (especially steel — blue-hot spirals). Safety glasses mandatory. Chip guards on lathes.
- **Heavy castings**: Machine beds weigh 50-200 kg. Use hoists, rollers, team lifts. Never lift alone.
- **Abrasive wheels**: Can explode if damaged or oversped. Ring test new wheels (suspend and tap — clear ring = good, dull thud = cracked). Never exceed rated RPM. Use wheel guards.

## References

- Dave Gingery, *Build Your Own Metal Working Shop from Scrap* (7-volume series) — the definitive bootstrap guide
- L. T. C. Rolt, *Tools for the Job* (history of machine tools)
- Moltrecht, *Machine Shop Practice* (practical machining reference)

## Side Quest Dependencies

- **[SQ 2: Measurement & Metrology](../side-quests/sq-02-measurement-metrology.md)** — deeply intertwined; you cannot build what you cannot measure. Every tolerance in this phase requires calibrated instruments.
- **[SQ 9: Textiles & Cordage](../side-quests/sq-09-textiles-fiber.md)** — drive belts for line shafts powering machine tools. Canvas or leather belts transmit water wheel or steam engine power to every machine.
- **[SQ 10: Lubricants & Oils](../side-quests/sq-10-lubricants-oils.md)** — bearing lubrication (tallow, lard) and cutting fluids essential for precision work and tool life.
- **[SQ 13: Aircraft Development](../side-quests/sq-13-aircraft-development.md)** — precision cylinders, gear cutting (dividing head), and crankshaft machining from Phase 3 directly enable aircraft piston engines.

[← Phase 2](phase-02-metallurgy.md) | [Overview](overview.md) | [Phase 4: Energy →](phase-04-energy.md)
