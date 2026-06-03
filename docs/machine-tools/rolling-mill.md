# Rolling Mill

> **Node ID**: machine-tools.rolling-mill
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`machine-tools.casting`](casting.md), [`machine-tools.machining`](machining.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`machine-tools.forming`](forming.md), [`energy.electricity`](../energy/electricity.md)
> **Timeline**: Years 10-20
> **Outputs**: bar_stock, sheet_metal, plate, rod
> **Critical**: Yes — rolling is the only practical method for producing uniform bar stock, sheet, and plate in quantity; these feed every downstream process

## Principle

A rolling mill reduces the cross-section of heated (or cold) metal by passing it between counter-rotating cylindrical rolls. Each pass reduces thickness by 10-30% and elongates the workpiece proportionally. The rolls grip the metal by friction and draw it through the narrowing gap. Force on each roll is determined by the material's flow stress at temperature, the contact area (roll bite), and the reduction ratio. For hot steel at 1000°C, yield stress is approximately 50-80 MPa — low enough for hand-powered mills to process bar up to 10 mm thick. Cold rolling requires higher force but produces work-hardened, dimensionally precise sheet.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Cast iron or forged steel (rolls) | 30-60 kg | 100-200 mm diameter × 200-400 mm face, hardened to 50-55 HRC surface | [Iron & Steel](../metals/iron-steel.md) | Chilled cast iron rolls (harder surface, more brittle) |
| Cast iron or steel plate (frame) | 50-150 kg | 20 mm minimum thickness for hand mill | [Casting](casting.md) | Welded steel frame (requires machining) |
| Fine-pitch threaded rod (screw-down) | 2 | M20, 1.5 mm pitch, 200-300 mm long | [Machining](machining.md) | Standard threaded rod (coarser adjustment) |
| Spur gears | 2 | 20-tooth, 2.5 module, matching roll spacing | [Machining](machining.md) | Chain drive (less precise synchronization) |
| Bronze bushings (bearings) | 4 | Matched to roll journal diameter, 0.02-0.05 mm clearance | [Casting](casting.md) | Lubricated cast iron bores (higher friction) |
| Hand crank | 1 | 300 mm radius handle with grip | [Forming](forming.md) | Chain wheel for powered drive |
| Steel key stock | 4 | 6 × 6 mm, for gear and crank mounting | [Iron & Steel](../metals/iron-steel.md) | Set screws (less secure) |

## Prerequisites

- [Casting capability](casting.md) — for cast iron rolls and frame, or access to forged steel stock
- [Machining capability](machining.md) — for turning rolls concentric, boring bearing housings, cutting gear teeth
- [Iron and steel stock](../metals/iron-steel.md) — medium-carbon steel for rolls, structural steel for frame
- [Bronze casting](casting.md) — for bushings (or steel bearings with grease lubrication)

## Construction Steps

### Rolls

1. **Cast or forge the rolls**: For a hand mill, cast two rolls from chilled cast iron (or forge from medium-carbon steel), 100 mm diameter × 200 mm face length. Cast the journals integral with the roll body: 30 mm diameter × 80 mm long on each end.
2. **Turn the rolls**: Mount each roll between centers on the lathe. Turn the roll face concentric to the journals within ±0.02 mm runout. Turn the journals to 30 mm diameter, fitting the bearing bushings.
3. **Harden the roll faces** (if steel): Heat to 820-850°C, quench in oil, temper at 350-400°C to 50-55 HRC. Grind the faces on a cylindrical grinder (or lathe-mounted grinding attachment) to final diameter with 0.8 μm Ra finish. Chilled cast iron rolls are already hard and only need grinding.

### Frame

4. **Fabricate the frame**: Cast a one-piece frame from gray cast iron, or weld from 20 mm steel plate. The frame has two vertical housings with bore pairs for the roll bearings. The housing bore centers must be parallel within 0.03 mm over the 200 mm face width.
5. **Bore bearing housings**: Bore the upper and lower bearing housing bores to 35.00 mm ±0.02 mm (to accept the bronze bushings). The lower bores are fixed; the upper bores are in sliding blocks that move vertically in guideways.
6. **Machine the guide ways**: Mill the vertical guide ways for the upper bearing blocks to 0.05 mm clearance on each side. The blocks must slide freely without tilting — tilt causes uneven roll gap.

### Screw-Down Mechanism

7. **Make the screw-down assemblies**: Thread the M20 × 1.5 mm holes in the top of the frame (or in separate bridge plates). Insert the fine-pitch threaded rods through bronze thrust washers into the upper bearing blocks. Each full turn of the screw adjusts the roll gap by 1.5 mm.
8. **Add calibrated dials**: Attach graduated dials to the screw-down rods. Mark 0.1 mm increments (each 1/15 turn = 0.1 mm). Both screw-downs must be adjustable independently to set a parallel gap.

### Drive

9. **Cut gear teeth**: Cut 20-tooth spur gears (2.5 module) on the roll journal extensions. The gears synchronize the two rolls so they rotate at the same speed. Key the gears to the journals with 6 × 6 mm key stock.
10. **Mount the crank**: Fix a hand crank (300 mm radius) on one roll journal. For added torque, install a 3:1 chain or gear reduction between the crank and the roll. A second operator feeds stock while the first cranks.

### Assembly

11. **Assemble rolls in frame**: Press the bronze bushings into the bearing housings. Insert the lower roll, then the upper roll. Engage the synchronizing gears. Install the screw-down mechanism on the upper bearing blocks.
12. **Set the roll gap**: Set the roll gap to zero (rolls just touching). Use a feeler gauge to verify both ends are equal. Back off each screw-down by equal amounts to set the desired gap.

## Calibration and Verification

1. **Roll gap uniformity**: Set the gap to a known value using the calibrated dials. Pass a 1 mm thick feeler gauge through the gap at three positions (center and both ends). The gap must be uniform within ±0.05 mm across the face width.
2. **Test strip**: Roll a 5 mm thick copper bar through a 3 mm gap setting. Measure the rolled thickness at three points along the length and at both edges. Thickness variation must be <0.1 mm.
3. **Runout check**: Mount a dial indicator against each roll face. Rotate the roll by hand. Total indicated runout must be <0.02 mm.
4. **Gear mesh**: Check that both rolls rotate smoothly together with no binding or backlash in the synchronizing gears. Apply grease to the gear teeth.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Roll pressure (hot steel, 15-20% reduction) | 50-150 kN |
| Capacity — hot rolling | Copper, bronze, soft iron bar up to ~10 mm thick |
| Capacity — cold rolling | Copper and brass sheet to ~1 mm |
| Minimum strip thickness (copper) | 0.5 mm with careful gap setting |
| Throughput (hand operation) | 2-5 kg/hour |
| Roll gap adjustment resolution | 0.1 mm per dial division |
| Roll face flatness | ±0.02 mm |
| Roll concentricity | ±0.02 mm runout |

### Powered Version (Water Wheel or Engine)

| Parameter | Value |
|-----------|-------|
| Roll diameter | 200-400 mm |
| Face width | 400-800 mm |
| Drive power | 3-10 HP minimum |
| Capacity (hot steel) | 50 mm square bloom to 10 mm round in 6-10 passes |
| Reduction per pass | 15-25% for hot steel |

## Strengths

- Produces uniform strip and bar with consistent cross-section — impossible to achieve by hammer forging
- Cold rolling work-hardens the metal, increasing yield strength by 50-100% for non-ferrous alloys
- Simple mechanical design — no external power required for hand-operated version

## Weaknesses

- Hand-powered capacity is limited to bar <10 mm thick (hot) or sheet <1 mm thick (cold, copper)
- Roll gap must be adjusted precisely — uneven gap produces tapered strip
- Two operators required (one cranks, one feeds stock) for continuous operation

## Variations

- **Two-high**: The simplest design — two rolls, one above the other. Stock passes through in one direction, then the gap is opened to return it (non-reversing). Or the mill reverses direction for each pass.
- **Three-high**: Three rolls stacked vertically. Stock passes through the upper pair in one direction, then through the lower pair on the return. No gap adjustment needed between passes — the upper and lower gaps are pre-set for progressive reduction. Higher throughput than two-high.
- **Four-high**: Two small work rolls supported by two large backup rolls. The backup rolls prevent the work rolls from deflecting under load, enabling precise gauge on wide sheet. Required for sheet <0.5 mm thickness.
- **Tandem**: Multiple stands in series, each reducing thickness progressively. Used for high-volume sheet production at 50-200 m/min line speed.

## See Also

- [Forming](forming.md) — rolling operations and procedures using the mill
- [Casting](casting.md) — casting the rolls and frame
- [Machining](machining.md) — machining rolls, gears, and bearing housings
- [Iterative Bootstrap](iterative-bootstrap.md) — machine tool construction sequence
- [Iron & Steel](../metals/iron-steel.md) — steel stock for mill construction

[← Back to Machine Tools](index.md)
