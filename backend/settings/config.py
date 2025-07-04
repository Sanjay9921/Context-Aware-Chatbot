# settings/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:

    # Together AI
    TOGETHER_API_URL = os.getenv("TOGETHER_API_URL")
    TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

    MODEL_NAME_1 = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
    MODEL_NAME_2 = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free"
    MODEL_NAME_3 = "lgai/exaone-3-5-32b-instruct"

    # HUGGING FACE
    HUGGING_FACE_API_URL = os.getenv("HUGGING_FACE_API_URL")
    HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")

    MODEL_NAME_4 = "meta-llama/Llama-3.3-70B-Instruct"

    # Default Parameters
    DEFAULT_API_URL =  TOGETHER_API_URL
    DEFAULT_API_KEY = TOGETHER_API_KEY
    DEFAULT_MODEL = MODEL_NAME_1