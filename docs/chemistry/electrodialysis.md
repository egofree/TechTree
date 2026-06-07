# Electrodialysis

> **Node ID**: chemistry.electrodialysis
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`Electrolysis`](electrolysis.md)
> **Enables**: [`Desalination`](desalination.md), [`Hydroponic pH Control`](hydroponic-ph-control.md), [`Blue Energy (Osmotic Power)`](blue-energy.md), [`Acid Regeneration`](acid-regeneration.md)
> **Timeline**: Years 25-45
> **Outputs**: separated_ions, purified_water
> **Critical**: No

## Overview

Ion separation using alternating cation and anion exchange membranes under electric field. Desalinates brackish water, recovers acids and bases from salt solutions, and concentrates process streams for industrial chemistry.

Electrodialysis enters the technology tree once a civilization can produce ion-exchange membranes (cross-linked styrene-divinylbenzene copolymers with fixed sulfonate or quaternary ammonium groups) and supply controlled DC power. Unlike reverse osmosis, which filters all solutes through a pressure-driven membrane, electrodialysis removes ions specifically by migrating them through alternating cation and anion exchange membranes under an electric field. This makes it more energy-efficient for brackish water desalination because the energy input scales with the amount of salt removed, not the volume of water processed.

The two outputs serve different purposes: purified water (the diluate stream, stripped of ions) goes to drinking water, industrial process water, or feed for further polishing; the concentrated ion stream (the concentrate, enriched in salts) is either disposed of, further processed for salt recovery, or used as a chemical feedstock.

Electrodialysis differs from reverse osmosis in that it removes ions specifically rather than filtering all solutes through a membrane. This makes it more energy-efficient for desalination of brackish water (which has lower salt content than seawater) because the energy input is proportional to the amount of salt removed, not the volume of water processed. For water with moderate salinity, electrodialysis often requires less energy per unit of purified water than reverse osmosis.

The key components are the ion exchange membranes. Cation exchange membranes contain fixed negative charges (sulfonate or carboxylate groups) that repel anions while allowing cations to pass. Anion exchange membranes contain fixed positive charges (quaternary ammonium groups) that repel cations while allowing anions to pass. These membranes are made from cross-linked polymers (typically styrene-divinylbenzene copolymers) with the charged functional groups attached to the polymer backbone. Membrane selectivity and electrical resistance are the primary performance parameters — good membranes have high ion selectivity (>95%) and low electrical resistance.

Electrodialysis also enables unique chemical processing capabilities that reverse osmosis cannot achieve. By selecting appropriate membrane configurations, it can split salt solutions into separate acid and base streams, concentrate specific ions for metal recovery, or remove ionic contaminants from process streams while retaining valuable non-ionic solutes.

## Prerequisites

### Materials

- Chemicals — process-specific feed solutions, electrode rinse solution (sodium sulfate or sodium chloride)
- Ion exchange membranes — cation exchange (CEM) and anion exchange (AEM) sheets
- Spacers and gaskets (polyethylene or rubber) for membrane stack assembly
- Electrode materials (titanium coated with mixed metal oxides for anode, stainless steel for cathode)

### Equipment

- [Electrolysis](electrolysis.md) — tool dependency
- DC power supply with voltage and current control
- Membrane stack (filter-press design with alternating CEM/AEM/spacer/gasket)
- Feed pumps for diluate, concentrate, and electrode rinse circuits
- Pre-filtration system for feed water treatment
- Clean-in-place (CIP) system for membrane maintenance

### Knowledge

- Ion transport under electric field: how cations migrate through CEM (fixed sulfonate groups pass Na⁺, Ca²⁺, Mg²⁺) and anions through AEM (fixed quaternary ammonium groups pass Cl⁻, SO₄²⁻, NO₃⁻), and why each membrane blocks the opposite charge via Donnan exclusion
- Concentration polarization: the depleted boundary layer that forms at the membrane surface when ions are removed faster than bulk diffusion can replenish them, and how flow spacers and current density limits prevent water splitting
- Stack assembly geometry: the alternating CEM/AEM/spacer/gasket filter-press pattern, and how a single reversed membrane creates a dead cell pair that reduces overall separation performance
- Conductivity-based process monitoring: how stack voltage at constant current tracks fouling, and how diluate conductivity tracks product quality in real time

### Infrastructure

- Enclosed workspace with ventilation for hydrogen gas removal from the cathode compartment, plus drainage for salt solution handling
- Power supply matching equipment requirements — DC rectifier with current and voltage control
- Water supply and drainage where applicable — feed water pre-treatment may be needed
- Waste handling and disposal facilities for process outputs — concentrate streams may require special disposal
- Membrane storage area with humidity and temperature control for spare membranes

## Process Description

An electrodialysis stack separates ions by arranging alternating cation exchange membranes (CEM) and anion exchange membranes (AEM) between two electrodes. The DC field drives cations toward the cathode and anions toward the anode. Each ion passes through its corresponding membrane type but is blocked by the opposite type, creating alternating compartments of depleted (diluate) and enriched (concentrate) solution.

An electrodialysis stack consists of alternating cation exchange membranes (CEM) and anion exchange membranes (AEM) placed between two electrodes. When a DC voltage is applied across the electrodes, cations migrate toward the cathode and anions toward the anode. Cations pass through CEMs but are blocked by AEMs. Anions pass through AEMs but are blocked by CEMs. This creates alternating compartments of diluate (depleted in ions) and concentrate (enriched in ions) as the feed flows through the stack.

### Step-by-Step Procedure

1. Prepare the electrolyte to specified concentration and temperature. Verify pH, conductivity, and metal ion content. Pre-filter all feed solutions to remove suspended particles larger than a few micrometers — particles foul membrane surfaces and block flow channels.
2. Assemble the membrane stack with alternating CEM and AEM sheets separated by spacers that define the flow channels. Ensure proper alignment — misaligned membranes create internal leaks between diluate and concentrate compartments.
3. Connect the DC power supply to the electrode compartments. Electrode rinse solution (typically sodium sulfate or sodium chloride) circulates separately to carry away electrode reaction products (acid at the anode, base at the cathode).
4. Start feed flow through the stack and apply DC current. Monitor stack voltage — rising voltage at constant current indicates membrane fouling or scaling.
5. Collect diluate (purified water or depleted stream) and concentrate (brine or enriched stream) separately. Adjust flow rates and current density to achieve the target ion removal.
6. Periodically reverse polarity (electrodialysis reversal, EDR) to flush scale deposits from membrane surfaces and extend membrane life.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Current density | Moderate | Limited by concentration polarization at membrane surface |
| Feed TDS | Low to moderate | Very high salinity increases energy consumption |
| Recovery | 75-95% | Higher recovery increases brine concentration |
| Membrane pair voltage | Typically 0.5-2V | Higher voltage indicates fouling |
| Stack temperature | Ambient to moderate | Higher temps increase conductivity but may damage membranes |

## Safety Considerations

Electrodialysis combines high-current DC electricity, pressurized fluid circuits, and chemically aggressive membrane materials. The hazards are specific to each subsystem:

- **Electrical hazards**: The DC power supply operates at substantial voltage (tens to hundreds of volts) and high current. All electrical connections must be insulated and the stack enclosure must prevent contact with energized components. Lockout/tagout procedures required for all maintenance.
- **Chemical exposure**: Feed and product streams may contain concentrated acids, bases, or salt solutions depending on the application. Electrode rinse streams become acidic (anode) or basic (cathode) during operation.
- **Hydrogen generation**: The cathode reaction produces hydrogen gas. In enclosed stacks or poorly ventilated areas, hydrogen can accumulate to flammable concentrations.
- **Membrane failure**: Damaged membranes allow mixing of diluate and concentrate streams. In some applications (e.g., acid/base production), mixing can generate heat or gas.

### Personal Protective Equipment

- Chemical splash goggles and face shield rated for the specific solutions being processed (acid, base, or concentrated brine)
- Chemical-resistant gloves appropriate to the solutions being processed
- Insulated tools for electrical connections
- Respiratory protection when cleaning membranes with acid solutions

### Emergency Procedures

- Electrical emergency: de-energize power supply before approaching the stack. Post grounding hooks near high-current equipment.
- Chemical spill: contain and neutralize per the specific chemical involved
- Hydrogen buildup: ensure continuous ventilation of stack enclosures; install hydrogen detectors in enclosed spaces

## Quality Control

### Acceptance Criteria

- **Separated Ions**: Concentrate stream must reach target ion concentration for downstream use or disposal. Current efficiency must remain above minimum threshold.
- **Purified Water**: Diluate stream must meet target TDS (total dissolved solids) for the intended application. Specific ion limits depend on the use case.

### Testing Methods

- Conductivity measurement for on-line monitoring of diluate and concentrate streams
- Ion-selective electrode or titration for specific ion quantification
- Total dissolved solids measurement by evaporation or conductivity correlation
- Membrane integrity testing by pressure hold or conductivity profiling

### Sampling Protocol

- Continuous conductivity monitoring on both diluate and concentrate outlets
- Daily laboratory analysis of feed and product streams for comprehensive ion balance
- Monthly membrane inspection and performance evaluation to detect fouling trends

## Scaling Notes

Scaling from a single laboratory membrane pair to a municipal desalination plant follows these stages:

- **Bench scale**: Single membrane pair in a laboratory cell. Processes milliliters to liters. Used for membrane selection, feed characterization, and process feasibility studies.
- **Pilot scale**: Small stack (10-50 membrane pairs) with controlled feed and product tanks. Processes hundreds to thousands of liters per day. Validates fouling behavior, energy consumption, and product quality over extended runs.
- **Production scale**: Multiple large stacks in parallel, each with hundreds of membrane pairs. Automated monitoring and control. Processes thousands of cubic meters per day for municipal or industrial applications.

Key scaling challenges: membrane fouling is the dominant operational issue — scaling (calcium carbonate, calcium sulfate), organic fouling, and biofouling all reduce performance over time. Pre-treatment requirements scale with feed water quality. Membrane replacement cost dominates the economics. Flow distribution across large stacks must be uniform to prevent channeling and localized concentration polarization.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Rising stack voltage | Membrane fouling or scaling | Clean-in-place with acid (for scaling) or caustic (for organics) |
| Poor ion removal | Insufficient current or short residence time | Increase current density; add membrane pairs; reduce flow rate |
| Internal leakage | Damaged membranes or misaligned spacers | Disassemble stack; inspect and replace damaged components |
| Electrode degradation | Electrode reaction products not flushed | Increase electrode rinse flow; check electrode polarity |
| Low product recovery | High brine concentration or osmotic back-flow | Reduce brine concentration; check membrane integrity |

## Variations and Alternatives

- **Electrodialysis Reversal (EDR)**: Periodic polarity reversal (every 15-30 minutes) to reduce scaling and fouling. Standard for municipal water treatment applications. Slightly more complex controls but significantly reduces membrane cleaning frequency.
- **Reverse osmosis (RO)**: Pressure-driven membrane process. More energy-efficient for high-TDS desalination (seawater). ED is more efficient for brackish water (lower TDS) and for selective ion removal.
- **Bipolar membrane electrodialysis (EDBM)**: Uses bipolar membranes to split water into H⁺ and OH⁻, directly generating acid and base from salt solutions without electrodes. Used in acid/base recovery and organic acid production.
- **Continuous electrodeionization (CEDI)**: Combines ion exchange resins with ED membranes for ultrapure water production. Resins fill the diluate chambers, enhancing ion transport and enabling very low product conductivity.

Electrodialysis is most economically competitive for brackish water desalination (TDS in the low-to-moderate range) and for niche industrial separations where selective ion removal or concentration is needed. For seawater desalination, reverse osmosis typically has lower energy consumption because ED energy scales linearly with salt concentration. For ultrapure water production, CEDI provides the final polishing step after RO pretreatment. The bipolar membrane variant opens unique chemical processing routes that cannot be achieved by pressure-driven membrane processes.

## References

- [Chemistry](chemistry.md) — parent capability
- [Chemistry Domain](./index.md) — domain overview and related capabilities
- [Electrolysis](electrolysis.md) — upstream dependency (tool)
- [Desalination](desalination.md) — downstream capability
- [Hydroponic pH Control](hydroponic-ph-control.md) — downstream capability
- [Blue Energy (Osmotic Power)](blue-energy.md) — downstream capability

Electrodialysis builds on the electrolysis capability — the membrane and electrode technology are shared. The purified water and concentrated ion streams it produces enable a range of downstream applications from desalination to industrial chemistry.

The energy consumption of electrodialysis is proportional to the amount of salt removed, not the volume of water processed. This makes it more economical than reverse osmosis for low-salinity feeds (brackish water, river water with moderate TDS) where the salt load is small but the water volume is large. For seawater desalination, the high salt load makes ED less competitive with RO on energy grounds, though ED has the advantage of higher water recovery (less brine waste) and no high-pressure pumping requirements.

Concentration polarization is the fundamental limitation on ED performance. At the membrane surface, ions are being removed faster than they can diffuse from the bulk solution, creating a depleted boundary layer. This increases the effective electrical resistance and, at extreme polarization, causes water splitting at the membrane surface (generating H⁺ and OH⁻ ions that carry current without contributing to separation). Controlling polarization requires adequate flow velocity across the membrane surface (maintained by the spacers), limiting current density, and avoiding excessive ion removal in a single pass.

The development of ion exchange membranes was historically tied to the development of ion exchange resins for water treatment. Early membranes were made by incorporating ion exchange resin particles into polymer films. Modern membranes are homogeneous — the charged groups are chemically bonded directly to the polymer backbone of the membrane film. This provides better selectivity and lower electrical resistance. Membrane lifetime is typically 3-7 years in clean applications (brackish water desalination) but can be much shorter in harsh chemical environments (acid recovery, organic process streams).

Electrodialysis systems are inherently modular — capacity can be increased by adding membrane pairs to a stack or by adding stacks in parallel. This makes ED well-suited to incremental capacity expansion as water demand grows. A small installation might start with a single stack producing a few hundred liters per hour of desalinated water, then expand by adding identical stacks as the community or industry grows. The DC power supply and control system can be shared across multiple stacks, with each stack individually valved for isolation during maintenance.

The electrode reactions in an ED system produce chemical changes that must be managed. At the anode, water oxidizes to produce oxygen gas and hydrogen ions (acid). At the cathode, water reduces to produce hydrogen gas and hydroxide ions (base). The electrode rinse stream carries these products away and must be kept separate from the product streams. In some configurations, the electrode rinse is itself a useful product — the anode compartment produces dilute acid and the cathode compartment produces dilute base. The gases (oxygen and hydrogen) are typically vented or captured. The electrode rinse solution must be chemically compatible with the electrodes and must not deposit scale or fouling materials on the electrode surfaces.

Electrodialysis reversal (EDR) was developed to address the scaling problem that plagued early ED installations. When the polarity is reversed, the diluate compartments become concentrate compartments and vice versa. This reversal flushes nascent scale deposits off the membrane surfaces before they can harden into permanent fouling. EDR systems switch polarity every 15-30 minutes, with automated valves redirecting the product streams appropriately. The brief mixing during the transition is accepted as a small quality tradeoff for greatly reduced membrane cleaning requirements. EDR is now the standard configuration for most municipal and industrial ED installations.

For desalination applications, the product water quality from ED is typically measured in total dissolved solids (TDS). Feed water with moderate TDS (brackish water) can be reduced to drinking water standards with a single ED pass. The power consumption is proportional to the TDS reduction — each gram of salt removed per liter requires a specific amount of electrical energy. For very dilute feeds (TDS below the drinking water standard), no ED treatment is needed. For very concentrated feeds (seawater), the energy cost of ED exceeds that of reverse osmosis. The optimal operating range for ED is therefore the middle ground: too salty for direct use but not so salty that pressure-driven methods are more efficient.

Electrodialysis also has advantages in situations where selective ion removal is needed rather than total desalination. For example, nitrate removal from drinking water, fluoride removal from groundwater, or hardness removal (water softening) can be accomplished by ED with appropriate membrane selection. In these applications, the target ions are removed while other dissolved solids are retained, producing partially treated water that meets specific quality criteria without the waste of removing all dissolved solids.

The membranes themselves are the primary consumable in an ED system. Over time, membranes lose selectivity and gain electrical resistance due to fouling (organic and biological), scaling (inorganic precipitates), and chemical degradation (oxidation, hydrolysis). Regular cleaning with acid (for scale), caustic (for organics), and biocide (for biofouling) extends membrane life but cannot restore damaged membranes. When membrane performance drops below the economic threshold, the stack must be disassembled and the membranes replaced. Spent membrane disposal follows hazardous waste protocols if the membranes have been in contact with regulated substances.


### Material Handling

Proper handling of input materials and products is essential for consistent results:

- Store ion exchange membranes in sealed bags with process solution; drying permanently damages the charged polymer structure and cannot be reversed by re-wetting
- Pre-condition new membranes in the process solution before installation to allow full swelling and dimensional stabilization; installing dry or partially swollen membranes causes buckling and leaks in the stack
- Maintain the CEM/AEM alternation pattern when reassembling the stack after cleaning; a single reversed membrane cell pair reduces separation performance and can create local pH extremes
- Tighten stack tie rods evenly in a cross-pattern to compress gaskets uniformly; over-tightening crushes membranes, under-tightening causes internal leakage between diluate and concentrate
- Log stack voltage, diluate conductivity, and product flow rate per shift; trends in these parameters predict membrane replacement timing weeks in advance

Ion exchange membranes are delicate and must be handled carefully. Keep membranes moist at all times — drying permanently damages the polymer structure. Store spares in sealed bags with a small amount of the process solution to maintain hydration. When installing new membranes, pre-condition them in the process solution before placing in the stack to allow full swelling and dimensional stabilization. Spent membranes are classified as hazardous waste if they have been used with toxic or corrosive process streams — follow applicable disposal regulations.

Membrane stack assembly requires care and precision. The alternating CEM/AEM pattern must be maintained throughout — a single reversed membrane reverses the ion transport in that cell pair, reducing overall performance and potentially creating local concentration extremes. Spacers between membranes define the flow channels and must be aligned to maintain uniform flow distribution. The stack bolts must be tightened evenly to compress the gaskets and create leak-tight seals without over-compressing the membranes. Most stacks use a filter-press design where the entire stack is held between two end plates by tie rods.
Spent membrane disposal follows hazardous waste protocols if the membranes have been in contact with regulated substances.

---
*Part of the [Bootciv Tech Tree](../index.md) · [Chemistry](./index.md) · [All Domains](../index.md)*
