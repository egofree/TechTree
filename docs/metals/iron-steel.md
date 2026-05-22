# Iron & Steel Production

> **Node ID**: metals.iron-steel
> **Domain**: [Metallurgy](./)
> **Dependencies**: [`metals.copper-bronze`](copper-bronze.md)
> **Enables**: [`energy.steam-power`](../energy/steam-power.md), [`machine-tools.casting`](../machine-tools/casting.md), [`machine-tools.joining`](../machine-tools/joining.md)
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

**[Cupola furnace](../glossary/cupola-furnace.html)** (for remelting pig iron and scrap):
- **Construction**: Cylindrical steel shell (~1-3 m diameter), lined with refractory brick. Charging door at middle height. Tuyeres (air nozzles) near the bottom connected to blower. Tap hole at the very bottom for molten iron. Slag hole slightly above the tap hole (slag floats on iron).
- **Operation**: Layer coke (fuel) and pig iron/scrap (metal charge) alternately through the charging door. Ignite the coke bed, then turn on the air blast. Metal melts, drips down through coke, and accumulates in the well at the bottom. Open tap hole periodically to let iron flow into ladles for pouring into molds. Slag is tapped separately.
- **Capacity**: Simple, fast, cheap — can melt 1-30 tonnes/hour depending on size. The workhorse of iron foundries. Can be operated intermittently — start and stop as needed.

**Types of cast iron**:
- **Gray cast iron**: Carbon present as graphite flakes in a matrix of iron. The graphite gives gray color to the fracture surface. Excellent machinability (graphite acts as built-in chip breaker), superior vibration damping (graphite absorbs vibration — ideal for machine bases), good wear resistance, and good thermal conductivity. Tensile strength 150-400 MPa. Casts easily — good fluidity, minimal shrinkage. Used for: machine tool bases and frames, engine blocks, cookware, pipes and fittings, fire hydrants, manhole covers.
- **White cast iron**: Carbon present as cementite (Fe₃C, iron carbide) rather than graphite. Very hard and wear-resistant, but extremely brittle and unmachinable. Chilled castings (rapid cooling against metal mold) produce a white iron surface. Used as intermediate for malleable iron production, or in applications requiring abrasion resistance (rock crusher jaws, mill liners).
- **Malleable iron**: Heat white iron castings at ~900°C for 40-80 hours (annealing). Cementite decomposes → graphite forms as discrete nodules (temper carbon) rather than flakes. The rounded nodules don't act as stress concentrators the way graphite flakes do → improved ductility and toughness vs. gray iron. Can handle moderate impact and bending. Used for pipe fittings, brackets, agricultural implements, hardware.

**[Sand casting](../glossary/sand-casting.html)** (the primary molding method for cast iron):
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
- **[Crucible steel (Wootz/Bulat method):](../glossary/crucible-steel-wootzbulat-method.html)** Place wrought iron + 1-3% carbon (charcoal powder or cast iron) in sealed clay crucible. Heat to 1450-1550°C (requires very good furnace + forced air) for 2-4 hours. Cool slowly. Produces homogeneous medium-to-high carbon steel (~0.8-1.5% C). This is the path to quality cutting tools and springs.

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

**[Forge welding](../glossary/forge-welding.html)** (the oldest welding method):
- **Principle**: Heat two pieces of iron/steel to bright yellow-white (~1300-1400°C) where the surface becomes pasty. Place together and hammer forcefully. The combination of heat, pressure, and clean surfaces causes a solid-state weld (atomic diffusion across interface).
- **Flux**: Sprinkle clean silica sand or borax on joint surfaces before welding. Flux melts, dissolves surface oxide (scale), and prevents oxidation during heating — allowing metal-to-metal contact. Without flux, scale prevents a sound weld.
- **Procedure**: Stack or overlap the pieces to be joined. Heat both evenly in forge fire. When metal reaches bright yellow-white (visible through scale breaking surface), quickly remove, brush off loose scale, apply flux if needed, position pieces on anvil, and strike firmly with hammer. Multiple rapid blows. Reheat and re-strike if needed for longer joints.
- **Joint types**: Lap joint (overlapping flat pieces — easiest), scarf joint (diagonal taper on both pieces, overlapped — stronger for bars), faggot weld (bundle of bars welded together for composite billets — used in Damascus/pattern-welded steel).
- **Quality test**: Bend test — a good weld bends without opening at the joint. Poor welds crack at the seam (oxide inclusion or insufficient heat).
- **Applications**: Welding iron bars into longer bars, making composite steel (pattern-welded blades), building up large forgings from smaller pieces, repairing broken tools, making chain links, hoop iron for barrels and wagon wheels.

**[Brazing](../glossary/brazing.html)** (joining with filler metal, later stages):
- **Principle**: Heat base metals to above the melting point of filler (but below their own melting point). Capillary action draws molten filler into the joint gap. On cooling, filler solidifies — strong joint without melting base metal.
- **Brass brazing (spelter brazing)**: Filler = brass alloy (Cu + Zn, typically 60/40, melts ~900°C). Flux = borax (sodium borate) paste. Heat joint to bright red (~950°C). Apply brazing rod — brass melts, flows into joint by capillary action. Strong joint, higher temperature than soldering.
- **Silver brazing (silver soldering)**: Filler = Ag-Cu-Zn alloy (melts 620-750°C depending on composition). Lower temperature than brass brazing, stronger than soft solder. Used for jewelry, instrument work, fine mechanisms. More expensive filler (requires silver).
- **Applications**: Joining dissimilar metals, joining cast iron (difficult to forge weld), making watertight joints (pipes, tanks, heat exchangers), bicycle frames, tool joints.

**[Soft soldering](../glossary/soft-soldering.html)** (lowest temperature joining):
- **Solder**: Tin-lead alloy (60/40 Sn/Pb melts at ~190°C; 50/50 melts at ~215°C). Lead-free alternatives: tin-silver (Sn-3.5Ag, melts ~221°C), tin-copper (Sn-0.7Cu, melts ~227°C). Produce by melting tin and lead together in iron ladle.
- **Flux**: Rosin (pine resin — dissolves oxides at soldering temperature), or zinc chloride solution (acidic — more aggressive cleaning, must be washed off after soldering to prevent corrosion). Make zinc chloride by dissolving zinc in hydrochloric acid.
- **Procedure**: Clean joint surfaces to bare metal (file, sand, scrape). Apply flux. Heat joint with copper soldering iron (copper bit heated in flame or on stove, holds heat well due to high thermal conductivity — tip temperature ~250-350°C). Touch solder to heated joint — solder melts, flows into joint by capillary action. Remove heat, hold still until solidified.
- **Applications**: Electrical connections (wire splices, terminals), plumbing (lead pipe joints, later copper pipe), tin-plated food containers, sheet metal seams (lanterns, ductwork), jewelry.

**[Spring making](../glossary/spring-making.html)** (critical for mechanisms, locks, suspensions, valves):
- **Material**: High-carbon steel (0.6-1.0% C) or spring steel (silicon-manganese steel 0.5-0.7% C + 1.5-2% Si). Higher carbon = harder spring, but more brittle.
- **Leaf spring**: Forge steel bar to flat taper. Heat to bright cherry red (~820°C). Bend over form or anvil horn to desired curve. Quench in oil (not water — water quenching high-carbon steel causes cracking). Temper at 350-450°C (light straw to brown oxide color) to relieve brittleness while maintaining elasticity. Stack multiple leaves (graduated lengths) for progressive spring rate. Bolt together with center bolt. For vehicle suspensions, the dominant spring type until coil springs.
- **Coil spring**: Wind high-carbon steel wire (drawn through successively smaller dies) around mandrel of desired diameter. Heat to austenitizing temperature (~820°C for 0.8% C steel). Quench in oil. Temper at 300-400°C. Compression springs: closed and ground ends. Extension springs: hooks formed at ends.
- **Torsion spring**: Wound wire that stores energy through twisting rather than bending. Heat treatment same as coil spring. Used in clothes pins, mouse traps, clock mechanisms, door hinges.
- **Flat spring**: Thin strip of hardened and tempered spring steel. Used in locks, snaps, electrical contacts, measuring instruments (galvanometer springs). File to consistent thickness, bend to shape, heat treat.
- **Testing**: Compress/bend spring and measure recovery. Spring should return to original shape without permanent deformation. Fatigue test: cycle spring many times (1000+) — if it breaks, temper at slightly higher temperature to increase toughness.

### Carbon Steel Grades

Plain carbon steels are classified by the SAE/AISI 10xx system, where "10" denotes plain carbon steel and "xx" gives the carbon content in hundredths of a percent (e.g., 1020 = 0.20% C). Carbon is the dominant alloying element — each 0.1% increase in carbon raises tensile strength by ~70-80 MPa and hardness by ~15-20 HRC (after quenching), but reduces ductility and weldability. Manganese (0.3-0.6% in most grades) provides deoxidation and moderate solid-solution strengthening. Phosphorus and sulfur are impurities kept below 0.05% and 0.05% respectively — they cause temper brittleness and hot shortness.

**Low carbon steel (mild steel, 0.05-0.25% C)**:
- **Grades**: 1006, 1008, 1010, 1015, 1018, 1020, 1025.
- **Properties**: Tensile strength 300-500 MPa (yield 180-350 MPa). Elongation 20-35%. Excellent ductility and formability — can be cold-rolled, deep-drawn, bent, and stamped without cracking. Good weldability (no preheat required for most thicknesses). Low hardenability — does not respond significantly to quenching.
- **Uses**: Structural shapes (I-beams, channels, angles — A36 specification at 0.26% C max), sheet and plate (automotive body panels, appliance housings, ductwork), wire (fencing, nails, baling wire), pipe and tubing, cold-headed fasteners (bolts, rivets). The workhorse of civilization — ~90% of all steel produced is mild steel.
- **Heat treatment response**: Negligible hardening from quenching. Case hardening (carburizing) used when a hard wear surface is needed on a tough core.

**Medium carbon steel (0.25-0.60% C)**:
- **Grades**: 1030, 1035, 1040, 1045, 1050, 1055, 1060.
- **Properties**: Tensile strength 500-900 MPa (quenched and tempered). Elongation 10-20% (heat-treated). Moderate hardenability — can be through-hardened in sections up to ~25-50 mm diameter by oil quenching. Good balance of strength, toughness, and wear resistance. Weldability decreases with carbon content — preheat to 150-250°C for >0.35% C to prevent hydrogen cracking.
- **Uses**: Forgings (crankshafts, connecting rods, gear blanks, axle shafts), machined components (shafts, spindles, couplings, hydraulic cylinder rods), railway rails and wheels (1080-1100 MPa tensile), high-strength bolts (Grade 5 and Grade 8), agricultural implements (plowshares, cultivator tines).
- **Heat treatment**: Quench and temper is the standard processing route. Austenitize at 820-870°C, quench in oil (or water for simple shapes <25 mm), temper at 400-650°C to achieve target strength-toughness combination. Normalizing (air cool from 850-900°C) used for uniform fine-grained structure before machining.

**High carbon steel (0.60-1.00% C)**:
- **Grades**: 1060, 1070, 1080, 1084, 1090, 1095.
- **Properties**: Tensile strength 700-1300 MPa (heat-treated). Elongation 5-12%. Very high hardness and wear resistance after quenching (55-65 HRC for 0.8-1.0% C). Low ductility — cannot be cold-formed extensively. Poor weldability — requires careful preheat and post-weld heat treatment. High spring properties (high elastic limit, good fatigue resistance).
- **Uses**: Springs (leaf, coil, flat — see Spring Making above), cutting tools (chisels, plane blades, knives, axes), wire (music wire, piano wire at 0.8-0.9% C — tensile strength up to 3000 MPa as cold-drawn), saw blades, files, rasps, agricultural cutting edges (scythes, sickles), wear plates.
- **Eutectoid composition**: At 0.76-0.83% C, the steel is exactly at the eutectoid point. Slow cooling produces 100% pearlite (alternating lamellae of ferrite and cementite, spacing ~0.1-1 μm). This composition has the finest pearlite and the most uniform response to heat treatment — preferred for blades and springs.

### Heat Treatment in Depth

The iron-carbon phase diagram defines the transformations that make steel uniquely versatile among structural metals. Steel can be hardened because iron undergoes an allotropic transformation: ferrite (BCC, α-iron) transforms to austenite (FCC, γ-iron) at 727°C (the eutectoid temperature) in the presence of carbon. The FCC structure dissolves up to 2.14% carbon; the BCC structure dissolves only 0.022%. This difference is the engine of heat treatment.

**TTT (Time-Temperature-Transformation) diagrams**:
- Also called IT (isothermal transformation) or C-curve diagrams. Plot transformation products vs. time at constant temperature for a given composition and austenite grain size.
- **Upper region (550-727°C)**: Austenite transforms to **pearlite**. At higher temperatures (~650-727°C), coarse pearlite forms (lamellar spacing ~0.5-1 μm, hardness ~15-25 HRC). At lower temperatures (~550-650°C), fine pearlite or sorbite forms (spacing ~0.1-0.3 μm, hardness ~30-40 HRC). Transformation starts in seconds to minutes.
- **Lower region (200-550°C)**: Austenite transforms to **bainite**. Upper bainite (350-550°C) consists of laths of ferrite with discrete cementite particles — moderate hardness (~40-50 HRC), good toughness. Lower bainite (200-350°C) has acicular (needle-like) ferrite plates with fine epsilon-carbide precipitates within the plates — high hardness (~45-55 HRC) with better toughness than martensite at equivalent hardness. Bainite forms over minutes to hours.
- **Martensite region (below ~200°C for most carbon steels)**: If austenite is cooled fast enough to miss the pearlite and bainite noses on the TTT diagram, it transforms to **[martensite](../glossary/martensite.html)** by a diffusionless shear mechanism. Carbon atoms are trapped in the BCT (body-centered tetragonal) lattice, causing severe lattice strain — this is what makes martensite hard (50-65 HRC depending on carbon content). Martensite starts forming at the Ms temperature (~200-350°C depending on carbon content) and finishes at Mf (~-50 to 150°C). Transformation is instantaneous at each temperature — no holding time needed.
- **Critical cooling rate**: The minimum cooling rate that avoids the pearlite nose entirely. For plain carbon steels, this is very fast (~100-600°C/second), requiring water quenching. This is why plain carbon steels have poor hardenability — only thin sections can be through-hardened.

**Hardenability — Jominy end-quench test**:
- A standardized test (ASTM A255) that measures how deep hardness penetrates into a steel section. A cylindrical specimen (25 mm diameter × 100 mm long) is austenitized at a standard temperature, then one end is quenched with a controlled water jet. This produces a continuous gradient of cooling rates from the quenched end (fastest) to the far end (slowest).
- After quenching, a flat is ground along the length and Rockwell hardness measured every 1.5 mm. The resulting Jominy curve (hardness vs. distance from quenched end) characterizes the steel's hardenability.
- Plain carbon steels (10xx) show steep hardness drop-off — the quenched end is hard martensite but within 5-10 mm the hardness drops to pearlite levels. Alloy steels (41xx, 51xx, 86xx) maintain hardness much further from the quenched end due to alloying elements shifting the TTT curves to longer times (slower critical cooling rate).
- **Practical significance**: Hardenability determines the maximum section size that can be through-hardened. A steel with high hardenability can be oil-quenched (less distortion, lower cracking risk) in larger sections and still achieve full martensite through the core.

**[Surface hardening methods](../glossary/surface-hardening-methods.html)** (hard surface + tough core):
- **Carburizing**: Pack the part in carbonaceous material (charcoal + energizer like BaCO₃ or Na₂CO₃) and heat to 900-950°C for 4-12 hours. Carbon diffuses into the low-carbon steel surface, producing a high-carbon case (0.7-1.0% C) over a tough low-carbon core. Case depth: 0.5-2 mm (roughly 0.5 mm per 4 hours at 925°C). After carburizing, quench to harden the case. Used for: gears, camshafts, bearings, pins — any part requiring wear-resistant surface with impact-resistant core.
- **Nitriding**: Heat medium-carbon steel (containing nitride-forming elements Al, Cr, Mo, V) to 500-590°C in ammonia gas (NH₃) atmosphere for 20-100 hours. Nitrogen from dissociated NH₃ diffuses into the surface and forms hard nitride precipitates (AlN, VN, CrN). Surface hardness 65-70 HRC (harder than carburized case). No quenching required — minimal distortion. Excellent fatigue life. Slow process but produces the hardest surface of any common treatment. Used for: precision gears, valve seats, injector nozzles, die surfaces.
- **Induction hardening**: Place steel part inside water-cooled copper induction coil. High-frequency alternating current (10-500 kHz) induces eddy currents in the part surface, heating it to austenitizing temperature (850-950°C) within seconds. Immediately spray-quench with water. Only the surface layer transforms to martensite; the core remains unaffected. Case depth controlled by frequency: higher frequency = shallower case (0.5-2 mm at 200-500 kHz; 2-5 mm at 10-50 kHz). Fast, localized, repeatable — ideal for high-volume production. Used for: shaft journals, gear teeth, cam lobes, bearing seats, piston rods.
- **Flame hardening**: Oxy-acetylene or oxy-propane torch heats the surface to austenitizing temperature, followed immediately by water spray quench. Manual or mechanized. Less precise than induction but requires no special equipment beyond a torch and water spray. Used for: large gears, crane wheels, rail ends, wear plates — parts too large for induction coils.

### Quality and Testing

The mechanical properties of iron and steel must be verified at every stage — from incoming raw material to finished component. The following test methods form the core of ferrous metallurgical quality control.

**Tensile testing**:
- **Method**: Universal Testing Machine (UTM) pulls a standardized specimen (typically 12.5 mm or 6.25 mm diameter gauge section, 50 mm gauge length) at a constant crosshead speed until fracture. Load and extension are continuously recorded.
- **Stress-strain curve interpretation**:
  - **Elastic region**: Linear stress-strain relationship (Hooke's law). Slope = Young's modulus (~200 GPa for steel). Reversible deformation.
  - **Yield point**: For low-carbon steel, a distinct upper yield point followed by a lower yield point and a yield point elongation (Lüders bands). For higher-carbon and alloy steels, the offset method (0.2% offset) defines yield strength. This is the practical limit for structural design — stresses below yield produce no permanent deformation.
  - **Strain hardening region**: Between yield and UTS, the steel strengthens by dislocation multiplication and pileup. The slope decreases as necking approaches.
  - **Ultimate Tensile Strength (UTS)**: Maximum load divided by original cross-sectional area. The peak of the engineering stress-strain curve.
  - **Elongation and reduction of area**: After fracture, fit the broken ends together and measure final gauge length. Elongation = (final - initial) / initial × 100%. Reduction of area = (original area - fracture area) / original area × 100%. These measure ductility — critical for forming operations and structural safety.
- **Typical values**: A36 structural steel: yield 250 MPa, UTS 400-550 MPa, elongation 20-23%. 1045 Q&T: yield 530 MPa, UTS 700 MPa, elongation 15%. 1095 quenched: UTS 1100+ MPa, elongation <10%.

**Impact testing (Charpy V-notch)**:
- **Method**: A notched bar specimen (10 × 10 × 55 mm, 2 mm deep 45° V-notch) is struck by a swinging pendulum. The energy absorbed in fracturing the specimen is measured by the height the pendulum reaches after breaking the sample.
- **Ductile-to-brittle transition temperature (DBTT)**: Test specimens at a range of temperatures (-80 to +100°C). BCC metals (ferritic steel) exhibit a sharp transition from ductile (high energy absorption, ~100-200 J) to brittle (low energy, ~5-30 J) fracture over a narrow temperature range. The DBTT is the temperature at which the fracture appearance is 50% ductile (fibrous) and 50% brittle (cleavage). For mild steel, DBTT is typically -20 to +20°C depending on composition and grain size.
- **Significance**: The DBTT must be well below the minimum service temperature. Liberty ship failures (1942-1944) were caused by welds with DBTT above the North Atlantic water temperature — ships literally cracked in half. Grain refinement (killed steel practice, normalizing, microalloy additions of Nb, V, Ti) lowers DBTT. Higher carbon and phosphorus raise DBTT.
- **[FCC metals](../glossary/fcc-metals.html)** (austenitic stainless, aluminum, copper) do not exhibit a DBTT — they remain ductile to cryogenic temperatures.

**Hardness testing**:
- **Brinell (HBW)**: 10 mm tungsten carbide ball pressed into the surface at 3000 kgf (for steel). Measure the indentation diameter with a low-power microscope. HBW = load / indentation area. Good for castings and forgings (large indentation averages out local variations). Range: 50-600 HBW.
- **Rockwell**: Minor load (10 kgf) seats the indenter, then major load (60, 100, or 150 kgf depending on scale) is applied. Hardness read directly from the dial or display — measures depth of penetration, not area. Fast, no optical measurement needed. Common scales: HRC (150 kgf, diamond cone, for hardened steel, range 20-70), HRB (100 kgf, 1/16" ball, for soft steel, range 60-100), HRA (60 kgf, diamond cone, for carbides and thin hard cases).
- **Vickers (HV)**: Diamond pyramid indenter, any load from 10 gf (microhardness) to 100 kgf. Measure diagonal of the square indentation. HV = 1.854 × load / diagonal². One continuous scale covers all metals. Ideal for microstructural analysis (hardness of individual phases, case depth measurement, heat-affected zone mapping). Range: 5-2000 HV.
- **Practical correlations**: For carbon steels, approximate UTS (MPa) ≈ 3.45 × HBW ≈ 3.55 × HRC (for HRC > 20). These correlations allow non-destructive strength estimation in the field.

**Metallography**:
- Cut, mount (in bakelite or epoxy), grind (120-600 grit SiC paper), polish (diamond paste 6 → 1 → 0.25 μm), etch (2% nital — nitric acid in ethanol — for carbon steels; reveals grain boundaries, ferrite/pearlite distribution, martensite, bainite). Examine under optical microscope at 100-1000×. Grain size measured by ASTM grain size number (G = 1 at ~15 grains/mm² to G = 8 at ~2000 grains/mm²). Finer grain size (higher G) means higher yield strength (Hall-Petch relationship: σ_y = σ₀ + k / √d) and lower DBTT.

**Non-destructive testing (NDT)**:
- **Ultrasonic testing (UT)**: High-frequency sound waves (1-10 MHz) transmitted through the part. Internal defects (cracks, inclusions, porosity) reflect the sound back to the transducer. Pulse-echo technique: time delay = distance to defect, amplitude = defect size. Portable flaw detectors for field inspection of shafts, pressure vessels, welds. Can detect defects as small as 0.5 mm in favorable geometry.
- **Magnetic particle inspection (MPI)**: Applicable only to ferromagnetic materials (iron and steel). Magnetize the part with a portable yoke or coil. Apply magnetic particles (dry powder or wet fluorescent suspension). Particles accumulate at surface and near-surface defects (cracks, seams, laps) where magnetic flux leaks out. Under UV light (fluorescent method), indications glow brightly. Fast, inexpensive — the standard method for inspecting welds, shafts, forgings, and castings in the field.
- **Dye penetrant testing (PT)**: Clean the surface, apply red dye penetrant (let dwell 10-30 minutes to seep into surface defects), wipe off excess, apply white developer (draws dye back out of defects). Red indications on white background show surface-breaking cracks, porosity, laps. Works on any non-porous material. Simpler than MPI but detects only surface-breaking defects.
- **Radiographic testing (RT)**: X-ray or gamma ray (Ir-192 or Co-60 source) passes through the part onto film or digital detector. Internal defects (porosity, slag inclusions, incomplete fusion, cracks oriented parallel to the beam) appear as density variations on the radiograph. The most expensive and slowest NDT method but the only one that provides a permanent visual record of internal condition. Standard for pressure vessel welds and critical structural castings.

### Wrought Iron vs Steel vs Cast Iron

These three forms of iron-carbon alloy represent fundamentally different material classes, each suited to different applications. The carbon content — and the form that carbon takes — is the primary differentiator.

| Property | Wrought Iron | Carbon Steel | Gray Cast Iron |
|---|---|---|---|
| **Carbon content** | 0.02-0.08% | 0.05-1.0% | 2.5-4.0% |
| **Carbon form** | Slag inclusions (fibrous) | Dissolved in ferrite + cementite (Fe₃C) | Graphite flakes in iron matrix |
| **Melting range** | ~1500-1538°C (nearly pure iron) | 1400-1520°C (decreases with C) | 1150-1250°C (low due to high C) |
| **Tensile strength** | 200-350 MPa | 300-1300 MPa (depends on grade/heat treatment) | 150-400 MPa |
| **Yield strength** | 150-250 MPa | 180-1000+ MPa | No definite yield point |
| **Elongation** | 15-25% | 5-35% (depends on grade/heat treatment) | <1% (brittle) |
| **Hardness (HBW)** | 100-120 | 120-650 (heat-treated) | 150-280 |
| **Ductility** | Excellent — can be hot- and cold-worked extensively | Good (low C) to poor (high C) | Nil — cannot be forged or rolled |
| **Castability** | Poor — cannot be cast into shapes (too high melting point, no fluidity) | Moderate — limited casting applications | Excellent — low melting point, high fluidity, minimal shrinkage |
| **Weldability** | Excellent forge welding (the traditional method) | Good (low C) to poor (high C); arc welding universal | Difficult — requires preheat, special electrodes, or brazing |
| **Machinability** | Poor — gummy, tears easily (slag stringers) | Good to moderate (depends on hardness) | Excellent — graphite acts as chip breaker and lubricant |
| **Corrosion resistance** | Good — slag inclusions interrupt corrosion paths | Moderate — rusts without protection | Good — graphite provides some barrier; alloyed grades very resistant |
| **Vibration damping** | Poor | Poor | Excellent — graphite absorbs vibration |
| **Typical uses** | Decorative ironwork, chains, anchors, historic structures | Structures, machines, tools, fasteners, springs, vehicles, pipes | Machine bases, engine blocks, pipes, cookware, manhole covers |
| **Historical period** | Ancient to ~1860 (replaced by steel for most uses) | 1856-present (Bessemer process onward) | ~1700-present (blast furnace + cupola) |

**Key distinctions**:
- Wrought iron's fibrous slag inclusions give it a wood-like grain structure. It is remarkably resistant to fatigue and corrosion — Victorian wrought iron structures survive after 150+ years with minimal maintenance. However, it cannot be hardened by heat treatment and is labor-intensive to produce (bloomery + extensive forging). Obsolete for structural use but still made in small quantities for restoration and decorative work.
- Steel is the chameleon material — its properties can be tuned across an enormous range by varying carbon content, heat treatment, and alloying. Mild steel (0.15-0.25% C) is ductile and weldable for structures. Medium carbon (0.35-0.50% C) quenched and tempered provides the best balance for machine parts. High carbon (0.70-1.0% C) hardened and tempered gives maximum hardness for tools and springs.
- Cast iron's advantage is economy — it can be poured directly into complex shapes from a cupola furnace at relatively low temperature. Its disadvantages (brittleness, no ductility) limit it to compressive-load applications and situations where vibration damping outweighs strength requirements. Ductile iron (spheroidal graphite — produced by Mg or Ce inoculation of the melt) bridges the gap: 350-700 MPa tensile strength with 2-10% elongation.

### Safety & Hazards

- **Extreme heat and burn risk**: Bloomery furnaces reach 1200-1400°C; extracted blooms glow white-hot at ~1200°C. Forge welding requires heating iron to 1300-1400°C (bright yellow-white). At these temperatures, radiation burns occur within seconds of close proximity. Wear heavy leather apron, gloves, face shield, and closed-toe boots. Use tongs sized to the work — dropping white-hot iron causes severe burns and fires. Maintain a clear, dry floor around the forge (no water puddles — steam explosions from spilled molten slag).
- **Carbon monoxide from charcoal combustion**: Bloomery smelting consumes charcoal at high rates, producing large volumes of carbon monoxide. CO is colorless, odorless, and causes headache, confusion, loss of consciousness, and death. Never operate a bloomery or forge in an enclosed space. Ensure cross-ventilation. If an operator becomes confused or lethargic, move them to fresh air immediately and monitor breathing.
- **Spark and slag spray during bloom consolidation**: Hammering the white-hot bloom ejects slag particles and sparks at temperatures exceeding 1000°C. Eye protection (safety glasses or face shield) is essential for this operation. Long sleeves and leather gloves prevent spark burns on forearms and hands.
- **Lead and zinc fume hazards from soldering and brazing**: Soft solder (60/40 tin-lead alloy) produces lead fumes above 500°C; brass brazing filler (60/40 copper-zinc) produces zinc oxide fumes at ~900°C. Zinc oxide fume causes "metal fume fever" (flu-like symptoms: chills, fever, muscle ache, 4-8 hours after exposure). Lead fume causes cumulative neurological and organ damage. Solder and braze with local exhaust ventilation. Avoid breathing fumes directly. Wash hands after handling solder materials.
- **Quenching hazards**: Plunging hot steel (780-850°C) into water produces violent boiling and steam splash. Oil quenching (used for springs and high-carbon steel to prevent cracking) creates risk of oil ignition — the oil can flash if the workpiece is too hot. Use a deep quench tank, lower the workpiece quickly and completely, and keep a lid nearby to smother oil fires. Do not use oil quenching near open flames.
---

*Part of the [Bootciv Tech Tree](../) • [Metals](./) • [All Domains](../)*
