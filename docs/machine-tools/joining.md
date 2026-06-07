# Metal Joining

> **Node ID**: machine-tools.joining
> **Domain**: [Machine Tools Bootstrap](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`energy.electricity`](../energy/electricity.md), [`metals.alloys`](../metals/alloys.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`energy.steam-power`](../energy/steam-power.md), [`machine-tools.joining.diffusion-bonding`](./joining.md), [`machine-tools.joining.electron-beam`](./joining.md), [`machine-tools.joining.friction-stir`](./joining.md), [`machine-tools.joining.laser-welding`](./joining.md), [`machine-tools.joining.mig-welding`](./joining.md), [`machine-tools.joining.resistance-welding`](./joining.md), [`machine-tools.joining.tig-welding`](./joining.md), [`machine-tools.joining.ultrasonic-bonding`](./joining.md)
> **Timeline**: Years 5-70
> **Outputs**: forge_welds, brazed_joints, soldered_joints, riveted_joints, welded_joints, acetylene, tig_welds, mig_welds, resistance_welds, electron_beam_welds, ultrasonic_bonds, friction_stir_welds, laser_welds, diffusion_bonds, hermetic_seals, wire_bonds
> **Critical**: Yes — makes machinery possible by assembling individual parts into structures, mechanisms, and pressure vessels


Metal joining is the capability that makes machinery possible. Individual forged or cast parts are rarely useful alone — they must be assembled into structures, mechanisms, pressure vessels, and frames. Each method occupies a specific niche defined by temperature, joint strength, equipment requirements, and the materials it can join. No single method replaces all others — a complete industrial shop needs all three families.

The three fundamental families of metal joining are:

1. **Fusion welding**: The base metal is melted at the joint. Forge welding, oxy-acetylene, arc welding (SMAW, TIG, MIG), electron beam, laser, and resistance welding all fall in this category. Fusion welding produces the strongest joints (350-550 MPa) but requires the most equipment and generates the most heat distortion.

2. **Filler alloy joining (brazing and soldering)**: A filler metal with a lower melting point than the base metal flows into the joint by capillary action. The base metal never melts, which means dissimilar metals can be joined and heat distortion is minimal. Brazing produces structural-strength joints (150-300 MPa); soldering produces lower-strength joints (20-50 MPa) suitable for electrical and plumbing applications.

3. **Mechanical fastening (riveting)**: No melting of any kind. Rivets are inserted through holes and deformed to clamp the parts together. The simplest and most inspectable joining method, but the most labor-intensive and the only one that weakens the base metal by drilling holes through it.

For the metallurgy of producing iron and steel stock to be joined, see [Iron & Steel](../metals/iron-steel.md). For the electrical infrastructure needed by arc welding, see [Electricity](../energy/electricity.md).

## Articles in this Section

- **[Welding](./welding.md)** — Forge welding, oxy-acetylene welding, SMAW (stick), TIG (GTAW), MIG (GMAW), resistance spot/seam welding, electron beam welding, ultrasonic welding & wire bonding, friction stir welding, laser welding, and diffusion bonding. Covers vacuum chamber fabrication, hermetic sealing, and weld quality inspection.
- **[Brazing & Soldering](./brazing-soldering.md)** — Brass brazing (spelter brazing), silver brazing (hard soldering), and soft soldering. Filler alloy joining where the base metal does not melt. Brazing for structural joints; soldering for electrical connections, plumbing, and sheet metal seams.
- **[Riveting](./riveting.md)** — Hot and cold riveting, joint configurations (lap, butt with cover plates, boiler seams), rivet patterns, and inspection. Mechanical joining with no heat at the joint.

## Bootstrap Progression

A civilization rebuilding its industrial base follows a predictable joining progression:

**Stage 1 — Forge welding and riveting (Years 5-15)**: With a forge and hammer, iron and low-carbon steel can be forge-welded at 1200-1300°C. Rivets require only drilled holes and a forge for heating. These two methods suffice for structural steel (bridges, building frames), boilers, ships, and machine frames. No electricity required. Every medieval-to-19th-century structure was built with forge welding and riveting.

**Stage 2 — Brazing and soldering (Years 5-20)**: Brass brazing requires copper, zinc, borax, and a forge or torch. Soft soldering requires tin, lead, and a simple torch. These enable plumbing, instrument work, electrical connections, and joining dissimilar metals (steel to copper, cast iron repair). Brazing and soldering are achievable as soon as the constituent metals are available.

**Stage 3 — Arc welding (Years 15-40)**: Oxy-acetylene welding requires acetylene generation (calcium carbide + water) and oxygen supply. SMAW (stick welding) requires electricity (50-400A at 20-50V), coated electrodes, and a welding power supply. TIG and MIG follow once tungsten electrodes and wire feed mechanisms are available. Arc welding transforms fabrication speed: a single welder replaces a riveting crew of 4-6 workers.

**Stage 4 — Advanced and precision joining (Years 40-70+)**: Resistance welding (spot, seam) for sheet metal production. Electron beam welding for vacuum chambers and aerospace. Friction stir welding for aluminum alloys. Ultrasonic wire bonding for semiconductor packaging. Laser welding for high-speed automated joining. Each method requires progressively more sophisticated equipment but enables correspondingly more demanding applications.

## Prerequisites by Method

| Method | Required Capabilities | Minimum Industrial Base |
|--------|----------------------|------------------------|
| Forge welding | Forge (charcoal or coal), hammer, anvil | Bloomery iron, basic blacksmithing |
| Riveting | Drill, forge for heating rivets, hammer | Wrought iron or mild steel, drilling capability |
| Brass brazing | Copper, zinc, borax, forge/torch (950°C) | Copper/zinc smelting, borax mining |
| Silver brazing | Silver, copper, zinc, fluoride flux, torch | Silver sourcing, gas torch |
| Soft soldering | Tin, lead, flux, soldering iron/torch (250°C) | Tin/lead smelting |
| Oxy-acetylene welding | Acetylene generator, oxygen supply, torch | Calcium carbide production, gas handling |
| SMAW (stick) | Welding power supply, coated electrodes | Electricity (200A+), electrode coating chemistry |
| TIG (GTAW) | Constant-current power supply, tungsten electrode, argon gas | Tungsten production, argon supply, precision gas flow control |
| MIG (GMAW) | Constant-voltage power supply, wire feed, shielding gas | Wire drawing, gas supply, motorized feed mechanism |
| Resistance welding | High-current transformer, copper electrodes, timer | Heavy electrical infrastructure (10-50 kA), process control |
| Electron beam | Vacuum chamber, electron gun, high-voltage supply (30-150 kV) | High-vacuum technology, precision machining, high-voltage engineering |
| Friction stir | CNC machine, hardened steel tool, force control | CNC machining, high-force spindle, process control |
| Laser welding | Laser source (1-10 kW), beam delivery, shielding gas | Laser technology, precision optics, automation |
| Ultrasonic bonding | Ultrasonic transducer (20-60 kHz), force control | Piezoelectric ceramics, power electronics |
| Diffusion bonding | Hot press, vacuum or inert atmosphere, surface prep | Vacuum furnaces, precision surface finishing (Ra ≤ 0.4 μm) |

## Integration Points

| Phase | Joining Methods Used | Key Structures Built |
|-------|---------------------|---------------------|
| Foundations | Forge welding, riveting | Tools, cart axles, simple bridges |
| Metallurgy | Forge welding, riveting, brass brazing | Bellows, furnace frames, rolling mill stands |
| Machine Tools | Brazing, soldering, early arc welding | Lathe beds, gearboxes, machine frames |
| Energy | Arc welding (SMAW), riveting, brazing | Steam boilers, engine frames, turbine casings |
| Chemistry | Soldering, brazing, TIG welding | Pressure vessels, piping, heat exchangers |
| Vacuum & Optics | TIG, electron beam, diffusion bonding | Vacuum chambers, optical mounts, UHV components |
| Silicon | Ultrasonic bonding, TIG, laser welding | Crystal pullers, wafer handling, process chambers |
| Electronics | Soft soldering, ultrasonic wire bonding, laser | PCB assembly, IC packaging, wire bonding |

## Scaling Notes

Joining production scales from individual craftsmen to automated production lines:

- **Workshop scale** (1-5 operators): Forge, anvil, torch, and a single arc welding station. Brazing and soldering at the bench. All joining methods available but slow. Production: 5-50 joints per hour. This is the bootstrap workshop that builds the first machine tools, engines, and infrastructure.

- **Factory scale** (10-50 operators): Multiple welding stations with dedicated SMAW and MIG stations. Brazing furnaces for batch production. Riveting crew for heavy structural work. Production: 50-500 joints per hour. This scale builds locomotives, bridges, ships, and power plants.

- **Industrial scale** (automated, 100+ operators): Robotic MIG welding cells for automotive frames. Submerged arc welding for ship hulls and pressure vessels. Electron beam welding for aerospace components. Laser welding for high-speed production. Automated soldering (wave soldering) for electronics. Production: 1000+ joints per hour. This scale enables mass production of vehicles, aircraft, electronics, and semiconductor equipment.

**Critical bottleneck**: Welding electrode and filler wire production. SMAW electrodes require core wire (drawn from steel rod), extruded flux coating (rutile, cellulose, or basic limestone-based mixtures with silicate binder), and baking to remove moisture. MIG wire requires precision drawing to 0.8-1.6 mm diameter with consistent feed characteristics. Without quality filler materials, even the best welding equipment produces defective joints.

## Quality Control

Joint quality is verified by increasingly sophisticated methods as the application demands:

1. **Visual inspection** (all methods): The most basic and universal test. Inspect fillet shape, penetration, undercut, porosity, and surface cracks with good lighting and 5-10× magnification. An experienced inspector catches 80-90% of surface defects visually.

2. **Tap testing** (rivets): Strike each rivet with a 200 g hammer. Tight rivets ring clearly; loose rivets produce a dull thud. Train inspectors on known-good and known-bad samples before allowing production inspection.

3. **Dye penetrant testing** (surface cracks): Apply red dye to cleaned joint surface, let sit 10-15 minutes, wipe clean, apply white developer. Surface cracks draw red dye out of the crack and display as bright red lines on white background. Detects cracks as fine as 1 μm wide.

4. **Magnetic particle testing** (ferromagnetic materials only): Magnetize the joint area, spray with iron particles (dry powder or wet fluorescent suspension). Surface and near-surface cracks create flux leakage that attracts particles, forming visible indications. More sensitive than dye penetrant for ferromagnetic materials.

5. **Radiographic inspection** (critical joints): X-ray or gamma-ray exposure of the joint. Voids, porosity, incomplete penetration, and slag inclusions appear as dark spots on the radiograph. Required for pressure vessel longitudinal seams and structural joints in nuclear and aerospace applications.

6. **Ultrasonic testing** (thick sections): High-frequency sound waves (1-10 MHz) reflect from internal defects. A skilled operator maps voids, cracks, and incomplete fusion zones inside thick welds. Required for critical applications where radiography is impractical (very thick sections, field inspections).

7. **Destructive testing** (qualification coupons): Weld test coupons using the same procedure, then bend, tensile-test, and cross-section for metallographic examination. Required for welding procedure qualification (WPQ) before production welding begins.

## See Also

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
- [Brazing & Soldering](./brazing-soldering.md) — filler alloy joining methods
- [Riveting](./riveting.md) — mechanical fastening with rivets
- [Welding](./welding.md) — fusion and solid-state welding processes

---

*Part of the [Bootciv Tech Tree](../index.md) · [Machine Tools Bootstrap](./index.md) · [All Domains](../index.md)*

