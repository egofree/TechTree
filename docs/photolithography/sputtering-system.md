# Sputtering System

> **Node ID**: photolithography.sputtering-system
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Dependencies**: [`vacuum.chambers`](../vacuum/chambers.md), [`vacuum.pumps`](../vacuum/pumps.md), [`gas-handling`](../gas-handling/index.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`photolithography.fab-processes`](fab-processes.md), [`optics.inspection.optical-coatings`](../optics/optical-coatings.md), [`silicon.basic-devices`](../silicon/basic-devices.md)
> **Timeline**: Years 35-50
> **Outputs**: sputtered_films, metal_interconnects, barrier_layers, adhesion_layers
> **Critical**: Yes — sputtering is the primary method for depositing metal interconnects (Al, Cu, Ti, W) and barrier/adhesion layers in semiconductor fabrication

This article covers the construction of magnetron sputtering systems for thin-film deposition. For sputtering process physics, film properties, and deposition parameter details, see [Deposition Systems](../vacuum/deposition-systems.md).

## Principle

In DC magnetron sputtering, a negative voltage (300-700 V DC) is applied to a conductive target material (cathode) inside a vacuum chamber filled with argon gas at 1-10 mTorr. The voltage creates a plasma — Ar⁺ ions are accelerated into the target, ejecting target atoms by momentum transfer. A magnetic field behind the target traps electrons in a closed racetrack pattern, increasing ionization efficiency near the target surface. Ejected target atoms travel through the low-pressure gas (mean free path >> target-to-substrate distance at 1-3 mTorr) and condense on the substrate as a thin film.

For insulating targets (SiO₂, Al₂O₃), RF power at 13.56 MHz alternates the voltage polarity each half-cycle, preventing charge accumulation that would extinguish a DC plasma. An impedance matching network couples the RF power to the plasma.

## Prerequisites

- [Vacuum chamber](../vacuum/vacuum-chamber.md) — stainless steel, base pressure <10⁻⁷ Torr
- [Turbomolecular pump](../vacuum/pumps.md) — 300-2000 L/s, with dry scroll backing pump
- [Gas handling](../gas-handling/index.md) — Ar sputter gas MFC, reactive gas MFCs (N₂, O₂)
- [DC and RF power supplies](../energy/electricity.md) — 1-20 kW DC, 300-2000 W RF
- [Permanent magnets](../metals/index.md) — NdFeB or SmCo for magnetron assembly
- [Precision machining](../machine-tools/machining.md) — for target bonding, substrate holder, shutter mechanism

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Stainless steel vacuum chamber | 1 | 350-500 mm diameter, CF-flanged | [Vacuum Chamber](../vacuum/vacuum-chamber.md) | — |
| Turbomolecular pump | 1 | 300-2000 L/s N₂, mag-lev or ball bearing | [Vacuum Pumps](../vacuum/pumps.md) | Diffusion pump (oil contamination) |
| Dry scroll backing pump | 1 | 10-30 L/s, oil-free | [Vacuum Pump](../vacuum/vacuum-pump.md) | Rotary vane (oil backstreaming risk) |
| Copper backing plate (target) | 1 per source | Water-cooled, 150-300 mm diameter | [Metals](../metals/index.md) | — |
| Sputter target material | 1 per source | 3-12 mm thick, bonded to backing plate | Varies by application | — |
| NdFeB permanent magnets | 1 set per source | Ring and center plug, B ≈ 0.03-0.05 T at target surface | [Metals](../metals/index.md) | SmCo (higher temperature tolerance) |
| DC power supply | 1 | 1-20 kW, current-regulated, arc suppression | [Energy](../energy/electricity.md) | — |
| RF power supply + matching network | 1 | 13.56 MHz, 300-2000 W | [Energy](../energy/electricity.md) | — |
| Substrate holder / platen | 1 | Heated or cooled, rotating (10-30 RPM) | [Machine Tools](../machine-tools/machining.md) | — |
| Quartz crystal microbalance (QCM) | 1 | 6 MHz AT-cut crystal, rate monitor | [Measurement](../measurement/index.md) | — |
| Mechanical shutter | 1 | Pneumatic or magnetic actuation | [Machine Tools](../machine-tools/machining.md) | — |
| Mass flow controllers | 2-4 | Ar (10-100 sccm), reactive gases | [Gas Handling](../gas-handling/index.md) | — |
| Load lock chamber | 1 | 5-20 L with gate valve | [Vacuum Chamber](../vacuum/vacuum-chamber.md) | Direct load (vent main chamber each run) |

## Construction Steps

### Chamber and Pumping System

1. **Prepare the vacuum chamber**: Construct or procure a stainless steel vacuum chamber per [Vacuum Chamber](../vacuum/vacuum-chamber.md). Install CF flanges for: the sputter source (top or side), turbomolecular pump (bottom or side), substrate holder entry, gas inlet, pressure gauge, QCM, viewport, and load lock gate valve. Base pressure target: <5×10⁻⁸ Torr after bake-out.

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

## Expected Performance

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

## See Also

- [Deposition Systems](../vacuum/deposition-systems.md) — DC/RF sputtering physics, evaporation comparison, deposition parameter tables
- [Vacuum Chamber](../vacuum/vacuum-chamber.md) — chamber construction and sealing
- [CVD Reactor](cvd-reactor.md) — alternative deposition technology for conformal films
- [Gas Handling](../gas-handling/index.md) — gas delivery and MFC specifications
- [Core Fab Processes](fab-processes.md) — how sputtering fits into the IC fabrication flow

[← Back to Photolithography](index.md)
