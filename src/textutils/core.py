def word_count(text: str) -> dict[str, int]:
    """Return a case-insensitive word frequency dict.
    
    Example: 
        >>> word_count("Red red BLUE")
        {"red": 2, "blue": 1}
    """
    if not text:
        return {}
    
    # Convert to lowercase for case-insensitive counting
    text = text.lower()
    
    # Remove punctuation (simple approach)
    import string
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split into words
    words = text.split()
    
    # Count frequencies
    counts = {}
    for word in words:
        if word:  # Skip empty strings
            counts[word] = counts.get(word, 0) + 1
    
    return counts