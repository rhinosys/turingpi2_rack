# Plateaux V7 calibrés — PETG HF noir

Un fichier 3MF par plateau, pour **Bambu X1 Carbon, buse 0,4 mm, plaque PEI lisse**. Tous les objets utilisent le même filament noir. Les quatre tunnels sont dressés verticalement, ouverture du tunnel sur le plateau. Les fonds de cassette reposent sur leur plancher ; les façades sont couchées face avant sur le plateau.

| Plateau | Contenu | Quantité |
|---|---|---:|
| 01 | Tunnel avant droit Q-AV-D | 1 |
| 02 | Tunnel avant gauche avec oreille Q-AV-G-EAR | 1 |
| 03 | Tunnel arrière droit Q-AR-D | 1 |
| 04 | Tunnel arrière gauche Q-AR-G | 1 |
| 05 | Fond avant du node droit BT-D | 1 |
| 06 | Fond arrière du node droit FOND-AR-D | 1 |
| 07 | Fond avant du node gauche BT-G | 1 |
| 08 | Fond arrière du node gauche FOND-AR-G | 1 |
| 09 | Façade droite + poignée + 8 BIS + 1 BIS-X | 11 objets |
| 10 | Façade gauche + poignée + 8 BIS + 1 BIS-X | 11 objets |
| 11 optionnel | Test de passage filament + deux moitiés de jonction | 3 objets |

Imprimer chaque plateau de production **une seule fois**. Total : 16 biscuits rectangulaires et 2 biscuits centraux. Les goupilles sont des morceaux de filament de 1,75 mm à couper, pas des objets à imprimer. Vis, écrous et composants électroniques ne sont pas inclus comme pièces imprimables.

## Réglages

Le profil reprend la planche de tolérances : couches 0,16 mm, première couche 0,2 mm, deux parois, 15 % de remplissage, aucune compensation XY additionnelle. Le PETG HF conserve ses températures et son débit du profil testé. Les réglages de supports et de bordure sont adaptés aux pièces : supports automatiques ajustés pour les tunnels, fonds et éprouvettes, ponts exclus des supports ; bordure extérieure de 5 mm sur les tunnels. Les plateaux de façades et biscuits n'ont pas de supports.

Les valeurs J0.2 et X0.2 sont des jeux **totaux**, pas des jeux par côté. Les passages de vis sont D3=3,2 et D4=4,3 mm ; les écrous M3/M4 ont des logements de 5,7/7,2 mm entre plats. Aucune compensation supplémentaire ne doit être ajoutée dans le trancheur.

## Ordre conseillé et contrôle

1. Imprimer le plateau optionnel 11 pour qualifier les doigts et le passage du filament, que la première planche n'a pas validés.
2. Faire les plateaux 05 et 06 pour un premier node ; contrôler la jonction et le coulissement avant de multiplier les pièces.
3. Imprimer les autres plateaux selon les besoins. Dans Bambu Studio, ouvrir chaque fichier comme **projet** pour conserver profil et placement. Sélectionner la bobine PETG HF noire réellement chargée lors de l'envoi.
4. Vérifier les supports dans l'aperçu des couches, puis les retirer soigneusement des interfaces. Les essais de tolérances initiaux étaient obtenus sans retouche ; les supports sont une opération distincte sur ces grandes pièces.
5. Tester progressivement le montage avec la charge réelle. Les deux parois du profil testé et les goupilles en filament ne constituent pas une qualification mécanique du rack complet.

Ces fichiers ne déclenchent aucune impression. Les câbles externes doivent être débranchés avant extraction d'un node. Les guides, le passage de filament de 2,1 mm et la tenue à chaud restent à valider physiquement.

`inventaire.json` donne les placements ; `verification/audit-plateaux.json` décrit les contrôles géométriques et les estimations de tranchage. Les PNG montrent les pièces, sans représenter les supports du G-code.

## Estimations de tranchage

Production complète : environ **95 h 40 et 3.10 kg** de PETG, supports et bordures compris selon Bambu Studio. Le plateau optionnel ajoute environ 2 h 07 et 31 g. Les temps réels peuvent varier.

| Plateau | Temps estimé | PETG |
|---|---:|---:|
| 01_Q-AV-D.3mf | 17 h 04 | 481 g |
| 02_Q-AV-G-EAR.3mf | 16 h 57 | 480 g |
| 03_Q-AR-D.3mf | 16 h 07 | 534 g |
| 04_Q-AR-G.3mf | 16 h 12 | 539 g |
| 05_BT-D.3mf | 3 h 57 | 135 g |
| 06_FOND-AR-D.3mf | 8 h 13 | 310 g |
| 07_BT-G.3mf | 3 h 55 | 135 g |
| 08_FOND-AR-G.3mf | 8 h 12 | 310 g |
| 09_Facade_D_poignee_biscuits.3mf | 2 h 29 | 89 g |
| 10_Facade_G_poignee_biscuits.3mf | 2 h 30 | 88 g |
| 11_OPTION_Test_filament_et_jonction.3mf | 2 h 07 | 31 g |

Les 11 projets ont été tranchés localement avec Bambu Studio 02.08.02.60. Aucun objet n’est ignoré ou hors plateau ; les empreintes de première couche incluent supports et bordures et laissent libre la zone de calibration avant. Le CLI émet un message de recherche de variante d’extrudeur ; il termine avec succès et les sorties contrôlées utilisent un seul PETG noir, avec la buse standard 0,4 mm. Les journaux sont conservés.
