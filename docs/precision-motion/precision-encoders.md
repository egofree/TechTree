# Precision Encoders & Feedback

> **Node ID**: precision-motion.precision-encoders
> **Domain**: [Precision Motion Control](./index.md)
> **Enables**: None
> **Timeline**: Years 35-55
> **Outputs**: laser_interferometers, optical_encoders, encoder_feedback_systems
> **Dependencies**: [`measurement.precision-metrology`](../measurement/precision-metrology.md),
> `optics`
> **Critical**: Yes — sub-nanometer position feedback is required for photolithography wafer stages

Nanometer positioning stages (see [Nanometer Positioning](./nanometer-positioning.md)) are only as accurate as their position feedback. A piezo stage may have 0.01 nm actuator resolution, but if the position sensor measures to only 10 nm, the effective positioning accuracy is 10 nm. This document covers the encoder and interferometer technologies that close the feedback loop for nanometer-precision motion: optical scale encoders, laser interferometers, and the signal processing that extracts sub-nanometer position from optical measurements.

## Prerequisites

- [Nanometer Positioning](nanometer-positioning.md) — the actuation systems these encoders serve
- [Optics](../optics/index.md) — optical components and laser sources
- [Precision Metrology](../measurement/precision-metrology.md) — measurement foundations

## Implementation Steps

1. **Determine resolution and accuracy requirements**: Match encoder specifications to the application using the Encoder Selection Guidelines table. Wafer scanners require interferometric measurement; CNC machines use optical encoders
2. **Select encoder type**: Choose between optical linear encoders (high resolution, non-contact) and laser interferometers (highest accuracy, traceable to wavelength of light). Use capacitive sensors for sub-mm range ultra-high resolution
3. **Specify scale and mounting**: Select scale substrate (Zerodur for highest accuracy, steel tape for long travel). Ensure thermal expansion matching between scale and machine structure
4. **Design signal processing**: Specify interpolation electronics (4,096× for 5 nm resolution with 20 μm pitch), LUT correction for sub-divisional error, and communication protocol (BiSS for lowest latency)
5. **Install and align**: Mount scale with adhesive or clamping. Align read head at 0.3-1.0 mm gap. For interferometers, align beam to <0.1 mrad parallelism with motion axis
6. **Compensate for environmental effects**: Install temperature, pressure, and humidity sensors for refractive index compensation (Edlén equation). For highest accuracy, enclose interferometer beam path in vacuum
7. **Calibrate and verify**: Measure systematic errors (SDE for encoders, cosine/Abbe error for interferometers). Build correction lookup table. Verify total measurement uncertainty against specification

## Optical Linear Encoders

Optical encoders measure linear displacement by detecting the passage of a precision grating pattern. A light source illuminates a graduated scale; photodetectors read the resulting interference pattern.

**Strengths**:
- High resolution: down to 0.24 nm with 4 μm pitch + 16,384× interpolation
- Repeatability ±0.02-0.1 μm — significantly better than absolute accuracy
- Non-contact measurement: read head never touches the scale

**Weaknesses**:
- Sub-divisional error (SDE): ±5-50 nm periodic error within one signal period
- Sensitive to contamination: a fingerprint on the scale causes signal dropout
- Maximum speed limited by signal processing bandwidth: 5-20 m/s

## Incremental Encoders

The most common encoder type for precision motion. A glass or steel scale carries a precise grating (typically 20 μm or 4 μm pitch). An index grating in the read head creates a Moiré interference pattern that cycles through light and dark as the read head moves relative to the scale.

- **Scale pitch**: 20 μm (standard), 4 μm (high-resolution), down to 0.5 μm (ultra-high-resolution with holographic gratings).
- **Signal period**: One full sinusoidal cycle per scale pitch. The read head produces two 90° phase-shifted sinusoidal signals (A and B channels) for bidirectional counting.
- **Interpolation**: Electronic interpolation subdivides each signal period. With 20 μm pitch and 4,096× interpolation: 0.005 μm (5 nm) digital resolution. With 4 μm pitch and 16,384× interpolation: 0.00024 μm (0.24 nm) digital resolution.
- **Accuracy (systematic)**: ±0.1-5 μm over 1 m travel depending on scale quality. The best precision scales use holographic gratings on zero-expansion glass substrates for ±0.1 μm accuracy over 1 m.
- **Repeatability**: ±0.02-0.1 μm — significantly better than absolute accuracy.
- **Maximum speed**: 5-20 m/s. Signal processing bandwidth limits the maximum speed at which interpolation works correctly.

## Scale Materials and Mounting

| Scale Type | Substrate | CTE (×10⁻⁶/°C) | Max Length | Application |
|------------|-----------|-----------------|-----------|-------------|
| Glass scale | Zerodur / glass-ceramic | 0.0-0.1 | 3 m | Highest accuracy, temperature-stable |
| Steel tape scale | Hardened steel | 10-12 | 30 m | Long travel, general industrial |
| Steel tape (low-expansion) | Invar-bonded steel | 0.5-1.0 | 5 m | Medium accuracy, long travel |

**Mounting considerations:**

- **Thermal expansion matching**: The scale's thermal expansion must match the machine structure, or compensation tables must be applied. A 1 m steel scale on a granite base: 12 μm differential expansion per °C — catastrophic at nanometer precision. Use glass-ceramic scales on granite or Invar structures.
- **Scale mounting**: Adhesive-bonded or clamped. Must not be stretched or compressed during mounting — forces distort the grating pitch.
- **Read head gap**: 0.3-1.0 mm air gap between read head and scale surface. Tolerant of small variations but must not contact the scale.

## Absolute Encoders

Incremental encoders lose position count if power is interrupted. Absolute encoders encode unique position in a multi-track code pattern:

- **Single-turn resolution**: 1-23 bits (0.04 μm at 23 bits over 1 m).
- **Serial communication**: BiSS, EnDat, or SSI protocols transmit position data. BiSS and EnDat support 10 MHz clock rates for low-latency position update.
- **Accuracy**: ±0.5-5 μm over full travel. Less accurate than incremental encoders for the finest work but provides power-up position without homing.
- **Application**: General CNC machines, axes where homing is inconvenient. Not typically used for the primary positioning axes of wafer stages (incremental interferometers preferred).

## Laser Interferometers

Laser interferometers measure displacement by counting interference fringes produced by a coherent laser beam. They provide the highest accuracy linear position measurement available, limited only by the wavelength of light and the stability of the optical path.

**Strengths**:
- Highest accuracy available: ±0.02-0.1 ppm of measured distance (±0.03-0.3 μm at 300 mm)
- Non-contact: measurement beam reflects off mirror on moving stage
- Traceable to fundamental physical constant (wavelength of light)

**Weaknesses**:
- Refractive index of air changes wavelength: requires continuous environmental compensation (temperature, pressure, humidity)
- Cosine error, Abbe error, and dead path error require careful alignment and multi-beam configurations
- Expensive: $50,000-200,000+ per multi-axis interferometer system

## Michelson Interferometer (Basic)

The fundamental configuration:

1. **Beam splitting**: A helium-neon (HeNe) laser emits a coherent beam at 632.8 nm wavelength. A beam splitter divides it into reference and measurement beams.
2. **Reference path**: One beam reflects off a stationary reference mirror and returns to the beam splitter.
3. **Measurement path**: The other beam reflects off a mirror attached to the moving stage and returns.
4. **Interference**: The two returning beams recombine at the beam splitter. Constructive or destructive interference depends on the path length difference.
5. **Counting fringes**: Each half-wavelength of stage motion (316.4 nm) produces one complete cycle of intensity variation at the photodetector.

- **Resolution**: 316.4 nm per fringe (basic counting). With electronic interpolation (typically 4-4,096×): 0.08 nm to 79 nm resolution.
- **Accuracy**: ±0.1-1 ppm of measured distance in controlled environment. At 300 mm: ±0.03-0.3 μm.
- **Non-contact**: The measurement beam reflects off a mirror on the stage — no physical contact between sensor and moving part.

## Heterodyne Interferometers

The standard for semiconductor lithography equipment. A Zeeman-split HeNe laser produces two closely-spaced frequencies (f1 and f2, separated by ~1.5-2 MHz) with orthogonal linear polarizations:

1. **Frequency f1** (measurement beam): Reflects off the stage mirror and returns Doppler-shifted by the stage velocity: f1 ± Δf.
2. **Frequency f2** (reference beam): Reflects off a fixed reference mirror at f2.
3. **Beat detection**: The detector measures the beat frequency difference. Stationary: f1 - f2 = 1.5 MHz. Moving: (f1 ± Δf) - f2 = 1.5 MHz ± Δf.
4. **Displacement calculation**: Δf is proportional to stage velocity (Doppler shift). Integrating velocity gives displacement.

**Advantages over homodyne:**
- **DC rejection**: The beat frequency is AC-coupled, rejecting intensity drift (laser power variation, detector aging, contamination).
- **Bidirectional sensing**: Phase of the beat signal relative to a reference indicates direction.
- **Multi-axis capability**: Different polarization or frequency encoding allows multiple axes from one laser source.

## Interferometer Accuracy Limitations

The vacuum wavelength of HeNe laser light is 632.8 nm. In air, the wavelength changes with refractive index:

**λ_air = λ_vacuum / n**

Where n (refractive index of air) depends on temperature, pressure, humidity, and gas composition:

| Factor | Effect on λ | Change per unit |
|--------|-------------|-----------------|
| Air temperature | λ increases | +0.96 ppm/°C |
| Air pressure | λ decreases | -0.27 ppm/hPa |
| Humidity | λ increases | +0.01 ppm/%RH |
| CO₂ concentration | λ decreases | -0.15 ppm/1000 ppm CO₂ |

**Compensation methods:**

1. **Air tracking compensator**: Temperature, pressure, and humidity sensors measure environmental conditions in real-time. The controller calculates refractive index correction using the Edlén equation and applies it to the interferometer reading.
2. **Wavelength tracker**: A separate reference interferometer measures the distance to a fixed mirror in the same air path. Any change in reading is due to refractive index change, providing direct compensation.
3. **Vacuum enclosure**: Enclose the interferometer beam path in a vacuum tube. Vacuum eliminates refractive index variation entirely. Used for the highest-precision applications.

**Remaining error sources:**

- **Cosine error**: If the interferometer beam is not perfectly parallel to the axis of motion, the measured distance is shorter than actual by a factor of cos(θ). At 1 mrad misalignment over 300 mm: 0.15 μm error. Alignment to < 0.1 mrad required.
- **Abbe error**: If the measurement beam is offset from the point of interest, angular error (pitch/yaw) causes measurement error = offset × sin(angle). At 100 mm offset and 10 μrad angular error: 1 μm. Multi-beam configurations measure and compensate.
- **Dead path error**: The non-changing portion of the beam path (between beam splitter and reference mirror) is sensitive to refractive index changes. Minimized by keeping dead path short (< 50 mm).
- **Target mirror flatness**: Mirror figure error directly adds to measurement error. Mirror flatness must be < λ/10 (63 nm) for standard precision, < λ/50 (12 nm) for nanometer-level work.

## Multi-Axis Interferometer Configurations

Wafer stages require simultaneous X, Y, and angular measurement:

**Plane mirror interferometer (PMI):** Measures displacement relative to a flat mirror. The beam makes double pass (incident + reflected) on the stage mirror, doubling sensitivity. One PMI measures one axis.

**Dual-beam angular measurement:** Two PMI beams separated by a known baseline (100-200 mm) both measure displacement on the same axis. The difference between readings gives angular error (pitch or yaw): θ = (d1 - d2) / baseline.

**Typical wafer stage interferometer configuration:**
- 3-4 X-axis beams (measuring X position and yaw)
- 2-3 Y-axis beams (measuring Y position and pitch)
- Total: 5-7 interferometer measurement channels per stage

## Interferometer Specifications for Semiconductor Equipment

| Parameter | Production Scanner | Research/Ultra-Precision |
|-----------|-------------------|--------------------------|
| Laser source | Zeeman-split HeNe | Stabilized HeNe or fiber laser |
| Wavelength | 632.991 nm (vacuum) | 632.991 nm or 1550 nm (fiber) |
| Resolution | 0.15-0.6 nm (with interpolation) | 0.02-0.15 nm |
| Accuracy (with compensation) | ±0.02-0.1 ppm | ±0.01-0.05 ppm |
| Maximum velocity | 2-5 m/s | 1-3 m/s |
| Measurement range | 0-1.5 m | 0-3 m |
| Update rate | 10-50 kHz | 50-200 kHz |
| Number of axes | 5-7 per stage | 3-12 per stage |

## Analog Interpolation

Raw encoder signals are sinusoidal. Extracting sub-period position requires precise interpolation:

- **Arctangent interpolation**: Position = (pitch / 2π) × arctan(A/B), where A and B are the quadrature signals. Requires accurate sinusoidal signals with equal amplitude, perfect 90° phase offset, and zero offset.
- **Signal quality**: Real encoder signals have amplitude mismatch (1-5%), phase error (90° ± 1-5°), and DC offset (0.5-5% of amplitude). These errors create interpolation errors (sub-divisional error, SDE).
- **Sub-divisional error (SDE)**: Periodic error within one signal period, typically ±5-50 nm for optical encoders. For nanometer positioning, SDE must be < ±2 nm. Achieved by careful signal conditioning and calibration.

## Digital Signal Processing

Modern encoder interfaces digitize the analog signals and apply real-time correction:

- **LUT correction**: A lookup table maps raw (A, B) values to corrected position, compensating for systematic signal imperfections measured during calibration.
- **Harmonic compensation**: SDE is decomposed into Fourier harmonics of the signal period. The dominant harmonics (1st, 2nd, 3rd, 4th) are corrected in real-time.
- **Noise filtering**: Anti-alias filters and digital smoothing reduce high-frequency noise. Careful filter design preserves phase margin in the servo loop.

## Latency and Phase Delay

Position feedback latency directly impacts servo performance:

- **Encoder processing latency**: 1-10 μs for interpolation and digital processing.
- **Communication latency**: 5-50 μs depending on protocol (BiSS: ~5 μs, EnDat: ~10 μs, analog: ~1 μs).
- **Total loop delay**: Encoder + communication + servo calculation + DAC output = 10-100 μs.
- **Impact**: At 500 Hz servo bandwidth, 50 μs delay introduces ~10° phase lag, reducing stability margin. Lower latency enables higher bandwidth → better disturbance rejection.

## Encoder Selection Guidelines

| Application | Encoder Type | Resolution | Accuracy | Update Rate |
|-------------|-------------|------------|----------|-------------|
| CNC machine tools | Optical linear, 20 μm pitch | 0.05-0.5 μm | ±1-5 μm/m | 1-5 kHz |
| Precision CNC | Optical linear, 4 μm pitch | 0.001-0.01 μm | ±0.1-1 μm/m | 5-20 kHz |
| Coordinate measuring machine | Optical linear + interferometer | 0.001 μm | ±0.1 μm/m | 10-20 kHz |
| Wafer stepper | Laser interferometer | 0.15-0.6 nm | ±0.05 ppm | 10-20 kHz |
| Wafer scanner | Laser interferometer | 0.15-0.6 nm | ±0.02 ppm | 20-50 kHz |
| Electron microscope stage | Optical linear, 4 μm pitch | 0.5-1 nm | ±0.1 μm | 5-10 kHz |
| AFM nanopositioning | Capacitive or interferometric | 0.01-0.1 nm | ±0.001 μm | 10-50 kHz |

## Capacitive Displacement Sensors

For short-range, ultra-high-resolution position measurement (alternative to encoders):

- **Principle**: Measures change in capacitance between a probe electrode and the target surface. Capacitance C = ε₀A/d, where d is the gap distance.
- **Range**: 0.05-2 mm. Very short range.
- **Resolution**: 0.01-0.1 nm — competitive with laser interferometers at short range.
- **Linearity**: ±0.05-0.5% of range after calibration.
- **Bandwidth**: 1-100 kHz — very fast response.
- **Application**: Fine stage Z-axis (focus), gap measurement, spindle runout monitoring, AFM feedback. Complementary to long-range encoders.

## Bearing Specifications for Precision Motion

The positioning accuracy of any stage is limited by its bearings. Bearings determine friction, stiffness, runout, and thermal stability. The choice of bearing type constrains what encoder resolution can actually be used.

### Bearing Type Comparison

| Bearing Type | Friction | Stiffness | Runout | Backlash | Speed | Load Capacity | Life | Application |
|-------------|----------|-----------|--------|----------|-------|--------------|------|-------------|
| Ball bearing (precision) | Low | Moderate | 0.5-2 μm | 1-5 μm | High | High | Long | CNC axes, general precision |
| Angular contact (paired) | Low | High | 0.2-1 μm | <1 μm (preloaded) | High | Moderate | Long | Machine tool spindles, rotary tables |
| Crossed roller | Very low | High | 0.1-0.5 μm | <0.5 μm (preloaded) | Moderate | Moderate | Long | CMMs, precision rotary stages |
| Air bearing | Zero (non-contact) | Moderate | 0.01-0.05 μm | Zero | Very high | Low | Unlimited | Wafer stages, spindles, CMMs |
| Hydrostatic (oil) | Near-zero | Very high | 0.01-0.1 μm | Zero | Moderate | Very high | Unlimited | Heavy precision grinding, large CMMs |
| Flexure | Zero | Low | <0.001 μm | Zero | Very low | Very low | Finite (fatigue) | Nanopositioning, AFM stages |
| Magnetic (active) | Zero | Adjustable | <0.01 μm | Zero | High | Moderate | Unlimited | Wafer scanners, vacuum stages |

### Air Bearing Specifications

Air bearings are the standard for semiconductor wafer stages because they eliminate friction, stiction, and wear. A thin film of pressurized air (typically 4-6 bar supply) separates the moving and stationary surfaces.

| Parameter | Typical Value | Notes |
|-----------|--------------|-------|
| Air gap | 3-10 μm | Determined by supply pressure, load, and orifice/porous design |
| Stiffness | 50-200 N/μm | Proportional to bearing area and supply pressure |
| Runout (axial) | 0.01-0.05 μm | Limited by surface flatness of the bearing faces |
| Runout (radial) | 0.02-0.1 μm | Limited by cylindrical form error |
| Pitch/yaw error | 0.1-1 arcsecond | Depends on bearing length and moment stiffness |
| Maximum speed | 30-100 m/s | Limited by air shear heating at extreme speeds |
| Supply air requirement | 4-6 bar, filtered to 0.1 μm, oil-free | Contaminated air destroys the bearing gap. Install coalescing filters and desiccant dryers. |
| Flatness requirement (guide surface) | < 0.5 μm over 300 mm | Air bearings replicate the guide surface errors — they do not average them out |

### Ball Screw Specifications (Linear Actuation)

Ball screws convert rotary motion from a servo motor into linear motion. The screw accuracy directly limits positioning accuracy for encoder-based systems.

| Parameter | Rolled Screw | Ground Screw (Precision) | Ground Screw (Ultra-Precision) |
|-----------|-------------|-------------------------|-------------------------------|
| Lead accuracy (over 300 mm) | ±50-100 μm | ±5-10 μm | ±1-3 μm |
| Lead accuracy (per 2π revolution) | ±5-10 μm | ±0.5-2 μm | ±0.1-0.5 μm |
| Backlash | 5-20 μm | 1-5 μm (preloaded: <1 μm) | <0.5 μm (double-nut preload) |
| Rigidity | 100-300 N/μm | 200-500 N/μm | 300-800 N/μm |
| Efficiency | 90-95% | 90-95% | 90-95% |
| Maximum speed | 1-3 m/s | 1-2 m/s | 0.5-1.5 m/s |
| Life at rated load | 10,000-50,000 km | 5,000-20,000 km | 5,000-10,000 km |

### Actuator Resolution and Positioning Accuracy

The relationship between actuator resolution, encoder resolution, and actual positioning accuracy. The system accuracy is always worse than any single component.

| Stage Type | Actuator | Actuator Resolution | Encoder Resolution | Actual Positioning Accuracy | Repeatability | Dominant Error Source |
|-----------|----------|--------------------|--------------------|-----------------------------|--------------|---------------------|
| Manual micrometer stage | Micrometer screw | 1 μm (0.5 μm with differential) | Graduations on drum | 2-5 μm | 1-2 μm | Screw lead error, thermal expansion |
| Stepper motor + ball screw | Stepper (200 steps/rev) + 5 mm/rev screw | 25 μm (full step), 1.56 μm (16× microstep) | Rotary encoder on motor | 5-25 μm | 3-10 μm | Microstep accuracy (~5% of full step), screw lead error |
| Servo motor + ball screw | AC servo + 5 mm/rev screw | Continuous (analog) | Linear encoder, 0.5 μm | 1-5 μm | 0.5-2 μm | Ball screw backlash, thermal growth |
| Piezo stack (direct drive) | PZT stack | 0.01 nm (command) | Capacitive sensor, 0.1 nm | 0.5-2 nm | 0.1-0.5 nm | Piezo hysteresis, creep, drift |
| Piezo flexure stage | PZT + flexure linkage | 0.001 nm (command) | Capacitive or interferometric, 0.01 nm | 0.1-1 nm | 0.01-0.1 nm | Flexure hysteresis, thermal drift |
| Voice coil + air bearing | Voice coil motor | Continuous | Interferometer, 0.15 nm | 10-50 nm | 5-20 nm | Air current disturbances, thermal drift |
| Linear motor + air bearing | Ironless linear motor | Continuous | Interferometer, 0.15 nm | 20-100 nm (over 300 mm) | 5-20 nm | Cosine error, Abbe error, thermal growth |
| Wafer scanner stage | Linear motor (dual) | Continuous | Heterodyne interferometer, 0.15 nm | 1-5 nm (over scan field) | 0.5-2 nm | Interferometer environmental compensation |

### Positioning Error Budget

For a wafer stage with 300 mm travel and nanometer target accuracy, the error budget allocates the total allowable error across all contributors:

| Error Source | Magnitude (nm, 3σ) | Mitigation |
|-------------|-------------------|------------|
| Encoder/interferometer measurement error | 5-15 | Multi-beam interferometer, environmental compensation |
| Abbe error (beam offset × angular error) | 5-20 | Multi-beam config measuring at the point of interest |
| Cosine error (beam misalignment) | 1-5 | Align to <0.05 mrad over full travel |
| Thermal expansion of stage structure | 10-50 | Granite or Invar structure, temperature control ±0.1°C |
| Bearing straightness error | 5-20 | Air bearings on lapped granite, active yaw correction |
| Vibration (floor transmitted) | 2-10 | Pneumatic isolation, active damping |
| Servo tracking error | 2-10 | High-bandwidth controller (500-2000 Hz), feedforward |
| **Total (RSS)** | **15-60 nm** | Combined effect (root-sum-square of all sources) |

## Safety

- **Laser safety**: HeNe interferometer lasers are typically Class II (< 1 mW). Do not stare into the beam. Fiber-delivered systems reduce exposure risk by enclosing the beam path.
- **Cleanliness**: Encoder scales and interferometer optics are sensitive to contamination. A fingerprint on an encoder scale causes signal dropout. Handle with gloves and clean with isopropanol.
- **Beam alignment**: Misaligned interferometer beams give incorrect readings. Regular verification with a reference standard is required.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Encoder signal dropout or noise | Contamination on scale or read head | Clean scale and read head with isopropanol; handle with gloves only; check for dust or fingerprints |
| Interferometer reading drift | Thermal expansion of optics or air path refractive index change | Control ambient temperature to ±0.1°C; compensate for air temperature/pressure/humidity; use common-path optics |
| Subdivision error (SDE) periodic | Imperfect scale grating or misaligned read head | Realign read head to scale; verify grating quality; run manufacturer calibration routine |
| Position jumps at direction reversal | Mechanical backlash or hysteresis in stage | Check for loose mechanical coupling; add backlash compensation in controller; verify preload on bearings |
| Signal loss at high speed | Bandwidth limit of photodetector or interpolation electronics | Reduce traverse speed; upgrade to higher-bandwidth read head; check cable length (signal degradation >3 m) |
| Interferometer fringes unstable | Vibration or air turbulence in beam path | Improve vibration isolation; enclose beam path; reduce air flow near interferometer |

## See Also

- [Nanometer Positioning](nanometer-positioning.md) — actuation technologies for precision stages
- [Wafer Stages & Scanner Systems](wafer-stages.md) — lithography stage systems using encoder feedback
- [Vibration Isolation](vibration-isolation.md) — environmental control for nanometer precision
- [Optical Inspection](../optics/inspection.md) — optical components for encoder systems
- [Precision Metrology](../measurement/precision-metrology.md) — measurement foundations
- [Precision Motion Control](./index.md) — domain overview

---

*Part of the [Bootciv Tech Tree](../index.md) • [Precision Motion Control](./index.md) • [All Domains](../index.md)*
