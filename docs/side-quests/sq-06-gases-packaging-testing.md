# SQ 6: Specialty Gases, Consumables, Packaging &amp; Testing

**Starts**: Phase 5–8  
**Priority**: Critical for semiconductor fabrication — the fab doesn't work without these.

## Problem

Semiconductor fabrication requires ultra-pure gases, specialized consumables, and packaging/testing infrastructure that are often overlooked in simplified tech trees. Without these, even perfect lithography produces non-functional chips.

## Technologies &amp; Systems

### Specialty Gas Production &amp; Purification
- **Inert gases**: Argon (from air separation — fractional distillation of liquid air), nitrogen
- **Hydrogen**: Electrolysis of water, steam reforming of hydrocarbons
- **Silane (SiH₄)**: MG-Si + HCl → trichlorosilane → redistribution reaction → SiH₄
  - Pyrophoric — auto-ignites in air, requires inert handling
- **Dopant gases**: Phosphine (PH₃), arsine (AsH₃), diborane (B₂H₆)
  - EXTREMELY toxic — ppb-level lethal concentrations
- **Etch gases**: CF₄, SF₆, Cl₂, BCl₃ (for plasma etching)
- **Purification**: Catalytic getters, molecular sieves, cryogenic trapping, palladium membrane (for H₂)

### Cleanroom Consumables
- **HEPA/ULPA filter media**: Fine fiberglass or synthetic fiber mats
- **Cleanroom garments**: Tyvek-like or woven synthetic coveralls, hoods, booties
- **Wipers and wipes**: Lint-free synthetic materials
- **Gloves**: Nitrile, latex, or synthetic — particle-free, chemical-resistant
- **Sticky mats**: Tacky surface mats for entrance areas (capture shoe particles)

### Semiconductor Packaging
- **Die attach**: Eutectic bonding or epoxy attachment of die to package/substrate
- **Wire bonding**: Fine gold or aluminum wire (1-mil diameter) connecting die pads to package leads
  - Requires: wire drawing to ultra-fine diameters, ultrasonic or thermosonic bonding equipment
- **Encapsulation**: Epoxy or ceramic hermetic sealing
- **Lead frames**: Stamped or etched metal frames for connecting die to circuit board
- **Advanced packaging** (later): Flip-chip, bumping, chip-scale packages, 2.5D/3D

### Testing Infrastructure
- **Wafer probing**: Probe cards with fine needles contacting bond pads for electrical testing
- **Parametric testing**: Measure transistor characteristics (Vt, Id, leakage, mobility)
- **Functional testing**: Verify logic operation of ICs
- **Burn-in**: Accelerated aging (elevated temperature and voltage) to catch early failures
- **Failure analysis**: Microscopy, cross-sectioning, deprocessing layers to find defects
- **Yield tracking**: Statistical process control for fab optimization

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Phase 5 | Bulk gas production, purification infrastructure |
| Phase 7 | Gas supply for CZ growth (argon), CVD precursors |
| Phase 8 | Complete gas/consumable supply chain for fab, packaging, testing |
| SQ 14 | Epoxy encapsulation, fiberglass filters, nitrile gloves, cleanroom garment materials |

## Key Deliverables

- High-purity argon, nitrogen, hydrogen production capability
- Silane and dopant gas production with full safety infrastructure
- Cleanroom consumable supply chain
- Die packaging line (attach, wire bond, encapsulate)
- Wafer probing and parametric test capability

[← Side Quests Index](index.md)
