# Ladder Logic Design

> **Node ID**: `electronics.control-circuits.ladder-logic`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.control-circuits.relay-logic`](control-circuits.relay-logic.md),
> [`electronics.electrical-systems`](electrical-systems.md)
> **Outputs**: ladder-logic-programs
> **Timeline**: Years 15-30
> **Critical**: No

Ladder logic is the diagram **notation** and design methodology for industrial control. It takes the relay circuits you learned in [Relay Logic Circuits](control-circuits.relay-logic.md) — seal-in latches, motor starters, interlocks, timer sequences — and renders them in a standardized two-rail, rung-by-rung drawing format that any control engineer in the world can read at a glance. Every relay schematic can be transcribed directly into a ladder diagram, and every ladder diagram can be wired up as relays or executed as a program on a [programmable logic controller](industrial-control.md). This article teaches the notation from first principles: the rail/rung structure, the contact and coil symbols, the timer and counter rungs, and the scan-cycle execution model. It assumes you already know what a [relay, contactor, and overload relay](electrical-systems.md) are and how [NO/NC contacts compose into AND/OR/NOT and seal-in memory](control-circuits.relay-logic.md).

## Why a Standard Notation

A factory relay panel from 1930 and a PLC program from today look almost identical on the page. That is not coincidence — it is the point of the notation. Before ladder logic, every control engineer drew schematics in a personal style: rails here or there, contacts drawn differently, coils labelled ad hoc. Debugging another engineer's panel meant tracing wires through an idiosyncratic drawing. Ladder logic standardized the drawing so that **the topology of the drawing matches the topology of the logic**: series contacts are drawn in series on a rung (AND), parallel contacts are drawn in parallel (OR), coils sit on the right end, and power flows from a left rail to a right rail exactly the way current flows from L1 to L2 in a wired control circuit. The notation is executable documentation — a blueprint you can build from and a program you can run.

The format was formalized by NEMA (National Electrical Manufacturers Association) in the 1950s for documenting relay panels, then adopted verbatim by Allen-Bradley's earliest PLCs (the 1969 MODICON 084 and the 1972 PLC-2) because the engineers who would program PLCs were relay-panel electricians — they already read ladder diagrams. The notation was later codified internationally as IEC 61131-3 (the PLC programming standard, 1993), which defines the graphical instruction set (XIC, XIO, OTE, OTL, OTU, TON, TOF, CTU, CTD) used below.

## Ladder Diagram Structure

A ladder diagram has three structural elements:

```
       LADDER DIAGRAM STRUCTURE

  Left rail (power)        Right rail (neutral)
  | |                       | |
  | |----[ Rung 1 ]--------| |     <- top rung (read first)
  | |                       | |
  | |----[ Rung 2 ]--------| |     <- second rung
  | |                       | |
  | |----[ Rung 3 ]--------| |     <- third rung
  | |                       | |
  | |        ...            | |
  | |----[ Rung N ]--------| |     <- bottom rung (read last)
  | |                       | |
  +-+                       +-+
```

- **Left rail** (also called the *power rail* or *bus bar*): the vertical line on the left, analogous to the L1 (hot) supply in a wired circuit. Logic power is "available" here.
- **Right rail** (also called the *neutral rail* or *return rail*): the vertical line on the right, analogous to L2 (neutral). A rung that conducts from left to right energizes its coil.
- **Rungs**: horizontal lines between the rails, each containing contacts (input conditions) on the left and a coil or output (the action) on the right. Each rung is one logical statement: "if the contact conditions are met, energize the coil."

**Reading order** is strictly **top to bottom, left to right**. Within a rung, solve the contact network left to right to determine whether the rightmost coil receives power. Across rungs, solve rung 1 fully before rung 2, rung 2 before rung 3, and so on. This ordering matters because later rungs can reference the results of earlier rungs (e.g., rung 2 might use a contact driven by the coil of rung 1). The top-to-bottom order is the execution order — changing the order of rungs can change the behavior of the program, just as rewiring a relay panel changes its behavior.

This is a direct graphical analogue of the relay schematic. The left rail is L1, the right rail is L2, a rung is one control circuit, a contact is a switch, and a coil is a relay coil. The only difference from a relay schematic is the standardized symbol set and the rule that every rung has exactly one output device on its right end.

## Contact Symbols: XIC and XIO

A contact is an input condition on a rung. It references a *bit* in memory — a physical input terminal, an internal relay (virtual coil), a timer done bit, a counter done bit — and tests whether that bit is currently 1 or 0. There are exactly two contact instructions:

### XIC — Examine If Closed (Normally Open)

```
   XIC symbol:        --[ ]--     (or  --| |-- )

   Meaning: "the rung conducts here IF the referenced bit is 1 (ON/TRUE)"
```

XIC is the **normally-open** contact. It asks: *is the referenced bit on?* If the bit is 1, the contact passes logic power onward (it "closes"). If the bit is 0, the contact blocks power (it stays "open"). This is exactly the NO contact from relay logic: a push-button at rest (bit = 0) is open; pressing it (bit = 1) closes it.

The referenced bit is usually a physical input. If `I:1/0` is wired to a START push-button (NO), then `--[ ]-- I:1/0` conducts when the operator presses START. The XIC can also reference an internal bit — a virtual coil `B3:0/0` — letting one rung's output feed another rung's input exactly as one relay's auxiliary contact feeds another relay's coil.

### XIO — Examine If Open (Normally Closed)

```
   XIO symbol:        --[/]--     (or  --|/|-- )

   Meaning: "the rung conducts here IF the referenced bit is 0 (OFF/FALSE)"
```

XIO is the **normally-closed** contact. It inverts: it asks *is the referenced bit off?* If the bit is 0, the contact passes power (it stays "closed" because it examines-if-open and finds the bit NOT open... the naming is the one genuinely confusing part of the notation, so memorize the truth table instead). If the bit is 1, the contact blocks power (it "opens"). This is the NC contact from relay logic: a STOP push-button (NC, physically closed at rest) passes power until you press it.

The crucial subtlety: the XIO instruction tests a **bit**, not a physical switch. If a STOP button is physically NC (closed at rest, wired to input `I:1/1`), then at rest the input bit is 1 (current flows through the closed NC button into the input). The XIO instruction `--[/]-- I:1/1` inverts that: bit = 1 → contact open → rung broken. That would mean the motor *cannot* run when STOP is at rest — the opposite of what we want. So for a physically-NC STOP button wired so the input bit is 1 at rest, we use an **XIC** (`--[ ]-- I:1/1`): bit = 1 → contact closed → rung conducts. The rule is to match the instruction to the **logic condition you want**, not to the physical contact type:

| Physical input device | Input bit at rest (no actuation) | Instruction to use for "run when device is at rest" | Instruction to use for "run when device is actuated" |
|-----------------------|----------------------------------|-----------------------------------------------------|------------------------------------------------------|
| NO push-button (START)| 0                                | XIO `--[/]--` (tests for 0)                         | XIC `--[ ]--` (tests for 1)                          |
| NC push-button (STOP) | 1                                | XIC `--[ ]--` (tests for 1)                         | XIO `--[/]--` (tests for 0)                          |

This is why the symbols are named by *examination* (XIC = examine if the bit is closed/on; XIO = examine if the bit is open/off) rather than by physical contact type: the instruction operates on the logic bit, decoupled from whether the physical switch is NO or NC. The relay-logic NC/NO naming describes the *hardware*; the ladder XIC/XIO naming describes the *logic test*. When translating a relay schematic to a ladder diagram, a relay NC contact becomes an XIO of the corresponding coil bit (the contact is closed when the coil bit is 0, matching XIO truth).

## Coil Symbols: OTE, OTL, OTU

A coil is an output instruction at the right end of a rung. When the rung's contact network conducts logic power from the left rail to the coil, the coil is **energized** and writes to a bit in memory — a physical output terminal, an internal relay bit, or a latch bit. There are three coil instructions for memory control:

### OTE — Output Energize (Non-retentive Coil)

```
   OTE symbol:        --( )--

   Meaning: "if rung power reaches me, set my bit = 1; if not, set my bit = 0"
```

OTE is the plain coil — the workhorse. It tracks rung continuity in real time: rung conducts → bit = 1; rung broken → bit = 0. This is a non-retentive (non-latching) output: the moment the contact conditions stop conducting, the coil de-energizes and the bit drops to 0. It is the direct analogue of a relay coil that follows its input instantly. If `O:2/0` is wired to a motor contactor, `--( )-- O:2/0` runs the motor while the rung conducts and stops it the instant the rung breaks.

### OTL — Output Latch (Retentive Set)

```
   OTL symbol:        --(L)--     (or  --(S)-- )

   Meaning: "if rung power reaches me, set my bit = 1 AND HOLD it at 1
             until an OTU instruction explicitly clears it — even if
             my rung subsequently loses power"
```

OTL is the **set** half of a latch. It is *retentive*: once it sets the bit to 1, the bit stays 1 even if the rung that triggered it later goes false, even if the controller loses power and restarts (the bit is stored in non-volatile or battery-backed memory). Only an OTU instruction referencing the same bit can clear it. This is the software equivalent of a latching relay (mechanically held) — a momentary signal sets it, and it holds until deliberately reset.

### OTU — Output Unlatch (Retentive Reset)

```
   OTL symbol:        --(U)--     (or  --(R)-- )

   Meaning: "if rung power reaches me, clear my bit to 0"
```

OTU is the **reset** half. It clears a latched bit. OTL and OTU always come in pairs referencing the same bit address — the latch rung sets it (on a START condition), the unlatch rung clears it (on a STOP condition). Together they implement a set-reset (SR) latch with retentive memory: a momentary START latches the bit on, a momentary STOP unlatches it off, and the bit holds its last state through power cycles.

The distinction between OTE and OTL/OTU is the distinction between **non-retentive** and **retentive** memory. OTE forgets the moment its rung goes false — like a plain relay coil. OTL/OTU remember — like a latching relay. Choose OTE for any output that should follow its input conditions directly (a motor that runs while a level switch is closed). Choose OTL/OTU for an output that should persist after its trigger disappears (an alarm that latches on a fault and stays on until an operator acknowledges it).

## Basic Rungs: AND, OR, NOT, Memory

The power of ladder logic is that the **drawing topology is the Boolean logic** — you read the function off the schematic by inspection. Four patterns cover the vast majority of rungs.

### AND — Series Contacts

Two or more XIC contacts in series on a rung conduct only if *all* conditions are true. This is logical AND.

```
   AND rung:  motor runs only if START is pressed AND guard is closed

   |   START            GUARD              MOTOR       |
   |---[ ]---[ I:1/0 ]--[ ]---[ I:1/2 ]---( )--(O:2/0)|
   |                                                   |
   |   Truth:  MOTOR = I:1/0 AND I:1/2                 |
   |   (both contacts must close for the coil to       |
   |    receive power from the left rail)              |
```

Series XIC contacts are the AND of their conditions. Adding a contact in series *adds* a requirement.

### OR — Parallel Contacts

Two or more contact branches in parallel conduct if *any* one branch is true. This is logical OR. In a ladder diagram, parallel branches are drawn as two or more horizontal contact paths stacked vertically between the same two rail-connection nodes:

```
   OR rung:  pump runs if the START button is pressed OR the AUTO mode is active

   |         +--[ ]--[ I:1/0 ]--+                       |
   |---|-----|--- START         |-----( )--( PUMP )----|
   |   |     +------------------+                      |
   |   +--[ ]--[ I:1/3 ]--- AUTO                       |
   |                                                  |
   |   Truth:  PUMP = I:1/0 OR I:1/3                  |
   |   (either branch conducts -> coil energizes)     |
```

Parallel branches are the OR of their conditions. Adding a branch in parallel *adds* an alternative path.

### NOT — The XIO Contact

A single XIO contact in series inverts a condition. The rung conducts *unless* the referenced bit is on. This is logical NOT, and it is how STOP buttons, overload trips, and inhibit signals are wired into rungs:

```
   NOT rung:  heater runs if the TEMP switch is low AND the E-STOP is NOT pressed

   |   TEMP             E-STOP             HEATER      |
   |---[ ]---[ I:1/4 ]--[/]--[ I:1/5 ]----( )--(O:2/3)|
   |                                                   |
   |   Truth:  HEATER = I:1/4 AND (NOT I:1/5)          |
   |   (E-STOP input goes to 1 when pressed; the XIO   |
   |    breaks the rung when the bit is 1, stopping    |
   |    the heater — fail-safe if the E-STOP is NC)    |
```

XIO is the NOT operator. Combined with series (AND) and parallel (OR) topology, any sum-of-products Boolean expression can be drawn directly as a contact network.

### Memory — Latch / Unlatch Pair

The seal-in circuit from [Relay Logic](control-circuits.relay-logic.md) — a momentary START that latches a load on until a STOP breaks the latch — is implemented in ladder logic two ways:

1. **Seal-in (OTE + XIC feedback)**: the coil's own bit is fed back as a parallel XIC contact around the START button, exactly mirroring the relay M-aux seal-in contact. This is non-retentive: if power drops, the coil drops, the seal opens, and the motor does not restart on its own.

2. **Latch/unlatch (OTL/OTU pair)**: the START rung uses an OTL to set a latch bit; a separate STOP rung uses an OTU to clear it. This is retentive: the latch holds through power loss.

Both are shown in the worked examples below.

## Timer and Counter Rungs

Relay timer-relays (on-delay, off-delay) and electromechanical counters become software instructions in ladder logic. Each timer and counter instruction occupies a rung position like a contact (it has an enable condition to its left) and exposes status bits used by later rungs (like a contact).

### TON — Timer On-Delay

```
   TON instruction:   --[ TON ]--
                        Timer On-Delay
                        Timer: T4:0
                        Preset: 5000   (units = 0.001 s, so 5.0 s)
                        Accum:   0     (counts up while enabled)
```

When the rung into a TON conducts (enable = true), the timer's Accumulator (`.ACC`) increments at the timebase (1 ms, 10 ms, 100 ms depending on the PLC timer resolution). When `.ACC` reaches the Preset (`.PRE`), the timer's **Done bit** (`.DN`) goes true. The `.DN` bit is then used as an XIC contact in downstream rungs: `--[ ]-- T4:0/DN`. If the rung enabling the TON goes false before `.PRE` is reached, `.ACC` resets to 0 and `.DN` stays false — TON is non-retentive. Mnemonic: "delayed on, instant off" — exactly the on-delay timer relay.

```
   Timer done bit used downstream:

   |   T4:0/DN                            VALVE       |
   |---[ ]---------------------------------( )--------|
   |                                                  |
   |   (the valve opens only after the 5.0 s timer    |
   |    T4:0 has finished counting)                   |
```

### TOF — Timer Off-Delay

TOF is the mirror: when its enabling rung goes from true to false, the `.ACC` counts up and the `.DN` bit stays true until `.ACC` reaches `.PRE`, then `.DN` goes false. While the rung is true, `.DN` is true immediately. Mnemonic: "instant on, delayed off" — the off-delay timer relay. Used to keep a fan running for a cooldown period after a furnace command stops.

### CTU — Count Up

```
   CTU instruction:   --[ CTU ]--
                        Count Up
                        Counter: C5:0
                        Preset: 100
                        Accum:   0
```

A CTU increments its `.ACC` by 1 each time the rung feeding it transitions from false to true (a rising edge — the rung must go false between counts). When `.ACC` reaches `.PRE`, the `.DN` bit goes true. Unlike timers, counters are **retentive** — they hold their count through power loss. A CTU is the software electromechanical counter, used for batch counting (fill 100 bottles then advance the conveyor), cycle counting (after 5000 motor starts, flag a maintenance interval), or totalizing pulses from a flow sensor.

### CTD — Count Down

A CTD decrements `.ACC` on each rising edge of its rung. Paired with a CTU on the same counter address, the pair tracks a running count up or down — the classic use is a two-bay loading dock: CTU increments when a part arrives, CTD decrements when a part leaves, and the count reflects the current inventory.

## Instruction Reference Table

The complete basic instruction set for ladder logic, as codified by IEC 61131-3 and the major PLC vendors (Allen-Bradley notation shown; Siemens/Mitsubishi use equivalent symbols):

| Instruction | Name | Symbol | Description |
|-------------|------|--------|-------------|
| XIC | Examine If Closed | `--[ ]--` | Normally-open contact. Conducts if the referenced bit is 1. The AND/condition element. |
| XIO | Examine If Open | `--[/]--` | Normally-closed contact. Conducts if the referenced bit is 0. The NOT/inversion element. |
| OTE | Output Energize | `--( )--` | Non-retentive coil. Sets bit = 1 while rung conducts, 0 when rung breaks. Plain relay coil. |
| OTL | Output Latch | `--(L)--` | Retentive set coil. Sets bit = 1 and holds it until an OTU clears it. Survives power loss. |
| OTU | Output Unlatch | `--(U)--` | Retentive reset coil. Clears a latched bit to 0. The reset half of an SR latch pair. |
| TON | Timer On-Delay | `--[ TON ]--` | Counts up while rung is true; `.DN` goes true when `.ACC ≥ .PRE`. Resets if rung goes false. Delayed-on, instant-off. |
| TOF | Timer Off-Delay | `--[ TOF ]--` | `.DN` is true while rung is true and stays true for `.PRE` after rung goes false. Instant-on, delayed-off. |
| CTU | Count Up | `--[ CTU ]--` | Increments `.ACC` on each rising edge of rung; `.DN` true when `.ACC ≥ .PRE`. Retentive. |
| CTD | Count Down | `--[ CTD ]--` | Decrements `.ACC` on each rising edge. Retentive. Paired with CTU for bidirectional counting. |

This is the core vocabulary. Real PLCs add comparison blocks (EQU, GRT, LES), math blocks (ADD, SUB, MUL, DIV), data move/copy (MOV), PID blocks, shift registers, and sequencers — but every one of those is built on top of the contact/coil/timer/counter foundation above, and every one was chosen to look like a relay-panel element so that relay electricians could read PLC programs without retraining.

## The Scan Cycle

A relay panel executes every circuit simultaneously — all the coils respond to their contacts in continuous time, at the speed of the relay armature (5-15 ms). A PLC running a ladder program does something different: it executes the program **one rung at a time, top to bottom, in a repeating scan**. The scan cycle has three phases:

```
   PLC SCAN CYCLE (repeats forever):

   1. READ INPUTS        Read every physical input terminal and copy
                  (I/O)  its state into the input image table
                         (the bits that XIC/XIO references).
                         Typical: 0.5-2 ms for a medium I/O count.

   2. SOLVE LOGIC        Execute rung 1, then rung 2, ..., then rung N,
                  (Scan) updating the bits in the output image table
                         and internal memory as each rung's coil writes.
                         Typical: 1-10 ms depending on program size.

   3. WRITE OUTPUTS      Copy the output image table to the physical
                  (I/O)  output terminals (energize/de-energize the
                         real contactors, solenoids, indicators).
                         Typical: 0.5-2 ms.

   -> goto 1 (repeat forever at the scan time = sum of the three phases)
```

**Key consequences of the scan model:**

- **Inputs are frozen for the scan.** All XIC/XIO contacts in a single scan read the *same* snapshot of the input image table, taken once at the top of the scan. An input that changes mid-scan is not seen until the next scan. This makes the program deterministic — a rung's result depends only on the snapshot, not on the timing of input changes during execution.

- **Outputs change only at the end of the scan.** A coil that writes to an output bit in rung 3 does not energize the physical output terminal until the write-outputs phase. Internal bits (used by later rungs in the same scan) take effect immediately within the scan, but physical outputs are updated in a batch.

- **Rung order matters.** If rung 5 sets an internal bit and rung 3 reads it, rung 3 reads the value from the *previous* scan (a one-scan-cycle lag). If rung 3 sets a bit and rung 5 reads it, rung 5 sees the new value in the *same* scan. This is why ladder programs are written top-down in causality order: the rung that produces a condition must come before the rung that consumes it.

- **Scan time sets the response speed.** A 10 ms scan cannot respond to an event faster than 10 ms. For motor control and machine sequencing this is ample (relays were 5-15 ms). For high-speed counting, motion control, or fast PID loops, a PLC needs hardware interrupts (special input cards that trigger a subroutine outside the normal scan) or a faster platform (an MCU or FPGA — see [Embedded Systems](../computing/embedded-systems.md)).

The scan cycle is the one genuinely new concept ladder logic introduces beyond relay hardware. Every other element — contacts, coils, timers, latch/unlatch — has a one-to-one relay ancestor. The scan replaces continuous-time relay response with discrete-time cyclic evaluation, trading a few milliseconds of latency for deterministic, reproducible behavior and the ability to re-program without rewiring.

## Worked Example: Translating the Relay Motor Starter to Ladder

The [Relay Logic article](control-circuits.relay-logic.md) develops the canonical **3-wire motor start/stop with overload** circuit. Here is that exact circuit, translated step by step into a ladder program. This is the worked example of the relay-to-ladder translation: every relay element maps to one ladder element.

### The Relay Circuit (recap)

From the relay-logic article, the motor starter is:

```
   RELAY 3-WIRE MOTOR START/STOP (from relay-logic.md):

   L1                                                L2
   |                                                  |
   |  STOP       START      M(aux)                    |
   |  [ / ]  |--[ / ]--|----[  ]----|                 |
   |   NC   |   NO    |   NO seal  |                  |
   |         +--------+---+---------+                 |
   |                       |                          |
   |                      OL   (NC, held closed       |
   |                            while motor OK)       |
   |                       |                          |
   |                  ( M coil )----------------------|
```

Components: STOP (NC push-button), START (NO push-button), M (contactor coil), M-aux (NO seal-in contact on M), OL (NC overload contact).

### Assigning I/O Addresses

First, assign each physical device to a PLC I/O point. The wiring is identical to the relay panel — the PLC input cards replace the relay coils' control-circuit wiring:

| Device | Type | PLC address | Bit state at rest (no actuation) |
|--------|------|-------------|----------------------------------|
| STOP push-button | NC, wired to input | `I:1/0` | 1 (NC closed at rest → input sees current → bit = 1) |
| START push-button | NO, wired to input | `I:1/1` | 0 (NO open at rest → no current → bit = 0) |
| Overload relay (OL) | NC, held closed while OK | `I:1/2` | 1 (NC closed while motor healthy → bit = 1) |
| Motor contactor M | Output coil | `O:2/0` | 0 (off at rest) |

Note the NC-vs-NO wiring carefully: the STOP and OL inputs are 1 at rest (because the NC contacts pass current into the input at rest). The START input is 0 at rest (NO open). These bit states determine whether we use XIC or XIO in the rung.

### Choosing the Instructions

For each input device, choose the instruction that makes the rung conduct *when the device is in its permissive (non-tripped) state*:

- **STOP** (`I:1/0`): we want the rung to conduct while STOP is *not pressed* (resting). At rest, bit = 1. To conduct when bit = 1, use **XIC** `--[ ]-- I:1/0`. Pressing STOP drives the bit to 0, the XIC opens, the rung breaks, the motor stops.
- **START** (`I:1/1`): we want the rung to conduct while START is *pressed*. Pressed, bit = 1. To conduct when bit = 1, use **XIC** `--[ ]-- I:1/1`. Releasing START drives the bit back to 0.
- **OL** (`I:1/2`): we want the rung to conduct while the motor is *healthy* (OL closed). Healthy, bit = 1. To conduct when bit = 1, use **XIC** `--[ ]-- I:1/2`. An overload trips the OL, the bit goes to 0, the XIC opens, the motor stops.
- **Seal-in**: the contactor's own output bit `O:2/0` is fed back as a parallel XIC around the START — once the motor is on, `O:2/0 = 1` holds the rung in via `--[ ]-- O:2/0`.

### The Ladder Diagram (Example 1)

```
   LADDER PROGRAM: 3-WIRE MOTOR START/STOP WITH OVERLOAD SEAL-IN
   Rung 0:

   |   STOP         +--[ ]-- START --+                   |
   |---[ ]-- I:1/0 -|                |----[ ]-- OL ------|( )-- M
   |                +--[ ]-- O:2/0 --+        I:1/2      |    O:2/0
   |                   (seal-in)                         |
   |                                                    |
   |   Truth:  O:2/0 = ( I:1/0 ) AND ( I:1/1 OR O:2/0 )
   |                                 AND ( I:1/2 )       |
   |                                                    |
   |   Trace:  1. START pressed -> I:1/1 = 1 -> rung    |
   |              conducts -> O:2/0 set to 1 -> motor   |
   |              starts.                               |
   |           2. START released -> I:1/1 = 0, but      |
   |              seal-in O:2/0 = 1 (set last scan),    |
   |              so rung still conducts -> motor runs.  |
   |           3. STOP pressed -> I:1/0 = 0 -> rung     |
   |              breaks -> O:2/0 = 0 -> seal opens,    |
   |              motor stops. Releasing STOP (bit -> 1)|
   |              does not restart the motor because    |
   |              O:2/0 is now 0 and START is 0.        |
   |           4. OL trips -> I:1/2 = 0 -> rung breaks  |
   |              -> motor stops. Operator must reset   |
   |              OL (bit -> 1) and press START again.  |
```

This rung is the relay 3-wire starter transcribed element-for-element: the STOP NC contact is the series XIC of `I:1/0`; the START NO contact in parallel with the M-aux seal-in is the two parallel XIC branches of `I:1/1` and `O:2/0`; the OL NC contact is the series XIC of `I:1/2`; the M coil is the OTE of `O:2/0`. The Boolean equation is identical to the relay circuit's equation. The behavior is identical. The only difference is that the seal-in feedback is a wire in the relay panel and a software bit reference in the PLC.

**Latch version (alternative):** the same motor control written with OTL/OTU retentive latches instead of a seal-in contact. Use this when the motor must *restart automatically* after a power flicker (the retentive bit survives the power loss and re-energizes the contactor when power returns). Use the seal-in version (above) when the motor must *not* restart after a power loss (non-retentive — safer for most machinery):

```
   RETENTIVE MOTOR CONTROL (OTL/OTU pair):

   Rung 0 (Latch):   START latches the motor bit on.

   |   STOP            START                            |
   |---[ ]-- I:1/0 ---[ ]-- I:1/1 ------(L)-- MOTOR_BIT|
   |                                       B3:0/0       |
   |                                                    |
   |   (a momentary press of START, while STOP is not   |
   |    pressed, sets B3:0/0 = 1 and holds it)          |

   Rung 1 (Unlatch): STOP or OL clears the motor bit.

   |   STOP          +-- and/or -- OL -----+           |
   |---[/]-- I:1/0 --|                      |--(U)-- MOTOR_BIT
   |                 +--[ ]-- I:1/2 --------+       B3:0/0
   |                                                    |
   |   Note: STOP uses XIO here (trips unlatch when bit |
   |   = 0... see below), or rewire STOP as NO to use   |
   |   XIC. The logic intent: pressing STOP OR OL       |
   |   tripping clears the latch.                       |
   |                                                    |
   |   CAUTION: unlatch-on-OL must be a condition that  |
   |   is TRUE when OL trips (bit I:1/2 -> 0), so use   |
   |   XIO of I:1/2 in the unlatch rung, NOT XIC.       |

   Rung 2 (Drive output): copy the latch bit to the physical output.

   |   B3:0/0                                           |
   |---[ ]-----------------------------------( )-- M   |
   |                                                  O:2/0
```

The two-version comparison is the design decision in ladder logic: **retentive vs non-retentive memory**, chosen per output based on the safety analysis of what should happen on power loss. The seal-in (OTE) version drops the motor on power loss and requires a deliberate START to restart. The OTL/OTU version restarts the motor automatically when power returns — desirable for an unattended remote pump, dangerous for a press brake.

### Example 2: Timer Sequence (Lubrication Pump Before Main Motor)

A common sequential-control requirement: a lube-oil pump must run for 5 seconds to establish bearing pressure before the main motor is allowed to start, and the motor must stop if the pump stops. This uses a TON timer and two rungs:

```
   LADDER PROGRAM: LUBE-PUMP PROVE, THEN MOTOR PERMIT
   (TON timer sequence)

   Rung 0:  Lube pump runs while the system is in RUN mode.

   |   RUN_MODE                              LUBE_PUMP |
   |---[ ]-- B3:1/0 ----------------------( )-- O:2/1 |
   |                                                  |
   |   (RUN_MODE is a latch bit set by the operator's |
   |    START button; covered in a prior rung.)       |

   Rung 1:  Timer T4:0 counts 5.0 s of lube-pump run time.

   |   RUN_MODE        LUBE_PUMP_feedback             |
   |---[ ]-- B3:1/0 ---[ ]-- O:2/1 ---[ TON ]---      |
   |                                    T4:0          |
   |                                    Preset 5000   |
   |                                    (5000 x 1ms   |
   |                                     = 5.0 s)     |
   |                                                  |
   |   (TON increments its accumulator while the rung  |
   |    conducts; when ACC reaches 5000, the .DN bit  |
   |    goes true. If the pump stops, the rung breaks, |
   |    ACC resets to 0, and .DN goes false — proving |
   |    the pump ran the full 5 seconds continuously.)|

   Rung 2:  Motor permit is TRUE only after T4:0 finishes AND pump still runs.

   |   T4:0/DN         LUBE_PUMP_feedback   MOTOR    |
   |---[ ]-------------[ ]-- O:2/1 ------( )-- O:2/0 |
   |                                                  |
   |   (the motor starts 5.0 s after the lube pump    |
   |    starts, and stops immediately if the pump     |
   |    stops, because LUBE_PUMP_feedback drops out   |
   |    of both the timer rung and the motor rung.)   |
   |                                                  |
   |   Trace:  t=0      RUN_MODE set -> LUBE_PUMP on. |
   |           t=0..5s  T4:0 counts, .DN = 0, motor   |
   |                      held off by T4:0/DN = 0.    |
   |           t=5.0s   T4:0/DN -> 1, motor starts.   |
   |           t=12s    LUBE_PUMP stops (fault) ->    |
   |                    rung 1 breaks, T4:0 resets;   |
   |                    rung 2 breaks, motor stops.   |
```

This is the same proving-time sequence a relay panel implements with an on-delay timer relay (TON) whose timed contact enables the main contactor coil. The ladder version is one TON instruction and two contacts, re-programmable in seconds without touching the wiring. Cascading TON timers (T4:0 done enables T4:1, which enables T4:2, ...) builds multi-step startup sequences — the same pattern relay panels built with chains of timer relays, but in software.

## Design Methodology

Translating any relay control circuit into a ladder program follows a fixed procedure:

1. **List the inputs and outputs.** Every push-button, limit switch, pressure switch, and sensor is an input; every contactor, solenoid, valve, and indicator is an output. Assign each an I/O address.
2. **Record the resting bit state of each input.** An NC device (STOP, OL) wired to an input gives bit = 1 at rest; an NO device (START, limit-made) gives bit = 0 at rest.
3. **For each output, write the Boolean condition** that should turn it on, in terms of the inputs. This is usually readable directly off the relay schematic as a series/parallel contact network.
4. **Choose XIC or XIO per input** based on the resting bit state and the permissive condition (conduct when permissive). The rule: if the permissive condition corresponds to bit = 1, use XIC; if it corresponds to bit = 0, use XIO.
5. **Draw the rung** left to right: series conditions for AND, parallel branches for OR, the coil (OTE, or OTL/OTU pair) on the right.
6. **Order the rungs top to bottom in causality order** — a rung that produces a condition (sets a bit) must precede any rung that consumes it, or the consumer sees a one-scan lag.
7. **Choose retentive vs non-retentive memory per output** based on the power-loss safety analysis. Default to OTE (seal-in) for machinery that must not restart; use OTL/OTU only where automatic restart is required.

This methodology is general — it applies to motor starters, interlock matrices, batch sequencers, and any other discrete control problem. The relay schematic is the specification; the ladder program is the executable transcription. Because the notation mirrors the hardware one-to-one, an experienced relay electrician can read a ladder program on sight and a control engineer can transcribe a relay panel into a PLC program in an afternoon.

## Boundary With PLC Hardware

This article teaches the **notation and methodology** — how to read, draw, and design ladder rungs. It does not cover PLC hardware architecture (CPU modules, I/O card types, rack wiring, communication buses, programming terminals), SCADA/HMI integration, or vendor-specific programming software. Those are the [Industrial Control](industrial-control.md) capability, which owns the *platform*; this capability owns the *logic notation* the platform executes. For the embedded-systems perspective on where PLCs sit among MCUs, FPGAs, and bare-metal options (and why the PLC's $50-200/channel cost buys integrated isolation and ladder-logic development speed), see [Embedded Systems](../computing/embedded-systems.md). For the Boolean algebra and digital-logic formalism underlying every contact network, see [Digital Logic](../computing/digital-logic.md).

## See Also

- [Relay Logic Circuits](control-circuits.relay-logic.md) — the relay hardware this notation documents: seal-in/latching, motor starters, interlocks, timer relays. Every ladder rung maps one-to-one onto a relay circuit.
- [Control Circuits](control-circuits.md) — parent capability: the design-pedagogy hub for relay, ladder, and discrete logic.
- [Electrical Systems](electrical-systems.md) — relays, contactors, motors, overload relays, and the industrial wiring that the I/O points of a ladder program connect to.
- [Industrial Control](industrial-control.md) — PLC, SCADA, and HMI platforms that execute ladder programs; owns the hardware platform this notation programs.
- [Embedded Systems](../computing/embedded-systems.md) — where PLCs sit among MCU, FPGA, and bare-metal options for embedded control.
- [Digital Logic](../computing/digital-logic.md) — the Boolean algebra and gate-level formalism that the contact networks implement.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
