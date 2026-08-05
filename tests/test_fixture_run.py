from pathlib import Path

from aida_lab.harness import run_and_scrub, run_root

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "fixtures" / "synthetic"


def test_synthetic_run_counts():
    raw = run_root(FIX)
    assert raw["counts"]["documents"] >= 3
    for d in raw["documents"]:
        assert d["ada_score"] >= 60
        assert "snippet" not in d


def test_scrubbed_public_shape():
    scrubbed = run_and_scrub(FIX)
    assert scrubbed["privacy_class"] == "public-summary"
    assert scrubbed["counts"]["documents"] >= 3
    for d in scrubbed["documents_metrics_only"]:
        assert "snippet" not in d
        assert "path" not in d
