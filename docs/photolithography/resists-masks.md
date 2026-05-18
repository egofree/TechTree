# Photoresists, Masks & Lithography

> **Node ID**: `photolithography.resists-masks`
> **Domain**: [Photolithography & IC Fabrication](./)
> **Dependencies**: `chemistry`, `polymers.thermosets`
> **Enables**: `vlsi-scaling.advanced-lithography`
> **Timeline**: Years 40-70
> **Outputs**: photoresists, masks, lithography_tools, patterned_wafers

### Photoresists

**Bitumen resist** (simplest, historical — Niépce, 1826):
- Dissolve bitumen of Judea (natural asphalt) in lavender oil or turpentine. Coat on substrate. Expose to UV through mask (hours of exposure — very slow). Exposed areas harden (polymerize), unexposed areas dissolve in solvent. Low resolution (~100 μm+), very slow, but requires zero chemistry infrastructure.

**Dichromated gelatin** (mid-19th century):
- Mix gelatin (from animal collagen) with ammonium dichromate ((NH₄)₂Cr₂O₇, ~5-10%). Coat on substrate. UV exposure causes Cr(VI) → Cr(III) reduction, cross-linking gelatin (insoluble). Unexposed gelatin washes away in warm water. Resolution ~10-50 μm. Chromium compounds are toxic and carcinogenic — handle with care.

**Novolac + DNQ resist** (standard positive-tone photoresist, requires the Chemistry stage organic chemistry):
- **Novolac resin**: Phenol + formaldehyde condensation polymer (m-cresol variant for photoresist). See [Polymers](../polymers/index.md) for production. Molecular weight ~2000-5000. Dissolves in aqueous base (NaOH or TMAH).
- **DNQ sensitizer**: Diazonaphthoquinone sulfonate (from naphthol + diazotization). ~20-30% by weight in resist. Function: DNQ acts as dissolution inhibitor — unexposed resist does NOT dissolve in developer. UV exposure → DNQ undergoes Wolff rearrangement → forms indene carboxylic acid → actually ENHANCES dissolution in aqueous base. This is the positive-tone mechanism.
- **Solvent**: Ethyl lactate or propylene glycol monomethyl ether acetate (PGMEA). ~60-80% of resist formulation.
- **Spin coating**: Dispense ~2-5 ml resist on wafer center. Spin at 1000-6000 RPM for 30-60 seconds. Centrifugal force spreads resist uniformly. Thickness: 0.5-3 μm (depends on viscosity and spin speed — roughly t ∝ 1/√ω). Edge bead removal (EBR): spray solvent at wafer edge while spinning to remove thick bead that forms at edge.
- **Soft bake (pre-bake)**: 90-110°C for 60-90 seconds on hot plate. Drives off solvent. Residual solvent <3%.
- **Exposure**: UV light (365 nm i-line, 405 nm h-line, or 436 nm g-line from mercury lamp). Dose: 50-200 mJ/cm². Exposed regions become soluble.
- **Post-exposure bake (PEB)**: 110-130°C for 60-90 seconds. Improves pattern definition by reducing standing wave effects.
- **Development**: Aqueous base — 2.38% TMAH (tetramethylammonium hydroxide) for 30-90 seconds with gentle agitation. TMAH preferred over NaOH (metal-ion-free developer — sodium contamination degrades MOS devices).
- **Hard bake**: 120-150°C for 60-120 seconds. Cross-links resist for etch resistance. Not always needed.

### Polymer Packaging Materials
- **Epoxy encapsulation**: Two-part epoxy for die attach and hermetic sealing — see [Polymers](../polymers/index.md) and [Specialty Gases](../specialty-gases/gases-packaging-testing.md)
- **Plastic substrates and lead frames**: Molded plastic packages for integrated circuits
- **Phenolic laminate (FR-4)**: PCB substrate material from phenolic or epoxy resin impregnated glass fabric — see [Polymers](../polymers/index.md)
- **Photoresist dependency**: Novolac resin (phenol + formaldehyde condensation polymer) production path documented in [Polymers](../polymers/index.md), with monomer feedstocks from [Petrochemicals](../petrochemicals/petroleum-alternatives.md)

### Mask Making
- **Pattern generation**: Large-scale drawings → optical reduction onto photosensitive plates
- **Mask substrates**: Glass (or fused silica for UV transmission) + chrome or emulsion layer
- **Pattern transfer**: Photoreduction using precision optics
- **Alignment marks**: For multi-layer registration

### Lithography Tools
- **Contact/proximity printing**: Mask touches (or nearly touches) wafer → UV exposure
  - Simple but damages mask and wafer
- **Projection printing**: Lens projects mask image onto wafer
  - Requires good optics (from the Vacuum & Optics stage)
- **Exposure sources**: Mercury arc lamps in quartz envelopes (g, h, i-line UV)
- **Precision stages**: From machine shop — micrometer-precision X-Y-θ stages for alignment
- **Alignment microscopes**: For overlay registration between layers
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
