[Lire en français](../fr/files.md)

# CAD sources and printing files

## Current downloads

- [Rack V7 native / natif](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/RackTuringPi2_Complet_V7.solidcraft)
- [V7 STEP assembly / assemblage](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/V7/exports/Assemblage_V7.step)
- [V7 Bambu plates / plateaux](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/V7/plateaux)
- [V7 individual geometry / géométries](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/V7/exports)
- [Rail R3 native / natif rails](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/Supports_Rails_L/R3/Supports_Rails_L_PETG_R3.solidcraft)
- [R3 rear pair / deux arrière](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/Supports_Rails_L/R3/Plateau_2_arriere_M4_R3_PETG_noir.3mf)
- [R3 all four / quatre supports](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/Supports_Rails_L/R3/Plateau_4_supports_R3_PETG_noir.3mf)
- [Tolerance coupon / planche de tolérances](https://github.com/rhinosys/turingpi2_rack/blob/main/CAD/RackBladeSolidCraft/Tolerances/Rack_Tolerance_PETG_R1.solidcraft)

Download a file with GitHub's **Download raw file** control; do not save the HTML preview as a CAD file. Clone the repository to obtain all sources together:

```sh
git clone https://github.com/rhinosys/turingpi2_rack.git
```

## File types and source of truth

- **.solidcraft**: editable native model and feature history. Calibrated V7 is the current rack; R3 is the current rail support set.
- **.step**: neutral solids for exchange and checking; not the native feature history.
- **exports/*.3mf**: oriented geometry, without a complete printer project.
- **V7/plateaux/*.3mf** and the named R3 plate files: Bambu projects with process, arrangement and sliced output. Recheck the target printer and filament before sending.
- **Python and command JSON**: construction/calibration/export traces; many describe incremental operations on a specific older native file, not a one-command full rebuild.
- **verification/**: retained JSON evidence, including intermediate failures. Use the version README to identify final reports.

## Repository layout

```text
CAD/RackBladeSolidCraft/
  RackTuringPi2_Complet_V7.solidcraft
  V7/exports/                 # calibrated geometry
  V7/plateaux/                # printing projects
  V7/calibration/             # measured-fit update and evidence
  Supports_Rails_L/R3/        # current rail saddles
  Tolerances/                # initial coupon
  V5/, V6/, Variants/         # historical work
  verification/              # construction history
  notice-visuelle/            # historical illustrated guide
  animation-guidage/         # historical movement demonstration
docs/en/, docs/fr/           # current bilingual guide
source-manifest.json        # SHA-256 inventory at publication
```

Older native files and French working notes are retained as historical engineering sources. The current user guide is translated in both languages. Raw G-code duplicates, generated ZIP bundles, temporary slicing geometry and backup duplicates were omitted. Packaged 3MF projects retain their sliced data. Some old archive links in historical working notes refer to intentionally omitted bundles; use this download index instead.

## Rebuilding

Open the supplied native model in SolidCraft and recalculate before exporting. Rail R3 `build.py` creates an isolated headless MCP model; `prepare_plate.py` uses the macOS Bambu Studio CLI and the shared V7 PETG profile. Mesh tools require Gmsh, NumPy and trimesh; previews require Pillow. Tool paths in historical scripts may need adaptation to your installation. Read the [maintenance guide](maintenance.md) before running mutating scripts.
