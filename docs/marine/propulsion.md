# Marine Propulsion Systems

> **Node ID**: marine.propulsion
> **Domain**: [Marine & Naval Engineering](./index.md)
> **Dependencies**: [`energy.engine`](../energy/engine.md), [`energy.steam-power`](../energy/steam-power.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`transport.shipping`](../transport/shipping.md), [`marine.navigation`](navigation.md)
> **Timeline**: Years 0-50+
> **Outputs**: marine engines, propellers, paddle wheels
> **Critical**: No — specialized maritime capability, not required for land-based civilization


Marine propulsion evolves through four stages: oar (muscle), sail (wind), steam (coal), and internal combustion (liquid fuel). Each stage increases power density and operational independence from weather. This document covers the engineering of marine propulsion systems — the adaptation of power sources for shipboard use.

For propulsion overview and hull speed calculations, see [Water Transport](../transport/shipping.md).

## Prerequisites

- [Heat Engines](../energy/engine.md) — internal combustion engine design
- [Steam Power](../energy/steam-power.md) — steam engine design and boiler construction
- [Iron & Steel](../metals/iron-steel.md) — materials for engine and propeller construction

## Oar Propulsion

The simplest marine drive: direct conversion of human muscle to thrust.

**Oar mechanics**:
- Oar acts as a lever: the fulcrum (oarlock or thole pin) is positioned so the inboard handle is shorter than the outboard blade
- Typical oar: 2.5-4.5 m length, blade 15-25 cm wide, loom (shaft) 4-6 cm diameter
- Rowing angle: oar sweeps 70-90° through the water per stroke
- Stroke rate: 20-30 strokes per minute for sustained cruising, 35-45 for sprinting
- Effective blade area per oar: 0.08-0.15 m²

**Power and speed**:
- A trained oarsman produces 0.1-0.2 HP sustained (75-150 W)
- A 30-oar galley (trireme): 3-6 HP sustained, speed 5-7 knots for 1-2 hours
- Limitations: crew fatigue limits range to 50-100 nm per day. Crew requires food and water (4-8 liters/person/day in hot climates). Crew occupies space that could carry cargo.

**Galley configurations**:
- **Unireme**: one row of oars per side, 25-50 oars total. Simple, common for merchant galleys.
- **Bireme**: two banks of oars per side, 50-100 oars total. Requires shorter oars and precise timing between banks.
- **Trireme**: three banks, 150-170 oars, 3 m overlapping stroke. The pinnacle of oared warship design. 37 m × 5.5 m, 50 tonnes displacement, crew of 200. Speed 7-8 knots burst, 4-5 knots sustained.

## Sail Propulsion

For detailed sail mechanics, rig types, and sail area calculations, see [Water Transport](../transport/shipping.md).

**Sail efficiency parameters**:
- **Drive force**: F = 0.5 × ρ × V² × A × CL, where ρ = air density (1.225 kg/m³), V = apparent wind speed (m/s), A = sail area (m²), CL = lift coefficient (0.8-1.5 depending on sail shape and angle of attack)
- **Heeling moment**: MH = F × h, where h = height of the center of effort above the center of lateral resistance. Must be resisted by the vessel's righting moment (GM × displacement × g).
- **Sail area to displacement ratio**: SA/D = sail area (m²) / (displacement volume (m³))^2/3. Target 15-20 for cargo, 20-30 for fast vessels.

**Wind power available**:
- At 10 knots wind speed with 100 m² sail area: F = 0.5 × 1.225 × 5.14² × 100 × 1.0 = 1,617 N (165 kgf)
- At 20 knots wind with same sail: F = 0.5 × 1.225 × 10.29² × 100 × 1.0 = 6,488 N (662 kgf) — 4× the force for 2× the wind speed
- Sail must be reefed (area reduced) in strong winds to prevent capsize or rig failure

## Steam Propulsion

Steam engines adapted for marine use must address unique challenges: saltwater corrosion, space constraints, weight distribution, and variable loading from waves.

**Marine boiler design**:
- **Fire-tube boiler** (early): hot combustion gases pass through tubes surrounded by water. Simple, robust. Working pressure 5-15 bar. Efficiency 50-60%. Weight: 8-12 kg/HP. Firebox and tubes are consumable — require replacement every 5-10 years due to salt deposition and corrosion.
- **Water-tube boiler** (later): water circulates inside tubes surrounded by hot gases. Higher pressure (15-30 bar), faster steam generation, lighter (3-6 kg/HP). More complex to build. Babcock & Wilcox type with headers and drums.
- **Feedwater treatment**: critical for marine boilers. Salt in feedwater deposits on tube surfaces as scale (calcium carbonate, magnesium hydroxide), reducing heat transfer and causing tube failure. Distill feedwater from seawater using a feedwater heater/evaporator. Target: <5 ppm total dissolved solids in feedwater.

**Marine steam engines**:

**Simple expansion (early, 1800s-1850s)**:
- Single cylinder, 3-5% thermal efficiency
- 5-15 HP initially, scaling to 100-500 HP by mid-century
- Operating pressure: 3-8 bar
- RPM: 20-60 (slow, requires large flywheel)
- Specific fuel consumption: 2-4 kg coal per HP-hour

**Compound engine (1860s-1880s)**:
- Steam expands through two cylinders in series: high-pressure (HP) then low-pressure (LP)
- HP cylinder: smaller bore, receives fresh steam at 8-15 bar
- LP cylinder: larger bore (2-3× HP diameter), receives exhaust steam at 2-5 bar
- Efficiency: 7-10%, roughly double the simple expansion engine
- Fuel consumption: 1.0-1.5 kg coal per HP-hour
- Key innovation: the LP cylinder captures energy from steam that would otherwise be wasted

**Triple-expansion engine (1880s-1920s)**:
- Steam expands through three cylinders: HP → IP (intermediate) → LP
- Cylinder bore ratios approximately 1 : 2 : 3.5 (HP:IP:LP)
- Operating pressure: 12-17 bar
- Efficiency: 10-15%
- Fuel consumption: 0.7-1.0 kg coal per HP-hour (or 0.5-0.7 kg oil)
- Power range: 500-5,000 HP per engine
- The dominant marine engine for 40 years. SS Warrington (1888) first triple-expansion cargo ship.

**Steam turbine (1900s+)**:
- Steam expands through rotating blades (no pistons, no reciprocating parts)
- Parsons turbine: steam flows axially through alternating rows of fixed and moving blades
- RPM: 2,000-5,000 (requires reduction gearing to drive propeller at 80-200 RPM)
- Efficiency: 15-20% (with condenser)
- Power density: 5-10× better than reciprocating engines (same power, smaller engine)
- Fuel consumption: 0.4-0.6 kg oil per HP-hour
- Requires precision manufacturing (blade tolerances ±0.05 mm) — depends on advanced machine tools

**Condenser system**:
- Essential for marine steam engines — allows feedwater reuse instead of dumping steam overboard
- Surface condenser: steam passes through tubes cooled by seawater on the outside. Condensed water (distillate) returns to the boiler as feedwater.
- Vacuum in the condenser (0.05-0.15 bar absolute) increases engine efficiency by lowering the exhaust back-pressure
- Condenser tube material: copper-nickel alloy (90/10 or 70/30) resists saltwater corrosion. Tube diameter 15-25 mm, wall thickness 1-1.5 mm.

## Screw Propeller

The screw propeller replaces paddle wheels for most applications by the 1860s.

**Propeller geometry**:
- Diameter (D): typically 0.6-0.8× the ship's draft. Larger diameter = more efficient but must fit within hull envelope.
- Pitch (P): distance the propeller would advance in one revolution if turning in a solid medium. P/D ratio: 0.8-1.4 (fixed-pitch propellers).
- Blade number: 3-5 blades. Fewer blades = higher efficiency but more vibration. 4 blades is the most common compromise.
- Blade area ratio (BAR): blade area / disk area. 0.3-0.8. Higher BAR prevents cavitation at high loading.

**Propeller efficiency**:
- Advance ratio: J = Va / (n × D), where Va = speed of advance (m/s), n = revolutions per second, D = diameter
- Optimal J for maximum efficiency: 0.6-0.9
- Open-water efficiency: 55-70% at optimal J. Lower at off-design conditions.
- Losses: friction on blade surfaces (5-10%), kinetic energy in the propeller wake (20-35%), cavitation losses (0-15%)

**Cavitation**:
- When local pressure on the blade surface drops below the vapor pressure of water (2.3 kPa at 20°C), water vapor bubbles form
- Bubbles collapse violently when they enter higher-pressure regions, eroding the blade surface (cavitation damage)
- Onset speed: approximately V = √(2 × (Patm - Pv) / ρ) ≈ 10-12 m/s blade tip speed
- Prevention: increase blade area, reduce RPM, increase diameter, or use a super-cavitating blade profile
- Cavitation damage: pitting and erosion of bronze propeller blades. 1-3 mm material loss per 1,000 hours if severe. Must inspect and repair during dry-docking.

**Propeller materials**:
- Manganese bronze: 58% Cu, 39% Zn, 1-2% Mn, 1% Fe, 1% Al. Tensile strength 450-550 MPa. Corrosion-resistant in seawater. The standard propeller material.
- Nickel-aluminum bronze: superior strength (600-750 MPa) and corrosion resistance. Used for high-powered vessels.
- Cast iron: cheap but brittle, only for small/slow vessels. Poor cavitation resistance.

**Propeller sizing calculation**:
- Thrust (T) = Resistance (R) at design speed. Required thrust includes hull resistance plus margin for waves and wind.
- Power delivered (PD) = T × Va / ηprop, where ηprop = propeller efficiency (0.55-0.70)
- Shaft power (PS) = PD / ηshaft, where ηshaft = shaft bearing efficiency (0.95-0.98)
- Brake power (PB) = PS / ηgear, where ηgear = reduction gear efficiency (0.95-0.98)

## Paddle Wheel

The earlier alternative to screw propellers.

**Side paddle wheels**: Two wheels, one on each side of the hull. Wheel diameter 4-10 m, width 1-3 m. Paddles (floats) bolted to the wheel rim at 8-16 per wheel. Dip depth: 0.5-1.0 m below the waterline.

**Stern paddle wheel**: Single wheel at the stern. Used for river boats. Simpler machinery (one wheel) but poorer steering.

**Strengths**:
- Simple mechanical connection — crankshaft drives paddle wheel directly via chain or gear, no complex shaft seals or stern tubes
- Works in shallow water — paddle dip is adjustable, suitable for rivers and coastal routes
- Proven at low technology levels — wooden paddles on iron wheels achievable with basic foundry capability
- Easy maintenance — all moving parts above the waterline, accessible without dry-docking
- Reverse by reversing engine rotation — no need for reversing gear or controllable-pitch mechanism

**Weaknesses**:
- Low efficiency (35-50%) — significant energy lost to paddle entry/exit splash, lifting water, and air entrainment
- Roll instability in beam seas — one wheel dips deeper than the other, causing the vessel to heel
- Limits ship beam (width) — paddle boxes occupy valuable deck space and reduce cargo capacity
- Exposed to damage — wheels protrude from the hull and are vulnerable to collision, grounding, and enemy fire
- Speed variation with vessel loading — as the ship sits lower in the water, paddle immersion increases, changing efficiency
- Obsolete for ocean-going vessels by the 1860s — screw propellers are superior in every respect for open water

## Internal Combustion Engine Propulsion

**Marine diesel engine (1900s+)**:

**Two-stroke slow-speed diesel**:
- The dominant engine for large cargo ships and tankers
- RPM: 60-120 (direct drive to propeller, no reduction gear needed)
- Bore: 300-960 mm. Stroke: 1,200-2,500 mm
- Single cylinder output: 500-5,000 HP
- Total engine: 6-14 cylinders, 3,000-70,000 HP
- Thermal efficiency: 45-52% (highest of any practical prime mover)
- Specific fuel consumption: 160-180 g/kWh (heavy fuel oil)
- Weight: 30-60 kg/HP (very heavy — acceptable in ships where weight is less critical)
- The MAN B&W and Wärtsilä two-stroke designs dominate modern shipping

**Four-stroke medium-speed diesel**:
- RPM: 400-800 (requires reduction gearing)
- Bore: 200-640 mm
- Power range: 500-25,000 HP
- Thermal efficiency: 40-45%
- Used for smaller vessels, ferries, tugs, and as generator sets on larger ships
- Weight: 8-20 kg/HP

**Fuel requirements**:
- Heavy fuel oil (HFO): residual oil from petroleum refining. Viscosity 180-700 cSt at 50°C. Must be heated to 100-130°C for injection. Contains sulfur (0.5-3.5%), vanadium, and sodium — causes corrosion and deposits. Requires purification (centrifuge) before use.
- Marine diesel oil (MDO): lighter, cleaner, more expensive. Used in smaller engines and in emission control areas.
- Energy density: HFO ~40,000 kJ/kg, MDO ~42,000 kJ/kg

## Propulsion Power Calculations

**Resistance-based power estimation**:

For a 100 m cargo vessel at 12 knots:
1. Hull resistance: R = 150-250 kN (from model testing or empirical formula)
2. Required thrust: T = R / (1 - wake fraction t) = 200 kN / (1 - 0.2) = 250 kN
3. Delivered power: PD = T × Va / ηP = 250,000 × 6.17 / 0.62 = 2,488 kW
4. Shaft power: PS = PD / ηS = 2,488 / 0.97 = 2,565 kW
5. Brake power: PB = PS / ηG = 2,565 / 0.97 = 2,644 kW (3,545 HP)

**Fuel consumption at this power**:
- Diesel engine (SFC 170 g/kWh): 2,644 × 0.170 = 449 kg/hour
- At 12 knots, range 5,000 nm requires: 5,000 / 12 = 417 hours × 449 = 187,233 kg (187 tonnes fuel)
- Steam turbine (SFC 220 g/kWh): 2,644 × 0.220 = 582 kg/hour, 242 tonnes for same range

## Safety & Hazards

- **Boiler explosion**: Steam at 15 bar contains enormous energy. A boiler explosion kills everyone in the engine room and can breach the hull. Safety valves (set to lift at design pressure +10%), water level gauges, and regular inspection prevent this. Never bypass safety valves.
- **Fuel oil fires**: HFO heated to 130°C for injection ignites easily if sprayed. Fuel line integrity is critical. Fire suppression (CO₂ flooding) in engine rooms mandatory.
- **Crankcase explosion**: Lubricating oil mist in enclosed crankcases can ignite at 250-300°C. Oil mist detectors and crankcase relief valves prevent catastrophic failure.
- **Propeller entanglement**: Rope, netting, or debris wrapping around the propeller shaft stops the engine and requires divers or dry-docking to clear. Rope cutters fitted on shafts reduce this risk.
- **Carbon monoxide**: Diesel engine exhaust contains CO. Exhaust systems must be gas-tight and discharge above deck level. Never run engines in enclosed spaces without ventilation.

## Propulsion Evolution Summary

| Era | Propulsion | Power Range | Efficiency | Fuel | Speed (100m vessel) |
|-----|-----------|-------------|-----------|------|-------------------|
| Stone Age | Oar | 1-6 HP | N/A (human) | Food | 3-5 knots |
| Bronze-Iron Age | Sail | 10-200 HP (wind) | N/A (free) | None | 5-10 knots |
| Early Industrial | Paddle steam | 50-500 HP | 3-5% | Coal | 6-8 knots |
| Mid Industrial | Screw steam | 200-5,000 HP | 10-15% | Coal | 8-12 knots |
| Late Industrial | Steam turbine | 1,000-70,000 HP | 15-20% | Oil/Coal | 12-25 knots |
| Modern | Diesel | 500-70,000 HP | 40-52% | Oil | 10-25 knots |

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Engine overheating under load | Raw water intake blocked or impeller worn | Clear intake strainer; replace impeller; check raw water pump output |
| Propeller cavitation (vibration, erosion) | Blade loading too high or tip speed excessive | Reduce engine RPM; install larger-diameter propeller with more blades; check hull clearance |
| Excessive vibration at cruising speed | Propeller out of balance or shaft misalignment | Dynamically balance propeller; realign shaft with dial indicators; check cutless bearing wear |
| Steam engine losing power | Boiler scale buildup or steam leaks | Blow down boiler; descale with acid wash; inspect and repack gland packing |
| Sail rig not pointing high enough | Sail shape too full or rigging slack | Tighten shrouds; flatten sail with outhaul and cunningham; check forestay tension |
| Engine won't reach rated RPM | Propeller pitch too coarse or hull fouling | Clean hull; reduce propeller pitch; check fuel system for restrictions |

## See Also

- [Water Transport](../transport/shipping.md) — propulsion overview, hull speed, displacement calculations
- [Steam Power](../energy/steam-power.md) — steam engine design and boiler construction
- [Heat Engines](../energy/engine.md) — internal combustion engine design
- [Metals: Iron & Steel](../metals/iron-steel.md) — materials for engine and propeller construction
- [Hull Construction](shipbuilding.md) — ship structural design
- [Metal Joining](../machine-tools/joining.md) — riveting and welding for hull construction
- [Navigation](navigation.md) — maritime navigation and piloting

[← Back to Marine & Naval Engineering](index.md)
