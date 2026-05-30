# Vacuum Measurement & Leak Detection

> **Node ID**: vacuum.measurement
> **Domain**: [Vacuum Technology](./index.md)
> **Dependencies**: `measurement`
> **Enables**: None (leaf capability)
> **Timeline**: Years 25-40
> **Outputs**: vacuum_measurement, leak_detection, rga_analysis, pressure_gauges

## Vacuum Measurement & Leak Detection

For basic vacuum gauge descriptions (Bourdon, Pirani, ion gauge principles), see [Gas Handling: Vacuum](../gas-handling/vacuum.md). This document covers detailed gauge specifications, residual gas analysis, leak detection methodology, and vacuum system diagnostics.

## Pressure Gauge Classification

| Gauge Type | Measurement Range (Torr) | Measurement Range (Pa) | Principle | Gas-Dependent? |
|---|---|---|---|---|
| Bourdon tube | 760 – 1 | 10⁵ – 100 | Mechanical deflection | No |
| Diaphragm (capacitance) | 760 – 10⁻⁴ | 10⁵ – 0.01 | Capacitance change | No |
| U-tube manometer | 760 – 1 | 10⁵ – 100 | Liquid column height | No |
| Pirani | 10 – 10⁻³ | 1300 – 0.1 | Thermal conductivity | Yes |
| Thermocouple | 5 – 10⁻³ | 650 – 0.1 | Thermocouple temperature | Yes |
| Convection-enhanced Pirani | 1000 – 10⁻⁴ | 10⁵ – 0.01 | Thermal conductivity + convection | Yes |
| Penning (cold cathode) | 10⁻³ – 10⁻⁷ | 0.1 – 10⁻⁵ | Ionization in magnetic field | Yes |
| Bayard-Alpert (hot cathode) | 10⁻³ – 10⁻¹¹ | 0.1 – 10⁻⁹ | Electron impact ionization | Yes |
| Spinning rotor | 10⁻² – 10⁻⁷ | 1 – 10⁻⁵ | Viscous drag on rotating ball | Mildly |

## Gauge Specifications

**Capacitance diaphragm gauge (CDG)**:

**Strengths**:
- Best accuracy in its range: ±0.5-1% of reading — gas-independent true total pressure
- No hot filament — no risk of burnout, can operate at any pressure
- High resolution: 0.01% of full scale

**Weaknesses**:
- Damaged by overpressure (>2× full scale) — requires protection valve
- Temperature sensitivity requires 15-30 minute warm-up for thermal equilibrium
- Limited range: each sensor covers ~4 decades of pressure

**Bayard-Alpert hot cathode ionization gauge (detailed)**:

**Strengths**:
- Widest measurement range: 10⁻³ – 10⁻¹¹ Torr (9 decades)
- Well-understood physics with standardized sensitivity factors for different gases
- X-ray limit of ~10⁻¹¹ Torr — sufficient for most UHV applications

**Weaknesses**:
- Hot filament (1800°C) burns out if operated above 10⁻³ Torr or exposed to oxygen
- Electron-stimulated desorption from grid creates false pressure readings during degassing
- Gas-dependent sensitivity requires correction factors for non-N₂ gases
- **Principle**: A thin metal diaphragm separates the vacuum system from a sealed reference cavity. A capacitance sensor on each side measures the diaphragm deflection. The pressure difference across the diaphragm causes proportional deflection, and the capacitance change is converted to a pressure reading.
- **Range**: 1000 – 10⁻⁴ Torr (multi-range models cover 1000-1, 100-10⁻², 10-10⁻⁴ Torr)
- **Accuracy**: ±0.5-1% of reading (best of any vacuum gauge in its range)
- **Gas independence**: Measures true total pressure regardless of gas composition (mechanical deflection, not gas-property dependent). This makes CDG the preferred gauge for process pressure monitoring where gas composition varies.
- **Resolution**: 0.01% of full scale
- **Temperature sensitivity**: Diaphragm deflection changes with temperature (thermal expansion). High-quality CDGs have internal temperature compensation (40-60°C operating range). Allow warm-up time of 15-30 minutes for the sensor to reach thermal equilibrium before taking readings.
- **Overpressure protection**: CDGs are damaged by pressures exceeding ~2× full scale. Install a protection valve that closes if pressure exceeds the gauge's rated range. Do not vent the system through a low-range CDG without isolation.

**Pirani gauge (detailed specifications)**:
- **Principle**: A heated wire (tungsten or platinum) in the vacuum system loses heat by gas conduction. At higher pressure, more gas molecules collide with the wire, conducting heat away faster. A Wheatstone bridge circuit compares the wire's resistance (proportional to temperature) to a reference.
- **Range**: 10 – 10⁻³ Torr (some extended range models: 1000 – 10⁻⁴ Torr)
- **Accuracy**: ±10-30% of reading (gas-dependent). Calibration is typically for N₂ or air. For other gases, apply correction factors:
  - Ar: multiply reading by ~0.7 (Ar has lower thermal conductivity than N₂ → gauge reads low)
  - He: multiply by ~1.0 (He has similar thermal conductivity to N₂)
  - H₂: multiply by ~0.5 (H₂ has much higher thermal conductivity → gauge reads high)
- **Response time**: 0.1-1 second (fast enough for most process monitoring)
- **Filament lifetime**: 5-10 years at normal operating temperatures. Filament degrades faster at higher pressures (oxidation, contamination). Do not operate a Pirani gauge at atmospheric pressure for extended periods — the filament overheats and burns out.

**Thermocouple gauge**:
- **Range**: 5 – 10⁻³ Torr
- **Accuracy**: ±20-50% of reading (less accurate than Pirani, but simpler and more robust)
- **Construction**: A heated filament with a welded thermocouple junction. The thermocouple directly measures filament temperature. As pressure drops, less gas conducts heat away, and the filament temperature rises. The thermocouple output voltage is calibrated to pressure.
- **Advantage**: Does not require a Wheatstone bridge circuit — simpler readout electronics. Often used as a roughing pump status indicator (switches a relay at a set pressure threshold).

**Bayard-Alpert hot cathode ionization gauge (detailed)**:
- **Principle**: A heated filament (thoriated tungsten, yttria-coated iridium, or thoria-coated iridium) emits electrons. Electrons are accelerated toward a helical grid (anode at +150-200 V). Gas molecules ionized by electron impact are collected on a thin central wire (collector at ground or slightly negative). Ion current I⁺ is proportional to gas density (pressure): I⁺ = S_g × I_e × P, where S_g is the gauge sensitivity factor (Torr⁻¹), I_e is the electron emission current, and P is pressure.
- **Range**: 10⁻³ – 10⁻¹¹ Torr
- **Sensitivity**: ~10/Torr for N₂ (varies by gas: Ar ~15/Torr, He ~2/Torr, H₂ ~3/Torr)
- **Emission current**: 0.1-10 mA (typical 1 mA). Lower emission for UHV measurements (reduces electron-stimulated desorption from the grid), higher emission for faster response at higher pressures.
- **X-ray limit**: The fundamental sensitivity limit of the Bayard-Alpert gauge. Soft X-rays produced when electrons hit the grid can strike the collector wire, generating photoelectrons that add to the ion current. This creates a false "pressure" signal independent of actual gas pressure. The BA gauge design (thin central collector) minimizes the solid angle subtended by the collector, reducing the X-ray current. X-ray limit: ~10⁻¹¹ Torr for a standard BA gauge, ~10⁻¹² Torr for an "extractor" gauge design.
- **Filament types**: Thoriated tungsten (high emission, cheap, but reacts with O₂ and hydrocarbons — avoid above 10⁻⁴ Torr). Yttria-coated iridium (oxidation-resistant, can survive brief air exposure — preferred for process tools). Thoria-coated iridium (highest emission, most robust).
- **Operating rules**: Do not turn on above 10⁻³ Torr (filament oxidizes rapidly). Always wait until roughing pump has reduced pressure below 10⁻³ Torr before degassing or operating the gauge. Degas function: electron-bombards the grid at high power (20-50 W) to desorb gas from the grid surface. Degas for 5-15 minutes after initial gauge turn-on or after a chamber vent.

**Penning (cold cathode) ionization gauge**:
- **Principle**: High voltage (2-5 kV) applied between cathode and anode in a magnetic field (~0.1 T from permanent magnet). Electrons spiral in the magnetic field, creating a self-sustaining gas discharge. Ion current is proportional to pressure.
- **Range**: 10⁻³ – 10⁻⁷ Torr
- **Advantages**: No hot filament (cannot burn out, rugged, can survive exposure to atmospheric pressure). Low power consumption. Used as a reliable indicator of high-vacuum conditions.
- **Disadvantages**: "Ignition delay" at very low pressures — the discharge may take seconds to minutes to start below 10⁻⁵ Torr, during which the gauge reads zero (falsely indicating lower pressure than actual). Limited accuracy (±50-100%). Can create contamination — sputtered cathode material deposits on nearby surfaces.

## Gauge Tubulation and Mounting

- **Connection location**: Mount gauges as close to the chamber as possible, on a short, wide tube. A gauge on a long, narrow tube reads a pressure that differs from the chamber pressure because of conductance-limited gas flow between chamber and gauge. For accurate readings: gauge tubulation ID ≥25 mm, length ≤50 mm.
- **Orientation**: Bayard-Alpert gauges should be mounted with the filament horizontal or vertical (filament down). Avoid filament-up orientation — the hot filament creates convection currents that affect the ionization environment.
- **Magnetic fields**: Ion gauges are sensitive to external magnetic fields (the electron trajectories in the gauge are affected). Keep ion gauges at least 30 cm from ion pumps, permanent magnets, or magnetically levitated turbopumps.
- **Stray light**: Do not expose ion gauge tubes to strong light — UV photons can generate photoelectrons at the collector, adding to the signal and causing falsely high pressure readings. Shield the gauge from direct light.

## Residual Gas Analyzer (RGA)

**Operating principle** (see also [Gas Handling: Vacuum](../gas-handling/vacuum.md) for basic RGA description):

The RGA is a miniature quadrupole mass spectrometer permanently mounted on the vacuum system. It ionizes gas molecules with a hot filament (electron impact at 70 eV), then separates ions by mass-to-charge ratio (m/z) using a quadrupole mass filter, and detects ions with a Faraday cup or electron multiplier.

**Quadrupole mass filter**: Four parallel rods with RF + DC voltages applied. Only ions of a specific m/z pass through the filter to the detector; all others collide with the rods. By scanning the RF/DC voltage ratio, the instrument sweeps through the mass range, measuring ion current at each mass.

**Performance specifications**:

| Parameter | Typical Value |
|---|---|
| Mass range | 1-100 amu (standard), 1-200 amu (extended) |
| Resolution | 0.5-1 amu (distinguishes adjacent masses) |
| Minimum detectable partial pressure | 10⁻¹³ Torr (with electron multiplier), 10⁻¹¹ Torr (Faraday cup) |
| Scan speed | 1-20 amu/second (for full scan); 0.1-1 second per mass (for selected ion monitoring) |
| Filament emission current | 0.1-1 mA |
| Operating pressure | <10⁻⁴ Torr (above this, filament and detector damaged) |

**Common mass spectra interpretation**:

| Mass (amu) | Gas | Source |
|---|---|---|
| 2 | H₂ | Outgassing from metals, dissociation of H₂O |
| 4 | He | Leak detection tracer, permeation through glass/O-rings |
| 12 | C (carbon fragment) | Organic contamination |
| 14 | N (fragment), N₂⁺⁺ | Air leak or N₂ background |
| 15 | CH₃ (fragment) | Organic contamination (pump oil, grease) |
| 16 | CH₄, O (fragment) | Methane from organic decomposition |
| 17 | OH, NH₃ (fragment) | Water vapor fragment |
| 18 | H₂O | Water vapor — dominant outgassing species |
| 28 | N₂, CO | Air leak (N₂) or outgassing from hot filaments (CO) |
| 32 | O₂ | Air leak |
| 40 | Ar | Air leak or argon process gas |
| 44 | CO₂ | Outgassing, atmospheric background |

**Diagnostic use cases**:

1. **Leak detection**: Spray helium outside the system while monitoring mass 4. A sudden increase in He partial pressure indicates the leak location. Sensitivity: ~10⁻¹² Pa·m³/s.

2. **Outgassing monitoring during bake-out**: Watch mass 18 (water) decrease as bake-out proceeds. When water peak drops below 10% of initial value and masses 2 (H₂) and 28 (CO) dominate, the bake is nearing completion.

3. **Process gas purity verification**: Before introducing process gas (e.g., Ar for sputtering), verify that the gas stream contains no contaminants (O₂, H₂O, N₂, hydrocarbons) that would degrade film quality. Connect the RGA to a tee in the gas line and sample during gas flow.

4. **Virtual leak diagnosis**: A virtual leak shows a constant or slowly decreasing atmospheric gas signature (N₂ at 28, O₂ at 32) that does not respond to external helium spray. A real leak shows a He response at mass 4 when sprayed.

5. **Contamination identification**: After a poor-quality deposition (e.g., hazy aluminum film), run an RGA scan. Hydrocarbon peaks (masses 15, 27, 29, 39, 41, 43, 55, 57) indicate oil contamination (from roughing pump backstreaming). Water peak (mass 18) indicates inadequate bake-out. Oxygen (mass 32) indicates air leak during deposition.

## Leak Detection Methods

**Helium mass spectrometer leak detection (primary method)**:

The helium leak detector is a dedicated mass spectrometer tuned to mass 4 (He), connected to the vacuum system via a valve. Two operational modes:

**Vacuum mode (spray probe)** — most common:
1. Connect leak detector to the vacuum system (at a port near the suspected leak, or on the roughing line).
2. The system is under vacuum, being pumped by the leak detector's internal turbo pump.
3. Spray a fine jet of helium gas (from a regulated cylinder with a fine nozzle) on the exterior surface, systematically working around all joints, welds, flanges, and feedthroughs.
4. When the helium spray passes over a leak, He enters the vacuum system and is detected by the mass spec within seconds (response time depends on internal volume and pumping speed).
5. Mark the location. Continue searching for additional leaks (systems often have multiple).
6. **Sensitivity**: 10⁻¹² atm·cc/s (can detect a leak so small it would take 30 years to leak 1 cc of gas).

**Sniffer mode (pressurized system)**:
1. Pressurize the system with helium (or He/N₂ mixture) to 1-2 bar above atmospheric.
2. Use a sniffer probe connected to the leak detector to scan exterior surfaces.
3. Helium escaping through leaks is drawn into the probe and detected.
4. **Sensitivity**: 10⁻⁷ atm·cc/s (much less sensitive than vacuum mode, but useful for large systems that cannot be evacuated).

**Helium leak detection best practices**:
- **Start from the top**: Helium is lighter than air and rises. Spray from the top of the system downward so that rising helium from a previous spray doesn't trigger a false positive at a higher location.
- **Enclose the spray area**: When testing a specific joint or flange, surround it with a plastic bag or tent. Spray helium into the enclosure and wait. This technique finds very small leaks that a transient spray might miss.
- **Background helium**: Helium is present in air at ~5 ppm. The leak detector automatically subtracts this background. But if the room has recently had helium sprayed (e.g., after extensive leak testing), the ambient He concentration rises, increasing background noise. Ventilate the room between leak testing sessions.
- **Virtual leaks vs. real leaks**: Helium leak detection only finds real leaks (holes communicating with the exterior). Virtual leaks (trapped internal volumes) do NOT show a He response because the trapped gas is already inside the system. Use the RGA to distinguish: virtual leaks show atmospheric gases (N₂, O₂) without He response.

**Bubble testing** (for gross leaks):
- Pressurize system to 1-2 bar above atmospheric with dry N₂.
- Apply commercial leak detection fluid (Snoop, or dilute dish soap) to all joints.
- Watch for bubble formation. Each bubble indicates a leak.
- Sensitivity: ~10⁻⁴ atm·cc/s (orders of magnitude less sensitive than He detection).
- Use for initial gross leak check before He testing, or for systems that cannot be evacuated.

**Pressure rise test** (for overall system integrity):
1. Pump the system to base pressure.
2. Isolate the system from all pumps (close all valves).
3. Monitor pressure rise over time.
4. Plot pressure vs. time. The curve has two components:
   - **Outgassing**: Initially rapid, follows 1/t decay. Dominates at short times (<1 hour).
   - **Real leak**: Constant pressure rise rate (linear with time). Dominates at long times (>1 hour) after outgassing has decreased.
5. The steady-state leak rate (slope of the linear portion) is: Q_leak = V × (dP/dt), where V is system volume and dP/dt is the pressure rise rate.
6. **Acceptable leak rates**:
   - Rough vacuum system: <10⁻³ Pa·L/s
   - High vacuum system: <10⁻⁶ Pa·L/s
   - UHV system: <10⁻⁹ Pa·L/s

**Ultrasonic leak detection**: Pressurize the system and scan with an ultrasonic detector (headphones + directional microphone tuned to 40 kHz). Gas flowing through a leak creates ultrasonic turbulence. Can detect leaks down to ~10⁻³ atm·cc/s. Useful for preliminary screening of large systems before He testing.

## Vacuum System Diagnostics

**Pump-down curve analysis**: Log pressure vs. time during pump-down. Compare to expected curve. Deviations indicate problems:

| Symptom | Likely Cause | Action |
|---|---|---|
| Pressure stalls at ~20 Torr | Roughing pump oil contaminated or low | Change oil, check gas ballast |
| Pressure stalls at ~10⁻¹ Torr | Leak or outgassing source | Pressure rise test, He leak check |
| Slow approach to base pressure | High outgassing (dirty chamber, new O-rings) | Bake the chamber |
| Pressure never reaches spec | Real leak | He leak detection |
| Pressure rises after reaching base, then slowly decreases | Virtual leak (trapped volume emptying) | Find and vent the trapped volume |
| Pressure spikes intermittently | Outgassing burst (desorbing chunk of contaminant) | Clean the chamber interior |
| RGA shows mass 28 increasing over time | CO from hot ion gauge filament, or slow air leak | Check mass 32 (O₂) — if present, air leak. If not, gauge outgassing. |

**RGA fingerprint of common problems**:

| Problem | RGA Signature |
|---|---|
| Air leak | Masses 28 (N₂) and 32 (O₂) in 4:1 ratio. Also mass 14 (N fragment) and 16 (O fragment). |
| Water outgassing | Mass 18 (H₂O) dominant, masses 16 (O) and 17 (OH) present. |
| Oil contamination | Masses 39, 41, 43, 55, 57 (hydrocarbon fragments). Mass 27 (C₂H₃). Characteristic "comb" pattern. |
| Elastomer (Viton) outgassing | Masses 69, 119, 169, 131 (fluorocarbon fragments from FKM decomposition). |
| Plasma process residual | Masses 69 (CF₃), 85 (C₂F₅), 50 (CF₂), 31 (CF) — fluorocarbon etch process residues. |
| Backstreaming from diffusion pump | Masses 39, 41, 43 (silicone oil fragments). If using Santovac: masses 77, 91, 115 (phenyl ether fragments). |
| Argon residual | Mass 40. From sputtering process gas or air leak. |
| Hydrogen in UHV | Mass 2. From stainless steel outgassing (H₂ dissolved in bulk metal diffuses to surface). Dominant residual gas in baked stainless steel UHV systems. |

## Gauge Calibration

**Primary standard — McLeod gauge**: Compresses a known volume of gas into a small capillary tube and measures the resulting pressure by the height of a mercury column. Provides an absolute pressure measurement (no calibration against another gauge needed). Range: 10 – 10⁻⁴ Torr. Accuracy: ±1-2%. Used as a transfer standard for calibrating other gauges. Being phased out due to mercury toxicity but remains the most accurate method for medium vacuum calibration.

**Spinning rotor gauge**: A steel ball levitated and spun at ~400 Hz inside a tube connected to the vacuum system. Gas molecules slow the ball by viscous drag. The deceleration rate is proportional to gas pressure and molecular weight. Range: 10⁻² – 10⁻⁷ Torr. Accuracy: ±1-3%. Used as a transfer standard for calibrating ion gauges and CDGs. Advantage: no hot filament, no ionization (truly non-perturbing).

**Calibration interval**: Vacuum gauges drift over time due to filament aging, contamination, and mechanical wear. Recommended calibration intervals:
- Pirani/thermocouple: 6-12 months
- CDG: 12 months
- Bayard-Alpert ion gauge: 6-12 months (or after filament replacement)
- Penning cold cathode: 12 months
- RGA mass scale: 6 months (mass scale calibration using known peaks: He at 4, N₂ at 28, Ar at 40)

## Gauge Protection

- **Interlocking**: Connect the ion gauge controller to a relay that closes the gate valve if pressure exceeds a threshold (e.g., 10⁻³ Torr). This protects the ion gauge filament from burning out during a sudden pressure burst (e.g., load lock valve accidentally opened). The same interlock can trigger an audible alarm.
- **Filament protection**: Never operate a Bayard-Alpert gauge above 10⁻³ Torr. The filament oxidizes rapidly in the presence of oxygen at high temperature. In process tools, install the ion gauge behind a throttle valve so that process pressure (which may be much higher than 10⁻³ Torr) does not reach the gauge.
- **RGA protection**: Install a gate valve between the RGA and the chamber. Close this valve during chamber vent and during high-pressure process steps. The RGA filament and electron multiplier are expensive and fragile.

## Safety

- **Mercury gauges**: McLeod gauges and some manometers contain mercury. Mercury vapor is toxic (TLV 0.025 mg/m³). A broken mercury manometer in a vacuum lab requires professional hazmat cleanup. Use electronic gauges wherever possible. If mercury gauges must be used, install them in a ventilated enclosure with a mercury vapor trap on the exhaust.
- **Ion gauge high voltage**: Bayard-Alpert gauges have 150-200 V on the grid and the filament runs at ~1800°C. Never touch the gauge connections while powered. Use insulated connectors. The gauge envelope is glass — handle carefully to avoid breakage.
- **Penning gauge high voltage**: 2-5 kV between electrodes. Maintain clearances per electrical safety standards. The magnetic field from the permanent magnet can attract ferromagnetic objects (keep steel tools away from the gauge body).


## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Bayard-Alpert ion gauge filament burns out immediately | Gauge turned on at pressure above 10⁻³ Torr — hot filament (1800°C) oxidizes rapidly in presence of oxygen | Always verify pressure is below 10⁻³ Torr via Pirani/thermocouple before activating ion gauge; install interlock relay that prevents gauge turn-on above threshold; replace filament with yttria-coated iridium (survives brief air exposure) |
| Pirani gauge reads 30% high when measuring argon | Gas-dependent calibration — Ar has lower thermal conductivity than N₂ (calibration gas), gauge reads low, not high — actually reading is gas-dependent | Apply correction factor: for Ar multiply reading by ~0.7; for H₂ multiply by ~0.5 (H₂ reads high due to high thermal conductivity); always use gas-specific correction factors when gas composition is known |
| CDG reading drifts during first 30 minutes after power-on | Temperature sensitivity — diaphragm thermal expansion affects deflection until internal temperature compensator stabilizes | Allow 15-30 minute warm-up for thermal equilibrium before taking readings; verify sensor is in its 40-60°C operating range; if drift persists after warm-up, recalibrate gauge against spinning rotor standard |
| RGA shows unexpected mass 28 (N₂) and 32 (O₂) in 4:1 ratio during pump-down | Real air leak — atmospheric N₂ and O₂ entering system through a seal or fitting | Perform helium leak detection (spray probe, vacuum mode); monitor mass 4 while spraying He at flanges, welds, and feedthroughs; sensitivity ~10⁻¹² atm·cc/s; fix leak and verify with pressure rise test (Q_leak = V × dP/dt) |
| Penning cold cathode gauge reads zero at 10⁻⁶ Torr | Ignition delay — discharge has not started at very low pressure; gauge falsely indicates lower pressure than actual | Wait 1-5 minutes for discharge to ignite; alternatively, briefly raise pressure to >10⁻⁴ Torr to strike the discharge then pump back down; do not trust Penning readings during ignition delay period |
| Pressure rise test shows linear (constant) leak rate after 1 hour | Real leak — constant pressure rise rate indicates gas entering from outside (vs. outgassing which follows 1/t decay) | Calculate Q_leak = V × (dP/dt); compare to acceptable limits (HV: <10⁻⁶ Pa·L/s, UHV: <10⁻⁹ Pa·L/s); perform helium spray probe leak detection to locate; repair and re-test |
| RGA shows hydrocarbon "comb" pattern at masses 39, 41, 43, 55, 57 | Oil contamination — backstreaming from diffusion pump or rotary vane roughing pump | Check LN₂ cold trap level on diffusion pump; verify oil mist eliminator on rotary vane exhaust; check that roughing pump is not operated at high throughput without gas ballast; consider switching to oil-free scroll backing pump |
| Ion gauge X-ray limit prevents measurement below 10⁻¹¹ Torr | Soft X-rays from electron-grid impacts generating photoelectrons at collector — fundamental BA gauge limit | Upgrade to extractor gauge design (X-ray limit ~10⁻¹² Torr); or use spinning rotor gauge for calibration at these pressures; verify gauge has been degassed (5-15 min at 20-50 W) to remove electron-stimulated desorption artifacts |
| Helium leak detector background too high to find small leaks | Room contaminated with helium from previous testing — ambient He >5 ppm normal background | Ventilate room thoroughly between leak testing sessions; allow 15-30 minutes for background to drop; check leak detector's internal He background reading before starting; use plastic bag enclosure technique for small leak isolation |
| Gauge reading disagrees with expected pressure by >50% after recent calibration | Gauge tubulation too long and narrow — conductance-limited gas flow between chamber and gauge reading differs from chamber pressure | Mount gauges with tubulation ID ≥25 mm and length ≤50 mm; for high-speed pumps (>100 L/s) this is especially critical; verify gauge is on a short, wide port directly on the chamber |

## See Also

- **[Gas Handling: Vacuum](../gas-handling/vacuum.md)**: Basic vacuum gauge principles, bubble testing, Tesla coil
- **[Vacuum Pumps](pumps.md)**: Pump selection and specifications
- **[Vacuum Chambers & Sealing](chambers.md)**: Chamber design and virtual leak prevention
- **[Measurement](../measurement/index.md)**: General measurement and instrumentation


[← Back to Vacuum](index.md)
