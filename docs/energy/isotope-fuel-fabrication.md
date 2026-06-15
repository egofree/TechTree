# Isotope Fuel Fabrication

> **Node ID**: energy.radioisotope-power.isotope-fuel-fabrication
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.radioisotope-power`](./radioisotope-power.md),
> [`energy.nuclear-fission.isotope-production`](./isotope-production.md),
> [`ehs.radiation-safety`](../ehs/radiation-safety.md)
> **Enables**: Thermoelectric RTG, Stirling isotope generator, radioisotope heater unit flight hardware
> **Timeline**: Years 30-100+
> **Outputs**: gphs_module, iridium_clad, fuel_pellet, rhu_unit
> **Critical**: No — not on the minimum-viable path. Fuel fabrication presupposes a operating isotope production line delivering Pu-238 oxide powder, a hot-cell and glovebox infrastructure qualified for alpha-emitting material, and a launch safety review process that runs 4-5 years per mission. All of this arrives decades after [nuclear fission](./nuclear-fission.md) is delivering baseload power.

## Overview

Isotope fuel fabrication is the transformation step between raw separated radioisotope and a launch-qualified heat source. [Isotope production](./isotope-production.md) delivers plutonium-238 dioxide powder in a jar; fuel fabrication turns that powder into a hot-pressed ceramic pellet, welds it inside an iridium capsule, wraps that capsule in multiple layers of graphite and carbon-carbon impact protection, and then runs the assembled module through the most rigorous safety qualification process in spaceflight. The output — a General Purpose Heat Source (GPHS) module or a Light Weight Radioisotope Heater Unit (LWRHU) — is the generic heat source that every American radioisotope power system has used since the 1980s.

This process matters because the fuel form determines the safety case. Raw PuO₂ powder is dispersible — inhaling milligrams is lethal. A hot-pressed ceramic pellet is a monolithic solid that fractures into large, non-respirable chunks. An iridium-clad pellet survives atmospheric reentry temperatures (1400 °C) and ground impact at 50 m/s. A GPHS module adds three independent containment barriers around the clad. Each fabrication step adds one layer of defence-in-depth, and the launch safety review (governed by NSPM-20, formerly PD/NSC-25) examines every layer against a sequence of accident environments: launch vehicle explosion, shrapnel impact, suborbital reentry, orbital reentry, and post-impact land or sea environments.

No classified safety analysis details, weapons-grade fabrication techniques, or Pu-239 metal production routes are described here. The fuel form discussed is exclusively the ceramic oxide heat-source grade used in space power systems.

## PuO₂ Pellet Fabrication

### Process

Plutonium-238 dioxide powder arrives from [isotope production](./isotope-production.md) as a fine olive-green ceramic powder. At Los Alamos National Laboratory (LANL), this powder is characterised for isotopic composition (Pu-238 content, Pu-236 impurity), particle size distribution, and specific power (W/g) before fabrication begins. The powder is then cold-pressed into a green compact at approximately 200 MPa, loaded into a graphite mould, and hot-pressed under vacuum or argon at 1200-1400 °C for several hours. The result is a dense ceramic cylinder.

### Pellet Specifications

| Parameter | Value |
|-----------|-------|
| Diameter | ~27.7 mm |
| Height | ~27.7 mm |
| Mass | ~150 g |
| Density | 87.4% of theoretical (9.6 g/cm³ for PuO₂) |
| Pu-236 impurity | < 2 ppm |
| Specific power | ~0.55 W/g (from Pu-238 decay) |
| Thermal output per pellet | ~62.5 W_th |

The 87.4% density target is deliberate. Fully dense PuO₂ (100% theoretical) is harder to fabricate and offers no thermal advantage; the 87.4% sintered density is high enough to ensure structural integrity and insolubility, while the residual porosity provides a sink for helium gas produced by alpha decay. Over the 14-year half-mission of an RTG, each gram of Pu-238 produces approximately 0.2 cm³ of helium at STP. Without porosity and the frit vent in the cladding, helium pressure would rupture the capsule.

### Why Ceramic?

The choice of plutonium dioxide ceramic over plutonium metal is driven by four factors:

1. **Thermal stability** — PuO₂ melts at 2400 °C, far above any reentry or accident temperature.
2. **Insolubility** — PuO₂ is chemically inert in water and biological fluids, drastically reducing biological uptake if a module lands in the ocean.
3. **Fracture behaviour** — A hot-pressed ceramic pellet shatters into large, non-respirable fragments under impact, unlike powder which disperses as respirable aerosol.
4. **Self-regulating heat** — The ceramic is a thermal conductor but electrical insulator, simplifying the thermal interface to the iridium clad.

The Pu-236 impurity limit of < 2 ppm is critical because Pu-236 has an alpha branch to a high-energy gamma emitter. Excess Pu-236 raises the neutron and gamma dose rate around the RTG, complicating integration handling and launch operations.

## Iridium Cladding

### DOP-26 Alloy

Each fuel pellet is encapsulated in a capsule made of DOP-26 iridium alloy — a proprietary alloy of iridium with 0.3% tungsten developed at Oak Ridge National Laboratory. Pure iridium is brittle under impact at elevated temperature; the tungsten addition, combined with grain-boundary dopants (thoria dispersion), improves ductility and impact resistance.

| Parameter | Value |
|-----------|-------|
| Alloy | DOP-26 (Ir + 0.3% W) |
| Capsule diameter | ~29 mm (OD) |
| Capsule height | ~29.4 mm |
| Wall thickness | 0.64 mm |
| Melting point | 2,443 °C |
| Reentry survival temp | Up to 1,400 °C |

Iridium was chosen because it is the only metal that retains useful mechanical strength at 1400 °C — the temperature reached during atmospheric reentry. No other cladding material (including refractory metals like tantalum or tungsten) combines iridium's high melting point, oxidation resistance, and ductility in the reentry thermal environment.

### Welding and Leak Testing

The clad consists of two halves — a cup and a lid — that are TIG (tungsten inert gas) welded in a glovebox under argon atmosphere. The weld is a full-penetration circumferential joint around the lid perimeter. After welding, each capsule undergoes:

1. **Helium leak testing** — The clad is pressurised with helium and tested in a vacuum chamber to confirm leak rates below 1×10⁻⁸ atm·cm³/s.
2. **Radiographic inspection** — X-ray radiography checks for weld porosity, inclusions, or incomplete penetration.
3. **Dimensional inspection** — Capsule dimensions are measured to confirm the pellet-clad gap is within tolerance for thermal transfer.
4. **Neutron radiography** — Confirms the pellet is seated correctly and no voids or cracks exceed acceptance criteria.

### Frit Vent

A critical design feature of the iridium clad is the frit vent — a sintered iridium powder disk, approximately 3 mm diameter, welded into a small port on the capsule lid. The disk's micrometre-scale pore size allows helium gas (produced by alpha decay of Pu-238) to escape while retaining the solid PuO₂ pellet and any particulate. Without the frit vent, helium would pressurise the capsule to the point of rupture within months of fabrication. The vent is a passive one-way diffusion barrier — gas flows out but particulate does not flow in or out.

## GPHS Module Assembly

### Structure

The General Purpose Heat Source (GPHS) is the modular heat-source architecture used in all modern American RTGs (MHW-RTG, GPHS-RTG, MMRTG). Each GPHS module contains two capsules, each holding two fuel pellets — four pellets per module. The module is assembled at the Idaho National Laboratory (INL) Space and Security Power Systems Facility (SSPSF) in argon-atmosphere gloveboxes at slight positive pressure to prevent air ingress.

| Parameter | Value |
|-----------|-------|
| Pellets per module | 4 (2 per clad, 2 clads) |
| Thermal output | ~250 W_th per module |
| Mass | 1.43 kg (legacy) to 1.61 kg (step 2, improved reentry survivability) |
| Module dimensions | ~96 mm × 96 mm × 52 mm |

### Containment Layers

Each GPHS module has three independent containment barriers between the PuO₂ fuel and the environment, in addition to the iridium clad itself:

1. **Graphite Impact Shell (GIS)** — A Fine Weave Pierced Fabric (FWPF) carbon-carbon composite shell that surrounds each pair of cladded capsules. FWPF is a three-dimensional woven carbon-fibre composite densified with chemical vapour infiltration (CVI) carbon. It provides mechanical strength for ground-impact survival (50 m/s on concrete) and ablation resistance for reentry.

2. **Carbon-Bonded Carbon Fibre (CBCF) Insulation** — A low-density carbon-fibre insulation disk that sits between the GIS and the aeroshell. CBCF provides thermal insulation, slowing heat flow from the hot clads to the aeroshell during reentry so the aeroshell sees a lower peak temperature. It also provides a refractory cushion that deforms under impact, absorbing kinetic energy.

3. **Aeroshell (FWPF)** — The outer carbon-carbon aeroshell that takes the brunt of atmospheric reentry heating. During reentry, the aeroshell surface ablates (pyrolyses), carrying heat away from the interior. The aeroshell is designed to survive the most severe reentry environment — a high-angle orbital reentry with peak temperatures near 1700 °C.

### Assembly Procedure

Assembly is performed in a dedicated glovebox line at INL SSPSF:

- Cladded capsules are inspected and weighed.
- Each capsule pair is loaded into a graphite impact shell with CBCF insulation disks on each face.
- The GIS is closed and the aeroshell is bonded around it using a carbonised resin adhesive.
- The assembled module is leak-tested, weighed, and radiographed.
- Modules are vacuum-baked at 300 °C for 48 hours to remove adsorbed moisture and volatiles before stacking into the RTG.

All operations use argon-atmosphere gloveboxes with continuous oxygen and moisture monitoring (dew point below −40 °C). Personnel work through glove ports using gauntlet gloves; the argon atmosphere prevents oxidation of the graphite components and suppresses any dispersible contamination from alpha-emitting material.

## Radioisotope Heater Unit (RHU)

The Light Weight Radioisotope Heater Unit (LWRHU) is a miniature heat source for spacecraft thermal control — keeping electronics above survival temperature in deep space or on the Martian surface. The Mars rovers Spirit, Opportunity, and Curiosity each carried dozens of RHUs around sensitive electronics.

| Parameter | Value |
|-----------|-------|
| Thermal output | 1.1 W_th |
| Total mass | 40 g |
| PuO₂ fuel mass | 2.66 g |
| Clad material | Pt-30Rh (platinum-30% rhodium alloy) |
| Clad dimensions | 32 mm × 12 mm × 0.6 mm wall |
| Insulation | 3 pyrolytic graphite sleeves |
| Aeroshell | FWPF carbon-carbon |
| Operating temperature | Up to 1250 °C |

The LWRHU uses a platinum-30% rhodium alloy clad instead of iridium — the lower heat output (1.1 W vs 62.5 W per pellet) means reentry temperatures are lower and platinum alloy, which is easier to fabricate and weld than DOP-26 iridium, is sufficient. The 2.66 g PuO₂ pellet is smaller than a standard GPHS pellet and is surrounded by three pyrolytic graphite sleeves that provide thermal insulation and a secondary containment barrier. The outer aeroshell is FWPF carbon-carbon, identical in concept to the GPHS aeroshell.

Each LWRHU undergoes the same safety review as a GPHS module, scaled to its smaller fuel inventory.

## Launch Safety Qualification

### NSPM-20 Process

Launch of any quantity of plutonium-238 is governed by the National Security Presidential Memorandum 20 (NSPM-20), which superseded Presidential Directive / National Security Council Memorandum 25 (PD/NSC-25). The process requires the requesting agency (NASA) to demonstrate that the risk to the public from a launch accident is acceptably low. The review takes 4-5 years from preliminary safety analysis to final launch approval.

### Safety Analysis Report (SAR)

NASA and the Department of Energy (DOE) prepare a multi-volume Safety Analysis Report (SAR) that examines the full launch accident sequence:

1. **Pre-launch** — handling accidents, pad fires, vehicle tip-over.
2. **Launch phase** — explosion on or near the pad, failure during first-stage ascent (liquid propellant fireball, solid motor case burst).
3. **Suborbital reentry** — vehicle failure above the atmosphere, modules reentering on a suborbital trajectory with high heating rates.
4. **Orbital reentry** — modules reentering from orbit after a long coast, with lower heating rates but longer duration.
5. **Post-impact** — modules on land (soil, rock, water) exposed to fire, wave action, or corrosion.

For each phase, the analysis examines whether the containment barriers (iridium clad, GIS, CBCF, aeroshell) survive or fail, and if they fail, how much fuel is released and in what physical form (large fragments vs respirable aerosol).

### INSRP Review

The Interagency Nuclear Safety Review Panel (INSRP, now INSRB) is an independent review body composed of seven agencies:

- Department of Defense (DOD)
- Department of Energy (DOE)
- Department of State
- Department of Transportation (DOT)
- Environmental Protection Agency (EPA)
- National Aeronautics and Space Administration (NASA)
- Nuclear Regulatory Commission (NRC)

INSRP conducts an independent evaluation of the SAR, issues a separate safety evaluation report, and identifies any issues requiring further analysis. The review includes probabilistic risk assessment with Monte Carlo simulation of millions of accident scenarios, but specific code names, probability inputs, and quantitative results are classified and not described here.

### Launch Approval

Final launch approval is granted by the Director of the Office of Science and Technology Policy (OSTP) in the Executive Office of the President (White House). The OSTP Director must determine that the safety analysis is adequate and that the benefits of the mission justify the residual risk. This is the only step in the spaceflight enterprise where the White House directly approves a hardware decision.

### Defence in Depth

The safety philosophy relies on multiple independent containment barriers, each of which must fail before fuel is released:

| Barrier | Material | Function |
|---------|----------|----------|
| Fuel form | PuO₂ ceramic pellet | Fractures into large non-respirable chunks |
| Clad | DOP-26 iridium capsule | Retains fuel through reentry (mp 2443 °C) and ground impact |
| GIS | FWPF carbon-carbon shell | Absorbs mechanical impact, provides reentry ablation |
| CBCF | Carbon-bonded carbon fibre | Thermal insulation, impact cushion |
| Aeroshell | FWPF carbon-carbon | Primary reentry ablator, 3rd independent barrier |

The result is that even in a catastrophic launch vehicle failure, the fuel is expected to remain contained or, at worst, be deposited as large solid fragments that are recoverable.

## RTG Integration and Shipping

### Integration at INL

Once GPHS modules pass safety qualification and acceptance testing, they are transported to INL for RTG integration. The modules are stacked in a graphite matrix — typically 18 modules for a GPHS-RTG, 8 for an MMRTG — and the thermoelectric converter is assembled around them. The converter (see [Thermoelectric RTG](./thermoelectric-rtg.md)) is a cylindrical assembly of PbTe/TAGS or Skutterudite thermocouples that convert the thermal gradient between the hot GPHS stack and the cold-space radiator into electricity.

Integration steps:

1. Stack GPHS modules in the generator housing with graphite thermal-interface pads.
2. Install the thermoelectric converter — hot shoes contact the module stack, cold shoes contact the radiator fin assembly.
3. Perform vacuum thermal testing — the assembled RTG is run at full thermal output in a vacuum chamber to confirm electrical performance and thermal balance.
4. Conduct acceptance testing — measure open-circuit voltage, internal resistance, and power output at matched load over a range of temperatures.
5. Final inspection, drain cooling gas (if used for storage), and prepare for shipping.

### Shipping

The integrated RTG is shipped from INL to the launch site (Kennedy Space Center or Vandenberg Space Force Base) in a Department of Transportation-certified Type B shipping package. The 9975 and 9516 casks are the standard packages — massive steel-and-lead casks weighing several tonnes, designed to survive transport accidents (drop, fire, immersion) without releasing their contents. The shipment travels by specialised convoy with armed escorts under DOT and DOE regulations.

## Facilities

Fuel fabrication involves three major DOE sites, each handling a different stage:

- **Oak Ridge National Laboratory (ORNL)** — REDC (Radiochemical Engineering Development Center): separates Np-237 targets after reactor irradiation, produces purified PuO₂ powder. See [Isotope Production](./isotope-production.md).
- **Los Alamos National Laboratory (LANL)** — PF-4 (Plutonium Facility): presses pellets, fabricates and welds iridium cladding, performs frit-vent insertion and leak testing.
- **Idaho National Laboratory (INL)** — SSPSF (Space and Security Power Systems Facility): assembles GPHS modules, integrates RTGs, performs acceptance testing and shipping.

All three facilities are designed for alpha-emitting material handling: glovebox lines with inert atmospheres, filtered ventilation with HEPA and high-efficiency charcoal stages, continuous air monitors, and personnel dosimetry programs. See [Radiation Safety](../ehs/radiation-safety.md).

## Quantitative Reference

| Component | Parameter | Value |
|-----------|-----------|-------|
| PuO₂ pellet | Diameter × height | 27.7 × 27.7 mm |
| PuO₂ pellet | Mass | ~150 g |
| PuO₂ pellet | Density | 87.4% theoretical |
| PuO₂ pellet | Pu-236 limit | < 2 ppm |
| Iridium clad | Alloy | DOP-26 (Ir + 0.3% W) |
| Iridium clad | Wall thickness | 0.64 mm |
| Iridium clad | Melting point | 2,443 °C |
| GPHS module | Pellets per module | 4 |
| GPHS module | Thermal output | ~250 W_th |
| GPHS module | Mass | 1.43-1.61 kg |
| LWRHU | Thermal output | 1.1 W_th |
| LWRHU | Total mass | 40 g |
| LWRHU | PuO₂ mass | 2.66 g |
| LWRHU | Clad | Pt-30Rh |
| Launch safety | Governing directive | NSPM-20 |
| Launch safety | Review duration | 4-5 years |
| INSRP | Agencies | 7 (DOD, DOE, State, DOT, EPA, NASA, NRC) |
| Approval | Authority | White House OSTP |

## Troubleshooting

| Problem | Cause | Mitigation |
|---------|-------|------------|
| Pellet density below 87.4% | Insufficient sintering temperature or time, or low green-press pressure | Increase hot-press temperature to 1400 °C; extend hold time; verify graphite mould condition |
| Pu-236 impurity above 2 ppm | Target enrichment in reactor exposed too long to neutron flux producing Pu-236 side-reaction | Reject batch; review reactor irradiation spectrum and target burnup with isotope production facility |
| Clad leak rate above 1×10⁻⁸ atm·cm³/s | TIG weld porosity, incomplete penetration, or frit-vent bond failure | Re-weld or reject clad; inspect weld parameters (current, travel speed, argon flow); verify frit-vent weld geometry |
| Helium pressure in stored clad | Pellets fabricated long before launch; alpha-decay helium accumulates | Frit vent should self-relieve; verify vent porosity; rotate module inventory to use oldest first |
| CBCF insulation cracked | Handling damage or thermal shock during vacuum baking | Replace CBCF disk; handle in argon glovebox at all times; control vacuum-bake ramp rate below 2 °C/min |
| Aeroshell bond line void | Carbonised resin adhesive trapped moisture or volatiles | Re-bake aeroshell components at 300 °C before bonding; apply adhesive in vacuum; radiograph bond line |
| Module mass outside tolerance | Excess adhesive, wrong CBCF density, or pellet mass variation | Re-weigh components against acceptance sheet; reject modules outside 1.43-1.61 kg window |

## See Also

- [Radioisotope Power](./radioisotope-power.md) — Parent capability: conversion methods, mission history
- [Isotope Production](./isotope-production.md) — Upstream: reactor irradiation, PUREX separation, Pu-238 powder production
- [Thermoelectric RTG](./thermoelectric-rtg.md) — Downstream: Seebeck conversion, thermocouple materials *(sub-article, Wave 4)*
- [Radiation Safety](../ehs/radiation-safety.md) — Shielding, dosimetry, ALARA, launch safety framework
- [Nuclear Fission Power](./nuclear-fission.md) — Reactor design, fuel cycle, parent of isotope production
- [Ceramics](../ceramics/index.md) — Hot-pressing, graphite, carbon-carbon composites
- [Metals](../metals/index.md) — Iridium, platinum-rhodium, refractory alloy fabrication

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
