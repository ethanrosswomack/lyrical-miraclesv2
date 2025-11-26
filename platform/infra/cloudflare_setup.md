# Cloudflare Deployment Plan

## 1. R2 Bucket
```bash
wrangler r2 bucket create lyrical-miracles
wrangler r2 object put lyrical-miracles/audio/demo --file media/audio/raw/<file>
```
- Use `dist/asset_map.json` to map local files → object keys.
- Store metadata: `--metadata release=... --metadata track=...`.

## 2. D1 (or Postgres)
```bash
wrangler d1 create lyrical_miracles
wrangler d1 execute lyrical_miracles --file platform/infra/sql/schema.sql
```
- Schema should include tables: releases, tracks, media_assets, articles, merch_products.
- Load `dist/manifest.parquet` (or JSON) via a lightweight ingest script.

## 3. Workers API
- Build a Worker (TypeScript) that exposes `/tracks`, `/releases`, `/search`.
- Worker reads from D1 and creates signed URLs for R2 objects.

## 4. Vectorize / Workers AI
```bash
wrangler vectorize create lyrical-miracles
```
- Use `scripts/autorag/ingest.py` to add embeddings for lyrics + essays.

> NOTE: Actual provisioning requires network access + Cloudflare credentials, which are not available inside this sandbox. Run these commands locally once ready.
