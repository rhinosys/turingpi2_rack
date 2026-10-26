# BOM — Rack Blade Turing Pi 2.5

Prototype : les vis de PSU et certaines interfaces nécessitent encore validation sur le matériel réel.

## Pièces imprimées

| Référence | Quantité |
|---|---:|
| Q-AV-D / Q-AV-G / Q-AR-D / Q-AR-G | 1 chacune |
| CL-AV / CL-AR | 1 chacune |
| FW-D / FW-G | 1 chacune |
| TOP-AV-D / TOP-AV-G / TOP-AR-D / TOP-AR-G | 1 chacune |
| EAR-D / EAR-G | 1 chacune |
| BT-D / BT-G | 1 chacune |
| BF-D / BF-G | 1 chacune |
| HANDLE-D / HANDLE-G | 1 chacune |
| BIS | 20 : 16 utilisés, 4 de réserve |
| BIS-X | 2 |

PETG, densité de calcul 1,27 g/cm³. Les masses du rapport sont à matériau plein, pas une prédiction du poids avec un taux de remplissage donné.

## Visserie indicative, à vérifier au montage

| Usage | Vis | Quantité | Écrous |
|---|---|---:|---|
| Cartes sur entretoises | M3 × 22 | 8 | 8 M3 |
| Façades sur tiroirs | M3 × 12 | 8 | 8 M3 |
| Oreilles sur cadres | M4 × 12 | 6 | 6 M4 |
| Verrouillage des blades | M4 moletée × 12, tête ≤ 8 mm | 4 | 4 M4 |
| Ventilateurs de 25 mm | M4 × 35 | 8 | 8 M4 |
| Pieds des parois ventilateurs | M4 × 16 | 4 | 4 M4 |
| Pieds des cloisons | M4 × 12 | 16 | 16 M4 |
| Jonctions latérales avant/arrière | M4 × 16 | 4 | 4 M4 |
| Rabats des capots | M4 × 12 | 12 | 12 M4 |
| Capots sur cloisons centrales | M4 × 16 + rondelles larges traversant la couture | 4 | 4 M4 |
| Poignées séparées | M4 × 35 | 4 | 4 M4 |
| Alimentations | UNC 6-32, longueur selon fabricant | 8 | filetage de l'alimentation, pas écrou M4 |
| Fixation au rack | vis et écrous-cages adaptés au rack | selon implantation | selon rack |

Total indicatif : 16 écrous M3, 62 écrous M4. Vérifier longueurs, engagement utile et absence de contact avec les PCB avant serrage. Ne pas remplacer les 6-32 par des vis métriques ni visser trop profondément dans une alimentation.

## Équipements

- Révision R2 : joints fins compressibles ou bande d'étanchéité pour les jonctions de panneaux et capots ; obturation des passages inutilisés. Choisir l'épaisseur comprimée selon les jeux réels. Consommables non modélisés.

- 2 Turing Pi 2.5.
- 8 RK1 et leurs dissipateurs ventilés.
- 2 Cooler Master MWE Bronze 750 V3 à câbles fixes.
- 2 ventilateurs 120 × 120 × 25 mm, 12 V, soufflant vers l'arrière.
- 2 boutons Ø 16 mm à LED, raccordement au header Front I/O.
- 2 sangles velcro de 25 mm pour les alimentations.
- 2 rallonges ATX 24 broches si les câbles d'origine ne permettent pas la course.
- Longueur de faisceau : réserve mobile minimale 250 mm selon cahier des charges, distincte de la longueur fixe de cheminement. Longueur totale à mesurer sur montage réel avec détours, rayon de courbure et détrompage.
