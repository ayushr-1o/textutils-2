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
    assert c.is_palindrome("Race Car") is False
    assert c.is_palindrome("ne ver odd or even") is False 
    
def test_is_palindrome_edge_cases_and_punctuation():
    """Test edge cases involving empty strings, single characters, and punctuation."""
    assert c.is_palindrome("") is True
    assert c.is_palindrome("a") is True
    assert c.is_palindrome(" !a! ") is True
    assert c.is_palindrome("Hello world!") is False 

def test_is_palindrome_with_emojis():
    """Test palindrome with emojis (should handle or normalize Unicode)"""
    assert c.is_palindrome("😊nice emojis😊") == True