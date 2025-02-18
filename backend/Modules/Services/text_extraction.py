"""
This module extracts features from PDF, JFON, Word and Voice input files to be used for 
further processing, embedding, and storage. 
"""

import json
from langchain_community.document_loaders import PyPDFLoader, JSONLoader
from langchain_google_community import SpeechToTextLoader
from typing import Optional, List


def extract_text_from_pdf(pdf_path: str) -> List[str]:
    """
    Extracts text from a PDF file page by page.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        List[str]: A list containing extracted text from each page.
    """
    loader = PyPDFLoader(pdf_path)
    extracted_docs = [page.page_content for page in loader.load()]  # Synchronous

    return extracted_docs


def extract_text_from_json(json_path: str) -> List[str]:
    """
    Extracts relevant text from a structured JSON file, including both work experience and projects.

    Args:
        json_path (str): Path to the JSON file.

    Returns:
        List[str]: A list of extracted text content.
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    extracted_text = []

    if isinstance(data, dict):
        # Extract work experience
        if "work_experience" in data:
            for job in data["work_experience"]:
                company = job.get("company_name", "")
                role = job.get("role", "")
                # Use "combined_description" which is a full narrative of tasks
                description = job.get("description", "")
                # Combine into one text block for this job
                job_text = f"Company: {company}, Role: {role}. {description}"
                extracted_text.append(job_text)
        
        # Extract projects
        if "projects" in data:
            for project in data["projects"]:
                title = project.get("project_title", "")
                description = project.get("description", "")
                project_text = f"Project: {title}. {description}"
                extracted_text.append(project_text)

    return extracted_text


"""
#Used later on for chatbot
def extract_text_from_voice(voice_path: str) -> str:
    loader = SpeechToTextLoader(voice_path)

    extracted_docs = []

    async for page in loader.load_pages():
        extracted_docs.append(page.page_content)
"""





