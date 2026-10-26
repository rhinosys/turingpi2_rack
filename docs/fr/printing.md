[Read in English](../en/printing.md)

# Guide d’impression

## 1. Ouvrir les bons projets

Utiliser les fichiers **plateaux** V7 calibrés, ouverts comme projets dans Bambu Studio. Les fichiers **exports** ne contiennent que la géométrie. Les projets préparés ciblent une **X1 Carbon, buse 0,4 mm, plaque PEI lisse et PETG HF noir**. Choisir la bobine réellement chargée lors de l’envoi ; aucun emplacement AMS n’est imposé.

![Les onze plateaux V7](../assets/plates-v7.png)

## 2. Commencer par la jonction non qualifiée

Imprimer le plateau optionnel 11. L’éprouvette de filament possède quatre passages : une encoche = 1,9 mm, deux = 2,0 mm, trois = 2,1 mm, quatre = 2,2 mm. Tester l’insertion et le retrait du filament réel sur toute la longueur. Assembler ensuite les deux éprouvettes de jonction. Le passage par défaut de 2,1 mm n’a **pas** été validé par les premiers essais d’écrous et de biscuits.

![Éprouvette des passages de filament](../assets/coupon-filament.png)

## 3. Conserver les orientations fournies

- Tunnels : debout, ouverture du tunnel sur le plateau.
- Fonds de cassette : plancher à plat, murets et passages de filament verticaux.
- Façades : face avant sur le plateau.
- Berceaux arrière R3 : platine M6 sur le plateau ; les avant conservent l’orientation latérale fournie.

![Orientation verticale d’un tunnel](../assets/tunnel-vertical.png)

La V7 utilise des couches de 0,16 mm, une première couche de 0,2 mm, deux parois et 15 % de remplissage issus du procédé testé. Les supports varient selon le plateau ; les tunnels ont une bordure de 5 mm. Les plateaux de façades/biscuits n’ont pas de supports. Examiner les couches tranchées : les images d’aperçu ne montrent pas tous les supports générés. Dégager les interfaces sans modifier leur taille nominale.

Les supports de rails utilisent un autre procédé : couches de 0,20 mm, six parois, 40 % de remplissage gyroid et bordure de 5 mm, sans supports. Ne pas leur appliquer le profil du rack par erreur.

## 4. Imprimer progressivement

Après le plateau 11, imprimer 05 et 06 pour un premier node, essayer la jonction, puis son ajustement au châssis. Imprimer chaque plateau de production 01–10 une fois. Ne pas ajouter de compensation XY : J0.2 et X0.2 représentent un jeu XY **total**, pas un jeu par côté.

| Plateau | Contenu | Temps estimé | PETG |
|---|---|---:|---:|
| 01 | Q-AV-D | 17 h 04 | 481 g |
| 02 | Q-AV-G-EAR | 16 h 57 | 480 g |
| 03 | Q-AR-D | 16 h 07 | 534 g |
| 04 | Q-AR-G | 16 h 12 | 539 g |
| 05 | BT-D | 3 h 57 | 135 g |
| 06 | FOND-AR-D | 8 h 13 | 310 g |
| 07 | BT-G | 3 h 55 | 135 g |
| 08 | FOND-AR-G | 8 h 12 | 310 g |
| 09 | BF-D + HANDLE-D + 8 BIS + 1 BIS-X | 2 h 29 | 89 g |
| 10 | BF-G + HANDLE-G + 8 BIS + 1 BIS-X | 2 h 30 | 88 g |
| 11 | TEST-FILAMENT + TEST-JONCTION | 2 h 07 | 31 g |

Production estimée : environ **95 h 40 / 3,10 kg**, hors éprouvettes optionnelles et berceaux. Deux arrière R3 : **2 h 26 / 86 g**. Jeu complet R3 : **4 h 12 / 155 g**. Ce sont des estimations du trancheur, pas des durées mesurées.

Passer à la [notice de montage](assembly.md). La tenue sous charge et en température reste à qualifier ; le procédé testé à deux parois ne prouve pas la résistance d’un rack chargé.
