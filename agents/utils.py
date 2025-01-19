# agents/utils.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def load_documents(doc_folder: str):
    # Your logic to load documents here
    documents = {}
    # Example document loading
    # documents = { 'doc1.txt': 'content', 'doc2.txt': 'content', ... }
    return documents

def encode_documents(documents):
    document_embeddings = []
    document_names = list(documents.keys())
    for doc in documents.values():
        embedding = model.encode([doc])[0]
        document_embeddings.append(embedding)
    return np.array(document_embeddings), document_names

def create_faiss_index(document_embeddings):
    index = faiss.IndexFlatL2(document_embeddings.shape[1])
    index.add(document_embeddings)
    return index

def retrieve_documents(query, model, index, document_names):
    query_embedding = model.encode([query])[0].reshape(1, -1)
    _, indices = index.search(query_embedding, 5)  # top 5 documents
    return [document_names[i] for i in indices[0]]
