# src/textutils/core.py
from __future__ import annotations
import string
import unicodedata


def _strip_accents(s: str) -> str:
    """Return s without diacritics, keeping base letters."""
    # NFKD decomposes letters + accents; filter combining marks
    return "".join(ch for ch in unicodedata.normalize("NFKD", s) if not unicodedata.combining(ch))


def _has_accents(s: str) -> bool:
    """True if s contains any diacritics."""
    return s != _strip_accents(s)


def unique_words(text: str) -> list[str]:
    """Return a sorted list of unique words.

    Rules:
      - Case insensitive
      - Punctuation removed (ASCII set)
      - Words deduplicated accent-insensitively
      - If both accented and unaccented versions appear, prefer the accented form
      - Output sorted alphabetically

    Examples:
        >>> unique_words("Red, red... BLUE blue? green")
        ['blue', 'green', 'red']
        >>> unique_words("café Cafe CAFÉ")
        ['café']
    """
    if not text:
        return []

    # Normalize case and strip ASCII punctuation
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into tokens
    tokens = [w for w in text.split() if w]

    # Map accent-stripped key -> chosen representative token
    rep: dict[str, str] = {}
    for w in tokens:
        key = _strip_accents(w)
        if key not in rep:
            # First time we see this base form, keep what we have
            rep[key] = w
        else:
            # If we previously stored an unaccented form but now we see an accented one, upgrade
            if not _has_accents(rep[key]) and _has_accents(w):
                rep[key] = w

    # Return sorted unique representatives
    return sorted(rep.values())
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