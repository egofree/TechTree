# Hoist & Winch

> **Node ID**: construction.hoist-winch
> **Domain**: [Construction](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`textiles.rope-making`](../textiles/rope-making.md)
> **Enables**: [`construction.crane`](./crane.md), [`construction.industrial-buildings`](./industrial-buildings.md), [`mining`](../mining/index.md)
> **Timeline**: Years 8-20
> **Outputs**: lifting_force, hauling_force
> **Critical**: Yes — mechanical lifting and pulling are fundamental to all construction, mining, and industrial operations above hand-carry capacity

## Principle

A winch converts rotational force (from a hand crank or motor) into linear pulling force by winding rope or cable around a drum. The mechanical advantage comes from the leverage ratio between the crank arm and the drum radius. A crank arm of 300 mm turning a drum of 100 mm radius gives a 3:1 force advantage — a 100 N push on the crank produces 300 N of pull on the rope. Combined with a ratchet and pawl mechanism, the winch holds loads in any position without continuous operator effort.

A hoist adds a pulley system (block and tackle) to the winch for vertical lifting. A single fixed pulley changes direction without adding force. A block and tackle with N rope segments between pulleys multiplies the lifting force N× while dividing the lifting speed by N. A 4-sheave block and tackle (4 rope segments) on a 5 kN winch lifts 20 kN (≈2 tonnes) at one-quarter the rope speed.

## Materials

### Hand-Cranked Winch (5 kN rated)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel bar (drum) | 10-15 kg | 100-150 mm diameter solid or thick-walled tube, 200-300 mm long | [Iron & Steel](../metals/iron-steel.md) | Hardwood drum on iron shaft (lower capacity, ≈2 kN) |
| Steel shaft | 5-8 kg | 30-40 mm diameter, 500-600 mm long, turned | [Iron & Steel](../metals/iron-steel.md) | Forged square shaft (needs bored drum) |
| Steel plate (frame) | 15-25 kg | 6-10 mm thick, for side plates and base | [Iron & Steel](../metals/iron-steel.md) | Timber frame with iron straps |
| Ratchet and pawl | 1 set | Forged steel, ratchet teeth 8-12 mm pitch | [Forging](../metals/forging.md) | Worm gear (self-locking, higher friction) |
| Crank handle | 1 | Forged steel, 250-350 mm arm, with grip | [Forging](../metals/forging.md) | Timber handle with iron ferrule |
| Bearings | 4 | Plain journal bearings, 30-40 mm bore, bronze or oil-impregnated iron | [Bearings](../machine-tools/bearings-abrasives.md) | Hardwood bearings with heavy grease |
| Rope | 20-50 m | Manila or hemp, 16-25 mm diameter, breaking strength ≥25 kN | [Rope Making](../textiles/rope-making.md) | Wire rope (requires specialized splicing) |
| Bolts and nuts | 2-4 kg | M12-M16, grade 8.8 | [Fasteners](../metals/fasteners.md) | Riveted joints |

### Block and Tackle (for hoisting, adds to winch)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Sheave pulleys | 2-4 | 100-150 mm diameter, turned from hardwood or cast iron, with groove for rope | [Machine Tools](../machine-tools/index.md) | None — pulleys are essential for mechanical advantage |
| Pulley pins | 2-4 | 15-20 mm steel rod, 100-150 mm long | [Iron & Steel](../metals/iron-steel.md) | Hardwood dowels (weaker) |
| Pulley blocks | 2 | Steel or hardwood housings for pulleys | [Iron & Steel](../metals/iron-steel.md) | Timber blocks with iron straps |
| Hook or shackle | 1-2 | Forged steel, rated ≥2× working load | [Forging](../metals/forging.md) | Rope sling (slower to attach) |

## Construction Steps

### Winch Drum

1. **Turn the drum**: Mount a solid steel bar (100-150 mm diameter) in the lathe. Turn the outer surface to a consistent diameter (±0.5 mm over the full length). Cut a rope groove: turn a shallow channel (2-3 mm deep, matching the rope diameter) in a spiral pattern along the drum length. This guides the rope to wind evenly and prevents overlapping. If a spiral groove is impractical, turn the drum with a slight barrel shape (1-2 mm larger at center than at ends) to encourage center-first winding.

2. **Bore the drum**: Drill or bore the drum through its center axis for the shaft. Bore diameter: 0.05-0.10 mm larger than the shaft diameter for a sliding fit. If using a solid bar, drill 30-35 mm through the full 200-300 mm length. Ream to final diameter for smooth bearing surface.

3. **Key the drum to shaft**: Cut a keyway (5 × 5 mm for a 30 mm shaft) in the drum bore and on the shaft. Fabricate a steel key (5 × 5 × 40 mm) for a press fit. The key prevents the drum from rotating independently of the shaft under load.

### Frame and Bearings

4. **Cut frame side plates**: Cut two side plates from 8-10 mm steel plate, each approximately 200 × 400 mm. Mark and drill bearing bores (30-40 mm) at the drum shaft location and the crank shaft location (if separate). Bearing bore tolerance: ±0.1 mm for journal bearings. Drill mounting holes for the ratchet mechanism and base plate.

5. **Install bearings**: Press journal bearings (bronze bushings) into the side plate bores. Bearing outer diameter: interference fit (0.02-0.05 mm larger than the bore). If pillow block bearings are used, bolt them to the side plates with the bearing centers aligned to ±0.5 mm.

6. **Assemble drum in frame**: Insert the shaft through one side plate bearing, through the drum, and into the opposite bearing. Verify the drum rotates freely with no binding. End play (axial movement): 0.5-1.0 mm. If the drum binds, shim the bearings or ream the bores.

### Ratchet and Pawl

7. **Fabricate ratchet wheel**: Forge or machine a ratchet wheel from 8-12 mm steel plate. Diameter: 120-180 mm. Number of teeth: 16-24 (more teeth = finer holding increments). Tooth profile: asymmetrical — steep face (≈70° from tangent) bears the load, shallow face (≈30°) allows pawl to engage. Hardness: heat-treat to 40-50 HRC for wear resistance.

8. **Mount ratchet to shaft**: Key the ratchet wheel to the drum shaft (same keyway as the drum, or a separate keyway on the same shaft). The ratchet must be pinned to the shaft so it cannot rotate independently. Secure with a setscrew or nut.

9. **Install pawl**: Pivot the pawl (forged steel, 15-20 mm wide, 80-120 mm long) on a pin bolted to one side plate. Pawl tip profile matches the ratchet tooth steep face. Gravity or a light spring holds the pawl engaged with the ratchet. Verify the pawl seats fully in each tooth with an audible click when the crank is released. The pawl must hold the full rated load without slipping — test with a 5 kN load before putting into service.

10. **Install crank handle**: Mount the crank arm (250-350 mm long forged steel) on the shaft end, on the side opposite the ratchet. Secure with a key and nut. The handle grip: a freely rotating sleeve (25-30 mm diameter tube) over the crank arm end, to prevent palm abrasion during cranking.

### Block and Tackle Assembly

11. **Turn sheave pulleys**: Mount hardwood blanks (or cast iron discs) in the lathe. Turn to 100-150 mm diameter, face flat, then cut a semi-circular groove (matching the rope diameter) around the circumference. Bore the center hole for the pin (15-20 mm diameter). Smooth all edges to prevent rope chafing.

12. **Assemble pulley blocks**: For each block (upper fixed block and lower moving block), house 1-2 sheave pulleys in a steel or hardwood housing. Insert the pins through the pulleys and housing. The pulleys must rotate freely on the pins — verify with hand spin, 5+ revolutions from a firm flick. If using multiple sheaves per block, space them 5-10 mm apart with washers on the pin.

13. **Reeve the tackle**: Thread the rope through the block and tackle. Start at the winch, pass the rope down to the moving block, up to the fixed block, and repeat for the desired number of falls (rope segments between blocks). For a 4-fall tackle: rope → fixed block sheave 1 → moving block sheave 1 → fixed block sheave 2 → moving block sheave 2 → free end (to be wound on the winch). Verify the rope runs freely through all sheaves with no crossing or twisting.

## Calibration and Verification

1. **Drum runout**: Mount a dial indicator against the drum surface. Rotate the drum by hand. Maximum radial runout: ≤1.0 mm. Excessive runout causes uneven rope winding.

2. **Ratchet holding test**: With the winch mounted securely, apply 125% of the rated load (6.25 kN for a 5 kN winch) to the rope. Release the crank. The pawl must hold the load without slipping. If the pawl disengages, increase the pawl spring tension or re-cut the ratchet teeth with steeper load faces.

3. **Free-running test**: With no load, crank the winch through 20 full revolutions. Average effort: ≤30 N at the crank handle (measured with a spring scale). Higher effort indicates bearing problems, shaft misalignment, or drum binding.

4. **Load test with block and tackle**: Apply 100% of the rated lifting load through the block and tackle. Lift the load 1 m, hold for 5 minutes, lower. Verify: no rope slip on the drum, no bearing overheating (warm is acceptable, hot is not), no frame deflection >2 mm at any point.

## Expected Performance

| Parameter | Hand-Cranked Winch | With 4-Fall Tackle |
|-----------|:------------------:|:-------------------:|
| Line pull (rope) | 5 kN (≈500 kg) | 20 kN (≈2,000 kg) lift |
| Line speed (no load) | 15-25 m/min | 4-6 m/min lift speed |
| Drum capacity (16 mm rope) | 40-60 m | 40-60 m (reduced lift height) |
| Crank effort at rated load | 80-120 N | 20-30 N (4× mechanical advantage) |
| Drum diameter | 100-150 mm | — |
| Overall weight | 25-45 kg | +10-15 kg for blocks and rope |
| Rope breaking strength (16 mm manila) | 25-35 kN | Working load: 5 kN per fall |
| Duty cycle | Intermittent — 5 min on, 2 min off | Same |
| Ratchet tooth life | 2-5 years with regular use | — |

## Strengths

- Simple, robust mechanism — a winch with ratchet and pawl has fewer than 20 parts and can be built in a small workshop
- Self-locking ratchet holds loads indefinitely without operator effort — essential for safe lifting
- Block and tackle provides scalable mechanical advantage without modifying the winch — add more sheaves for heavier loads
- Hand-cranked version works without any power supply — usable anywhere rope can reach

## Weaknesses

- Slow lifting speed — hand-cranked winches lift at 4-6 m/min with tackle, compared to 10-30 m/min for powered hoists
- Rope is the weak link — manila and hemp ropes degrade with UV exposure, moisture, and abrasion. Inspect before each use. Replace any rope with >10% broken fibers in any 1 m length
- No overload protection — a hand winch will keep taking force until something breaks (rope, ratchet tooth, frame). The operator must gauge the load and stop before failure
- Rope drum capacity is limited — 40-60 m of 16 mm rope is the practical limit for a hand winch drum. Longer lifts require larger drums or reeving systems

## Safety

- **Rope failure**: Rope under tension stores energy proportional to the load. A rope breaking under 5 kN of tension snaps back violently. Never stand in the line of a tensioned rope. Inspect the entire rope length before each lifting operation.
- **Load drop**: If the pawl disengages or the rope breaks, the load falls. Never stand or walk under a suspended load. Use tag lines to control loads from a safe distance.
- **Pinch points**: The drum-to-frame gap, the ratchet-to-pawl engagement point, and the sheave-to-block gap are all pinch hazards. Keep hands clear of rotating parts during operation.
- **Winch mounting**: The winch must be anchored to a structure capable of holding 2× the rated load. A 5 kN winch must be bolted to a frame or post that can resist a 10 kN pull without moving. Verify anchorage before every lift.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Rope winds unevenly (overlaps, bunches) | No groove on drum, drum too narrow for rope length | Cut spiral groove in drum; use wider drum; guide rope by hand during first few wraps |
| Ratchet slips under load | Pawl not seating fully, teeth worn, spring weak | Check pawl pivot for binding; file teeth to restore profile; replace pawl spring; re-harden ratchet wheel |
| Excessive crank effort | Bearings dry, shaft bent, drum overloaded | Lubricate bearings; check shaft with straightedge; reduce load to rated capacity |
| Rope slips on drum under load | Insufficient wraps (minimum 4 wraps needed for friction grip), drum surface too smooth | Ensure ≥4 wraps of rope on drum before applying load; score drum surface lightly for friction |
| Pulleys squeak or resist rotation | Pins dry, pulley bore worn oval | Lubricate pin with grease; re-bore pulley and install bushing; replace worn pulleys |
| Load drifts down when crank is held | Ratchet tooth worn on one side, pawl not fully engaging | Inspect ratchet teeth for uneven wear; replace ratchet wheel if teeth are rounded; verify pawl spring tension |

## Variations and Alternatives

- **Hand-cranked vs. worm-gear winch**: Worm-gear winches are self-locking (no ratchet needed) but have lower efficiency (40-60% vs. 80-90% for spur gears). The worm gear is harder to build but provides inherent load-holding safety.
- **Chain fall (chain hoist)**: Uses roller chain instead of rope, with a differential pulley mechanism for very high mechanical advantage (10-40×). Slower but more compact than a winch with block and tackle. Requires precision chain manufacturing.
- **Powered winch**: Replaces the hand crank with an electric motor (0.5-2 kW) and gearbox. Same drum and ratchet mechanism. Motor drives through a friction clutch that slips at 110% of rated load, providing overload protection that hand winches lack.

## See Also

- [Crane](./crane.md) — cranes use winches for hoisting and slewing
- [Building Materials](./building-materials.md) — timber framing construction using hoisting systems
- [Rope Making](../textiles/rope-making.md) — rope specifications, splicing, and strength ratings
- [Iron & Steel](../metals/iron-steel.md) — steel for frame, drum, and ratchet components
- [Mining](../mining/index.md) — mine hoists for vertical shafts using similar winch principles

---

*Part of the [Bootciv Tech Tree](../index.md) · [Construction](./index.md) · [All Domains](../index.md)*
