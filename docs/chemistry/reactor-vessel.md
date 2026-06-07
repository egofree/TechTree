# Reactor Vessel

> **Node ID**: chemistry.reactor-vessel
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`metals.forming`](../metals/forming.md), [`metals.welding`](../machine-tools/welding-equipment.md)
> **Enables**: [`chemistry.fermentation`](fermentation.md), [`chemistry.acids`](acids.md), [`chemistry.alkalis`](alkalis.md), [`chemistry.solvents`](solvents.md)
> **Timeline**: Years 15-30
> **Outputs**: batch_reaction, continuous_reaction
> **Critical**: Yes — reactor vessels are the fundamental unit of chemical manufacturing. Every batch reaction, fermentation, acid digestion, and synthesis requires a contained, controlled environment. No chemical industry operates without them.

## Overview

A reactor vessel is a sealed container designed to hold chemical reactions under controlled conditions of temperature, pressure, agitation, and residence time. The vessel must contain the reaction safely while allowing heat addition or removal, mixing of reactants, sampling, and product discharge. Reactor design is governed by the reaction kinetics (how fast the reaction proceeds), thermodynamics (how much heat is released or absorbed), and the physical properties of the reactants and products (corrosiveness, toxicity, flammability).

Two fundamental reactor types exist: **batch reactors** (fixed volume, reactants charged, reaction proceeds, products discharged) and **continuous reactors** (steady flow of reactants through the vessel, products continuously withdrawn). Batch reactors dominate at smaller scales and for multi-product facilities; continuous reactors (CSTR — continuously stirred tank reactor, or PFR — plug flow reactor) dominate at large scale for single high-volume products.

Reactor performance is characterized by conversion (fraction of reactant consumed), selectivity (fraction of consumed reactant that becomes the desired product), and yield (fraction of starting reactant that becomes the desired product). For a first-order reaction in a batch reactor, conversion X = 1 − e^(−kt), where k is the rate constant and t is the reaction time. The rate constant approximately doubles for every 10°C temperature increase (Arrhenius relationship). This temperature sensitivity makes precise temperature control critical — a 5°C error in reactor temperature can change the reaction rate by 30-50%.

The vessel shell must withstand the design pressure (internal or external) at the design temperature. For jacketed vessels, the shell also serves as the heat transfer surface. The agitator provides mixing to ensure uniform temperature and composition throughout the vessel volume. Baffles prevent vortexing and improve mixing efficiency. Three principal designs cover the range of chemical processing: **batch stirred-tank reactors** (versatile, most common), **continuous stirred-tank reactors (CSTR)** (same vessel, steady-state operation with continuous feed and discharge), and **plug flow reactors (PFR)** (tubular, no back-mixing, highest conversion per unit volume for positive-order reactions).

## Prerequisites

- **[Pressure vessel code](reactor-vessel.md)**: ASME Section VIII design and fabrication (this document)
- **[Welding](../machine-tools/welding-equipment.md)**: Full-penetration welds, radiographic inspection, ASME-qualified welders
- **[Steel plate](../metals/iron-steel.md)**: Carbon steel A516 Gr.70 or 304L/316L stainless for corrosive service
- **[Electric motor and gear reducer](../energy/electricity.md)**: 0.5-50 kW with 10:1 to 40:1 speed reduction for agitator
- **[Mechanical seal](../polymers/rubber.md)**: Cartridge-type seal rated for design pressure and temperature

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate](../metals/iron-steel.md) (shell) | 200-2,000 kg | Carbon steel A516 Gr.70, 6-25 mm thick | [Iron & Steel](../metals/iron-steel.md) | Stainless steel 304L/316L (corrosive service) |
| [Steel plate](../metals/iron-steel.md) (jacket) | 100-800 kg | Carbon steel A36, 6-10 mm thick | [Iron & Steel](../metals/iron-steel.md) | Half-pipe coil (less surface area, simpler) |
| [Stainless steel](../metals/iron-steel.md) | 50-500 kg | 316L for corrosive service, internal clad or solid | [Iron & Steel](../metals/iron-steel.md) | Glass-lined steel (for strong acids), titanium (for chlorides) |
| [Steel shaft](../metals/iron-steel.md) (agitator) | 20-100 kg | 1045 or 416 stainless, 40-80 mm diameter | [Iron & Steel](../metals/iron-steel.md) | Alloy 20 shaft (sulfuric acid service) |
| [Electric motor](../energy/electricity.md) | 1 unit | 1-50 kW, 3-phase, 1750 RPM | [Electricity](../energy/electricity.md) | Hydraulic drive (hazardous area) |
| [Gear reducer](../machine-tools/machining.md) | 1 unit | 10:1 to 40:1 ratio, rated for motor torque | [Machining](../machine-tools/machining.md) | V-belt drive (less precise) |
| [Mechanical seal](../polymers/rubber.md) | 1 unit | Cartridge-type, rated for design pressure and temperature | [Elastomers](../polymers/rubber.md) | Packed gland (simpler, higher leakage) |
| [Gaskets](../polymers/rubber.md) | 1 set | PTFE or spiral-wound, matched to flange size | [Elastomers](../polymers/rubber.md) | Compressed fiber (lower temperature) |
| [Bolts and nuts](../metals/steelmaking.md) | 10-50 kg | ASTM A193 B7 or B8, matched to flange class | [Fasteners](../metals/steelmaking.md) | — |
| [Welding consumables](../machine-tools/welding-equipment.md) | 10-50 kg | E7018 (carbon steel) or E316L-16 (stainless) | [Welding](../machine-tools/welding-equipment.md) | — |
| [Thermowell](../measurement/index.md) | 2-4 units | 316L stainless, 150-300 mm immersion | [Measurement](../measurement/index.md) | — |
| [Insulation](../construction/building-materials.md) | 10-50 m² | Mineral wool, 50-100 mm thick, aluminum cladding | [Construction](../construction/building-materials.md) | Calcium silicate (higher temperature) |

## Process Description

### Shell Fabrication

1. **Calculate design parameters**: Determine vessel volume (50-10,000 L typical), design pressure (1-20 bar), design temperature (−20°C to 300°C). Calculate minimum wall thickness per ASME Boiler and Pressure Vessel Code Section VIII: t = (P × R) / (S × E − 0.6 × P), where P = design pressure, R = inside radius, S = allowable stress, E = joint efficiency (0.85 for spot-radiographed, 1.0 for fully radiographed). For a 2,000 L vessel (1.3 m diameter, 1.5 m straight side) at 6 bar design pressure, A516 Gr.70 steel (S = 138 MPa at 200°C), E = 0.85: t = (6 × 650) / (138 × 0.85 − 0.6 × 6) = 34 mm → round to 36 mm with corrosion allowance.

2. **Roll shell cylinders**: Cut steel plate to the developed length (π × inside diameter + weld shrinkage allowance). Roll to cylinder in a plate roll — multiple passes for thicker plate. Check roundness with a sweep board: deviation <1% of diameter.

3. **Weld longitudinal seam**: Fit and tack the longitudinal seam. Weld with full-penetration double-V groove weld (root pass on inside, fill and cap on outside). Use E7018 electrodes (or E316L-16 for stainless). Grind flush on the inside for cleanability.

4. **Attach bottom head**: Fit and weld a torispherical (dished) head to the shell cylinder. Heads are either purchased as pre-formed dished heads or, for small vessels (<500 mm diameter), formed by spinning or pressing from a single plate disc. Weld with full-penetration butt weld.

5. **Attach top head or flange**: For vessels requiring internal access, attach a welding-neck flange ring to the top of the shell cylinder. For sealed vessels, attach a second dished head with nozzle penetrations for agitator shaft, feed, vent, pressure relief, and instrument connections.

6. **Weld nozzles**: Cut openings for all process connections (feed, discharge, vent, drain, instrument, agitator, thermowells). Weld nozzle necks (schedule 40 or 80 pipe, 50-150 mm diameter) into the shell with full-penetration welds. Reinforcement pads (repads) required when the opening exceeds 50% of the shell diameter.

7. **Radiograph welds**: X-ray or gamma-ray all longitudinal and circumferential seam welds. Acceptance per ASME Section VIII: no cracks, incomplete fusion, or slag inclusions exceeding the code limits. Repair and re-radiograph any defects.

### Jacket Attachment

8. **Install jacket spacer rings**: Weld two circumferential spacer rings to the outer shell surface at the top and bottom of the jacket zone. These define the jacket cavity height.

9. **Roll and fit jacket cylinder**: Roll outer jacket cylinder (6-10 mm plate) to fit over the spacer rings with 25-50 mm annular gap. The jacket cylinder is larger than the shell by twice the annular gap plus clearance.

10. **Weld jacket to spacer rings**: Fit jacket cylinder over spacer rings. Weld outer circumference at top and bottom with fillet welds. Install jacket coolant inlet and outlet nozzles (typically at bottom and top respectively for counter-current flow).

11. **Hydrostatic test jacket**: Fill jacket with water at 1.5× design pressure. Hold 30 minutes, inspect all welds for leaks. Zero leaks acceptable. Drain and dry.

### Agitator and Drive

12. **Fabricate agitator shaft**: Turn shaft from solid bar stock on a lathe. Diameter sized for torsional load: τ = T / (π × d³ / 16) must be below allowable shear stress at design RPM. Typical shaft diameter: 40-80 mm for vessels up to 5,000 L. Keyway at top for coupling to gear reducer.

13. **Attach impeller blades**: Weld or bolt impeller blades to the shaft. Common impeller types: Rushton turbine (6 flat blades on a disc, 100-300 mm diameter, for gas dispersion and high shear), pitched-blade turbine (4 blades at 45°, for axial flow and blending), marine propeller (for low-viscosity blending). Impeller diameter typically 1/3 to 1/2 of vessel diameter. Install 2-3 impellers spaced 1-1.5 impeller diameters apart on the shaft for tall vessels.

14. **Install baffles**: Weld four baffle plates (width = 1/10 to 1/12 of vessel diameter) to the vessel interior wall, 90° apart, offset 1/6 baffle width from the wall. Baffles prevent solid-body rotation and force turbulent mixing. For a 1,300 mm diameter vessel: baffle width = 110-130 mm.

15. **Mount mechanical seal**: Install the mechanical seal assembly on the agitator shaft at the top head penetration. The seal contains rotating and stationary faces (carbon vs. silicon carbide or tungsten carbide) pressed together by spring force, preventing process fluid from escaping along the shaft. For corrosive or toxic service, use a double mechanical seal with barrier fluid.

16. **Mount motor and gear reducer**: Bolt the gear reducer flange to the mounting bracket on the vessel top head. Couple the agitator shaft to the gear reducer output shaft via a rigid or flexible coupling. Bolt the motor to the gear reducer input. Align to within 0.05 mm offset and 0.05 mm angularity using dial indicators.

### Final Assembly and Testing

17. **Hydrostatic test vessel**: Fill the vessel with water. Pressurize to 1.5× MAWP (maximum allowable working pressure). Hold 30 minutes. Inspect all welds, nozzles, and flange connections for leaks. Zero leaks acceptable. Record test pressure and duration.

18. **Install pressure relief device**: Mount a pressure relief valve or rupture disc on a dedicated nozzle at the top of the vessel. Set relief pressure to 1.1× MAWP. The relief device must be sized to discharge the full rated flow at set pressure — calculate required orifice area per API 521 for the worst-case overpressure scenario (external fire, runaway reaction, utility failure).

19. **Install insulation**: Apply 50-100 mm mineral wool insulation to the vessel shell and jacket. Cover with 0.5 mm aluminum sheet metal cladding, secured with banding straps. Insulation reduces heat loss, stabilizes temperature, and provides personnel protection (surface temperature <60°C).

20. **Install instruments**: Mount thermowells (2-4 locations: top, middle, bottom, jacket inlet), pressure gauge (0-1.5× design range), and sight glass (for visual level and mixing observation). Connect temperature and pressure instruments to control panel.

## Operating Procedure (Batch Stirred-Tank Reactor)

1. **Pre-startup inspection**: Verify all nozzles are connected and valved correctly. Check that the pressure relief valve is installed and not blocked. Confirm the agitator shaft turns freely by hand (before charging). Verify the mechanical seal has barrier fluid (for double seals) or flush connection is active.
2. **Charge reactants**: Open the top head (or manway for flanged vessels). Charge solid reactants through the manway. Close and bolt the manway. Charge liquid reactants through the feed nozzle using a transfer pump. Record the mass of each reactant charged (mass flow meter or weighed containers).
3. **Establish mixing and heating**: Start the agitator at low speed. Open the jacket steam or hot water valve. Heat to the reaction initiation temperature at 1-2°C/min (limit thermal stress on the shell and jacket). Monitor temperature via the vessel thermowell (not the jacket inlet — vessel temperature lags jacket by 5-15°C).
4. **Reaction phase**: When the reaction temperature is reached, maintain temperature by modulating the jacket cooling/heating. For exothermic reactions: the jacket must remove the heat of reaction. Monitor temperature closely — a 2-3°C rise above setpoint may indicate a runaway starting. Record temperature, pressure, and agitator current every 5-15 minutes.
5. **Sampling**: Take a reaction sample through the sample valve (extended-stem valve with splash guard). Analyze by the appropriate method (titration, GC, pH, conductivity). Compare to the endpoint specification. Continue the reaction until the endpoint is reached.
6. **Cooling and discharge**: Switch the jacket to cooling. Cool to below 50°C (or the safe discharge temperature for the product). Stop the agitator. Open the bottom discharge valve. Transfer the product to the next processing step (filtration, crystallization, distillation). Rinse the vessel with solvent or water to recover residual product.
7. **Cleaning**: Clean the vessel interior between batches. For water-soluble products: rinse with hot water. For oil-based products: rinse with solvent, then water. For polymerized or encrusted deposits: fill with cleaning solution (NaOH 2-5% for organics, HCl 5-10% for mineral scale) and agitate at 60-80°C for 1-4 hours. Drain, rinse, and inspect.

## Calibration and Verification

1. **Pressure test verification**: Confirm hydrostatic test at 1.5× MAWP held for 30 minutes with zero pressure drop. All joints soap-tested.

2. **Agitator shaft runout**: Dial-indicate the shaft at the seal area with the shaft rotating by hand. Total indicated runout must be <0.05 mm. If excessive, check shaft straightness and coupling alignment.

3. **Motor current draw**: Run the agitator with the vessel filled with water at the design liquid level. Measure motor current at operating speed. Current should be 40-70% of motor nameplate full-load amps. If >85%, the impeller diameter or speed is too high for the fluid — reduce speed or trim impeller diameter.

4. **Heat transfer verification**: Fill jacket with hot water or steam at design temperature. Measure the rate of temperature rise in a vessel full of water. Calculate actual heat transfer coefficient: U = Q / (A × LMTD), where Q = m × Cp × ΔT/Δt, A = jacket surface area, LMTD = log mean temperature difference. Compare to design value; accept if within ±15%.

5. **Relief valve test**: Verify relief valve lifts at set pressure using a calibrated test stand or by pressurizing the vessel with water to the set point.

## Quantitative Parameters

| Parameter | Batch Stirred-Tank | CSTR | PFR (Tubular) |
|-----------|-------------------|------|---------------|
| Working volume | 50-10,000 L | 500-50,000 L | Pipe or tube bundle |
| Diameter-to-height ratio | 1:1 to 1:3 | 1:1 to 1:3 | 1:10 to 1:100 (L/D) |
| Design pressure | 1-20 bar | 1-10 bar | 1-300 bar |
| Design temperature | −20°C to 300°C | −20°C to 200°C | −40°C to 600°C |
| Heat transfer area (jacketed) | 2-30 m² | 5-100 m² | External (furnace or jacket) |
| Overall heat transfer coefficient (jacket, water-water) | 200-500 W/m²·K | 200-500 W/m²·K | 300-1,500 W/m²·K (tube wall) |
| Agitator power (typical) | 0.5-5 kW/m³ | 0.5-3 kW/m³ | N/A (no agitator) |
| Mixing time (low-viscosity) | 30-120 seconds to 95% | 30-120 seconds | N/A (no back-mixing) |
| Maximum fluid viscosity (turbine) | 5,000 mPa·s | 5,000 mPa·s | N/A |
| Residence time | Hours (batch) | Volume / flow rate | Volume / flow rate |
| Conversion per unit | 80-99% (batch) | 50-80% per stage | 80-99% (no back-mixing) |
| Service life | 10-20 years (CS), 20-30 years (SS) | 10-20 years | 10-30 years |

## Scaling Notes

- **Geometric similarity**: Scale vessels by maintaining constant diameter-to-height ratio, impeller-to-vessel diameter ratio, and baffle width-to-vessel diameter ratio. Power per unit volume (kW/m³) is the primary scale-up parameter for agitated vessels. Keep impeller tip speed constant for shear-sensitive products (<3 m/s for crystal suspensions, <1 m/s for cell cultures).
- **Heat transfer limitation**: Jacket heat transfer area scales with diameter × height (≈ D²), while volume scales with D² × H. For geometrically similar vessels, the area-to-volume ratio decreases as the vessel gets larger. Above 5,000 L, external heat exchangers with circulation loops may be required to supplement the jacket.
- **CSTR cascade scaling**: Higher conversion in CSTRs is achieved by chaining reactors in series. For a first-order reaction with 99% conversion, a single CSTR requires 100× the residence time of a PFR. Two CSTRs in series require 22×. Five CSTRs require 10×. The trade-off is equipment cost (more vessels) vs. conversion efficiency.
- **PFR scaling**: Scale by adding parallel tubes (multi-tubular reactor) or increasing tube length. For catalytic reactions, the tube diameter is fixed by heat transfer requirements (typically 25-50 mm). Scale to thousands of tubes for large production.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Incomplete mixing (temperature or concentration gradients) | Impeller too small or too slow; baffles missing or corroded; high-viscosity fluid beyond turbine capability | Increase impeller speed (verify motor current <85% FLA); install or replace baffles; for viscosity >5,000 mPa·s, switch to anchor or helical ribbon impeller |
| Poor heat transfer (U <70% of design) | Jacket fouled with scale or rust; air trapped in jacket (reduces effective area); steam condensate flooding jacket | Chemical clean jacket (acid descale); vent air from jacket high point; install steam trap and verify condensate drains freely |
| Mechanical seal leaking | Seal faces worn or damaged; shaft runout excessive; product crystallizing on seal faces | Replace seal faces; verify shaft runout <0.05 mm TIR; install quench or buffer fluid connection to wash seal faces; consider double seal for hazardous products |
| Agitator vibration | Shaft bent or coupling misaligned; impeller damaged or eroded; bearing failure; resonance at operating speed | Check shaft straightness (<0.02 mm/m); verify coupling alignment; inspect impeller for damage; replace bearings; verify operating speed is >20% above or below the first critical speed |
| Pressure relief valve weeping | Valve seat damaged by corrosion or debris; set pressure drift from spring fatigue; product solidifying on seat | Remove, clean, and lap the valve seat; test set pressure on calibrated stand; install a rupture disc upstream of the relief valve for corrosive service |
| Runaway reaction (temperature rising uncontrollably) | Cooling system failure (jacket steam trap failed, cooling water lost); feed rate too high for exothermic reaction; agitator failure causing hot spots | Emergency: activate backup cooling (quench water, dump cold solvent into vessel); shut off feed; verify emergency relief device is functional; install high-temperature alarm with automatic feed shutdown |

## Safety

- **Pressure vessel failure**: Overpressure can rupture the vessel, releasing energy proportional to the compressed gas volume. At 6 bar internal pressure, a 5,000 L vessel contains enough stored energy to destroy the surrounding structure. Install pressure relief valve at 1.1× MAWP. Never block or plug relief valves. Hydrostatic test at 1.5× MAWP before first use. Periodic inspection every 5 years per API 510.
- **Chemical burns**: Reactors handling acids, bases, and hot process fluids present severe burn hazards. All sample ports and drain valves must have splash guards. Emergency shower and eyewash within 10 seconds travel time. Insulate all hot surfaces to <60°C surface temperature.
- **Agitator entanglement**: The agitator shaft and impeller can entangle clothing, hair, or limbs. Never open a vessel manway with the agitator running. Lock-out/tag-out the motor before vessel entry. Guards on all exposed rotating parts.
- **Runaway reaction**: Exothermic reactions can accelerate uncontrollably if cooling fails. Design emergency cooling (backup water supply, quench system). Install high-temperature and high-pressure alarms with automatic shutdown. Size relief device for worst-case runaway scenario using DIERS methodology.
- **Flammable atmospheres**: Vessels containing flammable liquids must be purged with nitrogen before and after filling. Ground and bond all metal connections. Use explosion-proof motor and instruments (Class 1 Div 1 or 2).

## Quality Control

- **Reaction completion**: Monitor by temperature, pressure, or analytical measurement (pH, conductivity, gas evolution). Define endpoint criteria before each batch. For batch reactors: sample and analyze at 80% of expected reaction time to verify progress.
- **Product purity**: Sample product and analyze by the appropriate method (GC for organics, titration for acids/bases, HPLC for pharmaceuticals). Compare to specification. Re-crystallize or re-distill if out of spec.
- **Material balance**: Verify that charge weight + feed weight = product weight + waste weight + sampling losses (within ±2%). Larger discrepancy indicates leaks, spills, or measurement errors.
- **Vessel integrity**: Annual visual inspection of internal surfaces (corrosion, cracking, weld condition). Thickness measurement by ultrasonic testing at least every 5 years. Compare measured thickness to design minimum. Retire the vessel when any point reaches the calculated minimum wall thickness.

## Variations and Alternatives

- **Glass-lined reactors**: Carbon steel shell lined with vitreous enamel (borosilicate glass, 0.5-1.0 mm thick, fired at 800-900°C). Superior corrosion resistance to mineral acids (HCl, H₂SO₄, HNO₃, H₃PO₄) at temperatures up to 200°C. Used for pharmaceutical, dye, and specialty chemical production. Disadvantage: glass lining chips on mechanical impact — no metal tools or hard objects inside the vessel.
- **Stainless steel reactors**: Solid 316L stainless construction for food, pharmaceutical, and mildly corrosive chemical service. Electropolished internal surface (Ra <0.4 µm) for cleanability. Higher cost than carbon steel but longer life in corrosive service.
- **High-pressure reactors (autoclaves)**: Thick-walled vessels (25-100 mm wall) rated for 50-300 bar. Used for hydrogenation, polymerization, and hydrothermal synthesis. Forged or machined from solid billet rather than rolled plate. Require ASME Section VIII Division 2 design (higher safety factor, more rigorous analysis).
- **Plug flow reactor (PFR)**: Tubular reactor (pipe or tube bundle) with no back-mixing. Higher conversion per unit volume than CSTR for the same reaction. Used for large-volume continuous processes (petroleum cracking, polymerization). Constructed from pipe or tubes, not a vessel. No agitator — mixing occurs by turbulent flow.
- **Semi-batch reactor**: A batch vessel with one reactant charged initially and a second reactant added continuously. Used for highly exothermic reactions where controlling the addition rate limits heat release. Also used for reactions where one reactant is a gas (bubbled through the liquid continuously). Most hydrogenation and chlorination reactions use semi-batch operation.
- **Microreactor**: Channel dimensions 0.01-1 mm etched or machined in metal, glass, or silicon. Extremely high surface-area-to-volume ratio enables rapid heat removal (>10 kW/L). Used for highly exothermic or hazardous reactions at small scale (pharmaceutical intermediates, nitration). Not bootstrap-appropriate but relevant for understanding the limits of reactor miniaturization.
- **Autoclave**: A small, thick-walled batch reactor rated for high pressure (50-300 bar) and temperature (up to 500°C). Used for hydrogenation, polymerization, hydrothermal synthesis, and laboratory process development. Forged or machined from solid billet. Equipped with a magnetic-drive agitator (no shaft seal — the magnetic coupling transmits torque through the pressure boundary).

## References

- [Distillation Column](distillation-column.md) — column construction shares pressure vessel principles
- [Heat Exchanger](heat-exchanger.md) — jacket heat transfer design
- [Fermentation](fermentation.md) — bioreactor design for microbial cultures
- [Electrolysis](electrolysis.md) — electrochemical reactor (cell) construction
- [Electrochemical Processes](../electrochemistry/electrochemical-processes.md) — plating and electrolytic reactor design
- [Filter Press](filter-press.md) — reactor product separation by filtration
- [Centrifuge](centrifuge.md) — reactor product separation by centrifugation
- [Crystallizer](crystallizer.md) — crystallization of reactor products
- [Evaporator](evaporator.md) — concentration of reactor products
- [Chemical Recovery](chemical-recovery.md) — recovery and recycling of reactor outputs
- [Acids](acids.md) — acid digestion and synthesis reactors

## Reactor Sizing Example

A 2,000 L batch stirred-tank reactor for a neutralization reaction (acid + base → salt + water, ΔH = −57 kJ/mol):

- **Vessel dimensions**: 1,300 mm inside diameter × 1,500 mm straight side. Total volume: 2,300 L. Working volume (80%): 1,840 L.
- **Wall thickness**: ASME Section VIII, 6 bar design, A516 Gr.70 (S = 138 MPa), E = 0.85. t = (6 × 650) / (138 × 0.85 − 0.6 × 6) = 34 mm + 3 mm corrosion allowance = 37 mm → use 38 mm plate.
- **Jacket**: 50 mm annular gap, 6 mm plate, heating area = π × 1.3 × 1.5 = 6.1 m². Steam at 0.3 MPa (144°C) → U ≈ 350 W/m²·K → heating capacity = 350 × 6.1 × (144 − 60) = 180 kW. Heating time for 1,800 kg water from 20°C to 80°C: 1,800 × 4.18 × 60 / 180 = 2,510 seconds ≈ 42 minutes.
- **Agitator**: Rushton turbine, 450 mm diameter, at 120 RPM. Power: P = Np × ρ × N³ × D⁵ = 5.0 × 1,000 × 2³ × 0.45⁵ = 1.8 kW. Motor: 2.2 kW (1.5 HP) with 15:1 gear reducer.
- **Heat removal for exotherm**: If the reaction releases 500 kJ/L over 1 hour, total heat = 1,840 × 500 = 920 MJ = 256 kW. The jacket can remove 180 kW — additional cooling required (external heat exchanger with circulation loop adding 100 kW capacity).

## Agitator Selection Guide

| Impeller Type | Np (Power No.) | Flow Pattern | Shear Level | Best Application |
|---------------|----------------|--------------|-------------|------------------|
| Rushton turbine (6-blade disc) | 5.0 | Radial | High | Gas dispersion, liquid-liquid mixing |
| Pitched blade turbine (45°) | 1.3 | Axial (downward) | Medium | Solid suspension, blending |
| Hydrofoil (Lightnin A310) | 0.3 | Axial (downward) | Low | Blending, heat transfer |
| Anchor | 0.5 | Tangential | Very low | High-viscosity fluids (>50 Pa·s) |
| Helical ribbon | 1.0 | Tangential + axial | Very low | Very high viscosity (>100 Pa·s) |

Impeller tip speed is the primary mechanical design constraint. For standard steel impellers, the maximum tip speed is 5-8 m/s before vibration and bearing loads become excessive. For glass-lined steel impellers (corrosion-resistant), the maximum is 3-5 m/s due to the brittleness of the glass coating. The relationship between tip speed, diameter, and RPM: v_tip = π × D × N / 60. For a 450 mm Rushton turbine at 120 RPM: v_tip = π × 0.45 × 120 / 60 = 2.8 m/s — well within limits.

---
*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
