# Nanometer Positioning

> **Node ID**: precision-motion.nanometer-positioning
> **Domain**: Precision Motion Control
> **Timeline**: Years 35-55
> **Outputs**: nano_positioning_stages, air_bearing_slides, linear_motor_drives
> **Dependencies**: None (root capability)
> **Enables**: None (leaf capability)

The [EDM, CNC & Precision Grinding](../machine-tools/edm-cnc.md) domain achieves ±0.5 μm positioning on ultra-precision CNC machines. Semiconductor lithography demands three orders of magnitude better: wafer stages must position to ±5 nm over 300 mm travel, reticle stages to ±2 nm, and inspection stages to ±1 nm. This document covers the actuation technologies — piezoelectric stages, air bearings, and linear motors — that make nanometer positioning possible. For the measurement systems providing position feedback, see [Precision Encoders](./precision-encoders.md); for the vibration environment that nanometer positioning requires, see [Vibration Isolation](./vibration-isolation.md).

## Piezoelectric Positioning Stages

Piezoelectric actuators convert electrical voltage directly to mechanical displacement via the inverse piezoelectric effect in ferroelectric ceramics (lead zirconate titanate, PZT). No gears, no bearings, no friction — the crystal lattice itself deforms, providing essentially infinite positioning resolution limited only by drive electronics noise.

### Stack Actuators

Multiple thin PZT ceramic discs (0.1-1 mm thick) are mechanically stacked in series and electrically connected in parallel. Each disc expands ~0.1% of its thickness at maximum field strength (2 kV/mm).

- **Displacement**: 5-200 μm stroke depending on stack length. Typical: 30 μm for a 30 mm long stack.
- **Resolution**: Theoretically unlimited — determined by noise floor of drive voltage. Practical resolution: 0.01-0.1 nm with low-noise amplifiers (24-bit DAC at 150V range = 0.009 nm/bit).
- **Stiffness**: 50-500 N/μm. Extremely rigid — the stage acts as a stiff spring.
- **Resonant frequency**: 10-100 kHz for unstaged actuators. Very fast response — settling time < 1 ms for small steps.
- **Force generation**: 1-50 kN blocking force. Can push against substantial loads.
- **Hysteresis**: ±10-15% open-loop due to ferroelectric domain switching. This is the primary nonlinearity — closed-loop operation with strain gauge or capacitive sensor feedback is mandatory for repeatable positioning.
- **Creep**: After a voltage step, the actuator continues to creep ~1-5% over the first 10 minutes logarithmically. Closed-loop feedback compensates automatically.

### Flexure-Guided Stages

Stack actuators provide only raw expansion. To create useful XY or XYZ motion, the actuator is mounted in a flexure guide — a monolithic metal or silicon structure with carefully designed flexure hinges that constrain motion to the desired axis.

- **Flexure hinge design**: Notch-type or leaf-spring flexures machined into a single block of aluminum, steel, or invar. The flexure bends elastically; no sliding or rolling contact means zero friction, zero wear, zero stiction.
- **Travel range**: 50-800 μm per axis (limited by flexure stress and actuator stroke). Larger ranges require amplification mechanisms, trading force for displacement.
- **Parasitic motion**: Well-designed flexures limit off-axis error to < 10 μrad pitch/yaw over full travel.
- **Resonant frequency**: 200-2000 Hz for complete stages (lower than bare actuator due to flexure compliance and moving mass).

### Long-Travel Piezo Stages (Piezo-Walk / Piezo-Stepping)

Conventional piezo stacks are limited to ~200 μm travel. For millimeter-to-centimeter travel with nanometer precision, two approaches extend the range:

**Inertial stick-slip drives**: A piezo actuator slowly extends (carrying the payload with it via friction), then rapidly retracts — the inertia of the payload overcomes friction and the payload stays in place while the actuator slips back. Repeat at 1-20 kHz for continuous motion.

- **Step size**: 5-1000 nm per step (adjustable via drive voltage).
- **Speed**: 0.1-10 mm/s depending on frequency and step size.
- **Positioning resolution**: 1-5 nm (single step resolution).
- **Force**: 1-50 N (limited by friction interface).
- **Applications**: Microscope objective focusing, fiber optic alignment, vacuum-compatible positioning.

**Piezo-walk drives**: Multiple piezo legs alternate between clamping and extending, walking the stage along a guide rail — like an inchworm but with multiple legs.

- **Travel range**: Up to 50 mm (limited by guide rail length).
- **Resolution**: 0.1-1 nm in closed loop.
- **Speed**: 0.5-5 mm/s continuous, 10 mm/s burst.
- **Holding force**: 5-20 N when powered off (mechanical clamp).
- **Applications**: Semiconductor inspection stages, electron microscope sample positioning.

## Air Bearing Slides

Air bearings support the moving stage on a thin film (3-10 μm) of pressurized air (3-6 bar), eliminating mechanical contact between moving and stationary parts. Zero friction, zero wear, zero stiction, and sub-nanometer smoothness of motion.

### Aerostatic Flat Pad Bearings

Air is fed through a pattern of small orifices (0.1-0.3 mm diameter) or porous restrictors in a flat pad, creating a pressurized air film between the pad and the guide surface.

- **Load capacity**: 5-50 N/cm² bearing area. A 100 mm × 100 mm pad carries 500-5000 N.
- **Stiffness**: 10-200 N/μm depending on supply pressure, bearing area, and gap.
- **Gap (fly height)**: 3-10 μm. Determined by balance of supply pressure and load.
- **Straightness of travel**: 0.01-0.1 μm over 300 mm (limited by guide surface flatness). The air film averages out surface irregularities smaller than the bearing pad.
- **Pitch/yaw error**: 0.1-1 arc-second over 300 mm.
- **Air consumption**: 5-30 liters/min per bearing pad at 4 bar supply. Requires clean, dry, oil-free air (1 μm filtration minimum).

### Aerostatic Spindle Bearings

For rotary motion (e.g., wafer rotation during exposure), air-bearing spindles provide:

- **Radial runout**: 0.01-0.05 μm — two orders of magnitude better than precision ball bearings.
- **Axial runout**: 0.02-0.1 μm.
- **Speed**: 500-10,000 RPM depending on diameter and application.
- **Stiffness**: 50-500 N/μm radial.
- **Application**: Wafer rotation stages (300 mm wafers at 1000-3000 RPM in scanners), lens element rotation during polishing, precision rotary indexing.

### Guide Surface Requirements

The guide surface (the rail or flat that the air bearing rides on) directly determines motion accuracy:

- **Flatness**: Must be ≤ 0.1 μm over the full travel for nanometer positioning. Achieved by precision surface grinding followed by lapping (see [EDM, CNC & Precision Grinding](../machine-tools/edm-cnc.md)).
- **Material**: Granite (low thermal expansion, excellent damping, naturally flat when polished), ceramics (alumina, silicon carbide), or hardened steel with wear-resistant coating.
- **Surface finish**: ≤ 0.05 μm Ra. Scratches or imperfections create localized pressure variations in the air film.
- **Thermal stability**: ±0.1°C control needed to maintain sub-micron straightness over long travel. Granite's low thermal expansion coefficient (4-8 × 10⁻⁶/°C) helps but does not eliminate the requirement.

### Orifice vs. Porous Restrictors

The air supply restriction method affects bearing performance:

| Property | Orifice Restrictor | Porous Restrictor |
|----------|--------------------|-------------------|
| Material | Drilled holes in metal pad | Sintered bronze or carbon-graphite pad |
| Air distribution | Point sources → higher pressure between orifices | Uniform across entire surface |
| Stiffness | Good | Higher (more uniform pressure) |
| Damping | Lower | Higher (air flows through porous medium) |
| Crash tolerance | Orifices can be damaged if contact occurs | More tolerant — porous material provides some dry lubrication |
| Cost | Lower | Higher |
| Typical application | General-purpose stages | Ultra-precision spindles, wafer stages |

## Linear Motor Drives

Ball screws and lead screws (covered in [EDM, CNC & Precision Grinding](../machine-tools/edm-cnc.md)) convert rotary motor motion to linear motion with excellent precision. However, they introduce mechanical compliance, backlash (even when preloaded), friction, and wear. Linear motors eliminate all mechanical transmission — the electromagnetic force acts directly on the stage.

### Iron-Core Linear Motors

Copper windings embedded in a laminated iron core interact with permanent magnets on the stationary rail. Maximum force and efficiency, but with cogging.

- **Force**: 100-20,000 N continuous. Peak force 2-3× continuous for acceleration bursts.
- **Cogging**: Interaction between iron teeth and magnets creates force ripple of 1-5% of rated force. Detrimental to smoothness at low speed. Reduced by skewing magnets or optimized tooth geometry.
- **Thermal load**: Motor coils heat the stage. Water cooling required for high-force applications. Stage temperature rise must be managed to prevent thermal expansion errors.
- **Mass of moving part**: Iron core adds mass. Higher moving mass reduces acceleration and increases settling time.
- **Application**: High-force axes in machine tools, large wafer stage coarse positioning.

### Ironless (U-Channel) Linear Motors

Copper windings in a non-magnetic (epoxy-potted) coil assembly sit between two rows of permanent magnets in a U-shaped rail. No iron in the coil — zero cogging, minimum force ripple.

- **Force**: 10-2,000 N continuous. Lower than iron-core due to lack of iron flux focusing.
- **Cogging**: Zero — no iron teeth to interact with magnets.
- **Force ripple**: < 0.5% of rated force. Extremely smooth motion.
- **Moving mass**: Coil assembly is lightweight (epoxy + copper, no iron). Enables high acceleration.
- **Thermal isolation**: Coil can be thermally isolated from the stage via ceramic or composite spacers, minimizing thermal coupling.
- **Application**: Wafer stage fine positioning, reticle stages, inspection stages — any application requiring smooth, high-acceleration motion.

### Linear Motor Specifications for Semiconductor Equipment

| Parameter | Wafer Stage (Coarse) | Wafer Stage (Fine) | Reticle Stage |
|-----------|---------------------|-------------------|---------------|
| Travel range | 300-600 mm | 5-20 mm | 200-300 mm |
| Motor type | Iron-core | Ironless voice coil | Ironless |
| Continuous force | 2,000-5,000 N | 50-200 N | 500-1,500 N |
| Peak force | 10,000-20,000 N | 500-1,000 N | 3,000-6,000 N |
| Moving mass | 30-80 kg | 2-5 kg | 15-30 kg |
| Max acceleration | 20-30 m/s² (2-3g) | 100-500 m/s² (10-50g) | 30-80 m/s² (3-8g) |
| Max velocity | 1-2 m/s | 0.5-1 m/s | 1-3 m/s |
| Positioning accuracy | ±50 nm | ±5 nm | ±5 nm |

The coarse-fine architecture splits the positioning problem: the coarse iron-core motor provides long travel and high force for step-and-scan motions, while the fine voice-coil or piezo stage provides nanometer-resolution corrections over a short range.

## Voice Coil Actuators

A voice coil actuator is a single-phase linear motor: a coil in a permanent magnetic field. Like a loudspeaker voice coil but designed for precision positioning rather than sound reproduction.

- **Force**: Proportional to current: F = B × L × I (B = magnetic field, L = wire length, I = current). Extremely linear response.
- **Stroke**: 1-50 mm. Limited by coil length and magnetic field uniformity.
- **Bandwidth**: 200-2000 Hz. Very fast response for disturbance rejection.
- **Force range**: 1-500 N continuous.
- **Hysteresis**: Essentially zero — no magnetic hysteresis at typical operating fields.
- **Application**: Fine positioning stage overlay, focus adjustment in lithography lenses, AFM tip positioning.

## Magnetic Bearings

For rotary axes where air bearings cannot provide sufficient stiffness or where vacuum compatibility is required, active magnetic bearings suspend the rotor without physical contact using electromagnetic attraction:

- **Radial runout**: 0.05-0.5 μm (inferior to air bearings but usable).
- **Stiffness**: 500-5,000 N/μm active (controlled by feedback loop gain).
- **Speed**: Up to 100,000 RPM possible (limited by rotor material strength, no mechanical contact).
- **Active control**: Requires position sensors (eddy current or capacitive) and feedback controller running at 5-20 kHz update rate.
- **Power consumption**: 10-100 W per bearing axis for active control electronics.
- **Application**: High-speed vacuum-compatible spindles, turbomolecular pump rotors, flywheel energy storage.

## Stage Materials and Thermal Management

Nanometer positioning is extremely sensitive to thermal expansion. A 300 mm granite stage with α = 6 × 10⁻⁶/°C expands 1.8 μm per °C — 180× the 10 nm positioning budget. Thermal management is therefore as critical as mechanical design.

### Material Selection

| Material | CTE (×10⁻⁶/°C) | Stiffness (GPa) | Density (g/cm³) | Application |
|----------|-----------------|-----------------|------------------|-------------|
| Granite | 4-8 | 30-70 | 2.6-2.8 | Machine base, guide surfaces |
| Invar (Fe-36Ni) | 0.6-1.2 | 140 | 8.0 | Stage components, metrology frames |
| Zerodur (glass-ceramic) | 0.0-0.1 | 90 | 2.5 | Mirror substrates, reference surfaces |
| Silicon carbide (SiC) | 2.2-4.0 | 390-410 | 3.1 | Lightweight stiff stages |
| Aluminum | 22-24 | 70 | 2.7 | Actively cooled stages (high CTE compensated by cooling) |
| Carbon fiber composite | -1 to +8 (tailorable) | 100-400 | 1.5-2.0 | Lightweight stage structures |

### Thermal Control Strategies

1. **Material selection**: Low-CTE materials (Invar, Zerodur) minimize dimensional change per degree.
2. **Active liquid cooling**: Temperature-controlled water (±0.01°C) circulated through channels in the stage structure. Removes motor heat and environmental drift.
3. **Metrology frame**: A separate reference frame (Invar or Zerodur) carries the position-measuring interferometers, isolated from the stage's thermal expansion. The stage may expand, but the interferometer measures position relative to the stable metrology frame.
4. **Thermal shielding**: Enclosures with active temperature control (±0.05°C) surround the stage. Forced-air circulation minimizes gradients.
5. **Warm-up protocol**: Equipment must run for 30-120 minutes to reach thermal equilibrium before nanometer-precision work begins.

## Control System Architecture

Nanometer positioning requires multi-layer feedback control:

### PID Control Loop

The fundamental feedback loop compares commanded position to measured position (from encoders or interferometers):

- **Proportional gain**: Corrects position error proportional to its magnitude. High gain → fast response but risk of oscillation.
- **Integral gain**: Elimuates steady-state error. Required for zero tracking error under constant velocity.
- **Derivative gain**: Damps oscillation by responding to rate of error change.
- **Typical bandwidth**: 200-1000 Hz for the primary position loop.

### Feedforward Compensation

Feedback alone cannot track fast motion with nanometer error. Feedforward adds predicted control signals:

- **Velocity feedforward**: Adds a control signal proportional to commanded velocity (derived from trajectory planner). Compensates for damping losses in the system.
- **Acceleration feedforward**: Adds signal proportional to commanded acceleration. Compensates for system inertia.
- **Friction feedforward**: For systems with any friction (even small), adds compensation based on velocity direction.
- **Result**: With good feedforward, tracking error drops from hundreds of nanometers to <10 nm during constant-velocity scanning.

### Notch Filters and Disturbance Observers

Mechanical resonances in the stage structure limit the achievable feedback bandwidth:

- **Notch filters**: Attenuate specific resonance frequencies (identified during system commissioning) to prevent the controller from exciting them.
- **Disturbance observer**: Estimates external disturbances (cable forces, vibration, thermal drift) from the difference between predicted and actual behavior, then compensates in real-time.
- **Iterative learning control**: For repetitive motions (step-and-scan), the controller learns from previous cycles to improve tracking accuracy on subsequent cycles.

## Safety

- **Crash protection**: Air bearings offer no resistance to crash — if air supply fails, the stage drops onto the guide surface. Mechanical crash stops with dampers required. Air pressure monitoring with automatic shutdown.
- **Magnetic field safety**: Linear motors and voice coils produce strong magnetic fields. Keep ferromagnetic objects, pacemakers, and magnetic storage media at safe distance (>0.5 m).
- **Pinch points**: High-acceleration stages can close gaps in milliseconds. Physical guards and safety interlocks on stage enclosures. Light curtains for operator protection.
- **High voltage**: Piezo amplifiers produce 0-150V or 0-1000V at high frequency. Proper insulation and grounding required. Never disconnect piezo cables while amplifier is powered — the inductive kick can be dangerous.
- **Cleanroom compatibility**: Air bearings exhaust air into the environment. In cleanroom applications, the exhaust must be filtered. Linear motor heat may require water cooling to maintain cleanroom temperature specs.

## References

- Precision machining of stage components: [EDM, CNC & Precision Grinding](../machine-tools/edm-cnc.md)
- Precision measurement for calibration: [Precision Metrology](../measurement/precision-metrology.md)
- Encoders providing position feedback: [Precision Encoders & Feedback](./precision-encoders.md)
- Vibration isolation for stage environment: [Vibration Isolation](./vibration-isolation.md)
- Wafer stage applications: [Wafer Stages & Scanner Systems](./wafer-stages.md)
- Electricity supply for motors and controllers: [Electricity Generation & Distribution](../energy/electricity.md)

### See Also

- [Machine Tools Overview](../machine-tools/index.md) — Conventional precision manufacturing
- [Measurement & Instrumentation](../measurement/index.md) — Metrology foundations
- [Optics](../optics/index.md) — Optical components used in encoder systems
- [Precision Motion Control](./index.md) — Domain overview

---

*Part of the [Bootciv Tech Tree](../index.md) • [Precision Motion Control](./index.md) • [All Domains](../index.md)*
