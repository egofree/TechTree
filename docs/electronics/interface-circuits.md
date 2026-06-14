# Interface Circuits

> **Node ID**: electronics.interface-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](../silicon/basic-devices.md), [`electronics.passive-components`](passive-components.md)
> **Timeline**: Years 30-50
> **Outputs**: mixed-signal-interface
> **Critical**: No — pedagogy layer; underlying active and passive device manufacturing capabilities are the critical prerequisites

This capability is the **design pedagogy hub** for the circuits that bridge the analog and digital worlds: analog-to-digital converters (ADCs), digital-to-analog converters (DACs), and the signal-conditioning chains that prepare real-world sensor outputs for conversion. It does not re-explain semiconductor fabrication — that is owned by [semiconductor devices](../silicon/basic-devices.md). It teaches how to *design with* those parts to measure continuous quantities with known resolution, sample rate, and noise floor.

## The Pedagogical Progression

Mixed-signal interface design is taught as a two-stage chain:

```
  physical quantity  -->  sensor + conditioning  -->  ADC  -->  digital word
        ^                        ^                      ^
   temperature,           amplifier, filter,        sample, quantize,
   pressure, light,        protection, span         encode
   strain, position        shift

  digital word  -->  DAC  -->  reconstruction filter  -->  analog output
```

First comes **conversion fundamentals** — what sampling and quantization mean, the Nyquist limit, the resolution/speed tradeoff that picks a converter architecture. Then **signal conditioning** — how to take a millivolt thermocouple or a bridge strain gauge and lift, filter, and protect it until it matches an ADC's input range. The progression is ADC/DAC theory → sensor-specific conditioning, mirroring the Mims *Sensor Projects* and *Op Amp* threads.

## Prerequisites (manufacturing, linked not duplicated)

- **[Semiconductor devices](../silicon/basic-devices.md)** — supplies the precision references, comparators, and analog switches inside SAR, flash, and integrating converters, plus the photosensors and temperature sensors at the front of conditioning chains.
- **[Passive components](passive-components.md)** — supplies the precision matched resistors (R-2R ladders demand <0.1% matching), the integration capacitors in dual-slope converters, and the anti-alias filter components.
- **[Analog circuits](analog-circuits.md)** — op-amp comparators drive SAR logic, and active anti-alias filters are pure op-amp technique taught in that family.

## Articles in this family

| Article | Scope | Key circuits |
|---------|-------|--------------|
| adc-circuits | analog → digital conversion | SAR, flash, dual-slope/integrating, sigma-delta |
| dac-circuits | digital → analog conversion | R-2R ladder, weighted-resistor, string, PWM-as-DAC |
| sensor-circuits | real-world signal conditioning | thermocouple/RTD cold-junction, strain-gauge bridge, light, pressure |

## Cross-references

- [Analog circuits](analog-circuits.md) — comparators, op-amp active filters, and Schmitt triggers are the building blocks reused here.
- [Measurement](../measurement/electrical-instruments.md) — instrument-grade ADCs/DACs live inside DMMs and scopes; this family owns their *design pedagogy*.
- [Computing: embedded systems](../computing/embedded-systems.md) — microcontroller ADC peripherals consume these design techniques at the system level.

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
