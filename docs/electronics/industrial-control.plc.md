# PLC Design

> **Node ID**: `electronics.industrial-control.plc`
> **Domain**: [Electronics](index.md)
> **Dependencies**: `electronics.industrial-control`, `electronics.control-circuits.ladder-logic`, `electronics.control-circuits.relay-logic`, `electronics.control-circuits.discrete-logic-circuits`

A Programmable Logic Controller (PLC) is a rack-mounted industrial computer designed for one job: execute boolean and sequential control logic over a large number of digital and analog I/O points, deterministically, in a hostile electrical environment, for decades, without rebooting. It is the machine that ate the relay panel. Where a 1960s factory floor needed a cabinet of hundreds of electromechanical relays, timer relays, and counters — each wired in a bespoke tangle that took weeks to draw, build, and debug, and weeks more to re-wire when the process changed — a single PLC runs the same logic as a program, re-configurable from a laptop in minutes. This article teaches the PLC as a *platform*: its hardware architecture (rack, power supply, CPU, I/O modules), its opto-isolated input and output modules, its deterministic scan-cycle execution model, its memory organization, the five IEC 61131-3 programming languages, and its industrial communication buses. It assumes you already know the [relay hardware](control-circuits.relay-logic.md) the PLC replaced and the [ladder-logic notation](control-circuits.ladder-logic.md) the PLC executes — this article covers the *controller*, not the logic notation.

## Why the PLC: History and Rationale

Before 1968, industrial machine control meant relay panels. A single automated transfer line or an automobile assembly line could require **thousands of relays** in a cabinet the size of a room, wired per a schematic that took a draftsman weeks to draw. The relays failed mechanically (contact wear, armature sticking), the wiring fatigued, and the panel ran hot (each relay coil dissipates 1-5 W — a thousand-relay panel dumps kilowatts of heat). Worst of all, changing the control logic meant **re-wiring the panel** — a physical, labor-intensive, error-prone process. If a factory retooled a line every two years for a new model, the relay panel was rebuilt each time.

In 1968, General Motors' Hydramatic Division (the automatic-transmission plant in Ypsilanti, Michigan) wrote a now-famous specification asking the electronics industry for a **solid-state replacement for relay panels**. The ten requirements distilled to:

1. **Programmable** — control logic in software, reconfigurable without re-wiring.
2. **Easy to program and re-program** by the relay electricians on staff, not by computer programmers — meaning the programming interface had to look like a relay ladder diagram, not assembly language or punched cards.
3. **Rugged** — survive the factory floor (temperature swings, vibration, electrical noise from motor starts and welders), unlike a mainframe computer in its air-conditioned glass house.
4. **Maintainable** — modules plug in and out; a failed I/O card is swapped in minutes.

Bedford Associates won the bid and built the **MODICON 084** (Modular Digital Controller, model 084), installed at GM's Landshut, Michigan plant in 1969 — generally cited as the first commercial PLC. Allen-Bradley followed with the PLC-2 (1972), and the architecture rapidly displaced relay panels across the auto, steel, and process industries through the 1970s. The programming language was relay ladder logic — deliberately, so the existing relay electricians could read and write PLC programs on sight. The [ladder-logic article](control-circuits.ladder-logic.md) covers that notation in full.

The defining design choice of the PLC, and the one that distinguishes it from a general-purpose computer doing the same boolean operations, is the **deterministic scan cycle**. A PC or server responds to events as they arrive (interrupt-driven, variable latency, best-effort). A PLC does not wait for events. Instead it **polls every input, solves the entire logic program, drives every output, and repeats** — a fixed cyclic execution called the *scan*. The result is deterministic: the response time to any input change is bounded by (at most) two scan cycles, and every scan executes the same sequence of instructions in the same order. A control engineer can look at the program and the scan time and state with certainty that the motor will stop within 10 ms of the limit switch being hit. A general-purpose computer cannot make that guarantee because its operating system may have been busy with something else when the switch changed. This determinism — bought at the cost of a few milliseconds of polling latency — is why PLCs run factories and PCs do not.

For the embedded-systems perspective on where PLCs sit among microcontrollers, RTOS-based boards, and FPGA options for control — and why the PLC's $50-200/channel cost buys integrated isolation and ladder development speed — see [Embedded Systems](../computing/embedded-systems.md). This article is the authoritative source for PLC platform details; that cross-link provides the broader embedded-controller decision framework.

## Hardware Architecture

A PLC is built from four hardware blocks bolted into a common **rack** (also called a *chassis* or *backplane*). The rack is a physical frame with a printed-circuit backplane bus carrying power and data; the modules slide into slots and connect to the backplane via edge connectors. A small PLC (a "brick" or nano-PLC) integrates all four blocks into one sealed housing with a fixed I/O count; a mid-size PLC uses a 4-13 slot rack; a large PLC cascades multiple racks linked by extension cables to reach thousands of I/O points.

```
    PLC RACK ARCHITECTURE (mid-size modular PLC)

       Slot 0      Slot 1      Slot 2      Slot 3      Slot 4
    +-----------+-----------+-----------+-----------+-----------+
    |           |           |           |           |           |
    |  POWER    |   CPU     |  INPUT    |  INPUT    |  OUTPUT   |
    |  SUPPLY   |  MODULE   |  MODULE   |  MODULE   |  MODULE   |
    |  (PS)     |  (proc +  |  (DC 24V, |  (AC 120V)|  (relay)  |
    |           |  memory)  |  16 pt)   |  (8 pt)   |  (16 pt)  |
    |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+
         |           |           |           |           |
         +-----------+-----------+-----------+-----------+
                      BACKPLANE BUS (power + data)
         |                                   |
    +====+====+                         +====+====+
    |  L1/N/G  |                         |  field  |
    |  AC line |                         |  wiring |
    |  (120/   |                         |  (to    |
    |  240V)   |                         | sensors,|
    +==========+                         | actuators|
                                          +========+


    Field side (sensors -> input modules; output modules -> actuators):

    SENSOR_1 ----+      +----- INPUT MODULE slot 2 ---- backplane
    (24V DC      |      |
     proximity)  +------+         ...
    SENSOR_2 ----+
                  OUTPUT MODULE slot 4 ----+---- MOTOR CONTACTOR COIL
                                          |
                                          +---- SOLENOID VALVE
                                          |
                                          +---- INDICATOR LIGHT
```

The four blocks:

### Power Supply (PS)

Converts the plant AC line (120 V or 240 V AC, 50/60 Hz) or a 24 V DC plant bus to the low-voltage DC rails the backplane and logic need: typically +5 V for the CPU logic, ±12 V or ±15 V for analog I/O circuitry, and a regulated +24 V DC *field power* rail for sourcing current into input sensors and output loads. Power supply sizing is additive: sum the current draw of every module in the rack (each I/O card consumes 50-300 mA from the +5 V backplane rail depending on channel count and load) plus the field-side current the sensors and output loads draw, then add 20-30% margin. A typical 8-slot rack needs a 5 V / 10 A power supply for the backplane and a 24 V / 10 A supply for field power.

### CPU Module

The brain: a microprocessor (originally a bit-slice or early microcontroller; modern PLCs use ARM Cortex, PowerPC, or x86), program memory holding the user's ladder/ST/FBD logic, data memory holding the I/O image tables and variable store (see *Memory Organization* below), and the backplane interface that lets the CPU read input modules and write output modules on every scan. The CPU module also carries the programming-port (Ethernet, USB, or serial) for downloading programs from the engineering workstation, and runs the firmware that implements the scan cycle. CPU speed is specified in **K-instructions/ms** (thousands of boolean contact/coil instructions solved per millisecond) — a small CPU solves 0.1-1 K-instr/ms; a large CPU solves 10-100 K-instr/ms. This single number, more than clock rate, predicts scan time for a given program size.

### Input Modules

Read the state of field sensors and present it as bits to the CPU. Each input point is **galvanically isolated** from the field wiring by an optocoupler (LED + phototransistor in one package) so that a voltage spike on a field wire — from a lightning surge, a welder's arc, or an inductive kick from a motor contactor — destroys the optocoupler (a 50-cent part) rather than the CPU. Details in *Input Modules* below.

### Output Modules

Take output bits written by the CPU and drive the field actuators — contactor coils, solenoid valves, indicator lamps, motor starters. Like inputs, outputs are isolated (relay contacts inherently, opto-triac or opto-transistor for solid-state). Details in *Output Module Types* below.

### Expansion and Distributed I/O

A single rack holds 4-17 modules. For larger I/O counts, two strategies are used:

- **Expansion racks** — a second (third, ...) rack connected to the main rack's CPU by an expansion cable (parallel bus, distance < 3 m) or a serial link (RS-485 or proprietary, up to hundreds of meters). The CPU in the main rack reads/writes expansion-rack I/O transparently as if it were local.
- **Remote I/O** — a **fieldbus** link (Modbus RTU, Profibus, EtherNet/IP, Profinet) to satellite I/O *drops* placed near the sensors, each drop being a small rack with its own communication adapter. This slashes field-wiring cost: instead of running 200 home-run cables from sensors across a plant back to a central PLC cabinet, you run one fieldbus cable to a remote drop near the sensors and wire 32 local points into it. The communication scan adds latency (0.5-5 ms per drop) but saves tens of thousands of dollars in copper and conduit.

## Input Modules

The job of an input module is to take a **field signal** (a voltage from a sensor indicating "present" or "absent") and convert it into a **bit** the CPU reads. Two field-signal families dominate industrial sensing:

### DC Input (24 V DC)

The workhorse. Industrial DC sensors — proximity switches (inductive for metal, capacitive for liquid/plastic, photoelectric for beam-break), limit switches, push-buttons — run from a regulated 24 V DC supply. A "1" (sensor active / object detected / button pressed) is 24 V at the input terminal; a "0" is 0 V. Inside the input module:

```
    DC INPUT POINT (one channel of a 16-point DC input card):

    field +24V ----[ sensor: NO PNP proximity ]----+---- input terminal
                                                  |
                                                  R_limit (e.g. 2.2 kΩ)
                                                  |
                                                  +---->|----+----> to CPU
                                                  |    LED   |    bit register
                                                  |   (in   |
                                                  | opto-   +--[ phototransistor ]
                                                  | coupler)      |
                                                  |               |
    field 0V (DC common) -------------------------+---------------+---- 0V

    Signal path:  sensor ON -> 24V at terminal -> current through R_limit
    -> LED lights -> phototransistor conducts -> CPU bit = 1.
    sensor OFF -> terminal floats to 0V via pull-down -> no LED current
    -> phototransistor off -> CPU bit = 0.
```

The **LED + phototransistor** inside the optocoupler is the isolation barrier. The field side (sensor, 24 V) is electrically separate from the logic side (CPU, 5 V); the only coupling is the light beam inside the optocoupler. A 1500 V surge on the field wire punctures the optocoupler's LED (replacing a 50-cent part) and never reaches the CPU.

**Debounce filtering**: mechanical contacts (limit switches, push-buttons) *bounce* — the contact closes, bounces open, closes again, several times over 1-10 ms as the metal settles. Without filtering, the PLC sees this as a burst of 1-0-1-0-1 pulses. The input module applies an **RC low-pass filter** (typically 3-10 ms time constant) and/or a digital debounce (the input must be stable for N consecutive scans before the bit updates). This guarantees that one physical button press produces exactly one input transition, not a burst. The trade-off is added latency: a 5 ms filter adds up to 5 ms to the input's response time.

### AC Input (120/240 V AC)

Used when the field signal comes from AC-powered devices — older mechanical switches wired to the AC line, or AC proximity sensors common in legacy plants. AC input modules add a **bridge rectifier** before the optocoupler so the LED (which only conducts in one direction) sees a unipolar waveform from the bipolar AC input. A threshold + smoothing stage holds the bit at "1" as long as the AC peak exceeds the on-threshold each half-cycle, and drops to "0" if the AC disappears for more than one cycle (~20 ms at 50 Hz).

```
    AC INPUT POINT (one channel):

    field L1 (120V AC) ----[ sensor ]----+---- input terminal
                                        |
                                   bridge rectifier (4 diodes)
                                        |
                                   smoothing cap + R
                                        |
                                   LED in optocoupler
                                        |
    field N (neutral) ------------------+---- 0V

    AC at terminal -> rectified to DC pulses -> cap smooths ->
    LED lit continuously -> CPU bit = 1.
    AC removed -> cap drains within ~1 cycle -> LED dark -> bit = 0.
```

The 24 V DC standard is strongly preferred for new installations: lower shock hazard, smaller power supply, finer-gauge wire, and it matches the supply voltage of modern solid-state sensors. AC inputs survive mainly for retrofit compatibility.

## Output Module Types

Output modules take a bit from the CPU and switch a field load. Three technologies cover every industrial output need, chosen by load type (AC vs DC, inductive vs resistive) and switching speed:

### Relay Output

A mechanical relay inside the output module. The CPU bit energizes the relay coil; the relay's dry contact (a Form-A SPST NO contact, or Form-C SPDT for NO+NC) closes and passes the field voltage through to the load. Because it is a **dry contact**, the field voltage is whatever the user wires to the common terminal — AC or DC, 24 V or 240 V, the relay does not care (within its rating). This makes relay-output cards the most flexible: one card type drives contactor coils at 24 V DC, solenoid valves at 120 V AC, and indicator lamps at 240 V AC without changing the card.

- **Current rating**: typically 2 A per point, 8 A per common (a group of 4-8 points sharing a common terminal). Exceeding the per-point rating welds the contact shut — the load stays energized even when the PLC commands off, a dangerous failure mode for motors and heaters.
- **Switching speed**: slow. Relay mechanical operate time is 5-15 ms; release time is 5-20 ms. This makes relay outputs unsuitable for anything switched faster than ~5 Hz (PWM, stepper pulses, fast sequencing). They are for on/off control: motor start/stop, valve open/close, lamp on/off.
- **Lifetime**: electromechanical. Contacts wear with each switching cycle (arc erosion). A relay rated for 100,000 operations at full resistive load may last only 10,000 at an inductive load (contactor coils) due to the arc on break. At one cycle per minute, 100,000 operations is ~10 weeks — so relay outputs are not for cyclic duty, only occasional switching.
- **Flyback protection**: switching an inductive load (contactor coil, solenoid) generates a voltage spike on break (V = −L·di/dt, easily hundreds of volts). A flyback diode (DC loads) or RC snubber / MOV (AC loads) across the load absorbs the spike, protecting the relay contact from arcing.

### Triac Output (AC Solid-State)

A triac (bidirectional thyristor) switches AC loads with no moving parts. The CPU bit triggers the triac's gate via an opto-triac (an optocoupler with a triac output stage), so isolation is preserved. Unlike a relay, the triac only conducts AC — it cannot switch DC, because a triac latches on and only turns off at the next AC zero-crossing when the current through it drops below the holding current. With no DC zero-crossing, a DC load would keep the triac on forever once triggered.

- **Current rating**: 0.5-2 A per point typical. Solid-state, so no contact wear — effectively unlimited switching life.
- **Switching speed**: fast but **zero-crossing only** — the triac turns on at the next AC zero-crossing after the gate trigger, and off at the zero-crossing after the bit clears. Worst-case turn-on latency is one half-cycle (8.3 ms at 60 Hz, 10 ms at 50 Hz).
- **Leakage**: a small leakage current (0.5-2 mA) flows through the triac even when "off" — enough to faintly glow a sensitive indicator or hold in a small reed relay. A bleeder resistor (e.g. 10 kΩ across the load) bleeds off leakage so the off-state voltage is a clean 0 V.
- **Application**: AC loads that switch frequently or need long life — valve banks, lamp drivers, heater banks cycled by a PID loop. The triac's zero-cross turn-on also minimizes EMI (no abrupt voltage step mid-cycle).

### Transistor Output (DC Solid-State)

A MOSFET or bipolar transistor switches DC loads. Like the triac, it is solid-state and isolated via an optocoupler. Unlike the triac, it is **DC only** and **fast** — switching times of microseconds, supporting PWM (up to 100 kHz on fast cards), stepper pulse trains, and high-speed sequencing. The field voltage must match the card's rating (commonly 24 V DC sourcing or sinking).

- **Current rating**: 0.5-2 A per point. Transistors have no contact wear; life is limited only by thermal cycling and over-current/over-voltage events.
- **Switching speed**: 10-100 μs typical, with high-speed cards reaching 1 μs. This is the only output type suitable for PWM motor speed control, stepper drive step/dir signals, and servo enable/step trains.
- **Polarity**: DC, so sourcing (PNP, switches +24 V to the load) vs sinking (NPN, switches the load to 0 V) must match the load's input type. A sourcing card drives a sinking input device; a sinking card drives a sourcing input device. Mixing the two blows the transistor.
- **Application**: PWM-controlled heaters, stepper/servo drive commands, high-speed counter outputs, fast solenoid sequencing. Anywhere a relay is too slow or would wear out from cycling.

### Output Selection Summary

| Type | Load | Current/point | Max switch rate | Isolation | Best for |
|------|------|---------------|-----------------|-----------|----------|
| Relay | AC or DC (dry contact) | 2 A | ~5 Hz (mech limit) | Relay (galvanic) | Mixed AC/DC loads, infrequent switching |
| Triac | AC only | 0.5-2 A | ~60 Hz (zero-cross) | Opto-triac | Frequent AC switching, heater/valve cycling |
| Transistor | DC only | 0.5-2 A | 10-100 kHz | Optocoupler | PWM, stepper/servo, high-speed DC |

## The Scan Cycle

The scan cycle is the PLC's heartbeat and the source of its determinism. Unlike a general-purpose computer that reacts to events via interrupts with variable latency, the PLC **polls** every input, solves every logic rung, and drives every output in a fixed repeating loop. The scan has four phases:

```
    PLC SCAN CYCLE (repeats forever):

    +-----------------------+<---------+
    |  1. READ INPUTS (I/O) |          |
    |     Read every input  |          |
    |     terminal, copy to |          |
    |     INPUT IMAGE TABLE |          |
    |     (snapshot of all  |          |
    |     input bits).      |          |
    |     Time: 0.5-2 ms    |          |
    +-----------------------+          |
                |                      |
                v                      |
    +-----------------------+          |
    |  2. SOLVE LOGIC       |          |
    |     (Execute program) |          |
    |     Rung 1 -> rung 2  |   repeat |
    |     -> ... -> rung N, |   forever|
    |     each rung reads   |          |
    |     input image,      |          |
    |     writes output     |          |
    |     image + internal  |          |
    |     bits.             |          |
    |     Time: 1-50 ms     |          |
    |     (program-size     |          |
    |      dependent)       |          |
    +-----------------------+          |
                |                      |
                v                      |
    +-----------------------+          |
    |  3. WRITE OUTPUTS     |          |
    |     (I/O)             |          |
    |     Copy OUTPUT IMAGE |          |
    |     TABLE to physical |          |
    |     output terminals. |          |
    |     Time: 0.5-2 ms    |          |
    +-----------------------+          |
                |                      |
                v                      |
    +-----------------------+          |
    |  4. HOUSEKEEPING      |          |
    |     - Service comms   |          |
    |       (programming    |          |
    |        port, fieldbus) |---------+
    |     - Run diagnostics |
    |       (watchdog,      |
    |        self-test)     |
    |     - Update timers/  |
    |       counters        |
    |     Time: 1-5 ms      |
    +-----------------------+

    SCAN TIME = sum of phases 1+2+3+4.
    Typical small PLC: 1-10 ms.  Typical large PLC: 10-50 ms.
```

**Phase 1 — Read Inputs:** the CPU scans the backplane, reads every input module's current field state, and copies it into the **input image table** — a region of RAM holding one bit per input point. This snapshot is taken once, at the top of the scan. All logic execution in phase 2 reads this snapshot, not the live field terminals. Consequence: if an input changes *during* phase 2, the change is not seen until the next scan's phase 1. The input image is frozen for the duration of one scan.

**Phase 2 — Solve Logic:** the CPU executes the user program — rung 1, then rung 2, ..., then rung N, in strict top-to-bottom order. Each rung reads its contact bits from the input image table and from internal memory (timer/counter done bits, internal relay bits, output image table), solves the boolean condition, and writes its coil result to the output image table or an internal bit. Output writes to the *image table*, not the physical terminals — so a coil energized in rung 3 does not immediately energize the physical output; that happens in phase 3. Internal bit writes (e.g., a virtual relay bit used by a later rung) take effect immediately within phase 2, so rung 4 sees the bit rung 3 wrote.

**Phase 3 — Write Outputs:** the CPU copies the entire output image table out to the physical output modules over the backplane. The field actuators (contactor coils, valves, lamps) change state in this phase, as a batch, after all logic is solved.

**Phase 4 — Housekeeping:** service the programming port and any network/fieldbus connections (respond to a polling master, accept a program download, return diagnostic data to the engineering workstation), run CPU self-tests and the watchdog timer (if the scan overruns a preset limit, the watchdog faults the PLC to a safe state and lights the fault LED), and update timer/counter accumulators that tick once per scan. Then the loop returns to phase 1.

### Worked Example: Scan-Cycle Timing

A PLC controls a conveyor line with the following I/O:

- 512 digital inputs (photoelectric sensors, limit switches, push-buttons)
- 512 digital outputs (contactor coils, solenoid valves, indicator lamps)
- 32 analog inputs (temperature, pressure transmitters)
- User program: 1000 ladder rungs, averaging 5 instructions per rung = 5000 instructions total

The CPU is rated at 10 K-instructions/ms (a mid-range processor). What is the scan time and the worst-case response latency to an input change?

```
    Phase 1 — Read Inputs:
      Digital in:  512 points, backplane read ~ 0.8 ms
      Analog in:   32 channels, ADC conversion ~ 1.5 ms
      Subtotal phase 1:  2.3 ms

    Phase 2 — Solve Logic:
      5000 instructions / (10000 instr/ms) = 0.5 ms
      Subtotal phase 2:  0.5 ms

    Phase 3 — Write Outputs:
      Digital out: 512 points, backplane write ~ 0.5 ms
      (Analog out: none)
      Subtotal phase 3:  0.5 ms

    Phase 4 — Housekeeping:
      Comms + diagnostics + timer/counter update: ~1.7 ms
      Subtotal phase 4:  1.7 ms

    --------------------------------------------------------
    SCAN TIME = 2.3 + 0.5 + 0.5 + 1.7  =  5.0 ms
```

**Worst-case response latency:** an input that changes state just *after* phase 1's snapshot is taken misses the current scan entirely — the new state is captured on the next scan's phase 1, the logic responds in that scan's phase 2, and the output physically changes in that scan's phase 3. So the input waits one full scan to be seen, plus a second scan to propagate to the output:

```
    t=0     input changes (just after phase 1 snapshot)
    t=0..5  scan N completes (input not seen; old snapshot used)
    t=5     scan N+1 phase 1: input captured into image table
    t=5..10 scan N+1 phase 2: logic responds, output image updated
    t=10    scan N+1 phase 3: physical output changes
    ---->  WORST-CASE LATENCY = 2 x scan time = 10 ms
```

Best-case latency (input changes just *before* phase 1, captured immediately, output written at the end of the same scan) is one scan: 5 ms. So response latency is **5-10 ms** — one to two scans, always bounded, always predictable. Contrast a general-purpose computer running the same boolean logic as an event-driven program: an input interrupt could be serviced in 50 μs *or* delayed 100 ms if the OS was busy with disk I/O or garbage collection — unbounded, unpredictable. That unbounded latency disqualifies the PC for safety-critical deterministic control. The PLC's 10 ms guaranteed bound is what makes it suitable.

**Scan time budgeting:** scan time scales with program size (phase 2) and I/O count (phases 1 and 3). A 10,000-rung program on the same CPU would take 5 ms in phase 2 alone, pushing scan time past 10 ms and worst-case latency to 20 ms. If the process needs faster response than the scan allows — high-speed counting, motion control, fast PID — the PLC adds **hardware interrupts** (special input cards that trigger a subroutine outside the normal scan, called an *immediate* or *event* task, executing in 50-200 μs regardless of scan position) or offloads that loop to a dedicated motion module. For everything else, the scan is sufficient: motor control, machine sequencing, batch process logic all operate on the 5-50 ms timescale, well within one or two scans.

The [ladder-logic article](control-circuits.ladder-logic.md) covers the consequences of the scan model for ladder program design in detail — frozen inputs, batched outputs, rung ordering, and the one-scan-cycle lag when a rung reads a bit set by an earlier vs. later rung.

## Memory Organization

PLC memory is partitioned into fixed regions, each with a defined role. This partitioning — standardized across vendors by IEC 61131-3 — is simpler and more rigid than a general-purpose computer's flat memory model, because determinism demands that every variable have a known type, address, and update rule.

```
    PLC MEMORY MAP (typical mid-size PLC):

    +---------------------------------+
    |  SYSTEM / FIRMWARE              |  Vendor code (scan engine, comms
    |  (read-only, flash)             |  stacks, I/O drivers). Not user-
    |                                 |  accessible. Fixed size.
    +---------------------------------+
    |  PROGRAM MEMORY                 |  User's control logic — ladder
    |  (flash or battery-backed       |  rungs, ST blocks, FBD networks,
    |   RAM)                          |  SFC steps. The "program" that
    |                                 |  the scan executes. Kilobytes to
    |                                 |  megabytes depending on PLC class.
    +---------------------------------+
    |  DATA MEMORY (retentive)        |
    |  +---------------------------+  |
    |  | Input Image Table (I)     |  |  One bit per digital input point.
    |  |                           |  |  Updated in phase 1 (read inputs).
    |  |                           |  |  e.g. %IX0.0 .. %IX31.7
    |  +---------------------------+  |
    |  | Output Image Table (Q)    |  |  One bit per digital output point.
    |  |                           |  |  Written in phase 2 (logic),
    |  |                           |  |  copied to outputs in phase 3.
    |  |                           |  |  e.g. %QX0.0 .. %QX31.7
    |  +---------------------------+  |
    |  | Internal / Marker (M)     |  |  Internal bits — "virtual relays."
    |  |                           |  |  Used for inter-rung storage,
    |  |                           |  |  one-shots, state flags.
    |  |                           |  |  e.g. %MX0.0 .. %MX255.7
    |  +---------------------------+  |
    |  | Timer (T) / Counter (C)   |  |  TON/TOF/CTU/CTD accumulators,
    |  |                           |  |  presets, done bits. Counters
    |  |                           |  |  are retentive (battery-backed).
    |  +---------------------------+  |
    |  | Integer / Word Registers  |  |  16/32-bit integers: analog
    |  | (MW, DW)                  |  |  values, setpoints, counts,
    |  |                           |  |  arithmetic results.
    |  |                           |  |  e.g. %MW0 .. %MW1023
    |  +---------------------------+  |
    |  | Float / Real Registers    |  |  IEEE-754 32-bit floats for
    |  |                           |  |  PID loop gains, math results.
    |  +---------------------------+  |
    |  | Data Blocks / Files       |  |  Arrays, recipes, lookup tables,
    |  |                           |  |  shift registers, retentive logs.
    |  +---------------------------+  |
    +---------------------------------+
```

The address syntax shown (`%IX0.0`, `%QX2.7`, `%MW100`, `%T5`) follows the IEC 61131-3 convention: `%` prefix, a letter for the region (I=input, Q=output, M=marker, T=timer, C=counter), a size code (X=bit, B=byte, W=word, D=double-word, R=real), and an address. Allen-Bradley uses a file-based syntax instead (`I:1/0`, `O:2/0`, `B3:0/0`, `N7:0`, `F8:0`) but the partitioning is identical.

**Retentive vs. non-retentive memory:** counters, latched bits (set by OTL/OTU, see the [ladder-logic article](control-circuits.ladder-logic.md)), and selected data blocks are *retentive* — they survive power loss, backed by a battery or supercapacitor or flash. This matters for outputs that must restart in their last state after a power flicker (a remote unattended pump) vs. outputs that must drop to a safe default on power loss (a press brake). The choice of which variables are retentive is a safety-design decision, encoded in the program.

## IEC 61131-3 Programming Languages

The international standard IEC 61131-3 (first published 1993, current revision IEC 61131-3:2013) defines five programming languages for PLCs. Every major PLC vendor (Allen-Bradley, Siemens, Mitsubishi, Schneider, Beckhoff) supports a subset of these, though with vendor-specific dialects. A single PLC program can mix languages — a batch sequence in SFC, its analog math in ST, its motor interlocks in LD, all in one project — with the languages calling each other.

**Ladder Diagram (LD) is the primary language** and the one the vast majority of PLC programs use for discrete (on/off) control. The other four are mentioned here for awareness and for the niches where each excels; this article does not teach them in depth, because LD covers the overwhelming majority of industrial control logic and the other languages are used for specialized tasks (analog math, batch sequencing, legacy portability).

### LD — Ladder Diagram (primary)

The relay-ladder metaphor: two rails, rungs top-to-bottom, contacts (XIC/XIO) and coils (OTE/OTL/OTU) on rungs, executed by the scan cycle. It is the language relay electricians already knew (deliberately — that was the GM/Hydramatic requirement), and it remains the best language for discrete motor control, interlocks, seal-in logic, timer/counter sequences, and any logic that reads naturally as "if these conditions, then this output." The full notation — contacts, coils, timers, counters, the scan model, and worked examples — is taught in the [Ladder Logic Design](control-circuits.ladder-logic.md) article. This article does not re-teach it; LD is the language PLCs run, and that article owns the language.

### FBD — Function Block Diagram

A graphical language where the program is a network of **function blocks** — rectangles with named inputs on the left and outputs on the right — connected by lines carrying signals. Blocks are reusable, parametrized components: an AND block, an OR block, a PID block, a timer block, a scaling block. A line from block A's output to block B's input means "the signal computed by A feeds into B." FBD looks like a signal-flow diagram or an analog-computer patch panel.

```
    FBD EXAMPLE — a tank-level PID loop:

    setpoint ---->( PID )----> output
                      ^
                      |
    level_pv --------+
                      ^
                      |
                  ( SCALE )<---- raw ADC
```

FBD excels at **analog and continuous control** (PID loops, scaling, filtering) and at **reusable component libraries** (define a "motor_control" block once, drop instances for motor_1, motor_2, motor_3). It is preferred in the process industries (chemical, pharma, water treatment) where analog loops dominate and where the signal-flow metaphor matches the P&ID (piping and instrumentation diagram) the process engineers already think in.

### ST — Structured Text

A Pascal-like textual language with assignment statements (`:=`), `IF/THEN/ELSE`, `CASE`, `FOR/WHILE/REPEAT` loops, function calls, and full arithmetic. It is the language for **complex math** that is painful to express graphically: array operations, trigonometric coordinate transforms for motion control, statistical calculations, string handling, and any algorithm with nested loops or conditionals.

```
    ST EXAMPLE — convert Celsius to Fahrenheit for a sensor array:

    FOR i := 0 TO 7 DO
        TempF[i] := TempC[i] * 9.0 / 5.0 + 32.0;
        IF TempF[i] > AlarmLimit THEN
            OverTemp[i] := TRUE;
            AlarmCount  := AlarmCount + 1;
        END_IF;
    END_FOR;
```

ST is preferred by programmers coming from C/Pascal backgrounds and is increasingly common in modern PLCs (Siemens SCL, Beckhoff TwinCAT, Allen-Bradley Structured Text) for math-heavy logic, motion-control trajectory calculations, and communication-packet parsing.

### SFC — Sequential Function Chart

A state-machine / flowchart language for **sequential batch processes** — a recipe that proceeds through defined steps (fill, heat, react, drain, clean) with transitions between steps gated by conditions (level reached, temperature stable, timer elapsed). SFC represents the program as steps (boxes) connected by transitions (bars), with parallel branches and alternative paths. It is the direct descendant of Grafcet (the French state-machine notation formalized in 1977) and is the natural language for any process that moves through discrete phases.

```
    SFC EXAMPLE — a simple batch reactor:

    [ INIT ]----(start_cmd)---->[ FILL ]----(level_hi)---->[ HEAT ]
                                                                |
                                                          (temp_ok)
                                                                v
                       [ DRAIN ]<----(timer_done)----[ REACT ]
                                                                |
                                                                v
                                                           [ HOLD 30min ]
```

SFC excels at batch chemical, packaging machinery, and any process where the logic is "do step 1 until condition, then step 2 until condition, then ...". It makes the sequence visually obvious in a way that nested ladder rungs do not.

### IL — Instruction List (deprecated)

An assembly-like textual language — a list of opcodes (LD, AND, OR, ST, ADD, JMP) operating on an accumulator register. It was included in the original 1993 standard for compact, low-level programming on resource-limited PLCs, but it is **deprecated** (removed from the mandatory language set in IEC 61131-3:2013) and rarely used in new code. It survives mainly as a portable interchange format and on legacy installations. Mention it for historical completeness; do not write new PLC programs in IL.

### Language Selection

| Language | Best for | Paradigm | Typical user |
|----------|----------|----------|--------------|
| **LD** | Discrete control, interlocks, motor logic | Relay-rung graphical | Electricians, control engineers |
| FBD | Analog loops, PID, reusable components | Signal-flow graphical | Process engineers |
| ST | Complex math, arrays, string/packet handling | Textual (Pascal-like) | Software engineers |
| SFC | Batch sequences, state machines | State-chart graphical | Process/batch engineers |
| IL | (deprecated) legacy interchange | Assembly-like | Legacy maintenance |

The five languages exist because no single paradigm fits all control problems: discrete motor logic reads best as ladder, analog loops as function blocks, math as text, and batch sequences as state charts. A modern PLC project mixes them per task. But LD remains the entry point and the lingua franca — every PLC programmer reads ladder, and the majority of PLC programs in the field are predominantly or entirely ladder.

## Communication

A standalone PLC controls one machine or one cell. Real plants have tens to hundreds of PLCs that must share data — a bottling line's filler PLC tells the capper PLC when a bottle passes, a SCADA supervisory computer polls every PLC for production counts and alarm states, and an engineering workstation uploads program changes. PLC communication falls into two tiers:

### Fieldbus / Device-Level (PLC ↔ sensors, drives, remote I/O)

- **Modbus RTU** (1979, Modicon/Gould) — the original PLC protocol, still ubiquitous. Serial (RS-232 or RS-485), master-slave, register-based: the master sends a request ("read register 40001 from slave 5"), the slave replies with the value. Slow (9.6-115.2 kbps) and simple. Pervasive in legacy plants and simple devices.
- **Modbus TCP** (1999) — Modbus over standard Ethernet/IP, replacing the serial link with a 100/1000 Mbps Ethernet physical layer. Same register model, modern speed. The de facto open protocol for cross-vendor PLC communication.
- **Profibus DP** (1989, Siemens-led) — serial fieldbus (RS-485, up to 12 Mbps), dominant in European discrete manufacturing. Replaced in new installations by Profinet.
- **Profinet** (2003, PROFIBUS International) — real-time Ethernet, sub-millisecond cycle times for motion-control synchronization. Dominant in European automation.
- **EtherNet/IP** (2001, Allen-Bradley/Rockwell) — industrial Ethernet using standard TCP/UDP plus CIP (Common Industrial Protocol). Dominant in North American automation.
- **EtherCAT** (2003, Beckhoff-led) — Ethernet configured for real-time by "on-the-fly" processing (each node reads its data as the frame passes through, without decoding the whole frame). Master-slave, sub-100 μs cycle times for high-speed motion.

### Supervisory / Enterprise-Level (SCADA ↔ PLCs)

- **OPC UA** (OPC Unified Architecture, 2008) — the modern, platform-independent, vendor-neutral protocol for PLC-to-SCADA and PLC-to-MES (manufacturing execution system) communication. Replaces the Windows-COM-based "classic OPC" (OPC DA/AE/HDA). Built-in security (authentication, encryption), information model (each data point carries metadata — engineering units, alarm limits, data type), and service-oriented architecture. The standard for plant-wide data aggregation and IIoT (industrial IoT) integration.

### Polling and Latency

Fieldbus communication is usually **master-slave polling**: the master (PLC or SCADA) cycles through each slave in turn, sending a request and waiting for the reply before moving to the next slave. The polling rate determines how fresh the master's data is:

```
    POLLING LATENCY (Modbus RTU example):

    Master polls 10 slave I/O blocks, each 32 bytes in + 32 bytes out,
    over RS-485 at 38400 bps.

    Frame time per slave:
      Request frame (8 bytes):  8 x 11 bits / 38400 = 2.3 ms
      Slave processing:         ~5 ms (typical Modbus device)
      Response frame (40 bytes): 40 x 11 bits / 38400 = 11.5 ms
      Turnaround + framing:     ~1 ms
      ----> per-slave poll = ~20 ms

    Full poll cycle (10 slaves):  10 x 20 ms = 200 ms
```

So the master sees any given slave's data with a **200 ms update rate** (worst case) — too slow for fast control but adequate for supervisory monitoring (level trends, production counts, alarms). For faster data, switch to a higher-bandwidth fieldbus (Modbus TCP, EtherNet/IP) or a producer-consumer model (each slave broadcasts its state unsolicited, all masters listen, no round-trip wait) which cuts the latency to the single frame time plus jitter. Motion-control synchronization (coordinating multiple servo axes) demands the deterministic sub-millisecond cycle times of EtherCAT or Profinet IRT — standard Ethernet's collision-and-retry arbitration cannot guarantee a delivery deadline.

## Parameter Reference

Consolidated specifications for the module types covered above. Values are typical for mid-range industrial PLCs (Allen-Bradley CompactLogix, Siemens S7-1500, Mitsubishi MELSEC iQ-R class); specific products vary.

| Module Type | Voltage Range | On-state Current | Isolation | Typical Response Time | Best Application |
|-------------|---------------|------------------|-----------|----------------------|------------------|
| DC input | 15-30 V DC | 5-10 mA (at 24 V) | Optocoupler (1500 V AC) | 0.5-5 ms (+ debounce 3-10 ms) | Proximity switches, limit switches, push-buttons (modern standard) |
| AC input | 85-132 V AC (120 V) or 170-264 V AC (240 V) | 10-20 mA | Optocoupler (1500 V AC) + rectifier | 10-25 ms (cycle-dependent) | Legacy AC-powered sensors, AC line monitoring |
| Analog input | ±10 V, 0-10 V, 0-20 mA, 4-20 mA | n/a | Optocoupler or isolation amp | 10-100 ms (filter + ADC) | Temperature/pressure transmitters, level probes |
| Relay output | 5-264 V AC or 5-30 V DC (dry contact) | 2 A per point, 8 A/common | Relay (galvanic, 1500 V AC) | 5-15 ms operate, 5-20 ms release | Mixed AC/DC loads, infrequent switching, contactor/solenoid/lamp |
| Triac output | 20-264 V AC only | 0.5-2 A per point | Opto-triac (1500 V AC) | Up to 1 half-cycle (8-10 ms) zero-cross | Frequent AC switching, heater/valve cycling, lamp banks |
| Transistor output | 20-30 V DC (sourcing PNP or sinking NPN) | 0.5-2 A per point | Optocoupler (1500 V AC) | 10-100 μs (fast cards: <1 μs) | PWM, stepper/servo drives, high-speed DC sequencing |
| Analog output | 0-10 V, ±10 V, 0-20 mA, 4-20 mA | Sourcing 0-20 mA | Isolation amp | 0.5-2 ms settling | Valve positioners, VFD speed reference, retransmission |

**Input thresholds (DC):** the input guarantees a logic "1" at ≥ 15 V and a logic "0" at ≤ 5 V, with a hysteresis band between (5-15 V undefined). This 2:1 threshold margin rejects noise — a 24 V signal that droops to 18 V under load still registers as "1," and a grounded input that floats to 3 V from leakage still registers as "0."

**Derating:** output current ratings are at 25 °C ambient. Derate 2% per °C above 40 °C — a 2 A relay point is 1.4 A at 65 °C. Industrial enclosures routinely reach 50-60 °C internally, so derating is not optional.

## Boundary With Sibling Articles

This article owns the **PLC platform** — the controller hardware, the scan cycle, the memory model, the programming-language overview, and the communication buses. It deliberately does not re-teach:

- **Ladder-logic notation** (contacts, coils, timers, counters, rung structure, the scan model from the notation's perspective) — owned by [Ladder Logic Design](control-circuits.ladder-logic.md). This article links there and treats LD as the primary IEC 61131-3 language the PLC executes.
- **Relay hardware** (seal-in latches, motor starters, overload relays, interlocks, contactor sizing) — owned by [Relay Logic Circuits](control-circuits.relay-logic.md). This article links there and treats the relay panel as the historical ancestor the PLC replaced.
- **Digital logic fundamentals** (Boolean algebra, gate-level design, combinational and sequential logic) — owned by the discrete-logic-circuits article. PLC rungs implement boolean algebra, but the gate-level formalism is taught there.
- **MCU / RTOS / FPGA embedded control** (microcontroller selection, interrupt handling, watchdogs, bare-metal vs. RTOS firmware) — owned by [Embedded Systems](../computing/embedded-systems.md). The PLC is *one* embedded-controller option among MCU, RTOS-board, and FPGA; this article covers the PLC platform specifically, that article covers the broader decision framework.
- **SCADA, HMI, plant-wide control architecture** — future process articles under the [industrial-control](industrial-control.md) capability. This article covers the single PLC; the supervisory and architecture tiers are separate concerns.

## See Also

- [Industrial Control](industrial-control.md) — parent capability: the design-pedagogy hub for PLC, SCADA, HMI, and integrated control architecture.
- [Ladder Logic Design](control-circuits.ladder-logic.md) — the IEC 61131-3 ladder notation PLCs execute: contacts, coils, timers, counters, the scan model, worked rungs. The primary PLC programming language.
- [Relay Logic Circuits](control-circuits.relay-logic.md) — the relay hardware the PLC replaced: seal-in latches, motor starters, interlocks, timer relays. Every ladder rung maps one-to-one onto a relay circuit.
- [Control Circuits](control-circuits.md) — parent capability for relay, ladder, and discrete logic.
- [Embedded Systems](../computing/embedded-systems.md) — where the PLC sits among MCU, FPGA, and bare-metal options for embedded control, and the decision framework for choosing among them.
- [Electrical Systems](electrical-systems.md) — relays, contactors, motors, overload relays, and the industrial wiring that the PLC's I/O points connect to.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
