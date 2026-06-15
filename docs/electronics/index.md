# Electronics

Capabilities in this domain:

- [Electrical Systems](electrical-systems.md) — Power distribution wiring, switches, connectors, fuses, breakers, transformers, motor-generator sets, and power electronics.

- [Passive Components](passive-components.md) — Resistors, capacitors, and inductors as fundamental circuit building blocks for filtering, timing, impedance matching, and energy storage.
- [Semiconductor Devices](semiconductor-devices.md) — Discrete semiconductor components: diodes, BJTs, FETs, and thyristors for amplification, switching, rectification, and logic.

- [PCB Fabrication](pcb-fabrication.md) — Copper-clad substrate processing into patterned circuit interconnects providing mechanical support, electrical connections, and thermal management.
- [Power Electronics](power-electronics.md) — Semiconductor-based power conversion and control: rectifiers, inverters, DC-DC converters, and motor drives for efficient energy conversion and grid integration.

- [Electronics Assembly](assembly.md) — PCB fabrication, component placement, soldering (through-hole and surface mount), conformal coating, IC packaging, and testing.

- [IC Packaging & Interconnect](packaging.md) — Die attach, wire bonding, leadframes, BGA substrates, and encapsulation connecting bare silicon die to board-level interconnect.

- [Wire Insulation and Enameling](wire-insulation.md) — Magnet wire enameling (polyurethane, polyester, polyesterimide), rubber cable extrusion, cloth/paper wrapping, and varnish dipping for dielectric isolation in wound components.

- [Circuit Fundamentals](circuit-fundamentals.md) — Ohm's and Kirchhoff's laws, node/mesh analysis, network theorems, and impedance: the analytical foundation underlying all circuit design.
- [Power Supply Circuits](power-supply-circuits.md) — Linear and switching regulators (LDO, buck, boost, flyback) converting raw DC into stable, regulated rails for electronic loads.
- [Power Conversion Circuits](power-conversion-circuits.md) — Inverters, DC-DC converters, and motor drives converting between DC and AC at high efficiency using semiconductor switches.
- [Analog Circuits](analog-circuits.md) — Amplifiers, filters, oscillators, and signal-conditioning chains built from op-amps and discrete transistors for continuous-signal processing.
- [Interface Circuits](interface-circuits.md) — ADCs, DACs, level shifters, and mixed-signal bridges translating between analog sensors and digital logic domains.
- [Optoelectronic Circuits](optoelectronic-circuits.md) — LEDs, photodiodes, optocouplers, and light-based sensing, signaling, and galvanic-isolation circuits.
- [Communications Circuits](communications-circuits.md) — RF front-ends, modulators/demodulators, line drivers, and wireless/wired information-transfer circuitry.
- [Control Circuits](control-circuits.md) — Relay logic, ladder diagrams, discrete-state control, and feedback/comparator circuits for sequencing and automation.
- [Industrial Control](industrial-control.md) — PLC, SCADA, and HMI platforms integrating computing, sensing, and actuation for automated industrial processes.

- [Soldering Iron](soldering-iron.md) — Temperature-controlled soldering irons for electronics assembly, repair, and wire joining.

- [Electronic Test Equipment](test-equipment.md) — Multimeters, oscilloscopes, signal generators, and power supplies for circuit testing and characterization.

- [Semiconductor Packaging & Testing](packaging-testing.md) — Wafer backgrinding, die singulation, die attach, wire bonding, encapsulation, wafer probing, burn-in testing, reliability qualification (JEDEC, AEC-Q100, MIL-STD-883).

- [Amplifier Fundamentals](analog-circuits.amplifier-fundamentals.md) — This article is the discrete-transistor foundation of all analog electronics: how a single BJT or MOSFET, biased into its linear (active) region, turns a tiny input signal into a larger copy at the output.
- [Diode Circuits](analog-circuits.diode-circuits.md) — This is the first active circuit a practitioner builds. A diode on its own is a two-terminal lump of doped silicon (see Semiconductor Devices for how it is made); wired into a network with resistors, capacitors, and…
- [Multivibrator Circuits](analog-circuits.multivibrator-circuits.md) — A multivibrator is a two-state regenerative circuit: it uses positive feedback to snap cleanly between two voltage levels. The three flavors are named by how many of those levels are stable:
- [Op-Amp Circuits](analog-circuits.op-amp-circuits.md) — The operational amplifier is the most versatile analog integrated circuit ever built. A single 8-pin package, two supply rails, and a handful of resistors and capacitors replace rooms full of carefully biased…
- [Oscillator Circuits](analog-circuits.oscillator-circuits.md) — An oscillator is a circuit that produces a periodic output waveform with no input signal. It is the electronic embodiment of a self-sustaining feedback loop: a fraction of the amplifier's output is fed back to its input…
- [Power Amplifiers](analog-circuits.power-amplifiers.md) — This article is about amplifiers that deliver watts to a load — a loudspeaker, a transmission-line antenna, a servo motor, a piezo actuator — rather than the millivolts of signal voltage handled by Amplifier…
- [Timer Circuits](analog-circuits.timer-circuits.md) — The 555 timer is, by volume, the most ubiquitous integrated circuit ever manufactured. Introduced by Signetics in 1972 (designed by Hans Camenzind), it has sold in the tens of billions and is still in production from a…
- [Transistor Switch Circuits](analog-circuits.transistor-switch-circuits.md) — This is the second of the two "Basic Semiconductor Circuits" entry points (alongside Diode Circuits). It teaches the transistor used the way digital logic and power control use it: as a two-state switch — fully ON…
- [AC Circuit Analysis](circuit-fundamentals.ac-analysis.md) — This article teaches alternating-current (AC) circuit analysis from first principles. We assume you know DC theory — Ohm's law (V = IR), series/parallel resistor combinations, Kirchhoff's voltage and current laws, and P…
- [DC Circuit Analysis](circuit-fundamentals.dc-analysis.md) — This article teaches DC circuit analysis from first principles. It assumes you have copper wire, a battery, and some resistors (passive components) wired together with electrical systems infrastructure — but it assumes…
- [Modulation and Demodulation Circuits](communications-circuits.modulation-circuits.md) — This is the TESLA/RF thread — how information rides on a carrier. You already understand the sinusoid: v(t) = A·sin(ωt + φ), where amplitude A, angular frequency ω = 2πf, and phase φ are the three knobs you can turn.
- [Receiver Circuits](communications-circuits.receiver-circuits.md) — A receiver does the opposite of a transmitter: it captures a tiny modulated RF signal from an antenna, amplifies it, selects the desired station from dozens sharing the band, strips the modulation off the carrier, and…
- [RF Oscillator Circuits](communications-circuits.rf-oscillator-circuits.md) — This article is the RF thread of oscillator design. The general theory of oscillation — the Barkhausen criterion (loop gain ≥ 1, total phase shift = 360°), feedback amplifier topology, amplitude stabilization, and the…
- [Discrete Logic Circuits](control-circuits.discrete-logic-circuits.md) — This article is about how logic gates are built and used as electronic components — how a transistor becomes an inverter, how two transistors become a NAND gate, and how the 74xx TTL and 4000 CMOS integrated-circuit…
- [Ladder Logic Design](control-circuits.ladder-logic.md) — Ladder logic is the diagram notation and design methodology for industrial control. It takes the relay circuits you learned in Relay Logic Circuits — seal-in latches, motor starters, interlocks, timer sequences — and…
- [Relay Logic Circuits](control-circuits.relay-logic.md) — Relay logic is the Edison-era art of wiring electromechanical relays and contactors into control circuits that start and stop motors, interlock guards, time sequences, and implement Boolean decisions in hardware.
- [Sequential Logic Circuits](control-circuits.sequential-logic-circuits.md) — A sequential circuit differs from a combinational one in a single decisive way: its output depends not just on the current inputs but on the history of past inputs, because the circuit stores state.
- [HMI Design](industrial-control.hmi.md) — The Human-Machine Interface is the operator's window into the process. Where the PLC closes the control loop and SCADA aggregates data across the site, the HMI is what the operator actually looks at and touches: the…
- [Industrial Control Architecture](industrial-control.industrial-control-architecture.md) — This article is the integration tier. It does not teach the PLC, the SCADA system, the HMI, the relay panel, the ladder notation, the variable-frequency drive, the field sensor, or the analog-to-digital converter — each…
- [PLC Design](industrial-control.plc.md) — A Programmable Logic Controller (PLC) is a rack-mounted industrial computer designed for one job: execute boolean and sequential control logic over a large number of digital and analog I/O points, deterministically, in…
- [SCADA System Design](industrial-control.scada.md) — SCADA — Supervisory Control And Data Acquisition — is the system architecture that gives a human operator centralized visibility and command over geographically distributed process plants.
- [ADC Circuits](interface-circuits.adc-circuits.md) — This article is one half of the analog/digital bridge covered in Interface Circuits: where the companion DAC Circuits article teaches how to reconstruct an analog voltage from a digital word, this article teaches the…
- [DAC Circuits](interface-circuits.dac-circuits.md) — This article is the inverse of the companion ADC Circuits article: where that one captures an analog voltage as a digital word, this one reconstructs an analog voltage from a digital word.
- [Sensor Circuits](interface-circuits.sensor-circuits.md) — A sensor converts a physical quantity — magnetic field, temperature, mechanical strain, light, liquid level — into an electrical parameter (a voltage, a resistance, a current, or a contact closure).
- [LED Driver Circuits](optoelectronic-circuits.led-driver-circuits.md) — This is the Forrest Mims III Optoelectronics Projects entry point for light emission. An LED is a pn junction that emits photons when forward-biased — the semiconductor physics and device manufacturing are covered under…
- [Optocoupler Circuits](optoelectronic-circuits.optocoupler-circuits.md) — An optocoupler (also called an optoisolator or photocoupler) is a single package containing an LED on the input side optically coupled to a light-sensitive device on the output side, with no electrical connection…
- [Photodetector Circuits](optoelectronic-circuits.photodetector-circuits.md) — This is the inverse of the LED driver article: where that article teaches how to convert electricity into light, this article teaches how to convert light into electricity.
- [Inverter Circuits](power-conversion-circuits.inverter-circuits.md) — An inverter converts DC power into AC power. This is the mirror image of rectifier circuits (AC→DC): where a rectifier uses passive diodes that steer whichever way the AC happens to flow, an inverter must actively…
- [VFD Motor Control](power-conversion-circuits.vfd-motor-control.md) — A variable-frequency drive (VFD) is a power-electronic circuit that adjusts the speed and torque of an AC induction motor by synthesizing a three-phase AC waveform whose frequency and voltage are both controllable from…
- [Filter Circuits](power-supply-circuits.filter-circuits.md) — Filtering is the second stage of every power supply — the process of reducing the AC ripple from a rectifier to a tolerable level, producing near-DC voltage.
- [Linear Regulators](power-supply-circuits.linear-regulators.md) — Linear regulation is the third and final stage of a classic DC power supply — it takes the filtered but still-rough DC from the filter capacitor and delivers a stable, precise output voltage that does not move with line…
- [Rectifier Circuits](power-supply-circuits.rectifier-circuits.md) — Rectification is the first stage of every power supply — the process of converting bidirectional AC current into unidirectional (pulsating) DC.
- [Switching Regulators](power-supply-circuits.switching-regulators.md) — Switching regulation converts one DC voltage to another by chopping the input at high frequency and transferring energy through an inductor or transformer.

[↑ Back to Tech Tree](../index.md)

