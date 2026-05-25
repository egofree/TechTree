# Facility Design & HVAC

> **Node ID**: cleanrooms.facility-design
> **Domain**: [Clean Room Technology](./index.md)
> **Dependencies**: [`construction`](../construction/index.md), [`energy`](../energy/index.md), [`metals`](../metals/index.md)
> **Timeline**: Years 40-70
> **Outputs**: cleanroom_facilities, pressure_cascade_systems, raised_floor_systems, hvac_systems

### Overview

The physical facility is the structural envelope that houses clean room operations. A clean room is not a regular building with filters bolted on — it is a purpose-engineered structure where every surface, joint, penetration, and air path is designed for contamination control. The wall system must be airtight and non-shedding. The floor must drain static charges and return air. The ceiling must support filter modules and maintain level alignment. The HVAC system must deliver conditioned air at precise temperature (22±0.5°C) and humidity (43±3% RH) continuously, 24 hours per day, 365 days per year.

This capability covers modular wall systems, raised flooring, ceiling grids, make-up air handling, temperature and humidity control, positive pressure cascading, and airlock design. It does NOT cover filtration technology (see [HEPA/ULPA Filtration](hepa-ulpa-filtration.md)) or contamination protocols (see [Contamination Control](contamination-control.md)).

### Modular Wall Panel Construction

**Panel construction**:

Cleanroom walls use prefabricated sandwich panels — the same structural principle as insulated building panels, but with specialized surfaces:

- **Skins**: Steel (galvanized or stainless) or aluminum sheet, 0.5-1.0 mm thickness. Painted with epoxy or polyurethane paint (smooth, non-shedding, chemical-resistant). White or light gray color maximizes light reflectance and makes particle contamination visible.
- **Core**: Expanded polystyrene (EPS, cheapest, fire-rated with flame retardant), rockwool (mineral wool, best fire resistance, denser), or aluminum honeycomb (lightest, stiffest, most expensive). Core thickness: 50-100 mm provides structural stiffness and thermal insulation.
- **Surface smoothness**: <0.8 μm Ra (roughness average). Mirror-finish epoxy paint. This smoothness enables effective cleaning and minimizes particle adhesion. Any rougher surface traps particles that cannot be removed by wiping.

**Panel joining system**:

- **Cam-lock fasteners**: Panels interlock with rotating cam-lock fasteners embedded in the panel edges. Two adjacent panels hook together, and a cam lever rotates to draw them tight. No through-bolts, no exposed fasteners — every bolt head is a particle trap. The joint is sealed with silicone or polyurethane sealant applied between panel edges during assembly.
- **Joint sealing**: Continuous bead of non-outgassing silicone sealant (neutral-cure, not acetoxy — acetic acid off-gassing contaminates wafers) between all panel joints. The sealant fills any micro-gaps and creates an airtight, particle-tight connection. Sealant is tooled smooth with no recessed or raised beads that could collect particles.
- **Corner treatment**: Corners coved with 30-50 mm radius radius PVC or aluminum corner profiles. Sharp corners are prohibited — they are impossible to clean and collect particles. Cove radius must be large enough for a cleaning wipe to contact the entire surface.

**Wall penetrations**:

Every pipe, conduit, cable, and duct that passes through the cleanroom wall must be sealed:

- **Penetration boots**: Elastomeric (silicone or EPDM) boots that seal around the penetrating element and bond to the wall panel on both sides. The boot accommodates thermal expansion and vibration without losing the seal.
- **Conduit sealing**: Each electrical conduit penetration is sealed with fire-rated putty or expandable foam. Unsealed conduits are air leakage paths that compromise positive pressurization.
- **Pipe sealing**: Process pipes (water, chemicals, gases) pass through sealed wall sleeves with O-ring compression seals. The seal allows axial movement (thermal expansion) while maintaining an airtight barrier.
- **Design rule**: Minimize the number of penetrations. Route as many services as possible through the service chase (rear access corridor) rather than through the cleanroom wall. Every penetration is a potential leak point.

### Raised Floor Systems

The raised floor serves dual purposes: it provides the cleanroom working surface (perforated, anti-static tiles) and creates a return air plenum beneath for vertical laminar flow:

**Floor panel specifications**:

- **Panel size**: 600 × 600 mm standard (matching ceiling grid module). This modularity allows panels to be lifted for underfloor maintenance access.
- **Panel material**: Steel (galvanized or stainless) or aluminum. Aluminum is lighter and corrosion-resistant but more expensive. Steel is standard for most installations.
- **Perforation**: 20-25% open area for return airflow. Perforations are 2-5 mm diameter holes, evenly distributed. Higher open area improves return airflow uniformity but reduces structural load capacity.
- **Surface finish**: Conductive vinyl or epoxy coating. Surface resistance 10⁶-10⁹ Ω/square for ESD control. The coating must be smooth enough for cleaning but provide adequate slip resistance for personnel safety.
- **Load capacity**: 5-10 kPa for general access areas (personnel, carts). 20-30 kPa for equipment areas (process tools on raised floor). Heavy tools (ion implanters, large CVD reactors) may require structural reinforcement or direct slab mounting.

**Pedestal system**:

- **Pedestals**: Adjustable steel pedestals with a threaded stem for height adjustment. Base plate (100-150 mm square) is anchored to the structural slab with masonry bolts. Head plate supports the floor panel with corner pads.
- **Height**: 300-600 mm above structural slab. Greater height provides more plenum volume for return air, improving airflow uniformity. 400-500 mm is typical for ISO 5-6 cleanrooms.
- **Level tolerance**: ±1.5 mm across the entire floor. Uneven panels create turbulence in the return airflow and trip hazards for personnel. Level is set during installation and verified with a laser level.
- **Stringers**: Horizontal steel channels connecting pedestals at the top. Stringers provide lateral stability and prevent pedestal sway under dynamic loads (personnel walking, carts). Not always required at low heights (<300 mm) but recommended for all installations.
- **Grounding**: Each pedestal is electrically bonded to the building grounding system. The conductive floor panels discharge static through the pedestals to ground. Ground continuity is tested at installation and annually.

**Underfloor plenum**:

- The space between the structural slab and the raised floor is the return air plenum in vertical laminar flow cleanrooms. Air flows down through the perforated floor tiles, through the plenum, and back to the air handling units.
- **Plenum cleanliness**: The structural slab must be sealed (epoxy paint) and kept clean during construction. Any construction debris left in the plenum becomes a particle source. After construction, the plenum is vacuumed with HEPA-filtered vacuums before the floor is installed.
- **Obstructions**: Minimize underfloor obstructions (cables, pipes, structural members). Obstructions disrupt return airflow uniformity. Route cables in trays along the perimeter where possible.
- **Drainage**: The structural slab should slope toward floor drains (for wet cleaning and spill containment). The raised floor perimeter is sealed with a gasket to prevent underfloor air bypass.

### Ceiling Grid Systems

**Aluminum T-grid system**:

- **Grid module**: Standard 610 × 610 mm (2 × 2 ft) or 1220 × 610 mm (4 × 2 ft). The grid supports HEPA/ULPA filter modules, blank ceiling panels, and lighting fixtures.
- **Suspension**: Threaded rod hangers from the structural ceiling above, spaced at 1200-1500 mm intervals. Rod diameter: 6-10 mm. Hanger wire is NOT acceptable for cleanroom ceilings — it stretches under load and cannot maintain level.
- **Level tolerance**: ±1.5 mm across the entire ceiling. This is critical for laminar airflow uniformity — an uneven ceiling creates variations in the plenum pressure that cause non-uniform filter face velocity.
- **Grid material**: Aluminum extrusion (T-shaped cross section). Aluminum is lightweight, corrosion-resistant, and does not shed particles. The grid is painted white to match the ceiling panels.
- **Sealing**: Each filter module and blank panel sits on a gasket (neoprene or gel seal) in the grid. The gasket prevents unfiltered air from bypassing the filters through the grid joints. A single bypass leak can contaminate the entire area below.

**Lighting integration**:

- **Teardrop or flush-mounted fixtures**: No horizontal dust-collecting surfaces. Housing: white-painted steel with sealed acrylic or polycarbonate lens. No exposed screws or crevices.
- **Light levels**: 800-1200 lux at wafer height for visual inspection and alignment. 300-500 lux for general process areas.
- **Color rendering**: CRI >80 for accurate visual color matching (resist color inspection).
- **UV filtering**: Fixtures must block wavelengths below ~450 nm to prevent accidental photoresist exposure. UV-blocking sleeves over fluorescent tubes or UV-filtering lens material. Cleanrooms often appear slightly yellow for this reason.

### Positive Pressure Cascading

**Principle**: The cleanroom is maintained at a higher air pressure than surrounding areas. When doors open, clean air flows outward, preventing infiltration of contaminated air. The pressure cascade creates a one-way barrier:

**Typical pressure cascade**:

| Zone | Pressure Above Ambient | ISO Class |
|------|----------------------|-----------|
| Outside / corridor | 0 Pa (reference) | Uncontrolled |
| Pre-change room | +5 Pa | ISO 8 |
| Gowning room | +10 Pa | ISO 7 |
| Cleanroom | +15-25 Pa | ISO 5-6 |
| Critical zone (inside tool) | Higher than cleanroom | ISO 3-4 |

**Pressure maintenance**:

- The pressure differential is maintained by supplying slightly more air than is exhausted. The excess air leaks out through door gaps, wall penetrations, and exhaust systems, creating outward flow.
- **Make-up air**: Typically 15-30% of total circulation is fresh outside air. The remainder is recirculated through HEPA filters. Higher make-up rates dilute internal contaminants but increase energy costs (heating, cooling, dehumidifying outside air).
- **Pressure monitoring**: Magnahelic gauges or electronic differential pressure transmitters at each zone boundary. Alarm if pressure differential drops below the minimum threshold. Continuous data logging for regulatory compliance.
- **Interlocked doors**: Personnel and material airlocks have interlocked doors — one must close before the other opens. This maintains the pressure barrier even during transit. Door interlocks are fail-safe (both doors lock if power is lost, requiring manual override to prevent both opening simultaneously).

**Airlock design**:

- **Personnel airlock**: A small room (1.5 × 2 m) with interlocked doors on opposite walls. The operator enters from the gowning room, the inner door closes and locks, then the outer door to the cleanroom opens. Air shower: high-velocity filtered air jets (20-30 nozzles at 20-30 m/s) bombard the gowned operator for 15-30 seconds, dislodging particles from the garment surface. The airlock maintains +5 Pa above the gowning room.
- **Material airlock (pass-through)**: A double-door chamber (0.6 × 0.6 × 0.6 m or larger) built into the cleanroom wall. Materials are loaded from the service corridor side, wiped with IPA-dampened lint-free wipes, the outer door closes and locks, then the inner door opens for retrieval inside the cleanroom. Eliminates the need to carry materials through the gowning room.

### Temperature and Humidity Control

**Temperature control (22±0.5°C)**:

Tight temperature control is essential because photoresist dimensions are temperature-sensitive:

- Silicon thermal expansion: 2.6 × 10⁻⁶/°C. A 300 mm wafer changes length by 0.78 μm per °C — at 5 nm node, this is 156× the feature size.
- Photoresist viscosity changes with temperature, affecting spin-coated thickness uniformity. A 1°C change can alter resist thickness by 1-3%.
- Metal deposition rates are temperature-dependent. Consistent temperature ensures reproducible film thickness.

**Cooling system design**:

- **Chilled water**: Supplied at ~7°C from central chillers to air handling units. Chiller capacity: 50-200 W/m² of cleanroom floor area (internal heat load from process equipment: vacuum pumps, RF generators, bake plates, and the FFUs themselves).
- **Redundancy**: N+1 chiller configuration ensures continuous cooling during maintenance. A cleanroom that loses cooling rapidly exceeds temperature tolerance — process equipment generates significant heat.
- **Process cooling water**: Separate loop at 15-25°C for tool cooling (etchers, CVD reactors, ion implanters, vacuum pumps). Monitor conductivity to detect heat exchanger leaks into the cooling loop.

**Humidity control (43±3% RH)**:

- **Low humidity risk**: Below 30% RH, static charge accumulation accelerates dangerously (ESD risk). Below 20% RH, virtually all surfaces accumulate kilovolt-level charges.
- **High humidity risk**: Above 55% RH, photoresist absorbs moisture, affecting exposure and development. Humid particles agglomerate and settle faster (changing particle size distribution). Condensation on cold surfaces creates water spots and corrosion.
- **Dehumidification**: Chilled water cooling coils below the dew point condense moisture from the air. The condensate is drained away. Over-cooling followed by reheat maintains both temperature and humidity within tolerance.
- **Humidification**: Clean steam (steam generated from deionized water, free of minerals and boiler chemicals) injected into the air stream. Potable steam (from treated boiler water) is NOT acceptable — it introduces mineral particles.

### HVAC System Architecture

**Air handling unit (AHU)**:

The AHU conditions outside air and recirculated air to the required temperature and humidity:

1. **Outside air intake**: With coarse filter (MERV 8) and damper for volume control. Located on the building roof or wall, away from exhaust stacks and loading docks.
2. **Pre-filter**: MERV 11 pleated filter removes bulk of particulates, extending downstream HEPA life.
3. **Cooling coil**: Chilled water at 7°C. Cools air below the dew point for dehumidification, then reheats to target temperature. The cooling coil is the primary dehumidification mechanism.
4. **Heating coil**: Hot water or electric reheat. Brings dehumidified air back to the 22°C setpoint. Required because the cooling coil overshoots temperature during dehumidification.
5. **Humidifier**: Clean steam injection. Adds moisture when the air is too dry (common in winter when outside air is cold and dry).
6. **Fan**: Centrifugal blower sized for the total airflow (recirculated + make-up). Must overcome the pressure drop of pre-filters, cooling/heating coils, ductwork, and HEPA/ULPA final filters.
7. **Supply ductwork**: Galvanized steel or aluminum, internally lined with acoustic insulation (fiberglass with foil facing — the foil prevents fiber shedding into the air stream). All duct joints sealed with mastic or gasketed flanges.

**Recirculation vs. once-through**:

- **Recirculation system**: 70-85% of the air is recirculated through HEPA filters back to the cleanroom. 15-30% is fresh make-up air. Recirculation is energy-efficient (less outside air to heat/cool/dehumidify) but dilutes contaminants more slowly.
- **Once-through system**: 100% outside air, conditioned and filtered, passed through the cleanroom once, and exhausted. Used for cleanrooms with hazardous processes (toxic gas exhaust, solvent evaporation) where recirculation would concentrate contaminants. Energy cost is 3-5× higher than recirculation.

### Make-Up Air Details

**Make-up air volume calculation**:

The make-up air system must replace air exhausted by:
- Process tool exhaust (wet benches, solvent benches, chemical vapor deposition exhaust)
- Building leakage (door gaps, wall penetrations, ceiling penetrations)
- Pressurization excess (the air that leaks out through the building envelope to maintain positive pressure)

Typical make-up air: 15-30% of total cleanroom airflow. For a 100 m² ISO 5 cleanroom with 100% HEPA coverage at 0.45 m/s:
- Total airflow: ~162,000 m³/h
- Make-up air: ~24,000-48,000 m³/h
- This make-up air must be heated/cooled/dehumidified from outdoor conditions to 22°C / 43% RH — the dominant energy cost in cleanroom operation.

**Make-up air treatment**:

1. **Pre-filtration**: MERV 11 pleated filter removes outdoor dust, pollen, and insects.
2. **Pre-conditioning**: Heat recovery from exhaust air (heat exchanger) reduces the heating/cooling load by 40-60%. This is the single most effective energy conservation measure for cleanrooms.
3. **Cooling and dehumidification**: Chilled water coil cools to below dew point.
4. **Reheating**: Electric or hot water coil brings air to 22°C.
5. **Final filtration**: HEPA filter on the make-up air stream ensures the fresh air does not introduce particles.

### Support Systems

**Bulk gas distribution**:

- High-purity gases (N₂, Ar, O₂, compressed air) distributed through stainless steel tubing (304L or 316L, electropolished interior). Orbital-welded joints (no mechanical fittings inside the cleanroom). Gas panels with dual-stage regulators and purge valves for safe gas changeover.
- Gas purity requirements: N₂ at 99.999% (5N) minimum for inerting; Ar at 6N (99.9999%) for sputtering; O₂ at 4N (99.99%) for oxidation. Gas filters (0.003 μm) at the point of use remove any particles introduced in the distribution system.

**Bulk chemical distribution**:

- Centralized chemical storage room with pumped distribution lines to process stations. Benefits: fewer bottles in the cleanroom (reduced contamination risk), automated dispensing, leak detection on distribution lines.
- Materials: PTFE or PFA tubing, double-contained for hazardous chemicals (HF, H₂SO₄). Distribution pump: diaphragm type (no seals that leak), with leak detector in the secondary containment.

**Waste collection**:

- Separate drain systems for acid waste, solvent waste, and general waste. Acid waste collected in chemical-resistant tanks (HDPE or FRP), neutralized before discharge. Solvent waste collected in grounded metal tanks, recycled or incinerated. Never mix acid and solvent waste streams.

### Cleanroom Floor Plan and Workflow

**Equipment placement principles**:

1. **Upstream placement**: Most contamination-sensitive processes (photolithography exposure, gate oxide growth) positioned closest to the HEPA filter ceiling, upstream in the laminar airflow. These processes receive the cleanest air first.
2. **Downstream isolation**: Particle-generating equipment (sawing, grinding, CMP) placed downstream or in separate service chases with dedicated exhaust. This prevents their particles from contaminating upstream processes.
3. **Process flow**: Equipment arranged in wafer processing sequence (clean → coat → expose → develop → etch → deposit → test) to minimize wafer transport distance. Each unnecessary transport step increases contamination risk.
4. **Service chase**: A separate corridor behind the cleanroom wall houses pumps, gas panels, electrical distribution, and exhaust ducting. Maintenance personnel access equipment from the chase side without entering the cleanroom, keeping tool maintenance activities (which generate particles) outside the clean envelope.

### Design Parameters Summary

| Parameter | Value | Tolerance | Notes |
|-----------|-------|-----------|-------|
| Temperature | 22°C | ±0.5°C | Photoresist sensitivity |
| Relative humidity | 43% RH | ±3% | ESD/moisture balance |
| Positive pressure | +15-25 Pa | ±5 Pa | Above ambient |
| Air changes/hour (ISO 5) | ≥60 | — | Unidirectional flow preferred |
| Air changes/hour (ISO 7) | 30-70 | — | Turbulent flow |
| Face velocity | 0.3-0.5 m/s | ±20% | At filter face |
| Ceiling coverage (ISO 5) | 100% | — | All tiles are filter modules |
| Ceiling coverage (ISO 7) | 60-80% | — | Blank tiles between filters |
| Floor level tolerance | ±1.5 mm | — | Across entire floor |
| Ceiling level tolerance | ±1.5 mm | — | Across entire ceiling |
| Wall surface smoothness | <0.8 μm Ra | — | Mirror-finish epoxy |

### See Also

- [HEPA/ULPA Filtration](hepa-ulpa-filtration.md) — filter technology integrated into the ceiling system
- [Contamination Control](contamination-control.md) — operational protocols within the facility
- [Photolithography Cleanrooms](../photolithography/cleanrooms.md) — semiconductor-specific facility integration
- [Construction](../construction/index.md) — general building construction principles (different discipline)
- [Energy](../energy/index.md) — power requirements for HVAC and support systems

---

*Part of the [Bootciv Tech Tree](../index.md) • [Clean Room Technology](./index.md) • [All Domains](../index.md)*
