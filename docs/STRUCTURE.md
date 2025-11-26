# Repository Structure

| Path | Purpose |
| --- | --- |
| `content/articles` | Editorial essays, SEO briefs, front-matter originally in the v1 README. |
| `content/lyrics/releases/<release>` | Markdown/HTML/IPYNB lyric sources grouped per release (e.g., `HAWK-ARS-00`). |
| `content/notebooks` | Clean copies of Hawk Eye notebooks for creative/business ops. |
| `media/audio/raw` | Lossless masters + stems. This folder should mirror an R2 bucket path. |
| `media/images/raw` | Cover art, promo, zines. Also synced to R2. |
| `data/catalogs` | Canonical CSV/JSON exports (music catalog, merch, manifests, product feeds). |
| `data/reference` | Site navigation html, commentary md, notebooks, planning docs from the old repo. |
| `docs` | Living documentation (roadmaps, AutoRAG guide, this file). |
| `platform/exporters` | Scripts/adapters for WordPress, Ghost, Drupal, Shopify, etc. |
| `platform/infra` | Terraform / docker / MAAS plans pulled from *The Omniversal Aether*. |
| `platform/widgets` | UI components (lyrics player, merch embeds, Workers AI chat widget). |
| `scripts` | Automation entrypoints (`build_manifest.py`, `normalize_assets.py`, future ETL). |
| `dist` | Generated artifacts (manifest JSON/Parquet, ingestion batches, R2 upload maps). |

## Naming Conventions
- All files in `content/lyrics` follow `slug-case.md` with YAML front matter.  
- Audio/image filenames should match the lyric slug to keep IDs stable across DB/R2/CMS.  
- CSV headers use `snake_case` to match database schema for quick imports.  
- Generated assets never live outside `dist/`.
