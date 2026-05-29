# Machining

> **Node ID**: machine-tools.machining
> **Domain**: [Machine Tools Bootstrap](./index.md)
> **Timeline**: Years 10-25
> **Outputs**: machined_parts
> **Dependencies**: [`machine-tools.bearings-abrasives`](bearings-abrasives.md), [`machine-tools.iterative-bootstrap`](iterative-bootstrap.md)
> **Enables**: [`energy.gravity.water-turbines`](../energy/water-turbines.md), [`energy.steam-power.steam-turbines`](../energy/steam-turbines.md), [`knowledge.printing`](../knowledge/printing.md), [`machine-tools.edm-cnc`](edm-cnc.md), `machine-tools.joining.friction-stir`, [`mining.drilling`](../mining/drilling.md)
> **Critical**: Yes — achieves the precise geometry, surface finish, and dimensional tolerance that make interchangeable parts possible


Machining removes material from a workpiece to achieve precise geometry, surface finish, and dimensional tolerance. This document covers the cutting operations themselves — for machine construction, see [Iterative Bootstrap](./iterative-bootstrap.md); for cutting tool materials and abrasives, see [Bearings & Abrasives](./bearings-abrasives.md); for the formed stock that feeds machining, see [Forming](./forming.md).

## Lathe Operations

The lathe rotates the workpiece against a stationary single-point cutting tool. All cylindrical parts (shafts, bushings, pulleys, threads) originate here.

## Turning

Reduces the outer diameter of a rotating workpiece. The workpiece is held in a chuck or between centers; the tool moves parallel to the spindle axis.

**Construction steps for a turning operation** (roughing + finishing a 50 mm diameter shaft from 55 mm bar stock):
1. Mount the workpiece in a [3-jaw chuck](../glossary/lathe-chuck.md) with 25 mm grip length. Indicate the free end with a dial indicator — runout must be <0.05 mm. Adjust if necessary.
2. Select an HSS roughing tool: rake angle 8-12° (positive), relief angle 8°, nose radius 0.8 mm. Mount in toolpost with the cutting edge at center height (±0.5 mm).
3. Calculate spindle speed for roughing: RPM = (1000 × cutting speed) / (π × diameter). For mild steel with HSS at 25 m/min on 55 mm bar: RPM = (1000 × 25) / (π × 55) = 145 RPM. Set the lathe to the nearest available speed.
4. Set roughing depth of cut: 2.5 mm (removing 5 mm from diameter). Set cross-slide to 2.5 mm on the dial. Set longitudinal feed to 0.4 mm/rev.
5. Engage the feed lever. Cut from the chuck end toward the tailstock. Apply flood coolant (soluble oil emulsion, 5-10%). Complete the roughing pass.
6. Repeat roughing passes until the diameter is 1 mm oversize (50.5 mm). This ensures a clean, concentric surface for the finishing cut.
7. Select an HSS finishing tool: rake angle 12-15°, relief angle 10°, nose radius 1.5 mm. Set depth of cut: 0.25 mm. Set feed to 0.08 mm/rev. Reduce speed if needed for finish quality.
8. Take the finishing pass in one continuous stroke. Do not stop mid-pass — restart marks are visible defects.

**Calibration**: Measure the finished diameter with a micrometer (0-75 mm range, 0.01 mm resolution) at three points along the length and at two angular positions (90° apart). All six measurements must be within the specified tolerance band. For a ±0.02 mm tolerance, all readings must be 49.98-50.02 mm. Measure surface finish with a profilometer or compare against a surface finish standard (visual-tactile comparison block).

**Expected performance**: Roughing: 1.5-3 mm depth of cut, feed 0.3-0.6 mm/rev, surface finish 5-10 μm Ra, stock removal rate 15-40 cm³/min. Finishing: 0.25-0.5 mm depth, feed 0.05-0.15 mm/rev, surface finish 1-3 μm Ra, tolerance ±0.02 mm on diameter.

**Materials specifications**: HSS M2 tool bits (10 × 10 × 100 mm), soluble oil emulsion (5-10% concentration in water), mild steel bar stock (55 mm diameter, [Iron & Steel](../metals/iron-steel.md)), dial indicator (0.01 mm resolution), micrometer (0-75 mm range, 0.01 mm resolution).

**Strengths**:
- Produces cylindrical parts with precise dimensional control (±0.02 mm) and smooth surface finish (1-3 μm Ra)
- Roughing removes material quickly (15-40 cm³/min) — most of the work is done in 2-3 passes
- Finishing pass achieves tight tolerance and good surface finish in a single pass

**Weaknesses**:
- Limited to cylindrical or radially-symmetric parts — flat surfaces and complex profiles require milling
- Long, slender workpieces deflect under cutting force, producing taper (barrel-shaped or hourglass-shaped parts)
- Chips are hot and sharp — requires flood coolant and chip management for safe operation

## Facing

Cuts across the end of the workpiece perpendicular to the spindle axis, producing a flat surface. Tool feeds from center outward (or periphery inward). Use slow feed near center where surface speed drops to zero. Achievable flatness: ~0.02 mm across a 50 mm face.

**Construction steps for facing a 50 mm bar**:
1. Mount the workpiece in the chuck with 10-15 mm protrusion. Ensure the end to be faced is accessible.
2. Mount a facing tool (left-hand knife tool, 0° lead angle) in the toolpost at center height.
3. Set spindle speed for the outer diameter: RPM = (1000 × 25) / (π × 50) = 159 RPM for mild steel with HSS at 25 m/min.
4. Position the tool at the center of the workpiece (just touching the end face). Set the cross-slide dial to zero.
5. Engage cross-feed (automatic if available, or feed manually at 0.1-0.2 mm/rev). Feed outward from center to periphery.
6. Take a light finishing cut (0.1-0.2 mm depth) at 0.05 mm/rev feed for a smooth surface.

**Calibration**: Check flatness with a precision straightedge and feeler gauges across the face. Place the straightedge across a diameter — feeler gauge insertion must be <0.02 mm at any point. Check perpendicularity with a machinist's square against the bar OD — gap must be <0.02 mm over the face diameter.

**Expected performance**: Flatness: 0.02 mm across 50 mm face. Surface finish: 1-3 μm Ra (finishing cut). Material removal: one roughing pass (1-2 mm depth) + one finishing pass (0.1-0.2 mm) per face.

**Materials specifications**: Left-hand knife tool (HSS M2, 10 × 10 × 100 mm), soluble oil emulsion, precision straightedge (150 mm, flat to 0.005 mm), feeler gauge set (0.02-1.0 mm).

**Strengths**:
- Produces a flat reference surface perpendicular to the spindle axis — essential for subsequent operations
- Single-pass operation for most work (roughing + one finishing pass)
- Achievable flatness of 0.02 mm is adequate for most bearing seats, flange faces, and gauge surfaces

**Weaknesses**:
- Surface speed varies from zero at center to maximum at the periphery — surface finish is non-uniform
- Tool must be set precisely at center height — below center causes rubbing, above center causes chatter
- Facing large diameters (>100 mm) requires slow RPM and long cutting time at the outer edge

## Boring

Enlarges or trues an existing hole using a boring bar held in the toolpost. The workpiece rotates; the bar is fed into the bore. Essential for bearing housings and cylinder bores.

**Construction steps for boring a bearing housing** (25 mm bore, cast iron housing):
1. Mount the housing in the chuck, indicate the outer diameter to <0.02 mm runout. The existing cored or drilled hole should be 23-24 mm (1-2 mm undersize for boring).
2. Select a boring bar: diameter as large as will fit in the hole, length such that overhang ≤ 4× bar diameter. For a 25 mm bore, use a 16 mm diameter boring bar with 60 mm overhang (3.75× ratio — within the 4× limit).
3. Grind or select a boring tool bit: 10° positive rake for cast iron, 8° relief, 0.5 mm nose radius. Mount in the boring bar with the cutting edge at center height.
4. Set spindle speed for the bore diameter: RPM = (1000 × 20) / (π × 24) = 265 RPM for cast iron with HSS at 20 m/min.
5. Set depth of cut: 0.5 mm for roughing (removing 1 mm from diameter). Feed: 0.1 mm/rev. Apply cutting oil.
6. Take successive roughing passes until the bore is 0.2 mm undersize (24.8 mm).
7. Take a finishing pass: 0.1 mm depth, 0.05 mm/rev feed. Measure the bore with an inside micrometer after each finishing pass until the target diameter is reached (25.00 mm ±0.01 mm).

**Calibration**: Measure the finished bore with an inside micrometer or bore gauge at two positions along the length and two angular positions (90° apart). All four measurements must be within ±0.01 mm of the target diameter. Check for taper: the bore diameter at the open end and the bottom must agree within 0.01 mm. Check for roundness by measuring at multiple angular positions — variation must be <0.01 mm.

**Expected performance**: Tolerance: ±0.01 mm achievable with rigid setup. Surface finish: 0.8-2 μm Ra. Boring bar overhang limit: ≤ 4× bar diameter. Chatter threshold: above 4× overhang, vibration increases sharply, degrading finish and accuracy.

**Materials specifications**: Boring bar (16 mm diameter HSS or carbide-tipped, 100 mm long), HSS tool bit (8 × 8 mm), inside micrometer or bore gauge (0.01 mm resolution), cutting oil (sulfurized mineral oil), cast iron or steel housing.

**Strengths**:
- Achieves ±0.01 mm tolerance on internal diameters — essential for bearing fits
- Corrects eccentricity and taper in cored or drilled holes
- Boring bar setup is straightforward — uses the standard lathe toolpost

**Weaknesses**:
- Boring bar overhang causes chatter — limits the depth-to-diameter ratio that can be accurately bored
- Cannot bore blind holes deeper than the bar overhang limit (4× diameter)
- Surface finish degrades as the boring bar wears — tool must be re-sharpened periodically

## Threading

Cuts helical grooves on the workpiece surface. See [Bearings & Abrasives](./bearings-abrasives.md) for thread standards and tap/die production.

**Construction steps for cutting an M12×1.75 external thread**:
1. Turn the workpiece to the thread major diameter: 11.80-11.90 mm (0.1-0.2 mm below nominal 12 mm for clearance). Face the end and chamfer 1 mm × 45° to start the thread cleanly.
2. Grind a threading tool to 60° included angle with a tip radius of 0.05-0.10 mm. Verify the profile with a 60° thread gauge. Set the compound rest to 29.5° (half the thread angle + 0.5° for flank-only cutting).
3. Install change gears for 1.75 mm pitch. Verify: engage the half-nut and measure the leadscrew rotation versus carriage travel over 25 mm — must be exactly 1.75 mm pitch (14 threads in 25 mm).
4. Set spindle speed to 25-50% of normal turning speed (~80 RPM for 12 mm steel). Low speed gives time for half-nut engagement/disengagement.
5. Set the first cut depth to 0.1 mm on the compound dial. Engage the half-nut at the correct thread dial position (consult the thread dial chart for the specific lathe). Cut pass 1.
6. Disengage the half-nut at the end of the thread. Return the carriage to the start. Increase depth by 0.1-0.15 mm per pass. Re-engage the half-nut at the same dial position.
7. Continue passes until total infeed reaches 0.614 × pitch = 0.614 × 1.75 = 1.07 mm. Take a final spring pass (same depth as previous pass, no increase) to clean up the thread flanks.
8. Check the thread with a go/no-go ring gauge. The go gauge must thread on fully; the no-go gauge must not engage more than 2 turns.

**Calibration**: Thread pitch is verified by the change gear setup — measure 10 thread crests over a known distance with calipers. For M12×1.75: 10 crests should span 17.5 mm ±0.05 mm. Pitch diameter is checked with the go/no-go gauge. Visual: thread flanks should be smooth with no tear-out; the crests should show a flat (not sharp) profile.

**Expected performance**: Thread accuracy: ±0.05 mm on pitch diameter (6g tolerance class for M12×1.75). Surface finish: 1.6-6.3 μm Ra on flanks. Number of passes: 8-12 for M12×1.75 in mild steel. Time per thread: 3-5 minutes.

**Materials specifications**: HSS M2 threading tool bit (10 × 10 mm, ground to 60° profile), change gears (matching lathe specification for 1.75 mm pitch), thread gauge (60° profile), go/no-go ring gauge (M12×1.75, 6g tolerance), sulfurized cutting oil.

**Strengths**:
- Produces accurate threads (±0.05 mm pitch diameter) directly on the lathe — no tap or die needed
- Thread dial indicator allows precise re-engagement on the same groove for multi-pass threading
- Adjustable depth per pass gives full control over thread quality and tool load

**Weaknesses**:
- Slow — 8-12 passes per thread at 25-50% of normal turning speed
- Requires correct change gear setup for each pitch — wrong gears produce wrong thread
- Half-nut engagement must be at the correct thread dial position — mis-engagement ruins the thread

## Parting (Cutting Off)

Severs the finished part from the bar stock using a narrow parting tool (2-4 mm wide). Highest-risk lathe operation — tool is deeply embedded, prone to jamming and chatter.

**Construction steps for parting off a finished part**:
1. Position the parting tool at the correct distance from the finished face. The tool must be exactly perpendicular to the work — check with a small square against the tool side.
2. Set the parting blade height to center (±0.2 mm). A blade set above center rubs; below center digs in and jams.
3. Set spindle speed to the lowest setting: for 25 mm steel bar, ~100-150 RPM.
4. Engage the cross-slide feed (manual feed preferred for parting — feel for tool load). Feed rate: 0.05-0.10 mm/rev.
5. Apply flood coolant (soluble oil, heavy flow directed at both sides of the cut).
6. Feed steadily — do not stop mid-cut (work hardening makes restart difficult). Reduce feed rate as the tool approaches center to prevent the sudden snap-off that can damage the tool.
7. The part separates when the cut reaches approximately 2-3 mm from center. Catch the part to prevent damage to the finished surface.

**Calibration**: Measure the length of the parted piece with calipers — the parting cut removes 2-4 mm (blade width). Account for this in the initial positioning. Check the parted face for flatness — it should be flat within 0.1 mm. If the face shows a raised center ("pip"), the tool was below center height.

**Expected performance**: Blade width: 2-4 mm. Parting time for 25 mm steel bar: 30-60 seconds. Tool life: 20-50 parting operations before re-sharpening. Risk: tool breakage occurs in ~5% of operations if feed is uneven or coolant is inadequate.

**Materials specifications**: HSS parting blade (3 mm wide × 15 mm tall × 150 mm long), soluble oil coolant (flood application), calipers (0-150 mm, 0.02 mm resolution).

**Strengths**:
- Clean, flat cut surface — no secondary facing needed for non-critical applications
- Fast separation (30-60 seconds for 25 mm bar) once the tool is positioned

**Weaknesses**:
- Highest-risk lathe operation — tool jamming and breakage are common, especially on larger diameters
- Cannot stop mid-cut without work hardening the material, making restart difficult
- Tool must be precisely perpendicular and at center height — misalignment causes tapered cuts and breakage

## Milling Operations

The milling machine rotates a multi-tooth cutter while the workpiece moves on a programmable X-Y table. More versatile than the lathe for flat surfaces, slots, pockets, and complex profiles.

## Peripheral (Slab) Milling

Cutter axis is parallel to the machined surface. Teeth on the cutter periphery do the cutting. Used for squaring blocks and machining broad flats.

**Construction steps for slab milling a flat surface** (100 × 50 mm steel block):
1. Mount the workpiece in a milling vise on the machine table. Indicate the vise jaws with a dial indicator — alignment within ±0.01 mm over the jaw length. Seat the workpiece on parallels (flat the bottom first if needed).
2. Select a helical slab milling cutter: 75 mm diameter, 100 mm face width, 8 teeth, HSS. Mount on the arbor with a key to prevent rotation. Install the arbor support bracket.
3. Set spindle speed: RPM = (1000 × 25) / (π × 75) = 106 RPM for mild steel with HSS at 25 m/min.
4. Set depth of cut: 2 mm for roughing. Set table feed: 0.15 mm/tooth × 8 teeth × 106 RPM = 127 mm/min (set to nearest available feed rate, typically 125 mm/min).
5. Position the cutter just touching the workpiece surface (use a feeler gauge or paper strip method — 0.05 mm). Set the vertical dial to zero.
6. Raise the knee (or lower the spindle) by 2 mm. Engage the table feed. Cut across the full width of the workpiece. Apply flood coolant.
7. For the finishing pass: reduce depth to 0.25 mm, feed to 0.05 mm/tooth (42 mm/min). Take one pass across the full surface.

**Calibration**: Measure the machined surface flatness with a precision straightedge and feeler gauges — flatness within 0.02 mm over 100 mm length. Check parallelism between the top and bottom surfaces with a micrometer at four corners — variation <0.02 mm. Surface finish: compare against a standard block or measure with a profilometer (target: 1.5-3 μm Ra for finishing cut).

**Expected performance**: Depth of cut: 1-5 mm for roughing, 0.25-1 mm for finishing. Feed per tooth: 0.1-0.3 mm for roughing, 0.05-0.15 mm for finishing. Surface finish: 1.5-3 μm Ra (finishing). Flatness: 0.02 mm over 100 mm.

**Materials specifications**: Helical slab milling cutter (HSS, 75 mm diameter × 100 mm face, 8 teeth), milling vise (Kurt-type, precision ground jaws), parallels (matched height within 0.01 mm), soluble oil coolant, dial indicator (0.01 mm resolution).

- **Up-cut (conventional)**: Cutter rotates against feed direction. Chips start thin, end thick. Tends to pull workpiece into cutter — secure clamping essential. Better for older machines with leadscrew backlash.
- **Down-cut (climb)**: Cutter rotation matches feed direction. Chips start thick, end thin. Better surface finish, less tool wear. Requires rigid machine with zero backlash in feed screws.

**Strengths**:
- Produces broad flat surfaces with consistent thickness and parallelism
- Helical cutters provide a shearing cut — smoother finish and less chatter than straight-tooth cutters
- Multiple teeth share the cutting load — higher material removal rate than single-point turning

**Weaknesses**:
- Cutter deflection on long, thin workpieces produces uneven surfaces
- Requires a rigid machine with minimal backlash — climb milling is impossible on worn machines
- Setup time is significant (vise alignment, cutter selection, speed/feed calculation) compared to turning

## Face Milling

Cutter axis perpendicular to surface. Large-diameter face mill (50-100 mm) with inserted carbide or HSS tips machines broad flat surfaces efficiently. Preferred over slab milling for most flat work.

**Construction steps for face milling a steel plate** (150 × 100 × 10 mm):
1. Clamp the plate directly to the mill table using step blocks and clamps. Use at least two clamps on opposite sides. Place clamping force over solid support (not overhanging). Indicate the plate surface with a dial indicator on the spindle — shim until the surface is level within 0.02 mm over the full length.
2. Select a face mill: 63 mm diameter with 5 inserted HSS tips. Mount on the spindle with a pilot to ensure concentricity.
3. Set spindle speed: RPM = (1000 × 25) / (π × 63) = 126 RPM for mild steel with HSS at 25 m/min.
4. Set depth of cut: 1 mm for roughing. Feed per revolution: 0.5 mm/rev × 126 RPM = 63 mm/min.
5. Position the cutter with the workpiece offset so that the cutter enters from one side and exits the other (conventional milling). Take overlapping passes if the cutter diameter is smaller than the workpiece width. Overlap: 20-30% of cutter diameter.
6. For finishing: reduce depth to 0.25 mm, feed to 0.15 mm/rev. Take a single pass across the full surface.

**Calibration**: Measure surface flatness with a straightedge — 0.02 mm over 150 mm. Check surface finish with a profilometer or comparison block: 1.5-3 μm Ra for finishing. Inspect the tool insert edges under 10× magnification after machining — chipped or worn edges require indexing or replacement.

**Expected performance**: Cutting speed: same as turning for the given material. Feed per tooth: 0.1-0.3 mm for roughing, 0.05-0.15 mm for finishing. Surface finish: 1.5-3 μm Ra typical. Flatness: 0.02 mm over 150 mm with rigid setup.

**Materials specifications**: Face mill (63 mm diameter, 5 inserted HSS tips), milling machine with rigid spindle, step blocks and clamps (for direct table mounting), dial indicator (0.01 mm), soluble oil coolant.

**Strengths**:
- Most efficient method for machining broad flat surfaces — multiple inserts cutting simultaneously
- Inserted tips can be indexed (rotated to a fresh edge) when worn — no re-sharpening needed during a job
- Produces flat surfaces with excellent finish in a single finishing pass

**Weaknesses**:
- Large-diameter cutters require high spindle torque — small milling machines may stall on deep cuts
- Workpiece must be clamped directly to the table for maximum rigidity — vise clamping introduces deflection
- Insert cost adds up — each insert has 2-4 edges and costs $5-20 per edge

## End Milling

Small-diameter cutter (3-25 mm) for pockets, slots, profiles, and keyways. The workhorse of precision milling.

**Construction steps for milling a keyway** (6 mm wide × 3 mm deep on a 35 mm shaft):
1. Mount the shaft in V-blocks on the mill table. Clamp with strap clamps over the V-blocks. Indicate the shaft along its length with a dial indicator — alignment within 0.02 mm over the keyway length.
2. Select a 6 mm diameter, 4-flute HSS end mill. Mount in a collet chuck (not a drill chuck — insufficient grip for side cutting). Check runout with a dial indicator on the cutter body: <0.02 mm.
3. Set spindle speed: RPM = (1000 × 25) / (π × 6) = 1326 RPM for mild steel with HSS at 25 m/min.
4. Position the cutter at the start of the keyway. Use the edge finder to locate the shaft centerline. Offset by 3 mm (half the cutter diameter) to center the keyway on the shaft.
5. Cut the keyway in multiple axial passes. First pass: 1 mm depth. Second pass: 1 mm depth (2 mm total). Third pass: 1 mm depth (3 mm total — full depth). Feed: 0.05 mm/tooth × 4 flutes × 1326 RPM = 265 mm/min (reduce to 200 mm/min for safety in the keyway).
6. Apply flood coolant. Clear chips between passes with compressed air (safety glasses required).

**Calibration**: Measure the keyway width with a micrometer or slip gauges: 6.00-6.05 mm for a standard 6 mm keyway. Measure keyway depth with a depth micrometer: 3.00-3.10 mm from the shaft surface. Check keyway position: the keyway must be centered on the shaft within 0.05 mm — measure from each side of the shaft to the keyway edge with calipers; the two measurements must agree within 0.05 mm.

**Expected performance**: Slot width tolerance: ±0.05 mm with a new end mill. Depth tolerance: ±0.05 mm. Surface finish: 1.6-3.2 μm Ra on the keyway floor. Tool life: 30-60 minutes of cutting time in mild steel.

**Materials specifications**: HSS end mill (6 mm diameter, 4-flute, 20 mm flute length), V-blocks (matched pair, ground to 0.005 mm), collet chuck (6 mm collet), edge finder (0.200 mm tip diameter), depth micrometer (0-75 mm range, 0.01 mm resolution), soluble oil coolant.

- **Slotting**: End mill diameter matches slot width. Cut full depth in multiple passes (1-3 mm per pass axially) rather than single deep pass.
- **Pocketing**: Helical or ramp entry. Clear chips with air blast or coolant. Stepover = 40-60% of cutter diameter for roughing.
- **Keyway cutting**: Mill a rectangular slot on a shaft for a square or rectangular key. Width per standard (e.g., 6 mm keyway on 30-38 mm shaft). Depth: approximately half the keyway width.

**Strengths**:
- Versatile — pockets, slots, profiles, keyways, and complex contours all from one type of cutter
- Small-diameter cutters can access tight spaces and produce fine detail
- Collet mounting provides minimal runout — precise slot widths

**Weaknesses**:
- Small end mills (3-6 mm) are fragile — excessive depth of cut or feed rate breaks the cutter
- Chip evacuation in deep slots is poor — chips recut, degrading surface finish and accelerating tool wear
- Limited depth of cut per pass (1-3 mm) means many passes for deep features


## Drilling

Produces holes using a rotating twist drill. The drill press or lathe tailstock feeds the drill axially into the work.

**Construction steps for drilling a 10 mm hole** (in 15 mm mild steel plate):
1. Mark the hole location with a center punch. Use a magnifier and rule or a combination square for accurate layout. Punch mark should be 0.5-1.0 mm deep.
2. Mount the workpiece in a drill press vise, clamped to the table. Do not hold work by hand — the drill can grab and spin the workpiece.
3. Drill a pilot hole with a 4 mm drill bit: RPM = (1000 × 25) / (π × 4) = 1990 RPM. Feed: 0.15 mm/rev. Apply cutting oil. Through-hole in 15 mm steel.
4. Enlarge to 10 mm with a standard 118° point angle twist drill: RPM = (1000 × 25) / (π × 10) = 796 RPM. Feed: 0.2 mm/rev. Apply cutting oil. Use peck drilling: retract the drill every 2-3 mm to clear chips (prevents binding and breakage in holes deeper than 3× diameter).
5. Deburr both sides with a countersink or larger drill bit (12 mm) spun by hand.

**Calibration**: Measure the hole diameter with an inside micrometer or pin gauge: target 10.00-10.15 mm (±0.1 mm tolerance for a drilled hole). Check hole position with calipers from the edge: the hole center must be within ±0.15 mm of the layout mark. Check for bellmouth (oversize at the entrance) — measure at the top and bottom of the hole; the diameter difference must be <0.1 mm.

**Expected performance**: Hole tolerance: ±0.1 mm on diameter. Position accuracy: ±0.15 mm on drill press. Hole straightness: 0.05-0.15 mm deviation over 15 mm depth (longer holes deviate more). Surface finish: 3-6 μm Ra.

**Materials specifications**: HSS twist drill set (4 mm and 10 mm, 118° point angle), drill press vise (clamped to table), center punch (hardened steel), cutting oil, pin gauge set or inside micrometer.

- **Twist drill geometry**: 118° point angle (standard), 135° for harder materials. Two helical flutes evacuate chips.
- **Pilot hole**: For holes >10 mm, drill a pilot hole (3-5 mm) first to reduce cutting force and improve accuracy.
- **Peck drilling**: For holes deeper than 3× diameter, retract the drill every 1-2 mm to clear chips. Prevents binding and drill breakage.

**Strengths**:
- Fastest method for producing holes — a 10 mm through-hole in 15 mm steel takes 15-30 seconds
- Simple equipment — drill press or even a hand drill suffices for non-critical holes
- Pilot drilling improves accuracy and reduces the risk of drill breakage

**Weaknesses**:
- Limited accuracy (±0.1 mm) — drilled holes are not precise enough for bearing fits or dowel pins without reaming or boring
- Drill tends to wander on curved or angled surfaces — pilot hole or spot drill required
- Chips are difficult to evacuate in deep holes (>5× diameter) — peck drilling is slow

## Boring (Milling Machine)

Uses a single-point boring head in the milling machine spindle to enlarge and true a drilled hole. Adjustable boring head allows precise diameter control via micrometer adjustment (0.01 mm resolution).

**Construction steps for boring a bearing pocket** (25 mm diameter × 15 mm deep, in steel):
1. Drill a 23 mm hole through the workpiece (pilot drill to 10 mm, then enlarge to 23 mm).
2. Mount an adjustable boring head on the milling machine spindle. Install a carbide-tipped boring bar (12 mm diameter, 25 mm long). Set the initial radius slightly below 23 mm.
3. Set spindle speed: RPM = (1000 × 25) / (π × 23) = 345 RPM for steel with carbide at 25 m/min.
4. Bore roughing passes: set the boring head micrometer to remove 0.5 mm per pass (1 mm from diameter). Feed the table vertically at 0.1 mm/rev. Repeat until the diameter is 24.8 mm (0.2 mm undersize).
5. Bore finishing pass: set the boring head to remove 0.1 mm from diameter. Feed at 0.05 mm/rev. Measure the bore with an inside micrometer. Adjust the boring head micrometer by the difference between measured and target diameters. Take a final pass.

**Calibration**: Measure the finished bore with an inside micrometer at two depths (5 mm and 10 mm from the surface) and two angular positions (90° apart). Target: 25.00 mm ±0.01 mm. Check concentricity to a datum feature with a dial indicator on the spindle: runout <0.02 mm.

**Expected performance**: Tolerance: ±0.01 mm. Concentricity to existing features: ±0.02 mm. Surface finish: 0.8-2 μm Ra. Depth control: ±0.05 mm with knee dial.

**Materials specifications**: Adjustable boring head (0.01 mm micrometer resolution), carbide-tipped boring bar (12 mm diameter), inside micrometer (0.01 mm resolution), cutting oil.

**Strengths**:
- Achieves ±0.01 mm tolerance — suitable for bearing pocket and precision shaft hole applications
- Corrects position errors from the initial drilling — the boring tool cuts a true circle regardless of the drilled hole position
- Adjustable boring head allows incremental diameter adjustment in 0.01 mm steps

**Weaknesses**:
- Boring bar deflection limits depth-to-diameter ratio — chatter occurs above 4× overhang
- Slower than reaming for large batches — each bore requires multiple passes
- Requires a milling machine with a precision spindle (runout <0.01 mm)

## Reaming

Finishing operation that enlarges a drilled hole to precise diameter and smooth finish using a multi-flute reamer.

**Construction steps for reaming a 10 mm hole**:
1. Drill the hole 0.3 mm undersize (9.7 mm) using a standard twist drill. Deburr the entrance.
2. Mount a 10.00 mm machine reamer (HSS, straight shank, 6 flutes) in the drill press or lathe tailstock chuck. Do not use a keyless chuck — use a collet or jacobs chuck with sufficient grip.
3. Set speed to 1/3 of drilling speed: ~265 RPM for 10 mm in mild steel. Set feed to 0.4 mm/rev (steady, continuous).
4. Apply a generous stream of cutting oil (lard oil or soluble oil). Feed the reamer through the hole in one continuous motion. Do not stop or reverse while engaged — stopping produces chatter marks; reversing damages the reamer edges.
5. Remove the reamer by continuing to feed through the bottom of the hole (through-hole), or withdraw while still rotating in the forward direction (blind hole).

**Calibration**: Measure the reamed hole with a pin gauge or inside micrometer: target 10.00 mm ±0.01 mm. Check surface finish with a comparison block: 0.4-1.0 μm Ra. The reamed hole should have a uniform, smooth appearance with no visible chatter marks or scoring.

**Expected performance**: Tolerance: ±0.01 mm on diameter. Surface finish: 0.4-1.0 μm Ra. Straightness improvement: reaming improves drilled hole straightness by ~50%. Stock removal: 0.2-0.5 mm on diameter.

**Materials specifications**: HSS machine reamer (10.00 mm, 6 flutes, straight shank), cutting oil (lard oil preferred for steel), pin gauge (10.00 mm ±0.005 mm) or inside micrometer.

**Strengths**:
- Produces holes with excellent surface finish (0.4-1.0 μm Ra) and tight tolerance (±0.01 mm)
- Fast — single-pass operation after the undersized hole is drilled
- Improves hole straightness and roundness compared to drilling alone

**Weaknesses**:
- Cannot correct significant position errors — the reamer follows the drilled hole axis
- Requires a pre-drilled hole 0.2-0.5 mm undersize — adds a drilling setup step
- Reamer is damaged by reversing, stopping mid-cut, or running dry — tool cost is significant ($20-80 per reamer)

## Grinding Operations

Uses abrasive wheels for precision finishing. The final machining step before lapping. Achieves tolerances and finishes impossible with cutting tools.

## Surface Grinding

Flat workpiece on a magnetic chuck (or clamped). Horizontal-spindle grinding wheel reciprocates across the surface.

**Construction steps for surface grinding a gauge block** (50 × 25 × 10 mm steel):
1. Mount the workpiece on a [magnetic chuck](../glossary/magnetic-chuck.md). Place the workpiece on a clean chuck surface — any dirt or grit under the workpiece introduces tilt. Switch on the magnet. Verify hold by pushing the workpiece with moderate force — it must not shift.
2. Select a grinding wheel: 200 mm diameter × 20 mm wide, aluminum oxide, 60 grit, K-grade (medium hardness), vitrified bond. Dress the wheel with a single-point diamond dresser: pass the dresser across the wheel face at 0.02 mm depth, 0.5 m/min cross-feed, until the full face is clean and sharp.
3. Set wheel speed: 1500-2100 m/min peripheral speed (RPM = (1000 × 1800) / (π × 200) = 2865 RPM — check machine rating).
4. Set the cross-feed to cover the full workpiece width in overlapping passes. Step-over: 5 mm per stroke (25% of wheel width).
5. Set downfeed (depth of cut): 0.02 mm per pass for roughing. Engage the automatic table reciprocation and cross-feed. Apply flood coolant (soluble oil, heavily diluted, high volume).
6. Rough grind until 0.01 mm above target thickness. Take a spark-out pass (zero downfeed — one full stroke with the wheel at the same height to remove the last 0.005-0.01 mm by elastic recovery).
7. Measure the workpiece thickness with a micrometer. If within tolerance, demagnetize the chuck and remove the workpiece.

**Calibration**: Measure thickness at four corners and center with a micrometer (0.001 mm resolution): all five measurements must be within ±0.005 mm of target. Check parallelism between the ground surface and the opposite face with a dial indicator on a surface plate: variation <0.0025 mm. Check surface finish with a profilometer: 0.2-0.8 μm Ra.

**Expected performance**: Flatness: ±0.005 mm over 50 mm. Parallelism: ±0.0025 mm. Surface finish: 0.2-0.8 μm Ra. Material removal rate: 5-20 mm³/min per mm of wheel width. Downfeed: 0.005-0.05 mm per pass.

**Materials specifications**: Grinding wheel (Al₂O₃, 60 grit, K-grade, vitrified bond, 200 mm × 20 mm), single-point diamond dresser, magnetic chuck (electromagnetic or permanent magnet), soluble oil coolant (30:1 water-to-oil), micrometer (0.001 mm resolution).

**Strengths**:
- Achieves the tightest flatness tolerance of any conventional machining operation (±0.005 mm)
- Surface finish of 0.2-0.8 μm Ra is suitable for gauge surfaces, sealing faces, and precision slides
- Magnetic chuck provides quick, uniform clamping without mechanical fixtures

**Weaknesses**:
- Grinding generates intense localized heat (1000-1500°C at the grain-workpiece interface) — inadequate coolant causes surface burns and residual stress
- Slow material removal compared to milling — grinding is a finishing operation, not a bulk removal process
- Magnetic chuck only holds ferrous workpieces — non-ferrous materials require mechanical clamping

## Cylindrical Grinding

Workpiece rotates between centers; grinding wheel contacts the OD. For precision shafts, bearing journals, and gauge surfaces.

**Construction steps for grinding a bearing journal** (30 mm diameter × 40 mm long):
1. Mount the workpiece between centers (headstock center and tailstock center). Use a drive dog and faceplate to rotate the workpiece. Ensure centers are clean and lubricated with high-pressure grease.
2. Dress the grinding wheel (Al₂O₃, 80 grit, J-grade, 300 mm diameter) with a diamond dresser.
3. Set work speed: 10-25 m/min (RPM = (1000 × 15) / (π × 30) = 159 RPM). Grinding wheel speed: 1800 m/min.
4. Set infeed: 0.01 mm per pass for roughing. Engage the infeed and the work rotation. Apply flood coolant. Take roughing passes until 0.005 mm above the target diameter.
5. Take finishing passes: infeed 0.002 mm. Take a spark-out pass at zero infeed to clean up elastic deflection.
6. Measure with a micrometer: target 30.000 mm ±0.003 mm.

**Calibration**: Measure the journal diameter at three positions along the length and at two angular positions. All measurements must be within ±0.003 mm. Check roundness by rotating the workpiece slowly and measuring with a dial indicator: total indicated runout <0.003 mm. Surface finish: 0.1-0.4 μm Ra.

**Expected performance**: Tolerance: ±0.003 mm on diameter. Surface finish: 0.1-0.4 μm Ra. Roundness: 0.001-0.003 mm. Taper: <0.002 mm over 40 mm length. Infeed: 0.005-0.025 mm per pass (roughing), 0.002-0.005 mm (finishing).

**Materials specifications**: Grinding wheel (Al₂O₃, 80 grit, J-grade, vitrified bond, 300 mm diameter), diamond dresser, between-centers driver (dog and faceplate), soluble oil coolant, micrometer (0.001 mm resolution).

**Strengths**:
- Achieves the tightest cylindrical tolerance (±0.003 mm) of any conventional machining operation
- Surface finish of 0.1-0.4 μm Ra is suitable for bearing journals and high-speed shaft seals
- Between-centers mounting ensures concentricity with other machined features on the same shaft

**Weaknesses**:
- Slow — material removal rate is 10-50× lower than turning
- Requires a dedicated cylindrical grinder — not possible on a surface grinder without special fixturing
- Grinding heat can cause thermal damage (burns, residual stress) if coolant flow is interrupted

## Feeds & Speeds Guidelines

Cutting speed (surface meters per minute) determines spindle RPM: **RPM = (1000 × cutting speed) / (π × diameter)**.

| Material | HSS Turning (m/min) | HSS Milling (m/min) | Drilling (m/min) | Grinding (m/min) |
|----------|--------------------|--------------------|------------------|-----------------|
| Aluminum | 150-300 | 150-250 | 50-80 | — |
| Brass    | 80-150 | 80-120 | 30-60 | — |
| Cast iron | 25-45 | 20-35 | 15-25 | 25-35 |
| Mild steel | 20-40 | 18-30 | 15-25 | 25-35 |
| Tool steel | 12-25 | 10-20 | 8-15 | 20-30 |
| Stainless steel | 12-20 | 10-18 | 8-15 | 18-28 |

**[Feed rates](../glossary/feed-rates.md)** (for HSS tools):
- Turning roughing: 0.3-0.6 mm/rev; finishing: 0.05-0.15 mm/rev
- Milling: 0.05-0.3 mm/tooth (smaller for harder materials)
- Drilling: 0.1-0.3 mm/rev (larger diameter = higher feed)

Carbon steel tool bits run at roughly 50% of HSS speeds. See [Bearings & Abrasives](./bearings-abrasives.md) for tool material properties.

## Tolerance Summary by Operation

| Operation | Typical Tolerance | Surface Finish | Best Achievable |
|-----------|------------------|----------------|-----------------|
| Turning (rough) | ±0.1-0.25 mm | 3-10 μm Ra | ±0.05 mm |
| Turning (finish) | ±0.02-0.05 mm | 1-3 μm Ra | ±0.01 mm |
| Facing | ±0.02 mm flatness | 1-3 μm Ra | ±0.01 mm |
| Milling (rough) | ±0.1 mm | 3-6 μm Ra | ±0.05 mm |
| Milling (finish) | ±0.025-0.05 mm | 1-2 μm Ra | ±0.015 mm |
| Drilling | ±0.1 mm | 3-6 μm Ra | ±0.05 mm |
| Boring | ±0.01-0.025 mm | 0.8-2 μm Ra | ±0.005 mm |
| Reaming | ±0.01 mm | 0.4-1 μm Ra | ±0.005 mm |
| Surface grinding | ±0.005 mm | 0.2-0.8 μm Ra | ±0.002 mm |
| Cylindrical grinding | ±0.003 mm | 0.1-0.4 μm Ra | ±0.001 mm |
| Lapping | ±0.001 mm | 0.025-0.1 μm Ra | ±0.0005 mm |

## Workholding

Secure workholding is essential — a loose workpiece is both inaccurate and dangerous.

- **[Lathe chuck](../glossary/lathe-chuck.md)** (3-jaw self-centering): Quick setup, ±0.05 mm repeatability. For round and hex stock.
- **[Lathe chuck](../glossary/lathe-chuck.md)** (4-jaw independent): Each jaw adjusts separately. Can hold irregular shapes, achieve ±0.01 mm concentricity with dial indicator alignment.
- **Between centers**: Workpiece supported by centers in headstock and tailstock. Best concentricity. Requires drive dog and faceplate. For long shafts.
- **Collet**: Spring-steel sleeve grips bar stock tightly. Best concentricity (±0.005 mm). Limited diameter range per collet.
- **Milling vise**: Kurt-style precision vise. Clamp workpiece on mill table. Indicate (dial indicator) jaw for alignment to ±0.01 mm.
- **Clamps and step blocks**: Direct clamping to mill table T-slots. For oversized or irregular workpieces. Use at least two clamps. Place clamping force over solid support (not overhanging).
- **[Magnetic chuck](../glossary/magnetic-chuck.md)** (surface grinder): Electromagnetic or permanent magnet. Holds ferrous workpieces flat without mechanical clamps. Demagnetize workpiece after grinding.
- **V-blocks and clamps**: Hold round stock for milling flats or drilling cross-holes. Indicate V-block alignment with dial indicator.

## Cutting Fluid Application

Cutting fluids cool the tool and workpiece, lubricate the chip-tool interface, and flush chips. See [Lubricants](../chemistry/lubricants.md) for full production details.

**Quick reference by operation**:

| Operation | Recommended Fluid | Application |
|-----------|-------------------|-------------|
| Turning (light) | Soluble oil emulsion (5-10%) | Flood or manual |
| Turning (heavy) | Sulfurized cutting oil | Flood |
| Milling | Soluble oil emulsion | Flood |
| Drilling | Soluble oil emulsion | Flood or through-spindle |
| Tapping/threading | Straight cutting oil or sulfurized oil | Flood or manual |
| Reaming | Lard oil or soluble oil | Flood |
| Grinding | Soluble oil or synthetic (heavily diluted) | Flood — high volume |

## Safety

- **[Eye protection mandatory](../glossary/eye-protection-mandatory.md)** for all machining. Safety glasses (ANSI Z87.1 rated) at minimum. Face shield for grinding and boring operations that produce large chips. Chips are hot and sharp — steel chips at 300°C+ cause instant burns and lacerations.
- **[No loose clothing, gloves, rings, or long sleeves](../glossary/no-loose-clothing-gloves-rings-or-long-sleeves.md)** near rotating machinery. Lathe chucks and drill presses are entanglement hazards — loose items are pulled in within one revolution.
- **Chip management**: Use chip hook or brush — never hands. Steel chips are razor-sharp and hot (blue = 300°C+). Compressed air clearing produces airborne chips — wear safety glasses and point the air stream away from people.
- **Workpiece security**: Verify clamping before every cut. A thrown workpiece is a lethal projectile — 5 kg at 500 RPM has kinetic energy of ~700 J.
- **Abrasive wheels**: Ring test before mounting (suspend wheel, tap with hardwood dowel — clear ring = sound, dull thud = cracked and must be discarded). Never exceed rated speed. Use wheel guards (steel, covering 180° of wheel periphery). Dress wheels regularly to maintain sharpness and concentricity.
- **Grinding dust**: Use extraction or dust collection. Inhaling fine metal dust causes lung damage. Grinding cast iron and steel produces respirable particles (<10 μm) that penetrate deep into the lungs. Wet grinding is preferred — eliminates airborne dust.

## See Also

- Machine tool construction sequence: [Iterative Bootstrap](./iterative-bootstrap.md)
- Cutting tool materials and abrasives: [Bearings & Abrasives](./bearings-abrasives.md)
- Cutting fluid production and properties: [Lubricants](../chemistry/lubricants.md)
- Formed stock feeding machining operations: [Forming](./forming.md)
- Precision achievement milestones: See [Iterative Bootstrap](./iterative-bootstrap.md) precision table
- Iron and steel production: [Iron & Steel](../metals/iron-steel.md)

## Limitations

- **Material removal waste**: Machining converts 20-80% of raw material into chips (swarf). For expensive materials (copper, titanium), this waste is a significant cost factor. Chip recycling is energy-intensive.
- **Tool wear**: Cutting tools dull through abrasion, adhesion, diffusion, and fatigue. Tool life follows Taylor's equation: VTⁿ = C. Carbide tools last 15-60 minutes of cutting time depending on speed and material.
- **Thermal distortion**: Cutting generates heat (80% goes into chip, 15% into tool, 5% into workpiece). Thin workpieces distort from thermal expansion, requiring cool-down periods between roughing and finishing passes.
- **Vibration and chatter**: At certain depth-of-cut / speed combinations, the cutting process becomes unstable, causing chatter — self-excited vibration that degrades surface finish and can damage the tool. Requires stiffness analysis and parameter tuning.
- **Surface integrity**: Machining creates a worked surface layer (residual stress, microstructural changes, micro-cracks) 10-200 μm deep. Fatigue-critical parts may require post-machining treatments (shot peening, stress relief annealing).
- **Skill requirement**: Manual machining requires significant operator skill for setup, tool selection, and process control. CNC machining transfers this to programming but requires software expertise.

[← Back to Machine Tools](index.md)
