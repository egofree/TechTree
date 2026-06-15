# Reactor Design

> **Node ID**: energy.nuclear-fission.reactor-design
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.nuclear-fission`](./nuclear-fission.md), [`metals.iron-steel`](../metals/iron-steel.md), [`energy.cooling`](./cooling.md)
> **Enables**: [`energy.electricity`](./electricity.md), isotope production (medical, industrial, RTG fuel)
> **Timeline**: Years 30-100+
> **Outputs**: reactor_vessel, control_system, coolant_system, neutron_source
> **Critical**: No — reactor design is a process specialization within the non-critical nuclear fission capability; it presupposes a mature industrial base (vessel-steel forging, zirconium refining, precision instrumentation, licensed operators) that itself requires decades of prior capability buildup

## Overview

Reactor design is the engineering discipline of building a vessel in which a controlled nuclear chain reaction sustains itself at a selectable power level for months or years between refueling. The fission of a single U-235 nucleus releases ~200 MeV and 2-3 neutrons; the designer's task is to arrange fuel, moderator, coolant, and neutron absorbers so that exactly one of those neutrons (on average) goes on to cause another fission. Hold that balance at unity and the reactor runs steady; tilt it a fraction of a percent and power climbs or falls on a controllable timescale. This article covers the reactor types a bootstrapping civilization would consider, the core physics that governs their behavior, and the control, coolant, and safety systems that make them operable.

The design space is constrained by a few immutable facts: the delayed-neutron fraction (≈0.65% for U-235) sets the timescale on which a reactor can be controlled; the Doppler coefficient (negative, fast-acting) provides the inherent shutdown tendency as fuel heats up; and the temperature limit of the cladding (≈1200°C before rapid oxidation in steam) sets the hard boundary that every accident scenario must respect. Within those bounds, the choice of coolant and moderator defines the reactor type — and with it the enrichment requirement, power density, thermal efficiency, and the entire supply chain that must exist before construction. See [Nuclear Fission Power](./nuclear-fission.md) for the parent capability and fuel-cycle context.

## Reactor Types

The world's operating reactors fall into a small number of families, each defined by its choice of coolant and moderator. The comparison below is the designer's first decision tree: each row implies a different industrial base, a different fuel form, and a different safety case.

### Reactor Type Comparison

| Type | Coolant | Moderator | Pressure (MPa) | Coolant Outlet (°C) | Enrichment (% U-235) | Thermal Efficiency (%) | Power Density (MW/m³) | Notes |
|------|---------|-----------|----------------|----------------------|----------------------|------------------------|-----------------------|-------|
| **PWR** (Pressurized Water) | Light water | Light water | 15.5 | 320 | 3-5 | 32-34 | ~100 | Most common (~300 units worldwide); zircaloy-clad UO₂ pellets; secondary steam loop |
| **BWR** (Boiling Water) | Light water (boiling) | Light water | 7.2 | 285 | 2.5-4 | 30-32 | ~50 | Direct cycle — steam generated in core drives turbine; simpler than PWR, larger vessel |
| **CANDU / PHWR** | Heavy water (D₂O) | Heavy water (99.75% pure) | ~10 | 310 | 0.72 (natural U) | 28-30 | ~12 | No enrichment needed; pressure-tube design (not single pressure vessel); online refueling |
| **Gas-cooled** (Magnox/AGR/HTGR) | CO₂ or helium | Graphite | 2-7 (He up to 7) | 640-950 (HTGR) | Variable (natural to 20%) | 35-42 (HTGR) | 2-10 | Graphite-moderated; Magnox/AGR (CO₂) in UK; HTGR (He, TRISO particle fuel, 700-950°C) |
| **Liquid metal** (SFR, LFR) | Liquid sodium or lead | None (fast spectrum) | ~0.1 (Na) | 500-550 | 15-20% (MOX) | 38-42 | 200-300 | Fast-neutron spectrum enables breeding and actinide burning; sodium reacts violently with water |
| **Research reactor** (pool-type) | Light water | Light water / D₂O / graphite | atmospheric | 40-70 | 19.75 (LEU) | n/a (heat only) | 0.01-1 | Plate fuel for high surface area; neutron flux 10¹⁴-10¹⁵ n/cm²·s; isotope production |

### PWR — Pressurized Water Reactor

The dominant reactor type worldwide. The primary loop is held at 15.5 MPa to keep water liquid at 320°C (well above the 100°C atmospheric boiling point), then transfers heat through a steam generator to a secondary loop that boils at ~6 MPa to drive a conventional turbine. The two-loop isolation keeps reactor coolant (and any fission-product activity) inside the primary boundary. Fuel is UO₂ ceramic pellets enriched to 3-5% U-235, stacked in Zircaloy-4 tubes arranged in 17×17 assemblies. A typical 1 GWe PWR core contains 193 assemblies and runs 12-18 months between refuelings.

### BWR — Boiling Water Reactor

The BWR boils water directly in the core at 7.2 MPa (285°C core exit), eliminating the steam generator and its associated temperature drop. This raises efficiency slightly and lowers the primary-system pressure, but puts radioactive steam through the turbine (N-16 activity requires shielding of the turbine building during operation). The lower power density (~50 MW/m³ vs ~100 MW/m³ for PWR) and direct-cycle contamination trade-off make the BWR simpler to build but marginally harder to maintain.

### CANDU / PHWR — Heavy-Water Reactor

The CANDU (CANada Deuterium Uranium) uses 99.75% pure heavy water (D₂O) as both moderator and coolant. Deuterium's low neutron-capture cross-section preserves enough neutrons that natural uranium (0.72% U-235) sustains criticality — **no enrichment plant is required**. This is a profound supply-chain simplification, bought at the cost of expensive D₂O moderator (~$300/kg, hundreds of tonnes per reactor) and a pressure-tube design (hundreds of individual pressure tubes rather than one large forged vessel). Online refueling — fuel bundles pushed through the tubes while the reactor runs — enables high capacity factor.

### Gas-Cooled Reactors

UK Magnox and AGR designs use CO₂ coolant with graphite moderator and natural or low-enriched uranium in magnesium-alloy or stainless-steel cladding. The high-temperature gas-cooled reactor (HTGR) variant uses helium coolant and TRISO-coated particle fuel (tiny UO₂ kernels triple-coated in pyrolytic carbon and silicon carbide), achieving 700-950°C outlet temperatures — high enough for hydrogen production via thermochemical cycles. TRISO fuel retains fission products to 1600°C, an inherent safety margin. The low power density (2-10 MW/m³) means large cores.

### Liquid-Metal-Cooled Fast Reactors

Fast reactors operate without a moderator — the neutrons remain at their 2 MeV birth energies, where U-238 is fissionable and where plutonium can be bred from U-238 faster than it is consumed (in a breeder configuration). Sodium-cooled fast reactors (SFR, e.g., BN-800) run at near-atmospheric pressure (liquid sodium's boiling point is 883°C, so no pressurization is needed to keep it liquid at 500-550°C) and reach 38-42% thermal efficiency. The penalty: sodium reacts explosively with water and burns in air, requiring an intermediate sodium loop between the radioactive primary sodium and the steam generator. Lead-cooled reactors avoid the water reactivity but face corrosion challenges.

### Research Reactors

Pool-type research reactors are the first reactor a bootstrapping civilization would build. They operate at 10 kW to 100 MW thermal at atmospheric pressure, using plate-type fuel (high surface-to-volume ratio) for efficient heat removal at modest temperatures. Their purpose is not electricity but **neutron flux**: 10¹⁴-10¹⁵ n/cm²·s in the core, sufficient to irradiate target nuclides for isotope production (Co-60 for sterilization, Mo-99 for medical imaging, Np-237→Pu-238 for RTG fuel). A 10-50 MW thermal research reactor costs a tenth of a power reactor, validates reactor physics codes, and trains operators — the prerequisite steps before committing to a power plant.

## Reactor Pressure Vessel

The reactor pressure vessel (RPV) is the single largest steel component in a power reactor — a forged low-alloy steel cylinder (SA-508 Grade 3 Class 1 in PWRs) ~12 m tall, ~4-5 m diameter, 200-300 mm wall thickness, weighing ~400 tonnes for a 1 GWe plant. The vessel houses the core, control-rod drive mechanisms, and reactor internals; it must retain its fracture toughness over a 40-60 year design life while accumulating neutron fluence of ~10¹⁹ n/cm² (E > 1 MeV) at the core beltline.

Neutron irradiation embrittles the vessel steel — the ductile-to-brittle transition temperature (RTNDT) shifts upward over the plant life. Pressure-temperature (P-T) limit curves define the permitted operating envelope: the vessel cannot be pressurized above a threshold until it has warmed above its current RTNDT, preventing brittle fracture during startup and shutdown. Periodic surveillance capsule withdrawal and annealing (in some designs) track and mitigate this aging. See [Iron & Steel](../metals/iron-steel.md) for the underlying metallurgy.

## Fuel and Cladding

### Fuel Form

Light-water reactor fuel is uranium dioxide (UO₂) — a ceramic with melting point 2,865°C, sintered to 95-97% theoretical density (10.4-10.7 g/cm³) as pellets 8-13 mm diameter, 10-15 mm tall. The pellets are stacked end-to-end in Zircaloy cladding tubes to form fuel rods ~3.7 m long; rods are bundled into assemblies (17×17 for modern PWR, 10×10 for BWR) with spacer grids every 400-600 mm to maintain rod-to-rod spacing and promote coolant mixing.

The UO₂ ceramic retains fission products well — only the volatile fraction (~10% of iodine, cesium) migrates to the pellet-cladding gap under normal operation. Pellet microstructure (grain size 8-25 µm, pore distribution) is engineered to balance fission-gas release (small grains release more, swelling the rod plenum) against densification (which can cause pellet-cladding mechanical interaction).

### Cladding

Zircaloy-4 (Zr-1.5%Sn-0.2%Fe-0.1%Cr) or Zirlo (Zr-1.0%Sn-1.0%Nb-0.1%Fe) tubes have a thermal-neutron capture cross-section of ~0.18 barn — critical for neutron economy, since the cladding surrounds every fuel pellet. Wall thickness 0.57-0.62 mm, with a thin (~1 µm) oxide layer that grows over fuel life. The hard limit is the **cladding temperature excursion**: above 1200°C, zirconium reacts with steam in an exothermic oxidation reaction (Zr + 2H₂O → ZrO₂ + 2H₂ + heat), generating hydrogen and degrading the cladding. Every LOCA safety analysis must demonstrate that cladding stays below this limit with margin.

## Core Physics

### Effective Multiplication Factor (k_eff)

The **effective multiplication factor** is the ratio of neutrons in one generation to neutrons in the preceding generation:

- **k_eff = 1** (critical): chain reaction is steady — reactor runs at constant power
- **k_eff > 1** (supercritical): power rises
- **k_eff < 1** (subcritical): power falls

The reactor designer's daily task is to hold k_eff at 1.000 within a few pcm (percent-mille: 1 pcm = 10⁻⁵ Δk/k). Reactivity is the deviation from criticality: ρ = (k_eff − 1)/k_eff. Control rods, dissolved boron, burnable poisons, and fuel depletion all manipulate reactivity on different timescales.

### Delayed Neutrons

Only **0.6-0.7% of neutrons** from U-235 fission are "delayed" — emitted seconds to minutes after the fission event itself, from the radioactive decay of fission-product precursors (e.g., Br-87, I-137). The remaining 99.3% are "prompt," born within 10⁻¹⁴ s of fission. This tiny delayed fraction is the entire reason reactors are controllable: as long as k_eff stays below the prompt-critical threshold (k ≈ 1.0065 for U-235), the chain reaction's dynamics are governed by the seconds-to-minutes delayed-neutron precursor decay rather than the microsecond prompt-neutron lifetime. Pu-239 has a delayed fraction of only 0.21% — plutonium-fueled reactors are correspondingly faster and harder to control. Lose the delayed-neutron margin (e.g., by rapid reactivity insertion) and the reactor is prompt critical, with power doubling times too short for mechanical systems to respond.

### Reactor Period

The **reactor period** T is the time for power to change by a factor of e:

> T = l* / (k_eff − 1)

where l* is the mean neutron generation time (~10⁻⁴ s for thermal reactors, ~10⁻⁷ s for fast reactors). Without delayed neutrons, a small reactivity insertion of 0.1% would give T ≈ 0.1 s — far too fast for control systems. With delayed neutrons, the effective period stretches to tens of seconds, giving operators and automatic systems time to respond. The inhour equation relates the observed reactor period to the reactivity and the delayed-neutron group constants (six groups for U-235, with precursor half-lives from 0.23 s to 55 s). A reactor period of 20-50 seconds is typical for a controlled approach to criticality; operators adjust rod position to maintain this period as power rises toward the target.

### Shutdown Margin

The **shutdown margin** is the reactivity hold available with the most reactive control rod fully withdrawn (single-failure criterion) at cold, zero-power conditions — typically ≥1-2% Δk/k. This guarantees the reactor stays subcritical even if one rod sticks. Shutdown margin is verified during startup physics testing: the rod under test is withdrawn to its fully-out position and the reactor's subcritical multiplication (count rate response to a neutron source) is measured to confirm the hold.

### Reactivity Balance

At beginning of cycle (BOC), a PWR core carries substantial **excess reactivity** (~10% Δk/k) to compensate for fuel depletion over the 12-18 month cycle. This excess is held down by chemical shim (boron), burnable poisons, and control rods. As fuel depletes and fission products (notably xenon-135 and samarium-149) build in, reactivity drops, and the operator reduces boron concentration and withdraws rods to maintain k_eff = 1. The art of core design is shaping the burnable poison loading so that the excess reactivity curve matches the depletion curve, minimizing rod motion and boron adjustments.

### Feedback Coefficients

The reactor's response to perturbations is governed by inherent reactivity feedback — how k_eff changes as temperature, void fraction, and fuel depletion change:

- **Doppler coefficient** (fuel temperature): Negative and prompt. As fuel temperature rises, U-238 resonance absorption broadens (Doppler broadening), capturing more neutrons and reducing reactivity. Acts in milliseconds — the primary inherent shutdown mechanism. Typical: −3 to −1 pcm/K.
- **Moderator temperature coefficient**: As moderator heats it expands, reducing density and moderation. Negative in PWRs at end-of-cycle (good); can be positive at beginning-of-cycle when boron concentration is high (the boron's moderating contribution drops with temperature, partially offsetting).
- **Void coefficient**: Reactivity change from steam voids in the moderator. Negative in PWRs (voids reduce moderation → fewer thermal neutrons). Was positive in the RBMK design at Chernobyl — a design flaw central to that accident. BWR void coefficients are designed slightly negative or small-positive over the operating range.
- **Coolant density coefficient**: Related — as coolant density drops, it moderates less and absorbs less.

A well-designed reactor has **net negative feedback**: any temperature rise reduces reactivity, stabilizing power. This is the single most important passive safety property.

## Control Systems

### Control Rods

Control rods are tubes or assemblies of strong neutron absorbers that slide into (or out of) the core to reduce (or increase) reactivity. Materials:

- **Boron carbide (B₄C)** — B-10 has a thermal-neutron capture cross-section of 3,840 barns. Cheap, used in BWR control blades and fast-reactor absorber rods. Brittle; tends to swell under irradiation.
- **Silver-indium-cadmium (Ag 80%-In 15%-Cd 5%)** — The standard PWR control-rod absorber. Ag-In-Cd has a broad absorption spectrum (cadmium for thermal, silver and indium for epithermal), good mechanical properties, and acceptable irradiation stability. Encapsulated in stainless steel clad.
- **Hafnium** — Excellent neutron absorber across the energy spectrum, good mechanical and corrosion properties, used in naval reactors where longevity matters (hafnium does not swell like B₄C). Expensive and scarce.

### Burnable Poisons

Burnable poisons are neutron absorbers distributed through the fuel that deplete (burn) over the fuel cycle, compensating for the excess reactivity of fresh fuel. As the fuel's reactivity drops with depletion, the poison burns down too — flattening the reactivity curve over the 12-18 month cycle:

- **Gadolinium (Gd₂O₃)** mixed into selected UO₂ fuel pellets (Gd-157 capture cross-section = 254,000 barns — the largest of any stable nuclide)
- **Boron as ZrB₂ coating** on fuel pellet surfaces (Integral Fuel Burnable Absorber, IFBA)
- **Erbium (Er₂O₃)** — slower burnup rate, used in some BWR designs

### Chemical Shim

PWRs dissolve boric acid (H₃BO₃) in the primary coolant at 0-2,000 ppm B to provide **slow, uniform reactivity control**. Boron concentration is gradually reduced over the fuel cycle to compensate for fuel depletion, with the chemical and volume control system (CVCS) adding borated or dilute water. Chemical shim lets the designer size the control rods for fast shutdown rather than full reactivity hold, simplifying rod-drive mechanisms. BWRs cannot use chemical shim — boiling would concentrate boron in the remaining liquid.

## Coolant Systems

### Primary Loop (PWR)

The PWR primary loop circulates water at 15.5 MPa from the core (320°C hot leg, 290°C cold leg) through 2-4 steam generators and back via reactor coolant pumps. Typical 4-loop plant: 4 cold legs, 4 hot legs, 4 steam generators, 4 reactor coolant pumps (RCPs). Total primary flow: ~20 m³/s. The **pressurizer** — a steam-water tank connected to one hot leg — maintains primary pressure by electrical heating (to raise pressure) and spray (to lower pressure). Pressure setpoint: 15.5 ± 0.2 MPa.

### Secondary Loop (PWR)

The secondary loop boils in the steam generator (Inconel 690 U-tubes), producing saturated or slightly superheated steam at ~6 MPa, 275°C, which drives the turbine-condenser-feedwater train of a conventional Rankine cycle. The secondary side is the boundary that keeps primary activity out of the turbine — a key safety and maintainability advantage over the BWR's direct cycle.

### BWR Coolant

The BWR eliminates the steam generator: recirculation pumps drive a portion of the core flow through jet pumps, and the resulting two-phase mixture (quality ~15% at core exit) passes through steam separators and dryers directly to the turbine. Core flow control (varying recirculation rate) provides ~25% of the load-following capability without moving control rods.

### Cooling Tower

The turbine condenser rejects ~2 GW of waste heat (for a 1 GWe plant with 33% efficiency) to a cooling water source — once-through river/ocean water, or a wet cooling tower (~5°C approach to wet-bulb temperature, evaporation of ~0.5 m³/s per 100 MWe). See [Cooling Systems](./cooling.md) for the refrigeration and cooling-tower fundamentals shared with fossil and geothermal plants.

## Safety Systems

### Defense in Depth

Nuclear safety rests on **defense in depth** — multiple independent layers so that no single failure can release radioactivity:

1. Fuel matrix (UO₂ ceramic retains fission products to ~2800°C)
2. Zircaloy cladding (first physical barrier)
3. Reactor pressure vessel and primary piping
4. Containment building (1.2-2.0 m reinforced concrete, leak-tested to <0.1% volume/day)
5. Exclusion area and emergency planning zone

### Redundancy (N+2)

Safety systems are built with **N+2 redundancy** (or better): two trains each capable of 100% of the safety function, plus margin. The emergency core cooling system (ECCS) typically has 2-4 independent trains of high-pressure injection, accumulators (passive, nitrogen-pressurized tanks at ~4 MPa), and low-pressure injection. Any one train can cool the core; the second covers single failure; some designs add a third for maintenance unavailability.

### Emergency Core Cooling System (ECCS)

On a loss-of-coolant accident (LOCA) signal (low primary pressure or low pressurizer level), ECCS triggers:

1. **Reactor trip** — control rods drop by gravity into the core (scram), inserting ~3-4% Δk/k shutdown margin in 1-4 seconds
2. **High-pressure injection** — charging pumps inject borated water from the refueling water storage tank to maintain primary inventory at high pressure
3. **Accumulators** — passive nitrogen-pressurized tanks discharge into the cold legs when primary pressure drops below ~4 MPa
4. **Low-pressure injection** — residual heat removal (RHR) pumps inject once primary pressure has fallen, providing long-term recirculation from the containment sump

### Containment Building

The containment is the final barrier — a steel-lined reinforced concrete shell designed to contain the peak pressure and temperature of a design-basis accident (typically ~0.4 MPa, 150°C) with margin. Large dry containments (~70,000 m³ free volume for a 1 GWe PWR) or ice-condenser designs limit peak pressure. Filtered venting (post-Fukushima requirement in many jurisdictions) provides a controlled release path for beyond-design-basis accidents.

## Operational Considerations

### Load Following and Maneuvering

Modern reactors can load-follow (vary power to match grid demand) over a range of 50-100% of rated power at ramp rates of ±5%/minute. PWR load-following combines control-rod insertion (gray rods in some designs, which absorb neutrons without strongly distorting the power shape) with chemical-shim boron adjustment. BWRs load-follow primarily by varying core recirculation flow — a faster-acting mechanism. Baseload operation (constant full power) remains the economic and fuel-cycle optimum: capacity factor of 90-93% is achievable, the highest of any dispatchable source.

### Xenon and Samarium Transients

**Xenon-135** (σ_a = 2.6 × 10⁶ barns — the largest capture cross-section of any nuclide) is both produced directly from fission (~0.3% yield) and (mostly) from the decay of I-135 (6.6% fission yield, half-life 6.6 h). Xenon reaches equilibrium after ~40 hours of steady operation. On shutdown, iodine continues to decay into xenon but xenon is no longer being "burned off" by neutron absorption — xenon concentration rises for ~4-7 hours (the "xenon peak"), then decays with its 9.1 h half-life. During this peak, the reactor may be unable to restart (iodine pit) until xenon decays below the available shutdown margin. Large power reactors must account for xenon in startup planning.

**Samarium-149** (σ_a = 4.1 × 10⁴ barns) is a stable fission product that builds in over the cycle to a near-equilibrium level; it does not decay away after shutdown (the precursor Pm-149 has 53-hour half-life). Samarium's reactivity hold (~0.6% Δk/k) is a permanent depletion effect that must be compensated by excess fuel reactivity.

### Fuel Cycles and Burnup

Light-water reactor fuel typically reaches 45-55 GWd/tonne burnup before discharge — meaning each tonne of uranium has released 45-55 GW-days of thermal energy. Higher-burnup fuel (up to 60-70 GWd/t in modern designs) reduces refueling frequency and waste volume but increases fuel enrichment requirements and cladding duty. Fast-reactor fuel reaches 60-120 GWd/t. CANDU natural-uranium fuel discharges at only 7-9 GWd/t — but at no enrichment cost, the fuel-cost arithmetic is favorable.

## Quantitative Parameters

| Parameter | PWR | BWR | CANDU | HTGR | SFR (BN-800) |
|-----------|-----|-----|-------|------|--------------|
| Thermal power (MW_th) | 3,000 | 3,300 | 2,800 | 600 | 2,100 |
| Electric power (MW_e) | 1,000 | 1,100 | 850 | 250 | 800 |
| Thermal efficiency (%) | 32-34 | 30-32 | 28-30 | 35-42 | 38-42 |
| Power density (MW/m³) | ~100 | ~50 | ~12 | 2-10 | 200-300 |
| Specific power (kW/kg U) | 30-40 | 25-30 | 18-22 | 80-100 | 100-200 |
| Fuel temperature (°C, centerline) | 1,400-1,700 | 1,500-1,800 | 1,500 | 1,000-1,250 | 1,500-2,000 |
| Clad surface temperature (°C) | 320-350 | 285-300 | 310-330 | 700-950 | 500-550 |
| Coolant flow rate (m³/s) | ~20 | ~13 | ~12 | ~0.3 (He) | ~3.5 (Na) |
| Coolant velocity in core (m/s) | 4-5 | 2-3 | 5-7 | 5-10 | 3-5 |
| Fuel burnup (GWd/t) | 45-55 | 45-55 | 7-9 (natural U) | 80-100 | 60-120 |
| Capacity factor (%) | 90-93 | 90-92 | 88-93 | 85-90 | 80-85 |

Power density is the parameter that most directly drives the reactor's character. PWR's ~100 MW/m³ means a compact core (~30 m³) and aggressive cooling; CANDU's ~12 MW/m³ means a large calandria but enables natural-uranium fueling; SFR's ~300 MW/m³ means a tiny core running very hot, with the sodium coolant carrying the heat away with minimal pumping power. The trade-off across the spectrum: higher power density means smaller, cheaper cores but tighter safety margins and more demanding transient analysis; lower power density means larger cores and more forgiving thermal response but higher capital cost per megawatt.

## Materials and Prerequisites

- **Pressure vessel steel** — Forged SA-508 Gr.3 Cl.1, 200-300 mm wall, one of the largest single steel forgings made. See [Iron & Steel](../metals/iron-steel.md).
- **Zirconium cladding** — Zircaloy-4 or Zirlo tubes, 0.57-0.62 mm wall, low neutron-capture cross-section. See [Metals](../metals/index.md).
- **Uranium fuel** — UO₂ ceramic pellets enriched to 3-5% U-235 (light water) or natural 0.72% (CANDU). See [Chemistry](../chemistry/acids-bases.md).
- **Heavy water moderator** — D₂O at 99.75% purity for CANDU (~$300/kg). See [Chemistry](../chemistry/index.md).
- **Control materials** — B₄C, Ag-In-Cd, hafnium, gadolinium, boron (as ZrB₂ or boric acid). See [Chemistry](../chemistry/index.md).
- **Shielding concrete** — Magnetite or barite aggregate, 3,500-4,200 kg/m³ density, 1.2-2.0 m wall thickness. See [Construction](../construction/index.md).

## Bootstrap Position

The first reactor a bootstrapping civilization builds is a **research reactor** — 10-50 MW thermal, pool-type, plate fuel, 19.75% LEU. It produces the neutron flux for isotope production (medical, industrial, RTG fuel), validates reactor physics codes, and trains operators at a fraction of the cost and risk of a power reactor. Power generation follows only once the supply chain (vessel forging, cladding tube drawing, enrichment or heavy water, instrumentation, regulatory body, operating experience) is mature. See the parent [Nuclear Fission Power](./nuclear-fission.md) capability for the full prerequisite chain.

## Troubleshooting

| Problem | Probable Cause | Mitigation |
|---------|---------------|------------|
| Reactor period too short during startup | Excess reactivity from mis-calibrated rod worths or cold core over-moderation | Reduce withdrawal rate; if period < 10 s, reverse rod motion; verify source range count rate against predicted |
| Xenon oscillation (spatial flux instability) | Local power perturbation propagating through xenon absorption | Engage spatial power-distribution control; insert selected gray rods to flatten axial/azimuthal flux; monitor with in-core detectors |
| Loss of shutdown margin at BOC | Inadvertent boron dilution (CVCS leak, unborated water ingress) | Isolate dilution source; re-borate via makeup tanks; verify rod worth and SDM margin before further power changes |
| Cladding failure (rising coolant iodine/cesium) | Manufacturing defect, debris fretting, or pellet-cladding interaction during load changes | Power suppression to localize failed rod; planned shutdown and fuel assembly replacement at next outage |
| Pressurizer level unstable | Steam-space non-condensable gas (H₂, N₂) or spray valve malfunction | Vent non-condensables; verify spray flow path; check backup heater operation |
| Steam generator tube leak | Inconel stress-corrosion cracking at dents or support plates | Reduce power to limit activity release; isolate and plug affected tube; plan SG replacement if plugging exceeds 5-10% |
| Rod stuck on trip | Drive mechanism mechanical binding or coil failure | Enter abnormal operating procedure; verify rod drop time on next refueling; investigate stuck rod cause before restart |

## See Also

- **[Nuclear Fission Power](./nuclear-fission.md)** — Parent capability: fuel cycle, materials inventory, waste streams
- **[Cooling Systems](./cooling.md)** — Cooling-tower and refrigeration fundamentals shared with all thermal power plants
- **[Steam Power](./steam-power.md)** — Rankine cycle that converts reactor heat to electricity
- **[Steam Turbines](./steam-turbines.md)** — Turbine-generator sets for nuclear plants
- **[Electricity Generation](./electricity.md)** — Grid connection, transformers, power distribution
- **[Iron & Steel](../metals/iron-steel.md)** — Pressure-vessel steel, primary piping, containment rebar
- **[Radiation Safety](../ehs/radiation-safety.md)** — Shielding, dosimetry, contamination control, ALARA

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
