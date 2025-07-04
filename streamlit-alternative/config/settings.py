import os
from dotenv import load_dotenv # environment variables

load_dotenv()

TOGETHER_API_URL = os.getenv("TOGETHER_API_URL")
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

MODEL_NAME_1 = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
MODEL_NAME_2 = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free"
MODEL_NAME_3 = "lgai/exaone-3-5-32b-instruct"
MODEL_NAME_4 = "lgai/exaone-deep-32b"

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")