# Electrical Hazards

> **Type**: equipment | **Tier**: critical | **Domains**: ceramics, energy, optics

Evaporation sources carry high current (10-50 A) at low voltage (3-10 V) from a heavy-duty power supply. The current is sufficient to cause severe burns or fire if cables short. Insulate all connections. Use properly rated cables and connectors. Interlock the chamber door to cut power when opened.

## Context in the Tech Tree

Electrical hazards accompany every technology that uses electric power — from electric kilns operating at 240-480V to evaporation sources in semiconductor and optical coating equipment to electrolysis cells drawing hundreds of kiloamperes. The specific hazard profile depends on the voltage and current level: high voltage causes arc flash and electrocution risk; high current causes burns, fire, and magnetic force hazards; both require specific mitigation measures.

## Technical Details

In vacuum deposition systems (used for optical coatings and semiconductor metallization), evaporation sources operate at high current (10-50 A) and low voltage (3-10 V) — the power supply delivers hundreds of watts to resistively heat a boat or filament that evaporates the coating material. The current level is sufficient to cause severe burns if cables short circuit. All connections must be insulated, cables properly rated for the current, and connectors mechanically secure.

Electric kilns operate at higher voltage (240-480V) with correspondingly greater electrocution risk. Lockout/tagout procedures are mandatory for all maintenance. Ground fault protection interrupts circuit on leakage current. Electric furnace electrodes in submerged arc furnaces carry tens of thousands of amperes at low voltage — the magnetic fields around the bus bars can attract ferromagnetic objects and the resistive heating in joints can cause fires if connections are not properly torqued and maintained.

In electrolysis, the hazard is primarily from the DC bus bars carrying 100-500 kA at 4-5V per cell. Even 0.001 Ω of contact resistance at these currents dissipates kilowatts as heat. Bus bars must be short, thick, and well-cooled. Bolted joints use silver-plated contact surfaces to minimize resistance.

General mitigation principles apply across all systems: interlock doors to cut power when opened (especially vacuum chamber doors and kiln access panels); use lockout/tagout for maintenance; properly rate all cables and connectors for the maximum fault current; and ground all equipment chassis.

## Related Terms

- [Electrical Insulation](./electrical-insulation.md) — insulation prevents electrical hazards
- [Efficiency](./efficiency.md) — electrical losses create heat hazards

## Appears In

- [Advanced Ceramics](../ceramics/advanced-ceramics.md)
- [Electrode Manufacturing](../energy/electrode-manufacturing.md)
- [Optical Coatings](../optics/optical-coatings.md)
