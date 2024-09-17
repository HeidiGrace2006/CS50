from um import count

def test_counting():
    assert count("Hello, um, hi") == 1
    assert count("Hello, um, hi, um") == 2

def test_words():
    assert count("I have an umbrella") == 0

def test_mix():
    assert count("Hello, um, hi, I have an umbrella") == 1
    assert count("Hello, ummmmmm hi, um hows it going") == 1

def test_caser():
    assert count("UM, hi, howdy, um") == 2