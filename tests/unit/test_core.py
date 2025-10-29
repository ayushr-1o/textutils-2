import textutils.core as c

# Agrega esta sección al final de tu archivo test_core.py

def test_remove_punctuation_basic():
    """Removes standard punctuation marks."""
    text = "Hello, World! How are you?"
    expected = "Hello World How are you"
    assert c.remove_punctuation(text) == expected

def test_remove_punctuation_complex_and_spaces():
    """Handles various punctuation types and keeps spaces/newlines."""
    text = "Text--with...hyphens. And, a; colon: \n \"Quotes\"."
    expected = "Textwithhyphens And a colon \n Quotes"
    # Nota: Tu implementación deberá decidir cómo manejar la puntuación interna (como los guiones). 
    # Para simplicidad, podemos esperar que los elimine.
    assert c.remove_punctuation(text) == expected

def test_remove_punctuation_empty_input():
    """Handles empty or punctuation-only strings."""
    assert c.remove_punctuation("") == ""
    assert c.remove_punctuation(".,!?:;") == ""