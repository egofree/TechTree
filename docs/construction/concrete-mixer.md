# Concrete Mixer

> **Node ID**: construction.concrete-mixer
> **Domain**: [Construction](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`chemistry.cement`](../chemistry/cement.md)
> **Enables**: [`construction.industrial-buildings`](./industrial-buildings.md), [`transport.roads`](../transport/roads.md)
> **Timeline**: Years 10-25
> **Outputs**: mixed_concrete
> **Critical**: Yes — consistent concrete mixing is required for all reinforced concrete construction; hand mixing produces inconsistent strength and inadequate distribution of aggregate

## Principle

A concrete mixer combines cement, sand, aggregate, and water into a homogeneous mixture by tumbling the ingredients inside a rotating drum. Internal baffles (fixed blades welded to the drum interior) lift and fold the batch with each rotation, ensuring uniform distribution of cement paste around aggregate particles. The rotating-drum tilting design is the simplest effective mixer: a conical or cylindrical drum mounted on a frame, rotated by a hand crank or motor, and tilted to discharge the mixed batch.

Mixing effectiveness depends on drum geometry, rotation speed, and baffle design. Too slow: ingredients slide without mixing. Too fast: centrifugal force pins material to the drum wall, preventing folding. The optimal speed keeps the material in a cascading motion — lifted by baffles to the top of the drum, then falling through itself. Drum rotation rate: 15-25 RPM for hand-cranked, 12-20 RPM for powered mixers.

## Materials

### Hand-Cranked Tilting Drum Mixer (150-200 L batch)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel sheet (drum) | 30-50 kg | 3-5 mm thick, mild steel A36 or equivalent | [Iron & Steel](../metals/iron-steel.md) | Hardwood drum with metal bands (shorter life, absorbs water) |
| Steel bar (baffles) | 5-10 kg | 10 × 50 mm flat bar, 4-6 pieces | [Iron & Steel](../metals/iron-steel.md) | None — baffles are essential |
| Steel bar (frame) | 40-60 kg | 40 × 40 mm or 50 × 50 mm angle iron | [Iron & Steel](../metals/iron-steel.md) | Timber frame (heavier, rots) |
| Steel shaft (drum trunnion) | 5-10 kg | 30-40 mm diameter, 400-500 mm long, turned | [Iron & Steel](../metals/iron-steel.md) | Hardwood shaft with iron journals |
| Cast iron gears or chain drive | 1 set | 4:1 to 6:1 reduction ratio | [Foundry](../metals/casting.md) | V-belt and pulley (requires rubber belts) |
| Crank handle | 1 | Forged steel, 250-350 mm arm length | [Forging](../metals/forging.md) | Timber handle with iron ferrule |
| Bearings | 4 | Pillow block or plain journal bearings, 30-40 mm bore | [Bearings](../machine-tools/bearings-abrasives.md) | Hardwood bearings with grease (higher friction) |
| Bolts and nuts | 3-5 kg | M10-M16, grade 4.6 or 8.8 | [Fasteners](../metals/fasteners.md) | Riveted joints (non-adjustable) |

### Powered Conversion (adds to hand-cranked base)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Electric motor | 1 | 1.5-3 kW, 1400-1500 RPM, three-phase or single-phase | [Motors](../energy/electric-motors.md) | Petrol/diesel engine (5-8 HP) |
| V-belts and pulleys | 2-3 | A-section or B-section belts, cast iron pulleys | [Machine Tools](../machine-tools/index.md) | Roller chain and sprockets |
| Motor mount plate | 1 | 6-10 mm steel plate, adjustable slot for belt tension | [Iron & Steel](../metals/iron-steel.md) | Timber motor mount (less rigid) |

## Construction Steps

### Drum Fabrication

1. **Cut drum shell**: Mark and cut a rectangular sheet of 3-5 mm steel plate. For a 200 L mixer: approximately 900 mm wide × 1200 mm long (forming a cylinder 400 mm diameter × 900 mm long, with a conical discharge section). Roll the sheet into a cylinder on a plate roller or by bending over a mandrel. Overlap the seam 30-50 mm for welding.

2. **Form the conical discharge end**: Cut a truncated cone section from the same plate (small diameter 250 mm, large diameter matching the cylinder). Roll and weld the cone. Weld the cone to the cylinder with a continuous fillet weld, 4 mm leg size, inside and outside.

3. **Weld internal baffles**: Cut 4-6 flat bar baffles (10 × 50 mm, 350-400 mm long) to fit the drum interior at equal angular spacing. Weld each baffle to the drum wall with 30 mm fillet welds at each end. Baffle orientation: angled 30-45° from the drum axis to promote axial mixing (material moves toward the closed end during rotation). Ensure baffles are staggered — alternating left-hand and right-hand angles — to prevent material from migrating to one end.

4. **Fabricate trunnion rings**: Cut two rings from 6-8 mm steel plate, matching the drum outside diameter. Weld one ring near each end of the cylindrical section. These rings ride on the support rollers and transmit the drum weight to the frame. Grind the outer surface of each ring smooth and concentric with the drum axis (runout <2 mm).

5. **Install discharge chute**: Cut a rectangular opening (200 × 300 mm) in the closed end of the drum (opposite the cone). Weld a steel chute (formed from 2 mm sheet) over the opening, angled 45° downward for gravity discharge. The drum tilts to pour through this opening.

6. **Weld drive ring**: Weld a flat bar ring or sprocket mounting ring around the drum center. This provides the drive surface for the gear or chain. For chain drive: weld mounting lugs for a sprocket. For gear drive: the ring itself may be the driven gear if cast with teeth.

### Frame and Tilting Mechanism

7. **Fabricate frame**: Cut and weld the frame from 40 × 40 mm or 50 × 50 mm angle iron. The frame supports the drum via two pairs of rollers (one pair at each trunnion ring) and provides a mounting point for the crank/motor and the tilting mechanism. Frame dimensions: approximately 1200 mm long × 800 mm wide × 900 mm high (at the drum axis). Cross-brace the frame for rigidity.

8. **Mount support rollers**: Install four rollers (steel or cast iron, 50-80 mm diameter, 80-100 mm long) on shafts bolted to the frame. Two rollers per trunnion ring, positioned at 4 o'clock and 8 o'clock relative to the drum centerline. The drum rests on these rollers by gravity. Roller spacing: slightly wider than the trunnion ring width to allow the drum to rotate freely without lateral wandering. Clearance between drum and rollers: 0.5-1.0 mm.

9. **Build tilting mechanism**: Pivot the drum and roller assembly on a horizontal shaft mounted across the frame at the drum's center of gravity. The tilting shaft: 25-30 mm diameter steel rod through two pillow block bearings on the frame. Attach a lever arm (800-1000 mm long) to the tilting shaft. The operator pushes the lever to tilt the drum for discharge and pulls it back for loading. Lock the lever in the mixing position with a pin through the lever and frame.

10. **Install crank and drive**: Mount the crank shaft on the frame with two bearings. Connect the crank shaft to the drum via a gear reduction (4:1 to 6:1 ratio) or chain and sprocket. The crank handle mounts on the output shaft. Crank arm length: 250-350 mm. At a 5:1 ratio, one crank revolution rotates the drum 1/5 turn, reducing operator effort while maintaining adequate mixing speed.

### Powered Conversion

11. **Mount motor**: Bolt the motor to an adjustable slide plate on the frame. The slide plate allows belt tension adjustment. Motor position: below the drum axis, driving through a secondary shaft with a 3:1 to 4:1 reduction to the drum. Total reduction from motor to drum: 12:1 to 20:1 (1500 RPM motor → 75-125 RPM shaft → 12-20 RPM drum after all reduction stages).

12. **Install belts and guards**: Install V-belts from the motor to the intermediate shaft, and from the intermediate shaft to the drum drive. Adjust belt tension to 1-2% belt deflection under 10 N finger pressure at mid-span. Fabricate and install sheet-metal belt guards over all rotating components. Guards are mandatory — exposed belts and chains amputate fingers.

## Calibration and Verification

1. **Drum balance**: Rotate the empty drum by hand. It should turn smoothly with no binding, no more than 5 N·m of torque required at the crank (measured with a torque wrench on the crank handle). If the drum wobbles, check trunnion ring runout with a dial indicator — maximum 2 mm runout.

2. **Baffle check**: Verify all baffles are securely welded with no cracks. Strike each baffle with a hammer — a clear ring indicates solid weld; a rattle indicates a cracked weld requiring repair.

3. **Water leak test**: Fill the drum with 50 L of water. Rotate the drum slowly. Inspect all seams for leaks. No leaks acceptable — water leaks during operation indicate future cement paste leaks. Reweld any leaking seams and retest.

4. **Mix uniformity test**: Load a test batch (40 L dry volume: cement, sand, and aggregate in design proportions). Add water to the specified water-cement ratio. Mix for 3 minutes (hand crank) or 2 minutes (powered). Discharge onto a clean surface and examine: the batch should be uniform in color and consistency with no pockets of dry cement or segregated aggregate. If the mix is non-uniform, increase mixing time or adjust baffle angles.

5. **Tilt mechanism test**: Load the drum with the maximum batch weight (200 L of concrete ≈ 480 kg). Attempt to tilt for discharge. The lever force should not exceed 150 N (≈15 kg) at the lever end. If higher, adjust the pivot point closer to the center of gravity.

## Expected Performance

| Parameter | Hand-Cranked (200 L) | Powered (200 L) |
|-----------|:--------------------:|:---------------:|
| Batch volume | 150-200 L (0.15-0.20 m³) | 150-200 L |
| Mix cycle time | 3-5 minutes | 2-3 minutes |
| Output per hour | 1.5-3.0 m³ | 3-5 m³ |
| Drum rotation speed | 15-25 RPM (crank speed dependent) | 12-20 RPM |
| Maximum aggregate size | 40 mm | 40 mm |
| Discharge time | 30-60 seconds (tilt and pour) | 30-60 seconds |
| Operator effort | 1 person cranking continuously, 1 person loading | 1 person loading and operating |
| Weight (empty) | 200-350 kg | 250-400 kg |
| Drive power | Manual (≈150 W sustained) | 1.5-3.0 kW electric or 5-8 HP engine |
| Drum wall life | 5-10 years (concrete abrasion) | 5-10 years |
| Bearing life | 1-2 years (grease monthly) | 1-2 years |

## Strengths

- Produces consistent, homogeneous concrete — superior to hand mixing on a board in both strength and uniformity
- Tilting drum design is simple to build and maintain — no internal moving parts beyond baffles
- Hand-cranked version requires no power supply — usable on remote construction sites
- Scales directly: larger drums produce more concrete per batch with the same mechanism

## Weaknesses

- Limited to batch mixing — not continuous. A construction site needing >5 m³/hour requires multiple mixers or a larger unit
- Drum abrasion from aggregate gradually wears the steel wall — 5-10 year drum life before replacement
- Hand-cranked mixing is physically demanding at 150 W sustained output — operator fatigue limits daily output
- Cleaning is essential — leftover concrete hardens in the drum, reducing effective volume and damaging baffles. Wash immediately after each use

## Safety

- **Pinch points**: The drum-to-roller contact point and the gear/chain drive are primary pinch hazards. Install guards over all drive components. Never reach into the drum while it is rotating.
- **Heavy load**: A 200 L batch of wet concrete weighs approximately 480 kg. The mixer must be on stable, level ground before loading. An overloaded mixer can tip over during tilting.
- **Dust**: Loading dry cement produces respirable dust containing crystalline silica. Wear a dust mask (minimum P2/N95) during loading. Position the mixer upwind of the loading point.
- **Electrical hazard** (powered version): Motors and switches near water (concrete mixing) are an electrocution risk. Use ground-fault circuit interrupters (GFCI). Keep electrical connections above the mixing zone. Route cables away from water splash zones.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Concrete not mixing uniformly | Baffles broken or missing, drum speed too low | Inspect and re-weld baffles; increase crank speed to maintain 15-25 RPM |
| Drum difficult to turn | Overloaded, bearings failing, trunnion rings misaligned | Reduce batch size to rated capacity; replace bearings; realign trunnion rings |
| Concrete leaking from seams | Weld cracks in drum shell | Drain, clean, and reweld seams; test with water before returning to service |
| Motor stalling (powered) | Overloaded, belt slipping, motor undersized | Reduce batch size; tighten belts; verify motor rating ≥1.5 kW for 200 L drum |
| Drum wobbles during rotation | Trunnion ring not concentric, frame bent, rollers worn | Measure runout with dial indicator; replace worn rollers; shim frame to level |
| Material sticks to drum wall | Insufficient water, drum not cleaned after previous batch | Adjust water-cement ratio; clean drum immediately after each use — hardened concrete is extremely difficult to remove |

## Variations and Alternatives

- **Tilting drum vs. non-tilting drum**: Tilting drums discharge by tilting the entire drum, which is simpler to build. Non-tilting drums use an internal screw or reverse rotation to discharge, which is more complex but allows higher discharge points.
- **Hand-cranked vs. powered**: Hand-cranked is appropriate for output <3 m³/hour (small foundations, masonry work). Powered mixers are justified for continuous pours (floor slabs, road paving) where output >3 m³/hour is needed.
- **Transit mixer (truck-mounted)**: A large-scale variant where the mixing drum is mounted on a truck chassis. Not a construction-site build — requires truck chassis, hydraulic drive, and large drum fabrication.
- **Pan mixer**: A stationary pan with rotating blades (instead of rotating drum). Better for stiff, low-slump concrete mixes. More complex to build (sealed pan bottom, blade drive shaft through pan wall).

## See Also

- [Cement & Concrete](../chemistry/cement.md) — concrete mix design, water-cement ratio, and curing
- [Industrial Buildings](./industrial-buildings.md) — heavy-duty concrete construction requiring mixer output
- [Road & Bridge Construction](../transport/roads.md) — road paving requiring continuous concrete supply
- [Iron & Steel](../metals/iron-steel.md) — steel for drum, frame, and drive components
- [Machine Tools](../machine-tools/index.md) — turning and boring for shafts and bearings

---

*Part of the [Bootciv Tech Tree](../index.md) · [Construction](./index.md) · [All Domains](../index.md)*
