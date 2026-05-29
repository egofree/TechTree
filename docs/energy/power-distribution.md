# Transformer & Power Distribution

> **Node ID**: energy.power-distribution
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.electricity`](electricity.md), [`machine-tools`](../machine-tools/index.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`energy.electricity.power-systems`](electricity.md), [`electronics.electrical-systems`](../electronics/electrical-systems.md), [`telecom`](../telecom/index.md)
> **Timeline**: Years 15-30
> **Outputs**: distribution_transformers, power_transformers, substations, switchgear, distribution_panels, instrument_transformers
> **Critical**: Yes — Without transformers, AC power distribution beyond 1-2 km is impractical. No long-distance transmission means no centralized generation means no industrial-scale power.


Transformers are the enabling technology for alternating-current power distribution. They convert voltage levels with no moving parts — stepping generator output up to thousands of volts for efficient long-distance transmission, then stepping back down to safe utilization voltages at the point of use. Without transformers, every electrical load must be within 1-2 km of its generator, making centralized power generation useless and forcing every factory to operate its own power plant.

The physics is simple: two coils of wire on a shared iron core. Alternating current in the primary coil creates a changing magnetic flux in the core, which induces a voltage in the secondary coil. The voltage ratio equals the turns ratio — double the turns, double the voltage. Power is conserved minus a few percent loss. This elegant device, combined with three-phase AC generation, forms the backbone of every electrical grid from the 1880s to the present day.

This document covers transformer construction, core and winding manufacturing, insulation systems, oil-filled and dry-type designs, substation layout, switchgear, distribution panels, and the quantitative parameters needed to specify, build, and test power distribution equipment at workshop scale.


## Materials

- **Copper wire** — Drawn from electrorefined copper (99.99% purity). Magnet wire from 0.05 mm to 5.0 mm diameter with enamel insulation. See [Wire Drawing](electricity.md).
- **Silicon steel sheet** — 3-4% silicon-iron alloy, 0.23-0.50 mm thick, for laminated cores. Reduces eddy current losses. See [Iron & Steel](../metals/iron-steel.md).
- **Insulation materials** — Kraft paper (0.05-0.25 mm), pressboard (1-3 mm), varnish (shellac or synthetic), enamel for magnet wire. Higher temperature classes use mica, glass fiber, or silicone. See [Polymers](../polymers/thermoplastics.md).
- **Transformer oil** — Refined mineral oil (flash point >140°C, dielectric strength >30 kV/mm). Provides both electrical insulation and convective cooling.
- **Steel plate** — For transformer tanks, radiators, and structural supports. 3-12 mm thick.
- **Porcelain insulators** — For bushings and terminal connections. See [Ceramics](../ceramics/kilns.md).

## Tools and Equipment

- **Lathe and milling machine** — For core clamping hardware, bushing fabrication, tank fabrication. See [Machine Tools](../machine-tools/index.md).
- **Winding machine** — Hand-cranked or motor-driven mandrel for winding coils. Torque control maintains even tension.
- **Sheet metal shear and brake** — For cutting and bending core laminations and tank components.
- **Oven or kiln** — For core annealing (800-850°C to relieve stresses and develop grain orientation) and drying insulation (110-130°C to remove moisture before oil filling).
- **Megger (insulation resistance tester)** — 500-5000V DC test set. See [Electrical Instruments](../measurement/electrical-instruments.md).
- **Multimeter, ammeter, voltmeter** — For turns ratio verification, load testing, loss measurement.

## Knowledge

- AC circuit theory (voltage, current, impedance, power factor, three-phase systems)
- Magnetic circuit concepts (flux, permeability, saturation, hysteresis)
- Basic trigonometry for three-phase voltage calculations


## Distribution Transformer (100 kVA, 11 kV / 400V, Three-Phase)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Silicon steel sheet (0.3 mm, 3% Si) | 280-320 kg | [Iron & Steel](../metals/iron-steel.md) — cold-rolled grain-oriented | Hot-rolled non-oriented (50% higher core loss) |
| Copper magnet wire (enamel, 0.5-3.0 mm) | 85-110 kg | [Electrolysis](../chemistry/electrolysis.md) → [Wire Drawing](electricity.md) | Aluminum wire (larger cross-section needed, 60% conductivity of copper) |
| Copper bus bar / flat strap | 8-12 kg | [Wire Drawing](electricity.md) | Aluminum bus bar |
| Kraft paper insulation | 12-18 kg | [Forestry](../plants/index.md) — chemical pulping | Cotton or synthetic paper |
| Pressboard (1-3 mm) | 5-8 kg | [Chemistry](../chemistry/index.md) — cellulose processing | Phenolic laminate |
| Transformer oil | 180-250 liters | [Petroleum](../chemistry/petroleum-alternatives.md) — refined mineral oil | Silicone fluid (higher fire point, 3-5× cost) or dry-type air-cooled (no oil) |
| Steel plate (3-6 mm, tank) | 120-160 kg | [Iron & Steel](../metals/iron-steel.md) | Cast iron tank (heavier, brittle) |
| Porcelain bushings (4 off) | 4 pcs | [Ceramics](../ceramics/kilns.md) | Epoxy resin bushings (lower voltage rating) |
| Varnish / impregnating resin | 5-8 liters | [Chemistry](../chemistry/index.md) | Shellac (lower temperature class) |
| Hardware (bolts, clamps, gaskets) | 10-15 kg | [Metals](../metals/index.md) | — |


## Core Construction

1. **Cut laminations** to shape using sheet metal shear or stamping die. Standard shapes: E-I (shell type) or U-I (core type). For a 100 kVA core-type transformer, each lamination is approximately 600 mm × 150 mm for the legs and 600 mm × 100 mm for the yokes. Tolerance: ±0.5 mm on length, ±0.1 mm on width.

2. **Deburr** all cut edges with a file or abrasive paper. Burrs create electrical shorts between laminations, causing eddy current hot spots.

3. **Apply insulation coating** to each lamination if not pre-coated. Dip in varnish (phenolic or epoxy), drain excess, bake at 150-200°C for 30-60 minutes. Coating thickness: 5-15 μm per side. Alternatively, use pre-coated steel with inorganic phosphate or oxide coating from the steel mill.

4. **Stack laminations** in the core frame, alternating the overlap pattern by one lamination per layer (two-over-two or three-over-three pattern). This eliminates air gaps at the joints — each joint is bridged by the overlapping layer. Tighten clamping bolts to 20-30 Nm, maintaining uniform pressure across the core cross-section.

5. **Anneal the assembled core** (if grain-oriented steel is not available): heat to 800-850°C in a reducing atmosphere (to prevent oxidation), hold 2-4 hours, cool slowly at 50°C/hour to below 200°C. This relieves mechanical stresses from cutting and improves magnetic permeability by 20-40%.

**Materials**:
- [Silicon steel sheet](../metals/iron-steel.md) (0.3 mm thick, 3% Si, 280-320 kg for 100 kVA core)
- [Phenolic or epoxy varnish](../chemistry/index.md) (5-10 liters for lamination coating)
- [Core clamping bolts](../metals/index.md) (M12-M16, grade 8.8, 8-16 pieces with flat washers)
- [Kraft paper strips](../plants/index.md) (0.1-0.25 mm thick, for inter-lamination insulation if uncoated)

**Calibration / Verification**:
1. Measure each lamination's dimensions with calipers: length ±0.5 mm, width ±0.1 mm tolerance. Out-of-spec laminations cause uneven stacking.
2. Test inter-lamination resistance: stack 10 laminations under 20 N load, apply 500V DC across the stack. Leakage current must be <1 mA (indicates adequate insulation between laminations).
3. After annealing, measure core loss with a no-load test: apply rated voltage to the primary winding and measure watts consumed (target: core loss within ±10% of design — 220-320 W for 100 kVA).
4. Verify core dimensions: stack height, leg width, and window opening must match design within ±1 mm.

**Expected Performance**:
- Core loss: 220-320 W for 100 kVA transformer (constant regardless of load)
- Magnetic flux density: 1.5-1.7 Tesla at rated voltage
- No-load exciting current: 1-3% of rated current
- Annealing improvement: 20-40% reduction in core loss vs. unannealed

**Strengths**:
- Step-by-step process achievable with sheet metal shear and hand tools
- Annealing improves core quality by 20-40%, allowing use of non-grain-oriented steel
- Laminated core design eliminates eddy currents that would waste energy as heat
- Standardized lamination shapes (E-I, U-I) simplify cutting and stacking

**Weaknesses**:
- Annealing requires a furnace capable of 850°C in reducing atmosphere — not trivial
- Tight tolerances (±0.1 mm on width) demand precision cutting tools
- Core stacking is labor-intensive — 4-8 hours for a 100 kVA core
- Burrs from imprecise cutting create inter-lamination shorts, increasing core loss

## Winding

6. **Calculate turns** for primary and secondary windings. For 11 kV / 400V step-down: turns ratio = 11,000 / 400 = 27.5:1. If secondary has 40 turns per phase, primary needs 1,100 turns per phase. Volts per turn = 400 / 40 = 10 V/turn.

7. **Select wire gauge** based on current. Secondary full-load current at 400V: 100,000 / (√3 × 400) = 144A. At 3 A/mm², need 48 mm² cross-section. Use multiple parallel conductors or flat copper strap (e.g., 6 mm × 8 mm = 48 mm²). Primary current: 144 / 27.5 = 5.2A. At 3 A/mm², need 1.7 mm² — use 1.5 mm diameter wire (1.77 mm²).

8. **Wind secondary (low voltage)** first on the core leg using the winding machine. Layer-wound: wind turns in even layers with kraft paper insulation (0.1 mm) between layers. Keep winding tension constant at 10-20 N to avoid loose or overtight turns. Secure end turns with cotton tape.

9. **Apply major insulation** between secondary and primary — wrap with multiple layers of pressboard (total 2-4 mm) and kraft paper, secured with cotton tape. This barrier must withstand the full 11 kV test voltage.

10. **Wind primary (high voltage)** over the insulation barrier. Layer-wound with 0.1 mm kraft paper between each layer. At 1,100 turns and ~100 turns per layer, expect ~11 layers. Provide tapping points at ±2.5% and ±5% of rated voltage by bringing out looped turns at calculated positions (typically at turns 1,045 and 1,055 for ±5%).

11. **Secure and tie** all windings with cotton or glass tape at regular intervals (every 50-100 mm). Apply varnish by brushing or dipping. Bake at 110-130°C for 4-8 hours to cure varnish and drive out moisture.

**Materials**:
- [Copper magnet wire](../chemistry/electrolysis.md) (enamel-insulated, 0.5-3.0 mm diameter, 85-110 kg for 100 kVA)
- [Flat copper strap](electricity.md) (6 mm × 8 mm or similar, for secondary winding, 8-12 kg)
- [Kraft paper insulation](../plants/index.md) (0.05-0.25 mm thick, 12-18 kg for layer insulation)
- [Pressboard](../chemistry/index.md) (1-3 mm thick, 5-8 kg for major insulation barrier)
- [Varnish/impregnating resin](../chemistry/index.md) (5-8 liters, shellac or synthetic)
- [Cotton or glass tape](../textiles/index.md) (25 mm wide, 100-200 m for tying and securing)

**Calibration / Verification**:
1. Count turns on a test winding before committing to full production. Verify volts-per-turn ratio: apply 100V AC to the primary, measure secondary voltage. Ratio must match design within ±0.5%.
2. Measure DC resistance of each completed winding with a Kelvin bridge. Compare phases: all three must match within 2%.
3. Perform insulation resistance test between primary and secondary: apply 2,500V DC (megger). Minimum acceptable: 50 MΩ at room temperature before varnish impregnation.
4. Measure winding dimensions: build-up (radial thickness) and axial height must be within ±2 mm of design to fit in the core window.

**Expected Performance**:
- Winding resistance: primary 1.5-3.0 Ω, secondary 0.01-0.05 Ω (varies by design)
- Full-load copper loss: 1,700-2,300 W for 100 kVA transformer
- Current density: 3 A/mm² (oil-filled), 2-2.5 A/mm² (dry-type)
- Insulation class: Class A (105°C) or Class B (130°C) depending on varnish and paper grade

**Strengths**:
- Well-defined calculation procedure (turns ratio, wire gauge) reduces design errors
- Layer-wound construction provides predictable voltage distribution and good heat dissipation
- Tap changers (±2.5%, ±5%) allow output voltage adjustment in the field
- Varnish impregnation solidifies windings, improving mechanical strength and heat transfer

**Weaknesses**:
- Winding 1,100 turns of primary wire is slow and tedious (4-12 hours per phase)
- Constant tension (10-20 N) must be maintained — loose turns vibrate and abrade insulation
- Insulation defects between layers cause partial discharge that degrades transformer over time
- Copper wire is expensive and heavy — 85-110 kg for a single 100 kVA transformer

## Assembly and Tanking

12. **Mount core and coil assembly** on the tank base using steel clamps and insulated tie rods. Ensure the core is level and centered.

13. **Connect leads** from winding terminals to bushing terminals. Use copper bus bar or heavy-gauge wire with adequate clearance (minimum 25 mm/kV creepage distance in air, 6 mm/kV in oil). Solder or bolt connections using tin-plated copper lugs.

14. **Install bushings** in the tank cover. Porcelain bushings seal with rubber gaskets. Verify alignment and tightness.

15. **Attach radiator fins** (welded steel or bolted-on panel radiators) for oil cooling. Surface area: approximately 5-8 m² per 100 kVA of losses.

16. **Weld or bolt the tank cover** in place with oil-resistant gasket (cork-rubber or nitrile rubber). Install oil drain valve, sampling valve, and pressure relief device.

17. **Dry the assembly** before oil filling. Heat the completed transformer in an oven at 90-110°C for 24-48 hours (longer for larger units). Monitor insulation resistance — it should exceed 1,000 MΩ before oil filling. Alternatively, circulate hot dry air through the tank.

18. **Fill with transformer oil** under vacuum if possible (removes air bubbles from insulation, extends oil life). Fill rate: slow, to allow air to escape. Fill to the marked oil level on the sight glass.

19. **Seal and allow oil to impregnate** the paper and pressboard insulation for 24-48 hours before testing. Oil penetrates cellulose insulation, dramatically increasing dielectric strength.

**Materials**:
- [Transformer oil](../chemistry/petroleum-alternatives.md) (refined mineral oil, flash point >140°C, 180-250 liters for 100 kVA)
- [Steel plate](../metals/iron-steel.md) (3-6 mm thick, 120-160 kg for tank fabrication)
- [Porcelain bushings](../ceramics/index.md) (4 pieces, rated for 11 kV, creepage distance ≥275 mm)
- [Cork-rubber or nitrile gasket](../polymers/index.md) (oil-resistant, 5-10 m for tank cover and bushing seals)
- [Pressure relief device](../metals/index.md) (spring-loaded vent, set to 0.35-0.7 bar gauge)
- [Radiator fins](../metals/iron-steel.md) (welded steel panels, 5-8 m² surface area per 100 kVA losses)

**Calibration / Verification**:
1. Perform turns ratio test: apply 100V AC to primary, measure secondary voltage. Ratio must match nameplate within ±0.5% (for 27.5:1 ratio: 100V input → 3.636V ±0.018V output).
2. Insulation resistance test (megger): apply 2,500V DC between primary-secondary, primary-ground, secondary-ground. Minimum: 50 MΩ at room temperature. Polarization index (10 min / 1 min resistance) must be >2.0.
3. Oil dielectric breakdown test: sample oil from the drain valve, test in a standard cup with 2.5 mm gap. Raise voltage at 2 kV/s until breakdown. Minimum acceptable: 30 kV (new oil tests at 40-50 kV).
4. Load test (heat run): energize at full rated current for 8-24 hours. Monitor top-oil temperature rise (target: ≤55°C for 65°C rise class). Verify no leaks at gaskets, valves, or bushings.
5. Measure no-load and full-load losses. Compare to design specification: core loss 220-320 W, copper loss 1,700-2,300 W for 100 kVA.

**Expected Performance**:
- Total losses at full load: 1,920-2,620 W (1.9-2.6% of 100 kVA rating)
- Efficiency at 50% load: 98.8%, at 100% load: 98.0%
- Temperature rise: 50-65°C above ambient at full load
- Oil dielectric strength: >30 kV in 2.5 mm gap (new oil: 40-50 kV)
- Audible noise: 50-65 dB at 1 m distance (from magnetostriction in core)

**Strengths**:
- Oil provides both electrical insulation and convective cooling in one medium
- Sealed tank protects windings from moisture, dust, and mechanical damage
- Pressure relief device prevents tank rupture during internal faults
- Oil impregnation of paper insulation increases dielectric strength by 5-10× over dry paper

**Weaknesses**:
- Mineral oil is flammable (flash point 140-160°C) — creates fire risk if tank ruptures
- Oil filling and vacuum processing require specialized equipment (vacuum pump, oil filtration unit)
- Drying cycle (90-110°C for 24-48 hours) adds significant production time
- Oil must be tested periodically — moisture and dissolved gases degrade insulation over time


## Standard Distribution Transformer Ratings

| Rating (kVA) | HV Range (kV) | LV Range (V) | Core Loss (W) | Load Loss at 75°C (W) | Total Loss (% of rating) | Oil Volume (liters) | Weight (kg) |
|-------------|---------------|--------------|---------------|----------------------|------------------------|--------------------:|------------:|
| 10 | 2.4-11 | 120-240 | 50-80 | 250-350 | 3.0-4.0 | 40-60 | 150-200 |
| 25 | 2.4-11 | 120-240 | 90-130 | 550-750 | 2.5-3.5 | 80-120 | 280-380 |
| 50 | 4.16-11 | 240-415 | 140-200 | 950-1,300 | 2.2-3.0 | 120-180 | 420-580 |
| 100 | 4.16-11 | 240-415 | 220-320 | 1,700-2,300 | 1.9-2.6 | 180-250 | 650-900 |
| 200 | 4.16-11 | 240-415 | 350-500 | 2,800-3,800 | 1.6-2.2 | 280-400 | 1,100-1,500 |
| 315 | 4.16-11 | 415 | 480-700 | 3,800-5,200 | 1.4-1.9 | 380-520 | 1,500-2,000 |
| 500 | 4.16-11 | 415 | 650-950 | 5,200-7,200 | 1.2-1.6 | 500-700 | 2,000-2,800 |
| 1000 | 4.16-11 | 415 | 1,000-1,500 | 8,500-12,000 | 1.0-1.4 | 800-1,200 | 3,200-4,500 |

Core loss is constant (present whenever the transformer is energized). Load loss (copper I²R loss) varies with the square of the load. Total loss at full load: typically 1.0-4.0% of rated power. A 100 kVA transformer at full load wastes ~2 kW as heat.

## Wire Gauge vs Current Capacity for Transformer Windings

| Wire Diameter (mm) | Cross-Section (mm²) | Resistance (Ω/km) | Current Capacity 3 A/mm² (A) | Typical Application |
|--------------------|---------------------|--------------------|------------------------------|-------------------|
| 0.5 | 0.20 | 88 | 0.6 | Instrument transformers, metering |
| 0.8 | 0.50 | 35 | 1.5 | Small control transformers |
| 1.0 | 0.79 | 22 | 2.4 | HV windings of small transformers |
| 1.5 | 1.77 | 9.9 | 5.3 | HV windings of distribution transformers |
| 2.0 | 3.14 | 5.6 | 9.4 | HV windings, larger units |
| 3.0 | 7.07 | 2.5 | 21 | LV windings, medium transformers |
| 4.0 | 12.6 | 1.4 | 38 | LV windings, larger transformers |
| 5.0 | 19.6 | 0.9 | 59 | LV windings, high-current secondaries |
| Flat 3×10 | 30 | 0.58 | 90 | LV bus, small distribution |
| Flat 5×15 | 75 | 0.23 | 225 | LV bus, 200+ kVA transformers |
| Flat 6×25 | 150 | 0.12 | 450 | LV bus, 500+ kVA transformers |

Current density of 3 A/mm² is standard for oil-filled transformers with moderate temperature rise (55-65°C). Dry-type transformers use 2-2.5 A/mm² due to less effective air cooling. Increase current density to 4-5 A/mm² for intermittent duty or forced-cooled designs.

## Voltage Drop in Distribution Feeders

| Wire Size (mm²) | Resistance (Ω/km) | Max Current (A) | Voltage Drop per 100m at Max Current, 240V 1-Phase (%) | Max Recommended Run at Max Current (m) |
|-----------------|--------------------|-----------------|-------------------------------------------------------|--------------------------------------|
| 2.5 | 7.0 | 20 | 11.7% | 25 |
| 4.0 | 4.4 | 30 | 8.8% | 35 |
| 6.0 | 2.9 | 40 | 7.3% | 40 |
| 10 | 1.75 | 60 | 6.6% | 50 |
| 16 | 1.10 | 85 | 5.9% | 60 |
| 25 | 0.70 | 110 | 4.8% | 80 |
| 35 | 0.50 | 140 | 4.4% | 90 |
| 50 | 0.35 | 175 | 3.9% | 100 |
| 70 | 0.25 | 220 | 3.5% | 120 |
| 95 | 0.18 | 270 | 3.1% | 140 |
| 120 | 0.14 | 310 | 2.7% | 160 |

Formula: Voltage drop (%) = (2 × I × R × L) / V × 100, where I = current (A), R = resistance per km (Ω), L = one-way length (km), V = supply voltage (V). Factor of 2 accounts for outgoing and return conductors. For three-phase, replace factor 2 with √3 and use line-to-line voltage.

## Transformer Losses by Size

| Rating (kVA) | No-Load Loss (W) | Full-Load Loss (W) | Efficiency at 50% Load (%) | Efficiency at 100% Load (%) | Temperature Rise (°C) |
|-------------|------------------|--------------------|---------------------------|-----------------------------|-----------------------|
| 25 | 110 | 660 | 98.5 | 97.4 | 45-55 |
| 50 | 170 | 1,100 | 98.7 | 97.8 | 45-60 |
| 100 | 270 | 2,000 | 98.8 | 98.0 | 50-60 |
| 200 | 420 | 3,300 | 99.0 | 98.4 | 50-65 |
| 500 | 800 | 6,500 | 99.1 | 98.7 | 55-65 |
| 1000 | 1,250 | 10,500 | 99.2 | 98.9 | 55-65 |

Maximum efficiency occurs when core loss equals copper loss. For a 100 kVA transformer with 270 W core loss and 2,000 W full-load copper loss: optimal load = √(270/2000) = 0.37 = 37% of rated load. Distribution transformers spend most of their life below 50% load, so design favors lower core loss.


## Bench Scale (1-5 kVA)

A 1 kVA transformer for laboratory or instrument use fits in one hand. Core cross-section: 10-20 cm². Wire: 0.3-1.0 mm diameter. Air-cooled, no oil needed. Hand-wound on a simple mandrel. Construction time: 2-4 hours. Test with a multimeter and variac. Useful for power supplies, isolation, and instrument matching.

## Workshop Scale (10-100 kVA)

A 100 kVA pole-mounted or pad-mounted distribution transformer weighs 650-900 kg and requires mechanical assistance for winding (motorized winding machine) and handling (hoist, crane). Core stacking by hand takes 4-8 hours. Winding takes 4-12 hours per phase. Oil filling and curing adds 48 hours. Requires oven for drying, vacuum pump for oil impregnation (optional but strongly recommended).

## Production Scale (500-10,000 kVA)

Power transformers at this scale require automated core cutting (CNC notch-cutting machine), automated winding machines with precision layering, vapor-phase drying ovens (heating under vacuum with solvent vapor for thorough moisture removal), and oil processing plants (degassing, dehydration, filtration to <1 μm particle size). Tank welding requires certified welders and radiographic inspection of seams. Factory production: 2-20 units per month depending on size. Not achievable in early bootstrap — these are purchased or imported once the economy can support specialized transformer manufacturers.

## Key Scale Breakpoints

- **5 kVA**: Hand-buildable by one person with basic tools. Dry-type. No oil.
- **100 kVA**: Maximum practical hand-built size. Requires hoist, oven, oil handling. Oil-filled.
- **500 kVA**: Requires mechanized winding, proper drying oven, and oil filtration equipment.
- **5,000 kVA+**: Requires purpose-built factory with overhead cranes (10-50 tonne capacity), vacuum drying ovens, and oil processing systems.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| High no-load loss (core loss >110% of expected) | Lamination burrs causing eddy current shorts, or inadequate annealing | Deburr all lamination edges; anneal core at 800-850°C; check inter-lamination resistance (>1 Ω per lamination pair) |
| Overheating under load (temperature rise >65°C) | Undersized conductor, high resistance joints, or blocked oil flow | Check wire gauge matches design current density; inspect all bolted/soldered joints; verify radiator fins are clear and oil circulates freely |
| Buzzing or vibrating core | Loose clamping bolts, or insufficient core pressure | Tighten all core clamping bolts uniformly; add additional clamping points; pad joints with varnish-impregnated paper |
| Low insulation resistance (<100 MΩ) | Moisture in insulation or oil | Dry transformer at 90-110°C for 24-48 hours; test oil dielectric strength (>30 kV/mm); replace oil if contaminated |
| High voltage breakdown during test | Insufficient insulation between windings, or voids in insulation | Increase pressboard barrier thickness; ensure thorough varnish impregnation; vacuum-fill with oil to eliminate air pockets |
| Uneven voltage between phases (three-phase) | Unequal turns count, or asymmetric core leg dimensions | Count and verify turns on each phase; measure core leg cross-sections — must be equal within 1% |
| Oil discoloration or acidic smell | Oil oxidation from moisture and heat exposure | Test oil acidity (neutralization number <0.05 mg KOH/g oil); filter or replace oil; check tank seal for water ingress |
| Audible partial discharge (crackling) | Air bubbles trapped in oil or insulation | Degas oil under vacuum; circulate oil to release trapped air; maintain positive oil pressure |


## High Voltage Hazards

Distribution transformers operate at voltages from 2.4 kV to 34.5 kV on the primary side. These voltages are lethal — 1 mA through the chest causes muscle contraction, 100 mA causes ventricular fibrillation, and contact with 11 kV produces tens of amperes through the body. Treat all transformer terminals as energized until proven de-energized with a voltage detector rated for the voltage class.

## Oil Fire Risk

Transformer mineral oil has a flash point of 140-160°C and an auto-ignition point of 280-330°C. An internal fault (short circuit between windings) can generate arc temperatures of 3,000-8,000°C, decomposing oil into hydrogen and acetylene gas. If pressure builds faster than the relief valve can vent, the tank ruptures and the oil ignites. A 100 kVA transformer holds ~200 liters of oil — equivalent to ~6 GJ of combustion energy.

**Mitigations:**
- Install pressure relief devices (bursting disc or spring-loaded vent) on all oil-filled transformers. Set to vent at 0.35-0.7 bar gauge.
- Position transformers outdoors or in dedicated vaults with 3 m clearance from combustible materials.
- Provide gravel-lined oil containment pit (capacity = 110% of oil volume) to capture and quench burning oil that leaks from a ruptured tank.
- Never open an energized oil-filled transformer. De-energize, ground, and verify zero voltage before any internal access.

## Arc Flash

Secondary-side short circuits on a transformer fed by a stiff grid can produce arc currents of 10-50 kA. Incident energy at 0.5 m distance can exceed 20 cal/cm² — enough to ignite clothing and cause third-degree burns. Arc-rated PPE (face shield, coverall, gloves) is mandatory when opening or racking switchgear connected to a transformer secondary.

## Electrical Testing Safety

Insulation resistance testing (megger) applies 500-5,000V DC. Never touch terminals during a test. Discharge the winding to ground through a resistor after each test — stored charge can deliver a dangerous shock.


## Turns Ratio Test

Apply low AC voltage (e.g., 100V) to the primary. Measure secondary voltage. Calculate turns ratio: V_primary / V_secondary. Compare to design ratio. Acceptance: ±0.5% of nameplate ratio. A 27.5:1 transformer at 100V input should read 3.636V ±0.018V on the secondary. This test confirms correct winding turns before oil filling and energization.

## Insulation Resistance Test (Megger Test)

Apply 1,000V DC (for transformers up to 1 kV rating) or 2,500-5,000V DC (for higher voltage ratings) between primary and secondary, primary and ground, secondary and ground. Minimum acceptable values:

| Operating Voltage | Test Voltage (DC) | Minimum Insulation Resistance |
|-------------------|-------------------|-------------------------------|
| <1 kV | 1,000V | 1 MΩ per kV + 1 MΩ (minimum 2 MΩ) |
| 1-2.5 kV | 2,500V | 50 MΩ |
| 2.5-5 kV | 5,000V | 100 MΩ |
| 5-15 kV | 5,000V | 200 MΩ |

Measure polarization index (PI): resistance at 10 minutes / resistance at 1 minute. PI >2.0 = good insulation. PI 1.5-2.0 = marginal. PI <1.5 = deteriorated insulation — do not energize.

## Oil Dielectric Breakdown Test

Place oil sample in a standard test cup with two spherical electrodes, 2.5 mm gap. Raise AC voltage at 2 kV/s until breakdown occurs. Minimum acceptable: 30 kV (new oil tests at 40-50 kV). Test three times; discard the first result (electrode conditioning), average the next two. Low breakdown voltage indicates moisture, particles, or dissolved gases. Remediate with filtration (1-5 μm filter) and vacuum degassing.

## Winding Resistance Test

Measure DC resistance of each winding with a Kelvin bridge or micro-ohmmeter. Compare phases — three-phase windings must match within 2%. Excessive resistance indicates undersized conductor, poor joints, or loose connections.

## Load Test (Heat Run)

Energize transformer at full rated current for 8-24 hours. Monitor top-oil temperature rise. Acceptance: temperature rise ≤55°C for 65°C rise class (oil-filled), measured by thermocouple in top oil. If temperature exceeds limit, reduce loading rating or improve cooling.


## Oil-Filled vs Dry-Type

| Parameter | Oil-Filled | Dry-Type (Cast Resin) |
|-----------|-----------|----------------------|
| Voltage range | Up to 500+ kV | Up to 35 kV (typically ≤15 kV) |
| Rating range | 10 kVA to 1,000+ MVA | 30 kVA to 30 MVA |
| Efficiency | 98-99.5% | 97-98.5% |
| Fire risk | Mineral oil is combustible | Non-combustible (epoxy/silicone resin) |
| Indoor installation | Requires vault with fire suppression | Direct indoor installation |
| Maintenance | Oil testing, filtering, degassing | Minimal (visual inspection, cleaning) |
| Cost | Lower | 30-80% higher |
| Weight | Heavier (oil + tank) | Lighter (no oil, no tank) |
| Noise | 50-65 dB | 55-70 dB (louder, less damping) |

Oil-filled transformers are the default for all outdoor and high-voltage applications. Dry-type (cast coil) transformers use windings encapsulated in epoxy resin, cooled by air. Dry-type is preferred for indoor installations (office buildings, factories) where oil fire risk is unacceptable.

## Core Geometries

- **Core type**: Windings surround the core legs. Simpler construction, easier to insulate HV windings, better cooling (windings exposed). Standard for distribution transformers.
- **Shell type**: Core surrounds the windings. Lower leakage flux, better magnetic shielding, but more complex core stacking. Used for some specialty and furnace transformers.
- **Toroidal**: Continuous ring core with windings wrapped around it. No air gap in the core → very low magnetizing current and low stray field. Limited to smaller ratings (typically <10 kVA) because the core must be wound through the completed winding — the wire must be passed through the core ring turn by turn.

## Autotransformer

A single winding with a tap point serves as both primary and secondary. The common section carries the difference between input and output current, so the autotransformer is physically smaller and cheaper than a two-winding transformer of the same rating. Caveat: no electrical isolation between primary and secondary. A fault on the HV side appears directly on the LV side. Use only where isolation is provided elsewhere (e.g., motor starting, voltage adjustment within ±20%).

## Instrument Transformers

- **Current transformer (CT)**: Produces secondary current proportional to primary current. Typical ratio: 100:5A. Secondary must never be open-circuited while primary carries current — open secondary develops dangerous high voltage (kV range). Always short the secondary terminals before disconnecting the burden.
- **Potential transformer (PT)**: Steps down voltage for metering. Typical ratio: 11,000:110V. Accuracy: ±0.3-1.0%. Used for watt-hour meters, protective relays, and voltage indicators.

## See Also

- **[Electricity Generation & Distribution](electricity.md)** — generators, AC/DC systems, wire drawing, transmission line design. This document is the parent capability.
- **[Electrical Systems](../electronics/electrical-systems.md)** — wiring, switches, breakers, panelboards, power electronics, and motor control. Complements this document with secondary-side distribution details.
- **[Energy Storage & Diversification](storage.md)** — grid infrastructure, UPS systems, and backup generation that interface with power distribution.
- **[Electrical Insulation Classes](electricity.md)** — thermal class ratings (Class A through H) for transformer insulation life calculations.
- **[Wire Drawing](electricity.md)** — copper wire production process and gauge reference tables used in transformer winding.
- **[Iron & Steel](../metals/iron-steel.md)** — silicon steel production for transformer cores, steel plate for tanks and structural components.
- **[Ceramics](../ceramics/kilns.md)** — porcelain insulator and bushing production.
- **[Polymers](../polymers/thermoplastics.md)** — insulation materials (PVC, XLPE, epoxy resin, varnish).
- **[Lubricants](../chemistry/lubricants.md)** — transformer oil specification, testing, and filtration.
- **[Measurement Instruments](../measurement/electrical-instruments.md)** — megger, multimeter, power analyzer for transformer testing.



[← Back to Energy](index.md)
