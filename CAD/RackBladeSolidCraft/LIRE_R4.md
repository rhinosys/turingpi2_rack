# Rack complet R4 — 25 octobre 2026

Ouvrir **RackTuringPi2_Complet_R4.solidcraft** dans SolidCraft.

Ce fichier natif rassemble l'assemblage complet, dans sa position de montage, avec l'historique de construction et les paramètres. Il reprend exactement le fichier de la variante validée `Variants/Q-AV-G-EAR/Rack_variante_oreille_G.solidcraft` sous un nom explicite à la racine du dossier CAO. Le R3 original est conservé.

## Modifications incluses
- Hexagones d'allègement extérieurs avec fonds continus de 1 mm (`air_skin_t = 1`).
- Quadrant avant gauche et oreille gauche réunis dans Q-AV-G-EAR, anciennes fixations entre ces deux pièces rebouchées, appui avant prolongé.
- Capots démontables, notamment TOP-AV-G.
- Cloisons CL-AV et CL-AR ; CL-AV comporte les deux rainures intérieures de guidage des tiroirs.
- Deux tiroirs, façades, poignées, supports de ventilateurs, biscuits et autres éléments du modèle.

Les enveloppes de référence des cartes, RK1, SSD, alimentations et ventilateurs restent présentes mais masquées par défaut. Les réafficher dans l'arborescence si nécessaire. L'oreille droite reste séparée : la fusion autorisée concernait le côté gauche.

## Vérification et limites
Le contrôle de collision de cette géométrie comporte 49 corps, aucune collision et aucune paire non vérifiée : `Variants/Q-AV-G-EAR/verification-interferences.json`. Le fichier complet est enregistré avant la rotation de la pièce gauche pour l'impression.

Ce fichier ne constitue pas une validation de fabrication : jeux PETG, entrées chanfreinées des rails, course complète des tiroirs, supports d'impression et interfaces matérielles provisoires restent à valider. Voir les rapports R1/R3 et la notice. Aucune impression n'est lancée.

Rechargement et recalcul CLI effectués : 49 corps, 505 opérations, aucune erreur. Résultat : `verification/evaluation-complet-r4.json`.
