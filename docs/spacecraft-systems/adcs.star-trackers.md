# Star Trackers

> **Node ID**: spacecraft-systems.adcs.star-trackers
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.adcs`](./adcs.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: star_trackers
> **Critical**: No

Star trackers are the most accurate absolute attitude sensors on a spacecraft. They image a star field through a wide-aperture lens, identify the stars by pattern-matching against an on-board catalogue, and compute the inertial attitude quaternion from the known celestial positions. See [ADCS](./adcs.md) for the integrated control system context.

## Overview

A star tracker consists of three main assemblies: an optical baffle (stray light rejection), a lens assembly (focusing star images onto the detector), and a detector + processor unit (CMOS or CCD sensor, FPGA or microprocessor for star identification). The baffle suppresses off-axis sunlight by 10⁶–10⁸, enabling operation even when the sun is just outside the field of view.

Star identification uses a "lost-in-space" algorithm: the tracker extracts the brightest 5–20 stars from the image, computes the angular separations between star pairs, and searches an on-board catalogue (typically 3,000–90,000 stars) for a matching pattern. Once identified, the tracker switches to tracking mode, predicting where each star will appear in the next frame and updating the attitude at full rate.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Accuracy (boresight) | 5–50 arcsec |
| Cross-boresight accuracy | 3–10× worse |
| Update rate | 1–10 Hz |
| Lost-in-space acquisition | 2–60 s |
| Field of view | 10°–30° half-angle |
| Magnitude sensitivity | mv 4–7 |
| Baffle rejection ratio | 10⁶–10⁸ |
| Operating slew limit | 1–3 deg/s |

## Prerequisites

- Optical-grade lens fabrication and alignment ([optics](../optics/))
- Radiation-tolerant CMOS/CCD detector and readout electronics
- Star catalogue database and pattern-matching algorithm
- Thermal control for optical bench stability

## See Also

- [ADCS](./adcs.md) — parent capability
- [Sun & Earth Sensors](./adcs.sun-earth-sensors.md) — coarse backup
- [IMU & Gyroscopes](./adcs.imu-gyros.md) — rate propagation between updates

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
