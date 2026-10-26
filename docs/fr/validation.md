[Read in English](../en/validation.md)

# Mesures, contrôles et essais restants

## Ajustements testés sur l’imprimante

| Interface | Valeur retenue |
|---|---:|
| Biscuit rectangulaire J | Jeu XY total de 0,2 mm |
| Biscuit central X | Jeu XY total de 0,2 mm |
| Passage M3 | Diamètre 3,2 mm |
| Passage M4 | Diamètre 4,3 mm |
| Écrou hexagonal M3 | 5,7 mm entre plats |
| Écrou hexagonal M4 | 7,2 mm entre plats |

Résultats déclarés en PETG HF noir, sans ponçage ni ébavurage. L’orientation des essais d’écrou n’a pas été précisée : on ne peut pas valider les deux orientations séparément. Ces mesures ne valident ni les guides, ni la profondeur des biscuits, ni le passage filament, ni la résistance de la jonction.

## Contrôles numériques

Les rapports conservés couvrent recalcul natif, dimensions, fermeture/orientation des maillages et positions d’extraction échantillonnées. La V7 a été contrôlée à des positions discrètes jusqu’à 430 mm, y compris avec chaque node indépendamment. Ce n’est pas une analyse continue du volume balayé ; câbles souples et certaines fixations réelles sont absents.

Les projets Bambu calibrés ont été tranchés sans objet ignoré ou hors plateau, avec un seul PETG noir. Les maillages corrigés ont été retriangulés depuis les STEP puis comparés aux volumes et enveloppes CAO. Le tunnel arrière gauche V7 comporte une correction numérique d’extrémité d’environ 0,005 mm uniquement sur le maillage ; natif et STEP restent inchangés.

La réparation du maillage arrière R3 reste sous 0,01 mm d’écart d’enveloppe et 0,02 % d’écart de volume. Les deux plateaux R3 passent les contrôles de maillage et profil. L’alignement physique à 35 mm reste à essayer.

## Prochains essais à documenter

| Essai | Résultat attendu | État |
|---|---|---|
| Ajustement R3 | Rail en butée ; M4 traversant le trou choisi sans forcer | À faire |
| Éprouvette filament | Insertion et retrait du filament réel sur toute la longueur | À faire |
| Cassette vide | Deux guides engagés, aucun blocage au raccord central | Résultat physique attendu |
| Cassette chargée | Pas d’ouverture du joint ni de flèche inacceptable ; cassette soutenue à la sortie | À faire |
| Châssis à chaud | Températures stables, absence de déformation PETG inacceptable | À faire |
| Électronique réelle | Retenue PSU, I/O, NVMe et refroidissement RK1 contrôlés | À faire |
| Flux d’air | Entrée avant, sortie arrière, raccords fixes fermés et baie vide obturée | À faire |

Consigner filament, machine, buse, plaque, profil, décalage mesuré, photos et éventuelles retouches. Mettre à jour l’état de validation uniquement après un résultat réel.
