from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings 
from langchain_huggingface import HuggingFaceEndpoint
from backend.Modules.config import (
    FALCON_MODEL,
    DEEPSEEK_MODEL,
    HUGGINGFACE_KEY
)

#HuggingFaceEndpoint: Used to access model via API
#HuggingFacePipeline: Used to download model to local filesystem first

class Chatbot:
    def __init__(self, model_name: str = DEEPSEEK_MODEL, api_token: str = HUGGINGFACE_KEY):
        """
        Initializes the chatbot with Hugging Face API.

        Args:
            model_name (str): The Hugging Face model name.
            api_token (str): The Hugging Face API token.
        """
        self.model_name = model_name
        self.api_token = api_token
        self.llm = self.initialize_model(model_name)

    def initialize_model(self, model_name: str) -> HuggingFaceEndpoint:
        """
        Initializes the Hugging Face API-based model.

        Args:
            model_name (str): The Hugging Face model name.

        Returns:
            HuggingFaceEndpoint: The initialized API model.
        """
        return HuggingFaceEndpoint(
            repo_id=model_name,
            task="text-generation",
            max_new_tokens=300,
            do_sample=True,
            top_k=10,
            temperature=0.2,
            huggingfacehub_api_token=self.api_token,
        )

    def generate_text(self, prompt: str, context: str = None) -> str:
        """
        Generates text using the Hugging Face API model.

        Args:
            prompt (str): The user input or query.
            context (str, optional): Additional contextual information.

        Returns:
            str: The generated response.
        """
        if context is not None:
            prompt = f"""
             You are an AI assistant with access to specific documents. 
            If the user's question is about these documents, answer **only** from the context provided. 
            If the user asks a general question or engages in casual conversation, respond helpfully as normal. 
            Provide brief and concise answers unless the user explicitly asks for more details.

            Context:
            {context}

            Question: {prompt}

            Answer:
            """

        raw_response = self.llm.invoke(prompt)
        if isinstance(raw_response, list) and raw_response and "generated_text" in raw_response[0]:
            text = raw_response[0]["generated_text"]
        elif isinstance(raw_response, dict) and "generated_text" in raw_response:
            text = raw_response["generated_text"]
        else:
            text = str(raw_response)


        return text.strip()