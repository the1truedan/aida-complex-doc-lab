# PHI boundary

## Never commit

- Patient legal names, DOB, MRN, address, phone, insurance IDs  
- Full visit-note text, caregiver synthesis bodies, meeting brief bodies  
- Unredacted harness JSON with `snippet` fields  
- Screenshots of clinical PDFs  
- Real medical paths that include surnames (use role paths in prose)

## Always OK

- Document counts, byte sizes, SHA-256 of **synthetic** fixtures only  
- ADA scores / flags that contain no clinical content  
- Wall-clock mtimes for de-identified run metrics  
- Policy statements (local-only, no cloud LLM)  
- Invented fixture names (e.g. “Jordan Lee”)

## Never put in the committed denylist script

Real patient names, clinician names, MRNs, drug names tied to a real chart, or vendor case IDs.  
Operators may keep those only in **gitignored** `.phi_denylist.local` (see `.phi_denylist.local.example`).

## Live production lane

Real multi-document medical packets stay on operator LAN medical staging under local ops law. This lab proves the **pipeline** with synthetic data and **public metrics** only.
