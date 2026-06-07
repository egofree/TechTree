# Catalytic Cracking & Conversion

> **Node ID**: petroleum.refining.cracking
> **Domain**: [Petroleum](./index.md)
> **Dependencies**: See prerequisites
> **Enables**: [`Petroleum Refining`](refining.md), [`Atmospheric & Vacuum Distillation`](distillation.md)
> **Timeline**: Years 25-40
> **Outputs**: gasoline, diesel, jet_fuel, propylene_from_fcc, btx_aromatics, refinery_hydrogen
> **Critical**: No

## Overview

FCC converts heavy gas oil to gasoline (45-60% yield) and propylene using zeolite Y catalyst at 500-550°C. Hydrocracking converts VGO to diesel and jet fuel at 350-430°C and 80-200 bar with hydrogen. Reforming produces BTX aromatics and hydrogen from naphtha at 490-530°C over Pt-Re catalyst.

Fluid catalytic cracking is the workhorse conversion unit in a refinery. Hot regenerated catalyst particles contact atomized feedstock in the riser reactor, where the catalytic reaction cracks large hydrocarbon molecules into smaller, more valuable ones in seconds. Spent catalyst, coated with coke, is separated by cyclones and regenerated in a separate vessel by burning off the coke with air. The continuous catalyst circulation between reactor and regenerator provides both the heat for cracking and the catalyst regeneration.

Hydrocracking operates at higher pressure with hydrogen co-feed over bifunctional catalysts (acid sites for cracking, metal sites for hydrogenation). The hydrogen atmosphere suppresses coke formation, enabling higher conversion of heavy feeds without rapid catalyst deactivation. Product selectivity can be shifted between naphtha, diesel, and jet fuel by adjusting operating severity and catalyst formulation. This flexibility makes hydrocracking valuable for meeting seasonal shifts in product demand.

The development of catalytic cracking in the 1930s and 1940s transformed petroleum refining from a simple separation process into a sophisticated conversion operation. Eugene Houdry's fixed-bed catalytic cracking process, later superseded by the fluid catalytic cracking (FCC) design developed by Warren K. Lewis and Edwin R. Gilliland at MIT, allowed refiners to produce far more gasoline from a barrel of crude than distillation alone could yield.

Primary outputs: `gasoline`, `diesel`, `jet_fuel`, `propylene_from_fcc`, `btx_aromatics`, `refinery_hydrogen`.

The BTX aromatics (benzene, toluene, xylenes) produced by catalytic reforming serve as essential feedstocks for the chemical industry, used in the manufacture of plastics, synthetic fibers, resins, and solvents. The reformer thus serves a dual purpose: upgrading gasoline octane and producing petrochemical building blocks.

The propylene produced as a byproduct of FCC operation has become increasingly valuable as demand for polypropylene has grown. Some FCC units are now operated specifically for maximum propylene yield (petrochemical FCC) by using ZSM-5 zeolite additive in the catalyst and running at higher riser temperatures (540-560°C). This shifts the product distribution away from gasoline toward light olefins, with propylene yields reaching 15-20% of feed compared to the typical 5-8% from a gasoline-maximizing FCC.

## Prerequisites

### Materials

- Zeolite Y catalyst for FCC (rare earth-exchanged, USY grades for different severity levels)
- Platinum-rhenium catalyst for reforming (bimetallic on chlorided alumina support)
- Nickel-molybdenum or cobalt-molybdenum catalyst for hydrocracking (on zeolite or amorphous silica-alumina support)
- Heavy gas oil feedstock from atmospheric or vacuum distillation
- Hydrogen for hydrocracking and reformer net gas supply

### Equipment

- FCC reactor-regenerator with riser, cyclone separators, and catalyst slide valves
- Hydrocracking reactor with fixed-bed catalyst, hydrogen recycle compressor, and high-pressure separator
- Catalytic reformer with multi-bed reactor train and interstage heaters
- Product fractionator for separating cracked products
- Amine treating system for H₂S removal from hydrocracking recycle gas

### Knowledge

- Catalytic chemistry: understanding zeolite acidity, coke formation mechanisms, and metal poisoning (Ni, V, Na deposition on catalyst)
- Fluidized bed dynamics: catalyst circulation rate, catalyst-to-oil ratio, standpipe aeration, and slide valve pressure drop control
- Fractionation of cracked products: cut point management between gasoline, light cycle oil, and heavy cycle oil
- Regenerator heat balance: calculating coke burn rate, regenerator temperature, and excess oxygen requirements
- Hydrocracking reaction kinetics: understanding conversion per pass, hydrogen consumption, and product selectivity as a function of severity

### Infrastructure

- Refinery utility systems: high-pressure steam (for catalyst stripping), instrument air (for control valves), cooling water (for product condensation)
- Product tank farm with segregated storage for gasoline, diesel, jet fuel, LPG, and fuel gas
- Flare system for emergency hydrocarbon relief from all conversion units
- Spent catalyst handling and disposal system (nickel and vanadium-contaminated catalyst is classified hazardous waste)
- Laboratory with gas chromatograph for product yield analysis and micro-reactor for catalyst activity testing

## Process Description

### Step-by-Step Procedure

1. **Feed preheat and atomization**: Preheat heavy gas oil feed to 200-380°C through heat exchangers and a fired heater. Inject into the FCC riser bottom through feed nozzles that atomize the oil into fine droplets for rapid contact with hot regenerated catalyst (650-760°C).
2. **Riser cracking**: The oil-catalyst mixture travels up the riser in 2-10 seconds. Cracking reactions occur as the hydrocarbon vapors contact the zeolite acid sites. Conversion is controlled by catalyst-to-oil ratio (4-8:1) and riser outlet temperature (480-550°C). Higher temperature yields more gasoline and olefins; lower temperature yields more middle distillates.
3. **Catalyst separation**: At the riser top, cyclone separators disengage catalyst from product vapors. The vapors route to the main fractionator. Spent catalyst, now coated with 0.5-2% coke by weight, drops into the stripper section where steam removes entrained hydrocarbons.
4. **Catalyst regeneration**: Spent catalyst flows to the regenerator where air burns coke off the catalyst at 650-760°C. The exothermic combustion heats the catalyst, which then flows back to the riser, carrying the heat needed for the endothermic cracking reactions. Catalyst slide valves control circulation rate.
5. **Product fractionation**: Cracked vapors enter the main fractionator, which separates them into wet gas (C4 and lighter), gasoline (C5-220°C), light cycle oil (220-350°C), heavy cycle oil, and decant oil (slurry). Side strippers sharpen product cut points.
6. **Gas recovery**: The overhead wet gas is compressed and processed through absorbers and strippers to recover C3-C4 LPG and propylene from the fuel gas stream.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Riser outlet temperature | 480-550°C | Higher = more conversion, more gas, less LCO |
| Catalyst-to-oil ratio | 4-8:1 | Higher = more conversion, more coke |
| Regenerator temperature | 650-760°C | Excessive temp degrades zeolite |
| Reactor pressure | 1.5-3.0 bar gauge | Lower pressure favors gasoline yield |
| Catalyst makeup rate | 1-3 tonnes/day | Replaces attrition losses and maintains activity |
| Hydrocracking reactor temp | 350-430°C | Multi-bed with quench between beds |
| Hydrocracking pressure | 80-200 bar | Sufficient to maintain hydrogen partial pressure |

## Safety Considerations

- **Reactor-regenerator explosion**: The regenerator handles hot catalyst in an air atmosphere. Loss of catalyst level control can allow air to reach the reactor, creating an explosive hydrocarbon-air mixture. Catalyst slide valves provide the barrier between these two vessels, and their proper operation is the single most critical safety function.
- **Hydrocracking hydrogen fire**: Hydrocracking operates at 80-200 bar with hydrogen. A leak in the high-pressure circuit creates an immediate fire and explosion hazard. Hydrogen flames are nearly invisible in daylight. High-pressure shutdown systems must isolate the reactor and depressurize to flare within minutes.
- **Pyrophoric catalyst**: Reforming catalyst containing platinum-group metals is pyrophoric when exposed to air in a reduced state. During reactor shutdown, the catalyst must be purged with inert gas and carefully oxidized under controlled conditions before air is introduced.
- **FCC afterburn**: If oxygen breaks through the regenerator dense bed and encounters combustible CO in the dilute phase or cyclones, rapid temperature excursions (afterburn) can exceed metallurgical limits of the cyclones and plenum, causing structural failure.

### Personal Protective Equipment

- Flame-resistant clothing (FRC) for all personnel in the FCC and hydrocracking unit areas
- Self-contained breathing apparatus (SCBA) staged at unit entry points for H₂S emergency
- Insulated gloves and face shield when sampling hot catalyst or opening catalyst handling equipment
- Hard hat with attached hearing protection (FCC regenerator and air blower exceed 90 dBA)
- Personal H₂S monitor, clipped at breathing zone, calibrated monthly

### Emergency Procedures

- Maintain emergency steam supply for catalyst stripping during unplanned shutdown
- Verify firewater system coverage of all hydrocarbon-containing equipment on weekly test
- FCC slide valve failure: automatic shutdown system trips feed to the riser and diverts catalyst flow. Operators must verify slide valve positions and confirm catalyst circulation has stopped.
- Hydrocracking emergency depressurization: automatic system opens blowdown to flare. Operators confirm hydrogen makeup compressor has tripped and block valves have closed.
- Spill response: contain catalyst spills (dry powder, may generate dust). Contain hydrocarbon spills with foam application.

## Quality Control

### Acceptance Criteria

- **Gasoline**: Research octane number (RON) 90-95, Reid vapor pressure meeting seasonal specification, sulfur below regulatory limit
- **Diesel**: Cetane number 40-55, sulfur below regulatory limit, cold filter plugging point meeting seasonal spec
- **Jet Fuel**: Meeting ASTM D1655 specifications for flash point, freeze point, and thermal stability
- **Propylene from FCC**: Minimum 95% purity for chemical-grade, 99.5% for polymer-grade after purification

### Testing Methods

- Product fraction boiling range analysis by gas chromatography (ASTM D5443)
- Catalyst activity testing in laboratory micro-reactor (MAT test — micro-activity test)
- Octane number determination for gasoline by research method (ASTM D2699)
- Cetane number for diesel by engine test or calculated from cetane index (ASTM D976)
- Hydrogen purity analysis by thermal conductivity detector on reformer net gas
- Regenerator flue gas analysis: O₂, CO, CO₂, NOx for combustion efficiency monitoring

### Sampling Protocol

- Monitor catalyst circulation rate and catalyst-to-oil ratio continuously via slide valve pressure drop
- Track regenerator temperature and excess oxygen as safety indicators — rising O₂ after the dense bed signals afterburn risk
- Sample FCC gasoline for octane every 8 hours; adjust riser temperature if trending off-spec
- Sample hydrocracker products for nitrogen content weekly; rising nitrogen signals catalyst deactivation
- Track catalyst metals content (Ni, V, Na) monthly via laboratory analysis; high metals increase coke and gas yield

## Scaling Notes

Catalytic cracking units are among the most complex and capital-intensive equipment in a refinery. A world-scale FCC processes 30,000-100,000 barrels per day of feed. The regenerator vessel must handle large volumes of hot catalyst and combustion air while maintaining controlled temperature. Excessive regenerator temperature (above ~760°C) degrades the zeolite catalyst through hydrothermal dealumination, destroying its cracking activity.

Metal contaminants in the feed, particularly nickel and vanadium from the crude oil, deposit on the catalyst and promote undesirable dehydrogenation reactions. This increases coke and gas production at the expense of gasoline yield. Feedstock pretreatment (hydrotreating) or metal-tolerant catalyst formulations mitigate this issue, particularly when processing heavier crude oils with higher contaminant levels.

Catalyst makeup rates of 1-3 tonnes per day offset attrition losses and maintain activity. The fresh catalyst cost is a significant operating expense. Spent catalyst, loaded with nickel, vanadium, and coke residue, must be disposed of as hazardous waste.

Hydrocracking units scale to 15,000-50,000 barrels per day. The high-pressure reactor vessel (forged steel, 200+ bar design pressure) is a long-lead procurement item. Multiple catalyst beds with interbed quench control the exothermic heat of reaction. The hydrogen recycle compressor is the largest rotating equipment in the unit, consuming substantial power.

The FCC riser reactor is a vertical pipe, typically 30-50 meters tall and 0.5-1.5 meters in diameter, where the cracking reactions occur. Feed and catalyst enter at the bottom and travel upward together in 2-10 seconds of contact time. The short contact time is by design: longer contact promotes secondary cracking reactions that produce more light gas and coke at the expense of desired gasoline and LCO products. Modern short-contact-time riser designs terminate with rapid catalyst separation (riser termination devices, RTDs) to quench the reaction as quickly as possible.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Excessive coke on catalyst | Feed too heavy, cat-to-oil ratio too high, or riser temperature too high | Adjust feed blend to reduce Conradson carbon; lower catalyst-to-oil ratio; lower riser temperature |
| Afterburn in regenerator | Excess oxygen or uneven air distribution through the air ring | Reduce combustion air rate; inspect and clean air ring nozzles during turnaround |
| High dry gas yield | Severe cracking conditions or metals contamination on catalyst | Reduce riser temperature; reduce cat-to-oil ratio; increase fresh catalyst makeup to dilute metals |
| Low gasoline octane | Insufficient cracking severity | Raise riser outlet temperature; increase cat-to-oil ratio; check catalyst activity (MAT test) |
| Hydrocracker conversion dropping | Catalyst deactivation or lower reactor temperature | Raise reactor temperature (within limits); check hydrogen partial pressure; plan catalyst regeneration |
| Regenerator temperature too high | Excessive coke on catalyst or afterburn | Reduce feed rate; reduce cat-to-oil ratio; check for afterburn by analyzing flue gas CO profile |
| Catalyst attrition excessive | High catalyst circulation velocity or damaged cyclones | Reduce circulation rate; inspect cyclones during next turnaround; check catalyst hardness specification |
| Slide valve pressure drop low | Insufficient catalyst level above the valve or valve erosion | Increase catalyst inventory; inspect valve internals during turnaround; verify standpipe aeration is adequate |
| Regenerator afterburn temperature spike | Combustion of CO in the dilute phase above the dense bed | Reduce excess oxygen; check air ring nozzle condition; install CO combustion promoter catalyst |

## Variations and Alternatives

- **Thermal cracking**: Cracking without catalyst, using purely thermal energy. Older technology (Dubbs, Visbreaking), lower selectivity, more coke and gas, less gasoline. Simpler equipment but poorer economics.
- **Coking (delayed coking)**: Extreme thermal cracking of the heaviest refinery residues into petroleum coke, gas oil, and fuel gas. Provides a disposal pathway for vacuum residue that would otherwise accumulate. The coke product has value as electrode carbon or fuel.
- **Alkylation**: Reacts isobutane with light olefins (propylene, butylene) over strong acid catalyst (sulfuric or hydrofluoric acid) to produce high-octane gasoline blending stock. Valued for its high octane and low vapor pressure, making it an ideal gasoline component. Alkylation units require significant safety infrastructure due to the large inventories of concentrated acid.
- **Isomerization**: Converts straight-chain pentane and hexane (low octane, ~60 RON) into their branched isomers (high octane, ~85-90 RON) over platinum catalyst at moderate temperature. A mild conversion process that upgrades light naphtha without changing the carbon number.

Catalyst regeneration in the FCC unit is continuous. Spent catalyst flows from the reactor to the regenerator where coke is burned off with air, then returns to the reactor. This continuous loop means the FCC operates without shutdown for catalyst change, unlike fixed-bed hydrocracking reactors that must be taken offline for catalyst replacement. The heat from coke combustion in the regenerator supplies the endothermic heat of cracking in the reactor, making the FCC largely self-sustaining in energy terms once operating.

The yield structure from a cracking unit, the distribution of products across gasoline, diesel, jet fuel, LPG, and fuel gas fractions, is the primary economic driver. Refinery profitability depends on maximizing the yield of higher-value products (gasoline, diesel) while minimizing low-value fuel gas and heavy residue. Seasonal shifts in product demand are accommodated by adjusting operating severity and feedstock selection across the conversion units.

Catalytic reforming converts low-octane naphtha (typically 40-60 RON) into high-octane reformate (95-105 RON) by dehydrogenating naphthenes to aromatics and isomerizing paraffins. The reformer operates at 490-530°C over a platinum-rhenium catalyst on chlorided alumina. Net hydrogen production (200-400 Nm³/ton of feed) is a valuable byproduct used in hydrocracking, hydrotreating, and other hydrogen-consuming processes throughout the refinery. The reformer is often called the "heart" of the refinery because it produces both high-value gasoline blend stock and the hydrogen that enables clean fuel production.

The FCC catalyst is a fine powder (average particle size 60-80 μm) that flows like a liquid when aerated. This fluidization property allows continuous circulation between reactor and regenerator through standpipes and slide valves. The zeolite Y crystal structure provides the acid sites for cracking, while the matrix provides mesoporosity for pre-cracking large molecules before they enter the zeolite pores. Catalyst formulation is the primary tool for adjusting yield selectivity, with different grades optimized for maximum gasoline, maximum propylene, or maximum middle distillates.

Hydrocracking catalysts are bifunctional, combining metal hydrogenation sites (Ni-Mo or Co-Mo sulfides) with acidic cracking sites (zeolite or amorphous silica-alumina). The hydrogenation function saturates olefins and aromatics produced by cracking, preventing coke formation that would rapidly deactivate the catalyst. This allows hydrocracking to achieve near-complete conversion of heavy feeds to distillate-range products in a single pass, something the FCC cannot do with heavy, aromatic-rich feedstocks.

Reforming catalyst deactivation is managed through semi-regenerative or continuous regeneration designs. Semi-regenerative units operate for 6-24 months before shutdown for catalyst regeneration by burning off coke. Continuous catalyst regeneration (CCR) units circulate catalyst through a separate regenerator, similar to FCC, allowing the reactor to operate continuously at high severity without shutdown for years. CCR reformers produce more hydrogen and higher-octane gasoline but require more complex equipment.

The light cycle oil (LCO) from the FCC, a diesel-range product, typically has poor ignition quality (low cetane number, typically 20-30) and high sulfur and aromatic content. LCO requires hydrotreating to improve cetane and reduce sulfur before it can be blended into the diesel pool. This dependency on downstream hydrotreating capacity is a constraint on FCC LCO yield: if the hydrotreater is full, the FCC must reduce throughput or change operating conditions to produce less LCO.

The decant oil (slurry oil) drawn from the bottom of the FCC main fractionator is the heaviest liquid product, containing fine catalyst particles entrained from the reactor. Decant oil is used as fuel oil blend stock, carbon black feedstock, or in some cases recycled back to the FCC riser for additional conversion. Its high aromatic content and catalyst fines make it the lowest-value liquid product from the cracking unit.

## References

- [Petroleum Refining](refining.md) — parent capability
- [Petroleum Domain](./index.md) — domain overview and related capabilities
- [Petroleum Refining](refining.md) — downstream capability
- [Atmospheric & Vacuum Distillation](distillation.md) — downstream capability

### Material Handling

- Handle spent catalyst as hazardous waste: it contains deposited nickel, vanadium, and residual coke. Store in sealed containers awaiting disposal or metals reclamation.
- Store fresh FCC catalyst in sealed containers protected from moisture. Zeolite catalyst loses activity when exposed to humidity due to dealumination and pore collapse.
- Maintain hydrogen supply pipeline integrity with regular leak detection surveys. Hydrogen leaks are invisible and odorless but create immediate fire hazards.
- Label and segregate all hydrocarbon product streams in the tank farm. Cross-contamination between gasoline and diesel degrades both products.
- Sample each incoming catalyst shipment for activity testing before loading into the unit. Off-spec catalyst wastes a complete loading operation.
- Monitor hydrocracker hydrogen recycle gas purity regularly; contamination with light hydrocarbons reduces hydrogen partial pressure and accelerates catalyst coking
- Track fresh catalyst inventory and lead time for delivery; some specialty catalyst grades require 6-12 months of advance ordering

---
*Part of the [Bootciv Tech Tree](../index.md) · [Petroleum](./index.md) · [All Domains](../index.md)*
