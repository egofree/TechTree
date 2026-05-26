# Telephone Systems

> **Node ID**: telecom.telephone
> **Domain**: [Telecommunications](./index.md)
> **Dependencies**: [`energy.electricity`](../energy/electricity.md), `metals`, [`telecom.electric-telegraph`](electric-telegraph.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 25-50
> **Outputs**: telephone_service, telephone_exchanges, voice_communication

## Overview

The telephone transforms voice into electrical signals that travel over wire, enabling real-time two-way conversation at any distance. Unlike the telegraph (which transmits coded text requiring trained operators), the telephone allows anyone to communicate directly by speaking. This fundamental shift — from operator-mediated text to direct voice — transformed business, social life, and emergency response.

The telephone system builds on telegraph infrastructure (pole lines, wires, batteries) but requires fundamentally different terminal equipment (microphones, speakers, ringers) and switching systems (exchanges that connect any pair of subscribers on demand).

### Bell Telephone (1876)

**Principle**: A diaphragm vibrating in response to sound waves modulates the magnetic flux through a coil, inducing a varying electrical current. At the receiver, an identical device converts the current back into diaphragm vibration, reproducing the sound.

**Transmitter/receiver construction**:
- **Diaphragm**: Thin iron disc, 0.3-0.5 mm thick, 50-60 mm diameter, clamped at the edges.
- **Electromagnet**: Permanent magnet (horseshoe type) with a coil of fine copper wire (0.1-0.2 mm, 50-100 ohm) on each pole, 0.2-0.5 mm gap to diaphragm.

**Performance limitations**: The electromagnetic transmitter produces very weak signals (~1-10 mV). Effective range without amplification: 5-15 km on 1 mm copper wire. The Bell design works well as a receiver (earphone) but poorly as a transmitter.

### Carbon Microphone (Edison/Berliner, 1877-1878)

The enabling technology that made telephony practical beyond short distances. Produces a signal 50-100x stronger than the electromagnetic transmitter.

**Construction**:
- **Carbon granules**: Crushed carbon (anthracite coal or lampblack), 0.1-0.5 mm particle size. ~0.5 g packed between two metal plates.
- **Diaphragm**: Thin aluminum or mica disc acting as one electrode.
- **DC bias**: 3-6 V battery drives 10-50 mA through granules. Resistance varies ~20-100 ohm as diaphragm vibrates.
- **Output**: 0.5-2 V (100-1000x the Bell electromagnetic transmitter).

**Practical effect**: Carbon microphone enables clear conversations over 30-80 km on 1 mm copper wire without amplification. Maintenance: replace carbon granules every 6-24 months (moisture absorption degrades performance).

### Magneto Ringer

Before automatic exchanges, every telephone needed a way to alert the called party. The magneto ringer generates an AC ringing signal by hand-cranking a small generator.

**Magneto generator**: Permanent-magnet alternator, 2-5 bar magnets around a rotating armature (0.15-0.25 mm wire, 500-2000 turns). Output: 15-25 Hz AC at 50-100 V when cranked at 200-300 RPM. A 3-second crank produces 3-5 seconds of ringing.

**Polarized bell**: Two gongs (brass or steel, 25-40 mm diameter) with a clapper driven by a polarized electromagnet. Responds to 20-100 V AC at 15-25 Hz. Does NOT respond to DC voice current.

### Telephone Line Construction

**Wire**: Copper wire, 0.9-1.5 mm diameter (BWG 19-10 gauge). Hard-drawn for aerial lines (tensile strength 400-450 MPa). Resistance: 24-67 ohm/km. For a 10 km loop (20 km round trip): 480-1340 ohm total. With 3 V battery: 2-6 mA loop current — sufficient for intelligible speech.

**Cable**: Multiple twisted pairs in lead-sheathed cable. Typical city cable: 50-200 pairs of 0.5 mm copper wire (170 ohm/km per pair). Twisted pairs reduce crosstalk between adjacent circuits.

**Loading coils**: For long-distance lines (>30 km), 88 mH inductors spaced every 1.8 km extend effective range from ~30 km to ~150 km without amplification. Cutoff frequency: ~3400 Hz — this is why telephone audio is band-limited to 300-3400 Hz.

### Manual Switchboard (Cord Board)

The heart of a manual telephone exchange. An operator connects calling and called parties by plugging patch cords into jacks.

**Construction**:
- **Jack field**: 50-200 subscriber jacks, each with tip (T), ring (R), and sleeve (S) contacts.
- **Answering jacks**: Drop shutter falls when subscriber cranks magneto, indicating call request.
- **Cord pairs**: 10-20 cord pairs per operator position. Each pair has answering cord and calling cord, 1-2 m long.
- **Operator's set**: Headset (Bell-type receiver + carbon microphone breastplate transmitter).

**Call setup** (30-60 seconds):
1. Calling subscriber cranks magneto → drop shutter falls.
2. Operator plugs answering cord, lifts shutter, asks "Number please?"
3. Operator plugs calling cord into called subscriber's jack, presses ring key.
4. Called party answers → operator connects lines through cord pair.
5. On hang-up, supervisory lamp lights → operator pulls both cords.

**Capacity**: One operator handles 100-150 subscriber lines, completing 150-250 calls/hour at peak. A 5,000-subscriber exchange needs 30-50 operators per shift, 3 shifts = 90-150 total.

### Strowger Automatic Exchange (1889)

Eliminates human operators. A mechanical marvel that routes calls based on dialed digits.

**Strowger switch (two-motion selector)**:
- Wiper arm moves vertically (10 positions per digit) then horizontally (10 positions) to select one of 100 output lines.
- Dial pulses arrive at 10 pulses/second (60-66 ms break, 33-40 ms make).

**Dial telephone**: Rotary dial with 10 finger holes. Spring mechanism returns dial at governed speed (10 pulses/second). Dialing a 7-digit number takes 15-25 seconds.

**Exchange capacity**:
- 100-line: 1 selector bank. Small business or hotel.
- 1,000-line: 2 selector stages. Requires ~100 group selectors.
- 10,000-line: 3 selector stages. Thousands of switches in 500-1000 m2 building. Power consumption: 5-20 kW.

## Bill of Materials

### Single Telephone Set (manual exchange)

| Material | Quantity | Specification | Source |
|----------|----------|---------------|--------|
| Diaphragm (iron) | 1 | 0.3-0.5 mm thick, 50-60 mm diameter | [Metals](../metals/index.md) |
| Copper wire (coil) | 50-100 m | 0.1-0.2 mm diameter, enameled | [Metals](../metals/index.md) |
| Permanent magnet (horseshoe) | 1 | Barium ferrite or tungsten steel | [Metals](../metals/index.md) |
| Carbon granules | 0.5 g | Anthracite, 0.1-0.5 mm particle size | [Mining](../mining/index.md) |
| Magneto generator | 1 | 2-5 bar magnets, 500-2000 turn armature | [Metals](../metals/index.md) |
| Bell gongs (brass) | 2 | 25-40 mm diameter | [Metals](../metals/index.md) |
| Handset casing (bakelite) | 1 | Phenolic resin, molded | [Chemistry](../chemistry/index.md) |
| Battery (local) | 2-3 cells | Leclanche or lead-acid, 3-6 V | [Chemistry](../chemistry/index.md) |
| Terminal block and wiring | 1 set | Brass terminals, insulated copper wire | [Metals](../metals/index.md) |

### Pole Line (per km, 50-pair cable)

| Material | Quantity per km | Specification | Source |
|----------|----------------|---------------|--------|
| Poles (timber) | 12-20 | 7-9 m length, 15-20 cm top diameter, creosote-treated | [Forestry](../plants/index.md) |
| 50-pair cable | 1 km | 0.5 mm copper pairs, lead-sheathed, 170 ohm/km/pair | [Metals](../metals/index.md) |
| Suspension strand (steel) | 1 km | 6-8 mm galvanized steel wire | [Metals](../metals/index.md) |
| Pole hardware | 12-20 sets | Brackets, bolts, cable clamps | [Metals](../metals/index.md) |

### Loading Coils (per 1.8 km section)

| Material | Quantity per section | Specification | Source |
|----------|---------------------|---------------|--------|
| Powdered iron core | 1 | Toroidal, for 88 mH inductance | [Metals](../metals/index.md) |
| Copper magnet wire | 50-100 m | 0.2-0.4 mm diameter, enameled | [Metals](../metals/index.md) |
| Cast iron case | 1 | Weatherproof, sealed | [Metals](../metals/index.md) |

### Manual Switchboard (100-line)

| Material | Quantity | Specification | Source |
|----------|----------|---------------|--------|
| Subscriber jacks | 100 | 3-contact (T, R, S), panel-mounted | [Metals](../metals/index.md) |
| Drop shutters | 100 | Spring-loaded metal flaps | [Metals](../metals/index.md) |
| Cord pairs | 15-20 | 1-2 m flexible cord with plugs | [Textiles](../textiles/index.md) |
| Operator headsets | 2-3 | Bell receiver + carbon transmitter | [Metals](../metals/index.md) |
| Ringing battery | 1 bank | 48 V lead-acid or 75 V magneto | [Chemistry](../chemistry/index.md) |
| Desk/console | 1 | Wooden cabinet, 1.5 m wide x 1 m deep | [Forestry](../plants/index.md) |

## Quantitative Parameters

### Voice Signal Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Voice frequency band | 300-3400 Hz | Enforced by loading coils and exchange filters |
| Transmitter output (carbon mic) | 0.5-2 V | 50-100x Bell electromagnetic transmitter |
| Transmitter output (Bell type) | 1-10 mV | Too weak for practical use as transmitter |
| Loop current | 10-50 mA | Set by battery voltage and loop resistance |
| Local battery voltage | 3-6 V | For carbon microphone bias |
| Exchange battery voltage | 48 V | For automatic exchanges (loop-powered) |
| Ringing voltage | 50-100 V AC | 15-25 Hz, from magneto or exchange ringer |
| Ringing frequency | 15-25 Hz | Low enough to pass through ringer coil inductance |

### Line Parameters

| Parameter | 0.5 mm Cu | 0.9 mm Cu | 1.5 mm Cu | Notes |
|-----------|-----------|-----------|-----------|-------|
| Resistance (ohm/km/pair) | 170 | 56 | 24 | Round trip = 2x |
| Max loop length (unloaded) | ~5 km | ~15 km | ~30 km | Limited by loop resistance (~1500 ohm max) |
| Max loop length (H-88 loaded) | ~30 km | ~80 km | ~150 km | Loading coils every 1.83 km |
| Attenuation (unloaded, 1 kHz) | ~1.5 dB/km | ~0.8 dB/km | ~0.4 dB/km | Voice-frequency attenuation |
| Crosstalk (adjacent pairs) | -60 to -80 dB | -60 to -80 dB | -60 to -80 dB | With twisted pairs |

### Exchange Parameters

| Parameter | Manual Cord Board | Strowger (10,000-line) |
|-----------|-------------------|----------------------|
| Capacity | 100-5,000 lines | 100-10,000 lines |
| Operators required | 1 per 100-150 lines | None (automatic) |
| Call setup time | 30-60 seconds | 15-25 seconds (dialing) |
| Lines per operator | 100-150 | N/A |
| Power consumption | 500 W - 2 kW | 5-20 kW (switch magnets, ringers) |
| Floor space | 20-100 m2 | 500-1000 m2 |
| Dial pulse rate | N/A | 10 pulses/second |
| Switch reliability | Depends on operator | 100,000+ calls between failures |

## Scaling Notes

### Single Exchange (50-500 subscribers)

One exchange building with manual cord board or small Strowger switch. Covers a 5-15 km radius. A rural town exchange with 100 subscribers requires 1-2 operators (manual) or a small Strowger unit (automatic). Construction cost: $5,000-25,000. Local calls use 2-wire circuits with battery from the exchange or subscriber set. No amplification needed for loops under 10 km.

### City Network (2,000-50,000 subscribers)

Multiple exchanges connected by inter-exchange trunks. Each exchange covers a 3-5 km radius. Trunks are 4-wire (separate transmit and receive) for full-duplex with amplifiers. A 10,000-subscriber city needs 3-5 exchanges. Staffing (manual): 200-500 operators across all exchanges. Long-distance toll circuits connect to other cities via loading coils and, post-1915, vacuum tube repeater amplifiers.

### Long-Distance Network (100+ km between cities)

Toll circuits with loading coils every 1.83 km and vacuum tube repeaters every 80-150 km. A 500 km connection needs 3-6 repeater stations. Each repeater uses 2 vacuum tubes (one per direction) with 150-200 V plate supply. Construction cost: $10,000-30,000 per km for loaded toll cable. The first US transcontinental telephone line (1915, 5,400 km) used 130,000 poles, 2,500 tonnes of copper wire, and 3 vacuum tube repeaters.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| No dial tone (automatic exchange) | Line broken; exchange fuse blown; subscriber line card failed | Check line continuity from subscriber to exchange; replace line card fuse; test for ground fault on subscriber wiring |
| Faint or distant voice | High loop resistance (long line, corroded splice); degraded carbon granules | Test loop resistance (should be <1500 ohm); clean or re-splice joints; replace carbon granules in subscriber microphone |
| Crosstalk (hearing other conversations) | Cable pair untwisted; wet cable with reduced insulation; adjacent pair imbalance | Inspect cable for damage; test pair-to-pair insulation; resplice any untwisted sections; replace water-damaged cable sections |
| Hum (60/50 Hz buzz) | Power line induction; ground loop; unbalanced pair | Maintain 2 m separation from power lines; check ground connections; ensure pair is balanced (equal resistance on tip and ring) |
| Bell not ringing | Ringer coil open; magneto not generating; line too long (insufficient ringing voltage) | Test ringer coil continuity; check magneto output (should produce 50-100 V AC); if line is too long, install ringing booster or move subscriber to closer exchange |
| Dial not completing calls | Dial speed incorrect (not 10 pps); dirty dial contacts; Strowger switch mis-stepping | Adjust dial governor speed; clean dial pulse contacts with contact cleaner; check switch bank for worn wiper tips |
| Echo (hearing own voice back) | Impedance mismatch at 2-wire/4-wire hybrid; unloaded long line | Install impedance-matching hybrid coil at junction; add loading coils to long subscriber loops |
| Intermittent disconnects | Loose terminal screw; corroded battery contact; frayed cord wire | Tighten all terminal screws; clean battery contacts; replace frayed handset and line cords |
| Static/crackling | Dirty switchboard cord contacts; loose jumper wire at MDF; carbon granule contamination | Clean cord plug contacts; re-punch loose jumper wires at main distribution frame; replace carbon granules |
| Party line interference (cross-ringing) | Frequency-selective ringer misadjusted; wrong ringer frequency on shared line | Adjust ringer bias spring for correct frequency response; reassign subscriber to correct ringing frequency code |

## Safety Considerations

- **Battery acid**: Local batteries (Leclanche cells) contain acidic electrolyte. Spills corrode wooden cases and damage clothing. Keep batteries in drip trays. Replace leaking cells promptly.
- **Electrical shock**: Exchange batteries (48 V) deliver a painful shock under wet conditions. Ringing current (75-100 V AC at 20 Hz) is more hazardous — can cause muscle contraction preventing release. Never touch bare wires during ringing.
- **Fire**: Telephone exchanges contain thousands of relays generating heat and occasional sparks from contact arcing. Cable insulation (paper, lead, early plastics) is combustible. Fire suppression: CO2 or dry chemical extinguishers at each equipment bay. Water damages switch contacts — never use water on an exchange fire.
- **Hearing damage**: Strowger exchange equipment rooms produce 75-90 dB of continuous relay clicking. Prolonged exposure (>8 hours) causes permanent hearing loss. Maintenance staff should wear hearing protection.
- **Lead exposure**: Lead-sheathed underground cables present lead exposure risk during splicing. Workers must wash hands before eating. Cuts from lead sheathing are slow to heal and prone to infection.
- **Carbon microphone dust**: Fine particulate matter during granule replacement. Avoid inhaling dust. Replace granules in a well-ventilated area.
- **Electromagnetic interference**: Telephone lines parallel to power lines pick up induced 50/60 Hz hum. Maintain at least 2 m separation. Cross power lines at 90 degree angles.
- **Lightning and static**: Install carbon block lightning protectors at each subscriber's premises. In dry climates, static charge builds up on long above-ground wires — a discharge through the earpiece can startle the user.

## Telephone Network Growth

The telephone's growth rate exceeded the telegraph by 10x. In the US, telegraph lines took 40 years (1844-1884) to reach 250,000 miles of wire. The telephone reached 250,000 subscribers in just 20 years (1876-1896), and 10 million subscribers by 1920. The key difference: anyone can speak into a telephone, while telegraph requires trained Morse code operators.

**Subscriber density and exchange sizing**:
- **Rural exchange**: 50-200 subscribers, 1-2 operators or small Strowger. Covers 10-15 km radius.
- **Urban exchange**: 2,000-10,000 subscribers, 20-50 operators or multi-thousand-line Strowger. Covers 3-5 km radius. Multiple exchanges per city connected by inter-exchange trunks.
- **Toll (long-distance)**: Dedicated 4-wire lines between cities with loading coils and vacuum tube repeaters. A 500 km connection with 3 loading sections and 2 repeaters provides commercial-quality voice.

### See Also

- [Electrical Telegraph Networks](electric-telegraph.md) — The precursor network that telephone builds upon
- [Telegraph Communication](../transport/telegraph.md) — Hardware details for telegraph equipment
- [Radio Communication](radio.md) — Wireless voice communication
- [Submarine Cable Systems](submarine-cables.md) — Undersea telephone cables

---
*Part of the [Bootciv Tech Tree](../index.md) • [Telecommunications](./index.md) • [All Domains](../index.md)*
