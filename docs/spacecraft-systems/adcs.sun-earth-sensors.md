# Sun & Earth Sensors

> **Node ID**: spacecraft-systems.adcs.sun-earth-sensors
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.adcs`](./adcs.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: adcs_hardware
> **Critical**: No

Sun and Earth horizon sensors provide coarse attitude references for safe-hold modes, sun acquisition, and backup control. They are simpler, cheaper, and more robust than star trackers but two to three orders of magnitude less accurate. See [ADCS](./adcs.md) for the integrated control system context.

## Overview

**Coarse analog sun sensors** use photocells arranged behind a slit or aperture mask. The ratio of illumination between paired cells gives the sun's incidence angle. Accuracy is 1°–5° — sufficient for sun acquisition and power-positive safe hold. They are virtually failure-proof: no moving parts, no processor, no catalogue.

**Fine digital sun sensors** use a one- or two-dimensional photodiode array or active pixel sensor behind a precision mask. The digital readout interpolates the sun centroid to 0.01°–0.1°. Some designs use a MEMS chin-on-shoulder slit pattern for 2-axis measurement from a single sensor head.

**Earth horizon sensors** detect the infrared transition between cold space (~4 K) and the warm Earth disk (~220 K thermal infrared). A bolometer or thermopile scans across the horizon and measures the angular position of the Earth/space boundary. Constrained to Earth-pointing orbits (LEO or GEO); accuracy is 0.1°–0.5°.

## Key Parameters

| Sensor Type | Accuracy | Update Rate | Field of Regard |
|-------------|----------|-------------|-----------------|
| Coarse analog sun | 1°–5° | 10–50 Hz | Hemisphere |
| Fine digital sun | 0.01°–0.1° | 10–50 Hz | Hemisphere |
| Static IR horizon | 0.1°–0.5° | 1–5 Hz | Nadir ±15° |
| Conical scanning horizon | 0.05°–0.2° | 0.1–1 Hz | Full scan |

## Prerequisites

- Photocell or photodiode array manufacturing ([electronics](../electronics/))
- Optical filtering for infrared horizon sensors
- Calibration against known celestial references

## See Also

- [ADCS](./adcs.md) — parent capability
- [Star Trackers](./adcs.star-trackers.md) — fine attitude reference
- [Magnetorquers](./adcs.magnetorquers.md) — actuator for safe-hold mode

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
