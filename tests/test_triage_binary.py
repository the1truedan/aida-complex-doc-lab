from aida_lab.ada_compliance import ada_pre_check


def test_empty_content_penalized():
    r = ada_pre_check({"content": ""}, doc_type="pdf")
    assert r["ada_score"] <= 60
    assert "empty_content" in r["ada_flags"]


def test_good_text_high_score():
    r = ada_pre_check({"content": "Hello accessible document text.", "has_alt_text": True}, doc_type="pdf")
    assert r["ada_score"] >= 85
