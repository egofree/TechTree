# Optical Tracking

> **Node ID**: `space-ground-ops.range-safety.optical-tracking`
> **Domain**: [Space Ground Ops](./index.md)
> **Parent**: [Range Safety](./range-safety.md)
> **Dependencies**: [`space-ground-ops.range-safety`](./range-safety.md)
> **Outputs**: optical_tracking
> **Timeline**: Years 50+

## Overview

The non-RF, triangulation-based measurement of ascent trajectory. Deliberately diverse from
radar — cannot be jammed or spoofed, immune to RF failure — and uniquely capable of yielding
vehicle **attitude**, which radar cannot.

## Cinetheodolites

A precision theodolite (instrument measuring azimuth and elevation) fitted with a camera —
historically film, now high-frame-rate digital sensors. The exemplar is the **Contraves**
mount, deployed at ranges worldwide. A typical installation fields **two to six stations**
around the pad or along the coast, each recording the ascending vehicle against precision
angle references etched into the image.

## Triangulation

Each station yields a direction (azimuth, elevation) to the vehicle as a function of time.
Two or more observing the same event intersect in three dimensions to give position; a
sequence of frames reconstructs the trajectory. Accuracy is comparable to radar for the boost
phase, when the vehicle is close, bright, and slow enough for high-quality triangulation.

## Photogrammetry and Attitude

The shape and aspect of the vehicle in the image, fitted against a geometric model, give
pitch, yaw, and roll throughout ascent. For a post-flight anomaly investigation this is often
the decisive evidence — a staging failure captured at 1000 fps from two angles tells the
story telemetry could not.

## See Also

- [Range Safety](./range-safety.md) — parent capability
- [Range Radar](./range-safety.range-radar.md) — the RF-based cross-check
- [Optics](../optics/index.md) — theodolite and precision-mount heritage
