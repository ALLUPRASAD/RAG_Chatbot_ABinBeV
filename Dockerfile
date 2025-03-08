# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory inside the container
COPY . /app
WORKDIR /app/src/


# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Set environment variables (Modify as needed)
ENV APP_HOST="0.0.0.0"
ENV APP_PORT="8000"
ENV MODEL_NAME="all-MiniLM-L6-v2" 
ENV OPENAI_API_KEY=""

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI app with automatic reload for development
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
