# Wire Rope & Steel Cable

> **Node ID**: metals.wire-rope
> **Domain**: [Metallurgy](./index.md)
> **Dependencies**: [`metals.wire-drawing`](./wire-drawing.md)
> **Timeline**: Years 20-35
> **Outputs**: wire_rope, steel_cable, strand, wire_rope_sling
> **Critical**: false

## Overview

Wire rope is a composite structural element made from individual steel wires helically laid around a central core to form strands, which are themselves laid around a core to form the finished rope. The helical construction gives wire rope flexibility (it bends around sheaves and drums) while retaining the high tensile strength of the constituent steel wires (1570-1960 MPa). Wire rope replaced hemp rope and chain for lifting and hauling applications starting in the 1830s (Wilhelm Albert's 1834 mine hoist rope in Clausthal, Germany) and became indispensable for mining hoists, cranes, elevators, suspension bridges, cable cars, and aerial tramways.

Wire rope is not a single material — it is a mechanical assembly whose properties depend on wire grade, construction (number of wires per strand, number of strands, lay direction), core type, and end fitting method. Selecting the wrong construction for an application causes premature failure. A 6×19 rope on a small-diameter sheave will fatigue-break in weeks; a 6×37 rope on the same sheave will last months.

Position in the bootstrap chain: wire rope requires [high-carbon steel wire](iron-steel.md) from the [primary forming](forming.md) mill (wire rod rolling, then cold drawing through successively smaller dies). It enables mechanized vertical transport (mine hoists, elevators), heavy lifting (cranes, derricks), and long-span structural systems (suspension and cable-stayed bridges). Without wire rope, deep mining below ~200 m becomes impractical — man-hauling ore in buckets on chain limits both depth and tonnage.

## Prerequisites

**Materials**:
- [High-carbon steel wire rod](forming.md) (0.4-0.8% C, typically grade 1070-1080), 5-12 mm diameter, drawn to 0.3-5.0 mm finished wire
- [Lubricant](../chemistry/adhesives-coatings.md) — petrolatum-based or bituminous compound for internal rope lubrication and corrosion protection
- Zinc wire or zinc powder for socketing (end fittings)
- Epoxy resin for epoxy socketing

**Tools and equipment**:
- [Wire drawing bench](forming.md) — single-die or multi-die continuous drawing machine with tungsten carbide or diamond dies
- Stranding machine (tubular strander or planetary strander) — rotates bobbins of wire around a core
- Rope closing machine (closing machine) — rotates bobbins of strands around a core
- [Swaging press](../machine-tools/forming.md) — hydraulic or mechanical, 50-200 tonne capacity for swaging end fittings
- Tension measuring device — load cell or dynamometer for proof loading finished rope
- Calipers and micrometers for wire and rope diameter measurement

**Knowledge**:
- Understanding of helical geometry and lay length
- Tensile testing interpretation (minimum breaking force, proof force)
- Inspection and discard criteria for wire rope in service

**Infrastructure**:
- Covered workshop for stranding and closing (rope contamination by grit causes internal abrasion)
- Power source for drawing machines and strander (electric motor or line shaft, 10-50 kW)

## Bill of Materials

| Material | Quantity per 100 m rope (19 mm 6×19) | Source | Alternatives |
|----------|--------------------------------------|--------|-------------|
| High-carbon steel wire (drawn, 1.0 mm) | 130-140 kg | [Iron & Steel](iron-steel.md) → [Forming](forming.md) → wire drawing | Stainless steel wire (316 grade) for marine service — 30% lower strength |
| Fiber core (manila or sisal) | 3-5 kg | [Textiles](../textiles/index.md) — natural fiber rope | Independent wire rope core (IWRC) for 10-15% higher strength |
| Petrolatum lubricant | 2-4 kg | [Petroleum](../petroleum/index.md) — refined mineral grease | Bituminous compound for stationary ropes (bridge cables) |
| Zinc for socketing | 0.5-1.0 kg per socket | [Non-Ferrous Metals](non-ferrous.md) — zinc ingots | Epoxy resin socketing (no molten metal hazard) |

## Process Description

### Wire Drawing

Wire drawing reduces wire rod diameter and increases tensile strength through cold work hardening. Starting from 5-12 mm hot-rolled wire rod (from the [forming mill](forming.md)):

1. **Descaling**: Pass wire rod through mechanical descaler (reverse-bend rollers break off scale) or pickled in 10-15% hydrochloric acid at 20-40°C for 5-15 minutes to remove oxide scale. Rinse in water, then apply lime or borax coating as drawing lubricant carrier.
2. **Pointing**: Reduce the leading end of the wire rod to pass through the first die. Use rotary swaging, rolling, or hammer forging to taper the end to ~60% of the rod diameter over 100-200 mm length.
3. **Drawing**: Pull the pointed wire through a hardened die (tungsten carbide for wire >0.5 mm; natural or synthetic diamond for wire <0.5 mm). Each pass reduces the cross-section by 10-25% (area reduction). Soap or oil-based lubricant applied at die entry. Typical sequence: 8 mm rod → 6.5 → 5.2 → 4.1 → 3.3 → 2.6 → 2.1 → 1.7 → 1.4 → 1.1 mm (9 passes). Drawing speed: 50-300 m/min depending on diameter.
4. **Intermediate heat treatment** (patenting): For wire above ~0.5% C, heat to 870-950°C (austenitize), then quench in lead bath at 480-540°C (isothermal transformation to fine pearlite/sorbite). This restores ductility for further drawing while maintaining a high-strength microstructure. Patenting is the standard treatment for rope wire.
5. **Final drawing**: After patenting, draw to finished size in 3-6 additional passes. Final tensile strength: 1570-1960 MPa depending on carbon content and total reduction. Galvanize (zinc coat) before or after final drawing for corrosion-resistant ropes.
6. **Quality check**: Measure wire diameter with micrometer (tolerance ±0.02 mm for 1.0 mm wire). Tensile test one sample per coil (minimum breaking force must meet grade specification: 1570, 1770, or 1960 MPa). Torsion test: clamp wire at both ends, twist until fracture — count turns to failure (minimum 20-30 turns for 1.0 mm wire per ISO 17893).

### Stranding

Stranding lays multiple wires around a central core (fiber or wire) to form a strand. The most common strand is the single-lay strand: 6 outer wires around 1 center wire (1+6 = 7-wire strand).

1. **Load bobbins**: Mount spools of finished wire onto the cradle of the stranding machine. Each wire runs through an individual tension brake (adjustable friction drag to maintain uniform tension across all wires).
2. **Set lay length**: The lay length is the axial distance for one complete helical revolution of a wire around the core. Adjust the lay length by changing the gear ratio between the cradle rotation and the take-up haul-off speed. For a 7-wire strand with 1.0 mm wire, typical lay length is 50-70 mm (6-8× the strand diameter).
3. **Run the strander**: The cradle rotates, wrapping wires helically around the core fed from the center. Apply lubricant (petrolatum) to the core and wires as they converge at the closing point. The strand exits through a shaping die that ensures roundness and proper lay.
4. **Take-up**: Wind finished strand onto spool under controlled tension. Measure strand diameter (tolerance per ISO 17893: ±0.15 mm for 3-5 mm strand).

### Rope Closing

Rope closing lays multiple strands around a core to form the finished wire rope.

1. **Select core**: Fiber core (FC) — manila, sisal, or polypropylene — provides cushioning and internal lubricant reservoir. Independent wire rope core (IWRC) — a separate small wire rope — provides 10-15% higher breaking strength and better resistance to crushing on drums. For most general-purpose ropes, FC is standard.
2. **Load strand bobbins**: Mount strand spools onto the closing machine cradle. Standard 6-strand rope uses 6 strand bobbins.
3. **Set rope lay length**: Typically 6-8× the rope diameter. Adjust gear ratio between cradle rotation and take-up. The lay direction is either regular lay (strands laid in opposite direction to the wires within the strands — most common, resists kinking) or lang lay (same direction — more flexible, better wear resistance, but rotates under load).
4. **Close the rope**: Run the closing machine. Strands wrap helically around the core. Lubricant is pumped into the closing point to fill internal voids between strands and wires. The rope exits through a closing die.
5. **Take-up**: Wind finished rope onto a reel under tension. Measure rope diameter with calipers at three positions 1 m apart (tolerance: +0 to +5% of nominal diameter per ISO 17893).
6. **Proof load**: Apply a proof load equal to 50% of the minimum breaking force using a calibrated dynamometer. Hold for 5 minutes. This seats the strands and verifies structural integrity. Record the proof load value.

### End Fitting Attachment

Wire rope must terminate in a fitting that transfers load from the rope to the attachment point. The four standard methods:

**Swaging** (for thimbles and sleeves):
1. Pass rope end through a steel or aluminum swage sleeve.
2. Form a loop around a thimble (grooved metal former that prevents rope crushing at the bend).
3. Pass the tail back through the swage sleeve.
4. Place the sleeve in the swaging die set and compress with hydraulic press. The die reduces the sleeve diameter to a specified dimension, creating a friction bond. Follow manufacturer's die closure dimension — typically compress to 60-70% of original sleeve outer diameter.
5. Proof load the swaged fitting to 50% of rope breaking force.

**Zinc socketing** (for spelter sockets — the strongest permanent termination):
1. Unlay the rope end for a length equal to 1.5-2× the socket basket depth. Separate individual wires and fan them out (" brooming").
2. Clean wires with solvent (mineral spirits) to remove lubricant. Degreasing is critical — zinc will not bond to oily wire.
3. Insert the broomed wires into the socket basket. Ensure wires are evenly distributed. Pack with fine zinc wire or powder to fill gaps.
4. Heat zinc in a crucible to 450-480°C (zinc melts at 419°C). Skim dross from the surface.
5. Pour molten zinc into the socket basket in a single continuous pour. Fill completely. The zinc solidifies, locking every wire in place.
6. Allow to cool to ambient temperature (30-60 minutes). Inspect the poured cone — it must be solid with no voids or porosity visible at the open face.
7. Proof load to the rope's working load limit. Socketing efficiency: 100% of rope breaking force when done correctly (strongest termination method).

**Epoxy socketing** (alternative to zinc, lower temperature):
Same procedure as zinc socketing but fill the socket basket with two-part epoxy resin instead of molten zinc. Cure at ambient temperature for 24 hours or at 60°C for 2 hours. Epoxy socketing eliminates the molten metal hazard and achieves 90-100% of rope breaking force. Widely adopted since the 1980s.

**Mechanical clips** (wire rope clips, Crosby clips):
1. Form a loop or dead-end with the rope.
2. Install wire rope clips: saddle on the live (loaded) end, U-bolt on the dead end. Never place the saddle on the dead end — the mnemonic is "never saddle a dead horse."
3. Number of clips: minimum 3 clips for rope up to 25 mm, 4 clips for 25-50 mm, 5 clips for 50-75 mm (per ASME B30.5). Space clips at 6× rope diameter apart.
4. Torque clip nuts to manufacturer's specification (typically 40-200 N·m depending on clip size). Re-torque after initial loading.
5. Clip efficiency: 80-90% of rope breaking force (lower than swaging or socketing). Acceptable for temporary rigging and non-critical applications.

## Quantitative Parameters

### Wire Tensile Strength Grades

| Grade | Tensile Strength (MPa) | Typical Wire Carbon (%) | Application |
|-------|----------------------|------------------------|-------------|
| 1570 | 1570 min | 0.40-0.55 | General purpose, moderate loads |
| 1770 | 1770 min | 0.50-0.65 | Standard mining, crane ropes |
| 1960 | 1960 min | 0.60-0.80 | Heavy-duty hoisting, bridge strand |
| 2160 | 2160 min | 0.70-0.85 | Specialized high-load applications |

### Common Rope Constructions

| Construction | Wires per Strand | Total Wires (approx.) | Flexibility | Abrasion Resistance | Typical Sheave Diameter |
|---|---|---|---|---|---|
| 6×7 | 7 (1+6) | 42 + core | Low (stiff) | High | 42-56× rope diameter |
| 6×19 | 19 (1+6+12) | 114 + core | Moderate | Moderate | 30-45× rope diameter |
| 6×37 | 37 (1+6+12+18) | 222 + core | High (flexible) | Low | 18-30× rope diameter |
| 6×36 Warrington-Seale | 36 | 216 + core | High | Moderate-High | 20-30× rope diameter |

### Rope Minimum Breaking Force (6×19, FC, 1770 MPa grade)

| Nominal Diameter (mm) | Mass (kg/m) | Min. Breaking Force (kN) | Working Load Limit (kN, safety factor 5) |
|----------------------|-------------|-------------------------|----------------------------------------|
| 10 | 0.38 | 58 | 11.6 |
| 13 | 0.64 | 97 | 19.4 |
| 16 | 0.97 | 147 | 29.4 |
| 19 | 1.37 | 207 | 41.4 |
| 22 | 1.84 | 277 | 55.4 |
| 26 | 2.57 | 387 | 77.4 |
| 32 | 3.90 | 588 | 117.6 |

### Lay Length and Direction

| Parameter | Regular Lay | Lang Lay |
|-----------|------------|----------|
| Wire lay direction | Opposite to strand lay | Same as strand lay |
| Kink resistance | High (does not tend to unlay) | Low (tends to unlay under load) |
| Wear resistance | Moderate | High (wires present flat face to sheave) |
| Flexibility | Lower | Higher |
| Rotation under load | Minimal | Significant (requires swivel or non-rotating construction) |
| Typical applications | General hoisting, cranes, elevators | Mine hoisting (winding), drag lines |

## Scaling Notes

**Minimum viable wire rope plant**: A single-die hand-cranked drawing bench (drawing wire from 5 mm to 1 mm in multiple passes through hardened steel dies), a small tubular strander (6-bobbin), and a closing machine (6-bobbin) can produce 6×7 rope in diameters 6-16 mm. This is sufficient for light hoisting, small mine hoists, and guy wires. Estimated throughput: 50-200 m of rope per day. Capital investment: moderate — the strander and closing machine are specialized but mechanically simple (gear-driven cradles with haul-off).

**Scaling to industrial production**:
- Multi-die continuous drawing machines (5-9 dies in series) draw wire at 200-500 m/min — an order of magnitude faster than single-die benches. Requires continuous lubricant system and powered payoff/take-up.
- High-speed tubular stranders run at 500-2000 RPM cradle speed, producing strand at 30-100 m/min.
- Multiple closing machines running in parallel increase output linearly.
- Galvanizing line adds zinc coating inline during drawing — necessary for ropes exposed to weather, salt spray, or mine water. Hot-dip galvanizing at 440-460°C deposits 50-200 g/m² zinc.

**Scale breakpoints**:
- Below 50 tonnes/year wire rope production, batch drawing and single strander/closer are appropriate.
- Above 200 tonnes/year, continuous drawing lines and multiple strander/closer sets justify the capital investment.
- Rope diameters above 40 mm require large closing machines (12-bobbin or more) with 50-100 kW drive motors.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Wire breaks during drawing (cup-and-cone fracture) | Excessive area reduction per pass (>25%), or die angle too large (>16° half-angle) | Reduce area reduction to 15-20% per pass; use die with 12-14° half-angle; verify lubricant flow at die entry |
| Wire surface has die marks or scoring | Worn or damaged die, or insufficient lubricant | Replace die (tungsten carbide dies last ~10,000 m per die for 1 mm wire); increase lubricant flow; check die cooling |
| Rope diameter under specification after closing | Insufficient lay length (strands too tight) or too much tension during closing | Increase lay length by 5-10%; reduce closing tension; check closing die diameter |
| Rope diameter over specification | Excessive lubricant filling or loose lay | Reduce lubricant volume; decrease lay length by 5%; verify all strand bobbins applying equal tension |
| Broken wires appear in service within first month | Sheave diameter too small for rope construction (e.g., 6×19 on sheave <30× rope diameter) | Replace with more flexible construction (6×37) or increase sheave diameter to minimum 30× rope diameter for 6×19 |
| Rope develops "birdcage" (strands bulge outward) | Sudden release of load after severe overload, or rotation of rope end | Never shock-load wire rope; use swivel only with lang lay rope; discard rope if birdcage visible — internal damage has occurred |
| Corrosion spots on wire rope in humid/marine environment | Inadequate lubricant coverage or lubricant washed out by water | Re-lubricate with bituminous compound (stationary ropes) or petrolatum-based dressing (running ropes); consider galvanized rope for marine service |
| Swaged sleeve slips under load | Under-swaged (die closure too large) or wrong sleeve material | Re-swage with proper die to manufacturer's closure dimension; use only steel sleeves for steel rope (aluminum sleeves for lighter duty only); proof test every swage |
| Zinc socket has porosity or voids in the cone | Moisture on wires causing steam during pour, or insufficient brooming | Dry wires thoroughly before socketing; preheat socket basket to 100-150°C; pour zinc slowly and continuously to allow air escape |
| Rope rotates excessively under load | Lang lay rope used without swivel, or single-part line on free-hanging load | Switch to regular lay rope; use non-rotating rope construction (19×7 or 35×7) for single-part lifting; install swivel at dead end |

## Safety

- **Stored energy hazard**: Wire rope under tension stores enormous elastic energy. A 19 mm rope at its working load limit (41 kN) stores sufficient energy to cause lethal whip-lash if the rope or its termination fails. Never stand in the line of a tensioned rope. If a rope breaks, the recoiling ends travel at high velocity in the direction of the rope axis. Barricade or exclude personnel from the bight (the area between the load and the anchor point).
- **Broken wire hazard**: Protruding broken wire ends are sharp enough to cause deep puncture wounds and severed tendons. Wear heavy leather gloves when handling wire rope. Never slide bare hands along a rope — pat the rope surface to detect broken wires.
- **Socketing burn hazard**: Molten zinc at 450-480°C causes severe burns on skin contact. Splashes from pouring can travel 1-2 m. Wear full face shield, leather apron, and gauntlet gloves. Pour from a ladle with a long handle. Pre-dry all tools and socket baskets — any moisture in the socket causes explosive spatter of molten zinc.
- **Pinch points at sheaves and drums**: Wire rope passing over a sheave or winding onto a drum creates pinch points that can crush or amputate fingers. Never guide rope onto a drum by hand — use a guide bar or mallet. Keep hands at least 300 mm from any sheave or drum while rope is moving.
- **Sling angle derating**: When a wire rope sling is used in a basket hitch or with legs at an angle to the vertical, the working load limit decreases sharply. At 30° from vertical, derate to 87% of rated capacity. At 45°, derate to 71%. At 60°, derate to 50%. Never exceed 60° from vertical — the horizontal component of the force puts extreme tension on the sling legs and tends to crush the load. Calculate sling tension: T = Load / (number of legs × cos(sling angle from vertical)).
- **Electrical hazard**: Wire rope is electrically conductive. Never use wire rope near energized power lines. Minimum clearance: 3 m for lines up to 50 kV, 6 m for lines up to 200 kV (per OSHA 1926.1408). Contact with energized lines causes electrocution.

## Quality Control

**Incoming wire inspection**:
- Measure wire diameter with micrometer at three points per coil. Tolerance: ±0.02 mm for 0.5-1.5 mm wire (ISO 17893).
- Tensile test: one specimen per coil. Verify minimum breaking force meets grade (1570, 1770, or 1960 MPa).
- Torsion test: clamp 200 mm gauge length, twist until fracture. Count turns to failure — minimum 20 turns for 1.0 mm wire at 1770 MPa grade. Fewer turns indicate embrittlement from over-drawing or hydrogen damage.
- Zinc coating mass (for galvanized wire): dissolve zinc from a measured length in hydrochloric acid + antimony trioxide inhibitor, weigh before and after. Minimum coating mass: 40-120 g/m² depending on wire diameter (ISO 7989).

**Finished rope inspection**:
- Measure rope diameter with calipers at three positions 1 m apart. Acceptable range: nominal diameter to nominal +5% (ISO 17893).
- Visual examination for irregularities: loose wires, high strands, kinks, birdcaging, core protrusion. Any of these is cause for rejection.
- Proof load test to 50% of minimum breaking force. Hold 5 minutes. Record load. No permanent deformation or strand displacement allowed.

**In-service inspection and discard criteria**:
Wire rope in service must be inspected at regular intervals (daily visual, monthly detailed). Discard the rope when any of the following conditions are met (ISO 4309):
- **Broken wire count**: For 6-strand ropes on cranes and hoists, discard when the number of visible broken wires in one lay length exceeds: 6 for 6×7 construction; 12 for 6×19; 22 for 6×37. For running ropes, count both external and internally-visible broken wires.
- **Valley breaks** (broken wires between strands): More critical than crown breaks (on the surface). Discard if any valley breaks are found in a running rope — they indicate internal fatigue.
- **Diameter reduction**: Discard if rope diameter decreases by more than 10% from nominal (indicates core failure or excessive wire wear).
- **End fitting deterioration**: Cracked sockets, deformed swage sleeves, wire rope clips with stripped threads — replace the fitting or discard the rope.
- **Corrosion**: External corrosion visible as pitting or flaking reduces wire cross-section. Internal corrosion (detected by diameter reduction or stiffness increase) is grounds for immediate discard.

## Variations and Alternatives

### Rope Core Types

| Core Type | Description | Strength vs. FC | Flexibility | Crush Resistance | Typical Use |
|-----------|-------------|----------------|------------|-----------------|-------------|
| FC (fiber core) | Manila, sisal, or polypropylene rope | Baseline | High | Low | General purpose, flexing service |
| IWRC (independent wire rope core) | Separate small wire rope | +10-15% | Moderate | High | Multi-layer spooling, crushing service |
| WSC (wire strand core) | Single strand (same as outer strands) | +5-10% | Low | Moderate | Low-flex applications, pendants |

### Alternative Rope Materials

- **Stainless steel wire rope** (AISI 316): Tensile strength ~30% lower than carbon steel at equivalent diameter. Superior corrosion resistance in marine and chemical environments. 3-5× the material cost. Used where corrosion is the limiting factor: boat rigging, chemical plant hoists, architectural cables.
- **Galvanized wire rope**: Carbon steel wire with hot-dip zinc coating (50-200 g/m²). Standard choice for outdoor and mine service. Zinc sacrifices to protect steel but eventually consumed — design life limited by zinc thickness. Tensile strength equivalent to bright (uncoated) wire.
- **Polymer-coated wire rope**: PVC or polyurethane extruded jacket over the finished rope. Protects from abrasion and corrosion. Used for elevator ropes, exercise machine cables, architectural applications. Adds 10-15% to rope diameter.

### Non-Rope Alternatives for Lifting

| Method | Strength | Flexibility | Limitation |
|--------|----------|-------------|------------|
| [Chain](iron-steel.md) (grade 80 alloy) | High per cross-section | Low (articulated links) | Heavy per unit strength; cannot run over sheaves; shock-sensitive |
| Synthetic fiber sling (nylon, polyester) | High (up to 100 tonnes WLL) | Excellent | Degraded by UV, chemicals, heat (>90°C for nylon); lower safety factor required |
| Hemp/manila rope | Low (tensile ~100 MPa) | Excellent | Limited to light loads; degrades in moisture; no longer used for lifting |

## References

- [Iron & Steel Production](iron-steel.md) — high-carbon steel wire rod source material
- [Primary Metal Forming](forming.md) — wire rod rolling and drawing operations
- [Spring Manufacturing](springs.md) — related high-carbon steel wire processing (music wire, spring wire)
- [Structural Engineering](../construction/structural-engineering.md) — suspension bridge cables, cable-stayed structures
- ISO 17893:2004 — Steel wire ropes — Vocabulary, designation and classification
- ISO 4309:2010 — Cranes — Wire ropes — Care and maintenance, inspection and discard

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Metals](./index.md) • [All Domains](../../index.md)*
