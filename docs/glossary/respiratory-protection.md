# Respiratory Protection

> **Type**: equipment | **Tier**: critical | **Domains**: ehs, mining, chemistry, ceramics

Equipment and practices that prevent inhalation of harmful dusts, fumes, gases, and vapors. Respiratory protection is the last line of defense when engineering controls (ventilation, enclosure, wet methods) cannot reduce airborne contaminants to safe levels. In industrial bootstrapping, where enclosed processes and mechanical ventilation may not yet exist, respiratory protection is often the primary defense against silicosis, metal fume fever, chemical pneumonitis, and asphyxiation.

## Context in the Tech Tree

Respiratory hazards appear at every stage of industrial development. In [Mining](../mining/drilling.md), silica dust from drilling and crushing causes silicosis — the oldest known occupational disease. In [Metal Casting](../machine-tools/casting.md), metal fumes (zinc, lead, manganese) cause metal fume fever and chronic poisoning. In [Chemical Processing](../chemistry/acids.md), acid mists and toxic gases (chlorine, hydrogen sulfide, carbon monoxide) are lethal at low concentrations. In [Ceramics](../ceramics/kilns.md), kiln firing releases silica dust and heavy metal vapors from glazes.

Respiratory protection ranges from simple cloth filters (effective against coarse dust, useless against gases and fine particulates) to half-face respirators with replaceable cartridges (effective against specific contaminants when properly fitted) to supplied-air systems (necessary for Immediately Dangerous to Life and Health (IDLH) atmospheres).

## Technical Details

The hierarchy of respiratory protection, from simplest to most effective:

1. **Cloth/bandana filter**: Stops visible dust only. No protection against fine particulates (PM2.5), fumes, or gases. Better than nothing for coarse dust but creates false confidence.
2. **Disposable particulate respirator (N95/P100 equivalent)**: Mechanical filter that captures 95-99.97% of airborne particles ≥0.3 μm. Requires proper seal against face (no beards). Protection against dusts, mists, fumes — NOT gases or vapors. Service life limited by filter loading (breathing resistance increases).
3. **Half-face respirator with cartridges**: Reusable rubber facepiece with replaceable filter cartridges. Combined particulate/gas cartridges available. Requires fit testing and cartridge change schedule. Protects against specific gas classes (organic vapor, acid gas, ammonia, mercury vapor) when correct cartridge is selected.
4. **Full-face respirator**: Same as half-face but with face shield protecting eyes from splashes and irritants. Higher protection factor (50 vs. 10 for half-face).
5. **Supplied-air (airline) respirator**: Clean air from a remote source. Required for IDLH atmospheres (high CO, low oxygen, high toxic gas concentrations). Used in confined spaces, tank entry, emergency response.
6. **Self-contained breathing apparatus (SCBA)**: Independent air supply. Used for emergency entry into unknown atmospheres. Limited duration (15-60 minutes depending on tank size and exertion level).

For bootstrapping, the critical sequence is: wet methods and ventilation first (reduce the hazard at the source), then particulate filters for dust-generating operations, progressing to cartridge respirators as chemical processes are introduced. The minimum standard for any operation generating visible dust, fume, or mist is a properly fitted particulate respirator.

## Related Terms

- [Prevention](./prevention.md) — respiratory protection is the last line of defense when prevention is insufficient
- [Safety](./safety.md) — general safety practices including respiratory hazard identification
- [Contamination](./contamination.md) — airborne contamination is the respiratory protection concern

## Appears In

- [Mining Operations](../mining/drilling.md)
- [Metal Casting](../machine-tools/casting.md)
- [Acid Production](../chemistry/acids.md)
- [Kiln Design](../ceramics/kilns.md)
- [Personal Protective Equipment](../ehs/ppe.md)
