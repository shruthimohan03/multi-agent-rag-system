import os
from groq import Groq

client = Groq(
    api_key='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'
)
from pathlib import Path

def response_generator(top_docs, query):
    # Base path for the documents folder
    documents_folder = Path("documents")
    print(top_docs)
    # Combine the content of the top documents into a single string
    content = " ".join(
        (documents_folder / top_docs[0]).read_text(encoding="utf-8", errors="ignore") 
    )

    # Format the prompt using f-strings for clarity
    prompt = (
        f"You are a question answering system. The given question is: {query}. "
        f"\ncontent: {content} "
        "Combine information from 'content' into a clear response and answer the question. "
        "\nOutput only the answer."
    )

    messages = [
        {
            "role": "system",
            "content": "You are a question answering system."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    # Call the Groq API
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192"  
    )

    response = chat_completion.choices[0].message.content
    return response

