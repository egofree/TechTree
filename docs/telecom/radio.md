# Radio Communication

> **Node ID**: telecom.radio
> **Domain**: [Telecommunications](./index.md)
> **Dependencies**: [`energy.electricity`](../energy/electricity.md), `glass`, `metals`,
> [`telecom.electric-telegraph`](./electric-telegraph.md)
> **Enables**: None
> **Timeline**: Years 30-60
> **Outputs**: radio_communication, wireless_telegraphy, broadcast_capability
> **Critical**: No — communication accelerates coordination but is not strictly required for survival

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

## Vacuum Tube Construction Procedure

The vacuum tube is the enabling component of radio amplification and oscillation. Construction requires precision glassblowing, vacuum technology, and metallurgical skill. Early tubes (1904-1920) were handmade individually; mass production methods (exhaust machines, glass lathes) came later.

### Filament (Cathode)

The heated filament emits electrons via thermionic emission. Filament temperature, wire diameter, and material determine emission current and operating life.

**Receiving tube filament**:
- **Material**: Pure tungsten wire for early tubes; thoriated tungsten (1.0-2.0% thorium oxide by weight) from ~1920 onward provides higher emission at lower temperature and longer life.
- **Diameter**: 0.02-0.05 mm (roughly 44-34 AWG). A typical 01A-type filament is 0.03 mm diameter, 30-40 mm active length.
- **Form**: Hairpin (inverted V) or straight wire suspended between two support posts. Tension maintained by a spring hook on one support to compensate for thermal expansion.
- **Operating temperature**: Pure tungsten 2200-2500°C (bright yellow-white); thoriated tungsten 1700-1900°C (orange). Lower temperature reduces evaporation and extends life.
- **Emission**: Pure tungsten ~5-15 mA/cm²; thoriated tungsten ~50-200 mA/cm² at operating temperature. A receiving tube filament emitting 5-15 mA total.
- **Heater power**: 1.25 W typical (5.0 V × 0.25 A for type 01A). Transmitter tubes: 38-100 W filament power.

**Transmitter tube filament**:
- **Diameter**: 0.10-0.30 mm (roughly 38-28 AWG), or thicker ribbon for high-power tubes.
- **Material**: Thoriated tungsten or tantalum for tubes up to ~1 kW. Above 1 kW, directly heated cathodes use pure tungsten mesh or coated nickel sleeves on refractory cores.
- **Support**: Rigid molybdenum support posts (0.5-1.5 mm diameter), welded or clamped to the filament wire.

### Plate (Anode) Forming

The plate collects electrons emitted by the filament. Shape, material, and surface finish affect dissipation capacity and secondary emission.

**Receiving tube plate**:
- **Material**: Nickel sheet, 0.10-0.25 mm thick, 99.0%+ purity.
- **Form**: Rectangular or cylindrical sleeve surrounding the grid and filament. Typical dimensions: 10-25 mm tall, 8-15 mm wide (rectangular) or 8-12 mm diameter (cylindrical).
- **Surface finish**: Blackened by carbonization or sandblasted to increase radiative cooling. Carbon coating applied by heating the nickel in a hydrocarbon atmosphere (benzene vapor or acetylene at 600-800°C for 5-15 minutes).
- **Dissipation**: 1-5 W for receiving tubes. Adequate for class-A amplifier operation.

**Transmitter tube plate**:
- **Material**: Tantalum (0.3-1.0 mm thick) or molybdenum for 50-250 W tubes. Graphite anodes for tubes above 500 W (better thermal mass and radiation).
- **Form**: Cylindrical or finned designs to maximize radiative surface area. A 250 W tube plate may be 30-50 mm diameter, 50-80 mm tall, with 4-8 cooling fins.
- **Dissipation**: 50-300 W typical. Tantalum plates glow cherry-red at full dissipation. External forced-air cooling required above 100 W dissipation.

### Grid Construction

The grid controls electron flow between filament and plate. Precise, uniform spacing is critical for consistent amplification.

- **Material**: Nickel or molybdenum wire, 0.05-0.15 mm diameter (45-34 AWG).
- **Winding**: Helical winding on two parallel support rods (nickel or molybdenum, 0.3-0.8 mm diameter). Winding pitch: 0.5-2.0 mm between turns (12-50 turns per cm). The grid helix is typically 8-20 mm long and 3-8 mm in diameter.
- **Tension**: Wire wound under 5-20 g tension to maintain uniform spacing. Uneven spacing causes microphonic noise and gain variation.
- **Insulation**: Grid support rods welded to the glass stem at separate feedthrough pins, electrically isolated from filament and plate connections.

### Glass Envelope and Sealing

The glass envelope maintains vacuum and provides structural support for the internal elements.

**Glass composition**: Lead glass (20-30% PbO) preferred for its high resistivity, low dielectric loss at RF frequencies, and good thermal expansion match to dumet seals. Soda-lime glass acceptable for low-cost tubes but has higher leakage current.

**Bulb dimensions**:
- Receiving tubes: 25-45 mm maximum bulb diameter, 60-90 mm overall height. Wall thickness 0.5-1.0 mm.
- Transmitter tubes (250 W): 50-75 mm diameter, 120-180 mm height. Wall thickness 1.0-2.0 mm.

**Glass-to-metal seal (dumet)**:
- **Dumet wire**: 42% nickel / 58% iron core with copper cladding (25% of wire diameter). The composite thermal expansion coefficient (~6.5 × 10⁻⁶/°C) matches lead glass (~9 × 10⁻⁶/°C) closely enough to prevent seal cracking during thermal cycling. Typical dumet pin diameter: 0.8-1.5 mm.
- **Sealing procedure**: Heat the glass stem (flattened glass pinch with embedded dumet pins) and the dumet pins simultaneously to 700-800°C (glass softening point). Press the softened glass around the dumet pins to form a vacuum-tight seal. The copper cladding oxidizes slightly during sealing, bonding chemically with the glass. Borax flux may be applied to the dumet before sealing to improve wetting.

**Stem assembly**: Internal element supports (filament posts, grid rods, plate tab) are welded to the dumet pins before sealing. The stem is then sealed to the glass bulb by heating the bulb neck and stem shoulder to 700-800°C and fusing them together on a glass lathe (rotating to ensure uniform seal). Typical seal length: 8-15 mm of glass-to-glass fusion.

### Evacuation

The tube must be evacuated to a pressure where residual gas molecules do not interfere with electron flow (ionization causes reverse current, gas noise, and eventual cathode poisoning).

**Roughing stage**:
- Mechanical rotary pump (oil-sealed vane or piston type) reduces pressure from atmospheric to ~1 Torr (1 mm Hg). Time: 2-10 minutes per tube.
- Monitor with a thermocouple gauge or Pirani gauge.

**High-vacuum stage**:
- Mercury diffusion pump or oil diffusion pump reduces pressure from ~1 Torr to 10⁻⁵ to 10⁻⁷ Torr. A single-stage mercury pump achieves ~10⁻⁵ Torr; a two-stage system reaches 10⁻⁷ Torr.
- Pumping time: 5-30 minutes per tube, depending on internal surface area and outgassing rate. During pumping, bake the tube envelope with an external flame or oven at 300-400°C to drive off adsorbed moisture and gas from the glass and internal metal surfaces.
- Monitor with an ionization gauge. Target: <10⁻⁵ Torr for receiving tubes, <10⁻⁶ Torr for transmitter tubes.

**Tipping off**: Once the target vacuum is reached, heat the glass exhaust tube (the "tubulation" connecting the tube to the pump) with an oxygen-gas flame and melt it closed ("tip-off"). The tip is pulled off cleanly, leaving a sealed glass nub. This must be done while the pump is running to prevent backflow.

### Getter Activation

The getter absorbs residual and slowly evolving gases during tube life, maintaining the vacuum over thousands of operating hours.

**Getter material**:
- **Barium**: Most common for receiving tubes. Barium-aluminum alloy (50-70% Ba) or barium-magnesium, in the form of a small pellet, ribbon, or coated ring. Typical mass: 10-50 mg of active barium.
- **Magnesium**: Used in some early tubes and high-power tubes. Less effective than barium but easier to handle in air (barium is pyrophoric when pure).
- **Phosphorus (red)**: Used as an auxiliary getter in some transmitting tubes.

**Placement**: Getter attached to a support wire inside the tube, positioned away from the active electrode region (typically near the top of the bulb, above the plate). The support wire may be a separate external lead or may be heated by induction.

**Activation procedure**:
1. After tip-off, heat the getter by RF induction (a coil around the outside of the bulb, 200-500 kHz, inducing eddy currents in the getter metal) or by direct flame heating of the getter support wire. Barium flash temperature: 800-1000°C.
2. The getter metal vaporizes and condenses on the coolest part of the inner glass surface (typically the dome), depositing as a bright silver mirror (barium) or dull gray coating (magnesium).
3. The freshly deposited getter film is highly reactive and chemically binds residual gases (O₂, N₂, H₂O, CO₂, CO) through absorption and chemical reaction. Barium absorbs up to 30-50x its own volume of gas.
4. Verification: a properly flashed tube shows a uniform, bright mirror deposit. A mottled or dark deposit indicates excessive residual gas or incomplete flash.

**Effect**: A properly gettered tube maintains <10⁻⁶ Torr internal pressure throughout its operating life (1,000-10,000 hours). Without a getter, tube vacuum degrades within 100-500 hours due to gas evolution from internal surfaces under electron bombardment.

## Antenna Mast Construction

Antenna height is the single most important factor in long-wave and medium-wave radio performance. A 50 m vertical radiator at 300 kHz has ~5-15% radiation efficiency; raising it to 100 m improves efficiency to 15-35%. Mast construction must balance structural strength against material and labor cost.

### Structural Design

**Mast types**:
- **Self-supporting lattice tower**: Triangular or square cross-section, tapering from base to top. Suitable for heights up to 50 m. Requires no guy wires but needs a massive foundation. Material: angle iron or flat-bar steel, bolted or riveted joints.
- **Guyed mast**: Slender lattice or tubular steel column supported by guy wires at one or more levels. Economical for heights above 30 m. Guyed masts up to 200 m are practical with 1920s-era steel and rigging.

**Design loads**:
- **Wind pressure**: Design for 100-150 km/h survival (0.6-1.3 kPa on projected area). Antenna wire adds wind load: a 4 mm wire presents ~4 mm × length projected area.
- **Ice loading**: 25 mm radial ice adds 25-50% to wind load on lattice members. Ice zones require 1.5× structural safety factor.
- **Antenna wire tension**: Vertical wire at 100-300 N tension. Wind-induced sway adds lateral loads to the mast top.

### Guy Wire Sizing

Guy wires stabilize the mast against wind-induced bending and buckling. Three guy directions at 120° spacing is the minimum; four at 90° is common.

**Guy wire specifications**:

| Mast Height | Guy Levels | Guy Wire Diameter | Breaking Strength | Anchor Distance |
|-------------|------------|-------------------|-------------------|-----------------|
| 20-30 m | 1 level (at top) | 4-6 mm steel wire rope | 10-20 kN | 12-20 m from base |
| 30-50 m | 1-2 levels | 6-8 mm steel wire rope | 20-35 kN | 20-35 m from base |
| 50-80 m | 2 levels (1/3, 2/3 height) | 8-10 mm steel wire rope | 35-55 kN | 30-55 m from base |
| 80-120 m | 2-3 levels | 10-14 mm steel wire rope | 55-100 kN | 50-80 m from base |
| 120-200 m | 3-4 levels | 12-18 mm steel wire rope | 80-160 kN | 70-130 m from base |

- **Material**: Galvanized steel wire rope (6 × 7 or 6 × 19 construction). Galvanizing provides 10-25 year corrosion life in non-marine atmospheres.
- **Pre-tension**: Guy wires pre-tensioned to 10-15% of breaking strength. Check tension with a dynamometer or by measuring natural frequency (pluck test). Re-tension annually (thermal cycling and creep cause loosening).
- **Insulators**: Ceramic or porcelain guy-strain insulators inserted in each guy wire at 10-20 m intervals to prevent the guy from coupling RF energy to ground. Insulator rating: 5-15 kV RF per unit. Without insulators, guy wires detune the antenna and waste transmitter power.
- **Turnbuckles**: Forged steel turnbuckles at each anchor allow tension adjustment. Safety wire through the turnbuckle body prevents accidental loosening.

### Foundation Requirements

Foundations transfer mast compression and guy tension into the ground. Foundation design depends on soil bearing capacity.

**Mast base foundation**:
- **Self-supporting tower**: Reinforced concrete pad, 1.5-3.0 m square, 0.5-1.0 m deep, on compacted soil (bearing capacity >150 kPa). Each tower leg on a separate pad or a combined pad with pier pedestals.
- **Guyed mast**: Smaller base — concrete cylinder or pier, 0.6-1.0 m diameter, 1.0-1.5 m deep. Mast base carries primarily compressive load (guy wires resist overturning).
- **Grounding**: Bond the mast base to the station ground system (buried copper radials) with 2-4 mm copper wire. Ground resistance <5 ohm.

**Guy anchor foundations**:

| Guy Tension | Anchor Type | Concrete Volume | Depth | Soil Type |
|-------------|-------------|-----------------|-------|-----------|
| <20 kN | Deadman (log or steel beam) | 0.3-0.5 m³ | 1.0-1.5 m | Any (compact backfill) |
| 20-50 kN | Concrete block | 0.5-1.0 m³ | 1.0-2.0 m | Clay, loam |
| 50-100 kN | Concrete mass or screw anchor | 1.0-2.0 m³ | 1.5-2.5 m | Firm soil |
| >100 kN | Reinforced concrete deadman | 2.0-4.0 m³ | 2.0-3.0 m | Rock or firm soil |

- **Deadman anchor**: Horizontal timber beam or steel section buried at the specified depth. Guy wire attaches to a steel rod passing through the deadman to the surface. For temporary installations, a buried log (200-300 mm diameter, 1.0-1.5 m long) suffices for guy tensions up to 15 kN.
- **Concrete anchor**: Cast-in-place concrete block with embedded steel eye bolt or U-bolt. Minimum 7-day cure before applying guy tension; 28-day for full rated load.
- **Backfill**: Compact soil in 200 mm lifts around the anchor. Poorly compacted backfill reduces holding capacity by 30-50%.

### Erection Procedure (Guyed Mast, 50 m)

1. **Prepare foundations**: Cast base pier and guy anchor foundations. Allow concrete to cure 7+ days. Install anchor rods and base leveling nuts.
2. **Pre-assemble mast sections on ground**: Bolt lattice sections together horizontally on sawhorses or timber blocks. Install antenna mounting hardware, climbing steps, and aviation warning markers (if required) while the mast is accessible.
3. **Rig guy wires**: Attach guy wires to mast at designated levels with thimbles and wire rope clips (minimum 3 clips per termination, spaced at 6× wire diameter). Thread guy wires through turnbuckles at anchors.
4. **Raise the mast**: Use a gin pole (temporary lifting boom) or a crane. For a 50 m guyed mast, raise the base end first while the top end slides along the ground on a timber skid. A winch or tractor provides pulling force.
5. **Set the base**: Lower the mast base onto the foundation pier. Level with adjusting nuts. Shim if necessary.
6. **Tension guy wires**: At each level, pull guy wires hand-tight, then use a come-along or turnbuckle to reach design pre-tension. Work symmetrically — tension one wire of each trio, then the next, to avoid bending the mast.
7. **Plumb the mast**: Check verticality with a transit or theodolite from two positions 90° apart. Adjust guy wire tension to plumb the mast within 0.5° of vertical (±0.4 m deviation at 50 m height).
8. **Install antenna wire**: Hoist the vertical antenna wire (copper or copperweld, 2-4 mm diameter) using a halyard through a pulley at the mast top. Connect the base of the antenna wire to the tuning coil and transmitter coupling. Connect the mast itself to the ground system.
9. **Final check**: Verify all bolt torques, wire rope clip tightness, guy wire tension, and ground connections. Test the antenna with a low-power signal and measure SWR (standing wave ratio) or antenna current.

## Inductor Winding Specifications

Inductors (coils) are essential in every radio circuit — tuned circuits, loading coils, RF chokes, and transformer windings. Inductance value, Q factor (quality factor), and current-carrying capacity depend on geometry, wire gauge, and core material.

### Single-Layer Air-Core Solenoid

The most common inductor for radio tuning circuits. Predictable inductance, low loss, no core saturation.

**Inductance formula** (Wheeler's formula, single-layer solenoid):

L (uH) = (r² × n²) / (9 × r + 10 × l)

where r = coil radius in inches, l = winding length in inches, n = total turns. Accuracy: ±1% for coils where l > 0.4 × r.

**Specification table for common tuning inductors**:

| Inductance (uH) | Form Dia. (mm) | Wire Dia. (mm) | Turns | Winding Length (mm) | AWG | Application |
|-----------------|----------------|-----------------|-------|---------------------|-----|-------------|
| 10 | 50 | 1.5 | 18 | 30 | 15 | VHF tank circuit |
| 25 | 50 | 1.2 | 28 | 38 | 17 | HF receiving tank |
| 50 | 65 | 1.0 | 32 | 42 | 18 | HF transmitting tank |
| 100 | 75 | 0.8 | 48 | 55 | 20 | MF receiving tank |
| 200 | 75 | 0.6 | 65 | 70 | 22 | LF loading coil |
| 500 | 100 | 0.5 | 85 | 100 | 24 | Antenna loading (LF) |

**Q factor**: Single-layer air-core solenoids on dry forms achieve Q = 100-250 at 1 MHz. Q is highest when coil diameter ≈ winding length (the "square" coil optimum). Q degrades at higher frequencies due to skin effect and proximity effect.

**Skin effect**: At 1 MHz, RF current penetrates copper only ~0.066 mm. Wire thicker than ~0.2 mm carries most current on the surface. For high-Q coils above 500 kHz, use Litz wire (multiple insulated strands, each thinner than the skin depth, woven together) or copper tubing (large surface area, low RF resistance).

**Wire gauge selection**:
- **Receiving circuits** (current <50 mA): 24-30 AWG (0.5-0.25 mm) sufficient. Q limited by form losses more than wire resistance at MF.
- **Transmitter tank circuits** (current 0.5-5 A): 14-18 AWG (1.6-1.0 mm) for 100-500 W transmitters. 10-14 AWG (2.6-1.6 mm) for 1-5 kW.
- **Antenna loading coils** (current 1-20 A): 10-14 AWG (2.6-1.6 mm) minimum. Heavy loading coils (200-400 uH at 5-20 A) may require 8-12 AWG (3.3-2.0 mm) or copper strip/tubing.

### Form Materials

The coil form (bobbin) provides mechanical support. Form material affects Q through dielectric losses at RF frequencies.

| Material | Loss at 1 MHz | Moisture Sensitivity | Max Temp | Suitability |
|----------|---------------|---------------------|----------|-------------|
| Ceramic (porcelain, steatite) | Very low | None | >1000°C | Best — low loss, stable, dimensionally precise |
| Phenolic (Bakelite) | Low | Low | 120°C | Good — machinable, cheap, widely available |
| Dry hardwood (oak, maple) | Moderate | High (varies with humidity) | 100°C | Acceptable if dried and wax-impregnated |
| PVC | Moderate-high | None | 70°C | Poor — high dielectric loss above 500 kHz |
| Cardboard/paper | High | Very high | 80°C | Unacceptable — lossy and dimensionally unstable |

- **Wood form preparation**: Turn hardwood on a lathe to the required diameter. Dry at 100°C for 24 hours. Soak in molten beeswax or paraffin at 80-100°C for 2-4 hours to seal moisture and reduce dielectric loss. Wax-impregnated wood forms achieve Q within 10-20% of phenolic.
- **Ceramic forms**: Turn on a potter's wheel or press in a mold, then fire at 1000-1200°C. Glaze the outer surface for dimensional stability. Ceramic forms provide the most stable inductance over temperature and humidity.

### Winding Procedure (Single-Layer Solenoid)

1. **Prepare the form**: Cut the cylindrical form to length (winding length + 10-15 mm margin at each end). Drill two 1-2 mm holes at each end of the winding region for wire anchor points.
2. **Anchor the start**: Thread the wire through the start hole, leaving a 50-100 mm lead. Bend the wire flat against the form surface.
3. **Wind the coil**: Rotate the form slowly (by hand or on a lathe at low speed). Lay each turn tight against the previous turn, maintaining even tension (5-20 N for 0.5-1.5 mm wire). Count turns. Wind 2-3 extra turns beyond the calculated number for fine-tuning.
4. **Anchor the finish**: Thread the wire through the end hole. For variable inductors, leave 4-8 intermediate tap points (bare a 3-5 mm section of wire and solder a tinned copper lead to it).
5. **Secure the winding**: Apply a thin coat of shellac, varnish, or wax over the completed winding to lock turns in place. Allow to dry/cure fully before use.
6. **Measure and adjust**: Measure inductance with a grid-dip oscillator or by resonating the coil with a known capacitor (L = 1 / ((2πf)² × C)). Remove turns 1-2 at a time if inductance is high; add turns if low.

### Loading Coil for Electrically Short Antennas

A loading coil at the base of a short vertical antenna resonates the antenna-plus-coil system at the desired frequency, compensating for the antenna's capacitive reactance.

**Design example — 50 m antenna at 300 kHz**:
- Antenna capacitance: ~200-300 pF. Capacitive reactance at 300 kHz: ~1800-2700 ohm.
- Required inductance: ~200-400 uH to resonate at 300 kHz (f = 1/(2π√(LC))).
- Coil current at 1 kW transmitter power: ~1.5-3.0 A RMS.
- Required Q: >100 for reasonable efficiency. Coil resistance must be <5-15 ohm.
- Specification: 200-300 uH, wound on 100-150 mm diameter phenolic or ceramic form, 2.0-3.0 mm wire (12-10 AWG), 80-120 turns, single layer. Power dissipation in the coil: 5-30 W (depending on Q). The coil will warm noticeably during extended transmission — ventilate the coil housing.

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

---
*Part of the [Bootciv Tech Tree](../index.md) • [Telecommunications](./index.md) • [All Domains](../index.md)*
