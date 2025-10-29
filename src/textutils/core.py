def is_palindrome(text: str) -> bool:
    """Check if text is a palindrome (ignoring case, spaces, and punctuation).
    
    Example:
        >>> is_palindrome("RaceCar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("Madam, I'm Adam.")
        True
    """
    # Build a new list of characters,
    # keeping only alphanumeric ones and converting to lowercase.
    cleaned_chars = []
    for char in text:
        if char.isalnum():
            cleaned_chars.append(char.lower())
    
    # Join the clean characters into a new string
    cleaned = "".join(cleaned_chars)
    
    # Check if the cleaned string reads the same forwards and backwards.
    # This also correctly handles an empty string ("" == "") -> True
    return cleaned == cleaned[::-1]