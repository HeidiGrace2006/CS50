import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
def test_errors():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("-1/2")
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
def test_other():
    assert gauge(20) == "20%"