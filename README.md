🔍 RAG-Powered LLM Application
This project implements a Retrieval-Augmented Generation (RAG) pipeline using LLMs to provide intelligent, context-aware answers by combining document retrieval with generative AI. It also features an interactive Streamlit UI, and RESTful endpoints via FastAPI.

📂 Project Structure
graphql
Copy
Edit
├── chromadb/             # Local vector database (Chroma)
├── __pycache__/          # Python cache
├── api_app.py            # FastAPI application for serving API
├── catalog.json          # Data catalog with metadata/config
├── catalog_loader.py     # Utility to load and parse catalog.json
├── main.py               # Main runner / entry point
├── rag_engine.py         # Core RAG pipeline logic
├── requirements.txt      # Required Python packages
├── streamlit_app.py      # Streamlit-based UI
├── vector_store.py       # Embedding + Vector DB logic
🧠 Approach
🔹 1. Document Processing
Documents/data are loaded via catalog_loader.py.

Text chunks are embedded using pre-trained embeddings (e.g., OpenAI, SentenceTransformers).

These embeddings are stored in ChromaDB via vector_store.py.

🔹 2. Retrieval-Augmented Generation (RAG)
User input queries are first processed to retrieve relevant chunks from the vector database (rag_engine.py).

Retrieved content is passed to an LLM chain to generate informed answers. This hybrid improves factuality and context-awareness.

🔹 3. API Layer
api_app.py exposes the RAG engine as a REST API using FastAPI.

Endpoints allow querying the model and retrieving answers programmatically.

🔹 4. Interactive UI
streamlit_app.py provides a web-based interface.

Users can input queries and see responses with cited source chunks for transparency.

🚀 How to Run
1. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
2. Launch Streamlit App
bash
Copy
Edit
streamlit run streamlit_app.py
3. Run FastAPI Server
bash
Copy
Edit
uvicorn api_app:app --reload
📦 Dependencies
Key libraries include:

langchain or llama-index

chromadb

sentence-transformers or openai

streamlit

fastapi

✨ Features
RAG with real-time retrieval

Modular code: easy to plug in different vector DBs or models

Streamlit & FastAPI for flexible interfaces

Source-based answering (transparency)

🧪 Example Use Case
Query: "How does retrieval improve generative AI?"
Response: "Retrieval provides grounded, factual data to the language model, improving reliability and reducing hallucinations..."
(Sources: docs A, B, etc.)
