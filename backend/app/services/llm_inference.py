from config import DEEPSEEK_MODEL, HUGGINGFACE_KEY
from langchain_huggingface.llms import HuggingFacePipeline

FALCON_MODEL = "tiiuae/falcon-7b-instruct"

class DeepSeekModel:
    def __init__(self, model_name: str):
        """
        Initializes the DeepSeek model.

        Args:
            model_name (str): The Hugging Face model name.
        """
        self.model_name = model_name
        self.pipeline = self.initialize_model(model_name)

    def initialize_model(self, model_name: str):
        """
        Loads the Hugging Face model pipeline.

        Args:
            model_name (str): The Hugging Face model name.

        Returns:
            HuggingFacePipeline: The initialized model pipeline.
        """
        return HuggingFacePipeline.from_model_id(
            model_id=model_name,
            task="text-generation",
            model_kwargs={"device": "cpu", "temperature": 0.2, "max_length": 500}
        )

    def generate_text(self, prompt: str, context: str = None) -> str:
        """
        Generates text based on the provided prompt and context.

        Args:
            prompt (str): The user input or query.
            context (str, optional): Additional contextual information.

        Returns:
            str: The generated response.
        """
        if context is not None:
            prompt = f"""
            You are an AI assistant with access to specific documents.
            Use only the following context to answer the question.

            Context:
            {context}

            Question: {prompt}

            Answer:
            """

        sequences = self.pipeline(
            prompt, 
            max_length=500, 
            do_sample=True, 
            top_k=3, 
            num_return_sequences=1
            eos_token_id=HUGGINGFACE_KEY
            )

        # Extracting and returning the generated text
        return sequences[0]["generated_text"]
