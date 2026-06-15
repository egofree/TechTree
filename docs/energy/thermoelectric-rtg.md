# Thermoelectric RTG

> **Node ID**: energy.radioisotope-power.thermoelectric-rtg
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.radioisotope-power`](./radioisotope-power.md), [`metals.iron-steel`](../metals/iron-steel.md), [`energy.electricity`](./electricity.md)
> **Enables**: None
> **Timeline**: Years 30-100+
> **Outputs**: rtg_electricity, thermoelectric_heat
> **Critical**: No — thermoelectric RTGs are a process specialization of the non-critical radioisotope-power capability; every flight unit presupposes a mature Pu-238 production line, hot-cell fuel fabrication, semiconductor thermoelectric manufacturing, and a launch-qualified safety case, all of which arrive decades into the industrial buildup

## Overview

Thermoelectric radioisotope thermoelectric generators (RTGs) are the workhorse of space nuclear power. Since the first SNAP-3B launched on Transit 4A in June 1961, every nuclear-electric power source ever flown by the United States has used the Seebeck effect to convert the decay heat of plutonium-238 directly into electricity, with no moving parts, no turbines, no bearings, and no consumable working fluid. A thermocouple junction heated on one side by the isotope and cooled on the other by a space radiator drives electrons from hot to cold; wire enough couples in series and the result is a steady DC current that flows for as long as the fuel stays hot — 87.7 years for one half-life of Pu-238.

The trade-off is brutal efficiency. A flight RTG converts only 5-8% of its decay heat to electricity; the remaining 92-95% must be radiated to space as waste heat. The GPHS-RTG that powered Cassini generated 300 W of electricity and 4,200 W of waste heat, requiring a 7.4 m² radiator running at 300°C. That low efficiency is the price of total reliability: thermoelectric converters have no failure modes associated with moving parts, fluid leaks, or mechanical wear. Every NASA mission beyond Mars carries thermoelectric RTGs because no other conversion method has accumulated the flight heritage — Voyager 1's three RTGs still produced 219 W in 2024, 47 years after launch.

This article covers the six flight RTG variants fielded since 1961, the thermoelectric materials that define their performance (SiGe, PbTe/TAGS, skutterudite), the General Purpose Heat Source (GPHS) module that has standardised fuel containment since 1989, system integration (thermocouple ladders, hot shoe, radiator, Al 2219-T6 housing), and the commercial Sr-90 RTGs now being developed for terrestrial maritime use. See [Radioisotope Power](./radioisotope-power.md) for the parent capability and an overview of all conversion methods (Stirling, TPV, betavoltaic).

## Operating Principle — the Seebeck Effect

A temperature gradient ΔT across a thermoelectric material drives a voltage V = S·ΔT, where S is the Seebeck coefficient (typically 100-400 μV/K for semiconductors). A thermocouple is a pair of legs — one n-type (electron conduction) and one p-type (hole conduction) — wired in series electrical but parallel thermal, so the two voltages add. Cold junctions connect to an external load; hot junctions sit against the heat source.

The conversion efficiency is governed by the dimensionless figure of merit:

**ZT = S²σT / κ**

where σ is electrical conductivity and κ is thermal conductivity. A higher ZT means more electricity extracted per unit of heat flow. The two quantities pull against each other: good electrical conductors (metals) are also good thermal conductors (Wiedemann-Franz law), and insulators have high S but negligible σ. The optimum lies in heavily-doped semiconductors at carrier concentrations of 10¹⁹ carriers/cm³. Carnot-limited efficiency is approached only as ZT → ∞; at ZT = 1 the maximum efficiency is roughly 15-20% of Carnot.

A flight RTG stacks 100-300 thermocouples in a series-parallel ladder — series to build voltage (28-30 V bus), parallel branches to survive individual cell shorts. The GPHS-RTG uses 572 SiGe unicouples; the MMRTG uses 768 PbTe/TAGS couples in a thermally-series, electrically-independent arrangement.

## Flight Heritage Variants

Six distinct thermoelectric RTG designs have been built and flown by the United States since 1961. Each represents a distinct generation of fuel form, thermoelectric material, and heat-source engineering.

### SNAP-3B (1961) — the first flight RTG

The Systems for Nuclear Auxiliary Power (SNAP) programme's third design was the first RTG to reach orbit. SNAP-3B7 flew on Transit 4A (29 June 1961) and SNAP-3B8 on Transit 4B (15 November 1961). Each unit generated **2.7 W_e** at beginning of mission (BOM) from **93.79 g of plutonium-238 metal** (specific power 0.56 W/g Pu-238 at the source, ~0.029 W_e/g system). The complete generator massed **2.3 kg** including its lead-shielded capsule. The thermoelectric material was PbTe (lead telluride), hot junction at 590°C, cold junction at 230°C. SNAP-3B operated in orbit for over 15 years (Transit 4B was still transmitting in 1978), far exceeding its design life and proving that solid-state nuclear power was practical for satellites.

### SNAP-19 (1960s-70s) — the interplanetary pioneer

The SNAP-19 family was the first RTG designed for deep-space missions. It flew in three distinct configurations:

- **SNAP-19B2/B3** (1968, Nimbus-B launch failure recovery; Nimbus-III 1969) — 25 W_e per generator, two units per spacecraft.
- **SNAP-19 Pioneer 10/11** (1972/1973 launch) — 40 W_e BOM per generator, four units per spacecraft. Pioneer 10's RTGs operated for 30 years until the last signal in January 2003; Pioneer 11 operated for 22 years.
- **SNAP-19 Viking** (1976 Mars landers) — 42 W_e BOM per generator, two units per lander, using PbTe/TAGS segmented couples. The Viking 1 lander operated on the Martian surface for 6 years 116 days; Viking 2 for 3 years 221 days.

SNAP-19 massed approximately **15 kg** per generator, used **1.654 kg of Pu-238 fuel** per unit (in pressed-pellet form), and employed PbTe n-legs paired with TAGS (tellurium-antimony-germanium-silver, a silver-antimony-telluride alloy) p-legs — the first use of TAGS, which became the heritage material for all subsequent PbTe-class RTGs.

### GPHS-RTG (1989-2006) — the flagship deep-space power source

The General Purpose Heat Source RTG is the most successful RTG ever flown. It powered [Galileo](./index.md) (1989 launch, Jupiter orbiter), Ulysses (1990, solar polar orbiter), Cassini-Huygens (1997, Saturn orbiter), and New Horizons (2006, Pluto flyby). Each GPHS-RTG delivers **285-300 W_e at BOM** from **4,500 W_th of decay heat**, massing **55.9 kg** for a specific power of **5.1 W_e/kg**. Conversion efficiency is ~6.3% (electric output / thermal output).

The heat source comprises **18 General Purpose Heat Source (GPHS) modules** stacked vertically, each module producing ~250 W_th from ~0.6 kg of pressed ²³⁸PuO₂ fuel. The thermoelectric converter is built from **572 silicon-germanium (SiGe) unicouples** arranged around the cylindrical heat source stack. Hot junction temperature: **1,000°C** (1,273 K). Cold junction: **300°C** (573 K), set by the radiator fins. SiGe operates reliably at 1,000°C with a Si₃N₄ anti-sublimation coating that suppresses germanium loss at temperature.

GPHS-RTG telemetry from Voyager's earlier MHW-RTG (the predecessor, 158 W_e, 4.5 kg Pu-238, launched 1977) provides the longest-running engineering dataset in existence: 47+ years of continuous I-V curves, showing 1.0-1.5%/yr degradation from thermocouple sublimation and fuel decay combined. New Horizons' GPHS-RTG produced 245.7 W_e at launch in 2006 and 190 W in early 2024 — exactly tracking the predicted decay curve.

### MMRTG (2011-present) — the Mars surface workhorse

The Multi-Mission RTG, built by Teledyne Energy Systems and Idaho National Laboratory, was designed to operate in both vacuum (deep space) and planetary atmospheres (Mars surface, Titan). It powers Curiosity (MSL, landed 2012) and Perseverance (Mars 2020, landed 2021). Each MMRTG produces **110 W_e at BOM** from **~2,000 W_th**, massing **43.6 kg** (specific power **2.8 W_e/kg**, lower than GPHS-RTG because the atmospheric-rated radiator is heavier). Efficiency ~6%.

The heat source is **8 GPHS modules** (same modular unit as GPHS-RTG, see below). The thermoelectric converter uses **768 PbTe/TAGS thermocouples** segmented for hot-side operation up to **538°C** (811 K), with the cold side at **210°C** (483 K). The MMRTG was specified because PbTe/TAGS operates well at the lower ΔT appropriate for an atmosphere-cooled radiator; SiGe in vacuum would have been more efficient but required redesign for the atmospheric heat-transfer regime.

MMRTG degradation rate is **~4.8% per year** (faster than GPHS-RTG's 1-1.5%/yr) because PbTe/TAGS degrades faster than SiGe at the MMRTG's hot-junction temperature and because the thermoelectric material is exposed to trace oxygen. Curiosity's MMRTG produced 110 W at landing in August 2012; it produced ~85 W in mid-2024 — a 14-year mission still operating well within its 17-year design life. Perseverance's MMRTG is sized to support a 14-year surface mission.

### eMMRTG (Enhanced MMRTG, development paused)

The enhanced MMRTG was a NASA programme to replace PbTe/TAGS with **skutterudite** thermoelectric couples in the MMRTG form factor. Skutterudites (filled CoSb₃ structures, see [Thermoelectric Materials](#thermoelectric-materials) below) achieve ZT ~1.1 in n-type and 0.91 in p-type, roughly double the ZT of PbTe, so the same heat source could produce more power.

The eMMRTG target was **145 W_e** (vs. 110 W_e for MMRTG) at **8% efficiency** from the same 8 GPHS modules and 43.6 kg mass — boosting specific power to 3.3 W_e/kg. Crucially, skutterudite sublimation is slower than PbTe at the MMRTG's operating temperature, cutting degradation rate to **~2.5% per year** (half the MMRTG rate), extending surface-mission life. The eMMRTG was development paused after component-level testing at Teledyne/INL when the Next-Gen RTG programme was prioritised; the skutterudite couple technology remains flight-qualified.

### Next-Gen RTG (in development, targeting 2028)

The Next-Generation RTG is a NASA Aerojet Rocketdyne / Teledyne programme to develop a successor to the MMRTG for missions in the late 2020s and 2030s. The baseline design revives **silicon-germanium (SiGe)** unicouples in a vacuum-rated configuration (the GPHS-RTG heritage material, not PbTe/TAGS) — a deliberate choice to return to the low-degradation, high-temperature SiGe that gave GPHS-RTG its 40+ year lifetime.

Target performance is **~245 W_e** at a specific power of **4.4 W_e/kg**, with a hot junction around 1,000°C. The fuel load is 4 GPHS modules (~1,000 W_th). The Next-Gen RTG is being qualified for both atmospheric (Mars, Titan) and deep-space operation. Critical Design Review and qualification testing target **2028**; the first flight opportunity is the proposed Endurance-A Mars rover or a Titan mission later in the decade. The choice of SiGe reflects a strategic decision: the MMRTG's PbTe/TAGS, while mature, cannot reach the specific power or lifetime goals set by the Decadal Survey.

## RTG Variant Comparison

| Variant | First Flight | BOM Power (W_e) | Mass (kg) | Specific Power (W_e/kg) | Efficiency (%) | Fuel (kg Pu-238) | Hot/Cold Junction (°C) | TE Material | Degradation (%/yr) |
|---------|-------------|-----------------|-----------|-------------------------|----------------|-------------------|------------------------|-------------|---------------------|
| SNAP-3B | 1961 | 2.7 | 2.3 | 1.2 | ~5 | 0.094 (metal) | 590 / 230 | PbTe | n/a |
| SNAP-19 | 1972 | 40 | 15 | 2.7 | ~6 | 1.654 | 540 / 230 | PbTe/TAGS | ~2 |
| MHW-RTG | 1976 | 158 | 37 | 4.3 | ~6.6 | 4.5 | 1000 / 300 | SiGe | ~1.2 |
| GPHS-RTG | 1989 | 285-300 | 55.9 | 5.1 | 6.3 | 10.8 (18 modules) | 1000 / 300 | SiGe | ~1.2 |
| MMRTG | 2011 | 110 | 43.6 | 2.8 | ~6 | 4.8 (8 modules) | 538 / 210 | PbTe/TAGS | 4.8 |
| eMMRTG | dev paused | 145 | ~44 | 3.3 | 8.0 | 4.8 (8 modules) | ~600 / 200 | Skutterudite | 2.5 |
| Next-Gen | target 2028 | ~245 | ~56 | 4.4 | ~8 | ~4.0 (vacuum) | ~1000 / 300 | SiGe (revival) | ~1.5 |

The progression shows a clear trajectory: from 1.2 W_e/kg (SNAP-3B) to a peak of 5.1 W_e/kg (GPHS-RTG), then a regression to 2.8 W_e/kg for MMRTG because PbTe/TAGS required a heavier atmospheric radiator. The Next-Gen RTG seeks to recover the GPHS-RTG's specific power while delivering 2× the electrical output of MMRTG.

### Mission Heritage Timeline

| Year | Mission | RTG Variant | No. of RTGs | Mission Outcome |
|------|---------|-------------|-------------|-----------------|
| 1961 | Transit 4A / 4B | SNAP-3B | 1 each | First RTG in orbit; 15+ yr operation |
| 1969 | Nimbus-III | SNAP-19B | 2 | First RTG on a weather satellite |
| 1972 | Pioneer 10 | SNAP-19 | 4 | First spacecraft to leave solar system; operated 30 yr |
| 1973 | Pioneer 11 | SNAP-19 | 4 | First flyby of Saturn; operated 22 yr |
| 1976 | Viking 1 / 2 | SNAP-19 (Viking) | 2 each | First RTGs on Mars; Viking 1 ran 6 yr 116 d |
| 1977 | Voyager 1 / 2 | MHW-RTG | 3 each | Interstellar mission; 470 W → 219 W over 47 yr |
| 1989 | Galileo | GPHS-RTG | 2 | Jupiter orbiter; 14-yr mission |
| 1990 | Ulysses | GPHS-RTG | 1 | Solar polar orbiter; 19-yr mission |
| 1997 | Cassini-Huygens | GPHS-RTG | 3 | Saturn orbiter; 20-yr mission |
| 2006 | New Horizons | GPHS-RTG | 1 | Pluto flyby 2015; now in Kuiper Belt |
| 2011 | Curiosity (MSL) | MMRTG | 1 | Mars surface; still operating in 2024 |
| 2021 | Perseverance (Mars 2020) | MMRTG | 1 | Mars surface; sample-cache mission in progress |

## Thermoelectric Materials

The thermoelectric material is the heart of an RTG — it defines the hot-junction temperature, the achievable ZT, and the degradation rate over a multi-decade mission. Four material families matter.

### Silicon-Germanium (SiGe) — GPHS-RTG heritage

SiGe (Si₈₀Ge₂₀, doped n with P and p with B) is the high-temperature heritage material, used in MHW-RTG (Voyager, 1976) and GPHS-RTG (Galileo through New Horizons). ZT **~0.6 at 1,273 K** (1,000°C). Hot junction rated to **1,000°C continuous**, with a **Si₃N₄ anti-sublimation coating** (applied as a 0.1 mm sputtered layer) that suppresses germanium vapour loss at temperature — without this coating, SiGe loses Ge at 1.5%/yr and the couple's electrical characteristics drift. With the coating, degradation drops to **~1.0%/yr** combined fuel decay + couple aging.

SiGe's advantage is operating temperature. The Carnot limit at 1,000°C hot / 300°C cold is 65%, so even ZT = 0.6 yields ~6-7% absolute efficiency. SiGe is also mechanically robust — a brittle semiconductor, but its coefficient of thermal expansion matches molybdenum interconnects, so thermal cycling does not crack the legs.

### Lead Telluride / TAGS — MMRTG heritage

PbTe (n-type, doped with PbI₂) paired with TAGS (p-type — Te-Ag-Ge-Sb alloy, specifically (AgSbTe₂)₀.₅₅(GeTe)₀.₄₅) is the lower-temperature heritage material. ZT **~0.8 at 800 K** (527°C). Hot junction rated to **538°C** in the MMRTG. Used in SNAP-19 (Viking, 1976), the Mars rover MMRTGs (2011, 2020), and all atmospheric RTGs.

TAGS — discovered at Teledyne in the 1960s specifically for the SNAP programme — gives a higher p-leg ZT than PbTe alone because its band structure minimises thermal conductivity via point-defect scattering. PbTe/TAGS's weakness is degradation: PbTe sublimates tellurium at 538°C, dropping ZT by 0.5%/1,000 hours. The MMRTG's 4.8%/yr degradation is dominated by this mechanism (the rest is Pu-238 decay). Operating in an atmosphere (Curiosity, Perseverance) makes the sublimation worse than in vacuum.

### Skutterudite — the eMMRTG upgrade candidate

Skutterudites are filled cobalt antimonide structures: **CoSb₃ with rare-earth or alkaline-earth "rattler" atoms** (Yb, Ba, La, Ce) inserted into the crystalline cage. The rattlers scatter phonons without impeding electrons, dropping thermal conductivity while preserving electrical conductivity. ZT **~1.1 in n-type (Yb-filled)** and **0.91 in p-type (La/Fe-substituted)**, peaking at **823 K** (550°C). Skutterudite was the basis of the eMMRTG (145 W_e target, 8% efficiency, 2.5%/yr degradation).

Skutterudite's manufacturing challenge is synthesis — CoSb₃ is a line compound that must be quenched rapidly from the melt to avoid decomposition, then hot-pressed into dense pellets. Multiple-fill skutterudites (double-, triple-filled with combinations of Ba/La/Yb) push n-type ZT above 1.4 in the laboratory, but the flight-qualified material remains the single-filled Yb/CoSb₃ variety developed at JPL and Iowa State in the 2000s.

### Advanced Laboratory Materials — the research frontier

Beyond the flight materials, several laboratory systems achieve much higher ZT but have not yet been qualified for flight:

- **PbTe-SrTe (sodium-doped, strontium-telluride dispersed)** — ZT **~2.5 at 923 K**, demonstrated by Kanatzidis et al. at Northwestern in 2012 (Nature, 2012). The SrTe precipitates scatter phonons selectively; the result is the highest ZT ever measured in a PbTe-family material.
- **Yb₁₄MnSb₁₁** — ZT **~1.3 at 1,200 K**, a Zintl compound discovered at Caltech/JPL as a high-temperature p-leg alternative to SiGe. Higher ZT and higher operating temperature than SiGe.
- **SnSe (tin selenide)** — ZT **~2.6 at 923 K** (single crystal, Zhao et al. *Nature* 2014), but mechanical fragility has prevented device-scale fabrication.
- **Segmented generators** — by layering Bi₂Te₃ (cold side) → PbTe → TAGS or half-Heusler (hot side) across the temperature gradient, segmented couples achieve an **effective ZT ~1.5**, enabling theoretical efficiencies of **~18%**. The eMMRTG and Next-Gen RTG are the flight paths toward segmented architectures.

The figure of merit gap between flight hardware (ZT 0.6-1.1) and laboratory best (ZT 2.0-2.6) represents roughly a 2× efficiency improvement still on the table. The slow pace of flight qualification — 10-15 years per new material — reflects the multi-decade lifetime requirement and the impossibility of replacing a failed thermocouple after launch.

## GPHS Module — the Universal Heat Source Building Block

Since 1989, every US space RTG has used the **General Purpose Heat Source (GPHS)** module as its standardised fuel unit. A GPHS-RTG stacks 18 modules; an MMRTG stacks 8. Each module is a self-contained, launch-survivable capsule designed to contain its plutonium through rocket explosions, atmospheric re-entry, and ground impact.

### Module Specifications

- **Thermal output**: ~250 W_th per module (initial), declining with Pu-238 decay (87.7-yr half-life).
- **Mass**: 1.43 kg (legacy GPHS) to 1.61 kg (improved GPHS with thicker aeroshell).
- **Fuel**: 4 pressed ²³⁸PuO₂ ceramic pellets, ~151 g Pu-238 each (~600 g per module total fuel).
- **Dimensions**: 9.4 cm wide × 9.4 cm deep × 5.3 cm tall per module.

### Multi-Layer Containment Stack

Each GPHS module is built as a nested series of safety barriers, designed so that no single failure can release plutonium:

1. **Iridium-clad fuel capsule (DOP-26 iridium)** — Each of the 4 pellets is encased in a DOP-26 iridium cup welded shut. DOP-26 is a DOP-26 iridium alloy (Ir + 60 ppm W + 50 ppm Th + 50 ppm Al) with **0.64 mm wall thickness**, capsule dimensions 29.4 mm diameter × 29.4 mm tall. Iridium melts at **2,443°C** (2,716 K) — well above typical re-entry temperatures — and retains ductility to 1,200°C, allowing it to deform rather than shatter on impact. DOP-26 is the only iridium alloy qualified for flight; its grain size is controlled via thermomechanical processing at Oak Ridge National Laboratory.
2. **Graphite aeroshell (Fine Weave Pierced Fabric, FWPF)** — The 4 clad capsules sit inside a FWPF graphite aeroshell. FWPF is a 3D carbon-carbon composite (density 1.9 g/cm³) that ablates during atmospheric re-entry, carrying heat away from the iridium capsules. Peak re-entry heating is ~2,400°C; the aeroshell absorbs and radiates this while the iridium stays below 1,400°C.
3. **Carbon-bonded carbon fibre (CBCF) insulation** — Between the aeroshell and the iridium capsules, a CBCF graphite-fibre insulation layer (0.5 cm thick, density 0.2 g/cm³, thermal conductivity 0.2 W/m·K) buffers the iridium from thermal transients. CBCF is a felted graphite composite that survives to 2,500°C.
4. **Frit vent (sintered iridium)** — Each iridium capsule includes a sintered-iridium frit vent that allows helium (produced by alpha decay of Pu-238) to escape without releasing plutonium dust. Without this vent, helium pressure would rupture the capsule within decades; the frit's pore size (~0.5 μm) passes He atoms while blocking PuO₂ particulates.
5. **GIS (graphite impact shell) — outer assembly** — The complete 4-capsule module is wrapped in a FWPF graphite outer shell, forming a self-contained unit that can be handled and stacked.

The GPHS has been safety-tested in over a dozen simulated accident scenarios, including launch vehicle explosions, shrapnel impacts, atmospheric re-entry from orbital velocity, and ground impact on sand, water, and concrete. In every test the plutonium was either contained or recovered in large, non-respirable fragments.

## System Design and Integration

A flight RTG integrates the heat-source stack, thermoelectric converter, thermal insulation, radiator, and structural housing into a single self-contained unit. The major subsystems are:

### Thermocouple Ladder

GPHS-RTG uses 572 SiGe unicouples; MMRTG uses 768 PbTe/TAGS couples. Couples are wired in series to build voltage (28-30 V DC bus) and grouped into parallel strings so that a single cell short (the dominant failure mode) reduces output by 1/N rather than to zero. Each couple is an independent replaceable element during ground assembly — once launched, no replacement is possible.

### Hot Shoe and Cold Stack

The hot junction of each thermocouple is bonded to a **molybdenum hot shoe** that presses against the iridium clad of the GPHS module's outer aeroshell. The cold junction is bonded to a **copper cold stack** that conducts waste heat to the radiator. The bond is a high-temperature braze (Pt-Rh for SiGe at 1,000°C; Ag-Cu-Ti for PbTe at 538°C). Thermal contact resistance at these interfaces is critical: a 1°C contact drop in a ΔT of 700°C costs ~0.15% efficiency per interface.

### Thermal Insulation (MLI)

The heat-source stack is wrapped in **multi-layer insulation (MLI)** — alternating layers of aluminised Mylar or Kapton with Dacron netting spacers. The GPHS-RTG uses 30 layers of MLI; the MMRTG, operating in atmosphere where MLI is less effective, uses a combination of MLI and Min-K fibrous insulation. MLI reduces parasitic heat loss from the stack to the radiator; without it, 30% of the decay heat would bypass the thermocouples entirely.

### Radiator Fins

The cold side of the thermocouple ladder is bonded to a finned radiator. GPHS-RTG uses an aluminum radiator with 8 radial fins; total radiating area ~7.4 m² for 4,200 W of waste heat at 300°C. The Stefan-Boltzmann law (Q = εσAT⁴) governs sizing: doubling power requires either 2× the area or a 19% higher temperature. MMRTG's radiator is heavier per watt because convection to a planetary atmosphere adds a heat-transfer mode that complicates the radiator design.

### Structural Housing

The outer housing is **Aluminum 2219-T6** (an Al-Cu alloy, density 2.84 g/cm³, yield 350 MPa at room temperature). 2219-T6 is weldable, retains strength to 200°C, and was the same alloy used for the S-IC stage of the Saturn V. The housing provides launch-load structural support, a Faraday cage for EMI shielding, and the mounting interface to the spacecraft. See [Iron & Steel](../metals/iron-steel.md) for the broader context of structural metals.

## GPHS-RTG Mass Breakdown

| Subsystem | Mass (kg) | Fraction (%) | Notes |
|-----------|-----------|--------------|-------|
| 18 GPHS modules (fuel + clad + aeroshell) | 25.7 | 46.0 | Includes 10.8 kg PuO₂ fuel |
| Heat source support structure | 4.7 | 8.4 | Graphite spacers, spring preload |
| Thermal insulation (MLI + Min-K) | 6.4 | 11.4 | 30 layers MLI around stack |
| Thermoelectric converter (572 SiGe couples) | 6.2 | 11.1 | Unicouples, hot shoe, cold stack |
| Housing and radiator (Al 2219-T6) | 13.0 | 23.2 | 8 finned radiator panels |
| **Total** | **55.9** | **100.0** | BOM 285-300 W_e, 5.1 W_e/kg |

Nearly half the mass of a GPHS-RTG is the modular heat source — a direct consequence of the multi-layer safety containment. The 2219-T6 housing is the second-largest line item; reducing radiator mass is the primary target of Next-Gen RTG design studies.

## Degradation and Lifetime

RTG power output declines over mission life from three superimposed mechanisms:

1. **Pu-238 radioactive decay** — 87.7-year half-life means thermal output drops 0.79%/yr. This is the irreducible floor: even a perfect converter loses 0.79%/yr.
2. **Thermoelectric material degradation** — Sublimation of volatile species (Te from PbTe at 538°C, Ge from SiGe at 1,000°C if the Si₃N₄ coating fails), dopant diffusion, and contact-resistance increases at the braze joints. PbTe/TAGS degrades at 3-4%/yr on top of fuel decay; SiGe with intact coating degrades at 0.2-0.5%/yr.
3. **Thermal network drift** — MLI compaction, radiator surface emissivity changes from atomic-oxygen attack (in low Earth orbit), and hot-shoe creep all shift the hot/cold ΔT.

Net degradation rates: GPHS-RTG **~1.2%/yr** (SiGe, vacuum); MMRTG **~4.8%/yr** (PbTe/TAGS, atmosphere); eMMRTG target **2.5%/yr** (skutterudite). Voyager 1's three MHW-RTGs produced 470 W at launch in 1977 and 219 W in 2024 — a 47-year dataset that exactly matches the predicted SiGe degradation model.

## Fabrication and Assembly

RTG assembly is a multi-year sequence conducted entirely inside shielded hot cells and cleanrooms. The major steps, in order:

1. **Fuel pellet pressing** — ²³⁸PuO₂ powder (produced via Np-237 irradiation and chemical separation; see [Isotope Production](./isotope-production.md)) is uniaxially pressed into cylindrical pellets at 200 MPa, then sintered at 1,600°C in argon to >95% theoretical density. Each pellet is 29.4 mm diameter × 29.4 mm tall, massing ~151 g.
2. **Iridium clad encapsulation** — Each pellet is loaded into a DOP-26 iridium capsule (0.64 mm wall), the capsule is evacuated, backfilled with helium (to provide a thermal-conduction path and to test for leaks), and welded shut with an electron-beam weld. Helium leak rate must be <1×10⁻⁸ atm·cc/s.
3. **GPHS module assembly** — Four clad capsules are loaded into a CBCF insulation blanket, inserted into a FWPF graphite aeroshell, and the frit vent is installed. The completed module is dimensionally inspected and mass-balanced.
4. **Stack assembly** — Modules are stacked axially (GPHS-RTG: 18 high; MMRTG: 8 high) with graphite spring preloads to maintain thermal contact during launch vibration.
5. **Thermocouple installation** — Pre-tested thermocouples are bonded to the hot shoe (against the aeroshell) and cold stack (against the radiator). The full ladder is wired into series-parallel strings; individual couples are bench-screened for shorts before installation.
6. **MLI wrapping and housing closure** — The stack is wrapped in 30 layers of MLI, the Al 2219-T6 housing is bolted over the assembly, and the radiator fins are attached.
7. **Final acceptance testing** — Thermal-vacuum testing at full power, vibration testing to launch loads, electromagnetic compatibility testing, and radiological survey for surface contamination. Total fabrication time: 3-5 years per generator.

## Bill of Materials (GPHS-RTG)

| Component | Material | Quantity | Mass per Unit (kg) |
|-----------|----------|----------|--------------------|
| Fuel pellet | ²³⁸PuO₂ ceramic | 72 (4 × 18 modules) | 0.151 |
| Fuel clad | DOP-26 iridium (0.64 mm wall) | 72 capsules | 0.083 |
| Aeroshell | FWPF carbon-carbon composite | 18 modules | 0.42 |
| Insulation | CBCF graphite fibre felt | 18 modules | 0.15 |
| Frit vent | Sintered iridium (0.5 μm pore) | 72 vents | 0.005 |
| Thermocouple legs | SiGe (n+ P-doped, p+ B-doped) | 572 unicouples (1,144 legs) | 0.005 |
| Hot shoe | Molybdenum | 572 | 0.008 |
| Cold stack | OFHC copper | 572 | 0.012 |
| Insulation wrap | Aluminised Kapton MLI (30 layers) | 1 assembly | 6.4 |
| Radiator fins | Aluminum 2219-T6 | 8 panels | 1.6 |
| Structural housing | Aluminum 2219-T6 | 1 cylinder | 0.2 (per panel) |

## Calibration and Verification

1. **Beginning-of-mission electrical performance** — Measure I-V curve at full thermal output; verify BOM power within ±2% of design (GPHS-RTG: 285-300 W_e; MMRTG: 110 W_e). Document as baseline for degradation tracking.
2. **Hot/cold junction temperatures** — Thermocouple embedded in hot shoe (target 1,000°C ± 15°C for GPHS-RTG; 538°C ± 10°C for MMRTG). Cold junction via radiator-mounted sensors (300°C / 210°C respectively). Deviation >20°C indicates a thermal-bond failure.
3. **Helium leak rate** — Mass-spectrometer sniff test on each clad capsule before stacking; maximum acceptable leak 1×10⁻⁸ atm·cc/s. Any capsule failing this test is re-welded or scrapped.
4. **Thermal-vacuum soak** — 30-day thermal-vacuum test at operating temperature; monitor for power-output drift <0.5% over the test duration. Higher drift indicates a bond failure or MLI compaction issue.
5. **Vibration qualification** — Sine and random vibration along three orthogonal axes, replicating launch vehicle environments (Titan IV, Atlas V, SLS). Post-vibe electrical inspection must show no couple shorts; resistance change <1%.
6. **Radiological survey** — Wipe survey of external surfaces; removable contamination must be <2,200 dpm/100 cm² alpha. Document as the shipping-baseline radiological condition.

## Troubleshooting

| Problem | Probable Cause | Mitigation |
|---------|---------------|------------|
| Output power below BOM spec at launch | Thermocouple bond failure; MLI compaction during vibe | Re-bond affected couples; replace compacted MLI layers; re-run thermal-vac |
| Hot/cold ΔT smaller than predicted | Parasitic heat path (MLI bridge, housing conduction); radiator surface emissivity degraded | Inspect MLI for bridges; clean radiator; verify emissivity coating |
| Individual couple short-circuited | Hot-shoe braze failure; SiGe leg cracked | Couple is isolated by series-parallel ladder design — output drops 1/572; no in-flight mitigation possible |
| Helium pressure rising inside clad | Frit vent blocked by contamination or PuO₂ migration | Pre-launch: rework clad. In-flight: none; clad will eventually rupture (decades) |
| MMRTG output dropping faster than 4.8%/yr | PbTe sublimation accelerated by atmosphere ingress; radiator dust accumulation | Periodic dust removal (Martian wind); design margin absorbs additional loss |
| Radiator fin temperature non-uniform | Cold-stack contact resistance; uneven fin coating | Map with IR camera during thermal-vac; re-bond cold stack if local hot spots > 30°C above mean |

## Commercial and Terrestrial RTGs

Until recently, all US RTGs were government-built for space missions. The 2020s have seen commercial entrants targeting terrestrial and maritime markets where maintenance-free multi-decade power is valuable.

**Zeno Power** is developing **strontium-90-fueled RTGs** under the US DOE's DEPTHS (Dynamic, Encrypted, Power for Theaters, Hostile, and Sensitive environments) programme. Sr-90 (28.8-yr half-life, 0.46 W/g, beta emission) is cheaper and more available than Pu-238 because it is extracted from spent nuclear fuel rather than produced by reactor irradiation of Np-237. Sr-90's penalty is heavy shielding (the betas produce bremsstrahlung X-rays in any high-Z material) and lower specific power.

Zeno's first commercial unit targets **maritime applications** — seafloor sensors, oceanographic buoys, and underwater vehicles — where battery replacement is impractical and solar is unavailable. A **2026 at-sea demonstration** is planned under the DEPTHS contract. The thermoelectric converter is PbTe/TAGS, the same material as the MMRTG, but the heat source is SrTiO₃ pellets in a welded Hastelloy capsule rather than PuO₂ in iridium. Specific power targets ~0.5-1.0 W_e/kg (much lower than space RTGs because shielding dominates mass). See [Isotope Production](./isotope-production.md) for the Sr-90 supply chain.

Soviet-era **Beta-M** RTGs (580 kg, 10 W_e, Sr-90) powered thousands of unattended lighthouses along the Russian arctic coast from the 1970s to the 2000s; many have since been dismantled for radiological security reasons. The historical lesson is that terrestrial RTGs are technically mature but politically and security-constrained.

## Strengths and Weaknesses of Thermoelectric Conversion

**Strengths**:
- No moving parts — failure rate set by radioactive decay physics, not mechanical wear. Voyager's RTGs are still operating after 47 years.
- Launch-survivable through explosion, re-entry, and impact via the GPHS module's multi-layer containment.
- Operates in vacuum, atmosphere, or underwater with only radiator redesign — same GPHS heat source serves all environments.
- Self-regulating thermally — a thermocouple's electrical resistance rises with temperature, providing passive power limiting.
- Decades of unattended operation between fuel loadings; no refueling, no maintenance.

**Weaknesses**:
- Low efficiency (5-8%) means 92-95% of decay heat must be radiated to space as waste. A 300 W_e GPHS-RTG dissipates 4,200 W_th.
- Pu-238 is scarce — global production is ~1.5 kg/yr (ORNL, resumed 2015); a single GPHS-RTG needs 10.8 kg, equivalent to ~7 years of total world output.
- Heavy — 5.1 W_e/kg is the best ever achieved; solar arrays at Mars achieve 5-10 W/kg and improve with each generation.
- Slow degradation is predictable but unavoidable; every mission's power budget must plan for end-of-mission power, not BOM.
- Thermoelectric material fabrication (SiGe, PbTe/TAGS, skutterudite) requires semiconductor-grade tellurium, antimony, and germanium — themselves late-tier supply-chain products.

## Bootstrap Sequence

In the bootstrapping-civilisation tech tree, thermoelectric RTGs appear only after all of the following are in place:

1. **Operating nuclear fission reactor** — needed for the neutron flux (10¹⁴ n/cm²·s) to irradiate Np-237 targets into Pu-238. See [Nuclear Fission Power](./nuclear-fission.md) and [Isotope Production](./isotope-production.md).
2. **Hot-cell fuel fabrication** — glovebox and hot-cell infrastructure for pressing PuO₂ pellets, welding iridium clad, and assembling GPHS modules. The radiation level at the surface of a bare Pu-238 pellet is ~200 mSv/h; all handling is by remote manipulator. See [Radiation Safety](../ehs/radiation-safety.md).
3. **Thermoelectric semiconductor manufacturing** — doped PbTe, TAGS, and SiGe require zone-refined tellurium, antimony, germanium, and silicon of semiconductor purity. See [Silicon](../silicon/index.md) and the thermoelectric-semiconductor sub-tree.
4. **Iridium and graphite fabrication** — DOP-26 iridium requires iridium sponge (a PGM byproduct of platinum mining), zone-refined and thermomechanically processed. FWPF carbon-carbon requires pitch-fibre weaving and CVI densification.
5. **Launch qualification and safety case** — every flight RTG passes a Launch Approval process (Interagency Nuclear Safety Review Panel) that models launch-explosion, re-entry, and ground-impact scenarios.

These five prerequisites place thermoelectric RTGs firmly in the "Years 30-100+" tier — the same tier as their parent capability [radioisotope power](./radioisotope-power.md) and their grandparent [nuclear fission](./nuclear-fission.md). No shortcut exists.

## See Also

- **[Radioisotope Power](./radioisotope-power.md)** — Parent capability: overview of all conversion methods
- **[Isotope Production](./isotope-production.md)** — Pu-238 and Sr-90 supply chain
- **[Nuclear Fission Power](./nuclear-fission.md)** — Grandparent capability; neutron flux for isotope irradiation
- **[Electricity Generation](./electricity.md)** — Power conditioning bus, shunt regulators, DC-DC converters
- **[Iron & Steel](../metals/iron-steel.md)** — Aluminum 2219-T6 housing, iridium clad, titanium insulation
- **[Radiation Safety](../ehs/radiation-safety.md)** — Hot-cell work, launch-accident safety case, ALARA
- **[Stirling Engine](./stirling-engine.md)** — Alternative dynamic conversion (ASRG, 28.6% efficiency)
- **`stirling-isotope-generator`** (sub-article, Wave 4) — ASRG architecture and helium retention
- **[Isotope Fuel Fabrication](./isotope-fuel-fabrication.md)** — Hot-cell GPHS module assembly
- **`advanced-isotope-conversion`** (sub-article, Wave 4) — TPV, betavoltaic, and segmented thermoelectric couples

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
