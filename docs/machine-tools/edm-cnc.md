# EDM, CNC & Precision Grinding

> **Node ID**: machine-tools.edm-cnc
> **Domain**: Machine Tools Bootstrap
> **Timeline**: Years 25-50
> **Outputs**: edm_parts, cnc_machined_parts, precision_ground_surfaces
> **Dependencies**: [`energy.electricity`](../energy/electricity.md), [`machine-tools.machining`](machining.md)
> **Enables**: None (leaf capability)

Conventional machining (lathe, mill, drill — covered in [Machining](./machining.md)) reaches a practical floor around ±0.005 mm tolerance and 0.1 μm Ra surface finish. Semiconductor equipment demands sub-micron precision: wafer stage flatness below 0.5 μm across 300 mm, lens molds with nanometer-scale figure error, and IC package mold cavities with ±2 μm dimensional accuracy. This document covers three enabling technologies that break through conventional limits: Electrical Discharge Machining (EDM), Computer Numerical Control (CNC), and precision/ultra-precision grinding.

## Electrical Discharge Machining (EDM)

EDM removes material by controlled electrical sparks eroding the workpiece in a dielectric fluid bath. No mechanical cutting force is applied — the tool electrode never touches the workpiece. This enables machining of any electrically conductive material regardless of hardness, including hardened tool steel (60+ HRC), tungsten carbide, and titanium alloys.

### Spark Erosion Physics

Each spark discharge follows a sequence occurring in 1-100 μs:

1. **Voltage buildup**: Open-circuit voltage of 60-300 V applied across the spark gap (0.01-0.5 mm). No current flows yet.
2. **Dielectric breakdown**: The electric field ionizes the dielectric fluid in the narrowest gap region, forming a plasma channel (8,000-12,000°C locally).
3. **Material removal**: A tiny crater of material melts and partially vaporizes. The plasma pressure expels the molten material into the dielectric.
4. **Deionization**: Voltage drops, plasma collapses, dielectric recombines and flushes debris. Cycle repeats at 5-500 kHz.

Material removal rate: 1-100 mm³/min depending on power, electrode area, and material. Higher power = faster removal but rougher finish.

**Spark gap (overcut)**: The discharge gap is typically 0.01-0.05 mm per side. This must be compensated in electrode dimensions — a 10.00 mm electrode produces a ~10.04-10.10 mm cavity in the workpiece.

### Wire EDM

A thin brass or coated wire (0.05-0.30 mm diameter) serves as the electrode, continuously fed from a spool through the workpiece. The workpiece is mounted on an X-Y table that traces the cut profile.

- **Wire diameter**: Standard 0.25 mm brass wire for general work; 0.10 mm for fine features; 0.05 mm for micro-EDM (special zinc-coated or molybdenum wire).
- **Accuracy**: ±2-5 μm positional accuracy on modern machines. Taper cutting up to ±30° achievable with upper/lower independent guide control.
- **Surface finish**: 0.2-1.6 μm Ra depending on number of skim passes. Roughing cut: ~3-5 μm Ra. First skim: ~1.5 μm Ra. Second skim: ~0.8 μm Ra. Third skim: ~0.2-0.4 μm Ra.
- **Cutting speed**: 50-250 mm²/min in 50 mm thick steel (depends on material, thickness, wire diameter, and power). Thinner cuts faster; thicker slower.
- **Wire tension**: 5-15 N (500-1500 gf). Too loose = wire vibration and poor accuracy. Too tight = wire breakage.
- **Dielectric**: Deionized water (resistivity 1-20 MΩ·cm). Water quality directly affects cut quality — must maintain filtration and deionization.
- **Applications**: Extrusion dies, progressive stamping dies, gear profiles, turbine blade roots, IC leadframe dies, micro-mechanical components.

### Sinker EDM (Ram EDM)

A shaped electrode (typically copper, graphite, or copper-tungsten) is lowered into the workpiece, reproducing the electrode geometry as a cavity. No wire — the electrode is a 3D form.

- **Electrode materials**: Copper (good wear resistance, easy to machine), graphite (very low wear at high power, excellent for roughing), copper-tungsten (best wear ratio, expensive). Electrode wear ratio (workpiece removed : electrode lost) ranges from 1:1 (poor) to 100:1 (excellent with graphite at low power).
- **Electrode manufacturing**: The electrode itself must be machined (CNC milling, turning, or even another EDM operation). Multiple electrodes may be needed — roughing electrode with higher power/faster cut, followed by finishing electrode(s) with lower power/better finish.
- **Cavity accuracy**: ±5-10 μm typical. Surface finish: 0.8-6 μm Ra depending on settings.
- **Orbital motion**: Modern sinker EDM adds orbital (planetary) electrode motion to improve flushing and uniformity. Reduces electrode wear, improves surface finish by 30-50%.
- **Dielectric fluid**: Hydrocarbon oil (kerosene-based, flash point >90°C) or synthetic dielectric. Oil provides better surface finish than water for sinker EDM but is a fire hazard at high power. Must be filtered to <5 μm particle size.
- **Applications**: Injection molds, die-casting dies, forging dies, turbine blade cooling holes, IC packaging mold cavities, connector housings.

### Small Hole EDM (Hole Drilling)

Specialized EDM for drilling small, deep holes using a tubular electrode.

- **Hole diameter**: 0.1-3.0 mm (limited by available tube electrodes).
- **Aspect ratio**: Up to 100:1 (depth:diameter). A 0.5 mm hole can be drilled 50 mm deep.
- **Speed**: 1-30 mm/min penetration rate. Faster than conventional drilling for hard materials.
- **Applications**: Turbine blade cooling holes (0.3-1.0 mm, angled), fuel injector spray holes, start holes for wire EDM threading.

### EDM Process Parameters

| Parameter | Wire EDM | Sinker EDM | Hole Drilling |
|-----------|----------|------------|---------------|
| Voltage | 60-100 V | 60-300 V | 60-150 V |
| Peak current | 5-50 A | 5-200 A | 5-30 A |
| Pulse duration | 0.5-10 μs | 1-100 μs | 1-20 μs |
| Spark gap | 0.02-0.05 mm | 0.02-0.10 mm | 0.02-0.05 mm |
| Surface finish | 0.2-1.6 μm Ra | 0.8-6 μm Ra | 1-5 μm Ra |
| Accuracy | ±2-5 μm | ±5-10 μm | ±10-20 μm |

### Limitations

- **Conductivity requirement**: Only works on electrically conductive materials. Cannot machine ceramics, glass, plastics, or diamond directly.
- **Recast layer**: EDM leaves a thin (1-10 μm) resolidified and heat-affected layer on the machined surface. This layer is hard and brittle with micro-cracks. Critical parts may require post-EDM grinding or polishing to remove it.
- **Slow material removal**: EDM is 5-50× slower than conventional machining for bulk removal. Best for complex geometries, hard materials, and precision features.
- **Electrode wear**: Sinker EDM electrodes wear and must be periodically replaced or re-machined. Wire EDM avoids this by using fresh wire continuously.
- **Dielectric management**: Requires clean, filtered dielectric fluid. Oil-based dielectric is a fire hazard. Water-based dielectric causes rust on ferrous workpieces without inhibitors.

## Computer Numerical Control (CNC)

CNC replaces manual handwheel operation with motor-driven axes controlled by a computer executing programmed motion commands (G-code). This provides repeatable, programmable positioning accuracy far beyond manual machining, enabling complex 3D contours, automated tool changes, and consistent production of identical parts.

### Servo and Stepper Drive Systems

CNC machines use electric motors to drive each axis. Two types dominate:

**Stepper motors**: Open-loop positioning. Controller sends pulses; motor rotates a fixed angle per pulse (typically 1.8° = 200 steps/rev). No position feedback — if the motor misses a step, position is lost.

- **Resolution**: With 5 mm pitch ball screw, 1.8° stepper gives 0.025 mm/step. With 10× microstepping: 0.0025 mm/step (theoretical — actual accuracy is lower due to torque ripple).
- **Maximum speed**: ~1000-2000 RPM before torque drops significantly. Rapid traverse: 5-15 m/min.
- **Application**: Light-duty CNC routers, desktop mills, entry-level CNC lathes. Not suitable for high-precision or high-load applications.

**Servo motors**: Closed-loop positioning with encoder feedback. Controller compares commanded position to actual position and adjusts motor current continuously.

- **Encoder resolution**: Rotary encoders: 1,000-100,000 counts/rev. Linear encoders (direct position readout on the axis): 0.01-1 μm resolution.
- **Positioning accuracy**: With precision ball screws and linear encoders: ±1-5 μm over 1 m travel on precision CNC machines. High-end machines: ±0.5 μm.
- **Repeatability**: ±0.5-2 μm on precision machines.
- **Maximum speed**: Rapid traverse 20-60 m/min. Cutting feed up to 10 m/min.
- **Application**: All precision CNC machine tools, semiconductor equipment, wafer stages.

### Ball Screws and Linear Motion

Ball screws convert rotary motion to linear motion with minimal friction and backlash:

- **Construction**: Precision-ground screw shaft with ball nut containing recirculating ball bearings. Balls roll between screw and nut threads.
- **Lead accuracy**: ±5-50 μm over 300 mm for precision-ground screws (C3-C5 class). Rolled screws: ±50-200 μm (C7-C10).
- **Preloading**: Double-nut or single-nut preload eliminates backlash to <1-3 μm. Essential for bidirectional positioning accuracy.
- **Efficiency**: 90-95% (vs. 30-50% for Acme lead screws). Most of the motor torque goes into positioning, not overcoming friction.
- **Maximum length**: Practical limit ~3-5 m before screw whip (critical speed). Longer axes use rack-and-pinion or linear motors.
- **Lubrication**: Grease or oil bath. Cleanliness critical — contamination accelerates wear. Semiconductor equipment uses cleanroom-compatible lubricants.

### Linear Encoders and Feedback

Closed-loop positioning requires accurate position measurement:

- **Optical linear encoders**: Glass scale with precisely etched grating (20 μm pitch typical). Photodetector reads interference pattern. Resolution to 0.01 μm with electronic interpolation. Standard for precision CNC.
- **Magnetic linear encoders**: Magnetic tape with pole spacing (1-5 mm). Hall effect sensors read position. Less precise (1-5 μm resolution) but more robust against contamination. Used in harsh environments.
- **Laser interferometers**: HeNe laser (632.8 nm wavelength) measures position by counting interference fringes. Resolution: 0.001 μm (1 nm). Used for calibration and ultra-precision machines. Requires stable temperature (±0.1°C) and air refractivity compensation.

### 5-Axis Machining

Simultaneous control of five axes (typically X, Y, Z linear + two rotary axes) enables:

- **Complex 3D contours**: Impellers, turbine blades, mold cavities — impossible on 3-axis machines without multiple setups.
- **Reduced setups**: Parts requiring 5-10 setups on a 3-axis machine can be done in 1-2 setups on 5-axis. Each setup introduces alignment error (±5-20 μm per setup).
- **Better tool engagement**: Tool can be tilted to maintain optimal cutting conditions, improving surface finish and tool life.
- **Configurations**: Trunnion (rotary table + tilting rotary), swivel-head (tilting spindle + rotary table), and gantry (large 5-axis for aerospace).
- **Positioning accuracy for 5-axis**: ±3-10 μm linear, ±5-10 arc-seconds rotary on precision machines.

### G-Code Basics

CNC programs use G-code (ISO 6983 / RS274) to specify toolpath, feed rate, spindle speed, and auxiliary functions:

- **G00**: Rapid positioning (maximum speed, no cutting)
- **G01**: Linear interpolation at programmed feed rate
- **G02/G03**: Circular interpolation (clockwise/counterclockwise)
- **G04**: Dwell (pause for specified time)
- **G17/G18/G19**: Plane selection (XY, ZX, YZ)
- **G20/G21**: Inch/metric programming
- **G40/G41/G42**: Cutter compensation cancel/left/right
- **G43**: Tool length compensation
- **G54-G59**: Work coordinate system selection
- **G90/G91**: Absolute/incremental programming
- **M03/M04/M05**: Spindle start CW/CCW/stop
- **M06**: Tool change
- **M08/M09**: Coolant on/off
- **S-word**: Spindle speed (RPM)
- **F-word**: Feed rate (mm/min or mm/rev)

Example: milling a 50 mm square pocket at 1000 RPM, 200 mm/min feed:
```
G21 G90 G17
G54 G00 X0 Y0 Z10
M03 S1000
G00 X5 Y5
G01 Z-5 F50
G01 X45 F200
G01 Y45
G01 X5
G01 Y5
G00 Z10
M05 M09
M30
```

Modern CNC also supports conversational programming and CAM-generated toolpaths for complex geometry.

### CNC Precision Capabilities

| Parameter | Standard CNC | Precision CNC | Ultra-Precision CNC |
|-----------|-------------|---------------|---------------------|
| Positioning accuracy | ±5-10 μm | ±1-3 μm | ±0.1-0.5 μm |
| Repeatability | ±3-5 μm | ±0.5-1 μm | ±0.05-0.1 μm |
| Surface finish (turning) | 0.8-3 μm Ra | 0.2-0.8 μm Ra | 0.01-0.1 μm Ra |
| Surface finish (milling) | 0.8-6 μm Ra | 0.4-1.6 μm Ra | 0.05-0.4 μm Ra |
| Thermal stability | ±10-20 μm/°C | ±1-5 μm/°C | ±0.1-0.5 μm/°C |
| Machine cost indicator | 1× | 5-20× | 100-1000× |

Ultra-precision CNC machines (e.g., Moore Nanotech, Precitech) use air bearings, granite bases, oil shower temperature control (±0.01°C), and diamond tools to achieve nanometer-level surface finish.

## Precision Grinding for Semiconductor Equipment

[Machining](./machining.md) covers basic surface and cylindrical grinding to ±0.005 mm. Semiconductor equipment requires grinding processes that push a full order of magnitude further — into the sub-micron regime for flatness, parallelism, and surface finish.

### Jig Grinding

Jig grinding uses a precision grinding spindle mounted on a CNC-controlled X-Y table to grind holes, profiles, and contours to extreme accuracy:

- **Hole accuracy**: ±1-3 μm on diameter. Roundness: 0.5-2 μm.
- **Surface finish**: 0.05-0.4 μm Ra.
- **Spindle speed**: 20,000-175,000 RPM (air-bearing spindles for highest precision).
- **Application**: Die guide pin holes, punch bushings, precision lens molding die bores, semiconductor fixture alignment holes.

### Surface Grinding (Precision Grade)

Beyond the basic surface grinding covered in [Machining](./machining.md), precision surface grinding achieves:

- **Flatness**: 0.5-2 μm over 300 mm × 300 mm (vs. 5 μm in standard grinding).
- **Parallelism**: 0.5-3 μm between faces.
- **Surface finish**: 0.05-0.4 μm Ra with fine-grit wheel and spark-out passes.
- **Machine requirements**: Hydrostatic guideways (oil film bearing, zero stick-slip), automatic wheel dressing, temperature-controlled coolant (±0.5°C), vibration-isolated foundation.
- **Spark-out**: Final 5-10 passes with zero downfeed allow the wheel to "spark out" — removing the last microns of material as the system relaxes elastically. Essential for achieving sub-micron flatness.
- **Wheel selection for precision**: Fine-grit wheels (320-800 grit, 60-120 μm abrasive size) for finish grinding. Very fine grit (1000+ grit, <20 μm) for mirror finish.

### Cylindrical Grinding (Precision Grade)

Precision cylindrical grinding for shafts, spindles, and bearing journals used in semiconductor equipment:

- **Roundness**: 0.1-0.5 μm (vs. 1-3 μm standard).
- **Cylindricity**: 0.5-2 μm over 500 mm length.
- **Surface finish**: 0.02-0.2 μm Ra.
- **Work speed**: 5-15 m/min (slower than standard for better finish).
- **Infeed**: 0.5-2 μm per pass for finishing.
- **Application**: Air-bearing spindles, wafer stage guide shafts, precision lead screws, lens polishing machine spindles.

### Centerless Grinding

Workpiece is supported between a grinding wheel and a regulating wheel (no centers or chuck). Enables high-throughput grinding of cylindrical parts:

- **Diameter tolerance**: ±2-5 μm (precision setup).
- **Roundness**: 0.5-2 μm.
- **Surface finish**: 0.1-0.4 μm Ra.
- **Throughfeed rate**: 1-10 m/min for small parts. Can process hundreds of parts per hour continuously.
- **Application**: Bearing rollers, guide pins, piston pins, stylus shafts, probe needles.

### Grinding Wheel Selection

Wheel specification follows the standard marking system: **abrasive type – grit size – grade – bond type – structure**.

| Abrasive | Hardness (Mohs) | Application | Typical Workpiece Material |
|----------|----------------|-------------|---------------------------|
| Aluminum oxide (Al₂O₃) | 9 | General-purpose steel grinding | Carbon steel, tool steel, alloy steel |
| Silicon carbide (SiC) | 9.5 | Low-tensile materials, non-ferrous | Cast iron, aluminum, brass, ceramics, glass |
| Diamond (synthetic) | 10 | Hard/brittle materials | Tungsten carbide, ceramics, glass, silicon, PCD |
| Cubic boron nitride (CBN) | 9.5+ | Hardened steels, superalloys | Hardened tool steel (60+ HRC), Inconel, titanium |

**Grit size selection**:
- Roughing: 24-60 grit (250-800 μm) — fast removal, 3-10 μm Ra finish
- General: 60-120 grit (125-250 μm) — balance of speed and finish, 0.8-3 μm Ra
- Finishing: 120-320 grit (40-125 μm) — good finish, 0.2-1 μm Ra
- Precision: 320-800 grit (15-40 μm) — fine finish, 0.05-0.4 μm Ra
- Mirror: 800-2000 grit (1-15 μm) — mirror finish, 0.01-0.1 μm Ra

**Bond types**:
- **Vitrified (V)**: Glass-like bond. Porous, friable, good coolant delivery. Most common for precision grinding. Truing and dressing with diamond tools.
- **Resinoid (B)**: Synthetic resin bond. Good shock absorption, high speed capability. Used for roughing and cut-off.
- **Metal (M)**: Metal matrix (bronze, steel). Extremely durable. Used for diamond/CBN superabrasive wheels. Requires special truing with silicon carbide dressing sticks or EDM truing.
- **Electroplated**: Single layer of abrasive grains bonded to steel hub by nickel plating. Aggressive cutting, no dressing required. Good for form grinding. Limited life (single abrasive layer).

**Wheel speed**: 25-35 m/s for conventional abrasives. 45-120 m/s for CBN/diamond superabrasive wheels. Higher speed = more cutting events per second = better finish, but requires stronger wheel bonds and machine guarding.

### Coolant and Thermal Management

Precision grinding generates substantial heat in a very small zone (1,000-2,000°C at the grain-workpiece interface). Thermal management is critical:

- **Coolant flow**: 20-80 liters/min through nozzle directed at the grinding zone. Insufficient flow causes thermal damage (burn marks, tensile residual stress, metallurgical changes).
- **Coolant type**: Soluble oil emulsion (2-5% concentration) for most work. Synthetic coolant for highest finish. Water-based coolant filtered to 1-5 μm to prevent scratching.
- **Temperature control**: ±0.5°C for precision grinding. ±0.1°C for ultra-precision. Machine structure and workpiece must reach thermal equilibrium — warm-up period of 30-120 minutes.
- **Nozzle design**: Shoe-type nozzle matching wheel profile delivers coolant into the grinding zone at 70-90% of wheel speed. Prevents air barrier from deflecting coolant.

### Surface Finish Specifications

| Process | Ra (μm) | Rz (μm) | Application |
|---------|---------|---------|-------------|
| Rough grinding | 3.2-6.3 | 16-32 | Bulk material removal |
| Finish grinding | 0.8-3.2 | 4-16 | General precision parts |
| Fine grinding | 0.2-0.8 | 1-4 | Bearing surfaces, seal faces |
| Precision grinding | 0.05-0.2 | 0.4-1 | Wafer stage surfaces, lens molds |
| Mirror grinding | 0.01-0.05 | 0.1-0.4 | Optical surfaces, gauge faces |
| Lapping/honing | 0.005-0.025 | 0.05-0.25 | Reference surfaces, cylinder bores |

Ra = arithmetic average roughness. Rz = average maximum peak-to-valley height (≈ 4-6× Ra for grinding).

## Semiconductor Equipment Applications

### Wafer Stage Manufacturing

The wafer stage holds and positions silicon wafers during photolithography exposure. It is the most mechanically demanding single component in semiconductor manufacturing:

- **Flatness requirement**: <0.5 μm over 300 mm (for 300 mm wafers). This requires precision surface grinding followed by lapping and polishing.
- **Positioning accuracy**: ±0.01 μm (10 nm) with linear motor drives and interferometer feedback. The stage slides on air bearings with 0.01 μm straightness.
- **Materials**: Low-expansion materials (granite, ceramics, Invar) to minimize thermal drift. Aluminum for lightweight stages with thermal management.
- **Manufacturing sequence**: Rough machine → stress relief anneal → semi-finish grind → precision surface grind → lap → polish. Multiple intermediate measurement steps with laser interferometry.

### Lens and Optic Molding

Precision glass molding for camera lenses, projector optics, and photolithography lens elements:

- **Mold cavity accuracy**: ±0.5-2 μm form error. Mold surface finish: <0.01 μm Ra (mirror polish).
- **Mold material**: Tungsten carbide or silicon carbide (maintains shape at 500-700°C molding temperature). Mold life: 5,000-50,000 parts before refurbishment.
- **Manufacturing**: CNC machining of mold blank → precision grinding to near-net shape → ultra-precision CNC grinding to ±1 μm → magnetorheological finishing (MRF) or ion beam figuring for final figure correction.

### IC Package Mold Making

Transfer molds for encapsulating integrated circuits in epoxy-silica compound:

- **Cavity dimensional accuracy**: ±2-5 μm on critical dimensions (leadframe pocket depth, wire bonding shelf position).
- **Cavity count**: 100-500+ cavities per mold, all identical within ±2 μm.
- **Surface finish**: 0.1-0.4 μm Ra on cavity walls (for clean part ejection). Polished to <0.05 μm Ra on visible surfaces.
- **Manufacturing**: CNC milling (roughing) → CNC precision milling (semi-finish) → sinker EDM (cavity details) → wire EDM (split lines) → precision grinding (flat mating surfaces) → hand polishing.
- **Mold material**: Hardened tool steel (H13, S136) at 48-54 HRC. Must withstand 175-200°C molding temperature and 10-70 MPa transfer pressure for millions of cycles.

## Precision Achievement Hierarchy

The achievable precision depends on the complete system — machine, tooling, environment, measurement, and process:

| Level | Flatness | Positioning | Surface Finish | Key Enablers |
|-------|----------|-------------|----------------|--------------|
| Conventional | ±10-50 μm | ±50-100 μm | 1-10 μm Ra | Manual machine, standard grinding |
| Precision | ±1-5 μm | ±1-5 μm | 0.1-1 μm Ra | CNC, precision grinding, temperature control |
| High precision | ±0.1-1 μm | ±0.1-1 μm | 0.01-0.1 μm Ra | Precision CNC, air bearings, clean environment |
| Ultra-precision | ±0.01-0.1 μm | ±0.01-0.1 μm | 0.001-0.01 μm Ra | Diamond turning, vibration isolation, ±0.01°C control |

Each level requires roughly 10× the investment in machine capability, environmental control, and metrology infrastructure compared to the previous level.

## Safety

- **EDM fire hazard**: Oil-based dielectric can ignite at high power settings. Fire suppression systems mandatory. Never leave sinker EDM unattended during roughing operations.
- **EDM electrical hazard**: 60-300 V at 5-200 A is lethal. Interlocks on machine enclosure. Ground-fault protection required.
- **CNC rotating hazards**: Automatic operation means no operator control of spindle/axis motion. Enclosure doors with safety interlocks. Never reach into work area during program execution.
- **Grinding wheel safety**: Same as [Machining](./machining.md) safety — ring test, guards, speed limits. Precision grinding's higher wheel speeds (up to 120 m/s for CBN) require correspondingly stronger guards.
- **Grinding dust**: Fine metallic dust is a respiratory hazard and explosion risk. Dust collection mandatory. Coolant mist from high-speed grinding requires extraction.
- **Noise**: Grinding and EDM generate 80-100+ dB. Hearing protection required.

## References

- Basic machining operations: [Machining](./machining.md)
- Cutting tool materials and abrasives: [Bearings & Abrasives](./bearings-abrasives.md)
- Machine construction sequence: [Iterative Bootstrap](./iterative-bootstrap.md)
- Electricity supply: [Electricity Generation & Distribution](../energy/electricity.md)
- Precision measurement: [Precision Metrology](../measurement/precision-metrology.md)
- Lubrication: [Lubricants](../chemistry/lubricants.md)
- Silicon crystal growth (requires precision equipment): [Crystal Growth](../silicon/crystal-growth.md)

### See Also

- [Machining](machining.md) — Conventional machining operations (lathe, mill, drill, basic grinding)
- [Bearings & Abrasives](bearings-abrasives.md) — Abrasive materials and bearing manufacturing
- [Iterative Bootstrap](./iterative-bootstrap.md) — Precision improvement pathway
- [Machine Tools Overview](./index.md) — Complete machine tools reference

---

*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*
