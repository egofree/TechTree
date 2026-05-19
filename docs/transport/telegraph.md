# Telegraph Communication

> **Node ID**: transport.telegraph
> **Domain**: Transportation & Logistics
> **Timeline**: Years 15-30
> **Outputs**: telegraph_network

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

### Network Topology

**Hub-and-spoke**: Central station connects to multiple outstations. Switchboard (manual patch panel) connects any pair of lines. Message routing: operator receives message, re-transmits to destination line.

**Block signaling (railway integration)**: Telegraph circuits connect adjacent block posts on railway. Block instruments show line status (occupied/clear). Operator confirms train has cleared block before allowing next train entry. Prevents rear-end collisions — the first electrical safety system.

**Throughput**: 20-40 words/minute per line. For coordination of distant mining, manufacturing, and construction operations, this is transformative — decisions that took days by courier now take minutes.

### Safety & Hazards

- **Lightning**: Telegraph wires attract lightning strikes. Install lightning arresters (spark gaps to ground) at each station and at regular intervals along the line. Disconnect lines during electrical storms.
- **Electrocution**: Line voltages (10-200 V DC) can be lethal under wet conditions. Insulate all exposed contacts. Ground all equipment frames. Never touch wires during storms.
- **Battery acid**: Daniell cells contain sulfuric acid. Handle with care. Neutralize spills with baking soda. Eye wash station required at battery stations.
- **Strain injuries**: Telegraph operators develop repetitive strain injuries ("telegrapher's cramp") from hours of key manipulation. Ergonomic key design (light spring tension, proper wrist angle) reduces risk. Rotate operators.

*Part of the [Bootciv Tech Tree](../) • [Transport](./) • [All Domains](../)*
