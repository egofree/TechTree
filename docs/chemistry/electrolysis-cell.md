# Electrolysis Cell

> **Node ID**: chemistry.electrolysis-cell
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`energy.electricity`](../energy/electricity.md), [`chemistry.electrolysis`](electrolysis.md)
> **Enables**: [`chemistry.alkalis`](alkalis.md), [`metals.aluminum`](../metals/aluminum.md), [`chemistry.hydrogen-silane`](hydrogen-silane.md)
> **Timeline**: Years 15-30
> **Outputs**: chlorine, hydrogen, caustic_soda, aluminum
> **Critical**: Yes — the chlor-alkali cell produces chlorine, hydrogen, and NaOH simultaneously, enabling PVC production, HCl synthesis, semiconductor-grade hydrogen, and aluminum smelting. Electrolysis cells are among the most electricity-intensive industrial equipment.

## Principle

An electrolysis cell drives a non-spontaneous chemical reaction by applying direct current (DC) electricity between two electrodes immersed in an electrolyte. The anode (positive electrode) oxidizes species (loses electrons), while the cathode (negative electrode) reduces species (gains electrons). The minimum voltage required equals the thermodynamic reversible potential (determined by the Nernst equation), plus overpotentials for activation kinetics, concentration polarization, and resistive losses in the electrolyte and electrodes.

For the chlor-alkali process: 2NaCl + 2H₂O → Cl₂ + H₂ + 2NaOH. The reversible potential is approximately 2.2V at 25°C. Actual operating voltage is 3.2-3.8V per cell due to overpotentials and ohmic losses. Current efficiency (fraction of current producing desired product) is 90-97%. Energy consumption: 2,100-2,500 kWh per tonne of Cl₂ produced.

Individual cells operate at 3-4V but draw 5-200 kA current. Cells are stacked in electrical series (50-200 cells) to match available DC supply voltage (200-400V). This bipolar filter-press configuration is the standard industrial arrangement.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate](../metals/iron-steel.md) (cell body) | 100-1,000 kg | Carbon steel, 6-12 mm thick | [Iron & Steel](../metals/iron-steel.md) | Concrete (large stationary cells), fiberglass (corrosive) |
| [Graphite electrodes](../metals/iron-steel.md) | 50-500 kg | Electrode grade, 50-100 mm thick × 300-600 mm wide | [Carbon Products](../mining/index.md) | DSA (Ti + RuO₂/IrO₂, 5-8 year life vs 2-5 kg C/tonne Cl₂ for graphite) |
| [Nickel electrodes](../metals/iron-steel.md) | 20-200 kg | Nickel-plated steel or pure Ni sheet | [Iron & Steel](../metals/iron-steel.md) | Steel cathode (adequate for chlor-alkali) |
| [Diaphragm or membrane](../polymers/elastomers.md) | 1-20 m² | Asbestos fiber (diaphragm) or ion-exchange membrane (Nafion type) | [Polymers](../polymers/elastomers.md) | Polymer fabric (polypropylene) for water electrolysis |
| [Copper bus bar](../metals/iron-steel.md) | 50-500 kg | Electrolytic tough pitch copper, sized for current density <1.5 A/mm² | [Iron & Steel](../metals/iron-steel.md) | Aluminum bus (lighter but higher resistance) |
| [EPDM rubber gaskets](../polymers/elastomers.md) | 1 set | 3-6 mm thick, die-cut to cell frame shape | [Elastomers](../polymers/elastomers.md) | Neoprene (lower temperature limit) |
| [Bolts and tie rods](../metals/fasteners.md) | 50-200 kg | Stainless steel 316, sized for compression force | [Fasteners](../metals/fasteners.md) | — |
| [Titanium mesh](../metals/iron-steel.md) | 10-100 kg | Expanded or woven, for DSA substrate | [Iron & Steel](../metals/iron-steel.md) | — (only for DSA anodes) |
| [DC power supply](../energy/electricity.md) | 1 unit | Thyristor or IGBT rectifier, 100-400V, 5-200 kA | [Electricity](../energy/electricity.md) | Motor-generator set (older technology) |

## Construction Steps

### Chlor-Alkali Diaphragm Cell

1. **Fabricate cell body**: Weld a rectangular steel tank (1-2 m wide × 0.5-1 m deep × 2-3 m long) from 6-12 mm carbon steel plate. The cell must be electrically insulated from ground — mount on ceramic or rubber insulators. Weld internal brackets for electrode mounting and diaphragm support. Install brine inlet, Cl₂ outlet (anode side), H₂ outlet and NaOH outlet (cathode side) nozzles.

2. **Prepare cathode assembly**: Fabricate a perforated steel mesh or screen (2-3 mm wire, 3-5 mm openings) sized to fit inside the cell body as a vertical divider. This mesh serves as both cathode (where H₂ evolves and NaOH forms) and diaphragm support. Weld a steel frame around the mesh perimeter for structural support.

3. **Deposit asbestos diaphragm**: Prepare an asbestos fiber slurry (10-20 g/L in water). Place the cathode mesh in a vacuum chamber. Draw the asbestos slurry through the mesh by applying vacuum on one side. Asbestos fibers deposit on and within the mesh to form a 1-3 mm thick permeable layer. The diaphragm allows Na⁺ ions and water to pass but retards OH⁻ back-migration and prevents Cl₂/H₂ mixing. Cure at 100-120°C. Diaphragm life: 6-12 months before replating.

4. **Install anodes**: Mount graphite anode plates (50-100 mm thick, 300-600 mm wide, 600-1,200 mm tall) on copper bus bars inside the anode compartment. Multiple plates in parallel. Anode spacing: 10-20 mm from diaphragm surface. Alternative: mount DSA anodes (titanium mesh coated with RuO₂/IrO₂ mixed metal oxide, 5-15 μm coating) for longer life (5-8 years vs. graphite consumption at 2-5 kg per tonne Cl₂).

5. **Assemble cell**: Place the cathode-diaphragm assembly inside the cell body, dividing it into anode and cathode compartments. Install gaskets between the cathode frame and the cell body flanges. Bolt the cell cover in place. Ensure all gas passages are sealed — Cl₂ and H₂ must never mix (explosive at 4-93% H₂ in Cl₂).

6. **Connect electrical bus**: Weld copper bus bars to the anode mounting frame (positive terminal) and the cathode mesh (negative terminal). Size bus bars for the design current: cross-section (mm²) = current (A) / 1.5 (A/mm² maximum current density for copper). Connect to the DC power supply via flexible braided copper jumpers.

### Alkaline Water Electrolysis Cell

7. **Fabricate electrode plates**: Cut nickel-plated steel or pure nickel plates (1-3 mm thick, 200-1,000 mm square or rectangular) to serve as bipolar electrodes. In a bipolar stack, each plate is the cathode of one cell on one face and the anode of the adjacent cell on the other face. Drill or punch flow channels for electrolyte and gas passage.

8. **Prepare electrolyte**: Dissolve KOH (potassium hydroxide) in deionized water to 25-30% concentration (specific gravity 1.23-1.28). KOH is preferred over NaOH for water electrolysis because it has higher conductivity. The electrolyte is not consumed — only water is split.

9. **Assemble filter-press stack**: Stack alternating electrode plates and diaphragm separators (asbestos cloth, polypropylene fabric, or polysulfone membrane, 0.5-2 mm thick) between two thick steel end plates. Insert EPDM gaskets between each plate and diaphragm to seal the electrolyte channels. Compress the entire stack with tie rods through the end plates. Tighten in cross-pattern to achieve uniform gasket compression.

10. **Connect electrolyte manifolds**: Pipe the KOH electrolyte to feed manifolds on the stack. Each cell in the stack receives electrolyte in parallel. Gas outlets at the top of each cell carry H₂ (cathode side) and O₂ (anode side) to separate gas-liquid separators.

11. **Install gas-liquid separators**: Two vertical steel tanks (one for H₂, one for O₂) separate gas from entrained electrolyte. Gas rises to the top and exits through a demister pad (removes KOH mist). Liquid KOH returns to a circulation tank and is pumped back to the stack. Electrolyte circulation removes waste heat and maintains concentration.

### Commissioning

12. **Pressure test**: Fill all compartments with water. Pressurize to 1.5× design pressure. Hold 30 minutes. Inspect all gaskets, welds, and connections. Zero leaks acceptable. For electrolysis cells, even small leaks allow gas mixing — this is a critical safety hazard.

13. **Electrolyte fill**: Fill with process electrolyte (saturated brine for chlor-alkali, 25-30% KOH for water electrolysis). Purge all air from the system with nitrogen before applying voltage.

14. **Apply voltage at low current**: Energize the DC supply at 20-50% of rated current. Verify gas production at both electrodes: Cl₂ (greenish-yellow, pungent) at the anode, H₂ (colorless, flammable) at the cathode for chlor-alkali; H₂ at the cathode, O₂ at the anode for water electrolysis. Verify gas purity by sampling.

15. **Ramp to full current**: Increase current to design value over 1-4 hours while monitoring cell voltage, current, temperature, and gas production rate. Cell voltage should stabilize at 3.2-3.8V (chlor-alkali) or 1.8-2.2V (water electrolysis) per cell.

## Calibration and Verification

1. **Current efficiency**: Measure actual Cl₂ or H₂ production rate (gas flow meter). Calculate theoretical production: Faraday's law — 1 Faraday (96,485 C) produces 1 equivalent of product. Current efficiency = actual production / theoretical production × 100%. Acceptable: 90-97%. Below 85% indicates side reactions, diaphragm failure, or short circuits.

2. **Cell voltage monitoring**: Record voltage across each cell in the stack at operating current. All cells should be within ±0.1V of the average. A cell with significantly higher voltage has higher resistance (scale, blockage, electrode damage) and will overheat. A cell with significantly lower voltage may be short-circuited (diaphragm failure, gas mixing).

3. **Gas purity test**: Sample H₂ from the cathode and Cl₂ or O₂ from the anode. H₂ purity must be >99.5% (main impurity: O₂ traces). Cl₂ purity must be >97% (main impurities: O₂, CO₂, H₂). Gas mixing is an immediate safety hazard — shut down if H₂ appears in the Cl₂/O₂ stream above 2%.

## Expected Performance

| Parameter | Chlor-Alkali Diaphragm | Chlor-Alkali Membrane | Alkaline Water |
|-----------|----------------------|----------------------|----------------|
| Cell voltage | 3.5-4.0V | 3.0-3.5V | 1.8-2.2V |
| Current density | 1-3 kA/m² | 2-5 kA/m² | 2-4 kA/m² |
| Current efficiency | 90-95% | 93-97% | 95-99% |
| Energy consumption | 2,300-2,800 kWh/t Cl₂ | 2,100-2,500 kWh/t Cl₂ | 50-55 kWh/kg H₂ |
| Operating temperature | 80-90°C | 80-90°C | 60-90°C |
| NaOH concentration (product) | 10-12% (requires evaporation) | 30-35% (direct use) | N/A |
| Electrode life | Graphite: continuous consumption; DSA: 5-8 years | DSA: 5-8 years | Nickel: 10+ years |
| Diaphragm/membrane life | 6-12 months (asbestos) | 2-4 years (Nafion) | 5-10 years (polymer fabric) |
| Cells per stack | 10-100 | 10-100 | 50-200 |

## Safety

- **Chlorine gas**: Cl₂ is toxic (IDLH 10 ppm, immediately dangerous to life and health). Yellow-green gas, heavier than air, causes severe respiratory damage. Continuous Cl₂ monitoring with alarm at 1 ppm. Emergency scrubbing system (NaOH circulation tower) to neutralize any Cl₂ release. Full-face respirator with acid gas cartridges available at all cell room exits.
- **Hydrogen gas**: H₂ forms explosive mixtures with air at 4-75% concentration. Ignition energy as low as 0.02 mJ. Ventilate cell rooms to keep H₂ below 1% (25% of LEL). Bond and ground all metal. Explosion-proof electrical equipment. Never allow H₂ and Cl₂ or O₂ to mix.
- **High DC voltage**: Stacks at 200-400V DC present electrocution hazard. Insulate all bus bars and connections. Lockout/tagout before any cell maintenance. Use insulated tools. Post warning signs.
- **Caustic burns**: NaOH at 10-35% causes severe skin and eye burns. Chemical-resistant gloves, face shield, apron. Eyewash and safety shower within 10 seconds travel.
- **Asbestos handling**: Diaphragm cells use asbestos fiber — a known carcinogen. Use respirator with P100 filter during diaphragm deposition and replacement. Wet methods to suppress dust. Enclosed vacuum system for fiber handling.

## Variations and Alternatives

- **Membrane cell**: Replaces the asbestos diaphragm with an ion-exchange membrane (perfluorinated sulfonic acid, 100-200 μm thick). Produces 30-35% NaOH directly (no evaporation needed). Lower energy consumption (2,100-2,500 vs. 2,300-2,800 kWh/t Cl₂). Requires ultra-pure brine (Ca²⁺, Mg²⁺ <20 ppb). The membrane itself requires fluoropolymer chemistry (Nafion) — not available until the polymer industry is mature.
- **PEM electrolysis**: Proton exchange membrane replaces liquid KOH electrolyte. Higher current density (5-20 kA/m²), more compact, >99.99% H₂ purity. Requires Nafion membrane and platinum catalyst — not bootstrap-appropriate until fluoropolymer chemistry is established.
- **Hall-Héroult aluminum cell**: A specialized electrolysis cell operating at 950-1000°C in molten cryolite (Na₃AlF₆). Carbon anodes consumed as reactant. 4.0-4.5V per cell, 150-400 kA. See [Electrolysis](electrolysis.md) for detailed Hall-Héroult cell construction.

## See Also

- [Electrolysis](electrolysis.md) — electrochemical theory and all process variants
- [Alkalis](alkalis.md) — NaOH and KOH production and uses
- [Hydrogen and Silane](hydrogen-silane.md) — hydrogen purification and semiconductor applications
- [SEM Tech](sem-tech.md) — low-cost ion exchange membrane manufacturing

[← Back to Chemistry](index.md)
