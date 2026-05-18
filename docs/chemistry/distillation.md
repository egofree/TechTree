# Distillation

> **Node ID**: `chemistry.distillation`
> **Also covers**: `chemistry.cement`
> **Domain**: [Chemistry](./)
> **Dependencies**: `foundations.kilns-pottery`, `mining`
> **Enables**: `silicon.purification`
> **Timeline**: Years 20-35
> **Outputs**: distillation_capability, cement, concrete, reinforced_concrete

### Infrastructure

**Distillation columns**:
- **Construction**: Copper or steel shell, 2-10 m tall, 20-100 cm diameter. Internal plates or packing (ceramic Raschig rings, ceramic saddles, or structured packing). Reboiler (heated kettle at bottom), condenser (cooled coil at top — water-cooled copper coil).
- **Operation**: Feed mixture enters at middle height. Reboiler vaporizes components. Vapor rises through packing/plates, contacting descending liquid (reflux). More volatile components concentrate at top, less volatile at bottom. Temperature gradient along column indicates separation.
- **Fractional distillation** for petroleum (see [Petrochemicals](../chemistry/petroleum-alternatives.md)): Multiple fractions drawn at different heights corresponding to different boiling ranges.

**Column design fundamentals**:
- **Minimum reflux ratio**: The lowest reflux ratio (L/D, liquid returned to column ÷ distillate drawn off) that achieves the desired separation. Operating below this makes separation impossible regardless of column height. Typically operate at 1.2-1.5× minimum reflux.
- **Theoretical plates**: Each ideal equilibrium stage (one vapor-liquid contact achieving thermodynamic equilibrium). More plates = sharper separation. Estimate via McCabe-Thiele method: plot equilibrium curve (vapor composition vs. liquid composition at boiling), draw operating lines for rectifying and stripping sections, step off plates between curve and 45° line. Number of steps = number of theoretical plates.
- **HETP** (Height Equivalent to a Theoretical Plate): For packed columns, the packing height needed for one theoretical plate. Raschig rings: 0.3-0.6 m HETP. Structured packing: 0.1-0.3 m HETP. Multiply HETP by required plates for total column packing height.

**Specific distillation setups**:
- **Simple pot still**: Heated vessel + condenser. Batch operation. 1 theoretical plate (single vaporization-condensation). Sufficient for rough separations (water from salt, alcohol concentration to ~40-50%).
- **Fractional column**: Packed column (Raschig rings or structured packing) between boiler and condenser. 5-50 theoretical plates depending on height and packing. Batch or continuous. Used for petroleum fractions, alcohol purification, chlorosilane separation (see [Hydrogen & Silane](hydrogen-silane.md)).
- **Continuous distillation**: Feed enters at a middle tray (feed tray). Above: rectifying section (enriches light component). Below: stripping section (removes light component from bottoms). Reflux ratio controls product purity vs. energy consumption. Industrial standard for large-scale chemical and petroleum processing.

**Reactors**:
- **Batch reactors**: Jacketed steel or glass-lined vessels, 100-5000 liters. Heating/cooling via jacket (steam for heating, water for cooling). Agitator (motor-driven paddle or propeller). Charge reactants, react, discharge products.
- **Continuous flow reactors**: Tube or pipe reactors for large-scale continuous production. Better temperature control, higher throughput.
- **Materials**: Glass-lined steel (good for acids), lead-lined (for H₂SO₄), nickel or Monel (for HF), copper (for organic reactions), stainless steel (later, for many applications).

**Heat exchangers**:
- **Shell and tube**: Tube bundle inside cylindrical shell. One fluid inside tubes, other in shell. Countercurrent flow maximizes heat transfer. Copper tubes for good thermal conductivity. Steel shell.
- **Sizing**: Heat transfer area 1-50 m² depending on duty. Temperature approach (minimum ΔT between fluids) typically 5-20°C.

### Cement & Concrete

- **Portland cement**: Limestone + clay heated in kilns (~1450°C) → clinker (gray nodules 1-30 mm) → ground with gypsum (CaSO₄·2H₂O, 3-5%) in ball mill → cement powder. Kiln: rotating steel tube 30-60 m long, 2-4 m diameter, lined with refractory brick. Fuel: coal, gas, or oil. 3-5 kg fuel per kg cement.
- **Hydration**: Cement + water → calcium silicate hydrate gel (the binding matrix). Heat of hydration raises temperature significantly (important for mass concrete pours). Mix ratio: ~25-35% water by weight of cement.
- **Concrete**: Cement + sand + gravel + water. Typical mix 1:2:4 (cement:sand:gravel by volume) for structural concrete. Compressive strength 20-40 MPa at 28 days. Cure: keep moist for 7+ days (critical — early drying weakens concrete dramatically).
- **Reinforced concrete**: Steel rebar embedded in concrete. Steel handles tension, concrete handles compression. The dominant modern building material once you have both steel and cement.
- **Uses**: Factory foundations, dam construction (hydroelectric — Energy Storage), vibration isolation pads for precision equipment (Machine Tools, Silicon stages), road surfaces (Transport), chemical plant flooring.

### Polymer Feedstock Production

- The Chemistry stage's chemical industry enables production of key polymer feedstocks: phenol, formaldehyde, ethylene, propylene, styrene.
- See [Petrochemicals](../chemistry/petroleum-alternatives.md) for feedstock production and [Polymers](../polymers/overview.md) for polymerization.
- This bridges inorganic chemistry to the organic polymer industry.
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
