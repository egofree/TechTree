# Contamination Control

> **Node ID**: cleanrooms.contamination-control
> **Domain**: [Clean Room Technology](./index.md)
> **Dependencies**: None (root capability)
> **Enables**: None (leaf capability)
> **Timeline**: Years 40-70
> **Outputs**: contamination_control_protocols, iso_classification, esd_control, particle_monitoring
> **Critical**: Yes — semiconductor fabrication at sub-micron nodes is impossible without contamination control; a single particle destroys a die

### Overview

Contamination control is the operational discipline that keeps a clean room clean. Filtration removes particles from the air supply (see [HEPA/ULPA Filtration](hepa-ulpa-filtration.md)), but the facility itself generates particles continuously — from people, processes, equipment, and materials. Without rigorous contamination control protocols, even the most expensive HEPA/ULPA filtration system cannot maintain ISO Class 5 or better.

A single 100 nm particle on a semiconductor die can destroy it. At 5 nm process nodes, the critical defect size is 2.5-5 nm — a single bacterium (500-5000 nm) is a boulder by comparison. Contamination control at this scale requires a systems approach: garment engineering, behavioral protocols, continuous monitoring, ESD prevention, and ISO classification management.

This capability covers contamination sources and their control, garment systems, particle monitoring, ESD control, ISO 14644-1 classification, and personnel training. It does NOT cover filtration hardware (see [HEPA/ULPA Filtration](hepa-ulpa-filtration.md)) or facility construction (see [Facility Design & HVAC](facility-design.md)).

### ISO 14644-1 Cleanroom Classification

The ISO 14644-1 standard defines cleanroom classes by the maximum allowable particle concentration (particles per cubic meter) at specified particle sizes. This is the definitive classification system used worldwide:

| ISO Class | ≥0.1 μm | ≥0.2 μm | ≥0.3 μm | ≥0.5 μm | ≥1.0 μm | ≥5.0 μm | Typical Application |
|-----------|---------|---------|---------|---------|---------|---------|---------------------|
| ISO 1 | 10 | 2 | — | — | — | — | Theoretical (research only) |
| ISO 2 | 100 | 24 | 10 | 4 | — | — | Theoretical (research only) |
| ISO 3 | 1,000 | 237 | 102 | 35 | 8 | — | Extreme sub-micron fab |
| ISO 4 | 10,000 | 2,370 | 1,020 | 352 | 83 | — | Advanced semiconductor lithography |
| ISO 5 | 100,000 | 23,700 | 10,200 | 3,520 | 832 | 29 | Critical lithography, gate oxidation |
| ISO 6 | 1,000,000 | 237,000 | 102,000 | 35,200 | 8,320 | 293 | Wafer processing support areas |
| ISO 7 | — | — | — | 352,000 | 83,200 | 2,930 | Gowning rooms, service corridors |
| ISO 8 | — | — | — | 3,520,000 | 832,000 | 29,300 | General manufacturing support |
| ISO 9 | — | — | — | 35,200,000 | 8,320,000 | 293,000 | Ambient air (reference only) |

**Key relationships**:

- The particle concentration formula: Cn = 10^N × (0.1/D)^2.08, where N is the ISO class number and D is the particle diameter in μm.
- **Air change rate correlation**: ISO 5 requires ≥60 air changes per hour (ACH) for turbulent flow, or unidirectional flow at 0.3-0.5 m/s. ISO 6: 70-160 ACH. ISO 7: 30-70 ACH. ISO 8: 10-25 ACH. Higher ACH = faster particle clearance = lower steady-state concentration.
- **Recovery time**: After a contamination event, the time to return to specification is approximately t_recovery ≈ -ln(C_target/C_initial) × (V/Q), where V is room volume and Q is airflow rate. For ISO 5 at 60 ACH, recovery from a 10× particle spike takes ~3-5 minutes.

**Strengths:**
- Quantitative standard: particle concentration formula (Cn = 10^N × (0.1/D)^2.08) enables objective classification and verification with instruments
- Recovery time is predictable from air change rate and room volume, allowing rational facility design for any target cleanliness level

**Weaknesses:**
- Classification measures airborne particles only — does not address surface contamination, molecular contamination, or electrostatic discharge risks
- Higher ISO classes (lower numbers) require exponentially more air changes (ISO 5 at 60 ACH vs. ISO 8 at 10-25 ACH), driving energy costs up dramatically

### Contamination Sources

**People — the dominant source**:

A fully gowned cleanroom operator at rest emits approximately 100,000 particles ≥0.3 μm per minute. During moderate activity (walking, reaching), this rises to 1,000,000 particles per minute. The primary sources are:

- **Skin flakes**: Humans shed ~10⁹ skin cells per day (20-30 μm each, carrying bacteria and oils). Full-body garments with integrated hoods and face covers contain ~98% of skin flakes. The remaining 2% escape through the face opening and fabric pores.
- **Breath droplets**: Exhaled breath contains 1-5 μm moisture droplets carrying bacteria and salts. Face masks capture most but not all. Speaking produces 5-10× more droplets than quiet breathing.
- **Hair fragments**: Hair shedding is continuous. Bouffant caps must cover ALL hair — any exposed scalp or facial hair is a direct particle source.
- **Garment lint**: Even cleanroom-rated garments shed some fibers. Polyester sheds less than Tyvek (spun-bonded polyethylene), which is why polyester is preferred for production cleanrooms.

**Process-generated contamination**:

- **Metal evaporation**: Evaporation sources deposit metal on chamber walls. Flaking metal films generate particles. Regular chamber cleaning (wet or plasma) prevents buildup.
- **Photoresist spin coating**: Generates a fine mist of resist droplets. Coater cup with exhaust captures most mist. Cups require regular cleaning to prevent dried resist flakes from becoming airborne.
- **Chemical reactions**: Etch processes produce gaseous byproducts that condense in exhaust ducts. Condensate particles can be entrained in reverse airflow. Exhaust system design must prevent backflow.
- **CMP (chemical mechanical polishing)**: Generates slurry spray and silicon dioxide particles. CMP tools are enclosed with dedicated exhaust and wet vacuum collection.

**Equipment-generated contamination**:

- **Outgassing**: Plastics (cable insulation, wafer carriers, gaskets) release volatile organic compounds (VOCs) under vacuum or elevated temperature. These deposit as thin organic films on wafer surfaces. Low-outgassing materials (PTFE, PFA, stainless steel) are mandatory for vacuum-contact components.
- **Vibration**: Mechanical vibration from pumps and motors transmits through the floor to sensitive tools. Vibration generates particles from moving parts and degrades lithographic resolution. Isolate vibration-sensitive tools on separate inertia blocks.
- **Bearings and motors**: Sealed bearings with cleanroom-rated lubricant (low-volatility perfluorinated polyether, PFPE) minimize particle generation from rotating equipment.

**Strengths:**
- Identifying contamination sources enables targeted countermeasures rather than blanket approaches (e.g., knowing people emit 100,000+ particles/min justifies garment engineering investment)
- Contamination sources are well-characterized with quantitative emission rates, allowing modeling and budgeting of particle loads

**Weaknesses:**
- People remain the dominant source regardless of garment quality — eliminating 100% of human-generated particles requires full automation
- Process-generated contamination (evaporation, CMP, etch byproducts) cannot be eliminated, only managed through enclosure and exhaust design

### Garment Systems

**Materials**:

- **Polyester (woven)**: Preferred for production cleanrooms. Continuous-filament woven fabric with no staple fibers to shed. Reusable for 50+ wash cycles. Excellent particle containment. Constructed with sealed or bound seams — no raw edges.
- **Tyvek (spun-bonded polyethylene)**: Disposable, inexpensive, good particle containment but lower durability. Used for visitor garments or one-time-entry applications. Not recommended for daily production use due to limited reuse (1-3 wearings before degradation).
- **Polypropylene (nonwoven)**: Low-cost disposable option. Moderate particle containment. Used in ISO 7-8 environments where garment requirements are less stringent.

**Garment construction specifications**:

- **Coverall (bunny suit)**: Full-body coverage with integrated hood or separate hood with face opening. Snap closures or velcro — no zippers, buttons, or pockets (all are particle sources). Sealed or bound seams with no exposed raw edges. Ankle cuffs with elastic or snap closures. No exposed skin when properly worn.
- **Gloves**: Nitrile preferred (better chemical resistance than latex, no latex allergy issues). Powder-free (powder is a severe contamination source). Two pairs worn — inner pair donned before the bunny suit, outer pair over the suit cuffs. Double-gloving prevents skin exposure when the outer glove develops a pinhole or tear.
- **Shoe covers/boot covers**: Over-shoe booties that seal around the ankle, worn over street shoes. Over-boot covers that extend to the knee, sealed to the bunny suit at the calf. Two-layer system traps street-shoe particles.
- **Face mask**: Covers nose and mouth. High-filtration efficiency (≥95% at 0.3 μm, equivalent to N95 standard). Prevents breath droplets from entering the clean zone.

**Gowning protocol** (order matters — cover dirtiest areas first):

1. **Hair cover** (bouffant cap): Covers ALL hair. No exposed scalp, sideburns, or facial hair. The bouffant cap is the first item because hair is a continuous particle emitter.
2. **Shoe covers**: Over-shoe booties. Seal around ankle. Remove street-shoe particles before entering the gowning room.
3. **Face mask**: Covers nose and mouth. Prevents breath droplets. Position before the bunny suit so the suit does not touch the unprotected face.
4. **First pair of gloves** (nitrile, powder-free): Don before the bunny suit to keep inner gloves clean. Hands touch the dirtiest surfaces (shoes, face, hair) during gowning.
5. **Bunny suit** (coverall with hood): Step into legs, pull up, insert arms, close front snaps. Integrated hood covers head and neck. Sealed seams face outward.
6. **Second pair of gloves**: Over the bunny suit cuffs. Double-gloving ensures no skin exposure if the outer glove fails.
7. **Boot covers**: Over the bunny suit legs, sealed to the suit at the knee. Creates a continuous barrier from head to toe.

**Garment laundry and lifecycle**:

- Specialized cleanroom laundry: ultra-pure water wash, non-ionic detergent, drying in HEPA-filtered environment.
- Helmke drum test or body box test for particle shedding after each wash cycle.
- Garment tracking by serial number through the laundry cycle to enforce change schedule.
- **Change frequency**: Daily for ISO 4-5. Twice-weekly for ISO 6. Weekly for ISO 7-8.
- **Retirement**: After 30-50 wash cycles, or when particle shedding exceeds specification, whichever comes first.

**Strengths:**
- Polyester garments are reusable for 50+ wash cycles, reducing waste and long-term cost compared to disposable options
- Double-gloving and double boot-cover system provides redundancy — the outer layer can fail without exposing skin

**Weaknesses:**
- Gowning takes 5-10 minutes per entry and must follow exact sequence — any deviation compromises the seal
- Full bunny suit with hood causes heat stress during 8-12 hour shifts in 22°C environments; personnel productivity decreases with comfort

### Particle Monitoring Systems

**Continuous airborne particle counters**:

- **Principle**: Laser scattering. A laser beam illuminates a sample volume of air. Particles passing through the beam scatter light. A photodetector measures the scattered light intensity, which is proportional to particle size. Each particle is counted individually.
- **Sizing channels**: Typical multi-channel counters measure ≥0.1, ≥0.2, ≥0.3, ≥0.5, ≥1.0, and ≥5.0 μm simultaneously. The channel thresholds correspond to the ISO 14644-1 classification particle sizes.
- **Sample flow rate**: 1 CFM (cubic foot per minute, 28.3 L/min) is standard. Higher flow rates (2-3 CFM) provide better statistical confidence for ISO 3-4 environments where particle counts are very low.
- **Placement**: Critical locations include near process tools (especially lithography steppers), at return air grilles (indicates room-wide cleanliness), and in the gowning room (verifies gowning protocol effectiveness).
- **Alarm thresholds**: Set at the ISO class limit for the room. For ISO 5, alarm at >3,520 particles/m³ ≥0.5 μm (averaged over 1 minute). Alarms trigger investigation — particle spike indicates a problem (torn filter, process upset, gowning failure).

**Continuous monitoring data management**:

- All particle count data logged continuously (every 1-60 seconds depending on the monitoring system) to a central database.
- Trend analysis software plots particle counts over time. Sudden spikes require immediate investigation. Gradual upward trends indicate filter loading or deteriorating process conditions.
- Statistical process control (SPC) charts with upper control limits based on historical data. Points outside control limits trigger corrective action, even if they are below the ISO class alarm threshold.
- Data retention: Minimum 2 years for regulatory compliance and trend analysis. Semiconductor fabs often retain data for the lifetime of the product (10-20 years) for failure analysis correlation.

**Surface particle monitoring**:

- **Witness plates**: Clean, flat surfaces (silicon wafers or glass slides) placed at critical locations for a defined period (typically 24-168 hours). Particles settling on the plate are counted under a microscope or with a surface particle counter. Measures deposition rate (particles/cm²/hour), which is more relevant than airborne concentration for surface contamination assessment.
- **Contact particle counters**: Handheld instruments that count particles on surfaces (work surfaces, equipment, wafer carriers). Useful for routine cleaning verification and post-maintenance inspection.

**Strengths:**
- Continuous laser-scattering particle counters provide real-time contamination data, enabling immediate detection of filter failures and gowning breaches
- Statistical process control (SPC) analysis of monitoring data detects gradual trends (filter loading) before they cause yield loss

**Weaknesses:**
- Particle counters measure quantity and size but not composition — a count spike cannot identify the source (human, process, or equipment) without additional investigation
- Monitoring equipment is expensive (multi-channel counters: $5,000-20,000 each) and requires annual calibration against traceable standards

### Electrostatic Discharge (ESD) Control

ESD destroys MOS gate oxides at discharge voltages as low as 50 V. A person walking on a synthetic floor accumulates 5-20 kV. ESD control is mandatory for all semiconductor and electronics clean rooms:

**Human body model (HBM)**: The standard ESD threat model. 100 pF capacitor charged to a voltage, discharged through 1.5 kΩ to the device under test. A person walking on a synthetic floor is approximately equivalent to 100 pF at 5-20 kV. Discharge energy at 5 kV: E = ½CV² = ½ × 100 × 10⁻¹² × 5000² = 1.25 mJ. This is enough to vaporize a 1 μm aluminum trace.

**ESD countermeasures — layered defense**:

1. **Conductive flooring**: Vinyl or epoxy flooring with conductive filler (carbon or metallic particles). Surface resistance: 10⁶-10⁹ Ω/square. Grounded through the pedestal system to building earth. The floor drains static charge from personnel as they walk, preventing voltage accumulation.
2. **Grounded wrist straps**: 1 MΩ current-limiting resistor in series to ground. The resistor limits discharge current to safe levels for the person (maximum 0.22 mA at 220 V line voltage fault). Worn at all times when handling wafers, devices, or ESD-sensitive components. Wrist strap continuity tested daily — a failed strap provides no protection.
3. **Ionizer systems**: Neutralize static charges on insulators that cannot be grounded (wafer surfaces, plastic wafer carriers, display screens).
   - **Corona ionizers**: High-voltage needles (±5-10 kV) generate positive and negative ions. AC ionizers alternate polarity, providing balanced ion output. Balance adjustment: ±50 V offset from zero (measured with a charged plate monitor). Require periodic needle cleaning (contamination reduces ion output).
   - **Alpha ionizers**: Polonium-210 (Po-210) radioactive sources emit alpha particles that ionize air molecules. No power required. Limited lifetime (Po-210 half-life = 138 days; replace every 12-18 months). Regulatory issues with radioactive materials.
   - **Air-assisted ionizers**: Fan blows ionized air toward the work surface, extending effective range from ~100 mm (passive) to 500-1000 mm. Used at wafer handling stations and inspection areas.
4. **Humidity control**: Maintain 40-50% RH. Below 30% RH, static buildup increases dramatically. Above 60% RH, condensation and corrosion risks increase. The humidity sweet spot minimizes both ESD and moisture-related defects.

**ESD-safe workstations**:

- Grounded work surfaces (conductive mat with 1 MΩ resistor to ground)
- All metal tools and fixtures grounded
- ESD-safe containers for wafers and devices (conductive or dissipative plastic, surface resistance 10⁴-10¹¹ Ω)
- Ionizers positioned within 500 mm of the work surface
- No synthetic clothing or hair products (charge generators)
- Daily wrist strap testing and heel strap testing (for standing operators)

**Strengths:**
- Layered defense (flooring + wrist straps + ionizers + humidity control) provides redundancy — no single failure causes an ESD event
- Conductive flooring at 10⁶-10⁹ Ω/square drains static continuously as personnel walk, preventing voltage accumulation without requiring active compliance

**Weaknesses:**
- Wrist straps tether operators to ground points, restricting movement — incompatible with mobile wafer transport or equipment maintenance tasks
- Ionizer needles degrade and accumulate contamination, requiring cleaning every 2-4 weeks; neglected ionizers produce unbalanced ion output that charges surfaces instead of neutralizing them

### Personnel Training Requirements

**Initial cleanroom training** (before first entry):

- Gowning procedure: demonstrated proficiency in correct order, with no exposed skin or hair violations.
- Movement and behavior rules: no rapid movements, no speaking near open wafers, no touching wafer surfaces directly.
- Prohibited items: no cosmetics, perfumes, pencils, paper, food, or drink. No personal electronics (phones, watches). Cleanroom-rated pens only.
- Emergency procedures: fire evacuation routes, chemical spill response, emergency shower and eyewash locations.

**Annual recertification**:

- Gowning proficiency test: particle shedding measurement in a body box counter. The operator gowns up inside the body box, which measures particles emitted during and after gowning. Must meet the ISO class particle shedding specification.
- Written test on protocols, emergency procedures, and contamination control principles.
- Practical demonstration of chemical spill response and emergency shower use.

**Contamination awareness**:

- Training must convey WHY protocols exist, not just WHAT to do. Operators who understand that a single skin flake can destroy a $10,000 wafer are more motivated to follow gowning procedures meticulously.
- Visual aids: projected particle counter displays showing real-time counts reinforce the connection between behavior and cleanliness.
- Incident review: when contamination events occur, conduct a root cause analysis and share findings (anonymized) with all cleanroom personnel.

**Strengths:**
- Body box testing provides objective, quantitative verification of gowning proficiency — cannot be faked
- Understanding the "why" behind protocols (single skin flake = destroyed wafer) improves compliance more than rule memorization alone

**Weaknesses:**
- Training is time-consuming (4-8 hours initial + annual recertification) and must be repeated for every new hire
- Body box testing equipment costs $50,000-100,000 and requires dedicated space; smaller facilities may skip this verification

### Recovery After Contamination Events

**Particle spike recovery**:

After a transient particle event (dropped wafer, door left open, torn garment):

- The cleanroom returns to specification in approximately 3-5 air change cycles.
- For ISO 5 at 60 ACH (one air change per minute), recovery takes 3-5 minutes.
- For ISO 7 at 30 ACH (one air change every 2 minutes), recovery takes 6-10 minutes.
- Do NOT resume wafer processing until particle counts at all monitoring points have returned to baseline for at least 5 minutes.

**Chemical spill recovery**:

- Contain immediately with absorbent pads (polypropylene, chemical-resistant).
- Increase local exhaust ventilation.
- Wipe residual with IPA-dampened lint-free wipes.
- Monitor airborne solvent concentration with photoionization detector (PID) until readings return to baseline.
- Do NOT resume operations until the area is verified clean by surface particle count.

**Post-maintenance recovery**:

- Run air handling at full capacity for 30-60 minutes after any maintenance that opens equipment or the cleanroom envelope.
- Wipe all accessible surfaces in the affected area.
- Verify particle counts at the nearest monitoring station before resuming production.

**Strengths:**
- Recovery time is predictable from air change rate: ISO 5 at 60 ACH recovers in 3-5 minutes, enabling rational decisions about when to resume production
- Chemical spill recovery protocol (contain → ventilate → wipe → verify) is straightforward and uses standard cleanroom supplies

**Weaknesses:**
- Post-maintenance recovery requires 30-60 minutes at full air handling capacity, during which the cleanroom is unproductive
- Chemical spill recovery with IPA-dampened wipes introduces solvent vapor that must be monitored to baseline before resuming operations

### Contamination Control for Different ISO Classes

The rigor of contamination control protocols scales with the target ISO class. Requirements become progressively more stringent:

| Protocol | ISO 7-8 | ISO 5-6 | ISO 3-4 |
|----------|---------|---------|---------|
| Garment change | Weekly | Daily | Every entry |
| Garment type | Polypropylene coverall | Polyester coverall + hood | Polyester coverall + integrated hood + face cover |
| Gloves | Single nitrile | Double nitrile | Double nitrile, changed every 2 hours |
| Face mask | Surgical mask | N95 equivalent | Full face cover with exhalation filter |
| Shoe covers | Single booties | Double booties + over-boots | Double booties + over-boots + air shower |
| Particle monitoring | Weekly grab samples | Continuous at critical points | Continuous at all points + surface monitoring |
| Gowning test | Visual inspection | Body box test quarterly | Body box test per entry |
| Behavioral rules | No food, slow movement | No speaking near wafers, minimal movement | Stand still at workstation, no unnecessary movement |
| Cleaning | Daily wipe-down | Shift-start and shift-end wipe-down | Continuous wipe-down + weekly deep clean |

**Strengths:**
- Scaling table provides clear, actionable guidance for each ISO class — no ambiguity about what protocol level is required
- Higher ISO classes build on lower ones incrementally (same fundamental protocols, increased rigor), reducing training complexity

**Weaknesses:**
- The gap between ISO 5 and ISO 3 requirements is enormous (daily garment change vs. every entry, continuous monitoring vs. weekly grab samples), requiring separate facility designs for each tier
- ISO 3-4 requirements (stand still at workstation, continuous wipe-down) severely limit personnel productivity and are incompatible with manual wafer handling

### Materials

| Material | Use | Specification |
|----------|-----|---------------|
| Polyester (continuous filament) | Cleanroom garments | Woven, sealed seams, 50+ wash cycles |
| Nitrile rubber | Gloves | Powder-free, 0.08-0.15 mm thickness |
| Polypropylene (nonwoven) | Shoe covers, boot covers | Low-lint, disposable |
| Bouffant cap (polypropylene) | Hair cover | Covers all hair, elastic edge |
| Conductive vinyl | ESD flooring | 10⁶-10⁹ Ω/square surface resistance |
| Carbon-loaded foam | Wrist strap band | Adjustable, 1 MΩ resistor inline |

### Limitations

- **People are always the weakest link**: Even perfectly gowned operators emit 100,000+ particles per minute. The best contamination control strategy minimizes the number of people in the cleanroom (automation, robotic wafer handling, service chase access).
- **No protocol eliminates all contamination**: Cleanrooms manage contamination to acceptable levels for the process, not to zero particles. ISO 3 still allows 1,000 particles/m³ at 0.1 μm. The question is whether the remaining contamination causes defects at an acceptable rate (yield).
- **Protocol compliance degrades over time**: Personnel become complacent, skip gowning steps, or develop bad habits. Regular auditing, body box testing, and particle monitoring provide objective compliance checks.

### Safety

**Chemical exposure in cleaning**: IPA (isopropyl alcohol) used for surface wipe-down has a flash point of 12°C and is flammable. Use in well-ventilated areas away from ignition sources. Wear nitrile gloves and safety glasses. Isopropanol vapor causes eye and respiratory irritation at concentrations above 400 ppm (TWA TLV).

**ESD electrical hazards**: Conductive flooring and grounded wrist straps carry 1 MΩ current-limiting resistors, but line voltage faults can still deliver 0.22 mA at 220 V. Test wrist strap continuity daily — a failed strap provides no protection against the 5-20 kV static charges that accumulate on personnel. Ionizer high-voltage needles (±5-10 kV) must never be touched during operation.

**Gowning ergonomic hazards**: Prolonged wear of full cleanroom garments (bunny suits, double gloves, face covers) in 22°C environments with 40-50% humidity causes heat stress during 8-12 hour shifts. Monitor for signs of dehydration and heat exhaustion. Provide scheduled breaks in cooler areas.

**Photoionization detector hazards**: PID lamps used for chemical spill monitoring emit UV radiation at 10.6 eV. Never look directly at the lamp window when activated. The PID lamp contains proprietary gases under pressure — handle carefully to avoid breakage.

### See Also

- [HEPA/ULPA Filtration](hepa-ulpa-filtration.md) — filter technology that enables contamination control
- [Facility Design & HVAC](facility-design.md) — physical infrastructure for clean room operation
- [Photolithography Cleanrooms](../photolithography/cleanrooms.md) — semiconductor-specific contamination protocols
- [Health: Sanitation](../health/sanitation.md) — contamination control at a different scale (biological, not particulate)

---

*Part of the [Bootciv Tech Tree](../index.md) • [Clean Room Technology](./index.md) • [All Domains](../index.md)*
