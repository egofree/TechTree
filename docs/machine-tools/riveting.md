# Riveting

> **Node ID**: machine-tools.joining.riveting
> **Domain**: [Machine Tools Bootstrap](./index.md)
> **Dependencies**: [`machine-tools.machining`](machining.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Timeline**: Years 10-30
> **Outputs**: riveted_joints
> **Critical**: No — mechanical joining with permanent fasteners

Riveting is mechanical joining with no heat applied to the joint itself. Rivets are installed hot or cold through holes in overlapping plates, then the second head is formed by hammering. Riveted joints dominated structural steel construction (bridges, ships, boilers) from ~1840 until arc welding replaced them after ~1940. For welding processes, see [Welding](./welding.md). For filler alloy joining, see [Brazing & Soldering](./brazing-soldering.md). For the parent overview, see [Metal Joining](./joining.md).

**Historical context**: The Golden Gate Bridge contains approximately 600,000 rivets in its towers. The RMS Titanic used over 3 million rivets in its hull. The Eiffel Tower used 2.5 million rivets. Every major steel structure built before 1940 was riveted. Riveting lost to arc welding because of labor cost, not joint quality — a well-designed riveted joint achieves 80-95% of solid plate strength, comparable to a full-penetration weld.

**Prerequisites**:
- [Iron and steel production](../metals/iron-steel.md) for rivet stock and plate material
- [Drilling capability](machining.md) for producing precise holes through plate
- Forge for heating rivets to 900-1000°C
- Rivet snap (shaped cup tool) and dolly (heavy steel bar)

**Bill of Materials**:

| Item | Specification | Quantity per 100 Rivets | Source |
|------|--------------|------------------------|--------|
| Mild steel rivets | 0.1-0.2% C, shank dia 10-25 mm | 100 | Steel wire/rod, cut to length |
| Rivet snap tool | Hardened steel, cup-shaped to match head profile | 1 per rivet size | Machined from tool steel |
| Dolly bar | Heavy steel bar, 5-10 kg | 1 | Forged steel bar |
| Drift pins | Tapered steel, matching hole diameter | 4-6 | Machined from steel rod |
| Borax or red lead | Joint sealant between plates | 0.5-2 kg | Chemical supply |
| Forge fuel | Charcoal or coal | 5-10 kg | Fuel supply |

## Why Riveting Works

![Nietmaschine - Riveting machine on display](../images/machine-tools/machine-tools_joining_riveting.jpg)

> *A riveting machine for industrial purposes in Germany.*

> *Image: Photographer: Mosbatho, CC BY 4.0*

Hot riveting exploits thermal contraction. The rivet, heated to bright red (900-1000°C), is inserted through aligned holes and hammered to form the second head while still plastic. As the rivet cools to ambient temperature, it shrinks by the thermal expansion coefficient of steel (12 × 10⁻⁶ /°C) over a temperature drop of ~880°C. For a 20 mm diameter rivet with a grip length of 30 mm, this contraction generates a clamping force of 20-50 kN, pulling the plates into intimate contact.

This contraction-induced preload is why hot riveted joints are both leak-tight and resistant to vibration loosening. The clamping force from a single 20 mm rivet is equivalent to tightening a 20 mm bolt to roughly 60-70% of its proof load. Unlike bolts, which can loosen under cyclic vibration as the nut backs off, a rivet has no thread to unwind. The preload can only relax if the rivet yields in tension, which requires a force exceeding the rivet material's yield strength applied perpendicular to the joint plane.

The reason rivets were replaced by welding is not that riveted joints are weaker. A well-designed double-riveted double-cover butt joint achieves 80-95% of the solid plate strength, comparable to a full-penetration weld. Riveting lost to welding because it is far more labor-intensive: each rivet requires two workers (one hammering, one holding the dolly), preheating, and rapid driving before the rivet cools. Arc welding allows a single operator to join continuously at higher speed with less labor.

## Rivet Types and Materials

- **Material**: Wrought iron or mild steel rivets (matching the structure being joined). Copper rivets for copper structures. For boilers and pressure vessels, steel rivets of known composition.
- **Sizes**: Shank diameter 6-25 mm for structural work. Length = grip thickness (total plate thickness) + 1.5× shank diameter (to form the second head).
- **Hot riveting**: Heat rivet to bright red (~900-1000°C). Insert into hole. Hold manufactured head with a dolly (heavy steel bar held by helper). Hammer the protruding shank to form the second head (use a snap — a shaped tool that forms a hemispherical head). As the rivet cools, it contracts, clamping the plates together with enormous force. This contraction-induced clamping is the key advantage of hot riveting.
- **Cold riveting**: Drive rivet at room temperature with hammer or hydraulic riveter. No contraction clamping. Weaker joint. Used for small rivets (<10 mm) and non-critical applications. Aluminum and copper rivets are typically driven cold.

## Construction Steps for a Hot-Riveted Structural Joint

1. Drill matching holes through both plates. Hole diameter: rivet diameter + 1.0-1.5 mm clearance (for a 20 mm rivet, drill 21.0-21.5 mm hole). Deburr both sides.
2. Align the plates with drift pins in two holes at each end of the joint. Insert drift pins to hold alignment.
3. Heat rivets to bright red (900-1000°C) in a forge or portable rivet heater. One rivet at a time — they cool quickly.
4. Insert the hot rivet through the hole from the outside. Hold the manufactured head with a dolly (heavy steel bar, 5-10 kg, held against the head by a helper on the opposite side).
5. Hammer the protruding shank with a rivet snap (shaped cup tool matching the desired head profile). Two to four blows form the second head. Work quickly — the rivet must be formed before it cools below ~500°C.
6. The rivet contracts as it cools, clamping the plates with an estimated preload of 20-50 kN for a 20 mm rivet (proportional to the thermal contraction from 900°C to ambient).

**Calibration**: Inspect each rivet head — must be full-formed, concentric, and tight against the plate surface. Tap each rivet with a 200 g hammer: a tight rivet rings clearly, a loose rivet produces a dull thud and may vibrate. Reject and replace any loose rivets. Measure grip with feeler gauges — plates must be in full contact with no gaps >0.3 mm between rivets.

**Expected performance**: Single rivet shear strength: 80-150 MPa (depending on rivet material). Plate bearing stress: 200-400 MPa. Joint efficiency (riveted vs. solid plate): 55-75% for single-riveted lap joints, 80-95% for double-riveted double-cover butt joints. Contraction preload: 20-50 kN for 20 mm rivet.

**Materials specifications**: Mild steel rivets (0.1-0.2% C, shank diameter 6-25 mm, length = grip + 1.5× diameter), rivet snap (hardened steel, shaped to hemispherical head profile), dolly (heavy steel bar, 5-10 kg), drift pins (tapered steel, matching rivet hole diameter), forge for heating rivets.

## Strengths

- No heat applied to the plates being joined — no metallurgical changes, no distortion of the parent metal
- Hot rivets contract on cooling, producing a preload that resists vibration loosening and creates leak-tight joints
- Riveted joints are inspectable — a trained inspector can detect loose rivets by tap testing

## Weaknesses

- Holes reduce the effective cross-section of the plates by 15-25%, weakening the structure
- Two-person operation minimum (one hammers, one holds the dolly) — labor-intensive
- Rivets cannot be disassembled without destructive removal (chiseling or drilling out)

## Joint Configurations

- **Lap joint**: Two plates overlap, single row of rivets through both. Simplest. Used for thin sheet and non-critical work.
- **Butt joint with cover plates**: Two plates butted edge-to-edge, with a cover plate (gusset) on one or both sides, riveted through. Double-cover butt joint is the strongest riveted configuration — used for bridge chords and boiler seams.
- **Rivet patterns**: Chain riveting (rivets in straight lines), zig-zag riveting (staggered — stronger, less tendency to tear along a line of holes). Pitch (rivet spacing): typically 3-5× rivet diameter. Edge distance: minimum 1.5× rivet diameter from center of hole to plate edge.
- **Boiler joints**: Longitudinal seams use double-riveted double-cover butt joints. Circumferential seams use single-riveted lap joints (lower stress on circumferential seam — hoop stress is double longitudinal stress, so the longitudinal seam must be stronger).

### Joint Efficiency by Configuration

| Configuration | Efficiency | Application |
|---------------|-----------|-------------|
| Single-riveted lap | 55-60% | Thin sheet, tanks, ducts |
| Double-riveted lap | 65-75% | Medium-load structural joints |
| Single-riveted butt with single cover | 60-70% | Medium-pressure vessels |
| Double-riveted double-cover butt | 80-95% | Bridge chords, boiler longitudinal seams |
| Triple-riveted double-cover butt | 85-95% | Highest-efficiency riveted joint |

Efficiency is the ratio of joint strength to solid plate strength. The remaining 5-20% weakness comes from the holes reducing the plate cross-section and the shear/bearing failure modes of the rivets themselves.

### Minimum Dimensions by Rivet Size

| Rivet Diameter | Min. Edge Distance | Min. Pitch | Hole Diameter | Preload (hot) |
|---------------|-------------------|------------|---------------|----------------|
| 10 mm | 15 mm | 30-50 mm | 11.0-11.5 mm | 5-12 kN |
| 13 mm | 20 mm | 40-65 mm | 14.0-14.5 mm | 8-20 kN |
| 16 mm | 24 mm | 48-80 mm | 17.0-17.5 mm | 12-30 kN |
| 20 mm | 30 mm | 60-100 mm | 21.0-21.5 mm | 20-50 kN |
| 25 mm | 38 mm | 75-125 mm | 26.0-26.5 mm | 30-75 kN |

## Scaling Notes

Riveting production scales from two-person crews to industrial operations:

- **Workshop scale** (2-4 workers): A forge for heating rivets, hand hammers (2-4 kg), snap tools, and dolleys. One person heats and inserts rivets, one holds the dolly, one hammers. Production: 20-50 rivets per hour. Adequate for small structures, tanks, and repair work.

- **Bridge/ship scale** (10-50 workers): Multiple riveting crews working in sequence. Portable rivet heaters (gas-fired). Pneumatic riveting hammers (if compressed air available) replace hand hammers, tripling driving speed. A 20-person crew drives 200-500 rivets per day. This scale built the Eiffel Tower (2.5 million rivets), the RMS Titanic (3 million rivets), and every steel bridge before 1940.

- **Industrial scale** (hydraulic riveting): Hydraulic riveting machines apply controlled force (50-200 kN) to form the second head, replacing the hammer operator. Consistent head quality, less noise, faster production. Used in boiler shops and structural steel fabrication. Production: 500-1000 rivets per day per machine.

**Critical constraint**: Riveting is inherently labor-intensive. Each rivet requires drilling a hole, heating a rivet, inserting it, and forming the head — all before the rivet cools. Arc welding replaced riveting not because welded joints are stronger, but because a single welder can lay a continuous bead at 2-5 m/min, replacing dozens of rivets with a single pass. In a bootstrap civilization, riveting remains the primary structural joining method until arc welding equipment is available.

## Quality Control

Riveted joints are verified by visual, mechanical, and dimensional inspection:

1. **Visual inspection**: Each rivet head must be full-formed, concentric, and tight against the plate surface. Reject rivets with cracked heads, uneven formation, or visible gaps between head and plate. Inspect from both sides — the manufactured head and the driven head must both be sound.

2. **Tap testing**: The primary field inspection method. Strike each rivet with a 200 g hammer. A tight rivet rings clearly (high-frequency metallic ring). A loose rivet produces a dull thud and may vibrate visibly. Mark all loose rivets with paint for removal and replacement. Tap testing requires training — experienced inspectors can distinguish loose rivets from tight ones with >95% accuracy.

3. **Dimensional inspection**: Measure rivet head diameter (should be 1.5× shank diameter ±5%). Measure rivet head height (should be 0.4× shank diameter ±10%). Check plate gap between rivets with feeler gauges (must be <0.3 mm). Verify edge distance (minimum 1.5× rivet diameter from hole center to plate edge).

4. **Sample destructive testing**: For critical applications (boiler seams, bridge chords), drive extra test rivets using the same procedure, then cut cross-sections for metallographic examination. Verify rivet fills the hole completely with no voids, and the driven head has adequate grain flow (indicating proper forming temperature).

5. **Proof loading**: For structural joints, apply 1.5× design load and verify no rivet slip, plate separation, or permanent deformation. This is the ultimate acceptance test for bridge and boiler joints.

## Safety Considerations

Riveting involves hot metal, heavy tools, and overhead work. The combination creates hazards specific to the riveting process that differ from other joining methods.

- **Burns from hot rivets**: Rivets heated to 900-1000°C cause immediate deep burns on skin contact. The rivet remains above 500°C for 20-30 seconds after removal from the forge, which is still hot enough for second-degree burns. Use tongs for all handling. The dolly holder's hands are 200-300 mm from the hot rivet head — leather gloves are mandatory.
- **Hammer injuries**: Missed strikes with the 2-4 kg riveting hammer cause hand and finger fractures. The dolly (5-10 kg steel bar) can slip and strike the helper's hands or feet. Both workers need leather gloves with reinforced palms. Strike accuracy matters: a glancing blow sends the snap tool spinning.
- **Eye injury from rivet fragments**: When a rivet snap tool slips off the partially formed head, the hammer strikes bare steel, producing sharp metal fragments. Safety glasses with side shields are mandatory. During head formation, small sparks and scale flakes eject from the joint zone.
- **Overhead rivet hazard**: In ship and bridge construction, rivets are often driven overhead. A dropped hot rivet (even a 10 mm rivet weighs 10-15 g at 900°C) causes serious burns on the face, neck, and shoulders of workers below. Cotton or wool clothing (not synthetic, which melts) and a cloth cap under the hard hat provide protection. Rivet catchers (canvas funnels at the hole) prevent dropped rivets from falling through.
- **Noise exposure**: Hammering on steel produces impulse noise levels of 110-120 dB. A full day of structural riveting causes permanent hearing damage without protection. Earplugs or earmuffs are mandatory. The ringing sound used to test rivet tightness (200 g hammer tap) is also the sound that damages hearing during the driving operation.
- **Crush injuries from plate alignment**: Drift pins are driven into holes to align heavy steel plates. If the plates shift during alignment, fingers caught between plates are crushed or severed. Never place hands between plates being aligned. Use drift pins and clamps, not fingers, to position plates.

### Personal Protective Equipment

- Safety glasses with side shields at all times during riveting operations
- Leather gloves with reinforced palms for both hammer operator and dolly holder
- Long-sleeved cotton or wool shirt (no synthetic fabrics that melt onto skin)
- Hard hat with cloth cap liner for overhead riveting work
- Steel-toe boots for handling heavy plates, dolleys, and rivets
- Hearing protection (earplugs or earmuffs) during hammering operations
- Leather apron when heating rivets in the forge

### Emergency Procedures

- Keep a bucket of cold water within arm's reach for immediate cooling of burns from hot rivets
- Post a first aid station with burn treatment supplies at every riveting location
- Train both workers in the riveting pair on communication: the hammer operator must be able to see and hear the dolly holder at all times. Stop immediately if visual contact is lost.
- Establish a "heads up" call system when riveting overhead: the person inserting the rivet calls "heads up" before pushing it through, and workers below clear the area.
- Keep fire watch for 30 minutes after riveting near combustible materials (timber scaffolding, roofing) — scale and sparks from the forge can smolder.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Hot-driven rivet loose (dull thud on 200 g hammer tap test) | Rivet cooled below 500°C before second head fully formed, or drift pin misalignment left gap >0.3 mm between plates | Drive rivet faster (2-4 blows before cooling below 500°C); heat rivet to bright red 900-1000°C; verify plates in full contact with feeler gauges before driving; re-heat and re-drive loose rivets after removal |
| Rivet head not fully formed (flat or asymmetrical) | Insufficient blows, wrong snap tool size, or rivet cooled too fast | Use correct snap tool for rivet diameter; apply 3-5 firm blows within 10 seconds of insertion; preheat snap tool to reduce heat extraction from rivet |
| Plates not in contact (gap >0.3 mm measured with feeler gauge) | Drift pins misaligned, plate surfaces not clean, or bolts not tightened before riveting | Clean plate surfaces of scale and paint; bolt plates together tightly before riveting; verify alignment with straightedge and feeler gauges |
| Rivet hole elongation or tearing at plate edge | Edge distance too small (<1.5× rivet diameter) or rivet pitch too close | Maintain minimum edge distance of 1.5× rivet diameter from hole center to plate edge; maintain pitch of 3-5× rivet diameter |
| Rivet head cracking after driving | Rivet material too hard (high carbon content >0.25%) or quenched by cold plates | Use mild steel rivets (0.1-0.2% C); preheat plates in cold weather below 5°C to prevent rapid quenching of rivet; do not drive rivets when ambient temperature is below -5°C |
| Shearing of rivets in service | Joint overloaded or rivet diameter too small for the applied shear force | Calculate required rivet count: shear force per rivet = total joint force / number of rivets; must be below 80-150 MPa shear stress depending on rivet material |
| Corrosion around rivet heads | Moisture ingress between plates (no sealant) or dissimilar metal contact | Apply red lead or tar between plates during assembly; use matching rivet and plate materials; inspect and paint riveted joints regularly |
| Rivet spinning in hole (head turns when tapped) | Hole too large (>1.5 mm oversize) or rivet too short for the grip | Use correct hole diameter (rivet diameter + 1.0-1.5 mm); select rivet length = grip + 1.5× diameter; ream oversize holes and use larger rivets if needed |

## Scaling Notes

Riveting scales from individual workshop practice to industrial production:

- **Workshop scale** (1-10 joints/day): Hand-driven rivets with a sledgehammer (2-4 kg) and snap set. Forge rivets from bar stock or purchase pre-made. Pneumatic or hydraulic riveting guns not required. Adequate for structural repair, small bridges, and tank fabrication. One skilled riveter + one heater + one helper.

- **Shipyard scale** (100-1,000 rivets/day): Portable pneumatic riveting hammers (0.6-1.0 MPa compressed air). Multiple heater forges feeding rivets to teams. Pneumatic hydraulic squeezers for consistent shop rivets. 10-50 workers in riveting teams. This was the dominant method for shipbuilding and bridge construction from 1850-1940.

- **Factory scale** (5,000-50,000 rivets/day): Automated rivet feeding and squeezing machines for aircraft and structural steel production. Quality control via ultrasonic inspection of every joint. Statistical process control on rivet hole tolerance and clamp-up force. This scale supports mass production of aircraft, bridges, and pressure vessels.

**Key bottleneck**: Heating and driving speed. A rivet must be driven within 10-15 seconds of removal from the forge. Beyond this, the rivet cools below forging temperature (~500°C) and will not fill the hole properly. Large rivets (>25 mm diameter) require two workers with sledgehammers or a pneumatic hammer.

## Safety & Hazards

- **Burns**: Rivets at 900-1000°C cause severe burns on contact. Use tongs to handle hot rivets. Wear leather gloves and heavy canvas aprons. Mark hot rivet storage areas with barriers.
- **Noise**: Pneumatic riveting hammers produce 110-130 dB. Mandatory hearing protection (earmuffs rated NRR 25+). Limit exposure to 30-minute sessions with 15-minute breaks.
- **Eye injuries**: Flying rivet heads (snapped-off shop heads), hammer spatter, and metal chips from drilling. Mandatory safety glasses with side shields; face shields for overhead riveting.
- **Crush injuries**: Sledgehammers (2-4 kg) used for hand riveting can fracture bones on miss-strikes. Maintain clear swing path. Bucking bar (the dolly held against the rivet tail) can pinch fingers — use properly sized bar with handle.
- **Fall hazards**: Structural steel riveting occurs at heights. Riveter and heater must be tied off to independent lifelines.

## See Also

- [Welding](./welding.md) — fusion and solid-state welding processes that replaced riveting
- [Brazing & Soldering](./brazing-soldering.md) — filler alloy joining methods
- [Metal Joining](./joining.md) — parent overview of all joining methods
- [Iron & Steel](../metals/iron-steel.md) — rivet materials
- [Machining](machining.md) — drilling rivet holes
- [Metal Forming](./forming.md) — forming rivet heads
- [Lubricants](../chemistry/lubricants.md) — sealant compounds for riveted joints

---

*Part of the [Bootciv Tech Tree](../index.md) · [Machine Tools Bootstrap](./index.md) · [All Domains](../index.md)*
