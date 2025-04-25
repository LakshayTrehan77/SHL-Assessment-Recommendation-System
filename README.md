# SHL Assessment Recommendation System

This project implements a Retrieval-Augmented Generation (RAG) powered recommendation system designed to analyze job descriptions or candidate profiles and suggest relevant SHL assessments. By leveraging natural language processing (NLP), embeddings, and a ChromaDB vector database, it provides accurate, context-aware test recommendations to streamline the assessment selection process.

---

## ✨ Features

- **RAG-Powered Recommendations**: Combines retrieval of relevant assessment data with generative AI for context-aware outputs.
- **Flexible Input**: Supports text-based job descriptions or candidate profiles, with potential URL input support.
- **Structured Output**: Delivers detailed assessment recommendations, including name, URL, duration, and type.
- **SHL Catalog Integration**: Connects with an SHL assessment catalog stored in ChromaDB for up-to-date recommendations.
- **Debug Mode**: Offers transparency into the retrieval and generation process when enabled.
- **Data Validation**: Ensures reliable and consistent recommendation outputs.

---

## 📦 Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LakshayTrehan77/SHL-Assessment-Recommendation-System.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd SHL-Assessment-Recommendation-System
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**:
   - Set your API key in the environment:
     ```bash
     export API_KEY="your-api-key-here"
     ```

---

## 🚀 Usage

The project offers two ways to interact with the system:

### Option 1: Launch the Streamlit App
Run the Streamlit-based user interface:
```bash
streamlit run streamlit_app.py
```
- Access the app in your browser at `http://localhost:8501`.
- Input a job description or candidate profile and view recommended SHL assessments.

### Option 2: Start the FastAPI Server
Run the RESTful API server:
```bash
uvicorn api_app:app --reload
```
- Access the API endpoints at `http://localhost:8000`.
- Use tools like `curl` or Postman to query the system programmatically.

---

## 🧠 Approach

The SHL Assessment Recommendation System uses a Retrieval-Augmented Generation (RAG) pipeline to generate recommendations:

1. **Input Processing**:
   - Accepts job descriptions or candidate profiles via text input or URL (if supported).
   - Preprocesses the text to clean and standardize it for embedding generation.

2. **Embedding Generation**:
   - Converts input text into embeddings using pre-trained models.
   - Stores SHL assessment catalog data as embeddings in ChromaDB for efficient retrieval.

3. **Retrieval**:
   - Queries the ChromaDB vector database to retrieve the most relevant assessment entries based on similarity between input embeddings and stored embeddings.
   - Returns top-matching assessment metadata (e.g., name, URL, duration).

4. **Recommendation Generation**:
   - Feeds retrieved assessment data into a generative AI model (via Gemini API or similar) to produce context-aware, natural language recommendations.
   - Combines factual retrieval with generative output for improved accuracy and coherence.

5. **Output Delivery**:
   - Presents recommendations in a structured format (e.g., JSON or UI display).
   - Optionally includes debug information to explain the retrieval and generation process.

---

## 🛠 Tools and Technologies

The project is built using the following tools and technologies:

- **Programming Language**: Python
- **Web Frameworks**:
  - **Streamlit**: Powers the interactive user interface.
  - **FastAPI**: Provides RESTful API endpoints for programmatic access.
- **Data Processing**:
  - **Pandas**: For data manipulation and analysis.
  - **BeautifulSoup4**: For parsing HTML content (if URL input is supported).
- **Vector Database**:
  - **ChromaDB**: Stores and retrieves assessment embeddings for the RAG pipeline.
- **Embedding Models**:
  - Langchain and Gemini Embeddings.
- **RAG Framework**:
  - **LangChain**: Facilitates the RAG pipeline for retrieval and generation.
- **API Integration**:
  - **Gemini API**: Used for generative AI to produce natural language recommendations.


---

## 🧪 Example Use Case

### Input
A job description for a software engineering role:
```
"Looking for a Software Engineer with 3+ years of experience in Java, problem-solving skills, and teamwork."
```

### Output
A list of recommended SHL assessments:
```json
[
  {
    "Assessment Name": "Java Programming Test",
    "URL": "https://www.shl.com/assessments/java-programming-test",
    "Remote Testing Support": "Yes",
    "Adaptive/IRT Support": "Yes",
    "Duration": "30 mins",
    "Test Type": "Cognitive"
  },
  {
    "Assessment Name": "Problem Solving Assessment",
    "URL": "https://www.shl.com/assessments/problem-solving",
    "Remote Testing Support": "Yes",
    "Adaptive/IRT Support": "No",
    "Duration": "20 mins",
    "Test Type": "Cognitive"
  }
]
```

---

## 👥 Contributors

- Lakshay Trehan ([@LakshayTrehan77](https://github.com/LakshayTrehan77))

---



