# Material Transport

> **Node ID**: automation.material-transport
> **Domain**: [Automation & Robotics](./index.md)
> **Dependencies**: [`automation.equipment-communication`](equipment-communication.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 60-100+
> **Outputs**: foup_transport, agv_systems, overhead_hoist_transport, fab_logistics

## Problem

A 300 mm semiconductor fab processes 40,000-100,000 wafers per month. Each wafer visits 400-700 process steps across dozens of different tools. At any moment, thousands of FOUPs (each holding 25 wafers) must move between stockers (storage), process tools, and inspection stations. A single mis-delivered or delayed FOUP can idle a $20 million tool. Automated material transport is the logistics backbone that keeps the fab running at peak throughput.

## Decision Framework: Transport System Selection

| Scenario | Recommended System | Rationale |
|----------|-------------------|-----------|
| 300 mm high-volume fab (>30K wafers/month) | OHT primary + AGV supplement | OHT provides speed (1.5-2.0 m/s), zero floor space; AGVs handle overflow and special routes |
| 200 mm fab with manual/semi-auto operation | AGV with magnetic tape guidance | Lower installation cost, flexible routing, compatible with existing floor layout |
| High-throughput interbay transfer (>200 FOUPs/hr) | RGV on dedicated rails | Fastest transport (up to 5.0 m/s), highest throughput per vehicle |
| Development or low-volume fab | Manual transport with push carts | Lowest cost, maximum flexibility, acceptable when throughput is not critical |
| Mixed 200/300 mm fab | OHT for 300 mm bay + AGV for 200 mm bay | Each bay uses appropriate automation level for its wafer size |

### Implementation Steps

1. **Map material flow**: Analyze process flow to determine interbay and intrabay transport volumes, peak demand times, and delivery time requirements
2. **Design track layout**: Plan OHT rail network (or AGV paths) with stocker placement at bay boundaries. Minimize distance between high-traffic tool pairs
3. **Size the vehicle fleet**: Calculate required vehicles based on throughput targets (target 60-80% utilization). Include spares for maintenance
4. **Deploy stocker systems**: Install stockers at interbay transfer points with capacity for 4-8 hours of WIP buffer
5. **Integrate with MES**: Configure [Equipment Communication](equipment-communication.md) for FOUP RFID tracking, transport request dispatch, and delivery confirmation
6. **Commission and tune**: Run production simulations, adjust dispatch algorithms, optimize traffic management zones. Allow 3-6 months for system tuning

### Transport System Trade-offs

| Parameter | OHT | Floor AGV | RGV |
|-----------|-----|-----------|-----|
| Transport speed (avg) | 1.5-2.0 m/s | 0.3-0.8 m/s | 2.5-3.5 m/s |
| FOUP delivery time | 1-4 min | 3-8 min | 1-3 min |
| Floor space consumed | None (overhead) | 1.2 m aisle width | Flush rail in floor |
| Installation cost | High (rail infrastructure) | Low (tape/markers) | Medium (rail installation) |
| Route flexibility | Low (fixed rails) | Moderate (re-tape floor) | None (fixed rails) |
| Maintenance access | Difficult (overhead work) | Easy (floor level) | Medium (floor rails) |
| Throughput per vehicle | 15-25 FOUP/hr | 6-12 FOUP/hr | 20-40 FOUP/hr |

## FOUP (Front-Opening Unified Pod)

### Design Standards

The FOUP is the standardized wafer carrier for 300 mm fabs, defined by SEMI E1.9 and related standards.

**Physical specifications**:
- **External dimensions**: 475 mm (W) × 375 mm (D) × 215 mm (H), ±2 mm. Designed to fit standardized load ports.
- **Internal capacity**: 25 wafer slots, 10 mm pitch (center-to-center distance between slots). Usable wafer thickness: 0.5-1.0 mm.
- **Weight**: Empty FOUP: 3.5-4.5 kg. Fully loaded (25 × 300 mm wafers): 7.5-9.0 kg. Must be liftable by AGV, OHT, and human operator (under 10 kg ergonomic limit for occasional manual handling).
- **Materials**: Housing: polycarbonate (PC) or polyetheretherketone (PEEK) for chemical resistance, low particle generation, and dimensional stability. Internal wafer supports: PEEK or PTFE. No metal exposed to wafer environment (metallic contamination destroys device yield).
- **Cleanliness**: FOUP interior must maintain ISO Class 1 (≤1 particle ≥0.1 μm per cubic foot) during transport. Particle generation from door opening/closing: <50 particles ≥0.14 μm per cycle.

**Door mechanism**:
- **Front-opening interface pod (FOP)**: FOUP has a front door that opens downward (hinged at bottom edge). The load port on the process tool unlatches the door automatically and lowers it, exposing the wafer slots to the tool's mini-environment.
- **Door seal**: Peripheral gasket (silicone or fluorosilicone rubber) seals the door when closed. Gasket compression: 10-20% of original height to ensure hermetic seal without excessive force.
- **Interlock**: Mechanical interlock prevents door opening unless the FOUP is properly seated on a load port. Prevents accidental wafer exposure to uncontrolled environment.

**RFID tag**:
- **SEMI E142 standard**: Each FOUP carries a passive RFID tag (13.56 MHz, ISO 15693) embedded in the housing. Tag stores: FOUP serial number, lot ID (written by MES), wafer count, last process step, and cleanroom status.
- **Read range**: 100-300 mm from RFID reader antenna. Readers mounted at load ports, stockers, AGVs, and OHT pick points read the tag automatically.
- **Data capacity**: 256 bytes to 2 KB depending on tag model. Read/write time: <100 ms.

### FOUP Handling Requirements

- **Acceleration limits**: Maximum 0.5 g (4.9 m/s²) during transport to prevent wafer sliding within slots. Higher acceleration causes wafers to shift, risking contact with slot walls (particle generation) or adjacent wafers (scratching).
- **Vibration limits**: 0.1 g RMS maximum in the 10-500 Hz frequency range during transport. Vibration causes wafer micro-motion against support structures, generating particles.
- **Orientation**: FOUP must remain upright (wafer slots horizontal) at all times. Tilting beyond ±10° risks wafers sliding out of slots. Never invert — wafers fall out.
- **Temperature**: Store and transport between 18-28°C. Temperature cycling causes condensation inside sealed FOUP, contaminating wafers.

## Automated Guided Vehicles (AGVs)

### Design and Operation

AGVs are self-navigating vehicles that transport FOUPs along the fab floor between stockers, tools, and interbay transfer stations.

**Navigation methods**:
- **Magnetic tape guidance**: Ferromagnetic tape (25 mm wide) embedded in the floor. AGV detects tape position with magnetic sensors and follows it. Simple, reliable, but routes are fixed — tape must be re-laid to change paths. Accuracy: ±10 mm.
- **Magnetic grid guidance**: Magnetic pucks or markers embedded in the floor at regular intervals (1-2 m spacing). AGV uses dead reckoning between markers and corrects position at each marker. More flexible routing than continuous tape.
- **Laser navigation**: Laser scanner on AGV measures angles to retroreflective targets mounted on walls and columns. Triangulation gives AGV position with ±5 mm accuracy. Most flexible — paths defined in software, not hardware. Requires line-of-sight to ≥3 reflectors.
- **Inertial navigation**: Gyroscope and accelerometer track position relative to a known starting point. Drift accumulates (1-5 mm per minute) — must be corrected periodically by passing over a floor marker or reference point.

**Vehicle specifications**:
- **Payload**: 1-2 FOUPs (up to 18 kg). Some models carry 4 FOUPs for high-throughput interbay transport.
- **Speed**: 0.5-1.5 m/s (maximum). Average transport speed including acceleration, deceleration, and routing: 0.3-0.8 m/s.
- **Size**: Approximately 800 mm (L) × 600 mm (W) × 400 mm (H) for a single-FOUP unit. Must navigate 1.2 m minimum aisle width.
- **Battery**: Lead-acid or lithium-ion. Runtime: 4-8 hours per charge. Charging stations positioned around fab floor. Automatic battery swap or opportunity charging (charge during idle time at load ports) available on advanced models.
- **Safety sensors**: Bumper switches (contact detection), ultrasonic sensors (0.3-3 m range), laser area scanners (0.1-10 m range). Minimum stopping distance: 200 mm from obstacle detection at full speed. AGVs must stop within 0.5 seconds of obstacle detection.

**AGV dispatch and routing**:
- Central dispatch server receives transport requests from MES (Manufacturing Execution System). Request specifies: pickup location, destination, FOUP ID, priority (normal, urgent, hot lot).
- Dispatch algorithm assigns the nearest idle AGV or en-route AGV (if it can divert to pick up on its current path). Optimization targets: minimize delivery time, balance AGV utilization, avoid traffic congestion.
- Traffic management: AGVs request permission to enter track segments from a zone controller. Only one AGV per zone at a time — prevents collisions at intersections. Zone sizes typically 3-5 meters along the track.

### Performance Metrics

- **Delivery time**: Average 3-8 minutes per FOUP transport (depending on fab size and traffic). Hot lot (highest priority): 1-3 minutes.
- **Throughput**: 30-60 FOUP deliveries per hour per AGV (depends on average distance and loading/unloading time). A fab with 100 AGVs achieves 3,000-6,000 FOUP moves per hour.
- **Reliability**: 99.5-99.9% successful deliveries. Failures caused by: blocked paths (human, obstacle), low battery, navigation error, communication timeout with MES.
- **Utilization**: Target 60-80% of AGVs active (moving or loading/unloading). Below 60% = too many AGVs. Above 80% = insufficient fleet, delivery delays increase.

## Overhead Hoist Transport (OHT)

### Design and Operation

OHT vehicles run on ceiling-mounted rails, providing FOUP transport without consuming floor space. OHT is the dominant transport system in 300 mm fabs.

**Rail system**:
- **Rail profile**: Extruded aluminum or steel I-beam/box-section, 50-100 mm wide. Rail serves as both structural support and guide surface.
- **Mounting**: Suspended from fab ceiling structure at 1.0-1.5 m intervals. Rail height: 2.5-3.5 meters above floor (above tool enclosures, below ceiling ductwork).
- **Track layout**: Network of straight sections, curves (minimum radius 600 mm), switches (turnouts for branching), and merges. Track length in a large fab: 5-20 km total.
- **Power supply**: 24 VDC or 48 VDC bus bar integrated into the rail. Vehicles pick up power through sliding contacts (brushes). No onboard battery required for propulsion (small backup battery for safe lowering during power failure).

**OHT vehicle**:
- **Payload**: 1 FOUP (up to 9 kg). Single-FOUP vehicles are standard; dual-FOUP vehicles exist for high-traffic routes.
- **Speed**: Maximum 3.0 m/s on straight sections, 1.0-1.5 m/s on curves. Average speed including stops and switches: 1.5-2.0 m/s — 3-4× faster than floor AGVs.
- **FOUP handling**: Telescoping fork mechanism reaches down from the rail to pick up/place FOUP at tool load ports or stocker ports. Fork travel: 500-800 mm below rail level. Pickup/placement time: 8-15 seconds per FOUP.
- **Weight**: Vehicle: 15-25 kg. Combined weight of vehicle + FOUP: 25-35 kg. Rail and ceiling structure must support this load plus dynamic forces from acceleration and deceleration.
- **Vehicle density**: 1 vehicle per 10-20 meters of track (depends on traffic pattern). A large fab operates 200-400 OHT vehicles simultaneously.

**OHT control system**:
- **Zone control**: Track divided into zones (3-5 meters each). Only one vehicle per zone. Vehicle requests zone clearance from zone controller before entering.
- **Switch control**: Track switches (for branching) are powered devices that change position in 0.5-1.0 seconds. Vehicle requests switch position before arriving at the switch.
- **Communication**: Vehicle communicates with central controller via wireless LAN (2.4 GHz or 5 GHz) or infrared along the rail. Message latency: <50 ms for commands.
- **Traffic optimization**: Central controller computes optimal routes considering current vehicle positions, traffic density, and switch states. Re-routes vehicles around congestion in real-time.

### OHT vs AGV Comparison

| Parameter | OHT | Floor AGV |
|-----------|-----|-----------|
| Transport speed | 1.5-2.0 m/s avg | 0.3-0.8 m/s avg |
| FOUP delivery time | 1-4 min avg | 3-8 min avg |
| Throughput/vehicle | 15-25 FOUP/hr | 6-12 FOUP/hr |
| Floor space | None (overhead) | Aisle width 1.2 m |
| Installation cost | Higher (rail infrastructure) | Lower (tape/markers) |
| Flexibility | Fixed (rail changes costly) | Moderate (re-tape floor) |
| Maintenance access | Difficult (overhead work) | Easy (floor level) |

Most 300 mm fabs use OHT as the primary transport system and AGVs as a supplement for specific routes or as a backup.

## Rail-Guided Vehicles (RGV)

RGVs run on floor-level rails (not overhead) for high-speed, high-throughput interbay transport.

**Specifications**:
- **Rail**: Flush-mounted steel rails in the floor, 300-600 mm gauge. Rail is level with floor surface (no tripping hazard).
- **Speed**: Up to 5.0 m/s on straight sections — the fastest intrabay transport option. Average speed including stops: 2.5-3.5 m/s.
- **Payload**: 1-4 FOUPs.
- **Advantage**: Higher speed and throughput than AGVs or OHT on dedicated point-to-point routes.
- **Limitation**: Fixed route — cannot deviate from the rail. Used for high-volume interbay transfer between stocker aisles.

## Stockers

Stocker systems store FOUPs when they are not actively being processed. A large fab has multiple stockers totaling 5,000-20,000 FOUP storage positions.

**Crank-type stocker**:
- **Design**: Vertical storage rack with shelves on both sides of a central aisle. A crane mechanism (crank arm with FOUP gripper) travels vertically and horizontally to any shelf position. Stores and retrieves FOUPs on command from MES.
- **Capacity**: 100-500 FOUP positions per stocker unit. Multiple units can be combined into larger storage systems.
- **Access time**: 15-60 seconds for any FOUP (time for crane to travel to shelf, pick FOUP, return to I/O port). Average access time: 30 seconds.
- **Environment**: Stocker interior maintained at ISO Class 4-5 with continuous HEPA filtration. Nitrogen purge option for moisture-sensitive wafers.

## Fab Logistics Coordination

### MES Integration

The Manufacturing Execution System coordinates all material transport:

1. **Lot dispatch**: MES determines which lot should go to which tool next based on process flow, tool availability, and WIP (Work In Process) balancing.
2. **Transport request**: MES issues transport command to material control system (MCS) specifying FOUP ID, source location, destination location, and priority.
3. **MCS dispatch**: Material Control System selects the transport vehicle (OHT, AGV, or RGV), computes the route, and dispatches the vehicle.
4. **Delivery confirmation**: Vehicle confirms FOUP pickup and delivery via RFID read at each location. MES updates lot status and tool queue.

### Hot Lot Management

- **Hot lots** (priority lots for development or critical customer orders) receive preemptive transport: other vehicles are rerouted to clear the path. Target delivery time: ≤2 minutes for any destination in the fab.
- **Super hot lots**: Extremely high priority (typically <1% of lots). Entire tool dedication — the tool processes only this lot until complete. Transport vehicles assigned exclusively.

### Deadlock Prevention

- **Buffer management**: When a tool's input buffer is full, incoming FOUPs must be rerouted to a stocker. The MCS monitors buffer occupancy and reroutes transport proactively.
- **Vehicle starvation prevention**: MCS distributes transport requests across available vehicles to prevent some vehicles from being overloaded while others idle.
- **Traffic congestion detection**: When transport delivery times exceed threshold (e.g., >10 minutes for a normally 3-minute route), MCS reroutes traffic and may temporarily store FOUPs at intermediate stockers.

### Safety & Hazards

- **FOUP drop risk**: OHT vehicle dropping a FOUP from overhead height (2.5-3.5 m) is a catastrophic event — wafer destruction and potential injury. Redundant grip mechanisms (mechanical latch plus vacuum hold) and continuous grip-force monitoring prevent drops. Drop rate target: <1 per 10 million transports.
- **OHT collision**: Overhead vehicles can collide at switches or merge points. Zone control, anti-collision sensors, and emergency stop systems prevent collisions. System must fail-safe — on communication loss, vehicle stops and lowers FOUP to nearest safe position.
- **AGV pedestrian safety**: Floor-level AGVs share space with fab operators. AGVs must detect humans and stop. Bumper sensors (contact), ultrasonic proximity (preventive), and floor markings (travel paths) mitigate collision risk. Maximum AGV speed in pedestrian areas: 0.5 m/s.
- **FOUP contamination**: Transport system must not introduce particles into FOUP interior. Vehicle gripper mechanisms must be cleanroom-compatible. FOUP exterior cleaning (wiper or air knife) before loading onto tool load port.

## Interbay vs Intrabay Transport

### Transport Hierarchy

A fab is organized into bays — physically separate areas housing groups of related process tools. Transport operates at two levels:

**Interbay transport** (between bays):
- Moves FOUPs between different process areas (e.g., from diffusion bay to etch bay, from lithography to inspection). Distances: 50-300 meters between bays.
- High-speed, high-throughput transport: OHT on dedicated interbay express rails, or RGV on floor rails connecting bay stockers.
- Interbay stockers serve as transfer points: OHT from Bay A delivers FOUP to Bay A stocker → interbay transport picks up → delivers to Bay B stocker → Bay B OHT delivers to tool in Bay B.
- Throughput requirement: 200-500 interbay FOUP moves per hour in a high-volume fab.

**Intrabay transport** (within a bay):
- Moves FOUPs between tools within the same process bay. Distances: 5-50 meters.
- OHT on bay-level rails or AGVs on bay floor. Shorter distances, more frequent moves.
- Throughput requirement: 100-300 intrabay moves per hour per bay.
- Direct tool-to-tool transfers (bypassing stocker) are preferred to reduce delivery time. Requires coordination between MES, MCS, and tool scheduling.

### Unified MCS Architecture

The Material Control System (MCS) manages the entire transport hierarchy:

- **MCS layers**: Interbay MCS (manages interbay vehicles and stockers) communicates with multiple intrabay MCS instances (one per bay, managing bay-level vehicles and tools). Alternatively, a single unified MCS manages all levels.
- **Transport request pipeline**: MES → MCS: "Move FOUP X from Tool A (Bay 1) to Tool B (Bay 3)". MCS decomposes: (1) Intrabay move from Tool A to Bay 1 stocker, (2) Interbay move from Bay 1 stocker to Bay 3 stocker, (3) Intrabay move from Bay 3 stocker to Tool B. Each sub-move dispatched to the appropriate vehicle.
- **Delivery time target**: Total interbay delivery ≤8 minutes (including two stocker accesses and one interbay transit). Total intrabay delivery ≤3 minutes. Hot lot interbay ≤4 minutes.

## FOUP Handling Ergonomics

Even in highly automated fabs, operators occasionally handle FOUPs manually (tool setup, maintenance, off-line inspection):

- **Weight limit**: Fully loaded FOUP (9 kg) is within the 10-15 kg recommended maximum for occasional lifting (NIOSH lifting equation). However, repetitive manual handling (>10 FOUPs per hour) requires mechanical assist.
- **Ergonomic load port height**: Load ports positioned 900-1,100 mm above floor (waist height for average operator). Eliminates bending for FOUP loading/unloading.
- **Manual transport carts**: Push carts carrying 2-8 FOUPs for short-distance moves during tool maintenance. Cart wheel diameter ≥100 mm for smooth rolling on raised-floor panels. Caster brakes prevent uncontrolled rolling.

### Raised Floor Considerations

Most 300 mm fabs use raised access flooring (perforated panels 300-600 mm above structural slab) for under-floor air return and utility routing:

- **AGV floor flatness**: Raised floor panels must be level within ±1.5 mm over 3 meters for AGV navigation accuracy. Panels must support AGV wheel loads (concentrated 500-1,000 N per wheel) without deflection. Panel deflection under load causes AGV navigation errors.
- **Panel gap management**: Gaps between raised floor panels must be ≤1 mm to prevent AGV wheels catching. Anti-static panels (resistivity 10⁶-10⁹ Ω/sq) prevent static discharge damage to passing FOUPs.
- **Floor loading**: Raised floor rated for 5-12 kPa uniform load. FOUP stockers (2,000-5,000 kg) require reinforced floor sections or direct slab mounting.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Automation & Robotics](./index.md) • [All Domains](../index.md)*
