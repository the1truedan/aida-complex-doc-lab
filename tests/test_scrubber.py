from aida_lab.scrubber import scrub_document_row, scrub_harness


def test_scrub_drops_snippet_and_path():
    row = {
        "path": "/secret/medical/note.pdf",
        "name": "REALNAME.pdf",
        "snippet": "SHOULD NOT APPEAR patient details",
        "bytes": 100,
        "ada_score": 85,
        "ada_flags": ["missing_alt_text"],
        "chars": 10,
    }
    out = scrub_document_row(row)
    assert "snippet" not in out
    assert "path" not in out
    assert "name" not in out
    assert out["ada_score"] == 85
    assert out["ada_flags_count"] == 1


def test_scrub_harness_schema():
    payload = {
        "counts": {"documents": 1},
        "documents": [{"path": "/x", "snippet": "nope", "ada_score": 80, "bytes": 1}],
        "capabilities": {"ada_compliance": True},
    }
    scrubbed = scrub_harness(payload)
    assert scrubbed["no_phi_in_this_file"] is True
    assert "snippet" not in scrubbed["documents_metrics_only"][0]
