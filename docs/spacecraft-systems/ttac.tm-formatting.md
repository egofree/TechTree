# Telemetry Formatting

> **Node ID**: spacecraft-systems.ttac.tm-formatting
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.ttac`](./ttac.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: ttac_systems
> **Critical**: No

Telemetry formatting converts raw source data from spacecraft subsystems and instruments into standardized CCSDS packets and transfer frames suitable for RF downlink. See [TT&C Systems](./ttac.md) for the integrated communications context.

## CCSDS Protocol Stack

The formatting chain follows the CCSDS telemetry protocol stack:

1. **Source packets** (CCSDS 133.0-B): variable-length packets with 6-byte primary header identifying APID (Application Process ID), sequence count, and data length
2. **Transfer frames** (CCSDS 132.0-B): fixed-length containers (1115 or 2237 bytes) that multiplex packets from multiple APIDs; header carries spacecraft ID and virtual channel ID
3. **Channel coding**: convolutional (r=1/2, k=7), Reed-Solomon (255,223), Turbo, or LDPC coding applied to transfer frames
4. **Synchronization**: attached sync marker (ASM) — 32-bit pattern prepended to each coded frame for receiver lock

## Key Parameters

- **Source packet size**: 7-65542 bytes (variable)
- **Transfer frame size**: 1115 or 2237 bytes (fixed per mission)
- **Virtual channels**: up to 8 per physical channel (VCID 0-7)
- **APID range**: 0-2047 (11-bit), 0-127 typically reserved, 128-2047 for user-defined
- **Coding overhead**: 7.8% (RS only), 50% (convolutional), 14-40% (Turbo/LDPC depending on rate)
- **Throughput**: 1 kbps to 1 Gbps depending on link and hardware

## Virtual Channel Multiplexing

Virtual channels allow prioritized data streams on one physical RF link:

- VC0: real-time housekeeping telemetry (high priority, low latency)
- VC1: stored science data (bulk, best-effort)
- VC2: event data (anomaly reports, medium priority)
- VC3: fill data (idle pattern when no other data available)

## See Also

- [TT&C Systems](./ttac.md) — parent capability
- [RF Transponders](./ttac.rf-transponders.md) — modulator that transmits formatted frames
- [Mass Storage](./obdh.mass-storage.md) — buffers science data before formatting

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
