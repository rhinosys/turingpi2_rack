# Vérification R2 — flux d'air avant → arrière

25 octobre 2026. Cette révision remplace la ventilation latérale, inférieure et supérieure de R1 conformément à la correction demandée. Le rapport initial est conservé dans RAPPORT_VERIFICATION_R1.md ; ses mesures historiques ne décrivent plus les huit panneaux modifiés.

## Architecture et modifications

Entrée par les façades → cartes Turing Pi 2.5 / RK1 → deux ventilateurs centraux soufflant vers l'arrière → compartiments d'alimentation → grilles et échappements arrière.

- Planchers des quatre quadrants pleins : aérations hexagonales supprimées.
- Parois latérales des quatre quadrants pleines : aérations hexagonales supprimées.
- Quatre capots pleins : aérations supprimées, y compris au-dessus des alimentations.
- Aérations des façades et de l'arrière conservées.
- Entretoises, rails, fixations, logements de biscuits et ouvertures internes des tiroirs/cloisons conservés. Les fenêtres NVMe des tiroirs ne débouchent plus sur l'extérieur, car le plancher inférieur est fermé.
- Douze fonctions de coupe/motif désactivées dans l'historique SolidCraft ; les pièces gauches suivent les miroirs. Aucun bouchon simplement posé devant les anciennes grilles.

Les alimentations restent ventilateur vers le haut et aspirent désormais l'air du compartiment intérieur. L'espace vertical au-dessus de leurs enveloppes vaut 77,5 mm jusqu'au capot nominal (au moins 75,5 mm sous les renforts de capot). Ce dégagement géométrique ne démontre pas une température de fonctionnement acceptable.

## Étanchéité d'assemblage

Les panneaux sont pleins hors perçages fonctionnels. Les logements de biscuits sont des poches non traversantes. Les jonctions de panneaux, jeux de tiroirs et trous de fixation peuvent toutefois laisser passer un peu d'air.

Prévoir des joints fins compressibles ou une bande d'étanchéité adaptés aux jeux existants sur les coutures et capots. Installer toute la visserie, obturer les passages inutilisés et jointoyer les passages de câbles autour des faisceaux pour limiter la recirculation interne. Les joints sont des consommables d'assemblage, non des pièces CAO ajoutées. **Une étanchéité absolue n'est pas revendiquée.**

## Vérifications effectuées

- Historique : aucune erreur après reconstruction ; douze fonctions volontairement désactivées.
- Interférences : 50 corps, 0 collision, 0 paire non vérifiée, aucun dépassement du budget.
- Retrait simultané des blades à 195 mm : 0 collision, aucune paire non vérifiée. Essai discret, pas une simulation continue du mouvement.
- Dimensions générales conservées : corps 446 × 424 × 176,5 mm ; largeur aux oreilles 482,6 mm ; profondeur totale avec poignées 453 mm.
- 23 fichiers 3MF : géométries fermées selon l'audit des arêtes, posées sur Z = 0 et contenues dans 240 × 240 × 210 mm.
- Trois exports (Q-AV-D, Q-AV-G, Q-AR-D) retriangulés depuis les STEP avec Gmsh/OCC : écart de volume maximal < 0,0004 % ; dimensions conservées. Les exports bruts sont archivés dans verification/original-3mf/ et ne doivent pas être imprimés.
- Contrôle visuel : iso, face, arrière, dessus, dessous et vue ouverte. L'arrière conserve ses grilles ; côtés, capots et planchers n'ont plus les anciennes aérations.

## Mesures des pièces modifiées

| Pièce | Orientation d'impression X × Y × Z, mm | Volume cm³ | PETG plein, g |
|---|---|---:|---:|
| Q-AV-D | 223.00 × 220.00 × 173.50 | 382.56 | 485.85 |
| Q-AR-D | 223.00 × 213.80 × 173.50 | 454.59 | 577.33 |
| Q-AV-G | 223.00 × 220.00 × 173.50 | 382.56 | 485.85 |
| Q-AR-G | 223.00 × 213.80 × 173.50 | 454.59 | 577.33 |
| TOP-AV-D | 223.00 × 210.00 × 18.00 | 155.62 | 197.64 |
| TOP-AR-D | 223.00 × 214.00 × 18.00 | 158.64 | 201.47 |
| TOP-AV-G | 223.00 × 210.00 × 18.00 | 155.62 | 197.64 |
| TOP-AR-G | 223.00 × 214.00 × 18.00 | 158.64 | 201.47 |

Masse calculée de l'assemblage imprimé avec 16 biscuits standards et 2 centraux : **4550.3 g**, soit **+419.1 g** de matière par rapport à R1. Densité 1,27 g/cm³ ; masse à matériau plein, hors remplissage réel et supports. Les quatre biscuits standards de réserve ajoutent 6,58 g.

## Exports et preuves

Le document natif, les deux STEP d'assemblage, les STEP/3MF des huit panneaux, les captures et l'archive exports/RackTuringPi2_3MF.zip sont mis à jour. Les autres pièces restent identiques.

Les données actuelles sont dans verification/ : airflow-change.json, measure-assembly.json, measure-print.json, interference.json, drawer-motion.json, 3mf-audit.json et mesh-repair.json. Les anciens contrôles sont regroupés dans verification/r1-2026-10-24/.

## Comment tester le flux réel

1. Assembler les panneaux et leurs joints, installer les alimentations et fermer les capots.
2. Vérifier le sens des deux ventilateurs centraux : soufflage vers l'arrière.
3. Contrôler l'aspiration en façade et le rejet arrière avec un indicateur léger ; rechercher les fuites aux jonctions.
4. Tester les huit RK1 en charge et surveiller leurs températures et celles des alimentations avec le capot fermé.
5. Ajuster vitesse des ventilateurs et surface libre de façade si nécessaire.

Aucune CFD, mesure de débit, de pression ni validation thermique réelle n'a été effectuée. La fermeture des panneaux impose le trajet extérieur prévu, mais le débit disponible dépendra des ventilateurs, grilles et joints.

## Réserves de fabrication maintenues

Le modèle reste un prototype. Les perçages UNC 6-32 des alimentations, l'implantation réelle I/O/NVMe et l'accès BMC RESET restent à confirmer. Les faibles épaisseurs sous certaines poches d'écrou et les nervures de tiroir, les chanfreins et les supports d'impression doivent toujours être finalisés. La résistance des oreilles PETG n'est pas qualifiée. Voir le rapport R1 pour le détail des réserves indépendantes du flux d'air.
