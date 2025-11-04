import textutils.core as c

def test_word_analysis_pipeline():
    """Test complete word analysis workflow"""
    # Original text with mixed case and punctuation
    text = "Hello, world! Hello Python. Python is great!"
    
    # Step 1: Remove punctuation
    cleaned = c.remove_punctuation(text)
    
    # Step 2: Count words
    counts = c.word_count(cleaned)
    
    # Step 3: Get top words
    top_words = c.top_n(counts, 2)
    
    # Verify the pipeline works
    assert ("hello", 2) in top_words or ("python", 2) in top_words
    
def test_palindrome_with_normalization():
    """Test palindrome check with whitespace normalization"""
    text = "  race   car  "
    normalized = c.normalize_whitespace(text)
    assert c.is_palindrome(normalized) == True