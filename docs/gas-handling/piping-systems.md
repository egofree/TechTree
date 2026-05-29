# Gas Distribution Piping Systems

> **Node ID**: gas-handling.piping-systems
> **Domain**: [Gas Handling](./index.md)
> **Dependencies**: [`gas-handling.basic`](basic.md) (piping, valves), [`metals.iron-steel`](../metals/iron-steel.md) (steel pipe), [`machine-tools.machining`](../machine-tools/machining.md) (precision pipe threading)
> **Enables**: [`photolithography.fab-processes`](../photolithography/fab-processes.md) (fab gas distribution), [`chemistry.dopant-etch-gases`](../chemistry/dopant-etch-gases.md) (specialty gas panels), [`energy.steam-power`](../energy/steam-power.md) (steam distribution)
> **Timeline**: Years 20-40
> **Outputs**: gas_piping, distribution_manifolds, leak_tested_systems
> **Critical**: No — basic piping from gas-handling.basic covers the same function at lower scale

## Problem

Gas distribution piping systems deliver process gases from a central supply (cylinder manifold, bulk tank, or gas generator) to multiple points of use throughout a facility. While [Basic Gas Handling](basic.md) covers individual piping connections and fittings, this capability addresses the system-level design, installation, testing, and commissioning of complete gas distribution networks — from the gas supply room to the process tool connection points.

A semiconductor fab gas distribution system typically spans 10-500 meters of piping per gas species, with 5-30 different gases distributed to 20-200+ tool connection points. Each gas species requires dedicated piping — no mixing of gas types in shared lines. The system must deliver gas at the specified pressure and flow rate, with minimal pressure drop, zero contamination, and no leaks, for 10-30 years of service life with minimal maintenance.

The design process starts with demand analysis (flow rates and pressures at each point of use), proceeds through pipe sizing (balancing pressure drop against cost), material selection (compatibility with the gas and purity requirements), jointing method selection (welded, threaded, or compression), installation, pressure testing, leak testing, purging, and finally commissioning into service.

## Prerequisites

- **Materials**: Carbon steel pipe (ASTM A106 Grade B for steam and inert gases), stainless steel 316L pipe (ASTM A312 for corrosive and high-purity gases), copper tubing (ASTM B68 for water, air, and non-corrosive gases), PTFE or PFA tubing (for laboratory-scale corrosive service)
- **Tools and equipment**: [Machine tools](../machine-tools/index.md) — pipe threading machine, tube bending tools, orbital welding system; [Gas handling](basic.md) — pressure test pumps, helium leak detector, pressure gauges
- **Knowledge**: Fluid mechanics (pressure drop calculations, Reynolds number, Darcy-Weisbach equation), pipe stress analysis, material compatibility with process gases, welding metallurgy
- **Infrastructure**: Pipe fabrication shop (cutting, threading, welding), blast-resistant pressure test area, clean assembly environment (for high-purity systems)

## Bill of Materials

| Material | Quantity (per 100 m run) | Source | Alternatives |
|----------|-------------------------|--------|-------------|
| Carbon steel pipe (Schedule 40, 25 mm NB) | 100 m | [Metals](../metals/index.md) — seamless or ERW | Stainless steel 304L (higher cost, better corrosion resistance) |
| Stainless steel 316L pipe (Schedule 10S, 12.7 mm OD) | 100 m (high-purity gas) | [Metals](../metals/index.md) — seamless, mill-annealed | Electropolished 316L (lowest particle generation, 2-3× cost) |
| Copper tubing (12.7 mm OD, 1 mm wall) | 100 m (non-critical gas) | [Metals](../metals/index.md) — soft annealed | Steel pipe (heavier, harder to form) |
| Compression fittings (Swagelok-type) | 20-40 per 100 m | [Machine tools](../machine-tools/machining.md) — machined from brass or SS316 | Flared fittings (copper only, lower pressure rating) |
| Welded fittings (butt-weld or socket-weld) | 10-30 per 100 m | [Machine tools](../machine-tools/machining.md) — forged or machined | Threaded fittings (lower integrity, limited to <50 bar) |
| Gaskets (PTFE, compressed fiber, copper) | Per flanged joint | [Chemistry](../chemistry/index.md) or [Metals](../metals/index.md) | Spiral-wound gaskets (higher pressure/temperature) |
| Pipe supports (U-bolt, clevis, spring) | 10-20 per 100 m | [Machine tools](../machine-tools/forming.md) — fabricated from steel | Trapeze hangers (multiple pipes on one support) |
| Valves (ball, gate, diaphragm) | 5-15 per 100 m | [Machine tools](../machine-tools/machining.md) | Plug valves (higher torque, less common) |
| Pipe insulation (mineral wool, foam) | 100 m (if required) | [Chemistry](../chemistry/index.md) | Pre-insulated pipe (factory-applied, higher cost) |

## Process Description

## 4.1 System Design

1. **Demand analysis**: For each point of use, determine the required gas flow rate (L/min or m³/h at standard conditions), required delivery pressure (bar or kPa), required gas purity grade, and whether the gas is flammable, toxic, corrosive, or inert. Tabulate all demands in a gas utility schedule.
2. **Pipe sizing**: For each pipe segment, calculate the required inside diameter using the Darcy-Weisbach equation or a simplified gas pipe sizing chart. Target a pressure drop of less than 10% of the supply pressure from source to the farthest point of use. Larger diameter pipe reduces pressure drop but increases material cost. Standard practice: use the smallest pipe diameter that keeps velocity below 10 m/s and pressure drop within budget.
3. **Material selection**: Select pipe material based on gas compatibility. Inert gases (N₂, Ar, He, CO₂, compressed air): carbon steel or copper, standard fittings. Corrosive gases (HCl, Cl₂, H₂S, HF): stainless steel 316L with welded joints. Ultra-high-purity semiconductor gases: electropolished stainless steel 316L with orbital-welded joints and VCR fittings. Oxygen service: steel, copper, or Monel, oxygen-clean. Fuel gases (H₂, CH₄): steel or stainless steel. Acetylene: steel only (never copper alloys).
4. **Layout design**: Route piping to minimize length, avoid dead legs, provide isolation valves at each branch, and include drain points at all low spots. Route through pipe chases or utility corridors, not through occupied spaces (for toxic and flammable gases). Include expansion loops or bellows for long straight runs subject to thermal cycling.

**Strengths:**
- Darcy-Weisbach-based pipe sizing with 10% pressure drop budget provides predictable, quantifiable performance from source to farthest point of use
- Material selection scheme (carbon steel for inert, 316L for corrosive, EP 316L for UHP) matches cost to purity requirement

**Weaknesses:**
- Each gas species requires dedicated piping — a fab with 20 gases needs 20 independent distribution networks, multiplying installation cost
- Dead legs and low spots are inevitable in complex routing — they trap stagnant gas and condensate, requiring drain points and careful slope design

## 4.2 Pipe Fabrication and Installation

1. **Cutting**: Cut pipe to length with a pipe cutter (rotary cutting wheel for copper and thin-wall steel) or a band saw (for thick-wall steel). Deburr the cut end inside and out — burrs create turbulence, restrict flow, and generate particles. For stainless steel, use a dedicated cutting tool (not one previously used on carbon steel) to prevent iron contamination of the stainless surface (free iron particles rust and contaminate the gas stream).
2. **Jointing — threaded connections (carbon steel, <50 bar)**: Cut external threads on the pipe end with a pipe threading machine (dies cut tapered NPT threads, 1:16 taper). Apply PTFE tape (2-3 wraps clockwise looking at the threaded end) or pipe thread sealant to the male threads. Thread the fitting onto the pipe and tighten 1-2 turns past hand-tight. NPT threads seal by deformation — do not overtighten or the fitting may crack. Maximum reliable pressure: ~20 bar for steel, ~10 bar for brass. NPT is not acceptable for toxic gas service or semiconductor-grade gas distribution.
3. **Jointing — socket weld (steel and stainless steel, <200 bar)**: Fit the pipe into the socket of the fitting with a 1.5 mm gap at the bottom of the socket (thermal expansion clearance). Tack weld at two points 180° apart. Complete the fillet weld around the full circumference using TIG (GTAW) for stainless steel or arc welding (SMAW) for carbon steel. Socket welds provide a smooth internal bore (no crevice for contamination) and are the standard joint for chemical process piping.
4. **Jointing — butt weld (high-purity stainless steel, all pressures)**: Bevel both pipe ends to 30-37.5° (single-V preparation). Align the two ends with a tolerance of ±0.5 mm maximum offset. Tack weld at 3-4 points. Complete the root pass (first weld layer) using TIG with an argon purge on the inside of the pipe to prevent oxidation (sugar — black oxide scale — on the inside of a weld is unacceptable for high-purity gas service). Fill and cap passes complete the joint. 100% radiographic inspection for toxic gas and high-purity systems.
5. **Jointing — orbital welding (semiconductor-grade, automated)**: Use a computer-controlled orbital weld head that rotates the TIG torch around the joint circumference. Program the weld current, rotation speed, and pulse parameters for each joint. The automated process produces repeatable, high-quality welds with consistent penetration and internal bead profile. Essential for electropolished stainless steel gas distribution systems where manual weld quality is inconsistent. Each weld is documented with a weld log recording the joint number, weld parameters, and operator.
6. **Jointing — compression fittings (tubing, <100 bar)**: For stainless steel or copper tubing with compression fittings, fully insert the tube into the fitting body. Tighten the nut by hand until resistance is felt, then tighten with wrenches the specified number of turns past finger-tight (typically 1-1/4 turns for new stainless steel fittings). The front ferrule bites into the tube surface, creating a metal-to-metal seal. Do not mix ferrules from different manufacturers.

**Strengths:**
- Orbital welding produces repeatable, documented welds with consistent internal bead profile — essential for electropolished UHP systems where manual weld quality is inconsistent
- Compression fittings are removable and re-sealable, allowing system modification without cutting and rewelding

**Weaknesses:**
- NPT threaded connections are limited to ~20 bar (steel) and are not acceptable for toxic gas or semiconductor-grade service — seal quality depends on PTFE tape installation technique
- Butt weld root pass requires argon purge on the pipe inside to prevent oxidation ("sugar") — missed purge produces black oxide that contaminates the gas stream

## 4.3 Pressure Testing

1. **Hydrostatic test**: After installation and before insulation, pressure-test the completed piping system with water at 1.5× the maximum allowable working pressure (MAWP). Fill the system with water from the lowest point, venting air from the highest point (air pockets compress during testing and mask leaks). Hold test pressure for 30 minutes minimum. Inspect all joints visually for leaks (wipe joints with a dry cloth and check for moisture). Any leak requires draining, repair, and retest.
2. **Pneumatic test (when hydrostatic is impractical)**: If the system cannot be dried after water exposure (e.g., instrument air, high-purity gas), test with nitrogen or dry air at 1.1× MAWP. This is less safe than hydrostatic testing — a pneumatic failure releases stored energy. Exclude personnel from the test area during pressurization. Use soap solution or ultrasonic leak detector to find leaks.
3. **Leak testing (sensitivity verification)**: For flammable and toxic gas systems, perform a helium leak test after pressure testing. Pressurize the system with a helium-nitrogen mixture (5-10% He, balance N₂) to operating pressure. Scan all joints with a helium sniffer probe (sensitivity ~10⁻⁶ atm·cc/s). For semiconductor-grade systems, use a vacuum helium leak test: evacuate the piping and spray helium on the exterior; detect He entering through leaks with a mass spectrometer leak detector (sensitivity ~10⁻¹⁰ atm·cc/s). Document all leak test results. Zero detected leaks is the acceptance criterion.

**Strengths:**
- Hydrostatic testing with water at 1.5× MAWP is inherently safe — water is incompressible, so a failure releases minimal stored energy
- Vacuum helium leak testing at 10⁻¹⁰ atm·cc/s sensitivity finds leaks invisible to soap bubble or pressure decay methods — essential for toxic gas systems

**Weaknesses:**
- Pneumatic testing at 1.1× MAWP stores enormous energy — a 100 m run of 25 mm pipe at 200 bar contains ~10 MJ, equivalent to 2.4 kg TNT
- Hydrostatic testing leaves residual moisture requiring dry nitrogen purge before introducing moisture-sensitive gases

## 4.4 Purging and Commissioning

1. **Degreasing**: Before introducing process gas, degrease the piping system if oil or grease may be present from fabrication. Fill the system with a degreasing solvent (trisodium phosphate solution, or commercial degreaser) and circulate for 30 minutes. Drain and flush with clean water. Blow dry with oil-free nitrogen.
2. **Inert gas purge**: Connect a nitrogen source to one end of the piping system and open the far end to atmosphere. Flow nitrogen through the system at a rate that achieves 3-5 volume changes (one volume change = flowing a volume of nitrogen equal to the internal volume of the piping). For a 100 m run of 25 mm ID pipe (internal volume ~49 L), flow nitrogen at 50 L/min for 5 minutes (≈5 volume changes). Verify O₂ content at the outlet with an oxygen monitor — must be below 1% before introducing flammable gas, or below 100 ppm for high-purity inert gas service.
3. **Pressure stabilization**: Pressurize the system to operating pressure with the process gas. Monitor pressure for 24 hours — any pressure drop indicates a leak. For toxic and flammable gas systems, zero pressure drop over 24 hours is required before the system is placed in service.

**Strengths:**
- Inert gas purge with 3-5 volume changes reduces O₂ to below 1% with simple, predictable dilution physics
- 24-hour pressure stabilization test provides definitive leak verification — any pressure drop over a full diurnal temperature cycle indicates a real leak

**Weaknesses:**
- Degreasing with trisodium phosphate solution leaves moisture that must be completely dried before introducing reactive gases — incomplete drying creates contamination
- Purge verification requires a calibrated O₂ monitor at the outlet — without measurement, the actual O₂ concentration is unknown

## Quantitative Parameters

## Pipe Sizing — Maximum Flow Rates for Gas Service (m³/h at STP)

| Nominal Bore | Schedule 40 Steel | Max Velocity 10 m/s | Pressure Drop per 100 m at 7 bar |
|--------------|-------------------|---------------------|----------------------------------|
| 15 mm (1/2") | 21.3 mm OD, 1.73 mm wall | 6 m³/h | 0.08 bar |
| 20 mm (3/4") | 26.7 mm OD, 2.11 mm wall | 12 m³/h | 0.06 bar |
| 25 mm (1") | 33.4 mm OD, 2.77 mm wall | 20 m³/h | 0.05 bar |
| 32 mm (1-1/4") | 42.2 mm OD, 2.77 mm wall | 35 m³/h | 0.03 bar |
| 40 mm (1-1/2") | 48.3 mm OD, 3.18 mm wall | 50 m³/h | 0.03 bar |
| 50 mm (2") | 60.3 mm OD, 3.56 mm wall | 85 m³/h | 0.02 bar |
| 80 mm (3") | 88.9 mm OD, 4.78 mm wall | 190 m³/h | 0.01 bar |
| 100 mm (4") | 114.3 mm OD, 5.49 mm wall | 320 m³/h | 0.01 bar |

## Pressure Ratings by Material and Joint Type

| Material | Joint Type | Max Working Pressure | Max Temperature | Typical Service |
|----------|-----------|---------------------|-----------------|-----------------|
| Carbon steel (SCH 40) | Welded | 100-150 bar | 400°C | Steam, compressed air, inert gas |
| Carbon steel (SCH 40) | Threaded NPT | 15-20 bar | 200°C | Utility air, non-critical gas |
| Stainless steel 316L (SCH 10S) | Butt weld | 50-100 bar | 300°C | Corrosive gas, high-purity gas |
| Stainless steel 316L (SCH 10S) | Orbital weld | 50-100 bar | 300°C | Semiconductor-grade gas |
| Copper (12.7 mm OD, 1 mm wall) | Compression | 20-50 bar | 200°C | Water, air, non-corrosive gas |
| Copper (12.7 mm OD, 1 mm wall) | Brazed | 20-50 bar | 200°C | Refrigeration, water |
| PTFE tubing (6 mm OD) | Compression | 3-5 bar | 200°C | Laboratory corrosive gas |

## Scaling Notes

- **Laboratory scale**: 6-12 mm OD tubing with compression fittings, routed along bench walls. Manual valve isolation. Single gas source (cylinder) to 1-3 points of use. Total system volume <1 L. Leak test with soap solution. Install in 1-2 days.
- **Pilot plant scale**: 15-25 mm NB steel or stainless pipe, threaded or socket-welded. Gas supply from cylinder manifold or small bulk tank to 5-20 points of use. Total system volume 5-50 L. Hydrostatic test and helium leak test. Install in 1-2 weeks.
- **Semiconductor fab scale**: 12.7-25 mm OD electropolished stainless steel 316L tubing, orbital-welded with VCR fittings at connection points. 5-30 gas species, each with dedicated piping. Automatic switchover manifolds at the gas source. 20-200+ tool connection points. Total installed pipe length: 1-50 km across all gas species. Vacuum helium leak test every joint. Install over 3-12 months. Gas panel design (mini-manifolds at each tool) is a specialty skill requiring 6-12 months of training.
- **Scale bottleneck**: Weld quality control at fab scale. Manual TIG welding cannot consistently produce the internal bead quality required for electropolished high-purity systems. Orbital welding machines are essential. Each weld requires documentation, visual inspection (borescope of internal bead), and periodic radiographic or ultrasonic examination.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Excessive pressure drop at point of use | Pipe undersized for flow rate; fouling or debris in pipe; partially closed valve | Calculate actual flow vs. design flow. If flow exceeds design, upsize pipe. Check for closed or partially open valves. Inspect for internal fouling (scale, corrosion products). |
| Leak at threaded joint | Insufficient thread sealant, overtightened (cracked fitting), or thermal cycling loosened joint | Cut out threaded joint and replace with welded fitting. Threaded joints are not reliable for long-term high-purity or toxic gas service. |
| Leak at compression fitting | Incomplete tube insertion, mixed ferrule brands, or insufficient tightening | Disassemble. Verify tube is fully inserted (depth mark on tube). Verify ferrules match the fitting brand. Reassemble and tighten to specification. Replace ferrules if previously seated on a different tube. |
| Internal corrosion products contaminating gas stream | Carbon steel pipe in corrosive gas service, or moisture in normally dry system | Replace pipe with corrosion-resistant material (stainless steel 316L for corrosive gases). Install a moisture indicator and adsorbent dryer upstream. |
| Weld leak detected during pressure test | Porosity, incomplete penetration, or cracking in weld | Grind out the defective weld. Reweld using proper procedure (preheat if required for the material). Retest. If the system requires 100% radiographic inspection, rewelded joints must pass reinspection. |
| Water hammer or liquid slugging | Condensate accumulating in low spots, then propelled by gas flow | Install drain points (drip legs with automatic drain valves) at all low spots. Verify slope of horizontal piping (minimum 1:200 slope toward drain points). |
| Gas cross-contamination | Cross-connected piping, or shared purge line between incompatible gases | Verify piping is dedicated per gas species (no shared lines for incompatible gases). Eliminate cross-connections. Install check valves to prevent backflow. Label all piping at regular intervals. |

## Safety

**Confined space entry during installation**: Pipe trenches, utility tunnels, and crawl spaces where gas piping is routed may contain hazardous atmospheres (low O₂ from nitrogen purging, accumulated heavier-than-air gases like propane or CO₂). Test atmosphere with a calibrated four-gas monitor (O₂, LEL, CO, H₂S) before entry. Use supplied-air respirator if gas contamination is possible. Never enter a confined space alone — always have an attendant at the entry point.

**Hot work hazards during welding**: Welding and cutting on installed piping requires a hot work permit and fire watch. Sparks from welding can ignite flammable gas residues in nearby piping or combustible materials. Verify that all piping in the vicinity has been purged with nitrogen and tested for combustible gas (<1% LEL) before welding. Post a fire watch with a fire extinguisher for 30 minutes after hot work completion.

**High-pressure stored energy**: A 100 m run of 25 mm ID pipe at 200 bar contains approximately 10 MJ of stored energy — equivalent to 2.4 kg of TNT. A catastrophic failure of a high-pressure piping system creates a blast wave, shrapnel from pipe fragments, and a rapid gas release that can displace oxygen in enclosed spaces. Mitigation: install pressure relief valves at all high-pressure sources, limit the volume of high-pressure piping, and blast-shield critical sections.

**Toxic gas piping safety**: Piping carrying toxic gases (CO, H₂S, Cl₂, PH₃, AsH₃, SiH₄) must be contained within ventilated enclosures (pipe chase with continuous exhaust at 1 m³/min per meter of pipe chase length). Leak detection interlocks automatically close source valves and alarm upon detection. All joints in toxic gas piping must be welded or use metal-gasketed fittings — no threaded connections. Access panels for maintenance must have local exhaust capture to prevent gas release into occupied spaces when the panel is opened.

**Oxygen piping fire risk**: Oxygen at high pressure lowers the autoignition temperature of organic materials. A greasy fingerprint inside an oxygen pipe can ignite at 30-40 bar. All oxygen piping must be oxygen-cleaned before installation (degreased with hot alkaline wash, rinsed with deionized water, blown dry with oil-free nitrogen). Inspect with UV light for hydrocarbon residues (fluoresce under UV). Valves for oxygen service must be cleaned and labeled "OXYGEN" — never use a valve previously in hydrocarbon service on an oxygen line.

## Quality Control

**Weld inspection**: Visual inspection of every weld (external and internal via borescope). Acceptance: full penetration, no porosity visible at 10× magnification, no undercut deeper than 0.8 mm, no cracks. For high-purity systems: 100% radiographic inspection of butt welds. For toxic gas systems: 100% radiographic or ultrasonic examination. For utility systems: 10-20% spot radiography.

**Pressure test documentation**: Record test medium (water or nitrogen), test pressure, hold time, and pass/fail result for each piping section. Test certificates signed by the testing technician and reviewed by the responsible engineer.

**Leak test records**: Document every joint tested, the leak test method, sensitivity achieved, and pass/fail result. For semiconductor-grade systems: each orbital weld has a unique identification number, weld parameters logged by the orbital weld controller, and a weld map showing the physical location of every joint.

**Material traceability**: Maintain a material test report (MTR) for every length of pipe and every fitting installed in the system. The MTR documents heat number, material grade, chemical composition, and mechanical test results. This traceability is mandatory for pressure piping codes (ASME B31.3) and is critical for investigating failures.

**Flushing and cleanliness verification**: After pressure testing and before purging, flush the system with filtered nitrogen (0.2 μm particulate filter). Measure particulate concentration at the outlet with an online particle counter. Acceptance: <100 particles ≥0.2 μm per cubic foot for semiconductor-grade systems. For utility systems: blow down with compressed air until a white cloth held at the outlet shows no visible discoloration.

## Variations and Alternatives

| Piping System Type | Material | Joint Method | Best For | Cost (per meter installed) |
|-------------------|----------|-------------|----------|---------------------------|
| Utility gas distribution | Carbon steel SCH 40 | Threaded or socket weld | Compressed air, N₂, general inert gas | $30-80/m |
| Chemical process piping | Stainless steel 316L SCH 10S | Butt weld or socket weld | Corrosive gases, process chemicals | $80-200/m |
| High-purity semiconductor gas | EP SS316L, 12.7 mm OD tubing | Orbital weld + VCR fittings | Semiconductor fab process gases | $200-800/m |
| Laboratory gas distribution | Copper tubing 6-12 mm | Compression fittings | Bench-scale gas delivery | $15-50/m |
| High-pressure gas (200+ bar) | Alloy steel, thick wall | Butt weld, RTJ flanges | Gas cylinder filling, hydrostatic test | $100-300/m |
| Flexible connections | PTFE or PFA hose | Compression or flanged | Short flexible runs, equipment connections | $50-150/m |

**Double-containment piping**: For toxic and highly hazardous gases, install the process pipe inside a secondary containment pipe. The annular space between the two pipes is monitored for leaks (pressure or vacuum monitoring). If the inner pipe leaks, the outer pipe contains the release. The leak detection system alarms and automatically closes the gas source. Double-containment piping is mandatory for semiconductor fab distribution of arsine (AsH₃), phosphine (PH₃), and other immediately dangerous to life and health (IDLH) gases.

**Modular gas panels**: Instead of field-fabricated piping runs, factory-assembled gas panels (also called gas boxes or valve manifold boxes, VMBs) provide a pre-tested, pre-leak-checked gas distribution module. Each panel serves one or a few process tools and includes isolation valves, pressure regulators, flash-back arrestors (for flammable gases), purge valves, and exhaust connections. Factory assembly in a clean environment produces higher-quality systems faster than field fabrication. Install the panel as a module, connect the inlet gas supply and outlet to the tool, leak-test the field connections, and commission.

## Pipe Support Spacing and Thermal Expansion

Steel and stainless steel piping expands approximately 12 mm per 10 m per 100°C temperature rise. For a 100 m steam line operating at 200°C above ambient, total expansion is 240 mm. This expansion must be accommodated by expansion loops, bellows, or flexible connections.

| Pipe Size (NB) | Maximum Support Spacing (m) — Water | Maximum Support Spacing (m) — Gas | Maximum Support Spacing (m) — Steam |
|-----------------|-------------------------------------|-----------------------------------|------------------------------------|
| 15 mm (1/2") | 1.5 | 2.0 | 1.8 |
| 20 mm (3/4") | 1.8 | 2.3 | 2.0 |
| 25 mm (1") | 2.0 | 2.5 | 2.3 |
| 32 mm (1-1/4") | 2.3 | 3.0 | 2.5 |
| 40 mm (1-1/2") | 2.5 | 3.3 | 2.8 |
| 50 mm (2") | 3.0 | 3.8 | 3.3 |
| 80 mm (3") | 3.8 | 4.8 | 4.0 |
| 100 mm (4") | 4.5 | 5.5 | 4.8 |

## Piping System Labeling Requirements

Every gas piping system must be labeled at regular intervals and at each valve, branch, and penetration point. Labels identify:
- Gas name and chemical formula (e.g., "NITROGEN — N₂")
- Normal operating pressure (e.g., "7 BAR")
- Direction of flow arrow
- Hazard class color band (yellow for flammable, green for oxidizer, blue for inert, red for toxic)

Label spacing: at minimum every 6 m on straight runs, at each room entry/exit, at each valve, and at each branch connection. Labels must be legible from 1 m distance. Use engraved plastic or stamped metal tags secured with wire or adhesive. Piping labels are the primary means of preventing accidental cross-connection during maintenance.

## Commissioning Checklist for Gas Piping Systems

1. Verify all pipe material certificates (MTRs) match design specification
2. Verify all weld inspection reports (radiographic or visual) are approved
3. Complete hydrostatic pressure test — record test pressure, hold time, result
4. Complete pneumatic leak test (if hydrostatic impractical) — record sensitivity
5. Perform helium leak test (for toxic/flammable/high-purity systems)
6. Flush system with filtered nitrogen — verify particulate count at outlet
7. Purge system to below 1% O₂ — verify with calibrated O₂ monitor
8. Pressurize to operating pressure with process gas — hold 24 hours, verify zero pressure drop
9. Verify all labels and identification tags are installed
10. Issue commissioning certificate with test records attached

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Pressure drop higher than calculated | Undersized pipe or restricted flow at fitting | Verify pipe diameter matches design; check for debris or weld protrusion inside joints; recalculate with actual fitting count |
| Leak at welded joint | Incomplete weld penetration or weld porosity | Cut out and reweld; verify orbital weld parameters (amperage, rotation speed, purge gas); X-ray inspect critical joints |
| Particulate contamination at outlet | Weld slag, debris from construction, or dirty gas | Install point-of-use filter; flush system with filtered N₂; verify gas source purity |
| Cross-contamination between gas species | Improper isolation or shared vent lines | Verify double-block-and-bleed valves between incompatible gases; separate vent lines for corrosive vs inert gases |
| Valve packing leak (external) | Packing gland loose or packing material degraded | Tighten packing gland nut; if persistent, repack with compatible material (PTFE for corrosives, graphite for high temp) |
| Pressure instability at tool connection | Regulator hunting or inadequate buffer volume | Add surge tank near point of use; verify regulator sizing; check for upstream pressure fluctuations |

## See Also

- [Basic Gas Handling](basic.md) — pipe fitting techniques, gasket selection, and material compatibility
- [Vacuum Technology](vacuum.md) — vacuum piping conductance and sealing techniques
- [TIG Welding](../machine-tools/joining.md) — orbital welding procedures for stainless steel tubing
- [Iron & Steel Production](../metals/iron-steel.md) — steel pipe material grades
- [Dopant & Etch Gases](../chemistry/dopant-etch-gases.md) — toxic gas panel design and exhaust abatement
- [Gas Purification](gas-purification.md) — gas purification upstream of distribution piping

[← Back to Gas Handling](index.md)
