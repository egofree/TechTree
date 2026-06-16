# Precision Landing

> **Node ID**: `launch-vehicles.edl.precision-landing`
> **Domain**: [Launch Vehicles](./index.md)
> **Parent**: [Entry, Descent & Landing](./edl.md)
> **Outputs**: landing_navigation_systems, terrain_relative_maps
> **Timeline**: Years 30-200+

## Overview

Precision landing provides the navigation accuracy required to touch down at a predetermined point
— a recovery pad, an autonomous droneship, or a pre-surveyed safe site on another planet. The
challenge increases with distance from Earth (GPS is unavailable beyond LEO), atmospheric
unpredictability (Mars winds), and landing-site hazards (boulders, craters, slopes).

## Navigation Modes

**GPS-aided inertial**: For terrestrial landings, a GPS receiver on the descending stage provides
10-20 Hz position updates to the IMU. Falcon 9 uses this to achieve sub-metre landing accuracy on
the droneship. GPS is unavailable during hypersonic plasma blackout (~40-80 km altitude) but
recovers below ~40 km, before the landing burn begins.

**Terrain-Relative Navigation (TRN)**: For GPS-denied landings (Mars, Moon), TRN matches descent
camera imagery to a pre-loaded orbital map. A downward-looking camera captures images at 5-10 Hz
during the final 1-4 km of descent. An onboard processor correlates features (craters, ridges,
albedo variations) against a map generated from high-resolution orbital imagery (HiRISE for Mars,
LROC for the Moon). Position is determined to 5-40 m accuracy, feeding corrections to the IMU.

Mars 2020 Perseverance used TRN (the Lander Vision System) to achieve ~10 m landing accuracy —
versus 10+ km for Viking (1976) and 3-4 km for MSL (2012). This enabled landing in Jezero Crater,
a site too hazardous for earlier landers.

**Hazard avoidance**: Beyond navigation, the system must detect and avoid landing hazards. During
the final ~100 m of descent, hazard-detection algorithms analyse descent imagery for boulders
(>50 cm), craters, and slopes exceeding safety limits (>15°). If the target zone contains a
hazard, the system commands a divert manoeuvre to the nearest safe spot within reachable range.
Perseverance's system could detect 50 cm hazards and divert up to 300 m.

## Terminal Sensors

**Doppler radar altimeter**: Provides direct altitude and velocity measurement independent of
inertial drift. Ka-band or X-band radar measures round-trip time and Doppler shift for altitude
(to 0.1 m accuracy) and three-axis velocity (to 0.1 m/s). Used on Apollo LM, all Mars landers,
and Falcon 9.

**Lidar**: Some advanced systems use scanning lidar for higher-resolution hazard mapping in the
final seconds. Produces a 3D point cloud of the landing zone for centimetre-scale hazard detection.

## Key Parameters

| Parameter | Falcon 9 (GPS) | Perseverance (TRN) |
|-----------|---------------|-------------------|
| Landing accuracy | <1 m | ~10 m |
| Update rate | 20 Hz (GPS) | 5-10 Hz (camera) |
| Hazard detection | None (fixed pad) | 50 cm objects |
| Divert range | N/A | 300 m |

## See Also

- [Entry, Descent & Landing](./edl.md) — parent capability
- [Retropropulsion](./edl.retropropulsion.md) — landing burns guided by precision nav
- [GNC Integration](./vehicle-architecture.gvnc-integration.md) — ascent navigation

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
