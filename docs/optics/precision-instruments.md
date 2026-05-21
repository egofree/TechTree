# Precision Optical Instruments

> **Node ID**: optics.precision-instruments
> **Domain**: [Optics](./)
> **Dependencies**: `optics.inspection`, `measurement.optical-instruments`
> **Timeline**: Years 30-45
> **Outputs**: precision_lenses, optical_flats, interferometers, autocollimators, optical_comparators

## Problem

Semiconductor manufacturing tolerances shrink with every generation. Photolithography lenses demand surface figures better than λ/20 (25 nm). Mask flatness must be within λ/10 per centimeter. Alignment stages require angular positioning to arcsecond accuracy. Producing and verifying these surfaces needs instruments that measure what the eye cannot see, pushing optical fabrication from craft into metrology-grade precision.

## Precision Lens Manufacturing

Transforming a glass blank into a lens accurate to a fraction of a wavelength requires a controlled sequence of abrasive operations, each progressively finer, followed by polishing and figuring.

### Rough Grinding

Silicon carbide (SiC) abrasive, 80-220 grit (particle size 180-68 μm), removes bulk material quickly. Fix the glass blank to a cast iron tool whose curvature matches the desired lens surface (convex tool for concave lens, concave tool for convex lens). Apply abrasive slurry (SiC + water) and stroke the blank across the tool in random overlapping paths. Typical removal rate: 0.5-2 mm/hour. Check radius of curvature with a spherometer or template every 15 minutes. Coarse grit leaves pits 50-100 μm deep, removed in subsequent stages.

### Fine Grinding

Progress through 400 grit (23 μm) and 600 grit (14 μm). Each stage removes the pit damage from the previous stage, requiring removal of 3-5× the previous grit diameter. At 600 grit, the surface appears translucent and the correct curvature is within 5-10 μm of nominal. Wash the blank, tool, hands, and bench thoroughly between grits. A single grain of 80-grit SiC carried into the 600-grit stage will produce a deep scratch, forcing a return to 400 grit.

### Polishing

Cerium oxide (CeO₂) slurry (0.5-3 μm particle size, 5-15% by weight in water) on a pitch lap. The pitch (derived from pine tar or petroleum residues, hardness graded by pen test: soft pitch indents under a 1 kg load in 2-5 seconds at room temperature) conforms to the glass surface under pressure, ensuring uniform contact. Polishing removes the fine-ground surface layer at 0.1-0.5 μm/hour. Duration: 2-8 hours for a 50-100 mm diameter lens. The surface transitions from translucent to transparent. Test by reflecting a point source: a polished surface shows a sharp specular reflection.

### Figuring

Figuring corrects the polished surface from a sphere to the desired aspheric profile (paraboloid, hyperboloid, or multi-element correction). Zone tools (pitch laps cut to contact specific annular zones) selectively polish high areas identified by interferometric testing. Each figuring iteration: test → identify high zones → polish with zone tool → retest. A typical 100 mm camera lens requires 3-8 figuring iterations. A lithography-grade lens may require 20-50 iterations over weeks.

## Flat Surface Production

The three-plate method produces optically flat surfaces without any pre-existing reference flat. Three glass plates (A, B, C) are ground and polished alternately:

1. Grind A against B until they show uniform contact.
2. Grind B against C until uniform contact.
3. Grind C against A until uniform contact.
4. Repeat the cycle through fine grinding and polishing stages.

If A fits B and B fits C and C fits A, all three must be flat. Any curvature would cause a mismatch in at least one pairing. After 3-5 cycles through each grit stage, all three plates achieve flatness within λ/4 (140 nm) over their full aperture. Further polishing with fine figuring brings them to λ/10 or better.

## Angle Measurement

### Autocollimator

An autocollimator measures small angular deviations with extreme precision. Layout: light source → reticle (illuminated crosshair) → beam splitter → objective lens → target mirror → reflected light returns through objective → beam splitter → eyepiece with measuring scale.

When the target mirror is exactly perpendicular to the optical axis, the reflected reticle image coincides with the reticle itself. A mirror tilt of angle θ displaces the reflected image by 2f·tan(θ) at the focal plane, where f is the objective focal length. With f = 200 mm and a scale reading to 1 μm, the angular resolution is 0.5 arcseconds.

**Applications**: Straightness measurement of machine tool ways (reflect mirror along the ways, autocollimator reads angular changes at each position), perpendicularity checking, rotary table calibration, level measurement. Resolution to 0.1 arcsecond achievable with photoelectric readout.

### Optical Square

A pentagonal prism or mirror arrangement that deflects light by exactly 90°, regardless of small angular errors in the mounting. Used to establish perpendicular reference lines for machine tool alignment and construction. Accuracy: ±1 arcsecond for a quality pentagonal prism. Simpler than an autocollimator for 90° checks, and more compact than a precision engineer's square.

## Interferometric Flatness Testing

### Fizeau Interferometer

The Fizeau interferometer is the primary instrument for measuring surface flatness of optical components. A monochromatic light source (helium discharge lamp, λ = 587.6 nm, or laser) illuminates a reference flat (typically λ/20 flatness) resting on the test surface. A thin air wedge between the two surfaces creates interference fringes. Straight, equally spaced fringes indicate a flat surface. Curved or irregular fringes reveal surface errors.

**Interpretation**: One fringe deviation from straightness corresponds to λ/2 surface error (approximately 294 nm for He lamp). Counting fringe deviations: a surface showing two fringes of deviation has λ = λ/2 × 2 = one full wavelength of error. Certified reference flats (λ/10, λ/20) provide the measurement baseline. Flatness specification for lithography optics: λ/20 (29 nm) per 100 mm aperture.

**Recording**: Photograph the fringe pattern with a camera mounted above the interferometer. Measure fringe deviations from a straight reference line on the photograph. Digital analysis (fringe tracking software) automates the process, but manual reading with a ruler on a photograph suffices for most workshop applications.

### Newton's Rings

When a slightly curved lens surface rests on a flat reference surface, the air gap between them creates concentric circular interference fringes (Newton's rings). The radius of the nth dark ring is rₙ = √(nλR), where R is the radius of curvature. Counting rings from the center quantifies the deviation from flatness or the radius of curvature. Quick, requires only a reference flat and a monochromatic light source. Accuracy: λ/2 per ring, limited by contact pressure and cleanliness.

## Precision Levels

### Tubular Vial Level

A precision level uses a glass vial with a slightly curved inner surface (radius of curvature 10-50 m). An air bubble in the vial settles at the highest point. When the base tilts, the bubble moves. Vial sensitivity is the tilt angle that moves the bubble one division mark: 0.02 mm/m (4 arcseconds) for precision workshop levels, 0.01 mm/m (2 arcseconds) for laboratory-grade instruments.

**Construction**: The vial is mounted in a rigid cast iron or granite body with a flat reference surface (scraped or lapped flat to 0.005 mm). Adjusting screws (two, at opposite ends) allow zero-setting on any surface. The vial radius determines sensitivity: R = b/α, where b is the division spacing (typically 2 mm) and α is the sensitivity in radians. For 0.02 mm/m sensitivity: R = 2mm / 0.00002 = 100 m.

**Applications**: Machine tool installation (leveling lathe beds, milling machine columns), surface plate calibration, building straightness checks. The precision level is the foundation of all dimensional metrology in the machine shop.

## Optical Comparator

A profile projector (optical comparator) casts a magnified shadow of a workpiece onto a screen, where it is compared against a template drawing.

**Layout**: Light source (tungsten halogen or LED) → condenser lens (produces parallel illumination) → workpiece on stage → projection lens (10×, 20×, 50×, or 100× magnification) → first-surface mirror (folds optical path, keeps the instrument compact) → ground-glass projection screen (300-600 mm diameter).

**Measurement methods**:
- **Template overlay**: A mylar drawing of the part profile with tolerance bands is placed on the screen. If the shadow falls within the tolerance band, the part passes. Fast, visual, good for 0.05 mm tolerance at 20× magnification.
- **Screen crosshairs**: Rotating crosshairs etched on the screen, with digital readout of the angular position. Align crosshairs with shadow edges to measure angles. Accuracy: ±3 arcminutes at 20×.
- **Stage micrometers**: The workpiece stage moves in X-Y on precision micrometer screws (0.001 mm resolution). Measure feature positions by moving the stage to align the crosshair with each edge and reading the micrometers.

**Applications**: Thread profile inspection, gear tooth measurement, small machined parts, stampings, and molded components. Non-contact: measures soft, fragile, or flexible parts without deformation. The workhorse inspection instrument in any precision machine shop.

## Coordinate Measuring with Optics

### Toolmaker's Microscope

A toolmaker's microscope combines a compound optical microscope with a precision X-Y stage and angular measurement capability, designed for dimensional inspection of small parts and cutting tools.

**Stage**: X-axis travel 100 mm, Y-axis travel 50 mm. Linear scales (glass or steel, 0.001 mm resolution) on both axes. Rotatable circular stage with 360° graduation and vernier reading to 1 arcminute. Stage flatness: 0.005 mm over full travel.

**Optics**: Fixed-magnification objectives (2×, 5×, 10×) with 10× eyepiece containing a protractor reticle (360° scale with 1° divisions and vernier). Total magnification: 20× to 100×. Working distance: 50-80 mm (room for the workpiece and stage).

**Measurement capabilities**: Length (X-Y stage micrometers), angle (rotary stage + protractor reticle), thread pitch and profile, tool cutting edge angles, radius gauges, small hole diameters (using the double-image method with a birefringent prism). Accuracy: ±0.003 mm for linear measurements, ±1 arcminute for angles.

## Optical Flat Reference Standards

Optical flats are the primary reference for surface flatness measurement. They are discs of fused silica or optical glass, the measuring surface polished to a specified flatness tolerance.

**Material**: Fused silica preferred over optical glass for reference standards. Coefficient of thermal expansion: 0.5 × 10⁻⁶/°C for fused silica versus 3-7 × 10⁻⁶/°C for optical glasses. A 100 mm diameter fused silica flat changes flatness by only 0.5 nm per °C temperature change. BK7 optical glass changes by 3-7 nm per °C for the same geometry.

**Flatness grades**:
- λ/10 (63 nm per 100 mm): Workshop reference. Adequate for general machine shop flatness testing.
- λ/20 (31 nm per 100 mm): Precision reference. Used for calibrating surface plates, measuring gauge blocks.
- λ/50 (12 nm per 100 mm): Laboratory master. Calibration of other optical flats. Requires temperature-controlled storage (±0.5°C).

**Care and handling**: Handle only by the edges with cotton gloves. Finger contact on the measuring surface leaves oils that produce spurious fringes. Store in a padded wooden case, measuring surface facing up, covered with a lint-free cover. Re-calibrate annually against a master flat by Fizeau interferometry.

## Cleaning Procedures

Clean optics are a prerequisite for all precision optical work. A single dust particle on an optical flat creates a spurious fringe. A fingerprint on a lens scatters light and degrades contrast.

### Standard Cleaning Procedure

1. **Remove loose dust**: Blow with clean, oil-free compressed air or a rubber bulb. Never brush; brushing drags particles across the surface and scratches.
2. **Remove oils and residues**: Apply a few drops of acetone or isopropanol (reagent grade, not rubbing alcohol which contains water and oils) to a lint-free lens tissue (not paper towel, not cotton cloth). Do not apply solvent directly to the optic.
3. **Drag wipe technique**: Lay the dampened tissue flat on the surface. Pull it slowly across the surface in one smooth motion with gentle, even pressure. The solvent evaporates behind the moving tissue front, carrying dissolved contaminants away. Never rub in circles. Never apply heavy pressure. Let the solvent do the work.
4. **Inspect**: View the surface under a bright light at a grazing angle (hold the optic and look at the reflected light source). Residual streaks or spots require repeat cleaning.
5. **Persistent contamination**: For dried deposits, apply solvent and let it soak for 30 seconds before drag wiping. Avoid this on cemented optics (achromatic doublets, Amici prisms) because solvent can dissolve the Canada balsam or optical cement.

### Materials to Avoid

- **Acetone on plastic optics**: Dissolves acrylic, polycarbonate, and many adhesives. Use only on glass and fused silica.
- **Household glass cleaners**: Contain detergents and ammonia that leave films. These films are invisible under casual inspection but produce measurable scatter in precision instruments.
- **Lens pens and cleaning cloths**: Silicone-impregnated cleaning tools leave a thin silicone film. Acceptable for camera lenses, unacceptable for interferometric optics.
- **Ultrasonic cleaning**: Useful for removing particulate contamination from prisms and large optics, but can crack cemented assemblies and damage thin-film coatings if the frequency or power is too high.

## Construction: Optical Flat

**Materials**:
- Fused silica blank (25-150 mm diameter, 15-25 mm thickness, faces parallel within 0.1 mm)
- Cast iron lapping plate (300-600 mm diameter, flat to 0.01 mm)
- Silicon carbide abrasives: 220, 400, 600 grit
- Cerium oxide polishing compound (1-3 μm)
- Pine pitch for polishing lap
- Monochromatic light source (sodium lamp, 589.3 nm)
- Reference optical flat (one grade higher than target)

**Procedure**:

1. **Rough lap**: Grind the blank on the cast iron plate with 220 grit SiC until both faces are flat and parallel. Check parallelism with a micrometer at four points around the edge (variation < 0.02 mm).

2. **Fine grind**: Progress through 400 and 600 grit on the lapping plate. Rinse thoroughly between grits. After 600 grit, the surface should appear semi-transparent with no visible pits.

3. **Make the pitch lap**: Pour molten pitch onto a flat cast iron tool. Press the ground blank into the warm pitch to create a conforming surface. Cut channels (2 cm grid) with a hot knife to allow pitch flow during polishing.

4. **Polish**: Charge the pitch lap with cerium oxide slurry. Polish the blank with slow, random strokes for 4-8 hours. Test by viewing a distant point source reflected in the surface: no scattering halo indicates a polished surface.

5. **Figuring**: Test flatness against the reference flat using Fizeau fringes (sodium lamp illumination). Identify high zones. Polish selectively with smaller zone tools to reduce deviations. Retest after each figuring session. Repeat until fringes are straight within the target tolerance.

6. **Certify**: Measure fringe deviation photographically. Calculate flatness error in fractions of a wavelength. Engrave the flatness certification (e.g., "λ/10 per 100 mm") on the edge of the flat with a diamond scribe.

**Expected result**: λ/10 flatness per 100 mm diameter on the first attempt. λ/20 achievable with careful figuring and a stable temperature environment (±1°C during figuring).

### Thermal Stabilization

Before any precision flatness measurement, the optical flat and the test piece must equilibrate to the same temperature. A 100 mm fused silica flat handled for 30 seconds with bare hands absorbs enough heat to distort by λ/5. Allow a minimum of 30 minutes thermal settling time after handling before performing interferometric tests. For λ/20 measurements, allow 2 hours in a temperature-stable room (±0.5°C). Mark the settling time on the flat's storage case as a handling reminder.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Optics | Precision lenses, flats, and prisms for all optical instruments |
| Machine Tools | Autocollimator and level for machine alignment and calibration |
| Measurement | Interferometric flatness testing, optical comparator inspection |
| Photolithography | Lens figuring expertise for projection optics, flat references for masks |
| Silicon | Wafer flatness measurement by interferometry |
| Semiconductor Processing | Precision dimensional measurement of machined components and fixtures |

## Key Deliverables

- Lenses figured to λ/10 or better for imaging and projection systems
- Optical flat reference standards (λ/10, λ/20, λ/50 grades)
- Autocollimator for 0.1 arcsecond angular measurement
- Fizeau interferometer for surface flatness testing
- Precision tubular vial levels (0.02 mm/m sensitivity)
- Optical comparator (profile projector) with 10-100× magnification
- Toolmaker's microscope with 0.001 mm resolution

## Safety & Hazards

- **Pitch burns and fumes**: Polishing pitch melts at 60-80°C and causes deep burns on skin contact. Heating pitch produces volatile organic vapors (terpenes, aromatics) that irritate eyes and respiratory tract. Heat pitch in a ventilated area or under local exhaust. Wear leather gloves when handling warm pitch. Pitch fires are difficult to extinguish (dense smoke, reignition). Keep a fire blanket and sand bucket nearby, not water (causes splattering).
- **Cerium oxide and abrasive dust**: Dry cerium oxide powder and dried abrasive slurries produce respirable dust. Inhalation of fine cerium oxide particles causes pulmonary granulomas with chronic exposure. SiC dust is a mechanical irritant. Keep slurries wet. Clean spills while wet. Wear a dust mask (P100 respirator) when handling dry powders or cleaning dried polishing residues.
- **Acetone and isopropanol**: Both solvents are flammable (acetone flash point -20°C, isopropanol 12°C). Use in well-ventilated areas away from ignition sources. Acetone defats skin and causes cracking with repeated contact. Isopropanol is less aggressive but still drying. Wear nitrile gloves for prolonged solvent use. Store in flammable-liquid cabinets with grounding to prevent static ignition.
- **Optical flat breakage**: Fused silica optical flats are brittle and expensive. A dropped 100 mm diameter flat shatters into sharp fragments. Handle over a padded surface. Never place a flat face-down on a hard bench. Use a protective carrier (wooden or foam-lined case) for transport between instruments.

---

*Part of the [Bootciv Tech Tree](../) • [Optics](./) • [All Domains](../)*

[← Back to Optics](index.md)
