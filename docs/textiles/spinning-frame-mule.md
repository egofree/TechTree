# Spinning Mule (Crompton)

> **Node ID**: textiles.spinning-frame.mule
> **Domain**: [Textiles](./index.md)
> **Parent**: [Spinning Frame](spinning-frame.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`textiles.spinning`](spinning.md)
> **Enables**: [`textiles.weaving`](weaving.md) (finest yarn supply for quality cloth)
> **Timeline**: Years 17-25
> **Outputs**: finest, most uniform yarn of any spinning system (Ne 20-200+)
> **Critical**: No — produces premium yarn; water frame and ring frame handle bulk production

## Principle

The spinning mule (Crompton, 1779) combines water frame roller drafting with carriage travel. The carriage moves outward 1.5-2 m while rollers feed roving and spindles rotate, simultaneously drafting and twisting. On the return stroke, the wound yarn is deposited onto the spindle. The mule produces the finest, most uniform yarn of any system — fine enough to match hand-spun muslin. By the 1830s, mules carried 300-1,300+ spindles. The self-acting mule (1830s) automated the carriage return, eliminating manual pushing.

## Prerequisites

- [Precision machining](../machine-tools/machining.md) — rollers bored and ground to ±0.02 mm, spindles turned true, carriage rails machined flat
- [Iron & Steel](../metals/iron-steel.md) — cast iron headstock, forged steel rollers, iron or steel carriage frame
- [Bearings](../machine-tools/bearings-abrasives.md) — reliable bearings for spindle and carriage wheel assemblies
- [Power source](../energy/index.md) — steam engine (standard) or water wheel. 5-15 kW per 500 spindles.
- [Spinning](spinning.md) — fiber preparation (carding, combing, roving) as input to the mule

## Materials

| Material | Quantity (500-spindle mule) | Specifications | Source | Alternatives |
|----------|:---------------------------:|----------------|--------|-------------|
| Cast iron (headstock) | 500-1000 kg | Grade 25 or higher, machined flat | [Iron & Steel](../metals/iron-steel.md) | None — rigidity required |
| Steel bar (rollers) | 50-100 kg | 1045 or equivalent, 25 mm diameter, ground to ±0.02 mm | [Iron & Steel](../metals/iron-steel.md) | Chilled cast iron rollers (shorter life) |
| Steel wire (spindles) | 100-300 kg | 12-16 mm diameter, turned and polished | [Iron & Steel](../metals/iron-steel.md) | None — precision spindles required |
| Iron or wood (carriage) | 200-500 kg | 1.5-2 m wide frame on wheeled carriage | [Iron & Steel](../metals/iron-steel.md) | Wooden carriage (shorter life) |
| Leather or rubber (roller cots) | 100-200 pcs | 25 mm ID, 2-3 mm wall, shore A 65-80 | [Polymers](../polymers/index.md) | Leather (shorter life) |
| Bearings | 500-1300 pcs | Plain bronze or ball bearings for spindles | [Bearings](../machine-tools/bearings-abrasives.md) | Wooden bearings (short life) |
| Drive belts | 10-30 m | Leather or canvas, 50-100 mm wide | [Leather](../animals/leather.md) | Rope drive (less efficient) |
| Carriage rails | 2 × 2-3 m | Iron or steel, machined flat and parallel | [Iron & Steel](../metals/iron-steel.md) | Wooden rails (wear quickly) |

## Construction Steps

1. **Construct the carriage**: Build a carriage frame (wooden or iron, 1.5-2 m wide) on wheels running on rails. The carriage carries the spindles (mounted at an angle, typically 45° from horizontal) and moves outward from the rollers during drafting, then returns to wind yarn.

2. **Install the headstock**: The fixed frame at one end holds the roller drafting system, the drive mechanism, and the cam that controls carriage movement. The headstock connects to the carriage via a counterfaller and faller wire mechanism that controls yarn tension during the inward (winding) stroke.

3. **Connect carriage drive**: The carriage is driven by a scroll cam on the main shaft that converts rotary motion to the linear carriage travel. Carriage speed: outward stroke at 0.5-1.0 m/s, return stroke at 0.3-0.5 m/s. The total carriage travel is 1.5-2 m.

## Calibration and Verification

1. **Roller alignment**: Check that all roller pairs are parallel within 0.05 mm per 100 mm of width using a precision straightedge. Misaligned rollers produce uneven drafting and slubs.

2. **Spindle speed balance**: Run all spindles at full speed without yarn. Measure vibration at each spindle with a dial indicator — maximum runout 0.03 mm.

3. **Drafting ratio verification**: Feed a measured length of colored roving through the rollers. Measure the length of the drafted output. Actual draft ratio = output length / input length. Compare to calculated gear ratio — must match within ±2%.

4. **Carriage travel**: Verify carriage moves smoothly along full 1.5-2 m travel without binding. Check rail alignment and wheel bearing condition.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Spindles per mule | 300-1,300+ |
| Spindle speed | 5,000-8,000 rpm |
| Carriage travel | 1.5-2 m stroke |
| Yarn production per spindle | 0.08-0.2 kg/hour |
| Yarn count range | Ne 20-200+ (finest yarn of any system) |
| Cycles per minute | 3-5 stretch/wind cycles |
| Power consumption | 5-15 kW per 500 spindles |

## Strengths

- Produces the finest, most uniform yarn of any system — fine enough to match hand-spun muslin
- High spindle count (300-1,300+) enables mass production of premium yarns
- Self-acting mule (1830s) eliminates manual carriage pushing

## Weaknesses

- Carriage mechanism is mechanically complex — self-acting mule has 100+ moving parts
- Lower production rate per spindle than ring frame (intermittent vs. continuous motion)
- Requires skilled oversight for setup and changeovers

## Safety

- **High-speed spindles**: Spindles at 5,000-8,000 rpm contain significant rotational energy. Guard all spindle rails. A broken spindle becomes a projectile.
- **Entanglement**: Loose clothing, hair, or jewelry caught in rotating rollers, drive belts, or the moving carriage causes severe injury. Wear fitted clothing. Tie back long hair. Guard all drive belts and gears.
- **Dust and fly**: Carding and spinning generate fiber dust (fly). Prolonged inhalation causes byssinosis ("brown lung"). Ventilate spinning rooms. Wear dust masks in enclosed areas.
- **Carriage pinch points**: The moving carriage creates pinch points against the headstock. Guard the carriage path. Keep hands clear during operation.

## Maintenance

**Daily checks** (before each shift):
- Check roller cots for grooves, cracks, or glazing. Rotate or replace cots showing wear grooves deeper than 0.5 mm.
- Oil spindle bearings: 2-3 drops of spindle oil (light mineral oil, ISO VG 10-22) per bearing.
- Inspect carriage rails for debris and wheel bearings for smooth operation.

**Weekly maintenance**:
- Check drafting roller alignment with a precision straightedge.
- Inspect drive belts for tension, cracks, and alignment.
- Clean accumulated fly from around the spindle rail, carriage, and roller assemblies.
- Lubricate carriage wheel bearings and check rail alignment.

**Monthly maintenance**:
- Check spindle runout with a dial indicator. Maximum acceptable runout: 0.03 mm at the spindle tip.
- Inspect scroll cam and counterfaller mechanism for wear. The cam profile determines carriage motion — a worn cam causes irregular drafting.
- Check faller wire guides for wear grooves.

## Yarn Quality Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Uneven yarn (slubs) | Roller pressure uneven, worn cots, or drafting ratio too high for fiber length | Replace worn roller cots. Reduce draft ratio. Check roller alignment. |
| Frequent yarn breaks | Spindle vibration, or yarn too thin for spindle speed | Balance spindles. Reduce spindle speed for finer yarn. Check roving uniformity. |
| Mule yarn too hairy | Insufficient twist or drafting too aggressive | Increase twist (higher spindle speed or slower carriage). Reduce draft ratio. |
| Yarn count variation | Drafting ratio fluctuating or roving feed inconsistent | Check change gears for worn teeth. Verify roving bobbin tension in the creel. |

## See Also

- [Spinning Frame (overview)](spinning-frame.md) — parent article covering all spinning frame types
- [Spinning](spinning.md) — hand spinning methods, fiber preparation, twist and yarn properties
- [Weaving](weaving.md) — loom-based cloth production from spun yarn
- [Carding Machine](carding-machine.md) — fiber preparation for spinning frame feed
- [Machine Tools](../machine-tools/index.md) — precision machining for rollers and spindles
- [Energy](../energy/index.md) — power sources for driving spinning frames

---
*Part of the [Bootciv Tech Tree](../index.md) • [Textiles](./index.md) • [All Domains](../index.md)*
