import string
# Puedes añadir el import re si es necesario para más adelante
# import re 

def remove_punctuation(text: str) -> str:
    """Strip punctuation while keeping spaces and letters."""
    
    # Esta es la lógica principal que elimina los caracteres de puntuación
    translator = str.maketrans('', '', string.punctuation)
    text_without_punc = text.translate(translator)
  
    
    return text_without_punc 