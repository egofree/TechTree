# Air Separation & Bulk Gas Production

> **Node ID**: chemistry.air-separation
> **Domain**: Chemistry
> **Timeline**: Years 20-40
> **Outputs**: argon, nitrogen, oxygen

### Air Separation — Bulk Inert Gas Production

**Linde fractional distillation of liquid air**:
- **Principle**: Air is 78% N₂ (bp -196°C), 21% O₂ (bp -183°C), 0.93% Ar (bp -186°C). Cool air until it liquefies, then fractionally distill at cryogenic temperatures.
- **Air preparation**: Compress atmospheric air to 5-6 MPa. Remove water (desiccant beds — silica gel or activated alumina) and CO₂ (molecular sieve or NaOH scrubber — CO₂ would freeze and plug equipment at cryogenic temperatures). Filter particulates.
- **Cooling**: Compressed, cleaned air enters counter-current heat exchanger — cooled by outgoing cold nitrogen and oxygen product streams. Further cooled by expansion through throttle valve (Joule-Thomson effect: real gas cools when expanding at temperatures below its inversion temperature) or expansion engine (adiabatic expansion does work → larger temperature drop).
- **Distillation column**: Double-column design. Lower column at ~0.5 MPa (bp of N₂ at this pressure ~ -177°C). Upper column at ~0.1 MPa. Air enters between columns. N₂ (lower boiling point) rises as vapor, O₂ (higher boiling point) descends as liquid. Argon accumulates at an intermediate point — draw sidestream to separate argon column.
- **Products**:
  - **Nitrogen** (99-99.99%): Used as inert blanket gas, carrier gas, purge gas. Store as compressed gas or liquid N₂ in vacuum-insulated dewar (Dewar flask — double-walled vessel, vacuum between walls, silvered inner wall for radiation shielding. Evaporation rate: 0.5-2% per day).
  - **Oxygen** (95-99.5%): For steelmaking, welding, medical use, oxidation processes.
  - **Argon** (99-99.999%): Critical for CZ crystal growth (inert atmosphere prevents silicon oxidation and reactions with crucible). Also for welding shielding gas, sputtering.

### Plant Equipment Design

**Compressor**:
- **Type**: Multi-stage reciprocating (piston) compressor. 3-5 stages with intercoolers between each stage (cool compressed air back to near-ambient — reduces work of next stage and prevents overheating).
- **Pressure**: 5-20 bar (0.5-2 MPa) for Linde process. Higher pressure means more Joule-Thomson cooling but more compressor work.
- **Construction**: Cast iron or steel cylinders, steel pistons with piston rings, poppet or ring valves. Lubricated with mineral oil (must not contaminate process air — oil mist carries into downstream equipment). Later: oil-free compressors with PTFE piston rings for cleaner product.
- **Power**: Major electricity consumer — 0.3-0.5 kWh per Nm³ of air processed.

**Heat exchanger**:
- **Type**: Counter-current (countercurrent) shell-and-tube or plate-fin. Cold product gas streams (N₂, O₂) flow opposite to incoming warm compressed air. Temperature approach: 2-5°C at cold end.
- **Construction**: Copper or stainless steel tubing for good thermal conductivity at cryogenic temperatures. Insulated enclosure packed with perlite or mineral wool under slight positive nitrogen purge (prevents moisture ingress and ice formation). Welded joints — no threaded fittings at cryogenic temperatures (leak risk from thermal contraction).

**Construction sequence**: Compressor → aftercooler (initial air cooling) → molecular sieve traps (remove H₂O, CO₂) → main heat exchanger (cool to near-liquefaction) → expansion valve or turbine (final cooling to liquid) → lower distillation column → upper distillation column → product storage (compressed gas cylinders or vacuum-insulated dewars).

### Safety

- **Cryogenic burns**: LOX (−183°C) and LN₂ (−196°C) cause severe frostbite on skin contact. Insulated gloves, face shield, long sleeves mandatory. Never touch uninsulated cryogenic piping.
- **Oxygen-enriched fire hazard**: Materials burn vigorously in >25% O₂ atmospheres. Clothing saturated with LOX becomes explosive. Oil or grease on LOX-wetted surfaces can auto-ignite. Designate oxygen-safe zones — no petroleum products, no organic flooring.
- **Nitrogen asphyxiation**: LN₂ evaporates to 700× volume of gas. In confined spaces, N₂ displaces O₂ rapidly. Unconsciousness within seconds at <10% O₂, death within minutes. Continuous O₂ monitoring in all ASU enclosed areas. Ventilate before entry.

