FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt


# Set Hugging Face cache directory (to prevent downloading every time)
ENV HF_HOME=/app/huggingface_cache
RUN mkdir -p $HF_HOME

# Copy backend code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]