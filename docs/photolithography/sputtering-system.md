# Sputtering System

> **Node ID**: photolithography.sputtering-system
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Dependencies**: [`vacuum.chambers`](../vacuum/chambers.md), [`vacuum.pumps`](../vacuum/pumps.md), [`gas-handling`](../gas-handling/index.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`photolithography.fab-processes`](fab-processes.md), [`optics.inspection.optical-coatings`](../optics/optical-coatings.md), [`silicon.basic-devices`](../silicon/basic-devices.md)
> **Timeline**: Years 35-50
> **Outputs**: sputtered_films, metal_interconnects, barrier_layers, adhesion_layers
> **Critical**: Yes — sputtering is the primary method for depositing metal interconnects (Al, Cu, Ti, W) and barrier/adhesion layers in semiconductor fabrication

This article covers the construction of magnetron sputtering systems for thin-film deposition. For sputtering process physics, film properties, and deposition parameter details, see [Deposition Systems](../vacuum/deposition-systems.md).

## Overview

Magnetron sputtering is the primary method for depositing metal thin films in semiconductor manufacturing. A conductive target material is bombarded by argon ions in a vacuum chamber, ejecting target atoms that condense on the substrate as a thin film. Permanent magnets behind the target trap electrons in a closed racetrack, increasing ionization efficiency by 10-100× over simple diode sputtering. The result is high deposition rates (5-30 nm/min for metals) at moderate power levels (100-500 W) with excellent film adhesion.

Sputtering deposits the metal layers that form interconnects (Al, Cu), diffusion barriers (TiN, TaN), adhesion promoters (Ti), and gate electrodes (W) in integrated circuits. It handles both pure metals and alloys (Al-Cu, Al-Si) by sputtering from a target of the desired composition. Reactive sputtering extends the technique to compound films (TiN, TaN) by introducing nitrogen alongside argon.

The process requires high vacuum (base pressure <10⁻⁶ Torr) to prevent oxygen and water contamination in the deposited film, followed by controlled argon introduction to 1-10 mTorr for the sputtering plasma. A load-lock chamber preserves the main chamber vacuum during wafer exchange, reducing pump-down time from 30-60 minutes to 2-5 minutes per wafer.

## Principle

In DC magnetron sputtering, a negative voltage (300-700 V DC) is applied to a conductive target material (cathode) inside a vacuum chamber filled with argon gas at 1-10 mTorr. The voltage creates a plasma — Ar⁺ ions are accelerated into the target, ejecting target atoms by momentum transfer. A magnetic field behind the target traps electrons in a closed racetrack pattern, increasing ionization efficiency near the target surface. Ejected target atoms travel through the low-pressure gas (mean free path >> target-to-substrate distance at 1-3 mTorr) and condense on the substrate as a thin film.

For insulating targets (SiO₂, Al₂O₃), RF power at 13.56 MHz alternates the voltage polarity each half-cycle, preventing charge accumulation that would extinguish a DC plasma. An impedance matching network couples the RF power to the plasma.

## Prerequisites

- [Vacuum chamber](../vacuum/chambers.md) — stainless steel, base pressure <10⁻⁷ Torr
- [Turbomolecular pump](../vacuum/pumps.md) — 300-2000 L/s, with dry scroll backing pump
- [Gas handling](../gas-handling/index.md) — Ar sputter gas MFC, reactive gas MFCs (N₂, O₂)
- [DC and RF power supplies](../energy/electricity.md) — 1-20 kW DC, 300-2000 W RF
- [Permanent magnets](../metals/index.md) — NdFeB or SmCo for magnetron assembly
- [Precision machining](../machine-tools/machining.md) — for target bonding, substrate holder, shutter mechanism

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Stainless steel vacuum chamber | 1 | 350-500 mm diameter, CF-flanged | [Vacuum Chamber](../vacuum/chambers.md) | — |
| Turbomolecular pump | 1 | 300-2000 L/s N₂, mag-lev or ball bearing | [Vacuum Pumps](../vacuum/pumps.md) | Diffusion pump (oil contamination) |
| Dry scroll backing pump | 1 | 10-30 L/s, oil-free | [Vacuum Pump](../vacuum/pumps.md) | Rotary vane (oil backstreaming risk) |
| Copper backing plate (target) | 1 per source | Water-cooled, 150-300 mm diameter | [Metals](../metals/index.md) | — |
| Sputter target material | 1 per source | 3-12 mm thick, bonded to backing plate | Varies by application | — |
| NdFeB permanent magnets | 1 set per source | Ring and center plug, B ≈ 0.03-0.05 T at target surface | [Metals](../metals/index.md) | SmCo (higher temperature tolerance) |
| DC power supply | 1 | 1-20 kW, current-regulated, arc suppression | [Energy](../energy/electricity.md) | — |
| RF power supply + matching network | 1 | 13.56 MHz, 300-2000 W | [Energy](../energy/electricity.md) | — |
| Substrate holder / platen | 1 | Heated or cooled, rotating (10-30 RPM) | [Machine Tools](../machine-tools/machining.md) | — |
| Quartz crystal microbalance (QCM) | 1 | 6 MHz AT-cut crystal, rate monitor | [Measurement](../measurement/index.md) | — |
| Mechanical shutter | 1 | Pneumatic or magnetic actuation | [Machine Tools](../machine-tools/machining.md) | — |
| Mass flow controllers | 2-4 | Ar (10-100 sccm), reactive gases | [Gas Handling](../gas-handling/index.md) | — |
| Load lock chamber | 1 | 5-20 L with gate valve | [Vacuum Chamber](../vacuum/chambers.md) | Direct load (vent main chamber each run) |

## Process Description

### Chamber and Pumping System

1. **Prepare the vacuum chamber**: Construct or procure a stainless steel vacuum chamber per [Vacuum Chamber](../vacuum/chambers.md). Install CF flanges for: the sputter source (top or side), turbomolecular pump (bottom or side), substrate holder entry, gas inlet, pressure gauge, QCM, viewport, and load lock gate valve. Base pressure target: <5×10⁻⁸ Torr after bake-out.

2. **Mount the turbomolecular pump**: Bolt the turbo to the chamber via a gate valve and CF flange (CF160 or CF200). Connect the dry scroll backing pump to the turbo exhaust via flexible metal hose. Install a foreline pressure gauge. Verify that the backing pump maintains foreline below 0.1 Torr at maximum gas load.

3. **Install the throttle valve and pressure control**: Mount a throttle valve (angled butterfly type) between the chamber and the turbo gate valve. Connect a capacitance manometer (0-100 mTorr range) to the chamber. The throttle valve controller uses the manometer reading to maintain constant Ar pressure during sputtering (2-10 mTorr, stability ±0.5% of setpoint).

### Sputter Source Assembly

4. **Build the magnetron assembly**: Arrange NdFeB permanent magnets behind the target backing plate in a concentric ring pattern — an outer ring of magnets with alternating polarity around a center plug of opposite polarity. This creates a closed magnetic field loop (racetrack) above the target surface. The magnetic field strength at the target surface should be 0.03-0.05 T. Mount the magnets in a water-cooled copper or aluminum housing. The magnet housing is sealed from the vacuum by the target/backing plate assembly.

5. **Prepare and bond the target**: Cut the target material to match the backing plate diameter (150-300 mm). Bond the target to the water-cooled copper backing plate using indium solder (melting point 156°C — provides thermal contact without high-temperature processing) or mechanical clamping. Verify bond integrity — voids between target and backing cause local overheating and arcing. If available, inspect with ultrasonic C-scan.

6. **Mount the sputter source**: Install the magnetron source on the chamber flange (CF200 or larger). The target faces inward, toward the substrate. Connect water cooling lines to the backing plate (2-5 L/min flow). Connect the DC or RF power feedthrough to the backing plate (electrically isolated from the chamber by ceramic insulators). Target-to-substrate distance: 50-150 mm (adjustable via the source mounting).

### Substrate Holder

7. **Build the substrate holder**: Machine a flat aluminum or stainless steel platen (150-300 mm diameter) to hold the wafer. Install wafer clamping (mechanical clips or electrostatic chuck). For deposition uniformity, mount the platen on a rotary feedthrough (magnetic coupling or ferrofluidic seal) for planetary rotation at 10-30 RPM. Optionally add resistive heating elements for substrate heating (20-400°C).

8. **Install the shutter**: Mount a mechanical shutter (stainless steel plate, actuated by a pneumatic cylinder or magnetic feedthrough) between the target and the substrate. The shutter blocks deposition during target pre-sputtering (cleaning) and closes at the end of deposition for precise thickness control.

### Thickness Monitoring

9. **Install the QCM**: Mount a quartz crystal microbalance in the chamber at a position that receives the same flux as the substrate (or at a known geometric factor). The QCM head contains a 6 MHz AT-cut quartz crystal that oscillates at a frequency proportional to its mass. As film deposits, frequency decreases. Rate: ~2.27 Hz/nm for aluminum. Connect the QCM to a rate/thickness monitor controller. Crystal lifetime: 5,000-50,000 nm total thickness before replacement.

### Gas Delivery and Load Lock

10. **Build the gas delivery system**: Install MFCs for Ar (sputter gas) and any reactive gases (N₂ for TiN, O₂ for ITO). Route gas lines to an injection ring positioned near the target for uniform distribution. All wetted parts: electropolished 316L stainless steel with VCR fittings.

11. **Add the load lock**: Build a small antechamber (5-20 L) with two gate valves — one to atmosphere and one to the main chamber. Pump the load lock with a dedicated roughing pump + small turbo (or roughing pump only). Install a wafer transfer arm (motorized linear arm with vacuum chuck or edge-grip paddle). Load lock pump-down: 2-5 minutes from atmosphere to 10⁻⁶ Torr.

### DC Power Supply and Arc Suppression

12. **Connect the DC power supply**: For conductive targets (Al, Cu, Ti, W), connect a DC power supply (1-20 kW, current-regulated) to the target through a vacuum feedthrough. The positive terminal connects to the chamber (grounded anode). Install arc suppression circuitry — the power supply must detect voltage drops indicating micro-arcs and rapidly reverse polarity to extinguish arcs before target droplets are ejected.

13. **For RF sputtering**: For insulating targets (SiO₂, Al₂O₃), connect the RF generator (13.56 MHz, 300-2000 W) through the automatic matching network. The matching network minimizes reflected power (<5%) to protect the RF generator. RF power is coupled to the target through a blocking capacitor (prevents DC self-bias from shorting).

## Calibration and Verification

1. **Base pressure verification**: After bake-out at 150-250°C for 24 hours, verify base pressure <5×10⁻⁸ Torr with an ionization gauge. Perform an RGA scan — H₂O (mass 18) should be dominant; N₂/O₂ ratio of ~4:1 indicates an air leak requiring helium leak detection.

2. **Deposition rate calibration**: Sputter a test film on a silicon wafer at fixed power, pressure, and Ar flow. Measure film thickness with a profilometer or ellipsometer at 5-9 points across the wafer. Calculate deposition rate (nm/min) and uniformity (% thickness variation). Adjust source-to-substrate distance or add gas distribution baffle if uniformity exceeds ±10%.

3. **Target conditioning**: Before first production use, pre-sputter the target for 30-60 minutes with the shutter closed. Monitor discharge voltage — when it stabilizes, the target surface is clean (oxide removed). Record the stabilized voltage as the baseline for this target material.

4. **QCM calibration**: Compare QCM-measured thickness against profilometer measurements on test wafers. Adjust the QCM tooling factor (geometric correction between QCM position and wafer position) to match. Re-calibrate after each QCM crystal replacement.

## Quantitative Parameters

| Parameter | Value |
|-----------|-------|
| Base pressure | <5×10⁻⁸ Torr (after bake-out) |
| Process pressure (Ar) | 1-10 mTorr |
| Target voltage (DC) | 300-700 V |
| Discharge current | 1-20 A |
| Deposition rate (Al) | ~30 nm/min |
| Deposition rate (Ti) | ~10 nm/min |
| Deposition rate (W) | ~5 nm/min |
| Film uniformity | ±3-10% across 150-200 mm wafer |
| Substrate temperature | 20-400°C (heated platen) |
| RF power (insulating targets) | 300-2000 W at 13.56 MHz |
| Throughput | 10-25 wafers/hour (single wafer, load lock) |

## Strengths

- Wide range of materials — any solid that can be made into a target can be sputtered (metals, alloys, ceramics, semiconductors)
- Excellent adhesion — sputtered atoms arrive at the substrate with high kinetic energy (1-10 eV), producing dense, adherent films
- DC magnetron provides high deposition rates for conductors (up to 30 nm/min for Al) with relatively low substrate heating

## Weaknesses

- Line-of-sight deposition gives poor step coverage in high-aspect-ratio features — for conformal coverage, use CVD instead
- Target utilization is only 25-40% (the racetrack erodes deeply while center and edges remain)
- RF sputtering of insulators has lower deposition rates than DC sputtering of metals, and the matching network adds complexity

## Safety

- **High voltage**: DC supplies operate at 300-700 V with currents of 1-20 A. Lethal electrical hazard. Interlock the power supply so it shuts off when the chamber is open. Lock-out/tag-out before servicing.
- **RF radiation**: 13.56 MHz at 300-2000 W. Verify RF shielding — measure leakage with an RF probe at the chamber surface. Must be <10 mW/cm².
- **Reactive gases**: N₂ and O₂ in reactive sputtering are not toxic but O₂ enrichment increases fire risk. Ensure adequate ventilation.
- **Target materials**: Some targets contain toxic materials (Be, Cd, Cr, Se). Handle targets with gloves. Do not generate dust from target surfaces.

## Reactive Sputtering

Reactive sputtering deposits compound films by introducing a reactive gas (N₂, O₂, CH₄) along with the argon sputter gas. The reactive gas reacts with the sputtered metal atoms at the substrate surface to form a compound:

**TiN by reactive sputtering**: Sputter a Ti target in Ar + N₂ gas mixture. Nitrogen reacts with Ti atoms at the substrate to form TiN (titanium nitride). The nitrogen flow rate controls the stoichiometry — too little N₂ produces metallic Ti (golden color, low resistivity); too much N₂ "poisons" the target surface with TiN (reduced deposition rate, higher voltage). Target: stoichiometric TiN with resistivity 50-200 μΩ·cm, golden color.

**TaN by reactive sputtering**: Sputter Ta in Ar + N₂. TaN is amorphous and provides an excellent copper diffusion barrier — superior to crystalline Ta. Nitrogen flow controls the Ta:N ratio. Typical conditions: 300-500 W DC, 4-6 mTorr, N₂ at 5-15 sccm (15-25% of total gas flow).

**Target poisoning control**: As reactive gas flow increases, the target surface transitions from metallic mode (high rate, pure metal) to poisoned mode (low rate, compound). The transition is abrupt and hysteretic — the target poisons at a higher reactive gas flow than it recovers at. Closed-loop control (monitoring target voltage or plasma emission and adjusting reactive gas flow in real time) maintains operation at the transition point for optimal rate and composition.

## Multi-Target Systems

Production sputtering tools mount 3-6 targets on different source flanges, allowing sequential deposition of multiple film layers without breaking vacuum:

**Example: CMOS metallization stack**:
1. Ti adhesion layer: 20-50 nm from Ti target, 200 W DC, 3 mTorr Ar, 2 minutes
2. TiN barrier: 30-100 nm from Ti target + N₂ reactive gas, 400 W DC, 5 mTorr Ar/N₂, 5 minutes
3. Al-Cu interconnect: 0.5-1.5 μm from Al-0.5%Cu target, 500 W DC, 3 mTorr Ar, 20-50 minutes

Each target has its own:
- Shutter (blocks deposition during pre-sputter cleaning and between layers)
- Power supply (independently controlled)
- Gas flow (reactive gas on/off for compound vs. metal deposition)

Substrate rotates at 10-30 RPM during deposition for uniformity. Between layers, the substrate shutter closes, the previous target shutter closes, and the next target pre-sputters for 30-60 seconds before opening its shutter. Total pump-down + deposit + vent cycle: 60-90 minutes for a 3-layer stack.

## Film Characterization

After sputter deposition, films are characterized by:

**Thickness and uniformity**: Spectroscopic ellipsometry for transparent films (SiO₂, Si₃N₄), profilometer step-height for opaque films (metals). Measure at 9-49 points. Target: ±3-10% uniformity depending on film type.

**Resistivity**: Four-point probe measures sheet resistance. Convert to resistivity using film thickness: ρ = Rs × t. Compare to bulk resistivity (Al: 2.65 μΩ·cm, Cu: 1.68 μΩ·cm). Sputtered film resistivity is typically 1.5-3× bulk due to grain boundaries, impurities, and surface scattering. Resistivity decreases with post-deposition annealing (400-450°C, 30 min, forming gas).

**Stress**: Wafer curvature measurement. Sputtered films typically have compressive stress (-200 to -1000 MPa) at low Ar pressure (<3 mTorr) and tensile stress (+100 to +500 MPa) at high Ar pressure (>8 mTorr). The transition between compressive and tensile is the "transition pressure" — operating near this point produces near-zero stress films. Stress causes wafer bow (affects photolithography focus) and can cause film cracking or delamination.

**Grain structure**: Cross-sectional SEM reveals columnar grain structure typical of sputtered films. Column diameter: 20-200 nm depending on material, power, and substrate temperature. Higher substrate temperature produces larger grains (lower resistivity). Thornton's structure zone model predicts grain morphology as a function of T/Tm ratio (substrate temperature / melting temperature).

## Quality Control

**Film thickness verification**: Spectroscopic ellipsometry (transparent films) or profilometer step-height (opaque films) at 9-49 points across the wafer after each deposition run. Accuracy: ±1-2 nm. Uniformity target: ±3-10% depending on film and wafer size. Non-uniformity >±10% indicates target erosion, substrate rotation failure, or gas distribution problem.

**Sheet resistance mapping**: Four-point probe at 49 points across the wafer. Sheet resistance uniformity target: ±5%. Convert to resistivity: ρ = Rs × t (film thickness). Sputtered film resistivity is typically 1.5-3× bulk due to grain boundaries and impurities. Post-deposition anneal (400-450°C, 30 min, forming gas N₂/H₂) reduces resistivity toward bulk.

**Adhesion test**: Tape pull test (ASTM D3359) — apply pressure-sensitive tape to the film surface and pull at 180°. No film should detach. Adhesion failure indicates surface contamination or missing adhesion layer (Ti for metals on SiO₂).

**Film stress measurement**: Wafer curvature measurement (laser scanning) before and after deposition. Sputtered films are compressive at low Ar pressure (<3 mTorr) and tensile at high Ar pressure (>8 mTorr). Target: <500 MPa stress. High stress causes wafer bow (affects lithography focus), film cracking (tensile), or delamination (compressive).

**Step coverage evaluation**: Cross-sectional SEM over patterned topography (contact holes, trench steps). Sputtering provides moderate step coverage (50-70% of field thickness on sidewalls). Coverage <30% at contact bottoms indicates excessive directionality — increase Ar pressure to 5-8 mTorr for more scattering, or switch to CVD.

**Deposition rate stability**: Track QCM-measured deposition rate across runs on a control chart. Rate should be stable within ±5% for a given target condition. Rate drift signals target erosion (gradual rate decrease as racetrack deepens), magnet degradation, or power supply drift.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Target arcing — voltage drops to zero, then recovers | Oxide or contaminant layer on target surface; moisture in chamber; insufficient target pre-sputter | Pre-sputter with shutter closed for 5-10 minutes; verify base pressure before introducing Ar; use arc suppression power supply (detects arc, reverses polarity briefly) |
| Film has high resistivity (>5× bulk) | Oxygen or water incorporation from poor base pressure; low adatom energy from excessive Ar pressure; no substrate heating | Improve base pressure to <10⁻⁶ Torr; reduce Ar pressure to 2-4 mTorr; heat substrate to 200-350°C for denser film; add Ti getter pre-sputter before main deposition |
| Poor adhesion — film peels during tape test | Missing adhesion layer; contaminated substrate surface; native oxide between film and substrate | Deposit 20-50 nm Ti adhesion layer first; perform Ar sputter clean (200 W, 60 s) immediately before deposition; verify wafer surface is clean (RCA clean or piranha before load) |
| Non-uniform deposition ±15% across wafer | Target erosion groove deep; substrate not rotating; magnetron magnet degraded | Rotate substrate at 10-30 RPM; replace target when erosion groove exceeds 50% depth; remagnetize or replace NdFeB magnets if field weakened |
| Depositing wrong stoichiometry in reactive sputtering | Reactive gas flow unstable; target poisoning state ambiguous | Install closed-loop reactive gas control (monitor target voltage or plasma emission at 500 nm for Ti); reduce N₂ flow and increase Ar; pre-condition target surface |

## Scaling Notes

- **From single-target to multi-target**: Add additional sputter source flanges to the chamber. Each source needs its own power supply, shutter, and cooling. Three sources cover most CMOS metallization needs (Ti, TiN/reactive, Al-Cu).

- **From batch to single-wafer with load lock**: Batch coaters process multiple wafers simultaneously but have poor uniformity control. Single-wafer tools with load locks provide better uniformity and faster wafer turnaround (load lock pump-down: 2-5 minutes vs. main chamber pump-down: 30-60 minutes).

- **Target utilization**: Standard magnetron targets erode in a racetrack pattern, utilizing only 25-40% of the target material. Planar magnetrons with optimized magnet arrays achieve 40-50%. Rotating cylindrical magnetrons (targets are cylinders that rotate through the plasma) achieve >80% utilization — used in large-area coating applications (architectural glass, solar panels) but not common in semiconductor tools.

## Variations and Alternatives

| Method | Deposition Rate | Step Coverage | Materials | When to Use |
|--------|----------------|---------------|-----------|-------------|
| DC magnetron sputtering | 5-30 nm/min (metals) | Moderate | Conductive targets only (Al, Ti, Cu, Ta, W) | Standard for metal interconnects and barriers |
| RF sputtering | 1-20 nm/min | Moderate | Insulating targets (SiO₂, Al₂O₃, ITO) | When dielectric films are needed from sputtering |
| Reactive sputtering | 3-10 nm/min | Moderate | Compounds formed in-situ (TiN, TaN, ITO) | When compound films with precise stoichiometry are needed |
| Thermal evaporation | 5-100 nm/min | Poor (line-of-sight) | Low-melting-point metals (Al, Au, Cr) | Simplest PVD method, good for research and thick single-layer metals |
| E-beam evaporation | 10-500 nm/min | Poor (line-of-sight) | Refractory metals and ceramics | High-purity, high-rate deposition of difficult materials |
| CVD | 2-50 nm/min | Excellent (conformal) | SiO₂, Si₃N₄, poly-Si, W | When conformal coverage in high-aspect-ratio features is required |

Sputtering is the default for metals (good adhesion, uniform, alloy-compatible). Evaporation is simpler but provides poor step coverage. CVD provides the best conformality but cannot deposit pure metals as easily as PVD.

## References

- [Deposition Systems](../vacuum/deposition-systems.md) — DC/RF sputtering physics, evaporation comparison, deposition parameter tables
- [Vacuum Chamber](../vacuum/chambers.md) — chamber construction and sealing
- [CVD Reactor](cvd-reactor.md) — alternative deposition technology for conformal films
- [Gas Handling](../gas-handling/index.md) — gas delivery and MFC specifications
- [Core Fab Processes](fab-processes.md) — how sputtering fits into the IC fabrication flow

---
*Part of the [Bootciv Tech Tree](../../index.md) • [Photolithography & IC Fabrication](./index.md) • [All Domains](../../index.md)*
