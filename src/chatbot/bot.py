from retriever.retriever import Retriever
from model.model import LLMModel
from logging_config.logger_config import logger  # Import the logger
logger.info("Initializing chatbot...")

class Chatbot:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLMModel()
        logger.info("Chatbot initialized with Retriever and LLMModel.")

    def answer(self, query):
        logger.info(f"Received query: {query}")

        retrieved_chunks = self.retriever.retrieve(query, top_k=3)
        logger.debug(f"Retrieved chunks: {retrieved_chunks}")

        if not retrieved_chunks:
            logger.warning("No relevant information found for the query.")
            return "I'm sorry, I couldn't find relevant information."

        # Combine retrieved text
        retrieved_text = "\n".join(retrieved_chunks)

        # Generate answer
        answer = self.llm.generate_answer(retrieved_text, query)
        logger.info("Generated response successfully.")
        return answer

# Run chatbot for testing
if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.answer("How do I install a package in Ubuntu?")
    print(response)
