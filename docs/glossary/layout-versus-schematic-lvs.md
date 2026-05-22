# Layout versus schematic (LVS)

> **Type**: material | **Tier**: important | **Domains**: vlsi-scaling

Extracts the circuit from the physical layout (identify transistors from drawn geometries, trace connectivity through metal layers) and compares it to the original schematic/netlist. Catches errors where layout connections differ from the intended circuit — a single misrouted wire can cause functional failure that simulation won't catch if the wrong path happens to be functionally similar. LVS must report a clean match before tapeout.
