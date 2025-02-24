from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings 
from langchain.memory import ChatMessageHistory
from typing import List, Optional
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
        self.chat_history = ChatMessageHistory()
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
            max_new_tokens=100,
            do_sample=True,
            top_k=10,
            temperature=0.2,
            huggingfacehub_api_token=self.api_token,
        )

    def generate_text(self, prompt: str, context: str = None) -> str:
            
            """
            Generates text using the Hugging Face API model,
            incorporating conversation history and context.

            Args:
                prompt (str): The user input or query.
                context (str, optional): Additional contextual information.

            Returns:
                str: The generated response.
            """
            greetings = ['hi', 'hello', 'hey', 'hui', 'hiiii', 'hii', 'hiii', 'heyyy']
            
            # Add the user message to chat history
            self.chat_history.add_user_message(prompt)
            
            # Build a history string from chat_history messages.
            # Depending on your ChatMessageHistory implementation, messages may be HumanMessage/AIMessage objects.
            # We'll assume they have a .content attribute and use their type names.
            history_str = "\n".join(
                [f"{msg.__class__.__name__}: {msg.content}" for msg in self.chat_history.messages]
            ) if self.chat_history.messages else "No conversation history."

            # If the prompt is a greeting, use a simple response.
            if prompt.lower().strip() in greetings:
                final_prompt = 'Just simply reply with "Hello! How can I assist you today?"'
            else:
                if context is not None:
                    final_prompt = f"""
                    You are an AI assistant with access to specific documents.
                    Answer the question based only on the following context.
                    If the question is out of context, please respond with "I can't answer questions out of context."

                    Conversation History:
                    {history_str}

                    Context:
                    {context}

                    Question: {prompt}

                    Answer:
                    """
                else:
                    final_prompt = f"""
                    You are an AI assistant.
                    Conversation History:
                    {history_str}

                    Question: {prompt}

                    Answer:
                    """
                final_prompt = "\n".join(line.strip() for line in final_prompt.strip().splitlines())

            # Invoke the model with the final prompt
            raw_response = self.llm.invoke(final_prompt)
            
            # Parse the response: if the model returns a list/dict with "generated_text", extract it; otherwise, cast to string.
            if isinstance(raw_response, list) and raw_response and "generated_text" in raw_response[0]:
                response_text = raw_response[0]["generated_text"]
            elif isinstance(raw_response, dict) and "generated_text" in raw_response:
                response_text = raw_response["generated_text"]
            else:
                response_text = str(raw_response)

            response_text = response_text.strip()

            # Add the AI's reply to chat history
            self.chat_history.add_ai_message(response_text)

            return response_text
