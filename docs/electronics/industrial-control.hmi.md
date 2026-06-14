# HMI Design

> **Node ID**: electronics.industrial-control.hmi
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.industrial-control`](industrial-control.md), [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.industrial-control.plc`](industrial-control.plc.md)
> **Timeline**: Years 35-55
> **Outputs**: hmi-designs
> **Critical**: No — HMI is the operator-facing presentation layer built atop the controller and semiconductor substrate; it organizes human-machine interaction rather than gating a primary bootstrap dependency

The **H**uman-**M**achine **I**nterface is the operator's window into the process. Where the [PLC](industrial-control.plc.md) closes the control loop and [SCADA](industrial-control.scada.md) aggregates data across the site, the HMI is what the operator actually *looks at and touches*: the screen that shows the pump running, the valve position, the tank level, the alarm that just tripped — and the buttons, setpoint entry fields, and confirmation dialogs that let the operator command the process.

A well-designed HMI makes a complex plant legible at a glance and unambiguous under stress. A poorly-designed HMI causes operator error — the wrong button pressed during an upset, a critical alarm buried in a flood, a misread value that leads to the wrong action. HMI design is therefore not decoration; it is a safety engineering discipline governed by standards (ISA-101, EEMUA 201). This article teaches its principles.

## HMI Purpose

Every HMI does three things:

1. **Display process state** — show the operator what the plant is doing right now: which equipment is running, what the temperatures/pressures/flows are, where the valves are positioned. The process mimic diagram with animated, color-coded equipment is the primary display.
2. **Accept operator commands** — let the operator change the process: start/stop a pump, open/close a valve, raise/lower a setpoint, switch a loop to manual. Every command flows through the HMI to the PLC, which executes it.
3. **Present alarms and trends** — surface abnormal conditions (alarms) and show how variables have changed over time (trends), so the operator can detect developing problems and diagnose causes.

The HMI is the bridge between the deterministic, fast machine world of the PLC and the slow, judgment-driven world of the human operator. Its job is to translate each for the other: machine state into human-readable pictures, human intent into machine commands.

## Display Types — Historical Evolution

HMI hardware has evolved through three generations:

**Text panels (1970s-80s)**: Simple 2- or 4-line character LCD or VFD displays with a few function keys. The screen shows lines of text: `PUMP P-101: RUNNING`, `TANK T-204 LVL: 72.3%`. Navigation is by page-up/page-down through a fixed list of messages. Cheap, robust, still used for simple machines (a single-packaging line, a small compressor skid) where a full graphical display is unjustified. Limited: no mimics, no trends, no overview — the operator must know which page has which value.

**Monographic / vector graphics (1980s-90s)**: Early CRT displays rendering line drawings — pipe schematics with stick-figure pumps and valves, basic bar-graph trends. A step up from text: the operator sees a *picture* of the process. Monochrome (often green or amber phosphor) limited the visual vocabulary; state had to be encoded by shape or blinking rather than color.

**Full-color graphical (1990s-present)**: Color LCD/LED panels or PC-based monitors running graphical HMI software (Wonderware, FactoryTalk View, Ignition). Process mimics with realistic equipment symbols, full color coding, pop-up faceplates, embedded trends, alarm banners. This is the modern standard. Touchscreens have largely replaced dedicated hard buttons on panel-mounted HMIs; the display surface itself is the input device.

**Touchscreen evolution**: Early touch HMIs used resistive touch (work with gloves/stylus, low resolution). Modern industrial touchscreens use projected capacitive (multi-touch, like a phone) but must be gloved-operable — a common field complaint is that consumer-grade capacitive screens don't register a finger inside a thick work glove. Industrial-grade panels specify glove-compatible touch.

## Screen Design Principles

The core principle of HMI screen design is **hierarchy**: the operator should be able to drill from a plant-wide overview down to a single device, and back, without losing context. A three-tier hierarchy is standard:

```
   OVERVIEW screen
   ┌──────────────────────────────────────────────────────────┐
   │  Plant-wide status: every area as one block, colored by   │
   │  health (green=normal, yellow=warning, red=alarm).        │
   │  Click an area block → drill to that area.                │
   └──────────────────────────────────────────────────────────┘
                            │  (click area "Boiler House")
                            ▼
   AREA screen
   ┌──────────────────────────────────────────────────────────┐
   │  Process mimic of the boiler house: all equipment shown   │
   │  with live states and key values. Click a device → drill  │
   │  to that device's faceplate.                              │
   └──────────────────────────────────────────────────────────┘
                            │  (click pump P-101)
                            ▼
   DETAIL / FACEPLATE (pop-up)
   ┌──────────────────────────────────────────────────────────┐
   │  Everything about pump P-101: running/stopped, amps,      │
   │  hours, start/stop/auto buttons, setpoint entry, alarms.  │
   │  Close pop-up → return to area screen.                    │
   └──────────────────────────────────────────────────────────┘
```

**Consistent navigation**: A "home" button always returns to the overview. Breadcrumbs (Overview › Boiler House › P-101) show where you are. Back/forward navigation. The operator should never be "lost" — three clicks max from any device to any other.

### Color Coding Conventions

Color is the fastest channel for state communication — but only if used consistently. The ISA-101 and EEMUA 201 standards enforce a disciplined palette so that a red element means the same thing on every screen, in every plant:

| Color | Meaning | Examples |
|-------|---------|----------|
| **Red** | Alarm / stopped / off-state of running equipment | Pump tripped, valve closed (when it should be open), critical alarm active |
| **Green** | Running / normal / on-state | Pump running, valve open, process in auto, value in-range |
| **Yellow** | Warning / abnormal | Pre-alarm threshold, device in manual, maintenance overdue |
| **Blue / Cyan** | Information / out-of-service | Device tagged out, bypassed, under test, informational alarm |
| **White / Gray** | Static / neutral | Pipe lines, labels, inactive elements, values with no alarm |

**Critical rule**: color must be *redundant* — never encode information in color alone (colorblind operators, monochrome printouts). A red pump must also be labeled STOPPED or show a stopped symbol; a green pump must also say RUNNING. Shape, text, and color together.

**Blinking**: reserved for unacknowledged alarms. Once acknowledged, the element stops blinking and holds steady in its priority color. Blinking should never be used for "decoration" — it is a demand for attention and loses its force if overused.

### Example Screen Layout — Process Overview

A typical overview screen for a small process area (two feed pumps, a heat exchanger, a process tank):

```
┌─ BOILER FEEDWATER AREA ──────────────────────────── 14:32:07 ─┐
│ OVERVIEW › FEEDWATER                                          │
│                                                               │
│   ╔═══════╗         ┌─────────────┐         ╔═══════╗         │
│   │  P-101│████████▶│   E-201     │████████▶│ T-301 │         │
│   │ (RUN) │  line   │  Feed HX    │  line   │ LVL:  │         │
│   │grn    │────────▶│             │────────▶│ 72.3% │         │
│   ╚═══════╝   FT    └─────────────┘   TT    ║  grn  ║         │
│      ▲                                          │            │
│      │ 4-20mA                                    │ 4-20mA     │
│   ┌──┴───┐                                     ┌─┴──┐         │
│   │ P-102│  (STOP)                       ┌─────│LT  │         │
│   │ red  │  standby                      │     │301 │         │
│   ╚══════╝                               │     └────┘         │
│                                          ▼                    │
│                                   ╔══════════╗                │
│                                   │ V-302    │  OUT TO BOILER │
│                                   │ (AUTO)   │████████████▶   │
│                                   │  grn     │                │
│                                   ╚══════════╝                │
│                                                               │
├─ ALARM BANNER ────────────────────────────────────────────────┤
│ [!] 14:28:45  T-301 LEVEL HIGH          WARNING   (ack)       │
│                                                               │
├───────────────────────────────────────────────────────────────┤
│ [HOME] [AREA↑] [ALARM SUM] [TRENDS] [Faceplate▼]   OP: J.SMITH│
└───────────────────────────────────────────────────────────────┘

Legend: grn=green(normal/run)  red=red(stopped/alarm)
        ████ = pipe with flow   ──── = pipe no flow
        FT = flow transmitter   TT = temp transmitter   LT = level tx
```

The operator sees at a glance: P-101 is running (green), P-102 is standby (red), flow is going through E-201 into T-301 at 72.3% level, and there's one active warning alarm on T-301 high level (yellow, acknowledged). Clicking P-101 opens its faceplate; clicking T-301 opens the tank detail.

## Operator Interaction Patterns

The HMI accepts several distinct input styles, each matched to the kind of command being issued:

**Pushbuttons (momentary)**: A START or STOP button that is active only while pressed (on a touchscreen, while touched). The HMI sends a momentary command to the PLC, which seals it in with its own logic (the START energizes a seal-in coil in the PLC ladder — see [control-circuits.ladder-logic](control-circuits.ladder-logic.md)). Used for discrete on/off commands. Standard appearance: a labeled rectangle, sometimes a raised-button graphic.

**Selectors (maintained)**: A multi-position switch graphic — AUTO / MANUAL / OFF, or LOCAL / REMOTE. Tapping a position holds that selection until changed. The HMI writes the corresponding value to a PLC register. Used for mode selection.

**Setpoint entry (numeric keypad)**: The operator taps a setpoint value on the screen (e.g., the "72.3%" on the tank, or a temperature setpoint), a numeric keypad pop-up appears, the operator enters the new value, and presses ENTER. The HMI validates the entry against limits (min/max) before writing it to the PLC, rejecting out-of-range values. Used for analog command values.

**Faceplates**: A pop-up panel showing everything about one device — current state, measured value, setpoint, output, mode, alarms, and all command buttons (start/stop/auto/manual/setpoint). The faceplate is the device's "home screen," summoned by clicking the device symbol on any mimic. It keeps the mimic uncluttered while making full detail one click away.

### Permissives and Interlocks at the HMI Level

The HMI enforces a layer of **soft interlocks** — logic that prevents an invalid operator command from even reaching the PLC. Examples:

- The START button for a pump is grayed out (disabled) if the suction valve is closed or the discharge valve is closed — the permissives in the PLC logic are mirrored in the HMI so the operator cannot *attempt* a start that the PLC would reject anyway.
- A setpoint entry is rejected if it's outside the configured min/max band for that loop (e.g., a temperature setpoint above the vessel's relief-valve set pressure).
- A mode switch to MANUAL requires the loop to be stable first (no active high-high alarm) — the HMI blocks the switch with a reason message.

**Important**: HMI soft interlocks are a *convenience and a guard against operator error*, NOT a safety system. The **hard interlocks** in the PLC (and the wired relay interlocks behind them) are what actually protect equipment and personnel. If the HMI and PLC disagree, the PLC wins — the HMI command is just a write to a register that the PLC logic can refuse to act on. Safety-critical interlocks (emergency stop, overpressure trip) must be implemented in the PLC or in dedicated safety hardware, never in the HMI alone.

## Alarm Management in the HMI

The HMI is where the operator *experiences* alarms. Three display regions handle them:

**Alarm banner**: A strip — usually across the bottom or top of every screen — showing the most recent active unacknowledged alarm. It is always visible, regardless of which screen the operator is on. Its purpose is to interrupt: a new critical alarm flashes here and demands the ack. The banner typically shows one line (highest-priority, most-recent) with a button to jump to the full alarm summary.

**Alarm summary page**: A full screen listing **all currently active alarms** — tag, description, priority, time-of-occurrence, state (active/acked). Sortable by time or priority. The operator's working list during an upset. Each row has an Acknowledge button. This is where the operator triages multiple simultaneous alarms.

**Alarm history (log)**: A chronological log of **all alarm events** — including alarms that have since returned to normal and been acknowledged. Used for post-incident analysis: "what was the sequence of events that led to the trip?" The history is fed by the SCADA historian (see [industrial-control.scada](industrial-control.scada.md) §Historical Trending) and can be filtered by tag, time range, and priority.

### Ack / Reset Interaction Model

The standard alarm lifecycle, mirrored from the SCADA alarm-management section but focused on the operator's actions:

1. **Occurrence**: condition crosses threshold → alarm appears in banner (blinking, priority color) and summary page (active, unacked). An audible horn sounds for critical/warning.
2. **Acknowledge**: operator clicks ACK → blinking stops, horn silences. The alarm is now "active, acked" — still in the summary, steady color. Acknowledgment tells the system "I have seen this and am aware."
3. **Return to normal**: condition returns below threshold → alarm state changes to "returned, unacked" (some systems re-flag for acknowledgment; others auto-clear once acked).
4. **Reset / clear**: after the operator acknowledges the return-to-normal, the alarm leaves the active summary and moves to history only.

**Ack vs Reset distinction**: Acknowledgment silences the annunciation; Reset clears the alarm from the active list. Some systems combine these (one ACK button does both); ISA-18.2 favors keeping them separate so an operator cannot clear an alarm without explicitly confirming the condition has resolved.

## Trend Displays

Trends show how a variable has changed over time — essential for detecting gradual drift and diagnosing the cause of a trip. Two flavors:

**Real-time trends (scrolling strip-chart)**: A fixed-width chart showing the last N minutes of a tag, updating continuously. As new samples arrive, the trace scrolls left and old data falls off the edge. Mimics the paper strip-chart recorder of the pre-digital era. Typically 1-4 tags overlaid. Time window: 5-60 minutes. Used for monitoring active process dynamics ("is the level still rising?").

**Historical trends (query by time range)**: The operator specifies a tag and a time range (e.g., "yesterday 02:00 to 06:00") and the historian returns the data for display. Pan and zoom across hours, days, or months. Used for post-incident analysis ("when did the vibration start increasing?") and long-term performance tracking. The data comes from the SCADA historian.

**Embedded statistics**: Trend displays show the value scale (engineering units) on the Y-axis and time on the X-axis. Many HMIs overlay **min/max/avg** bands for the selected period — shaded regions showing the historical range — so the operator can see whether the current value is typical or an outlier without querying a separate report.

```
   T-301 LEVEL  ──  last 60 min ──
 80% ┤              ╭──╮              ╭────────────╮
     │             ╱    ╰─────── HIGH ──────────── warning
 75% ┤───────────╱───────────────────────────────╯
     │        ╭─╯                                  ← current 72.3%
 72% ┤───────╯       avg band ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
     │
 65% ┤
     └┬─────────┬─────────┬─────────┬─────────┬──
     13:35     13:45     13:55     14:05     14:15
```

## Safety Interlocks in the UI

For critical actions — those that can directly cause equipment damage, injury, or a process upset — the HMI adds a layer of operator confirmation above the PLC's hard interlocks:

**Confirmation dialogs**: START, STOP, RESET, and mode-change commands for critical equipment pop a confirmation dialog: "Confirm START of P-101 FEEDWATER PUMP? [OK] [CANCEL]." This prevents an accidental tap from commanding a pump start. The dialog names the specific device and action — generic "Are you sure?" dialogs are ineffective because operators click through them reflexively.

**Two-key operations**: For the most critical actions (e.g., resetting a safety interlock, overriding an emergency shutdown), the HMI requires two simultaneous inputs — two buttons held, or a key-switch plus a screen confirmation — so that a single accidental touch cannot execute the command.

**Audit trail**: Every operator command is logged with timestamp, operator ID, tag, and action. The audit trail is written to the historian and is tamper-evident. This supports incident investigation ("who opened the valve at 03:14?") and regulatory compliance (in regulated industries — nuclear, pharmaceutical, pipeline — the audit trail is a legal record).

**Key principle**: The HMI's safety features exist to prevent *operator error*, not to substitute for equipment safety. The hard interlocks (wired e-stops, relief valves, overspeed trip bolts — see [energy.steam-turbines](../energy/steam-turbines.md)) protect regardless of what the HMI does or what the operator clicks. The HMI layer is defense against human mistake; the PLC/hardware layer is defense against everything.

## Display Parameter Table

| Display Type | Resolution | Input Method | Typical Application | Cost Class |
|--------------|-----------|--------------|---------------------|------------|
| Text panel (2-4 line) | 16×4 to 40×4 chars | Function keys | Single-machine status, small skid, local indicator | Low ($200-800) |
| Monochrome graphical | 320×240 to 640×480 | Touch / keys | Legacy systems, simple sequence display | Low-Med ($500-2k) |
| Color touchscreen panel | 800×480 to 1280×800 | Resistive touch | Machine-mounted HMI, small process cell | Medium ($1-5k) |
| Full-graphical panel PC | 1280×1024 to 1920×1080 | Capacitive touch + mouse/kbd | Process area HMI, multi-loop station | Medium-High ($3-10k) |
| Control-room console (multi-monitor) | 1920×1080 ×2-4 per operator | Mouse + keyboard | Plant-wide SCADA operator station | High ($5-20k/seat) |

The progression mirrors the HMI's evolution: from a single-line text readout on a small machine, to a touch panel at a process cell, to a multi-monitor operator console in a central control room running the full SCADA system. A bootstrap civilization starts at the text-panel end (any character LCD + a few buttons + a serial link to the PLC) and works toward the graphical end as display technology and computing power permit — each step adds legibility and reduces operator error.

## Relationship to Sibling Articles

This article owns the **operator-facing presentation and interaction layer**: screen hierarchy, color coding, alarm display, trend rendering, and operator-command patterns. It does not re-teach:

- **SCADA supervisory architecture, telemetry protocols, historian** — the MTU that *runs* the HMI software at the plant-wide level. See [industrial-control.scada](industrial-control.scada.md).
- **PLC hardware and control logic** — the controller whose state the HMI displays and whose registers the HMI writes. See [industrial-control.plc](industrial-control.plc.md).
- **Embedded-system substrate** (display controllers, touch digitizers, graphics processing) that the HMI hardware is built from. See [computing.embedded-systems](../computing/embedded-systems.md).
- **Alarm *rationalization* and priority assignment** at the system-engineering level — that discipline lives in the [SCADA](industrial-control.scada.md) alarm-management section; this article covers how the resulting alarms are *displayed* to the operator.

The [semiconductor-devices](semiconductor-devices.md) capability provides the silicon — display drivers, touch controllers, and the processors that render the graphics — on which every modern HMI is built.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
