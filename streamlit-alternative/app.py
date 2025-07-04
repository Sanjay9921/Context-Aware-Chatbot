import streamlit as st
import fitz
from modules.pdf_parser import extract_text_from_pdf
from modules.text_preprocessor import preprocess_text
from modules.qa_engine import generate_answer
from config.settings import  MODEL_NAME_1, MODEL_NAME_2

# Streamlit page setup
st.set_page_config(page_title="Context-Aware PDF Chatbot", layout="wide")
st.title("Chat with your PDF")

# Upload a PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    # Step 1: Extract text from PDF
    text = extract_text_from_pdf(uploaded_file)
    
    # Step 2: Preprocess text (chunking via Langchain)
    chunks = preprocess_text(text)
    full_context = "\n".join(chunks[:15])  # Limit to top 15 chunks for context

    st.success("PDF processed. Ask your questions!")

    # Step 3: User input for questions
    user_question = st.text_input("Ask a question about the document:")

    if user_question:
        with st.spinner("Generating answer..."):
            _model = MODEL_NAME_1
            print(_model)
            answer = generate_answer(full_context, user_question, model=_model)
        st.markdown("** Answer:**")
        st.write(answer)