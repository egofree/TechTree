# Bearings

> **Node ID**: machine-tools.bearings
> **Domain**: [Machine Tools Bootstrap](./index.md)
> **Dependencies**: [`machine-tools.iterative-bootstrap`](iterative-bootstrap.md)
> **Enables**: [`machine-tools.machining`](machining.md)
> **Timeline**: Years 10-25
> **Outputs**: bearings, ball_bearings, plain_bearings, babbitt_linings
> **Critical**: Yes — precision enablers for all machine tool construction


Bearings are the precision enablers of machine tool construction. Without bearings, shafts seize and machines destroy themselves from friction. This article covers plain (journal) bearings, rolling element (ball and roller) bearings, bearing selection, and bearing lubricants. For abrasive materials and cutting tools, see [Abrasives & Cutting Tools](abrasives.md).

For the machine tool construction sequence, see [Iterative Bootstrap](./iterative-bootstrap.md). For the machining operations that use these tools, see [Machining](./machining.md).


## Plain (Journal) Bearings

The simplest and most robust bearing type. A cylindrical shaft rotates inside a slightly larger cylindrical housing, separated by a thin film of lubricant.

**Construction steps for a babbitt-lined journal bearing**:
1. Machine the bearing shell from cast iron or steel. Shell bore: shaft diameter + 4-6 mm (to allow for babbitt lining thickness). Shell length: 1.0-1.5 × shaft diameter. Finish the bore surface rough (~1-2 mm Ra) to provide mechanical keying for the babbitt.
2. Prepare the mandrel: turn a steel rod to shaft diameter + radial clearance (0.001-0.002 × shaft diameter; for a 50 mm shaft, mandrel = 50.05-50.10 mm). Coat the mandrel with soot or graphite to prevent babbitt adhesion.
3. Assemble the shell around the mandrel. Seal both ends with clay or putty to contain the molten babbitt. Leave a pouring hole at the top (10-15 mm diameter).
4. Melt babbitt metal (Sn-Sb-Cu alloy, 88/8/4 typical composition) in a crucible to 400-450°C (well above the 240°C liquidus, but below 500°C to avoid oxidation). Skim dross from the surface.
5. Preheat the assembled shell and mandrel to 150-200°C to prevent premature solidification. Pour babbitt through the pouring hole in a steady, continuous stream until it fills the cavity and overflows slightly.
6. Allow to cool to room temperature (30-60 minutes). Disassemble. The babbitt shell now has a precise bore matching the mandrel diameter. Machine oil grooves (2-3 mm wide × 1.5 mm deep) in the babbitt surface in an axial or figure-8 pattern.

**Calibration**: Insert the shaft into the bearing. Measure radial clearance with feeler gauges: target 0.001-0.002 × shaft diameter (50 mm shaft → 0.05-0.10 mm). Spin the shaft by hand — it should rotate freely with no binding but minimal perceptible play. Check axial end float: 0.1-0.3 mm.

**Expected performance**: Allowable bearing pressure: 2-8 MPa for babbitt on steel. Coefficient of friction: 0.01-0.03 (hydrodynamic regime). Speed range: 0-1500 RPM depending on load and lubrication. Operating temperature: up to 100°C with adequate lubrication. Service life: 10,000-50,000 hours with proper lubrication.

**Materials specifications**: Babbitt metal (88% Sn / 8% Sb / 4% Cu), cast iron shell (minimum wall thickness 5 mm), steel mandrel (turned to shaft diameter + clearance, ±0.02 mm), lubricating oil (SAE 30 or equivalent mineral oil).

**Lubrication**: Oil ring (a ring rides on the shaft, dips into oil reservoir below, carries oil up to the bearing surface) or gravity-fed oil cup. Grease-packed for slow-speed bearings.

**Strengths**:
- Simple to manufacture — requires only basic casting and machining capability
- Tolerant of misalignment (the soft babbitt conforms to shaft position over time)
- Embeds contaminants — dirt particles press into the soft babbitt rather than scoring the shaft

**Weaknesses**:
- Higher friction than rolling bearings (~0.01-0.03 coefficient of friction vs. ~0.001 for ball bearings)
- Requires continuous lubrication — oil starvation causes rapid failure (minutes to hours)
- Limited speed capability — above 1500 RPM, friction heat overwhelms cooling capacity

## Rolling Element Bearings (Precision)

Ball and roller bearings reduce friction and enable high-speed machinery (machine tool spindles, engines, generators).

**Construction steps for a ball bearing (6205 type)**:
1. **Inner ring**: Forge bearing steel (52100 grade, 1% C, 1.5% Cr) to ring blank. Turn on lathe to final dimensions: 25.00 mm bore (H5 tolerance, +0.004/0 mm), 31.5 mm OD, 15 mm width. Grind the raceway (the curved track the balls ride on) to a groove radius of 3.97 mm (ball radius + 2-3% for conformity), with 0.05 μm Ra surface finish.
2. **Outer ring**: Forge and turn to 52.00 mm OD (±0.002 mm), 46.5 mm bore with raceway groove, 15 mm width. Grind raceway to same profile and finish as inner ring.
3. **Balls**: Cut 7.94 mm diameter wire into slugs. Cold head into rough spheres in a header. Grind between grooved cast iron plates (the plates have concentric grooves matching the ball radius, and the balls roll between them under load for 2-4 hours). Lap to 1-5 μm sphericity variation using 600-1200 grit abrasive paste. Harden at 820-860°C, oil quench, temper at 150-200°C to 58-62 HRC.
4. **Cage**: Stamp from 0.5 mm brass sheet (or 0.5 mm mild steel sheet). Two halves, each with ball pockets (7 pockets for a 6205 bearing). Rivet halves together through the pillar posts.
5. **Assembly**: Place balls between inner and outer raceways. Compress the cage halves around the balls. Rivet cage halves together. Pack with lithium grease. Install seals or shields (pressed steel, crimped into the outer ring groove).

**Calibration**: Measure bore with a bore gauge: 25.000-25.004 mm (H5 tolerance). Measure OD with a micrometer: 52.000-52.002 mm. Check radial internal clearance with a dial indicator: 0.005-0.015 mm for C2 (tight) clearance, 0.015-0.030 mm for CN (normal) clearance. Spin the bearing by hand — should rotate smoothly with no detectable roughness or clicking.

**Expected performance**: Radial load rating: 14.0 kN (basic static, 6205). Speed rating: 12,000 RPM (grease lubricated) or 15,000 RPM (oil lubricated). Friction coefficient: 0.001-0.002. Service life (L10): 20,000-50,000 hours at rated load and speed. Operating temperature range: -30°C to +120°C with lithium grease.

**Materials specifications**: Bearing steel 52100 (1.0% C, 1.5% Cr, balance Fe) for rings and balls, brass sheet (0.5 mm) or steel sheet (0.5 mm) for cage, lithium grease (NLGI grade 2), NBR rubber or pressed steel for seals.

**Tolerance classes**: ABEC-1 (standard) to ABEC-9 (ultra-precision). Higher classes = tighter tolerances on bore, OD, and runout. Machine tool spindles need ABEC-5 or better.

**Strengths**:
- Very low friction (0.001-0.002 coefficient) — 10× lower than plain bearings
- Precise shaft location — radial clearance of 0.005-0.030 mm
- Pre-sealed, pre-greased units require minimal maintenance

**Weaknesses**:
- Complex manufacturing requiring precision grinding (0.05 μm Ra raceway finish) — beyond bootstrap capability initially
- Sensitive to contamination — even 1-5 μm particles cause raceway damage and premature failure
- Finite fatigue life (L10) — even properly loaded bearings eventually develop subsurface spalling

## Bearing Selection Guide

| Application | Type | Speed | Load | Lubrication |
|-------------|------|-------|------|-------------|
| Line shaft | Plain (babbitt) | Low-medium | Moderate | Oil ring |
| Lathe spindle | Ball bearing (ABEC-5+) | Medium-high | Light-moderate | Grease or oil mist |
| Flywheel | Plain (babbitt) | Low | Heavy | Oil cup |
| Milling spindle | Ball bearing (ABEC-7+) | High | Moderate | Grease |
| Engine crankshaft | Plain (babbitt/insert) | Medium | Heavy | Pressure oil |
| High-speed grinder | Ball bearing or air bearing | Very high | Light | Oil mist |


## Bearing Lubricants

- **Mineral oil**: Refined petroleum oil. Standard lubricant for most bearings. Viscosity grade selected by speed and load (thicker oil for slower speeds and heavier loads).
- **Animal fat (tallow, lard)**: Pre-petroleum lubricant. Works well for plain bearings and slow-speed applications. Lard oil as cutting fluid for turning and threading — reduces friction, improves finish.
- **[Vegetable oil](../glossary/vegetable-oil.md)** (linseed, castor): Cutting fluid for brass and aluminum. Castor oil has excellent film strength for high-speed bearings. Not ideal for steel machining (polymerizes and gums).
- **Grease**: Oil thickened with soap (calcium, lithium, or sodium soap). Stays in place, does not drain away. Used for sealed bearings and slow-speed applications. Lithium grease is the general-purpose standard.

**Strengths**:
- Multiple options available at different technology levels (animal fat at the earliest, mineral oil and synthetic grease later)
- Lubrication dramatically extends bearing life — 10-50× compared to dry running

**Weaknesses**:
- Lubricant contamination (dirt, water, metal particles) degrades performance and accelerates wear
- Some lubricants (vegetable oil, animal fat) have limited shelf life — they oxidize and become acidic

## Precision Metrology for Bearing Production

- **Micrometer**: Measures external dimensions to 0.01 mm resolution. Essential for checking shaft diameters against bearing bore specifications.
- **Bore gauge / inside micrometer**: Measures internal diameters to 0.01 mm. For checking bearing housing bores.
- **Dial indicator**: Measures runout (eccentricity) to 0.01 mm. For checking shaft straightness and bearing alignment.
- **Surface plate**: Flat granite or cast iron reference surface (flat to 0.002 mm). The foundation of all dimensional measurement.

## Limitations

- **Bearing speed limits**: Ball and roller bearings have maximum speed ratings (dN value = bore diameter × speed). Exceeding limits causes lubricant breakdown, cage failure, and seizure. High-speed applications require special designs (angular contact, hybrid ceramic).
- **Bearing fatigue life**: Rolling element bearings fail by subsurface fatigue (spalling) after a statistical number of stress cycles. Rated life (L10) is the cycles at which 10% of bearings fail. Design life typically 20,000-100,000 hours.
- **Contamination sensitivity**: Bearing performance degrades rapidly with particulate contamination. Even 1-5 μm particles cause surface damage. Clean assembly environments and effective sealing are essential.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Babbitt bearing overheating and seizing (operating temp >100°C) | Radial clearance too tight (<0.001× shaft diameter) or oil starvation — babbitt fails within minutes without lubrication | Set radial clearance to 0.001-0.002× shaft diameter (50 mm shaft → 0.05-0.10 mm measured with feeler gauges); verify oil ring dips into reservoir and carries oil to shaft surface; check that oil grooves (2-3 mm wide × 1.5 mm deep) are unobstructed |
| Ball bearing rough rotation (clicking or gritty feel, radial clearance >0.030 mm) | Contamination with 1-5 μm particles scoring raceways, or bearing exceeded L10 fatigue life (20,000-50,000 hours) | Disassemble, clean in solvent, and inspect raceways under 10× magnification for scoring/spalling; replace if raceway damage visible; reassemble in clean environment with fresh lithium grease (NLGI grade 2); ensure seals/shields are intact |

## Cross-References

- [Abrasives & Cutting Tools](./abrasives.md) — abrasive materials and cutting tool production
- [Machining](./machining.md) — lathe, mill, and grinding operations using these tools
- [Iterative Bootstrap](./iterative-bootstrap.md) — building precision machines from these components
- [Forming](./forming.md) — forging and rolling of bearing steel
- [Lubricants](../chemistry/lubricants.md) — cutting fluid and bearing oil production
- [Iron & Steel](../metals/iron-steel.md) — bearing steel (52100) and tool steel production
- [Casting](../metals/casting.md) — casting bearing shells

*Part of the [Bootciv Tech Tree](../index.md) · [Machine Tools Bootstrap](./index.md) · [All Domains](../index.md)*
