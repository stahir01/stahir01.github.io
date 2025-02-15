import os
from configparser import ConfigParser
from dotenv import load_dotenv

config = ConfigParser()

load_dotenv()


# Hugging Face API Key
HUGGINGFACE_KEY = os.getenv("HUGGINGFACE_KEY")

# OpenAI API Key
OPENAI_KEY = os.getenv("OPENAI_KEY")

# Hugging Face Model Names
DEEPSEEK_MODEL = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B"
FALCON_MODEL = "tiiuae/falcon-7b-instruct"
LLAMA_MODEL_70B = "meta-llama/Llama-2-70b-chat-hf"
MISTRAL_MODEL = "mistralai/Mistral-Large-Instruct-2407"

# Vector Database Configuration
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "vector_store")

#Embeddings
MINI_LM_EMBED = 'sentence-transformers/all-MiniLM-L6-v2'


