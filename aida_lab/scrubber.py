"""Export public-safe metrics from harness-like JSON (drops free text)."""

from __future__ import annotations

from typing import Any, Dict, List

_DROP_KEYS = {
    "snippet",
    "text",
    "content",
    "text_preview",
    "body",
    "name",
    "path",
    "patient",
    "mrn",
    "dob",
    "address",
    "phone",
    "diagnosis",
    "doc_types",
}


def scrub_document_row(row: Dict[str, Any]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for k, v in row.items():
        kl = k.lower()
        if k in _DROP_KEYS or any(x in kl for x in ("snippet", "text", "name", "path", "patient")):
            continue
        if isinstance(v, (str, bytes)) and len(str(v)) > 200:
            continue
        if isinstance(v, dict):
            out[k] = scrub_document_row(v)
        elif isinstance(v, list):
            if k == "ada_flags":
                out["ada_flags_count"] = len(v)
            elif all(isinstance(x, (int, float, bool)) for x in v):
                out[k] = v
            else:
                out[f"{k}_count"] = len(v)
        else:
            out[k] = v
    return out


def scrub_harness(payload: Dict[str, Any]) -> Dict[str, Any]:
    docs: List[Dict[str, Any]] = []
    for d in payload.get("documents") or []:
        if isinstance(d, dict):
            docs.append(scrub_document_row(d))
    return {
        "schema": "aida.public_run_metrics.v1",
        "privacy_class": "public-summary",
        "no_phi_in_this_file": True,
        "counts": payload.get("counts"),
        "documents_metrics_only": docs,
        "capabilities": {
            k: v
            for k, v in (payload.get("capabilities") or {}).items()
            if not isinstance(v, str) or len(v) < 80
        },
    }
