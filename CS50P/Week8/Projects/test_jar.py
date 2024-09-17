from jar import Jar
import pytest

def test_init():
    jar1 = Jar(12, 0)
    assert str(jar1.capacity) == "12"

def test_str():
    jar2 = Jar()
    assert str(jar2) == ""
    jar2.deposit(1)
    assert str(jar2) == "🍪"
    jar2.deposit(11)
    assert str(jar2) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar3 = Jar()
    jar3.deposit(5)
    assert str(jar3) == "🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar3.deposit(8)

def test_withdraw():
    jar4 = Jar(12, 5)
    with pytest.raises(ValueError):
        jar4.withdraw(6)