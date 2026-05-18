# Metallurgical-Grade Silicon Production

> **Node ID**: `silicon.mg-si-production`
> **Domain**: [Silicon](./)
> **Dependencies**: `energy.electric-furnaces`, `mining`
> **Timeline**: Years 30-40
> **Outputs**: mg_silicon

### Metallurgical-Grade Silicon (MG-Si) Production

**Process**: Carbothermic reduction of quartz in submerged arc electric furnace.
- **Reaction**: SiO₂ + 2C → Si + 2CO (endothermic, ΔH ≈ +690 kJ/mol)
- **Temperature**: ~1800-2100°C in the reaction zone
- **Raw materials**:
  - **Quartz**: High-purity SiO₂ (>98%). Crushed to 2-10 cm lumps. Impurities (Fe, Al, Ca) become contaminants in product silicon.
  - **Carbon reductant**: Mix of charcoal, coke, and wood chips (provides porosity for gas escape). Coal/coke alone produces dense charge that traps gas.
  - **Typical charge ratio**: ~2 tonnes quartz + 1 tonne carbon → ~1 tonne MG-Si (+ byproducts)
- **Furnace construction**:
  - **Shell**: Steel, 3-8 m diameter, lined with carbon refractory (prebaked carbon blocks or rammed carbon paste).
  - **Electrodes**: 1-3 prebaked graphite electrodes (Søderberg self-baking electrodes possible). Diameter 300-800 mm. Suspended from hydraulic hoists, adjustable height.
  - **Power**: 5-30 MW per furnace. Three-phase AC (for 3-electrode furnace). Voltage 100-250V, current 20,000-100,000 A.
  - **Tapping**: Molten silicon (density 2.33 g/cm³, lighter than slag) tapped from furnace bottom through taphole into cast iron molds or ladle. Tap every 1-4 hours.
- **Energy consumption**: ~11-13 kWh/kg MG-Si (this is enormous — a 1 tonne/day furnace needs ~500 kW continuous).
- **MG-Si purity**: ~97-99% Si. Major impurities: Fe (0.3-0.8%), Al (0.2-0.7%), Ca (0.1-0.5%), Ti, Mn, C. Not pure enough for electronics or efficient solar cells.
- **Crushing**: Break MG-Si ingots to 1-10 cm chunks with jaw crusher, then ball mill to 100-500 μm powder for chemical purification.

### Yield & Material Balance

- **Silicon yield**: 75-85% of theoretical. Losses come from SiO gas escaping the furnace (SiO₂ + C → SiO + CO at intermediate temperatures), silicon dissolving into slag, and spillage during tapping.
- **Specific consumption**: ~2.7-3.0 tonnes quartz + 1.0-1.4 tonnes carbon reductant per tonne of MG-Si produced. Wood chips add ~0.5-1.0 tonnes for porosity (partial reductant, partial gas channel).
- **Improving yield**: Charge porosity is critical. Too dense → SiO gas trapped, forms SiO₂ fume that condenses in off-gas system (lost silicon). Too porous → uneven heating, cold spots. Wood chip ratio is a tuning parameter.

### Electrode Consumption

Electrodes are a major operating cost and a bootstrapping dependency:
- **Prebaked graphite electrodes**: Consumption ~400-500 kg per tonne Si. Higher cost, lower consumption, more consistent operation. Must be manufactured off-site (see [electric-furnaces.md](../energy/electric-furnaces.md) for electrode manufacturing).
- **Søderberg self-baking electrodes**: Consumption ~300-400 kg per tonne Si. Carbon paste (petroleum coke + coal tar pitch) added continuously at top of electrode column. Furnace heat bakes the paste as it descends — no separate graphitization step needed. Simpler supply chain but less pure (contaminants from paste enter silicon).
- **Choice for bootstrapping**: Søderberg electrodes are easier to produce (no graphitization furnace required) but introduce more impurities. For MG-Si destined for chemical purification (Siemens process), this is acceptable since impurities are removed downstream.

### Off-Gas Handling

The furnace produces large volumes of hot, toxic gas:
- **CO gas**: ~2.5-3.5 tonnes CO per tonne Si. Carbon monoxide is flammable (LFL 12.5% in air) and acutely toxic (binds hemoglobin 200× stronger than O₂). Must be captured, never vented untreated.
  - **Flaring**: Burn CO to CO₂ at the furnace hood. Simple but wastes chemical energy. Requires continuous pilot light — if flame extinguishes, raw CO accumulates.
  - **Energy recovery**: Route CO to a boiler or gas turbine for co-generation. Recovers ~30-40% of furnace electrical input as thermal energy. Requires gas cleaning (dust, SiO fume) before combustion.
- **SiO fume**: Silicon monoxide vapor condenses to ultrafine SiO₂ particles (<1 μm) in the off-gas. Known as "silica fume." Collected in baghouse filters. ~200-400 kg per tonne Si. Valuable byproduct — sold as pozzolanic additive for high-strength concrete, or reprocessed.
- **Dust**: Quartz fines and carbon particles entrained in gas stream. Removed by cyclone separators + baghouse. Recycle coarse dust to furnace charge.

### Slag Management

- **Slag formation**: Impurities in quartz and reductant (Al₂O₃, CaO, FeO, MgO) form a molten slag layer floating above the denser silicon. Slag is intentionally managed — sometimes flux (lime, silica) is added to control slag viscosity and trap impurities.
- **Slag composition** (typical): 30-50% SiO₂, 15-30% Al₂O₃, 10-20% CaO, 5-15% SiC, balance FeO, MgO. Varies with raw material quality.
- **Tapping**: Slag tapped separately from silicon through a higher taphole (slag floats on silicon). Some furnaces use a single taphole with sequential tapping (slag first, then silicon).
- **Disposal or reuse**: Slag can be crushed and used as road base aggregate or construction fill. If heavy metal content is low, it may be returned to the furnace as partial charge (recovers trapped silicon). Some operators sell slag to cement manufacturers as a silica source.

### Furnace Startup & Shutdown

- **Cold startup** (from ambient): Preheat furnace with gas burners or resistive heating to ~800-1000°C over 24-48 hours. This dries the lining and prevents thermal shock cracking of carbon refractory. Then charge raw materials, lower electrodes, strike arc, and gradually increase power over 6-12 hours to full load. Full production reached in 24-72 hours.
- **Hot restart** (after brief interruption <4 hours): Electrodes still hot, lining warm. Re-strike arc and ramp power over 2-4 hours.
- **Planned shutdown**: Reduce power gradually over 4-8 hours. Raise electrodes. Seal furnace to retain heat. A well-sealed furnace retains >500°C for 24+ hours, enabling easier restart.
- **Emergency shutdown**: Cut power immediately. Raise electrodes. Risk: molten silicon freezes in taphole, requiring drilling or oxygen lancing to clear. Keep taphole open during emergency drain if possible.

### Safety Hazards

Operating a submerged arc furnace for silicon production involves severe hazards:
- **CO gas poisoning**: Carbon monoxide is colorless, odorless, and lethal at 0.1% concentration in air for 1 hour. Off-gas system leaks are the primary risk. Fixed CO detectors with audible alarms mandatory in furnace building. Personnel must evacuate at >50 ppm. Never enter furnace hood area without supplied-air respirator during operation.
- **Molten silicon**: Pours at ~1450-1600°C. Contact causes immediate deep burns. Molten silicon on wet surfaces or water causes steam explosion — catastrophic ejection of molten metal. All molds, ladles, and tools must be thoroughly pre-dried. No water in tapping area. Pouring ladle must be lined with dry refractory.
- **Arc flash**: 20,000-100,000 A at 100-250V. Electrode adjustment system failure can cause short circuit with explosive energy release. Arc flash boundary: 2-5 m minimum. Flame-resistant clothing, face shield, insulating gloves required near electrode hoists.
- **Silica dust inhalation**: Quartz handling (crushing, loading) generates respirable crystalline SiO₂ dust. Causes silicosis (irreversible lung scarring) after years of exposure. Dust suppression: wet crushing, enclosed conveyor systems, local exhaust ventilation. Respirator (P100) required in dusty areas.
- **Burns from hot surfaces**: Furnace shell, electrode columns, and tap ladles are 200-600°C on exterior. Thermal gloves (rated to 500°C minimum) and face protection for all tapping operations. Mark hot zones with barricades.
- **Cooling water hazard**: Furnace components (electrode clamps, shell panels) are water-cooled. A cooling water leak into the furnace causes immediate steam explosion. Monitor cooling water flow and temperature continuously. Automatic shutdown on flow loss.

---
*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*