import os
import glob
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document
from logging_config.logging_config import logger  # Import the logger
logger.info("LangChain VectorStore initialized.")

class VectorStore:
    def __init__(self, data_path="qna_chatbot/data/**/*.md", model_name="all-MiniLM-L6-v2", chunk_size=500, overlap=100):
        self.data_path = data_path
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.embeddings = SentenceTransformerEmbeddings(model_name=model_name)
        self.vector_store = None
        logger.info("LangChain VectorStore initialized.")

    def load_and_process_documents(self):
        """Loads markdown documents, splits them into overlapping chunks, and processes them."""
        try:
            file_paths = glob.glob(self.data_path, recursive=True)
            if not file_paths:
                logger.warning("No markdown files found.")
                return []

            documents = []
            for file_path in file_paths:
                try:
                    loader = TextLoader(file_path, encoding="utf-8")
                    docs = loader.load()  # Returns a list of `Document` objects
                    documents.extend(docs)
                    logger.info(f"Loaded file: {file_path}")
                except Exception as e:
                    logger.error(f"Error reading file {file_path}: {e}")

            return self.chunk_documents(documents)
            
        except Exception as e:
            logger.error(f"Error loading files: {e}")
            return []

    def chunk_documents(self, documents):
        """Splits documents into overlapping chunks and returns them as `Document` objects."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""],
        )

        chunks = []
        for doc in documents:
            split_texts = text_splitter.split_text(doc.page_content)  # Extracts `page_content`
            chunks.extend([Document(page_content=chunk) for chunk in split_texts])  # Wraps chunks as `Document`

        logger.info(f"Created {len(chunks)} chunks from documents.")
        return chunks

    def build_index(self):
        """Creates a FAISS vector store."""
        try:
            chunks = self.load_and_process_documents()
            if not chunks:
                logger.warning("No document chunks available for indexing.")
                return

            self.vector_store = FAISS.from_documents(chunks, self.embeddings)
            self.vector_store.save_local("vector_store")

            logger.info(f"Vector Store Created with {len(chunks)} chunks!")

        except Exception as e:
            logger.error(f"Error building FAISS index: {e}")

    def load_index(self):
        """Loads an existing FAISS index from the correct path."""
        index_path = "qna_chatbot/src/faiss_index"
    
        try:
            if not os.path.exists(os.path.join(index_path, "index.faiss")):
                raise FileNotFoundError(f" FAISS index not found at {index_path}. Ensure you have built it.")
    
            self.vector_store = FAISS.load_local(index_path, self.embeddings)
            logger.info(f"✅ Successfully loaded FAISS index from {index_path}.")
    
        except Exception as e:
            logger.warning(f"No existing index found. Please build one first. Error: {e}")

if __name__ == "__main__":
    try:
        vector_store = VectorStore(chunk_size=500, overlap=100)
        vector_store.build_index()
    except Exception as e:
        logger.critical(f"Critical error: {e}")
