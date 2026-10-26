# Turing Pi 2 Rack · SolidCraft CAD

**19-inch / 4U · Two complete removable blades · Black PETG**

[English documentation](https://rhinosys.github.io/turingpi2_rack/en/) · [Documentation française](https://rhinosys.github.io/turingpi2_rack/fr/)

![Integrated enclosure](docs/assets/enclosure-v6.png)

## English

A printable enclosure prototype for two Turing Pi 2.5 boards, RK1 cooling, two ATX supplies and two 120 mm fans. The fixed shell guides front-to-rear airflow; the complete nodes slide out after external cables are disconnected.

**Current:** calibrated rack **V7** and rail saddles **R3** (M4 locking hole 35 mm from the rail end). R3 physical fit and full loaded/thermal performance remain to be validated.

- [CAD and printing files](docs/en/files.md)
- [Printing guide](docs/en/printing.md) · [Illustrated assembly](docs/en/assembly.md)
- [Development timeline](docs/en/timeline.md) · [Initial prompt](docs/en/prompt.md)

## Français

Prototype de châssis imprimable pour deux Turing Pi 2.5, refroidissement RK1, deux alimentations ATX et deux ventilateurs 120 mm. Le châssis fixe guide le flux avant-arrière ; les nodes complets coulissent après débranchement des câbles externes.

**Versions actuelles : V7 calibrée et berceaux R3**, verrou M4 à 35 mm du bout du rail. Ajustement physique R3, charge complète et tenue thermique restent à valider.

- [Fichiers CAD et impression](docs/fr/files.md)
- [Guide d’impression](docs/fr/printing.md) · [Montage illustré](docs/fr/assembly.md)
- [Chronologie](docs/fr/timeline.md) · [Prompt initial](docs/fr/prompt.md)

## Build the docs / Construire la documentation

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-docs.txt
python scripts/check_publication.py
mkdocs build --strict
mkdocs serve
```

No license selected yet / Aucune licence choisie pour le moment. See [maintenance and provenance](docs/en/maintenance.md).
