# Control Circuits

> **Node ID**: electronics.control-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.electrical-systems`](electrical-systems.md)
> **Enables**: None
> **Timeline**: Years 15-35
> **Outputs**: control-circuit-design
> **Critical**: No — control-circuit design pedagogy builds on electrical systems and computing logic; it organizes relay/ladder/discrete-logic knowledge rather than gating a primary bootstrap dependency

## Overview

Control circuits are the electromechanical and discrete-logic layer that sequences industrial machinery — starting and stopping motors, interlocking guards, timing operations, and implementing AND/OR/NOT decisions in hardware before programmable controllers existed. This capability is the **design pedagogy** layer: how to read, draw, and reason about these circuits from first principles, starting from the Edison-era relay and progressing to the discrete/sequential logic that bridged electromechanics and semiconductors.

The progression covers three layers. **Relay logic** is the hardware foundation: relays and contactors implement Boolean functions physically — normally-open (NO) contacts in series perform AND, in parallel perform OR, normally-closed (NC) contacts perform NOT. Seal-in (latching) circuits give memory. Timer relays give sequencing. This is the Edison-era control paradigm and the direct ancestor of every programmable controller. **Ladder logic** is the diagram notation: the rung/rail form, contact/coil symbols (XIC/XIO/OTE), latch/timer/counter rungs, and the scan-cycle concept that later carried over to PLCs. **Discrete and sequential logic** is the circuit-level bridge from relays to semiconductors: building gates, flip-flops, counters, and state machines from discrete transistors and early ICs.

This capability owns circuit-level control hardware and notation. It does **not** re-teach Boolean algebra, HDL, and FPGA design — those live in [computing digital-logic](../computing/digital-logic.md). It does **not** cover PLC hardware architecture and SCADA — those live in [industrial control](industrial-control.md). This capability teaches the *logic* those controllers execute; the controller *platform* is the industrial-control capability.

## Prerequisites

### Materials

- **Relays and contactors** — ice-cube relays (DPDT, 12/24 VDC coil, 10 A contacts), motor contactors (3-pole, 24 VAC coil, 25–100 A). From [electrical systems](electrical-systems.md).
- **Timer relays** — on-delay (TDE), off-delay (TDD), repeat-cycle, 0.1–60 s adjustable. From [electrical systems](electrical-systems.md).
- **Limit switches and pushbuttons** — NO/NC momentary, selector switches, mushroom-head E-stops.
- **Transistors for discrete logic** — 2N3904/2N2222 NPN BJTs for RTL gates; 7400-series TTL ICs (quad NAND, flip-flops, counters) from [semiconductor devices](semiconductor-devices.md).
- **Indicators** — 6/24 V incandescent or LED pilot lights (red/amber/green).

### Tools and Equipment

- [Electrical systems](electrical-systems.md) — 24 VDC bench supply for relay control circuits; 120/240 VAC for contactor power circuits (use isolation transformer).
- Multimeter for continuity and voltage verification.
- Logic probe (or oscilloscope) for discrete-logic troubleshooting.

### Knowledge

- Relay anatomy: coil, armature, NO and NC contacts; contact ratings vs. coil voltage.
- Boolean algebra (AND, OR, NOT, XOR) — the math underlying every relay circuit.
- [Circuit fundamentals](circuit-fundamentals.md) — series/parallel combination, voltage drop across contacts.

## Bill of Materials

| Component | Quantity (per motor-control panel) | Source | Alternatives |
|-----------|-----------------------------------|--------|--------------|
| Motor contactor (3-pole, 24 VAC coil, 25 A) | 1 | [Electrical systems](electrical-systems.md) | Solid-state relay (for low-current) |
| Overload relay (class 10, matched to contactor) | 1 | [Electrical systems](electrical-systems.md) | Electronic overload (PLC input) |
| Control relay (DPDT, 24 VDC coil, 10 A contacts) | 3–5 | [Electrical systems](electrical-systems.md) | PLC output card (replaces relay panel) |
| On-delay timer relay (0.1–60 s) | 1–2 | [Electrical systems](electrical-systems.md) | PLC timer instruction |
| Pushbutton station (start NO, stop NC, E-stop NC twist-release) | 1 | [Electrical systems](electrical-systems.md) | HMI touchscreen (replaces buttons) |
| Limit switch (roller-arm, 1 NO + 1 NC) | 2–4 | [Electrical systems](electrical-systems.md) | Proximity sensor (inductive/capacitive) |
| Pilot lights (24 V, red/amber/green) | 3 | [Electrical systems](electrical-systems.md) | LED panel lamps |
| Control transformer 120:24 V, 100 VA | 1 | [Electrical systems](electrical-systems.md) | 24 VDC switch-mode supply |
| Terminal blocks (DIN-rail, 20-position strip) | 5 strips | [Electrical systems](electrical-systems.md) | Crimp connectors |

## Process Description

### Step 1: Relay Logic — Motor Start-Stop with Seal-In

The canonical relay circuit is the three-wire motor control with seal-in (latching):

1. Wire a stop pushbutton (NC, normally closed) in series with a start pushbutton (NO) across the 24 V control bus.
2. Wire the contactor coil (M) in series with the overload contact (NC, opens on overload).
3. Wire an auxiliary NO contact on the contactor (M-seal) in parallel with the start button.

**Operation**: Momentarily pressing Start energizes coil M, which closes the main contacts (starting the motor) AND the auxiliary seal-in contact. The seal-in contact now bypasses the start button, keeping the coil energized after release. Pressing Stop breaks the circuit, dropping out the coil and opening the seal-in — the motor stays off until Start is pressed again. A power interruption also drops the coil (fail-safe: motor does not auto-restart). *(Deep article: [relay-logic](control-circuits.relay-logic.md))*

### Step 2: Boolean Logic with Contacts

Compose AND, OR, and NOT from contacts:
- **AND**: two NO contacts in series. Both must be closed for current to flow.
- **OR**: two NO contacts in parallel. Either closes → current flows.
- **NOT**: an NC contact. Output is true when the input is de-energized.

Build a two-hand safety interlock: two palm buttons (NO) must both be pressed within 0.5 s to start a press. This is a series AND. Add a timer relay (on-delay, 0.5 s) that drops the output if only one button is held — a timeout logic.

### Step 3: Ladder Logic Documentation

Draw the circuit in ladder-diagram form: two vertical rails (L1 left, L2 right), horizontal rungs between them. Each rung is one logical statement: inputs on the left (contacts), output on the right (coil). Use standard symbols: `]|[` for XIC (examine-if-closed, NO), `]/[` for XIO (examine-if-open, NC), `( )` for OTE (output energize, coil). Number each wire and each rung for documentation. *(Deep article: [ladder-logic](control-circuits.ladder-logic.md))*

### Step 4: Sequential Logic — Traffic Light Example

Build a sequencer with three timer relays (T1, T2, T3) cycling through green-yellow-red. T1 (green, 10 s) on-delay → when T1 times out, it starts T2 (yellow, 3 s) → T2 starts T3 (red, 10 s) → T3 resets T1. Each timer's instantaneous contact controls the corresponding lamp; the timed contact sequences to the next timer.

### Step 5: Discrete-Logic Gates from Transistors

Build RTL (resistor-transistor logic) gates: a 2N3904 with collector resistor and two base resistors implements a 2-input NOR. Invert it (add another transistor) for OR. Cascade two BJT switches for AND. These are the building blocks of [computing digital logic](../computing/digital-logic.md). Verify the truth table with a logic probe. *(Deep articles: [discrete-logic-circuits](control-circuits.discrete-logic-circuits.md), [sequential-logic-circuits](control-circuits.sequential-logic-circuits.md))*

### Step 6: PID Controller (Discrete Implementation)

For continuous process control (temperature, pressure), implement a PID controller: output = K_p·e + K_i·∫e dt + K_d·de/dt, where e = setpoint − measurement. In a relay-based bang-bang controller, replace the proportional term with a comparator and hysteresis (Schmitt trigger). For a full analog PID, use op-amp integrator and differentiator stages from [analog circuits](analog-circuits.md).

## Quantitative Parameters

### Relay Logic Contact Ratings

| Component | Coil voltage | Coil current | Contact rating | Mechanical life | Electrical life |
|-----------|-------------|-------------|---------------|----------------|----------------|
| Ice-cube relay (DPDT) | 12/24 VDC | 40–80 mA | 10 A @ 240 VAC resistive | 10⁷ operations | 10⁶ operations at rated load |
| Motor contactor (size 1) | 24 VAC | 100–200 mA (inrush 5×) | 25 A continuous, 3-phase | 10⁶ operations | 500 000 at rated current |
| Timer relay (DIN-rail) | 24 VDC/VAC | 20 mA | 5 A @ 250 VAC | 20 × 10⁶ operations | 100 000 at rated load |
| Limit switch | N/A | N/A | 10 A @ 240 VAC | 10⁷ mechanical | 500 000 at 6 A |

### Ziegler-Nichols PID Tuning

| Parameter | P-only controller | PI controller | PID controller |
|-----------|------------------|--------------|---------------|
| K_p (proportional gain) | 0.5 · K_u | 0.45 · K_u | 0.6 · K_u |
| K_i (integral gain) | 0 | 0.54 · K_u / T_u | 1.2 · K_u / T_u |
| K_d (derivative gain) | 0 | 0 | 0.075 · K_u · T_u |

K_u = ultimate gain (gain at which the loop sustains steady oscillation with K_i = K_d = 0). T_u = ultimate period (period of that oscillation). Values from the 1942 Ziegler-Nichols paper; give approximately quarter-amplitude decay response.

### PLC Scan Time Benchmarks

| PLC class | Scan time (typical) | Program size | Application |
|-----------|-------------------|-------------|-------------|
| Micro (Allen-Bradley Micro800) | 2–10 ms | 2–20 KB (ladder) | Small machine control (<20 I/O) |
| Mid-range (Siemens S7-1200) | 1–5 ms | 50–200 KB | Cell control (50–200 I/O) |
| High-end (AB ControlLogix) | 0.5–2 ms | 1–10 MB | Process control (1000+ I/O) |
| Safety PLC ( redundant) | <1 ms (task) | Dedicated | ESD, fire & gas |

Scan time = read inputs → execute logic → write outputs → diagnostics. Deterministic — the same every cycle. Fast enough for motor control at 1 ms scan; too slow for sub-microsecond regulation (analog PID needed).

### Boolean Gate Implementations

| Logic function | Relay implementation | Transistor (RTL) | TTL IC |
|----------------|---------------------|-----------------|--------|
| AND | 2 NO contacts in series | 2 BJT switches cascaded | 7408 (quad AND) |
| OR | 2 NO contacts in parallel | 2 emitters into 1 BJT | 7432 (quad OR) |
| NOT | 1 NC contact | 1 BJT inverter | 7404 (hex NOT) |
| NAND | 2 NO in series → NC coil | 2-input BJT NOR + NOT | 7400 (quad NAND) |
| NOR | 2 NO in parallel → NC coil | 2-input common-emitter | 7402 (quad NOR) |
| XOR | 2 relays cross-wired | 4-BJT arrangement | 7486 (quad XOR) |
| Latch (SR flip-flop) | 2 relays, each holding the other's coil | 2 cross-coupled inverters | 74279 (quad SR latch) |

## Scaling Notes

- **Single-machine scale**: one relay panel with 5–20 relays, 2–3 timers, and 10–30 limit switches. Typical 1960s machine control. Panel size 60×90 cm; wiring takes 2–4 days.
- **Multi-station scale**: 50–100 relays in a large panel. Wiring complexity grows as N² (cross-connections). Troubleshooting becomes difficult — this is the problem PLCs were invented to solve in 1968.
- **PLC scale**: a single PLC replaces 50–200 relays in a panel 1/4 the size. Scan time 1–10 ms; deterministic. Programs are software — modifiable without rewiring. *(See [industrial control](industrial-control.md).)*
- **Discrete-logic scale**: a PCB with 7400-series TTL ICs implements a fixed controller (traffic light, elevator sequencer). Faster than relays (ns vs ms) but not reprogrammable. Obsolete for new designs — replaced by microcontrollers and CPLDs.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Motor starts but won't stay running (drops out when Start released) | Seal-in contact not closing, or wired to wrong auxiliary contact | Verify continuity across seal-in auxiliary when coil energized; check that seal-in is NO (not NC) and across the start button |
| Motor starts on its own after power restored | Seal-in contact stuck closed, or no proper drop-out on power loss | Replace welded contactor; verify overload is NC (drops coil on trip); design must fail-safe (drop out, not latch) |
| Timer doesn't time out | Timer coil undervoltage (24 V supply sagging under relay inrush), or timer set to wrong mode (on vs. off delay) | Measure coil voltage under load; verify mode selector on timer relay |
| Relay chatter (rapid buzzing) | Coil undervoltage (brownout), or AC coil on DC supply (or vice versa) | Measure coil voltage; verify AC vs DC coil marking; check for shorted turns (coil overheats) |
| Contact arcing / welding on motor contactor | Inrush current (6× FLC for motor start) exceeding contact rating; or frequent starts | Verify contactor rated for motor starting current (AC-3 utilization category); add surge suppressor across coil |
| Discrete-logic gate output stuck | Input floating (no pull-up/pull-down resistor), or IC damaged by ESD | Tie unused inputs to Vcc (via pull-up) or GND; handle CMOS with ESD precautions; verify Vcc and GND connected |

## Safety

- **Arc flash on contactors**: Opening a motor contactor under load draws an arc (the inductive motor winding sustains current). At 480 V and 50 A, this arc is dangerous. Use arc-flash-rated PPE (category 2+) when working in an energized motor control center.
- **Fail-safe design**: All control circuits must fail to a safe state on power loss. Stop buttons are NC (de-energizing the coil stops the motor). Relays drop out on power failure. E-stops are hard-wired (not software-dependent), breaking the control circuit directly.
- **Guard interlocks**: Moving-machinery guards must interlock the motor contactor directly (NC limit switch in the coil circuit). Opening the guard breaks the circuit — the motor cannot run with the guard open.
- **Lockout/tagout**: Before working on any motor control panel, disconnect and lock the main disconnect. Stored energy in capacitors (VFD DC bus) must be bled. Verify absence of voltage with a meter.
- **Wire color codes**: Follow NFPA 79 / IEC 60204: red = AC control, blue = DC control, black = AC power circuits, green/yellow = earth ground. Mis-wiring causes injury during troubleshooting.

## Quality Control

### Acceptance Criteria

- All control circuits pass a point-to-point continuity check against the schematic before energizing.
- E-stop function drops the motor contactor within 100 ms (verify with a stopwatch or scope).
- Sequence logic follows the timing chart: each step transitions at the specified time (±10% of timer setting).
- No contact welding: verify the contactor opens cleanly after 10 start-stop cycles at rated motor current.

### Testing Methods

- Cold continuity check (power off): verify every wire against the schematic with a DMM on continuity range.
- Dry-run test (control power on, motor disconnected): cycle through all sequences; verify pilot lights and timer behavior.
- Load test (motor connected): start-stop 10 cycles; verify no contact welding, no overheating.
- E-stop test: press E-stop at various points in the cycle; verify immediate motor stop and that reset requires deliberate action (twist or pull).

## Variations and Alternatives

### Control Technology Comparison

| Technology | Speed | Reprogrammability | Cost (20 I/O) | Best for |
|-----------|-------|------------------|--------------|----------|
| Relay logic | 10–50 ms | No (rewire) | $500–1500 | Simple fixed sequences (<10 relays) |
| Solid-state logic (TTL/CMOS) | ns | No (rebuild) | $200–500 | High-speed fixed logic (now rare) |
| PLC (Programmable Logic Controller) | 1–10 ms | Yes (software) | $400–2000 | Industrial machine control (standard) |
| Microcontroller (embedded) | µs | Yes (reprogram) | $20–100 | Custom low-cost control (low I/O count) |

### PID Controller Implementations

| Implementation | Speed | Accuracy | Complexity | Typical use |
|---------------|-------|---------|-----------|-------------|
| Bang-bang (relay on/off with hysteresis) | Relay cycle (1–10 s) | ±2–5 °C | Lowest | Home thermostat, simple oven |
- Op-amp analog PID | Continuous | ±0.1–1% | Medium | Lab temperature, precision process |
- Microcontroller digital PID | Scan time (10–100 ms) | ±0.05% (12-bit) | High (software) | Modern industrial process |
- PLC PID block | Scan time (10–100 ms) | ±0.1% | Medium (instruction block) | Industrial process standard |

## References

- [Electrical systems](electrical-systems.md) — relays, contactors, motors, and the power wiring this control layer switches.
- [Industrial control](industrial-control.md) — PLC hardware, SCADA, and the platform that executes this logic at scale.
- [Circuit fundamentals](circuit-fundamentals.md) — series/parallel combination underlying contact logic.
- [Analog circuits](analog-circuits.md) — op-amp PID implementation and Schmitt triggers for hysteresis.
- [Computing: digital logic](../computing/digital-logic.md) — Boolean algebra, HDL, and FPGA design.
- [Computing: electromechanical](../computing/electromechanical.md) — relay history and the electromechanical computer era.
- Deep articles: [relay-logic](control-circuits.relay-logic.md), [ladder-logic](control-circuits.ladder-logic.md), [discrete-logic-circuits](control-circuits.discrete-logic-circuits.md), [sequential-logic-circuits](control-circuits.sequential-logic-circuits.md).

---
*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](./index.md)*
