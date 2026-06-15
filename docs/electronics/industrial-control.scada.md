# SCADA System Design

> **Node ID**: electronics.industrial-control.scada
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.industrial-control`](industrial-control.md), [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.industrial-control.plc`](industrial-control.plc.md)
> **Enables**: None
> **Timeline**: Years 35-55
> **Outputs**: scada-system-designs
> **Critical**: No — SCADA is the supervisory/aggregation layer built atop the embedded controller and semiconductor substrate; it organizes visibility and coordination across sites rather than gating a primary bootstrap dependency

SCADA — **S**upervisory **C**ontrol **A**nd **D**ata **A**cquisition — is the system architecture that gives a human operator centralized visibility and command over geographically distributed process plants. Where a single [PLC](industrial-control.plc.md) controls one machine or one process cell, SCADA stitches dozens or hundreds of PLCs and field devices into one observable whole: the operator at a control-center console sees every pump, valve, temperature, and flow rate across the entire site, and can issue setpoint changes without leaving the chair.

The distinction between SCADA and its near cousins matters:

- **PLC** = the *controller*. It executes deterministic logic (ladder/structured text) on a fixed scan cycle, directly wired to sensors and actuators. Covered in [industrial-control.plc](industrial-control.plc.md) (task 27).
- **HMI** = the *operator screen*. It displays process state and accepts commands for one local area. Covered in [industrial-control.hmi](industrial-control.hmi.md).
- **SCADA** = the *supervisory network*. It aggregates many PLCs/RTUs across a site or region, stores historical trends, manages plant-wide alarms, and presents one unified operator interface. The MTU (Master Terminal Unit) at the top is where SCADA lives.

SCADA does not *replace* the PLC — it *supervises* many PLCs. The PLC still closes the local control loop (e.g., maintain tank level at setpoint). SCADA reads the level, logs the trend, raises an alarm if it deviates, and lets the operator change the setpoint from the control room rather than walking to the panel.

This article teaches SCADA architecture from the MTU at the top down to the field instrument at the bottom, with worked telemetry examples and a protocol comparison.

## The SCADA Hierarchy

Every SCADA system is a layered tree. At the top sits the control center; at the bottom sit the physical sensors and actuators. Data flows up the tree (telemetry); commands flow down (supervisory setpoints and digital commands).

```
                         ┌─────────────────────────────────┐
                         │         CONTROL CENTER          │
                         │   ┌───────────────────────────┐ │
            Level 3      │   │   MTU (Master Terminal)   │ │
   (Enterprise /         │   │  HMI software + historian │ │
    Site-wide)           │   │  + alarm mgmt + reports   │ │
                         │   └─────────────┬─────────────┘ │
                         └─────────────────┼───────────────┘
                                           │  communication network
                    ┌──────────────────────┼──────────────────────┐
                    │                      │                      │
                    ▼                      ▼                      ▼
              ┌──────────┐           ┌──────────┐           ┌──────────┐
   Level 2    │   RTU    │           │   RTU    │    ...    │   PLC    │
  (Substation/│  or PLC  │           │  or PLC  │           │  field   │
   Field site)│ field #1 │           │ field #2 │           │  cell N  │
              └────┬─────┘           └────┬─────┘           └────┬─────┘
                   │                      │                      │
            ┌──────┼──────┐         ┌──────┼──────┐         ┌──────┼──────┐
            ▼      ▼      ▼         ▼      ▼      ▼         ▼      ▼      ▼
          sens  sens   actr      sens  sens   actr       sens  sens   actr
   Level 1  or   or     or        or    or     or          or    or     or
  (Field     TT   FT    valve     PT    LT    pump        TT    FT    valve
   devices)  ─    ─     ─         ─     ─     ─           ─     ─     ─
            4-20  4-20  4-20      4-20  4-20  discrete    4-20  4-20  4-20
            mA    mA    mA        mA    mA    output      mA    mA    mA
```

**Level 1 — Field devices**: The physical instruments. Analog sensors (temperature transmitters, pressure transmitters, flow meters) output a 4-20 mA current-loop signal proportional to the measured variable. Discrete devices (pump running, valve open, level switch) provide a simple on/off contact. Actuators (control valves, variable-speed drives) accept a 4-20 mA command or discrete signal.

**Level 2 — RTU / PLC**: The [Remote Terminal Unit](#rtu-remote-terminal-unit) or PLC is the field-site data concentrator and controller. It wires directly to the Level 1 devices, runs local control logic, and communicates with the MTU over the SCADA network.

**Level 3 — MTU / Control Center**: The [Master Terminal Unit](#mtu-master-terminal-unit) is the central computer running HMI software, the process historian, and the alarm management system. The operators sit here. This is where the SCADA "lives" in the everyday sense.

The communication network connecting Level 3 to Level 2 is the defining characteristic of SCADA — it spans whatever distance separates the control room from the field sites: a few hundred meters within a single plant (Ethernet, fiber), or hundreds of kilometers across a utility service territory (radio, cellular, microwave, leased line).

## MTU (Master Terminal Unit)

The MTU is the central supervisory computer. It is typically a redundant pair of rack servers (primary + hot-standby) running commercial SCADA software (Wonderware, VTScada, Ignition, WinCC, or a custom application). The MTU performs four functions continuously:

### 1. Poll the field (data acquisition)

The MTU cycles through every RTU/PLC in its address list, requesting current values. In a **poll/response** (master-slave) architecture, the MTU asks each field unit in turn: "send me your data." The field unit responds. In an **exception-report** (report-by-exception, RBQ) architecture, the field unit transmits only when a value has changed beyond a deadband or an event has occurred — the MTU still periodically polls to confirm the link is alive. The polling strategy determines the communication load (see [worked example](#worked-example-rtu-poll-rate) below).

### 2. Display process status

The MTU drives the operator HMI screens — process mimic displays showing animated pumps, valves, tanks, and pipes colored by state; live numeric readouts of every analog variable; and alarm banners. This is the human-facing layer; see [HMI Design](industrial-control.hmi.md) for screen-design principles.

### 3. Log trends (the historian)

Every analog value and every event is timestamped and written to the **process historian** — a time-series database optimized for high-rate append and range queries. The historian is what makes trending, efficiency accounting, and predictive maintenance possible. A mid-size plant historian ingests thousands of tags at 1-second resolution, storing years of history. Typical queries: "show tank-3 level for the last 24 hours," "what was the steam flow when the trip occurred at 03:14?"

### 4. Manage alarms and generate reports

The MTU evaluates every incoming value against alarm limits. When a value crosses a threshold, it generates an alarm event (priority, timestamp, tag, description) that is pushed to the operator's alarm banner and logged to the alarm history. The MTU also generates periodic reports (shift logs, daily production totals, efficiency calculations, environmental compliance records) by querying the historian.

## RTU (Remote Terminal Unit)

The RTU is the field-mounted data concentrator. It is the SCADA system's outpost at a remote site — a substation, a pump station, a wellhead, a pipeline metering skid — where there is no operator and no local HMI, just instruments and a communication link back to the MTU.

**Hardware architecture**: An RTU contains:

- **Digital input (DI) modules**: dry-contact inputs for discrete states (pump running, valve open, level switch tripped). Optically isolated (optocoupler) to protect the RTU from field wiring faults.
- **Digital output (DO) modules**: relay or transistor outputs for discrete commands (start pump, open valve). Often latching relays so a command survives a communication dropout.
- **Analog input (AI) modules**: analog-to-digital converters reading 4-20 mA current loops or voltage signals. Resolution is typically 12-16 bits. Each channel has a precision burden resistor (e.g., 250 Ω converts 4-20 mA to 1-5 V for the ADC).
- **Analog output (AO) modules**: digital-to-analog converters generating 4-20 mA command signals for control valves or speed references.
- **Communication interface**: serial (RS-232, RS-485), Ethernet, radio modem, or cellular modem — whatever reaches the MTU.
- **CPU + memory**: a microcontroller (see [computing.embedded-systems](../computing/embedded-systems.md)) that scans the I/O, runs any local logic, buffers data during communication outages, and manages the protocol stack.

**RTU vs PLC**: The line has blurred. Historically, an RTU was a data concentrator optimized for remote communication (serial protocols, radio links, data buffering during outages, low power for solar sites), while a PLC was a high-speed local controller optimized for deterministic logic execution. Modern devices do both: a PLC with a communication card can serve as an RTU, and a modern RTU can run ladder logic. The [PLC](industrial-control.plc.md) article covers the controller side; here we treat both as the Level-2 field unit.

**Communication media to the MTU**: The RTU-to-MTU link is the most variable part of a SCADA system. Options:

- **Leased copper line / serial**: RS-232 (point-to-point, <15 m) or RS-485 (multi-drop, up to 1.2 km, 32 nodes). Old but reliable for in-plant links.
- **Radio**: licensed VHF/UHF (reliable, long range, requires license) or unlicensed 900 MHz spread-spectrum (shorter range, no license). The classic SCADA medium for geographically dispersed utilities.
- **Cellular**: 4G LTE / NB-IoT modems. Cheap, ubiquitous, but introduces a dependency on a carrier network (coverage, subscription, latency).
- **Microwave**: point-to-point directional links for high-bandwidth backbone routes.
- **Fiber optic**: highest bandwidth and reliability, but requires physical cable installation — only economic for high-value sites or in-plant networks.

### Worked Example: RTU Poll Rate

A water utility SCADA system supervises **50 remote pump stations**. Each station has one RTU reporting **32 analog values** (suction pressure, discharge pressure, flow rate, tank level, motor amps, etc.), each digitized to **16-bit resolution** (2 bytes). The MTU polls every station every **5 seconds**. What is the minimum telemetry data rate, and what modem speed is needed?

**Step 1 — Payload per RTU per poll:**

```
32 values × 2 bytes/value = 64 bytes of analog data
```

**Step 2 — Total payload per poll cycle (all 50 RTUs):**

```
64 bytes/RTU × 50 RTUs = 3,200 bytes per 5-second cycle
```

**Step 3 — Raw bit rate (payload only):**

```
3,200 bytes × 8 bits/byte = 25,600 bits per 5-second cycle
25,600 bits ÷ 5 s = 5,120 bps   ← raw payload rate
```

**Step 4 — Add protocol overhead:** The Modbus RTU frame (address + function + data + CRC) adds ~5 bytes overhead per register block. A realistic poll/response exchange for 32 registers adds ~10 bytes for the request frame and ~10 bytes of response framing/CRC overhead per RTU:

```
overhead per RTU ≈ 20 bytes → 20 × 50 = 1,000 bytes overhead per cycle
total = 3,200 + 1,000 = 4,200 bytes/cycle
4,200 × 8 ÷ 5 = 6,720 bps   ← with framing
```

Turnaround delay between poll and response (typical 50-100 ms per RTU on a serial multi-drop link) consumes a significant fraction of the cycle at low speeds: 50 RTUs × 50 ms = 2.5 s of dead time in a 5 s cycle — tight. In practice you either poll less frequently, poll in parallel across multiple sub-channels, or upgrade the link.

**Step 5 — Select modem speed:** A 9600 bps modem (the slowest standard serial speed used in legacy SCADA) provides ~6,720 bps usable after accounting for the turnaround margins above — barely adequate for this load at a 5 s poll rate. A 19,200 bps or 38,400 bps link provides comfortable headroom. Modern Ethernet/TCP-based systems (Modbus TCP, DNP3 over LAN) make this calculation moot — a 100 Mbps link handles thousands of tags per second — but legacy radio and serial SCADA systems still live and die by this arithmetic.

**Takeaway**: The poll rate is not free. Doubling the number of RTUs, doubling the tags per RTU, or halving the poll interval all double the required bandwidth. SCADA engineers size the communication link for the *peak* aggregate load, not the average, and leave 50% headroom for future expansion.

## Communication Protocols

The protocol defines how the MTU and field units encode their conversation. Four protocols dominate industrial SCADA:

### Modbus RTU (serial)

The oldest and simplest. Developed by Modicon in 1979 for PLC communication. **Master-slave** over RS-485 multi-drop serial. The master sends a request (read holding register, write coil); the addressed slave responds. Frame = slave address (1 byte) + function code (1 byte) + data + CRC-16 (2 bytes). No timestamps, no event-driven reporting, no built-in security — just a deterministic register read/write protocol. Ubiquitous because every industrial device on earth supports it. Speed: 1,200 to 115,200 bps, typically 9,600 or 19,200 bps.

### Modbus TCP

Modbus RTU encapsulated in TCP/IP and sent over Ethernet. Same register/coil data model, no CRC (TCP's checksum replaces it). Uses port 502. Faster (100 Mbps+ Ethernet), supports multiple masters, and rides on standard IT network infrastructure. Still no built-in security (authentication is optional and rarely configured).

### DNP3 (Distributed Network Protocol)

The standard for **electric utility** SCADA in North America and many other regions. Designed for the realities of remote telemetry: **event-driven with timestamps**. A DNP3 field unit can report "analog input 3 changed from 72.4 to 73.1 at 14:03:22.517" without being polled — the MTU receives a timestamped event it can reconstruct in exact chronological order even if the link was down when the event occurred (the RTU buffers events and replays them on reconnect). Supports classes of data (class 0 = all, class 1/2/3 = prioritized event queues). More complex than Modbus but far better suited to wide-area utility SCADA where communication is intermittent.

### OPC UA (Unified Architecture)

The modern, platform-independent industrial interoperability standard. Unlike the wire-protocol-focused Modbus/DNP3, OPC UA defines a rich information model: every data point carries metadata (engineering unit, range, alarm limits, data type). Built-in security (X.509 certificates, signing, encryption). Runs over TCP. The standard for **plant-floor integration** — connecting PLCs, HMIs, historians, MES, and ERP systems within a site where high bandwidth and rich data semantics matter more than minimal-overhead telemetry.

### Protocol Comparison Table

| Protocol | Medium | Typical Speed | Topology | Data Model | Timestamps | Security | Typical Application |
|----------|--------|---------------|----------|------------|------------|----------|---------------------|
| Modbus RTU | RS-485 serial | 9.6–115 kbps | Multi-drop (master-slave) | Registers / coils | No | None | In-plant PLC-to-PLC, simple field I/O |
| Modbus TCP | Ethernet | 100 Mbps+ | Star / any IP topology | Registers / coils | No | Optional (rare) | Plant LAN, PLC-to-HMI, building automation |
| DNP3 | Serial, radio, Ethernet | 9.6 kbps–10 Mbps | Master-slave / multi-master | Objects (analog, binary, counter) | Yes (event-driven) | Optional (authentication v5) | Electric/water utility wide-area SCADA |
| OPC UA | Ethernet / IP | 100 Mbps+ | Client-server / publish-subscribe | Rich objects with metadata | Yes | Built-in (certs, signing, encryption) | Plant integration, MES/ERP, IIoT |

**Selection rule of thumb**: Modbus for simple in-plant links where every device supports it and cost matters; DNP3 for geographically dispersed utility SCADA where event timestamps and outage buffering are essential; OPC UA for high-value plant integration where semantic data models and security are required.

## Telemetry: What Gets Sent

The SCADA system carries three categories of process data from field to MTU:

**Analog process variables** — continuously varying measurements: temperature (thermocouple or RTD via 4-20 mA transmitter), pressure, flow rate (from a magnetic or vortex flow meter), level (from a pressure or ultrasonic transmitter), motor current, voltage, frequency. Each analog value arrives as a 16-bit integer representing a scaled engineering value (e.g., 0-100% level, or 0-1000 kPa pressure). The MTU applies the scaling to display engineering units.

**Digital states** — on/off conditions: pump running, valve open, auto/manual mode, circuit breaker closed, level switch tripped, fault present. Each digital state is one bit. A single 16-bit register can carry 16 digital states — efficient for packing many discrete signals into one poll.

**Accumulator (counter) values** — running totals: totalized flow (m³ since last reset), energy (kWh), run-hours, event counts. These are typically 32-bit unsigned integers, polled periodically and reset by the MTU after recording the total for the period.

**Data concentration strategies**: Rather than polling every individual instrument, the RTU/PLC concentrates all local data and presents a single block to the MTU. The MTU requests "holding registers 40001-40032" and gets all 32 analog values in one Modbus response frame — far more efficient than 32 separate requests. Exception reporting (DNP3, or Modbus with a polling optimizer) skips values that haven't changed, reducing bandwidth on slow radio links.

## Historical Trending

The **process historian** is the MTU's long-term memory. It is what separates SCADA from a bare HMI: an HMI shows you *now*; SCADA shows you *now and the last five years*.

**Time-series storage**: Every tag (analog value or digital state) is sampled at a configurable rate (typically 1 second for critical loops, 1 minute for slowly-varying values) and written to disk with a timestamp. Modern historians use compressed columnar storage — a full year of 1-second data for 10,000 tags fits in tens of gigabytes, not terabytes.

**Trend display**: The operator selects a tag (or several) and a time range. The historian returns the data points and the HMI renders a strip-chart: time on the X-axis, engineering value on the Y-axis, with zoom and pan. Multiple tags overlay on the same chart for correlation (e.g., "did the pressure spike when the flow dropped?").

**Analysis applications**:

- **Efficiency accounting**: total steam consumed vs. total product produced over a shift; heat-rate calculations for power generation.
- **Anomaly detection**: a trend that drifts gradually over weeks (heat exchanger fouling, filter clogging) is invisible on a real-time screen but obvious on a 30-day trend.
- **Predictive maintenance**: bearing vibration trends, motor current signatures, and run-hour accumulation trigger maintenance before failure. This is the foundation of condition-based maintenance — fix it when the trend says it's degrading, not on a fixed calendar schedule.

See [energy.steam-turbines](../energy/steam-turbines.md): the AGC (Automatic Generation Control) telemetry link mentioned there — "remote setpoint from grid dispatch center adjusts turbine load in real-time to match system demand, requires telemetry link (serial communication or SCADA)" — *is* the SCADA system this article describes. The turbine governor's speed/load control is local; the SCADA system supervises it from the dispatch center.

## Alarm Management

An alarm is the SCADA system's way of demanding operator attention. The discipline of alarm management — deciding what alarms, how it's prioritized, and how the operator interacts — is a safety-critical engineering task, governed by standards (ISA-18.2, EEMUA 191).

**Priority levels**: Every alarm is assigned a priority — typically three tiers:

- **Critical** (red): immediate operator action required to prevent injury, equipment damage, environmental release, or production loss. Examples: turbine trip, boiler drum low-low level, emergency-shutdown signal.
- **Warning** (yellow): prompt operator action required to prevent the condition from escalating to critical. Examples: tank level high (not yet high-high), bearing temperature rising, backup pump failed to start.
- **Info** (blue/cyan): awareness only — no action required, but the operator should know. Examples: pump switched to standby, filter replacement due, manual mode selected.

**Alarm floods**: The cardinal sin of SCADA design. When a single upstream disturbance (a unit trip, a power blip) generates hundreds of alarms in seconds, the operator is overwhelmed and cannot find the root cause in the noise. ISA-18.2 explicitly addresses this: alarm rationalization should limit the system to ~1 alarm per 10 minutes per operator during normal operation and ~10 alarms per 10 minutes during an upset. Every alarm should be **unique, actionable, and auditable** — if the operator can do nothing about it, it should not be an alarm.

**Alarm states and the operator's job**: An alarm transitions through states:

```
  NORMAL ──condition crosses threshold──> UNACKED-ACTIVE (annunciate!)
                                              │
                                  operator acknowledges
                                              │
                                              ▼
                                       ALARM-ACKED (still active,
                                        silenced, acknowledged)
                                              │
                                    condition returns to normal
                                              │
                                              ▼
                                  UNACKED-RETURNED (needs ack
                                        to clear from banner)
                                              │
                                  operator acknowledges
                                              │
                                              ▼
                                         NORMAL (cleared
                                          from active list)
```

**Shelving**: An operator can temporarily suppress (shelve) a nuisance alarm — a known-bad transmitter that chatters, or a device under maintenance — for a fixed period (e.g., 30 minutes) after which it automatically un-shelves. Shelving is logged; it must not be used as a permanent fix.

**Alarm rationalization**: The process of reviewing every potential alarm and deciding: does it deserve to be an alarm? what priority? what are the operator's response actions? A well-rationalized system has fewer, more meaningful alarms. Most legacy SCADA systems have far too many alarms because every threshold was configured without asking "will the operator actually do something?"

## IT/OT Cybersecurity — A Brief Awareness

SCADA systems were historically **air-gapped** — physically disconnected from the office IT network and the internet. That assumption is no longer reliably true: remote access for vendor support, integration with enterprise systems (MES, ERP), and IIoT connectivity have bridged the air gap. High-profile incidents (Stuxnet 2010, Ukraine power grid 2015) demonstrated that industrial control systems are attack targets with physical consequences.

Defensive measures, in increasing order of rigor:

- **Network segmentation**: separate the control network (OT) from the office network (IT) with a firewall; restrict traffic to only what is necessary.
- **DMZ**: a buffer zone between OT and IT where historians, OPC servers, and jump hosts live — neither fully inside the control network nor exposed to the office.
- **Unidirectional gateways** (data diodes): hardware that physically permits data flow in only one direction (control network → enterprise), making it impossible for an attacker to reach the PLCs from the enterprise side. Used in high-security environments (nuclear, critical infrastructure).
- **Protocol security**: prefer OPC UA (built-in encryption/authentication) over bare Modbus TCP (none); configure DNP3 Secure Authentication v5 where supported.
- **Patch and harden**: the control-room servers and PLCs run for years without patches (you cannot reboot a running plant), which means known vulnerabilities accumulate. Hardening (disabling unused services, changing default passwords, restricting physical and remote access) is the primary practical defense.

This is a brief awareness only — IT/OT cybersecurity is a discipline unto itself. The key principle: **treat the SCADA network as a safety system**, not as a branch of the office network.

## Relationship to Sibling Articles

This article owns the **supervisory/aggregation layer**: the MTU, telemetry protocols, historian, and plant-wide alarm management. It does not re-teach:

- **PLC hardware and programming** — the Level-2 field controller executing deterministic logic. See [industrial-control.plc](industrial-control.plc.md). The PLC is what SCADA supervises.
- **Operator screen design, color coding, faceplates, local alarm banners** — the HMI layer. See [industrial-control.hmi](industrial-control.hmi.md). The MTU *runs* HMI software, but the screen-design discipline lives in the HMI article.
- **Embedded-system substrate** (MCU, RTOS, watchdog, interrupt handling) that the RTU/PLC hardware is built from. See [computing.embedded-systems](../computing/embedded-systems.md).
- **Control-circuit logic** (relay/ladder/sequential) that the PLC executes. See [control-circuits](control-circuits.md).

The [semiconductor-devices](semiconductor-devices.md) capability provides the silicon — microcontrollers, ADCs/DACs, communication transceivers — on which the RTU, PLC, and MTU hardware are all built.

---


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
