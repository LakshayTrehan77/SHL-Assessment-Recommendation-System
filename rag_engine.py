import os
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

os.environ["GOOGLE_API_KEY"] = "AIzaSyAs0LwCSfSlECkmcYhVJ8r5sHYKcKNfX6E"

def get_rag_chain():
    
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    db = Chroma(
        persist_directory="./chromadb", 
        embedding_function=embedding
    )
    
    retriever = db.as_retriever(search_kwargs={"k": 10})
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
    
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    
    return chain