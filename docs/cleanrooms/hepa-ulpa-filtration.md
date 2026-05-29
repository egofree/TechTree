# HEPA/ULPA Filtration & Laminar Flow

> **Node ID**: cleanrooms.hepa-ulpa-filtration
> **Domain**: [Clean Room Technology](./index.md)
> **Dependencies**: None (root capability)
> **Enables**: None (leaf capability)
> **Timeline**: Years 40-70
> **Outputs**: hepa_filters, ulpa_filters, laminar_flow_systems, fan_filter_units
> **Critical**: Yes — HEPA/ULPA filtration removes sub-micron particles from air supply; without it, no cleanroom can achieve even ISO Class 8

### Overview

High-efficiency particulate air (HEPA) and ultra-low penetration air (ULPA) filters are the core contamination removal technology in clean rooms. Without effective filtration, no clean room can achieve even ISO 8 classification. A single HEPA filter removes 99.97% of particles at the most penetrating particle size (MPPS) of 0.3 μm; ULPA extends this to 99.999% at 0.12 μm. Modern semiconductor fabrication at 5 nm nodes requires particle control 10-100× smaller than a single transistor gate — demanding ULPA filtration and laminar flow discipline simultaneously.

This capability covers the engineering of filter media, filter housing and sealing, fan-filter unit (FFU) design, pre-filtration stages, laminar flow physics, and integrity testing. It does NOT cover the facility design (see [Facility Design & HVAC](facility-design.md)) or contamination control protocols (see [Contamination Control](contamination-control.md)).

### Filter Media Construction

**Borosilicate glass microfiber media**:

The filter medium is a mat of borosilicate glass microfibers with diameters ranging from 0.5 to 4 μm. These fibers are formed into a paper-like sheet through a wet-laying process similar to paper manufacturing. The fiber mat is pleated to increase the effective filtration surface area by 20-50× compared to a flat sheet, which reduces the pressure drop across the filter at a given airflow rate.

- **Fiber composition**: Borosilicate glass (SiO₂ 70-80%, B₂O₃ 7-13%, Na₂O/K₂O 3-5%, Al₂O₃ 1-3%). The high silica content provides thermal stability and chemical resistance. Fiber diameter is the critical parameter — finer fibers capture smaller particles but increase pressure drop.
- **Media binder**: Acrylic resin (5-10% by weight) holds the fiber matrix together during handling and operation. The binder must be chemically inert, non-outgassing, and temperature-stable up to 90°C (maximum operating temperature for standard HEPA filters).
- **Pleating geometry**: Pleat depth 25-50 mm, pleat spacing 3-5 mm. Deeper pleats increase surface area but can cause flow maldistribution between pleats if spacing is too tight. Separators (corrugated aluminum or synthetic string) maintain pleat spacing under airflow pressure.
- **Media area vs. face area**: A standard 610 × 610 mm HEPA panel contains 20-25 m² of media within a 0.37 m² face area — a 54-68× area ratio achieved through pleating.

**Filter frame construction**:

- **Standard frame**: Rigid frame of aluminum (preferred) or galvanized steel. Aluminum is lighter and corrosion-resistant. Wood frames are prohibited — they warp under humidity cycling, breaking the seal.
- **Frame dimensions**: 610 × 610 mm (2 × 2 ft) and 1220 × 610 mm (4 × 2 ft) are standard ceiling-grid-compatible sizes. Depth: 150-300 mm depending on media area and pleat depth.
- **Gasket seal**: Neoprene or closed-cell foam gasket between the filter frame and the ceiling grid or housing. The gasket must be continuous with no gaps — any bypass leak defeats the entire filter. Gasket compression of 20-30% ensures a seal.
- **Gel sealant**: For critical installations (ISO 3-4 cleanrooms), a non-drying silicone or polyurethane gel channel replaces the gasket. The filter frame sits in the gel, creating a bubble-tight seal that accommodates minor frame irregularities. Gel seals are re-usable when filters are replaced.

**Strengths:**
- Pleating achieves 54-68× area ratio within a standard 610 × 610 mm ceiling tile, enabling high flow rates at low face velocity (0.3-0.5 m/s) and low pressure drop (~250 Pa clean)
- Borosilicate glass fiber media resists temperatures up to 90°C and is chemically inert to most cleanroom chemicals, allowing in-situ decontamination

**Weaknesses:**
- Media is fragile — shipping, handling, and installation require care to avoid tears that create bypass leaks negating the filter's purpose
- Acrylic binder degrades above 90°C, limiting HEPA filter use in high-temperature applications (e.g., inline exhaust duct heaters require heat-resistant filter media)

### HEPA Filtration Physics

**Three capture mechanisms** operate simultaneously in a HEPA filter. Understanding these is essential for filter selection and performance prediction:

1. **Interception**: Particles following an airflow streamline come within one particle radius of a fiber and adhere via Van der Waals forces. Dominant for particles 0.3-1.0 μm. Larger particles are more likely to be intercepted because their larger radius means they contact fibers from further away.

2. **Impaction**: Particles with sufficient inertia cannot follow the curved streamlines around fibers and collide directly. Dominant for particles >1.0 μm. The impact parameter (Stokes number) determines whether impaction occurs — higher particle mass and velocity increase impaction probability.

3. **Diffusion (Brownian motion)**: Sub-micron particles exhibit random Brownian motion due to molecular collisions. This random walk increases the probability that particles will contact a fiber. Dominant for particles <0.3 μm. Smaller particles diffuse more vigorously and are actually easier to capture than 0.3 μm particles.

**The most penetrating particle size (MPPS)** occurs at the crossover point where diffusion and interception/impaction are both at their weakest — approximately 0.3 μm for standard HEPA media. This is why HEPA efficiency is specified at 0.3 μm: it represents the worst-case particle size. Particles both larger and smaller than MPPS are captured more efficiently.

- **HEPA specification**: 99.97% capture efficiency at 0.3 μm (MPPS). This is a minimum — actual efficiency is typically 99.97-99.99% across the full particle size range.
- **ULPA specification**: 99.999% capture efficiency at 0.12 μm (MPPS for ULPA-grade media with finer fibers). ULPA filters use smaller-diameter fibers (0.25-1.0 μm) and tighter packing, shifting the MPPS downward.
- **Pressure drop**: Clean HEPA at rated flow: ~250 Pa. Clean ULPA: ~500 Pa (roughly 2× HEPA due to finer media). As the filter loads with particles, pressure drop increases. Replace when pressure drop reaches 2× the initial value (typically ~500 Pa for HEPA, ~1000 Pa for ULPA).

**Strengths:**
- MPPS-based testing at 0.3 μm (HEPA) and 0.12 μm (ULPA) represents worst-case particle size — actual filtration efficiency is higher for both larger and smaller particles
- Three complementary capture mechanisms (interception, impaction, diffusion) ensure high efficiency across the full particle size spectrum from 0.001 to 10 μm

**Weaknesses:**
- MPPS efficiency testing is destructive (performed at the factory, not in-situ) — installed filter performance depends entirely on seal integrity, verified only by annual DOP/PAO scans
- Pressure drop doubles from clean to fully loaded, requiring variable-speed fans or oversized motors to maintain constant airflow throughout the filter's service life

### ULPA Filtration — Extended Requirements

ULPA filters are required for ISO Class 3-4 cleanrooms (semiconductor fabrication at sub-micron nodes). The tighter filtration imposes additional design constraints:

- **Higher fan power**: Double the pressure drop of HEPA means roughly double the energy consumption per unit of airflow. For a 100 m² cleanroom with 100% ULPA ceiling coverage at 0.45 m/s face velocity, fan power is approximately 8-12 kW versus 4-6 kW for HEPA.
- **Finer media fragility**: ULPA media with sub-micron fibers is more delicate. Shipping, handling, and installation require care to avoid media damage. The filter must be installed with the arrow indicating airflow direction pointing downward (media upstream side faces the plenum).
- **Lower tolerance for bypass leaks**: At 99.999% efficiency, a single pinhole leak that bypasses 0.01% of airflow introduces as many particles as the entire filter face captures. Gel seal systems are strongly recommended for ULPA installations.
- **Filter life**: ULPA filters in ISO 3-4 environments typically last 3-5 years. The tighter media clogs faster than HEPA, but the cleaner operating environment (pre-filtered air from make-up air handlers) extends life. Pressure drop monitoring is essential — replace at 2× initial drop.

**Strengths:**
- ULPA's 99.999% efficiency at 0.12 μm MPPS provides 10× better particle removal than HEPA, essential for sub-10 nm semiconductor lithography where a single particle destroys a die
- Gel seal systems accommodate frame irregularities and are re-usable, eliminating bypass leaks that would negate the filter's performance

**Weaknesses:**
- Double the pressure drop of HEPA requires roughly double the fan energy per unit airflow (8-12 kW vs. 4-6 kW for a 100 m² cleanroom)
- Finer ULPA media is more fragile during shipping and installation — damage that creates a pinhole leak defeats the filter's entire purpose since a 0.01% bypass introduces as many particles as the filter face captures

### Pre-Filtration Stages

Pre-filters extend HEPA/ULPA life by removing the bulk of large particles before they reach the final filter. A well-designed pre-filtration cascade can extend final filter life by 2-3×:

**Stage 1 — Coarse pre-filter (MERV 8, G4)**:
- 30-40% efficient at 1-10 μm particles. Washable or disposable panel filters. Catches dust, lint, and large debris. Changed every 1-3 months depending on ambient air quality. These are the first line of defense and protect downstream filters from rapid loading.

**Stage 2 — Medium pre-filter (MERV 11, F7)**:
- 60-80% efficient at 1-3 μm. Pleated disposable filters. 65% ASHRAE spot rating. Changed every 3-6 months based on pressure drop monitoring. These capture the bulk of particulate load and are the primary HEPA life extender.

**Stage 3 — Final filter (HEPA/ULPA)**:
- The cleanest air reaches the final filter with only sub-micron particles remaining. Pre-filters remove 90-95% of the total particulate mass, reducing HEPA loading to 5-10% of what it would be without pre-filtration. The economics are clear: pre-filters cost $5-30 each; HEPA filters cost $200-800 each. Replacing pre-filters quarterly is far cheaper than replacing HEPA filters annually.

### Fan-Filter Unit (FFU) Design

The FFU integrates the fan, pre-filter, and HEPA/ULPA filter into a single ceiling-tile-sized module:

- **Housing**: Painted steel or aluminum enclosure, sized to fit standard ceiling grids (610 × 610 mm or 1220 × 610 mm). The housing contains the fan, motor, pre-filter, and final filter in a stack.
- **Fan**: Centrifugal blower (forward-curved or backward-curved impeller). Must overcome the filter pressure drop (250-500 Pa clean, up to 1000 Pa loaded) and deliver the design airflow. Motor: EC (electronically commutated) or AC with variable speed control.
- **Speed control**: Adjustable fan RPM to set the desired face velocity at the filter exit. Typical range: 0.2-0.5 m/s. Lower speeds save energy but reduce particle clearance rate. Speed is set during commissioning and adjusted as filters load.
- **Noise**: FFU noise at 0.45 m/s face velocity: 45-55 dBA at 1 m distance. Noise is a significant ergonomic concern in cleanrooms with 100% ceiling coverage — operators work under hundreds of FFUs for 8-12 hour shifts.
- **Power**: Individual FFU power consumption: 100-300 W at rated flow. A 100 m² ISO 5 cleanroom with 100% FFU coverage (~270 FFUs at 610 × 610 mm) draws 27-81 kW continuously. Energy is the single largest operating cost for cleanrooms.
- **Modularity**: FFUs are plug-and-play modules. A cleanroom can be expanded by adding more FFUs to the ceiling grid. Failed FFUs are replaced individually without shutting down the entire air handling system. This modularity enables incremental construction and maintenance.

**Strengths:**
- Self-contained plug-and-play modules simplify installation and allow incremental cleanroom expansion — add FFUs to the ceiling grid as production capacity grows
- Individual FFU replacement without system shutdown enables 24/7 operation; a failed FFU affects only its local area

**Weaknesses:**
- Noise level of 45-55 dBA at 1 m from hundreds of FFUs creates a fatiguing acoustic environment for operators during 8-12 hour shifts
- Power consumption of 100-300 W per FFU adds up to 27-81 kW for a 100 m² ISO 5 cleanroom — the single largest operating cost after process equipment electricity

### Laminar Flow Design

**Vertical laminar flow** (ceiling-to-floor) is the standard for semiconductor cleanrooms:

- **Principle**: Air flows in parallel streamlines from the HEPA/ULPA filter ceiling downward to the perforated raised floor. The unidirectional flow sweeps particles away from critical work areas. There is no mixing or recirculation within the clean zone — any particle generated is immediately carried downward and out.
- **Face velocity**: 0.3-0.5 m/s at the filter face. Below 0.3 m/s, the flow becomes unstable and turbulent eddies form. Above 0.5 m/s, energy costs increase disproportionately and turbulence is induced by the high velocity interacting with equipment and personnel.
- **Flow uniformity**: ±20% of the average face velocity across the entire filter ceiling. Achieved by balancing FFU speeds and ensuring the plenum above the filters is well-pressurized. Non-uniform flow creates dead zones where particles accumulate.
- **Ceiling coverage**: ISO 5 requires 100% HEPA ceiling coverage (every ceiling tile is a filter module). ISO 6-7 can use 60-80% coverage with blank ceiling panels between filters. ISO 8 can use 25-40% coverage. Higher coverage = more uniform laminar flow = lower particle counts.

**Horizontal laminar flow** (wall-to-wall) is used in some pharmaceutical and biomedical applications:

- Air flows from a HEPA-filtered wall across the room to a return wall on the opposite side. Less common in semiconductor fab because the long horizontal path allows particles generated upstream to contaminate downstream processes. Vertical flow keeps each floor-level workstation in its own clean column.

**Obstruction effects**:

- Any physical object (equipment, personnel, carts) in the laminar flow stream creates a downstream wake zone where particles can accumulate. The wake extends 5-10 obstruction-diameters downstream.
- **Design rule**: Position the most contamination-sensitive processes (lithography exposure, gate oxidation) upstream, closest to the filter ceiling. Place particle-generating processes (CMP, grinding, chemical processing) downstream or in separate service chases with dedicated exhaust.
- Personnel are the largest obstruction. A standing person creates a wake zone extending 1-2 m downstream at 0.45 m/s face velocity. This is one reason why cleanroom operators must stand still and move slowly — rapid movement creates turbulence that overwhelms the laminar flow.

**Strengths:**
- Vertical laminar flow at 0.3-0.5 m/s sweeps particles directly away from critical work areas in parallel streamlines with no mixing, providing predictable contamination control
- 100% HEPA ceiling coverage for ISO 5 guarantees every location receives filtered air first, with no recirculation zones

**Weaknesses:**
- Any obstruction (equipment, personnel, carts) creates a downstream wake zone 5-10 diameters long where particles accumulate — impossible to eliminate in a working cleanroom
- Face velocity above 0.5 m/s causes turbulence from equipment interaction and increases energy costs disproportionately, while below 0.3 m/s the flow becomes unstable

### Filter Integrity Testing

**DOP/PAO challenge test** (performed annually and after installation):

The integrity test verifies that the installed filter has no bypass leaks (at the gasket, frame, or media). It does NOT test the filter media efficiency — that is certified by the manufacturer.

1. **Generate challenge aerosol**: DOP (dioctyl phthalate, now largely replaced by PAO — polyalphaolefin) is vaporized and re-condensed to create a polydisperse aerosol with a mass median diameter of 0.3 μm (matching the MPPS). The aerosol is injected upstream of the filter at a concentration sufficient to produce a measurable signal.
2. **Scan the downstream face**: A photometer probe is passed over the entire downstream face of the filter at a scanning speed ≤5 cm/s, with the probe 25-50 mm from the media surface. The probe path must overlap by at least 50% between passes to ensure complete coverage.
3. **Acceptance criterion**: Any local reading exceeding 0.01% of the upstream concentration indicates a leak. For ULPA filters in ISO 3-4 environments, the criterion is tightened to 0.005%.
4. **Repair protocol**: Small media pinholes can be repaired with a maximum of three dabs of gel sealant or silicone, each no larger than 25 mm diameter. Larger tears or gasket leaks require filter replacement. A repaired filter must pass the integrity test again before the cleanroom returns to production.

**Strengths:**
- DOP/PAO challenge test detects bypass leaks at 0.01% of upstream concentration — finds defects invisible to the naked eye
- Scanning at ≤5 cm/s with 50% overlap ensures complete coverage of the filter face with no uninspected areas

**Weaknesses:**
- Annual integrity testing of hundreds of filter modules is labor-intensive (5-15 minutes per filter × 270 FFUs = 22-67 hours)
- PAO aerosol is an inhalation irritant; testing requires respiratory protection and adequate ventilation in the ceiling plenum

**Pressure drop monitoring**:

- Each FFU or filter bank should have a differential pressure gauge (magnahelic or electronic). The gauge measures the pressure drop across the filter. As particles accumulate, the pressure drop increases.
- **Baseline**: Record the initial pressure drop when the filter is new and clean. This is the reference point.
- **Replacement trigger**: When pressure drop reaches 2× the initial value (or the manufacturer's specified terminal pressure drop, whichever is lower), replace the filter. Operating beyond this point wastes fan energy and risks media rupture.
- **Trend analysis**: Plot pressure drop over time. A sudden increase indicates a process upset (excessive particle generation upstream). A gradual increase is normal filter loading. The rate of increase predicts remaining filter life.

### HEPA Filter Bootstrapping Sequence

Manufacturing HEPA filters from scratch requires several upstream capabilities:

1. **Glass fiber production**: Borosilicate glass batch is melted in a furnace (1400-1600°C) and fiberized through a centrifugal spinner (similar to mineral wool production). Fiber diameter is controlled by spinner speed and melt viscosity. This is a specialized glass fiber process — not the same as fiberglass insulation production.
2. **Media forming**: The glass fibers are wet-laid onto a moving screen (paper machine) with acrylic binder. The mat is dried and cured in an oven. Sheet thickness and density are controlled by the machine speed and slurry consistency.
3. **Pleating**: The flat media sheet is pleated on a rotary pleating machine. Pleat depth and spacing are set by the tooling. Separators are inserted between pleats.
4. **Frame fabrication**: Aluminum extrusion is cut and welded into rectangular frames. Gasket channels are formed into the frame edge.
5. **Assembly and testing**: Pleated media is bonded into the frame with polyurethane potting compound (seals media edges to frame). Each filter is tested for efficiency (particle penetration test at MPPS) and pressure drop before shipping.

### Energy Considerations

Cleanroom air handling is energy-intensive. A 100 m² ISO 5 cleanroom with 100% HEPA coverage at 0.45 m/s:

- **Total airflow**: 100 m² × 0.45 m/s × 3,600 s/h = 162,000 m³/h
- **Fan power**: ~50 kW for HEPA, ~100 kW for ULPA (at ~60% fan efficiency)
- **Cooling load**: 200-500 W/m² from process equipment = 20-50 kW
- **Annual energy**: ~500,000 kWh (fan + cooling combined), costing $50,000-100,000/year at $0.10-0.20/kWh
- **Air changes per hour**: 162,000 / (100 m² × 3 m ceiling height) = 540 ACH. This is 9× the minimum for ISO 5 (60 ACH). High air change rates improve particle clearance but waste energy.

Optimization strategies:
- Reduce ceiling coverage to the minimum required for the target ISO class
- Lower face velocity to 0.3 m/s during non-critical operations (nights, weekends)
- Use variable-speed FFUs that ramp down during unoccupied periods
- Stage cleanroom zones — ISO 5 only where critical, ISO 7-8 elsewhere

**Strengths:**
- Reducing face velocity to 0.3 m/s during non-critical operations cuts fan energy by 50% while maintaining adequate particle clearance
- Staged zoning (ISO 5 only where critical) reduces the high-cleanliness footprint and associated energy cost proportionally

**Weaknesses:**
- Even optimized, a 100 m² ISO 5 cleanroom consumes ~500,000 kWh/year ($50,000-100,000), representing a major ongoing operational expense
- Variable-speed FFU ramp-down during unoccupied periods risks contamination events if ramp-up is too slow when production resumes

### Filter Selection Guide

Choosing between HEPA and ULPA depends on the target ISO class and the sensitivity of the process:

| ISO Class | Minimum Filter | Coverage | Typical Application |
|-----------|---------------|----------|---------------------|
| ISO 3 | ULPA (99.999% @ 0.12 μm) | 100% | Sub-10 nm lithography, EUV |
| ISO 4 | ULPA (99.999% @ 0.12 μm) | 100% | Sub-micron lithography, gate oxidation |
| ISO 5 | HEPA (99.97% @ 0.3 μm) | 100% | Critical wafer processing, metrology |
| ISO 6 | HEPA (99.97% @ 0.3 μm) | 80-100% | Wafer cleaning, coating, support |
| ISO 7 | HEPA (99.97% @ 0.3 μm) | 60-80% | Gowning rooms, service corridors |
| ISO 8 | HEPA (99.97% @ 0.3 μm) | 25-40% | General manufacturing support |

**Cost implications**: ULPA filters cost 2-3× more than HEPA ($400-1200 vs. $200-400 per panel). ULPA systems require 2× the fan energy. However, the cost of contamination-caused defects far exceeds the filtration premium — a single spoiled wafer lot at a modern fab can cost $50,000-500,000.

### Filter Storage and Handling

- **Storage**: Filters must be stored in their original packaging in a clean, dry environment. Do not stack — the weight compresses the gaskets. Storage temperature: 10-35°C. Humidity: <80% RH. Shelf life: 5 years in original packaging.
- **Handling**: Carry filters by the frame, never by the media. The media is fragile and tears easily. Do not set filters face-down on surfaces. Use the protective plastic caps on the gasket during transport. Inspect each filter for shipping damage (dented frame, torn media, displaced gasket) before installation.
- **Installation sequence**: Remove protective caps → inspect gasket for damage → position filter in ceiling grid with airflow arrow pointing down → press firmly to compress gasket → verify seal visually. After installation, run the integrity test before commissioning the cleanroom.
- **Post-installation protection**: If the cleanroom is not immediately commissioned, cover the filter faces with clean plastic sheeting to prevent premature loading from construction dust.

### Materials

| Material | Use | Specification |
|----------|-----|---------------|
| Borosilicate glass fiber | Filter media | Fiber diameter 0.5-4 μm, SiO₂ >70% |
| Acrylic resin | Media binder | Non-outgassing, stable to 90°C |
| Aluminum extrusion | Filter frame | 6063-T5, powder-coated or anodized |
| Neoprene/closed-cell foam | Gasket | 10-15 mm width, 30-40% compression |
| Silicone gel | Sealant | Non-drying, re-usable |
| Polyurethane potting | Media-frame bond | Low-outgassing formulation |
| Corrugated aluminum | Pleat separator | Maintains pleat spacing under airflow pressure |
| Galvanized steel | Filter housing | Powder-coated, corrosion-resistant |

### Limitations

- **No chemical filtration**: HEPA/ULPA filters remove particles, not gases or vapors. Chemical vapor contamination (acid fumes, solvent vapors, ammonia) requires activated carbon filters or chemical scrubbers in a separate stage upstream of the particulate filters.
- **No living organism elimination**: While HEPA captures bacteria and fungi (0.5-5 μm), it does not kill them. Captured microorganisms can grow on the filter media if conditions are favorable (high humidity, nutrient availability). Biocidal-treated media and regular filter replacement prevent biological growth.
- **Finite capacity**: Every filter has a finite dust-holding capacity. In heavily loaded environments, pre-filters may need weekly replacement and HEPA filters may last only 1-2 years instead of 3-7 years. Pressure drop monitoring is the only reliable predictor of remaining filter life.
- **Bypass vulnerability**: A filter is only as good as its installation seal. A 1 mm gap in the gasket seal bypasses more particles than the entire filter face captures. This is why integrity testing (DOP/PAO scan) is mandatory after installation and annually thereafter.

### Safety

**DOP/PAO aerosol hazard**: The challenge aerosol used for filter integrity testing (PAO — polyalphaolefin, replacing DOP/dioctyl phthalate) is a fine mist with mass median diameter 0.3 μm. Inhalation of PAO aerosol at high concentrations causes respiratory irritation. Perform integrity testing with adequate ventilation. Wear N95 or better respirator when generating challenge aerosol in enclosed spaces.

**Fan-filter unit electrical hazard**: Individual FFUs draw 100-300 W at 120-240 VAC. A fully populated cleanroom ceiling has hundreds of FFUs. Arc flash hazard exists when servicing FFU electrical connections. De-energize and lock out before servicing. The FFU fan impeller can cause laceration — never reach into the fan housing while energized.

**Compressed air hazard in air showers**: Air shower nozzles deliver 20-30 m/s jet velocity at pressures of 2-4 bar. Direct exposure to air jets at close range can cause air embolism through broken skin. Never direct air shower nozzles toward eyes or open wounds.

**Gel sealant chemical exposure**: Non-drying silicone gel used for ULPA filter seals can cause skin irritation with prolonged contact. Wear nitrile gloves when handling gel seal material. Polyurethane potting compound used to bond media to frame is a skin sensitizer — avoid repeated exposure.

### See Also

- [Contamination Control](contamination-control.md) — gowning, monitoring, ESD, ISO classification
- [Facility Design & HVAC](facility-design.md) — walls, floors, ceiling, HVAC, pressure cascading
- [Photolithography Cleanrooms](../photolithography/cleanrooms.md) — semiconductor-specific cleanroom integration with fab processes
- [Health: Sanitation](../health/sanitation.md) — water purification, contamination principles (different scale and methodology)

### Equipment

| Equipment | Purpose | Specification |
|-----------|---------|---------------|
| FFU (fan-filter unit) | Ceiling-mounted air delivery | 610×610 mm, 0.3-0.5 m/s, 100-300 W |
| DOP/PAO aerosol generator | Filter integrity testing | 0.3 μm mass median diameter |
| Photometer | Leak scanning | 0.001% sensitivity minimum |
| Differential pressure gauge | Filter loading monitor | 0-1000 Pa range, ±2% accuracy |

---

*Part of the [Bootciv Tech Tree](../index.md) • [Clean Room Technology](./index.md) • [All Domains](../index.md)*
