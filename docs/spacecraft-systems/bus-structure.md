# Bus Structure + Deployables

> **Node ID**: spacecraft-systems.bus-structure
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: `metals.aluminum`, `polymers.composites`, `machine-tools`, `vacuum`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 40-200+
> **Outputs**: satellite_structures, deployable_arrays
> **Critical**: Yes

The spacecraft bus structure is the skeleton that carries every subsystem through launch loads and then supports them in orbit. It must survive acoustic vibration, steady acceleration, shock transients from separation events, and pyrotechnic pyroshock — then deploy antennas, solar arrays, booms, and radiators with millimetre-level precision in vacuum. No other structure in the tech tree combines such high load-to-mass ratios with such stringent deployment reliability.

This article covers the integrated design of spacecraft bus structures across three process areas: [primary structure fabrication](./bus-structure.primary-structure.md) (honeycomb panels, isogrid machining, mass budgets), [deployable structures](./bus-structure.deployable-structures.md) (solar array panels, CoilABLE booms, STEM deployers), and [mechanisms](./bus-structure.mechanisms.md) (Frangibolts, HDRMs, pyrotechnic release, hinge actuators). Each is a discipline in its own right; together they define the satellite's mechanical identity.

## Overview

A spacecraft primary structure typically accounts for 15-25% of the dry bus mass. Unlike an aircraft fuselage, which is optimised for repeated load cycles over decades, the primary structure sees its worst load once — during the eight-to-ten minutes of ascent — and then operates at near-zero load for the rest of its orbital life. This single-flight-dominated design philosophy drives the use of sandwich panels, isogrid plates, and thin-walled shells that would be unacceptable in any reusable vehicle.

The [aluminium](../metals/aluminum.md) industry provides the manufacturing heritage for spacecraft structures. Aluminium 6061-T6, 7075-T73, and the newer aluminium-lithium 2195 alloy are the workhorse materials, machined on [machine tools](../machine-tools/index.md) capable of holding 0.05 mm tolerances over metre-scale parts. [Composite materials](../polymers/composites.md) — carbon-fibre-reinforced polymer (CFRP) facesheets and aluminium honeycomb cores — have progressively replaced solid metal panels where stiffness-to-mass ratio matters. [Vacuum](../vacuum/index.md) technology underpins both the deployment testing (thermal-vacuum chambers simulate the orbital environment) and the outgassing-free material selection requirements.

## Structural Materials Comparison

| Property | Al 6061-T6 | Al 7075-T6 | Al-Li 2195 | CFRP (M55J) |
|----------|-----------|-----------|-----------|-------------|
| Density (g/cm³) | 2.70 | 2.81 | 2.71 | 1.60 |
| Tensile strength (MPa) | 310 | 572 | 590 | 2100 |
| Elastic modulus (GPa) | 69 | 72 | 79 | 340 |
| CTE (×10⁻⁶/K) | 23.6 | 23.6 | 23.5 | ~0.5 (axial) |
| Thermal conductivity (W/m·K) | 167 | 130 | 105 | 50-300 (varies) |
| Max service temp (°C) | 180 | 150 | 175 | 150-400 (resin dependent) |
| Typical use | Panels, frames | Fittings, fasteners | Tanks, fairings | Panels, struts |

Aluminium 6061-T6 remains the default for non-critical panels because its weldability, corrosion resistance, and cost dominate the trade. Aluminium-lithium 2195 (developed for the Space Shuttle Super Lightweight Tank) offers 5% lower density and 30% higher stiffness than conventional 2219, but requires specialised welding. CFRP wins decisively on stiffness-to-weight for solar array substrates and precision optical benches, but its near-zero axial coefficient of thermal expansion (CTE) must be managed at interfaces with metal fittings where differential expansion drives shear loads.

## Honeycomb Sandwich Panels

The honeycomb sandwich panel is the dominant spacecraft structural element. It consists of two thin faceskins bonded to a thick, low-density core, producing a panel with high bending stiffness at minimal mass — the same principle as an I-beam, but extended to two dimensions.

### Geometry and Specifications

| Parameter | Typical value | Range |
|-----------|--------------|-------|
| Core material | Al 5052 (hexagonal) | Al, Nomex, Kevlar |
| Core thickness | 25 mm | 10-50 mm |
| Cell size | 4.8 mm (3/16") | 3.2-6.4 mm |
| Foil thickness | 0.025 mm | 0.018-0.075 mm |
| Faceskin material | Al 6061-T6 | Al, CFRP |
| Faceskin thickness | 0.30 mm | 0.15-1.0 mm |
| Adhesive | Film epoxy (FM300) | — |
| Panel areal density | 2.5 kg/m² | 1.5-8.0 kg/m² |

A 25-mm-core panel with 0.3 mm aluminium faceskins weighs approximately 2.5 kg/m² and achieves a bending stiffness equivalent to a 2 mm solid sheet at one-third the mass. Doubling the core thickness to 50 mm quadruples the bending stiffness (stiffness scales with core thickness squared) while adding only 15% mass from the additional core foil.

### Manufacturing Steps

1. Cut facesheets from coil stock; flatten and clean with solvent wipe
2. Machine core to final panel footprint; expand core to nominal cell geometry
3. Pot core insert sections at fastener locations using epoxy filler
4. Lay up adhesive film on inner faceskin; position core; add second faceskin
5. Vacuum bag the assembly; cure in autoclave at 120-180°C, 0.3-0.6 MPa for 90-120 min
6. Trim cured panel to final dimensions; machine edge close-outs
7. Non-destructive inspection: ultrasonic C-scan for bondline voids (reject >10 mm diameter)
8. Install inserts (potted or bonded); apply edge close-out channels

## Isogrid Structures

Isogrid construction machined from solid plate provides an alternative to sandwich panels where through-thickness loads, attachment points, or thermal conductivity requirements make honeycomb unsuitable. An isogrid plate has triangular ribbing machined into one face, leaving a thin skin with an integral stiffening pattern that approximates an isotropic plate — hence "iso-grid."

### Isogrid Dimensions

| Parameter | Typical value | Notes |
|-----------|--------------|-------|
| Rib height | 15-40 mm | Machined from 20-50 mm plate |
| Rib width | 3-5 mm | Thicker at nodes |
| Rib spacing | 70-100 mm | Equilateral triangle pattern |
| Skin thickness | 1.5-3.0 mm | Remaining after machining |
| Pocket radius | 3-5 mm | Reduces stress concentration |
| Material | Al 6061-T6 | Also Al-Li 2195, Ti-6Al-4V |

The machining of isogrid is material-intensive: a 1 m × 1 m isogrid plate machined from 40 mm plate removes 60-70% of the stock as chips. Five-axis CNC machining centres with high-speed spindles (20,000+ RPM) and flood coolant achieve surface finishes of 1.6 µm Ra on pocket floors while maintaining rib wall thickness to ±0.1 mm. The recovered chips are recycled through the [metal recycling](../metals/metal-recycling.md) stream.

## Deployable Solar Arrays

Modern spacecraft generate power from deployable solar arrays that fold or roll into a compact stowed volume for launch and then extend to areas of 20-100 m². The deployment mechanism must achieve reliable, single-shot extension in vacuum without ground intervention.

### Deployment Mechanism Types

| Mechanism | Stowed ratio | Power density | Flight heritage | Complexity |
|-----------|-------------|--------------|----------------|------------|
| Rigid panel (Z-fold) | 5:1 | 100-150 W/m² | High (1960s-present) | Low |
| Flexible blanket (Z-fold) | 10:1 | 100-200 W/m² | Moderate (1990s-present) | Medium |
| CoilABLE boom | 20:1 | 80-120 W/m² | High (1970s-present) | Medium |
| STEM (Storable Tubular) | 30:1 | N/A (boom) | High (1960s-present) | Medium |
| Telescopic | 8:1 | N/A (boom) | Moderate | High |
| Inflatable/rigidisable | 50:1 | 50-100 W/m² | Low (experimental) | High |

### CoilABLE Boom

The CoilABLE boom (originally developed by Astro Research, now Northrop Grumman) is a truss-section boom that flattens into a tape and coils onto a spool for stowage. When released, stored elastic strain energy causes the boom to self-deploy and re-constitute its triangular cross-section. Typical booms are 10-50 m long with 15-30 cm deployed diameter, stowing into a 30 cm × 60 cm canister.

Key design parameters:

- Longerons: 3 fibreglass or CFRP rods, 6-12 mm diameter
- Batten frames: aluminium or CFRP, triangular or square cross-section
- Diagonals: tensioned wires or thin CFRP strips
- Tip deployment velocity: 5-15 cm/s (controlled by governor motor)
- Deployed natural frequency: 0.1-0.5 Hz (first bending mode)

### STEM (Storable Tubular Extendible Member)

STEM booms are formed from thin metal tape (beryllium-copper or CFRP) that is flattened, rolled onto a drum, and then deploy by unrolling and re-rounding into a slit tube. They are simpler and more compact than CoilABLE designs but offer lower bending stiffness per unit mass. The original STEM design dates to 1960s Canadian Alouette satellites and remains in use for magnetometer booms and antenna supports.

## Release Mechanisms

Every deployable appendage is held in its stowed configuration during launch by a release mechanism that must survive random vibration, acoustic loads, and shock — then actuate on command with sub-millisecond response and minimal debris generation.

### Release Mechanism Comparison

| Device | Release shock | Resettable | Hold-off load | Power | Flight heritage |
|--------|-------------|-----------|--------------|-------|----------------|
| Frangibolt (SMA) | Very low (300g @ 12") | Yes | 5-45 kN | 20-90 W | High |
| HDRM (paraffin) | Very low (100g @ 12") | Yes | 5-25 kN | 10-30 W | Very high |
| Pyrotechnic (pyro) | High (3000g @ 12") | No | 10-200 kN | 1-5 ms pulse | Very high |
| Cutters (SMA/thermal) | Very low | No | 0.5-5 kN | 10-40 W | High |
| Electromagnetic | Low | Yes | 1-10 kN | 5-20 W | Moderate |

### Frangibolt

The Frangibolt uses a shape-memory alloy (SMA) collar that contracts when heated above its transformation temperature (~80°C), applying tension to a notched bolt until it fractures at a predetermined cross-section. The fracture releases the held component with minimal shock — typically 300g measured 12 inches from the release point, compared to 3000g for an equivalent pyrotechnic bolt cutter. The Frangibolt is resettable (the SMA can be cooled and the bolt reinstalled) and requires only 20-90 W of electrical heating power for 30-120 seconds.

### HDRM (Hold-Down Release Mechanism)

The paraffin-actuated HDRM uses a phase-change wax that expands when heated, driving a pin that shears a retaining ring. It is the lowest-shock release device available (under 100g at 12 inches) and has accumulated extensive flight heritage on communications satellites and interplanetary probes. Its limitation is hold-off load: paraffin actuators are practical up to 25 kN, above which pyrotechnic devices remain dominant.

### Pyrotechnic Release

Pyrotechnic release devices (explosive bolt cutters, separation nuts, guillotine cutters) generate the highest hold-off forces and the fastest actuation (sub-millisecond). They remain indispensable for launch vehicle separation and large-solar-array deployment. Their drawback is pyroshock — the high-frequency transient (100 Hz-100 kHz) that propagates through the structure at up to 10,000g near the source. Pyroshock-sensitive components (electronics, optics, gyros) must be located far from pyrotechnic devices or protected by shock-isolation mounts.

## Hinge and Deployment Actuator Design

Deployable panels articulate on hinge mechanisms that must provide precise alignment in the deployed state while remaining locked through launch. The most common design combines a hinge bearing (plain or rolling element) with an appropriation actuator that drives deployment.

### Hinge Types

1. **Plain bearing hinge**: PTFE-lined bushings on steel pins; simplest, lowest cost, highest friction
2. **Rolling element hinge**: Ball or roller bearings for low friction and precise alignment; heavier
3. **Flexure hinge**: Thin metal flexure (beryllium-copper or Inconel); no sliding contact, no wear, limited rotation angle
4. **Clevis pin**: Quick-release pin in a clevis bracket; used for ground handling and test

### Deployment Actuator Types

- **Spring-driven**: Torsion or extension springs; simple, reliable, uncontrolled deployment velocity
- **Motor-driven**: DC or stepper motor with gear train; controllable velocity and position feedback
- **SMA actuated**: Shape-memory wire contracts when heated; high force-to-weight, slow stroke
- **Damped spring**: Spring deployment with viscous damper for controlled velocity; most common for solar arrays

The damped spring deployment is the workhorse approach for rigid-panel solar arrays. A torsion spring at each hinge provides the deployment force; a fluid damper (silicone oil in a cylinder) limits deployment velocity to 10-30°/s, completing the deployment in 10-60 seconds. The damper prevents the "snap" that would otherwise shock the panels and risk fracturing solar cell coverslides.

## Mass Budget Example

A representative 500 kg dry-mass communications satellite bus allocates its primary structure mass as follows:

| Element | Mass (kg) | % of dry mass |
|---------|----------|---------------|
| Central thrust tube | 35 | 7.0% |
| Equipment panels (4) | 28 | 5.6% |
| Top and bottom panels | 12 | 2.4% |
| Solar array substrates | 8 | 1.6% |
| Solar array yoke & hinges | 4 | 0.8% |
| Fasteners, inserts, brackets | 10 | 2.0% |
| Release devices (8× HDRM) | 2 | 0.4% |
| **Total primary structure** | **99** | **19.8%** |

The central thrust tube carries the launch interface load to the separation ring and is the single most critical structural component. It is typically a 0.8-1.2 m diameter cylindrical or conical shell with aluminium honeycomb or CFRP faceskins over aluminium core, 1.0-1.5 m tall.

## Deployment Sequence

A typical rigid-panel solar array deployment proceeds through the following sequence after separation from the launch vehicle:

1. **T+0 s**: Separation confirmation; spacecraft attitude stabilised to within 5° of sun-pointing
2. **T+10 s**: Release command to 4× HDRMs holding solar array panels stowed against bus
3. **T+10.1 s**: HDRM actuation complete; panels held only by deployment hinges and release springs
4. **T+11 s**: Release springs push yoke outward; yoke rotates 90° to horizontal position
5. **T+13 s**: Panel deployment begins; torsion springs drive panels open, damper limits velocity
6. **T+25 s**: First panel pair latched; microswitch confirms latch engagement
7. **T+40 s**: Second panel pair latched; deployment complete
8. **T+45 s**: Solar array drive actuator rotates array to sun-tracking position
9. **T+60 s**: Power bus voltage rises as cells illuminate; battery charge begins

## Fastener Systems and Inserts

Spacecraft structures are assembled almost entirely with threaded fasteners and bonded inserts rather than welds or rivets. This is driven by the need for disassembly during integration and test, and by the risk of weld distortion on lightweight panels.

### Fastener Selection

| Fastener type | Material | Typical use | Notes |
|--------------|----------|------------|-------|
| Socket head cap screw | A-286, Inconel 718 | Primary structural joints | High strength, reusable |
| Hi-Lok pin | Ti-6Al-4V | Shear-critical joints | Pre-installed collar |
| Rivnut / Clinchnut | Al 5056 | Blind-side panel attachment | Installed from one side |
| Potted insert | Al 6061-T6 | Honeycomb panel attach | Bonded into core with epoxy |
| Locked insert | Al 6061-T6 | High-load panel attach | Expands against core walls |

Potted inserts are the defining feature of honeycomb panel assembly. A hole is drilled through both faceskins and the core, the core around the hole is cleared, and an insert is bonded in place with epoxy potting compound. The cured adhesive transfers fastener loads into the core shear webs, enabling a honeycomb panel to carry concentrated fastener loads that would otherwise punch through the thin faceskin.

### Insert Installation Procedure

1. Drill through-hole at insert location (typical 8 mm for 1/4"-28 insert)
2. Ream hole to ±0.1 mm tolerance
3. Remove core material within insert cavity using core plug cutter
4. Clean cavity with solvent (isopropyl alcohol); verify dryness
5. Inject two-part epoxy potting compound into cavity (vacuum-assisted to prevent voids)
6. Insert threaded insert to specified depth; verify perpendicularity (±1°)
7. Cure at room temperature 24 hours or 65°C for 2 hours
8. Pull-test sample coupons from same production batch; verify ≥2 kN pull-out strength

## Qualification Testing

Every spacecraft structure passes through a qualification programme that verifies its ability to survive the launch environment with positive margins. The test sequence typically includes static load, vibration, acoustic, shock, and thermal-vacuum deployment tests.

### Static Load Test

The structure is loaded to 1.25-1.5× the maximum expected flight load (MEFL) using hydraulic actuators and whiffletree load-introduction fixtures. Strain gauges at critical locations confirm that measured strains match the finite-element model prediction within ±10%. Permanent deformation must not exceed 0.1% of the critical dimension after return to zero load.

### Vibration and Acoustic Test

The stowed configuration is vibrated on a shaker table along each of three orthogonal axes, using the launch vehicle's acoustic/vibration spectrum enveloped by 3 dB. Random vibration levels of 0.2-1.0 g²/Hz are typical for direct-mounted spacecraft, attenuated by isolators at the separation interface. Acoustic testing in a reverberant chamber (140-148 dB overall sound pressure level) excites the large panel areas that shaker vibration cannot drive effectively.

## Thermal-Vacuum Testing

All deployable structures must be tested in a thermal-vacuum chamber that simulates the orbital environment. The chamber is evacuated to 10⁻⁵ Pa or lower and cycled through expected temperature extremes (typically -80°C to +100°C for LEO, -150°C to +120°C for deep space). Deployment tests are conducted at hot-soak, cold-soak, and ambient temperature points to verify margins across the qualification temperature range.

Common failure modes discovered in thermal-vacuum testing include:

- Adhesive softening at hot temperatures causing panel delamination
- Bearing lubricant outgassing creating drag in vacuum
- Material CTE mismatch causing binding at temperature extremes
- Residual moisture in honeycomb core causing outgassing and pressure buildup
- Shape-memory alloy actuators failing to reach transformation temperature at cold extremes
- Electronic deployment controllers drifting outside qualification range

## Troubleshooting

| Symptom | Likely cause | Diagnostic | Fix |
|---------|-------------|-----------|-----|
| Panel delamination in TVAC | Adhesive cure incomplete | Ultrasonic C-scan; DSC on adhesive | Re-bond with verified cure cycle |
| Deployment stalls | Bearing friction in vacuum | Bench test in vacuum chamber | Replace lubricant with MoS₂ or Ag-plated bearing |
| Latch fails to engage | Thermal contraction of panel stack | Measure gap at cold extreme | Adjust latch preload; add compliance |
| Pyroshock damage to electronics | Insufficient standoff distance | Accelerometer survey at component locations | Move component or add isolator |
| Crack at insert | Core potting void | X-ray inspection of insert region | Re-pot insert; vacuum-assisted potting |

## Glossary

- **CoilABLE**: Coilable Articulating Longeron Mast — a self-deploying truss boom that flattens into a tape and coils on a spool
- **STEM**: Storable Tubular Extendible Member — a thin tape that rolls onto a drum and deploys by self-rounding into a slit tube
- **HDRM**: Hold-Down Release Mechanism — a paraffin-actuated device that releases held-down components with minimal shock
- **Frangibolt**: A shape-memory-alloy collar that fractures a notched bolt when heated, releasing the held component
- **Isogrid**: A machined plate with triangular ribbing that approximates isotropic stiffness properties
- **Faceskin**: The outer sheet of a sandwich panel, bonded to the core
- **Pyroshock**: The high-frequency transient mechanical shock generated by pyrotechnic devices
- **Appropriation actuator**: An actuator that drives a deployable component from stowed to deployed position
