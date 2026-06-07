# Wire Drawing Die (Draw Plate)

> **Node ID**: machine-tools.wire-drawing-die
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](machining.md)
> **Enables**: [`machine-tools.forming`](forming.md), [`energy.electricity`](../energy/electricity.md)
> **Timeline**: Years 10-20
> **Outputs**: wire, drawn_rod
> **Critical**: Yes — wire drawing produces the copper wire for generators, motors, and transformers; no substitute process exists for making long, uniform-diameter wire

## Overview

Wire drawing pulls metal rod through a hardened die with a tapered hole of precisely controlled diameter. Each die reduces the cross-section by 15-25% and elongates the wire proportionally. The die entrance bell (30° included angle) guides the metal into the bearing section (short, straight, ~1× diameter long), where the actual reduction occurs. A back-relief angle at the exit prevents the drawn wire from scoring the die. Drawing is performed cold — the metal work-hardens with each pass, increasing tensile strength by 50-100%. Annealing every 3-5 passes restores ductility for further reduction.

The draw plate is the bootstrap form of wire drawing dies: a single hardened steel plate with multiple tapered holes graduating in size from 8.0 mm down to 1.0 mm. It requires no specialized die-making equipment — only a drill, reamers, and heat treatment capability. With a draw plate and a pulling force (hand-powered for fine wire, a draw bench for heavier stock), a workshop can produce uniform-diameter wire from cast or rolled rod.

Wire drawing is a critical-path capability because copper wire is the basis of all electrical technology. Generators, motors, transformers, electromagnets, solenoids, and inductors all require copper wire in specific gauges, typically 0.5-3.0 mm diameter. No alternative process produces long, uniform-diameter wire — forging produces rod (too rough and variable), and rolling produces strip (not round). Only drawing through a die produces wire with the diameter tolerance (±0.05 mm) and surface finish needed for electrical windings. Without wire drawing, the entire [electricity](../energy/electricity.md) domain is blocked.

The draw force required depends on the material yield strength, the reduction ratio, and the friction coefficient at the die-wall interface. For annealed copper with a 20% area reduction, the theoretical draw force is approximately 15-25% of the material's yield strength times the wire cross-sectional area. Lubrication reduces the draw force by 30-50% and is essential to prevent galling — the welding of wire material to the die surface that destroys both the wire and the die in a single pass.

## Prerequisites

- [High-carbon steel](../metals/iron-steel.md) — for the die plate (must be through-hardenable to 58-62 HRC)
- [Drilling and reaming capability](machining.md) — for creating precise, tapered holes in the die plate
- [Heat treatment capability](../metals/iron-steel.md) — hardening and tempering the die plate to 58-62 HRC
- [Abrasive polishing capability](bearings-abrasives.md) — for finishing die holes to mirror smoothness
- [Metal rod or wire stock](../metals/iron-steel.md) — copper, brass, iron, or steel rod as starting material for drawing
- [Annealing furnace](foundry-equipment.md) — for inter-pass annealing of work-hardened wire

## Bill of Materials

### Draw Plate (Primary Build)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| High-carbon steel plate | 1 | 0.8-1.0% C, 15 mm thick × 100 mm × 200 mm | [Iron & Steel](../metals/iron-steel.md) | Tool steel (O1, D2 — better wear life, harder to source) |
| Tapered reamer | 1 | 30° included angle | [Machining](machining.md) | Ground and polished punch (less precise) |
| Straight reamer set | 1 set | 1.0-8.0 mm in 0.5 mm steps | [Machining](machining.md) | Precision-ground drill bits (oversized by 0.1-0.2 mm) |
| Quenching oil | 2-5 L | Mineral oil or vegetable oil | [Chemistry](../chemistry/lubricants.md) | Brine (faster cooling, higher cracking risk) |
| Abrasive paste | 1 set | 180, 320, 600, 1200 grit | [Bearings & Abrasives](bearings-abrasives.md) | Natural emery + oil (slower but functional) |
| Tapered mandrel (polishing) | 1 set | Hardwood or steel, matching die sizes | [Machining](machining.md) | Wrapped dowel with abrasive paper |

### Draw Bench (for Wire > 2 mm)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel channel (bed) | 1 | 100 × 50 × 5 mm, 2-3 m long | [Iron & Steel](../metals/iron-steel.md) | Hardwood beam (less rigid) |
| Chain | 1 | 10-15 mm pitch, 3-4 m long | [Iron & Steel](../metals/iron-steel.md) | Wire rope (less positive grip) |
| Sprocket (drive) | 1 | Matching chain pitch, hand-cranked or powered | [Machining](machining.md) | Windlass drum |
| Gripping jaw | 1 | Hardened steel jaws, spring-loaded | [Iron & Steel](../metals/iron-steel.md) | Vise grips (less secure) |
| Die holder | 1 | Steel block with mounting hole for draw plate | [Iron & Steel](../metals/iron-steel.md) | Bolted directly to bench end |

## Process Description

### Die Plate Preparation

1. **Select and prepare the plate**: Start with a flat plate of high-carbon steel (0.8-1.0% C), 15 mm thick × 100 mm × 200 mm. Mill or grind both faces flat and parallel to within 0.05 mm. The faces must be flat for uniform heat treatment and consistent die geometry.
2. **Mark hole positions**: Layout two rows of holes, spaced 15 mm apart center-to-center, 15 mm from the edges. Mark hole diameters from 8.0 mm down to 1.0 mm in 0.5 mm steps. Smaller holes toward one end; larger toward the other. A plate with 15 holes covers the range 8.0 mm to 1.0 mm in 0.5 mm increments. Mark clearly with stamps or engraving — after heat treatment, the markings must still be legible.

### Drilling and Reaming

3. **Drill undersized holes**: Drill each hole 0.3 mm undersize using a drill press. Use the appropriate drill bit for each target diameter. Maintain perpendicularity — the hole axis must be perpendicular to the plate face within 0.05 mm over the 15 mm plate thickness. Use a drill press with the plate clamped to the table, not a hand drill. Any tilt produces an elliptical die hole.
4. **Ream to final diameter**: Ream each hole to final diameter tolerance ±0.02 mm with a straight reamer. The straight section through the full plate thickness serves as the bearing land — this is where the wire is actually reduced in diameter. Use cutting oil during reaming. The reamed surface should show a smooth, uniform finish with no chatter marks.
5. **Form the entrance bell**: On one face of the plate, use a tapered reamer (30° included angle) to countersink each hole to approximately 2-3 mm depth. This creates the entrance bell that guides the wire into the bearing section. The transition from bell to bearing must be smooth and blended — a sharp step causes wire marking and increases draw force. The bell angle controls the deformation zone: 30° is standard for most metals; a smaller angle (15-20°) reduces draw force but increases the bearing contact length and friction.
6. **Form the back relief**: On the opposite face, countersink each hole with a 45° countersink to 0.5 mm depth. This prevents the drawn wire from contacting the die exit edge, which would score the wire surface and rapidly wear the die.

### Heat Treatment

7. **Harden the plate**: Heat the entire plate to 780-820°C in a furnace or forge (cherry red for 0.8-1.0% C steel). Soak for 15-20 minutes at temperature for uniform austenitization — the entire cross-section must reach temperature, not just the surface. Quench in oil (NOT water — high-carbon steel cracks in water due to excessive cooling rate). Agitate the plate during quenching to break the vapor blanket that forms around the hot metal, which insulates and causes soft spots. The plate should be fully martensitic after quenching, approximately 63-65 HRC.
8. **Temper**: Reheat to 200-250°C for 1-2 hours. This tempers the brittle martensite to 58-62 HRC while retaining most of the as-quenched hardness. The die must be hard enough to resist wear (wire drawing generates enormous contact pressures, 500-2000 MPa at the bearing) but not so hard that it chips under the shock of threading the wire. Temper at the lower end (200°C) for maximum hardness when drawing soft metals (copper, aluminum); temper at 250°C for more toughness when drawing harder metals (steel).

### Die Hole Polishing

9. **Coarse polish (180 grit)**: Wrap 180-grit abrasive paper around a tapered hardwood mandrel that matches the die hole taper. Work each hole by hand or with a low-speed drill (200-400 RPM) to remove scale and roughness from heat treatment. Use light pressure and keep the mandrel rotating to avoid producing longitudinal scratches. The goal at this stage is to remove the heat-treat oxide layer and produce a uniform matte finish.
10. **Medium polish (320 then 600 grit)**: Progress through 320 and 600 grit using the same mandrel technique. At 600 grit, the surface should appear uniformly smooth with no visible scratches. Apply light oil as a lubricant during polishing.
11. **Fine polish (1200 grit paste)**: Apply 1200-grit abrasive paste to the mandrel and polish each hole to a mirror finish. The bearing surface (straight section) must be mirror-smooth — any roughness causes galling (metal pickup on the die surface), increases draw force, and produces wire with a rough surface. Inspect with a 10× loupe: the surface should show no visible scratches, tool marks, or pitting. Run a fingernail across the bearing surface — it should glide without catching.

### Draw Bench Construction (for Wire > 2 mm)

12. **Build the bench frame**: Assemble a 2-3 m long bed from steel channel (100 × 50 × 5 mm) bolted to a heavy timber or steel stand at 800-900 mm working height. The bed must be rigid — any flex during drawing produces vibration that marks the wire and can cause breakage.
13. **Mount the die holder**: Fabricate a steel block (50 × 50 × 30 mm) with a rectangular opening matching the draw plate dimensions. Bolt the die holder to the head (front) of the bench. The draw plate slides into the holder and is secured with set screws. The die face must be perpendicular to the draw direction.
14. **Install the chain and sprocket**: Mount a sprocket at the tail (rear) of the bench, on a shaft supported by two pillow-block bearings. The chain runs along the bed from the sprocket to the front of the bench. A gripping jaw (hardened steel jaws, spring-loaded) attaches to the chain and grabs the pointed end of the wire.
15. **Add the drive**: For hand operation, mount a 400-500 mm crank handle on the sprocket shaft. For powered operation, connect a belt pulley to the sprocket shaft and drive from a motor or line shaft at 10-30 RPM. Pull force capacity: 10-50 kN depending on chain strength and drive torque.

### Drawing Procedure

16. **Point the wire**: Reduce the leading end of the rod to a point (or smaller diameter) so it can pass through the next die. Forging the end to a taper on an [anvil](anvil.md) or turning it down on a [lathe](machining.md) works. The point must be small enough to pass through the target die and long enough for the gripping jaw to grab (30-50 mm of reduced diameter).
17. **Lubricate**: Apply drawing lubricant to the wire and die entrance. For copper: soapy water or oil. For steel: soap solution, lime coating, or proprietary drawing compounds. Lubricant reduces draw force by 30-50% and dramatically extends die life. Do NOT draw dry — the wire will gall (pick up and weld to the die surface), destroying both the wire and the die.
18. **Thread and pull**: Push the pointed wire end through the die from the entrance-bell side. Grip the point with the draw bench jaw (or pliers for hand drawing). Apply steady, smooth pulling force. Do not jerk — sudden force spikes cause wire breakage. The wire should emerge from the die exit at constant speed.
19. **Anneal between passes**: Every 3-5 passes (or whenever the wire becomes noticeably stiffer and harder to draw), anneal the wire to restore ductility. Copper: heat to 350-400°C, air cool. Steel: heat to 700-750°C, cool in ashes (slow cool). Brass: heat to 450-550°C, air cool. Without annealing, work-hardening causes the wire to break during drawing.

### Calibration

20. **Pin gauge test**: Pass a precision-ground steel pin (known diameter, ±0.01 mm) through each die hole. The pin should pass through with light finger pressure — if it requires force, the die is undersized; if it falls through freely, the die is oversized. Record the actual diameter for each hole.
21. **Wire diameter measurement**: Draw a short length of copper wire through each successive die. Measure the wire diameter before and after each pass with a micrometer (0.01 mm resolution). The actual reduction should match the calculated area reduction within ±2%. If the wire diameter doesn't match the die diameter, the die may be worn or the wire may be elastic-recovering (springback).
22. **Pull force measurement**: For a reference wire diameter and material, measure the pull force with a spring scale. Normal draw force for copper: F = σ_y × A × ln(A₀/A_f), where A₀ is the initial area and A_f is the final area. If the measured force exceeds the calculated force by more than 20%, the die has excessive friction — polish the die hole further or check the entrance angle.

**Expected performance**: Area reduction per pass: 15-25%. Wire diameter tolerance: ±0.05 mm per die. Die life (soft metals): 200-500 passes. Pull force (copper, 3 mm → 2.5 mm): 5-15 kN. Minimum wire diameter (steel die): 1.0 mm.

## Quantitative Parameters

| Parameter | Value |
|-----------|-------|
| Reduction per pass | 15-25% area reduction |
| Wire diameter tolerance | ±0.05 mm per die |
| Die life (soft metals — copper, brass) | 200-500 passes before hole enlarges beyond tolerance |
| Die life (hard metals — iron, steel) | 50-200 passes |
| Pull force (copper, 3 mm → 2.5 mm) | 5-15 kN |
| Pull force (steel, 3 mm → 2.5 mm) | 15-30 kN |
| Minimum wire diameter (steel die) | 1.0 mm |
| Minimum wire diameter (tungsten carbide die) | 0.1 mm |
| Number of holes per plate | 10-20 (graduated sizes) |
| Die hardness (high-carbon steel) | 58-62 HRC |
| Entrance bell angle | 30° included (standard), 15-20° (low-friction) |
| Bearing land length | ~1× wire diameter |

### Draw Force Calculation (Copper Wire)

| Starting Dia. (mm) | Final Dia. (mm) | Area Reduction (%) | Approx. Draw Force (kN) |
|---------------------|------------------|--------------------|-----------------------|
| 8.0 | 7.0 | 23% | 12-18 |
| 5.0 | 4.5 | 19% | 5-8 |
| 3.0 | 2.5 | 31% | 5-15 |
| 2.0 | 1.5 | 44% | 4-10 |
| 1.5 | 1.0 | 56% | 2-6 |

Note: 31%+ reduction in a single pass is aggressive — normally done in two passes (3.0 → 2.65 → 2.5). Values assume annealed copper, lubricated die.

### Annealing Schedule by Material

| Material | Annealing Temperature | Hold Time | Cooling Method | Frequency |
|----------|----------------------|-----------|----------------|-----------|
| Copper (C110) | 350-400°C | 30-60 min | Air cool | Every 3-4 passes |
| Brass (C260) | 450-550°C | 30-60 min | Air cool | Every 2-3 passes |
| Low-carbon steel | 700-750°C | 30-60 min | Slow cool in ashes | Every 3-5 passes |
| High-carbon steel | 650-700°C | 30-60 min | Slow cool in ashes | Every 2-3 passes |
| Aluminum (1100) | 300-350°C | 30-60 min | Air cool | Every 2-3 passes |

### Typical Wire Drawing Sequence (8 mm Copper Rod → 1.5 mm Wire)

| Pass | Die Size (mm) | Wire Dia. After (mm) | Area Reduction (%) | Cumulative Reduction |
|------|---------------|---------------------|--------------------|---------------------|
| 1 | 7.2 | 7.2 | 19% | 19% |
| 2 | 6.4 | 6.4 | 21% | 36% |
| 3 | 5.7 | 5.7 | 21% | 49% (anneal) |
| 4 | 5.1 | 5.1 | 20% | 59% |
| 5 | 4.5 | 4.5 | 22% | 68% |
| 6 | 4.0 | 4.0 | 21% | 75% (anneal) |
| 7 | 3.5 | 3.5 | 23% | 81% |
| 8 | 3.1 | 3.1 | 22% | 85% |
| 9 | 2.7 | 2.7 | 24% | 89% (anneal) |
| 10 | 2.4 | 2.4 | 21% | 91% |
| 11 | 2.0 | 2.0 | 31% | 94% (anneal) |
| 12 | 1.8 | 1.8 | 19% | 95% |
| 13 | 1.5 | 1.5 | 30% | 96% (anneal) |

## Scaling Notes

- A single draw plate with 15 holes (8.0 mm to 1.0 mm in 0.5 mm steps) handles most bootstrap wire needs. Copper wire for electrical windings is typically 0.5-3.0 mm diameter, requiring 10-20 passes from 8 mm rod.
- For wire finer than 1.0 mm, steel dies wear too rapidly (the bearing area is tiny and contact pressure is extreme). Tungsten carbide inserts (pressed into a steel holder) extend die life 10-50×. Tungsten carbide requires powder metallurgy — a post-bootstrap capability.
- A capstan draw machine (rotating drum) enables continuous drawing of fine wire at 30-100 m/min, versus the batch process of the draw bench. The wire wraps multiple turns around the capstan drum; friction between wire and drum provides the pulling force. Build a capstan when wire demand exceeds 100 m/day.
- Multi-hole wire drawing machines pass the wire through several dies in sequence, with a capstan between each die. Each capstan runs progressively faster to match the wire elongation. These are industrial-era machines requiring precision speed control — build them when the manufacturing base can produce precision gears and bearings.
- For steel wire rope production, draw the individual wires to 0.5-2.0 mm diameter, then twist (strand) them around a core. Wire rope requires uniform wire diameter — the draw plate's ±0.05 mm tolerance is adequate.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Wire breaks during drawing | Excessive reduction per pass; wire work-hardened; die surface rough | Reduce to 15% area reduction per pass; anneal the wire; re-polish die with 1200 grit |
| Wire surface rough or scored | Die surface rough; insufficient lubrication; debris in die entrance | Re-polish die; apply more lubricant; clean die entrance before each pass |
| Wire diameter larger than die | Elastic recovery (springback); die oversized from wear | Use a smaller die; replace worn die; measure wire diameter after drawing, not before |
| Die hole enlarges rapidly | Die too soft (insufficient hardening); drawing hard material; no lubricant | Verify die hardness (58-62 HRC); apply lubricant; reduce die temperature by cooling |
| Wire galls (picks up on die surface) | No lubricant; wrong lubricant; die surface not polished enough | Apply drawing lubricant (soap solution for copper, lime coating for steel); re-polish die |
| Excessive draw force | Die entrance angle wrong; bearing land too long; die surface rough | Verify 30° entrance angle; keep bearing land at ~1× diameter; re-polish die |
| Wire has oval cross-section | Die hole drilled at an angle; plate not flat; uneven wear | Redrill and ream the die perpendicular to the plate face; flip and use the other face |
| Cannot thread wire through die | Wire point too large; point not centered; debris in die | Forge a longer, thinner point; ensure point is concentric with wire axis; clean the die |
| Wire diameter varies along length | Uneven pull speed; wire temperature variation; inconsistent lubrication | Pull at constant speed; allow wire to cool between passes; apply lubricant uniformly before each pass |
| Wire has center burst (cup-and-cone fracture) | Excessive reduction per pass (>30% area); die entrance angle too large | Reduce to 15-20% area reduction per pass; verify 30° entrance angle; anneal before the next pass |

## Safety

- **Whipping wire (snap-back)**: Wire under drawing tension stores elastic energy. If the wire breaks during drawing, the free end whips violently — a 3 mm steel wire at 20 kN tension can cause serious injury when it snaps. Stand to the side of the draw line, never in line with the wire. Wear safety glasses. Place a shield (plywood or steel plate) between the draw bench and the operator.
- **Pinch points (draw bench)**: The chain drive, sprocket, and gripping jaw create severe pinch hazards. Keep hands clear of the chain during operation. Guard the sprocket with a metal cover. Never reach into the chain path while the bench is under tension.
- **Sharp wire ends**: The pointed wire ends (for threading through dies) are sharp enough to puncture skin. Handle pointed ends with pliers or gloves, not bare hands. After drawing, cut off the pointed end with wire cutters before coiling.
- **Die plate handling**: The hardened die plate is heavy (1-2 kg) and has sharp hole edges on the entrance-bell side. Handle with care. Store in a padded box to prevent the polished die holes from being damaged by contact with other tools.
- **Hot wire (post-annealing)**: Wire fresh from the annealing furnace is at 350-750°C and may not glow visibly at the lower end of this range. Use tongs or heat-resistant gloves to handle annealed wire. Allow to cool on a heat-resistant surface before drawing.

## Quality Control

1. **Die diameter verification**: Before each production run, pass a pin gauge through the dies to be used. Record the actual diameter. If a die has enlarged more than 0.1 mm from its nominal size, reclassify it (e.g., a nominal 3.0 mm die that now measures 3.08 mm becomes the "3.1 mm" die). Mark the actual size on the plate with an engraving tool.
2. **Wire diameter measurement**: After each drawing pass, measure the wire diameter with a micrometer at three points along the length (beginning, middle, end). The diameter should be uniform within ±0.05 mm. Variation >0.1 mm indicates die wear, uneven lubrication, or wire temperature variation.
3. **Wire surface inspection**: Visually inspect the drawn wire surface under good lighting. The surface should be smooth and uniform — any longitudinal scratches indicate die surface damage; any transverse marks indicate vibration or jerky pulling. Run a fingernail along the wire — it should be smooth without catching.
4. **Draw force monitoring**: If using a draw bench with a force gauge, record the draw force for each pass. A steady increase in draw force for the same die and material indicates the die is wearing or the lubricant is failing. A sudden increase indicates wire galling — stop immediately and inspect the die.
5. **Tensile testing (periodic)**: For critical applications (electrical windings, wire rope), periodically tensile-test a sample of drawn wire. Work-hardened copper wire should have a tensile strength of 300-450 MPa (versus 220 MPa for annealed). If the tensile strength is too high (>500 MPa), the wire is over-hardened and needs annealing before further drawing or winding.

## Variations and Alternatives

- **Draw plate (this article's primary build)**: Hardened steel plate with multiple tapered holes. Simplest wire drawing tool. One plate covers 1.0-8.0 mm diameter range. Constructable with drill press, reamers, and heat treatment. The bootstrap standard.
- **Individual die inserts**: Each die is a separate hardened steel (or tungsten carbide) insert pressed into a steel holder. Higher precision and easier replacement than a draw plate. Required for fine wire (<1.0 mm) and high-volume production. Each insert has one hole; the workshop maintains a set of 20-50 inserts covering the full diameter range.
- **Tungsten carbide dies**: Inserts made from sintered tungsten carbide (WC-Co). Hardness: 85-92 HRA (equivalent to >70 HRC). Die life: 10-50× steel dies. Required for drawing steel wire in volume and for wire diameters below 1.0 mm. Requires powder metallurgy and cobalt binder — a post-bootstrap material. See [Ultra-Pure Materials](../ultra-pure/index.md) for powder processing.
- **Diamond dies**: Synthetic or natural single-crystal diamond with a laser-drilled hole. Used for the finest wire (<0.1 mm diameter). Die life: millions of meters of copper wire. Requires laser drilling and diamond sourcing — far post-bootstrap.
- **Capstan draw machine**: Continuous drawing of fine wire. The wire wraps around a rotating drum (capstan); friction provides the pulling force. Speed: 30-100 m/min for copper. The wire passes through a die, wraps the capstan, and exits to a take-up spool. Multiple capstans in series with dies between them enable multi-pass continuous drawing. Industrial-era machine requiring precision bearings and speed control.
- **Extrusion (alternative to drawing)**: Metal is pushed through a die rather than pulled. Used for rods, tubes, and complex cross-sections. Requires much higher pressures (500-1000 MPa) but can produce shapes that drawing cannot. See [Extruder](extruder.md) for the equipment.
- **Swaging (alternative to drawing)**: Rotary or die swaging reduces rod diameter by hammering it from all sides simultaneously. Produces rod rather than wire (minimum diameter ~2 mm). Does not produce the smooth, precise surface that drawing does. See [Forming](forming.md).
- Lubricant selection: For copper wire, soapy water (5-10% soap solution) or mineral oil works at room temperature. For steel wire, a lime coating (Ca(OH)₂ slurry, dried before drawing) or phosphate coating reduces friction and prevents galling. Dry soap powder is the industrial standard for high-speed drawing — apply by passing the wire through a box of powdered soap before the die.
- Die wear tracking: Record the number of passes through each die. When a die hole enlarges 0.1 mm beyond its nominal diameter, reclassify the die and stamp the new size on the plate. A worn die produces oversize wire that fails tolerance checks. Expect 200-500 passes for copper (steel die) before the hole enlarges beyond usable tolerance.
- Wire coiling and storage: After drawing, coil the wire on a wooden or steel drum. Coil diameter should be >100× the wire diameter to prevent residual curvature. Store copper wire in a dry location — oxidation produces a green patina that increases contact resistance in electrical applications. For long-term storage, coat copper wire with a thin film of oil or wrap in plastic.
- Starting material preparation: The input to wire drawing is typically rolled rod (8-12 mm diameter) produced by the [rolling mill](rolling-mill.md). The rod must be cleaned of scale and lubricant residue before drawing — scale embedded in the die surface causes scoring. Pickle steel rod in 10% sulfuric acid, then rinse and lime-coat. Copper rod can be drawn as-rolled if the surface is clean.
- Wire gauge standards: The American Wire Gauge (AWG) system defines 40 standard sizes from 0000 (11.68 mm) to 40 (0.078 mm). For bootstrap purposes, produce wire in 0.5 mm increments from 8.0 mm to 1.0 mm (15 sizes). This covers all common electrical winding applications. Finer gauges require tungsten carbide dies and capstan machines.

## References

- [Forming](forming.md) — wire drawing procedures, annealing schedules, and deformation theory
- [Machining](machining.md) — drilling and reaming operations for die construction
- [Bearings & Abrasives](bearings-abrasives.md) — abrasive polishing materials for die finishing
- [Iron & Steel](../metals/iron-steel.md) — high-carbon steel for die plate material and heat treatment
- [Foundry Equipment](foundry-equipment.md) — annealing furnace for inter-pass heat treatment
- [Iterative Bootstrap](iterative-bootstrap.md) — machine tool construction sequence
- [Electricity](../energy/electricity.md) — the primary consumer of drawn copper wire
- [Extruder](extruder.md) — alternative metal shaping by extrusion

---
*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*
