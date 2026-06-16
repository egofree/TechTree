# Single Event Effects Mitigation

> **Node ID**: spacecraft-systems.radiation-hardening.see-mitigation
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.radiation-hardening`](./radiation-hardening.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: radhard_electronics
> **Critical**: No

Single Event Effects (SEE) mitigation addresses instantaneous damage from individual high-energy particle strikes. Unlike TID (cumulative), SEE events are stochastic — a single particle can flip a bit or destroy a component. See [Radiation Hardening](./radiation-hardening.md) for the integrated radiation context.

## SEE Classification

| Effect | Mechanism | Consequence |
|--------|-----------|-------------|
| SEU (Upset) | Charge in memory cell | Bit flip (transient) |
| SET (Transient) | Voltage pulse in logic | Propagating glitch |
| SEL (Latchup) | Parasitic thyristor ON | Destructive short |
| SEB (Burnout) | Avalanche in power FET | Destructive |
| SEGR (Gate Rupture) | Oxide puncture | Destructive |
| SEFI (Functional Interrupt) | State machine corruption | Device reset needed |

## Mitigation Techniques

### Error Detection and Correction (EDAC)
- **Hamming SEC-DED**: 7 parity bits per 32-bit word; corrects 1-bit, detects 2-bit errors
- **Reed-Solomon (255,223)**: burst correction for mass storage pages
- **Background scrubbing**: periodic read-write every 1-10 s prevents multi-bit accumulation

### Triple Modular Redundancy (TMR)
- Three identical circuits compute in parallel; majority voter selects output (2-of-3)
- Cost: ~3.3× area; any single SEU masked by redundant modules
- Applied to: critical flip-flops, state machines, processor registers
- DICE cell: 8-transistor TMR variant for latch-level redundancy

### Other Mitigation
- **Current limiting**: series resistor on COTS ICs; trips on latchup in <1 μs
- **Latchup immunity**: SOI/SOS processes eliminate parasitic thyristors (SEL > 80 MeV·cm²/mg)
- **Watchdog timer**: hardware reset on software hang or SEFI
- **Redundant computing**: dual/triple processor strings with synchronization and voting

## Key Parameters

- **SEU onset LET**: 1-10 MeV·cm²/mg (commercial); 30-80 (rad-hard)
- **SEL immunity threshold**: > 80 MeV·cm²/mg (rad-hard); > 37 (upscreened)
- **SEU rate**: 10⁻⁷ to 10⁻¹⁰ upsets/bit/day depending on environment and process
- **Scrub interval**: 1-10 seconds (ensures <2 upsets per word between scrubs)

## See Also

- [Radiation Hardening](./radiation-hardening.md) — parent capability
- [TID Design](./radiation-hardening.tid-design.md) — complementary cumulative-dose hardening
- [Shielding Design](./radiation-hardening.shielding-design.md) — reducing particle flux at components
- [Onboard Data Handling](./obdh.md) — flight computers that use SEE mitigation

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
