import os
import logging
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from logging_config.logger_config import logger  # Import the logger
logger.info("Successfully loaded FAISS index.")


class Retriever:
    def __init__(self, model_name="all-MiniLM-L6-v2", index_path="faiss_index"):
        """Initialize the Retriever with a SentenceTransformer model and FAISS index."""
        self.embeddings = SentenceTransformerEmbeddings(model_name=model_name)

        try:
            if not os.path.exists(f"{index_path}/index.faiss"):
                raise FileNotFoundError(f"FAISS index not found at {index_path}. Ensure you have built it.")

            # Enable safe deserialization
            self.vector_store = FAISS.load_local(index_path, self.embeddings, allow_dangerous_deserialization=True)
            logger.info(f"✅ Successfully loaded FAISS index from {index_path}")

        except Exception as e:
            logger.error(f"Failed to load FAISS index: {e}")
            raise  # Propagate error

    def retrieve(self, query, top_k=3):
        """Retrieves the top_k most similar documents for a given query."""
        try:
            results = self.vector_store.similarity_search(query, k=top_k)
            return [doc.page_content for doc in results]  # Extracts document text
        except Exception as e:
            logger.error(f"Error retrieving results: {e}")
            return []

# Example usage
if __name__ == "__main__":
    retriever = Retriever()
    results = retriever.retrieve("How do I update Ubuntu?")
    
    print("\n🔍 Top Retrieved Documents:")
    for i, res in enumerate(results, 1):
        print(f"{i}. {res}")

    print(" Retriever Ready!")
