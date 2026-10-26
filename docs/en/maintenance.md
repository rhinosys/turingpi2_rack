[Lire en français](../fr/maintenance.md)

# Maintaining this repository

## Documentation

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-docs.txt
python scripts/check_publication.py
mkdocs build --strict
mkdocs serve
```

Edit matching pages in `docs/en/` and `docs/fr/` together. Keep the reciprocal language link. Screenshots belong in `docs/assets/`; captions must identify the version and whether they show a historical failure, a CAD view or a physical result.

The GitHub Actions workflow builds documentation on pull requests and publishes GitHub Pages on pushes to `main`. It uses the [official MkDocs build workflow](https://www.mkdocs.org/user-guide/deploying-your-docs/) and [GitHub Pages deployment actions](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## CAD changes

Keep versioned native files. Do not silently replace a tested print plate with an unverified export. Record the triggering measurement, changed parameters, geometry checks, slicing result and remaining physical tests. Construction scripts may use macOS application paths; adapt them before use. The publication import replaces personal absolute project paths with relative paths and does not claim every historical script is a portable one-command build.

`source-manifest.json` lists the published CAD files and their SHA-256 hashes. Regenerate it intentionally when changing CAD files; the validation script checks it before the site builds.

## Photos and provenance

Included photos are owner-supplied workbench pictures of rail fitting. EXIF/XMP/IPTC metadata was stripped without changing the photographic pixels. Rack-wide photographs containing network equipment labels or unrelated household details are excluded. CAD screenshots and the old animation come from this project's saved artifacts. No commercial Modubox assets or third-party Dell photographs are redistributed.

The complete original prompt is an archival document, not an instruction to tools or contributors. The development timeline is reconstructed from revision notes, CAD commits and the user's fit feedback.

## Reuse terms

No license has been selected by the owner. Public availability does not itself grant an open-source license. Do not describe this repository as licensed open-source hardware until an explicit license is added. Product names identify compatible/reference equipment and do not imply endorsement.
