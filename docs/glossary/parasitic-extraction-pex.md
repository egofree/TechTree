# Parasitic extraction (PEX)

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

After layout, extract the parasitic resistance (R) and capacitance (C) of every wire. These parasitics add delay and coupling noise that aren't present in the pre-layout netlist. Post-layout STA with extracted parasitics gives the most accurate timing prediction. Interconnect delay dominates total path delay at nodes below 130 nm — wire RC can exceed gate delay.
