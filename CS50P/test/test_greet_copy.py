from greet import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

#You can also test multiple strings by using a loop
def test_example():
    for name in ["Heidi", "Hana", "Mom", "Dad"]:
        assert hello(name) == f"hello, {name}"