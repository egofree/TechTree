# Cleanrooms

> **Node ID**: photolithography.cleanrooms
> **Domain**: [Photolithography & IC Fabrication](./)
> **Dependencies**: `machine-tools`, `chemistry`
> **Timeline**: Years 40-70
> **Outputs**: cleanrooms, ultra_pure_water, cleanroom_consumables

### Cleanrooms
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

### Operational Protocols
- **Gowning sequence** (order matters — cover dirtiest areas first):
  1. Hair cover (bouffant cap — covers all hair, no exposed scalp)
  2. Shoe covers (over-shoe booties — seal around ankle)
  3. Face mask (covers nose and mouth — source of breath droplets)
  4. Gloves (nitrile, powder-free — don before bunny suit to keep inner gloves clean)
  5. Bunny suit (coverall with integrated hood — sealed seams, snap or velcro closures, no pockets or exposed buttons)
  6. Second pair of gloves (over bunny suit cuffs — double-gloving prevents skin exposure)
  7. Boot covers (over bunny suit legs — sealed to suit at knee)
- **Airlock entry procedure**: Personnel airlock with interlocked doors (one must close before the other opens). Air shower (high-velocity filtered air jets from multiple nozzles, 15-30 seconds) dislodges particles from garments. Material airlock (pass-through) for tools, wafers, chemicals — items wiped with IPA-dampened wipes before entry. No cardboard, paper, or wood in cleanroom (uses cleanroom-rated polypropylene or polycarbonate alternatives).
- **Behavioral rules**: No rapid movements (creates turbulence and particle shedding). No cosmetics, perfumes, or hair products. No writing with pencils (graphite particles) — use cleanroom-rated pens. Touch wafer only with wafer wands or vacuum wands, never gloved hands directly.

### Vibration & ESD Control
- **Vibration isolation**: Precision photolithography tools (steppers, mask aligners) require vibration <0.1 μm displacement. Vibration isolation pads (neoprene rubber or air-spring mounts) under tool bases. Massive concrete inertia blocks (2-5 tonnes) decouple tools from floor vibrations. Facility sited away from heavy machinery, rail lines, and road traffic if possible.
- **ESD (electrostatic discharge) control**: MOS devices are destroyed by static discharges as low as 50-100 V. Human body model (HBM) discharge: 100 pF through 1.5 kΩ — a person walking on a synthetic floor can accumulate 5-20 kV. Countermeasures:
  - Anti-static flooring (conductive vinyl or epoxy, resistance 10⁶-10⁹ Ω/sq, grounded through 1 MΩ resistor for safety)
  - Grounded wrist straps (1 MΩ current-limiting resistor to ground — worn at all times when handling wafers or devices)
  - Ionizers (fan-driven or corona-discharge type) neutralize static on insulators that cannot be grounded (wafer surfaces, plastic wafer carriers)
  - Humidity control at 40-50% RH (lower humidity increases static buildup — below 30% RH is dangerous)

### HEPA Filter Bootstrapping
- **Filter media**: Borosilicate glass microfibers (fiber diameter 0.5-4 μm), formed into a pleated paper-like mat. Pleating increases surface area 20-50× versus flat media, reducing pressure drop. Media binder: acrylic resin (holds fiber matrix together).
- **Filter efficiency**: 99.97% capture at 0.3 μm (the most penetrating particle size — MPPS). Larger particles are intercepted directly; smaller particles are captured by diffusion. HEPA grade is defined by this single-point efficiency.
- **Filter frame construction**: Rigid frame of aluminum or galvanized steel (wood frames warp). Gasket seal (neoprene or closed-cell foam) between filter and ceiling grid — any bypass leak defeats the entire filter. Gel sealant (non-drying silicone or urethane) for critical installations. Filter life: 3-7 years depending on particulate loading; pressure drop monitoring indicates replacement time.
- **Fan/filter unit (FFU) design**: Integrated module — centrifugal fan motor + HEPA filter + pre-filter in a single ceiling tile-sized panel (2×2 ft or 2×4 ft standard). Speed control (adjustable fan RPM for desired air velocity, typically 0.3-0.5 m/s). Modular installation: mount in cleanroom ceiling grid, wire to power, adjust speed. Enables incremental cleanroom expansion.

### Cleanroom Garments
- **Materials**: Tyvek (spun-bonded polyethylene — disposable, inexpensive, good particle containment but low durability), or polyester (woven, reusable, excellent particle containment, durable for 50+ wash cycles). Polyester preferred for production cleanrooms.
- **Construction**: Sealed or bound seams (no raw edges that shed fibers). No pockets, zippers, or buttons (particle sources). Garments are continuous-filament woven fabric — no staple fibers to shed. Coverall design with integrated hood or separate hood with face opening. Snap closures or velcro (no hooks that catch particles).
- **Laundry**: Specialized cleanroom laundry — ultra-pure water wash, non-ionic detergent, drying in HEPA-filtered environment. Garments tested for particle shedding after each wash (Helmke drum test or body box test). Typically replaced after 30-50 wash cycles when particle shedding exceeds specification.

### Hazards & Safety

- **Chemical handling**: Acetone, IPA, and MEK solvents are highly flammable (flash points well below room temperature). Use only in ventilated solvent benches with spark-free equipment. Store in flammable-materials cabinets; keep fire extinguishers (CO₂ or dry chemical) within 10 m of solvent stations.
- **UV exposure**: Mercury arc lamps and UV curing tools emit i-line (365 nm) and shorter wavelengths that cause corneal burns and skin erythema. Enclose beam paths; wear UV-blocking safety glasses (OD 5+ at 365 nm) when aligning or servicing lithography tools. Never look directly at an energized lamp.
- **ESD damage to devices**: Static discharges as low as 50 V destroy MOS gate oxides. Wear grounded wrist straps (1 MΩ current-limiting resistor) at all times when handling wafers or packaged devices. Maintain humidity at 40-50 % RH; use ionizers on non-groundable surfaces. Test wrist-strap continuity daily.
- **Ergonomic hazards**: Cleanroom bunny suits cause heat stress (limited ventilation, full-body coverage). Limit continuous gowning sessions to 2 hours with cooling breaks. Airlock entry/exit protocols add physical strain — rotate personnel to reduce repetitive-motion injury from gowning and wafer handling.
- **Piranha solution** (if used for cleaning): See [Resists & Masks](resists-masks.md) for piranha hazards.

---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
