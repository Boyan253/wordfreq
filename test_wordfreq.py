import wordfreq


def test_tokenize_lowercases_and_splits():
    assert wordfreq.tokenize("Hello, World!") == ["hello", "world"]

def test_tokenize_keeps_apostrophes():
    assert "don't" in wordfreq.tokenize("Don't stop")
