# Unmanned Aerial Vehicles

> **Node ID**: aerospace.uav
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`electronics`](../electronics/index.md),
> [`computing`](../computing/index.md),
> [`aerospace.aviation`](aviation.md),
> [`energy.electricity.motor`](../energy/index.md)
> **Enables**: None
> **Timeline**: Years 40-60+
> **Outputs**: unmanned_aerial_vehicles, flight_controllers, drone_airframes
> **Critical**: No

Unmanned Aerial Vehicles (UAVs), commonly called drones, are the simplest powered aircraft: no pilot, no cockpit, no life-support systems, no control linkages routed to a stick. All weight is devoted to airframe, propulsion, sensors, and payload. This weight budget advantage — combined with fly-by-wire stabilization that no human reflexes can match — makes UAVs the easiest powered flying machine to build, test, and deploy. A 1 kg quadcopter carries a camera that would have required a manned helicopter in 1980.

The trade-off: a UAV replaces mechanical control linkages with electronics and software. A multirotor drone without its flight controller is unflyable — it would flip and crash within seconds because no human can modulate four motor speeds 400 times per second. The flight controller, an inertial measurement unit (IMU), and a microprocessor running PID control loops are not conveniences but prerequisites. This places UAVs firmly in the electronic era: they cannot exist without PCB manufacturing, MEMS gyroscopes, brushless DC motors, and lithium-polymer batteries.

## UAV Classification

UAVs are classified by weight, endurance, and operating altitude. The following taxonomy is adapted from public-source frameworks (NATO Class I-V, EASA Open/Specific/Certified categories).

| Class | Weight | Endurance | Altitude | Example |
|-------|--------|-----------|----------|---------|
| I (Micro/Nano) | < 250 g | 5-15 min | < 120 m | Toy quadcopters, racing drones |
| II (Mini/Small) | 250 g - 2 kg | 15-30 min | < 120 m | DJI Phantom, Parrot AR.Drone |
| III (Light) | 2-25 kg | 30-60 min | < 150 m | DJI Inspire, DJI Mavic 3 |
| IV (Medium) | 25-150 kg | 1-6 hours | < 3000 m | General Atomics MQ-9 Predator |
| V (Heavy/HALE) | > 150 kg | 6-24+ hours | < 6000 m | MQ-9, RQ-4 Global Hawk |

**Class I-II** (consumer/hobbyist): Foam or injection-molded plastic airframes, brushless motors with 5-10 inch propellers, 2S-4S lithium polymer batteries (7.4-14.8 V). Flight controllers based on STM32 ARM Cortex-M microcontrollers. Cost: $100-3,000. Examples: DJI Phantom series (2013-present), Parrot AR.Drone (2010, one of the first smartphone-controlled UAVs).

**Class III** (professional/commercial): Carbon fiber airframes, weatherproof electronics, 6S batteries (22.2 V), gimbal-stabilized cameras with 4K video. Redundant IMU and GPS. Retractable landing gear on larger models. Cost: $3,000-30,000. Examples: DJI Inspire series, DJI Mavic 3 Enterprise.

**Class IV-V** (large/long-endurance): Composite airframes with aluminum or titanium structural elements. Gasoline or heavy-fuel piston engines, or turboprops, for endurance beyond electric battery limits. Satellite communication beyond line-of-sight. Cost: $500,000-$20,000,000+. Examples: General Atomics MQ-9 Predator (public-source data only — no classified performance parameters). All performance data in this article is sourced from publicly available manufacturer specifications and open literature.

## Why UAVs Are the Simplest Powered Aircraft

A manned aircraft must carry: a pilot (80 kg), a cockpit (structure, windshield, canopy — 30-50 kg), environmental controls (heating, ventilation, oxygen — 10-20 kg), control stick and rudder pedals with mechanical linkages (10-15 kg), instruments and avionics (10-20 kg), and a seat and harness (5-10 kg). Total pilot-system weight: 145-195 kg. An equivalent UAV replaces all of this with a flight controller board weighing 5-50 g.

For the bootstrap scenario, this means:
- **No life-support**: No oxygen system, no pressurization, no cabin heat.
- **No pilot training**: No need for months of flight instruction. The software is the pilot.
- **Expendable**: A crashed UAV is a lost airframe, not a lost life. Testing is aggressive and iterative.
- **Smaller scale**: A 1-5 kg UAV requires proportionally less material, less manufacturing precision, and less infrastructure than a manned aircraft.

The barrier shifts from mechanical engineering (control linkages, cockpit layout, pilot safety) to electronic engineering (sensor integration, firmware, control loops). This is why UAVs appear at Year 40-60+ in the bootstrap timeline — they require mature electronics and computing capabilities that precede them.

## Flight Controller Architecture

The flight controller (FC) is the core of any UAV. It is a single-board computer that reads sensor data, computes desired motor outputs, and sends commands to electronic speed controllers (ESCs) at 400-8000 Hz update rates.

### Sensor Suite

**Inertial Measurement Unit (IMU)**:
- **Gyroscope**: Measures angular velocity (°/s) around three axes (roll, pitch, yaw). Modern UAVs use MEMS gyroscopes (e.g., MPU-6050, ICM-42688) — tiny vibrating structures whose Coriolis effect produces a signal proportional to rotation rate. Range: ±250 to ±2000 °/s. Noise: 0.01-0.05 °/s RMS. Bandwidth: 50-500 Hz.
- **Accelerometer**: Measures linear acceleration (including gravity) along three axes. MEMS accelerometers use a proof mass suspended on silicon springs; capacitance changes between the mass and fixed plates are proportional to acceleration. Range: ±2 to ±16 g. Used for leveling (gravity vector provides roll/pitch reference) and altitude hold (double-integration of vertical acceleration).
- **Magnetometer**: Measures Earth's magnetic field for compass heading. 3-axis Hall-effect or magnetoresistive sensor (e.g., HMC5883L, QMC5883L). Range: ±1 to ±8 gauss. Subject to interference from motors, ESCs, and ferromagnetic airframe materials — requires calibration (figure-8 motion to map hard-iron and soft-iron distortions).

**Barometer**: Measures atmospheric pressure for altitude estimation. MEMS barometers (e.g., MS5611, BMP388) provide altitude resolution of 0.1-1 m. Subject to drift from temperature changes and atmospheric pressure variation. Used for altitude hold and RTH altitude.

**GPS Receiver**: Global Positioning System receiver provides latitude, longitude, altitude, ground speed, and heading (from successive position fixes). Consumer UAVs use L1 C/A code receivers (3-5 m accuracy). Dual-band (L1/L5) receivers achieve 0.5-2 m accuracy with corrections. Update rate: 1-10 Hz. A UAV needs at least 6 satellites for a 3D position fix with reasonable integrity. GPS is the primary outdoor position sensor; indoor flight requires optical flow or time-of-flight sensors instead.

### Sensor Fusion

No single sensor provides complete attitude and position information. The gyroscope drifts over time (integration of bias). The accelerometer is noisy and cannot distinguish gravity from acceleration. The magnetometer is distorted by nearby metal. The GPS updates too slowly for inner-loop stabilization.

**Complementary filter** (simplest): A high-pass filter on the gyroscope (trust short-term rotation rate) combined with a low-pass filter on the accelerometer/magnetometer (trust long-term absolute reference). The cutoff frequency determines the blend: typically 0.5-2 Hz. Easy to implement, adequate for stable hover flight.

**Extended Kalman Filter (EKF)** (standard): A recursive estimator that maintains a state vector (quaternion attitude, velocity, position, gyro bias, accelerometer bias) and updates it with each sensor measurement weighted by its uncertainty. The EKF predicts state using the gyroscope and corrects it using accelerometer, magnetometer, barometer, and GPS data. The mathematical foundation (state transition matrix, Jacobian, covariance update) is well-documented in public literature. Open-source implementations: PX4 `ekf2`, ArduPilot `AP_NavEKF`.

### Control Loops

A UAV uses a cascaded PID control architecture:

**Inner loop (attitude rate)**: Runs at 400-8000 Hz. Input: desired angular velocity (from outer loop). Feedback: gyroscope angular velocity. Output: per-motor thrust correction. This loop must be fast enough to counteract aerodynamic disturbances (propeller torque, wind gusts) within one motor update cycle.

**Middle loop (attitude angle)**: Runs at 100-400 Hz. Input: desired roll/pitch/yaw angle (from pilot or navigation). Feedback: estimated attitude from sensor fusion. Output: desired angular velocity to inner loop.

**Outer loop (position/velocity)**: Runs at 10-50 Hz. Input: desired position or velocity (from waypoint navigation or pilot stick). Feedback: GPS position, accelerometer velocity. Output: desired attitude to middle loop.

**PID tuning**: Proportional (P) gain determines response aggressiveness — too low: sluggish, too high: oscillation. Integral (I) gain eliminates steady-state error — too high: integral windup, overshoot. Derivative (D) gain dampens oscillation — sensitive to sensor noise (requires low-pass filtering). Typical quadcopter PID values: roll/pitch P = 40-80, I = 30-60, D = 15-35. Tuning is aircraft-specific and verified by step-response flight testing.

## Multirotor Flight Mechanics

A quadcopter uses four motors arranged in an X or + pattern. Motors 1 and 3 rotate clockwise (CW); motors 2 and 4 rotate counter-clockwise (CCW). This counter-rotation cancels net torque — without it, the airframe would spin uncontrollably.

**Roll**: Increase speed on one side, decrease on the other. E.g., to roll right: increase left motors, decrease right motors.

**Pitch**: Increase speed on rear motors, decrease front motors (to pitch forward) or vice versa.

**Yaw**: Increase speed on CW motors, decrease on CCW motors (or vice versa). This creates a net torque imbalance that rotates the airframe around the vertical axis.

**Throttle**: Increase or decrease all four motors equally.

The flight controller computes these four adjustments (roll, pitch, yaw, throttle) every cycle and mixes them into four motor commands using a mixing matrix:

```
Motor[0] = Throttle - Roll + Pitch + Yaw   (front-left, CCW)
Motor[1] = Throttle - Roll - Pitch - Yaw   (rear-left, CW)
Motor[2] = Throttle + Roll + Pitch - Yaw   (front-right, CW)
Motor[3] = Throttle + Roll - Pitch + Yaw   (rear-right, CCW)
```

This "mixing" is the fundamental control allocation for a quadcopter X-frame.

## Electronic Speed Controllers (ESC)

Each brushless motor requires an ESC — a dedicated power electronics module that converts DC battery voltage into three-phase AC for the brushless motor. The ESC reads throttle commands (PWM, OneShot, or DShot protocol) from the flight controller and commutates the motor by energizing stator coils in sequence based on rotor position (sensed via back-EMF or a Hall-effect sensor).

Modern ESCs use field-oriented control (FOC) for smooth, efficient torque production, and support bidirectional communication (telemetry: RPM, voltage, current, temperature). DShot600 is a common digital protocol: 600 kHz bit rate, 16-bit frames (11-bit throttle + 1-bit telemetry request + 4-bit CRC).

## Propulsion System

**Brushless DC motors (BLDC)**: Outrunner configuration (stator inside, rotating permanent-magnet shell outside) for high torque at low RPM — ideal for large propellers. Stator: laminated silicon steel with copper windings (typically 12 or 14 poles, 380-2600 KV rating where KV = RPM per volt). Rotor: steel ring with bonded neodymium magnets (N35-N52 grade). Bearings: sealed radial ball bearings (e.g., 6804-2RS). Typical efficiencies: 80-90%.

**Propellers**: Injection-molded ABS/nylon or carbon fiber. Common sizes: 5-inch (racing), 8-10 inch (Class I-II), 12-15 inch (Class III). Pitch: 3-5 inches (low pitch = more thrust at low speed, high pitch = more speed). Two-blade is most efficient; three-blade used when prop diameter is constrained. Propeller balance is critical — unbalanced props cause vibration that corrupts IMU data and fatigues the airframe.

**Batteries**: Lithium polymer (LiPo) cells at 3.7 V nominal (4.2 V charged). Configurations: 2S (7.4 V) for micro drones, 4S (14.8 V) for Class I-II, 6S (22.2 V) for Class III. Energy density: 150-250 Wh/kg. Discharge rate (C-rating): 25-100C (continuous). A 4S 1500 mAh 75C battery can deliver 15 × 75 = 112.5 A burst. Flight time: 5-30 minutes depending on payload and flight mode.

## Airframe Construction

**Foam (EPS/EPO)**: Used for beginner and fixed-wing drones. Expanded polyolefin foam is lightweight, cheap, repairable with hot glue, and absorbs impact. Injection-molded at low cost. Strength is low — foam airframes are disposable.

**Injection-molded plastic**: ABS or polycarbonate shells for consumer quadcopters (DJI Phantom). Provides consistent manufacturing, good surface finish, moderate strength. Snap-fit assembly reduces fastener count.

**Carbon fiber composite**: Prepreg carbon fiber laid up in molds and cured under vacuum bag at 120-150°C. Used for professional and racing drones. Strength-to-weight ratio 3-5x better than aluminum. Plate-and-standoff construction (flat carbon plates separated by aluminum or carbon spacers) is the simplest composite airframe style. Tubular carbon spars for fixed-wing drone wings.

**Aluminum**: Used for motor mounts, standoffs, and structural arms on larger UAVs. 6061-T6 and 7075-T6 alloys. Provides heat sinking for motors and rigid structural members.

## Applications

| Application | Description | Typical UAV Class |
|-------------|-------------|-------------------|
| **Aerial photography** | Gimbal-stabilized cameras for film, real estate, events | II-III |
| **Survey/mapping** | Photogrammetry, 3D terrain modeling, orthomosaic maps | II-IV |
| **Agriculture** | Crop health monitoring (NDVI), precision spraying, livestock counting | II-IV |
| **Delivery** | Medical supply delivery, e-commerce last-mile delivery (prototype) | III-IV |
| **Search & rescue** | Aerial search patterns, thermal imaging for missing persons | III-IV |
| **Infrastructure inspection** | Power line, wind turbine, pipeline, bridge inspection | II-III |
| **Environmental monitoring** | Wildlife tracking, forest fire mapping, pollution detection | II-IV |

## Bootstrap Relevance

In a civilization bootstrap scenario, UAVs serve critical roles before manned flight becomes practical:

1. **Aerial survey without pilots**: Map terrain, identify resources, plan road and rail routes, assess agricultural land — all without training a pilot or risking a life.
2. **Communications relay**: A hovering or loitering UAV can serve as a temporary radio repeater for ground teams operating in difficult terrain.
3. **Search and rescue**: Locate lost persons or survey disaster areas before ground teams can reach them.
4. **Crop monitoring**: Identify irrigation problems, pest outbreaks, and nutrient deficiencies before they reduce yield — critical for food security in early agriculture.
5. **Bridge to manned flight**: UAV development validates aerodynamic designs, tests materials, and builds institutional knowledge of flight dynamics before the first manned aircraft. Every crash teaches a lesson at no human cost.

The prerequisite chain: electronics (PCBs, MEMS sensors) → computing (microcontrollers, RTOS) → energy.electricity.motor (brushless motors, ESCs, LiPo batteries) → aerospace.aviation (aerodynamics, airframe design) → aerospace.uav. Each prerequisite is well-established before UAV construction begins.

## Notable Public-Source UAV Platforms

**Parrot AR.Drone (2010)**: One of the first consumer UAVs controlled via smartphone. WiFi video link, foam airframe, two cameras (front 720p, downward QVGA). Demonstrated that a toy-class UAV could be mass-produced at ~$300. Open SDK enabled academic research.

**DJI Phantom (2013)**: Ready-to-fly quadcopter with integrated GPS, NAZA flight controller, and GoPro camera mount. Made UAV photography accessible to non-hobbyists. Subsequent Phantom 3/4 added 4K cameras, obstacle sensing, and computer-vision-based tracking (ActiveTrack).

**DJI Mavic / Inspire series (2016-present)**: Folding-arm designs (Mavic) for portability; professional cinema platforms (Inspire) with interchangeable cameras and 360° gimbal rotation. The Inspire 2 uses a dual-battery system for redundancy and can reach 80 km/h in sport mode.

**General Atomics MQ-9 Predator (public-source data only)**: Class V medium-altitude long-endurance (MALE) UAV. Public specifications: wingspan 20 m, maximum takeoff weight 4760 kg, service ceiling 15,420 m, endurance 14-27 hours depending on configuration. Powered by a 900 HP turboprop engine. This article references only publicly available specifications — no classified performance parameters are discussed.

## Communication Systems

A UAV communicates with its ground station via a radio link for command/control (RC) and telemetry, and a separate link for live video.

**RC link (command/control)**: Consumer UAVs use 2.4 GHz spread-spectrum protocols (DJI OcuSync, FrSky ACCST, TBS Crossfire). Range: 100 m to 15 km depending on protocol and environment. Long-range UAVs use 433 MHz or 868/915 MHz UHF links for greater range at lower bandwidth. The protocol must be bidirectional — the ground station sends stick commands, the UAV sends telemetry (battery voltage, GPS position, attitude, mode).

**Video link**: Analog 5.8 GHz FPV (first-person view) — analog composite video transmitted on one of 40 channels (5740-5920 MHz). Range: 0.5-3 km, latency <40 ms. Used for racing and freestyle. Digital video (DJI HD, Walksnail) offers 720p/1080p with 30-100 ms latency at longer range.

**Telemetry**: MAVLink is the de facto standard protocol — a compact binary message format over serial/UART or UDP. Messages include HEARTBEAT (system status), ATTITUDE (roll/pitch/yaw), GLOBAL_POSITION_INT (lat/lon/alt), SYS_STATUS (battery, errors), and MISSION_ITEM (waypoints). A typical telemetry stream runs at 57,600 baud, consuming <5 kB/s.

## Ground Station Software

The ground station is the operator's interface to the UAV. It displays telemetry, allows mission planning, and logs flight data. Open-source options: QGroundControl (cross-platform, MAVLink-based), Mission Planner (Windows, ArduPilot). Features: real-time map with UAV position and trajectory, waypoint editor (click on map to set mission), joystick/keyboard control for manual override, parameter tuning (PID gains, flight mode settings), and flight data recording for post-flight analysis.

## Flight Testing Methodology

UAV testing follows a progressive envelope expansion approach — similar to manned aircraft testing but at lower risk and higher iteration speed.

**Bench testing**: With propellers removed, arm the flight controller and verify motor response to manual stick inputs. Check that each motor spins in the correct direction and that the FC correctly maps roll/pitch/yaw commands to the expected motor mix. Verify sensor readings: gyro near zero when stationary, accelerometer showing 1 g downward, magnetometer pointing toward magnetic north.

**Tethered hover test**: Suspend the UAV from a tether or test stand that prevents free flight but allows limited movement. Verify stable hover, correct attitude response to stick inputs, and no oscillation or instability. If oscillation occurs, reduce P gain. If sluggish, increase P gain.

**Free flight — manual**: In an open area with no obstacles or people, perform a brief hover at 1-2 m altitude. Test pitch, roll, yaw response. Land. If all is well, gradually increase altitude and distance.

**GPS flight test**: Enable position-hold mode. Verify the UAV holds position within 1-2 m in calm air. Test waypoint navigation with a short mission (2-3 waypoints, 50-100 m spacing). Verify RTH by turning off the transmitter — the UAV should climb to safe altitude, return, and land.

**Failure mode testing**: Deliberately induce single-motor failure on a hexacopter or octocopter (disable one ESC in software). Verify the UAV can maintain controlled flight and land safely. Test GPS loss — the UAV should switch to attitude-hold mode and remain controllable.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| UAV flips on takeoff | Motor direction wrong or props on wrong arms | Verify motor rotation direction and propeller placement against the frame diagram |
| Violent oscillation in hover | P gain too high | Reduce roll/pitch P gain by 20-30%; increase D gain slightly for damping |
| Toilet-bowl effect (circular drifting in GPS hold) | GPS interference or poor PID on position loop | Recalibrate compass away from metal; reduce position-hold P gain; check GPS HDOP < 2.0 |
| Flyaway on GPS mode | Compass interference from battery or power distribution | Perform compass calibration; relocate compass away from battery; add ferrite ring to power leads |
| Short flight time (<50% expected) | Battery aging, high drag, motor inefficiency | Check battery internal resistance (<20 mΩ per cell); verify propeller balance; check motor bearings for wear |
| ESC desync (motor stops mid-flight) | ESC firmware incompatible or signal wire noise | Update ESC firmware (BLHeli_S/32); enable DShot for digital signal; add capacitor to reduce electrical noise |
| GPS drift > 5 m | Poor satellite geometry or multipath | Wait for HDOP < 2.0; fly in open area away from buildings; upgrade to dual-frequency GPS |

## Reference Specifications

**Class II multirotor (DJI Phantom class)**:

| Parameter | Value |
|-----------|-------|
| Weight (all-up) | 1.0-1.4 kg |
| Diagonal wheelbase | 350-450 mm |
| Motors | 4 × 2312 size, 960 KV |
| Propellers | 4 × 9.4 × 5.0 inch (CW/CCW pairs) |
| Battery | 4S LiPo, 4480-5870 mAh |
| Flight time (hover) | 20-28 min |
| Max speed | 16 m/s (sport mode) |
| Max wind resistance | 10 m/s |
| Operating temperature | 0°C to 40°C |
| GPS accuracy (hover) | ±0.5-2 m |

**Class III multirotor (DJI Inspire class)**:

| Parameter | Value |
|-----------|-------|
| Weight (all-up) | 2.5-4.2 kg |
| Wheelbase | 550-650 mm |
| Motors | 4 × 3515 size, 420 KV |
| Propellers | 4 × 13 × 4.5 inch |
| Battery | 6S LiPo, 4280-7100 mAh |
| Flight time (with payload) | 15-27 min |
| Max speed | 26 m/s |
| Payload capacity | 0.5-2.5 kg (camera + gimbal) |

## Limitations

- **Battery life**: 5-30 minutes for electric multirotors. Fixed-wing electric: 30-90 minutes. Endurance beyond 1 hour requires internal combustion engines or fuel cells.
- **Weather**: Consumer UAVs cannot fly in rain (electronics not waterproofed) or wind above 10-15 m/s. Multirotors are especially susceptible to wind due to their light weight and large side profile.
- **Payload**: Class I-II UAVs carry 0.1-1 kg. Delivery applications require Class III or larger.
- **Regulatory**: UAV operations are restricted by airspace regulations in most jurisdictions. BVLOS (beyond visual line of sight) operations require special authorization.
- **Security**: Radio control links can be jammed. GPS can be spoofed. Autonomous UAVs with robust anti-jam and visual navigation are an active research area.
- **Manufacturing complexity**: MEMS sensors, brushless motors, and LiPo batteries are not trivial to manufacture. The electronics supply chain must be mature.

## Safety Considerations

- **Battery fire**: LiPo batteries can ignite if punctured, overcharged, or short-circuited. Store in fireproof bags. Charge in a supervised area with a balanced charger. A burning LiPo battery cannot be extinguished with water or conventional fire extinguishers — it must burn out.
- **Propeller strike**: A spinning 10-inch propeller at 8000 RPM has blade tip speed of 106 m/s. Contact with skin causes laceration. Contact with eyes can cause permanent injury. Always remove props when bench-testing.
- **Flyaway**: Loss of radio link or GPS glitch can cause the UAV to fly away. Failsafe RTH (return-to-home) is mandatory — if radio link is lost for >2 seconds, the UAV automatically returns to its launch point and lands.
- **Midair collision**: A UAV colliding with a manned aircraft can cause engine failure or windshield penetration. Never fly above 120 m (400 ft) or within 5 km of an airport without authorization.

## Integration Points

| Stage | Contribution |
|-------|-------------|
| [Electronics](../electronics/index.md) | PCBs, MEMS sensors (gyro, accel, mag, baro), GPS receivers |
| [Computing](../computing/index.md) | Microcontrollers, RTOS, sensor fusion algorithms, flight control firmware |
| [Aviation](aviation.md) | Aerodynamics, airframe design, propeller theory, flight testing methodology |
| [Electric Motors](../energy/index.md) | Brushless DC motors, electronic speed controllers, LiPo batteries |
| [Polymers](../polymers/index.md) | Injection-molded airframe shells, foam airframes, composite matrix resins |
| [Metals](../metals/index.md) | Aluminum structural members, motor housings, steel bearings |

## Key Deliverables

- Flyable multirotor airframe (carbon fiber or molded plastic, 0.25-25 kg)
- Flight controller board (STM32 or equivalent, IMU, barometer, GPS)
- Electronic speed controllers (one per motor, DShot or PWM protocol)
- Brushless DC motors matched to propeller size and airframe weight
- Flight control firmware with attitude stabilization and GPS position hold
- Autonomous waypoint navigation with failsafe return-to-home
- Ground station software for mission planning and telemetry display
- Battery charging and maintenance protocol (LiPo safety)

## See Also

- [Aviation](aviation.md) — manned aircraft, full-scale aerodynamics, flight testing
- [Electronics](../electronics/index.md) — PCB manufacturing, sensors, microcontrollers
- [Computing](../computing/index.md) — software, real-time operating systems, algorithms
- [Energy](../energy/index.md) — electric motors, battery technology
- [Fixed-Wing Drones](uav.fixed-wing-drones.md) — long-endurance fixed-wing UAV construction
- [Multirotor Drones](uav.multirotor-drones.md) — quadcopter/hexacopter construction
- [Autonomous Navigation](uav.autonomous-navigation.md) — flight controllers, sensor fusion, autonomy

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
