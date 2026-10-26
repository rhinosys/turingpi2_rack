# Rapport de vérification — Rack Blade Turing Pi 2.5

Date : 24 octobre 2026. Réalisation : MCP SolidCraft, moteur local headless.

**Statut : prototype géométrique à finaliser. Les contrôles de géométrie ne constituent pas une qualification d'impression, de résistance ni d'intégration électrique.** Les réserves ci-dessous sont ouvertes.

## Architecture et composants

Deux baies pour deux TP2.5, chacune avec quatre RK1 et leurs dissipateurs ventilés, deux MWE Bronze 750 V3, deux ventilateurs 120 × 120 × 25. Carte et I/O côté avant. Alimentations à l'arrière, admission supérieure. Les poignées sont des pièces séparées pour éviter de supporter toute la façade à l'impression.

Enveloppes REF : PCB 170 × 170 × 1,6 ; équipements au-dessus 170 × 170 × 45 ; NVMe hypothétique 150 × 120 × 12 au droit de la fenêtre ; PSU 150 × 140 × 86 ; ventilateurs 120 × 120 × 25. **Le REF NVMe n'est pas le plan des quatre SSD réels.**

## Dimensions vérifiées

| Contrôle | Résultat | Statut |
|---|---|---|
| Largeur aux oreilles | 482,60 mm, X = ±241,30 | Conforme |
| Largeur du corps | 446,00 mm | Conforme |
| Hauteur hors tout | 176,50 mm ≤ 177,00 | Conforme |
| Profondeur du corps | 424,00 mm | Conforme |
| Profondeur complète avec poignées | 453,00 mm, Y = −29 à 424 | Dépassement avant volontaire |
| Centres des lumières rack | X = ±232,55 ; Z = 6,35 / 38,10 / 66,675 / 111,125 / 139,70 / 171,45 | Conforme aux cotes demandées |
| Lumières des oreilles | 12 × 7 mm, six par oreille | Conforme |
| Dessous PCB | Z = 26 mm ; fond du tiroir Z = 11 mm | 15 mm de dégagement |
| NVMe hypothétique | Z = 14 à 26, fenêtre 150 × 120 | Enveloppe 12 mm libre ; implantation réelle non vérifiée |
| Ventilateurs | Y = 218 à 243 ; dessus Z = 134 | 39,5 mm jusqu'au dessous nominal du capot |
| Réserve de câbles derrière ventilateurs | Y = 243 à 280 | 37 mm |
| Langue dans la rainure | langue Z = 8,2 à 11,2 ; rainure 8 à 11,4 | 0,2 mm en bas et en haut |
| Fond rainure extérieure | X = 206, langue jusqu'à 205,4 | 0,6 mm, pas 0,1 mm comme annoncé dans le texte source |
| Fond rainure centrale | X = 2, langue commence à 2,6 | 0,6 mm |
| Façade / oreille | X = 208 et 211,3 côté droit | 3,3 mm |
| Alimentation / capot | PSU Z = 10 à 96 | 77,5 mm jusqu'au capot nominal |

La largeur de langue 2,9 mm additionnée au jeu latéral de 0,5 mm donne 0,6 mm au fond des rainures : l'objectif textuel 0,1 mm et les coordonnées du cahier des charges ne sont pas compatibles.

## Volume d'impression et masses

Les mesures ci-dessous viennent de SolidCraft après rotation et translation de chaque pièce pour son export. Limite retenue : 240 × 240 × 210 mm. Les maillages exportés ont également été contrôlés indépendamment.

| Pièce | Encombrement d'impression X × Y × Z, mm | Volume cm³ | PETG plein, g | Volume X1C |
|---|---|---:|---:|---|
| Q-AV-D | 223.00 × 220.00 × 173.50 | 311.95 | 396.18 | Conforme |
| Q-AR-D | 223.00 × 213.80 × 173.50 | 417.25 | 529.91 | Conforme |
| Q-AV-G | 223.00 × 220.00 × 173.50 | 311.95 | 396.18 | Conforme |
| Q-AR-G | 223.00 × 213.80 × 173.50 | 417.25 | 529.91 | Conforme |
| CL-AV | 169.50 × 210.00 × 40.00 | 284.83 | 361.73 | Conforme |
| CL-AR | 169.30 × 210.00 × 40.00 | 281.63 | 357.67 | Conforme |
| FW-D | 214.00 × 164.90 × 21.00 | 141.55 | 179.77 | Conforme |
| FW-G | 214.00 × 164.90 × 21.00 | 141.55 | 179.77 | Conforme |
| BT-D | 202.80 × 201.00 × 19.60 | 74.58 | 94.72 | Conforme |
| BT-G | 202.80 × 201.00 × 19.60 | 73.96 | 93.93 | Conforme |
| EAR-D | 30.00 × 176.50 × 5.00 | 23.83 | 30.26 | Conforme |
| EAR-G | 30.00 × 176.50 × 5.00 | 23.83 | 30.26 | Conforme |
| BF-D | 207.00 × 165.00 × 7.00 | 96.01 | 121.93 | Conforme |
| BF-G | 207.00 × 165.00 × 7.00 | 95.91 | 121.80 | Conforme |
| TOP-AV-D | 223.00 × 210.00 × 18.00 | 127.10 | 161.42 | Conforme |
| TOP-AR-D | 223.00 × 214.00 × 18.00 | 130.12 | 165.25 | Conforme |
| TOP-AV-G | 223.00 × 210.00 × 18.00 | 127.10 | 161.42 | Conforme |
| TOP-AR-G | 223.00 × 214.00 × 18.00 | 130.12 | 165.25 | Conforme |
| BIS | 21.80 × 19.80 × 3.00 | 1.29 | 1.64 | Conforme |
| BIS-X | 21.80 × 21.80 × 3.00 | 1.43 | 1.81 | Conforme |
| HANDLE-G | 90.00 × 25.00 × 12.00 | 9.40 | 11.94 | Conforme |
| HANDLE-D | 90.00 × 25.00 × 12.00 | 9.40 | 11.94 | Conforme |

Masse théorique assemblée avec 16 BIS + 2 BIS-X : **4131.2 g**.
Masse théorique avec les 4 BIS supplémentaires du lot : **4137.8 g**.
Le poids réel dépendra du remplissage, des périmètres, des supports et du tranchage ; aucune consommation de filament tranchée n'est annoncée.

Le lot de 20 biscuits + 2 centraux est un seul 3MF de 22 objets, disposés dans 125,8 × 125,8 × 3 mm.

## Interférences et course

- Contrôle final avec les références et les 18 biscuits installés : **50 corps examinés, 0 interférence, aucune paire non vérifiée, aucun dépassement du budget**. Les deux biscuits maîtres sont stockés à côté de l'assemblage et exclus des STEP d'assemblage.
- 167 paires candidates, 42 écartées géométriquement, 125 intersectées par le moteur.
- Essais de retrait simultané des deux blades : 50, 100, 150 et 195 mm ; chacun donne 0 interférence et aucune paire non vérifiée.
- Ces essais sont quatre positions discrètes, pas une analyse continue de volume balayé ; ils précèdent l'ajout des biscuits, qui restent hors du volume des tiroirs.
- À 195 mm de déplacement, le bord arrière du tiroir arrive à Y = 6 ; le retrait intégral demande environ 201 mm.
- Les câbles ne sont pas modélisés comme des solides flexibles. Il faut au moins 250 mm de réserve mobile, en plus du cheminement fixe. Une longueur totale ne peut pas être certifiée sans position réelle du connecteur, longueur d'origine et rayon de courbure. Prévoir deux rallonges si nécessaire.

Fichiers probants : verification/interference.json et verification/drawer-motion.json.

## Paramètres et historique

Essai standoff_h : 15 → 16 → 15 mm. Les deux reconstructions ont réussi sans erreur (288 fonctions recalculées). Le sommet des entretoises a bien évolué de Z = 26 à 27 mm, puis retour nominal. Le test ne valide pas toutes les combinaisons de paramètres.

L'audit d'historique avant export comporte 482 entrées sans erreur. Onze opérations ont nécessité de légers déplacements de l'outil booléen, inférieurs à 0,001 mm, consignés dans verification/timeline-before-exports.json. Plusieurs détails d'interface restent cotés numériquement : le modèle n'est pas un générateur universel de racks de toutes tailles.

## Ajustements de conception

- PSU surélevés de 6 mm pour reposer sur les berceaux ; ouverture arrière décalée vers le haut.
- Nervures sous tiroirs réduites à 1,6 mm et déplacées. Les nervures de 8 mm initiales pénétraient le plancher. **Cette réduction ne satisfait pas le minimum général de 2,4 mm et doit être revue pour fabrication.**
- Reliefs autour des pieds de cloison et des renforts de biscuits ; jeu de 0,2 mm à la jonction avant/arrière. Assise de CL-AR dégagée de 0,2 mm : contrôler le serrage et prévoir une cale si nécessaire.
- Rabats de capot vers l'intérieur pour conserver 446 mm de largeur ; un rabat extérieur aurait dépassé l'ouverture du rack.
- Pattes de liaison latérales prolongeant les quadrants avant à 220 mm ; leur volume reste imprimable.
- Parois ventilateurs dégagées des pattes, biscuits et capots : hauteur finale 164,9 mm.
- Poignées séparées, vissées ; façades épaissies localement derrière leurs fixations.
- Tiroir gauche copié par translation, pour ne pas inverser le motif Mini-ITX réel. Sa façade conserve des trous supplémentaires rapprochés aux fixations de tiroir : nettoyer ce détail dans la prochaine révision.

## Réserves avant fabrication définitive

1. **PSU : les huit perçages UNC 6-32 ne sont pas réalisés**, faute de relevé réel. Ouverture arrière, berceau et sangle seulement. Dimensions 150 × 140 × 86 à confirmer.
2. **Carte TP2.5 :** motif de fixation repris du prompt, non validé sur plan mécanique officiel orienté face avant. Bord de carte à Y = 16, façade à Y = 0 : contrôler la portée réelle des connecteurs et le besoin d'un panneau I/O avancé ou de rallonges.
3. **SSD :** fenêtre 150 × 120 provisoire ; couverture des quatre M.2 non certifiée.
4. **BMC RESET :** aucun trou fictif ; position à relever.
5. **Dissipateurs :** enveloppe 45 mm retenue. Le fabricant annonce 18 mm pour le dissipateur RK1 seul, pas pour la pile connecteur + module + dissipateur montée sur la carte.
6. **Impression sans support non validée :** toutes les arêtes de plateau ne sont pas chanfreinées ; entrées de rail et toits à 45° non finalisés. Les cloisons avec pieds de chaque côté et les tiroirs nervurés nécessitent une étude des supports/orientations.
7. **Épaisseurs résiduelles :** un fond de tiroir de 3 mm avec poche M3 de 2,6 mm ne laisse que 0,4 mm ; plusieurs logements M4 et bords de fixation doivent être renforcés. Ne pas assimiler une intersection nulle à une validation de résistance.
8. Le motif de ventilation arrière supérieur est rectangulaire, pas un découpage circulaire Ø130 strict. L'aération de façade est constituée de bandes autour de la poignée et du bouton.
9. Résistance des oreilles PETG, charge du châssis, vibrations, températures et refroidissement en charge : non testés. Aucun calcul structurel ni essai physique réalisé.

## Livrables et vérification visuelle

- Document SolidCraft avec historique et paramètres.
- STEP assemblé avec et sans REF, et STEP de chaque pièce.
- 3MF individuels orientés, plus le lot 20 + 2.
- Captures iso, avant, dessus, arrière, vue ouverte avec REF, et iso de chaque pièce dans previews/.
- BOM.md et README.md pour reprise.

La réparation/audit des maillages est détaillée dans verification/3mf-audit.json et, le cas échéant, verification/mesh-repair.json. Toute correction de triangulation est distincte du modèle paramétrique.

## Audit final des 3MF

**23 fichiers vérifiés, aucun échec** : géométries sur Z = 0, dans 240 × 240 × 210 mm, chaque arête de maillage partagée par exactement deux triangles. Le lot de biscuits contient 22 objets.

Les exports directs de Q-AV-D, Q-AV-G et Q-AR-D présentaient des arêtes non-manifold. Une réparation automatique de fermeture a été rejetée car elle modifiait fortement la géométrie. Ces trois pièces ont été **retriangulées depuis leurs STEP SolidCraft avec Gmsh/OCC**, sans modifier le document CAO ni les STEP. Maillages fermés, orientation cohérente ; écart de volume maximal au modèle SolidCraft : **0,000295 %** ; encombrements inchangés à la précision numérique.

Les trois exports bruts défectueux sont conservés uniquement dans verification/original-3mf/ pour traçabilité ; **ne pas les imprimer**. Les versions contrôlées sont dans exports/3mf/ et dans exports/RackTuringPi2_3MF.zip. Scripts reproductibles : verification/remesh_step.py et verification/audit_3mf.py.

Ce succès de triangulation ne lève pas les réserves de conception, les épaisseurs trop faibles ni les besoins de supports décrits ci-dessus.
