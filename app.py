# app.py
import streamlit as st
from agents.document_retriever_ranker import document_retriever_ranker
from agents.response_generator import response_generator

def streamlit_app():
    st.title('Multi-Agentic Retrieval-Augmented Generation System')

    query = st.text_input("Enter your query:")
    # Empty containers for previous outputs (results and response)
    results_placeholder = st.empty()
    response_placeholder = st.empty()
    if query:
        st.write("Processing your query...")

        ranked_docs = document_retriever_ranker(query)  # Get top 3 ranked documents along with similarity scores
        if ranked_docs:
            st.write("Top 5 Documents:")
            for doc, score in ranked_docs:
                st.write(f"Document: {doc}, Similarity Score: {score:.4f}")  # Display document name and similarity score

            # Generate a response based on the top 3 documents
            response = response_generator([doc for doc, _ in ranked_docs],query)
            st.write("Generated Response:")
            st.write(response)
        else:
            st.write("No relevant documents found!")
    else:
        st.write("Please enter a query.")

if __name__ == "__main__":
    streamlit_app()
