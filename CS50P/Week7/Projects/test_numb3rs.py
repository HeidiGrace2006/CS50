from numb3rs import validate

def test_format():
    assert validate("1.1.1.1") == True
    assert validate("cat") == False
    assert validate("1.1..1.1") == False
    assert validate("1.1.1.1.1") == False

def test_range():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.256") == False
    assert validate("256.0.0.0") == False
    assert validate("11111.2.3.4") == False
