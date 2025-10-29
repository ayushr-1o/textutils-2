
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