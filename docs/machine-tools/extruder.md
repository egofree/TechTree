# Extruder (Single-Screw and Twin-Screw)

> **Node ID**: machine-tools.extruder
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](machining.md), [`energy.electric-motors`](../energy/electric-motors.md)
> **Enables**: [`polymers.thermoplastics`](../polymers/thermoplastics.md), [`polymers.synthetics`](../polymers/synthetic.md), [`chemistry.petroleum`](../chemistry/petroleum-alternatives.md)
> **Timeline**: Years 15-25
> **Outputs**: continuous_profiles, pipe, sheet, film, wire_insulation, pelletized_resin
> **Critical**: Yes — the extruder is the primary machine for processing thermoplastics and many synthetic polymers; no practical substitute for continuous-profile production

## Principle

A rotating screw pushes polymer granules through a heated barrel, melting and compressing them into a homogeneous melt, then forcing the melt through a shaped die to produce a continuous product of constant cross-section. The screw performs three functions in sequence along its length: feeding (conveying solid granules forward), compressing (melting and densifying the polymer), and metering (delivering uniform-pressure melt to the die).

The melt pressure at the die is generated entirely by the screw rotation against the resistance of the die. Output rate is proportional to screw speed and screw diameter. For a single-screw extruder, volumetric output Q ≈ (π² D² N H sin φ cos φ) / 2 — (π D H³ sin² φ ΔP) / (12 η L), where D is screw diameter, N is screw speed (RPM), H is channel depth, φ is helix angle, ΔP is die pressure drop, η is melt viscosity, and L is metering section length. The first term is drag flow (screw-driven); the second is pressure back-flow. A well-designed screw operates with back-flow less than 10% of drag flow.

Twin-screw extruders use two intermeshing screws that provide superior mixing and self-wiping action. Counter-rotating twin screws are used for PVC (heat-sensitive, needs low shear). Co-rotating twin screws are used for compounding (filler dispersion, polymer blending). Twin-screw machines are more complex to build but essential for formulations requiring intimate mixing.

## Prerequisites

- [Steel plate and bar](../metals/iron-steel.md) — for barrel, frame, and drive housing
- [Seamless tubing or bored solid bar](../metals/forming.md) — for barrel bore
- [Machining capability](machining.md) — lathe for screw turning, boring for barrel, milling for frame
- [Electric motor](../energy/electric-motors.md) — 5-100 kW depending on screw diameter
- [Temperature controllers](../electronics/electrical-systems.md) — PID-type, one per heating zone
- [Band heaters](../energy/electric-furnaces.md) — resistive heating elements for barrel

## Materials

### Frame and Drive

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (frame) | 50-200 kg | A36 or equivalent, 10-20 mm thick | [Iron & Steel](../metals/iron-steel.md) | Cast iron frame (heavier, absorbs vibration) |
| Electric motor | 1 | 5-100 kW, 3-phase or DC, 100-1500 RPM | [Electric Motors](../energy/electric-motors.md) | Hydraulic motor (for variable speed without electronics) |
| Gear reducer | 1 | 10:1 to 30:1 ratio, rated to 2× motor torque | [Machine Tools](./index.md) | Belt-and-pulley reduction (less efficient, no sealed lubrication) |
| Bearings | 2-4 sets | Tapered roller, rated to 20 kN thrust + radial | [Bearings](./bearings-abrasives.md) | Bronze sleeve bearings (shorter life, higher friction) |
| Coupling | 1 | Flexible or gear coupling, rated to screw torque | [Machine Tools](./index.md) | Direct keyed connection (no misalignment tolerance) |

### Barrel

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Seamless steel tubing | 1 piece | ID matched to screw OD +0.05-0.15 mm, 10 mm wall, length = L/D × D | [Forming](../metals/forming.md) | Bored solid bar (more machining but better bore quality) |
| Nitriding steel (barrel liner) | 1 piece | 4140 or nitralloy, for bimetallic liner in wear zone | [Iron & Steel](../metals/iron-steel.md) | Hardened tool steel insert (shorter wear life) |
| Band heaters | 3-6 | Ceramic-insulated, 2-5 kW each, 220-480 V | [Electric Furnaces](../energy/electric-furnaces.md) | Cast-in aluminum heaters (better heat transfer, harder to replace) |
| Thermocouples | 3-6 | Type K, 0-400°C range, one per heating zone | [Measurement](../measurement/precision.md) | RTD sensors (more accurate, slower response) |

### Screw

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Alloy steel bar (screw) | 1 piece | 4140 or 4340, 30-120 mm diameter × L/D ratio length | [Iron & Steel](../metals/iron-steel.md) | Hardened stainless steel (corrosive polymers like PVC) |
| Hard-facing weld (flight surfaces) | 0.5-2 kg | Stellite or Colmonoy, applied by welding | [Joining](./joining.md) | Through-hardened screw (uniform hardness, no overlay step) |
| Chrome plating | — | 0.02-0.05 mm hard chrome on finished screw surface | [Electrochemistry](../electrochemistry/index.md) | Polished bare steel (higher friction, more polymer adhesion) |

### Die and Downstream

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Tool steel (die body) | 5-20 kg | P20 or H13, machined to target profile | [Iron & Steel](../metals/iron-steel.md) | Machined mild steel (shorter die life, lower precision) |
| Band heater (die) | 1-2 | 1-3 kW, matched to die geometry | [Electric Furnaces](../energy/electric-furnaces.md) | Gas torch (poor temperature control, not viable for precision) |
| Cooling bath tank | 1 | 2-4 m long, stainless or aluminum, water-cooled | [Metals](../metals/iron-steel.md) | Wooden trough with copper coil (leaks, short life) |

## Construction Steps

### Frame and Drive Assembly

1. **Fabricate frame base**: Cut two C-channel or I-beam steel members (100 × 50 mm, 1.5-2.5 m long depending on screw L/D) for the frame rails. Weld cross-members at 500 mm intervals to create a rigid base. Grind welds flush. The frame must support 200-500 kg of barrel and drive without flexing more than 0.5 mm.

2. **Mount gear reducer and motor**: Bolt gear reducer to one end of the frame with Grade 8.8 bolts. Align output shaft of reducer with barrel centerline using a dial indicator — maximum misalignment 0.05 mm. Mount motor to reducer input (direct-coupled or belt-driven). Install flexible coupling between reducer output and screw shank.

3. **Install thrust bearing**: Mount a tapered roller thrust bearing assembly behind the screw shank. This bearing absorbs the die back-pressure force, which can reach 20-40 MPa × screw cross-sectional area (300-4500 N for 30-120 mm screws). A 60 mm screw at 30 MPa die pressure generates ~85 kN thrust — the bearing must be rated accordingly.

### Barrel

4. **Prepare barrel bore**: If using seamless tubing, hone the ID to 0.8 μm Ra finish or better. Bore diameter must be concentric within 0.02 mm over the full length. If boring from solid bar, rough-bore to within 0.5 mm of finish diameter, stress-relieve at 600°C for 2 hours, then finish-bore and hone. For a 60 mm screw, bore to 60.10 ±0.02 mm ID (0.10 mm radial clearance).

5. **Install barrel liner** (if bimetallic construction): Press-fit a nitralloy or hardened tool steel liner into the bore. The liner should be 2-3 mm thick, honed to final ID after installation. Liner extends the full barrel length. Interference fit: 0.02-0.05 mm per 100 mm diameter. Heat the barrel to 200-300°C, insert cold liner, allow to shrink-fit on cooling.

6. **Mount barrel to frame**: Fabricate barrel support brackets from 10 mm steel plate. Bolt barrel to frame at three points (feed zone, middle, die end). Barrel must be straight and aligned with screw centerline within 0.05 mm TIR (total indicator reading) over full length. Use shims at mounting points to adjust alignment.

7. **Install band heaters**: Clamp ceramic band heaters around the barrel at 150-200 mm intervals (typically 3-5 zones for a 20:1 L/D extruder). Wire each zone to its own PID temperature controller and thermocouple. Heater bands must make full contact with barrel surface — gaps cause hot spots. Wrap heaters with 25-50 mm mineral wool insulation.

### Screw

8. **Machine screw blank**: Turn screw blank from 4140 or 4340 steel bar on a lathe. The screw has three zones with different channel depths: feed zone (deepest channel, 0.15-0.20 D), compression zone (tapered from feed to metering depth), metering zone (shallowest, 0.04-0.07 D). For a 60 mm screw with 24:1 L/D: feed zone 5D long, compression zone 12D, metering zone 7D. Turn the root diameter as a smooth taper.

9. **Cut screw flights**: Mill the helical flight groove into the screw body using a milling machine with a indexing head. Flight pitch is typically 1.0 D (square pitch). Flight width: 0.1 D. Helix angle at square pitch: 17.66°. The flight land (top surface) must be concentric with the screw axis within 0.02 mm. After milling, grind flight surfaces smooth and polish root diameter to 0.4 μm Ra.

10. **Apply hard-facing**: Weld Stellite or Colmonoy hard-facing alloy to the flight land surfaces (pushing face and top of flight). Grind back to final dimensions after welding. Hard-facing extends screw life 3-5× against abrasive fillers (glass fiber, mineral fillers). Alternative: through-harden the entire screw to 55-60 HRC by heat treatment.

11. **Chrome-plate screw** (optional but recommended): Apply 0.02-0.05 mm hard chrome plating to the entire screw surface. Chrome reduces polymer adhesion, eases cleaning, and provides additional wear resistance. Polish after plating.

12. **Install screw**: Slide screw into barrel through the thrust bearing housing at the drive end. The screw should rotate freely by hand — any binding indicates misalignment or debris. Check radial clearance between screw flights and barrel ID with feeler gauges: 0.05-0.15 mm uniform around the circumference.

### Feed Hopper and Throat

13. **Fabricate hopper**: Weld a conical or pyramidal hopper from 2-3 mm steel sheet. Hopper opening: 150 × 150 mm minimum for a 60 mm screw. Install a slide gate (steel plate) at the hopper base to stop feed. The hopper throat must align with the feed opening in the barrel. Install a water-cooled throat section (copper tubing wound around the feed throat, connected to a water supply) to prevent polymer from melting and bridging in the feed zone.

### Die

14. **Machine die body**: Turn or mill the die body from P20 or H13 tool steel. For a simple strand die (for pelletizing): bore a conical入口 tapering to a straight land (3-5 mm long) at the exit diameter. For pipe die: machine mandrel and spider legs to support the mandrel inside the die body. The die land length determines surface finish — longer land = smoother surface but higher pressure drop.

15. **Install die heater**: Clamp a band heater around the die body. Wire to a separate PID controller. Die temperature must match the last barrel zone temperature (±5°C). Install a thermocouple in the die body wall, 5 mm from the melt channel.

16. **Attach die to barrel**: Bolt die to barrel flange using a breaker plate (perforated steel disk, 3-5 mm thick, holes 3-5 mm diameter) between barrel and die. The breaker plate filters unmelted polymer and metal contamination. Install a screen pack (20-80 mesh stainless wire screens) in front of the breaker plate for additional filtration.

### Downstream Equipment

17. **Install cooling bath**: Position a water trough (2-4 m long) directly below and after the die exit. Water temperature 15-25°C, flow rate 5-20 liters/minute. For pipe: include a sizing sleeve (water-cooled metal ring) at the bath entry to set the pipe OD.

18. **Mount puller**: Install a caterpillar-type puller (two rubber-belted conveyor belts pressing on the extruded product) downstream of the cooling bath. Puller speed must match extruder output: calibrate by measuring extrudate diameter at various puller speeds. Target: ±2% of nominal diameter.

19. **Install cutter or winder**: For rigid profiles, mount a rotary saw synchronized to extrusion length. For flexible products (film, tubing), mount a winding drum. Cutter/winder speed tracks puller speed.

## Calibration and Verification

1. **Barrel alignment**: Install a mandrel (ground steel rod, 0.02 mm smaller than barrel ID) through the full barrel length. The mandrel must slide freely from end to end with no binding. Measure runout at each bearing and support point with a dial indicator. Maximum TIR: 0.05 mm.

2. **Temperature zone calibration**: Heat each barrel zone to setpoint (200°C for PE test). Wait 30 minutes for thermal equilibrium. Verify actual temperature at each zone with a calibrated pyrometer or independent thermocouple inserted into the barrel wall. Each zone must hold setpoint within ±3°C. Zone-to-zone variation must not exceed ±5°C.

3. **Screw clearance check**: With screw installed and barrel at operating temperature (heated to 200°C), rotate screw by hand. No scraping or grinding sounds. Check clearance at feed, center, and die end with feeler gauges through the die opening. Uniform clearance 0.05-0.15 mm required.

4. **Die flow test**: Run a test extrusion with LDPE (most forgiving polymer). Set barrel profile: 160°C → 180°C → 200°C → 220°C (die). Start screw at 20 RPM, increase to 50 RPM. Measure extrudate diameter at 1-minute intervals for 10 minutes. Diameter variation must be <±3% after 5 minutes (initial start-up transient excluded). Die swell for LDPE: 20-40% above die orifice diameter.

5. **Output rate verification**: Weigh extrudate produced in 60 seconds at steady-state screw speed. Compare to theoretical output: Q_theoretical = ρ × N × (π² D² H sin φ cos φ / 2), where ρ is melt density (~0.75 g/cm³ for PE). Actual output should be 80-95% of theoretical (remainder is back-flow and leakage).

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Output rate (30 mm screw) | 10-30 kg/hour |
| Output rate (60 mm screw) | 50-200 kg/hour |
| Output rate (120 mm screw) | 500-1500 kg/hour |
| Screw speed range | 10-200 RPM (variable) |
| Melt temperature range | 160-320°C (polymer-dependent) |
| Die pressure | 5-30 MPa |
| L/D ratio | 20-30:1 (24:1 most common) |
| Number of heating zones | 3-6 (plus die) |
| Temperature control accuracy | ±3°C per zone |
| Motor power (60 mm screw) | 20-50 kW |
| Extrudate dimensional tolerance | ±3-5% of nominal diameter |
| Screw and barrel service life | 10,000-50,000 hours (filler-dependent; glass-filled polymers wear 5-10× faster) |
| Duty cycle | Continuous operation for 24+ hours |

## Strengths

- Continuous process — produces unlimited length of constant cross-section; only stops for material changeover
- Versatile — any thermoplastic can be extruded by adjusting temperature profile and screw design
- Scalable — output proportional to screw diameter²; a 120 mm screw produces ~25× the output of a 30 mm screw
- Relatively simple die tooling — extrusion dies cost $1,000-10,000 vs. $10,000-100,000+ for injection molds

## Weaknesses

- Limited to constant cross-section products — cannot produce features perpendicular to extrusion direction
- Long start-up waste — 5-20 kg of material consumed before process stabilizes and dimensions are on-spec
- Screw and barrel wear — abrasive fillers (glass fiber, mineral fillers) erode flights and bore, requiring periodic rebuilding or replacement
- Not suitable for thermosets — the continuous heating would trigger premature cross-linking

## Variations and Alternatives

- **Single-screw vs. twin-screw**: Single-screw is simpler to build, adequate for simple profiles and re-pelletizing. Twin-screw provides better mixing for compounding, filler dispersion, and polymer blending. Build single-screw first; add twin-screw when compounding demand justifies the complexity.
- **Plunger extruder**: For bootstrapping, a simple heated cylinder with a hydraulic or lever-driven plunger can extrude small-diameter rod and tube. No screw needed. Output is intermittent (batch, not continuous). Suitable for prototyping and low-volume production.
- **Hand-cranked extruder**: A 20 mm screw driven by a hand crank can process LDPE and PS at 1-3 kg/hour. No motor required. Useful as a first-step bootstrap machine.

## Safety

- **Molten polymer burns**: Extruder dies operate at 200-320°C. Polymer melt at these temperatures sticks to skin on contact and cannot be wiped off. Wear heat-resistant gloves, face shield, and long sleeves when adjusting the die or handling extrudate. If molten polymer contacts skin, cool under running water for 15+ minutes — do NOT peel.
- **Pinch points**: The screw-to-barrel gap and the puller belts are pinch hazards. Guard the screw coupling at the drive end. Never reach into the hopper while the screw is turning — use a wooden push stick if feed assistance is needed.
- **Die pressure buildup**: A blocked die can generate 40+ MPa pressure, enough to blow the die off the barrel flange. Install a rupture disk (rated to 1.5× maximum operating pressure) between the breaker plate and the die. Never stand in front of the die during start-up.
- **Electrical hazard**: Band heaters operate at 220-480 V with high current draw. Ground all heater casings. Use insulated terminal boxes. Lock out motor and heater power before performing maintenance.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Surging (cyclic output variation) | Feed inconsistency or screw design issue | Check hopper for bridging; verify screw channel depth taper is smooth; install a starve feeder |
| Melt fracture (sharkskin surface) | Die land too short or shear rate too high | Increase die land length 50-100%; reduce screw speed; raise die temperature 5-10°C |
| Uneven heating across zones | Thermocouple not seated or heater band gap | Re-seat thermocouple in barrel wall; re-clamp heater bands for full contact; check heater resistance |
| Polymer degradation (discoloration, gas) | Barrel temperature too high or residence time too long | Lower barrel temperature 10-20°C; increase screw speed to reduce residence time; check for dead spots in flow path |
| Excessive motor current | Die pressure too high or screw worn | Open die restriction; check screen pack for blockage; measure screw-to-barrel clearance (if >0.5 mm, recondition screw) |

## See Also

- [Injection Molding Machine](injection-molding-machine.md) — uses similar screw-barrel principle for batch injection
- [Blow Molding Equipment](blow-molding-equipment.md) — extruder feeds parison for blow molding
- [Compression Press](compression-press.md) — alternative forming method for thermosets and rubber
- [Machining](machining.md) — screw and barrel manufacturing
- [Electric Motors](../energy/electric-motors.md) — drive motor selection
- [Thermoplastics](../polymers/thermoplastics.md) — polymer processing methods that use extruders
- [Extrusion](../polymers/thermoplastics.md) — extrusion process parameters by polymer type

[← Back to Machine Tools](index.md)
