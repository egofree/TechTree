# Soldering Iron

> **Node ID**: electronics.soldering-iron
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`energy.electricity`](../energy/electricity.md), [`ceramics.insulators`](../ceramics/index.md)
> **Enables**: [`electronics.assembly`](assembly.md), [`electronics.electrical-systems`](electrical-systems.md)
> **Timeline**: Years 15-25
> **Outputs**: soldered_joints, reworked_assemblies
> **Critical**: Yes — no electronic circuit can be assembled or repaired without a reliable heat source for soldering; the soldering iron is the single most essential tool in electronics

## Overview

A soldering iron converts electrical energy into heat at a concentrated tip, raising the temperature of metal workpieces and solder alloy above the solder's melting point. The molten solder wets the metal surfaces through metallurgical bonding — a thin intermetallic layer (1-5 μm) forms between the solder and the base metal, creating both electrical continuity and mechanical attachment. The iron maintains tip temperature at 320-420°C, well above the melting points of common solders (Sn63/Pb37: 183°C; SAC305 lead-free: 217-220°C), providing sufficient thermal headroom to overcome heat sinking by the workpiece and PCB substrate.

Heating is achieved by passing current through a resistive element (nichrome wire or ceramic PTC heater) embedded in the iron body. The thermal mass of the tip stores heat and delivers it to the joint in a brief 2-5 second contact. Temperature-controlled irons use a thermocouple or thermistor in the tip, feeding back to a power controller (triac or MOSFET) that maintains the set temperature within ±5-10°C.

Position in the dependency chain: the soldering iron depends on [Iron & Steel](../metals/iron-steel.md) for the body and structural components, [Electricity](../energy/electricity.md) for the power source, and [Ceramics](../ceramics/index.md) for the insulating tube. It enables [Electronics Assembly](assembly.md) (PCB soldering, rework, and prototyping) and [Electrical Systems](electrical-systems.md) (wiring harness construction, connector attachment, and power distribution assembly). Without a reliable soldering heat source, electronics manufacturing is limited to mechanical connections (screw terminals, crimps) that are bulkier, less reliable, and unsuitable for PCB assembly.

## Prerequisites

- [Electricity](../energy/electricity.md) — 120 V or 230 V AC supply (or 12-24 V DC for low-voltage irons)
- [Iron & Steel](../metals/iron-steel.md) — steel tube for body, iron plating for tips
- [Copper](../metals/copper.md) — copper rod for tip stock (thermal conductivity 401 W/m·K)
- [Ceramics](../ceramics/index.md) — alumina or mullite tube for heater insulation
- [Nichrome wire](../metals/alloys.md) — NiCr 80/20 resistance wire for the heating element
- [Wire drawing](../machine-tools/machining.md) — for producing nichrome wire and copper wire
- [Electroplating](../electrochemistry/electroplating.md) — optional, for iron-plating tips to extend life

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Copper rod (tip) | 1 piece, 30-60 mm × 6-10 mm | OFHC copper, >99.9% purity | [Electrolysis](../chemistry/electrolysis.md) | Copper-clad steel (lower thermal conductivity) |
| Nichrome wire (heater) | 0.5-1.0 m | NiCr 80/20, 28-34 AWG (0.16-0.32 mm), resistance 6-15 Ω/m | [Wire drawing](../machine-tools/machining.md) | Kanthal A1 (higher temperature rating) |
| Ceramic tube (insulator) | 1 piece, 40-70 mm | Alumina or mullite, ID 4-8 mm, OD 8-14 mm, rated >500°C | [Ceramics](../ceramics/index.md) | Mica sheet wrapped in layers (fragile) |
| Steel tube (body) | 1 piece, 80-120 mm | Mild steel or stainless, ID 10-16 mm, wall 1-2 mm | [Iron & Steel](../metals/iron-steel.md) | Brass tube (softer, conducts heat to handle) |
| Wooden or phenolic handle | 1 piece | Hardwood (oak, beech) or [phenolic resin](../polymers/thermosets.md), 80-120 mm, turned to 20-30 mm diameter | [Foundations](../foundations/tools-basic.md) | Ceramic handle (heavier) |
| Power cord | 1-2 m | Stranded copper, 18-20 AWG, with [PVC insulation](../polymers/thermoplastics.md), rated 300V, 3A minimum | [Electrical Systems](electrical-systems.md) | Cloth-insulated wire (less safe) |
| Iron-plating for tip | Optional | Electroplated iron, 50-150 μm over copper core | [Electroplating](../electrochemistry/electroplating.md) | Bare copper tip (wears faster, needs frequent dressing) |
| Stainless steel set screw | 1-2 | M3 or M4, for securing tip and electrical connection | [Iron & Steel](../metals/iron-steel.md) | Split collar clamp |

## Process Description

### Tip Geometry and Selection

The tip shape determines how effectively heat transfers to the joint. Three primary geometries cover most soldering tasks:

- **Chisel tip** (4-5 mm wide, 1-2 mm thick): the most versatile. The flat face contacts both the component lead and the PCB pad simultaneously, maximizing thermal transfer area. Used for through-hole soldering, tinning wires, and general-purpose work. Tip temperature distribution: 340-380°C at the flat face, dropping to 280-320°C at the edges.
- **Conical tip** (1-2 mm diameter, pointed): for precision work on small components (SOT-23, 0805 passives). The small contact area limits heat transfer — only suitable for joints with low thermal mass. Requires higher iron temperature (380-420°C) to compensate for reduced contact area.
- **Bevel tip** (3-4 mm wide, 30° angle): combines the contact area of a chisel with the access of a conical. Useful for drag-soldering multi-pin ICs and for soldering in confined spaces.

### Basic Soldering Iron Construction (Uncontrolled, 25-40 W)

1. **Form the copper tip**: Turn or file the copper rod to the desired tip shape. A chisel tip (4-5 mm wide, 1-2 mm thick at the business end) is the most versatile. The shank end (10-15 mm) should be a sliding fit inside the ceramic insulator. Clean the copper to bare metal with abrasive paper.
2. **Wind the heater element**: Measure the required resistance for the target wattage at your supply voltage. For a 40 W iron on 230 V: R = V²/P = 230²/40 = 1323 Ω. For 120 V: R = 120²/40 = 360 Ω. Wind nichrome wire in a close spiral around the ceramic tube, starting 15 mm from one end and extending 30-40 mm. Leave 20 mm pigtails at each end for electrical connection. Secure the ends by passing through small holes drilled in the ceramic or by crimping with stainless steel ferrules.
3. **Assemble the heating element**: Slide the ceramic tube with wound heater over the copper tip shank. The heater section should surround the thick part of the tip (not the pointed end). The copper shank should extend 5-10 mm past the ceramic to allow tip changing.
4. **Install in the steel body tube**: Slide the ceramic + heater assembly into the steel tube. The steel tube protects the ceramic from mechanical damage and provides a grip surface. Fill any gap between ceramic and steel with a thin layer of ceramic fiber or mica to prevent rattling and reduce heat loss.
5. **Make electrical connections**: Connect one nichrome pigtail to the copper tip (this provides one pole through the tip to the workpiece for grounded operation). Connect the other pigtail to one conductor of the power cord. Connect the second power cord conductor to the steel body (for a grounded tip configuration) or to a separate ring terminal that contacts the tip via a set screw. Use crimped ring terminals on all connections. Insulate connections with ceramic fiber or glass-fiber sleeving.
6. **Mount the handle**: Bore a hole in the wooden handle matching the steel tube OD (tight fit). Apply heat-resistant epoxy (or friction-fit) to secure the steel tube in the handle. Route the power cord through a hole drilled in the handle and add a strain relief (cable gland or knot inside the handle).
7. **Shape and tin the tip**: Before first use, heat the iron and apply solder with flux to the tip. The solder should flow and coat the tip in a thin, shiny layer ("tinning"). A tinned tip transfers heat efficiently and resists oxidation.

### Temperature-Controlled Soldering Iron (50-80 W)

8. **Add thermocouple**: Embed a Type K thermocouple (chromel-alumel, 0.5 mm wire) in a small hole drilled in the copper tip, 3-5 mm from the working end. Secure with high-temperature ceramic cement (alumina-based, rated >800°C). Route the thermocouple wires alongside the heater through the body to the handle.
9. **Build the controller**: Construct a temperature controller using a thermocouple amplifier (op-amp circuit with cold-junction compensation), a comparator with setpoint adjustment (potentiometer), and a power switching element (triac for AC or MOSFET for DC). The controller modulates power to the heater to maintain the set tip temperature. For a simple implementation: use a 555-timer-based PWM circuit driving a MOSFET, with the thermocouple voltage compared against a reference set by a potentiometer. Calibrate by measuring tip temperature with a separate thermocouple at the setpoint.

### Soldering Technique

10. **Prepare the joint**: Clean both surfaces to be joined. Oxidized copper does not wet — abrade with fine sandpaper or use flux. Apply flux to both the component lead and the PCB pad. Flux removes surface oxides during heating and promotes solder wetting.
11. **Heat the joint**: Apply the iron tip to the joint so it contacts both the component lead and the PCB pad simultaneously. Apply a small amount of solder to the tip-to-joint interface to create a thermal bridge (the liquid solder conducts heat far better than dry contact). Hold for 2-5 seconds for through-hole joints, 1-2 seconds for small SMD.
12. **Feed solder**: Apply solder wire to the heated joint (not to the iron tip). The solder should flow into the joint by capillary action, forming a concave fillet. Feed until the fillet is complete — typically 1-3 mm of solder wire per through-hole joint.
13. **Remove and inspect**: Remove solder wire first, then the iron. Do not move the joint for 3-5 seconds while the solder solidifies. Inspect: a good joint has a shiny, concave fillet (Sn/Pb) or a smooth, satin fillet (lead-free) wetting both lead and pad. A dull, grainy, or convex fillet indicates a cold joint — reheat and add flux.

### Desoldering and Rework

Removing soldered components requires a different technique than soldering:

1. **Add fresh solder**: Apply flux-cored solder to the existing joint. The fresh flux activates and the additional solder improves thermal contact between the iron and the old joint.
2. **Heat the joint**: Apply the iron tip to the reflowed joint for 2-3 seconds (through-hole) or 1-2 seconds (SMD). The fresh and old solder melt together.
3. **Remove solder**: Use a solder sucker (spring-loaded vacuum pump) or solder wick (braided copper impregnated with flux). Solder sucker: position the nozzle at the joint, release the plunger to vacuum molten solder. Solder wick: place wick on the joint, press the iron tip on top of the wick, solder wicks into the braid by capillary action.
4. **Remove the component**: Once solder is removed, the component lead should be free. Gently pull the lead from the hole. If stuck, reheat and apply more wick — do not force it.
5. **Clean the pads**: After component removal, clean the pads with flux and wick to remove residual solder. The pads should be flat for the replacement component.

Solder wick specification: 1.5-3.0 mm width, flux-impregnated braided copper. One 30 cm length cleans approximately 20-40 through-hole joints before the saturated section must be cut off.

## Quantitative Parameters

### Operating Parameters by Iron Type

| Parameter | Uncontrolled (25-40 W) | Controlled (50-80 W) |
|-----------|:----------------------:|:--------------------:|
| Tip temperature range | 300-420°C (load-dependent) | 200-480°C (set ±5°C) |
| Heat-up time to 350°C | 60-120 seconds | 30-60 seconds |
| Thermal recovery time | 5-15 seconds | 2-8 seconds |
| Power consumption | 25-40 W | 50-80 W |
| Supply voltage | 120 V or 230 V AC | 120 V or 230 V AC (or 12-24 V DC via station) |
| Tip-to-joint thermal resistance | 20-50°C/W | 10-30°C/W |
| Idle temperature drift (±10% line voltage) | ±20-30°C | ±5°C (controller compensates) |

### Tip Life Data

| Tip Type | Operating Hours Before Failure | Failure Mode |
|----------|-------------------------------|--------------|
| Bare copper (unplated) | 20-50 hours | Erosion from tin-copper intermetallic dissolution |
| Iron-plated (standard) | 500-2,000 hours | Plating breach exposing copper core |
| Iron-plated + pre-tinned | 1,000-3,000 hours | Slow plating wear; pre-tin reduces oxidation |
| Ceramic heater (integrated) | 5,000-10,000 hours | Heater element failure |

### Solder Alloy Parameters

| Alloy | Melting Point | Wetting Speed | Joint Strength (shear) | Use Case |
|-------|:------------:|:------------:|:---------------------:|----------|
| Sn63/Pb37 | 183°C | Fast (0.5-1.0 s) | 40-60 MPa | General electronics, easiest to work |
| Sn60/Pb40 | 183-190°C | Fast | 35-55 MPa | General purpose (slightly pasty range) |
| SAC305 (Sn96.5/Ag3.0/Cu0.5) | 217-220°C | Moderate (1.0-2.0 s) | 30-45 MPa | Lead-free compliant, RoHS |
| Sn99.3/Cu0.7 | 227°C | Slow (1.5-2.5 s) | 25-40 MPa | Lead-free, cheapest, no silver |

### Wattage Selection by Application

| Application | Recommended Wattage | Tip Temperature | Rationale |
|------------|:-------------------:|:---------------:|-----------|
| Through-hole soldering (0.8 mm PCB) | 25-40 W | 320-370°C | Adequate thermal mass for single-sided boards; 40 W handles ground planes |
| Multi-layer PCB, ground planes | 50-80 W (controlled) | 350-380°C | Higher thermal demand; temperature control prevents overheating during recovery |
| Lead-free soldering (SAC305) | 50-80 W (controlled) | 370-420°C | Higher melting point requires 30-40°C more tip temperature than Sn/Pb |
| SMD rework (0805 and larger) | 25-40 W | 320-360°C | Conical tip for precision; low thermal mass of joints reduces demand |
| Heavy connectors, 10 AWG wire | 80-150 W | 370-420°C | Large thermal mass requires sustained heat delivery; gun-type or high-watt station |
| Sheet metal seams, tinwork | 100-250 W (soldering gun) | 400-500°C | High thermal mass of workpiece; gun-type provides instant heat |

Select the lowest wattage that maintains tip temperature at the joint. Excess wattage without temperature control shortens tip life and damages components.

## Scaling Notes

- **25-40 W uncontrolled**: Sufficient for through-hole soldering on single-layer PCBs with 0.8-1.6 mm substrate. Struggles with ground planes and multi-layer boards — the thermal mass drains heat faster than the iron can supply it.
- **50-80 W temperature-controlled**: Handles multi-layer PCBs, ground planes, and lead-free soldering (which requires 30-40°C higher tip temperature). The controller maintains temperature under varying thermal loads.
- **100-150 W soldering station**: For production soldering of large connectors, bus bars, and heavy-gauge wire (10 AWG and larger). Not needed for PCB work.
- **Solder pot / wave solder**: For production PCB assembly, a solder pot (5-20 kg of molten solder at 250°C) replaces the iron for through-hole soldering of entire boards. Requires 1-3 kW heating. See [Electronics Assembly](assembly.md).

Minimum practical scale: a single 40 W iron serves a workshop soldering 50-100 joints per day. A production line soldering 500+ joints per day benefits from a temperature-controlled station for consistency.

Scaling from workshop to production: a single operator with a temperature-controlled iron produces 200-400 solder joints per hour on through-hole PCBs. For SMD work, throughput drops to 100-200 components per hour due to precision requirements. Beyond 1,000 joints per hour, consider batch methods (wave soldering for through-hole, reflow oven for SMD) rather than adding more hand-soldering stations.

Tip replacement schedule: in continuous production (8 hours/day), replace iron-plated tips every 3-6 months (approximately 500-1,000 operating hours). Bare copper tips require reshaping every 2-3 days. Stock 3-5 spare tips per iron to avoid downtime.

Energy consumption: a 40 W iron running 8 hours per day consumes 0.32 kWh/day. A temperature-controlled station (70 W, cycling at 50% duty) consumes 0.28 kWh/day. Annual energy: 80-100 kWh per iron — negligible compared to other workshop loads (lathes, drill presses, lighting).

## Flux

Flux is essential to soldering — without it, solder will not wet oxidized copper. Flux chemically reduces surface oxides at soldering temperature, exposing clean metal for the solder to bond. Three types cover the range from workshop to production:

- **Rosin flux (R, RMA, RA)**: Extracted from pine tree sap (colophony). R (rosin, inactive) for clean surfaces. RMA (rosin mildly activated) contains organic activators that improve oxide removal — the standard for electronics. RA (rosin activated) for heavily oxidized surfaces. Residue is non-corrosive and can be left on the board (though cleaning with isopropanol is preferred for inspection clarity). The visible "smoke" during soldering is vaporized rosin, not metal fume.
- **Organic acid flux (OA)**: Water-soluble, aggressive oxide removal. Used for soldering to difficult surfaces (nickel, stainless steel). Residue is corrosive and must be washed off with water within 1-2 hours of soldering — left in place, OA flux causes long-term corrosion of copper traces.
- **No-clean flux**: Leaves a thin, non-corrosive, non-conductive residue that does not require removal. Used in production where cleaning adds cost. Less aggressive than RMA — may not adequately clean heavily oxidized leads.

Flux application: use flux-cored solder wire (flux is inside the wire, released during melting) for most work. For surface-mount work or rework, apply additional flux from a flux pen or small brush. Flux paste (thickened rosin or organic flux) is used for tinning large surfaces and for soldering connectors.

Flux storage: rosin flux is stable indefinitely at room temperature. Organic acid flux has a shelf life of 6-12 months (activators degrade). No-clean flux is stable for 12-24 months. Keep all flux containers sealed — exposure to air degrades activators.

## Tip Maintenance

Tip life is the primary ongoing cost of soldering iron operation. Proper maintenance extends iron-plated tip life from months to years.

- **Always tin the tip** before and after each use session. A thin layer of solder protects the iron plating from oxidation. An untinned tip left at operating temperature oxidizes within minutes, forming a black crust that prevents wetting.
- **Clean on brass wool, never a file**. Brass wire wool (or a brass-tip cleaner) removes oxide without damaging the iron plating. A file or abrasive paper strips the plating, exposing the copper core to rapid erosion.
- **Never leave the iron at temperature without solder on the tip**. Idle operation at 350°C with no solder accelerates iron plating oxidation 5-10× compared to a tinned tip.
- **Use the lowest effective temperature**. For Sn/Pb soldering, 350°C is sufficient — there is no benefit to running at 400°C. Each 25°C increase roughly halves tip life by accelerating intermetallic growth between the iron plating and copper core.
- **Avoid abrasive fluxes**. No-clean and RMA fluxes are mild. Organic acid flux attacks iron plating. If OA flux is necessary, clean the tip immediately after use.
- **Replace tips when plating fails**. A dimple or hole in the iron plating exposes copper, which erodes rapidly (20-50 hours). Replace at first sign of plating breach — continuing to use a breached tip produces solder contamination (copper dissolves into the solder, raising its melting point).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Tip will not tin (solder balls off) | Oxidized tip surface or insufficient temperature | Clean tip with brass wire wool (not file — damages plating); apply fresh solder with flux; verify tip temperature >300°C |
| Tip temperature too low | Heater element partially failed, poor electrical connection, or low supply voltage | Measure heater resistance (should match design: V²/R); check set screw connections; verify supply voltage |
| Tip eroding rapidly (copper) | Bare copper tip with no plating, high solder volume | Iron-plate the tip or accept frequent reshaping as maintenance; keep tip tinned when not in use |
| Handle getting hot | Insufficient thermal break between heater body and handle | Add phenolic washer or increase air gap; wrap steel body with glass-fiber tape near the handle |
| Iron takes too long to heat up | Heater resistance too high (too many turns of nichrome) or low voltage | Recalculate nichrome length for target wattage; verify supply voltage matches design |
| Solder joints look dull and grainy | Tip temperature too low, insufficient flux, or iron not making good thermal contact | Increase temperature; apply fresh flux; ensure tip is tinned and contacts both pad and lead simultaneously |
| Tip blackens and will not wet | Severe oxidation from running iron dry at high temperature | Re-tin immediately: clean with brass wool, apply fresh flux-cored solder; never leave iron at temperature without tinning the tip |
| Cold joints (solder did not flow) | Insufficient heat time, joint moved during solidification | Reheat joint with fresh flux; hold iron 2-3 seconds longer; immobilize component during cooling |
| Solder bridges between adjacent pads | Excess solder, tip too large for pitch | Use a smaller tip (conical); apply less solder; use solder wick (braided copper) to remove bridges |
| Pad lifting from PCB substrate | Excessive heat duration (>10 s) or repeated rework cycles on same pad | Limit contact time to 2-5 s; allow 30 s cooling between rework attempts on same pad |
| Nichrome heater open circuit | Overheating from running dry, or mechanical fatigue from thermal cycling | Replace heater winding; ensure tip is always tinned (dry tip runs hotter than rated) |

## Safety

- **Thermal burns**: Tip temperature of 350-420°C causes immediate second-degree burns on skin contact. Always return the iron to a stable rest (metal cradle, not the workbench) when not actively soldering. The rest must be heavy enough to resist tipping.
- **Lead exposure**: When using Sn63/Pb37 solder, wash hands thoroughly before eating or drinking. Lead oxide fume generation is minimal at normal tip temperatures (<500°C) but hand-to-mouth contamination from handling solder wire is the primary risk.
- **Solder fumes**: The visible "smoke" from soldering is flux vapor (colophony), not metal fume. Use local exhaust ventilation or a fume extractor with activated carbon filter positioned 5-15 cm from the joint. Capture velocity: 0.3-0.5 m/s.
- **Electrical safety**: Ensure the iron body and tip are properly grounded. A fault in the heater insulation can apply line voltage to the tip — lethal if the user touches both the tip and a grounded surface. Use a 3-wire cord with ground. Inspect cord integrity before each use.

## Quality Control

- **Visual inspection**: Every solder joint should have a smooth, concave fillet wetting both the component lead and the pad. Reject joints that are: dull/grainy (cold joint), convex/balled (insufficient heat or flux), cracked (moved during solidification), or having solder bridges between adjacent pads.
- **Pull test (through-hole)**: Gently tug each component lead after soldering. A properly soldered joint holds the lead with zero movement. If the lead moves, the joint is defective — reheat with flux.
- **Magnification**: Use a 5-10× loupe or magnifier for inspecting fine-pitch SMD soldering. Defects invisible to the naked eye (solder balls, tombstoning, insufficient fillet) become apparent at 10×.
- **Sample rate**: For production work, inspect 100% of joints visually. For high-reliability applications, add electrical continuity testing on every joint using a [multimeter](test-equipment.md).
- **IPC-A-610 criteria** (reference standard): Class 1 (general electronic products) allows minor cosmetic defects. Class 2 (dedicated service — industrial, communications) requires good wetting and fillet shape. Class 3 (high performance — medical, aerospace) demands optimal wetting, fillet height ≥ lead thickness, and zero visible defects. For bootstrapping, target Class 2 quality as the minimum standard for all assemblies.

Joint defect rate tracking: count defects per 100 joints. Target: <2% defect rate for experienced operators, <5% during training. Defect rates above 5% indicate: insufficient operator training, wrong tip temperature, wrong tip geometry, or contaminated solder/flux.

## Variations and Alternatives

- **Soldering gun (transformer type)**: A step-down transformer drives high current (50-100 A at 1-3 V) directly through a copper wire tip. The tip heats resistively in seconds. Advantages: instant heat, high power (100-250 W). Disadvantages: tip temperature uncontrolled (rises to 500°C+ quickly), bulky, generates electromagnetic field that can damage sensitive components. Suitable for heavy wire and sheet metal soldering, not PCB work.
- **Gas soldering iron (butane)**: A catalytic converter heated by butane flame. Portable — no electrical supply needed. Power: 20-75 W equivalent. Tip temperature: adjustable by gas flow. Disadvantages: open flame hazard, limited tip selection, flame-out in windy conditions. Useful for field repairs.
- **Solder pot**: A temperature-controlled pot of molten solder (5-20 kg) used for tinning wires, dip-soldering PCBs, and component tinning. Maintains solder at 250-260°C with 1-3 kW heating. See [Electronics Assembly](assembly.md).
- **Resistance soldering**: Passes current directly through the workpiece via two electrodes — the joint itself heats by resistance. No tip heating required. Useful for delicate work where an iron tip would be too large.

## References

- [Electronics Assembly](assembly.md) — soldering procedures and joint quality standards
- [Electrical Systems](electrical-systems.md) — wiring harness assembly using soldering irons
- [Power Electronics](power-electronics.md) — high-power assembly requiring temperature-controlled irons
- [Electrolysis](../chemistry/electrolysis.md) — copper production for soldering iron tips
- [Ceramics](../ceramics/index.md) — ceramic insulators for heater construction
- [Electroplating](../electrochemistry/electroplating.md) — iron plating for tip longevity
- [Passive Components](passive-components.md) — component leads and terminals that require soldering
- [PCB Fabrication](pcb-fabrication.md) — circuit boards with copper pads that receive soldered joints
- [Test Equipment](test-equipment.md) — multimeters for continuity and joint verification

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](./index.md) • [All Domains](../index.md)*
