# Sheet Metal Brake

> **Node ID**: machine-tools.sheet-metal-brake
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](machining.md)
> **Enables**: [`machine-tools.forming`](forming.md), [`construction.structural-engineering`](../construction/structural-engineering.md)
> **Timeline**: Years 10-15
> **Outputs**: bent_sheet, formed_panels, ductwork, boxes
> **Critical**: No — bending can be done in a vise or over an anvil edge for small work, but a brake is the only practical method for producing long, straight, repeatable bends in sheet metal

## Principle

A sheet metal brake clamps a flat sheet between a stationary bed and a clamping bar, then swings a hinged bending leaf upward around the clamp edge to fold the sheet to a precise angle. The bend occurs along a straight line defined by the clamping bar edge. The inner bend radius equals the clamping bar edge radius (typically 1-3 mm for sharp bends). Springback of 2-5° in mild steel and 5-10° in aluminum requires overbending past the target angle. The brake handles sheet metal up to 1.5 m wide and 1.5 mm (mild steel) or 2 mm (aluminum) thick in hand-operated versions.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel flat bar (bed) | 10-20 kg | 60 × 8 mm, 1.5 m long, flat and straight | [Iron & Steel](../metals/iron-steel.md) | Cast iron bed (heavier, self-damping) |
| Steel flat bar (clamping bar) | 5-10 kg | 40 × 6 mm, 1.5 m long | [Iron & Steel](../metals/iron-steel.md) | Hardened tool steel edge (longer life) |
| Steel plate (bending leaf) | 10-15 kg | 4-6 mm thick, 150 mm wide × 1.5 m long | [Iron & Steel](../metals/iron-steel.md) | Aluminum plate (lighter, less rigid) |
| Steel angle iron (frame) | 10-20 kg | 50 × 50 × 5 mm, for frame and hinges | [Iron & Steel](../metals/iron-steel.md) | Welded box section (stiffer) |
| Hinge pins | 2-3 | 10 mm diameter steel rod, 100 mm long | [Iron & Steel](../metals/iron-steel.md) | Commercial butt hinges (limited strength) |
| Clamping bolts with nuts | 10-15 | M10 or M12, 80 mm long | [Iron & Steel](../metals/iron-steel.md) | C-clamps (slower to operate) |
| Angle protractor | 1 | 0-180°, 1° graduations | [Measurement](../measurement/index.md) | Bevel gauge (less precise) |
| Steel stand or bench | 1 | Heavy enough to resist bending force without tipping | [Construction](../construction/index.md) | Bolted to existing workbench |

## Prerequisites

- [Steel flat bar and plate](../metals/iron-steel.md) — for bed, clamping bar, and bending leaf
- [Basic machining](machining.md) — for straightening edges, drilling holes, and fitting hinges
- [Drilling capability](machining.md) — for bolt holes and hinge pin holes
- [Measurement](../measurement/index.md) — straightedge and protractor for alignment and angle setting

## Construction Steps

1. **Prepare the bed**: Select a steel flat bar (60 × 8 mm, 1.5 m long) for the bed. Mill or file the top edge straight and true to 0.1 mm over the full length. This edge defines the bend line — any waviness reproduces as a wavy bend.
2. **Prepare the clamping bar**: Select a steel flat bar (40 × 6 mm, 1.5 m long) for the clamping bar. Mill or file the bottom edge (the edge that contacts the sheet) straight and sharp. A slight radius (0.5-1.0 mm) on the bottom edge produces a clean inner bend without marking the sheet surface. Too sharp an edge causes cracking on harder alloys.
3. **Build the frame**: Weld or bolt a rectangular frame from 50 × 50 × 5 mm angle iron. The frame holds the bed stationary at approximately 900 mm height (comfortable working height for a standing operator). The bed bar bolts to the top of the frame along the front edge. Cross-brace the frame to prevent racking — the bending force acts horizontally and can twist an unbraced frame.
4. **Install the clamping mechanism**: Drill holes through the clamping bar at 100 mm intervals (15 holes for a 1.5 m bar). Drill matching holes in a second flat bar (the top clamp bar) that sits above the clamping bar. Install M10 or M12 bolts through both bars. The sheet metal is clamped between the bed and the clamping bar by tightening these bolts. Cam-action clamps (eccentric levers) speed up operation compared to threaded bolts.
5. **Fabricate the bending leaf**: Cut a steel plate (4-6 mm thick, 150 mm wide × 1.5 m long) for the bending leaf. The leading edge (the edge that contacts the sheet during bending) must be straight and slightly rounded (1-2 mm radius). File or grind this edge smooth.
6. **Install hinges**: Mount hinge brackets on the underside of the bending leaf, 150 mm from each end and one in the center (3 hinges minimum for a 1.5 m leaf). Mount matching hinge brackets on the bed frame, positioned so the hinge pin centerline is directly below the clamping bar edge. The hinge pin axis defines the bend axis — it must be exactly parallel to the clamping bar edge within 0.2 mm over the full length. Use 10 mm steel rod for hinge pins.
7. **Add a stroke limiter** (optional): Install an adjustable stop on each end of the frame to limit the bending leaf travel. Set the stop to the desired bend angle (e.g., 90°). This ensures repeatable bends without measuring each one. A bolt threaded through a bracket serves as the stop — adjust the thread depth to change the angle.
8. **Add a handle**: Weld or bolt a steel tube (25 mm diameter, 500 mm long) to each end of the bending leaf. The handles give the operator leverage to bend the leaf upward. For heavier gauges, extend the handles to 700-800 mm.

## Calibration and Verification

1. **Edge straightness**: Place a precision straightedge against the bed top edge and the clamping bar bottom edge. No gap should exceed 0.1 mm. If gaps are found, shim behind the bars or re-machine the edges.
2. **Hinge alignment**: Swing the bending leaf through its full range. It should move smoothly without binding or lateral play. Check that the hinge pin axis is parallel to the clamping bar edge by measuring the gap between the bending leaf edge and the clamping bar at both ends — the gap should be equal within 0.2 mm.
3. **Angle test**: Clamp a piece of 1 mm mild steel sheet. Bend to 90° using the stroke limiter. Measure the actual angle with a protractor. Adjust the stroke limiter to compensate for springback (typically set to 93-95° for a 90° bend in mild steel).
4. **Repeated bend test**: Bend 5 identical pieces to the same angle setting. Measure all 5 — the bend angle must be repeatable within ±1°.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Maximum sheet width | 1.5 m (bed length) |
| Maximum thickness (mild steel) | 1.5 mm (hand-operated) |
| Maximum thickness (aluminum) | 2.0 mm (hand-operated) |
| Minimum bend radius | 1-3 mm (clamping bar edge radius) |
| Bend angle range | 0-135° (depending on frame design) |
| Angle repeatability | ±1° (with stroke limiter) |
| Springback (mild steel) | 2-5° |
| Springback (aluminum) | 5-10° |
| Clamping bolt spacing | 100 mm |
| Number of clamping bolts | 15 (for 1.5 m bed) |
| Bending force (1 mm steel, 1 m bend) | 250-400 N at handle end |

## Strengths

- Produces long, straight, repeatable bends impossible to achieve by hand
- Simple construction from flat bar and angle iron — no castings or precision machining required
- Adjustable clamping bar position allows setting the flange length precisely
- Stroke limiter ensures repeatable bend angles for production runs

## Weaknesses

- Limited to straight-line bends — cannot produce curved or contoured bends
- Maximum thickness is limited by the operator's strength and the frame rigidity
- Clamping bolts must be tightened individually — slow setup for each bend
- Springback varies with material batch and thickness — requires test bends for critical work

## Safety

- **Pinch points**: The clamping bar and bending leaf create severe pinch hazards. Keep hands clear of the hinge area during bending. Use push sticks or pliers for small workpieces.
- **Sharp edges**: Sheet metal edges are razor-sharp after cutting. Wear leather gloves when handling sheet stock.
- **Heavy leaf**: The bending leaf is heavy (10-15 kg). When released after a bend, it falls by gravity. Keep fingers away from the leaf path.

## Press Brake Alternative

For heavier work (>1.5 mm steel), a press brake mounted on a hydraulic or mechanical press provides the necessary force. See [Hydraulic Press](hydraulic-press.md) for the press construction. The tonnage calculation for V-die bending is: P = 650 × S² × L / V, where P = bending force (kN), S = sheet thickness (mm), L = bend length (mm), V = V-die opening width (mm). For example, bending 3 mm mild steel sheet 1000 mm long in a 24 mm V-die requires 244 kN (~25 tonnes).

## See Also

- [Forming](forming.md) — sheet metal bending operations, springback compensation, and tonnage calculations
- [Machining](machining.md) — machining operations for straightening edges and drilling hinge holes
- [Hydraulic Press](hydraulic-press.md) — press brake forming for heavier gauge material
- [Iron & Steel](../metals/iron-steel.md) — steel stock for brake construction

[← Back to Machine Tools](index.md)
