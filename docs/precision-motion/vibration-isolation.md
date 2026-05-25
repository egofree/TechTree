# Vibration Isolation

> **Node ID**: precision-motion.vibration-isolation
> **Domain**: Precision Motion Control
> **Timeline**: Years 35-60
> **Outputs**: vibration_isolation_systems, isolation_platforms, vibration_specs
> **Dependencies**: None (root capability)
> **Enables**: None (leaf capability)

Nanometer positioning (covered in [Nanometer Positioning](./nanometer-positioning.md)) assumes a vibration-free environment. In reality, semiconductor fabs and precision laboratories are full of vibration sources: rotating machinery, foot traffic, HVAC systems, external road traffic, and even the motion of the precision equipment itself. This document covers the passive and active vibration isolation systems that create the ultra-quiet mechanical environment required for nanometer-precision work. A wafer stage positioning to ±5 nm is meaningless if the floor vibrates by 100 nm — the isolation system must attenuate floor vibration to well below the positioning budget.

## Vibration Sources and Characteristics

### Ground-Borne Vibration

Vibration enters through the building foundation from external and internal sources:

| Source | Frequency Range | Amplitude (displacement) | Notes |
|--------|----------------|--------------------------|-------|
| Road traffic | 5-30 Hz | 1-10 μm | Heavy trucks at 20-100 m distance |
| Railway | 5-30 Hz | 0.5-5 μm | Freight trains at 100-500 m |
| Construction | 5-50 Hz | 1-100 μm | Pile driving, demolition |
| Rotating machinery | 10-200 Hz | 0.1-5 μm | HVAC fans, compressors, pumps |
| Foot traffic | 1-10 Hz | 0.5-5 μm | Walking near equipment |
| Building resonances | 1-20 Hz | 0.1-2 μm | Structural modes excited by wind or machinery |
| Acoustic noise | 20-20,000 Hz | Converted to vibration | Loud machinery, compressed air |

### Vibration Specification: VC Curves

The generic vibration criterion (VC) curves define acceptable floor vibration levels for various precision applications:

| Criterion | Max Velocity (μm/s RMS) | Frequency Range | Application |
|-----------|------------------------|-----------------|-------------|
| VC-A | 50 | 4-80 Hz | Optical microscope, 1 μm precision |
| VC-B | 25 | 4-100 Hz | Electron microscope, 0.1 μm precision |
| VC-C | 12.5 | 4-200 Hz | Probe station, 30 nm precision |
| VC-D | 6.25 | 4-200 Hz | Stepper/scanner, 10 nm precision |
| VC-E | 3.12 | 4-200 Hz | EUV lithography, AFM, <5 nm precision |
| VC-F | 1.56 | 4-200 Hz | Extreme precision metrology, <1 nm |

For wafer steppers and scanners (VC-D to VC-E), the floor vibration velocity must be below 3-6 μm/s RMS across 4-200 Hz. Most factory floors are 10-50 μm/s — isolation is mandatory.

### Self-Generated Vibration

The precision equipment itself generates vibration during operation:

- **Stage acceleration forces**: A 50 kg wafer stage accelerating at 30 m/s² generates 1,500 N reaction force into the machine base. Even with reaction compensation, residual forces of 10-50 N remain.
- **Motor cogging**: Iron-core linear motor cogging at 5-50 Hz (1-5% force ripple).
- **Coolant flow**: Liquid cooling pumps and flowing water in cooling channels create 10-100 Hz vibration.
- **Fan noise**: Electronics cooling fans generate 100-1000 Hz vibration.
- **Cable forces**: Moving cables exert changing forces on the stage, causing 1-10 Hz disturbances.

## Passive Vibration Isolation

Passive isolation uses mechanical elements (springs, dampers, pneumatic air springs) to attenuate floor vibration before it reaches the payload. No sensors, no electronics, no power required.

### Pneumatic Air Spring Isolation

The most common passive isolation for precision equipment. Three or four air springs (also called air isolators or pneumatic mounts) support the equipment on a rigid platform.

**Operating principle**: A sealed rubber/fabric air bag filled with compressed air (2-8 bar) acts as a soft spring. The air's compressibility provides low spring stiffness, giving a low natural frequency (0.5-3 Hz). An orifice connecting the main air volume to a small damping chamber provides viscous damping.

- **Natural frequency**: 0.5-3 Hz vertically, 1-5 Hz horizontally. Lower natural frequency → better isolation at higher frequencies.
- **Isolation efficiency (transmissibility)**: Above the natural frequency, vibration is attenuated. At 10 Hz with 1.5 Hz natural frequency: ~90% isolation (10:1 attenuation). At 50 Hz: >99% isolation.
- **Damping ratio**: 2-8% of critical. Higher damping reduces resonance amplification at the natural frequency but slightly degrades high-frequency isolation.
- **Load capacity**: 100-50,000 N per isolator depending on size and pressure.
- **Leveling**: Automatic leveling valves maintain platform height within ±0.1 mm as load changes (wafer loading, stage motion). Three isolators define a plane; four isolators require individual leveling valves.
- **Transmissibility at resonance**: 3-10× amplification at the natural frequency. This is the trade-off — low-frequency vibration near the natural frequency is amplified, not attenuated.

### Transmissibility Curve

```
Transmissibility (output/input)
  ^
10│    ╱╲
  │   ╱  ╲  ← resonance amplification
 1├──╱────╲─────────────────────────
  │ ╱      ╲
  │╱        ╲
0.1│         ╲
  │          ╲
0.01│          ╲___________________
  └───────────────────────────────→ Frequency (Hz)
       f_n     2f_n   5f_n   10f_n
```

Below natural frequency (f_n): transmissibility ≈ 1 (no isolation).
At f_n: transmissibility = 3-10× (amplification).
Above √2 × f_n: transmissibility < 1 (isolation begins).
At 5× f_n: transmissibility ≈ 0.04 (96% isolation).

### Mechanical Spring Isolation

Steel coil springs with viscous dampers provide an alternative to pneumatic isolation:

- **Natural frequency**: 1-5 Hz (higher than pneumatic due to stiffer springs).
- **Advantages**: No air supply needed, no leveling valves to maintain, wider temperature range.
- **Disadvantages**: Higher natural frequency means less isolation at low frequencies. Steel springs transmit high-frequency vibration through internal resonance modes.
- **Application**: Equipment in locations where compressed air is unavailable, or where maintenance-free operation is required.

### Elastomeric (Rubber) Mounts

Simple rubber pads or molded mounts provide minimal isolation:

- **Natural frequency**: 5-20 Hz — too high for nanometer precision.
- **Isolation**: Effective above 20-50 Hz only.
- **Application**: Light-duty isolation for optical tables, bench-top instruments. Not suitable as primary isolation for semiconductor lithography equipment, but used for secondary equipment (pumps, chillers).

## Active Vibration Isolation

Active isolation adds sensors and actuators to the passive system, enabling:

1. **Better low-frequency isolation**: Cancel vibration below the passive natural frequency where passive systems amplify.
2. **Narrow-band cancellation**: Target specific disturbance frequencies (e.g., 50 Hz from electrical mains).
3. **Active leveling**: Maintain platform position without mechanical leveling valves.

### Sensor-Actuator Architecture

Each isolation axis uses a combination of:

**Sensors:**
- **Geophones (velocity sensors)**: Moving-coil geophones measure absolute floor velocity from 0.5-200 Hz. Sensitivity: 1-50 V/(m/s). Passive — no power required.
- **Accelerometers**: Piezoelectric accelerometers measure absolute acceleration from 1-10,000 Hz. Sensitivity: 1-100 mV/g.
- **Displacement sensors**: LVDT or capacitive sensors measure relative displacement between isolated platform and floor. Used for active leveling.

**Actuators:**
- **Voice coil actuators**: Force proportional to current, bandwidth to 1000 Hz. Force range: 10-500 N per axis. Most common for active isolation.
- **Piezo actuators**: High stiffness, fast response, limited stroke (10-100 μm). Used for fine vibration cancellation.
- **Pneumatic actuators**: Modulate air spring pressure via servo valves. High force, low bandwidth (< 10 Hz). Used for active leveling and very-low-frequency compensation.

### Feedback Control Strategies

**Feedforward cancellation**: Floor vibration is measured by reference sensors on the floor. The controller predicts the vibration that will reach the payload and generates a canceling force. Works well for predictable, repetitive disturbances.

**Feedback cancellation**: Payload vibration is measured directly. The controller generates a force to drive the measured vibration to zero. Works for all disturbances but limited by stability margins.

**Combined feedforward + feedback**: Best performance. Feedforward handles predictable floor vibration; feedback handles unpredictable disturbances and self-generated vibration.

### Active Isolation Performance

| Parameter | Passive Only | Passive + Active |
|-----------|-------------|------------------|
| Natural frequency (vertical) | 1.5 Hz | < 0.3 Hz (effective) |
| Transmissibility at 1 Hz | 2-5× (amplified) | < 0.5 (attenuated) |
| Transmissibility at 5 Hz | 0.2 | < 0.05 |
| Transmissibility at 10 Hz | 0.05 | < 0.01 |
| Transmissibility at 50 Hz | 0.005 | < 0.001 |
| Settling time (after step) | 2-5 s | 0.2-0.5 s |
| Active power consumption | 0 W | 50-500 W |
| Cost multiplier | 1× | 3-10× |

## Foundation and Installation Design

### Isolation Pit Design

For the best vibration performance, precision equipment is installed on a massive concrete block isolated from the building floor:

- **Block mass**: 10-100 tonnes depending on equipment mass and isolation requirements. Rule of thumb: block mass ≥ 5× equipment mass.
- **Isolation from building**: The block rests on pneumatic isolators or elastomeric pads, completely separated from the surrounding floor slab by a 50-100 mm air gap.
- **Center of gravity**: Equipment must be mounted with its center of gravity close to the block's center. Off-center loads create rocking modes.
- **Inertia block material**: Reinforced concrete (density 2,400 kg/m³). For extreme performance, lead-filled concrete (5,000+ kg/m³) increases mass in a given volume.

### Floor Vibration Assessment

Before installing precision equipment, a vibration site survey is conducted:

1. **Measurement duration**: Minimum 24 hours to capture daily traffic patterns, HVAC cycles, and construction activity.
2. **Sensor placement**: Triaxial accelerometer on the proposed installation location.
3. **Frequency analysis**: FFT of vibration data identifies dominant frequencies and their amplitudes.
4. **VC curve comparison**: Measured vibration is compared to the required VC criterion.
5. **Remediation if needed**: If floor vibration exceeds the criterion, additional isolation (deeper foundation, active isolation upgrade, or relocation) is specified.

### Environmental Vibration Control

Beyond the isolation system, the fab environment is designed to minimize vibration sources:

- **Equipment placement**: Precision tools located away from loading docks, elevators, and mechanical rooms. Minimum 15-30 m from heavy vibrating machinery.
- **Structural decoupling**: Equipment foundations mechanically isolated from the building structure. Expansion joints between foundation slabs.
- **HVAC design**: Low-vibration air handlers with flexible duct connections. Vibration-isolated compressor mounts. Air velocity in ducts near tools limited to < 5 m/s to minimize aerodynamic vibration.
- **Raised access floors**: Precision tools often mounted on isolated pads below the raised floor, not on the raised floor itself which amplifies foot traffic vibration.

## Vibration Measurement and Diagnostics

### Accelerometer Specifications for Vibration Monitoring

| Parameter | Value | Notes |
|-----------|-------|-------|
| Sensitivity | 1-10 V/g | High sensitivity for low-level vibration |
| Frequency range | 0.5-1000 Hz | Covers VC-criterion bandwidth |
| Noise floor | < 1 μg/√Hz | Must measure below VC-E criterion |
| Dynamic range | > 120 dB | Simultaneously capture large and small vibrations |
| Temperature range | -20 to +80°C | For fab environment |
| Mounting | Stud-mounted or magnetic | Stud mounting for best frequency response |

### Vibration Diagnostics

When vibration exceeds specification:

1. **Frequency identification**: FFT analysis reveals dominant frequencies. Match to known sources (motor RPM, fan blade pass frequency, electrical mains harmonics).
2. **Time-domain correlation**: Compare vibration spikes to equipment operation logs (wafer stage acceleration events, pump cycling).
3. **Propagation path analysis**: Measure vibration at multiple points (floor, base, stage) to identify the transmission path.
4. **Source remediation**: Fix the source if possible (balance rotating equipment, add dampers, reschedule heavy traffic). Add isolation if the source cannot be fixed.

## Isolation for Specific Applications

### Optical Table Isolation

For laboratory-scale precision optics and metrology:

- **Honeycomb optical table**: Stainless steel top and bottom skins bonded to aluminum honeycomb core. Flat, rigid, lightweight, with threaded mounting holes on 25 mm grid.
- **Pneumatic table legs**: Four air-spring isolators with automatic leveling. Natural frequency 1-2 Hz.
- **Performance**: <10 nm vibration on table surface in typical lab environment.
- **Application**: Interferometry, holography, laser-based measurement, small-scale wafer inspection.

### Large Lithography Tool Isolation

For production wafer steppers and scanners:

- **Three-point pneumatic isolation**: Machine base supported on three large-diameter air springs (300-600 mm diameter each) for unambiguous plane definition.
- **Active isolation option**: Voice coil actuators in parallel with air springs for low-frequency cancellation.
- **Isolation specification**: VC-D to VC-E at the wafer stage mounting interface.
- **Machine base mass**: 5,000-20,000 kg. Massive base provides inertia against stage reaction forces.
- **Installation**: On isolated inertia block in fab, with 0.5-1 m thick concrete slab.

### Electron Microscope Isolation

For SEM/TEM requiring <1 nm vibration:

- **Passive isolation**: High-performance pneumatic isolators with 0.5-1 Hz natural frequency.
- **Active isolation**: Optional for sites with poor floor vibration.
- **Acoustic enclosure**: Additional enclosure to attenuate airborne sound that couples to column vibration.
- **Magnetic field shielding**: μ-metal enclosure around column to prevent AC magnetic fields from deflecting the electron beam.
- **Performance**: Floor vibration at column tip < 0.5 nm RMS.

## Safety

- **Pneumatic pressure**: Air springs contain compressed air at 2-8 bar. Sudden rupture can cause platform to drop. Burst discs and pressure relief valves required.
- **Pinch hazards**: Heavy equipment on isolated platforms can move several millimeters during leveling. Keep hands clear of gaps between platform and fixed structures.
- **Active system failure**: If active isolation loses power, the system reverts to passive mode. Platform may oscillate briefly at the passive natural frequency. Equipment should be designed to tolerate this reversion.
- **Earthquake design**: In seismic zones, isolation systems must include mechanical restraints (snubbers) that limit platform displacement during an earthquake to prevent the equipment from sliding off its mounts.

## References

- Nanometer positioning that requires vibration isolation: [Nanometer Positioning](./nanometer-positioning.md)
- Wafer stage vibration sensitivity: [Wafer Stages & Scanner Systems](./wafer-stages.md)
- Precision measurement for vibration monitoring: [Precision Metrology](../measurement/precision-metrology.md)
- Pneumatic and hydraulic systems: [Gas Handling](../gas-handling/index.md)
- Building and foundation design: [Construction](../construction/index.md)

### See Also

- [Nanometer Positioning](nanometer-positioning.md) — Actuation technologies
- [Wafer Stages & Scanner Systems](wafer-stages.md) — Lithography stage systems
- [Precision Encoders](precision-encoders.md) — Measurement feedback
- [Precision Motion Control](./index.md) — Domain overview

---

*Part of the [Bootciv Tech Tree](../index.md) • [Precision Motion Control](./index.md) • [All Domains](../index.md)*
