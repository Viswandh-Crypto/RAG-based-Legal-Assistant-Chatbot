# Legal Assistant Chatbot
# Features:
# - Loads court order PDF
# - Stores embeddings in FAISS
# - Interactive chatbot for Q&A
# - Gemini-2.0-flash as LLM backend

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.document_loaders import PyMuPDFLoader  
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# Load PDF from URL
loader = PyMuPDFLoader("https://nclt.gov.in/gen_pdf.php?filepath=/Efile_Document/ncltdoc/casedoc/2709138008372023/04/Order-Challenge/04_order-Challange_004_168441092321415434206466122b78ec3.pdf")
pages = loader.load_and_split()
print(len(pages), "pages loaded.")

# Set up LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Embeddings(Hugging face) + FAISS
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector = FAISS.from_documents(pages, embeddings)

# Prompt 
prompt = ChatPromptTemplate.from_template("""
You are a lawyer assistant. Use the following court order context to answer user questions clearly and concisely.

<context>
{context}
</context>

Question: {input}
Answer as if you are preparing a legal brief.
""")

# Build chain
document_chain = create_stuff_documents_chain(llm, prompt)
retriever = vector.as_retriever(search_kwargs={"k": 4})
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Chatbot loop
print("\n💼 Legal Assistant ready. Ask your questions about the case (type 'exit' to quit).\n")

chat_history = []

while True:
    query = input("👤 You: ")
    if query.strip.lower() in ["exit", "quit", "bye"]:
        print("👋 Exiting Legal Assistant. Goodbye!")
        break

    result = retrieval_chain.invoke({"input": query})
    answer = result["answer"]
    print(f"\n⚖️ Legal Assistant: {answer}\n")

    chat_history.append((query, answer))
