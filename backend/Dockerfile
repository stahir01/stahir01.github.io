FROM python:3.13

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend directory (including backend/)
COPY . .

# Set PYTHONPATH to include the /app directory so Python can find the 'backend' package
ENV PYTHONPATH=/app

# Expose port 8000 for the API
EXPOSE 8000

# Run the FastAPI application using uvicorn, pointing to backend.main
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]