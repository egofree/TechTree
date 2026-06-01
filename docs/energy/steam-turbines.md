# Steam Turbines

> **Node ID**: energy.steam-power.steam-turbines
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.steam-power`](steam-power.md), [`machine-tools.machining`](../machine-tools/machining.md), [`metals.alloys`](../metals/alloys.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 20-35
> **Outputs**: turbine_power, electrical_generation, rotary_power
> **Critical**: Yes — steam turbines are the dominant prime mover for large-scale electricity generation; no practical alternative exists for utility-scale power above 50 MW

Steam turbines replace reciprocating engines for power generation by converting the thermal energy of expanding steam directly into continuous rotary motion. No pistons, no crankshaft, no valve gear — just rows of blades spinning in a steam flow. They operate at far higher speeds and efficiencies than any reciprocating steam engine, and they are the reason large-scale electrical generation became practical. A single turbine-generator unit can deliver 50-500+ MW at 30-40% thermal efficiency, dwarfing the 5-15% efficiency and 1000-5000 HP ceiling of triple-expansion engines.

## Impulse Turbines (De Laval)

**Principle**: Steam expands entirely through stationary nozzles, converting pressure energy into kinetic energy (high-velocity jet). The jet impinges on bucket-shaped blades on the rotor. All pressure drop occurs at the nozzle — the rotor blades experience only the impulse (momentum transfer) of the jet. No pressure drop across the moving blades; the rotor casing operates at essentially atmospheric pressure.

**Construction**:
- **Nozzle**: Converging-diverging (de Laval) nozzle shape for supersonic steam velocities. Machined from bronze or steel. Steam exits at 500-1200 m/s depending on inlet conditions.
- **Rotor**: Single disc with bucket-shaped blades around the perimeter. Blades have a splitter ridge that divides the jet, redirecting each half ~165° for maximum momentum transfer.
- **Speed**: Single-stage impulse turbines run at 10,000-30,000 RPM. This is far too fast for direct generator coupling — requires reduction gearing (helical or epicyclic gears, 10:1 to 50:1 ratio).
- **Applications**: Small units (0.5-10 MW) for industrial power, marine propulsion (turbo-electric drives), and mechanical drives (compressors, pumps).

**Multi-stage impulse (Curtis / Rateau)**:
- Single-stage impulse wastes energy — the exhaust jet still carries significant velocity. Multi-stage designs arrange multiple rows of nozzles and blades in series.
- **Curtis staging**: Velocity-compound — one nozzle feeds a row of moving blades, then a row of fixed guide blades redirect the steam into a second row of moving blades on the same disc. Extracts more energy per disc but adds complexity.
- **Rateau staging**: Pressure-compound — multiple nozzles in series, each expanding the steam through a pressure drop, each feeding its own row of moving blades. Each row runs at lower steam velocity than a single-stage design.
- **Combined**: Large turbines use Curtis stages at the high-pressure end (compact, handle high energy density) and Rateau stages for intermediate and low-pressure sections.

**Strengths**:
- Simple rotor design — no pressure differential across blades, reducing thrust bearing loads
- Nozzle-based design allows partial admission (only some nozzles active) for efficient operation at reduced load
- Multi-stage designs (Curtis, Rateau) extract far more energy per unit than single-stage impulse

**Weaknesses**:
- Single-stage requires 10,000-30,000 RPM — reduction gearing is mandatory for generator coupling
- Multi-stage designs require precision-machined blade profiles and nozzle clearances (tolerances ±0.1 mm)
- No casing pressure seal needed for pure impulse, but multi-stage designs lose this advantage

## Reaction Turbines (Parsons)

**Principle**: Steam expands through both stationary guide blades (nozzles) AND rotating blades. The rotating blades act as moving nozzles — pressure drops continuously across both fixed and moving rows. The rotor is pushed both by impulse (velocity change) and reaction (pressure difference across the blade).

**Construction**:
- **Blading**: Alternating rows of fixed stator blades (mounted in the casing) and moving rotor blades (mounted on the rotor disc or drum). Each blade row has an airfoil profile optimized for the local steam conditions.
- **Rotor**: Drum-type (long cylinder with blades mounted along its length) or disc-type (individual discs shrunk onto a shaft). Drum-type handles thermal expansion better for large units.
- **Casing**: Heavy cast or fabricated steel shell containing the stator blades. Must withstand full steam pressure at the HP inlet.
- **Speed**: 1,500-3,600 RPM (direct drive to 50/60 Hz generators is practical). Lower speed than impulse because each stage extracts only a fraction of the energy — many stages in series.

**Multi-stage design**:
- A typical large turbine has 20-50 stages. Steam conditions progress from high-pressure, high-temperature, low-volume at the inlet to low-pressure, low-temperature, high-volume at the exhaust.
- **HP section**: Small blade heights (50-150 mm), high pressure (10-100+ bar), high temperature (400-540°C). Materials: 12% chromium steel or austenitic stainless.
- **IP section**: Medium blade heights (200-400 mm), moderate conditions. Materials: chromium-molybdenum steel.
- **LP section**: Very long blades (300-1200 mm, last-row blades are the longest precision blades ever manufactured), near-vacuum exhaust (0.05-0.1 bar absolute). Materials: precipitation-hardened stainless steel or titanium for last-row blades.
- **Double-flow LP**: The low-pressure section is often split into two flows (steam enters the center and exits both ends) to keep blade lengths manageable and reduce thrust bearing loads.

**Strengths**:
- Direct-drive to 50/60 Hz generators at 1,500-3,600 RPM — no reduction gearing needed
- Highest peak efficiency of any steam turbine type (80-94% stage efficiency)
- 20-50 stages extract nearly all available energy from the steam expansion

**Weaknesses**:
- Requires pressure-tight casing — casing must withstand full steam pressure at HP inlet (10-100+ bar)
- Thrust bearings must handle significant axial force from pressure differential across rotor discs
- LP last-row blades (300-1200 mm) are among the longest precision-machined components in manufacturing

## Impulse-Reaction Combination

Modern utility turbines use impulse stages at the HP end and reaction stages in the LP end:
- **HP impulse stages**: High steam density means partial admission (only some nozzle arcs are open) is efficient — impulse handles this well. Impulse stages are shorter and more robust against erosion from water droplets in the steam.
- **LP reaction stages**: Steam volume is enormous — full admission across the entire annulus. Reaction blading provides better efficiency at large volume flows and lower pressures.
- **Transition**: The crossover from impulse to reaction is gradual — intermediate stages often have a mix of characteristics.

## Condenser Systems and Feedwater Heating

### Surface Condenser

**[Surface condenser](../glossary/surface-condenser.md)** (standard for power generation):

Exhaust steam enters a shell-and-tube heat exchanger positioned directly below the turbine exhaust. The shell is a cylindrical or box-shaped steel vessel rated for full vacuum (external pressure of ~1 bar). Inside, thousands of tubes (20-30 mm OD, 0.5-1.0 mm wall thickness, brass, cupro-nickel, or titanium) carry cooling water. Steam condenses on the tube outer surfaces, dripping to a hotwell for recovery as feed water.

- **Vacuum**: The condenser operates at 0.03-0.1 bar absolute pressure (96-97% vacuum). This low exhaust pressure is what makes condensing turbines so much more efficient than non-condensing types — the pressure ratio across the turbine increases from perhaps 10:1 (exhaust to atmosphere) to 100:1 or more (exhaust to vacuum). Each 1 kPa reduction in exhaust pressure improves turbine output by roughly 0.5-1% of rated power. Improves efficiency by 8-12 percentage points.
- **Cooling water**: River water, sea water, or cooling tower circulation. Flow rate: ~50-100 m³ per MW of turbine output. Temperature rise across condenser: 8-12°C. Cooling water inlet temperature must be 10-20°C below the steam saturation temperature at the desired condenser vacuum. For a condenser operating at 5 kPa absolute (saturation temperature 33°C), cooling water inlet should be at 15-20°C.
- **Air ejector system**: Non-condensable gases (air leaking through shaft seals, gases dissolved in feedwater) accumulate in the condenser and degrade vacuum. A two-stage steam jet air ejector is the standard removal method. The first stage pulls the air-steam mixture from the condenser, compresses it, and condenses the steam in an inter-aftercondenser. The second stage compresses the remaining non-condensables to atmospheric pressure for venting. Mechanical vacuum pumps (liquid ring type) are an alternative where motive steam is scarce.
- **Condensate return**: Condensed steam collects in the hotwell as pure, deaerated water at near-boiling temperature. Condensate extraction pumps (typically two in parallel, one standby) pump this water forward through the feedwater heating chain back to the boiler. Returning hot condensate saves 10-15% on boiler fuel compared to cold makeup water. Condensate purity is monitored continuously: a conductivity increase indicates a cooling water tube leak (cooling water contamination would cause boiler scale and corrosion).

### Condenser Tube Materials

| Cooling Water Source | Tube Material | Reason | Life Expectancy |
|---------------------|--------------|--------|-----------------|
| Freshwater (river, lake) | Admiralty brass (71Cu-28Zn-1Sn) | Good corrosion resistance, reasonable cost | 15-25 years |
| Brackish water | 90-10 cupro-nickel | Superior resistance to chloride pitting | 20-30 years |
| Seawater | 70-30 cupro-nickel or titanium | High resistance to saltwater corrosion and erosion | 25-40+ years |
| Cooling tower (treated) | Stainless steel (304L or 316L) | Resists corrosion from concentrated chemistry | 20-30 years |

Titanium condenser tubes are increasingly standard for seawater-cooled plants despite 3-5× higher material cost — their corrosion resistance eliminates the periodic retubing that brass and cupro-nickel require.

### Regenerative Feedwater Heating

Regenerative feedwater heating is the single most impactful thermal efficiency improvement available to a steam power cycle — adding 8-12 percentage points of efficiency with no change to the boiler or turbine design.

**Principle**: Rather than sending all the steam through the turbine to the condenser (where its remaining energy is wasted to cooling water), bleed steam from intermediate turbine stages to preheat the boiler feedwater through a cascade of shell-and-tube heaters. Each heater uses steam at a progressively higher pressure and temperature.

**Typical feedwater heating train** (for a 300 MW reheat unit):
1. **LP heaters** (3-4 units): Bleed steam from LP turbine stages. Heat condensate from ~35°C (condenser hotwell) to ~130°C. Drain cascades forward to the condenser.
2. **Deaerator** (direct-contact heater): Feedwater is sprayed into a vessel filled with steam bled from the IP exhaust. The steam heats the water to saturation (~170-180°C at 8-10 bar) and strips dissolved oxygen to <7 ppb (parts per billion). Dissolved oxygen is the primary cause of boiler tube corrosion — deaeration is mandatory.
3. **HP heaters** (2-3 units): Bleed steam from HP and IP turbine stages. Heat deaerated feedwater from ~180°C to ~250-280°C before it enters the boiler economizer. Drain cascades backward to the deaerator.

**Terminal temperature difference (TTD)**: The difference between the bleed steam saturation temperature and the feedwater outlet temperature. Design TTD: -1 to +3°C (negative TTD is possible in heaters with a desuperheating zone that uses the superheat in the bleed steam). Lower TTD = higher efficiency but larger (more expensive) heater.

**Heat balance impact**: Without feedwater heating, a 100 bar, 540°C steam cycle achieves ~33% thermal efficiency. With 7 stages of regenerative heating raising final feedwater temperature to 260°C, efficiency rises to ~41% — a 24% improvement in fuel economy. The turbine loses perhaps 15-20% of its gross power to bleed steam extraction, but the boiler saves 30-35% on fuel input.

### Condenser Performance Monitoring

- **Heat transfer coefficient**: Calculate from condenser duty, log-mean temperature difference, and tube surface area. Design value: 2,500-4,000 W/(m²·K) for clean tubes. Degradation below 70% of design indicates fouling requiring cleaning.
- **Tube leak detection**: Conductivity monitoring of condensate (target <0.2 µS/cm). Sudden increase indicates tube leak. Confirm by dosing fluorescent dye into cooling water and checking condensate with UV light.
- **Air ingress detection**: Monitor dissolved oxygen in condensate. Target: <10 ppb at deaerator outlet. Increasing dissolved oxygen at condenser extraction pump discharge indicates air leaking into the condenser (typically through turbine shaft seals, expansion joints, or valve packing). Locate leaks with helium leak detector (mass spectrometer sniffing for helium sprayed on suspect joints externally).

## Blade Materials

Blades operate under extreme conditions — centrifugal stress, steam erosion, corrosion, and thermal cycling:
- **HP blades (400-565°C)**: 12-25% chromium martensitic stainless steel (AISI 422 or similar). The chromium provides oxidation resistance and hardenability. Creep resistance is the critical property: the blade must not slowly elongate under centrifugal stress at operating temperature. Precipitation-hardening grades (17-4PH) for highest-stress locations. For temperatures above 565°C, austenitic stainless steels or nickel-based alloys are required.
- **IP blades (200-400°C)**: Chromium-molybdenum steel (1-2.25% Cr, 0.5-1% Mo). Good strength, fatigue resistance, and oxidation resistance. The molybdenum contributes to creep strength.
- **LP last-row blades**: Precipitation-hardened stainless steel or titanium alloy (Ti-6Al-4V). Titanium preferred for the longest blades (>900 mm) because its density (4430 kg/m³) is roughly half that of steel (7850 kg/m³), halving the centrifugal load for the same blade geometry. Titanium also has excellent resistance to water-droplet erosion, which is severe in the wet-steam environment of the LP exhaust.
- **Erosion protection**: LP blades suffer erosion from water droplets condensing in the expanding steam. Hard-facing (stellite, tungsten carbide) on leading edges extends blade life. Moisture-recovery stages (water extraction slots in the casing) reduce the problem upstream.

## Blade Manufacturing Process

Turbine blades are among the most precisely manufactured metal components in any industry. The manufacturing method depends on the blade's operating conditions, geometry complexity, and production volume.

### Forging and Machining (HP and IP Blades)

For blades operating below 540°C with relatively simple airfoil profiles, forged and machined construction is standard:

1. **Blank preparation**: Cut bar stock of the specified alloy (12Cr martensitic stainless for HP, Cr-Mo steel for IP) to rough length. Heat to forging temperature (1050-1150°C for martensitic stainless) and upset or roll-forge in closed dies to rough airfoil shape. Forging grain flow follows the blade contour, improving fatigue strength by 20-30% over machined-from-bar alternatives.
2. **Normalizing and tempering**: Heat to 950-1050°C (austenitizing), air cool, then temper at 650-700°C to achieve final hardness (HRC 28-35 for HP blades). This heat treatment develops the martensitic structure that provides creep resistance.
3. **Rough machining**: Turn root platform and shroud (if present) on a lathe. Rough-mill airfoil profile to within 0.5 mm of final dimensions using 4- or 5-axis CNC milling — see [Machining](../machine-tools/machining.md).
4. **Finish machining**: Profile-grind the airfoil to final dimensions using formed grinding wheels or continuous-path CNC creep-feed grinding. Tolerance: ±0.01 mm over the entire airfoil surface. Surface finish: Ra 0.4-1.6 μm.
5. **Root machining**: Wire-EDM (electrical discharge machining) or broach the fir-tree root form to ±0.01 mm tolerance. Each serrated tooth must be identical to distribute centrifugal load evenly.

### Precision Investment Casting (HP Blades with Internal Cooling)

For blades requiring complex internal cooling passages (operating above 540°C in supercritical units), [investment casting](../machine-tools/casting.md) is the only practical manufacturing method:

1. **Wax pattern injection**: Inject molten wax (paraffin-microcrystalline blend, 60-80°C) into an aluminum die at 0.1-0.3 MPa. The die contains a soluble wax or ceramic core that defines the internal cooling passage geometry — serpentine channels, pin-fin arrays, and film-cooling holes. Core positioning tolerance: ±0.05 mm.
2. **Pattern assembly**: Attach individual blade patterns to a central wax sprue (runner tree). Typical tree: 5-25 blade patterns depending on size.
3. **Ceramic shell building**: Dip the tree in fine ceramic slurry (colloidal silica binder + zircon flour, 200-325 mesh), stucco with zircon sand. Repeat for 5-7 coats, each drying 2-4 hours. Final shell thickness: 6-12 mm. The shell must withstand molten superalloy at 1500-1600°C.
4. **Dewax and burnout**: Heat to 100-200°C to melt and drain wax (recovered for reuse). Then fire to 800-1000°C for 1-2 hours to burn out residual organics and sinter the ceramic shell to full strength.
5. **Casting**: Pour molten superalloy into the preheated shell (600-900°C). For directionally solidified (DS) blades, the shell is withdrawn from a furnace at a controlled rate (2-10 mm/min) through a steep thermal gradient, producing columnar grains aligned with the blade's centrifugal stress axis. For single-crystal (SX) blades, a helical grain selector at the base ensures only one crystal propagates into the blade — no grain boundaries at all, eliminating the need for grain-boundary-strengthening elements (hafnium, boron, zirconium).
6. **Shell removal and finishing**: Break away ceramic shell. Dissolve the internal core with alkaline solution (NaOH or KOH). Cut blades from the tree. Grind gate stubs flush.

### Superalloy Selection by Temperature

Blade material selection follows the operating temperature. See [Refractory & Specialty Metals](../metals/refractory-specialty.md) for detailed alloy properties.

| Temperature Range | Alloy Class | Example Alloys | Key Properties |
|-------------------|-------------|----------------|----------------|
| 400-540°C | 12Cr martensitic stainless | AISI 422, H46 | Good creep strength, oxidation resistance, proven service history |
| 540-600°C | Austenitic stainless / PH grades | 17-4PH, A286 | Precipitation-hardened, higher creep strength than martensitic |
| 600-750°C | Iron-nickel superalloys | Inconel 718, A-286 | Gamma-prime precipitation hardening, excellent fatigue resistance |
| 750-950°C | Nickel-based superalloys (equiaxed) | Inconel 738, Udimet 500 | Cast blades, gamma-prime volume fraction 40-60% |
| 950-1050°C | Nickel-based superalloys (DS/SX) | CMSX-4, PWA 1484 | Single crystal, no grain boundaries, 2-3× creep life of equiaxed |
| 1050°C+ | Nickel-based with thermal barrier coating (TBC) | CMSX-4 + YSZ coating | Ceramic coating (yttria-stabilized zirconia, 150-300 μm) insulates metal surface by 100-150°C |

**Directional solidification vs. conventional casting**: DS blades cost 2-3× more than equiaxed castings but last 2-5× longer in service because columnar grains aligned with the stress axis eliminate transverse grain boundaries — the primary creep crack initiation sites. Single-crystal blades cost 5-10× more but eliminate all grain boundaries, offering the highest creep rupture life. For a bootstrap civilization, equiaxed investment-cast blades in nickel superalloy represent the practical first step; DS and SX are targets for process refinement.

### Root Attachment Design

The blade root (fir-tree or dovetail) carries the full centrifugal load — a last-row LP blade at 3,600 RPM experiences 10,000-25,000 g at the root. The fir-tree design distributes this load across 3-6 pairs of interlocking serrated contact faces, each machined to ±0.01 mm. The blade slides axially into the disc groove and is locked by a small pin or peened tab. Contact face pressure must not exceed the material's yield strength at operating temperature — typically limited to 400-600 MPa for martensitic stainless at 500°C.

### Blade Profile Grinding and Inspection

The airfoil profile must match design intent within ±0.01 mm. Deviations cause:
- Flow separation → local efficiency loss (0.5-1% per blade row)
- Local stress concentrations → premature fatigue cracking
- Altered natural frequency → risk of resonance vibration

**Grinding process**: Creep-feed grinding on 5-axis CNC machines using cubic boron nitride (CBN) or aluminum oxide wheels. Wheel speed 25-35 m/s. Feed rate 50-200 mm/min. Coolant: water-soluble oil at high flow. Surface finish: Ra 0.4-1.6 μm.

**Inspection**: Coordinate measuring machine (CMM) with ±0.005 mm accuracy, or optical comparator against master profile template. Every blade is measured — not statistical sampling. Blades outside tolerance are reworked or scrapped.

### Surface Finishing for Erosion Resistance

LP blades suffer water-droplet erosion from condensing steam. Protection methods:
- **Stellite hard-facing**: Cobalt-chromium-tungsten alloy (Stellite 6 or 12) welded or laser-clad onto leading edges. Hardness HRC 40-50. Adds 0.5-1.5 mm thickness. Most common industrial practice.
- **Shot peening**: Bombard blade surface with steel or glass shot (0.2-0.8 mm diameter) at controlled intensity (Almen A scale 0.15-0.40 mm). Creates compressive residual stress layer 0.1-0.3 mm deep that resists crack initiation. Applied to all blade surfaces, not just leading edges.
- **Titanium last-row blades**: Ti-6Al-4V has natural erosion resistance 3-5× superior to steel, plus half the density (4430 vs 7850 kg/m³) — centrifugal stress is halved, enabling longer blades for the same disc loading.

## Rotor Balancing

Steam turbine rotors spin at 1,500-3,600 RPM (direct-drive generators) or 10,000-30,000 RPM (single-stage impulse units). Even small mass imbalances produce enormous centrifugal forces at these speeds: a 1 gram offset at 100 mm radius at 3,600 RPM generates ~14 N of rotating force, enough to excite vibration in the entire turbine-generator foundation. Precision balancing is mandatory.

### Static vs. Dynamic Balance

- **Static imbalance**: The rotor's center of mass is offset from the geometric axis. The rotor will always rotate to rest with the heavy spot at the bottom. Corrected by adding or removing mass in a single plane.
- **Dynamic (couple) imbalance**: The rotor has equal-and-opposite mass offsets at different axial positions. Static balance is fine, but the rotor wobbles when spinning — like an unbalanced car wheel. Requires correction in two separate planes. All multi-stage turbine rotors have both static and dynamic imbalance.

### Balancing Procedure

1. **Low-speed balancing** (500-800 RPM, well below first critical speed): Mount the rotor on soft-bearing balancing machine. The machine measures vibration amplitude and phase at each bearing. Two correction planes are used (typically near the first and last disc). The machine calculates the required correction mass and angular position for each plane. Add mass by welding or bolting weights to the disc rims, or remove mass by drilling. Target: residual imbalance ≤ 25 g·mm per kg of rotor mass (ISO 1940 G2.5 grade for turbine rotors).

2. **High-speed balancing** (at or above operating speed): After low-speed balance, spin the rotor in a high-speed balancing bunker (reinforced concrete cell) at operating speed (1,500-3,600 RPM) and at overspeed (110-120% of operating speed). Measure vibration at multiple speeds to detect any speed-dependent behavior (thermal bow, oil whirl resonance). For large rotors (>10 tonnes), this is done in a vacuum chamber to eliminate windage heating.

3. **Overspeed test**: Every rotor is spun to 120% of rated speed for 1-3 minutes to verify structural integrity. This proves that blades will not liberate at operating speed with normal margins. Overspeed testing is done in a bunker — a rotor burst at 120% speed produces fragments with kinetic energy comparable to artillery shells.

4. **Field trim balancing**: After installation, vibration may differ from shop conditions due to foundation stiffness, alignment, and thermal effects. Trim balance weights are added or adjusted based on field vibration measurements at operating temperature and load. Typical field balance criterion: shaft vibration ≤ 50 μm peak-to-peak at bearing locations, or bearing housing vibration velocity ≤ 2.5 mm/s RMS.

### Critical Speeds

A turbine rotor has multiple natural frequencies (critical speeds). The operating speed must be sufficiently separated from any critical:
- **Rigid rotor**: Operating speed below the first bending critical. Typical for short, stiff rotors (small turbines).
- **Flexible rotor**: Operating speed above the first (and possibly second) bending critical. Standard for large utility turbines. The rotor passes through critical speeds during startup — vibration peaks sharply at each critical. Startup procedures specify maximum hold times at critical speeds (typically 5-10 seconds maximum dwell) to avoid exciting resonance.
- **Design margin**: Critical speeds should be at least ±15% separated from operating speed. For a 3,600 RPM turbine, no critical should occur between 3,060-4,140 RPM.

### Rotor Construction Types

- **Disc-on-shaft**: Individual forged discs with machined blade grooves, shrunk onto a central shaft with interference fit (0.05-0.15 mm diametral interference). Each disc is balanced individually before assembly. Standard for HP and IP rotors.
- **Drum rotor**: Solid forged cylinder with blade grooves machined directly into the surface. Lighter and stiffer than disc-on-shaft. Used for reaction turbines with many stages of small blade height. Monoblock forging up to 10 tonnes requires large steelmaking capability — see [Steelmaking](../metals/steelmaking.md).
- **Welded rotor**: Multiple forged discs welded together (narrow-gap TIG or electron beam welding). Combines the advantages of disc construction (smaller forgings, individually inspectable) with the structural continuity of a drum. Used for LP rotors where disc shrink fits risk loosening under centrifugal load.
- **Bolted construction**: Flanged connections between disc sections, secured by high-strength bolts (40-80 bolts per flange, torqued to 70-80% of proof load). Allows disassembly for blade replacement. Used where field maintenance access is important.

## Casing Design

The turbine casing contains the steam pressure, directs flow through the blade path, and supports the stationary (stator) blade rows. It is one of the largest and most stressed pressure vessels in any power plant.

### Casing Configuration

- **Single-shell casing**: One-piece cylindrical or semi-cylindrical casing split horizontally at the rotor centerline (upper and lower halves bolted together). Standard for small and medium turbines (up to ~100 MW). The horizontal joint has 40-200 bolts, each torqued to maintain a seal against full steam pressure at the HP inlet.
- **Double-shell casing**: Inner casing contains the blade path and steam pressure; outer casing provides structural support and thermal insulation. The space between shells is at an intermediate pressure, reducing the pressure differential (and therefore stress) on each shell. Standard for HP sections of large utility turbines (100+ MW) where inlet conditions exceed 100 bar, 540°C.
- **Multi-shell (triple)**: Used for ultra-supercritical units (250+ bar, 600°C+). Each successive shell sees lower pressure and temperature, allowing optimized material selection per shell.

### Casing Materials and Manufacturing

| Section | Conditions | Material | Manufacturing Method |
|---------|-----------|----------|---------------------|
| HP inner casing | 100-250 bar, 480-620°C | Cr-Mo-V cast steel (1.25Cr-1Mo-0.25V or 9-12Cr cast) | Sand casting from [Steelmaking](../metals/steelmaking.md) |
| HP outer casing | Lower ΔP, 300-450°C | Carbon steel casting or fabricated plate | Sand casting or welded fabrication |
| IP casing | 20-50 bar, 300-500°C | Cr-Mo steel casting or carbon steel fabrication | Sand casting |
| LP casing | Near-vacuum (0.03-0.1 bar), 40-80°C | Carbon steel fabrication or cast iron | Welded plate construction |
| Exhaust hood | Vacuum, wet steam | Carbon steel plate, stainless cladding in wet zones | Welded fabrication |

**HP casing casting**: The HP inner casing is one of the largest steel castings in industrial production — a typical 300 MW turbine HP casing weighs 30-60 tonnes as-cast. The [sand casting](../machine-tools/casting.md) process requires:
- Pattern: Large wooden or metal pattern with 1-2% shrinkage allowance, split at the horizontal joint line
- Mold: Green sand or dry sand mold, chemically bonded (furan resin) for dimensional stability
- Pouring: Cast steel at 1580-1620°C, poured through multiple gates to ensure uniform fill of the complex thin-walled sections (30-80 mm wall thickness)
- Feeding: Large risers at thick sections (blade-path diaphragms, flange transitions) to prevent shrinkage cavities
- Heat treatment: Normalize (920-960°C, air cool) and temper (680-720°C) to develop the required creep-rupture properties

**Flange design**: The horizontal joint flange must seal against full steam pressure. Flange width is 200-400 mm, bolted at 100-200 mm pitch. Bolt diameter: 50-150 mm (M50-M150). Each bolt is torqued in a three-pass pattern (first to 30%, then 60%, then 100% of target torque) to ensure even gasket pressure. At operating temperature, differential thermal expansion between bolts and flange reduces bolt tension — high-temperature bolt materials (Cr-Mo-V or nickel alloy) match flange thermal expansion more closely than carbon steel bolts.

**Thermal expansion provisions**: The casing grows 10-20 mm axially and 2-5 mm radially from cold to operating temperature. Sliding feet or flex plates at the support points allow this movement without transferring forces to the foundation. The casing is anchored at one end (usually the exhaust) and slides freely at the other supports. Dead-ended piping connections use expansion bellows or sliding joints.

**Diaphragms and nozzle boxes**: The stationary blade rows (nozzles for impulse stages, stator blades for reaction stages) are mounted in diaphragms — annular rings that locate in grooves in the casing. Diaphragms are typically cast iron with machined blade slots (HP) or fabricated steel with welded blade profiles (LP). The nozzle box at the HP inlet receives boiler steam through the stop and control valves and directs it into the first-stage nozzles.

### Casing Inspection and Maintenance

- **Bolt inspection**: HP casing bolts are inspected every 4-8 years during major overhauls. Ultrasonic testing for internal cracks. Thread inspection for galling or stretch. Replace any bolt that shows signs of creep elongation (>0.2% permanent strain).
- **Joint face inspection**: Check horizontal joint faces for steam cuts (grooves eroded by leaking steam). Light cuts are stoned or lapped flat; deep cuts require in-situ welding and remachining.
- **Casing cracking**: Thermal cycling causes fatigue cracking at stress concentrations (nozzle-box corners, diaphragm groove fillets, drain connections). Inspect with magnetic particle testing (MT) or penetrant testing (PT) during overhauls. Cracks are ground out and weld-repaired with preheat and post-weld heat treatment.

## Bearing Systems

Steam turbine bearings support the rotor (typically 5-50 tonnes for utility units), maintain precise radial and axial positioning, and absorb thrust loads from steam pressure differentials. Bearing design directly determines vibration levels, rotor alignment, and machine reliability.

### Journal Bearings (Radial Support)

The rotor is supported on two (small units) to six (large multi-casing units) journal bearings. Each bearing is a split cylindrical sleeve (top and bottom halves) lined with a thin layer of bearing alloy (babbitt — tin-antimony-copper or lead-antimony-tin alloy, 0.5-3 mm thick) on a steel backing shell.

**Hydrodynamic lubrication**: At operating speed, the journal (rotor shaft) draws oil into the converging wedge between journal and bearing surface. The wedge generates hydrodynamic pressure (10-20 MPa peak film pressure) that completely separates the metal surfaces — the rotor literally floats on a film of oil 10-50 μm thick. There is zero metal-to-metal contact at operating speed. This is why turbine bearings can run for 100,000+ hours without measurable wear.

**Bearing designs**:
- **Plain cylindrical**: Simplest. Good load capacity. Prone to oil whirl instability at light loads.
- **Elliptical (lemon bore)**: Bearing bore is machined with slightly different vertical and horizontal clearances (vertical clearance ≈ 1.5× horizontal). Creates two oil wedges. Suppresses oil whirl. Most common for utility turbines.
- **Tilting-pad (segmented)**: 4-5 independently pivoting pads. Each pad develops its own oil wedge. Extremely stable — no oil whirl. Standard for high-speed, flexible-rotor machines and any application where stability is critical. Higher power loss (10-30% more friction than plain bearings) due to multiple shear surfaces.

**Clearances**: Journal bearing radial clearance is 0.1-0.2% of shaft diameter. For a 300 mm diameter journal: clearance 0.30-0.60 mm diametral. Too tight: high oil temperature, potential wiping (melting babbitt). Too loose: excessive vibration, oil leakage.

### Thrust Bearings (Axial Position Control)

Steam pressure differentials across the rotor discs generate axial thrust — typically 50-500 kN for large turbines, directed toward the generator end. The thrust bearing prevents axial movement and maintains blade-tip clearances.

**Tilting-pad thrust bearing** (Kingsbury / Mitchell type): 6-12 pivoting pads (segments) arranged in a circle. Each pad tilts to form a converging oil wedge. Load capacity: 1.5-4.0 MPa average bearing pressure. For a 500 kN thrust load at 2.5 MPa, pad area = 200,000 mm² — a bearing of roughly 500 mm outer diameter.

**Equalizing linkage**: A system of leveling plates behind the pads distributes load evenly across all pads. Without equalization, pad-to-pad machining variations would concentrate load on the highest pad, causing premature failure.

**Thrust bearing monitoring**: Axial displacement probes (eddy-current proximity sensors) monitor rotor position to within ±0.01 mm. If thrust bearing babbitt temperature exceeds 95°C, or axial displacement exceeds the setpoint (typically ±0.25 mm from normal position), the turbine trips automatically. Thrust bearing failure allows the rotor to shift axially — blades contact stationary parts and the machine destroys itself in seconds.

### Oil System

See [Bearings & Abrasives](../machine-tools/bearings-abrasives.md) for general bearing theory. The turbine oil system is a dedicated, filtered, cooled lubrication circuit:

- **Main oil pump**: Shaft-driven gear pump, delivers oil at 1-3 bar to bearings. Flow rate: 50-200 L/min per bearing depending on size.
- **Auxiliary oil pump**: AC motor-driven pump for startup and shutdown when shaft speed is too low for the main pump. Also AC-powered backup during operation if main pump pressure drops.
- **Emergency oil pump**: DC battery-powered pump — provides minimum bearing lubrication during coast-down if AC power fails. Battery must support 30-60 minutes of coast-down oil flow.
- **Oil coolers**: Shell-and-tube heat exchangers, cooling water on tube side, lubricating oil on shell side. Maintain oil temperature at 40-50°C at bearing outlets. Oil temperature rise across each bearing: 10-20°C.
- **Filters**: Duplex full-flow filters (one in service, one on standby) with 10-25 μm absolute rating. Oil cleanliness target: ISO 4406 16/14/11 or better. Dirty oil causes bearing scoring and servo-valve stiction in the governing system.
- **Oil reservoir**: 2,000-10,000 liters capacity. Equipped with vapor extraction to remove oil mist, level gauge, and sample point for oil analysis.

**Oil selection**: Turbine oil ISO VG 32 or 46 (viscosity 32-46 mm²/s at 40°C). Must have excellent oxidation stability (TOST life > 2,000 hours), rust inhibition, air release properties, and demulsibility (resistance to water emulsion). Oil is sampled monthly for water content (<0.1%), particle count, acid number, and viscosity.

## Governing and Speed Control Systems

The governor is the turbine's primary safety and control system. It maintains constant rotor speed (and therefore constant electrical frequency) under varying load conditions, prevents overspeed on load rejection, and coordinates steam flow with boiler output.

### Mechanical-Hydraulic Governor

Speed sensing begins with centrifugal flyweights mounted on a governor shaft driven from the main turbine rotor (typically via a worm gear at 1/10 to 1/20 of turbine speed). As turbine speed increases, the flyweights swing outward, lifting a sleeve connected to a pilot valve. The pilot valve modulates hydraulic oil pressure to the main steam admission valve servomotor. Proportional control with adjustable droop (typically 4-5% speed drop from no-load to full-load). Self-contained, reliable, no external power required for basic operation.

### Electro-Hydraulic Governor (EHG)

Electronic speed sensor (magnetic pickup on a gear tooth) provides speed signal to an electronic controller, which drives hydraulic servo valves through analog or digital signal processing. The EHG replaces the mechanical flyweight-sensor-pilot-valve chain with electronic sensing and computation, while retaining hydraulic servo actuators for steam valve positioning (hydraulic force is needed to overcome steam pressure forces on the large valve plugs).

**Electronic controller architecture**:
- **Speed sensing**: Magnetic pickup generates a pulse train proportional to shaft speed. Pulse frequency is measured by a counter/timer circuit. Resolution: 0.01% of rated speed (0.15 RPM at 1,500 RPM, 0.36 RPM at 3,600 RPM). Three independent speed channels (two-out-of-three voting) for reliability.
- **PID control**: Proportional-integral-derivative algorithm drives the servo output. The integral term eliminates steady-state speed error; the derivative term dampens oscillations. PID parameters are tuned to the specific turbine-generator's inertia and steam response characteristics — see [Power Electronics](../electronics/power-electronics.md) for electronic control fundamentals.
- **Load reference**: The operator sets a desired load (MW). The controller adjusts steam flow to match while maintaining frequency droop. In frequency-response mode, the turbine automatically adjusts load to support grid frequency.
- **Automatic generation control (AGC)**: Remote setpoint from grid dispatch center adjusts turbine load in real-time to match system demand. Requires telemetry link (serial communication or SCADA).

**Speed regulation accuracy**: For electrical generation, the turbine must maintain speed within ±0.1% to produce AC power at the correct frequency (50.00 ± 0.05 Hz or 60.00 ± 0.06 Hz). This requires a governor with high gain and fast response — the steam valve must begin moving within 50-100 ms of a speed deviation, and reach full travel in 0.3-1.0 second.

**Droop setting**: Governor droop is the percentage speed change from no-load to full-load. A 4% droop means the turbine runs 4% faster unloaded than at rated load. Droop is essential for load sharing between parallel turbines: each turbine picks up load in proportion to its droop setting. Lower droop gives faster response but risks hunting (oscillation). Isochronous (0% droop) mode is possible with electronic governors for single-turbine installations or island operation.

### Overspeed Protection

The last line of defense against runaway — three independent systems:

1. **Overspeed trip bolt**: Independent mechanical bolt mounted on the rotor shaft. At 110-115% of rated speed, centrifugal force flings the bolt outward, tripping a latch that dumps hydraulic oil from the steam valve actuators — valves slam shut under spring force. Test regularly by tripping it electrically at reduced speed.
2. **Electronic overspeed (2/3 voting)**: Three independent speed sensors feed three independent overspeed detectors. If two-of-three detect speed exceeding 110%, the electronic trip system de-energizes the trip solenoid, dumping hydraulic oil and closing all steam valves.
3. **Acceleratory protection**: Detects rate of speed increase (RPM/second). If the rotor is accelerating faster than normal load-rejection characteristics, it trips preemptively before reaching the overspeed setpoint — critical for preventing overspeed during full-load rejection events.

### Steam Valve Arrangement

- **Main stop valve (MSV)**: Trip valve, normally open, closes only on trip signal. Located between boiler and control valves. Full-port design to minimize pressure drop during normal operation.
- **Governor/control valves (GV)**: 4-8 valves arranged around the HP casing, each feeding a separate nozzle arc group. Modulating — position varies from closed to full open under governor control. Partial admission mode (only some valves open) at reduced loads improves efficiency by maintaining higher steam velocity through active nozzle arcs.
- **Interceptor valves (reheat turbines)**: Located between reheater and IP section. Trip-close on overspeed to prevent the large volume of reheat steam from accelerating the rotor after a load rejection.
- **Non-return valves**: Prevent reverse steam flow from the reheat system into the HP exhaust on load rejection.

## Auxiliary Systems

**Lubrication system**: Turbine bearings require forced-feed lubrication at 1-3 bar oil pressure. A main shaft-driven oil pump circulates oil through coolers and filters to the bearings. An auxiliary AC or DC motor-driven pump provides oil pressure during startup and coast-down when the shaft pump is ineffective. Oil temperature maintained at 40-50°C. Bearing metal temperature monitored with thermocouples: alarm at 85°C, trip at 95°C.

**Steam seal system**: Where the rotor shaft exits the casing, labyrinth seals (interlocking fins on the rotor and grooves in the casing) minimize steam leakage. A small amount of sealing steam is supplied at slightly above atmospheric pressure to prevent air ingress into the vacuum section. Gland steam condenser recovers the sealing steam.

## Power Output Ranges

| Size Class | Power Output | Steam Conditions | Application |
|-----------|-------------|-----------------|-------------|
| Small industrial | 0.5-10 MW | 10-40 bar, 300-400°C | Factory cogeneration, mechanical drives |
| Medium utility | 10-100 MW | 40-100 bar, 400-480°C | Regional power plants |
| Large utility | 100-500 MW | 100-165 bar, 480-540°C | Baseload generation |
| Ultra-supercritical | 500-1000+ MW | 250-350 bar, 580-620°C | Most efficient baseload |

## Combined-Cycle Configuration

The combined-cycle power plant is the most thermally efficient fossil-fueled power generation system: a gas turbine (Brayton cycle) topping a steam turbine (Rankine cycle) recovers energy that either cycle alone would waste. Combined efficiency reaches 55-62% (net, LHV basis) — far surpassing any single-cycle steam plant (40-45%) or simple gas turbine (35-42%).

### Heat Recovery Steam Generator (HRSG)

The HRSG is a large heat exchanger that captures exhaust heat from the gas turbine (typically 500-620°C exhaust temperature) to generate steam for the bottoming cycle:

- **Architecture**: Vertical or horizontal tube banks arranged in modules (HP, IP, LP sections). Gas turbine exhaust flows across finned tubes carrying water/steam. No combustion in the HRSG (unfired design) — all energy comes from gas turbine exhaust.
- **Multiple pressure levels**: Modern HRSGs generate steam at three pressure levels:
  - **HP section**: 60-130 bar, 500-565°C superheat. Feeds the HP steam turbine section. Economizer (preheats water) → evaporator (boils water) → superheater (heats steam above saturation). HP steam production: 3-5 kg per kg of gas turbine exhaust flow.
  - **IP section**: 15-40 bar, 300-450°C. Feeds the IP turbine section or provides steam for the reheater. Sometimes includes a reheater that combines cold reheat from the HP turbine exhaust with IP-generated steam.
  - **LP section**: 3-8 bar, 140-250°C. Feeds the LP turbine section. Also provides steam for feedwater deaeration.
- **Once-through vs. drum-type**: Drum-type HRSGs use a steam drum to separate saturated steam from water (like a conventional boiler). Once-through HRSGs pump water through a single continuous tube path from economizer inlet to superheater outlet — no drum, faster startup, better load-following capability, but requires more precise water chemistry control.
- **Supplementary firing**: A duct burner between the gas turbine and HRSG can increase steam production by burning additional fuel in the oxygen-rich exhaust. Increases output by 20-50% but reduces combined-cycle efficiency. Used for peaking service where maximum output matters more than fuel economy.

### Steam Turbine for Combined Cycle

The bottoming-cycle steam turbine differs from conventional utility turbines:

- **No boiler**: Steam comes from the HRSG, not from a dedicated boiler. The turbine has no feedwater heaters of its own (the HRSG economizer sections perform this function). This simplifies the turbine but means the steam conditions are entirely determined by the gas turbine exhaust temperature.
- **Full-arc admission**: Unlike conventional turbines that use partial admission at the HP end for efficiency at part load, the combined-cycle steam turbine always has full admission (steam enters around the entire circumference) because the HRSG supplies all steam at a uniform rate.
- **Triple-pressure admission**: HP steam enters at the front, IP steam is admitted partway through the expansion, and LP steam joins near the exhaust end. The turbine casing has three separate steam inlets.
- **Size relationship**: The steam turbine output is roughly 50-55% of the gas turbine output (for unfired combined cycle). A 200 MW gas turbine produces enough exhaust heat for a 100-110 MW steam turbine, yielding 300-310 MW combined.

### Performance Comparison

| Configuration | Net Efficiency (LHV) | Typical Size | Capital Cost ($/kW) | Start Time |
|--------------|----------------------|--------------|---------------------|------------|
| Simple steam cycle (subcritical) | 33-38% | 100-800 MW | 800-1,200 | 4-8 hours (cold) |
| Simple steam cycle (supercritical) | 40-45% | 400-1,200 MW | 1,000-1,500 | 6-10 hours (cold) |
| Simple gas turbine | 35-42% | 50-400 MW | 300-500 | 10-20 minutes |
| Combined cycle (1×1) | 55-62% | 150-600 MW | 500-800 | 60-120 minutes |
| Combined cycle (multi-shaft) | 55-60% | 300-1,200 MW | 450-700 | 30-90 minutes |

### Bootstrap Implications

Combined-cycle plants require both gas turbine and steam turbine technology. The steam turbine in a combined cycle is simpler than a standalone unit (no boiler, no superheater controls, fewer feedwater heaters) but the overall system requires:
- Gas turbine manufacturing capability (precision airfoil blades, high-temperature materials, combustion engineering)
- HRSG fabrication (large finned-tube heat exchanger, multiple pressure levels, drum or once-through design)
- Integrated control system coordinating gas turbine fuel flow with steam turbine steam conditions

For a bootstrap civilization, the progression is: standalone steam turbine plants first (they can burn any fuel in the boiler), then gas turbines when metallurgy supports turbine inlet temperatures above 1,000°C, then combined cycle as the capstone efficiency improvement.

## Thermal Efficiency

- **Simple non-condensing**: 15-20% (exhausts to atmosphere, no condenser). Simple but wasteful.
- **Condensing turbine**: 30-40% (with condenser vacuum). Standard for power generation.
- **Superheat**: Each 50°C of superheat above saturation improves efficiency by ~2 percentage points.
- **Reheat**: Extract steam after the HP section, route back through the boiler for additional superheating, then return to the IP section. Adds 4-5 percentage points of efficiency.
- **Regenerative feedwater heating**: Bleed steam from intermediate turbine stages to preheat boiler feed water through a series of shell-and-tube heaters. Recovers energy that would otherwise be lost to the condenser. Adds 5-8 percentage points of efficiency.
- **Combined cycle**: Turbine exhaust heat generates steam for a second (bottoming) turbine. Combined efficiencies reach 55-62%.

## Safety and Hazards

- **Overspeed failure**: If the turbine loses its load (generator disconnects) and the governor fails to close the steam valves, the rotor accelerates until centrifugal forces tear the blades from the disc. Blade fragments become lethal projectiles. Prevention: redundant governor systems, tested overspeed trip bolt, regular testing of all protection systems.
- **Steam leaks**: High-pressure steam (100+ bar, 500+°C) leaks from flanges, valve packing, or casing cracks are invisible and instantly fatal. Infrared thermography for leak detection. Regular inspection of all bolted joints. Never approach a pressurized steam turbine without verifying isolation and depressurization.
- **Lubricating oil fires**: Turbine bearings are lubricated with large volumes of oil (hundreds of liters). An oil leak onto hot steam piping ignites spontaneously. Oil-fire detection and suppression systems required. Fire-resistant hydraulic fluids available but expensive.
- **Condenser vacuum failure**: If cooling water flow is lost, vacuum collapses, exhaust pressure rises, and the last LP stages operate in choked, overheated flow. Automatic trip on low vacuum protects the turbine. Never override vacuum trip.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Turbine vibration increasing | Blade loss or erosion, bearing wear, misalignment, thermal bow | Check vibration amplitude and frequency; inspect blades for erosion or cracking; check bearing clearances; verify alignment; if cold, roll rotor slowly to straighten thermal bow |
| Reduced power output at same steam flow | Blade fouling (silica deposits), nozzle erosion, condenser vacuum loss | Inspect blade surfaces through casing openings; clean condenser tubes; check cooling water flow; verify air ejector operation |
| High bearing temperature (>85°C alarm) | Oil flow restriction, oil cooler fouling, bearing damage, excessive load | Check oil pressure and flow; clean oil cooler; inspect bearing babbitt for damage; verify alignment and bearing preload |
| Condenser vacuum degrading | Air leak into condenser, fouled tubes, cooling water flow loss, air ejector failure | Leak test with helium sniffer or vacuum decay; clean condenser tubes; verify cooling water pump operation; inspect air ejector steam supply |
| Overspeed trip activates unexpectedly | Governor malfunction, electrical load rejection, trip bolt fatigue | Test governor response; check electrical breaker coordination; inspect trip bolt for wear; verify hydraulic oil pressure to steam valves |
| Blade cracking in LP stages | Water-droplet erosion fatigue, resonance vibration, corrosion pitting | Inspect last-stage blades for erosion depth (>0.5 mm requires replacement); verify moisture extraction slots are clear; check blade vibration frequency against running speed |
| Steam leak at casing joints | Bolt relaxation from thermal cycling, gasket degradation, casing distortion | Re-torque casing bolts to specification after thermal cycle; replace gaskets; check casing flange flatness with straightedge |
| Turbine fails to reach rated speed | Steam valve not fully open, excessive starting torque, governor set too low | Verify steam admission valve fully open; check driven equipment (generator, pump) for mechanical drag; verify governor speed setting |
| Oil contamination (water or particles) | Steam seal leak into bearing housing, cooler tube leak, filter bypass | Inspect gland steam seals; oil cooler pressure test; replace filter elements; check oil purifier operation |
| Differential expansion trip on startup | Rapid heating rate, insufficient soak time at intermediate temperatures | Follow manufacturer start-up curve: limit temperature ramp to 2-3°C/min; hold at 150°C and 300°C for thermal soaking; verify differential expansion indicators |

## Limitations

- **Water quality requirements**: Boiler feedwater must be highly purified (conductivity <0.2 µS/cm). Dissolved oxygen, silica, and dissolved solids cause corrosion and scale. Extensive water treatment plant required.
- **Start-up time**: Large steam turbines require 4-8 hours from cold start to full load due to thermal expansion constraints. Rapid start-up causes differential expansion and blade rubbing.
- **Blade erosion**: Moisture in low-pressure stages causes erosion of last-stage blades. Water droplets impact blade leading edges at high velocity. Requires stainless steel or Stellite-shielded blade tips.
- **Condenser fouling**: Cooling water fouling (biofilm, scaling, sediment) degrades vacuum and reduces efficiency by 2-5%. Regular tube cleaning required.
- **High capital cost**: Steam turbine plants require boiler, turbine, condenser, feedwater system, and cooling system — complex integrated plant with high upfront investment.
- **Minimum efficient size**: Steam turbines become cost-effective above ~5 MW. Below this, reciprocating steam engines or internal combustion engines are more economical.

## See Also

- [Steam Power](steam-power.md) — boilers providing steam for turbines
- [Electricity Generation](electricity.md) — generators and power distribution
- [Coal](coal.md) — primary fuel for steam turbine plants
- [Water Turbines](water-turbines.md) — hydraulic turbine comparison
- [Cooling Systems](cooling.md) — condenser cooling systems
- [Iron & Steel](../metals/iron-steel.md) — materials for blades and casings
- [Steelmaking](../metals/steelmaking.md) — large steel castings for HP casings and rotor forgings
- [Refractory & Specialty Metals](../metals/refractory-specialty.md) — superalloys for high-temperature blades
- [Metal Casting](../machine-tools/casting.md) — investment casting for blade manufacturing
- [Bearings & Abrasives](../machine-tools/bearings-abrasives.md) — bearing theory, babbitt lining, journal bearings
- [Machining](../machine-tools/machining.md) — precision machining of blade profiles and rotor discs
- [Power Electronics](../electronics/power-electronics.md) — electronic governor controllers and servo systems
- [Electric Furnaces](electric-furnaces.md) — graphite for turbine seals and lubricants
- [Geothermal Energy](geothermal.md) — geothermal flash steam driving turbines

[← Back to Energy](index.md)
