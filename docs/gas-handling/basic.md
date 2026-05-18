# Basic Gas Handling

> **Node ID**: `gas-handling.basic`
> **Domain**: [Gas Handling](./)
> **Enables**: `specialty-gases.air-separation`, `specialty-gases.hydrogen-silane`
> **Timeline**: Years 20-35
> **Outputs**: gas_handling, compressed_gases, purified_gases

### Infrastructure

**Piping, valves, pumps**:
- **Pipes**: Cast iron (water, dilute alkalis), lead (H₂SO₄ <80%), copper (organic solvents, water), ceramic (acids at high temperature), glass (laboratory scale). Steel for steam and high-pressure gas.
- **Valves**: Bronze gate valves, cast iron plug valves, glass stopcocks (laboratory). PTFE-packed valves for HF service.
- **Pumps**: Centrifugal pumps (motor-driven impeller — most common for liquids), diaphragm pumps (for corrosive/acids), piston pumps (high pressure), gear pumps (viscous liquids). Machine Tools machining produces the precision parts.

**Gas handling**:
- **Compression**: Reciprocating piston compressors (steam or motor driven), 1-10 bar for general use, 100-300 bar for gas cylinders. Multi-stage with intercoolers for high pressures.
- **Storage**: Gas holders (water-sealed bell-type for low pressure), steel cylinders (high pressure, 150-200 bar). Liquified gases in insulated tanks.
- **Purification**: Drying (CaCl₂, silica gel, molecular sieves), scrubbing (water, NaOH solution for acid gases), catalytic getters (for trace impurity removal).

### Pipe Fitting Techniques

- **Threaded connections (NPT — National Pipe Thread Tapered)**: Taper of 1:16 (3/4 inch per foot). Threads seal by deformation of mating surfaces as fitting is tightened. Wrap male threads with PTFE (Teflon) tape — 2-3 wraps clockwise, or apply pipe dope (linseed oil-based paste with fillers). NPT seals are not truly gas-tight at high pressure without sealant. Torque to 1-2 turns past hand-tight. Maximum reliable pressure: ~20 bar for steel, ~10 bar for brass. For higher pressures, use flanged or welded connections.
- **Flanged connections**: Flat-faced or raised-face flanges bolted together with gasket between. Bolt pattern (number and circle diameter) standardized by pressure class (e.g., 4 bolts for 1" Class 150, 8 bolts for 4" Class 150). Tighten bolts in crisscross pattern to seat gasket evenly. Allow re-torque after first thermal cycle.

### Gasket Material Selection

| Material | Service | Temperature Range | Notes |
|----------|---------|-------------------|-------|
| **Copper** | High-temperature steam, oxygen | up to 600°C | Soft metal, seals by plastic deformation. Used in high-pressure and high-temp flanges. |
| **Viton (FKM)** | Aggressive chemicals, fuel gases | -20°C to 200°C | Fluorocarbon elastomer. Resists most organics, acids, chlorine. Swells in ketones. |
| **PTFE (Teflon)** | High-purity gas, corrosive service | -200°C to 260°C | Chemically inert, non-outgassing. Poor creep resistance — use filled PTFE (glass or carbon) for bolted flanges. |
| **Compressed fiber** | Steam, water, inert gases | up to 400°C | Traditional gasket material (asbestos historically, now aramid or glass fiber). Good for utility services. |
| **Rubber (NBR/EPDM)** | Air, water, inert gases at moderate temp | -30°C to 120°C | Cheap, forgiving. Not for hydrocarbons (NBR) or steam (EPDM preferred). |

### Compressor Types

- **Reciprocating (piston)**: Pressure ratio 3-5 per stage. For >5 bar discharge, use multi-stage with intercoolers between stages (cool gas back to near-ambient before next compression stage — reduces work and prevents excessive discharge temperature). Lubricated cylinders for most gases; non-lubricated (PTFE piston rings) for purity-critical service.
- **Diaphragm**: Gas separated from drive mechanism by flexible metal diaphragm. Zero oil contamination — essential for ultra-pure gases (semiconductor-grade H₂, O₂, Ar). Pressure ratio 3-10 per stage. Lower flow rates than piston type.
- **Rotary screw**: Two intermeshing helical rotors compress gas continuously. No pulsation — smooth flow. Pressure ratio 3-15 in single stage. Oil-flooded version for general industry; oil-free (dry screw) for process gas. Higher power consumption than piston at same pressure.

### Gas Cylinder Filling

- **Pressure ratings**: Standard industrial cylinders: 150-200 bar at 15°C. High-pressure cylinders: 250-300 bar. Cylinder stamped with test pressure, date, and serial number.
- **Hydrostatic testing**: Pressurize cylinder with water to 5/3 of working pressure every 5-10 years. Measure permanent expansion (<10% of total expansion). Reject if exceeds limit or if visual inspection finds corrosion, dents, or fire damage.
- **Valve types**: CGA (Compressed Gas Association) standard connections — each gas type has a unique thread/pin pattern to prevent cross-connection (e.g., CGA 580 for inert gases, CGA 350 for flammable gases, CGA 540 for oxygen). Valve outlet threads are right-hand for non-fuel gases and left-hand for fuel gases as an additional safety check.
- **Filling procedure**: Weigh cylinder to determine empty weight (tare). Fill by weight or pressure, accounting for gas compressibility factor. Never exceed stamped fill pressure.
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
