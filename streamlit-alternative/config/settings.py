import streamlit as st

TOGETHER_API_URL = st.secrets["TOGETHER_API_URL"]
TOGETHER_API_KEY = st.secrets["TOGETHER_API_KEY"]

MODEL_NAME_1 = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
MODEL_NAME_2 = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free"
MODEL_NAME_3 = "lgai/exaone-3-5-32b-instruct"