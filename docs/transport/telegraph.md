# Telegraph Communication

> **Node ID**: transport.telegraph
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`chemistry.acids`](../chemistry/acids.md), [`energy.electricity`](../energy/electricity.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`telecom`](../telecom/index.md), [`telecom.electric-telegraph`](../telecom/electric-telegraph.md)
> **Timeline**: Years 15-30
> **Outputs**: telegraph_network
> **Critical**: No

### Principles

Electrical current through wire produces electromagnetic effect at receiver. Information encoded as sequences of current on/off (binary — Morse code: dots and dashes represent letters and numbers).

**Circuit**: Battery (or generator) → telegraph key (switch) → transmission wire → sounder (electromagnet + armature) → ground return (earth completes circuit — single wire sufficient for most installations).

### Telegraph Key

Spring-loaded lever with electrical contacts. Press lever → contacts close → current flows → remote sounder clicks. Release → spring opens contacts → sounder clacks.

- **"Dot"** = short press (~0.1 s)
- **"Dash"** = long press (~0.3 s)
- **Pause between elements** ~0.1 s
- **Pause between letters** ~0.3 s
- **Pause between words** ~0.7 s

Construction: brass contacts, steel spring, hardwood lever mounted on cast iron base. Contacts adjustable with set screws for feel and gap. Wear-resistant contact points (silver or platinum for longevity). Multiple keys per station for operators sending on different lines simultaneously.

### Sounder

Electromagnet (iron core with many turns of fine copper wire — 5-20 Ω resistance). Armature (iron bar) held above electromagnet core by spring. When current flows → electromagnet pulls armature down → "click" sound. When current stops → spring pulls armature up → "clack" sound. Operator listens to click-clack pattern and translates to letters. Trained operators achieve 20-40 words per minute.

- **Electromagnet**: Soft iron core (laminated to reduce eddy currents), wound with 200-500 turns of enameled copper wire (0.3-0.5 mm diameter). Resistance 5-20 Ω matches line characteristics.
- **Armature**: Mild steel bar, hinged at one end. Adjustable spring tension controls click force and response speed.
- **Mounting**: Wood or iron base, adjustable feet for stable placement on operator's desk.

### Morse Code

Standardized international code:
```
A .-    B -...  C -.-.  D -..   E .     F ..-.  G --.   H ....
I ..    J .---  K -.-   L .-..  M --    N -.    O ---   P .--.
Q --.-  R .-.   S ...   T -     U ..-   V ...-  W .--   X -..-
Y -.--  Z --..
0 -----  1 .----  2 ..---  3 ...--  4 ....-  5 .....
6 -....  7 --...  8 ---..  9 ----.
```

Prosigns (procedure signals): `AR` (end of message), `SK` (end of work), `R` (received), `GA` (go ahead), `ERR` (error — cancel last word).

### Wire and Line Construction

**Wire**: Iron or copper wire, 2-4 mm diameter. Iron stronger (less sag between poles) but higher resistance (poor conductor). Copper better conductor but requires more support. Galvanized iron wire (zinc-coated for corrosion resistance) is the common compromise. Resistance: ~10-50 Ω/km depending on wire gauge.

**Poles**: Wooden poles (treated timber, 6-10 m tall), spaced 40-60 m apart. Wire attached via glass or ceramic insulators (prevents current leakage through wet pole). Single wire on cross-arm. Ground wire at each station.

**Insulators**: Glass or ceramic. Threaded onto wooden pins on cross-arm. Wire tied with wire wrap or clamp. Insulator prevents leakage path through wet pole to ground — critical in rain and fog.

**Range**: Direct current from batteries effective to ~50-100 km (voltage drop in wire limits range). For longer distances: relay stations every 50-100 km. Or use higher voltage (100-200 V from generator). Transcontinental telegraph: ~5000 km with ~50-100 relay stations.

### Battery Supply

**Daniell cell**: Copper electrode in CuSO₄ solution | unglazed porcelain separator | zinc electrode in ZnSO₄ or dilute H₂SO₄ solution. Voltage: 1.1 V per cell. Stack 10-50 cells in series for desired line voltage (10-50 V). Stable output, long life (months of continuous operation).

- **Construction**: Glass or earthenware jars. Copper plate in outer compartment filled with saturated CuSO₄ solution (blue). Zinc plate in inner porous pot filled with dilute H₂SO₄. Replace zinc electrode as it corrodes.
- **Alternative**: Leclanché cell (carbon-zinc, 1.5 V, cheaper but less stable). Or use DC generator for higher voltage and no consumable electrodes.

### Relay Stations

At ~50-100 km intervals along long lines. Incoming signal activates electromechanical relay → re-transmits signal on fresh battery power to next station. Each relay station needs: battery bank, relay mechanism, operator (or automatic relay), shelter.

- **Relay mechanism**: Sensitive polarized relay (two electromagnets, permanent magnet bias) responds to weak incoming signal. Contacts close on local circuit → transmits strong signal to next section.
- **Staffing**: One operator per relay station, 24-hour shifts. Reads incoming messages, logs, re-transmits.

**Strengths**:
- Single wire + ground return minimizes infrastructure — one wire per circuit instead of two
- Trained operators achieve 20-40 words per minute with Morse code
- Daniell cells provide stable 1.1 V per cell for months of continuous operation

**Weaknesses**:
- DC from batteries effective only to ~50-100 km — relay stations needed every 50-100 km
- Iron wire has high resistance (~10-50 Ω/km) — limits range without relay stations
- Glass/ceramic insulators critical in rain and fog — leakage through wet poles degrades signal

### Network Topology

**Hub-and-spoke**: Central station connects to multiple outstations. Switchboard (manual patch panel) connects any pair of lines. Message routing: operator receives message, re-transmits to destination line.

**Block signaling (railway integration)**: Telegraph circuits connect adjacent block posts on railway. Block instruments show line status (occupied/clear). Operator confirms train has cleared block before allowing next train entry. Prevents rear-end collisions — the first electrical safety system.

**Throughput**: 20-40 words/minute per line. For coordination of distant mining, manufacturing, and construction operations, this is transformative — decisions that took days by courier now take minutes.

### Wire Technology

**Iron wire**: The standard telegraph conductor for decades. Drawn from wrought iron rod through successive dies to 3-4 mm diameter. Tensile strength 350-450 MPa. Breaking load for 4 mm wire: ~4500 N (450 kg). Resistance approximately 50-80 Ω/km for 3 mm wire, 30-50 Ω/km for 4 mm. Galvanized (zinc-coated by hot-dipping at 450°C) for corrosion resistance. Galvanized coating thickness 40-80 μm, extends service life from 2-5 years (bare iron rusts quickly outdoors) to 15-25 years.

**Copper wire**: Superior conductor (resistivity 17 nΩ·m vs. 100 nΩ·m for iron). A 3 mm copper wire has resistance ~24 Ω/km, roughly one-third that of iron. But copper's tensile strength is only 200-300 MPa (annealed), so it sags more between poles. Hard-drawn copper (cold-worked during drawing) reaches 400-450 MPa but becomes brittle. Copper wire became practical once galvanizing or rubber insulation prevented corrosion at attachment points.

**Wire stringing**: Pay out wire from a reel mounted on a wagon. Attach to insulators on each pole. Tension the wire to 15-25% of breaking load (enough to minimize sag without risking fatigue failure from wind vibration). Sag between poles at 50 m span: calculate with the catenary equation. For 4 mm iron wire at 20% breaking load, sag is approximately 0.5-1.0 m at 50 m span. Adjust tension at each pole with a turnbuckle.

**Pole line construction**:
- Poles: treated timber (creosote or pentachlorophenol), 6-10 m tall, 15-20 cm diameter at the top. Set in augured holes 1.2-1.5 m deep, backfilled and tamped. Pole spacing 40-60 m (closer on curves and in heavy ice regions). A single pole supports 1-6 wires on cross-arms (timber brackets bolted to the pole, each arm carrying 4-8 wires).
- Guy wires (steel wire rope, 6-8 mm) brace corner poles and terminal poles against the unbalanced wire tension. Anchor guy wires to a buried log or screw anchor rated at 5000-10000 N holding power.

### Electrical Specifications

**Line current**: A typical telegraph circuit draws 20-50 mA when the key is closed. The sounder relay pulls in at 5-10 mA (sensitivity threshold). Below 5 mA, the armature won't reliably pull in, and characters are lost. The operator has to request re-transmission.

**Voltage budget**: For a 100 km line of 4 mm iron wire (resistance ~40 Ω/km), total loop resistance is 4000 Ω (100 km out + 100 km ground return, though ground return is typically 10-20 Ω and negligible). Add sounder resistance (5-20 Ω). Battery voltage needed: V = I × R = 0.030 A × 4020 Ω = 120 V. Stack 110 Daniell cells in series (1.1 V each). At 50 km, only 60 V needed (55 cells).

**Line insulation**: Each insulator must present >100 MΩ resistance to ground in dry weather, >10 MΩ in rain. Wet glass insulators can leak enough current to drop the line below relay threshold. Double-petticoat insulators (two nested glass bells with an air gap) provide a longer leakage path and better wet-weather performance.

**Relay sensitivity**: Polarized relay uses a permanent magnet to bias the armature. The signal current creates a magnetic field that adds to or opposes the permanent magnet bias. Sensitivity down to 1-5 mA with careful adjustment. The relay contacts switch a local circuit powered by a fresh battery, regenerating the signal at full strength for the next line segment. This is the fundamental repeater principle.

### Morse Code Timing

**Element timing**:
- Dot duration: 0.1-0.2 seconds (operator dependent). This is the basic time unit.
- Dash: exactly 3× dot duration (0.3-0.6 s).
- Intra-character gap: 1× dot (space between dots/dashes within a letter).
- Inter-character gap: 3× dot (space between letters).
- Word gap: 7× dot (space between words).

**Practical speed**: 20-30 words per minute for a skilled operator. A "word" is standardized as 5 characters (the "PARIS" standard: the word PARIS has 50 time units including word gap, so 50 dot-lengths = 1 word at a given speed). At 20 WPM, one dot = 60 ms. At 30 WPM, one dot = 40 ms. Automatic keying (machines reading punched paper tape) can reach 60-100 WPM.

**Signal propagation**: Electrical signals travel at near light speed (~200,000-280,000 km/s on iron wire, slower than in free space due to the velocity factor of the conductor). A 3000 km line has roughly 10-15 ms propagation delay, negligible for Morse code. The bottleneck is always the human operator.

### Network Architecture

**Main office switchboard**:
- A manually operated patch panel (copper bus bars with spring clips or plug-and-jack connections). The switchboard operator connects any incoming line to any outgoing line by inserting a patch cord. A busy main office handles 20-50 lines simultaneously.
- Each line has a call indicator (a galvanometer needle or a small sounder that clicks when a distant station starts transmitting). The operator hears the click, plugs into that line, and routes the message to the destination.

**Message handling**:
- Incoming message: operator copies by ear onto a message form (time, date, origin, destination, text, number of words). Verifies word count. Routes to destination line and re-transmits.
- Billing: by the word (distance-independent within the network, or distance-tiered). A 20-word message between cities costs roughly equivalent to a day's wages for a laborer. Expensive enough to keep messages concise, cheap enough to transform business coordination.

### Telephone Development

**[Bell telephone](../glossary/bell-telephone.md)** (1876):
- A diaphragm (thin iron disc, 0.3-0.5 mm thick, 50-60 mm diameter) vibrates in response to sound waves. A permanent magnet with a coil of fine wire (0.1-0.2 mm, 50-100 Ω) sits near the diaphragm. Vibration changes the magnetic flux through the coil, inducing a current that is an electrical analog of the sound.
- At the receiver, an identical device converts the varying current back into diaphragm vibration, reproducing the sound. The same unit can serve as both transmitter and receiver (though performance is poor as a transmitter compared to a carbon microphone).

**[Carbon microphone](../glossary/carbon-microphone.md)** (Edison/Berlinner improvement):
- A capsule containing carbon granules (0.1-0.5 mm crushed carbon) between two metal plates. One plate is the diaphragm. Sound pressure compresses the granules, changing their contact resistance. A DC bias current (from a battery, 3-6 V) flows through the granules. The resistance variation modulates the current, producing a much stronger signal than the Bell electromagnetic transmitter (100× the output).
- Requires a battery at each telephone set. The carbon microphone made telephony practical at distances beyond a few kilometers.

**Magneto ringer**:
- A hand-cranked AC generator (2-5 magnet permanent-magnet alternator, 15-25 Hz output, 50-100 V) at each telephone. Cranking the magneto sends an AC ringing signal down the line to alert the called party. A polarized bell (two gongs with a clapper driven by an electromagnet) at the receiver responds to the AC signal. The bell does not respond to DC (voice current is superimposed on DC and is too weak to ring the bell).

**Switchboard (manual exchange)**:
- An operator at a cord board connects calling and called parties by plugging patch cords into jacks. Each subscriber line has a calling indicator (a metal flap that drops when the subscriber cranks their magneto). The operator speaks to the caller, determines the destination, rings the called party, and connects the two lines. Capacity: one operator handles 50-100 subscriber lines.

### Wireless Telegraphy

**Spark gap transmitter**:
- A high-voltage transformer (or induction coil) charges a capacitor (Leyden jar: glass plate with tin foil on both sides, 500-2000 pF, rated to 20-50 kV). When voltage exceeds the breakdown voltage of the spark gap (adjustable brass balls, 1-5 mm gap), a spark arcs across. The spark excites a tuned circuit (inductor + capacitor) connected to an antenna wire, producing a damped radio-frequency oscillation at 100-1000 kHz (wavelengths 300-3000 m).
- Key the transmitter by interrupting the power to the induction coil with a telegraph key (same Morse code). The spark produces a broad-band burst of RF energy heard as a loud buzz or crackle at the receiver. Range: 50-500 km depending on transmitter power (0.5-10 kW), antenna height, and propagation conditions.
- The spark gap transmitter radiates on many frequencies simultaneously (broadband). It interferes with all other nearby receivers. By the 1910s, this led to regulatory pressure to move to narrower-band transmissions.

**Crystal receiver**:
- No power required. An antenna wire (20-50 m long, as high as possible) picks up the radio signal. A tuned circuit (variable inductor and capacitor) selects the desired frequency. A crystal detector (galena lead sulfide crystal with a cat's-whisker wire contact, or carborundum with a bias voltage) acts as a diode, rectifying the RF signal to recover the audio envelope. High-impedance headphones (2000-4000 Ω) convert the audio to sound.
- Sensitivity: can detect signals from a 1 kW spark transmitter at 100-300 km. No amplification, so reception is limited by the headphone sensitivity and ambient noise. Crystal receivers are simple to build (the crystal detector is the only active component) and were widely used by amateurs and maritime stations.

**Antenna**: A vertical wire or mast radiator. For wavelengths around 600 m (500 kHz), an efficient quarter-wave antenna would be 150 m tall, which is impractical for most installations. Short antennas (20-50 m) work but with reduced efficiency. Ground the antenna system with buried copper wire radials (10-20 wires, each at least 0.1 wavelength long) to provide a low-resistance return path.

### Line Testing and Maintenance

**Testing instruments**:
- **Galvanometer**: A sensitive current detector (moving-coil or moving-magnet type). A mirror galvanometer can detect currents below 1 μA. For telegraph line testing, a milliammeter (0-100 mA range) suffices to verify that line current is above the 5 mA relay threshold.
- **Wheatstone bridge**: Measures unknown resistance by balancing two legs of a bridge circuit. Locate wire faults by measuring loop resistance from each end and comparing: fault distance = (R₁ / (R₁ + R₂)) × total line length, where R₁ and R₂ are the resistances measured from each end. For a 100 km line with a break at 40 km, the near end reads 40 × 40 = 1600 Ω and the far end reads 60 × 40 = 2400 Ω.
- **Earth testing**: Verify ground connection quality at each station. A good earth ground has <5 Ω resistance (measured with a three-point fall-of-potential test). Poor ground increases the circuit resistance and reduces the operating current. Improve grounds by burying copper plates (0.5 × 0.5 m) in moist soil, or surrounding the ground rod with charcoal and salt to reduce contact resistance.

**Routine maintenance**:
- Inspect pole line annually: check for rotted poles (push with a pike pole, replace if the base feels soft), leaning poles, broken insulators, loose guy wires, tree branches within 1 m of wires (vegetation clearance). Replace 5-10% of poles per year on a mature line.
- Retension wires that have sagged below specification (especially after heavy ice loading in winter). A slack wire whips in the wind, accelerating fatigue failure at the insulator attachment.
- Clean and re-adjust relay contacts monthly. Burned or pitted contacts increase resistance and cause missed signals. File contacts smooth with a points file (fine abrasive strip), then adjust gap to manufacturer specification.

### Telegraph in Practice

**Message formats**:
- Standard telegraph message structure: start mark → addressee (city, office, recipient name) → text → signature → end mark. Operators count words as they copy (billing is per word). A typical business message is 15-30 words. A stock quotation message might be 50-100 words.
- Prepaid vs. collect: prepaid messages are paid by the sender. Collect messages are paid by the recipient (similar to postage due). Government and press messages often have priority routing and reduced rates.
- Cipher and code books: commercial enterprises use code books (pre-arranged code words replacing common phrases) to reduce word count and cost. "SELL" might become "AXOLOTL" in the code book. This also provides rudimentary commercial confidentiality, since the code book is private.

**Transmission media comparison**:
- **Overhead wire**: cheapest per km, vulnerable to weather (ice loading, wind, lightning). Typical life: 15-25 years for iron wire, 25-40 years for copper. Most common telegraph medium for the first 50 years.
- **Underground cable**: insulated copper conductors buried in lead-sheathed cable. Protected from weather but 3-5× the cost per km. Vulnerable to digging damage and water ingress at splice points. Used in cities (overhead wires were considered unsightly) and for river crossings (submarine cable).
- **Submarine telegraph cable**: gutta-percha (natural latex from Palaquium gutta tree) insulation around copper conductor, armored with iron wire wrapping for mechanical protection. Laid on the ocean floor from a cable-laying ship. The first transatlantic cable (1858) was 3200 km. Signal attenuation: a transatlantic cable has ~2000 Ω resistance and ~0.5 μF capacitance, causing severe pulse distortion. Only 1-2 words per minute were possible on early submarine cables (vs. 20-30 WPM on land lines).

**Duplex telegraphy**: Sending two messages simultaneously in opposite directions on a single wire. Uses a differential relay and a balancing network (resistors and capacitors that simulate the impedance of the distant station's line). Each station's transmitter creates equal and opposite currents in the two halves of its relay coil, so the local transmitter does not activate the local receiver. Only the distant station's signal activates it. Doubles line capacity without adding wires.

**Quadruplex telegraphy**: Sending four messages on a single wire (two in each direction). Combines duplex operation with a polarized relay that responds to current direction (positive/negative) as well as current on/off. One message uses current polarity, the other uses current on/off, and both are independent. Invented by Edison in 1874. Quadruplex increased line revenue 4× without new construction, making long-distance telegraphy far more profitable.

### Safety & Hazards

- **Lightning**: Telegraph wires attract lightning strikes. Install lightning arresters (spark gaps to ground) at each station and at regular intervals along the line. Disconnect lines during electrical storms.
- **Electrocution**: Line voltages (10-200 V DC) can be lethal under wet conditions. Insulate all exposed contacts. Ground all equipment frames. Never touch wires during storms.
- **Battery acid**: Daniell cells contain sulfuric acid. Handle with care. Neutralize spills with baking soda. Eye wash station required at battery stations.
- **Strain injuries**: Telegraph operators develop repetitive strain injuries ("telegrapher's cramp") from hours of key manipulation. Ergonomic key design (light spring tension, proper wrist angle) reduces risk. Rotate operators.
- **RF burns**: Spark gap transmitters produce high-voltage RF at the antenna terminal. Never touch the antenna or feed line during transmission. RF burns are deep and slow to heal.
- **Spark gap fire hazard**: The spark gap operates in open air with continuous arcing. Keep flammable materials at least 2 m from the gap. Hydrogen gas from charging batteries accumulates at ceiling level. Ventilate battery rooms continuously. No open flames.
- **Acoustic trauma**: The sounder clicking at 20-40 words per minute for 8-12 hour shifts causes hearing damage over years of service. Sounders produce 70-85 dB peaks at the operator's ear position. Soundproof the receiving desk area with felt or cork padding. Provide ear plugs for long shifts.
- **Eye strain**: Copying Morse by ear under dim oil lamp or early electric light for extended periods causes eye fatigue and headaches. Provide adequate, shadow-free lighting at the receiving desk (minimum 200 lux at the message form surface).
- **Cadmium and mercury exposure**: Some relay contacts use cadmium or mercury for low-resistance switching. Cadmium oxide fumes from arcing contacts are toxic (inhalation causes pulmonary edema). Mercury relays release vapor at room temperature. Use in ventilated spaces. Replace mercury relays with dry-contact relays where possible.
- **Lead exposure**: Lead-sheathed underground cables present a lead exposure risk during splicing and repair. Workers handling lead sheathing should wash hands before eating. Lead accumulates in the body over time (chronic toxicity: neurological, renal, and hematological effects).
- **Cold weather operation**: Iron wire contracts in cold weather, increasing tension by 30-50% between summer and winter. Lines tensioned in summer may snap in winter cold snaps. In cold climates, set line tension in spring or autumn at 10-15% of breaking load, allowing margin for thermal contraction. Alternatively, use invar (iron-nickel alloy with near-zero thermal expansion) for critical spans. Invar (36% nickel) has a thermal expansion coefficient of 1.2 × 10⁻⁶/°C, versus 12 × 10⁻⁶/°C for iron.
- **Fire in telegraph offices**: Oil lamps for illumination, paper message forms stacked for filing, and wooden furniture create significant fire load. Telegraph offices have caused urban fires (the Great Chicago Fire of 1871 burned the telegraph office, cutting communications). Store message archives in fireproof vaults. Use metal desks and filing cabinets. Keep oil lamps away from paper. Install fire extinguishers (soda-acid type) at each operator position.
- **Animal hazards on pole lines**: Pole line construction crews work outdoors in all weather. Snake bites, insect stings, and large animal encounters are real risks in rural and wilderness line construction. Carry a first aid kit with antivenin protocols, tourniquets, and epinephrine for anaphylactic reactions to stings. Line crews typically work in pairs for this reason.
- **Repetitive message errors**: Under high-volume traffic (stock exchanges, news wires), operators copying at speed make character errors that distort meaning. A single misplaced dot can change "BUY" to "BUT" or "SEND" to "SOLD". Financial telegraph offices use a verification operator who reads back each message to the sending operator before transmission. Accuracy above 99.5% is the target; at 20 WPM, this means fewer than 1 error per 400 characters.

### Telegraph Economics and Social Impact

**Cost per word**: The first transatlantic telegraph cable (1866) charged $0.25-1.00 per word for a minimum 10-word message — a full day's wages for a laborer. By 1900, competition from multiple cable companies (Anglo-American, Commercial, Direct Spanish) drove the transatlantic rate down to $0.05 per word. Domestic US rates: Western Union charged $0.50-1.00 for a 10-word message between major cities in 1870, falling to $0.30 by 1900.

**Revenue**: Western Union's gross revenue was $7 million in 1866 (the year of the first successful transatlantic cable), growing to $50 million by 1900 and $100 million by 1929. The telegraph industry was one of the largest corporate enterprises of the 19th century. At its peak (1930s), Western Union transmitted over 200 million messages per year.

**Message volume**: US domestic telegraph traffic grew from approximately 20 million messages per year in 1870 to 60 million by 1890 and 80 million by 1900. The stock ticker (introduced 1867) alone consumed 30-40% of line capacity in financial centers, transmitting price quotations continuously during trading hours at 2-3 characters per second.

**Speed of information transformation**: Before the telegraph, transatlantic information traveled at ship speed — 10-14 days by fast sailing packet, 7-10 days by steamship. After the 1866 cable, the same information crossed in minutes. On land, news traveled at telegraph speed (~15 words per minute on a single line, multiplied by hundreds of parallel lines) versus courier or pony express speed (8-15 km/h, with relay stations every 15-25 km). The telegraph compressed information transit time by a factor of 10,000-100,000 for intercontinental communication.

### Limitations

- **Single-channel capacity**: A single telegraph wire carries one message at a time at 15-25 words per minute. Multiplexing (duplex, quadruplex) increases this to 4 channels max on one wire. High-traffic routes require many parallel wires.
- **Line maintenance**: Overhead wires break from ice loading, wind, tree falls, and vandalism. Underground cables are vulnerable to water ingress and excavation damage. A single break halts all traffic on that circuit.
- **No privacy**: Anyone with a tap on the wire can read the signal. Commercial cipher systems exist but add complexity and error risk.
- **Signal attenuation**: Long lines (>500 km) suffer signal degradation from resistance and capacitance. Requires relay (repeater) stations with batteries every 200-300 km, staffed 24/7.
- **No voice communication**: Telegraph transmits coded text only. No real-time voice, image, or data transmission. Operator skill required at both ends.
- **Infrastructure cost**: 100 km of single-wire telegraph line with poles requires ~2 tonnes of iron or copper wire, 500-1000 poles, and insulators. Mountainous or swampy terrain dramatically increases construction cost.

### See Also

- [Railways](railways.md) — Railway signaling and dispatch via telegraph
- [Electricity](../energy/electricity.md) — Electrical principles underlying telegraph systems
- [Roads & Bridges](roads.md) — Transport infrastructure parallels

*Part of the [Bootciv Tech Tree](../index.md) • [Transport](./index.md) • [All Domains](../index.md)*


