# Portfolio Website

This project is a comprehensive portfolio website that not only showcases work experience and projects but also integrates a sophisticated Retrieval-Augmented Generation (RAG) chatbot. The chatbot is connected to a vector database to answer user queries based on document context. It also maintains conversation history to ensure context-aware and coherent responses, making the interaction both dynamic and informative.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setting Up the Project](#setup)
- [Local Development](#local-development)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Docker Instructions](#docker-instructions)
  - [Building and Running Containers Individually](#building-and-running-containers-individually)
  - [Using Docker Compose](#using-docker-compose)

## Overview

This portfolio website displays information about the developer's work and projects. The **frontend** is a static site built with HTML, CSS, and JavaScript, while the **backend** is a REST API built with FastAPI that serves data and processes chatbot queries.

- **Backend:** FastAPI application that can be run with Uvicorn.
- **Frontend:** Static site served by Nginx.

## Project Structure

Portfolio_New/ ├── backend/ │ ├── main.py │ ├── requirements.txt │ └── Modules/ │ └── ... (backend code) ├── frontend/ │ ├── index.html │ ├── css/ │ ├── js/ │ └── ... (other static assets) ├── docker-compose.yml └── README.md

## Setting Up the Project

1. **Install Python and Create a Virtual Environment.**

    First, make sure you have Python 3.9+ installed. Then, create a virtual environment:

    ```bash
    python -m venv venv  # Create virtual environment
    source venv/bin/activate  # Activate on macOS/Linux
    ```

2. **Install Required Libraries**

    Once the virtual environment is activated, install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a .env File**

    The ```bash.env``` file is important in order to store HuggingFace credentials. Since this implementation uses Hugging Face models instead of OpenAI or Ollama, you need to add your API key:

    ```bash
    HUGGINGFACE_Key = <your_huggingface_api_key>
    ```

## Local Development

### Backend

1. **Navigate to the backend folder:**

   ```bash
   cd backend
   ```
2. **Run the FastAPI server with Uvicorn:**

   ```bash
   uvicorn main:app --reload
   ```
3. **Test the API:**
Visit ```http://localhost:8000/docs``` in your browser to see the Swagger UI and test your endpoints.

### Frontend

1. **Navigate to the frontend folder (if needed):**

   ```bash
   cd frontend
   ```
2. **Run the FastAPI server with Uvicorn:**

   ```bash
   python -m http.server 80
   ```
3. **Test the API:**
Visit ```http://localhost:80``` in your browser.


## Docker Instructions

### Backend

1. **Build the backend Docker image:**

   ```bash
   cd backend
    docker build -t website_backend:latest .
   ```
2. **Run the backend container:**

   ```bash
   docker run -p 8000:8000 --name backend_container website_backend:latest
   ```
The FastAPI backend will be accessible at ```http://localhost:8000.```



### Frontend

1. **Build the frontend Docker image:**

   ```bash
   cd frontend
    docker build -t website_frontend:latest .
   ```
2. **Run the frontend container:**

   ```bash
   docker run -p 80:80 --name frontend_container website_frontend:latest
   ```
The frontend site will be accessible at ```http://localhost:80```.



## Using Docker Compose
A ```docker-compose.yml``` file is provided to run both containers together.

1. **Build and run both containers:**

   ```bash
   docker-compose up --build
   ```
2. **Access the services:** 
- The FastAPI backend will be accessible at ```http://localhost:8000```.
- The frontend site will be accessible at ```http://localhost:80```.





