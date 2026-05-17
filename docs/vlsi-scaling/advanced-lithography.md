# Advanced Lithography

> **Node ID**: `vlsi-scaling.advanced-lithography`
> **Domain**: [VLSI Scaling & Advanced Semiconductor](./)
> **Dependencies**: `photolithography.resists-masks`, `vacuum-optics.optics-inspection`
> **Timeline**: Years 70-200+
> **Outputs**: advanced_lithography, euv_capability, duv_capability

### Advanced Lithography Scaling

**Contact/proximity printing** (Photolithography baseline — features down to ~2-5 μm):
- Mask contacts or nearly contacts wafer. Simple, but mask damage from contact limits yield. Good enough for early production.

**Projection steppers/scanners** (features down to ~0.5 μm):
- **Step-and-repeat**: Lens projects reduced mask image (typically 5:1 or 10:1 reduction) onto one exposure field (~20×20 mm). Stage steps to next field. Each wafer requires 50-200+ exposures.
- **Alignment**: Automatic alignment using microscope + pattern recognition. Overlay accuracy: ±0.1-0.5 μm.
- **I-line (365 nm)**: Mercury lamp + narrowband filter. Features down to ~0.35 μm with resolution enhancement techniques (RET): phase-shift masks, off-axis illumination, optical proximity correction (OPC).

**DUV lithography** (features down to ~0.07 μm with immersion):
- **KrF excimer laser** (248 nm): Features down to ~0.25 μm. Laser gas: Kr + F₂ mixture, electrically pumped. 1000 Hz pulse rate, ~10 W output.
- **ArF excimer laser** (193 nm): Features down to ~0.13 μm (dry), ~0.07 μm (immersion). Immersion: water layer between lens and wafer increases numerical aperture (NA >1.0).
- **Resist chemistry**: Chemically amplified resists (CAR) — photoacid generator (PAG) produces acid on exposure, acid catalytically cleaves protecting groups during PEB, amplifying sensitivity 10-100x. Required for low DUV exposure doses. Environmental stability challenging (airborne base contaminants neutralize acid).

**EUV lithography** (features below 7 nm — extremely long-term):
- **Source**: 13.5 nm wavelength from tin (Sn) plasma. High-power CO₂ laser hits Sn droplets at 50 kHz → plasma emits EUV. Power: 200-500 W at intermediate focus. Everything absorbs EUV — must use reflective optics, not lenses.
- **Optics**: Multilayer Mo/Si mirrors (40+ bilayer pairs, ~3 nm period each). Each mirror reflects ~70% of EUV. 10-mirror system transmits only ~3% of source light. Mirror figure accuracy: <0.1 nm RMS.
- **Resist**: New chemically amplified resists, metal-oxide resists, or molecular glass resists. Sensitivity, resolution, and line-edge roughness (LER) are competing requirements.
- **Vacuum**: Entire beam path must be in high vacuum (EUV absorbed by any gas).
- **This is one of the last achievements — incredibly demanding.** Even with full modern knowledge, EUV required 20+ years and $10B+ investment by ASML and partners.
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
