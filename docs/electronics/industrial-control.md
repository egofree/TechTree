# Industrial Control

> **Node ID**: electronics.industrial-control
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`computing.embedded-systems`](../computing/embedded-systems.md)
> **Enables**: None
> **Timeline**: Years 30-55
> **Outputs**: industrial-control-system
> **Critical**: No — industrial-control architecture integrates existing computing and control-circuit capabilities into system-level platforms (PLC/SCADA/HMI); it organizes integration knowledge rather than gating a primary bootstrap dependency

## Overview

Industrial control is the system-architecture layer that orchestrates factories and process plants: programmable logic controllers (PLCs) execute control logic, supervisory control and data acquisition (SCADA) systems aggregate and supervise across sites, and human-machine interfaces (HMIs) give operators visibility and command. This capability is the **design pedagogy** layer for integrating these platforms into a coherent control architecture — progressing from the single PLC up to distributed supervisory systems.

The PLC is the foundation. Invented in 1968 (Bedford Associates / Modicon 084) to replace hard-wired relay panels in General Motors' automotive plants, the PLC is a rack-mounted industrial computer that executes [ladder logic](control-circuits.ladder-logic.md) — the same rung-and-contact notation used for relay panels, now in software. Its defining properties are deterministic scan-cycle execution (read inputs → execute logic → write outputs, 1–100 ms), rugged construction (industrial temperature, vibration, EMI), and modular I/O (add digital, analog, or specialty cards as needed). Modern PLCs also support function block diagram (FBD), structured text (ST), sequential function chart (SFC), and instruction list (IL) — the five IEC 61131-3 languages.

SCADA sits above the PLC, polling data from multiple controllers over industrial networks (Modbus, Profibus, EtherNet/IP) and presenting a site-wide or regional view to operators. HMI is the local operator interface — typically a touchscreen panel connected to a single PLC or a small cell. Together, these layers turn isolated controllers into an observable, commandable system.

This capability owns the industrial-control platform and architecture as an electronics-systems discipline. It does not re-teach the embedded-computing substrate (MCU, RTOS, FPGA) — that lives in [computing embedded-systems](../computing/embedded-systems.md). It does not re-teach relay and ladder logic — that lives in [control circuits](control-circuits.md). It focuses on PLC programming models, SCADA topology, HMI design, and plant-wide architecture.

## Prerequisites

### Materials

- **PLC hardware** — a micro-PLC (Allen-Bradley Micro820 or Siemens S7-1200, 10–20 I/O) for bench; a mid-range PLC (Siemens S7-1500 or AB CompactLogix, 100–500 I/O) for cell-scale work.
- **I/O modules** — digital input (24 VDC sinking/sourcing), digital output (relay or transistor), analog input (0–10 V or 4–20 mA, 12–16 bit), analog output (0–10 V, 12 bit).
- **Communication modules** — Ethernet (Modbus TCP, EtherNet/IP), serial (Modbus RTU, RS-485), or fieldbus (Profibus DP, Profinet).
- **HMI panel** — 4–10 inch touchscreen (Siemens KTP, Allen-Bradley PanelView), or PC-based SCADA software (Ignition, Wonderware).
- **Sensors and actuators** — limit switches, proximity sensors, RTD/thermocouple transmitters, motor contactors, proportional valves. From [electrical systems](electrical-systems.md) and [interface circuits](interface-circuits.md).

### Tools and Equipment

- Programming PC with vendor software (Rockwell Studio 5000, Siemens TIA Portal, Codesys).
- Ethernet switch (industrial-rated, managed, for Profinet/EtherNet/IP).
- DMM and oscilloscope for field I/O troubleshooting.
- Modbus / fieldbus analyzer (for protocol debugging).

### Knowledge

- [Control circuits](control-circuits.md) — relay logic and ladder logic (the IEC 61131-3 LD language).
- [Computing: embedded systems](../computing/embedded-systems.md) — microcontroller architecture, RTOS concepts, interrupt handling.
- Process control fundamentals — PID tuning, feedback loop stability.

## Bill of Materials

| Component | Quantity (per cell-control system) | Source | Alternatives |
|-----------|-----------------------------------|--------|--------------|
| Mid-range PLC (Siemens S7-1200, CPU 1214C, 14 DI / 10 DO / 2 AI) | 1 | [Semiconductor devices](semiconductor-devices.md) | AB CompactLogix, Codesys softPLC |
| Signal module (8 DI, 24 V) | 2–3 | [Semiconductor devices](semiconductor-devices.md) | ET200 distributed I/O |
| Signal module (4 AO, 0–10 V) | 1 | [Semiconductor devices](semiconductor-devices.md) | PWM output + RC filter |
| HMI panel (7" touchscreen, KTP700) | 1 | [Semiconductor devices](semiconductor-devices.md) | PC-based SCADA (Ignition) |
| Industrial Ethernet switch (5-port, managed) | 1 | [Electrical systems](electrical-systems.md) | Unmanaged (no diagnostics) |
| 24 VDC power supply, 5 A (for I/O) | 1 | [Power supply circuits](power-supply-circuits.md) | 10 A for larger cells |
| DIN-rail enclosure, 400 mm | 1 | [Electrical systems](electrical-systems.md) | Free-standing cabinet |
| Shielded twisted-pair cable (Cat 5e industrial) | 50 m | [Electrical systems](electrical-systems.md) | Fiber (for long runs / EMI) |
| Sensor cable (shielded, 4-conductor, for 4–20 mA) | 100 m | [Electrical systems](electrical-systems.md) | Multicore (12-cond) for runs |

## Process Description

### Step 1: Select the PLC

Match the PLC to the application:
- **I/O count**: count every digital and analog point with 20% spare capacity.
- **Scan time requirement**: motor interlocking needs <10 ms; temperature control tolerates 100 ms.
- **Memory**: 1 KB ladder ≈ 50–100 rungs; size the program and leave 50% spare.
- **Communication**: does it need Ethernet, Modbus, or a fieldbus?

For a 50-point cell control with HMI, a Siemens S7-1200 CPU 1214C (14 DI + 10 DO + 2 AI built in) plus two 8-DI signal modules and one 4-AO module covers 30 DI / 10 DO / 2 AI / 4 AO — adequate with spares. *(Deep article: [PLC](industrial-control.plc.md))*

### Step 2: Wire the I/O

Wire digital inputs from limit switches and pushbuttons to the PLC's DI cards (24 V sinking or sourcing — pick one convention per system). Wire digital outputs (relay or transistor) to motor contactors, solenoid valves, and indicators. Wire analog inputs from 4–20 mA transmitters (temperature, pressure, flow) to AI cards. Terminate the shield at one end only (usually the PLC cabinet) to prevent ground loops. Label every wire at both ends.

### Step 3: Program the Logic

Write the control program in ladder logic (LD) or function block diagram (FBD). Structure it in sections: (1) E-stop and safety logic (highest priority, first scanned), (2) mode selection (auto/manual), (3) per-device interlocks and commands, (4) analog scaling and PID loops, (5) alarms and HMI interface. Use IEC 61131-3 conventions: `%I0.0` for inputs, `%Q0.0` for outputs, `%M0.0` for internal memory, `%IW0` for analog input words.

### Step 4: Configure the HMI

Design the HMI screens: a main overview showing machine state (running/stopped/faulted), a detail page per station with live values and setpoints, and an alarm page with active and historical alarms. Bind each HMI tag to the corresponding PLC variable over Ethernet (Profinet or EtherNet/IP). Keep screens simple — operators in a plant environment need large indicators and minimal text, not dense dashboards. *(Deep article: [HMI](industrial-control.hmi.md))*

### Step 5: Set Up SCADA Communications

For multi-controller systems, configure the SCADA host to poll each PLC over Modbus TCP or EtherNet/IP. Set poll rates appropriate to the data: 1 s for status bits, 100 ms for alarms, 5–60 s for historical trending. Configure data logging to a database (historian) for post-mortem analysis. *(Deep article: [SCADA](industrial-control.scada.md))*

### Step 6: Partition the Architecture

For a large plant, partition controllers by zone: one PLC per machine or process unit, networked to a supervisory layer. Define the network hierarchy: field level (sensors → PLC, hardwired), cell level (PLC ↔ PLC, industrial Ethernet), supervisory level (SCADA ↔ PLCs, Ethernet TCP/IP), enterprise level (MES/ERP, standard IT network). *(Deep article: [industrial-control-architecture](industrial-control.industrial-control-architecture.md))*

## Quantitative Parameters

### PLC Platform Comparison

| Parameter | Allen-Bradley CompactLogix 5380 | Siemens S7-1500 | Codesys softPLC |
|-----------|-------------------------------|----------------|-----------------|
| Max digital I/O | 96 (expandable to 256) | 256+ (ET200 distributed) | Unlimited (PC-based) |
| Scan time (typical program) | 1–5 ms | 0.5–2 ms | 1–10 ms (depends on PC) |
| Program memory | 4 MB | 500 KB – 5 MB | PC RAM limited |
| Analog resolution | 16 bit | 16 bit | Card-dependent |
| Native protocols | EtherNet/IP | Profinet | Modbus TCP, EtherNet/IP, Profinet |
| Programming software | Studio 5000 ($$$) | TIA Portal ($$) | Codesys (free IDE) |
| Vendor lock-in | High | High | Low (open standard) |
| Price (CPU base) | $1500–4000 | $800–3000 | Free + PC hardware |

### Industrial Communication Protocols

| Protocol | Physical layer | Max speed | Max distance | Max nodes | Topology |
|----------|---------------|-----------|-------------|-----------|----------|
| Modbus RTU | RS-232 / RS-485 | 115.2 kbaud | RS-485: 1.2 km | RS-485: 32 | Line (daisy chain) |
| Modbus TCP | Ethernet (Cat 5e) | 100 Mbit/s | 100 m (copper), km (fiber) | 254 (IP subnet) | Star, ring |
| Profibus DP | RS-485 | 12 Mbaud | 1 km (at 12 Mbaud: 100 m) | 126 | Line (daisy chain) |
| Profinet IRT | Ethernet (Cat 5e) | 100 Mbit/s | 100 m (copper) | 254 per subnet | Star, ring |
| EtherNet/IP | Ethernet (Cat 5e) | 100 Mbit/s – 1 Gbit/s | 100 m (copper) | Standard IP | Star, ring |
| CAN bus | Twisted pair | 1 Mbaud | 40 m (1 Mbaud), 1 km (50 kbaud) | 110 | Multi-master bus |
| HART | 4–20 mA loop (superimposed) | 1200 bit/s | Same as analog loop | 1–15 (multidrop) | Point-to-point / bus |

### HMI and SCADA Sizing

| System level | Typical I/O count | HMI type | Poll rate | Historian capacity |
|-------------|------------------|----------|-----------|-------------------|
| Single machine | 10–50 | 4" panel (KTP400) | 100 ms–1 s | 10 000 tags |
| Cell (multi-machine) | 50–500 | 7–10" panel (KTP700/PanelView) | 100 ms | 100 000 tags |
| Plant area | 500–5000 | PC SCADA (Ignition, Wonderware) | 100 ms (alarms), 5 s (logs) | 1 M+ tags |
| Site-wide / regional | 5000–50 000 | Server SCADA (redundant) | 1 s (status), 60 s (logs) | 10 M+ tags, 5+ yr history |

## Scaling Notes

- **Single-machine scale**: one micro-PLC (Siemens S7-1200 CPU 1211C, 6 DI / 4 DO / 2 AI built-in) with a 4" HMI. Handles 10–20 I/O. Program fits in 10 KB. Typical for a standalone packaging machine or pump skid.
- **Cell scale**: one mid-range PLC (S7-1500 or CompactLogix) with 3–5 I/O modules, a 7–10" HMI, and a single industrial Ethernet switch. Handles 100–500 I/O. Program 50–500 KB. Typical for a manufacturing cell or process unit.
- **Plant scale**: 10–100 PLCs networked to redundant SCADA servers over managed Ethernet. Handles 5000–50 000 I/O. Requires careful network segmentation (VLANs), cybersecurity (firewall, no direct internet), and a structured tag-naming convention (ISA-95 hierarchy: Enterprise/Site/Area/Cell/Unit/Control Module).
- **The integration bottleneck is not I/O count but architecture**: at 50+ PLCs, the challenge becomes naming conventions, change management, alarm rationalization, and cybersecurity. Poor architecture scales poorly — a flat Modbus poll of 100 PLCs saturates the master. Use hierarchical polling (local SCADA aggregates cell data; central SCADA polls aggregates).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| PLC digital input not reading the sensor | Wrong wiring (sinking vs sourcing mismatch), or sensor output below PLC threshold (24 V vs. 12 V) | Verify wiring convention (all inputs same direction); measure sensor output voltage at the PLC terminal; check PLC input LED |
| PLC analog input reads wrong value | Unscaled raw value (need engineering conversion), or 4–20 mA loop wiring broken | Scale in PLC: engineering = (raw − raw_min) / (raw_max − raw_min) × (eng_max − eng_min); measure loop current with DMM (expect 4–20 mA) |
| HMI cannot connect to PLC | Wrong IP address, subnet, or protocol; Ethernet cable crossed vs. straight; firewall blocking | Ping PLC from HMI PC; verify IP/subnet match; check protocol (Profinet vs EtherNet/IP) |
| PLC scan time exceeds limit (>20 ms) | Program too large, or PID / motion block takes too long | Profile the program (identify slow blocks); move fast logic to a high-priority task; optimize PID execution rate |
| Intermittent I/O faults / noise on analog | Ground loops, unshielded cable, or VFD EMI coupling into signal wires | Use shielded twisted pair; ground shield at one end only; route signal cables away from VFD motor leads (separate conduits); add ferrite chokes |
| SCADA data freeze / lagging | Poll rate too fast for network capacity, or too many tags on one poll cycle | Distribute polls across multiple tasks; increase poll rate for non-critical tags; use exception-based reporting (report on change) |

## Safety

- **Safety PLC vs standard PLC**: Do not use a standard PLC for safety-critical functions (E-stop, light curtain, safety door). Use a safety-certified PLC (SIL 2 or SIL 3 per IEC 61508) with redundant architecture and self-diagnostics. Safety functions must execute independently of the standard control.
- **Cybersecurity**: Modern PLCs and SCADA are network-connected and vulnerable. The Stuxnet worm (2010) demonstrated that industrial control systems are real targets. Air-gap the control network from the internet; enforce strong authentication on SCADA; patch PLCs per vendor security advisories; segment the network with firewalls (Purdue Model levels 0–5).
- **Arc flash in PLC cabinets**: PLC cabinets often share space with motor power wiring. The 480 VAC section is an arc-flash hazard (category 2+). Only qualified electricians should open energized power sections; PLC programming ports are typically in the low-voltage section.
- **Stored energy**: PLC output cards driving inductive loads (contactors, solenoids) can produce voltage spikes when de-energized. Add flyback diodes (DC loads) or MOVs (AC loads) across each coil to protect the output transistor.
- **Process safety interlocks**: Hard-wire critical interlocks (high-pressure trip, high-temperature trip) so they function even if the PLC fails. Do not rely solely on software logic for personnel safety.

## Quality Control

### Acceptance Criteria

- I/O checkout: every input and output verified end-to-end (activate field device → PLC reads it → HMI displays it → PLC commands output → field device actuates). Documented in a factory acceptance test (FAT) report.
- Scan time within design limit (typically <10 ms for machine control, <100 ms for process).
- Alarm rationalization: every alarm has a documented cause, consequence, and operator response. No "nuisance" alarms (alarms that trip during normal operation).
- Software version control: PLC program and HMI configuration under a versioned baseline before commissioning.

### Testing Methods

- **I/O simulation**: use a signal generator to inject known analog values (4 mA, 12 mA, 20 mA) and verify the PLC reads them correctly (scaled engineering units).
- **Forced I/O**: in the PLC programming tool, force inputs and outputs to test logic without field devices connected (use with caution — forces override field status).
- **FAT (Factory Acceptance Test)**: run the complete system at the integrator's shop with simulated I/O before shipment to site. The customer witnesses and signs off.
- **SAT (Site Acceptance Test)**: re-verify with real field devices after installation.

## Variations and Alternatives

### PLC vs DCS vs RTU

| System | Origin | Architecture | Best for | Example vendors |
|--------|--------|-------------|----------|----------------|
| PLC | Discrete manufacturing | Scanned logic, fast I/O | Machine control, high-speed sequencing | Allen-Bradley, Siemens, Mitsubishi |
| DCS (Distributed Control System) | Process industries (refining) | Controller-per-loop, peer network | Continuous process (temperature, pressure, flow) | Honeywell, Emerson, Yokogawa |
| RTU (Remote Terminal Unit) | Utilities / pipeline | Polling-based, remote | Geographically distributed assets (pipelines, water) | Schweitzer, ABB, Motorola |
| SoftPLC / IPC | Open-architecture | PC hardware, IEC 61131-3 runtime | Cost-sensitive, open-source | Codesys, Beckhoff, B&R |

The boundary is blurring: modern PLCs do continuous PID control; modern DCSs do sequencing. For a bootstrapping civilization, a PLC with analog I/O and PID blocks covers 90% of industrial control needs.

### Communication Protocol Selection

| Need | Protocol choice | Why |
|------|----------------|-----|
| Simple, 1 master, few slaves | Modbus RTU (RS-485) | Open, simple, ubiquitous, slow |
| Fast, deterministic, multi-master | Profinet IRT / EtherNet/IP | Industrial Ethernet; supports explicit and cyclic data |
| Interoperability across vendors | Modbus TCP | Lowest common denominator; every PLC supports it |
| Safety communication | PROFIsafe / CIP Safety | Black-channel approach; safety data piggybacks on standard protocol |
| Field instrument (4–20 mA + diagnostics) | HART | Analog signal + digital overlay; legacy but pervasive |

### IEC 61131-3 Programming Languages

The standard defines five languages for PLC programming. A given PLC may support any subset; most modern PLCs support at least LD and FBD:

| Language | Abbr | Form | Best for |
|----------|------|------|----------|
| Ladder Diagram | LD | Graphical (rung/contact/coil) | Relay-logic replacement, discrete sequencing |
| Function Block Diagram | FBD | Graphical (block wiring) | Process control, analog interlocks, re-usable function blocks |
| Structured Text | ST | Textual (Pascal-like) | Math, array processing, string handling |
| Sequential Function Chart | SFC | Graphical (state diagram) | Batch processes, state machines |
| Instruction List | IL | Textual (assembly-like) | Deprecated in IEC 61131-3 (Ed. 3); legacy only |

Most control programs mix languages: LD for discrete I/O and interlocks, FBD for PID loops, ST for recipe calculations, SFC for batch sequencing. The choice is per-section, not per-project.

### Analog Signal Standards in Industrial I/O

| Standard | Signal range | Live zero? | Wire count | Max distance | Notes |
|----------|-------------|-----------|-----------|-------------|-------|
| 4–20 mA current loop | 4–20 mA | Yes (4 mA) | 2 | 1+ km | Industry standard for process instruments; immune to voltage drop |
| 0–10 V voltage | 0–10 V | No | 2 (or 3 with shield) | ~100 m | Simpler, but voltage drop limits distance |
| 0–5 V voltage | 0–5 V | No | 2 | ~10 m | Board-level / short runs |
| Thermocouple (type K) | −10 to +40 mV | N/A | 2 (extension) | Short (cold junction at PLC) | Needs CJC; measures temperature directly |
| RTD (Pt100) | 100–138.5 Ω (0–100 °C) | N/A | 2, 3, or 4 wire | Short (<100 m, 3/4-wire for lead compensation) | Most accurate temperature |
| HART | 4–20 mA + FSK digital | Yes | 2 | Same as current loop | Digital overlay for diagnostics |

The 4 mA "live zero" distinguishes a 0% signal (4 mA) from a broken wire (0 mA), which is why the 4–20 mA current loop dominates process instrumentation.

## References

- [Computing: embedded systems](../computing/embedded-systems.md) — the MCU/PLC/FPGA substrate.
- [Control circuits](control-circuits.md) — relay logic and ladder logic that PLCs execute.
- [Electrical systems](electrical-systems.md) — motors, contactors, sensors, industrial wiring.
- [Communications circuits](communications-circuits.md) — physical-layer signaling underlying Modbus and fieldbus.
- [Power supply circuits](power-supply-circuits.md) — the 24 VDC supply that powers PLC I/O.
- Deep articles: [PLC](industrial-control.plc.md), [SCADA](industrial-control.scada.md), [HMI](industrial-control.hmi.md), [industrial-control-architecture](industrial-control.industrial-control-architecture.md).

---
*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](./index.md)*
