# agents/query_parser.py
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

def query_parser(query: str):
    tokens = word_tokenize(query.lower())  # Tokenize the query into words
    print(f"Parsed query: {tokens}")  # Debugging query parsing
    return tokens
