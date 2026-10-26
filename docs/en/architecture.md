[Lire en français](../fr/architecture.md)

# Architecture and parts

## Fixed enclosure

Four integral tunnels combine the floor, outer wall, roof, half of the centre partition and guide. They are printed with the tunnel axis vertical. The two centre half-walls sit back-to-back; the front tunnels include the rack ears.

![Empty enclosure; V6 geometry retained in V7](../assets/enclosure-v6.png)

| Envelope | Nominal dimension |
|---|---:|
| Front width including ears | 482.6 mm |
| Enclosure width | 446 mm |
| Enclosure height | 176.5 mm |
| Enclosure depth | 424 mm |

Air enters at the front and exits at the rear. Outer hexagonal relief pockets retain a **1 mm skin** instead of becoming air leaks through the sides, floor or roof. Seal fixed seams without obstructing the guides. A blanking panel is needed when operating with an empty bay; a production blanking panel is not included.

## Removable cassettes

Each cassette joins a front floor to a rear floor with approximately 60 mm-high side walls. Interleaving fingers are pinned with 1.75 mm filament. The front/rear split keeps the parts printable. The filament pins replace the old screwed splice bars, not equipment or rack fasteners.

![Filament-locked joint, exploded](../assets/joint-v7.png)

| Reference | Meaning | Quantity for the rack |
|---|---|---:|
| Q-AV-D / Q-AV-G-EAR | Right/left front tunnel, integrated ear | 1 each |
| Q-AR-D / Q-AR-G | Right/left rear tunnel | 1 each |
| BT-D / BT-G | Front cassette floor and board supports | 1 each |
| FOND-AR-D / FOND-AR-G | Rear floor, fan support, PSU cradle and rear panel | 1 each |
| BF-D / BF-G | Front panel | 1 each |
| HANDLE-D / HANDLE-G | Handle | 1 each |
| BIS / BIS-X | Rectangular / central alignment biscuits | 16 / 2 |
| Filament pins | Cut from 1.75 mm filament, about 61 mm long | 4 |

D = right, G = left, AV = front, AR = rear. REF bodies are clearance envelopes and must not be printed.

## Purchased hardware

Two Turing Pi 2.5 boards, RK1 modules with active coolers, two Cooler Master MWE Bronze 750 V3 supplies, two 120 mm fans, board/front-panel/handle fasteners, PSU retaining straps, two metal L rails and four rail saddles. The reference PSU envelope is 150 × 140 × 86 mm, fan envelope 120 × 120 × 25 mm. These are **design assumptions to verify on the purchased hardware**, not measured guarantees.

The rail saddles need eight M6 rack fasteners total, two per saddle, plus two M4 × 20 screws and two M4 nuts for rear locking. Confirm the M6 length from the actual rack/plate/washer stack. Equipment screw lengths and PSU retention need final fit checks; the original prompt BOM is not a final V7 shopping list.
