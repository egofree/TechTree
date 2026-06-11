# Water Frame (Arkwright)

> **Node ID**: textiles.spinning-frame.water
> **Domain**: [Textiles](./index.md)
> **Parent**: [Spinning Frame](spinning-frame.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`textiles.spinning`](spinning.md)
> **Enables**: [`textiles.weaving`](weaving.md) (firm warp yarn supply)
> **Timeline**: Years 15-20
> **Outputs**: firm, even warp yarn at 10-50× hand spinning rate
> **Critical**: Yes — mechanized spinning breaks the hand-spinning bottleneck that limited cloth production to the pace of individual spinners

## Principle

The water frame (Arkwright, 1769) uses pairs of rollers to draw fiber out (drafting), each successive pair rotating faster than the last. A typical 4-pair roller system increases surface speed 4-8× from first to last pair, attenuating the roving to the target thickness. The final pair feeds the attenuated fiber to a flyer that inserts twist. The water frame produces firm, even yarn suitable for warp — the critical bottleneck that limited hand spinning to weft-only production. Roller diameters: 25 mm typical, ground smooth to ±0.02 mm.

## Prerequisites

- [Precision machining](../machine-tools/machining.md) — rollers bored and ground to ±0.02 mm, spindles turned true
- [Iron & Steel](../metals/iron-steel.md) — cast iron frames, forged steel rollers
- [Bearings](../machine-tools/bearings-abrasives.md) — reliable plain or roller bearings for high-speed spindles (4,000-6,000 rpm)
- [Power source](../energy/index.md) — water wheel (original) or steam engine. Minimum 2-5 kW for a 100-spindle frame.
- [Spinning](spinning.md) — fiber preparation (carding, combing, roving) as input to the frame

## Materials

| Material | Quantity (100-spindle frame) | Specifications | Source | Alternatives |
|----------|:---------------------------:|----------------|--------|-------------|
| Cast iron (frame) | 500-1000 kg | Grade 25 or higher, bed and uprights | [Iron & Steel](../metals/iron-steel.md) | Welded steel plate (lighter, requires welding) |
| Steel bar (rollers) | 50-100 kg | 1045 or equivalent, 25 mm diameter, ground to ±0.02 mm | [Iron & Steel](../metals/iron-steel.md) | Chilled cast iron rollers (shorter life) |
| Steel wire (spindles) | 20-50 kg | 12-16 mm diameter, turned and polished | [Iron & Steel](../metals/iron-steel.md) | None — precision spindles required |
| Leather or rubber (roller cots) | 100-200 pcs | 25 mm ID, 2-3 mm wall, shore A 65-80 | [Polymers](../polymers/index.md) | Leather (shorter life, less consistent grip) |
| Bearings | 200-400 pcs | Plain bronze or ball bearings for spindles | [Bearings](../machine-tools/bearings-abrasives.md) | Wooden bearings with oil cups (short life at high rpm) |
| Drive belts | 5-15 m | Leather or canvas, 50-100 mm wide | [Leather](../animals/leather.md) | Rope drive (less efficient) |
| Bolts and fasteners | 20-50 kg | Grade 8.8, M8-M16 | [Iron & Steel](../metals/iron-steel.md) — fabricated in-house | Riveted joints (non-adjustable) |

## Construction Steps

1. **Cast the frame**: Pour cast iron into sand molds for the bed plate (2000 × 400 × 50 mm) and two upright columns (1500 × 200 × 150 mm). The bed must be flat within 0.1 mm over its length — machine the top surface on a planer. Bolt uprights to the bed with 4 × M16 bolts per column, aligned perpendicular within 0.05 mm per 100 mm.

2. **Machine the rollers**: Turn 25 mm diameter steel bar to ±0.02 mm cylindricity in sets of matched pairs. Each pair must have identical diameters (matched within 0.01 mm) for even drafting. Grind the surface to 0.4 μm Ra finish. Mount in bearing blocks bored to 25.00 +0.02/-0.00 mm. For a 4-pair drafting system: pairs 1-2 handle coarse feed, pairs 3-4 handle fine draft.

3. **Set drafting ratios**: Gear the roller drives so each successive pair rotates faster. Surface speed ratio between consecutive pairs: 1.5-2.0×. Total draft ratio (last pair to first): 4-8× for medium yarn, 10-20× for fine yarn. Change gears allow ratio adjustment for different yarn counts. Mount change gears on a lay shaft with sliding key engagement.

4. **Mount the spindles**: Install 4-8 spindles per frame (early water frames) on the spindle rail, spaced 80-100 mm apart. Each spindle is a 12-16 mm steel shaft running in two bearings, with a whorl (pulley) at the base driven by a continuous cord from the tin roller (cylinder drum). Spindle speed: 4,000-6,000 rpm. Mount flyers (U-shaped brackets with hooks) on each spindle to guide yarn onto the bobbin.

5. **Install the bobbin rail**: A horizontal rail that traverses up and down (via a cam mechanism on the main shaft) to build yarn evenly on the bobbin. Traverse speed: 20-40 cycles per minute. Guide eyes above each spindle align yarn to the bobbin center.

6. **Connect drive system**: Mount a main drive shaft running the length of the frame, driven by belts from the power source (water wheel, steam engine, or motor). The main shaft drives the roller gear train via change gears, and the tin roller (spindle drive) via a separate belt.

## Calibration and Verification

1. **Roller alignment**: Check that all roller pairs are parallel within 0.05 mm per 100 mm of width using a precision straightedge. Misaligned rollers produce uneven drafting and slubs.

2. **Spindle speed balance**: Run all spindles at full speed without yarn. Measure vibration at each spindle with a dial indicator — maximum runout 0.03 mm. Re-balance or replace spindles exceeding this limit. Imbalance at 5,000+ rpm causes destructive vibration.

3. **Drafting ratio verification**: Feed a measured length of colored roving through the rollers. Measure the length of the drafted output. Actual draft ratio = output length / input length. Compare to calculated gear ratio — must match within ±2%.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Spindles per frame | 4-8 (early), 40-80 (later) |
| Spindle speed | 4,000-6,000 rpm |
| Yarn production per spindle | 0.1-0.3 kg/hour |
| Draft ratio | 4-8× (adjustable via change gears) |
| Yarn count range | Ne 10-40 (medium count) |
| Power consumption | 2-5 kW per 100 spindles |
| Roller surface speed | 5-40 m/min (graduated) |
| Service life | 20-40 years with bearing and cot replacement |

## Strengths

- Produces firm, even warp yarn — breaks the hand-spinning bottleneck that limited textile production
- 100-spindle frame replaces 50-100 hand spinners — dramatic labor reduction

## Weaknesses

- Requires precision-turned rollers (±0.02 mm) and reliable high-speed bearings
- Rollers crush fibers if pressure is uneven — roller cots need frequent replacement

## Safety

- **High-speed spindles**: Spindles at 4,000-6,000 rpm contain significant rotational energy. Guard all spindle rails. A broken spindle becomes a projectile. Inspect spindles for cracks and fatigue before each shift.
- **Entanglement**: Loose clothing, hair, or jewelry caught in rotating rollers or drive belts causes severe injury. Wear fitted clothing. Tie back long hair. Guard all drive belts and gears.
- **Dust and fly**: Carding and spinning generate fiber dust (fly). Prolonged inhalation causes byssinosis ("brown lung"). Ventilate spinning rooms. Wear dust masks in enclosed areas.
- **Drive belts**: Leather and canvas belts at high speed can break and whip. Guard belt runs. Maintain belt tension — loose belts slip and fray.

## Maintenance

**Daily checks** (before each shift):
- Check roller cots (rubber or leather covers on drafting rollers) for grooves, cracks, or glazing. Worn cots grip fiber unevenly, producing slubs and drafting faults. Rotate or replace cots showing wear grooves deeper than 0.5 mm.
- Oil spindle bearings: 2-3 drops of spindle oil (light mineral oil, ISO VG 10-22) per bearing. Under-lubricated bearings generate heat and wear rapidly at 5,000+ rpm.

**Weekly maintenance**:
- Check drafting roller alignment with a precision straightedge. Misalignment greater than 0.05 mm per 100 mm produces uneven drafting and slubs. Adjust bearing block positions.
- Inspect drive belts for tension, cracks, and alignment. A belt that tracks off the pulley edge will fray and break within hours.
- Clean accumulated fly (fiber dust) from around the spindle rail and roller assemblies.

**Monthly maintenance**:
- Check spindle runout with a dial indicator. Maximum acceptable runout: 0.03 mm at the spindle tip. Higher runout causes vibration, yarn breaks, and uneven package building. Re-balance or replace spindles exceeding this limit.

## See Also

- [Spinning Frame (overview)](spinning-frame.md) — parent article covering all spinning frame types
- [Spinning](spinning.md) — hand spinning methods, fiber preparation, twist and yarn properties
- [Weaving](weaving.md) — loom-based cloth production from spun yarn
- [Carding Machine](carding-machine.md) — fiber preparation for spinning frame feed
- [Machine Tools](../machine-tools/index.md) — precision machining for rollers and spindles
- [Energy](../energy/index.md) — power sources for driving spinning frames

---
*Part of the [Bootciv Tech Tree](../../index.md) • [Textiles](./index.md) • [All Domains](../../index.md)*
