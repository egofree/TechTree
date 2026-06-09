# Fluid & Gas Thermostats

> **Node ID**: measurement.thermostat-fluid
> **Domain**: [Measurement](./index.md)
> **Dependencies**: [`measurement.thermostat-mechanical`](./thermostat-mechanical.md), [`glass.glassblowing`](../glass/glassblowing.md), [`chemistry.distillation`](../chemistry/distillation.md)
> **Enables**: [`energy.cooling`](../energy/cooling.md), [`energy.hvac`](../energy/cooling.md)
> **Critical**: No — mechanical and electrical thermostats are functional alternatives
> **Timeline**: Years 10-30
> **Outputs**: remote_sensing, proportional_control, mercury_switching


Fluid and gas thermostats add liquids, vapors, and gases as the sensing medium, enabling remote temperature sensing (the sensor can be meters from the controller) and frictionless switching via mercury. They build directly on the mechanical types: the mercury tilt thermostat uses a bimetallic coil to move a mercury ampoule, and the liquid expansion thermostat replaces thermal expansion of a metal rod with thermal expansion of a liquid. These types bridge the gap between purely mechanical devices and the electrical/electronic types that follow.


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

5. **Evacuate and seal**: Before sealing, evacuate the system to remove air. Air in the system adds a partial pressure that is independent of temperature, adding a constant offset that reduces the dynamic range of the pressure signal. Connect a vacuum pump to the fill port, evacuate to below 1 mbar, then seal by crimping and brazing.

6. **Add the actuator mechanism**: The bellows or bourdon tube moves proportionally to vapor pressure. Since vapor pressure is an exponential function of temperature, the actuator motion is non-linear with respect to temperature. This means the calibration scale is compressed at the low end and expanded at the high end. Account for this in the linkage design or calibration marks.

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
- [Temperature sensor](./thermostat-mechanical.html#bimetallic-strip-thermostat) (bimetallic strip, or [liquid/gas bulb](#liquid-expansion-thermostat-bulb-bellows))

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


## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Mercury thermostat setpoint drifts over weeks | Mercury contamination (oxidation film on mercury surface or electrode tips) or pivot friction increasing | Clean the mercury ampoule: remove, drain mercury, rinse with nitric acid (dilute, 10%) to dissolve oxide, rinse with distilled water, dry, and refill with fresh mercury. Clean platinum electrodes with fine abrasive (0.5 μm alumina) and rinse. Check pivot bearings for wear and lubricate with a drop of watch oil |
| Mercury does not flow between electrodes | Ampoule cracked (lost vacuum) or mercury solidified below -38°C | Inspect the glass ampoule under magnification for cracks or pinholes. If the ambient temperature is below -38°C, mercury freezes — this design cannot operate in sub-arctic conditions. Replace with a gas expansion thermostat for cold environments |
| Liquid expansion thermostat reading shifts after capillary is bent | Capillary partially kinked, restricting flow | Inspect the capillary along its length for kinks or sharp bends (minimum bend radius: 50 mm for 1.5 mm OD copper tube). A kinked capillary traps liquid on one side, causing a permanent offset. Replace the capillary section or the entire assembly |
| Vapor pressure thermostat calibration drifts | Fill quantity wrong (too much liquid — no vapor space at low temperature; too little — all evaporates at high temperature) | Verify that both liquid and vapor exist at all operating temperatures. At the lowest operating temperature, there must be liquid present. At the highest, there must be vapor space. Adjust by evacuating and refilling with the correct quantity (typically 60-80% of bulb volume as liquid at 20°C) |
| Wax pellet actuator does not return when cooled | Wax leaked past the piston seal or rubber boot torn | Disassemble and inspect the rubber boot for cracks, tears, or hardening. Check the copper guide ring for wear (worn ring allows wax extrusion). Replace the boot and guide ring. Refill with fresh wax of the correct grade. Verify the return spring provides at least 30 N force at full compression |
| TRV does not close fully (radiator overheats) | Valve seat fouled with debris or PTFE disc worn | Remove the valve body and inspect the seat. Clean with a soft brush and vinegar solution (to dissolve mineral deposits). If the PTFE disc is permanently indented or cracked, replace it. Check that the valve stem moves freely (no binding from scale or corrosion) |
| Pneumatic output pressure unstable | Supply pressure fluctuating or nozzle contaminated | Verify compressed air supply is stable at 18-20 psi (install a regulator if not). Clean the nozzle orifice (0.8 mm) with solvent and compressed air. Check the restrictor orifice (0.15 mm) for partial blockage from oil or dust in the air supply — install an inline air filter if not already present |
| Liquid expansion bellows leaks | Fatigue crack at a bellows convolution or brazed joint failed | Pressurize the system to 5 bar and immerse in water to locate the leak (bubble test). Small cracks in brass bellows can be re-brazed; stainless bellows cracks require replacement. Root cause is usually exceeding the design temperature (fill liquid expands beyond the bellows stroke, overstressing the convolutions) |
| Gas expansion thermostat reading non-linear | Air leaked into the system or gas leaked out | Test linearity by plotting bellows extension vs. temperature. A leak (air in or gas out) causes curvature. For a sealed nitrogen system, the relationship must be perfectly linear (P ∝ T). Any deviation indicates seal failure. Replace the entire assembly — field repair of hermetic seals on gas systems is unreliable |
| Mercury contact thermometer hysteresis >1°C | Capillary bore non-uniform or mercury column separated | Inspect the capillary for constrictions by watching the mercury meniscus move under gentle heating — it should move smoothly. A separated column (gap in the mercury) is caused by mechanical shock or trapped gas. Rejoin by cooling the bulb in ice (mercury contracts) and tapping gently, or by heating the bulb to drive all mercury into the upper expansion chamber |

## Safety & Hazards

- **Mercury toxicity**: All mercury-containing thermostats (mercury tilt, mercury-in-glass) contain elemental mercury, a potent neurotoxin. Acute inhalation of mercury vapor causes pneumonitis; chronic exposure causes tremor, gingivitis, and kidney damage. The IDLH (immediately dangerous to life or health) concentration is 10 mg/m³. Mercury vapor pressure at 20°C (0.0012 mm Hg) can exceed occupational exposure limits in unventilated rooms after a spill. Build and calibrate mercury thermostats under local exhaust ventilation. Clean spills with zinc dust, sulfur powder, or a commercial mercury absorbent kit. Never vacuum mercury spills (disperses mercury vapor through the exhaust). Store mercury in sealed glass containers under a layer of mineral oil or water. Dispose of mercury waste as hazardous material.
- **Glass ampoule breakage**: The borosilicate glass ampoule in mercury tilt thermostats and the capillary tube in mercury contact thermometers are fragile. A dropped ampoule releases 0.3-0.5 g of mercury as tiny droplets that spread across the floor and into crevices. Handle ampoules over a tray lined with absorbent paper. Mount mercury thermostats in protective housings (metal or plastic cover) in service.
- **Pressurized systems**: Gas expansion thermostats operate at 5-10 bar fill pressure. At maximum temperature (800°C), internal pressure can reach 25+ bar. A ruptured bellows or failed braze joint releases high-pressure gas and hot liquid. Test all pressure-containing assemblies hydrostatically at 1.5× maximum working pressure before filling with gas. Never exceed the rated temperature of the sensing bulb.
- **Volatile fill liquid hazards**: Methyl chloride (refrigeration thermostats) is toxic, flammable, and a suspected carcinogen. Acetone is extremely flammable (flash point -20°C). Toluene is flammable and a reproductive toxin. Handle fill liquids in ventilated areas with appropriate respiratory protection. Use grounding and bonding when transferring flammable liquids to prevent static ignition.
- **Compressed air**: Pneumatic thermostats operate from compressed air at 18-20 psi. While this is low pressure, compressed air injected into the skin through a cut or abrasion causes an air embolism (a medical emergency). Never point compressed air nozzles at skin. Wear safety glasses when working with pneumatic systems — particulate in the air stream can cause eye injury.



---

*Part of [Thermostats & Temperature Control](./thermostat.md) • [Measurement](./index.md) • [All Domains](../../index.md)*
