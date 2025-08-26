# RAG-based-Legal-Assistant-Chatbot

📚 RAG-based Legal Assistant Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with LangChain, HuggingFace embeddings, FAISS, and Gemini Pro LLM.
This assistant ingests legal documents (court orders, judgments, filings), indexes them for semantic search, and provides accurate, context-aware answers to user queries in natural language.

🔍 Features

 •📄 Document Ingestion: Load legal PDFs and split into context-preserving chunks.

 •🧠 Semantic Search with FAISS: Store embeddings for fast and relevant retrieval.

 •🤖 RAG Workflow: Retrieve top-k relevant chunks and augment LLM responses.

 •⚖️ Legal Query Answering: Summarize cases, identify petitioners, deadlines, and compliance details.

 •🔑 Pluggable LLMs: Currently supports Google Gemini Pro, but can be swapped with OpenAI, Anthropic, or others.

⚡ Tech Stack

 •LangChain
 – Orchestration framework

 •HuggingFace Transformers
 – Embeddings (sentence-transformers/all-MiniLM-L6-v2)

 •FAISS
 – Vector database for semantic search

 •Google Gemini Pro
 – LLM for generation

 🧑‍⚖️ Example Usage:
 22 pages loaded. 💼 Legal Assistant ready. Ask your questions about the case (type 'exit' to quit).

👤 You: summarize the case in 3 bullet points.

⚖️ Legal Assistant:
Here is a summary of the case based on the provided context:

• **Scheme Petition:** The Petitioner Companies filed a Company Scheme Petition (C.P. (CAA) / 20 / MB / 2023) connected with C.A. (CAA) / 256 / MB / 2022, seeking approval for a scheme of amalgamation. The meetings of the shareholders and creditors of the Petitioner Companies were dispensed with by the Hon’ble Tribunal vide order dated 16th December 2022.

• **Compliance and Fairness:** The Petitioner Companies complied with all statutory obligations. The Tribunal found the scheme fair, reasonable, not violative of law, and not contrary to public policy. Clarifications were provided in response to observations by the Official Liquidator and the Central Government.

• **Order and Directions:** The Tribunal sanctioned the scheme of amalgamation with an appointed date of 1st April 2022. Petitioner Companies must file a certified copy of the order and the scheme with the Registrar of Companies within 30 days.

👤 You: who were the petitioners?

⚖️ Legal Assistant:
The Petitioners in this matter are:

1. **KSDPL** – Kisan Sahakari Distillery Private Limited (Transferor Company 1)
2. **MVPL** – MYKINGDOM Ventures Private Limited (Transferor Company 2)
3. **SGPL** – Srirampur Grains Private Limited (Transferor Company 3)
4. **SPPL** – Studd Projects Private Limited (Transferor Company 4)
5. **TIL** – Tilaknagar Industries Limited (Transferee Company)

👤 You: what observations did the Official Liquidator make?

⚖️ Legal Assistant:
The Official Liquidator, High Court, Bombay, filed a report dated 17th April 2023 containing findings and factual details. One key observation was about Clause 12.1 of the scheme, which was stated to override Section 232(3)(i) of the Companies Act, 2013.

👤 You: bye 
⚖️ Legal Assistant:👋 Exiting Legal Assistant. Goodbye!

 🎯 Why RAG?

Legal documents are long, repetitive, and citation-heavy. Pure LLMs hallucinate.
This project anchors responses in retrieved evidence, ensuring factual accuracy and legal reliability.

🌟 Future Improvements

 • Add support for multiple document uploads

 • Implement chat history memory

 • Extend to multi-jurisdictional case law databases

 • Deploy as a web app (Streamlit / FastAPI)
