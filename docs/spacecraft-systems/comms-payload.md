# Communications Payload

> **Node ID**: spacecraft-systems.comms-payload
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`telecom.radio`](../telecom/radio.md),
> `electronics`, `vacuum.deposition-systems`, `metals`
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: comms_payloads, satellite_antennas, twtas
> **Critical**: No — communications payloads are the revenue-generating heart of every commercial satellite. Without high-power transponders, shaped-beam antennas, and efficient TWTAs, a commsat is inert mass. Yet the entire payload builds on terrestrial radio-frequency heritage and adds only the space-rated amplifier, aperture, and filter engineering that turns a 20-watt radio into a 20-kilowatt bent-pipe relay serving a continent

The communications payload is what separates a communications satellite from any other spacecraft. It comprises the [transponders](./comms-payload.transponders.md) (frequency conversion and channel routing), the [antennas](./comms-payload.antennas.md) (reflectors, horns, and phased arrays that shape the coverage footprint), the [traveling-wave tube amplifiers](./comms-payload.traveling-wave-tubes.md) (TWTAs that boost the signal to hundreds of watts), and the [RF multiplexers](./comms-payload.multiplexers.md) (input and output multiplexers that filter and combine dozens of channels). Together these four subsystems define the satellite's capacity — measured in gigabits per second for digital payloads or in transponder equivalents (36-MHz channels) for analog broadcast.

This article covers the integrated payload engineering: frequency-band selection, link-budget physics, EIRP sizing, amplifier technology trade-offs (TWTA vs SSPA), antenna architectures (single feed, shaped reflector, phased array), and the multiplexer filtering that prevents adjacent-channel interference. The [telecom radio](../telecom/radio.md) heritage provides the RF circuit foundation, the broader [electronics](../electronics/index.md) domain supplies the mixed-signal and GaN/GaAs solid-state amplifiers, [vacuum deposition systems](../vacuum/deposition-systems.md) enable the thin-film coatings and cathode fabrication critical to TWTA production, and [metals](../metals/index.md) provide the waveguide and reflector structures.

## Overview

A commsat payload is a **bent-pipe relay**: it receives an uplink signal from a ground station, amplifies it, translates it to the downlink frequency, and re-radiates it toward the service area. The figure of merit is the **Effective Isotropic Radiated Power (EIRP)** — the product of transmit power and antenna gain, expressed in dBW. A high-EIRP satellite lets customer terminals use small, cheap antennas. A Ku-band DBS satellite broadcasting 52 dBW EIRP enables 45-cm dishes; a Ka-band HTS pushing 60+ dBW enables 30-cm ultrasmall-aperture terminals (USATs). The engineering challenge is delivering that EIRP reliably for 15 years in the thermal, radiation, and vacuum environment of geostationary orbit.

Modern high-throughput satellites (HTS) like ViaSat-3 and Jupiter-3 deliver over 500 Gbps by combining dozens of spot beams with full frequency reuse — each spot reuses the same Ku or Ka spectrum via spatial isolation, multiplying total capacity. LEO constellations like Starlink use phased-array antennas to form hundreds of steerable user beams from a single flat-panel aperture, tracking ground terminals as the satellite moves at 7 km/s.

## Frequency Bands

The ITU allocates spectrum for satellite communications across six primary bands. Higher frequencies offer more bandwidth (more capacity) but suffer greater rain attenuation and require tighter pointing.

| Band | Uplink (GHz) | Downlink (GHz) | Bandwidth | Rain Fade | Typical Use |
|------|-------------|-----------------|-----------|-----------|-------------|
| L | 1.6 | 1.5 | 30 MHz | <0.2 dB | Mobile, GPS, Inmarsat |
| S | 2.6-2.7 | 2.5-2.6 | 70 MHz | <0.5 dB | Mobile, military, NASA TT&C |
| C | 5.9-6.4 | 3.7-4.2 | 500 MHz | <1 dB | Regional TV, legacy telephony |
| Ku | 14.0-14.5 | 10.7-12.75 | 2.0 GHz | 3-8 dB | DTH broadcast, VSAT, HTS |
| Ka | 27.5-31.0 | 17.7-21.2 | 3.5 GHz | 8-25 dB | HTS broadband, ViaSat, Starlink |
| V | 47-51 | 37-42 | 5 GHz | 20-40 dB | Future backhaul, experimental |

C-band (4 GHz) was the original commsat band (Intelsat I, 1965) and remains valuable for tropical regions where rain fade makes Ku/Ka impractical. Ku-band dominates direct-to-home (DTH) television (DirecTV, Dish, SES Astra). Ka-band is the current frontier for high-throughput broadband, offering 3.5 GHz of usable bandwidth — seven times Ku — at the cost of severe rain fading that requires uplink power control and adaptive coding (ACM).

V-band (40 GHz) is experimental territory, targeted for terabit-per-second satellite backhaul and inter-satellite links. Q-band (20-40 GHz) overlaps Ka downlink. These millimetre-wave bands demand precision pointing (0.02°) and advanced propagation countermeasures.

## EIRP and Link Budget

The EIRP is the satellite's most-quoted specification. It combines transmit power and antenna gain into a single number that determines ground-terminal size.

```
EIRP (dBW) = Pt (dBW) + Gt (dBi) - L_feed (dB)
```

For a typical Ku-band transponder delivering 120 W (20.8 dBW) through a 0.8-m spot-beam antenna (38 dBi gain) with 1.5 dB feed loss, the EIRP is 57.3 dBW. The received flux density on the ground follows the inverse-square law:

```
Φ (dBW/m²) = EIRP - 10·log₁₀(4πR²)
```

At GEO distance (35,786 km), the spreading loss at 12 GHz is roughly 162.5 dB. A 57.3 dBW EIRP beam delivers -105 dBW/m² to the edge of coverage. A 45-cm dish (0.16 m² effective area, 33 dBi gain) captures -116 dBW — enough for DVB-S2 demodulation at 30 Msps with QPSK and 3/4 coding (Es/N0 threshold ~6 dB).

| Coverage | Beamwidth | Antenna | Gain | EIRP (120W TWTA) | Terminal Size |
|----------|-----------|---------|------|------------------|---------------|
| Global beam | 17° | Horn | 20 dBi | 40 dBW | 3.0 m dish |
| Hemispherical | 8° | Reflector | 28 dBi | 48 dBW | 1.2 m dish |
| Zone beam | 4° | Shaped reflector | 34 dBi | 54 dBW | 0.6 m dish |
| Spot beam | 1.5° | Offset reflector | 39 dBi | 59 dBW | 0.4 m dish |
| Spot beam (HTS) | 0.8° | Multibeam | 45 dBi | 65 dBW | 0.3 m dish |
| Spot beam (VHTS) | 0.5° | Phased array | 49 dBi | 69 dBW | 0.25 m dish |

The trend is unmistakable: more, narrower beams. A traditional C-band satellite had one global beam; an HTS like ViaSat-3 has over 100 spot beams, each reusing the same 500 MHz of Ka-band spectrum. This **frequency reuse** multiplies capacity 20-fold without increasing total spectrum.

## Transponder Architecture

The transponder converts the uplink signal to the downlink frequency and amplifies it. See [Communications Transponders](./comms-payload.transponders.md) for full detail.

### Bent-Pipe (Transparent)

The bent-pipe transponder coherently translates the uplink to the downlink without demodulation. A 6/4 GHz C-band transponder mixes the 5.9-6.4 GHz uplink down to 3.7-4.2 GHz using a 2225 MHz local oscillator. Each channel is filtered to 36 MHz (or 72 MHz for wideband), amplified by a TWTA or SSPA, and combined in the output multiplexer before reaching the antenna. The architecture is simple, robust, and technology-agnostic — the satellite does not care whether the signal is analog TV, DVB-S, or TDMA voice.

### Regenerative (Onboard Processing)

The regenerative transponder fully demodulates the uplink, decodes the data, switches it onboard, and re-encodes it for the downlink. This breaks uplink and downlink noise coupling, enabling independent link optimisation, smaller margins, and mesh connectivity without a hub double-hop. The IRIS (Internet Routing in Space) payload and Inmarsat-4's digital channeliser are early examples. The cost is mass, power, and the inability to upgrade modulation after launch — a bent-pipe satellite can adopt new waveforms through ground upgrades; a regenerative one is locked to its launch-era codec.

### Digital Channeliser

The digital channeliser splits the uplink into narrow subchannels (e.g., 1.25 MHz), routes each independently between beams, and recombines for the downlink. This enables flexible bandwidth allocation — a beam serving a temporary event can borrow capacity from a quiet beam. Intelsat EpicNG and Inmarsat-6 carry digital channelisers with thousands of routable subchannels.

## Traveling-Wave Tube Amplifiers

The TWTA is the workhorse amplifier for high-power satellite downlinks above 10 GHz. See [Traveling-Wave Tube Amplifiers](./comms-payload.traveling-wave-tubes.md) for full detail. A TWTA converts the DC input from the spacecraft bus into RF output by bunching electrons in a slow-wave structure and transferring their kinetic energy to the RF wave. Modern space TWTAs achieve 60-70% overall efficiency — roughly double that of comparable solid-state amplifiers at Ku/Ka-band power levels.

| Parameter | Ku-band TWTA | Ka-band TWTA | V-band TWTA |
|-----------|-------------|-------------|-------------|
| RF output | 100-250 W | 50-150 W | 20-50 W |
| DC input | 150-380 W | 80-230 W | 35-80 W |
| Efficiency | 65-70% | 60-66% | 55-60% |
| Mass | 0.9-1.4 kg | 0.7-1.0 kg | 0.5-0.8 kg |
| Lifetime | 15-18 years | 15 years | 12-15 years |
| Saturated gain | 50-60 dB | 45-55 dB | 40-50 dB |
| Phase shift (sat) | 40-55° | 35-50° | 30-45° |

### SSPA vs TWTA Trade-Off

Solid-state power amplifiers (SSPAs) using GaAs and increasingly GaN devices dominate at C-band and low-power S-band applications. Above 50 W at Ku-band, TWTAs retain a clear efficiency advantage: a 150 W Ku TWTA at 68% efficiency draws 220 W DC, while a GaN SSPA of the same output draws 280-300 W (50-55% efficiency). That 60-80 W difference, multiplied across dozens of transponders, directly determines solar array and battery sizing. SSPAs win on linearity (less backoff needed), graceful degradation (transistor failures reduce power rather than total failure), and lower phase noise. The trend in VHTS payloads is **hybrid architectures**: SSPAs for low-power spot beams, TWTAs for high-power broadcast beams.

| Metric | TWTA | GaN SSPA | GaAs SSPA |
|--------|------|----------|-----------|
| Efficiency (Ku 120W) | 68% | 55% | 38% |
| Efficiency (Ka 50W) | 62% | 52% | 32% |
| Linearity (IMD3) | Moderate | Good | Good |
| Phase noise | Higher | Lower | Lowest |
| Failure mode | Hard fail | Graceful | Graceful |
| Mass (120W unit) | 1.1 kg | 1.5 kg | 2.2 kg |
| Qualification (years) | 18 | 12 | 15 |
| Cost (relative) | 1.0× | 0.8× | 0.6× |

### Linearisation and Backoff

TWTAs are inherently nonlinear near saturation. To limit intermodulation distortion (IMD), they are operated at output backoff (OBO) — typically 2-3 dB for single-carrier, 3-4 dB for multicarrier operation. A lineariser (a predistortion circuit ahead of the TWTA) recovers 1-1.5 dB of that backoff, effectively increasing useful output by 25-40%. All modern space TWTAs ship with an integrated lineariser, reducing OBO to 1-2 dB while keeping spurious emissions within ITU limits.

## Satellite Antennas

The antenna system shapes the satellite's coverage footprint and polarisation. See [Satellite Antennas](./comms-payload.antennas.md) for full detail. Four architectures dominate modern commsats.

### Reflector Antennas

Most GEO commsats use single or dual offset-fed parabolic reflectors, 1-3 m in diameter, illuminated by a feed array. A **shaped reflector** uses a computer-designed surface contour to cast the beam onto a specific landmass — Europe, CONUS, India — rather than a circle. Intelsat 39 carries a 2.4 m shaped reflector producing a Europe-to-Africa beam with 50 dBW edge EIRP.

### Phased Arrays

A phased array steers beams electronically by varying the phase of each radiating element. No moving parts, rapid reconfigurability, and the ability to form multiple simultaneous beams make phased arrays the architecture of choice for LEO constellations. Starlink satellites carry three flat-panel phased arrays (two user beams, one gateway) each with roughly 1,200-1,500 radiating elements operating at 12 and 14 GHz. Element counts scale with beam-pointing precision: a 0.5° spot beam at Ku-band requires ~1,000 elements over a 0.7 m² aperture.

| Architecture | Elements | Beamwidth | Beams | Scan Range | Mass |
|-------------|----------|-----------|-------|------------|------|
| Iridium NEXT L-band | ~120 | 5° | 48 | ±60° | 12 kg |
| Starlink Ku user array | ~1,200 | 1.2° | 2-4 | ±55° | 9 kg |
| AEHF EHF phased array | ~500 | 1.5° | 8 | ±45° | 15 kg |
| ViaSat-3 Ka reflector | N/A (feed) | 0.5° | 100+ | Fixed | 8 kg |
| Future O3b mPOWER | ~2,000 | 0.4° | 30+ | ±60° | 18 kg |

### Horn and Helix Antennas

Horn antennas (corrugated potter horns) feed reflectors and provide global-beam coverage at C and L band. Helix antennas provide circular polarisation for mobile satellite services (Inmarsat L-band, GPS navigation). Quadrifilar helices on GPS Block III radiate an L1/L2/L5 combined beam covering the entire visible Earth.

### Deployable Mesh Reflectors

Large deployable mesh reflectors (5-30 m) enable high-gain beams at low frequencies. The Inmarsat-4 satellites carry 9 m unfurlable meshes for L-band mobile services. The upcoming Jupiter-3 carries a 9 m Ka-band mesh providing 14 spot beams to the Americas.

## RF Multiplexers

The input multiplexer (IMUX) and output multiplexer (OMUX) filter and combine the transponder channels. See [RF Multiplexers](./comms-payload.multiplexers.md) for full detail. The IMUX sits after the receiver and splits the uplink into individual channels; the OMUX sits after the TWTAs and combines the amplified channels into a single waveguide to the antenna.

Each multiplexer channel is a waveguide cavity filter with steep skirts (selectivity) and low insertion loss. A Ku-band OMUX channel filter at 12 GHz with 36 MHz bandwidth must reject the adjacent channel (36 MHz away) by 25 dB while losing less than 0.6 dB in-band. This requires 6-8 coupled cavities with carefully shaped coupling irises — typically machined from aluminium (silver-plated) or invar for thermal stability.

| Parameter | IMUX | OMUX |
|-----------|------|------|
| Location | After receiver | After TWTAs |
| Function | Split uplink | Combine downlink |
| Channel count | 24-60 | 24-60 |
| Channel bandwidth | 26-72 MHz | 26-72 MHz |
| Insertion loss | 1-2 dB | 0.3-0.6 dB |
| Adjacent rejection | 20-30 dB | 25-35 dB |
| Power handling | Low (<1 W) | High (50-300 W) |
| Technology | Cavity (TE₁₁₃) | Cavity (TE₁₁₃) |
| Mass (per channel) | 0.08 kg | 0.15 kg |
| Temperature range | -5 to +45°C | 0 to +95°C |

OMUX design is constrained by **multipactor** — a resonant vacuum discharge that occurs when secondary electron emission from RF fields produces an electron avalanche. At 150 W Ku-band and millitorr pressure, a 2 mm gap can multipactor. OMUX cavities are designed with gaps large enough and surfaces passivated (silver-over-aluminium, alumina coating) to push the multipactor threshold above the operating power. All designs undergo multipactor testing at 1.5× rated power in a vacuum chamber.

## Real-World Satellites

| Satellite | Operator | Launch | Band | TWTAs | Beams | Capacity | EIRP (peak) |
|-----------|----------|--------|------|-------|-------|----------|-------------|
| Intelsat 39 | Intelsat | 2018 | C/Ku/Ka | 94× 150W | 7 | 40 Gbps | 56 dBW |
| Starlink v2-mini | SpaceX | 2023+ | Ku/Ka | 4× 80W | 4-8 spot | ~50 Gbps/sat | 58 dBW |
| ViaSat-3 Americas | Viasat | 2023 | Ka | 100+ | 100+ spot | 1000+ Gbps | 65 dBW |
| Jupiter-3 | EchoStar | 2023 | Ku/Ka | 60× 200W | 14 spot + zone | 500 Gbps | 61 dBW |
| O3b mPOWER | SES | 2023+ | Ka | 30+ | 30 steerable | 800 Gbps/sat | 60 dBW |
| Inmarsat-6 F1 | Inmarsat | 2021 | L/Ka | digital | 200+ spot | 60 Gbps | 54 dBW |
| AEHF-6 | USAF | 2020 | EHF/SHF | 40× 120W | 8 phased | classified | classified |

The capacity progression is striking: Intelsat I (1965) carried 240 voice circuits; Intelsat 39 carries the equivalent of 200,000. ViaSat-3 represents the terabit-per-second class, enabled by 100+ spot beams each reusing the full Ka-band with high-gain phased-array and reflector combinations. Starlink's v2-mini satellites, while individually lower-capacity (~50 Gbps), achieve system throughput through 5,500+ satellites in LEO — a fundamentally different architecture trading constellation size for per-satellite simplicity.

## Capacity Sizing — Worked Example

To deliver 100 Gbps from a single GEO satellite using Ka-band with 2 GHz of usable spectrum (27.5-29.5 GHz up, 17.7-19.7 GHz down):

1. **Spectral efficiency**: DVB-S2X with 32APSK 9/10 coding achieves 7.8 b/s/Hz at 15 dB Es/N0
2. **Per-beam capacity**: 250 MHz × 7.8 = 1.95 Gbps per beam (clear sky)
3. **Frequency reuse**: 2 GHz / 250 MHz = 8 reuse factor with 4-colour scheme (2 polarisations × 2 sub-bands)
4. **Number of beams**: 100 Gbps / 1.95 Gbps × (rain margin factor 1.5) = 77 beams required
5. **EIRP per beam**: 49 dBi antenna gain × 150 W TWTA = 70 dBW EIRP (peak), 65 dBW edge
6. **Total DC power**: 77 beams × 150 W / 0.62 efficiency = 18.6 kW RF alone
7. **Antenna aperture**: 0.5° beamwidth at 19 GHz requires ~2.2 m effective aperture → deployable reflector

This 18.6 kW RF load, plus ~5 kW for the spacecraft bus, defines the solar array (~24 kW) and the thermal rejection system — ViaSat-3's bus is one of the largest commercial GEO buses ever built, precisely because of this RF power requirement.

## Manufacturing and Test

Space TWTAs are manufactured in cleanrooms with vacuum brazing for the slow-wave structure, oxide-cathode impregnation (barium aluminate) in [vacuum deposition systems](../vacuum/deposition-systems.md), and 2000-hour life-test burn-in. Each TWTA undergoes vibration (random + sine), thermal vacuum cycling (-20 to +75°C, 10 cycles), and EMI testing before integration. Reflector surfaces are carbon-fibre composite (skin on aluminium honeycomb core) coated with vacuum-deposited aluminium for RF reflectivity, achieving surface RMS of λ/100 (30 µm at Ku-band). OMUX cavities are CNC-machined from 6061-T6 aluminium, silver-plated (5 µm), and tuned on a vector network analyser to within 0.05 dB of the target response.

## TWTA Cathode and Slow-Wave Structure

The heart of a space TWTA is the **oxide cathode** — a porous tungsten matrix impregnated with barium-calcium-aluminate (B-type, 4:1:1 ratio). The cathode emits 0.5-1.5 A/cm² at 1000°C operating temperature, heated by a tungsten filament drawing 3-6 W. Cathode lifetime is the TWTA lifetime-limiting factor: the barium activator depletes over thousands of hours, reducing emission current until the tube can no longer deliver rated saturated power. Modern cathodes rated for 100,000+ hours (12+ years continuous) use M-type (osmium-coated) cathodes that run 80-100°C cooler, extending barium lifetime by 40%.

The **slow-wave structure** (helix for broadband, coupled-cavity for high power) slows the RF wave to match the electron beam velocity (~0.1 c at 10 kV), enabling sustained energy transfer. Helix TWTs cover a full octave bandwidth (e.g., 10-18 GHz) but are limited to ~150 W saturated output. Coupled-cavity TWTs achieve 250-500 W but over narrower bandwidth (5-10%). The helix is wound from tungsten or copper tape, supported by three BeO ceramic rods that provide thermal conduction to the casing — a design that requires the [vacuum deposition systems](../vacuum/deposition-systems.md) to braze the ceramic supports without contaminating the slow-wave circuit.

### Beam Focusing

The electron beam must stay narrow (0.3-0.5 mm) over the 100-200 mm interaction length. A **periodic permanent magnet (PPM)** stack of samarium-cobalt rings focuses the beam, alternating polarity every 5-10 mm to create a Brillouin flow. Beam interception on the helix (0.5-2% of beam current) determines the tube's thermal budget and limits maximum duty cycle. PPM alignment to within ±0.05 mm along the stack is a manufacturing tolerance that drives yield and cost.

## Phased Array Beamforming

A phased array steers a beam by applying a progressive phase shift across its radiating elements. The beam direction for a uniform linear array of N elements spaced d apart is:

```
θ_scan = arcsin(λ / (N·d) × Δφ / (2π))
```

For a Starlink-class Ku array with 1,200 elements over 0.7 m² (effective aperture), element spacing is ~20 mm (0.8λ at 12 GHz). A full 360° phase shift at each element covers ±60° scan range with sidelobes below -15 dB via Taylor amplitude tapering. Beamforming is implemented with low-loss ferrite phase shifters (analog, <1 dB loss, 2-4 µs switching) or digitally at baseband (flexible, but requires an ADC/DAC per element — power-hungry for 1,200 channels).

| Beamforming Type | Loss | Switching | Power/Element | Reconfigurability |
|-----------------|------|-----------|---------------|-------------------|
| Ferrite analog | 0.7-1.0 dB | 3-5 µs | 0 mW (passive) | Low (fixed weights) |
| PIN diode analog | 1.0-1.5 dB | 0.1-1 µs | 5-15 mW | Moderate |
| MMIC digital (4-bit) | 2-3 dB | <50 ns | 50-150 mW | Full (per-element) |
| Hybrid (subarray) | 1.5-2.0 dB | 0.5-2 µs | 20-60 mW | High |

The trade is loss vs flexibility. Analog ferrite arrays are efficient but produce one fixed beam pattern at a time; digital arrays can form multiple simultaneous beams and nulls toward interferers, but dissipate kilowatts of DC power in the beamforming network. LEO constellations favour analog or hybrid because the 7 km/s satellite motion means beam pointing changes faster than the digital reconfiguration latency allows for thousands of user terminals.

## Link Budget — Worked Starlink Example

A Starlink v2-mini satellite at 550 km altitude serves a user terminal with a 0.4 m dish. Downlink at 12 GHz, 250 MHz bandwidth, weather factor 1 dB:

```
Pt (TWTA shared)      = 23 dBW (200W / 4 beams)
Gt (satellite array)  = 35 dBi
Gr (terminal dish)    = 33 dBi
Range (550 km)        = 148.8 dB free-space loss
Atmosphere            = 1.0 dB
Other losses          = 1.5 dB (pointing, polarisation, feed)

C/N0 = EIRP + Gr/L - kTsys
     = (23+35) + (33-1-1.5-148.8) - (-228.6+24.5)
     = 58 - 118.3 + 204.1 = 79.8 dB-Hz

Eb/N0 (at 100 Mbps)   = 79.8 - 10·log₁₀(100e6)
                      = 79.8 - 80.0 = -0.2 dB
```

At -0.2 dB Eb/N0 the link does not close with DVB-S2X (threshold ~2 dB for QPSK 1/2). The satellite must either increase TWTA power, narrow the beam (higher gain), or reduce the data rate. In practice Starlink uses higher-gain beams (~40 dBi), lower user rates (50-150 Mbps typical), and ACM that drops to QPSK 1/4 (~-2 dB threshold) in marginal conditions. This worked example shows the razor-thin margins in LEO broadband — every tenth of a decibel matters.

## Troubleshooting Payload Anomalies

| Symptom | Likely Cause | Diagnostic | Remedy |
|---------|-------------|-----------|--------|
| Low EIRP on one channel | TWTA underperforming | Check cathode current vs flight baseline | Switch to redundant TWTA |
| EIRP drop in rain | Atmospheric fade (Ka-band) | Monitor beacon S/N at reference station | Enable ACM, uplink power control |
| Adjacent channel interference | OMUX detuning (thermal) | Sweep VNA response vs temperature | Retune channel via heater trim |
| Beam pointing drift | Antenna thermal distortion | Compare beacon peak vs ephemeris | Update beam pointing tables |
| Multipactor event | Power surge in OMUX | Detect noise burst on spectrum analyser | Reduce power, re-test after bakeout |
| TWTA arcing | Internal contamination | Cathode current spikes, helix trip | Power cycle after 24 h hold |
| Phased array sidelobe rise | Failed phase shifter module | Beam pattern sweep via ground station | Disable element, re-taper weights |
| Cross-polarisation degradation | Feed misalignment or degradation | Measure XPD on boresight | Adjust polariser or accept reduced reuse |
| IMUX passband ripple | Temperature drift of cavities | VNA sweep in-orbit telemetry | Heater adjustment, channel reassignment |

## What This Article Does Not Cover

This article focuses on the RF payload — amplifiers, antennas, filters. It does **not** cover the [TT&C subsystem](./ttac.md) (spacecraft command and housekeeping telemetry), the [onboard data handling](./obdh.md) (avionics and flight software), the [power system](./spacecraft-power.md) (which supplies the 20 kW the payload demands), or the [thermal control](./thermal-control.md) (which rejects 10 kW of TWTA waste heat). Those are separate capabilities in the spacecraft-systems domain, each with their own article. The [telecom radio](../telecom/radio.md) heritage covers the underlying RF circuit design; this article covers only the space-specific amplifier, aperture, and filter engineering.

## Key Parameters Summary

- **Frequency**: S/C/Ku/Ka/V band, 1.5-51 GHz; Ku/Ka dominate modern broadband
- **TWTA power**: 50-250 W per channel; 60-70% DC-to-RF efficiency
- **TWTA lifetime**: 15-18 years (cathode limited, ~100,000 hours rated)
- **EIRP**: 40 dBW (global) to 70 dBW (VHTS spot beam)
- **Antenna diameter**: 0.8-3 m (reflector), 5-30 m (deployable mesh)
- **Phased array elements**: 120-2,000 per aperture (frequency/scan dependent)
- **Channel bandwidth**: 26-72 MHz (legacy), 125-500 MHz (HTS)
- **OMUX insertion loss**: 0.3-0.6 dB per channel
- **Multipactor margin**: designed >6 dB, tested at 1.5× rated power
- **Payload mass**: 200-800 kg (GEO commsat), 30-120 kg (LEO)
- **Payload DC power**: 1-20 kW (drives solar array and radiator sizing)

## See Also

- [Communications Transponders](./comms-payload.transponders.md) — bent-pipe and regenerative architectures
- [Satellite Antennas](./comms-payload.antennas.md) — reflectors, horns, phased arrays
- [Traveling-Wave Tube Amplifiers](./comms-payload.traveling-wave-tubes.md) — high-power microwave amplification
- [RF Multiplexers](./comms-payload.multiplexers.md) — channel filtering and combining
- [TT&C Systems](./ttac.md) — spacecraft command and telemetry link (separate subsystem)
- [Spacecraft Power](./spacecraft-power.md) — the solar arrays that feed the payload
- [Thermal Control](./thermal-control.md) — rejecting TWTA waste heat
- [Radio Communications](../telecom/radio.md) — RF circuit heritage
- [Electronics](../electronics/index.md) — mixed-signal and solid-state amplifier devices
- [Vacuum Deposition Systems](../vacuum/deposition-systems.md) — TWTA cathode and reflector coatings

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
