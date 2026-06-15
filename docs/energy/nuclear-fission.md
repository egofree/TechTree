# Nuclear Fission Power

> **Node ID**: energy.nuclear-fission
> **Domain**: [Energy](./index.md)
> **Dependencies**: `energy`, [`energy.electricity`](./electricity.md),
> [`metals.iron-steel`](../metals/iron-steel.md),
> [`ehs.radiation-safety`](../ehs/radiation-safety.md)
> **Enables**: None
> **Timeline**: Years 30-100+
> **Outputs**: nuclear_electricity, nuclear_heat, neutron_flux, fission_products
> **Critical**: No — not on the minimum-viable path. Nuclear fission demands a mature industrial base (pressure-vessel steel, zirconium refining, precision manufacturing, fuel-cycle chemistry, and a licensed radiation safety regime) that itself requires decades of prior capability buildup.

## Overview

Nuclear fission splits a heavy nucleus — most usefully uranium-235 or plutonium-239 — into two lighter fission fragments, releasing roughly 200 MeV (3.2 × 10⁻¹¹ J) per fission. Each fission also releases 2-3 neutrons (2.43 average for thermal U-235 fission), which can strike further fissile nuclei and sustain a chain reaction. The energy density is unmatched among practical sources: fissioning 1 gram of U-235 liberates about 24 MWh of heat, equivalent to burning 3 tonnes of coal or 2,000 litres of fuel oil.

For a bootstrapping civilization, nuclear fission is the densest non-solar energy source available. It decouples power generation from fuel logistics (a single fuel load runs 12-24 months), produces the neutron flux needed to manufacture every radioisotope power source, and yields process heat at scales that biomass, wind, and solar cannot match without vast land and storage investment. The cost is exacting: every reactor requires a forged pressure vessel, engineered safety systems, a licensed radiation safety program, and a closed fuel cycle for waste disposition.

This capability sits late in the tech tree because it presupposes precision metallurgy (vessel steels, zirconium cladding), industrial chemistry (enrichment, fuel fabrication, reprocessing), precision manufacturing (steam generators, control-rod drive mechanisms), and a functioning radiation-safety regime (see [Radiation Safety](../ehs/radiation-safety.md)). The reward is a baseload source with 90-93% capacity factor, fuel reserves that outlast any fossil horizon, and the neutron flux that unlocks every downstream isotope-dependent technology from Pu-238 RTGs to medical imaging.

## Materials and Prerequisites

- **Fuel** — Uranium dioxide (UO₂) ceramic pellets, enriched to 3-5% U-235 for light-water reactors, or natural uranium (0.72% U-235) for heavy-water designs. Thorium dioxide (ThO₂) is an alternative fertile matrix for the thorium cycle. Pellets are sintered to 95-97% theoretical density (10.4-10.7 g/cm³) and ground to ±10 µm diameter tolerance. See [Chemistry](../chemistry/acids-bases.md).
- **Cladding** — Zircaloy-4 or Zirlo tubes (zirconium alloyed with tin, niobium, iron, chromium) — 9.4-10.7 mm OD, 0.57-0.62 mm wall. Low thermal-neutron capture cross-section (0.18 barn for Zr vs 0.66 barn for Fe) preserves neutron economy; 9-13 µm oxide tolerance limit before oxidation accelerates. See [Metals](../metals/index.md).
- **Moderator** — Light water (H₂O, the dominant choice), heavy water (D₂O at 99.75% purity for CANDU), or nuclear-grade graphite (impurities below 1.5 ppm boron equivalent, bulk density ≥1.74 g/cm³). The moderator thermalizes prompt fast neutrons (2 MeV average birth energy) down to thermal energies (~0.025 eV) where U-235 fission cross-section peaks at 585 barns.
- **Control materials** — Boron carbide (B₄C), silver-indium-cadmium (Ag 80%-In 15%-Cd 5%), and hafnium for control rods; gadolinium (Gd₂O₃) and boron (as ZrB₂ coating or integral burnable poison) in the fuel matrix; boric acid dissolved in PWR coolant as chemical shim (0-2,000 ppm B).
- **Structural metals** — Forged low-alloy steel (SA-508 Grade 3 Class 1) for the reactor pressure vessel (a 400-tonne PWR vessel is a single open-die forging, one of the largest steel parts ever made); austenitic stainless steel (304/316) for primary piping, reactor internals, and steam-generator tubes; carbon steel for the containment building. See [Iron & Steel](../metals/iron-steel.md).
- **Coolant** — Light water (PWR/BWR), heavy water (CANDU), helium (HTGR at 5-7 MPa, 700-950°C), liquid sodium (fast reactors at ~0.1 MPa, 500-550°C), or molten FLiBe salt (600-700°C).
- **Shielding** — Concrete with magnetite or barite aggregate (density 3,500-4,200 kg/m³) for the bioshield; lead and steel plates for streaming patches; water and polyethylene for neutron shielding. Typical wall thickness: 1.2-2.0 m of heavy concrete reduces dose rates from the core to occupational limits. See [Construction](../construction/index.md).

### Materials Inventory (Reference 1 GWe PWR)

| Material | Quantity | Source |
|----------|----------|--------|
| Reactor pressure vessel (SA-508 Gr.3 Cl.1) | 1 unit, ~400 t | [Iron & Steel](../metals/iron-steel.md) |
| Steam generators (Inconel 690 U-tubes) | 2-4 units, ~300 t each | [Metals](../metals/index.md) |
| Primary loop piping (316 stainless) | ~1,500 m, 600-900 mm OD | [Iron & Steel](../metals/iron-steel.md) |
| Reactor internals (304 stainless) | ~100 t (baffles, formers, guide thimbles) | [Metals](../metals/index.md) |
| Fuel assemblies (17×17 Zircaloy-4/UO₂) | 193 assemblies, ~80 t heavy metal | [Chemistry](../chemistry/acids-bases.md) |
| Control rod drive mechanisms | 50-90 units, Inconel housings | [Metals](../metals/index.md) |
| Pressurizer (low-alloy steel, clad) | 1 unit, ~80 t | [Iron & Steel](../metals/iron-steel.md) |
| Containment building (prestressed concrete) | ~150,000 m³, 1.2-2.0 m wall | [Construction](../construction/index.md) |
| Coolant inventory (borated water) | ~250 t primary, ~500 t secondary | [Chemistry](../chemistry/acids-bases.md) |
| Bioshield concrete (heavy aggregate) | ~3,000 m³ | [Construction](../construction/index.md) |

## Fission Physics

Each U-235 fission releases 200 MeV, distributed as follows: 168 MeV as fission-fragment kinetic energy, 5 MeV to prompt neutrons, 7 MeV to prompt gammas, and the balance (~20 MeV) distributed across beta decays, delayed gammas, and neutrinos. The neutrino energy (~10 MeV) escapes the reactor and is unrecoverable. The recoverable energy per fission is ~190 MeV (3.04 × 10⁻¹¹ J).

The effective multiplication factor `k_eff` is the ratio of neutrons in one generation to the previous:

- `k_eff < 1` — subcritical; the chain reaction dies away exponentially
- `k_eff = 1` — critical; power is steady (the operating condition)
- `k_eff > 1` — supercritical; power rises

Reactor control is possible because a small fraction of neutrons (β = 0.65% for U-235, 0.21% for Pu-239) are *delayed* — emitted seconds to minutes after fission from the beta decay of fission products such as Br-87 (precursor to Kr-87, t₁/₂ = 55.6 s). Reactor periods stay in the tens-of-seconds to minutes range as long as `k_eff` does not exceed 1 + β (the prompt-critical threshold), giving operators and control systems time to act. Pushing `k_eff` past prompt criticality produces periods of microseconds — the regime of weapon assemblies, irrelevant to power reactors and out of scope here.

Prompt negative reactivity feedback returns the core toward steady state after a disturbance:

- **Doppler coefficient** (negative, ~-3 pcm/K): resonance broadening in U-238 increases neutron capture as fuel temperature rises. This is the fastest feedback (microseconds) and is present in every thermal reactor.
- **Moderator temperature coefficient** (negative in PWRs at operating temperature, ~-10 pcm/K): density drop reduces moderation.
- **Void coefficient** (negative in PWRs, design-dependent in BWRs, positive in RBMK — the Chernobyl type): steam voiding alters moderation.

A stable reactor has net negative reactivity feedback across the entire operating envelope — the single most important inherent safety property.

Neutron cross-sections drive reactor design. Thermal (0.025 eV) cross-sections govern LWRs: U-235 fission 585 barns, U-235 capture 99 barns, U-238 capture 2.7 barns, Xe-135 capture 2.65 × 10⁶ barns. The four-factor formula (`k_∞ = ηεpf`) gives the infinite-lattice multiplication: η (neutrons per U-235 absorption, 2.07 for thermal), ε (fast-fission factor, 1.03), p (resonance escape probability, ~0.75), and f (thermal utilization, ~0.85). Multiplying by the non-leakage probability gives `k_eff`. Designers tune p and f through fuel enrichment, moderator-to-fuel ratio (typically 2:1 to 4:1 by volume in LWRs), and burnable poison loading.

Xenon-135 poisoning deserves attention: Xe-135 has a thermal absorption cross-section of 2.65 million barns, the largest of any nuclide. It builds up over hours of operation (equilibrium at ~3 × 10¹⁵ atoms/cm³ in a 1 GWth core) and absorbs 2-3% of neutrons. After shutdown, Xe-135 continues to build for 4-6 hours as I-135 decays, peaking at ~7 hours before beta decay to Cs-135 catches up. During this xenon-dead-time window (~24-30 hours), the core may lack the excess reactivity to restart — a planning constraint for every reactor operator.

## Reactor Types

| Type | Coolant | Moderator | Primary Conditions | Outlet Temp | Spectrum |
|------|---------|-----------|--------------------|-------------|----------|
| PWR | Light water | Light water | 15.5 MPa | 320°C (hot leg), 290°C (cold leg) | Thermal |
| BWR | Light water | Light water | 7.2 MPa | 285°C | Thermal |
| CANDU / PHWR | Heavy water | Heavy water | 10-11 MPa | 310°C | Thermal |
| HTGR | Helium | Graphite | 5-7 MPa | 700-950°C | Thermal |
| SFR (fast breeder) | Liquid sodium | None (fast) | ~0.1 MPa | 500-550°C | Fast |
| Research (pool) | Light water | Light water / Be | Atmospheric | 50-100°C | Thermal |

**PWR** is the most common type worldwide (~300 units). Water at 15.5 MPa is pumped through the core, exits at 320°C (hot leg), and transfers heat to a secondary loop through U-tube steam generators. The pressurizer holds primary pressure above saturation to prevent bulk boiling. The secondary loop produces saturated steam at 5.5-7.5 MPa that drives the turbine.

**BWR** boils water directly in the core at 7.2 MPa. Steam exits at 285°C, passes through moisture separators and dryers, and drives the turbine in a direct cycle. The simpler primary loop eliminates steam generators (a major corrosion-replacement item) at the cost of carrying radioactive N-16 (t₁/₂ = 7.1 s) through the turbine during operation.

**CANDU** uses natural uranium (no enrichment needed) by replacing light water with 99.75% pure D₂O as both moderator and coolant. Fuel bundles sit in horizontal pressure tubes (Zr-2.5%Nb, 103 mm ID) rather than a single pressure vessel — a major manufacturing advantage, since pressure tubes are smaller forgings than a 400-tonne PWR vessel. On-power refueling (two fuelling machines attach to opposite ends) enables high capacity factors.

**Gas-cooled reactors** (Magnox, AGR, HTGR) use graphite moderation and helium or CO₂ coolant. The HTGR reaches 700-950°C outlet temperatures, enabling hydrogen production via thermochemical cycles (sulfur-iodine, hybrid copper-chlorine) and high-efficiency direct Brayton cycles (45%+). TRISO fuel (TRIstructural-ISOtropic particles: UO₂ kernel, pyrolytic carbon, SiC, pyrolytic carbon) retains fission products to 1,600°C.

**Sodium-cooled fast reactors** (BN-800, EBR-II heritage, CEFR) breed Pu-239 from U-238 blankets and operate without a moderator. Liquid sodium at atmospheric pressure removes heat at 500-550°C with excellent heat-transfer coefficients (~50,000 W/m²·K), but reacts violently with water and air — forcing an intermediate sodium loop between primary and steam systems. The fast spectrum burns actinides (Np, Am, Cm) that would otherwise dominate long-term waste heat.

**Research reactors** (HFIR, ATR, MTR pool types) are compact, high-flux machines optimized for isotope production and materials testing rather than electricity. They use plate-type fuel (U₃Si₂-Al or UMo-Al dispersion) for high surface-area heat transfer, run at 10 kW to 100 MW thermal, and deliver neutron fluxes of 10¹⁴ to 10¹⁵ n/cm²·s. They are the primary means of producing Pu-238 (from Np-237 targets), Co-60 (from Co-59), Mo-99 (from U-235 fission), and other activation products.

Each type involves trade-offs. PWR offers the most operational experience but pays for it with steam-generator corrosion and the 400-tonne pressure-vessel forging (only a handful of foundries worldwide — Japan Steel Works, China First Heavy Industries, AREVA Creusot — can supply these). BWR simplifies the primary loop at the cost of turbine-shine dose during operation and more complex core flow control. CANDU avoids enrichment and large forgings but depends on D₂O (heavy water costs ~$300/kg, and a typical CANDU inventory is 300-400 tonnes). HTGR offers high temperature and TRISO particle fuel integrity but has limited commercial deployment. SFR closes the fuel cycle but battles sodium-water reactivity and positive void coefficients in some designs.

## Reactor Operation

1. **Achieve criticality**: Withdraw control rods in small, logged increments while monitoring the startup count rate from intrinsic neutron sources (Pu-Be or Am-Be startup sources, plus photoneutron yield from gamma rays on D₂O in CANDU). Confirm criticality by the inverse count rate method — plot 1/M versus rod position and extrapolate to the rod position where 1/M approaches zero. Never approach criticality by extrapolation alone; perform the final approach with the reactor period meter in service.

2. **Raise power to operating level**: Continue rod withdrawal through the source-range (10⁰ to 10⁵ n/cm²·s), intermediate-range (10⁵ to 10¹⁰), and power-range (10¹⁰ to 10¹⁴) channels. Once at 10⁻⁸ to 10⁻⁶ of rated power, transition instrumentation. At ~0.1% power, switch to power-range control and engage the automatic controller. Hold at 15-20% to warm the turbine and condenser before loading.

3. **Synchronize to the grid**: Admit steam to the turbine through stop valves and control valves, roll up to 1,500 or 3,600 RPM (grid frequency divided by pole count), close the generator breaker when phase, voltage, frequency, and phase rotation match the grid within ±5 degrees, ±1 V, ±0.05 Hz. Then ramp reactor and turbine together to 100% power at 5%/minute (the maximum rate compatible with fuel pellet thermal stress limits).

4. **Maintain criticality over the cycle**: As fissile material depletes and fission-product poisons (Xe-135, Sm-149) accumulate, reactivity drops. Compensate in PWRs by diluting boric acid at 5-20 L/min; in BWRs by withdrawing control rods; in CANDU by daily on-power refueling (8-12 bundles per channel per refuel). A typical 18-month cycle reaches end-of-life when shutdown margin falls below the licensed minimum.

5. **Shut down**: Insert all control rods (scram, <2.5 seconds in PWRs). The reactor goes subcritical within milliseconds. Maintain forced circulation for decay heat removal: 6.5% of full power at shutdown, 1.5% after 1 hour, 0.4% after 1 day. Loss of forced cooling during this window is the design-basis accident (Fukushima Daiichi, 2011).

### Operational Verification

Continuous monitoring during operation:

- **In-core flux maps**: Movable fission chambers or self-powered neutron detectors map the 3D power distribution weekly. Verify peak linear heat generation rate stays below ~47 kW/m (PWR) to prevent centerline fuel melt (UO₂ mp 2,865°C) and departure from nucleate boiling on cladding.
- **Primary coolant activity**: Gamma spectroscopy on grab samples tracks iodine isotopes. Steady-state I-131 below 0.1 GBq/t; rising iodine indicates cladding defects. A failed fuel rod releases fission gases into the coolant, detectable within hours.
- **Coolant chemistry**: Maintain lithium 0.6-2.2 ppm (pairs with boric acid to set pH 6.9-7.4 in PWRs), dissolved oxygen <5 ppb (via hydrazine dosing at 0.1-0.3 ppm), hydrogen 25-50 cc/kg (suppresses radiolytic oxygen). Chloride and fluoride below 0.1 ppm each (stress-corrosion cracking in stainless).
- **Containment integrity**: Verify leak rate <0.1% of containment volume per day at design pressure (Type A test, every 10 years). Local leak rate tests on penetrations (Type B and C, every 30-60 months).
- **Fatigue and embrittlement**: Track pressure-temperature cycles on the vessel; surveil capsule dosimeters removed periodically to measure shifts in RTNDT (reference nil-ductility transition temperature) — the brittleness metric that sets pressure-temperature limits during heatup and cooldown.

## Quantitative Parameters

| Parameter | Value (PWR reference) |
|-----------|-----------------------|
| Energy per U-235 fission | 200 MeV (3.2 × 10⁻¹¹ J) |
| Recoverable energy per fission | 190 MeV (3.04 × 10⁻¹¹ J) |
| Neutrons per fission | 2.43 average (thermal) |
| Delayed neutron fraction β | 0.0065 (U-235), 0.0021 (Pu-239) |
| Fuel enrichment | 3-5% U-235 (LWR), natural 0.72% (CANDU) |
| Burnup | 33-50 GWd/t (typical LWR), up to 60+ GWd/t (advanced) |
| Core power density | 70-110 MW/m³ (PWR) |
| Specific power | 30-40 kW/kg of heavy metal |
| Primary coolant temperature | 290°C (cold leg) to 320°C (hot leg) |
| Primary pressure | 15.5 MPa (PWR), 7.2 MPa (BWR) |
| Thermal efficiency | 32-34% (LWR), 40-45% (HTGR Brayton, SFR) |
| Capacity factor | 90-93% (best-in-class units) |
| Refueling interval | 12-24 months |
| Neutron flux | 10¹³ to 10¹⁴ n/cm²·s (power reactors), 10¹⁴ to 10¹⁵ n/cm²·s (research) |
| Core heavy-metal inventory | ~80 tonnes UO₂ (1 GWe PWR) |
| Annual U-235 consumption | ~1 tonne per GWe (fissioned) |
| Annual spent fuel discharge | ~20-25 tonnes per GWe |

A 1 GWe PWR consumes roughly 1 tonne of U-235 per year (fissioned) while loading 20-25 tonnes of fresh enriched fuel and discharging the same mass as spent fuel with ~0.8% residual U-235, ~1% Pu, and ~3-4% fission products.

## Scaling Tiers

- **Research reactor (10 kW to 100 MW thermal)**: Pool-type, plate fuel, atmospheric pressure. Produces medical isotopes (Mo-99/Tc-99m), neutron-dopes silicon for power semiconductors, activates targets for Pu-238 and Co-60 production, and performs materials irradiation. Buildable with 1950s-era industrial infrastructure. Neutron flux: 10¹³ to 10¹⁵ n/cm²·s. This is the minimum viable entry point for nuclear capability.
- **Pilot power reactor (50-300 MWe)**: First-of-a-kind units (Shippingport 1958, 60 MWe; Calder Hall 1956, 50 MWe each; nuclear submarine plants ~165 MWth). Enable the first utility-scale electricity, district heating, and naval propulsion. Require a qualified pressure vessel, full safety-grade electrical systems, and licensed operators.
- **Commercial power reactor (300-1,600 MWe)**: Standard PWR/BWR/CANDU fleet units. Provide baseload electricity at 32-34% thermal efficiency and 90%+ capacity factor. Require sustained fuel-cycle infrastructure: enrichment (for non-CANDU), fuel fabrication, spent-fuel storage, decommissioning funds, and a strong regulator.
- **Fast breeder reactor (500-1,200 MWe)**: Converts U-238 to Pu-239 faster than it consumes fissile material. Extends fuel resources 60-fold by using the 99.3% of natural uranium that is non-fissile U-238. BN-800 (Russia, 2015) operates commercially; prototype breeders ran in the US (EBR-II, 1964-1994), France (Phénix 1973-2009, Superphénix 1986-1998), and India (PFBR, commissioning).

## Fuel Cycle Overview

The fuel cycle has a front end (mining through fabrication) and a back end (discharge through disposition).

**Front end**:
1. **Mining and milling**: Open-pit, underground, or in-situ leach (ISL) mining produces ore (0.05-0.5% U). Milling to yellowcake (U₃O₈, ~80% U by mass).
2. **Conversion**: U₃O₈ to uranium hexafluoride (UF₆), the feedstock for enrichment (sublimes at 56°C).
3. **Enrichment**: Increase U-235 from 0.72% to 3-5%. Modern gas centrifuges (Zippe-type rotors, 50-100 m/s tip speed in maraging steel or carbon fiber) consume ~50-100 SWU/kg of product — orders of magnitude less energy than the gaseous diffusion plants they replaced.
4. **Fabrication**: Convert enriched UF₆ to UO₂ powder, press and sinter pellets, load into zircaloy tubes, assemble into fuel bundles (17×17 PWR array: 264 fuel rods, 24 guide thimbles, 1 instrumentation tube).

**Back end**:
1. **Cooling**: Discharge spent fuel to a water-filled spent fuel pool for at least 5 years (decay heat and short-lived fission products must decline before dry storage).
2. **Interim storage**: Transfer to dry casks (steel-and-concrete, passively cooled by natural convection) for 20-60 years.
3. **Reprocessing (closed cycle)**: Dissolve spent fuel in nitric acid; PUREX solvent extraction (tributyl phosphate in kerosene) separates U (for re-enrichment), Pu (for MOX fuel), and fission products + minor actinides (as high-level waste). France (La Hague), UK (Sellafield), Russia (Mayak), and Japan (Rokkasho) operate commercial reprocessing.
4. **Disposition**: Once-through cycle stores spent fuel as waste in a geological repository; closed cycle vitrifies the fission products into borosilicate glass and emplaces in deep granite, clay, or salt formations.

## Safety Systems

Nuclear reactors release decay heat (~7% of full power immediately after scram, decaying per the Way-Wigner relation) that continues for years. Removing this heat without active power for the first 72 hours is the central safety requirement.

- **Defense in depth**: Five concentric barriers — fuel ceramic matrix (melting point 2,865°C for UO₂), zircaloy cladding, reactor pressure vessel, primary coolant boundary, and containment building. Each barrier must fail independently before release becomes possible.
- **Emergency Core Cooling System (ECCS)**: High-pressure injection pumps (PWR, 4-17 MPa), core spray and low-pressure injection (BWR), and accumulator tanks (pressurized with nitrogen to ~4 MPa, passively inject when primary pressure drops below that setpoint). ECCS must deliver against a double-ended guillotine break of the largest primary pipe — the design-basis LOCA.
- **Containment**: Pre-stressed concrete with steel liner, designed for peak internal pressure (0.35-0.45 MPa) and temperature (~150°C) following a LOCA, plus hydrogen mitigation (igniters or passive autocatalytic recombiners to control zirconium-steam reaction hydrogen).
- **Decay heat removal**: Auxiliary feedwater to steam generators (PWR), reactor core isolation cooling (BWR), and passive containment cooling (AP1000: water film on the steel containment shell, gravity-driven for 72 hours). Extended loss of all AC power (station blackout) drove the Fukushima Daiichi accidents in 2011.
- **Reactivity control**: Redundant and diverse shutdown systems — control rods plus a separate, independent shutdown system (a second set of rods, or liquid poison injection). CANDU uses two full-capability shutdown systems in compliance with the single-failure criterion.
- **Criticality safety**: Controls on fissile mass, geometry (always subcritical shapes — slab or cylinder below critical diameter), moderation, and reflection in fuel handling and storage. Prevents accidental criticality outside the reactor (e.g., in dissolution tanks during reprocessing, as occurred at Tokaimura in 1999). See [Radiation Safety](../ehs/radiation-safety.md).

## Variations

- **Breeder reactors**: Convert fertile material (U-238 or Th-232) to fissile (Pu-239 or U-233) at a rate exceeding consumption. Breeding ratio above 1 requires a fast neutron spectrum (for U-238/Pu-239) or a carefully thermalized spectrum (for Th-232/U-233). Liquid-metal fast breeders (SFR) and molten-salt breeders (MSBR) are the main designs. The IFR (Integral Fast Reactor, Argonne 1984-1994) paired metallic U-Pu-Zr fuel with pyroprocessing (electrorefining in molten LiCl-KCl) for an on-site closed fuel cycle.
- **Thorium fuel cycle**: Th-232 absorbs a neutron to become Th-233, which beta-decays (twice, through Pa-233) to U-233, a fissile isotope with higher neutron yield per thermal absorption (2.27) than U-235 (2.07). Thorium is three times more abundant than uranium in Earth's crust and produces less long-lived transuranic waste, but requires either a fissile driver (U-235 or Pu-239) to start the cycle or a dedicated external neutron source. The MSRE (Oak Ridge, 1965-1969) demonstrated the molten-salt thorium concept; India's three-stage nuclear power program targets thorium because India holds ~25% of world thorium reserves but little uranium.
- **Molten salt reactors**: Fuel dissolved in a fluoride (FLiBe — 67% LiF, 33% BeF₂) or chloride salt that serves as both fuel matrix and primary coolant. Operate at atmospheric pressure and 600-700°C, eliminating the high-pressure coolant that drives LOCA risk. Freeze plugs drain the fuel to passively-cooled drain tanks on loss of power. The MSRE demonstrated the concept; modern variants (FHR, TerraPower MCFR, ThorCon) are in licensing.
- **Small Modular Reactors (SMRs)**: 50-300 MWe units built in factories and transported to site by truck, rail, or barge. Target lower capital cost per unit, faster construction (3 years vs 7+ for large PWRs), and passive safety (natural circulation for decay heat removal). NuScale (77 MWe per module, 12-module plant, first US NRC design certification 2023); Rolls-Royce SMR (470 MWe); GE Hitachi BWRX-300 (300 MWe). Whether factory fabrication actually lowers dollar-per-kilowatt is unproven at fleet scale — first-of-a-kind economics dominate the early market.
- **Accident-tolerant fuels (ATF)**: Replacement of zircaloy cladding with chromium-coated zirconium, FeCrAl alloys, or silicon carbide ceramic composites. ATF reduces high-temperature oxidation (and the associated hydrogen generation that drove the Fukushima explosions) and extends coping time from minutes to hours under loss-of-coolant conditions. Lead test assemblies entered commercial US reactors in 2019-2023.
- **Microreactors (1-20 MWe)**: Truck-transportable units for remote sites, military bases, and mining operations. Designs include eVinci (Westinghouse, heat-pipe cooled), Project Pele (DoD, mobile), and Aurora (Oklo, fast spectrum). Target unattended operation for 10-20 years before factory refueling.

## Comparison with Other Baseload Sources

| Source | Capacity Factor | Thermal Efficiency | Fuel Logistics | Capital Cost ($/kW) |
|--------|-----------------|--------------------|----------------|---------------------|
| Nuclear (LWR) | 90-93% | 32-34% | Annual refueling | 6,000-9,000 |
| Coal (supercritical) | 50-70% | 38-43% | Continuous rail/barge | 2,500-3,500 |
| Combined-cycle gas | 50-60% | 55-62% | Continuous pipeline | 700-1,000 |
| Geothermal | 90-97% | 10-18% | None | 2,000-5,000 |
| Hydropower | 30-50% | 90%+ | None | 1,500-3,000 |

Nuclear's combination of very high capacity factor and refueling intervals measured in years is unique. Coal requires continuous fuel delivery equal to roughly 3 tonnes of coal per MWh — a logistics chain that fails without a rail or barge network. Gas turbines depend on pipeline pressure. Only nuclear and geothermal offer multi-year fuel independence; see [Geothermal Energy](./geothermal.md) for the renewable baseload alternative.

## Historical Milestones

| Year | Event | Significance |
|------|-------|--------------|
| 1942 | Chicago Pile-1 (CP-1) | First sustained chain reaction; 0.5 W, graphite-moderated |
| 1954 | Obninsk (USSR) | First grid-connected power reactor, 5 MWe |
| 1956 | Calder Hall (UK) | First commercial-scale plant, 4 × 50 MWe (Magnox) |
| 1957 | Shippingport (US) | First US PWR, 60 MWe, pressurized water design validated |
| 1970s-80s | Fleet buildout | ~400 reactors commissioned worldwide; LWR dominance established |
| 1986 | Chernobyl Unit 4 | RBMK positive void coefficient and disabled safety systems → catastrophic release |
| 2011 | Fukushima Daiichi | Station blackout, loss of decay-heat cooling → three core meltdowns |
| 2015 | BN-800 (Russia) | Commercial fast breeder reaches full power (880 MWe) |
| 2023 | NuScale design cert | First US NRC-certified SMR (77 MWe per module) |

The operating record now spans 18,000+ reactor-years. The two accidents that released significant radioactivity (Chernobyl 1986, Fukushima 2011) had specific technical causes: Chernobyl from an inherently unstable design (positive void coefficient in a graphite-moderated, water-cooled core) combined with disabled automatic trip; Fukushima from a station-blackout beyond design basis that defeated core cooling for days. Both drove regulatory reform — expansion of severe-accident management guidelines, filtered containment vents, hardened vents for BWR suppression pools, and FLEX (diverse and flexible mitigation capability) mobile equipment staged at every plant.

## Decommissioning

Every reactor reaches end of life — typically 40-60 years for the pressure vessel, which suffers neutron embrittlement. Three disposition strategies:

1. **Immediate dismantling**: Begin within months of shutdown, complete in 5-10 years. Requires hot-cell handling of activated components. Used when workforces and funding are available.
2. **Safe storage (SAFSTOR)**: De-fuel, secure the plant, wait 40-60 years while radioactivity decays by 10-100×. Lower occupational dose and deferred cost. Used at most US commercial plants.
3. **Entombment**: Encase in situ. Used only for specialized cases (Chernobyl shelter object). Not a general option for power reactors because of site size.

Activated concrete in the bioshield (containing Eu-152, Co-60, Cs-134) and the reactor vessel itself (Ni-63, Co-60) dominate low-level waste volumes. Spent fuel remains the highest-activity stream and must move to either reprocessing or a geological repository — the unresolved back-end question for once-through fuel cycles.

## Bootstrap Position

Nuclear fission is a pinnacle technology in this tree. The minimum prerequisites — pressure-vessel steel forgings, zirconium cladding, enrichment or heavy water, instrumentation and control, licensed operators, and a waste-management plan — together require most of the rest of the tech tree to exist first. The payoff is the only practical baseload source independent of geography (unlike hydroelectric or geothermal), weather (unlike wind or solar), and continuous fuel logistics (unlike coal or biomass).

The first reactor a bootstrapping civilization builds is almost certainly a research reactor (10-50 MW thermal, pool-type, plate fuel). It produces neutrons for isotope manufacture, validates reactor physics codes, and trains operators — at a fraction of the cost and risk of a power reactor. Power generation can follow once the supply chain, regulatory body, and operating experience exist.

## Troubleshooting

| Problem | Probable Cause | Mitigation |
|---------|---------------|------------|
| Cladding failure (rising coolant iodine) | Manufacturing defect, debris fretting, or pellet-cladding interaction during load changes | Power suppression to localize the failed rod; planned shutdown and fuel assembly replacement at next outage |
| Xenon oscillations (spatial flux instability) | Local power perturbations propagate through xenon absorption in large cores | Engage spatial power-distribution control; insert selected control rods to flatten flux; verify axial offset within band |
| Excess boron dilution (loss of shutdown margin) | Inadvertent addition of unborated water to primary (CVCS malfunction, seal-injection leak) | Isolate dilution source; re-borate via boric acid makeup tanks; verify rod worth and SDM margin |
| Steam generator tube leak | Inconel 600/690 stress-corrosion cracking at dents or support plates | Reduce power to limit activity release; isolate and blank the affected tube (plug); plan SG replacement if plugging exceeds 5-10% |
| Pressure-temperature excursion outside the LCO | Operator error during heatup/cooldown exceeding ramp limits (e.g., 50°C/hour) | Stop heating/cooling; verify vessel RTNDT margin to current temperature before resuming; root-cause the procedural violation |

## See Also

- **[Nuclear Fuel Cycle](./nuclear-fuel-cycle.md)** — Front-end (mining, enrichment, fabrication) and back-end (storage, reprocessing, disposition) of reactor fuel
- **[Reactor Design](./reactor-design.md)** — Vessel, core, coolant, and safety system engineering for fission reactors
- **[Isotope Production](./isotope-production.md)** — Reactor neutron-driven manufacture of Pu-238, Sr-90, Co-60, and other radioisotopes
- **[Electricity Generation](./electricity.md)** — Generators, transformers, and grid synchronization for nuclear plants
- **[Iron & Steel](../metals/iron-steel.md)** — Reactor pressure vessels, primary piping, containment rebar
- **[Radiation Safety](../ehs/radiation-safety.md)** — Shielding, dosimetry, contamination control, ALARA
- **[Steam Power](./steam-power.md)** — Rankine cycle fundamentals shared with fossil and geothermal plants
- **[Cooling Systems](./cooling.md)** — Wet and dry cooling towers for turbine condenser heat rejection
- **[Chemistry](../chemistry/acids-bases.md)** — Boric acid (chemical shim), hydrazine (oxygen scavenger), lithium hydroxide (pH control)

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
