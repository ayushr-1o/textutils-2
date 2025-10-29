def is_palindrome(text: str) -> bool:
    """Check if text is a palindrome (ignoring case and spaces).
    
    Example:
        >>> is_palindrome("RaceCar")
        True
        >>> is_palindrome("hello")
        False
    """
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    
    # Check if it reads the same forwards and backwards
    return cleaned == cleaned[::-1]