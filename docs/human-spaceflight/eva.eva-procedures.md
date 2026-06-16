# EVA Procedures + Protocols

> **Node ID**: human-spaceflight.eva.eva-procedures
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.eva`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: eva_procedures, eva_capability
> **Critical**: Yes

EVA procedure development encompasses prebreath protocols, airlock operations, timeline construction, and the choreographed sequence of tasks that constitute a spacewalk. The fundamental challenge is decompression sickness (DCS): the cabin is at 101 kPa (21% O₂) but the suit operates at 29.6 kPa (100% O₂), requiring nitrogen washout before depressurisation.

Two prebreath protocols are in use: the campout protocol (8-hour overnight stay in the airlock at 70.3 kPa) and the exercise prebreath protocol (30 minutes of cycling combined with pure oxygen breathing). Both achieve zero DCS incidence across hundreds of EVAs.

## Key Parameters

| Parameter | Campout | Exercise |
|-----------|---------|----------|
| Total prebreath time | ~10 hr | ~4 hr |
| Exercise required | No | Yes (10 min cycle) |
| Airlock pressure | 70.3 kPa overnight | 101 kPa (cabin) |
| DCS incidence | 0% | 0% |
| EVA duration | 6-8 hr | 6-8 hr |

## EVA Timeline Structure

1. **T-18 hr**: Pre-campout mask, begin O₂ breathing
2. **T-15 hr**: Airlock sealed at 70.3 kPa for overnight campout
3. **T-2 hr**: Suit donning and checkouts
4. **T-1 hr**: Suit purge to 100% O₂
5. **T-0**: Airlock depress; EVA begins
6. **T+6 to T+8 hr**: Return to airlock; repress

## Prerequisites

- [EVA](./eva.md) — parent capability
- [Space Suits](./space-suits.md) — EMU pressure garment and PLSS
- [ECLSS](./eclss.md) — airlock depress/repress and oxygen supply
- [Space Stations](./space-stations.md) — airlock and exterior worksite

## See Also

- [Extravehicular Activity](./eva.md) — parent capability
- [EVA Tools + Restraints](./eva.eva-tools.md) — sibling process
- [Space Suits](./space-suits.md) — suit hardware
