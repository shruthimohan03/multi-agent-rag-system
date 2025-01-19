from sentence_transformers import SentenceTransformer
import numpy as np
from agents.query_parser import query_parser
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

# Load documents from the 'documents' folder
documents_folder = Path('documents')
documents = {}
for doc_path in documents_folder.glob('*.txt'):  # Read all .txt files
    with open(doc_path, 'r', encoding='utf-8') as file:
        documents[doc_path.name] = file.read()

# Initialize the model for encoding documents and queries
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Encode documents into embeddings
document_embeddings = []
document_names = list(documents.keys())

for doc in documents.values():
    embedding = model.encode([doc])[0]  # Ensure we're getting the embedding
    document_embeddings.append(embedding)

document_embeddings = np.array(document_embeddings)

# Function to retrieve documents based on a query and return top 3 ranked by similarity
def document_retriever_ranker(query: str):
    parsed_query = query_parser(query)  # Process the query
    query_embedding = model.encode([query])[0].reshape(1, -1)  # Get the embedding for the query

    # Calculate cosine similarity between the query embedding and all document embeddings
    similarities = cosine_similarity(query_embedding, document_embeddings)[0]

    # Get indices of top 3 most similar documents (sorted in descending order)
    top_indices = similarities.argsort()[-5:][::-1]

    # Return the top 3 documents with the highest similarity scores
    top_docs = [document_names[i] for i in top_indices]
    top_scores = similarities[top_indices]
    return list(zip(top_docs, top_scores))
