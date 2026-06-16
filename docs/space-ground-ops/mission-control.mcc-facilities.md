# MCC Facilities

> **Node ID**: `space-ground-ops.mission-control.mcc-facilities`
> **Domain**: [Space Ground Ops](./index.md)
> **Parent**: [Mission Control](./mission-control.md)
> **Dependencies**: [`space-ground-ops.mission-control`](./mission-control.md)
> **Outputs**: mcc_facilities
> **Timeline**: Years 50+

## Overview

The mission control centre facility: the console positions, backrooms, and support spaces
that house a 24/7 flight operations team. The ISS MCC at NASA Johnson Space Center mans
**~30–50 front-room positions** during crewed operations, each a multi-screen console cluster
for a named discipline (FLIGHT, CAPCOM, PROP, GNC, EPS, ECLSS, COMM, SURGEON, …).

## Layout

| Area | Role |
|------|------|
| Front room (consoles) | real-time operations, the operational authority |
| Backroom (MAT / specialists) | deeper analysis, history plots, offline modelling |
| Flight dynamics | orbit determination, manoeuvre design, conjunction screening |
| Operations planning | timeline build, command-load generation |
| Simulation / training | crew and controller rehearsal facility |

## Voice Loops

Party-line conferences with strict transmit/monitor discipline. The flight director's loop is
authoritative; each subsystem has its own; CAPCOM alone talks to the crew. Loops are recorded
as part of the mission archive.

## See Also

- [Mission Control](./mission-control.md) — parent capability
- [Telemetry Processing](./mission-control.telemetry-processing.md) — the data pipeline feeding consoles
