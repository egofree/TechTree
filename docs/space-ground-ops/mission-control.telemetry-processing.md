# Telemetry Processing

> **Node ID**: `space-ground-ops.mission-control.telemetry-processing`
> **Domain**: [Space Ground Ops](./index.md)
> **Parent**: [Mission Control](./mission-control.md)
> **Dependencies**: [`space-ground-ops.mission-control`](./mission-control.md)
> **Outputs**: telemetry_processing
> **Timeline**: Years 50+

## Overview

The pipeline that turns raw spacecraft transfer frames into engineering parameters on a
controller's screen and into an archived record for post-flight analysis.

## Stages

1. **Frame synchronisation** — lock to the CCSDS sync pattern, recover the bit stream.
2. **Decommutation** — unpack frames → VCDUs → packets (by APID) → individual parameters,
   applying the mission database (byte offset, type, scale, units). Raw counts become
   engineering units, time-tagged with on-board time.
3. **Real-time display & limit checking** — publish to the display bus; raise yellow/red
   alarms on limit crossings, with alarm-suppression for cascading consequent flags.
4. **Archiving** — every parameter, command, voice loop, and console event written to
   long-term storage for trend analysis and anomaly reconstruction.
5. **Payload data processing** — separate science stream delivered to the payload operations
   centre for level-0 → level-1 calibration.

## See Also

- [Mission Control](./mission-control.md) — parent capability
- [MCC Facilities](./mission-control.mcc-facilities.md) — the consoles the pipeline feeds
