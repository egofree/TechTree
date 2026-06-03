# Soldering Iron

> **Node ID**: electronics.soldering-iron
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`energy.electricity`](../energy/electricity.md), [`ceramics.insulators`](../ceramics/index.md)
> **Enables**: [`electronics.assembly`](assembly.md), [`electronics.electrical-systems`](electrical-systems.md)
> **Timeline**: Years 15-25
> **Outputs**: soldered_joints, reworked_assemblies
> **Critical**: Yes — no electronic circuit can be assembled or repaired without a reliable heat source for soldering; the soldering iron is the single most essential tool in electronics

## Principle

A soldering iron converts electrical energy into heat at a concentrated tip, raising the temperature of metal workpieces and solder alloy above the solder's melting point. The molten solder wets the metal surfaces through metallurgical bonding — a thin intermetallic layer (1-5 μm) forms between the solder and the base metal, creating both electrical continuity and mechanical attachment. The iron maintains tip temperature at 320-420°C, well above the melting points of common solders (Sn63/Pb37: 183°C; SAC305 lead-free: 217-220°C), providing sufficient thermal headroom to overcome heat sinking by the workpiece and PCB substrate.

Heating is achieved by passing current through a resistive element (nichrome wire or ceramic PTC heater) embedded in the iron body. The thermal mass of the tip stores heat and delivers it to the joint in a brief 2-5 second contact. Temperature-controlled irons use a thermocouple or thermistor in the tip, feeding back to a power controller (triac or MOSFET) that maintains the set temperature within ±5-10°C.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Copper rod (tip) | 1 piece, 30-60 mm × 6-10 mm | OFHC copper, >99.9% purity | [Electrolysis](../chemistry/electrolysis.md) | Copper-clad steel (lower thermal conductivity) |
| Nichrome wire (heater) | 0.5-1.0 m | NiCr 80/20, 28-34 AWG (0.16-0.32 mm), resistance 6-15 Ω/m | [Wire drawing](../machine-tools/machining.md) | Kanthal A1 (higher temperature rating) |
| Ceramic tube (insulator) | 1 piece, 40-70 mm | Alumina or mullite, ID 4-8 mm, OD 8-14 mm, rated >500°C | [Ceramics](../ceramics/index.md) | Mica sheet wrapped in layers (fragile) |
| Steel tube (body) | 1 piece, 80-120 mm | Mild steel or stainless, ID 10-16 mm, wall 1-2 mm | [Iron & Steel](../metals/iron-steel.md) | Brass tube (softer, conducts heat to handle) |
| Wooden or phenolic handle | 1 piece | Hardwood (oak, beech) or [phenolic resin](../polymers/thermosets.md), 80-120 mm, turned to 20-30 mm diameter | [Foundations](../foundations/tools-basic.md) | Ceramic handle (heavier) |
| Power cord | 1-2 m | Stranded copper, 18-20 AWG, with [PVC insulation](../polymers/thermoplastics.md), rated 300V, 3A minimum | [Electrical Systems](electrical-systems.md) | Cloth-insulated wire (less safe) |
| Iron-plating for tip | Optional | Electroplated iron, 50-150 μm over copper core | [Electroplating](../electrochemistry/electroplating.md) | Bare copper tip (wears faster, needs frequent dressing) |
| Stainless steel set screw | 1-2 | M3 or M4, for securing tip and electrical connection | [Fasteners](../metals/fasteners.md) | Split collar clamp |

## Construction Steps

### Basic Soldering Iron (Uncontrolled, 25-40 W)

1. **Form the copper tip**: Turn or file the copper rod to the desired tip shape. A chisel tip (4-5 mm wide, 1-2 mm thick at the business end) is the most versatile. The shank end (10-15 mm) should be a sliding fit inside the ceramic insulator. Clean the copper to bare metal with abrasive paper.
2. **Wind the heater element**: Measure the required resistance for the target wattage at your supply voltage. For a 40 W iron on 230 V: R = V²/P = 230²/40 = 1323 Ω. For 120 V: R = 120²/40 = 360 Ω. Wind nichrome wire in a close spiral around the ceramic tube, starting 15 mm from one end and extending 30-40 mm. Leave 20 mm pigtails at each end for electrical connection. Secure the ends by passing through small holes drilled in the ceramic or by crimping with stainless steel ferrules.
3. **Assemble the heating element**: Slide the ceramic tube with wound heater over the copper tip shank. The heater section should surround the thick part of the tip (not the pointed end). The copper shank should extend 5-10 mm past the ceramic to allow tip changing.
4. **Install in the steel body tube**: Slide the ceramic + heater assembly into the steel tube. The steel tube protects the ceramic from mechanical damage and provides a grip surface. Fill any gap between ceramic and steel with a thin layer of ceramic fiber or mica to prevent rattling and reduce heat loss.
5. **Make electrical connections**: Connect one nichrome pigtail to the copper tip (this provides one pole through the tip to the workpiece for grounded operation). Connect the other pigtail to one conductor of the power cord. Connect the second power cord conductor to the steel body (for a grounded tip configuration) or to a separate ring terminal that contacts the tip via a set screw. Use crimped ring terminals on all connections. Insulate connections with ceramic fiber or glass-fiber sleeving.
6. **Mount the handle**: Bore a hole in the wooden handle matching the steel tube OD (tight fit). Apply heat-resistant epoxy (or friction-fit) to secure the steel tube in the handle. Route the power cord through a hole drilled in the handle and add a strain relief (cable gland or knot inside the handle).
7. **Shape and tin the tip**: Before first use, heat the iron and apply solder with flux to the tip. The solder should flow and coat the tip in a thin, shiny layer ("tinning"). A tinned tip transfers heat efficiently and resists oxidation.

### Temperature-Controlled Soldering Iron (50-80 W)

8. **Add thermocouple**: Embed a Type K thermocouple (chromel-alumel, 0.5 mm wire) in a small hole drilled in the copper tip, 3-5 mm from the working end. Secure with high-temperature ceramic cement (alumina-based, rated >800°C). Route the thermocouple wires alongside the heater through the body to the handle.
9. **Build the controller**: Construct a temperature controller using a thermocouple amplifier (op-amp circuit with cold-junction compensation), a comparator with setpoint adjustment (potentiometer), and a power switching element (triac for AC or MOSFET for DC). The controller modulates power to the heater to maintain the set tip temperature. For a simple implementation: use a 555-timer-based PWM circuit driving a MOSFET, with the thermocouple voltage compared against a reference set by a potentiometer. Calibrate by measuring tip temperature with a separate thermocouple at the setpoint.

## Calibration and Verification

1. **Tip temperature check**: Measure the tip temperature with a thermocouple or temperature-indicating crayon (marks melt at specific temperatures). Verify the tip reaches 350-380°C (Sn/Pb soldering) or 380-420°C (lead-free) within 60-120 seconds of power-on.
2. **Thermal recovery test**: Apply the tip to a large copper bus bar (10 × 10 × 2 mm) for 5 seconds, simulating a heavy thermal load. Remove and measure time for the tip to recover to within 10°C of set temperature. Recovery time: 5-15 seconds for a 40 W iron, 2-8 seconds for an 80 W iron.
3. **Leakage current test**: Measure AC leakage current from the tip to ground with the iron energized. Must be <2 mA for ESD-safe operation. High leakage indicates insufficient insulation between heater and tip.
4. **Handle temperature check**: Run the iron at maximum temperature for 30 minutes. Measure handle temperature at the grip point. Must remain below 50°C — if hotter, add a thermal break (air gap or phenolic washer) between steel body and handle.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Tip temperature (uncontrolled, 40 W) | 300-420°C (varies with load and supply voltage) |
| Tip temperature (controlled, 80 W) | Set ±5°C (typical 200-480°C range) |
| Heat-up time to 350°C | 60-120 seconds (40 W), 30-60 seconds (80 W) |
| Thermal recovery time | 5-15 seconds (40 W), 2-8 seconds (80 W) |
| Tip-to-joint thermal resistance | 20-50°C/W (copper tip, tinned) |
| Power consumption | 25-40 W (standard), 50-80 W (temperature-controlled) |
| Tip life (copper, bare) | 20-50 hours of active soldering before reshaping required |
| Tip life (iron-plated) | 500-2000 hours before plating failure exposes copper |
| Duty cycle | Continuous (derate uncontrolled iron to 70% for long sessions) |
| Service life (before heater replacement) | 1000-5000 hours (nichrome), 5000-10000 hours (ceramic heater) |

## Strengths

- Simple construction from copper, nichrome wire, and ceramic — all achievable with Year 15 materials
- Copper tip provides excellent thermal conductivity (401 W/m·K) for rapid heat transfer to joints
- Temperature-controlled variants enable consistent soldering across varying workpiece sizes and lead-free alloys

## Weaknesses

- Uncontrolled irons drift with supply voltage fluctuations (±10% line voltage causes ±20-30°C tip variation)
- Copper tips erode rapidly in contact with solder — bare copper requires reshaping every 20-50 hours
- No ESD-safe construction without isolated heater and grounded tip design

## Safety

- **Thermal burns**: Tip temperature of 350-420°C causes immediate second-degree burns on skin contact. Always return the iron to a stable rest (metal cradle, not the workbench) when not actively soldering. The rest must be heavy enough to resist tipping.
- **Lead exposure**: When using Sn63/Pb37 solder, wash hands thoroughly before eating or drinking. Lead oxide fume generation is minimal at normal tip temperatures (<500°C) but hand-to-mouth contamination from handling solder wire is the primary risk.
- **Solder fumes**: The visible "smoke" from soldering is flux vapor (colophony), not metal fume. Use local exhaust ventilation or a fume extractor with activated carbon filter positioned 5-15 cm from the joint. Capture velocity: 0.3-0.5 m/s.
- **Electrical safety**: Ensure the iron body and tip are properly grounded. A fault in the heater insulation can apply line voltage to the tip — lethal if the user touches both the tip and a grounded surface. Use a 3-wire cord with ground. Inspect cord integrity before each use.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Tip will not tin (solder balls off) | Oxidized tip surface or insufficient temperature | Clean tip with brass wire wool (not file — damages plating); apply fresh solder with flux; verify tip temperature >300°C |
| Tip temperature too low | Heater element partially failed, poor electrical connection, or low supply voltage | Measure heater resistance (should match design: V²/R); check set screw connections; verify supply voltage |
| Tip eroding rapidly (copper) | Bare copper tip with no plating, high solder volume | Iron-plate the tip or accept frequent reshaping as maintenance; keep tip tinned when not in use |
| Handle getting hot | Insufficient thermal break between heater body and handle | Add phenolic washer or increase air gap; wrap steel body with glass-fiber tape near the handle |
| Iron takes too long to heat up | Heater resistance too high (too many turns of nichrome) or low voltage | Recalculate nichrome length for target wattage; verify supply voltage matches design |
| Solder joints look dull and grainy | Tip temperature too low, insufficient flux, or iron not making good thermal contact | Increase temperature; apply fresh flux; ensure tip is tinned and contacts both pad and lead simultaneously |

## See Also

- [Electronics Assembly](assembly.md) — soldering procedures and joint quality standards
- [Electrical Systems](electrical-systems.md) — wiring harness assembly using soldering irons
- [Power Electronics](power-electronics.md) — high-power assembly requiring temperature-controlled irons
- [Electrolysis](../chemistry/electrolysis.md) — copper production for soldering iron tips
- [Ceramics](../ceramics/index.md) — ceramic insulators for heater construction

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](./index.md) • [All Domains](../index.md)*
