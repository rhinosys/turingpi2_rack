[Read in English](../en/architecture.md)

# Architecture et pièces

## Châssis fixe

Quatre tunnels monoblocs réunissent plancher, paroi extérieure, toit, demi-cloison centrale et guide. Ils s’impriment avec l’axe du tunnel vertical. Les deux demi-cloisons centrales se présentent dos à dos ; les tunnels avant intègrent les oreilles de fixation.

![Châssis vide ; géométrie V6 conservée en V7](../assets/enclosure-v6.png)

| Enveloppe | Dimension nominale |
|---|---:|
| Largeur de façade avec oreilles | 482,6 mm |
| Largeur du châssis | 446 mm |
| Hauteur du châssis | 176,5 mm |
| Profondeur du châssis | 424 mm |

L’air entre devant et sort derrière. Les poches hexagonales extérieures conservent un **fond de 1 mm** pour éviter les fuites par les côtés, le dessous et le toit. Jointoyer les raccords fixes sans obstruer les guides. Une baie vide nécessite un obturateur si l’autre fonctionne ; aucun obturateur de production n’est fourni.

## Cassettes extractibles

Chaque cassette réunit un fond avant et un fond arrière avec des murets d’environ 60 mm. Leurs doigts entrelacés sont verrouillés par du filament de 1,75 mm. La division avant/arrière permet l’impression. Les goupilles en filament remplacent les anciennes éclisses vissées, pas les fixations des équipements ou du rack.

![Jonction verrouillée par filament, vue éclatée](../assets/joint-v7.png)

| Référence | Fonction | Quantité pour le rack |
|---|---|---:|
| Q-AV-D / Q-AV-G-EAR | Tunnel avant droit/gauche avec oreille intégrée | 1 chacun |
| Q-AR-D / Q-AR-G | Tunnel arrière droit/gauche | 1 chacun |
| BT-D / BT-G | Fond avant et supports de carte | 1 chacun |
| FOND-AR-D / FOND-AR-G | Fond arrière, support ventilateur, berceau PSU et panneau arrière | 1 chacun |
| BF-D / BF-G | Façade | 1 chacun |
| HANDLE-D / HANDLE-G | Poignée | 1 chacun |
| BIS / BIS-X | Biscuits rectangulaires / centraux | 16 / 2 |
| Goupilles filament | Filament de 1,75 mm, longueur d’environ 61 mm | 4 |

D = droite, G = gauche, AV = avant, AR = arrière. Les corps REF sont des gabarits d’encombrement et ne doivent pas être imprimés.

## Matériel acheté

Deux Turing Pi 2.5, modules RK1 avec refroidissement actif, deux Cooler Master MWE Bronze 750 V3, deux ventilateurs 120 mm, visserie de carte/façade/poignée, sangles de maintien PSU, deux rails métalliques en L et quatre berceaux. Les enveloppes de référence sont 150 × 140 × 86 mm pour la PSU et 120 × 120 × 25 mm pour le ventilateur. Ces **hypothèses de conception restent à vérifier sur le matériel acheté**.

Les berceaux demandent huit fixations M6 au total, deux par berceau, puis deux vis M4 × 20 et deux écrous M4 pour les verrous arrière. Déterminer la longueur M6 avec l’empilage réel montant/platine/rondelle. Les longueurs de vis des équipements et le maintien PSU demandent un contrôle final ; la nomenclature du prompt initial n’est pas une liste d’achat V7 définitive.
