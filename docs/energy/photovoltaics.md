# Photovoltaic Solar Power

> **Node ID**: energy.photovoltaics
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`silicon.basic-devices`](../silicon/basic-devices.md), [`electronics.power-electronics`](../electronics/power-electronics.md), [`glass.basic`](../glass/basic.md)
> **Enables**: distributed power generation, grid-connected solar farms
> **Timeline**: Years 30-50
> **Outputs**: solar_modules, dc_electricity
> **Critical**: No — supplementary energy source that scales from watts to megawatts without fuel supply chain


Solar photovoltaics convert sunlight directly into electricity using semiconductor p-n junctions. Unlike every other power source in the bootstrap chain, photovoltaics require no fuel — no coal, no gas, no moving water or wind. Once manufactured, a solar panel produces electricity for 25-30 years with minimal maintenance. This makes photovoltaics uniquely attractive for bootstrapping: a factory that builds solar panels is, in effect, building its own future energy supply.

The trade-off is manufacturing complexity. Producing functional solar cells demands silicon purification, crystal growth, wafer slicing, doping, metallization, and encapsulation — capabilities that arrive decades into the bootstrap sequence. But once silicon device fabrication is established (see [Basic Semiconductor Devices](../silicon/basic-devices.md)), solar cells are among the simplest devices to produce, requiring far less precision than integrated circuits.


## P-N Junction Physics

The photovoltaic effect occurs when photons with energy above the semiconductor bandgap create electron-hole pairs near a p-n junction. The built-in electric field at the junction separates these carriers, driving electrons toward the n-type side and holes toward the p-type side. This produces a voltage (~0.5-0.7 V per cell for silicon) and, when connected to a load, a current proportional to the incident light intensity.

Key parameters:

- **Bandgap**: Crystalline silicon has a bandgap of 1.12 eV, absorbing photons with wavelengths below ~1,100 nm (near-infrared and visible light). This is near-optimal for the solar spectrum.
- **Open-circuit voltage (Voc)**: 0.5-0.7 V per cell, determined by the junction quality and bandgap.
- **Short-circuit current (Isc)**: 35-42 mA/cm² for commercial silicon cells, proportional to photon flux.
- **Fill factor (FF)**: 0.75-0.83, representing the "squareness" of the I-V curve. Higher fill factor means more usable power.
- **Efficiency**: The product η = (Voc × Isc × FF) / Pin, where Pin is incident solar power (~1,000 W/m² at standard conditions).

The theoretical maximum efficiency for a single-junction silicon cell (the Shockley-Queisser limit) is approximately 33%. Practical commercial cells achieve lower efficiencies due to reflection losses, incomplete absorption, carrier recombination, and resistive losses in contacts.


## Cell Manufacturing

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


## Efficiency by Technology

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
