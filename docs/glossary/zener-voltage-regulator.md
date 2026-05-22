# Zener voltage regulator

> **Type**: equipment | **Tier**: important | **Domains**: silicon

Zener diode in reverse bias with series resistor. Input voltage Vin through resistor R to Zener cathode. Zener maintains approximately constant voltage Vz across the load. Design: R = (Vin_min - Vz)/(Iz_min + Iload_max). Power dissipation in Zener: Pz = Vz × Iz. Must keep Pz below Zener's rated dissipation (typically 0.4-1.5W for small devices).
