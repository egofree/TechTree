# Timing constraints

> **Type**: material | **Tier**: important | **Domains**: vlsi-scaling

Designers specify clock frequency target (e.g., 1 GHz → 1 ns period) and I/O timing requirements (setup time, hold time at chip pins). The synthesizer uses static timing analysis to verify all paths meet constraints across process corners (fast/fast, slow/slow, typical/typical) and temperature ranges (-40°C to +125°C). Setup violations (data arrives too late) are fixed by adding pipeline stages or upsizing cells. Hold violations (data changes too early before clock) are fixed by adding delay ...
