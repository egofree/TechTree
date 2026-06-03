# CVD Reactor

> **Node ID**: photolithography.cvd-reactor
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Dependencies**: [`vacuum.chambers`](../vacuum/chambers.md), [`gas-handling`](../gas-handling/index.md), [`energy.electricity`](../energy/electricity.md), [`measurement`](../measurement/index.md)
> **Enables**: [`photolithography.fab-processes`](fab-processes.md), [`silicon.basic-devices`](../silicon/basic-devices.md)
> **Timeline**: Years 35-50
> **Outputs**: cvd_films, deposited_oxides, deposited_nitrides, polysilicon_films
> **Critical**: Yes — CVD is the primary method for depositing gate oxides, interlayer dielectrics, and passivation layers in semiconductor fabrication

This article covers the construction of chemical vapor deposition (CVD) reactor systems. For CVD process chemistry, film properties, and deposition parameters, see [Deposition Systems](../vacuum/deposition-systems.md).

## Principle

Chemical vapor deposition (CVD) produces thin solid films on substrate surfaces by thermally driven or plasma-driven chemical reactions of gas-phase precursors. The reactor provides a controlled environment where process gases flow over heated substrates, decompose at the surface, and deposit the desired film material while volatile byproducts are carried away by the gas flow.

Two reactor configurations are addressed:

**LPCVD hot-wall tube reactor**: A horizontal or vertical quartz tube heated by a multi-zone resistance furnace. Wafers stand vertically in a slotted quartz boat at low pressure (0.1–1 Torr). The hot walls mean film deposits everywhere — on wafers and tube walls alike — but temperature uniformity is excellent (±1°C across the hot zone). Used for poly-Si, Si₃N₄, and SiO₂ films.

**PECVD parallel-plate reactor**: A vacuum chamber with two parallel electrodes — a showerhead gas distributor and a heated substrate platen. RF power (13.56 MHz) generates a plasma between the plates, enabling deposition at lower temperatures (200–400°C). Used for SiNₓ passivation, SiO₂ interlayer dielectrics, and amorphous silicon.

## Prerequisites

- [Vacuum chamber](../vacuum/vacuum-chamber.md) — stainless steel chamber for PECVD
- [Vacuum pump](../vacuum/vacuum-pump.md) — roughing pump for LPCVD; turbomolecular pump for PECVD
- [Gas handling](../gas-handling/index.md) — mass flow controllers, gas manifold, pneumatic valves
- [Resistance furnace](../energy/electric-furnaces.md) — 3-5 zone furnace for LPCVD tube
- [Fused silica production](../glass/index.md) — quartz tube for LPCVD reactor
- [RF power supply](../energy/electricity.md) — 13.56 MHz generator for PECVD

## Materials

### LPCVD Hot-Wall Tube Reactor

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Fused silica tube | 1 | 150-300 mm ID, 1200-2400 mm length, 3-5 mm wall | [Glass](../glass/index.md) | — |
| Resistance furnace (3-5 zone) | 1 | 600-1200 mm hot zone, ±1°C uniformity, max 1200°C | [Electric Furnaces](../energy/electric-furnaces.md) | — |
| Quartz boat and paddle | 1 set | Slotted boat for 50-200 wafers, 3-10 mm spacing | [Glass](../glass/index.md) | — |
| Stainless steel end caps | 2 | With O-ring seals, gas inlet/outlet ports | [Iron & Steel](../metals/iron-steel.md) | — |
| Rotary vane or scroll pump | 1 | 50-300 L/min, for 0.1-1 Torr operating pressure | [Vacuum Pump](../vacuum/vacuum-pump.md) | — |
| Mass flow controllers | 3-6 | 0-500 sccm range, for SiH₄, NH₃, N₂O, N₂, etc. | [Gas Handling](../gas-handling/index.md) | Needle valves + rotameter (less precise) |
| Capacitance manometer | 1 | 0-10 Torr range, ±0.5% accuracy | [Measurement](../measurement/index.md) | — |
| Throttle valve | 1 | Controlled conductance for pressure regulation | [Gas Handling](../gas-handling/index.md) | — |
| Thermocouples (Type K or S) | 3-5 | One per furnace zone | [Measurement](../measurement/index.md) | — |

### PECVD Parallel-Plate Reactor

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Stainless steel chamber | 1 | 300-500 mm diameter, CF-flanged | [Vacuum Chamber](../vacuum/vacuum-chamber.md) | Aluminum (lighter, He permeation) |
| Aluminum showerhead electrode | 1 | Perforated plate, hundreds of 1-2 mm holes | [Metals](../metals/index.md) | Anodized aluminum (corrosion resistance) |
| Heated substrate platen | 1 | Resistive or lamp-heated, 200-400°C, ±5°C uniformity | [Energy](../energy/energy.md) | — |
| Turbomolecular pump | 1 | 300-2000 L/s, backed by scroll pump | [Vacuum Pumps](../vacuum/pumps.md) | Diffusion pump (oil contamination risk) |
| RF generator (13.56 MHz) | 1 | 300-3000 W, with automatic matching network | [Energy](../energy/electricity.md) | — |
| Mass flow controllers | 3-6 | For SiH₄, NH₃, N₂, N₂O, etc. | [Gas Handling](../gas-handling/index.md) | — |
| Capacitance manometer | 1 | 0-10 Torr range | [Measurement](../measurement/index.md) | — |
| Load lock chamber | 1 | 5-20 L, with gate valve to main chamber | [Vacuum Chamber](../vacuum/vacuum-chamber.md) | — |

## Construction Steps

### LPCVD Hot-Wall Tube Reactor

1. **Install the furnace**: Mount the 3- or 5-zone resistance furnace on a horizontal frame. Align the furnace bore horizontally (use a level, ±0.5 mm/m). Install Type K thermocouples in each zone, positioned at the furnace wall near the tube surface. Connect each zone to a PID temperature controller.

2. **Insert the quartz tube**: Slide the fused silica tube through the furnace bore. Center it axially so the hot zone (uniform temperature region) is in the middle 600-1200 mm. Support the tube at both ends on V-blocks or rollers — do not clamp rigidly (quartz expands ~0.5×10⁻⁶/K and needs freedom to shift).

3. **Install end cap assemblies**: Fit stainless steel end caps to each end of the quartz tube. Each end cap has: an O-ring seal (Viton, compression-fit against the quartz tube OD), a gas inlet port (source end) or outlet port (exhaust end), and a thermocouple feedthrough. The inlet end cap connects to the gas manifold; the outlet connects to the throttle valve and roughing pump.

4. **Build the gas manifold**: Connect mass flow controllers (MFCs) to a gas distribution manifold on the inlet side. Use electropolished 316L stainless steel tubing (6-10 mm OD) with Swagelok or VCR fittings. Each MFC controls one process gas (SiH₄, NH₃, N₂O, TEOS bubbler carrier N₂, dilution N₂). Install pneumatic shut-off valves upstream of each MFC for safety.

5. **Install the vacuum and pressure control system**: Connect the throttle valve to the outlet end cap, then to the roughing pump. Install a capacitance manometer at the tube midpoint (via a port in the end cap) for pressure measurement. The throttle valve controller uses the manometer reading to maintain constant process pressure (±1% of setpoint).

6. **Fabricate the wafer boat and cantilever loader**: Fabricate a slotted quartz boat from fused silica rod and sheet. Slot spacing: 3-10 mm (determined by gas diffusion requirements). Mount the boat on a quartz paddle. The paddle attaches to a cantilever loader (stainless steel rod with magnetic feedthrough) that pushes the boat into the furnace at <5 cm/min (to avoid thermal shock to the quartz).

7. **Leak test and qualify**: Evacuate the tube to 10⁻³ Torr. Helium leak check all end cap seals, gas connections, and pump lines. Target: <10⁻⁶ atm·cc/s. Perform a blank run (no wafers, N₂ flow at process pressure) to verify temperature uniformity (±1°C across the hot zone) and pressure stability (±1% of setpoint).

### PECVD Parallel-Plate Reactor

1. **Prepare the vacuum chamber**: Construct or procure a stainless steel vacuum chamber (300-500 mm diameter, 250-350 mm tall) per [Vacuum Chamber](../vacuum/vacuum-chamber.md). Install CF flanges for: turbomolecular pump (bottom), showerhead electrode (top), gas inlet, viewport, pressure gauge, and RGA port.

2. **Machine the showerhead electrode**: Machine a flat aluminum plate (250-400 mm diameter, 10-15 mm thick) with hundreds of through-holes (1-2 mm diameter) distributed in a pattern that provides uniform gas flow across the wafer. The hole pattern is typically concentric rings with decreasing hole density toward the center (to compensate for gas depletion at the edges). Anodize or coat with Y₂O₃ for corrosion resistance against plasma species. Mount the showerhead on a CF flange with a ceramic (alumina) insulator providing electrical isolation from the chamber.

3. **Build the heated substrate platen**: Machine an aluminum or stainless steel plate (200-300 mm diameter) with embedded cartridge heaters (resistive heating elements, 500-2000 W total). Install a thermocouple in the plate surface for temperature feedback. The platen is the lower electrode (grounded) and is mounted on a lift mechanism for wafer loading. Temperature uniformity: ±5°C across 200 mm wafer.

4. **Install the RF system**: Mount the 13.56 MHz RF generator outside the chamber. Connect the RF output to the showerhead electrode through a coaxial feedthrough and automatic matching network. The matching network contains two variable capacitors that adjust to minimize reflected power (<5% of forward power). Install an RF power sensor between the matching network and the feedthrough for forward/reflected power monitoring.

5. **Install the pumping system**: Mount the turbomolecular pump on the bottom CF flange (CF160 or CF200). Connect a dry scroll backing pump to the turbo exhaust. Install a throttle valve between the chamber and the turbo for process pressure control (PECVD operates at 0.5-5 Torr — the turbo must be throttled to maintain this pressure). Install a capacitance manometer for pressure feedback.

6. **Build the gas manifold**: Assemble MFCs and pneumatic valves for each process gas (SiH₄, NH₃, N₂, N₂O). Route gas lines to the showerhead inlet. All wetted parts: electropolished 316L stainless steel. Install check valves and flash-back arrestors on flammable gas lines (SiH₄).

7. **Add the load lock**: Build a small vacuum chamber (5-20 L) with two gate valves — one to atmosphere (wafer loading door) and one to the main chamber. Pump the load lock with a dedicated roughing pump. Install a wafer transfer mechanism (magnetic feedthrough or motorized arm). This allows wafer exchange without venting the main chamber.

8. **Assemble and qualify**: Pump down the main chamber to base pressure (<10⁻⁶ Torr). Helium leak check all seals and feedthroughs. Fire the RF plasma at low power (100 W) in Ar to verify uniform glow between the electrodes. Measure deposition rate and uniformity on a test wafer — target ±5-10% thickness uniformity across the wafer.

## Expected Performance

### LPCVD Hot-Wall Tube Reactor

| Parameter | Value |
|-----------|-------|
| Operating pressure | 0.1-1 Torr |
| Operating temperature | 450-900°C (process-dependent) |
| Temperature uniformity | ±1°C across hot zone |
| Film uniformity | ±2-5% across wafer, ±3-8% wafer-to-wafer in batch |
| Batch capacity | 50-200 wafers (150-200 mm) |
| Deposition rate (poly-Si, SiH₄, 620°C) | ~10 nm/min |
| Deposition rate (Si₃N₄, DCS+NH₃, 800°C) | ~3-5 nm/min |
| Deposition rate (SiO₂ TEOS, 700°C) | ~5-15 nm/min |
| Pump-down time (atmosphere to 0.1 Torr) | 5-15 minutes |

### PECVD Parallel-Plate Reactor

| Parameter | Value |
|-----------|-------|
| Base pressure | <10⁻⁶ Torr |
| Process pressure | 0.5-5 Torr |
| Substrate temperature | 200-400°C |
| RF power density | 0.1-1 W/cm² |
| Film uniformity | ±5-10% across 200 mm wafer |
| Deposition rate (SiNₓ, SiH₄+NH₃, 350°C) | 5-50 nm/min |
| Deposition rate (SiO₂, SiH₄+N₂O, 350°C) | 10-30 nm/min |
| Throughput | 10-25 wafers/hour (single wafer, with load lock) |
| Pump-down (load lock) | 2-5 minutes |
| Pump-down (main chamber from vent) | 15-30 minutes |

## Strengths

- LPCVD: excellent film uniformity (±2-5%), high throughput (batch of 50-200 wafers), simple vacuum requirements (roughing pump only)
- PECVD: low deposition temperature (200-400°C) enables deposition on metallized wafers; plasma-enhanced reactions give higher deposition rates

## Weaknesses

- LPCVD: hot-wall design deposits film on tube walls, requiring periodic tube replacement (50-200 runs); particle generation from wall flaking
- PECVD: higher particle generation from chamber wall deposition; film quality (hydrogen content, density) lower than LPCVD; RF system adds complexity

## Safety

- **Silane (SiH₄)**: Pyrophoric — ignites spontaneously in air. Leaks produce silicon dioxide powder and fire. Use in enclosed gas cabinets with continuous monitoring. Install flash-back arrestors on all SiH₄ lines. Exhaust gas must pass through a burn box or scrubber.
- **Ammonia (NH₃)**: Corrosive and toxic (IDLH 300 ppm). Use in gas cabinets with leak detection. Exhaust through wet scrubber.
- **RF radiation**: 13.56 MHz RF power at 300-3000 W. Interlocked enclosure — RF must shut off when chamber is open. Measure RF leakage at the chamber surface — must be below 10 mW/cm² per OSHA standards.
- **Hot surfaces**: LPCVD tube at 600-900°C and PECVD platen at 200-400°C. Allow cooling before servicing. Use heat-resistant gloves. Post temperature warning signs.

## See Also

- [Deposition Systems](../vacuum/deposition-systems.md) — process chemistry, CVD vs. PVD selection guide
- [Vacuum Chamber](../vacuum/vacuum-chamber.md) — chamber construction details
- [Gas Handling](../gas-handling/index.md) — gas delivery, MFCs, gas cabinet safety
- [Core Fab Processes](fab-processes.md) — how CVD fits into the full IC fabrication flow
- [Electric Furnaces](../energy/electric-furnaces.md) — resistance furnace construction

[← Back to Photolithography](index.md)
