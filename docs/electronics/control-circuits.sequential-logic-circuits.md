# Sequential Logic Circuits

> **Node ID**: `electronics.control-circuits.sequential-logic-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md),
> [`electronics.passive-components`](passive-components.md),
> [`electronics.control-circuits.discrete-logic-circuits`](control-circuits.discrete-logic-circuits.md)
> **Outputs**: sequential-logic-designs
> **Timeline**: Years 25-45
> **Critical**: No

A **sequential** circuit differs from a **combinational** one in a single decisive way: its output depends not just on the *current* inputs but on the *history* of past inputs, because the circuit stores state. The [Discrete Logic Circuits](control-circuits.discrete-logic-circuits.md) article showed how to build gates that compute AND, OR, NOT in the instant; this article shows how to add **feedback** so those gates *remember* a bit, latch it on a clock edge, count pulses, and shift data down a register. It is the circuit-level hardware behind every counter, register, and memory cell. It assumes you have read the [discrete-logic](control-circuits.discrete-logic-circuits.md) article and understand gate symbols and logic levels.

> **Boundary statement.** This article covers how latches, flip-flops, counters, and shift registers are *built* and *used* as electronic components (gate-level circuits and 74xx/4000-series ICs). For state-machine design methodology, state encoding (one-hot vs binary vs Gray), HDL coding of sequential logic, and FPGA register inference, see [Digital Logic](../computing/digital-logic.md) and [Logic Design](../computing/logic-design.md). Those articles teach the *systematic methodology* for designing complex sequential systems; this one teaches the *components*.

## The Idea of Feedback: Why a Gate Becomes a Memory

Take the output of an inverter and feed it back to its input, and you have built an oscillator (the output chases its own negation forever). Take the output of two inverters in series and feed *that* back, and you have a loop that can sit in one of two stable states indefinitely — a **bistable** element. That is the [bistable multivibrator](analog-circuits.multivibrator-circuits.md), the discrete-transistor ancestor of every flip-flop. The same idea, built from logic gates rather than discrete transistors, is the **SR latch**.

## SR Latch

The simplest memory element is two cross-coupled NOR gates. The output of each NOR feeds an input of the other, forming a feedback loop with two stable states.

```
       NOR SR LATCH (active-high inputs)

              SET (S) -----+
                           |
                        +--+--+
                        | NOR |----+----> Q
                        +-----+    |
                           |       |
                          (cross-coupling)
                           |       |
                        +--+--     |
              RESET (R) -+ NOR |<--'  (Q feeds back)
                        +-----+
                           |
                           +----> Q-bar (complement of Q)

   S=1, R=0 -> SET   : forces Q=1, Q-bar=0
   S=0, R=1 -> RESET : forces Q=0, Q-bar=1
   S=0, R=0 -> HOLD  : outputs retain previous state (memory!)
   S=1, R=1 -> FORBIDDEN: both outputs go 0 (not complementary); next state unpredictable
```

**Operation.** When S=1 and R=0, the top NOR (with S=1) outputs 0 regardless of its other input, so Q-bar = 0. That 0 feeds the bottom NOR along with R=0, so the bottom NOR outputs Q = 1. The latch is **set**. Remove S (S→0) and Q stays 1, because Q-bar is still 0 (held by the now-stable loop), so the bottom NOR still sees two 0 inputs. The latch *remembers* the set command.

When R=1 and S=0, the symmetric process forces Q=0, Q-bar=1. The latch is **reset**. Remove R and it holds the reset.

When S=0 and R=0 simultaneously (after a set or reset), both NOR outputs depend on the feedback. The loop settles into whichever state it was already in — this is the **hold** mode, the defining behavior of a memory element. The state persists indefinitely with no further input.

**The forbidden state.** When S=1 and R=1, both NOR gates output 0 (each sees a 1 input). This violates the invariant that Q and Q-bar are complements — both are 0. The danger is in *leaving* the forbidden state: if S and R both drop to 0 at the same instant, both NOR gates briefly see all-0 inputs and both try to output 1. Whichever gate is fractionally faster wins, and the latch settles into an unpredictable state. This **race condition** is why S=R=1 is forbidden for the NOR latch.

### NAND SR Latch (Active-Low)

The same circuit built from NAND gates is **active-low**: the set and reset inputs are normally held HIGH, and a LOW pulse performs the action.

| S-bar | R-bar | Q | Mode |
|-------|-------|---|------|
| 0 | 1 | 1 | Set |
| 1 | 0 | 0 | Reset |
| 1 | 1 | Q_prev | Hold |
| 0 | 0 | — | Forbidden (both outputs 1) |

The NAND latch is preferred in some families because NAND gates are slightly cheaper than NOR in TTL and CMOS (see the [discrete-logic](control-circuits.discrete-logic-circuits.md) article). The active-low convention matches the de-asserted state to the "resting" level of the inputs.

## Clocked SR Latch (Gated Latch)

The plain SR latch responds to its inputs *immediately* — any bounce on the S or R line is latched. A **clocked** (or gated) latch adds an enable input (the clock) so that the latch only responds to S and R during a specific window.

```
       CLOCKED SR LATCH

   S ---+---\
        |    \      +-----+
   CLK -+-----|AND |-----|NOR  |---+---> Q
        |    /      | (SR)|   |
   R ---+---/       +-----+   |
                             (cross-coupled as before)

   CLK=0 -> both AND gates output 0 -> latch HOLD (ignores S, R)
   CLK=1 -> S and R pass through to the underlying SR latch -> normal SR behavior
```

When CLK=0, the AND gates block S and R; the latch sees S=R=0 and holds. When CLK=1, S and R reach the latch and it sets or resets as commanded. This makes the latch **transparent** while the clock is HIGH — Q follows S and R with the usual SR behavior, every moment the clock stays high. That transparency is a problem for cascaded designs (a change in Q can propagate through downstream logic and come back as a new S or R within the same clock-high period, causing multiple transitions). The fix is the edge-triggered flip-flop.

## D Flip-Flop (Edge-Triggered)

The **D (data) flip-flop** is the fundamental register element of modern digital design. It captures the value of the D input at the moment of the clock edge and holds it until the next edge. Between edges, the output does not change even if D wiggles — the flip-flop is **not transparent**.

The canonical implementation is the **master-slave** D flip-flop: two cascaded gated D latches with opposite clock phases. The master latch samples D while the clock is HIGH; the slave latch updates Q on the falling edge. The result is negative-edge-triggered behavior: Q changes only at the clock falling edge, sampling whatever D was at that moment.

```
       MASTER-SLAVE D FLIP-FLOP (negative-edge-triggered)

          +-------------+        +-------------+
   D ---->| Master      |------->| Slave       |----> Q
          | D Latch     |  Qm    | D Latch     |
   CLK --+|> (transparent|       | (transparent|
          |  when CLK=1)|        |  when CLK=0)|
          +-------------+        +-------------+
                 |
                CLK is inverted for the slave

   CLK=1 (high phase): master transparent  -> Qm follows D
                        slave opaque        -> Q holds old value
   CLK 1->0 (falling edge): master freezes Qm = D(at edge)
                            slave transparent -> Q = Qm
   CLK=0 (low phase): master opaque, slave transparent -> Q stable at Qm

   => Q updates to D only on the falling clock edge. Non-transparent between edges.
```

**The 7474** is the canonical TTL dual positive-edge-triggered D flip-flop. It adds asynchronous **preset** (set Q=1) and **clear** (set Q=0) inputs that act independently of the clock — used for system reset on power-up. The **4013** is the CMOS 4000-series dual D flip-flop equivalent.

### Truth Table (7474, positive-edge-triggered)

| CLK | D | PRE | CLR | Q(next) | Mode |
|-----|---|-----|-----|---------|------|
| ↑ | 0 | 1 | 1 | 0 | Capture 0 |
| ↑ | 1 | 1 | 1 | 1 | Capture 1 |
| 0/1 | X | 1 | 1 | Q(prev) | Hold (no edge) |
| X | X | 0 | 1 | 1 | Async Preset |
| X | X | 1 | 0 | 0 | Async Clear |
| X | X | 0 | 0 | — | Forbidden |

(↑ = rising edge, X = don't care. PRE and CLR are usually active-low on the actual 7474.)

**Characteristic equation:** Q(next) = D. This is the simplest possible — the next state equals the data input at the clock edge. This simplicity is why the D flip-flop has displaced all other types in modern ASIC and FPGA design.

## JK Flip-Flop

The **JK flip-flop** generalizes the SR latch and removes the forbidden state. J is the "set" input, K is the "reset" input, and when J=K=1 the flip-flop **toggles** (Q flips to its complement on every clock edge). This eliminates the race condition of the SR latch: there is no invalid input combination.

| J | K | Q(next) | Mode |
|---|---|---------|------|
| 0 | 0 | Q(prev) | Hold (no change) |
| 1 | 0 | 1       | Set |
| 0 | 1 | 0       | Reset |
| 1 | 1 | Q-bar(prev) | Toggle |

**Characteristic equation:** Q(next) = J·Q-bar(prev) + K-bar·Q(prev). The toggle mode (J=K=1) makes the JK flip-flop a natural 1-bit counter: wire J=K=1 and the output flips on every clock edge, dividing the clock frequency by 2.

The **7473** and **74112** are TTL JK flip-flops. Historically the JK was the workhorse of counter design in the 1970s, but it has been largely replaced by the D flip-flop in modern design because (a) the D flop uses fewer transistors, (b) scan-chain testing (essential for ASIC manufacturing test) is simpler with D flops, and (c) a toggle is easily built from a D flop by feeding Q-bar back to D. The JK remains useful in teaching and in discrete-IC counter circuits.

## T Flip-Flop

The **T (toggle) flip-flop** changes state on every clock edge when T=1, and holds when T=0. It is the JK flip-flop with J tied to K; or equivalently a D flip-flop with Q-bar fed back to D.

| T | Q(next) | Mode |
|---|---------|------|
| 0 | Q(prev) | Hold |
| 1 | Q-bar(prev) | Toggle |

**Characteristic equation:** Q(next) = T ⊕ Q(prev) (T XOR Q). When T=1, the output toggles every clock edge, dividing the input frequency by exactly 2. This is the basis of every binary counter: a chain of T flip-flops divides the clock by 2, 4, 8, 16, ... at each successive stage.

The T flip-flop is rarely sold as a standalone IC; it is built by wiring a JK with J=K=T, or a D with D = Q-bar (permanently toggling). The toggle behavior is what makes the ripple counter (below) work.

## Counters

### Ripple (Asynchronous) Counter

A **ripple counter** cascades T flip-flops so that the output of one drives the clock of the next. Each stage divides its input frequency by 2, so an N-stage counter divides by 2^N.

```
       4-BIT RIPPLE (ASYNCHRONOUS) COUNTER

   INPUT CLOCK ---->|T FF1|---->|T FF2|---->|T FF3|---->|T FF4|
                    | (Q0)|     | (Q1)|     | (Q2)|     | (Q3)|
                     toggle      toggle      toggle      toggle
                     every       every 2     every 4     every 8
                     input       inputs      inputs      inputs

   Q0 = input / 2
   Q1 = input / 4
   Q2 = input / 8
   Q3 = input / 16
   Q3Q2Q1Q0 = binary count 0000 .. 1111 (16 states)
```

Each flip-flop is wired to toggle permanently (J=K=1, or T=1). The first flip-flop toggles on every input clock edge (Q0 = clock/2). The second flip-flop's clock *is* Q0, so it toggles every time Q0 changes (Q1 = Q0/2 = clock/4). And so on: the count "ripples" through the chain, each stage triggering the next, which is why this is called an **asynchronous** or **ripple** counter — there is no common clock; the stages trigger one another in sequence.

**Worked example: frequency division by 16.** A 1 MHz input clock feeds a 4-bit ripple counter. The output frequency at each stage:

| Stage | Output | Frequency | Period |
|-------|--------|-----------|--------|
| Input | —      | 1.000 MHz | 1.000 µs |
| Q0    | FF1    | 500.000 kHz | 2.000 µs |
| Q1    | FF2    | 250.000 kHz | 4.000 µs |
| Q2    | FF3    | 125.000 kHz | 8.000 µs |
| Q3    | FF4    | **62.500 kHz** | 16.000 µs |

So Q3 (the fourth bit) produces a clean **62.5 kHz** square wave — the original 1 MHz divided by 2^4 = 16. The binary count Q3Q2Q1Q0 cycles 0000 → 0001 → 0010 → ... → 1111 → 0000 every 16 input cycles. This is a **divide-by-16 counter**, and it doubles as a 4-bit binary counter for counting events. The **7493** is a TTL 4-bit ripple counter in a single IC.

**Ripple delay.** The ripple counter's weakness is that the count does not update instantaneously — each stage waits for the previous one to toggle, and each flip-flop has a propagation delay (t_pd ≈ 10–50 ns depending on family). For a 4-stage counter, the worst-case settling time is 4 × t_pd. The output bits briefly display a wrong count (the "ripple through" glitches) before settling. For a display or a slow control signal this is invisible; for feeding the count directly into combinational decode logic (like a 7-segment decoder), the glitches produce brief false readings. The fix is the **synchronous counter**.

### Synchronous Counter

A **synchronous counter** clocks all flip-flops from the *same* clock, so they all update simultaneously on the same edge. The logic that decides whether each flip-flop toggles is computed from the *current* count, not from a delayed ripple. The result: no settling delay, no glitches, and a maximum count frequency limited by a single flip-flop's t_pd plus the decode-logic delay, not by the number of stages.

The toggle logic is: a stage toggles only when all lower stages are 1 (the "ripple carry" is pre-computed rather than propagated). So FF2 toggles when Q0 AND Q1 are both 1; FF3 toggles when Q0 AND Q1 AND Q2 are all 1; and so on. Each stage's T input is the AND of all previous Q outputs, computed with a gate rather than waited for through a chain. The **74160–74163** are synchronous 4-bit counters in TTL.

The trade-off: a synchronous counter needs more gates (the AND-network grows with each stage), but the count updates in one t_pd. For any counter that must feed decode logic or run above a few MHz, synchronous is mandatory.

## Shift Registers

A **shift register** is a chain of flip-flops clocked together, with each flop's Q feeding the D of the next. On every clock edge, the data shifts one position down the chain. The shift register is the hardware for serial-to-parallel and parallel-to-serial conversion, for delay lines, and for serial arithmetic.

```
       4-BIT SERIAL-IN / PARALLEL-OUT SHIFT REGISTER

   Serial In --+-->|D FF1|-->|D FF2|-->|D FF3|-->|D FF4|
               |   | (Q0)|   | (Q1)|   | (Q2)|   | (Q3)|
               |    | ^ |    | ^ |    | ^ |    | ^ |
               |    +-|-+    +-|-+    +-|-+    +-|-+
               |      |        |        |        |
               |     CLK      CLK      CLK      CLK  (all clocked together)
               |
               +-- Q0 feeds D1, Q1 feeds D2, Q2 feeds D3 (shift right)

   Parallel Out: Q0 Q1 Q2 Q3 (read all four after 4 clock edges)
```

**Serial-in / serial-out (SISO):** data enters at the left, shifts right one position per clock, exits at the right after N clocks. This is a **delay line** of N clock periods. The **7491** is an 8-bit SISO TTL shift register.

**Serial-in / parallel-out (SIPO):** data enters serially at the left, and after N clocks the full N-bit word is available in parallel at all Q outputs. This is how a serial data stream (from a sensor, a radio, or a USB cable) is converted into a parallel byte for a processor to read. The **74164** is an 8-bit SIPO TTL shift register. The **4094** is the 4000-series CMOS equivalent.

**Parallel-in / serial-out (PISO):** a parallel word is loaded into all flip-flops at once (via a load/shift control), then shifted out one bit per clock. This is how a parallel byte from a processor is serialized for transmission over a single wire. The **74165** is an 8-bit PISO TTL shift register.

**Universal shift register:** combines all modes — serial-in left, serial-in right, parallel-in, parallel-out, hold — under control of two mode-select pins. The **74194** is a 4-bit universal shift register; the **74198** is an 8-bit version. This is the most flexible single-chip shift register and the basis of most discrete-IC register designs.

**Ring counter:** a shift register with its last output fed back to its first input. A single 1 bit circulates around the ring, producing a one-hot sequence (0001 → 0010 → 0100 → 1000 → 0001). Used for state-machine sequencing and as a simple decoded counter (no decode gates needed, since the one-hot output directly selects one of N states).

## Clocks and Timing

Every flip-flop is governed by its **clock** — the signal whose edge triggers the state change. The timing relationships around that edge are what make or break a sequential circuit.

### Setup and Hold Time

- **Setup time (t_su):** the data input D must be **stable** (not changing) for at least t_su *before* the clock edge. If D is still settling when the edge arrives, the master latch may capture an intermediate (wrong) value.
- **Hold time (t_h):** D must remain stable for at least t_h *after* the clock edge. If D changes too quickly after the edge, the master latch may release before the slave has fully captured the value.

For a 7474 at 5 V, t_su ≈ 20 ns and t_h ≈ 5 ns. For a 74HC74 at 5 V, t_su ≈ 10 ns and t_h ≈ 0 ns (modern CMOS processes have driven hold time toward zero). These numbers define a **sampling window** of t_su + t_h around the edge during which D must not change.

### Propagation Delay and Maximum Clock Frequency

- **Clock-to-Q propagation delay (t_pd or t_CQ):** the time from the clock edge to the moment Q actually reflects the new value. For a 7474, t_pd ≈ 25 ns; for a 74HC74, ~15 ns.
- **Maximum clock frequency (f_max):** the clock period must be long enough for Q to update, for the combinational logic between flip-flops to settle, and for the next flip-flop's setup time to be met:

```
   T_clk ≥ t_pd,FF + t_pd,logic + t_su

   f_max = 1 / (t_pd,FF + t_pd,logic + t_su)
```

**Worked example.** A shift register (Q of one flop feeds D of the next, no logic between): t_pd,FF = 25 ns (7474), t_pd,logic = 0, t_su = 20 ns. T_clk ≥ 25 + 0 + 20 = 45 ns, so f_max = 1 / 45 ns ≈ 22 MHz. Pushing the clock faster than this guarantees setup violations and metastability.

### Metastability

If D changes within the sampling window (violating setup or hold), the master latch's internal cross-coupled inverter loop is left in an **indeterminate** state — neither a clean 1 nor a clean 0, but a voltage that hovers at mid-rail. This is **metastability**. The output will eventually resolve to a valid 0 or 1, but the resolution time is unbounded (it depends on how close to the metastable point the latch landed — a statistical phenomenon).

Metastability is unavoidable when sampling an **asynchronous** signal (one not synchronized to the clock) — for example, a debounced switch input, or data crossing between two different clock domains. The standard mitigation is a **two-stage synchronizer**: two D flip-flops in series, clocked by the system clock. The first flop has a high probability of going metastable if the input changes near the edge, but the metastability has a full clock period to resolve before the second flop samples it. The probability of metastability propagating through both flops falls off exponentially with the clock period, making it vanishingly small at any reasonable clock rate. This is why every asynchronous input to a clocked system goes through a synchronizer.

## Flip-Flop Parameter Comparison

| Flip-Flop | Triggering | Characteristic Equation | Typical TTL IC | Typical CMOS IC |
|-----------|------------|------------------------|----------------|------------------|
| SR latch | Level (transparent) | Q = S + R-bar·Q | 74279 (quad SR) | 4043 (quad NOR SR) |
| Gated D latch | Level (transparent when CLK=1) | Q = D while CLK=1 | 7475 (quad D latch) | 4042 (quad D latch) |
| D flip-flop | Edge (rising or falling) | Q(next) = D | 7474 (dual, rising-edge) | 4013 (dual D FF) |
| JK flip-flop | Edge | Q(next) = J·Q-bar + K-bar·Q | 7473, 74112 (dual JK) | 4027 (dual JK FF) |
| T flip-flop | Edge | Q(next) = T ⊕ Q | (built from JK with J=K) | (built from 4013 with D=Q-bar) |

**Which to use?** For any new design, the **D flip-flop** is the universal choice — it is what modern synthesis tools target, it is what FPGAs are built from (their lookup-table-plus-register cells are D-based), and it is the simplest to analyze. Use JK only when porting an older discrete-IC counter design (the 7490 decade counter, the 7493 binary counter are internally JK-based). Use the level-sensitive D latch only when you specifically need transparency (e.g., address latching in a microprocessor bus), not for general storage.

## From Components to Systems

The components in this article — latches, flip-flops, counters, shift registers — are the alphabet of sequential hardware. Wire a shift register to an adder and you have a serial accumulator. Wire a counter to a decoder and you have a sequencer. Wire a state register to next-state logic and you have a finite-state machine. Each of these is a combinatorial explosion of design choices: state encoding, clocking scheme, reset strategy, timing closure. The systematic methodology for making those choices — state diagrams, Karnaugh-map minimization of next-state logic, HDL coding patterns — is the subject of [Logic Design](../computing/logic-design.md). This article stops at the components; that one starts at the systems.

The arc from [relay logic](control-circuits.relay-logic.md) (the seal-in latch as the first memory element) through the [discrete gates](control-circuits.discrete-logic-circuits.md) of TTL and CMOS to the flip-flops and counters here traces the physical implementation of one idea: **feedback creates memory, and clocked feedback creates synchronized memory that scales into computation.**

## See Also

- [Control Circuits](control-circuits.md) — parent capability: the design-pedagogy hub.
- [Discrete Logic Circuits](control-circuits.discrete-logic-circuits.md) — the companion article: the gates (NAND, NOR, AND, OR, XOR, NOT) these latches and flip-flops are built from.
- [Relay Logic Circuits](control-circuits.relay-logic.md) — the seal-in latch is the electromechanical ancestor of the SR latch; the same set/reset/hold states.
- [Multivibrator Circuits](analog-circuits.multivibrator-circuits.md) — the bistable multivibrator is the discrete-transistor predecessor of the flip-flop; the astable is a clock oscillator.
- [Oscillator Circuits](analog-circuits.oscillator-circuits.md) — crystal and RC oscillators that generate the clock signals these flip-flops run on.
- [Semiconductor Devices](semiconductor-devices.md) — BJT and MOSFET physics underlying every gate in every flip-flop.
- [Passive Components](passive-components.md) — resistors and capacitors for pull-ups, decoupling, and RC timing.
- [Digital Logic](../computing/digital-logic.md) — state-machine design methodology, state encoding, and sequential logic analysis at the system level.
- [Logic Design](../computing/logic-design.md) — HDL coding of sequential logic, FPGA register inference, and timing closure methodology.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
