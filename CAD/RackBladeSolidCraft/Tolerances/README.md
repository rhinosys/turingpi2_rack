# Planche de tolérances — rack R3

Fichier à ouvrir dans Bambu Studio : **Rack_Tolerance_PETG_R1.3mf**. Géométrie uniquement, sans profil machine ni filament intégré. Ensemble déjà orienté : **210 × 226 × 14 mm**, 11 objets séparés. Le boîtier du rack reste inchangé.

## Architecture et composants

Une planche principale de 210 × 150 × 6 mm, cinq blocs de rainures, deux biscuits, une languette et deux barrettes d'écrous verticaux. Les cotes de référence proviennent des paramètres du modèle SolidCraft R3 ; ce sont des dimensions CAO, pas des mesures promises après impression.

| Repère gravé | Essai | Variantes, mm | Référence rack |
|---|---|---|---|
| M3 | Hexagone sur plats, profondeur 2,6 | 5,6 / 5,7 / 5,8 / 5,9 / 6,0 | 5,8 |
| M4 | Hexagone sur plats, profondeur 3,4 | 7,1 / 7,2 / 7,3 / 7,4 / 7,5 | 7,3 |
| D3 | Diamètre de passage de vis | 3,2 / 3,3 / 3,4 / 3,5 / 3,6 | 3,4 |
| D4 | Diamètre de passage de vis | 4,3 / 4,4 / 4,5 / 4,6 / 4,7 | 4,5 |
| J0.1 à J0.5 | Jeu total en longueur ET largeur autour du biscuit | 0,1 / 0,2 / 0,3 / 0,4 / 0,5 | J0.2 |
| P3.0 / P3.2 / P3.4 | Profondeur de poche, plan fixe 22 × 20 | 3,0 / 3,2 / 3,4 | P3.2 |
| X 0.2 | Poche centrale 22 × 22, profondeur 3,2 | Biscuit carré 21,8 × 21,8 × 3 | Jeu total 0,2 |
| Blocs 3.1 à 3.5 | Hauteur de rainure, profondeur fixe 3 | 3,1 / 3,2 / 3,3 / 3,4 / 3,5 | 3,4 |
| FOND 1 | Alvéole hexagonale de 14 sur plats | Fond continu de 1 | Peau R3 |

**J est le jeu total, pas le jeu par côté.** Exemple J0.2 : biscuit 21,8 × 19,8 dans poche 22 × 20, soit 0,1 par côté si centré. Toutes les poches J ont une profondeur de 3,2 mm. Les trous sous les neuf poches permettent d'éjecter les biscuits avec une tige.

Les deux barrettes isolées reproduisent les logements M3 et M4 sur une face verticale, pointe de l'hexagone en haut. Elles portent les mêmes valeurs sur plats que les lignes de la planche. Leurs trous traversants permettent de pousser un écrou coincé.

La languette isolée a une saillie de 2,9 mm et une épaisseur de 3 mm. Engager son extrémité dans les rainures par leur bout et faire coulisser sur 25 mm. Les blocs testent le jeu vertical : 0,1 à 0,5 mm total, soit 0,05 à 0,25 mm par face si centré. Le rack utilise 0,4 mm total. Cet échantillon ne valide pas le parallélisme de deux rails sur toute la longueur du tiroir.

## Modèle et fichiers

- `.solidcraft` : modèle modifiable créé avec le MCP SolidCraft.
- `.3mf` : disposition de tous les objets pour impression ; couleurs d'aperçu uniquement, utiliser un seul filament.
- `.stl` : alternative avec plusieurs coques dans un fichier.
- `.step` : géométrie exacte pour reprise CAO.
- `Tolerance_top.png` et `Tolerance_iso.png` : repérage des pièces.
- `resultats.csv` : relevé des ajustements.
- `verification/` : commandes de construction, mesures, contrôles de volume et de maillage.

## Comment imprimer et tester

1. Utiliser le même PETG, la même buse, hauteur de couche et les mêmes réglages de compensation que pour le rack. Conserver l'orientation fournie. Si le profil final n'est pas encore fixé, choisir un profil puis le conserver pendant les essais.
2. Imprimer par couches, tous les objets ensemble, en un seul matériau. Ne pas activer l'impression séquentielle par objet dans cette disposition rapprochée. Ne pas redimensionner. Vérifier l'aperçu de tranchage, notamment les petits ponts des rainures et les poches verticales ; ne pas remplir ces logements de supports.
3. Laisser refroidir. Enlever uniquement fils et bavures libres ; ne pas limer les surfaces d'ajustement avant de les évaluer. Contrôler aussi le pied d'éléphant des biscuits.
4. Essayer les vrais écrous et vis destinés au rack. Commencer par le logement le plus grand. Retenir un écrou qui entre sans fissurer le plastique et ne tourne pas au serrage. Comparer séparément les versions à plat et verticales.
5. Tester le biscuit rectangulaire dans J0.5 puis descendre. Retenir un montage manuel, ferme et démontable. Vérifier ensuite son affleurement dans les poches P. Utiliser le biscuit carré pour X.
6. Tester la languette dans 3.5 puis descendre : chercher un coulissement régulier sans coincement. Ne pas confondre le marquage de hauteur avec le jeu.
7. Vérifier la continuité imprimée du fond de 1 mm à contre-jour ; cet essai ne prouve pas l'étanchéité à l'air.
8. Noter les résultats et les réglages dans resultats.csv. Transmettre les valeurs retenues pour adapter les paramètres du rack.

## Vérifications et limites

Historique reconstruit sans erreur. Volumes avant gravure comparés aux formules géométriques (écart maximal inférieur à 0,001 %). Les 11 maillages 3MF sont fermés, orientés de façon cohérente et posés sur Z = 0. Leur volume total diffère de 0,0143 % de la CAO exacte, du fait de la triangulation des courbes ; seuil de contrôle : 0,02 %. Les valeurs ne sont validées pour l'imprimante qu'après impression et essai réels. La planche teste les ajustements, pas la résistance du rack ni les épaisseurs résiduelles sous ses logements d'écrous.

TODO(agent): reporter les choix mesurés dans le rack après retour utilisateur, sans changer globalement les cotes à partir d'un seul essai d'orientation différente.
