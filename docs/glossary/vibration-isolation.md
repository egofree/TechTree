# Vibration Isolation

> **Type**: noun | **Tier**: critical | **Domains**: chemistry, photolithography, silicon, vlsi-scaling

Precision photolithography tools (steppers, mask aligners) require vibration <0.1 μm displacement. Vibration isolation pads (neoprene rubber or air-spring mounts) under tool bases. Massive concrete inertia blocks (2-5 tonnes) decouple tools from floor vibrations. Facility sited away from heavy machinery, rail lines, and road traffic if possible.

## Context in the Tech Tree

Vibration isolation — the practice of decoupling precision equipment from external vibration sources — becomes critical at the highest levels of manufacturing precision. In [Cleanrooms](../photolithography/cleanrooms.md), photolithography steppers and mask aligners project circuit patterns onto silicon wafers at sub-micron resolution; any vibration during exposure blurs the image, destroying device yield. In [CZ Crystal Pulling](../silicon/crystal-growth.cz-pulling.md), vibration disturbs the crystal-melt interface, introducing dislocations that render silicon ingots useless. In [Advanced Lithography](../vlsi-scaling/advanced-lithography.md), as feature sizes shrink below 1 μm, vibration tolerance tightens proportionally.

## Technical Details

Vibration isolation uses both passive and active approaches. Passive isolation relies on mechanical compliance: neoprene rubber pads (effective above ~10 Hz), air-spring mounts (adjustable stiffness, effective above ~2 Hz), and massive inertia blocks (2-5 tonne concrete slabs that absorb vibration energy through inertia). The isolation principle is mechanical impedance mismatch — a soft mount between a rigid floor and a massive tool attenuates transmitted vibration proportional to the frequency ratio above the system's natural frequency.

Facility siting provides the first line of defense: locate precision manufacturing away from heavy machinery (forge hammers, stamping presses), rail lines, and busy roads. Where isolation from ambient ground vibration is insufficient, active vibration cancellation systems use sensors and actuators to generate anti-phase vibrations that cancel incoming disturbances.

The vibration budget cascades through the tool stack: floor → isolation mounts → tool frame → wafer stage → exposure plane. Each interface must attenuate vibration below the cumulative tolerance for the final feature size.

## Related Terms

- [Vibration](./vibration.md) — the mechanical phenomenon being isolated
- [Temperature Control](./temperature-control.md) — companion precision requirement in cleanrooms

## Appears In

- [Cement](../chemistry/cement.md)
- [Cleanrooms](../photolithography/cleanrooms.md)
- [CZ Crystal Pulling](../silicon/crystal-growth.cz-pulling.md)
- [Advanced Lithography](../vlsi-scaling/advanced-lithography.md)
