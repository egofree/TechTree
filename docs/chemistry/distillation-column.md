# Distillation Column

> **Node ID**: chemistry.distillation-column
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`metals.welding`](../metals/welding.md), [`chemistry.distillation`](distillation.md), [`ceramics.kilns`](../ceramics/kilns.md)
> **Enables**: [`chemistry.solvents`](solvents.md), [`petroleum.refining`](../petroleum/refining.md), [`silicon.purification`](../silicon/purification.md)
> **Timeline**: Years 15-30
> **Outputs**: fractionated_liquids
> **Critical**: Yes — the distillation column is the most important separation apparatus in chemical manufacturing, responsible for 40-60% of capital cost in a typical chemical plant. Petroleum refining, solvent purification, and silicon chlorosilane separation all require multi-stage fractional distillation columns.

## Principle

A distillation column separates liquid mixtures into their component fractions by exploiting differences in boiling points (volatility). Vapor rising from the reboiler contacts liquid descending from the condenser on trays or packing inside the column. At each contact point, the more volatile component transfers from liquid to vapor, and the less volatile component transfers from vapor to liquid. After many such contacts (theoretical plates), the overhead vapor is enriched in the more volatile component and the bottoms liquid is enriched in the less volatile component.

The column shell is a tall cylindrical pressure vessel containing internal contacting devices (trays or packing). The reboiler at the base provides vapor by boiling the bottoms liquid. The condenser at the top liquefies overhead vapor; part returns as reflux, part is drawn as distillate product. Feed enters at a mid-point nozzle. Product draw nozzles at intermediate heights allow multi-product fractionation.

Column diameter is set by vapor velocity (typically 0.5-1.5 m/s at atmospheric pressure). Column height is set by the number of theoretical plates required for the desired separation, multiplied by the tray spacing (450-600 mm) or packing HETP (0.1-0.6 m). Typical height-to-diameter ratio: 10-30:1.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate](../metals/iron-steel.md) (shell) | 500-5,000 kg | Carbon steel A516 Gr.70, 6-25 mm thick | [Iron & Steel](../metals/iron-steel.md) | 304L/316L stainless (corrosive service) |
| [Steel plate](../metals/iron-steel.md) (heads) | 100-1,000 kg | Matching shell grade, torispherical | [Iron & Steel](../metals/iron-steel.md) | — |
| [Steel pipe](../metals/forming.md) (nozzles) | 50-200 kg | Schedule 40, 50-200 mm diameter | [Forming](../metals/forming.md) | Flanged nozzles (removable) |
| [Stainless steel tubing](../metals/forming.md) | 50-500 kg | 316L, for condenser tubes | [Forming](../metals/forming.md) | Copper-nickel alloy (seawater cooling) |
| [Steel plate](../metals/iron-steel.md) (condenser shell) | 100-500 kg | A36 or 316L, 6-10 mm thick | [Iron & Steel](../metals/iron-steel.md) | — |
| [Trays or packing](../ceramics/pottery.md) | As needed | Sieve trays (steel) or ceramic saddles | [Ceramics](../ceramics/pottery.md) | Structured packing (corrugated stainless sheets) |
| [Welding consumables](../metals/welding.md) | 20-100 kg | E7018 (CS) or E316L-16 (SS) | [Welding](../metals/welding.md) | — |
| [Gaskets](../polymers/elastomers.md) | 1 set | PTFE or spiral-wound, all flange sizes | [Elastomers](../polymers/elastomers.md) | — |
| [Bolts](../metals/fasteners.md) | 50-200 kg | ASTM A193 B7 or B8 | [Fasteners](../metals/fasteners.md) | — |
| [Insulation](../construction/building-materials.md) | 20-100 m² | Mineral wool 50-100 mm, aluminum cladding | [Construction](../construction/building-materials.md) | Calcium silicate (high temperature) |
| [Pressure relief valve](../measurement/index.md) | 1-2 units | Rated to 1.1× MAWP | [Measurement](../measurement/index.md) | Rupture disc (no resetting) |

## Construction Steps

### Shell Fabrication

1. **Calculate design parameters**: Determine column height (2-30 m), diameter (200 mm to 8 m), design pressure (atmospheric to 20 bar), design temperature (ambient to 400°C). Calculate minimum wall thickness per ASME Section VIII. For vacuum service, check external pressure collapse resistance: vacuum columns require stiffening rings at 1-2 m intervals and minimum 6 mm wall for <1 m diameter.

2. **Roll shell sections**: Roll steel plate to cylindrical sections (can courses), each 1.5-3 m long. Check roundness with sweep board: deviation <1% diameter. For columns taller than 5 m, fabricate multiple sections to be welded together.

3. **Weld longitudinal seams**: Full-penetration double-V groove weld, all longitudinal seams. Radiograph 100% of longitudinal welds. Grind internal welds flush for smooth flow and to avoid creating dead zones where liquid accumulates.

4. **Install internal support rings**: Weld circumferential support rings (flat bar, 25-50 mm wide, 6-10 mm thick) at each tray or packing support level. Ring spacing: 450-600 mm for trays, or as required by packing module height. Ensure rings are level within ±3 mm around the circumference — out-of-level trays cause liquid maldistribution.

5. **Weld sections together**: Stack and weld can courses with circumferential butt welds. Maintain column straightness: deviation <0.2% of total height. Use alignment clamps and check with plumb line or laser level.

6. **Install nozzles**: Cut openings and weld nozzle necks for feed (mid-height), overhead vapor outlet (top), bottoms liquid outlet (bottom), reboiler return (bottom), reflux inlet (top), side draws (as needed), and instruments (thermowells at top, middle, bottom; pressure taps). Install reinforcement pads on openings exceeding 50% of shell diameter.

7. **Attach top and bottom heads**: Weld torispherical or elliptical heads to shell ends. The top head may incorporate a flanged manway (300-600 mm diameter) for internal access during construction and maintenance.

8. **Install tray support hardware**: For sieve or valve trays, weld downcomer bars and tray support clips to the support rings. For packed columns, install packing support grids (grating or woven wire mesh) on the support rings.

### Tray Installation

9. **Install sieve trays**: Cut flat steel plates to match the internal column diameter. Drill or punch perforations: 3-12 mm diameter holes on 12-25 mm triangular pitch (5-15% open area). Install downcomer channels (40-60 mm wide channels at alternating edges of each tray) to route liquid from one tray to the next. Secure trays on support clips. Check that each tray is level within ±3 mm.

10. **Alternative — install packing**: Pour random packing (ceramic Raschig rings, Pall rings, or saddles) into the column from the top, distributing evenly. Or stack structured packing modules (corrugated metal sheets in pre-formed cylindrical cartridges) on support grids. Install liquid distributors (perforated pipes or drip-pan type, >40 pour points per m²) above each packed bed. Redistributors every 3-4 m of packed height.

### Condenser

11. **Construct shell-and-tube condenser**: Roll a cylindrical shell (200-600 mm diameter, 1-3 m long) from steel plate. Insert a tube bundle: 20-200 tubes (316L stainless or copper-nickel, 19-25 mm OD, 1.5-2.5 mm wall) rolled or welded into tubesheets at both ends. Tubesheets are drilled with tube holes on triangular pitch. Tube-side: overhead vapor condenses inside tubes. Shell-side: cooling water flows baffled across tube bundle. Weld or bolt tubesheets to the shell. Install water inlet and outlet nozzles, and vapor inlet and condensate outlet nozzles.

12. **Size condenser area**: Calculate required heat transfer area: A = Q / (U × LMTD), where Q = total condensation duty (reflux + product draw), U = 300-800 W/m²·K for condensing organics, LMTD = log mean temperature difference between condensing vapor and cooling water. Temperature approach: 5-15°C.

### Reboiler

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

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Column height (packed batch) | 2-10 m |
| Column height (continuous fractional) | 10-50 m |
| Column diameter | 200 mm - 8 m (set by vapor velocity) |
| Height-to-diameter ratio | 10-30:1 |
| Number of theoretical plates (packed batch) | 5-15 |
| Number of theoretical plates (continuous) | 15-50 |
| HETP (Raschig rings) | 0.4-0.6 m |
| HETP (Pall rings) | 0.3-0.4 m |
| HETP (structured packing) | 0.1-0.3 m |
| Vapor velocity (atmospheric, tray column) | 0.5-1.5 m/s |
| Vapor velocity (vacuum column) | 3-5 m/s |
| Pressure drop per tray (sieve) | 0.3-0.7 kPa |
| Pressure drop per theoretical plate (structured packing) | 0.05-0.15 kPa |
| Reboiler heat transfer coefficient | 800-1,500 W/m²·K |
| Condenser heat transfer coefficient | 300-800 W/m²·K |
| Design pressure (atmospheric column) | 1-2 bar |
| Design pressure (pressure column) | 2-20 bar |
| Service life (before major turnaround) | 5-15 years (inspection and cleaning cycle) |

## Safety

- **Flammable vapor explosion**: Hydrocarbon and solvent vapors form explosive mixtures at 1-10% in air. Ground and bond all metal vessels and piping. Use explosion-proof electrical equipment. Nitrogen purge before introducing flammables. Install flame arrestors on all vent lines.
- **Hot surfaces and boiling liquids**: Reboiler contents at 80-350°C. Insulate all hot surfaces to <60°C. Emergency shower within 10 m. Thermal gloves and face shield for sampling.
- **Toxic chemical exposure**: Chlorosilanes release HCl on moisture contact. Benzene and aromatic fractions are carcinogenic. Local exhaust ventilation at all sample ports. Respiratory protection for toxic distillates.
- **Pressure vessel safety**: Relief valve at 1.1× MAWP. Hydrostatic test at 1.5× design pressure before commissioning. Differential pressure monitoring — sudden increase signals flooding, reduce boilup immediately.
- **Column flooding**: Excessive vapor velocity causes liquid entrainment upward, separation fails, pressure drop spikes. Response: reduce reboiler heat immediately. Do NOT increase reflux (worsens flooding).
- **Static electricity**: Low-conductivity liquids flowing through pipes and packing generate static charge. Ground all metal. Limit filling velocity to <1 m/s. Use antistatic additives in fuels.

## See Also

- [Distillation](distillation.md) — distillation theory, types, and process design
- [Heat Exchanger](heat-exchanger.md) — shell-and-tube and plate exchanger construction
- [Reactor Vessel](reactor-vessel.md) — pressure vessel construction principles
- [Chemical Recovery](chemical-recovery.md) — solvent recovery by distillation
- [Solvents](solvents.md) — solvent production and purification

[← Back to Chemistry](index.md)
