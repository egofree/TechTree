# Wire Drawing

> **Node ID**: metals.wire-drawing
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`Electricity Generation & Distribution`](../energy/electricity.md), [`Wire Rope & Steel Cable`](wire-rope.md)
> **Enables**: [`Iron & Steel Production`](iron-steel.md), [`Primary Metal Forming`](forming.md)
> **Timeline**: Years 8-18
> **Outputs**: drawn-wire, copper-wire, steel-wire, fine-gauge-wire
> **Critical**: No

## Overview

Drawing metal rod through progressively smaller dies to reduce the diameter and increase the length of wire. Wire drawing is the process that converts rolled rod stock (typically 5-12 mm diameter) into wire of any specified gauge, down to fine wire below 0.1 mm for electronics and magnet winding applications.

The process is straightforward in principle: a pointed wire end is threaded through a die with a hole smaller than the current wire diameter, gripped by a draw block or pulling mechanism, and pulled through. The die forces the wire to compress and elongate, reducing its cross-section while increasing its length proportionally. In practice, the details of die material, die angle, lubrication, reduction per pass, and intermediate annealing determine whether the wire breaks, how the surface looks, and whether the final dimensions are within tolerance.

The relationship between the wire and the die is the core of the process. A new die has a precise, polished bore with a conical approach section and a cylindrical bearing section. The wire enters through the approach cone, is compressed as it passes through the bearing, and exits at a smaller diameter. The die must be harder than the wire being drawn. Tungsten carbide handles most ferrous and non-ferrous wire above 1 mm. Diamond (natural or synthetic) handles fine copper and precious metal wire below 1 mm where tungsten carbide wears too quickly for acceptable die life. The die angle (the included angle of the approach cone) affects the balance between drawing force and surface quality: steeper angles require less force but produce a rougher surface.

Primary outputs: `drawn-wire`, `copper-wire`, `steel-wire`, `fine-gauge-wire`.

Wire gauges are standardized by systems such as AWG (American Wire Gauge), SWG (Imperial Standard Wire Gauge), and metric designations (diameter in mm). The AWG system is logarithmic: every 6-gauge decrease doubles the wire cross-section area. For example, 10 AWG is approximately 2.59 mm diameter, while 16 AWG is 1.29 mm. Going from rod to fine wire requires many passes through progressively smaller dies, with intermediate anneals to restore ductility.

## Prerequisites

### Materials

- Rolled rod stock (copper, steel, aluminum, or other metal), typically 5-12 mm diameter, with clean, smooth surface
- Drawing dies: tungsten carbide dies for large wire (>1 mm), natural or synthetic single-crystal diamond dies for fine wire (<1 mm)
- Polycrystalline diamond (PCD) dies for medium wire (0.5-2 mm), bridging the gap between WC and natural diamond
- Lubricant: dry soap powder (for steel), oil emulsion (for copper and non-ferrous), or water-based lubricant
- Pickling acid (dilute sulfuric or hydrochloric acid) for descaling steel rod before drawing
- Flux for pointing the wire end (sulfuric acid or mechanical swaging)

### Equipment

- [Electricity Generation & Distribution](../energy/electricity.md) — material dependency
- [Wire Rope & Steel Cable](wire-rope.md) — material dependency
- Draw bench (for single-length draws of large diameter rod) or bull block / multi-die drawing machine (for continuous drawing of smaller wire)
- Drawing dies mounted in die holders with water or air cooling
- Capstans (draw blocks) of graded diameter to pull wire through each successive die at increasing speed
- Pointing machine or swaging tool to taper the wire end for threading through the die
- Coiler or spooler to collect the drawn wire
- Annealing furnace (bell furnace, strand annealer, or resistance annealer) for intermediate and final heat treatment
- Pickling tank and rinse tank for descaling steel rod
- Wire flattening rolls or shaping rolls (if producing shaped wire, not round)
- Dead block coiler or spooler with automatic layer winding for neat coil formation
- Wire diameter measurement gauge (laser micrometer or contact micrometer) for in-process monitoring

### Knowledge

- Die selection: tungsten carbide for large wire, polycrystalline diamond (PCD) for medium wire, single-crystal natural diamond for fine wire. Die bearing length and approach angle affect drawing force and surface quality.
- Reduction per pass: typically 10-40% reduction in cross-sectional area per die. Too much reduction causes wire breakage; too little requires too many passes.
- Die angle: the included angle of the die cone is typically 6-24 degrees. Steeper angles reduce drawing force but give poorer surface finish. Shallower angles give better surface but increase friction.
- Work hardening: each drawing pass cold-works the wire and increases its hardness and tensile strength. After several passes, the wire becomes too hard and brittle to draw further without intermediate annealing.
- Lubrication: soap powder, oil emulsion, or water-based lubricant carried into the die with the wire. Adequate lubrication reduces drawing force, die wear, and surface defects. Insufficient lubrication causes scoring, galling, and wire breakage.
- Annealing schedule: temperature and time to restore ductility after cold working without causing excessive grain growth. Copper anneals at 300-650°C depending on the degree of prior cold work.
- Thread-ability: recognizing when rod surface quality is inadequate for fine wire drawing, and how surface defects in the rod propagate and amplify through successive die passes

### Infrastructure

- Drawing machine floor with heavy foundations (the machines are large and generate vibration)
- Die storage and inspection area (dies are expensive and must be tracked by size, material, and wear)
- Lubricant mixing and recirculation system (for wet drawing with oil emulsion)
- Annealing furnace with atmosphere control (inert gas or reducing atmosphere to prevent oxidation of bright-annealed copper wire)
- Pickling area with acid-resistant flooring, ventilation, and drainage (for steel rod descaling)
- Wire coiling and packaging area
- Adequate power supply (drawing machines and annealing furnaces draw significant current)
- Die grinding and polishing equipment for re-sizing worn dies (a lathe with diamond grinding wheels)

## Process Description

### Step-by-Step Procedure

1. Prepare the rod stock. For steel rod: pickle in dilute sulfuric or hydrochloric acid to remove mill scale, rinse thoroughly, and apply a lubricant coating (phosphate + soap for steel, or lime + soap). For copper rod: the rod is usually already clean from the rolling mill. Inspect for surface defects.
2. Point the wire end. Swage or file the leading end of the rod to a tapered point small enough to pass through the first die. On mechanized lines, a rotary swager or pointing machine does this automatically.
3. Thread the pointed end through the first die. Grip the protruding end with tongs or the draw block jaws. Begin pulling. The wire feeds through the die, and the capstan pulls it at a speed that matches the elongation from the die reduction.
4. On a multi-die machine, the wire passes through several dies in sequence. Each die reduces the diameter further. The capstan between each die runs faster than the previous one to account for the length increase from the reduction. The speed ratio between capstans must precisely match the reduction ratio of each die, or the wire will break from excess tension or accumulate slack.
5. Apply lubrication continuously at each die. For dry drawing (steel), soap powder is picked up by the wire as it enters the die. For wet drawing (copper), oil emulsion is sprayed onto the die and wire. The lubricant reduces friction, carries away heat, and prevents metal-to-metal contact between the wire and die.
6. Monitor for wire breakage. A broken wire means stopping the machine, re-threading through all downstream dies, and restarting. Frequent breakage indicates die wear, inadequate lubrication, dirty stock, or incorrect reduction schedule.
7. After the final pass, coil the wire onto a spool or coiler. Weigh and label the coil with material, diameter, tensile strength, and batch number.
8. If the wire has been work-hardened beyond the acceptable limit for the application, anneal before shipping. Copper wire for electrical use is typically annealed to restore maximum conductivity and ductility. Steel wire for spring applications may be drawn to full hard and shipped without annealing.

9. For fine wire (below 0.5 mm), the final passes use diamond dies and wet drawing with oil emulsion lubrication. The wire speed is highest in the final passes (10-30 m/s on modern machines). Even a momentary loss of lubrication at these speeds causes immediate wire breakage.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Reduction per pass (area) | 10-40% | Larger reductions risk wire breakage; smaller reductions waste passes |
| Die approach angle (included) | 6-24° | Steeper for soft metals (copper), shallower for hard metals (steel) |
| Die bearing length | 0.3-1.0x wire diameter | Longer bearing gives better roundness and surface finish |
| Drawing speed | 1-30 m/s | Faster for fine wire on multi-die machines; slower for large rod on draw benches |
| Die material | WC for >1mm, PCD for 0.5-1mm, diamond for <0.5mm | Larger dies can be re-sized by polishing; diamond dies are expensive |
| Lubricant | Soap (dry, steel), oil emulsion (wet, copper) | Must be clean and free of abrasive particles |
| Annealing temperature (copper) | 300-650°C | Lower temp for light anneal (partial softening); higher for full soft |
| Annealing temperature (steel) | 600-750°C | Depends on carbon content and desired final properties |
| Number of passes | 5-20+ | Depends on starting rod diameter and final wire gauge |

A typical copper wire drawing schedule from 8 mm rod to 1.0 mm wire might use 9 dies with area reductions of 20-30% per pass. The wire exits the first die at about 7.1 mm and the last die at 1.0 mm. The drawing speed increases from roughly 1 m/s at the first die to about 50 m/s at the last die, because the same mass of wire must travel faster as the cross-section decreases.

### Copper Wire Drawing Schedule (8 mm rod to 1.0 mm)

| Pass | Entry Ø (mm) | Exit Ø (mm) | Area Reduction (%) | Drawing Speed (m/s) | Drawing Force (N) |
|------|---------------|-------------|---------------------|---------------------|-------------------|
| 1 | 8.00 | 7.13 | 20.5% | 1.0 | 2200-2800 |
| 2 | 7.13 | 6.35 | 20.6% | 1.3 | 1750-2200 |
| 3 | 6.35 | 5.65 | 20.8% | 1.6 | 1400-1750 |
| 4 | 5.65 | 5.03 | 20.9% | 2.0 | 1100-1400 |
| 5 | 5.03 | 4.48 | 20.9% | 2.5 | 870-1100 |
| — | — | — | **Anneal at 400-500°C** | — | — |
| 6 | 4.48 | 3.99 | 20.7% | 3.2 | 690-870 |
| 7 | 3.99 | 3.55 | 20.8% | 4.0 | 540-690 |
| 8 | 3.55 | 3.16 | 20.7% | 5.0 | 430-540 |
| 9 | 3.16 | 2.50 | 37.3% (two-pass) | 8.0 | 340-430 |

**Note**: Passes 1-5 accumulate about 60% total cold work. An intermediate anneal at 400-500°C for 30-60 minutes restores ductility for the remaining passes. Without annealing, wire breaks increase dramatically after pass 5.

### Drawing Force Calculation

The drawing force F can be estimated: F = σ_d × A_f, where σ_d is the drawing stress and A_f is the final wire cross-section. The drawing stress is approximately 40-70% of the wire's flow stress (which increases with each pass due to work hardening). For copper rod with a yield strength of 200 MPa, the first-pass drawing stress is roughly 80-140 MPa, giving a drawing force of ~2200-2800 N for an 8 mm rod reduced to 7.13 mm.

### AWG Wire Gauge Reference

| AWG | Diameter (mm) | Cross-section (mm²) | Resistance (Ω/km) | Max Current (A, chassis) |
|-----|---------------|----------------------|--------------------|--------------------------|
| 10 | 2.588 | 5.26 | 3.277 | 55 |
| 12 | 2.053 | 3.31 | 5.211 | 41 |
| 14 | 1.628 | 2.08 | 8.286 | 32 |
| 16 | 1.291 | 1.31 | 13.17 | 22 |
| 18 | 1.024 | 0.823 | 20.95 | 16 |
| 20 | 0.812 | 0.518 | 33.31 | 11 |
| 22 | 0.644 | 0.326 | 52.96 | 7 |
| 24 | 0.511 | 0.205 | 84.22 | 3.5 |

**Why AWG is logarithmic**: Every 6-gauge decrease doubles the cross-section area (and current capacity). Every 3-gauge decrease doubles the cross-section by √2. This allows simple mental math for wire substitution.

## Safety Considerations

- **Wire break (whiplash)**: Wire under tension stores elastic energy. When a wire breaks, the stored energy releases violently, and the wire whips back. A broken steel wire at high speed can cause serious lacerations and eye injuries. Workers must stand clear of the wire path, and guards must be in place around the drawing machine.
- **Pinch points**: The capstans, coilers, and die holders have powerful rotating components. Clothing, fingers, and hair caught in rotating machinery cause severe injuries. Guards and emergency stops are mandatory.
- **Die fragments**: A shattered die ejects fragments at high velocity. Die failure is rare but catastrophic. Die boxes must have guards, and workers must stand clear during start-up when die failure is most likely.
- **Acid burns**: Pickling steel rod in sulfuric or hydrochloric acid produces chemical burns on contact. The pickling area requires acid-resistant PPE and emergency wash stations.
- **Noise**: Multi-die drawing machines and capstans produce continuous high noise levels. Hearing protection is mandatory on the drawing floor.
- **Heavy coils**: Finished wire coils can weigh hundreds of kilograms. Use mechanical lifting equipment. Never stand under a suspended coil.

### Personal Protective Equipment

- Safety glasses with side shields at all times on the drawing floor
- Face shield when pointing wire, threading dies, or standing near a running draw during start-up
- Hearing protection (plugs or muffs) in the drawing machine area
- Steel-toe boots
- Leather gloves when handling wire coils and dies (not when operating the machine)
- Acid-resistant gloves, apron, and face shield in the pickling area

### Emergency Procedures

- For wire break: the machine should have an automatic stop triggered by wire break detection. Do not approach the wire path until the machine has stopped. Inspect for the break cause before restarting.
- For caught clothing in rotating machinery: hit the emergency stop immediately. Do not reach toward rotating parts. Cut the clothing to free the worker if needed.
- For acid splash: flush with water for at least 15 minutes. Remove contaminated clothing. Seek medical attention.
- Keep a wire cutter (bolt cutter) accessible for emergency wire severing if needed.

## Quality Control

### Acceptance Criteria

- **Drawn Wire (general)**: Diameter within specified tolerance (typically +/- 0.01-0.05 mm depending on gauge). Roundness (ovality) within tolerance. Surface smooth, free of scratches, die marks, and lubricant residue.
- **Copper Wire (electrical)**: Diameter tolerance per AWG or metric gauge. Tensile strength and elongation meet specification for the temper (hard, half-hard, soft/annealed). Electrical conductivity meets the grade requirement (minimum IACS percentage). Surface must be clean for subsequent enameling or tinning.
- **Steel Wire (structural)**: Tensile strength meets specification. Diameter tolerance per gauge. No surface cracks, seams, or laps. Zinc coating uniform and meets weight requirement if galvanized.
- **Fine Gauge Wire**: Diameter tolerance tight (typically +/- 0.005 mm or tighter). Surface free of defects at high magnification. No internal defects (center burst) detectable by bend testing.

### Testing Methods

- **Micrometer measurement**: Measure diameter at multiple points along the wire length and around the circumference (to check roundness). The standard method for wire gauge verification.
- **Tensile testing**: Pull a sample to failure in a tensile testing machine. Measures breaking strength, yield strength (if applicable), and elongation. Standard quality test for all wire grades.
- **Wrap test (mandrel wrap)**: Wrap the wire tightly around a mandrel of specified diameter (typically 1x to 5x the wire diameter). The wire must not crack or break. This tests ductility and detects surface defects.
- **Reverse bend test**: Clamp the wire and bend it 90 degrees alternately in opposite directions. Count the number of bends to failure. Tests ductility and surface quality.
- **Electrical conductivity**: Measure resistance per unit length and convert to % IACS. Even small impurity levels or cold work reduce copper conductivity measurably.
- **Surface inspection**: Visual inspection under good lighting. For fine wire, use magnification. Look for die marks, scratches, pits, and lubricant residue.
- **Bend and break test for center burst**: Bend a short sample sharply and break it. Examine the fracture surface. A cup-and-cone fracture is normal. A flat, fibrous fracture with a center defect indicates an internal chevron crack (center burst) from excessive die reduction.

### Sampling Protocol

- Measure diameter and check surface on every coil
- Tensile test samples from the beginning and end of each coil (properties can vary along the length)
- Wrap test samples from each heat lot
- Track die wear by measuring wire diameter trend: if diameter drifts toward the upper tolerance, the die is wearing and should be replaced
- For electrical copper wire, test conductivity on every coil before certification

## Scaling Notes

- **Single-die draw bench**: Hand-operated or motorized chain draw bench. One die, one pass at a time. For large diameter rod (5-12 mm) and small batches. The entry point for wire drawing capability. Produces tens to hundreds of meters per hour.
- **Bull block (single-block drawing machine)**: A single capstan with one die. Motorized. Higher throughput than a draw bench. Good for intermediate sizes.
- **Multi-die continuous drawing machine**: 5-12 dies in series, each with its own capstan running at progressively higher speed. Continuous operation from rod to finished wire. The standard production machine. Produces kilometers of wire per shift.
- **Multi-wire drawing machine**: Several wires drawn simultaneously on the same machine. Highest throughput for mass production of common gauges (fencing wire, nail wire, electrical conductor).

Key scaling challenges: multi-die machines require precise speed matching between capstans. If the speed ratio between adjacent capstans does not exactly match the die reduction ratio, the wire accumulates tension or slack and breaks. Dies wear progressively during a production run, changing the actual reduction. Regular die inspection and replacement is a significant operating cost. Annealing furnaces must handle the throughput of the drawing machine without becoming the bottleneck.

Die life varies by material and wire diameter. Tungsten carbide dies drawing copper rod at 8 mm may last for hundreds of tonnes before needing re-polishing. The same dies drawing hard steel wire may wear out in tens of tonnes. Diamond dies for fine copper wire (<0.5 mm) can last for very long runs because copper is soft and the wire force is low, but they are expensive to replace when they eventually wear or chip.

Wire drawing also produces shaped wire (square, hexagonal, flat) by using dies with the appropriate cross-sectional profile, or by passing round wire through Turks-head rolls (four adjustable rollers that form the wire into a rectangle or square). Shaped wire is used for keys, architectural trim, and electrical bus bar.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Wire breakage at die | Die wear (bore enlarged, bearing damaged); inadequate lubrication; surface defects in rod; too-high reduction per pass | Replace worn die (bore size >2% over nominal); check and improve lubrication flow (10-15 L/min per die for wet drawing); inspect rod quality with magnifying glass; reduce per-pass reduction to 15-20% |
| Surface scoring (die marks) | Worn or damaged die, dirty lubricant, hard particles on wire surface | Replace die; filter or replace lubricant (filter to 5 μm); clean rod with acid pickle or mechanical descaling before drawing |
| Center burst (chevron cracks inside wire) | Too-high reduction per pass (>40%), too-steep die angle (>24°), insufficient back tension | Reduce per-pass reduction to 20-30%; use a die with 12-18° included angle; apply 5-15% back tension |
| Excessive ovality (out-of-round wire) | Die worn out-of-round, excessive bearing wear, misaligned die holder | Replace die; check die holder alignment with dial indicator (runout <0.05 mm); use a die with longer bearing length (0.5-1.0× wire diameter) |
| Wire too hard after drawing | Excessive cold work without intermediate annealing (>50% total reduction) | Schedule intermediate anneals at 300-650°C (copper) or 600-750°C (steel); limit total reduction between anneals to 40-60% |
| Copper wire conductivity too low | Impurities in the rod (>0.01% total); excessive cold work not annealed out; contaminated lubricant residue | Use higher purity rod (electrolytic tough pitch, >99.9% Cu); anneal the wire at 400-500°C for 30-60 min to restore conductivity; clean lubricant residue with solvent wipe |
| Lubricant residue on wire | Excessive lubricant flow, wrong lubricant viscosity, insufficient wipe-off after die | Reduce lubricant flow; switch to lower viscosity emulsion; add a wiper die or air knife 100-200 mm after the drawing die |
| Die life too short (<10 tonnes for WC) | Abrasive rod surface (mill scale, sand); insufficient lubrication; wrong die material for the wire type | Clean rod surface before drawing (acid pickle + rinse + lime coat for steel); improve lubrication; upgrade die material (WC to PCD for 0.5-2 mm, PCD to diamond for <0.5 mm) |
| Wire wraps unevenly on spool | Tension too low (loose coils) or too high (tight, overlapping); capstan speed mismatch | Adjust spooler tension to 5-15% of wire breaking load; verify capstan speed ratio matches die reduction ratio within ±1% |
| Die heating (die too hot to touch) | Insufficient cooling; drawing speed too high for the die size | Add water cooling to die holder (2-5 L/min); reduce drawing speed by 20-30%; check die bore is not partially blocked |
| Wire diameter drifts toward upper tolerance | Die bore wearing progressively (normal wear); wire temperature increasing | Track die bore by measuring wire diameter every 5-10 tonnes; replace die when wire reaches +75% of upper tolerance; monitor and control wire temperature |
| "Crowning" (wire thicker in middle than at ends) | Die bearing too short; wire speed fluctuations | Use die with longer bearing (0.8-1.0× wire diameter); stabilize motor speed (±0.5% regulation) |

## Variations and Alternatives

- **Dry drawing (soap powder lubrication)**: Standard for steel wire. Soap powder is carried into the die with the wire, forming a lubricating film under the extreme pressure in the die. Simple, low-cost, but leaves soap residue on the wire.
- **Wet drawing (oil emulsion lubrication)**: Standard for copper and non-ferrous wire. Oil-in-water emulsion is sprayed onto the die and wire. Provides better cooling and cleaner surface than dry drawing. The emulsion must be filtered and maintained to prevent bacterial growth.
- **Hydrostatic extrusion**: An alternative to wire drawing for difficult-to-draw materials. The billet is enclosed in a pressure vessel and forced through the die by hydraulic pressure acting through a fluid medium. Lower friction than conventional drawing but more complex equipment.
- **Bundled drawing**: Multiple wires drawn simultaneously through a single large die. Used for producing very fine wire efficiently. The wires are separated after drawing.
- **Tube drawing**: Similar to wire drawing but with a mandrel inside the tube to control the inner diameter. The same equipment with the addition of a floating or fixed mandrel. Produces precision tubing.

### Material Handling

Store rod stock by material and diameter in racks or on spools, protected from corrosion. Steel rod should be kept dry or coated with a light oil to prevent rust before drawing. Copper rod from the rolling mill has a thin oxide layer that may need removal before fine wire drawing. Keep dies organized by size and material, and track cumulative usage (dies wear gradually and must be re-polished or replaced). Lubricant systems should be monitored for contamination, filtered regularly, and replaced on a schedule. Finished wire coils should be labeled with material, diameter, temper, batch number, and date.

## References

- [Metals](index.md) — parent capability
- [Metals Domain](./index.md) — domain overview and related capabilities
- [Electricity Generation & Distribution](../energy/electricity.md) — upstream dependency (material)
- [Wire Rope & Steel Cable](wire-rope.md) — upstream dependency (material)
- [Iron & Steel Production](iron-steel.md) — downstream capability
- [Primary Metal Forming](forming.md) — downstream capability

---
*Part of the [Bootciv Tech Tree](../../index.md) · [Metals](./index.md) · [All Domains](../../index.md)*
