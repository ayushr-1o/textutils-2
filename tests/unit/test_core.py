import textutils.core as c

def test_normalize_whitespace_multiple_spaces():
    """Test collapsing multiple spaces"""
    text = "hello    world"
    assert c.normalize_whitespace(text) == "hello world"

def test_normalize_whitespace_leading_trailing():
    """Test removing leading and trailing spaces"""
    text = "   hello world   "
    assert c.normalize_whitespace(text) == "hello world"

def test_normalize_whitespace_newlines_tabs():
    """Test converting newlines and tabs to spaces"""
    text = "hello\n\tworld"
    assert c.normalize_whitespace(text) == "hello world"

def test_normalize_whitespace_complex():
    """Test complex whitespace scenario"""
    text = "  a   b \n  c  "
    assert c.normalize_whitespace(text) == "a b c"

import textutils.core as c

def test_top_n_basic():
    """Test basic top-n selection"""
    counts = {"apple": 5, "banana": 3, "cherry": 8}
    result = c.top_n(counts, 2)
    assert result == [("cherry", 8), ("apple", 5)]

def test_top_n_with_ties():
    """Test that ties are sorted alphabetically"""
    counts = {"a": 2, "b": 2, "c": 1}
    result = c.top_n(counts, 2)
    assert result == [("a", 2), ("b", 2)]

def test_top_n_empty():
    """Test with empty dict"""
    assert c.top_n({}, 5) == []

def test_top_n_n_larger_than_dict():
    """Test when n is larger than number of items"""
    counts = {"x": 1}
    result = c.top_n(counts, 10)
    assert result == [("x", 1)]
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