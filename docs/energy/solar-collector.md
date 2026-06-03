# Solar Thermal Collector

> **Node ID**: energy.solar-thermal.collector
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.solar-thermal`](solar-thermal.md), [`glass.basic`](../glass/basic.md), [`metals.copper-bronze`](../metals/copper-bronze.md)
> **Enables**: [`energy.steam-power`](steam-power.md), [`energy.cooling`](cooling.md)
> **Timeline**: Years 5-20
> **Outputs**: solar_heat, heated_water, process_heat
> **Critical**: No — solar thermal collectors supplement fuel-fired heat sources, reducing fuel consumption where sunlight is available

## Principle

A solar thermal collector absorbs solar radiation and converts it to usable heat. Two fundamental designs exist: **flat-plate collectors** (no concentration, 40-80°C output) and **parabolic trough concentrators** (30-100× concentration, 300-500°C output). Both rely on the selective surface principle — a surface that absorbs strongly in the solar spectrum (absorptivity >0.95) but emits weakly in the infrared (emissivity <0.15), minimizing radiative heat loss while maximizing solar energy capture.

The energy balance is: Q_useful = (Solar irradiance × Aperture area × Optical efficiency) - (Thermal losses from receiver). Flat-plate collectors lose heat by convection and radiation from the entire absorber surface. Concentrating collectors reduce thermal losses by focusing sunlight onto a small receiver area, achieving higher temperatures at the cost of requiring sun tracking.

Peak solar irradiance at Earth's surface: 800-1000 W/m² (direct normal irradiance, DNI). Annual solar energy: 1000-2800 kWh/m²/year depending on latitude and climate.

## Materials

### Flat-Plate Collector (2 m², water heating)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Copper tubing](../metals/copper-bronze.md) | 15-20 m | 15 mm OD, 1 mm wall, serpentine pattern | [Copper & Bronze](../metals/copper-bronze.md) | Stainless steel tubing (lower conductivity) |
| [Flat glass sheet](../glass/basic.md) | 1 sheet | 4 mm thick, 2 m², low-iron tempered | [Glass](../glass/basic.md) | Polycarbonate (UV degrades, lower temp) |
| [Steel sheet (absorber plate)](../metals/iron-steel.md) | 2 m² | 0.5-1.0 mm, painted matte black | [Iron & Steel](../metals/iron-steel.md) | Copper sheet (better conductivity, expensive) |
| [Mineral wool insulation](../chemistry/index.md) | 1-2 m² | 50 mm thick, 50-100 kg/m³ | [Chemistry](../chemistry/index.md) | Cork (lower R-value), straw (fire risk) |
| [Steel or copper tank](../metals/index.md) | 1 unit | 200 liters, 1.5 mm wall | [Metals](../metals/index.md) | Concrete tank with liner |
| [Black paint](../chemistry/index.md) | 1 liter | Matte, solar absorptivity >0.95 | [Chemistry](../chemistry/index.md) | Soot mixed with linseed oil |
| [Rubber or silicone gasket](../polymers/index.md) | 5 m | 3-5 mm cord, food-grade silicone | [Polymers](../polymers/index.md) | Clay putty (less durable) |
| [Wood or steel framing](../plants/structural-plants.md) | 5-10 m | 25 × 50 mm timber or 1 mm steel | [Plants](../plants/index.md) | Aluminum extrusion |

### Parabolic Trough Collector (10 m² aperture)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Curved glass mirror](../glass/basic.md) | 10 m² | 4 mm, silvered, reflectivity 90-95% | [Glass](../glass/basic.md) | Polished aluminum (70-80% reflectivity) |
| [Steel receiver tube](../metals/iron-steel.md) | 5-8 m | 50 mm OD, selective coating | [Iron & Steel](../metals/iron-steel.md) | Copper tube (better conductivity, lower max temp) |
| [Glass envelope tube](../glass/basic.md) | 5-8 m | 80 mm OD, borosilicate, evacuated | [Glass](../glass/basic.md) | None — required for vacuum insulation |
| [Steel support structure](../metals/iron-steel.md) | 50-80 kg | Galvanized, parabolic frame | [Iron & Steel](../metals/iron-steel.md) | Wood (limited rigidity, rot) |
| [Heat transfer fluid](../chemistry/index.md) | 50-100 liters | Mineral oil, rated to 300°C | [Chemistry](../chemistry/index.md) | Water (limited to 100°C at 1 atm) |
| [Tracking mechanism](../electronics/index.md) | 1 unit | Gear motor + shadow sensor controller | [Electronics](../electronics/index.md) | Manual adjustment (labor-intensive) |
| [Circulation pump](steam-power.md) | 1 unit | 0.5-1 kW, rated for fluid temperature | [Energy](./index.md) | Thermosiphon (limited height) |

## Construction Steps

### Flat-Plate Collector

1. **Build the absorber plate**: Paint a copper or steel sheet matte black (two coats, cured at 100°C for 1 hour). Solder or braze copper tubing in a serpentine pattern on the back of the plate, spacing tubes 100-150 mm apart. Test solder joints at 2 bar water pressure for 30 minutes — zero leaks acceptable.

2. **Assemble the collector box**: Build a shallow wooden or metal box (100-150 mm deep). Install 50 mm mineral wool insulation on the bottom and sides. Place the absorber plate (painted side up) on top of the insulation.

3. **Install the glass cover**: Lay a single pane of 4 mm flat glass on top of the box, sealed with silicone gasket around the perimeter. The 25-40 mm air gap between glass and absorber provides greenhouse-effect insulation (glass transmits visible light but blocks infrared re-radiation from the absorber).

4. **Seal the box** with weatherproofing — paint or varnish all exterior wood, caulk all joints. The box must be watertight to prevent insulation degradation.

5. **Mount the storage tank** above the collector (minimum 0.5 m height difference for thermosiphon flow). Connect the collector outlet to the tank top (hot) and tank bottom to the collector inlet (cold) with insulated copper pipe. Slope pipes at 10-20 mm/m toward the collector for drainage.

6. **Fill and bleed**: Fill the system with water. Open the bleed valve at the highest point until water flows (all air purged). Close bleed valve. The system is now ready for thermosiphon circulation — no pump required.

### Parabolic Trough Collector

7. **Form the parabolic reflector**: Bend glass sheet into a parabolic curve using a mold and heat, or attach polished aluminum sheet to a parabolic-shaped steel frame. The parabola equation y = x²/(4f) defines the curve, where f is the focal length. For a 2 m aperture width with f = 0.5 m: the focal point is 500 mm above the vertex.

8. **Install the silver backing** (if using glass): Apply silver nitrate solution to the concave surface, reduce to metallic silver. Protect with copper backing and paint. Reflectivity: 90-95%.

9. **Mount the receiver tube** at the focal line. The receiver is a steel tube (50 mm OD) with a selective coating (black chrome electroplated — absorptivity >0.95, emissivity <0.15). Surround the receiver with a glass envelope tube (80 mm OD borosilicate), evacuate to <0.1 Pa (0.001 mbar). The vacuum eliminates convective heat loss from the receiver.

10. **Fabricate the support structure** from galvanized steel. The trough rotates on a single horizontal axis (east-west tracking). Mount the pivot bearings on steel posts set in concrete foundations.

11. **Install the tracking system**: A small gear motor (10-30 W) drives the trough rotation. A shadow-sensor controller (two photovoltaic cells on a divider — motor turns until both cells receive equal light) provides simple, reliable sun tracking. Accuracy: ±0.1°.

12. **Connect the heat transfer loop**: Route heat transfer fluid (mineral oil) through the receiver tube in a closed loop. Install a circulation pump (0.5-1 kW), an expansion tank, a pressure gauge, and a temperature indicator at the receiver outlet.

## Calibration and Verification

1. **Flat-plate pressure test**: Pressurize the collector tubing at 2 bar for 30 minutes. Zero pressure drop acceptable.

2. **Flat-plate thermal test**: On a clear day with solar irradiance >700 W/m², measure the temperature rise between tank bottom (cold) and collector outlet (hot). Target: 15-30°C at peak sun. Calculate daily thermal output: Q = V × ρ × Cp × ΔT. Target: 6-10 kWh/day for 2 m² in summer.

3. **Parabolic alignment**: Place a target rod at the calculated focal point. Sunlight reflected from the trough should concentrate on a line no wider than 25 mm diameter. Adjust mirror mounting if focal line is wider.

4. **Parabolic thermal test**: At peak sun (DNI >800 W/m²), measure heat transfer fluid temperature rise through the receiver. Target: 30-80°C rise depending on flow rate. Receiver tube temperature should reach 300-500°C at design flow rate.

5. **Tracking accuracy**: Observe the concentrated line on the receiver throughout the day. It should remain centered within ±5 mm of receiver center. Adjust controller sensitivity if tracking drifts.

## Expected Performance

### Flat-Plate Collector

| Parameter | Value |
|-----------|-------|
| Thermal output | 6-10 kWh/day (summer, 2 m², temperate) |
| Peak water temperature | 50-80°C |
| Collector efficiency | 40-55% |
| Stagnation temperature | 120-180°C (no flow) |
| Thermosiphon flow rate | 0.01-0.05 L/s (passive) |
| Service life | 20-30 years (glass cover), 10-15 years (selective coating) |

### Parabolic Trough Collector

| Parameter | Value |
|-----------|-------|
| Thermal output | 5-8 kW peak per 10 m² (DNI >800 W/m²) |
| Receiver temperature | 300-500°C |
| Concentration ratio | 30-100× |
| Collector efficiency | 55-70% |
| Tracking accuracy | ±0.1° (motorized), ±1° (manual) |
| Mirror reflectivity (new) | 90-95% |
| Service life | 25-30 years (mirrors), 15-20 years (selective coating) |

## Strengths

- **Flat-plate**: No moving parts or pumps (thermosiphon), buildable with basic materials (copper, glass, steel), 20-30 year lifetime, reduces fuel consumption 50-70% for water heating
- **Parabolic trough**: Achieves temperatures (300-500°C) suitable for steam generation and industrial processes, modular and scalable, proven commercial technology

## Weaknesses

- **Flat-plate**: Maximum 80°C limits applications, no output at night, winter output is 30-40% of summer, freezing risk in cold climates
- **Parabolic trough**: Requires curved glass or precision-formed reflectors, tracking system adds complexity and maintenance, single-axis tracking loses 10-15% of available energy vs. two-axis

## Safety

- **Parabolic concentrated flux**: Reflected sunlight from trough concentrators produces flux densities capable of igniting clothing and causing retinal damage. Never look directly at the receiver from within the mirror field.
- **Hot heat transfer fluid**: Mineral oil at 300°C causes severe burns. Use insulated piping and avoid contact.
- **Evacuated tube implosion**: Evacuated glass tubes are under external atmospheric pressure. A tube break produces an implosion with glass fragments. Wear safety glasses when handling.

## See Also

- [Solar Thermal Energy](solar-thermal.md) — full coverage of solar thermal technologies, heliostats, and thermal storage
- [Steam Power](steam-power.md) — steam generation from solar-heated fluid
- [Steam Turbines](steam-turbines.md) — power generation from solar-generated steam
- [Glass Manufacturing](../glass/basic.md) — mirror and cover glass production
- [Copper & Bronze](../metals/copper-bronze.md) — tubing for absorber plates and receivers
- [Cooling Systems](cooling.md) — absorption cooling driven by solar heat

---

*Part of the [Bootciv Tech Tree](../index.md) · [Energy](./index.md) · [All Domains](../index.md)*
