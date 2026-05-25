# Radio Communication

> **Node ID**: telecom.radio
> **Domain**: [Telecommunications](./index.md)
> **Dependencies**: [`energy.electricity`](../energy/electricity.md), `glass`, `metals`, [`telecom.electric-telegraph`](electric-telegraph.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 30-60
> **Outputs**: radio_communication, wireless_telegraphy, broadcast_capability

### Overview

Radio communication transmits information via electromagnetic waves propagating through free space, eliminating the need for wires between transmitter and receiver. The progression from spark-gap transmitters (1895-1910) through crystal detectors to vacuum tube transmitters and receivers (1906-1920) represents one of the most rapid technology evolutions in history — from laboratory curiosity to intercontinental communication in under 20 years.

Radio enables communication with ships at sea, aircraft in flight, and remote locations where wire installation is impractical. It is the foundation of broadcast (one-to-many) communication, transforming information distribution from point-to-point to mass media.

### Electromagnetic Wave Propagation Fundamentals

**Frequency and wavelength**: λ = c/f, where c is the speed of light (3 × 10⁸ m/s) and f is frequency. The radio spectrum spans from ~3 kHz (λ = 100 km) to ~300 GHz (λ = 1 mm). Early radio operated at 100-1000 kHz (wavelengths 300-3000 m), known as the "long wave" band.

**Ground wave**: Low-frequency radio waves (below ~500 kHz) follow the curvature of the Earth via diffraction. This allows reliable over-the-horizon communication up to 1,000-2,000 km without any ionospheric reflection. Ground wave range depends on frequency (lower = farther), transmitter power, and ground conductivity (seawater is excellent; dry soil is poor).

**Sky wave (ionospheric reflection)**: Medium and high-frequency waves (3-30 MHz) are reflected by the ionosphere (layers of ionized gas at 80-300 km altitude) back to Earth, enabling intercontinental communication. The ionosphere's reflective properties vary with time of day, season, and sunspot cycle — sky wave communication is inherently variable.

**Path loss**: Signal strength decreases with distance. Free-space path loss: L = (4πd/λ)², where d is distance and λ is wavelength. For a 300 kHz signal (λ = 1000 m) at 100 km: L = (4π × 100,000 / 1000)² = (1257)² ≈ 62 dB. At 500 km: L ≈ 76 dB. Each doubling of distance adds ~6 dB of loss.

### Spark-Gap Transmitter (1895-1910)

The first practical radio transmitter. A high-voltage spark across a gap excites a tuned circuit (inductor + capacitor) that rings at its resonant frequency, producing damped radio-frequency oscillations. The oscillation radiates from an antenna wire as electromagnetic waves.

**Circuit**:
1. **Power source**: Battery-powered induction coil (Ruhmkorff coil) or AC transformer producing 10-50 kV. The induction coil's vibrator (a buzzer-like interrupter) repeatedly makes and breaks the primary circuit, generating a train of high-voltage pulses.
2. **Capacitor (Leyden jar)**: Glass plate with tin foil on both sides, 500-2000 pF, rated to 20-50 kV. Stores charge from the induction coil and releases it through the spark gap.
3. **Spark gap**: Two brass balls (10-30 mm diameter) separated by 1-5 mm adjustable gap. When capacitor voltage exceeds the breakdown voltage (V ≈ 30 kV/cm for air at standard pressure), a spark arcs across. The spark ionizes the air, creating a conductive plasma channel that allows the capacitor to discharge through the tuned circuit.
4. **Tuned circuit**: An inductor (air-core or single-layer solenoid, 50-500 μH) connected in parallel with the capacitor. When the spark fires, the LC circuit oscillates at its resonant frequency: f = 1/(2π√(LC)). For L = 200 μH and C = 1000 pF: f = 356 kHz (λ = 843 m). The oscillation is heavily damped — each spark produces 5-20 cycles of decaying RF energy.
5. **Antenna**: A vertical wire or mast, connected to one end of the tuned circuit. The antenna radiates the RF energy as electromagnetic waves. The other end of the circuit connects to ground (buried copper plates or wire mesh).

**Keying**: The telegraph key interrupts the power to the induction coil. Key down = spark fires continuously (producing a train of RF bursts at the spark repetition rate of 100-800 per second). Key up = no spark. The bursts are heard at the receiver as a loud buzz or crackle. Morse code dots and dashes modulate the burst train duration.

**Technical parameters**:
- **Transmitter power**: 0.5-10 kW (input power to the induction coil). Radiated power: 10-30% efficiency (most energy is lost as heat in the spark gap and circuit resistance). A 1 kW spark transmitter radiates ~100-300 W of RF.
- **Frequency range**: 100-1000 kHz (wavelengths 300-3000 m), determined by the LC circuit values. Early transmitters were broadband (radiating energy over a wide frequency range) — this is a fundamental limitation.
- **Range**: 50-500 km for ship-to-shore, 200-3,000 km for shore-to-shore with high-power transmitters and good antennas. Marconi's first transatlantic test (1901, Cornwall to Newfoundland, ~3,500 km) used a 10 kW transmitter and a 200 m antenna supported by kites.

**Fundamental limitation**: The spark gap transmitter radiates on many frequencies simultaneously (broadband emission). A single transmitter creates interference across a wide swath of the radio spectrum. As more transmitters came on air, mutual interference became crippling. By 1910-1912, regulatory pressure (Radio Act of 1912 in the US) demanded narrower-band transmissions, driving the transition to arc transmitters and vacuum tube oscillators.

**Safety**:
- **High voltage**: The induction coil output is 10-50 kV. Contact with the high-voltage side during operation causes severe electric shock or death. The spark gap operates in open air with continuous arcing — maintain 2 m clearance.
- **RF burns**: The antenna terminal carries high-voltage RF during transmission. RF burns are deep and slow to heal (they heat tissue below the skin surface). Never touch the antenna during transmission.
- **Fire hazard**: Sparks ignite flammable gases and vapors. Battery charging produces hydrogen. Keep spark transmitters away from battery rooms and fuel storage.
- **Mercury hazard**: Some spark gaps used mercury pools for self-healing contacts. Mercury vapor is toxic. Use in well-ventilated spaces.
- **Ozone and nitrogen oxides**: The spark produces ozone (O₃) and nitrogen oxides (NOx) from the air. These are lung irritants. Ventilate the transmitter room.

### Crystal Detector Receiver (1900-1920)

The simplest radio receiver — no power source required. The antenna picks up the radio signal, a tuned circuit selects the desired frequency, and a crystal detector rectifies the RF to recover the audio envelope. High-impedance headphones convert the audio to sound.

**Circuit**:
1. **Antenna**: A long wire (20-50 m) as high as possible. For best reception at 300 kHz, a quarter-wave antenna would be 250 m — impractical. Short antennas (20-50 m) work but with reduced efficiency.
2. **Ground**: Buried copper wire or a metal water pipe. The ground connection is essential — it provides the return path for the received signal. A poor ground reduces sensitivity by 50-80%.
3. **Tuned circuit**: A variable inductor (single-layer solenoid with a sliding contact or a variometer — two series-connected coils, one rotating inside the other) in parallel with a variable capacitor (air variable, 50-500 pF). The tuned circuit selects the desired frequency from all signals arriving at the antenna. Adjust L and C to resonate at the transmitter's frequency.
4. **Crystal detector**: A semiconductor diode formed by a mineral crystal and a thin wire ("cat's whisker") contact. The contact rectifies the RF signal, converting the amplitude-modulated RF into audio-frequency current.
5. **Headphones**: High-impedance magnetic headphones (2000-4000 Ω), sensitive enough to produce audible sound from the microwatt-level signals received. Crystal receivers produce no amplification — the headphones are the only output transducer.

**Crystal types**:
- **Galena (PbS, lead sulfide)**: The most common detector crystal. A galena crystal in a small cup with a cat's whisker (fine phosphor bronze or silver wire, 0.05-0.1 mm) that the operator adjusts to find a sensitive spot on the crystal surface. Sensitivity varies widely across the crystal face — finding a good spot requires patient probing. Once found, the spot may drift with vibration or temperature changes.
- **Carborundum (SiC, silicon carbide)**: More stable than galena but less sensitive. Used with a DC bias voltage (~1 V from a battery) to set the operating point in the most sensitive region of its current-voltage characteristic. Does not require the cat's-whisker adjustment — a fixed pressure contact works.
- **Iron pyrite (FeS₂)**: Less common but reasonably sensitive and more stable than galena.

**Sensitivity**: A crystal receiver with a good antenna can detect signals from a 1 kW spark transmitter at 100-300 km. The limiting factor is headphone sensitivity — the headphones must produce audible sound from signals as weak as 1-10 μW. High-impedance headphones (2000-4000 Ω) achieve this with carefully adjusted magnetic gaps and thin diaphragms.

### Vacuum Tube Development (1904-1920)

The vacuum tube transformed radio from a limited point-to-point technology into a universal communication medium. The key innovations were the diode (rectifier), the triode (amplifier), and feedback oscillators.

**Fleming valve (diode, 1904)**:
- A heated filament (cathode) emits electrons inside an evacuated glass bulb. A metal plate (anode) collects the electrons. Current flows only when the plate is positive relative to the filament (rectification). The Fleming valve replaced the crystal detector with a more reliable and sensitive rectifier.
- **Construction**: Glass bulb (50-100 ml), evacuated to ~10⁻³ Torr. Tungsten filament (operating at ~2000°C, bright orange glow). Nickel or molybdenum plate (10-20 mm diameter). Base: brass pins in a phenolic (Bakelite) base.
- **Operating parameters**: Filament voltage 2-6 V, filament current 0.5-2 A (significant power consumption). Plate voltage 20-100 V. Plate current 1-10 mA. Forward resistance: ~1-5 kΩ. Reverse resistance: >1 MΩ.
- **Limitation**: The diode detects but does not amplify. Signal strength at the receiver is still limited by the received power from the antenna.

**de Forest Audion (triode, 1906)**:
- Adds a third electrode — the **grid** (a wire mesh or zigzag wire between the filament and plate). The grid controls the electron flow from filament to plate. A small voltage change on the grid produces a large change in plate current — this is **amplification**.
- **Amplification factor (μ)**: Grid voltage change of 1 V produces the same plate current change as a plate voltage change of μ volts. Early Audions: μ = 3-10. Later triodes (1915-1925): μ = 8-100.
- **Transconductance (gm)**: The ratio of plate current change to grid voltage change. Typical: 0.5-5 mA/V. This determines how much the tube amplifies — higher gm = more gain.
- **Operation**: Filament heats cathode → electrons flow to plate. Grid voltage (a few volts) modulates this flow. The plate circuit (with a higher voltage supply, 50-200 V) reproduces the grid signal at higher power. A single triode stage provides voltage gain of 10-50×. Multiple stages in cascade provide gains of 1,000-100,000×.

**Feedback oscillator (Meissner, Armstrong, 1912-1913)**:
- Feed some of the triode's output back to the grid through a tuned circuit. If the feedback is positive (in phase) and sufficient to overcome circuit losses, the tube oscillates continuously at the tuned frequency. This replaces the spark gap with a clean, single-frequency, continuous-wave (CW) transmitter.
- **Advantages over spark gap**: Single frequency (no broadband interference), continuous wave (enables efficient receivers), frequency stability (determined by LC circuit, not spark discharge), and much higher efficiency (20-50% vs. 10-30%).
- **Frequency range**: 20 kHz to 30 MHz with appropriate LC values. The oscillator can generate any frequency within the radio spectrum.

### Antenna Systems

**Marconi antenna (monopole)**: A vertical wire or mast, grounded at the base. The Earth acts as the return conductor. For a quarter-wave antenna at 300 kHz (λ = 1000 m), the ideal height is 250 m — impractical for most installations. Short antennas (20-100 m) work but with reduced radiation efficiency. A 50 m vertical wire at 300 kHz has radiation efficiency of ~5-15% (most input power is dissipated as heat in the loading coil and ground resistance).

**Loading coil**: For electrically short antennas, a series inductor (loading coil) at the base resonates the antenna at the desired frequency. The loading coil compensates for the antenna's capacitive reactance. A 50 m antenna at 300 kHz needs a loading coil of ~200-400 μH. The coil must carry the full antenna current (5-50 A for a 1 kW transmitter) with low resistance to minimize loss.

**Ground system**: Buried copper wire radials (10-20 wires, each at least 0.1 wavelength long = 100+ m at 300 kHz). Good ground resistance: <5 Ω. Poor ground (>20 Ω) wastes 50-80% of transmitter power as heat in the ground connection. For shore stations, seawater provides an excellent ground (conductivity ~4 S/m) — a metal plate in the surf suffices.

**Antenna coupler**: A variable LC network that matches the transmitter's output impedance (typically 50-500 Ω) to the antenna's impedance (varies with frequency and antenna dimensions). Maximum power transfer requires impedance matching. A mismatched antenna reflects power back to the transmitter, reducing radiated power and potentially damaging the transmitter's output stage.

### Radio Receiver Evolution

**Regenerative receiver (Armstrong, 1912)**: A triode amplifier with controlled positive feedback. The feedback increases the effective Q of the tuned circuit, dramatically improving selectivity (ability to separate stations on adjacent frequencies) and sensitivity (ability to detect weak signals). A regenerative receiver provides gain equivalent to 3-5 stages of conventional amplification in a single tube. However, if the feedback is set too high, the receiver breaks into oscillation and becomes a transmitter itself — interfering with nearby receivers.

**Superheterodyne receiver (Armstrong, 1918)**: The receiver architecture that dominated radio for 100+ years. The incoming RF signal is mixed (heterodyned) with a local oscillator to produce an intermediate frequency (IF), typically 455 kHz for AM broadcast. The IF stages provide fixed-frequency amplification and filtering, offering much better selectivity and stability than direct RF amplification. The superheterodyne principle: convert any received frequency to a single, fixed IF for processing.

### Technical Specifications Summary

| Parameter | Spark Gap | Crystal Receiver | Vacuum Tube CW |
|-----------|-----------|-----------------|----------------|
| Frequency range | 100-1000 kHz | 100-3000 kHz | 20 kHz - 30 MHz |
| Transmitter power | 0.5-10 kW | N/A | 0.1-50 kW |
| Radiated bandwidth | 50-200 kHz (broadband) | N/A | 0.1-5 kHz (narrowband) |
| Range (ground wave) | 50-500 km | 100-300 km reception | 200-2000 km |
| Range (sky wave) | 200-3000 km | N/A | 500-15,000 km |
| Receiver sensitivity | N/A | ~10 μW | ~0.1 μW (superhet) |
| Operating voltage | 10-50 kV | None | 50-200 V (plate) |
| Power consumption | 0.5-10 kW | Zero | 10-500 W |

### Vacuum Tube Operating Parameters

**Typical triode specifications** (Type 01A, 1920s, representative early receiving tube):
- Filament voltage: 5.0 V (DC, from battery). Filament current: 0.25 A (power: 1.25 W just for the filament).
- Plate voltage: 45-90 V (from B battery). Plate current: 1.5-3.0 mA.
- Grid bias: -4.5 to -9.0 V (from C battery). Amplification factor (μ): 8. Transconductance (gm): 0.3-0.5 mA/V.

**Power supply for a 5-tube receiver**:
- A battery (filament): 5 V, 1.25 A = 6.25 W. Lead-acid storage battery, recharged weekly.
- B battery (plate): 90 V, 15 mA = 1.35 W. Dry cells (non-rechargeable, replaced monthly) — expensive (~$5 in 1925 for a set).
- C battery (grid bias): -4.5 V, negligible current. Small dry cell lasting 6-12 months.

**Transmitter tube** (Type UV-204A, 250 W): Filament 11 V / 3.5 A = 38.5 W. Plate: 1,000-2,000 V at 150-250 mA. Plate dissipation: 250 W. RF output: ~150-200 W (60-75% efficiency). Cooling: external fins + forced air. Tube life: 1,000-3,000 hours (filament burnout).

### Safety Considerations

- **High-voltage RF**: Spark gap transmitters produce 10-50 kV at the antenna. Vacuum tube transmitters produce 200-2000 V at the output. RF burns penetrate deep tissue. Maintain 2+ m clearance from the antenna during transmission. Ground the antenna when not transmitting.
- **Vacuum tube filament temperature**: Tungsten filaments operate at 2000-2500°C (bright white-orange). Tube envelopes reach 100-200°C. Allow tubes to cool before handling. Fire hazard: keep flammable materials away from tube equipment.
- **B+ voltage**: Vacuum tube plate supplies deliver 50-300 V DC at 10-200 mA. This is enough to cause cardiac fibrillation under wet conditions. Bleeder resistors must discharge filter capacitors when power is removed (capacitors store lethal charge for minutes after power-off).
- **Lead shielding**: Some high-power tubes used lead-glass envelopes for X-ray shielding. Broken tubes may release lead-containing glass fragments. Handle with gloves.
- **Mercury vapor tubes**: Some rectifier tubes (mercury vapor type, used in high-voltage power supplies) contain liquid mercury. If the glass breaks, mercury contamination requires professional cleanup. Mercury vapor is toxic at concentrations above 0.05 mg/m³.
- **Antenna tower climbing**: Masts and towers for long-wave antennas are 20-200 m tall. Climbing for maintenance requires safety harnesses, fall arrestors, and two-person teams. Wind speed limit: 50 km/h for safe climbing.

### See Also

- [Electrical Telegraph Networks](electric-telegraph.md) — Morse code and wire-based telegraph systems
- [Telephone Systems](telephone.md) — Wire-based voice communication
- [Electricity](../energy/electricity.md) — Electrical generation and distribution
- [Glass](../glass/index.md) — Glass for vacuum tube envelopes

*Part of the [Bootciv Tech Tree](../index.md) • [Telecommunications](./index.md) • [All Domains](../index.md)*
