# Embedded Systems

> **Node ID**: computing.embedded-systems
> **Domain**: [Computing](./index.md)
> **Dependencies**: [`computing.computer-architecture`](computer-architecture.md), [`computing.data-storage`](data-storage.md), [`electronics.pcb-fabrication`](../electronics/pcb-fabrication.md)
> **Enables**: Industrial process control, semiconductor fab equipment control, automation systems
> **Timeline**: Years 55-75+
> **Outputs**: microcontroller_systems, firmware, real_time_control, sensor_interfaces
> **Critical**: Yes — embedded systems bridge computing hardware and physical process control; without them, semiconductor fab tools cannot be automated

## 1. Overview

An embedded system is a computer designed for a dedicated control function within a larger physical system, with real-time constraints, limited resources, and direct hardware interfaces to sensors and actuators. Unlike general-purpose computers that run varied software, an embedded system runs a single firmware program that must respond to physical events within guaranteed time limits.

Embedded systems are the computing hardware that controls industrial processes: motor drives, temperature controllers, valve actuators, sensor arrays, and communication links. In the semiconductor fab context, embedded controllers manage wafer handling robots, process chamber temperature profiles, gas flow mass controllers, and vacuum pump sequencing. Every piece of automated equipment contains one or more embedded processors.

This capability applies the architecture concepts from [`computing.computer-architecture`](computer-architecture.md) to the specific problems of real-time control: deterministic response times, sensor interfacing (ADC/DAC), interrupt-driven I/O, power constraints, and reliable operation without human intervention. The logic design methodology from [`computing.logic-design`](logic-design.md) provides the FPGA-based implementation path for custom control hardware.

**Boundary with software-bootstrapping**: This document covers the hardware — microcontroller selection, circuit design for sensor interfaces, ADC/DAC specifications, watchdog timers, and power management. Firmware architecture (task scheduling, interrupt handlers, device drivers) is described here because it is inseparable from the hardware design. Writing compilers or operating systems for embedded targets is software construction — see the software-bootstrapping domain.

## 2. Prerequisites

### Materials

- Microcontroller IC or FPGA from [`computing.computer-architecture`](computer-architecture.md)
- Passive components from [`electronics.passive-components`](../electronics/passive-components.md)
- PCB assemblies from [`electronics.pcb-fabrication`](../electronics/pcb-fabrication.md)
- Sensors (thermocouples, pressure transducers, optical encoders) — application-specific
- Actuators (solenoids, motors, heaters, valves) — application-specific
- Connectors and wiring harnesses from [`electronics.electrical-systems`](../electronics/electrical-systems.md)

### Tools and Equipment

- Oscilloscope (100+ MHz, 4 channels for mixed-signal debugging)
- Logic analyzer (for digital protocol decoding: SPI, I²C, UART)
- Multimeter with current measurement
- In-circuit programmer/debugger (JTAG or SWD interface)
- Power supply with current limiting (0-30V, 0-3A)

### Knowledge

- Computer architecture fundamentals (see [`computing.computer-architecture`](computer-architecture.md))
- Analog circuit basics (Op-amp circuits, RC filters, voltage dividers)
- Binary and hexadecimal number systems
- Interrupt-driven programming concepts

## 3. Bill of Materials

| Component | Quantity (per controller board) | Source | Alternatives |
|-----------|----------------------------------|--------|-------------|
| Microcontroller (8-bit AVR/PIC, 16 MHz) | 1 | Semiconductor fab + packaging | FPGA with soft processor core |
| Microcontroller (32-bit ARM Cortex-M, 48-100 MHz) | 1 | Semiconductor fab + packaging | Multiple 8-bit MCUs with communication |
| Crystal oscillator (8-16 MHz) | 1 | Quartz crystal + amplifier | Internal RC oscillator (±1-3% tolerance) |
| Voltage regulator (3.3V, 500 mA LDO) | 1 | [`electronics.power-electronics`](../electronics/power-electronics.md) | Switching regulator (higher efficiency, more noise) |
| ADC (10-12 bit, 100 kS/s) — often integrated in MCU | 0-1 | Integrated in MCU or external IC | Comparator + resistor ladder (lower resolution) |
| DAC (8-12 bit) — often integrated in MCU | 0-1 | Integrated in MCU or external IC | PWM + RC filter (lower bandwidth, 8-bit effective) |
| RS-485 transceiver (for industrial communication) | 1-2 | [`electronics.semiconductor-devices`](../electronics/semiconductor-devices.md) | RS-232 (shorter range, point-to-point) |
| Decoupling capacitors (100 nF ceramic) | 10-20 | [`electronics.passive-components`](../electronics/passive-components.md) | 1 μF tantalum (larger, higher ESR) |
| Pull-up/pull-down resistors (4.7-10 kΩ) | 10-20 | [`electronics.passive-components`](../electronics/passive-components.md) | Internal MCU pull-ups (higher tolerance, 20-50 kΩ) |
| PCB (2-layer minimum, 4-layer preferred) | 1 | [`electronics.pcb-fabrication`](../electronics/pcb-fabrication.md) | Perfboard (prototyping only) |
| Watchdog timer IC (if not integrated in MCU) | 0-1 | Semiconductor fab + packaging | Software watchdog (less reliable) |

## 4. Process Description

### 4.1 Microcontroller Selection

1. **Determine processing requirements.** Estimate the computational load:
   - Simple control loop (read sensor, compare, set output): 8-bit MCU at 1-16 MHz.
   - Multi-channel control with communication: 32-bit MCU at 48-100 MHz.
   - Signal processing (FFT, digital filtering): 32-bit MCU with FPU or DSP extensions.

2. **Count I/O requirements.** List every digital input, digital output, analog input, analog output, and communication interface needed. Add 20% margin. Match against MCU peripheral set.

3. **Determine memory requirements.** Program size (flash): 4-32 KB for simple control, 64-256 KB for multi-task systems with communication stacks. RAM: 256 bytes-4 KB for simple tasks, 8-64 KB for complex systems. Choose an MCU with 2× headroom.

4. **Evaluate real-time constraints.** Determine the fastest event that requires a response. Interrupt latency must be less than 10% of the minimum event interval. For a 1 kHz control loop (1 ms period), interrupt latency must be <100 μs.

### 4.2 Sensor Interface Design (ADC)

1. **Choose the ADC resolution.** Resolution determines the smallest detectable change:
   - 8-bit ADC: 256 levels, 0.39% resolution. Adequate for coarse measurements (battery voltage, temperature ±2°C).
   - 10-bit ADC: 1,024 levels, 0.098% resolution. Standard for MCU-integrated ADCs.
   - 12-bit ADC: 4,096 levels, 0.024% resolution. Required for precision measurements (pressure ±0.1%, strain gauge).
   - 16-bit ADC: 65,536 levels, 0.0015% resolution. Instrumentation grade (thermocouple, load cell).

2. **Condition the sensor signal.** Scale the sensor output to match the ADC input range (0-VREF). Use an operational amplifier circuit: non-inverting amplifier for voltage scaling, instrumentation amplifier for differential signals (bridge sensors). Add an anti-aliasing RC low-pass filter with cutoff frequency ≤ fsample/2 (Nyquist criterion).

3. **Configure the ADC.** Set the sampling rate (must be ≥2× the highest frequency component in the signal). For a 100 Hz temperature sensor: sample at 200+ Hz. For a 10 kHz vibration sensor: sample at 20+ kHz. Configure reference voltage (internal bandgap 1.1V, external VREF, or VDD). Choose between single-ended and differential input modes.

4. **Read and convert.** Trigger conversion (software trigger, timer-triggered, or continuous). Wait for conversion complete (polling or interrupt). Read the result register. Convert to engineering units: `value = (ADC_result / 2^N) × VREF × scale_factor + offset`.

### 4.3 Actuator Interface Design (DAC and PWM)

1. **Choose the output method.** DAC for precision analog output (motor speed control, valve position). PWM for efficient power control (heater duty cycle, LED brightness, motor speed). Digital output for binary control (relay on/off, solenoid energize/de-energize).

2. **Design the DAC interface.** For an integrated DAC: write the output code to the DAC data register. Resolution determines output precision: 8-bit DAC with 3.3V reference → 12.9 mV steps. For external DAC: send output code via SPI or I²C. Add a buffer amplifier if the DAC cannot drive the load directly.

3. **Design the PWM interface.** Configure timer/counter for PWM mode: set period register (frequency), duty cycle register (on-time fraction). PWM frequency: 1-20 kHz for motor control (above audible range preferred), 100-500 Hz for heating, 100-1000 Hz for LED dimming. Add an RC low-pass filter to convert PWM to analog voltage if needed (cutoff frequency ≪ PWM frequency).

### 4.4 Interrupt Handling

1. **Identify interrupt sources.** List every event requiring immediate attention: timer overflow (periodic sampling), ADC conversion complete, UART receive (communication), external pin change (limit switch, emergency stop), watchdog timeout.

2. **Assign priorities.** Non-maskable interrupt (NMI) for critical faults (watchdog, brownout). High priority: emergency stop, communication errors. Medium priority: timer tick, ADC complete. Low priority: UART receive, status updates. The MCU executes the highest-priority pending interrupt first.

3. **Write ISR (interrupt service routine) design rules**:
   - Keep ISRs short: save status, read/write data, set flag, return. Do no processing in the ISR — defer to the main loop.
   - Never block in an ISR (no waiting for UART, no delays).
   - Use volatile declarations for all variables shared between ISR and main loop.
   - Disable interrupts only for the minimum time needed to update shared data structures.

### 4.5 Watchdog Timer Configuration

1. **Select timeout period.** Must be longer than the longest expected task execution time. For a 10 ms control loop with 3 tasks: set watchdog to 50-100 ms (5-10× the loop period). Too short → spurious resets. Too long → slow fault detection.

2. **Enable the watchdog.** Configure hardware watchdog (preferred) or external watchdog IC. Many MCUs offer a windowed watchdog: the refresh must occur within a time window (not too early, not too late), catching both hung and runaway code.

3. **Service the watchdog.** Kick (refresh) the watchdog at the end of each main loop iteration, after verifying that all tasks completed correctly. If any task hangs, the kick doesn't happen, and the watchdog resets the MCU after the timeout period.

## 5. Quantitative Parameters

### Common Microcontroller Specifications

| Parameter | 8-bit (ATmega328P) | 16-bit (MSP430) | 32-bit (STM32F103) | 32-bit (STM32F4) |
|-----------|---------------------|------------------|---------------------|-------------------|
| Architecture | AVR | MSP430 | ARM Cortex-M3 | ARM Cortex-M4F |
| Clock speed | 16 MHz | 16 MHz | 72 MHz | 168 MHz |
| Flash | 32 KB | 16-60 KB | 64-128 KB | 512 KB-1 MB |
| SRAM | 2 KB | 1-4 KB | 8-20 KB | 192 KB |
| ADC resolution | 10-bit | 10/12-bit | 12-bit | 12-bit |
| ADC speed | 15 kS/s | 200 kS/s | 1 MS/s | 2.4 MS/s |
| DAC | None | 12-bit (some) | None | 12-bit |
| PWM channels | 6 | 4-7 | 12 | 14 |
| UART/SPI/I²C | 1/1/1 | 1/1/1 | 3/2/2 | 6/3/3 |
| GPIO pins | 23 | 16-48 | 37-80 | 80-140 |
| Power (active) | 15 mA @ 5V | 3 mA @ 3.3V | 36 mA @ 3.3V | 90 mA @ 3.3V |
| Power (sleep) | 1 μA | 1 μA | 2 μA | 10 μA |
| Package | 28-DIP/32-TQFP | 20/40-DIP | 48-144 LQFP | 100-176 LQFP |

### ADC Performance by Resolution

| Resolution | Steps | LSB at 3.3V ref | Application |
|------------|-------|------------------|-------------|
| 8-bit | 256 | 12.9 mV | Coarse measurements |
| 10-bit | 1,024 | 3.2 mV | General purpose |
| 12-bit | 4,096 | 0.8 mV | Precision control |
| 16-bit | 65,536 | 50 μV | Instrumentation |

### Real-Time Deadline Examples

| Application | Sampling rate | Worst-case latency | Interrupt priority |
|-------------|---------------|-------------------|-------------------|
| Temperature control | 1-10 Hz | 100 ms | Low |
| Motor speed control | 1-10 kHz | 100 μs | High |
| Emergency stop | Event-driven | <1 ms | Highest (NMI) |
| Communication (UART) | 9,600-115,200 baud | 1 ms | Medium |
| Power fault detection | Event-driven | <10 μs | Highest (NMI) |

### Power Consumption Comparison

| Mode | ATmega328P (5V) | STM32F103 (3.3V) | STM32F4 (3.3V) |
|------|-----------------|-------------------|----------------|
| Active (full speed) | 15 mA (75 mW) | 36 mA (120 mW) | 90 mA (300 mW) |
| Idle (CPU halted, peripherals on) | 6 mA | 10 mA | 30 mA |
| Sleep (CPU off, RAM held) | 1 μA | 2 μA | 10 μA |
| Deep sleep (oscillator off) | 0.1 μA | 0.3 μA | 2 μA |

## 6. Scaling Notes

**From 8-bit to 32-bit microcontroller**: An 8-bit MCU handles simple control loops (thermostat, motor on/off, sensor reading). When the application requires floating-point math, complex communication stacks (TCP/IP, CAN bus), or multiple concurrent tasks, a 32-bit ARM Cortex-M provides 10-50× computational throughput at similar power consumption. Migration requires rewriting I/O register access (different peripheral maps) but the control logic transfers directly.

**From MCU to FPGA + soft processor**: When the application requires custom hardware acceleration (high-speed pulse generation, parallel sensor processing, deterministic timing that exceeds MCU interrupt latency), an FPGA with an embedded soft processor (MicroBlaze, RISC-V soft core) combines the programmability of a processor with the determinism of hardware logic. The soft processor handles control flow and communication; custom FPGA logic handles time-critical I/O.

**From single MCU to distributed system**: For complex systems (semiconductor fab tool, multi-axis machine), deploy multiple MCUs communicating over CAN bus, RS-485, or Ethernet. Each MCU controls one subsystem (temperature, gas flow, wafer transport, vacuum). A supervisory processor coordinates the subsystems. This scales to any complexity but introduces communication latency (0.1-10 ms per message depending on bus).

**Minimum useful system**: An 8-bit MCU (ATtiny85, 6 pins, 8 KB flash, 512 bytes RAM) running a single control loop at 1 MHz can read one sensor via ADC and drive one PWM output. This is the entry point: 6 components (MCU, crystal, 2 decoupling caps, voltage regulator, sensor). Sufficient for basic temperature control, LED dimming, or simple sequencing.

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| ADC readings are noisy | Missing anti-aliasing filter or decoupling cap on VREF | Add 100 nF cap on VREF pin; add RC low-pass filter on analog input (cutoff ≤ fs/2); average multiple samples (4-16 samples reduces noise by √N) |
| System resets randomly | Power supply brownout or watchdog timeout | Monitor VDD with oscilloscope during motor/relay switching; add bulk capacitor (100-1000 μF) near MCU; check watchdog kick timing |
| UART communication corrupted | Baud rate mismatch between transmitter and receiver | Verify both sides use identical baud rate, parity, and stop bits; measure actual baud rate with oscilloscope; use auto-baud detection if available |
| PWM output has jitter | Timer clock source instability or interrupt latency affecting register update | Use hardware PWM (timer peripheral) not software bit-banging; set PWM duty cycle register in timer ISR, not main loop |
| Interrupt latency too high | Other interrupts blocking or ISR too long | Reduce ISR execution time; use interrupt priorities (preempt lower-priority ISRs); move processing to main loop; use DMA for data transfers |
| Sleep mode current higher than expected | Unused peripheral still clocked or floating input drawing current | Disable all unused peripherals in power management registers; configure unused GPIO as output low or input with pull-up/down (never floating CMOS input) |

## 8. Safety

- **Watchdog timer is mandatory**: Every embedded system in a safety-critical application (motor control, heating, chemical process) must include a hardware watchdog. If the firmware hangs, the watchdog resets the MCU within a guaranteed time. Without it, a hung processor leaves actuators in their last state — a heater stays on, a motor keeps running, a valve stays open. Set the watchdog timeout to 2-5× the longest expected task cycle.
- **Brownout detection**: MCU brownout detection resets the processor when VDD drops below the minimum operating voltage. Below minimum VDD, the processor executes instructions incorrectly — I/O pins may toggle unpredictably. Enable the hardware brownout detector; do not rely on software voltage monitoring.
- **EMC (electromagnetic compatibility)**: Embedded systems with switching loads (relays, motors, PWM-driven heaters) generate electromagnetic interference that can corrupt sensitive analog inputs and digital communication. Route analog and digital grounds separately, meeting at a single point. Use opto-isolation for all off-board digital I/O. Add ferrite beads on cables leaving the enclosure.
- **Reverse polarity protection**: A reversed power supply connection destroys the MCU and most ICs instantly. Add a series diode (1N4007, 1V drop) or a MOSFET-based reverse polarity circuit (near-zero voltage drop). For battery-powered systems, use a polarized connector that cannot be reversed.
- **Overcurrent protection on I/O**: GPIO pins typically source/sink 4-20 mA maximum. Exceeding this destroys the pin driver. Use buffer ICs or transistor drivers for loads exceeding 20 mA. Add current-limiting resistors (220-470 Ω) on all digital outputs connected to off-board circuitry.

## 9. Quality Control

### Hardware Acceptance Tests

- **Power rail verification**: Measure VDD at the MCU pins under all operating conditions (idle, full load, all outputs driven). VDD must remain within specification (e.g., 3.0-3.6V for 3.3V MCU). Ripple <50 mV peak-to-peak.
- **ADC accuracy test**: Apply known voltage levels (0V, VREF/4, VREF/2, 3VREF/4, VREF) and verify ADC readings are within ±1 LSB of expected values. Linearity error must not exceed datasheet specification.
- **Communication stress test**: Send 10,000 frames at maximum baud rate with CRC check. Zero errors expected over a properly terminated bus.

### Firmware Quality

- **Watchdog test**: Intentionally disable the watchdog kick and verify the system resets within the expected timeout. Verify that the reset cause register indicates watchdog timeout.
- **Interrupt stress test**: Generate simultaneous interrupt sources at maximum rate. Verify no interrupts are lost and no priority inversion occurs.
- **Long-duration soak test**: Run the system for 24-72 hours continuous under realistic load. Monitor for memory leaks, timer drift, and communication errors.

### Environmental Tests

- **Temperature range**: Verify correct operation across the specified temperature range (typically -40°C to +85°C for industrial grade, 0°C to +70°C for commercial). ADC accuracy typically drifts 2-5 LSB over temperature — calibrate at two temperature points if needed.

## 10. Variations and Alternatives

### Bare-Metal Firmware

The firmware runs directly on the hardware with no operating system. A super-loop architecture: `while(1) { read_sensors(); compute_control(); update_outputs(); service_watchdog(); }`. Simple, deterministic, no RTOS overhead. Suitable for systems with <5 concurrent tasks and simple timing requirements. The default approach for most embedded bootstrapping.

### Real-Time Operating System (RTOS)

A minimal RTOS provides task scheduling (preemptive priority-based), inter-task communication (queues, semaphores), and timer services. overhead: 1-5 KB flash, 500 bytes-2 KB RAM. Appropriate when the system has 5+ concurrent tasks with different priority levels and timing requirements. Examples: FreeRTOS, Zephyr. The RTOS itself is software — see software-bootstrapping domain for construction methodology.

### FPGA-Based Control

For applications requiring sub-microsecond deterministic response or custom signal processing, implement the control logic directly in FPGA fabric. The FPGA processes sensor data and drives actuants in hardware (no software latency). A soft processor core handles non-time-critical tasks (communication, user interface). The control loop runs at the FPGA clock rate (50-200 MHz), providing nanosecond-level timing resolution.

### PLC (Programmable Logic Controller)

Industrial control using standardized PLC hardware: rack-mounted I/O modules, ladder logic programming, built-in isolation and fault tolerance. Higher cost per channel than custom MCU boards but faster development for standard industrial control tasks. The PLC itself is a packaged embedded system — this option trades hardware flexibility for development speed.

### Comparison for Bootstrap Context

| Approach | Development time | Determinism | Cost/channel | Flexibility |
|----------|-----------------|-------------|-------------|-------------|
| Bare-metal MCU | Days | Good (μs) | $2-10 | High |
| MCU + RTOS | Weeks | Good (μs) | $2-10 + RTOS port | High |
| FPGA + soft processor | Weeks-months | Excellent (ns) | $15-50 | Very high |
| PLC | Hours-days | Good (ms) | $50-200/channel | Low (fixed I/O types) |

## 11. References

- [`computing.computer-architecture`](computer-architecture.md) — CPU design, instruction sets, memory hierarchy, bus architecture. The hardware foundation for embedded processors.
- [`computing.logic-design`](logic-design.md) — Gate-level design and FPGA methodology used for custom embedded hardware.
- [`computing.digital-logic`](digital-logic.md) — Transistor-level gate physics, arithmetic circuits, and memory cells.
- [`computing.data-storage`](data-storage.md) — Flash memory and EEPROM used for embedded firmware storage.
- [`electronics.semiconductor-devices`](../electronics/semiconductor-devices.md) — Diodes and transistors used in sensor interface circuits and power switching.
- [`electronics.passive-components`](../electronics/passive-components.md) — Resistors, capacitors, and inductors for signal conditioning and filtering.
- [`electronics.pcb-fabrication`](../electronics/pcb-fabrication.md) — PCB layout considerations for mixed-signal embedded designs.
- [`electronics.power-electronics`](../electronics/power-electronics.md) — Power supply and motor drive design for embedded systems.

---

*Part of the [Bootciv Tech Tree](../index.md) · [Computing](./index.md) · [All Domains](../index.md)*
