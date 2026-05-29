# Basic Gas Handling

> **Node ID**: gas-handling.basic
> **Domain**: [Gas Handling](./index.md)
> **Dependencies**: None (root capability)
> **Enables**: [`chemistry.air-separation`](../chemistry/air-separation.md), [`chemistry.hydrogen-silane`](../chemistry/hydrogen-silane.md), [`silicon.purification`](../silicon/purification.md)
> **Timeline**: Years 20-35
> **Outputs**: gas_handling, compressed_gases, purified_gases
> **Critical**: No — basic gas handling supports many processes but individual processes can use simpler alternatives

## Infrastructure

**Piping, valves, pumps**:
- **Pipes**: Cast iron (water, dilute alkalis), lead (H₂SO₄ <80%), copper (organic solvents, water), ceramic (acids at high temperature), glass (laboratory scale). Steel for steam and high-pressure gas.
- **Valves**: Bronze gate valves, cast iron plug valves, glass stopcocks (laboratory). PTFE-packed valves for HF service.
- **Pumps**: Centrifugal pumps (motor-driven impeller — most common for liquids), diaphragm pumps (for corrosive/acids), piston pumps (high pressure), gear pumps (viscous liquids). Machine Tools machining produces the precision parts.

**Strengths:**
- PTFE-packed valves handle HF service — one of the few materials compatible with hydrofluoric acid at all concentrations
- Diaphragm pumps isolate the process fluid from the drive mechanism, providing zero-contamination transfer for corrosive and ultra-pure liquids

**Weaknesses:**
- Cast iron piping corrodes rapidly in acid service, and lead piping for H₂SO₄ is heavy and toxic — no single material covers all chemical services
- Reciprocating piston compressors produce pulsating flow that requires pulsation dampeners for sensitive downstream processes

**Gas handling**:
- **Compression**: Reciprocating piston compressors (steam or motor driven), 1-10 bar for general use, 100-300 bar for gas cylinders. Multi-stage with intercoolers for high pressures.
- **Storage**: Gas holders (water-sealed bell-type for low pressure), steel cylinders (high pressure, 150-200 bar). Liquified gases in insulated tanks.
- **Purification**: Drying (CaCl₂, silica gel, molecular sieves), scrubbing (water, NaOH solution for acid gases), catalytic getters (for trace impurity removal).

## Pipe Fitting Techniques

- **Threaded connections (NPT — National Pipe Thread Tapered)**: Taper of 1:16 (3/4 inch per foot). Threads seal by deformation of mating surfaces as fitting is tightened. Wrap male threads with PTFE (Teflon) tape — 2-3 wraps clockwise, or apply pipe dope (linseed oil-based paste with fillers). NPT seals are not truly gas-tight at high pressure without sealant. Torque to 1-2 turns past hand-tight. Maximum reliable pressure: ~20 bar for steel, ~10 bar for brass. For higher pressures, use flanged or welded connections.
- **Flanged connections**: Flat-faced or raised-face flanges bolted together with gasket between. Bolt pattern (number and circle diameter) standardized by pressure class (e.g., 4 bolts for 1" Class 150, 8 bolts for 4" Class 150). Tighten bolts in crisscross pattern to seat gasket evenly. Allow re-torque after first thermal cycle.

**Strengths:**
- NPT threaded connections are universal, low-cost, and require only PTFE tape or pipe dope to seal — suitable for pressures up to 20 bar (steel) with simple hand tools
- Flanged connections allow disassembly for maintenance and accommodate thermal cycling with re-torque

**Weaknesses:**
- NPT seals are not truly gas-tight at high pressure without sealant — micro-leakage through thread roots is inherent to the tapered thread design
- Flanged connections are bulky and heavy compared to welded or compression fittings, and the gasket is a periodic replacement item

## Gasket Material Selection

| Material | Service | Temperature Range | Notes |
|----------|---------|-------------------|-------|
| **[Copper](../glossary/copper.md)** | High-temperature steam, oxygen | up to 600°C | Soft metal, seals by plastic deformation. Used in high-pressure and high-temp flanges. |
| **[Viton (FKM)](../glossary/viton-fkm.md)** | Aggressive chemicals, fuel gases | -20°C to 200°C | Fluorocarbon elastomer. Resists most organics, acids, chlorine. Swells in ketones. |
| **[PTFE (Teflon)](../glossary/ptfe-teflon.md)** | High-purity gas, corrosive service | -200°C to 260°C | Chemically inert, non-outgassing. Poor creep resistance — use filled PTFE (glass or carbon) for bolted flanges. |
| **[Compressed fiber](../glossary/compressed-fiber.md)** | Steam, water, inert gases | up to 400°C | Traditional gasket material (asbestos historically, now aramid or glass fiber). Good for utility services. |
| **[Rubber (NBR/EPDM)](../glossary/rubber-nbrepdm.md)** | Air, water, inert gases at moderate temp | -30°C to 120°C | Cheap, forgiving. Not for hydrocarbons (NBR) or steam (EPDM preferred). |

## Compressor Types

- **Reciprocating (piston)**: Pressure ratio 3-5 per stage. For >5 bar discharge, use multi-stage with intercoolers between stages (cool gas back to near-ambient before next compression stage — reduces work and prevents excessive discharge temperature). Lubricated cylinders for most gases; non-lubricated (PTFE piston rings) for purity-critical service.
- **Diaphragm**: Gas separated from drive mechanism by flexible metal diaphragm. Zero oil contamination — essential for ultra-pure gases (semiconductor-grade H₂, O₂, Ar). Pressure ratio 3-10 per stage. Lower flow rates than piston type.
- **Rotary screw**: Two intermeshing helical rotors compress gas continuously. No pulsation — smooth flow. Pressure ratio 3-15 in single stage. Oil-flooded version for general industry; oil-free (dry screw) for process gas. Higher power consumption than piston at same pressure.

**Strengths:**
- Diaphragm compressors provide zero oil contamination — essential for semiconductor-grade gases where even ppm-level oil is unacceptable
- Rotary screw compressors deliver smooth, pulsation-free flow and high pressure ratios (3-15) in a single stage

**Weaknesses:**
- Reciprocating piston compressors require multi-stage intercooling above 5 bar discharge — each stage adds cost, piping, and a heat exchanger
- Oil-free (dry screw) rotary compressors consume 15-25% more power than oil-flooded versions due to the lack of oil sealing between rotors

## Gas Cylinder Filling

- **Pressure ratings**: Standard industrial cylinders: 150-200 bar at 15°C. High-pressure cylinders: 250-300 bar. Cylinder stamped with test pressure, date, and serial number.
- **Hydrostatic testing**: Pressurize cylinder with water to 5/3 of working pressure every 5-10 years. Measure permanent expansion (<10% of total expansion). Reject if exceeds limit or if visual inspection finds corrosion, dents, or fire damage.
- **Valve types**: CGA (Compressed Gas Association) standard connections — each gas type has a unique thread/pin pattern to prevent cross-connection (e.g., CGA 580 for inert gases, CGA 350 for flammable gases, CGA 540 for oxygen). Valve outlet threads are right-hand for non-fuel gases and left-hand for fuel gases as an additional safety check.
- **Filling procedure**: Weigh cylinder to determine empty weight (tare). Fill by weight or pressure, accounting for gas compressibility factor. Never exceed stamped fill pressure.

**Strengths:**
- CGA standard connections have unique thread/pin patterns per gas family — physical impossibility of cross-connecting incompatible gases
- Hydrostatic testing at 5/3 working pressure with permanent expansion measurement (<10% limit) catches cylinders with hidden wall thinning before failure

**Weaknesses:**
- Hydrostatic retesting every 5-10 years removes cylinders from service and requires specialized test equipment
- Fill by weight requires a calibrated scale at each fill station; fill by pressure alone risks overfilling due to temperature-dependent gas density

## Safety & Hazards

**Compressed gas cylinder safety**:
- **Securing cylinders**: Cylinders must be chained or strapped to a wall, bench, or cylinder cart at all times — both in storage and in use. An unsecured cylinder knocked over can snap the valve off, turning the cylinder into an unguided projectile (a 50 kg cylinder at 200 bar contains enough energy to penetrate a concrete wall). Use two chains: one at upper third, one at lower third of cylinder body.
- **Pressure regulator use**: Always use the correct regulator for the gas type (CGA connection matching). Never force a regulator onto a mismatched fitting. Open cylinder valve slowly — sudden pressurization can damage the regulator diaphragm or cause adiabatic compression heating (fire hazard with oxygen). Stand to the side of the regulator when opening the cylinder valve, not in front of the gauge face (glasses can blow out). Never use oil or grease on oxygen fittings — spontaneous ignition. Release adjusting screw (close regulator) before opening cylinder valve, then set downstream pressure.
- **Ventilation for toxic gases**: Gases like CO, H₂S, NOx, and chlorine require use in ventilated enclosures or gas cabinets with continuous exhaust. Gas detection alarms for the specific gas must be installed. Scrubbers or absorbers on exhaust for toxic gas cylinders. Emergency shutoff valves accessible from outside the work area.

**Asphyxiation risk from inert gases**: Nitrogen, argon, helium, and CO₂ are inert to chemical interaction but displace oxygen in confined spaces. A nitrogen leak in an unventilated room can reduce O₂ from 21% to below 10% without any sensation of breathlessness (the human breathing reflex is triggered by CO₂ buildup, not O₂ depletion — inert gas asphyxiation causes euphoria, confusion, and unconsciousness with no warning signs). At <6% O₂, loss of consciousness in seconds, death in minutes. O₂ monitoring alarms required in confined spaces and rooms with large inert gas storage. Never enter a confined space where inert gas may be present without atmospheric testing.

**Gas identification and labeling**: Every cylinder must be clearly labeled with contents, hazard class, and NFPA diamond. Color-coding alone is unreliable — different suppliers use different color schemes. Never assume cylinder contents from color; always read the label. Store incompatible gases separately (flammables from oxidizers, toxics from everything). Empty cylinders should be marked "MT" and returned to supplier — never mix gases by refilling with a different product.

**Strengths:**
- Two-chain securing protocol (upper third + lower third) prevents both tip-over and valve snap-off — the dominant fatal cylinder accident type
- Inert gas asphyxiation risk is entirely preventable with continuous O₂ monitoring at the 19.5% alarm threshold — the hazard is well-understood and mitigation is straightforward

**Weaknesses:**
- Inert gas asphyxiation produces no physiological warning — the breathing reflex is triggered by CO₂, not O₂ depletion, so victims feel euphoric before losing consciousness
- Color-coding is supplier-specific and unreliable — content misidentification from color alone has caused fatal accidents

## Gas Cylinder Specifications

**Cylinder construction**:
- **Material**: Seamless steel (manganese steel or chromium-molybdenum alloy). Drawn from a single steel disc, no welded seams (seamless construction eliminates the weakest point). Outer surface painted with identifying color and labeled. Inner surface clean and dry.
- **Working pressure**: 150-200 bar at 15°C (standard industrial). High-pressure cylinders: 250-300 bar for hydrogen and helium (these gases have high compressibility). Cylinder expands slightly under pressure — this is normal elastic deformation.
- **Water capacity**: 10-50 L typical (larger cylinders for high-consumption applications, smaller for laboratory use). A 50 L cylinder at 200 bar holds ~10,000 L of gas at atmospheric pressure (STP volume = water capacity × fill pressure).
- **Valve types**: Diaphragm valve for high-purity and reactive gases (metal diaphragm isolates gas from packing, eliminates contamination). Packed valve for industrial gases (cheaper, adequate for non-critical applications). Needle valve for fine flow control on regulator outlet.

**Strengths:**
- Seamless construction from a single steel disc eliminates welded seams — the most common failure point in pressure vessels
- 50 L cylinder at 200 bar stores ~10,000 L STP of gas, providing a compact and portable high-density energy storage medium

**Weaknesses:**
- Seamless steel cylinders weigh 30-80 kg empty — heavy to move and handle, requiring purpose-built carts
- Diaphragm valves for high-purity service cost 5-10× more than packed valves, justified only for semiconductor-grade gases

## Pressure Regulators

**Single-stage regulator**:
- **Construction**: Brass body (for inert and non-corrosive gases) or stainless steel (for corrosive gases like HCl, Cl₂, H₂S). High-pressure inlet gauge (0-300 bar), low-pressure delivery gauge (0-10 bar typical). Adjustable spring-loaded diaphragm controls outlet pressure.
- **Behavior**: Delivery pressure rises as cylinder pressure drops (the "decaying inlet characteristic"). At full cylinder, set delivery to 3 bar. When cylinder drops to 30 bar, delivery may creep to 4-5 bar. For processes requiring constant delivery pressure, this is a problem requiring frequent manual adjustment or a two-stage regulator.
- **CGA connections**: Each gas family has a unique CGA inlet fitting. CGA 580 (inert: N₂, Ar, He), CGA 350 (flammable: H₂, CH₄), CGA 540 (O₂ — right-hand thread, brass, no oil), CGA 330 (toxic/corrosive: HCl, Cl₂). The different thread patterns prevent connecting the wrong regulator to the wrong cylinder.

**Two-stage regulator**:
- **Principle**: Two pressure-reduction stages in series. First stage reduces cylinder pressure to a fixed intermediate pressure (~15-30 bar). Second stage reduces intermediate to the adjustable delivery pressure (0-10 bar). The intermediate stage acts as a buffer, isolating delivery pressure from cylinder pressure changes.
- **Result**: Constant delivery pressure across the full cylinder pressure range. The preferred choice for analytical instruments, mass flow controllers, and any process requiring stable gas pressure.

**Strengths:**
- Two-stage regulator maintains constant delivery pressure across the full cylinder range (200→10 bar inlet), eliminating the need for manual readjustment
- CGA connection system with unique thread patterns per gas family physically prevents cross-connection of incompatible gases

**Weaknesses:**
- Single-stage regulator's decaying inlet characteristic causes delivery pressure to creep up as cylinder empties — unacceptable for analytical instruments without frequent manual correction
- Two-stage regulators cost 2-3× more than single-stage and have more internal components that can fail

## Gas Distribution Hardware

**Tubing selection**:
- **Copper**: Soft-annealed copper tubing (6-12 mm OD, 1 mm wall) for most gases at <10 bar. Flared or compression fittings. Easy to bend and form. Not suitable for ammonia (forms complex), acetylene (forms explosive copper acetylide), or ultra-high-purity applications (copper particles shed from inner surface).
- **Stainless steel 316L**: For corrosive gases (HCl, Cl₂), high-purity semiconductor gases, and high-pressure applications (>10 bar). Electropolished interior for ultra-high-purity service (smooth surface prevents particle generation and gas adsorption). Welded or orbital-welded connections for permanent installations. Compression fittings for removable connections.
- **PTFE (Teflon)**: Flexible tubing for low-pressure (<3 bar) connections. Chemically inert to nearly all gases. Permeable to some gases (He, H₂ diffuse through PTFE walls). Used for short flexible connections between regulators and equipment.

**Fitting types**:
- **[Compression fittings](../glossary/compression-fittings.md)** (Swagelok-type): Three-piece design: body, front ferrule (stainless or brass), back ferrule. Tighten nut → ferrules compress onto tube outer surface, creating a metal-to-metal seal. Removable and re-sealable. Tube must be fully inserted and nut tightened to the specified number of turns past finger-tight (typically 1-1/4 turns for new fittings). Do not mix ferrules from different manufacturers.
- **Flanged connections**: For tubing >25 mm diameter. Flat-faced or raised-face flanges bolted together with gasket between. Standardized by pressure class (Class 150, 300, 600, etc.). Bolt torque in crisscross pattern for even gasket compression. Allow re-torque after first thermal cycle.

**Strengths:**
- Stainless steel 316L with electropolished interior provides both corrosion resistance and ultra-smooth surfaces (<0.25 μm Ra) that prevent particle generation and gas adsorption
- Compression fittings (Swagelok-type) create metal-to-metal seals that are removable and re-sealable — allow system modification without cutting and rewelding

**Weaknesses:**
- Copper tubing cannot be used for ammonia (forms complex), acetylene (forms explosive copper acetylide), or ultra-high-purity service (particles shed from inner surface)
- PTFE tubing is permeable to He and H₂ — small molecules diffuse through the wall, making it unsuitable for containment of these gases over long periods

## Gas Detection Systems

**Combustible gas detection**:
- **Catalytic bead (pellistor) sensor**: Two platinum wire coils embedded in ceramic beads, one coated with a catalyst (active bead) and one without (reference). Both heated to ~500°C. Combustible gas oxidizes on the active bead, raising its temperature and resistance. The resistance difference between active and reference beads is proportional to gas concentration. Measures 0-100% LEL (lower explosive limit). Responds to all combustible gases but with varying sensitivity. Poisoned by silicones, lead, and halogenated compounds.

**Oxygen detection**:
- **Paramagnetic cell**: Oxygen is strongly paramagnetic (attracted to a magnetic field). A dumbbell suspended in a magnetic field deflects proportional to the O₂ concentration in the sample gas. Measures 0-25% O₂. Accurate, non-depleting, but mechanically delicate. Used for calibration and fixed installations.
- **Electrochemical cell**: Oxygen diffuses through a membrane and reacts at an electrode, generating a current proportional to concentration. Compact, inexpensive. Cell life 1-2 years (consumed by the reaction). Measures 0-25% O₂. Used for portable monitors and confined space entry.

**Toxic gas detection**:
- **[Electrochemical cells](../glossary/electrochemical-cells.md)** (gas-specific): Each cell is designed for one target gas. H₂S cell: 0-50 ppm or 0-100 ppm range, alarm at 10 ppm (TWA) and 15 ppm (STEL). CO cell: 0-500 ppm, alarm at 25 ppm (TWA) and 100 ppm (STEL). Cl₂ cell: 0-10 ppm. Cell life 1-3 years. Cross-sensitivity exists (H₂S sensors may respond to SO₂, etc.) — review manufacturer data.
- **Gas cabinet ventilation**: Enclose toxic gas cylinders in a ventilated gas cabinet. Face velocity 100-200 fpm (0.5-1.0 m/s) at the cabinet access opening. Exhaust to outside, never recirculate. Install leak detection interlock: if the gas detector alarms, automatic shutoff valve closes the cylinder, ventilation runs at maximum, and audible/visual alarms activate. Emergency shutoff accessible from outside the cabinet.

**Strengths:**
- Catalytic bead sensors respond to all combustible gases with a single device — broad-spectrum coverage for mixed-hazard environments
- Electrochemical cells are compact and inexpensive ($50-200), enabling deployment of multiple sensors throughout a facility

**Weaknesses:**
- Catalytic bead sensors are poisoned by silicones, lead, and halogenated compounds — one exposure to silicone sealant fumes can permanently disable the sensor
- Electrochemical cells have 1-3 year service life and cross-sensitivity issues (H₂S sensors respond to SO₂) — false alarms and missed detections are both possible

## Gas Purification and Drying

**Drying agents (desiccants)**:
- **Calcium chloride (CaCl₂)**: Inexpensive, absorbs water to form hydrated salts. Capacity: ~30% of its weight in water. Non-regenerable (discard when saturated). Used for rough drying of gases. Leaves traces of CaCl₂ dust in the gas stream, so a particulate filter downstream is needed.
- **Silica gel**: Amorphous SiO₂ with enormous internal surface area (~700 m²/g). Absorbs water by physical adsorption (capillary condensation in pores). Capacity: ~30-40% by weight. Regenerable by heating to 150-200°C for 2-4 hours (drives off adsorbed water). Indicator silica gel contains cobalt chloride (blue when dry, pink when saturated). Non-reactive with most gases.
- **Molecular sieves (zeolites)**: Crystalline aluminosilicates with uniform pore sizes (3Å, 4Å, 5Å, 10Å). Adsorb molecules smaller than the pore diameter while excluding larger molecules. 3Å sieves adsorb water but exclude all other molecules (ideal for drying gases). 4Å sieves adsorb water, CO₂, H₂S, and small hydrocarbons. Regenerable by heating to 250-350°C or by vacuum. Capacity: 15-25% by weight. Extremely effective: can dry gases to <1 ppm H₂O.
- **Phosphorus pentoxide (P₂O₅)**: Chemical desiccant that reacts with water to form phosphoric acid. Ultimate drying capacity: can reduce water vapor to <0.00001 mg/L (the most effective common desiccant). Not regenerable. Corrosive and hazardous (reacts violently with water in bulk). Used as a final polishing desiccant after silica gel or molecular sieve.

**Scrubbing systems**:
- **Water scrubber**: Packed column (ceramic or plastic packing) with water flowing countercurrent to the gas stream. Water absorbs water-soluble gases (HCl, HF, NH₃, SO₂). Simple, continuous operation. Scrubber water becomes acidic or basic and must be neutralized before disposal.
- **Caustic scrubber**: NaOH solution (5-20%) in packed column. Removes acid gases: Cl₂ (forms NaOCl + NaCl), HCl (forms NaCl), H₂S (forms Na₂S), SO₂ (forms Na₂SO₃). Essential for exhaust gas treatment before venting to atmosphere. Monitor scrubber solution pH (replace when pH drops below 10).
- **Activated carbon adsorber**: Bed of granular activated carbon (GAC) through which gas flows. Carbon adsorbs organic vapors, oil mist, and odors by physical adsorption on its enormous surface area (~1,000 m²/g). Used for: removing trace organic contaminants from gas streams, protecting compressor intakes, purging solvent vapors from exhaust. Saturates over time (replace or regenerate by steam desorption at 120-150°C).

**Strengths:**
- Molecular sieves (zeolites) dry gases to <1 ppm H₂O with uniform pore sizes that exclude all but the smallest molecules — the most effective regenerable desiccant available
- Caustic scrubbers convert toxic acid gases (Cl₂, HCl, H₂S) to non-toxic salts (NaOCl, NaCl, Na₂S), enabling safe atmospheric discharge

**Weaknesses:**
- Calcium chloride is non-regenerable and releases dust into the gas stream — requires a downstream particulate filter, adding complexity
- Activated carbon saturates unpredictably depending on contaminant load — breakthrough occurs suddenly, releasing accumulated contaminants downstream

## Specialized Gas Handling

**[Acetylene handling](../glossary/acetylene-handling.md)** (exceptionally dangerous gas):
- **Properties**: Acetylene (C₂H₂) is unstable and can decompose explosively without oxygen at pressures above ~2 bar. It cannot be stored in plain steel cylinders like other gases.
- **Cylinder design**: Acetylene cylinders are filled with a porous material (calcium silicate or diatomaceous earth) soaked with acetone. Acetylene dissolves in the acetone (acetone dissolves ~25× its own volume of acetylene at 15 bar). The porous matrix prevents any decomposition from propagating through the cylinder. Maximum withdrawal rate: 1/7 of cylinder contents per hour (faster withdrawal carries acetone out of the cylinder, depleting the stabilizer).
- **Piping restrictions**: Never use copper or copper alloys (>65% Cu) for acetylene service (forms explosive copper acetylide). Use steel or brass (copper <65%). Never use unalloyed silver solder. Maximum pressure in distribution lines: 1.5 bar.

**Oxygen service cleanliness**:
- **Contamination hazard**: Any organic material (oil, grease, dust, lint) in contact with compressed oxygen can ignite spontaneously. Oxygen at high pressure lowers the autoignition temperature of organic materials dramatically. A greasy fingerprint on an oxygen fitting can cause a fire.
- **Cleaning procedure**: Wash all oxygen-contact surfaces in hot alkaline detergent solution. Rinse with deionized water. Blow dry with oil-free nitrogen or clean air. Inspect visually (no visible oil, grease, or particles). Test with UV light (hydrocarbon residues fluoresce). Assemble with clean tools (dedicated oxygen-clean tools, never used on other services).
- **Material restrictions**: No oil, grease, or hydrocarbon lubricants on any oxygen-contact component. Use PTFE-based lubricants only where lubrication is required (valve seats). Gaskets: PTFE or virgin PTFE-coated materials only. Never use Viton (fluorocarbon elastomer is acceptable for O₂ at moderate pressures but not at >200 bar).

**Strengths:**
- Acetylene cylinder design (porous matrix + acetone solvent) allows safe storage of a gas that would otherwise decompose explosively above 2 bar — elegant chemical engineering solution
- Oxygen-clean procedures (alkaline wash, DI water rinse, UV inspection) are straightforward and detect hydrocarbon residues that would be invisible to the naked eye

**Weaknesses:**
- Acetylene withdrawal rate limited to 1/7 of cylinder contents per hour — faster withdrawal carries acetone out, depleting the stabilizer and risking decomposition
- Oxygen service contamination hazard is invisible — a greasy fingerprint on an O₂ fitting can cause spontaneous ignition, and there is no warning before ignition occurs

## Ventilation for Gas Storage and Use

**Gas cabinet design**: Toxic, corrosive, and pyrophoric gas cylinders must be stored and used in ventilated enclosures (gas cabinets). The cabinet is a sheet metal enclosure with a clear viewing window, an access door, and an exhaust duct connection. The exhaust system maintains a face velocity of 100-200 feet per minute (0.5-1.0 m/s) at the cabinet access opening, ensuring that any leak inside the cabinet is captured and exhausted outside the building rather than entering the workspace. The exhaust duct runs directly to the building exterior, with no recirculation. A flow sensor in the exhaust duct triggers an alarm if face velocity drops below the minimum threshold.

**Leak detection interlock**: The gas cabinet includes a gas-specific detector mounted inside the enclosure. If the detector measures gas concentration above the alarm threshold (typically 0.5× the TLV-TWA for that gas), the interlock system automatically closes the cylinder's pneumatically actuated shutoff valve, switches the exhaust to maximum flow, and activates audible and visual alarms both at the cabinet and at the building's central alarm panel. Personnel are not permitted to open the cabinet door while the alarm is active.

**Laboratory ventilation**: For non-toxic gases used at bench scale (N₂, Ar, compressed air), a general laboratory ventilation rate of 6-12 air changes per hour provides adequate dilution. For toxic gases (CO, H₂S, Cl₂, NH₃), a chemical fume hood with 80-120 fpm face velocity is the minimum requirement. Fume hoods are tested annually with a smoke pencil or vaneometer to verify face velocity across the entire sash opening.

**Strengths:**
- Gas cabinet with 100-200 fpm face velocity captures any leak inside the enclosure and exhausts it outside — the operator's breathing zone is never exposed
- Leak detection interlock automatically closes the cylinder valve on alarm, stopping the leak without requiring human intervention

**Weaknesses:**
- Exhaust system is a single point of failure — if the exhaust fan stops, the cabinet loses containment and toxic gas enters the workspace
- Fume hood face velocity testing is annual; a sash adjustment or equipment relocation between tests can create low-velocity zones that leak contaminants

## Inert Gas Purging

**Purpose**: Before introducing a flammable or reactive gas into a piping system, vessel, or enclosure, the air (and its oxygen content) must be displaced with an inert gas (nitrogen or argon) to prevent forming a flammable mixture. Similarly, before opening a vessel that contained a toxic gas, purge with inert gas to displace the toxic atmosphere before introducing air for personnel entry.

**Purge by dilution**: Flow inert gas through the vessel at a steady rate. The oxygen concentration decays exponentially as the incoming inert gas dilutes the remaining air. After 3-5 volume changes (where one volume change equals flowing a volume of inert gas equal to the vessel volume), the oxygen concentration drops below 1%. After 7-10 volume changes, O₂ is below 0.1%. The exact number depends on mixing efficiency. Poor mixing (dead zones, internal baffles) extends the required purge time. Internal baffles and obstructions create stagnant pockets that dilute slowly. Where possible, orient purge inlet and outlet on opposite ends of the vessel, and use a diffuser on the inlet to promote turbulent mixing.

**Verification**: Before introducing flammable gas, measure O₂ concentration with a calibrated oxygen monitor. The reading must be below 1% (or below the specific threshold for the gas mixture in question, often 0.5% for hydrogen service). Before personnel entry into a confined space after inert gas purging, verify O₂ is between 19.5% and 23.5% (normal air range) with a calibrated four-gas monitor. Never trust a purge without measurement verification.

**Hot work precautions**: Before welding, cutting, or brazing on or near a vessel or piping system that contained flammable gas, purge the system with nitrogen until combustible gas concentration is below 1% LEL AND oxygen is below 1%. Both conditions must be met. Use a combustible gas detector to verify. Continuous monitoring during hot work is required, with a fire watch posted for 30 minutes after work completion.

**Strengths:**
- Dilution purging is simple and requires only an inert gas source — after 3-5 volume changes, O₂ drops below 1% without complex equipment
- Measurement verification (O₂ monitor before flammable gas introduction, combustible gas detector before hot work) provides objective go/no-go criteria

**Weaknesses:**
- Poor mixing from internal baffles and dead zones extends purge time beyond the theoretical 3-5 volume changes — stagnant pockets may retain O₂ well after bulk concentration reads safe
- Hot work requires BOTH combustible gas <1% LEL AND O₂ <1% — checking only one condition has caused re-ignition explosions

## Piping System Design

**Pressure drop calculation**: Gas flowing through a pipe loses pressure due to friction against the pipe wall. The Darcy-Weisbach equation gives the pressure drop: ΔP = f × (L/D) × (ρv²/2), where f is the friction factor (from Moody chart, depends on pipe roughness and Reynolds number), L is pipe length, D is pipe inside diameter, ρ is gas density, and v is gas velocity. For long distribution lines, pressure drop limits the flow rate. Size the pipe so that the pressure drop from source to point-of-use is less than 10% of the supply pressure.

**Velocity limits**: Keep gas velocity below 10 m/s in general service piping. Higher velocities cause excessive pressure drop, noise, vibration, and erosion at bends and fittings. For oxygen service, the velocity limit is stricter (typically 8 m/s for steel pipe, 15 m/s for copper or Monel) because high-velocity oxygen impingement on particles or contaminants can cause ignition in the pipe. For dirty or particulate-laden gas streams, lower velocities (<5 m/s) prevent erosion.

**Drain points and dead legs**: Install drain points (drip legs or low-point drains with valves) at all low spots in the piping system. Condensate and liquid water collect at these low points. Without drains, liquid accumulates and restricts gas flow, or worse, slugs of liquid travel downstream and damage equipment (liquid hammer). Avoid dead legs (sections of pipe closed at one end, with no through-flow). Dead legs trap stagnant gas, collect condensate, and create corrosion pockets. Where a branch connection is necessary, keep the dead leg length less than 6× the pipe diameter.

**Material selection by gas type**: Inert gases (N₂, Ar, He, CO₂): carbon steel or copper, standard fittings. Corrosive gases (HCl, Cl₂, H₂S): stainless steel 316L with welded or orbital-welded joints, PTFE gaskets. Ultra-high-purity gases (semiconductor grade): electropolished stainless steel 316L with orbital-welded joints and VCR-type fittings, to prevent particle generation and contamination. Fuel gases (H₂, CH₄, C₂H₂): steel or stainless steel. Never use copper or copper alloys for acetylene. Oxygen: steel, copper, or Monel, with oxygen-clean components.

**Strengths:**
- Darcy-Weisbach equation provides predictable pressure drop calculation, enabling pipe sizing to keep losses below 10% of supply pressure
- Material selection scheme (carbon steel for inert, 316L for corrosive, electropolished 316L for UHP) matches cost to application requirements

**Weaknesses:**
- Oxygen velocity limit of 8 m/s in steel pipe constrains flow rates — high-demand O₂ systems require larger-diameter piping than equivalent inert gas services
- Dead legs (<6× pipe diameter) trap stagnant gas and collect condensate, creating corrosion pockets that are difficult to inspect

## Pressure Testing and Commissioning

**Hydrostatic testing**: Before placing a new piping system in gas service, pressure-test it with water (hydrostatic test) at 1.5× the maximum allowable working pressure (MAWP). Water is incompressible, so a failure during hydrostatic testing releases a small volume of water rather than the violent energy release of compressed gas. Hold test pressure for 30 minutes minimum while inspecting all joints for leaks (visually and by wiping joints with a dry cloth and checking for moisture). Drain and dry the system thoroughly after testing. For systems that cannot tolerate residual moisture (instrument air, high-purity gas), purge with dry nitrogen after draining.

**Pneumatic testing**: When hydrostatic testing is impractical (system cannot be dried, or weight of water would overload supports), a pneumatic test with air or nitrogen is permitted. The test pressure is lower (typically 1.1× MAWP) due to the stored energy hazard. A pneumatic failure releases the full compressed gas volume, creating a blast wave. Personnel must be excluded from the test area during pressurization. The energy stored in a pneumatic test is proportional to the system volume and the square of the pressure. For large, high-pressure systems, hydrostatic testing is strongly preferred for safety.

**Leak testing after commissioning**: After pressure testing and before introducing process gas, perform a sensitive leak test on the completed system. For flammable gas systems, pressurize with nitrogen at operating pressure and check all joints with soap solution (bubble test). For higher sensitivity, pressurize with a helium-nitrogen mixture and use a helium sniffer probe to check each joint (sensitivity ~10⁻⁶ atm·cc/s). Document all leak test results. Any detected leak, no matter how small, must be repaired before the system is placed in service with hazardous gas.

**Strengths:**
- Hydrostatic testing with water at 1.5× MAWP is inherently safe — water is incompressible, so a failure releases minimal stored energy
- Helium leak testing at 10⁻⁶ atm·cc/s sensitivity finds leaks too small for soap bubble or pressure decay methods — essential for toxic gas systems

**Weaknesses:**
- Pneumatic testing at 1.1× MAWP stores enormous energy in compressed gas — a failure creates a blast wave, requiring personnel exclusion from the entire test area
- Hydrostatic testing leaves residual moisture that must be purged with dry nitrogen before introducing moisture-sensitive gases — adds time and dry gas cost

## Emergency Procedures

**Gas leak response**: If a gas leak is detected (odor, alarm, or visible damage to piping), the first priority is to stop the flow. Close the nearest upstream valve. For cylinder leaks where the valve cannot be closed (valve packing failure, damaged valve seat), evacuate the area and summon the fire department or hazmat team. Do not attempt to cap or plug a leaking cylinder. For toxic gas leaks, evacuate the area immediately and do not re-enter until the gas detector reads zero and the space has been verified safe with a calibrated monitor. For flammable gas leaks, eliminate all ignition sources (no switches, no phones, no static-generating activity) and ventilate the area before attempting to close any valve.

**Cylinder valve emergencies**: If a cylinder valve fails to close (stripped threads, broken stem), and the gas is non-toxic and non-flammable (e.g., N₂, Ar), the cylinder can be moved to a well-ventilated outdoor area and allowed to empty slowly. For toxic or flammable gas cylinders with failed valves, evacuate the building and contact emergency services. Do not attempt to transport a leaking toxic gas cylinder. Place an inverted bucket or plastic bag over the valve to contain and direct the leak upward, if this can be done safely.

**Regulator fire**: If a regulator catches fire (most common with oxygen service due to contamination), do not attempt to close the cylinder valve. Shut off the gas supply at a remote location (a valve further upstream) if possible. Let the cylinder burn itself out while cooling adjacent cylinders with water spray to prevent pressure relief activation. After the fire is extinguished, treat all equipment in the area as contaminated and submit for forensic analysis before reuse.

**Strengths:**
- Remote shutoff valves accessible from outside the work area enable emergency gas isolation without exposing personnel to the leak source
- Cylinder valve emergencies with non-toxic gases can be resolved by moving the cylinder outdoors — the simplest possible mitigation

**Weaknesses:**
- For toxic gas cylinder valve failures, the only safe response is building evacuation and emergency services — no safe DIY mitigation exists
- Regulator fires in oxygen service cannot be extinguished at the cylinder valve — the operator must reach a remote shutoff while the cylinder burns

## Gas Storage and Inventory Management

**Cylinder storage areas**: Store gas cylinders in a designated, well-ventilated area, protected from weather and direct sunlight (sun heating raises cylinder pressure). Store full and empty cylinders separately, clearly labeled. Flammable gas storage must be at least 20 feet from oxidizer storage, or separated by a fire-rated barrier (minimum 1/2 hour rating). Toxic gas cylinders in ventilated gas cabinets or dedicated gas rooms with continuous exhaust and leak detection. Maximum cylinder quantities per storage area are defined by fire code (typically 2,500 ft³ of flammable gas or 6,000 ft³ of inert gas in unsprinklered spaces).

**Inventory tracking**: Maintain a log of every cylinder on site: gas type, cylinder serial number, date received, fill pressure at receipt, location, date placed in service, and date returned empty. This log enables tracking of gas consumption rates, identification of slow leaks (cylinder pressure dropping faster than usage accounts for), and compliance with regulatory reporting requirements for toxic and hazardous gases. Cylinder rental charges accrue daily, so prompt return of empty cylinders reduces cost.

**Strengths:**
- Inventory log detects slow leaks by tracking pressure decay against consumption — catches problems before cylinders empty unexpectedly
- Daily cylinder rental charges create a financial incentive for prompt return and efficient inventory management

**Weaknesses:**
- Manual inventory tracking is labor-intensive and error-prone for facilities with hundreds of cylinders — barcode or RFID systems reduce errors but add cost
- 20-foot separation requirement between flammable and oxidizer storage limits layout options for facilities with diverse gas inventories

**Cylinder handling and transport**: Move cylinders only with a purpose-built hand cart or cylinder trolley, never rolled or dragged. Cap the valve protection cap during transport (the metal cap protects the valve from impact). Never lift a cylinder by the valve or cap. Secure the cylinder to the cart with a chain or strap. For loading docks and elevators, cylinders are transported upright and secured. In laboratory settings, cylinders must be supported by a bench clamp, wall bracket, or floor stand at all times, not merely stood upright against a bench where they can be knocked over.

## Flow Measurement and Control

**Mass flow controllers (MFCs)**: For process gas delivery in semiconductor and chemical manufacturing, the gas flow rate must be precisely controlled. An MFC measures the mass flow rate (not volume flow rate, which varies with temperature and pressure) using a thermal sensor. A portion of the gas stream passes through a capillary tube with a heated element and two temperature sensors upstream and downstream. The temperature difference between the two sensors is proportional to the mass flow. A control valve (solenoid or piezoelectric) adjusts the gas flow to match the setpoint. Accuracy: ±1% of full scale. Range: typically 10-100% of full scale rating. MFCs are calibrated for a specific gas; using the wrong gas requires a correction factor based on the ratio of specific heats and thermal conductivities.

**Rotameters (variable-area flow meters)**: A simple, low-cost device for visual indication of volumetric gas flow. A float (stainless steel, glass, or plastic ball) rises in a tapered glass tube as gas flows upward. The float reaches an equilibrium position where the drag force from the gas equals the float weight. The position on the calibrated scale indicates flow rate. Accuracy: ±5-10% of full scale. Requires vertical installation. Calibrated for a specific gas at a specific temperature and pressure; correction factors needed for other conditions. No external power required. Useful for purge flow indication and non-critical process flows where ±10% accuracy is acceptable.

**Calibration of gas measurement instruments**: Mass flow controllers and rotameters are calibrated against a primary standard (a volumetric displacement calibrator or a gravimetric calibrator that measures the mass of gas delivered over a timed interval). Calibration is performed at the operating temperature and pressure, or correction factors are applied. Recalibration interval: 6-12 months for process-critical MFCs, 12 months for general-purpose instruments. Calibration records document the as-found and as-left readings at multiple points across the range (typically 0%, 25%, 50%, 75%, 100% of full scale). An MFC whose calibration has drifted more than ±2% from the reference standard requires adjustment or replacement.

**Strengths:**
- MFCs measure mass flow (not volume) with ±1% accuracy — independent of temperature and pressure variations that affect volumetric measurements
- Rotameters require no external power and provide instant visual flow indication — ideal for purge monitoring and non-critical applications

**Weaknesses:**
- MFCs are gas-specific — using the wrong gas without applying correction factors introduces errors of 20-50%
- Rotameters at ±5-10% accuracy are unsuitable for process-critical dosing; recalibration of MFCs every 6-12 months adds maintenance burden

## Emergency Response for Gas Incidents

**Leaking cylinder**: If a cylinder valve leaks and cannot be tightened, move the cylinder outdoors or to a well-ventilated area. For toxic gases, evacuate the building and call emergency services. Attempt to stop the leak by tightening the valve packing nut (the nut around the valve stem) with a wrench. If the leak is from the cylinder body (rare, indicates corrosion or damage), the cylinder cannot be repaired. Isolate it, vent contents safely through a scrubber if possible, and return to supplier.

**Cylinder fire**: If gas from a leaking cylinder ignites, do NOT attempt to extinguish the flame while the gas is still flowing (extinguishing the flame creates an unignited gas cloud that may re-ignite explosively). Instead, shut off the cylinder valve to stop gas flow. If the valve cannot be reached, cool the cylinder with water spray from a safe distance (prevents pressure buildup from heating) and evacuate the area.

**Asphyxiation rescue**: If a person is found unconscious in an area where inert gas asphyxiation is suspected, do NOT enter without supplied-air respirator. Multiple fatalities occur when untrained rescuers rush in without protection. Ventilate the area first. Remove the victim to fresh air. Begin rescue breathing or CPR if breathing has stopped. Continue until medical help arrives or the victim recovers.

**Toxic gas exposure first aid**: For inhaled toxic gases (CO, H₂S, Cl₂), move the victim to fresh air immediately. For hydrogen sulfide, the rotten-egg odor disappears at concentrations above 100 ppm due to olfactory fatigue, so the absence of smell does not mean the gas is gone. Administer 100% oxygen if available. For chlorine gas exposure, flush eyes with copious water for 15 minutes. Seek medical attention for any toxic gas exposure, even if symptoms appear mild initially (some effects are delayed).

**Strengths:**
- Asphyxiation rescue protocol (do NOT enter without supplied-air respirator) prevents the common pattern of multiple fatalities from would-be rescuers
- Cylinder fire protocol (do NOT extinguish while gas flows) prevents creation of unignited explosive gas clouds that re-ignite catastrophically

**Weaknesses:**
- H₂S olfactory fatigue above 100 ppm eliminates the natural warning — workers may believe the gas has dissipated when concentration is actually lethal
- Toxic gas exposure effects can be delayed (CO binds hemoglobin with symptoms worsening over hours) — victims who seem fine may deteriorate rapidly

## Gas Storage Layout

The physical arrangement of gas storage affects both safety and operational efficiency:

- **Segregation by hazard class**: Store flammable gases (H₂, CH₄, C₂H₂) at least 6 m from oxidizers (O₂, Cl₂) and 15 m from toxic gases. Incompatible gases must not share the same cabinet or manifold. Use physical barriers (concrete block walls) between hazard classes for quantities exceeding 1000 cubic feet.
- **Outdoor storage preferred**: Gas cylinders are best stored outdoors under a roof or canopy (protection from rain and direct sunlight) with chain-link fencing for security. Ventilation is unlimited. Temperature stays below 50°C in most climates, avoiding pressure buildup from heating. Indoor storage requires mechanical ventilation at 1 CFM per square foot of floor area.
- **Cylinder racks**: Store cylinders upright in purpose-built racks with individual chain restraints. Organize by gas type with clear signage at eye level showing contents, hazard class, and NFPA diamond. Keep empty and full cylinders in separate sections. Position the most frequently used cylinders closest to the distribution panel for easy changeover.

**Strengths:**
- Outdoor storage under canopy provides unlimited ventilation and avoids temperature-induced pressure buildup above 50°C
- Hazard class segregation (6 m flammable-to-oxidizer, 15 m flammable-to-toxic) with concrete barriers prevents cascading incidents

**Weaknesses:**
- Outdoor storage exposes cylinders to weather and corrosion — painted surfaces degrade requiring periodic repaint
- 6 m and 15 m separation distances consume significant facility footprint for diverse gas inventories


## Limitations

- **Leak detection difficulty**: Small gas leaks (especially H₂ and He, which have tiny molecules) are difficult to detect by smell or visual inspection. Hydrogen leaks are invisible and odorless — a hydrogen flame is nearly invisible in daylight. Leak detection requires specialized equipment (hydrogen sensors, helium mass spectrometers). In complex distribution systems, locating the exact leak point can take hours.
- **Material compatibility constraints**: No single material handles all gases. Copper acetylene welding requires that acetylene never contact copper (>65% Cu alloys) — it forms explosive copper acetylide. Oxygen service requires degreased, oil-free components — any hydrocarbon residue in an O₂ system is an explosion hazard. Fluorine attacks most metals. Each gas system demands its own materials analysis.
- **Pressure rating limits**: Gas cylinder pressures (150-300 bar) require heavy-walled steel or composite-wound vessels. Distribution piping at lower pressures (1-15 bar) uses copper, stainless steel, or PTFE. Every component in the chain must be rated for the maximum possible pressure, including relief valve set points. A single under-rated component can fail catastrophically.
- **Gas cylinder logistics**: High-pressure gas cylinders are heavy (30-80 kg each), require secure upright storage, periodic hydrostatic retesting (every 5-10 years), and careful handling. Large-volume gas users install bulk tanks (liquid O₂, N₂, Ar) to avoid cylinder logistics, but bulk tanks require concrete pads, vaporizers, and DOT permitting.

**Strengths:**
- No single material handles all gases — this is a feature, not a bug: material-gas incompatibility (copper/acetylene, oil/oxygen) provides inherent chemical barriers against dangerous cross-connections
- Bulk tanks replace hundreds of cylinder deliveries with monthly tanker truck visits, reducing handling labor and injury risk

**Weaknesses:**
- H₂ and He leak detection requires specialized equipment (hydrogen sensors, helium mass spectrometers) — these small-molecule gases are invisible, odorless, and undetectable by smell
- Gas cylinder logistics (30-80 kg each, 5-10 year retest cycle) create ongoing operational burden that bulk tanks eliminate only with significant capital investment

## See Also

- **[Vacuum Systems](vacuum.md)**: Low-pressure gas handling and vacuum pump technology
- **[Dopant and Etch Gases](../chemistry/dopant-etch-gases.md)**: Specialty gas distribution for semiconductor manufacturing
- **[Hydrogen and Silane](../chemistry/hydrogen-silane.md)**: Pyrophoric gas handling and safety
- **[SEM Tech](../chemistry/sem-tech.md)**: Chlorine and hydrogen gas handling in chlor-alkali cells
- **[Welding](../machine-tools/joining.md)**: Shielding gas (Ar, CO₂, He) distribution for welding


[← Back to Gas Handling](index.md)
