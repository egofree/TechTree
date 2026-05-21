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

### Relay Computing Machines

**Konrad Zuse Z3** (1941, first working programmable computer):
- **Architecture**: 64 words of 22-bit floating-point memory (relays), arithmetic unit using relay logic, program on punched 35 mm film strip. Binary floating-point representation: 1 sign bit, 7 exponent bits, 14 mantissa bits.
- **Hardware**: ~2,000 relays total. Clock speed 4-5 Hz. Addition: 3 cycles (~0.7 seconds). Multiplication: 5 cycles (~3 seconds). Division: 6 cycles (~3.5 seconds).
- **Power**: ~4 kW. Physical size: roughly equivalent to a large wardrobe. The Z3 demonstrated that relay computing was practical, though relay speed limited performance.
- **Limitations**: Program was read-only (punched film), no conditional branching in the original design. Data input via keyboard, output via lamp display. Destroyed in 1943 Berlin bombing.

**Harvard Mark I** (IBM ASCC, 1944):
- **Scale**: 765,000 parts, 51 feet long, 8 feet tall. 3,500 relays plus mechanical counters and clutches. Weight: ~5 tonnes.
- **Number format**: 23-digit decimal numbers with sign. Stored in mechanical counter wheels (24 registers). 60 constants set by switch panel.
- **Performance**: Addition 0.3 seconds, multiplication 6 seconds, division 15.3 seconds, logarithm/sine ~1 minute. Five to ten times faster than a skilled human with a mechanical calculator.
- **Program**: 24-channel punched paper tape. Separate tape readers for instructions, constants, and data. No conditional branching natively, though later modifications added some conditional operation.
- **Reliability**: Several relay failures per day. Diagnostic routines ran before each computation. Maintenance staff on site during all operating hours.

**Relay specifications for computing**:
- **Contact arrangement**: DPDT (double-pole, double-throw) most common. Each relay provides two independent switchable contacts, usable for logic functions and signal routing.
- **Operate time**: 5-15 ms from coil energization to contact closure. Release time: 3-10 ms. These switching times limit maximum clock frequency to ~30-50 Hz with careful design.
- **Contact rating**: 2-10 A at 24-250 V AC or DC. Contacts rated for 10⁸-10⁹ operations at signal levels (dry circuit: <50 mA, <30 V). Contact life decreases dramatically at higher currents due to arcing.
- **Coil power**: 0.5-2 W per relay. A 2,000-relay computer draws 1-4 kW just for coil power, plus additional power for signal circuits.
- **Failure modes**: Contact sticking (welding from inrush current), contact corrosion (oxidation increases resistance), coil burnout (overheating), armature binding (mechanical wear). MTBF ~10⁷ operations per relay. A 2,000-relay machine expects a failure every few hours.

### Punch Card Tabulating Systems

**Hollerith tabulating machine** (1890 census):
- **Card format**: Original 1890 card: 24 columns × 12 rows. Punched holes represent data values. Later standardized to 80 columns × 12 rows (the "IBM card," 187 × 83 mm, 0.18 mm card stock).
- **Sensing**: Spring-loaded pins press against card. Where a hole exists, pin passes through, completes electrical circuit through mercury pool beneath. One pin per punch position, 80 pins per column set.
- **Counting**: Electromagnetic counters (one per category) increment when circuit completes. Sorter bin: card drops into the bin corresponding to the selected category. 80-column tabulator handles 100-200 cards per minute.
- **Sorting**: Separate sorting machine reads one column at a time, routes each card to one of 13 pockets (digits 0-9, two zone positions, and a reject pocket). Multi-column sort requires multiple passes.

### Electromagnetic Storage

**Magnetic drum memory**:
- **Construction**: Rotating cylinder (100-400 mm diameter, 200-600 mm long) coated with ferromagnetic material (iron oxide or nickel-cobalt alloy). Read/write heads mounted on adjustable arms, one per track, positioned 5-25 μm from drum surface. Rotation: 1,000-4,000 RPM (higher RPM = shorter access time but tighter mechanical tolerances).
- **Capacity**: 1,000-100,000 bits per drum. Track density: 5-50 tracks per cm. Bit density: 50-200 bits per cm along track. Early drums: a few KB. Late drums (1960s): up to several MB.
- **Access time**: 8-50 ms average (half-rotation at operating speed). Not random access — must wait for data to rotate under the read head. Predictable latency used for scheduling I/O operations.
- **Applications**: Main memory for early computers (IBM 650), swap storage, program storage in CNC machines. Replaced by magnetic core and then disk drives.

**Relay-based storage**:
- **Latching relay memory**: Each relay stores one bit. Set coil writes 1, reset coil writes 0. Contact state indicates stored value. Non-volatile (retains state without power). Used in: telephone exchanges (store routing digits), early calculators, process control systems.
- **Cost and scale**: A 1 KB relay memory requires 8,192 latching relays. At ~$5 per relay (1950s pricing), that is ~$40,000 for 1 KB. Impractical for large-scale memory, but adequate for registers and small buffers.

### Safety & Hazards

- **Moving machinery pinch points**: Relays, gears, cam followers, and Strowger switches have moving parts that can crush or amputate fingers. Install physical guards over exposed mechanisms. Use interlocks that disconnect power when guard panels are opened. Never reach into operating machinery.
- **High-voltage relay contacts**: Electromechanical relays switching inductive loads (motors, solenoids) produce arc flash across contact gaps — temperatures exceed 10,000°C at the arc root. Risk of electrocution and flash burns. Always disconnect and lock out power before servicing relay panels. Use insulated tools rated for the circuit voltage. Wear safety glasses when working near energized contacts.
- **Fire from relay contact arcing**: Repeated arcing at relay contacts generates metal vapors and carbon deposits that accumulate as combustible dust. Combined with the arc's ignition energy, this causes fires in relay cabinets. Keep relay panels clean and dust-free. Use arc suppressors (RC snubber circuits or diodes across inductive loads) to reduce arcing. Maintain smoke detection in equipment rooms.

### Electromagnetic Components

**Solenoids** (linear actuators):
- **Construction**: Cylindrical coil wound on a bobbin, with a soft iron plunger (armature) that slides freely in the bore. When current flows through the coil, magnetic field pulls the plunger into the coil center. Spring returns plunger when current stops.
- **Force**: Proportional to current squared and number of turns. Typical pull force: 5-500 N depending on size and current. Stroke length: 5-50 mm. Response time: 5-50 ms.
- **Applications**: Valve actuation (solenoid valves for pneumatic and hydraulic control), latch mechanisms, relay actuators, printer head firing pins, coin mechanisms.

**Stepper motors** (incremental rotation):
- **Principle**: Motor rotor moves in discrete angular steps in response to electrical pulses. Each pulse advances the rotor by a fixed angle (typically 1.8° or 7.5° per step, giving 200 or 48 steps per revolution). Position is determined by pulse count, without feedback sensors (open-loop control).
- **Drive circuitry**: Sequential energization of motor phases. For a 4-phase unipolar stepper: energize phases A, B, C, D in sequence for forward rotation; reverse sequence for backward. Half-stepping (energize two adjacent phases simultaneously) doubles angular resolution.
- **Applications**: Paper feed in printers, positioning tables, X-Y plotters, floppy disk drive head positioning, CNC machine tool axis control (early implementations). Maximum speed: 500-2000 steps/second (torque decreases at higher speeds due to inductance).

**Synchronous motors** (constant speed):
- **Principle**: AC motor whose rotor rotation is synchronized with the AC supply frequency. At 50 Hz supply, a 2-pole synchronous motor runs at exactly 3,000 RPM; at 60 Hz, 3,600 RPM. Speed does not vary with load (up to the pull-out torque limit).
- **Applications**: Clocks, timer mechanisms, chart recorders, phonograph turntables, telescopic drive motors. Any application requiring precise, constant speed tied to the power line frequency.

### Electromagnetic Power Control

**Motor starters and contactors**:
- **Contactor**: Heavy-duty electromagnetic switch rated for motor starting currents (5-8× full load current). Coil energizes → contacts close → motor starts. Coil de-energizes → contacts open (spring return). Rated by current capacity: 10-1,000 A.
- **Overload protection**: Thermal overload relay (bimetallic strip heated by motor current). If motor draws excessive current for too long, bimetallic strip bends and trips a mechanical latch that opens the contactor coil circuit, shutting down the motor. Protects motor from sustained overload without nuisance tripping on normal starting current surges.
- **Reversing starter**: Two contactors with electrical and mechanical interlocking. One contactor applies forward phase sequence; the other reverses two phases, reversing a 3-phase motor. Interlock prevents both contactors from closing simultaneously (which would create a line-to-line short circuit).

### Electromagnetic Instruments

**Moving-coil meter (D'Arsonval movement)**:
- **Principle**: Coil of fine wire suspended in the field of a permanent magnet. Current through the coil creates a magnetic field that interacts with the permanent field, producing torque. A spiral spring provides restoring torque proportional to deflection angle. At equilibrium, pointer deflection is proportional to current.
- **Sensitivity**: Typical full-scale deflection at 50 μA (for voltmeter applications) or 1 mA (for general-purpose meters). Internal resistance: 50-500 Ω for 1 mA movement. Higher sensitivity movements use stronger magnets and more coil turns but are more fragile.
- **Multimeter construction**: The basic movement is adapted for multiple ranges using shunt resistors (for current measurement, bypass most current around the movement) and series resistors (for voltage measurement, limit current through the movement). Rotary switch selects the range. A rectifier bridge converts AC to DC for AC measurement.
- **Accuracy**: ±1-3% of full scale for analog meters. Calibration against a standard cell (Weston cadmium cell: 1.01864V at 20°C) ensures traceability.

**Watt-hour meter** (energy measurement):
- **Principle**: Small induction motor whose speed is proportional to power (voltage × current). Voltage coil creates flux proportional to line voltage. Current coil creates flux proportional to load current. The interaction of these fluxes with the aluminum disc rotor produces torque proportional to power. Permanent magnet provides braking torque proportional to speed. At equilibrium, disc speed is proportional to power, and total revolutions are proportional to energy consumed.
- **Register**: Gear train from the disc shaft drives odometer-type registers displaying kilowatt-hours. The gear ratio (disc revolutions per kWh) is the meter constant, typically labeled on the meter nameplate (e.g., Kh = 7.2 watt-hours per revolution).
- **Calibration**: Adjust by changing the strength of the braking magnet (screws that shift the magnet position relative to the disc). Test with known load (standard resistor and voltage source). Accuracy: ±1-2% over the rated load range.

### Magnetic Recording

**Wire recording** (early audio and data storage):
- **Principle**: Steel wire (0.1-0.25 mm diameter) passes over an electromagnet (recording head). Audio signal drives the electromagnet, magnetizing the wire in a pattern corresponding to the signal waveform. Playback: wire passes over a similar head, and the varying magnetic field induces a voltage proportional to the recorded signal.
- **Specifications**: Wire speed: 0.6-2.4 m/s. Recording time: 30-120 minutes per reel. Frequency response: 100-5000 Hz (adequate for speech, marginal for music). Wire must withstand transport tension without breaking.
- **Data storage**: Binary data recorded on magnetic wire as magnetization pulses. Storage density: ~100 bits per cm. Used in early flight data recorders and industrial data logging.

**Early magnetic tape**:
- **Paper-based tape**: Paper strip (6-12 mm wide) coated with iron oxide powder in a cellulose binder. Coating process: mix Fe₃O₄ powder (~0.5 μm particle size) with binder, coat onto paper, dry, calender for smooth surface. Coercivity: 200-400 Oe. The simplest magnetic recording medium.
- **Plastic-based tape**: Cellulose acetate or PVC backing with gamma-Fe₂O₃ coating. Superior to paper in strength and uniformity. Tape width: 6.35 mm (¼ inch) for audio, 12.7 mm (½ inch) for instrumentation. The basis of the recording industry from ~1950 onward.

### Telegraph and Teletype Systems

**Telegraph relay**:
- **Function**: Amplify weak telegraph signals over long distances. A small current in the incoming line coil operates a sensitive relay, which closes a contact carrying a stronger local current to drive the next line segment or a sounder. Repeaters every 100-300 km extend telegraph lines across continents.
- **Sensitivity**: Polarized relays (with permanent magnet bias) respond to currents as low as 0.1-1 mA. Neutral relays (no bias) require 5-20 mA. The incoming signal polarity (mark/space) drives the armature between two contacts.

**Teletype communication protocol**:
- **Baudot code** (5-bit): 32 characters. Two shift states (letters shift and figures shift) double the effective character set to ~60. Each character: 1 start bit (space), 5 data bits, 1.42 stop bits (mark). At 45.5 baud (standard teletype speed), one character takes 163 ms (6 characters/second). Synchronous motor drives both sender and receiver at the same speed.
- **ASCII code** (7-bit, later standard): 128 characters including uppercase, lowercase, digits, punctuation, and control codes. 8-bit transmission with parity. Used in later teletypes and all computer terminals.

### Detailed Relay Computing Specifications

**DPDT relay characteristics**:
- **Contact configuration**: Double-pole, double-throw (2 form-C contacts per relay). Each pole has a common (C), normally-open (NO), and normally-closed (NC) terminal. Both poles switch simultaneously when the coil energizes. Provides two independent signal paths per relay.
- **Coil parameters**: Resistance 500-5,000 Ω for typical 24-48 VDC computing relays. Operate current: 5-50 mA. Power dissipation: 0.25-2 W per coil. Continuous duty rated (designed for indefinite energization without overheating).
- **Timing**: Operate time 5-15 ms (coil energized to contact closure). Release time 3-10 ms (coil de-energized to contact opening). The operate/release asymmetry arises because the armature has mechanical inertia and the magnetic field collapses gradually. Maximum practical clock frequency: 30-50 Hz with careful design, limited by the slowest relay in the circuit.
- **Contact rating**: 2 A at 24 VDC for signal switching. Mechanical life: 10⁷ operations minimum. At 10 Hz operation, that is roughly 12 days of continuous switching before expected failure of a single relay. A machine with 2,000 relays experiences a failure every few hours.
- **Arc suppression**: Diodes across coils (reverse-biased during normal operation) suppress the inductive kick when the coil de-energizes. Without suppression, the coil's back-EMF can reach 10× the supply voltage, arcing across switch contacts and degrading them rapidly.

**Relay binary adder**:
- **Full adder circuit**: 2 relays per bit position implement the sum and carry functions. Sum = A XOR B XOR Cin (three relays if counting XOR implementation separately, but compact designs reuse the carry relay for one XOR term). Carry = (A AND B) OR (Cin AND (A XOR B)). Each relay adds ~10 ms propagation delay. An 8-bit ripple-carry adder accumulates 80-240 ms of carry propagation, since each bit must wait for the previous carry to settle.
- **Shift register**: 2 relays per bit (one holds current state, one accepts next state). A clock pulse (generated by a motor-driven cam or a free-running relay oscillator at 5-10 Hz) simultaneously transfers all bits one position. An 8-bit shift register needs 16 relays and shifts at 5-10 Hz.
- **Latching relay memory**: One bit per relay. The latching relay has two stable positions, held by a magnetic or mechanical latch. A "set" pulse writes 1, a "reset" pulse writes 0. No power needed to maintain state (non-volatile). Reading: apply a small sense current through the contacts. Cost scales linearly: 1 KB = 8,192 relays, prohibitively expensive for large memory.

**IBM 80-column punch card system**:
- **Card specifications**: 187.3 × 83.3 mm, 0.18 mm card stock. 12 rows × 80 columns = 960 punch positions per card. Rows numbered 12, 11, 0, 1-9 (top to bottom). Numeric encoding: one punch per column in rows 0-9. Alphabetic: zone punch (row 12, 11, or 0) plus one digit punch. Special characters: two or three punches per column. Maximum information density: ~960 bits per card, though typical data encoding uses fewer.
- **Keypunch** (IBM 029, standard model): Operator types on keyboard, machine punches holes at 10 characters per second. Each keystroke punches one column and advances to the next. Verification mode: a second operator re-keys the same data, and the machine compares punches to keystrokes without punching, flagging mismatches.
- **Sorter** (IBM 082): Reads one selected column per pass. Drops each card into one of 13 pockets (digits 0-9, zones 11/12, reject). Throughput: 450 cards per minute. Multi-digit sorting requires one pass per digit position, sorting least significant digit first. Sorting 10,000 cards on a 5-digit field: 5 passes × 22 minutes per pass ≈ 2 hours.
- **Tabulator** (IBM 407): Reads cards at 150 per minute. Performs addition and subtraction on up to 20 counters (each up to 8 digits). Prints one line per card or per control group, with selective printing based on punch patterns. Program control via removable wiring panel (plugboard) that defines which columns feed which counters and when printing occurs.

**Harvard Mark I operating detail**:
- **Physical scale**: 765,000 parts, 51 feet (15.5 m) long, 8 feet (2.4 m) tall, weighed approximately 10,000 lb (4,500 kg). 530 miles of wire connected 3,500 relays. The machine occupied most of a large room.
- **Number storage**: 23-digit decimal numbers with sign. Stored in 60 sets of 24-position mechanical switches (constant storage, set by hand). Working registers: 72 adding storage units (mechanical counter wheels, each holding a 23-digit number). The switch-set constants could be changed during setup but not during program execution.
- **Computation timing**: Addition: 0.3 seconds (three 0.1-second machine cycles). Multiplication: 6 seconds. Division: 15.3 seconds. Logarithm: 71.4 seconds. Sine: ~60 seconds. Compared to a human with a mechanical calculator, Mark I was 5-10× faster on addition and 3-5× faster on multiplication.
- **Programming**: 24-channel punched paper tape. Three separate tape readers ran simultaneously: one for instructions, one for constants, one for data output formatting. Each instruction occupied one line of tape specifying the operation code, source register, and destination register. No conditional branching in the original design. Programs were strictly sequential, looping achieved by splicing the tape into a physical loop.

**Strowger switch exchange architecture**:
- **2-motion selector**: A wiper arm moves vertically to one of 10 levels (bank), then horizontally across one of 10 positions at that level. Each position is a set of contacts (typically 3-wire: tip, ring, and control). Total contacts per switch: 100. The selector steps vertically under pulse control from the first dialed digit, then horizontally under the second digit.
- **Exchange sizing**: A 1,000-line exchange uses 100 two-motion selectors (10 groups of 10). Each subscriber line connects to a line finder (which hunts for an idle selector when the subscriber lifts the handset). The selector then receives dialed pulses and routes the call. For 10,000 subscribers, add a second selector stage: first two digits route through a "group selector" to one of 100 final selectors, last two digits select the line. Switching time: 2-5 seconds per digit.
- **Mechanical life**: Each selector performs millions of stepping operations. Contact wear and wiper alignment drift require periodic maintenance. A 10,000-line exchange contains roughly 200-400 selectors and requires full-time maintenance staff.

---

*Part of the [Bootciv Tech Tree](../) • [Computing](./) • [All Domains](../)*

