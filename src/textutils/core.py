def normalize_whitespace(text: str) -> str:
    """
    Collapse any whitespace runs to single spaces and trim.

    Example:
        >>> normalize_whitespace("  a   b \n  c  ")
        'a b c'
    """
    # Split on any whitespace and rejoin with single spaces.
    # This automatically handles leading/trailing whitespace.
    return ' '.join(text.split())
def top_n(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return the top n (word, count) pairs sorted by:
    1) highest count descending
    2) word alphabetically for ties
    
    Example:
        >>> top_n({"a": 2, "b": 2, "c": 1}, 2)
        [("a", 2), ("b", 2)]
    """
    if not counts:
        return []
    
    # Sort by: count descending (-item[1]), then word ascending (item[0])
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    
    # Return top n items
    return sorted_items[:n]

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