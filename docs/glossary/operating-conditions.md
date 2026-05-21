# Operating Conditions

> **Type**: noun | **Tier**: critical | **Domains**: chemistry, photolithography

The specific set of parameters — temperature, pressure, gas flow rates, concentrations, and durations — under which a process runs. In low-pressure chemical vapor deposition (LPCVD), operating conditions are 25-250 Pa (0.2-2 Torr) at 550-900°C in a hot-wall reactor using resistance-heated quartz tubes. In the Haber-Bosch process, conditions are 400-500°C at 15-30 MPa with an iron catalyst. Operating conditions are the control knobs that determine process yield, product quality, and throughput.

## Context in the Tech Tree

Operating conditions are specified for every controlled process in the tech tree. In the chemistry domain, ammonia synthesis, electrolysis, and chemical vapor deposition each have precisely defined conditions that must be maintained within narrow ranges. In the photolithography domain, fab processes (oxidation, deposition, etching, implantation) have specific operating conditions for each step — deviation outside specified ranges produces defective wafers.

The difference between a process that works and one that does not often comes down to operating conditions. A catalyst that achieves 98% conversion at 450°C may drop to 20% at 400°C. A vacuum process that runs correctly at 100 Pa may fail at 200 Pa due to mean free path changes affecting gas-phase uniformity.

## Technical Details

Operating conditions are determined through process development — systematic variation of parameters to find optimal combinations. Response surface methodology maps the relationship between input variables (temperature, pressure, concentration, flow rate) and output variables (yield, purity, deposition rate, etch rate, uniformity). The resulting process window defines the acceptable range for each parameter.

Process control maintains operating conditions within specified limits using feedback loops: sensors measure the controlled variable (temperature, pressure, flow rate), controllers compare the measurement to the setpoint, and actuators (heaters, valves, mass flow controllers) adjust the process input to minimize deviation. PID (proportional-integral-derivative) control is the standard algorithm. For semiconductor manufacturing, process control tolerances are extremely tight — temperature ±0.5°C, pressure ±1%, gas flow ±1% of setpoint.

## Related Terms

- [Measurement](./measurement.md) — monitoring operating conditions requires measurement
- [Manufacturing](./manufacturing.md) — manufacturing processes are defined by operating conditions
- [Limitations](./limitations.md) — equipment limitations constrain achievable operating conditions

## Appears In

- [Ammonia](../chemistry/ammonia.md)
- [Electrolysis](../chemistry/electrolysis.md)
- [Fab Processes](../photolithography/fab-processes.md)
