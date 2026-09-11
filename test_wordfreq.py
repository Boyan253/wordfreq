import wordfreq


def test_tokenize_lowercases_and_splits():
    assert wordfreq.tokenize("Hello, World!") == ["hello", "world"]

def test_tokenize_keeps_apostrophes():
    assert "don't" in wordfreq.tokenize("Don't stop")


def test_tokenize_drops_digits():
    assert wordfreq.tokenize("abc 123 def") == ["abc", "def"]

def test_min_length_filter():
    assert wordfreq.tokenize("a bb ccc", min_length=3) == ["ccc"]


def test_stopwords_are_removed_by_default():
    pairs = dict(wordfreq.count("the the the cat"))
    assert "the" not in pairs and pairs["cat"] == 1

def test_keeping_stopwords():
    pairs = dict(wordfreq.count("the the cat", use_stopwords=False))
    assert pairs["the"] == 2


def test_bigrams():
    pairs = dict(wordfreq.count("red car red car", n=2, use_stopwords=False))
    assert pairs["red car"] == 2

def test_bar_scales_to_the_biggest():
    assert len(wordfreq.bar(10, 10, width=10)) == 10
    assert len(wordfreq.bar(5, 10, width=10)) == 5
