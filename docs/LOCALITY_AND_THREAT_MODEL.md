# Locality and threat model

## Claim levels for “documents never left the LAN”

| Claim | Strength | Evidence in this repo |
|-------|----------|------------------------|
| Source PDFs staged on LAN medical root | Strong (ops) | Policy + public metrics; path omitted |
| No PHI in git remotes | Strong if verify script clean **and** history scrubbed | CI/local script + no real tokens in denylist |
| Inference on local model route only | Policy-strong | Operator local-only model route; not proven by this repo alone |
| Cryptographic proof no cloud token left the house | Stretch | Needs gateway audit receipt for that session — template only |

## Threats

| Threat | Mitigation |
|--------|------------|
| Agent dumps medical extracts into public git | PHI_BOUNDARY + verify script |
| Cloud LLM on clinical text | Forbidden route; lab uses offline fixtures |
| AgentsView bulk scrape into prompts | Index-only rule |
| Credential-bearing git remotes | Clean URLs + helper/SSH |

## Prepare-only

Accessibility scores are triage, not Section 508 certification. Plain-language helpers are not medical advice.
