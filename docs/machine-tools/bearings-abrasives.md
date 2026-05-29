# Bearings, Abrasives & Cutting Tools

> **Node ID**: machine-tools.bearings-abrasives
> **Domain**: [Machine Tools Bootstrap](./index.md)
> **Dependencies**: [`machine-tools.iterative-bootstrap`](iterative-bootstrap.md)
> **Enables**: [`machine-tools.machining`](machining.md)
> **Timeline**: Years 10-25
> **Outputs**: bearings, ball_bearings, abrasives, cutting_tools, taps, dies, hss_tool_bits
> **Critical**: Yes — precision enablers for all machine tool construction

## Overview

Bearings, abrasives, and cutting tools are the precision enablers of machine tool construction. Without bearings, shafts seize and machines destroy themselves from friction. Without abrasives and cutting tools, metal cannot be shaped to the tolerances that make interchangeable parts possible. This capability represents the transition from "rough iron castings" to "precision machines" — the difference between a crude lathe that wobbles and a precision lathe that can turn a true cylinder to ±0.01 mm.

For the machine tool construction sequence, see [Iterative Bootstrap](./iterative-bootstrap.md). For the machining operations that use these tools, see [Machining](./machining.md).

## Abrasives & Grinding Media

### Natural Abrasives (Available Immediately)

Natural abrasives require no industrial infrastructure — they are collected from geological deposits and graded by sieving. They provide the starting point for all precision grinding and polishing.

- **Emery**: Natural aluminum oxide (50-80% Al₂O₃) + iron oxide. Found in Greece, Turkey, and other locations. Grit grades: coarse (24-60), medium (80-120), fine (150-240). For grinding and polishing metals and stone.
- **Pumice**: Volcanic glass, porous and lightweight. Fine polishing of wood, metal, and stone. Available near volcanic regions.
- **Sandstone**: Natural grinding wheels. Dress (shape) with iron dresser. Moderate hardness — adequate for sharpening tools and grinding soft metals.
- **Quartz sand**: Ground to powder, sieved to grade. Lapping and grinding compound. Readily available everywhere.
- **[Jeweler's rouge](../glossary/jewelers-rouge.md)** (iron oxide, Fe₂O₃): Fine polishing compound. Heat steel wool or iron filings in open air until red-hot. Grind resulting oxide to fine powder. Produces mirror-like finish on metals.
- **Tripoli**: Silica-based polishing compound from natural deposits. Fine finish on soft metals (brass, copper, aluminum).
- **Garnet**: Moderate hardness natural abrasive. Used in sandpaper and abrasive blasting. Found in metamorphic rock deposits.

**Strengths**:
- Available without any industrial infrastructure — collected from geological deposits
- Wide geographic availability (quartz sand, sandstone found nearly everywhere)
- Adequate for tool sharpening, light grinding, and polishing tasks

**Weaknesses**:
- Inconsistent hardness and grit distribution compared to synthetic abrasives
- Lower cutting efficiency — natural grains fracture irregularly, producing duller cutting edges
- Limited supply in non-volcanic regions (pumice, emery are geographically restricted)

### Grit Grading System

Sieve abrasive through woven wire screens. Screen mesh number = grit number (60 mesh = 60 grit, particles ~250 μm). Stack sieves coarse to fine, shake, weigh fractions:

| Grit Number | Particle Size (μm) | Use |
|-------------|-------------------|-----|
| 24-40 | 600-1000 | Rough grinding, stock removal |
| 60-80 | 180-250 | General grinding |
| 100-150 | 100-150 | Medium finishing |
| 180-240 | 50-80 | Fine finishing |
| 320-400 | 25-40 | Very fine finish |
| 600-1200 | 5-25 | Lapping, mirror polishing |

**Construction steps for a sieve set**:
1. Obtain woven brass or steel wire mesh in standard sizes: 24, 40, 60, 80, 120, 180, 240, 400, and 600 mesh. Wire diameter tolerance ±0.01 mm.
2. Cut mesh into 200 mm diameter discs. Stretch each disc taut over a wooden frame (25 mm × 25 mm timber, mitered corners, glued and pinned). Secure with copper tacks at 15 mm spacing.
3. Stack frames coarse (24 mesh) on top to fine (600 mesh) on bottom. Align frames so abrasive tumbles through sequentially.
4. Pour crushed abrasive onto top sieve. Shake the stack in a circular motion for 5 minutes at approximately 1 Hz frequency.
5. Weigh the fraction captured on each sieve to determine grit distribution.

**Calibration**: Check mesh integrity monthly by passing a known-weight sample of graded abrasive through. If more than 5% of the sample passes through to the next finer sieve, the mesh has stretched and must be replaced.

**Expected performance**: A 5-sieve stack sorts abrasive into 5 distinct grades with ±15% particle size variation within each grade. A 200 g batch processes in 5 minutes.

**Materials specifications**: Woven brass wire mesh (0.15-0.50 mm wire diameter depending on mesh size), hardwood frame timber (25 × 25 mm), copper tacks (12 mm).

**Strengths**:
- Simple, repeatable grading system using only wire mesh and basic carpentry
- Sieves can be constructed in any workshop with standard materials
- Direct correspondence between mesh number and particle size

**Weaknesses**:
- Sieve mesh wears and stretches over time, requiring periodic replacement
- Fine grades (below 400 mesh) are increasingly difficult to produce by sieving alone — sedimentation becomes necessary
- Irregularly shaped particles pass diagonally, introducing grading errors

### Synthetic Abrasives (Require Electric Arc Furnace)

- **[Silicon carbide (SiC)](../glossary/silicon-carbide-sic.md)** — Acheson process: Silica sand + petroleum coke, heat in electric furnace to 2200-2500°C for 36-48 hours. SiO₂ + 3C → SiC + 2CO. Green to black crystalline mass. Crush, grade. Harder than aluminum oxide (9.5 Mohs), sharp fracture pattern — ideal for grinding glass, stone, cast iron, and non-ferrous metals.
- **[Aluminum oxide (Al₂O₃)](../glossary/aluminum-oxide-alo.md)** — Bauxite fused in electric arc furnace at 2000-2200°C. Cool, crush, grade. Tougher than SiC (less brittle), better for grinding steel and alloys. 9 Mohs.

**Construction steps for synthetic abrasive production** (SiC):
1. Mix silica sand (SiO₂, >98% purity, 0.5-1 mm grain size) with petroleum coke (carbon, >95% fixed carbon) at a 1:3 molar ratio by weight. Add 2-5% sawdust as porosity agent.
2. Load mixture into a rectangular refractory furnace trough (dimensions: 3 m long × 1.5 m wide × 1 m deep, lined with [refractories](../chemistry/refractories.md)).
3. Insert graphite electrodes at each end. Apply 2000-4000 A at 100-200 V for 36-48 hours. Core temperature reaches 2200-2500°C.
4. Allow 24 hours cooling. Break apart the mass. The inner zone (within ~200 mm of core) contains crystalline SiC; the outer zone is partially reacted and is recycled.
5. Crush SiC mass in a jaw crusher, then ball-mill to break down aggregates. Sieve to grade (see Grit Grading System above).

**Calibration**: Test hardness by scratching a piece of window glass (Mohs 5.5). SiC scratches glass easily — if it does not, the batch is under-reacted. Check crystal color: green to black indicates good quality; brown or gray indicates incomplete reaction.

**Expected performance**: A 4-ton batch yields 1.5-2 tons of usable SiC abrasive. Energy consumption: 8,000-12,000 kWh per ton of SiC produced. Grain hardness: 9.5 Mohs (25,000-30,000 N/mm² Knoop).

**Materials specifications**: Silica sand (SiO₂ >98%), petroleum coke (>95% fixed carbon), graphite electrodes (50-100 mm diameter), sawdust (2-5% by weight), refractory furnace lining (alumina or firebrick rated to 2600°C).

**Strengths**:
- SiC is harder than any natural abrasive (9.5 Mohs vs. 7-9 for natural materials)
- Sharp conchoidal fracture produces self-sharpening grain edges
- Consistent quality and grit distribution — batch-processable to tight tolerances

**Weaknesses**:
- Requires electric arc furnace (8,000-12,000 kWh per ton) — major energy infrastructure
- SiC is brittle and fractures too quickly for grinding tough steels — better suited for cast iron and non-ferrous metals
- Production scale: minimum practical batch size is several tons

### Grinding Wheel Construction

**Construction steps for a vitrified grinding wheel**:
1. Weigh abrasive grain (selected grit grade), clay bonding agent (10-20% by weight for medium-grade wheel), and temporary binder (dextrin or sodium silicate, 2-3%). Mix dry for 10 minutes, then add 5-8% water and mix to uniform consistency.
2. Press mixture into a steel mold matching wheel dimensions. Typical: 150 mm OD × 20 mm bore × 25 mm thick for a bench grinder wheel. Apply 15-30 MPa hydraulic pressure. Hold for 30 seconds.
3. Dry the pressed wheel at 80-100°C for 24 hours to remove moisture slowly (fast drying causes cracks).
4. Fire in a kiln at 1200-1300°C for 12-24 hours with a controlled heating rate of 50-100°C/hour to prevent thermal shock. The clay vitrifies, bonding the abrasive grains into a rigid matrix.
5. Cool at 30-50°C/hour to room temperature. Bore the center hole to final tolerance (H7 fit on the arbor, ±0.015 mm for a 20 mm bore).
6. Dress the wheel on a truing device: mount on a balancing arbor, rotate at operating speed, and apply a diamond or hardened steel dresser to the periphery to achieve ±0.02 mm runout.

**Calibration**: Ring test before mounting — suspend the wheel freely on a rod through the bore, tap the periphery 45° from vertical with a non-metallic tool (hardwood dowel, 15 mm diameter). A sound wheel produces a clear, sustained ring (~2-3 seconds). A cracked wheel produces a dull thud with no sustain. Reject any wheel that fails the ring test.

**Expected performance**: Wheel peripheral speed 1500-2100 m/min at rated RPM. Material removal rate: 5-20 mm³/s per mm of wheel width for medium-grade vitrified wheels on mild steel. Wheel wear rate: 0.01-0.05 mm per minute of grinding time. Surface finish: 0.8-3.2 μm Ra with 60-80 grit wheel.

**Materials specifications**: Abrasive grain (Al₂O₃ or SiC, selected grit), clay (kaolin or ball clay, 10-20% by weight), dextrin or sodium silicate binder (2-3%), steel mold (machined to wheel dimensions ±0.1 mm).

**Wheel grade**: Soft-grade wheels release dulled grains easily (for hard materials). Hard-grade wheels hold grains longer (for soft materials). Paradox: use softer wheels for harder workpieces.

**Strengths**:
- Vitrified bond is rigid and porous — allows coolant flow through the wheel and produces precise geometry
- Self-dressing action: as grains dull, they fracture or pull out, exposing sharp new grains
- Long wheel life (weeks to months depending on use) with periodic dressing

**Weaknesses**:
- Vitrified wheels are brittle and can shatter if dropped or subjected to thermal shock
- Wheel speed is a critical safety parameter — exceeding rated speed causes explosive failure
- Requires careful balance — an unbalanced wheel vibrates, degrading surface finish and bearing life

### Lapping and Honing

**Lapping construction steps**:
1. Cast a lapping plate from gray cast iron, 200-300 mm diameter × 20-30 mm thick. Machine the working surface flat to 0.002 mm over the full diameter on a surface grinder. Cut three radial grooves (2 mm wide × 1 mm deep) spaced 120° apart to distribute abrasive slurry.
2. Prepare lapping compound: mix graded abrasive (600-1200 grit, 5-25 μm particle size) with medium-viscosity mineral oil or [vegetable oil](../glossary/vegetable-oil.md) to a paste consistency (approximately 3:1 abrasive to oil by weight).
3. Apply a thin, even layer of compound to the lapping plate surface. Place the workpiece on the plate.
4. Rub the workpiece in a figure-8 pattern, applying firm, even downward pressure (5-15 N for a 50 mm diameter workpiece). Rotate the workpiece 90° every 30-60 seconds to ensure uniform material removal.
5. Clean the workpiece and measure. Material removal rate: 0.001-0.01 mm per hour. Continue lapping until target flatness and finish are achieved.

**Calibration**: Check lapping plate flatness weekly with a precision straightedge and feeler gauges (0.002-0.01 mm set). If the plate shows more than 0.005 mm deviation, recondition by lapping three plates together (plate A laps B, B laps C, C laps A) until all three are flat.

**Expected performance**: Surface flatness: 0.0005 mm (0.5 μm) over 50 mm diameter. Surface finish: 0.025-0.1 μm Ra. Material removal rate: 0.001-0.01 mm/hour depending on abrasive grade and pressure.

**Materials specifications**: Cast iron lapping plate (gray iron, 200-300 mm diameter, flat to 0.002 mm), abrasive compound (Al₂O₃ or SiC, 600-1200 grit), carrier oil (mineral oil or vegetable oil, medium viscosity).

**Honing**: Abrasive stones mounted on an expanding mandrel are rotated and reciprocated inside a cylinder bore. Produces precise diameter, roundness, and cross-hatched surface pattern ideal for oil retention. Used for engine cylinder bores, hydraulic cylinder bores, and gun barrels.

**Strengths**:
- Produces optically flat surfaces — essential for gauge blocks, valve seats, and sealing faces
- Very low material removal rate gives fine control over final dimensions
- No special machinery required for lapping — a flat plate and abrasive paste suffice

**Weaknesses**:
- Extremely slow process (0.001-0.01 mm/hour) — impractical for large amounts of stock removal
- Abrasive particles embed in soft workpiece surfaces, contaminating the finish — thorough cleaning required
- Operator skill is critical — uneven pressure or pattern produces non-flat surfaces

## Thread Standards & Fastener Production

### Thread Profile Standard

Choose ONE system and standardize immediately. Mixing thread standards is catastrophic for interchangeable parts.

- **Metric (ISO)**: 60° thread angle, flat crests and roots. Designated M×pitch (e.g., M8×1.25 = 8 mm major diameter, 1.25 mm pitch). Coarse pitch series is default (M8 coarse = 1.25 mm pitch). Used worldwide.
- **Unified (UNC/UNF)**: 60° thread angle, flat crests, rounded roots. Designated by diameter + TPI (e.g., 5/16-18 UNC = 5/16" diameter, 18 threads per inch, coarse series). Used in North America.
- **CRITICAL**: Pick metric OR unified and commit. All taps, dies, gauges, and screws must match. Mixed inventories cause assembly failures, cross-threading, and loose joints.

**Strengths**:
- Standardization enables interchangeable parts across all machinery
- Metric system simplifies calculation (decimal pitch) and is used worldwide

**Weaknesses**:
- Once committed to a standard, changing is extremely costly (all tooling, fasteners, and gauges must be replaced)
- Thread gauges for each size are required for quality control — significant tooling investment

### Thread Cutting on Lathe

**Construction steps for thread cutting setup**:
1. Mount workpiece in [lathe chuck](../glossary/lathe-chuck.md) (3-jaw self-centering for round stock, ±0.05 mm runout). Face the end and turn a pilot diameter 0.1-0.2 mm below the thread major diameter for the first 3-5 mm of length — this pilot guides the threading tool.
2. Install change gears between spindle and leadscrew for the desired pitch. Gear ratio = (pitch to cut / leadscrew pitch) × (stud gear teeth / lead gear teeth). Example: to cut M8×1.25 with a 4 mm leadscrew, ratio = 1.25/4 × stud/lead = 0.3125. Use a 25-tooth stud gear and 80-tooth lead gear (25/80 = 0.3125).
3. Grind threading tool to 60° included angle with a tool grinding fixture. Tip radius: 0.05-0.15 mm for coarse threads, 0.02-0.05 mm for fine threads. Verify angle with a thread profile gauge (±0.5°).
4. Set compound rest to 29-30° (half the thread angle + 0.5°) so the tool feeds along the leading flank only, reducing cutting force and improving chip flow.

**Calibration**: Cut a test thread in a scrap piece of the same material. Check with a thread micrometer or go/no-go gauge. The go gauge must thread fully into the nut by hand; the no-go gauge must not enter more than 2 turns. Adjust depth ±0.02 mm and retry if the gauge does not pass correctly.

**Expected performance**: Thread accuracy: ±0.05 mm on pitch diameter for manual threading with HSS tool. Surface finish: 1.6-6.3 μm Ra on thread flanks. Production rate: 8-15 passes per thread, 3-5 minutes per thread for M8×1.25 in mild steel.

**Materials specifications**: HSS tool bit (M2 grade, 10 × 10 × 100 mm), change gears (cast iron or steel, matching lathe specification), thread profile gauge (60°, hardened steel), thread micrometer (0-25 mm range, 0.01 mm resolution).

**Strengths**:
- Thread dial indicator allows precise re-engagement on the same groove — no cross-threading risk
- Adjustable depth per pass (0.1-0.2 mm increments) gives full control over thread quality
- Works for any pitch within the leadscrew gear range

**Weaknesses**:
- Slow process — 8-15 passes per thread at 25-50% of normal turning speed
- Requires correct change gear setup for each pitch — wrong gears produce wrong pitch
- Cannot disengage half-nut mid-thread without losing synchronization (except at specific dial positions)

### Tap and Die Production

**Construction steps for a hand tap**:
1. Turn [HSS](../glossary/hardness-retained-to-600c.md) rod to nominal diameter +0.05 mm (e.g., 8.05 mm for M8 tap) on a lathe between centers. Turn the shank to 6.0 mm for a tap wrench fit, with a 1 mm radius shoulder transition.
2. Cut 3-4 longitudinal flutes using a milling cutter on the lathe or milling machine. Flute depth: 2-3 mm for an 8 mm tap. Flute spacing: equal (90° for 4 flutes, 120° for 3 flutes). Flute helix angle: 0° (straight flutes for hand taps).
3. Cut the thread profile between the flutes on the lathe using the thread cutting procedure above. Thread depth: 0.614 × pitch.
4. Grind the chamfer on the cutting end. Taper tap: 7-10 threads chamfered (lead angle ~4°). Plug tap: 3-5 threads chamfered (lead angle ~8°). Bottoming tap: 1-2 threads chamfered (lead angle ~15°).
5. Harden: heat to 1250-1280°C in a salt bath or forge, quench in oil at 40-60°C. Temper at 540-560°C for 2 hours, air cool. Target hardness: 62-65 HRC.
6. Grind the shank to final dimension (6.00 mm ±0.02 mm) on a cylindrical grinder. Square the driving end.

**Calibration**: Thread the tap into a standard go/no-go gauge block. The tap must produce a thread that accepts the go gauge fully and rejects the no-go gauge. Measure thread pitch diameter with a thread micrometer: tolerance ±0.02 mm on pitch diameter.

**Expected performance**: A single hand tap in M8 size produces 50-200 threads in mild steel before resharpening is needed. Thread accuracy: 6H tolerance class (ISO), ±0.03 mm on pitch diameter. Cutting torque: 2-5 Nm for M8 in mild steel with cutting oil.

**Materials specifications**: HSS M2 round stock (8 mm diameter × 80 mm long), cutting oil (sulfurized mineral oil), oil-hardening salt bath (BaCl₂, 1250°C).

**[Taps](../glossary/taps.md)** (cut internal threads): Three-tap set:
- **Taper tap**: 7-10 chamfered threads at the tip — starts easily, used to begin the thread.
- **Plug tap**: 3-5 chamfered threads — general purpose, most commonly used.
- **Bottoming tap**: 1-2 chamfered threads — threads to the bottom of blind holes.

**[Dies](../glossary/dies.md)** (cut external threads): Hardened steel plate with threaded hole and 3-4 cutting edges, split by adjustable slot for controlling cut depth. Die stock holds die and provides leverage for hand turning.

**Thread gauges**: Go/no-go gauges for each thread size. "Go" gauge threads fully into the hole/part. "No-go" gauge does not enter. Essential for quality control.

**Strengths**:
- Three-tap set allows threading through-holes (taper alone) and blind holes (taper → plug → bottoming)
- Hand taps require no machinery — usable with a tap wrench in the field
- Dies produce external threads on rod stock without a lathe

**Weaknesses**:
- Taps are brittle (hardened HSS) and break easily if tilted or forced — a broken tap in a workpiece is extremely difficult to remove
- Thread quality depends on the tap remaining perpendicular to the work surface — requires careful starting technique
- Dies produce less accurate threads than lathe-cut threads due to limited alignment control

### Bolt Making

**Construction steps for a bolt (M8 × 40 mm, grade 8.8)**:
1. Cut [mild steel](../metals/iron-steel.md) rod to 45 mm length (40 mm grip + 5 mm for heading). Diameter: 7.8-8.0 mm (slightly undersized for heading).
2. Heat one end to bright orange (~1000°C) in a forge. Upset (compress) the heated end in a heading tool (hardened steel die with a hexagonal cavity, 13 mm across flats, 5 mm deep). Two to three hammer blows form the hex head.
3. Turn the shank to 8.00 mm ±0.05 mm on a lathe. Face the under-head surface square to the shank (runout <0.05 mm).
4. Cut threads with a die (M8×1.25). Apply sulfurized cutting oil. Turn the die stock clockwise 1/4 turn, then back 1/8 turn to break the chip. Thread length: 25 mm minimum.
5. Heat treat for grade 8.8: austenitize at 820°C for 15 minutes, quench in oil at 40-60°C, temper at 400-500°C for 1 hour. Result: ~800 MPa tensile strength.

**Calibration**: Test tensile strength by threading the bolt into a test fixture and applying load with a hydraulic press. Grade 8.8 bolt must withstand 800 MPa tensile stress (proof load ~580 MPa). Verify thread fit with go/no-go gauge. Measure hardness on the shank: 22-32 HRC after heat treatment.

**Expected performance**: Production rate: 20-50 bolts per hour by hand, 100-200/hour with machine threading. Bolt tensile strength: 800 MPa (grade 8.8). Thread accuracy: 6g tolerance class (ISO).

**Materials specifications**: Medium-carbon steel rod (0.35-0.45% C, 8 mm diameter), heading tool die (hardened steel, hexagonal cavity), M8×1.25 die, sulfurized cutting oil, oil for quenching (40-60°C).

**Strengths**:
- Heading produces a head that is larger in diameter than the shank from the same piece of rod — efficient material use
- Heat-treated bolts achieve 800 MPa tensile strength, suitable for structural applications
- Standardized thread production enables interchangeable fasteners across all machinery

**Weaknesses**:
- Hand-production rate is slow (20-50/hour) — significant labor for large assemblies requiring hundreds of bolts
- Heat treatment adds complexity — poorly controlled tempering produces brittle or soft bolts
- Thread quality depends on die sharpness — worn dies produce torn or oversize threads

## Bearing Design & Production

### Plain (Journal) Bearings

The simplest and most robust bearing type. A cylindrical shaft rotates inside a slightly larger cylindrical housing, separated by a thin film of lubricant.

**Construction steps for a babbitt-lined journal bearing**:
1. Machine the bearing shell from cast iron or steel. Shell bore: shaft diameter + 4-6 mm (to allow for babbitt lining thickness). Shell length: 1.0-1.5 × shaft diameter. Finish the bore surface rough (~1-2 mm Ra) to provide mechanical keying for the babbitt.
2. Prepare the mandrel: turn a steel rod to shaft diameter + radial clearance (0.001-0.002 × shaft diameter; for a 50 mm shaft, mandrel = 50.05-50.10 mm). Coat the mandrel with soot or graphite to prevent babbitt adhesion.
3. Assemble the shell around the mandrel. Seal both ends with clay or putty to contain the molten babbitt. Leave a pouring hole at the top (10-15 mm diameter).
4. Melt babbitt metal (Sn-Sb-Cu alloy, 88/8/4 typical composition) in a crucible to 400-450°C (well above the 240°C liquidus, but below 500°C to avoid oxidation). Skim dross from the surface.
5. Preheat the assembled shell and mandrel to 150-200°C to prevent premature solidification. Pour babbitt through the pouring hole in a steady, continuous stream until it fills the cavity and overflows slightly.
6. Allow to cool to room temperature (30-60 minutes). Disassemble. The babbitt shell now has a precise bore matching the mandrel diameter. Machine oil grooves (2-3 mm wide × 1.5 mm deep) in the babbitt surface in an axial or figure-8 pattern.

**Calibration**: Insert the shaft into the bearing. Measure radial clearance with feeler gauges: target 0.001-0.002 × shaft diameter (50 mm shaft → 0.05-0.10 mm). Spin the shaft by hand — it should rotate freely with no binding but minimal perceptible play. Check axial end float: 0.1-0.3 mm.

**Expected performance**: Allowable bearing pressure: 2-8 MPa for babbitt on steel. Coefficient of friction: 0.01-0.03 (hydrodynamic regime). Speed range: 0-1500 RPM depending on load and lubrication. Operating temperature: up to 100°C with adequate lubrication. Service life: 10,000-50,000 hours with proper lubrication.

**Materials specifications**: Babbitt metal (88% Sn / 8% Sb / 4% Cu), cast iron shell (minimum wall thickness 5 mm), steel mandrel (turned to shaft diameter + clearance, ±0.02 mm), lubricating oil (SAE 30 or equivalent mineral oil).

**Lubrication**: Oil ring (a ring rides on the shaft, dips into oil reservoir below, carries oil up to the bearing surface) or gravity-fed oil cup. Grease-packed for slow-speed bearings.

**Strengths**:
- Simple to manufacture — requires only basic casting and machining capability
- Tolerant of misalignment (the soft babbitt conforms to shaft position over time)
- Embeds contaminants — dirt particles press into the soft babbitt rather than scoring the shaft

**Weaknesses**:
- Higher friction than rolling bearings (~0.01-0.03 coefficient of friction vs. ~0.001 for ball bearings)
- Requires continuous lubrication — oil starvation causes rapid failure (minutes to hours)
- Limited speed capability — above 1500 RPM, friction heat overwhelms cooling capacity

### Rolling Element Bearings (Precision)

Ball and roller bearings reduce friction and enable high-speed machinery (machine tool spindles, engines, generators).

**Construction steps for a ball bearing (6205 type)**:
1. **Inner ring**: Forge bearing steel (52100 grade, 1% C, 1.5% Cr) to ring blank. Turn on lathe to final dimensions: 25.00 mm bore (H5 tolerance, +0.004/0 mm), 31.5 mm OD, 15 mm width. Grind the raceway (the curved track the balls ride on) to a groove radius of 3.97 mm (ball radius + 2-3% for conformity), with 0.05 μm Ra surface finish.
2. **Outer ring**: Forge and turn to 52.00 mm OD (±0.002 mm), 46.5 mm bore with raceway groove, 15 mm width. Grind raceway to same profile and finish as inner ring.
3. **Balls**: Cut 7.94 mm diameter wire into slugs. Cold head into rough spheres in a header. Grind between grooved cast iron plates (the plates have concentric grooves matching the ball radius, and the balls roll between them under load for 2-4 hours). Lap to 1-5 μm sphericity variation using 600-1200 grit abrasive paste. Harden at 820-860°C, oil quench, temper at 150-200°C to 58-62 HRC.
4. **Cage**: Stamp from 0.5 mm brass sheet (or 0.5 mm mild steel sheet). Two halves, each with ball pockets (7 pockets for a 6205 bearing). Rivet halves together through the pillar posts.
5. **Assembly**: Place balls between inner and outer raceways. Compress the cage halves around the balls. Rivet cage halves together. Pack with lithium grease. Install seals or shields (pressed steel, crimped into the outer ring groove).

**Calibration**: Measure bore with a bore gauge: 25.000-25.004 mm (H5 tolerance). Measure OD with a micrometer: 52.000-52.002 mm. Check radial internal clearance with a dial indicator: 0.005-0.015 mm for C2 (tight) clearance, 0.015-0.030 mm for CN (normal) clearance. Spin the bearing by hand — should rotate smoothly with no detectable roughness or clicking.

**Expected performance**: Radial load rating: 14.0 kN (basic static, 6205). Speed rating: 12,000 RPM (grease lubricated) or 15,000 RPM (oil lubricated). Friction coefficient: 0.001-0.002. Service life (L10): 20,000-50,000 hours at rated load and speed. Operating temperature range: -30°C to +120°C with lithium grease.

**Materials specifications**: Bearing steel 52100 (1.0% C, 1.5% Cr, balance Fe) for rings and balls, brass sheet (0.5 mm) or steel sheet (0.5 mm) for cage, lithium grease (NLGI grade 2), NBR rubber or pressed steel for seals.

**Tolerance classes**: ABEC-1 (standard) to ABEC-9 (ultra-precision). Higher classes = tighter tolerances on bore, OD, and runout. Machine tool spindles need ABEC-5 or better.

**Strengths**:
- Very low friction (0.001-0.002 coefficient) — 10× lower than plain bearings
- Precise shaft location — radial clearance of 0.005-0.030 mm
- Pre-sealed, pre-greased units require minimal maintenance

**Weaknesses**:
- Complex manufacturing requiring precision grinding (0.05 μm Ra raceway finish) — beyond bootstrap capability initially
- Sensitive to contamination — even 1-5 μm particles cause raceway damage and premature failure
- Finite fatigue life (L10) — even properly loaded bearings eventually develop subsurface spalling

### Bearing Selection Guide

| Application | Type | Speed | Load | Lubrication |
|-------------|------|-------|------|-------------|
| Line shaft | Plain (babbitt) | Low-medium | Moderate | Oil ring |
| Lathe spindle | Ball bearing (ABEC-5+) | Medium-high | Light-moderate | Grease or oil mist |
| Flywheel | Plain (babbitt) | Low | Heavy | Oil cup |
| Milling spindle | Ball bearing (ABEC-7+) | High | Moderate | Grease |
| Engine crankshaft | Plain (babbitt/insert) | Medium | Heavy | Pressure oil |
| High-speed grinder | Ball bearing or air bearing | Very high | Light | Oil mist |

## Lubrication & Coolants

### Bearing Lubricants

- **Mineral oil**: Refined petroleum oil. Standard lubricant for most bearings. Viscosity grade selected by speed and load (thicker oil for slower speeds and heavier loads).
- **Animal fat (tallow, lard)**: Pre-petroleum lubricant. Works well for plain bearings and slow-speed applications. Lard oil as cutting fluid for turning and threading — reduces friction, improves finish.
- **[Vegetable oil](../glossary/vegetable-oil.md)** (linseed, castor): Cutting fluid for brass and aluminum. Castor oil has excellent film strength for high-speed bearings. Not ideal for steel machining (polymerizes and gums).
- **Grease**: Oil thickened with soap (calcium, lithium, or sodium soap). Stays in place, does not drain away. Used for sealed bearings and slow-speed applications. Lithium grease is the general-purpose standard.

**Strengths**:
- Multiple options available at different technology levels (animal fat at the earliest, mineral oil and synthetic grease later)
- Lubrication dramatically extends bearing life — 10-50× compared to dry running

**Weaknesses**:
- Lubricant contamination (dirt, water, metal particles) degrades performance and accelerates wear
- Some lubricants (vegetable oil, animal fat) have limited shelf life — they oxidize and become acidic

### Cutting Fluids

- **Water with soluble oil**: Best for heavy machining (grinding, milling). 20:1 water-to-emulsifiable-oil ratio. Cools AND lubricates. Primary cutting fluid for production machining.
- **Sulfurized cutting oil**: For heavy turning and gear cutting. Add flowers of sulfur (5-10%) to mineral oil or lard oil. Extreme pressure lubrication — sulfur compounds react with metal surface to prevent welding of chip to tool.
- **Cutting fluid application**: Flood coolant (continuous stream directed at the cutting zone) for production. Manual application (brush or squeeze bottle) for light work. Mist coolant for grinding (air + oil mist).
- See [Lubricants](../chemistry/lubricants.md) for the full production chain.

## Cutting Tool Materials

### Carbon Steel Tool Bits (First Available)

**Construction steps**:
1. Forge or grind high-carbon steel rod (0.8-1.3% C, 10 × 10 × 100 mm blank) to the desired tool geometry: rake angle 5-15° (positive for aluminum/brass), relief angle 6-12°, nose radius 0.5-2 mm for finishing.
2. Harden: heat the cutting end to cherry red (780-820°C, visible color) in a forge or furnace. Quench immediately in water or 10% brine solution (agitate vigorously for uniform cooling).
3. Clean the surface to bright metal with an abrasive stone. Temper by carefully reheating the cutting end to 200-250°C (straw color on the polished surface — use a color chart). Hold at temperature for 30 minutes. Air cool.
4. Grind the final cutting edge geometry on an abrasive wheel (60-80 grit for roughing, 120-180 grit for finishing). Keep the tool cool during grinding — dip in water every 10-15 seconds to prevent drawing the temper.

**Calibration**: Test hardness with a file — a hardened carbon tool bit should resist a standard mill file (the file skids without cutting). Scratch test: the tool should scratch glass (Mohs 5.5+). Check edge sharpness under 10× magnification — the cutting edge should be continuous with no chips or rounded areas larger than 0.02 mm.

**Expected performance**: Hardness: 60-62 HRC after heat treatment. Loses hardness above ~200°C (blue heat) — limited to light cuts and slow speeds. Cutting speed: 5-10 m/min for steel, 15-30 m/min for cast iron and brass. Tool life: 15-30 minutes of cutting time in mild steel at recommended speeds.

**Materials specifications**: High-carbon steel (0.8-1.3% C, 10 × 10 mm bar stock), water or 10% brine for quenching, abrasive wheel (60-180 grit) for grinding.

**Strengths**:
- Available at the earliest stage of machine tool development — requires no alloy elements
- Easy to forge, harden, and re-sharpen with basic forge equipment
- Adequate for roughing and general work at modest speeds

**Weaknesses**:
- Loses hardness above ~200°C (blue heat) — cannot sustain production machining speeds in steel
- Tool life is short (15-30 minutes) compared to HSS or carbide
- Limited cutting speed (5-10 m/min for steel) makes production slow

### High-Speed Steel (HSS)

- **Composition**: Tungsten (18%), chromium (4%), vanadium (1%), carbon (0.7-0.8%) — classic T1 grade. M2 grade (more common): 6% W, 5% Mo, 4% Cr, 2% V, 0.85% C.
- **[Hardness retained to ~600°C](../glossary/hardness-retained-to-600c.md)** — 3-5× faster cutting than carbon steel. The "red hardness" property means HSS tools cut effectively even when glowing dull red.
- **Manufacturing**: Melt alloy in electric furnace, cast into ingots, forge to shape, heat treat (austenitize at 1250-1300°C, quench in oil or salt bath, triple temper at 540-570°C — three tempering cycles of 1-2 hours each to convert retained austenite and relieve stress).
- **Cutting speed**: 20-45 m/min for steel, 40-80 m/min for cast iron, 100-200+ m/min for aluminum.
- **Availability**: Requires tungsten, chromium, and vanadium from mining or chemistry. Not available at the very beginning of the machine tools stage, but becomes the standard once alloy elements are sourced.

**Strengths**:
- Retains cutting hardness to 600°C — 3-5× faster cutting than carbon steel
- Triple temper produces a stable, stress-free microstructure with consistent hardness
- Versatile: can be forged, ground, and resharpened in standard workshop equipment

**Weaknesses**:
- Requires alloying elements (W, Cr, V) from mining — not available at the earliest bootstrap stage
- Triple temper cycle (3 × 1-2 hours at 540-570°C) is time-consuming and requires temperature-controlled furnaces
- Maximum cutting speed in steel is still limited to ~45 m/min — carbide tools are 3-5× faster

### Tool Grinding

Grind tool bits on abrasive wheel to correct geometry:

- **Rake angle**: Positive (5-15°) for aluminum/brass (material shears cleanly). Neutral to negative (-5 to 0°) for steel and heavy cuts (material pushes rather than shears — negative rake provides stronger cutting edge).
- **Relief/clearance angle**: 6-12° below cutting edge. Prevents the tool from rubbing on the workpiece behind the cut. Too much relief weakens the cutting edge.
- **Nose radius**: 0.5-2 mm for finishing (smooth surface, longer tool life). Sharp point for roughing (concentrates force for deeper cuts but leaves rougher finish).
- **Chip breaker**: Small step or groove on the rake face that curls the chip tightly, causing it to break into short segments rather than forming long, dangerous ribbons.

## Precision Metrology for Bearing and Thread Production

- **Micrometer**: Measures external dimensions to 0.01 mm resolution. Essential for checking shaft diameters against bearing bore specifications.
- **Bore gauge / inside micrometer**: Measures internal diameters to 0.01 mm. For checking bearing housing bores.
- **Thread gauge**: Go/no-go plug gauge for internal threads, ring gauge for external threads. Verifies thread is within tolerance.
- **Dial indicator**: Measures runout (eccentricity) to 0.01 mm. For checking shaft straightness and bearing alignment.
- **Surface plate**: Flat granite or cast iron reference surface (flat to 0.002 mm). The foundation of all dimensional measurement.

## Safety & Hazards

- **Abrasives dust inhalation**: Grinding and polishing generates fine dust from both the abrasive and the workpiece. Silica dust from sandstone wheels causes silicosis (lung scarring, irreversible, latency period 10-30 years). Aluminum oxide and silicon carbide dust are respiratory irritants. Wear N95 or better respirators during dry grinding. Wet grinding preferred — eliminates airborne dust and improves surface finish.
- **High-speed machinery**: Grinding wheels and machine tools rotate at high speeds (1000-3000 RPM for grinding, 100-3000 RPM for lathes). Loose clothing, long hair, or jewelry can be caught. Guard all rotating parts. Eye protection mandatory (ANSI Z87.1 rated safety glasses minimum) — grinding wheels can shatter and eject fragments at velocities exceeding 100 m/s.
- **Cutting tool hazards**: Sharp cutting tools (taps, dies, tool bits) cause severe lacerations. Handle with care. Use tool holders, not bare hands, when possible. Cut away from body.
- **Hot metal chips**: Machining metal produces hot, sharp chips (especially steel). Do not handle with bare hands. Clear chips with brush, not hands or compressed air (compressed air blows chips into eyes and skin).
- **Grinding wheel explosions**: A cracked grinding wheel can detonate at operating speed, releasing fragments with kinetic energy equivalent to a bullet. Ring test every wheel before mounting. Never exceed rated speed. Use wheel guards (steel, 1.5-3 mm thick, covering 180° of the wheel periphery). Dress wheels regularly to maintain balance and sharpness.

## Cross-References

- [Machining](./machining.md) — lathe, mill, and grinding operations using these tools
- [Iterative Bootstrap](./iterative-bootstrap.md) — building precision machines from these components
- [Forming](./forming.md) — forging and rolling of bearing steel
- [Lubricants](../chemistry/lubricants.md) — cutting fluid and bearing oil production
- [Advanced Ceramics](../ceramics/advanced-ceramics.md) — ceramic bearings and abrasive grains

### FEPA Abrasive Grading System

The Federation of European Producers of Abrasives (FEPA) defines two standard grit ranges for bonded and coated abrasives. Understanding this system is essential for selecting the correct abrasive for each machining operation.

**Bonded abrasive grains (macrogrits)**: FEPA F-series, F8 through F220. These designate the coarse particles used in grinding wheels and sharpening stones. The grit number corresponds to the mesh size of the sieve through which the particles pass: F60 ≈ 250 μm median particle diameter, F80 ≈ 180 μm, F120 ≈ 125 μm, F150 ≈ 100 μm, F180 ≈ 75 μm, F220 ≈ 63 μm. Coarser grits (F8-F36) remove stock rapidly but leave a rough surface (50-100 μm Ra). Medium grits (F46-F120) balance removal rate and finish (6-25 μm Ra). Fine grits (F150-F220) produce finishing cuts (1.5-6 μm Ra).

**Micrograins (fine grits)**: FEPA F230 through F1200, graded by sedimentation or laser diffraction rather than sieving. F230 ≈ 53 μm, F320 ≈ 29 μm, F400 ≈ 17 μm, F600 ≈ 9 μm, F800 ≈ 6.5 μm, F1200 ≈ 3 μm. These ultra-fine grades are used for lapping compounds, super-finishing stones, and honing sticks. F600-F1200 produce surface finishes below 0.5 μm Ra.

**Mesh-to-micron conversion**: US mesh number ≈ 15,000 / particle diameter in μm (approximate). For example, 60 mesh ≈ 250 μm, 120 mesh ≈ 125 μm, 220 mesh ≈ 63 μm. The conversion is not exact because particles are irregular, not spherical, and each grit grade spans a size distribution rather than a single dimension.

**Grit selection by operation**: Rough grinding cast iron welds: F24-F46. General tool sharpening: F60-F80. Finish grinding tool bits: F100-F150.

### Limitations

- **Precision grinding heat**: Grinding generates intense localized heat (1000-1500°C at the grain-workpiece interface). Without adequate coolant, workpiece surface burns, develops tensile residual stresses, or suffers metallurgical damage (rehardening burns, temper burns).
- **Bearing speed limits**: Ball and roller bearings have maximum speed ratings (dN value = bore diameter × speed). Exceeding limits causes lubricant breakdown, cage failure, and seizure. High-speed applications require special designs (angular contact, hybrid ceramic).
- **Abrasives embedment**: Loose abrasive particles embed in soft workpiece surfaces during lapping and honing, contaminating the surface. Thorough cleaning required between operations and before assembly.
- **Bearing fatigue life**: Rolling element bearings fail by subsurface fatigue (spalling) after a statistical number of stress cycles. Rated life (L10) is the cycles at which 10% of bearings fail. Design life typically 20,000-100,000 hours.
- **Grinding wheel dressing**: Grinding wheels require periodic dressing (truing and sharpening) with diamond tools to restore geometry and expose fresh abrasive grains. Wheel wear limits dimensional consistency in long production runs.
- **Contamination sensitivity**: Bearing performance degrades rapidly with particulate contamination. Even 1-5 μm particles cause surface damage. Clean assembly environments and effective sealing are essential.

### See Also

- [Machining](machining.md) — Pre-grinding machining operations
- [Forming](forming.md) — Forming operations requiring bearing-equipped presses
- [Iterative Bootstrap](./iterative-bootstrap.md) — Precision achievement using abrasives
- [Iron & Steel](../metals/iron-steel.md) — Bearing steel (52100, SUJ2) and abrasive grit materials
- [Machine Tools Overview](./index.md) — Complete machine tools reference

---

*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*
