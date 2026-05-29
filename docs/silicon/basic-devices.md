# Basic Semiconductor Devices

> **Node ID**: silicon.basic-devices
> **Domain**: [Silicon](./index.md)
> **Dependencies**: [`chemistry.acids`](../chemistry/acids.md), [`gas-handling.vacuum`](../gas-handling/vacuum.md), [`metals.aluminum`](../metals/aluminum.md), [`silicon.crystal-growth`](crystal-growth.md), [`silicon.wafering`](wafering.md), [`vacuum.pumps`](../vacuum/pumps.md)
> **Enables**: [`computing.electronic`](../computing/electronic.md), [`electronics.assembly`](../electronics/assembly.md), [`vlsi-scaling.eda-design`](../vlsi-scaling/eda-design.md)
> **Timeline**: Years 30-50
> **Outputs**: solar_cells, diodes, transistors

### Basic Semiconductor Devices

#### Solar Cells (Primary Target — simplest useful semiconductor device)

**Structure**: Large-area (100-300 cm²) pn junction on single-crystal or multicrystalline silicon wafer.

**Materials**:
- P-type (boron-doped) silicon wafer, 1-10 Ω·cm, <100> orientation, 180-300 μm thick
- POCl₃ gas (phosphorus oxychloride) for n-type emitter diffusion
- HF (hydrofluoric acid), 5-10% concentration, for phosphorus glass removal
- SiNₓ (silicon nitride) for anti-reflection coating, deposited by PECVD
- Silver paste (front contacts): finger width 50-100 μm, bus bar 1-2 mm
- Aluminum paste (rear contact): full-area coverage

**Process flow**:
1. **Starting wafer**: p-type (boron-doped), 1-10 Ω·cm, <100> orientation, 180-300 μm thick. Saw-damage etch in NaOH or KOH (20-40%, 80°C, 2-5 min) to remove ~10-20 μm of damaged surface.
2. **[Texturing](../glossary/texturing.md)** (optional, improves light trapping): Anisotropic etch in KOH/IPA solution (2-5% KOH, 5-10% IPA, 70-80°C, 20-30 min). Pyramidal texture on <100> surface reduces reflection from ~35% to ~10%.
3. **Emitter diffusion**: Phosphorus diffusion to form n-type layer. POCl₃ gas in diffusion furnace at 800-900°C for 15-60 min. Target junction depth 0.3-1.0 μm. Sheet resistance 40-80 Ω/sq. Forms n+/p junction.
4. **Phosphorus glass removal**: HF dip (5-10%, 30-60 sec) removes PSG (phosphosilicate glass formed during diffusion).
5. **Anti-reflection coating**: Deposit SiNₓ (silicon nitride) by PECVD at 300-400°C. Thickness ~75 nm (quarter-wave for peak solar wavelength). Also serves as surface passivation.
6. **Metallization — front contacts**: Screen-print silver paste in grid pattern (finger width 50-100 μm, bus bar 1-2 mm). Dry at 150-200°C, fire at 700-800°C (fast ramp, belt furnace, ~30 sec at peak). Ag paste etches through SiNₓ to contact n+ emitter.
7. **Metallization — rear contact**: Screen-print Al paste (full area). Fire simultaneously with front. Al alloys with Si, forms p+ back surface field (BSF) — reduces recombination at rear surface.
8. **Edge isolation**: Laser scribe or plasma etch around wafer edge to prevent front-rear short circuit through junction that wraps around edges.
9. **Testing**: I-V curve under simulated sunlight (AM1.5, 1000 W/m²). Measure Voc, Isc, fill factor, efficiency.

**Verification**:
1. Measure I-V curve under AM1.5 solar simulator (1000 W/m², 25°C)
2. Check Voc > 0.58V and Isc > 8.0A for a 156×156 mm cell
3. Measure fill factor (FF) > 0.75; if lower, check for shunts via dark I-V measurement
4. Verify no front-rear short by measuring isolation resistance > 1 MΩ at 500V

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

**MOSFET structure**: Metal-Oxide-Semiconductor Field-Effect Transistor. A gate electrode insulated from the semiconductor channel by a thin layer of SiO₂ (gate oxide). Source and drain regions are doped opposite to the substrate. Voltage on the gate creates an electric field that induces a conductive channel between source and drain — no current flows through the gate itself (unlike bipolar transistors). Two modes: **[enhancement mode](../glossary/enhancement-mode.md)** (normally off, channel forms when gate voltage applied — the standard for logic) and **[depletion mode](../glossary/depletion-mode.md)** (normally on, channel forms at zero gate voltage, requires gate voltage to turn off — used for load resistors and analog switches).

**[NMOS](../glossary/nmos.md)** (N-channel MOSFET): Electrons carry current in n-type channel induced in p-type substrate. Higher electron mobility (~2.5× hole mobility) means NMOS is faster and lower resistance than PMOS for the same geometry. Substrate is p-type silicon, source and drain are n+ doped regions. Gate voltage above threshold induces n-type inversion layer (channel) connecting source to drain. Dominant transistor for 1970s microprocessors (Intel 4004, 8080).

**[PMOS](../glossary/pmos.md)** (P-channel MOSFET): Holes carry current in p-type channel induced in n-type substrate. Slower than NMOS due to lower hole mobility, but was actually developed first because it was easier to manufacture with early processing (contamination issues favored p-channel operation). Substrate is n-type silicon, source and drain are p+ doped regions. Used in combination with NMOS to form CMOS circuits.

**[CMOS](../glossary/cmos.md)** (Complementary MOS): The key breakthrough that enabled VLSI. Uses NMOS and PMOS transistors in complementary pairs. In a CMOS inverter: when input is high, NMOS turns on and PMOS turns off → output pulled low. When input is low, PMOS turns on and NMOS turns off → output pulled high. In either steady state, only one transistor is on and there is no DC path from power to ground — **near-zero static power dissipation**. This is the fundamental advantage over NMOS-only logic (which draws static power through load transistors). Power consumption scales with switching frequency and capacitance only (P = fCV²). CMOS enabled billion-transistor chips that would be thermally impossible with NMOS alone.

**Gate oxide**: SiO₂ grown by thermal oxidation of silicon (dry O₂ at 900-1100°C or wet O₂/H₂O at 800-950°C). Thickness 5-50 nm depending on technology generation. Thinner oxide → stronger gate coupling → faster switching, but exponentially higher gate leakage current (quantum tunneling through oxide). Oxide quality is critical — even a single defect in the gate oxide can cause catastrophic breakdown (short circuit from gate to channel). Oxide integrity requires ultra-clean processing and careful handling.

**[Threshold voltage](../glossary/threshold-voltage.md)** (Vth): Minimum gate-to-source voltage required to induce a conductive channel. Typically 0.5-1.5V. Controlled by substrate doping concentration (higher doping → higher Vth), oxide thickness (thinner oxide → lower Vth), and gate electrode material. Matching Vth between NMOS and PMOS transistors is essential for symmetric CMOS switching characteristics. Process variations in threshold voltage are a major yield limiter.

**[Scaling](../glossary/scaling.md)** (Dennard scaling rules): Shrink all device dimensions (channel length, oxide thickness, junction depth) by factor k while scaling voltage by k. Result: transistors are k² times smaller (2× per generation → 4× more per chip), k times faster, and power density remains constant. This held from the 1970s to ~2006. Breakdown cause: as oxide thickness approached a few nm, gate leakage current from quantum tunneling became unacceptable. Voltage could no longer scale proportionally → power density increased → the "power wall." Modern scaling continues geometry reduction but requires architectural workarounds (finFETs, multi-core, dark silicon).

### Metallization & Contacts

**[Vacuum evaporation](../glossary/vacuum-evaporation.md)** (simplest deposition method):
- **Process**: Place metal source (Al, Au, Ti) in tungsten or molybdenum boat or basket in vacuum chamber. Pump to 10⁻⁵ to 10⁻⁶ Torr. Heat source resistively (current through boat) to metal's evaporation temperature (Al: 1200°C, Au: 1500°C). Metal vapor travels in straight lines to substrate. Deposit 0.1-2 μm film.
- **Rate monitoring**: Quartz crystal microbalance — crystal oscillation frequency decreases as metal deposits. Calibrated to thickness.
- **Uniformity**: Source-to-substrate distance 30-50 cm. Rotating planetary fixture for uniform thickness on multiple wafers.
- **Pattern definition**: Shadow mask (thin metal sheet with cutout pattern held against wafer during deposition) or lift-off (pattern photoresist before deposition, dissolve resist after — metal on resist lifts off, leaving patterned metal on wafer).

**[Screen printing](../glossary/screen-printing.md)** (for solar cell contacts):
- Print conductive paste (Ag, Al, or carbon) through mesh screen with patterned emulsion. Squeegee forces paste through open areas onto wafer. Dry and fire. Simpler than evaporation, lower resolution (~50 μm minimum line width).

**[Sputtering](../glossary/sputtering.md)** (later, more versatile):
- **Process**: Argon plasma bombards target material → atoms ejected → deposit on substrate. Works for any material (metals, insulators, alloys). Better step coverage than evaporation. Requires: RF or DC power supply, vacuum system, target material, argon gas.
- **DC sputtering**: Conductive targets only (metals). 200-1000V, 0.1-10 Torr Ar.
- **RF sputtering**: Any target material (including insulators). 13.56 MHz standard frequency.

### Semiconductor Device Physics

**P-N junction**:
- **Depletion region**: At the junction between p-type and n-type silicon, electrons diffuse from the n-side into the p-side and recombine with holes. This creates a region depleted of free carriers (the depletion region), leaving behind fixed ionized dopant atoms: negative acceptor ions on the p-side, positive donor ions on the n-side. The resulting electric field (built-in potential, Vbi ≈ 0.7V for silicon) opposes further diffusion.
- **Depletion width**: W = √(2εᵣε₀(Vbi - V)/(qN)), where εᵣ = 11.7 for silicon, ε₀ = 8.854×10⁻¹² F/m, q = 1.6×10⁻¹⁹ C, and N is the dopant concentration on the lightly-doped side. For a typical junction with N = 10¹⁶/cm³ and zero bias: W ≈ 0.3 μm. Under reverse bias, W increases as √V.
- **Forward bias I-V characteristic**: I = I₀(e^(qV/nkT) - 1), where I₀ is the reverse saturation current (typically 10⁻¹² to 10⁻⁹ A for small diodes), n is the ideality factor (1.0-2.0, where n=1 is ideal diffusion current and n=2 indicates recombination current), k is Boltzmann's constant (1.38×10⁻²³ J/K), and T is absolute temperature. At room temperature, kT/q ≈ 26 mV.
- **Reverse bias breakdown**: When reverse voltage exceeds a threshold, current increases dramatically. **[Avalanche breakdown](../glossary/avalanche-breakdown.md)** (dominant for breakdown voltages >7V): accelerated carriers collide with lattice atoms, ionizing them and creating more carriers (chain reaction). **[Zener breakdown](../glossary/zener-breakdown.md)** (dominant for breakdown voltages <5V): quantum mechanical tunneling of carriers through the narrow depletion region in heavily-doped junctions.

**Diode types**:
- **Rectifier diode**: General purpose. Forward voltage drop 0.6-0.7V (silicon). Reverse breakdown 50-2000V depending on design. Recovery time: fast (Schottky) to slow (standard rectifier). Used for AC-to-DC conversion, reverse polarity protection, signal clamping.
- **Zener diode**: Designed to operate in reverse breakdown. Breakdown voltage specified from 2.7V to 200V in standard values. Tolerance ±5% (tighter available). At breakdown, voltage remains nearly constant over a wide current range (dynamic impedance 1-100 Ω). Used for voltage regulation and reference. Requires series resistor to limit current: R = (Vin - Vz)/Iz.
- **Schottky diode**: Metal-semiconductor junction (not a p-n junction). Lower forward voltage drop (0.2-0.4V, depending on the metal). Faster switching (no minority carrier storage — majority carrier device). Higher reverse leakage current than silicon p-n diodes. Used in high-frequency rectifiers, power supply OR-ing, RF detectors.
- **LED (light-emitting diode)**: Forward-biased p-n junction where electron-hole recombination produces photons. Photon energy ≈ bandgap energy. GaAs: infrared (~870 nm). GaAsP: red (~630 nm). GaP: green (~555 nm). GaN: blue (~450 nm). External quantum efficiency: 1-30% depending on material and structure.

**Bipolar Junction Transistor (BJT) operation**:
- **Current gain**: β = Ic/Ib, typically 50-300 for small-signal transistors, 10-50 for power transistors. The base current controls a much larger collector current. Small changes in base current cause large changes in collector current, which is the amplification mechanism.
- **Operating regions**: **[Cutoff](../glossary/cutoff.md)** (base-emitter junction not forward biased: Ic ≈ 0). **[Active](../glossary/active.md)** (base-emitter forward biased, base-collector reverse biased: Ic = β·Ib, amplifier operation). **[Saturation](../glossary/saturation.md)** (both junctions forward biased: Vce ≈ 0.2V, switch "on" state). **[Reverse active](../glossary/reverse-active.md)** (junctions reversed, β very low, rarely used).
- **Bias circuits**: Operating point (quiescent point) set by base bias resistors. Fixed bias (single base resistor, β-dependent). Voltage divider bias (two resistors from Vcc to ground with base at junction, most stable against β variation). Emitter resistor provides negative feedback: if Ic increases → Ie increases → Ve increases → Vbe decreases → Ic decreases. Self-stabilizing.

**MOSFET device parameters**:
- **Gate oxide**: 5-100 nm thickness (5-10 nm for modern logic, 50-100 nm for power MOSFETs). Grown by thermal oxidation. Breakdown field ~10 MV/cm. A 10 nm oxide breaks down at ~10V. Oxide integrity is the single most critical fabrication parameter.
- **Threshold voltage (Vth)**: 0.5-2V for enhancement-mode. Vth = 2φF + (√(2εs·q·Na·(2φF)))/Cox, where φF is the Fermi potential, Na is substrate doping, and Cox is oxide capacitance per unit area. Vth increases with substrate doping and oxide thickness.
- **On-resistance (RDS(on))**: 0.01-10 Ω depending on device size and voltage rating. For power MOSFETs: RDS(on) × area ≈ constant for a given voltage rating. Higher voltage devices have higher specific on-resistance (more drift region to sustain voltage).
- **Gate charge (Qg)**: Total charge that must be supplied to the gate to turn the device fully on. Determines switching speed: ton ≈ Qg/Ig where Ig is the gate driver current. Typical values: 1-100 nC depending on device size. Gate charge is a key parameter for switching loss calculation: Pswitch = Qg × Vgs × f.

### Simple Circuit Building Blocks

**Full-wave bridge rectifier**: Four diodes in a bridge configuration. AC input across two opposite corners, DC output across the other two. Converts AC to pulsating DC. Output voltage = |Vac| - 2×Vd (two diode drops, ~1.4V for silicon). With a filter capacitor: Vdc ≈ Vpeak - 1.4V - (Iload)/(2·f·C). The capacitor smooths the pulsating DC; larger capacitance gives less ripple.

**Zener voltage regulator**: Zener diode in reverse bias with series resistor. Input voltage Vin through resistor R to Zener cathode. Zener maintains approximately constant voltage Vz across the load. Design: R = (Vin_min - Vz)/(Iz_min + Iload_max). Power dissipation in Zener: Pz = Vz × Iz. Must keep Pz below Zener's rated dissipation (typically 0.4-1.5W for small devices).

**Astable multivibrator**: Two transistors, two collector resistors, two base resistors, and two coupling capacitors. Each transistor alternately turns on and off. Frequency: f = 1/(1.4·R·C) where R is the base resistor and C is the coupling capacitor (symmetric circuit). Used as a simple clock oscillator. Output: square wave at the collector of either transistor. Duty cycle ~50% with equal R and C values.

### Safety Hazards

Semiconductor device fabrication uses some of the most dangerous chemicals in industrial processing:
- **Hydrofluoric acid (HF)**: Used at 5-10% concentration for phosphorus glass removal and oxide etching. HF penetrates skin painlessly, attacks deep tissue and bone, and causes systemic fluoride poisoning. A splash covering ~2.5% of body surface area (palm-sized) from 50% HF can be lethal; even 5-10% solutions cause serious burns. **Calcium gluconate gel (2.5%) must be on-site and accessible before any HF work begins.** Apply to exposed area immediately and seek emergency medical treatment — do not wait for pain. PPE: neoprene or thick nitrile gloves (double-gloving recommended), face shield, chemical splash apron, closed-toe shoes. Work in fume hood with local exhaust. Never store or handle HF in glass containers — use PTFE or polyethylene only.
- **POCl₃ (phosphorus oxychloride)**: Used for n-type emitter diffusion. Reacts violently with moisture in air, releasing HCl gas and phosphoric acid mist. Toxic by inhalation — causes severe respiratory burns and pulmonary edema. Handle in sealed gas delivery system with nitrogen purge. Leak detection: HCl monitor in furnace area. PPE: full-face respirator with acid gas cartridge for cylinder changes, chemical splash suit.
- **NaOH / KOH (caustic etchants)**: 20-40% solutions at 80°C for saw-damage removal and texturing. Causes deep caustic burns on skin and permanent eye damage. Heat increases severity. PPE: chemical splash goggles (not just safety glasses), nitrile gloves, apron. Eye wash station within 10 seconds travel. If splashed in eyes, flush with water for 15+ minutes immediately.
- **Belt furnace burn hazard**: Metal contacts are fired at 700-800°C on a moving belt. Exposed hot surfaces, infrared radiation. Thermal gloves and face shield for loading/unloading. Belt pinch points — keep hands clear of moving belt edges.
- **Vacuum chamber implosion**: Evaporation and sputtering chambers are evacuated to 10⁻⁵-10⁻⁶ Torr. A flawed glass viewport or corroded chamber wall can implode violently. Inspect viewports for scratches or star cracks before each pump-down. Safety glasses at all times near evacuated chambers. Never exceed rated pressure differential.

### Process Integration for Simple Devices

**Rectifier diode fabrication flow** (simplest discrete device):
1. **Starting wafer**: n-type <111> silicon, 5-20 Ω·cm, 300-500 μm thick.
2. **Boron diffusion**: Spin boron dopant source (BBr₃ in N₂ carrier) onto wafer surface. Load in diffusion furnace at 1000-1100°C for 30-120 minutes. Drive-in at 1100°C for 30-60 minutes to deepen junction. Result: p-type layer ~1-5 μm deep on one surface, forming p-n junction.
3. **Oxide removal**: Strip the boron glass (SiO₂-B₂O₃) in dilute HF (5%, 30-60 seconds).
4. **Back side etch**: Remove p-type layer from the back side using wax masking (paint wax on the front, etch back with HF:HNO₃ mixture).
5. **Metallization**: Evaporate aluminum on both sides (1-2 μm front, 2-5 μm back). Front contact: small dot or ring pattern defined by shadow mask. Back contact: full area.
6. **Alloy**: Heat to 450°C for 15 minutes in forming gas (N₂/H₂). Aluminum alloys with silicon at the contact, forming a low-resistance ohmic contact.
7. **Scribe and break**: Separate individual diodes from the wafer by diamond scribing and snapping. Typical die size: 1×1 mm to 5×5 mm depending on current rating.
8. **Package**: Solder die into metal-glass or plastic package. Wire bond from package lead to front contact. Seal.

**Solar cell process optimization**:
- **Gettering**: Phosphorus diffusion for the n+ emitter also acts as a gettering step (phosphorus atoms in the near-surface region attract and trap metallic impurities from the bulk silicon). This improves minority carrier lifetime in the base, increasing open-circuit voltage. Process: extend the POCl₃ pre-deposition time by 10-15 minutes beyond what is needed for junction depth alone.
- **Surface passivation**: The SiNₓ anti-reflection coating deposited by PECVD also provides surface passivation. Hydrogen atoms in the SiNₓ film diffuse to the silicon surface during the firing step, terminating dangling bonds that would otherwise act as recombination centers. This passivation is critical for achieving >16% efficiency.
- **Firing optimization**: The rapid thermal processing (belt furnace, 700-800°C peak, ~30 seconds) serves three purposes simultaneously: (1) Ag paste etches through SiNₓ to contact the n+ emitter, (2) Al alloys with silicon to form the p+ back surface field, and (3) hydrogen from SiNₓ passivates surface and bulk defects. Temperature must be precisely controlled: too low → poor contact, too high → junction degradation.

### Device Testing

**I-V characterization**:
- **Diode testing**: Measure forward voltage at a specified current (e.g., Vf at 1 mA, 10 mA, 100 mA). Normal silicon diode: Vf ≈ 0.6-0.7V at 1 mA. Higher Vf indicates poor contact or high series resistance. Measure reverse leakage at rated voltage (e.g., leakage at 50V). Good rectifier diode: leakage <1 μA at rated voltage.
- **Solar cell I-V curve**: Illuminate cell with standard solar spectrum (AM1.5, 1000 W/m²). Measure open-circuit voltage (Voc), short-circuit current (Isc), and maximum power point (Pmax). Fill factor FF = Pmax/(Voc × Isc). Efficiency η = Pmax/(incident power × cell area). A good 156×156 mm cell: Voc ~0.62V, Isc ~9A, FF ~0.78, η ~17%.

**Transistor testing**:
- **BJT gain measurement**: Apply known base current (e.g., 10 μA), measure collector current. β = Ic/Ib. Test at multiple base currents (1 μA to 10 mA) to characterize gain variation. Plot gain vs. collector current (gain peaks at intermediate current, falls at both extremes).
- **MOSFET threshold voltage**: Apply gate voltage sweep from 0 to 5V with drain at 0.1V. Plot Id vs. Vg. Threshold voltage Vth = gate voltage where drain current reaches a specified value (e.g., 1 μA × W/L). Check that Vth is within specification (typically 0.5-2V for enhancement mode).

### Reliability and Failure Modes

**Common failure mechanisms for semiconductor devices**:
- **Electrostatic discharge (ESD)**: A static discharge as low as 50-100V can puncture the thin gate oxide of a MOSFET, creating a short circuit from gate to channel. Even non-catastrophic ESD events degrade oxide integrity, leading to premature failure weeks or months later. Prevention: grounded wrist straps, conductive flooring, ionizers, ESD-safe packaging (conductive foam or bags).
- **Electromigration**: High current density in metal interconnect lines causes metal atoms to migrate in the direction of electron flow. Over time, this thins the conductor until it opens (open circuit) or forms a hillock that shorts to an adjacent line. MTTF ∝ J⁻² × exp(Ea/kT), where J is current density and Ea is activation energy (~0.5-0.7 eV for Al). Design rule: keep current density below 1 mA/μm² for aluminum interconnects.
- **Hot carrier injection**: High electric fields near the drain end of short-channel MOSFETs accelerate electrons to high energy. These "hot carriers" can be injected into the gate oxide, causing threshold voltage shift and transconductance degradation over time. Worse at higher drain voltages and lower temperatures. Mitigated by lightly-doped drain (LDD) structures that reduce the peak electric field.
- **Oxide breakdown**: Gate oxide fails when the electric field exceeds the breakdown strength (~10 MV/cm for SiO₂). Time-dependent dielectric breakdown (TDDB) occurs at fields well below the instantaneous breakdown threshold: defects in the oxide accumulate charge over time until a conductive path forms through the oxide. Accelerated by voltage stress and temperature.

**Simple device qualification tests**:
- **Temperature cycling**: Cycle devices between -40°C and +125°C (or wider range) for 100-1000 cycles. Checks for thermal expansion mismatch failures (wire bond lifting, die attach cracking, package delamination).
- **Burn-in**: Operate devices at elevated temperature (125-150°C) and maximum rated voltage for 24-168 hours. Weeds out "infant mortality" failures (devices with latent defects that fail early in life). The bathtub curve: high failure rate in the first few hundred hours (infant mortality), low constant rate during operational life, rising rate at end of life (wearout).
- **High temperature operating life (HTOL)**: Operate at maximum rated temperature and voltage for 1000 hours. Measures long-term reliability and extracts failure rate data for lifetime predictions.

### Device Packaging

**Discrete device packages**:
- **DO-41 (axial lead)**: Glass-sealed cylindrical package for small-signal and rectifier diodes. Glass body (2-4 mm diameter, 4-6 mm long) with axial metal leads (copper or steel, 0.5-0.8 mm diameter). Glass-to-metal seal hermetically seals the die. Rated to 500V-1000V, 1A average forward current. The simplest and cheapest diode package. Color band on cathode end indicates polarity.
- **TO-220 (through-hole, power)**: Plastic-molded package (10×15×5 mm) with a metal tab for heat sink mounting. Three leads (for transistors) or two leads (for diodes). Rated for 1-50A, up to 1000V. The metal tab is electrically connected to the device (collector for BJT, drain for MOSFET, cathode for diode) — requires electrical insulation (mica washer or thermal pad) when mounting to a grounded heat sink.
- **TO-92 (through-hole, small signal)**: Plastic-molded package (3×5 mm body, 3 leads). For low-power transistors and sensors. Rated to 350 mW dissipation, 200 mA collector current. Inexpensive and widely used for small-signal applications.

**Wire bonding**:
- **Purpose**: Electrically connect the silicon die to the package leads with fine wire (25 μm gold or 25-50 μm aluminum).
- **[Ball bonding](../glossary/ball-bonding.md)** (gold wire): Flame-off creates a small ball at the wire tip. Thermosonic bonding (heat + ultrasonic vibration + pressure) attaches the ball to the aluminum bond pad on the die. Wire is looped to the package lead, where a second bond (wedge) is made. Ball bonding is the dominant method for ICs and most discrete devices.
- **[Wedge bonding](../glossary/wedge-bonding.md)** (aluminum wire): Ultrasonic energy and pressure form a wedge bond at both die and lead. No heat required (can be done at room temperature). Used for power devices (thicker aluminum wire, 100-500 μm, carries higher current) and for devices sensitive to gold contamination.

**Die attach**:
- **Solder attach**: Eutectic solder (Au-Si at 363°C, or soft solder Sn-Pb at 183°C) bonds the die to the package header or lead frame. Good thermal and electrical conductivity. The die back side is metallized (Ti/Ni/Ag or Ti/Pd/Au) for solder wetting.
- **Epoxy attach**: Conductive epoxy (silver-filled) or non-conductive epoxy bonds the die at lower temperature (150°C cure). Simpler process, lower cost. Used for plastic packages where hermeticity is not required.

**Hermetic vs. non-hermetic packages**:
- **Hermetic (metal or ceramic)**: Metal can (TO-3, TO-5, TO-99) with glass-to-metal seal feedthroughs, or ceramic dual-in-line package (CERDIP) with glass-sealed lid. Gas-tight seal protects the die from moisture and contaminants. Required for military, aerospace, and high-reliability applications. Leak tested with helium mass spectrometer (reject rate >10⁻⁸ atm·cc/s). Shelf life: unlimited in dry storage.
- **Non-hermetic (plastic)**: Epoxy or silicone resin molded around the die and lead frame (transfer molding at 175°C, 5-10 MPa). Lower cost (10-100× cheaper than ceramic). Moisture can penetrate plastic over time (absorption rate ~0.1-1% by weight at 85°C/85% RH). Moisture inside the package causes corrosion of aluminum bond wires and die metallization, especially during solder reflow (popcorn cracking: absorbed moisture vaporizes explosively during reflow heating, cracking the package). Mitigated by: moisture barrier bags for storage, bake-out before soldering, and moisture-absorbing die attach materials.

### Semiconductor Process Flow Summary

**Solar cell process flow** (simplest useful semiconductor device):
1. Wafer incoming inspection (resistivity, thickness, TTV, particles)
2. Saw damage etch (NaOH 20%, 80°C, 5 min)
3. Texturing (KOH/IPA, 75°C, 25 min)
4. Phosphorus diffusion (POCl₃, 850°C, 30 min)
5. PSG removal (HF 5%, 60 sec)
6. SiNₓ AR coating (PECVD, 350°C)
7. Front contact print (Ag paste, screen print)
8. Rear contact print (Al paste, screen print)
9. Co-firing (belt furnace, 780°C peak, 30 sec)
10. Edge isolation (laser scribe or plasma etch)
11. I-V testing and sorting

**Typical yield**: First runs 30-50%, improving to 80-95% with process optimization. Key yield limiters: contamination (particles on wafer surface kill cells), uniformity (non-uniform diffusion creates shunts), and mechanical breakage (thin wafers are fragile). Each step requires process control and monitoring to maintain yield. For integrated circuits, typical IC yield at the 180nm node runs 80-90% for simple logic and 50-70% for large SoC designs. Yield follows the Poisson model: yield = (1-D×A)^N, where D is defect density (defects/cm² per masking level), A is chip area (cm²), and N is the number of masking levels. Cost per good die = wafer cost / (dies per wafer × yield), which means yield improvement has a direct, multiplied impact on cost.

**Solar cell parameter relationships**:
- **Efficiency**: η = (Voc × Jsc × FF) / Pin, where Voc is open-circuit voltage (V), Jsc is short-circuit current density (mA/cm²), FF is fill factor (dimensionless, 0.7-0.85), and Pin is incident power density (100 mW/cm² at AM1.5).
- **Voc**: Typically 0.55-0.72V for crystalline silicon. Increases with: higher base resistivity (lower doping → less Auger recombination), better surface passivation, and lower temperature (Voc decreases ~2.2 mV/°C).
- **Jsc**: Typically 30-42 mA/cm² for crystalline silicon. Increases with: better light trapping (texturing, anti-reflection coating), higher minority carrier lifetime in the base, and thinner metal grid lines (less shading).
- **Temperature sensitivity**: Solar cell efficiency decreases ~0.3-0.5% per °C above 25°C. A module at 60°C produces ~10-15% less power than at 25°C. This is a fundamental semiconductor property (increased temperature increases dark current, reducing Voc).

**Device parameter comparison**:

| Parameter | Rectifier diode | Zener diode | BJT (small signal) | MOSFET (logic) | Solar cell |
|---|---|---|---|---|---|
| Forward voltage | 0.6-0.7V | N/A (reverse) | Vce(sat) ~0.2V | RDS(on) × Id | N/A |
| Breakdown voltage | 50-2000V | 2.7-200V | BVceo 20-80V | 10-20V (logic) | N/A |
| Speed (tr/tf) | 1-50 μs | N/A | 10-100 ns | 1-10 ns | N/A |
| Current range | 0.1-50A | 5-1000 mA | 1 mA-1A | 1 μA-50A | 0-9A (156mm cell) |
| Key metric | Vf at rated I | Vz tolerance | β (50-300) | Vth (0.5-2V) | η (15-18%) |

### Circuit Design Examples

#### Rectifier Bridge

Four diodes arranged in a bridge convert AC to DC. During the positive half-cycle of the AC input, two diagonally opposite diodes conduct. During the negative half-cycle, the other two conduct. Current through the load flows in the same direction in both half-cycles.

- **Voltage drop**: 2× Vf ≈ 1.4V for silicon diodes (two diodes conduct in series during each half-cycle). For a 12V AC input, the DC output is Vpeak - 1.4V = 17V - 1.4V ≈ 15.6V after peak rectification.
- **PIV rating**: Each diode must withstand a peak inverse voltage equal to the peak AC input voltage. In practice, select diodes rated for 2× peak input voltage to handle line transients and voltage spikes safely.
- **Filter capacitor**: Add a reservoir capacitor across the DC output to smooth the 120 Hz (or 100 Hz) ripple. Size: C ≥ Iload/(2·f·ΔV), where ΔV is the allowable ripple voltage. For 1A load and 2V ripple at 60 Hz: C ≥ 1/(2·60·2) = 4,200 μF. Use a 4,700 μF/25V electrolytic capacitor.
- **Ripple current**: The capacitor carries large AC ripple current (2-3× DC load current). Select capacitors rated for the ripple current at the operating temperature. Overheated capacitors vent electrolyte and fail.

#### Voltage Regulator (Zener Shunt)

A Zener diode in reverse breakdown maintains a nearly constant voltage across the load. A series resistor drops the excess voltage.

- **Series resistor**: R = (Vin - Vz) / (Iz + Iload). Choose Iz to be at least 5-10 mA to keep the Zener in its regulation region. For Vin = 12V, Vz = 5.1V, Iload = 20 mA, Iz = 10 mA: R = (12 - 5.1)/(0.03) = 230 Ω. Use 220 Ω standard value.
- **Power dissipation**: In the Zener: Pz = Vz × Iz = 5.1 × 0.03 = 0.153W. In the resistor: Pr = (Vin - Vz) × Itotal = 6.9 × 0.03 = 0.207W. Use at least 0.5W rated components.
- **Regulation quality**: Output voltage varies with load current because the Zener dynamic impedance (typically 5-50 Ω) forms a voltage divider with the series resistor. For better regulation, use a series pass transistor (emitter follower driven by the Zener) to amplify the Zener's current capability.

#### LED Driver

An LED is a current-driven device. A series resistor sets the operating current.

- **Series resistor**: R = (Vs - Vf) / If, where Vs is the supply voltage, Vf is the LED forward voltage, and If is the desired forward current.
- **Forward voltages by color**: Red GaAsP: 1.8-2.2V. Green GaP: 2.0-2.4V. Blue/white GaN: 3.0-3.6V. Infrared GaAs: 1.2-1.5V.
- **Typical operating current**: 10-20 mA for standard indicator LEDs. 350-700 mA for high-power illumination LEDs. 1-5 mA sufficient for low-brightness indicators.
- **Example**: Blue LED (Vf = 3.2V) from 5V supply at 15 mA: R = (5 - 3.2)/0.015 = 120 Ω. Power in resistor: P = I²R = 0.015² × 120 = 0.027W. A 0.125W (1/8W) resistor is adequate.

#### Transistor Switch

A BJT used as a switch operates in cutoff (off) or saturation (on). The base resistor must supply enough base current to drive the transistor into saturation under worst-case conditions.

- **Base resistor**: Rb = (Vin - 0.7) / Ib, where 0.7V is the base-emitter forward voltage drop and Ib = Ic / β. Use the minimum β from the datasheet (βmin) to ensure saturation even with the lowest-gain transistor.
- **Saturation requirement**: βforced = Ic / Ib must be less than βmin (typically βforced of 10-20 ensures hard saturation). At saturation, Vce ≈ 0.1-0.3V (not zero). This residual voltage is the saturation voltage, Vce(sat).
- **Example**: Switch a 500 mA load from a 5V logic signal using a transistor with βmin = 50. Ib = 500/50 = 10 mA. Rb = (5 - 0.7)/0.01 = 430 Ω. Use 390 Ω standard value for extra margin.

#### Oscillator Circuits

**Astable multivibrator**: Two cross-coupled transistor switches that alternate on/off. Each collector drives the opposite base through an RC network. Frequency: f = 1/(1.4 × R × C) for a symmetric circuit (R = base resistor, C = coupling capacitor). Duty cycle ≈ 50% with matched components. Output: square wave, amplitude ≈ Vcc. Frequency stability: poor (±20% with temperature), but sufficient for blinking LEDs, clock generation for simple digital circuits, and tone generation.

**Colpitts oscillator**: Single transistor with capacitive voltage divider feedback. Two capacitors in series form the resonant circuit with an inductor. Oscillation frequency: f = 1/(2π√(L·Cseries)), where Cseries = C1·C2/(C1+C2). Feedback ratio: C1/C2 sets the loop gain. Typical values: C1 = C2 = 100 pF, L = 10 μH → f ≈ 7 MHz. Used for RF oscillators and local oscillators in radio receivers.

**Crystal oscillator**: A quartz crystal resonator replaces the LC tank. The crystal's piezoelectric resonance provides extremely high Q (10,000-100,000), giving frequency stability of ±0.01% (100 ppm) over temperature. Basic Pierce circuit: one inverting amplifier (transistor or logic gate), two load capacitors (10-30 pF each), and the crystal. Frequency range: 32.768 kHz (real-time clocks) to 50 MHz (microcontroller clocks). The crystal oscillator is the timing backbone of every digital system.

#### Operational Amplifier Basics

The op-amp is a high-gain differential amplifier with two inputs (inverting -, non-inverting +) and one output. Negative feedback trades open-loop gain (100,000-1,000,000×) for predictable, stable closed-loop gain set by external resistors.

- **Inverting amplifier**: Output = -(Rf/Rin) × Vin. Input impedance = Rin. Signal is inverted (180° phase shift). Gain accuracy depends only on resistor ratio, not the op-amp's internal gain. Example: Rf = 100 kΩ, Rin = 10 kΩ → gain = -10.
- **Non-inverting amplifier**: Output = (1 + Rf/Rin) × Vin. Input impedance >1 MΩ (depends on op-amp input stage, >10¹² Ω for FET-input op-amps). No phase inversion. Minimum gain = 1 (voltage follower: Rf = 0, Rin = ∞). The voltage follower buffers high-impedance sources without loading them.
- **Practical limits**: Input offset voltage (1-5 mV for general-purpose op-amps like LM741) adds a DC error. Input bias current (100 nA for bipolar, 1 pA for FET-input) flows through input resistors, creating additional offset. Bandwidth: 1-10 MHz gain-bandwidth product for general-purpose parts. At gain = 100, bandwidth = GBW/100 = 10-100 kHz.
- **Output drive**: Output impedance <100 Ω at DC (with feedback), rising at higher frequencies. Maximum output current: 20-40 mA for general-purpose op-amps. Output voltage swing: within 1-2V of the supply rails (0-5V swing from ±15V supplies). Rail-to-rail output op-amps swing to within millivolts of the supply rails.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Silicon](./index.md) • [All Domains](../index.md)*
