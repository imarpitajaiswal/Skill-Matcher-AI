# Skill-Matcher-AI
# A conceptual snippet for your DocuMind engine
from langchain_community.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def process_document(file_path):
    # 1. Load the document
    loader = PyPDFLoader(file_path)
    data = loader.load()
    
    # 2. Create Embeddings & Store in Vector DB
    # This is the "Industry Level" part - using a Vector Store
    vectorstore = Chroma.from_documents(documents=data, embedding=OpenAIEmbeddings())
    
    return vectorstore

# 3. Future Step: Integrate with an LLM (LangChain) to answer questions
print("Document processed and vectorized into database.")
