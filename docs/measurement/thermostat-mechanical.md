# Mechanical Thermostats

> **Node ID**: measurement.thermostat-mechanical
> **Domain**: [Measurement](./index.md)
> **Dependencies**: [`metals`](../metals/copper-bronze.md), [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.forming`](../machine-tools/forming.md)
> **Enables**: [`measurement.thermostat-fluid`](./thermostat-fluid.md), [`measurement.thermostat-electrical`](./thermostat-electrical.md)
> **Critical**: No — manual temperature monitoring is a functional alternative
> **Timeline**: Years 5-20
> **Outputs**: on_off_control, temperature_switching, mechanical_actuation


Mechanical thermostats use thermal expansion of metals to actuate switches without any external power source. They range from the simplest possible temperature switch (a single metal rod pushing a contact) to mass-produced bimetallic discs that protect billions of appliances. All four types covered here share the same operating principle: differential thermal expansion of metals produces mechanical motion that trips a switch. They require only basic metalworking to build and operate reliably across millions of cycles.


## Single-Metal Expansion Rod Thermostat

**Principle**: A long metal rod expands linearly when heated. Linear thermal expansion follows ΔL = L₀ × α × ΔT, where L₀ is original length, α is the coefficient of thermal expansion, and ΔT is the temperature change. A 500 mm iron rod (α ≈ 12 × 10⁻⁶/°C) grows 0.6 mm per 100°C of heating. One end of the rod is fixed; the other end pushes against a spring-loaded lever or electrical contact. When the rod grows enough, it trips the mechanism, breaking the circuit or closing a draft damper.

**Prerequisites**:
- [Iron or bronze forging, filing](../metals/iron-steel.md)
- [Lever mechanism](../machine-tools/forming.md) or spring-loaded contact
- Flat reference surface for mounting

**Materials**:
- [Iron rod](../metals/iron-steel.md) or [bronze rod](../metals/copper-bronze.md) (10-15 mm diameter, 400-600 mm length)
- [Mounting bracket](../metals/iron-steel.md) (cast iron or forged steel)
- [Leaf spring](../metals/iron-steel.md) or [coil spring](../metals/iron-steel.md) (steel, 5-20 N force)
- [Electrical contact points](../metals/copper-bronze.md) (brass or copper strips, 1-2 mm thick) or mechanical lever for damper control
- [Adjustable set screw](../machine-tools/machining.md) (threaded steel, 6-8 mm) with locknut

**Construction**:

1. **Prepare the rod**: Forge or machine the iron rod to 500 mm length, 12 mm diameter. File both ends flat and perpendicular to the rod axis. Any tilt on the contact end introduces angular error that changes the effective contact point as the rod expands. Polish the last 20 mm of the free end to a smooth finish for consistent contact.

2. **Build the mounting bracket**: Cast or forge a bracket with a rigid clamping block at one end. The clamping block must grip the rod firmly and act as the fixed (cold) reference point. Drill and tap a hole for the 8 mm set screw perpendicular to the rod axis, about 5 mm from the free end of the rod. The set screw adjusts how far the rod must expand before tripping the contact.

3. **Install the contact mechanism**: Mount two brass contact strips (1 mm thick, 15 mm wide, 40 mm long) on insulating spacers (ceramic or hardwood) on either side of the set screw. Wire these contacts into the heater circuit. When the rod expands, it pushes the set screw into the first contact strip, which bridges to the second, completing or breaking the circuit.

4. **Add the return spring**: Install a leaf spring (steel, 0.5 mm thick, 15 mm wide) pressing the rod back toward its cold position. This ensures positive mechanical contact and prevents the rod from hanging up after cooling. Spring force should be 5-10 N: enough to maintain contact but not enough to bend the rod.

5. **Mount the assembly**: Bolt the bracket rigidly to a heavy base plate (cast iron, 10 mm thick). The base plate anchors the fixed end and prevents frame flexure from being mistaken for thermal expansion. Any movement in the mount reads as false temperature change.

**Calibration**:

1. Place the entire thermostat in a temperature-controlled environment (oven or heated oil bath). Use a reference thermometer (see [Temperature & Pressure](./temperature-pressure.md)) to monitor actual temperature.
2. Start cold. Adjust the set screw until the contacts just close (measure with an ohmmeter or connect a lamp in series).
3. Heat slowly (2-3°C/minute). Record the temperature at which contacts open.
4. Cool slowly. Record the temperature at which contacts close again. The difference between opening and closing temperatures is the deadband, typically 5-15°C for this type due to friction and mechanical play.
5. Adjust set screw to shift the trip point. Repeat until the trip temperature matches the desired setpoint.

**Expected accuracy**: ±10-20°C over 100-800°C range. The deadband (hysteresis between on and off) is 5-15°C. This is crude but functional for furnace draft control and simple kiln regulation.

**Applications**: Furnace draft damper control, simple kiln temperature limiting, oven safety cutoff. Use this when you need *some* temperature regulation and have only basic metalworking. The rod-and-tube design (next) is strictly better when you can fabricate tubes.

**Strengths**:
- Simplest possible thermostat to build, requiring only basic metalworking
- No power source needed; operates purely on thermal expansion
- Works at very high temperatures (up to 800°C with iron)
- Mechanically robust with few wearing parts
- Field-adjustable setpoint via set screw

**Weaknesses**:
- Very low sensitivity; requires a long rod (500 mm) for usable motion
- Wide deadband (5-15°C) due to friction and mechanical play
- Accuracy of only ±10-20°C, unsuitable for precise work
- Mounting flexure introduces false temperature readings
- Slow response due to large thermal mass of the rod


## Rod-and-Tube Thermostat

**Principle**: A low-expansion rod (iron or steel, α ≈ 12 × 10⁻⁶/°C) runs inside a high-expansion tube (copper or brass, α ≈ 17-19 × 10⁻⁶/°C). Both are fixed together at one end. When heated, the tube grows faster than the rod, creating relative displacement between the free ends. The differential expansion ΔL = L₀ × (α_tube - α_rod) × ΔT amplifies the usable motion compared to a single-metal rod, since both elements respond to the same temperature but at different rates.

**Prerequisites**:
- [Metal tube drawing](../metals/copper-bronze.md) (capillary tube, 1-3 mm OD)
- [Brazing or welding capability](../machine-tools/joining.md)
- Two metals with different thermal expansion coefficients
- [Basic machining](../machine-tools/machining.md) (lathe for turning rod to fit inside tube)

**Materials**:
- [Outer tube: copper or brass](../metals/copper-bronze.md) (10 mm OD, 8 mm ID, 300-500 mm length)
- [Inner rod: iron or steel](../metals/iron-steel.md) (7.5 mm diameter, same length as tube, sliding fit inside)
- [Mounting flange: steel or brass disc](../metals/copper-bronze.md) (30 mm diameter, 3 mm thick) brazed to one end of both tube and rod
- [Contact mechanism](../metals/copper-bronze.md): brass contact strips, adjustable set screw with locknut
- [Return spring](../metals/iron-steel.md) (steel, 3-5 N)

**Construction**:

1. **Prepare the tube**: Draw or procure a copper tube (10 mm OD, 8 mm ID, 400 mm long). Anneal by heating to dull red (600-650°C) and quenching in water. This softens the copper for easier assembly and relieves residual stresses that would cause drift.

2. **Prepare the rod**: Turn an iron rod on a lathe to 7.5 mm diameter (0.5 mm clearance inside the 8 mm bore). Polish the surface smooth. The sliding fit must be free but not loose: too tight and the rod seizes when heated (differential expansion can bind the assembly), too loose and the rod rattles, causing erratic contact.

3. **Fix one end**: Braze both the rod and tube to a brass flange at one end. The rod must be centered in the tube. Use a spacer ring (copper wire, 0.5 mm thick) wrapped around the rod at the free end to maintain centering. The braze joint at the flange must be solid and leak-tight; any movement here reads as false temperature signal.

4. **Install contact mechanism**: At the free end, the rod protrudes slightly beyond the tube (about 1 mm at room temperature). Mount an adjustable contact screw opposite the rod end. As temperature rises, the tube grows more than the rod, and the rod end retreats *into* the tube. The relative motion is about 2.5 mm per 100°C for a 400 mm copper/iron assembly (Δα ≈ 6 × 10⁻⁶/°C).

5. **Add linkage to heater circuit**: Connect the contact screw and rod (through the flange) to the heater control circuit using insulated wire. The circuit closes when the rod contacts the screw, and opens as the rod retreats with heating.

**Calibration**:

1. Place the assembly in a calibration oven with a [reference thermometer](./temperature-pressure.md).
2. At room temperature, adjust the contact screw until the circuit just closes.
3. Heat to the desired trip temperature. The circuit opens as the rod retreats.
4. Fine-tune by adjusting the screw. Each full turn of an M6 screw (1 mm pitch) shifts the trip point by approximately 1/(L₀ × Δα) ≈ 40°C per mm of screw travel. One quarter turn shifts it about 10°C.
5. Lock the set screw with its locknut. Recheck trip point after locking.

**Expected accuracy**: ±5-10°C over 50-800°C range. Deadband 3-8°C. Better than the single-metal rod because the differential motion is easier to sense precisely.

**Applications**: Oven temperature control, kiln regulation, furnace safety cutoff. The rod-and-tube principle is the direct ancestor of modern gas appliance safety valves (thermocouples replaced it, but the differential expansion concept remains in many industrial controls).

**Strengths**:
- Better sensitivity than a single-metal rod through differential expansion
- More compact than the single-metal rod for the same usable motion
- No power source required
- Adjustable setpoint via contact screw
- Moderate accuracy (±5-10°C) suitable for many kiln and oven applications

**Weaknesses**:
- Requires tube-drawing capability, a step up in metalworking skill
- Sliding fit between rod and tube can bind at high temperatures
- Differential expansion still produces modest motion, limiting precision
- Mechanical deadband of 3-8°C prevents tight control
- Spring must be carefully calibrated to avoid overriding the expansion force


## Bimetallic Strip Thermostat

**Principle**: Two metal strips with different thermal expansion coefficients are bonded together along their entire length. When heated, the high-expansion side grows more than the low-expansion side, but the bond prevents independent movement. The strip must bend to accommodate the differential, curving toward the low-expansion side. The deflection of a cantilever bimetallic strip is approximately D = K × (L²/t) × ΔT, where K is a constant depending on the two metals, L is the length, t is total thickness, and ΔT is temperature change. Longer and thinner strips produce more deflection.

**Prerequisites**:
- [Rolling mill](../machine-tools/forming.md) (to produce thin, uniform metal strips)
- Two metals with different expansion coefficients (e.g., [brass](../metals/copper-bronze.md) α ≈ 19 × 10⁻⁶/°C + [steel](../metals/iron-steel.md) α ≈ 12 × 10⁻⁶/°C, or [steel](../metals/iron-steel.md) + [invar](../metals/alloys.md) α ≈ 1.2 × 10⁻⁶/°C)
- [Bonding method](../machine-tools/joining.md): riveting, brazing, or explosive welding
- [Spring tempering](../metals/iron-steel.md) capability

**Materials**:
- [Brass strip](../metals/copper-bronze.md) (high-expansion side): 0.3 mm thick, 12 mm wide, 100 mm long, half-hard temper
- [Steel strip](../metals/iron-steel.md) (low-expansion side): 0.3 mm thick, 12 mm wide, 100 mm long, spring temper
- [Brass rivets](../metals/copper-bronze.md) (1.5 mm diameter, 4-5 mm long), 6-8 pieces
- [Contact point: silver](../metals/precious-metals.md) or [tungsten](../metals/refractory-metals.md) contact tip (2-3 mm diameter) brazed to the free end
- [Adjustable contact screw](../metals/copper-bronze.md) (brass, M4) with locknut
- [Mounting bracket](../metals/iron-steel.md) (steel)

**Construction**:

1. **Prepare the strips**: Roll the brass and steel strips to 0.3 mm thickness with ±0.02 mm uniformity. Thickness variation across the width or length causes uneven bending and unpredictable calibration. Anneal the brass strip at 400°C for 30 minutes to remove rolling stresses. Do *not* anneal the steel strip; it needs spring temper for snap-action behavior.

2. **Bond the strips**: Clamp the two strips together with the brass on one side and steel on the other. Drill rivet holes (1.6 mm) through both strips at 6-8 positions along the center line, spaced about 15 mm apart. Insert brass rivets from the brass side and peen tight on the steel side. The bond must be intimate: any gap between the strips allows independent movement, reducing bending force and making the thermostat erratic. Alternatively, braze the strips together using silver solder (flows at 620°C, below the melting point of either metal) along the full length, then roll to final thickness.

3. **Form the cantilever**: Clamp one end of the bonded strip firmly in a mounting bracket (steel, 3 mm thick, with a clamping bar and two M4 bolts). The free end extends 80-100 mm. The brass side faces the direction you want the strip to bend *away from* when heated (brass expands more, so the strip bends toward the steel side).

4. **Install contacts**: Braze a silver contact tip (2 mm diameter) to the free end of the strip on the steel side. Mount an adjustable brass contact screw (M4, with locknut) on a bracket positioned so the strip contact tip touches the screw at the trip temperature. Wire the strip and the screw into the heater circuit through insulated connections.

5. **Add snap-action (optional but recommended)**: A plain bimetallic strip bends gradually, which means contacts separate slowly, causing arcing and burning. To add snap-action, slightly overbend the strip past flat (give it a slight initial curve toward the brass side, about 2-3 mm of camber over its length). The stored elastic energy causes the strip to snap suddenly between positions rather than creeping. This dramatically reduces arcing and extends contact life.

**Calibration**:

1. Mount the thermostat in a calibration oven with a [reference thermometer](./temperature-pressure.md).
2. At room temperature, adjust the contact screw until the contacts just touch (circuit closes, measure with ohmmeter or test lamp).
3. Heat slowly. Record the temperature at which the contacts snap open.
4. Adjust the contact screw: turning it inward (toward the strip) raises the trip temperature, backing it out lowers it. Each quarter turn of the M4 screw (0.35 mm pitch) shifts the trip point by roughly 2-5°C depending on strip geometry.
5. Check both heating and cooling trip points. The deadband (hysteresis) should be 3-8°C for a snap-action strip, or 1-3°C for a plain strip without snap-action.
6. Verify at 3-5 different setpoints across the intended range by adjusting the screw.

**Expected accuracy**: ±2-5°C over -50 to 500°C range. The fundamental limit is the consistency of the bimetallic bond and the uniformity of the strip thickness.

**Applications**: Home heating thermostats, oven temperature control, refrigerator defrost control, industrial furnace safety cutoffs, electric iron temperature regulation. The bimetallic strip is probably the most widely produced thermostat type in history, with billions manufactured. It requires no power, no fluids, and no electronics. Its main limitation is moderate accuracy and limited ability to control temperature tightly.

**Strengths**:
- Requires no power, no fluids, and no electronics
- Mass-producible once rolling mill capability exists
- Snap-action version provides clean switching with minimal arcing
- Wide operating range (-50 to 500°C)
- Adjustable setpoint in the field
- Billions manufactured; extremely well-proven design

**Weaknesses**:
- Moderate accuracy (±2-5°C) insufficient for precision applications
- Contact points wear and oxidize over millions of cycles
- Bond integrity between strips can degrade at extreme temperatures
- Calibration drifts with mechanical fatigue over years of cycling
- Deadband of 1-8°C prevents tight temperature regulation
- No remote sensing capability; sensor must be at the control point


## Bimetallic Snap-Action Disc Thermostat

**Principle**: A shallow dished disc stamped from bimetallic sheet stores elastic energy in its curved shape. As temperature rises, differential expansion builds stress in the disc. At a critical temperature, the stress overcomes the geometric stability of the dome, and the disc snaps suddenly to an inverted curvature. This snap transition is extremely fast (milliseconds) and produces a clean, decisive mechanical motion ideal for switching. The snap temperature is determined by the disc geometry (diameter, dish depth, thickness) and the bimetallic combination. Once set by stamping, the trip temperature is fixed.

**Prerequisites**:
- [Rolling mill](../machine-tools/forming.md) (to produce thin, uniform metal strips)
- Two metals with different expansion coefficients (e.g., [brass](../metals/copper-bronze.md) + [steel](../metals/iron-steel.md), or [steel](../metals/iron-steel.md) + [invar](../metals/alloys.md))
- [Bonding method](../machine-tools/joining.md): riveting, brazing, or explosive welding
- [Spring tempering](../metals/iron-steel.md) capability
- [Precision stamping dies](../machine-tools/machining.md) (for repeatable disc geometry)
- [Spring-tempered bimetallic sheet stock](../metals/alloys.md)

**Materials**:
- [Bimetallic sheet](../metals/alloys.md) (steel/brass or steel/invar, 0.3-0.5 mm thick, stamped to 15-25 mm diameter discs)
- [Silver contact points](../metals/precious-metals.md) (2 mm diameter, brazed to disc center on both sides)
- [Housing](../metals/copper-bronze.md): steel or brass cup (30 mm diameter, 10 mm deep) with mounting threads
- [Electrical terminals](../metals/copper-bronze.md) (brass, riveted to housing)

**Construction**:

1. **Stamp the disc**: Cut discs from bimetallic sheet using a precision stamping die. The die controls two critical parameters: the disc diameter (controls force and stroke) and the dish depth (controls the trip temperature). Deeper dishes snap at higher temperatures. Typical disc: 20 mm diameter, 0.4 mm thick, dished to 0.8-1.2 mm center height. The stamping die must be hard and accurate: a 0.05 mm variation in dish depth shifts the snap temperature by 5-10°C.

2. **Heat-treat for stability**: After stamping, heat the discs to 350°C for 2 hours and cool slowly. This stress-relieves the cold-worked metal and stabilizes the snap temperature. Skipping this step causes the trip point to drift 5-10°C over the first few hundred thermal cycles as residual stresses relax.

3. **Attach contacts**: Braze silver contact points (2 mm diameter) to the center of each side of the disc. The contacts carry the switching current. Silver resists oxidation and maintains low contact resistance even after thousands of cycles.

4. **Assemble in housing**: Place the disc in the brass or steel housing cup. The disc sits on a shoulder inside the cup with just enough clearance to move freely when it snaps. The housing has two electrical terminals: one connected to the disc (through a spring finger pressing on the disc center), the other to the housing body. When the disc is in the "cold" position, the contacts are closed (circuit on). When it snaps to the "hot" position, the center lifts off the spring finger, opening the circuit.

5. **Seal the housing**: Crimp or solder a cap onto the housing to seal the disc from contamination. Dust or corrosion on the contact surfaces causes resistance buildup and eventual failure.

**Calibration**:

1. Calibrate by batch testing. Place a sample of discs (5-10% of each production batch) in a calibration oven.
2. Heat slowly (1°C/minute) and record the snap temperature for each disc using a reference thermometer.
3. If the batch mean is more than ±3°C from the target trip temperature, adjust the stamping die (increase dish depth to raise trip point, decrease depth to lower it) and re-stamp.
4. Disc-to-disc variation should be ±2-3°C. Reject individual discs that fall outside this range.

**Expected accuracy**: ±2-3°C at a fixed, factory-set temperature. Range: 30-300°C. The disc thermostat is not adjustable in the field. It is a single-temperature safety device.

**Applications**: Electric iron overtemperature protection, hair dryer cutoff, coffee maker thermostat, electric motor thermal protection, battery pack overtemperature safety. The disc thermostat is the workhorse of appliance safety: cheap, reliable, and fixed in temperature so the end user cannot misadjust it. Every electric kettle, clothes iron, and hair dryer made in the last century contains at least one.

**Strengths**:
- Extremely fast snap transition (milliseconds) eliminates arcing and extends contact life
- Cheap to mass-produce once stamping dies are made
- Factory-sealed housing protects contacts from dust and corrosion
- Fixed trip temperature prevents end-user misadjustment
- No power source required; purely passive operation

**Weaknesses**:
- Not adjustable in the field; trip temperature is fixed at manufacture
- Limited to a single temperature setpoint per disc
- Requires precision stamping dies for consistent disc geometry
- Narrow operating range (30-300°C) determined by bimetallic combination
- Disc-to-disc variation of ±2-3°C even with careful production


## Scaling Notes

Mechanical thermostats scale from individual bench assembly to mass production:

- **Workshop scale** (10-50 units/day): Hand-cut bimetallic strips from purchased stock. Manual stamping of snap discs. Bench calibration with temperature-controlled oil bath. One skilled worker. Adequate for maintenance, replacement, and small-batch equipment production.

- **Factory scale** (500-5,000 units/day): Stamped bimetallic strips and snap discs from continuous strip stock. Automated resistance welding of contacts. Conveyor calibration through temperature-controlled zones. 10-20 workers. This scale supplies an industrial economy's HVAC, appliance, and safety thermostat needs.

- **Mass production** (50,000+ units/day): Fully automated stamping, welding, and calibration lines. Statistical process control on trip temperature (±1°C distribution). Laser trimming of bimetallic strips for precise calibration. This scale supplies global appliance and automotive markets.

## Quality Control

1. **Trip temperature verification**: Calibrate each thermostat in a stirred oil bath or air oven, ramping temperature at 1°C/min through the trip point. Record both make and break temperatures. Tolerance: ±2°C for standard thermostats, ±0.5°C for precision grades.

2. **Contact resistance**: Measure closed-contact resistance with a 4-wire milliohmmeter. Must be below 50 mΩ for silver contacts, below 100 mΩ for tungsten. Higher resistance indicates oxidation or contamination on the contact surfaces.

3. **Cycle life testing**: Cycle the thermostat 10,000 times between 20°C below and 20°C above the trip point. Verify trip temperature has not drifted more than ±2°C from initial calibration. Contact resistance must remain below specification throughout.

4. **Dielectric strength**: Apply 1500 VAC between contacts and housing for 1 minute. No breakdown or leakage above 1 mA. Verifies electrical isolation of the contact mechanism from the mounting structure.

## Variations and Alternatives

| Thermostat Type | Temp Range | Accuracy | Switching Capacity | Best For |
|----------------|-----------|----------|-------------------|----------|
| Single-metal expansion rod | 50-400°C | ±3-5°C | 5-15 A | Furnace safety cutoffs, water heaters |
| Rod-and-tube | -20 to 300°C | ±2-3°C | 10-25 A | Engine cooling, HVAC, refrigeration |
| Bimetallic strip (creep) | -50 to 400°C | ±2-5°C | 5-15 A | Oven control, slow cycling applications |
| Bimetallic snap disc | -20 to 300°C | ±2-4°C | 10-30 A | Appliances, safety cutoffs, fast switching |
| Thermocouple thermostat | -200 to 1300°C | ±1-2°C | External relay | Wide temperature range, precision switching |
| Electronic (thermistor) | -50 to 300°C | ±0.1-0.5°C | External relay | Precision control, narrow deadband |

## See Also

- **[Thermostats Overview](thermostat.md)**: Parent overview of all thermostat types
- **[Electrical Thermostats](thermostat-electrical.md)**: Thermocouple and RTD based
- **[Electronic Thermostats](thermostat-electronic.md)**: Thermistor and IC based
- **[Advanced Thermostats](thermostat-advanced.md)**: SMA, quartz, and IR types

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Single-metal rod thermostat trips at wrong temperature | Set screw shifted or mounting bracket loose | Lock the set screw with its locknut after calibration; verify the mounting bracket is bolted rigidly to a heavy base plate (any frame flexure reads as false temperature change); recalibrate against a reference thermometer |
| Rod-and-tube assembly binds at high temperature | Sliding fit between rod and tube too tight, or differential thermal expansion exceeds clearance | Increase the rod-to-bore clearance to 0.5 mm for applications above 500°C; ensure the rod surface is polished smooth; apply a thin film of graphite or molybdenum disulfide dry lubricant to the rod (oil-based lubricants carbonize at high temperature) |
| Bimetallic strip bends erratically | Strips not fully bonded or thickness non-uniform | Check the rivet or braze bond: any visible gap between strips allows independent movement; re-braze or re-rivet. Verify strip thickness is within ±0.02 mm across the width and length — thickness variation causes uneven bending |
| Bimetallic disc does not snap at rated temperature | Disc geometry wrong (dish depth off by >0.05 mm) or residual stress not relieved | Verify dish depth with a dial indicator. A 0.05 mm error in dish depth shifts the snap temperature by 5-10°C. If the disc was not heat-treated after stamping (350°C for 2 hours), residual stresses cause the trip point to drift during the first few hundred cycles |
| Contact points arc and burn | Snap-action not working — contacts separate slowly instead of snapping | Add a slight overbend (2-3 mm camber over strip length) to create snap-action. Snap-action separates contacts in <1 ms, extinguishing the arc before it damages the contacts. For severely burned contacts, dress with a fine file and re-adjust the gap |
| Calibration drifts after months of cycling | Bimetallic bond fatigue or spring relaxation | Replace the bimetallic strip (brass-steel bonds degrade after ~1 million cycles at high temperature). Check the return spring: springs that have been cycled past their elastic limit will not return the strip fully, changing the trip point |
| Thermostat chatters (rapid cycling) | Deadband too narrow for the application | Widen the deadband by increasing the snap-action camber (bimetallic strip) or increasing the contact gap (rod types). For heating applications, 3-5°C deadband prevents rapid cycling. For safety cutoffs, tight deadband (1-2°C) is acceptable since the device trips infrequently |
| Contacts stick closed (welded) | Inrush current exceeded contact rating | Check that the heater inrush current (typically 5-10× steady-state for resistive heaters) does not exceed the contact rating. Add a pre-charge resistor or use contacts rated for at least 3× the steady-state current. Silver contacts weld less than copper |

## Safety & Hazards

- **Contact arcing fire risk**: Thermostat contacts switching inductive loads or high-current resistive loads can sustain an arc that ignites nearby combustible material. Enclose contact mechanisms in a non-combustible housing (ceramic, steel, or phenolic). Do not use wooden or plastic enclosures for thermostats switching more than 5 A. Keep flammable materials at least 150 mm from open-contact thermostats.
- **Spring energy**: Bimetallic snap-action discs and the return springs in rod-and-tube thermostats store mechanical energy. A disc snapping unexpectedly can eject small components. Wear safety glasses when assembling and adjusting snap-action mechanisms. Point the disc away from your face during calibration.
- **Thermal burns during calibration**: Calibration involves heating the thermostat to its trip temperature, which may exceed 300°C. Use tongs or heat-resistant gloves to handle hot thermostats. Allow adequate cooling time before handling with bare hands. A 300°C metal component causes a deep burn on contact in less than 1 second.
- **Metal fume exposure**: Brazing bimetallic strips (silver solder at 620°C) produces metal oxide fumes. Cadmium-bearing silver solders (still found in older stock) produce cadmium oxide fume, which is extremely toxic. Use cadmium-free silver solder only. Braze under local exhaust ventilation or in a well-ventilated area.
- **Lead exposure**: Some bimetallic strip alloys and solder types contain lead. Handle with gloves. Wash hands before eating. Do not sand or grind lead-containing alloys without respiratory protection (P100 respirator).


---

*Part of [Thermostats & Temperature Control](./thermostat.md) • [Measurement](./index.md) • [All Domains](../../index.md)*
