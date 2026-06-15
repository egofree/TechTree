# Advanced Isotope Conversion

> **Node ID**: energy.radioisotope-power.advanced-isotope-conversion
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.radioisotope-power`](./radioisotope-power.md),
> [`energy.photovoltaics`](./photovoltaics.md),
> `electronics`
> **Enables**: high-efficiency solid-state nuclear power, millennial micro-power sources
> **Timeline**: Years 30-100+
> **Outputs**: tpv_electricity, betavoltaic_power, alphavoltaic_power
> **Critical**: No — emerging conversion technologies at TRL 3-4. Heritage [thermoelectric RTGs](./radioisotope-power.md) and Stirling systems cover all current mission needs. These methods extend specific power, lifetime, and miniaturisation beyond conventional limits but are not on the minimum-viable path.

## Overview

Heritage radioisotope power relies on two conversion principles: the Seebeck thermoelectric effect (5-8% efficiency, flown on every RTG since 1961) and Stirling dynamic conversion (28.6% efficiency, cancelled ASRG). Both are mature. This article covers the next generation — four emerging conversion technologies that push beyond those limits in different directions, plus two abandoned approaches documented for completeness.

**Thermophotovoltaic (TPV)** converters aim to beat Stirling efficiency with no moving parts, by coupling a hot isotope capsule to tuned infrared photovoltaic cells. A 2024 breakthrough demonstrated 32.5% efficiency at 1,309K — higher than any flight-proven RPS. TPV borrows directly from [photovoltaic](./photovoltaics.md) solar cell technology, adapting III-V semiconductor junctions to the infrared emission spectrum of a 1,300K heat source rather than the 5,800K solar spectrum.

**Betavoltaic** cells operate at the opposite end of the power scale. Instead of harvesting decay heat, they capture beta particles (high-energy electrons) directly in a semiconductor junction, producing microwatts of power for decades. The Betavolt BV100 — a 100 μW nuclear battery using Ni-63 and diamond semiconductor — entered mass production in 2025. These are the only power sources that deliver centennial lifetimes at sub-milliwatt scale, filling a niche no battery or harvester can match.

**Alpha-voltaic** cells apply the same direct-conversion principle to alpha particles, using wider-bandgap semiconductors (GaN, SiC) to absorb the 5 MeV energy of each alpha without immediate lattice destruction. The best result is 4.51% efficiency from a GaN PIN diode (2023). Radiation damage remains the binding constraint.

**Segmented thermoelectric** conversion is not new physics — it is an evolutionary advance on heritage thermoelectric RTGs, layering multiple materials across the temperature gradient to push efficiency from 6% toward 18%. It bridges the gap between current flight RTGs and the higher efficiencies promised by TPV and Stirling. Material data is covered in the dedicated thermoelectric RTG sub-article; this article references only the system-level performance predictions.

None of these methods replaces heritage [thermoelectric RTGs](./radioisotope-power.md) today. TPV and alpha-voltaic are laboratory demonstrations; betavoltaics serve a niche too small for spacecraft; segmented thermoelectric is the only approach approaching flight readiness. They matter for the bootstrap because they define the performance ceiling of radioisotope power — the upper bound on specific power, lifetime, and miniaturisation that a mature nuclear infrastructure can eventually reach.

## Materials

- **InGaAs (0.60 eV)** — Indium gallium arsenide, lattice-matched to InP substrate. The best TPV cell material, used in the 32.5% efficiency demonstration. Grown by MOCVD. See [Photovoltaics](./photovoltaics.md).
- **GaSb (0.67 eV)** — Gallium antimonide. Early TPV workhorse, mature growth technology. Lower bandgap than InGaAs but simpler manufacturing.
- **InGaAsSb (0.55 eV)** — Indium gallium arsenide antimonide. Widest infrared absorption of any III-V TPV material, extending to 2.5 μm. Research stage.
- **Silicon carbide (SiC, 3.26 eV)** — Wide-bandgap semiconductor for betavoltaic and alpha-voltaic junctions. Radiation-tolerant, mature from power electronics industry. See [Electronics](../electronics/index.md).
- **Gallium nitride (GaN, 3.40 eV)** — Widest practical bandgap semiconductor. Best alpha-voltaic efficiency (4.51%). Grown by HVPE or MOCVD on sapphire or GaN substrates.
- **Diamond (5.47 eV)** — Synthetic diamond semiconductor, the ultimate wide-bandgap material for radiation-hard nuclear batteries. Used in the Betavolt BV100 and Arkenlight C-14 cells. CVD-grown from methane/hydrogen plasma.
- **Tungsten emitter** — Spectrally selective thermal emitter for TPV, operating at 1,200-1,500K. High emissivity in the cell's absorption band, low emissivity elsewhere.
- **Yb₁₄MnSb₁₁** — p-type thermoelectric, ZT ≈ 1.3 at 1,200K. Best material for the hot segment of next-generation segmented couples.
- **La₃₋ₓTe₄** — n-type thermoelectric, ZT ≈ 1.2 at 1,250K. Matches Yb₁₄MnSb₁₁ in the hot segment.

## Thermophotovoltaic (TPV) Conversion

### Principle

A thermophotovoltaic converter works in three stages. First, the radioisotope capsule heats an emitter surface to 1,200-1,500K. Second, the emitter radiates infrared photons with a spectrum peaked at 2-4 μm wavelength (Wien's displacement law: λ_max = 2898/T μm). Third, photovoltaic cells with bandgaps tuned to 0.5-0.7 eV absorb those photons and convert them to electricity, exactly as a solar cell absorbs visible light.

The critical difference from [solar photovoltaics](./photovoltaics.md) is the photon energy. Solar cells use silicon (1.12 eV bandgap, absorbs below 1,100 nm). TPV cells must absorb photons at 2-4 μm, requiring much narrower bandgaps: 0.60 eV for InGaAs, 0.67 eV for GaSb, 0.55 eV for InGaAsSb. These low-bandgap III-V compounds are grown by metal-organic chemical vapour deposition (MOCVD) on lattice-matched substrates — the same III-V epitaxy platform used for multi-junction solar cells and infrared detectors.

### Demonstrated Efficiency

- **19% module efficiency at 1,330K emitter** — demonstrated under a radioisotope-equivalent heat source, reported in the AIAA Journal of Propulsion and Power. This used 0.60 eV InGaAs cells with a tandem plasma/interference spectral filter that reflects sub-bandgap photons back to the emitter for re-absorption.
- **32.5% breakthrough at 1,309K (2024)** — a National Science Foundation-funded study achieved 32.5% TPV efficiency using a semitransparent InGaAs/InP cell coupled to a secondary tungsten emitter. The semitransparent design allows sub-bandgap photons to transmit through the cell to a rear reflector, returning them to the emitter. This exceeded the best prior result by 13 percentage points and surpassed the efficiency of any flight-proven Stirling generator.
- **Theoretical system efficiency**: ~24% at the generator level (accounting for thermal losses, radiator mass, and peripheral overhead), with a specific power of ~21 W_e/kg — roughly three times the MMRTG's 2.8 W/kg.

### Cell Materials

| Cell Type | Bandgap (eV) | Substrate | Peak λ (μm) | Status |
|-----------|-------------|-----------|-------------|-------- |
| InGaAs (0.60 eV) | 0.60 | InP | 2.07 | Best demonstrated, used in 32.5% result |
| GaSb | 0.67 | GaSb | 1.85 | Mature, used in early TPV demos |
| InGaAsSb | 0.55 | GaSb | 2.25 | Widest IR absorption, research stage |

### Spectral Control

Without spectral control, roughly half of emitted photons fall below the cell bandgap and are wasted as heat. Three techniques recover this energy:

- **Tandem plasma/interference filters** — dielectric multilayer stacks that transmit above-bandgap photons and reflect sub-bandgap photons back to the emitter. Used in the 19% AIAA demonstration.
- **Semitransparent cells** — the 2024 breakthrough design. The cell itself transmits sub-bandgap photons to a rear mirror, eliminating the need for a separate filter.
- **2D photonic crystal emitters** — nanostructured tungsten surfaces with sub-wavelength surface features that selectively emit only at wavelengths the cell can absorb, suppressing sub-bandgap emission at the source.

### Advantages and Status

TPV's appeal is all-solid-state conversion at Stirling-class efficiency. No pistons, no helium, no bearings, no wear. Specific power targets of 21 W_e/kg would triple the MMRTG, meaning a mission could deliver three times the power for the same launch mass, or use one-third the plutonium for the same power.

The technology sits at **TRL 4** — component validation in laboratory. Two obstacles block flight qualification. First, material compatibility at 1,300-1,500K: the emitter, cell, and optical filters must survive continuous extreme-temperature operation without degradation for the 17-year design lifetime of a deep-space mission. Second, the narrow-bandgap III-V cells degrade faster than silicon under particle radiation, requiring shielding that erodes the mass advantage. No TPV radioisotope generator has flown.

### System Architecture

A flight TPV radioisotope generator would integrate:

1. **Heat source** — Standard GPHS module stack (Pu-238 dioxide, iridium clad, graphite aeroshell). Provides 1-2 kW_th at 1,300K. Identical to heritage RTG fuel — TPV does not require a new isotope, only a higher operating temperature.
2. **Emitter** — Tungsten or tantalum spectrally selective surface bonded to the heat source capsule. Coated with a 2D photonic crystal to shape emission. Operates at 1,200-1,500K.
3. **TPV cell array** — Circular or cylindrical InGaAs cell array surrounding the emitter, with a 5-10 mm vacuum gap. Cells are series-interconnected on a flexible substrate for thermal expansion matching.
4. **Spectral filter** — Tandem plasma/interference multilayer deposited on the cell's front surface, or a semitransparent cell design with rear reflector.
5. **Radiator** — The cell array's back side radiates waste heat to space at 300-400K. This dominates the radiator area — a TPV generator rejects more heat per watt than a thermoelectric RTG because the hot-side temperature is higher.
6. **Power conditioning** — DC-DC converters boost the low cell voltage (0.3-0.5 V per cell) to bus voltage. Series strings of 50-100 cells achieve 28V directly.

The thermal management challenge is significant. The emitter runs 200-300K hotter than a thermoelectric RTG hot junction, demanding refractory-metal emitter structures and high-temperature optical filters that do not degrade. The 17-year lifetime requirement means no filter delamination, no emitter oxidation, and no cell efficiency drift — all at temperatures where most materials creep, diffuse, or sublimate.

## Betavoltaic Cells

### Principle

A betavoltaic cell converts beta particles (high-energy electrons emitted during radioactive beta decay) directly into electricity using a semiconductor p-n junction. Each beta particle, carrying 17-225 keV of kinetic energy depending on the isotope, enters the semiconductor and generates hundreds of electron-hole pairs via impact ionisation. The junction's built-in electric field sweeps these carriers to the contacts, producing a small DC current.

This is the same physical principle as a photovoltaic cell — except the "photons" are beta particles with 10,000× more energy than visible-light photons. The challenge is that beta particles also damage the semiconductor lattice, creating defects that reduce carrier collection efficiency over time.

### Isotope Options

| Isotope | Half-life | Max β Energy | Typical Junction | Efficiency | Power Density |
|---------|-----------|-------------|-----------------|------------|---------------|
| Ni-63 | 100.1 yr | 67 keV | SiC / diamond | ~10% | 2.60 μW/cm² |
| Tritium (H-3) | 12.3 yr | 18.6 keV | SiC / diamond | 1-5% | 0.1-1.0 μW/cm² |
| Pm-147 | 2.62 yr | 224 keV | GaAs / SiC | 2-4% | 5-50 μW/cm² |

Nickel-63 dominates commercial betavoltaics because its 100-year half-life means power output drops by only 0.7% per year — a device still delivers 50% of rated power after 100 years. Its 67 keV maximum beta energy is below the 170 keV threshold for significant radiation damage in SiC and diamond, so the junction degrades slowly.

### Commercial Status (2025-2026)

- **Betavolt BV100 (China)** — The first mass-produced betavoltaic battery. 100 μW at 3V, using Ni-63 sources coupled to a diamond semiconductor converter. Package size 15×15×5 mm. 50-year guaranteed operating life. Betavolt announced mass production in 2025, targeting industrial sensors, medical implants, and extreme-environment electronics. The BV100 delivers roughly 10 μW/cm³ — too low for any active load but sufficient for CMOS memory retention, passive sensor polling, and trickle-charging a secondary battery.
- **City Labs (USA)** — Tritium-powered betavoltaic cells with a 20-year guaranteed operating life. Funded by the US National Institutes of Health for cardiac pacemaker power supplies, where the 20-year tritium half-life aligns with patient lifetime expectations. City Labs cells are certified for implantation and have accumulated over a decade of clinical deployment.
- **Infinity Power (USA)** — Ni-63 coin-cell betavoltaic claiming >60% conversion efficiency using a novel electrochemical (non-semiconductor) conversion stage that bypasses the betavoltaic junction entirely. The claim is controversial and the underlying physics differs from conventional p-n junction betavoltaics; independent verification is pending.
- **Arkenlight (UK)** — Carbon-14/diamond betavoltaic batteries manufactured from C-14 extracted from nuclear waste graphite. The C-14 (5,730-year half-life) is incorporated into a synthetic diamond lattice that functions as both the beta source and the semiconductor converter. Arkenlight's approach recycles long-lived nuclear waste into centennial power sources.

### Junction Design

The betavoltaic junction must be thin enough for beta particles (67 keV max for Ni-63) to penetrate the depletion region, yet thick enough to collect the generated carriers. The depletion width in a SiC PIN junction at 0V bias is 1-5 μm — comparable to the 6 μm penetration depth of a 67 keV electron in SiC. This alignment maximises carrier generation within the collection region.

Diamond junctions offer superior radiation tolerance — diamond's 5.47 eV bandgap and strong sp³ bonds resist displacement damage from beta impacts. The Betavolt BV100 uses a diamond semiconductor converter specifically for this radiation hardness, achieving the 50-year lifetime guarantee. Diamond CVD growth on lattice-matched substrates is the manufacturing bottleneck, as high-quality electronic-grade single-crystal diamond remains expensive and limited in wafer size.

### Limitations

The self-absorption effect is the binding physical limit. A thick isotope source absorbs its own beta particles before they reach the semiconductor — only the outer few micrometres of source material contribute. This caps practical power density in the microwatt-per-square-centimetre range regardless of total isotope mass. No betavoltaic can deliver milliwatts or watts; they are fundamentally micro-power sources.

Betavoltaics are suited for:

- MEMS devices and wireless sensor nodes with microampere average current
- Medical implants (pacemakers, neural stimulators, drug pumps)
- CMOS SRAM and non-volatile memory retention
- Cryptographic key storage and RTC backup

They are **not** suited for any load drawing more than ~1 mW continuous. A betavoltaic-powered radio transmitter is physically impossible at useful range — the isotope mass required would exceed the self-absorption limit.

## Alpha-Voltaic Cells

### Principle

Alpha-voltaic cells convert alpha particles (helium-4 nuclei, 4-6 MeV kinetic energy) directly into electricity using wide-bandgap semiconductor junctions. Each alpha particle carries 100× more energy than a beta particle, so a single alpha generates thousands of electron-hole pairs. The theoretical conversion efficiency is high — but so is the damage.

The challenge is that a 5 MeV alpha particle displaces several thousand atoms from the semiconductor lattice as it decelerates, creating a defect cascade that accumulates with fluence. After enough alpha impacts, the lattice becomes so damaged that carrier recombination at defects overwhelms the junction's collection efficiency, and power output collapses. Silicon junctions fail within hours. The solution is wide-bandgap semiconductors — GaN (3.4 eV) and SiC (3.26 eV) — whose stronger bonds better resist displacement damage.

### Demonstrated Results

- **GaN PIN diode: 4.51% efficiency (2023)** — reported in *Nature Communications Materials*. A GaN PIN junction irradiated with a Pu-238 alpha source achieved 4.51% energy conversion, the current record. Power density was 67.91 μW/cm² at the cell surface.
- **SiC PIN diode: 2.10% efficiency (2024)** — a 4H-SiC PIN junction achieved 2.10% conversion. SiC is preferred for its superior radiation tolerance and mature manufacturing base (power electronics industry), but its lower bandgap than GaN means more damage per alpha.
- **Theoretical**: >10 mW/cm³ is possible if radiation damage can be mitigated, but no cell has approached this. The gap between theory and demonstration is two orders of magnitude.

### The Damage Problem

Radiation damage at high fluence is the binding constraint. After 10¹⁴ alpha/cm², GaN lattice disorder reduces efficiency by 50%. After 10¹⁵, the junction is non-functional. A 1 mCi Pu-238 source delivers roughly 3.7×10⁷ alphas/second — reaching 10¹⁴ alphas in about 30 days at 1 cm distance. This makes sustained alpha-voltaic power from high-activity sources impractical without periodic annealing or extremely low source activity.

Current research explores defect-tolerant diamond junctions and three-dimensional structured geometries that spread the alpha flux over a larger semiconductor volume, reducing localised damage. No design has achieved practical operating lifetime.

### Damage Mitigation Strategies

Three approaches are under investigation to extend alpha-voltaic lifetime:

- **Periodic thermal annealing** — heating the junction to 500-800K after accumulated damage allows the lattice to partially self-repair via vacancy migration. Demonstrated for SiC, recovering 30-60% of pre-irradiation efficiency. Impractical for continuous operation but viable for pulsed-duty sensors.
- **Three-dimensional structured junctions** — fabricating the semiconductor as a forest of micropillars or trenches, with the alpha source deposited conformally around each pillar. This spreads the alpha flux over 10-100× more semiconductor surface area per unit volume, reducing localised damage density by the same factor.
- **Liquid-semiconductor junctions** — replacing the solid semiconductor with an ionic liquid that cannot sustain permanent lattice damage. Theoretical work only; no practical device demonstrated.

None of these has produced a device with useful sustained power output. Alpha-voltaic conversion remains a materials science challenge, not an engineering one.

### Status

Alpha-voltaic conversion is at **TRL 3** — analytical and experimental proof of concept in the laboratory. No device has demonstrated sustained operation at useful power for useful duration. The technology is a research topic, not a near-term deployment candidate.

## Segmented Thermoelectric Bridge

Between heritage thermoelectric RTGs (6% efficiency) and future TPV (24% theoretical), segmented thermoelectric conversion offers an evolutionary path. The concept layers multiple thermoelectric materials across the temperature gradient — each material optimised for its local temperature band — to push the effective figure of merit ZT above any single material's limit.

A fully segmented next-generation RTG couples:

- **p-leg**: Bi₂Te₃ (cold, 25-150°C) → Zn₄Sb₃ (mid, 150-400°C) → CeFe₄Sb₁₂ (hot, 400-700°C)
- **n-leg**: Bi₂Te₃ (cold) → PbTe (mid) → CoSb₃ (hot-mid) → La₂Te₃ (hot, up to 1,000°C)

Key advanced materials driving performance:

- **Yb₁₄MnSb₁₁** — p-type skutterudite-related compound, ZT ≈ 1.3 at 1,200K. Discovered at NASA-JPL, it is the best p-type material above 900K. See the thermoelectric RTG sub-article for detailed material properties and degradation data.
- **La₃₋ₓTe₄** — n-type compound, ZT ≈ 1.2 at 1,250K. The best n-type match for Yb₁₄MnSb₁₁ above 900K.

**Predicted efficiency**: ~18% at ΔT = 25°C to 1,000°C, triple the 6% of heritage PbTe/TAGS couples. This would give a next-generation RTG roughly 3× the electrical output of the MMRTG for the same plutonium inventory — without the moving parts of Stirling or the unproven infrared cells of TPV.

Detailed thermoelectric material data (ZT curves, sublimation rates, dopant diffusion coefficients, couple geometry) is documented in the dedicated thermoelectric RTG sub-article. This article references only the system-level predictions to avoid duplication.

## Other Conversion Methods

Two further conversion principles have been explored for radioisotope power and effectively abandoned:

### Thermionic Conversion

Thermionic converters boil electrons off a hot cathode (1,500K+) across a small vacuum gap to a cooler anode, directly producing electricity. The principle works — Soviet TOPAZ space reactors used thermionic conversion at 1,500-1,800K cathode temperatures. But for radioisotope power, the 1,500K cathode requirement exceeds the safe operating temperature of Pu-238 fuel capsules (iridium clad softens above 1,400°C). No thermionic RPS has been built; the approach was abandoned in the 1990s in favour of thermoelectric and Stirling.

### Piezoelectric Conversion

Research-stage designs couple beta or alpha particles to a piezoelectric transducer via a charge-collection membrane, converting the mechanical impulse of particle absorption into AC electrical output. Power levels are negligible (nanowatts), conversion efficiency is below 1%, and no mature design exists. Piezoelectric conversion is a curiosity in the academic literature with no practical deployment path.

## Bootstrap Relevance

For a civilization rebuilding industrial capacity from fundamentals, advanced isotope conversion is a late-game technology. Every approach in this article presupposes:

- A operating [nuclear fission](./nuclear-fission.md) reactor producing neutrons for [isotope production](./isotope-production.md)
- [Semiconductor fabrication](../electronics/index.md) capability for SiC, GaN, diamond, and III-V epitaxy — capabilities that arrive well after basic silicon device manufacturing
- [Photovoltaic](./photovoltaics.md) cell manufacturing for TPV — specifically III-V MOCVD growth, which is more advanced than silicon cell production
- Hot-cell [radiation safety](../ehs/radiation-safety.md) infrastructure for isotope handling and fuel encapsulation

The practical near-term win is segmented thermoelectric conversion: it requires no new physics, no new isotope, and no new manufacturing capability beyond what heritage RTG production already demands. The materials (Yb₁₄MnSb₁₁, La₃₋ₓTe₄) are synthesised from rare-earth elements recovered as fission product byproducts or from conventional mining.

Betavoltaics offer the earliest practical deployment for a bootstrapping civilization — a single Ni-63 betavoltaic cell can power a CMOS memory or RTC for a century with zero maintenance, once semiconductor junction fabrication and isotope separation are established. The BV100 demonstrates that this technology is commercially manufacturable with 2025-era capabilities.

TPV and alpha-voltaic remain aspirational. They define the performance ceiling but do not constrain the bootstrap path.

## Comparison of Advanced Conversion Technologies

| Technology | Efficiency | Power Scale | Isotope | TRL | Key Limitation |
|------------|------------|-------------|---------|-----|----------------|
| Thermophotovoltaic (TPV) | 32.5% @ 1,309K (cell) | 1-500 W | Pu-238 (heat) | 4 | 17-year survival at 1,300K |
| Betavoltaic (Ni-63) | ~10% | 1-100 μW | Ni-63 (β) | 9 (commercial) | Self-absorption caps power at μW |
| Alpha-voltaic (GaN) | 4.51% | μW-cm² scale | Pu-238, Am-241 (α) | 3 | Radiation damage at high fluence |
| Segmented thermoelectric | ~18% (predicted) | 10-300 W | Pu-238 (heat) | 6 | Material sublimation over 17 yr |

## Quantitative Parameters

| Parameter | TPV | Betavoltaic | Alpha-Voltaic | Segmented TE |
|-----------|-----|-------------|---------------|-------------|
| Cell efficiency | 32.5% @ 1,309K | ~10% (Ni-63/SiC) | 4.51% (GaN PIN) | ~18% (predicted) |
| System efficiency | ~24% (theoretical) | 1-10% | <5% | ~15% (system) |
| Specific power | ~21 W_e/kg | ~1 μW/g | <1 μW/g | ~5 W_e/kg |
| Power output range | 1-500 W | 1-100 μW | <1 μW/cm² | 10-300 W |
| Operating lifetime | 17 yr (design) | 50-100 yr | Months (damage) | 17 yr (heritage) |
| Moving parts | None | None | None | None |
| Temperature range | 1,200-1,500K emitter | Ambient | Ambient | 300-1,300K gradient |
| Key isotope | Pu-238 (heat) | Ni-63 (β), H-3 (β) | Pu-241, Am-241 (α) | Pu-238 (heat) |

## Products

| Output | Description | Use Case |
|--------|-------------|----------|
| `tpv_electricity` | DC electrical power from infrared photovoltaic conversion of a heated emitter | Future high-efficiency space RPS, deep-space missions |
| `betavoltaic_power` | Microwatt DC electrical power from direct beta-particle conversion in a semiconductor junction | Medical implants, sensor memory backup, MEMS |
| `alphavoltaic_power` | Microwatt DC electrical power from direct alpha-particle conversion in a wide-bandgap junction | Research-stage, high-energy-density micro-power (future) |

## See Also

- [Radioisotope Power](./radioisotope-power.md) — Parent capability: fuel supply, safety, containment
- [Isotope Production](./isotope-production.md) — Reactor irradiation of Np-237, Sr-90, Ni-63 target nuclides
- [Photovoltaic Solar Power](./photovoltaics.md) — Solar cell technology that TPV adapts for infrared emission spectra
- [Nuclear Fission Power](./nuclear-fission.md) — Reactor design and fuel cycle, parent nuclear capability
- [Electronics](../electronics/index.md) — Semiconductor junction fabrication for betavoltaic and alpha-voltaic cells
- [Radiation Safety](../ehs/radiation-safety.md) — Shielding, dosimetry, source handling for isotope work

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
