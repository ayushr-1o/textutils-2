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