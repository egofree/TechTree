# Radio Communication

> **Node ID**: telecom.radio
> **Domain**: [Telecommunications](./index.md)
> **Dependencies**: [`energy.electricity`](../energy/electricity.md), [`glass`](../glass/index.md), [`metals`](../metals/index.md), [`telecom.electric-telegraph`](electric-telegraph.md)
> **Enables**: [`telecom.submarine-cables`](submarine-cables.md), [`telecom.telephone`](telephone.md)
> **Timeline**: Years 30-60
> **Outputs**: radio_communication, wireless_telegraphy, broadcast_capability
> **Critical**: No — communication accelerates coordination but is not strictly required for survival

## Problem

Wired communication (telegraph, telephone) requires physical infrastructure — poles, wires, and cable-laying across terrain. This limits communication to locations connected by wire, making it impossible to reach ships at sea, aircraft in flight, or remote settlements without enormous infrastructure investment. Radio communication eliminates the wire: electromagnetic waves propagate through free space, carrying information across oceans and over mountains with no physical connection between transmitter and receiver. The challenge is generating, modulating, detecting, and amplifying these waves with the technology available at each stage of the bootstrapping process — from spark-gap transmitters and crystal detectors (requiring only basic electrical components) to vacuum tube transmitters and superheterodyne receivers (requiring glassblowing and vacuum technology).

## Prerequisites

- [Electricity](../energy/electricity.md) — power generation for transmitters and receivers
- [Electric Telegraph](electric-telegraph.md) — Morse code, keying techniques, and telegraph operating practice
- [Glass](../glass/index.md) — vacuum tube envelopes and Leyden jar capacitors
- [Metals](../metals/index.md) — copper wire for coils and antennas, brass for spark gaps, tungsten for tube filaments
- [Semiconductor materials](../electronics/index.md) — mineral crystals for detector diodes (galena, carborundum)


Radio communication transmits information via electromagnetic waves propagating through free space, eliminating the need for wires between transmitter and receiver. The progression from spark-gap transmitters (1895-1910) through crystal detectors to vacuum tube transmitters and receivers (1906-1920) represents one of the most rapid technology evolutions in history — from laboratory curiosity to intercontinental communication in under 20 years.

Radio enables communication with ships at sea, aircraft in flight, and remote locations where wire installation is impractical. It is the foundation of broadcast (one-to-many) communication, transforming information distribution from point-to-point to mass media.

## Electromagnetic Wave Propagation Fundamentals

**Frequency and wavelength**: wavelength = c/f, where c is the speed of light (3 x 10^8 m/s) and f is frequency. The radio spectrum spans from ~3 kHz (wavelength = 100 km) to ~300 GHz (wavelength = 1 mm). Early radio operated at 100-1000 kHz (wavelengths 300-3000 m), known as the "long wave" band.

**Ground wave**: Low-frequency radio waves (below ~500 kHz) follow the curvature of the Earth via diffraction. This allows reliable over-the-horizon communication up to 1,000-2,000 km without any ionospheric reflection. Ground wave range depends on frequency (lower = farther), transmitter power, and ground conductivity (seawater is excellent; dry soil is poor).

**Sky wave (ionospheric reflection)**: Medium and high-frequency waves (3-30 MHz) are reflected by the ionosphere (layers of ionized gas at 80-300 km altitude) back to Earth, enabling intercontinental communication. The ionosphere's reflective properties vary with time of day, season, and sunspot cycle — sky wave communication is inherently variable.

**Path loss**: Signal strength decreases with distance. Free-space path loss: L = (4*pi*d/wavelength)^2. For a 300 kHz signal at 100 km: L ~ 62 dB. At 500 km: L ~ 76 dB. Each doubling of distance adds ~6 dB of loss.

## Spark-Gap Transmitter (1895-1910)

The first practical radio transmitter. A high-voltage spark across a gap excites a tuned circuit (inductor + capacitor) that rings at its resonant frequency, producing damped radio-frequency oscillations radiated from an antenna wire.

**Circuit**:
1. **Power source**: Battery-powered induction coil (Ruhmkorff coil) producing 10-50 kV.
2. **Capacitor (Leyden jar)**: Glass plate with tin foil on both sides, 500-2000 pF, rated to 20-50 kV.
3. **Spark gap**: Two brass balls (10-30 mm diameter) separated by 1-5 mm adjustable gap.
4. **Tuned circuit**: Inductor (50-500 uH) connected in parallel with the capacitor. Resonant frequency: f = 1/(2*pi*sqrt(LC)). For L = 200 uH and C = 1000 pF: f = 356 kHz.
5. **Antenna**: Vertical wire or mast connected to one end of the tuned circuit; the other end connects to ground.

**Keying**: The telegraph key interrupts power to the induction coil. Key down = spark fires continuously. Key up = no spark. Morse code dots and dashes modulate the burst train duration.

**Fundamental limitation**: The spark gap transmitter radiates on many frequencies simultaneously (broadband emission). A single transmitter creates interference across a wide swath of the radio spectrum. By 1910-1912, regulatory pressure demanded narrower-band transmissions, driving the transition to arc transmitters and vacuum tube oscillators.

## Crystal Detector Receiver (1900-1920)

The simplest radio receiver — no power source required. The antenna picks up the radio signal, a tuned circuit selects the desired frequency, and a crystal detector rectifies the RF to recover the audio envelope. High-impedance headphones convert the audio to sound.

**Circuit**:
1. **Antenna**: Long wire (20-50 m) as high as possible.
2. **Ground**: Buried copper wire or metal water pipe. A poor ground reduces sensitivity by 50-80%.
3. **Tuned circuit**: Variable inductor in parallel with variable capacitor (50-500 pF). Adjust L and C to resonate at the transmitter's frequency.
4. **Crystal detector**: A semiconductor diode formed by a mineral crystal and a thin wire ("cat's whisker") contact.
5. **Headphones**: High-impedance magnetic headphones (2000-4000 ohm), producing audible sound from microwatt-level signals.

**Crystal types**:
- **Galena (PbS)**: Most common. Cat's whisker (fine phosphor bronze wire, 0.05-0.1 mm) adjusted to find a sensitive spot. Sensitivity varies across the crystal face.
- **Carborundum (SiC)**: More stable but less sensitive. Used with DC bias voltage (~1 V). Fixed pressure contact — no cat's whisker adjustment needed.
- **Iron pyrite (FeS2)**: Less common but reasonably sensitive and more stable than galena.

**Sensitivity**: A crystal receiver with a good antenna can detect signals from a 1 kW spark transmitter at 100-300 km. Limiting factor is headphone sensitivity — must produce audible sound from signals as weak as 1-10 uW.

## Vacuum Tube Development (1904-1920)

The vacuum tube transformed radio from a limited point-to-point technology into a universal communication medium.

**Fleming valve (diode, 1904)**:
- Heated filament (cathode) emits electrons inside an evacuated glass bulb. Metal plate (anode) collects electrons. Current flows only when plate is positive relative to filament (rectification).
- **Construction**: Glass bulb (50-100 ml), evacuated to ~10^-3 Torr. Tungsten filament (~2000C). Nickel plate (10-20 mm diameter). Brass pins in phenolic base.
- **Parameters**: Filament 2-6 V, 0.5-2 A. Plate 20-100 V. Plate current 1-10 mA. Forward resistance ~1-5 kohm. Reverse resistance >1 Mohm.

**de Forest Audion (triode, 1906)**:
- Adds a **grid** (wire mesh between filament and plate). Small grid voltage changes produce large plate current changes — **amplification**.
- **Amplification factor**: Early Audions: mu = 3-10. Later triodes (1915-1925): mu = 8-100.
- **Transconductance**: 0.5-5 mA/V. A single triode stage provides voltage gain of 10-50x. Multiple stages provide gains of 1,000-100,000x.

**Feedback oscillator (1912-1913)**:
- Feed triode output back to the grid through a tuned circuit. If feedback is positive and sufficient, the tube oscillates continuously at the tuned frequency. Replaces the spark gap with a clean, single-frequency, continuous-wave (CW) transmitter.
- **Advantages over spark gap**: Single frequency (no broadband interference), continuous wave, frequency stability, much higher efficiency (20-50% vs. 10-30%).
- **Frequency range**: 20 kHz to 30 MHz with appropriate LC values.

## Antenna Systems

**Marconi antenna (monopole)**: Vertical wire or mast, grounded at the base. For a quarter-wave antenna at 300 kHz (wavelength = 1000 m), ideal height is 250 m — impractical. Short antennas (20-100 m) work but with reduced efficiency. A 50 m vertical wire at 300 kHz has radiation efficiency ~5-15%.

**Loading coil**: For electrically short antennas, a series inductor at the base resonates the antenna at the desired frequency. A 50 m antenna at 300 kHz needs ~200-400 uH.

**Ground system**: Buried copper wire radials (10-20 wires, each 100+ m at 300 kHz). Good ground resistance: <5 ohm. Poor ground (>20 ohm) wastes 50-80% of transmitter power.

## Radio Receiver Evolution

**Regenerative receiver (Armstrong, 1912)**: A triode amplifier with controlled positive feedback. Provides gain equivalent to 3-5 stages of conventional amplification in a single tube. However, excessive feedback causes oscillation — the receiver becomes a transmitter, interfering with nearby receivers.

**Superheterodyne receiver (Armstrong, 1918)**: The dominant receiver architecture for 100+ years. The incoming RF signal is mixed with a local oscillator to produce an intermediate frequency (IF, typically 455 kHz for AM). IF stages provide fixed-frequency amplification and filtering, offering superior selectivity and stability.

## Bill of Materials

## Spark-Gap Transmitter Station (1 kW)

| Material | Quantity | Specification | Source |
|----------|----------|---------------|--------|
| Induction coil (Ruhmkorff) | 1 | 10-50 kV output, battery powered | [Metals](../metals/index.md) |
| Leyden jars (capacitors) | 2-6 | Glass/tin foil, 500-2000 pF, 20-50 kV rating | [Glass](../glass/index.md) |
| Spark gap electrodes | 2-4 | Brass balls, 10-30 mm diameter, adjustable | [Metals](../metals/index.md) |
| Tuning inductor | 1 | Air-core solenoid, 50-500 uH, heavy copper wire | [Metals](../metals/index.md) |
| Antenna wire (copper) | 200-500 m | Stranded copper, 2-4 mm diameter | [Metals](../metals/index.md) |
| Ground wire + plates | 50-100 m + 2-4 plates | Copper wire 4 mm, copper plates 30x30 cm | [Metals](../metals/index.md) |
| Telegraph key | 1 | Heavy-duty contact key | [Metals](../metals/index.md) |
| Battery (primary cells) | 6-12 V bank | Lead-acid or Leclanche, 1-5 kW capacity | [Chemistry](../chemistry/index.md) |

## Crystal Receiver Station

| Material | Quantity | Specification | Source |
|----------|----------|---------------|--------|
| Antenna wire (copper) | 50-100 m | Stranded copper, 1-2 mm diameter | [Metals](../metals/index.md) |
| Variable inductor | 1 | Single-layer solenoid with sliding contact, 50-500 uH | [Metals](../metals/index.md) |
| Variable capacitor | 1 | Air variable, 50-500 pF | [Metals](../metals/index.md) |
| Crystal detector (galena) | 1 | PbS crystal in cup with cat's whisker | [Mining](../mining/index.md) |
| Headphones | 1 pair | 2000-4000 ohm magnetic, high sensitivity | [Metals](../metals/index.md) |
| Ground rod/wire | 1 | Copper rod 1-2 m + 10 m wire | [Metals](../metals/index.md) |

## Quantitative Parameters

## Transmitter Specifications by Era

| Parameter | Spark Gap (1895-1910) | Vacuum Tube CW (1915-1930) |
|-----------|----------------------|---------------------------|
| Frequency range | 100-1000 kHz | 20 kHz - 30 MHz |
| Transmitter power (input) | 0.5-10 kW | 0.1-50 kW |
| Radiated bandwidth | 50-200 kHz (broadband) | 0.1-5 kHz (narrowband) |
| Radiated efficiency | 10-30% | 20-50% |
| Range (ground wave) | 50-500 km | 200-2000 km |
| Range (sky wave) | 200-3000 km | 500-15,000 km |
| Operating voltage | 10-50 kV | 50-2000 V (plate) |

## Receiver Sensitivity by Type

| Receiver Type | Minimum Detectable Signal | Power Required | Selectivity |
|---------------|--------------------------|----------------|-------------|
| Crystal detector | ~10 uW | Zero (passive) | Poor (broadband) |
| Regenerative (1 tube) | ~1 uW | 5-10 W (filament + plate) | Good (with regeneration) |
| Superheterodyne (5 tubes) | ~0.1 uW | 10-20 W (filament + plate) | Excellent (IF filtering) |

## Vacuum Tube Operating Parameters

**Receiving tube** (Type 01A, 1920s):
- Filament: 5.0 V, 0.25 A (1.25 W). Plate: 45-90 V, 1.5-3.0 mA. Grid bias: -4.5 to -9.0 V.
- Amplification factor: 8. Transconductance: 0.3-0.5 mA/V.

**Power supply for a 5-tube receiver**:
- A battery (filament): 5 V, 1.25 A = 6.25 W. Lead-acid, recharged weekly.
- B battery (plate): 90 V, 15 mA = 1.35 W. Dry cells (replaced monthly).
- C battery (grid bias): -4.5 V, negligible current. Lasts 6-12 months.

**Transmitter tube** (Type UV-204A, 250 W): Filament 11 V / 3.5 A = 38.5 W. Plate: 1000-2000 V at 150-250 mA. RF output: ~150-200 W (60-75% efficiency). Tube life: 1,000-3,000 hours.

## Frequency Bands and Propagation Characteristics

| Band | Frequency | Wavelength | Primary Mode | Typical Range |
|------|-----------|-----------|--------------|---------------|
| Long wave (LF) | 30-300 kHz | 1-10 km | Ground wave | 500-2,000 km |
| Medium wave (MF) | 300-3000 kHz | 100-1000 m | Ground + sky wave | 100-2,000 km |
| Short wave (HF) | 3-30 MHz | 10-100 m | Sky wave (ionospheric) | 500-15,000 km |
| Very high freq (VHF) | 30-300 MHz | 1-10 m | Line of sight | 5-100 km |

## Scaling Notes

## Short-Range Station (5-50 km)

Crystal receiver + low-power spark or tube transmitter (0.1-0.5 kW). Ship-to-shore, harbor communication, local military coordination. Antenna height: 10-30 m. Construction cost: $200-500. No amplification needed at receiver if transmitter is within 50 km. Operating power: 100-500 W transmitter, zero for crystal receivers.

## Medium-Range Station (50-500 km)

1-5 kW tube transmitter + regenerative or superheterodyne receiver. Ground wave propagation on long wave (150-500 kHz). Antenna: 30-80 m vertical mast with ground radials. Requires skilled operator for tuning and maintenance. Construction cost: $2,000-10,000. Typical shore-to-ship service radius.

## Long-Range / Intercontinental Station (1,000-15,000 km)

10-50 kW tube transmitter + directional antenna arrays. Sky wave propagation on short wave (5-25 MHz). Antenna: 50-200 m masts or horizontal wire arrays. Requires frequency selection based on time of day, season, and sunspot cycle. Construction cost: $50,000-500,000. Staff: 10-30 technicians for 24-hour operation. The minimum practical transmitter for reliable intercontinental communication is 5 kW with a well-engineered antenna.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| No signal received (crystal set) | Cat's whisker not on sensitive spot; antenna too short; poor ground | Probe crystal surface with whisker until signal peaks; lengthen antenna to 30+ m; improve ground connection (bury more copper wire) |
| Weak signal at distance | Antenna too short for frequency; poor ground conductivity; low transmitter power | Add loading coil to resonate short antenna; install ground radials; increase transmitter power or improve antenna efficiency |
| Interference from other stations | Broadband spark transmission; poor receiver selectivity | Switch to vacuum tube CW transmitter (narrowband); use regenerative or superheterodyne receiver with better selectivity |
| Receiver oscillation (regenerative) | Excessive feedback; coupling between antenna and detector | Reduce regeneration control; increase shielding between stages; add RF choke in antenna lead |
| Vacuum tube filament failure | Filament burnout (end of life); overvoltage from battery charging | Replace tube (1,000-3,000 hour life typical); regulate filament voltage to specification; use series resistor if battery voltage is high |
| Key clicking (interference) | Spark gap arcing during key-up; abrupt current interruption | Install key filter (RC network across key contacts); use shielded key enclosure; ensure spark gap quenching with magnetic blowout or rotary gap |
| Frequency drift | LC circuit temperature changes; mechanical vibration; poor component stability | Use rigid coil construction; shield tuned circuit from heat sources; allow warm-up time before critical transmissions |
| Audio distortion at receiver | Overdriven tube stages; overloaded headphones; detector non-linearity | Reduce RF gain; use higher-impedance headphones; adjust detector bias point (carborundum type) |

## Safety Considerations

- **High-voltage RF**: Spark gap transmitters produce 10-50 kV at the antenna. Vacuum tube transmitters produce 200-2000 V at the output. RF burns penetrate deep tissue. Maintain 2+ m clearance from the antenna during transmission. Ground the antenna when not transmitting.
- **Vacuum tube filament temperature**: Tungsten filaments operate at 2000-2500C. Tube envelopes reach 100-200C. Allow tubes to cool before handling. Keep flammable materials away from tube equipment.
- **B+ voltage**: Vacuum tube plate supplies deliver 50-300 V DC at 10-200 mA. Sufficient to cause cardiac fibrillation under wet conditions. Bleeder resistors must discharge filter capacitors when power is removed (capacitors store lethal charge for minutes after power-off).
- **Lead shielding**: Some high-power tubes used lead-glass envelopes for X-ray shielding. Broken tubes may release lead-containing glass fragments. Handle with gloves.
- **Mercury vapor tubes**: Some rectifier tubes contain liquid mercury. If the glass breaks, mercury contamination requires professional cleanup. Mercury vapor is toxic above 0.05 mg/m3.
- **Antenna tower climbing**: Masts for long-wave antennas are 20-200 m tall. Climbing requires safety harnesses, fall arrestors, and two-person teams. Wind speed limit: 50 km/h for safe climbing.
- **Ozone and nitrogen oxides**: Spark gaps produce ozone (O3) and nitrogen oxides (NOx) from the air. These are lung irritants. Ventilate the transmitter room.
- **RF burns**: Antenna terminals carry high-voltage RF during transmission. RF burns are deep and slow to heal. Never touch the antenna during transmission.

## See Also

- [Electrical Telegraph Networks](electric-telegraph.md) — Morse code and wire-based telegraph systems
- [Telephone Systems](telephone.md) — wire-based voice communication
- [Submarine Cables](submarine-cables.md) — undersea cable communication
- [Electricity](../energy/electricity.md) — electrical generation and distribution
- [Glass](../glass/index.md) — glass for vacuum tube envelopes and Leyden jars
- [Semiconductor](../electronics/index.md) — crystal detectors and early solid-state devices
- [Electromechanical Computing](../computing/electromechanical.md) — relay-based switching for telecom networks
- [Data Storage](../computing/data-storage.md) — magnetic recording for signal logging
- [Measurement / Electrical Instruments](../measurement/electrical-instruments.md) — galvanometers, oscilloscopes, and signal measurement

[← Back to Telecom](index.md)
