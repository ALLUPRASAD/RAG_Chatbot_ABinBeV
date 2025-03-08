
import os
import logging
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Load API key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure logging
from logging_config.logger_config import logger  # Import the logger
logger.info("loading model...")

class LLMModel:
    def __init__(self, model_name="gpt-3.5-turbo"):
        if not OPENAI_API_KEY:
            logger.error("OPENAI_API_KEY not found. Please check your .env file.")
            raise ValueError("OPENAI_API_KEY is missing.")
        
        self.llm = ChatOpenAI(model_name=model_name, temperature=0.7)  # LangChain wrapper
        logger.info(f"Initialized LangChainLLM with model: {model_name}")

    def generate_answer(self, retrieved_text, query):
        """Generates a response using the LLM."""
        if not retrieved_text.strip():
            logger.warning("Retrieved text is empty. The response may not be relevant.")

        logger.info(f"Generating response for query: {query}")

        try:
            messages = [
                SystemMessage(content="You are a helpful assistant."),
                HumanMessage(content=f"{retrieved_text}\n\n{query}")
            ]
            response = self.llm(messages)  # Call the LLM using LangChain

            logger.info("Successfully generated response from LLM.")
            return response.content
        
        except Exception as e:
            logger.error(f"Error while generating response: {e}")
            return "Sorry, I encountered an error while processing your request."

# Example usage
if __name__ == "__main__":
    llm = LangChainLLM()
    answer = llm.generate_answer("To update Ubuntu, use 'sudo apt update && sudo apt upgrade'", "How do I update Ubuntu?")
    print(answer)

