# Cleanrooms

> **Node ID**: photolithography.cleanrooms
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Dependencies**: [`ceramics.refractories`](../ceramics/index.md), [`chemistry.basic`](../chemistry/index.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 40-70
> **Outputs**: cleanrooms, ultra_pure_water, cleanroom_consumables
> **Critical**: Yes — contamination control is the single largest yield determinant in semiconductor manufacturing

## Cleanrooms
Contamination is the enemy of yield. A single 1 μm particle on a wafer can kill an entire chip. Cleanroom class determines minimum feature size achievable: Class 1000 (ISO 6) for >5 μm features, Class 100 (ISO 5) for 1-5 μm, Class 10 (ISO 4) for sub-micron.

**Cleanroom construction**:
- **Structure**: Enclosed room with smooth, non-shedding walls (epoxy-painted steel, aluminum, or plastic laminate). Flush surfaces, rounded corners, no horizontal surfaces that collect dust. Positive pressure (10-20 Pa above ambient) so air leaks OUT, not in. Airlock entry (personnel and materials enter through separate airlocks with interlocked doors).
- **Air filtration**: HEPA filters (99.97% efficient at 0.3 μm) in ceiling. Laminar flow (air flows in parallel streamlines from ceiling to floor perforations). 20-60 air changes per hour for Class 100. ULPA filters (99.999% at 0.12 μm) for Class 10 and below.
- **Flooring**: Vinyl or raised perforated floor panels (air return). Sticky mats at entrances (tacky surface pulls particles off shoe covers). Anti-static treatment.
- **Lighting**: Tear-drop or flush-mounted fixtures (no horizontal surfaces). UV-blocking if photoresist is light-sensitive.
- **Gowning**: Cleanroom garments (Tyvek, polyester, or polypropylene — non-linting) cover head, body, and shoes. Gloves (nitrile or latex — powder-free). Face mask. Gowning room with sticky mat and air shower.
- **Ultra-pure water (UPW) system**:
  - **Pre-treatment**: Sand filter → carbon filter → water softener
  - **RO (reverse osmosis)**: Semi-permeable membrane removes 95-99% of dissolved ions and organics. Pressure 10-60 bar.
  - **DI (deionization)**: Ion exchange resin beds remove remaining ions. Resistivity target >18 MΩ·cm.
  - **UV sterilization**: 254 nm UV lamp kills bacteria and algae.
  - **Final filtration**: 0.05-0.2 μm membrane filter removes particles.
  - **Distribution**: PVDF or PFA piping (no leaching). Continuous recirculation (no dead legs where bacteria grow).
  - **Quality testing**: Online resistivity monitoring, particle counting, TOC (total organic carbon) analysis

**Strengths**:
- Positive pressure (10-20 Pa) ensures air leaks outward, preventing unfiltered infiltration through any gap
- HEPA filtration at 99.97% efficiency (0.3 μm MPPS) provides clean air sufficient for features down to ~1 μm

**Weaknesses**:
- UPW production chain (sand filter → RO → DI → UV → UF) is multi-stage and requires continuous monitoring to maintain 18 MΩ·cm
- Full cleanroom garment ensemble causes heat stress — limited to 2-hour continuous sessions with cooling breaks

## Operational Protocols
- **[Gowning sequence](../glossary/gowning-sequence.md)** (order matters — cover dirtiest areas first):
  1. Hair cover (bouffant cap — covers all hair, no exposed scalp)
  2. Shoe covers (over-shoe booties — seal around ankle)
  3. Face mask (covers nose and mouth — source of breath droplets)
  4. Gloves (nitrile, powder-free — don before bunny suit to keep inner gloves clean)
  5. Bunny suit (coverall with integrated hood — sealed seams, snap or velcro closures, no pockets or exposed buttons)
  6. Second pair of gloves (over bunny suit cuffs — double-gloving prevents skin exposure)
  7. Boot covers (over bunny suit legs — sealed to suit at knee)
- **Airlock entry procedure**: Personnel airlock with interlocked doors (one must close before the other opens). Air shower (high-velocity filtered air jets from multiple nozzles, 15-30 seconds) dislodges particles from garments. Material airlock (pass-through) for tools, wafers, chemicals — items wiped with IPA-dampened wipes before entry. No cardboard, paper, or wood in cleanroom (uses cleanroom-rated polypropylene or polycarbonate alternatives).
- **Behavioral rules**: No rapid movements (creates turbulence and particle shedding). No cosmetics, perfumes, or hair products. No writing with pencils (graphite particles) — use cleanroom-rated pens. Touch wafer only with wafer wands or vacuum wands, never gloved hands directly.

**Strengths**:
- Structured gowning sequence (cover dirtiest areas first) reduces operator-borne contamination by >98% compared to ungowned entry
- Air shower with high-velocity filtered air jets dislodges residual particles from garments before cleanroom entry

**Weaknesses**:
- Full gowning takes 5-10 minutes per entry — significant productivity overhead in high-traffic fabs
- Double-gloving and boot covers are uncomfortable, limiting continuous wear time to ~2 hours

## Vibration & ESD Control
- **Vibration isolation**: Precision photolithography tools (steppers, mask aligners) require vibration <0.1 μm displacement. Vibration isolation pads (neoprene rubber or air-spring mounts) under tool bases. Massive concrete inertia blocks (2-5 tonnes) decouple tools from floor vibrations. Facility sited away from heavy machinery, rail lines, and road traffic if possible.
- **ESD (electrostatic discharge) control**: MOS devices are destroyed by static discharges as low as 50-100 V. Human body model (HBM) discharge: 100 pF through 1.5 kΩ — a person walking on a synthetic floor can accumulate 5-20 kV. Countermeasures:
  - Anti-static flooring (conductive vinyl or epoxy, resistance 10⁶-10⁹ Ω/sq, grounded through 1 MΩ resistor for safety)
  - Grounded wrist straps (1 MΩ current-limiting resistor to ground — worn at all times when handling wafers or devices)
  - Ionizers (fan-driven or corona-discharge type) neutralize static on insulators that cannot be grounded (wafer surfaces, plastic wafer carriers)
  - Humidity control at 40-50% RH (lower humidity increases static buildup — below 30% RH is dangerous)

**Strengths**:
- Air-spring vibration isolation with 2-5 tonne concrete inertia blocks achieves <0.1 μm displacement — sufficient for sub-micron lithography
- Conductive flooring at 10⁶-10⁹ Ω/sq with grounded wrist straps eliminates >99% of ESD risk to MOS devices

**Weaknesses**:
- Vibration isolation requires massive concrete foundations and careful site selection away from roads and rail lines
- Humidity below 30% RH creates dangerous static conditions — requires active humidification in dry climates

## HEPA Filter Bootstrapping
- **Filter media**: Borosilicate glass microfibers (fiber diameter 0.5-4 μm), formed into a pleated paper-like mat. Pleating increases surface area 20-50× versus flat media, reducing pressure drop. Media binder: acrylic resin (holds fiber matrix together).
- **Filter efficiency**: 99.97% capture at 0.3 μm (the most penetrating particle size — MPPS). Larger particles are intercepted directly; smaller particles are captured by diffusion. HEPA grade is defined by this single-point efficiency.
- **Filter frame construction**: Rigid frame of aluminum or galvanized steel (wood frames warp). Gasket seal (neoprene or closed-cell foam) between filter and ceiling grid — any bypass leak defeats the entire filter. Gel sealant (non-drying silicone or urethane) for critical installations. Filter life: 3-7 years depending on particulate loading; pressure drop monitoring indicates replacement time.
- **Fan/filter unit (FFU) design**: Integrated module — centrifugal fan motor + HEPA filter + pre-filter in a single ceiling tile-sized panel (2×2 ft or 2×4 ft standard). Speed control (adjustable fan RPM for desired air velocity, typically 0.3-0.5 m/s). Modular installation: mount in cleanroom ceiling grid, wire to power, adjust speed. Enables incremental cleanroom expansion.

**Strengths**:
- Pleated media increases surface area 20-50× versus flat, reducing pressure drop while maintaining 99.97% capture at MPPS
- Modular FFU design enables incremental cleanroom expansion — add ceiling tiles as needed without redesigning air handling

**Weaknesses**:
- Borosilicate glass microfiber media requires specialized manufacturing (0.5-4 μm fiber diameter) — not trivially bootstrappable
- Filter life of 3-7 years means ongoing replacement cost and DOP/PAO integrity testing annually

## Cleanroom Garments
- **Materials**: Tyvek (spun-bonded polyethylene — disposable, inexpensive, good particle containment but low durability), or polyester (woven, reusable, excellent particle containment, durable for 50+ wash cycles). Polyester preferred for production cleanrooms.
- **Construction**: Sealed or bound seams (no raw edges that shed fibers). No pockets, zippers, or buttons (particle sources). Garments are continuous-filament woven fabric — no staple fibers to shed. Coverall design with integrated hood or separate hood with face opening. Snap closures or velcro (no hooks that catch particles).
- **Laundry**: Specialized cleanroom laundry — ultra-pure water wash, non-ionic detergent, drying in HEPA-filtered environment. Garments tested for particle shedding after each wash (Helmke drum test or body box test). Typically replaced after 30-50 wash cycles when particle shedding exceeds specification.

**Strengths**:
- Polyester woven garments withstand 50+ wash cycles with consistent particle containment — cost-effective for production
- Sealed seams and continuous-filament fabric eliminate fiber shedding, the primary garment contamination source

**Weaknesses**:
- Tyvek garments are disposable (single-use or few uses) — high consumable cost for large fab operations
- Specialized cleanroom laundry with UPW wash and HEPA-filtered drying is a dedicated infrastructure requirement

## Hazards & Safety

- **Chemical handling**: Acetone, IPA, and MEK solvents are highly flammable (flash points well below room temperature). Use only in ventilated solvent benches with spark-free equipment. Store in flammable-materials cabinets; keep fire extinguishers (CO₂ or dry chemical) within 10 m of solvent stations.
- **UV exposure**: Mercury arc lamps and UV curing tools emit i-line (365 nm) and shorter wavelengths that cause corneal burns and skin erythema. Enclose beam paths; wear UV-blocking safety glasses (OD 5+ at 365 nm) when aligning or servicing lithography tools. Never look directly at an energized lamp.
- **ESD damage to devices**: Static discharges as low as 50 V destroy MOS gate oxides. Wear grounded wrist straps (1 MΩ current-limiting resistor) at all times when handling wafers or packaged devices. Maintain humidity at 40-50 % RH; use ionizers on non-groundable surfaces. Test wrist-strap continuity daily.
- **Ergonomic hazards**: Cleanroom bunny suits cause heat stress (limited ventilation, full-body coverage). Limit continuous gowning sessions to 2 hours with cooling breaks. Airlock entry/exit protocols add physical strain — rotate personnel to reduce repetitive-motion injury from gowning and wafer handling.
- **Piranha solution** (if used for cleaning): See [Resists & Masks](resists-masks.md) for piranha hazards.

## Cleanroom Construction Detail

**Modular construction**:
- **Wall panels**: Prefabricated sandwich panels (steel or aluminum skins with expanded polystyrene or rockwool core), 50-100 mm thick. Panels interlock with cam-lock fasteners (no through-bolts that create particle traps). Joint seals: silicone or polyurethane sealant applied between panels to create airtight, particle-tight connections. Panels arrive factory-finished with epoxy or polyurethane paint (smooth, non-shedding, chemical-resistant).
- **Ceiling grid**: Aluminum T-grid (standard 2×2 ft or 2×4 ft module) suspended from structural ceiling by threaded rod hangers. Grid supports HEPA filter modules, ceiling panels, and lighting. Level to ±1.5 mm across the entire room (critical for laminar airflow uniformity).
- **Raised floor**: Perforated steel or aluminum floor panels (25% open area for return airflow) supported on adjustable steel pedestals. Plenum space below the floor serves as the return air path. Floor height: 300-600 mm above structural slab. Floor panels are anti-static (conductive coating grounded to building earth).

**Air handling system**:
- **Pre-filtration**: 65% ASHRAE (MERV 11) pleated filters remove large particles, extending HEPA life. Changed every 3-6 months based on pressure drop monitoring.
- **HEPA filtration**: 99.97% efficient at 0.3 μm (the most penetrating particle size, MPPS). Larger particles (>0.3 μm) are intercepted directly or by impaction. Smaller particles (<0.3 μm) are captured by Brownian diffusion. HEPA is a probabilistic filter — it does not have a sharp cutoff, but its minimum efficiency occurs at 0.3 μm.
- **ULPA filtration**: 99.999% efficient at 0.12 μm for Class 1-10 (ISO 3-4) cleanrooms. Required for sub-micron semiconductor fabrication. Higher pressure drop than HEPA (~2×), requiring more fan power.
- **Airflow**: Vertical laminar flow from ceiling to floor, 0.3-0.5 m/s face velocity. Air travels in parallel streamlines without mixing (laminar, not turbulent). Turbulence causes particle re-entrainment. Obstructions (equipment, personnel) disrupt laminar flow downstream — position critical processes upstream of obstructions.

**Temperature and humidity control**:
- **Temperature**: 22±0.5°C. Tight control required because photoresist dimensions are temperature-sensitive (thermal expansion of silicon at 2.6×10⁻⁶/°C, and resist viscosity changes with temperature affect spin-coated thickness).
- **Humidity**: 43±3% RH. Low humidity increases static charge buildup (ESD risk to MOS devices). High humidity causes photoresist to absorb moisture, affecting exposure and development characteristics. Humidity also affects particle behavior (humid particles agglomerate and settle faster).

**Strengths**:
- Modular sandwich panels with cam-lock fasteners enable rapid construction without through-bolts that create particle traps
- Vertical laminar flow at 0.3-0.5 m/s with 99.97% HEPA filtration achieves ISO 5 (Class 100) with 20-60 air changes/hour

**Weaknesses**:
- Temperature control of ±0.5°C requires continuous chilled water circulation at 50-200 W/m² — significant energy cost
- ULPA filtration (99.999% at 0.12 μm) has ~2× the pressure drop of HEPA, doubling fan energy per air change

## Contamination Sources and Control

**People** (the dominant contamination source):
- At rest: a fully gowned cleanroom operator emits ~100,000 particles ≥0.3 μm per minute (skin flakes, hair fragments, lint from garments, breath droplets). At moderate activity (walking, reaching): ~1,000,000 particles per minute. This is why gowning, behavior protocols, and laminar airflow are all essential simultaneously.
- **Skin flakes**: Humans shed ~10⁹ skin cells per day. Each skin cell is ~20-30 μm across, carrying bacteria and oils. Full-body garments with integrated hoods and face covers contain ~98% of skin flakes. The remaining 2% escape through the face opening and fabric pores.
- **Breath**: Exhaled breath contains moisture droplets (1-5 μm) carrying bacteria and salts. Face mask captures most but not all. Speaking produces more droplets than breathing. Eat, drink, and smoke only outside the cleanroom.

**Process-generated contamination**:
- **Evaporation**: Metal evaporation sources (Al, Ti, Au) deposit not only on wafers but also on chamber walls and fixtures. Flaking metal films generate particles. Regular chamber cleaning (wet or plasma) required.
- **Spinning**: Photoresist spin coating generates a fine mist of resist droplets. Coater cup with exhaust captures most mist. Cups must be cleaned regularly to prevent dried resist flakes from becoming airborne.
- **Chemical reactions**: Etch processes produce gaseous byproducts that can condense in exhaust ducts. Condensate particles can be entrained in reverse airflow. Exhaust system design must prevent backflow.

**Equipment-generated contamination**:
- **Outgassing**: Plastics (cable insulation, wafer carriers, gaskets) release volatile organic compounds (VOCs) under vacuum or elevated temperature. These VOCs deposit on wafer surfaces as thin organic films. Use low-outgassing materials (PTFE, PFA, stainless steel) for all components in contact with wafers or vacuum.
- **Vibration**: Mechanical vibration from pumps, motors, and air handling equipment transmits through the floor to sensitive tools (steppers, mask aligners). Vibration degrades lithographic resolution. Isolate vibration-sensitive tools on separate inertia blocks.

**Strengths**:
- Laminar airflow sweeps particles away from wafer surfaces at 0.3-0.5 m/s — active contamination removal rather than passive containment
- Full-body garments with integrated hoods contain ~98% of human skin flakes, the dominant particle source

**Weaknesses**:
- A gowned operator at moderate activity emits ~1,000,000 particles/min — people are always the dominant contamination source despite best protocols
- Process equipment (evaporation sources, spin coaters) generates metal and resist particles that require regular chamber cleaning

## Electrostatic Discharge (ESD) Control

**Ionizer systems**:
- **Alpha ionizers**: Polonium-210 (Po-210) radioactive sources emit alpha particles that ionize air molecules, creating equal numbers of positive and negative ions. The ions neutralize static charges on wafer surfaces and equipment. No power required. Limited lifetime (Po-210 half-life = 138 days; replace every 12-18 months). Regulatory issues with radioactive materials in some jurisdictions.
- **Corona ionizers**: High-voltage needles (±5-10 kV) generate corona discharge, producing ions. AC ionizers alternate polarity every few milliseconds, providing balanced ion output. DC ionizers use separate positive and negative emitter points. Balance adjustment: ±50V offset from zero (measured with a charged plate monitor). Require periodic cleaning (needle contamination reduces ion output).
- **Air-assisted ionizers**: Fan blows ionized air toward the work surface. Extends effective range from ~100 mm (passive) to ~500-1000 mm. Used at wafer handling stations, inspection areas, and packaging lines.

**Strengths**:
- Corona ionizers with AC polarity switching provide balanced ion output (±50V offset) without radioactive material
- Air-assisted ionizers extend effective neutralization range to 500-1000 mm, covering entire wafer handling stations

**Weaknesses**:
- Alpha ionizers (Po-210) require replacement every 12-18 months due to 138-day half-life and regulatory burden
- Corona emitter needles require periodic cleaning — contamination reduces ion output and unbalances polarity

## Monitoring and Maintenance

**Particle monitoring**:
- **Continuous particle counters**: Laser scattering counters installed at critical locations (near process tools, at return air grilles). Count particles ≥0.1-5 μm in real-time. Data logged continuously for trend analysis. Alarms trigger at threshold levels (e.g., >100 particles/ft³ ≥0.5 μm for Class 100).
- **Trend analysis**: Sudden particle spikes indicate a problem (torn filter, process upset, gowning failure). Gradual upward trends indicate filter loading or deteriorating process conditions. Review particle data daily, investigate any anomaly.
- **Periodic certification**: Cleanroom classification verified quarterly by third-party testing per ISO 14644-1. Measure particle concentration at specified sampling locations under at-rest and operational conditions. Document results for regulatory compliance and process qualification.

**HEPA filter maintenance**:
- **Life prediction**: Monitor pressure drop across each HEPA filter. As the filter loads with particles, pressure drop increases. When it reaches 2× the initial pressure drop (typically from ~250 Pa to ~500 Pa), replace the filter. Typical HEPA life: 3-7 years in a Class 100 cleanroom.
- **Integrity testing**: DOP (dioctyl phthalate) or PAO (polyalphaolefin) challenge test annually. Generate a uniform aerosol upstream of the filter and scan the downstream face with a photometer. Any leak >0.01% of the upstream concentration indicates a defect (pinhole, gasket leak, damaged media). Repair or replace.

**Strengths**:
- Continuous laser-scattering particle counters provide real-time monitoring with automatic alarms at threshold levels — immediate contamination detection
- DOP/PAO integrity testing detects leaks >0.01% — catches filter defects before they impact wafer yield

**Weaknesses**:
- Quarterly ISO 14644-1 certification by third-party testing adds recurring cost and requires production scheduling around testing
- HEPA replacement at 2× initial pressure drop means 3-7 year cycle requiring cleanroom shutdown for filter swap

## Cleanroom Protocol Details

**Material introduction procedure**:
- All materials entering the cleanroom must be pre-cleaned. Wipe boxes, containers, and tool parts with IPA-dampened lint-free wipes in the material airlock. Remove cardboard, paper, and wood packaging before entry (replace with cleanroom-compatible polypropylene or polycarbonate containers).
- Chemical bottles: Wipe exterior with IPA. Transfer chemicals from shipping containers to cleanroom-rated bottles through a filtered dispensing station. Chemical purity is compromised if the bottle exterior is contaminated and handled inside the cleanroom.
- Wafers: Transport in sealed, clean wafer carriers (fluoropolymer or polypropylene). Open carriers only inside the cleanroom or inside process tools. Never touch wafer surfaces with bare or gloved hands.

**Cleaning and housekeeping**:
- **Daily**: Wipe all work surfaces with IPA at the start and end of each shift. Clean equipment surfaces. Inspect sticky mats at entrances (replace when visibly loaded with particles).
- **Weekly**: Deep clean all horizontal surfaces. Vacuum floor perforations with HEPA-filtered vacuum. Clean light fixtures (dust accumulates on top surfaces). Wipe down walls from top to bottom with cleanroom-rated detergent.
- **Monthly**: Clean ceiling panels and HEPA filter housings (carefully, without disturbing filters). Inspect and clean air return grilles. Verify particle counts meet specification at all monitoring points.

**Personnel training requirements**:
- Cleanroom behavior training before first entry: gowning procedure, movement rules, prohibited items and actions, emergency procedures.
- Process-specific training for each chemical and equipment station: chemical hazards, spill response, emergency shower and eyewash locations, fire extinguisher locations.
- Annual recertification: gowning proficiency test (particle shedding measurement in a body box counter), written test on protocols, practical demonstration of emergency response.

**Strengths**:
- Material pre-cleaning in airlock with IPA wipes removes >99% of surface particles before entry
- Daily/weekly/monthly cleaning cadence with IPA and HEPA vacuum maintains particle counts within specification

**Weaknesses**:
- Annual gowning recertification with body box particle counting is time-consuming but necessary to catch protocol drift
- IPA consumed in large quantities for daily surface wiping — flammable storage and ventilation requirements

## Cleanroom Support Systems

**Chilled water system**: Temperature control (22±0.5°C) requires chilled water at ~7°C supplied to air handling units. Chiller capacity: 50-200 W per m² of cleanroom floor area (depending on internal heat load from process equipment). Redundant chillers (N+1) ensure continuous cooling during maintenance.

**Process cooling water**: Many process tools (etchers, CVD reactors, ion implanters, vacuum pumps) require cooling water at 15-25°C. Separate loop from chilled water (process water is higher temperature and may contain trace chemicals from heat exchanger leaks). Monitor conductivity to detect leaks into the cooling loop.

**Bulk chemical distribution**: Centralized chemical storage room with pumped distribution lines to process stations. Benefits: fewer bottles in the cleanroom (reduced contamination risk), automated dispensing, leak detection on distribution lines. Materials: PTFE or PFA tubing, double-contained for hazardous chemicals (HF, H₂SO₄). Distribution pump: diaphragm type (no seals that leak), with leak detector in the secondary containment.

**Waste collection**: Separate drain systems for acid waste, solvent waste, and general waste. Acid waste collected in chemical-resistant tanks (HDPE or FRP), neutralized before discharge. Solvent waste collected in grounded metal tanks, recycled or incinerated. Never mix acid and solvent waste streams.

**Strengths**:
- Centralized bulk chemical distribution with PTFE/PFA tubing reduces bottle handling in the cleanroom, lowering contamination risk
- N+1 redundant chillers ensure continuous temperature control during maintenance — no process interruption

**Weaknesses**:
- Chilled water system at 50-200 W/m² cooling load is a major energy consumer — a 2000 m² cleanroom needs 100-400 kW just for temperature control
- Separate acid and solvent waste drain systems double the plumbing infrastructure cost

## ISO Cleanroom Classification

The ISO 14644-1 standard defines cleanroom classes by the maximum allowable particle concentration at specified particle sizes:

| ISO Class | ≥0.1 μm | ≥0.2 μm | ≥0.3 μm | ≥0.5 μm | ≥1.0 μm | ≥5.0 μm |
|-----------|---------|---------|---------|---------|---------|---------|
| ISO 1 | 10 | 2 | 0 | 0 | 0 | 0 |
| ISO 3 | 1,000 | 237 | 102 | 35 | 8 | 0 |
| ISO 4 (Class 10) | 10,000 | 2,370 | 1,020 | 352 | 83 | 0 |
| ISO 5 (Class 100) | 100,000 | 23,700 | 10,200 | 3,520 | 832 | 29 |
| ISO 6 (Class 1000) | 1M | 237,000 | 102,000 | 35,200 | 8,320 | 293 |
| ISO 7 (Class 10,000) | — | — | — | 352,000 | 83,200 | 2,930 |

Particle counts are per cubic meter. The relationship between ISO class N and particle concentration Cn at particle size D (in μm) follows Cn = 10^N × (0.1/D)^2.08. For semiconductor fabrication: ISO 4-5 for critical lithography and etch areas, ISO 6-7 for supporting areas (photoresist coating, wafer cleaning, metrology).

## Make-Up Air and Pressurization

A cleanroom loses air through exhaust systems (wet benches, solvent benches, process tool exhaust) and through building leakage. The make-up air system replaces this exhausted air with fresh, filtered, conditioned air:

- **Make-up air volume**: Typically 15-30% of total cleanroom air circulation is fresh make-up air. The remainder is recirculated through HEPA filters. Higher make-up rates increase energy costs (heating, cooling, and dehumidifying outside air) but dilute internal contaminants.
- **Positive pressurization**: The cleanroom is maintained at 10-20 Pa (0.04-0.08 inches of water gauge) above the surrounding corridors. This ensures that when doors open, clean air flows outward, preventing infiltration of contaminated air from less-clean areas. Pressure is maintained by supplying slightly more air than is exhausted. Pressure differential is monitored continuously with a magnahelic gauge; an alarm sounds if pressurization is lost.
- **Airlock pressure cascades**: Personnel and material airlocks form pressure steps between the cleanroom and the outside. A typical cascade: outside (ambient) → gowning room (+5 Pa) → cleanroom (+15 Pa). Each step prevents backflow of contaminated air. Interlocked doors (only one open at a time) maintain the pressure barrier even during transit.

**Strengths**:
- Positive pressurization at 10-20 Pa ensures clean air leaks outward through any gap — passive contamination barrier requiring no operator intervention
- Airlock pressure cascades with interlocked doors maintain the pressure barrier even during personnel and material transit

**Weaknesses**:
- 15-30% make-up air requires continuous heating, cooling, and dehumidifying of outside air — significant energy cost
- Loss of pressurization (fan failure, door propped open) immediately compromises the cleanroom, requiring recovery time

## Recovery After Contamination Events

When a contamination event occurs (spill, equipment failure, filter breach, or improper gowning), the cleanroom must recover to specification:

- **Particle spike recovery**: After a transient particle event (e.g., a wafer dropping), the cleanroom particle count returns to baseline in approximately 3-5 air change cycles. For a Class 100 (ISO 5) cleanroom with 40 air changes per hour, recovery takes 5-8 minutes. The time is calculated as t_recovery ≈ -ln(C_target/C_initial) × (V/Q), where V is room volume and Q is airflow rate.
- **Chemical spill recovery**: Solvent spills are the most common chemical contamination event. Contain the spill with absorbent pads immediately. Ventilate the area by increasing local exhaust. Wipe residual solvent with IPA-dampened wipes. Monitor airborne solvent concentration with a photoionization detector (PID) until readings return to baseline. Do not resume wafer processing until the area is verified clean.
- **Filter breach**: If a HEPA filter develops a leak (detected by routine DOP/PAO integrity testing), the affected area shows elevated particle counts. Seal the leak with gel sealant or replace the filter. The area downstream of the breach must be cleaned and particle counts verified before resuming operations.
- **Post-maintenance recovery**: After any maintenance activity that opens process equipment or the cleanroom envelope, run the air handling system at full capacity for 30-60 minutes before resuming production. Wipe all accessible surfaces in the affected area. Verify particle counts at the nearest monitoring station.

**Strengths**:
- Particle spike recovery in 5-8 minutes (3-5 air change cycles) means transient events have minimal production impact
- Calculated recovery time (t ≈ -ln(C_target/C_initial) × V/Q) enables predictive scheduling after contamination events

**Weaknesses**:
- Chemical spill recovery requires PID monitoring until baseline — may take hours for volatile solvents
- Filter breach requires DOP/PAO testing and possible filter replacement, taking the affected area offline for hours to days

## Cleanroom Floor Plan and Workflow

The layout of a cleanroom directly affects contamination control and operational efficiency:

- **Equipment placement**: Position the most contamination-sensitive processes (photolithography exposure, gate oxide growth) upstream in the laminar airflow, closest to the HEPA filter ceiling. Place particle-generating equipment (sawing, grinding, chemical mechanical polishing) downstream or in separate service chases with their own exhaust.
- **Process flow**: Arrange equipment in the sequence of wafer processing (clean → coat → expose → develop → etch → deposit → test) to minimize wafer transport distance. Each unnecessary transport step increases the risk of particle contamination and handling damage. Wafers travel in sealed carriers between stations.
- **Service chase**: A separate corridor behind the cleanroom wall houses pumps, gas panels, electrical distribution, and exhaust ducting. Maintenance personnel access equipment from the chase side without entering the cleanroom. This separation keeps tools and repair activities (which generate particles) outside the clean envelope. Plumbing and electrical connections pass through sealed wall penetrations.
- **Pass-through windows**: Material transfer between rooms occurs through double-door pass-through chambers with interlocked doors. Load items from the service corridor, wipe down, close the outer door, then retrieve from inside the cleanroom. This eliminates the need to carry materials through the gowning room.

**Strengths**:
- Service chase separation keeps pumps, gas panels, and maintenance activities outside the clean envelope — repairs don't require gowning
- Sequential process flow layout minimizes wafer transport distance, reducing particle contamination risk at each transfer

**Weaknesses**:
- Equipment placement constrained by laminar airflow direction — most sensitive tools must be upstream, limiting layout flexibility
- Sealed wall penetrations for plumbing and electrical add construction complexity and potential leak points

## Cleanroom Flooring Systems

The floor is a critical contamination control surface and must meet several requirements simultaneously:

- **Raised perforated floor**: Steel or aluminum panels (600 × 600 mm) with 20-25% open area (perforations 2-5 mm diameter) supported on adjustable pedestals 300-600 mm above the structural slab. The underfloor plenum serves as the return air path in vertical laminar flow cleanrooms. Panels must be level to ±1.5 mm across the room (uneven panels create turbulence in the return airflow). Floor loading: 5-10 kPa for personnel areas, 20-30 kPa for areas with heavy equipment.
- **Antistatic properties**: Floor panels coated with conductive vinyl or epoxy (surface resistance 10⁶-10⁹ Ω/sq). Grounded through the pedestal base to the building earth. This prevents static charge accumulation from personnel walking, which could discharge onto wafers or damage MOS devices. Conductive flooring is tested with a megohmmeter at installation and annually thereafter.
- **Sticky mats**: Adhesive-coated mats at every cleanroom entrance (personnel and material airlocks). The tacky surface pulls particles off shoe covers and cart wheels. Replace when the surface loses tack or becomes visibly loaded (typically daily in high-traffic areas). Multi-layer mats allow peeling off the top layer to expose fresh adhesive underneath, extending time between complete mat replacements.

**Cleanroom lighting detail**:
- **Luminaires**: Teardrop or flush-mounted fixtures that minimize horizontal dust-collecting surfaces. Housing: white-painted steel with sealed lens (acrylic or polycarbonate). No exposed screws or crevices. Fixture must be gasketed to the ceiling grid to prevent unfiltered air bypass.
- **Light levels**: 800-1200 lux at wafer height for visual inspection and alignment tasks. 300-500 lux for general process areas. Color rendering index (CRI) >80 for accurate visual color matching (important for resist color inspection).
- **UV filtering**: If photoresist is present in the room, light fixtures must block wavelengths below ~450 nm to prevent accidental resist exposure. UV-blocking sleeves over fluorescent tubes or UV-filtering lens material. This is why cleanrooms often have a slightly yellowish appearance.

**Strengths**:
- Raised perforated floor with 20-25% open area provides uniform return airflow while supporting 5-30 kPa floor loading
- Multi-layer sticky mats allow quick refresh by peeling off the top layer — no downtime for mat replacement

**Weaknesses**:
- Raised floor at 300-600 mm above structural slab requires significant building height and adjustable pedestal installation
- UV-blocking lenses give cleanrooms a yellowish tint that can cause eye strain during extended shifts

## Cleanroom Construction Parameters

**Wall panels**: Painted steel or aluminum honeycomb sandwich panels, 50-100 mm thick. Aluminum honeycomb core (cell size 6-12 mm, foil 0.05 mm) provides stiffness at low weight. Sealed joints with neoprene gasket strips between panels prevent particle leakage. Wall surface smoothness <0.8 μm Ra (mirror-finish epoxy paint) for easy cleaning and minimal particle adhesion. Corners coved with 30-50 mm radius to eliminate particle traps.

**Raised floor system**: Perforated aluminum tiles, 600×600 mm, on adjustable steel pedestals. Plenum depth 300-600 mm below the raised floor for return air. Perforation open area 20-25% (holes 2-5 mm diameter) to balance return airflow uniformity with structural load capacity. Floor tiles are anti-static conductive (surface resistance 10⁶-10⁹ Ω/sq), grounded through pedestals.

**Ceiling system**: HEPA/ULPA fan-filter modules cover 60-100% of ceiling area. In ISO 5 (Class 100) areas, 100% coverage provides uniform laminar flow; ISO 7 (Class 10,000) service areas may use 60% coverage with blank ceiling panels between. LED lighting fixtures integrated into ceiling grid, providing 500-1000 lux at the work surface. UV-blocking lenses prevent accidental photoresist exposure below 450 nm.

**Air handling parameters**: Make-up air supplies 10-20% of total airflow volume, maintaining positive pressure at 10-25 Pa above ambient to prevent infiltration. Cooling load: 200-500 W/m² of cleanroom floor area from process equipment heat dissipation (vacuum pumps, RF generators, bake plates). Humidity control via chilled water cooling coils (dehumidification) and clean steam humidification (re-humidification), maintaining 43±3% RH.

**Strengths**:
- Aluminum honeycomb sandwich panels (50-100 mm) provide high stiffness at low weight — structural efficiency for modular construction
- 100% HEPA ceiling coverage in ISO 5 areas ensures uniform laminar flow with no turbulent dead zones

**Weaknesses**:
- Cooling load of 200-500 W/m² from process equipment requires oversized chillers — a 2000 m² fab needs 400-1000 kW cooling capacity
- Wall surface smoothness <0.8 μm Ra requires factory-applied mirror-finish epoxy paint, not field-applied coatings

## Gowning Room Protocol

**Airlock entry cascade**: Three-stage progression — pre-change room (ambient pressure) → gowning room (+5 Pa) → cleanroom (+15 Pa). Interlocked doors prevent two adjacent doors from opening simultaneously, maintaining the pressure barrier. Sticky adhesive mat at each threshold removes particles from shoe covers and cart wheels (peel off top layer when visibly soiled).

**Gowning room layout**: Garment storage in sealed cabinets with HEPA-filtered air supply. Clean garments dispensed from individually sealed bags. Soiled garment return through a pass-through window to the laundry collection area, preventing cross-contamination. Full-length mirror for self-inspection before entering the cleanroom (verify no exposed skin, no loose hair, proper glove seal).

**Garment change frequency**: Daily change for ISO 5 (Class 100) and cleaner environments — garments accumulate skin flakes and particles with each wearing. Twice-weekly for ISO 6 (Class 1000). Weekly for ISO 7 (Class 10,000). Garments are numbered and tracked by serial number through the laundry cycle to enforce change schedule.

**Strengths**:
- Three-stage airlock cascade (ambient → +5 Pa → +15 Pa) with interlocked doors provides redundant contamination barriers
- Serial-numbered garment tracking through laundry enforces change schedule and identifies garments past their wash cycle limit

**Weaknesses**:
- Daily garment change for ISO 5 environments requires large garment inventory and frequent specialized laundry service
- Full-length mirror self-inspection relies on human compliance — no automated verification of proper gowning

## Cleanroom Disciplines

**Prohibited items and practices**: No cosmetics, perfumes, or aftershave (particles and volatile organics). No paper products — use cleanroom-compatible synthetic paper (polypropylene-based) for notes and documentation. No pencils (graphite particles) — use cleanroom-rated ballpoint pens with retained caps. No food, drink, or smoking within the gowning area.

**Movement and behavior**: Move slowly and deliberately to minimize particle generation (a walking person sheds 5-10× more particles than one standing still). Avoid rapid arm movements. Keep conversations brief and quiet. Never touch wafer surfaces directly, even with gloved hands — use wafer wands or vacuum pickups only.

**Daily cleaning protocol**: Wipe all work surfaces, equipment handles, and keyboard covers with 70% IPA (isopropyl alcohol) dampened lint-free wipes at the start and end of each shift. IPA evaporates quickly without residue. Replace sticky mats at entrances when tack diminishes. Empty and wipe process tool catch trays. Inspect and clean wafer carrier interiors before each use.

**Strengths**:
- Slow, deliberate movement reduces particle shedding by 5-10× compared to normal walking pace
- 70% IPA wipes evaporate without residue, making daily surface cleaning fast and effective

**Weaknesses**:
- Prohibition on paper, pencils, and cosmetics requires complete behavioral change from normal work habits
- Walking personnel shed 5-10× more particles than standing — even compliant behavior generates contamination



## See Also

- [Core Fab Processes](fab-processes.md) — processes requiring cleanroom environments
- [Resists & Masks](resists-masks.md) — lithography contamination sensitivity
- [Ceramics Index](../ceramics/index.md) — refractory construction materials
- [Chemistry Index](../chemistry/index.md) — chemical handling in cleanrooms
- [Wafer Handling Robots](../automation/wafer-handling.md) — cleanroom-compatible automation
- [HEPA/ULPA Filtration](../cleanrooms/hepa-ulpa-filtration.md) — air filtration technology

[← Back to Photolithography](index.md)
