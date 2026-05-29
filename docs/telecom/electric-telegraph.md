# Electrical Telegraph Networks

> **Node ID**: telecom.electric-telegraph
> **Domain**: [Telecommunications](./index.md)
> **Dependencies**: [`energy.electricity`](../energy/electricity.md), [`metals`](../metals/index.md), [`telecom.pre-electric`](pre-electric.md), [`transport.telegraph`](../transport/telegraph.md)
> **Enables**: [`telecom.radio`](radio.md), [`telecom.submarine-cables`](submarine-cables.md), [`telecom.telephone`](telephone.md)
> **Timeline**: Years 20-40
> **Outputs**: telegraph_networks, block_signaling_systems, message_routing
> **Critical**: No — communication accelerates coordination but is not strictly required for survival

This node covers the **network architecture** of electrical telegraph systems — how point-to-point telegraph circuits become information networks that route messages between cities, countries, and continents. For hardware details (telegraph keys, sounders, batteries, pole-line construction), see [Telegraph Communication](../transport/telegraph.md).

The key insight: a single telegraph wire between two stations is a communication channel. A network of wires connecting dozens of stations through central switching offices is an information infrastructure that transforms civilization's coordination speed by orders of magnitude.

## Network Topology

**Hub-and-spoke**: The dominant telegraph network architecture. A central office (hub) connects to multiple outstations (spokes) via dedicated wire pairs. Messages between outstations are routed through the hub, where an operator receives the incoming message and re-transmits it on the destination line.

- **Central office**: Houses the switchboard, battery bank, relay racks, and operator desks. A busy central office handles 20-100 lines simultaneously. Physical layout: switchboard in the center, operators arranged around it in a semicircle, each managing 2-4 lines.
- **Switchboard**: A manual patch panel connecting any incoming line to any outgoing line. Spring clips or plug-and-jack connections on copper bus bars. The operator inserts a patch cord to bridge the desired circuit pair. Early switchboards handled 20-50 lines; later designs managed 200+ lines.
- **Call indicator**: Each line has a galvanometer needle or small sounder that alerts the operator when a distant station starts transmitting. The operator hears the alert, identifies the line, and routes the message.

**Star network capacity**: A hub with *n* lines can theoretically route between any pair. Maximum simultaneous connections: *n*/2 (each connection uses 2 lines). A 50-line hub can carry 25 simultaneous conversations. In practice, not all stations transmit simultaneously, so the hub handles far more message traffic by time-sharing lines.

## Message Routing

**Direct routing**: If a dedicated wire exists between source and destination, the message travels directly. This is the fastest path — no relay delays.

**Relay routing**: If no direct wire exists, the message is routed through intermediate offices. Each relay point introduces 2-5 minutes of delay (operator receives, logs, re-transmits). A message crossing 3 relay points takes 6-15 minutes additional transit time beyond the electrical propagation time (negligible at ~280,000 km/s on wire).

**Routing table**: Each central office maintains a routing directory listing which destination offices are reachable via which outgoing lines. For complex networks with multiple possible paths, operators choose based on line availability and current congestion. Formal routing protocols did not exist until the teleprinter/telex era (1920s+).

## Multiplexing: Doubling and Quadrupling Line Capacity

A single telegraph wire carries one message at a time. Multiplexing techniques allow multiple simultaneous messages on one wire, dramatically increasing line revenue without new construction.

**Duplex telegraphy** (two messages on one wire, one in each direction):
- Uses a **differential relay** and a **balancing network** (resistors and capacitors simulating the distant station's line impedance).
- Each station's transmitter creates equal and opposite currents in the two halves of its relay coil. The local transmitter's current cancels itself in the local receiver. Only the distant station's signal activates the local receiver.
- **Practical effect**: Doubles line capacity. A 50-line hub can now carry traffic equivalent to 100 single-channel lines. Revenue per wire doubles.
- **Balancing challenge**: The balancing network must closely match the actual line impedance, which varies with weather (wet insulators change the capacitance and leakage). Operators adjust the balance at the start of each shift and after rainstorms.

**Quadruplex telegraphy** (four messages on one wire, two in each direction):
- Combines duplex with a **polarized relay** that responds to current *direction* (positive/negative) as well as current *on/off*.
- Channel 1: current on/off (one message). Channel 2: current polarity reversal (second message). Both operate simultaneously and independently.
- Invented by Edison in 1874. Required more complex equipment (two relays per station, a polarity-reversing key, and precise balance).
- **Practical effect**: Quadruples line capacity. Revenue per wire increases 4x. Made long-distance telegraphy enormously profitable — Western Union's profits surged after deploying quadruplex on major routes.
- **Difficulty**: Maintaining balance on quadruplex circuits required skilled technicians. A 5% impedance mismatch caused crosstalk between channels. Regular maintenance every 4-8 hours was standard.

## Railway Block Signaling

The first automatic safety system enabled by telegraph technology. Block signaling prevents rear-end train collisions by ensuring that only one train occupies a given section (block) of track at a time.

**Principle**: The railway is divided into blocks (typically 2-5 km long). Each block has a signal post at its entrance and a telegraph circuit connecting it to adjacent block posts. A train entering a block triggers the block instrument to show "occupied" at both ends.

**Block instrument** (Tyers or Sykes type):
- A small telegraph instrument at each block post with three positions: **Line Clear** (green), **Line Blocked** (red), **Train on Line** (amber or special indicator).
- Electrically interlocked: the signalman at the exit end must acknowledge receipt before the entry end can clear the signal for the next train. This prevents one signalman's error from causing a collision.
- **Bell code**: Signalmen communicate via a single-stroke bell circuit. A prescribed sequence of bell rings (e.g., "2 rings = train approaching", "2-1 rings = train clear") standardizes communication between adjacent boxes.

**Absolute block system** (UK standard after 1889):
- Only one train allowed in a block section at any time. The signalman must receive "train out of section" confirmation from the next block post before accepting a new train.
- Typical block post spacing: 2-3 km on busy lines, 5-10 km on rural lines. A 100 km route needs 20-50 block posts.
- Each block post requires a signalman (24/7 staffing on busy lines). Three shifts per post. A 50-block-post line requires 150 signalmen continuously.

## Bill of Materials

## Overhead Pole Line (per km)

| Material | Quantity per km | Specification | Source |
|----------|----------------|---------------|--------|
| Telegraph wire (iron) | 80-120 kg | 3-4 mm diameter galvanized iron, tensile strength >350 MPa | [Metals](../metals/index.md) |
| Telegraph wire (copper) | 65-100 kg | 2.5-3.5 mm diameter hard-drawn copper | [Metals](../metals/index.md) |
| Poles (timber) | 12-20 | 7-9 m length, 15-20 cm top diameter, treated with creosote | [Forestry](../plants/index.md) |
| Insulators (glass) | 12-20 | Pin-type, 50-100 mm diameter, breakdown voltage >20 kV | [Glass](../glass/index.md) |
| Cross-arms (timber) | 6-10 | 1.0-1.5 m pine or oak, bolted to pole | [Forestry](../plants/index.md) |
| Pole hardware | 12-20 sets | Wrought iron brackets, bolts, pins | [Metals](../metals/index.md) |

## Central Office Equipment (50-line hub)

| Material | Quantity | Specification | Source |
|----------|----------|---------------|--------|
| Battery cells (Daniell) | 50-100 | Copper/zinc, 1.0-1.1 V each, 2-4 per line | [Metals](../metals/index.md) |
| Sounders/relays | 50-100 | Electromagnetic, 50-500 ohm coil resistance | [Metals](../metals/index.md) |
| Switchboard | 1 | 50-line manual patch panel, copper bus bars | [Metals](../metals/index.md) |
| Interior wiring | 2-5 km | 0.5-1.0 mm copper, insulated with gutta-percha or cotton | [Polymers](../polymers/index.md) |
| Patch cords | 50-100 | 1-2 m flexible cord with plug terminals | [Polymers](../polymers/index.md) |
| Zinc electrodes | 50-100 kg/year | Consumable, replaced every 2-6 months per cell | [Metals](../metals/index.md) |

## Quantitative Parameters

## Signal Propagation

| Parameter | Value | Notes |
|-----------|-------|-------|
| Propagation velocity | ~280,000 km/s | Velocity factor ~0.93c on iron wire |
| Operating current | 10-50 mA | Sufficient to activate sounder armature |
| Operating voltage | 2-12 V per station pair | Battery-powered; voltage drops with line resistance |
| Line resistance (iron wire) | 30-80 ohm/km | 3-4 mm diameter, varies with temperature and weather |
| Line resistance (copper wire) | 5-20 ohm/km | 2.5-3.5 mm diameter, preferred for long-distance |
| Insulation leakage (dry) | 10-50 Mohm-km | Wet weather reduces insulation resistance by 10-100x |
| Signaling speed (manual Morse) | 15-25 WPM | Trained operator; ~20 WPM sustained |
| Signaling speed (automatic) | 60-200 WPM | Paper tape punched off-line, transmitted mechanically |

## Multiplexing Capacity

| Technique | Channels per Wire | Equipment per Station | Revenue Multiplier |
|-----------|-------------------|----------------------|-------------------|
| Simplex (single) | 1 | Standard relay + key | 1x |
| Duplex | 2 | Differential relay + balance network | 2x |
| Quadruplex | 4 | 2 polarized relays + balance + polarity key | 4x |

## Block Signaling Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Block circuit resistance | 50-200 ohm | Wire + instruments total |
| Block battery voltage | 2-6 V | 2-4 Leclanche cells |
| Relay pull-in current | 5-10 mA | Minimum current to operate block instrument |
| Block post spacing (busy lines) | 2-3 km | Higher density for higher traffic |
| Block post spacing (rural lines) | 5-10 km | Lower traffic justifies wider spacing |
| Collision reduction | ~95% | Compared to time-interval signaling |

## Scaling Notes

## Local Network (10-50 km, single city)

A single central office with 10-30 lines covers a city and immediate surroundings. Construction: 1-3 months. Staff: 5-15 operators. Single-wire construction is adequate; copper preferred for reliability. Revenue: sufficient to cover operating costs at 50-200 messages/day. A 30 km overhead line costs $6,000-15,000 (1880s USD).

## Regional Network (100-500 km, connecting cities)

Multiple central offices connected by trunk lines carrying 1-4 channels (simplex to quadruplex). Relay stations at 50-100 km intervals. Construction: 6-18 months. Staff: 50-200 operators across all offices. Key constraint: trunk line construction cost ($200-500/km overhead). Quadruplex on trunk lines reduces per-message cost by 4x. A 300 km regional network with 5 offices costs $60,000-150,000.

## Continental Network (1,000-5,000 km)

Requires massive capital investment ($500,000-2,000,000 for a transcontinental network). Repeater stations every 200-400 km. Multiple trunk routes for redundancy. 24-hour staffing at all offices. Construction: 2-5 years with 500+ linemen. Key bottleneck: not wire or poles, but skilled operators and maintenance crews. The first US transcontinental telegraph (1861, 3,200 km) took 2 years to build with 50+ relay stations.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Signal too weak at receiver | Line resistance too high (wet insulators, corroded joints) | Test insulation resistance; clean or replace wet insulators; re-splice corroded joints |
| Intermittent signal dropouts | Wire sagging into tree or building | Inspect pole line for clearance; trim vegetation; retension wire |
| Duplex/quadruplex crosstalk | Balance network drifted (temperature, moisture) | Re-balance at start of shift and after rain; adjust resistance and capacitance to match line conditions |
| Complete circuit failure | Wire break (storm, fallen tree, vehicle) | Locate break by resistance measurement (resistance / ohm/km = distance); splice and insulate |
| Sounder chattering | Loose connections, corroded battery terminals | Clean contacts with abrasive cloth; tighten binding screws; replace degraded cells |
| Signal speed degradation | Operator fatigue, poor key adjustment | Adjust key spring tension (0.5-1.5 mm gap); rotate operators every 2-3 hours |
| Ground fault | Cracked insulator, wire touching cross-arm | Test with megger; isolate sections to locate faulted insulator; replace |
| Battery drain (excessive current) | Short circuit in wiring or instruments | Disconnect instruments one at a time to isolate; check insulation damage; replace faulty instrument |

## Safety Considerations

- **Electrical shock**: Battery banks (6-48 V DC) deliver a painful shock under wet conditions. Ringing current on party lines (75-100 V AC) can cause muscle contraction. Never touch bare wires with wet hands.
- **Battery chemicals**: Daniell cells contain copper sulfate solution; Leclanche cells contain ammonium chloride paste. Spills corrode metalwork and burn skin. Keep cells in drip trays. Handle electrolyte with rubber gloves and eye protection.
- **Pole climbing**: Linemen climb 7-9 m poles using spiked gaffs and body belts. Falls are the leading cause of lineman fatalities. Always use safety belt. Inspect poles for rot at ground line before climbing. Never climb in ice or winds >50 km/h.
- **Lightning**: Overhead wires attract lightning. Install lightning arresters (carbon block or spark gap) at each terminal and every 5-10 km. Ground arresters with copper wire to a driven ground rod (>3 m deep).
- **Wire tension**: Telegraph wire is tensioned to 50-200 kg force. A snapping wire whips with lethal force. Stand clear when retensioning. Never walk under wire being tensioned.
- **Fire**: Battery charging produces hydrogen gas. Relay racks generate heat. Keep CO2 or dry chemical extinguishers at all offices. Never use water on electrical fires.

## Message Handling and Economics

**Message format** (standardized across most networks):
```
-number-   [sequential message number]
ORIGIN     [city name]
DATE       [day month year]
TIME       [HH:MM filing time]
TO         [destination city + recipient]
TEXT       [message body, charged per word]
SIG        [sender's name or code]
```

**Billing**: Per word, distance-tiered. A 10-word message between cities 100 km apart might cost $0.25; between cities 1,000 km apart, $1.00. Government and press messages received priority routing and reduced rates (typically 50% discount).

**Traffic statistics** (US, 1900):
- Western Union transmitted ~63 million messages per year.
- Average message length: 15-20 words.
- Peak traffic: stock exchange hours (10 AM - 3 PM), when financial wires consumed 30-40% of line capacity.
- Average delivery time: 30 minutes for same-city, 1-4 hours cross-country, 10-30 minutes transatlantic.

## Code Books and Compression

Commercial enterprises used pre-arranged **code books** to compress common phrases into single code words, reducing both cost and transmission time:

- A code book maps phrases to arbitrary code words. "SELL 100 SHARES AT MARKET PRICE" becomes one word instead of six.
- Code words were constructed to be pronounceable and distinguishable when heard over a sounder (avoiding similar-sounding pairs).
- **Security benefit**: Code books provided rudimentary commercial confidentiality. Without the code book, an intercepted message reads as nonsense.
- **Error risk**: A single misread dot could change a code word, potentially inverting "BUY" to "SELL". Verification operators re-read critical messages before transmission.

## Telegraph Economics

**Construction costs** (approximate, 1880s US):
- Single-wire overhead line: $200-500 per km (poles, wire, insulators, labor).
- Underground cable (lead-sheathed): $1,000-3,000 per km.
- Central office with 50-line switchboard: $10,000-25,000.
- Relay station (unmanned): $500-1,000.

**Revenue** (Western Union, 1900):
- Gross revenue: ~$50 million/year.
- Average revenue per message: ~$0.75.
- Operating expenses: ~60% of revenue (labor was the largest cost — operators, linemen, clerks).
- Net profit margin: ~25-30%.

## Telegraph and Social Transformation

**Speed compression**: Before the telegraph, information traveled at physical transport speed — 5-15 km/h by horse, 20-40 km/h by rail. After the telegraph, information traveled at ~280,000 km/s on wire (velocity factor ~0.93c for iron wire). For a 3,000 km distance, the telegraph compressed information transit from 3-5 days (rail) to instantaneous (~10 ms propagation delay). This 10,000x speedup transformed:
- **Financial markets**: Stock and commodity prices synchronized across cities in minutes rather than days.
- **Military coordination**: Troop movements and intelligence transmitted in hours rather than days. The Union's telegraph network enabled strategic coordination across a 3,000 km front in the American Civil War.
- **News distribution**: The Associated Press (founded 1846) was created to share telegraph costs among newspapers.
- **Railway operations**: Train orders transmitted by telegraph replaced time-interval scheduling, reducing collisions by ~95%.

## Line Maintenance

**Routine maintenance costs** (per 100 km of overhead line, annual):
- Pole inspection and 5-10% replacement: $500-1,000. Poles rot at the ground line; treated timber lasts 15-25 years.
- Wire retensioning (after ice storms, high winds): $200-500. Iron wire contracts in cold weather, increasing tension by 30-50%.
- Insulator replacement (breakage, surface tracking): $100-300. Glass insulators crack from thermal shock.
- Relay station battery replacement: $200-400/station. Daniell cells consume zinc electrodes; replace every 2-6 months.
- Lineman wages (1 lineman per 20-30 km): $1,000-1,500.
- **Total**: $2,000-4,000/year per 100 km (~5-10% of construction cost annually).

## Legacy and Successor Systems

The telegraph network established the infrastructure (pole lines, wire, right-of-way, operating companies) that the telephone later leveraged. When telephone service began in the 1870s, it used the same pole lines and often the same companies. The transition from telegraph to telephone dominance took ~40 years (1880-1920), with telegraph traffic peaking in the 1920s and declining thereafter.

**Teleprinter (telex) transition**: From 1930 onward, manual Morse code telegraphy was gradually replaced by teleprinters (electromechanical typewriters connected by wire). The teleprinter transmitted at 50-100 WPM automatically, eliminating the skilled operator bottleneck. Telex networks survived into the 1990s.

**Key dates in telegraph network evolution**:
- 1837: Cooke and Wheatstone demonstrate first commercial telegraph (London).
- 1844: Morse demonstrates Washington-Baltimore line (60 km).
- 1851: First submarine cable (Dover-Calais, 35 km).
- 1861: First US transcontinental telegraph (3,200 km).
- 1866: First reliable transatlantic cable (3,200 km).
- 1874: Edison invents quadruplex.
- 1915: AT&T opens first transcontinental telephone line.

## See Also

- [Telegraph Communication](../transport/telegraph.md) — hardware details: keys, sounders, batteries, pole-line construction
- [Telephone Systems](telephone.md) — the voice successor to telegraph networks
- [Submarine Cable Systems](submarine-cables.md) — intercontinental telegraph connections
- [Railways](../transport/railways.md) — railway infrastructure that telegraph block signaling protects

[← Back to Telecommunications](index.md)
