from seasons import check
import pytest

def test_format():
    assert check("2006-04-15") == "Nine million, two hundred thirty-one thousand, eight hundred forty"
    with pytest.raises(SystemExit):
        check("04-15-2006")
        check("April 15th, 2006")
        check("Cat")

