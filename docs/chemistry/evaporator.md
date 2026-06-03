# Evaporator

> **Node ID**: chemistry.evaporator
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`chemistry.heat-exchanger`](heat-exchanger.md), [`energy.steam`](../energy/coal.md)
> **Enables**: [`chemistry.alkalis`](alkalis.md), [`chemistry.water-treatment`](water-treatment.md), [`food-processing.preservation`](../food-processing/preservation.md)
> **Timeline**: Years 10-25
> **Outputs**: concentrated_liquid, distilled_water
> **Critical**: No — evaporators concentrate solutions and recover solvents but can be replaced by simpler methods (open-pan evaporation, solar evaporation) at lower efficiency

## Principle

An evaporator concentrates a liquid solution by boiling off the solvent (typically water) as vapor, leaving the dissolved solids behind in a more concentrated liquid. Unlike distillation, which separates components by boiling point differences, evaporation simply removes bulk solvent to reduce volume, increase concentration, or recover purified solvent. The driving force is heat input that supplies the latent heat of vaporization (2,260 kJ/kg for water at 100°C).

Industrial evaporators operate under vacuum to lower the boiling point, reducing thermal degradation of heat-sensitive products and improving energy efficiency (lower temperature = lower heat loss). Multiple-effect arrangements use the vapor from one effect as the heating steam for the next effect at lower pressure, recovering 60-80% of the latent heat. A single-effect evaporator requires approximately 1.1 kg steam per kg water evaporated; a triple-effect requires only 0.4 kg steam per kg evaporated.

Four main configurations serve chemical processing: **forced-circulation** (pump circulates liquid through a shell-and-tube heater, best for scaling and fouling fluids), **falling-film** (liquid flows as a thin film down the inside of heated tubes, best for heat-sensitive products), **long-tube vertical** (natural circulation in long tubes, simple and common), and **wiped-film/thin-film** (mechanical wiper spreads liquid into a thin film on a heated surface, for viscous and heat-sensitive materials).

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate](../metals/iron-steel.md) (vessel) | 200-3,000 kg | 316L SS (corrosive), carbon steel (non-corrosive), 6-12 mm | [Iron & Steel](../metals/iron-steel.md) | Titanium (high-chloride), Hastelloy (acid) |
| [Steel tubing](../metals/forming.md) | 100-1,000 kg | 316L SS tubes, 25-50 mm OD, 2-3 mm wall, 2-6 m long | [Forming](../metals/forming.md) | Copper-nickel (seawater service) |
| [Steel plate](../metals/iron-steel.md) (tubesheets) | 50-300 kg | 316L SS or CS, 25-40 mm thick | [Iron & Steel](../metals/iron-steel.md) | — |
| [Steel pipe](../metals/forming.md) (circulation pump) | 50-200 kg | 316L SS, sized for circulation rate | [Forming](../metals/forming.md) | — |
| [Circulation pump](../energy/hydraulics.md) | 1 unit | Centrifugal, corrosion-resistant, rated for boiling liquid | [Hydraulics](../energy/hydraulics.md) | — (natural circulation for simple types) |
| [Vacuum system](../gas-handling/vacuum.md) | 1 unit | Steam ejector or liquid-ring vacuum pump, to 50-200 mmHg | [Vacuum](../gas-handling/vacuum.md) | Water aspirator (limited vacuum) |
| [Insulation](../construction/building-materials.md) | 20-50 m² | Mineral wool 50-100 mm, aluminum cladding | [Construction](../construction/building-materials.md) | — |
| [Steam supply](../energy/coal.md) | — | 0.3-1.0 MPa saturated steam | [Coal](../energy/coal.md) | Hot oil (higher temperature), electric heating (small scale) |

## Construction Steps

### Forced-Circulation Evaporator

1. **Fabricate the vapor body**: Construct a vertical cylindrical vessel (0.5-3 m diameter, 2-5 m tall) from 316L stainless steel. This is the vapor-liquid separation space where boiling occurs. The vessel has a tangential feed inlet near the bottom (creates a swirling flow that aids vapor-liquid separation), a vapor outlet at the top, and a concentrated liquid outlet at the bottom. The top may be fitted with a demister pad (wire mesh, 100-150 mm thick) to remove entrained liquid droplets from the vapor.

2. **Construct the heater**: Build a shell-and-tube heat exchanger (per [Heat Exchanger](heat-exchanger.md)): 1-4 m² shell diameter, 2-6 m tube length, 100-1,000 tubes. Process liquid flows through the tubes; steam heats the shell side. Design for the heating duty: Q = m × ΔHvap × evaporation rate, where m is the evaporation rate (kg/h), ΔHvap is the latent heat of vaporization. Steam consumption ≈ 1.1 × evaporation rate for single-effect (includes heating feed to boiling point plus heat losses).

3. **Connect circulation loop**: Pipe the concentrated liquid from the vapor body bottom through the circulation pump, through the heater (tubes), and back to the vapor body feed inlet. The pump circulates liquid at 2-5 m/s tube velocity (high velocity prevents scale deposition and boiling in the tubes — boiling occurs only when the heated liquid enters the lower-pressure vapor body). Circulation rate: 3-10× the feed rate.

4. **Install vacuum system**: Connect the vapor outlet to a condenser (shell-and-tube, water-cooled) and a vacuum source. The condenser captures the evaporated solvent vapor for recovery. Non-condensable gases (air leaking into the system) are removed by the vacuum pump or steam ejector. Operating pressure: 50-200 mmHg absolute (typical), reducing boiling point from 100°C to 40-70°C depending on the product.

5. **Install feed and product connections**: Feed enters the circulation loop (or directly into the vapor body). Product (concentrated liquid) is withdrawn from the vapor body bottom at a rate that maintains the desired concentration. Install a sight glass on the vapor body for liquid level observation. Install a conductivity meter in the product line — conductivity increases with concentration and provides continuous concentration monitoring.

### Multiple-Effect Arrangement

6. **Arrange effects in series**: Connect the vapor outlet from the first effect (Effect 1) to the heater shell of the second effect (Effect 2). Effect 2 operates at lower pressure than Effect 1, so the vapor from Effect 1 (at temperature T₁) can boil the liquid in Effect 2 (at temperature T₂ < T₁). Effect 2 vapor feeds Effect 3 heater, and so on.

7. **Install inter-effect piping**: Each effect has its own vapor body, heater, and circulation loop. Vapor from Effect N feeds the heater of Effect N+1. Concentrated liquid flows from Effect 1 to Effect 2 to Effect N (forward feed) or vice versa (backward feed, for viscous products). Install transfer pumps between effects if gravity flow is insufficient.

8. **Install final condenser and vacuum**: The vapor from the last effect condenses in a final condenser (water-cooled shell-and-tube). The vacuum system pulls non-condensable gases from the last effect, maintaining the pressure cascade across all effects.

### Falling-Film Evaporator

9. **Construct the calandria (heating body)**: A single-pass shell-and-tube exchanger, mounted vertically, 3-8 m tube length. Liquid is distributed to the top of each tube and flows down the inside wall as a thin film (0.5-2 mm thick). Steam on the shell side heats the tube wall. The thin film provides excellent heat transfer (1,500-4,000 W/m²·K) with very short residence time (10-30 seconds) — ideal for heat-sensitive products (fruit juices, dairy, pharmaceutical extracts).

10. **Fabricate liquid distributor**: Install a distributor plate at the top of the calandria with precision holes or slots (1-3 mm diameter) feeding each tube. Uniform distribution is critical — a dry tube spot fouls rapidly. Verify distribution by running water through the distributor and observing flow from each tube.

## Calibration and Verification

1. **Heat balance test**: Run the evaporator at design conditions. Measure steam input (flow meter), feed rate, product rate, and vapor rate. Energy balance: steam heat input = feed heating + evaporation + heat losses. The balance should close within ±5%. Larger discrepancy indicates uninsulated surfaces, steam leaks, or instrumentation errors.

2. **Concentration test**: Feed a solution of known initial concentration. Measure product concentration (density meter or refractometer). Verify that the concentration ratio matches the volume reduction ratio: C_product / C_feed ≈ V_feed / V_product.

3. **Vacuum leak test**: Close all process connections. Pull vacuum to the design operating pressure. Close the vacuum valve. Monitor pressure rise for 30 minutes. Acceptable leak rate: <5% of operating pressure per 30 minutes. Higher rates indicate air leaks at flanges, valve packing, or instrument connections.

4. **Heat transfer coefficient verification**: Measure the overall heat transfer coefficient (U) during operation: U = Q / (A × LMTD). For forced-circulation: expected 1,500-3,000 W/m²·K (liquid to boiling liquid). For falling-film: 1,500-4,000 W/m²·K. If U is below 70% of design, suspect fouling on the tube side (scale, polymer deposits).

## Expected Performance

| Parameter | Single-Effect | Triple-Effect | Falling-Film |
|-----------|--------------|---------------|--------------|
| Steam consumption (kg steam / kg water evaporated) | 1.0-1.2 | 0.35-0.45 | 1.0-1.2 (single-effect) |
| Operating temperature | 50-120°C | 40-110°C (last to first effect) | 50-90°C (vacuum) |
| Operating pressure | 50-200 mmHg | 50-200 mmHg (last effect) to atmospheric (first) | 30-150 mmHg |
| Evaporation capacity | 100-10,000 kg/h | 500-50,000 kg/h | 500-30,000 kg/h |
| Heat transfer coefficient | 1,500-3,000 W/m²·K | 1,000-2,500 W/m²·K (per effect) | 1,500-4,000 W/m²·K |
| Residence time (process liquid) | 10-60 minutes | 30-120 minutes (total) | 10-30 seconds |
| Concentration ratio (product/feed) | 2-10× | 2-5× per effect | 2-8× |
| Energy consumption | 600-700 kWh/m³ water evaporated | 200-250 kWh/m³ | 600-700 kWh/m³ |

## Safety

- **Vacuum collapse**: The vapor body operates under vacuum. If the vacuum system fails and atmospheric pressure rushes in, the vessel can collapse inward if not designed for full external pressure. Design all vacuum vessels for full vacuum (external pressure collapse). Install vacuum relief valve.
- **Hot surfaces**: Steam-heated surfaces reach 100-180°C. Insulate all steam lines, heaters, and vapor body. Surface temperature <60°C. Emergency shower within 10 m.
- **Boiling liquid hazards**: The process liquid is at its boiling point. Flashing can occur at sample ports and drain valves. Use extended-stem valves to keep operators away from the flash point. Install splash guards on sample valves.
- **Chemical concentration**: As solvent evaporates, dissolved chemicals concentrate. Corrosive solutions become more corrosive; toxic solutions become more toxic. Verify materials of construction are compatible with the final product concentration, not just the feed.
- **Scale and fouling**: Mineral scale (CaCO₃, CaSO₄) deposits on heated tube surfaces reduce heat transfer and can block tubes. Schedule periodic chemical cleaning (acid wash for mineral scale, alkali wash for organic fouling). Monitor heat transfer coefficient — a 20% drop from baseline signals cleaning needed.

## Variations and Alternatives

- **Multiple-effect vs. mechanical vapor recompression (MVR)**: MVR compresses the overhead vapor to raise its condensation temperature, then uses it as the heating steam. MVR consumes electricity (compressor) instead of steam, achieving 10-20% of the energy cost of single-effect evaporation. Economical where electricity is cheaper than steam. See [Distillation](distillation.md) for MVR details.
- **Solar evaporation ponds**: The simplest evaporator — a shallow lined pond exposed to sunlight. Zero energy cost. Very slow (weeks to months). Requires large land area (5-20 m² per m³/year). Used for salt production, brine concentration, and mining leachate management. Not suitable for heat-sensitive, volatile, or valuable products.
- **Open-pan boiling**: Heat a shallow pan of liquid over a fire or steam coil. Simplest evaporator for small-scale operation (syrup production, salt making). No vacuum, no condenser. High energy cost. Product quality limited by high temperature.

## See Also

- [Heat Exchanger](heat-exchanger.md) — the heater component of an evaporator
- [Crystallizer](crystallizer.md) — evaporation to supersaturation for crystal formation
- [Distillation Column](distillation-column.md) — separation by boiling point (not concentration)
- [Water Treatment](water-treatment.md) — brine concentration for zero liquid discharge
- [Distillation](distillation.md) — multiple-effect distillation and MVR principles

[← Back to Chemistry](index.md)
