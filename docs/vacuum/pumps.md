# Vacuum Pumps

> **Node ID**: vacuum.pumps
> **Domain**: [Vacuum Technology](./index.md)
> **Enables**: [`silicon.basic-devices`](../silicon/basic-devices.md), [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`optics.inspection`](../optics/inspection.md)
> **Timeline**: Years 25-40
> **Outputs**: vacuum_pumps, roughing_pumps, high_vacuum_pumps, uhv_pumps

### Vacuum Pumps

For foundational vacuum pump descriptions (rotary vane, diffusion, scroll, diaphragm principles), see [Gas Handling: Vacuum](../gas-handling/vacuum.md). This document covers pump selection, advanced pump types, performance specifications, and system design.

### Pump Classification by Pressure Range

| Vacuum Range | Pressure (Torr) | Pressure (Pa) | Primary Pump Types | Typical Application |
|---|---|---|---|---|
| Rough vacuum | 760 – 10⁻³ | 10⁵ – 0.1 | Rotary vane, scroll, diaphragm, piston | Initial pump-down, backing for HV pumps |
| Medium vacuum | 10⁻³ – 10⁻⁵ | 0.1 – 10⁻³ | Roots blower, sorption | Dehydration, freeze drying, metallurgy |
| High vacuum (HV) | 10⁻⁵ – 10⁻⁸ | 10⁻³ – 10⁻⁶ | Turbomolecular, diffusion | Sputtering, evaporation, CVD, SEM |
| Ultra-high vacuum (UHV) | 10⁻⁸ – 10⁻¹¹ | 10⁻⁶ – 10⁻⁹ | Ion pump, cryopump, NEG, titanium sublimation | Surface science, MBE, particle accelerators |
| Extreme high vacuum (XHV) | <10⁻¹¹ | <10⁻⁹ | Combination NEG + ion + cryo | Space simulation, fundamental physics |

### Roughing Pumps — Detailed Specifications

**[Rotary vane pump](../glossary/rotary-vane-pump.md)** (see [Gas Handling: Vacuum](../gas-handling/vacuum.md) for operating principle):

| Parameter | Small (1-10 L/min) | Medium (10-100 L/min) | Large (100-500 L/min) |
|---|---|---|---|
| Pumping speed | 1-10 L/min (0.04-0.4 CFM) | 10-100 L/min (0.4-3.5 CFM) | 100-500 L/min (3.5-18 CFM) |
| Ultimate vacuum (single-stage) | ~10⁻² Torr | ~10⁻² Torr | ~10⁻² Torr |
| Ultimate vacuum (two-stage) | ~10⁻³ Torr | ~5×10⁻⁴ Torr | ~10⁻³ Torr |
| Oil charge | 0.2-0.5 L | 0.5-2 L | 2-8 L |
| Motor power | 0.1-0.25 kW | 0.25-1.5 kW | 1.5-4 kW |
| Noise level | 50-60 dB | 55-65 dB | 60-75 dB |

- **Oil selection**: Use low-vapor-pressure vacuum oil (see [Lubricants](../chemistry/lubricants.md)). Inland 19 or equivalent (mineral oil, vapor pressure ~5×10⁻⁵ Torr at 25°C). For cleaner vacuum: Inland 45 (synthetic, ~5×10⁻⁷ Torr at 25°C). Change oil every 3-6 months or when oil appears dark/cloudy (contaminated oil limits ultimate vacuum).
- **Gas ballast operation**: When pumping wet systems or condensable vapors, open the gas ballast valve. This admits a small amount of air during the compression stroke, preventing vapor condensation in the oil. Gas ballast raises the ultimate vacuum by ~10× (from 10⁻³ to 10⁻² Torr), but it protects the oil from contamination. Close gas ballast for the final stages of pump-down when vapor load is negligible.
- **Exhaust filtration**: Install an oil mist eliminator on the exhaust port. Without it, the pump emits a fine oil mist that coats nearby equipment and creates a respiratory hazard. The mist eliminator (coalescing filter) captures >99% of oil droplets. Replace filter element when saturated (typically every 6-12 months).

**[Scroll pump](../glossary/scroll-pump.md)** — oil-free roughing (see [Gas Handling: Vacuum](../gas-handling/vacuum.md) for operating principle):

| Parameter | Small | Medium | Large |
|---|---|---|---|
| Pumping speed | 5-15 m³/h (1.5-4 CFM) | 15-35 m³/h (4-10 CFM) | 35-60 m³/h (10-18 CFM) |
| Ultimate vacuum | ~10⁻² mbar (~7.5×10⁻³ Torr) | ~10⁻² mbar | ~5×10⁻³ mbar |
| Noise level | 45-55 dB | 50-60 dB | 55-65 dB |

- **Advantages for semiconductor processing**: Oil-free exhaust means no hydrocarbon backstreaming contamination of the process chamber. Critical for: sputtering (even trace oil on target or substrate ruins film quality), CVD (oil contamination poisons catalysts and creates defects), and surface analysis (XPS, Auger detect hydrocarbons at monolayer levels).
- **Maintenance**: Scroll tip seals wear over time. Typical seal life: 15,000-30,000 hours. Seal replacement requires factory service or trained technician — not field-serviceable in most models. Plan for pump rotation or scheduled maintenance.

### High-Vacuum Pumps — Detailed Specifications

**[Turbomolecular pump](../glossary/turbomolecular-pump.md)** (see [Gas Handling: Vacuum](../gas-handling/vacuum.md) for operating principle):

| Parameter | Small (50-200 L/s) | Medium (200-1000 L/s) | Large (1000-5000 L/s) |
|---|---|---|---|
| Pumping speed (N₂) | 50-200 L/s | 200-1000 L/s | 1000-5000 L/s |
| Compression ratio (N₂) | >10⁹ | >10⁹ | >10⁹ |
| Compression ratio (H₂) | 10³-10⁵ | 10³-10⁵ | 10³-10⁵ |
| Compression ratio (He) | 10⁴-10⁶ | 10⁴-10⁶ | 10⁴-10⁶ |
| Rotor speed | 60,000-90,000 RPM | 40,000-70,000 RPM | 20,000-45,000 RPM |
| Startup time | 1-3 min | 2-5 min | 5-15 min |
| Ultimate vacuum | 10⁻¹⁰ mbar (with baking) | 10⁻¹⁰ mbar | 10⁻¹⁰ mbar |
| Backing requirement | <0.1-1 mbar foreline | <0.1-1 mbar | <0.1-1 mbar |

- **Bearing types**: Ceramic ball bearings (standard, lifetime ~30,000-50,000 hours, require periodic lubrication) vs. active magnetic levitation bearings (lifetime essentially unlimited, no lubrication, no vibration, but more expensive and require backup power for safe spin-down during power failure).
- **Vibration considerations**: At 40,000-90,000 RPM, turbopumps transmit vibration to the chamber. For vibration-sensitive applications (SEM, TEM, atomic force microscopy), use: (1) magnetically levitated turbo (zero mechanical contact), (2) vibration isolation bellows between pump and chamber, or (3) mount pump on a separate frame connected by a flexible bellows. Typical vibration amplitude: 0.1-1 μm for ball-bearing pumps, <0.01 μm for mag-lev.
- **Corrosive gas service**: For pumping corrosive process gases (Cl₂, F₂, CF₄, SF₆ decomposition products), use a turbo with nickel-coated rotor and stator blades, and FKM (Viton) or PTFE seals. Standard stainless/ aluminum turbos corrode rapidly in halogen service. Purge the pump with dry N₂ after corrosive gas processing to extend life.
- **Protection devices**: Install a foreline pressure sensor interlocked to the turbo controller. If foreline pressure exceeds the critical backing pressure (typically 1-10 mbar), the turbo stalls and the controller must shut down the pump to prevent rotor contact. Sudden pressure bursts from process upsets can destroy a turbo in seconds — a fast-acting gate valve between chamber and pump provides protection.

**[Diffusion pump](../glossary/diffusion-pump.md)** (see [Gas Handling: Vacuum](../gas-handling/vacuum.md) for operating principle):

| Parameter | Small (2-inch) | Medium (4-inch) | Large (6-10 inch) |
|---|---|---|---|
| Pumping speed (N₂) | 50-150 L/s | 300-800 L/s | 1000-10,000 L/s |
| Ultimate vacuum | 10⁻⁶-10⁻⁷ Torr | 10⁻⁷-10⁻⁸ Torr | 10⁻⁷-10⁻⁸ Torr |
| Foreline tolerance | <0.5 Torr | <0.5 Torr | <0.5 Torr |
| Boiler temperature | 150-200°C | 150-200°C | 150-200°C |
| Heater power | 0.3-0.5 kW | 1-2 kW | 3-10 kW |
| Cooling water | 1-2 L/min | 3-5 L/min | 5-15 L/min |
| Oil charge | 50-100 mL | 200-500 mL | 500-2000 mL |

- **Working fluid selection**: DC-704 (tetraphenyl tetramethyl trisiloxane, vapor pressure ~10⁻⁸ Torr at 25°C) for general high-vacuum use. Santovac 5 (polyphenyl ether, vapor pressure ~10⁻⁹ Torr at 25°C) for the cleanest possible diffusion pump vacuum. DC-705 (pentaphenyl trimethyl trisiloxane) for UHV applications. Never use hydrocarbon oils in diffusion pumps — they decompose rapidly and create carbon deposits.
- **Cold trap requirements**: A liquid nitrogen (LN₂) cooled baffle between the diffusion pump and the chamber is essential. Without it, backstreaming oil vapor contaminates the vacuum chamber at a rate of ~10⁻⁶ g/cm²/min. With a properly maintained LN₂ cold trap: backstreaming <10⁻¹⁰ g/cm²/min. The cold trap also acts as a cryopump for condensable gases (water, CO₂, solvents), improving effective pumping speed.
- **Cooling water interlock**: The most critical safety system on a diffusion pump. Install a water flow switch that shuts off the heater if cooling water flow drops below minimum. Without cooling, the boiler overheats, oil decomposes (producing flammable gases), and the pump body can reach temperatures that damage seals and nearby equipment. Test the interlock monthly.

### Ultra-High Vacuum Pumps

**Cryopumps**: Condense and trap gas molecules on cold surfaces. The pump contains a refrigerated cold head (closed-cycle helium refrigerator, typically 10-20 K for the second stage, 40-80 K for the first stage).

- **Operating principle**: The cold head consists of two stages. The first stage (40-80 K) cools a radiation shield and an array that condenses high-boiling-point gases (H₂O, CO₂, hydrocarbons). The second stage (10-20 K) cools charcoal-coated panels that cryosorb low-boiling-point gases (H₂, He, Ne) by physisorption in the charcoal pores.
- **Pumping speed**: 500-50,000 L/s depending on cold head size and array geometry. Pumping speed varies by gas: H₂O is pumped very fast (condenses on first stage), H₂ slower (depends on charcoal sorption capacity).
- **Ultimate vacuum**: ~10⁻¹¹ Torr (limited by H₂ and He vapor pressures at the cold stage temperature).
- **Capacity**: A cryopump saturates when the charcoal pores fill with sorbed gas. Typical capacity: 10⁴-10⁵ Torr·L of N₂ equivalent before regeneration needed. For H₂: ~10³ Torr·L. Monitor pressure rise during pump-down — when base pressure no longer reaches specification, the pump needs regeneration.
- **Regeneration**: Warm the pump to room temperature (or above) while valved off from the chamber, then pump away the released gases with a roughing pump. Regeneration cycle: 2-8 hours depending on pump size and gas load. Automated regeneration controllers warm the pump, open the roughing valve, pump to base pressure, then re-cool.
- **Advantages**: Clean (no oil, no moving parts in the vacuum), high pumping speed for water vapor (critical for rapidly pumping down after chamber vent), captures all gases including H₂ and He. **Disadvantages**: Finite capacity requires periodic regeneration, helium compressor is noisy and requires maintenance, sudden loss of cooling releases trapped gas into chamber (install a safety relief valve).

**Ion pumps (sputter ion pumps)**: Ionize gas molecules in a magnetic field, accelerate them into a titanium cathode, and bury them. The sputtered titanium also acts as a getter (chemically reactive surface that captures active gases).

- **Operating principle**: A Penning cell — two titanium cathode plates with a stainless steel anode cylinder between them. A strong magnetic field (~0.1-0.2 T from permanent magnets) forces electrons into long spiral paths, increasing ionization probability. Positive ions bombard the cathode, sputtering titanium. Gas molecules are pumped by: (1) burial in the cathode (ion implantation), (2) chemical reaction with sputtered titanium (gettering), and (3) burial under fresh titanium deposits.
- **Pumping speed**: 5-500 L/s depending on number of Penning cells and pump size. Pumping speed varies strongly by gas: N₂, O₂, CO, CO₂ pumped efficiently (gettering by titanium). Noble gases (Ar, He) pumped poorly (only by ion burial — no chemical gettering). H₂ pumped well initially but diffuses back out over time (not permanently trapped).
- **Ultimate vacuum**: ~10⁻¹¹ Torr (limited by noble gas instability — argon periodically re-emitted in "argon instability" events where buried Ar ions are released by fresh sputtering).
- **Starting pressure**: Ion pumps cannot start at atmospheric pressure. They require a starting pressure below ~10⁻³ Torr (use a roughing pump + turbo or sorption pump to reach this). At higher pressures, the discharge current is too high and the pump overheats.
- **Power requirement**: 3-7 kV DC at 1-100 mA depending on pressure (current proportional to gas density). At UHV pressures, current is in the μA range — power consumption is negligible. No backing pump required once started.
- **Applications**: SEM, TEM, surface analysis (XPS, AES, SIMS), particle accelerators, space simulation chambers. Ideal for long-term unattended operation at UHV — no moving parts, no backing pump, no regeneration.

**Titanium sublimation pumps (TSP)**: Periodically heat a titanium filament to ~1400°C, subliming a fresh titanium film onto nearby chamber walls. The fresh titanium is an extremely active getter that chemisorbs active gases (O₂, N₂, H₂, CO, CO₂, H₂O).

- **Pumping speed**: Very high for active gases: 1-10 L/s per cm² of fresh titanium surface (100-10,000 L/s total depending on chamber geometry). Essentially zero pumping for noble gases (Ar, He, Ne).
- **Filament life**: Each filament (Ti alloy wire, typically 85% Ti / 15% Mo) lasts 30-100 sublimation cycles. Typical system has 3 filaments for ~200-300 total cycles. Filament current: 30-50 A at 2-4 V.
- **Usage pattern**: Sublime for 30-60 seconds to deposit fresh film, then the film pumps continuously until saturated (hours to days depending on gas load). Sublime again when pressure rises. In a well-baked UHV system, a single sublimation can maintain UHV for weeks.
- **Integration**: TSP is always used as a supplemental pump alongside an ion pump (which handles noble gases) or cryopump.

**Non-evaporable getter (NEG) pumps**: Heat a Zr-V-Fe alloy (St 707 from SAES Getters, or equivalent) to ~400-450°C to activate the surface. The activated alloy getters active gases at room temperature, providing continuous pumping without power consumption during operation.

- **Pumping speed**: 10-500 L/s depending on cartridge/stripped geometry. Very high for H₂ (diffuses into the bulk alloy), moderate for CO, CO₂, N₂, O₂ (surface chemisorption only), zero for noble gases and methane.
- **Activation**: Heat to 400-450°C for 30-60 minutes under vacuum. This dissociates the surface oxide/passivation layer, exposing fresh reactive alloy. After activation and cool-down, the NEG pumps at room temperature indefinitely until the surface saturates.
- **Capacity**: For H₂: extremely high (dissolves into bulk, ~50 Torr·L/g of alloy). For CO, N₂, O₂: limited by monolayer surface coverage (~1 Torr·L per 100 cm² of NEG surface). Can be re-activated by re-heating after saturation.
- **Advantages**: No moving parts, no power during pumping, no vibration, no magnetic field, compact, can be installed inside the vacuum chamber (no external footprint). Ideal for particle accelerators and portable UHV systems. **Disadvantages**: Does not pump noble gases or methane, requires periodic re-activation, heating during activation releases some previously pumped gas.

### Pump Selection Matrix for Semiconductor Applications

| Application | Base Pressure Required | Primary Pump | Backing Pump | Notes |
|---|---|---|---|---|
| Vacuum evaporation (metallization) | 10⁻⁵ – 10⁻⁶ Torr | Diffusion pump + LN₂ trap | Rotary vane (2-stage) | Most common bootstrap configuration. Cheap, reliable. |
| DC/RF sputtering | 10⁻⁵ – 10⁻⁷ Torr | Turbomolecular | Scroll (oil-free) | Oil-free critical for film quality. |
| PECVD | 10⁻³ – 10 Torr (process pressure) | Turbomolecular (throttled) | Rotary vane | Pump throttled to maintain process pressure. Gas load high. |
| LPCVD | 0.1 – 1 Torr (process pressure) | Rotary vane + Roots blower | — | High throughput, moderate vacuum. |
| Ion implantation | 10⁻⁶ – 10⁻⁷ Torr | Cryopump or turbo | — | High gas loads from dopant sources. |
| SEM inspection | 10⁻⁵ – 10⁻⁷ Torr | Ion pump + TSP or turbo (mag-lev) | — | Vibration-free critical for imaging. |
| Surface analysis (XPS, AES) | 10⁻⁹ – 10⁻¹⁰ Torr | Ion pump + NEG + TSP | Turbo (for initial pump-down) | UHV required for clean surfaces. |
| Crystal growth (CZ puller) | 10⁻³ – 10⁻⁴ Torr (argon atmosphere at ~10-30 Torr) | Roots blower + rotary vane | — | Roughing pumps for argon recirculation. |

### Pump-Down Time Calculations

**Roughing phase** (atmospheric to ~1 Pa, outgassing negligible):

t = (V / S_eff) × ln(P₁ / P₂)

where V = chamber volume (L), S_eff = effective pumping speed at chamber (L/s), P₁ = starting pressure, P₂ = target pressure.

**Example**: 100 L chamber with 5 L/s effective pumping speed, from 10⁵ Pa to 1 Pa:

t = (100 / 5) × ln(10⁵ / 1) = 20 × 11.51 = 230 seconds ≈ 4 minutes

The effective pumping speed is lower than the pump's rated speed due to conductance limitations of piping between the chamber and pump:

1/S_eff = 1/S_pump + 1/C_pipe

where C_pipe is the conductance of the connecting pipe (L/s). For a 1 m length of 25 mm ID pipe in molecular flow, C ≈ 30 L/s for N₂. If the pump is rated at 5 L/s, then 1/S_eff = 1/5 + 1/30, giving S_eff ≈ 4.3 L/s. The pipe costs only 14% of the pump speed. But if the pump is rated at 300 L/s (turbomolecular), S_eff ≈ 27 L/s — the pipe chokes the pump to only 9% of its rated speed. Lesson: use short, wide piping for high-speed pumps.

**High-vacuum phase** (below 1 Pa, outgassing dominates):

The time to reach a target pressure in the high-vacuum regime depends on the total gas load Q from outgassing:

P = Q / S_eff

A chamber reaches its base pressure when the outgassing rate equals the effective pumping speed times the pressure. Outgassing decreases over time following approximately:

q(t) = q₀ × t⁻¹

where q₀ is the initial outgassing rate and t is time in hours. For a stainless steel chamber (electropolished, unbaked), q₀ ≈ 2×10⁻⁶ Pa·m³/s·m². After 10 hours of pumping, q drops to ~2×10⁻⁷. After baking at 250°C for 24 hours: q drops to ~10⁻⁸ to 10⁻⁹ Pa·m³/s·m².

### Backing Pump Sizing

The backing pump must maintain foreline pressure below the high-vacuum pump's critical backing pressure at maximum throughput:

S_backing ≥ Q_max / P_critical

where Q_max is the maximum gas load (Pa·L/s) and P_critical is the critical foreline pressure (Pa).

**Example**: A turbomolecular pump with P_critical = 1 Pa, processing gas load Q = 10 Pa·L/s:

S_backing ≥ 10 / 1 = 10 L/s = 600 L/min

A 600 L/min rotary vane pump is required as backing for this gas load.

### Pump Maintenance Schedule

| Pump Type | Maintenance Item | Interval |
|---|---|---|
| Rotary vane | Oil change | 3-6 months |
| Rotary vane | Oil mist filter replacement | 6-12 months |
| Rotary vane | Vane replacement | 2-3 years |
| Scroll | Tip seal replacement | 15,000-30,000 hours |
| Turbomolecular (ball bearing) | Bearing lubrication | Per manufacturer |
| Turbomolecular (ball bearing) | Bearing replacement | 30,000-50,000 hours |
| Turbomolecular (mag-lev) | Controller capacitor check | 5 years |
| Diffusion pump | Oil change | 1-3 years |
| Diffusion pump | Heater element replacement | 3-5 years |
| Diffusion pump | Cooling system inspection | 6 months |
| Cryopump | Regeneration | Every 4-24 hours (depends on gas load) |
| Cryopump | Cold head overhaul | 2-3 years |
| Cryopump | Charcoal array replacement | 5-10 years |
| Ion pump | Filament/cathode replacement | When speed drops (5-10 years typical) |
| TSP | Filament replacement | 30-100 sublimations per filament |
| NEG | Re-activation | When saturated (months to years) |

### Safety & Hazard Summary

- **Turbomolecular pump mechanical hazard**: Rotor at 20,000-90,000 RPM. Never open the pump inlet while rotor is spinning. Wait for complete stop before servicing. A broken rotor blade becomes a high-velocity projectile.
- **Diffusion pump fire hazard**: Cooling water failure → oil overheats → decomposition gases (flammable) → air ingress → ignition. Mandatory: water flow interlock that cuts heater power.
- **Cryopump cold burn hazard**: Cold head at 10-20 K causes immediate frostbite on contact. Use cryogenic gloves. LN₂ cold traps: same hazard plus LOX condensation risk if trap is vented while still cold (see [Gas Handling: Vacuum](../gas-handling/vacuum.md)).
- **Electrical hazard**: Ion pumps operate at 3-7 kV DC. TSP filaments at 30-50 A. Diffusion pump heaters at 200-500°C surface temperature. Lock-out/tag-out procedures for all maintenance.

---

## See Also

- **[Gas Handling: Vacuum](../gas-handling/vacuum.md)**: Foundational vacuum pump operating principles
- **[Vacuum Chambers & Sealing](chambers.md)**: Chamber design and sealing systems
- **[Vacuum Measurement & Leak Detection](measurement.md)**: Pressure gauges and leak detection
- **[Lubricants, Oils & Fluid Mechanics](../chemistry/lubricants.md)**: Vacuum oil specifications

*Part of the [Bootciv Tech Tree](../index.md) • [Vacuum Technology](./index.md) • [All Domains](../index.md)*
