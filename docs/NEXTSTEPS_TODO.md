oh that’s a great checkpoint moment — you’ve got the core of the archive *and* a public repo that finally feels alive. nice work.

here’s a drop-in **`NEXT_STEPS_TODO.md`** you can add at the root of `lyrical-miracles/`.
it’s formatted in plain markdown so you can check boxes as you go or feed it to Notion/Joplin later.

---

# EverLight / Lyrical-Miracles — TODO Roadmap

A working sequence for finishing the archive, syncing music releases, and deploying the full EverLight stack.

---

## 🧾 Phase 1 — Proofing and Curation

* [ ] Review every notebook in `HAWK-ARS/notebooks/`
* [ ] Proofread and edit each lyric file (`.md`, `.html`, `.ipynb`)
* [ ] Fill in missing singles (titles, metadata, cover art)
* [ ] Finish formatting **Shadow Banned** and **Malicious**
* [ ] Standardize filenames → all lowercase, dash-separated slugs
  e.g. `reincarnated-2-resist.md`
* [ ] Verify every image in `HAWK-ARS/images/` renders correctly on GitHub
* [ ] Verify every audio file in `HAWK-ARS/audio/` plays/downloads

---

## 🎶 Phase 2 — Lyrics ↔ Music Sync

* [ ] Update **DistroKid** lyric entries for all released tracks
* [ ] Cross-check song lengths, capitalization, and metadata
* [ ] Add missing release dates and ISRC codes to `HAWK_Eye_Music.csv`
* [ ] Embed updated streaming links in lyric markdown headers
* [ ] Export a fresh `lyrics_manifest.json` once all metadata is verified

---

## 🌐 Phase 3 — Site Rebuild (Arsenal Project)

Goal: use this repo as the content source for
[`https://arsenal.reincarnated2resist.com`](https://arsenal.reincarnated2resist.com)

* [ ] Generate new static pages from `lyrics_manifest.json`
* [ ] Rebuild homepage and album navigation
* [ ] Add **track player** + **lyrics overlay** UI
* [ ] Integrate cover art from `HAWK-ARS/images/`
* [ ] Link merch / store data from `HAWK-ARS/data/printful_products.csv`
* [ ] Stage preview locally (Jekyll, Astro, or Next.js)
* [ ] Deploy build output → Cloudflare R2 bucket `lyrics-hawk-ars`
* [ ] Attach domain and enable HTTPS

---

## ⚡ Phase 4 — Cloudflare and AutoRAG

* [ ] Create / verify Vectorize index `lyrical-miracles`
* [ ] Upload embeddings (`ingest_batch.json`)
* [ ] Test `/search` endpoint with sample queries
* [ ] Add chat widget to lyric pages
* [ ] Configure automatic rebuild + ingest on repo push
* [ ] Document the full process in `EverLights_autorag_guidebook.md`

---

## 🧱 Phase 5 — Polish and Docs

* [ ] Update top-level `README.md` (Hawk’s Nest + navigation)
* [ ] Add screenshots of site + index examples
* [ ] Write a one-pager: *How to add new tracks*
* [ ] Tag repo v1.0.0 (`git tag -a v1.0.0 -m "First full archive build"`)
* [ ] Mirror to Bitbucket and back up to R2 Vault
* [ ] Announce milestone across platforms

---

## 🧭 Phase 6 — Stretch Goals

* [ ] Integrate merch / store sync automation (Stripe + Printful)
* [ ] Add streaming-API hooks (Spotify, Apple Music)
* [ ] Train small local embedding model for offline lyric search
* [ ] Build an “EverLight Dashboard” notebook summarizing analytics
* [ ] Launch **Omniversal Media Portal** page linking all properties

---

### 💡 Notes

* Keep commit messages atomic: *“proofread Illuminati.md”*, *“add manifest update”*
* Re-run the manifest + site build scripts after every major edit.
* When in doubt, **push to GitHub first, mirror to Bitbucket second**.

---

want me to export this as a ready-to-download `.md` file for you now?
