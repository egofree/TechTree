# HDL input

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

Designers write behavior in Verilog or VHDL. Behavioral code describes *what* the circuit does (e.g., "compute CRC-32 on incoming data stream"), not *how* it's built (specific gates and wiring). Register Transfer Level (RTL) is the typical abstraction — data moves between registers on clock edges, with combinational logic between them.
