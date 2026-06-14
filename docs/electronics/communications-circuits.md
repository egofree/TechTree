# Communications Circuits

> **Node ID**: electronics.communications-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.electrical-systems`](electrical-systems.md), [`electronics.passive-components`](passive-components.md)
> **Timeline**: Years 25-50
> **Outputs**: communication-circuit-design
> **Critical**: No — communications circuits extend electronics into wireless and wired information transfer, but they are not on the minimum-viable bootstrap critical path

Communications circuits transmit and receive information by impressing a signal onto a carrier. This capability owns the **Tesla-era AC/RF lineage** — the thread that begins with Nikola Tesla's pioneering work on alternating current, resonant transformers (Tesla coils), and radio-frequency tuning, and runs through Forrest Mims III's *Communications Projects* to modern modulation, oscillator, and receiver design. It is the design-pedagogy hub, not a deep article.

The Tesla grounding matters because RF is fundamentally an AC phenomenon: resonant LC circuits, impedance, and phase — the tools of [AC circuit analysis](electrical-systems.md) — are what make a tuned circuit select one station out of the ether. Every radio receiver is, at its core, a Tesla-era resonant tank circuit followed by a detector.

## Learning Progression

The family follows the natural signal chain of a communications link — each stage prepares the signal for the next:

```
 Modulation        RF Oscillator        Receiver
 Circuits    →     Circuits       →     Circuits
 (impress info     (generate the        (select, amplify,
  on a carrier)     RF carrier)          detect the signal)
     │                  │                     │
     ▼                  ▼                     ▼
 AM / FM / mixing   LC / crystal tank    tuned RF amp + detector
 envelope detector  Barkhausen criterion superheterodyne (intro)
 transmitter blocks frequency stability   AGC, selectivity
```

1. **[Modulation circuits](communications-circuits.modulation-circuits.md)** — How information (voice, data) rides on a carrier. Teaches AM modulation and envelope-detector demodulation, FM with varactor tuning and a phase-locked-loop (PLL) introduction, and frequency-conversion mixers. The key concept is the **modulation index** and the trade-off between signal-to-noise and bandwidth. This is the Mims *Communications Projects* entry point.
2. **[RF-oscillator circuits](communications-circuits.rf-oscillator-circuits.md)** — How the carrier itself is generated. Teaches LC oscillators (Colpitts, Hartley), crystal oscillators (Pierce) for frequency stability, and the Barkhausen criterion for sustained oscillation. This builds on the general [oscillator circuits](analog-circuits.oscillator-circuits.md) family but emphasizes frequency stability, phase noise, and tuning range — the RF-specific concerns.
3. **[Receiver circuits](communications-circuits.receiver-circuits.md)** — How a weak RF signal is selected from a crowded spectrum and recovered. Teaches tuned RF amplification, the superheterodyne architecture (introductory level), envelope/product detection, and automatic gain control (AGC). The key concept is **selectivity** — separating the desired signal from adjacent channels.

## Scope Boundary — Mims Level Only

This capability stays at the **Forrest Mims III / introductory level**. It deliberately does **not** cover:

- Smith charts and impedance-matching network synthesis
- Phased-array and beamforming antenna systems
- Digital modulation constellations (QAM, PSK) beyond a mention
- Software-defined radio (SDR) architecture

Those advanced topics belong to a specialized RF engineering track well beyond the bootstrap horizon. Here we teach enough to build a working AM/FM receiver, a simple transmitter, and an IR or low-band wireless data link — the Mims *Communications Projects* scope.

## Why It Matters

Communications circuits are the foundation for:

- **Wireless telemetry and control** — the lowest-complexity way to command a remote sensor or actuator without a physical wire run.
- **Broadcast information** — radio is the classic one-to-many communications medium, achievable early in the electronics bootstrap once resonant LC circuits and detectors exist.
- **Spectrum as a shared resource** — understanding modulation, bandwidth, and selectivity is prerequisite to any organized use of the electromagnetic spectrum.

## Prerequisites

- [Electrical Systems](electrical-systems.md) — AC theory, transformers, and resonance are the substrate of every RF circuit. The tuned LC tank is a Tesla-era invention.
- [Passive Components](passive-components.md) — inductors and capacitors set the resonant frequency; their construction quality and tolerance directly determine oscillator stability and receiver selectivity.
- AC circuit analysis (phasors, reactance, impedance, resonance) — covered under the circuit-fundamentals track.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](./index.md)*
