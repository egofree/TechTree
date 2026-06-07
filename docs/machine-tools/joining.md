# Metal Joining

> **Node ID**: machine-tools.joining
> **Domain**: [Machine Tools Bootstrap](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`energy.electricity`](../energy/electricity.md), [`metals.alloys`](../metals/alloys.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`energy.steam-power`](../energy/steam-power.md), [`machine-tools.joining.diffusion-bonding`](./joining.md), [`machine-tools.joining.electron-beam`](./joining.md), [`machine-tools.joining.friction-stir`](./joining.md), [`machine-tools.joining.laser-welding`](./joining.md), [`machine-tools.joining.mig-welding`](./joining.md), [`machine-tools.joining.resistance-welding`](./joining.md), [`machine-tools.joining.tig-welding`](./joining.md), [`machine-tools.joining.ultrasonic-bonding`](./joining.md)
> **Timeline**: Years 5-70
> **Outputs**: forge_welds, brazed_joints, soldered_joints, riveted_joints, welded_joints, acetylene, tig_welds, mig_welds, resistance_welds, electron_beam_welds, ultrasonic_bonds, friction_stir_welds, laser_welds, diffusion_bonds, hermetic_seals, wire_bonds
> **Critical**: Yes — makes machinery possible by assembling individual parts into structures, mechanisms, and pressure vessels


Metal joining is the capability that makes machinery possible. Individual forged or cast parts are rarely useful alone — they must be assembled into structures, mechanisms, pressure vessels, and frames. Each method occupies a specific niche defined by temperature, joint strength, equipment requirements, and the materials it can join. No single method replaces all others — a complete industrial shop needs all three families.

For the metallurgy of producing iron and steel stock to be joined, see [Iron & Steel](../metals/iron-steel.md). For the electrical infrastructure needed by arc welding, see [Electricity](../energy/electricity.md).

## Articles in this Section

- **[Welding](./welding.md)** — Forge welding, oxy-acetylene welding, SMAW (stick), TIG (GTAW), MIG (GMAW), resistance spot/seam welding, electron beam welding, ultrasonic welding & wire bonding, friction stir welding, laser welding, and diffusion bonding. Covers vacuum chamber fabrication, hermetic sealing, and weld quality inspection.
- **[Brazing & Soldering](./brazing-soldering.md)** — Brass brazing (spelter brazing), silver brazing (hard soldering), and soft soldering. Filler alloy joining where the base metal does not melt. Brazing for structural joints; soldering for electrical connections, plumbing, and sheet metal seams.
- **[Riveting](./riveting.md)** — Hot and cold riveting, joint configurations (lap, butt with cover plates, boiler seams), rivet patterns, and inspection. Mechanical joining with no heat at the joint.

## Method Selection Overview

| Method | Temp Range | Joint Strength | Best For |
|--------|-----------|---------------|----------|
| Soft soldering | 180-250°C | 20-50 MPa | Electrical connections, plumbing, sheet metal seams |
| Silver brazing | 620-780°C | 150-300 MPa | Fine mechanisms, instruments, dissimilar metals |
| Brass brazing | 870-950°C | 150-250 MPa | Structural joints, cast iron, pipe fittings |
| Riveting | Cold or 900°C | 80-150 MPa (shear) | Structural steel, boilers, bridges, ship hulls |
| Forge welding | 1200-1300°C | 250-400 MPa | Iron/low-carbon steel bars, chains, composite billets |
| Oxy-acetylene | ~3100°C | 300-450 MPa | Sheet metal, repair, cutting, general fabrication |
| SMAW (stick) | ~6000°C (arc) | 350-480 MPa | Structural steel, heavy fabrication, pressure vessels |
| TIG (GTAW) | ~6000°C (arc) | 350-520 MPa | Stainless steel, aluminum, titanium, thin-wall tubing |
| MIG (GMAW) | ~6000°C (arc) | 350-500 MPa | High-deposition fabrication, sheet metal, automotive |
| Resistance (spot) | N/A | 200-400 MPa (shear) | Sheet metal lap joints, automotive, appliance panels |
| Electron beam | N/A | 350-550 MPa | Vacuum chambers, aerospace, refractory metals |
| Friction stir | N/A | 300-500 MPa | Aluminum alloys (2xxx, 7xxx), dissimilar metal joints |
| Laser | N/A | 350-520 MPa | High-speed welding, precision, automation |
| Diffusion bonding | 50-80% Tm | 80-100% parent | Dissimilar metals, UHV components, complex internals |

## Method Selection by Application

| Application | Preferred Method | Why | Typical Parameters |
|-------------|-----------------|-----|-------------------|
| Structural steel buildings | SMAW (stick) | Works outdoors, wind-tolerant, portable | E7018, 90-150A, 2.4-3.2 mm rod |
| Ship hull plates | MIG or FCAW | High deposition rate, long continuous seams | 1.2 mm wire, 200-300A, 25-30V |
| Stainless steel tubing (sanitary) | TIG (orbital) | Clean welds, smooth internal bead, no contamination | 1.6 mm tungsten, 80-120A, argon shielding + back purge |
| Aluminum airframe structures | Friction stir welding | Joins 2xxx/7xxx alloys without hot cracking or porosity | 1000-1500 RPM, 200-400 mm/min traverse |
| Copper battery tabs to bus bars | Ultrasonic welding | Solid-state, no melt, no intermetallics | 20 kHz, 200-500 N, 0.2-0.5 s |
| Semiconductor vacuum chambers | Electron beam or TIG | Zero porosity, leak rate below 10⁻⁹ mbar·L/s | EB: 60-120 kV, 20-50 mA; TIG: orbital, argon |
| Bridge repair (field) | SMAW or FCAW | No shielding gas needed in wind, portable equipment | E7018 or E71T-1 self-shielded wire |
| Boiler longitudinal seam | Double-riveted butt or submerged arc | Historically riveted for inspectability; modern: submerged arc | Rivets: 20-25 mm dia, 900°C hot-driven |
| Electronic PCB assembly | Soft soldering | Low temperature (183-250°C), no component damage | Sn63/Pb37 or SAC305, 250°C iron tip |
| Thin sheet metal ductwork | Resistance spot welding | Fast, no filler, no fumes, automated | 5-8 kA, 8-15 cycles, 2-4 kN force |

## Troubleshooting Common Joint Failures

| Failure Mode | Probable Cause | Diagnostic Method | Solution |
|-------------|---------------|-------------------|----------|
| Weld cracking (solidification) | High restraint, incorrect filler, or fast cooling | Visual inspection under magnification; magnetic particle testing | Preheat to 100-200°C; select matching filler composition; use low-hydrogen electrodes (E7018 for steel) |
| Porosity in arc welds | Contaminated surface, wet electrode, or inadequate shielding | Radiographic inspection; cross-section metallography | Clean to bright metal; bake electrodes at 120°C for 1 hour; verify gas flow (10-20 L/min) |
| Incomplete penetration | Insufficient current, wrong joint prep, or too-fast travel | Cross-section macroetch; bend testing of qualification coupons | Increase current 10-15%; open root gap to 1-3 mm; slow travel speed |
| Brittle joint (brazed) | Overheated filler, incorrect clearance, or flux residue | Tap test (brittle joint sounds dead vs. ringing); bend testing | Maintain joint clearance 0.05-0.15 mm; heat to flow temperature only (620-780°C for silver braze); clean flux residue promptly |
| Solder joint failure (cold joint) | Insufficient heat, contaminated surfaces, or movement during solidification | Visual: dull/grainy appearance instead of shiny smooth | Clean surfaces to bare metal; heat both parts before applying solder; hold still during cooling |
| Rivet loosening in service | Vibration loosening, corrosion, or thermal cycling | Tap test with 200 g hammer: dull thud = loose | Replace loose rivets with hot-driven rivets; ensure plate contact <0.3 mm gap; apply sealant between plates |
| Resistance spot weld expulsion | Surface contamination, insufficient electrode force, or excessive current | Visual: metal splash around weld; cross-section shows voids | Clean surfaces; increase force to 3-8 kN; reduce current by 10-15% |
| Diffusion bond voids | Surface roughness >0.4 μm Ra, oxide contamination, or insufficient pressure | Ultrasonic C-scan; cross-section metallography | Polish to Ra ≤ 0.4 μm; sputter clean immediately before bonding; increase pressure to 5-10 MPa |
| Tungsten inclusion (TIG) | Electrode touched weld pool | Visual under magnification; radiography | Maintain 1-3 mm arc length; replace contaminated electrode; keep filler rod angled away from tungsten |

## Safety Considerations by Method

Metal joining processes share common hazards (burns, eye injury, toxic fumes) but each method adds specific dangers that require method-specific controls.

### Universal Hazards (All Methods)

- **Burns**: Molten metal, hot workpieces, and heated tools cause burns. Minimum safe handling temperature: 60°C (skin damage begins at 44°C with prolonged contact). Use tongs, leather gloves, and pliers for all hot work. Allow welded parts to cool below 60°C before handling without heat-resistant gloves (this takes 20-60 minutes for typical structural joints depending on thickness).
- **Eye injury**: Flying sparks, grinding debris, and chipping slag cause corneal abrasions and permanent vision damage. Safety glasses with side shields are the minimum protection for any joining operation. Face shields are required for grinding, chipping, and overhead welding.
- **Fire**: Sparks and hot slag travel 5-10 meters from the work zone and smolder in combustible materials for 30+ minutes before igniting. Clear a 10-meter radius of combustibles, or cover with fire-resistant blankets. Maintain fire watch for 30 minutes after hot work stops.

### Arc Welding Specific Hazards

- **Arc radiation (UV/IR)**: The welding arc emits intense ultraviolet and infrared radiation. Unprotected exposure for even a few seconds causes welder's flash (photokeratitis), a painful corneal inflammation that feels like sand in the eyes and lasts 12-24 hours. Wear a welding helmet with shade 10-13 filter (shade selection depends on current: shade 10 for <100A, shade 12 for 100-300A, shade 14 for >300A). Protect nearby workers with screens or curtains.
- **Toxic fumes**: Welding fumes contain metal oxides. Hexavalent chromium (Cr VI) from stainless steel welding is a confirmed carcinogen with an OSHA exposure limit of 5 μg/m³. Zinc oxide fume from galvanized steel causes metal fume fever (flu-like symptoms: chills, fever, nausea, muscle aches) 4-8 hours after exposure. Manganese fume from carbon steel welding causes neurological damage with chronic overexposure. Use local exhaust ventilation at the arc, positioned 100-200 mm from the weld zone, drawing 2-4 m³/min.
- **Electrical shock**: Arc welding power supplies deliver 20-50V open circuit at 100-400A. Wet conditions, damaged cables, or poor grounding create paths for current through the welder's body. 30 mA across the chest causes ventricular fibrillation. Keep cables dry, inspect insulation before each use, ground the workpiece, and never weld in wet conditions or while standing on wet surfaces.

### Resistance Welding Specific Hazards

- **Pinch/crush**: Electrodes close with 1-8 kN force. Finger amputations occur when operators reach between tips. Two-hand anti-tie-down controls are mandatory on manual spot welders: both hands must be on controls to close the electrodes, and releasing either hand must immediately open them.
- **Expulsion (metal splash)**: Molten metal droplets eject from the weld interface at unpredictable intervals. Droplets cause eye injuries and burns at 2-3 meters distance. Face protection is mandatory during manual spot welding.

### Radiant Heat Joining (Brazing, Soldering)

- **Lead exposure**: Soft solder historically contains lead (Sn63/Pb37). Lead fume generation at soldering temperatures (below 250°C) is minimal, but hand-to-mouth contact with lead oxide residues causes cumulative lead poisoning. Wash hands after soldering. Modern lead-free solders (SAC305: Sn96.5/Ag3.0/Cu0.5) eliminate this hazard but require higher temperatures (217-220°C liquidus vs. 183°C for Sn-Pb).
- **Flux fumes**: Brazing flux containing borax, boric acid, or fluorides generates irritating fumes at brazing temperatures (870-950°C). Fluoride flux fumes cause bone damage (fluorosis) with chronic exposure. Use local exhaust ventilation.

### High-Energy Joining (Electron Beam, Laser)

- **X-ray radiation (EBW)**: Bremsstrahlung X-rays generated when 30-150 kV electrons strike the workpiece. At 150 kV, X-rays penetrate thin steel. Interlocked radiation shielding and annual surveys with calibrated radiation detectors are mandatory. Personnel wear dosimeter badges.
- **Laser eye damage**: Fiber laser radiation (1.06 μm) passes through the cornea and focuses on the retina, causing irreversible burns from scattered reflections. Class 4 laser enclosures with interlocked doors and laser-specific safety glasses (OD 5+ at 1.06 μm) are mandatory. The hazard extends to reflected beam paths meters from the workpiece.

## Cross-References

- [Iron & Steel](../metals/iron-steel.md) — primary metals for welding
- [Specialty Alloys](../metals/alloys.md) — alloy weldability and filler metals
- [Electricity](../energy/electricity.md) — power for arc welding processes
- [Chemistry Index](../chemistry/index.md) — flux chemistry and shielding gases
- [Steam Power](../energy/steam-power.md) — boiler fabrication with welded joints
- [Metal Forming](../metals/forming.md) — shaping before joining
- [Machining](machining.md) — post-weld finishing and repair

---

*Part of the [Bootciv Tech Tree](../index.md) · [Machine Tools Bootstrap](./index.md) · [All Domains](../index.md)*