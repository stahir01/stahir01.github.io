FROM python:3.13

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend directory (including backend/)
COPY . .

# Expose port 8000 for the API
EXPOSE 8000

# Run the FastAPI application using uvicorn, pointing to backend.main
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]