# Pumped Hydroelectric Storage

> **Node ID**: energy.storage.pumped-hydro
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.storage`](storage.md), [`energy.gravity`](gravity.md), [`machine-tools`](../machine-tools/index.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`energy.electricity`](electricity.md) (grid stabilization), [`silicon`](../silicon/index.md) (reliable power for continuous processes)
> **Timeline**: Years 25-40
> **Outputs**: grid_storage, peak_shaving, frequency_regulation

### Overview

Pumped hydroelectric storage (pumped hydro) is the only practical method for storing energy at the scale required by an industrial civilization. During periods of surplus power generation, water is pumped from a lower reservoir to an upper reservoir. During periods of high demand, the water is released back through a turbine to generate electricity. It is a mechanical battery using water and elevation — simple in principle, massive in scale, and unmatched in longevity (plants routinely operate for 50-100 years). Round-trip efficiency is 70-85%, making it the most efficient large-scale storage technology available.

### Operating Principle

**[Pumping mode](../glossary/pumping-mode.html)** (charging):
- Surplus electrical power drives a pump-motor unit. Water is drawn from the lower reservoir and pumped uphill to the upper reservoir. The pump adds gravitational potential energy to the water: E = ρ × g × h × V, where ρ = water density (1000 kg/m³), g = 9.81 m/s², h = elevation difference between reservoir surfaces, V = volume pumped.
- Pumping is typically done during off-peak hours (night) when base-load generators (steam, nuclear) have surplus capacity.

**[Generating mode](../glossary/generating-mode.html)** (discharging):
- Water is released from the upper reservoir through a penstock to a turbine-generator unit. The turbine extracts the gravitational potential energy, driving the generator to produce electricity. Spent water returns to the lower reservoir.
- Generation occurs during peak demand hours (day) when electricity is most valuable.

**Reversible pump-turbine**: Modern installations use a single machine that operates as a turbine in one direction of rotation and as a pump in the opposite direction. This eliminates the need for separate pump and turbine units, reducing cost and civil works complexity. The motor-generator operates as a motor during pumping and as a generator during generation — the same electrical machine, different operating mode.

### Energy Storage Capacity

**Energy stored**: E = ρ × g × h × V × η

Where:
- ρ = 1000 kg/m³ (water density)
- g = 9.81 m/s² (gravitational acceleration)
- h = head (elevation difference between upper and lower reservoir water surfaces, in meters)
- V = useful volume of upper reservoir (m³) — not total capacity, but the volume between maximum and minimum operating levels
- η = round-trip efficiency (0.70-0.85)

**Examples**:
- 100 m head, 100,000 m³ reservoir: E = 1000 × 9.81 × 100 × 100,000 × 0.75 / 3.6 × 10⁶ ≈ 20,400 kWh ≈ 20.4 MWh
- 300 m head, 1,000,000 m³ reservoir: E = 1000 × 9.81 × 300 × 1,000,000 × 0.75 / 3.6 × 10⁶ ≈ 613,000 kWh ≈ 613 MWh
- 500 m head, 10,000,000 m³ reservoir: E ≈ 10.2 GWh — enough to supply a small city for several hours

**Energy density comparison**: Even at 500 m head, water stores only ~1.36 kWh per cubic meter (before efficiency losses). Pumped hydro requires enormous volumes of water and land. It is viable only where geography provides natural elevation differences.

### Reversible Pump-Turbines

**[Francis pump-turbine](../glossary/francis-pump-turbine.html)** (most common):
- A Francis turbine runner operates efficiently in reverse as a centrifugal pump. The same spiral casing, runner, and draft tube serve both modes. Rotation direction reverses between pumping and generating.
- **Head range**: 50-700 m. Most pumped-hydro installations operate in the 100-500 m head range.
- **Efficiency**: 85-92% as turbine, 80-90% as pump. Round-trip efficiency: 70-85% (product of pump and turbine efficiencies, less hydraulic losses and motor/generator losses).
- **Operating speed**: 300-1000 RPM (synchronous with electrical grid frequency). Large-diameter runners for high-flow, low-head sites; smaller runners for high-head sites.

**Operating transitions**:
- Pumping to generating: Stop the unit, dewater the runner (drain water from casing), reverse rotation direction, refill the runner, re-synchronize to grid. Transition time: 5-15 minutes.
- Generating to pumping: Reverse of above. Similar transition time.
- Modern units can transition faster with advanced control systems, but the physical reversal of a large rotating machine takes time.

**[Three-machine sets](../glossary/three-machine-sets.html)** (older installations):
- Separate pump, turbine, and motor-generator on a common shaft. Allows simultaneous starting of pump while turbine is stopped (the turbine acts as a starting motor via water filling). Simpler individual machines but more complex civil works (three machines in one powerhouse). Largely superseded by reversible units.

### Upper and Lower Reservoirs

**Upper reservoir**:
- Natural lake, existing reservoir, or purpose-built basin on elevated ground. Must be watertight — lined with clay, concrete, or geomembrane if the natural geology is permeable.
- Operating volume determines energy storage capacity. The larger the volume between full and minimum drawdown levels, the more energy stored.
- Water level fluctuates daily — the reservoir cycles between full (after night pumping) and near-empty (after peak generation). Earth slopes must be stable under repeated wetting/drying cycles.
- Spillway for flood protection — the upper reservoir must never overtop.

**Lower reservoir**:
- Natural lake, river, or purpose-built basin downstream. Often shares water with the upper reservoir (the system is essentially closed-loop — water circulates between the two reservoirs with only minor losses to evaporation and seepage).
- Must have sufficient capacity to receive the full upper reservoir volume without flooding downstream.
- Can double as a cooling water source or recreation area.

**Site selection**:
- Elevation difference (head) is the primary factor — higher head = more energy per cubic meter of water. Sites with 100-500 m of head over a short horizontal distance are ideal (steep terrain near rivers or coastal cliffs).
- Geology: Stable rock formations for dam foundations and underground powerhouse. Impermeable rock or clay to minimize reservoir seepage. Seismic stability — dams must withstand earthquakes.
- Water supply: While pumped-hydro is essentially a closed loop, initial filling requires water, and ongoing evaporation and seepage must be replaced. A reliable water source (stream, river) at the lower reservoir level is needed.

### Dam Construction

**Upper reservoir dam**:
- Height determined by storage requirements and topography. Typical heights: 10-100 m for purpose-built basins.
- **Earthfill dam**: Compacted earth and rockfill with clay core for watertightness. Most common for upper reservoirs. Requires sufficient impervious material (clay) near the site.
- **Concrete gravity dam**: Massive concrete structure that resists water pressure by its own weight. Suitable where bedrock is strong and available at the surface.
- **Concrete arch dam**: Curved wall transfers water pressure to the canyon walls. Very efficient use of concrete — requires strong rock abutments on both sides. Not applicable to broad valley sites.
- **Roller-compacted concrete (RCC)**: Lean concrete placed in thin layers and compacted with vibratory rollers. Faster and cheaper than conventional concrete. Increasingly common for medium-height dams.

**Seepage control**:
- Grout curtain: Drill holes and inject cement grout into the rock foundation beneath the dam to fill fractures and reduce seepage.
- Cutoff trench: Excavate a deep trench into impermeable material below the dam base and backfill with clay or concrete.
- Drainage blanket: Layer of gravel and drain pipes downstream of the dam core to safely collect and discharge seepage water.

### Head Requirements

- **Minimum practical head**: ~50 m. Below this, the energy density is too low — enormous reservoir volumes are needed for useful storage.
- **Optimal head range**: 100-500 m. Balances civil works cost (lower heads require larger reservoirs and larger-diameter penstocks) against equipment cost (higher heads require stronger penstocks and higher-pressure pump-turbines).
- **Maximum head**: ~700-1000 m with multi-stage pump-turbines. Single-stage Francis machines become impractical above ~600-700 m due to excessive runner peripheral speed and cavitation risk. Multi-stage machines stack two or more runners on a common shaft, each handling a fraction of the total head.

### Grid Applications

**Peak shaving**: Store cheap off-peak power and generate during peak demand periods. Economics depend on the price spread between off-peak and peak electricity — the wider the spread, the more profitable pumped hydro.

**Frequency regulation**: Pumped-hydro units can respond to grid frequency deviations within seconds by adjusting generation or pumping load. Fast response capability makes them valuable for grid stability, especially in systems with intermittent generation (wind, solar).

**Grid stabilization**: Acts as both load (when pumping) and generator (when discharging). Absorbs surplus generation (preventing overvoltage and frequency rise) and fills generation gaps (preventing undervoltage and underfrequency). The ability to switch between pumping and generating provides bidirectional grid support.

**Black start**: Pumped-hydro plants can restart the grid after a total blackout if the upper reservoir is full. Water release generates power to start other generators, which then restart the rest of the system.

**Capacity factor**: Typical pumped-hydro units cycle daily. Annual capacity factor: 10-25% (not continuously generating — spends significant time pumping or idle). High capital cost but very low operating cost per cycle.

### Safety and Hazards

- **Dam failure**: Both upper and lower reservoir dams must be designed and maintained to prevent catastrophic failure. A dam breach at the upper reservoir releases the full stored volume downhill — potentially devastating. Regular inspection (annual visual, detailed engineering every 5-10 years), instrumentation (piezometers to monitor seepage, survey markers to detect settlement), and emergency action plans.
- **Penstock rupture**: The penstock (pipe connecting upper reservoir to powerhouse) operates at high pressure. A rupture releases the full static head of water through the breach. Steel penstocks require regular inspection for corrosion, weld cracks, and wall thinning. Pressure relief valves and emergency shutdown gates.
- **Drowning**: Reservoirs, intakes, spillways, and tailraces are drowning hazards. Fencing, signage, and restricted access around all water features. Life rings and throw lines at access points.
- **Confined spaces**: The powerhouse, penstock gallery, and valve chambers are confined spaces. Atmospheric testing (oxygen, hydrogen sulfide, carbon monoxide) before entry. Ventilation, rescue equipment, and buddy system required.
- **Pump-turbine runaway**: If load is lost during generating mode and the guide vanes fail to close, the unit accelerates to runaway speed. Overspeed trip bolts and independent guide-vane closing systems prevent this. Test all protection systems regularly.

### Cross-References

- **Water turbines for generating mode**: [water-turbines.md](water-turbines.md)
- **Energy storage overview**: [storage.md](storage.md)
- **Grid infrastructure**: [electricity.md](electricity.md)
 - **Dam and civil engineering foundations**: [Foundations](../foundations/index.md)

### Reversible Pump-Turbine Design

The Francis-type reversible pump-turbine is the standard machine for pumped hydro. The runner (3-6 m diameter for medium installations) has curved vanes that function efficiently in both directions of rotation. In generating mode, water enters radially through a spiral casing, passes through adjustable guide vanes (wicket gates) that control flow, turns 90° through the runner, and exits axially into the draft tube. In pumping mode, the sequence reverses: the motor drives the runner in the opposite direction, drawing water up through the draft tube and discharging radially through the spiral casing into the penstock.

Operating speed for grid-connected units must be synchronous: 300, 333, 375, 428, 500, 600, 750, or 1000 RPM for 50 Hz systems (360, 400, 450, 514, 600, 720, 900, 1200 RPM for 60 Hz), determined by the formula N = 120f/p where f is grid frequency and p is number of pole pairs. The choice of speed depends on head and flow: high-head sites use higher-speed, smaller runners; low-head sites need slower, larger-diameter runners to avoid cavitation.

Generator-motor efficiency runs 95-98% in both modes. Combined with hydraulic efficiency of 85-92% for the pump-turbine, this gives the overall round-trip efficiency of 70-85%. Large units (100+ MW) tend toward the upper end of each range due to reduced relative losses. The motor-generator is typically a vertical-shaft synchronous machine mounted directly above the pump-turbine, with the shaft running through the bearing housing. Thrust bearing (supports the entire rotating mass plus hydraulic downthrust) is one of the most critical components: Kingsbury or tilting-pad type, oil-lubricated, rated for loads of 500-5000 tonnes depending on unit size.

### Penstock Construction

The penstock carries water between the upper reservoir and the powerhouse under full static head pressure. Material and construction depend on head and diameter:

**[Wooden stave pipe](../glossary/wooden-stave-pipe.html)** (suitable for low to medium head, up to 50-100 m):
- Construction: Douglas fir or redwood staves (tangential-cut boards), 75-150 mm thick, assembled into a circular pipe with flat steel bands tightened around the exterior. Band spacing: 150-300 mm for low pressure, 75-150 mm for higher pressure. Diameter up to 3 m practical.
- Joints between staves swell when wet, creating a watertight seal. The wood must be kept moist to maintain the seal; drying causes leakage.
- Advantages: No steel required for the pipe body (only bands). Low friction coefficient (Hazen-Williams C = 110-120). Resistant to corrosion and mild acidic water.
- Limitations: Maximum pressure limited by band strength and stave thickness. Not suitable above ~1 MPa internal pressure. Requires continuous maintenance of bands and protective coating.

**[Steel penstock](../glossary/steel-penstock.html)** (medium to high head, standard for most installations):
- Welded steel plate construction, 6-25 mm wall thickness depending on diameter and head. Steel grade: mild steel (yield strength 250-350 MPa) or high-strength low-alloy steel (yield 350-550 MPa) for high-head applications.
- Wall thickness calculation: t = P × D / (2 × σ × η + P), where P = internal pressure (static head × 0.0098 MPa/m + water hammer allowance), D = diameter, σ = allowable stress (yield / safety factor, typically 1.5-2.0), η = weld joint efficiency (0.85-1.0).
- Concrete anchor blocks every 30-50 m on sloped sections to prevent penstock movement from thermal expansion, water hammer, and gravity loads. Expansion joints or telescopic sleeves accommodate longitudinal thermal movement (0.012 mm/m/°C for steel).
- Corrosion protection: Interior coating with coal tar epoxy or cement mortar lining. Exterior painting or wrapping. Cathodic protection (sacrificial zinc or magnesium anodes, or impressed current) for buried sections.
- Pressure rating must include water hammer allowance. Sudden closure of turbine guide vanes can generate a pressure surge of 10-50% above static head, depending on closure time and penstock length. Surge tanks or pressure relief valves mitigate this.

### Surge Tank

A surge tank is a vertical shaft or standpipe connected to the penstock near the powerhouse, designed to absorb pressure transients from rapid load changes:

- **Simple surge tank**: Vertical cylindrical shaft, 2-5 m diameter, extending 10-30 m above the headwater level (maximum surge height). Open to atmosphere at the top. When turbine load is suddenly rejected (guide vanes close), the water column in the penstock decelerates. Without a surge tank, the kinetic energy of the decelerating water column converts to a pressure spike (water hammer) that can rupture the penstock. The surge tank provides an expansion volume: water rises in the shaft, absorbing the transient, then oscillates back and forth with decreasing amplitude until friction damps the oscillation (typically 2-5 minutes to settle).
- **Sizing**: Surge tank cross-sectional area must be large enough to keep the maximum surge level below the tank top and the minimum surge level above the penstock connection. A rule of thumb: the surge tank area should be 1.5-3× the penstock cross-sectional area. The volume between maximum and minimum surge levels should accommodate the full kinetic energy of the water column in the penstock (½ρALv², where A is penstock area, L is penstock length, v is water velocity).
- **Restricted orifice surge tank**: An orifice plate at the base of the surge tank throttles flow in and out, providing additional damping. The orifice area is typically 30-50% of the penstock area. Higher damping means faster oscillation decay but more energy loss during transients.

### Head Loss Calculation

Friction losses in the penstock reduce the effective head available at the turbine. The Hazen-Williams formula provides a practical estimate:

h_f = 10.67 × Q^1.852 / (C^1.852 × D^4.87)

Where:
- h_f = friction head loss per meter of penstock length (m/m)
- Q = flow rate (m³/s)
- C = Hazen-Williams roughness coefficient (100 for old steel, 120 for new steel, 140 for smooth concrete, 110-120 for wooden stave)
- D = internal pipe diameter (m)

For a penstock of total length L, total head loss: H_f = h_f × L. The net effective head at the turbine is H_gross - H_f, where H_gross is the elevation difference between reservoir surfaces. Penstock design targets head loss below 5-10% of gross head to maintain acceptable efficiency. Increasing diameter reduces head loss but raises material and construction costs. The economic diameter is the point where the present value of energy lost to friction equals the incremental cost of a larger pipe.

Minor losses from bends, valves, and transitions add 5-15% to the straight-pipe friction loss. Each bend contributes a loss of K × v² / (2g), where K = 0.1-0.5 depending on bend angle and radius.

### Site Selection Criteria

Practical pumped hydro site evaluation requires matching four parameters:

- **Head**: 50-1000 m. Higher head is better: energy stored per unit volume scales linearly with head, so a 500 m head site stores 5× the energy of a 100 m site per cubic meter of water. Sites below 50 m require impractically large reservoir volumes. Above 700 m, single-stage pump-turbines reach their limits and multi-stage machines are needed.
- **Flow / storage volume**: Minimum continuous flow of 0.1 m³/s for initial filling and makeup water. Storage volume determined by upper reservoir surface area × drawdown depth. A 10-hectare reservoir (100,000 m²) with 5 m drawdown holds 500,000 m³ of usable storage.
- **Horizontal distance between reservoirs**: Shorter is better. The ratio of head to horizontal distance (the "head-to-distance ratio") determines penstock length and cost. A site with 300 m head over 1 km horizontal distance (ratio 0.3) is far more economical than 300 m over 5 km (ratio 0.06). Steep terrain near river valleys or coastal cliffs offers the best ratios.
- **Geological stability**: Bedrock capable of supporting dam foundations and (for underground powerhouses) stable rock for tunneling. No active faulting. Low permeability for the upper reservoir basin (or economically amendable with clay or geomembrane lining). Seismic risk assessment mandatory.

### Powerhouse Design

The powerhouse houses the pump-turbine, motor-generator, and associated equipment. For a pumped hydro installation, it is typically located at the lower reservoir level, either surface or underground:

- **Surface powerhouse**: Concrete structure at the base of the head. Lower construction cost than underground. Suitable when the lower reservoir has suitable terrain adjacent to the penstock outlet. The turbine pit, generator floor, and auxiliary equipment rooms are arranged vertically. Crane capacity: 50-200 tonnes for installing and maintaining the rotating assembly.
- **Underground powerhouse**: Excavated cavern in stable rock, accessible by tunnel. Unaffected by surface weather, flooding, or landslides. Permits shorter penstock runs (the tunnel to the upper reservoir can follow the most direct underground route). Common for high-head installations in mountainous terrain. Cavern dimensions for a 100 MW unit: approximately 20 m wide × 40 m tall × 50 m long. Requires ventilation shaft and access tunnel.
- **Auxiliary systems**: Cooling water system for generator bearings and transformers (heat exchanger using lower reservoir water). Compressed air system for turbine dewatering (blowing water out of the runner to reduce drag when spinning in air during pump startup). Governor system (hydraulic actuator controlling wicket gate position to regulate turbine speed and power output).

### Environmental Considerations

Pumped hydro storage has a large physical footprint and several environmental impacts to manage:

- **Reservoir footprint**: Upper and lower reservoirs inundate land. A 1 million m³ reservoir covering 10 hectares displaces that land from other use. Reservoir banks must be stabilized against erosion from daily water level fluctuations (the upper reservoir cycles through its full drawdown range daily, creating a 5-15 m "bathtub ring" of exposed shoreline susceptible to wave erosion).
- **Water temperature and quality**: Pumped storage operation mixes water between reservoirs, potentially transferring warm surface water to deeper, cooler zones. Stratification patterns in the lower reservoir may be disrupted, affecting aquatic ecosystems. In tropical or temperate climates, the mixing can increase dissolved oxygen in deeper water (beneficial) or redistribute nutrients and sediment (potentially harmful).
- **Evaporation losses**: Open reservoirs lose water to evaporation at 2-6 mm per day depending on climate (arid regions lose more). For a 10-hectare upper reservoir in a semi-arid climate: 10,000 m² × 4 mm/day = 40 m³/day lost, or ~14,600 m³/year. This must be replaced from a water source at the lower reservoir level. Net consumptive water use is modest compared to thermal power plant cooling but is not zero.
- **Fish passage**: If the lower reservoir is on a river, fish passage (fish ladders or lifts) around the lower dam may be required to maintain migratory fish populations. Pump intakes must have screens to prevent fish entrainment.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
