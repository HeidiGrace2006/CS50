from bank import value

def test_zero():
    assert value("hello") == 0
def test_h():
    assert value("howdy") == 20
def test_hundred():
    assert value("bye") == 100
def test_caps():
    assert value("HELLO") == 0
    assert value("HOWDY") == 20
    assert value("BYE") == 100

