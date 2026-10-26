[Read in English](../en/files.md)

# Sources CAD et fichiers d’impression

## Téléchargements actuels

- [Rack V7 native / natif](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/RackTuringPi2_Complet_V7.solidcraft)
- [V7 STEP assembly / assemblage](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/V7/exports/Assemblage_V7.step)
- [V7 Bambu plates / plateaux](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/V7/plateaux)
- [V7 individual geometry / géométries](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/V7/exports)
- [Rail R3 native / natif rails](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/Supports_Rails_L/R3/Supports_Rails_L_PETG_R3.solidcraft)
- [R3 rear pair / deux arrière](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/Supports_Rails_L/R3/Plateau_2_arriere_M4_R3_PETG_noir.3mf)
- [R3 all four / quatre supports](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/Supports_Rails_L/R3/Plateau_4_supports_R3_PETG_noir.3mf)
- [Tolerance coupon / planche de tolérances](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/Tolerances/Rack_Tolerance_PETG_R1.solidcraft)

Utiliser **Download raw file** dans GitHub ; ne pas enregistrer la page HTML comme fichier CAO. Pour récupérer l’ensemble :

```sh
git clone https://github.com/rhinosys/turingpi2_rack.git
```

## Formats et fichiers de référence

- **.solidcraft** : modèle modifiable et historique d’opérations. V7 calibrée pour le rack, R3 pour les berceaux actuels.
- **.step** : solides neutres pour échange et contrôle, sans historique paramétrique natif.
- **exports/*.3mf** : géométries orientées, sans projet machine complet.
- **V7/plateaux/*.3mf** et plateaux R3 nommés : projets Bambu avec procédé, placement et tranchage. Vérifier machine et filament avant envoi.
- **Python et commandes JSON** : traces de construction/calibration/export ; souvent des opérations incrémentales sur un ancien natif précis, pas une reconstruction complète en une commande.
- **verification/** : preuves JSON conservées, y compris des échecs intermédiaires. Le README de chaque version indique les rapports finaux.

## Organisation

```text
CAD/RackBladeSolidCraft/
  RackTuringPi2_Complet_V7.solidcraft
  V7/exports/                 # géométries calibrées
  V7/plateaux/                # projets d’impression
  V7/calibration/             # calibration et preuves
  Supports_Rails_L/R3/        # berceaux actuels
  Tolerances/                # planche initiale
  V5/, V6/, Variants/         # travaux historiques
  verification/              # historique de construction
  notice-visuelle/            # ancienne notice illustrée
  animation-guidage/         # ancienne démonstration du mouvement
docs/en/, docs/fr/           # guide bilingue actuel
source-manifest.json        # inventaire SHA-256 à la publication
```

Les anciens natifs et notes françaises sont conservés comme sources d’ingénierie historiques. Le guide utilisateur actuel existe dans les deux langues. Les G-code en doublon, archives ZIP générées, géométries temporaires du trancheur et sauvegardes redondantes sont omis. Les projets 3MF conservent leurs données tranchées. Certains liens d’archives des anciennes notes visent des ZIP volontairement omis ; utiliser cet index.

## Reconstruction

Ouvrir le natif dans SolidCraft et recalculer avant export. `build.py` de R3 construit un modèle MCP isolé ; `prepare_plate.py` utilise le CLI macOS de Bambu Studio et le profil PETG partagé V7. Les outils de maillage nécessitent Gmsh, NumPy et trimesh ; les aperçus utilisent Pillow. Adapter les chemins des outils historiques à son installation. Lire le [guide de maintenance](maintenance.md) avant d’exécuter un script qui modifie des fichiers.
