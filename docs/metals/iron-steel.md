# Iron & Steel Production

> **Node ID**: metals.iron-steel
> **Domain**: [Metallurgy](./)
> **Dependencies**: `metals.copper-bronze`
> **Enables**: `energy.steam-power`, `machine-tools.casting`, `machine-tools.joining`
> **Timeline**: Years 5-15
> **Outputs**: wrought_iron, steel, iron_bloom, heat_treated_steel, forge_welds, brazed_joints, soldered_joints, springs, bellows, tongs, ...

### Iron Production

Iron requires higher temperatures than copper (melting point 1538°C, but bloomery process works below melting point). This is the critical metallurgical capability that enables all subsequent phases.

**Bloomery smelting**:
- **Principle**: Iron ore is *reduced* (oxygen removed by carbon/CO) but not fully melted. Produces a spongy mass (bloom) of iron + slag + charcoal.
- **Furnace**: Taller than copper furnace (60-120 cm), 30-50 cm diameter. Clay walls with charcoal/sand insulation. MUST have forced air — bellows are non-negotiable.
- **Ores**: Hematite (Fe₂O₃, red), magnetite (Fe₃O₄, black, magnetic), limonite (FeO(OH)·nH₂O, brown/yellow).
- **Process**:
  1. **Preheat** with charcoal and gentle blast, 30 min.
  2. **Charge layers**: Charcoal (3-5 cm) + crushed ore (1-3 cm pieces), alternating. Ratio: ~4-8 kg charcoal per kg ore.
  3. **Full blast**: Temperature reaches 1200-1400°C. This is *below* iron's melting point (1538°C) but above slag melting point (~1100-1200°C).
  4. **Reduction reactions**: Fe₂O₃ → Fe₃O₄ → FeO → Fe (each step driven by CO from charcoal combustion). Total time: 2-6 hours.
  5. **Bloom formation**: Reduced iron particles sinter together into a spongy mass, impregnated with liquid slag. Bloom weighs 5-20 kg typically.
  6. **Extraction**: Break open furnace front, pull out bloom with tongs. It will be white-hot (~1200°C), glowing, covered in slag.

**Consolidating the bloom (wrought iron)**:
1. **Initial forge**: Place bloom on flat stone or iron anvil. Hammer with 2-5 kg stone or iron hammer. Sparks and slag spray out (dangerous — eye protection essential). This compacts the iron and squeezes out liquid slag.
2. **Reheating**: Bloom cools quickly. Reheat in forge (charcoal + bellows, ~1100-1200°C) every 2-3 minutes of hammering. Repeat 10-30 cycles.
3. **Folding and welding**: Heat to bright yellow-orange (~1200-1300°C). Fold iron on itself, hammer to weld the layers together (the heat and pressure cause solid-state welding). This homogenizes the metal and works out remaining slag. Each fold doubles the layers. 6-8 folds = well-consolidated bar.
4. **Result**: Wrought iron bar — soft, ductile, fibrous fracture surface, ~0.02-0.08% carbon. Excellent for forging. Not suitable for edge tools without further treatment.

### Cast Iron

Iron with 2-4.3% carbon — significantly more than wrought iron (<0.1% C) and steel (0.1-2% C). This is what blast furnaces naturally produce when iron is fully melted in contact with carbon fuel. Cast iron is not forgeable (too brittle), but it excels at being cast into complex shapes in sand molds.

**Production — pig iron from blast furnace**:
Blast furnace smelting produces pig iron with typical composition: ~4% C, ~1% Si, ~0.5% Mn, ~0.1% S, ~0.1% P. The high carbon content lowers the melting point from pure iron's 1538°C to ~1150-1200°C, making it fully liquid in the furnace. Pig iron is too brittle for most direct uses — it must be remelted and cast, or refined further into steel.

**Cupola furnace** (for remelting pig iron and scrap):
- **Construction**: Cylindrical steel shell (~1-3 m diameter), lined with refractory brick. Charging door at middle height. Tuyeres (air nozzles) near the bottom connected to blower. Tap hole at the very bottom for molten iron. Slag hole slightly above the tap hole (slag floats on iron).
- **Operation**: Layer coke (fuel) and pig iron/scrap (metal charge) alternately through the charging door. Ignite the coke bed, then turn on the air blast. Metal melts, drips down through coke, and accumulates in the well at the bottom. Open tap hole periodically to let iron flow into ladles for pouring into molds. Slag is tapped separately.
- **Capacity**: Simple, fast, cheap — can melt 1-30 tons/hour depending on size. The workhorse of iron foundries. Can be operated intermittently — start and stop as needed.

**Types of cast iron**:
- **Gray cast iron**: Carbon present as graphite flakes in a matrix of iron. The graphite gives gray color to the fracture surface. Excellent machinability (graphite acts as built-in chip breaker), superior vibration damping (graphite absorbs vibration — ideal for machine bases), good wear resistance, and good thermal conductivity. Tensile strength 150-400 MPa. Casts easily — good fluidity, minimal shrinkage. Used for: machine tool bases and frames, engine blocks, cookware, pipes and fittings, fire hydrants, manhole covers.
- **White cast iron**: Carbon present as cementite (Fe₃C, iron carbide) rather than graphite. Very hard and wear-resistant, but extremely brittle and unmachinable. Chilled castings (rapid cooling against metal mold) produce a white iron surface. Used as intermediate for malleable iron production, or in applications requiring abrasion resistance (rock crusher jaws, mill liners).
- **Malleable iron**: Heat white iron castings at ~900°C for 40-80 hours (annealing). Cementite decomposes → graphite forms as discrete nodules (temper carbon) rather than flakes. The rounded nodules don't act as stress concentrators the way graphite flakes do → improved ductility and toughness vs. gray iron. Can handle moderate impact and bending. Used for pipe fittings, brackets, agricultural implements, hardware.

**Sand casting** (the primary molding method for cast iron):
1. Make a wooden pattern (slightly oversized to account for shrinkage — ~1% for cast iron).
2. Pack molding sand (silica sand + 5-10% clay binder + 3-5% water) around the pattern in a two-part flask (cope and drag).
3. Separate flask halves, remove pattern → cavity remains.
4. Create sprue (pouring channel) and risers (reservoirs to feed shrinkage). Add cores (baked sand shapes) for internal cavities if needed.
5. Close flask, clamp halves together.
6. Pour molten iron from ladle into sprue.
7. Allow to cool (30 minutes to several hours depending on casting size).
8. Break away sand mold, cut off sprue and risers, clean casting. Sand is reusable (recondition by adding fresh clay and water).

**Why cast iron matters**: It bridges the gap between wrought iron and steel. Easier to cast into complex shapes than either (lower melting point, excellent fluidity). Good enough for many structural and machine applications. The dominant structural metal from ~1700 to ~1850 — cast iron bridges (Iron Bridge, Shropshire, 1779), building columns, steam engine cylinders, machine frames, pipes. Superseded by steel for structural use after the Bessemer process (1856) made cheap steel available, but remains indispensable for machine bases, engine blocks, cookware, and pipes.

**Steel production (carburization)**:
- **Pack carburizing**: Pack wrought iron bars in charcoal dust inside sealed clay box. Heat to 900-950°C for 4-12 hours. Carbon from charcoal diffuses into iron surface. Produces 1-2 mm case depth per 4 hours. Result: low-carbon steel skin on wrought iron core.
- **Crucible steel (Wootz/Bulat method):** Place wrought iron + 1-3% carbon (charcoal powder or cast iron) in sealed clay crucible. Heat to 1450-1550°C (requires very good furnace + forced air) for 2-4 hours. Cool slowly. Produces homogeneous medium-to-high carbon steel (~0.8-1.5% C). This is the path to quality cutting tools and springs.

**Heat treatment**:
- **Annealing**: Heat to 700-900°C (bright red), cool slowly (bury in ashes or lime). Softens steel for shaping. Essential after forging.
- **Quenching**: Heat to 780-850°C (cherry red for ~0.8% C steel), plunge into water (hard quench) or oil (softer quench). Makes steel extremely hard but brittle.
- **Tempering**: After quenching, reheat to 200-350°C (pale straw to brown oxidation colors on polished surface) for 30-60 minutes. Reduces brittleness while retaining most hardness. Temperature controls hardness-toughness tradeoff.

### Metalworking Tools

**Anvil evolution**:
- **Stone anvil**: Large flat granite or basalt boulder (50+ kg). Bounces hammer energy but works for copper and early iron. Use flat face for hammering, edge for bending.
- **Iron anvil**: Cast or forged from wrought iron with steel face (carburized and hardened). 20-100+ kg. Must be bolted to heavy stump. Returns hammer energy efficiently. The single most important tool in the smithy.

**Hammer types**:
- **Cross-peen hammer**: 1-3 kg iron head, one flat face, one wedge-shaped peen. General forging, drawing out metal, starting nail/rod shapes.
- **Ball-peen hammer**: Flat face + rounded peen. Riveting, shaping curves.
- **Sledge hammer**: 4-8 kg, two-handed. Heavy forging, bloom consolidation.

**Bellows construction**:
- **Skin/bag bellows**: Animal hide (goat, sheep) sewn into bag with valve (flap of leather over hole) at bottom and nozzle (clay tube or hollow wood) at top. Operator opens bag (valve admits air), then presses/expels air through nozzle into furnace. Produces intermittent blast.
- **Piston bellows**: Wooden box (30×30×60 cm) with leather-gasketed piston, one-way valve. More consistent air flow. 60-100 strokes/minute. Connect to tuyere with clay pipe.
- **Air delivery**: 100-300 liters/minute per bellows operator. Multiple bellows in parallel for larger furnaces. Tuyere diameter 2-4 cm.

**Essential smithy tools**:
- Tongs (3+ pairs of different jaw sizes for holding different stock)
- Chisels (hot cut, cold cut — different hardness/temper)
- Punches and drifts (for making holes in hot metal)
- Swages (shaped recesses for forming specific profiles)
- Fuller (round-nosed tool for grooving/necking stock)
- Slack tub (water barrel for quenching, ~50 liters)

### Joining Metals — Forge Welding, Brazing & Soldering

**Forge welding** (the oldest welding method):
- **Principle**: Heat two pieces of iron/steel to bright yellow-white (~1300-1400°C) where the surface becomes pasty. Place together and hammer forcefully. The combination of heat, pressure, and clean surfaces causes a solid-state weld (atomic diffusion across interface).
- **Flux**: Sprinkle clean silica sand or borax on joint surfaces before welding. Flux melts, dissolves surface oxide (scale), and prevents oxidation during heating — allowing metal-to-metal contact. Without flux, scale prevents a sound weld.
- **Procedure**: Stack or overlap the pieces to be joined. Heat both evenly in forge fire. When metal reaches bright yellow-white (visible through scale breaking surface), quickly remove, brush off loose scale, apply flux if needed, position pieces on anvil, and strike firmly with hammer. Multiple rapid blows. Reheat and re-strike if needed for longer joints.
- **Joint types**: Lap joint (overlapping flat pieces — easiest), scarf joint (diagonal taper on both pieces, overlapped — stronger for bars), faggot weld (bundle of bars welded together for composite billets — used in Damascus/pattern-welded steel).
- **Quality test**: Bend test — a good weld bends without opening at the joint. Poor welds crack at the seam (oxide inclusion or insufficient heat).
- **Applications**: Welding iron bars into longer bars, making composite steel (pattern-welded blades), building up large forgings from smaller pieces, repairing broken tools, making chain links, hoop iron for barrels and wagon wheels.

**Brazing** (joining with filler metal, later stages):
- **Principle**: Heat base metals to above the melting point of filler (but below their own melting point). Capillary action draws molten filler into the joint gap. On cooling, filler solidifies — strong joint without melting base metal.
- **Brass brazing (spelter brazing)**: Filler = brass alloy (Cu + Zn, typically 60/40, melts ~900°C). Flux = borax (sodium borate) paste. Heat joint to bright red (~950°C). Apply brazing rod — brass melts, flows into joint by capillary action. Strong joint, higher temperature than soldering.
- **Silver brazing (silver soldering)**: Filler = Ag-Cu-Zn alloy (melts 620-750°C depending on composition). Lower temperature than brass brazing, stronger than soft solder. Used for jewelry, instrument work, fine mechanisms. More expensive filler (requires silver).
- **Applications**: Joining dissimilar metals, joining cast iron (difficult to forge weld), making watertight joints (pipes, tanks, heat exchangers), bicycle frames, tool joints.

**Soft soldering** (lowest temperature joining):
- **Solder**: Tin-lead alloy (60/40 Sn/Pb melts at ~190°C; 50/50 melts at ~215°C). Lead-free alternatives: tin-silver (Sn-3.5Ag, melts ~221°C), tin-copper (Sn-0.7Cu, melts ~227°C). Produce by melting tin and lead together in iron ladle.
- **Flux**: Rosin (pine resin — dissolves oxides at soldering temperature), or zinc chloride solution (acidic — more aggressive cleaning, must be washed off after soldering to prevent corrosion). Make zinc chloride by dissolving zinc in hydrochloric acid.
- **Procedure**: Clean joint surfaces to bare metal (file, sand, scrape). Apply flux. Heat joint with copper soldering iron (copper bit heated in flame or on stove, holds heat well due to high thermal conductivity — tip temperature ~250-350°C). Touch solder to heated joint — solder melts, flows into joint by capillary action. Remove heat, hold still until solidified.
- **Applications**: Electrical connections (wire splices, terminals), plumbing (lead pipe joints, later copper pipe), tin-plated food containers, sheet metal seams (lanterns, ductwork), jewelry.

**Spring making** (critical for mechanisms, locks, suspensions, valves):
- **Material**: High-carbon steel (0.6-1.0% C) or spring steel (silicon-manganese steel 0.5-0.7% C + 1.5-2% Si). Higher carbon = harder spring, but more brittle.
- **Leaf spring**: Forge steel bar to flat taper. Heat to bright cherry red (~820°C). Bend over form or anvil horn to desired curve. Quench in oil (not water — water quenching high-carbon steel causes cracking). Temper at 350-450°C (light straw to brown oxide color) to relieve brittleness while maintaining elasticity. Stack multiple leaves (graduated lengths) for progressive spring rate. Bolt together with center bolt. For vehicle suspensions, the dominant spring type until coil springs.
- **Coil spring**: Wind high-carbon steel wire (drawn through successively smaller dies) around mandrel of desired diameter. Heat to austenitizing temperature (~820°C for 0.8% C steel). Quench in oil. Temper at 300-400°C. Compression springs: closed and ground ends. Extension springs: hooks formed at ends.
- **Torsion spring**: Wound wire that stores energy through twisting rather than bending. Heat treatment same as coil spring. Used in clothes pins, mouse traps, clock mechanisms, door hinges.
- **Flat spring**: Thin strip of hardened and tempered spring steel. Used in locks, snaps, electrical contacts, measuring instruments (galvanometer springs). File to consistent thickness, bend to shape, heat treat.
- **Testing**: Compress/bend spring and measure recovery. Spring should return to original shape without permanent deformation. Fatigue test: cycle spring many times (1000+) — if it breaks, temper at slightly higher temperature to increase toughness.

### Safety & Hazards

- **Extreme heat and burn risk**: Bloomery furnaces reach 1200-1400°C; extracted blooms glow white-hot at ~1200°C. Forge welding requires heating iron to 1300-1400°C (bright yellow-white). At these temperatures, radiation burns occur within seconds of close proximity. Wear heavy leather apron, gloves, face shield, and closed-toe boots. Use tongs sized to the work — dropping white-hot iron causes severe burns and fires. Maintain a clear, dry floor around the forge (no water puddles — steam explosions from spilled molten slag).
- **Carbon monoxide from charcoal combustion**: Bloomery smelting consumes charcoal at high rates, producing large volumes of carbon monoxide. CO is colorless, odorless, and causes headache, confusion, loss of consciousness, and death. Never operate a bloomery or forge in an enclosed space. Ensure cross-ventilation. If an operator becomes confused or lethargic, move them to fresh air immediately and monitor breathing.
- **Spark and slag spray during bloom consolidation**: Hammering the white-hot bloom ejects slag particles and sparks at temperatures exceeding 1000°C. Eye protection is explicitly essential — the text notes "eye protection essential" for this operation. Use safety glasses or a full face shield. Long sleeves and leather gloves prevent spark burns on forearms and hands.
- **Lead and zinc fume hazards from soldering and brazing**: Soft solder (60/40 tin-lead alloy) produces lead fumes above 500°C; brass brazing filler (60/40 copper-zinc) produces zinc oxide fumes at ~900°C. Zinc oxide fume causes "metal fume fever" (flu-like symptoms: chills, fever, muscle ache, 4-8 hours after exposure). Lead fume causes cumulative neurological and organ damage. Solder and braze with local exhaust ventilation. Avoid breathing fumes directly. Wash hands after handling solder materials.
- **Quenching hazards**: Plunging hot steel (780-850°C) into water produces violent boiling and steam splash. Oil quenching (used for springs and high-carbon steel to prevent cracking) creates risk of oil ignition — the oil can flash if the workpiece is too hot. Use a deep quench tank, lower the workpiece quickly and completely, and keep a lid nearby to smother oil fires. Do not use oil quenching near open flames.
---

*Part of the [Bootciv Tech Tree](../) • [Metals](./) • [All Domains](../)*
