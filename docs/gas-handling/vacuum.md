# Vacuum Technology

> **Node ID**: gas-handling.vacuum
> **Domain**: [Gas Handling](./)
> **Enables**: `photolithography.fab-processes`, `silicon.basic-devices`
> **Timeline**: Years 25-40
> **Outputs**: vacuum_pumps, vacuum_chambers, vacuum_measurement, leak_detection

### Vacuum Technology

**Mechanical pumps** (foundation of all vacuum work):

**Piston pump** (simplest, lower vacuum):
- **Construction**: Cast iron cylinder, machined piston with leather cup seal, inlet and outlet check valves (leather or steel flappers). Driven by crank from motor or hand wheel.
- **Performance**: ~10-100 L/min pumping speed. Ultimate vacuum ~10-50 Torr (rough vacuum).
- **Applications**: Initial roughing pump, gas transfer, compression.

**Rotary vane pump** (workhorse — achieves medium vacuum):
- **Principle**: Eccentric rotor in cylindrical stator. Spring-loaded vanes slide in rotor slots, maintaining contact with stator wall. Gas enters inlet port, trapped between vanes and stator, compressed, expelled through exhaust valve.
- **Construction**: Cast iron stator (bored to ~0.01 mm tolerance on Machine Tools lathe/boring machine). Steel rotor. Steel or carbon fiber vanes. Oil-filled for sealing and lubrication (oil seals microscopic gaps between vanes and stator).
- **Oil requirements**: Low vapor pressure vacuum oil (see [Lubricants](../chemistry/lubricants.md)). Mineral oil with low volatility, or silicone oil. Oil changed regularly — contaminated oil limits ultimate vacuum.
- **Performance**: 1-50 L/min (small), 50-500 L/min (medium). Ultimate vacuum: ~10⁻² to 10⁻³ Torr (0.01-0.001 Pa). Single-stage: ~10⁻² Torr. Two-stage: ~10⁻³ Torr.
- **Gas ballast**: Small valve admits air during compression phase to prevent condensation of vapors (water, solvents) in pump oil. Essential when pumping wet systems.

**Diffusion pump** (high vacuum, no moving parts):
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

**Two-stage pump system** (standard for high vacuum):
- **Roughing pump** (rotary vane or diaphragm): Pulls system from atmospheric pressure (~10⁵ Pa) down to ~0.1-1 Pa. This is the "rough vacuum" phase. The roughing pump handles the bulk of the gas load — most of the air molecules are removed in this stage.
- **High-vacuum pump** (turbomolecular or diffusion pump): Takes over at the **crossover pressure** (~1 Pa, or ~10⁻² Torr). Below this pressure, molecular flow dominates and the high-vacuum pump becomes effective. Crossover too early → gas load overloads the high-vacuum pump. Crossover too late → wastes time and risks oil backstreaming from roughing pump.
- **Pump-down sequence**: Open roughing valve, close high-vacuum valve. Rough to ~1 Pa. Close roughing valve, open high-vacuum valve. Continue pumping to target base pressure (10⁻⁴ to 10⁻⁶ Pa for most semiconductor processes).
- **Turbomolecular pump vs. diffusion pump**: Turbo pump — fast startup (1-3 min), clean (no oil vapor), expensive to build (precision rotor at 30,000-90,000 RPM). Diffusion pump — slower startup (15-30 min), requires cold trap to prevent oil backstreaming, simpler construction, lower cost.

### Outgassing Rates by Material

Every surface in a vacuum system releases adsorbed gas molecules — this is outgassing, and it dominates pump-down time below ~1 Pa.

| Material | Outgassing Rate (Pa·m³/s·m²) | Conditions |
|----------|-------------------------------|------------|
| **Stainless steel** (electropolished) | ~10⁻⁸ after bake | Standard for vacuum chambers. Improves 10-100× with bake-out. |
| **Stainless steel** (unbaked) | ~10⁻⁶ | Freshly manufactured, exposed to air. Mainly H₂O desorption. |
| **Viton** (unbaked) | ~10⁻⁶ | Elastomer O-ring seals. Major gas source. Bake reduces by 10-100×. |
| **Viton** (baked) | ~10⁻⁷ to 10⁻⁸ | After 24h at 150°C. Still higher than metal. |
| **Copper** (OFHC, baked) | ~10⁻⁹ | Lowest outgassing of practical materials. Used for CF flange gaskets. |
| **PTFE** | ~10⁻⁶ | Good chemical resistance but high outgassing. Avoid in UHV. |
| **Aluminum** (baked) | ~10⁻⁹ | Good if surface oxide is controlled. Porous to He — problematic for leak detection. |

Design rule: minimize internal surface area, avoid elastomers where possible, bake if target pressure is below 10⁻⁵ Pa.

### Bake-Out Procedures

- **Purpose**: Accelerate desorption of water vapor, dissolved gases, and volatile contaminants from vacuum chamber walls. A system that takes 2 weeks to reach 10⁻⁶ Pa without bake-out can reach it in 24-48 hours with bake-out.
- **Temperature**: 150-300°C depending on chamber materials and seals. Stainless steel chambers with copper CF gaskets: 250-300°C. Viton-sealed chambers: 150°C maximum (Viton degrades above 200°C). Glass systems: 200-300°C.
- **Duration**: 24-48 hours at temperature while continuously pumping. Longer bake for lower target pressures.
- **Method**: Wrap chamber with heating tape (nichrome or silicone rubber insulated) or use custom-fitted band heaters. Cover with aluminum foil or fiberglass insulation to maintain uniform temperature. Monitor with thermocouples taped to multiple points on the chamber surface (top, bottom, side, ports). Avoid hot spots — local overheating warps flanges and ruins sealing surfaces.
- **Cool-down**: After bake, turn off heaters. Allow system to cool naturally while still under vacuum. Do not vent until below 50°C — rapid cooling with air exposure re-adsorbs moisture, undoing much of the bake-out benefit.
### Safety & Hazards

**Implosion risk from glass vacuum chambers**: Glass bell jars and glass vacuum apparatus are under ~1 atmosphere (14.7 psi) of external pressure when evacuated. A flaw, scratch, or star crack concentrates stress and can cause sudden catastrophic implosion — the glass fragments are accelerated inward by atmospheric pressure, then bounce outward at high velocity. Risk mitigation: inspect all glassware for scratches, chips, and internal stresses before each use. Wrap glass chambers with adhesive-backed shatter film or multiple layers of tape (contains fragments if implosion occurs). Use polycarbonate safety shields between the operator and the glass chamber. Wear safety glasses at all times near evacuated glass systems. For larger chambers, prefer steel or stainless steel construction over glass.

**Vacuum chamber overpressure protection**: If a vacuum system is accidentally connected to a pressure source (wrong valve opened, gas line backfeed), the chamber can be pressurized beyond its design limit. Steel vacuum chambers are designed for external pressure (vacuum) and may have thin walls that fail under internal pressure. Install pressure relief valves (set slightly above atmospheric, typically 1.1-1.5 bar absolute) on all vacuum chambers. Never pressurize a vacuum vessel beyond its rated pressure. If using a chamber for both vacuum and positive pressure, ensure it is rated for both conditions.

**Oil diffusion pump fire hazard**: Diffusion pump oil is heated to 150-200°C in the boiler. If the cooling water fails (or was never turned on), oil temperature rises uncontrollably — silicone oil decomposes above ~250-300°C, producing flammable decomposition gases. If air leaks into a hot diffusion pump, the mixture of hot oil vapor and oxygen can ignite. Prevention: interlock cooling water flow to pump heater — if water flow stops, heater must shut off automatically. Never vent a hot diffusion pump to air; always cool the boiler below 50°C before venting. Use high-thermal-stability oils (Santovac, DC-705) that resist decomposition. Keep a Class B fire extinguisher nearby.

**Cryogenic trap handling**: Cold traps cooled with liquid nitrogen (LN₂, -196°C) present cold burn and condensation hazards. Skin contact with LN₂-cooled surfaces causes immediate frostbite (tissue destruction identical to burns). Wear insulated cryogenic gloves (not just leather work gloves — cold penetrates thin gloves rapidly) and face shield when handling LN₂ or manipulating cold traps. When filling a cold trap, add LN₂ slowly — rapid pouring causes violent boiling and splashing. **Critical hazard**: if a cold trap is left filled with LN₂ after the vacuum system is vented to air, the trap will condense liquid oxygen from the air (LOX boils at -183°C, warmer than LN₂ at -196°C). LOX is a powerful oxidizer — contact with any organic material (oil, grease, vacuum grease, O-rings) can cause spontaneous ignition or explosion. Always empty cold traps before venting the vacuum system, or warm the trap to above -183°C before air exposure.

---

*Part of the [Bootciv Tech Tree](../) • [Gas Handling](./) • [All Domains](../)*
