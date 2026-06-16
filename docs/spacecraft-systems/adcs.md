# Attitude Determination & Control

> **Node ID**: spacecraft-systems.adcs
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: `optics`, `precision-motion`, `electronics`,
> `machine-tools`
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: adcs_hardware, star_trackers, reaction_wheels
> **Critical**: No — ADCS integrates mature disciplines (optics, precision mechanics, sensor electronics) into a spacecraft pointing system; the challenge is systems engineering under mass, power, and radiation constraints, not a single breakthrough material or process

Attitude Determination and Control Systems (ADCS) are the nervous system of a spacecraft. They determine where the vehicle is pointing, compare that to where it *should* be pointing, and drive actuators to close the gap — continuously, autonomously, for years. A geostationary communications satellite must hold its antenna beam to within 0.05° of a ground target; the Hubble Space Telescope must stabilize to 0.001° (3.6 arcseconds) to produce unblurred long exposures; an Earth-observation satellite needs 0.01° pointing to map terrain at sub-metre resolution. Every decimal place of pointing accuracy demands an order of magnitude more engineering.

This article covers the integrated design of spacecraft ADCS across six process areas: [star trackers](./adcs.star-trackers.md), [sun and Earth sensors](./adcs.sun-earth-sensors.md), [IMU and gyroscopes](./adcs.imu-gyros.md), [reaction wheels](./adcs.reaction-wheels.md), [magnetorquers](./adcs.magnetorquers.md), and [thruster control](./adcs.thruster-control.md). Each plays a distinct role in the sensing-estimation-control-actuation loop. Together they determine the pointing accuracy, agility, and lifetime of the spacecraft.

## Overview

ADCS operation follows a classic feedback control loop. **Sensors** measure the spacecraft's attitude (orientation in inertial space) and angular rate. An **estimator** — typically an Extended Kalman Filter (EKF) or Unscented Kalman Filter (UKF) — fuses noisy, asynchronously sampled sensor data into a best-estimate attitude quaternion and gyro bias. A **control law** compares the estimated attitude to the commanded attitude and computes the required torque. An **actuator allocation** scheme distributes that torque command across the available actuators (wheels, magnetorquers, thrusters). The actuators apply torque, the spacecraft rotates, and the loop closes.

The difficulty is that every element of this loop has limitations. Star trackers are accurate but update slowly (1–10 Hz) and lose track during fast slews or blinding by the sun. Gyroscopes provide high-bandwidth rate data but drift over time. Reaction wheels deliver precise, continuous torque but saturate when they absorb too much angular momentum from disturbance torques. Magnetorquers are cheap and reliable but only work in low Earth orbit (LEO) where the geomagnetic field is strong. Thrusters provide authoritative torque but consume irreplaceable propellant. The art of ADCS design is selecting the right sensor-actuator mix for the mission and writing the flight software that orchestrates them.

### Control Loop Block Diagram

The ADCS control loop can be described as a signal chain:

```
Sensors → Attitude Estimator (EKF/UKF) → Control Law (Quaternion Feedback) → Actuator Allocation → Actuators → Spacecraft Dynamics → Sensors
```

Each stage:

1. **Sensors**: Star trackers (absolute attitude), sun/Earth sensors (coarse attitude), IMU gyros (angular rate), magnetometers (field vector)
2. **Attitude Estimator**: EKF or UKF fuses star tracker quaternions (low-frequency, low-noise) with gyro rates (high-frequency, high-noise) to produce a continuous best-estimate quaternion and gyro bias correction
3. **Control Law**: Proportional-derivative quaternion feedback computes torque as τ = −Kp × q_error − Kd × ω, where q_error is the vector part of the quaternion error and ω is the angular rate
4. **Actuator Allocation**: Distributes torque demand across reaction wheels (Trij = I_wheel × α_wheel), magnetorquers (τ = m × B), or thrusters, respecting saturation limits and power constraints
5. **Spacecraft Dynamics**: Rigid-body (or flexible-body) dynamics with disturbance torques from aerodynamic drag, solar radiation pressure, gravity gradient, and residual magnetic dipole

## Sensor Comparison

The following table compares the four primary attitude sensor types used in modern spacecraft. Every sensor is a trade between accuracy, update rate, field of regard, mass, and cost. A well-designed ADCS fuses multiple sensor types so that the strengths of one compensate for the weaknesses of another.

| Sensor Type | Accuracy | Update Rate | Field of Regard | Mass | Notes |
|-------------|----------|-------------|-----------------|------|-------|
| Star tracker | 5–50 arcsec (0.0025°–0.014°) | 1–10 Hz | 20°–40° cone | 1–5 kg | Lost-in-space acquisition 2–60 s |
| Sun sensor (fine digital) | 0.01°–0.1° | 10–50 Hz | Hemisphere | 0.1–0.5 kg | Blinded in eclipse |
| Sun sensor (coarse analog) | 1°–5° | 10–50 Hz | Hemisphere | 0.05–0.2 kg | Survival mode only |
| Earth horizon sensor | 0.1°–0.5° | 1–5 Hz | Nadir only | 0.3–1.5 kg | Constrained to Earth-pointing orbits |
| Magnetometer | 0.5°–2° | 1–10 Hz | Full sphere | 0.1–0.3 kg | LEO only, needs magnetic cleanliness |
| MEMS gyro | 0.01–1 deg/hr drift | 100–1000 Hz | Full rate | 0.05–0.2 kg | Degrades with radiation |
| FOG (fiber-optic gyro) | 0.001–0.01 deg/hr drift | 100–1000 Hz | Full rate | 0.5–2 kg | Premium navigation grade |
| RLG (ring laser gyro) | 0.0001–0.001 deg/hr drift | 100–1000 Hz | Full rate | 1–3 kg | Highest precision, no moving parts |

### Star Tracker Benchmarks

The star tracker is the king of attitude sensors. It images a star field, identifies the stars by pattern-matching against an on-board catalogue, and computes the spacecraft's inertial attitude from the known positions of those stars. The process is analogous to a sailor finding their position by sighting known stars — but executed in seconds, autonomously, and with arcsecond precision.

| Star Tracker | Accuracy | Update Rate | Acquisition Time | Mass | Flight Heritage |
|-------------|----------|-------------|-----------------|------|----------------|
| Sinclair ST-16 (Douglas) | 16 arcsec | 2 Hz | <5 s | 0.4 kg | CanX satellites |
| Ball CT-402 | 7 arcsec (3σ) | 10 Hz | <10 s | 1.5 kg | LRO, SDO, JPSS |
| Sirius SSTL SENSE-2020 | 5 arcsec (3σ) | 4 Hz | <3 s | 0.9 kg | Earth observation |
| Jena ASTRO-15 | 6 arcsec | 5 Hz | <60 s | 2.7 kg | Sentinel, Galileo |
| Leonardo HYDRA | 10 arcsec | 10 Hz | <5 s | 1.4 kg | Cosmo-SkyMed |

Key star tracker performance parameters:

- **Accuracy**: The cross-boresight accuracy is typically 3–10× worse than the boresight (pitch/yaw) accuracy because the star pattern constrains rotation about the sensor axis less tightly than rotation perpendicular to it
- **Update rate**: Limited by exposure time (10–100 ms), readout, and processing. Faster trackers use CMOS sensors and FPGA-based star identification
- **Lost-in-space acquisition**: When the tracker has no prior attitude knowledge, it must identify stars from a full-sky catalogue — this "lost-in-space" mode takes 2–60 seconds depending on catalogue size, FOV, and processor speed
- **Tracking mode**: Once identified, the tracker tracks known star positions frame-to-frame at full update rate, but loses track during angular rates above ~1–3 deg/s or when the sun or moon enters the FOV
- **Stray light rejection**: Requires an external baffle (often 1–3× the sensor length) to suppress off-axis sunlight by 10⁻⁶ to 10⁻⁸

### IMU and Gyroscope Technology

Gyroscopes measure angular rate and fill the temporal gap between star tracker updates. A modern Inertial Measurement Unit (IMU) contains three orthogonal gyros (measuring ωx, ωy, ωz) and often three accelerometers. The critical parameter is **drift** — the slow accumulation of angular error when the spacecraft is stationary.

- **MEMS (Micro-Electro-Mechanical Systems)**: Coriolis-force vibrating structure etched from silicon. Drift: 0.01–1 deg/hr. Mass: 50–200 g. Used in cubesats and cost-sensitive missions. Radiation-sensitive (single-event upsets corrupt the resonator electronics)
- **FOG (Fiber-Optic Gyro)**: Two counter-propagating light beams in a fiber coil; rotation causes a Sagnac phase shift proportional to angular rate. Drift: 0.001–0.01 deg/hr. Mass: 0.5–2 kg. No moving parts, excellent lifetime. Used in most medium-class satellites
- **RLG (Ring Laser Gyro)**: Two counter-propagating laser beams in a triangular or square ring cavity; rotation causes a beat frequency. Drift: 0.0001–0.001 deg/hr. Mass: 1–3 kg. Highest precision but requires high-voltage ignition and dither motors to avoid lock-in at low rates. Used in strategic platforms (intercontinental missiles, high-end reconnaissance)

The gyro drift is estimated in real time by the EKF, which compares the rate-integrated attitude against star tracker measurements. A typical star tracker update every 1–10 seconds bounds the gyro drift accumulation to a few arcseconds, making the combined sensor fusion far more accurate than either sensor alone.

## Actuator Comparison

Actuators apply torque to change or maintain the spacecraft's attitude. The choice of actuator determines the agility, lifetime, and propellant budget of the ADCS.

| Actuator Type | Torque Range | Continuous? | Propellant? | Best Use |
|---------------|-------------|-------------|-------------|----------|
| Reaction wheel | 0.01–1 Nm | Yes (electrical) | No (battery power) | Fine pointing, fast slews |
| Control moment gyro (CMG) | 10–1000 Nm | Yes (electrical) | No | Large spacecraft agile slews |
| Magnetorquer | 0.001–0.1 Nm | Conditional (field) | No | LEO momentum dumping |
| Cold gas thruster | 0.1–10 N | Pulsed | Yes (N2) | Backup, contingency |
| Monopropellant thruster | 1–500 N | Pulsed | Yes (hydrazine) | Orbit adjust + momentum dump |

### Reaction Wheel Specifications

Reaction wheels are the workhorse actuator for precision pointing. A reaction wheel is simply a flywheel spun by a brushless DC motor: accelerating the wheel in one direction produces a spacecraft torque in the opposite direction (conservation of angular momentum). A typical spacecraft carries three or four wheels (the fourth is skewed for redundancy and to handle singularity avoidance).

| Parameter | Small Sat | Medium Sat | Large Sat |
|-----------|-----------|------------|-----------|
| Angular momentum capacity | 0.1–1 Nms | 1–10 Nms | 10–50 Nms |
| Maximum torque | 0.01–0.05 Nm | 0.05–0.2 Nm | 0.2–0.5 Nm |
| Max speed | 6,000 RPM | 6,000 RPM | 6,000–10,000 RPM |
| Bearing type | Ball bearings | Ball bearings | Ball / magnetic |
| Bearing MTBF | >5 years | >7 years | >10 years |
| Wheel imbalance | <0.5 g·cm | <0.5 g·cm | <0.1 g·cm |
| Mass | 1–3 kg | 3–8 kg | 8–15 kg |

Critical reaction wheel design parameters:

- **Angular momentum capacity**: Determines how much angular momentum the wheel can absorb before saturating. Saturation occurs when the wheel reaches its maximum speed and can no longer provide torque in that direction
- **Maximum torque**: Sets the maximum slew rate. A 0.1 Nm torque on a 500 kg spacecraft with I = 200 kg·m² produces α = 0.0005 rad/s², requiring ~140 seconds for a 90° slew
- **Bearing MTBF**: The single greatest lifetime limiter. Ball bearing lubricant degrades in vacuum; typical qualified life is 7–10 years. Magnetic bearings eliminate contact wear but are heavier and more complex
- **Micro-vibration**: Wheel imbalance at the spin frequency introduces jitter that degrades pointing for imaging payloads. Active isolation or very low imbalance (<0.1 g·cm) is needed for sub-arcsecond missions
- **Viscous friction**: At high speed, bearing friction produces a parasitic drag torque that must be overcome, wasting power and generating heat

### Magnetorquer Specifications

Magnetorquers (also called magnetic torque rods) exploit the interaction between an on-board magnetic dipole and the Earth's geomagnetic field. A current-carrying coil produces a dipole moment **m** (measured in A·m²), and the resulting torque is τ = **m** × **B**, where **B** is the local geomagnetic field vector. The torque is always perpendicular to **B** — magnetorquers cannot produce torque about the field axis.

- **Dipole moment**: 1–10 A·m² for typical LEO satellites; cubesat magnetorquers (embedded in PCB coils) produce 0.1–0.5 A·m²
- **Operating altitude**: Effective below ~2000 km where the geomagnetic field is strong enough; useless at GEO where the field is ~100× weaker
- **Control authority**: A 5 A·m² dipole in a 30 μT LEO field produces 0.15 mN·m — enough to dump wheel momentum over minutes, not enough for agile slews
- **Uses**: Momentum dumping (desaturating reaction wheels), detumbling after separation, backup attitude control, and B-dot stabilization during safe hold mode
- **Limitation**: The two-axis torque constraint means magnetorquers cannot hold arbitrary attitudes; they are always paired with reaction wheels or gravity-gradient stabilization

### Thruster Control for Momentum Management

When reaction wheels saturate and magnetorquers are unavailable (or insufficient), thrusters provide the authority to dump accumulated angular momentum. Thruster control consumes propellant — a finite resource that ultimately limits spacecraft lifetime.

- **Cold gas (N₂)**: Simplest system — stored nitrogen expanded through a nozzle. Isp ~65 s. Thrust 0.1–10 N. Non-toxic, non-reactive. Used on cubesats and some LEO constellations for both orbit and attitude control
- **Monopropellant (hydrazine, N₂H₄)**: Catalytic decomposition on a hot iridium bed produces hot nitrogen and hydrogen gas. Isp ~220 s. Thrust 1–500 N. The workhorse for medium and large satellites. Toxic and requires careful handling
- **Pulse width modulation**: Thrusters fire in short pulses (10–100 ms) to approximate continuous torque. Minimum impulse bit (MIB) determines pointing precision: a 1 N thruster with 10 ms MIB produces 0.01 N·s impulse, coarser than a reaction wheel by 3 orders of magnitude
- **Dual-mode systems**: Many spacecraft use reaction wheels for fine pointing and thrusters only for periodic momentum dumping (every few hours to days, depending on disturbance torque magnitude)

## Pointing Accuracy by Mission Class

The required pointing accuracy drives every ADCS design decision — from the number and grade of star trackers to the rigidity of the spacecraft structure and the sophistication of the control law.

| Mission Class | Pointing Accuracy | Stability | Typical Sensor Suite | Typical Actuators |
|---------------|-------------------|-----------|---------------------|-------------------|
| Simple LEO cubesat | 1°–5° | 0.5°/s | Coarse sun sensors, magnetometer | Magnetorquers only |
| LEO Earth observation | 0.01°–0.1° | 0.001°/s | 1 star tracker, MEMS gyro | 3 reaction wheels + magnetorquer |
| GEO communications | 0.05°–0.2° | 0.005°/s | 2 star trackers, FOG | 4 reaction wheels + thruster dump |
| Science (Hubble, JWST) | 0.001°–0.005° | 0.0001°/s | 3+ star trackers, FOG/RLG | 4–6 wheels + fine guidance |
| Interplanetary | 0.01°–0.1° | 0.001°/s | 2 star trackers, FOG | Wheels + thruster backup |

The Hubble Space Telescope exemplifies the extreme end: it achieves 0.001° (3.6 arcsecond) absolute pointing using three Fine Guidance Sensors (specialised star trackers), six rate gyros (three operational, three backup), and four reaction wheel assemblies. The James Webb Space Telescope pushes further to milli-arcsecond pointing using six reaction wheels, a fine steering mirror for tip-tilt correction, and 126 sunshield membrane tensioners that must not inject vibration.

## Momentum Management

Reaction wheels absorb angular momentum from external disturbance torques. In LEO, the dominant disturbances are aerodynamic drag (below ~400 km), gravity gradient torque (for non-symmetric spacecraft), solar radiation pressure, and residual magnetic dipole from on-board current loops. These disturbances are continuous and one-sided — they always push the wheel in the same direction. Without active momentum management, a reaction wheel will saturate within hours to days.

### The Saturation Problem

When a wheel reaches its maximum speed, it can no longer accelerate in the saturation direction. The ADCS loses attitude control authority along that axis until the stored momentum is "dumped" — transferred out of the wheel and into the orbital environment. The three dumping methods:

1. **Magnetorquer dumping**: Fire magnetorquers to produce a torque that opposes the disturbance torque while simultaneously commanding the reaction wheel to decelerate. The angular momentum flows from the wheel into the Earth's magnetic field. This is the standard method for LEO spacecraft and requires no propellant — only electrical power
2. **Thruster dumping**: Fire attitude thrusters to produce a continuous torque while the wheels decelerate. Consumes propellant. Used at GEO (no usable magnetic field) and as backup at LEO. Typical dump events last 5–30 seconds and are scheduled during non-observation windows
3. **Gravity gradient dumping**: Reorient the spacecraft so that the gravity gradient torque naturally opposes the stored momentum. Passive, no actuators needed, but very slow (minutes to hours) and constrains the attitude

The dumping cycle is typically automated: the flight software monitors wheel speeds and triggers a dump sequence when any wheel exceeds ~80% of its capacity. The dump completes in minutes (magnetorquer) or seconds (thruster), then normal pointing operations resume.

## Attitude Estimation: EKF and UKF

The heart of the ADCS flight software is the attitude estimator. Its job is to fuse asynchronous, noisy, multi-rate sensor data into a continuous best-estimate attitude. The two dominant algorithms are the Extended Kalman Filter (EKF) and the Unscented Kalman Filter (UKF).

- **EKF**: Linearises the attitude kinematics about the current estimate. The state vector typically includes the attitude quaternion (4 components, but only 3 are independent) and the gyro bias vector (3 components). The EKF propagates the state using gyro rate data at 50–100 Hz and updates it with star tracker quaternions at 1–10 Hz. Fast and well-understood, but the linearisation can diverge during large-angle slews
- **UKF**: Uses the unscented transform (a deterministic sampling of sigma points) to propagate the mean and covariance through the full nonlinear dynamics. More accurate than EKF for large-angle slews and nonlinear sensor models, but computationally heavier (typically 2n+1 function evaluations per step, where n is the state dimension)
- **MEKF (Multiplicative EKF)**: The most common flight implementation. Uses a small error quaternion (δq) as the state rather than the full quaternion, avoiding the quaternion normalisation constraint and ensuring the covariance remains well-conditioned

The estimator output — a best-estimate quaternion and angular rate at 50–100 Hz — feeds directly into the control law with essentially zero latency from the spacecraft's perspective. The star tracker's slow update rate is invisible to the control loop because the estimator interpolates between updates using the gyro data.

## Control Law Design

The control law converts the attitude error into a torque command. The most common approach is **proportional-derivative quaternion feedback**:

τ = −Kp × q_e(v) − Kd × ω

Where q_e(v) is the vector part of the quaternion error (the scalar part carries redundant information), ω is the estimated angular rate, Kp is the proportional gain (stiffness), and Kd is the derivative gain (damping). The gains are tuned to balance slew speed against structural excitation and fuel consumption.

Design considerations:

- **Gain scheduling**: Kp and Kd are often scheduled as a function of wheel speed (lower gains near saturation to avoid commanding impossible torques) and slew mode (high gains for fine pointing, lower gains for large slews to limit structural loads)
- **Integral action**: An integral term can be added to counter steady-state disturbance torques, but risks windup. Anti-windup logic is mandatory
- **Rate limiting**: The control law clips the commanded torque to the actuator's maximum, preventing the wheels from being driven into saturation by aggressive commands
- **Actuator allocation**: For a four-wheel configuration with one skewed wheel, a pseudoinverse allocation matrix maps the 3-axis torque command to four wheel torque commands while minimising total wheel speed and avoiding singular configurations

## Manufacturing Dependencies

The ADCS capability depends on four upstream industrial domains, each contributing a critical technology:

- **Optics**: Star tracker lenses, baffles, and optical alignment are [precision-optics](../optics/) products. A star tracker baffle must suppress stray light by 10⁶–10⁸ while maintaining thermal stability across a 200°C sun-to-eclipse swing
- **Precision-motion**: Reaction wheel bearings, gimbal assemblies, and wheel balancing rely on [precision-motion](../precision-motion/) engineering. Ball bearings with sub-micron runout and vacuum-compatible lubrication are essential for the 7+ year bearing MTBF requirement
- **Electronics**: Star tracker processors, gyro readout electronics, motor controllers, and sensor interface circuits are all [electronics](../electronics/) products. Radiation-hardened electronics survive the total ionising dose (10–100 krad for LEO, 1–10 Mrad for interplanetary)
- **Machine-tools**: Reaction wheel rotor balancing to <0.1 g·cm, star tracker housing machining to micron tolerances, and thruster valve seat lapping all require [machine-tools](../machine-tools/) capability at the precision end of the spectrum

## System Integration Challenges

ADCS is fundamentally a systems integration problem. The individual sensors and actuators are mature, off-the-shelf components in many cases. The difficulty lies in integrating them into a coherent, reliable, autonomous system:

- **Structural flexibility**: Solar panels and antennas are flexible appendages that couple their vibration modes into the rigid-body attitude dynamics. The control law must not excite these modes — typically by limiting bandwidth below the first flexible mode frequency (often 0.1–1 Hz for large panels)
- **Thermo-elastic distortion**: Temperature gradients across the spacecraft structure bend the structure, shifting the alignment between star trackers and payload. A 1°C gradient across a 1 m carbon-fibre truss produces ~1 arcsecond of misalignment — significant for science missions
- **Radiation effects**: Total ionising dose degrades sensor electronics (gyro drift increases, star tracker dark current rises). Single-event upsets corrupt processor memory. The ADCS must detect and recover from these events autonomously
- **Safe-hold mode**: When the primary ADCS fails, a backup mode using coarse sun sensors and magnetorquers must keep the spacecraft power-positive and thermally stable until ground intervention. This "safe hold" mode is often the difference between a recoverable anomaly and a total loss

## Key Parameters Summary

| Parameter | Value Range | Notes |
|-----------|-------------|-------|
| Pointing accuracy | 0.001°–5° | Mission-dependent |
| Pointing stability | 0.0001°–1°/s | Over 1–60 s integration windows |
| Slew rate | 0.1–10 deg/s | Agile vs. observatory class |
| Star tracker accuracy | 5–50 arcsec | Boresight; cross-axis 3–10× worse |
| Gyro drift (MEMS) | 0.01–1 deg/hr | Radiation-degraded over mission life |
| Gyro drift (FOG) | 0.001–0.01 deg/hr | Premium navigation grade |
| Reaction wheel momentum | 0.1–50 Nms | Scales with spacecraft I×slew requirement |
| Reaction wheel torque | 0.01–0.5 Nm | Sets max slew acceleration |
| Magnetorquer dipole | 0.1–10 A·m² | LEO only |
| Thruster impulse bit | 0.001–0.1 N·s | Sets pointing resolution |
| Control loop rate | 50–100 Hz | Estimator propagation |
| Star tracker update | 1–10 Hz | Measurement update to EKF |

## ADCS Operating Modes

A spacecraft ADCS typically operates in a sequence of modes, each with different sensor-actuator combinations and control objectives. The mode transitions are managed autonomously by the flight software based on sensor health, pointing requirements, and spacecraft state.

| Mode | Sensors | Actuators | Purpose |
|------|---------|-----------|---------|
| Detumble | Magnetometer, coarse gyro | Magnetorquers | Stop post-separation rotation (B-dot law) |
| Rate damping | Coarse sun sensors, gyro | Magnetorquers, thrusters | Reduce rates to <0.1 deg/s |
| Sun acquisition | Coarse sun sensors | Wheels or thrusters | Align solar panels to sun |
| Safe hold | Sun sensors, magnetometer | Magnetorquers | Power-positive, thermally safe |
| Standby | Star tracker, gyro | Wheels (zero-torque) | Hold current attitude, ready for command |
| Pointing | Star tracker, gyro, FOG | Wheels | Precision pointing for payload ops |
| Slew | Star tracker, gyro | Wheels (high torque) | Repoint to new target |

### Detumble Mode

Immediately after separation from the launch vehicle, the spacecraft may be tumbling at rates of 1–10 deg/s. Detumble mode uses the simplest control law — **B-dot**: τ = −k × dB/dt. The magnetorquer torque opposes the measured rate of change of the magnetic field vector, which is proportional to the spacecraft rotation rate. This passively damps rotation without needing attitude knowledge. Detumble typically completes in 5–30 minutes.

### Sun Acquisition and Safe Hold

After detumble, the ADCS commands a rotation to find the sun (using coarse sun sensors). Once acquired, the spacecraft aligns its solar panels sunward and enters safe hold — a passive, power-positive state that can be maintained indefinitely. If the primary ADCS fails at any point during the mission, the spacecraft autonomously falls back to safe hold to preserve battery and thermal stability.

## See Also

- [Star Trackers](./adcs.star-trackers.md) — optical attitude sensing
- [Sun & Earth Sensors](./adcs.sun-earth-sensors.md) — coarse attitude reference
- [IMU & Gyroscopes](./adcs.imu-gyros.md) — rate sensing and propagation
- [Reaction Wheels](./adcs.reaction-wheels.md) — primary actuator
- [Magnetorquers](./adcs.magnetorquers.md) — momentum dumping
- [Thruster Control](./adcs.thruster-control.md) — backup actuation and momentum management
- [Optics](../optics/) — star tracker lenses and baffles
- [Precision Motion](../precision-motion/) — bearings and gimbals
- [Electronics](../electronics/) — sensor processing and motor control
- [Machine Tools](../machine-tools/) — precision balancing and machining

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
