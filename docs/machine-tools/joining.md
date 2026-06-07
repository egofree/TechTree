# Metal Joining

> **Node ID**: machine-tools.joining
> **Domain**: [Machine Tools Bootstrap](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`energy.electricity`](../energy/electricity.md), [`metals.alloys`](../metals/alloys.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`energy.steam-power`](../energy/steam-power.md), [`machine-tools.joining.diffusion-bonding`](./joining.md), [`machine-tools.joining.electron-beam`](./joining.md), [`machine-tools.joining.friction-stir`](./joining.md), [`machine-tools.joining.laser-welding`](./joining.md), [`machine-tools.joining.mig-welding`](./joining.md), [`machine-tools.joining.resistance-welding`](./joining.md), [`machine-tools.joining.tig-welding`](./joining.md), [`machine-tools.joining.ultrasonic-bonding`](./joining.md)
> **Timeline**: Years 5-70
> **Outputs**: forge_welds, brazed_joints, soldered_joints, riveted_joints, welded_joints, acetylene, tig_welds, mig_welds, resistance_welds, electron_beam_welds, ultrasonic_bonds, friction_stir_welds, laser_welds, diffusion_bonds, hermetic_seals, wire_bonds
> **Critical**: Yes — makes machinery possible by assembling individual parts into structures, mechanisms, and pressure vessels


Metal joining is the capability that makes machinery possible. Individual forged or cast parts are rarely useful alone — they must be assembled into structures, mechanisms, pressure vessels, and frames. Each method occupies a specific niche defined by temperature, joint strength, equipment requirements, and the materials it can join. No single method replaces all others — a complete industrial shop needs all three families.

For the metallurgy of producing iron and steel stock to be joined, see [Iron & Steel](../metals/iron-steel.md). For the electrical infrastructure needed by arc welding, see [Electricity](../energy/electricity.md).

## Articles in this Section

- **[Welding](./welding.md)** — Forge welding, oxy-acetylene welding, SMAW (stick), TIG (GTAW), MIG (GMAW), resistance spot/seam welding, electron beam welding, ultrasonic welding & wire bonding, friction stir welding, laser welding, and diffusion bonding. Covers vacuum chamber fabrication, hermetic sealing, and weld quality inspection.
- **[Brazing & Soldering](./brazing-soldering.md)** — Brass brazing (spelter brazing), silver brazing (hard soldering), and soft soldering. Filler alloy joining where the base metal does not melt. Brazing for structural joints; soldering for electrical connections, plumbing, and sheet metal seams.
- **[Riveting](./riveting.md)** — Hot and cold riveting, joint configurations (lap, butt with cover plates, boiler seams), rivet patterns, and inspection. Mechanical joining with no heat at the joint.

## Method Selection Overview

| Method | Temp Range | Joint Strength | Best For |
|--------|-----------|---------------|----------|
| Soft soldering | 180-250°C | 20-50 MPa | Electrical connections, plumbing, sheet metal seams |
| Silver brazing | 620-780°C | 150-300 MPa | Fine mechanisms, instruments, dissimilar metals |
| Brass brazing | 870-950°C | 150-250 MPa | Structural joints, cast iron, pipe fittings |
| Riveting | Cold or 900°C | 80-150 MPa (shear) | Structural steel, boilers, bridges, ship hulls |
| Forge welding | 1200-1300°C | 250-400 MPa | Iron/low-carbon steel bars, chains, composite billets |
| Oxy-acetylene | ~3100°C | 300-450 MPa | Sheet metal, repair, cutting, general fabrication |
| SMAW (stick) | ~6000°C (arc) | 350-480 MPa | Structural steel, heavy fabrication, pressure vessels |
| TIG (GTAW) | ~6000°C (arc) | 350-520 MPa | Stainless steel, aluminum, titanium, thin-wall tubing |
| MIG (GMAW) | ~6000°C (arc) | 350-500 MPa | High-deposition fabrication, sheet metal, automotive |
| Resistance (spot) | N/A | 200-400 MPa (shear) | Sheet metal lap joints, automotive, appliance panels |
| Electron beam | N/A | 350-550 MPa | Vacuum chambers, aerospace, refractory metals |
| Friction stir | N/A | 300-500 MPa | Aluminum alloys (2xxx, 7xxx), dissimilar metal joints |
| Laser | N/A | 350-520 MPa | High-speed welding, precision, automation |
| Diffusion bonding | 50-80% Tm | 80-100% parent | Dissimilar metals, UHV components, complex internals |

## Cross-References

- [Iron & Steel](../metals/iron-steel.md) — primary metals for welding
- [Specialty Alloys](../metals/alloys.md) — alloy weldability and filler metals
- [Electricity](../energy/electricity.md) — power for arc welding processes
- [Chemistry Index](../chemistry/index.md) — flux chemistry and shielding gases
- [Steam Power](../energy/steam-power.md) — boiler fabrication with welded joints
- [Metal Forming](../metals/forming.md) — shaping before joining
- [Machining](machining.md) — post-weld finishing and repair

---

*Part of the [Bootciv Tech Tree](../index.md) · [Machine Tools Bootstrap](./index.md) · [All Domains](../index.md)*