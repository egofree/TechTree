# Sawmilling & Timber Processing

> **Node ID**: foundations.sawmilling
> **Domain**: [Foundations](./index.md)
> **Dependencies**: None
> **Enables**: [`construction.building-materials`](../construction/building-materials.md)
> **Timeline**: Years 5-20
> **Outputs**: dimensional_lumber, planks, beams, sawdust
> **Critical**: No

## Overview

Conversion of raw timber into standardized dimensional lumber through log felling, pit sawing, water-powered sawmilling, steam-powered mills, and seasoning/drying. Produces planks, beams, and dimensional lumber for construction, shipbuilding, and papermaking. Sawdust as byproduct for fuel, composite board, and chemical feedstock.

The sawmill is one of the highest-return investments in a growing settlement. Converting logs to dimensional lumber with a saw rather than splitting or hewing reduces waste by 30-50% and produces far more usable board feet per tree. A water-powered sash saw produces in one day what two pit sawyers produce in a week. The transition from manual pit sawing to water-powered milling marks the shift from subsistence construction to systematic building.

Sawmilling also produces sawdust as a byproduct in substantial volume — a single water-powered mill generates tonnes of sawdust per year. This sawdust serves as fuel for kilns and boilers, feedstock for charcoal production, and raw material for composite board manufacturing, making the sawmill a node that connects forestry to both construction and chemical industries.

**How a saw cuts wood**: A saw blade works by a row of teeth, each acting as a tiny chisel. Rip saw teeth (filed straight across at 90°) act like chisels, scooping out fiber bundles along the grain. Crosscut saw teeth (filed at 15-20° bevel) act like knives, severing fibers on each side of the kerf, then the intermediate fiber breaks out. The kerf (width of the cut) is always wider than the blade body because the teeth are "set" — alternately bent outward by 0.2-0.4 mm per side. This clearance prevents the blade from binding in the cut. A thinner kerf means more lumber recovered from each log, but also a less rigid blade that is more prone to wandering.

## Prerequisites

### Materials

- **Logs** — freshly felled timber, sorted by species and diameter. Hardwoods for structural and furniture stock; softwoods for framing lumber. Log length typically 2-6 meters depending on available handling equipment.
- **Saw blades and files** — blades for sharpening and replacement. Iron or steel saw blades, files for tooth sharpening. Blade maintenance consumes a steady supply of files and replacement blades.
- **Stickers** — thin, dry wooden strips (typically 20×25 mm) placed between layers of stacked lumber to allow air circulation during drying. Must be uniform thickness and aligned vertically in the stack.
- **Lubricant** — water or tallow applied to the saw blade during cutting to reduce friction and heat buildup.

### Equipment

- **Saw blade**: Crosscut hand saw, rip saw, or frame saw blade. Pit saw for manual operation. Circular saw blade for powered mills.
  - **Pit saw blade**: 1.2-2.0 meters long, 100-150 mm wide at the middle, tapering to 75-100 mm at the ends. Teeth filed for rip cutting (straight across), 3-4 TPI. Blade thickness 1.5-2.0 mm, kerf 3-4 mm. Two handles: a removable handle (till) at the top for the top sawyer, and a fixed box handle at the bottom for the pitman. Iron or low-carbon steel; high-carbon steel holds an edge longer but is harder to file.
  - **Sash saw (frame saw) blade**: 1.0-1.5 meters long, 75-120 mm wide, 1.0-1.5 mm thick. Tensioned in a wooden frame with wooden wedges or screw adjustment. Kerf 2-3 mm. Teeth 4-6 TPI, filed for rip cutting. Blade tension is critical: too loose and the blade snakes in the cut, too tight and the blade or frame may crack. A rule of thumb for frame saw tension: pluck the blade like a guitar string — it should produce a clear, medium-pitched tone, not a dull thud.
  - **Circular saw blade**: 500-1200 mm diameter for primary breakdown (head saw), 300-400 mm for resawing and edging. Blade thickness 2-4 mm (thinner for resaws, thicker for head saws). 30-60 teeth depending on diameter and intended cut. Tooth speed at the rim: 40-60 m/second for ripping hardwoods, 50-70 m/second for softwoods. RPM calculated from blade diameter: a 600 mm blade at 3000 RPM gives a rim speed of 94 m/s — too fast for most hardwoods and will burn the cut. Target 1500-2000 RPM for a 600 mm blade (47-63 m/s). Blade must be "tensioned" (hammered or rolled) by a saw doctor to run true at operating speed — centrifugal force causes a flat-ground blade to flutter.
- **Log handling**: Peavey or cant hook (rolling logs), log dogs (securing logs to carriage), chains or rope for dragging. A cant hook uses a hinged hook on a long handle (1.2-1.5 m) to grip and roll logs; a peavey adds a spike point for leverage.
- **Measuring and marking**: Log scale stick (estimates board feet in a log), tape measure, lumber rule with nominal dimensions marked.
- **Seasoning infrastructure**: Stickered stacking area (covered, ventilated) for air drying; or a kiln chamber with heat source and circulation fans for accelerated drying.
- [Building Materials & Methods](../construction/building-materials.md) — material dependency

### Knowledge

- Understanding of wood grain direction and how it affects cutting resistance and board quality
- Familiarity with log scaling (estimating board feet from log diameter and length) and lumber grading rules
- Ability to sharpen saw teeth — filing set (bending alternate teeth outward) and jointing (making all teeth the same height)
- Safety training for saw operation, log handling, and steam boiler operation (if applicable)
- Understanding of wood moisture behavior and seasoning principles — equilibrium moisture content, drying defects, and stacking methods

### Log Scaling (Estimating Lumber Yield)

Log scaling estimates the board feet of usable lumber in a log before sawing. Three common scales are used in North America:

**Doyle Scale** (underestimates small logs, widely used for hardwoods):
- Board feet = (D - 4)² × L / 16, where D = small-end diameter inside bark (inches), L = log length (feet)
- A 30 cm (12 inch) diameter, 3 m (10 ft) log: (12-4)² × 10 / 16 = 40 board feet
- Doyle penalizes small logs heavily — a 25 cm (10 inch) log scales to only 22 bf despite actually containing 35-40 bf. This makes Doyle unfavorable for the seller but conservative for the buyer.

**Scribner Scale** (more accurate, common in softwood regions):
- Uses a diagram-based method; approximately: BF ≈ (0.0494 × D² × L) - (0.212 × D × L) - (0.622 × L)
- A 30 cm, 3 m log scales to approximately 54 board feet

**International ¼-Inch Scale** (most accurate, accounts for kerf and taper):
- Board feet per 4-foot section = 0.22 × D² - 0.71 × D
- A 30 cm, 3 m log scales to approximately 60 board feet
- This scale assumes a ¼-inch (6.35 mm) kerf and ½-inch taper per 4-foot section

| Log Diameter (small end) | Doyle (bf per 3m log) | Scribner (bf per 3m log) | International ¼" (bf per 3m log) |
|--------------------------|----------------------|-------------------------|----------------------------------|
| 20 cm (8 in) | 12 | 20 | 25 |
| 25 cm (10 in) | 22 | 36 | 40 |
| 30 cm (12 in) | 40 | 54 | 60 |
| 35 cm (14 in) | 63 | 76 | 85 |
| 40 cm (16 in) | 90 | 104 | 115 |
| 50 cm (20 in) | 160 | 165 | 180 |
| 60 cm (24 in) | 250 | 234 | 260 |

Actual recovery runs 85-110% of scale depending on log quality, sawyer skill, and saw accuracy. Straight logs with minimal taper and few knots yield above scale; crooked, knotty logs yield below.

### Infrastructure

- **Mill site**: Level ground adjacent to the water source (for water power) or with space for boiler and fuel storage (for steam). Access road for log delivery and lumber shipment.
- **Log storage area**: Open yard for staging logs before sawing. Keep logs elevated on cross-bunks to prevent ground contact and rot. Process logs within weeks of felling in warm weather to prevent stain and insect attack.
- **Sawmill structure**: Covered building housing the saw mechanism, log carriage, and controls. Must be rigid enough that the saw frame does not vibrate excessively — vibration produces wavy cuts.
- **Drying yard or kiln**: Covered, ventilated area for stickered lumber stacks. Level concrete, stone, or treated timber foundation. For kiln drying: an insulated chamber with heat source and air circulation.
- **Waste handling**: Sawdust collection and removal system — conveyor, cart, or manual sweep. Sawdust is flammable and must be removed daily. Offcut and edging pile for re-processing or fuel.

## Process Description

Sawmilling converts felled logs into standardized dimensional lumber through a sequence of debarking, primary breakdown (ripping the log into slabs and cant), secondary breakdown (edging and trimming to final dimensions), and seasoning. The process efficiency depends on log quality, saw accuracy, and the kerf (width of cut) — thinner kerfs waste less wood to sawdust but require more precise saw setting.

**Why debarking matters before sawing**: Bark carries grit — soil particles, sand, and small stones embedded during the tree's growth and from skidding logs on the ground. This grit dulls saw teeth at 5-10× the rate of clean wood. A single saw pass through a muddy log can cost 20-30 minutes of re-filing. Bark also prevents the sawyer from seeing surface defects that indicate internal problems (rot, mineral streak, insect damage). Debarking adds 15-30 minutes per log but saves hours of blade maintenance.

**Why kerf width determines profitability**: A circular saw with a 5 mm kerf produces approximately 15% more sawdust (waste) than a band saw with a 2 mm kerf. On a 30 cm diameter log yielding ~60 board feet, the circular saw loses roughly 9 board feet to kerf, while the band saw loses only about 3.5 board feet. At scale, this difference is substantial: a mill processing 10,000 board feet per day loses 1,500 bf to circular saw kerf vs. 580 bf with a band saw — a difference of 920 bf of recoverable lumber per day.

### Step-by-Step Procedure

1. Select and fell timber appropriate to the intended product. Assess grain, knots, and defects. Hardwood logs (oak, ash, maple) produce structural beams and furniture stock; softwood logs (pine, fir, spruce) produce framing lumber.
2. Transport logs to the processing area. Remove bark with a drawknife or spud (bark spud: a broad, dull blade for prying bark from the log). Sort by diameter and quality. Bark removal prevents grit from dulling saw teeth.
3. Cut timber to specified dimensions using the appropriate method:
   - **Pit sawing**: One sawyer stands above the log on a scaffold; a second stands below in a pit. The top sawyer guides the cut; the bottom sawyer pulls the saw down. Feed rate: 15-25 strokes per minute, each stroke removing 1-2 mm of wood. A 30 cm diameter log takes 2-3 hours to rip into 25 mm boards. Output: ~100-200 board feet per day with two skilled workers. The earliest mechanized method for producing boards wider than hand-splitting allows.
   - **Water-powered sash saw**: A water wheel drives a reciprocating frame saw up and down through the log, which is fed forward on a carriage. The sash makes 100-200 strokes per minute. Feed rate adjustable via the ratchet mechanism on the carriage: 1-3 mm per stroke. Water wheel diameter 3-5 meters, generating 3-15 kW depending on flow rate and head. A 3-meter head with 200 liters/second flow delivers roughly 5.9 kW (8 hp) — enough for a single frame saw. Output: 500-2,000 board feet per day depending on water flow. Requires a permanent installation with a millrace or dam.
   - **Circular saw (steam-powered)**: A rotating disc saw cuts continuously in one direction, producing much faster throughput than reciprocating saws. Blade diameter 500-1200 mm for primary breakdown. Feed rate: 10-30 meters per minute for softwoods, 5-15 m/min for hardwoods. A 15 hp (11 kW) steam engine drives the head saw with power to spare for the log carriage feed mechanism. Output: 2,000-10,000 board feet per day. Requires steam engine and boiler infrastructure.
4. Season the cut lumber — air dry or kiln dry to target moisture content. Air drying: stack stickered lumber in a covered, ventilated area for 6-12 months (softwood) or 1-3 years (hardwood). Kiln drying: accelerated using heated air circulation, reducing drying time to days or weeks but requiring fuel and a kiln chamber.
5. Surface and finish as required — plane surfaces flat, rip to final width, crosscut to final length. Grade each piece for structural quality.
6. Inspect for defects, dimensions, and moisture content before storage or use.

### Why Seasoning Works

Fresh-cut wood contains two types of water: free water in the hollow cell cavities, and bound water in the cell walls. Free water evaporates first and accounts for most of the weight difference between green and seasoned wood. Removing free water does not cause shrinkage. The cell walls themselves are still saturated.

At the fiber saturation point (~30% moisture content), all free water is gone and the cell walls begin to dry. This is where shrinkage starts. As bound water molecules leave the cellulose structure, the cell walls contract. Because wood cells are long tubes, the walls contract more in diameter than in length — which is why tangential shrinkage (5-10%) exceeds radial shrinkage (2-5%) and longitudinal shrinkage is negligible (~0.1%). A board that dries from 30% to 8% MC may shrink 4% in width if flat-sawn, or 2% if quarter-sawn.

Drying too fast causes surface checking (cracks) because the surface dries and shrinks while the interior is still wet and swollen. The resulting stress tears the surface fibers apart. Drying too slowly invites fungal staining (blue stain in pine, brown rot in oak) because fungi thrive between 20-30% MC and 20-35°C. The target drying rate balances these risks: fast enough to clear the fungal danger zone within weeks, slow enough to prevent surface rupture.

### Saw Types and Selection

| Saw Type | Power Source | Throughput | Kerf Width | Infrastructure |
|----------|-------------|------------|------------|----------------|
| Pit saw (whip saw) | Two workers | 100-200 bf/day | 3-4 mm | Minimal — scaffold |
| Sash saw (frame saw) | Water wheel | 500-2,000 bf/day | 2-3 mm | Millrace, dam, frame |
| Circular saw | Steam or water | 2,000-10,000 bf/day | 4-6 mm | Engine, boiler, fuel |

### Seasoning and Drying

Freshly sawn lumber (green) contains moisture content from 30% to over 100% depending on species. Green lumber shrinks, warps, and may decay if used without drying. Two approaches:

- **Air drying**: Stack lumber with stickers between each layer in a covered, open-sided shed. Softwoods reach 15-20% moisture in 6-12 months; hardwoods take 1-3 years. Air drying costs nothing but time and space. Protect from rain (top cover) and direct sun (causes checking on exposed faces). Stack on a level foundation to prevent the stack from leaning and boards from warping under their own weight.
- **Kiln drying**: Enclose stacked lumber in a heated chamber with forced air circulation. Fuel sources: wood waste (sawdust, offcuts), coal, or steam from a boiler. Kiln drying reduces moisture content to 6-8% in days to weeks. Faster than air drying but requires fuel and monitoring. Overly rapid drying causes surface checking and honeycombing (internal checking). Monitor with sample boards weighed periodically to track moisture loss rate.

**Why sticker alignment matters**: Stickers transfer the weight of upper boards to lower boards. If stickers are not aligned vertically (each sticker directly above the one below), the weight creates bending stress on the boards between misaligned stickers, causing permanent warp. Stickers that are not uniform thickness (varying more than 0.5 mm) produce the same problem. Use dry, straight-grained sticks — green stickers shrink and distort the stack as they dry.

### Kiln Drying Schedules (Temperature by Moisture Content Stage)

| Stage | White Pine (MC Range) | White Oak (MC Range) | Temperature | Relative Humidity |
|-------|----------------------|---------------------|-------------|------------------|
| Initial (above 30%) | >30% | >30% | 50-55°C | 80-85% |
| Intermediate | 30-20% | 30-20% | 60-65°C | 65-75% |
| Final | 20-10% | 20-15% | 70-75°C | 45-55% |
| Equalizing | 10-8% | 15-10% | 75-80°C | 30-40% |
| Conditioning | 8-6% | 10-8% | 80°C | 65-70% (briefly re-moisturize to relieve case hardening) |

Oak dries at roughly half the rate of pine. Rushing oak through a pine schedule causes honeycombing — internal cracks invisible from the surface that render the lumber structurally useless. The conditioning step at the end is essential: kiln drying creates a moisture gradient (drier surface, wetter core). Raising humidity briefly allows the surface to re-absorb a small amount of moisture, equalizing internal stress. Without conditioning, the boards may develop case hardening: the dry surface layer is in tension, and resawing the board causes it to warp immediately as the internal stresses release.

Target moisture content varies by end use: 15-19% for outdoor construction (fences, barns), 12-15% for house framing, 8-12% for interior finish work and furniture. Using lumber above these targets in enclosed spaces leads to shrinkage gaps, joint opening, and warping as the wood equilibrates to indoor conditions.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Green moisture content | 30-100% | Varies by species; softwoods generally lower. Fresh oak: 60-80%; fresh pine: 40-60%; fresh balsa: up to 200% |
| Fiber saturation point | ~30% MC | Below this, wood shrinks; above, dimensional stability. This is the critical threshold |
| Target MC (construction) | 12-19% | Higher range for outdoor use (fences, barns), lower for enclosed structures |
| Target MC (finish/furniture) | 8-12% | Lower for stability and joint integrity. Must match indoor equilibrium conditions |
| Air drying time (softwood) | 6-12 months | Climate dependent — faster in dry, warm conditions. One year per 25 mm of thickness is a rough rule for hardwoods |
| Air drying time (hardwood) | 1-3 years | Oak and similar dense species dry slowly. A 50 mm thick oak board needs 2+ years to air-dry to 12% |
| Kiln drying time | 1-4 weeks | Softwoods: 7-14 days; hardwoods: 14-28 days. Depends on thickness and species |
| Kiln temperature (initial) | 50-55°C | Must start cool to avoid surface checking on green lumber |
| Kiln temperature (final) | 75-80°C | Safe maximum for most species. Higher temps cause darkening and strength loss |
| Pit saw feed rate | 15-25 strokes/min | Each stroke removes 1-2 mm of wood in softwood |
| Sash saw stroke rate | 100-200 strokes/min | 1-3 mm feed per stroke; water wheel dependent |
| Circular saw rim speed | 40-60 m/s (hardwood) | 50-70 m/s for softwoods. Calculated: π × D × RPM / 60 |
| Circular saw feed rate | 5-30 m/min | Hardwood: 5-15 m/min; softwood: 15-30 m/min |
| Band saw blade tension | 100-200 N/mm² | Depends on blade width and thickness. A 50 mm wide, 0.8 mm thick blade needs roughly 40-80 kg of tension |
| Kerf width (pit saw) | 3-4 mm | Thickest kerf; lowest yield |
| Kerf width (sash saw) | 2-3 mm | Moderate kerf; good yield |
| Kerf width (circular saw) | 4-6 mm | Thinnest practical circular saw blades waste more than band saws |
| Kerf width (band saw) | 1.5-2.5 mm | Thinnest kerf; highest yield. Requires precise blade tracking and guides |
| Lumber recovery factor | 40-65% | Percentage of log volume recovered as usable lumber. Depends on log quality, saw method, and kerf |

## Safety Considerations

This process involves specific hazards requiring trained personnel and protective measures:

- **Saw blade contact injuries**: A circular saw blade spinning at 1500 RPM with a 600 mm diameter has teeth traveling at 47 m/s (170 km/h). Contact with the blade causes immediate, deep amputation injuries. Never reach across a running saw blade. Use a push stick for narrow cuts. The blade guard must cover the portion of the blade above the table at all times. In the seconds between contact and a worker's ability to react, the blade has already completed multiple revolutions — the injury happens faster than human reflexes can respond.
- **Kickback from pinched cuts**: A board pinched between the blade and fence can be thrown violently rearward. A 2-meter board thrown by a circular saw kickback can strike with enough force to break bones or cause fatal head injuries. Use a splitter or riving knife behind the blade to prevent the cut from closing on the blade. Never release a board until it fully clears the blade. Stand to the side of the blade, not directly behind the workpiece.
- **Crush injuries from rolling logs**: A green oak log 40 cm diameter and 3 meters long weighs roughly 180-220 kg. A log rolling off a pile or carriage can pin a worker against the ground or a wall, causing crush injuries to the chest and pelvis. Secure logs on the carriage with dogs before cutting. Never stand in the path of a rolling log. Two workers should handle any log over 30 cm diameter.
- **Hearing damage**: A circular saw operating under load produces 100-110 dB at the operator's position. At 105 dB, permanent hearing damage begins after approximately 1 hour of exposure without protection. A full shift (8 hours) at this level without hearing protection causes measurable permanent threshold shift. Hearing protection rated NRR 25+ is mandatory within 10 meters of an operating sawmill.
- **Sawdust explosion hazard**: Sawdust suspended in air at concentrations above 40-50 g/m³ forms an explosive mixture. A spark from a metal contact (nail embedded in a log hitting the saw teeth), an overheated bearing, or static discharge can trigger a primary explosion. The pressure wave from a primary explosion disturbs settled dust on beams and ledges, creating a larger secondary explosion that can destroy the building. Keep dust accumulation below 3 mm on any surface. Install explosion vents in enclosed dust collection systems. Ground all metal ductwork to prevent static buildup.
- **Sawdust inhalation**: Softwood dust causes respiratory irritation; hardwood dust (oak, beech) is classified as a Group 1 carcinogen by IARC, causing sino-nasal adenocarcinoma with prolonged exposure. Workers in dusty mills without respiratory protection show elevated cancer rates after 10+ years of exposure. Use local dust extraction at the saw, and wear a P2 (N95) or better respirator when dust cannot be controlled by ventilation.
- **Steam boiler hazards** (steam-powered mills only): Boiler explosion from low water level or overpressure can level a mill building. A boiler at 6 bar gauge pressure holds enough stored energy to project fragments hundreds of meters. Water level must be visible in the gauge glass at all times. Safety valves must be tested weekly. The fireman must never leave the boiler unattended while under pressure. See [Energy → Steam Power](../energy/steam-power.md) for full boiler safety procedures.
- **Hypothermia in the pit** (pit sawing): The pit sawyer works below ground level, often in damp, cold conditions. In winter, hypothermia risk is significant after 2-3 hours of sedentary work. The pitman should rotate out of the pit every 60-90 minutes in cold weather.

### Personal Protective Equipment

- Safety glasses or face shield — mandatory near any operating saw
- Leather gloves for log handling (remove for proximity to moving blades)
- Hearing protection — required for circular saw and steam engine operations
- Steel-toe boots with metatarsal guard for log and beam handling
- Hard hat when working around log stacks and overhead rigging

### Emergency Procedures

- Maintain first aid kit with tourniquet, wound compression bandages, and splint — saw injuries can cause severe bleeding.
- Know locations of emergency shutoffs for the saw drive mechanism, steam supply, and water flow.
- Establish evacuation routes and assembly points. Ensure all workers know the path away from the saw blade and any steam equipment.
- Train all personnel on fire suppression — sawdust, offcuts, and drying lumber are all combustible. Keep sand buckets and water accessible. A sawmill fire spreads extremely fast through airborne sawdust.
- Never work alone at a sawmill. A second person must be present to shut down equipment and render aid in case of injury.

## Quality Control

### Acceptance Criteria

- **Dimensional Lumber**: Width and thickness within ±2 mm of nominal dimensions at the time of measurement. Length within +25 mm of specified. No wane (bark edge) exceeding 10% of the face width.
- **Planks**: Surface planed flat with no warp exceeding 3 mm per meter of length. Moisture content at or below the specified seasoning target (typically 12-19% for construction, 8-12% for furniture).
- **Beams**: Structural members must be free of through-checks, heart shake, and decay. Maximum knot size: one-third of the face width. Slope of grain not exceeding 1:10 for structural grades.
- **Sawdust**: Collected clean, free of bark and debris. Suitable for use as fuel, compost, or feedstock for composite board production.

### Testing Methods

- **Dimensional measurement**: Tape measure for length, calipers or framing square for width and thickness. Measure at three points along each dimension — both ends and the middle — to detect taper, bow, and twist.
- **Moisture content**: Use the oven-dry method (weigh sample, dry at 105°C to constant weight, re-weigh) or a moisture meter (electrical resistance type, calibrated for the species being tested). Moisture content = (wet - dry) / dry × 100%.
- **Straightness and square**: Pull a taut string line along the face and edge to detect bow and crook. Check edges with a framing square for twist. Place on a flat reference surface to detect cupping.
- **Visual grading**: Inspect for knots (size, type, location), checks, shakes, pitch pockets, and evidence of insect damage or fungal decay. Grade each piece per established grading rules.

### Sampling Protocol

- Inspect the first board from each log for dimensional accuracy and surface quality. Adjust saw guides if dimensions deviate from target.
- Measure moisture content from sample boards in each drying batch. Select samples from the top, middle, and bottom of the stack — the middle dries slowest.
- Record all measurements for trend analysis. Track saw blade wear by monitoring kerf width and surface quality over time.
- Reject and investigate any out-of-specification results. Common causes: blade wear, guide misalignment, log shifting on carriage, or moisture gradient in drying stack.
- Grade each piece of lumber per established grading rules. Stamp or mark the grade on each piece. Lower grades find use in non-structural applications; only the highest grades go to structural or furniture use.

## Scaling Notes

Transitioning from bench-scale to production involves these considerations:

- **Bench scale (pit saw)**: Two workers, hand tools. Produces boards from felled logs on-site. No fixed infrastructure required. Suitable for initial settlement construction when timber must be processed at the felling location.
- **Pilot scale (water-powered sash saw)**: Permanent mill installation with water wheel, frame saw, and log carriage. Requires a reliable water source with adequate flow and head. Processes 500-2,000 board feet per day. Serves a local community.
- **Production scale (steam-powered circular saw)**: Steam boiler, engine, and one or more circular saws. Location independent (no water course required). Multiple saws for different operations: head saw (primary breakdown), resaw (splitting thicker stock), edger (trimming wane), trimmer (cutting to length). Produces standardized dimensional lumber in volume.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Uneven board thickness | Saw not properly tensioned or guide misaligned | Check saw guide alignment with a straightedge; adjust blade tension (frame saw: tighten wedges until blade rings when plucked; circular saw: have saw doctor check tensioning marks); verify carriage runs true on its rails |
| Excessive sawdust (low yield) | Thick kerf or poor sawing pattern | Use thinner-kerf saw (band saw at 1.5-2 mm saves 10-15% vs. circular saw at 5-6 mm); plan cuts to maximize board recovery from each log; saw the largest boards first, then re-saw the cant |
| Boards warp during seasoning | Stacked without stickers or drying too fast | Restack with proper sticker spacing (every 600 mm, aligned vertically); protect from direct sun and wind; for air drying, maintain 50-60% roof coverage with open sides for airflow |
| Saw blade dulls rapidly | Bark or embedded grit in logs | Remove all bark before sawing; wash logs if muddy; avoid sawing near ground contact. A circular saw blade cutting clean wood should last 4-8 hours between filings |
| Log jams on carriage | Inconsistent feed rate or log not secured | Maintain steady feed; use dogs (log hooks) to secure log firmly to carriage. Check carriage track for debris and lubrication |
| Wavy cut (snaking) | Blade flutter or insufficient guide pressure | Tighten blade guides (reduce gap to 1-2 mm from blade); reduce feed rate by 25-50%; check blade tension — a loose blade in a frame saw produces snaking proportional to the looseness |
| Blue stain on pine lumber | Stain fungi colonizing during slow air drying | Stack pine lumber within 48 hours of sawing; ensure good air circulation (6 m/min minimum through the stack); dip lumber in a borax solution (1-2% sodium borate by weight in water) before stacking to inhibit fungal growth |
| End-checking in hardwood | Ends dry much faster than the middle | Seal log ends with wax, paint, or thick polyethylene wrap immediately after cross-cutting. End-grain loses moisture 10-15× faster than face-grain because the open tube ends wick moisture out directly |
| Blade overheating (discoloration) | Feed rate too high or blade dull | Reduce feed rate; check blade sharpness. A blued (discolored) blade has lost its temper and must be re-tempered or replaced — the blued area is softer and will dull rapidly |
| Boards stick together in stack | Stickers missing or too thin at that layer | Re-stack with uniform stickers (20×25 mm minimum) at 600 mm spacing, aligned vertically. Boards in contact dry unevenly and develop localized staining and warp |
| Circular saw howling or vibrating | Blade out of balance or damaged tooth | Inspect blade for missing or bent teeth; have a saw doctor check balance. A blade with one missing tooth creates imbalanced centrifugal force that produces visible vibration and audible howling at operating RPM |
| Lumber dimensions drift during run | Saw guide loosening or blade wearing | Tighten guide locks; measure output every 10th board; re-file or replace blade when dimensions drift more than ±1 mm from target |

## Variations and Alternatives

- **Pit sawing (manual)**: Lowest technology threshold. Two workers, a scaffold, and a long two-handled saw. Produces boards without any fixed infrastructure. The baseline method for initial settlement construction.
  - **Why pit sawing is limited**: Each stroke of the pit saw removes only 1-2 mm of wood. A 3-meter long cut through a 30 cm log requires 150-300 strokes. At 15-25 strokes per minute, that is 6-20 minutes per board, not including setup, turning the log, and rest breaks. Two skilled pit sawyers produce 100-200 board feet per day — enough for a small shed, but not for a settlement.
- **Water-powered sash saw**: Moderate infrastructure (millrace, dam, water wheel, frame). Runs when water flows — seasonal limitation in cold climates where water freezes. Produces consistent boards at modest throughput.
  - **Why water power changes everything**: A water wheel converts the potential energy of flowing water into continuous reciprocating motion. The saw never tires. It makes 100-200 strokes per minute, each removing 1-3 mm — 5-10× the rate of manual pit sawing. The water wheel runs as long as the river flows, which in temperate climates means 8-12 months per year. The limiting factor becomes log supply and sawyer skill, not physical stamina.
- **Steam-powered circular saw**: Requires boiler, engine, and fuel supply. Not dependent on water flow or weather. Higher throughput but demands more maintenance and a reliable fuel supply (wood waste from the mill itself can supply part of the fuel demand — a mill producing 5000 bf/day generates roughly 2-3 tonnes of sawdust and offcuts, with a heating value of 15-18 MJ/kg when dry).
  - **Why circular saws are faster than sash saws**: A sash saw wastes half its cycle — the blade only cuts on the downstroke, and the upstroke is empty travel. A circular saw cuts continuously in one direction, so the cutting time per board is roughly halved. Combined with higher rim speed (50+ m/s for circular vs. 2-3 m/s effective cutting speed for sash), throughput increases 5-10×.
- **Band saw (later development)**: Thinner kerf than circular saw (1.5-2 mm vs. 4-6 mm), yielding more lumber per log. Requires welded or riveted continuous steel band. Higher blade maintenance but less waste. Band saws also cut curves, allowing the sawyer to follow the log's natural taper and grain, recovering more usable lumber from crooked logs.
  - **Band saw blade maintenance**: A band saw blade stretches under tension and fatigues from running over the wheels. Typical blade life: 4-8 hours of cutting before the blade dulls or cracks at the weld. Blade tension for a 50 mm wide blade: 40-80 kg (check manufacturer spec; over-tensioning causes premature blade breakage). Blade tracking (running centered on the wheel crown) must be checked every time the blade is changed.

### Saw Method Comparison

| Parameter | Pit Saw | Sash Saw | Circular Saw | Band Saw |
|-----------|---------|----------|-------------|----------|
| Power source | 2 workers | Water wheel (3-15 kW) | Steam (11-75 kW) | Steam or electric |
| Throughput (bf/day) | 100-200 | 500-2,000 | 2,000-10,000 | 3,000-15,000 |
| Kerf width | 3-4 mm | 2-3 mm | 4-6 mm | 1.5-2.5 mm |
| Lumber recovery | 35-45% | 45-55% | 40-50% | 50-65% |
| Minimum infrastructure | Scaffold | Millrace, dam, building | Boiler, engine, building | Same as circular + blade welder |
| Seasonal limitation | None | Freezing water stops mill | Fuel supply dependent | Same as circular |
| Blade maintenance | File after each log | File daily | Re-file every 4-8 hours | Replace blade every 4-8 hours |
| Typical era | Settlement (Year 0-5) | Village (Year 5-20) | Town (Year 20+) | Town (Year 20+) |

## References

- [Foundations](index.md) — parent capability
- [Foundations Domain](./index.md) — domain overview and related capabilities
- [Building Materials & Methods](../construction/building-materials.md) — upstream dependency (material)

Sawmilling connects directly to [Carpentry](carpentry.md), which transforms dimensional lumber into finished goods, and to [Construction](../construction/index.md), which consumes beams and planks for structures. Sawdust byproduct feeds [Chemistry](../chemistry/index.md) processes including wood distillation (charcoal, methanol, tar).

### Material Handling

Proper handling of input materials and products is essential for consistent results:

- Stack green lumber immediately after sawing — delay allows fungal attack in warm weather. Stain fungi can discolor lumber within days in humid conditions.
- Sticker all stacks with uniform-thickness sticks placed in vertical alignment (every 600 mm along the board length) to prevent the stack from settling unevenly and warping the boards.
- Use FIFO (first-in, first-out) inventory management for drying lumber. Older stacks should be moved to storage or shipment first.
- Label each stack with species, date sawn, date stacking began, and intended drying method (air or kiln).
- Inspect lumber before use — reject any that show signs of fungal decay (blue stain, soft spots, fruiting bodies), excessive checking, or insect damage.
- Keep the sawmill area clear of debris. Sawdust accumulation creates slip hazards and fire risk. Remove sawdust daily.
- Segregate waste streams: sawdust for fuel or compost, bark for mulch, offcuts for kindling or re-sawing.

---

*Part of the [Bootciv Tech Tree](../index.md) · [Foundations](./index.md) · [All Domains](../index.md)*
