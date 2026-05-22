# Energy Storage & Diversification

> **Node ID**: energy.storage
> **Domain**: [Energy Storage & Diversification](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`energy`](index.md), [`metals`](../metals/index.md)
> **Timeline**: Years 15-200+
> **Outputs**: lead_acid_batteries, grid_infrastructure, ups_systems, hydroelectric_power, wind_power

## Problem

Semiconductor fabrication equipment cannot tolerate power interruptions — a power glitch during a crystal growth run or lithography exposure destroys expensive work-in-progress. Energy storage provides buffer capacity, and diversification prevents single-source dependency.

## Technologies & Systems

### Lead-Acid Battery

**Chemistry**:
- **Discharge**: Pb (anode) + PbO₂ (cathode) + 2H₂SO₄ → 2PbSO₄ + 2H₂O (cell voltage: 2.05V nominal)
- **Charge**: Reverse reaction — apply external voltage >2.4V per cell → convert PbSO₄ back to Pb and PbO₂, regenerate H₂SO₄.
- **Electrolyte**: 30-40% sulfuric acid (H₂SO₄) in water. Density indicates state of charge: fully charged = 1.265 g/cm³, discharged = 1.120 g/cm³. Measure with hydrometer (glass float in electrolyte sample — calibrated markings indicate density/charge state).

**Construction**:
- **Plates**: Lead grids (cast or expanded from lead sheet, 3-5 mm thick, with lattice openings). Paste fill: PbO (lead oxide) + H₂SO₄ + water → paste. Apply paste to grids. Cure 24-48 hours (paste converts to Pb₃O₄ and PbSO₄). Form (electrochemically convert): Positive plates → PbO₂ (brown), negative plates → Pb (gray spongy lead). Typical plate dimensions: 10-20 cm × 10-20 cm × 0.3-0.5 cm.
- **Assembly**: Stack alternating positive and negative plates with separators between (porous rubber, PVC, or glass fiber mat — prevents electrical contact while allowing ion flow). Connect all positives in parallel (lead bus bar), all negatives in parallel. Insert into cell container (hard rubber or polypropylene box, acid-resistant). 3 cells in series = 6V battery, 6 cells = 12V.
- **Capacity**: Measured in ampere-hours (Ah) at 20-hour discharge rate. Example: 100 Ah battery delivers 5A for 20 hours. Higher discharge rates reduce effective capacity (Peukert's law: capacity decreases non-linearly with increasing current). Energy density: 25-35 Wh/kg.

**Charging**:
- **Constant voltage**: Apply 2.35-2.45V per cell. Current initially high, tapers as battery charges. Full charge in 8-14 hours. Monitor electrolyte density — stop charging when density reaches 1.265 g/cm³ and stabilizes.
- **Equalizing charge**: Periodic overcharge (2.5V per cell for 1-2 hours after full charge) to equalize cell voltages and mix electrolyte (prevents acid stratification). Only for flooded (wet) batteries.
- **Gassing**: At >2.4V per cell, electrolysis of water begins → H₂ + O₂ gas. Ventilate battery rooms (hydrogen explosive at 4-74% in air). Top up with distilled water periodically to replace lost water. NEVER add acid.

**Sizing for backup power**:
- Determine critical load (W) and required backup time (hours). Calculate required energy: E = P × t (Wh). Battery capacity: C = E / (V × DOD × η), where V = battery voltage, DOD = depth of discharge (maximum 50-80% for lead-acid — deeper discharge shortens life), η = inverter efficiency (~0.85-0.95).
- Example: 2 kW critical load, 4-hour backup. E = 2000 × 4 = 8000 Wh. At 48V system, 50% DOD, 90% efficiency: C = 8000 / (48 × 0.5 × 0.9) = 370 Ah. This requires ~370 kg of lead-acid batteries (at 25 Wh/kg). Heavy, but achievable.

### Nickel-Iron (Edison) Battery

**Chemistry**:
- **Discharge**: Fe (anode) + 2NiOOH + 2H₂O → Fe(OH)₂ + 2Ni(OH)₂ (cell voltage: 1.2V nominal)
- **Electrolyte**: 20-25% KOH (potassium hydroxide) solution — alkaline, NOT acid.

**Advantages over lead-acid**:
- Extremely long cycle life (3000-10000+ cycles vs. 300-1500 for lead-acid).
- Tolerant of abuse (overcharge, overdischarge, short circuit).
- Wide temperature range (-40°C to +60°C).
- Nickel and iron are more available than lead in some locations.

**Disadvantages**:
- Lower energy density (20-30 Wh/kg).
- Higher self-discharge rate (20-40% per month vs. 5% for lead-acid).
- Voltage decreases significantly during discharge (1.2V → 1.0V vs. relatively flat 2.0V for lead-acid).
- Higher internal resistance → lower discharge rate capability.

**Construction**:
- **Positive plates**: Nickel hydroxide Ni(OH)₂ mixed with graphite (conductivity enhancer) and nickel flake, packed into perforated nickel-plated steel tubes or pockets.
- **Negative plates**: Iron powder mixed with small amounts of mercury (reduces passivation, improves conductivity) in perforated steel pockets.
- **Assembly**: Similar to lead-acid — alternating plates with separators in alkaline-resistant container (nickel-plated steel or plastic).

### Mechanical Energy Storage

**Pumped hydroelectric storage**:
- **Principle**: During surplus power, pump water from lower reservoir to upper reservoir (elevation gain). During demand, release water through turbine → generate electricity. Round-trip efficiency: 70-85%.
- **Requirements**: Two reservoirs with elevation difference (minimum 50-100 m head for useful energy density). Upper reservoir: natural lake or constructed reservoir. Lower reservoir: river, lake, or constructed. Penstock (pipe or tunnel connecting reservoirs) sized for maximum flow rate. Pump/turbine (reversible Francis turbine — acts as pump in one direction, turbine in reverse).
- **Energy storage**: E = ρ × g × h × V × η, where ρ = water density (1000 kg/m³), g = 9.81 m/s², h = head (m), V = volume (m³), η = efficiency. Example: 100 m head, 10,000 m³ upper reservoir = 1000 × 9.81 × 100 × 10000 × 0.75 / 3.6 × 10⁶ = ~2044 kWh. This is substantial.
- **Construction**: Major civil engineering project. Dam construction, tunnel boring, powerhouse. Requires powered machinery. Payback: decades of service. Most cost-effective large-scale storage.

**Flywheel energy storage**:
- **Principle**: Rotating mass stores kinetic energy: E = ½Iω², where I = moment of inertia, ω = angular velocity. Energy proportional to mass × radius² × RPM². Double RPM → 4× energy.
- **Construction**: Heavy steel rotor (solid cylinder or rim-weighted) on precision bearings. 100-500 kg, 0.3-1 m diameter, 3000-10000 RPM. Motor/generator couples to flywheel shaft — accelerates to store energy, decelerates to release.
- **Bearings**: Precision ball bearings (Machine Tools) minimum. Magnetic bearings (electromagnetic levitation, zero friction) for high-RPM, long-duration storage.
- **Enclosure**: Vacuum chamber (Vacuum & Optics) to eliminate air friction — at high RPM, air drag is enormous. Safety: containment vessel must withstand rotor burst (kinetic energy equivalent to explosion if rotor fails).
- **Energy density**: 5-50 Wh/kg (depending on RPM and material strength). Short discharge duration (seconds to minutes). Best for power quality (voltage/frequency stabilization), not long-duration energy storage.

**Compressed air energy storage (CAES)**:
- **Principle**: Compress air into storage vessel or underground cavern during surplus. Release through turbine during demand. Compression heats air → must cool (waste heat). Expansion cools air → must reheat (recover waste heat or burn fuel). Round-trip efficiency: 40-70% depending on heat recovery.
- **Storage vessel**: Steel pressure vessel (2-5 MPa rated). Underground salt cavern (solution-mined by dissolving salt with water — powered machinery, cheapest large-scale option). Abandoned mine workings (if gas-tight).
- **Compressor**: Multi-stage reciprocating or centrifugal compressor. Intercoolers between stages (remove heat of compression → less work required for next stage).
- **Applications**: Grid-scale energy storage (100+ MWh), industrial compressed air systems (pneumatic tools, actuators, instrument air).

### Energy Diversification

**Hydroelectric power**:
- **Resource assessment**: Measure stream/river flow rate (m³/s) and available head (vertical drop, m). Power potential: P = ρ × g × Q × h × η, where Q = flow rate, η = overall efficiency (0.6-0.85). Example: 1 m³/s flow, 10 m head = 1000 × 9.81 × 1 × 10 × 0.75 = ~73.6 kW. Reliable, continuous baseload power.
- **Turbine types**: Pelton wheel (high head, low flow — jet of water hits buckets on runner). Francis turbine (medium head, medium flow — water enters radially, exits axially). Kaplan turbine (low head, high flow — propeller-type with adjustable blade pitch). Selection based on head and flow characteristics.
- **Generator**: AC synchronous generator (see Energy). Connect to turbine shaft. Voltage regulation via excitation current control. Grid connection requires frequency and phase synchronization.

**Wind power**:
- **Wind assessment**: Measure wind speed distribution over months (anemometer — rotating cups driving counter or generator). Average wind speed >5 m/s at hub height for economic viability. Power proportional to wind speed cubed: P = ½ρAv³Cp, where ρ = air density, A = swept area, Cp = power coefficient (max 0.593, Betz limit; practical 0.3-0.45).
- **Wind turbine construction**: Tower (steel lattice or tubular, 10-50 m height — higher = more consistent, faster wind). Rotor (2-3 blades, wood + fabric or later fiberglass, 5-20 m diameter). Generator (DC or AC, 1-100+ kW). Yaw mechanism (vane or tail keeps rotor facing wind). Speed regulation (blade pitch control or mechanical brake to prevent overspeed in high winds).
- **Limitation**: Intermittent. Power output varies dramatically with wind conditions. Requires storage or backup for reliable supply. Best as supplemental source.

**[Solar photovoltaic](../glossary/solar-photovoltaic.html)** (Silicon):
- Early solar cells (5-15% efficiency) provide supplemental power. Positive feedback: solar cells produce power to make more solar cells. See Silicon for fabrication details.
- **Installation**: Mount panels facing equator (south in northern hemisphere) at angle ≈ latitude. Track sun (single-axis or dual-axis tracker increases output 20-40% but adds complexity). Connect to grid via inverter (DC → AC). Use battery storage for nighttime.

**Biomass**:
- Wood gasification (see Petrochemicals): gasifier + internal combustion engine + generator. Fuel: wood chips, agricultural waste, charcoal. 15-25% overall efficiency (biomass energy → electricity). Reliable if fuel supply is consistent. ~1 kg wood → ~1 kWh electricity.
- **Biogas**: Anaerobic digestion of organic waste (manure, food waste, crop residues) in sealed tank at 30-40°C. Produces biogas (~60% CH₄, ~40% CO₂). Burn in engine or boiler. ~0.3 m³ biogas per kg of organic waste.

### Grid Infrastructure

**Power distribution**:
- **Transmission**: High voltage (10-100+ kV) reduces line losses (P_loss = I²R — higher voltage = lower current = lower loss for same power). Step up at generator with transformer, step down at load. Three-phase AC transmission (3 conductors, 120° phase separation — most efficient wire utilization). Copper or aluminum conductors on wooden or steel towers.
- **Substation**: Transformers (step voltage up/down), circuit breakers (protect against short circuits), switches (isolate sections for maintenance), busbars (distribute to multiple feeders). Ground fault protection (detect leakage current → trip breaker).
- **Distribution**: Lower voltage (100-400V) to end users. Single-phase or three-phase service. Fuses or circuit breakers at each load for overcurrent protection.

**Load management**:
- **Demand response**: Schedule heavy loads (furnaces, pumps, charging) during periods of surplus generation. Shed non-critical loads during shortage.
- **Priority system**: Rank loads by criticality. Semiconductor fab equipment > lighting > heating > charging > non-essential. Automatic load shedding controller disconnects lowest-priority loads first when generation drops.
- **Power factor correction**: Inductive loads (motors, transformers) cause current to lag voltage → wasted capacity. Install capacitor banks to correct power factor → more usable power from same infrastructure.

**Uninterruptible Power Supply (UPS)**:
- **Topology**: Battery bank → inverter (DC → AC) → critical loads. Utility/generator → rectifier (AC → DC) → battery → inverter → loads (online UPS, continuous battery buffering). Or utility → load with battery/inverter on standby (offline UPS, switches to battery on utility failure — brief interruption).
- **For semiconductor fab**: Online UPS mandatory (zero transfer time). Battery sized for 15-30 minutes minimum (bridge to generator start). Generator for extended outages (diesel, gas, or wood-gas fueled, auto-start on utility failure, 10-30 second start time).
- **Inverter**: Convert DC battery voltage to AC (sine wave, 50 or 60 Hz, 220-240V). Motor-generator set (DC motor drives AC generator — simple, rugged, inefficient) or solid-state inverter (Photolithography — transistors switch DC at high frequency → synthesize sine wave, 85-95% efficient).

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Energy | Lead-acid batteries, pumped hydro, grid basics, steam + water power |
| Chemistry | Improved battery chemistry, electrolysis for hydrogen storage |
| Vacuum & Optics | Vacuum flywheel enclosures, magnetic bearings |
| Silicon | Solar cells add generation capacity (positive feedback loop) |
| Photolithography | UPS systems for fab equipment, solid-state inverters |
| VLSI Scaling+ | Nuclear baseload for industrial scale |

## Key Deliverables

- Lead-acid battery bank for critical equipment backup (sized for 15-30 min bridge)
- Standby generator (diesel or wood-gas, auto-start) for extended outages
- At least one diversified energy source beyond primary (hydro, wind, solar, biomass)
- Grid infrastructure with transmission, distribution, and load management
- Online UPS for semiconductor fabrication equipment (zero transfer time)
- Pumped hydro for large-scale storage (if geography permits)

### Safety & Hazards

- **Lead-acid batteries**: Sulfuric acid electrolyte (30-40%) causes severe chemical burns. Wear acid-resistant gloves and eye protection when handling cells. Spills neutralized with baking soda (NaHCO₃). Lead exposure risk during plate manufacturing — wash hands, avoid inhalation of lead oxide dust.
- **Hydrogen gas explosion**: Charging above 2.4V/cell electrolyzes water, producing H₂ + O₂. Hydrogen is explosive at 4-74% concentration in air. Battery rooms require forced ventilation (minimum 2 air changes/hour), no open flames, explosion-proof electrical fittings.
- **Short-circuit fire**: Lead-acid batteries can deliver hundreds of amps into a short circuit — instant arc, molten metal, fire. Insulate all tools when working near battery terminals. Install fuses or circuit breakers on every battery string.
- **Lithium thermal runaway** (later chemistries): Lithium-ion cells can enter self-sustaining overheating if overcharged, punctured, or shorted. Fire burns without external oxygen (self-oxidizing). Requires Class D fire extinguisher or sand — water may worsen lithium fires. Not applicable to lead-acid/nickel-iron bootstrap phase.

## Lead-Acid Battery Construction Detail

### Paste Mixing

The active material for each plate type requires a different paste formulation:

- **Positive paste**: Mix lead oxide (PbO, litharge) with sulfuric acid (H₂SO₄) and water. Typical ratio: 100 kg PbO, 6-8 L H₂SO₄ (SG 1.40), 8-12 L water. The acid reacts exothermically with PbO, forming a stiff gray-brown paste of lead sulfates and oxides. Mixing temperature must stay below 65°C (cooling jacket on mixer) to prevent premature hardening. Paste consistency: putty-like, must hold shape when pressed but flow under the paster roller.
- **Negative paste**: Same base (PbO + H₂SO₄ + water) but with expanders added: barium sulfate (BaSO₄, 0.3-1.0% by weight, acts as nucleation sites for lead sulfate crystals during discharge), carbon black (0.1-0.5%, improves conductivity), and lignin or organic expander (0.2-0.6%, prevents sintering of the spongy lead active material during cycling). Without expanders, the negative paste densifies over 100-200 cycles and loses capacity.
- **Paste application (pasting)**: Feed lead grids through a belt pasting machine. A hopper deposits paste onto the grid, and a roller or trowel presses paste into the lattice openings. Excess paste is scraped off. Pasted plates are flash-dried at 60-80°C for 1-2 hours to develop handling strength. Plate weight after pasting: 2-5 kg per plate depending on size.

### Curing

Freshly pasted plates undergo a controlled curing process that converts the paste from a soft mass into a hard, porous, mechanically robust active material:

- **Conditions**: 3-7 days at 30-40°C, 90-95% relative humidity. Humidity is critical. Too dry and the paste cracks and loses adhesion. Too wet and it stays soft.
- **Chemical changes during cure**: Free lead oxide in the paste reacts with CO₂ from the air to form lead carbonate (PbCO₃). Remaining PbO undergoes crystal growth, forming interlocking 3BS (3PbO·PbSO₄·H₂O) or 4BS (4PbO·PbSO₄) crystals that mechanically bind the paste to the grid. The grid-paste bond strength after curing should exceed 1.5 MPa.
- **Formation charging**: Cured plates are assembled into cells with dilute electrolyte (SG 1.05-1.10) and connected to a DC power supply. The formation process is a controlled first charge that electrochemically converts the paste: positive plates oxidize to PbO₂ (chocolate brown), negative plates reduce to spongy lead (gray). Formation protocol: 3-stage charging. Stage 1: constant current at C/20 rate (capacity divided by 20 hours) until cell voltage reaches 2.35V. Stage 2: constant voltage at 2.4V per cell, current tapers. Stage 3: finish at 2.5V per cell until specific gravity stabilizes and gas evolution is steady. Total formation time: 24-72 hours depending on plate thickness.
- **Electrolyte**: After formation, electrolyte is adjusted to its operating specific gravity: 1.25-1.28 SG (30-40% H₂SO₄ by weight) for flooded lead-acid batteries. The acid concentration corresponds to approximately 4.2-4.5 molar H₂SO₄. Freezing point of fully charged electrolyte (SG 1.28): approximately -70°C. Discharged electrolyte (SG 1.12): freezes near -10°C, a critical winter failure mode for undercharged batteries.

### Performance Specifications

- **Specific energy**: 30-40 Wh/kg (flooded), 25-35 Wh/kg (deep-cycle with thicker plates). A 12V, 100 Ah automotive battery weighs approximately 25-30 kg.
- **Cycle life**: 200-500 cycles for automotive starting batteries (thin plates, optimized for high current bursts not deep cycling). 500-1500 cycles for deep-cycle traction batteries (thick plates, 3-5 mm active material, designed for 80% depth of discharge). Cycle life degrades sharply below 20% state of charge, where irreversible lead sulfate crystallization (sulfation) accelerates.
- **Self-discharge**: 3-5% per month at 25°C. Doubles for every 10°C temperature increase. Batteries stored above 35°C self-discharge fast enough to sulfate in weeks if not periodically recharged.

## Nickel-Iron (Edison) Battery Construction Detail

The nickel-iron cell, patented by Thomas Edison in 1901, uses rugged materials suited to harsh industrial environments:

- **Positive plates**: Nickel hydroxide (Ni(OH)₂) active material mixed with graphite (20-30% by weight for conductivity) and nickel flake (5-10%), packed into perforated nickel-plated steel tubes or flat pockets. Tube diameter: 6-12 mm. Each tube is crimped or welded shut after filling. 20-50 tubes per plate, depending on cell size. The graphite and nickel flake form a conductive network through the poorly conducting Ni(OH)₂.
- **Negative plates**: Iron powder (electrolytic or reduced iron oxide) mixed with small amounts of mercury (0.1-0.5% to reduce passivation of iron by oxide films) in perforated nickel-plated steel pockets. Iron particle size: 50-200 μm.
- **Electrolyte**: 20-25% potassium hydroxide (KOH) solution, specific gravity 1.19-1.21. The electrolyte serves only as an ion conductor and does not participate in the overall cell reaction (unlike lead-acid where H₂SO₄ is consumed during discharge). This means electrolyte SG does not change with state of charge, so a hydrometer cannot be used to monitor charge state. Lithium hydroxide (LiOH, 5-15 g/L) is added to improve cycle life by retarding iron electrode degradation.
- **Cell voltage**: 1.2V nominal (1.3V at full charge, declining to 1.0V at end of discharge).
- **Specific energy**: 30-50 Wh/kg (improved designs with tubular positives reach the upper end).
- **Cycle life**: 3000-10,000+ cycles. Some Edison battery installations from the 1920s were still operational 40+ years later. The extraordinary longevity comes from the mechanical stability of the pocket plate construction and the benign chemistry (no irreversible sulfation as in lead-acid).
- **Temperature tolerance**: -40°C to +60°C. The alkaline electrolyte does not freeze as readily as sulfuric acid, and the iron electrode tolerates cold operation better than lead.
- **Overcharge/overdischarge tolerance**: The nickel-iron cell can be overcharged indefinitely (excess current electrolyzes water, but the electrodes are not damaged) and can be fully discharged to 0V without permanent damage. This makes the battery nearly indestructible in service, a major advantage for remote or unattended installations.
- **Disadvantage**: High self-discharge (20-40% per month). Not suitable for standby applications where the battery sits idle for months. Best used in daily cycling applications (solar off-grid, traction, mine locomotives) where the battery is continuously charged and discharged.

### Battery Bank Configuration

Individual cells are connected in series and parallel to achieve the required system voltage and capacity:

- **Series connection**: Adds voltages. Six 2V lead-acid cells in series = 12V battery. Twenty-four cells in series = 48V system (common for telecom and UPS). Current capacity remains that of a single cell.
- **Parallel connection**: Adds capacity. Two 100 Ah batteries in parallel = 200 Ah at the same voltage. Voltage remains that of a single battery string. Parallel strings should be identical (same age, same capacity, same manufacturer) to prevent circulating currents between mismatched strings.
- **Series-parallel**: For a 48V, 200 Ah system: two parallel strings of 24 series-connected 2V, 100 Ah cells. Total: 48 cells, weight approximately 800-1000 kg for lead-acid.
- **Battery room requirements**: Level floor capable of supporting 500-1500 kg/m² (battery racks are heavy). Temperature maintained at 20-25°C (capacity drops ~1% per °C below 25°C; life drops ~50% for every 8°C sustained above 25°C). Forced ventilation at minimum 2 air changes per hour for hydrogen removal. Acid-resistant flooring (epoxy paint or ceramic tile) with a containment berm to catch electrolyte spills. No open flames, no spark-producing equipment within the battery room.

### Charging System Design

Battery charging requires a DC power source matched to the battery bank voltage and capacity:

- **Rectifier-charger**: AC mains (or generator) → transformer → rectifier (full-wave bridge using silicon diodes) → filter (capacitor + inductor for ripple reduction) → battery. Output voltage regulated to ±1% of setpoint. Current limited to the maximum charge rate (C/10 for lead-acid, C/5 for nickel-iron). A 48V, 200 Ah battery bank requires a charger capable of 54-58 VDC output at 20 A (C/10), or about 1.2 kW.
- **Temperature compensation**: Lead-acid charge voltage must decrease by 3-4 mV per cell per °C above 25°C (and increase by the same amount below 25°C). Without compensation, a battery at 40°C will be overcharged at the 25°C voltage setting, accelerating water loss and grid corrosion. Most commercial chargers include a temperature probe that plugs into the battery and adjusts voltage automatically.
- **Equalizing charge**: Performed monthly on flooded lead-acid batteries to reverse stratification (dense acid settles to the bottom of the cell, dilute acid floats to the top). Apply 2.5V per cell (30V for a 24-cell 48V bank) for 2-4 hours after reaching full charge. The elevated voltage drives gas evolution, which physically mixes the electrolyte. Specific gravity should be measured in each cell after equalizing and should read within 0.020 of the average. Cells more than 0.030 below average may be failing.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
