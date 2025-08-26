# RAG-based-Legal-Assistant-Chatbot

📚 RAG-based Legal Assistant Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with LangChain, HuggingFace embeddings, FAISS, and Gemini Pro LLM.
This assistant ingests legal documents (court orders, judgments, filings), indexes them for semantic search, and provides accurate, context-aware answers to user queries in natural language.

🔍 Features

📄 Document Ingestion: Load legal PDFs and split into context-preserving chunks.
🧠 Semantic Search with FAISS: Store embeddings for fast and relevant retrieval.
🤖 RAG Workflow: Retrieve top-k relevant chunks and augment LLM responses.
⚖️ Legal Query Answering: Summarize cases, identify petitioners, deadlines, and compliance details.
🔑 Pluggable LLMs: Currently supports Google Gemini Pro, but can be swapped with OpenAI, Anthropic, or others.
