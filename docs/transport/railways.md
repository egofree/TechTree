# Railways

> **Node ID**: transport.railways
> **Domain**: Transportation & Logistics
> **Timeline**: Years 20-50+
> **Outputs**: railways

### Railways

**Track construction**:
- **Subgrade**: Graded and compacted earth foundation. Ballast: crushed stone (10-15 cm layer) for drainage and load distribution.
- **Rails**: Initially iron straps on wooden stringers (strap rail — iron bar 2.5-5 cm wide × 1-1.5 cm thick nailed to timber). By the Energy stage: wrought iron or steel T-rails (inverted-T cross section, 15-30 kg/m, rolled in iron rolling mill). Rail length: 5-10 m sections, joined by fish plates (steel plates bolted through rail web holes).
- **Gauge**: Standard gauge 1435 mm (4 ft 8½ in). Standardize early — different gauges prevent network interoperability. This specific gauge is the global standard derived from Roman chariot wheel spacing.
- **Sleepers (ties)**: Timber (treated with creosote or tar), 2.4-2.7 m long × 20-25 cm wide × 12-15 cm thick. Spaced every 0.6-0.8 m. Rails spiked to sleepers with cut spikes (L-shaped iron spikes driven into wood).
- **Grade**: Maximum 2-3% for steam locomotives. Minimum curve radius 150-300 m. Gentle grades and curves = lower fuel consumption, higher speed, less wear.

**Steam locomotive** (Energy):
- **Boiler**: Fire-tube boiler (fire tubes carry hot gas through water space). Pressure 0.7-1.5 MPa. Diameter 1-1.5 m, length 3-5 m. 50-200 fire tubes, 5 cm diameter each. Coal-fired firebox at one end, smokebox and chimney at other. Steam dome on top for dry steam collection.
- **Cylinders**: 2 cylinders, 30-50 cm bore, 40-60 cm stroke. Steam admitted alternately on each side of piston (double-acting). Slide valve or piston valve, actuated by Stephenson valve gear (link motion — adjustable cutoff for steam economy). Operating pressure: 0.7-1.0 MPa.
- **Power**: 50-200 HP. Speed: 30-80 km/h. Tractive effort: 2000-10000 kgf. Haul 50-200 tonnes on level track.
- **Driving wheels**: 4-8 driven wheels (coupled by connecting rods). Leading and trailing trucks (unpowered wheels) for stability.

### Telegraph Communication

**Principles**:
- Electrical current through wire → electromagnetic effect at receiver. Encode information as sequences of current on/off (binary code — Morse code: dots and dashes represent letters and numbers).
- **Circuit**: Battery (or generator) → telegraph key (switch) → transmission wire → sounder (electromagnet + armature) → ground return (earth completes circuit — single wire sufficient for most installations).

**Telegraph key**:
- Spring-loaded lever with electrical contacts. Press lever → contacts close → current flows → remote sounder clicks. Release → spring opens contacts → sounder clacks. "Dot" = short press (~0.1 s). "Dash" = long press (~0.3 s). Pause between elements ~0.1 s, between letters ~0.3 s, between words ~0.7 s.

**Sounder**:
- Electromagnet (iron core with many turns of fine copper wire — 5-20 Ω resistance). Armature (iron bar) held above electromagnet core by spring. When current flows → electromagnet pulls armature down → "click" sound. When current stops → spring pulls armature up → "clack" sound. Operator listens to click-clack pattern and translates to letters. Trained operators achieve 20-40 words per minute.

**Wire and line construction**:
- **Wire**: Iron or copper wire, 2-4 mm diameter. Iron stronger (less sag between poles) but higher resistance (poor conductor). Copper better conductor but requires more support. Galvanized iron wire (zinc-coated for corrosion resistance) common compromise. Resistance: ~10-50 Ω/km depending on wire gauge.
- **Poles**: Wooden poles (treated timber, 6-10 m tall), spaced 40-60 m apart. Wire attached via glass or ceramic insulators (prevents current leakage through wet pole). Single wire on cross-arm. Ground wire at each station.
- **Range**: Direct current from batteries effective to ~50-100 km (voltage drop in wire limits range). For longer distances: relay stations every 50-100 km (incoming signal activates relay → re-transmits on fresh battery to next station). Or use higher voltage (100-200V from generator). Transcontinental telegraph: ~5000 km with ~50-100 relay stations.

**Battery for telegraph**:
- **Daniell cell**: Copper electrode in CuSO₄ solution | unglazed porcelain separator | zinc electrode in ZnSO₄ or dilute H₂SO₄ solution. Voltage: 1.1V per cell. Stack 10-50 cells in series for desired line voltage (10-50V). Stable output, long life. Or use DC generator for higher voltage.

**Morse code** (standardized):
```
A .-    B -...  C -.-.  D -..   E .     F ..-.  G --.   H ....
I ..    J .---  K -.-   L .-..  M --    N -.    O ---   P .--.
Q --.-  R .-.   S ...   T -     U ..-   V ...-  W .--   X -..-
Y -.--  Z --..
0 -----  1 .----  2 ..---  3 ...--  4 ....-  5 .....
6 -....  7 --...  8 ---..  9 ----.
```

**Telegraph network**:
- Hub-and-spoke topology: Central station connects to multiple outstations. Switchboard (manual patch panel) connects any pair of lines. Message routing: operator receives message, re-transmits to destination line.
- **Throughput**: 20-40 words/minute per line. For coordination of distant mining, manufacturing, and construction operations, this is transformative — decisions that took days by courier now take minutes.

### Logistics Management

**Standardized containers**:
- Wooden crates in standard sizes (0.5 m³, 1.0 m³, 2.0 m³). Stackable. Labeled with contents, weight, destination, handling instructions. Enables efficient loading of carts, wagons, rail cars.

**Inventory management**:
- **Ledger system**: Double-entry bookkeeping. Track all materials in, out, and on hand. Perpetual inventory (update with every transaction). Periodic physical count to verify ledger accuracy.
- **Reorder points**: Minimum stock levels for critical materials. When stock falls below reorder point → trigger procurement. Prevents stockouts that halt production.
- **Buffer stocks**: Maintain 2-4 weeks of critical materials (coal, iron, copper, chemicals). Protects against supply disruption.

**Warehouse design**:
- Dry, well-ventilated building. Organized by material type. Heavy materials on ground floor (structural load). Flammables in separate fireproof building. Chemicals in ventilated, bunded (liquid-tight containment) area. Shelving for small items. Open floor for bulk materials. Loading dock for vehicle access. Inventory control at entry/exit.

### Signaling & Rolling Stock

**Railway signaling**:
- **Semaphore signals**: Blade (arm) pivoted on mast. Horizontal = stop (danger). Angled down 45° = proceed (clear). Night indication: red lamp (stop), green lamp (clear). Operated by wire pull from signal box (lever frame). Visible 300-500 m in daylight.
- **Block system**: Divide track into blocks (1-3 km sections). Only one train permitted in each block at a time. Block instruments (telegraph-based) at each block post — operator confirms train has cleared before allowing next entry. Prevents rear-end collisions. Absolute block: next train must wait for clear signal. Permissive block: following train may enter at restricted speed (lower capacity, used on lightly trafficked lines).
- **Interlocking**: Mechanical linkage between signals and points (switches) in lever frame. Prevents conflicting routes — operator physically cannot pull lever to set conflicting signal/point combination. Crush prevention built into the mechanism. Essential for junction safety.

**Freight and passenger car design**:
- **Flat car**: Simple wooden or steel deck on bogie (truck) frame. 10-20 tonne capacity. For timber, machinery, vehicles. Stake pockets for load securing.
- **Box car**: Enclosed wooden or steel body, sliding door. 15-30 tonne capacity. For bagged grain, manufactured goods, anything needing weather protection.
- **Tank car**: Cylindrical tank on frame. For liquids (water, oil, chemicals). Fill dome on top, drain valve at bottom. 15-30 m³ capacity.
- **Passenger coach**: Wooden or steel body with bench or individual seating. Sprung suspension (leaf springs or elliptic springs on bogies). 40-80 passengers per coach. Oil lamp lighting (later electric). Hardy vacuum or air brake system continuous through train — brake applies automatically if train parts or air pressure is lost.

### Safety & Hazards

- **Boiler explosions**: Steam locomotive boilers can explode from low water, overpressure, or corrosion. Two safety valves, water gauge, regular inspection required.
- **Runaway trains**: Brake failure on gradients. Dead-man's control. Fail-safe brakes.
- **Coupling injuries**: Manual coupling crushes fingers. Use coupler bars. Never stand between cars on grade.
- **Derailment**: Speed, track condition, broken rails. Regular inspection. Speed limits.

*Part of the [Bootciv Tech Tree](../) • [Transport](./) • [All Domains](../)*

