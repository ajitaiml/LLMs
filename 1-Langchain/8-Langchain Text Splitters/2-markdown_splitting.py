from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
# Project Name: Python Code Splitter

A simple Python-based project to split code into smaller chunks for easier processing using LangChain’s `RecursiveCharacterTextSplitter`.

## Features
- Split Python code into chunks
- Customize `chunk_size` and `chunk_overlap`
- Supports splitting code directly from a string

## Code

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Example Python code string
python_code = 
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(add(2, 3))
print(multiply(4, 5))
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 50,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

num_of_chars = char_count = len(text)

print(num_of_chars)
print(len(chunks))
print(chunks)