[Read in English](../en/index.md)

# Un châssis imprimable avec deux blades complets extractibles

Ce projet développe un boîtier 19 pouces, 4U, pour deux cartes Turing Pi 2.5 et deux alimentations ATX. Chaque carte est destinée à recevoir des modules RK1 avec leurs dissipateurs et ventilateurs. Les équipements représentés en CAO sont des enveloppes simplifiées ; les dégagements définitifs restent à mesurer.

Le châssis fixe assure la structure, le guidage et le chemin d’air. Chaque cassette amovible emporte sa façade, son plateau de carte, son ventilateur, son alimentation et sa paroi arrière. **Éteindre et débrancher les câbles externes avant extraction.** Aucun fond de panier à connexion automatique ni mécanisme de remplacement à chaud n’est prévu.

![Cassette V7 avec ses murets](../assets/cassette-v7.png)

## Pour commencer

1. Lire l’[architecture et les pièces](architecture.md).
2. Choisir les [fichiers calibrés](files.md), puis suivre le [guide d’impression](printing.md).
3. Construire un premier node avec la [notice de montage illustrée](assembly.md).
4. Installer les [supports de rails R3](rails.md).
5. Consulter les [essais et validations restantes](validation.md) avant de considérer le prototype comme terminé.

## État actuel

| Élément | État |
|---|---|
| Rack V7 | CAO native, STEP, géométries et projets Bambu tranchés disponibles |
| Ajustements mesurés | J0.2, X0.2, trous M3/M4 et logements d’écrous ajustés sans retouche selon les essais |
| Rail arrière R3 | Axe déplacé de 30 à 35 mm ; géométrie et tranchage contrôlés ; essai physique à venir |
| Rack complet chargé | Résistance mécanique, fluage du PETG à chaud et comportement thermique non qualifiés |

Les couleurs CAO servent au repérage. Les fichiers de production utilisent **un seul PETG noir**. La [chronologie](timeline.md) retrace le projet ; le [prompt initial](prompt.md) est historique et ne constitue pas la spécification de fabrication actuelle.
