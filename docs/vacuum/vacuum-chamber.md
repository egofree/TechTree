# Vacuum Chamber

> **Node ID**: vacuum.vacuum-chamber
> **Domain**: [Vacuum Technology](./index.md)
> **Dependencies**: [`machine-tools.joining`](../machine-tools/joining.md), [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md)
> **Enables**: [`vacuum.deposition-systems`](./deposition-systems.md), [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`silicon.basic-devices`](../silicon/basic-devices.md)
> **Timeline**: Years 25-35
> **Outputs**: vacuum_chambers, vacuum_seals, viewports_assemblies, gate_valve_assemblies
> **Critical**: Yes — vacuum chambers are the sealed enclosures for all semiconductor thin-film deposition and plasma processes

This article covers the construction of stainless steel vacuum chambers for semiconductor processing. For chamber design engineering, flange systems, outgassing rates, and load lock design, see [Vacuum Chambers & Sealing](chambers.md). For cleaning and bake-out procedures, see [Gas Handling: Vacuum](../gas-handling/vacuum.md).

## Principle

A vacuum chamber is a sealed vessel that maintains a controlled low-pressure environment while providing access ports for pumping, gas delivery, electrical power, cooling, and optical observation. The chamber must withstand 1 atmosphere (101 kPa, 14.7 psi) of external pressure without buckling, maintain leak rates below 10⁻⁸ atm·cc/s for semiconductor processes, and present a clean internal surface that does not outgas contaminants into the process volume.

The governing structural equation for a cylindrical chamber under external pressure is the compressive hoop stress: σ = P × D / (2 × t), where P = atmospheric pressure (~0.1 MPa), D = chamber diameter, and t = wall thickness. For a 300 mm diameter chamber with 5 mm wall thickness: σ = 3 MPa — well below the 200 MPa yield strength of 304L stainless steel. However, thin-walled cylinders under external pressure fail by elastic buckling at stresses far below yield, so a buckling safety factor of 4-6 is required.

## Prerequisites

- [TIG welding capability](../machine-tools/joining.md) — full-penetration welds in stainless steel
- [Precision machining](../machine-tools/machining.md) — flange sealing surfaces to ±0.02 mm flatness
- [Stainless steel production](../metals/iron-steel.md) — 304L or 316L plate, sheet, and bar
- [Vacuum pump](./vacuum-pump.md) — for leak testing completed chamber
- [Leak detection](./leak-detection.md) — helium mass spectrometer for verifying seal integrity

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| 304L stainless steel plate (cylinder) | 30-100 kg | 3-8 mm thick, depending on diameter | [Iron & Steel](../metals/iron-steel.md) | 316L (corrosive gas service, 30-50% cost premium) |
| 304L stainless steel plate (end caps) | 10-50 kg | 8-15 mm thick, dished or flat | [Iron & Steel](../metals/iron-steel.md) | — |
| 304L stainless steel bar (flanges) | 5-30 kg | For CF or KF flange machining | [Iron & Steel](../metals/iron-steel.md) | Commercial flanges (if available) |
| OFHC copper (CF gaskets) | 0.5-2 kg | Annealed, 1-3 mm thick | [Metals](../metals/index.md) | — |
| Viton O-rings (KF seals) | Per port | Correct dash size for each KF flange | [Elastomers](../polymers/rubber.md) | Silicone O-rings (higher outgassing) |
| TIG welding consumables | 2-10 kg | ER308L filler rod, 1.6-2.4 mm | [Joining](../machine-tools/joining.md) | — |
| Fused silica (viewports) | Per viewport | 3-10 mm thick, polished | [Glass](../glass/index.md) | Borosilicate glass (no UV transmission) |
| Stainless steel tubing (cooling) | 5-20 m | 6-12 mm OD, welded to exterior | [Iron & Steel](../metals/iron-steel.md) | External water jacket |

## Construction Steps

### Main Chamber Body

1. **Roll the cylinder**: Cut 304L stainless steel plate to the developed length (π × D). Roll to the required diameter on a plate roll. For a 300 mm diameter chamber from 5 mm plate: developed length = 942 mm. Roll tolerance: ±1 mm on diameter. The longitudinal seam should be aligned for welding.

2. **Weld the longitudinal seam**: TIG weld the longitudinal seam with ER308L filler rod. Full-penetration weld from the interior first (root pass), then exterior (cover pass). Grind the interior weld flush with the base metal — any protrusion or crevice traps gas (virtual leak). Inspect with dye penetrant for surface defects.

3. **Prepare end caps**: Cut circular blanks from 8-15 mm plate. For dished (torispherical) caps: hot-form over a die to the required radius (crown radius = diameter, knuckle radius = 6% of diameter). For flat caps: machine sealing surface flat to ±0.02 mm. Flat caps are simpler but require thicker plate to resist deflection under vacuum.

4. **Weld end caps to cylinder**: Fit the end caps to the cylinder ends. Tack weld at 4-8 points. Complete circumferential weld with full penetration. Grind interior welds flush. Test all welds with dye penetrant or radiographic inspection for porosity, undercut, and incomplete fusion.

5. **Machine flange ports**: Cut openings in the cylinder wall for vacuum pump, gas inlet, electrical feedthroughs, and viewports. TIG weld pre-machined flange stubs into each opening. For UHV: use CF (ConFlat) flanges with knife-edge sealing surfaces machined to 70° included angle, 0.1 mm tip radius. For roughing and vent lines: use KF (quick-connect) flanges.

6. **Machine CF flange sealing surfaces**: If machining flanges from bar stock: turn the flange face flat to ±0.02 mm. Machine the knife-edge groove (70° included angle, 0.1 mm tip radius, depth 0.5-0.8 mm). Drill bolt holes (6-24 bolts per flange depending on size) on the bolt circle diameter. Tap bolt holes or use through-bolts with nuts.

### Viewports

7. **Install viewports**: Weld a CF flanged viewport housing into the chamber wall. The viewport consists of a fused silica or borosilicate glass window brazed into a stainless steel (or Kovar) housing that mates with a CF flange. Install on the side or top of the chamber — never the bottom (vulnerable to dropped objects). Tighten the viewport flange bolts in a star pattern (3-4 stages, final torque 15-25 N·m per bolt for CF flanges).

### Gate Valve Mounting

8. **Install gate valve flange**: Weld a large CF flange (DN100-DN200) to the pump port. The gate valve mounts between this flange and the high-vacuum pump. The gate valve isolates the pump from the chamber during vent cycles, protecting the pump from pressure bursts.

### Water Cooling

9. **Weld cooling coils**: Weld stainless steel tubing (6-12 mm OD) to the chamber exterior in a serpentine pattern. Water flows through the tubing, cooling the chamber wall during plasma processes (heat loads of 100-5000 W). Alternatively, weld an external water jacket (5-10 mm gap, welded closed). Connect water inlet/outlet with compression fittings. Pressure-test the cooling circuit at 3 bar for 10 minutes — zero leaks.

### Electrical Feedthroughs

10. **Install electrical feedthroughs**: Weld CF-flanged electrical feedthroughs into the chamber wall. Each feedthrough has ceramic-to-metal sealed pins (alumina insulator, Kovar housing) that pass electrical signals and power through the vacuum wall. Specify feedthroughs with 20-30% more pins than currently needed — adding feedthroughs later requires welding and risks damaging other components.

### Surface Preparation

11. **Clean interior surfaces**: Wipe all interior surfaces with lint-free cloth soaked in acetone to remove machining oils and handling residues. Follow with IPA rinse. Blow dry with clean, oil-free nitrogen. Inspect under bright light for scratches, weld porosity, debris, and fingerprints.

12. **Electropolish (if required)**: For UHV chambers (<10⁻⁸ Torr), electropolish the interior surfaces to Ra <0.4 μm. Electropolishing bath: phosphoric acid + sulfuric acid + glycerol, 50-80°C, current density 10-30 A/dm². This reduces outgassing by ~50% compared to mechanical polishing by creating a smooth, chromium-rich surface.

## Calibration and Verification

1. **Pressure test**: Pressurize the chamber to 1.5 bar with dry nitrogen. Hold for 30 minutes. Monitor with a pressure gauge — any pressure drop indicates a leak. Soap-test all welds and flanges for bubbles.

2. **Helium leak test**: Connect a helium mass spectrometer leak detector to the chamber. Evacuate to <10⁻³ Torr with a roughing pump. Spray helium around every weld seam, flange, viewport, and feedthrough from top to bottom. Acceptable leak rate: <10⁻⁸ atm·cc/s for semiconductor process chambers. Mark and repair any leaks found.

3. **Virtual leak check**: Isolate the chamber from all pumps. Monitor pressure rise over 2-4 hours with a capacitance manometer. If pressure rises linearly (not concave/1/t decay), a real leak exists. If pressure rises and then plateaus, suspect a virtual leak (trapped gas pocket). Re-inspect for unvented screw holes or trapped volumes.

4. **Bake-out verification**: Wrap the chamber with heating tape. Heat to 150-250°C while pumping for 24 hours. Monitor outgassing rate — it should drop from ~2×10⁻⁶ Pa·m³/s·m² (unbaked) to ~10⁻⁸ Pa·m³/s·m² (baked). Allow to cool under vacuum before venting.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Base pressure (unbaked, with turbo pump) | 10⁻⁶ to 10⁻⁷ Torr |
| Base pressure (baked 24h at 250°C, with turbo) | 10⁻⁸ to 10⁻⁹ Torr |
| Leak rate (all CF seals) | <10⁻⁹ atm·cc/s |
| Outgassing rate (304L, electropolished, baked) | ~10⁻⁸ Pa·m³/s·m² |
| Wall deflection under vacuum (300 mm dia, 5 mm wall) | <0.05 mm |
| Pump-down time to 10⁻⁶ Torr (100 L volume, unbaked) | 4-8 hours |
| Bake-out temperature range | 150-250°C (do not exceed 300°C on 304L to avoid sensitization) |
| Service life | 20+ years with proper maintenance |

## Strengths

- Stainless steel 304L is weldable, corrosion-resistant, and achieves very low outgassing after electropolishing and baking
- CF copper gasket seals are leak-tight to below 10⁻¹² atm·cc/s — suitable for the most demanding vacuum applications
- Cylindrical geometry provides uniform stress distribution and straightforward fabrication

## Weaknesses

- CF gaskets are single-use — every chamber opening requires new gaskets, adding consumable cost
- Stainless steel is heavy (8.0 g/cm³) — large chambers require cranes for handling
- Full pump-down to 10⁻⁸ Torr requires 24+ hours including bake-out — every vent event costs a full day of production

## Safety

- **Implosion hazard**: The chamber experiences ~101 kPa (14.7 psi) of external pressure under vacuum. A 300 mm viewport experiences ~7,100 N (~1,600 lbf) of force. Inspect all viewports for scratches before each pump-down. Replace any with scratches >0.1 mm deep. Install polycarbonate shields over viewports.
- **Confined space**: Large chambers are confined spaces. Never enter a chamber under vacuum — atmospheric pressure will cause lethal injuries. Never enter a chamber that has been purged with nitrogen — oxygen deficiency causes unconsciousness in seconds.
- **Sharp edges**: CF knife-edges are sharp enough to cut skin. Handle flanges with gloves. Cover exposed knife-edges with protective caps when not assembled.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Cannot reach base pressure after vent | Water vapor adsorbed on chamber walls during atmospheric exposure | Bake at 150-200°C for 24 hours while pumping; vent with dry N₂ instead of air; extend pump-down |
| CF flange leak after reassembly | Copper gasket work-hardened from previous use (single-use) or knife-edge nicked | Replace copper gasket (mandatory on each assembly); inspect knife-edge for nicks with magnifier |
| Virtual leak — slow pressure rise after isolation | Unvented screw hole or trapped volume in weld | Replace screws with vented screws (axial hole drilled through center); inspect welds for incomplete fusion |
| Viewport cracking during bake-out | Differential thermal expansion between glass and metal housing | Use Kovar-matched viewports; limit bake-out rate to 1-2°C/min; never tighten viewport bolts while hot |

## See Also

- [Vacuum Chambers & Sealing](chambers.md) — advanced chamber design, flange systems, outgassing data
- [Vacuum Pump](./vacuum-pump.md) — pump construction for evacuating chambers
- [Leak Detection](./leak-detection.md) — helium leak detection methods
- [Gas Handling: Vacuum](../gas-handling/vacuum.md) — outgassing rates and bake-out procedures
- [Deposition Systems](deposition-systems.md) — integrated systems built around vacuum chambers

Chamber passivation reduces baseline outgassing and improves ultimate vacuum. Electropolished stainless steel provides a natural chromium oxide passivation layer. For UHV applications, titanium sublimation pumping deposits a fresh titanium getter film on chamber walls that actively absorbs reactive gas molecules.

Internal components (fixtures, sample holders, process tooling) must use low-outgassing materials: stainless steel and aluminum are preferred. Avoid plastics, elastomers, and porous materials inside the chamber unless specifically rated for vacuum. Clean all internal components by the same solvent/IPA/bake procedure used for the chamber itself before installation.

## Scaling Notes

Vacuum chamber production scales with welding capability and machining precision:

- **Laboratory scale** (1-5 chambers/year): Hand-rolled cylinder from 3-5 mm plate. Manual TIG welding of all seams. Flanges machined on a manual lathe and mill. Helium leak testing with a portable leak detector. Adequate for R&D, university labs, and small-scale process development. One skilled TIG welder + one machinist. Chamber size limited to ~300 mm diameter × 400 mm length.

- **Production scale** (10-50 chambers/year): CNC-rolled and welded cylinders. Automated orbital TIG welding for consistent full-penetration seams. CNC-machined flanges from bar stock. Integrated helium leak testing station with automated spray probing. Water jet cutting for port openings. 5-10 workers. Chamber sizes up to 1,000 mm diameter. This scale supports a semiconductor fab's equipment needs.

- **Large-scale** (custom, 2-10 per year): Chambers for batch processing tools, space simulation, or large-coating systems. Diameters 1-5 meters. Require specialized rolling equipment, large-capacity welding positioners, and on-site machining for flange sealing surfaces. Vacuum testing requires dedicated roughing/turbo pump sets sized for the volume. These are one-of-a-kind or small-batch items.

**Critical bottleneck**: Leak-tight welding. A single pinhole porosity defect in a weld seam renders the entire chamber unusable for high vacuum. TIG welding stainless steel in the flat and horizontal positions with full penetration requires significant skill. Automated orbital welding eliminates the skill dependency but requires capital investment in welding equipment.

## Quality Control

| Check | Method | Acceptance Criteria |
|-------|--------|-------------------|
| Weld integrity | Dye penetrant testing (all seams) | No linear indications >1 mm |
| Weld integrity (critical) | Radiographic inspection (circumferential seams) | No porosity >1.5 mm, no incomplete fusion |
| Flange sealing surface flatness | Surface plate + dial indicator | ±0.02 mm across full flange face |
| CF knife-edge geometry | Optical comparator or profile projector | 70° ±2° included angle, 0.1 mm tip radius ±0.05 mm |
| Pressure test (positive) | 1.5 bar dry N₂, 30 min hold | Zero pressure drop on gauge |
| Helium leak test | Mass spectrometer, spray probe all seams | <10⁻⁸ atm·cc/s total |
| Virtual leak test | Isolate chamber, monitor 4 hours | Pressure plateaus (no linear rise) |
| Outgassing rate (post-bake) | Rate-of-rise measurement | <10⁻⁸ Pa·m³/s·m² for electropolished 304L |
| Wall deflection under vacuum | Dial indicator on viewport center | <0.05 mm for 300 mm dia, 5 mm wall |

## Variations and Alternatives

| Chamber Type | Material | Pressure Range | Best Application |
|-------------|----------|---------------|-----------------|
| Cylindrical, 304L SS | 304L stainless steel | 10⁻⁶ to 10⁻⁹ Torr | General semiconductor processing, sputtering, evaporation |
| Bell jar on baseplate | Borosilicate glass or SS | 10⁻⁴ to 10⁻⁷ Torr | Simple evaporation, educational, small-batch coating |
| Box chamber (rectangular) | 304L SS, reinforced | 10⁻⁶ to 10⁻⁸ Torr | Batch wafer processing, large substrate coating |
| Aluminum chamber | 6061-T6 aluminum | 10⁻⁶ to 10⁻⁸ Torr | Non-magnetic applications (beam lines, particle physics) |
| Copper chamber | OFHC copper | 10⁻⁹ to 10⁻¹² Torr | Extreme UHV, surface science, synchrotron |
| Titanium sublimation chamber | 304L SS + Ti getter | 10⁻⁹ to 10⁻¹¹ Torr | UHV surface analysis, molecular beam epitaxy |

**Bell jar alternative**: For simple evaporation and coating applications that do not require UHV, a glass bell jar seated on a polished steel baseplate is far simpler to construct than a welded stainless chamber. Base pressure is limited to ~10⁻⁶ Torr by the glass outgassing rate, but this is adequate for many thin-film deposition tasks. No welding required — only the baseplate needs machining for pump and feedthrough ports.

## Safety & Hazards

- **Implosion hazard**: The chamber experiences ~101 kPa (14.7 psi) of external pressure under vacuum. A 300 mm viewport experiences ~7,100 N (~1,600 lbf) of force. Inspect all viewports for scratches before each pump-down. Replace any with scratches >0.1 mm deep. Install polycarbonate shields over viewports. Never stand in the direct line of a viewport during pump-down.
- **Confined space**: Large chambers are confined spaces. Never enter a chamber under vacuum — atmospheric pressure will cause lethal injuries. Never enter a chamber that has been purged with nitrogen — oxygen deficiency causes unconsciousness in seconds. Follow OSHA confined space entry procedures (atmospheric testing, rescue plan, attendant).
- **Sharp edges**: CF knife-edges are sharp enough to cut skin. Handle flanges with gloves. Cover exposed knife-edges with protective caps when not assembled. Dispose of used copper gaskets carefully — the compressed gasket edges are razor-sharp.
- **Bake-out burn hazard**: Chambers during bake-out reach 150-250°C on external surfaces. Post warning signs during bake-out. Allow full cooling before touching chamber surfaces. Use infrared thermometer to verify temperature before contact.
- **Heavy lifting**: A 300 mm diameter stainless chamber with flanges weighs 50-150 kg. Use overhead crane or engine hoist for installation. Never lift by a flange port — lift from the main cylinder body with rated slings.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Cannot reach base pressure after vent | Water vapor adsorbed on chamber walls during atmospheric exposure | Bake at 150-200°C for 24 hours while pumping; vent with dry N₂ instead of air; extend pump-down |
| CF flange leak after reassembly | Copper gasket work-hardened from previous use (single-use) or knife-edge nicked | Replace copper gasket (mandatory on each assembly); inspect knife-edge for nicks with magnifier |
| Virtual leak — slow pressure rise after isolation | Unvented screw hole or trapped volume in weld | Replace screws with vented screws (axial hole drilled through center); inspect welds for incomplete fusion |
| Viewport cracking during bake-out | Differential thermal expansion between glass and metal housing | Use Kovar-matched viewports; limit bake-out rate to 1-2°C/min; never tighten viewport bolts while hot |
| Pressure rises linearly (not plateau) after isolation | Real leak at weld seam, flange, or feedthrough | Helium leak test with spray probe, working top to bottom; repair weld defects by grinding out and re-welding |
| Outgassing rate does not drop during bake-out | Internal surfaces contaminated with oil, fingerprints, or machining residue | Disassemble and clean interior with acetone/IPA; re-electropolish if necessary; verify all plastic and elastomeric materials removed from chamber |

## See Also

- [Vacuum Chambers & Sealing](chambers.md) — advanced chamber design, flange systems, outgassing data
- [Vacuum Pump](./vacuum-pump.md) — pump construction for evacuating chambers
- [Leak Detection](./leak-detection.md) — helium leak detection methods
- [Gas Handling: Vacuum](../gas-handling/vacuum.md) — outgassing rates and bake-out procedures
- [Deposition Systems](deposition-systems.md) — integrated systems built around vacuum chambers

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Vacuum Technology](./index.md) • [All Domains](../../index.md)*
