# Temperature & Pressure Measurement

> **Node ID**: measurement.temperature-pressure
> **Domain**: [Measurement](./index.md)
> **Dependencies**: [`energy.electricity`](../energy/electricity.md), [`metals`](../metals/index.md)
> **Enables**: [`silicon.crystal-growth.cz-pulling`](../silicon/cz-pulling.md)
> **Timeline**: Years 25-40
> **Outputs**: thermocouples, temperature_measurement, electrical_measurement, pressure_measurement
> **Critical**: No — measurement improves quality but civilization can function without precision instruments

## Problem

Semiconductor manufacturing demands precise thermal control: crystal growth furnaces (1400-1500°C ±0.5°C), diffusion furnaces (800-1200°C ±0.1°C), CVD reactors (300-1100°C), and epitaxial deposition (1050-1200°C). Pressure control is equally critical — vacuum systems for sputtering (10⁻³ to 10⁻⁶ mbar), LPCVD (0.2-2 mbar), and photolithography exposure tools. Without accurate temperature and pressure sensing, process repeatability is impossible.

## Thermocouples

Two dissimilar metals joined at a measurement junction generate a voltage (Seebeck effect) proportional to the temperature difference between the measurement junction and a reference (cold) junction. Output is in the millivolt range — read with a precision millivoltmeter or potentiometer circuit. Cold-junction compensation required (measure reference junction temperature independently, apply correction).

### Thermocouple Type Comparison

| Type | Positive Leg | Negative Leg | Range (°C) | Sensitivity | Best Use |
|------|-------------|-------------|------------|-------------|----------|
| **K** | Chromel (Ni-Cr) | Alumel (Ni-Al) | -200 to +1260 | ~41 μV/°C | General-purpose furnaces, kilns |
| **J** | Iron | Constantan (Cu-Ni) | -40 to +750 | ~51 μV/°C | Reducing atmospheres, older equipment |
| **T** | Copper | Constantan (Cu-Ni) | -200 to +350 | ~43 μV/°C | Cryogenic, low-temperature precision |
| **S** | Pt-10%Rh | Platinum | 0 to +1600 | ~6 μV/°C | High-temperature calibration standard |
| **B** | Pt-30%Rh | Pt-6%Rh | 0 to +1820 | ~1-5 μV/°C | Ultra-high temperature, glass melting |
| **R** | Pt-13%Rh | Platinum | 0 to +1600 | ~6 μV/°C | Similar to Type S, regional preference |

Type K is the workhorse — low cost, wide range, good accuracy (±1.5°C or ±0.25%, whichever is larger). Type S and R serve as secondary calibration references (±1.0°C) because platinum-rhodium alloys are exceptionally stable at high temperature. Type B's output is near zero below 50°C, so no cold-junction compensation needed for high-temperature use.

**Construction**: Thermocouple wire (0.25-3 mm diameter) welded at junction. Insulated with ceramic beads or mineral-packed metal sheath (MgO insulation in Inconel sheath for harsh environments). Sheath protects from corrosion and electrical noise.

## Resistance Temperature Detectors (RTDs)

Platinum wire (or thin-film) sensor whose resistance increases predictably with temperature. Pt100 standard: 100.0 Ω at 0°C, temperature coefficient +0.385 Ω/°C. Accuracy: ±0.1°C (Class A) to ±0.3°C (Class B) over 0-100°C range. Range: -200°C to +850°C.

**Measurement**: Four-wire (Kelvin) connection eliminates lead resistance errors. Constant current source drives sensor, measure voltage drop → R = V/I → temperature from lookup table or Callendar-Van Dusen equation. For semiconductor furnace control, RTDs handle the low-to-mid range; thermocouples handle the high end.

## Bimetallic Strips

Two metals bonded together with different thermal expansion coefficients (e.g., steel + invar, or brass + steel). Temperature change causes differential expansion → strip bends. Calibrated to indicate temperature on a dial (coil-spring bimetallic thermometer). Accuracy: ±1-2% of span. Range: -50°C to +500°C. No electrical power needed — useful as backup sensors and in thermostatic switches (furnace safety cutoffs).

## Pyrometers (Radiation Thermometry)

Non-contact temperature measurement from thermal radiation. Essential for moving targets, molten metals, and semiconductor wafers in process.

- **Optical (brightness) pyrometer**: Operator matches filament brightness against target through eyepiece. Range: 700-3000°C. Accuracy ±5-10°C. Requires skill but no calibration drift.
- **Two-color (ratio) pyrometer**: Measures ratio of radiation at two wavelengths. Emissivity-independent (unlike single-color). Range: 600-3000°C. Accuracy ±0.5%. Preferred for semiconductor furnaces where emissivity varies during process.
- **Infrared thermometer**: Broadband IR detector. Range: -50°C to +3000°C (model-dependent). Accuracy ±1-2%. Fast response (ms). Must correct for target emissivity.

## Pressure Gauges

### Bourdon Tube Gauge

Curved or helical tube of brass, steel, or beryllium copper. Internal pressure straightens the tube → mechanical linkage rotates pointer on dial. Range: 0-1 bar to 0-7000 bar. Accuracy: ±0.5-2% of full scale. Most common industrial pressure indicator. Simple, robust, no power required.

### Diaphragm Gauge

Flexible metal diaphragm (stainless steel, Hastelloy) deflects under differential pressure. Deflection measured mechanically (linkage to dial) or electrically (capacitive or strain-gauge sensor). Range: 0-10 mbar to 0-400 bar. Preferred for low-pressure and corrosive media. Capacitive diaphragm gauges achieve ±0.1% accuracy — used in semiconductor process chambers.

## Barometers

- **Mercury barometer**: Glass tube (~1 m) sealed at top, open at bottom, immersed in mercury reservoir. Atmospheric pressure supports mercury column. Height ≈ 760 mm at sea level. Read with vernier scale to ±0.1 mm Hg (±0.13 mbar). The absolute pressure reference. Mercury toxicity requires careful handling.
- **Aneroid barometer**: Evacuated metal capsule (thin-wall beryllium copper) compresses/expands with atmospheric pressure changes. Mechanical linkage amplifies motion to dial. No mercury. Accuracy ±1-2 mbar. Used for weather monitoring and altitude-corrected process pressure readings.

## Manometers

- **U-tube manometer**: Glass U-tube partially filled with liquid (water, oil, or mercury). Pressure applied to one arm → liquid level difference indicates pressure: P = ρgh. Range depends on fill fluid: water gives ~0.1 mbar resolution (for short tubes), mercury extends to ~1 bar. Absolute calibration — no zero drift. Used as primary standard for low-pressure calibration.
- **Inclined manometer**: Tube tilted at shallow angle (5-15°) → liquid travels further for same pressure change → resolution improved by 1/sin(θ). Resolution: 0.01 mbar with water fill. Used for draft measurement, cleanroom pressure differentials, and HVAC balancing.

## Flow Measurement

- **Orifice plate**: Thin plate with precision bore inserted in pipe. Pressure drop across plate proportional to flow rate squared (Bernoulli's equation). Measure ΔP with differential pressure gauge → compute flow. Simple, cheap, 2-5% accuracy. Permanent pressure loss 30-70% of ΔP.
- **Venturi tube**: Converging-diverging nozzle. Same Bernoulli principle as orifice plate but with gradual profile → lower permanent pressure loss (10-15% of ΔP). More expensive to fabricate but energy-efficient for continuous flow. 1-2% accuracy.

## Construction Procedures

### Liquid-in-Glass Thermometer

**Materials**:
- Borosilicate glass capillary tube (0.1-0.3 mm bore, 5-8 mm OD, 250-400 mm length)
- Mercury (for range -38°C to +357°C) or dyed alcohol (for range -80°C to +70°C)
- Reference temperature baths: ice-water slurry (0.00°C), boiling water (100.00°C at 1 atm)
- Precision dividing engine or scribing tools for scale markings
- Gas-oxygen torch (for borosilicate working)

**Fabrication**:

1. **Capillary tube selection**: Draw tube from borosilicate glass (see [Glass — Advanced](../glass/advanced.md) for tube production methods). Select a length with uniform bore — test by drawing a short mercury thread through and verifying it moves freely without sticking. Bore must be consistent to within 5% or scale readings will be non-linear. Reject tubes with visible constrictions or diameter variations.

2. **Form the bulb**: Heat one end of the capillary tube in gas-oxygen flame until soft. Blow gently through the open end to expand a bulb (5-10 mm diameter). The bulb must be symmetrical and thin-walled (~0.5 mm) for fast thermal response. Wall thickness uniformity matters — thin spots risk breakage during filling and use.

3. **Fill with mercury**:
   - Place mercury in a clean glass dish. Heat to ~150°C to drive off dissolved gases and moisture.
   - Invert the thermometer tube (bulb down). Apply gentle heat to the bulb to expand air inside.
   - Place the open end into the mercury pool. Allow to cool — contraction draws mercury into the bulb and capillary.
   - Repeat heat/cool cycle 3-5 times to fill completely. Any trapped air bubbles cause reading errors at every subsequent step.
   - *Alcohol alternative*: Fill with dyed alcohol (food coloring or eosin), then boil gently to drive out dissolved air before sealing. Alcohol thermometers are less precise but avoid mercury hazards.

4. **Seal the tube**: Heat the open end of the capillary in flame until it collapses and seals closed. Leave a small expansion chamber above the top scale mark — without it, thermal expansion of fill fluid at the top of the range can burst the tube. Ensure the seal is pure glass with no trapped mercury (mercury trapped in the seal vaporizes during annealing and causes drift).

5. **Anneal**: Place in annealing oven at 560°C (borosilicate), hold 30 minutes, cool at 1-2°C/minute to room temperature. Relieves residual stress from sealing and prevents spontaneous cracking days or weeks later.

**Calibration**:

1. Immerse bulb and stem in ice-water slurry (crushed ice + distilled water, well-stirred). Wait 10 minutes for thermal equilibrium. Mark the meniscus position — this is 0°C.
2. Suspend in steam bath above boiling water (not touching water surface) at 1 atm. Mark meniscus — this is 100°C. Correct for local atmospheric pressure: boiling point drops ~0.37°C per 100 m altitude gain.
3. Divide the interval between marks into 100 equal divisions using a precision dividing engine or careful scribing against a reference ruler. For higher accuracy, add intermediate fixed points: melting tin (231.9°C), freezing zinc (419.5°C).
4. Verify linearity by checking at intermediate points (body temperature ~37°C, freezing brine ~-18°C). Non-linearity indicates bore inconsistency — reject and redraw tube.

**Expected accuracy**: ±0.1°C for mercury thermometers with etched scale and magnifier reading. ±0.5°C for alcohol-filled thermometers (alcohol expansion is less linear than mercury).

### Bourdon Tube Pressure Gauge

**Materials**:
- Seamless brass or beryllium copper tube (oval/flat cross-section, 6-10 mm minor axis, 0.5-1.0 mm wall)
- Steel or brass dial plate (100-150 mm diameter) with pre-printed or engraved scale
- Brass pointer (lightweight, balanced, blackened for visibility)
- Brass linkage components: sector gear (partial gear, ~90° arc), pinion (8-12 teeth), connecting link rod
- Jeweled or brass bearings for pivot points
- Silver solder or brass brazing compound for joints
- Deadweight tester or calibrated reference gauge for calibration

**Fabrication**:

1. **Form the Bourdon tube**: Start with oval-cross-section tube (flatten round tube between rollers, or draw through oval die). Bend into C-shape (arc ~270°) around a hardwood or steel form. Radius depends on pressure range: 25-40 mm for low pressure (0-10 bar), 15-25 mm for high pressure (0-100+ bar). The oval cross-section is the active element — internal pressure acts on the flat sides, generating a net unbending force that straightens the tube proportionally to applied pressure.

2. **Seal and connect**: Silver-solder one end of the tube closed. Silver-solder a threaded connector (brass or steel) to the open end — this is the pressure inlet. The connector must be leak-tight and aligned so the tube moves freely in its bending plane without binding.

3. **Build the linkage mechanism**:
   - **Sector gear**: Cut brass sector (partial gear, 20-30 teeth) on dividing engine. Pivot at the center of the tooth arc. One arm connects to the sealed tip of the Bourdon tube via a link rod.
   - **Pinion**: Small brass gear (8-12 teeth) on the pointer shaft, meshing with the sector gear. The gear ratio amplifies motion — a 2° tube tip travel becomes 30-60° pointer rotation on the dial.
   - **Connecting link**: Thin brass strip or threaded rod connecting the Bourdon tube tip to the sector arm. Adjustable length (threaded rod with locknuts) provides the primary calibration adjustment.
   - **Bearings**: Press brass bushings or jeweled bearings (agate or synthetic ruby) into the gauge housing for the sector pivot and pointer shaft. Friction at these pivots is the dominant error source — even tiny friction causes hysteresis (different readings on rising vs. falling pressure).

4. **Assemble**: Mount Bourdon tube in gauge housing with inlet connector aligned to the pressure port. Connect link rod from tube tip to sector arm. Mount sector and pinion in their bearings. Attach pointer to pinion shaft. Install dial plate with scale markings. Seal housing with glass crystal and gasket to protect internals from dust and corrosion.

**Calibration**:

1. Connect gauge to deadweight tester (precision piston of known area + calibrated weights applying known pressure: P = F/A). Apply pressure at 0%, 25%, 50%, 75%, and 100% of full scale.
2. Adjust link rod length to set zero (no pressure → pointer reads zero). Adjust sector arm connection point to set full-scale span.
3. Check intermediate points for linearity. Non-linearity indicates friction, gear backlash, or inconsistent tube response.
4. Check hysteresis: sweep pressure up to full scale, then back down. Rising and falling readings at each point must agree within ±0.5% of span. Excess hysteresis means pivot friction — disassemble, clean bearings, reassemble.
5. Repeat until all points read within tolerance. Lock all adjustments with set screws or locknuts. Apply thread-locking compound to prevent drift.

**Expected accuracy**: ±1-2% of full scale for hand-built gauges with careful calibration. ±0.5% achievable with low-friction jeweled bearings and precise linkage adjustment.

### Mercury Barometer

**Materials**:
- Borosilicate glass tube (~900 mm length, 6-10 mm ID, sealed at one end during drawing)
- Mercury (7-10 kg, reagent grade — triple-distilled if available)
- Glass or stainless steel reservoir dish (50-80 mm diameter, 40+ mm deep)
- Vernier slide with magnifier lens
- Brass or wood mounting tube with hanging hook
- Plumb line for vertical alignment

**Fabrication**:

1. **Prepare the tube**: Clean glass tube with dilute nitric acid (dissolves metal contamination), rinse repeatedly with distilled water, dry in oven at 120°C. Any contamination or residue on the inner wall creates nucleation sites for air bubbles, causing permanent reading errors. Verify the sealed end is fully closed — pressurize with a rubber bulb and immerse in water; any bubbles indicate a pinhole leak.

2. **Fill with mercury**:
   - Stand the tube vertically with sealed end down, open end up, in a clean glass tray.
   - Pour mercury slowly into the open end using a small funnel lined with filter paper (catches dust particles that would block the column).
   - Fill to within ~20 mm of the top. Tap the tube gently along its length with a wooden stick to dislodge trapped air bubbles clinging to the walls.
   - **Remove dissolved air**: Warm the filled tube gently in a water bath (~50°C, not hotter — mercury expands significantly). Dissolved air expands out of the mercury and rises as visible bubbles. Tap again. Repeat warm/tap cycle 3-4 times until no more bubbles appear.
   - *Vacuum fill method* (if vacuum equipment available): Place tube and mercury in vacuum chamber. Evacuate to <1 mbar to boil off dissolved air from the mercury. Allow mercury to fill the degassed tube. Produces a more perfect Torricelli vacuum above the finished column.

3. **Invert into reservoir**:
   - Place a clean gloved finger over the open end of the completely filled tube.
   - Invert the tube in one smooth motion, immersing the finger-covered end into the mercury reservoir before removing your finger.
   - Remove finger only after the open end is below the reservoir mercury surface. Atmospheric pressure now supports the column; vacuum forms above.
   - The mercury column drops to ~760 mm at sea level. If it drops much lower (or mercury separates with a visible gap), air leaked in during inversion — drain, refill, and retry.
   - A properly filled barometer shows a clean, bright mercury column with a convex meniscus and a completely dark, empty space above (the Torricelli vacuum).

4. **Mount the barometer**:
   - Hang tube vertically by the sealed end from a hook or bracket. Never rest it on the reservoir bottom — glass breaks under its own weight plus mercury load.
   - Brass or wood mounting tube protects the glass from accidental impact and provides a mounting surface for the scale.
   - Verify vertical alignment with a plumb line — a 2° tilt causes ~0.06 mm reading error, accumulating over many readings.

**Calibration**:

1. **Set the zero reference**: Adjust the reservoir level or the vernier zero to the mercury surface in the reservoir. Some designs use an ivory or glass pointer — lower it until it just touches its reflection in the reservoir mercury surface (zero contact point).
2. **Read the column**: Slide the vernier scale until its horizontal index aligns with the top of the mercury meniscus (convex dome). Read the vernier to 0.1 mm resolution.
3. **Temperature correction**: Mercury expands with temperature, making the column appear taller at higher temperatures. Apply correction: P_corrected = P_observed × [1 - (α_Hg - α_glass) × (T - 0°C)], where α_Hg = 181 × 10⁻⁶/°C, α_glass ≈ 3 × 10⁻⁶/°C (borosilicate). At 20°C, the uncorrected reading is ~2.5 mm Hg too high. Record temperature at every reading and apply correction.
4. **Gravity correction**: Standard gravity is 9.80665 m/s². Local gravity varies with latitude and altitude (±0.3% from standard). Apply correction factor g_local / g_standard if high accuracy is required.
5. **Expected accuracy**: ±0.13 mbar (±0.1 mm Hg) with vernier scale, temperature correction, and careful reading technique. This is the absolute pressure reference against which all other pressure instruments are calibrated.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Metallurgy | Thermocouples (dissimilar metal junctions), bimetallic strips |
| Energy | Temperature monitoring for steam systems, pressure gauges for boilers |
| Chemistry | Process temperature control (reactions, distillation columns) |
| Vacuum & Optics | Low-pressure measurement for vacuum systems, pyrometers |
| Silicon | Furnace control for crystal growth, diffusion, oxidation (RTDs + thermocouples) |
| Photolithography | Precision chamber pressure and temperature for resist processing |

## Key Deliverables

- Thermocouple sets (Type K for general use, Type S for calibration, Type J for reducing atmospheres)
- Pt100 RTDs with four-wire readout for ±0.1°C furnace control
- Bourdon tube and diaphragm pressure gauges for process monitoring
- Mercury barometer as absolute pressure reference
- U-tube manometers for low-pressure calibration
- Two-color pyrometers for non-contact high-temperature measurement
- Orifice plates and venturi tubes for process flow measurement

## Safety & Hazards

- **Mercury toxicity**: Mercury vapor from spills, broken thermometers, and barometer filling causes cumulative neurological damage (tremor, memory loss, kidney damage). IDLH: 10 mg/m³. Vapor pressure at 20°C is 0.0012 mm Hg — enough to exceed safe limits in unventilated rooms after a spill. Fill barometers in fume hoods or under local exhaust ventilation. Clean spills immediately with zinc dust or commercial mercury absorbent sponge — never vacuum (vaporizes mercury and disperses it through the exhaust). Store mercury in sealed glass containers under water or mineral oil to suppress vaporization. Use mercury-free alternatives (alcohol thermometers, thermocouples, aneroid barometers) wherever precision requirements permit. Pregnant workers must not handle mercury or work in mercury exposure areas.
- **Pressure testing hazards**: Hydraulic and pneumatic proof-testing of Bourdon gauges, manometer fittings, and pressure connections risks explosive failure. A Bourdon tube at 100 bar stores sufficient strain energy to launch brass fragments through sheet metal. Test behind a polycarbonate blast shield (minimum 6 mm thickness). Use hydraulic fluid (incompressible — stores minimal energy) rather than compressed air (compressible — stores energy proportional to volume × pressure) for all proof tests. Pressurize slowly (1-2 bar/second maximum). Never exceed 1.5× rated working pressure. Inspect tubes for cracks, thin walls, and defective brazed joints before every test cycle. Replace any gauge that has been over-pressured — permanent deformation may not be visible but causes calibration drift and weakened burst resistance.
- **High-temperature burn risks**: Glass tube drawing (800-1100°C), thermometer bulb forming (800-1100°C), and tube sealing (700-900°C) all involve temperatures far above the instantaneous skin-burn threshold (~70°C for 1-second contact). Borosilicate glass at working temperature shows only a dull red glow — it does not look "hot" in bright lighting. Silica glass working requires hydrogen-oxygen torch at 3400°C flame temperature. Use heat-resistant gloves (leather or Kevlar, rated to 500°C) when handling hot glass. Use tungsten-carbide-tipped tongs for sustained high-temperature work (steel tongs soften above 800°C). Keep a burn kit with sterile dressings and cool running water within arm's reach of all glassworking stations. Eye protection is mandatory — hot glass spalls without warning, and mercury spatter from overfilled thermometers causes corneal damage.

## Limitations

- **Thermocouple accuracy**: Base-metal thermocouples (Type K, J, T) achieve ±1-2°C accuracy. Precious-metal thermocouples (Type S, R) achieve ±0.5°C but are expensive. Thermocouple accuracy degrades with age and thermal cycling due to drift in the Seebeck coefficient. Regular calibration against fixed-point references (ice point 0°C, steam point 100°C) is essential.
- **Mercury hazards**: Mercury-filled thermometers and barometers contain elemental mercury, a neurotoxin. Breakage creates hazardous contamination. Alcohol-filled thermometers are safer but less precise (±1°C vs. ±0.1°C). Digital sensors (thermistors, RTDs) eliminate mercury risk but require electronics.
- **Pressure gauge calibration**: Bourdon tube gauges drift with age and overpressure events. Annual calibration against a dead-weight tester (precision weights applying known pressure) is required for critical measurements. Uncalibrated gauges may read 5-10% off actual pressure.
- **Manometer limitations**: U-tube manometers provide excellent accuracy (±0.1 mm of fluid column) but are limited to low pressures (below ~2 bar for mercury, ~0.2 bar for water). They require vertical mounting, stable temperature (fluid density changes with temperature), and careful reading of meniscus.
- **No digital data logging**: Without electronics, all measurements are read visually and recorded manually. Continuous monitoring requires an operator present at all times. Data logging (chart recorders, digital acquisition) arrives with the electronics stage.

## See Also

- [Precision Metrology](precision-metrology.md) — base unit standards, calibration infrastructure
- [Optical Instruments](optical-instruments.md) — spectroscopes, refractometers, interferometers
- [Electrical Instruments](electrical-instruments.md) — multimeters, oscilloscopes, frequency counters
- [Energy](../energy/index.md) — steam power, boilers (major application of temperature/pressure measurement)
- [Chemistry](../chemistry/index.md) — thermocouple materials, mercury production

---

*Part of the [Bootciv Tech Tree](../index.md) • [Measurement](./index.md) • [All Domains](../index.md)*
