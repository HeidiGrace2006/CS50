from project import get_word, win_check, lose_check

icecream_cone = [
    "       ()",
    "      (__)",
    "     (____)",
    "    (______)",
    "   (________)",
    "  (__________)",
    r"   \/\/\/\/\/",
    r"    \/\/\/\/",
    r"     \/\/\/",
    r"      \/\/",
    r"       \/"
]

word = "tiger"
guessed_correct = []

def test_get_word():
    plants = ["cactus", "basil", "lettuce", "lavender", "orchid", "hibiscus", "flower", "thyme", "herb"]
    assert get_word("plants") in plants

def test_win_check():
    assert win_check("t", word) is False
    assert win_check("i", word) is False
    assert win_check("g", word) is False
    assert win_check("x", word) is False
    guessed_correct.extend(["t", "i", "g"])
    assert win_check("e", word) is False
    assert win_check("r", word) is True
    guessed_correct.extend(["e", "r"])
    assert win_check("r", word) is True

def test_lose_check():
    assert lose_check() is False


