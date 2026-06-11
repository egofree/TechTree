# Ring Spinning Frame (Thorpe)

> **Node ID**: textiles.spinning-frame.ring
> **Domain**: [Textiles](./index.md)
> **Parent**: [Spinning Frame](spinning-frame.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`textiles.spinning`](spinning.md)
> **Enables**: [`textiles.weaving`](weaving.md) (mass-scale yarn supply)
> **Timeline**: Years 18-25
> **Outputs**: yarn at industrial scale (continuous motion, dominant spinning system)
> **Critical**: Yes — by 1900 ring spinning produced ~80% of the world's cotton yarn; remains dominant today (~70% of short-staple spinning)

## Principle

Ring spinning (Thorpe, 1828) uses a C-shaped traveler (small wire loop) that rotates around a ring at 3,000-15,000 rpm, simultaneously inserting twist and winding yarn onto the bobbin. No carriage stroke needed — continuous motion. Simpler mechanism, faster production than mule spinning. The ring rail traverses vertically to build yarn packages evenly on the bobbin.

## Prerequisites

- [Precision machining](../machine-tools/machining.md) — rollers bored and ground to ±0.02 mm, spindles turned true, rings ground to precise inner diameter
- [Iron & Steel](../metals/iron-steel.md) — cast iron frames, forged steel rollers, hardened steel rings and travelers
- [Bearings](../machine-tools/bearings-abrasives.md) — reliable plain or roller bearings for high-speed spindles (8,000-15,000 rpm)
- [Power source](../energy/index.md) — electric motor (modern), steam engine, or water wheel. 3-8 kW per 100 spindles.
- [Spinning](spinning.md) — fiber preparation (carding, combing, roving) as input to the frame

## Materials

| Material | Quantity (100-spindle frame) | Specifications | Source | Alternatives |
|----------|:---------------------------:|----------------|--------|-------------|
| Cast iron (frame) | 500-1000 kg | Grade 25 or higher, bed and uprights | [Iron & Steel](../metals/iron-steel.md) | Welded steel plate (lighter, requires welding) |
| Steel bar (rollers) | 50-100 kg | 1045 or equivalent, 25 mm diameter, ground to ±0.02 mm | [Iron & Steel](../metals/iron-steel.md) | Chilled cast iron rollers (shorter life) |
| Steel wire (spindles) | 20-50 kg | 12-16 mm diameter, turned and polished | [Iron & Steel](../metals/iron-steel.md) | None — precision spindles required |
| Hardened steel (rings) | 100-200 pcs | Flanged ring, 40-55 mm inner diameter, 50-60 HRC | [Iron & Steel](../metals/iron-steel.md) | None — hardened rings essential for traveler life |
| Steel wire (travelers) | 200-400 pcs | C-shaped, 0.3-0.5 mm wire, hardened and tempered | [Iron & Steel](../metals/iron-steel.md) | None — wears out; consumable |
| Leather or rubber (roller cots) | 100-200 pcs | 25 mm ID, 2-3 mm wall, shore A 65-80 | [Polymers](../polymers/index.md) | Leather (shorter life, less consistent grip) |
| Bearings | 200-400 pcs | Plain bronze or ball bearings for spindles | [Bearings](../machine-tools/bearings-abrasives.md) | Wooden bearings with oil cups (short life at high rpm) |
| Drive belts | 5-15 m | Leather or canvas, 50-100 mm wide | [Leather](../animals/leather.md) | Rope drive (less efficient) |
| Bolts and fasteners | 20-50 kg | Grade 8.8, M8-M16 | [Iron & Steel](../metals/iron-steel.md) — fabricated in-house | Riveted joints (non-adjustable) |

## Construction Steps

1. **Cast and machine the frame**: Pour cast iron into sand molds for the bed plate and upright columns. Machine top surface flat within 0.1 mm. Add an inverter (U-shaped bracket) at the top of each spindle position to support the ring rail. The ring rail must traverse smoothly up and down.

2. **Install spindle-rail and spindles**: Mount spindles at 80-100 mm spacing on the spindle rail. Spindle speed: 8,000-15,000 rpm for modern machines; 3,000-5,000 rpm for early bootstrap versions. Higher speed requires better bearings and balance.

3. **Mount rings and travelers**: Press a hardened steel ring into the ring rail at each spindle position. Thread a C-shaped steel traveler onto each ring. The traveler rotates around the ring at high speed, inserting twist and winding yarn simultaneously. Ring inner diameter: 40-55 mm. Traveler weight: 20-80 mg depending on yarn count.

4. **Install ring rail lifting mechanism**: Connect the ring rail to a cam-driven lifting mechanism that traverses the rail up and down to build the bobbin package. The lift pattern (chase) determines package density. Typical chase: 30-50 mm. A reversing cam produces the tapered package shape (cop build).

5. **Install creel and guide eyes**: Mount a creel (rack) above the rollers to hold roving bobbins. Thread roving from the creel through guide eyes into the roller drafting system, then down through the traveler and ring to the bobbin.

## Calibration and Verification

1. **Roller alignment**: Check that all roller pairs are parallel within 0.05 mm per 100 mm of width using a precision straightedge. Misaligned rollers produce uneven drafting and slubs.

2. **Spindle speed balance**: Run all spindles at full speed without yarn. Measure vibration at each spindle with a dial indicator — maximum runout 0.03 mm. Re-balance or replace spindles exceeding this limit.

3. **Ring-traveler clearance**: Check that each traveler rotates freely on its ring without sticking. Apply a thin film of spindle oil to the ring. Spin the traveler by hand — it should complete 3+ revolutions from a single flick. Sticking travelers cause yarn breaks.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Spindles per frame | 100-1,000+ (modern), 20-100 (bootstrap) |
| Spindle speed | 3,000-5,000 rpm (early), 8,000-15,000 rpm (modern) |
| Yarn production per spindle | 0.15-0.5 kg/hour |
| Traveler speed | 3,000-15,000 rpm (matches spindle) |
| Yarn count range | Ne 6-100+ |
| Ring inner diameter | 40-55 mm |
| Power consumption | 3-8 kW per 100 spindles |
| Traveler life | 100-500 hours (consumable — hardened steel wears) |
| Ring life | 5,000-15,000 hours |

## Strengths

- Continuous motion (no carriage stroke) — simpler mechanism and faster than mule spinning
- Highest production rate per spindle of any spinning system
- By 1900, ring spinning produced ~80% of the world's cotton yarn; remains dominant today (~70% of short-staple)

## Weaknesses

- Travelers wear out in 100-500 hours — hardened steel consumable
- Requires precision-turned rollers (±0.02 mm) and reliable high-speed bearings
- Spindle speed limited by traveler weight and ring friction at very high speeds

## Safety

- **High-speed spindles**: Spindles at 8,000-15,000 rpm contain significant rotational energy. Guard all spindle rails. A broken spindle becomes a projectile. Inspect spindles for cracks and fatigue before each shift.
- **Entanglement**: Loose clothing, hair, or jewelry caught in rotating rollers or drive belts causes severe injury. Wear fitted clothing. Tie back long hair. Guard all drive belts and gears.
- **Dust and fly**: Carding and spinning generate fiber dust (fly). Prolonged inhalation causes byssinosis ("brown lung"). Ventilate spinning rooms. Wear dust masks in enclosed areas.
- **Noise**: Ring frames at 10,000+ rpm generate 85-95 dB. Hearing protection required for extended exposure.
- **Drive belts**: Leather and canvas belts at high speed can break and whip. Guard belt runs. Maintain belt tension — loose belts slip and fray.

## Maintenance

**Daily checks** (before each shift):
- Inspect travelers for wear. A worn traveler (rounded edges, thin wire) causes uneven twist and frequent yarn breaks. Replace worn travelers — they are consumable items with 100-500 hour life.
- Check roller cots for grooves, cracks, or glazing. Rotate or replace cots showing wear grooves deeper than 0.5 mm.
- Oil spindle bearings: 2-3 drops of spindle oil (light mineral oil, ISO VG 10-22) per bearing.

**Weekly maintenance**:
- Check drafting roller alignment with a precision straightedge. Misalignment greater than 0.05 mm per 100 mm produces uneven drafting and slubs. Adjust bearing block positions.
- Inspect drive belts for tension, cracks, and alignment.
- Clean accumulated fly from around the spindle rail, ring rail, and roller assemblies. Fly buildup interferes with traveler rotation and contaminates yarn.

**Monthly maintenance**:
- Measure ring wear with a bore gauge. Ring inner diameter increases with use; the traveler-to-ring clearance must stay within specification. Rings worn more than 0.1 mm over nominal diameter must be replaced.
- Check spindle runout with a dial indicator. Maximum acceptable runout: 0.03 mm at the spindle tip.
- Inspect the ring rail lifting cam for wear. The cam profile determines package shape — a worn cam produces uneven bobbins.

**Ring and traveler replacement schedule**:
- Travelers: replace every 100-500 operating hours depending on yarn count and spindle speed.
- Rings: replace every 5,000-15,000 operating hours. Ring surface finish degrades progressively.
- When replacing rings, clean the ring rail seat thoroughly before pressing in the new ring. Any debris under the ring causes misalignment.

## Yarn Quality Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Uneven yarn (slubs) | Roller pressure uneven, worn cots, or drafting ratio too high | Replace worn roller cots. Reduce draft ratio. Check roller alignment. |
| Frequent yarn breaks | Spindle vibration, worn traveler, or yarn too thin for spindle speed | Balance spindles. Replace worn travelers. Reduce spindle speed. |
| Traveler flying off ring | Traveler too light for spindle speed, or ring worn | Use heavier traveler weight. Replace worn rings. Reduce spindle speed. |
| Ring frame package density uneven | Ring rail lift timing off or chase too long/short | Adjust cam profile for lift pattern. Shorten chase for denser package. |
| Yarn hairiness (excessive fiber protrusion) | Traveler too light, ring worn, or spindle speed too high | Increase traveler weight. Replace worn rings. Reduce spindle speed by 10-15%. |
| Yarn count variation | Drafting ratio fluctuating or roving feed inconsistent | Check change gears for worn teeth. Verify roving bobbin tension. Clean guide eyes. |

## See Also

- [Spinning Frame (overview)](spinning-frame.md) — parent article covering all spinning frame types
- [Spinning](spinning.md) — hand spinning methods, fiber preparation, twist and yarn properties
- [Weaving](weaving.md) — loom-based cloth production from spun yarn
- [Carding Machine](carding-machine.md) — fiber preparation for spinning frame feed
- [Machine Tools](../machine-tools/index.md) — precision machining for rollers and spindles
- [Bearings](../machine-tools/bearings-abrasives.md) — bearing selection for high-speed spindles
- [Energy](../energy/index.md) — power sources for driving spinning frames

---
*Part of the [Bootciv Tech Tree](../../index.md) • [Textiles](./index.md) • [All Domains](../../index.md)*
