# Cylinder Filling

> **Node ID**: gas-handling.cylinder-filling
> **Domain**: [Gas Handling](./index.md)
> **Dependencies**: [`gas-handling.basic`](basic.md) (compressors, valves), [`metals.iron-steel`](../metals/iron-steel.md) (cylinder material), [`gas-handling.gas-purification`](gas-purification.md) (purified product gas)
> **Enables**: [`chemistry.hydrogen-silane`](../chemistry/hydrogen-silane.md) (H₂ cylinders), [`chemistry.dopant-etch-gases`](../chemistry/dopant-etch-gases.md) (specialty gas cylinders), [`energy.storage`](../energy/storage.md) (compressed gas energy storage)
> **Timeline**: Years 20-35
> **Outputs**: filled_cylinders, tested_cylinders, certified_cylinders
> **Critical**: No — bulk gas can be delivered via pipeline; cylinders provide portable storage

Gas cylinder filling is the process of compressing purified gases into high-pressure steel or composite vessels for storage, transport, and point-of-use delivery. Cylinders are the primary packaging format for industrial and specialty gases when pipeline distribution is impractical: remote locations, laboratory-scale consumption, mobile applications (welding, medical oxygen), and semiconductor fabs consuming specialty gases at rates too low to justify bulk delivery.

The filling process combines gas compression, cylinder inspection and preparation, controlled filling by weight or pressure, and post-fill verification. A filled cylinder at 150-200 bar contains an enormous store of compressed energy — a standard 50 L cylinder at 200 bar holds approximately 10,000 L of gas at atmospheric pressure, and the sudden release of that pressure through a failed valve or ruptured vessel creates a blast wave capable of propelling the cylinder through a concrete wall.

This capability also covers cylinder production (seamless steel tube forming), hydrostatic retesting, valve maintenance, and the regulatory framework governing cylinder certification. Every cylinder in service must be traceable to its manufacturing lot, tested on a fixed schedule, and marked with its test date, working pressure, and serial number.

## Prerequisites

- **Materials**: Seamless steel tube (manganese steel or Cr-Mo alloy), valve brass or stainless steel, PTFE valve packing, cylinder paint and labels
- **Tools and equipment**: [Basic gas handling](basic.md) — high-pressure compressors (100-300 bar); [Machine tools](../machine-tools/index.md) — lathes for valve threading, grinders for surface finishing; [Metal forming](../machine-tools/forming.md) — deep drawing or hot spinning for cylinder bodies
- **Knowledge**: High-pressure vessel design (thin-wall and thick-wall pressure vessel theory), material fatigue under cyclic loading, gas compressibility factors and equations of state
- **Infrastructure**: Filling station with blast-resistant barriers, hydrostatic test pit, cylinder drying oven, compressed air for pneumatic tools, ventilation for gas release

## Bill of Materials

| Material | Quantity (per cylinder) | Source | Alternatives |
|----------|------------------------|--------|-------------|
| Seamless steel tube (34CrMo4) | 30-60 kg per 50 L cylinder | [Metals](../metals/index.md) — forged and drawn from billet | Carbon steel (lower strength, heavier wall required) |
| Brass valve body (C36000) | 0.5-1.0 kg | [Metals](../metals/index.md) — hot forged and machined | Stainless steel valve (corrosive gas service) |
| PTFE valve packing | 5-15 g per valve | [Polymers](../polymers/index.md) | Graphite packing (higher friction, lower chemical resistance) |
| CGA connection fitting | 1 per cylinder | [Machine tools](../machine-tools/machining.md) — machined from brass or steel | DIN fitting (European standard) |
| Cylinder paint (epoxy-based) | 100-200 g | [Chemistry](../chemistry/index.md) — epoxy resin + pigments | Powder coating (requires curing oven) |
| Pressure relief device (burst disc) | 1 per cylinder | [Metals](../metals/index.md) — stamped Inconel disc | Fusible plug (melts in fire, lower precision) |
| Label (contents, hazard, DOT spec) | 1 per cylinder | [Printing](../knowledge/printing.md) | Hand-painted marking (less durable) |

## Process Description

## Cylinder Production

1. **Tube forming**: Heat a steel billet to 1100-1200°C in a gas-fired or induction furnace. Pierce the billet with a mandrel to create a hollow tube. Hot-draw the tube through a series of dies to achieve the target wall thickness (5-8 mm for 200 bar service) and outside diameter (200-230 mm for standard cylinders). The drawing process work-hardens the steel, increasing tensile strength. No welded seams — seamless construction eliminates the weakest point in a pressure vessel.
2. **Neck forming**: Hot-swell the top end of the tube inward to form the neck (reducing diameter from ~230 mm to ~25 mm for the valve opening). This is done by pressing a shaped mandrel into the heated tube end. Form the shoulder transition with a smooth radius (minimum 3× wall thickness) to avoid stress concentration.
3. **Heat treatment**: Normalize the formed cylinder body at 850-900°C to relieve forming stresses and achieve uniform grain structure. Quench in oil or water, then temper at 550-650°C to achieve the target tensile strength (800-1000 MPa for Cr-Mo steel). Improper heat treatment leaves residual stresses that cause premature fatigue failure under pressure cycling.
4. **Machining**: Thread the neck opening with a tapered internal thread (typically 25 mm ISO taper, 1:16 taper ratio) on a lathe. Machine the bottom to form a convex base (hemispherical or elliptical head distributes stress uniformly). Grind the exterior to remove scale and surface defects.
5. **Surface finishing**: Shot-blast exterior to remove oxide scale. Apply primer and paint. Paint color indicates gas contents per CGA color code (though color-coding alone is unreliable — the label is authoritative).

**Strengths:**
- Seamless construction from a single billet eliminates welded seams — the most common failure point in pressure vessels
- Hot drawing work-hardens the steel, achieving 800-1000 MPa tensile strength in Cr-Mo alloy without requiring post-forming cold work

**Weaknesses:**
- Tube forming requires 1100-1200°C furnace temperature and precision die sets — significant energy and tooling investment
- Improper heat treatment (wrong temper temperature, uneven quench) leaves residual stresses that cause premature fatigue failure under pressure cycling

## Cylinder Inspection and Preparation for Filling

1. **Visual inspection**: Examine every cylinder before filling. Reject cylinders with: visible rust or corrosion (especially at the base where moisture collects), dents deeper than 2 mm, arc burns or fire damage (discolors and weakens steel), cracked or damaged valve threads, illegible markings or expired test date. Mark rejected cylinders "REJECT" and segregate for retesting or scrapping.
2. **Check hydrostatic test date**: Every cylinder must have a current hydrostatic test (retest interval: 5 years for most steel cylinders, 10 years for certain exemptions). The test date is stamped into the cylinder shoulder. Do not fill a cylinder with an expired test date.
3. **Verify valve condition**: Ensure the cylinder valve operates smoothly (opens and closes without excessive force). Check valve outlet thread for damage. Verify the CGA connection matches the gas to be filled (wrong CGA connection = wrong gas type = potential cross-contamination or dangerous reaction).
4. **Evacuate residual gas**: Connect the cylinder to a vacuum pump and evacuate to below 100 mbar. This removes residual gas from the previous fill and any moisture that entered during storage. For cylinders that previously contained a different gas, perform three purge cycles (fill with nitrogen to 2 bar, evacuate, repeat) to ensure no cross-contamination.
5. **Weigh empty cylinder (tare weight)**: Record the tare weight to the nearest 50 g. The tare weight plus the target gas fill weight gives the final gross weight. This is the primary verification of fill completeness.

**Strengths:**
- Visual inspection catches obvious defects (dents, corrosion, fire damage) before filling — preventing pressurization of compromised vessels
- Three purge cycles for gas changeover ensure no cross-contamination — critical when switching between incompatible gases

**Weaknesses:**
- 5-year hydrostatic retest interval means a cylinder with developing fatigue cracks can be in service for years between inspections
- Visual inspection cannot detect internal corrosion or wall thinning — only hydrostatic testing measures actual material condition

## Filling Procedure

1. **Connect cylinder to fill manifold**: Secure the cylinder in the filling station (chain or clamp to prevent rotation). Connect the fill line to the cylinder valve using the correct CGA fitting. Tighten to the specified torque (typically 30-50 N·m for brass CGA fittings). Do not overtighten — brass threads deform and leak.
2. **Pressurize in stages**: For high-pressure fills (>50 bar), pressurize in stages to allow the gas and cylinder to equilibrate thermally. Stage 1: fill to 30 bar, pause 2-3 minutes. Stage 2: fill to 80 bar, pause 2-3 minutes. Stage 3: fill to target pressure. Rapid pressurization generates adiabatic heating (gas temperature rises 30-80°C depending on pressure ratio), which causes the fill pressure to read artificially high. When the cylinder cools to ambient temperature, the pressure drops 5-15% below the reading taken during hot fill.
3. **Monitor fill weight**: Place the cylinder on a calibrated platform scale during filling. Fill to the target gross weight (tare + fill weight), not to a target pressure. Weight is independent of temperature; pressure is not. The fill weight is determined from the gas density at the target fill pressure and 15°C reference temperature, corrected for the gas compressibility factor (Z).
4. **Verify fill pressure**: After the cylinder has cooled to ambient temperature (wait 2-4 hours or quench in a water bath to 15°C), verify the pressure matches the target fill pressure ±2%. If pressure is below specification, add gas. If above, vent to specification.
5. **Leak test**: Apply leak detection solution (soap solution or commercial Snoop) to the valve outlet, valve body-to-cylinder connection, and pressure relief device. Any bubble formation indicates a leak. Tighten the leaking joint or replace the valve. Do not ship a leaking cylinder.
6. **Label and document**: Affix a label showing: gas name, chemical formula, hazard class, UN number, NFPA diamond, cylinder serial number, fill date, fill pressure, and filler's identity. Record the fill in the cylinder tracking log (serial number, gas type, tare weight, gross weight, fill pressure, date, operator initials).

**Strengths:**
- Fill by weight (not pressure) is temperature-independent — eliminates the adiabatic heating error that causes 5-15% pressure overread during rapid filling
- Staged pressurization (30→80→target bar) allows thermal equilibration, reducing the magnitude of adiabatic heating effects

**Weaknesses:**
- Adiabatic heating during rapid fill causes 30-80°C temperature rise — a cylinder filled to rated pressure while hot will be 5-15% underfilled after cooling
- Brass CGA fitting threads deform if overtightened (>50 N·m), creating a permanent leak path that requires valve replacement

## Hydrostatic Retesting

1. Remove the cylinder valve using a valve wrench or powered unscrewing tool.
2. Fill the cylinder completely with water (no air pockets). Water is incompressible — a failure during hydrostatic testing releases a small volume of water, not the violent energy release of compressed gas.
3. Place the water-filled cylinder in a test jacket (a sealed container filled with water, graduated to measure displaced volume). Connect a hydraulic pump to pressurize the cylinder internally.
4. Pressurize the cylinder to the test pressure: 5/3 × (or 10/6 ×) the working pressure. For a 200 bar cylinder, test pressure is 333 bar.
5. Hold test pressure for 30 seconds minimum. Measure total volumetric expansion (the cylinder stretches elastically under pressure, displacing water from the test jacket into a graduated burette).
6. Release pressure. Measure permanent volumetric expansion (the cylinder does not fully return to its original volume — some plastic deformation occurs). Calculate permanent expansion as a percentage of total expansion.
7. **Acceptance criteria**: Permanent expansion must be less than 10% of total expansion. If permanent expansion exceeds 10%, the cylinder has yielded plastically and must be condemned. Also reject if the cylinder bursts during testing (obvious), or if visual inspection reveals wall thinning, corrosion pitting deeper than 1 mm, or cracks.
8. Stamp the test date and tester's mark into the cylinder shoulder. Reinstall the valve and return to service.

**Strengths:**
- Water-filled hydrostatic testing at 5/3× MAWP is inherently safe — water is incompressible, so a cylinder rupture releases minimal stored energy
- Permanent expansion <10% criterion detects material yield before catastrophic failure — a quantitative, objective pass/fail threshold

**Weaknesses:**
- Valve removal and reinstallation for retesting risks cross-threading the neck — the tapered thread is easily damaged if the valve is inserted at an angle
- 5-year retest interval allows fatigue cracks to develop and grow between inspections — cylinders in severe service should be tested more frequently

## Quantitative Parameters

## Cylinder Specifications by Type

| Parameter | Standard Industrial | High-Pressure | Acetylene | Composite (Type III/IV) |
|-----------|-------------------|---------------|-----------|------------------------|
| Working pressure at 15°C | 150-200 bar | 250-300 bar | 15-19 bar (dissolved) | 200-700 bar |
| Test pressure (hydro) | 250-333 bar | 417-500 bar | 25-32 bar | 300-1050 bar |
| Water capacity | 10-50 L | 10-50 L | 10-50 L | 10-100 L |
| Cylinder weight (empty) | 30-80 kg | 40-90 kg | 40-70 kg | 15-40 kg |
| Steel wall thickness | 5-8 mm | 7-12 mm | 5-7 mm | N/A (aluminum liner + carbon fiber) |
| Retest interval | 5-10 years | 5 years | 5 years | 5 years (visual), 3 years (hydro) |
| Service life | 30-50 years | 20-40 years | 20-30 years | 15 years |

## Filling Parameters by Gas Type

| Gas | Fill Pressure (bar) | Fill Temperature (°C) | Compressibility Factor (Z) | Fill Weight (kg per 50 L cylinder) |
|-----|---------------------|----------------------|---------------------------|-----------------------------------|
| Nitrogen (N₂) | 200 | 15 | 1.05 | 11.5 |
| Oxygen (O₂) | 200 | 15 | 1.00 | 13.2 |
| Argon (Ar) | 200 | 15 | 0.96 | 16.8 |
| Hydrogen (H₂) | 200 | 15 | 1.08 | 0.86 |
| Helium (He) | 200 | 15 | 1.09 | 0.80 |
| Carbon dioxide (CO₂) | 57 (liquid phase) | 15 | N/A | 24.0 |
| Acetylene (C₂H₂) | 15 (dissolved in acetone) | 15 | N/A | 6.5 (in acetone) |

## Scaling Notes

- **Bench scale**: Single-cylinder manual fill station with a single-stage compressor. Operator connects cylinder, monitors pressure gauge, and manually shuts off at target pressure. Throughput: 2-5 cylinders per hour. Adequate for small operations filling 10-50 cylinders per day.
- **Pilot scale**: Multi-position fill manifold (4-12 cylinders simultaneously) with a high-pressure booster compressor. Semi-automatic: operator connects cylinders, sets target pressure, and the system fills and shuts off automatically. Throughput: 10-30 cylinders per hour. This is the standard for industrial gas distributors serving local markets.
- **Production scale**: Automated carousel fill system (20-60 positions) with computer-controlled filling by weight, automatic cylinder detection (barcode or RFID), and integrated leak testing. Throughput: 50-200+ cylinders per hour. Required for large gas distribution companies and specialty gas suppliers.
- **Scale bottleneck**: Compressor capacity. A single-stage piston compressor delivers 50-200 L/min at 200 bar. For a 50 L cylinder (10,000 L STP), fill time is 50-200 minutes per cylinder. Multi-position manifolds solve this by filling many cylinders in parallel from a common compressor, but the compressor must be sized to maintain fill rate across all positions. A booster compressor (taking gas from an intermediate-pressure source at 10-30 bar and boosting to 200 bar) reduces the total compression work.
- **Specialty gas filling**: Semiconductor-grade gases require dedicated fill stations with electropolished stainless steel piping, orbital-welded connections, and cylinder preparation including electropolishing, vacuum baking (200°C for 24 hours under vacuum), and moisture verification. Throughput is lower (1-5 cylinders per batch) but purity requirements demand the extra preparation time.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Fill pressure reads high but drops after cooling | Adiabatic heating during rapid fill | Fill more slowly (reduce compressor output), or use staged filling with pauses. Always verify final pressure after cooling. |
| Cylinder valve leaks after filling | Valve packing worn or damaged | Replace valve packing (PTFE rings). Retighten packing gland nut to specified torque. If valve seat is damaged, replace entire valve. |
| Cylinder weight exceeds expected fill weight | Water or oil contamination in cylinder | Drain and dry cylinder before refilling. Check compressor for oil carryover (install coalescing filter on compressor discharge). |
| Cylinder pressure drops during storage | Micro-leak at valve or fitting, or gas permeation (H₂, He) | Perform leak test with soap solution. For H₂/He, some permeation through steel is normal at very long storage times. Re-pressurize before use. |
| Cylinder fails hydrostatic retest (permanent expansion >10%) | Material fatigue from pressure cycling, corrosion thinning, or manufacturing defect | Condemn the cylinder. Drill a hole in the sidewall to prevent reuse. Send to scrap metal recycling. |
| Cross-threading cylinder valve | Valve inserted at angle or forced | Back off immediately. Inspect threads for damage (galling). If threads are damaged, re-tap or chase threads. If severe, condemn cylinder. |
| Acetylene cylinder fills too fast | Exceeding maximum withdrawal/fill rate carries acetone out of cylinder | Limit fill and withdrawal rates to 1/7 of cylinder contents per hour. Acetone loss reduces the stabilizing medium for dissolved acetylene. |
| Frost forming on cylinder during filling | Rapid gas expansion or Joule-Thomson cooling | Reduce fill rate. For CO₂ and some liquefied gases, frost formation during filling is normal; allow the cylinder to warm to ambient before final pressure check. |
| Fill rate drops, compressor runs hot | Discharge valve leaking or inlet filter clogged | Inspect and replace compressor valves; clean or replace inlet filter |
| Cylinder won't reach target pressure | Gas supply depleted or cylinder valve not fully open | Verify gas supply pressure; confirm cylinder valve is fully open; check for restrictions in fill line |
| Cylinder weight off by >2% | Scale calibration drift or residual gas/liquid in cylinder | Recalibrate fill scale; verify cylinder is fully evacuated before filling |
| Valve stem leak detected (bubble test) | Valve packing worn or stem damaged | Replace valve or repack valve stem; never use a cylinder with a leaking valve |
| Cylinder neck threads corroded | Moisture ingress or storage in humid environment | Clean threads with wire brush; inspect for thread damage; reject if thread wear exceeds limits |
| Filled cylinder shows pressure drop over 24h | Micro-leak at valve seat or cylinder wall crack | Re-test with leak detection solution; if wall crack suspected, condemn cylinder immediately |
| Excessive heating during fill | Fill rate too high for gas type (adiabatic heating) | Reduce fill rate; allow cooling between stages; monitor cylinder wall temperature |

## Safety

**Cylinder projectile hazard**: A cylinder with a broken valve is an unguided missile. The thrust from a 50 L cylinder at 200 bar discharging through a broken valve opening (~10 mm diameter) is approximately 1,600 N (equivalent to 160 kg force). The cylinder accelerates to lethal velocity in under 1 meter. Prevention: never drop a cylinder. Always transport with the valve protection cap installed. Secure cylinders to walls, benches, or carts with chains or straps at all times. Never lift a cylinder by the valve.

**Overfilling hazard**: Filling a cylinder beyond its rated pressure (or fill weight for liquefied gases) creates a risk of rupture, especially if the cylinder is subsequently exposed to elevated temperature (fire, direct sunlight, hot process equipment). For liquefied gases (CO₂, propane, ammonia), overfilling is particularly dangerous because the liquid has near-zero compressibility — thermal expansion of the liquid with no gas headspace generates hydrostatic pressure that can exceed the burst pressure. Fill by weight, not by pressure, for all liquefied gases.

**Oxygen-enriched atmosphere during filling**: Filling oxygen cylinders releases O₂-enriched gas through vent lines and purging operations. Oxygen at concentrations above 23.5% dramatically increases the combustibility of all materials — clothing, oil, grease, and organic materials that would merely smolder in normal air burn vigorously in oxygen-enriched atmospheres. Keep oxygen fill stations physically separate from flammable gas fill stations. No oil or grease on any oxygen-contact component. Use oxygen-clean tools.

**Compressor explosion hazard**: Compressing gas generates heat. If flammable gas (H₂, CH₄, C₂H₂) is being compressed and a leak or cross-contamination introduces air into the compressor intake, the mixture of fuel gas + air + compression heat can detonate inside the cylinder. Prevention: purge compressor and fill lines with nitrogen before introducing flammable gas. Monitor compressor discharge temperature (must remain below 140°C for most gases). Install flashback arrestors on acetylene compressors.

**Hearing protection**: High-pressure gas venting through a relief valve or fill line produces noise levels of 100-130 dB — sufficient to cause permanent hearing damage in seconds. Wear hearing protection (earmuffs rated NRR 25+ dB) when operating near filling stations with active venting.

## Quality Control

**Fill verification by weight**: Every filled cylinder must be weighed on a calibrated scale (accuracy ±50 g or better). Compare actual gross weight to expected gross weight (tare + calculated fill weight). Acceptance: ±1% of expected fill weight. Cylinders outside this range are overfilled or underfilled and must be corrected.

**Pressure verification**: After the filled cylinder cools to 15±3°C, verify pressure with a calibrated gauge (accuracy ±0.25% of full scale). Acceptance: fill pressure ±2%. Record the pressure reading and the cylinder temperature at the time of measurement. Correct pressure to the standard 15°C reference temperature using the ideal gas law or the gas-specific pressure-temperature chart.

**Residual moisture in filled cylinder**: For moisture-sensitive gases (electronic grade), sample the gas from the filled cylinder and analyze by electrolytic hygrometer. Acceptance: dew point below -65°C (<5 ppm H₂O) for industrial grade, below -76°C (<1 ppm H₂O) for semiconductor grade. If moisture exceeds specification, the cylinder was inadequately dried before filling — evacuate and repeat the evacuation/purge cycle.

**Gas purity verification**: For semiconductor-grade gases, perform gas chromatography analysis on a sample from each batch (typically 1 cylinder per 10-20 filled). Verify that all specified contaminants are below the guaranteed maximums. For industrial-grade gases, periodic lot sampling (1 cylinder per 100) is sufficient.

**Valve leak test**: After filling, test every cylinder valve for leaks using soap solution or electronic leak detection (thermal conductivity or ultrasonic). Zero tolerance for leaks on filled cylinders — any detected leak requires correction before the cylinder leaves the filling station.

## Variations and Alternatives

**Tube trailers instead of individual cylinders**: For large-volume gas consumers, a tube trailer (a skid of 6-12 large steel tubes, total capacity 3,000-10,000 m³ at STP) replaces hundreds of individual cylinders. Tube trailers are filled at the gas production plant and transported by truck to the point of use. The filling procedure is identical but scaled up. Tube trailers require DOT certification and periodic hydrostatic retesting, same as individual cylinders.

**Composite (Type III/IV) cylinders**: Aluminum or polymer liner wrapped with carbon fiber reinforcement. 30-70% lighter than steel for equivalent capacity. Working pressures up to 700 bar (H₂ vehicle fuel tanks). Higher cost per cylinder but lower transport weight. Limited service life (15 years for Type IV). Type III (metal liner + carbon fiber) is reusable and retestable; Type IV (polymer liner + carbon fiber) has limited retest capability.

**Bulk liquid delivery**: For very high-volume consumers (semiconductor fabs, steel mills), gases are delivered as cryogenic liquids in vacuum-insulated tanker trucks and stored on-site in vacuum-insulated bulk tanks. A 15,000 L liquid nitrogen tank holds approximately 12,000 m³ of gas at STP (equivalent to 1,200 standard cylinders). Vaporizers convert liquid to gas on demand. Requires cryogenic handling capability and specialized storage infrastructure.

**Gas generators (on-site production)**: Pressure Swing Adsorption (PSA) nitrogen generators produce 95-99.99% N₂ from compressed air on-site, eliminating cylinder logistics entirely for nitrogen consumers. Oxygen generators (PSA or VSA) produce 90-95% O₂ from air. On-site generation trades purity (lower than cylinder gas) for convenience (no cylinders, no deliveries).

## Cylinder Valve Types and Applications

| Valve Type | Construction | Gas Service | Flow Rate | Advantages |
|-----------|-------------|------------|-----------|------------|
| Packed valve (CGA standard) | Brass body, PTFE packing around stem | Industrial gases (N₂, Ar, O₂, CO₂) | 0-200 L/min | Inexpensive, robust, widely available |
| Diaphragm valve | Stainless body, welded metal diaphragm | High-purity and corrosive gases (HCl, SiH₄) | 0-50 L/min | Zero contamination from packing, leak-tight |
| Piston valve | Brass body, precision piston seal | High-flow applications | 0-500 L/min | Higher flow than diaphragm type |
| Excess flow valve | Integrated check valve | All gases (safety device) | Shuts off at 200-500% normal flow | Automatically stops flow if line breaks |
| Non-return (check) valve | Spring-loaded disc | All gases (backflow prevention) | 0-200 L/min | Prevents reverse flow into cylinder |

## Cylinder Storage Layout Best Practices

- **Segregation by hazard class**: Store flammable gases (H₂, CH₄, C₂H₂) at least 6 m from oxidizers (O₂, Cl₂). Store toxic gases (CO, H₂S, PH₃) in dedicated ventilated gas cabinets with continuous exhaust and leak detection interlocks.
- **Temperature control**: Store cylinders below 50°C. Direct sunlight on a full cylinder at 200 bar raises internal pressure by 2-3 bar per 10°C temperature increase. If ambient temperature exceeds 40°C, provide shade or indoor storage with ventilation.
- **Upright storage**: All cylinders stored upright with valve protection cap installed. Chain or strap to a wall rack or cylinder cart. Horizontal storage is permitted only for specific gases (some liquefied gas cylinders) and only when the cylinder is designed for horizontal use.
- **FIFO rotation**: Use first-in-first-out inventory rotation. Older cylinders should be used before newer ones to minimize rental charges and reduce the chance of cylinder valve seizing from prolonged storage.
- **Empty cylinder management**: Mark empty cylinders "MT" with a dedicated label. Store empty cylinders in a separate section from full cylinders. Return empty cylinders to the supplier promptly — daily rental charges accrue until the cylinder is returned.

## Cylinder Manufacturing Tolerances

| Dimension | Tolerance | Measurement Method |
|-----------|-----------|-------------------|
| Outside diameter | ±1.5 mm | Tape measure or PI tape |
| Wall thickness | ±0.5 mm | Ultrasonic thickness gauge |
| Neck thread (25 mm ISO taper) | Class A fit | Go/no-go thread gauge |
| Overall length | ±5 mm | Steel tape |
| Hydrostatic expansion (total) | Measured, recorded | Graduated burette in test jacket |
| Burst pressure | >2× working pressure | Destructive test (sample) |

## Cylinder Filling Safety Equipment Checklist

Every cylinder filling station must have the following safety equipment inspected and ready for use:

- **Eye wash station**: Within 10 seconds travel time from any fill position. Flush with water for 15 minutes minimum after chemical exposure. Test weekly.
- **Safety shower**: Within 25 meters of the fill area. Full-body deluge for large-volume chemical exposure. Test monthly (verify flow rate >75 L/min).
- **Fire extinguisher**: Class B (CO₂ or dry chemical) for flammable gas fires. Class D (dry powder) for metal fires (titanium, magnesium cylinder components). Inspect monthly, service annually.
- **Gas detectors**: Combustible gas detector (LEL meter) for flammable gas fill areas. O₂ monitor for areas where asphyxiant gases are handled. Toxic gas detectors specific to gases being filled. Calibrate quarterly.
- **Emergency shutoff**: Remotely operable valve that shuts off gas supply to the entire fill manifold. Accessible from outside the fill room. Test quarterly.
- **Blast barrier**: Minimum 6 mm steel plate or 200 mm concrete block wall between the fill station and the operator. The barrier absorbs the energy of a cylinder or valve failure. Inspect annually for cracks or damage.

## See Also

- [Basic Gas Handling](basic.md) — compressors, regulators, and gas cylinder safety
- [Gas Purification](gas-purification.md) — gas purification before cylinder filling
- [Metal Forming](../machine-tools/forming.md) — cylinder body forming processes
- [Iron & Steel Production](../metals/iron-steel.md) — steel grades for pressure vessel construction
- [Hydrogen & Silane Production](../chemistry/hydrogen-silane.md) — high-pressure hydrogen cylinder requirements
- [Lubricants, Oils & Fluid Mechanics](../chemistry/lubricants.md) — compressor oil selection for gas service
- [Piping Systems](piping-systems.md) — gas distribution infrastructure

[← Back to Gas Handling](index.md)
