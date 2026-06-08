# SOI Wafer Production

> **Node ID**: silicon.wafering.soi
> **Domain**: [Silicon](./index.md)
> **Dependencies**: See prerequisites
> **Enables**: [`Wafer Slicing & Polishing`](wafering.md)
> **Timeline**: Years 60-150+
> **Outputs**: soi_wafers, buried_oxide_layers
> **Critical**: No

## Overview

![Fossils of all kinds, digested into a method, suitable to their mutual relation and affinity : with the names by which they were known to the antients, and those by which they are at this day known: and notes conducing to the setting forth the natural history, and the main uses, of some of the most considerable of them. As also several papers tending to the further advancement of the knowledge of minerals, of the ores of metalls, and of all other subterraneous productions](../images/silicon/silicon_soi.jpg)

> *"The importance of Woodward's treatise is manifest, from the standpoint of the mineralogist it provides a scheme of classification of as much merit as it was possible to accure in that time, and from the standpoints of the paleontologist and gemologist it truly identifies fossils for what they are, also figured stones to which all sorts of superstitious beliefs had been attached..."--Gemology by J. Sinkankas, entry no. 7324.*

> *Image: John Woodward, Public domain*

Silicon-on-insulator wafer fabrication via SIMOX (oxygen implantation), Bonded SOI (wafer bonding and back-thinning), and Smart Cut (hydrogen-induced splitting) processes. Produces wafers with a buried SiO₂ layer for reduced parasitic capacitance and radiation-hard applications.

An SOI wafer stacks three layers: a thin single-crystal silicon device layer on top, a buried oxide (BOX) layer of silicon dioxide in the middle, and a thick silicon handle wafer as the mechanical support. The BOX electrically isolates transistors built in the device layer from the substrate and from each other, eliminating latch-up, reducing source/drain junction capacitance, and enabling fully depleted transistors that switch faster at lower voltage than their bulk CMOS counterparts.

Three manufacturing methods compete for SOI production. SIMOX (Separation by IMplanted OXygen) implants a massive dose of oxygen ions into a silicon wafer, then anneals at 1300°C+ to form a buried SiO₂ layer in place. Bonded SOI (BESOI) thermally oxidizes one wafer, bonds it face-to-face with a second wafer, then grinds and polishes one side down to the target device layer thickness. Smart Cut implants hydrogen into a donor wafer at a controlled depth, bonds it to a handle wafer, then splits the donor along the hydrogen plane by thermal annealing, leaving a thin silicon film bonded to the handle.

The device layer thickness ranges from ultra-thin (5-20 nm for fully depleted SOI) to several micrometers (for power electronics and MEMS devices). The BOX thickness ranges from 10 nm (thin BOX for FD-SOI with back-gate bias capability) to 3 μm (thick BOX for high-voltage isolation). Both dimensions must be controlled to tight tolerances, typically ±2% across the wafer, because device characteristics depend directly on these thicknesses.

SOI technology provides inherent radiation hardness because the thin device layer collects fewer charge carriers from ionizing radiation events than a bulk silicon substrate. The reduced junction area (source and drain extend only through the thin device layer rather than deep into the substrate) also lowers junction capacitance, improving switching speed and reducing power consumption compared to equivalent bulk CMOS circuits. These advantages make SOI the substrate of choice for space electronics and high-performance computing.

## Prerequisites

### Materials

- Prime-grade silicon wafers (double-side polished for bonding processes)
- High-purity oxygen for thermal oxidation (Smart Cut and BESOI)
- Hydrogen gas for ion implantation (Smart Cut)
- CMP slurries for post-bonding polish
- RCA cleaning chemicals (NH₄OH, H₂O₂, HCl) for wafer surface preparation before bonding
- Hydrofluoric acid (dilute, 1-5%) for surface activation and characterization

### Equipment

- [Silicon](index.md) — material dependency
- High-energy ion implanter: oxygen (SIMOX) or hydrogen (Smart Cut), capable of MeV energies and mA-level beam currents
- Wafer bonding system: cleanroom-class bonding chamber with alignment capability
- Chemical mechanical polishing (CMP) system for final device layer thinning
- Infrared or ultrasonic inspection system for void detection at bonded interfaces
- Spectroscopic ellipsometer for SOI and BOX thickness measurement
- Wafer flatness measurement tool (laser interferometer or capacitance gauge) for pre-bond inspection

### Knowledge

- Ion implantation physics: projected range, damage accumulation, high-dose effects
- Wafer bonding: surface preparation (hydrophilic versus hydrophobic), Van der Waals bonding, thermal annealing for bond strengthening
- Fracture mechanics: hydrogen platelet formation, crack propagation along the implant plane (Smart Cut)
- Thin film metrology: spectroscopic ellipsometry for nm-scale thickness mapping
- CMP process control: removal rate, selectivity, and uniformity for thin silicon films

### Infrastructure

- Class 10 cleanroom or better for wafer bonding (a single particle between bonded wafers creates a void)
- Ion implanter with X-ray shielding and high-voltage safety systems
- CMP waste treatment: used slurry contains colloidal silica and must be settled or filtered
- Thermal oxidation furnace capable of growing high-quality SiO₂ (for BESOI and Smart Cut BOX)
- Wafer inspection station with collimated light for surface quality verification before bonding

## Process Description

The Smart Cut process has become the dominant SOI manufacturing method because it provides good thickness uniformity, high crystal quality, and efficient material use (the donor wafer can be recycled as a future handle wafer after cleaving). The process runs in five stages.

First, a donor wafer is thermally oxidized to grow the BOX layer. The oxide thickness (typically 10 nm to 3 μm) determines the final buried oxide thickness in the SOI wafer. Second, the donor wafer is implanted with hydrogen ions at an energy that places the hydrogen peak at the desired device layer depth. The dose (typically 5×10¹⁶ to 1×10¹⁷ H⁺/cm²) is high enough to create micro-bubbles and platelets along the implant plane but not so high as to blister the surface. Third, the donor wafer and a handle wafer are cleaned to remove all particles and organic contamination, their surfaces are rendered hydrophilic (for oxide bonding) by a final clean step, and they are bonded face-to-face at room temperature by Van der Waals forces. Fourth, the bonded pair is annealed at 400-600°C. The hydrogen platelets coalesce into micro-cracks that propagate laterally, splitting the donor wafer along the implant plane. The thin silicon film remains bonded to the handle wafer, separated from it by the thermal oxide (BOX). Fifth, the split surface is polished by CMP to remove the roughness left by the cleaving process, producing the final SOI wafer with a smooth, device-ready surface.

SIMOX takes a different approach. A single silicon wafer is implanted with oxygen ions at 150-200 keV with a dose of 10¹⁷ to 10¹⁸ O⁺/cm². This is an enormous dose that requires many hours of implantation at high beam current. A subsequent high-temperature anneal (1300-1400°C for several hours in an inert or slightly oxidizing ambient) causes the implanted oxygen to react with the silicon to form a stoichiometric SiO₂ layer buried beneath a single-crystal silicon surface layer. The SIMOX process produces SOI wafers from a single starting wafer without bonding, but the high-dose implantation is slow and expensive, and the resulting BOX thickness is limited to 50-400 nm.

### Step-by-Step Procedure

1. Prepare donor and handle wafers: double-side polished, thermally oxidize the donor wafer to the target BOX thickness.
2. Implant the donor wafer with H⁺ at the energy corresponding to the desired device layer thickness. Verify dose uniformity across the wafer.
3. Clean both wafer surfaces in a Class 10 environment: RCA clean, DI water rinse, spin-dry. Any particle between the surfaces will create a void.
4. Bond the wafers face-to-face at room temperature: contact at a single initiation point and allow the bond wave to propagate across the wafer. Verify bond quality by infrared imaging.
5. Anneal the bonded pair at 400-600°C to trigger the Smart Cut splitting. The donor wafer cleaves along the H⁺ implant plane, leaving the thin silicon device layer on the handle wafer.
6. Polish the split surface by CMP to the final device layer specification. Measure SOI and BOX thickness at 49+ points across the wafer.

The quality of the bonded interface is critical. Room-temperature bonding between hydrophilic oxide surfaces creates Van der Waals bonds (hydrogen bonding between surface OH groups) that are weak initially but strengthen dramatically during a post-bond anneal at 800-1100°C, where the hydrogen bonds convert to covalent Si-O-Si bonds. Any particle trapped between the surfaces prevents local bonding, creating a void that is typically detectable by infrared imaging before the splitting anneal. Voids larger than a few micrometers can cause device failures and must be avoided by rigorous particle control in the bonding cleanroom.

The buried oxide (BOX) layer must be pinhole-free, as any defect in the oxide creates a leakage path between the device layer and the handle wafer. In Smart Cut wafers, the BOX is a thermally grown oxide (grown before the hydrogen implant and bonding), which provides excellent quality and uniformity. In SIMOX wafers, the BOX forms by internal oxidation during the high-temperature anneal; its quality depends on the oxygen dose uniformity and anneal conditions. BOX thickness uniformity directly affects transistor threshold voltage in FD-SOI devices, where the back-gate (the handle wafer beneath the BOX) influences the device characteristics.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| SOI Layer Thickness | 10 nm - 100 μm | FD-SOI: 5-20 nm; PD-SOI: 50-200 nm; power: 1-100 μm |
| BOX Thickness | 10 nm - 3 μm | Thin BOX for FD-SOI (10-25 nm); thick for power devices (1-3 μm) |
| H⁺ Implant Energy | 20 - 200 keV | Sets device layer thickness via projected range |
| H⁺ Implant Dose | 5×10¹⁶ - 1×10¹⁷ cm⁻² | Must be sufficient to create a continuous fracture plane |
| Splitting Anneal | 400 - 600°C | Higher temperature = faster splitting but more surface roughness |
| CMP Removal | 50 - 500 nm | Removes the damaged layer from the split surface |

## Safety Considerations

SOI wafer fabrication involves high-energy ion implantation, which brings the same hazards as conventional implantation: lethal high voltages (hundreds of kilovolts), X-ray generation from beam strikes on metal surfaces, and toxic gas handling for the implant source. The hydrogen implant in Smart Cut adds a specific concern: the implanted wafer is mechanically fragile, with a built-in fracture plane that could split prematurely if mishandled.

Wafer bonding requires extremely clean surfaces, so the primary hazard is the chemical cleaning steps. HF dips (to remove native oxide and render surfaces hydrophobic for direct Si-Si bonding) present hydrofluoric acid burn risk. HF penetrates skin without immediate pain and causes deep tissue damage by chelating calcium; calcium gluconate gel must be stocked within reach.

Thermal oxidation furnaces operate at 900-1100°C with quartzware that can shatter if cooled too quickly. The oxidation atmosphere is dry O₂ or wet (steam), both of which are non-toxic but present burn hazards from hot surfaces and radiant heat.

- **Electrical**: High-voltage implanter hazards: lockout/tagout, X-ray shielding, interlocked access
- **Chemical**: HF burns from wafer cleaning; calcium gluconate gel must be accessible
- **Mechanical**: Implanted wafers with hydrogen fracture plane can split during handling; store in padded containers
- **Thermal**: Oxidation furnaces at 1000°C+; radiation shields and cool-down protocols

### Personal Protective Equipment

- HF-rated chemical gloves (neoprene or nitrile, double-gloved) and face shield during cleaning steps
- Calcium gluconate gel at the bench for immediate HF exposure first aid
- Heat-resistant gloves for loading and unloading oxidation furnaces
- Standard cleanroom garments (bunny suit, gloves, shoe covers) in the bonding area

### Emergency Procedures

- HF skin contact: rinse immediately with water for 15 minutes, apply calcium gluconate gel, seek medical attention
- Implanted wafer breakage (Smart Cut): collect fragments, ventilate area (hydrogen may have been trapped), dispose as silicon waste
- Furnace quartzware breakage: evacuate hot zone, allow to cool before cleanup (quartz fragments are sharp)
- Ion implanter interlock breach: beam stops, high voltage discharges automatically

## Quality Control

### Acceptance Criteria

- **SOI Wafers**: Device layer thickness uniformity within ±2% across the wafer; surface roughness below 0.5 nm RMS after CMP
- **Buried Oxide Layers**: BOX thickness uniformity within ±2%; pinhole density below 0.01 cm⁻²; bond interface void-free (infrared inspection)

### Testing Methods

- Spectroscopic ellipsometry: measures both SOI and BOX thickness simultaneously at nm resolution; 49+ point mapping across the wafer
- Infrared transmission imaging: detects voids and unbonded areas at the bonded interface (dark spots in the IR image)
- Ultrasonic imaging: alternative void detection method that works for opaque or patterned wafers
- Surface roughness measurement: AFM or white-light interferometry to verify CMP finish quality
- Electrical test: leakage current between device layer and handle wafer to verify BOX integrity
- SOI thickness uniformity mapping: 49-point ellipsometry across the wafer surface
- Stress measurement: wafer curvature (bow) measurement to detect film stress in the device layer

### Sampling Protocol

- Map thickness (ellipsometry) on every wafer at 49+ sites; reject any wafer with uniformity worse than ±3%
- Infrared void inspection on every bonded pair before the splitting anneal (catches bonding defects early)
- Surface roughness measurement on 3 wafers per lot after CMP
- BOX leakage current test on one wafer per lot to verify dielectric integrity

## Scaling Notes

SOI wafer production scales from single-wafer lab processes to batch production tools. The primary bottlenecks are the hydrogen implant (high dose, many hours per wafer on standard implanters) and the CMP step (device layer thinning to nm precision).

- **Research scale**: Single wafer bonded by hand in a clean bench, low-dose implant, manual CMP. One or two SOI wafers per week.
- **Pilot production**: Automated bonding tool, dedicated high-current hydrogen implanter, production CMP. 10-50 wafers per day.
- **Volume production**: Cluster tools integrating clean, bond, anneal, and CMP modules. Dedicated high-current implanters for H⁺ with batch end stations. Hundreds of wafers per week.

Smart Cut economics improve at scale because the donor wafer (minus the cleaved layer) can be reclaimed, re-polished, and reused as a handle wafer for subsequent runs. This material recycling halves the raw silicon cost compared to a non-recycling process.

The transition from bulk CMOS to SOI requires circuit design changes beyond simply swapping the substrate. In fully depleted SOI, the thin device layer means the gate field extends through the entire silicon film, improving subthreshold slope and reducing off-state leakage. However, the buried oxide is a thermal barrier that impedes heat flow from the transistor channel to the substrate. Self-heating can raise the channel temperature by 10-30°C above the substrate temperature, degrading carrier mobility and increasing device variability. Thermal modeling and careful layout (spacing hot devices apart, adding thermal vias) are necessary to manage self-heating in SOI circuits.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Voids at bonded interface | Particle contamination between wafer surfaces during bonding | Improve cleanroom class, add filtration, verify RCA clean effectiveness |
| SOI thickness variation across wafer | Non-uniform H⁺ implant dose or CMP over-polish in one region | Recalibrate implanter beam scanning; adjust CMP carrier film and downforce profile |
| Silicon film stress or bowing | Mismatch in thermal expansion between SOI layer and handle during anneal | Adjust anneal temperature ramp rate; use handle wafers of matched orientation |
| BOX pinholes | Incomplete oxidation before bonding (Smart Cut) or oxygen dose too low (SIMOX) | Grow thicker thermal oxide; verify oxidation furnace temperature uniformity |
| Premature splitting before bonding | H⁺ dose too high or wafer stored too long at elevated temperature before bonding | Reduce implant dose, store implanted wafers at room temperature, bond promptly after implant |
| High leakage current through BOX | Contaminants at bond interface or incomplete anneal of implant damage | Verify wafer clean chemistry; increase anneal temperature or duration |
| BOX thickness non-uniformity | Non-uniform thermal oxidation before bonding | Check oxidation furnace temperature uniformity; add in-situ steam generation uniformity check |
| Device layer delamination during CMP | Weak bond strength from insufficient post-bond anneal | Increase post-bond anneal temperature (above 800°C for covalent bonding) or extend anneal time |
| CMP removal rate too high | Soft device layer (possibly damaged by hydrogen implant) | Verify H⁺ dose is not excessive; adjust CMP downforce and slurry chemistry |

## Variations and Alternatives

- **SIMOX (Separation by IMplanted OXygen)**: Single-wafer process, no bonding required. Oxygen implant at 150-200 keV followed by 1300°C anneal. Produces thin BOX (50-400 nm). Slow and expensive due to the high dose, but excellent BOX quality.
- **Smart Cut (Unibond)**: Hydrogen-implant splitting plus wafer bonding. Dominant production method. Donor wafer is recyclable. Flexible BOX and SOI thickness control. Requires bonding capability.
- **BESOI (Bond and Etch-back)**: Two wafers bonded, one thinned by grinding and selective etch. Simple concept but thickness control depends on etch selectivity, limiting uniformity. Being displaced by Smart Cut for advanced applications.
- **ELTRAN (Epitaxial Layer Transfer)**: Porous silicon layer formed on a donor wafer, epitaxial layer grown on top, bonded to handle wafer, then the porous layer is etched away to separate. Provides smooth transfer without CMP. Developed by Canon, limited commercial adoption.
- **FD-SOI (Fully Depleted)**: Ultra-thin SOI device layer (5-20 nm) where the gate field extends through the entire film. Superior electrostatic control, lower operating voltage, reduced leakage. Gaining adoption for low-power IoT and mobile as a FinFET alternative at 28nm and below.
- **Silicon-on-sapphire (SOS)**: A heteroepitaxial variant where silicon is grown on a sapphire substrate instead of a silicon handle. Sapphire provides excellent RF isolation and is transparent, making SOS useful for integrated optics and RF switches. The lattice mismatch between silicon and sapphire creates defect challenges that limit silicon film quality.

Partially depleted SOI (PD-SOI) uses a device layer thick enough (typically 50-200 nm) that the gate field does not fully deplete the silicon film. The undepleted region acts as a floating body that can accumulate charge. PD-SOI devices behave similarly to bulk CMOS but with reduced parasitic capacitance, making them easier to design with as a drop-in replacement. Fully depleted SOI (FD-SOI) uses an ultra-thin device layer (5-20 nm) that is completely depleted by the gate field, providing superior electrostatic control of the channel and enabling lower operating voltages. FD-SOI requires precise thickness control (±0.5 nm) because the threshold voltage depends directly on the silicon film thickness.

The Smart Cut process was developed at CEA-Leti in the 1990s and commercialized by Soitec. Its key innovation is the use of hydrogen implantation to create a controlled fracture plane inside the silicon crystal. The implanted hydrogen forms platelets (flat micro-bubbles) along the (100) crystal planes at the depth of the hydrogen concentration peak. During the splitting anneal, these platelets grow and coalesce into a continuous crack front that propagates across the entire wafer. The splitting is remarkably uniform, producing a device layer whose thickness is determined by the hydrogen implant energy with ±5 nm precision before CMP.

SIMOX wafers have a more limited market share but remain important for applications requiring very thin BOX layers (below 50 nm) where the Smart Cut thermal oxide would be difficult to control at such thicknesses. The SIMOX process produces the BOX by internal oxidation during a high-temperature anneal (1300-1400°C for 4-6 hours) of an oxygen-implanted wafer. The oxygen dose must be extremely uniform across the wafer to produce a uniform BOX, requiring a specialized high-current oxygen implanter with excellent scanning uniformity. Multiple implant-and-anneal cycles (ITOX: Internal Thermal OXidation) improve the BOX stoichiometry and reduce defect density in the overlying silicon layer.

## References

- [Wafer Slicing & Polishing](wafering.md) — parent capability
- [Silicon Domain](./index.md) — domain overview and related capabilities
- [Wafer Slicing & Polishing](wafering.md) — downstream capability

---

SOI wafer pricing is 5-10× higher than bulk silicon wafers, reflecting the complex processing (implant, oxidation, bonding, CMP) and lower yields compared to bulk wafer production. The cost premium limits SOI adoption to applications where the performance benefits justify the added expense: high-performance computing (AMD processors), low-power mobile and IoT (FD-SOI at 28nm and below), radiation-hardened space and military electronics, and high-voltage power management ICs where the BOX provides electrical isolation for lateral DMOS transistors.

Wafer bonding technology developed for SOI production has found applications beyond semiconductor substrates. Direct wafer bonding (without the Smart Cut splitting) is used to create silicon-on-glass displays, MEMS encapsulated devices (bonding a cap wafer over the MEMS device for hermetic sealing), and 3D integrated circuits where multiple device layers are bonded and interconnected with through-silicon vias. The bonding process fundamentals are the same: atomically clean, flat surfaces brought into contact at room temperature, then annealed to form a permanent bond.

Smart Cut wafers require careful handling between the hydrogen implant and the splitting anneal. The implanted wafer contains a built-in fracture plane that is stable at room temperature but becomes increasingly fragile as temperature rises. Mechanical stress during wafer transfer or bonding can trigger premature splitting. The bonding operation itself must proceed quickly after the H⁺ implant (typically within 24-48 hours) because hydrogen can diffuse out of the implant peak at room temperature over longer periods, weakening the fracture plane and producing non-uniform splitting.

The CMP step after splitting removes the rough surface left by the fracture. The as-split surface has a peak-to-valley roughness of 5-15 nm with a characteristic pattern from the hydrogen platelets. CMP removes 50-500 nm of silicon to achieve a final surface roughness below 0.5 nm RMS, suitable for gate oxide growth. The CMP removal must be uniform across the wafer because any remaining thickness variation directly affects transistor characteristics in FD-SOI devices. Production CMP tools use in-situ endpoint detection (motor current or optical) to stop at the target thickness.

---
*Part of the [Bootciv Tech Tree](../index.md) · [Silicon](./index.md) · [All Domains](../index.md)*
