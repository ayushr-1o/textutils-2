# tests/unit/test_core.py
from textutils.core import unique_words


def test_unique_words_basic():
    text = "Red, red... BLUE blue? green"
    assert unique_words(text) == ["blue", "green", "red"]


def test_unique_words_empty():
    assert unique_words("") == []


def test_unique_words_only_whitespace():
    assert unique_words("   \n\t  ") == []


def test_unique_words_punctuation_and_spacing():
    text = "hello!!!   hello,, world; world?"
    assert unique_words(text) == ["hello", "world"]


def test_unique_words_case_insensitive():
    text = "Word word WORD WoRd"
    assert unique_words(text) == ["word"]


def test_unique_words_numbers_allowed():
    text = "room 101 and 101 dalmatians"
    assert unique_words(text) == ["101", "and", "dalmatians", "room"]


def test_unique_words_unicode_letters():
    text = "café Cafe CAFÉ"
    assert unique_words(text) == ["café"]


def test_unique_words_only_punctuation():
    text = "!!! ??? ,,, ..."
    assert unique_words(text) == []