from plates import is_valid

def test_begin_with_alpha():
    assert is_valid("Hello") == True
    assert is_valid("11hi") == False
    assert is_valid("11") == False
    assert is_valid("AA") == True
    assert is_valid("1234AB") == False
def test_amount_of_characters():
    assert is_valid("abcdef") == True
    assert is_valid("a") == False
    assert is_valid("abcdefg") == False
def test_nums():
    assert is_valid("AA11") == True
    assert is_valid("AA11A1") == False
    assert is_valid("AA10") == True
    assert is_valid("AA01") == False
def test_punct():
    assert is_valid("AA11") == True
    assert is_valid("AA!!") == False