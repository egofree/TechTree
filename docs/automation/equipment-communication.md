# Equipment Communication

> **Node ID**: automation.equipment-communication
> **Domain**: [Automation & Robotics](./index.md)
> **Dependencies**: `computing`, `electronics`
> **Enables**: [`automation.material-transport`](material-transport.md), [`automation.process-control`](process-control.md)
> **Timeline**: Years 50-100+
> **Outputs**: secs_gem_communication, equipment_state_data, alarm_events, process_trace_data

## Problem

A modern semiconductor fab contains hundreds of process tools — etchers, CVD reactors, implanters, lithography scanners, CMP polishers — each from different manufacturers, each with proprietary control interfaces. Without standardized communication, every tool integration requires custom software, and centralized fab control is impossible. SECS/GEM protocols solve this by defining a universal language for equipment-to-host data exchange, enabling automated process control, recipe management, and real-time monitoring across the entire fab.

## Decision Framework: Communication Protocol Selection

| Scenario | Recommended Protocol | Rationale |
|----------|---------------------|-----------|
| New 300 mm fab with all modern tools | HSMS + GEM + GEM300 | Maximum throughput, full automation, 300 mm carrier/substrate tracking |
| Legacy tools with serial ports only | SECS-I + GEM | Backward compatible, works with existing hardware |
| Multi-equipment behind one network connection | HSMS-GS (General Session) | Reduces TCP connections, single host port serves multiple tools |
| Safety-critical gas cabinet communication | HSMS with dual redundant paths | Fault tolerance for life-safety systems |
| Lab-scale or development tools | SECS-I serial or HSMS with minimal GEM | Lowest integration cost for non-production equipment |

### Implementation Steps

1. **Inventory all process tools**: Document each tool's communication capability (SECS-I, HSMS, GEM compliance level, GEM300 support)
2. **Deploy SECS gateway server**: Install centralized gateway with HSMS connections to all HSMS-capable tools and serial-to-HSMS converters for legacy tools
3. **Develop equipment drivers**: For each tool type, develop a SECS/GEM driver that maps tool-specific variables to MES data fields. Allow 2-6 months per tool type for driver development and testing
4. **Conduct conformance testing**: Run SEMI GEM conformance test suite on each tool before production deployment. Verify state transitions, alarm reporting, event notification, and error recovery
5. **Integrate with MES**: Connect gateway to MES application. Configure event subscriptions, trace data collection, and recipe management workflows
6. **Validate end-to-end**: Download recipe, start process, collect trace data, verify alarm handling. Integration testing: 1-4 weeks per tool type

## SECS Protocol Family

### SECS-I (SEMI E4)

SECS-I defines the physical and data link layer for serial communication between equipment and host computers.

**Strengths**:
- Simple point-to-point wiring: one serial cable per tool, no network infrastructure needed
- Proven protocol with decades of field deployment and broad tool support
- Low cost: standard RS-232 ports and cabling

**Weaknesses**:
- Limited throughput: ~10 KB/s at 115,200 baud — insufficient for high-frequency trace data
- Point-to-point only: each tool requires a dedicated serial port on the host (200 tools = 200 ports)
- Maximum cable length 15 meters — limits tool placement flexibility

**Physical layer**:
- **Interface**: RS-232C serial connection. Point-to-point (one host port to one equipment port).
- **Cable**: DB-25 or DB-9 connector, maximum cable length 15 meters (RS-232 limit). For longer runs, use RS-232 to fiber-optic converters.
- **Signal levels**: Mark (logic 1) = -3V to -15V. Space (logic 0) = +3V to +15V. RS-232 receivers must tolerate ±25V.
- **Baud rates**: Supported: 9,600, 19,200, 38,400, 76,800, 115,200 baud. Modern implementations default to 115,200 baud. Higher baud rates reduce message latency but increase susceptibility to electrical noise.

**Data link layer**:
- **Message framing**: Each message is a sequence of 10-bit bytes (1 start bit, 8 data bits, 1 stop bit). Messages are blocked into 256-byte blocks maximum.
- **Block structure**: Each block contains a 10-byte header and up to 246 bytes of data. Header includes: device ID (2 bytes), reserved (1 byte), system bytes (4 bytes), and block metadata.
- **T1/T2/T3/T4 timers**: T1 = inter-character timeout (typically 10 seconds between characters within a message). T2 = response timeout (equipment must reply within T2 seconds, typically 10-30 seconds). T3 = reply delay (equipment processing time before response). T4 = inter-block timeout for multi-block messages.
- **Error handling**: Linktest messages verify connection integrity. Timeout on T1 or T2 triggers retry or link reset. CRC or checksum validation on each block.

**Limitations of SECS-I**:
- Serial communication limits throughput to ~10 KB/s at 115,200 baud.
- Point-to-point only: each equipment requires a dedicated serial port on the host.
- No built-in network addressing — the host must have one RS-232 port per tool.
- A fab with 200 tools requires 200 serial ports and 200 RS-232 cables. This cabling nightmare motivated the development of HSMS.

### SECS-II (SEMI E5)

SECS-II defines the message content — the application-layer protocol that structures data into hierarchical messages regardless of transport (SECS-I or HSMS).

**Message structure**:
- **Stream and Function**: Each SECS-II message is identified by Stream (S) and Function (F) numbers. Stream = category of operation (1-127). Function = specific operation within that stream (1-255). Odd function numbers = primary message (request). Even function numbers = secondary message (reply).
- **Common streams**: S1 = Facility Status, S2 = Equipment Control, S5 = Exception Handling, S6 = Data Collection, S7 = Process Program Management, S9 = System Errors.

**Data item types**:
- **Binary**: Raw byte sequences. Used for images, waveforms, and opaque data blocks.
- **Boolean**: TRUE/FALSE values. Used for status flags.
- **ASCII**: Character strings. Used for equipment IDs, alarm text, recipe names, variable identifiers.
- **Integer (I1, I2, I4, I8)**: Signed integers of 1, 2, 4, or 8 bytes. I1 range: -128 to 127. I2: -32,768 to 32,767. I4: -2,147,483,648 to 2,147,483,647. I8: -2⁶³ to 2⁶³-1.
- **Unsigned (U1, U2, U4, U8)**: Same sizes but unsigned. U1 range: 0-255. U2: 0-65,535. U4: 0-4,294,967,295.
- **Floating point (F4, F8)**: IEEE 754 single (32-bit) and double (64-bit) precision. F4: ±3.4×10³⁸ with 7 significant digits. F8: ±1.8×10³⁰⁸ with 15 significant digits.

**List structures**:
- SECS-II data is organized as nested lists. A List item contains zero or more items (which can themselves be lists, creating tree structures).
- Example: S1F1 (Are You There request) has no data body — the message itself is the query. S1F2 (Online Data reply) contains a list of: [MDLN (model name string), SOFTREV (software revision string)].
- Example: S2F41 (Host Command Send) contains: [RCMD (remote command string), CP NAME=VALUE pairs]. The list structure allows variable-length parameter sets.

**Key message types**:
- **S1F1/F2**: Are You There / Online Data. Equipment identification handshake.
- **S2F13/F14**: Equipment Constant Request/Reply. Read configuration parameters.
- **S2F15/F16**: New Equipment Constant Send/Acknowledge. Write configuration parameters.
- **S2F41/F42**: Host Command Send/Acknowledge. Execute remote command (e.g., START, ABORT, PAUSE process).
- **S5F1/F2**: Alarm Report Send/Acknowledge. Equipment reports alarm condition to host.
- **S5F3/F4**: Enable/Disable Alarm Post. Host controls which alarms are reported.
- **S6F1/F2**: Trace Data Send/Acknowledge. Periodic data sampling (e.g., temperature every 5 seconds during process run).
- **S7F1/F2**: Process Program Load Inquire/Acknowledge. Ask if equipment can accept a recipe.
- **S7F3/F4**: Process Program Send/Acknowledge. Transfer recipe to equipment.
- **S7F5/F6**: Process Program Request/Acknowledge. Upload recipe from equipment.

### HSMS (SEMI E37)

High-Speed SECS Message Services replaces SECS-I with TCP/IP networking, solving the cabling and throughput limitations.

**Strengths**:
- 50× faster than SECS-I: ~500 messages/second on 100 Mbps Ethernet
- Standard TCP/IP: one Ethernet switch serves dozens of tools — eliminates serial port cabling
- Bidirectional: equipment can initiate messages, not just respond to host

**Weaknesses**:
- Requires Ethernet infrastructure and IP address management in fab network
- TCP connection maintenance: keep-alive and reconnection logic adds software complexity
- Network security: must be isolated from corporate LAN and internet to prevent unauthorized access

**Transport layer**:
- **Protocol**: TCP/IP. Equipment acts as TCP server listening on a configurable port (commonly port 5000). Host connects as TCP client.
- **Network**: Standard Ethernet (10/100/1000 Mbps). A single Ethernet switch serves dozens of equipment connections.
- **Session**: One TCP connection per equipment-host pair. Connection maintained persistently (keep-alive). Linktest messages (similar to SECS-I) verify connection health.

**Message differences from SECS-I**:
- **Same SECS-II message content**: HSMS only replaces the transport; all Stream/Function messages are identical.
- **System bytes**: 4-byte system ID for matching requests and replies. Each new primary message increments the system byte counter.
- **Select procedure**: After TCP connect, host sends Select.req to establish HSMS session. Equipment responds Select.rsp. Only after Select is the session active for SECS messaging.
- **Deselect procedure**: Graceful session termination before TCP disconnect.
- **Separate connection**: HSMS allows equipment to initiate messages (not just respond). In SECS-I, only the host initiates. HSMS supports both host-initiated and equipment-initiated connections.

**HSMS-GS (General Session)**: Extension for multi-equipment on a single TCP connection. Each equipment identified by a device ID within the session. Reduces the number of TCP connections needed for large fab deployments.

**Throughput**: Ethernet at 100 Mbps delivers effective SECS message throughput of ~500 messages per second (limited by message processing, not bandwidth). This is 50× faster than SECS-I serial at 115,200 baud.

### GEM (SEMI E30)

GEM (Generic Equipment Model) builds on SECS-II messaging to define standard equipment behavior for factory automation.

**GEM state model**:
Equipment follows a defined state machine with states:
- **EQUIP/NOT_COMM**: Equipment not communicating.
- **DISABLED**: Equipment powered but not enabled for remote control.
- **ENABLED**: Equipment ready for remote commands. Sub-states:
  - **IDLE**: No process active, ready to receive new lot.
  - **SETUP**: Loading recipe parameters for next process.
  - **READY**: Recipe loaded, waiting for START command or auto-start.
  - **EXECUTE**: Process actively running. Sub-states within EXECUTE track process phase (e.g., pump-down, heat, process, vent).
  - **PAUSE**: Process temporarily suspended (operator or host command).
  - **COMPLETING**: Process finishing, data logging, wafer map update.
- **ABORTING**: Process terminated early. Equipment transitioning to safe state.

**State transitions**:
- Host commands trigger state transitions via S2F41 (Remote Command).
- Equipment-initiated transitions (e.g., process complete) reported via S6F11 (Event Report).
- The host tracks equipment state by subscribing to state change events. Each state change generates an event report containing: [CEID (Collection Event ID), timestamp, state data].

**GEM capabilities**:
1. **Establish Communications**: S1F13/F14 establish online identity exchange.
2. **Status Variable Collection**: Read equipment status on demand (temperatures, pressures, gas flows, RF power).
3. **Equipment Constants**: Read/write equipment configuration (gas flow limits, temperature setpoints, safety thresholds).
4. **Alarm Management**: Equipment reports alarms via S5F1. Host acknowledges via S5F2. Host can enable/disable individual alarms. Alarm states: ON (active), OFF (cleared). Alarms have severity levels: personal safety, equipment safety, process, advisory.
5. **Event Notification**: Equipment sends unsolicited event reports (state changes, process milestones, operator actions) via S6F11. Host subscribes to specific events by CEID.
6. **Trace Data**: Continuous periodic data collection. Host defines trace request: [RPTID, variables to sample, sampling period, total samples]. Equipment sends periodic S6F1 messages with sampled data. Used for real-time process monitoring.
7. **Remote Control**: Host sends process commands via S2F41: START, ABORT, PAUSE, RESUME. Equipment acknowledges via S2F42 with result code (accepted, rejected, already-in-state).
8. **Process Program Management**: Upload/download recipes between host and equipment via S7 messages. Recipes versioned and checksummed.
9. **Material Movement**: Coordinate wafer transfer with material handling system. Equipment reports port status, wafer presence, and lot identity.

**Event model**:
- **CEID (Collection Event ID)**: Each reportable event has a unique numeric identifier. Example: CEID 101 = "Process Started", CEID 102 = "Process Completed", CEID 103 = "Temperature Stabilized".
- **RPTID (Report ID)**: Defines which data variables are included in an event report. One RPTID maps to a list of variable IDs (VID). When the event fires, the equipment collects current values of all variables in the report and sends them.
- **Link Event Report**: S2F35 links a CEID to an RPTID. "When event 101 occurs, send report 5 (containing temperature, pressure, gas flow)."
- **Enable Event Report**: S2F37 enables/disables reporting for specific CEIDs.

### Equipment Integration Architecture

**Host-to-equipment data flow**:
1. Host connects via HSMS TCP/IP to equipment.
2. Select procedure establishes session.
3. Host performs S1F13 (Establish Communications) to verify equipment identity and software version.
4. Host subscribes to relevant events using S2F35/S2F37.
5. Host downloads active recipe via S7F3.
6. Host sends START command via S2F41.
7. Equipment transitions to EXECUTE state, sends S6F11 event reports at each process milestone.
8. Equipment sends trace data (S6F1) during process at configured intervals.
9. Equipment reports completion via S6F11 (CEID = process complete) with final process data.
10. Host uploads process results, wafer maps, and alarm history.

**Error handling**:
- **S9 messages**: System errors for protocol violations. S9F1 = Unrecognized Device ID. S9F3 = Unrecognized Stream Type. S9F5 = Unrecognized Function Type. S9F7 = Illegal Data. S9F9 = Transaction Timer Timeout.
- **S2F42 rejection codes**: HCACK (Host Command Acknowledge) = 0 (acknowledged), 1 (rejected: invalid command), 2 (rejected: cannot perform now), 3 (rejected: parameter error).
- **T3 timeout**: If equipment does not reply within T3 seconds, the host logs a communication error and may retry or escalate to operator intervention.

### Safety & Hazards

- **Remote control risk**: GEM allows the host to start and stop equipment remotely. Incorrect commands can cause equipment damage or operator injury. All remotely-triggered equipment actions must have safety interlocks independent of the communication channel (hardware E-stop, door interlocks, gas detection).
- **Recipe corruption**: A corrupted recipe downloaded via S7F3 can cause equipment to operate outside safe parameters (e.g., wrong gas flow, excessive RF power). Validate recipe checksums before loading. Maintain recipe revision control with approval workflows.
- **Network isolation**: HSMS runs over TCP/IP but must be on an isolated fab network, not accessible from the Internet or corporate LAN. Network breaches could compromise equipment control. Use dedicated VLANs and firewalls between equipment network and MES server network.
- **Alarm flooding**: Equipment malfunction can generate thousands of alarm events per second, overwhelming the host communication channel. Implement alarm suppression (group related alarms, throttle repeated alarms) and priority-based alarm delivery.

## Implementation Considerations

**Equipment driver development**:
- **SECS driver**: Software library implementing SECS-I/HSMS transport and SECS-II message formatting. Available as commercial packages (Brooks, PEER, GW Associates) or open-source implementations (e.g., HSMS libraries in C, C++, Python, Java). A typical driver handles: TCP connection management, message serialization/deserialization, T1/T2/T3 timer management, linktest heartbeat, and callback hooks for incoming messages.
- **Equipment-side implementation**: Equipment manufacturers embed a SECS/GEM stack in the tool controller (typically a Windows or Linux industrial PC). The stack exposes a C/C++ API for the equipment firmware to report events, update status variables, and respond to host commands. Implementation effort: 2-6 months of software engineering per tool type.
- **Host-side (MES) implementation**: The MES connects to hundreds of tools simultaneously. A SECS gateway server multiplexes all tool connections and presents a unified API to the MES application. The gateway handles connection failures, message queuing, and tool state tracking.

**Testing and qualification**:
- **SECS/GEM conformance testing**: SEMI provides a conformance test suite verifying that equipment implements GEM state transitions correctly. Tests include: communication establishment, remote command execution, alarm reporting, event notification, and error recovery. Equipment must pass all conformance tests before deployment in production.
- **Integration testing**: After conformance testing, the MES team performs integration testing: download a recipe, start a process, collect trace data, verify alarm handling. Typical integration: 1-4 weeks per tool type depending on complexity.
- **Regression testing**: When equipment firmware is updated, re-run integration tests to verify SECS/GEM behavior is unchanged. Automated test scripts execute standard scenarios and compare results against baseline.

**Performance benchmarks**:
- **Message latency**: HSMS message round-trip time (host sends primary message, receives reply): 10-50 ms on a dedicated LAN. Adds 50-100 ms overhead for message processing on each end. SECS-I serial: 50-500 ms per message at 115,200 baud.
- **Trace data throughput**: Continuous trace reporting (20 variables at 1 Hz per tool): 20 messages/second × 200 bytes/message = 4 KB/s per tool. A fab with 200 tools generates 800 KB/s of trace data continuously. FDC servers must ingest and process this in real-time.
- **Event processing**: Equipment state changes generate 5-20 events per process run. With 200 tools each processing 10 lots/day: 10,000-40,000 events/day. MES must process each event within 1 second to maintain real-time lot tracking.

### GEM300 Extensions

For 300 mm fabs, SEMI E38 (GEM300) adds capabilities specific to automated wafer handling:

**Carrier Management (SEMI E84)**:
- **Carrier ID**: Barcode or RFID on the FOUP housing, read by the load port. MES verifies carrier identity matches the expected lot before processing begins.
- **Carrier Access**: Automated load port opens the FOUP door, scans wafer slots (using optical sensors), and reports slot map to MES via SECS/GEM event.
- **Transfer Status**: Load port reports FOUP transfer state: IDLE, READY_TO_LOAD, TRANSFER_BLOCKED, COMPLETE. MES uses transfer status to coordinate AGV/OHT delivery timing.

**Substrate Tracking (SEMI E90)**:
- **Substrate ID**: Individual wafer tracking by wafer ID (read from wafer markings or inferred from slot position in a mapped FOUP).
- **Substrate Location**: MES tracks which wafer is in which chamber at which processing step. The tool reports substrate arrival/departure events.
- **Substrate History**: Every wafer's complete processing history stored in MES database, traceable by wafer ID.

**Process Job Management (SEMI E94)**:
- **Process Job**: MES defines a process job containing: lot ID, recipe ID, tool type, and execution criteria. The job is sent to the equipment controller, which manages execution autonomously (including wafer movement between chambers) and reports completion.
- **Control Job**: Higher-level container for multiple process jobs on the same tool. Enables batch scheduling and resource sharing between jobs.

**Terminal Services (SEMI E87)**:
- **Terminal mode**: Provides a text-based operator interface on the equipment display for MES to send instructions, display lot information, and prompt operator actions (e.g., "Load FOUP A12345 at Load Port 1").
- **Remote display**: MES can push messages to the equipment's operator panel, eliminating the need for separate terminal displays at each tool.

### Communication Redundancy

- **Dual network paths**: Critical tools may have dual HSMS connections (primary and backup Ethernet paths) for fault tolerance. If the primary network switch fails, the backup path takes over within 5 seconds.
- **Local operation mode**: If all communication with MES is lost, the tool must continue operating in local mode. The operator selects recipes manually from the tool's control panel and monitors the process using the tool's built-in displays. Local operation is logged and reported when communication is restored.
- **Message queuing**: During brief communication interruptions (<30 seconds), the HSMS gateway queues messages and delivers them when the connection recovers. Longer interruptions (>30 seconds) trigger the tool to enter local mode and alert the operator.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| HSMS connection refused | Equipment controller not running or firewall blocking | Verify equipment controller process is active; check TCP port 5000 (default); verify network path and firewall rules |
| Message timeout (T3 timer) | Network congestion or equipment slow to respond | Increase T3 timeout; check network switch load; verify equipment CPU not overloaded |
| S1F13 error (communication establishment fails) | Incompatible SECS/GEM version or device ID mismatch | Verify device ID matches host configuration; check SECS/GEM version compatibility; review equipment logs |
| Duplicate message received | Network retransmission or equipment sending twice | Check for network packet duplication; verify T5 (connect separation timer) configuration |
| Equipment alarm flood | Process upset generating hundreds of alarms | Configure alarm filtering at gateway; group related alarms; check equipment-side alarm thresholds |
| Data collection events missing | Equipment not configured to send trace data | Verify S2F33/S2F35 trace setup; check event enable flags; confirm recipe includes trace parameters |

## See Also

- [Process Control](process-control.md) — the automation system that consumes equipment data
- [Material Transport](material-transport.md) — automated wafer and carrier movement
- [Electronics](../electronics/index.md) — electronic hardware underlying communication
- [Computing](../computing/index.md) — computing infrastructure for fab control systems
- [Photolithography / Fab Processes](../photolithography/fab-processes.md) — the tools being controlled
- [Cleanrooms](../photolithography/cleanrooms.md) — the environment housing the equipment

[← Back to Automation & Robotics](index.md)
