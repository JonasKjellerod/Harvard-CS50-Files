from twttr import shorten

def test_shorten_upper():
    assert shorten("twitter") == "twttr"
    assert shorten("TwITteR") == "TwTtR"
    assert shorten("1234") == "1234"
    assert shorten(".,!@?") == ".,!@?"


