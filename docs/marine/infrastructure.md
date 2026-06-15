# Maritime Infrastructure & Underwater Engineering

> **Node ID**: marine.infrastructure
> **Domain**: [Marine & Naval Engineering](./index.md)
> **Dependencies**: `machine-tools`, [`metals.iron-steel`](../metals/iron-steel.md),
> [`polymers.rubber.gutta-percha`](../polymers/gutta-percha.md)
> **Enables**: None
> **Timeline**: Years 5-50+
> **Outputs**: harbor works, dry docks, submarine cables, lighthouses, corrosion protection
> **Critical**: No — specialized maritime capability, not required for land-based civilization

## Prerequisites

Maritime infrastructure requires significant industrial capability for construction materials and precision engineering:

- [Machine tools](../machine-tools/index.md) — precision manufacturing for pumps, caissons, and cable-laying equipment
- [Iron and steel production](../metals/iron-steel.md) — structural steel for dry docks, piers, and cable armoring
- [Gutta-percha](../polymers/gutta-percha.md) — natural polymer for submarine cable insulation
- [Cement and concrete](../chemistry/cement.md) — concrete for harbor and dock construction

Maritime infrastructure enables vessels to operate safely: harbors for shelter, docks for construction and repair, lighthouses for navigation, and underwater cables for communication. This capability also covers corrosion prevention — the perpetual battle against seawater's destruction of metal structures.

For basic harbor and port facility descriptions, see [Water Transport](../transport/shipping.md).

## Harbor Design

**Site selection criteria**. A good harbor site offers natural protection from prevailing wind and waves (headlands, islands, bays), adequate water depth at the entrance (minimum 1.5× the deepest draft vessel expected), sufficient area inside for vessel maneuvering and anchorage, a firm seabed for breakwater and quay foundations (rock or dense sand preferred; soft clay requires extensive foundations), and land access for transport connections (roads, railways).

**Breakwater construction**:

**Rubble mound breakwater** (most common):
- Core: quarry-run stone (50-500 kg pieces), placed by barge or crane
- Filter layer: intermediate stone (0.5-5 tonnes) prevents core material washing out through gaps in the armor
- Armor layer: the largest stones (5-50 tonnes each) on the seaward face, positioned by crane. Two layers thick. Interlocking placement (each stone contacts 3-4 neighbors) resists wave displacement.
- Crest elevation: 2-5 m above the highest expected storm wave height
- Base width: 3-5× the height. A 10 m high breakwater has a 30-50 m base.
- Wave attenuation: reduces wave height inside the harbor by 50-80%
- Material quantity: 10,000-500,000 tonnes of stone depending on length and depth
- Typical length: 200-1,000 m for a small-to-medium harbor

**Trade-offs**. The rubble mound breakwater is the simplest and most proven design, used since antiquity. It requires no precision fitting — quarry stone placed by barge or crane settles into place on uneven seabeds without strict foundation preparation. Its porous structure dissipates wave energy rather than reflecting it, reducing scour at the base. Damaged armor stones are replaced individually without draining or heavy lift equipment. The technology threshold is the lowest of any breakwater type: only quarry stone, cranes, and barges are needed, with no concrete or reinforcement. The penalties are material volume and footprint. A single breakwater consumes 10,000-500,000 tonnes of stone, requiring a nearby quarry — long-distance transport makes the design uneconomic. The structure settles over time as core material shifts under wave action, requiring periodic topping up. The wide base footprint (3-5× the height, so a 10 m breakwater occupies 30-50 m of seabed width) and the fact that material volume scales with depth cubed make rubble mounds impractical beyond ~20 m water depth.

**Vertical wall (caisson) breakwater**:
- Reinforced concrete caissons (hollow boxes, 15-25 m wide × 15-30 m tall × 30-60 m long) prefabricated in a dry dock
- Floated into position, sunk onto a prepared seabed foundation
- Filled with sand or concrete for mass
- Resists waves by mass and vertical face (reflects wave energy)
- Requires deep water and heavy lift capacity for caisson placement

**Trade-offs**. The vertical wall (caisson) breakwater is the deep-water answer where rubble mounds become impractical. Its narrow footprint uses far less seabed area than a rubble mound of equivalent height, and caissons built 15-30 m tall handle water depths that rule out stone structures. Installation is fast once the caissons are fabricated — float, sink, fill in days per unit — and the vertical wall reflects wave energy effectively to create calm water inside the harbor. It can even serve as a berth face, providing a docking surface for vessels, and caissons are placed on the prepared foundation with controlled tolerances. The requirements and risks are more demanding. Caisson fabrication requires reinforced concrete and a dry dock, a higher technology threshold than quarry stone. Each caisson weighs 1,000-5,000 tonnes, requiring heavy lift capacity for placement. The reflected wave energy can cause problems at the harbor entrance (standing waves, cross-sea). The foundation must be precisely leveled before placement — caissons are intolerant of uneven seabeds. The higher unit cost per meter reflects the concrete and reinforcement expense. And reflected wave energy scours the seabed at the base, potentially undermining the structure unless scour protection is installed.

**Harbor entrance**:
- Width: 1.5-3× the beam of the largest vessel expected. Minimum 30 m for small craft harbor, 100-200 m for commercial ports.
- Orientation: avoid prevailing wind and wave direction. Entrance on the lee side of the breakwater.
- Navigation channel: marked with buoys and leading lights. Minimum depth 1.15× the deepest draft vessel (allows for squat at speed).

## Dock and Quay Construction

**Quay wall types**:

**Gravity wall (mass concrete or masonry)**:
- Relies on self-weight to resist soil and water pressure
- Base width: 0.4-0.6× the wall height
- Height: 8-15 m from foundation to quay deck level
- Construction: concrete poured in situ or precast concrete blocks
- Foundation: mass concrete on firm seabed, or piled foundation on soft ground
- Quay deck: reinforced concrete slab, 0.5-1.0 m thick, designed for 20-40 kPa live load (forklifts, containers, cargo)

**Sheet pile wall**:
- Interlocking steel or timber sheets driven into the seabed
- Anchored by tie rods connected to deadman (buried concrete block) or ground anchors
- Suited for moderate heights (5-12 m) and firm soils
- Steel sheet piles: Z-profile or U-profile, 6-20 mm web thickness, 300-500 mm width per sheet
- Driving: vibratory hammer or impact hammer (steam, diesel, or hydraulic)

**Dolphin (mooring point)**:
- Isolated pile cluster or solid structure for vessel mooring
- Breasting dolphin: absorbs the berthing impact (typically 500-2,000 kN for a 10,000 tonne vessel at 0.2 m/s approach speed)
- Mooring dolphin: provides secure mooring point for lines
- Construction: timber piles (300-500 mm diameter) or steel pipe piles (600-1,200 mm diameter), driven in groups of 3-8 piles, connected by a cap

## Dry Dock Facilities

**Graving dock (dry dock)**:
- Excavated chamber with watertight gate at the entrance
- Vessel enters at high tide. Gate closes. Pumps remove water.
- Vessel settles on keel blocks (timber or concrete, 1.0-1.5 m high) and bilge blocks (angled supports)
- Side shores (timber props at 30-45°) stabilize the vessel upright
- Dimensions: 150-400 m long, 25-60 m wide, 8-15 m depth below sill (the entrance threshold)
- Pumping capacity: 5,000-50,000 m³/hour. Emptying time 2-6 hours.
- Gate types: floating caisson gate (concrete or steel box, floats into position, sinks when flooded) or miter gate (hinged doors, like canal lock gates)
- Floor construction: reinforced concrete slab, 1.0-3.0 m thick, on a waterproof membrane. Floor must resist hydrostatic uplift pressure when the dock is empty.

**Trade-offs**. The graving dock handles the largest vessels — ships up to 400 m length and 100,000+ tonnes — on a permanent, stable working platform where the vessel sits on fixed keel blocks with no motion during repair. Workers have full access to the hull, walking under and around the vessel on the dock floor, and cranes on the dock walls handle large components. Concrete graving docks last 50-100+ years with maintenance. The costs are capital and time. A large commercial graving dock costs $50-200 million and takes 12-36 months to construct, requiring deep excavation and dewatering. The fixed location cannot be moved or redeployed. The dock entrance must be dredged periodically to maintain sill depth against siltation. And the empty dock floor must resist hydrostatic uplift pressure, requiring a massive concrete slab 1.0-3.0 m thick on a waterproof membrane.

**Floating dry dock**:
- U-shaped steel or timber pontoon with wing walls
- Operates by flooding ballast tanks to sink below the vessel's keel. Vessel is positioned over the dock. Pumps empty ballast tanks, dock rises, lifting the vessel.
- Lift capacity: 1,000-100,000 tonnes
- Advantages: mobile (can be towed to where needed), no permanent excavation required
- Construction: steel plate on frames (similar to ship hull construction), divided into multiple watertight compartments for stability during lifting

**Trade-offs**. The floating dry dock is mobile — it can be towed to any location to respond to emergencies or shifting demand, with minimal shore-side construction (just a mooring point) and faster deployment than a graving dock (fabricated in a shipyard, towed to site, operational in weeks). Smaller floating docks (1,000-5,000 tonnes) are affordable for small repair yards, and the dock can be beached or moored in sheltered water. The trade-offs are structural and operational. The steel pontoon flexes under asymmetric vessel loading, restricting maximum vessel weight. Vessel and dock move with waves and swell, making precision work difficult in exposed locations. The steel hull requires periodic dry-docking itself for painting and repair. Multiple independent ballast compartments must be carefully managed during lifting. And the service life is shorter than a graving dock — 25-40 years versus 50-100+.

**Patent slip (marine railway)**:
- Inclined track (1:8 to 1:12 slope) running from above the high water mark into deep water
- A wheeled cradle rides the track, hauled by wire rope and winch
- Vessel is floated onto the submerged cradle, then winched up the slope
- Capacity: 100-5,000 tonnes
- Simpler and cheaper than a graving dock. Suitable for smaller vessels and repair yards.

**Trade-offs**. The patent slip (marine railway) is the lowest-cost dry-docking option — a simple track, cradle, and winch system on an inclined foundation (1:8 to 1:12 slope), with no excavation or watertight gates. It hauls vessels out of the water in 30-60 minutes and suits smaller vessels (100-5,000 tonnes) like fishing fleets, tugs, and coastal craft. The track can be extended to accommodate larger vessels incrementally. The limitations are capacity and access. Maximum capacity is 5,000 tonnes, constrained by wire rope and winch strength. The cradle blocks hull access below the keel line, so the vessel is accessible from only one side. The vessel sits on an inclined cradle rather than level, making some tasks awkward. Submerged rail sections corrode and require periodic inspection. And hauling operations halt in heavy seas when vessel motion prevents safe cradle alignment.

## Lighthouse Engineering

**Structural design**:
- **Stone tower**: granite or limestone blocks, tapered (1:10 to 1:15 batter ratio — base diameter is 10-15% wider than top). Wall thickness decreases with height. Height 20-60 m. Base diameter 5-15 m. Withstands hurricane-force winds and wave impact at the base.
- **Cast iron tower**: prefabricated cast iron plates bolted together on a stone foundation. Lighter than stone, easier to erect on remote sites. Height 15-40 m. Requires foundry capacity.
- **Reinforced concrete tower** (later): monolithic concrete with steel reinforcement. Tapered cylindrical or octagonal shape.

**Optical system**:
- **Light source**: oil lamp (whale oil until 1850s, then kerosene), then incandescent electric bulb (1900s+). Typical output: 100-1,000 candela (oil), 10,000-1,000,000 candela (electric with lens)
- **Lens**: Fresnel lens (invented 1822) — concentric annular sections that focus light into narrow horizontal beams. First-order Fresnel lens: 1.8 m tall, 1.2 m diameter. Rotating lens assembly produces characteristic flash pattern (e.g., one flash every 5 seconds).
- **Rotation mechanism**: clockwork driven by descending weights (like a grandfather clock). Weights descend through the center of the tower. Wound by the keeper every 4-8 hours.
- **Range**: visibility determined by height and atmospheric conditions. Geographic range = 2.08 × √height_meters nautical miles. Luminous range depends on light intensity and visibility.

**Subsidiary structures**:
- Keepers' quarters: living space for 1-3 keepers (before automation)
- Fuel store: oil or kerosene storage in a fire-resistant building separate from the tower
- Fog signal: bell, horn, or siren for fog conditions. Compressed air horn: audible 3-5 nautical miles. Requires an air compressor and reservoir.

## Submarine Cable Engineering

**Telegraph cable design**:
- **Conductor**: copper wire, 7-strand (one center wire surrounded by six). Diameter 1.5-3.0 mm. Conductivity: >95% IACS (International Annealed Copper Standard). Carries pulsed DC current (Morse code).
- **Insulation**: gutta-percha (natural polymer from Palaquium gutta tree). Properties: thermoplastic (softens at 60-70°C), excellent electrical insulation (dielectric strength 20-30 kV/mm), impermeable to water, remains flexible at seabed temperatures (2-10°C). Applied in 3-4 layers over the conductor, total thickness 3-8 mm.
- **Armor protection**: iron or steel wire strands (10-18 wires, 1.5-3.0 mm diameter) wound helically around the insulated core. Provides tensile strength for laying and protection against damage. Deeper water cables use lighter armor; shallow water cables use heavier armor (fishing damage risk).
- **Serving**: hemp or jute yarn wrapped between insulation and armor to prevent chafing
- **Outer serving**: tarred hemp or polyethylene sheath over the armor for corrosion protection

**Cable specifications (typical 19th-century telegraph cable)**:
- Overall diameter: 15-30 mm
- Weight in air: 2-8 tonnes/km
- Weight in seawater: 0.5-3.0 tonnes/km (positive = sinks)
- Breaking strength: 50-200 kN (5-20 tonnes)
- Electrical resistance: 5-15 Ω/km (conductor)
- Insulation resistance: >1,000 MΩ•km
- Maximum laying depth: 5,000-8,000 m (deepest oceans)

**Cable laying process**:
1. Manufacture cable on shore in long lengths (100-2,000 nm per section)
2. Load onto cable ship: coiled in large tanks (3-5 m diameter turns). Cable must not be bent sharper than its minimum bending radius (typically 50× the cable diameter).
3. Pay out from the ship over the stern through a paying-out machine (tension-controlled drum brake)
4. Cable speed must exceed ship speed by 2-5% to allow for catenary sag and prevent tension spikes
5. Cable sinks to the seabed under its own weight. A 5,000 m depth cable takes 15-30 minutes to reach the bottom.
6. Tension monitoring: strain gauges on the paying-out gear. Tension should remain 10-30% of breaking strength during normal laying.

**Cable joining (splicing)**:
- When two cable sections must be joined at sea, a splice is made
- Strip back armor and serving on both ends. Expose the gutta-percha insulation.
- Solder or crimp the copper conductors together.
- Melt gutta-percha over the joint in 3-4 overlapping layers, each heated and pressed to form a seamless seal. A poorly insulated joint allows seawater ingress, which shorts the conductor to ground and renders the cable useless.
- Re-apply armor wires by splicing individual strands with wire wrappings
- Splice increases cable diameter locally (joint box: 30-50 cm long, 2-3× normal diameter). Must still pass over the ship's sheaves.

**Cable faults and repair**:
- Faults: insulation failure (seawater ingress), conductor break (tension), or external damage (fishing trawls, anchors, submarine landslides)
- Locate fault: measure electrical resistance from shore station. A short circuit at distance d has resistance R = ρd/A, giving d = RA/ρ.
- Grapnel: a hooked iron bar towed across the seabed to catch and lift the cable
- Lift cable to surface, cut, bring both ends aboard the repair ship, insert a new section (repair length), splice both ends, lower back to the seabed

## Corrosion Prevention

Seawater (3.5% NaCl, pH 8.0-8.3) is one of the most corrosive natural environments for metals. Steel corrosion rate in seawater: 0.1-0.3 mm/year without protection. A 10 mm steel hull plate loses 1-3 mm per decade.

**Corrosion mechanisms**. Seawater attacks steel through four distinct mechanisms. Uniform corrosion causes even material loss across the surface at 0.1-0.3 mm/year on bare steel. Pitting corrosion creates localized deep pits (0.5-3.0 mm deep, 1-5 mm diameter) that perforate thin plate, driven by chlorides and accelerated by stagnant water and crevices. Galvanic corrosion occurs when two dissimilar metals are electrically connected in seawater — the more active (anodic) metal corrodes preferentially, so steel in contact with copper corrodes 5-10× faster than isolated steel. Stress corrosion cracking results from the combination of tensile stress and corrosive environment, causing sudden brittle fracture in high-strength steels and stainless steels.

**Anti-fouling coatings**:
- Marine organisms (barnacles, tubeworms, algae) colonize hull surfaces within weeks. A fouled hull has 20-40% more drag than a clean hull.
- Traditional: copper sheathing (0.5-1.0 mm sheets nailed below waterline). Copper ions are toxic to marine organisms. Effective for 2-5 years before replacement needed.
- Anti-fouling paint: copper oxide or tributyltin oxide (TBT, now banned by IMO) in a paint matrix. Leaches biocide at controlled rate. Effective for 1-3 years. Must be reapplied during dry-docking.
- Modern: silicone-based fouling-release coatings (non-toxic, low surface energy prevents organism adhesion). Effective but expensive.

**Cathodic protection**:

**Sacrificial anode system**:
- Attach blocks of a more active metal (zinc, aluminum, or magnesium alloy) directly to the steel structure
- The anode corrodes preferentially, protecting the steel (cathode)
- Zinc anode consumption rate: 10-12 kg per ampere-year. Typical hull anode: 10-30 kg, lasting 1-3 years.
- Current density required: 10-30 mA/m² for painted steel in seawater, 50-100 mA/m² for bare steel.
- A 5,000 m² wetted hull area at 20 mA/m² needs 100 amperes continuous protection. Annual zinc consumption: 100 A × 11 kg/A•yr = 1,100 kg.

**Trade-offs**. The sacrificial anode system requires no external power — the galvanic potential difference between anode and hull drives the protective current. Installation is as simple as welding or bolting anodes directly to the hull, with no wiring or electronics. The system is fail-safe: if the coating fails, anode current increases automatically to compensate. It is the lowest-cost option for small installations (zinc anodes at $5-15 per kg), requires no maintenance during service life (anodes are inspected and replaced during dry-docking), and works on any size vessel from small boats (single 5 kg anode) to large ships (hundreds of anodes). The limitations are driving voltage and consumption. Zinc provides only ~0.25 V potential difference, insufficient for large bare steel areas. Anodes are consumed at 10-12 kg per ampere-year and must be replaced every 1-3 years during dry-docking. Protruding anode blocks add 1-3% to hull drag. A large vessel needs 500-2,000 kg of zinc anodes, adding weight to the hull. And the current output depends on anode area and water resistivity, so it cannot be tuned to changing conditions.

**Impressed current system (ICCP)**:
- External DC power source (rectifier, 10-50 V, 10-200 A) drives current through inert anodes (platinum-coated titanium or mixed metal oxide) to the hull
- Reference electrode (silver/silver chloride) monitors hull potential. Control circuit maintains protection potential: -0.80 to -0.95 V vs. Ag/AgCl
- Advantages: longer life, adjustable output, fewer anodes needed
- Requires reliable electrical power supply

**Trade-offs**. The impressed current system (ICCP) provides higher driving voltage — an adjustable 10-50 V output that delivers adequate current for large bare steel areas. Only 5-20 inert anodes are needed to replace hundreds of sacrificial anodes, and the inert anodes (Pt/Ti, MMO) last 10-20+ years versus 1-3 years for zinc. A reference electrode provides automatic potential control, maintaining the optimal protection voltage, and the system compensates for coating degradation, water resistivity changes, and vessel operating conditions. Inert anodes do not dissolve, so no metal ions enter the marine environment. The complications are power dependency and complexity. The system requires continuous electrical power — a power failure leaves the hull unprotected. The initial cost is higher (rectifier, reference electrodes, inert anodes, and control electronics). Excessive voltage risks damaging paint coatings (cathodic disbondment) or causing hydrogen embrittlement in high-strength steel. The wiring, junction boxes, and electronics require skilled technicians. And the reference electrode calibration drifts, requiring periodic verification against a known standard.

**Protective coatings**:
- **Primer**: zinc-rich epoxy (80-90% zinc dust in epoxy binder). Provides both barrier protection and cathodic protection at scratches.
- **Intermediate coat**: epoxy or polyurethane, 150-300 μm thick. Barrier to water and oxygen penetration.
- **Topcoat**: polyurethane for UV resistance and color, 50-100 μm.
- Total dry film thickness: 300-500 μm for submerged service, 200-300 μm for atmospheric exposure.
- Surface preparation: abrasive blasting to Sa 2.5 (near-white metal, ISO 8501-1). All rust, mill scale, and old paint removed. Surface profile 50-100 μm for coating adhesion.

## Underwater Construction

**Caisson (cofferdam) construction**:
- For building harbor walls, bridge piers, or other structures below the waterline
- Open-bottom steel or timber caisson sunk onto the prepared seabed
- Compressed air injected to keep water out (pneumatic caisson). Workers enter through an airlock.
- Maximum working depth: 30-35 m (air pressure 3.0-3.5 atm). Beyond this, nitrogen narcosis and decompression sickness make work impossible without saturation diving techniques.
- Decompression: workers must decompress in stages. A 30-minute exposure at 3 atm requires 15-20 minutes of decompression. Failure to decompress causes decompression sickness ("the bends") — nitrogen bubbles form in blood and tissues, causing pain, paralysis, or death.

**Concrete underwater**:
- Tremie concrete: concrete placed through a vertical pipe (tremie, 200-300 mm diameter) with the lower end kept embedded in the fresh concrete. Prevents washout of cement by water.
- Mix design: high cement content (350-450 kg/m³), low water/cement ratio (0.40-0.45), 10-20 mm aggregate. Slump: 150-200 mm (very workable for placement through tremie).
- Anti-washout admixtures (cellulose ethers) increase cohesiveness of concrete in water.

## Safety & Hazards

- **Drowning**: The primary hazard of all marine construction. Life jackets mandatory for all personnel working within 2 m of water edge or on floating plant. Safety boats standing by during in-water work.
- **Compressed air work**: Caisson disease (decompression sickness) affects workers in pneumatic caissons. Strict decompression schedules mandatory. Medical lock on site for emergency recompression.
- **Underwater explosion**: Blasting for rock excavation underwater generates shock waves that are lethal to divers at close range. Clear all divers from the water before detonation. Minimum safe distance: 300-500 m for 10 kg charge.
- **Cable laying tensions**: Cable under tension stores enormous energy. A cable parting under load whips violently. Personnel must stand clear of the cable path during laying operations. Steel blast shields around the paying-out gear.
- **Chemical exposure**: Anti-fouling paints, solvents, and epoxy coatings contain toxic compounds (copper compounds, isocyanates). Respiratory protection and skin protection mandatory during application.

## Infrastructure Specifications Summary

| Structure | Key Dimension | Material | Quantity | Construction Time |
|-----------|--------------|----------|----------|------------------|
| Breakwater | 200-500 m length | Quarry stone | 10,000-50,000 tonnes | 6-24 months |
| Stone quay | 100-300 m length | Granite/concrete | 5,000-30,000 m³ | 6-18 months |
| Graving dock | 150-400 m × 25-60 m | Reinforced concrete | 30,000-200,000 m³ | 12-36 months |
| Lighthouse | 20-60 m height | Stone/cast iron/concrete | 500-5,000 tonnes | 6-24 months |
| Submarine cable | 100-5,000 km | Copper, gutta-percha, steel | 200-40,000 tonnes | 1-12 months (laying) |

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Rubble mound breakwater armor stones displaced after storm | Individual stones too light for wave climate or insufficient interlocking | Use armor stones 5-50 tonnes on seaward face; ensure each stone contacts 3-4 neighbors in interlocking placement; crest elevation must be 2-5 m above highest expected storm wave height |
| Caisson breakwater foundation scour undermines structure | Reflected wave energy scours seabed at the base | Install scour protection (riprap or concrete mattress) around the caisson base; consider rubble mound toe protection to dissipate reflected wave energy before it reaches the foundation |
| Graving dock floor cracks from hydrostatic uplift | Floor slab insufficient thickness for upward water pressure when dock is empty | Design floor as reinforced concrete slab 1.0-3.0 m thick with waterproof membrane; floor must resist full hydrostatic pressure when dock is pumped dry; add tension piles if uplift exceeds slab dead weight |
| Submarine cable insulation fails within months of laying | Gutta-percha joint poorly sealed during splice, allowing seawater ingress | Apply gutta-percha in 3-4 overlapping heated and pressed layers at every splice; test insulation resistance (>1,000 MΩ·km) before and after laying; a single compromised joint shorts the entire cable |
| Sacrificial zinc anodes consumed faster than expected (under 1 year) | Hull coating damaged exposing large bare steel area, increasing current demand | Repair coating to reduce current demand (target 10-30 mA/m² for painted steel); anode consumption is 10-12 kg per ampere-year — a 5,000 m² hull at 20 mA/m² needs 1,100 kg zinc annually |
| ICCP system overprotects hull (voltage below −0.95 V vs Ag/AgCl) | Rectifier output too high, causing cathodic disbondment of paint | Adjust rectifier to maintain −0.80 to −0.95 V vs Ag/AgCl; excessive voltage causes paint blistering (cathodic disbondment) and hydrogen embrittlement in high-strength steel |
| Floating dry dock lists during vessel lifting | Ballast tank pumping sequence incorrect — asymmetric water removal | Pump ballast tanks in synchronized pairs (port/starboard); monitor list angle continuously; use multiple independent compartments to maintain level during the critical lift phase |
| Tremie concrete washes out underwater | Pipe tip not kept embedded in fresh concrete, allowing water to mix | Keep the lower end of the tremie pipe embedded at least 1.5 m in previously placed concrete at all times; use high cement content (350-450 kg/m³) and anti-washout admixtures |
| Lighthouse Fresnel lens rotation stops | Clockwork weight chain jammed or drive mechanism corroded | Inspect and lubricate clockwork monthly; ensure weight channel through the tower is clear of debris; wind weights every 4-8 hours as specified — missed winding stops rotation |
| Pneumatic caisson workers develop decompression sickness | Inadequate decompression time after working at 3.0-3.5 atm | Follow strict decompression tables: 15-20 minutes decompression for 30 minutes at 3 atm; maintain medical lock on site for emergency recompression; never exceed 30-35 m working depth |

## See Also

- [Water Transport](../transport/shipping.md) — basic harbor facilities, port operations
- [Metals: Iron & Steel](../metals/iron-steel.md) — materials for construction
- [Machine Tools](../machine-tools/index.md) — precision manufacturing for marine components
- [Polymers: Gutta-Percha](../polymers/index.md) — gutta-percha production and properties for cable insulation
- [Cement & Concrete](../chemistry/cement.md) — concrete for harbor and dock construction
- [Hull Construction](shipbuilding.md) — shipbuilding for cable ships and construction vessels

---
*Part of the [Bootciv Tech Tree](../index.md) • [Marine & Naval Engineering](./index.md) • [All Domains](../index.md)*

