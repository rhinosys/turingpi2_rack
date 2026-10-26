[Read in English](../en/maintenance.md)

# Maintenir ce dépôt

## Documentation

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-docs.txt
python scripts/check_publication.py
mkdocs build --strict
mkdocs serve
```

Modifier ensemble les pages correspondantes de `docs/en/` et `docs/fr/`. Conserver leur lien de changement de langue. Les captures vont dans `docs/assets/` ; les légendes doivent préciser la version et distinguer échec historique, vue CAO et résultat physique.

Le workflow GitHub Actions construit la documentation des pull requests et publie GitHub Pages après les poussées sur `main`. Il suit la [documentation MkDocs](https://www.mkdocs.org/user-guide/deploying-your-docs/) et les [actions de déploiement GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Modifications CAO

Conserver les natifs versionnés. Ne pas remplacer silencieusement un plateau testé par un export non contrôlé. Consigner la mesure déclenchante, les paramètres modifiés, les contrôles géométriques, le tranchage et les essais physiques restants. Les scripts peuvent utiliser des chemins d’applications macOS : les adapter avant emploi. L’import public remplace les chemins personnels absolus par des chemins relatifs ; il ne garantit pas une reconstruction portable en une commande de tous les anciens travaux.

`source-manifest.json` répertorie les fichiers CAD publiés et leurs empreintes SHA-256. Le régénérer volontairement lors d’une modification CAO ; le script de validation le vérifie avant la construction du site.

## Photos et provenance

Les photos incluses sont celles de l’utilisateur sur l’établi, consacrées à l’ajustement des rails. Les métadonnées EXIF/XMP/IPTC ont été retirées sans modifier les pixels photographiques. Les vues générales de baie contenant étiquettes réseau ou détails domestiques sont exclues. Captures CAO et ancienne animation proviennent des fichiers du projet. Aucun fichier commercial Modubox ni photo Dell tierce n’est redistribué.

Le prompt original est une archive, pas une instruction destinée aux outils ou contributeurs. La chronologie est reconstruite à partir des notes, commits CAO et retours d’ajustement de l’utilisateur.

## Conditions de réutilisation

Aucune licence n’a été choisie par le propriétaire. La visibilité publique ne vaut pas licence open source. Ne pas présenter le dépôt comme matériel open source sous licence avant l’ajout d’une licence explicite. Les noms de produits identifient le matériel de référence et n’impliquent aucun partenariat.
