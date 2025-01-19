# Multi-Agent Response Generator

This project is a multi-agent response generator that uses the Groq API to generate responses based on top documents and a given query.

## Setup

1. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the root directory and add your Groq API key:
    ```env
    GROQ_API_KEY=your_api_key_here
    ```

## Usage

To run the Streamlit app, use the following command:
```sh
streamlit run app.py
```

## Project Structure

```
multi_agent_rag/
│
├── agents/
│   ├── document_retriever_ranker.py
│   ├── query_parser.py
│   ├── response_generator.py
│   └── utils.py
│
├── documents/
│   └── (your text documents here)
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```
