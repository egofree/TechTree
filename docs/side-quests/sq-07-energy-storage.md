# SQ 7: Energy Storage &amp; Diversification

**Starts**: Phase 4+
**Priority**: Medium — grows in importance as energy demands increase and grid stability matters.

## Problem

Semiconductor fabrication equipment cannot tolerate power interruptions — a power glitch during a crystal growth run or lithography exposure destroys expensive work-in-progress. Energy storage provides buffer capacity, and diversification prevents single-source dependency.

## Technologies &amp; Systems

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
- **Construction**: Major civil engineering project. Dam construction, tunnel boring, powerhouse. Phase 4+ capability. Payback: decades of service. Most cost-effective large-scale storage.

**Flywheel energy storage**:
- **Principle**: Rotating mass stores kinetic energy: E = ½Iω², where I = moment of inertia, ω = angular velocity. Energy proportional to mass × radius² × RPM². Double RPM → 4× energy.
- **Construction**: Heavy steel rotor (solid cylinder or rim-weighted) on precision bearings. 100-500 kg, 0.3-1 m diameter, 3000-10000 RPM. Motor/generator couples to flywheel shaft — accelerates to store energy, decelerates to release.
- **Bearings**: Precision ball bearings (Phase 3) minimum. Magnetic bearings (Phase 6+ — electromagnetic levitation, zero friction) for high-RPM, long-duration storage.
- **Enclosure**: Vacuum chamber (Phase 6) to eliminate air friction — at high RPM, air drag is enormous. Safety: containment vessel must withstand rotor burst (kinetic energy equivalent to explosion if rotor fails).
- **Energy density**: 5-50 Wh/kg (depending on RPM and material strength). Short discharge duration (seconds to minutes). Best for power quality (voltage/frequency stabilization), not long-duration energy storage.

**Compressed air energy storage (CAES)**:
- **Principle**: Compress air into storage vessel or underground cavern during surplus. Release through turbine during demand. Compression heats air → must cool (waste heat). Expansion cools air → must reheat (recover waste heat or burn fuel). Round-trip efficiency: 40-70% depending on heat recovery.
- **Storage vessel**: Steel pressure vessel (2-5 MPa rated). Underground salt cavern (solution-mined by dissolving salt with water — Phase 4+ capability, cheapest large-scale option). Abandoned mine workings (if gas-tight).
- **Compressor**: Multi-stage reciprocating or centrifugal compressor. Intercoolers between stages (remove heat of compression → less work required for next stage). Phase 4+ technology.
- **Applications**: Grid-scale energy storage (100+ MWh), industrial compressed air systems (pneumatic tools, actuators, instrument air).

### Energy Diversification

**Hydroelectric power**:
- **Resource assessment**: Measure stream/river flow rate (m³/s) and available head (vertical drop, m). Power potential: P = ρ × g × Q × h × η, where Q = flow rate, η = overall efficiency (0.6-0.85). Example: 1 m³/s flow, 10 m head = 1000 × 9.81 × 1 × 10 × 0.75 = ~73.6 kW. Reliable, continuous baseload power.
- **Turbine types**: Pelton wheel (high head, low flow — jet of water hits buckets on runner). Francis turbine (medium head, medium flow — water enters radially, exits axially). Kaplan turbine (low head, high flow — propeller-type with adjustable blade pitch). Selection based on head and flow characteristics.
- **Generator**: AC synchronous generator (see Phase 4). Connect to turbine shaft. Voltage regulation via excitation current control. Grid connection requires frequency and phase synchronization.

**Wind power**:
- **Wind assessment**: Measure wind speed distribution over months (anemometer — rotating cups driving counter or generator). Average wind speed >5 m/s at hub height for economic viability. Power proportional to wind speed cubed: P = ½ρAv³Cp, where ρ = air density, A = swept area, Cp = power coefficient (max 0.593, Betz limit; practical 0.3-0.45).
- **Wind turbine construction**: Tower (steel lattice or tubular, 10-50 m height — higher = more consistent, faster wind). Rotor (2-3 blades, wood + fabric or later fiberglass, 5-20 m diameter). Generator (DC or AC, 1-100+ kW). Yaw mechanism (vane or tail keeps rotor facing wind). Speed regulation (blade pitch control or mechanical brake to prevent overspeed in high winds).
- **Limitation**: Intermittent. Power output varies dramatically with wind conditions. Requires storage or backup for reliable supply. Best as supplemental source.

**Solar photovoltaic** (Phase 7):
- Early solar cells (5-15% efficiency) provide supplemental power. Positive feedback: solar cells produce power to make more solar cells. See Phase 7 for fabrication details.
- **Installation**: Mount panels facing equator (south in northern hemisphere) at angle ≈ latitude. Track sun (single-axis or dual-axis tracker increases output 20-40% but adds complexity). Connect to grid via inverter (DC → AC). Use battery storage for nighttime.

**Biomass**:
- Wood gasification (see SQ 12): gasifier + internal combustion engine + generator. Fuel: wood chips, agricultural waste, charcoal. 15-25% overall efficiency (biomass energy → electricity). Reliable if fuel supply is consistent. ~1 kg wood → ~1 kWh electricity.
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
- **Inverter**: Convert DC battery voltage to AC (sine wave, 50 or 60 Hz, 220-240V). Motor-generator set (DC motor drives AC generator — simple, rugged, inefficient) or solid-state inverter (Phase 8 — transistors switch DC at high frequency → synthesize sine wave, 85-95% efficient).

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Phase 4 | Lead-acid batteries, pumped hydro, grid basics, steam + water power |
| Phase 5 | Improved battery chemistry, electrolysis for hydrogen storage |
| Phase 6 | Vacuum flywheel enclosures, magnetic bearings |
| Phase 7 | Solar cells add generation capacity (positive feedback loop) |
| Phase 8 | UPS systems for fab equipment, solid-state inverters |
| Phase 9+ | Nuclear baseload for industrial scale |

## Key Deliverables

- Lead-acid battery bank for critical equipment backup (sized for 15-30 min bridge)
- Standby generator (diesel or wood-gas, auto-start) for extended outages
- At least one diversified energy source beyond primary (hydro, wind, solar, biomass)
- Grid infrastructure with transmission, distribution, and load management
- Online UPS for semiconductor fabrication equipment (zero transfer time)
- Pumped hydro for large-scale storage (if geography permits)

[← Side Quests Index](index.md)
