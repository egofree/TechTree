# Thermostats & Temperature Control Devices

> **Node ID**: measurement.thermostat
> **Domain**: [Measurement](./index.md)
> **Dependencies**: [`metals`](../metals/copper-bronze.md), [`measurement.temperature-pressure`](./temperature-pressure.md)
> **Enables**: [`energy.cooling`](../energy/cooling.md), [`silicon.crystal-growth.cz-pulling`](../silicon/cz-pulling.md)
> **Timeline**: Years 5-60+
> **Outputs**: on_off_control, proportional_control, pid_control, temperature_regulation


Temperature control is what separates haphazard craft from repeatable manufacturing. A kiln that overshoots by 50°C cracks its pottery. A furnace running too cold wastes fuel and produces inconsistent metal. A chemical reactor that drifts 10°C produces different reaction products than intended. And semiconductor manufacturing? Crystal growth furnaces need ±0.5°C stability at 1400°C. Diffusion furnaces demand ±0.1°C. Without thermostats, every thermal process is a gamble controlled by human attention span and guesswork.

A civilization that cannot regulate temperature cannot produce consistent steel, cannot run chemical processes reliably, and certainly cannot grow silicon crystals or fabricate integrated circuits. Thermostats close the feedback loop: sense temperature, compare it to a setpoint, and actuate a heater or cooler to drive the process toward the target. This article covers 22 thermostat types, progressing from the simplest mechanical expansion rod (buildable with basic metalworking) through pneumatic and electronic systems to infrared pyrometer feedback loops suitable for semiconductor furnaces.

Each type builds on the ones before it. The single-metal expansion rod teaches the core principle of thermal expansion. The rod-and-tube adds differential expansion for better sensitivity. The bimetallic strip improves on that with bending action. Mercury and fluid systems add frictionless switching and remote sensing. Electrical types bring precision. Electronic types bring digital control. By the end, you have PID loops holding temperature to hundredths of a degree.

## Tier 1: Pre-Industrial Metalworking

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


## Mercury Tilt Thermostat

**Principle**: A bimetallic coil (or strip) is mechanically linked to a small glass ampoule containing a blob of mercury. As temperature changes, the bimetallic element bends or coils, tilting the ampoule. When tilted past a critical angle, the mercury flows to one end of the ampoule, bridging two platinum wire electrodes sealed through the glass and completing the circuit. When tilted back (temperature returns), the mercury flows away from the electrodes, breaking the circuit. The genius of this design is that mercury switching is essentially frictionless. There is no mechanical contact to wear, oxidize, or stick. The mercury simply sloshes.

**Prerequisites**:
- [Rolling mill](../machine-tools/forming.md) for producing thin metal strips
- Two metals with different expansion coefficients ([brass](../metals/copper-bronze.md) + [steel](../metals/iron-steel.md))
- [Bonding method](../machine-tools/joining.md) for bimetallic strip (riveting, brazing)
- [Spring tempering](../metals/iron-steel.md) capability
- [Glassblowing capability](../glass/glassblowing.md)
- [Mercury](../chemistry/distillation.md) (from cinnabar ore roasting)
- [Platinum wire](../metals/precious-metals.md) (for electrodes)
- [Precision pivot bearings](../machine-tools/bearings-abrasives.md)

**Materials**:
- [Bimetallic strip](../metals/alloys.md) (steel/brass, 0.3 mm thick, 8 mm wide, 150 mm long, coiled into spiral)
- [Glass ampoule: borosilicate glass tube](../glass/advanced.md) (6 mm OD, 4 mm ID, 30-40 mm long), sealed at both ends
- [Mercury](../chemistry/distillation.md): 0.3-0.5 g (a small bead, roughly 3-4 mm diameter)
- [Platinum wire electrodes](../metals/precious-metals.md) (0.3 mm diameter, 15 mm long, two pieces)
- [Pivot bearings](../machine-tools/bearings-abrasives.md): brass bushings or steel pointed screws
- [Mounting base](../metals/iron-steel.md) and calibration dial

**Construction**:

1. **Make the glass ampoule**: From borosilicate glass tubing (6 mm OD, 4 mm ID), cut a 35 mm length. Using a gas-oxygen torch, seal one end closed. Insert two platinum wire electrodes (0.3 mm diameter) through the open end, positioned so their tips are about 2 mm apart at one end of the tube. The platinum wires must be sealed into the glass wall at the closed end. Heat the glass around each wire until it melts and fuses to the platinum, creating a hermetic seal. Test the seal: apply gentle air pressure and check for bubbles under water. Any leak lets air in, oxidizing the mercury and eventually causing the contacts to fail.

2. **Fill with mercury**: Using a clean glass syringe, inject 0.3-0.5 g of mercury into the ampoule. Heat the ampoule gently to 80°C to expand air inside, then seal the open end in the torch flame while the air is expanded. As it cools, the partial vacuum helps keep the mercury at the electrode end during operation.

3. **Form the bimetallic coil**: Clamp one end of the bimetallic strip and wind it into a flat spiral (3-4 turns, about 20 mm outer diameter). The coil unwinds slightly when heated (brass side expands, causing the coil to open). This rotary motion is what tilts the mercury ampoule. A coil produces more angular motion than a straight strip in a compact package.

4. **Link coil to ampoule**: Mount the glass ampoule on a lightweight arm (aluminum or brass, 1 mm thick, 30 mm long) attached to the center of the bimetallic coil. The coil's center rotates as temperature changes, tilting the arm and ampoule. Adjust the arm length and angle so that at the desired setpoint temperature, the mercury just reaches the electrode gap.

5. **Mount on pivot bearings**: Install the assembly on a low-friction pivot (two pointed steel screws in brass bushings, adjusted to minimal play). The entire moving mass (coil + arm + ampoule + mercury) must be balanced on the pivot. Any static imbalance causes gravitational bias that shifts the setpoint depending on mounting orientation.

6. **Add calibration adjustment**: Mount an eccentric cam or threaded adjuster that changes the rest angle of the coil. This is the temperature setpoint dial. Rotating the dial tilts the entire assembly, effectively shifting the temperature at which the mercury reaches the electrodes.

**Calibration**:

1. Mount the thermostat in the intended orientation (usually wall-mounted, vertical). Orientation matters because gravity determines which way the mercury flows.
2. Place in a temperature-controlled environment with a [reference thermometer](./temperature-pressure.md).
3. Set the dial to a mid-range position. Heat slowly until the mercury contacts the electrodes (circuit closes, detected with ohmmeter). Record temperature.
4. Adjust the dial and repeat at 3-5 setpoints across the range (typically 15-30°C for room thermostats).
5. Check hysteresis: the difference between the "heat on" temperature and "heat off" temperature. Mercury tilt thermostats typically have 0.5-1.5°C hysteresis, which is ideal for heating systems (prevents rapid cycling).
6. If hysteresis is excessive (>2°C), check for pivot friction, ampoule contamination, or coil fatigue.

**Expected accuracy**: ±0.5-1°C over -10 to 300°C range (the range is limited by mercury's boiling point at 357°C and freezing point at -38°C). This is remarkably good for a purely mechanical device.

**Applications**: Room heating thermostats (the iconic Honeywell round thermostat, introduced 1953, uses this principle), incubator temperature control, laboratory oven regulation. The mercury tilt thermostat was the gold standard for precision mechanical temperature control for nearly a century. Its main drawbacks are mercury toxicity and sensitivity to mounting orientation.

> **Safety warning**: Mercury is a potent neurotoxin. Vapor pressure at 20°C is 0.0012 mm Hg, enough to exceed safe exposure limits in unventilated spaces after a spill. IDLH concentration: 10 mg/m³. Build and calibrate mercury thermostats under local exhaust ventilation. Clean spills with zinc dust or commercial mercury absorbent. Never vacuum mercury spills (vaporizes and disperses mercury through the exhaust). Store mercury in sealed glass containers under water or mineral oil. Consider alternatives (bimetallic strip, thermocouple) when the slight accuracy advantage of mercury switching is not required.

**Strengths**:
- Frictionless mercury switching eliminates contact wear entirely
- Excellent accuracy (±0.5-1°C) for a purely mechanical device
- Very low hysteresis (0.5-1.5°C) ideal for heating systems
- No electrical power required
- Visual confirmation of switching via mercury position

**Weaknesses**:
- Mercury is a potent neurotoxin; vapor pressure at 20°C exceeds safe limits after a spill
- Sensitive to mounting orientation (gravity-dependent operation)
- Glass ampoule is fragile; breakage releases mercury
- Operating range limited by mercury freezing (-38°C) and boiling (357°C)
- Requires advanced glassblowing to create hermetic platinum-to-glass seals


## Mercury-in-Glass Contact Thermometer

**Principle**: A mercury thermometer with a special capillary tube containing two platinum wire electrodes sealed into the glass at a precise, adjustable position. The mercury column rises with temperature. When it reaches the electrode tips, it bridges the gap between them, completing an electrical circuit. This provides a precise, visual temperature indication combined with electrical switching. The setpoint can be adjusted by moving one electrode (via a threaded magnetic adjuster or a calibrated screw mechanism) up or down the capillary.

**Prerequisites**:
- [Glassblowing](../glass/glassblowing.md) (borosilicate, precision capillary work)
- [Platinum wire](../metals/precious-metals.md)
- [Mercury production and purification](../chemistry/distillation.md)
- [Precision glass working](../glass/advanced.md) (sealing metal wire into glass)

**Materials**:
- [Borosilicate glass capillary tube](../glass/advanced.md) (0.15-0.25 mm bore, 6 mm OD, 300 mm length)
- [Mercury](../chemistry/distillation.md) (2-5 g, distilled)
- [Platinum wire](../metals/precious-metals.md) (0.1-0.2 mm diameter): two pieces, one fixed (sealed into bulb end), one adjustable
- [Brass or stainless steel head fitting](../metals/copper-bronze.md) with threaded adjuster
- [Iron slug](../metals/iron-steel.md) (for magnetic adjustment, if making adjustable type): 1.5 mm diameter, 3 mm long
- [Reference thermometer](./temperature-pressure.md) for calibration

**Construction**:

1. **Prepare the capillary and bulb**: Draw borosilicate glass to produce a capillary tube with 0.2 mm bore and 6 mm OD. Blow a bulb (8 mm diameter) at one end using a gas-oxygen torch. Test bore uniformity by drawing a short mercury thread through and checking it moves freely without sticking. Reject any tube with constrictions. See [Temperature & Pressure](./temperature-pressure.md) for detailed thermometer fabrication.

2. **Seal the fixed electrode**: Insert a platinum wire (0.15 mm diameter, 30 mm long) through the bulb wall before filling. Heat the glass around the wire until it melts and fuses to the platinum. The platinum wire extends into the capillary bore about 5 mm above the bulb. This is the fixed (common) electrode.

3. **Install the adjustable electrode** (fixed-setpoint version): Seal a second platinum wire into the capillary wall at the desired trip temperature height. The gap between the two electrode tips inside the capillary determines the setpoint. Mercury rises, fills the gap, circuit closes. This is the simplest version but not adjustable after sealing.

4. **Install the adjustable electrode** (adjustable version): This uses a thin platinum wire threaded down into the capillary from the top, held by a micrometer screw at the thermometer head. The wire's lower end is the movable setpoint. Turning the screw raises or lowers the wire in the capillary, changing the setpoint temperature. The wire must be thin enough (0.1 mm) to fit in the capillary alongside the mercury column without restricting flow. An iron slug soldered to the top of the platinum wire allows external magnetic adjustment without breaking the seal.

5. **Fill with mercury and seal**: Fill the thermometer with mercury using the vacuum-fill method (see [Temperature & Pressure](./temperature-pressure.md) for detailed procedure). Eliminate all air bubbles. Seal the open end of the capillary with the electrode assembly.

6. **Wire the connections**: Solder insulated copper leads to the external portions of both platinum wires. These connect to the control circuit (typically driving a relay).

**Calibration**:

1. Immerse the bulb in an ice-water bath (0°C). Wait 10 minutes. The mercury meniscus should be well below the adjustable electrode. Record position.
2. Heat slowly in a controlled bath. When the mercury touches the adjustable electrode, the circuit closes (detect with ohmmeter). Record the temperature from a [reference thermometer](./temperature-pressure.md).
3. Adjust the electrode height (via screw or magnetic adjuster) to set the desired trip point.
4. Repeat at 3-5 temperatures to verify linearity. The contact thermometer follows the same thermal expansion physics as a regular mercury thermometer, so if the bore is uniform, the relationship between mercury height and temperature is linear.

**Expected accuracy**: ±0.1-0.5°C over -30 to 300°C. This is one of the most precise mechanical switching thermostats available. The limit is set by the capillary bore uniformity and the ability to position the electrode precisely.

**Applications**: Laboratory temperature regulation, incubator control, precision oven control, chemical process temperature switching. Before electronic thermostats became cheap, the mercury contact thermometer was the standard for laboratory temperature control. Many university labs still use them because of their reliability and visual indication of both temperature and setpoint.

> **Safety warning**: Same mercury hazards as Type 5. Additionally, the thin glass capillary is fragile. Breakage releases mercury and platinum wire. Handle with care and mount in protective housings. The electrical current through the mercury must be limited to a few milliamps (use the contact thermometer to drive a relay, not to switch the heater directly). Excessive current causes heating at the mercury-electrode interface, driving off mercury vapor and degrading the contact.

**Strengths**:
- Outstanding accuracy (±0.1-0.5°C) for a mechanical switching thermostat
- Visual indication of both current temperature and setpoint
- Adjustable setpoint via micrometer screw or magnetic adjuster
- Linear response thanks to mercury thermal expansion
- Laboratory-proven over decades of use

**Weaknesses**:
- Mercury toxicity requires careful handling and spill protocols
- Fragile thin glass capillary; breakage releases mercury and platinum
- Very limited switching current (a few milliamps); must drive a relay, not a heater directly
- Slow response due to thermal mass of mercury column
- Requires precision glassworking skill to fabricate


## Tier 2: Fluid Handling & Sealed Systems

## Liquid Expansion Thermostat (Bulb & Bellows)

**Principle**: A sealed metal bulb connected by a thin capillary tube to a bellows or diaphragm. The bulb is filled with a liquid (oil, alcohol, or glycol mixture) that expands when heated. The expanding liquid pushes through the capillary and pressurizes the bellows, which extends with force proportional to temperature. The bellows motion operates a switch, valve, or lever. The key advantage: the sensing bulb can be placed remotely from the controller, connected only by the capillary tube. This allows temperature sensing inside furnaces, pipes, or tanks while the control mechanism sits safely outside.

**Prerequisites**:
- [Metal tube drawing](../metals/copper-bronze.md) (capillary tube, 1-3 mm OD)
- [Bellows fabrication](../metals/copper-bronze.md) (hydraulic forming or deep drawing)
- [Hermetic sealing](../machine-tools/joining.md) (brazing, welding)
- [Liquid fill material](../chemistry/solvents.md) (silicone oil, mineral oil, or alcohol)

**Materials**:
- [Sensing bulb: copper or stainless steel tube](../metals/copper-bronze.md) (12 mm OD, 1 mm wall, 100-200 mm long), one end capped
- [Capillary tube: copper or stainless steel](../metals/copper-bronze.md) (1.5 mm OD, 0.3 mm ID, 1-5 m length)
- [Bellows: brass or stainless steel](../metals/copper-bronze.md), 20-30 mm diameter, 10-15 mm stroke
- [Fill liquid: silicone oil](../chemistry/solvents.md) (range -50 to 250°C) or [mineral oil](../chemistry/solvents.md) (range -20 to 200°C)
- [Switch mechanism](../electronics/passive-components.md): microswitch or contact assembly
- [Return spring](../metals/iron-steel.md): steel, calibrated force

**Construction**:

1. **Fabricate the bulb**: Cut copper tube to 150 mm length. Braze one end closed with a copper cap. The bulb wall must be thin (1 mm or less) for fast thermal response but strong enough to withstand internal pressure at maximum temperature. Calculate maximum internal pressure: at 200°C, silicone oil expands about 10% from its 20°C volume. If the bulb contains 10 mL of oil and the capillary adds 2 mL volume, the 10% expansion (1.2 mL) must be absorbed by the bellows. The bellows compressibility determines the system pressure.

2. **Prepare the capillary**: Draw or procure 1.5 mm OD copper tube with 0.3 mm ID bore. This is the same tube-drawing technique used for thermometer capillaries. The capillary must be free of constrictions. Test by blowing air through it under water. The long, thin bore prevents convection and minimizes ambient temperature effects on the transmission line. Coil any excess capillary rather than cutting it, since the volume of liquid in the capillary affects calibration.

3. **Make the bellows**: Deep-draw or hydroform a brass bellows (25 mm diameter, 15 mm free length, 8 convolutions). Alternatively, weld individual stamped diaphragms together to form a welded bellows. The bellows must be hermetic. Test by pressurizing to 5 bar under water and checking for bubbles. Any leak means the fill liquid escapes and the thermostat fails.

4. **Connect bulb to capillary to bellows**: Braze the capillary tube to the open end of the sensing bulb. Braze the other end of the capillary to the bellows inlet. All joints must be leak-tight. Use silver solder (flows at 620°C) for copper-to-copper joints.

5. **Fill the system**:
   - Connect a filling funnel to the bellows end (temporarily).
   - Pour silicone oil into the funnel. Allow it to flow through the capillary into the bulb by gravity. Tap the capillary to dislodge air bubbles.
   - Heat the bulb gently (50-60°C) to expand trapped air and drive it out through the funnel.
   - Continue filling until the system is completely liquid-filled with no air pockets. Any trapped air compresses under pressure and makes the response non-linear.
   - Seal the fill port by crimping and brazing while the system is at a known reference temperature (typically 20°C).

6. **Add the switch mechanism**: Mount a microswitch or contact assembly next to the bellows. As the bellows extends with heating, it pushes against the switch actuator. An adjustable stop screw sets the trip point.

**Calibration**:

1. Place the sensing bulb in a temperature bath with a [reference thermometer](./temperature-pressure.md).
2. At the minimum intended temperature, adjust the stop screw so the switch is in the "cold" position (heater on).
3. Heat slowly. Record the temperature at which the bellows trips the switch.
4. Adjust the stop screw to set the desired trip point. Each mm of bellows stroke corresponds to approximately 5-15°C depending on fill liquid and bulb volume.
5. Verify at 3-5 temperatures across the range.

**Expected accuracy**: ±1-3°C over -50 to 400°C range (limited by fill liquid). Response time depends on bulb mass and capillary length: 10-60 seconds typically.

**Applications**: Remote temperature sensing for industrial ovens, hot water tank control, refrigeration systems, HVAC zone control, chemical process temperature regulation. The bulb can be immersed in liquid, bolted to a pipe, or inserted into a furnace while the switch mechanism sits at a safe distance.

**Strengths**:
- Remote sensing: bulb can be placed meters away from the controller
- No electrical power required; purely mechanical operation
- Robust and resistant to vibration and harsh environments
- Wide temperature range depending on fill liquid selection
- Proportional output possible (bellows extension tracks temperature)

**Weaknesses**:
- Slow response time (10-60 seconds) due to thermal mass and capillary flow
- Hermetic seal is critical; any leak causes total failure
- Long capillary runs affected by ambient temperature changes
- Fill liquid limits maximum temperature (silicone oil degrades above 250°C)
- Bulb and capillary volume must be carefully matched to bellows stroke


## Vapor Pressure Thermostat

**Principle**: A sealed bulb is partially filled with a volatile liquid, leaving the rest of the volume filled with its saturated vapor. The vapor pressure above a liquid depends solely on temperature (Clausius-Clapeyron relation), not on the quantity of liquid. As the bulb temperature rises, more liquid evaporates and vapor pressure increases exponentially with temperature. This pressure is transmitted through a capillary to a bellows or bourdon tube, which actuates a switch or valve. The key distinction from the liquid expansion type: vapor pressure systems use the *pressure* of the vapor phase, not the *volume expansion* of the liquid phase.

**Prerequisites**:
- [Metal tube drawing](../metals/copper-bronze.md) (capillary tube, 1-3 mm OD)
- [Bellows fabrication](../metals/copper-bronze.md) (hydraulic forming or deep drawing)
- [Hermetic sealing](../machine-tools/joining.md) (brazing, welding)
- Volatile liquid appropriate to the temperature range (see table below)
- [Vacuum filling equipment](../vacuum/pumps.md) (to control the fill quantity and eliminate air)

**Materials**:
- [Sensing bulb: copper or stainless steel tube](../metals/copper-bronze.md) (12 mm OD, 1 mm wall, 100-200 mm long), one end capped
- [Capillary tube: copper or stainless steel](../metals/copper-bronze.md) (1.5 mm OD, 0.3 mm ID, 1-5 m length)
- [Bellows: brass or stainless steel](../metals/copper-bronze.md), 20-30 mm diameter, 10-15 mm stroke
- Volatile fill liquid (select based on operating range):
  - [Methyl chloride](../chemistry/solvents.md) (-60 to 70°C, refrigeration)
  - [Ethyl chloride](../chemistry/solvents.md) (-20 to 120°C)
  - [Methyl alcohol](../chemistry/solvents.md) (0 to 150°C)
  - [Acetone](../chemistry/solvents.md) (20 to 200°C)
  - [Toluene](../chemistry/solvents.md) (50 to 250°C)

**Construction**:

1. **Fabricate the bulb**: Cut copper tube to 150 mm length. Braze one end closed with a copper cap. The bulb wall must be thin (1 mm or less) for fast thermal response but strong enough to withstand internal pressure at maximum temperature.

2. **Prepare the capillary**: Draw or procure 1.5 mm OD copper tube with 0.3 mm ID bore. The capillary must be free of constrictions. Test by blowing air through it under water. Coil any excess capillary rather than cutting it.

3. **Make the bellows**: Deep-draw or hydroform a brass bellows (25 mm diameter, 15 mm free length, 8 convolutions). Alternatively, weld individual stamped diaphragms together. Test by pressurizing to 5 bar under water and checking for bubbles.

4. **Connect bulb to capillary to bellows**: Braze the capillary tube to the open end of the sensing bulb. Braze the other end of the capillary to the bellows inlet. All joints must be leak-tight. Use silver solder for copper-to-copper joints.
3. **Evacuate and seal**: Before sealing, evacuate the system to remove air. Air in the system adds a partial pressure that is independent of temperature, adding a constant offset that reduces the dynamic range of the pressure signal. Connect a vacuum pump to the fill port, evacuate to below 1 mbar, then seal by crimping and brazing.

4. **Add the actuator mechanism**: The bellows or bourdon tube moves proportionally to vapor pressure. Since vapor pressure is an exponential function of temperature, the actuator motion is non-linear with respect to temperature. This means the calibration scale is compressed at the low end and expanded at the high end. Account for this in the linkage design or calibration marks.

**Calibration**:

1. Place the bulb in a temperature bath with a [reference thermometer](./temperature-pressure.md). Record the actuator position (bellows extension or bourdon tube tip travel) at 5-6 temperatures across the range.
2. Plot a calibration curve. The curve should follow the Clausius-Clapeyron relationship: ln(P) = A - B/T, where T is absolute temperature.
3. Adjust the switch trip point by moving the switch position relative to the bellows.
4. Verify that the system contains both liquid and vapor at the extreme temperatures of the intended range. If the bulb is entirely liquid-filled at the low end (no vapor space), the pressure response changes character and calibration is invalid.

**Expected accuracy**: ±1-2°C over -50 to 300°C range. The exponential pressure-temperature relationship actually helps with sensitivity at the upper end of the range.

**Applications**: Refrigeration thermostatic expansion valves (TXVs), automotive air conditioning, hot water temperature control. The vapor pressure principle is the basis of most refrigeration expansion valves: the sensing bulb is strapped to the evaporator outlet, and the vapor pressure in the bulb modulates the refrigerant flow through the valve. This is a self-contained proportional controller with no electrical power required.

**Strengths**:
- Self-contained proportional controller with no electrical power needed
- Exponential pressure response provides high sensitivity at upper end of range
- Wide temperature range available by selecting different volatile liquids
- Remote sensing capability via capillary tube
- Well-proven in refrigeration applications worldwide

**Weaknesses**:
- Non-linear response (exponential) complicates calibration and setpoint adjustment
- Fill quantity must be carefully controlled; too much or too little ruins operation
- Requires vacuum pump for proper evacuation during filling
- Each volatile liquid covers a limited range; switching ranges means rebuilding
- Hermetic seal failure causes total loss of function


## Gas Expansion Thermostat

**Principle**: A sealed bulb filled with an inert gas (nitrogen or helium) connected by capillary to a pressure-sensing element (bellows or bourdon tube). Unlike liquid or vapor systems, the gas follows the ideal gas law: P × V = n × R × T. Since the volume is fixed (sealed system), pressure is directly proportional to absolute temperature (Gay-Lussac's Law: P/T = constant). This gives a perfectly linear pressure-temperature relationship, unlike the exponential behavior of vapor pressure systems. The gas expansion thermostat has the widest useful range of any sealed-system type.

**Prerequisites**:
- [Metal tube drawing](../metals/copper-bronze.md) (capillary tube, 1-3 mm OD)
- [Bellows fabrication](../metals/copper-bronze.md) (hydraulic forming or deep drawing)
- [Hermetic sealing](../machine-tools/joining.md) (brazing, welding)
- [Inert gas supply](../chemistry/air-separation.md) (nitrogen cylinder or generated by air liquefaction/fractionation)
- [Vacuum pump](../vacuum/pumps.md) for filling

**Materials**:
- [Sensing bulb: stainless steel tube](../metals/iron-steel.md) (12 mm OD, 1 mm wall, 150 mm long) -- stainless preferred over copper for high-temperature strength
- [Capillary tube: stainless steel](../metals/iron-steel.md) (1.5 mm OD, 0.3 mm ID, up to 10 m length)
- [Bellows: stainless steel](../metals/iron-steel.md) (25 mm diameter, 15 mm stroke)
- [Fill gas: dry nitrogen](../chemistry/air-separation.md) (inert, non-condensing over the entire range)
- [Pressure gauge](./temperature-pressure.md) or switch mechanism

**Construction**:

1. **Assemble the bulb-capillary-bellows system**: Cut stainless steel tube to 150 mm length. Braze one end closed with a cap. Draw or procure stainless steel capillary tube. Deep-draw or hydroform a stainless steel bellows. Braze or TIG weld all joints. Use stainless steel throughout for high-temperature capability. All joints brazed with silver solder (copper-to-stainless) or TIG welded (stainless-to-stainless).

2. **Evacuate**: Connect a vacuum pump to the fill port. Evacuate the entire system (bulb, capillary, bellows) to below 0.1 mbar. Hold vacuum for 10 minutes to allow outgassing of internal surfaces. Any residual gas (air, water vapor) adds to the nitrogen pressure and causes zero-point error.

3. **Fill with nitrogen**: With the bulb at a known reference temperature (20°C), admit dry nitrogen to a fill pressure of 5-10 bar (gauge). The fill pressure determines the sensitivity: higher fill pressure means more pressure change per degree, but also requires a stiffer bellows.

4. **Seal the fill port**: Crimp and braze the fill port closed while the system is at the reference temperature and fill pressure. The sealed system now has a fixed mass of gas. Pressure at any temperature can be calculated: P = P_fill × (T / T_fill), where temperatures are in Kelvin. At 20°C (293 K) fill pressure of 10 bar, the pressure at 500°C (773 K) would be 10 × (773/293) = 26.4 bar. Design the bellows and housing to withstand the maximum pressure.

5. **Add the switch mechanism**: Mount a [microswitch](../electronics/passive-components.md) or contact assembly next to the bellows. As the bellows extends with heating, it pushes against the switch actuator. An adjustable stop screw sets the trip point. The linear pressure-temperature relationship makes calibration straightforward.

**Calibration**:

1. Place the bulb in a temperature bath with a [reference thermometer](./temperature-pressure.md). Measure the bellows extension at 5-6 temperatures.
2. Verify linearity: plot extension vs. temperature. The plot should be a straight line. Any curvature indicates a leak (gas escaping) or a non-ideal gas effect (negligible for nitrogen below 200 bar).
3. Set the switch trip point by adjusting the stop screw.

**Expected accuracy**: ±0.5-1°C over -200 to 800°C range. This is the widest range of any sealed-system thermostat. The low end is limited by the gas condensing (nitrogen liquefies at -196°C at 1 atm, so the bulb must be filled to a pressure that prevents condensation at the lowest operating temperature).

**Applications**: Industrial furnace temperature control, cryogenic temperature regulation, high-temperature process control where thermocouples are not yet available or where a self-contained mechanical system is preferred. Gas expansion systems are used in industrial thermostats for gas-fired furnaces and ovens.

**Strengths**:
- Widest useful range of any sealed-system thermostat (-200 to 800°C)
- Perfectly linear pressure-temperature relationship simplifies calibration
- No condensation or phase-change complications within the operating range
- No electrical power required; purely mechanical operation
- Remote sensing via capillary tube

**Weaknesses**:
- Requires high-pressure fill (5-10 bar), demanding stronger construction
- Lower sensitivity than vapor pressure systems at moderate temperatures
- Any gas leak causes complete calibration failure
- Bulb and capillary must withstand maximum pressure at highest temperature
- Ambient temperature changes along the capillary affect the reading


## Wax Pellet Thermostat (Wax Actuator)

**Principle**: A metal cylinder (pellet) contains a specially formulated wax that melts and expands dramatically (10-15% by volume) at a precise temperature. The expanding wax pushes a piston outward against a return spring. The piston stroke is proportional to temperature in the melting range. Unlike bimetallic or gas systems, the wax actuator produces large forces (50-200 N) in a compact package, making it ideal for operating valves directly without amplification.

**Prerequisites**:
- [Wax production](../chemistry/petroleum-alternatives.md) (beeswax from apiculture, or petroleum-derived microcrystalline wax from oil refining)
- [Precision cylinder boring and piston machining](../machine-tools/machining.md)
- [Rubber boot seal fabrication](../polymers/rubber.md)
- Spring tempering

**Materials**:
- [Wax pellet housing: brass cup](../metals/copper-bronze.md) (20 mm diameter, 25 mm deep, 1 mm wall)
- [Piston: brass rod](../metals/copper-bronze.md) (8 mm diameter, 20 mm long, lapped to sliding fit in housing)
- [Wax](../chemistry/petroleum-alternatives.md): microcrystalline petroleum wax or beeswax blend, selected for melting range
- [Rubber boot](../polymers/rubber.md): nitrile rubber or natural rubber, 0.5 mm thick, shaped like an accordion fold
- [Return spring](../metals/iron-steel.md): steel, 30-80 N at full compression, 15-20 mm free length
- [Copper guide ring](../metals/copper-bronze.md) (to prevent wax extrusion past piston)

**Construction**:

1. **Select or blend the wax**: The wax melting range determines the actuator temperature. Common formulations:
   - Beeswax: melts 62-65°C (too variable for precision use without blending)
   - Microcrystalline petroleum waxes: available in melting points from 60°C to 95°C in 5°C increments
   - Custom blends: mix waxes of different melting points to tune the transition temperature. The wax must have a sharp melting transition (narrow melting range, ideally 2-3°C) for precise actuation.
   Test the wax by placing a sample in a temperature bath with a thermometer and noting the melting range. A wax that melts over a 15°C range will produce a sluggish, imprecise actuator.

2. **Machine the housing**: Bore the brass cup to 18.0 mm ID, polished to a smooth finish. The bore must be uniform within 0.02 mm along its entire length. Any taper causes the piston to bind. Cut a step at the open end to seat the rubber boot.

3. **Machine the piston**: Turn the brass piston to 17.95 mm diameter (0.05 mm clearance in the 18.0 mm bore). The piston must slide freely without sticking, but the clearance must be small enough that the copper guide ring prevents wax from extruding past. Polish the piston surface. Cut a groove near the piston head for the copper guide ring (0.3 mm thick wire, compressed into the groove).

4. **Fill with wax**: Melt the wax to 10-15°C above its melting point. Pour into the housing, filling to about 85% of the bore volume. The air gap at the top allows for initial expansion without preloading the piston. The wax shrinks slightly as it solidifies, which is normal.

5. **Assemble**: Insert the piston into the bore. Install the rubber boot over the open end of the housing, sealed to the housing rim and the piston stem. The boot prevents water, oil, or debris from entering the mechanism. It also accommodates the piston stroke without breaking the seal.

6. **Add the return spring**: Place the spring around the piston stem, between the housing flange and the piston head. The spring pushes the piston back into the housing as the wax cools and contracts.

**Calibration**:

1. Mount the wax actuator in a fixture that measures piston stroke (dial indicator or ruler) while the housing is immersed in a temperature bath with a [reference thermometer](./temperature-pressure.md).
2. Heat slowly (0.5°C/minute) through the wax melting range. Record piston stroke vs. temperature.
3. The stroke-temperature curve shows three regions: solid wax (minimal expansion below melting point), melting range (rapid expansion as wax transitions), and liquid wax (moderate thermal expansion above melting point). The useful operating range is the melting region.
4. Total stroke is typically 8-12 mm for a 25 mm deep pellet. The onset temperature and stroke curve depend on the wax formulation.
5. If the onset temperature is wrong, change the wax blend. If the stroke is insufficient, increase the pellet volume or select a wax with greater volumetric expansion.

**Expected accuracy**: ±2-3°C over 30-95°C range (narrow range, limited by wax chemistry). The wax pellet is not a precision thermostat but produces large actuation forces in a simple, reliable package.

**Applications**: Automotive engine cooling thermostats (the most common application: opens coolant flow to radiator at 82-92°C), thermostatic mixing valves, shower temperature control, greenhouse vent actuators. Nearly every internal combustion engine on Earth uses a wax pellet thermostat. It is cheap, reliable, self-contained, and produces enough force to operate a valve directly against water pressure.

**Strengths**:
- Large actuation force (50-200 N) in a very compact package
- Direct valve operation without linkages or amplification
- Self-contained and requires no external power
- Extremely reliable; millions in daily use in automotive engines
- Simple construction from readily available materials

**Weaknesses**:
- Very narrow operating range (30-95°C) limited by wax chemistry
- Slow response due to thermal mass of wax and housing
- Not adjustable after filling; setpoint fixed by wax blend
- Wax degrades and changes properties after many thousands of thermal cycles
- Hysteresis between melting and solidification temperatures


## Thermostatic Radiator Valve (TRV)

**Principle**: A self-contained proportional valve that combines a temperature sensor (wax pellet or liquid-filled bulb) with a valve body in a single unit. The sensor directly operates the valve stem: as room temperature rises above the setpoint, the expanding wax or liquid pushes the valve stem toward the closed position, reducing hot water flow through the radiator. As the room cools, the sensor contracts and a return spring opens the valve. The TRV provides continuous proportional control (not just on/off) without any external power source.

**Prerequisites**:
- [Wax production](../chemistry/petroleum-alternatives.md) for wax pellet sensor, or [liquid fill material](../chemistry/solvents.md) for bulb sensor
- [Precision cylinder boring and piston machining](../machine-tools/machining.md)
- [Rubber boot seal fabrication](../polymers/rubber.md)
- [Spring tempering](../metals/iron-steel.md)
- [Metal tube drawing](../metals/copper-bronze.md) (if using liquid bulb sensor)
- [Bellows fabrication](../metals/copper-bronze.md) (if using liquid bulb sensor)
- [Hermetic sealing](../machine-tools/joining.md) (brazing, welding)
- [Valve body machining](../machine-tools/machining.md) (brass valve body, precision bore)
- [Spring selection and calibration](../metals/iron-steel.md)

**Materials**:
- [Valve body: hot-pressed brass forging](../metals/copper-bronze.md), 15 mm (1/2") or 22 mm (3/4") BSP threads
- [Valve stem: brass](../metals/copper-bronze.md) (6 mm diameter, 30 mm long)
- [Valve seat: brass or stainless steel](../metals/copper-bronze.md), lapped to seal against valve disc
- [Valve disc](../polymers/rubber.md): nitrile rubber or [PTFE](../polymers/thermoplastics.md) (compressed against seat)
- [Sensor housing: brass](../metals/copper-bronze.md) (miniature wax pellet or liquid-filled bulb, 15 mm diameter)
- [Return spring](../metals/iron-steel.md): steel, calibrated force
- [Setpoint dial](../polymers/thermoplastics.md): plastic or brass knob with temperature markings

**Construction**:

1. **Machine the valve body**: Start with a brass forging (valve body blank). Drill and tap the inlet and outlet ports (15 mm BSP). Bore the valve chamber (12 mm diameter, 20 mm deep) to receive the valve stem and disc. Machine the valve seat at the bottom of the chamber: a narrow annular ridge (1 mm wide) that the valve disc presses against to shut off flow. The seat must be flat and smooth; any imperfection causes leakage when "closed."

2. **Make the valve stem and disc**: Turn the brass valve stem to 5.95 mm diameter (sliding fit in the 6.0 mm bore). Press a PTFE disc (8 mm diameter, 2 mm thick) onto the end of the stem. The PTFE disc provides a compliant seal against the brass valve seat. PTFE deforms slightly under pressure to fill minor seat imperfections, unlike a metal-to-metal seal that requires lapped surfaces.

3. **Build the sensor**: Construct a miniature wax pellet actuator (10 mm diameter, 20 mm long): select [wax](../chemistry/petroleum-alternatives.md) for the room-temperature range (15-25°C), bore a [brass housing](../metals/copper-bronze.md), machine a [brass piston](../metals/copper-bronze.md), fill with wax, and seal with a [rubber boot](../polymers/rubber.md). Alternatively, use a small liquid-filled bulb with [alcohol](../chemistry/solvents.md) or [butane](../chemistry/petroleum-alternatives.md) as the fill fluid, connected to a miniature bellows that pushes the valve stem.

4. **Connect sensor to valve stem**: Mount the sensor housing directly above the valve body, with the sensor piston pushing down on the valve stem. As the wax expands, it pushes the valve stem downward, closing the valve against the seat. The return spring pushes the valve stem upward (opening the valve) when the wax contracts.

5. **Add the setpoint adjustment**: Mount a threaded ring between the sensor housing and the valve body. Turning the ring compresses or extends the spring preload, effectively shifting the temperature at which the valve starts to close. Mark the ring with temperature indications (typically *, 1, 2, 3, 4, 5 corresponding to approximately 5-28°C).

6. **Seal and assemble**: Install O-ring seals around the valve stem to prevent water leakage. Assemble the sensor, spring, valve stem, and body. Test for water leaks at 2 bar pressure with the valve in both open and closed positions.

**Calibration**:

1. Mount the TRV in a test rig with controlled-temperature air flowing over the sensor head. Measure hot water flow rate through the valve at various air temperatures.
2. With the setpoint at position "3" (typically ~20°C), the valve should be fully open at 16°C, beginning to close at 18°C, and fully closed at 22-23°C. This 4-5°C proportional band prevents rapid cycling while maintaining reasonable temperature control.
3. Check all setpoint positions. Adjust the spring preload or wax quantity if any position is out of range.

**Expected accuracy**: ±1-2°C over 5-30°C range. The proportional action means the radiator output varies smoothly rather than cycling on/off, which provides more stable room temperature.

**Applications**: Radiator temperature control in central heating systems, zone control for hydronic heating, industrial process temperature regulation with hot water. The TRV is the most common self-contained proportional temperature controller in existence.

**Strengths**:
- Proportional control without any external power source
- Self-contained installation; fits on a standard radiator valve body
- Easy zone-by-zone control in multi-room buildings
- Reliable and maintenance-free for years
- User-adjustable setpoint via dial

**Weaknesses**:
- Limited to room-temperature range (5-30°C)
- Slow response due to wax or liquid thermal mass
- Requires a hydronic (hot water) heating system to function
- Wax or liquid sensor drifts slightly over years of operation
- No remote control capability; setpoint adjusted only at the valve


## Pneumatic Thermostat

**Principle**: A temperature-sensitive element (bimetallic strip, liquid-filled bulb, or gas-filled bulb) modulates the clearance in a nozzle-flapper assembly. Compressed air (typically 3-15 psi / 0.2-1.0 bar) is supplied to the nozzle. The flapper (a thin metal plate) is positioned by the temperature sensor. As temperature rises, the sensor moves the flapper closer to the nozzle, restricting airflow and building up back-pressure in the signal line. This variable air pressure (3 psi = full cooling, 15 psi = full heating, or vice versa) drives pneumatic actuators on valves, dampers, and other equipment. The pneumatic thermostat provides continuous proportional control with no electrical power.

**Prerequisites**:
- [Compressed air supply](../energy/storage.md) (clean, dry, regulated to 18-20 psi supply)
- [Precision nozzle](../machine-tools/machining.md) (0.5-1.0 mm orifice)
- [Relay valve](../metals/copper-bronze.md) (amplifier: boosts the weak nozzle back-pressure signal to actuator-driving pressure)
- [Pneumatic actuators](../energy/storage.md) (diaphragm or piston type) on controlled equipment
- [Temperature sensor](#3-bimetallic-strip-thermostat) (bimetallic strip, or [liquid/gas bulb](#7-liquid-expansion-thermostat-bulb--bellows))

**Materials**:
- [Nozzle: brass or stainless steel](../metals/copper-bronze.md), 0.8 mm orifice
- [Flapper: phosphor bronze strip](../metals/copper-bronze.md) (0.1 mm thick, 8 mm wide, 30 mm long)
- [Bimetallic strip](../metals/alloys.md) (steel/brass, 0.3 mm thick, 8 mm wide, 60 mm long, connected to flapper)
- [Restrictor orifice](../metals/copper-bronze.md): brass plug with 0.15 mm drilled hole (in the supply line)
- [Relay valve](../metals/copper-bronze.md): brass body with diaphragm and spool valve
- [Air supply tubing](../metals/copper-bronze.md): copper or polyethylene, 6 mm OD
- [Mounting base](../metals/iron-steel.md) with air connections

**Construction**:

1. **Build the nozzle-flapper assembly**: Press a brass nozzle (0.8 mm orifice, 5 mm long) into the thermostat base. The nozzle faces upward. Mount the flapper (phosphor bronze strip, 0.1 mm thick) on a pivot directly above the nozzle, with its free end positioned by the bimetallic strip. The clearance between flapper and nozzle tip is critical: at the setpoint temperature, the gap should be about 0.1-0.2 mm. This gap determines the nozzle back-pressure.

2. **Understand the nozzle-flapper gain**: With the restrictor orifice (0.15 mm) in the supply line, the nozzle-flapper acts as a pressure divider. When the flapper is far from the nozzle, air escapes freely and back-pressure is low (near 0 psi). When the flapper nearly blocks the nozzle, back-pressure rises to nearly supply pressure. The transition from low to high pressure occurs over a very small range of flapper motion (0.01-0.05 mm), giving extremely high gain (pressure change per unit of flapper motion).

3. **Add the relay amplifier**: The nozzle back-pressure alone cannot drive large pneumatic actuators (it can only move a small volume of air through the restrictor). A relay valve amplifies the signal: nozzle back-pressure acts on a small diaphragm, which moves a spool valve that directly connects the supply to the output line. The relay provides both pressure amplification and flow amplification. Construct the relay from a brass body (30 mm diameter) with a rubber diaphragm (20 mm diameter, 0.5 mm thick) and a brass spool valve.

4. **Connect the temperature sensor**: Link the bimetallic strip to the flapper. As temperature rises, the bimetallic strip bends, pushing the flapper closer to (or farther from) the nozzle, depending on the desired action (direct or reverse acting). The linkage converts the small bending motion of the bimetallic strip into the tiny flapper motion needed to span the 3-15 psi output range.

5. **Add the setpoint adjustment**: Install an adjustable spring that biases the flapper position. Turning a knob or set screw compresses or extends the spring, shifting the temperature at which the output pressure is at mid-range (9 psi). This is the setpoint.

6. **Connect air supply and output**: Connect the compressed air supply (18-20 psi) to the restrictor inlet. Connect the nozzle back-pressure chamber to the relay diaphragm. Connect the relay output to the pneumatic actuator on the controlled equipment (valve or damper). Run copper or polyethylene tubing (6 mm OD) for all connections.

**Calibration**:

1. Supply clean, dry air at 18 psi to the thermostat. Measure output pressure with a [precision pressure gauge](./temperature-pressure.md) (0-20 psi, 0.1 psi resolution).
2. Place the thermostat in a temperature-controlled environment. At the setpoint temperature, the output should be 9 psi (mid-range).
3. Below setpoint, output should increase toward 15 psi (calling for heating). Above setpoint, output should decrease toward 3 psi (satisfied).
4. Adjust the proportional band: the temperature range over which the output spans 3-15 psi. Typical setting: 2-5°C proportional band. Narrower band = tighter control but risk of instability (hunting). Wider band = more stable but less precise. Adjust by changing the mechanical advantage between the sensor and flapper.
5. Verify that the output changes smoothly and linearly with temperature across the proportional band. Step changes or dead zones indicate linkage problems or nozzle contamination.

**Expected accuracy**: ±0.5-1°C over 10-35°C range with properly tuned system. The pneumatic thermostat can achieve proportional control accuracy comparable to electronic thermostats, using only compressed air.

**Applications**: Commercial building HVAC systems (the dominant technology for large-building temperature control from the 1920s through the 1980s, and still common), industrial process control, cleanroom temperature regulation. Pneumatic control systems were the standard for building automation before cheap electronics. They have a major advantage in hazardous environments: no electrical sparks.

**Strengths**:
- Proportional control with no electrical power; inherently safe in explosive atmospheres
- Multiplexable: one compressed air supply drives many thermostats and actuators
- Proven technology; decades of reliable service in large commercial buildings
- Tunable proportional band allows balancing precision and stability
- No electromagnetic interference concerns

**Weaknesses**:
- Requires a continuous supply of clean, dry compressed air
- Air leaks in tubing cause gradual failure and waste energy
- Needs regular maintenance (filter changes, leak detection)
- Complex calibration requiring pressure gauges and temperature baths
- Limited to environments where compressed air infrastructure exists


## Tier 3: Basic Electrical/Electronic Infrastructure

## Thermocouple-Based Thermostat

**Principle**: Two dissimilar metals joined at a measurement junction generate a small voltage (Seebeck effect) proportional to the temperature difference between the measurement (hot) junction and the reference (cold) junction. This voltage, typically in the millivolt range, drives a galvanometer relay or electronic comparator. When the voltage exceeds the setpoint threshold (corresponding to the target temperature), the relay trips, shutting off the heater. The thermocouple is self-generating: it needs no external power to produce its temperature signal. This makes it the simplest possible high-temperature thermostat.

**Prerequisites**:
- [Thermocouple wire](./temperature-pressure.md) (chromel, alumel, or other dissimilar metal pairs)
- [Millivoltmeter or galvanometer relay](./electrical-instruments.md), or [electronic comparator circuit](../electronics/semiconductor-devices.md)
- [Relay](../electronics/passive-components.md) for switching the heater (if not using a galvanometer relay directly)
- [Cold-junction temperature measurement](./temperature-pressure.md) (for compensation)

**Materials**:
- [Thermocouple wire](./temperature-pressure.md) (Type K: chromel + alumel, 0.5-1.0 mm diameter, 1-3 m length, depending on application)
- [Thermocouple plug/jack](../metals/alloys.md) (compatible alloy terminals, to avoid introducing third-metal errors)
- [Galvanometer relay](./electrical-instruments.md) (moving-coil meter with contacts) or [electronic comparator](../electronics/semiconductor-devices.md) (op-amp + reference voltage + relay driver)
- [Relay](../electronics/passive-components.md): mechanical (10-20 A contacts) or [solid-state relay](../electronics/power-electronics.md) (SSR, 20-40 A)
- [Reference temperature sensor](./temperature-pressure.md) (thermistor or RTD at the cold junction) if using electronic compensation
- [Ice bath](../water/procurement.md) or isothermal block for cold junction (if using manual compensation)

**Construction**:

1. **Make the thermocouple junction**: Strip 10 mm of insulation from both thermocouple wires. Twist the bare ends together tightly (6-8 turns). Weld the junction using a capacitance-discharge welder (preferred for consistent junctions) or gas torch with borax flux. The junction must be a clean weld, not just a twist. A twisted junction adds contact resistance that drifts with corrosion and mechanical vibration. Test: the resistance of the junction should be within 10% of the calculated resistance of the wire lengths.

2. **Insulate the wires**: Slide ceramic insulator beads (2 mm bore, 4 mm long) over each wire from the junction to the terminals. Alternatively, use mineral-insulated (MgO) sheathed thermocouple cable for harsh environments. The two wires must not short together anywhere except at the measurement junction.

3. **Connect to the measuring circuit**:
   - **Galvanometer relay method** (simplest, no electronics): Connect the thermocouple wires directly to a galvanometer relay. This is a sensitive moving-coil meter (like a millivoltmeter) with adjustable contact points. The meter needle deflects proportionally to the thermocouple voltage. When the needle reaches the setpoint contact, the circuit closes, driving a power relay. Cold junction compensation is done mechanically: a bimetallic strip on the galvanometer coil shifts the zero point to compensate for ambient temperature changes.
   - **Electronic comparator method** (more precise): Connect the thermocouple to an instrumentation amplifier (gain 100-1000×). The amplified voltage is compared to a reference voltage (set by a potentiometer, the setpoint dial) using a comparator IC (LM311 or similar). When the thermocouple voltage exceeds the setpoint, the comparator output drives a relay or SSR. Cold junction compensation is done electronically: a thermistor or RTD at the terminal block measures the local temperature, and a compensation circuit adds or subtracts the appropriate offset voltage.

4. **Set up cold junction compensation**: The thermocouple voltage represents the *difference* between the hot junction and the cold junction (terminal block) temperatures. To measure absolute temperature, you must know the cold junction temperature. Three methods:
   - **Ice bath** (most accurate): immerse the terminal block in an ice-water slurry (0°C). The thermocouple voltage now reads directly in °C (0°C reference). Not practical for permanent installations but used for calibration.
   - **Electronic compensation**: measure the terminal block temperature with a thermistor or RTD and add the corresponding compensation voltage. This is standard in all commercial thermocouple instruments.
   - **Isothermal block**: mount the terminal block on a large aluminum block with slow thermal response. The block temperature is measured once and assumed constant during short measurements.

5. **Wire the output**: Connect the relay output to the heater circuit. For simple on/off control, wire the relay contacts in series with the heater power. For a basic proportional control, use a time-proportioning relay (cycling the heater on and off with variable duty cycle).

**Calibration**:

1. Calibrate the thermocouple at two reference points: ice-water (0°C) and boiling water (100°C at 1 atm). Record the output voltage at each point. For Type K, the expected values are 0.000 mV at 0°C and 4.096 mV at 100°C (with cold junction at 0°C).
2. Check linearity at intermediate points. Type K is not perfectly linear (sensitivity varies from ~39 μV/°C at 0°C to ~42 μV/°C at 1000°C), but it is close enough for ±2-3°C accuracy using linear interpolation.
3. Verify cold junction compensation: with the thermocouple at a known temperature (e.g., immersed in boiling water at 100°C), check that the instrument reads correctly with the terminal block at room temperature (typically 20-25°C). If the reading is off by about the room temperature value, the cold junction compensation is not working.
4. For the galvanometer relay, adjust the contact position to set the trip point. For the electronic comparator, adjust the reference potentiometer.

**Expected accuracy**: ±1-5°C over -200 to 1800°C (depending on thermocouple type and calibration effort). Self-generating, no power required for the sensor itself. Type K covers -200 to 1260°C. Type S covers 0 to 1600°C with lower sensitivity but better stability.

**Applications**: Furnace temperature control, kiln firing, gas appliance safety (thermocouple holds gas valve open while pilot flame heats the junction), automotive exhaust gas temperature, any application requiring high-temperature sensing with minimal infrastructure. The thermocouple thermostat is the workhorse of industrial temperature control. If you can make two different metal wires and weld their ends together, you can regulate furnace temperature.

**Strengths**:
- Self-generating sensor; no power needed at the measurement point
- Widest temperature range of any contact sensor (-200 to 1800°C depending on type)
- Extremely simple to construct: two wires welded together
- Rugged and resistant to vibration, shock, and high temperature
- Fast response, especially with bare or grounded junctions

**Weaknesses**:
- Very low output signal (millivolts) susceptible to electrical noise
- Cold junction compensation required for accurate readings
- Non-linear voltage-temperature relationship varies by thermocouple type
- Calibration drift of 1-5°C per 1000 hours at high temperature
- Lower accuracy than RTDs or thermistors without careful calibration


## Resistance Thermometer (RTD) Thermostat

**Principle**: A fine platinum wire (or thin-film platinum element) increases in electrical resistance predictably with temperature. The Pt100 standard specifies 100.0 Ω at 0°C with a temperature coefficient of +0.385 Ω/°C. At 100°C, the resistance is 138.5 Ω. The resistance is measured using a Wheatstone bridge circuit: three fixed resistors and the RTD form the bridge, and a galvanometer or amplifier detects the imbalance voltage when the RTD resistance deviates from the setpoint value. The bridge output drives a relay or control circuit.

**Prerequisites**:
- [Fine wire drawing capability](../metals/precious-metals.md) (platinum wire, 0.025-0.05 mm diameter) or thin-film deposition
- [Wheatstone bridge circuit construction](../electronics/passive-components.md) (precision resistors, galvanometer or amplifier)
- [Platinum sourcing](../metals/precious-metals.md) (rare but needed for accuracy and stability)
- [Four-wire measurement technique](../electronics/passive-components.md) for lead resistance elimination

**Materials**:
- [Platinum wire](../metals/precious-metals.md) (0.05 mm diameter, 2 m length) or commercial Pt100 element
- [Manganin wire](../metals/alloys.md) (for precision bridge resistors): 0.1 mm diameter, low temperature coefficient (~20 ppm/°C)
- Wheatstone bridge: two fixed arms (100.0 Ω each, ±0.01%), one variable arm (decade resistance box or potentiometer for setpoint), and the RTD
- [Galvanometer or zero-center millivoltmeter](./electrical-instruments.md) (±50 mV range)
- [Relay driver circuit](../electronics/power-electronics.md): amplifier + relay or [SSR](../electronics/power-electronics.md)
- [Ceramic bobbin for winding RTD element](../ceramics/electronic-ceramics.md) (alumina, 5 mm diameter, 30 mm long)

**Construction**:

1. **Wind the RTD element** (if not using a commercial element): Wind platinum wire (0.05 mm diameter) in a bifilar pattern (folded back on itself to cancel inductance) onto the ceramic bobbin. The bifilar winding is essential for AC bridge measurements. Calculate the wire length needed: Pt100 at 0°C requires resistance of exactly 100.0 Ω. Platinum wire at 0.05 mm diameter has resistance of approximately 3.8 Ω/m, so you need about 26 m of wire. Wind this onto the bobbin, taking care not to kink or stretch the wire (platinum work-hardens and its resistance changes with strain). The wire must be wound loosely enough that it can expand and contract freely with temperature, without binding on the bobbin.

2. **Trim to exact value**: Measure the resistance at 0°C (ice bath). Carefully unwind wire until the resistance is exactly 100.0 Ω. This is fussy work with 0.05 mm wire. Each cm of wire removed changes the resistance by about 0.04 Ω (0.1°C). Patience pays off.

3. **Seal the element**: Coat the wound bobbin with a thin layer of alumina cement or enclose it in a stainless steel sheath (6 mm OD, 50-100 mm long) packed with alumina powder for thermal contact and electrical insulation. The sheath protects the delicate platinum wire from mechanical damage and contamination.

4. **Build the Wheatstone bridge**: Construct three bridge arms using manganin wire resistors. Manganin (84% Cu, 12% Mn, 4% Ni) has a near-zero temperature coefficient, so the bridge resistors do not drift with ambient temperature changes. Wind the resistors bifilar on ceramic bobbins. Two arms should be exactly 100.0 Ω. The third arm is the setpoint: a decade resistance box or a calibrated potentiometer that allows the operator to dial in the desired resistance (and thus the desired temperature).

5. **Wire the bridge**: Connect the RTD to the bridge using a four-wire (Kelvin) connection. In a four-wire setup, two wires carry the excitation current and two wires sense the voltage across the RTD. This eliminates the resistance of the lead wires from the measurement. With 3 m of copper lead wire (0.5 mm diameter), the lead resistance is about 0.6 Ω, which would cause a 1.5°C error in a two-wire measurement. Four-wire eliminates this error entirely.

6. **Add the detector and relay**: Connect a galvanometer or instrumentation amplifier across the bridge output (the two midpoints). When the RTD resistance matches the setpoint resistance, the bridge is balanced and the output is zero. When temperature deviates, the bridge output is proportional to the temperature error. Amplify this signal and drive a relay or SSR.

**Calibration**:

1. Immerse the RTD in an ice-water bath (0°C). Adjust the bridge setpoint to 100.0 Ω. The bridge should balance (zero output). If not, trim the bridge resistors.
2. Transfer to a steam bath (100°C). The RTD should read 138.5 Ω. Set the bridge setpoint to 138.5 Ω and verify that the bridge balances at 100°C.
3. Check at intermediate points (37°C body temperature = 114.2 Ω). Linearity should be excellent: the Callendar-Van Dusen equation for platinum deviates less than 0.1°C from linearity over 0-200°C.
4. For thermostat operation, set the bridge setpoint to the resistance corresponding to the desired trip temperature. Use the formula: R(T) = 100 × (1 + 0.00385 × T), where T is in °C. For example, 200°C corresponds to 177.0 Ω.

**Expected accuracy**: ±0.1-1°C over -200 to 850°C. RTDs are among the most stable and accurate temperature sensors available. Platinum is chemically inert and the resistance-temperature relationship is extremely stable over time and thermal cycling.

**Applications**: Precision furnace control, semiconductor processing (crystal growth, diffusion, oxidation furnaces), calibration laboratory temperature standards, food processing temperature monitoring, pharmaceutical process temperature validation. The RTD thermostat is the choice when you need better than ±1°C accuracy and have electronic measurement capability.

**Strengths**:
- Highest accuracy and long-term stability of any contact temperature sensor
- Nearly linear resistance-temperature relationship simplifies circuit design
- Wide range (-200 to 850°C) with excellent interchangeability (Pt100 standard)
- Platinum is chemically inert; no contamination or drift from oxidation
- Well-characterized physics; Callendar-Van Dusen equation gives precise modeling

**Weaknesses**:
- Requires electronic measurement circuitry (bridge, amplifier)
- Platinum is expensive and rare
- Fragile fine wire (0.05 mm) requires careful handling during winding
- Slow response when sheathed for protection
- Lead resistance errors require four-wire measurement for accuracy


## Reed Switch Thermostat

**Principle**: A permanent magnet is mounted on a bimetallic element. As temperature changes, the bimetallic element bends, moving the magnet relative to a sealed glass reed switch. The reed switch contains two ferromagnetic reed blades hermetically sealed in an inert gas atmosphere. When the magnet approaches, the magnetic field magnetizes the reed blades, causing them to attract each other and snap together, closing the circuit. When the magnet moves away, the field weakens and the reeds spring apart. The reed switch provides contactless switching: the magnet never touches the switch, and the contacts are sealed inside a glass envelope, immune to dust, oxidation, and corrosion.

**Prerequisites**:
- [Rolling mill](../machine-tools/forming.md) for producing thin bimetallic strips
- Two metals with different expansion coefficients ([brass](../metals/copper-bronze.md) + [steel](../metals/iron-steel.md))
- [Bonding method](../machine-tools/joining.md) for bimetallic strip (riveting, brazing)
- [Spring tempering](../metals/iron-steel.md) capability
- [Permanent magnet](../metals/non-ferrous.md) (ferrite or alnico)
- Sealed reed switch (glass envelope, normally open contacts)

**Materials**:
- [Bimetallic strip](../metals/alloys.md) (steel/brass, 0.3 mm thick, 8 mm wide, 60 mm long)
- [Permanent magnet](../metals/non-ferrous.md): ferrite bar (5 × 5 × 10 mm) or [alnico disc](../metals/alloys.md) (6 mm diameter, 3 mm thick)
- [Reed switch](../electronics/passive-components.md): glass envelope (45 mm long, 5 mm diameter), normally open contacts rated for 0.5-1 A
- [Mounting bracket](../metals/iron-steel.md) (aluminum or plastic)
- [Adjustment screw](../machine-tools/machining.md) (M3) with locknut

**Construction**:

1. **Mount the magnet on the bimetallic strip**: Epoxy or braze the permanent magnet to the free end of the bimetallic strip. The magnet's orientation matters: the magnetic field must be parallel to the reed switch axis (longitudinal to the reed blades) for maximum sensitivity. A magnet oriented perpendicular to the reeds requires closer approach to actuate.

2. **Mount the reed switch**: Fix the reed switch in a stationary position on the mounting bracket, parallel to the bimetallic strip, with the reed blade gap positioned at the point where the magnet will pass. The gap between the magnet and the reed switch at the actuation temperature should be about 2-5 mm, depending on magnet strength.

3. **Calculate the geometry**: The bimetallic strip deflects approximately D = K × (L²/t) × ΔT. For a 60 mm long, 0.6 mm thick steel-brass strip, K ≈ 14 × 10⁻⁶/°C. At ΔT = 20°C, deflection D ≈ 14 × 10⁻⁶ × (60²/0.6) × 20 = 1.7 mm. The magnet must move about 2-3 mm relative to the reed switch to transition from "on" to "off." This requires a strip long enough to produce that deflection over the desired temperature range.

4. **Set the trip point**: Mount an adjustment screw that moves the reed switch position relative to the strip. Turning the screw shifts the switch closer to or farther from the magnet, changing the temperature at which the magnetic field is strong enough to close the reeds.

5. **Wire the circuit**: Connect the reed switch leads in series with the heater circuit (through a relay if the heater draws more than the reed switch's rated current, typically 0.5-1 A). The reed switch carries only the relay coil current, not the full heater load.

**Calibration**:

1. Place in a temperature-controlled environment with a [reference thermometer](./temperature-pressure.md). Adjust the screw until the reed switch just closes at the desired trip temperature (detect with ohmmeter).
2. Heat and cool through the trip point 5-10 times to verify consistency. The reed switch should trip at the same temperature within ±1°C each cycle.
3. Check the deadband: the temperature difference between switch closing (on heating) and switch opening (on cooling). Reed switches with magnets have a hysteresis of about 1-2°C due to the magnetic latching effect (the reeds close at a certain field strength but don't release until the field drops below a lower threshold).

**Expected accuracy**: ±1-2°C over -40 to 120°C range. Limited by the bimetallic element and the magnet-reed hysteresis.

**Applications**: Low-voltage thermostat switching (battery-powered systems), intrinsically safe circuits (no spark outside the sealed glass envelope), protective thermostat for electronics, electric blanket control, refrigerator thermostat replacement. The reed switch thermostat is ideal for environments where contact sparking is a concern (flammable gas atmospheres, though not explosion-proof rated).

**Strengths**:
- Sealed glass envelope protects contacts from dust, oxidation, and corrosion
- No electrical power required at the sensor
- Contactless actuation via magnet; no mechanical wear on the switch
- Spark-free switching suitable for hazardous atmospheres
- Simple construction with few components

**Weaknesses**:
- Very limited current rating (0.5-1 A); must drive a relay for larger loads
- Magnetic hysteresis adds 1-2°C deadband
- Sensitive to external magnetic fields that can cause false triggering
- Limited temperature range (-40 to 120°C) set by magnet and bimetallic properties
- Not proportional; on/off switching only


## Tier 4: Semiconductor/Electronics Industry

## Thermistor-Based Electronic Thermostat

**Principle**: A thermistor is a sintered metal-oxide ceramic (typically manganese, nickel, or cobalt oxides) whose electrical resistance changes dramatically with temperature. NTC (negative temperature coefficient) thermistors decrease in resistance by 3-6% per °C, roughly 10× the sensitivity of an RTD. A 10 kΩ NTC thermistor at 25°C drops to about 3.6 kΩ at 60°C. This large resistance change simplifies the electronics: a simple voltage divider (thermistor + fixed resistor) produces a voltage that changes significantly with temperature, directly compatible with a comparator input. No bridge circuit needed.

**Prerequisites**:
- [Metal oxide powder processing](../ceramics/electronic-ceramics.md) (MnO₂, NiO, Co₃O₄)
- [High-temperature sintering](../ceramics/kilns.md) (1200-1400°C kiln)
- [Comparator circuit](../electronics/semiconductor-devices.md) (op-amp, resistors, potentiometer)
- [Relay](../electronics/passive-components.md) or [triac](../electronics/power-electronics.md) for heater switching
- [Basic PCB assembly](../electronics/pcb-fabrication.md)

**Materials**:
- [Thermistor](../ceramics/electronic-ceramics.md): NTC disc or bead type, 10 kΩ at 25°C, ±1% tolerance (or hand-made, see below)
- [Fixed resistor](../electronics/passive-components.md): 10 kΩ, 1% metal film (for voltage divider)
- [Comparator](../electronics/semiconductor-devices.md): LM311 or LM393 (dual comparator)
- [Potentiometer](../electronics/passive-components.md): 10 kΩ linear taper (for setpoint adjustment)
- [Relay](../electronics/passive-components.md): 12V DC coil, 10A contacts, or [triac](../electronics/power-electronics.md) (BT136 for AC loads)
- [Power supply](../electronics/electrical-systems.md): 5V or 12V DC regulated
- Thermistor fabrication materials (if not using commercial part):
  - [Manganese dioxide (MnO₂) powder](../chemistry/coatings.md)
  - [Nickel oxide (NiO) powder](../chemistry/coatings.md)
  - [Cobalt oxide (Co₃O₄) powder](../chemistry/coatings.md)
  - [Binder: polyvinyl alcohol (PVA) solution](../polymers/synthetic.md)
  - [Silver paste](../metals/precious-metals.md) (for electrodes)
  - [Kiln](../ceramics/kilns.md) capable of 1300°C

**Construction**:

1. **Fabricate the thermistor** (if commercial parts are unavailable): Mix MnO₂, NiO, and Co₃O₄ powders in the desired ratio (a common composition is 60% MnO₂, 30% NiO, 10% Co₃O₄ for a 10 kΩ NTC thermistor). Add PVA binder and press into discs (5 mm diameter, 2 mm thick) at 10 tons pressure. Dry at 120°C for 2 hours. Sinter at 1300°C for 4 hours in air, then cool at 5°C/minute. The sintering process fuses the oxide particles into a dense ceramic with semiconducting properties. Apply silver paste to both faces and fire at 800°C for 10 minutes to create electrical contacts. Solder lead wires to the silver electrodes. The resulting thermistor will have a nominal resistance that depends on the exact composition and sintering conditions. Measure and sort.

2. **Build the voltage divider**: Connect the thermistor in series with the fixed resistor between Vcc and ground. The junction between thermistor and resistor is the output. At 25°C, with a 10 kΩ thermistor and 10 kΩ fixed resistor, the output is Vcc/2 (2.5V with 5V supply). As temperature rises, the NTC thermistor resistance drops, and the output voltage rises (if thermistor is the lower element) or drops (if thermistor is the upper element). Choose the configuration that gives increasing voltage with increasing temperature for a heating thermostat.

3. **Build the comparator circuit**: Connect the voltage divider output to the non-inverting input of the comparator (LM311). Connect a potentiometer (voltage divider from Vcc to ground) to the inverting input. The potentiometer sets the threshold voltage (setpoint). When the thermistor voltage exceeds the setpoint, the comparator output goes high, driving the relay through a transistor driver.

4. **Add hysteresis**: Connect a high-value resistor (1-10 MΩ) from the comparator output back to the non-inverting input. This provides positive feedback that creates a small voltage hysteresis (0.5-2°C equivalent), preventing rapid on/off cycling when the temperature is near the setpoint. Without hysteresis, electrical noise or tiny temperature fluctuations cause the relay to chatter, which destroys relay contacts quickly.

5. **Wire the relay**: Connect the comparator output through a current-limiting resistor to the base of a switching transistor (2N2222 or similar). The transistor drives the relay coil. Add a flyback diode (1N4007) across the relay coil to protect the transistor from inductive voltage spikes when the relay opens.

**Calibration**:

1. Immerse the thermistor in a temperature bath with a [reference thermometer](./temperature-pressure.md).
2. Measure the voltage divider output at several temperatures. Record voltage vs. temperature.
3. Set the potentiometer to the voltage corresponding to the desired setpoint. Use the recorded data as a lookup.
4. Verify the trip point by heating through the setpoint and checking that the relay switches at the correct temperature.
5. Adjust hysteresis: if the relay cycles rapidly, increase the feedback resistor. If the deadband is too wide (temperature swings too large), decrease it.

**Expected accuracy**: ±0.1-1°C over -50 to 300°C range. The high sensitivity of NTC thermistors makes them easy to use with simple circuits. Long-term stability is ±0.1-0.2°C per year for glass-encapsulated beads, worse for epoxy-coated discs.

**Applications**: 3D printer hotend control, battery pack thermal management, home brewing temperature control, HVAC systems, medical thermometer circuits, refrigerator temperature control. The thermistor thermostat is the most common electronic thermostat in consumer products. It is cheap, sensitive, and simple to interface with both analog and digital circuits.

**Strengths**:
- Very high sensitivity (3-6% per °C) simplifies circuit design
- Simple voltage divider interface; no bridge circuit needed
- Small size allows fast response and easy placement
- Cheap to produce in quantity
- Compatible with both analog and digital circuits

**Weaknesses**:
- Non-linear resistance-temperature response complicates wide-range use
- Limited temperature range (-50 to 300°C) compared to thermocouples
- Self-heating errors if excitation current is too high
- Long-term drift of ±0.1-0.2°C per year requires periodic recalibration
- Not interchangeable without selection or software compensation


## Silicon Junction (Diode/Transistor) Thermostat

**Principle**: The forward voltage drop of a silicon pn junction decreases by approximately -2.0 to -2.2 mV per °C, nearly linearly over a wide temperature range. This property is inherent to silicon semiconductor physics: the bandgap voltage decreases with temperature, and the forward voltage tracks it. A diode (1N4148, 1N4001) or the base-emitter junction of a transistor (2N2222) driven by a constant current source produces a temperature-dependent voltage that can be measured with a simple op-amp circuit.

**Prerequisites**:
- [Semiconductor diode or transistor manufacturing](../silicon/basic-devices.md)
- [Constant current source circuit](../electronics/semiconductor-devices.md)
- [Operational amplifier](../electronics/semiconductor-devices.md)
- [Basic electronics assembly](../electronics/assembly.md)

**Materials**:
- [Silicon diode](../silicon/basic-devices.md) (1N4148 or 1N4001) or [NPN transistor](../silicon/basic-devices.md) (2N2222, connected as diode: base and collector shorted)
- [Constant current source](../electronics/semiconductor-devices.md): LM334 adjustable current source or discrete circuit (op-amp + transistor + resistor)
- [Operational amplifier](../electronics/semiconductor-devices.md): LM358 or TL072
- [Precision resistors](../electronics/passive-components.md) (1% metal film)
- [Potentiometer](../electronics/passive-components.md) for setpoint (10 kΩ, 10-turn)
- [Relay driver](../electronics/semiconductor-devices.md): switching transistor (2N2222)
- [Relay](../electronics/passive-components.md): 12V DC coil, 10A contacts
- [Flyback diode](../electronics/semiconductor-devices.md) (1N4007)
- [5V or 12V regulated power supply](../electronics/electrical-systems.md)

**Construction**:

1. **Configure the temperature sensor**: Connect a transistor as a diode (short base to collector, use the base-emitter junction as the sensing element). Drive it with a constant current of 100 μA (set by the LM334 with a 680 Ω programming resistor). At 25°C, the forward voltage is about 650 mV. At 100°C, it drops to about 485 mV. The sensitivity is about -2.1 mV/°C.

2. **Build the measurement circuit**: Amplify the diode voltage with an op-amp. Since the diode voltage decreases with temperature (for a heating thermostat, you want the output to *increase* with temperature), use an inverting amplifier configuration. Gain of 50 converts the -2.1 mV/°C slope to -105 mV/°C, which is -0.105 V/°C. Over a 100°C range, this gives a 10.5 V swing (use a ±12V supply or reduce the gain).

3. **Add the setpoint comparator**: Feed the amplified sensor voltage to one input of a comparator (LM311). Connect a potentiometer (voltage divider from Vcc to ground) to the other input as the setpoint. Add hysteresis by connecting a feedback resistor (1-10 MΩ) from the comparator output back to the sensor input.

4. **Calibration compensation**: Silicon diodes from different batches have varying nominal forward voltages (600-700 mV at 25°C). The sensor must be individually calibrated. Add an offset adjustment potentiometer to null out the part-to-part variation.

**Calibration**:

1. Immerse the sensor in an ice-water bath (0°C). Measure the output voltage. Adjust the offset pot to a convenient reference (e.g., 0V at 0°C).
2. Transfer to boiling water (100°C). The output should change by approximately 10.5V (with gain of 50). Adjust the gain resistor if needed.
3. Set the comparator trip point using the calibrated output voltage.
4. The linearity is excellent: the diode forward voltage is within ±0.5°C of linear over -55 to 150°C.

**Expected accuracy**: ±1-3°C over -55 to 150°C range. Accuracy is limited by the initial calibration and the current source stability. With careful calibration, ±0.5°C is achievable.

**Applications**: CPU temperature monitoring and throttle control, battery charger temperature cutoff, power supply overtemperature protection, simple electronic thermostat where a thermistor is not available. The silicon junction sensor is very cheap (a single diode) but has a limited temperature range compared to thermistors or RTDs. Most useful as an embedded sensor in electronic systems where a silicon diode or transistor is already present.

**Strengths**:
- Sensor is extremely cheap (a single diode or transistor)
- Nearly linear response over the operating range
- Easy to integrate into existing electronic circuits
- Small size and fast thermal response
- Well-understood semiconductor physics

**Weaknesses**:
- Limited temperature range (-55 to 150°C); unusable for high-temperature applications
- Significant part-to-part variation in forward voltage requires individual calibration
- Requires a stable constant current source for accurate readings
- Not as accurate as RTDs or thermistors without careful calibration
- Accuracy degrades if current source drifts with temperature or supply voltage


## IC Temperature Sensor Thermostat

**Principle**: A dedicated integrated circuit combines a bandgap temperature sensor with signal conditioning, analog-to-digital conversion, and (in digital types) a serial interface. The bandgap sensor exploits the difference between the thermal voltage (PTAT: proportional to absolute temperature) and the bandgap voltage (constant with temperature) to produce a calibrated output. Analog types (LM35, TMP36) output a voltage directly proportional to temperature (10 mV/°C for LM35). Digital types (DS18B20) output temperature as a digital number over a 1-wire serial interface, eliminating analog noise issues.

**Prerequisites**:
- [IC fabrication capability](../silicon/basic-devices.md)
- [PCB assembly](../electronics/assembly.md) (soldering)
- [Microcontroller](../computing/embedded-systems.md) for digital types (reading serial data)
- [Regulated power supply](../electronics/electrical-systems.md)

**Materials**:
- IC temperature sensor:
  - Analog: [LM35](../silicon/basic-devices.md) (10 mV/°C, 0-150°C), TMP36 (500 mV offset + 10 mV/°C, -40 to 125°C)
  - Digital: [DS18B20](../silicon/basic-devices.md) (12-bit resolution, -55 to 125°C, 1-wire interface), LM75 (I2C interface)
- [Comparator](../electronics/semiconductor-devices.md) (for analog types): LM311
- [Microcontroller](../computing/embedded-systems.md) (for digital types): ATmega328 or similar
- [Relay driver](../electronics/semiconductor-devices.md): switching transistor (2N2222) with [flyback diode](../electronics/semiconductor-devices.md) (1N4007)
- [Relay](../electronics/passive-components.md): 12V DC coil, 10A contacts, or [SSR](../electronics/power-electronics.md)
- [PCB](../electronics/pcb-fabrication.md), solder, hookup wire
- [Bypass capacitors](../electronics/passive-components.md) (100 nF ceramic, 10 μF electrolytic)

**Construction (Analog Type - LM35)**:

1. **Power the sensor**: Connect Vcc (4-30V) and ground to the LM35. Add a 100 nF bypass capacitor between Vcc and ground, placed within 10 mm of the IC. The LM35 draws only 60 μA, so self-heating is negligible (<0.1°C in still air).

2. **Read the output**: The LM35 output pin produces a voltage of 10 mV/°C. At 25°C, the output is 250 mV. At 100°C, it is 1.000V. This low-level signal is susceptible to noise pickup on long wires. Keep the sensor close to the comparator, or use shielded cable.

3. **Build the comparator**: Feed the LM35 output to the non-inverting input of an LM311 comparator. Feed the setpoint (from a potentiometer voltage divider) to the inverting input. The setpoint voltage for a desired temperature T is: V_setpoint = T × 0.01V. For 50°C: V_setpoint = 0.500V.

4. **Add hysteresis and relay driver**: Connect a high-value resistor (1-10 MΩ) from the comparator output back to the non-inverting input for hysteresis. Connect the comparator output through a current-limiting resistor to the base of a switching transistor (2N2222). The transistor drives the relay coil. Add a flyback diode (1N4007) across the relay coil.

**Construction (Digital Type - DS18B20)**:

1. **Wire the 1-wire bus**: Connect the DS18B20 data pin to a microcontroller GPIO pin through a 4.7 kΩ pullup resistor to Vcc. The 1-wire bus can connect multiple sensors on the same wire (each DS18B20 has a unique 64-bit serial number).

2. **Write the firmware**: Initialize the 1-wire bus, send a temperature conversion command, wait 750 ms (for 12-bit resolution), read the result. The DS18B20 returns temperature as a 16-bit signed integer in units of 0.0625°C. For thermostat operation, compare the reading to a setpoint stored in the microcontroller's EEPROM. Drive a relay based on the comparison.

3. **Add a display** (optional): Connect a 16×2 LCD or 7-segment display to show current temperature and setpoint. Add up/down buttons for setpoint adjustment. Store the setpoint in EEPROM so it survives power cycles.

**Calibration**:

1. For the LM35: verify at two temperatures (ice water and body temperature or boiling water). The LM35 is factory-calibrated to ±0.5°C at 25°C. If the reading is off by a constant offset, add a correction in the comparator setpoint. If the slope is wrong (reading drifts with temperature), the IC is defective.
2. For the DS18B20: the digital output is factory-calibrated to ±0.5°C from -10 to 85°C. Verify by immersion in a known-temperature bath. Apply a software offset correction if needed.

**Expected accuracy**: ±0.5°C typical (factory-calibrated). The DS18B20's 12-bit resolution gives 0.0625°C granularity, though absolute accuracy is ±0.5°C. The LM35 is ±0.25°C at room temperature, ±0.75°C over full range.

**Applications**: Precision temperature monitoring and control where IC packaging is acceptable, data logging temperature with microcontroller, multi-zone temperature monitoring (multiple DS18B20 on one 1-wire bus), smart thermostat projects, laboratory equipment with digital readout. The IC temperature sensor is the modern default for electronic thermostat projects: easy to interface, factory-calibrated, and available in convenient packages.

**Strengths**:
- Factory calibrated; no sensor-level calibration needed
- Easy interface (voltage output for analog, serial bus for digital)
- Digital types eliminate analog noise and long-wire signal degradation
- Multiple sensors on a single bus (DS18B20 1-wire)
- Compact IC packages with minimal external components

**Weaknesses**:
- Requires full IC fabrication infrastructure to manufacture
- Limited temperature range (-55 to 150°C) by silicon semiconductor physics
- Packaged ICs not suitable for harsh environments (corrosive, high-pressure, cryogenic)
- Self-heating in small packages affects accuracy at low airflow
- Dependent on a single supplier or complex supply chain for specific IC types


## Digital/Microcontroller PID Thermostat

**Principle**: Any electronic temperature sensor (thermocouple, RTD, thermistor, IC sensor) feeds its reading to a microcontroller running a Proportional-Integral-Derivative (PID) control algorithm. The PID algorithm computes three terms from the error (difference between measured temperature and setpoint): P = proportional to current error, I = integral of error over time (eliminates steady-state offset), D = derivative of error (anticipates future error, reduces overshoot). The combined PID output drives a solid-state relay (SSR), triac, or PWM-controlled heater. The result is smooth, precise temperature regulation without the oscillation inherent in on/off control.

The PID algorithm in discrete form: output(n) = Kp × e(n) + Ki × Σe(i) × Δt + Kd × (e(n) - e(n-1)) / Δt, where e(n) = setpoint - measurement, Kp/Ki/Kd are tuning constants, and Δt is the sample interval.

**Prerequisites**:
- [Microcontroller](../computing/embedded-systems.md) (Arduino ATmega328, ESP32, STM32, or similar)
- [Firmware development capability](../computing/embedded-systems.md) (C/C++ programming)
- [Electronic temperature sensor](./temperature-pressure.md) (thermistor, RTD, thermocouple with amplifier, or IC sensor)
- [Solid-state relay (SSR)](../electronics/power-electronics.md) or [triac](../electronics/power-electronics.md) for heater switching
- [PCB assembly](../electronics/pcb-fabrication.md) and [power supply](../electronics/electrical-systems.md)

**Materials**:
- [Microcontroller board](../computing/embedded-systems.md) (Arduino Nano, ATmega328P, or equivalent)
- Temperature sensor (choose one):
  - [Thermistor](../ceramics/electronic-ceramics.md) (10 kΩ NTC) with voltage divider
  - [RTD (Pt100)](../metals/precious-metals.md) with Wheatstone bridge and amplifier
  - [Thermocouple](./temperature-pressure.md) with MAX6675 or MAX31855 converter IC
  - [IC sensor (DS18B20 or LM35)](../silicon/basic-devices.md)
- [SSR](../electronics/power-electronics.md): DC-controlled AC solid-state relay (Fotek SSR-25DA or equivalent, rated for heater current)
- [Enclosure](../polymers/thermoplastics.md) and connectors
- [Display (optional)](../electronics/semiconductor-devices.md): 16×2 LCD or OLED
- [Keypad or rotary encoder](../electronics/passive-components.md) (for setpoint entry)
- [Power supply](../electronics/electrical-systems.md): 5V DC for microcontroller, 12V DC for SSR control

**Construction**:

1. **Build the sensor interface**: Connect the temperature sensor to the microcontroller's ADC input (for analog sensors) or digital I/O (for DS18B20 or other digital sensors). For thermocouple input, use a MAX6675 or MAX31855 thermocouple-to-digital converter IC, which handles cold junction compensation and outputs temperature directly over SPI.

2. **Wire the SSR control**: Connect a microcontroller PWM output pin to the SSR control input through a current-limiting resistor (220 Ω for most SSRs). The SSR switches the AC heater power. The microcontroller varies the duty cycle of the PWM signal to control average heater power. A 10-second PWM period with 1-second resolution gives 10% power steps, sufficient for most applications. Faster PWM (1-2 second period) gives smoother control.

3. **Write the PID firmware**:
   ```
   // Pseudocode for PID thermostat
   setpoint = desired_temperature
   Kp = 10.0   // Proportional gain (tuning parameter)
   Ki = 0.5    // Integral gain
   Kd = 50.0   // Derivative gain
   integral = 0
   prev_error = 0
   
   loop every 500ms:
     measurement = read_sensor()
     error = setpoint - measurement
     integral = integral + error * dt
     integral = clamp(integral, -max, max)  // Anti-windup
     derivative = (error - prev_error) / dt
     output = Kp * error + Ki * integral + Kd * derivative
     output = clamp(output, 0, 100)  // 0-100% heater power
     set_pwm_duty(output)
     prev_error = error
   ```

4. **Tune the PID constants**: Start with Kp only (Ki=0, Kd=0). Increase Kp until the system oscillates, then halve it. Add Ki to eliminate steady-state offset (start small, 0.1-0.5). Add Kd to reduce overshoot (start with Kd ≈ Kp × 0.1). The Ziegler-Nichols tuning method provides a systematic approach.

5. **Add safety features**:
   - **Watchdog timer**: If the microcontroller crashes, the watchdog resets it within 250 ms, ensuring the heater doesn't stay on indefinitely.
   - **High-limit cutoff**: Independent hardware thermostat (bimetallic strip, Type 3) wired in series with the heater as a backup. If the software fails, the hardware cutoff prevents runaway heating.
   - **Sensor break detection**: If the sensor reading goes out of range (open circuit, short circuit), shut off the heater and sound an alarm.

**Calibration**:

1. Calibrate the sensor separately by comparing it to a [reference thermometer](./temperature-pressure.md) at known temperature points. For a thermistor, record resistance vs. temperature. For a thermocouple, verify voltage output at ice point and boiling point. For an IC sensor, check against factory calibration at two temperatures.
2. The PID algorithm itself needs no calibration, only tuning. Tuning depends on the thermal characteristics of the system (heater power, thermal mass, insulation, heat loss rate). A well-insulated kiln with 2 kW heater and 50 kg of thermal mass will need different PID constants than a small oven with 200 W heater and 2 kg thermal mass.
3. Typical tuning for a small oven: Kp = 5-20, Ki = 0.1-1.0, Kd = 10-100. Start conservative (low gains) and increase until response is satisfactory.
4. Verify by running the system through a full setpoint range (e.g., from room temperature to setpoint and back). Watch for overshoot (should be <5°C), settling time (should be <10 minutes for small systems), and steady-state error (should be <0.5°C with integral term active).

**Expected accuracy**: Determined entirely by the sensor. With a thermistor: ±0.1-0.5°C. With an RTD: ±0.05-0.2°C. With a thermocouple: ±1-3°C. The PID algorithm itself contributes negligible error if properly tuned. Temperature stability of ±0.01°C is achievable with a good RTD sensor and well-tuned PID.

**Applications**: Precision furnace control for semiconductor manufacturing (crystal growth, diffusion, oxidation), laboratory oven regulation, reflow soldering, espresso machine temperature control, sous-vide cooking, 3D printer hotend and heated bed control, incubator temperature regulation. The digital PID thermostat is the standard for any application requiring precise, stable temperature control. It supersedes all purely mechanical thermostats for new designs.

**Strengths**:
- Best possible temperature control: eliminates steady-state offset (integral term), reduces overshoot (derivative term)
- Compatible with any electronic temperature sensor
- Tunable for different thermal systems by adjusting PID constants
- Supports data logging, remote monitoring, and complex control profiles
- Proportional output eliminates on/off cycling and extends heater life

**Weaknesses**:
- Requires firmware development skill (C/C++ programming)
- Software bugs can cause heater runaway if watchdog timer is not implemented
- Needs a reliable power supply; power loss disables all control
- PID tuning requires experimentation for each new thermal system
- More expensive and complex than mechanical or simple electronic alternatives


## Shape Memory Alloy (SMA) Thermostat

**Principle**: Certain alloys, most notably nickel-titanium (NiTi, also called Nitinol), undergo a reversible crystal-structure phase transition at a specific temperature. Below the transition, the alloy is in a martensitic phase (soft, easily deformed). Above the transition, it transforms to an austenitic phase (stiff, returns to a "trained" shape). If the alloy is deformed while cold and then heated through the transition temperature, it snaps back to its trained shape with substantial force (up to 500 MPa stress recovery). This provides a compact, powerful thermal actuator with no springs, no bellows, no fluid.

**Prerequisites**:
- [Nickel and titanium smelting](../metals/non-ferrous.md)
- [Precision alloy heat-treatment](../metals/alloys.md) (training the shape memory)
- [Arc melting or induction melting](../metals/refractory-metals.md) for alloy production

**Materials**:
- [NiTi wire](../metals/alloys.md) (55.8-56.0 wt% Ni, balance Ti): 0.5-1.0 mm diameter, 50-100 mm length
- Alternatively, [NiTi sheet](../metals/alloys.md) (0.2-0.5 mm thick) stamped into spring shapes
- [Bias spring](../metals/iron-steel.md) (steel, to deform the SMA when cold)
- [Electrical connections](../electronics/assembly.md) for resistive heating (if self-heated)

**Construction**:

1. **Obtain the alloy**: Melt nickel and titanium together in an arc furnace under argon atmosphere (titanium oxidizes rapidly in air at melting temperature). The composition must be controlled to within ±0.1 wt% nickel. A 56.0 wt% Ni alloy has an austenite finish temperature (Af) of about 60°C. Increasing nickel content by 0.1% lowers Af by about 10°C. This sensitivity makes precise composition control essential.

2. **Train the shape memory**: Heat the NiTi wire to 500°C (in the austenitic phase) and hold for 5 minutes. While hot, form it into the desired hot-state shape (typically straight, or a tightly coiled spring). Cool to room temperature. The wire "remembers" this shape. Now deform it to the cold-state shape (bend it, stretch it, compress it) using the bias spring. When heated above the transition temperature, it will recover the trained shape.

3. **Assemble the actuator**: Connect the NiTi wire in tension between a fixed anchor and a moving element (valve stem, switch lever). Install a steel bias spring that pulls the wire into the deformed (cold) state. When heated (either by ambient temperature or by passing electrical current through the wire), the wire contracts with force, overcoming the bias spring and moving the actuator. When cooled, the bias spring stretches the wire back to the cold position.

4. **Wire for self-heating (optional)**: If the SMA actuator is to be electrically heated (rather than responding to ambient temperature), connect electrical leads to both ends of the wire. Current through the wire causes resistive heating (NiTi resistivity is about 80 μΩ·cm). For a 100 mm length of 0.5 mm diameter wire, resistance is about 4 Ω. At 2V, this draws 0.5A (1W), sufficient to heat the wire above its transition temperature in a few seconds.

**Calibration**:

1. The transition temperature is fixed by the alloy composition. You cannot adjust it after manufacture (unlike a bimetallic strip where you can change the setpoint screw). Calibrate by immersion in a temperature bath with a [reference thermometer](./temperature-pressure.md) and measuring the actuation temperature.
2. The actuator has hysteresis: the martensite-to-austenite transition occurs at a higher temperature than the reverse. Typical hysteresis is 20-40°C. This means the actuator might snap to its hot shape at 60°C but not return to cold shape until it cools to 30-40°C. This limits the thermostat to applications where wide hysteresis is acceptable.
3. For resistive heating, calibrate the current needed to reach the transition temperature. Apply increasing current until the actuator snaps. Record the current value. This is the drive current.

**Expected accuracy**: ±1-2°C at a fixed transition temperature (determined by alloy composition). Range: -100 to 100°C, adjustable by alloy composition (NiTi transition temperature can be tuned from about -50°C to 110°C by adjusting Ni/Ti ratio and adding ternary elements like copper).

**Applications**: Automatic greenhouse vent openers, fire sprinkler actuators, automotive transmission thermal valves, medical devices (stents that deploy at body temperature), micro-actuators for robotics. SMA thermostats are niche but valuable where compact, high-force thermal actuation is needed without any external power (ambient-temperature-actuated types).

**Strengths**:
- Extremely compact actuator for the force it produces (up to 500 MPa)
- No springs, bellows, or fluids needed; the alloy itself is the actuator
- Ambient-heated versions require no external power at all
- Silent operation; no mechanical clicking or switching noise
- Can be electrically heated for active control when desired

**Weaknesses**:
- Transition temperature is fixed by alloy composition; not adjustable after manufacture
- Very wide hysteresis (20-40°C) limits precision and applicability
- Fatigue and drift after many thousands of thermal cycles
- Expensive alloy requiring precise composition control during melting
- Slow response compared to electronic switching (seconds to actuate)


## Quartz Crystal Temperature Sensor Thermostat

**Principle**: A quartz crystal cut at a specific orientation (typically Y-cut or LC-cut) has a resonant frequency that changes linearly with temperature, at about 1000 ppm/°C (1 kHz per MHz of resonant frequency per °C). A 10 MHz crystal shifts by 10 kHz per °C. A frequency counter measures the resonant frequency with high precision (1 Hz resolution is routine), giving a temperature resolution of 0.001°C for a 10 MHz crystal. The frequency-temperature relationship is exceptionally stable and reproducible, limited only by the crystal's aging rate (a few ppm per year).

**Prerequisites**:
- [Quartz crystal oscillator manufacturing](../silicon/basic-devices.md) (crystal cutting, electrode deposition)
- [Frequency counter electronics](./electrical-instruments.md) (or microcontroller with counter input)
- [Temperature-stable oscillator reference](../electronics/semiconductor-devices.md)
- [Digital electronics](../computing/digital-logic.md) for frequency-to-temperature conversion

**Materials**:
- [Temperature-sensing quartz crystal](../silicon/basic-devices.md): Y-cut, 10 MHz nominal frequency
- [Oscillator circuit](../electronics/semiconductor-devices.md): Pierce or Colpitts oscillator built around the crystal
- [Frequency counter](./electrical-instruments.md): microcontroller counter input or dedicated counter IC
- [Reference oscillator](../silicon/basic-devices.md): standard AT-cut quartz crystal (temperature-stable, ±10 ppm over 0-60°C) for the frequency counter clock
- [Microcontroller](../computing/embedded-systems.md) for frequency-to-temperature conversion and thermostat logic
- [SSR](../electronics/power-electronics.md) for heater control

**Construction**:

1. **Select the crystal**: A Y-cut quartz crystal has a nearly linear frequency-temperature coefficient of about +90 ppm/°C. An LC-cut (linear coefficient) crystal is specifically designed for temperature measurement and provides better linearity (frequency deviates less than ±0.1°C from linear over -50 to 150°C). The crystal is packaged in a metal can (HC-49 or similar) with two pins.

2. **Build the oscillator**: Construct a Pierce oscillator circuit around the temperature-sensing crystal. The circuit consists of the crystal, two capacitors (15-33 pF), a feedback resistor (1-10 MΩ), and an inverting amplifier (74HC04 hex inverter, one section). The oscillator produces a square wave at the crystal's resonant frequency. Keep component values stable: use NPO/COG ceramic capacitors (temperature coefficient ±30 ppm/°C) or silver mica capacitors.

3. **Count the frequency**: Feed the oscillator output to a microcontroller counter input. Count the number of oscillations in a 1-second gate time (gated by the reference oscillator). A 10 MHz crystal at 25°C might produce 10,000,000 Hz. At 26°C, it produces 10,000,000 × (1 + 90 × 10⁻⁶) = 10,000,900 Hz. The 900 Hz difference is easily measured with a 1-second gate time. Longer gate times (10 seconds) give 10× better resolution.

4. **Convert frequency to temperature**: The microcontroller computes temperature from frequency using a calibration formula. For an LC-cut crystal with linear coefficient: T = (f_measured - f_0) / (f_0 × k), where f_0 is the frequency at 0°C and k is the temperature coefficient (about 90 × 10⁻⁶/°C). For better accuracy, use a 3rd-order polynomial fit from calibration data.

5. **Implement thermostat logic**: Compare the computed temperature to the setpoint. Drive the SSR with proportional control: compute the temperature error (setpoint minus measurement), multiply by a gain factor to get heater power percentage, and set the SSR PWM duty cycle accordingly. For tighter control, implement a full PID algorithm: compute proportional (current error), integral (accumulated error over time), and derivative (rate of error change) terms, combine them with tuning constants, and output the result as heater power percentage. The microcontroller updates the output every 500 ms to 1 second, adjusting the PWM duty cycle sent to the SSR.

**Calibration**:

1. Immerse the crystal sensor in a temperature-stable bath (ice-water, body temperature, boiling water) with a [reference thermometer](./temperature-pressure.md). Measure the frequency at each point.
2. Fit a polynomial: f(T) = f₀ × (1 + k₁T + k₂T² + k₃T³). The coefficients k₁, k₂, k₃ are determined by the crystal cut and are stable over the crystal's lifetime. For an LC-cut crystal, k₁ ≈ 35 × 10⁻⁶/°C, k₂ is small, k₃ is negligible.
3. Store the calibration coefficients in the microcontroller's EEPROM.
4. Verify at intermediate temperatures. Residual error should be less than ±0.05°C over the calibrated range.

**Expected accuracy**: ±0.01-0.05°C over -50 to 250°C range. Resolution limited only by frequency counter gate time and reference oscillator stability. With a 10-second gate time and a stable reference oscillator, resolution of 0.001°C is achievable.

**Applications**: High-precision temperature measurement and control, calibration of other temperature sensors, meteorological reference instruments, semiconductor process monitoring where ultra-stable temperature measurement is needed. The quartz crystal thermostat is overkill for most applications but provides the best combination of accuracy, stability, and resolution available in a reasonably simple electronic sensor.

**Strengths**:
- Best resolution of any practical temperature sensor (0.001°C achievable)
- Exceptional long-term stability (a few ppm per year aging)
- Digital output (frequency) inherently immune to analog noise
- Frequency-temperature relationship is stable and reproducible
- Suitable for calibration of other temperature sensors

**Weaknesses**:
- Complex electronics required (oscillator, frequency counter, microcontroller)
- Expensive specialized crystal (Y-cut or LC-cut, not the common AT-cut)
- Limited range compared to thermocouples (-50 to 250°C)
- Slow thermal response due to metal can packaging
- Overkill for most applications; hard to justify the cost and complexity


## Infrared/Radiation Pyrometer Thermostat

**Principle**: Every object above absolute zero emits thermal radiation described by Planck's law. The total radiated power and its spectral distribution depend on the object's temperature and emissivity. An infrared pyrometer collects this radiation (through optics: lens, mirror, or fiber optic), focuses it onto a detector (thermopile, pyroelectric sensor, or photodiode), and converts the detector signal to a temperature reading. Because the sensor measures radiation without physical contact, it can regulate the temperature of moving objects, molten metals, semiconductor wafers in vacuum, and any target that cannot be touched by a probe.

**Prerequisites**:
- [Optical components](../optics/inspection.md) (lenses, mirrors, windows transparent to IR radiation)
- [IR detector fabrication](../electronics/semiconductor-devices.md) (thermopile, pyroelectric, or photon detector)
- [Amplifier and signal conditioning electronics](../electronics/semiconductor-devices.md)
- [Calibration](./precision-metrology.md) against known-temperature blackbody sources
- [Microcontroller](../computing/embedded-systems.md) for temperature computation and PID control

**Materials**:
- IR optics: [germanium lens](../optics/inspection.md) (for 2-14 μm band), [calcium fluoride window](../optics/inspection.md), or [gold-coated mirror](../optics/optical-coatings.md)
- Detector:
  - [Thermopile](../electronics/semiconductor-devices.md) (multiple thermocouple junctions on a silicon chip, output ~50 μV/°C of target temperature)
  - [Pyroelectric sensor](../ceramics/advanced-ceramics.md) (lithium tantalate crystal, generates charge proportional to rate of temperature change)
  - [InGaAs photodiode](../silicon/basic-devices.md) (for 1-2.5 μm band, high-temperature targets)
- [Amplifier](../electronics/semiconductor-devices.md): low-noise op-amp (OP27, AD745) with gain 1000-10000
- [Microcontroller](../computing/embedded-systems.md) with ADC
- [Emissivity adjustment](../electronics/passive-components.md): potentiometer or software setting

**Construction**:

1. **Build the optics**: For a single-wavelength (spectral) pyrometer, use a germanium lens (25 mm diameter, 50 mm focal length, AR-coated for 8-14 μm) to focus IR radiation from the target onto the detector. The lens must be made of a material transparent at the measurement wavelength (glass is opaque in the thermal IR). Germanium, zinc selenide, and calcium fluoride are common IR lens materials. For a simpler design, use a reflective objective (gold-coated concave mirror) which avoids chromatic aberration and works over any wavelength.

2. **Mount the detector**: Position the detector element at the focal point of the optics. For a thermopile detector, the active area is typically 1-2 mm diameter. The detector must see only the target (no stray radiation from the housing). Use a baffled tube (inner surface painted matte black) between the lens and detector to block stray light.

3. **Build the amplifier**: The thermopile output is tiny (50-500 μV for typical temperature ranges). Amplify with a precision instrumentation amplifier (gain 1000-10000, input offset < 1 μV). Use a low-pass filter (0.1-1 Hz cutoff) to reject 50/60 Hz power-line interference and high-frequency noise. Shield the amplifier and detector connections in a metal enclosure to reduce electromagnetic pickup.

4. **Add the reference junction**: The thermopile measures the difference between the target temperature and the detector temperature. You must measure the detector's own temperature independently (with a thermistor or RTD mounted on the thermopile package) and add it to the differential reading to get absolute target temperature.

5. **Compute temperature from radiation**: The total radiated power per unit area is given by the Stefan-Boltzmann law: P = ε × σ × T⁴, where ε is emissivity (0-1), σ is the Stefan-Boltzmann constant (5.67 × 10⁻⁸ W/m²/K⁴), and T is absolute temperature. The detector voltage is proportional to the received power, which is proportional to the target's T⁴ (minus the detector's T⁴). The microcontroller computes: T_target = ((V_detector / (ε × k)) + T_detector⁴)^(1/4), where k is a calibration constant.

6. **Handle emissivity**: The emissivity ε varies with material and surface condition. Polished metals have ε = 0.05-0.2 (poor emitters, difficult to measure with IR). Oxidized metals and most non-metals have ε = 0.8-0.95 (good emitters). The operator must set the correct emissivity value in the pyrometer. Error from wrong emissivity setting: a 10% error in ε causes about 2.5% error in measured temperature (at typical process temperatures, this is 10-30°C). A two-color (ratio) pyrometer avoids this problem by measuring the ratio of radiation at two wavelengths; the ratio is emissivity-independent.

7. **Implement PID control**: Feed the computed temperature to a PID algorithm running on the microcontroller. Compute the proportional term (gain times current error), the integral term (accumulated error over time), and the derivative term (rate of error change). Combine all three with tuning constants to produce a heater power output from 0 to 100%. Drive the SSR with PWM at the computed duty cycle. Update the control loop every 500 ms to 1 second, reading the detector, computing temperature, and adjusting heater power.

**Calibration**:

1. **Blackbody calibration**: Point the pyrometer at a blackbody calibration source (a cavity with ε ≈ 0.999, heated to a known temperature by a calibrated RTD). Measure the pyrometer output at 5-6 temperatures across the range.
2. Fit a calibration curve: plot detector voltage vs. T⁴ (Stefan-Boltzmann). The relationship should be linear for a thermopile detector. The slope gives the calibration constant k; the intercept gives the detector self-radiation offset.
3. **Emissivity verification**: Measure a known-temperature object with known emissivity (e.g., a painted steel plate at 200°C, ε ≈ 0.95) to verify that the emissivity compensation works correctly.
4. For a two-color pyrometer: calibrate at two or more temperatures using the blackbody source. The ratio of the two detector channels should be independent of emissivity.

**Expected accuracy**: ±0.5-2% of reading (in Kelvin) over 0 to 3000°C+. A 2% error at 1000°C (1273 K) is about 25°C. At 200°C (473 K), it is about 9°C. Better accuracy requires careful calibration and correct emissivity setting. Two-color pyrometers achieve ±0.5% with emissivity independence.

**Applications**: Steel and glass melting furnace control, semiconductor wafer temperature measurement during rapid thermal processing, kiln and furnace regulation where contact sensors cannot survive, moving web temperature monitoring (paper, plastic film, steel strip), engine turbine blade temperature measurement. The IR pyrometer thermostat is essential for any application where the target cannot be contacted, is moving, is too hot for contact sensors, or is in a vacuum chamber where a probe would contaminate the process.

**Strengths**:
- Non-contact sensing; measures temperature without touching the target
- Very high temperature capability (0 to 3000°C+)
- Can measure moving objects, molten metals, and targets in vacuum chambers
- Fast response limited only by detector and electronics speed
- No probe contamination or degradation in harsh environments

**Weaknesses**:
- Accuracy depends heavily on correct emissivity setting
- Expensive IR-transparent optics (germanium, zinc selenide)
- Requires clear line of sight to the target
- Struggles with polished metals (low emissivity, weak signal)
- Needs blackbody calibration source for reliable accuracy


## Selection Guide

| Type | Range (°C) | Accuracy | Power Required | Remote Sensing | Best Use |
|------|-----------|----------|---------------|----------------|----------|
| 1. Single-metal rod | 100-800 | ±10-20°C | None | No | Crude furnace draft control |
| 2. Rod-and-tube | 50-800 | ±5-10°C | None | No | Simple oven, kiln control |
| 3. Bimetallic strip | -50 to 500 | ±2-5°C | None | No | General-purpose switching |
| 4. Snap-action disc | 30-300 | ±2-3°C | None | No | Appliance safety cutoff |
| 5. Mercury tilt | -10 to 300 | ±0.5-1°C | None | No | Room thermostat (heating) |
| 6. Mercury contact | -30 to 300 | ±0.1-0.5°C | None | No | Lab temperature regulation |
| 7. Liquid expansion | -50 to 400 | ±1-3°C | None | Yes | Remote oven/tank sensing |
| 8. Vapor pressure | -50 to 300 | ±1-2°C | None | Yes | Refrigeration TXV |
| 9. Gas expansion | -200 to 800 | ±0.5-1°C | None | Yes | Industrial furnace |
| 10. Wax pellet | 30-95 | ±2-3°C | None | No | Engine cooling thermostat |
| 11. TRV | 5-30 | ±1-2°C | None | No | Radiator zone control |
| 12. Pneumatic | 10-35 | ±0.5-1°C | Compressed air | No | Building HVAC |
| 13. Thermocouple | -200 to 1800 | ±1-5°C | Sensor: none | Yes | High-temp furnace control |
| 14. RTD | -200 to 850 | ±0.1-1°C | Electronics | Yes | Precision furnace control |
| 15. Reed switch | -40 to 120 | ±1-2°C | None | No | Spark-free switching |
| 16. Thermistor | -50 to 300 | ±0.1-1°C | Electronics | Yes | General electronic thermostat |
| 17. Silicon junction | -55 to 150 | ±1-3°C | Electronics | No | Embedded sensor in circuits |
| 18. IC sensor | -55 to 150 | ±0.5°C | Electronics | No | Smart thermostat projects |
| 19. PID/microcontroller | Sensor-dependent | ±0.01°C possible | Electronics | Yes | Precision process control |
| 20. SMA actuator | -100 to 100 | ±1-2°C | Optional | No | Compact thermal actuator |
| 21. Quartz crystal | -50 to 250 | ±0.01-0.05°C | Electronics | No | Calibration-grade sensing |
| 22. IR pyrometer | 0 to 3000+ | ±0.5-2% | Electronics | Yes (non-contact) | High-temp, non-contact |

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Foundational metalworking | Expansion rod, rod-and-tube, bimetallic strip thermostats for furnace and kiln control |
| Glass & Chemistry | Mercury tilt, mercury contact, liquid/vapor/gas thermostats (glassworking, hermetic sealing, fluid handling) |
| Energy & Steam | Pneumatic thermostats for building HVAC, thermocouple-based boiler control, wax pellet engine cooling |
| Chemistry & Processes | Vapor pressure thermostats for refrigeration, RTD thermostats for reaction temperature control |
| Electronics | Thermistor, silicon junction, and IC sensor thermostats; PID control with microcontroller |
| Silicon & Semiconductors | PID-controlled furnaces with RTD or thermocouple sensors (±0.1-0.5°C), IR pyrometers for wafer temperature |
| Quality Control | Calibration-grade quartz crystal sensors (±0.01°C), temperature cycling tests |

## Key Deliverables

- **Tier 1** (Years 5-15): Bimetallic strip and snap-action disc thermostats for basic furnace and kiln control. These require only metalworking and are sufficient for steel production, pottery firing, and basic chemical processing.
- **Tier 2** (Years 15-25): Mercury tilt thermostat for precise room and oven control. Liquid expansion and vapor pressure thermostats for remote sensing in industrial processes. Wax pellet thermostats for engine cooling once internal combustion is developed.
- **Tier 3** (Years 25-40): Thermocouple thermostats for high-temperature furnace control (steel, glass, ceramics). RTD thermostats for precision applications. These are essential for the chemistry and early semiconductor stages.
- **Tier 4** (Years 40-60+): Digital PID thermostats with thermistor, RTD, or IC sensors for semiconductor furnace control (±0.1°C or better). IR pyrometer feedback for crystal growth and rapid thermal processing. Quartz crystal sensors for calibration-grade temperature measurement.

## Safety & Hazards

- **Mercury toxicity**: Types 5 and 6 use elemental mercury. Mercury vapor from spills, broken ampoules, and filling operations causes cumulative neurological damage. IDLH: 10 mg/m³. Vapor pressure at 20°C is 0.0012 mm Hg, enough to exceed safe limits in unventilated rooms after a spill. Fill and calibrate mercury thermostats in fume hoods or under local exhaust ventilation. Clean spills with zinc dust or commercial mercury absorbent. Never vacuum mercury spills (vaporizes mercury and disperses it). Store mercury in sealed glass containers under water or mineral oil. Use mercury-free alternatives (bimetallic strip, thermocouple, thermistor) wherever possible.
- **Pressure hazards**: Types 7-9 (sealed fluid and gas systems) contain pressurized fluids. A gas expansion thermostat at 800°C may contain nitrogen at 25+ bar. Sudden rupture of the bulb or capillary causes explosive release of hot fluid. Proof-test all sealed systems at 1.5× maximum operating pressure behind a polycarbonate blast shield. Never point the capillary end toward anyone during pressure testing. Replace any unit that shows bulging, cracking, or corrosion.
- **High-temperature burn risks**: Thermostat calibration involves placing sensors in hot baths, ovens, and furnaces. Temperatures of 200-1000°C cause instant deep burns on contact. Use heat-resistant gloves, tongs, and face shields. Allow equipment to cool before handling.
- **Electrical hazards**: Types 13-19 involve mains-voltage switching (120-240V AC) through relays and triacs. Incorrect wiring causes electrocution, fire, or equipment damage. Use insulated tools, work with power disconnected, and verify with a voltmeter before touching any circuit. Enclose all mains-voltage wiring in grounded metal or insulated enclosures.
- **Fire risk from heater runaway**: The most dangerous failure mode for any thermostat is stuck-on (heater remains powered indefinitely). A 2 kW oven element stuck on in an insulated enclosure can reach 800°C, igniting surrounding materials. Always include an independent high-limit cutoff (bimetallic disc, Type 4) wired in series with the heater, set 20-50°C above the normal operating range. This backup device must be mechanically independent of the primary thermostat.

## Limitations

- **Mechanical wear**: Contact-type thermostats (Types 1-6, 15) rely on physical contacts that erode with each switching cycle. A relay switching 10A at 240V AC has a rated life of 100,000-1,000,000 cycles. At 6 cycles per hour (typical heating system), this is 2-20 years. Arcing accelerates wear; snap-action mechanisms (Types 4, 5) reduce arcing by switching fast.
- **Deadband and hysteresis**: On/off thermostats cannot hold temperature exactly at the setpoint. They cycle between an upper and lower limit (the deadband). Mechanical thermostats have deadbands of 1-15°C. Even electronic on/off thermostats have 0.5-2°C deadband (set by software hysteresis). Only PID control (Type 19) eliminates deadband by modulating heater power proportionally.
- **Thermal lag**: The sensor temperature always lags behind the process temperature. A bimetallic strip in still air takes 30-60 seconds to reach equilibrium. A thermocouple in a thermowell takes 5-20 seconds. This lag causes overshoot (heater is still on when the process is already above setpoint because the sensor has not caught up). PID control compensates for lag with the derivative term, but it cannot eliminate it entirely.
- **Sensor range limits**: No single sensor covers the full range from cryogenic to 3000°C. Thermocouples cover the widest range but sacrifice low-temperature accuracy. RTDs are best from -200 to 850°C. Thermistors are best from -50 to 300°C. IR pyrometers struggle below 0°C (weak radiation signal). Any bootstrap civilization needs multiple sensor types for different applications.
- **Calibration drift**: All temperature sensors drift with time and thermal cycling. Thermocouples drift 1-5°C per 1000 hours at high temperature. RTDs drift 0.1-0.5°C per year. Thermistors drift 0.1-0.2°C per year. Regular calibration against fixed-point references (ice point, steam point, metal freezing points) is essential. A thermostat that was accurate when installed will be inaccurate after a year of service without recalibration.
- **Electromagnetic interference**: Electronic thermostats (Types 16-19) are susceptible to EMI from motor drives, welders, and radio transmitters. A thermocouple wire run alongside a motor power cable can pick up several millivolts of noise, causing temperature errors of 10-50°C. Use twisted-pair wiring, shielded cables, and signal conditioning filters to reject interference.

## See Also

- [Temperature & Pressure Measurement](./temperature-pressure.md): thermocouples, RTDs, pyrometers, pressure gauges
- [Precision Metrology](./precision-metrology.md): calibration infrastructure, measurement uncertainty
- [Electrical Instruments](./electrical-instruments.md): multimeters, oscilloscopes, frequency counters
- [Metals](../metals/iron-steel.md): metal forming, thermocouple materials, spring steel
- [Glass](../glass/glassblowing.md): glassworking for mercury thermostats, ampoules
- [Chemistry](../chemistry/semiconductor-chemicals.md): mercury production, metal oxides for thermistors
- [Silicon](../silicon/basic-devices.md): semiconductor sensors, IC temperature sensors
- [Energy](../energy/cooling.md): steam systems, HVAC, engine cooling



[← Back to Measurement](index.md)
