# Electromechanical Computing

> **Node ID**: computing.electromechanical
> **Domain**: Computing & Automation
> **Timeline**: Years 30-50
> **Outputs**: automated_machines, punch_cards

### Automation & Control

**Cams and followers**:
- **Cam**: Rotating or sliding piece with shaped profile. **Follower**: lever or rod that moves in response to cam profile. Convert continuous rotary motion into complex, pre-programmed linear or oscillating motion.
- **Design**: Plot desired follower displacement vs. cam rotation angle. Transfer to cam blank. Cut profile with dividing head and milling machine. Harden cam surface (case-harden low-carbon steel — heat to 900°C, pack in charcoal, hold, quench).
- **Applications**: Automate machine tool cycles (feed, cut, retract, index), valve timing in engines, printing press coordination, textile machinery patterns. Each cam is a mechanical "program" — one revolution = one complete cycle.

**Linkages**:
- **Four-bar linkage**: Two rotating links (crank and follower), one connecting rod (coupler), and one fixed link (frame). Converts rotary motion to oscillating, or vice versa. Modify link lengths to change motion characteristics.
- **Slider-crank**: Crank + connecting rod + sliding piston. Converts rotary to linear (or vice versa). Used in every piston engine and pump.
- **Pantograph**: Linked parallelogram for scaling drawings. One tracing point follows original, cutting head produces scaled copy. Used for engraving maps, type, and decorative patterns. Ratio adjustable by changing pivot point.
- **Applications**: Convert motion between types (rotary ↔ linear ↔ oscillating), amplify force (lever principle), reproduce patterns at different scales, compute geometric relationships (mechanical analog computing).

**Governors**:
- **Centrifugal governor** (Watt governor): Two heavy balls on hinged arms rotate with engine shaft. As speed increases, centrifugal force swings balls outward → arms move collar downward → linkage reduces steam valve opening → engine slows. As speed decreases, balls fall inward → valve opens wider → engine speeds up. Equilibrium speed set by spring tension or weight adjustment.
- **Performance**: Maintains speed within ±2-5% of setpoint under varying load. Response time: 1-5 seconds. Essential for steam engines, water wheels, and any rotating machinery requiring constant speed.
- **Improved versions**: Porter governor (heavier central load for wider speed range), Proell governor (additional springs for faster response), Hartnell governor (spring-loaded for compact installation).

**Feedback control**:
- **Thermostat**: Bimetallic strip (brass + steel laminated strip — brass expands more than steel when heated, causing strip to bend). At set temperature, bent strip opens electrical contacts → heater off. As temperature drops, strip straightens → contacts close → heater on. Hysteresis: small gap between on and off temperatures (1-3°C). For furnaces, ovens, incubators.
- **Pressure regulator**: Spring-loaded diaphragm or piston. Downstream pressure pushes against spring. If pressure exceeds setpoint → valve closes. If below → valve opens. Maintains constant delivery pressure despite upstream fluctuations. For steam, compressed air, gas distribution.
- **Float valve**: Buoyant float on lever arm operates valve. Water level rises → float rises → valve closes inlet. Level drops → float drops → valve opens. Simple, reliable liquid level control for tanks, boilers, reservoirs.

### Integration with Manufacturing

**Cam-operated turret lathe**:
- **Turret**: Indexable tool holder (6-8 positions). Each position holds a different cutting tool (turning, facing, drilling, boring, threading, parting). Cam drum rotates → trip levers index turret → advance tool → cut → retract → index to next tool. Cycle repeats automatically. One operator can run 3-5 machines simultaneously.
- **Production rate**: 10-50 parts/hour depending on complexity. Each part identical to the last (within machine tolerance). This is the foundation of mass production — interchangeable parts by machine rather than hand fitting.

**Automatic screw machine**:
- Specialized for high-volume production of small turned parts (screws, bolts, shafts, pins). Bar stock fed through collet. Multiple cross-slides and turret tools operate in sequence under cam control. Cycle time: 5-30 seconds per part. Produces thousands of identical parts per day. THE machine that enabled the hardware industry.

**Pattern-following milling** (tracing):
- **Tracer mill**: Stylus follows a master template (wood, plaster, or metal pattern). Hydraulic or electrical linkage drives milling cutter to duplicate pattern in workpiece. Enables production of complex 3D shapes (dies, molds, turbine blades) without direct CNC capability. Accuracy: ±0.05-0.1 mm depending on tracer mechanism.

### Punch Card Systems

**Punch card** (for data and program storage):
- **Card**: Stiff paper card (187 × 83 mm, the "IBM card" or "Hollerith card"). 12 rows × 80 columns. Each column represents one character. Punch holes in specific row positions to encode data (numeric 0-9, or alphanumeric via zone punches in rows 0, 11, 12 combined with digit punches).
- **Card punch**: Keyboard-operated machine that punches holes in card. Operator types data → machine punches corresponding hole pattern.
- **Card reader**: Spring-loaded metal brushes or photoelectric sensors detect presence/absence of holes as card passes through reader. Converts hole pattern to electrical signals.
- **Tabulating machine**: Reads punch cards, counts, sorts, and accumulates data. Electromagnetic counters and relays perform basic arithmetic and logical operations. Herman Hollerith's 1890 census machine was the breakthrough — processed 1890 US census data in months vs. years.
- **Application**: Census data, inventory tracking, payroll, process recipes (encode process parameters on cards → feed into machine that controls cam timing), and later (Photolithography) as program input for early computers.

### Relay Logic & Switching

**Relay logic circuits**:
- **AND circuit**: Two relay coils in series (both must energize to complete circuit). Output on only when both inputs are active. Used for safety interlocks (e.g., door closed AND guard in place before machine starts).
- **OR circuit**: Two relay coils in parallel (either energizes output). Output on when any input is active. Used for alarm systems (any sensor triggers alert).
- **NOT circuit**: Normally-closed relay contact. When coil energizes, contact opens (output off). When coil de-energized, contact closed (output on). Inversion for alarm cutoffs, safety resets.
- **Latching relay**: Relay with second coil (or mechanical latch) that holds state after trigger pulse removed. Used for memory — the basis of sequential logic and early computer memory. One relay = one bit.

**Strowger switch** (telephone switching):
- **Design**: Two-motion selector — vertical (10 levels) then horizontal (10 positions) = 100-contact array per switch. Input pulse train from rotary dial: first digit selects vertical level, second digit selects horizontal position. Routes one telephone line to any of 100 destination lines automatically.
- **Application**: Automatic telephone exchanges eliminating human operators. Hundreds of Strowger switches per exchange, cascaded for multi-digit numbers (10,000 subscribers with 4-digit dialing). Electromechanical switching enabled communications networks before transistor electronics.

### Safety & Hazards

- **Moving machinery pinch points**: Relays, gears, cam followers, and Strowger switches have moving parts that can crush or amputate fingers. Install physical guards over exposed mechanisms. Use interlocks that disconnect power when guard panels are opened. Never reach into operating machinery.
- **High-voltage relay contacts**: Electromechanical relays switching inductive loads (motors, solenoids) produce arc flash across contact gaps — temperatures exceed 10,000°C at the arc root. Risk of electrocution and flash burns. Always disconnect and lock out power before servicing relay panels. Use insulated tools rated for the circuit voltage. Wear safety glasses when working near energized contacts.
- **Fire from relay contact arcing**: Repeated arcing at relay contacts generates metal vapors and carbon deposits that accumulate as combustible dust. Combined with the arc's ignition energy, this causes fires in relay cabinets. Keep relay panels clean and dust-free. Use arc suppressors (RC snubber circuits or diodes across inductive loads) to reduce arcing. Maintain smoke detection in equipment rooms.

*Part of the [Bootciv Tech Tree](../) • [Computing](./) • [All Domains](../)*

