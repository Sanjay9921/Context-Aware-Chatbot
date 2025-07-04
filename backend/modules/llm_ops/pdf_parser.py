# modules/llm_ops/pdf_parser.py

import fitz  # PyMuPDF
from typing import Union, IO # static PDF uploads

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def extract_text_from_static_pdf(uploaded_file: Union[str, IO[bytes]]) -> str:
    # Check if input is a path or file-like object
    if isinstance(uploaded_file, str):
        doc = fitz.open(uploaded_file)
    else:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    full_text = ""
    for page in doc:
        full_text += page.get_text()

    return full_text