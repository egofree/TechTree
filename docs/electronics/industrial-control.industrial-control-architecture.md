# Industrial Control Architecture

> **Node ID**: electronics.industrial-control.industrial-control-architecture
> **Domain**: [Electronics](index.md)
> **Dependencies**: `electronics.industrial-control`, `electronics.industrial-control.plc`, `electronics.industrial-control.scada`, `electronics.industrial-control.hmi`

This article is the **integration tier**. It does not teach the [PLC](industrial-control.plc.md), the [SCADA system](industrial-control.scada.md), the [HMI](industrial-control.hmi.md), the [relay panel](control-circuits.relay-logic.md), the [ladder notation](control-circuits.ladder-logic.md), the [variable-frequency drive](power-conversion-circuits.vfd-motor-control.md), the [field sensor](interface-circuits.sensor-circuits.md), or the [analog-to-digital converter](interface-circuits.adc-circuits.md) — each of those has its own deep article. This article teaches **how they fit together**: the ISA-95 hierarchy that places every device at its correct level, the sensor-to-actuator control chain that every loop follows, the response-time budget that dictates which technology handles which signal, the safety layering that keeps people alive when the controller fails, and the communication hierarchy that moves data from a millivolt thermocouple up to a production schedule. Read this article to understand the *architecture*; follow the cross-links for any component you need to design in detail.

## The ISA-95 / Purdue Hierarchy

The recurring problem of industrial control is that a plant contains devices that operate on wildly different timescales — a power-electronics switch turns off in a microsecond, a PLC solves its logic in ten milliseconds, a SCADA historian logs once a second, and a production scheduler issues a new plan once a shift. Trying to mix these on one network or in one program produces a tangled, unmaintainable, unsafe system. The solution, formalized as the **ISA-95** standard (derived from the Purdue Enterprise Reference Architecture developed for Computer Integrated Manufacturing in the 1990s), is to **layer** the plant into levels, each with its own devices, its own timescale, its own network, and a defined interface to the level above and below.

```
    THE ISA-95 / PURDUE HIERARCHY

    +-------------------------------------------------------------------+
    |  LEVEL 4 — BUSINESS PLANNING & LOGISTICS                          |
    |  (Enterprise / ERP)                                               |
    |  - Production schedules, orders, inventory, accounting            |
    |  - Timescale: minutes to days to months                           |
    |  - Network: corporate WAN / IT network                            |
    |  - Example: SAP schedule says "10,000 cases of cola today"        |
    +-------------------------------------------------------------------+
                                  ^  production orders
                                  v  actual production counts
    +-------------------------------------------------------------------+
    |  LEVEL 3 — MANUFACTURING OPERATIONS MANAGEMENT                    |
    |  (SCADA, MES, historian, batch control)                           |
    |  - Supervises many cells/lines, logs trends, raises alarms        |
    |  - Timescale: seconds to minutes                                  |
    |  - Network: plant LAN (Ethernet), OPC UA                          |
    |  - Example: SCADA MTU polls 40 PLCs, logs fill-count trend,      |
    |             raises low-fill alarm, ships daily report to ERP      |
    +-------------------------------------------------------------------+
                                  ^  supervisory commands / setpoints
                                  v  aggregated process data
    +-------------------------------------------------------------------+
    |  LEVEL 2 — MONITORING & SUPERVISING (local control)               |
    |  (PLC, local control loops, RTU)                                  |
    |  - Executes deterministic control logic on its own I/O            |
    |  - Timescale: milliseconds (one PLC scan)                         |
    |  - Network: fieldbus to I/O, industrial Ethernet to peers         |
    |  - Example: PLC runs ladder logic: if bottle-present AND         |
    |             fill-level < setpoint THEN open fill valve            |
    +-------------------------------------------------------------------+
                                  ^  discrete/analog commands
                                  v  raw sensor readings
    +-------------------------------------------------------------------+
    |  LEVEL 1 — SENSING & MANIPULATION (basic I/O)                     |
    |  (Signal conditioning, ADC/DAC, I/O modules)                      |
    |  - Converts physical signals to bits/words and back               |
    |  - Timescale: microseconds to milliseconds                        |
    |  - Network: backplane bus, local wiring                           |
    |  - Example: 24 V proximity pulse -> optocoupler -> input bit;     |
    |             4-20 mA level signal -> 250 Ω -> 1-5 V -> ADC -> word  |
    +-------------------------------------------------------------------+
                                  ^  drive signals
                                  v  raw electrical signals
    +-------------------------------------------------------------------+
    |  LEVEL 0 — THE PROCESS (field equipment)                          |
    |  (Sensors, actuators, motors, valves, heaters)                    |
    |  - The physical thing being controlled                             |
    |  - Timescale: continuous physical process                         |
    |  - Network: hardwired point-to-point, 4-20 mA loops               |
    |  - Example: photodetector sees a bottle; solenoid opens fill      |
    |             valve; conveyor motor turns at 1750 rpm                |
    +-------------------------------------------------------------------+
```

The key discipline of ISA-95 is **level separation**: each level talks only to its immediate neighbours through a defined interface, on its own timescale, over its own network. The ERP does not poll a photodetector. The PLC does not issue a purchase order. Violating the level boundaries — say, wiring a raw field signal straight into a business database, or letting a scheduler directly command a valve — is how brittle, dangerous, unmaintainable plants are built. The architecture's job is to enforce those boundaries and define the data that crosses each one.

Level 4 (business planning) is **out of scope** for electronics circuit design — it is the domain of IT and operations management. This article covers Levels 0 through 3, which is where the electronics and control engineering live, and notes the interface to Level 4 at the top.

## The Control Chain

Every automatic control loop, from the simplest relay latching circuit to the most elaborate SCADA-supervised process, follows the same chain of stages. The chain is the horizontal slice through the ISA-95 levels — it runs down through Levels 2-1-0 and back up:

```
    THE UNIVERSAL CONTROL CHAIN (follows every loop top-to-bottom):

    +----------+   physical    +----------------+   mA/V    +----------+
    |  PROCESS |<--------------|   ACTUATOR     |<---------| ACTUATOR |
    | (liquid  |   effect      | (motor, valve, |  command |  DRIVER  |
    |  in tank)|               |  heater)       |          |(DAC/VFD/ |
    +----------+               +----------------+          | starter) |
          ^                                                  +----------+
          |  physical                                               ^
          |  quantity                                               | drive
          |                                                         | signal
    +----------+   electrical   +----------------+   word/    +----------+
    |  SENSOR  |--------------->|   SIGNAL        |  bit  --->|CONTROLLER|
    |(thermocp,|   (mV, mA,     |  CONDITIONING  |           |(relay /  |
    | photo,   |    ohm, Hz)    | (amplify,      |           | PLC /    |
    | encdr)   |                |  filter, ADC)  |           | RTU)     |
    +----------+                +----------------+           +----------+
                                                                      ^
                                                                      | logic
                                                                      | solve
                                                           (scan cycle / event)
```

Reading the chain left-to-right-bottom-to-top, then back down:

1. **Sensor** (Level 0) converts a physical quantity (temperature, pressure, position, light, flow) into an electrical signal. A thermocouple produces millivolts; a photodetector changes resistance; an encoder produces pulse trains. The [sensor-circuits article](interface-circuits.sensor-circuits.md) teaches each family in depth.
2. **Signal conditioning** (Level 1) takes the raw electrical signal and turns it into a clean digital value the controller can use: amplify the millivolts, filter the noise, digitize via the [ADC](interface-circuits.adc-circuits.md). For a discrete sensor this is just an optocoupler input module; for an analog sensor it is an instrumentation amplifier plus an anti-alias filter plus a sampling ADC.
3. **Controller** (Level 2) reads the conditioned input and decides what to do. In the historical progression of this tech tree, the controller evolves from a [relay panel](control-circuits.relay-logic.md) (hard-wired boolean, no software) to a [PLC](industrial-control.plc.md) executing [ladder logic](control-circuits.ladder-logic.md) (software-reconfigurable, deterministic scan). The controller is where the "thinking" happens.
4. **Actuator driver** (Level 1) takes the controller's command — a bit, a word, a duty cycle — and converts it into the power signal the actuator needs. A relay output drives a contactor coil; a [DAC](interface-circuits.adc-circuits.md) produces an analog speed reference; a [variable-frequency drive](power-conversion-circuits.vfd-motor-control.md) synthesizes three-phase AC at the commanded frequency; a motor starter connects line power to the motor.
5. **Actuator** (Level 0) does the physical work: a motor turns, a valve opens, a heater warms. The actuator changes the process, the sensor measures the new process state, and the loop closes.

The chain is universal. A 1905 motorized conveyor with a relay panel, a 1975 CNC with a PLC, and a 2020 smart factory with an OPC-UA-connected edge gateway all follow the same five stages — only the implementation technology at each stage differs.

## Worked Example — Bottling Line Control Architecture

To make the hierarchy concrete, consider a soft-drink bottling line. The line fills, caps, and conveys bottles at 300 bottles/minute. Here is the full control architecture, traced from the field device up to the supervisory layer.

```
    BOTTLING LINE CONTROL ARCHITECTURE

    FIELD DEVICES (Level 0)            CONTROLLER (Level 2)
    ==========================         =========================================
    bottle-present  ----(24V)----+     |  PLC (Allen-Bradley CompactLogix)     |
    photodetector                +---->|  I/O: 32 DI / 16 DO / 8 AI / 4 AO      |
    fill-level sensor --(4-20mA)-+---->|  Scan: 5 ms                           |
    cap-present sensor --(24V)---+     |  Program: ladder logic (LD) + ST      |
    conveyor encoder --( pulses)-+     |                                       |
                                       |  Rungs (executed every scan):         |
    ACTUATORS (Level 0)                |   1. conveyor_run := start AND        |
    ==========================         |        estop_ok AND door_closed       |
    conveyor motor   <----(VFD)---+    |   2. fill_valve := bottle_present     |
    (3 kW, 460V)                  |    |        AND (level < setpoint)         |
    fill solenoid    <---(DO)-----+----|   3. cap_press := cap_present AND     |
    valves (x8)                   |    |        conveyor_stopped               |
    cap press cyl.   <---(DO)-----+    |   4. vfd_speed := 1750 * rate_cmd     |
    (pneumatic)                   |    |   ...                                  |
                                 +<-----------(AO 0-10V speed ref)-----------+
                                 +<-----------(DO relay contact)-------------+
                                 +<-----------(DO relay contact)-------------+

    ACTUATOR DRIVERS (Level 1)         SIGNAL CONDITIONING (Level 1)
    ============================       =========================================
    VFD (480V, 5hp) -----> conveyor    24V DI: optocoupler + 5ms debounce
        receives 0-10V speed ref,      4-20mA AI: 250 Ω -> 1-5 V -> 16-bit ADC
        synthesizes 3-phase AC         encoder: high-speed counter card (DI pulse
        at commanded Hz                @ 100 kHz)
    Solenoid drivers (relay out):      AO: 16-bit DAC -> 0-10 V, 0.5 ms settling
        PLC DO ----> relay ----> 24V
        to solenoid coil
    Cap press: PLC DO ----> relay ----> 120V to solenoid valve (pneumatic)

    SUPERVISORY (Level 3)              OPERATOR (Level 3/4 interface)
    ===========================        =========================================
    SCADA RTU polls PLC every 1 s      HMI (touch panel, 15" color)
    via EtherNet/IP:                   - line overview screen (pumps, conveyor,
      - reads: bottle count,             fill valves, animated)
        fill rate, low-fill count,     - alarm banner (red = unacknowledged)
        vfd speed, estop status,       - production-rate trend (5-min strip chart)
        alarm bits                     - setpoint entry keypad (fill level, line
      - writes: rate_cmd setpoint,       speed)
        recipe select                  - momentary START / STOP pushbuttons
    Historian logs all values           (commands gated by PLC permissives)
    every 1 s; 30-day trend.
```

Tracing one control loop in detail — **the fill loop**:

1. **Sensor**: a fill-level sensor in each filler head produces 4-20 mA proportional to liquid height (4 mA = empty, 20 mA = full).
2. **Signal conditioning**: the PLC's analog input module drops the 4-20 mA across a precision 250 Ω resistor to 1-5 V, filters it, and samples it with a 16-bit ADC every scan (5 ms). The PLC scales the raw count to engineering units (millilitres) via the configured scale.
3. **Controller**: a ladder rung computes `fill_valve := bottle_present AND (level < fill_setpoint)`. While the bottle is present and the level is below the setpoint, the rung is true. Every scan (5 ms), the logic re-evaluates — when the level crosses the setpoint, the rung goes false and the valve closes. The fill accuracy is bounded by the scan time plus the valve closing time: at 300 bottles/min the bottle is under the filler for 200 ms; a 5 ms scan plus a 20 ms valve-close gives ≤ 25 ms of overshoot, which at the fill rate corresponds to a few millilitres — the fill-level setpoint is trimmed to compensate.
4. **Actuator driver**: the fill-valve rung's coil drives a relay output module; the relay contact switches 24 V DC to the solenoid valve coil.
5. **Actuator**: the solenoid valve opens (pressurized product flows in) and closes (flow stops).
6. **Supervisory**: the SCADA RTU polls the PLC's bottle-count and low-fill-count registers once per second, logs them to the historian, and raises a low-fill alarm if the count exceeds a threshold over a rolling window. The HMI shows the running fill rate as a trend and lets the operator adjust the fill-level setpoint (which the PLC reads as a new value on the next scan).

This one loop exercises every level of the hierarchy: the field sensor (Level 0), the analog input conditioning (Level 1), the PLC scan solving the control logic (Level 2), the SCADA polling and historian (Level 3), and the HMI display and setpoint entry (Level 3/4). The architectural discipline is that each level minds its own timescale: the PLC does not wait for the SCADA poll, the SCADA does not solve the fill logic, the HMI does not directly command the valve.

## Response-Time Hierarchy

The reason the architecture is layered is that **each level operates on a different timescale**, and matching the technology to the timescale is what makes the system deterministic and reliable. The table below shows the typical response time at each level. A signal that needs a faster response than a level can provide must be handled at a lower level; a signal that is polled faster than necessary wastes bandwidth and CPU.

| Level | Component | Response Time | Example Signal |
|-------|-----------|---------------|----------------|
| 0 | Sensor / actuator (physical) | μs - ms | Photodetector pulse; valve open/close |
| 0 | Actuator physics | ms - s | Motor spin-up; liquid level rise |
| 1 | Signal conditioning (ADC) | μs - ms | ADC conversion (10-100 μs SAR) |
| 1 | Input debounce filter | 3 - 10 ms | Limit switch bounce rejection |
| 2 | PLC scan cycle | 1 - 50 ms | Ladder logic solve (fill valve rung) |
| 2 | VFD speed update | 1 - 10 ms | PWM duty cycle (current loop) |
| 2 | Relay output operate | 5 - 15 ms | Contactor coil energize |
| 3 | SCADA RTU poll cycle | 1 - 60 s | Plant-wide data collection |
| 3 | Historian log interval | 1 s | Trend sample storage |
| 4 | HMI screen refresh | 100 ms - 1 s | Operator display update |
| 4 | ERP production schedule | minutes - days | Daily order plan |

The architecture's rule: **each level must respond faster than the level above it needs data, and slower than the level below it provides data.** The PLC's 5 ms scan is much faster than the SCADA's 1 s poll (so the SCADA always sees fresh data) and much slower than the ADC's 10 μs conversion (so the input value is always settled when the PLC reads it). Violate this ordering and the system breaks: if the PLC scan were slower than the SCADA poll, the SCADA would read stale data; if the ADC were slower than the scan, the input would be mid-conversion when read.

### Response-Time Budget Worked Example

For the bottling-line fill loop, the worst-case response to a level reaching the setpoint is:

```
    Event: liquid level crosses fill_setpoint
      |
      v
    Level sensor (4-20 mA):              continuous, ~0 ms delay
    AI module ADC conversion:             +0.1 ms (16-bit SAR)
    PLC scan waits to read input image:   +0..5 ms (next phase-1 read)
    PLC logic solve (fill rung):          +<0.1 ms (one rung)
    PLC waits to write output image:      +0..5 ms (next phase-3 write)
    Relay output operate:                 +10 ms (mechanical relay)
    Solenoid valve close:                 +15 ms (pneumatic pilot + poppet)
    --------------------------------------------------------------
    Worst-case total:  ~30 ms from level-cross to valve-closed
```

At a fill rate of 50 ml/s, 30 ms of overshoot = 1.5 ml of overfill — acceptable for a 500 ml bottle (0.3 %). If tighter accuracy were needed, the relay output (10 ms) could be replaced with a transistor output (0.1 ms) and the solenoid with a faster proportional valve, cutting the budget to ~10 ms and the overfill to ~0.5 ml. This is the kind of trade-off the architecture makes explicit: the control chain's total response time is the **sum** of every stage's delay, and the slowest stage dominates.

## Integration Principles

Three principles govern how the pieces combine into a working, safe, maintainable plant.

### 1. Determinism — the PLC Scan vs the PC Event Model

The central architectural choice in industrial control is **deterministic polling over event-driven reaction**. A PLC does not wait for an interrupt; it [scans](industrial-control.plc.md) every input, solves every rung, drives every output, and repeats — on a fixed cycle. The response time to any input is therefore bounded by (at most) two scans, always predictable, always the same. A general-purpose computer running the same logic as an event-driven program cannot make that guarantee: the operating system may be busy with disk I/O, garbage collection, or a network stack when the input arrives, and the latency is unbounded.

This is why the PLC owns Level 2 (the control loop) and the PC owns Level 3/4 (supervision and planning). The SCADA PC, the HMI, the historian, the ERP — none of them are trusted to close a safety-critical loop, because none of them can guarantee a response deadline. The architecture enforces this: control logic lives in the PLC; supervision and display live above it; the interface between them is a poll, not a shared variable. If the SCADA PC crashes, the PLC keeps controlling the plant on its own (in "local" or "last-setpoint" mode); if the PLC crashes, the plant must fail safe (see below). The hierarchy is also a fault hierarchy: each level degrades gracefully without the level above.

### 2. Safety Layers — Hardwired, Outside the PLC

The most important architectural rule for personnel safety is that **the emergency-stop and safety interlock chain is hardwired, outside the PLC, and independent of the controller software.** A software-only safety — "the PLC will stop the motor when the light curtain is broken" — fails dangerously if the PLC hangs, the I/O module shorts, the program has a bug, or the output relay welds shut. The architecture therefore provides a **parallel hardwired safety chain** that removes power from the actuators regardless of what the PLC does:

```
    SAFETY CHAIN (hardwired, independent of PLC):

       +24V ---[ E-STOP btn ]---[ DOOR SW ]---[ LIGHT CURTAIN ]
                                                       |
                                                       v
                                              +----------------+
                                              | SAFETY RELAY   |
                                              | (monitors the  |
                                              |  chain, forces  |
                                              |  drop-out if    |
                                              |  any opens or   |
                                              |  a wire breaks) |
                                              +----------------+
                                                       |
                          +----------------------------+----------------------------+
                          |                            |                            |
                          v                            v                            v
                   Motor contactor              Solenoid power            VFD enable
                   coil power                   bus contactor             (STO input)
                   (removes motor               (closes all                (stops VFD
                    line power)                  fill valves)               output)
```

The safety chain runs through every emergency stop button, every guard-door switch, every light curtain, and every two-hand control in series. If any opens — or if a wire breaks (the safety relay pulses a test signal and detects opens) — the safety relay drops out and physically removes power from the motor contactors, the solenoid bus, and the VFD's Safe-Torque-Off (STO) input. The PLC cannot override this; the PLC's output relay may be welded closed and the motor still stops, because the contactor coil has no power. This is the principle of **safety by hardware, not software**.

Safety integrity is quantified by **SIL (Safety Integrity Level)**, defined in IEC 61508 and IEC 62061 (machinery safety). SIL 1 through SIL 4 specify the probability of failure on demand (PFD) and the risk-reduction factor. Most machinery safety operates at SIL 1-2 (PFD 10⁻¹ to 10⁻²); process-industry burner and emergency-shutdown systems target SIL 3 (PFD 10⁻³). A SIL-rated safety relay, safety PLC, or safety network (CIP Safety, PROFIsafe) achieves the level through redundant channels, diagnostic coverage, and proven-in-use components. The architecture's job is to identify each safety function, assign it a SIL target from the risk assessment, and implement it with hardware rated to that SIL — independently of the basic process control system.

### 3. Communication Hierarchy — Fieldbus, Ethernet, WAN

Each ISA-95 level has its own communication network, matched to its timescale and distance:

```
    COMMUNICATION HIERARCHY (bottom to top):

    Level 0-1:  HARDWIRED point-to-point
                4-20 mA current loops, 24 V DI/DO, thermocouple millivolts
                Distance: meters. Speed: instantaneous (DC).
                Why: each field device gets its own wire; no protocol overhead.

    Level 1-2:  FIELDBUS (PLC <-> remote I/O, drives, smart instruments)
                Modbus RTU (RS-485, 9.6-115 kbps)
                PROFIBUS DP (RS-485, up to 12 Mbps)
                DeviceNet, AS-i
                Distance: hundreds of meters. Speed: ms-cycle.
                Why: serial bus replaces many home-run wires; one cable to
                a remote I/O drop serves 32 local points.

    Level 2-3:  INDUSTRIAL ETHERNET (PLC <-> PLC, PLC <-> SCADA)
                Modbus TCP, EtherNet/IP, Profinet, EtherCAT
                Distance: plant-wide (switched Ethernet). Speed: sub-ms to ms.
                Why: high bandwidth, standard IT infrastructure, cross-vendor
                interoperability via OPC UA information model.

    Level 3-4:  ENTERPRISE NETWORK (SCADA/MES <-> ERP)
                OPC UA, MQTT, REST/HTTP over corporate WAN
                Distance: global. Speed: seconds to minutes.
                Why: business systems need structured data with metadata
                (engineering units, alarm limits, timestamps), not raw bits.
```

The hierarchy is also a **security boundary**. The fieldbus (Level 1-2) is electrically isolated and physically contained. The industrial Ethernet (Level 2-3) is a dedicated plant LAN, separated from the corporate IT network by a firewall or data diode — the so-called **IT/OT (Information Technology / Operational Technology) split**. The principle is that a compromised business network must not be able to reach the PLCs. Historically this was enforced by an "air gap" (no physical connection at all); modern integrated plants use a DMZ with tightly controlled one-way data flows (historian data up, no commands down). The [SCADA article](industrial-control.scada.md) covers the protocols and the cybersecurity awareness in more depth.

## How the Articles Fit Together

This article is the synthesis layer. Each component of the architecture is taught in depth in its own article; here is where each fits in the ISA-95 model and the control chain:

| Article | Role | ISA-95 Level | Position in Control Chain |
|---------|------|--------------|---------------------------|
| [Relay Logic Circuits](control-circuits.relay-logic.md) | Hard-wired boolean controller (historical) | 2 | Controller (pre-PLC) |
| [Ladder Logic Design](control-circuits.ladder-logic.md) | The programming notation PLCs execute | 2 | Controller (programming) |
| [PLC Design](industrial-control.plc.md) | The deterministic controller platform | 2 | Controller (hardware) |
| [SCADA System Design](industrial-control.scada.md) | Supervisory polling + historian | 3 | Supervisory layer |
| [HMI Design](industrial-control.hmi.md) | Operator display + command | 3/4 | Operator interface |
| [VFD Motor Control](power-conversion-circuits.vfd-motor-control.md) | Variable-speed actuator driver | 1 | Actuator driver (motor) |
| [Sensor Circuits](interface-circuits.sensor-circuits.md) | Field measurement | 0 | Sensor |
| [ADC Circuits](interface-circuits.adc-circuits.md) | Signal digitization | 1 | Signal conditioning |

The progression through these articles mirrors the historical and pedagogical progression of industrial control itself. The [relay panel](control-circuits.relay-logic.md) is the original Level-2 controller — boolean logic in hardware, inflexible but robust. [Ladder logic](control-circuits.ladder-logic.md) is the notation invented so that relay electricians could read the new software-driven controllers. The [PLC](industrial-control.plc.md) is that software-driven controller — the same logic, reconfigurable from a laptop, executing on a deterministic scan. [SCADA](industrial-control.scada.md) and the [HMI](industrial-control.hmi.md) are the layers above — turning isolated controllers into a supervised, observable, operable plant. This article ties them together with the architecture that structures the whole.

## See Also

- [Industrial Control](industrial-control.md) — parent capability: the design-pedagogy hub for PLC, SCADA, HMI, and integrated control architecture.
- [PLC Design](industrial-control.plc.md) — the Level-2 controller: rack/CPU/I/O hardware, scan cycle, memory model, IEC 61131-3 languages, industrial communication. The core of any modern architecture.
- [SCADA System Design](industrial-control.scada.md) — the Level-3 supervisory layer: MTU/RTU hierarchy, telemetry polling, protocols, historian, alarm management.
- [HMI Design](industrial-control.hmi.md) — the operator interface: screen design, alarm display, trending, permissives, the human side of the control room.
- [Relay Logic Circuits](control-circuits.relay-logic.md) — the hardware-logic precursor to the PLC; seal-in latches, motor starters, interlocks, the relay panel the PLC replaced.
- [Ladder Logic Design](control-circuits.ladder-logic.md) — the IEC 61131-3 ladder notation PLCs execute; contacts, coils, timers, counters, the scan model.
- [VFD Motor Control](power-conversion-circuits.vfd-motor-control.md) — the variable-frequency drive: rectifier → DC bus → inverter, V/f and vector control, the actuator driver for every variable-speed motor.
- [Sensor Circuits](interface-circuits.sensor-circuits.md) — the field-measurement front end: thermistors, RTDs, strain gauges, Hall sensors, signal conditioning for each.
- [ADC Circuits](interface-circuits.adc-circuits.md) — sampling, quantization, SAR/flash/sigma-delta architectures; the Level-1 digitization that feeds the controller.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
