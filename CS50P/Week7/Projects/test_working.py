from working import convert
import pytest

def test_valid_times():
    assert convert("12 AM to 1 PM") == "00:00 to 13:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
 #       convert("9:65 AM to 4:34 PM")
        convert("9:34 AM to 4:65 PM")
        convert("13 AM to 15 AM")
   #     convert("cat AM to dog PM")

def test_AM_or_PM():
  #  assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    with pytest.raises(ValueError):
        convert("5 am to 9 PM")

def test_formats():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:01 AM to 5:01 PM") == "09:01 to 17:01"
    with pytest.raises(ValueError):
    #    convert("5 to 9")
 #       convert("5 AM through 9 PM")
        convert("5 AM 9 PM")

