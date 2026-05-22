# Heat Engines

> **Node ID**: energy.engine
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.fuels`](fuels.md), [`metals`](../metals/index.md), [`machine-tools`](../machine-tools/index.md)
> **Timeline**: Years 20-50
> **Outputs**: internal_combustion_engines, gasoline_engines, diesel_engines, mechanical_power

Internal combustion engines convert chemical energy in fuel directly into mechanical work inside the engine itself — unlike steam engines (external combustion), where fuel burns in a separate boiler. The key advantage is power-to-weight ratio: a gasoline engine produces 5-50 kW per kilogram of engine weight, compared to 0.01-0.05 kW/kg for a steam engine. This makes motorized transport, aviation, and portable power generation practical.

### Otto Cycle (Four-Stroke Gasoline Engine)

Invented by Nikolaus Otto (1876). The dominant engine for road vehicles and small aircraft.

**[Four-stroke cycle](../glossary/four-stroke-cycle.html)** (two crankshaft revolutions per power stroke):

1. **Intake stroke**: Piston moves down. Intake valve opens. Fuel-air mixture (from carburetor or fuel injector) drawn into cylinder. Typical mixture: 14.7:1 air-to-fuel ratio by mass (stoichiometric for gasoline).
2. **Compression stroke**: Both valves close. Piston moves up, compressing mixture to 8-12× atmospheric pressure (compression ratio 8:1 to 12:1). Compressed mixture reaches 400-600°C.
3. **Power stroke**: Spark plug ignites compressed mixture near top dead center (TDC). Combustion gases reach 2000-2500°C and 40-80 bar pressure, driving piston down. Peak cylinder pressure 50-80 bar.
4. **Exhaust stroke**: Exhaust valve opens. Piston moves up, pushing burnt gases out. Exhaust temperature 600-900°C.

**Thermal efficiency**: 25-35% (fuel energy → mechanical work). The remaining 65-75% is lost as heat in exhaust (30-40%) and cooling system (30-35%).

**Compression ratio effects**: Higher compression = more efficient (Otto cycle efficiency = 1 - 1/r^(γ-1), where r is compression ratio and γ ≈ 1.4 for air). Practical limit: gasoline-air mixture auto-ignites (knocks) above ~12:1. Octane rating measures knock resistance — higher octane enables higher compression.

**Key components**:
- **Cylinder block**: Cast iron or aluminum alloy. Houses cylinders (1-12 cylinders in common configurations). Bore 60-120 mm, stroke 60-120 mm.
- **Cylinder head**: Cast iron or aluminum. Contains intake and exhaust valves, spark plugs, and combustion chamber. Typically 2-4 valves per cylinder.
- **Pistons**: Aluminum alloy (low weight for high reciprocating speed). Piston rings (cast iron) seal against cylinder wall — compression rings (2) and oil control ring (1). Wrist pin connects piston to connecting rod.
- **Connecting rod**: Forged steel. Converts reciprocating piston motion to rotary crankshaft motion. Length 2× stroke typically.
- **Crankshaft**: Forged steel. Converts force from connecting rods into rotary output. Counterweights balance reciprocating masses. Main bearings (2-7) and rod bearings are babbitt-lined or tri-metal (steel-copper-lead).
- **Valvetrain**: Intake and exhaust valves operated by camshaft via pushrods (OHV) or directly (OHC). Valve springs close valves. Valve timing: intake opens 5-30° before TDC, closes 40-70° after BDC; exhaust opens 40-70° before BDC, closes 5-30° after TDC. Duration ~240-300° of crankshaft rotation.

**Ignition system**: Battery-powered ignition coil steps 6-12V to 10,000-40,000V. Distributor routes high voltage to spark plugs in firing order. Spark timing: 5-40° before TDC (advances with engine speed). Later: electronic ignition replaces points and distributor.

### Diesel Cycle

Invented by Rudolf Diesel (1892). Higher efficiency than Otto cycle, used for trucks, heavy equipment, ships, and generators.

**Key differences from Otto cycle**:
- **No throttle, no spark plug**: Air is compressed alone (no fuel mixture). Fuel is injected directly into hot compressed air at the end of the compression stroke. The high temperature from compression ignites the fuel spontaneously.
- **Compression ratio 14:1 to 24:1**: Much higher than gasoline. Compressed air reaches 700-900°C — above the auto-ignition temperature of diesel fuel (~210°C).
- **Thermal efficiency**: 35-45%. Higher than Otto cycle due to higher compression ratio and lean-burn operation (excess air).

**Fuel injection**: High-pressure fuel pump (100-2000 bar for modern common-rail, 100-350 bar for older systems) forces fuel through precision injector nozzles. Nozzle orifice diameter 0.1-0.3 mm. Injection timing: begins 5-20° before TDC, continues 20-40° of crank rotation. Injection duration and timing control power output and emissions.

**Construction differences from gasoline engine**:
- **Stronger block and head**: Higher cylinder pressures (80-200 bar peak vs. 50-80 bar for gasoline) require heavier cast iron block and head. Thicker cylinder walls, stronger head bolts.
- **Heavier pistons**: Pistons must withstand higher peak pressures. Often have integrated cooling galleries (oil jet sprays piston underside).
- **Glow plugs**: Electric heaters in combustion chamber for cold starting (heat compressed air above auto-ignition temperature). Required below ~5°C ambient. Draw 5-15A each, preheat 3-15 seconds before cranking.

**Turbocharging**: Exhaust gas turbine drives compressor that forces more air into cylinders. Increases power output 30-100% for same displacement. Nearly universal on modern diesels. Boost pressure 0.5-2.5 bar gauge. Turbocharger spins at 80,000-250,000 RPM — requires precision bearings lubricated by engine oil. Intercooler cools compressed air before intake (cooler air = denser = more oxygen = more power).

### Materials of Construction

- **Engine block**: Gray cast iron (Grade 25-30, ~180-230 BHN) or aluminum alloy (A356-T6, silicon-aluminum casting alloy). Cast iron is heavier but stiffer, cheaper, and wears well. Aluminum is 60% lighter but requires cast-iron cylinder liners.
- **Crankshaft**: Forged medium-carbon steel (AISI 1045) or nodular cast iron. Hardened journal surfaces (induction hardening to 50-60 HRC). Surface finish < 0.4 μm Ra on journals.
- **Connecting rods**: Forged steel (AISI 4140) or powdered metal. I-beam cross-section for strength-to-weight. Big end bearings are split, babbitt-lined or tri-metal.
- **Pistons**: Aluminum-silicon alloy (11-13% Si — low thermal expansion). Piston rings: gray cast iron or steel. Top ring may be chrome-plated or molybdenum-coated for wear resistance.
- **Cylinder head**: Cast iron or aluminum alloy. Must withstand combustion temperatures and pressures while housing valves, spark plugs/injectors, and cooling passages.
- **Valves**: Intake valves: chromium-silicon alloy steel (Silchrome 1, ~21-4N). Exhaust valves: austenitic stainless steel (21-12N) or Inconel — must withstand 700-900°C exhaust gas continuously. Valve seats: hardened alloy iron or Stellite (cobalt-chromium) inserts.
- **Gaskets**: Cylinder head gasket: copper-asbestos composite or multi-layer steel (MLS). Must seal combustion pressure (40-200 bar) while accommodating thermal expansion mismatch between block and head.
- **Bearings**: Crankshaft main and rod bearings — babbitt (tin-antimony-copper) on steel backing, or tri-metal (steel-copper-lead-tin overlay). Oil film thickness at operating speed: 2-10 μm. Oil pressure: 2-5 bar.

### Manufacturing Requirements

Internal combustion engines demand precision machining beyond what early steam engines require:

- **Cylinder boring**: Cylinders must be round and straight within 10-25 μm tolerance over full stroke length. Requires precision boring bar on lathe or dedicated boring machine. Honing after boring to achieve < 0.5 μm Ra surface finish.
- **Crankshaft grinding**: Journal surfaces ground to 5-10 μm tolerance and < 0.2 μm Ra finish. Requires cylindrical grinder.
- **Valve seat machining**: Valve seats ground at precise angles (typically 45°) to ensure gas-tight seal. Concentricity with valve guide < 0.05 mm.
- **Piston-ring gap**: Rings fitted with specific end gap (0.2-0.5 mm per 100 mm bore diameter). Gap too small → ring ends butt when hot → ring scuffs and breaks. Gap too large → blow-by and lost compression.
- **Fuel injector (diesel)**: Nozzle orifice diameter 0.1-0.3 mm, requiring precision drilling and grinding. Needle valve seat lapped for zero leakage below opening pressure.
- **Assembly clearances**: Main bearing clearance 0.025-0.065 mm. Rod bearing clearance 0.025-0.060 mm. Piston-to-cylinder wall clearance 0.025-0.070 mm (varies with piston material and expected operating temperature).

These tolerances require the full machine tool bootstrap: lathe, mill, drill press, cylindrical grinder, surface grinder, and honing equipment — all from [Machine Tools](../machine-tools/iterative-bootstrap.md). [Precision metrology](../measurement/precision-metrology.md) (micrometers, bore gauges, dial indicators) is essential for measuring these clearances during assembly.

### Applications

- **Stationary generators**: Diesel generators from 5 kW (residential backup) to 10,000+ kW (industrial power). Run at fixed speed (1500 or 1800 RPM for 50/60 Hz AC output). Fuel consumption: 0.2-0.3 L/kWh.
- **Road vehicles**: Gasoline engines for cars and light trucks (40-400 kW). Diesel engines for trucks and buses (100-500 kW). Transmission (gearbox) matches engine speed/torque to vehicle speed/load requirements.
- **Aircraft**: Gasoline engines for propeller-driven aircraft (50-2000 kW). Air-cooled radial or opposed-cylinder configurations common. Requires reliable operation at altitude and in all attitudes (including inverted flight for aerobatic aircraft). See [Aviation](../transport/aviation.md).
- **Marine**: Diesel engines for ships (500-80,000+ kW). Low-speed two-stroke diesels (50-250 RPM) directly coupled to propeller. High thermal efficiency (45-50%) makes diesel the standard for commercial shipping.
- **Pumps and compressors**: Engines driving irrigation pumps, natural gas compressors, and industrial process equipment. Often run continuously for thousands of hours between overhauls.

### Fuel Requirements

- **Gasoline**: Fractional distillation of petroleum boiling at 30-200°C. Octane rating 80-95 RON. Energy density ~44 MJ/kg (~34 MJ/L). Volatility tuned for ambient temperature range. Additives: tetraethyl lead (historical — phased out due to neurotoxicity), MTBE, ethanol blending.
- **Diesel fuel**: Petroleum fraction boiling at 180-360°C. Cetane number 40-55 (measures ignition quality — higher = shorter ignition delay). Energy density ~45 MJ/kg (~38 MJ/L). Cloud point and pour point critical for cold weather operation — paraffin wax crystallizes at low temperatures, clogging fuel filters.
- **Alternative fuels**: Producer gas (wood gasification — CO + H₂ + N₂ mixture, ~5-6 MJ/m³) can power gasoline engines with carburetor modification. Lower power output (40-60% of gasoline) but works without petroleum. Biodiesel from vegetable oil transesterification. Ethanol from fermentation.

### Gas Turbines (Brayton Cycle)

Continuous-flow engine operating on the Brayton cycle: compressor → combustor → turbine. Air is compressed, fuel is injected and burned at constant pressure, and the resulting hot gas expands through the turbine. First practical gas turbine: Frank Whittle (UK) and Hans von Ohain (Germany), independently in the 1930s.

**Principle and efficiency**: Thermal efficiency 15-40% for simple cycle (compressor work consumes 60-80% of turbine output). Combined cycle (exhaust heat drives a steam Rankine bottoming cycle) achieves 55-60%+ efficiency — the highest of any commercial power generation cycle.

**Compressor**: Axial or centrifugal. Axial compressors for large turbines: 10-16 stages, compression ratio 10:1 to 30:1, each stage adds 1.1-1.4× pressure ratio. Centrifugal compressors for small turbines: 1-2 stages, compression ratio 4:1 to 12:1, robust and tolerant of debris. Compressor efficiency 85-90%.

**Combustor**: Annular or can-annular design. Fuel injected as atomized spray into compressed air stream. Continuous combustion (no intermittent explosions like reciprocating engines). Combustion temperature 1200-1500°C. Turbine inlet temperature (TIT) limited by blade materials — nickel superalloys with air cooling allow TIT up to 1500-1700°C in advanced engines.

**Turbine section**: Axial flow, 2-5 stages. Blade cooling via internal air passages (bleed air from compressor routed through blade interior) allows gas path temperatures 200-500°C above blade metal melting point. Turbine blade materials: single-crystal nickel-based superalloys (Inconel, CMSX-4) with ceramic thermal barrier coatings (yttria-stabilized zirconia). Each blade is a precision investment casting — tolerances of ±25 μm on airfoil surfaces.

**Applications**:
- **Aircraft propulsion**: Turbojet (pure jet exhaust), turbofan (bypass air for efficiency and noise reduction), turboprop (turbine drives propeller). Modern turbofan bypass ratios 8-12:1. Overall pressure ratios 40-50:1 in latest commercial engines.
- **Power generation**: Simple cycle gas turbines 20-40% efficiency for peaking and load-following. Combined cycle (gas turbine + heat recovery steam generator + steam turbine) 55-60%+ efficiency for baseload. Units from 1 MW to 600+ MW.
- **Mechanical drive**: Pipeline compressors, gas reinjection compressors, naval propulsion. Industrial gas turbines often derived from aircraft engines (aeroderivative).

**Bootstrapping note**: Gas turbines are late-stage technology. They require precision investment casting of heat-resistant superalloys, precision machining of compressor and turbine blades to tight tolerances, advanced metallurgy (directionally solidified and single-crystal casting), and sophisticated bearing and sealing technology. Not achievable until well into the industrial era — after precision machine tools, advanced foundry practice, and alloy development are established.

### Stirling Engine

Closed-cycle external combustion engine. Working gas (air, helium, or hydrogen) is permanently sealed inside the engine and alternately heated and cooled. No valves, no explosions — smooth, quiet operation. Invented by Robert Stirling (1816), predating internal combustion engines by decades.

**Principle**: Working gas is shuttled between hot and cold spaces by a displacer. When gas is in the hot space it expands, pushing the power piston. When gas moves to the cold space it contracts, allowing the piston to return. The cycle is thermodynamically reversible — the theoretical efficiency approaches the Carnot limit: η = 1 - T_cold/T_hot.

**Configurations**:
- **Alpha**: Two separate cylinders — one hot, one cold — each with its own piston. 90° phase angle between pistons. Highest power density but more complex seals.
- **Beta**: Single cylinder with displacer and power piston in-line. Displacer moves gas between hot and cold ends; power piston extracts work. Most common configuration for small engines.
- **Gamma**: Separate expansion (hot) cylinder and compression (cold) cylinder connected by a displacer. Lower power density but mechanically simple. Often used for low-temperature difference engines.

**Performance**: Thermal efficiency 5-40% depending on temperature ratio. Key parameter: T_hot/T_cold should be maximized. Typical operating temperatures: 500-800°C hot end, 20-100°C cold end. Power density 10-100× lower than internal combustion engines of similar size. Efficiency improves with higher mean pressure — helium at 10-20 MPa achieves best results.

**Advantages**: External combustion — any heat source works (concentrated solar thermal, biomass combustion, waste industrial heat, geothermal, radioisotope). Extremely quiet operation (no combustion explosions). High theoretical efficiency approaching Carnot limit. Can run in reverse as a cryocooler or heat pump. Long service life — no fuel contamination of lubricating oil, no corrosive combustion products inside cylinders.

**Disadvantages**: Lower power density and higher weight per kW than IC engines. Dynamic sealing at high temperature is difficult — leakage reduces efficiency over time. Slow thermal response to load changes (heat exchangers have thermal inertia). Expensive heat exchangers required on both hot and cold sides. Helium and hydrogen working fluids require high-pressure sealing (hydrogen permeates many materials). Regenerator (porous matrix between hot and cold spaces) must have high surface area and low pressure drop — wire mesh or sintered metal required.

**Bootstrapping potential**: Can be built with moderate machining capability. A simple beta-configuration Stirling engine with air as working gas and cast-iron cylinder is achievable with a lathe and basic foundry work. Power output will be low (tens of watts to a few kW) but useful for small-scale solar thermal power generation or biomass combined heat and power (CHP). The critical path is sealing the power piston at elevated temperature without excessive friction or leakage.

### Safety

- **Fuel fires**: Gasoline ignites easily (flash point -43°C). Fuel system leaks near hot engine surfaces or electrical sparks cause fires. Diesel is safer (flash point 52-96°C) but atomized diesel spray ignites readily. Fuel lines must be metal tubing or approved flexible hose with proper fittings. Fire extinguisher (CO₂ or dry chemical) required near all operating engines. Fuel storage away from ignition sources, in approved containers, with proper ventilation.
- **Gas turbine hazards**: High-RPM rotating machinery (turbine spool 10,000-40,000 RPM in industrial, up to 100,000+ RPM in small aeroderivative units). Rotors contain enormous kinetic energy — catastrophic failure of a spinning turbine disc releases fragments with lethal velocity. NEVER approach a running gas turbine without approved blast shields and exclusion zones. Hot exhaust gases exit at 400-600°C (simple cycle) — severe burn hazard and ignition risk for nearby combustible materials. Fuel systems operate at high pressure (gas fuel up to 40 bar, liquid fuel up to 100 bar injection pressure). Gas turbines can auto-accelerate on load rejection — require overspeed protection systems.
- **Stirling engine hazards**: Pressurized working gas (up to 20 MPa in high-performance engines with helium/hydrogen). Vessel failure releases high-pressure gas explosively. Pressure relief valves mandatory on all sealed Stirling systems. Hydrogen working fluid is flammable and permeates many seal materials — detect and eliminate leaks before pressurizing. Hot end surfaces reach 500-800°C — same burn hazards as other high-temperature engines. Hot heat exchangers retain thermal energy for extended periods after shutdown — allow cooling before servicing.
- **Exhaust carbon monoxide (CO)**: Colorless, odorless, lethal gas. Gasoline engines produce 1-10% CO in exhaust. Diesel engines produce 0.05-0.5% CO. Running engines in enclosed spaces causes CO poisoning within minutes at these concentrations. Always operate in well-ventilated areas or route exhaust outside with sealed pipe. CO detectors in any space where engines operate. Symptoms of CO poisoning: headache, dizziness, nausea — evacuate immediately, seek fresh air and medical attention.
- **Rotating machinery hazards**: Fan belts, pulleys, chains, and rotating shafts catch loose clothing, hair, and fingers. Install guards over all rotating components. Never reach into engine compartment while running. Maintenance only with engine stopped and spark plug disconnected (gasoline) or fuel shut off (diesel). Pressurized cooling system — never remove radiator cap while engine is hot (scalding coolant at 90-120°C under 1-2 bar pressure).
- **Noise**: Unmuffled engines produce 100-120 dB — causes permanent hearing damage with exposure > 15 minutes. Mufflers reduce to 70-90 dB. Hearing protection (earmuffs rated NRR 20-30 dB) required for extended operation.
- **Hot surfaces**: Exhaust manifolds reach 300-600°C during operation. Severe burn hazard. Allow 30+ minutes cooling before touching. Exhaust heat shields where personnel may contact.
- **Battery hazards (engine starting)**: Lead-acid batteries produce hydrogen gas during charging. Spark at battery terminal ignites hydrogen → explosion. Connect/disconnect battery terminals with loads off (no sparks). Lead-acid battery electrolyte (sulfuric acid) causes chemical burns — wear eye protection when servicing.
- **Diesel fuel injection pressure**: Modern common-rail systems operate at 1000-2000+ bar. High-pressure fuel spray penetrates skin, causing tissue necrosis and potential amputation. Never touch fuel injector or high-pressure lines while engine is running. Use cardboard/paper (not hands) to search for high-pressure leaks.

### Cross-References

- **Fuel production**: [Fuel Production](fuels.md), [Petroleum & Alternative Chemistry](../chemistry/petroleum-alternatives.md)
- **Metalworking for engine blocks**: [Metal Casting](../machine-tools/casting.md), [Machining](../machine-tools/machining.md)
- **Bearings and lubrication**: [Bearings, Abrasives & Cutting Tools](../machine-tools/bearings-abrasives.md), [Lubricants](../chemistry/lubricants.md)
- **Steam engines** (external combustion predecessor): [Steam Power](steam-power.md)
- **Aviation applications**: [Aviation](../transport/aviation.md)
- **Electrical generation**: [Electricity Generation & Distribution](electricity.md)

### Diesel Engine Operating Parameters

**Compression ignition detail**: The diesel engine compresses air alone to 14:1 to 24:1 ratio, raising the charge temperature to 700-900°C at top dead center. Fuel is then injected directly into this hot compressed air. The auto-ignition temperature of diesel fuel is roughly 210°C, so the compressed air is well above the threshold. Ignition occurs within 1-4 milliseconds of injection start (ignition delay period), followed by rapid premixed combustion of the fuel that vaporized during the delay, then diffusion-controlled combustion as the remaining fuel mixes with air.

**Fuel injection timing**: Injection begins 5-15° of crankshaft rotation before TDC. The timing is critical: too early and peak cylinder pressure rises excessively (mechanical stress, knocking); too late and the fuel burns late in the expansion stroke, reducing efficiency and raising exhaust temperature. Injection duration: 20-40° of crankshaft rotation at full load. At 1500 RPM, 40° of rotation takes roughly 4.4 milliseconds.

**Injection pressure**: Modern common-rail systems operate at 100-200 MPa (1000-2000 bar). The high pressure forces fuel through nozzle orifices 0.1-0.3 mm in diameter, atomizing it into droplets of 5-50 micrometers. Smaller droplets evaporate and mix faster, enabling more complete combustion. Older mechanical injection pumps (jerk pump or distributor pump) achieve 30-100 MPa. Pilot injection (a small initial fuel quantity 2-5° before the main injection) reduces combustion noise and peak pressure in modern engines.

**Fuel quality requirements**: Cetane number ≥40 (preferably 45-55). Cetane number measures ignition quality: higher values mean shorter ignition delay and smoother combustion. Viscosity: 2.0-4.5 cSt at 40°C. Too viscous and the injection pump cannot deliver fuel at the required rate; too thin and pump lubrication suffers. Sulfur content: historically up to 2%, now limited to 10-50 ppm in most jurisdictions due to emissions concerns. Lubricity additives compensate for the lubricating properties lost with sulfur removal.

### Gas Turbine Operating Parameters

**Brayton cycle performance**: The compressor pressure ratio is the primary determinant of thermal efficiency. Early industrial gas turbines operated at 4:1 to 8:1 pressure ratio, achieving 20-28% thermal efficiency. Modern units at 20:1 to 30:1 reach 35-40% simple-cycle efficiency. The specific power output (power per unit of air mass flow) increases with both pressure ratio and turbine inlet temperature.

**Turbine inlet temperature (TIT)**: The gas temperature entering the first turbine stage is the single most important performance parameter. Early gas turbines: 800-900°C. Modern industrial units: 1200-1400°C. Advanced aero engines: 1500-1700°C (above the melting point of the blade alloy, requiring internal cooling). Each 50°C increase in TIT improves thermal efficiency by roughly 1-2 percentage points and specific power by 5-10%.

**Specific power**: Modern gas turbines produce 100-300 kW per kg/s of air mass flow. A 100 MW industrial gas turbine processes roughly 300-400 kg/s of air. The compressor absorbs 60-75% of the turbine's gross power output, leaving 25-40% as net useful shaft power. This is why combined-cycle operation is so attractive: the exhaust gas at 450-600°C still carries enormous energy that can drive a steam bottoming cycle.

### Stirling Engine Operating Parameters

**External combustion advantage**: Unlike internal combustion engines, the Stirling engine's working gas never contacts combustion products. The heat source warms the hot heat exchanger from outside, and the working gas (sealed permanently inside the engine) transfers that thermal energy into mechanical work. This means any heat source at sufficient temperature works: concentrated solar, biomass combustion, waste heat from industrial processes, geothermal, even radioisotope decay (as in space probes).

**Working gas and pressure**: Helium and hydrogen are the preferred working gases due to their high thermal conductivity and low viscosity, which minimize heat exchanger losses. Operating pressures of 5-20 MPa mean the engine casing must be a pressure vessel. Air at atmospheric pressure works for simple demonstration engines but produces very low power density (roughly 1/10 the output of helium at equivalent pressure). Hydrogen offers the best thermodynamic performance but permeates steel at high temperature and is flammable if it leaks.

**Temperature and efficiency**: Heater temperature typically 650-800°C, cooler temperature 20-60°C. Theoretical Carnot efficiency for 700°C heater and 40°C cooler: η_Carnot = 1 - 313/973 = 67.8%. Practical Stirling engines achieve 30-40% of thermal efficiency, meaning real-world output is roughly half the theoretical maximum. The gap comes from heat exchanger temperature differences, regenerator ineffectiveness, mechanical friction, and pressure drop through heat exchangers.

### Diesel Engine Operating Parameters

**Compression ignition detail**: The diesel engine compresses air alone to 14:1 to 24:1 ratio, raising the charge temperature to 700-900°C at top dead center. Fuel is injected directly into this hot compressed air. The auto-ignition temperature of diesel fuel is roughly 210°C, so the compressed air is well above the threshold. Ignition delay: 1-4 milliseconds. Injection begins 5-15° before TDC and continues 20-40° of crank rotation.

**Injection pressure**: Modern common-rail systems operate at 100-200 MPa (1000-2000 bar). The high pressure atomizes fuel through orifices 0.1-0.3 mm in diameter into droplets of 5-50 μm. Older mechanical pumps achieve 30-100 MPa. Pilot injection (a small initial fuel quantity 2-5° before main injection) reduces combustion noise and peak pressure.

**Fuel quality**: Cetane number ≥40 (preferably 45-55) for ignition quality. Viscosity: 2.0-4.5 cSt at 40°C. Sulfur: historically up to 2%, now limited to 10-50 ppm. Lubricity additives compensate for lubricating properties lost with sulfur removal.

### Gas Turbine Operating Parameters

**Brayton cycle**: Compressor pressure ratio 4:1 to 30:1. Early turbines at 4:1 to 8:1 achieved 20-28% efficiency. Modern units at 20:1 to 30:1 reach 35-40% simple-cycle. Turbine inlet temperature: 800-900°C (early), 1200-1400°C (modern industrial), 1500-1700°C (advanced aero). Each 50°C increase in TIT improves efficiency by roughly 1-2 percentage points.

**Specific power**: Modern gas turbines produce 100-300 kW per kg/s of air mass flow. The compressor absorbs 60-75% of turbine gross power. Thermal efficiency: 25-40% simple cycle, 55-60% combined cycle (with steam bottoming cycle). Combined cycle is the most efficient commercial power generation cycle.

**Diesel fuel injection timing**: Injection begins 5-15° before TDC. Timing is critical: too early causes excessive peak pressure and mechanical stress; too late reduces efficiency and raises exhaust temperature. At 1500 RPM, 40° of crank rotation takes roughly 4.4 milliseconds. Modern common-rail systems adjust timing electronically across the operating range for optimal emissions and efficiency at each load point.

**Turbocharger boost and intercooling**: Turbocharger compressors spin at 80,000-250,000 RPM on precision oil-lubricated bearings. Boost pressure: 0.5-2.5 bar gauge, increasing power 30-100% for the same displacement. Intercoolers cool the compressed air (which heats during compression) back toward ambient, increasing air density and oxygen mass per cylinder fill. Intercooler effectiveness of 70-85% is typical with air-to-air or water-to-air designs.

**Marine diesel engines**: Low-speed two-stroke diesels (50-250 RPM) directly coupled to the ship's propeller are the standard for commercial shipping. Thermal efficiency of 45-50% makes them the most efficient internal combustion engines in production. Cylinder bore up to 960 mm, stroke up to 2500 mm, individual cylinder output up to 7,000 kW. These engines burn heavy fuel oil (bunker fuel, viscosity up to 700 cSt at 50°C, requiring heated fuel systems).

**Alternative fuels for IC engines**: Producer gas (wood gasification, CO + H₂ + N₂ mixture at ~5-6 MJ/m³) can power gasoline engines with carburetor modification, though at 40-60% of gasoline power output. Biodiesel from vegetable oil transesterification substitutes directly for petroleum diesel. Ethanol from fermentation can replace or blend with gasoline. These alternatives are critical for bootstrap economies without petroleum access.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
