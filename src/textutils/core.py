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