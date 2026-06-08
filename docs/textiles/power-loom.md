# Power Loom

> **Node ID**: textiles.power-loom
> **Domain**: [Textiles](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`textiles.weaving`](weaving.md), [`energy.steam-power`](../energy/steam-power.md)
> **Enables**: mass-scale cloth production (10-20× handloom rate)
> **Timeline**: Years 20-30
> **Outputs**: woven cloth at industrial scale
> **Critical**: Yes — power looms transform cloth from a craft product to an industrial commodity, enabling mass textile production for clothing, sails, tents, and industrial fabrics

## Principle

![Masson Mills WTM 12b Power Loom 5877](../images/textiles/textiles_power-loom.jpg)

> *Masson Mills built in 1783 is home to a working textile mills. There is a small weaving shed with working looms some dating back to before 1867. Power Loom referred to here as a Yorkshire Loom. It has a longer reedspace than the Lancashire Loom so can weave wider fabric.*

> *Image: Clem Rutter, Rochester, Kent., CC BY-SA 3.0*

A power loom mechanizes the three basic motions of hand weaving — shedding (raising alternate warp threads), picking (passing the weft through the shed), and beating (packing the weft against the fell) — using power from a steam engine, water wheel, or electric motor transmitted via belt drive to a main crank shaft. Each revolution of the crank shaft completes one weaving cycle: shed opens → shuttle flies across → reed beats weft → shed changes.

The Cartwright power loom (1785) was the first practical design: an iron frame supporting the warp beam, cloth beam, heddle shafts, shuttle race, and reed (beater). The main shaft drives a cam system that raises and lowers heddle shafts (shedding), a picking stick that propels the shuttle across the warp (picking), and a lay (batten) that swings the reed forward to pack the weft (beating). Later improvements added automatic shuttle changing (Roberts self-acting loom, 1820s-1840s), automatic bobbin replacement (Northrop, 1894), and eventually shuttleless designs (rapier, projectile, air-jet, 1950s+).

This article covers the construction of a basic power loom suitable for bootstrap production: an iron-frame loom with cam shedding, fly-shuttle picking, and reed beating, driven by belt from a line shaft or individual motor.

## Prerequisites

- [Iron & Steel](../metals/iron-steel.md) — cast iron for the frame, forged steel for the crank shaft and picking mechanism
- [Machine Tools](../machine-tools/index.md) — lathe for turning shafts, planer for frame surfaces, drilling for bearing housings
- [Bearings](../machine-tools/bearings-abrasives.md) — reliable bearings for the main crank shaft and lay shaft
- [Power source](../energy/index.md) — steam engine, water wheel, or electric motor (2-5 kW per loom)
- [Weaving](weaving.md) — treadle loom construction provides the basis for understanding loom geometry; power loom adds mechanization to the same principles
- [Spinning Frame](spinning-frame.md) — industrial yarn supply to keep the power loom fed

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Cast iron (frame) | 300-600 kg | Side frames (2), breast beam, back beam, base plates | [Iron & Steel](../metals/iron-steel.md) | Welded steel plate (lighter, requires welding) |
| Steel shafts | 30-60 kg | Main crank shaft 50-60 mm dia., cam shaft 35-45 mm dia., turned and ground | [Iron & Steel](../metals/iron-steel.md) | None — precision shafts required |
| Steel (picking stick) | 5-10 kg | Forged or spring steel, 600-800 mm long, tapered | [Iron & Steel](../metals/iron-steel.md) | Ash wood picking stick (shorter life) |
| Steel reed (beater) | 1 pcs | Metal dents (0.3-0.5 mm) in wooden baulks, 100-120 cm wide, 10-15 dpi | [Iron & Steel](../metals/iron-steel.md) | Cane/bamboo reed (less durable) |
| Wire heddles | 800-2,000 pcs | Steel wire, 0.5-0.8 mm, with centered eye | [Iron & Steel](../metals/iron-steel.md) | String heddles (stretch, shorter life) |
| Cast iron pulleys | 3-5 pcs | 150-300 mm diameter, keyed to shafts | [Iron & Steel](../metals/iron-steel.md) | Wooden pulleys (less durable) |
| Leather belts | 3-5 m | 50-75 mm wide, for drive and take-up | [Leather](../animals/leather.md) | Canvas belt (less grip) |
| Bearings | 8-16 pcs | Bronze bushings for shaft journals | [Bearings](../machine-tools/bearings-abrasives.md) | Wooden bearings with oil cups |
| Hardwood (shuttle) | 1-2 pcs | Boxwood, ash, or hornbeam, boat-shaped, 300-350 mm long | [Foundations](../foundations/tools-basic.md) | None — shuttle must be smooth and balanced |
| Springs (heddle return) | 4-8 pcs | Steel coil or leaf springs | [Iron & Steel](../metals/iron-steel.md) | Counterweights (bulkier) |

## Construction Steps

### Frame

1. **Cast the side frames**: Cast two matching side frames in iron (each approximately 1400 × 200 × 150 mm). Each side frame has integral bearing housings for the main crank shaft and cam shaft, machined after casting. The side frames must be identical — cast from the same pattern. Machine the mating surfaces (where cross-members bolt on) flat within 0.1 mm.

2. **Assemble the frame**: Bolt the two side frames together with cast iron cross-members: breast beam (front, where cloth passes over), back beam (rear, where warp feeds from), and two base rails. The frame must form a rigid rectangular box. Check diagonal measurements — both diagonals must be equal within 2 mm (frame is square).

3. **Bore the shaft bearings**: Line-bore the main crank shaft bearings (2 journals per side frame, 50-60 mm bore) and the cam shaft bearings (2 journals, 35-45 mm bore). The main crank shaft and cam shaft must be parallel within 0.1 mm per meter of length. Press bronze bushings into the bearing housings.

### Crank Shaft and Cams

4. **Turn the main crank shaft**: Turn a 50-60 mm diameter steel shaft to ±0.05 mm cylindricity. The shaft runs the full width of the loom (1200-1500 mm) and carries: a drive pulley at one end, a crank throw (eccentric) for the lay mechanism, and timing gears for the cam shaft.

5. **Cut the cams**: Machine shedding cams (one pair per shaft — minimum 2 pairs for plain weave, 4+ for twill) from cast iron blanks. Each cam has a profile that raises and lowers a heddle shaft in the correct sequence. The cam profile determines the shed timing — the shed must be fully open when the shuttle passes and closed when the reed beats. Mount cams on the cam shaft with keyed connections.

6. **Install timing gears**: Mount a gear on the main crank shaft that drives the cam shaft at 1:1 ratio (one pick per revolution). The timing between crank position (picking and beating) and cam position (shedding) is critical — the shed must open before the shuttle launches and close after the reed beats.

### Shedding Mechanism

7. **Mount heddle shafts**: Suspend heddle frames (lightweight wooden or iron frames holding wire heddles) from levers (treadle levers) pivoting on the loom top. Each lever connects to a cam follower (roller) that rides on a cam. When the cam lifts the follower, the heddle shaft rises; a return spring or counterweight pulls it down. For plain weave: 2 heddle shafts. For twill: 4 shafts.

8. **Adjust shed geometry**: The shed (gap between raised and lowered warp threads) must be clean and deep enough for the shuttle to pass (minimum 40-50 mm at the shuttle race). Adjust by varying the cam lift (heddle shaft travel) and the lever pivot position. The shed should open quickly, hold open during shuttle passage, and close quickly after beating.

### Picking Mechanism

9. **Install picking sticks**: Mount a picking stick on each side of the loom (left and right). Each stick is a lever pivoting on a vertical pin, with one end driven by a cam or cone on the main crank shaft and the other end connected to a picker (leather or wooden buffer that strikes the shuttle). The cam imparts a sharp angular impulse to the picking stick, accelerating the shuttle across the shed.

10. **Install shuttle boxes**: Mount shuttle boxes (metal or hardwood housings) at each end of the shuttle race. Each shuttle box catches the arriving shuttle, centers it, and holds it until the next pick. Install leather buffers in each box to absorb shuttle impact. The shuttle box must be aligned with the shuttle race — any vertical or lateral misalignment causes the shuttle to derail.

11. **Install the shuttle race**: Mount a smooth metal or hardwood race (track) spanning the loom width between the shuttle boxes. The shuttle slides on this track as it crosses. The race must be flat within 0.5 mm over its full length and level within 1 mm.

### Beating (Lay) Mechanism

12. **Construct the lay (batten)**: The lay is a heavy frame that swings from pivot points on the loom sides, carrying the reed (beater). Construct from iron or hardwood, 100-120 cm wide. Mount the reed in the lay with removable clips (the reed may need to be changed for different cloth densities).

13. **Connect the lay to the crank**: Connect the lay to the crank throw on the main shaft via connecting rods (pitman arms). The crank rotation converts to the lay's forward-backward swing. The lay swings forward at the moment the shed is closing, packing the weft against the fell. Adjust the timing so the reed contacts the fell 20-30° after top dead center of the crank.

### Warp and Cloth Beam

14. **Install warp and cloth beams**: Mount the warp beam (rear) and cloth beam (front) in bearing housings on the side frames. Each beam is a steel or hardwood roller, 80-100 mm diameter × 120-150 cm long, with iron ratchet and pawl for tension adjustment. Install a friction brake on the warp beam (let-off) that maintains constant warp tension as the beam unwinds. Install a take-up mechanism on the cloth beam that advances the cloth by one pick spacing after each beat.

### Drive System

15. **Install drive pulley and belt**: Mount a flat pulley (200-300 mm diameter) on the main crank shaft. Run a leather belt from the line shaft or motor to this pulley. Install a clutch or tight-and-loose pulley arrangement so the loom can be started and stopped without stopping the power source.

16. **Install stop motions**: Mount a feeler bar (thin metal rod) that detects a broken warp thread — when a thread breaks, it sags and contacts the feeler, which trips a mechanism that disengages the clutch and stops the loom. Also install a shuttle-flight detector — if the shuttle fails to reach the opposite box, the loom stops before the next pick (prevents the reed from beating without weft, which produces a defect called a "broken pick").

## Calibration and Verification

1. **Timing check**: Rotate the main shaft slowly by hand through one complete revolution. Verify the sequence: shed opens → shuttle launches → shuttle arrives at opposite box → lay beats → shed changes → next shuttle launches. The shed must be fully open before the shuttle launches and remain open until the shuttle arrives.

2. **Shuttle flight test**: Launch the shuttle by hand (without power) and verify it reaches the opposite shuttle box cleanly, without bouncing, jamming, or climbing out of the race. Adjust picker force, shuttle box alignment, and shuttle weight (add lead weight inside if needed).

3. **Beat-up force**: Weave a test strip. Check that the reed packs weft tightly enough — the cloth should have uniform pick spacing when examined with a pick glass. If picks are too loose, increase the lay weight or advance the timing.

4. **Warp tension test**: Thread a short warp and run the loom at slow speed. All warp threads should produce the same pitch when plucked. Uneven tension causes broken ends, selvedge draw-in, and uneven cloth.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Weaving width | 100-120 cm |
| Picks per minute | 60-80 (Cartwright type), 120-150 (improved) |
| Cloth production | 5-15 m²/hour |
| Weave structures | Plain, twill (with additional shafts) |
| Power consumption | 2-5 kW per loom |
| Shuttle speed | 8-12 m/s across shed |
| Warp tension | 100-300 N per 100 ends |
| Noise level | 85-95 dB |
| Service life | 30-50 years with bearing and reed replacement |
| Weavers per loom | 1 (tending 2-4 looms on improved models) |

**Throughput by cloth type**:

The picks-per-minute rate alone does not determine cloth production. The weft density (picks per inch) and weaving width also affect how many square meters of cloth are produced per hour.

| Cloth Type | Weft Density (ppi) | Effective Picks/min | Width (cm) | Production (m²/hr) | Loom Type |
|------------|--------------------|--------------------|------------|---------------------|-----------|
| Heavy canvas (10 ppi) | 10 | 60-80 | 120 | 20-30 | Plain shuttle |
| Medium cotton (20 ppi) | 20 | 100-130 | 120 | 12-18 | Improved shuttle |
| Fine shirting (40 ppi) | 40 | 120-150 | 100 | 5-8 | Improved shuttle |
| Denim (25 ppi) | 25 | 100-130 | 150 | 12-18 | Heavy shuttle |
| Toweling (18 ppi) | 18 | 80-110 | 120 | 15-22 | Standard shuttle |
| Wool suiting (30 ppi) | 30 | 80-100 | 150 | 8-12 | Heavy shuttle |

Production calculation: m²/hr = (picks/min × 60) / (picks/inch × 39.37) × (weaving width in m). Example: 120 picks/min at 20 ppi on a 1.2 m loom = (120 × 60) / (20 × 39.37) × 1.2 = 11 m²/hr.

**Power consumption breakdown**:

| Component | Power Share | Notes |
|-----------|-------------|-------|
| Shuttle picking (acceleration + deceleration) | 30-40% | Most energy-intensive single motion; shuttle accelerates from 0 to 8-12 m/s in ~10 ms |
| Beating (lay swing) | 20-25% | Heavy lay + reed; must overcome friction and inertia |
| Shedding (heddle shaft lifting) | 15-20% | Lifts half the warp threads against tension each pick |
| Friction (bearings, belts, gears) | 10-15% | Increases with worn bearings and misalignment |
| Take-up and let-off | 5-10% | Low power but must be precisely timed |
| Total per loom | 2-5 kW | Varies with width, speed, and cloth weight |

**Warp preparation for power looms**:

Power looms consume yarn faster than hand looms and require larger, more uniformly prepared warps. A single power loom weaving 12 m²/hr of 20 ppi cloth with Ne 30 yarn consumes approximately 0.3-0.5 kg of warp yarn and 0.2-0.4 kg of weft yarn per hour. A 10-loom weaving shed thus needs 5-9 kg of yarn per hour, or 40-70 kg per 8-hour shift.

Warp preparation sequence for power looms:
1. **Warping**: Wind the required number of warp ends (typically 2,000-5,000 for a 100 cm width) from yarn packages onto a warp beam. Sectional warping (winding narrow sections side by side) or direct warping (winding all ends simultaneously). Tension must be uniform across all ends: a tension variation greater than 10% causes uneven cloth and frequent breaks.
2. **Warp sizing**: Apply a starch or PVA coating to the warp yarn to strengthen it for the mechanical stress of power loom weaving. Size pick-up: 6-12% by weight for cotton warp. The sizing machine passes the warp sheet through a size bath, squeezes out excess with rollers, and dries it on heated cylinders. Without sizing, cotton warp breakage on a power loom increases 5-10× because the mechanized shedding and beating place far more stress on each thread than hand weaving.
3. **Drawing in**: Thread each warp end through a heddle eye and a reed dent. For a 4,000-end warp at 20 epi, this takes 4-8 hours by hand or 30-60 minutes with a mechanical drawing-in machine. Incorrect drawing-in produces pattern errors that run the entire length of the cloth.

## Strengths

- 10-20× faster than handloom production — a single weaver tending 2-4 power looms outproduces 20-40 hand weavers
- Consistent beat-up force produces uniform cloth density — less variation than hand beating
- Iron frame eliminates the flex that limits wooden handloom width — wider cloth possible
- Cam-driven shedding enables complex weave structures without manual shaft lifting

## Weaknesses

- Iron frame castings and precision shaft machining require industrial foundry and machine tool capability
- Shuttle impact at each pick causes noise (85-95 dB) and vibration — hearing protection mandatory
- Broken warp threads stop the loom — warp breakage rate must be kept low with quality yarn and proper tension
- Shuttle boxes and race require precise alignment — a misaligned shuttle box causes shuttle crashes and cloth defects

## Safety

- **Flying shuttles**: A shuttle at 8-12 m/s is a projectile. Early power looms regularly ejected shuttles — guard bars across the front and back are mandatory. Never stand in the shuttle flight path.
- **Pinch points**: The lay mechanism, picking sticks, and cam followers all have severe pinch hazards. Guard all moving parts. Emergency stop mechanism (clutch disengagement) must be within arm's reach.
- **Noise**: 85-95 dB causes hearing damage with prolonged exposure. Hearing protection required in power weaving sheds.
- **Dust and fly**: Weaving generates cotton dust and fiber fly. Ventilate the weaving room. Byssinosis risk with cotton dust — wear dust masks.
- **Entanglement**: Loose clothing, hair, or jewelry caught in the belt drive or crank shaft causes severe injury. Fitted clothing, hair tied back, guards on all rotating parts.

## Maintenance

Power looms require systematic maintenance to maintain cloth quality and prevent breakdowns. A neglected loom produces defects and can fail catastrophically from fatigue in high-stress components.

**Daily checks** (before each shift):
- Inspect the reed for bent or broken dents. A single bent dent produces a visible vertical line (reed mark) on every pick. Straighten bent dents with fine-nose pliers; replace broken dents immediately.
- Check shuttle boxes for wear on leather buffers. Worn buffers allow the shuttle to bounce back out of the box, causing missed picks and potential shuttle ejection.
- Verify warp tension uniformity by plucking warp threads at 5-10 positions across the width. All threads should produce the same pitch.
- Oil all bearing points: main crank shaft bearings, cam shaft bearings, lay pivot pins, picking stick pivots, and treadle lever pivots. Use machine oil (SAE 30). A loom running 8 hours per day needs 5-10 mL of oil per bearing per week.

**Weekly maintenance**:
- Check timing between shedding, picking, and beating. Rotate the main shaft slowly by hand and verify: shed fully open before shuttle launches, shuttle arrives before lay beats, lay contacts fell after shed begins to close. Timing drifts as cam followers and connecting rods wear.
- Inspect heddle frames for bent or broken wire heddles. A broken heddle drops its warp thread, producing a broken end defect. Replace broken heddles individually — do not wait for accumulation.
- Clean the shuttle race (track) and check for wear grooves. A worn race causes the shuttle to wobble and potentially derail. Sand smooth or replace the race surface.
- Check the belt for cracks, glazing, and proper tension. A slipping belt causes speed variation and inconsistent pick spacing.

**Monthly maintenance**:
- Inspect the crank shaft for fatigue cracks at the crank throw (the highest-stress point). A cracked crank shaft fails catastrophically. Replace if any crack is visible.
- Check the lay (batten) pivot points for wear. Excessive play in the lay pivot causes inconsistent beat-up force, producing uneven pick density.
- Inspect the picking stick for cracks and splinters at the cam contact point. A broken picking stick stops the loom. Replace picking sticks before they fail, not after.
- Clean and inspect the warp let-off brake mechanism. The brake must maintain constant tension as the warp beam unwinds. A slipping brake causes tension variation and broken ends.

**Shuttle maintenance**:
- Check shuttle weight: standard shuttle weighs 300-500 g. Replace worn or damaged shuttles — a cracked shuttle can disintegrate in flight.
- Check shuttle bobbin fit: the bobbin must spin freely in the shuttle cavity. A tight bobbin causes thread breakage; a loose bobbin causes uneven thread delivery.
- Inspect the shuttle eye (thread exit hole) for burrs. Polish with fine abrasive if thread is fraying at the exit point.

## Troubleshooting (Power Loom Specific)

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Shuttle not reaching opposite box | Picking stick worn, picker buffer deteriorated, or shuttle too light | Replace picker buffer. Increase picking force (adjust cam engagement). Add lead weight inside shuttle. |
| Broken ends (frequent) | Warp tension too high, heddle eyes rough, or yarn quality insufficient | Reduce warp tension by 10-15%. Polish heddle eyes with fine emery. Check yarn strength — apply warp sizing (starch coating) if needed. |
| Cloth draw-in at selvedge | Weft tension too high or no temple used | Install temple (cloth stretcher) at fell line. Reduce weft package tension. Check shuttle bobbin winding quality. |
| Inconsistent pick spacing | Let-off tension varying or take-up mechanism slipping | Clean and adjust the warp beam brake ratchet. Check take-up pawl engagement. Oil take-up gear train. |
| Shuttle flying out of race | Race worn, shuttle box misaligned, or picking force excessive | Replace worn race surface. Align shuttle boxes with the race. Reduce picking force. Install guard bars. |
| Loom stopping (false trips) | Stop-motion feeler bar too sensitive or vibration triggering mechanism | Adjust feeler bar gap. Mount feeler bar with anti-vibration brackets. Check for loose connections in the stop-motion linkage. |

## Cloth Defect Classification

| Defect | Description | Severity | Action |
|--------|-------------|----------|--------|
| Broken end | Missing warp thread, thin vertical line | Major | Hand-mend if possible; otherwise downgrade cloth |
| Missed pick | Missing weft thread, thin horizontal line | Major | Stop loom, back up, re-insert weft |
| Float | Yarn floating over surface instead of interweaving | Major | Check heddle and re-thread |
| Slack pick | Loose weft, visible as slightly wider spacing | Minor | Increase take-up tension |
| Tight pick | Packed weft, visible as slightly narrower spacing | Minor | Decrease take-up tension |
| Reed mark | Vertical line at reed dent spacing | Minor | Clean or replace reed |
| Oil spot | Lubricant contamination on cloth | Minor | Reduce oiling quantity; install drip guards |
| Slub | Thick lump in yarn | Cosmetic | Trim flush; improve yarn quality upstream |

## See Also

- [Weaving](weaving.md) — hand loom construction, weave structures, warping procedures
- [Spinning Frame](spinning-frame.md) — industrial yarn production for power loom feed
- [Steam Power](../energy/steam-power.md) — power source for line shaft drives
- [Machine Tools](../machine-tools/index.md) — precision machining for shafts, cams, and frames
- [Bearings](../machine-tools/bearings-abrasives.md) — bearing selection for crank shafts and cam shafts
- [Sewing & Tailoring](sewing-tailoring.md) — garment construction from woven cloth
- [Finishing](finishing.md) — post-weave finishing processes for loomstate cloth
- [Dyeing](dyeing.md) — coloring woven cloth before and after finishing

---
*Part of the [Bootciv Tech Tree](../index.md) • [Textiles](./index.md) • [All Domains](../index.md)*
