from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot.bot import Chatbot
from logging_config.logger_config import logger  # Import the logger

# Initialize FastAPI application
app = FastAPI(
    title="Q&A Chatbot API",
    description="An API to interact with a Q&A chatbot trained on Ubuntu documentation.",
    version="1.0"
)

# Initialize chatbot instance
chatbot = Chatbot()

# Request model
class QueryRequest(BaseModel):
    query: str

@app.post("/ask", summary="Get chatbot response", response_description="Chatbot-generated answer")
async def ask(request: QueryRequest):
    """
    Accepts a user query and returns a response from the chatbot.
    """
    try:
        logger.info(f"Received query: {request.query}")
        response = chatbot.answer(request.query)
        logger.info(f"Generated response: {response}")
        return {"response": response}
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/", summary="Health check", response_description="API status")
async def health_check():
    """
    Health check endpoint to confirm API is running.
    """
    logger.info("Health check requested.")
    return {"message": "✅ Q&A Chatbot API is running!"}
