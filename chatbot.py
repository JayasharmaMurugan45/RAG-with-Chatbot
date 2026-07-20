from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

# 1️⃣ Load PDF
pdf_path = r"D:\PYTHON\CHATBOT\Q.pdf"
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# 2️⃣ Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10
)
chunks = text_splitter.split_documents(documents)

# 3️⃣ Embeddings (FREE)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4️⃣ Vector store
vectorstore = FAISS.from_documents(chunks, embeddings)

# 5️⃣ FREE LLM (no OpenAI)
qa_pipeline = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_length=50
)

# 6️⃣ Chat loop
print("📚 RAG Chatbot ready! Type 'exit' to quit.")

while True:
    query = input("\nYou: ")

    if query.lower() in ["exit", "quit"]:
        print("Bye! 👋")
        break

    # 🔍 Retrieve relevant chunks
    docs = vectorstore.similarity_search(query, k=3)

    context = " ".join([doc.page_content for doc in docs])
    # print(context)

    # 🧠 Generate answer
    prompt = f"""
    You must answer ONLY from the given context.
    Do NOT add extra information.
    If the answer is not in the context, say "Not found in document".
    {context}

    Question: {query}
    Answer:
    """

    result = qa_pipeline(prompt)

    # output = result[0]['generated_text']

    
    # if "Answer:" in output:
    #     answer = output.split("Answer:")[-1].strip()
    # else:
    #     answer = output.strip()

    print("Bot:", result)