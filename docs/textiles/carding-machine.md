# Carding Machine

> **Node ID**: textiles.carding-machine
> **Domain**: [Textiles](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`textiles.spinning`](spinning.md)
> **Enables**: [`textiles.spinning-frame`](spinning-frame.md) (uniform roving feed for mechanized spinning)
> **Timeline**: Years 10-20
> **Outputs**: carded batt (aligned fiber sheet), carded roving
> **Critical**: Yes — drum carding produces the uniform fiber batts required for mechanized spinning at 10-20× the rate of hand carding

## Principle

A carding machine aligns textile fibers from a tangled mass into a parallel sheet (batt) using rotating drums covered in card clothing — stiff wire teeth set in a flexible backing. The machine uses two drums: a large main cylinder (20-40 cm diameter) covered with fine wire teeth rotating at 100-200 rpm, and a smaller licker-in roller (10-15 cm diameter) rotating at 300-600 rpm that feeds fiber onto the main cylinder. A doffer roller (15-25 cm diameter) running opposite to the main cylinder strips the carded batt off.

The key mechanism is "carding action": two surfaces covered in wire teeth moving relative to each other. When the teeth point in the same direction and the surfaces move in opposite directions (or at different speeds in the same direction), the teeth comb through the fiber mass, separating and aligning individual fibers. The working angle of the wire teeth (20-35° from perpendicular) determines whether fiber is held (carding point) or released (stripping point).

Carding converts 0.5-1 kg/hour of hand-carded fiber output to 5-10 kg/hour throughput, making it the essential link between fiber preparation and mechanized spinning. Without drum carding, a spinning frame cannot be fed fast enough to justify its construction cost.

## Prerequisites

- [Iron & Steel](../metals/iron-steel.md) — wire for card clothing, shafts for drums
- [Machine Tools](../machine-tools/index.md) — turning drums, boring bearing housings
- [Leather or Rubber](../animals/leather.md) — flexible backing for card clothing
- [Power source](../energy/index.md) — hand crank for small units, water wheel or motor for production units (0.5-2 kW)

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Cast iron (drums) | 30-60 kg | Main cylinder 20-40 cm dia × 40-60 cm wide, licker-in 10-15 cm dia, doffer 15-25 cm dia | [Iron & Steel](../metals/iron-steel.md) | Hardwood drums (lighter, less stable, shorter life) |
| Steel shafts | 3 pcs, 10-15 kg | 20-30 mm diameter, ground to ±0.05 mm | [Iron & Steel](../metals/iron-steel.md) | None — precision required |
| Card wire | 5-15 kg | 28-32 gauge steel wire, hardened, bent to 20-35° angle, 5-10 mm projection | [Iron & Steel](../metals/iron-steel.md) | Hand-card wire teeth (slower production) |
| Leather or rubber backing | 1-2 m² | 3-5 mm thick flexible sheet, wrapped around drums | [Leather](../animals/leather.md) | Rubber sheet (better grip, less available) |
| Bearings | 6-12 pcs | Bronze plain bearings or ball bearings | [Bearings](../machine-tools/bearings-abrasives.md) | Wooden bearings with oil cups (shorter life) |
| Frame timber or angle iron | 20-40 kg | Sturdy frame supporting drum shafts at precise centers | [Iron & Steel](../metals/iron-steel.md) | Hardwood frame (heavier, absorbs vibration) |
| Drive gears or belts | 1 set | Step-down ratio 2:1 to 6:1 between licker-in and main cylinder | [Metals](../metals/index.md) | Rope drive (less positive) |
| Bolts and fasteners | 5-10 kg | M8-M12 | [Fasteners](../metals/fasteners.md) | Through-bolts with nuts |

## Construction Steps

### Frame

1. **Build the frame**: Construct a rigid frame from angle iron (50 × 50 × 5 mm) or hardwood (100 × 100 mm posts). The frame must hold three parallel shafts at precise center distances: licker-in to main cylinder gap 0.3-0.8 mm, main cylinder to doffer gap 0.3-0.5 mm. Bore bearing housings in the frame with a jig to maintain alignment — shaft centers must be parallel within 0.1 mm over the full drum width. Any misalignment causes uneven carding and fiber buildup.

2. **Mount bearing blocks**: Install split-bearing housings (bronze bushings) at each shaft position. The bearing housings for the licker-in and doffer must be adjustable — slots in the frame allow these drums to be moved closer to or farther from the main cylinder, setting the critical carding gap.

### Drums

3. **Prepare the main cylinder**: Turn the main cylinder (cast iron, 20-40 cm diameter × 40-60 cm wide) on a lathe. The surface must be concentric within 0.05 mm and smooth (1.6 μm Ra). Balance the cylinder statically — an unbalanced drum at 200 rpm vibrates destructively. Drill and tap mounting holes for the card clothing attachment clips at each end.

4. **Wrap card clothing on the main cylinder**: Cut card cloth (leather or rubber backing with embedded wire teeth) to the cylinder circumference length plus 10 mm overlap. Apply adhesive (hide glue or rubber cement) to the cylinder surface. Wrap the card cloth tightly around the cylinder, teeth pointing in the direction of rotation. Secure the leading and trailing edges with flat iron clips screwed into the cylinder ends. The teeth must be uniform in height (±0.5 mm) — uneven teeth produce uneven carding.

5. **Prepare the licker-in roller**: Turn the licker-in (10-15 cm diameter × 40-60 cm wide) to the same surface finish as the main cylinder. Wrap with coarser card cloth (fewer, stouter teeth — the licker-in opens the fiber mass before it reaches the fine main cylinder). Licker-in wire: 20-25 gauge, 8-12 mm projection, 30-35° working angle.

6. **Prepare the doffer roller**: Turn the doffer (15-25 cm diameter × 40-60 cm wide) and wrap with fine card cloth. The doffer must strip fiber cleanly from the main cylinder — its teeth are slightly finer and set at a stripping angle (opposite to main cylinder teeth direction).

### Assembly and Drive

7. **Mount drums in frame**: Install the main cylinder first, then adjust the licker-in and doffer positions to set the carding gaps. Licker-in to main cylinder: 0.3-0.8 mm (wider for coarse fiber like wool, narrower for fine fiber like cotton). Main cylinder to doffer: 0.3-0.5 mm. Check gaps with a feeler gauge at both ends and the center of each drum.

8. **Install drive system**: Connect a hand crank, foot treadle, or motor to the main cylinder shaft. Gear or belt-drive the licker-in from the main cylinder at 2-4× the main cylinder speed (the licker-in must rotate faster to open the feed). Gear or belt-drive the doffer at 0.5-1.0× the main cylinder speed (the doffer runs slower to condense the fiber web). A typical speed ratio: main cylinder 150 rpm, licker-in 400-600 rpm, doffer 80-120 rpm.

9. **Install feed tray and doffer comb**: Mount a feed tray (flat wooden or metal surface) above the licker-in where the operator places loose fiber. Install a doffer comb (thin steel blade set 0.5-1.0 mm from the doffer surface) that peels the carded batt off the doffer as a continuous web.

10. **Install batt take-up**: Guide the carded batt from the doffer comb through a pair of calender rollers (smooth steel rollers, 30-50 mm diameter, spring-loaded to compress the batt) and onto a collection spool or tray. The calender rollers consolidate the loose batt into a coherent sheet.

## Calibration and Verification

1. **Gap check**: Measure the gap between licker-in and main cylinder, and between main cylinder and doffer, at three positions (both ends and center). Use a 0.3 mm feeler gauge for fine carding, 0.5-0.8 mm for coarse. Adjust drum positions until gaps are uniform within ±0.1 mm across the width.

2. **Rotation direction verification**: The main cylinder and doffer must counter-rotate at the carding point (surfaces move in opposite directions). The licker-in and main cylinder surfaces must also move in opposite directions at their nip point. Verify by hand-cranking before applying power.

3. **Balance test**: Run the main cylinder at full speed (150-200 rpm) without card cloth. Measure vibration amplitude at each bearing housing — maximum 0.05 mm. If vibration exceeds this, add balance weights to the cylinder rim.

4. **Carding quality test**: Feed 100 g of prepared fiber through the machine. Inspect the output batt: fibers should be uniformly aligned parallel to the machine direction, with no clumps, neps (tangled fiber balls), or uncarded patches. If neps appear, reduce the feed rate or tighten the carding gap.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Main cylinder diameter | 20-40 cm |
| Throughput (fiber) | 5-10 kg/hour |
| Output form | Continuous batt, 40-60 cm wide, 1-3 mm thick |
| Main cylinder speed | 100-200 rpm |
| Licker-in speed | 300-600 rpm |
| Doffer speed | 80-120 rpm |
| Carding gap (licker-in to cylinder) | 0.3-0.8 mm |
| Carding gap (cylinder to doffer) | 0.3-0.5 mm |
| Power requirement | 0.5-2 kW (hand-cranked or motorized) |
| Wire tooth life | 2,000-5,000 hours (replace card cloth) |
| Drum balance tolerance | ≤0.05 mm vibration amplitude |

## Strengths

- 5-10 kg/hour throughput vs. 0.5-1 kg/hour for hand cards — 10× productivity gain
- Produces uniform batts suitable for feeding spinning frames — essential link in mechanized textile production
- Continuous output (batt or roving) vs. discrete rolags from hand carding — integrates with downstream machinery
- Handles wool, cotton, and short-staple fibers with the same machine (adjust gap and wire gauge)

## Weaknesses

- Card clothing (wire teeth in leather/rubber backing) wears out in 2,000-5,000 hours and must be re-wrapped — time-consuming maintenance
- Drum balance is critical — an unbalanced 30 cm drum at 200 rpm vibrates destructively within hours
- Carding gap must be set precisely (0.3-0.8 mm) — too wide produces neps, too tight cuts fibers
- Wire teeth bend or break if foreign objects (twigs, metal fragments) enter with the fiber

## Safety

- **Rotating drums**: The main cylinder and licker-in present nip hazards where clothing, hair, or fingers can be drawn in. Guard all nip points. Never reach into the feed tray while the machine is running. Use a push stick to feed fiber.
- **Wire teeth**: Card wire is sharp. Handling card cloth or reaching near drums without guards causes puncture wounds and lacerations. Wear leather gloves when handling card clothing.
- **Dust and fly**: Carding generates fine fiber dust at 5-10× the rate of hand carding. Ventilate the carding area. Wear a dust mask — chronic inhalation causes byssinosis.
- **Entanglement in drive belts**: Guard all belts and gears. Loose clothing catches in rotating shafts.

## See Also

- [Spinning](spinning.md) — hand spinning methods, fiber properties, hand cards
- [Spinning Frame](spinning-frame.md) — industrial spinning machines fed by carded batts
- [Fibers](fibers.md) — fiber types, preparation, and properties
- [Machine Tools](../machine-tools/index.md) — precision turning for drums and shafts
- [Bearings](../machine-tools/bearings-abrasives.md) — bearing selection for rotating drums

[← Back to Textiles](index.md)
