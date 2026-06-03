# Seed Press

> **Node ID**: food-processing.seed-press
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`food-processing.oil-processing`](oil-processing.md)
> **Enables**: [`chemistry.soap`](../chemistry/soap.md) (vegetable oil feedstock), village-scale oil extraction
> **Timeline**: Years 10-20
> **Outputs**: vegetable oil, press cake (animal feed)
> **Critical**: No — oil processing enhances food quality and enables soap, but basic nutrition has alternatives

## Principle

A seed press extracts oil from oilseeds (sunflower, rapeseed, sesame, flax, peanut) by applying high pressure to conditioned seed flakes, forcing the oil through a cage of bars or perforated plate while retaining the compressed meal (press cake) inside. Two designs serve bootstrap-scale production:

**Screw press (expeller)**: A rotating screw shaft with progressively decreasing channel depth forces seed material through a cylindrical cage of bars with narrowing gaps. The screw compresses the material progressively — pressure increases from the feed end (near atmospheric) to the discharge end (50-150 bar). Oil flows out through the cage bar gaps; compressed meal exits as a solid cake at the discharge choke. The screw both conveys and compresses, making it a continuous process: feed seed in one end, oil flows out the sides, cake exits the other.

**Hydraulic pack press**: Seed flakes wrapped in pressing cloth are stacked between plates in a vertical press. A hydraulic ram or screw mechanism applies pressure (50-100 bar) to the stack. Oil is squeezed through the cloth and runs down to a collection tray. Batch process — load, press, unload, repeat. Higher oil yield per press (up to 85% extraction) but slower and more labor-intensive than a screw press.

The screw press is the preferred design for bootstrap industrialization because it operates continuously and requires less manual handling.

## Prerequisites

- [Iron & Steel](../metals/iron-steel.md) — cast iron for the cage, forged steel for the screw shaft
- [Machine Tools](../machine-tools/index.md) — lathe for turning the screw shaft and boring the cage housing
- [Oil Processing](oil-processing.md) — seed preparation (cleaning, flaking, conditioning) procedures
- [Power source](../energy/index.md) — hand crank for small units, 2-5 kW motor or engine for production units

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel bar (screw shaft) | 20-50 kg | 1045 or 4140, 60-100 mm diameter × 500-800 mm long, hardened to 45-50 HRC | [Iron & Steel](../metals/iron-steel.md) | Cast iron screw (softer, shorter life) |
| Steel bars (cage) | 10-20 kg | 10-15 mm × 10-15 mm cross-section, 500-800 mm long, 20-30 pcs | [Iron & Steel](../metals/iron-steel.md) | Perforated steel plate (less drainage area) |
| Cast iron (housing) | 50-100 kg | Cage housing, feed hopper, frame | [Iron & Steel](../metals/iron-steel.md) | Welded steel plate (lighter) |
| Steel plate (end plates) | 10-20 kg | 10-15 mm thick, for cage end caps | [Iron & Steel](../metals/iron-steel.md) | None — structural |
| Bearings | 2-4 pcs | Heavy-duty journal bearings for screw shaft | [Bearings](../machine-tools/bearings-abrasives.md) | Bronze bushings with oil cups |
| Drive gears or pulleys | 1 set | Reduction ratio 10:1 to 20:1 (screw runs at 30-60 rpm) | [Iron & Steel](../metals/iron-steel.md) | Chain drive |
| Filter cloth | 2-5 m² | Fine linen or cotton for oil filtration | [Textiles](../textiles/weaving.md) | None — required for clean oil |

### Hydraulic Press Variant (Additional Materials)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (rams and plates) | 50-100 kg | 15-25 mm thick, 300-500 mm diameter | [Iron & Steel](../metals/iron-steel.md) | Cast iron plates (heavier, adequate) |
| Hydraulic cylinder | 1 pcs | 80-150 mm bore, 200-400 mm stroke, rated 20 MPa | [Machine Tools](../machine-tools/index.md) | Screw mechanism (slower, less controllable) |
| Pressing cloth bags | 10-20 pcs | Heavy canvas or linen, sized to plates | [Textiles](../textiles/weaving.md) | None — required |

## Construction Steps

### Screw Press (Expeller)

1. **Machine the screw shaft**: Turn a 60-100 mm diameter steel shaft on a lathe. Cut the screw flight (helical thread) with progressively decreasing channel depth from feed end to discharge end. Feed end channel depth: 20-30 mm. Discharge end channel depth: 3-8 mm. This compression ratio (3:1 to 6:1) generates the extraction pressure. The flight pitch remains constant (80-120 mm) while the root diameter increases toward the discharge. Hardened to 45-50 HRC to resist wear from abrasive seed particles.

2. **Machine the discharge choke**: Turn a conical choke (tapered nose) for the discharge end of the screw shaft. The choke restricts the exit opening, creating back-pressure that forces oil out through the cage bars. A narrower choke opening produces higher pressure but lower throughput. Make the choke adjustable (threaded into the end plate) so pressure can be varied for different seeds. Choke gap range: 1-5 mm.

3. **Fabricate the cage bars**: Cut 20-30 rectangular steel bars (10-15 mm × 10-15 mm × 500-800 mm long). Surface-harden the inner face (the face that contacts the seed material) to 50-55 HRC by flame hardening or case hardening. The cage bars are arranged in a circle around the screw shaft, held by the cage housing. The gaps between bars allow oil to escape while retaining the solid meal. Gap width: 0.15-0.30 mm at the feed end (wider), 0.10-0.20 mm at the discharge end (narrower). Insert thin steel shims between bars to set the gap.

4. **Assemble the cage**: Insert the cage bars into the housing — a two-piece cast iron cylinder split lengthwise for assembly access. Clamp the two halves around the bars with bolts. The bars must be held firmly — any movement under pressure allows meal to extrude through the gaps (blocking oil flow). Set gap shims at assembly. Verify gap uniformity by measuring at 4-6 points along the cage length with a feeler gauge.

5. **Install the screw shaft**: Insert the screw shaft through the cage. Mount the shaft in journal bearings at the feed end (thrust bearing to resist back-pressure) and discharge end. Check shaft-to-cage-bar clearance: 0.5-1.0 mm radial gap. Too tight and the screw bars contact the cage (metal-on-metal wear); too loose and meal bypasses without full compression.

6. **Mount the feed hopper**: Fabricate a sheet-metal or cast-iron hopper (200-300 mm square opening, tapering to match the feed end of the cage). Bolt the hopper to the cage housing above the feed opening. The hopper must hold enough seed for 5-10 minutes of continuous operation (5-15 kg capacity).

7. **Install the drive**: Mount a large pulley or gear on the screw shaft extension beyond the feed bearing. Connect via belt or chain to a reduction gearbox or direct motor drive. Screw speed: 30-60 rpm. Higher speed increases throughput but reduces oil yield (less time under pressure). A 5 kW motor driving a 15:1 reduction produces ~60 rpm at the screw with adequate torque (~800 N·m) for pressing.

8. **Install oil collection tray**: Fabricate a sheet-metal tray under the cage to collect oil flowing from the cage bar gaps. The tray should slope toward a drain spout leading to a collection container. Install a coarse screen (2-5 mm mesh) in the tray to catch large meal particles.

9. **Install cake discharge chute**: Fabricate a chute at the discharge end to guide the pressed cake (flat, dense discs or strips) into a collection bin. The cake exits hot (80-100°C from friction) — the chute must be metal, not wood.

### Hydraulic Pack Press (Alternative)

10. **Construct the frame**: Build an H-frame from steel plate (15-25 mm) or heavy timber. The frame must withstand the full ram force (50-150 kN) without deflection. Bolt or weld cross-members between the uprights to form the base and top plate.

11. **Prepare the press plates**: Cut 15-25 mm steel plates to 300-500 mm diameter (circular) or 300-400 mm square. Surface-grind flat within 0.1 mm. Drill drainage grooves (3-5 mm wide, 2-3 mm deep) in a radial pattern on the pressing face — these channels allow oil to flow to the plate edges.

12. **Assemble the hydraulic system**: Mount a hydraulic cylinder (80-150 mm bore, 20 MPa rated) on the top of the frame, ram pointing down. Connect a hand pump or powered pump to the cylinder. Install a pressure gauge (0-30 MPa range) in the hydraulic line. Set the relief valve to 20 MPa maximum working pressure.

13. **Prepare pressing cloths**: Cut heavy canvas or linen into circles or squares 50-100 mm larger than the press plates. Hem the edges. Each cloth holds one layer of conditioned seed flakes. The cloth contains the flakes while allowing oil to pass through.

## Calibration and Verification

1. **Screw clearance check**: Rotate the screw shaft by hand and listen for metal contact with the cage bars. Any scraping or metallic sound indicates insufficient clearance. Adjust bearing position to center the shaft. Verify radial clearance (0.5-1.0 mm) with feeler gauges through the bar gaps.

2. **Pressure test (screw press)**: Run the press with a small batch of conditioned seed. Measure oil flow rate and check that cake exits as a coherent strip, not as meal or paste. If cake is too wet (high residual oil), tighten the choke. If cake will not exit (stalling), open the choke. Target: cake residual oil 15-20% (single pressing), 8-12% (double pressing).

3. **Pressure test (hydraulic press)**: Load 5-10 kg of conditioned seed in cloth bags between plates. Apply pressure gradually to 10 MPa over 5 minutes, then to 20 MPa over the next 5 minutes. Hold at 20 MPa for 15-30 minutes. Measure oil yield by weight. Target: 60-80% of available oil extracted.

4. **Temperature check**: The screw press generates friction heat. Measure cake temperature at the discharge — target 80-100°C. Above 120°C, oil darkens and develops off-flavors. Reduce screw speed or increase cooling if temperature is excessive.

## Expected Performance

### Screw Press (Expeller)

| Parameter | Value |
|-----------|-------|
| Throughput (seed) | 5-20 kg/hour (small expeller), 1-10 tonnes/day (industrial) |
| Oil yield | 60-80% of available oil (single pressing) |
| Pressing pressure | 50-150 bar |
| Screw speed | 30-60 rpm |
| Cake residual oil | 15-20% (single pressing), 8-12% (double pressing) |
| Power consumption | 2-5 kW (small), 50-200 kW (industrial) |
| Cake exit temperature | 80-100°C |
| Screw shaft life | 2,000-5,000 hours before resurfacing (abrasive seeds wear faster) |
| Cage bar life | 3,000-8,000 hours |

### Hydraulic Pack Press

| Parameter | Value |
|-----------|-------|
| Throughput (seed) | 50-200 kg/batch (3-5 batches/day) |
| Oil yield | 70-85% of available oil |
| Pressing pressure | 50-100 bar |
| Press cycle time | 20-40 minutes per batch |
| Cake residual oil | 10-18% |
| Power consumption | Hand pump: human labor; powered pump: 1-3 kW |
| Cloth life | 50-100 batches (before replacement) |

## Strengths

- Screw press operates continuously — feed seed in, oil flows out, no stopping to load/unload
- Handles all common oilseeds (sunflower, rapeseed, sesame, peanut, flax) with the same machine
- Press cake byproduct contains 30-45% protein — valuable as animal feed (dual revenue stream)
- Hydraulic press achieves higher extraction yield (up to 85%) with simpler construction

## Weaknesses

- Screw shaft and cage bars require hardened steel to withstand 50-150 bar pressure and abrasive seed particles
- Single pressing leaves 15-20% residual oil in cake — double pressing or solvent extraction needed for higher yield
- Heat from friction (80-100°C) degrades heat-sensitive nutrients (vitamin E, polyphenols) in the oil
- Screw press requires precise gap setting (0.10-0.30 mm) — too wide leaks meal, too narrow blocks oil flow

## Safety

- **High pressure**: The screw press develops 50-150 bar. Never open the cage housing while the machine is running or pressurized. Hydraulic presses at 20 MPa can cause catastrophic failure of improperly maintained components.
- **Hot cake and oil**: Cake exits at 80-100°C, oil at 60-90°C. Wear leather gloves when handling. Hot oil splashes cause severe burns.
- **Entanglement**: The screw shaft rotates with significant torque (500-1000 N·m). Guard the drive mechanism. Loose clothing or hair caught in the feed hopper is drawn into the screw — install a feed grate across the hopper opening.
- **Fire hazard**: Oil and oil-laden dust are flammable. Oil fires burn at 300-400°C. Keep a lid or fire blanket nearby for smothering. Never use water on an oil fire.
- **Press cake self-heating**: Stacked press cake can self-heat from residual microbial activity. Spread in thin layers (<1 m deep) to cool before storage. Process within 1-2 weeks.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low oil yield | Insufficient pressure, seed not conditioned, or choke too wide | Tighten choke to increase back-pressure. Verify seed moisture 8-10% and conditioning temperature 60-90°C. |
| Cake too oily (>20% residual) | Insufficient pressure or seed not properly conditioned | Increase screw compression ratio. Condition at 70-90°C before pressing. Consider double pressing. |
| Press stalls (motor trips) | Choke too tight, foreign object in cage, or seed too wet | Open choke slightly. Clear any obstruction. Dry seed to 8-10% moisture. |
| Oil dark or burnt-smelling | Excessive pressing temperature (>120°C) | Reduce screw speed. Add cooling jacket around cage (water circulation). Reduce seed feed rate. |
| Meal extruding through cage gaps | Cage bar gaps too wide or bars shifted | Replace gap shims with thinner ones. Re-tighten cage housing bolts. Check for shifted bars. |
| Screw shaft scoring | Contact with cage bars from shaft misalignment | Re-align shaft in bearings. Check thrust bearing for wear. Re-machine scored shaft areas. |

## See Also

- [Oil & Fat Processing](oil-processing.md) — complete oil processing workflow, seed preparation, refining
- [Metals](../metals/iron-steel.md) — steel for screw shafts and cage bars
- [Machine Tools](../machine-tools/index.md) — precision machining for screw and cage components
- [Chemistry: Soap](../chemistry/soap.md) — vegetable oil as soap-making feedstock
- [Hydraulics](../energy/hydraulics.md) — hydraulic press principles
- [Dairy Processing](dairy.md) — butter and ghee as alternative cooking fats

[← Back to Food Processing](index.md)
