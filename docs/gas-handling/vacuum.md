# Vacuum Technology

> **Node ID**: gas-handling.vacuum
> **Domain**: [Gas Handling](./index.md)
> **Dependencies**: None (root capability)
> **Enables**: [`metals.specialty-semiconductor`](../metals/specialty-semiconductor.md), [`optics.inspection.optical-coatings`](../optics/optical-coatings.md), [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`silicon.basic-devices`](../silicon/basic-devices.md)
> **Timeline**: Years 25-40
> **Outputs**: vacuum_pumps, vacuum_chambers, vacuum_measurement, leak_detection
> **Critical**: Yes — vacuum technology is required for semiconductor thin-film deposition, lithography, and packaging; no alternative exists

### Vacuum Technology

**[Mechanical pumps](../glossary/mechanical-pumps.md)** (foundation of all vacuum work):

**[Piston pump](../glossary/piston-pump.md)** (simplest, lower vacuum):
- **Construction**: Cast iron cylinder, machined piston with leather cup seal, inlet and outlet check valves (leather or steel flappers). Driven by crank from motor or hand wheel.
- **Performance**: ~10-100 L/min pumping speed. Ultimate vacuum ~10-50 Torr (rough vacuum).
- **Applications**: Initial roughing pump, gas transfer, compression.

**Strengths:**
- Simple construction: cast iron cylinder, leather seals, no precision components — can be built with basic machining capability
- Tolerates dirty and wet gas streams; leather seals are forgiving of particulate contamination
- Low cost: no precision bearings, no oil filtration system, minimal maintenance

**Weaknesses:**
- Limited ultimate vacuum (~10-50 Torr) — insufficient for any thin-film process
- Low pumping speed (10-100 L/min) compared to rotary vane pumps of similar size
- Leather seals wear and require periodic replacement (every 500-2000 hours depending on service)

**[Rotary vane pump](../glossary/rotary-vane-pump.md)** (workhorse — achieves medium vacuum):
- **Principle**: Eccentric rotor in cylindrical stator. Spring-loaded vanes slide in rotor slots, maintaining contact with stator wall. Gas enters inlet port, trapped between vanes and stator, compressed, expelled through exhaust valve.
- **Construction**: Cast iron stator (bored to ~0.01 mm tolerance on Machine Tools lathe/boring machine). Steel rotor. Steel or carbon fiber vanes. Oil-filled for sealing and lubrication (oil seals microscopic gaps between vanes and stator).
- **Oil requirements**: Low vapor pressure vacuum oil (see [Lubricants](../chemistry/lubricants.md)). Mineral oil with low volatility, or silicone oil. Oil changed regularly — contaminated oil limits ultimate vacuum.
- **Performance**: 1-50 L/min (small), 50-500 L/min (medium). Ultimate vacuum: ~10⁻² to 10⁻³ Torr (0.01-0.001 Pa). Single-stage: ~10⁻² Torr. Two-stage: ~10⁻³ Torr.
- **Gas ballast**: Small valve admits air during compression phase to prevent condensation of vapors (water, solvents) in pump oil. Essential when pumping wet systems.

**Strengths:**
- Achieves 10⁻² to 10⁻³ Torr (medium vacuum) in a compact, oil-sealed package — sufficient backing for diffusion and turbomolecular pumps
- Gas ballast prevents vapor condensation in pump oil, extending oil life when pumping wet systems

**Weaknesses:**
- Oil-sealed design introduces backstreaming risk — hot oil vapor migrates toward the vacuum chamber, contaminating sensitive surfaces
- Oil changes required every 3-6 months; contaminated oil limits ultimate vacuum and produces objectionable odor

**[Diffusion pump](../glossary/diffusion-pump.md)** (high vacuum, no moving parts):
- **Principle**: Boiler heats silicone or hydrocarbon oil → vapor jets shoot downward → gas molecules from vacuum chamber diffuse into vapor stream → carried to exhaust → removed by backing pump. No moving parts, very reliable.
- **Backing pump requirement**: Diffusion pump requires a mechanical backing pump (rotary vane) to maintain foreline pressure below ~0.5 Torr. Without backing, diffusion pump stalls and oil backstreams into chamber.
- **Performance**: Pumping speed 50-10,000 L/s. Ultimate vacuum: ~10⁻⁶ to 10⁻⁸ Torr with proper trapping and baking.
- **Oil**: Silicone oil (DC-704, DC-705) or Santovac (polyphenyl ether). Low vapor pressure, high thermal stability. Oil heated to ~150-200°C in boiler.
- **Cold trap**: Liquid nitrogen cooled baffle between diffusion pump and chamber. Condenses backstreaming oil vapor. Essential for clean vacuum. LN₂ from the Chemistry stage air liquefaction.

**Vacuum chambers**:
- **Materials**: Steel or stainless steel (welded construction, all seams seal-welded). Aluminum (lighter, easier to machine, but more porous to He). Glass bell jars (for small systems — visual observation).
- **Design**: Cylindrical or spherical (uniform stress distribution). Viewports (glass windows with CF or ISO flanges). Multiple ports for feedthroughs (electrical, mechanical, gas).
- **Surface preparation**: Electropolish stainless steel internal surfaces (smooth surface = less outgassing). Clean with acetone, then alcohol, then bake.

**Vacuum measurement**:
- **Rough vacuum (760-1 Torr)**: Bourdon tube gauge (mechanical). U-tube manometer (oil or mercury — measures pressure difference directly).
- **Medium vacuum (1-10⁻³ Torr)**: Thermocouple gauge or Pirani gauge (heated wire — thermal conductivity of gas depends on pressure). Inexpensive, reliable.
- **High vacuum (10⁻³-10⁻⁸ Torr)**: Penning ionization gauge (cold cathode ionizes gas, ion current proportional to pressure). Bayard-Alpert ion gauge (hot cathode version, more accurate). Calibration against McLeod gauge (absolute pressure measurement using compressed gas column — primary standard).

**Leak detection**:
- **Bubble test**: Pressurize system, spray soap solution on exterior, watch for bubbles. Finds large leaks.
- **Helium leak detector**: Mass spectrometer tuned to He. Spray He on exterior, detect He entering vacuum system. Sensitivity ~10⁻¹² atm·cc/s. The gold standard.
- **Tesla coil**: High-frequency spark probe. Spark penetrates small holes in glass apparatus (visible discharge inside). Glass systems only.

### Vacuum System Design

**[Two-stage pump system](../glossary/two-stage-pump-system.md)** (standard for high vacuum):
- **[Roughing pump](../glossary/roughing-pump.md)** (rotary vane or diaphragm): Pulls system from atmospheric pressure (~10⁵ Pa) down to ~0.1-1 Pa. This is the "rough vacuum" phase. The roughing pump handles the bulk of the gas load — most of the air molecules are removed in this stage.
- **[High-vacuum pump](../glossary/high-vacuum-pump.md)** (turbomolecular or diffusion pump): Takes over at the **[crossover pressure](../glossary/crossover-pressure.md)** (~1 Pa, or ~10⁻² Torr). Below this pressure, molecular flow dominates and the high-vacuum pump becomes effective. Crossover too early → gas load overloads the high-vacuum pump. Crossover too late → wastes time and risks oil backstreaming from roughing pump.
- **Pump-down sequence**: Open roughing valve, close high-vacuum valve. Rough to ~1 Pa. Close roughing valve, open high-vacuum valve. Continue pumping to target base pressure (10⁻⁴ to 10⁻⁶ Pa for most semiconductor processes).
- **Turbomolecular pump vs. diffusion pump**: Turbo pump — fast startup (1-3 min), clean (no oil vapor), expensive to build (precision rotor at 30,000-90,000 RPM). Diffusion pump — slower startup (15-30 min), requires cold trap to prevent oil backstreaming, simpler construction, lower cost.

### Outgassing Rates by Material

Every surface in a vacuum system releases adsorbed gas molecules — this is outgassing, and it dominates pump-down time below ~1 Pa.

| Material | Outgassing Rate (Pa·m³/s·m²) | Conditions |
|----------|-------------------------------|------------|
| **[Stainless steel](../glossary/stainless-steel.md)** (electropolished) | ~10⁻⁸ after bake | Standard for vacuum chambers. Improves 10-100× with bake-out. |
| **[Stainless steel](../glossary/stainless-steel.md)** (unbaked) | ~10⁻⁶ | Freshly manufactured, exposed to air. Mainly H₂O desorption. |
| **[Viton](../glossary/viton.md)** (unbaked) | ~10⁻⁶ | Elastomer O-ring seals. Major gas source. Bake reduces by 10-100×. |
| **[Viton](../glossary/viton.md)** (baked) | ~10⁻⁷ to 10⁻⁸ | After 24h at 150°C. Still higher than metal. |
| **[Copper](../glossary/copper.md)** (OFHC, baked) | ~10⁻⁹ | Lowest outgassing of practical materials. Used for CF flange gaskets. |
| **[PTFE](../glossary/ptfe.md)** | ~10⁻⁶ | Good chemical resistance but high outgassing. Avoid in UHV. |
| **[Aluminum](../metals/aluminum.md)** (baked) | ~10⁻⁹ | Good if surface oxide is controlled. Porous to He — problematic for leak detection. |

Design rule: minimize internal surface area, avoid elastomers where possible, bake if target pressure is below 10⁻⁵ Pa.

### Bake-Out Procedures

- **Purpose**: Accelerate desorption of water vapor, dissolved gases, and volatile contaminants from vacuum chamber walls. A system that takes 2 weeks to reach 10⁻⁶ Pa without bake-out can reach it in 24-48 hours with bake-out.
- **Temperature**: 150-300°C depending on chamber materials and seals. Stainless steel chambers with copper CF gaskets: 250-300°C. Viton-sealed chambers: 150°C maximum (Viton degrades above 200°C). Glass systems: 200-300°C.
- **Duration**: 24-48 hours at temperature while continuously pumping. Longer bake for lower target pressures.
- **Method**: Wrap chamber with heating tape (nichrome or silicone rubber insulated) or use custom-fitted band heaters. Cover with aluminum foil or fiberglass insulation to maintain uniform temperature. Monitor with thermocouples taped to multiple points on the chamber surface (top, bottom, side, ports). Avoid hot spots — local overheating warps flanges and ruins sealing surfaces.
- **Cool-down**: After bake, turn off heaters. Allow system to cool naturally while still under vacuum. Do not vent until below 50°C — rapid cooling with air exposure re-adsorbs moisture, undoing much of the bake-out benefit.

### Additional Vacuum Pump Types

**[Diaphragm pump](../glossary/diaphragm-pump.md)** (oil-free roughing):
- **Principle**: Flexible PTFE or elastomer diaphragm oscillates in a chamber, drawing gas in through an inlet valve and expelling it through an outlet valve. The diaphragm separates the drive mechanism from the gas stream, so no oil contacts the gas.
- **Performance**: Ultimate vacuum 1-10 mbar. Pumping speed 0.5-50 L/min. Not capable of reaching high vacuum on its own, but serves as a clean backing pump for turbomolecular pumps in applications where oil contamination is unacceptable (surface analysis, mass spectrometry, semiconductor processing).
- **Advantages**: Oil-free (no backstreaming, no oil changes), chemically resistant with PTFE heads (can pump corrosive vapors), low maintenance (diaphragm replacement every 5,000-10,000 hours). Disadvantages: limited ultimate vacuum, lower pumping speed than comparable rotary vane pumps.

**[Scroll pump](../glossary/scroll-pump.md)** (oil-free, medium vacuum):
- **Principle**: Two interleaving spiral scrolls — one fixed, one orbiting. The orbiting motion creates crescent-shaped gas pockets that progressively decrease in volume, compressing gas from inlet to outlet. No sliding contacts, no oil seal.
- **Performance**: Ultimate vacuum ~10⁻² mbar. Pumping speed 5-60 m³/h. Noise level 50-65 dB (quieter than rotary vane).
- **Advantages**: Oil-free, low vibration, low maintenance (only scroll tip seals wear). Used as backing pump for small turbomolecular pumps, and for applications requiring clean rough vacuum (freeze drying, degassing, solvent evaporation).

**[Turbomolecular pump](../glossary/turbomolecular-pump.md)** (high/ultra-high vacuum):
- **Principle**: Rotor with multiple angled blade stacks spins at 20,000-90,000 RPM. Gas molecules hitting the spinning blades receive a momentum kick in the exhaust direction. Each blade stage provides a small compression ratio; 5-40 stages achieve compression ratios of 10⁸-10¹² for N₂. Compression ratio depends on molecular weight: heavy gases (oil vapors) are pumped much more effectively than light gases (H₂, He). This is why a backing pump is required to handle light gas molecules that pass through the turbo pump relatively unaffected.
- **Backing pump requirement**: Rotary vane, diaphragm, or scroll pump maintains foreline pressure below 0.1-1 mbar. Without backing, the turbo pump cannot establish a pressure gradient and stalls.
- **Performance**: 10⁻³ to 10⁻¹⁰ mbar (with appropriate backing and baking). Pumping speed 50-5,000 L/s. Compression ratio for N₂: >10⁹; for H₂: ~10³-10⁵ (light gases are the hardest to pump).
- **Advantages**: Clean (no oil vapor), fast startup (1-3 minutes to full speed), no backstreaming. Disadvantages: Precision rotor at extreme RPM requires high-quality bearings (ceramic ball bearings or magnetic levitation), expensive to manufacture, vulnerable to mechanical shock and sudden pressure bursts (vents the system slowly).

### Vacuum Measurement in Detail

**Rough vacuum gauges**:
- **Bourdon tube gauge**: Curved hollow metal tube connected to vacuum system. External atmospheric pressure vs. internal pressure difference deflects the tube, moving a needle on a dial. Range: 1000-1 mbar. Simple, rugged, requires no power. Accuracy ±2-5% of full scale. Cannot measure below ~1 mbar. Useful for monitoring roughing pump performance.

**Medium vacuum gauges**:
- **Pirani gauge**: Heated wire element (tungsten or platinum) in the vacuum system. Gas molecules conduct heat away from the wire. At higher pressure, more molecules collide with the wire, cooling it (lower resistance). At lower pressure, fewer collisions, wire stays hotter (higher resistance). A Wheatstone bridge circuit measures resistance change and converts to pressure reading. Range: 1-10⁻³ mbar. Gas-type dependent (thermal conductivity varies with gas molecular weight — calibration is typically for N₂ or air; read differently for He, Ar, H₂).
- **Thermocouple gauge**: Similar principle to Pirani but uses a thermocouple welded to a heated filament to directly measure filament temperature. Range: 5-10⁻³ mbar. Less accurate than Pirani but simpler and more robust.

**High and ultra-high vacuum gauges**:
- **Penning cold cathode gauge**: High voltage (2-5 kV) applied between cathode and anode in a magnetic field. Electrons spiral in the magnetic field, ionizing gas molecules. Ion current is proportional to gas density (pressure). Range: 10⁻³-10⁻⁷ mbar. Robust (no hot filament to burn out). Cannot be used above 10⁻² mbar (arcing). Ignition delay at very low pressures (may read zero briefly until discharge starts).
- **Bayard-Alpert hot cathode ion gauge**: Heated filament emits electrons (typically at 30-100 mA emission current). Electrons accelerated toward a grid, ionizing gas molecules. Ions collected on a thin central wire (collector). Ion current proportional to pressure. Range: 10⁻³-10⁻¹¹ mbar. Most accurate and widest-range vacuum gauge. Filament can burn out (replaceable tubes). Do not operate above 10⁻³ mbar (filament oxidizes and fails rapidly).

### Vacuum System Design Principles

**Outgassing and bake-out**:
- Every surface in a vacuum system releases adsorbed gas molecules (primarily water vapor, also CO, CO₂, H₂). This outgassing dominates pump-down time below ~1 Pa. The rate decreases over time as the most loosely bound molecules desorb first.
- **Bake-out procedure**: Heat the entire vacuum system to 150-400°C while pumping continuously. This accelerates desorption by orders of magnitude. A system that takes 2 weeks to reach 10⁻⁶ Pa without bake-out reaches it in 24-48 hours with bake-out. Stainless steel chambers with copper CF gaskets tolerate the highest bake temperatures (300-400°C). Viton-sealed systems limited to 150°C.
- **Material selection**: Stainless steel (304L or 316L, electropolished interior) is the standard vacuum chamber material. Copper (OFHC) gaskets for CF flanges provide the lowest outgassing metal seal. Avoid elastomers (Viton O-rings) in ultra-high vacuum, or accept their higher outgassing and replace regularly. Minimize internal surface area (smooth surfaces, no screw threads or blind holes exposed to vacuum).

**Conductance**:
- Gas flow through vacuum piping is limited by the pipe's conductance (analogous to electrical conductance). Conductance depends on pressure regime (viscous flow at higher pressures, molecular flow at lower pressures), pipe diameter, and pipe length.
- **Rule of thumb**: Keep foreline piping between the vacuum chamber and the pump as short and wide as practical. A 1 m length of 25 mm ID pipe has a molecular flow conductance of ~30 L/s for N₂. If the pump has a speed of 300 L/s but is connected through this pipe, the effective pumping speed at the chamber is only ~27 L/s. The pipe chokes the pump. Double the pipe diameter → four times the conductance.
- **Valve conductance**: Every valve in the system adds flow resistance. Gate valves have the highest conductance (nearly full pipe bore when open). Angle valves have lower conductance (gas must change direction 90°). Factor valve conductance into system design calculations.

### Safety & Hazards

**Implosion risk from glass vacuum chambers**: Glass bell jars and glass vacuum apparatus are under ~1 atmosphere (14.7 psi) of external pressure when evacuated. A flaw, scratch, or star crack concentrates stress and can cause sudden catastrophic implosion — the glass fragments are accelerated inward by atmospheric pressure, then bounce outward at high velocity. Risk mitigation: inspect all glassware for scratches, chips, and internal stresses before each use. Wrap glass chambers with adhesive-backed shatter film or multiple layers of tape (contains fragments if implosion occurs). Use polycarbonate safety shields between the operator and the glass chamber. Wear safety glasses at all times near evacuated glass systems. For larger chambers, prefer steel or stainless steel construction over glass.

**Vacuum chamber overpressure protection**: If a vacuum system is accidentally connected to a pressure source (wrong valve opened, gas line backfeed), the chamber can be pressurized beyond its design limit. Steel vacuum chambers are designed for external pressure (vacuum) and may have thin walls that fail under internal pressure. Install pressure relief valves (set slightly above atmospheric, typically 1.1-1.5 bar absolute) on all vacuum chambers. Never pressurize a vacuum vessel beyond its rated pressure. If using a chamber for both vacuum and positive pressure, ensure it is rated for both conditions.

**Oil diffusion pump fire hazard**: Diffusion pump oil is heated to 150-200°C in the boiler. If the cooling water fails (or was never turned on), oil temperature rises uncontrollably — silicone oil decomposes above ~250-300°C, producing flammable decomposition gases. If air leaks into a hot diffusion pump, the mixture of hot oil vapor and oxygen can ignite. Prevention: interlock cooling water flow to pump heater — if water flow stops, heater must shut off automatically. Never vent a hot diffusion pump to air; always cool the boiler below 50°C before venting. Use high-thermal-stability oils (Santovac, DC-705) that resist decomposition. Keep a Class B fire extinguisher nearby.

**Cryogenic trap handling**: Cold traps cooled with liquid nitrogen (LN₂, -196°C) present cold burn and condensation hazards. Skin contact with LN₂-cooled surfaces causes immediate frostbite (tissue destruction identical to burns). Wear insulated cryogenic gloves (not just leather work gloves — cold penetrates thin gloves rapidly) and face shield when handling LN₂ or manipulating cold traps. When filling a cold trap, add LN₂ slowly — rapid pouring causes violent boiling and splashing. **Critical hazard**: if a cold trap is left filled with LN₂ after the vacuum system is vented to air, the trap will condense liquid oxygen from the air (LOX boils at -183°C, warmer than LN₂ at -196°C). LOX is a powerful oxidizer — contact with any organic material (oil, grease, vacuum grease, O-rings) can cause spontaneous ignition or explosion. Always empty cold traps before venting the vacuum system, or warm the trap to above -183°C before air exposure.

### Vacuum Sealing Techniques

**Elastomer O-ring seals**:
- **Material**: Viton (FKM, fluorocarbon) is the standard for vacuum O-rings. Temperature range -20°C to 200°C. Outgassing rate ~10⁻⁶ Pa·m³/s·m² unbaked. Buna-N (nitrile) is cheaper but has higher outgassing and lower temperature limit (~120°C). Silicone O-rings have the widest temperature range (-60°C to 230°C) but highest outgassing and are too soft for some applications.
- **Groove design**: O-ring sits in a rectangular groove machined into one flange face. Groove depth = 70-80% of O-ring cross-section diameter (compresses the ring 20-30% to create seal). Groove width = 120-140% of cross-section (room for the ring to expand when compressed). Surface finish on groove walls: Ra <1.6 μm (smooth enough to prevent leaks past the ring).
- **Limitations**: Elastomer seals limit ultimate vacuum to ~10⁻⁶ to 10⁻⁷ Pa due to outgassing and permeation (atmospheric helium permeates through Viton at ~10⁻⁹ Pa·m³/s). For ultra-high vacuum, metal seals are mandatory.

**Metal seals (CF/ConFlat flanges)**:
- **Design**: Two flat-faced flanges clamp a soft metal gasket (oxygen-free high-conductivity copper, OFHC) between knife-edge grooves machined into each flange face. As bolts are tightened, the knife edges cut into the copper, creating a metal-to-metal seal that is leak-tight to <10⁻¹¹ Pa·m³/s.
- **Advantages**: Bakeable to 450°C, lowest outgassing of any seal type, helium-leak-tight, reusable flanges (copper gasket replaced each time the seal is opened). The standard for ultra-high vacuum (UHV) systems.
- **Disadvantages**: Requires higher bolt torque than O-ring seals (each bolt torqued to 20-30 N·m for typical 2-3/4" CF flanges). Flange surfaces must be protected from scratches (a scratched knife edge leaks). Copper gaskets are single-use.

**Vacuum greases**:
- **Purpose**: Thin film of grease on O-rings improves sealing by filling microscopic surface imperfections. Also lubricates O-ring to prevent binding and tearing during assembly.
- **Types**: Apiezon L (hydrocarbon, lowest vapor pressure ~10⁻⁸ Pa at 20°C, for high vacuum). Apiezon N (general purpose, higher vapor pressure). Silicone vacuum grease (wide temperature range, but can migrate and contaminate surfaces). Fomblin (perfluorinated polyether, chemically inert, for oxygen and reactive gas service).
- **Application rule**: Use as little as possible. Excess grease migrates to chamber walls, increasing outgassing. Apply a thin film, then wipe off the excess with a lint-free cloth until the surface appears only slightly glossy.

### Partial Pressure Measurement

**Residual gas analyzer (RGA)**:
- **Principle**: A miniature mass spectrometer mounted on the vacuum system. Ionizes gas molecules, separates ions by mass-to-charge ratio using a quadrupole mass filter (four parallel rods with RF+DC voltages), and detects ions with a Faraday cup or electron multiplier.
- **Mass range**: 1-100 or 1-200 amu. Resolution: 1 amu (distinguishes adjacent masses).
- **Applications**: Identify what gases remain in the vacuum system (water at 18 amu, nitrogen at 28, oxygen at 32, carbon monoxide at 28, argon at 40, hydrogen at 2, helium at 4). Detect leaks (sudden increase in atmospheric gases). Monitor outgassing during bake-out (watch water peak decrease). Verify process gas purity (contaminants in sputtering or CVD gas streams).
- **Leak detection with RGA**: Spray helium outside the vacuum system while monitoring mass 4 on the RGA. A sudden spike in helium partial pressure indicates the location of the leak. Sensitivity: ~10⁻¹² Pa·m³/s, comparable to dedicated helium leak detectors.

### Vacuum System Materials

**Stainless steel (304L / 316L)**: The standard chamber and piping material for high and ultra-high vacuum. Both grades have low outgassing rates (<10⁻⁹ Torr·L/s·cm² after bake-out), good weldability (the "L" designation means low carbon, which prevents carbide precipitation and corrosion at weld seams), and adequate mechanical strength. 316L is preferred for corrosive gas applications (contains molybdenum for pitting resistance). Electropolishing the interior surface reduces the effective surface area by roughly 50% compared to mechanically polished surfaces, which directly reduces outgassing by cutting the number of adsorption sites for water and gas molecules. Electropolishing also creates a smooth, chromium-rich passive layer that is easier to clean.

**Copper (OFHC)**: Oxygen-free high-conductivity copper is used for CF flange gaskets, internal heat sinks, and braze joints in vacuum assemblies. OFHC copper has very low outgassing (<10⁻⁹ Torr·L/s·cm² baked) and good thermal conductivity (391 W/m·K), making it the standard sealing material for UHV. Copper gaskets are single-use items. Each time a CF flange is opened, the old gasket is discarded and a new one installed. The knife edges on the flanges cut into the copper to a depth of ~0.8 mm during compression, creating a cold-welded metal-to-metal seal. The compressed copper flows into the knife-edge grooves, forming a gas-tight joint rated to below 10⁻¹² Torr.

**Viton O-rings (FKM)**: The standard elastomer for O-ring sealed vacuum flanges (ISO-KF and similar). Usable down to ~10⁻⁸ Torr with proper bake-out. Bakeable to 200°C (short excursions to 250°C are possible but accelerate hardening). Above 200°C, Viton begins to decompose, releasing fluorocarbon fragments that contaminate the vacuum system. For pressures below 10⁻⁸ Torr, Viton's outgassing and helium permeation rate become the limiting factor, and metal seals (copper CF gaskets) are required.

### Leak Detection Methods

**Helium mass spectrometer leak detection**: The most sensitive and widely used method for finding vacuum leaks. A mass spectrometer tuned to helium (mass 4) is connected to the vacuum system. Two modes: (1) Vacuum mode (spray probe): the system is under vacuum and connected to the leak detector. Helium is sprayed on the exterior surface using a fine nozzle. When the spray passes over a leak, helium enters the system and is detected within seconds (response time depends on pumping speed and internal volume). Sensitivity: 10⁻¹² atm·cc/s. (2) Sniffer mode: the system is pressurized with helium (or a helium-air mixture) and a sniffer probe connected to the leak detector is passed over the exterior. Helium escaping through leaks is drawn into the probe. Used for gross leak detection in large systems that cannot easily be evacuated.

**Bubble testing**: The simplest leak detection method, suitable for finding gross leaks (>10⁻⁴ atm·cc/s). Pressurize the system with dry air or nitrogen to 1-2 bar above atmospheric. Apply a soap solution (commercial leak detection fluid or diluted dish soap) to all joints, welds, and fittings. Watch for bubble formation. Each bubble indicates a leak path. The method is inexpensive and requires no special equipment, but it cannot detect the small leaks that matter in high-vacuum systems.

### Pump-Down Time Estimation

The time to pump a vacuum chamber from atmospheric pressure to a target pressure can be estimated from the ideal gas law and the pumping speed. For the roughing phase (above 1 Pa), where outgassing is negligible compared to the gas volume being removed:

t = (V / S) × ln(P₁ / P₂)

where V is the chamber volume (liters), S is the effective pumping speed (liters/second), P₁ is the starting pressure, and P₂ is the target pressure. This assumes constant pumping speed and viscous flow throughout the pressure range. For a 100 L chamber with a 5 L/s rotary vane pump, pumping from 10⁵ Pa to 1 Pa takes roughly t = (100/5) × ln(10⁵/1) = 20 × 11.5 = 230 seconds, or about 4 minutes. In practice, the pumping speed decreases as the pressure drops (especially below 10 Pa where molecular flow begins), and outgassing from chamber walls becomes the dominant gas load below ~1 Pa. The actual roughing time is typically 2-3× the calculated value to account for these effects.

Below 1 Pa, outgassing dominates. The pump-down time to reach 10⁻⁴ Pa (10⁻⁶ Torr) depends on the total outgassing rate of all internal surfaces, not on the chamber volume. A chamber with a large surface area, or one made with high-outgassing materials (Viton, unbaked steel), may take days to reach 10⁻⁴ Pa. Baking the chamber accelerates outgassing by 10-100×, allowing the system to reach base pressure in hours instead of days.

### Vacuum Hygiene

The cleanliness of components installed in a vacuum system directly determines the achievable base pressure and the time to reach it. Contamination from handling, storage, and assembly introduces water, oils, and organic residues that outgas slowly and raise the base pressure.

**Handling**: Never touch vacuum-facing surfaces with bare hands. Skin oils (sebum, primarily fatty acids and squalene) have extremely low vapor pressure and persist on surfaces for days. Use clean nitrile gloves (powder-free) when handling vacuum components, flanges, gaskets, and fixtures. Change gloves if they contact a non-clean surface (bench top, tool handle, clothing). Handle components by their exterior (atmospheric) surfaces whenever possible.

**Cleaning**: New and re-used vacuum components are cleaned in a two-step solvent wash. First, wash with acetone to dissolve organic residues (oils, greases, flux). Acetone is a strong organic solvent that evaporates quickly and leaves minimal residue. Second, rinse with isopropyl alcohol (IPA) to remove the acetone and any remaining water. IPA displaces water and evaporates cleanly. Blow dry with clean, oil-free nitrogen. Do not use compressed shop air (contains oil mist from the compressor). All cleaning is done in a fume hood due to solvent vapors.

**Assembly**: Keep cleaned components wrapped in clean aluminum foil until the moment of installation. Minimize the time the system is open to ambient air (humidity adsorbs on internal surfaces at roughly one monolayer per second at 50% relative humidity). Plan the assembly sequence to minimize open-chamber time. After assembly, pump down immediately and begin bake-out.

**Baking during pump-down**: Heating the vacuum chamber to 150-400°C while pumping accelerates outgassing by 10-100×, converting what would be a weeks-long process into hours. The bake-out temperature is chosen based on the most temperature-sensitive component in the system. Stainless steel chambers with copper CF gaskets tolerate 300-400°C. Viton-sealed systems are limited to 150°C. Internal components (viewports, electrical feedthroughs, sample stages) may have lower temperature limits that constrain the overall bake temperature. Thermocouple gauges taped to the chamber exterior at multiple points verify uniform heating. Hot spots above the target temperature can damage seals or warp flanges, creating new leak paths. The pump-down and bake-out sequence is: rough pump to 1 Pa, start heating, continue pumping while temperature ramps up, hold at temperature for 24-48 hours while monitoring pressure, then cool naturally under vacuum before venting.

**Virtual leaks**: Not all leaks are holes in the chamber wall. A virtual leak is a trapped volume of gas inside the vacuum system that slowly releases into the chamber over time. Common sources: screw threads with trapped air pockets, blind holes that are not vented, gaps between stacked components, and cracks in welds that communicate with the interior through a long, narrow path. Virtual leaks are frustrating because they cause the system to lose vacuum slowly, but helium leak detection cannot find them (the trapped gas is already inside). Prevention: vent all blind holes (drill a relief hole through to the vacuum side or use vented screws), avoid trapped volumes in mechanical designs, and inspect welds radiographically for internal cracks. If a virtual leak is suspected, the pump-down curve shows a characteristic slow, asymptotic approach to base pressure that does not match the calculated outgassing curve.

**Desorption and readsorption**: After a system reaches base pressure and the bake-out is complete, the chamber walls are relatively clean. But every time the system is vented to air (even with dry nitrogen), water vapor and atmospheric gases adsorb on the internal surfaces. The first pump-down after a vent is always slower than subsequent pump-downs on the same system without venting, because the freshly adsorbed gas layers must be desorbed. For systems that must cycle frequently between vacuum and atmosphere (load-lock chambers, batch process tools), a vent-and-purge approach with dry nitrogen reduces the readsorption load compared to venting with humid ambient air. Dry nitrogen venting leaves the surface with only a thin physisorbed N₂ layer, which pumps away quickly, rather than multiple monolayers of water that require extended pumping to remove.

**Vacuum system cost scaling**: The cost of a vacuum system scales roughly with the chamber volume raised to the 0.7 power and with the inverse of the target pressure. A system for 10⁻⁶ Pa costs ~10× more than one for 10⁻³ Pa of the same volume, primarily due to the need for higher-performance pumps, metal-sealed flanges, and bake-out capability. For bootstrap semiconductor manufacturing, the vacuum requirements for basic evaporation (10⁻⁵ to 10⁻⁶ Torr) are achievable with a rotary vane roughing pump plus a small diffusion pump, at modest cost.

---

## Limitations

- **Ultimate pressure limits**: Each pump type has a practical lower pressure limit: rotary vane ~10⁻³ Torr, diffusion pump ~10⁻⁸ Torr, turbomolecular ~10⁻¹⁰ Torr, cryopump ~10⁻¹¹ Torr. Achieving lower pressures requires combining pump types (roughing pump + high-vacuum pump) and careful management of outgassing from chamber walls and internal surfaces.
- **Outgassing dominates at high vacuum**: Below 10⁻⁶ Torr, gas load from outgassing (water vapor desorbing from chamber walls, dissolved gas diffusing from bulk materials) exceeds the gas load from leaks. Achieving UHV requires bake-out (heating the entire chamber to 150-400°C for 24-72 hours while pumping) to drive off adsorbed water and reduce outgassing rates by 100-10,000×.
- **Vibration**: Turbomolecular pumps spinning at 40,000-60,000 RPM transmit vibration to the chamber. Vibration-sensitive applications (SEM, TEM, atomic force microscopy) require vibration isolation or alternative pump technology (ion pumps + NEG for UHV, which have no moving parts).
- **Maintenance intervals**: Rotary vane pumps require oil changes every 3-6 months. Diffusion pump fluid degrades over 1-3 years. Turbomolecular pump bearings last 3-5 years. Cryopumps require regeneration (warm-up to release captured gas) every 4-24 hours depending on gas load. Vacuum system maintenance is a recurring operational cost.

## See Also

- **[Gas Handling Basics](basic.md)**: Positive-pressure gas distribution, piping, and valves
- **[Dopant and Etch Gases](../chemistry/dopant-etch-gases.md)**: Gas panel design and scrubber systems for semiconductor fabs
- **[Hydrogen and Silane](../chemistry/hydrogen-silane.md)**: Vacuum requirements for CVD silicon deposition
- **[Packaging and Testing](../chemistry/packaging-testing.md)**: Vacuum requirements for IC packaging (hermetic sealing)

*Part of the [Bootciv Tech Tree](../index.md) • [Gas Handling](./index.md) • [All Domains](../index.md)*
