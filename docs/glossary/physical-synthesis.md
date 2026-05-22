# Physical synthesis

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

Traditional synthesis operates on an abstract netlist without physical information. Physical synthesis iterates between synthesis and placement — the tool re-synthesizes paths based on actual wire loads from placement rather than statistical wire load models. Critical for sub-130nm designs where interconnect delay dominates. Resizing cells, inserting buffers, and restructuring logic based on physical reality can improve timing by 10-30% over pure logical synthesis.
