# aida-complex-doc-lab

[![Version](https://img.shields.io/badge/version-0.2.0-8eb4ff.svg)](CHANGELOG.md)
[![Pages](https://img.shields.io/badge/pages-aida--complex--doc--lab-e8c27a.svg)](https://the1truedan.github.io/aida-complex-doc-lab/)

**Public** proof lab for an **ADA-ish, prepare-only** multi-document pipeline aimed at **caregiver cognitive load** — structure dense paperwork into reviewable markdown **without** shipping protected health information.

**Site:** [the1truedan.github.io/aida-complex-doc-lab](https://the1truedan.github.io/aida-complex-doc-lab/) ·
**Release:** [`v0.2.0`](CHANGELOG.md)

| | |
|--|--|
| Visibility | **Public** (GitHub) · optional private Forgejo mirror |
| Live clinical PDFs | **Never** in this git tree |
| Related public stack | [ai-gateway](https://the1truedan.github.io/ai-gateway/) · [grok-tua-tok-tua](https://the1truedan.github.io/grok-tua-tok-tua/) · [johnny-appleseed-chipper](https://the1truedan.github.io/johnny-appleseed-chipper/) |

---

## Why this exists

Family caregivers often get **same-day multi-document packets** (many pages, many months of notes) hours before a care-system meeting. Re-reading everything under stress is the failure mode.

This lab packages:

1. A **runnable** accessibility triage harness on **synthetic** fixtures  
2. A **de-identified** production case study with **file-timestamp proof**  
3. Hard **PHI boundaries** so multi-brand coding agents cannot “helpfully” commit clinical text  

It is **not** a PTSD therapy product, not a clinical decision system, and not a certified Section 508 auditor. Prepare-only; humans sign off.

---

## Production proof (metrics only — Aug 2026)

Full numbers: [`evidence/complex_multidoc_2026-08-04_PUBLIC_METRICS.json`](evidence/complex_multidoc_2026-08-04_PUBLIC_METRICS.json) · narrative: [`docs/CASE_STUDY_DEIDENTIFIED.md`](docs/CASE_STUDY_DEIDENTIFIED.md)

| Signal | Result |
|--------|--------|
| Documents | **9** multi-page PDFs (~2.3 MB) |
| Span (filename dates) | ~15 months |
| Extracted text | ~160k characters · **OCR not required** |
| ADA-ish triage | **9/9** · score **85** typical |
| Caregiver synthesis size | ~62 KB markdown (body **not** here) |
| Meeting brief size | ~12 KB (body **not** here) |
| Extract → brief wall clock | **~19 minutes** (mtime delta) |
| Locality policy | LAN staging · local model route · **no cloud LLM** · no PHI in git |

Obfuscated story: *family member · home-based care visit notes · multi-month span · same-day structure for next-morning process questions — not as a weapon, as clarity.*

---

## Quick start (synthetic only)

Stdlib only for the harness. Optional: `pytest` for unit tests.

```bash
python3 scripts/run_harness.py fixtures/synthetic --json /tmp/lab_out.json
bash scripts/verify_no_phi_grep.sh
# optional:
# python3 -m pytest -q
```

---

## Docs

| Doc | Purpose |
|-----|---------|
| [`docs/PHI_BOUNDARY.md`](docs/PHI_BOUNDARY.md) | What never enters git |
| [`docs/CASE_STUDY_DEIDENTIFIED.md`](docs/CASE_STUDY_DEIDENTIFIED.md) | Scrubbed real-world use |
| [`docs/LOCALITY_AND_THREAT_MODEL.md`](docs/LOCALITY_AND_THREAT_MODEL.md) | LAN claims (honest strength) |
| [`docs/RELEASE_RELATIONSHIP.md`](docs/RELEASE_RELATIONSHIP.md) | mok-tua / Johnny / public AIDA extracts |
| [`docs/MANAGER_CONNECTIVITY.md`](docs/MANAGER_CONNECTIVITY.md) | How this lab sits in the full M.A.N.A.G.E.R. mesh |

---

## Multi-brand agents

Before filewalking medical storage or SSH: read [`docs/PHI_BOUNDARY.md`](docs/PHI_BOUNDARY.md) and
[`docs/MANAGER_CONNECTIVITY.md`](docs/MANAGER_CONNECTIVITY.md). Prefer session **IDs** over bulk
chat dumps. Do not walk medical NFS “for context.” Use `evidence/*PUBLIC*` metrics only.

Optional local denylist for operators handling real packets: copy
[`.phi_denylist.local.example`](.phi_denylist.local.example) → `.phi_denylist.local` (gitignored).

---

## Honest limits

- Scores are first-pass triage, not legal accessibility certification  
- Fixtures are invented people/events  
- Absolute network proof of “no cloud token ever” needs a gateway audit receipt (stretch)  
- Creative Pinokio orchestration is a **different** product (mok-tua), not this repo  
- Future public extracts (`ada-doc-check`, `plain-language-relay`) are siblings, not this tree  
- Vendor/agency brand names for the live run are **genericized** in public evidence filenames  

## Why ship proof without the full monorepo (yet)

This lab is a **prepare-only slice**: synthetic harness + scrubbed metrics + cognitive-load framing.  
The private control monorepo is planned for a later **public fork** with PHI and private identifiers removed — enough of the human *why* left in that others can see how lived caregiving, ethics, and hard work turned into tools, without chart dumps or personal chat noise. Full intent: [`docs/RELEASE_RELATIONSHIP.md`](docs/RELEASE_RELATIONSHIP.md) § *Eventually: the control monorepo, scrubbed*.
