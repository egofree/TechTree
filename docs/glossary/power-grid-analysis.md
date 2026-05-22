# Power grid analysis

> **Type**: material | **Tier**: important | **Domains**: vlsi-scaling

Verify the VDD and VSS distribution networks can deliver required current without excessive voltage drop. IR drop (voltage = current × resistance) reduces supply voltage at the transistor, slowing it down and potentially causing timing failures. Simultaneous switching noise (di/dt × L) causes transient voltage spikes on the power rails. Power grid analysis uses finite-element techniques on the mesh of power wires to compute voltage at every point. Minimum 5-10% margin on supply voltage is sta...
