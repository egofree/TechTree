# Scaling

> **Type**: equipment | **Tier**: critical | **Domains**: computing, mining, silicon

The systematic reduction of device dimensions while maintaining or improving electrical characteristics. In semiconductor manufacturing, Dennard scaling rules govern how transistor shrinkage enables higher density and performance.

## Context in the Tech Tree

Scaling appears in [Electronic Computing](../computing/electronic.md) as the fundamental driver of computational progress, in [Mining Extraction](../mining/extraction.md) for scaling operations from prospecting to production, and in [Basic Semiconductor Devices](../silicon/basic-devices.md) where transistor miniaturization follows predictable physical rules.

## Technical Details

Dennard scaling rules: shrink all device dimensions (channel length, oxide thickness, junction depth) by factor k while scaling voltage by k. Result: transistors are k² times smaller (2× per generation), operate k times faster, and consume k² less power per transistor. Power density remains constant — more transistors per area at the same total power.

This scaling held from the 1 µm node through approximately 65 nm (roughly 1970-2005). Below 65 nm, gate oxide thickness approaches atomic dimensions (1-2 nm), causing quantum tunneling leakage. Voltage scaling stalled at ~1V because subthreshold swing has a physical limit of ~60 mV/decade at room temperature. FinFET and gate-all-around (GAA) transistor architectures were introduced to maintain electrostatic control at smaller nodes.

In mining, scaling refers to moving from small test pits to full production: larger equipment, continuous processing, and higher throughput require proportionally more infrastructure and capital.

## Related Terms

- [NMOS](./nmos.md) — early scaling technology
- [CMOS](./cmos.md) — complementary MOS scaling
- [Crystal Oscillator](./crystal-oscillator.md) — frequency scaling
- [Efficiency](./efficiency.md) — scaling improvements in efficiency
- [Structure](./structure.md) — structural changes at different scales

## Appears In

- [Electronic Computing](../computing/electronic.md)
- [Mining Extraction](../mining/extraction.md)
- [Basic Devices](../silicon/basic-devices.md)
