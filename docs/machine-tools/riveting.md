# Riveting

> **Node ID**: machine-tools.joining.riveting
> **Domain**: [Machine Tools Bootstrap](./index.md)
> **Dependencies**: [`machine-tools.machining`](machining.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Timeline**: Years 10-30
> **Outputs**: riveted_joints
> **Critical**: No — mechanical joining with permanent fasteners


Riveting is mechanical joining with no heat applied to the joint itself. Rivets are installed hot or cold through holes in overlapping plates, then the second head is formed by hammering. Riveted joints dominated structural steel construction (bridges, ships, boilers) from ~1840 until arc welding replaced them after ~1940. For welding processes, see [Welding](./welding.md). For filler alloy joining, see [Brazing & Soldering](./brazing-soldering.md). For the parent overview, see [Metal Joining](./joining.md).

## Rivet Types and Materials

- **Material**: Wrought iron or mild steel rivets (matching the structure being joined). Copper rivets for copper structures. For boilers and pressure vessels, steel rivets of known composition.
- **Sizes**: Shank diameter 6-25 mm for structural work. Length = grip thickness (total plate thickness) + 1.5× shank diameter (to form the second head).
- **Hot riveting**: Heat rivet to bright red (~900-1000°C). Insert into hole. Hold manufactured head with a dolly (heavy steel bar held by helper). Hammer the protruding shank to form the second head (use a snap — a shaped tool that forms a hemispherical head). As the rivet cools, it contracts, clamping the plates together with enormous force. This contraction-induced clamping is the key advantage of hot riveting — produces a preload that makes the joint leak-tight and resistant to vibration loosening.
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

- **Lap joint**: Two plates overlap, single row of rivets through both. Simplest. Used for thin sheet and non-structural work.
- **Butt joint with cover plates**: Two plates butted edge-to-edge, with a cover plate (gusset) on one or both sides, riveted through. Double-cover butt joint is the strongest riveted configuration — used for bridge chords and boiler seams.
- **Rivet patterns**: Chain riveting (rivets in straight lines), zig-zag riveting (staggered — stronger, less tendency to tear along a line of holes). Pitch (rivet spacing): typically 3-5× rivet diameter. Edge distance: minimum 1.5× rivet diameter from center of hole to plate edge.
- **Boiler joints**: Longitudinal seams use double-riveted double-cover butt joints. Circumferential seams use single-riveted lap joints (lower stress on circumferential seam — hoop stress is double longitudinal stress, so the longitudinal seam must be stronger).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Hot-driven rivet loose (dull thud on 200 g hammer tap test) | Rivet cooled below 500°C before second head fully formed, or drift pin misalignment left gap >0.3 mm between plates | Drive rivet faster (2-4 blows before cooling below 500°C); heat rivet to bright red 900-1000°C; verify plates in full contact with feeler gauges before driving; re-heat and re-drive loose rivets after removal |

## Cross-References

- [Welding](./welding.md) — fusion and solid-state welding processes
- [Brazing & Soldering](./brazing-soldering.md) — filler alloy joining methods
- [Metal Joining](./joining.md) — parent overview of all joining methods
- [Iron & Steel](../metals/iron-steel.md) — rivet materials
- [Machining](machining.md) — drilling rivet holes
- [Metal Forming](./forming.md) — forming rivet heads

---

*Part of the [Bootciv Tech Tree](../index.md) · [Machine Tools Bootstrap](./index.md) · [All Domains](../index.md)*