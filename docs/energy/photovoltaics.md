# Photovoltaic Solar Power

> **Node ID**: energy.photovoltaics
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`silicon.basic-devices`](../silicon/basic-devices.md), [`electronics.power-electronics`](../electronics/power-electronics.md), [`glass.basic`](../glass/basic.md)
> **Enables**: distributed power generation, grid-connected solar farms
> **Timeline**: Years 30-50
> **Outputs**: solar_modules, dc_electricity
> **Critical**: No — supplementary energy source that scales from watts to megawatts without fuel supply chain


Solar photovoltaics convert sunlight directly into electricity using semiconductor p-n junctions. Unlike every other power source in the bootstrap chain, photovoltaics require no fuel — no coal, no gas, no moving water or wind. Once manufactured, a solar panel produces electricity for 25-30 years with minimal maintenance. This makes photovoltaics uniquely attractive for bootstrapping: a factory that builds solar panels is, in effect, building its own future energy supply.

The trade-off is manufacturing complexity. Producing functional solar cells demands silicon purification, crystal growth, wafer slicing, doping, metallization, and encapsulation — capabilities that arrive decades into the bootstrap sequence. But once silicon device fabrication is established (see [Basic Semiconductor Devices](../silicon/basic-devices.md)), solar cells are among the simplest devices to produce, requiring far less precision than integrated circuits. Cross-reference: [Silicon Processing](../silicon/index.md) for the full silicon capability chain; [Power Electronics](../electronics/power-electronics.md) for inverters that convert DC panel output to usable AC power.

## Overview


## P-N Junction Physics

The photovoltaic effect occurs when photons with energy above the semiconductor bandgap create electron-hole pairs near a p-n junction. The built-in electric field at the junction separates these carriers, driving electrons toward the n-type side and holes toward the p-type side. This produces a voltage (~0.5-0.7 V per cell for silicon) and, when connected to a load, a current proportional to the incident light intensity.

Key parameters:

- **Bandgap**: Crystalline silicon has a bandgap of 1.12 eV, absorbing photons with wavelengths below ~1,100 nm (near-infrared and visible light). This is near-optimal for the solar spectrum.
- **Open-circuit voltage (Voc)**: 0.5-0.7 V per cell, determined by the junction quality and bandgap.
- **Short-circuit current (Isc)**: 35-42 mA/cm² for commercial silicon cells, proportional to photon flux.
- **Fill factor (FF)**: 0.75-0.83, representing the "squareness" of the I-V curve. Higher fill factor means more usable power.
- **Efficiency**: The product η = (Voc × Isc × FF) / Pin, where Pin is incident solar power (~1,000 W/m² at standard conditions).

The theoretical maximum efficiency for a single-junction silicon cell (the Shockley-Queisser limit) is approximately 33%. Practical commercial cells achieve lower efficiencies due to reflection losses, incomplete absorption, carrier recombination, and resistive losses in contacts.


## Prerequisites

- [Solar-grade silicon (6N purity)](../silicon/mg-si-production.md) — purified from metallurgical-grade silicon
- [Czochralski crystal puller](../silicon/cz-pulling.md) — for monocrystalline ingot growth, or casting furnace for polycrystalline
- [Diamond wire saw](../machine-tools/machining.md) — for wafer slicing (180-200 μm thick)
- [Diffusion furnace](../silicon/basic-devices.md) — quartz tube furnace, 900°C capability, gas handling for POCl₃
- [PECVD system](../silicon/basic-devices.md) — for SiNₓ anti-reflection coating deposition
- [Screen printer](../machine-tools/machining.md) — for front Ag and back Al paste metallization
- [Belt furnace](../ceramics/kilns.md) — 8-zone, peak 850°C, for paste firing
- [Solar simulator](../measurement/temperature-pressure.md) — xenon flash, Class AAA, for cell testing
- [Tempered low-iron glass](../glass/basic.md) — front cover sheets for module assembly
- [Clean room capability](../cleanrooms/index.md) — Class 1000 minimum for cell processing

## Process Description

### Cell Manufacturing

Solar cell production follows a sequence that parallels semiconductor manufacturing but with far less demanding feature sizes and purity requirements than integrated circuits. See [Basic Semiconductor Devices](../silicon/basic-devices.md) for the underlying silicon processing capabilities.

### Silicon Feedstock

Solar-grade silicon requires 99.9999% (6N) purity — substantially less than electronic-grade (11N), but far beyond metallurgical grade (98%). The Siemens process (trichlorosilane decomposition) or fluidized bed reactor methods purify silicon to solar grade. Emerging approaches use metallurgical upgrading (acid leaching, directional solidification) to reach 4-5N at lower cost, suitable for lower-efficiency cells.

### Wafer Production

**Monocrystalline wafers** are sliced from single-crystal ingots grown by the Czochralski process. The resulting wafers have uniform crystal structure, enabling the highest efficiencies (~22% commercial average). The Czochralski pull yields round ingots that are squared off, producing characteristic "pseudo-square" wafers with clipped corners.

**Polycrystalline wafers** are sliced from cast blocks of directionally solidified multicrystalline silicon. Grain boundaries between crystals act as recombination sites, reducing efficiency (~18% commercial average). The casting process is simpler, cheaper, and wastes less silicon than Czochralski growth.

### Cell Processing

For a standard aluminum back-surface-field (Al-BSF) cell — the simplest commercial architecture:

1. **Surface texturing** — Chemical etching (alkali for mono, acid for poly) creates pyramidal microstructures that trap light by reflecting bouncing photons back into the cell rather than out.
2. **Phosphorus diffusion** — A POCl₃ source at 800-900°C creates the n-type emitter on the p-type wafer, forming the p-n junction. Junction depth is 0.3-0.5 μm.
3. **Edge isolation** — Laser scribing or plasma etching removes the conductive phosphorus layer from wafer edges to prevent front-to-back short circuits.
4. **Anti-reflection coating** — Silicon nitride (SiNₓ) deposited by plasma-enhanced chemical vapor deposition (PECVD) reduces surface reflection from ~30% to ~3%. Layer thickness (~75 nm) is tuned for quarter-wave destructive interference.
5. **Metallization** — Screen-printed silver paste on the front (finger grid pattern to minimize shading while collecting current) and aluminum paste on the back. Fired at 700-800°C to form ohmic contacts.
6. **Testing and sorting** — Cells are flash-tested under simulated sunlight (1,000 W/m², 25°C, AM1.5 spectrum) and binned by current output for matched module assembly.

### Step 1: Surface Texturing Parameters

| Parameter | Monocrystalline (alkali) | Polycrystalline (acid) |
|-----------|--------------------------|----------------------|
| Etchant | 2-5% NaOH aqueous solution | HF (1-2%) + HNO₃ (15-20%) mixture |
| Temperature | 80-85°C | 20-30°C |
| Duration | 20-40 minutes | 1-3 minutes |
| Result | Inverted pyramids, 2-10 µm feature size | Hemispherical pits, 1-5 µm feature size |
| Reflection reduction | ~30% → ~10% | ~30% → ~12% |
| Rinse | DI water, 5 minutes | DI water, 5 minutes |
| Wafer loss | 5-10 µm per side | 3-8 µm per side |

### Step 2: Phosphorus Diffusion Parameters

| Parameter | Value |
|-----------|-------|
| Dopant source | POCl₃ liquid, bubbled by N₂ carrier gas at 0.5-2.0 L/min |
| Deposition temperature | 800-850°C |
| Drive-in temperature | 850-900°C |
| Total cycle time | 30-60 minutes in quartz tube furnace |
| N₂ carrier + O₂ (oxidizing ambient) | N₂ at 5-10 L/min + O₂ at 0.5-1.0 L/min |
| Junction depth (sheet resistance 40-80 Ω/sq) | 0.3-0.5 µm |
| PSG removal | Dip in 5-10% HF for 30-60 seconds after diffusion |

### Step 3: Edge Isolation Parameters

| Method | Parameters |
|--------|-----------|
| Plasma etching | CF₄/O₂ plasma, 100-200 W RF power, 30-120 seconds |
| Laser scribing | 532 nm or 1064 nm laser, 10-20 W, speed 100-500 mm/s, scribe groove 10-20 µm deep |

### Step 4: SiNₓ Anti-Reflection Coating

| Parameter | Value |
|-----------|-------|
| Deposition method | PECVD (plasma-enhanced chemical vapor deposition) |
| Precursor gases | SiH₄ (silane) at 20-50 sccm + NH₃ (ammonia) at 500-2000 sccm |
| RF power | 20-50 W at 13.56 MHz |
| Substrate temperature | 300-450°C |
| Chamber pressure | 0.5-1.0 Torr |
| Deposition rate | 10-30 nm/min |
| Target thickness | 75-80 nm (quarter-wave for 600 nm wavelength) |
| Refractive index | 2.0-2.1 |
| Reflection after coating | ~3% at 600 nm |

### Step 5: Metallization Parameters

| Parameter | Front contacts (Ag) | Back contact (Al) |
|-----------|---------------------|-------------------|
| Paste composition | Ag powder 70-85%, glass frit 2-5%, organic vehicle 10-25% | Al powder 70-80%, glass frit 1-3%, organic vehicle 15-25% |
| Screen mesh | 325-400 mesh, 15-20 µm wire diameter | 200-280 mesh |
| Finger width (printed) | 50-80 µm | N/A (full-area print) |
| Finger spacing | 1.5-2.5 mm | N/A |
| Busbar width | 1.0-1.5 mm, 3-5 busbars per cell | N/A |
| Drying | 150-200°C, 2-5 minutes | Same |
| Firing (co-firing) | Peak 750-820°C, 1-3 seconds above 700°C in belt furnace | Same |
| Belt speed | 4-6 m/min through 8-zone furnace | Same |

### Minimum Equipment for Cell Production Line

| Equipment | Specification | Purpose |
|-----------|--------------|---------|
| Wafer cleaning bench | Wet bench with DI water, ultrasonic, hotplate | Pre-texture cleaning, post-etch rinsing |
| Texturing bath | Heated tank with fume exhaust, temperature control ±2°C | Surface texturing |
| Quartz tube diffusion furnace | 3-5 tubes, 900°C max, N₂/O₂ gas supply | Phosphorus diffusion |
| HF wet bench | Fume hood, PP construction, emergency shower | PSG removal |
| PECVD system | 13.56 MHz RF, SiH₄/NH₃ gas handling, load-lock | SiNₓ deposition |
| Screen printer | Alignment ±25 µm, vacuum chuck | Front Ag and back Al paste application |
| Belt furnace | 8-zone, peak 850°C, belt speed 4-6 m/min, N₂ atmosphere | Paste firing / contact formation |
| Solar simulator | Xenon flash, Class AAA, 1000 W/m² AM1.5 | Cell testing and sorting |
| DI water system | 18 MΩ·cm, 5-10 L/min | Process water for all wet steps |


## Bill of Materials

### Per 1000 Cells (156 mm × 156 mm polycrystalline, ~18% efficiency)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Solar-grade silicon](../silicon/mg-si-production.md) | 80-120 kg | 6N purity (99.9999%), polysilicon chunks | [Silicon](../silicon/index.md) | MG-Si with upgraded metallurgical purification (4-5N, lower efficiency) |
| [Phosphorus oxychloride (POCl₃)](../chemistry/index.md) | 2-5 kg | Liquid dopant source, >99% purity | [Chemistry](../chemistry/index.md) | Phosphine gas (PH₃, more hazardous) |
| [Silane (SiH₄)](../chemistry/index.md) | 5-10 kg | Gas, pyrophoric, for PECVD SiNₓ | [Chemistry](../chemistry/index.md) | — |
| [Ammonia (NH₃)](../chemistry/ammonia.md) | 20-50 kg | Gas, for PECVD SiNₓ nitrogen source | [Ammonia](../chemistry/ammonia.md) | — |
| [Silver paste (front contacts)](../metals/precious-metals.md) | 5-10 kg | Ag powder 70-85%, glass frit, organic vehicle | [Precious Metals](../metals/precious-metals.md) | Copper plating (lower cost, developing technology) |
| [Aluminum paste (back contact)](../metals/aluminum.md) | 10-20 kg | Al powder 70-80%, glass frit, organic vehicle | [Aluminum](../metals/aluminum.md) | — |
| [Hydrofluoric acid (HF)](../chemistry/index.md) | 10-20 kg | 5-10% aqueous, for PSG removal | [Chemistry](../chemistry/index.md) | — |
| [Sodium hydroxide (NaOH)](../chemistry/index.md) | 10-30 kg | 2-5% aqueous, for surface texturing | [Chemistry](../chemistry/index.md) | KOH (potassium hydroxide) |
| [Tempered glass (front cover)](../glass/basic.md) | 250-350 m² | 3.2 mm, low-iron, >91% transmission | [Glass](../glass/basic.md) | Standard tempered glass (~88% transmission, 3-4% efficiency loss) |
| [EVA encapsulant film](../polymers/index.md) | 500-700 m² | 0.5 mm thick, cross-linkable | [Polymers](../polymers/index.md) | PVB (polyvinyl butyral) film |
| [Back sheet (Tedlar/PET)](../polymers/index.md) | 250-350 m² | Multi-layer, UV-resistant, moisture barrier | [Polymers](../polymers/index.md) | Tempered glass (bifacial design) |
| [Solder ribbon (interconnection)](../metals/copper-bronze.md) | 10-20 km | Tinned copper, 1.5-2.0 mm wide, 0.15-0.20 mm thick | [Copper](../metals/copper-bronze.md) | Conductive adhesive (lower reliability) |

## Quantitative Parameters

### Efficiency by Technology

| Technology | Commercial Efficiency | Lab Record | Notes |
|------------|----------------------|------------|-------|
| Monocrystalline PERC | ~22% | 26.8% | Highest commercial efficiency; passivated emitter rear contact reduces recombination |
| Polycrystalline Al-BSF | ~18% | 23.3% | Lower cost; grain boundaries limit carrier lifetime |
| Amorphous silicon (a-Si) | ~10% | 14.0% | Thin-film; flexible substrates; degrades ~15-20% in first months (Staebler-Wronski effect) |
| PERC+ (mono, bifacial) | ~23-24% | — | Rear side captures reflected ground light; gaining market share |

For bootstrap purposes, polycrystalline cells at ~18% efficiency represent the best balance of manufacturing simplicity and performance. Monocrystalline cells gain ~4 percentage points but require Czochralski pullers and higher silicon quality. Amorphous silicon's ~10% efficiency is attractive for thin-film deposition on cheap substrates but suffers long-term degradation.


## Module Assembly

Individual cells (~156 mm × 156 mm, producing ~8-10 W peak each at ~22% efficiency) are interconnected into strings of 60-72 cells using soldered or conductive-adhesive ribbon connections. The module laminator encapsulates this assembly in a moisture-proof sandwich:

| Layer (top to bottom) | Material | Function |
|----------------------|----------|----------|
| Front cover | Tempered low-iron glass (3.2 mm) | Mechanical protection, light transmission (~92%) |
| Encapsulant | Ethylene-vinyl acetate (EVA) film | Bonds layers, cushions thermal stress, blocks moisture |
| Cell matrix | Interconnected silicon cells | Active photovoltaic conversion |
| Encapsulant | EVA film | Rear encapsulation |
| Back sheet | Tedlar/PET/Tedlar or glass | UV protection, electrical insulation, moisture barrier |

Lamination occurs in a vacuum press at 140-160°C for 8-15 minutes, cross-linking the EVA into a clear, durable seal. The finished module is framed in aluminum extrusion, a junction box is attached to the rear, and cables with MC4-compatible connectors are fitted.

The glass front sheet is critical — see [Basic Glass Production](../glass/basic.md). Low-iron glass (reduced Fe₂O₃ content) transmits 91-92% of incident light versus ~88% for standard window glass. For bootstrap applications, standard tempered glass is acceptable with a ~3-4% relative efficiency penalty.

A 60-cell polycrystalline module produces approximately 270-285 W peak under standard test conditions. A 72-cell monocrystalline PERC module reaches 380-400 W peak.


## System Design

### Inverter Selection

Solar modules produce direct current (DC). Nearly all practical loads — motors, lighting, appliances — and grid interconnection require alternating current (AC). The inverter converts DC to AC, performing maximum power point tracking (MPPT) to continuously adjust the operating voltage for peak power output as irradiance and temperature change. See [Power Electronics](../electronics/power-electronics.md) for inverter technology.

Inverter types:

- **String inverter** — One inverter per string of 8-15 modules. Simple, low cost, but shading on any cell in the string reduces output of the entire string.
- **Microinverter** — One small inverter per module. Higher cost, but module-level MPPT eliminates string mismatch losses.
- **Central inverter** — Large (100 kW to multi-MW) inverters for utility-scale arrays. Most cost-effective per watt at scale.

### Mounting and Structures

- **Fixed-tilt ground mount** — Steel or aluminum racking at 15-35° tilt (latitude-dependent). Simplest and most common. Concrete foundations or driven piles.
- **Single-axis tracker** — Rotates the array east-to-west daily, boosting energy yield 15-25% over fixed tilt. Adds motors, controllers, bearings.
- **Rooftop mount** — Ballasted or structurally attached. Common for distributed generation.

For bootstrap contexts, fixed-tilt ground mount with manual seasonal angle adjustment (2-4 adjustments per year) captures most of the tracking benefit at zero complexity.

### Balance of System

- **DC wiring** — Weather-resistant cables (PV wire, 10-12 AWG) with MC4 connectors. String wiring combines modules in series (higher voltage) and parallel (higher current).
- **Combiner box** — Fuses or circuit breakers for each string; surge protection.
- **Disconnect switches** — Required for maintenance and emergency isolation on both DC and AC sides.
- **Metering** — Net metering or feed-in tariff measurement for grid-connected systems.
- **Monitoring** — Current/voltage sensors per string for fault detection.

### Sizing Example

A small workshop requiring 5 kW average power in a location with 5 peak-sun-hours/day:

- Daily energy need: 5 kW × 24 h = 120 kWh
- Accounting for system losses (inverter ~96%, wiring ~98%, soiling ~95%, temperature ~90%): derate factor ≈ 0.80
- Array size: 120 kWh / (5 h × 0.80) = 30 kW peak
- At ~18% efficiency, 30 kW requires ~170 m² of module area
- With 285 W modules: ~105 modules
- Inverter rating: ~30 kW (string or central)

A system at this scale can power machine tools, lighting, and small furnaces without any fuel supply chain.


## Performance Parameters

### Temperature Effects

Solar cell efficiency decreases with temperature — a critical factor since modules operate at 20-40°C above ambient in full sun. The temperature coefficient of power for crystalline silicon is typically -0.35% to -0.45% per °C above 25°C (standard test condition). A module at 65°C produces roughly 14-18% less power than rated.

### Degradation

- **Light-induced degradation (LID)**: Boron-oxygen complexes in p-type Czochralski silicon cause ~1-3% irreversible loss in the first days of exposure.
- **Potential-induced degradation (PID)**: Voltage stress between cells and grounded frame can cause ~10-20% reversible loss. Mitigated by module design and inverter grounding.
- **Annual degradation**: ~0.5-0.8% per year. A 30-year-old module still produces ~75-85% of its original output.

### Capacity Factor

The ratio of actual energy produced to theoretical maximum (nameplate × 8,760 hours). Typical capacity factors:

- Fixed-tilt, good solar resource: 16-22%
- Single-axis tracked, good resource: 20-28%
- Desert locations: up to 30%

Despite lower capacity factors than thermal plants, the zero-fuel cost makes photovoltaics economically compelling wherever the manufacturing base exists.


## Bootstrap Path

Photovoltaics enters the tech tree after silicon device fabrication is established. The path is:

1. **Establish silicon processing** — [Basic Semiconductor Devices](../silicon/basic-devices.md) provides wafer slicing, doping, and metallization
2. **Add cell-specific steps** — Surface texturing, SiNₓ anti-reflection coating, screen-printed contacts
3. **Module assembly** — Tempered glass from [Basic Glass Production](../glass/basic.md), EVA encapsulation, aluminum framing
4. **System integration** — [Power Electronics](../electronics/power-electronics.md) for inverters and charge controllers; [Construction](../construction/index.md) for mounting structures
5. **Scale up** — From kilowatts powering individual workshops to megawatt arrays driving industrial loads

The key advantage in a bootstrap context: once the first solar array is operational, it produces energy indefinitely without fuel, creating a positive feedback loop where energy enables more manufacturing, which enables more solar production.


## Scaling Notes

| Scale | Peak Power | Module Count | Array Area | Annual Energy (5 PSH) | Application |
|-------|-----------|--------------|------------|----------------------|-------------|
| Household | 3-5 kW | 10-18 | 18-30 m² | 4,400-7,300 kWh | Lighting, refrigeration, small appliances |
| Workshop | 15-30 kW | 50-105 | 85-170 m² | 22,000-44,000 kWh | Machine tools (1-3 simultaneous), lighting, welding |
| Small factory | 100-250 kW | 350-875 | 570-1,400 m² | 146,000-365,000 kWh | Multiple machine tools, furnaces, compressors |
| Industrial | 500 kW-1 MW | 1,750-3,500 | 2,850-5,700 m² | 730,000-1,460,000 kWh | Silicon purification, crystal growth, fabs |
| Utility scale | 5-100 MW | 17,500-350,000 | 28,500-570,000 m² | 7.3-146 GWh | Grid power, heavy industry |

Array area calculated at ~170 W/m² module efficiency (18% polycrystalline, including frame and spacing). Annual energy = peak power × peak sun hours × 365 × derate factor (0.80). In desert locations (7 PSH), annual energy is 40% higher.

Minimum economic scale for industrial bootstrap: 30 kW peak (105 modules, 170 m²), sufficient to power a workshop with machine tools and a small electric furnace. Below 5 kW, the manufacturing effort per watt of solar capacity is difficult to justify — use wind or water power instead.

Land area requirement: approximately 2.5-3.5× the module area for fixed-tilt ground-mount arrays (includes access aisles, inverter pads, and shading clearance). A 1 MW array requires approximately 1.5-2 hectares (3.5-5 acres).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Module output 15-25% below rated | High cell temperature (40°C above 25°C STC) | Normal — temperature coefficient causes -0.35 to -0.45%/°C loss. Improve ventilation behind modules; mount with 100+ mm air gap to allow convective cooling |
| String output significantly lower than expected | One or more shaded or damaged cells | Individual cell shading drops entire string output (bypass diodes limit loss to one-third of string). Identify shaded cells — trim vegetation, relocate obstruction, or reconfigure strings |
| Entire array offline (zero output) | Inverter fault or grid disconnection | Check inverter display for error codes; verify DC disconnect is closed; measure string voltage at combiner box |
| Hot spot on module (visible in IR) | Cracked cell or failed bypass diode causing reverse-bias heating | Replace the affected module — hot spots indicate cell damage that will worsen. Failed bypass diodes can be replaced in the junction box |
| Gradual output decline (>2%/year) | Soiling (dust, pollen, bird droppings) or degradation | Clean modules with water and soft brush — soiling losses of 5-25% are common in arid regions. If clean modules still show excessive decline, test individual strings for cell degradation |
| Inverter trips repeatedly | Ground fault in DC wiring | Check for insulation damage in cables, especially where wires pass through metal conduit. Megger test string wiring: minimum 40 MΩ to ground |
| Moisture inside module (fogged glass) | Delamination of EVA encapsulation | The module is failing — moisture ingress will corrode cell metallization. Replace the module. This failure is caused by manufacturing defects in lamination or physical damage to backsheet |

## Quality Control

- **Flash testing**: Each cell is tested under a solar simulator (1,000 W/m², 25°C, AM1.5 spectrum) before module assembly. Cells are sorted into matching current bins (±3%) for string assembly — mismatched cells waste power through resistive losses.
- **Module flash testing**: Each completed module is flash-tested to verify power output meets the rated specification (positive tolerance: actual output ≥ nameplate). Record Isc, Voc, Imp, Vmp, and Pmax. Modules must be within ±3% of nameplate power.
- **Electroluminescence imaging**: Apply forward bias to the module in a dark room; the cells emit infrared light proportional to their activity. A specialized IR camera reveals cracked cells, inactive areas, and shunting defects invisible to visual inspection. This test is performed at the factory; field testing requires portable EL equipment.
- **Insulation resistance**: Megger test between cell strings and grounded frame at 1,000V DC. Minimum: 40 MΩ per IEC 61730. Below 10 MΩ indicates moisture ingress or insulation damage — do not install.
- **Thermal imaging (field)**: Scan operating arrays with an IR camera annually. Hot cells (>20°C above neighbors) indicate degradation, cracks, or solder joint failures. Replace affected modules within 12 months to prevent fire risk.
- **Annual performance verification**: Compare actual annual energy production to predicted (peak kW × PSH × 365 × 0.80 derate). Actual within 90-110% of predicted is normal. Below 85% warrants investigation of soiling, shading, inverter faults, or module degradation.

## Safety

- **DC electrical hazard**: Solar arrays produce DC voltage at dangerous levels (300-1000V DC per string). Unlike AC, DC arcs do not self-extinguish at zero crossings — an arc fault can sustain indefinitely, causing fire. Install DC arc-fault circuit interrupters (AFCI) on strings. De-energize by covering modules with opaque material before working on wiring — modules produce voltage whenever illuminated.
- **Installation falls**: Rooftop and ground-mount array installation involves working at heights. Fall protection (harness, anchor point rated to 2,200 kg) is mandatory above 2 m. Wind loading on partially installed modules can be hazardous — secure modules immediately upon placement.
- **Lifting injuries**: A 60-cell module weighs 18-25 kg. Handling modules on rooftops in hot weather causes fatigue injuries. Use two-person lifts for all module handling. A dropped module shatters into hazardous glass fragments.
- **Fire risk**: DC arc faults in module wiring or junction boxes can ignite rooftop materials. Maintain clearance between array and combustible roofing. Install rapid-shutdown devices that reduce module voltage to safe levels within 30 seconds of emergency shutdown activation.
- **Chemical (manufacturing)**: Solar cell manufacturing uses hydrofluoric acid (HF) for surface etching, POCl₃ for phosphorus diffusion, and silane (SiH₄) gas for SiNₓ deposition. HF causes deep tissue burns with delayed symptoms — calcium gluconate gel must be available at every HF workstation. Silane is pyrophoric — it ignites spontaneously in air. See [Chemistry](../chemistry/index.md) for chemical handling procedures.

## Variations and Alternatives

### Thin-Film Solar Cells

Deposited as thin films (1-10 μm) on cheap substrates (glass, stainless steel, flexible plastic). Use far less semiconductor material than crystalline silicon wafers (180-200 μm thick). Three commercial types:

| Technology | Efficiency | Substrate | Advantages | Limitations |
|------------|-----------|-----------|------------|-------------|
| CdTe (cadmium telluride) | 18-22% | Glass | Lowest cost per watt of any PV technology; simple manufacturing (vapor deposition) | Cadmium is toxic; tellurium is scarce |
| CIGS (copper indium gallium selenide) | 14-20% | Glass or flexible | Flexible modules possible; good low-light performance | Indium and gallium are scarce; complex deposition |
| a-Si (amorphous silicon) | 8-12% | Glass or flexible | Simple manufacturing; no toxic materials; good in diffuse light | Staebler-Wronski degradation (~15% loss in first 6 months); low efficiency |

For bootstrap contexts, thin-film manufacturing may be accessible before crystalline silicon wafer processing because it avoids wafer slicing — but the lower efficiency means 2-3× more array area for the same power.

### Concentrated Photovoltaics (CPV)

Lenses or mirrors concentrate sunlight 500-1000× onto small, high-efficiency multi-junction cells (III-V semiconductors, ~40% efficiency). Requires two-axis sun tracking and only works with direct normal irradiance (no diffuse light). Highest efficiency but highest complexity. Not practical for bootstrap — the multi-junction cells require III-V semiconductor epitaxy (gallium arsenide, indium phosphide) that is more complex than silicon processing.

### Emerging: Perovskite Solar Cells

Lead-halide perovskite (CH₃NH₃PbI₃) cells have reached >25% lab efficiency with simple solution processing. Potential for very low-cost manufacturing. Current limitations: lead toxicity, moisture sensitivity (modules degrade without perfect encapsulation), and uncertain long-term stability (<5 years demonstrated vs. 25+ years for silicon). Not yet ready for bootstrap applications but a technology to watch if stability issues are resolved.

## References

- [Basic Semiconductor Devices](../silicon/basic-devices.md) — silicon processing, wafer production, doping, and metallization
- [Basic Glass Production](../glass/basic.md) — tempered low-iron glass for front cover sheets
- [Power Electronics](../electronics/power-electronics.md) — inverters, charge controllers, and MPPT tracking
- [Construction](../construction/index.md) — mounting structures, foundations, and wiring
- [Electricity Generation](electricity.md) — grid integration and power distribution
- [Fuels](fuels.md) — comparative energy sources and cost analysis

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
