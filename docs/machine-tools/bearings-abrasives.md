# Bearings, Abrasives & Cutting Tools

> **Node ID**: machine-tools.bearings-abrasives
> **Domain**: Machine Tools Bootstrap
> **Timeline**: Years 10-25
> **Outputs**: bearings, ball_bearings, abrasives, cutting_tools, taps, dies, hss_tool_bits

## Overview

Bearings, abrasives, and cutting tools are the precision enablers of machine tool construction. Without bearings, shafts seize and machines destroy themselves from friction. Without abrasives and cutting tools, metal cannot be shaped to the tolerances that make interchangeable parts possible. This capability represents the transition from "rough iron castings" to "precision machines" — the difference between a crude lathe that wobbles and a precision lathe that can turn a true cylinder to ±0.01 mm.

## Abrasives & Grinding Media

### Natural Abrasives (Available Immediately)

- **Emery**: Natural aluminum oxide (50-80% Al₂O₃) + iron oxide. Found in Greece, Turkey, and other locations. Grit grades: coarse (24-60), medium (80-120), fine (150-240). For grinding and polishing metals and stone.
- **Pumice**: Volcanic glass, porous and lightweight. Fine polishing of wood, metal, and stone. Available near volcanic regions.
- **Sandstone**: Natural grinding wheels. Dress (shape) with iron dresser. Moderate hardness — adequate for sharpening tools and grinding soft metals.
- **Quartz sand**: Ground to powder, sieved to grade. Lapping and grinding compound. Readily available everywhere.
- **[Jeweler's rouge](../glossary/jewelers-rouge.md)** (iron oxide, Fe₂O₃): Fine polishing compound. Heat steel wool or iron filings in open air until red-hot. Grind resulting oxide to fine powder. Produces mirror-like finish on metals.
- **Tripoli**: Silica-based polishing compound from natural deposits. Fine finish on soft metals (brass, copper, aluminum).
- **Garnet**: Moderate hardness natural abrasive. Used in sandpaper and abrasive blasting. Found in metamorphic rock deposits.

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

### Synthetic Abrasives (Require Electric Arc Furnace)

- **[Silicon carbide (SiC)](../glossary/silicon-carbide-sic.md)** — Acheson process: Silica sand + petroleum coke, heat in electric furnace to 2200-2500°C for 36-48 hours. SiO₂ + 3C → SiC + 2CO. Green to black crystalline mass. Crush, grade. Harder than aluminum oxide (9.5 Mohs), sharp fracture pattern — ideal for grinding glass, stone, cast iron, and non-ferrous metals.
- **[Aluminum oxide (Al₂O₃)](../glossary/aluminum-oxide-alo.md)** — Bauxite fused in electric arc furnace at 2000-2200°C. Cool, crush, grade. Tougher than SiC (less brittle), better for grinding steel and alloys. 9 Mohs.

### Grinding Wheel Construction

- **Bonded wheel**: Mix abrasive grains with bonding agent, press into wheel shape, fire (vitrified bond — clay/glass, fired to 1200°C) or cure (resinoid bond — synthetic resin, cured at 150-200°C).
- **Wheel grade**: Soft-grade wheels release dulled grains easily (for hard materials). Hard-grade wheels hold grains longer (for soft materials). Paradox: use softer wheels for harder workpieces.
- **Wheel speed**: Critical safety parameter. Never exceed rated speed. Typical: 1500-2100 m/min peripheral speed. Ring test before mounting (suspend wheel, tap with non-metallic tool — clear ring = sound, dull thud = cracked).

### Lapping and Honing

- **Lapping**: Mix graded abrasive (600-1200 grit, ~5-25 μm) with oil or water into slurry. Place slurry between two flat surfaces (lapping plate = cast iron, flat to 0.002 mm), rub in figure-8 pattern. Removes ~0.001-0.01 mm per hour. Produces optically flat surfaces. Essential for gauge blocks, valve seats, bearing surfaces, and sealing faces.
- **Honing**: Abrasive stones mounted on a expanding mandrel are rotated and reciprocated inside a cylinder bore. Produces precise diameter, roundness, and cross-hatched surface pattern ideal for oil retention. Used for engine cylinder bores, hydraulic cylinder bores, and gun barrels.

## Thread Standards & Fastener Production

### Thread Profile Standard

Choose ONE system and standardize immediately. Mixing thread standards is catastrophic for interchangeable parts.

- **Metric (ISO)**: 60° thread angle, flat crests and roots. Designated M×pitch (e.g., M8×1.25 = 8 mm major diameter, 1.25 mm pitch). Coarse pitch series is default (M8 coarse = 1.25 mm pitch). Used worldwide.
- **Unified (UNC/UNF)**: 60° thread angle, flat crests, rounded roots. Designated by diameter + TPI (e.g., 5/16-18 UNC = 5/16" diameter, 18 threads per inch, coarse series). Used in North America.
- **CRITICAL**: Pick metric OR unified and commit. All taps, dies, gauges, and screws must match. Mixed inventories cause assembly failures, cross-threading, and loose joints.

### Thread Cutting on Lathe

- **Setup**: Mount workpiece in chuck. Install correct change gears between spindle and leadscrew for desired pitch. Gear ratio = (pitch to cut / leadscrew pitch) × (stud gear teeth / lead gear teeth).
- **Procedure**: Engage half-nut on leadscrew. First pass at 0.1-0.2 mm depth. Disengage half-nut at end of cut, return carriage to start. Re-engage on SAME thread (use thread dial indicator). Increase depth 0.1-0.2 mm per pass. Total depth for 60° thread = 0.614 × pitch. Final pass at full depth with light cut for smooth finish.
- **Thread dial indicator**: Marks on the dial correspond to positions where the half-nut can be engaged to track the same thread groove. Prevents "cross-threading" (cutting a new groove instead of deepening the existing one).

### Tap and Die Production

- **[Taps](../glossary/taps.md)** (cut internal threads): Turn HSS rod to diameter, cut 3-4 flutes with milling cutter, thread between flutes on lathe, harden and temper. Three-tap set:
  - **Taper tap**: 7-10 chamfered threads at the tip — starts easily, used to begin the thread.
  - **Plug tap**: 3-5 chamfered threads — general purpose, most commonly used.
  - **Bottoming tap**: 1-2 chamfered threads — threads to the bottom of blind holes.
- **[Dies](../glossary/dies.md)** (cut external threads): Hardened steel plate with threaded hole and 3-4 cutting edges, split by adjustable slot for controlling cut depth. Die stock holds die and provides leverage for hand turning.
- **Thread gauges**: Go/no-go gauges for each thread size. "Go" gauge threads fully into the hole/part. "No-go" gauge does not enter. Essential for quality control.

### Bolt Making

- **Heading**: Heat rod end, upset (compress) in heading tool to form hex or square head. The upset creates a larger-diameter head from the rod stock.
- **Shank turning**: Turn shank to nominal diameter on lathe.
- **Threading**: Cut threads with die (hand or machine).
- **Heat treatment** (for high-strength bolts): Harden at 820°C, quench in oil, temper at 400-500°C. Result: ~800 MPa tensile strength (grade 8.8 bolt equivalent).
- **Production rate**: A skilled bolt-maker can produce 20-50 bolts per hour by hand. Machine threading (lathe or threading machine) increases to 100-200/hour.

## Bearing Design & Production

### Plain (Journal) Bearings

The simplest and most robust bearing type. A cylindrical shaft rotates inside a slightly larger cylindrical housing, separated by a thin film of lubricant.

- **Babbitt lining**: Babbitt metal: Sn-Sb-Cu alloy (88/8/4 typical) — soft, embeds dirt particles, conforms to shaft imperfections. Pour molten babbitt into shell around a mandrel (the mandrel diameter = shaft diameter + clearance).
- **Clearance**: 0.001-0.002 × shaft diameter (50 mm shaft = 0.05-0.10 mm radial clearance). Too tight → friction, heat, seizure. Too loose → vibration, impact loading, noise.
- **Load capacity**: Allowable bearing pressure 2-8 MPa for babbitt on steel. Heavily loaded bearings require larger bearing area or harder bearing materials.
- **Lubrication**: Oil ring (a ring rides on the shaft, dips into oil reservoir below, carries oil up to the bearing surface) or gravity-fed oil cup. Grease-packed for slow-speed bearings.
- **Advantages**: Simple to manufacture, tolerant of misalignment, embeds contaminants, runs quietly. Good for low to moderate speed applications (line shafts, flywheels, pumps).
- **Disadvantages**: Higher friction than rolling bearings (~0.01-0.03 coefficient of friction vs ~0.001 for ball bearings). Requires continuous lubrication. Limited speed capability.

### Rolling Element Bearings (Precision)

Ball and roller bearings dramatically reduce friction and enable high-speed machinery (machine tool spindles, engines, generators):

- **Ball bearing construction**: Inner ring, outer ring (hardened 52100 steel, 1% C, 1.5% Cr), balls, cage (brass or stamped steel). Standard 6200 series (light): e.g., 6205 = 25 mm bore × 52 mm OD × 15 mm width.
- **Ball production**: Cut wire → cold head into rough spheres → grind between grooved ring plates (like rolling balls between two concave plates) → lap to 1-5 μm sphericity variation. Harden 820-860°C, oil quench, temper 150-200°C to 58-62 HRC.
- **Ring production**: Forge from bearing steel → turn on lathe → heat treat (58-62 HRC) → grind raceways on specialized grinder → super-finish to 0.05 μm Ra surface roughness.
- **Assembly**: Press balls into cage between races, rivet cage halves together, pack with grease, install seals/shields.
- **Tolerance classes**: ABEC-1 (standard) to ABEC-9 (ultra-precision). Higher classes = tighter tolerances on bore, OD, and runout. Machine tool spindles need ABEC-5 or better.

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

### Cutting Fluids

- **Water with soluble oil**: Best for heavy machining (grinding, milling). 20:1 water-to-emulsifiable-oil ratio. Cools AND lubricates. Primary cutting fluid for production machining.
- **Sulfurized cutting oil**: For heavy turning and gear cutting. Add flowers of sulfur (5-10%) to mineral oil or lard oil. Extreme pressure lubrication — sulfur compounds react with metal surface to prevent welding of chip to tool.
- **Cutting fluid application**: Flood coolant (continuous stream directed at the cutting zone) for production. Manual application (brush or squeeze bottle) for light work. Mist coolant for grinding (air + oil mist).
- See [Lubricants](../chemistry/lubricants.md) for the full production chain.

## Cutting Tool Materials

### Carbon Steel Tool Bits (First Available)

- **Composition**: 0.8-1.3% carbon steel. Harden by heating to cherry red (780-820°C), quenching in water or brine, tempering at 200-250°C (straw color on polished surface).
- **Hardness**: ~60-62 HRC after heat treatment. Loses hardness above ~200°C (blue heat) — limited to light cuts and slow speeds.
- **Cutting speed**: 5-10 m/min for steel, 15-30 m/min for cast iron and brass.
- **Use**: First cutting tools available. Adequate for roughing and general work at modest speeds. Not suitable for production machining of steel.

### High-Speed Steel (HSS)

- **Composition**: Tungsten (18%), chromium (4%), vanadium (1%), carbon (0.7-0.8%) — classic T1 grade. M2 grade (more common): 6% W, 5% Mo, 4% Cr, 2% V, 0.85% C.
- **[Hardness retained to ~600°C](../glossary/hardness-retained-to-600c.md)** — 3-5x faster cutting than carbon steel. The "red hardness" property means HSS tools cut effectively even when glowing dull red.
- **Manufacturing**: Melt alloy in electric furnace, cast into ingots, forge to shape, heat treat (austenitize at 1250-1300°C, quench in oil or salt bath, triple temper at 540-570°C — three tempering cycles of 1-2 hours each to convert retained austenite and relieve stress).
- **Cutting speed**: 20-45 m/min for steel, 40-80 m/min for cast iron, 100-200+ m/min for aluminum.
- **Availability**: Requires tungsten, chromium, and vanadium from mining or chemistry. Not available at the very beginning of the machine tools stage, but becomes the standard once alloy elements are sourced.

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

- **Abrasives dust inhalation**: Grinding and polishing generates fine dust from both the abrasive and the workpiece. Silica dust from sandstone wheels causes silicosis. Aluminum oxide and silicon carbide dust are respiratory irritants. Wear respirators during dry grinding. Wet grinding preferred — eliminates airborne dust and improves surface finish.
- **High-speed machinery**: Grinding wheels and machine tools rotate at high speeds (1000-3000 RPM for grinding, 100-3000 RPM for lathes). Loose clothing, long hair, or jewelry can be caught. Guard all rotating parts. Eye protection mandatory — grinding wheels can shatter and eject fragments at high velocity.
- **Cutting tool hazards**: Sharp cutting tools (taps, dies, tool bits) cause severe lacerations. Handle with care. Use tool holders, not bare hands, when possible. Cut away from body.
- **Hot metal chips**: Machining metal produces hot, sharp chips (especially steel). Do not handle with bare hands. Clear chips with brush, not hands or compressed air (compressed air blows chips into eyes and skin).
- **Grinding wheel explosions**: A cracked grinding wheel can detonate at operating speed. Ring test every wheel before mounting. Never exceed rated speed. Use wheel guards. Dress wheels regularly to maintain balance and sharpness.

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
- **Contamination sensitivity**: Bearing performance degrades rapidly with particulate contamination. Even 1-5 µm particles cause surface damage. Clean assembly environments and effective sealing are essential.

### See Also

- [Machining](machining.md) — Pre-grinding machining operations
- [Forming](forming.md) — Forming operations requiring bearing-equipped presses
- [Iterative Bootstrap](./iterative-bootstrap.md) — Precision achievement using abrasives
- [Measurement & Gauges](./measurement.md) — Precision measurement for bearing fits
- [Iron & Steel](../metals/iron-steel.md) — Bearing steel (52100, SUJ2) and abrasive grit materials
- [Machine Tools Overview](./index.md) — Complete machine tools reference

---

*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*
