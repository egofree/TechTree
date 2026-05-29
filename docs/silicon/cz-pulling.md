# Czochralski Crystal Pulling — Equipment & Construction

> **Node ID**: silicon.crystal-growth.cz-pulling
> **Domain**: Silicon
> **Dependencies**: [`measurement.temperature-pressure`](../measurement/temperature-pressure.md), [`silicon.crystal-growth`](crystal-growth.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 30-50
> **Outputs**: single_crystal_ingots

This document covers the CZ puller as a **machine** — design, materials, fabrication, and assembly from scratch. For the crystal growth process theory (seed insertion, neck growth, shoulder, body, tail-out), see [Crystal Growth & Wafering](./crystal-growth.md). For the polysilicon feedstock, see [MG-Si Production](./mg-si-production.md) and [Silicon Purification](./purification.md).

### Puller Chamber Assembly

**Main vessel**:
- Water-cooled stainless steel (304 or 316) cylindrical chamber. Two sections: upper (pull chamber, 300-500 mm diameter, 800-1200 mm tall) and lower (furnace chamber, 400-600 mm diameter, 400-600 mm tall). Separated by a gate valve to allow crystal removal without exposing hot crucible to air.
- Wall construction: 5-10 mm stainless steel inner shell, welded water cooling channels (external half-pipe welding or bonded jacket). Cooling water flow: 5-15 L/min at 2-4 bar. Thermal load on walls: 5-15 kW during growth — inadequate cooling warps the chamber and contaminates the crystal.
- Viewport: Fused silica window (50-80 mm diameter, 10-15 mm thick) with O-ring seal (Viton or metal C-ring) for visual observation of melt meniscus and crystal diameter. Pyrometer or optical diameter measurement through this port.
- Seals: All flanged connections use Viton O-rings for argon atmosphere (leak rate <10⁻⁶ mbar·L/s). Metal-sealed (ConFlat-type copper gaskets) preferred for ultra-low leak but require higher machining precision.

**Materials list**:
- Stainless steel 304/316 plate, 5-10 mm thick (chamber shells)
- Fused silica viewport window, 50-80 mm diameter, 10-15 mm thick
- Viton O-rings (size per flange diameter) or ConFlat copper gaskets
- Water cooling fittings: 1/2" NPT or ISO hydraulic fittings, stainless steel

**Strengths**:
- Water-cooled stainless steel construction provides robust thermal management and long service life (years between chamber replacements)
- Gate valve between pull and furnace chambers allows crystal removal without breaking furnace vacuum, reducing pump-down time for the next run

**Weaknesses**:
- 5-10 mm stainless steel plate requires heavy welding (TIG or MIG) with full-penetration seams — challenging for small workshops
- Water cooling channels are prone to mineral scale buildup in hard-water regions, requiring periodic descaling with inhibited HCl

### Pull Mechanism — Precision Motion System

**Seed holder and pull rod**:
- Seed crystal holder: Machined from high-purity graphite or molybdenum. Three- or four-jaw collet grips the seed crystal (5-10 mm square, 50-80 mm long, oriented <100> or <111>).
- Pull rod: Stainless steel or molybdenum, 15-25 mm diameter, 800-1200 mm long. Must be straight to within 0.05 mm over full length (runout causes crystal eccentricity). Lower end threads into seed holder; upper end connects to rotation mechanism through a vacuum feedthrough.
- **Wire alternative**: For smaller pullers, a stainless steel wire (2-3 mm diameter) wound on a precision drum replaces the rigid pull rod. Wire is simpler but limits rotation torque.

**Rotation mechanism**:
- Seed rotation: 5-15 RPM via stepper motor or DC servo with encoder feedback. Motor mounts above the chamber, drives through a rotary vacuum feedthrough (magnetic coupling or ferrofluidic seal — ferrofluidic preferred for zero leak, but requires ferrofluid synthesis; magnetic coupling is buildable from NdFeB magnets and stainless steel housing).
- Crucible rotation: 3-10 RPM counter-rotation, driven by a second motor below the furnace chamber. Counter-rotation mixes the melt and homogenizes thermal/dopant distribution.
- **Vibration isolation**: The entire puller assembly must be isolated from floor vibration. Concrete inertia block (1-5 tonnes) on air springs or rubber pads. Motor vibrations transmit through the pull rod to the crystal-melt interface — even 1 μm vibration produces growth striations.

**Lift mechanism**:
- Precision leadscrew (machined on lathe, 2-5 mm pitch, 25-40 mm diameter) driven by stepper motor with microstepping (0.001-0.01 mm per step). Or ball screw (anti-backlash) for smoother motion.
- Pull speed: 0.5-2.0 mm/min during body growth, 3-5 mm/min during Dash neck. Speed stability ±0.5% required — fluctuations cause diameter oscillations and dopant striations.
- Linear guide rails (ground steel shafts with linear ball bearings) constrain pull rod to vertical travel only.

**Strengths**:
- Precision leadscrew with microstepping provides 0.001-0.01 mm resolution — sufficient for ±0.5% speed stability during crystal growth
- Counter-rotating seed and crucible homogenize both temperature and dopant distribution in the melt, producing uniform crystal properties

**Weaknesses**:
- Ferrofluidic vacuum feedthrough (zero leak, preferred) requires ferrofluid synthesis — magnetic coupling is buildable but has slightly higher leak rate (~10⁻⁸ mbar·L/s)
- Vibration isolation adds 1-5 tonnes of concrete inertia block, requiring reinforced floor and crane access for installation

### Thermal System

**Graphite resistance heater**:
- Cylindrical heater: Machined from isostatically pressed graphite (grade G347 or equivalent, density >1.70 g/cm³). Cylindrical shape, 300-450 mm inner diameter, 250-400 mm tall, 15-25 mm wall thickness. Slotted vertically (8-16 slots) to create a long current path and uniform heating. Electrode connections at top and bottom via graphite blocks and water-cooled copper bus bars.
- Power supply: Silicon-controlled rectifier (SCR) or IGBT-based DC supply, 20-100 kW, 10-40 V, 500-3000 A. Power stability ±0.1% needed for ±0.5°C melt temperature control. PID controller with pyrometer or thermocouple (type B: Pt-30%Rh/Pt-6%Rh, usable to 1800°C) feedback.

**Insulation package**:
- Graphite felt (carbonized rayon or PAN felt, density 0.1-0.2 g/cm³, thermal conductivity ~0.2 W/(m·K) at 1400°C in argon). Multiple layers (25-75 mm total thickness) wrapped around heater and below crucible support. Held in place by graphite foil or molybdenum pins.
- Outer shield: Stainless steel or water-cooled copper shell. Without insulation, power consumption doubles and chamber walls overheat.

**Temperature control**:
- Thermocouple (type B or type C: W-5%Re/W-26%Re) in graphite well near crucible. Read to ±0.1°C. Pyrometer (two-color ratio, 0.8-1.1 μm wavelength) aimed at melt surface through viewport as secondary reference.
- Silicon melts at 1414°C. Growth temperature: 1415-1430°C. The melt-solid interface must be maintained within ±0.5°C — a 1°C change shifts pull rate by ~10% and alters crystal diameter. Automatic diameter control via pull speed adjustment based on meniscus shape (observed through viewport or inferred from crystal weight measurement by load cell on pull rod).

**Strengths**:
- Graphite resistance heating is simple and reliable — no RF generator, no moving parts in the hot zone, no precision coil winding required
- ±0.1% power stability (achievable with SCR/IGBT supply and PID control) maintains melt temperature within ±0.5°C

**Weaknesses**:
- 500-3000 A current requires massive water-cooled copper bus bars (25-50 mm² cross section) — a cooling water leak near bus bars causes electrolysis and eventual arc flash
- Graphite heater lifetime is limited to 6-12 months by sublimation at 1400°C in argon; replacement requires full hot zone rebuild (8-16 hours downtime)

### Crucible and Support

**Fused silica (SiO₂) crucible**:
- 300-450 mm diameter (for 150-300 mm crystals), 200-300 mm tall, 5-10 mm wall thickness. Fabricated by arc fusion of high-purity SiO₂ powder against a rotating graphite mandrel — see [Advanced Glass Production](../glass/advanced.md).
- **Single-use**: The crucible slowly dissolves into the silicon melt during growth. Dissolution rate ~0.01-0.03 mm/hour. This introduces 10-20 ppma oxygen into the crystal (from SiO₂ → Si + O). Cannot be reused — the thinning wall weakens and may fail catastrophically during a subsequent run.
- Cost driver: Each crystal requires a new crucible. For civilization bootstrap, crucible production is a critical supply chain bottleneck.

**Graphite susceptor**:
- Cylindrical graphite sleeve, 2-5 mm wall thickness, supporting the crucible mechanically. Provides even heat distribution from heater to crucible. Susceptor is reusable — lasts 50-100 pulls before replacement (slow erosion and cracking from thermal cycling).

**Crucible lift**:
- Hydraulic or screw-driven platform raises/lowers the crucible assembly during charging and growth. Allows crucible position adjustment to maintain optimal thermal centering as melt level drops during pulling.

**Strengths**:
- Fused silica crucible is chemically compatible with molten silicon — introduces only oxygen (a manageable impurity) rather than metallic contaminants
- Graphite susceptor provides mechanical support and thermal uniformity while being reusable for 50-100 pulls

**Weaknesses**:
- Single-use fused silica crucible is the highest consumable cost per crystal — each crucible requires arc-fusion fabrication from high-purity SiO₂ powder
- Crucible dissolution introduces 10-20 ppma oxygen into the crystal, limiting electrical properties compared to float-zone (oxygen-free) silicon

### Atmosphere Control

**Argon inert gas system**:
- Flow rate: 10-30 L/min, continuous. Slight positive pressure in chamber (5-50 mbar above ambient). Argon prevents oxidation of graphite heater/insulation (C + O₂ → CO/CO₂ at >400°C) and suppresses SiO volatilization from melt surface.
- Argon source: Cryogenic air separation (0.93% Ar in atmosphere) — see [Air Separation](../chemistry/air-separation.md). Argon is the third most abundant atmospheric gas but requires distillation at -186°C to isolate.
- Gas flow path: Enter from top of pull chamber (above crystal), flow downward past crystal and melt, exit from bottom of furnace chamber through exhaust. This sweeps SiO and CO away from the crystal.
- Chamber evacuation before backfill: Rotary vane pump to <1 mbar, then backfill with Ar. Repeat 3× purge cycle to reduce residual O₂ and H₂O to <1 ppm. Oxygen in graphite hot zone produces CO, which dissolves into melt as carbon contamination (<1 ppma C target).

**Strengths**:
- Argon is inert and non-reactive with silicon, graphite, and silica at 1400°C — provides a clean growth environment
- 3× purge cycle reduces residual O₂ and H₂O to <1 ppm without requiring high-vacuum pumps

**Weaknesses**:
- Argon consumption of 2-5 m³ per crystal run is a significant ongoing cost — requires a dedicated air separation unit or regular gas deliveries
- Argon is heavier than air — any leak pools at floor level, creating an asphyxiation hazard in enclosed spaces

### Defect Mechanisms and Mitigation

**Dislocations**:
- Origin: Seed-melt contact stress, thermal shock, inclusions. A single dislocation threading through the crystal makes it useless for semiconductor devices (dislocations act as recombination centers and short circuits).
- **Dash necking**: Pull thin neck (~3 mm diameter, 50-100 mm long) at 3-5 mm/min after seed contact. Dislocations cannot propagate through such a thin section — they grow out to the surface. This is the single most critical step for producing device-grade crystals. Requires careful observation through viewport.

**Oxygen incorporation**:
- Source: Crucible dissolution (SiO₂ → Si + O). Concentration 10-20 ppma, higher at start of pull when crucible wall is thickest. Oxygen forms electrically active complexes (thermal donors) that alter resistivity if not managed.
- Mitigation: Accept 10-20 ppma as standard CZ level. Subsequent wafer annealing (600-800°C) stabilizes oxygen into inert SiO₂ precipitates. Magnetic CZ (MCZ — apply magnetic field to suppress melt convection) reduces oxygen to <5 ppma but requires superconducting or large electromagnet (advanced).

**Carbon contamination**:
- Source: Graphite heater/insulation → CO → dissolved C in melt. Target: <1 ppma. Controlled by argon flow rate, chamber tightness, and thorough purge before melt.
- Carbon above 5 ppma causes SiC precipitates in crystal — hard particles that disrupt wafer slicing and device fabrication.

### Resource Budget Per Crystal (150 mm, ~15 kg)

| Resource | Quantity | Notes |
|----------|----------|-------|
| Polysilicon | ~15 kg | From [Silicon Purification](./purification.md) |
| Quartz crucible | 1 | Consumed — dissolved into melt |
| Argon | ~2-5 m³ | Continuous flow during 24-48 hour cycle |
| Electricity | ~200-400 kWh | Heater + motors + cooling water pumps |
| Graphite susceptor | ~0.01 (amortized) | Lasts 50-100 pulls |

### Downstream

Pulled ingots proceed to [Crystal Growth & Wafering](./crystal-growth.md) for cropping, grinding to diameter, wire saw slicing, lapping, and CMP polishing. Finished wafers feed [Basic Semiconductor Devices](./basic-devices.md) — primarily solar cells in early production, with the solar cell feedback loop (electricity → more furnaces → more silicon → more solar cells) driving exponential capacity growth.

### Safety Hazards

The CZ puller combines extreme heat, high electrical current, precision mechanisms, and argon atmosphere — all in one machine:
- **Molten silicon spill**: 10-30 kg of silicon at 1420°C. Worst case: quartz crucible ruptures (wall thins from dissolution, thermal shock cracks) and molten silicon contacts water-cooled chamber shell → steam explosion. Crucible inspection before each run. Automatic thermal runaway shutdown. Secondary containment tray under crucible platform.
- **Argon asphyxiation**: Continuous argon flow (10-30 L/min) into an enclosed chamber. Any leak into the workroom displaces oxygen — argon is heavier than air and pools at floor level. O₂ monitors with alarms at floor level and breathing height. Exhaust vented outdoors. If a puller chamber must be opened after argon fill, purge with air first or use supplied-air respirator.
- **High-current electrical hazard**: Heater draws 500-3000 A. Water-cooled copper bus bars carry this current — a cooling water leak near bus bars causes electrolysis, corrosion, and eventual arc flash. Inspect water connections before each run. Lock-out/tag-out for all maintenance. Arc-flash-rated face shield and flame-resistant clothing for bus bar work.
- **Pull rod mechanical failure**: The seed holder and pull rod support the full crystal weight (10-30 kg) at up to 1200 mm from the drive mechanism. A rod fracture or collet slip drops the crystal into the melt — causes splashing of molten silicon and potential crucible fracture. Rod straightness and thread integrity must be inspected before each run. Pull rod fatigue limit: replace after manufacturer-specified number of cycles.
- **Rotation mechanism hazards**: Counter-rotating seed (5-15 RPM) and crucible (3-10 RPM) create pinch points. The crucible rotation drive is below the furnace — access during operation is prohibited. Guards on all rotating components. Emergency stop accessible from operator position.
- **Burn hazards**: Chamber walls are water-cooled but internal graphite components remain at >1400°C. Even after power-off, thermal mass keeps the hot zone above 1000°C for hours. Cool-down period mandatory before chamber entry. Thermal gloves rated to 500°C for any post-run internal access.

### Czochralski Process Detail

#### Apparatus Configuration

The CZ puller integrates five subsystems into one machine: thermal, mechanical, atmospheric, control, and structural. Each must work within spec for the crystal to be device-grade.

**Crucible assembly**:
- Fused silica crucible, 200-450 mm diameter, 200-300 mm tall, 5-10 mm wall thickness. Wall dissolves into the melt at 0.01-0.03 mm/hour, introducing 5-20 ppma oxygen. Crucible is single-use. After one pull, the thinned wall risks rupture if reused.
- Graphite susceptor sleeve, 2-5 mm wall, supports the crucible mechanically and distributes heat evenly from the resistance heater. Reusable for 50-100 pulls before thermal cycling cracks it.
- Water-cooled copper hearth plate under the susceptor provides the thermal boundary. Cooling water at 2-4 bar, 5-15 L/min. The hearth plate must be flat to within 0.1 mm, or the crucible sits crooked and the crystal grows eccentric.
- Crucible lift platform (hydraulic or screw-driven) adjusts height during growth to keep the melt surface at the optimal position relative to the heater as silicon is consumed.

**Heating**:
- Two options: graphite resistance heating (most common) or RF induction heating (requires a water-cooled copper coil around the susceptor, 10-50 kHz, 20-80 kW).
- Resistance heater: cylindrical graphite element, 300-450 mm inner diameter, 250-400 mm tall, 15-25 mm wall. Slotted with 8-16 vertical cuts to create a long current path. Power supply: SCR or IGBT, 20-100 kW, 10-40 V, 500-3000 A. Power stability ±0.1% for ±0.5°C melt temperature control.
- RF heating: faster response but requires an RF generator (more complex to build from scratch). Graphite susceptor couples to the RF field, heats by eddy currents, radiates to crucible. Used in some small pullers.

**Pull shaft and seed holder**:
- Seed holder: three- or four-jaw collet machined from high-purity graphite or molybdenum, gripping a 5-10 mm square, 50-80 mm long seed crystal oriented <100> or <111>.
- Pull rod: stainless steel or molybdenum, 15-25 mm diameter, 800-1200 mm long. Straightness within 0.05 mm over full length. Connects seed holder to the rotation/lift mechanism through a vacuum feedthrough.
- Seed rotation: 5-20 RPM via stepper motor or DC servo with encoder. Crucible counter-rotation: 3-15 RPM. Counter-rotation mixes the melt, homogenizing both temperature and dopant distribution.

**Argon atmosphere**:
- Chamber backfilled with argon after 3× purge cycle (evacuate to <1 mbar, backfill with Ar). Operating pressure 5-20 mbar (slight positive pressure prevents air ingress).
- Argon flow 20-60 L/min sweeps SiO and CO away from the crystal. Flow enters above the crystal, passes down past the melt surface, exits at the furnace bottom.
- Gas purity: >99.999% Ar, with O₂ and H₂O each <1 ppm. Residual oxygen in the hot zone forms CO from graphite, which dissolves carbon into the melt.

#### Pulling Procedure

The pull cycle runs 24-48 hours for a single crystal. Each phase has specific speed and temperature requirements.

**Melt phase**:
- Load 5-50 kg polysilicon chunks into the crucible. Larger charges need multiple loading steps (melt a partial charge, add more chunks) to avoid bridging, where solid silicon forms an arch above the melt and collapses unpredictably.
- Heat to 1420-1430°C. Silicon melts at 1414°C. Full melt takes 3-6 hours for a 10-30 kg charge. Monitor through the viewport: the charge should collapse into a flat, mirror-like liquid surface.

**Seed contact and meniscus**:
- Lower the seed crystal until it contacts the melt surface. The seed partially melts, establishing a liquid-solid interface. A meniscus forms at the contact point, shaped by surface tension and the temperature gradient. Meniscus height 2-5 mm. Its shape is the primary indicator of crystal diameter.

**Dash neck**:
- Pull at 3-5 mm/min to form a thin neck, ~3 mm diameter, 50-100 mm long. This is the most critical step for crystal quality. Dislocations from the seed cannot propagate through such a thin cross-section. They grow out to the free surface within the first 20-30 mm of neck. If the neck is too thick (>5 mm), dislocations survive and thread into the crystal body, ruining it for semiconductor use.

**Strengths**:
- Dash necking eliminates dislocations with no additional equipment — the geometry of a thin neck naturally forces dislocations to the surface
- Works for all crystal orientations (<100>, <111>) and dopant types

**Weaknesses**:
- The 3 mm neck is fragile — a momentary speed fluctuation or vibration snaps it, requiring a restart (lost polysilicon charge and crucible)
- Requires skilled operator observation through the viewport or a well-tuned automated controller

**Diameter control**:
- After the neck, reduce pull speed to grow the shoulder and then the body. Pull speed during body growth: 0.5-2.0 mm/min.
- Diameter is controlled by a PID loop that adjusts pull speed and heater power simultaneously. If the crystal grows too thick, the PID increases pull speed (pulls faster, less time for radial growth) and/or raises heater power slightly (melts more material at the interface). If too thin, the opposite. Feedback comes from either optical meniscus observation through the viewport or load cell weight measurement on the pull rod.
- Target diameter stability: ±1 mm over the full body length.

#### Dopant Addition and Resistivity Control

**Doping methods**:
- Add doped polysilicon chunks to the initial charge. For p-type: boron-doped polysilicon, or add SiO₂+B₂O₃ pellets to the melt. For n-type: phosphorus-doped polysilicon, or add SiPO₄ (silicon phosphate) to the melt.
- Target resistivity 1-100 Ω·cm depending on application (1-10 Ω·cm for solar cells, 5-50 Ω·cm for power devices, 1-20 Ω·cm for CMOS).
- Dopant concentration in the melt is not constant throughout the pull. Segregation coefficient k = C_solid/C_liquid at the interface determines how the dopant partitions. Boron has k ≈ 0.8, close to unity, so p-type crystals are relatively uniform axially (resistivity varies ±5-10% from seed to tail). Phosphorus has k ≈ 0.35, meaning the solid rejects P into the melt, enriching it over time. The tail end of an n-type crystal has lower resistivity (more P) than the seed end. This limits the usable length of n-type CZ crystals.

**Dopant addition timing**:
- For boron: add at the start, dissolved boron distributes uniformly in the melt before pulling begins.
- For phosphorus: add at the start, but expect axial variation. Alternatively, use co-rotation/counter-rotation melt stirring to homogenize, but the segregation effect at the interface is fundamental and cannot be eliminated.

**Strengths**:
- Boron segregation coefficient (k ≈ 0.8) produces axially uniform p-type crystals — ±5-10% resistivity variation from seed to tail
- Boron is available as borax (Na₂B₄O₇·10H₂O), a widely available industrial chemical — no exotic precursor needed

**Weaknesses**:
- Phosphorus segregation coefficient (k ≈ 0.35) causes significant axial resistivity gradient in n-type crystals — the tail end has 2-3× lower resistivity than the seed end
- Tight resistivity tolerances (±5%) require charge calculations specific to each crystal size and target length

#### Crystal Properties and Grading

**Oxygen content**: 5-20 ppma, introduced by crucible dissolution. Oxygen is higher at the seed end (crucible wall is thickest) and decreases toward the tail. Oxygen forms thermal donors (electrically active complexes) if the crystal is not annealed. Standard practice: heat-treat wafers at 600-800°C to precipitate oxygen into inert SiO₂ particles.

**Carbon content**: <1 ppma target, from CO produced by graphite heater/insulation. Carbon above 5 ppma forms SiC precipitates, hard particles that damage wire saw blades and disrupt device fabrication.

**Dislocation density**: <100/cm² for electronic grade (ideally zero after Dash necking). Solar grade crystals tolerate >5000/cm² because grain boundaries in solar cells already dominate recombination.

**Strengths**:
- CZ silicon with Dash necking achieves near-zero dislocation density (<10/cm²), suitable for all semiconductor device types
- 10-20 ppma oxygen provides built-in gettering: oxygen precipitates in the wafer bulk trap metallic impurities away from the active device region

**Weaknesses**:
- Oxygen concentration varies along the crystal length (higher at seed end), causing resistivity variation that must be characterized and managed
- Carbon contamination from graphite hot zone must be kept below 1 ppma — requires high-purity argon and tight chamber seals

#### Hot Zone Design

The hot zone is everything inside the furnace chamber between the heater and the chamber walls: insulation, radiation shields, gas flow channels, and structural supports.

**Radiation shields**: Graphite or molybdenum discs and cylinders positioned above the crucible to trap heat and create a uniform thermal environment around the crystal. Without shields, the crystal radiates heat to the cold chamber walls, creating steep axial temperature gradients that cause thermal stress and dislocations.

**Argon flow design**: Gas enters above the crystal, flows down past the crystal and melt, exits at the bottom. Flow rate 20-60 L/min. The flow path must avoid dead zones where SiO or CO accumulates and re-deposits on the crystal surface. Baffles direct flow along the crucible wall to sweep SiO downward and away.

**Crucible life**: 100-300 hours of cumulative hot time before the thinned wall cracks under thermal stress or the weight of a fresh charge. Some operations track crucible hours and retire them on a schedule. A crucible failure during a pull is catastrophic: molten silicon spills onto the susceptor and heater, destroying the hot zone and requiring a full rebuild (days of downtime).

**Strengths**:
- Radiation shields reduce heat loss by 30-50%, cutting power consumption from 80-100 kW down to 50-70 kW for a 200 mm pull
- Well-designed argon flow sweeps SiO and CO away from the crystal, keeping the growth interface clean

**Weaknesses**:
- Hot zone rebuild after 100-300 hours takes 8-16 hours of downtime — new crucible, susceptor inspection, insulation replacement, SiO deposit cleaning
- Radiation shields add thermal mass that slows temperature changes, reducing the response time of the diameter control PID loop

### Pulling Procedure, Step by Step

Every CZ pull follows the same sequence. Timing and temperature control at each stage determine whether the result is a device-grade ingot or scrap silicon.

**Charging and melting**:
Polysilicon chunks (5-50 kg depending on crucible size) are loaded into the fused silica crucible. The charge is often topped with dopant material at this stage (see Dopant Addition below). The chamber is sealed, evacuated to <1 mbar with a rotary vane pump, then backfilled with argon. This purge cycle repeats three times to drive residual oxygen and moisture below 1 ppm. Once purged, heater power ramps up over 4-8 hours to bring the charge to 1420°C, fully melting the silicon. Melt stabilization follows: hold at target temperature for 30-60 minutes while the melt homogenizes thermally and chemically. Temperature must settle within ±0.1°C before seeding begins.

**Seeding**:
The seed crystal (5-10 mm square, oriented <100> or <111>) is lowered on the pull rod until it contacts the melt surface. This is the most delicate moment in the entire cycle. Contact too fast and thermal shock spawns dislocations through the seed. The operator watches through the viewport for the melt meniscus to wrap around the seed edge, confirming wetting. Melt temperature is adjusted ±0.5°C until the meniscus is stable.

**Dash neck**:
After seed contact, pull speed increases to 3-5 mm/min and the crystal diameter is reduced to roughly 3 mm. This narrow neck, 50-100 mm long, is where dislocations die. Any dislocation propagating from the seed cannot fit through a 3 mm cross section and instead grows out to the surface. Without Dash necking, the entire crystal inherits dislocations from the seed. It takes steady hand-eye coordination or a well-tuned closed-loop controller to maintain this diameter without the neck snapping.

**Shoulder (crown) growth**:
Once the neck is established, pull speed drops to 0.2-0.5 mm/min and the crystal diameter expands outward to the target body diameter (100-300 mm). The transition from neck to full diameter looks like a cone or rounded shoulder. If the shoulder grows too fast, new dislocations nucleate at the convex growth interface. The shoulder angle is typically 45-60° from the vertical axis. This phase takes 1-3 hours depending on target diameter.

**Body growth**:
At full diameter, pull speed settles to 0.5-2.0 mm/min. This is the longest phase: 12-36 hours for a typical 15-30 kg crystal. Diameter is held constant by a PID control loop that adjusts pull speed based on either a load cell measuring crystal weight (weight increase rate corresponds to diameter) or an optical sensor measuring diameter directly through the viewport. Setpoint: ±1 mm on diameter. The PID loop responds every 1-5 seconds. Melt temperature drifts by less than ±0.5°C during the entire body pull.

**Tail-out**:
Near the end of the pull, melt volume is low and thermal gradients steepen. Rather than yanking the crystal free (which causes thermal shock dislocations in the last 20-30 mm of ingot), pull speed is gradually increased to narrow the crystal into a tail. Diameter shrinks over 10-30 minutes until the crystal detaches naturally from the melt. The finished ingot is lifted into the upper chamber, the gate valve closes, and the crystal cools under argon before removal.

### Dopant Addition and Resistivity Control

Electrical properties of the crystal come from dopants added to the melt before pulling. The choice of dopant and its concentration determine resistivity, which in turn determines whether the wafer works for a given device.

**Dopant types and delivery**:
Boron (p-type) is added as boron-doped polysilicon chips, or as a mixture of SiO₂ and B₂O₃ that dissolves into the melt. Phosphorus (n-type) is added as phosphorus-doped polysilicon or as silicon phosphate (SiPO₄). Antimony and arsenic are alternatives for n-type but have lower segregation coefficients and are harder to control. For bootstrap production, boron is the easiest dopant: it is chemically stable, readily available as borax (Na₂B₄O₇·10H₂O), and has a segregation coefficient close to unity.

**Segregation and axial uniformity**:
As the crystal grows, dopant concentration in the melt changes because the solid incorporates dopant at a different rate than the liquid supplies it. The segregation coefficient k = C_solid / C_liquid determines this behavior. Boron has k ≈ 0.8, meaning the crystal takes up 80% of the melt concentration. This makes boron-doped crystals remarkably uniform along their length. Phosphorus has k ≈ 0.35, so the crystal initially rejects phosphorus and the melt enriches over time. A phosphorus-doped crystal shows significant resistivity gradient from seed end (higher resistivity, less P) to tail end (lower resistivity, more P). For tight resistivity tolerances with phosphorus, melt replenishment systems add doped silicon during the pull to maintain constant melt composition.

**Target resistivity**:
Typical targets: 1-100 Ω·cm. Solar cells use 1-10 Ω·cm (moderately doped for good carrier lifetime). Logic devices might target 10-50 Ω·cm. Resistivity maps to carrier concentration through ρ = 1/(q·n·μ), where q is electron charge, n is carrier density, and μ is mobility. A resistivity of 10 Ω·cm corresponds to roughly 1.5×10¹⁵ boron atoms/cm³.

**Oxygen from crucible dissolution**:
Fused silica crucibles slowly dissolve into the melt during growth, introducing 5-20 ppma (parts per million atomic) of oxygen into the crystal. This is not purely harmful. When wafers are heat-treated at 600-800°C in subsequent processing, interstitial oxygen precipitates as SiO₂ clusters in the wafer bulk. These clusters act as gettering sites: they trap metallic impurities (iron, copper, nickel) that would otherwise degrade device performance in the active surface region. This "internal gettering" is a deliberate feature of CZ-grown silicon. Float-zone silicon, by contrast, has oxygen below 1 ppma and lacks this built-in gettering.

### Crystal Properties and Defect Classification

Not all crystals are created equal. The defect density determines whether an ingot is electronic grade, solar grade, or scrap.

**Dislocation density**:
Electronic grade silicon requires dislocation density below 100 per cm². Modern production CZ crystals with proper Dash necking achieve near-zero dislocations (<10/cm²). Solar grade tolerates higher dislocation density (>5000/cm²) because solar cells are less sensitive to individual defects than integrated circuits. Dislocations act as recombination centers that reduce minority carrier lifetime, and in extreme cases provide electrical short-circuit paths through p-n junctions.

**Slip lines**:
Thermal stress during cooling generates slip, a plastic deformation where crystal planes shear along specific crystallographic directions. Slip appears as visible lines on etched wafer surfaces. The danger zone is 800-1200°C, where silicon is hot enough for dislocations to move under stress but cool enough that applied stress is significant. Cooling faster than 5°C/min through this range almost guarantees slip. In practice, the ingot cools inside the puller upper chamber under argon for 2-4 hours after tail-out before removal.

**Vacancy clusters (COP)**:
Crystal originated particles (COP) are tiny octahedral voids, 50-200 nm in size, formed by vacancy aggregation during crystal growth. Vacancies are thermally generated point defects (empty lattice sites) that exist in equilibrium at the melting point. As the crystal cools, vacancies become supersaturated and cluster together. COPs are a problem for gate oxide integrity in advanced ICs (they cause localized oxide thinning and breakdown). In nitrogen-free pulls, vacancy concentration can reach 10¹⁰-10¹² per cm³.

**Nitrogen doping for COP suppression**:
Adding 1-5×10¹⁴ nitrogen atoms/cm³ to the melt suppresses COP formation. Nitrogen atoms bind to vacancies during growth, preventing them from clustering into voids. The nitrogen is introduced as Si₃N₄ powder mixed into the polysilicon charge. For bootstrap production targeting solar cells rather than sub-micron ICs, COP suppression is a low priority. But if the goal is CMOS logic at 1 μm or below, nitrogen-doped CZ silicon is worth the added process complexity.

### Hot Zone Design and Maintenance

The "hot zone" is everything inside the furnace chamber that is not the crystal or the melt: heater, insulation, susceptor, radiation shields, gas flow channels, and structural supports. Hot zone design determines temperature uniformity, power consumption, crystal quality, and operational lifetime.

**Radiation shielding**:
At 1420°C, radiation is the dominant mode of heat transfer. Without shielding above the crucible, the melt surface radiates directly toward the cold chamber lid and the growing crystal, creating steep thermal gradients that cause thermal stress in the crystal. Radiation shields made of graphite felt or molybdenum sheets are positioned above the crucible to reflect heat back toward the melt. A well-designed shield array reduces heat loss by 30-50% and cuts power consumption from 80-100 kW down to 50-70 kW for a 200 mm pull.

**SiO vapor management**:
Silicon reacts with oxygen from the dissolving crucible at 1420°C to form silicon monoxide vapor (Si + ½O₂ → SiO). This volatile gas condenses on cooler surfaces inside the chamber: the pull rod, radiation shields, chamber walls. SiO deposits are brownish and powdery, and over many runs they build up and flake off, falling back into the melt as particulate contamination. The argon flow (20-60 L/min, directed from the top of the pull chamber downward past the crystal and out the bottom) carries SiO vapor away before it condenses on critical surfaces. The exhaust gas passes through a particulate filter or cold trap before venting.

**Crucible lifetime and hot zone rebuild**:
The fused silica crucible dissolves at 0.01-0.03 mm per hour into the melt. A crucible starting at 8 mm wall thickness and running a 30-hour pull ends with walls roughly 7.1-7.7 mm thick. After 100-300 hours of cumulative use (including the susceptor and insulation), the hot zone requires a full rebuild: new crucible, inspection and possible replacement of the graphite susceptor (checking for cracks from thermal cycling), replacement of contaminated insulation felt, and cleaning of SiO deposits from all surfaces. Hot zone rebuild takes 8-16 hours and is scheduled between pulls.

**Power efficiency and thermal balance**:
A 200 mm CZ puller running a 20 kg crystal consumes roughly 200-400 kWh over its 24-48 hour cycle. Of the total heater input power (50-100 kW), only about 10-15 kW goes into maintaining the melt at 1420°C. The rest is lost to radiation, convection in the argon, and conduction through supports. Good insulation and radiation shielding are not luxury features; they are the difference between a puller that runs on 50 kW and one that needs 100 kW, which matters enormously when your electricity supply is limited. Every kilowatt saved on the puller is a kilowatt available for another furnace, another process step, another step up the production curve.

### Process Parameter Summary

| Parameter | Value | Tolerance |
|-----------|-------|-----------|
| Melt temperature | 1415-1430°C | ±0.5°C during body growth |
| Pull speed (body) | 0.5-2.0 mm/min | ±0.5% |
| Pull speed (Dash neck) | 3-5 mm/min | ±1% |
| Seed rotation | 5-15 RPM | ±0.5 RPM |
| Crucible counter-rotation | 3-10 RPM | ±0.5 RPM |
| Argon flow | 20-60 L/min | ±5 L/min |
| Base pressure | <10⁻⁴ Pa | — |
| Crystal diameter | 100-300 mm | ±1 mm |
| Dash neck diameter | ~3 mm | ±0.5 mm |
| Pull rod straightness | — | <0.05 mm over 1200 mm |

---

*Part of the [Bootciv Tech Tree](../index.md) • [Silicon](./index.md) • [All Domains](../index.md)*
