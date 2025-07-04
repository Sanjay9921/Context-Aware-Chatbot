# modules/llm_testing/preprocessing.py

from modules.pdf_parser import extract_text_from_static_pdf
from modules.text_preprocessor import preprocess_text
import time

def prepare_context(file_path, num_chunks=15):
    start = time.time()
    text = extract_text_from_static_pdf(file_path)
    chunks = preprocess_text(text)
    end = time.time()

    return "\n".join(chunks[:num_chunks]), {
        "chunking_time_s": round(end - start, 2),
        "total_chunks": len(chunks),
        "total_characters": len(text)
    }