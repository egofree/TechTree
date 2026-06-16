# RF Multiplexers

> **Node ID**: spacecraft-systems.comms-payload.multiplexers
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.comms-payload`](./comms-payload.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: comms_payloads
> **Critical**: No

The input multiplexer (IMUX) and output multiplexer (OMUX) filter and combine the transponder channels. The IMUX sits after the receiver and splits the uplink into individual channels for amplification; the OMUX sits after the TWTAs and combines the amplified downlink channels into a single waveguide to the antenna. Both are critical to channel isolation and spectral efficiency. See [Communications Payload](./comms-payload.md) for the integrated payload context.

## Architecture

Each multiplexer channel is a waveguide cavity filter — typically 6-8 coupled cylindrical cavities operating in TE₁₁₃ mode, with coupling irises machined to set the filter response. The cavities are CNC-machined from 6061-T6 aluminium, silver-plated (5 µm) for low surface resistance, and tuned on a vector network analyser to within 0.05 dB of the target response. The OMUX must handle 50-300 W per channel without multipactor breakdown — a resonant vacuum discharge that occurs when secondary electron emission produces an electron avalanche in high-RF-field gaps. OMUX cavities are designed with gaps large enough and surfaces passivated to push the multipactor threshold above operating power, then vacuum-tested at 1.5× rated power.

## Key Parameters

- **Channel count**: 24-60 (legacy GEO), 60+ (VHTS)
- **Channel bandwidth**: 26-72 MHz (legacy), 125-500 MHz (HTS)
- **Insertion loss**: IMUX 1-2 dB, OMUX 0.3-0.6 dB
- **Adjacent rejection**: 20-35 dB
- **Cavity count per channel**: 6-8 (TE₁₁₃ mode)
- **OMUX power handling**: 50-300 W per channel (multipactor margin > 6 dB)
- **Material**: 6061-T6 aluminium, silver-plated (5 µm), invar for thermal stability
- **Mass per channel**: 0.08 kg (IMUX), 0.15 kg (OMUX)
- **Temperature range**: -5 to +45°C (IMUX), 0 to +95°C (OMUX, heated by TWTA output)
- **Tuning**: vector network analyser, 0.05 dB target response match

## Prerequisites

- Precision waveguide machining from [Metals](../metals/index.md)
- Silver plating and surface passivation
- Multipactor vacuum testing capability

## See Also

- [Communications Payload](./comms-payload.md) — parent capability
- [Communications Transponders](./comms-payload.transponders.md) — sits between IMUX and OMUX
- [Traveling-Wave Tube Amplifiers](./comms-payload.traveling-wave-tubes.md) — feeds the OMUX
- [Satellite Antennas](./comms-payload.antennas.md) — receives the combined OMUX output

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
