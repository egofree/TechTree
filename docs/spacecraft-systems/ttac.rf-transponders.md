# RF Transponders

> **Node ID**: spacecraft-systems.ttac.rf-transponders
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.ttac`](./ttac.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: ttac_systems
> **Critical**: No

The RF transponder is the spacecraft's radio: it receives the uplink, demodulates commands and ranging, and generates the downlink carrier modulated with telemetry. See [TT&C Systems](./ttac.md) for the integrated communications context.

## Architecture

Two architectures dominate. The **bent-pipe** (transparent) transponder coherently translates the uplink carrier to the downlink frequency via a phase-locked loop (PLL), preserving the phase relationship for two-way Doppler. The **regenerative** transponder fully demodulates the uplink, decodes digital data, and re-encodes it for the downlink, breaking noise coupling between links.

## Key Components

1. **Receiver front-end**: low-noise amplifier (LNA), typically GaAs or InP HEMT with NF < 1.5 dB
2. **Downconverter**: mixes RF to intermediate frequency (IF), typically 10-200 MHz
3. **PLL / carrier tracking**: Costas loop or squaring loop for BPSK/QPSK demodulation
4. **Turn-around ratio synthesizer**: generates coherent downlink from uplink reference (e.g., 880/749 for X-band)
5. **Modulator**: BPSK/QPSK modulator on downlink, driven by telemetry formatting hardware
6. **Power amplifier**: solid-state power amplifier (SSPA, 1-20 W) or traveling-wave tube amplifier (TWTA, 20-200 W)

## Key Parameters

- **Frequency bands**: S-band (2.2-2.3 GHz), X-band (8.4-8.5 GHz), Ka-band (25.5-27.0 GHz)
- **Receiver sensitivity**: -150 to -160 dBW (threshold for 10⁻⁶ BER)
- **Transmit power**: 5 W (SSPA) to 200 W (TWTA)
- **Turn-around ratio**: 240/221 (S), 880/749 (X), 3344/2849 (Ka)
- **Phase noise**: <-90 dBc/Hz at 10 kHz offset
- **Mass**: 1-5 kg typical; power: 10-50 W DC

## See Also

- [TT&C Systems](./ttac.md) — parent capability
- [Telemetry Formatting](./ttac.tm-formatting.md) — CCSDS packetization feeding the modulator
- [Ground Link Budget](./ttac.ground-link-budget.md) — link margin engineering
- [Radio Communications](../telecom/radio.md) — RF circuit heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
