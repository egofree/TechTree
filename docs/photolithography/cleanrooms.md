# Cleanrooms

> **Node ID**: `photolithography.cleanrooms`
> **Domain**: [Photolithography & IC Fabrication](./)
> **Dependencies**: `advanced-materials`, `specialty-gases`
> **Timeline**: Years 40-70
> **Outputs**: cleanrooms, ultra_pure_water, cleanroom_consumables

### Cleanrooms
Contamination is the enemy of yield. A single 1 μm particle on a wafer can kill an entire chip. Cleanroom class determines minimum feature size achievable: Class 1000 (ISO 6) for >5 μm features, Class 100 (ISO 5) for 1-5 μm, Class 10 (ISO 4) for sub-micron.

**Cleanroom construction**:
- **Structure**: Enclosed room with smooth, non-shedding walls (epoxy-painted steel, aluminum, or plastic laminate). Flush surfaces, rounded corners, no horizontal surfaces that collect dust. Positive pressure (10-20 Pa above ambient) so air leaks OUT, not in. Airlock entry (personnel and materials enter through separate airlocks with interlocked doors).
- **Air filtration**: HEPA filters (99.97% efficient at 0.3 μm) in ceiling. Laminar flow (air flows in parallel streamlines from ceiling to floor perforations). 20-60 air changes per hour for Class 100. ULPA filters (99.999% at 0.12 μm) for Class 10 and below.
- **Flooring**: Vinyl or raised perforated floor panels (air return). Sticky mats at entrances (tacky surface pulls particles off shoe covers). Anti-static treatment.
- **Lighting**: Tear-drop or flush-mounted fixtures (no horizontal surfaces). UV-blocking if photoresist is light-sensitive.
- **Gowning**: Cleanroom garments (Tyvek, polyester, or polypropylene — non-linting) cover head, body, and shoes. Gloves (nitrile or latex — powder-free). Face mask. Gowning room with sticky mat and air shower.
- **Ultra-pure water (UPW) system**:
  - **Pre-treatment**: Sand filter → carbon filter → water softener
  - **RO (reverse osmosis)**: Semi-permeable membrane removes 95-99% of dissolved ions and organics. Pressure 10-60 bar.
  - **DI (deionization)**: Ion exchange resin beds remove remaining ions. Resistivity target >18 MΩ·cm.
  - **UV sterilization**: 254 nm UV lamp kills bacteria and algae.
  - **Final filtration**: 0.05-0.2 μm membrane filter removes particles.
  - **Distribution**: PVDF or PFA piping (no leaching). Continuous recirculation (no dead legs where bacteria grow).
  - **Quality testing**: Online resistivity monitoring, particle counting, TOC (total organic carbon) analysis
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
