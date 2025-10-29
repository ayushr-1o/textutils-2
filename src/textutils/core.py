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
