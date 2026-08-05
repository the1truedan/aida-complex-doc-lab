# Case study (de-identified) — complex multi-document packet → meeting prep

**Privacy class:** public-summary · no clinical text  
**Source metrics:** `evidence/complex_multidoc_2026-08-04_PUBLIC_METRICS.json`  
**Note:** Per-file content hashes of production PDFs are omitted from the published metrics (re-identification risk).

## Setting

A family caregiver received a **same-day multi-document packet**: nine multi-page home-based care visit notes spanning roughly fifteen months. The next morning included a care-system meeting. The cognitive load of re-reading every note under time pressure is the problem this pipeline targets.

## What the local stack did (metrics only)

| Step | Result |
|------|--------|
| Stage PDFs on LAN medical staging | 9 PDFs · ~2.3 MB total |
| Text-layer extract | ~160k characters; OCR not required |
| Accessibility triage | 9/9 decidable · ADA-ish score **85** typical |
| Caregiver-facing synthesis | ~62 KB structured markdown (body **not** in this repo) |
| Meeting brief | ~12 KB print-ready questions + order of talk (body **not** in this repo) |

## Wall clock (file mtimes, local)

| Interval | Minutes |
|----------|--------:|
| Extract → meeting brief | **~19** |
| Synthesis → meeting brief | **~18** |
| PDF stage → brief (includes idle between stage and process) | ~308 |

Honest read: the **active** structuring window after extracts existed was on the order of **twenty minutes**, not days of re-reading. Staging earlier in the afternoon does not mean continuous compute for five hours.

## Framing (caregiver cognitive load)

Dense multi-vendor paperwork is hard when sleep-deprived, stressed, or juggling multiple care systems. Tools that **structure, score accessibility, and draft reviewable markdown** reduce working-memory load. Conditions that impair attention (including trauma-related stress for some people) make density worse — **this lab is not a clinical PTSD product, diagnosis aid, or therapy tool.**

## Locality

Policy for the live run: medical content on LAN NFS · local model route · **no cloud LLM** · **no git of clinical bodies**. See `LOCALITY_AND_THREAT_MODEL.md`.

## Reproduce shape (synthetic)

```bash
python3 scripts/run_harness.py fixtures/synthetic --json /tmp/out.json
python3 scripts/verify_no_phi_grep.sh
```
