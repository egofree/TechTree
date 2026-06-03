# Filter Press

> **Node ID**: chemistry.filter-press
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`metals.welding`](../metals/welding.md), [`polymers.elastomers`](../polymers/elastomers.md)
> **Enables**: [`chemistry.water-treatment`](water-treatment.md), [`chemistry.chemical-recovery`](chemical-recovery.md), [`metals.metal-recycling`](../metals/metal-recycling.md)
> **Timeline**: Years 10-25
> **Outputs**: filter_cake, filtrate
> **Critical**: No — filter presses are the workhorse of solid-liquid separation but settling tanks, centrifuges, and vacuum filters can substitute at lower performance

## Principle

A filter press separates solids from liquids by forcing a slurry under pressure through a porous filter medium (cloth, paper, or membrane) that retains solid particles as a cake while allowing clear liquid (filtrate) to pass. The plate-and-frame design sandwiches filter cloth between alternating plates and frames (or recessed chamber plates) compressed by a hydraulic or screw mechanism. Slurry is pumped into the chambers at 5-15 bar pressure. Solids accumulate as cake in each chamber; filtrate drains through the cloth and exits through internal channels.

Filtration continues until the chambers fill with cake (indicated by decreasing filtrate flow or increasing feed pressure). The press is then opened, and the filter cake is discharged by gravity. Filter cloth is cleaned or replaced between cycles. Typical cycle time: 1-8 hours depending on slurry characteristics and cake compressibility.

The filter press achieves higher solids content in the cake (30-60% by weight) than vacuum filtration (15-40%) or settling (5-20%). The trade-off is batch operation and manual cake discharge for standard designs. The filter press is the lowest-cost option for solid-liquid separation at small to medium scale (1-50 m³ slurry per batch).

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate](../metals/iron-steel.md) (end plates) | 100-500 kg | A36, 20-40 mm thick, machined flat | [Iron & Steel](../metals/iron-steel.md) | Cast iron end plates (heavier) |
| [Steel plate](../metals/iron-steel.md) (frame) | 200-1,000 kg | Structural steel channel or I-beam | [Iron & Steel](../metals/iron-steel.md) | Concrete frame (stationary installation) |
| [Cast iron plates](../metals/casting.md) | 10-50 units | Recessed chamber, 400-1200 mm square | [Casting](../metals/casting.md) | Polypropylene plates (corrosive slurries) |
| [Filter cloth](../textiles/fibers.md) | 10-50 sheets | Polypropylene or polyester felt, 200-800 g/m² | [Textiles](../textiles/fibers.md) | Cotton (lower chemical resistance) |
| [Hydraulic cylinder](../energy/hydraulics.md) | 1 unit | 50-200 mm bore, rated to 200 bar, manual or powered pump | [Hydraulics](../energy/hydraulics.md) | Handwheel screw (slower, no hydraulics needed) |
| [Steel pipe](../metals/forming.md) (feed manifold) | 10-50 kg | Carbon steel or 316L SS, 25-50 mm | [Forming](../metals/forming.md) | — |
| [Diaphragm pump](../energy/hydraulics.md) | 1 unit | 5-15 bar, corrosion-resistant wetted parts | [Hydraulics](../energy/hydraulics.md) | Progressive cavity pump (continuous feed) |

## Construction Steps

1. **Fabricate the structural frame**: Weld a rectangular frame from structural steel channel (100-200 mm) or I-beam. The frame consists of two vertical end plates connected by four horizontal tie bars. The fixed head plate (stationary end) has the feed inlet connection. The movable head plate (driven by the hydraulic cylinder) presses the plate stack closed. Overall frame dimensions: 1-3 m long (depending on number of plates) × 0.5-1.5 m wide × 1-2 m tall.

2. **Fabricate or procure filter plates**: Cast or machine recessed chamber plates from cast iron or polypropylene. Standard plate sizes: 400 × 400 mm, 630 × 630 mm, 800 × 800 mm, or 1000 × 1000 mm. Each plate has a recessed chamber (15-40 mm deep on each side), a central feed hole (25-50 mm diameter), filtrate drainage channels on the surface (grooved or studded pattern at 20-40 mm spacing), and four corner filtrate discharge holes. Plate thickness: 30-60 mm.

3. **Install guide rails**: Mount two horizontal steel rails on the inside of the frame's side members. The filter plates slide on these rails during opening and closing. Ensure rails are parallel within 1 mm over their full length to prevent plate misalignment.

4. **Mount hydraulic closure system**: Install the hydraulic cylinder (50-200 mm bore) on the movable head end of the frame. The cylinder rod connects to the movable head plate. When pressurized, the cylinder pushes the head plate toward the fixed end, compressing the plate stack. Closure force: 5-20 tonnes (sufficient to seal all gaskets under maximum feed pressure). Manual hydraulic pump (hand-lever) for small presses; powered hydraulic pump unit for larger presses.

5. **Assemble the plate pack**: Thread filter cloths over each plate (each cloth is cut to cover both faces of the plate, with a hole for the central feed port). Stack the clothed plates on the guide rails, alternating plates and frames (for plate-and-frame type) or stacking recessed chamber plates directly (for recessed plate type). Install a tail plate (solid, no feed hole) at the end.

6. **Connect feed manifold**: Pipe the slurry feed pump to the central feed hole in the fixed head plate. The feed manifold runs through the center of all plates — slurry enters each chamber simultaneously when the pump runs. Install a pressure gauge (0-20 bar) on the feed line.

7. **Connect filtrate drain**: Pipe the corner filtrate discharge holes to a common filtrate collection manifold visible at the front of the press. Individual filtrate streams from each plate allow visual inspection — a cloudy stream indicates a torn or leaking filter cloth.

8. **Install drip tray**: Mount a steel drip tray under the plate pack to catch filtrate drips and cake discharge. The tray should be sized to hold the full cake volume from one cycle. Include a drain connection to the filtrate collection tank.

## Calibration and Verification

1. **Closure pressure test**: Close the press under full hydraulic pressure. Measure the gap between the movable head and the fixed head at four corners. Maximum deviation: <1 mm. Uneven closure indicates frame misalignment or worn guide rails.

2. **Leak test (empty)**: Close the press. Fill the chambers with water via the feed pump at 5 bar. Inspect all plate edges for leaks. Zero leaks at the plate gasket faces. Minor weeping at the filter cloth edges is acceptable during water test (solids in real slurry will seal these leaks).

3. **Filtration trial**: Process a batch of test slurry. Measure filtrate clarity (turbidity <50 NTU for most applications), filtration rate (L/min at specified pressure), and cake solids content (30-60% by weight depending on slurry). Adjust feed pressure and cloth type if filtrate is cloudy (indicating cloth pores too large) or filtration is too slow (cloth too tight).

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Plate size | 400-1,200 mm square |
| Number of chambers | 10-50 per press |
| Chamber depth (per side) | 15-40 mm |
| Cake volume per chamber | 5-40 L (depends on plate size and depth) |
| Total cake capacity | 50-2,000 L per cycle |
| Operating pressure | 5-15 bar (typical), up to 30 bar for hard-to-filter slurries |
| Filtration cycle time | 1-8 hours (depends on slurry filterability) |
| Cake moisture content | 30-60% (depends on solid type and squeeze pressure) |
| Filtrate clarity | <50 NTU (with correct cloth selection) |
| Throughput | 1-50 m³ slurry per cycle |
| Closure force | 5-20 tonnes |
| Filter cloth life | 100-2,000 cycles (depends on abrasiveness of solids) |
| Plate life | 5-15 years (cast iron), 3-8 years (polypropylene) |

## Safety

- **High pressure**: The feed pump delivers 5-15 bar to the chambers. A plate failure under pressure releases hot or corrosive slurry. Never open the press while under feed pressure. Install a pressure relief valve on the feed line. Close the feed valve and depressurize before releasing the hydraulic closure.
- **Heavy plates**: Cast iron filter plates (630-1,000 mm) weigh 20-60 kg each. Manual handling of plates during maintenance causes back injuries. Use lifting equipment for plates larger than 630 mm. Two-person minimum for plate replacement.
- **Hydraulic system**: The closure cylinder operates at 100-200 bar hydraulic pressure. Hydraulic injection injuries from pinhole leaks require immediate surgical debridement. Never use hands to search for hydraulic leaks — use cardboard.
- **Chemical exposure**: Slurries containing acids, bases, or heavy metals present splash and contact hazards. Chemical-resistant gloves and face shield during cake discharge. Secondary containment under the press for chemical slurries.
- **Pinch points**: The plate stack closes with tonnes of force. Keep hands clear of plate edges during closure. Two-hand operation of the hydraulic control.

## See Also

- [Water Treatment](water-treatment.md) — sludge dewatering with filter presses
- [Chemical Recovery](chemical-recovery.md) — catalyst and precipitate recovery
- [Centrifuge](centrifuge.md) — alternative solid-liquid separation (continuous, higher cost)
- [Crystallizer](crystallizer.md) — crystal recovery by filtration

[← Back to Chemistry](index.md)
