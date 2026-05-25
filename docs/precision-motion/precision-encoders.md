# Precision Encoders & Feedback

> **Node ID**: precision-motion.precision-encoders
> **Domain**: Precision Motion Control
> **Timeline**: Years 35-55
> **Outputs**: laser_interferometers, optical_encoders, encoder_feedback_systems
> **Dependencies**: None (root capability)
> **Enables**: None (leaf capability)

Nanometer positioning stages (see [Nanometer Positioning](./nanometer-positioning.md)) are only as accurate as their position feedback. A piezo stage may have 0.01 nm actuator resolution, but if the position sensor measures to only 10 nm, the effective positioning accuracy is 10 nm. This document covers the encoder and interferometer technologies that close the feedback loop for nanometer-precision motion: optical scale encoders, laser interferometers, and the signal processing that extracts sub-nanometer position from optical measurements.

## Optical Linear Encoders

Optical encoders measure linear displacement by detecting the passage of a precision grating pattern. A light source illuminates a graduated scale; photodetectors read the resulting interference pattern.

### Incremental Encoders

The most common encoder type for precision motion. A glass or steel scale carries a precise grating (typically 20 μm or 4 μm pitch). An index grating in the read head creates a Moiré interference pattern that cycles through light and dark as the read head moves relative to the scale.

- **Scale pitch**: 20 μm (standard), 4 μm (high-resolution), down to 0.5 μm (ultra-high-resolution with holographic gratings).
- **Signal period**: One full sinusoidal cycle per scale pitch. The read head produces two 90° phase-shifted sinusoidal signals (A and B channels) for bidirectional counting.
- **Interpolation**: Electronic interpolation subdivides each signal period. With 20 μm pitch and 4,096× interpolation: 0.005 μm (5 nm) digital resolution. With 4 μm pitch and 16,384× interpolation: 0.00024 μm (0.24 nm) digital resolution.
- **Accuracy (systematic)**: ±0.1-5 μm over 1 m travel depending on scale quality. The best precision scales use holographic gratings on zero-expansion glass substrates for ±0.1 μm accuracy over 1 m.
- **Repeatability**: ±0.02-0.1 μm — significantly better than absolute accuracy.
- **Maximum speed**: 5-20 m/s. Signal processing bandwidth limits the maximum speed at which interpolation works correctly.

### Scale Materials and Mounting

| Scale Type | Substrate | CTE (×10⁻⁶/°C) | Max Length | Application |
|------------|-----------|-----------------|-----------|-------------|
| Glass scale | Zerodur / glass-ceramic | 0.0-0.1 | 3 m | Highest accuracy, temperature-stable |
| Steel tape scale | Hardened steel | 10-12 | 30 m | Long travel, general industrial |
| Steel tape (low-expansion) | Invar-bonded steel | 0.5-1.0 | 5 m | Medium accuracy, long travel |

**Mounting considerations:**

- **Thermal expansion matching**: The scale's thermal expansion must match the machine structure, or compensation tables must be applied. A 1 m steel scale on a granite base: 12 μm differential expansion per °C — catastrophic at nanometer precision. Use glass-ceramic scales on granite or Invar structures.
- **Scale mounting**: Adhesive-bonded or clamped. Must not be stretched or compressed during mounting — forces distort the grating pitch.
- **Read head gap**: 0.3-1.0 mm air gap between read head and scale surface. Tolerant of small variations but must not contact the scale.

### Absolute Encoders

Incremental encoders lose position count if power is interrupted. Absolute encoders encode unique position in a multi-track code pattern:

- **Single-turn resolution**: 1-23 bits (0.04 μm at 23 bits over 1 m).
- **Serial communication**: BiSS, EnDat, or SSI protocols transmit position data. BiSS and EnDat support 10 MHz clock rates for low-latency position update.
- **Accuracy**: ±0.5-5 μm over full travel. Less accurate than incremental encoders for the finest work but provides power-up position without homing.
- **Application**: General CNC machines, axes where homing is inconvenient. Not typically used for the primary positioning axes of wafer stages (incremental interferometers preferred).

## Laser Interferometers

Laser interferometers measure displacement by counting interference fringes produced by a coherent laser beam. They provide the highest accuracy linear position measurement available, limited only by the wavelength of light and the stability of the optical path.

### Michelson Interferometer (Basic)

The fundamental configuration:

1. **Beam splitting**: A helium-neon (HeNe) laser emits a coherent beam at 632.8 nm wavelength. A beam splitter divides it into reference and measurement beams.
2. **Reference path**: One beam reflects off a stationary reference mirror and returns to the beam splitter.
3. **Measurement path**: The other beam reflects off a mirror attached to the moving stage and returns.
4. **Interference**: The two returning beams recombine at the beam splitter. Constructive or destructive interference depends on the path length difference.
5. **Counting fringes**: Each half-wavelength of stage motion (316.4 nm) produces one complete cycle of intensity variation at the photodetector.

- **Resolution**: 316.4 nm per fringe (basic counting). With electronic interpolation (typically 4-4,096×): 0.08 nm to 79 nm resolution.
- **Accuracy**: ±0.1-1 ppm of measured distance in controlled environment. At 300 mm: ±0.03-0.3 μm.
- **Non-contact**: The measurement beam reflects off a mirror on the stage — no physical contact between sensor and moving part.

### Heterodyne Interferometers

The standard for semiconductor lithography equipment. A Zeeman-split HeNe laser produces two closely-spaced frequencies (f1 and f2, separated by ~1.5-2 MHz) with orthogonal linear polarizations:

1. **Frequency f1** (measurement beam): Reflects off the stage mirror and returns Doppler-shifted by the stage velocity: f1 ± Δf.
2. **Frequency f2** (reference beam): Reflects off a fixed reference mirror at f2.
3. **Beat detection**: The detector measures the beat frequency difference. Stationary: f1 - f2 = 1.5 MHz. Moving: (f1 ± Δf) - f2 = 1.5 MHz ± Δf.
4. **Displacement calculation**: Δf is proportional to stage velocity (Doppler shift). Integrating velocity gives displacement.

**Advantages over homodyne:**
- **DC rejection**: The beat frequency is AC-coupled, rejecting intensity drift (laser power variation, detector aging, contamination).
- **Bidirectional sensing**: Phase of the beat signal relative to a reference indicates direction.
- **Multi-axis capability**: Different polarization or frequency encoding allows multiple axes from one laser source.

### Interferometer Accuracy Limitations

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

### Multi-Axis Interferometer Configurations

Wafer stages require simultaneous X, Y, and angular measurement:

**Plane mirror interferometer (PMI):** Measures displacement relative to a flat mirror. The beam makes double pass (incident + reflected) on the stage mirror, doubling sensitivity. One PMI measures one axis.

**Dual-beam angular measurement:** Two PMI beams separated by a known baseline (100-200 mm) both measure displacement on the same axis. The difference between readings gives angular error (pitch or yaw): θ = (d1 - d2) / baseline.

**Typical wafer stage interferometer configuration:**
- 3-4 X-axis beams (measuring X position and yaw)
- 2-3 Y-axis beams (measuring Y position and pitch)
- Total: 5-7 interferometer measurement channels per stage

### Interferometer Specifications for Semiconductor Equipment

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

## Encoder Signal Processing

### Analog Interpolation

Raw encoder signals are sinusoidal. Extracting sub-period position requires precise interpolation:

- **Arctangent interpolation**: Position = (pitch / 2π) × arctan(A/B), where A and B are the quadrature signals. Requires accurate sinusoidal signals with equal amplitude, perfect 90° phase offset, and zero offset.
- **Signal quality**: Real encoder signals have amplitude mismatch (1-5%), phase error (90° ± 1-5°), and DC offset (0.5-5% of amplitude). These errors create interpolation errors (sub-divisional error, SDE).
- **Sub-divisional error (SDE)**: Periodic error within one signal period, typically ±5-50 nm for optical encoders. For nanometer positioning, SDE must be < ±2 nm. Achieved by careful signal conditioning and calibration.

### Digital Signal Processing

Modern encoder interfaces digitize the analog signals and apply real-time correction:

- **LUT correction**: A lookup table maps raw (A, B) values to corrected position, compensating for systematic signal imperfections measured during calibration.
- **Harmonic compensation**: SDE is decomposed into Fourier harmonics of the signal period. The dominant harmonics (1st, 2nd, 3rd, 4th) are corrected in real-time.
- **Noise filtering**: Anti-alias filters and digital smoothing reduce high-frequency noise. Careful filter design preserves phase margin in the servo loop.

### Latency and Phase Delay

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

## Safety

- **Laser safety**: HeNe interferometer lasers are typically Class II (< 1 mW). Do not stare into the beam. Fiber-delivered systems reduce exposure risk by enclosing the beam path.
- **Cleanliness**: Encoder scales and interferometer optics are sensitive to contamination. A fingerprint on an encoder scale causes signal dropout. Handle with gloves and clean with isopropanol.
- **Beam alignment**: Misaligned interferometer beams give incorrect readings. Regular verification with a reference standard is required.

## References

- Nanometer positioning stages using encoder feedback: [Nanometer Positioning](./nanometer-positioning.md)
- Wafer stage interferometer configurations: [Wafer Stages & Scanner Systems](./wafer-stages.md)
- Optical components for encoder systems: [Optical Inspection](../optics/inspection.md)
- Precision metrology foundations: [Precision Metrology](../measurement/precision-metrology.md)
- Laser sources: [Optics](../optics/index.md)

### See Also

- [Nanometer Positioning](nanometer-positioning.md) — Actuation technologies
- [Wafer Stages & Scanner Systems](wafer-stages.md) — Lithography stage systems
- [Vibration Isolation](vibration-isolation.md) — Environmental control
- [Precision Motion Control](./index.md) — Domain overview

---

*Part of the [Bootciv Tech Tree](../index.md) • [Precision Motion Control](./index.md) • [All Domains](../index.md)*
