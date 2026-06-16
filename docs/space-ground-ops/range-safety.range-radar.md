# Range Radar

> **Node ID**: `space-ground-ops.range-safety.range-radar`
> **Domain**: [Space Ground Ops](./index.md)
> **Parent**: [Range Safety](./range-safety.md)
> **Dependencies**: [`space-ground-ops.range-safety`](./range-safety.md)
> **Outputs**: range_radar
> **Timeline**: Years 50+

## Overview

The C-band metric tracking radar that measures a launch vehicle's actual trajectory during
ascent and compares it, in real time, against the destruct-line envelope.

## AN/FPS-16

The exemplar instrument: an instrumented tracking radar developed in the 1950s, transmitting
at **~5.4–5.9 GHz**, skin-tracking the vehicle's hull echo (no transponder needed). Delivers
range, azimuth, elevation accurate to a few metres and a fraction of a milliradian. Skin-track
is valuable because it works on a dead or unresponsive rocket just as well as a healthy one;
at longer range a vehicle-borne C-band transponder beacon extends the track.

| Radar | Role |
|-------|------|
| AN/FPS-16 | precision metric track (workhorse since 1950s) |
| AN/FPQ-6 / FPQ-16 | higher-accuracy successors |
| Multi-object tracking radar | debris tracking after termination |

## Tracking Servo

Kalman-filter predictor keeps the antenna ahead of the vehicle during high-g ascent; staging
briefly doubles the target and may drop lock, recovered in seconds if the predictor holds the
estimated trajectory through the gap.

## Impact Prediction

Multiple radars (a range fields two or more for geometry and redundancy) feed a real-time
trajectory filter. From the state vector the filter propagates the **instantaneous impact
point** — where the vehicle would land if thrust ceased now — and plots it against the
destruct lines. A crossing commits the range to action in seconds.

## See Also

- [Range Safety](./range-safety.md) — parent capability
- [Optical Tracking](./range-safety.optical-tracking.md) — RF-independent cross-check
- [Flight Termination](./range-safety.flight-termination.md) — the action triggered
