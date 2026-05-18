# Temperature & Pressure Measurement

> **Node ID**: `measurement.temperature-pressure`
> **Domain**: [Measurement](./)
> **Dependencies**: `foundations`, `metallurgy`, `energy`
> **Timeline**: Years 25-40
> **Outputs**: thermocouples, temperature_measurement, electrical_measurement, pressure_measurement

## Problem

Semiconductor manufacturing demands precise thermal control: crystal growth furnaces (1400-1500°C ±0.5°C), diffusion furnaces (800-1200°C ±0.1°C), CVD reactors (300-1100°C), and epitaxial deposition (1050-1200°C). Pressure control is equally critical — vacuum systems for sputtering (10⁻³ to 10⁻⁶ mbar), LPCVD (0.2-2 mbar), and photolithography exposure tools. Without accurate temperature and pressure sensing, process repeatability is impossible.

## Thermocouples

Two dissimilar metals joined at a measurement junction generate a voltage (Seebeck effect) proportional to the temperature difference between the measurement junction and a reference (cold) junction. Output is in the millivolt range — read with a precision millivoltmeter or potentiometer circuit. Cold-junction compensation required (measure reference junction temperature independently, apply correction).

### Thermocouple Type Comparison

| Type | Positive Leg | Negative Leg | Range (°C) | Sensitivity | Best Use |
|------|-------------|-------------|------------|-------------|----------|
| **K** | Chromel (Ni-Cr) | Alumel (Ni-Al) | -200 to +1260 | ~41 μV/°C | General-purpose furnaces, kilns |
| **J** | Iron | Constantan (Cu-Ni) | -40 to +750 | ~51 μV/°C | Reducing atmospheres, older equipment |
| **T** | Copper | Constantan (Cu-Ni) | -200 to +350 | ~43 μV/°C | Cryogenic, low-temperature precision |
| **S** | Pt-10%Rh | Platinum | 0 to +1600 | ~6 μV/°C | High-temperature calibration standard |
| **B** | Pt-30%Rh | Pt-6%Rh | 0 to +1820 | ~1-5 μV/°C | Ultra-high temperature, glass melting |
| **R** | Pt-13%Rh | Platinum | 0 to +1600 | ~6 μV/°C | Similar to Type S, regional preference |

Type K is the workhorse — low cost, wide range, good accuracy (±1.5°C or ±0.25%, whichever is larger). Type S and R serve as secondary calibration references (±1.0°C) because platinum-rhodium alloys are exceptionally stable at high temperature. Type B's output is near zero below 50°C, so no cold-junction compensation needed for high-temperature use.

**Construction**: Thermocouple wire (0.25-3 mm diameter) welded at junction. Insulated with ceramic beads or mineral-packed metal sheath (MgO insulation in Inconel sheath for harsh environments). Sheath protects from corrosion and electrical noise.

## Resistance Temperature Detectors (RTDs)

Platinum wire (or thin-film) sensor whose resistance increases predictably with temperature. Pt100 standard: 100.0 Ω at 0°C, temperature coefficient +0.385 Ω/°C. Accuracy: ±0.1°C (Class A) to ±0.3°C (Class B) over 0-100°C range. Range: -200°C to +850°C.

**Measurement**: Four-wire (Kelvin) connection eliminates lead resistance errors. Constant current source drives sensor, measure voltage drop → R = V/I → temperature from lookup table or Callendar-Van Dusen equation. For semiconductor furnace control, RTDs handle the low-to-mid range; thermocouples handle the high end.

## Bimetallic Strips

Two metals bonded together with different thermal expansion coefficients (e.g., steel + invar, or brass + steel). Temperature change causes differential expansion → strip bends. Calibrated to indicate temperature on a dial (coil-spring bimetallic thermometer). Accuracy: ±1-2% of span. Range: -50°C to +500°C. No electrical power needed — useful as backup sensors and in thermostatic switches (furnace safety cutoffs).

## Pyrometers (Radiation Thermometry)

Non-contact temperature measurement from thermal radiation. Essential for moving targets, molten metals, and semiconductor wafers in process.

- **Optical (brightness) pyrometer**: Operator matches filament brightness against target through eyepiece. Range: 700-3000°C. Accuracy ±5-10°C. Requires skill but no calibration drift.
- **Two-color (ratio) pyrometer**: Measures ratio of radiation at two wavelengths. Emissivity-independent (unlike single-color). Range: 600-3000°C. Accuracy ±0.5%. Preferred for semiconductor furnaces where emissivity varies during process.
- **Infrared thermometer**: Broadband IR detector. Range: -50°C to +3000°C (model-dependent). Accuracy ±1-2%. Fast response (ms). Must correct for target emissivity.

## Pressure Gauges

### Bourdon Tube Gauge

Curved or helical tube of brass, steel, or beryllium copper. Internal pressure straightens the tube → mechanical linkage rotates pointer on dial. Range: 0-1 bar to 0-7000 bar. Accuracy: ±0.5-2% of full scale. Most common industrial pressure indicator. Simple, robust, no power required.

### Diaphragm Gauge

Flexible metal diaphragm (stainless steel, Hastelloy) deflects under differential pressure. Deflection measured mechanically (linkage to dial) or electrically (capacitive or strain-gauge sensor). Range: 0-10 mbar to 0-400 bar. Preferred for low-pressure and corrosive media. Capacitive diaphragm gauges achieve ±0.1% accuracy — used in semiconductor process chambers.

## Barometers

- **Mercury barometer**: Glass tube (~1 m) sealed at top, open at bottom, immersed in mercury reservoir. Atmospheric pressure supports mercury column. Height ≈ 760 mm at sea level. Read with vernier scale to ±0.1 mm Hg (±0.13 mbar). The absolute pressure reference. Mercury toxicity requires careful handling.
- **Aneroid barometer**: Evacuated metal capsule (thin-wall beryllium copper) compresses/expands with atmospheric pressure changes. Mechanical linkage amplifies motion to dial. No mercury. Accuracy ±1-2 mbar. Used for weather monitoring and altitude-corrected process pressure readings.

## Manometers

- **U-tube manometer**: Glass U-tube partially filled with liquid (water, oil, or mercury). Pressure applied to one arm → liquid level difference indicates pressure: P = ρgh. Range depends on fill fluid: water gives ~0.1 mbar resolution (for short tubes), mercury extends to ~1 bar. Absolute calibration — no zero drift. Used as primary standard for low-pressure calibration.
- **Inclined manometer**: Tube tilted at shallow angle (5-15°) → liquid travels further for same pressure change → resolution improved by 1/sin(θ). Resolution: 0.01 mbar with water fill. Used for draft measurement, cleanroom pressure differentials, and HVAC balancing.

## Flow Measurement

- **Orifice plate**: Thin plate with precision bore inserted in pipe. Pressure drop across plate proportional to flow rate squared (Bernoulli's equation). Measure ΔP with differential pressure gauge → compute flow. Simple, cheap, 2-5% accuracy. Permanent pressure loss 30-70% of ΔP.
- **Venturi tube**: Converging-diverging nozzle. Same Bernoulli principle as orifice plate but with gradual profile → lower permanent pressure loss (10-15% of ΔP). More expensive to fabricate but energy-efficient for continuous flow. 1-2% accuracy.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Metallurgy | Thermocouples (dissimilar metal junctions), bimetallic strips |
| Energy | Temperature monitoring for steam systems, pressure gauges for boilers |
| Chemistry | Process temperature control (reactions, distillation columns) |
| Vacuum & Optics | Low-pressure measurement for vacuum systems, pyrometers |
| Silicon | Furnace control for crystal growth, diffusion, oxidation (RTDs + thermocouples) |
| Photolithography | Precision chamber pressure and temperature for resist processing |

## Key Deliverables

- Thermocouple sets (Type K for general use, Type S for calibration, Type J for reducing atmospheres)
- Pt100 RTDs with four-wire readout for ±0.1°C furnace control
- Bourdon tube and diaphragm pressure gauges for process monitoring
- Mercury barometer as absolute pressure reference
- U-tube manometers for low-pressure calibration
- Two-color pyrometers for non-contact high-temperature measurement
- Orifice plates and venturi tubes for process flow measurement

---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
