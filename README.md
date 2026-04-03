# pxr-usd-api

Unofficial community-maintained reference for NVIDIA Omniverse Kit `pxr` Python APIs.

This repository contains an annotated mirror of the NVIDIA `pxr-usd-api` docs for Kit `110.0.0`, with progressively enriched Python signatures, return types, and notes validated from local Kit runtime behavior where possible.

This project is not affiliated with, endorsed by, or sponsored by NVIDIA. NVIDIA, Omniverse, and related marks are trademarks or registered trademarks of NVIDIA and their respective owners. Prefer the official NVIDIA documentation for canonical source material:

- [NVIDIA pxr Python docs](https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/latest/pxr.html)
- [OpenUSD C++ API docs](https://openusd.org/release/api/index.html)

## Online docs

After GitHub Pages is enabled for this repository, the docs entry page is:

- `docs/index.html`
- `docs/pxr.html`

Typical Pages URL:

- `https://jamefei-lab.github.io/pxr-usd-api/`

## Repo layout

- `docs/`: publishable static documentation site
- `patch_*.py`: local patch scripts used to enrich mirrored HTML pages
- `inspect_pxr_api.py`: local inspection helper
- `usd_*_enrichment_report.json`: validation notes gathered during enrichment

## Notes

- Function names and page structure follow NVIDIA's Python docs.
- Signatures and return values are enriched from local Kit `110.0.0` runtime checks wherever possible.
- When a detail could not be verified confidently, the docs are kept conservative.
