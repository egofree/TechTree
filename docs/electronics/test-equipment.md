# Electronic Test Equipment

> **Node ID**: electronics.test-equipment
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md), [`electronics.pcb-fabrication`](pcb-fabrication.md)
> **Enables**: [`electronics.assembly`](assembly.md), [`electronics.power-electronics`](power-electronics.md), [`computing.logic-design`](../computing/logic-design.md)
> **Timeline**: Years 30-60+
> **Outputs**: voltage_measurement, current_measurement, resistance_measurement, waveform_visualization
> **Critical**: No — basic measurements can be made with a simple galvanometer and resistors, but precision test equipment is required for reliable electronics development beyond simple circuits

## Principle

Electronic test equipment measures electrical quantities — voltage, current, resistance, frequency, and waveform characteristics — enabling verification, debugging, and characterization of electronic circuits. The three fundamental instruments are the multimeter (measures DC/AC voltage, current, and resistance), the oscilloscope (displays voltage waveforms vs. time), and the logic analyzer (captures and displays digital bus states).

The operating principle of each instrument:

- **Multimeter**: An analog-to-digital converter (dual-slope integrating ADC for precision, or successive-approximation for speed) measures voltage directly. Current is measured as voltage across a precision shunt resistor (I = V/R_shunt). Resistance is measured by applying a known current and measuring the resulting voltage drop (R = V/I_source). Input impedance: >10 MΩ for voltage measurements (to avoid loading the circuit under test).
- **Oscilloscope**: A high-speed ADC (100 MS/s to 10 GS/s) samples the input voltage at regular intervals and stores the samples in a circular memory buffer. A trigger circuit captures the waveform when a specified condition is met (edge crossing, pulse width, etc.). The stored samples are displayed as a voltage-vs-time graph. Bandwidth determines the highest frequency the instrument can accurately display: a 100 MHz oscilloscope can display 100 MHz sine waves with <3 dB attenuation.
- **Logic analyzer**: Multiple digital inputs (8-136+ channels) sampled synchronously at high speed (100-500 MHz). Each sample is a 1 or 0 (above or below threshold). The captured data is displayed as timing waveforms or listed as state tables synchronized to a clock signal. Used for debugging microprocessor buses, communication protocols, and state machines.

## Constructability Assessment

**Requires further research.** Electronic test equipment at the complexity level described above requires advanced semiconductor devices (high-speed op-amps, precision ADCs, custom ASICs for signal processing), high-density PCBs with controlled impedance, and display technology (CRT or LCD). These represent the pinnacle of electronics manufacturing capability — achievable only after a fully functional semiconductor fabrication facility is operational.

### What Can Be Built Earlier

Before full test equipment is available, the following simpler instruments are constructible with Year 20-30 technology:

**Galvanometer-based multimeter (analog)**:

A moving-coil galvanometer (D'Arsonval movement) measures DC current by the torque on a coil in a magnetic field. The coil rotates against a spring, and the deflection angle is proportional to current. A basic movement might have 50 μA full-scale deflection (FSD) and 1000 Ω coil resistance.

- **DC voltage ranges**: Add series resistors. For 0-10 V range with a 50 μA/1000 Ω movement: total resistance needed = 10 V / 50 μA = 200 kΩ. Series resistor = 200 kΩ - 1 kΩ = 199 kΩ. Multiple ranges by switching series resistors.
- **DC current ranges**: Add shunt resistors in parallel. For 0-1 A range: shunt resistance = (50 μA × 1000 Ω) / (1 A - 50 μA) ≈ 0.050 Ω. Precision wire-wound or manganin shunt.
- **Resistance measurement**: Apply a known voltage through a known resistor, measure current. Requires an internal battery. Accuracy: ±5-10%.

**Construction** (galvanometer movement):

1. **Wind the coil**: Wind 100-500 turns of enameled copper wire (40-44 AWG, 0.08-0.06 mm) on a lightweight aluminum or plastic former (10-20 mm × 8-15 mm rectangular). The coil must rotate freely in the gap of a permanent magnet. Coil resistance: 500-2000 Ω. Suspend the coil on taut-band or pivot-and-jewel bearings.
2. **Magnet system**: A permanent magnet (Alnico or ferrite) with soft-iron pole pieces concentrating the magnetic field in the gap where the coil sits. Field strength: 0.1-0.3 T. The stronger the field, the more sensitive the movement.
3. **Pointer and scale**: Attach a lightweight aluminum pointer (50-80 mm) to the coil. Calibrate the scale by applying known currents and marking the deflection points. A linear scale indicates a uniform magnetic field in the gap.
4. **Range switching**: Wire a rotary switch to select between series resistors (voltage ranges), shunt resistors (current ranges), and the internal battery + known resistor (resistance ranges).

### What Remains Out of Reach

The following instruments require semiconductor capabilities documented in [Semiconductor Devices](semiconductor-devices.md) and are not constructible until those capabilities are fully developed:

- **Digital multimeter (DMM)**: Requires a precision ADC (dual-slope or sigma-delta), microcontroller or custom logic, LCD display, and precision voltage reference. Accuracy: ±0.1-0.5%. Construction requires semiconductor fab + display manufacturing.
- **Oscilloscope**: Requires a high-speed ADC pipeline (100+ MS/s), fast memory (SRAM or SDRAM), trigger circuitry with adjustable hysteresis, and a display (CRT with deflection amplifiers or LCD with rasterizer). Even the simplest storage oscilloscope requires hundreds of ICs or a modern SoC. Not constructible from discrete components at any practical bandwidth.
- **Logic analyzer**: Requires high-speed digital input comparators, deep capture memory, and a display + user interface. Fundamentally a specialized computer — requires Year 50+ computing capability.
- **LCR meter**: Requires AC signal generation, precision impedance measurement bridge, and phase-sensitive detection. Constructible as a Wheatstone bridge with AC excitation and null detector at moderate accuracy (±1-5%), but precision LCR meters (±0.1%) require semiconductor-based circuitry.

## Materials (Galvanometer Multimeter)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Copper magnet wire | 20-50 m | 40-44 AWG (0.06-0.08 mm), enamel insulation | [Electrolysis](../chemistry/electrolysis.md) | — |
| Permanent magnet | 1 piece | Alnico or ferrite, 20-40 mm, field >0.1 T in gap | [Metals](../metals/index.md) | Electromagnet (requires DC current) |
| Soft iron pole pieces | 2 pieces | Machined to concentrate field in cylindrical gap | [Iron & Steel](../metals/iron-steel.md) | — |
| Precision resistors | 5-10 | Wire-wound or metal film, 0.1-5% tolerance | [Passive Components](passive-components.md) | Carbon composition (5-20% tolerance) |
| Manganin wire (shunts) | 0.5-2 m | Low temperature coefficient (<15 ppm/°C), 0.05-0.5 mm | [Metals](../metals/alloys.md) | Constantan (higher thermal EMF) |
| Aluminum pointer | 1 piece | 50-80 mm, tapered, <0.5 g | [Metals](../metals/aluminum.md) | Bamboo splint (lighter, less rigid) |
| Rotary switch | 1 | Multi-position, 12-20 positions | [Electrical Systems](electrical-systems.md) | Individual binding posts per range |
| Battery | 1 | 1.5-9 V (for resistance measurement) | [Energy Storage](../energy/storage.md) | — |
| Case and scale plate | 1 | Wooden or sheet metal enclosure, printed or engraved scale | [Foundations](../foundations/tools-basic.md) | Bakelite case |

## Expected Performance (Galvanometer Multimeter)

| Parameter | Value |
|-----------|-------|
| DC voltage ranges | 0-1 V, 0-10 V, 0-100 V, 0-1000 V |
| DC voltage accuracy | ±3-5% of full scale |
| DC current ranges | 0-50 μA, 0-1 mA, 0-100 mA, 0-1 A |
| DC current accuracy | ±3-5% of full scale |
| Resistance ranges | 0-1 kΩ, 0-100 kΩ, 0-10 MΩ (battery-powered) |
| Resistance accuracy | ±5-10% |
| Input impedance (voltage) | 20 kΩ/V (50 μA movement) — loads circuit under test |
| AC measurement | Not available (requires rectifier) — AC rectifier add-on: ±10% accuracy |
| Frequency response (with rectifier) | 20-1000 Hz (copper-oxide or germanium rectifier) |

## Expected Performance (Digital Instruments — Target)

| Parameter | Value |
|-----------|-------|
| DMM DC voltage accuracy | ±0.1-0.5% + 1 digit |
| DMM resolution | 3.5 to 6.5 digits (1999 to 2,200,000 counts) |
| Oscilloscope bandwidth | 50-500 MHz |
| Oscilloscope sample rate | 500 MS/s to 5 GS/s |
| Oscilloscope channels | 2-4 |
| Oscilloscope memory depth | 1K-100M points per channel |
| Logic analyzer channels | 16-136 |
| Logic analyzer sample rate | 100-500 MHz |
| LCR meter accuracy | ±0.1-1% |

## See Also

- [Electronics Assembly](assembly.md) — test procedures for assembled PCBs
- [Electrical Systems](electrical-systems.md) — power distribution testing with multimeters and meggers
- [Power Electronics](power-electronics.md) — oscilloscope verification of switching waveforms
- [Semiconductor Devices](semiconductor-devices.md) — devices required for digital test equipment
- [Passive Components](passive-components.md) — precision resistors for measurement circuits
- [Measurement](../measurement/electrical-instruments.md) — general electrical measurement principles

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](./index.md) • [All Domains](../index.md)*
