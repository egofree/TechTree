# Basic Semiconductor Devices

> **Node ID**: `silicon.basic-devices`
> **Domain**: [Silicon](./)
> **Dependencies**: `chemistry.acids`, `silicon.crystal-growth`, `vacuum-optics.vacuum-systems`
> **Timeline**: Years 30-50
> **Outputs**: solar_cells, diodes, transistors

### Basic Semiconductor Devices

#### Solar Cells (Primary Target — simplest useful semiconductor device)

**Structure**: Large-area (100-300 cm²) pn junction on single-crystal or multicrystalline silicon wafer.

**Process flow**:
1. **Starting wafer**: p-type (boron-doped), 1-10 Ω·cm, <100> orientation, 180-300 μm thick. Saw-damage etch in NaOH or KOH (20-40%, 80°C, 2-5 min) to remove ~10-20 μm of damaged surface.
2. **Texturing** (optional, improves light trapping): Anisotropic etch in KOH/IPA solution (2-5% KOH, 5-10% IPA, 70-80°C, 20-30 min). Pyramidal texture on <100> surface reduces reflection from ~35% to ~10%.
3. **Emitter diffusion**: Phosphorus diffusion to form n-type layer. POCl₃ gas in diffusion furnace at 800-900°C for 15-60 min. Target junction depth 0.3-1.0 μm. Sheet resistance 40-80 Ω/sq. Forms n+/p junction.
4. **Phosphorus glass removal**: HF dip (5-10%, 30-60 sec) removes PSG (phosphosilicate glass formed during diffusion).
5. **Anti-reflection coating**: Deposit SiNₓ (silicon nitride) by PECVD at 300-400°C. Thickness ~75 nm (quarter-wave for peak solar wavelength). Also serves as surface passivation.
6. **Metallization — front contacts**: Screen-print silver paste in grid pattern (finger width 50-100 μm, bus bar 1-2 mm). Dry at 150-200°C, fire at 700-800°C (fast ramp, belt furnace, ~30 sec at peak). Ag paste etches through SiNₓ to contact n+ emitter.
7. **Metallization — rear contact**: Screen-print Al paste (full area). Fire simultaneously with front. Al alloys with Si, forms p+ back surface field (BSF) — reduces recombination at rear surface.
8. **Edge isolation**: Laser scribe or plasma etch around wafer edge to prevent front-rear short circuit through junction that wraps around edges.
9. **Testing**: I-V curve under simulated sunlight (AM1.5, 1000 W/m²). Measure Voc, Isc, fill factor, efficiency.

**Expected performance**:
- First cells: 5-10% efficiency (poor passivation, simple contacts)
- Mature process: 15-18% efficiency (screen-printed, BSF, AR coating)
- Advanced: 20%+ (PERC, bifacial — VLSI Scaling stage)

**Solar cell as energy amplifier**: Each cm² of 15% efficient solar cell produces ~15 mW peak. A 156×156 mm cell produces ~3.6 W peak. Over 20-year lifetime: ~50 kWh per cell. Energy payback time: 1-3 years. The solar cell feedback loop (solar → electricity → more silicon furnaces → more solar cells) is one of the most important positive feedback loops in the entire tech tree.

#### Diodes & Simple Transistors

**Point-contact diode**: Sharpened tungsten or phosphor-bronze wire whisker pressed against n-type silicon crystal. Forms small p-type region at contact point (metal-semiconductor junction). Simple, requires no processing. Used for: rectifiers, radio detectors.

**Alloy junction transistor**: Place indium dots on both sides of thin n-type germanium or silicon wafer (~100-200 μm). Heat to 500-600°C. Indium alloys into semiconductor, creating p-type regions. Result: pnp transistor. Simple but low performance (low frequency, high leakage). Historically important (first transistors, 1950s).

**Diffused transistor**: Phosphorus diffused into p-type wafer through oxide mask window to form base and emitter. More controlled geometry. Requires: oxidation furnace, photolithography (or shadow masking), diffusion furnace. Bridge to the Photolithography stage planar process.

### Metallization & Contacts

**Vacuum evaporation** (simplest deposition method):
- **Process**: Place metal source (Al, Au, Ti) in tungsten or molybdenum boat or basket in vacuum chamber. Pump to 10⁻⁵ to 10⁻⁶ Torr. Heat source resistively (current through boat) to metal's evaporation temperature (Al: 1200°C, Au: 1500°C). Metal vapor travels in straight lines to substrate. Deposit 0.1-2 μm film.
- **Rate monitoring**: Quartz crystal microbalance — crystal oscillation frequency decreases as metal deposits. Calibrated to thickness.
- **Uniformity**: Source-to-substrate distance 30-50 cm. Rotating planetary fixture for uniform thickness on multiple wafers.
- **Pattern definition**: Shadow mask (thin metal sheet with cutout pattern held against wafer during deposition) or lift-off (pattern photoresist before deposition, dissolve resist after — metal on resist lifts off, leaving patterned metal on wafer).

**Screen printing** (for solar cell contacts):
- Print conductive paste (Ag, Al, or carbon) through mesh screen with patterned emulsion. Squeegee forces paste through open areas onto wafer. Dry and fire. Simpler than evaporation, lower resolution (~50 μm minimum line width).

**Sputtering** (later, more versatile):
- **Process**: Argon plasma bombards target material → atoms ejected → deposit on substrate. Works for any material (metals, insulators, alloys). Better step coverage than evaporation. Requires: RF or DC power supply, vacuum system, target material, argon gas.
- **DC sputtering**: Conductive targets only (metals). 200-1000V, 0.1-10 Torr Ar.
- **RF sputtering**: Any target material (including insulators). 13.56 MHz standard frequency.
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
