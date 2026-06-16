# Radiation Hardening

> **Node ID**: spacecraft-systems.radiation-hardening
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`silicon`](../silicon/index.md),
> [`ehs.radiation-safety`](../ehs/radiation-safety.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: radhard_electronics
> **Critical**: No — radiation hardening is what makes space electronics survive. A commercial microprocessor in low Earth orbit will fail within hours from total ionizing dose or single-event latchup. Hardening adds cost, complexity, and 10-15 years of performance lag behind commercial silicon, but without it no spacecraft flies

The space radiation environment is hostile to semiconductors in ways that terrestrial electronics never encounter. Energetic protons and electrons trapped in planetary radiation belts, solar flare particles, and galactic cosmic rays deposit charge in transistor gates, shift threshold voltages, flip memory bits, and — in extreme cases — short-circuit and destroy components. Radiation hardening is the discipline of designing electronics that survive this bombardment for the mission lifetime: typically 1-15 years in orbit, sometimes decades for interplanetary probes.

This article covers three process areas: [total ionizing dose (TID) design](./radiation-hardening.tid-design.md) (cumulative degradation from trapped particles), [single event effects (SEE) mitigation](./radiation-hardening.see-mitigation.md) (instantaneous damage from individual particle strikes), and [shielding design](./radiation-hardening.shielding-design.md) (aluminum-equivalent mass that reduces the dose at the component level). The [silicon](../silicon/index.md) domain provides the semiconductor fabrication processes; [radiation safety](../ehs/radiation-safety.md) provides the environmental knowledge base for radiation effects on biological and electronic systems.

## Overview

Radiation damage in semiconductors occurs through two fundamentally different mechanisms. **Total Ionizing Dose (TID)** is cumulative: each particle deposits a small amount of charge in the gate oxide, gradually shifting transistor threshold voltages until the device stops functioning. **Single Event Effects (SEE)** are instantaneous: a single high-energy particle deposits enough charge in a sensitive node to cause a transient pulse, a bit flip, or a destructive short circuit. The two mechanisms require different mitigation strategies and are tested separately.

A typical low-Earth-orbit mission at 600 km altitude accumulates 5-20 krad/year behind 2.5 mm aluminum shielding. A Jupiter mission like Juno encounters 20,000 krad (20 Mrad) over its lifetime. Designing for these environments requires understanding both the particle environment and the failure modes of each component technology.

## Radiation Environments

### Trapped Radiation Belts (Van Allen)

The Earth's magnetosphere traps energetic protons (1-500 MeV) and electrons (0.1-10 MeV) in two toroidal belts:

- **Inner belt** (1,000-12,000 km): dominated by high-energy protons (up to 500 MeV), peak dose ~100 krad/year behind 2.5 mm Al
- **Outer belt** (13,000-60,000 km): dominated by electrons (up to 10 MeV), peak dose ~1,000 krad/year behind 2.5 mm Al
- **South Atlantic Anomaly (SAA)**: dip in the inner belt where it dips to ~200 km altitude; LEO satellites pass through it 3-6 times per day, receiving 90% of their total dose in 5% of orbit time

### Solar Particle Events (SPE)

Solar flares and coronal mass ejections produce bursts of protons (10-500 MeV) and heavier ions:

- **Typical event**: 10⁷-10⁹ protons/cm² over 24-72 hours (10-100 krad behind 2.5 mm Al)
- **Carrington-class event**: 10× typical, potentially lethal to unshielded astronauts
- **Frequency**: ~3-10 major events per year during solar maximum, rare during solar minimum
- **Prediction**: 12-48 hours warning via solar observatories (SOHO, STEREO, DSCOVR)

### Galactic Cosmic Rays (GCR)

Originate outside the solar system; consist of fully ionized nuclei from protons to iron (and beyond):

- **Flux**: ~2-5 particles/cm²/s (modulated by solar cycle, lower during solar max)
- **Energy**: 100 MeV/nucleon to >10 GeV/nucleon
- **LET spectrum**: peaks at 0.1-1 MeV·cm²/mg; rare heavy ions (Fe, Z>26) up to 30 MeV·cm²/mg
- **Shielding**: practically impossible to stop — 10 cm of aluminum barely attenuates GCR flux
- **Effect**: single event upsets dominate; contributes ~1 SEU/bit/day in SRAM

## Total Ionizing Dose (TID)

### Mechanism

Ionizing radiation deposits electron-hole pairs in the SiO₂ gate oxide of MOS transistors. Holes are trapped near the Si/SiO₂ interface, causing a gradual positive threshold voltage shift in n-channel devices and negative shift in p-channel devices. At sufficient dose, the transistor's threshold voltage exits the operating range and the device fails:

1. **Hole generation**: radiation creates ~8×10¹² electron-hole pairs per rad(Si) per cm³ of SiO₂
2. **Hole transport**: holes drift to the Si/SiO₂ interface (μs to seconds depending on oxide field)
3. **Trap buildup**: fraction of holes are trapped at interface states (permanent, anneals slowly at T>100°C)
4. **Threshold shift**: ΔVth = -Q_ox / C_ox (shifts NMOS toward depletion, PMOS toward enhancement)
5. **Leakage increase**: parasitic field-oxide transistors turn on, increasing standby current

### Dose Levels

| Environment | Dose rate | Annual dose (2.5mm Al) | Design target |
|-------------|-----------|----------------------|---------------|
| LEO polar (600 km) | 1-5 krad/yr | 3-10 krad | 20-30 krad |
| LEO equatorial (ISS, 400 km) | 0.1-1 krad/yr | 0.5-3 krad | 10 krad |
| GEO (geostationary) | 5-50 krad/yr | 10-50 krad | 100-300 krad |
| GPS (20,200 km) | 10-100 krad/yr | 30-100 krad | 300-1000 krad |
| Jupiter orbit | 1,000-10,000 krad/mission | — | 1-30 Mrad |
| Lunar surface | 0.5-5 krad/yr | 1-5 krad | 20 krad |

### Rad-Hard Process Technologies

- **SOI (Silicon-on-Insulator)**: thin device silicon layer on buried SiO₂; isolates transistor body from substrate, reducing parasitic paths and TID sensitivity. 100-1000× improvement over bulk CMOS. LEON3 and RAD750 use SOI.
- **SOS (Silicon-on-Sapphire)**: device silicon on crystalline sapphire substrate; even better isolation than SOI but higher defect density. Used in legacy RH1750 processors.
- **SiGe (Silicon-Germanium) HBT**: heterojunction bipolar transistors with inherent TID tolerance up to 1-5 Mrad without design changes. Used in high-frequency RF transponders.
- **Bulk CMOS with guard rings**: commercial CMOS with added layout features (annular transistors, guard bands) that improve TID tolerance to 30-100 krad at no processing cost premium

### Design margins

Standard practice requires 2× dose margin: if the mission predicts 50 krad at end-of-life behind the chosen shielding, components are qualified to 100 krad minimum. For critical components (processor, memory, bus controller), 3× margin (150 krad) is common.

### TID Failure Modes

The progression of TID degradation follows a predictable pattern:

1. **Threshold voltage shift**: NMOS Vth decreases (device turns on easier); PMOS Vth increases (harder to turn on)
2. **Leakage current increase**: standby power rises as field-oxide transistors begin conducting
3. **Timing margin erosion**: gate propagation delay increases as drive current drops
4. **Functional failure**: logic threshold crossed; transistor stuck ON or OFF permanently

The failure threshold depends on process node: older technologies (0.35 μm, 0.5 μm) survive 50-300 krad before failure; modern deep-submicron (28 nm) may fail at 10-30 krad due to ultra-thin gate oxides. Paradoxically, SOI variants of the same node can survive 1 Mrad or more.

## Single Event Effects (SEE)

A single high-energy particle traversing a semiconductor deposits charge along its track. If the track passes through a sensitive junction (drain of an OFF transistor, reverse-biased PN junction), the collected charge can cause transient or permanent effects:

### SEE Classification

| Effect | Abbreviation | Mechanism | Consequence | Duration |
|--------|-------------|-----------|-------------|----------|
| Single Event Upset | SEU | Charge collected in memory cell or flip-flop | Bit flip (0→1 or 1→0) | Transient |
| Single Event Transient | SET | Voltage pulse in combinational logic | Propagates, may latch | Transient |
| Single Event Latchup | SEL | Parasitic thyristor turns on | Destructive short circuit | Permanent (unless power-cycled) |
| Single Event Burnout | SEB | Avalanche breakdown in power MOSFET | Destructive | Permanent |
| Single Event Gate Rupture | SEGR | Gate oxide puncture in power MOSFET | Destructive | Permanent |
| Single Event Functional Interrupt | SEFI | State machine corruption in complex IC | Device enters undefined state | Requires reset |

### SEE Rates

The rate of single event upsets depends on the LET (Linear Energy Transfer) spectrum at the component location and the component's critical charge (Qcrit):

- **Cross-section**: σ_SEU(L) — measured in cm²/bit, function of particle LET
- **Onset LET**: LET threshold at which upsets begin (typical: 1-10 MeV·cm²/mg for commercial, 30-80 for rad-hard)
- **Saturated cross-section**: σ_∞ — plateau upset cross-section (typical: 10⁻⁷ to 10⁻¹⁰ cm²/bit)
- **SEU rate**: R = Φ × σ_∞, where Φ is particle flux (particles/cm²/s)

For a commercial SRAM in GEO: Φ_GCR ≈ 2 particles/cm²/s, σ ≈ 10⁻⁷ cm²/bit → R ≈ 2×10⁻⁷ upsets/bit/s = ~0.017 upsets/bit/day = 17,000 upsets/day for a 1 MB memory.

### Worked Example: SEU Budget for a LEO Satellite

A 1 MB flight computer SRAM in a 600 km sun-synchronous orbit behind 4 mm Al shielding:

1. **Environment**: SAA passage delivers 90% of trapped-proton flux; effective flux Φ_eff ≈ 50 protons/cm²/s (average over orbit including SAA passes)
2. **Component**: commercial SRAM, σ_∞ = 5×10⁻⁸ cm²/bit, onset LET = 2.5 MeV·cm²/mg
3. **SEU rate**: R = 50 × 5×10⁻⁸ = 2.5×10⁻⁶ upsets/bit/s = 0.22 upsets/bit/day
4. **Daily upsets**: 0.22 × 8×10⁶ bits ≈ 1,740 upsets/day
5. **With Hamming SEC-DED**: all single-bit upsets corrected; double-bit errors (P²/2) ≈ 0.02/day → one uncorrectable error every ~50 days
6. **Mitigation**: add scrubbing every 10 s → worst-case 2 upsets in same word before scrub = negligible double-bit risk

This demonstrates why EDAC + scrubbing is mandatory even for LEO missions.

### SEE Mitigation Techniques

**Error Detection and Correction (EDAC)**:
- **Hamming code** (SEC-DED — Single Error Correction, Double Error Detection): adds 7 parity bits per 32-bit word; corrects any single-bit error, detects double-bit errors. Standard for SRAM in space computers.
- **Reed-Muller code**: higher correction capability; used for critical register files
- **Reed-Solomon (255, 223)**: burst-error correction; used for mass storage pages
- **Implementation**: hardware EDAC controller transparently corrects reads; background scrubber periodically reads and rewrites every memory location to prevent multi-bit accumulation

**Triple Modular Redundancy (TMR)**:
- Three identical logic circuits compute the same function in parallel
- A majority voter selects the output (2-of-3 wins)
- Any single SEU in one module is masked by the other two
- Cost: 3× area + voter overhead (~3.3× total)
- Applied to: critical flip-flops, state machines, processor registers
- DICE (Dual Interlocked Cell): a TMR variant using only 8 transistors per latch (vs 6 for standard)

**Other mitigation**:
- **Scrubbing**: periodic memory read-write cycle to correct accumulated upsets before they become multi-bit (typical: every 1-10 seconds, depends on SEU rate and code word size)
- **Current limiting**: series resistor or current-limited regulator on each COTS IC; prevents latchup from drawing destructive current (response in <1 μs)
- **Latchup immunity**: rad-hard processes (SOI, SOS) eliminate parasitic thyristors entirely; SEL threshold > 80 MeV·cm²/mg
- **Watchdog timer**: hardware counter that resets the processor if software fails to service it; catches SEFI events and software hangs
- **Redundant computing**: dual or triple redundant processor strings with periodic synchronization; voting masks single-processor failures

## Shielding Design

### Aluminum Equivalent

Spacecraft electronics are housed inside an aluminum structure that provides passive shielding. The thickness varies by location: outer walls (2-4 mm), internal bays (1-3 mm), spot shields around sensitive components (5-10 mm added).

| Shielding (mm Al) | LEO dose (1yr) | GEO dose (1yr) | Jupiter dose (1yr) |
|-------------------|----------------|----------------|---------------------|
| 1 mm | 10-30 krad | 100-500 krad | 5,000+ krad |
| 2.5 mm | 3-10 krad | 30-100 krad | 1,000-5,000 krad |
| 5 mm | 1-5 krad | 10-50 krad | 500-2,000 krad |
| 10 mm | 0.5-2 krad | 5-20 krad | 200-1,000 krad |
| 20 mm | 0.2-1 krad | 2-10 krad | 100-500 krad |

### Dose-Depth Curves

The dose-depth curve shows total dose vs. aluminum shielding thickness for a given orbit. It follows a power law at low thickness (proton attenuation) and flattens at high thickness (secondary radiation from electron bremsstrahlung limits further improvement). Key features:

- **Knee**: the shielding thickness where adding material yields diminishing returns (typically 3-8 mm Al for most orbits)
- **Bremsstrahlung limit**: high-Z materials (tantalum, tungsten) generate more secondary radiation than they stop; aluminum (low-Z) is preferred
- **Graded-Z shielding**: layering low-Z (outer) → high-Z (inner) minimizes secondary radiation; sometimes used for detector shielding

### Spot Shielding

For specific sensitive components (e.g., the flight processor), localized shielding (tantalum or tungsten patches) can reduce the dose by 2-5× at the component level:

- **Tantalum dome**: 2-5 mm Ta over the processor package (density 16.6 g/cm³, 2× Al effectiveness)
- **Tungsten inserts**: 1-2 mm W in critical bays (density 19.3 g/cm³)
- **Mass cost**: 50-500 g per component — significant for small satellites, minor for large platforms
- **Trade-off**: spot shielding is most effective for small-volume sensitive components (processors, FPGAs); less practical for large memory arrays

## Parts Classification

| Category | Description | TID rating | SEE | Cost | Example |
|----------|-------------|-----------|-----|------|---------|
| Rad-hard (RH) | Designed and processed for radiation | 1 Mrad+ | SEL >100 MeV·cm²/mg | $100K+ | RAD750, AT697F |
| Rad-tolerant | Commercial process with hardening | 100-300 krad | SEL >75 MeV·cm²/mg | $1K-10K | Actel RTAX-S FPGA |
| COTS-upscreened | Commercial, 100% lot-tested | 30-100 krad | SEL >37 MeV·cm²/mg | $100-1K | Industrial-grade ICs |
| COTS | Commercial off-the-shelf | 5-30 krad | SEL possible at 10-30 | $1-100 | Standard commercial ICs |

The RAD750 processor costs approximately $200,000 per unit and takes 18-24 months from order to delivery. A commercial PowerPC 750 (same architecture) costs $5 and ships in 2 weeks. This 40,000× cost differential and 50× lead time gap define the boundary of what is economically feasible for space missions.

## Design Margins and Qualification

Standard radiation qualification requires:

1. **TID testing**: Cobalt-60 gamma source irradiates samples to 2× mission dose at representative bias and temperature
2. **SEE testing**: particle accelerator (cyclotron) bombards samples with protons and heavy ions at various LETs
3. **Post-irradiation testing**: electrical parametric measurements within 1 hour (and at 24 hours, for annealing assessment)
4. **Post-irradiation testing**: electrical parametric measurements within 1 hour (and at 24 hours, for annealing assessment)
5. **Lot acceptance**: 100% screening for Class V (space) parts; sample testing for Class S
6. **Margin verification**: components must pass at 1.5-2× mission dose with <10% parametric degradation

## Troubleshooting

| Symptom | Likely cause | Diagnostic action |
|---------|-------------|-------------------|
| Standby current increasing over time | TID-induced leakage in field oxide | Measure IDDQ vs dose; plan replacement if >2× initial |
| Random bit flips in SRAM | GCR-induced SEU | Check EDAC correction rate; verify scrubber is active |
| Destructive component failure | SEL in COTS part | Add current limiter; switch to rad-hard or SOI part |
| Intermittent processor hang | SEFI in processor | Hardware watchdog; TMR on critical registers |
| Parametric drift (Vth shift) | TID in gate oxide | Monitor timing margins; derate clock speed if needed |

## Strengths

- Rad-hard processes (SOI, SOS, SiGe) provide inherent TID tolerance up to 1 Mrad without additional circuit-level hardening
- EDAC and TMR provide transparent SEU correction without flight software awareness or intervention
- Shielding trades mass for dose reduction: 10 mm Al reduces LEO dose by 10-20× at moderate mass cost
- Layered defense (shielding + rad-hard process + EDAC + TMR + watchdog + FDIR) provides multiple fault containment barriers
- Standards (MIL-STD-883, ESCC, JEDEC JESD-57) ensure consistent radiation qualification across vendors
- Spot shielding (tantalum domes) can protect critical components with minimal mass penalty

## Weaknesses

- Rad-hard silicon lags commercial by 10-15 years: the RAD750 at 200 MHz competes with a 1999 desktop processor
- Shielding mass scales linearly with thickness: doubling shielding doubles mass, with diminishing dose reduction past the knee
- GCR cannot be practically shielded: 20 cm of aluminum barely reduces GCR flux (secondary radiation cancels primary attenuation)
- COTS upscreening has statistical risk: lot-to-lot variation means a tested sample may not represent flight parts
- Radiation testing facilities (cobalt-60, cyclotrons) are scarce and expensive, creating qualification bottlenecks
- Rad-hard components are single-sourced (BAE Systems, Atmel), creating supply chain vulnerability

## See Also

- [Total Ionizing Dose Design](./radiation-hardening.tid-design.md) — SOI/SOS processes, threshold shifts, dose margins
- [Single Event Effects Mitigation](./radiation-hardening.see-mitigation.md) — EDAC, TMR, scrubbing, latchup prevention
- [Shielding Design](./radiation-hardening.shielding-design.md) — dose-depth curves, aluminum equivalent, spot shielding
- [Silicon](../silicon/index.md) — semiconductor fabrication processes for rad-hard ICs
- [Radiation Safety](../ehs/radiation-safety.md) — radiation environment knowledge and biological effects
- [Onboard Data Handling](./obdh.md) — flight computers and memory that consume rad-hard components
- [TT&C Systems](./ttac.md) — RF transponders that require radiation-tolerant electronics

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
