# AGENTS.md — aida-complex-doc-lab

**Visibility:** public (GitHub).  
**Class:** document accessibility + caregiver cognitive-load tooling **without PHI bodies**.

## Before any work

1. Read `docs/PHI_BOUNDARY.md` — clinical text never enters this repo.  
2. Prefer synthetic fixtures under `fixtures/synthetic/`.  
3. Do not filewalk medical NFS trees “for context.” Use `evidence/*PUBLIC*` metrics only.  
4. Session history UIs are an **index** — session IDs only, no bulk dumps of chat bodies.  
5. Real-token denylist (if any) lives only in gitignored `.phi_denylist.local` — never commit real names/IDs into `scripts/verify_no_phi_grep.sh`.

## Routing

- Code/tests: local Python; no network required for fixture harness.  
- Any real medical work stays on operator LAN staging with a local-only model route — not in this repo.

## Prepare-only

Scoring and synthesis helpers are **not** certification or clinical decision tools. A human signs off.

## Public siblings

- https://the1truedan.github.io/ai-gateway/  
- https://the1truedan.github.io/grok-tua-tok-tua/  
- https://the1truedan.github.io/johnny-appleseed-chipper/  
- https://the1truedan.github.io/aida-complex-doc-lab/  
