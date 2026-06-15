# Extruder (Single-Screw and Twin-Screw)

> **Node ID**: machine-tools.extruder
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](machining.md), [`energy.electric-motor`](../energy/electric-motor.md)
> **Enables**: [`polymers.thermoplastics`](../polymers/thermoplastics.md), [`polymers.synthetics`](../polymers/synthetic.md), [`chemistry.petroleum`](../chemistry/petroleum-alternatives.md)
> **Timeline**: Years 15-25
> **Outputs**: continuous_profiles, pipe, sheet, film, wire_insulation, pelletized_resin
> **Critical**: Yes — the extruder is the primary machine for processing thermoplastics and many synthetic polymers; no practical substitute for continuous-profile production

## Overview

A rotating screw pushes polymer granules through a heated barrel, melting and compressing them into a homogeneous melt, then forcing the melt through a shaped die to produce a continuous product of constant cross-section. The screw performs three functions in sequence along its length: feeding (conveying solid granules forward), compressing (melting and densifying the polymer), and metering (delivering uniform-pressure melt to the die).

The melt pressure at the die is generated entirely by the screw rotation against the resistance of the die. Output rate is proportional to screw speed and screw diameter. For a single-screw extruder, volumetric output Q ≈ (π² D² N H sin φ cos φ) / 2 — (π D H³ sin² φ ΔP) / (12 η L), where D is screw diameter, N is screw speed (RPM), H is channel depth, φ is helix angle, ΔP is die pressure drop, η is melt viscosity, and L is metering section length. The first term is drag flow (screw-driven); the second is pressure back-flow. A well-designed screw operates with back-flow less than 10% of drag flow.

The extruder produces pipe, sheet, film, wire insulation, and pelletized resin. It also feeds the [injection molding machine](injection-molding-machine.md) (same barrel-and-screw principle) and the [blow molder](blow-molding-equipment.md) (extruder feeds the parison). Twin-screw variants provide superior mixing for compounding. No other machine can produce continuous thermoplastic profiles — the extruder is irreplaceable in the polymer processing chain.

The three functional zones of the screw are defined by channel depth: the feed zone has deep channels (0.15-0.20 D) for conveying granules; the compression zone tapers the channel depth to build pressure and melt the polymer; the metering zone has shallow channels (0.04-0.07 D) for delivering uniform-pressure melt. The compression ratio (feed depth / metering depth) ranges from 2:1 for easily melted polymers (LDPE) to 4:1 for crystalline polymers (nylon, PET) that require more work input to melt. A general-purpose screw with 2.5:1 compression ratio handles most commodity polymers.

The extruder is also the most energy-intensive polymer processing machine: 0.15-0.35 kWh per kg of polymer processed. Most of this energy comes from the screw motor (mechanical shear heating), with band heaters providing supplemental heat during start-up. At steady state for LDPE, the screw generates 70-90% of the required heat through viscous dissipation — the barrel heaters serve mainly to prevent heat loss to the environment.

## Prerequisites

- [Steel plate and bar](../metals/iron-steel.md) — for barrel, frame, and drive housing
- [Seamless tubing or bored solid bar](../metals/forming.md) — for barrel bore
- [Machining capability](machining.md) — lathe for screw turning, boring for barrel, milling for frame
- [Electric motor](../energy/electric-motor.md) — 5-100 kW depending on screw diameter
- [Temperature controllers](../electronics/electrical-systems.md) — PID-type, one per heating zone
- [Band heaters](../energy/electric-furnaces.md) — resistive heating elements for barrel

## Bill of Materials

### Frame and Drive

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (frame) | 50-200 kg | A36 or equivalent, 10-20 mm thick | [Iron & Steel](../metals/iron-steel.md) | Cast iron frame (heavier, absorbs vibration) |
| Electric motor | 1 | 5-100 kW, 3-phase or DC, 100-1500 RPM | [Electric Motor](../energy/electric-motor.md) | Hydraulic motor (for variable speed without electronics) |
| Gear reducer | 1 | 10:1 to 30:1 ratio, rated to 2× motor torque | [Machine Tools](./index.md) | Belt-and-pulley reduction (less efficient) |
| Bearings | 2-4 sets | Tapered roller, rated to 20 kN thrust + radial | [Bearings](./bearings-abrasives.md) | Bronze sleeve bearings (shorter life) |

### Barrel

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Seamless steel tubing | 1 piece | ID matched to screw OD +0.05-0.15 mm, 10 mm wall, length = L/D × D | [Forming](../metals/forming.md) | Bored solid bar (more machining, better bore quality) |
| Nitriding steel (barrel liner) | 1 piece | 4140 or nitralloy, for bimetallic liner in wear zone | [Iron & Steel](../metals/iron-steel.md) | Hardened tool steel insert (shorter wear life) |
| Band heaters | 3-6 | Ceramic-insulated, 2-5 kW each, 220-480 V | [Electric Furnaces](../energy/electric-furnaces.md) | Cast-in aluminum heaters (better heat transfer, harder to replace) |
| Thermocouples | 3-6 | Type K, 0-400°C range, one per heating zone | [Measurement](../measurement/precision-metrology.md) | RTD sensors (more accurate, slower response) |

### Screw

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Alloy steel bar (screw) | 1 piece | 4140 or 4340, 30-120 mm diameter × L/D ratio length | [Iron & Steel](../metals/iron-steel.md) | Hardened stainless steel (corrosive polymers like PVC) |
| Hard-facing weld (flight surfaces) | 0.5-2 kg | Stellite or Colmonoy, applied by welding | [Joining](./joining.md) | Through-hardened screw (uniform hardness) |
| Chrome plating | — | 0.02-0.05 mm hard chrome on finished screw surface | [Electrochemistry](../electrochemistry/index.md) | Polished bare steel (higher friction) |

### Die and Downstream

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Tool steel (die body) | 5-20 kg | P20 or H13, machined to target profile | [Iron & Steel](../metals/iron-steel.md) | Machined mild steel (shorter die life) |
| Band heater (die) | 1-2 | 1-3 kW, matched to die geometry | [Electric Furnaces](../energy/electric-furnaces.md) | Gas torch (poor temperature control) |
| Cooling bath tank | 1 | 2-4 m long, stainless or aluminum, water-cooled | [Metals](../metals/iron-steel.md) | Wooden trough with copper coil |

## Process Description

### Frame and Drive Assembly

1. **Fabricate frame base**: Cut two C-channel or I-beam steel members (100 × 50 mm, 1.5-2.5 m long) for the frame rails. Weld cross-members at 500 mm intervals. The frame must support 200-500 kg of barrel and drive without flexing more than 0.5 mm.
2. **Mount gear reducer and motor**: Bolt gear reducer to one end of the frame with Grade 8.8 bolts. Align output shaft with barrel centerline using a dial indicator — maximum misalignment 0.05 mm. Mount motor to reducer input. Install flexible coupling between reducer output and screw shank.
3. **Install thrust bearing**: Mount a tapered roller thrust bearing assembly behind the screw shank. This bearing absorbs the die back-pressure force: 20-40 MPa × screw cross-sectional area. A 60 mm screw at 30 MPa die pressure generates ~85 kN thrust — the bearing must be rated accordingly.

**Calibration**: Check coupling alignment with dial indicator — runout <0.05 mm. Verify bearing preload per manufacturer specification.

**Expected performance**: Thrust capacity: 50-5000 N depending on screw size. Drive efficiency: 85-95% through gear reducer.

### Barrel

4. **Prepare barrel bore**: If using seamless tubing, hone the ID to 0.8 μm Ra finish or better. Bore diameter must be concentric within 0.02 mm over the full length. If boring from solid bar, rough-bore to within 0.5 mm of finish diameter, stress-relieve at 600°C for 2 hours, then finish-bore and hone. For a 60 mm screw: bore to 60.10 ±0.02 mm ID.
5. **Install barrel liner** (if bimetallic construction): Press-fit a nitralloy or hardened tool steel liner into the bore. Liner thickness: 2-3 mm, honed to final ID after installation. Interference fit: 0.02-0.05 mm per 100 mm diameter. Heat barrel to 200-300°C, insert cold liner, allow to shrink-fit.
6. **Mount barrel to frame**: Bolt barrel to frame at three points (feed zone, middle, die end). Barrel must be aligned with screw centerline within 0.05 mm TIR over full length. Use shims at mounting points.
7. **Install band heaters**: Clamp ceramic band heaters around the barrel at 150-200 mm intervals (3-5 zones for a 20:1 L/D extruder). Wire each zone to its own PID temperature controller. Wrap heaters with 25-50 mm mineral wool insulation.

**Calibration**: Install a ground mandrel through the barrel — must slide freely end to end. Measure runout at each support with a dial indicator — maximum TIR: 0.05 mm.

**Expected performance**: Barrel ID tolerance: ±0.02 mm. Temperature control: ±3°C per zone. Screw-to-barrel clearance: 0.05-0.15 mm radial.

### Screw

8. **Machine screw blank**: Turn screw blank from 4140 or 4340 steel bar. Three zones with different channel depths: feed zone (0.15-0.20 D), compression zone (tapered), metering zone (0.04-0.07 D). For a 60 mm screw with 24:1 L/D: feed zone 5D, compression zone 12D, metering zone 7D.
9. **Cut screw flights**: Mill helical flight groove using a milling machine with indexing head. Flight pitch: typically 1.0 D (square pitch). Flight width: 0.1 D. Helix angle at square pitch: 17.66°. Flight land concentric with screw axis within 0.02 mm.
10. **Apply hard-facing**: Weld Stellite or Colmonoy hard-facing alloy to flight land surfaces. Grind back to final dimensions. Hard-facing extends screw life 3-5× against abrasive fillers.
11. **Chrome-plate screw**: Apply 0.02-0.05 mm hard chrome plating to entire screw surface. Polish after plating.
12. **Install screw**: Slide screw into barrel through the thrust bearing housing. Rotate freely by hand — any binding indicates misalignment. Check radial clearance with feeler gauges: 0.05-0.15 mm uniform.

**Calibration**: With barrel at 200°C operating temperature, rotate screw by hand — no scraping or grinding sounds. Check clearance at feed, center, and die end.

**Expected performance**: Flight concentricity: ±0.02 mm. Hard-facing thickness: 1-3 mm. Chrome plating: 0.02-0.05 mm.

### Die, Feed, and Downstream

13. **Machine die body**: Turn or mill die body from P20 or H13 tool steel. For a strand die: conical entrance tapering to a straight land (3-5 mm long) at exit diameter. For pipe die: mandrel and spider legs. Die land length determines surface finish — longer land = smoother but higher pressure drop.
14. **Install die heater and breaker plate**: Clamp band heater around die body, wire to separate PID controller. Bolt die to barrel flange using a breaker plate (perforated steel disk, 3-5 mm thick, holes 3-5 mm) and screen pack (20-80 mesh stainless screens) for filtration.
15. **Fabricate hopper and cooling bath**: Weld conical hopper from 2-3 mm steel sheet (150 × 150 mm opening minimum). Install water-cooled throat section. Position cooling bath (2-4 m long, 15-25°C water) below die exit. Mount caterpillar puller and cutter/winder.

**Calibration**: Run test extrusion with LDPE. Barrel profile: 160°C → 180°C → 200°C → 220°C (die). Start at 20 RPM, increase to 50 RPM. Measure extrudate diameter at 1-minute intervals for 10 minutes — variation <±3% after 5 minutes.

**Expected performance**: Die swell for LDPE: 20-40% above orifice diameter. Extrudate tolerance: ±3-5% of nominal diameter.

## Quantitative Parameters

### Output and Performance

| Parameter | 30 mm screw | 60 mm screw | 120 mm screw |
|-----------|-------------|-------------|--------------|
| Output rate | 10-30 kg/hour | 50-200 kg/hour | 500-1500 kg/hour |
| Motor power | 5-15 kW | 20-50 kW | 100-300 kW |
| Die pressure | 5-20 MPa | 5-30 MPa | 5-30 MPa |
| Typical L/D | 20-24:1 | 24-30:1 | 24-30:1 |
| Heating zones | 3 | 4-5 | 5-6 |

### Operating Parameters

| Parameter | Value |
|-----------|-------|
| Screw speed range | 10-200 RPM (variable) |
| Melt temperature range | 160-320°C (polymer-dependent) |
| Temperature control accuracy | ±3°C per zone |
| Extrudate dimensional tolerance | ±3-5% of nominal diameter |
| Screw and barrel service life | 10,000-50,000 hours (filler-dependent) |
| Duty cycle | Continuous operation for 24+ hours |

### Barrel Temperature Profiles by Polymer

| Polymer | Zone 1 (Feed) | Zone 2 (Compression) | Zone 3 (Metering) | Zone 4 (Die) |
|---------|---------------|---------------------|-------------------|-------------|
| LDPE | 140°C | 160°C | 180°C | 190°C |
| HDPE | 160°C | 190°C | 210°C | 220°C |
| PP | 180°C | 210°C | 230°C | 240°C |
| PVC (rigid) | 140°C | 155°C | 165°C | 170°C |
| PS | 170°C | 190°C | 210°C | 215°C |
| Nylon 6 | 220°C | 240°C | 260°C | 270°C |

## Scaling Notes

- A 30 mm screw extruder (5-15 kW) produces 10-30 kg/hour of profile or pelletized resin. Sufficient for bootstrapping polymer processing.
- Scale to 60 mm screw (20-50 kW) for 50-200 kg/hour output — the general-purpose production size for pipe, sheet, and wire insulation.
- Output scales approximately with screw diameter squared: a 120 mm screw produces ~25× the output of a 30 mm screw.
- Twin-screw extruders require two precisely intermeshing screws — build single-screw first, add twin-screw only when compounding or filler dispersion demands justify the complexity.
- Long start-up waste: 5-20 kg of material consumed before process stabilizes and dimensions are on-spec. This waste scales with extruder size.
- A hand-cranked 20 mm screw can process LDPE and PS at 1-3 kg/hour — a viable bootstrap machine requiring no motor.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Surging (cyclic output variation) | Feed inconsistency or screw design issue | Check hopper for bridging; verify channel depth taper is smooth; install a starve feeder |
| Melt fracture (sharkskin surface) | Die land too short or shear rate too high | Increase die land length 50-100%; reduce screw speed; raise die temperature 5-10°C |
| Uneven heating across zones | Thermocouple not seated or heater band gap | Re-seat thermocouple; re-clamp heater bands for full contact; check heater resistance |
| Polymer degradation (discoloration, gas) | Barrel temperature too high or residence time too long | Lower barrel temperature 10-20°C; increase screw speed; check for dead spots |
| Excessive motor current | Die pressure too high or screw worn | Open die restriction; check screen pack for blockage; measure screw-to-barrel clearance |
| Die lip buildup (die drool) | Low-molecular-weight fraction; die too cold | Install die lip heater; lower rear barrel zone 5-10°C; increase screen mesh |
| Screw flight wear (5000+ hours) | Abrasive fillers in compound | Apply Stellite hard-facing; reduce filler loading; install bimetallic barrel liner |
| Vibration at screw coupling | Misalignment between drive and screw | Check coupling runout (<0.05 mm); shim motor mounts; inspect coupling insert |
| Surging at low screw speed (<20 RPM) | Feed zone not gripping granules; hopper bridging | Roughen feed zone barrel surface; install hopper vibrator; preheat feed material |
| Screw pushes back during injection (injection molder) | Check valve not sealing | Inspect non-return ring for wear; replace if clearance >0.1 mm; clean valve seat |
| Barrel wear in feed zone (after 10,000+ hours) | Abrasive fillers (glass fiber, mineral) grinding barrel wall | Install bimetallic liner in feed zone; reduce filler loading; use larger L/D barrel for lower shear |

## Safety

- **Molten polymer burns**: Extruder dies operate at 200-320°C. Polymer melt at these temperatures sticks to skin on contact and cannot be wiped off. Wear heat-resistant gloves, face shield, and long sleeves when adjusting the die or handling extrudate. If molten polymer contacts skin, cool under running water for 15+ minutes — do NOT peel.
- **Pinch points**: The screw-to-barrel gap and the puller belts are pinch hazards. Guard the screw coupling at the drive end. Never reach into the hopper while the screw is turning — use a wooden push stick if feed assistance is needed.
- **Die pressure buildup**: A blocked die can generate 40+ MPa pressure, enough to blow the die off the barrel flange. Install a rupture disk (rated to 1.5× maximum operating pressure) between the breaker plate and die. Never stand in front of the die during start-up.
- **Electrical hazard**: Band heaters operate at 220-480 V with high current draw. Ground all heater casings. Use insulated terminal boxes. Lock out motor and heater power before maintenance.
- **Ventilation**: Some polymers (PVC, acetals) release toxic decomposition products (HCl, formaldehyde) if overheated. Provide local exhaust ventilation above the die exit. Monitor for decomposition: a yellowish or brownish tint in normally clear extrudate indicates thermal degradation — stop and reduce barrel temperature immediately.

## Quality Control

1. **Extrudate diameter**: Measure at 1-minute intervals during steady-state operation. Variation must be <±3% of nominal. Use laser micrometer or mechanical micrometer.
2. **Melt temperature**: Insert a melt thermocouple probe into the extrudate stream at the die exit. Actual melt temperature must be within ±5°C of setpoint. A >10°C difference between zones indicates poor mixing.
3. **Output rate**: Weigh extrudate produced in 60 seconds at a fixed screw speed. Track over time — a 10% drop from baseline indicates screw or barrel wear.
4. **Screen pack inspection**: After each production run, remove and inspect the screen pack. Contaminant buildup (unmelted pellets, foreign material, degraded polymer) indicates barrel temperature or screw design issues. Replace screens when pressure drop exceeds 50% of clean-screen pressure.
5. **Screw and barrel clearance**: Measure radial clearance between screw flights and barrel ID annually (or every 5000 hours). New clearance: 0.05-0.15 mm. When clearance exceeds 0.3 mm, output rate drops and melt homogeneity degrades. Resurface or replace the screw.

## Variations and Alternatives

- **Single-screw vs. twin-screw**: Single-screw is simpler to build, adequate for simple profiles and re-pelletizing. Twin-screw provides better mixing for compounding, filler dispersion, and polymer blending. Counter-rotating twin screws suit PVC (heat-sensitive); co-rotating suit compounding. Build single-screw first.
- **Plunger extruder**: For bootstrapping, a heated cylinder with a hydraulic or lever-driven plunger can extrude small-diameter rod and tube. No screw needed. Output is intermittent (batch). Suitable for prototyping.
- **Hand-cranked extruder**: A 20 mm screw driven by a hand crank processes LDPE and PS at 1-3 kg/hour. No motor required. Useful as a first-step bootstrap machine.
- **Injection molding machine** ([injection-molding-machine.md](injection-molding-machine.md)): Uses the same barrel-and-screw principle for batch injection rather than continuous extrusion.
- Start-up procedure: Heat all barrel zones to setpoint before starting the screw. Running the screw cold causes excessive torque and can shear the screw or damage the drive. Allow 30-45 minutes for heat soak from cold start. Start the screw at low speed (10-20 RPM) and increase gradually as melt exits the die.
- Purging: When changing polymer types or colors, purge the barrel by feeding the new material until the extrudate runs clean. Typical purge waste: 2-5 kg for a 30 mm screw, 5-15 kg for a 60 mm screw. Use LDPE as a universal purge material — it has broad temperature compatibility and good sweeping action.
- Die design rule: The die land length (straight section at the die exit) controls the extrudate surface finish and dimensional stability. A longer land (3-5× the gap width) produces smoother extrudate and allows more die swell to occur inside the die, giving better dimensional control. A shorter land reduces pressure drop but gives a rougher surface.

## References

- [Injection Molding Machine](injection-molding-machine.md) — uses similar screw-barrel principle for batch injection
- [Blow Molding Equipment](blow-molding-equipment.md) — extruder feeds parison for blow molding
- [Compression Press](compression-press.md) — alternative forming method for thermosets and rubber
- [Machining](machining.md) — screw and barrel manufacturing
- [Electric Motor](../energy/electric-motor.md) — drive motor selection
- [Thermoplastics](../polymers/thermoplastics.md) — polymer processing methods that use extruders
- Die swell ratio for LDPE: 1.3-1.6× die orifice. For HDPE: 1.5-2.0×. Account for die swell when setting die gap.

---
*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*

