# Spectrometers

> **Node ID**: spacecraft-systems.science-instruments.spectrometers
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.science-instruments`](./science-instruments.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: science_payloads
> **Critical**: No

Spaceborne spectrometers analyze electromagnetic spectra across UV, visible, IR, and X-ray bands to determine the composition, temperature, and velocity of astronomical objects and planetary atmospheres. See [Science Instruments](./science-instruments.md) for the full instrument context.

## Types

1. **Dispersive (grating/prism)**: separates light by wavelength using a diffraction grating or prism. JWST NIRSpec (R~100-2700), Hubble WFC3 grism (R~100-700), COS FUV (R~3000-20,000).
2. **Fourier-transform (FTS)**: Michelson interferometer with scanning mirror; spectrum obtained via FFT of the interferogram. High throughput (Jacquinot advantage), simultaneous all-wavelength (Fellgett advantage). Used on Mars Climate Sounder, IASI on MetOp.
3. **Fabry-Perot (etalon)**: resonant cavity between two parallel plates transmits narrow wavelength bands. R~1000-10,000. Used for narrow-band imaging of atmospheric emission lines (MAVEN IUVS).
4. **Echelle**: high-order grating (m=10-100) with cross-disperser producing a 2D spectral format. R~10,000-100,000. Heritage from Hubble STIS.
5. **X-ray spectrometers**: CCD-based energy-dispersive detection (Chandra ACIS) or diffraction-grating spectrometers (Chandra HETG, R~1000).

## Key Parameters

- **Spectral resolution**: R = λ/Δλ; R~100 (low), R~1000 (medium), R~10,000+ (high)
- **Wavelength coverage**: 10 nm (EUV) to 500 μm (far-IR) depending on instrument
- **Detector type**: CCD (UV-vis), HgCdTe (near-IR), Si:As IBC (mid-IR), MCP (far-UV)
- **Cryogenic requirement**: 30-77 K for near-IR; <7 K for mid-IR (JWST MIRI)

## See Also

- [Science Instruments](./science-instruments.md) — parent capability
- [Optics](../optics/index.md) — gratings, prisms, mirrors
- [Silicon](../silicon/index.md) — detector substrates

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
