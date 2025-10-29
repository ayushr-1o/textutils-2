import textutils.core as c
from textutils.core import unique_words
import textutils.core as c
import textutils.core as c

# Agrega esta sección al final de tu archivo test_core.py

def test_remove_punctuation_basic():
    """Removes standard punctuation marks."""
    text = "Hello, World! How are you?"
    expected = "Hello World How are you"
    assert c.remove_punctuation(text) == expected

def test_remove_punctuation_complex_and_spaces():
    """Handles various punctuation types and keeps spaces/newlines."""
    text = "Text--with...hyphens. And, a; colon: \n \"Quotes\"."
    expected = "Textwithhyphens And a colon \n Quotes"
    # Nota: Tu implementación deberá decidir cómo manejar la puntuación interna (como los guiones). 
    # Para simplicidad, podemos esperar que los elimine.
    assert c.remove_punctuation(text) == expected

def test_remove_punctuation_empty_input():
    """Handles empty or punctuation-only strings."""
    assert c.remove_punctuation("") == ""
    assert c.remove_punctuation(".,!?:;") == ""
# tests/unit/test_core.py


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
import textutils.core as c

def test_is_palindrome_basic():
    """Test basic palindrome"""
    assert c.is_palindrome("racecar") == True

def test_is_palindrome_with_spaces():
    """Test palindrome with spaces (should ignore)"""
    assert c.is_palindrome("race car") == True

def test_is_palindrome_case_insensitive():
    """Test that case is ignored"""
    assert c.is_palindrome("RaceCar") == True

def test_is_palindrome_not():
    """Test non-palindrome"""
    assert c.is_palindrome("hello") == False
# added by Ayush  
def test_is_palindrome_empty():
    """Test empty string"""
    assert c.is_palindrome("") == True

def test_is_palindrome_single_char():
    """Test single character"""
    assert c.is_palindrome("a") == True
# added by Patricia 
def test_is_palindrome_with_punctuation():
    """Test palindrome ignoring punctuation"""
    assert c.is_palindrome("Madam, I'm Adam.") == True

def test_is_palindrome_numbers():
    """Test numeric palindrome"""
    assert c.is_palindrome("12321") == True

#added by Lucas 
def test_is_palindrome_mixed_case():
    """Test palindrome with mixed case"""
    assert c.is_palindrome("RaceCar") == True

def test_is_palindrome_with_spaces():
    """Test palindrome with spaces (ignoring case and spaces)"""
    assert c.is_palindrome("A man a plan a canal Panama") == True

#added by Cesc
 
def test_is_palindrome_full_noise_coverage():
    """Test a complex palindrome that requires ignoring case, spaces, and punctuation."""
    # This comprehensive test ensures the core logic handles all required clean-up steps
    assert c.is_palindrome("A man, a plan, a canal: Panama.") is True
    assert c.is_palindrome("Madam, I'm Adam.") is True
    
def test_is_palindrome_numeric_and_complex_false():
    """Test numeric and complex non-palindrome cases."""
    # Test numeric palindrome
    assert c.is_palindrome("12321") is True
    # Test complex non-palindrome
    assert c.is_palindrome("Race Car") is True
    assert c.is_palindrome("ne ver odd or even") is True 
    
def test_is_palindrome_edge_cases_and_punctuation():
    """Test edge cases involving empty strings, single characters, and punctuation."""
    assert c.is_palindrome("") is True
    assert c.is_palindrome("a") is True
    assert c.is_palindrome(" !a! ") is True
    assert c.is_palindrome("Hello world!") is False 

def test_is_palindrome_with_emojis():
    """Test non-palindrome with emojis (should handle or normalize Unicode)"""
    # The function strips emojis, and "niceemojis" is not a palindrome.
    assert c.is_palindrome("😊nice emojis😊") == False