# Navigation Signal Generation

> **Node ID**: spacecraft-systems.navigation-payload.signal-generation
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.navigation-payload`](./navigation-payload.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: pnt_payloads
> **Critical**: No

Navigation signal generation produces the spread-spectrum signals broadcast by GNSS satellites. The atomic clock reference drives PRN code generators and navigation message modulators, producing the L-band signals that receivers correlate to determine pseudorange. See [Navigation & PNT Payloads](./navigation-payload.md) for the integrated navigation context.

## Architecture

The signal chain begins with the 10.23 MHz atomic clock reference. A frequency synthesis unit (FSU) derives integer-multiple L-band carriers (L1 = 154×, L2 = 120×, L5 = 115×). The navigation baseband unit generates PRN spreading codes, multiplexes them with the navigation message, and modulates the carriers. Solid-state power amplifiers boost each signal to ~50 W before the phased-array antenna.

## Key Components

1. **Frequency synthesis unit (FSU)**: phase-coherent multiplier chain from 10.23 MHz to L-band carriers
2. **PRN code generator**: shift-register-based or memory-based pseudo-random noise code sequences, unique per satellite and signal
3. **Navigation message modulator**: 50 bps (legacy) to 500 bps (modern) data with FEC encoding
4. **SSPA / TWTA**: solid-state or travelling-wave-tube power amplifiers, 50-250 W per signal

## Key Parameters

- **Carrier frequencies**: L1 (1575.42 MHz), L2 (1227.60 MHz), L5 (1176.45 MHz)
- **Code rates**: 1.023 Mchips/s (C/A), 10.23 Mchips/s (P, L5)
- **Modulation**: BPSK, BOC, MBOC, AltBOC
- **Transmit power**: 50 W (L1 C/A) to 250 W (L5)
- **Bandwidth**: 2-24 MHz per signal
- **Navigation message rate**: 25-500 bps

## See Also

- [Navigation & PNT Payloads](./navigation-payload.md) — parent capability
- [Electronics](../electronics/index.md) — RF signal generation and modulation
- [Radio Communications](../telecom/radio.md) — spread-spectrum and RF heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
