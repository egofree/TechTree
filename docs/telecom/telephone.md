# Telephone Systems

> **Node ID**: telecom.telephone
> **Domain**: [Telecommunications](./index.md)
> **Dependencies**: [`telecom.electric-telegraph`](electric-telegraph.md), [`energy.electricity`](../energy/electricity.md), [`metals`](../metals/index.md)
> **Timeline**: Years 25-50
> **Outputs**: telephone_service, telephone_exchanges, voice_communication

### Overview

The telephone transforms voice into electrical signals that travel over wire, enabling real-time two-way conversation at any distance. Unlike the telegraph (which transmits coded text requiring trained operators), the telephone allows anyone to communicate directly by speaking. This fundamental shift — from operator-mediated text to direct voice — transformed business, social life, and emergency response.

The telephone system builds on telegraph infrastructure (pole lines, wires, batteries) but requires fundamentally different terminal equipment (microphones, speakers, ringers) and switching systems (exchanges that connect any pair of subscribers on demand).

### Bell Telephone (1876)

**Principle**: A diaphragm vibrating in response to sound waves modulates the magnetic flux through a coil, inducing a varying electrical current. At the receiver, an identical device converts the current back into diaphragm vibration, reproducing the sound.

**Transmitter/receiver construction**:
- **Diaphragm**: Thin iron disc, 0.3-0.5 mm thick, 50-60 mm diameter, clamped at the edges. The diaphragm must be light enough to follow speech frequencies (100-3000 Hz) but stiff enough to move air effectively.
- **Electromagnet**: Permanent magnet (horseshoe type, barium ferrite or Alnico in later versions) with a coil of fine copper wire (0.1-0.2 mm diameter, 50-100 Ω resistance) wound on each pole. The coil sits close to the diaphragm (0.2-0.5 mm gap).
- **Operation**: Sound pressure → diaphragm vibrates → changes distance to magnet poles → changes magnetic flux → induces current in coil (Faraday's law). The induced current is proportional to diaphragm velocity, not position — it is inherently a differential (AC-coupled) signal.

**Performance limitations of the Bell design as transmitter**: The electromagnetic transmitter produces very weak signals (~1-10 mV output for normal speech at 30 cm distance). Effective range without amplification: 5-15 km on 1 mm copper wire. Beyond this, the signal-to-noise ratio drops below intelligibility. The Bell design works well as a receiver (earphone) but poorly as a transmitter.

### Carbon Microphone (Edison/Berliner, 1877-1878)

The enabling technology that made telephony practical beyond short distances. The carbon microphone produces a signal 50-100× stronger than the electromagnetic transmitter.

**Construction**:
- **Carbon granules**: Crushed carbon (anthracite coal or lampblack), sieved to 0.1-0.5 mm particle size. Packed loosely between two metal plates in a button-shaped capsule. Filling: ~0.5 g of granules.
- **Diaphragm**: Thin aluminum or mica disc acting as one electrode. The other electrode is a fixed brass button behind the granule chamber.
- **DC bias**: A battery (3-6 V) drives a DC current (10-50 mA) through the granules. Sound pressure compresses the granules, increasing contact area and decreasing resistance. Resistance varies from ~20-100 Ω as the diaphragm vibrates.
- **Output**: The resistance variation modulates the DC bias current, producing an AC signal superimposed on the DC. Output voltage: 0.5-2 V (100-1000× the Bell electromagnetic transmitter).

**Practical effect**: A carbon microphone transmitter enables clear telephone conversations over 30-80 km on 1 mm copper wire without amplification. The carbon microphone made city-wide telephone networks feasible.

**Maintenance**: Carbon granules degrade over time (moisture absorption, packing). Replace granules every 6-24 months. Humid environments require more frequent replacement. The microphone capsule unscrews for granule replacement.

### Magneto Ringer

Before automatic exchanges, every telephone needed a way to alert the called party (ringing). The magneto ringer generates an AC ringing signal by hand-cranking a small generator.

**Magneto generator**:
- Permanent-magnet alternator: 2-5 bar magnets (Alnico or tungsten steel) arranged around a rotating armature wound with fine copper wire (0.15-0.25 mm, 500-2000 turns).
- Output: 15-25 Hz AC at 50-100 V when cranked at 200-300 RPM. Power output: 2-5 W. Ringing is a low-frequency AC signal because the subscriber's bell responds to AC (the ringer coil inductance blocks DC voice frequencies).
- **Cranking effort**: Moderate — about the same as grinding coffee. A 3-second crank produces 3-5 seconds of ringing at the distant telephone.

**Polarized bell (ringer)**:
- Two gongs (brass or steel, 25-40 mm diameter) with a clapper driven by a polarized electromagnet. The electromagnet has a permanent magnet bias that causes the clapper to alternate between the gongs as the AC signal reverses polarity each half-cycle.
- Sensitivity: responds to 20-100 V AC at 15-25 Hz. Does NOT respond to DC (voice current is superimposed on DC and is too weak to ring the bell). The impedance matching between line and ringer coil is critical — too low an impedance loads the line and reduces voice volume; too high and the bell won't ring.

### Telephone Line Construction

**Wire**: Copper wire, 0.9-1.5 mm diameter (BWG 19-10 gauge). Hard-drawn copper for aerial lines (tensile strength 400-450 MPa). Resistance: 24-67 Ω/km depending on gauge. For a 10 km subscriber loop (20 km round trip), total wire resistance: 480-1340 Ω. With a 3 V battery and carbon microphone (20 Ω nominal), loop current: 2-6 mA — sufficient for intelligible speech.

**Cable**: Multiple twisted pairs in a lead-sheathed cable for underground or aerial installation. Typical city cable: 50-200 pairs of 0.5 mm copper wire (170 Ω/km per pair). Twisted pairs reduce crosstalk between adjacent circuits (the twist cancels inductive coupling).

**Loading coils**: For long-distance lines (>30 km), inductance loading extends the effective range. Loading coils (88 mH, spaced every 1.8 km along the line) compensate for the line's distributed capacitance, reducing attenuation in the voice frequency band (300-3400 Hz). With loading, effective telephone range extends from ~30 km to ~150 km without amplification.

**Loading coil specifications**:
- **Inductance**: 88 mH (standard "H-88" loading). Other values: 44 mH, 135 mH for different line conditions.
- **Spacing**: 1830 m (6000 ft) between coils. Must be precisely spaced — a 5% deviation causes impedance mismatch and signal reflection.
- **Cutoff frequency**: ~3400 Hz for H-88 loading. Frequencies above cutoff are severely attenuated. This is why telephone audio is band-limited to 300-3400 Hz — the loading coils enforce it.
- **Physical construction**: Toroidal coil wound on a powdered iron core, sealed in a cast iron case for weather protection. Installed in manholes or on pole-line brackets.

### Manual Switchboard (Cord Board)

The heart of a manual telephone exchange. An operator connects calling and called parties by plugging patch cords into jacks.

**Construction**:
- **Jack field**: A panel of 50-200 subscriber jacks, each connected to one subscriber line. Each jack has contacts for tip (T), ring (R), and sleeve (S) — the three-wire interface standard.
- **Answering jacks**: Each subscriber line also has an answering jack with a drop shutter (metal flap that falls when the subscriber cranks their magneto, indicating a call request).
- **Cord pairs**: Each operator position has 10-20 cord pairs. Each pair consists of an answering cord (plugged into the calling subscriber's jack) and a calling cord (plugged into the called subscriber's jack). Cords are 1-2 m long, with 1/4 inch phone plugs at each end.
- **Operator's set**: Headset (Bell-type receiver + carbon microphone breastplate transmitter) for speaking to subscribers. A "listen key" connects the operator to the cord pair. A "ring key" sends ringing current to the called party.

**Call setup procedure** (typical, 30-60 seconds):
1. Calling subscriber cranks magneto → drop shutter falls on the operator's board.
2. Operator plugs answering cord into the calling subscriber's jack, lifts the drop shutter, and asks "Number please?"
3. Caller says the number (e.g., "Main 2341").
4. Operator plugs calling cord into the called subscriber's jack and presses the ring key to ring the called party.
5. Called party answers → operator connects the two lines through the cord pair and monitors for call completion.
6. When either subscriber hangs up or cranks magneto, a supervisory lamp lights. Operator pulls both cords, resetting the connection.

**Capacity**: One operator handles 100-150 subscriber lines, completing 150-250 calls per hour during peak traffic. A busy exchange with 5,000 subscribers needs 30-50 operators per shift, 3 shifts = 90-150 operators total.

### Strowger Automatic Exchange (1889)

The step-by-step automatic exchange eliminates human operators. Invented by Almon B. Strowger (an undertaker who suspected operators were redirecting his calls to a competitor), the Strowger switch is a mechanical marvel that routes calls based on the dialed digits.

**Strowger switch (two-motion selector)**:
- A wiper arm that moves vertically (10 positions for each dialed digit) and then horizontally (10 positions) to select one of 100 output lines per switch. For an *n*-digit number, *n* switches are cascaded.
- **Vertical motion**: An electromagnet lifts the wiper arm one step per dial pulse. A 7-digit number (e.g., "7") sends 7 pulses, lifting the wiper to the 7th level.
- **Horizontal motion**: After reaching the correct vertical level, a second electromagnet rotates the wiper horizontally to find a free (idle) line on that level. The wiper tests each line in sequence (busy/idle test) and stops on the first free line.
- **Timing**: Dial pulses arrive at 10 pulses per second (international standard). Each pulse is a brief loop break (60-66 ms break, 33-40 ms make). The switch must track pulse count accurately — a missed pulse connects the wrong line.

**Dial telephone**:
- A rotary dial with 10 finger holes (1-0). The caller inserts a finger and rotates the dial to the finger stop, then releases. A spring mechanism returns the dial to rest position at a governed speed (10 pulses per second). Each digit produces a corresponding number of loop-break pulses.
- **Minimum inter-digit pause**: 200-500 ms for the switch to complete vertical stepping and begin horizontal hunting. Dialing a 7-digit number takes 15-25 seconds.

**Exchange capacity**:
- **100-line exchange**: 1 selector bank (10 × 10). Suitable for a small business or hotel.
- **1,000-line exchange**: 2 selector stages (10 groups of 100). Requires ~100 group selectors and ~1,000 line finders.
- **10,000-line exchange**: 3 selector stages. Requires thousands of switches, occupying a large building. Power consumption: 5-20 kW for the ringer generators (ringing current is generated by a motor-driven alternator), switch magnets, and supervisory circuits.
- **Physical size**: A 10,000-line Strowger exchange fills a 500-1000 m² floor with equipment racks 2-3 m tall. The switches are noisy (clicking and clacking of relays and stepping magnets) — operators in the exchange room required hearing protection in later years.

**Reliability**: Strowger switches are remarkably reliable. A well-maintained switch completes 100,000+ calls between failures. Maintenance: clean contacts monthly, adjust spring tension quarterly, replace worn wiper tips annually. Each switch has 50-100 moving parts — the mechanical complexity is the main failure mode.

### Technical Specifications Summary

| Parameter | Value | Notes |
|-----------|-------|-------|
| Voice frequency band | 300-3400 Hz | Limited by loading coils |
| Transmitter output (carbon) | 0.5-2 V | 50-100× Bell electromagnetic |
| Loop current | 10-50 mA | Set by battery voltage and loop resistance |
| Battery voltage | 3-6 V (local) / 48 V (exchange) | Local battery at subscriber; exchange battery for automatic |
| Maximum loop resistance | ~1500 Ω | ~30 km on 0.9 mm Cu (unloaded) |
| Loading coil spacing | 1830 m | H-88 standard |
| Dial pulse rate | 10 pulses/second | International standard |
| Exchange capacity | 100-10,000 lines | Strowger step-by-step |
| Operator capacity | 100-150 lines/operator | Manual cord board |

### Telephone Network Growth

The telephone's growth rate exceeded the telegraph by 10×. In the US, telegraph lines took 40 years (1844-1884) to reach 250,000 miles of wire. The telephone reached 250,000 subscribers in just 20 years (1876-1896), and 10 million subscribers by 1920. The key difference: anyone can speak into a telephone, while telegraph requires trained Morse code operators.

**Subscriber density and exchange sizing**:
- **Rural exchange**: 50-200 subscribers, 1-2 operators (or a small Strowger exchange). Covers a 10-15 km radius. One exchange per small town.
- **Urban exchange**: 2,000-10,000 subscribers, 20-50 operators (or a multi-thousand-line Strowger). Covers a 3-5 km radius. Multiple exchanges per city, connected by inter-exchange trunks.
- **Toll (long-distance) connections**: Dedicated lines between city exchanges, usually 4-wire (separate transmit and receive paths) for full-duplex operation with amplifiers. A 500 km toll connection with 3 loading coil sections and 2 vacuum tube repeater amplifiers (post-1915) provides commercial-quality voice transmission.

### Safety Considerations

- **Battery acid**: Local batteries (2-3 Leclanché cells) contain acidic electrolyte. Spills corrode the wooden telephone case and damage clothing. Keep batteries in a drip tray. Replace leaking cells promptly.
- **Electrical shock**: Exchange batteries (48 V) can deliver a painful shock under wet conditions. The ringing current (75-100 V AC at 20 Hz) is more hazardous — it can cause muscle contraction and prevent the victim from releasing the wire. Never touch bare wires during ringing.
- **Fire**: Telephone exchanges contain thousands of relays in close proximity, generating heat and occasional sparks from contact arcing. The relay racks are made of steel (fire-resistant), but cable insulation (paper, lead, early plastics) is combustible. Fire suppression: CO₂ or dry chemical extinguishers at each equipment bay. Water damages switch contacts — never use water on an exchange fire.
- **Hearing damage**: Strowger exchange equipment rooms produce 75-90 dB of continuous relay clicking. Prolonged exposure (>8 hours) causes permanent hearing loss. Maintenance staff should wear hearing protection.
- **Lead exposure**: Lead-sheathed underground cables present lead exposure risk during splicing. Workers must wash hands before eating. Lead sheathing is cut with a knife — cuts from the lead sheath are slow to heal and prone to infection.
- **Carbon microphone dust**: Carbon granules from microphone capsules are fine particulate matter. Avoid inhaling granule dust during replacement. The carbon itself is not toxic, but chronic inhalation of any fine particulate damages lung tissue. Replace granules in a well-ventilated area.
- **Electromagnetic interference**: Telephone lines running parallel to power lines for extended distances pick up induced 50/60 Hz hum from the power line's magnetic field. This is not a safety hazard but severely degrades call quality. Maintain at least 2 m separation between telephone and power lines on joint-use poles. Cross power lines at 90° angles where possible.
- **Static electricity**: In dry climates, static charge builds up on long above-ground telephone wires. A static discharge through the earpiece can startle the user (unpleasant but rarely dangerous). Install carbon block lightning protectors at each subscriber's premises to shunt static and lightning-induced surges to ground.

### See Also

- [Electrical Telegraph Networks](electric-telegraph.md) — The precursor network that telephone builds upon
- [Telegraph Communication](../transport/telegraph.md) — Hardware details for telegraph equipment
- [Radio Communication](radio.md) — Wireless voice communication
- [Submarine Cable Systems](submarine-cables.md) — Undersea telephone cables

*Part of the [Bootciv Tech Tree](../index.md) • [Telecommunications](./index.md) • [All Domains](../index.md)*
