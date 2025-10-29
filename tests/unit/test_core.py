import textutils.core as c

def test_normalize_whitespace_multiple_spaces():
    """Test collapsing multiple spaces"""
    text = "hello    world"
    assert c.normalize_whitespace(text) == "hello world"

def test_normalize_whitespace_leading_trailing():
    """Test removing leading and trailing spaces"""
    text = "   hello world   "
    assert c.normalize_whitespace(text) == "hello world"

def test_normalize_whitespace_newlines_tabs():
    """Test converting newlines and tabs to spaces"""
    text = "hello\n\tworld"
    assert c.normalize_whitespace(text) == "hello world"

def test_normalize_whitespace_complex():
    """Test complex whitespace scenario"""
    text = "  a   b \n  c  "
    assert c.normalize_whitespace(text) == "a b c"