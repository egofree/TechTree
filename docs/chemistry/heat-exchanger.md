# Heat Exchanger

> **Node ID**: chemistry.heat-exchanger
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: None
> **Enables**: None
> **Timeline**: Years 15-25
> **Outputs**: heat_transfer
> **Critical**: No — heat exchangers improve energy efficiency and process control but simpler alternatives (direct-fired heating, air cooling) can substitute at lower efficiency

## Overview

A heat exchanger transfers thermal energy between two fluid streams at different temperatures without allowing the fluids to mix. A solid wall (metal tube or plate) separates the hot and cold fluids; heat flows through the wall by conduction. The rate of heat transfer is governed by Q = U × A × LMTD, where Q is heat duty (W), U is the overall heat transfer coefficient (W/m²·K), A is the heat transfer surface area (m²), and LMTD is the log mean temperature difference (K) between the two streams.

Three principal configurations dominate industrial practice: **shell-and-tube** (one fluid inside a bundle of tubes, the other fluid in the surrounding shell — handles pressures to 300 bar and temperatures to 600°C), **plate** (fluids flow between alternating corrugated plates — higher heat transfer coefficients of 3,000-7,000 W/m²·K in a compact footprint, but limited to <25 bar and <200°C), and **double-pipe** (one pipe inside another — the simplest design, used for small heat duties and high-pressure streams). Shell-and-tube exchangers account for approximately 70% of all industrial heat exchanger installations.

Heat exchangers appear in every chemical process: condensers and reboilers on [distillation columns](distillation-column.md), heating and cooling jackets on [reactor vessels](reactor-vessel.md), feed preheaters, product coolers, and waste heat recovery units. Properly designed heat integration (using hot process streams to heat cold ones) reduces a plant's energy consumption by 30-50%. The LMTD (log mean temperature difference) is the driving force for heat transfer — counter-current flow maximizes LMTD, while co-current flow reduces it. For this reason, most industrial exchangers use counter-current or multi-pass cross-flow arrangements.

Fouling is the primary operational challenge for heat exchangers. All real fluids deposit some material on the heat transfer surface: mineral scale (CaCO₃, CaSO₄) from hard water, biological growth in cooling water, polymer deposits from organic processes, and corrosion products from the piping. Fouling adds a thermal resistance that reduces the overall heat transfer coefficient. Design practice adds a fouling factor (Rf) to the clean U value: 1/U_dirty = 1/U_clean + Rf. Typical fouling factors range from 0.0001 m²·K/W for clean fluids to 0.001 m²·K/W for dirty or polymerizing fluids.

The overall heat transfer coefficient U depends on the convective heat transfer coefficients on both sides (h_hot and h_cold), the thermal conductivity of the wall (k), and the wall thickness (t): 1/U = 1/h_hot + t/k + 1/h_cold + Rf. The limiting side is the one with the lowest h value. For gas-to-liquid exchangers, the gas side (h = 30-100 W/m²·K) dominates. For liquid-to-liquid, both sides contribute (h = 1,000-5,000 W/m²·K). Fins on the limiting side increase the effective area and partially compensate for low h values.

Counter-current flow gives the highest LMTD and is the default arrangement. Co-current (parallel) flow has a lower LMTD but is sometimes used when the cold-side outlet temperature must be limited (e.g., to prevent thermal degradation). In shell-and-tube exchangers with multiple tube passes, the flow pattern is a mix of counter-current and co-current, requiring an LMTD correction factor (F). When F < 0.8, redesign with more passes or a pure counter-current arrangement.

## Prerequisites

- **[Tube and pipe fabrication](../metals/forming.md)**: Heat exchanger tubes, pipe cutting, and bending
- **[Welding](../machine-tools/welding-equipment.md)**: Shell longitudinal seams, nozzle welds, tube-to-tubesheet joints
- **[Steel plate](../metals/iron-steel.md)**: Carbon steel A516 Gr.70 for shells, 316L stainless for corrosive service
- **[Gaskets](../polymers/rubber.md)**: EPDM, NBR, PTFE, or Viton depending on temperature and fluid

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel pipe](../metals/forming.md) (tubes) | 50-500 kg | 316L SS or carbon steel, 19-25 mm OD, 1.5-2.5 mm wall | [Forming](../metals/forming.md) | Copper-nickel (seawater), titanium (highly corrosive) |
| [Steel plate](../metals/iron-steel.md) (shell) | 100-500 kg | Carbon steel A516 Gr.70, 6-12 mm thick | [Iron & Steel](../metals/iron-steel.md) | Stainless steel (corrosive shell-side fluid) |
| [Steel plate](../metals/iron-steel.md) (tubesheets) | 20-100 kg | Forged or rolled, 25-50 mm thick | [Iron & Steel](../metals/iron-steel.md) | Clad tubesheet (carbon steel + stainless cladding) |
| [Steel plate](../metals/iron-steel.md) (baffles) | 10-50 kg | Carbon steel or stainless, 3-6 mm thick | [Iron & Steel](../metals/iron-steel.md) | — |
| [Stainless steel plates](../metals/iron-steel.md) | 50-200 kg | 316L, 0.5-1.0 mm thick, corrugated (plate type only) | [Iron & Steel](../metals/iron-steel.md) | Titanium plates (seawater desalination) |
| [Gaskets](../polymers/rubber.md) | 1 set | EPDM or NBR (plate type); PTFE (shell-and-tube flanges) | [Elastomers](../polymers/rubber.md) | Viton (high temperature) |
| [Welding consumables](../machine-tools/welding-equipment.md) | 5-30 kg | E7018 (CS) or E316L-16 (SS) | [Welding](../machine-tools/welding-equipment.md) | — |
| [Bolts](../metals/steelmaking.md) | 10-50 kg | ASTM A193 B7/B8 | [Fasteners](../metals/steelmaking.md) | — |

## Process Description

### Shell-and-Tube Heat Exchanger

1. **Design the exchanger**: Determine heat duty (Q), hot and cold stream flow rates, inlet and outlet temperatures, and allowable pressure drop. Calculate LMTD for counter-current or cross-flow arrangement. Select tube size (19 mm OD is standard), tube length (2-6 m), number of tube passes (1, 2, or 4), and shell diameter. Calculate required heat transfer area: A = Q / (U × LMTD). Number of tubes = A / (π × OD × L). Typical U values: 300-800 W/m²·K for liquid-liquid, 800-1,500 W/m²·K for condensing vapor-liquid, 30-300 W/m²·K for gas-gas. The LMTD correction factor (F) accounts for non-counter-current flow: F = 0.8-0.95 for well-designed multi-pass exchangers.

2. **Drill tubesheets**: Cut two circular tubesheets (25-50 mm thick) from forged steel plate. Mark and drill tube holes on triangular or square pitch (pitch = 1.25-1.5 × tube OD). Hole diameter = tube OD + 0.2-0.4 mm for roller expansion. For a 500 mm shell diameter with 19 mm tubes on 25 mm triangular pitch: approximately 150-200 tube holes. Each hole must be smooth (reamed finish) and free of burrs to ensure a tight tube joint.

3. **Prepare tubes**: Cut heat exchanger tubes to design length (2-6 m). Deburr both ends. Inspect each tube for defects (eddy current testing or visual). 316L stainless tubes for corrosive service; carbon steel for non-corrosive service (water, steam, hydrocarbons).

4. **Assemble tube bundle**: Insert tubes through both tubesheets. Expand (roll) each tube into the tubesheet holes using a mechanical tube expander: insert the expander mandrel, rotate to expand the tube wall outward into firm contact with the tubesheet bore. Roller expansion creates a pressure-tight joint without welding. For higher-pressure service (>20 bar), weld each tube to the front tubesheet (tube-to-tubesheet weld) using orbital TIG welding.

5. **Install baffles**: Cut semicircular baffles (segmental type, 3-6 mm thick, cutout = 20-35% of shell diameter) from steel plate. Slide baffles onto the tubes at regular intervals (baffle spacing = 0.2-1.0 × shell diameter). Baffles support the tube bundle, prevent tube vibration, and direct shell-side fluid to flow across the tubes (cross-flow) rather than along them. Secure baffles with tie rods and spacer sleeves. Baffle spacing determines shell-side velocity and pressure drop: closer spacing = higher velocity = better heat transfer but higher pressure drop.

6. **Fabricate shell**: Roll a cylindrical shell from steel plate. Weld the longitudinal seam. Cut openings for shell-side inlet and outlet nozzles. The shell inside diameter must be 3-6 mm larger than the outer tube limit (OTL — the circle circumscribing all tubes) for bundle insertion.

7. **Assemble exchanger**: Slide the completed tube bundle (tubesheets + tubes + baffles) into the shell. Bolt the front and rear heads (channel covers) to the tubesheets with gaskets. The front head directs tube-side fluid into the tubes; the rear head collects tube-side fluid and may provide a return path for multi-pass arrangements. Install a floating head (U-tube or packed gland) on one end to accommodate differential thermal expansion between tubes and shell.

  8. **Hydrostatic test**: Fill the shell side with water. Pressurize to 1.5× design pressure. Hold 30 minutes. Inspect all tube-to-tubesheet joints for leaks (weeping). Zero leaks acceptable. Repeat for the tube side. If tubes leak at the roller-expanded joint, re-roll or weld.

  **Strengths:**
  - Widest operating range of any heat exchanger type — pressures to 300 bar, temperatures to 600°C
  - Mechanical cleaning of tube interiors with rotating brushes or high-pressure water jets
  - Tube failures are isolated — individual tubes can be plugged (up to 10%) without replacing the unit
  - Standardized design (TEMA classes R, B, C) with extensive manufacturer and engineering data

  **Weaknesses:**
  - Largest physical footprint per unit of heat transfer area — 3-5× larger than plate type
  - Shell-side cleaning requires tube bundle removal — heavy and difficult for large exchangers (>500 kg)
  - Shell-side flow maldistribution and bypass streams reduce effective heat transfer by 10-30%
  - Typical approach temperature limited to 5-15°C — cannot match plate-type 1-3°C approach

### Plate Heat Exchanger

9. **Fabricate plates**: Stamp or press corrugated plates (316L stainless, 0.5-1.0 mm thick) in a chevron or washboard pattern. Corrugation depth 2-5 mm, creating turbulent flow channels when plates are stacked. Punch inlet and outlet port holes at the four corners of each plate. The corrugation pattern creates turbulence at Reynolds numbers as low as 100-400, ensuring high heat transfer coefficients even at low flow rates.

10. **Install gaskets**: Bond EPDM or NBR gaskets into the peripheral groove on each plate. Gaskets seal the plate edges and port holes, directing the two fluids into alternate channels. The gasket pattern alternates between plates to separate hot and cold streams. Select gasket material by operating temperature: EPDM for water and dilute chemicals up to 160°C; NBR for oils up to 130°C; Viton for aggressive chemicals up to 200°C; PTFE encapsulated for steam.

11. **Stack plates**: Stack 20-200 plates between two thick end plates (carbon steel, 15-25 mm). Align port holes. Insert alignment guide pins. Each pair of adjacent plates creates a flow channel — one for the hot fluid, one for the cold, in alternating sequence.

12. **Compress stack**: Tighten tie rods to compress the plate pack. The compression force squeezes the gaskets to form tight seals. Measure the compressed pack dimension — it must match the design value within ±2 mm. Over-compression damages gaskets; under-compression causes leaks.

  13. **Pressure test**: Pressurize each fluid channel separately with water at 1.5× design pressure. Inspect for cross-leakage between channels (indicates damaged gasket or plate). Zero cross-contamination acceptable.

  **Strengths:**
  - Highest heat transfer coefficient of common types (3,000-7,000 W/m²·K) — most compact design
  - Achieves 1-3°C approach temperature — best for heat recovery applications with small driving force
  - Easy to inspect and clean — open the stack and clean every plate in minutes
  - Capacity easily adjusted — add or remove plates without changing the frame

  **Weaknesses:**
  - Limited to <25 bar and <200°C — gasket material constrains both pressure and temperature
  - Narrow channels (2-5 mm gap between plates) plug with fibrous or particulate fouling
  - Gaskets are consumable — replacement every 2-5 years, requiring full disassembly
  - Cannot handle highly viscous fluids (>500 mPa·s) — pressure drop becomes excessive in narrow channels

### Double-Pipe Heat Exchanger

14. **Assemble concentric pipes**: Select an inner pipe (25-50 mm OD) and an outer pipe (75-150 mm OD). The inner pipe carries one fluid; the annular space between the pipes carries the other. Weld or thread the inner pipe to the end fittings with return bends. The outer pipe has inlet and outlet nozzles for the annular fluid. Double-pipe exchangers are the simplest shell-and-tube variant — no tubesheet, no baffles. Maximum area per unit: 1-10 m². Used for small heat duties, high-pressure streams, and as building blocks for multi-unit hairpin exchangers. The inner pipe can be finned (longitudinal fins, 20-30 fins per pipe) to increase the effective heat transfer area on the annular side by 3-10×.

  15. **Connect in series or parallel**: For larger duties, connect multiple double-pipe units in series (both fluids) or in parallel (one fluid split across units). Series connection increases effective length; parallel connection increases effective area. Hairpin exchangers (U-shaped double-pipe units with a 180° return bend) stack vertically to save floor space. A bank of 10 hairpin units provides up to 100 m² of heat transfer area in a compact footprint.

  **Strengths:**
  - Simplest heat exchanger to fabricate — concentric pipes with end fittings, no tubesheets or baffles
  - Handles high-pressure streams (to 300 bar) on the inner pipe — standard piping components
  - Easy to clean — remove inner pipe for full access to both surfaces
  - Inner pipe can be finned to increase annular-side area by 3-10× for gas or viscous fluid service

  **Weaknesses:**
  - Lowest heat transfer area per unit (1-10 m²) — requires many units for large duties
  - Highest cost per m² of heat transfer area — inefficient use of materials
  - Many pipe connections and fittings increase leak potential compared to single shell-and-tube unit
  - Not suitable for large-scale industrial applications (>50 m² area) — use shell-and-tube or plate instead

## Operating Procedure

1. **Startup — cold side first**: Open the cold-side inlet and outlet valves. Establish cold fluid flow at the design rate. Verify flow by checking the flow meter and pressure drop across the exchanger. Cold fluid must be flowing before hot fluid is introduced — otherwise thermal shock can damage tube-to-tubesheet joints.
2. **Introduce hot side**: Gradually open the hot-side inlet valve. Increase hot flow over 10-15 minutes to the design rate. Monitor temperatures on both sides. The cold-side outlet temperature should rise as the hot side is introduced. Record the steady-state inlet and outlet temperatures on both sides after 15-30 minutes.
3. **Verify performance**: Calculate the actual heat duty: Q = m_cold × Cp_cold × (T_cold_out − T_cold_in). Verify the energy balance closes: Q_hot = Q_cold within ±5%. Calculate the actual LMTD and U value. Compare to design. Accept if U is within ±15% of the design value.
4. **Normal operation**: Monitor inlet and outlet temperatures on both sides. Track the U value weekly. A gradual decline in U indicates fouling. When U drops below 70% of the clean value, schedule cleaning.
5. **Shutdown**: Close the hot-side valve first (reduce thermal stress). Then close the cold-side valve. If the exchanger will be idle in freezing conditions, drain all water to prevent freeze damage. For prolonged shutdown, flush with a corrosion inhibitor solution.

## Calibration and Verification

1. **Heat transfer test**: Flow hot water (60-80°C) on one side and cold water (15-25°C) on the other at design flow rates. Measure inlet and outlet temperatures on both sides with calibrated thermometers (±0.1°C). Calculate actual heat duty: Q = m × Cp × ΔT for both streams (energy balance must close within ±5%). Calculate actual U value: U = Q / (A × LMTD). Compare to design value; accept if within ±15%.

2. **Pressure drop test**: Measure pressure drop on both sides at design flow rate. Compare to design calculation. Excessive pressure drop indicates fouling, debris, or incorrect baffle/plate installation.

3. **Leak test**: After thermal testing, re-pressurize both sides. Check for cross-contamination by sampling the cold outlet for hot-side fluid markers.

## Quantitative Parameters

| Parameter | Shell-and-Tube | Plate | Double-Pipe |
|-----------|---------------|-------|-------------|
| Heat transfer coefficient (liquid-liquid) | 300-1,500 W/m²·K | 3,000-7,000 W/m²·K | 300-1,000 W/m²·K |
| Maximum pressure | 10-300 bar | 10-25 bar | 10-300 bar |
| Maximum temperature | 600°C | 180°C (gasket limit) | 600°C |
| Surface area per unit | 2-500 m² | 1-200 m² | 1-10 m² |
| Footprint (per m² area) | Large | Compact (3-5× smaller) | Very large |
| Cleanability | Mechanical cleaning of shell side; chemical cleaning of tube side | Open for mechanical cleaning of all plates | Simple — remove inner pipe |
| Typical approach temperature | 5-15°C | 1-3°C | 5-15°C |
| Service life (gaskets) | 5-10 years (flange gaskets) | 2-5 years (plate gaskets) | 5-10 years |
| Service life (tubes/plates) | 10-30 years | 10-20 years | 10-30 years |
| Fouling tolerance | Moderate (shell side hard to clean) | Low (narrow channels plug) | Good (easy to clean) |
| Cost per m² area | Moderate | Low (at larger sizes) | High (inefficient at scale) |

## Scaling Notes

- **Shell-and-tube scaling**: Heat transfer area increases linearly with tube count × tube length. Diameter scaling: add tubes (limited by shell diameter). Length scaling: extend tube length (limited by shop handling and shipping — typically max 12 m). For areas >500 m², use multiple shells in series or parallel.
- **Plate exchanger scaling**: Add plates to increase area without changing the frame size (up to the frame capacity). Changing plate corrugation angle (high-θ for high heat transfer, low-θ for low pressure drop) tunes the performance without changing the physical size.
- **Temperature approach**: Plate exchangers achieve 1-3°C approach temperatures (near the theoretical limit), making them ideal for heat recovery applications where the available temperature driving force is small. Shell-and-tube exchangers typically achieve 5-15°C approach due to flow maldistribution and bypass streams.
- **Fouling factor**: Design calculations must include a fouling resistance (Rf) that accounts for scale, deposits, and corrosion products. Typical Rf values: 0.0001-0.0002 m²·K/W for clean water, 0.0003-0.0005 for cooling tower water, 0.0005-0.001 for dirty or polymerizing fluids. Excess area from fouling allowance means the exchanger is overdesigned when clean — plan for periodic cleaning to restore performance.
- **Tube vibration**: At high shell-side velocities, tubes can vibrate due to vortex shedding or fluidelastic instability. The maximum unsupported tube span (set by baffle spacing) must be short enough to keep the tube natural frequency above the vortex shedding frequency. Rule of thumb: baffle spacing ≤ 50 × tube OD for gas service, ≤ 100 × tube OD for liquid service.
- **Thermal expansion**: Fixed-tubesheet exchangers cannot accommodate differential thermal expansion between the tubes and shell. For temperature differences >30°C between tube and shell, use a U-tube or floating-head design. Alternatively, install an external bellows expansion joint on the shell.
- **Cost optimization**: Heat exchanger cost is approximately proportional to (area)^0.6. Doubling the area increases cost by only 50%. This economy of scale favors fewer, larger exchangers over many small ones. However, the shell diameter must accommodate the tube bundle — maximum practical tube count is approximately 3,000 tubes in a 2 m diameter shell.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Heat transfer rate below design (>15% low U value) | Tube-side or shell-side fouling (scale, biological growth, polymer deposits); air bound on one side (reduces effective area); baffle bypass (leakage around bundle) | Chemically clean fouled side (acid for mineral scale, alkali for organics, biocide for biofouling); vent air from high points; install seal strips to block bypass flow around bundle |
| Excessive pressure drop (>2× design) | Fouling restricting flow passages; debris from construction or corrosion; baffle installed backward; plate corrugation misaligned | Clean fouled side; flush with high-velocity water; inspect baffles during maintenance (segmental cut must face correct direction); verify plate orientation marks align during assembly |
| Cross-contamination (hot fluid appearing in cold stream) | Tube failure (corrosion, erosion, fatigue crack); plate perforation; gasket failure | Isolate and identify failed tube (plug both ends of leaking tube — acceptable to plug up to 10% of tubes before replacement); replace perforated plate; replace damaged gasket; install conductivity monitor on low-pressure outlet for early leak detection |
| Vibration and noise (shell-and-tube) | Flow-induced vibration (vortex shedding or fluidelastic instability) at high shell-side velocity; baffle spacing too wide | Reduce shell-side flow velocity; add intermediate baffles to reduce unsupported tube span; install antivibration baffles or detuning wires |
| Gasket failure (plate exchanger) — external leak | Over-compression or under-compression; gasket degraded by temperature or chemical attack; gasket groove damaged | Re-compress to design pack dimension (±2 mm); replace gaskets with correct material (EPDM for water <160°C, Viton for chemicals <200°C); inspect and repair gasket grooves |

## Safety

- **Thermal shock**: Rapid temperature changes create differential expansion between tubes and shell, stressing tube-to-tubesheet joints. Limit temperature ramp rates to 50°C/hour for startup and shutdown. Install expansion joints on fixed-tubesheet exchangers.
- **High-pressure fluid**: Shell-and-tube exchangers at 50+ bar contain significant stored energy. Pressure relief on both shell and tube sides. Never open a flanged connection while under pressure.
- **Cross-contamination**: Tube or plate failure allows hot and cold streams to mix. For hazardous fluids (toxic, flammable), install conductivity or pH monitors on the low-pressure outlet to detect leaks early. Double tubesheet construction prevents cross-contamination for critical applications.
- **Gasket failure (plate type)**: Gasket blowout at overpressure releases both fluids simultaneously. Pressure relief valves on both fluid ports. Secondary containment under plate exchangers handling hazardous fluids.

## Quality Control

- **Heat transfer coefficient monitoring**: Calculate U from operating data (flow rates, temperatures) weekly. Plot trend. A 20% decline from the clean baseline indicates fouling. Schedule cleaning when U drops to 70% of the clean value.
- **Pressure drop monitoring**: Record pressure drop on both sides at standard flow rates. A gradual increase indicates fouling; a sudden increase indicates blockage or debris.
- **Tube bundle inspection**: During turnaround, inspect tubes for corrosion, erosion, and cracking. Eddy current testing detects tube wall thinning before failure. Plug tubes with >50% wall loss.
- **Leak testing**: After any maintenance involving flange opening or tube work, hydrostatic test both sides at 1.5× design pressure before returning to service.

## Variations and Alternatives

- **Spiral heat exchanger**: Two flat plates rolled into a spiral, creating two concentric spiral channels. Single-pass, counter-current flow. Self-cleaning (spiral flow prevents fouling). Used for sludge, viscous fluids, and fouling applications where shell-and-tube exchangers plug. Limited to moderate pressures (<20 bar).
- **Air-cooled heat exchanger**: Rows of finned tubes with ambient air blown across by fans. Eliminates the need for cooling water. Used in arid locations and where water conservation is required. Lower heat transfer coefficient than water-cooled (30-60 W/m²·K with fins) — requires much larger surface area.
- **Coil-in-tank**: A simple immersed coil (copper or stainless steel tubing) in a tank of process fluid. Steam or hot water flows through the coil. The simplest heat exchanger — no shell, no baffles. Low heat transfer coefficient (100-300 W/m²·K for natural convection). Used for small-scale heating and cooling.
- **Graphite block heat exchanger**: Drilled holes in a block of impervious graphite. One fluid flows through horizontal holes, the other through vertical holes. Graphite provides excellent corrosion resistance to HCl, HF, and other aggressive acids at temperatures to 180°C. Used in acid cooling and heating where metal exchangers would corrode rapidly. Graphite is brittle — mechanical shock protection required.
- **Printed circuit heat exchanger (PCHE)**: Flat metal plates with chemically etched microchannels (0.5-2 mm deep), diffusion-bonded together. Extremely compact (5-10× smaller than shell-and-tube per unit area). Handles pressures to 600 bar. Used in offshore gas processing and supercritical CO₂ power cycles. Manufacturing requires photochemical etching and hot isostatic pressing — not bootstrap-appropriate but relevant as an advanced target.

## Material Selection Guide

| Fluid Pair | Shell/Tube Material | Gasket Material | Max Temp | Notes |
|------------|--------------------|-----------------|----------|-------|
| Water / water | Carbon steel (both) | EPDM | 120°C | Corrosion allowance 3 mm for CS; upgrade to 316L SS if water is corrosive |
| Steam / organic | CS shell, 316L tubes | Graphite or PTFE | 200°C | Steam on shell side for easy cleaning of condensate |
| Organic / organic | 316L SS (both) | PTFE | 200°C | Check compatibility — some organics attack specific elastomers |
| Acid / water | Graphite block or Hastelloy C-276 | PTFE or Viton | 150°C | Carbon steel and 316L SS corrode rapidly in HCl, HF at elevated temperature |
| Oil / water | CS shell, 304L SS tubes | Nitrile rubber (NBR) | 130°C | Oil on tube side for cleaning; CS shell acceptable for treated cooling water |
| Gas / water | CS shell, 304L SS tubes (finned) | EPDM | 180°C | Fins on gas side compensate for low gas-side h value |

Select materials based on the most aggressive fluid on each side. When in doubt, upgrade one grade: carbon steel → 304L SS → 316L SS → Hastelloy C-276 → titanium. The cost multiplier per upgrade step is approximately 2-3×. For gasketed plate exchangers, the gasket material (not the plate material) usually limits the maximum temperature. EPDM is the standard for water applications. Viton (FKM) handles higher temperatures and more aggressive chemicals but costs 3-5× more than EPDM.

## References

- [Distillation Column](distillation-column.md) — condenser and reboiler are shell-and-tube heat exchangers
- [Reactor Vessel](reactor-vessel.md) — jacket heat transfer design
- [Evaporator](evaporator.md) — heat exchanger used for evaporation duty
- [Distillation](distillation.md) — heat integration and pinch analysis
- [Water Treatment](water-treatment.md) — cooling water system design
- [Crystallizer](crystallizer.md) — cooling jacket and circulation heater design
- [Chemical Recovery](chemical-recovery.md) — heat recovery from process streams

## Heat Exchanger Sizing Example

A shell-and-tube heat exchanger cooling 10,000 kg/h of product from 80°C to 40°C using cooling water at 25°C (return at 35°C):

- **Heat duty**: Q = 10,000 × 4.18 × (80 − 40) / 3,600 = 464 kW
- **Cooling water flow**: m = 464 / (4.18 × (35 − 25)) = 11.1 kg/s = 40,000 kg/h
- **LMTD** (counter-current): ΔT₁ = 80 − 35 = 45°C, ΔT₂ = 40 − 25 = 15°C. LMTD = (45 − 15) / ln(45/15) = 27.5°C
- **Overall U** (organic liquid / water): 500 W/m²·K
- **Required area**: A = 464,000 / (500 × 27.5) = 33.7 m²
- **Tube selection**: 19 mm OD, 2 m length, 1.5 mm wall, 316L stainless. Area per tube = π × 0.019 × 2 = 0.119 m²
- **Number of tubes**: 33.7 / 0.119 = 283 tubes
- **Shell diameter** (25 mm triangular pitch): D ≈ 680 mm (with 25% baffle cut)
- **Tube-side pressure drop** (2-pass): 15-25 kPa (water velocity ≈ 1.2 m/s)
- **Shell-side pressure drop**: 20-40 kPa (baffle spacing ≈ 500 mm)

## Cleaning Methods

- **Mechanical cleaning**: Pull the tube bundle and clean tubes with rotating brushes or high-pressure water jets (200-1,000 bar). Shell side: clean with steam or high-pressure water. Frequency: every 6-24 months depending on fouling rate.
- **Chemical cleaning**: Circulate a cleaning solution through the exchanger without disassembly. For mineral scale (CaCO₃): 5-10% HCl with corrosion inhibitor. For organic deposits: 2-5% NaOH at 80°C. For biological fouling: sodium hypochlorite (200-500 ppm Cl₂). After chemical cleaning, flush thoroughly with water before returning to service.
- **Hydroblasting**: High-pressure water (500-2,000 bar) through flexible lances inserted into each tube. Effective for hard scale deposits. Requires tube bundle removal. Time: 2-8 hours for a 200-tube bundle.

## Thermal Design Fundamentals

The fundamental equation for heat exchanger design is Q = U × A × ΔT_lm, where Q is the heat duty (W), U is the overall heat transfer coefficient (W/m²·K), A is the heat transfer area (m²), and ΔT_lm is the log-mean temperature difference (K). Each of these three terms has a distinct physical meaning:

- **Q**: Determined by the process requirement (how much heat must be transferred). For heating: Q = m × Cp × (T_out − T_in). For phase change (condensation or boiling): Q = m × λ (latent heat). There is no design freedom in Q — it is set by the production rate.
- **U**: Determined by the fluids and geometry. The overall coefficient combines the convective resistance on both sides, the conductive resistance of the wall, and the fouling resistance: 1/U = 1/h_hot + t_wall/k_wall + 1/h_cold + Rf. Designers can influence U by choosing tube diameter, flow velocity, baffles, and surface enhancements (fins, corrugation).
- **ΔT_lm**: The log-mean temperature difference accounts for the changing temperature difference along the exchanger length. Counter-current flow maximizes ΔT_lm. For a 1-2 shell-and-tube exchanger (one shell pass, two tube passes), apply a correction factor F (typically 0.8-0.95).

The design iteration: start with Q and estimated U → calculate required A → select tube count, length, shell diameter → calculate actual U and pressure drop → iterate until converged. Most designs converge in 3-5 iterations.

---
*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
