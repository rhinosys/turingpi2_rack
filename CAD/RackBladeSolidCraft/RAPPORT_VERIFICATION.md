# Vérification R3 — hexagones avec fond de 1 mm

25 octobre 2026. Correction réalisée avec le MCP SolidCraft. Les hexagones extérieurs sont rétablis comme poches non traversantes. Rapports R1 et R2 conservés pour historique.

## Architecture et composants

Entrée en façade → Turing Pi 2.5 / RK1 → ventilateurs centraux soufflant vers l’arrière → compartiments des alimentations → sorties arrière.

- Côtés et planchers de 4 mm : poches profondes de 3 mm, fond intérieur continu de 1 mm.
- Capots de 3 mm : poches profondes de 2 mm, fond intérieur continu de 1 mm.
- Grilles avant et arrière traversantes conservées.
- Huit pièces modifiées : quatre quadrants et quatre capots ; douze fonctions de coupe/motif réactivées. Les pièces gauches suivent les miroirs.
- Paramètre SolidCraft air_skin_t = 1 mm pour les fonds.

Les alimentations aspirent l’air intérieur au-dessus de leur ventilateur. Dégagement nominal au capot : 77,5 mm, au moins 75,5 mm sous les renforts. Jointoyer les coutures et capots et traiter les passages de câbles à l’assemblage. Les jeux fonctionnels et fixations peuvent laisser passer de l’air : aucune étanchéité absolue n’est revendiquée.

## Vérifications

- Reconstruction sans erreur ; aucune fonction supprimée de l’évaluation.
- Douze mesures entre fond de poche et face intérieure : 1 mm dans la précision numérique, sur quatre planchers, quatre côtés et quatre capots.
- 50 corps : aucune collision et aucune paire non vérifiée.
- Retrait simultané des tiroirs à 195 mm : aucune collision ; contrôle discret, pas une simulation continue.
- Dimensions conservées : châssis 446 × 424 × 176,5 mm ; oreilles 482,6 mm ; profondeur avec poignées 453 mm.
- 23 fichiers 3MF : arêtes fermées, posés sur Z = 0, contenus dans 240 × 240 × 210 mm.
- Q-AV-D, Q-AV-G et Q-AR-D retriangulés depuis les STEP avec Gmsh/OCC : maillages fermés, orientation cohérente, écart maximal de volume inférieur à 0,0004 %. Exports bruts dans verification/original-3mf/.
- Captures d’assemblage et des pièces actualisées.

## Mesures des pièces modifiées

| Pièce | Dimensions orientées pour impression, mm | Volume cm³ | PETG plein, g |
|---|---|---:|---:|
| Q-AV-D | 223.00 × 220.00 × 173.50 | 329.60 | 418.60 |
| Q-AR-D | 223.00 × 213.80 × 173.50 | 426.58 | 541.76 |
| Q-AV-G | 223.00 × 220.00 × 173.50 | 329.60 | 418.60 |
| Q-AR-G | 223.00 × 213.80 × 173.50 | 426.58 | 541.76 |
| TOP-AV-D | 223.00 × 210.00 × 18.00 | 136.61 | 173.49 |
| TOP-AR-D | 223.00 × 214.00 × 18.00 | 139.63 | 177.33 |
| TOP-AV-G | 223.00 × 210.00 × 18.00 | 136.61 | 173.49 |
| TOP-AR-G | 223.00 × 214.00 × 18.00 | 139.63 | 177.33 |

Masse de l’assemblage imprimé avec 16 biscuits standards et 2 centraux : **4248,5 g**, soit **302,2 g économisés** par rapport à R2. PETG à 1,27 g/cm³, matériau plein ; la masse tranchée dépend du remplissage et des supports.

## Fichiers et preuves

Natif SolidCraft, STEP, 3MF et archive complète actualisés. Données courantes dans verification/ : skin-thickness.json, airflow-change.json, measure-assembly.json, measure-print.json, interference.json, drawer-motion.json, 3mf-audit.json et mesh-repair.json. Contrôles antérieurs dans r1-2026-10-24/ et r2-2026-10-25/.

## Comment tester

1. Contrôler les fonds de 1 mm dans le trancheur et imprimer un échantillon.
2. Assembler avec joints, fermer les capots et vérifier le sens des ventilateurs.
3. Contrôler aspiration avant, rejet arrière et fuites aux jonctions.
4. Tester les huit RK1 en charge et surveiller leurs températures et celles des alimentations.

Aucune CFD ni validation thermique physique réalisée. Le débit réel dépend des ventilateurs, grilles et joints.

## Réserves maintenues

Prototype pour revue et essais d’ajustement. Restent à confirmer : trous UNC 6-32 des alimentations, interfaces I/O/NVMe et accès BMC RESET. Les faibles épaisseurs sous certaines poches d’écrous, nervures de tiroir, chanfreins et supports d’impression restent à finaliser. La résistance des oreilles PETG n’est pas qualifiée. Voir le rapport R1 pour les réserves détaillées.
