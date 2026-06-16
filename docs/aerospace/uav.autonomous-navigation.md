# Autonomous Navigation

> **Node ID**: aerospace.uav.autonomous-navigation
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.uav`](uav.md)
> **Timeline**: Years 45-60+
> **Outputs**: flight_controllers
> **Critical**: No

Autonomous navigation encompasses the flight controller hardware, sensor fusion algorithms, and software that allow a UAV to fly without continuous human control. A multirotor cannot fly without active stabilization — the flight controller is not an autopilot add-on but the primary pilot. This process covers flight controller board design, firmware development, GPS waypoint navigation, and failsafe systems.

## Flight Controller Hardware

A standard flight controller board contains: a 32-bit ARM Cortex-M microcontroller (STM32F4/F7/H7, 168-480 MHz), an IMU (3-axis gyro + accelerometer, e.g., ICM-42688), a barometer (MS5611), a magnetometer, a GPS receiver (u-blox NEO-M8N or similar), and interfaces for ESC output (PWM, DShot), radio receiver input (SBUS, CRSF), and telemetry (UART). Size: 35-45 mm square. Weight: 5-15 g.

## Sensor Fusion

The flight controller estimates attitude and position by fusing multiple sensors. The gyroscope provides high-rate angular velocity (400-8000 Hz) for inner-loop stabilization. The accelerometer and magnetometer provide absolute attitude reference at lower rates. The barometer provides altitude. GPS provides position and velocity. An Extended Kalman Filter (EKF) combines these into a single optimal state estimate with quantified uncertainty. Open-source implementations: PX4 `ekf2`, ArduPilot `AP_NavEKF3`.

## Autonomous Flight Modes

**Position hold**: GPS-locked hover. The UAV maintains position and altitude using GPS and barometer. Wind gusts are corrected within 0.5-2 m. **Waypoint navigation**: The UAV flies a pre-planned mission of GPS waypoints loaded from a ground station. Heading, speed, and altitude are controlled autonomously between waypoints. **Return-to-home (RTH)**: Failsafe behavior — if radio link is lost or battery is low, the UAV climbs to a safe altitude, flies straight to its launch GPS coordinate, and descends vertically to land. **Geofencing**: Virtual boundaries prevent the UAV from entering restricted areas.

## Computer Vision

Advanced UAVs add optical flow (downward camera tracks ground movement for GPS-denied position hold), time-of-flight sensors (obstacle distance), and object tracking (onboard image processing for follow-me and ActiveTrack). These capabilities require more powerful companion computers (Raspberry Pi, NVIDIA Jetson) alongside the flight controller.

## Prerequisites

- [UAV capability](uav.md) — parent capability
- [Computing](../computing/index.md) — microcontrollers, real-time software
- [Electronics](../electronics/index.md) — sensors, PCBs
- [GPS and RF](../electronics/index.md) — satellite navigation, radio links

## See Also

- [Unmanned Aerial Vehicles](uav.md) — parent capability overview
- [Multirotor Drones](uav.multirotor-drones.md) — airframe that uses this FC
- [Fixed-Wing Drones](uav.fixed-wing-drones.md) — airframe that uses this FC

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
