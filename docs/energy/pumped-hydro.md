# Pumped Hydroelectric Storage

> **Node ID**: energy.storage.pumped-hydro
> **Domain**: [Energy](./)
> **Dependencies**: `energy.storage`, `energy.gravity`, `machine-tools`, `metals.iron-steel`
> **Enables**: `energy.electricity` (grid stabilization), `silicon` (reliable power for continuous processes)
> **Timeline**: Years 25-40
> **Outputs**: grid_storage, peak_shaving, frequency_regulation

### Overview

Pumped hydroelectric storage (pumped hydro) is the only practical method for storing energy at the scale required by an industrial civilization. During periods of surplus power generation, water is pumped from a lower reservoir to an upper reservoir. During periods of high demand, the water is released back through a turbine to generate electricity. It is a mechanical battery using water and elevation — simple in principle, massive in scale, and unmatched in longevity (plants routinely operate for 50-100 years). Round-trip efficiency is 70-85%, making it the most efficient large-scale storage technology available.

### Operating Principle

**Pumping mode** (charging):
- Surplus electrical power drives a pump-motor unit. Water is drawn from the lower reservoir and pumped uphill to the upper reservoir. The pump adds gravitational potential energy to the water: E = ρ × g × h × V, where ρ = water density (1000 kg/m³), g = 9.81 m/s², h = elevation difference between reservoir surfaces, V = volume pumped.
- Pumping is typically done during off-peak hours (night) when base-load generators (steam, nuclear) have surplus capacity.

**Generating mode** (discharging):
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

**Francis pump-turbine** (most common):
- A Francis turbine runner operates efficiently in reverse as a centrifugal pump. The same spiral casing, runner, and draft tube serve both modes. Rotation direction reverses between pumping and generating.
- **Head range**: 50-700 m. Most pumped-hydro installations operate in the 100-500 m head range.
- **Efficiency**: 85-92% as turbine, 80-90% as pump. Round-trip efficiency: 70-85% (product of pump and turbine efficiencies, less hydraulic losses and motor/generator losses).
- **Operating speed**: 300-1000 RPM (synchronous with electrical grid frequency). Large-diameter runners for high-flow, low-head sites; smaller runners for high-head sites.

**Operating transitions**:
- Pumping to generating: Stop the unit, dewater the runner (drain water from casing), reverse rotation direction, refill the runner, re-synchronize to grid. Transition time: 5-15 minutes.
- Generating to pumping: Reverse of above. Similar transition time.
- Modern units can transition faster with advanced control systems, but the physical reversal of a large rotating machine takes time.

**Three-machine sets** (older installations):
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
 - **Dam and civil engineering foundations**: [Foundations](../foundations/)

---

*Part of the [Bootciv Tech Tree](../) • [Energy](./) • [All Domains](../)*
