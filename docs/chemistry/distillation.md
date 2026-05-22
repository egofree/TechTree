# Distillation

> **Node ID**: chemistry.distillation
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`ceramics.kilns`](../ceramics/kilns.md), [`mining`](../mining/index.md)
> **Enables**: [`silicon.purification`](../silicon/purification.md)
> **Timeline**: Years 20-35
> **Outputs**: distillation_capability, fractionated_chemicals

### Types of Distillation

**Simple distillation**:
Single vaporization-condensation step (1 theoretical plate). Heated vessel + condenser. Batch operation. Sufficient for rough separations: water from dissolved salts, alcohol concentration to ~40-50%. No reflux control. Fast setup — a copper pot with a condensing coil suffices. Yield and purity limited by single-stage equilibrium. Used for: water purification, crude alcohol concentration, essential oil steam distillation, solvent recovery from waste streams.

**Fractional distillation**:
Packed or plated column between boiler and condenser provides multiple equilibrium stages (5-50+ theoretical plates). Reflux ratio controls sharpness of separation. Batch or continuous operation. Used for petroleum fractions, alcohol purification to azeotrope (95.6%), chlorosilane separation for silicon purification, solvent purification. The workhorse of industrial chemical separation — accounts for 40-60% of capital cost in a typical chemical plant.

**Vacuum distillation**:
Reduce column pressure to 10-100 mmHg using a vacuum system (steam ejector or mechanical vacuum pump). Lowers boiling points by 50-150°C, enabling distillation of heat-sensitive compounds (fatty acids, vitamins, certain polymers, pharmaceutical intermediates) and high-boiling materials (heavy petroleum residues, waxes, long-chain alcohols). Column diameter increases at lower pressure because vapor specific volume expands. Typical application: atmospheric residue from crude distillation (bp >350°C) is vacuum-distilled to produce lubricating oil base stocks, waxes, and feedstock for catalytic cracking. Vacuum column operates at 10-30 mmHg with 0.3-0.5 m/s vapor velocity.

**Steam distillation**:
Inject live steam directly into the still pot. Water and the organic compound form a heterogeneous azeotrope — both boil at a temperature below either pure component's boiling point. The combined vapor pressure equals atmospheric pressure at a temperature lower than either boiling point alone. Essential oils (lavender, peppermint, eucalyptus, tea tree) are extracted this way at 95-100°C instead of their native 200-300°C boiling points, preserving thermally labile fragrance compounds. Equipment: steam boiler + still pot + condenser + Florentine flask (separates condensate into oil and water layers). Steam consumption: 2-5 kg steam per kg of organic product.

**Azeotropic distillation**:
Add an entrainer (third component) that forms a new, lower-boiling azeotrope with one component, breaking the original azeotrope. Example: ethanol-water azeotrope at 95.6% ethanol — add benzene or cyclohexane to form a ternary azeotrope (bp 64.9°C) that carries water overhead, leaving anhydrous ethanol (>99.5%) in the bottoms. The overhead ternary mixture separates into two liquid phases in a decanter — the entrainer-rich phase is returned as reflux. The entrainer is recovered and recycled. Widely used before molecular sieves became available. Disadvantage: benzene is carcinogenic; modern plants use cyclohexane or n-pentane as entrainer.

**Extractive distillation**:
Add a high-boiling solvent (extractive agent) that selectively alters relative volatility of the components. The extractive agent does not form an azeotrope — it stays in the liquid phase and preferentially associates with one component, making the other more volatile. Example: adding glycerol or ethylene glycol to ethanol-water feed increases water's effective boiling point, allowing ethanol to be drawn off as near-pure distillate without azeotrope interference. The extractive agent (now water-rich) exits the column bottoms and is separated from water in a second column, then recycled. Preferred over azeotropic distillation when the entrainer is non-toxic and readily available.

### Column Internals

**Bubble cap trays**:
Horizontal plates with riser tubes (50-75 mm tall) covered by slotted caps. Vapor rises through risers, bubbles under caps, and passes through slots into liquid flowing across the tray. Each tray provides approximately one theoretical plate (70-85% Murphree efficiency). Advantages: handles wide liquid/vapor flow ratio variations without leaking or flooding. Disadvantages: expensive to fabricate (complex cap geometry), high pressure drop (0.5-1.5 kPa per tray), heavy, traps liquid on shutdown. Used in petroleum refineries since the 1920s — still found in older installations. Tray spacing: 450-600 mm. Typical column: 20-40 bubble cap trays.

**Sieve trays**:
Flat perforated plates with 3-12 mm diameter holes on 12-25 mm triangular pitch (5-15% open area). Vapor rises through holes and contacts the liquid pool on the tray. Liquid flows to the next tray via downcomers (channels at the tray edge). Much simpler and cheaper than bubble caps. Lower pressure drop (0.3-0.7 kPa per tray). Disadvantage: narrow operating range. At low vapor flow (<60% of design), liquid weeps through the holes, reducing tray efficiency. At high vapor flow (>120% of design), liquid entrainment floods the tray above. Most common new tray installation. Efficiency: 60-80% Murphree.

**[Valve trays](../glossary/valve-trays.html)** (floating valve):
Perforated tray with movable valve caps (stamped metal discs with legs) that lift with vapor flow. At low vapor rates, valves partially close — preventing weeping. At high rates, valves fully open — allowing high throughput. Combines bubble-cap flexibility with sieve-tray low cost and low pressure drop. Dominant modern tray design (Glitsch Ballast Tray, Koch Float Valve). Pressure drop: 0.3-0.8 kPa per tray. Efficiency: 65-80% Murphree. Valve material: stainless steel (thin stamped discs).

**Random packing**:
Dumped ceramic or metal elements filling the column volume. Liquid distributes over packing surface as thin film; vapor flows through the interstitial voids. Lower pressure drop than trays (critical for vacuum distillation).

- **Raschig rings**: Simple hollow cylinders (length ≈ diameter), 25-50 mm size. Ceramic or metal. Oldest packing type. HETP: 0.4-0.6 m. Cheap but inefficient by modern standards. Liquid distribution degrades with height — requires redistribution every 3-4 m.
- **Pall rings**: Raschig rings with internal fingers and external tabs stamped from the wall. Improves liquid distribution and vapor flow through the ring interior. 30-50% lower HETP than Raschig rings. Metal or plastic. Most common random packing.
- **[Ceramic saddles](../glossary/ceramic-saddles.html)** (Intalox, Berl): Saddle-shaped elements. Better liquid distribution than rings because shape prevents nesting and channeling. HETP: 0.3-0.5 m. Used where ceramic resistance to corrosion is needed (acid distillation).

**Structured packing**:
Corrugated metal sheets arranged in precise geometric modules, stacked vertically. Creates uniform, well-defined channels for vapor-liquid contact. Very low HETP (0.1-0.3 m), very low pressure drop (0.05-0.15 kPa per theoretical plate). Essential for vacuum distillation where pressure drop must be minimized. Examples: Sulzer Mellapak (corrugated sheets at 30° or 45° angle, alternating direction per layer), Koch-Glitsch Flexipac. Expensive per unit volume but saves column height and energy. Installed in pre-formed modules (diameter matches column), stacked on support rings with liquid redistributors every 4-6 m.

### Column Design Fundamentals

**Minimum reflux ratio**: The lowest L/D (liquid returned to column ÷ distillate drawn off) that achieves the desired separation. Operating below this makes separation impossible regardless of column height. Determined from the intersection of the rectifying operating line with the equilibrium curve on a McCabe-Thiele diagram. Typical operation: 1.2-1.5× minimum reflux ratio. Higher reflux ratio produces purer distillate but costs more energy (reboiler duty is proportional to reflux + product draw).

**Theoretical plates**: Each ideal equilibrium stage where vapor and liquid achieve thermodynamic equilibrium. More plates = sharper separation = taller column. Estimated via McCabe-Thiele method: plot vapor-liquid equilibrium curve (y vs x, where y = vapor mole fraction, x = liquid mole fraction), draw rectifying and stripping section operating lines, step off stages between curve and 45° diagonal. Number of steps = number of theoretical plates. The feed plate is where the operating lines intersect.

**[HETP](../glossary/hetp.html)** (Height Equivalent to a Theoretical Plate): For packed columns, the height of packing needed for one theoretical plate. Raschig rings: 0.4-0.6 m. Pall rings: 0.3-0.4 m. Structured packing: 0.1-0.3 m. Total packing height = HETP × required theoretical plates. Add 20% safety margin for maldistribution effects.

**Feed tray location**: The optimal feed tray minimizes total plates required. Placing the feed too high wastes plates in the stripping section; too low wastes plates in the rectifying section. Determined from McCabe-Thiele diagram: the feed should enter at the tray where the operating lines intersect (the "pinch" region).

**Column diameter**: Set by vapor velocity. Too fast → flooding (vapor carries liquid upward, no separation). Too slow → poor vapor-liquid contact, weeping. Design at 50-80% of flooding velocity. Flooding velocity calculated from packing characteristics (packing factor), liquid-to-vapor ratio, and physical properties (densities, viscosities, surface tension). Typical vapor velocity: 0.5-1.5 m/s in tray columns, 1.0-2.5 m/s in packed columns at atmospheric pressure. Vacuum columns may run at 3-5 m/s.

**Column construction procedure**:
1. **Shell fabrication**: Roll steel plate to cylinder (2-10 m tall, 20-100 cm diameter). Weld longitudinal seam. Attach flanged top and bottom caps with gasketed joints.
2. **Internal fittings**: Weld support rings every 0.5-1 m. Install feed nozzle at calculated feed-tray height. Install thermowells at top, middle, bottom.
3. **Packing or trays**: Install trays with downcomers, or pour random packing / stack structured packing modules on support grids. Ensure uniform distribution.
4. **Reboiler**: Weld or bolt heated kettle (steam coil or fire-heated jacket) to column bottom. Size for 1.2-1.5× minimum boilup.
5. **Condenser**: Water-cooled shell-and-tube or coil condenser at top. Distillate collection with reflux splitter (controls reflux ratio).
6. **Leak test**: Pressurize to 0.3-0.5 bar gauge. Soap-test all joints. 30-minute hold with <5% pressure drop.
7. **Insulation**: 50-100 mm mineral wool with sheet metal cladding. Reduces heat loss, stabilizes temperature gradient, prevents burns.

### Worked Examples

**Example 1: Ethanol-water separation**:
Feed: 10% ethanol fermented wash at 100°C, 1 atm. Target: 95.6% azeotrope.
- Relative volatility α ≈ 2.5 (favorable). At azeotrope (95.6%), α = 1.0 (cannot separate further by simple distillation).
- McCabe-Thiele analysis at R = 2.5 (reflux ratio): ~15 theoretical plates required.
- Packed column with ceramic saddles (HETP 0.4 m): 15 × 0.4 = 6 m packing + 2 m disengagement = 8 m total column height. Diameter: 0.3 m for 100 L/h feed rate.
- Reboiler duty: (R + 1) × D × ΔHvap = 3.5 × D × 846 kJ/kg. Steam consumption ≈ 3-4 kg steam per kg ethanol.
- Breaking the azeotrope: molecular sieves (3Å zeolite beads adsorb water preferentially, regenerable at 200-300°C with dry gas purge) or extractive distillation with glycerol (adds 2-3 more columns).

**Example 2: Chlorosilane separation (silicon purification)**:
Feed: direct reaction of metallurgical-grade silicon + HCl gas at 300°C → mixture of trichlorosilane (TCS, SiHCl₃, bp 31.8°C), silicon tetrachloride (STC, SiCl₄, bp 57.6°C), dichlorosilane (DCS, SiH₂Cl₂, bp 8.2°C), and unreacted H₂.
- Three-column train operating at 2-3 bar to keep chlorosilanes liquid at ambient cooling temperatures:
  - **Column 1** (light ends): Strip H₂ gas (overhead, vented/recycled) and DCS (condensed at -30°C using brine refrigeration). Bottoms feed to Column 2.
  - **Column 2** (TCS product): TCS taken as distillate at 31.8°C. TCS/STC relative volatility ≈ 2.0. Requires ~25 theoretical plates for electronic-grade purity (99.999%). Structured packing (HETP 0.2 m): 5 m packing. Column diameter 0.5-1.0 m. This TCS feeds the Siemens polysilicon reactor.
  - **Column 3** (STC recovery): STC taken as distillate at 57.6°C. Bottoms (heavy chlorinated residues) are waste. STC recycled to the MG-Si reactor.
- Critical: All equipment must be dry (chlorosilanes hydrolyze violently to HCl + SiO₂ on moisture contact). Nitrogen-purged, sealed stainless steel (316L) systems with welded connections. No atmospheric vents.

**Example 3: Petroleum crude distillation (atmospheric)**:
Feed: preheated crude oil (350-380°C from tube-still furnace) enters as partially vaporized mixture.
- Column: 30-50 m tall, 3-8 m diameter, 30-50 actual trays (sieve or valve), operates at 1-2 bar slight positive pressure.
- Product cuts drawn at different heights:
  - Overhead: refinery gas (C₁-C₄, bp <40°C) — sent to gas plant for LPG recovery
  - Top draw: light naphtha (40-90°C) — gasoline blending, petrochemical feedstock
  - Second draw: heavy naphtha (90-180°C) — catalytic reformer feed for aromatics
  - Third draw: kerosene (180-260°C) — jet fuel, diesel blending
  - Fourth draw: diesel/gas oil (260-350°C) — diesel fuel, heating oil
  - Bottoms: atmospheric residue (bp >350°C) — sent to vacuum distillation or used as fuel oil
- Pumparounds: liquid side-draws cooled and returned at intermediate heights to remove heat and control vapor load. 2-3 pumparounds typical.
- Energy: crude furnace consumes ~2% of throughput as fuel. Overall refinery energy: 5-10% of crude input. Heat integration: cold crude preheated by hot product streams in shell-and-tube exchangers (crude preheat train) before entering the furnace — recovers 60-70% of product heat.

### Heat Integration

**Pinch analysis**: Plot composite heating and cooling curves (temperature vs. enthalpy) for all process streams. The pinch point is where hot and cold curves are closest (minimum ΔT). Design heat exchanger network: match hot streams above the pinch with cold streams above the pinch; match cold streams below with cold below. No heat should cross the pinch — doing so increases both heating and cooling utility demand. Typical minimum approach: 10-20°C. Energy savings from proper pinch design: 30-50% reduction in utility consumption.

**Multiple-effect distillation**: Overhead vapor from Column 1 serves as heating medium for Column 2 (operating at lower pressure, lower boiling point). Column 2 vapor heats Column 3 (lower still). Three-effect system reduces steam consumption ~60% versus single column. Trade-off: each effect requires larger heat transfer area (smaller ΔT), increasing capital cost. Economical for large throughput, close-boiling separations. Widely used in ethanol dehydration and seawater desalination.

**Vapor recompression (MVR)**: Compress overhead vapor to raise its condensation temperature above the reboiler temperature. Compressed vapor condenses in the reboiler, providing heat. Eliminates external steam and cooling water. Compressor energy ≈ 10-20% of the energy saved. Economical for close-boiling separations where ΔT between top and bottom is small (propane/propylene, isobutane/n-butane, wastewater organic removal). Mechanical compressor driven by electric motor or steam turbine.

### Bootstrap Sequence

1. **[Pot still](../glossary/pot-still.html)** (Year 1-5): Copper pot + condensing coil. Batch. 1 theoretical plate. Alcohol concentration to 40-50%, water purification, essential oil steam distillation. Fuel: wood or waste heat.
2. **[Packed batch column](../glossary/packed-batch-column.html)** (Year 5-15): Add 1-3 m ceramic Raschig rings or saddles. Reflux control via manual split of condensate. 5-10 theoretical plates. Solvent purification, coal tar light oil fractionation, ethanol to 85-90%.
3. **[Continuous fractional column](../glossary/continuous-fractional-column.html)** (Year 15-25): Feed at mid-point, continuous steam-heated reboiler, water-cooled condenser. 15-30 theoretical plates. Petroleum fractionation, chlorosilane purification, acid concentration.
4. **[Multi-product train with heat integration](../glossary/multi-product-train-with-heat-integration.html)** (Year 25+): Atmospheric + vacuum columns, side-draw fractions, pumparound cooling, crude preheat train, multiple-effect energy recovery. Full petroleum refining. Specialty chemical purification (pharmaceutical intermediates, electronic-grade solvents).

### Safety & Hazards

- **Hot and boiling liquids**: Reboiler contents at 80-350°C. Severe thermal burns on contact. Thermal gloves, face shields, splash guards on sample ports. Emergency shower within 10 m of operating column. Insulate all hot surfaces.
- **Flammable vapor explosion**: Hydrocarbon and solvent vapors form explosive mixtures at 1-10% in air. Ignition energy as low as 0.2 mJ (static spark). Bond and ground all metal vessels and piping. Vent column area. Explosion-proof electrical equipment (Class 1 Div 1 or 2). Never operate near open flames or hot work. Nitrogen purge before introducing flammables.
- **Toxic chemical exposure**: Chlorosilanes release HCl on moisture contact — corrosive to lungs, eyes, skin. Benzene and aromatic fractions are carcinogenic (leukemia risk with chronic exposure). Sulfuric acid mists from acid distillation. Local exhaust ventilation at all feed and product ports. Respiratory protection for toxic distillates. Emergency eyewash adjacent to column.
- **Pressure vessel safety**: Install pressure relief valve at 1.1× MAWP (maximum allowable working pressure). Rupture disc as secondary relief. Vacuum columns need wall thickness ≥3-5 mm steel for <1 m diameter to resist collapse. Hydrostatic test at 1.5× design pressure before commissioning. Column differential pressure monitoring — sudden increase signals flooding, reduce boilup immediately.
- **Reflux drum overfill**: Automated level control with high-level alarm and emergency dump valve. Overfill sends liquid to reboiler — can cause thermal runaway with reactive chemicals.
- **Column flooding**: Vapor velocity exceeds capacity, liquid entrains upward, separation fails, pressure drop spikes. Causes: excessive boilup, restricted downcomers, fouled packing. Response: reduce reboiler heat immediately. Do NOT increase reflux (worsens flooding).
- **Static electricity**: Flow of low-conductivity liquids (hydrocarbons, organic solvents) through pipes and packing generates static charge. Accumulated charge discharges as spark — ignition source. Ground all metal. Limit filling velocity to <1 m/s. Bond containers before transfer. Use antistatic additives in fuels.

 ---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*

## Column Design Parameters

**Height-to-diameter ratio**: Fractional distillation columns typically have H/D ratios of 10-30:1. This ratio ensures adequate separation stages while maintaining reasonable vapor velocity. Too tall and narrow (H/D > 30) leads to poor liquid distribution and channeling in packed columns. Too short and wide (H/D < 10) requires large diameter for vapor handling but provides few theoretical plates. For example, a column with 20 theoretical plates at HETP 0.4 m requires 8 m packing height; at H/D 15, the column diameter would be 0.53 m.

**Reflux ratio selection**: Reflux ratio (R = L/D, where L = reflux flow, D = distillate flow) is the primary operating variable controlling separation sharpness. Minimum reflux ratio (R_min) is the lowest value that achieves the specified separation, determined from the McCabe-Thiele diagram intersection of the rectifying line with the equilibrium curve. Operating at R_min requires infinite plates (impossible). Practical operation uses R = 1.2-1.5 × R_min. Higher R produces purer distillate but increases reboiler energy consumption proportionally (reboiler duty ∝ R + 1). Economic optimization balances energy cost (higher R) against capital cost (more plates at lower R).

**Number of theoretical plates**: Determined by McCabe-Thiele method for binary systems. Plot the vapor-liquid equilibrium (VLE) curve (y vs x), draw the 45° diagonal, construct operating lines for rectifying and stripping sections, step off stages between the curve and operating lines. For multicomponent mixtures, the Fenske-Underwood-Gilliland (FUG) method provides short-cut estimates. Typical plate counts: ethanol-water to azeotrope requires 15-25 plates, chlorosilane separation 25-35 plates, petroleum crude atmospheric distillation 30-50 plates.

## Petroleum Fractional Distillation

**Atmospheric distillation unit (ADU)**: The first processing step in a petroleum refinery. Crude oil preheated to 350-370°C in a tube-still furnace (fuel-fired, 70-80% thermal efficiency) enters the atmospheric distillation column as a partially vaporized mixture. The column operates at 1-2 atm slight positive pressure, with 30-50 actual trays. Product fractions drawn at different heights based on boiling range:

- Light naphtha overhead (40-90°C bp): gasoline blending component, petrochemical feedstock for steam cracking to ethylene
- Heavy naphtha side-draw (90-180°C): catalytic reformer feed (converted to high-octane aromatics: benzene, toluene, xylene)
- Kerosene side-draw (180-250°C): jet fuel (Jet A-1 freeze point -47°C, flash point 38°C minimum), illuminating kerosene, diesel blending
- Diesel/gas oil side-draw (250-320°C): diesel fuel (cetane number 40-55), heating oil, FCC (fluid catalytic cracking) feedstock
- Atmospheric residue bottoms (bp >350°C): feeds the vacuum distillation unit, or used as fuel oil and bitumen

**Vacuum distillation unit (VDU)**: Atmospheric residue (bp >350°C) would thermally crack (decompose) if distilled further at atmospheric pressure. The VDU operates at 10-20 mmHg (absolute), reducing boiling points by 150-200°C. This allows distillation of high-boiling materials at 350-400°C without thermal degradation. Products: vacuum gas oil (VGO, 350-540°C bp range, FCC or hydrocracker feed), lubricating oil base stocks (light, medium, heavy neutral grades), and vacuum residue (bp >540°C, used for bitumen/asphalt production or delayed coking feed).

## Vacuum Distillation Techniques

**Water aspirator**: The simplest vacuum source. Water flows through a Venturi nozzle, creating suction by the Bernoulli effect. Achieves 15-25 mmHg (limited by water vapor pressure at the water temperature: ~24 mmHg at 25°C). Sufficient for reducing boiling points by 50-100°C. No moving parts, inexpensive. Disadvantage: consumes large volumes of water (5-20 L/min) and cannot achieve deep vacuum.

**Rotary vane vacuum pump**: Mechanical pump with eccentrically mounted rotor and spring-loaded vanes. Achieves 0.01-1 mmHg (ultimate vacuum). Two-stage pumps reach 0.001 mmHg. Pumping speed 1-50 m³/hour. Oil-sealed (hydrocarbon vacuum oil lubricates vanes and seals). Suitable for laboratory and small industrial vacuum distillation. Oil must be changed regularly (contamination by solvent vapors degrades performance). Not suitable for corrosive vapors without cold traps.

**Steam ejectors**: Multi-stage steam ejector systems achieve 0.1-10 mmHg for large industrial vacuum columns. First-stage ejector uses 0.7-1.0 MPa steam, pulls vacuum to ~100 mmHg. Second stage pulls to ~10 mmHg. Third and fourth stages pull to 1-5 mmHg. Inter-stage condensers (water-cooled) remove condensed steam and vapors, reducing the load on subsequent stages. Advantages: no moving parts, handles large gas volumes, tolerates corrosive vapors. Disadvantage: high steam consumption (5-15 kg steam per kg of gas removed). Standard for petroleum VDU vacuum systems.

## Steam Distillation Applications

**Essential oil extraction**: Plant material (lavender flowers, peppermint leaves, eucalyptus foliage) loaded into a still and steam injected directly. Water and the volatile oil form a heterogeneous mixture that boils at a temperature below either pure component. Example: eugenol (clove oil, bp 254°C) co-distills with water at 99.5°C. The condensate separates in a Florentine flask: essential oil (lower density, floats on top) is collected while water returns to the still or is discarded. Steam consumption: 2-5 kg steam per kg of plant material. Yield varies enormously: lavender 0.5-1.5% oil by weight, cloves 15-20%.

**Heat-sensitive organic purification**: Compounds that decompose at their atmospheric boiling point can be distilled at reduced temperature by steam co-distillation. Glycerol (bp 290°C, decomposes above 200°C) can be steam-distilled at ~180°C. Fatty acids (bp >300°C) can be purified by steam stripping. The principle applies wherever immiscible water-organic systems allow reduced boiling temperature through combined vapor pressure.

## Distillation Control Systems

**Temperature control**: Product purity is maintained by controlling column temperatures. The temperature at the top of the column indicates distillate composition (for binary systems, the temperature directly maps to composition via the VLE curve). A temperature controller adjusts reflux ratio or reboiler heat to maintain constant overhead temperature. In multicomponent columns, a "sensitive tray" near the feed point is controlled rather than the top temperature, as it shows the strongest response to composition changes. Temperature measurement: Pt100 RTD or thermocouple in a thermowell inserted into the vapor space at the control tray. Accuracy ±0.5°C.

**Pressure control**: Column pressure affects relative volatility and tray capacity. Lower pressure generally improves relative volatility (easier separation) but reduces vapor density (may require larger diameter). Atmospheric columns: pressure controlled by a vent or nitrogen blanketing system. Vacuum columns: pressure controlled by regulating vacuum pump or steam ejector operation. Pressure fluctuations cause tray flooding or weeping, destabilizing the separation.

**Level control**: Liquid levels must be maintained in the reboiler (to prevent dry firing or flooding the bottom trays) and the reflux drum (to provide adequate residence time for phase separation and pump suction). Level controllers adjust bottom product draw rate (reboiler level) and distillate draw rate (reflux drum level). Cascade control: level controller output becomes the setpoint for the flow controller on the draw valve.

**Advanced control**: Model predictive control (MPC) optimizes the entire column operation by predicting the effect of feed composition changes, ambient temperature variations, and other disturbances on product quality. MPC adjusts multiple manipulated variables (reboiler heat, reflux ratio, feed tray position) simultaneously to maintain product specifications while minimizing energy consumption. Benefits: 5-15% energy reduction compared to conventional PID control, tighter product quality control, and smoother operation during feed changes.

## Distillation Equipment Construction

**Shell construction**: Column shells are fabricated from rolled steel plate (carbon steel for non-corrosive service, 304L or 316L stainless steel for corrosive chemicals). Plate thickness: 6-25 mm depending on diameter and design pressure. Shells with diameter >1 m typically require post-weld heat treatment to relieve residual stresses. For vacuum service, shell thickness is governed by external pressure collapse resistance rather than internal pressure: a 1 m diameter column at 10 mmHg requires minimum 6 mm wall thickness with stiffening rings at 1-2 m intervals.

**Condenser design**: Shell-and-tube condenser is standard. Cooling water flows on the shell side (lower pressure drop, easier to clean), vapor condenses inside the tubes. Tube material: 316L stainless steel or copper-nickel alloy for corrosion resistance. Water inlet temperature 20-30°C, outlet 35-45°C (limited to prevent scale deposition). Temperature approach (condensing temperature minus water outlet temperature): 5-15°C. Heat transfer coefficient: 300-800 W/m²·K for condensing organic vapors. Condenser area sized for total condensation of overhead vapor (reflux + product).

**Reboiler design**: Kettle reboiler (most common): liquid from the column bottom enters a shell-side pool heated by tube-side steam (or hot oil). Vapor rises back to the column, liquid product exits from the bottom. Steam pressure: 0.3-1.0 MPa (saturation temperature 144-184°C). Heat transfer coefficient: 800-1500 W/m²·K for boiling organic liquids. Thermosiphon reboiler (vertical tube, natural circulation): more compact, better for clean services. Forced circulation reboiler (pump circulates liquid through the heater): handles viscous or fouling fluids.

**Insulation and heat loss**: All distillation columns and associated piping must be insulated to minimize heat loss. Mineral wool or calcium silicate insulation, 50-100 mm thickness, with aluminum sheet metal cladding for weather protection. Heat loss from an insulated column: 50-200 W/m² of external surface area, depending on operating temperature and ambient conditions. Uninsulated, a column operating at 150°C loses 1000-2000 W/m², destabilizing the temperature gradient and wasting energy. Insulation also provides personnel protection (surface temperature <60°C to prevent burns).

## Column Troubleshooting

**Flooding diagnosis**: Column flooding is indicated by a sudden, large increase in differential pressure across the column (normal ΔP: 0.3-1.0 kPa per tray, flooded: 2-5× normal). Causes: (1) excessive vapor flow (reboiler too hot), (2) excessive liquid flow (reflux too high for the vapor rate), (3) fouled trays or packing (debris, polymerized material, corrosion products), (4) downcomer blockage (prevents liquid from draining to the tray below). Response: immediately reduce reboiler heat. Do not increase reflux (this adds more liquid to an already flooded column, worsening the situation). If caused by fouling, the column must be shut down, drained, and mechanically cleaned.

**Channeling in packed columns**: Liquid maldistribution causes some areas of the packing to run dry (vapor passes through with no liquid contact, no separation) while other areas flood. Causes: inadequate liquid distributor design, damaged distributor, or packing installation not level. Symptoms: poor separation despite adequate packing height, asymmetrical temperature profile. Prevention: liquid distributors with >40 pour points per m² of column cross-section, verified by water distribution test before packing installation. Redistributors every 3-4 m of packed height to reset the liquid pattern.

**Foaming**: Some systems (amine gas treating, caustic washing, fermentation products) generate stable foam that traps vapor and liquid, reducing tray efficiency and capacity. Antifoam agents (silicone oil or polyglycol, 5-50 ppm) injected continuously or as needed. Mechanical foam breakers (centrifugal or impact type) in the vapor space above the top tray. Foam detection: differential pressure cell across the foam layer or conductivity probe. Severe foaming can carry liquid overhead into the condenser, contaminating the distillate product.

## Distillation Economics

**Energy costs**: Distillation is the most energy-intensive separation method in the chemical industry, accounting for 40-60% of a typical plant's energy consumption. Reboiler duty is the dominant cost. For a typical binary column separating 10 tonnes/hour of feed with reflux ratio 3:1, reboiler steam consumption is approximately 15-25 tonnes/hour. At $20/tonne steam, annual energy cost is $3-5 million. A 10% reduction in reflux ratio (from 3.0 to 2.7) saves 10% reboiler energy with minimal impact on product purity if the column has excess theoretical plates.

**Capital costs**: Carbon steel distillation column: $50,000-200,000 per meter of height and $100,000-500,000 per meter of diameter (2020 basis, depending on internals, pressure rating, and alloy). A 20 m tall × 1 m diameter sieve tray column with 30 trays, reboiler, condenser, reflux drum, pumps, and instruments: $500,000-2,000,000 installed. Stainless steel doubles the cost. Glass-lined or alloy construction triples it. Packed columns are 10-30% cheaper than trayed columns for the same separation due to lower height (better HETP).

**Optimization tradeoff**: Increasing the number of theoretical plates (taller column, more capital) allows operation at lower reflux ratio (less energy, lower operating cost). The economic optimum occurs where the annualized capital charge for the additional plates equals the annual energy savings from reduced reflux. This tradeoff is evaluated by plotting total annualized cost (capital + energy) versus number of plates, finding the minimum. Typical result: the optimum reflux ratio is 1.2-1.5× minimum reflux, and the optimum number of plates is 2-3× the minimum number.
Distillation remains the backbone of chemical separation worldwide, and its mastery is prerequisite for any civilization rebuilding its chemical industry from basic principles.
