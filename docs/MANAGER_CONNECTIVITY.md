# How this lab connects to M.A.N.A.G.E.R.

**Repo:** `aida-complex-doc-lab` (**public**)  
**Role:** production-proof + synthetic harness for **document** cognitive load — not the full monorepo.

---

## 1. Why this lab (need-driven)

Same-day multi-document care packets arrive before process meetings. Re-reading everything under stress is the failure mode. This lab exists because a **real multi-PDF drop** had to become structured, reviewable markdown **the same day** — with hard PHI boundaries so agents cannot “helpfully” commit clinical text.

That is **post-problem progress toward production tools**, not pure top-down design.

---

## 2. Named-module chain (document path)

```text
Raw docs / PDFs
  → D.A.N.          (Digital Assimilating Neuron — intake)
  → A.I.D.A.        first_pass  (structure, ADA-ish triage, prepare-only)
  → A.I.D.A.        deep_assurance  (when ADA flags need more)
  → M.A.R.K.        (Markdown archival / reconciliation)
  → N.A.R.C.        (PHI detect/mask)
  → P.E.A.L.        (privacy / consent audit)
  → K.A.R.E.N.      (rule gate before side effects)
  → J.E.S.U.S.      (audit / re-vet — prepare-only still)
  → syn:N.A.P.S.E.  (immutable receipt — no raw PHI bodies)
```

**This lab** exercises the **A.I.D.A. middle** (ADA-ish harness + de-identified case metrics).  
Full mesh modules live in the private control monorepo (not published here).

---

## 3. Gateway path (code work vs care work)

| Work class | Path | Notes |
|------------|------|--------|
| **Code / docs (non-PHI)** | coding CLI → Headroom compress → LiteLLM place | Prefer local GPU workers for heavy code |
| **Care / PHI** | LAN staging + local-only model route | **No** free-cloud façades; **no** git of clinical bodies |
| **Session index** | local UI — **IDs only** | Do not bulk-dump year view into models |

Public sibling that shows how agents attach to the gateway:  
https://github.com/the1truedan/grok-tua-tok-tua  

Public gateway glue:  
https://github.com/the1truedan/ai-gateway  

---

## 4. Future public extracts (siblings, not this repo)

| Product | Future public name | Scope |
|---------|-------------------|--------|
| **A** | `ada-doc-check` | Generic ADA/WCAG scorer — no PHI vocabulary required |
| **B** | `plain-language-relay` | Dual-audience plain language (care vocabulary packs optional) |

This lab **feeds honesty** for those extracts (metrics + synthetic fixtures). It is **not** a substitute for them.

Creative Pinokio/Comfy conductor is **mok-tua** — different product class.

---

## 5. PHI boundary

See [`PHI_BOUNDARY.md`](./PHI_BOUNDARY.md).

---

## 6. Big-picture spine (one paragraph)

Home-lab caregiving work repeatedly hit **document overload**. A.I.D.A. grew inside M.A.N.A.G.E.R. as prepare-only accessibility + structure between raw intake (D.A.N.) and audit (J.E.S.U.S.). This public lab freezes a **scrubbed production story** so multi-brand agents stop rediscovering the same multi-PDF problem via storage walks, while future ADA extracts can ship without clinical bodies.
