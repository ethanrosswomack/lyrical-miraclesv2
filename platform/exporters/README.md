# Exporters

Add one adapter per downstream surface. Each script should accept the unified
manifest (`dist/manifest.json`) and push the appropriate subset:

- `wordpress.py` — creates/updates pages via WP REST API.
- `ghost.ts` — uses the Ghost Admin API for long-form posts.
- `drupal.js` — syncs nodes + media entities.
- `astro.ts` or `nextjs.ts` — emits Markdown/JSON for static builds.

Keep secrets out of the repo (use `.env`, Workers Secrets, or CI vaults).
