# Antenna Systems

> **Node ID**: `space-ground-ops.ground-stations.antenna-systems`
> **Domain**: [Space Ground Ops](./index.md)
> **Parent**: [Ground Stations](./ground-stations.md)
> **Dependencies**: [`space-ground-ops.ground-stations`](./ground-stations.md)
> **Outputs**: antenna_systems
> **Timeline**: Years 50+

## Overview

The aperture, mount, and servo system that points a dish at a moving spacecraft to within a
fraction of its beamwidth. Reference architecture: the NASA Deep Space Network.

## Aperture Classes

| Aperture | Band | Use |
|----------|------|-----|
| 12 m | S-band | LEO TT&C, launch telemetry |
| 18 m | X-band | Earth-obs downlink, GNSS ground segment |
| 34 m HEF / BWG | X, Ka, S | DSN workhorse; can be arrayed |
| 70 m BWG | X, Ka, S | weakest-signal / deepest-space targets |

## DSN Geometry

Three complexes at **~120° longitude spacing** — Goldstone (~117° W), Madrid (~4° W),
Canberra (~149° E) — keep the sky continuously visible as the Earth rotates. The
beam-waveguide (BWG) design routes the signal through reflectors to a stationary basement
feed room, so cryogenic receivers and transmitters stay put while the dish moves.

## Pointing

Az-el mount (with a zenith keyhole to steer around) or X-Y (no keyhole, more complex).
Servo control under an antenna-pointing model that corrects axis error, gravity sag, and
atmospheric refraction; residual error ~millidegrees for a 34-m at X-band.

## See Also

- [Ground Stations](./ground-stations.md) — parent capability
- [RF Front-Ends](./ground-stations.rf-front-ends.md) — the receiver behind the dish
