# Distillation Column

> **Node ID**: chemistry.distillation-column
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`metals.welding`](../machine-tools/welding-equipment.md), [`chemistry.distillation`](distillation.md), [`ceramics.kilns`](../ceramics/kilns.md)
> **Enables**: [`chemistry.solvents`](solvents.md), [`petroleum.refining`](../petroleum/refining.md), [`silicon.purification`](../silicon/purification.md)
> **Timeline**: Years 15-30
> **Outputs**: fractionated_liquids
> **Critical**: Yes — the distillation column is the most important separation apparatus in chemical manufacturing, responsible for 40-60% of capital cost in a typical chemical plant. Petroleum refining, solvent purification, and silicon chlorosilane separation all require multi-stage fractional distillation columns.

## Overview

A distillation column separates liquid mixtures into their component fractions by exploiting differences in boiling points (volatility). Vapor rising from the reboiler contacts liquid descending from the condenser on trays or packing inside the column. At each contact point, the more volatile component transfers from liquid to vapor, and the less volatile component transfers from vapor to liquid. After many such contacts (theoretical plates), the overhead vapor is enriched in the more volatile component and the bottoms liquid is enriched in the less volatile component.

The column shell is a tall cylindrical pressure vessel containing internal contacting devices (trays or packing). The reboiler at the base provides vapor by boiling the bottoms liquid. The condenser at the top liquefies overhead vapor; part returns as reflux, part is drawn as distillate product. Feed enters at a mid-point nozzle. Product draw nozzles at intermediate heights allow multi-product fractionation. Column diameter is set by vapor velocity (typically 0.5-1.5 m/s at atmospheric pressure). Column height is set by the number of theoretical plates required for the desired separation, multiplied by the tray spacing (450-600 mm) or packing HETP (0.1-0.6 m). Typical height-to-diameter ratio: 10-30:1.

Three principal internal configurations serve different separation duties: **bubble-cap trays** (high turndown ratio, handles variable liquid rates, oldest design), **sieve trays** (simple perforated plates, lowest cost, most common modern design), and **packed columns** (random or structured packing, lowest pressure drop, preferred for vacuum service and heat-sensitive materials). The choice between trays and packing depends on the column operating pressure, liquid-to-vapor ratio, fouling tendency, and required number of theoretical stages.

## Prerequisites

- **[Pressure vessel construction](reactor-vessel.md)**: Column shell must meet ASME Section VIII design requirements
- **[Welding](../machine-tools/welding-equipment.md)**: Full-penetration welds on all shell seams, radiographic inspection
- **[Heat exchanger](heat-exchanger.md)**: Condenser and reboiler construction
- **[Steel plate](../metals/iron-steel.md)**: Carbon steel A516 Gr.70 or 304L/316L stainless for corrosive service
- **[Packing or trays](../ceramics/pottery.md)**: Ceramic saddles for random packing, or fabricated steel trays

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate](../metals/iron-steel.md) (shell) | 500-5,000 kg | Carbon steel A516 Gr.70, 6-25 mm thick | [Iron & Steel](../metals/iron-steel.md) | 304L/316L stainless (corrosive service) |
| [Steel plate](../metals/iron-steel.md) (heads) | 100-1,000 kg | Matching shell grade, torispherical | [Iron & Steel](../metals/iron-steel.md) | — |
| [Steel pipe](../metals/forming.md) (nozzles) | 50-200 kg | Schedule 40, 50-200 mm diameter | [Forming](../metals/forming.md) | Flanged nozzles (removable) |
| [Stainless steel tubing](../metals/forming.md) | 50-500 kg | 316L, for condenser tubes | [Forming](../metals/forming.md) | Copper-nickel alloy (seawater cooling) |
| [Steel plate](../metals/iron-steel.md) (condenser shell) | 100-500 kg | A36 or 316L, 6-10 mm thick | [Iron & Steel](../metals/iron-steel.md) | — |
| [Trays or packing](../ceramics/pottery.md) | As needed | Sieve trays (steel) or ceramic saddles | [Ceramics](../ceramics/pottery.md) | Structured packing (corrugated stainless sheets) |
| [Welding consumables](../machine-tools/welding-equipment.md) | 20-100 kg | E7018 (CS) or E316L-16 (SS) | [Welding](../machine-tools/welding-equipment.md) | — |
| [Gaskets](../polymers/rubber.md) | 1 set | PTFE or spiral-wound, all flange sizes | [Elastomers](../polymers/rubber.md) | — |
| [Bolts](../metals/steelmaking.md) | 50-200 kg | ASTM A193 B7 or B8 | [Fasteners](../metals/steelmaking.md) | — |
| [Insulation](../construction/building-materials.md) | 20-100 m² | Mineral wool 50-100 mm, aluminum cladding | [Construction](../construction/building-materials.md) | Calcium silicate (high temperature) |
| [Pressure relief valve](../measurement/index.md) | 1-2 units | Rated to 1.1× MAWP | [Measurement](../measurement/index.md) | Rupture disc (no resetting) |

## Process Description

### Shell Fabrication

1. **Calculate design parameters**: Determine column height (2-30 m), diameter (200 mm to 8 m), design pressure (atmospheric to 20 bar), design temperature (ambient to 400°C). Calculate minimum wall thickness per ASME Section VIII. For vacuum service, check external pressure collapse resistance: vacuum columns require stiffening rings at 1-2 m intervals and minimum 6 mm wall for <1 m diameter.

2. **Roll shell sections**: Roll steel plate to cylindrical sections (can courses), each 1.5-3 m long. Check roundness with sweep board: deviation <1% diameter. For columns taller than 5 m, fabricate multiple sections to be welded together.

3. **Weld longitudinal seams**: Full-penetration double-V groove weld, all longitudinal seams. Radiograph 100% of longitudinal welds. Grind internal welds flush for smooth flow and to avoid creating dead zones where liquid accumulates.

4. **Install internal support rings**: Weld circumferential support rings (flat bar, 25-50 mm wide, 6-10 mm thick) at each tray or packing support level. Ring spacing: 450-600 mm for trays, or as required by packing module height. Ensure rings are level within ±3 mm around the circumference — out-of-level trays cause liquid maldistribution.

5. **Weld sections together**: Stack and weld can courses with circumferential butt welds. Maintain column straightness: deviation <0.2% of total height. Use alignment clamps and check with plumb line or laser level.

6. **Install nozzles**: Cut openings and weld nozzle necks for feed (mid-height), overhead vapor outlet (top), bottoms liquid outlet (bottom), reboiler return (bottom), reflux inlet (top), side draws (as needed), and instruments (thermowells at top, middle, bottom; pressure taps). Install reinforcement pads on openings exceeding 50% of shell diameter.

7. **Attach top and bottom heads**: Weld torispherical or elliptical heads to shell ends. The top head may incorporate a flanged manway (300-600 mm diameter) for internal access during construction and maintenance.

8. **Install tray support hardware**: For sieve or valve trays, weld downcomer bars and tray support clips to the support rings. For packed columns, install packing support grids (grating or woven wire mesh) on the support rings.

### Tray Installation — Sieve Trays

9. **Install sieve trays**: Cut flat steel plates to match the internal column diameter. Drill or punch perforations: 3-12 mm diameter holes on 12-25 mm triangular pitch (5-15% open area). Install downcomer channels (40-60 mm wide channels at alternating edges of each tray) to route liquid from one tray to the next. Secure trays on support clips. Check that each tray is level within ±3 mm. Sieve trays are the simplest and most common tray type — low cost, easy to fabricate, and adequate for most separations. Weep point (minimum vapor velocity below which liquid drains through the holes): typically 0.3-0.5 m/s. Flooding point: 1.5-2.5 m/s.

### Tray Installation — Bubble-Cap Trays

10. **Install bubble-cap trays**: Fabricate or procure bubble caps (35-150 mm diameter cast iron or stamped steel caps mounted on risers). Each cap has slots or serrations at the base. Vapor rises through the riser, is directed downward by the cap, and bubbles through the liquid seal. Bubble-cap trays handle wider liquid rate variation than sieve trays (turndown ratio 10:1 vs. 3:1) and do not weep at low vapor rates — the liquid seal prevents drainage. Disadvantages: higher cost, higher pressure drop (0.5-1.0 kPa per tray vs. 0.3-0.7 kPa for sieve trays), and more difficult to clean. Tray spacing: 450-600 mm.

### Packed Column Installation

11. **Install packing**: Pour random packing (ceramic Raschig rings 25-50 mm, Pall rings 25-50 mm, or saddles 25-50 mm) into the column from the top, distributing evenly. Or stack structured packing modules (corrugated metal sheets in pre-formed cylindrical cartridges) on support grids. Install liquid distributors (perforated pipes or drip-pan type, >40 pour points per m²) above each packed bed. Redistributors every 3-4 m of packed height. Packing HETP values: Raschig rings 0.4-0.6 m, Pall rings 0.3-0.4 m, structured packing 0.1-0.3 m.

### Condenser and Reboiler

12. **Construct shell-and-tube condenser**: Roll a cylindrical shell (200-600 mm diameter, 1-3 m long) from steel plate. Insert a tube bundle: 20-200 tubes (316L stainless or copper-nickel, 19-25 mm OD, 1.5-2.5 mm wall) rolled or welded into tubesheets at both ends. Tubesheets are drilled with tube holes on triangular pitch. Tube-side: overhead vapor condenses inside tubes. Shell-side: cooling water flows baffled across tube bundle. Weld or bolt tubesheets to the shell. Install water inlet and outlet nozzles, and vapor inlet and condensate outlet nozzles. Heat transfer coefficient: 300-800 W/m²·K for condensing organics. Size condenser area: A = Q / (U × LMTD), where Q = total condensation duty, LMTD = log mean temperature difference. Temperature approach: 5-15°C.

13. **Construct kettle reboiler**: A horizontal shell (400-1000 mm diameter, 1-3 m long) with a tube bundle inside. Steam (0.3-1.0 MPa) flows through tubes; column bottoms liquid fills the shell side and boils. A weir at one end maintains liquid level above the tube bundle. Vapor exits the top to return to the column bottom. Liquid product overflows the weir and exits at the bottom. Heat transfer coefficient: 800-1,500 W/m²·K for boiling organics.

14. **Alternative — thermosiphon reboiler**: Vertical shell-and-tube exchanger. Liquid from the column bottom enters the tube side at the bottom. Steam heats the shell side. Boiling in the tubes creates a two-phase mixture less dense than the liquid column, driving natural circulation (thermosiphon effect). More compact than kettle type. Better for clean (non-fouling) services.

### Assembly and Testing

15. **Mount column on support structure**: Weld or bolt the column to a structural steel skirt or legs. The support must carry the column weight (including liquid fill during operation) and resist wind loads. Tall columns (>10 m) may require guy wires or a structural frame. Ensure the column is plumb within 0.2% of height.

16. **Connect condenser and reboiler**: Pipe the overhead vapor line from the column top to the condenser shell. Pipe condensate from the condenser to a reflux drum (small horizontal vessel). Pipe reflux from the drum back to the column top (via pump or gravity). Connect the reboiler to the column bottom: liquid draw to reboiler, vapor return to column.

17. **Install reflux splitter**: Install a valve or diverter on the condensate line from the reflux drum. This controls the reflux ratio (L/D): one stream returns to the column as reflux, the other is drawn as distillate product. Manual valve for simple columns; automated control valve with temperature controller for precise operation.

18. **Install pressure relief**: Mount pressure relief valve on the top head or overhead vapor line, set to 1.1× MAWP. Install rupture disc as secondary relief for critical applications.

19. **Hydrostatic test**: Fill the entire column, condenser, reboiler, and piping with water. Pressurize to 1.5× MAWP. Hold 30 minutes. Inspect all welds, flanges, and connections. Zero leaks acceptable. For tall columns, consider the hydrostatic head at the bottom (water at 10 m depth adds 1 bar pressure).

20. **Install insulation**: Apply 50-100 mm mineral wool insulation to the column shell, reboiler, and all hot process piping. Clad with aluminum sheet metal. Do NOT insulate the condenser (it must reject heat).

## Calibration and Verification

1. **Pressure test**: Verify 1.5× MAWP hydrostatic hold with zero pressure drop over 30 minutes.

2. **Leak test**: After hydrostatic test and draining, pressurize to 0.3-0.5 bar with air. Soap-test all flanged connections and nozzles. Repair any leaks.

3. **Tray level check**: For trayed columns, fill with water to the top tray and verify all trays hold water level within ±3 mm around the circumference. Excessive weep-through indicates damaged or poorly fitted trays.

4. **Packing distribution test**: For packed columns, run water through the top liquid distributor at design flow rate. Verify uniform drip pattern across the column cross-section (>40 pour points per m²). Dry spots indicate distributor problems that will cause channeling.

5. **Heat transfer test**: Run the reboiler at 50% design duty with water in the column. Verify boilup rate and condenser capacity. Measure approach temperatures on both reboiler and condenser.

## Quantitative Parameters

| Parameter | Sieve Trays | Bubble-Cap Trays | Packed (Random) | Packed (Structured) |
|-----------|-------------|-----------------|-----------------|---------------------|
| HETP (height equivalent to a theoretical plate) | 450-600 mm (at tray spacing) | 450-600 mm | 400-600 mm (Raschig), 300-400 mm (Pall) | 100-300 mm |
| Pressure drop per theoretical plate | 0.3-0.7 kPa | 0.5-1.0 kPa | 0.15-0.4 kPa | 0.05-0.15 kPa |
| Vapor velocity (atmospheric) | 0.5-1.5 m/s | 0.3-1.2 m/s | 0.5-1.5 m/s | 0.5-2.0 m/s |
| Turndown ratio | 3:1 | 10:1 | 3:1 | 3:1 |
| Tray spacing | 450-600 mm | 450-600 mm | N/A | N/A |
| Open area (trays) | 5-15% | N/A (caps) | N/A | N/A |
| Liquid load range | 5-80 m³/m·h | 5-100 m³/m·h | 5-60 m³/m·h | 5-80 m³/m·h |
| Fouling tolerance | Moderate | Low (caps trap deposits) | Low (packing plugs) | Low |
| Best application | General purpose, clean service | Variable feed rates, startup/shutdown | Vacuum service, corrosive | High-purity, low ΔP |

| Parameter | Value |
|-----------|-------|
| Column height (packed batch) | 2-10 m |
| Column height (continuous fractional) | 10-50 m |
| Column diameter | 200 mm - 8 m (set by vapor velocity) |
| Height-to-diameter ratio | 10-30:1 |
| Number of theoretical plates (packed batch) | 5-15 |
| Number of theoretical plates (continuous) | 15-50 |
| Reboiler heat transfer coefficient | 800-1,500 W/m²·K |
| Condenser heat transfer coefficient | 300-800 W/m²·K |
| Design pressure (atmospheric column) | 1-2 bar |
| Design pressure (pressure column) | 2-20 bar |
| Service life (before major turnaround) | 5-15 years (inspection and cleaning cycle) |

## Scaling Notes

- **Diameter scaling**: Column diameter is proportional to the square root of the vapor rate. Double the throughput requires approximately 41% larger diameter (× √2). The F-factor (vapor velocity × √vapor density) should be kept below the flooding limit: F < 1.5-2.5 Pa^0.5 for trays, F < 2.0-3.0 for structured packing.
- **Height scaling**: The number of theoretical stages is independent of column diameter. A 300 mm laboratory column with 20 stages requires the same number of stages as a 3 m production column. Height scales only with the internal device (tray spacing or HETP).
- **Pressure drop scaling**: Total column pressure drop = number of stages × pressure drop per stage. For vacuum columns processing heat-sensitive materials, structured packing (0.05-0.15 kPa per stage) is mandatory — sieve trays (0.3-0.7 kPa per stage) would cause excessive bottom temperatures across 30+ stages.
- **Reflux ratio**: Higher reflux ratio improves separation but increases energy consumption (more reboiler duty and condenser duty). Minimum reflux ratio is calculated by the Underwood equation. Practical operation at 1.2-1.5× minimum reflux.
- **Feed stage optimization**: The feed should enter at the stage where the liquid composition most closely matches the feed composition. Introducing the feed at the wrong stage reduces separation efficiency by 10-30%. For a new column, the optimal feed stage can be determined by simulation or by operating the column at several feed points and comparing product purities.
- **Turnaround planning**: Schedule major turnaround every 5-8 years. Inspect trays/packing for damage, corrosion, and fouling. Measure shell thickness by ultrasonic testing at corrosion-prone locations (feed zone, reboiler return, overhead). Replace damaged trays, clean fouled packing, re-seat all flange gaskets. A typical turnaround takes 2-4 weeks.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Column flooding (ΔP spike, loss of separation) | Vapor velocity too high; excessive liquid load; fouled trays or plugged packing | Reduce reboiler heat immediately to lower boilup; reduce feed rate; check liquid distributor for blockage; clean or replace fouled internals |
| Poor separation (overhead contains heavy components) | Insufficient reflux; damaged or missing trays; liquid maldistribution in packed column | Increase reflux ratio by 20-50%; inspect trays via manway (check for dislodged trays, broken caps, or corroded sieve holes); verify liquid distributor has >40 pour points/m² |
| Excessive pressure drop (>2× design) | Fouled or plugged trays/packing; liquid flooding from excessive reflux; foreign objects blocking downcomers | Reduce reflux and feed rates; schedule cleaning (chemical wash or mechanical); inspect downcomers for blockage |
| Weeping (sieve trays) — liquid draining through perforations | Vapor velocity below weep point (0.3-0.5 m/s); low boilup; feed interruption | Increase reboiler duty to raise vapor velocity; reduce feed rate; consider switching to valve trays or bubble caps for low-load operation |
| Product discoloration or degradation | Hot spots in reboiler; excessive bottom temperature (thermal degradation); metal corrosion products in column | Reduce reboiler temperature; switch to thermosiphon reboiler (lower residence time); verify metallurgy is compatible with process fluid; install corrosion coupon monitoring |
| Condenser overload (overhead temperature rising) | Cooling water insufficient; condenser tubes fouled; non-condensable gas accumulation | Increase cooling water flow; clean condenser tubes; vent non-condensables from the reflux drum |

## Safety

- **Flammable vapor explosion**: Hydrocarbon and solvent vapors form explosive mixtures at 1-10% in air. Ground and bond all metal vessels and piping. Use explosion-proof electrical equipment. Nitrogen purge before introducing flammables. Install flame arrestors on all vent lines.
- **Hot surfaces and boiling liquids**: Reboiler contents at 80-350°C. Insulate all hot surfaces to <60°C. Emergency shower within 10 m. Thermal gloves and face shield for sampling.
- **Toxic chemical exposure**: Chlorosilanes release HCl on moisture contact. Benzene and aromatic fractions are carcinogenic. Local exhaust ventilation at all sample ports. Respiratory protection for toxic distillates.
- **Pressure vessel safety**: Relief valve at 1.1× MAWP. Hydrostatic test at 1.5× design pressure before commissioning. Differential pressure monitoring — sudden increase signals flooding, reduce boilup immediately.
- **Column flooding**: Excessive vapor velocity causes liquid entrainment upward, separation fails, pressure drop spikes. Response: reduce reboiler heat immediately. Do NOT increase reflux (worsens flooding).
- **Static electricity**: Low-conductivity liquids flowing through pipes and packing generate static charge. Ground all metal. Limit filling velocity to <1 m/s. Use antistatic additives in fuels.

## Quality Control

- **Distillate composition**: Sample overhead product and analyze by gas chromatography or refractive index. Verify the concentration of the key component meets specification (e.g., >99.0% ethanol, <0.5% water in anhydrous solvent).
- **Bottoms composition**: Sample bottoms product for heavy key component content. Verify light key component content in bottoms is below specification (e.g., <0.5% ethanol in bottoms for an ethanol-water column).
- **Temperature profile**: Record temperatures at top, middle, and bottom of the column during steady operation. Compare to the calculated temperature profile for the design separation. A shifted temperature profile indicates feed composition changes, tray damage, or reflux ratio deviation.
- **Material balance verification**: Measure feed, distillate, and bottoms flow rates. Verify that total mass in ≈ total mass out (within ±2%). Verify component balance: feed × feed composition ≈ distillate × distillate composition + bottoms × bottoms composition.
- **Reflux ratio verification**: Measure the reflux and distillate flow rates. Reflux ratio = reflux flow / distillate flow. Compare to the design value. A reflux ratio that is too low causes poor separation; too high wastes energy without improving product quality.
- **Column pressure drop trend**: Record total column differential pressure daily. A gradual increase indicates fouling or flooding tendency. A sudden decrease may indicate tray damage or loss of packing. Plot the trend and set alarm limits at ±20% of the baseline steady-state value.

## Variations and Alternatives

- **Batch distillation**: A single vessel (pot still) with a column attached. Charge the pot, heat, collect fractions in sequence (most volatile first). Used for small-scale and multi-product operations. Lower capital cost, higher energy consumption per unit product. Typical column: 2-5 m height, 100-500 mm diameter, 5-15 theoretical plates.
- **Azeotropic distillation**: Add an entrainer (third component) that forms a heterogeneous azeotrope with one component, breaking the azeotrope. Example: ethyl acetate added to ethanol-water to carry water overhead. Requires a separate entrainer recovery column.
- **Extractive distillation**: Add a high-boiling solvent that selectively alters relative volatility. Example: ethylene glycol added to isopropanol-water to make water less volatile. The solvent leaves in the bottoms and is recycled. The solvent must be non-toxic, thermally stable, and easily separated from the bottoms product.
- **Steam stripping**: Inject live steam directly into the column bottom (no reboiler). Used when the bottoms product is water or when the feed contains water-immiscible organics. Eliminates reboiler capital cost but dilutes the bottoms.
- **Reactive distillation**: Combine reaction and separation in one column. The reaction produces the product, which is immediately distilled away, driving the equilibrium forward. Example: esterification (ethanol + acetic acid → ethyl acetate + water) — removing the ester and water from the reaction zone increases conversion beyond the equilibrium limit. Requires a catalyst bed within the column (structured packing with catalyst embedded).
- **Dividing-wall column**: A vertical partition inside the column shell creates three sections in a single shell, replacing two conventional columns. Reduces capital cost by 20-30% and energy consumption by 30%. More complex to design and control. Used for separating three-component mixtures where the middle component has intermediate volatility.
- **Heat-integrated distillation**: Use the overhead vapor from a high-temperature column as the heating medium for a low-temperature column (multi-column heat integration). Requires careful pressure selection to create the temperature driving force between columns. Pinch analysis (see [Distillation](distillation.md)) determines the optimal heat integration scheme for a multi-column plant.

## References

- [Distillation](distillation.md) — distillation theory, types, and process design
- [Heat Exchanger](heat-exchanger.md) — shell-and-tube and plate exchanger construction
- [Reactor Vessel](reactor-vessel.md) — pressure vessel construction principles
- [Chemical Recovery](chemical-recovery.md) — solvent recovery by distillation
- [Solvents](solvents.md) — solvent production, purification, and recovery by distillation
- [Evaporator](evaporator.md) — concentration by evaporation (related but different separation)
- [Chemical Recovery](chemical-recovery.md) — solvent recovery and recycling by distillation
- [Petroleum Refining](../petroleum/refining.md) — distillation is the primary separation in petroleum refining

## Feed Preheat and Energy Recovery

The feed to a distillation column should be preheated to near its bubble point (the temperature at which the first vapor bubble forms at the feed pressure) to minimize the reboiler duty and prevent thermal shock to the trays at the feed point. A cold feed entering a hot column causes excessive condensation at the feed tray, disrupting the vapor-liquid balance and reducing separation efficiency by 10-20%.

Feed preheat is typically accomplished by exchanging heat with a hot product stream. The bottoms product exits the reboiler at the highest temperature in the column — routing the bottoms through a shell-and-tube heat exchanger that preheats the feed recovers 30-50% of the reboiler energy. For a column with 80°C overhead and 150°C bottoms, preheating the feed from 25°C to 130°C reduces reboiler steam consumption by approximately 40%.

In a petroleum refinery, the crude preheat train uses 6-10 shell-and-tube heat exchangers in series, recovering heat from all hot product streams (naphtha, kerosene, diesel, gas oil) before the crude enters the tube-still furnace. A well-designed preheat train brings the crude to 280-320°C before firing, reducing furnace fuel consumption by 60-70%.

## Column Sizing Example

A column separating ethanol (bp 78.4°C) from water (bp 100°C) at atmospheric pressure. Feed: 1,000 kg/h of 40 wt% ethanol. Desired products: distillate >92 wt% ethanol, bottoms <0.5 wt% ethanol.

- **Minimum stages** (Fenske equation, total reflux): N_min = 6.6
- **Minimum reflux** (Underwood equation): R_min = 1.3
- **Operating reflux**: R = 1.5 × R_min = 1.95
- **Actual stages** (Gilliland correlation): N = 16 theoretical stages + reboiler = 17 total
- **Feed stage**: Stage 10 (from bottom)
- **Column diameter** (at 0.8 m/s vapor velocity): 0.5 m (for 1,000 kg/h feed)
- **Column height** (450 mm tray spacing, 17 stages): 17 × 0.45 = 7.65 m + 1.5 m disengagement = 9.15 m
- **Condenser duty**: 350 kW (total condenser, reflux + product)
- **Reboiler duty**: 370 kW (slightly more than condenser due to feed preheat)

---
*Part of the [Bootciv Tech Tree](../../index.md) • [Chemistry](./index.md) • [All Domains](../../index.md)*
