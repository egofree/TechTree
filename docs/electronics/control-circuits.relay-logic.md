# Relay Logic Circuits

> **Node ID**: `electronics.control-circuits.relay-logic`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.electrical-systems`](electrical-systems.md),
> [`electronics.passive-components`](passive-components.md)
> **Outputs**: relay-control-logic
> **Timeline**: Years 15-30
> **Critical**: No

Relay logic is the Edison-era art of wiring electromechanical relays and contactors into control circuits that start and stop motors, interlock guards, time sequences, and implement Boolean decisions in hardware. Before programmable controllers, every automated factory line, elevator, and machine tool was a panel of relays wired into logic. Relay logic is the direct ancestor of [ladder logic](./control-circuits.md) (the diagram notation) and of [programmable logic controllers](./industrial-control.md) — a PLC still executes the same rung-by-rung scan of contacts and coils that a relay panel wired physically. This article teaches how to compose contacts into control functions from first principles, assuming you already know what a [relay and contactor](electrical-systems.md) are physically.

## Relay Fundamentals for Logic

A control relay has three parts relevant to logic: the **coil** (an electromagnet), the **armature** (the moving iron that the coil pulls), and the **contacts** (the switches the armature actuates). When you energize the coil with its rated voltage, the armature pulls in and changes every contact's state. When you de-energize, a spring returns the armature and the contacts revert. For relay construction, arc suppression, and contact physics, see [Electrical Systems](electrical-systems.md).

Two contact types are the alphabet of relay logic:

- **NO — normally open**: open (no current passes) when the coil is de-energized; closes when the coil energizes. A resting NO contact blocks current; an energized one passes it.
- **NC — normally closed**: closed (current passes) when the coil is de-energized; opens when the coil energizes. A resting NC contact passes current; an energized one blocks it.

The word "normally" always means *with the coil de-energized* — the resting, shelf state of the relay. This is the single most important convention in control wiring: read every contact as its de-energized state first, then ask what happens when the coil pulls in.

**Contact ratings** determine what a relay can switch. A contact has a continuous current rating (the amps it can carry closed without overheating), a voltage rating (the max voltage it can hold off when open), and a make/break rating (the inrush it can survive on closure and the arc it can extinguish on opening). Switching an inductive load like a motor or solenoid is far harder than switching a resistive load of the same current, because breaking inductive current sustains an arc. For contact ratings by NEMA size and the arcing physics, see the parameter table below.

**Pull-in and drop-out voltage.** A relay coil does not actuate at a single threshold. **Pull-in voltage** (typically 75-85% of rated) is the rising voltage at which the armature finally snaps closed. **Drop-out voltage** (typically 10-30% of rated) is the falling voltage at which the armature releases. The wide hysteresis between them is intentional: it makes the relay immune to brownouts and supply ripple once energized, and gives a decisive snap action rather than a drift. This hysteresis is also why a seal-in contact (below) is reliable — the coil keeps the armature in firmly until voltage collapses well below the holding point.

## Basic Control Functions: AND, OR, NOT

Relay contacts implement Boolean logic directly. The wiring topology — series or parallel — *is* the logic function. There is no abstraction layer between the schematic and the Boolean equation.

**AND — series NO contacts.** Two NO contacts wired one after the other (in series) pass current only when *both* are actuated. If contact A is open OR contact B is open, the circuit is broken. This is a logical AND.

```
   L1                                L2
   |                                  |
   |----[ A ]----[ B ]----( LOAD )----|
   |
   NO           NO         coil/relay
 (A actuated  (B actuated   energizes only
  = closed)    = closed)     when A AND B)
```

**OR — parallel NO contacts.** Two NO contacts wired side by side (in parallel) pass current when *either* is actuated. Current flows if A closes OR B closes. This is a logical OR.

```
   L1                                L2
   |                                  |
   |----+-----------------------------|
   |    |                             |
   |   [A]          ( LOAD )          |
   |    |                             |
   |   [B]                            |
   |    |                             |
   |----+-----------------------------|
   |
   NO paths in parallel: A OR B closes -> load energizes
```

**NOT — an NC contact.** A normally-closed contact inverts. With the coil de-energized the NC contact passes current (output "on"); when the coil energizes the contact opens and the output goes "off." A single NC contact in series with a load is a logical NOT — the load is on *unless* the relay is energized. This is the basis of fail-safe wiring: a de-energized relay presents closed contacts so that a broken wire or lost power drops the load out safely (the stop function defaults to safe).

These three compose into every combinatorial function. Series-parallel networks of NO/NC contacts implement arbitrary sum-of-products Boolean expressions, exactly as digital logic gates do — relay logic *is* gate logic, built from metal and magnetism instead of silicon. The formal Boolean algebra that describes both is covered in [Digital Logic](../computing/digital-logic.md); this article stays on the hardware.

## Memory: The Seal-In (Latching) Circuit

The most important relay circuit ever invented is the **seal-in** (also called latching or holding) circuit. It gives a relay *memory*: a momentary push of a button turns a load on, and the load stays on after the button is released, until a separate stop button breaks the circuit. Without seal-in, every control function would need a maintained (held-down) switch; with it, a tap of a finger latches megawatts of machinery.

The circuit works by wiring an auxiliary NO contact of the relay's *own* coil in parallel with the momentary start button. Once the coil energizes, its own contact closes and supplies current by a second path, bypassing the start button:

```
                SEAL-IN / LATCHING CIRCUIT

   L1 (hot)                                L2 (neutral)
   |                                        |
   |   STOP          START      M aux       |
   |   [ / ]    |--[ / ]--|----[  ]--|      |
   |    NC     |   NO     |   NO    |       |
   |           |          |  (seal) |       |
   |           +----------+---------+       |
   |                                 |      |
   |                            ( M )-------|
   |                              coil      |
   |                                        |
   | START = momentary NO push-button       |
   | STOP  = momentary NC push-button       |
   | M aux = auxiliary NO contact on coil M |
```

Sequence of operation:

1. **Rest.** Coil M is de-energized. M aux is open. STOP is closed (NC rests closed). START is open (NO rests open). No current flows.
2. **Start pressed.** Current flows L1 → STOP (closed) → START (held closed) → M aux (open, irrelevant) → coil M → L2. The coil energizes.
3. **Seal-in.** Coil M energizes → M aux snaps closed. Now current flows through *two* parallel paths: through START and through M aux. The coil is holding itself in.
4. **Start released.** START springs open. But M aux is still closed (coil is still energized), so current continues through the M aux path. The load stays on — the relay "remembers" the start command.
5. **Stop pressed.** STOP opens (NC contact breaks the only remaining current path). Coil M de-energizes → M aux opens. The seal is broken. Releasing STOP restores its NC contact, but now neither START nor M aux passes current, so the coil stays off until START is pressed again.

This is one bit of memory. A relay panel of dozens of seal-in circuits holds the state of an entire production line. The same pattern — a device that latches itself via its own auxiliary contact until a break condition occurs — underlies every latch, set-reset flip-flop, and holding register in digital logic and in PLC programming.

## Motor Start/Stop with Overload (3-Wire Control)

The seal-in circuit becomes industrial motor control by adding a **contactor** (a heavy-duty relay rated for motor current) and an **overload relay** (OL) that protects the motor from sustained overcurrent. This is the canonical 3-wire motor control circuit — the most replicated control circuit in industry.

```
         3-WIRE MOTOR START/STOP WITH OVERLOAD

   L1                                                L2
   |                                                  |
   |   STOP       START      M(aux)                   |
   |   [ / ]  |--[ / ]--|----[  ]----|                |
   |    NC   |   NO    |   NO seal  |                 |
   |         +--------+---+---------+                 |
   |                       |                          |
   |                      OL   <-- overload relay     |
   |                    (NC,                          |
   |                   held closed                    |
   |                   while OK)                      |
   |                       |                          |
   |                  ( M coil )----------------------|
   |                    contactor                     |
   |                    coil                          |
   |                                                  |
   |  M coil also closes the 3-pole MAIN power        |
   |  contacts that apply 3-phase line voltage        |
   |  to the motor terminals (drawn separately).      |
```

Components:

- **STOP** — momentary NC push-button. Resting closed; pressing opens the circuit.
- **START** — momentary NO push-button. Resting open; pressing closes the circuit.
- **M (coil)** — the contactor coil. Energizing it closes the main power contacts that apply line voltage to the motor (drawn separately from the control circuit).
- **M (aux)** — an auxiliary NO contact on the contactor, wired in parallel with START as the seal-in.
- **OL** — overload relay. A NC contact held closed while motor current is within limits. If the motor draws excessive current long enough to heat the OL element (a bimetallic strip or eutectic alloy), the OL contact opens and drops out the contactor — exactly like pressing STOP. The OL contact is wired in series with the coil so that any overload trips the seal-in. The OL must be manually reset after it cools.

Operation is the seal-in sequence with the OL as an automatic stop. Pressing START energizes M, which seals itself in via M aux. The motor runs until either STOP is pressed (manual stop) or OL opens (motor overloaded). Because the OL contact is in series with the seal-in path, an overload trips the latch and the motor cannot restart on its own — the operator must clear the fault, reset the OL, and press START again. This is fail-safe: a fault leaves the motor off.

### Worked Example: Sizing a Contactor for a 5 HP, 460 V Motor

A 3-phase induction motor draws approximately **1.2 A per HP at 460 V**. For a 5 HP motor:

- **Full-load current (FLC):** 5 × 1.2 = **6.0 A** (the NEC table value is 7.6 A for a typical 5 HP 460V motor — always use the nameplate or NEC Table 430.250 value; the 1.2 A/HP rule is a rough estimate).
- **Starting (inrush) current:** 5-8× FLC, so roughly **38-61 A** for the 0.5-5 seconds it takes the motor to reach speed. The contactor must close against and the OL must tolerate this surge without tripping (the OL is timed to ride through inrush).
- **Contactor selection (NEMA size):** Per NEMA ICS 2, a **Size 1** contactor is rated 30 A continuous with an AC-3 (motor starting) rating of 10 HP at 460 V — ample headroom for a 5 HP motor. A Size 0 (15 A, 3 HP at 460 V) would be marginal; a Size 1 is the standard choice for 5 HP, providing the contact margin and arcing capacity for tens of thousands of start cycles.
- **Overload relay setting:** Set the OL to the motor nameplate FLC (7.6 A). A Class 10 OL trips within 10 seconds at 600% of FLC (riding through the start inrush, which lasts <5 seconds), protecting a motor with a 1.0 service factor. For motors that start frequently or have high inertia, use a Class 20 (trips in 20 s at 600%) to avoid nuisance tripping.
- **Control circuit voltage:** The coil M is often powered at 120 V or 24 V (stepped down from line voltage by a control transformer) so that push-buttons in the operator station carry safe, low voltage. The contactor's main contacts still switch the full 460 V motor power, isolated from the control circuit.

This is the same arithmetic every motor-control center (MCC) bucket is built from. See [Electrical Systems](electrical-systems.md) for motor selection, NEC ampacity tables, and MCC construction.

## Timer Relays

A timer relay delays the change of a contact relative to its coil. Where a plain relay's contacts follow the coil instantly (5-15 ms), a timer relay's contacts wait a preset interval — the foundation of sequential control. Two families cover most needs:

- **On-delay (TON):** when the coil energizes, the timer begins counting. After the preset delay, the timed contacts change state (NO closes, NC opens). When the coil de-energizes, the contacts revert instantly. Mnemonic: "delayed on, instant off." Used to start equipment only after a prerequisite has been stable for a proving time (e.g., lube-oil pump must run 10 s before the main motor can start).
- **Off-delay (TOF):** when the coil energizes, the contacts change instantly. When the coil de-energizes, the timer holds the new state for the preset delay before reverting. Mnemonic: "instant on, delayed off." Used to keep a fan or purge running for a cooldown period after a furnace stops.

Historically these were pneumatic (an air dashpot slowed the armature) or motor-driven (a small synchronous motor ran a cam through a gear train after the coil engaged). Modern timers are electronic (RC or crystal), but the contact behavior is identical. Timers compose into sequence logic: TON-A completes and enables a second TON-B, cascading operations in time order the way seal-in cascades them in state order.

## Interlocks

An interlock is a wiring pattern that *prevents* an unsafe combination of states, usually by feeding a NC contact from one device into the control circuit of another so that one being on forces the other off. Interlocks are the hardware ancestor of PLC safety logic.

**Forward/reverse motor interlock.** A 3-phase motor reverses direction by swapping two of the three phase leads. This is done with two contactors — F (forward) and R (reverse) — where R crosses two phases. If F and R ever close at the same time, the crossed phases create a dead short across the line (a phase-to-phase fault) that destroys the contactors. The interlock prevents this: each contactor's coil circuit passes through a NC auxiliary contact of the *other* contactor. Energizing F opens F's NC contact in R's coil circuit, so R cannot energize while F is on — and vice versa.

```
       FORWARD / REVERSE MOTOR INTERLOCK

   L1                                                  L2
   |                                                    |
   |  STOP                                              |
   |  [ / ]--+------------------------------------------|
   |   NC   |                                           |
   |        |                                           |
   |   FWD      REV          F aux        R aux         |
   |  [ / ]   [ / ]      +--[ / ]--+--[ / ]--+          |
   |   NO     NO        |   NC    |   NC    |          |
   |        |           | (in R   | (in F   |          |
   |        |           |  ckt)   |  ckt)   |          |
   |        |           |         |         |          |
   |        +--F coil---+         |         |          |
   |        |                     |         |          |
   |        +----------R coil-----+---------+          |
   |                                                    |
   |  F coil path passes through R aux(NC):             |
   |    if R is energized, R aux opens -> F cannot run  |
   |  R coil path passes through F aux(NC):             |
   |    if F is energized, F aux opens -> R cannot run  |
   |  => Both can NEVER be on simultaneously.           |
```

The diagonal NC contacts are the interlock. This pattern — a NC contact of device X placed in series with the coil of mutually-exclusive device Y — is called **electrical interlocking**. Critical reversing starters add **mechanical interlocking** as well: a physical tie-bar between the two contactors so that even if both coils somehow energize, the armatures cannot both close. Belt and suspenders for line faults.

**Sequence interlocks.** The same NC-contact-in-series technique sequences operations: pump P1 must run before pump P2 (P2's coil passes through a NO aux contact of P1, so P2 cannot start until P1 is on), or heater H must be off before a door can open (the door latch solenoid passes through a NC aux of H). Any "A only if B" relationship is one auxiliary contact.

## Relay Logic vs Digital Logic

A relay panel of seal-in circuits, timers, and interlocks is, mathematically, a sequential logic machine — a collection of combinatorial functions (AND/OR/NOT contact networks) feeding memory elements (seal-in latches) clocked by timers and external events. This is precisely the structure of the flip-flop-and-gate state machines built later from transistors and ICs. The relay computer era (the [Zuse Z3 and Harvard Mark I](../computing/electromechanical.md)) proved that relay logic can implement arbitrary computation; the only limits were speed (5-15 ms per relay vs. nanoseconds per gate) and reliability (a 2,000-relay machine expected a failure every few hours).

This continuity is why the article sits under [Control Circuits](./control-circuits.md): relay logic is the hardware foundation that the [ladder logic](./control-circuits.md) diagram notation formalized and that [programmable logic controllers](./industrial-control.md) later automated. A PLC does not replace relay logic — it *emulates* it, scanning a stored program of virtual contacts and coils that map one-to-one onto the relay schematic above. The seal-in rung in a PLC ladder program is the same circuit, drawn the same way, executing the same Boolean equation. Learning relay hardware first is what makes ladder logic and PLC programming intelligible rather than arbitrary.

## Contact Ratings and NEMA Contactor Sizes

Contact ratings determine what each device can switch and survive. The voltage rating is the maximum the open contact can hold off without arcing across the gap; the current rating is the continuous amps the closed contact can carry without overheating; the making/breaking rating is the transient current it can close against and interrupt without welding or excessive arc erosion. Inductive loads (motors, solenoids, coils) are the hard case — breaking inductive current sustains an arc far longer than resistive current of the same magnitude, so contact life is dominated by the inductive breaking duty.

| NEMA Size | Continuous Current | AC-3 Motor HP @ 460 V 3-phase | Typical Use | Arc Chute |
|-----------|--------------------|-------------------------------|-------------|-----------|
| 00 | 9 A | 1.5 HP | Small fans, pumps (<1 kW) | Simple splitter |
| 0 | 18 A | 3 HP | Small conveyors, blowers | Splitter plates |
| 1 | 27 A | 7.5 / 10 HP | General industrial motors | Magnetic blowout |
| 2 | 45 A | 15 / 25 HP | Medium pumps, compressors | Magnetic blowout |
| 3 | 90 A | 30 / 50 HP | Large fans, crushers | Arc chute + grid |
| 4 | 135 A | 60 / 100 HP | Main process drives | Arc chute + grid |
| 5 | 270 A | 150 / 200 HP | High-power mills | Vacuum / SF6 |
| 6 | 540 A | 300 / 400 HP | Very large drives | Vacuum / SF6 |

Notes on the table: the AC-3 rating (motor starting, 6× inrush make, full-load break) is lower than the continuous current rating because starting an induction motor stresses the contacts far more than steady-state running. The "make" must close against 5-8× FLC without bouncing or welding; the "break" must extinguish the arc of an inductive load. **Arc chutes** (splitter plates that divide and cool the arc, or magnetic blowout coils that stretch the arc upward into the chute) are what let a contactor interrupt motor current at all — without them the arc would sustain across the gap until it destroyed the contacts. AC current is easier to interrupt than DC of the same voltage because the AC current passes through zero twice per cycle (100/120 times per second), giving the arc a chance to extinguish; DC arcs never self-quench and need much more aggressive suppression. For the underlying arc physics, contact materials (AgCdO, AgSnO₂), and snubber circuits, see [Electrical Systems](electrical-systems.md).

Control-circuit relays (the small relays that implement the AND/OR/seal-in logic, distinct from the power contactors that switch the motor) typically have contacts rated 6-10 A at 120-240 V AC — enough to switch a contactor coil directly and to carry the control-circuit current, but not to switch motor power.

## See Also

- [Control Circuits](./control-circuits.md) — parent capability: the design-pedagogy hub for relay, ladder, and discrete logic.
- [Electrical Systems](electrical-systems.md) — relays, contactors, motors, overload relays, arc suppression, and NEMA sizing; the physical components this logic is built from.
- [Passive Components](passive-components.md) — resistors, inductors, and transformers used in control-circuit timing and conditioning networks.
- [Industrial Control](./industrial-control.md) — PLCs and SCADA that emulate relay logic in software.
- [Electromechanical Computing](../computing/electromechanical.md) — relay history, relay computers, and the bridge from relays to electronic computing.
- [Digital Logic](../computing/digital-logic.md) — the Boolean algebra and gate-level formalism that relay logic implements in hardware.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
