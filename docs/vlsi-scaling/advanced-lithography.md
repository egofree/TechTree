# Advanced Lithography

> **Node ID**: vlsi-scaling.advanced-lithography
> **Domain**: [VLSI Scaling & Advanced Semiconductor](./index.md)
> **Dependencies**: [`optics.inspection`](../optics/inspection.md),
> [`photolithography.resists-masks`](../photolithography/resists-masks.md)
> **Timeline**: Years 70-200+
> **Outputs**: euv_capability, advanced_patterning
> **Critical**: Yes — EUV lithography is the primary enabler of feature size scaling below 7 nm

This article covers **EUV (extreme ultraviolet) lithography** and extreme-node multiple patterning in depth: source technology, resist chemistry, high-NA EUV, and edge placement error management. For DUV lithography (g-line through ArF immersion), projection scanner design, resolution enhancement techniques, immersion systems, mask technology, overlay control, computational lithography, and throughput/cost analysis, see the companion article [Lithography](lithography.md).

## Prerequisites

- [Lithography](lithography.md) — DUV lithography systems, scanner mechanics, RET, immersion, mask technology, and overlay control (this article builds on that foundation)
- [Optics Inspection](../optics/inspection.md) — lens quality verification and mirror metrology
- [Resists & Masks](../photolithography/resists-masks.md) — photoresist chemistry and photomask fabrication

## Excimer Laser Sources

Excimer (excited dimer) lasers produce DUV light from gas mixtures that only lase in an excited state. They are the workhorse light source for DUV lithography and represent the optical technology that EUV ultimately replaced for the most critical layers.

**Common types**:
| Laser | Wavelength | Gas Mix | Power | First Use |
|-------|-----------|---------|-------|-----------|
| KrF | 248 nm | Kr + F₂ + Ne/He buffer | 20-40 W | ~1994 (250 nm node) |
| ArF | 193 nm | Ar + F₂ + Ne/He buffer | 20-60 W | ~2000 (130 nm node) |
| F₂ | 157 nm | F₂ + He/Ne buffer | 2-5 W | Never deployed in production |

**Key subsystems**:
- **Discharge tube**: Ceramic or metal tube (~50-100 cm long) with pre-ionization pins that create a uniform plasma before the main discharge. Electrodes must withstand highly corrosive fluorine gas — typically nickel or aluminum alloys.
- **Discharge circuit**: High-voltage (15-30 kV) thyratron or solid-state switch discharges a capacitor bank through the gas in ~100 ns pulses. Peak current: 10-50 kA. Pulse energy: 5-30 mJ per pulse.
- **Gas handling system**: Excimer laser gas degrades with use (fluorine reacts with tube materials, generates impurities). Closed-cycle gas system with purifiers and gas replenishment. Typical gas lifetime: 1-5 million pulses before gas exchange.
- **Repetition rate**: 1000-6000 Hz (modern ArF lasers). Higher rep rate → more wafer throughput, but also more thermal load on optics and gas.
- **Spectral purity**: Intracavity line-narrowing optics (etalons, prisms) reduce bandwidth to <0.5 pm FWHM — required for chromatic aberration control in high-NA projection lenses.

**Strengths**:
- ArF excimer laser at 193 nm provides 20-60 W output at 1000-6000 Hz — reliable, high-throughput DUV source
- Spectral bandwidth <0.5 pm FWHM enables chromatic aberration control in high-NA projection lenses

**Weaknesses**:
- Fluorine gas in the laser mixture is extremely corrosive — requires nickel/alloy discharge tubes and passivated gas handling
- Gas lifetime only 1-5 million pulses before exchange — frequent maintenance interrupting production

## EUV Source Technology

The EUV light source is the single most complex subsystem in an EUV lithography scanner. Generating 13.5 nm photons at industrial scale required solving problems across plasma physics, high-power lasers, vacuum engineering, and optical collection. For a compact EUV overview (source, mirrors, resist, vacuum), see [Lithography § EUV Lithography](lithography.md#euv-lithography).

**Tin (Sn) plasma source**:
- A high-power CO₂ laser (10-30 kW CW equivalent) fires pulses at tin droplets falling at 50-80 kHz repetition rate (one droplet every 12.5-20 μs). Each droplet is ~25-30 μm in diameter. The laser pre-pulse flattens the droplet into a disc, then the main pulse (~100 ns, ~0.5-1 J per pulse) vaporizes and ionizes the tin, creating a ~30-50 eV plasma that emits strongly at 13.5 nm wavelength.
- Sn debris mitigation: Ionized tin condenses on nearby optics, destroying their reflectivity. A hydrogen gas flow (200-500 sccm) across the plasma region chemically reacts with tin deposits (Sn + H₂ → SnH₄, stannane gas, though in practice Sn is removed as volatile hydrides or particulates). Debris shields and magnetic fields deflect charged Sn ions. Collector mirror lifetime: 3-6 months with active mitigation, vs. hours without.
- **Power progression**: Pre-production EUV sources (2010-2015): 10-30 W. First production (2016-2018): 80-125 W. Current production (2022+): 250-500 W at intermediate focus (IF). Target: 1000 W for high-throughput manufacturing. Each watt of EUV power at the wafer requires ~100-200 W of CO₂ laser input — the overall wall-plug efficiency of EUV generation is ~0.01-0.02%.

**CO₂ laser system**:
- Main amplifier: Radio-frequency-pumped CO₂ gas laser operating at 10.6 μm wavelength. Multi-stage system: seed laser → pre-amplifier → power amplifier chain. Output: 10-30 kW peak power in ~100 ns pulses at 50-80 kHz. Gas mix: CO₂:N₂:He at ~50-100 mbar total pressure. RF excitation at 50-100 MHz.
- Beam transport: Gold-coated copper mirrors guide the 10.6 μm beam from the laser cabinet through the scanner structure to the Sn droplet target. Mirror cooling (water channels behind the reflecting surface) manages thermal distortion at multi-kilowatt beam power. Alignment tolerance: <0.1 mrad.

**Collector optics**:
- The first optical element after the plasma is a multilayer Mo/Si collector mirror (similar technology to the projection optics mirrors, but larger — ~600 mm diameter). This normal-incidence collector captures ~2π steradians of the isotropic EUV emission and directs it toward the intermediate focus (IF) point.
- Collector reflectivity: ~65-70% per surface. Only ~1-2% of total Sn plasma EUV emission reaches the IF due to the limited solid angle of collection and single-reflection losses.

**Strengths**:
- Sn plasma source at 13.5 nm enables sub-7 nm features in a single exposure — no multiple patterning needed
- CO₂ laser-driven source achieves 250-500 W at intermediate focus, supporting 100-180 wafers/hr throughput

**Weaknesses**:
- Wall-plug efficiency ~0.01-0.02% — each watt of EUV at wafer requires 100-200 W of CO₂ laser input
- Sn debris limits collector mirror lifetime to 3-6 months even with active hydrogen mitigation

## EUV Resist Technology

Resist materials must satisfy three competing requirements simultaneously: resolution (smallest printable feature), sensitivity (dose needed for exposure — lower is better for throughput), and line-edge roughness (LER — statistical variation in feature edge position). This "RLS trade-off" (Resolution-LER-Sensitivity) is fundamental: improving one typically degrades another.

**EUV photon statistics and shot noise**:
- EUV photon energy is 92 eV (vs. 6.4 eV for 193 nm). Each photon carries ~14× more energy, but EUV sources produce far fewer photons per watt. At 20 mJ/cm² dose, only ~5-10 photons expose each 10 nm × 10 nm pixel — shot noise (Poisson statistics) causes 10-20% dose variation at the smallest features. This directly translates to line-edge roughness: LER ∝ 1/√(photon count).
- **LER specification**: At 7 nm node, LER must be <2 nm (3σ) for gate patterns. LER causes transistor threshold voltage variation (each nm of LER translates to ~1-2 mV Vth variation in short-channel devices). Current EUV resists achieve 3-5 nm LER — closing this gap is an active research area.

**Metal-oxide resists**:
- Organometallic compounds (e.g., tin-oxo clusters, zirconium oxide, hafnium oxide) offer higher EUV absorption than organic resists (metal atoms have larger absorption cross-sections at 13.5 nm). Sn-based resists achieve 13-16 nm half-pitch resolution with LER < 3 nm at dose 20-30 mJ/cm². However, metal contamination of fab equipment is a concern — Sn, Zr, and Hf are not standard in FEOL processing.

**Stochastic defects**: At extreme node dimensions, EUV patterning exhibits stochastic defects (random micro-bridges between lines or line breaks) at ~10⁻⁹ per feature rate, increasing exponentially with decreasing feature size. These are fundamentally different from systematic defects — they cannot be eliminated by process optimization alone, only reduced through dose/resist engineering.

**Strengths**:
- Metal-oxide resists (Sn, Zr, Hf) offer higher EUV absorption than organic resists, achieving 13-16 nm half-pitch
- Understanding shot noise statistics enables dose optimization to balance LER vs. throughput

**Weaknesses**:
- RLS trade-off is fundamental — improving resolution degrades LER and/or sensitivity simultaneously
- EUV shot noise at ~5-10 photons per 10 nm pixel causes 10-20% dose variation, directly translating to LER of 3-5 nm

## High-NA EUV

Standard EUV scanners operate at NA = 0.28-0.33 with 4:1 reduction. High-NA EUV targets NA = 0.55 with 8:1 anamorphic reduction (different X/Y magnification). Resolution: ~8 nm half-pitch single exposure (enabling ~2 nm node without multiple patterning). Mirrors ~1 m+ diameter, new mask format (no backward compatibility with current EUV masks). Estimated cost: $500-700M per scanner. First production expected 2025-2027.

**Implications**: High-NA EUV eliminates the need for SAQP on the most critical layers at 2 nm node, but the anamorphic reduction means mask infrastructure (blanks, writers, inspection) must be completely redesigned. The larger mirrors require new manufacturing techniques for sub-0.1 nm RMS figure accuracy at >1 m diameter.

**Strengths**:
- NA = 0.55 with 8:1 anamorphic reduction enables ~8 nm half-pitch single exposure — eliminates multiple patterning at 2 nm node
- Extends EUV lithography roadmap through the 2 nm / 1.4 nm nodes

**Weaknesses**:
- $500-700M per scanner with no backward-compatible mask format — requires entirely new mask infrastructure
- Mirror diameters >1 m with <0.1 nm RMS figure accuracy push the limits of optical manufacturing

## Multiple Patterning at Extreme Nodes

When EUV single-exposure resolution is insufficient for the target node, or when EUV throughput/cost makes DUV multi-patterning more economical, multiple patterning techniques extend patterning capability. For the foundational multiple patterning methods (LELE, SADP, SAQP, LE³/LE⁴) and their application at 20-7 nm nodes, see [Lithography § Multiple Patterning](lithography.md#multiple-patterning).

**EUV + DUV hybrid patterning** (sub-7 nm):
- EUV used for the most critical layers (gate, M0/M1) where single-exposure resolution suffices. DUV immersion with SAQP used for dense regular arrays (fins, gates at earlier nodes) where the self-aligned approach is more economical. Contact/via layers may use EUV + SADP to achieve sub-20 nm pitch without a second EUV exposure.
- Trade-off: EUV scanner time is the fab bottleneck. Using DUV for non-critical layers maximizes EUV throughput on the layers that benefit most.

**EUV double patterning** (sub-5 nm):
- When even EUV (13.5 nm, NA 0.33) cannot resolve target features in a single exposure (<8 nm half-pitch), EUV double patterning (two EUV exposures per layer) becomes necessary. Overlay requirement: <1.5 nm (3σ) between exposures — even more demanding than DUV double patterning. Mask count doubles for these layers.
- At 3 nm / 2 nm nodes, some layers require EUV double patterning with High-NA EUV available only for a subset.

**Strengths**:
- EUV + DUV hybrid approach maximizes scarce EUV scanner capacity for the most critical layers
- EUV double patterning extends 13.5 nm wavelength below 8 nm half-pitch

**Weaknesses**:
- EUV double patterning requires <1.5 nm overlay between EUV exposures — extreme scanner precision demand
- Hybrid patterning increases process complexity and requires tight coordination between DUV and EUV tool sets

## Edge Placement Error at Sub-10 nm

At sub-10 nm nodes, edge placement error (EPE) — the cumulative error in the position of any feature edge from its intended location — becomes the central patterning challenge. EPE includes overlay error, CD variation, mask error factor (MEF, typically 1.5-4× for dense patterns), and process bias. For overlay control methodology, see [Lithography § Alignment and Overlay Control](lithography.md#alignment-and-overlay-control).

**EPE budget at 5 nm node**:
- Overlay: ~3 nm (scanner positioning + mask registration)
- CD variation: ~2 nm (lithography + etch + resist)
- Total EPE: ~5 nm — approximately equal to the minimum space between adjacent features

When EPE exceeds the margin between adjacent features, a short or open circuit results. At 3 nm node, the EPE budget tightens to ~3-4 nm while feature spacing decreases proportionally — near-zero margin for error across all sources simultaneously.

**Strengths**:
- Decomposing EPE into overlay + CD + mask + process bias enables targeted improvement of the dominant error source
- Self-aligned patterning (SADP/SAQP) eliminates overlay contribution to EPE for suitable layout topologies

**Weaknesses**:
- Total EPE budget of ~5 nm at 5 nm node leaves almost zero margin — overlay, CD, and etch must all be near-perfect simultaneously
- Process-induced distortion from film stress and CMP consumes fixed overhead regardless of scanner capability

## EUV-Specific Hazards

For DUV lithography hazards (excimer laser HV, DUV radiation, fluorine gas, photoresist solvents, scanner noise), see [Lithography § Hazards & Safety](lithography.md#hazards--safety).

- **Class 4 CO₂ laser at 10-30 kW**: Severe eye and skin hazard. Beam path fully enclosed with interlocked covers. IR-rated safety glasses during alignment. Beam terminates on water-cooled absorber if any enclosure panel is opened.
- **Tin (Sn) vapor and SnH₄ (stannane)**: Toxic tin compounds from plasma source. Hydrogen gas flow carries volatile tin hydrides away from optics — exhaust gas must be scrubbed. SnH₄ is pyrophoric and toxic. Leak detection with tin-specific sensors in source compartment.
- **Hydrogen gas for debris mitigation**: Flammable gas (LEL 4% in air) flows at 200-500 sccm in the source chamber. Hydrogen detectors with automatic ventilation and source shutdown. Forced ventilation in EUV source compartments per NFPA 497.
- **Vacuum system hazards**: EUV beam path at ~10⁻⁵ to 10⁻⁷ Torr in a 10-20 m³ chamber. Risk of rapid decompression. Vacuum-rated viewports and interlocked access doors. See [Vacuum Systems](vacuum-systems.md) for detailed vacuum safety.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| EUV source power drops below 250 W — throughput falls under 100 WPH | Sn debris accumulating on collector mirror; CO₂ laser misalignment reducing pre-pulse/main-pulse coupling | Increase H₂ flow (200-500 sccm) for Sn removal; verify magnetic debris deflection; check CO₂ laser alignment on Sn droplet stream; schedule collector mirror replacement (lifetime: 3-6 months) |
| EUV line-edge roughness (LER) exceeds 3-5 nm target | Shot noise at ~5-10 photons per 10×10 nm pixel causes 10-20% dose variation; resist stochastic effects | Increase dose to improve photon statistics; evaluate metal-oxide resists (Sn, Zr, Hf based) for higher EUV absorption; reduce feature size dependence with optimized PEB conditions |
| Stochastic micro-bridges or line breaks at sub-10 nm | Insufficient photon dose; resist material stochastic effects at extreme dimensions | Increase exposure dose (trade: lower throughput); evaluate higher-absorption metal-oxide resists; tighten post-exposure bake uniformity to <±0.1°C; inspect with high-NA e-beam for stochastic defect density |
| EUV mask defect prints on every die — detected at wafer inspection | Multilayer Mo/Si defect in mask blank (substrate particle or pit); absorber patterning defect | Inspect mask with actinic EUV inspection; attempt FIB repair (±5-10 nm) if absorber defect; multilayer defects are unrepairable — blank replacement at $50,000-100,000 and 4-8 weeks |
| Collector mirror reflectivity degrading faster than expected | Insufficient H₂ flow for Sn removal; Sn droplet generator instability (irregular droplets causing excess debris) | Verify H₂ flow rate and purity; check Sn droplet generator timing and diameter (25-30 μm); increase magnetic field strength for ion deflection; schedule earlier collector replacement |

For DUV troubleshooting (CD variation, overlay, immersion defects, excimer laser, RET convergence, scanner stage noise), see [Lithography § Troubleshooting](lithography.md#troubleshooting).

## Decision and Implementation Framework

This section covers EUV adoption decisions. For DUV lithography selection (g-line through ArF immersion) and general patterning strategy, see [Lithography § Decision Framework](lithography.md#decision-and-implementation-framework).

### C1: EUV Adoption Criteria

| Factor | EUV Required | DUV Multiple Patterning Sufficient |
|---|---|---|
| Target node | <7 nm | 7-45 nm |
| Critical layer count | >10 layers at <20 nm HP | <10 layers at <38 nm HP |
| Monthly volume | >100K wafers | Any volume |
| Available capital | >$500M for lithography tools | $100-300M |
| DUV multiple-patterning cost per layer | Exceeds EUV single-pass cost | Below EUV cost |

### C2: EUV Implementation Prerequisites

1. **Establish DUV immersion lithography** with SAQP capability. EUV cannot be developed without DUV infrastructure for non-critical layers and mask inspection.
2. **Develop or acquire CO₂ laser system** capable of 10+ kW pulsed operation at 50-80 kHz. This alone requires significant laser technology development.
3. **Build Sn droplet generator** with 25-30 μm droplets at 50-80 kHz. Droplet timing jitter must be <±1 μs for consistent laser-droplet interaction.
4. **Fabricate Mo/Si multilayer mirrors** with 40-50 bilayer pairs at ±0.01 nm thickness control. Requires DC magnetron sputtering with in-situ monitoring. See [Optics Inspection](../optics/inspection.md) for mirror metrology.
5. **Achieve high vacuum** (10⁻⁵ to 10⁻⁷ Torr) in 10-20 m³ chamber. See [Vacuum Systems](vacuum-systems.md) for pumping technology.
6. **Develop EUV-compatible resists** — metal-oxide resists with <3 nm LER at 20-30 mJ/cm² dose. Resist outgassing in vacuum must be controlled to prevent mirror contamination.

### C3: EUV vs. DUV Multiple Patterning Trade-offs

| Factor | EUV Single Exposure | DUV Multiple Patterning (SAQP) |
|---|---|---|
| Cost per critical layer | $8-15/wafer | $5-10/wafer (but 2-4× more layers) |
| Overlay accumulation | 1 exposure → no accumulation | 2-4 exposures → ±2-3 nm cumulative |
| Mask count | 1 mask per layer | 2-4 masks + cut masks per layer |
| Cycle time | Single pass | 2-4× litho-etch cycles |
| Feature flexibility | Any pattern topology | Best for regular arrays (fins, gates) |
| Throughput bottleneck | Source power (100-180 WPH) | Not scanner-limited (200+ WPH per pass) |

## See Also

- [Lithography](lithography.md) — DUV lithography systems (g-line through ArF immersion), scanner mechanics, RET, immersion, mask technology, overlay, computational lithography, throughput/cost
- [Photoresists & Masks](../photolithography/resists-masks.md) — resist chemistry and photomask fabrication
- [Optics Inspection](../optics/inspection.md) — lithographic lens and mirror quality verification
- [Advanced Processes](advanced-processes.md) — etching and deposition at fine nodes
- [Continuous Scaling](continuous-scaling.md) — technology node progression
- [EDA Design](eda-design.md) — design rules for advanced nodes
- [Vacuum Systems](vacuum-systems.md) — vacuum technology for EUV beam path

---
*Part of the [Bootciv Tech Tree](../../index.md) • [VLSI Scaling](./index.md) • [All Domains](../../index.md)*
