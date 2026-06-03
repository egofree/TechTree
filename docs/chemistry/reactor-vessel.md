# Reactor Vessel

> **Node ID**: chemistry.reactor-vessel
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`metals.forming`](../metals/forming.md), [`metals.welding`](../metals/welding.md)
> **Enables**: [`chemistry.fermentation`](fermentation.md), [`chemistry.acids`](acids.md), [`chemistry.alkalis`](alkalis.md), [`chemistry.solvents`](solvents.md)
> **Timeline**: Years 15-30
> **Outputs**: batch_reaction, continuous_reaction
> **Critical**: Yes — reactor vessels are the fundamental unit of chemical manufacturing. Every batch reaction, fermentation, acid digestion, and synthesis requires a contained, controlled environment. No chemical industry operates without them.

## Principle

A reactor vessel is a sealed container designed to hold chemical reactions under controlled conditions of temperature, pressure, agitation, and residence time. The vessel must contain the reaction safely while allowing heat addition or removal, mixing of reactants, sampling, and product discharge. Reactor design is governed by the reaction kinetics (how fast the reaction proceeds), thermodynamics (how much heat is released or absorbed), and the physical properties of the reactants and products (corrosiveness, toxicity, flammability).

Two fundamental reactor types exist: **batch reactors** (fixed volume, reactants charged, reaction proceeds, products discharged) and **continuous reactors** (steady flow of reactants through the vessel, products continuously withdrawn). Batch reactors dominate at smaller scales and for multi-product facilities; continuous reactors (CSTR — continuously stirred tank reactor, or PFR — plug flow reactor) dominate at large scale for single high-volume products.

The vessel shell must withstand the design pressure (internal or external) at the design temperature. For jacketed vessels, the shell also serves as the heat transfer surface. The agitator provides mixing to ensure uniform temperature and composition throughout the vessel volume. Baffles prevent vortexing and improve mixing efficiency.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate](../metals/iron-steel.md) (shell) | 200-2,000 kg | Carbon steel A516 Gr.70, 6-25 mm thick | [Iron & Steel](../metals/iron-steel.md) | Stainless steel 304L/316L (corrosive service) |
| [Steel plate](../metals/iron-steel.md) (jacket) | 100-800 kg | Carbon steel A36, 6-10 mm thick | [Iron & Steel](../metals/iron-steel.md) | Half-pipe coil (less surface area, simpler) |
| [Stainless steel](../metals/iron-steel.md) | 50-500 kg | 316L for corrosive service, internal clad or solid | [Iron & Steel](../metals/iron-steel.md) | Glass-lined steel (for strong acids), titanium (for chlorides) |
| [Steel shaft](../metals/iron-steel.md) (agitator) | 20-100 kg | 1045 or 416 stainless, 40-80 mm diameter | [Iron & Steel](../metals/iron-steel.md) | Alloy 20 shaft (sulfuric acid service) |
| [Electric motor](../energy/electricity.md) | 1 unit | 1-50 kW, 3-phase, 1750 RPM | [Electricity](../energy/electricity.md) | Hydraulic drive (hazardous area) |
| [Gear reducer](../machine-tools/machining.md) | 1 unit | 10:1 to 40:1 ratio, rated for motor torque | [Machining](../machine-tools/machining.md) | V-belt drive (less precise) |
| [Mechanical seal](../polymers/elastomers.md) | 1 unit | Cartridge-type, rated for design pressure and temperature | [Elastomers](../polymers/elastomers.md) | Packed gland (simpler, higher leakage) |
| [Gaskets](../polymers/elastomers.md) | 1 set | PTFE or spiral-wound, matched to flange size | [Elastomers](../polymers/elastomers.md) | Compressed fiber (lower temperature) |
| [Bolts and nuts](../metals/fasteners.md) | 10-50 kg | ASTM A193 B7 or B8, matched to flange class | [Fasteners](../metals/fasteners.md) | — |
| [Welding consumables](../metals/welding.md) | 10-50 kg | E7018 (carbon steel) or E316L-16 (stainless) | [Welding](../metals/welding.md) | — |
| [Thermowell](../measurement/index.md) | 2-4 units | 316L stainless, 150-300 mm immersion | [Measurement](../measurement/index.md) | — |
| [Insulation](../construction/building-materials.md) | 10-50 m² | Mineral wool, 50-100 mm thick, aluminum cladding | [Construction](../construction/building-materials.md) | Calcium silicate (higher temperature) |

## Construction Steps

### Shell Fabrication

1. **Calculate design parameters**: Determine vessel volume (50-10,000 L typical), design pressure (1-20 bar), design temperature (−20°C to 300°C). Calculate minimum wall thickness per ASME Boiler and Pressure Vessel Code Section VIII: t = (P × R) / (S × E − 0.6 × P), where P = design pressure, R = inside radius, S = allowable stress, E = joint efficiency (0.85 for spot-radiographed, 1.0 for fully radiographed).

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

14. **Install baffles**: Weld four baffle plates (width = 1/10 to 1/12 of vessel diameter) to the vessel interior wall, 90° apart, offset 1/6 baffle width from the wall. Baffles prevent solid-body rotation and force turbulent mixing.

15. **Mount mechanical seal**: Install the mechanical seal assembly on the agitator shaft at the top head penetration. The seal contains rotating and stationary faces (carbon vs. silicon carbide or tungsten carbide) pressed together by spring force, preventing process fluid from escaping along the shaft. For corrosive or toxic service, use a double mechanical seal with barrier fluid.

16. **Mount motor and gear reducer**: Bolt the gear reducer flange to the mounting bracket on the vessel top head. Couple the agitator shaft to the gear reducer output shaft via a rigid or flexible coupling. Bolt the motor to the gear reducer input. Align to within 0.05 mm offset and 0.05 mm angularity using dial indicators.

### Final Assembly and Testing

17. **Hydrostatic test vessel**: Fill the vessel with water. Pressurize to 1.5× MAWP (maximum allowable working pressure). Hold 30 minutes. Inspect all welds, nozzles, and flange connections for leaks. Zero leaks acceptable. Record test pressure and duration.

18. **Install pressure relief device**: Mount a pressure relief valve or rupture disc on a dedicated nozzle at the top of the vessel. Set relief pressure to 1.1× MAWP. The relief device must be sized to discharge the full rated flow at set pressure — calculate required orifice area per API 521 for the worst-case overpressure scenario (external fire, runaway reaction, utility failure).

19. **Install insulation**: Apply 50-100 mm mineral wool insulation to the vessel shell and jacket. Cover with 0.5 mm aluminum sheet metal cladding, secured with banding straps. Insulation reduces heat loss, stabilizes temperature, and provides personnel protection (surface temperature <60°C).

20. **Install instruments**: Mount thermowells (2-4 locations: top, middle, bottom, jacket inlet), pressure gauge (0-1.5× design range), and sight glass (for visual level and mixing observation). Connect temperature and pressure instruments to control panel.

## Calibration and Verification

1. **Pressure test verification**: Confirm hydrostatic test at 1.5× MAWP held for 30 minutes with zero pressure drop. All joints soap-tested.

2. **Agitator shaft runout**: Dial-indicate the shaft at the seal area with the shaft rotating by hand. Total indicated runout must be <0.05 mm. If excessive, check shaft straightness and coupling alignment.

3. **Motor current draw**: Run the agitator with the vessel filled with water at the design liquid level. Measure motor current at operating speed. Current should be 40-70% of motor nameplate full-load amps. If >85%, the impeller diameter or speed is too high for the fluid — reduce speed or trim impeller diameter.

4. **Heat transfer verification**: Fill jacket with hot water or steam at design temperature. Measure the rate of temperature rise in a vessel full of water. Calculate actual heat transfer coefficient: U = Q / (A × LMTD), where Q = m × Cp × ΔT/Δt, A = jacket surface area, LMTD = log mean temperature difference. Compare to design value; accept if within ±15%.

5. **Relief valve test**: Verify relief valve lifts at set pressure using a calibrated test stand or by pressurizing the vessel with water to the set point.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Working volume | 50-10,000 L (80% of total volume to allow headspace) |
| Design pressure | 1-20 bar (typical: 6 bar for atmospheric chemical reactors) |
| Design temperature | −20°C to 300°C (depends on shell material and gaskets) |
| Heat transfer area (jacketed) | 2-30 m² (proportional to vessel diameter × jacket height) |
| Overall heat transfer coefficient (jacketed, water-to-water) | 200-500 W/m²·K |
| Agitator power (typical) | 0.5-5 kW/m³ (depends on fluid viscosity and impeller type) |
| Mixing time (low-viscosity, Rushton turbine) | 30-120 seconds to 95% homogeneity |
| Maximum fluid viscosity (Rushton turbine) | 5,000 mPa·s (above this, use anchor or helical ribbon impeller) |
| Vessel diameter-to-height ratio | 1:1 to 1:3 (batch); 1:3 to 1:10 (continuous/tall reactors) |
| Service life (before major inspection) | 10-20 years (carbon steel), 20-30 years (stainless steel, non-corrosive) |

## Safety

- **Pressure vessel failure**: Overpressure can rupture the vessel, releasing energy proportional to the compressed gas volume. At 6 bar internal pressure, a 5,000 L vessel contains enough stored energy to destroy the surrounding structure. Install pressure relief valve at 1.1× MAWP. Never block or plug relief valves. Hydrostatic test at 1.5× MAWP before first use. Periodic inspection every 5 years per API 510.
- **Chemical burns**: Reactors handling acids, bases, and hot process fluids present severe burn hazards. All sample ports and drain valves must have splash guards. Emergency shower and eyewash within 10 seconds travel time. Insulate all hot surfaces to <60°C surface temperature.
- **Agitator entanglement**: The agitator shaft and impeller can entangle clothing, hair, or limbs. Never open a vessel manway with the agitator running. Lock-out/tag-out the motor before vessel entry. Guards on all exposed rotating parts.
- **Runaway reaction**: Exothermic reactions can accelerate uncontrollably if cooling fails. Design emergency cooling (backup water supply, quench system). Install high-temperature and high-pressure alarms with automatic shutdown. Size relief device for worst-case runaway scenario using DIERS methodology.
- **Flammable atmospheres**: Vessels containing flammable liquids must be purged with nitrogen before and after filling. Ground and bond all metal connections. Use explosion-proof motor and instruments (Class 1 Div 1 or 2).

## Variations and Alternatives

- **Glass-lined reactors**: Carbon steel shell lined with vitreous enamel (borosilicate glass, 0.5-1.0 mm thick, fired at 800-900°C). Superior corrosion resistance to mineral acids (HCl, H₂SO₄, HNO₃, H₃PO₄) at temperatures up to 200°C. Used for pharmaceutical, dye, and specialty chemical production. Disadvantage: glass lining chips on mechanical impact — no metal tools or hard objects inside the vessel.
- **Stainless steel reactors**: Solid 316L stainless construction for food, pharmaceutical, and mildly corrosive chemical service. Electropolished internal surface (Ra <0.4 μm) for cleanability. Higher cost than carbon steel but longer life in corrosive service.
- **High-pressure reactors (autoclaves)**: Thick-walled vessels (25-100 mm wall) rated for 50-300 bar. Used for hydrogenation, polymerization, and hydrothermal synthesis. Forged or machined from solid billet rather than rolled plate. Require ASME Section VIII Division 2 design (higher safety factor, more rigorous analysis).
- **Continuous stirred tank reactor (CSTR)**: Same vessel construction as batch, but with continuous feed and product withdrawal. Overflow weir or level-controlled discharge maintains constant liquid level. Residence time = vessel volume / volumetric flow rate. CSTRs are chained in series for higher conversion.
- **Plug flow reactor (PFR)**: Tubular reactor (pipe or tube bundle) with no back-mixing. Higher conversion per unit volume than CSTR for the same reaction. Used for large-volume continuous processes (petroleum cracking, polymerization). Constructed from pipe or tubes, not a vessel.

## See Also

- [Distillation Column](distillation-column.md) — column construction shares pressure vessel principles
- [Heat Exchanger](heat-exchanger.md) — jacket heat transfer design
- [Fermentation](fermentation.md) — bioreactor design for microbial cultures
- [Electrolysis](electrolysis.md) — electrochemical reactor (cell) construction
- [Electrochemical Processes](../electrochemistry/electrochemical-processes.md) — plating and electrolytic reactor design

[← Back to Chemistry](index.md)
