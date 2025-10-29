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

def test_is_palindrome_empty():
    """Test empty string"""
    assert c.is_palindrome("") == True

def test_is_palindrome_single_char():
    """Test single character"""
    assert c.is_palindrome("a") == True

def test_is_palindrome_simple_true():
    """Test a simple palindrome word"""
    assert c.is_palindrome("madam") == True

def test_is_palindrome_simple_false():
    """Test a non-palindrome word"""
    assert c.is_palindrome("hello") == False