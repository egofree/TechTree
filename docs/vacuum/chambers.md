# Vacuum Chambers & Sealing

> **Node ID**: vacuum.chambers
> **Domain**: [Vacuum Technology](./index.md)
> **Dependencies**: `machine-tools`, `machine-tools.joining.electron-beam`, `machine-tools.joining.tig-welding`, `metals`
> **Enables**: [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`silicon.basic-devices`](../silicon/basic-devices.md)
> **Timeline**: Years 25-40
> **Outputs**: vacuum_chambers, vacuum_seals, viewports, gate_valves, load_locks
> **Critical**: Yes — vacuum chambers are required for all semiconductor thin-film deposition and lithography processes

## Problem

Vacuum chambers are sealed enclosures that maintain controlled low-pressure environments for semiconductor processing, thin-film deposition, and surface analysis. For basic vacuum concepts and outgassing tables, see [Gas Handling: Vacuum](../gas-handling/vacuum.md). This document covers chamber design engineering, advanced sealing systems, and chamber subsystems. The central challenge is building a vessel that is structurally sound under 1 atmosphere of external pressure, leak-tight to 10⁻⁹ Torr, clean enough to avoid contaminating the process, and equipped with sealed ports for power, cooling, viewports, and sample introduction.

## Prerequisites

- [Machine Tools](../machine-tools/index.md) — precision machining for flange sealing surfaces
- [TIG Welding](../machine-tools/joining.md) — stainless steel chamber welding
- [Metals](../metals/index.md) — stainless steel and aluminum for chamber construction

## Chamber Design Principles

**Pressure loading**: A vacuum chamber is a pressure vessel loaded in external pressure (compression). At high vacuum (10⁻⁶ Torr), the pressure differential is ~1 atmosphere (14.7 psi, 101 kPa) pushing inward on every surface. For a cylindrical chamber of diameter D and wall thickness t, the compressive hoop stress is:

σ = P × D / (2 × t)

where P is the external pressure (atmospheric, ~0.1 MPa). For a 300 mm diameter chamber with 5 mm wall thickness: σ = 0.1 × 300 / (2 × 5) = 3 MPa. Stainless steel yield strength ~200 MPa — stress is well within limits. But for larger chambers (e.g., 1 m diameter with 3 mm wall): σ = 0.1 × 1000 / (2 × 3) = 16.7 MPa. Still safe, but approaching the regime where buckling (elastic instability) rather than yield becomes the failure mode.

**Buckling criterion**: Thin-walled cylinders under external pressure fail by buckling at stresses far below yield. The critical buckling pressure for a thin cylinder is:

P_cr = 0.92 × E × (t/D)^(5/2) × (L/D)

where E is Young's modulus (~200 GPa for stainless steel), t is wall thickness, D is diameter, L is length. Design with a safety factor of 4-6 against buckling for vacuum chambers.

**Spherical vs. cylindrical**: Spherical chambers are the most efficient shape for vacuum (uniform stress distribution, minimum surface area for given volume). But they are expensive to manufacture and difficult to fit with ports and viewports. Most semiconductor vacuum chambers are cylindrical with dished (ellipsoidal or torispherical) end caps, or rectangular (for batch processing tools with internal wafer transport).

## Chamber Materials

**Stainless steel 304L (primary material)**:

**Strengths**:
- Excellent weldability with matching 308L filler — all standard joining processes applicable
- Low outgassing after electropolishing: 10⁻⁸ to 10⁻⁹ Pa·m³/s·m² after 24h bake at 250°C
- Widely available, well-characterized mechanical properties, proven vacuum performance

**Weaknesses**:
- Heavy (density 8.0 g/cm³) — large chambers require cranes for handling
- Low thermal conductivity (16 W/m·K) — slow to heat uniformly during bake-out
- Susceptible to sensitization at >300°C (chromium carbide precipitation) if not "L" grade
- **Composition**: 18% Cr, 8% Ni, ≤0.03% C (the "L" = low carbon, prevents sensitization and intergranular corrosion at welds)
- **Properties**: Yield strength ~170-200 MPa, thermal conductivity ~16 W/m·K (low — helps with thermal isolation), coefficient of thermal expansion ~17.3 μm/m·K
- **Outgassing**: 2×10⁻⁶ Pa·m³/s·m² unbaked, 10⁻⁸ to 10⁻⁹ Pa·m³/s·m² after 24h bake at 250°C
- **Weldability**: Excellent. 304L can be TIG welded with matching 308L filler rod. Autogenous welding (no filler) for thin sections. All interior welds must be full-penetration, smooth (ground flush), and free of porosity, undercut, and crevices. Crevices trap gas — virtual leak sources.
- **Surface preparation**: Electropolishing reduces effective surface area by ~50% vs. mechanical polishing. The electropolished surface is chromium-rich (Cr₂O₃ passive layer) and smooth (Ra <0.4 μm), directly reducing outgassing by cutting adsorption sites. Electropolishing bath: phosphoric acid + sulfuric acid + glycerol, 50-80°C, current density 10-30 A/dm².

**Stainless steel 316L (for corrosive service)**:
- **Additional alloying**: 2-3% molybdenum for pitting and crevice corrosion resistance. Essential when the chamber will be exposed to halogen gases (Cl₂, F₂, CF₄ decomposition products) during plasma etching or CVD processes.
- **Cost premium**: ~30-50% more expensive than 304L. Use 304L for general vacuum chambers and 316L for process chambers with corrosive gas exposure.

**Aluminum 6061-T6 (lightweight alternative)**:
- **Properties**: Yield strength ~275 MPa (higher than 304L), density 2.7 g/cm³ (1/3 of steel), thermal conductivity 167 W/m·K (10× steel — excellent for uniform heating/cooling)
- **Advantages**: Lighter (easier to handle and ship), machines easily, good thermal conductivity for bake-out uniformity, non-magnetic (important for electron optics and ion pumps)
- **Disadvantages**: Porous to helium (He permeation rate ~10⁻⁹ Pa·L/s per cm² at room temperature — problematic for He leak detection, as He diffuses through the chamber walls, creating a false background signal). Aluminum develops a surface oxide (Al₂O₃) that is very stable but relatively thick (~5-10 nm), providing adsorption sites for water vapor. Cannot be easily welded to stainless steel flanges (thermal expansion mismatch, galvanic corrosion).
- **Sealing approach**: Aluminum chambers typically use wire seals (aluminum, indium, or copper wire in a groove) rather than CF knife-edge seals, because aluminum is too soft to maintain the knife edges. Or use stainless steel flanges brazed or transition-fit onto aluminum chamber bodies.

## Flange Systems

**CF (ConFlat) flanges — the UHV standard**:

**Strengths**:
- Leak rate <10⁻¹² Pa·m³/s — helium leak-tight to below detection limit
- Bakeable to 450°C — suitable for UHV systems requiring high-temperature bake-out
- Metal-to-metal seal (copper gasket) — no elastomer outgassing

**Weaknesses**:
- Single-use gaskets — must be replaced each time flange is opened (consumable cost)
- Overtightening permanently damages knife edges — requires careful torque procedure
- Bolt tightening in star pattern with 3-4 stages — time-consuming for large flanges

**ISO-KF flanges — the quick-connect standard for roughing/medium vacuum**:

**Strengths**:
- Quick connect/disconnect: clamp closure in seconds — no bolt tightening
- Universal compatibility across manufacturers
- Low cost: stamped flanges and molded O-rings

**Weaknesses**:
- O-ring outgassing limits ultimate vacuum to ~10⁻⁸ Pa·m³/s — not UHV compatible
- Viton O-rings limited to 150°C bake — silicone alternative has higher outgassing
- O-rings degrade over time: compression set, chemical attack, radiation damage

**ISO-K flanges — larger sizes for roughing/medium vacuum**:
- **Design**: Similar to KF but for larger diameters (DN63 through DN500). Uses a rubber O-ring on a metal carrier ring, held by claw clamps that engage grooves in the flange OD.
- **Application**: Main pump lines, large foreline manifolds, roughing lines for large chambers.

## Viewports

**Purpose**: Optical access to the vacuum chamber interior for visual inspection, optical pyrometry, laser entrance/exit, and UV curing.

**Construction**: A glass window (fused silica, borosilicate, or sapphire) brazed into a stainless steel or Kovar housing that mates with a CF or KF flange. The glass-to-metal seal must be leak-tight and withstand bake-out temperatures.

**Window materials**:
| Material | Transmission Range | Bake Temperature | Typical Use |
|---|---|---|---|
| Borosilicate glass | 300 nm – 3 μm | ≤350°C | Visual inspection, general purpose |
| Fused silica (quartz) | 160 nm – 4 μm | ≤450°C | UV processes, UV lithography, pyrometry |
| Sapphire (Al₂O₃) | 150 nm – 6 μm | ≤450°C | High-pressure differential, IR transmission, scratch-resistant |
| MgF₂ | 110 nm – 8 μm | ≤300°C | Deep UV, VUV applications |
| ZnSe | 500 nm – 20 μm | ≤200°C | CO₂ laser (10.6 μm), IR pyrometry |

**Design considerations**: Viewports are the weakest point in a UHV system — the glass-to-metal seal can develop micro-cracks from thermal cycling, and the glass itself can fracture from mechanical shock. Install viewports on the side or top of the chamber (not the bottom, where they are vulnerable to dropped objects). Protect viewport exteriors with removable caps when not in use. Never touch viewport glass with bare hands (skin oils deposit a film that is difficult to clean and absorbs UV). Clean viewports with acetone followed by IPA on lint-free wipes.

## Gate Valves

**Purpose**: Isolate the high-vacuum pump from the chamber, allowing the pump to remain under vacuum while the chamber is vented (or vice versa). Essential for: (1) protecting turbo pumps from sudden pressure bursts during chamber venting, (2) allowing pump maintenance without venting the entire system, and (3) load lock isolation.

**Types**:
- **Pneumatic gate valve**: Compressed air actuator drives a gate (flat plate with O-ring seal) across the valve body. Opening/closing time: 1-3 seconds. Reliable, fast, but requires compressed air supply (~5-6 bar). Most common in semiconductor processing equipment.
- **Manual gate valve**: Hand knob drives the gate via a lead screw. Slower to operate but no external power required. Common on smaller systems and laboratory setups.
- **Magnetically coupled gate valve**: Gate driven through the valve body wall by external magnetic coupling. No bellows or shaft seal — eliminates one potential leak path. Higher cost.

**Sealing**: Gate valves use an elastomer O-ring (Viton or silicone) on the gate plate to seal against the valve body. Some UHV gate valves use a copper or indium seal on the gate, but these are single-use (like CF gaskets). Standard gate valves are NOT suitable for UHV isolation — they leak at the shaft feedthrough (bellows) and the gate O-ring. For UHV, use all-metal angle valves (with copper gasket seat) instead.

**Conductance**: When open, a gate valve has nearly the full bore of the connected flange — very high conductance. This is why gate valves are preferred over angle valves on high-vacuum pump lines (where maximum conductance is critical).

## Load Locks

**Purpose**: Transfer samples into and out of the vacuum chamber without venting the main chamber to atmosphere. Every vent-and-repump cycle exposes the main chamber to water vapor and contaminants, requiring hours of pumping to recover base pressure. A load lock limits contamination to the small lock volume.

**Design**:
- **Volume**: Minimize load lock volume to minimize pump-down time. Typical load lock: 5-20 L (holds 1-25 wafers). Pump-down from atmosphere to 10⁻⁶ Torr: 5-15 minutes (vs. 2-8 hours for main chamber).
- **Pumping**: Dedicated roughing pump + small turbo (or just a roughing pump if the load lock only needs medium vacuum). Valved connection to main chamber for high-vacuum transfer.
- **Gate valves**: Two gate valves — one to atmosphere (or a vent valve) and one to the main chamber. The sample enters through the atmospheric gate, the lock is pumped down, then the high-vacuum gate opens for transfer.
- **Sample transfer mechanism**: Magnetic feedthrough (external magnet moves a trolley inside the lock), wobble stick (bellows-sealed push rod), or motorized transfer arm. Must not introduce particles or contaminants into the main chamber.

**Vent gas**: Always vent load locks with dry nitrogen (N₂) rather than atmospheric air. Dry N₂ leaves only a thin physisorbed N₂ layer on internal surfaces, which pumps away quickly. Atmospheric air deposits multiple monolayers of water vapor, requiring extended pumping. Connect a N₂ supply with a pressure regulator set to 1.0-1.2 bar absolute (slightly above atmospheric) and a 0.2 μm particle filter to prevent dust ingress.

## Outgassing Rate Table — Materials for Chamber Design

| Material | Outgassing Rate (Pa·m³/s·m²) | After 10h pumping | After 24h bake at 250°C | Notes |
|---|---|---|---|---|
| SS 304L, electropolished | 2×10⁻⁶ | ~2×10⁻⁷ | ~10⁻⁸ to 10⁻⁹ | Standard chamber material |
| SS 304L, mechanically polished | 5×10⁻⁶ | ~5×10⁻⁷ | ~2×10⁻⁸ | Rougher surface = more adsorption |
| SS 304L, as-received | 10⁻⁵ | ~10⁻⁶ | ~5×10⁻⁸ | Needs cleaning and baking |
| Aluminum 6061, machined | 5×10⁻⁶ | ~5×10⁻⁷ | ~10⁻⁸ | He permeation issue |
| Copper OFHC, baked | 10⁻⁶ | ~10⁻⁷ | ~10⁻⁹ | CF gasket material |
| Viton, unbaked | 10⁻⁵ | ~10⁻⁶ | N/A (degrades >200°C) | Elastomer seal |
| Viton, baked 150°C/24h | 10⁻⁶ | ~10⁻⁷ | N/A | Pre-baked O-rings |
| PTFE (Teflon) | 10⁻⁵ | ~10⁻⁶ | ~10⁻⁷ (max 300°C) | Avoid in UHV — high outgassing |
| Glass (borosilicate) | 10⁻⁷ | ~10⁻⁸ | ~10⁻⁹ | Viewport material |
| Alumina ceramic | 10⁻⁷ | ~10⁻⁸ | ~10⁻⁹ | Electrical feedthrough insulator |

## Virtual Leaks

A virtual leak is a trapped volume of gas inside the vacuum system that slowly releases into the chamber over time, causing slow pressure decay that mimics a real leak but cannot be detected by helium leak detection.

**Common sources**:
- **Unvented screw holes**: A screw threaded into a blind hole traps air in the threads. As the chamber is evacuated, this trapped air slowly leaks past the threads over hours to days. Prevention: use vented screws (with a hole drilled through the center or a flat milled along the thread), or never use threaded fasteners that face the vacuum side.
- **Double O-ring seals with unvented gap**: Two concentric O-rings with an unventilated annular gap between them trap gas. Prevention: drill a small vent hole through the flange to the gap, connecting it to the vacuum side.
- **Internal cracks in welds**: A subsurface crack that communicates with the vacuum through a long, narrow path. The crack volume empties slowly. Prevention: full-penetration welds on all vacuum-side joints, radiographic inspection of critical welds.
- **Gaps between stacked components**: Two flanges bolted together with an unsealed gap between them. Prevention: design joints with continuous metal-to-metal contact, or seal all edges.

**Diagnostic signature**: A virtual leak causes a characteristic pressure vs. time curve that follows 1/t decay (outgassing) rather than the exponential decay of a real leak. The system pressure asymptotically approaches a steady-state value that is higher than expected. Helium spray testing finds nothing. RGA shows atmospheric gas composition (N₂, O₂) rather than He.

## Chamber Cleaning Protocol

**New chamber preparation** (before first pump-down):
1. **Degrease**: Wipe all interior surfaces with lint-free cloth soaked in acetone. Remove machining oils, cutting fluids, and handling residues. Acetone dissolves organic contaminants.
2. **Solvent rinse**: Rinse with isopropyl alcohol (IPA) to remove acetone residue and any remaining water. IPA displaces water and evaporates cleanly.
3. **Dry**: Blow dry with clean, oil-free nitrogen. Never use compressed shop air (contains oil mist).
4. **Inspect**: Examine all interior surfaces, welds, and sealing surfaces under bright light. Look for: scratches on sealing surfaces, weld porosity, debris, fingerprints.
5. **Wrap**: Cover all openings with clean aluminum foil until ready for assembly. Do not use plastic caps (outgas plasticizers).

**Routine cleaning** (between process runs):
1. **Wipe down**: Clean interior with acetone-soaked lint-free wipes to remove process deposits (metal films, polymer residues, particles).
2. **Stubborn deposits**: For thick metal deposits (e.g., aluminum from evaporation), soak with dilute NaOH solution (10%, room temperature, 5-10 minutes) — NaOH dissolves aluminum without attacking stainless steel. Rinse thoroughly with DI water, then IPA, then dry.
3. **Plasma clean**: For organic contamination, run an O₂ plasma (100-300 W, 0.5-1 Torr, 10-30 minutes) in the chamber. Oxygen plasma oxidizes organic residues to CO₂ and H₂O, which are pumped away. The chamber must be equipped with an RF electrode for this.

## Bake-Out Hardware

- **Heating tape**: Silicone rubber insulated heating tape (nichrome wire element) wrapped around the chamber exterior. Available in widths 10-50 mm, power density 0.5-2 W/cm². Attach with aluminum foil tape (good thermal contact). Cover with fiberglass insulation blanket (25-50 mm thick) to minimize heat loss.
- **Band heaters**: Custom-fitted aluminum or stainless steel heating bands with embedded cartridge heaters. Better thermal contact than tape, more uniform heating. Used on production equipment.
- **Temperature monitoring**: Attach Type K thermocouples to the chamber exterior at 4-8 locations (top, bottom, sides, flanges). Monitor during bake to ensure uniformity ±20°C. Hot spots above 300°C on stainless steel can cause sensitization (chromium carbide precipitation at grain boundaries) — avoid.
- **Cooling**: After bake, turn off heaters and allow natural cooling under vacuum. Do not force-cool with fans (creates thermal gradients that warp flanges). Do not vent until chamber exterior is below 50°C.

## Electrical Feedthroughs

**Purpose**: Pass electrical signals and power through the vacuum chamber wall while maintaining vacuum integrity.

**Types by construction**:
- **Ceramic-to-metal seal**: Alumina (Al₂O₃) ceramic insulator brazed to a Kovar (Fe-Ni-Co alloy) housing, which is welded into a CF flange. The ceramic provides electrical insulation, the metal housing provides the vacuum seal. Rated for UHV (bakeable to 450°C), leak rate <10⁻¹¹ Pa·m³/s.
- **Glass-to-metal seal**: Glass insulator sealed to a metal shell. Lower cost but limited bake temperature (≤200°C) and more fragile. Used for KF and roughing vacuum feedthroughs.
- **Epoxy seal**: Pins potted in epoxy in a metal shell. Lowest cost, but epoxy outgasses and limits bake temperature to ≤120°C. Not suitable for UHV. Acceptable for rough vacuum instrumentation.

**Common configurations**:
| Type | Pin Count | Current Rating | Voltage Rating | Typical Use |
|---|---|---|---|---|
| Power feedthrough | 2-8 pins | 5-30 A/pin | 1-5 kV | Heater power, motor drives |
| Signal feedthrough | 4-50 pins | 1-5 A/pin | 200-500 V | Thermocouples, sensors, gauges |
| Coaxial (BNC, SMA) | 1 coax | 1 A | 500 V | RF signals, detector outputs |
| High voltage | 1-2 pins | 0.5-2 A | 5-50 kV | Ion pumps, e-beam, plasma |
| Thermocouple (matched) | 2-8 pairs | Low | 50 V | Type K thermocouple wires |

**Design rule**: Always specify feedthroughs with more pins than currently needed. Adding a feedthrough to an existing chamber requires welding, which is expensive and risks damaging other components. Include 20-30% spare pins for future instrumentation.

## Water Cooling Lines

**Purpose**: Remove heat from chamber walls during processing (plasma processes generate significant heat: 100-5000 W at the chamber walls).

**Design**:
- Weld stainless steel tubing (6-12 mm OD) to the exterior of the chamber in a serpentine pattern. Water flows through the tubing, cooling the chamber wall by conduction.
- Alternatively, weld a full water jacket (outer shell around the chamber with 5-10 mm water gap) for maximum cooling capacity.
- Water flow rate: 2-10 L/min depending on heat load. Temperature rise: ΔT = Q / (c × ρ × V_flow), where Q is heat load (W), c = 4186 J/kg·K, ρ = 1000 kg/m³.
- **Example**: Removing 1000 W with 5 L/min water flow: ΔT = 1000 / (4186 × 1000/60 × 0.005) = 2.9°C. Modest temperature rise — adequate cooling.
- Water connections: Use Swagelok or compression fittings on the atmospheric side. Ensure water lines do not create a leak path into the vacuum chamber — all welds between cooling channels and the vacuum wall must be leak-tested.

## Chamber Design Checklist

- [ ] Minimum internal surface area (smooth surfaces, no crevices, no blind holes)
- [ ] All vacuum-side welds are full-penetration, ground smooth, and inspected
- [ ] Material: 304L (general) or 316L (corrosive gas service) stainless steel
- [ ] Interior surface electropolished (Ra < 0.4 μm)
- [ ] Flanges: CF for UHV connections, KF for roughing/venting
- [ ] Viewports on sides or top (not bottom), with protective caps
- [ ] Gate valve between chamber and high-vacuum pump
- [ ] Load lock for sample introduction (avoid venting main chamber)
- [ ] Pressure relief valve (1.1-1.5 bar absolute) for overpressure protection
- [ ] Thermocouple ports for bake-out temperature monitoring
- [ ] Electrical feedthroughs (pins rated for required current/voltage)
- [ ] All virtual leak sources eliminated (vented screws, no unvented gaps)
- [ ] Water cooling lines for high-power process heat removal
- [ ] RGA port for residual gas monitoring during processing

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Cannot reach base pressure after vent | Water vapor readsorbed on chamber walls | Bake chamber at 150-200°C for 24h while pumping; use dry N₂ vent instead of air; extend pump-down |
| Virtual leak (slow pressure rise after isolation) | Trapped gas pocket in screw hole or weld crevice | Use vented screws; eliminate unvented blind holes; Helium leak check interior welds |
| CF flange leak after thermal cycling | Copper gasket work-hardened or flange face damaged | Replace copper gasket; inspect flange knife-edge for nicks; re-torque bolts in star pattern |
| Viewport cracking | Differential thermal expansion or mechanical stress | Use compatible viewport glass (Kovar-matched); avoid tightening viewport under vacuum; protect from deposition |
| Chamber wall corrosion | Reactive process gases attacking stainless steel | Electropolish internal surfaces; use aluminum chamber for chlorine processes; apply protective coating |
| Gate valve failing to seal | Bellows fatigue or particle contamination on seal | Cycle valve to dislodge particles; replace bellows if cracked; install upstream particulate filter |

## See Also

- [Gas Handling: Vacuum](../gas-handling/vacuum.md) — outgassing rates, bake-out procedures, vacuum hygiene
- [Vacuum Pumps](pumps.md) — pump selection and specifications
- [Vacuum Measurement & Leak Detection](measurement.md) — leak detection methods
- [Lubricants](../chemistry/lubricants.md) — vacuum grease specifications

[← Back to Vacuum Technology](index.md)
