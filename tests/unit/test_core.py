import textutils.core as c

def test_word_count_basic():
    """Test basic word counting with mixed case"""
    text = "Red red BLUE"
    assert c.word_count(text) == {"red": 2, "blue": 1}

def test_word_count_empty():
    """Test empty string returns empty dict"""
    assert c.word_count("") == {}

def test_word_count_single_word():
    """Test single word"""
    assert c.word_count("hello") == {"hello": 1}

def test_word_count_with_punctuation():
    """Test that punctuation is handled"""
    text = "Hello, world! Hello?"
    # This assumes we strip punctuation
    result = c.word_count(text)
    assert "hello" in result
    assert result["hello"] == 2