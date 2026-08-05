"""Minimal local harness for synthetic text fixtures (no network)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List

from aida_lab.ada_compliance import ada_pre_check
from aida_lab.scrubber import scrub_harness

_CHUNK = 1024 * 1024


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(_CHUNK), b""):
            h.update(block)
    return h.hexdigest()


def process_text_file(path: Path) -> Dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    score = ada_pre_check({"content": raw, "has_alt_text": True}, doc_type="document")
    return {
        "name": path.name,
        "ext": path.suffix.lstrip(".") or "txt",
        "bytes": path.stat().st_size,
        "sha256": sha256_of(path),
        "chars": len(raw),
        "needs_ocr": False,
        "decidable": True,
        "accessible_as_is": score["ada_score"] >= 60,
        "ada_score": score["ada_score"],
        "ada_flags": score["ada_flags"],
        "errors": [],
        # deliberately no snippet field in lab default path
    }


def run_root(root: Path) -> Dict[str, Any]:
    files = sorted(
        p
        for p in root.rglob("*")
        if p.is_file() and p.suffix.lower() in {".txt", ".md"} and not p.name.startswith(".")
    )
    docs: List[Dict[str, Any]] = [process_text_file(p) for p in files]
    payload = {
        "counts": {"documents": len(docs), "unique": len(docs), "duplicate_sets": 0},
        "documents": docs,
        "capabilities": {"ada_compliance": True, "pdf_tools": {"available": False, "note": "text fixtures only"}},
    }
    return payload


def run_and_scrub(root: Path) -> Dict[str, Any]:
    return scrub_harness(run_root(root))


def write_json(payload: Dict[str, Any], out: Path) -> None:
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
