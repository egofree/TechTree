# Communications Transponders

> **Node ID**: spacecraft-systems.comms-payload.transponders
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.comms-payload`](./comms-payload.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: comms_payloads
> **Critical**: No

The communications transponder is the frequency-conversion and channel-routing core of the satellite payload. It receives the uplink, filters it into individual channels via the input multiplexer, translates each channel to the downlink frequency, and feeds the amplified signal to the output multiplexer and antenna. See [Communications Payload](./comms-payload.md) for the integrated payload context.

## Architecture

Three transponder architectures dominate. The **bent-pipe** (transparent) transponder coherently mixes the uplink to the downlink using a fixed local oscillator (e.g., 2225 MHz for C-band, 1750 MHz for Ku), preserving phase for any modulation type. The **regenerative** transponder demodulates the uplink to baseband, decodes, switches, and re-encodes — enabling independent link optimisation and mesh connectivity without hub double-hop. The **digital channeliser** splits the uplink into narrow subchannels (1.25 MHz), routes each independently between beams, and recombines for the downlink — providing flexible bandwidth allocation across a multi-beam HTS payload.

## Key Parameters

- **Frequency translation**: C 2225 MHz, Ku 1750 MHz, Ka 2350 MHz (typical)
- **Channel bandwidth**: 36 MHz (legacy broadcast), 72 MHz (wideband), 125-500 MHz (HTS spot)
- **Channel count**: 24 (legacy GEO) to 60+ (VHTS)
- **Receiver noise figure**: 1.2-2.0 dB (GaAs HEMT LNA), 0.8-1.5 dB (InP HEMT)
- **LO phase noise**: <-90 dBc/Hz at 10 kHz offset
- **Group delay flatness**: ±5 ns across 80% of passband
- **Power consumption**: 15-40 W DC per receiver, plus LO/distribution
- **Mass**: 3-8 kg per redundant receiver pair

## Prerequisites

- RF circuit heritage from [Radio Communications](../telecom/radio.md)
- Mixed-signal ICs and GaN/GaAs amplifiers from [Electronics](../electronics/index.md)
- Local oscillator stability from crystal/atomic references (coherent turn-around ratios)

## See Also

- [Communications Payload](./comms-payload.md) — parent capability
- [Traveling-Wave Tube Amplifiers](./comms-payload.traveling-wave-tubes.md) — downstream power amplification
- [RF Multiplexers](./comms-payload.multiplexers.md) — channel filtering before and after transponder
- [TT&C RF Transponders](./ttac.rf-transponders.md) — separate TT&C transponder (command link)

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
