# Satellite Antennas

> **Node ID**: spacecraft-systems.comms-payload.antennas
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.comms-payload`](./comms-payload.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: satellite_antennas, comms_payloads
> **Critical**: No

The satellite antenna system shapes the coverage footprint and determines the EIRP distribution across the service area. It is the most visible payload element — a commsat's reflector diameter and feed count largely determine its capacity and coverage map. See [Communications Payload](./comms-payload.md) for the integrated payload context.

## Architectures

Four antenna families serve modern commsats. **Reflector antennas** (single or dual offset-fed parabolic) dominate GEO commsats, with 1-3 m shaped reflectors casting beams onto specific landmasses. **Phased arrays** of hundreds to thousands of radiating elements steer multiple beams electronically, essential for LEO constellations that must track ground terminals from a moving satellite. **Horn and helix antennas** provide global-beam coverage and circular-polarised mobile services. **Deployable mesh reflectors** (5-30 m unfurlable) enable high-gain beams at low frequencies where a rigid reflector would not fit inside a fairing.

## Key Parameters

- **Reflector diameter**: 0.8-3 m (fixed), 5-30 m (deployable mesh)
- **Surface accuracy**: λ/100 RMS (30 µm at Ku-band, 17 µm at Ka-band)
- **Phased array elements**: 120-2,000 per aperture
- **Beamwidth**: 0.5° (HTS spot) to 17° (global beam)
- **Scan range**: ±45 to ±60° from boresight (phased array)
- **Polarisation**: linear (CP vs LP) or dual-polarisation (XPD > 30 dB)
- **Feed losses**: 0.5-1.5 dB (waveguide run from OMUX)
- **Reflector material**: carbon-fibre composite skin on Al honeycomb, vacuum-deposited Al coating

## Prerequisites

- Precision reflector manufacture (machine tools, composite layup)
- Feed horn and waveguide fabrication from [Metals](../metals/index.md)
- Surface coating via [vacuum deposition](../vacuum/deposition-systems.md)

## See Also

- [Communications Payload](./comms-payload.md) — parent capability
- [Traveling-Wave Tube Amplifiers](./comms-payload.traveling-wave-tubes.md) — feeds the antenna via OMUX
- [RF Multiplexers](./comms-payload.multiplexers.md) — output filtering into the antenna feed
- [TT&C Systems](./ttac.md) — TT&C antennas (separate omnidirectional coverage)

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
