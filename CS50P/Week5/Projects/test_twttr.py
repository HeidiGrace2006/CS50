from twttr import shorten

def test_lower():
    assert shorten("hello") == "hll"
def test_upper():
    assert shorten("HELLO") == "HLL"
def test_mix_case():
    assert shorten("hELlO") == "hLl"
def test_num():
    assert shorten("123") == "123"
def test_punct():
    assert shorten("!?$") == "!?$"
