 Q&A Chatbot (Basic RAG)

## Project Overview
This project involves creating a Q&A chatbot that leverages a vector store and a Language Model (LLM) to provide accurate responses to user queries. The chatbot utilizes Ubuntu documentation in markdown format as its knowledge base.

## Main Tasks (100 Marks)

### Part 1: Create Vector Store
- Use provided Ubuntu documentation.
- Implement a local vector store (Faiss or ChromaDB preferred).
- Use OS Embeddings models from Hugging Face.

### Part 2: Build Chatbot with Vector Store & LLM
- Integrate vector store with chatbot.
- Implement query interpretation and response generation.
- Use a free OpenAI endpoint for LLM querying.

## Bonus Tasks
- Implement a FastAPI endpoint (`app.py`) for local deployment (50 marks).
- Deploy the chatbot using Docker and test via Swagger (50 marks).

## Requirements
- Utilize provided input files and demo video.
- Implement modular, structured, and maintainable code.
- Include logging for different levels.
- Implement proper error and exception handling.
- Optimize document parsing and chunking strategy.

## General Guidelines
- Push code to a public GitHub repository with commit-wise grouping.
- Create an `.md` file with outcome screenshots.
- Share a working demo video as the final deliverable.

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


