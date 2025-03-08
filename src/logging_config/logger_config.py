import logging
import os

# Ensure log directory exists
log_dir = os.path.join(os.path.dirname(__file__), "../../data/logs")
os.makedirs(log_dir, exist_ok=True)

# Define log file path
log_file = os.path.join(log_dir, "chatbot.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),  # Logs to file
        logging.StreamHandler()         # Logs to console
    ]
)

# Get logger instance
logger = logging.getLogger(__name__)
