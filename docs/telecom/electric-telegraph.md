# Electrical Telegraph Networks

> **Node ID**: telecom.electric-telegraph
> **Domain**: [Telecommunications](./index.md)
> **Dependencies**: [`transport.telegraph`](../transport/telegraph.md), [`energy.electricity`](../energy/electricity.md), [`metals`](../metals/index.md)
> **Enables**: [`telecom.telephone`](telephone.md), [`telecom.submarine-cables`](submarine-cables.md)
> **Timeline**: Years 20-40
> **Outputs**: telegraph_networks, block_signaling_systems, message_routing

### Overview

This node covers the **network architecture** of electrical telegraph systems — how point-to-point telegraph circuits become information networks that route messages between cities, countries, and continents. For hardware details (telegraph keys, sounders, batteries, pole-line construction), see [Telegraph Communication](../transport/telegraph.md).

The key insight: a single telegraph wire between two stations is a communication channel. A network of wires connecting dozens of stations through central switching offices is an information infrastructure that transforms civilization's coordination speed by orders of magnitude.

### Network Topology

**Hub-and-spoke**: The dominant telegraph network architecture. A central office (hub) connects to multiple outstations (spokes) via dedicated wire pairs. Messages between outstations are routed through the hub, where an operator receives the incoming message and re-transmits it on the destination line.

- **Central office**: Houses the switchboard, battery bank, relay racks, and operator desks. A busy central office handles 20-100 lines simultaneously. Physical layout: switchboard in the center, operators arranged around it in a semicircle, each managing 2-4 lines.
- **Switchboard**: A manual patch panel connecting any incoming line to any outgoing line. Spring clips or plug-and-jack connections on copper bus bars. The operator inserts a patch cord to bridge the desired circuit pair. Early switchboards handled 20-50 lines; later designs managed 200+ lines.
- **Call indicator**: Each line has a galvanometer needle or small sounder that alerts the operator when a distant station starts transmitting. The operator hears the alert, identifies the line, and routes the message.

**Star network capacity**: A hub with *n* lines can theoretically route between any pair. Maximum simultaneous connections: *n*/2 (each connection uses 2 lines). A 50-line hub can carry 25 simultaneous conversations. In practice, not all stations transmit simultaneously, so the hub handles far more message traffic by time-sharing lines.

### Message Routing

**Direct routing**: If a dedicated wire exists between source and destination, the message travels directly. This is the fastest path — no relay delays.

**Relay routing**: If no direct wire exists, the message is routed through intermediate offices. Each relay point introduces 2-5 minutes of delay (operator receives, logs, re-transmits). A message crossing 3 relay points takes 6-15 minutes additional transit time beyond the electrical propagation time (negligible at ~280,000 km/s on wire).

**Routing table**: Each central office maintains a routing directory listing which destination offices are reachable via which outgoing lines. For complex networks with multiple possible paths, operators choose based on line availability and current congestion. Formal routing protocols did not exist until the teleprinter/telex era (1920s+).

### Multiplexing: Doubling and Quadrupling Line Capacity

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
- **Practical effect**: Quadruples line capacity. Revenue per wire increases 4×. Made long-distance telegraphy enormously profitable — Western Union's profits surged after deploying quadruplex on major routes.
- **Difficulty**: Maintaining balance on quadruplex circuits required skilled technicians. A 5% impedance mismatch caused crosstalk between channels. Regular maintenance every 4-8 hours was standard.

### Railway Block Signaling

The first automatic safety system enabled by telegraph technology. Block signaling prevents rear-end train collisions by ensuring that only one train occupies a given section (block) of track at a time.

**Principle**: The railway is divided into blocks (typically 2-5 km long). Each block has a signal post at its entrance and a telegraph circuit connecting it to adjacent block posts. A train entering a block triggers the block instrument to show "occupied" at both ends.

**Block instrument** (Tyers or Sykes type):
- A small telegraph instrument at each block post with three positions: **Line Clear** (green), **Line Blocked** (red), **Train on Line** (amber or special indicator).
- Electrically interlocked: the signalman at the exit end must acknowledge receipt before the entry end can clear the signal for the next train. This prevents one signalman's error from causing a collision.
- **Bell code**: Signalmen communicate via a single-stroke bell circuit. A prescribed sequence of bell rings (e.g., "2 rings = train approaching", "2-1 rings = train clear") standardizes communication between adjacent boxes. The bell code book for a busy line might define 20-30 distinct codes for different train types, routing instructions, and emergency conditions.

**Absolute block system** (UK standard after 1889):
- Only one train allowed in a block section at any time. The signalman must receive "train out of section" confirmation from the next block post before accepting a new train.
- Typical block post spacing: 2-3 km on busy lines, 5-10 km on rural lines. A 100 km route needs 20-50 block posts.
- Each block post requires a signalman (24/7 staffing on busy lines). Three shifts per post. A 50-block-post line requires 150 signalmen continuously.

**Technical parameters**:
- **Block circuit resistance**: 50-200 Ω total (wire + instruments). Battery: 2-6 V (2-4 Leclanché cells). Operating current: 10-30 mA. The block instrument relay pulls in at 5-10 mA.
- **Wire**: Single iron or copper wire on pole line alongside the track. Separate circuit for each block section. A 100 km double-track railway needs 200+ km of telegraph wire for block signaling alone.
- **Reliability**: The absolute block system reduced train collisions by 95% compared to time-interval signaling (where trains were spaced by time, not by confirmed track section clearance).

### Message Handling and Traffic Management

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
- Average delivery time: 30 minutes for same-city messages, 1-4 hours for cross-country, 10-30 minutes for transatlantic (after cable landing).

### Code Books and Compression

Commercial enterprises used pre-arranged **code books** to compress common phrases into single code words, reducing both cost and transmission time:

- A code book maps phrases to arbitrary code words. "SELL 100 SHARES AT MARKET PRICE" → "AXOLOTL" (one word instead of six).
- Code words were constructed to be pronounceable and distinguishable when heard over a sounder (avoiding similar-sounding pairs like "BIDEN" vs. "BIDET").
- **Security benefit**: Code books provided rudimentary commercial confidentiality. Without the code book, an intercepted message reads as nonsense code words.
- **Error risk**: A single misread dot could change "AXOLOTL" to a different code word, potentially inverting "BUY" to "SELL". Verification operators re-read critical messages before transmission.

### Telegraph Economics

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

### Telegraph and Social Transformation

**Speed compression**: Before the telegraph, information traveled at physical transport speed — 5-15 km/h by horse, 20-40 km/h by rail. After the telegraph, information traveled at ~280,000 km/s on wire (velocity factor ~0.93c for iron wire). For a 3,000 km distance, the telegraph compressed information transit from 3-5 days (rail) to instantaneous (~10 ms propagation delay). This 10,000× speedup transformed:
- **Financial markets**: Stock and commodity prices synchronized across cities in minutes rather than days. Arbitrage between markets became possible, but so did financial panic contagion.
- **Military coordination**: Troop movements, supply requests, and intelligence reports transmitted in hours rather than days. The telegraph was a decisive advantage in the American Civil War (1861-1865) — the Union's superior telegraph network enabled strategic coordination across a 3,000 km front.
- **News distribution**: The Associated Press (founded 1846) was created specifically to share telegraph costs among newspapers. A single correspondent in Washington could file a story read simultaneously by newspapers in New York, Boston, Philadelphia, and Chicago.
- **Railway operations**: Train orders transmitted by telegraph replaced time-interval scheduling, reducing head-on collisions by ~95%. The telegraph was essential to operating single-track railways safely at any useful frequency.

### Telegraph Line Maintenance

**Routine maintenance costs** (per 100 km of overhead line, annual):
- Pole inspection and 5-10% replacement: $500-1,000. Poles rot at the ground line; treated timber lasts 15-25 years but individual poles fail from insect damage, vehicle strikes, and wind loading.
- Wire retensioning (after ice storms, high winds): $200-500. Iron wire contracts in cold weather, increasing tension by 30-50%. Lines tensioned in summer may snap in winter.
- Insulator replacement (breakage, surface tracking): $100-300. Glass insulators crack from thermal shock (ice on one side, sun on the other). Surface contamination creates carbon tracks that leak current.
- Relay station battery replacement: $200-400/station. Daniell cells consume zinc electrodes; replace every 2-6 months.
- Lineman wages (1 lineman per 20-30 km): $1,000-1,500.
- **Total**: $2,000-4,000/year per 100 km (~5-10% of construction cost annually).

### Legacy and Successor Systems

The telegraph network established the infrastructure (pole lines, wire, right-of-way, operating companies) that the telephone later leveraged. When telephone service began in the 1870s, it used the same pole lines and often the same companies (Western Union briefly considered acquiring the telephone patent before deciding the technology was inferior to telegraph). The transition from telegraph to telephone dominance took ~40 years (1880-1920), with telegraph traffic peaking in the 1920s and declining thereafter as telephone service expanded.

**Teleprinter (telex) transition**: From 1930 onward, manual Morse code telegraphy was gradually replaced by teleprinters (electromechanical typewriters connected by wire). The teleprinter transmitted at 50-100 WPM automatically, eliminating the skilled operator bottleneck. Telex networks survived into the 1990s as a reliable backup to telephone for written business communication.

**Telegraph's lasting impact**: The telegraph established conventions still used in modern telecommunications: message addressing, routing tables, multiplexing, error detection (parity checks on teleprinter codes), and network management. The store-and-forward message relay model pioneered by telegraph hub offices is the direct ancestor of packet-switched data networks.

**Key dates in telegraph network evolution**:
- 1837: Cooke and Wheatstone demonstrate first commercial telegraph (London).
- 1844: Morse demonstrates Washington-Baltimore line (60 km). First US telegraph line.
- 1851: First submarine cable (Dover-Calais, 35 km). Cross-channel telegraph begins.
- 1861: First US transcontinental telegraph (3,200 km). Pony Express ceases operation 2 days later.
- 1866: First reliable transatlantic cable (3,200 km). Information crosses ocean in minutes, not weeks.
- 1874: Edison invents quadruplex. Quadruples line capacity overnight.
- 1915: AT&T opens first transcontinental telephone line, rendering telegraph obsolete for voice.

### See Also

- [Telegraph Communication](../transport/telegraph.md) — Hardware details: keys, sounders, batteries, pole-line construction, wire specifications
- [Telephone Systems](telephone.md) — The voice successor to telegraph networks
- [Submarine Cable Systems](submarine-cables.md) — Intercontinental telegraph connections
- [Railways](../transport/railways.md) — Railway infrastructure that telegraph block signaling protects

*Part of the [Bootciv Tech Tree](../index.md) • [Telecommunications](./index.md) • [All Domains](../index.md)*
