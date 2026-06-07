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


Vacuum chamber O-rings (typically Viton or Buna-N) must be kept clean and free of nicks or cuts. Even a single hair across an O-ring seal can prevent the chamber from reaching high vacuum. Handle O-rings with clean, lint-free gloves. Apply a thin film of vacuum grease only if recommended by the manufacturer — excess grease contaminates the vacuum surface and increases outgassing. Replace O-rings on a regular maintenance schedule, as they harden and lose elasticity over time, especially in high-temperature bakeout cycles.

Water vapor is the most pervasive contaminant in vacuum systems. Atmospheric air contains water vapor that adsorbs on all internal surfaces as molecular layers. When the chamber is pumped down, these layers desorb slowly, creating a continuous gas load that dominates the pumpdown at pressures below the medium vacuum range. Baking the chamber (heating to elevated temperature while pumping) accelerates the desorption of water and reduces the time to reach base pressure from days to hours. The baking temperature is limited by the materials present — elastomer seals cannot tolerate temperatures above 150-200°C, while all-metal sealed chambers can be baked above 300°C.

Chamber design must account for the pumping ports, feedthroughs (electrical, mechanical, fluid), viewports, and access doors needed for the specific application. Each penetration through the chamber wall is a potential leak source and an outgassing source. Minimizing the number of penetrations reduces both the leak probability and the outgassing load. Ports should be sized for the required conductance — undersized ports restrict pumping speed, while oversized ports add unnecessary cost and surface area.

The choice of sealing method depends on the vacuum level and the need for repeated opening. For rough vacuum, elastomer O-rings (Viton, Buna-N, silicone) provide adequate sealing and allow easy access. For high vacuum, elastomer O-rings can still be used but their outgassing rate limits the achievable base pressure. For ultra-high vacuum, metal seals (copper gaskets in Conflat flanges, or indium wire seals) are mandatory because they have negligible outgassing and can be baked to high temperatures. Metal seals are single-use — the gasket must be replaced each time the flange is opened.
as gas reservoirs that slowly release adsorbed molecules during pumpdown.
and are less likely to trap contaminant particles. Rough or porous surfaces act
mirror finish) have less surface area for gas adsorption, are easier to clean,
cleanability. Polished surfaces (electropolished or mechanically polished to
The surface finish of internal chamber walls affects both outgassing rate and

replaced each time the connection is opened.
for many gasket changes), but the copper gaskets are single-use and must be
provides virtually zero leakage. CF flanges are reusable (the knife edges last
creating a metal-to-metal seal that is bakeable to high temperatures and
They use a flat copper gasket compressed between two knife-edge flanges,
Conflat (CF) flanges are the standard high-vacuum and UHV connection system.

reducing time-to-base-pressure from days to hours.
Baking the chamber to elevated temperature while pumping accelerates desorption,
during pumpdown, dominating the gas load at pressures below medium vacuum.
layers on all internal surfaces from atmospheric exposure, then desorbs slowly
Water vapor is the most pervasive vacuum contaminant. It adsorbs as molecular

surface area.
undersized ports restrict pumping speed, while oversized ports add cost and
leak and outgassing source. Ports should be sized for adequate conductance —
mechanical, fluid), viewports, and access doors. Each penetration is a potential
Chamber design must account for pumping ports, feedthroughs (electrical,

are mandatory for negligible outgassing and high-temperature baking capability.
pressure. For ultra-high vacuum, metal seals (copper gaskets in Conflat flanges)
high vacuum, O-rings are still usable but their outgassing limits the base
elastomer O-rings (Viton, Buna-N) provide adequate sealing and easy access. For
The choice of sealing method depends on the vacuum level. For rough vacuum,

Vacuum chamber internals (fixtures, sample holders, process tooling) must be designed for
minimal outgassing. Stainless steel and aluminum are the preferred materials. Avoid plastics,
elastomers, and porous materials inside the chamber unless specifically rated for vacuum use.
All internal components should be cleaned by the same procedures used for the chamber itself
(solvent washing, deionized water rinse, bakeout) before installation.

The cost of a vacuum chamber scales steeply with size and vacuum level. A small laboratory
bell jar for rough vacuum costs relatively little. A large production chamber for high-vacuum
thin film deposition, with multiple ports, viewports, and a load-lock, represents a major
capital investment. The chamber body must be fabricated by a machine shop capable of producing
flat, smooth sealing surfaces and precision-welded joints. This manufacturing requirement
places vacuum chamber production firmly in the industrial development phase.

Viewport materials must be chosen for both optical transparency and vacuum compatibility.
Borosilicate glass is standard for most applications, while quartz (fused silica) is used for
UV transparency or higher temperature resistance. Viewports are typically mounted on ConFlat
flanges with copper gaskets and must be handled carefully to avoid scratching or cracking the
glass, which would compromise both the optical path and the vacuum integrity.


---

Chamber passivation — coating the interior surfaces with a stable, low-outgassing film —
reduces the baseline outgassing rate and improves the achievable ultimate vacuum. Electropolished
stainless steel surfaces provide a natural chromium oxide passivation layer. For ultra-high
vacuum applications, titanium sublimation pumping deposits a fresh titanium getter film on the
chamber walls that actively absorbs reactive gas molecules.


*Part of the [Bootciv Tech Tree](../index.md) • [Vacuum Technology](./index.md) • [All Domains](../index.md)*
