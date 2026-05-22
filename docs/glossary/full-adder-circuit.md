# Full adder circuit

> **Type**: noun | **Tier**: important | **Domains**: computing

2 relays per bit position implement the sum and carry functions. Sum = A XOR B XOR Cin (three relays if counting XOR implementation separately, but compact designs reuse the carry relay for one XOR term). Carry = (A AND B) OR (Cin AND (A XOR B)). Each relay adds ~10 ms propagation delay. An 8-bit ripple-carry adder accumulates 80-240 ms of carry propagation, since each bit must wait for the previous carry to settle.
