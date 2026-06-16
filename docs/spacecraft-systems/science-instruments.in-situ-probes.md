# In-Situ Probes

> **Node ID**: spacecraft-systems.science-instruments.in-situ-probes
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.science-instruments`](./science-instruments.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: science_payloads
> **Critical**: No

In-situ probes directly sample surface materials and atmospheres for compositional analysis. Unlike remote-sensing spectrometers, these instruments ingest and analyze physical samples — providing definitive identification of minerals, organics, and isotopes. See [Science Instruments](./science-instruments.md) for the full instrument context.

## Instrument Types

1. **Mass spectrometers (MS)**: ionize sample molecules and separate by mass-to-charge ratio (m/z). Quadrupole MS (SAM on Curiosity: 2-535 Da), ion trap, or time-of-flight designs. Sensitivity: parts-per-billion for organic molecules.
2. **Gas chromatographs (GC)**: separate volatile compounds by retention time in a capillary column before MS detection. SAM has 6 chromatographic columns for C1-C12 organics.
3. **X-ray diffraction/fluorescence (XRD/XRF)**: identify crystalline mineral phases by Bragg diffraction (CheMin on Curiosity: Co K-alpha source, 5-50° 2-theta). Simultaneous XRF for elemental composition.
4. **Tunable laser spectrometers (TLS)**: measure trace gases and isotopic ratios via absorption spectroscopy. SAM TLS detects methane at sub-ppb levels using a 2-μm diode laser in a Herriott cell (8.96 m path).
5. **Sampling mechanisms**: pneumatic drills (Curiosity, Perseverance), scoops (Phoenix), pyrotechnic penetrators (sampling probes), and pneumatic transfer tubes delivering powder to instrument inlets.

## Key Parameters

- **Sample size**: 10-100 mg powdered solid (CheMin), or 0.1-1 cc gas (SAM)
- **Pyrolysis temperature**: up to 1100 °C (SAM) to release volatiles from refractory minerals
- **Detection limit**: ppb (organics by GCMS); sub-ppb (methane by TLS)
- **Operating power**: 20-100 W during analysis; 5 W standby

## See Also

- [Science Instruments](./science-instruments.md) — parent capability
- [Spectrometers](./science-instruments.spectrometers.md) — remote-sensing spectroscopy
- [Chemistry](../chemistry/index.md) — analytical chemistry foundations

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
