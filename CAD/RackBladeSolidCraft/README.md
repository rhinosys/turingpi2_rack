# Rack Blade Turing Pi 2.5 — prototype CAO SolidCraft

Modèle construit via le MCP SolidCraft pour deux cartes Turing Pi 2.5 avec quatre RK1 et dissipateurs ventilés par carte. Révision R3 du 25 octobre 2026 : hexagones extérieurs d'allègement avec fond continu de 1 mm pour une ventilation de l'avant vers l'arrière.

**Statut : prototype dimensionnel, pas encore bon à imprimer pour montage définitif.** Les exports sont fournis pour revue et essais d'ajustement. Lire RAPPORT_VERIFICATION.md avant fabrication.

## Architecture
Deux baies, tiroirs extraits vers l'avant, deux alimentations arrière, deux ventilateurs centraux de 120 mm. Repère X largeur, Y profondeur vers l'arrière, Z hauteur. Châssis 446 × 424 × 176,5 mm ; oreilles 482,6 mm. Les poignées dépassent de 29 mm à l'avant.

Le modèle natif est l'autorité : RackTuringPi2_SolidCraft.solidcraft. Ouvrir ce fichier dans SolidCraft. Les STEP représentent la géométrie assemblée. Les 3MF sont des géométries orientées, sans profil de tranchage Bambu.

## Composants
L'air entre par les façades et sort à l'arrière. Les alimentations aspirent l'air intérieur au-dessus de leurs ventilateurs. Jointoyer les coutures et capots pour limiter les fuites ; le débit et les températures restent à tester en charge.

Quatre quadrants, deux cloisons, deux parois ventilateurs, quatre capots, deux tiroirs, deux façades, deux oreilles, deux poignées séparées et biscuits. Les volumes REF sont des enveloppes simplifiées, pas les CAO exactes des équipements.

## Modèle et paramètres
Les paramètres principaux sont accessibles dans SolidCraft (hauteur, largeur, profondeur, épaisseurs, alimentation, carte, jeu de rail, entretoises). Plusieurs positions et détails sont des cotes numériques fixes du cahier des charges ; changer arbitrairement les dimensions impose de recontrôler les interfaces. Les motifs hexagonaux utilisent une coupe répétée, au maximum 56 occurrences par motif.

verification/r1-2026-10-24/construction-batches.json est une trace de la construction initiale. verification/airflow-change.json décrit la correction R3 ; skin-thickness.json contient les douze mesures des fonds. Le paramètre air_skin_t pilote leur épaisseur. Le document natif contient l'historique complet.

## Comment tester
1. Lire les réserves du rapport, mesurer les alimentations, vérifier le plan TP2.5 et la zone NVMe.
2. Ouvrir le document natif ; contrôler les composants et afficher REF.
3. Vérifier les cotes/jeux après toute modification ; répéter inspect.interference.
4. Imprimer d'abord un échantillon rainure/langue et un logement d'écrou PETG avec les mêmes réglages.
5. Examiner chaque 3MF dans Bambu Studio : orientation, supports, ponts, écrous, épaisseurs et accessibilité des vis.
6. Valider mécaniquement sur établi avant montage dans le rack. Le modèle n'est pas accompagné d'un calcul de charge des oreilles PETG : prévoir un support sous le châssis pour les essais.

## Prochaines améliorations nécessaires
- TODO(agent): relever les quatre trous UNC 6-32 de chaque alimentation ; ils ne sont pas inventés dans cette version.
- TODO(agent): confirmer le plan de fixation Mini-ITX orienté I/O en façade, l'alignement des connecteurs et l'accès réel aux quatre SSD.
- TODO(agent): définir l'accès BMC RESET depuis la carte réelle ; pas de trou fictif.
- TODO(agent): généraliser les chanfreins anti pied d'éléphant, les entrées de rails et les toits à 45° ; vérifier toutes les parois après poches d'écrous.
- TODO(agent): étudier les épaisseurs résiduelles et la résistance du montage rack ; finaliser le routage et la retenue des câbles.
- TODO(agent): tester le refroidissement en charge avec huit RK1, deux ventilateurs centraux et les deux alimentations.

## Références
- Cahier des charges fourni : CAHIER_DES_CHARGES.txt.
- Carte 2.5 : https://turingpi.com/product/turing-pi-2-5/
- Dissipateur actif RK1 : https://turingpi.com/product/rk1-heatsink/ (hauteur annoncée 18 mm ; largeur contradictoire 42/45 mm dans la page).
- Montage : https://docs.turingpi.com/docs/mounting-heatsink
- Refroidissement : https://docs.turingpi.com/docs/turing-pi2-specs-and-io-ports-case-and-cooling
