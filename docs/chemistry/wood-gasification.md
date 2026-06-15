# Wood Gasification

> **Node ID**: chemistry.petroleum-alternatives.wood-gasification
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: See prerequisites
> **Enables**: [`Petroleum & Alternative Chemistry`](petroleum-alternatives.md)
> **Timeline**: Years 15-40
> **Outputs**: producer_gas, syngas
> **Critical**: No

## Overview

Producer gas generation from biomass via shaft gasifier: partial combustion produces CO+H₂+N₂ mixture (~5-6 MJ/m³). Gas cleaning via water scrubbing, sawdust filter, cyclone. Can power internal combustion engines directly. Powered vehicles during WWII fuel shortages. Bridge technology before natural gas infrastructure.

Wood gasification sits between complete combustion (excess air, products are CO₂ and H₂O) and pyrolysis (no air, products are charcoal, tar, and wood gas). By carefully limiting the air supply, the biomass is partially oxidized, providing the heat to drive endothermic reactions that convert the remaining solid carbon and volatile matter into combustible gases. The resulting producer gas contains carbon monoxide (15-25%), hydrogen (10-20%), methane (1-3%), carbon dioxide (8-12%), and nitrogen (50-55% from the air blast). The nitrogen dilution is the main drawback: it halves the heating value compared to oxygen-blown syngas (CO + H₂, ~11 MJ/m³).

Primary outputs: `producer_gas`, `syngas`. Producer gas (air-blown) fuels internal combustion engines and industrial furnaces. Syngas (oxygen-blown or steam-blown, no nitrogen dilution) serves as a chemical feedstock for Fischer-Tropsch synthesis (methanol, synthetic diesel), ammonia production, and hydrogen extraction.

During World War II, over a million European vehicles ran on wood gas when gasoline was unavailable. A vehicle-mounted gasifier consumed wood chips at roughly 1 kg per 2-3 km of driving, with a 20-40% power penalty compared to gasoline. The technology works. It is dirty, labor-intensive, and requires constant attention, but it converts biomass into mechanical power with no petroleum.

The gas composition determines the engine tuning. Producer gas burns slower than gasoline, requiring 5-15 degrees more ignition advance. The lower heating value means larger fuel-air volumes must pass through the engine, requiring larger carburetor jets or mixer adjustments. The hydrogen component (10-20%) in the gas raises the flame speed and can cause engine knocking if the compression ratio is too high. Engines converted to producer gas typically run at compression ratios below 8:1 to avoid detonation.

## Prerequisites

### Materials

- Wood chips or chunks (hardwood preferred, 10-20% moisture content, uniform size 3-8 cm)
- Charcoal (alternative fuel: cleaner gas, simpler gasifier, but requires separate charcoal production)
- Steel plate and pipe for gasifier body, fire tube, and gas piping
- Refractory lining (firebrick or castable refractory) for the combustion and reduction zones

### Equipment

- Welded steel gasifier vessel (updraft, downdraft, or fluidized bed design)
- Gas cleaning train: cyclone separator, wet scrubber (water spray tower), fabric or sawdust filter
- Blower or fan for draft (natural draft works for updraft gasifiers but limits output)
- Internal combustion engine or burner modified for producer gas (larger jets, advanced timing)

### Knowledge

- Gasifier zone physics: drying, pyrolysis, combustion, and reduction zones and their temperature profiles
- Tar formation and cracking: understanding that tar condensation in engines causes carbon buildup and failure, and that downdraft gasifiers crack tars by passing gas through a hot charcoal bed at 1000°C+
- Air-fuel ratio control: too much air burns the gas to CO₂; too little air quenches the gasifier
- Gas composition analysis: using Orsat apparatus or portable gas analyzer to measure CO, H₂, CH₄, CO₂ proportions

### Infrastructure

- Covered fuel storage with good air circulation for natural wood drying (season 6-12 months to reach 15-20% moisture)
- Concrete pad for gasifier installation with drainage for scrubber water
- Chimney or flare stack for gas flaring during startup and shutdown
- Access to welding and metalworking for gasifier construction and repair

## Process Description

A downdraft (Imbert) gasifier is the most common design for engine fuel because it produces the cleanest gas. Air and fuel move downward together through four zones:

**Drying zone (top, 50-100°C)**: Fresh wood enters at the top. Heat from rising gases (in an updraft design) or from the zones below evaporates residual moisture. Wood above 25% moisture quenches the reduction zone and produces excessive tar. Fuel must be pre-dried.

**Pyrolysis zone (200-500°C)**: The dried wood thermally decomposes, releasing volatile organic compounds (tars, creosote, light hydrocarbons) and leaving a charcoal residue. In a downdraft gasifier, these volatile tars are carried downward into the hot zones rather than escaping directly into the product gas.

**Combustion zone (1000-1200°C)**: A limited air supply is introduced at the throat (the narrowest section). Part of the charcoal burns, providing the heat that drives all the endothermic reactions. The primary reactions are C + O₂ → CO₂ (complete combustion) and 2C + O₂ → 2CO (partial combustion). The combustion zone is deliberately restricted to concentrate heat in a small volume.

**Reduction zone (800-1000°C)**: Below the combustion zone, hot gases pass through a deep bed of glowing charcoal. Two key endothermic reactions convert combustion products to fuel gas: the Boudouard reaction (CO₂ + C → 2CO, absorbs heat) and the water-gas reaction (H₂O + C → CO + H₂, absorbs heat). The gas exits the reduction zone at 600-800°C and passes into the gas cleaning system.

An updraft gasifier reverses the air flow direction. Air enters from the bottom; fuel enters from the top and moves down by gravity. The gas exits from the top, passing through the drying and pyrolysis zones on its way out. This means tar vapors from pyrolysis are carried directly into the product gas without passing through a hot cracking zone. Updraft gasifiers produce gas with tar content 10-50 g/m³, compared to 0.1-1 g/m³ for downdraft designs. Updraft gas is suitable for direct combustion (boilers, kilns) but requires extensive cleaning for engine use.

Gas cleaning is essential for any engine application. Raw producer gas carries three contaminant classes: tars (condensable organic compounds that deposit as carbon in engine intake systems), particulates (ash, char fines, and soot that abrade cylinder walls), and moisture (reduces heating value and promotes corrosion). The cleaning train typically starts with a cyclone separator (centrifugal force throws particulates outward to the wall, where they fall to a collection bin). Next, a wet scrubber (the gas bubbles upward through a water spray or packed bed, where water dissolves tars and captures fine particles). Finally, a fabric or sawdust filter removes the last traces of particulates. For tar elimination rather than mere capture, a catalytic cracker (hot dolomite or nickel catalyst at 800-900°C) decomposes tars into simpler non-condensable gases (CO, H₂, CH₄), converting the problem contaminant into additional fuel.

### Step-by-Step Procedure

1. Prepare fuel: cut wood to uniform chunks (3-8 cm for downdraft gasifiers, 5-15 cm for updraft). Dry to below 20% moisture (seasoned wood or kiln-dried). Sort out oversized pieces and fines (fines block airflow; oversized pieces bridge and create voids).
2. Charge the gasifier: fill the hopper with prepared fuel. For a cold start, place kindling and a small amount of charcoal in the combustion zone to establish the fire quickly.
3. Ignite and establish the gasifier: light the kindling through the ignition port. Turn on the draft fan (or open the natural draft damper). White smoke (steam and volatiles) appears first. After 5-10 minutes, the smoke clears and the gas becomes combustible (test by flaring at the flare stack). Never start a gasifier with the engine connected; flare until gas quality stabilizes.
4. Connect to the load (engine or burner) once gas is consistently flammable. Monitor gasifier outlet temperature: 400-600°C indicates good reduction zone performance. Below 300°C suggests the reduction zone is too cool (incomplete cracking, high tar).
5. Operate by maintaining the fuel level (refill hopper before it empties completely; an empty hopper lets air into the gas system, creating an explosion risk). Adjust air supply to maintain even combustion. Shake the grate periodically to clear ash buildup.
6. Shut down by closing the air supply and disconnecting the engine. Allow the gasifier to cool with the lid open. Never seal a hot gasifier; residual char can continue producing CO, pressurizing the vessel. Flare any remaining gas during cooldown.
7. After shutdown and cooling, clean the grate and remove accumulated ash. Inspect the throat and reduction zone for clinker formation (ash that has melted and fused into hard lumps). Clinkers indicate excessive temperature in the combustion zone, possibly from too much air or low-ash-point fuel. Remove clinkers mechanically before the next run; they block gas flow and create hot spots that damage the fire tube.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Gasification temperature (combustion zone) | 1000-1200°C | Below 900°C, tar cracking is incomplete |
| Reduction zone temperature | 800-1000°C | Below 700°C, CO₂ reduction to CO stalls |
| Air/fuel ratio | 0.25-0.35 kg air per kg wood (dry basis) | Too much air: gas becomes CO₂-rich, heating value drops. Too little: gasifier quenches. |
| Fuel moisture content | Below 20% (wet basis) | Above 25%, steam quenches the reduction zone and tar production spikes |
| Gas heating value (producer gas) | 4.5-6.5 MJ/Nm³ | Compared to 35-40 MJ/Nm³ for natural gas |
| Gas heating value (syngas, O₂-blown) | 10-14 MJ/Nm³ | No nitrogen dilution |
| Engine power derating on producer gas | 20-40% vs. gasoline | Lower heating value and slower burn rate. Advance ignition timing 5-15° to compensate. |

## Safety Considerations

Carbon monoxide is the primary killer in wood gasification. Producer gas contains 15-25% CO, a colorless, odorless gas that binds to hemoglobin 200-300 times more strongly than oxygen. At 200 ppm in air, CO causes headache and dizziness after 2-3 hours. At 1000 ppm, it causes unconsciousness within an hour. At 10,000 ppm (1%), it is lethal within minutes. A gasifier operating in an enclosed space without ventilation is a death trap.

- **CO poisoning**: The insidious hazard. Workers may not realize they are being exposed until symptoms appear. Never operate a gasifier indoors without forced ventilation and a CO detector at breathing height. If someone complains of headache, dizziness, or nausea near a gasifier, evacuate them to fresh air immediately. CO symptoms improve rapidly with fresh air but reappear if exposure resumes.
- **Gas explosion**: Producer gas is flammable at 15-70% concentration in air. Gasifier startup and shutdown are the highest risk periods, when air and gas mix in the system. Always flare gas during startup before connecting to the engine. Never open the fuel hopper while the gasifier is under positive pressure (the gas-air mixture can flash back).
- **Burns**: The gasifier shell reaches 200-400°C on the outside. The combustion zone is above 1000°C. Ash removal involves handling hot material. Use long-handled tools for grate shaking and ash removal.
- **Scrubber water contamination**: The wet scrubber produces contaminated water containing dissolved tars, phenols, and ammonia. This water is toxic to aquatic life. Do not discharge to waterways. Recirculate scrubber water and replace when it becomes too contaminated to absorb effectively.
- **Charcoal dust and ash**: Dry ash from the grate and charcoal fines are respiratory irritants. The ash is alkaline (contains K₂O, CaO) and can cause eye and skin irritation. Wet down ash before removing it from the gasifier to suppress dust.

### Personal Protective Equipment

- Leather gloves (welding gauntlets) for fuel handling, grate shaking, and ash removal
- Safety glasses with side shields (gasifier blowbacks spray hot ash and sparks)
- Flame-resistant clothing (no synthetic fabrics that melt onto skin)
- CO detector badge clipped to the collar when working near an operating gasifier
- Hearing protection if operating an engine driven by producer gas (engine noise plus blower)

### Emergency Procedures

- **CO exposure symptoms (headache, dizziness, nausea, confusion)**: Move the affected person to fresh air immediately. Do not let them walk unaided (collapse risk). If unconscious, call for medical help and begin rescue breathing. Recovery is usually rapid with fresh air, but severe exposure requires oxygen therapy. Anyone who has lost consciousness from CO exposure should receive medical evaluation, as delayed neurological effects can appear hours later.
- **Gasifier flashback**: A backfire through the ignition port or fuel hopper is alarming but usually self-extinguishing. Close the air supply. Do not stand over the hopper during startup. Keep the ignition port closed after lighting.
- **Gas leak fire**: Shut off the air supply to the gasifier (starves the reaction). Isolate the gasifier from the engine with a shutoff valve. Do not attempt to extinguish a gas fire at the leak point; let it burn until the gasifier is isolated and the gas burns off.
- **Scrubber water spill**: Contain with sand or earth. Do not flush into drainage. Collect contaminated material for proper disposal. The water contains phenols and dissolved organics that contaminate groundwater.

## Quality Control

### Acceptance Criteria

- **Producer Gas**: CO content 15-25%, H₂ content 10-20%, CH₄ content 1-3%, CO₂ content 8-12%. Tar content below 50 mg/Nm³ for engine use (downdraft with cleaning). Particulate matter below 10 mg/Nm³. Heating value 4.5-6.5 MJ/Nm³.
- **Syngas (O₂-blown)**: CO + H₂ content above 80%. CO₂ below 10%. CH₄ below 3%. Tar below 10 mg/Nm³. Heating value 10-14 MJ/Nm³.

### Testing Methods

- **Gas composition analysis**: Orsat apparatus (absorbs CO₂ in KOH, O₂ in alkaline pyrogallol, CO in cuprous chloride solution) for basic field analysis. Portable gas analyzer (electrochemical or infrared sensors) for continuous monitoring. Gas chromatography for detailed laboratory analysis.
- **Tar content**: Draw a measured volume of gas through an isopropanol-filled impinger train. Evaporate the solvent and weigh the tar residue. Target: below 50 mg/Nm³ for engine fuel.
- **Heating value calculation**: From gas composition: HHV = (12.7 × %CO) + (12.8 × %H₂) + (40.0 × %CH₄) MJ/Nm³. A quick field check: if the gas flares steadily with a blue-orange flame, it is above 4 MJ/m³ and usable.
- **Calorimetric test (burn test)**: Burn a measured volume of gas in a calibrated burner and measure temperature rise in a known mass of water. Direct measurement of heating value without gas analysis.

### Sampling Protocol

- Continuous gas temperature monitoring at the reduction zone outlet (thermocouple): 400-600°C indicates healthy operation
- Gas composition check every 2-4 hours using Orsat or portable analyzer during steady operation
- Tar content measurement at startup and after any operating condition change
- Visual inspection of gas color: clear gas is low-tar; white or yellowish gas indicates high moisture or tar carryover
- Engine performance monitoring: if engine power drops more than 10% from baseline, check gas quality first
- Weekly scrubber water replacement or recharge. Measure pH and dissolved organic content to determine when scrubber water is spent (pH drops below 7 or water turns dark brown with visible tar film)

## Scaling Notes

- **Small stationary (5-20 kW engine)**: Downdraft gasifier, 20-50 cm diameter fire tube, produces 20-50 m³ gas per hour. Consumes 5-15 kg wood per hour. Suitable for farm machinery, small generators, water pumps. One person can build and operate. Most WWII vehicle gasifiers were in this range.
- **Medium stationary (50-200 kW engine)**: Larger downdraft or cross-draft gasifier, 50-100 cm fire tube, produces 100-500 m³ gas per hour. Requires automatic fuel feeding (auger or conveyor) and mechanical grate shaking. Full gas cleaning train (cyclone, wet scrubber, fabric filter). Two to three operators.
- **Industrial (1-10 MW thermal)**: Fluidized bed gasifier or large updraft design. Handles varied fuels (wood waste, agricultural residue, municipal waste). Produces gas for boilers, kilns, or power generation. Requires continuous fuel handling, ash removal, and gas cleaning. A staff of 5-10 per shift.

The key scaling insight: downdraft gasifiers scale poorly above about 200 kW because the throat diameter needed for larger throughput makes it hard to maintain the concentrated high-temperature zone that cracks tars. Fluidized bed gasifiers solve this by suspending fuel in an upward air stream, achieving uniform temperature, but they require blowers, control systems, and more complex gas cleaning.

At any scale, the fuel preparation requirement is a constant labor burden. A 20 kW gasifier consumes 5-15 kg of wood per hour. A 200 kW gasifier consumes 50-150 kg per hour. All of this fuel must be cut to size and dried before use. For continuous operation, a week's fuel reserve for a 200 kW gasifier is roughly 10-20 tonnes of prepared, dried wood. This is not a casual undertaking. Fuel handling logistics often determine the practical maximum gasifier size more than the gasifier technology itself.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Gas won't ignite (no flare) | Gasifier too cold (reduction zone below 600°C); air supply insufficient; fuel too wet (steam quenching the reaction) | Pre-heat with more kindling and charcoal. Increase air supply. Check fuel moisture (target below 20%). Re-light and establish a hotter combustion zone before connecting load. |
| High tar content in gas (engine carbon buildup) | Downdraft throat too cool to crack tars; reduction zone too shallow; fuel too wet | Increase air supply to raise throat temperature above 1000°C. Ensure reduction zone has at least 20 cm of hot charcoal bed. Dry fuel to below 15% moisture. |
| Gasifier "bridging" (fuel stops feeding) | Oversized fuel pieces jamming in the hopper or throat; wet fuel sticking together; ash buildup blocking the throat | Use uniformly sized fuel (3-8 cm). Dry fuel before use. Poke the fuel bed with a poker rod through the access port. Clean ash from the throat area. |
| Gas heating value too low (CO below 15%) | Excess air (air/fuel ratio too high); reduction zone too cool; or insufficient charcoal depth | Reduce air supply. Add more fuel to build up the charcoal bed. Check for air leaks in the gasifier shell (uncontrolled air entry oxidizes product gas to CO₂). |
| Engine knocking or backfiring on producer gas | Gas contains oxygen (air leak in gas piping); gas temperature too high (hot gas is less dense, engine runs lean); or ignition timing wrong for producer gas | Check all gas pipe joints for leaks (paint with soap solution, look for bubbles). Install a gas cooler (water jacket or air cooler) to bring gas below 40°C before the engine. Advance ignition timing 5-15 degrees from gasoline settings (producer gas burns slower). |
| Excessive ash buildup blocking grate | High-ash fuel (bark, leaves, agricultural waste); grate not shaken frequently enough; or ash melting and forming clinkers at high temperature | Shake grate every 15-30 minutes during operation. Use cleaner wood (debarked). If clinkers form, reduce combustion zone temperature by increasing air (counterintuitively, excess air cools the zone by diluting the combustion). |

## Variations and Alternatives

- **Charcoal gasification**: Uses charcoal instead of raw wood as fuel. Produces much cleaner gas (charcoal has no volatile matter, so no tar) with simpler gasifier design. The tradeoff is that charcoal production loses roughly half the wood's energy content as waste heat and byproduct gases during the pyrolysis step. Charcoal gasifiers powered many WWII vehicles because the cleaner gas reduced engine maintenance.
- **Updraft gasifier**: Air enters at the bottom, gas exits at the top. Higher tar output (10-50 g/m³) because volatile tars from pyrolysis bypass the hot zone. Simpler design, more tolerant of fuel size and moisture variation. Best for direct combustion applications (boilers, kilns) where tar condensation in the burner is less problematic.
- **Fluidized bed gasifier**: Air (or O₂/steam) flows upward through a bed of sand or inert particles at sufficient velocity to suspend the bed in a fluid-like state. Biomass feeds into the fluidized bed. Excellent temperature uniformity and fuel flexibility. Can gasify wood waste, agricultural residues, and even municipal solid waste. Requires blowers and more complex controls. Used at industrial scale (1-50 MW).
- **Steam gasification**: Steam instead of air as the gasifying agent. Produces syngas without nitrogen dilution (heating value 10-14 MJ/m³). Endothermic: requires external heat input (combustion of part of the fuel in a separate chamber, or external heating). Higher H₂ content in the product gas (up to 50%) due to the water-gas shift reaction (CO + H₂O → CO₂ + H₂).
- **Anaerobic digestion**: Biological decomposition of organic matter in the absence of oxygen, producing biogas (60-70% CH₄, 30-40% CO₂, heating value 20-25 MJ/m³). Completely different process: operates at 35-55°C with bacteria, not at 1000°C with fire. Suitable for wet, low-lignin biomass (manure, food waste, sewage sludge) that gasifiers cannot handle. Lower throughput and longer residence time but much lower temperature.

- **Producer gas to liquid fuels (Fischer-Tropsch)**: Syngas (CO + H₂) from oxygen-blown gasification can be catalytically converted to liquid hydrocarbons (synthetic diesel, waxes, alcohols) over iron or cobalt catalysts at 200-350°C and 20-30 bar. This is the route from biomass to drop-in liquid fuels, but it requires clean syngas with precise H₂:CO ratio (2:1 for Fischer-Tropsch), oxygen-blown gasification (no nitrogen dilution), and a catalyst preparation capability. Several steps beyond simple producer gas generation.

## References

- [Petroleum & Alternative Chemistry](petroleum-alternatives.md) — parent capability
- [Chemistry Domain](./index.md) — domain overview and related capabilities
- [Petroleum & Alternative Chemistry](petroleum-alternatives.md) — downstream capability

### Material Handling

Fuel preparation is the most labor-intensive part of wood gasification. Wood must be cut to uniform size (3-8 cm chunks for downdraft, 5-15 cm for updraft) and dried to below 20% moisture. Green (fresh-cut) wood can be 40-60% moisture and produces three times more tar than dry wood. Air drying takes 6-12 months; kiln drying takes days but requires fuel. Store prepared fuel under cover with ventilation to allow continued drying while protecting from rain.

Charcoal fuel for charcoal gasifiers must be kept dry (charcoal absorbs moisture readily) and sized to 2-5 cm lumps. Fines (below 1 cm) block airflow. Charcoal dust is a respiratory irritant; handle with a dust mask.

Scrubber water becomes toxic over time as it accumulates dissolved tars, phenols, ammonia, and PAHs (polycyclic aromatic hydrocarbons). Recirculate scrubber water until it becomes dark brown and loses effectiveness (typically 2-5 days of operation). Dispose of spent scrubber water by evaporation in a shallow pond (organics degrade in sunlight) or by incineration in the gasifier's combustion zone. Do not discharge to waterways or septic systems.

Ash from the gasifier grate is a mixture of mineral oxides (CaO, K₂O, SiO₂) and unburned carbon. Wood ash can be returned to soil as a liming agent and potassium source. Ash with high unburned carbon content (above 10%) indicates the gasifier is not processing fuel completely; consider reducing fuel feed rate or increasing residence time.

The choice between wood and charcoal as gasifier fuel affects the entire system design. Wood is the direct feedstock, available from any forest. Charcoal must be produced first (pyrolysis in a kiln), losing roughly half the original wood's energy as waste heat and byproduct gases. But charcoal gasifiers are simpler, produce much cleaner gas, and are more tolerant of operating variations. For stationary power where gas quality matters (engine operation), charcoal is the better fuel despite the extra processing step. For direct combustion applications (boilers, kilns), wood gasification with an updraft gasifier is the simpler and more efficient choice because the tars in the gas burn along with the combustible components.

A wood gasifier combined with an internal combustion engine provides a biomass-to-mechanical-power pathway that requires no petroleum. For stationary power generation, a 20 kW gasifier-engine-generator set consuming 10-15 kg of wood per hour can provide continuous electrical power for a small workshop, farm, or village, using locally grown wood. The energy conversion efficiency from wood to electricity is 15-20% (gasifier converts wood to gas at 60-70% efficiency, engine-generator converts gas to electricity at 25-30%). This is competitive with steam engines at similar scale and far simpler than building a steam plant from scratch.

The downdraft gasifier design is more demanding to build than the updraft because the throat (the narrow constriction where tars are cracked) must withstand temperatures above 1000°C while maintaining a consistent cross-section. The throat is typically a refractory-lined cylinder 15-25 cm in diameter for a 20-50 kW unit. Too narrow and it plugs with fuel; too wide and the gas velocity drops below what is needed to maintain the hot reduction zone. Getting the throat diameter right for a given fuel type and power output requires either careful calculation or empirical adjustment (start slightly too large and add refractory inserts to reduce the diameter until performance peaks).

The gasifier fire tube (the section enclosing the combustion and reduction zones) experiences the most severe thermal and chemical stress. Temperatures reach 1000-1200°C in an oxidizing and reducing atmosphere alternately. Mild steel fire tubes last 1,000-3,000 operating hours before burning through. Stainless steel (310 or 316 grade) extends this to 5,000-10,000 hours. Ceramic-lined fire tubes (refractory castable or firebrick) last indefinitely but add thermal mass that slows startup. For a balance of cost and durability, a stainless steel fire tube with internal refractory coating is the typical choice for a gasifier expected to operate 2,000-4,000 hours per year.

Producer gas cannot be stored or transported economically over long distances. The low heating value (5-6 MJ/m³) means that the volume of gas needed for meaningful energy delivery is enormous. A 200 kW engine requires roughly 60-80 m³ of gas per hour, which must be produced and consumed in real time. This is why gasifiers are always located at or near the point of gas use. The one exception is medium-energy syngas from oxygen-blown gasification (10-14 MJ/m³), which can be piped moderate distances in dedicated pipelines. But oxygen-blown gasification requires an air separation plant, adding another layer of complexity.

The WWII experience with wood gas vehicles provides a wealth of practical design data. The most common design was the Imbert downdraft gasifier, produced in hundreds of thousands of units across Europe. These units had a fire tube diameter of 10-25 cm (depending on engine displacement), a throat constriction to 60-80% of fire tube diameter, and a reduction zone charcoal bed depth of 15-30 cm. The gas cleaning system was typically a cyclone, a water-filled scrubber, and a fabric filter. The entire gasifier assembly weighed 60-120 kg and mounted on a bracket behind the car or on a small trailer. Modern recreations of these designs are built by enthusiasts and tested regularly, confirming that the basic technology is sound and reproducible.

The Imbert gasifier design has been extensively documented in wartime manuals and modern rebuilding guides. The key dimensional relationships are: fire tube diameter determines maximum throughput (roughly 100 cm² of fire tube cross-section per 10 kW of engine power), throat diameter is 60-80% of fire tube diameter, and reduction zone height is 1-2 times the throat diameter. These proportions have been validated across hundreds of different builds and can be scaled with reasonable confidence for new designs targeting different power outputs.

---
*Part of the [Bootciv Tech Tree](../index.md) · [Chemistry](./index.md) · [All Domains](../index.md)*

