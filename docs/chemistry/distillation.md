# Distillation

> **Node ID**: chemistry.distillation
> **Domain**: [Chemistry](./)
> **Dependencies**: `ceramics.kilns`, `mining`
> **Enables**: `silicon.purification`
> **Timeline**: Years 20-35
> **Outputs**: distillation_capability, fractionated_chemicals

### Infrastructure

**Distillation columns**:
- **Construction**: Copper or steel shell, 2-10 m tall, 20-100 cm diameter. Internal plates or packing (ceramic Raschig rings, ceramic saddles, or structured packing). Reboiler (heated kettle at bottom), condenser (cooled coil at top — water-cooled copper coil).
- **Operation**: Feed mixture enters at middle height. Reboiler vaporizes components. Vapor rises through packing/plates, contacting descending liquid (reflux). More volatile components concentrate at top, less volatile at bottom. Temperature gradient along column indicates separation.
- **Fractional distillation** for petroleum (see [Petrochemicals](../chemistry/petroleum-alternatives.md)): Multiple fractions drawn at different heights corresponding to different boiling ranges.

**Column design fundamentals**:
- **Minimum reflux ratio**: The lowest reflux ratio (L/D, liquid returned to column ÷ distillate drawn off) that achieves the desired separation. Operating below this makes separation impossible regardless of column height. Typically operate at 1.2-1.5× minimum reflux.
- **Theoretical plates**: Each ideal equilibrium stage (one vapor-liquid contact achieving thermodynamic equilibrium). More plates = sharper separation. Estimate via McCabe-Thiele method: plot equilibrium curve (vapor composition vs. liquid composition at boiling), draw operating lines for rectifying and stripping sections, step off plates between curve and 45° line. Number of steps = number of theoretical plates.
- **HETP** (Height Equivalent to a Theoretical Plate): For packed columns, the packing height needed for one theoretical plate. Raschig rings: 0.3-0.6 m HETP. Structured packing: 0.1-0.3 m HETP. Multiply HETP by required plates for total column packing height.

**Column construction procedure**:
1. **Shell fabrication**: Roll steel or copper plate to cylindrical shape (2-10 m tall, 20-100 cm diameter). Weld or rivet longitudinal seam. Attach flanged top and bottom caps with bolted gasketed joints (asbestos or compressed fiber gaskets).
2. **Internal fittings**: Weld support rings inside shell every 0.5-1 m to hold packing or plates. Install feed nozzle at calculated feed-tray height. Install thermowells (temperature probe ports) at top, middle, and bottom.
3. **Packing installation**: Pour ceramic Raschig rings (25-50 mm diameter × length) or saddles into shell, filling between support rings. Avoid bridging or voids — pack uniformly. Alternatively, install structured packing sections (corrugated ceramic or metal sheets) stacked on support rings.
4. **Reboiler**: Weld or bolt a heated kettle (steel shell, internal steam coil or external fire-heated jacket) to column bottom. Size reboiler to provide 1.2-1.5× minimum boilup rate. Include drain valve and sight glass.
5. **Condenser**: Install water-cooled copper coil or shell-and-tube condenser at column top. Connect cooling water supply and return. Include distillate collection vessel with reflux splitter (valve or adjustable weir to control reflux ratio).
6. **Leak testing**: Pressurize assembled column with air to 0.3-0.5 bar gauge. Soap-test all joints, flanges, and welds. Pressure hold test: 30-minute hold with <5% pressure drop. Fix all leaks before introducing process chemicals.
7. **Insulation**: Wrap column shell with mineral wool or asbestos rope (50-100 mm thick) and secure with sheet metal cladding. Proper insulation reduces heat loss, stabilizes temperature gradient, and prevents burns from contact.

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

### Safety & Hazards

- **Hot and boiling liquids**: Reboiler contents at 80-350°C cause severe thermal burns on skin contact. Condenser outlets, sample ports, and drain valves are primary contact hazards. Use thermal gloves and face shields when sampling or adjusting valves. Install splash guards on all sample points. Emergency shower within 10 meters of operating column.
- **Flammable vapor explosion risk**: Hydrocarbon and organic solvent vapors (petroleum fractions, alcohols, ethers) form explosive mixtures with air at concentrations of 1-10% by volume. A single ignition source (static discharge, hot surface, open flame) can cause catastrophic deflagration. Bond and ground all metal vessels and piping to prevent static buildup. Vent column area to atmosphere (no enclosed spaces). Use explosion-proof electrical equipment. Never operate flammable distillations near open flames or hot work.
- **Toxic chemical exposure**: Chlorosilanes (SiHCl₃, SiCl₄) release HCl on contact with moisture — corrosive to lungs, eyes, and skin. Benzene and aromatic fractions are carcinogenic. H₂SO₄ and other strong acids cause chemical burns. Use local exhaust ventilation at feed and product ports. Respiratory protection (cartridge respirator or supplied air) required for toxic distillates. Emergency eyewash station adjacent to column.
- **Pressure vessel safety**: Columns operating above atmospheric pressure (vacuum distillation or pressurized systems) store significant mechanical energy. Overpressure can rupture the shell. Install pressure relief valve on reboiler set to 1.1× maximum allowable working pressure. Vacuum columns must handle external atmospheric pressure — collapse risk if wall thickness is insufficient (minimum 3-5 mm steel for columns <1 m diameter). Hydrostatically test all pressure vessels at 1.5× design pressure before first use. Never exceed rated pressure.

### Cement & Concrete

Distillation supports cement and concrete production in several ways:
- **Kiln fuel processing**: Rotary cement kilns require 3-5 kg fuel per kg cement. Petroleum distillation produces the heavy fuel oil or coal tar fractions used as kiln fuel, and fractional distillation separates the light fractions for other industrial uses.
- **Chemical feedstock isolation**: Gypsum (CaSO₄·2H₂O), essential for controlling cement set time, may require evaporation and crystallization steps related to distillation technology. Sulfuric acid production (contact process) uses distillation-type absorption towers and involves fractionation of sulfur compounds.
- **Solvent recovery**: Concrete admixture manufacturing and curing compound production use organic solvents that are recovered and recycled via distillation.
- For full cement/concrete production details (clinker formation, hydration chemistry, reinforced concrete, alternative cements), see [Cement & Concrete](./cement.md).

### Polymer Feedstock Production

- The Chemistry stage's chemical industry enables production of key polymer feedstocks: phenol, formaldehyde, ethylene, propylene, styrene.
- See [Petrochemicals](../chemistry/petroleum-alternatives.md) for feedstock production and [Polymers](../polymers/index.md) for polymerization.
- This bridges inorganic chemistry to the organic polymer industry.
---

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
