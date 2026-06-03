# Heat Exchanger

> **Node ID**: chemistry.heat-exchanger
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`metals.forming`](../metals/forming.md), [`metals.welding`](../metals/welding.md)
> **Enables**: [`chemistry.distillation`](distillation.md), [`chemistry.chemical-recovery`](chemical-recovery.md), [`energy.geothermal`](../energy/geothermal.md)
> **Timeline**: Years 15-25
> **Outputs**: heat_transfer
> **Critical**: No — heat exchangers improve energy efficiency and process control but simpler alternatives (direct-fired heating, air cooling) can substitute at lower efficiency

## Principle

A heat exchanger transfers thermal energy between two fluid streams at different temperatures without allowing the fluids to mix. A solid wall (metal tube or plate) separates the hot and cold fluids; heat flows through the wall by conduction. The rate of heat transfer is governed by Q = U × A × LMTD, where Q is heat duty (W), U is the overall heat transfer coefficient (W/m²·K), A is the heat transfer surface area (m²), and LMTD is the log mean temperature difference (K) between the two streams.

Two principal configurations dominate industrial practice: **shell-and-tube** (one fluid inside a bundle of tubes, the other fluid in the surrounding shell) and **plate** (fluids flow between alternating corrugated plates). Shell-and-tube exchangers handle higher pressures (up to 300 bar) and temperatures (up to 600°C); plate exchangers offer higher heat transfer coefficients (3,000-7,000 W/m²·K vs. 300-1,500 W/m²·K for shell-and-tube) in a more compact footprint but are limited to moderate pressures (<25 bar) and temperatures (<200°C).

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel pipe](../metals/forming.md) (tubes) | 50-500 kg | 316L SS or carbon steel, 19-25 mm OD, 1.5-2.5 mm wall | [Forming](../metals/forming.md) | Copper-nickel (seawater), titanium (highly corrosive) |
| [Steel plate](../metals/iron-steel.md) (shell) | 100-500 kg | Carbon steel A516 Gr.70, 6-12 mm thick | [Iron & Steel](../metals/iron-steel.md) | Stainless steel (corrosive shell-side fluid) |
| [Steel plate](../metals/iron-steel.md) (tubesheets) | 20-100 kg | Forged or rolled, 25-50 mm thick | [Iron & Steel](../metals/iron-steel.md) | Clad tubesheet (carbon steel + stainless cladding) |
| [Steel plate](../metals/iron-steel.md) (baffles) | 10-50 kg | Carbon steel or stainless, 3-6 mm thick | [Iron & Steel](../metals/iron-steel.md) | — |
| [Stainless steel plates](../metals/iron-steel.md) | 50-200 kg | 316L, 0.5-1.0 mm thick, corrugated (plate type only) | [Iron & Steel](../metals/iron-steel.md) | Titanium plates (seawater desalination) |
| [Gaskets](../polymers/elastomers.md) | 1 set | EPDM or NBR (plate type); PTFE (shell-and-tube flanges) | [Elastomers](../polymers/elastomers.md) | Viton (high temperature) |
| [Welding consumables](../metals/welding.md) | 5-30 kg | E7018 (CS) or E316L-16 (SS) | [Welding](../metals/welding.md) | — |
| [Bolts](../metals/fasteners.md) | 10-50 kg | ASTM A193 B7/B8 | [Fasteners](../metals/fasteners.md) | — |

## Construction Steps

### Shell-and-Tube Heat Exchanger

1. **Design the exchanger**: Determine heat duty (Q), hot and cold stream flow rates, inlet and outlet temperatures, and allowable pressure drop. Calculate LMTD for counter-current or cross-flow arrangement. Select tube size (19 mm OD is standard), tube length (2-6 m), number of tube passes (1, 2, or 4), and shell diameter. Calculate required heat transfer area: A = Q / (U × LMTD). Number of tubes = A / (π × OD × L). Typical U values: 300-800 W/m²·K for liquid-liquid, 800-1,500 W/m²·K for condensing vapor-liquid, 30-300 W/m²·K for gas-gas.

2. **Drill tubesheets**: Cut two circular tubesheets (25-50 mm thick) from forged steel plate. Mark and drill tube holes on triangular or square pitch (pitch = 1.25-1.5 × tube OD). Hole diameter = tube OD + 0.2-0.4 mm for roller expansion. For a 500 mm shell diameter with 19 mm tubes on 25 mm triangular pitch: approximately 150-200 tube holes.

3. **Prepare tubes**: Cut heat exchanger tubes to design length (2-6 m). Deburr both ends. Inspect each tube for defects (eddy current testing or visual). 316L stainless tubes for corrosive service; carbon steel for non-corrosive service (water, steam, hydrocarbons).

4. **Assemble tube bundle**: Insert tubes through both tubesheets. Expand (roll) each tube into the tubesheet holes using a mechanical tube expander: insert the expander mandrel, rotate to expand the tube wall outward into firm contact with the tubesheet bore. Roller expansion creates a pressure-tight joint without welding. For higher-pressure service (>20 bar), weld each tube to the front tubesheet (tube-to-tubesheet weld) using orbital TIG welding.

5. **Install baffles**: Cut semicircular baffles (segmental type, 3-6 mm thick, cutout = 20-35% of shell diameter) from steel plate. Slide baffles onto the tubes at regular intervals (baffle spacing = 0.2-1.0 × shell diameter). Baffles support the tube bundle, prevent tube vibration, and direct shell-side fluid to flow across the tubes (cross-flow) rather than along them. Secure baffles with tie rods and spacer sleeves.

6. **Fabricate shell**: Roll a cylindrical shell from steel plate. Weld the longitudinal seam. Cut openings for shell-side inlet and outlet nozzles. The shell inside diameter must be 3-6 mm larger than the outer tube limit (OTL — the circle circumscribing all tubes) for bundle insertion.

7. **Assemble exchanger**: Slide the completed tube bundle (tubesheets + tubes + baffles) into the shell. Bolt the front and rear heads (channel covers) to the tubesheets with gaskets. The front head directs tube-side fluid into the tubes; the rear head collects tube-side fluid and may provide a return path for multi-pass arrangements.

8. **Hydrostatic test**: Fill the shell side with water. Pressurize to 1.5× design pressure. Hold 30 minutes. Inspect all tube-to-tubesheet joints for leaks (weeping). Zero leaks acceptable. Repeat for the tube side. If tubes leak at the roller-expanded joint, re-roll or weld.

### Plate Heat Exchanger

9. **Fabricate plates**: Stamp or press corrugated plates (316L stainless, 0.5-1.0 mm thick) in a chevron or washboard pattern. Corrugation depth 2-5 mm, creating turbulent flow channels when plates are stacked. Punch inlet and outlet port holes at the four corners of each plate.

10. **Install gaskets**: Bond EPDM or NBR gaskets into the peripheral groove on each plate. Gaskets seal the plate edges and port holes, directing the two fluids into alternate channels. The gasket pattern alternates between plates to separate hot and cold streams.

11. **Stack plates**: Stack 20-200 plates between two thick end plates (carbon steel, 15-25 mm). Align port holes. Insert alignment guide pins.

12. **Compress stack**: Tighten tie rods to compress the plate pack. The compression force squeezes the gaskets to form tight seals. Measure the compressed pack dimension — it must match the design value within ±2 mm. Over-compression damages gaskets; under-compression causes leaks.

13. **Pressure test**: Pressurize each fluid channel separately with water at 1.5× design pressure. Inspect for cross-leakage between channels (indicates damaged gasket or plate). Zero cross-contamination acceptable.

## Calibration and Verification

1. **Heat transfer test**: Flow hot water (60-80°C) on one side and cold water (15-25°C) on the other at design flow rates. Measure inlet and outlet temperatures on both sides with calibrated thermometers (±0.1°C). Calculate actual heat duty: Q = m × Cp × ΔT for both streams (energy balance must close within ±5%). Calculate actual U value: U = Q / (A × LMTD). Compare to design value; accept if within ±15%.

2. **Pressure drop test**: Measure pressure drop on both sides at design flow rate. Compare to design calculation. Excessive pressure drop indicates fouling, debris, or incorrect baffle/plate installation.

3. **Leak test**: After thermal testing, re-pressurize both sides. Check for cross-contamination by sampling the cold outlet for hot-side fluid markers.

## Expected Performance

| Parameter | Shell-and-Tube | Plate |
|-----------|---------------|-------|
| Heat transfer coefficient (liquid-liquid) | 300-1,500 W/m²·K | 3,000-7,000 W/m²·K |
| Maximum pressure | 10-300 bar | 10-25 bar |
| Maximum temperature | 600°C | 180°C (gasket limit) |
| Surface area per unit | 2-500 m² | 1-200 m² |
| Footprint (per m² area) | Large | Compact (3-5× smaller) |
| Cleanability | Mechanical cleaning of shell side; chemical cleaning of tube side | Open for mechanical cleaning of all plates |
| Typical approach temperature | 5-15°C | 1-3°C |
| Service life (gaskets) | 5-10 years (flange gaskets) | 2-5 years (plate gaskets) |
| Service life (tubes/plates) | 10-30 years | 10-20 years |

## Strengths

- **Shell-and-tube**: Handles extreme pressures and temperatures; rugged construction tolerates thermal shock and vibration; tube bundles can be pulled for cleaning and repair; standardized designs (TEMA classification) with 100+ years of engineering practice.
- **Plate**: Very high heat transfer coefficients in a compact package; approach temperatures as low as 1°C (excellent for heat recovery); easy to expand capacity by adding plates; all heat transfer surfaces accessible for cleaning.

## Weaknesses

- **Shell-and-tube**: Lower heat transfer coefficient than plate type (requires more area); shell-side fouling difficult to clean mechanically; limited to single tube pass or fixed multi-pass; tube vibration can cause fatigue failure at flow velocities >2 m/s shell-side.
- **Plate**: Limited to moderate pressure and temperature by gasket capability; gaskets are a recurring maintenance cost; plate corrosion or cracking causes cross-contamination; cannot handle fluids containing fibrous or large particulate matter (blocks channels).

## Safety

- **Thermal shock**: Rapid temperature changes create differential expansion between tubes and shell, stressing tube-to-tubesheet joints. Limit temperature ramp rates to 50°C/hour for startup and shutdown. Install expansion joints on fixed-tubesheet exchangers.
- **High-pressure fluid**: Shell-and-tube exchangers at 50+ bar contain significant stored energy. Pressure relief on both shell and tube sides. Never open a flanged connection while under pressure.
- **Cross-contamination**: Tube or plate failure allows hot and cold streams to mix. For hazardous fluids (toxic, flammable), install conductivity or pH monitors on the low-pressure outlet to detect leaks early. Double tubesheet construction prevents cross-contamination for critical applications.
- **Gasket failure (plate type)**: Gasket blowout at overpressure releases both fluids simultaneously. Pressure relief valves on both fluid ports. Secondary containment under plate exchangers handling hazardous fluids.

## See Also

- [Distillation Column](distillation-column.md) — condenser and reboiler are shell-and-tube heat exchangers
- [Reactor Vessel](reactor-vessel.md) — jacket heat transfer design
- [Evaporator](evaporator.md) — heat exchanger used for evaporation duty
- [Distillation](distillation.md) — heat integration and pinch analysis

[← Back to Chemistry](index.md)
