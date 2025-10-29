import textutils.core as c

def test_unique_words_basic():
    """Test extracting unique words from a simple sentence"""
    text = "hello world hello"
    assert set(c.unique_words(text)) == {"hello", "world"}

def test_unique_words_punctuation():
    """Test handling punctuation correctly"""
    text = "Hello, world! Hello?"
    assert set(c.unique_words(text)) == {"hello", "world"}

def test_unique_words_case_insensitive():
    """Test case insensitivity"""
    text = "Apple apple APPLE"
    assert set(c.unique_words(text)) == {"apple"}

def test_unique_words_with_numbers():
    """Test keeping numbers as words"""
    text = "car model 2025 model"
    assert set(c.unique_words(text)) == {"car", "model", "2025"}

def test_unique_words_empty_string():
    """Test empty input string"""
    text = ""
    assert c.unique_words(text) == []

def test_unique_words_complex():
    """Test complex text with punctuation and mixed cases"""
    text = "Python, python! PYTHON? Data, data."
    assert set(c.unique_words(text)) == {"python", "data"}