# Measurement

> **Type**: material | **Tier**: critical | **Domains**: measurement, photolithography, silicon, textiles

The process of determining the magnitude of a physical quantity — length, mass, temperature, pressure, voltage, optical rotation, or any other observable property. In the tech tree, measurement ranges from simple visual comparison ( judging firing temperature by clay color) to instrumental precision (polarimetry for optical rotation: specific rotation [α] = α/(c·l), where c is concentration and l is path length). Measurement underpins quality control, process monitoring, and scientific understanding at every stage.

## Context in the Tech Tree

The measurement domain provides the instrumentation and techniques that every other domain relies on for process control. Temperature measurement (thermocouples, pyrometers, resistance thermometers) controls kiln firing, metal melting, and chemical reaction temperatures. Pressure measurement (manometers, Bourdon gauges, vacuum ionization gauges) monitors steam boilers, vacuum systems, and gas processes. Electrical measurement (galvanometers, voltmeters, ammeters, Wheatstone bridges) characterizes generators, motors, and circuits. Optical measurement (spectrometers, polarimeters, interferometers) determines material composition, crystal quality, and surface flatness.

Silicon wafer production requires measurement at every step: crystal orientation (X-ray diffraction), resistivity (four-point probe), impurity concentration (mass spectrometry), surface flatness (interferometry), and dimensional tolerances (precision metrology). Photolithography depends on overlay measurement to align successive pattern layers within nanometer tolerances.

## Technical Details

Measurement accuracy depends on calibration against known standards, instrument resolution (the smallest detectable change), and measurement precision (repeatability). The measurement domain progresses from simple references (a marked stick for length, a known weight for mass) through mechanical instruments (micrometers, dial gauges) to electronic instruments (digital multimeters, automated test equipment) and optical instruments (interferometers, spectrometers).

Calibration chains trace working instruments back to primary standards. A shop-floor micrometer is calibrated against gauge blocks, which are calibrated against national reference standards. Each link in the chain has its own uncertainty, and these uncertainties accumulate. For the bootstrap sequence, establishing and maintaining calibration standards is essential — uncalibrated instruments produce unreliable measurements that propagate errors through every downstream process.

## Related Terms

- [Materials](./materials.md) — material properties are defined through measurement
- [Limitations](./limitations.md) — measurement precision limits process capability
- [Calibration](./calibration.md) — calibration ensures measurement accuracy

## Appears In

- [Optical Instruments](../measurement/optical-instruments.md)
- [Temperature & Pressure](../measurement/temperature-pressure.md)
- [Resists & Masks](../photolithography/resists-masks.md)
- [Silicon Purification](../silicon/purification.md)
