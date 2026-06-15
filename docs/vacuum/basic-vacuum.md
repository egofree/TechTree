# Basic Vacuum Technology

> **Node ID**: vacuum.basic-vacuum
> **Domain**: [Vacuum](./index.md)
> **Level**: Capability
> **Era**: Industrial
> **Timeline**: Years 25-40
> **Dependencies**: [`vacuum`](./index.md)
> **Enables**: None
> **Outputs**: basic_vacuum_pumps, basic_vacuum_chambers, basic_vacuum_measurement, basic_leak_detection
> **Critical**: No — basic vacuum enables many processes but higher vacuum is achievable by other means

## Overview

Basic vacuum technology is the foundational tier of low-pressure engineering: the pumps, chambers, gauges, and leak-finding methods that produce and measure pressures from atmospheric (760 Torr) down to roughly 10⁻⁶ Torr. Everything more advanced — turbomolecular pumps, ultra-high vacuum, semiconductor thin-film deposition — builds on this base. A civilization that can reliably reach 10⁻³ Torr with an oil-sealed rotary vane pump and measure it with a Pirani gauge has crossed the threshold from "vessels that suck" into engineered vacuum.

The capability matters because vacuum is a processing environment, not just an absence of gas. Lamp bulbs (Edison/Swan, 1879) need vacuum so the filament does not oxidize in seconds. Vacuum distillation separates heat-sensitive compounds (vitamins, essential oils, glycerin) at temperatures that would decompose them at atmospheric pressure. Freeze drying preserves food and biologicals. Steel degassing removes dissolved hydrogen and nitrogen that embrittle the metal. Later, vacuum becomes the working medium of semiconductor manufacturing: every sputtering, evaporation, and CVD step runs at 10⁻⁶ Torr or below.

Position in the chain: basic vacuum depends on [precision machining](../machine-tools/machining.md) for close-tolerance pump rotors and on [iron & steel](../metals/iron-steel.md) for chamber walls that do not warp or leak. It unlocks [Vacuum Pumps](./pumps.md) (advanced types), [Vacuum Chambers](./chambers.md), and downstream capabilities like incandescent lighting, vacuum metallurgy, and eventually [silicon](../silicon/index.md) device fabrication. Without basic vacuum, none of these exist.

This article covers the three workhorse pump types (rotary vane, diffusion, and the rotary piston / diaphragm alternatives), simple steel-and-glass chambers, Bourdon and Pirani gauges, and leak detection via pressure-rise testing and tracer gas sniffing. For high-vacuum pump selection, system design, and advanced types (turbomolecular, ion, cryo), see [Vacuum Pumps](./pumps.md); for chamber construction and feedthroughs, see [Vacuum Chambers](./chambers.md); for measurement below 10⁻³ Torr, see [Vacuum Measurement](./measurement.md).

## Prerequisites

### Materials

- Cast iron and forged steel for pump bodies, vanes, and chamber walls — see [Iron & Steel](../metals/iron-steel.md)
- Low-vapor-pressure vacuum pump oil (mineral oil, <10⁻⁴ Torr vapor pressure at 20°C) for sealing rotary vane pumps
- Brass or copper gasket stock, lead wire, or O-ring rubber for demountable seals — see [Polymers](../polymers/index.md) for elastomer sourcing
- Borosilicate or soda-lime glass for gauge tubes and sight ports — see [Glass](../glass/index.md)
- Tungsten or platinum wire for Pirani gauge filaments

### Tools and Equipment

- [Precision machining](../machine-tools/machining.md) — lathe and mill capable of ±0.02 mm tolerances for pump rotors and cylinder bores
- [Precision motion](../precision-motion/index.md) bearings for pump shafts (3,000-1,800 RPM continuous)
- [Glassblowing](../glass/glassblowing.md) capability for gauge tubes and chamber viewports
- Surface grinder or lapping plate for flat chamber flange faces
- Torque wrenches for flange bolting (consistent gasket compression)

### Knowledge

- Gas laws (Boyle's law PV = constant at fixed temperature) — the foundation of pump-down volume calculations
- Mean free path concept — gas molecule collision distance grows from ~68 nm at 760 Torr to ~5 cm at 10⁻³ Torr; determines when flow transitions from viscous to molecular
- Vapor pressure — every material in a vacuum system outgasses; water vapor dominates the first hours of pump-down
- Outgassing and bakeout — chamber walls release adsorbed gases for hours; heating to 150-300°C accelerates removal 10-100×

### Infrastructure

- Closed cooling water loop (15-25°C) for diffusion pump cooling jackets
- 3-phase electrical power for pump motors (0.5-5 kW range)
- Ventilation for pump exhaust (oil mist, backstreamed vapors)
- Clean assembly area free of dust, lint, and volatile solvents

## Bill of Materials

BOM for a representative bench-scale basic vacuum system: one roughing pump, one diffusion pump, a 30 L steel chamber, Pirani gauge, and connecting plumbing.

| Material | Quantity per system | Source | Alternatives |
|----------|---------------------|--------|--------------|
| Cast iron pump body (rotary vane) | 1 unit, 15-25 kg | [Iron & Steel](../metals/iron-steel.md) sand casting + machining | Ductile iron; forged steel billet (higher cost) |
| Steel rotor and vanes (tool steel, hardened) | 1 rotor + 2-4 vanes | [Machine Tools](../machine-tools/machining.md) | Carbon steel (shorter life); ceramic vanes (oil-free service) |
| Vacuum pump oil (mineral, ISO VG 68) | 0.5-2 L fill | [Petroleum](../petroleum/index.md) refining — highly refined lube base stock | Synthetic ester oils (lower vapor pressure, higher cost) |
| Diffusion pump body (steel, water-jacketed) | 1 unit, 5-15 kg | [Iron & Steel](../metals/iron-steel.md) fabrication | Stainless steel 304 (lower outgassing, higher cost) |
| Diffusion pump fluid (silicone or hydrocarbon) | 0.05-0.3 L charge | [Chemistry](../chemistry/index.md) — polyphenyl ether or distilled hydrocarbon | Mercury (historical only — toxic vapor) |
| Chamber shell (mild steel, 3-6 mm wall) | 30 L volume cylinder | [Iron & Steel](../metals/iron-steel.md) weldment | Stainless steel (cleaner, costlier); glass bell jar (small systems) |
| Copper gasket stock (1-2 mm wire) | 1-5 m | [Metals](../metals/index.md) copper | Lead wire (soft, historical); O-ring elastomer (lower vacuum only) |
| Brass fittings, nipples, valve bodies | 10-30 pieces | [Metals](../metals/copper.md) brass | Steel fittings (rust risk); stainless (best, costly) |
| Pirani gauge tube (glass + tungsten filament) | 1-2 units | [Glassblowing](../glass/glassblowing.md) + tungsten wire | Thermocouple gauge (similar principle, lower sensitivity) |
| Bourdon gauge (brass, 0-760 Torr) | 1 unit | [Metals](../metals/copper.md) brass + [Machine Tools](../machine-tools/machining.md) | Diaphragm gauge (more accurate below 100 Torr) |

## Process Description

### Step-by-Step: Pump-Down of a Basic Vacuum Chamber

1. **Clean the chamber interior.** Wipe all surfaces with lint-free cloth dampened with acetone or ethanol. Residual oils, fingerprints, and solvents outgas for hours and prevent reaching target vacuum. Do not leave rags or tools inside.

2. **Verify seal integrity.** Inspect all O-rings and gaskets for cracks, nicks, embedded grit. Lightly grease O-rings with high-vacuum silicone grease (a film, not a glob). Install copper gaskets on knife-edge flanges; confirm seating before torquing.

3. **Torque flange bolts in a criss-cross pattern.** Bring all bolts to finger-tight, then torque in 1/3 increments to the gasket manufacturer's spec (typically 15-30 N·m for copper gaskets on 1-3 inch flanges). Uneven torquing causes leaks and warps flanges.

4. **Close all valves.** Set the roughing valve open, the high-vacuum (diffusion pump) valve closed, and the vent valve closed. The diffusion pump must NOT be exposed to atmosphere while hot.

5. **Start the roughing pump.** With gas ballast open if moisture is suspected, run the rotary vane pump. Monitor chamber pressure on the Bourdon gauge; expect a drop from 760 to ~10 Torr within 1-3 minutes for a 30 L chamber with a 5 L/s pump.

6. **Continue roughing to the crossover pressure.** The Pirani gauge takes over below ~10 Torr. Keep roughing until chamber pressure reaches the diffusion pump crossover point — typically 5×10⁻² to 1×10⁻¹ Torr. Crossing over at higher pressure saturates the diffusion pump jet and backstreams oil into the chamber.

7. **Start the diffusion pump heater.** With cooling water ON, energize the heater (400-1,000 W). Wait 15-30 minutes for the fluid to reach boiling (silicone fluid 704 boils ~210°C at atmospheric, much lower under vacuum). The pump is ready when the upper jet appears stable.

8. **Open the high-vacuum valve slowly.** A rapid full-open dumps the chamber gas load into the diffusion pump, quenching the vapor jet. Crack the valve, let pressure settle, open fully over 30-60 seconds.

9. **Monitor pump-down.** Chamber pressure should fall from ~10⁻¹ Torr toward 10⁻⁴ to 10⁻⁶ Torr over 30 minutes to several hours, depending on surface area, outgassing rate, and pump speed. The first hours are dominated by water vapor desorbing from chamber walls.

10. **Optional bakeout.** If the target is below 10⁻⁵ Torr, heat the chamber walls to 150-250°C with external heater tapes during pump-down. This accelerates outgassing 10-100×. Allow to cool before measuring final pressure — warm walls continue to outgas.

11. **Shutdown procedure.** Close the high-vacuum valve first. Vent the chamber with dry nitrogen or filtered air (never vent through a hot diffusion pump — the inrush of air oxidizes the hot fluid). Turn off the diffusion pump heater but keep cooling water flowing for 20-30 minutes until the pump body is below 50°C. Only then may the roughing pump be stopped.

### Pressure-Rise Leak Test

When the target vacuum is not reached, isolate the chamber from the pump (close all valves) and record pressure vs. time. A flat low rise indicates outgassing (decays after bakeout). A steady linear rise indicates a real leak. A leak rate of 10⁻⁴ Torr·L/s is tolerable for rough work; 10⁻⁶ Torr·L/s is needed for high vacuum. Locate leaks by spraying suspected joints with a tracer (ethanol or — if available — helium) while watching the gauge; a pressure jump identifies the leak location.

## Quantitative Parameters

| Parameter | Rotary Vane (1-stage) | Rotary Vane (2-stage) | Diffusion Pump (4-inch) | Rotary Piston |
|-----------|----------------------|----------------------|------------------------|---------------|
| Ultimate pressure (Torr) | 10⁻² | 5×10⁻⁴ | 10⁻⁶ to 10⁻⁷ | 10⁻² |
| Pumping speed (L/s) | 0.5-5 (rough) | 0.5-5 (rough) | 100-400 (at 10⁻⁴ Torr) | 5-50 |
| Throughput at 1 Torr (Torr·L/s) | 5-30 | 5-30 | 0.1-0.5 (declines with vacuum) | 30-150 |
| Pump-down: 760→10 Torr, 30 L chamber | 1-3 min | 1-3 min | Not used for roughing | 0.5-2 min |
| Pump-down: 10→10⁻³ Torr, 30 L chamber | 5-15 min | 3-8 min | 3-10 min (after crossover) | 4-12 min |
| Heater power (diffusion) | — | — | 400-1,000 W | — |
| Cooling water flow (diffusion) | — | — | 0.5-2 L/min, 15-25°C | — |
| Oil / fluid charge | 0.5-2 L mineral | 0.5-2 L mineral | 50-300 mL silicone 704 | 1-4 L mineral |
| Oil change interval | 3-6 months | 3-6 months | 1-2 years (sealed system) | 6-12 months |
| Backstreaming rate (mg/cm²·min) | 0.001-0.01 | 0.001-0.01 | 0.0001-0.001 (with cold cap / baffle) | 0.001-0.01 |
| Noise level at 1 m (dB) | 50-75 | 50-72 | 35-45 (pump itself; blower noise dominates) | 60-80 |

### Outgassing Reference Data

| Surface treatment | Outgassing rate (Torr·L/s·cm²) after 1 h pumping | After 10 h |
|-------------------|--------------------------------------------------|------------|
| Mild steel, as-received (oily) | 1×10⁻⁶ | 3×10⁻⁷ |
| Mild steel, cleaned + dried | 5×10⁻⁷ | 1×10⁻⁷ |
| Stainless steel, cleaned | 2×10⁻⁷ | 5×10⁻⁸ |
| Stainless steel, baked 24 h at 150°C | 5×10⁻¹⁰ | 1×10⁻¹⁰ |
| O-ring elastomer (Buna-N), unbaked | 1×10⁻⁵ | 3×10⁻⁶ |
| PTFE (Teflon) | 3×10⁻⁶ | 1×10⁻⁶ |

## Scaling Notes

- **Bench scale (5-30 L chamber):** A single 5 L/s two-stage rotary vane pump plus a 4-inch diffusion pump reaches 10⁻⁵ Torr in under an hour. Suitable for lamp sealing, small vacuum distillation, lab demonstration. Total equipment mass ~50 kg.
- **Workshop scale (50-500 L chamber):** Step up to a 15-50 L/s roughing pump and a 6-inch diffusion pump. Pump-down time scales roughly with volume ÷ pump speed, but outgassing surface area grows with V^(2/3), so the dominant time cost shifts toward desorption. Bakeout becomes mandatory below 10⁻⁴ Torr.
- **Production scale (1,000+ L):** Add a Roots blower between the roughing pump and chamber to cut pump-down to 10⁻¹ Torr by 5-10×. Multiple diffusion pumps in parallel, or a single large (10-20 inch) pump. Chamber wall material becomes critical — mild steel outgassing limits ultimate vacuum; stainless steel or coated interiors are standard.
- **Minimum economic scale:** A 5 L/s rotary vane pump and a 10 L glass bell jar on a brass baseplate is the smallest useful configuration — roughly $500-1,000 of equipment at modern prices, reachable in bootstrap with cast iron + machining.
- **Non-linear scaling limits:** Pumping speed does not scale linearly with pump size below 10⁻⁴ Torr because outgassing and permeation (gas diffusing through chamber walls and elastomers) dominate. Doubling pump speed at 10⁻⁶ Torr may only improve ultimate vacuum by 2×, not halve it.
- **Bottleneck:** Below 10⁻⁵ Torr, water vapor is 60-90% of the residual gas load. A water-cooled or cryogenic trap (Meissner coil) above the diffusion pump freezes out water and cuts pump-down time to ultimate vacuum by 3-10×.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Chamber will not pump below ~10 Torr | Gross leak at a flange, valve, or weld porosity; vent valve partially open | Torque-check all flange bolts; close and seat vent valve; pressure-rise test (isolate chamber, watch gauge); spray suspected joints with ethanol and watch for pressure jump |
| Pump reaches 10⁻² Torr but no better | Single-stage pump at its ultimate limit, or oil contaminated with water / solvent | Switch to two-stage pump; change oil (cloudy or milky oil indicates water emulsion); run gas ballast 30 min to decontaminate |
| Diffusion pump gives no improvement below 10⁻³ Torr | Crossed over at too high a pressure (jet quenched), or fluid degraded / low, or cooling water too warm | Re-rough to <5×10⁻² Torr before opening HV valve; check fluid level and color (dark = oxidized, replace); verify cooling water ≤25°C and flow ≥0.5 L/min |
| Oil backstreaming contaminates chamber (oily film on surfaces) | No baffle or cold cap above diffusion pump; roughing pump oil mist reaching chamber | Install water-cooled baffle or chevron trap above diffusion pump; add molecular sieve oil trap on roughing line; minimize time on roughing pump alone |
| Pressure rises when HV valve opened | Diffusion pump not yet at operating temperature, or fluid charge low | Wait full 20-30 min warm-up; top up fluid to rated level (50-300 mL depending on pump size) |
| Pressure spikes during operation | Coolant interruption to diffusion pump (fluid boils over, backstreams into chamber) | Install coolant flow interlock; never operate diffusion pump without cooling water flowing |
| Pirani gauge reading erratic or stuck high | Filament contaminated with oil deposit, or gauge exposed to liquid water | Clean or replace gauge tube; mount gauge above chamber midline to avoid condensate dripping in |
| Pump motor overheats or trips breaker | Low oil level, seized vane, or running against closed inlet | Check oil sight glass; stop pump immediately and inspect vanes; never run a rotary vane pump with inlet and outlet both blocked (explosion risk from sealed gas compression) |
| Slow pump-down after weeks of good performance | Chamber wall outgassing has accumulated (adsorbed water, hydrocarbons from fingerprints) | Clean interior with acetone; bake out at 150-200°C for 4-12 h while pumping |

## Safety

- **Oil-sealed rotary vane pumps compress gas continuously.** Never operate with both inlet and outlet blocked — the sealed gas volume can be compressed to ignition pressures, exploding the pump housing. Always confirm the exhaust is open to atmosphere or a vent line before starting.
- **Hot diffusion pump fluid (200-300°C).** Contact with air while hot oxidizes the fluid instantly, producing acidic fumes that attack lung tissue and corrode the pump interior. Always cool below 50°C before opening to atmosphere. Use the high-vacuum valve to isolate the pump before venting the chamber.
- **Mercury diffusion pump fluid (historical).** Mercury boils at 157°C under vacuum and produces a vapor that is a cumulative neurotoxin. Avoid mercury entirely; if encountered in legacy equipment, treat as hazardous waste. Mercury vapor IDLH: 10 mg/m³ (NIOSH).
- **Diffusion pump heater: 400-1,000 W at line voltage.** Electrical hazard during maintenance. Lock out / tag out the heater circuit before opening the pump. Cool the pump before servicing — hot silicone fluid causes thermal burns.
- **Implosion risk for glass chambers and gauge tubes.** A glass bell jar under vacuum stores ~1 atm × surface area of energy. A 30 cm diameter jar stores ~7,000 J of pressure energy; if it fails, glass fragments travel at high velocity. Wrap glass chambers with tape or mesh; wear safety glasses; place a polycarbonate shield between the operator and the chamber.
- **Oil mist in exhaust.** Rotary vane pumps emit a fine oil mist that accumulates in the lungs on chronic exposure. Vent exhaust outside or through an oil-mist filter. Provide 5-10 air changes per hour in the pump room.

### Personal Protective Equipment

- Safety glasses or face shield when viewing vacuum chambers under operation
- Heat-resistant gloves when handling diffusion pump bodies or heated chambers
- Oil-resistant nitrile gloves when changing pump oil
- Hearing protection around large roughing pumps (>70 dB)

### Emergency Procedures

- **Glass implosion:** Evacuate the area, wait 5 minutes for fragments to settle, sweep up with damp cloth (not bare hands), dispose of as sharp waste.
- **Diffusion pump thermal runaway (coolant loss):** Shut off heater immediately, leave cooling water on, do NOT vent the pump to atmosphere until below 50°C.
- **Oil spill:** Absorb with vermiculite or sand; dispose of as hazardous waste if contaminated with solvents. Do not flush oil into drains.

## Quality Control

### Acceptance Criteria

- **Rough vacuum system:** Reaches ≤5×10⁻² Torr within 30 min on a clean, dry 30 L chamber, holds ≤1×10⁻¹ Torr for 1 hour isolated (leak rate ≤10⁻⁴ Torr·L/s).
- **High vacuum system (with diffusion pump):** Reaches ≤5×10⁻⁵ Torr within 4 h on a clean 30 L chamber; ultimate vacuum ≤1×10⁻⁶ Torr after 12 h with bakeout.
- **Seal integrity:** Pressure rise ≤0.1 Torr/min when isolated at 10⁻² Torr.

### Testing Methods

- **Bourdon gauge (0-760 Torr):** Mechanical, ±5% of reading. Use for initial pump-down verification and vent monitoring. Tap the gauge lightly before reading to overcome static friction.
- **Pirani gauge (10⁻³ to 10 Torr typical):** Thermal-conductivity gauge, ±10% of reading. Calibrate against a known reference (McLeod gauge or capacitance manometer) quarterly. Filament resistance varies with gas thermal conductivity — air and nitrogen calibrate directly; helium and hydrogen read high (faster heat conduction); argon and heavy oils read low.
- **Pressure-rise test (leak quantification):** Isolate chamber, record P(t) for 10-60 minutes. Linear slope = leak rate; decaying slope = outgassing. Convert slope × volume to leak rate (Torr·L/s).
- **Bubble test (gross leak location):** Pressurize the evacuated chamber's exterior with a tracer gas, or apply soap solution to suspected external joints while under vacuum and watch for bubbles (works only for large inward leaks).
- **McLeod gauge (reference standard, 10⁻¹ to 10⁻⁵ Torr):** Mercury compression gauge, absolute, ±1%. Used to calibrate Pirani gauges. Bulky, fragile, mercury hazard — use only for calibration, not routine monitoring.

### Sampling Procedure

- Log pump-down curve (pressure vs. time) on each first pump-down of a chamber after opening to atmosphere.
- Check oil level and clarity in the rotary vane pump sight glass weekly; change when cloudy.
- Verify diffusion pump fluid color and level monthly; replace when dark brown or when ultimate vacuum degrades by >5×.

## Variations and Alternatives

- **Rotary vane pump (oil-sealed):** The universal workhorse of rough vacuum. Two-stage variants reach 5×10⁻⁴ Torr. Cheapest cost-per-L/s. Oil backstreaming is the main drawback. Covered above as the default.
- **Rotary piston pump:** Larger displacement (5-50 L/s) for industrial chambers. More robust than vane pumps, tolerates dust and condensable vapors. Noisier (60-80 dB). Used for steel degassing and large vacuum furnaces.
- **Diaphragm pump:** Oil-free, dry pumping to ~1 Torr. Used where any oil contamination is unacceptable (mass spectrometer inlets, food processing). Lower ultimate vacuum than oil-sealed pumps. Diaphragm lifetime 5,000-10,000 hours.
- **Scroll pump:** Oil-free alternative reaching ~10⁻² Torr. Quieter (45-55 dB) and cleaner than rotary vane. Tip seals wear out (15,000-30,000 h) and require factory service. Higher capital cost.
- **Water aspirator (Venturi):** Uses flowing water to produce ~10-20 Torr vacuum (limited by water vapor pressure at ambient temperature). No moving parts. Cheap. Contaminates the process with water vapor. Useful for filtration and degassing only — not for drying or high vacuum.
- **Hand-operated piston pump:** Historical bootstrap option. Two leather-cup piston pumps in series reach ~50 Torr. Slow (1-3 L/min). Useful only for very small volumes or demonstration.
- **Steam ejector:** Multi-stage steam ejectors reach 10⁻¹ to 10⁻² Torr without moving parts, using high-pressure steam as the motive fluid. Industrial scale (vacuum distillation columns, steel degassing). Requires a steam boiler (≥3 bar); see [Steam Power](../energy/steam-power.md).

### Trade-off Comparison

| Method | Ultimate vacuum | Capital cost | Maintenance | Oil contamination |
|--------|----------------|--------------|-------------|-------------------|
| Rotary vane (2-stage) | 5×10⁻⁴ Torr | Low | Oil change 3-6 mo | Yes (backstreaming) |
| Rotary piston | 10⁻² Torr | Medium | Oil change 6-12 mo | Yes |
| Diaphragm | ~1 Torr | Medium | Diaphragm 5-10 kh | None |
| Scroll | 10⁻² Torr | High | Tip seals 15-30 kh | None |
| Water aspirator | 10-20 Torr | Very low | None | Water vapor only |
| Steam ejector (3-stage) | 10⁻² Torr | Medium | None (no moving parts) | None (steam only) |

## References

- [Vacuum Pumps](./pumps.md) — advanced pump types (turbomolecular, ion, cryo), selection guide, system design
- [Vacuum Chambers](./chambers.md) — chamber construction, feedthroughs, flange standards
- [Vacuum Measurement](./measurement.md) — high-vacuum gauges (Bayard-Alpert ionization, capacitance manometers)
- [Leak Detection](./leak-detection.md) — helium mass spectrometry leak detection, tracer methods
- [Gas Handling: Vacuum](../gas-handling/vacuum.md) — foundational pump operating principles (rotary vane, scroll, diaphragm)
- [Machine Tools](../machine-tools/index.md) — precision machining capability for pump rotors and chamber fabrication
- [Iron & Steel](../metals/iron-steel.md) — structural material for pump bodies and chamber walls

---
*Part of the [Bootciv Tech Tree](../index.md) • [Vacuum](./index.md) • [All Domains](../index.md)*
