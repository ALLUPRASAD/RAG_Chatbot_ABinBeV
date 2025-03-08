# Q&A Chatbot (Basic RAG)

## Project Overview
This project involves creating a Q&A chatbot that leverages a vector store and a Language Model (LLM) Trubo3.5 to provide accurate responses to user queries. The chatbot utilizes Ubuntu documentation in markdown format as its knowledge base.

### 1: Create Vector Store
- Use provided Ubuntu documentation.
- Implement a local vector store Faiss.

### 2: Build Chatbot with Vector Store & LLM
 Integrate vector store with chatbot using **LangChain retrievers**.
- Implement query interpretation and response generation.
- Use a free OpenAI endpoint for LLM querying (**GPT-3.5/GPT-4**).
- Implement structured logging and proper exception handling.
  
### 3.Project Root
├── 📄 requirements.txt
├── 📄 Dockerfile
├── 📄 README.md
├── 📄 .gitignore
├── 📂 data
│   ├── 📂 logs
│   │   └── 📄 chatbot.log
│   ├── 📂 ubuntu-docs
│   │   ├── 📄 .DS_Store
│   │   ├── 📄 .gitignore
│   │   └── 📄 .sass-lint.yml
├── 📂 src
│   ├── 📄 .DS_Store
│   ├── 📄 requirements.txt
│   ├── 📂 chatbot
│   │   ├── 📄 __init__.py
│   │   └── 📄 bot.py
│   ├── 📂 logging_config
│   │   └── 📄 logger_config.py
│   ├── 📂 retriever
│   │   └── 📄 retriever.py
│   ├── 📂 vector_store
│   │   └── 📄 ingest.py
│   ├── 📂 model
│   │   └── 📄 model.py
│   ├── 📂 faiss_index
│   │   ├── 📄 index.faiss
│   │   └── 📄 index.pkl
│   └── 📄 app.py


##4 How to Run

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt


## How to Run

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start FastAPI Server
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### Step 3: Run in Docker
```bash
docker build -t qna-chatbot .
docker run -d -p 8000:8000 --name qna_chatbot_container qna-chatbot
```

### Step 4: Access API
- Open `http://localhost:8000/docs` in your browser to test via Swagger UI.


