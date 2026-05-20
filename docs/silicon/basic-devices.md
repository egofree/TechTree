# Basic Semiconductor Devices

> **Node ID**: silicon.basic-devices
> **Domain**: [Silicon](./)
> **Dependencies**: `chemistry.acids`, `silicon.crystal-growth`, `gas-handling.vacuum`
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

#### MOSFETs & CMOS

**MOSFET structure**: Metal-Oxide-Semiconductor Field-Effect Transistor. A gate electrode insulated from the semiconductor channel by a thin layer of SiO₂ (gate oxide). Source and drain regions are doped opposite to the substrate. Voltage on the gate creates an electric field that induces a conductive channel between source and drain — no current flows through the gate itself (unlike bipolar transistors). Two modes: **enhancement mode** (normally off, channel forms when gate voltage applied — the standard for logic) and **depletion mode** (normally on, channel forms at zero gate voltage, requires gate voltage to turn off — used for load resistors and analog switches).

**NMOS** (N-channel MOSFET): Electrons carry current in n-type channel induced in p-type substrate. Higher electron mobility (~2.5× hole mobility) means NMOS is faster and lower resistance than PMOS for the same geometry. Substrate is p-type silicon, source and drain are n+ doped regions. Gate voltage above threshold induces n-type inversion layer (channel) connecting source to drain. Dominant transistor for 1970s microprocessors (Intel 4004, 8080).

**PMOS** (P-channel MOSFET): Holes carry current in p-type channel induced in n-type substrate. Slower than NMOS due to lower hole mobility, but was actually developed first because it was easier to manufacture with early processing (contamination issues favored p-channel operation). Substrate is n-type silicon, source and drain are p+ doped regions. Used in combination with NMOS to form CMOS circuits.

**CMOS** (Complementary MOS): The key breakthrough that enabled VLSI. Uses NMOS and PMOS transistors in complementary pairs. In a CMOS inverter: when input is high, NMOS turns on and PMOS turns off → output pulled low. When input is low, PMOS turns on and NMOS turns off → output pulled high. In either steady state, only one transistor is on and there is no DC path from power to ground — **near-zero static power dissipation**. This is the fundamental advantage over NMOS-only logic (which draws static power through load transistors). Power consumption scales with switching frequency and capacitance only (P = fCV²). CMOS enabled billion-transistor chips that would be thermally impossible with NMOS alone.

**Gate oxide**: SiO₂ grown by thermal oxidation of silicon (dry O₂ at 900-1100°C or wet O₂/H₂O at 800-950°C). Thickness 5-50 nm depending on technology generation. Thinner oxide → stronger gate coupling → faster switching, but exponentially higher gate leakage current (quantum tunneling through oxide). Oxide quality is critical — even a single defect in the gate oxide can cause catastrophic breakdown (short circuit from gate to channel). Oxide integrity requires ultra-clean processing and careful handling.

**Threshold voltage** (Vth): Minimum gate-to-source voltage required to induce a conductive channel. Typically 0.5-1.5V. Controlled by substrate doping concentration (higher doping → higher Vth), oxide thickness (thinner oxide → lower Vth), and gate electrode material. Matching Vth between NMOS and PMOS transistors is essential for symmetric CMOS switching characteristics. Process variations in threshold voltage are a major yield limiter.

**Scaling** (Dennard scaling rules): Shrink all device dimensions (channel length, oxide thickness, junction depth) by factor k while scaling voltage by k. Result: transistors are k² times smaller (2× per generation → 4× more per chip), k times faster, and power density remains constant. This held from the 1970s to ~2006. Breakdown cause: as oxide thickness approached a few nm, gate leakage current from quantum tunneling became unacceptable. Voltage could no longer scale proportionally → power density increased → the "power wall." Modern scaling continues geometry reduction but requires architectural workarounds (finFETs, multi-core, dark silicon).

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

### Safety Hazards

Semiconductor device fabrication uses some of the most dangerous chemicals in industrial processing:
- **Hydrofluoric acid (HF)**: Used at 5-10% concentration for phosphorus glass removal and oxide etching. HF penetrates skin painlessly, attacks deep tissue and bone, and causes systemic fluoride poisoning. A splash covering ~2.5% of body surface area (palm-sized) from 50% HF can be lethal; even 5-10% solutions cause serious burns. **Calcium gluconate gel (2.5%) must be on-site and accessible before any HF work begins.** Apply to exposed area immediately and seek emergency medical treatment — do not wait for pain. PPE: neoprene or thick nitrile gloves (double-gloving recommended), face shield, chemical splash apron, closed-toe shoes. Work in fume hood with local exhaust. Never store or handle HF in glass containers — use PTFE or polyethylene only.
- **POCl₃ (phosphorus oxychloride)**: Used for n-type emitter diffusion. Reacts violently with moisture in air, releasing HCl gas and phosphoric acid mist. Toxic by inhalation — causes severe respiratory burns and pulmonary edema. Handle in sealed gas delivery system with nitrogen purge. Leak detection: HCl monitor in furnace area. PPE: full-face respirator with acid gas cartridge for cylinder changes, chemical splash suit.
- **NaOH / KOH (caustic etchants)**: 20-40% solutions at 80°C for saw-damage removal and texturing. Causes deep caustic burns on skin and permanent eye damage. Heat increases severity. PPE: chemical splash goggles (not just safety glasses), nitrile gloves, apron. Eye wash station within 10 seconds travel. If splashed in eyes, flush with water for 15+ minutes immediately.
- **Belt furnace burn hazard**: Metal contacts are fired at 700-800°C on a moving belt. Exposed hot surfaces, infrared radiation. Thermal gloves and face shield for loading/unloading. Belt pinch points — keep hands clear of moving belt edges.
- **Vacuum chamber implosion**: Evaporation and sputtering chambers are evacuated to 10⁻⁵-10⁻⁶ Torr. A flawed glass viewport or corroded chamber wall can implode violently. Inspect viewports for scratches or star cracks before each pump-down. Safety glasses at all times near evacuated chambers. Never exceed rated pressure differential.

---

*Part of the [Bootciv Tech Tree](../) • [Silicon](./) • [All Domains](../)*
