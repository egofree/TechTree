# Rolling Mill

> **Node ID**: machine-tools.rolling-mill
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`machine-tools.casting`](../metals/casting.md), [`machine-tools.machining`](machining.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`machine-tools.forming`](forming.md), [`energy.electricity`](../energy/electricity.md)
> **Timeline**: Years 10-20
> **Outputs**: bar_stock, sheet_metal, plate, rod
> **Critical**: Yes — rolling is the only practical method for producing uniform bar stock, sheet, and plate in quantity; these feed every downstream process

## Overview

A rolling mill reduces the cross-section of heated (or cold) metal by passing it between counter-rotating cylindrical rolls. Each pass reduces thickness by 10-30% and elongates the workpiece proportionally. The rolls grip the metal by friction and draw it through the narrowing gap. Force on each roll is determined by the material's flow stress at temperature, the contact area (roll bite), and the reduction ratio. For hot steel at 1000°C, yield stress is approximately 50-80 MPa — low enough for hand-powered mills to process bar up to 10 mm thick. Cold rolling requires higher force but produces work-hardened, dimensionally precise sheet.

Rolling is the only practical method for producing uniform bar stock, sheet, and plate in quantity. These materials feed every downstream process: [machining](machining.md), [forming](forming.md), [construction](../construction/index.md), and [electrical wiring](../energy/electricity.md). Without rolling, all stock must be forged by hammer — a process limited to ±1-3 mm dimensional accuracy and low throughput. The rolling mill transforms metallurgical output (ingots, blooms) into the standardized shapes that industrial production requires.

The [forming article](forming.md) covers rolling operations and procedures; this article covers the construction and setup of the rolling mill itself.

The rolling process is governed by friction between the rolls and the workpiece. The rolls grip the metal when the contact angle (the angle subtended by the roll bite at the center) is less than the friction angle. For steel rolls on hot steel, the maximum bite angle is 20-25°; for cold rolling, it is 5-8°. The roll separating force is given by: F = σ_f × w × L, where σ_f is the material flow stress, w is the strip width, and L = √(R × Δh) is the projected contact length (R = roll radius, Δh = thickness reduction). For hot steel at 1000°C with σ_f ≈ 60 MPa, a 200 mm roll reducing 10 mm stock by 2 mm over 300 mm width generates F = 60 × 300 × √(100 × 2) = 254 kN (~26 tonnes). This force must be resisted by the frame and the screw-down mechanism without excessive deflection.

Roll gap setting accuracy determines the dimensional tolerance of the rolled product. A hand-operated screw-down with 1.5 mm pitch and a calibrated dial marked in 0.1 mm divisions gives adequate control for hot rolling (±0.2-0.5 mm tolerance). Cold rolling requires finer adjustment — a 0.5 mm pitch screw-down with a vernier dial reading to 0.02 mm is necessary to achieve ±0.02-0.1 mm tolerance on cold-rolled sheet.

## Prerequisites

- [Casting capability](../metals/casting.md) — for cast iron rolls and frame, or access to forged steel stock
- [Machining capability](machining.md) — for turning rolls concentric, boring bearing housings, cutting gear teeth
- [Iron and steel stock](../metals/iron-steel.md) — medium-carbon steel for rolls, structural steel for frame
- [Bronze casting](../metals/casting.md) — for bushings (or steel bearings with grease lubrication)
- [Power source](../energy/index.md) — water wheel (3-5 HP) or electric motor for powered operation; hand crank for bootstrap

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Cast iron or forged steel (rolls) | 30-60 kg | 100-200 mm diameter × 200-400 mm face, hardened to 50-55 HRC surface | [Iron & Steel](../metals/iron-steel.md) | Chilled cast iron rolls (harder surface, more brittle) |
| Cast iron or steel plate (frame) | 50-150 kg | 20 mm minimum thickness for hand mill | [Casting](../metals/casting.md) | Welded steel frame (requires machining) |
| Fine-pitch threaded rod (screw-down) | 2 | M20, 1.5 mm pitch, 200-300 mm long | [Machining](machining.md) | Standard threaded rod (coarser adjustment) |
| Spur gears | 2 | 20-tooth, 2.5 module, matching roll spacing | [Machining](machining.md) | Chain drive (less precise synchronization) |
| Bronze bushings (bearings) | 4 | Matched to roll journal diameter, 0.02-0.05 mm clearance | [Casting](../metals/casting.md) | Lubricated cast iron bores (higher friction) |
| Hand crank | 1 | 300 mm radius handle with grip | [Forming](forming.md) | Chain wheel for powered drive |
| Steel key stock | 4 | 6 × 6 mm, for gear and crank mounting | [Iron & Steel](../metals/iron-steel.md) | Set screws (less secure) |

## Process Description

### Rolls

1. **Cast or forge the rolls**: For a hand mill, cast two rolls from chilled cast iron (or forge from medium-carbon steel), 100 mm diameter × 200 mm face length. Cast the journals integral with the roll body: 30 mm diameter × 80 mm long on each end.
2. **Turn the rolls**: Mount each roll between centers on the lathe. Turn the roll face concentric to the journals within ±0.02 mm runout. Turn the journals to 30 mm diameter, fitting the bearing bushings.
3. **Harden the roll faces** (if steel): Heat to 820-850°C, quench in oil, temper at 350-400°C to 50-55 HRC. Grind faces on a cylindrical grinder to 0.8 μm Ra finish. Chilled cast iron rolls are already hard and only need grinding.

**Calibration**: Mount a dial indicator against each roll face. Rotate by hand. Total indicated runout must be <0.02 mm.

**Expected performance**: Roll face flatness: ±0.02 mm. Concentricity: ±0.02 mm runout. Surface hardness: 50-55 HRC.

### Frame

4. **Fabricate the frame**: Cast a one-piece frame from gray cast iron, or weld from 20 mm steel plate. The frame has two vertical housings with bore pairs for the roll bearings. Housing bore centers must be parallel within 0.03 mm over the 200 mm face width.
5. **Bore bearing housings**: Bore the upper and lower bearing housing bores to 35.00 mm ±0.02 mm (to accept bronze bushings). The lower bores are fixed; the upper bores are in sliding blocks that move vertically in guideways.
6. **Machine the guide ways**: Mill the vertical guide ways for the upper bearing blocks to 0.05 mm clearance on each side. The blocks must slide freely without tilting — tilt causes uneven roll gap.

### Screw-Down Mechanism

7. **Make the screw-down assemblies**: Thread M20 × 1.5 mm holes in the top of the frame (or in separate bridge plates). Insert fine-pitch threaded rods through bronze thrust washers into the upper bearing blocks. Each full turn adjusts the roll gap by 1.5 mm.
8. **Add calibrated dials**: Attach graduated dials to the screw-down rods. Mark 0.1 mm increments (each 1/15 turn = 0.1 mm). Both screw-downs must be adjustable independently to set a parallel gap.

### Drive and Assembly

9. **Cut gear teeth**: Cut 20-tooth spur gears (2.5 module) on the roll journal extensions to synchronize the two rolls. Key the gears to the journals with 6 × 6 mm key stock.
10. **Mount the crank**: Fix a hand crank (300 mm radius) on one roll journal. For added torque, install a 3:1 chain or gear reduction.
11. **Assemble rolls in frame**: Press bronze bushings into bearing housings. Insert lower roll, then upper roll. Engage synchronizing gears. Install screw-down mechanism on upper bearing blocks.
12. **Set the roll gap**: Set gap to zero (rolls just touching). Verify both ends are equal with a feeler gauge. Back off each screw-down by equal amounts to set the desired gap.

**Calibration**: Set gap using calibrated dials. Pass a 1 mm feeler gauge through the gap at three positions (center and both ends) — uniform within ±0.05 mm. Roll a 5 mm thick copper bar through a 3 mm gap setting. Measure rolled thickness at three points along length and at both edges — variation <0.1 mm.

**Expected performance**: Roll gap adjustment resolution: 0.1 mm per dial division. Roll pressure: 50-150 kN for hot steel at 15-20% reduction. Throughput: 2-5 kg/hour for hand operation.

## Quantitative Parameters

### Hand-Operated Mill

| Parameter | Value |
|-----------|-------|
| Roll diameter | 100-150 mm |
| Face width | 200-300 mm |
| Roll pressure (hot steel, 15-20% reduction) | 50-150 kN |
| Capacity — hot rolling | Copper, bronze, soft iron bar up to ~10 mm thick |
| Capacity — cold rolling | Copper and brass sheet to ~1 mm |
| Minimum strip thickness (copper) | 0.5 mm with careful gap setting |
| Throughput (hand operation) | 2-5 kg/hour |
| Roll gap adjustment resolution | 0.1 mm per dial division |
| Reduction per pass (hot) | 15-30% |
| Reduction per pass (cold) | 5-15% |

### Powered Mill (Water Wheel or Engine)

| Parameter | Value |
|-----------|-------|
| Roll diameter | 200-400 mm |
| Face width | 400-800 mm |
| Drive power | 3-10 HP minimum (2-7.5 kW) |
| Roll force | 100-5000 kN (10-500 tonnes) |
| Roll speed | 0.1-5 m/s |
| Strip width capacity | 200-2000 mm |
| Capacity (hot steel) | 50 mm square bloom to 10 mm round in 6-10 passes |
| Capacity (cold steel sheet) | 2 mm → 0.3 mm in 8-12 passes |

### Hot Rolling vs. Cold Rolling

| Parameter | Hot Rolling | Cold Rolling |
|-----------|-------------|--------------|
| Temperature | 900-1200°C (steel), 600-900°C (copper) | Room temperature |
| Reduction per pass | 15-30% | 5-15% |
| Force required | Lower (material softer at temperature) | Higher (material at full yield strength) |
| Surface finish | Rough (scale, oxide) | Smooth (0.5-2 μm Ra) |
| Dimensional tolerance | ±0.2-0.5 mm | ±0.02-0.1 mm |
| Work hardening | None (recrystallizes) | Yes — 50-100% yield strength increase |
| Annealing required | No | Between passes if reduction >40% cumulative |

### Roll Pass Schedule (50 mm Square Bloom → 10 mm Round Bar)

| Pass | Starting Section | Gap Setting | Ending Section | Reduction |
|------|-----------------|-------------|----------------|-----------|
| 1 | 50 mm square | 38 mm | 38 mm oval | 25% |
| 2 | 38 mm oval | 30 mm | 30 mm oval | 21% |
| 3 | 30 mm oval | 24 mm | 24 mm oval | 20% |
| 4 | 24 mm oval | 19 mm | 19 mm oval | 21% |
| 5 | 19 mm oval | 15 mm | 15 mm oval | 21% |
| 6 | 15 mm oval | 12 mm | 12 mm round | 20% |
| 7 | 12 mm round | 10 mm | 10 mm round | 17% (finish) |

## Scaling Notes

- A hand mill with 100 mm rolls processes copper, brass, and soft iron bar — sufficient for bootstrap: bus bar, ground strap, and small structural sections.
- Scale to a powered mill (200-300 mm rolls, 5-10 HP) when consistent production of steel bar stock is needed. A water wheel at 2-5 HP can drive a small production mill.
- Sheet production below 0.5 mm requires four-high rolls (small work rolls backed by large support rolls) to prevent work roll deflection. Build two-high mills first; add backup rolls when thin sheet is demanded.
- Industrial-scale strip mills (1000+ mm wide, 0.1-30 m/s roll speed, 5000 tonne roll force) require precision bearings, large cast steel frames, and 500+ kW drive motors. These are post-bootstrap machines.
- Roll material selection: Chilled cast iron rolls develop a hard white-iron surface layer (55-60 HRC) during casting — ideal for cold rolling. Forged steel rolls (50-55 HRC after heat treatment) are tougher and resist spalling. For hot rolling, softer rolls (40-45 HRC) resist thermal cracking better.
- Bearing lubrication: Bronze bushings require lubrication every 30-60 minutes of operation. Apply grease through zerk fittings or drip oilers. Running dry causes rapid bushing wear and increases roll gap variation. Antifriction bearings (tapered roller) reduce friction and maintenance but require higher machining precision to install.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Wavy edges on strip | Roll face crowning incorrect; gap wider at center than edges | Grind slight crown (0.02-0.05 mm convex) on roll faces; check screw-down uniformity with feeler gauges |
| Strip camber (curves sideways) | Uneven reduction across width; one side of gap wider | Adjust screw-downs independently; check bearing wear; center stock on roll face |
| Splitting or cracking | Too much reduction per pass; material too cold | Reduce to 10-15% per pass; reheat stock to 900°C+ for steel |
| Out-of-tolerance thickness | Roll gap drifted; bearing wear; thermal expansion | Re-set gap before each batch; measure every 5th pass; replace worn bushings (clearance >0.1 mm) |
| Roll marks on strip | Roll face damaged; foreign object on roll | Grind roll faces smooth; clean rolls between passes; remove scale from stock |
| Stock slips (rolls don't grip) | Gap too small; roll face too smooth; stock too cold | Open gap slightly; roughen roll face (80-120 grit); reheat stock |
| Excessive force required | Stock too thick for gap; material too cold; reduction too aggressive | Use multiple passes with smaller reductions; reheat; verify material grade |
| Roll deflection (thicker center, thinner edges) | Roll diameter too small for face width; excessive force | Reduce reduction per pass; increase roll diameter; apply roll crown compensation (grind 0.02-0.05 mm convex on face) |
| Inconsistent thickness along strip | Bearing wear creating roll movement; thermal expansion | Replace worn bushings; allow rolls to reach thermal equilibrium before critical passes; measure every 5th strip |

## Safety

- **Pinch points — the primary hazard**: The roll bite draws in anything that contacts it. A finger caught between 100 mm rolls at hand-crank speed is crushed instantly. Never reach toward the rolls while the crank is turning. Feed stock using tongs or pliers with 300+ mm handles. Install a safety bar across the front of the mill at roll center height.
- **Hot metal handling**: Hot-rolled steel at 900-1100°C causes severe burns on contact. Use tongs with 400+ mm handles. Wear leather welding gloves. Clear area of combustible material — hot scale ignites wood and cloth within seconds.
- **Roll gap adjustment lockout**: Before adjusting the screw-down mechanism, disengage gears or remove the crank. An unexpected crank rotation while hands are near the rolls causes crush injuries. Secure crank with a pin or bolt when not actively rolling.
- **Emergency stop procedure**: If material jams, stop cranking immediately. Do not force the stock through — rolls can shatter under overload. Back off the screw-down to release the jam. For powered mills, install an emergency stop button within arm's reach.
- **Flying scale**: Hot rolling produces loose scale (iron oxide flakes). Wear safety glasses (ANSI Z87.1 rated). Scale in the eye causes corneal abrasion.
- **Heavy roll handling**: Rolls weigh 15-60 kg each. Use a hoist or two-person lift for installation. Never lift a roll alone above waist height.

## Quality Control

1. **Thickness measurement**: Measure rolled strip with a micrometer at three positions along the length and at both edges. Tolerance for hot-rolled bar: ±0.2 mm. Tolerance for cold-rolled sheet: ±0.05 mm.
2. **Flatness check**: Lay rolled sheet on a surface plate. Measure gap under a straightedge at 100 mm intervals. Maximum gap: 0.5 mm per 300 mm (hot-rolled); 0.1 mm per 300 mm (cold-rolled).
3. **Surface inspection**: Inspect roll surface for nicks, embedded scale, or grinding marks. Any defect transfers to every part rolled afterward. Run a test piece first when changing setup.
4. **Hardness verification (cold-rolled)**: Cold rolling work-hardens the metal. Measure hardness after final pass. Cold-rolled copper: 100-150 HV (up from 50-70 HV annealed). Cold-rolled mild steel: 150-200 HV (up from 120-140 HV).
5. **Roll surface inspection**: Before each production run, inspect roll surfaces for nicks, embedded scale, or grinding marks. Any defect on the roll transfers to every piece rolled. Remove minor defects by hand-stoning with a fine India stone. Major defects require regrinding on a cylindrical grinder.
6. **Gear alignment check**: Verify that synchronizing gears are properly meshed — a mismatch causes one roll to lead or lag, producing skewed strips and uneven wear on the gears. Check gear backlash: 0.05-0.15 mm is the target range. Excessive backlash produces jerky rotation that marks the strip.

## Variations and Alternatives

- **Two-high**: The simplest design — two rolls, one above the other. Stock passes through in one direction, then the gap is opened to return it. Or the mill reverses direction for each pass.
- **Three-high**: Three rolls stacked vertically. Stock passes through the upper pair in one direction, then through the lower pair on the return. No gap adjustment needed between passes. Higher throughput than two-high.
- **Four-high**: Two small work rolls supported by two large backup rolls. Backup rolls prevent work roll deflection under load, enabling precise gauge on wide sheet. Required for sheet <0.5 mm thickness.
- **Tandem**: Multiple stands in series, each reducing thickness progressively. Used for high-volume sheet production at 50-200 m/min line speed.
- **Cluster mill (Sendzimer)**: Multiple small work rolls supported by a cluster of larger backup rolls. Used for precision thin foil (<0.1 mm). Extremely rigid but complex to build.
- **Forge hammer** ([forge-hammer.md](forge-hammer.md)): Alternative for shaping bar and billet by impact rather than rolling. Lower dimensional precision (±1-3 mm) but no roll gap setup required.
- Roll pass design: Reducing a 50 mm square bloom to 10 mm round requires 6-10 passes through progressively smaller roll gaps. Each pass reduces the cross-section by 15-25%. Plan the pass sequence in advance: rough passes (20-30% reduction) followed by finishing passes (10-15% reduction). The final pass sets the dimensional tolerance.
- Roll cooling: Hot rolling heats the rolls through contact. Uncontrolled roll heating causes thermal expansion that changes the roll gap during a production run. Water spray cooling (5-15 L/min per roll face) maintains roll temperature within ±10°C. Monitor roll surface temperature with a pyrometer — target <150°C for steel rolls.
- Roll material service life: Chilled cast iron rolls develop surface spalling after 2000-5000 hours of hot rolling. Forged steel rolls last 5000-10,000 hours. Resurface by cylindrical grinding when surface defects become visible on the rolled product. Each regrind removes 0.5-2 mm from the roll diameter — adjust the screw-down zero point after grinding.
- Material yield in rolling: Hot rolling produces 5-10% oxide scale loss (iron oxidized during heating). Cold rolling has no scale loss but 2-5% edge trim waste. Plan material inputs accordingly — to produce 100 kg of hot-rolled bar, start with 110-115 kg of heated bloom.
- Roll surface maintenance: Between production runs, clean the roll faces with a cloth and light oil to prevent rust. Store the mill with the rolls separated (gap open) to prevent contact corrosion. Inspect the roll faces for embedded scale — a small piece of iron oxide pressed into the roll surface produces a repeating defect on every subsequent piece. Remove embedded scale with a fine India stone.
- Power transmission for hand mills: A 400-500 mm crank handle provides sufficient leverage for a single operator on a 100 mm roll mill. For heavier stock (6-10 mm), mount a chain wheel on the roll shaft and use a chain drive from a larger sprocket (3:1 reduction). This reduces the cranking effort at the cost of slower throughput.
- Edge guiding: Flat strip tends to wander sideways during rolling, producing camber (curved strip). Install edge guides (steel bars bolted to the frame, spaced 1-2 mm wider than the strip) to keep the stock centered on the roll face. For bar rolling, the roll grooves themselves guide the stock.

## References

- [Forming](forming.md) — rolling operations and procedures using the mill
- [Casting](../metals/casting.md) — casting the rolls and frame
- [Machining](machining.md) — machining rolls, gears, and bearing housings
- [Iterative Bootstrap](iterative-bootstrap.md) — machine tool construction sequence
- [Iron & Steel](../metals/iron-steel.md) — steel stock for mill construction
- [Bearings & Abrasives](bearings-abrasives.md) — bearing design and lubrication
- Roll pressure approximation: P = σ_f × L × w, where σ_f is flow stress, L = √(R × Δh) (roll bite contact length), w is strip width. Hot steel at 1000°C: σ_f ≈ 50-80 MPa. Cold mild steel: σ_f ≈ 250-400 MPa.
- Forward slip: exit velocity 2-5% faster than roll surface speed due to compression recovery.
- Roll separating force calculation: F = σ_f × w × √(R × Δh), where σ_f = flow stress, w = strip width, R = roll radius, Δh = thickness reduction. Hot steel at 1000°C: σ_f ≈ 50-80 MPa. Cold mild steel: σ_f ≈ 250-400 MPa.
- Stock preparation for hot rolling: Heat blooms uniformly to 900-1200°C in a forge or furnace. Soak for 15-30 minutes per 25 mm of cross-section to ensure uniform temperature. Scale forms rapidly above 800°C — descale by tapping the hot bloom with a hammer before the first pass to prevent scale from embedding in the roll surface.
- Measurement protocol: Measure rolled strip thickness before the first pass and after every 3rd pass with a micrometer at three points along the length and at both edges. Record all measurements. This data identifies roll gap drift, roll crown issues, and bearing wear trends before they produce out-of-tolerance product.
- Strip coiling and handling: After the final pass, coil the rolled strip on a mandrel or drum for storage and transport. Coil diameter should be at least 50× the strip thickness to prevent permanent set (curvature). For flat bar and plate, stack flat on a level surface — do not lean against a wall (causes bow). Label each piece with material, thickness, and date rolled.
- Lubrication for cold rolling: Apply a light film of mineral oil or soluble oil emulsion to the strip surface before cold rolling. Lubrication reduces roll force by 15-25%, improves surface finish, and extends roll life. For copper and brass, a 5% soluble oil emulsion works. For steel, a heavier rolling oil or lime coating is needed. Do not cold roll dry — the high contact pressures (500-2000 MPa at the roll bite) cause the strip to gall and weld to the roll surface.
- Safety guard installation: Install a steel bar across the front of the mill at roll center height. This prevents the operator's hands from contacting the roll bite during stock feeding. The guard should be 25-30 mm wide, positioned 20-30 mm from the roll face. For powered mills, install an emergency stop bar (pressure-sensitive bar across the full width of the mill) that immediately disengages the drive when pressed.
- Straightening rolled strip: If cold-rolled strip develops camber (curve to one side), straighten by passing it through the mill with slightly more pressure on the concave side. Alternatively, clamp one end in a vise and apply controlled bending force with a lever. For production straightening, a three-roll straightener (two support rolls and one adjustable center roll) removes camber and curvature in a single pass.
- Roll gap measurement: Use a feeler gauge set (0.02-1.0 mm) to verify the roll gap at three positions (center and both ends) before each production run. The gap must be uniform within ±0.05 mm across the face width. A non-uniform gap produces strip with thickness variation across its width. Set the gap to zero (rolls just touching) and back off each screw-down by equal amounts. Verify with the feeler gauge after each adjustment.
- Roll speed for hand operation: A crank speed of 30-60 RPM produces a roll surface speed of 150-300 mm/s for 100 mm rolls. This is a comfortable cranking speed for sustained operation. Faster cranking (60-100 RPM) increases throughput but causes operator fatigue within 10-15 minutes. For production rolling of long lengths, two operators can alternate in 15-minute shifts.

---
*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*
