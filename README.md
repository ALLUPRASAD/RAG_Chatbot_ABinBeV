# Q&A Chatbot (Basic RAG)

## Project Overview
This project involves creating a Q&A chatbot that leverages a vector store and a Language Model (LLM) Trubo3.5 to provide accurate responses to user queries. The chatbot utilizes Ubuntu documentation in markdown format as its knowledge base.

### Part 1: Create Vector Store
- Use provided Ubuntu documentation.
- Implement a local vector store Faiss.

### Part 2: Build Chatbot with Vector Store & LLM
- Integrate vector store with chatbot.
- Implement query interpretation and response generation.
- Use a free OpenAI endpoint for LLM querying.


## How to Run

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


