# Notice visuelle 3D V2

Livrable : `../../../output/pdf/Notice_Rack_3D_V2.pdf` (16 pages A4 paysage).

Les PNG de ce dossier sont calculés depuis les triangles des 3MF R3, et non générés à partir d'une image. `build_notice.py` inverse les transformations d'export décrites dans `verification/r1-2026-10-24/measure-print.json`, mises à jour par `verification/print-changes.json`, puis applique des déplacements de présentation aux vues éclatées. Le modèle SolidCraft et les 3MF restent inchangés. La session MCP de cette reprise ne permettait pas l'ouverture du dossier du projet ; les exports locaux existants ont donc été utilisés sans modifier ses autorisations.

Turquoise : pièces de l'étape ; gris : assemblage précédent ; orange : rapprochement vers la position assemblée. Les vis, joints, ventilateurs et équipements ne sont pas modélisés dans ces nouvelles vues. Les quantités de vis proviennent de BOM.md ; les longueurs restent indicatives. La carte des biscuits est un schéma des positions nominales du cahier des charges, à comparer aux poches réelles après adaptation des tolérances.

La notice n'autorise pas la fabrication définitive des zones signalées comme provisoires : épaisseurs sous écrous, nervures de tiroirs, trous PSU et interfaces carte/SSD. Voir les rapports R1 et R3.

Reproduction : Python avec numpy, Pillow et reportlab. Exécuter `build_notice.py` depuis le dépôt ; il recrée les PNG et le PDF dans `output/pdf/`. Contrôle effectué par rendu de toutes les pages avec pdftoppm, planche-contact et inspection des pages de détail.
