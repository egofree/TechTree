# GNC Integration

> **Node ID**: `launch-vehicles.vehicle-architecture.gvnc-integration`
> **Domain**: [Launch Vehicles](./index.md)
> **Parent**: [Vehicle Architecture](./vehicle-architecture.md)
> **Outputs**: avionics_buses, flight_software, gnss_receivers
> **Timeline**: Years 30-200+

## Overview

Guidance, Navigation, and Control (GNC) is the avionics and software system that steers the launch
vehicle along its planned trajectory to the target orbit. Without closed-loop guidance, a rocket is
an unguided ballistic projectile. GNC determines orbital insertion accuracy (position, velocity at
payload separation) and vehicle survival through Max-Q, stage separation, and engine transients.

## Navigation Sensors

**Inertial Measurement Unit (IMU)**: The IMU is the navigation core. Modern strapdown IMUs use
ring-laser gyroscopes (RLG) or fibre-optic gyroscopes (FOG) measuring angular rate with drift
below 0.001°/hour, plus accelerometers (quartz flexure or MEMS) measuring linear acceleration to
micro-g precision. The IMU integrates acceleration to velocity and position (dead reckoning),
accumulating 10-50 m of position error over a 10-minute ascent without external correction.

**GPS/GNSS receiver**: A multi-channel GPS receiver on the upper stage provides 10-20 Hz position
and velocity updates that bound IMU drift. This reduces orbital insertion error from kilometres
(IMU-only, as in early ICBMs) to tens of metres (GPS-aided, as in modern vehicles). GPS is
unavailable during hypersonic plasma blackout (~40-80 km altitude) but recovers before the final
coast and circularisation phases.

**Star tracker**: An optical camera identifies star patterns and computes attitude to arcsecond
precision (1 arcsec ≈ 5 µrad). Star trackers provide an absolute attitude reference that does not
drift, correcting IMU gyro drift on long coasts. Most vehicles carry one or two star trackers for
terminal guidance.

## Guidance and Control

**Guidance law**: The flight computer executes a **powered explicit guidance (PEG)** algorithm
that continuously computes the thrust direction needed to reach the target orbit, given the
current state vector, remaining propellant, and engine performance. PAG converges in real time,
adapting to off-nominal thrust, winds, and vehicle mass properties.

**Thrust vector control (TVC)**: Engine nozzles gimbal ±5-10° to steer the vehicle by deflecting
thrust. The control loop commands TVC actuators (hydraulic or electromechanical) at 20-100 Hz to
maintain the guidance-commanded attitude. Solid rocket boosters use jet vanes or liquid-injection
TVC since the nozzle itself is fixed.

## Flight Software

The flight software for a modern launch vehicle runs to 100,000-500,000 lines of code on
triple-redundant flight computers (voting logic rejects a failed channel). The software is
developed under DO-178C or equivalent safety-critical process, with extensive hardware-in-the-loop
(HITL) simulation covering thousands of nominal and off-nominal scenarios before first flight.

## See Also

- [Vehicle Architecture](./vehicle-architecture.md) — parent capability
- [Electronics](../electronics/index.md) — avionics hardware
- [Computing](../computing/index.md) — flight software and simulation

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
