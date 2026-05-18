# Vacuum Technology

> **Node ID**: `gas-handling.vacuum`
> **Domain**: [Gas Handling](./)
> **Enables**: `photolithography.fab-processes`, `silicon.basic-devices`
> **Timeline**: Years 25-40
> **Outputs**: vacuum_pumps, vacuum_chambers, vacuum_measurement, leak_detection

### Vacuum Technology

**Mechanical pumps** (foundation of all vacuum work):

**Piston pump** (simplest, lower vacuum):
- **Construction**: Cast iron cylinder, machined piston with leather cup seal, inlet and outlet check valves (leather or steel flappers). Driven by crank from motor or hand wheel.
- **Performance**: ~10-100 L/min pumping speed. Ultimate vacuum ~10-50 Torr (rough vacuum).
- **Applications**: Initial roughing pump, gas transfer, compression.

**Rotary vane pump** (workhorse — achieves medium vacuum):
- **Principle**: Eccentric rotor in cylindrical stator. Spring-loaded vanes slide in rotor slots, maintaining contact with stator wall. Gas enters inlet port, trapped between vanes and stator, compressed, expelled through exhaust valve.
- **Construction**: Cast iron stator (bored to ~0.01 mm tolerance on Machine Tools lathe/boring machine). Steel rotor. Steel or carbon fiber vanes. Oil-filled for sealing and lubrication (oil seals microscopic gaps between vanes and stator).
- **Oil requirements**: Low vapor pressure vacuum oil (see [Lubricants](../chemistry/lubricants.md)). Mineral oil with low volatility, or silicone oil. Oil changed regularly — contaminated oil limits ultimate vacuum.
- **Performance**: 1-50 L/min (small), 50-500 L/min (medium). Ultimate vacuum: ~10⁻² to 10⁻³ Torr (0.01-0.001 Pa). Single-stage: ~10⁻² Torr. Two-stage: ~10⁻³ Torr.
- **Gas ballast**: Small valve admits air during compression phase to prevent condensation of vapors (water, solvents) in pump oil. Essential when pumping wet systems.

**Diffusion pump** (high vacuum, no moving parts):
- **Principle**: Boiler heats silicone or hydrocarbon oil → vapor jets shoot downward → gas molecules from vacuum chamber diffuse into vapor stream → carried to exhaust → removed by backing pump. No moving parts, very reliable.
- **Backing pump requirement**: Diffusion pump requires a mechanical backing pump (rotary vane) to maintain foreline pressure below ~0.5 Torr. Without backing, diffusion pump stalls and oil backstreams into chamber.
- **Performance**: Pumping speed 50-10,000 L/s. Ultimate vacuum: ~10⁻⁶ to 10⁻⁸ Torr with proper trapping and baking.
- **Oil**: Silicone oil (DC-704, DC-705) or Santovac (polyphenyl ether). Low vapor pressure, high thermal stability. Oil heated to ~150-200°C in boiler.
- **Cold trap**: Liquid nitrogen cooled baffle between diffusion pump and chamber. Condenses backstreaming oil vapor. Essential for clean vacuum. LN₂ from the Chemistry stage air liquefaction.

**Vacuum chambers**:
- **Materials**: Steel or stainless steel (welded construction, all seams seal-welded). Aluminum (lighter, easier to machine, but more porous to He). Glass bell jars (for small systems — visual observation).
- **Design**: Cylindrical or spherical (uniform stress distribution). Viewports (glass windows with CF or ISO flanges). Multiple ports for feedthroughs (electrical, mechanical, gas).
- **Surface preparation**: Electropolish stainless steel internal surfaces (smooth surface = less outgassing). Clean with acetone, then alcohol, then bake.

**Vacuum measurement**:
- **Rough vacuum (760-1 Torr)**: Bourdon tube gauge (mechanical). U-tube manometer (oil or mercury — measures pressure difference directly).
- **Medium vacuum (1-10⁻³ Torr)**: Thermocouple gauge or Pirani gauge (heated wire — thermal conductivity of gas depends on pressure). Inexpensive, reliable.
- **High vacuum (10⁻³-10⁻⁸ Torr)**: Penning ionization gauge (cold cathode ionizes gas, ion current proportional to pressure). Bayard-Alpert ion gauge (hot cathode version, more accurate). Calibration against McLeod gauge (absolute pressure measurement using compressed gas column — primary standard).

**Leak detection**:
- **Bubble test**: Pressurize system, spray soap solution on exterior, watch for bubbles. Finds large leaks.
- **Helium leak detector** (Photolithography+): Mass spectrometer tuned to He. Spray He on exterior, detect He entering vacuum system. Sensitivity ~10⁻¹² atm·cc/s. The gold standard.
- **Tesla coil**: High-frequency spark probe. Spark penetrates small holes in glass apparatus (visible discharge inside). Glass systems only.
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
