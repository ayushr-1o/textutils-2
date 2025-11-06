# textutils-2

A collaborative Python package providing simple text utilities.

## Team Members
- Ayush Raj (@ayushr-1o) - Repository Owner
- Lucas (@Lucashaesaert)
- Patricia (@PatriciaUnger)
- Cesc (@francesc-canavate)
- Riwad (@Riwad00)

## Features 

Our package includes the following text utility functions:

- `word_count(text)` — Count word frequencies (case-insensitive)
- `top_n(counts, n)` — Get top-N most frequent words
- `normalize_whitespace(text)` — Collapse multiple spaces/newlines
- `remove_punctuation(text)` — Strip punctuation from text
- `is_palindrome(text)` — Check if text is a palindrome
- `unique_words(text)` — Check the amount of unique words

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/ayush/textutils-2.git
cd textutils-2
```

### 2. Create the environment
```bash
micromamba create -f textutils.yml -y
micromamba activate textutils
```

### 3. Install the package
```bash
pip install -e .
```

## Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=src/textutils --cov-report=term-missing
```

## Usage Example

```python
import textutils.core as tc

# Count words
text = "Hello world hello"
counts = tc.word_count(text)
print(counts)  # {"hello": 2, "world": 1}

# Get top words
top = tc.top_n(counts, 1)
print(top)  # [("hello", 2)]

# Check palindrome
print(tc.is_palindrome("racecar"))  # True
```

## Development

This project was developed as a collaborative assignment using:
- Test-Driven Development (TDD)
- Feature branch workflow
- Git version control
- Continuous testing with pytest

## License

Educational project for Esade Business School.