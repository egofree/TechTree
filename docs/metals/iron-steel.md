# Iron & Steel Production

> **Node ID**: metals.iron-steel
> **Also covers**: `metallurgy.metalworking`
> **Domain**: [Metallurgy](./)
> **Dependencies**: `metallurgy.iron-steel`
> **Enables**: `energy.ice`, `energy.steam-power`, `machine-tools.foundry`, `metallurgy.metalworking`
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

**Steel production (carburization)**:
- **Pack carburizing**: Pack wrought iron bars in charcoal dust inside sealed clay box. Heat to 900-950°C for 4-12 hours. Carbon from charcoal diffuses into iron surface. Produces 1-2 mm case depth per 4 hours. Result: low-carbon steel skin on wrought iron core.
- **Crucible steel (Wootz/Bulat method)****: Place wrought iron + 1-3% carbon (charcoal powder or cast iron) in sealed clay crucible. Heat to 1450-1550°C (requires very good furnace + forced air) for 2-4 hours. Cool slowly. Produces homogeneous medium-to-high carbon steel (~0.8-1.5% C). This is the path to quality cutting tools and springs.

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

### Joining Metals — Forge Welding, Brazing &amp; Soldering

**Forge welding** (the oldest welding method, (Metallurgy stage):
- **Principle**: Heat two pieces of iron/steel to bright yellow-white (~1300-1400°C) where the surface becomes pasty. Place together and hammer forcefully. The combination of heat, pressure, and clean surfaces causes a solid-state weld (atomic diffusion across interface).
- **Flux**: Sprinkle clean silica sand or borite on joint surfaces before welding. Flux melts, dissolves surface oxide (scale), and prevents oxidation during heating — allowing metal-to-metal contact. Without flux, scale prevents a sound weld.
- **Procedure**: Stack or overlap the pieces to be joined. Heat both evenly in forge fire. When metal reaches bright yellow-white (visible through scale breaking surface), quickly remove, brush off loose scale, apply flux if needed, position pieces on anvil, and strike firmly with hammer. Multiple rapid blows. Reheat and re-strike if needed for longer joints.
- **Joint types**: Lap joint (overlapping flat pieces — easiest), scarf joint (diagonal taper on both pieces, overlapped — stronger for bars), faggot weld (bundle of bars welded together for composite billets — used in Damascus/pattern-welded steel).
- **Quality test**: Bend test — a good weld bends without opening at the joint. Poor welds crack at the seam (oxide inclusion or insufficient heat).
- **Applications**: Welding iron bars into longer bars, making composite steel (pattern-welded blades), building up large forgings from smaller pieces, repairing broken tools, making chain links, hoop iron for barrels and wagon wheels.

**Brazing** (joining with filler metal, Metallurgy+):
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
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
