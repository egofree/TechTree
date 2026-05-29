# Semiconductor Devices

> **Node ID**: electronics.semiconductor-devices
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`silicon.basic-devices`](../silicon/basic-devices.md), [`chemistry.acids`](../chemistry/acids.md), [`gas-handling.vacuum`](../gas-handling/vacuum.md), [`electronics.passive-components`](passive-components.md)
> **Enables**: [`electronics.power-electronics`](power-electronics.md), [`computing.electronic`](../computing/electronic.md), [`vlsi-scaling.eda-design`](../vlsi-scaling/eda-design.md)
> **Timeline**: Years 30-55
> **Outputs**: diodes, transistors, thyristors, voltage_references
> **Critical**: Yes — diodes and transistors are the fundamental active components enabling all power conversion, signal processing, and digital logic


This document covers the physics, construction, and application of discrete semiconductor devices at the component level — diodes, bipolar junction transistors (BJTs), field-effect transistors (FETs), and thyristors. These are the active devices that make amplification, switching, rectification, and logic possible.

**Domain boundary**: The [Silicon domain](../silicon/basic-devices.md) covers wafer-level processes — crystal growth, wafer preparation, and basic pn junction formation. This document covers the device physics, packaging into discrete components, circuit-level behavior, and selection/application of those devices. The [Photolithography domain](../photolithography/fab-processes.md) covers IC fabrication processes (patterned doping, metallization, planarization) for integrated circuits.

Semiconductor devices sit at the heart of the electronics bootstrap chain. [Passive components](passive-components.md) alone cannot amplify signals or perform logic — active devices are required. Every [power electronics](power-electronics.md) converter relies on diodes and transistors for switching. Every [computing](../computing/electronic.md) system uses transistors as logic switches.

## Prerequisites

## Materials
- **Silicon wafers**: Single-crystal, 50-300 mm diameter, p-type (boron) or n-type (phosphorus), from [wafer production](../silicon/wafering.md)
- **Dopant sources**: Phosphorus (POCl₃ gas, PH₃ gas), boron (BBr₃ gas, B₂H₆ gas), arsenic (AsH₃ gas), antimony (Sb)
- **Metallization**: Aluminum (1% Si, 99.99% purity), gold wire (25 μm for wire bonding)
- **Oxidation gases**: O₂ (dry oxidation), H₂ + O₂ (wet oxidation — grows oxide 5-10× faster)
- **Encapsulation**: Epoxy molding compound, ceramic (alumina) for hermetic packages, Kovar lead frames

## Tools
- [Diffusion furnace](../energy/electric-furnaces.md) (800-1200°C, ±0.5°C uniformity)
- [Vacuum equipment](../gas-handling/vacuum.md) for deposition processes
- [Photolithography](../photolithography/resists-masks.md) equipment for patterned doping
- [Wire bonding](assembly.md) equipment for package interconnect
- [Electrical measurement](../measurement/electrical-instruments.md) instruments for device characterization

## Knowledge
- Semiconductor physics: band gap (Si: 1.12 eV), intrinsic carrier concentration, doping, pn junction
- Device equations: diode (I = Iₛ(e^(V/nVt) - 1)), BJT (Ic = β × Ib), MOSFET (Id = ½μnCox(W/L)(Vgs-Vth)²)
- Thermal management: junction temperature, thermal resistance, power dissipation

## Bill of Materials

| Material | Quantity (per 1000 discrete transistors, TO-92 package) | Source | Alternatives |
|----------|--------------------------------------------------------|--------|-------------|
| Silicon wafer (100 mm, n-type, 5-10 Ω·cm) | 0.1-0.2 wafer | [Wafer Production](../silicon/wafering.md) | Germanium (lower Tj, obsolete for most uses) |
| Phosphorus oxychloride (POCl₃) | 5-10 mL | [Chemistry](../chemistry/acids.md) | PH₃ gas (toxic, pyrophoric) |
| Boron tribromide (BBr₃) | 5-10 mL | [Chemistry](../chemistry/acids.md) | B₂H₆ gas (toxic, pyrophoric) |
| Aluminum wire (1% Si) | 5-20 m | [Metals](../metals/index.md) | Gold (higher cost, better for wire bonding) |
| Gold wire (25 μm) | 50-200 m | [Metals](../metals/index.md) | Aluminum wire (25-50 μm, wedge bonding) |
| Epoxy molding compound | 0.5-1.0 kg | [Polymers](../polymers/thermosets.md) | Ceramic hermetic package (military/space) |
| Copper alloy lead frame (42 pins/strip) | 5-10 strips | [Metals](../metals/index.md) | Kovar alloy (CTE-matched for hermetic) |

## Process Description

## Diode Construction

#### Discrete PN Junction Diode

1. **Starting wafer**: n-type silicon (phosphorus-doped, 1-10 Ω·cm, <111> or <100> orientation, 300-500 μm thick).
2. **Oxidation**: Grow 0.5-1.0 μm SiO₂ in dry O₂ at 1000-1100°C (4-8 hours) or wet oxidation (H₂ + O₂) at 900-1000°C (1-2 hours). Wet oxidation is 5-10× faster but produces slightly lower quality oxide.
3. **Photolithography**: Apply photoresist → expose through mask (defines diffusion windows) → develop. Opens windows in oxide where boron will be diffused.
4. **Boron diffusion (p-type region)**: Load wafers into diffusion furnace. Pre-deposition: BBr₃ source at 900-1000°C for 15-60 min in N₂ carrier gas. Drive-in: 1050-1150°C for 30-120 min in O₂/N₂. Target junction depth: 1-10 μm. Sheet resistance: 5-50 Ω/sq.
5. **Strip oxide**: HF dip (10-20%, 1-5 min) removes diffusion oxide.
6. **Back-side preparation**: Grind back of wafer to remove any back-side oxide and dopant. Reduce thickness to final device thickness (150-300 μm).
7. **Metallization**: Evaporate or sputter aluminum (1% Si) on front (anode contact) and back (cathode contact). Thickness: 0.5-2.0 μm. Alloy at 425-450°C for 15-30 min in N₂/H₂ forming gas to form ohmic contacts.
8. **Scribe and dice**: Diamond scribe or laser scribe wafer into individual die (0.5 × 0.5 mm for small-signal to 10 × 10 mm for power diodes). Break or saw along scribe lines.
9. **Package**: Die-attach to lead frame (silver epoxy or soft solder). Wire-bond anode contact. Mold in epoxy (transfer mold at 175°C, 70 bar, 90 sec). Trim and form leads. Mark with type designation.

#### Zener Diode

Same process as standard diode but with heavily doped p and n regions to achieve specific breakdown voltage. Zener breakdown (tunneling) dominates below ~5V; avalanche breakdown (impact ionization) dominates above ~5V. Common voltages: 3.3V, 3.6V, 3.9V, 4.3V, 4.7V, 5.1V, 5.6V, 6.2V, 6.8V, 7.5V, 8.2V, 9.1V, 10V, 12V, 15V, 18V, 24V, 30V, 36V, 47V. Tolerance: ±2% (A suffix), ±5% (B suffix, standard).

#### Schottky Diode

Metal-semiconductor junction (no p-type region). Aluminum, platinum, or titanium deposited directly on n-type silicon. Forward voltage drop: 0.2-0.4V (vs. 0.6-0.7V for silicon pn junction). Faster switching (no minority carrier storage). Used in high-frequency rectification and power conversion. Reverse leakage higher than pn diodes: 1-100 μA at rated voltage (increases exponentially with temperature).

**Strengths** (diode family):
- PN junction diodes are the simplest semiconductor device (single diffusion step after oxidation) — process complexity is minimal, enabling early bootstrap production with a single furnace and basic photolithography
- Zener diodes provide voltage reference and regulation from a two-terminal device with no external bias circuitry — available in 24 standard voltages from 3.3V to 47V
- Schottky diodes have 50-70% lower forward voltage drop (0.2-0.4V) than PN diodes, reducing rectifier power loss proportionally — critical for high-efficiency power converters

**Weaknesses** (diode family):
- PN junction diodes have relatively slow reverse recovery (2-10 μs for rectifier types) due to stored minority carrier charge — this limits usable switching frequency to <100 kHz for standard diodes
- Zener diodes below 5V have soft knee characteristics and high temperature coefficient — voltage regulation degrades significantly with load current and temperature variation
- Schottky diodes have high reverse leakage current (1-100 μA) that doubles every 10°C — at elevated temperatures, leakage power dissipation can exceed forward conduction savings

## Bipolar Junction Transistor (BJT)

#### NPN Transistor Construction

1. **Starting wafer**: n-type silicon (collector region), 5-20 Ω·cm, 300-500 μm thick.
2. **Grow oxide, photolithography** for base region windows.
3. **Base diffusion (p-type)**: Boron diffusion. Pre-deposition at 900-950°C, drive-in at 1100-1150°C. Target base width: 1-5 μm. Sheet resistance: 100-300 Ω/sq. Base width is critical — too wide reduces β (current gain); too narrow risks punch-through (collector-base short at high voltage).
4. **Oxidation, photolithography** for emitter region windows.
5. **Emitter diffusion (n+ type)**: Phosphorus diffusion at 950-1050°C. Heavy doping (n+) for low emitter resistance and high injection efficiency. Emitter junction depth: 0.5-2.0 μm from surface. Pushes base region slightly deeper (emitter push effect).
6. **Metallization**: Open contact windows in oxide. Deposit aluminum. Pattern (photolithography + etch) to form separate base and emitter contacts.
7. **Back metallization**: Aluminum or gold-sputtered back for collector contact.
8. **Alloy, dice, package**: Same as diode.

**Key parameters**:
- β (hFE, current gain): 50-500 (general purpose), 100-20,000 (Darlington). β varies with Ic — peaks at 1-100 mA for small-signal devices, 1-10A for power devices. β decreases at very low and very high currents.
- Vbe (base-emitter voltage): 0.6-0.7V at moderate currents (silicon). Temperature coefficient: -2.2 mV/°C.
- Vce(sat) (collector-emitter saturation voltage): 0.1-0.5V. Determines power dissipation when used as a switch.
- Ft (transition frequency): 100-500 MHz (general purpose), 1-10 GHz (RF). Ft = gm / (2π × (Cbe + Cbc)). Above Ft, β drops below 1 — device cannot amplify.

**Strengths**:
- Low saturation voltage (Vce(sat) = 0.1-0.5V) provides efficient switching for power applications — lower conduction loss than MOSFETs at high voltage (>600V) where MOSFET Rds(on) becomes prohibitive
- Current-controlled operation provides inherent current limiting — the base current proportionally controls collector current, making BJT circuits naturally protected against load faults in linear regulator and amplifier applications
- Mature, well-understood fabrication process with only 2 diffusion steps (base + emitter) — requires fewer photolithography masks than MOSFET, reducing process complexity and cost

**Weaknesses**:
- Current-driven input requires continuous base current to maintain conduction — a power BJT switching 10A with β=20 needs 500 mA base drive, wasting 2.5% of switched power as gate drive loss
- Secondary breakdown: localized thermal runaway at high Vce × Ic combinations creates destruction zones that limit safe operating area (SOA) — MOSFETs do not have this failure mode
- β varies with temperature (doubles from 25°C to 100°C), collector current (peaks at 1-100 mA, drops at high and low current), and between individual devices — requires careful bias circuit design for linear applications

## MOSFET (Metal-Oxide-Semiconductor FET)

#### N-Channel Enhancement MOSFET

1. **Starting wafer**: p-type silicon substrate, 5-20 Ω·cm.
2. **Grow gate oxide**: Dry oxidation at 900-1000°C for thin, high-quality SiO₂. Thickness: 10-100 nm (controls Vth). For power MOSFETs: 50-100 nm (higher voltage rating). Gate oxide quality is the most critical parameter — a single defect causes gate leakage or oxide rupture.
3. **Polysilicon gate deposition**: Deposit 0.3-0.5 μm polysilicon by LPCVD at 600-650°C. Dope heavily n+ (phosphorus diffusion or ion implantation). Pattern gate electrode.
4. **Source/drain formation**: Implant or diffuse phosphorus/arsenic into exposed areas on either side of gate. Self-aligned process: gate electrode acts as mask for source/drain doping. Junction depth: 0.5-2.0 μm.
5. **Interlayer dielectric**: Deposit SiO₂ (1.0-2.0 μm) by CVD.
6. **Contact formation**: Etch contact holes through oxide to source, drain, and gate. Metallize with aluminum (1% Si/0.5% Cu). Pattern.
7. **Dice, package**: For power MOSFETs, use vertical structure (current flows vertically through chip): drain on bottom, source and gate on top. Package in TO-220, TO-247, D²PAK for heat dissipation.

**Key parameters**:
- Vth (threshold voltage): 1-4V (logic level), 2-5V (standard). Below Vth: device is off (Ids ≈ 0). Above Vth: device conducts.
- Rds(on) (on-resistance): 0.001-10 Ω (determines conduction loss). Lower is better — power dissipation = Id² × Rds(on). Power MOSFETs target <0.1 Ω.
- Vds(max) (drain-source breakdown): 20-1200V depending on design. Higher voltage = thicker drift region = higher Rds(on). Trade-off: Rds(on) ∝ Vds²·⁵ for silicon.
- Qgs (total gate charge): 1-200 nC (determines switching speed and gate drive power). Switching time ≈ Qgs / Ig. Pgate = Qgs × Vgs × fsw.
- Id (continuous drain current): 0.1-200A (package-limited at high current).

**Strengths**:
- Voltage-driven gate requires negligible steady-state gate current (<1 nA leakage) — a single gate driver can control multiple parallel MOSFETs without the power waste of BJT base drive
- No secondary breakdown — the positive temperature coefficient of Rds(on) causes current to redistribute away from hot spots, enabling safe paralleling of multiple devices and wider SOA than BJTs
- Fast switching (10-100 ns) with no minority carrier storage charge — enables high-frequency operation (20-500 kHz) for switching power converters, reducing magnetic component size proportionally

**Weaknesses**:
- Gate oxide is the most fragile element in any semiconductor device — a single defect in the 10-100 nm SiO₂ layer causes gate leakage or catastrophic oxide rupture from ESD (as low as 100V for thin-oxide types)
- Rds(on) ∝ Vds²·⁵ for silicon — above ~600V, the on-resistance becomes impractically high, making MOSFETs unsuitable for high-voltage switching where IGBTs or thyristors are required
- Gate charge (Qgs = 1-200 nC) must be supplied and removed each switching cycle — at high frequency, gate drive power (Pgate = Qgs × Vgs × fsw) becomes significant and requires careful driver design

## Thyristor (SCR — Silicon Controlled Rectifier)

Four-layer pnpn device. Latches on when gate current is applied while anode is positive relative to cathode. Remains conducting until anode current drops below holding current (Ih, typically 5-50 mA). Used for AC power control (light dimmers, motor speed control, HVDC transmission).

1. **Starting wafer**: n-type silicon, 20-100 Ω·cm (high resistivity for high voltage blocking), 300-500 μm.
2. **p-type diffusion** (both sides): Boron diffusion at 1100-1200°C forms p layers. Drive-in to depth of 20-50 μm.
3. **n+ diffusion** (cathode side): Phosphorus diffusion, 5-15 μm deep, heavily doped.
4. **Gate region**: Etch window to p-base layer. Metallize for gate contact.
5. **Package**: Large-area devices (10-150 mm diameter die) in hockey-puck packages (disc-type, clamped between heat sinks with 5-30 kN force) or stud-mount (screw-base for easy mounting on heat sinks).

**Key parameters**: Vdrm (repetitive peak off-state voltage): 100-10,000V. It(av) (average on-state current): 1-5000A. Igt (gate trigger current): 5-200 mA. Vt (on-state voltage): 1.0-2.0V at rated current. di/dt rating: 50-500 A/μs (exceeding causes localized hot spots). dv/dt rating: 50-1000 V/μs (exceeding causes false triggering).

**Strengths**:
- Highest voltage and current capability of any semiconductor switch (up to 10,000V, 5000A in a single device) — a 150 mm diameter thyristor die handles power levels that would require hundreds of paralleled MOSFETs
- Low on-state voltage (1.0-2.0V) at rated current provides efficient conduction — lower total loss than MOSFET or IGBT at very high current due to the double-sided injection from the pnpn structure
- Self-latching: once triggered, the thyristor remains conducting without continuous gate drive — simplifies control circuitry for AC phase-angle power control and HVDC transmission

**Weaknesses**:
- Cannot be turned off by the gate — current must be forced below the holding current (5-50 mA) by external circuit action (natural AC zero-crossing or forced commutation), making thyristors unsuitable for DC circuit breaking or PWM applications
- Susceptible to false triggering from rapid voltage transients (dv/dt > 50-1000 V/μs) — requires snubber circuits (RC network across the device) that add cost and complexity
- Slow turn-on (di/dt limited to 50-500 A/μs) — the conducting area spreads from the gate region at ~0.1 mm/μs, creating localized hot spots if current rises faster than the conducting area expands

## Quantitative Parameters

## Diode Parameters

| Parameter | Signal Diode (1N4148) | Rectifier Diode (1N5408) | Schottky (1N5822) | Zener (1N4736A) |
|-----------|----------------------|--------------------------|-------------------|-----------------|
| Forward voltage (Vf) | 0.6-0.7V at 10 mA | 0.7-1.0V at 3A | 0.2-0.4V at 3A | — |
| Reverse voltage (Vr) | 75-100V | 1000V | 40V | — (breakdown = 6.8V) |
| Forward current (If) | 300 mA | 3A | 3A | — (Izt = 76 mA) |
| Reverse leakage (Ir) | 25 nA at 75V | 10 μA at 1000V | 1-5 mA at 40V | — |
| Reverse recovery (trr) | 4 ns | 2-10 μs | <50 ns | — |
| Junction capacitance | 4 pF at 0V | 20-50 pF | 100-200 pF | — |
| Power dissipation | 500 mW | 3W (with leads) | 3W | 1W |
| Operating temperature | -65 to 200°C | -65 to 175°C | -65 to 150°C | -65 to 200°C |

## BJT Parameters

| Parameter | Small-Signal (2N3904) | Power (TIP31C) | Darlington (TIP122) | RF (2N2222) |
|-----------|----------------------|----------------|---------------------|-------------|
| Type | NPN | NPN | NPN | NPN |
| Vceo (max) | 40V | 100V | 100V | 40V |
| Ic (max) | 200 mA | 3A | 5A | 800 mA |
| β (hFE) | 100-400 | 10-100 | 1000-20,000 | 50-300 |
| Ft | 300 MHz | 3 MHz | — | 300-600 MHz |
| Vce(sat) | 0.2-0.3V | 0.2-1.2V | 1.5-2.5V | 0.3-1.0V |
| Power dissipation | 625 mW | 40W (on heatsink) | 65W (on heatsink) | 1.8W |
| Package | TO-92 | TO-220 | TO-220 | TO-18/TO-92 |

## MOSFET Parameters

| Parameter | Logic-Level (2N7002) | Standard (IRF540N) | High-Voltage (FQA11N90) | Low-Rds (IRL3803) |
|-----------|---------------------|---------------------|-------------------------|-------------------|
| Vds(max) | 60V | 100V | 900V | 30V |
| Id(max) | 0.34A | 33A | 11A | 140A |
| Rds(on) | 1.2-5.0 Ω | 0.044 Ω | 1.1 Ω | 0.004 Ω |
| Vgs(th) | 1.0-2.5V | 2.0-4.0V | 3.0-5.0V | 1.0-2.0V |
| Qgs(total) | 1-3 nC | 71 nC | 38 nC | 160 nC |
| Switching time | 10-30 ns | 30-100 ns | 50-150 ns | 20-60 ns |
| Power dissipation | 0.35W | 130W (heatsink) | 250W (heatsink) | 200W (heatsink) |
| Package | SOT-23 | TO-220 | TO-247 | TO-220 |

## Thyristor Parameters

| Parameter | Sensitive Gate (MCR100) | Standard (2N6509) | Power (SKKT106) | High-Voltage (5STP 52) |
|-----------|------------------------|--------------------|-----------------|----------------------|
| Vdrm | 400V | 800V | 1600V | 8500V |
| It(av) | 0.8A | 12A | 115A | 5200A |
| Igt (gate trigger) | 0.2 mA | 30 mA | 150 mA | 300 mA |
| Vt (on-state voltage) | 1.6V | 1.5V | 1.3V | 1.5V |
| Ih (holding current) | 5 mA | 40 mA | 300 mA | 500 mA |
| di/dt | 50 A/μs | 100 A/μs | 200 A/μs | 500 A/μs |
| Package | TO-92 | TO-220 | Disc (hockey-puck) | Disc (hockey-puck) |

## Scaling Notes

## From Discrete to Integrated

- **Discrete devices** (1-10 mm² die): Individual diodes, transistors, thyristors in their own packages. Simple fabrication (3-6 lithography steps). Yield per die: 95-99%. Used for power applications and prototyping.
- **Small-scale integration (SSI)**: 1-100 transistors on one die. 6-10 lithography steps. Yield: 80-95%. Logic gates, flip-flops, op-amps.
- **Large-scale integration (LSI)**: 1,000-100,000 transistors. 10-20 lithography steps. Requires [photolithography](../photolithography/fab-processes.md) processes.
- **VLSI/ULSI**: >100,000 transistors. 20-40+ lithography steps. Microprocessors, memory, GPUs. Covered in [VLSI Scaling](../vlsi-scaling/index.md).

## Power Device Scaling

Power semiconductor capability scales with die area and blocking voltage. Key trade-off: Rds(on) ∝ Vds²·⁵ for silicon MOSFETs. For applications above ~600V, IGBTs (Insulated Gate Bipolar Transistors) are preferred — they combine MOSFET gate drive simplicity with BJT-like conduction at high voltage.

| Power Level | Device Type | Die Size | Package | Typical Application |
|-------------|-----------|----------|---------|-------------------|
| <1W | Signal diode/small BJT | 0.25 × 0.25 mm | SOT-23, TO-92 | Logic, signal conditioning |
| 1-50W | Medium-power MOSFET | 2 × 2 mm | TO-220, D²PAK | Motor drives, DC-DC converters |
| 50-500W | Power MOSFET/IGBT | 5 × 5 mm | TO-247, SOT-227 | Inverters, SMPS, welding |
| 500W-10kW | Large-area MOSFET/IGBT | 10-25 mm dia | Module (multi-die) | Industrial drives, EV traction |
| >10kW | Thyristor/GTO/IGCT | 25-150 mm dia | Disc (hockey-puck) | HVDC, FACTS, steel melting |

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| BJT β much lower than expected | Base width too wide (insufficient diffusion drive-in) | Increase drive-in temperature or time; verify furnace temperature uniformity |
| MOSFET Vth too high | Gate oxide too thick, or fixed oxide charge too high | Reduce oxidation time/temperature; improve pre-oxidation clean; check for contamination |
| MOSFET gate leakage | Gate oxide pinhole defect from contamination | Improve cleanroom practice; use filtered gases; reduce oxidation temperature for better oxide quality |
| Diode high reverse leakage | Incomplete junction formation, surface contamination, crystal defects | Extend diffusion time; improve surface passivation (grow thermal oxide over junction); check wafer quality |
| Thyristor false triggering | dv/dt exceeds rating, noise on gate terminal | Add snubber circuit (RC across device: R = 10-100 Ω, C = 0.1-1.0 μF); shield gate trace; add gate-cathode resistor (100-1000 Ω) |
| Thermal runaway (power device) | Positive temperature coefficient of leakage current | Ensure adequate heatsinking; add emitter/source ballast resistance; derate power at high ambient temperature |
| MOSFET failure during switching | Voltage spike from inductive load exceeds Vds(max) | Add freewheeling diode across inductive load; use avalanche-rated MOSFET; increase gate resistor to slow switching (reduces spike but increases switching loss) |
| BJT secondary breakdown | Localized hot spot from non-uniform current distribution at high Vce and high Ic simultaneously | Operate within safe operating area (SOA) curve; use MOSFETs instead for linear applications; add emitter ballast resistors for parallel operation |
| Wire bond failure in package | Thermal cycling fatigue, moisture-induced corrosion | Use gold wire for high-reliability; control molding compound moisture; follow MSL handling procedures |

## Safety

- **Hydrogen gas**: Wet oxidation and epitaxial deposition use H₂ gas. Hydrogen is explosive at 4-75% concentration in air. Use hydrogen detectors, adequate ventilation, and nitrogen purge before introducing hydrogen. Never use open flames near hydrogen systems.
- **Dopant gases**: PH₃ (phosphine), B₂H₆ (diborane), AsH₃ (arsine) are extremely toxic (TLV: 0.3 ppm for PH₃, 0.05 ppm for AsH₃). All are pyrophoric (ignite spontaneously in air). Use in gas cabinets with continuous monitoring, automatic shutoff, and exhaust scrubbing. Emergency procedures: evacuate immediately if leak detected. Liquid dopants (POCl₃, BBr₃) are less immediately dangerous but are corrosive and moisture-sensitive (react with humidity to release toxic fumes).
- **Hydrofluoric acid (HF)**: Used for oxide etching in wafer processing. HF is a contact poison — it penetrates skin, binds calcium, and causes deep tissue necrosis that may not be immediately painful. Even small exposures (<2% body surface area) can cause fatal systemic hypocalcemia. ALWAYS wear HF-rated gloves (neoprene or nitrile), face shield, and apron. Calcium gluconate gel must be immediately available at the workstation — apply to any skin contact and seek emergency medical treatment.
- **Arsenic and heavy metals**: Some dopant sources and III-V semiconductors (GaAs, InP) contain arsenic. Arsenic is a cumulative poison. Handle in ventilated enclosures. Wash hands thoroughly after handling. Industrial hygiene monitoring required for arsenic exposure.
- **High-temperature furnaces**: Diffusion and oxidation furnaces operate at 900-1200°C. External surfaces: 50-80°C (burn risk). Loading/unloading wafers requires long quartz loading rods — hot wafers and quartz ware cause severe burns. Use thermal gloves rated to 500°C. Gas burn hazard: furnace exhaust gases may be hot and contain toxic species.
- **Electrical testing of power devices**: High-voltage devices are tested at hundreds to thousands of volts. Capacitive energy storage in test equipment can deliver lethal shocks. Use insulated probes, discharge capacitors before handling, and maintain one-hand rule (never have both hands in the test fixture simultaneously).

## Quality Control

## Wafer-Level Tests (Probe Test)
- **Die-by-die probe**: Automated probe card contacts each die on the wafer. Measures key parameters: Vf (diodes), β and Vce(sat) (BJTs), Vth and Rds(on) (MOSFETs), Vdrm and Igt (thyristors). Inking or electronic mapping of failed die. Wafer probe yield target: 85-98% depending on die size and process maturity.
- **Breakdown voltage test**: Ramp voltage to rated Vdrm/Vceo/Vds and verify leakage is within spec. Apply 10-20% above rated for screening.

## Package-Level Tests
- **Parameter verification**: 100% tested at final test. All datasheet parameters within specification at 25°C.
- **Burn-in**: Power devices stressed at 100-150°C, rated voltage and current for 24-168 hours. Eliminates infant mortality failures. Failure rate during burn-in: 0.1-2%. Power cycling (on/off cycles) for MOSFETs and IGBTs: 10,000-100,000 cycles.
- **Hermeticity test** (ceramic/metal packages): Fine leak: <1×10⁻⁸ atm·cm³/s He (helium mass spectrometer). Gross leak: bubble test in fluorocarbon fluid at 125°C.
- **Visual inspection**: Optical microscope at 10-40× for wire bonds, die attach, mold defects, lead condition.

## Reliability Qualification
- **High-temperature operating life (HTOL)**: 1000 hours at 125°C junction temperature under bias. Parameter drift <10%.
- **Temperature cycling**: -65°C to +150°C, 500-1000 cycles. Checks die attach, wire bond, and package integrity.
- **Highly accelerated stress test (HAST)**: 130°C, 85% RH, 96 hours under bias. Tests moisture resistance.
- **Electrostatic discharge (ESD)**: HBM (Human Body Model): 100 pF through 1.5 kΩ. MOSFETs: 200-2000V rating. Diodes: 2000-15,000V.

## Variations and Alternatives

## Device Technology Trade-offs

| Application | Best Device | Reason | Alternative |
|-------------|-----------|--------|-------------|
| Low-voltage rectification | Schottky diode | Low Vf (0.2-0.4V), fast switching | PN diode (higher Vf but lower leakage) |
| High-voltage rectification | Fast recovery PN diode | High voltage rating, moderate speed | SiC Schottky (lower Vf, faster, but expensive) |
| Low-frequency power switching | BJT | Low Vce(sat), mature technology | MOSFET (easier drive but higher Rds(on) at high voltage) |
| High-frequency power switching | MOSFET | Fast switching, voltage-driven | GaN HEMT (faster, lower loss, but expensive and fragile) |
| Very high voltage power | IGBT | Combines MOS gate with BJT conduction | Thyristor (highest power but cannot turn off via gate) |
| AC power control | Thyristor (SCR/Triac) | Latching, self-commutating in AC | MOSFET + controller (more flexible but more complex) |
| Voltage reference | Zener diode | Simple, low cost | Bandgap reference (better accuracy and TC) |
| Logic switching | MOSFET (CMOS) | Zero static power, high density | BJT (ECL — faster but power-hungry) |

## Emerging Wide-Bandgap Semiconductors

| Property | Silicon (Si) | Silicon Carbide (SiC) | Gallium Nitride (GaN) |
|----------|-------------|----------------------|----------------------|
| Band gap | 1.12 eV | 3.26 eV | 3.39 eV |
| Breakdown field | 0.3 MV/cm | 3.0 MV/cm | 3.3 MV/cm |
| Thermal conductivity | 1.5 W/cm·K | 4.9 W/cm·K | 1.3 W/cm·K |
| Maximum operating temperature | 150-200°C | 300-600°C | 200-400°C |
| Electron mobility | 1400 cm²/V·s | 900 cm²/V·s | 2000 cm²/V·s |
| On-resistance (relative, same voltage) | 1× | 1/100× | 1/300× |
| Switching frequency (practical max) | 1-10 MHz | 10-100 MHz | 100-1000 MHz |
| Status in bootstrap | Standard | Advanced (Year 60+) | Advanced (Year 80+) |

## Historical Bootstrap Path

1. **Crystal diode** (Year 15-20): Cat's whisker detector — galena (PbS) crystal with fine wire contact. Unreliable but demonstrates rectification. Silicon crystal detectors for early radio.
2. **Germanium diode and transistor** (Year 25-30): Lower processing temperature (Ge melts at 938°C vs. Si at 1414°C). Point-contact transistor (fragile, unreliable). Alloy junction transistor. Germanium has lower band gap (0.67 eV) — higher leakage at elevated temperature. First practical transistors used germanium because it required lower purity than silicon.
3. **Silicon planar transistor** (Year 30-40): Oxide-passivated junction (planar process). Revolutionized reliability. Silicon's higher band gap (1.12 eV) enables operation up to 200°C junction temperature.
4. **Power MOSFET** (Year 35-45): Vertical DMOS structure enables high voltage and high current. Rds(on) steadily decreasing with each generation.
5. **IGBT** (Year 40-50): Combines MOS gate drive with bipolar conduction. Dominates medium-to-high power conversion (1 kW to 10 MW).

## See Also

- **[Basic Semiconductor Devices](../silicon/basic-devices.md)**: wafer-level processes for creating pn junctions and basic devices
- **[Passive Components](passive-components.md)**: resistors, capacitors, and inductors used in circuits with semiconductor devices
- **[Power Electronics](power-electronics.md)**: converters that use diodes, transistors, and thyristors as switching elements
- **[Electronics Assembly](assembly.md)**: packaging and soldering of discrete semiconductor devices
- **[Photolithography Fab Processes](../photolithography/fab-processes.md)**: IC fabrication processes for integrated circuits
- **[Cleanrooms](../photolithography/cleanrooms.md)**: controlled environments required for semiconductor processing
- **[Vacuum Systems](../gas-handling/vacuum.md)**: vacuum equipment for deposition processes
- **[Electric Furnaces](../energy/electric-furnaces.md)**: diffusion and oxidation furnace requirements



[← Back to Electronics](index.md)
