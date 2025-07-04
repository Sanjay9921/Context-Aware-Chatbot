# modules/llm_testing/scoring.py

from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from .keyword_cleaning import clean_expected_keywords_list
import ast

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_similarity(text1: str, text2: str) -> float:
    embeddings = embedder.encode([text1, text2])
    return round(cosine_similarity([embeddings[0]], [embeddings[1]])[0][0], 4)

def generate_and_score_response(prompt, model, expected_keywords, generate_answer_fn, reference_response=None, context=None):
    import time
    start = time.time()
    response = generate_answer_fn(context, prompt, model)
    end = time.time()

    response_time = round(end - start, 2)
    consistency_score, similarity_score, matched_keywords = "N/A", "N/A", []

    try:
        if isinstance(expected_keywords, str):
            expected_keywords = ast.literal_eval(expected_keywords)

        expected_keywords = [str(kw).strip().lower() for kw in expected_keywords]
        matched_keywords = [kw for kw in expected_keywords if kw in response.lower()]
        consistency_score = round(len(matched_keywords) / len(expected_keywords), 2) if expected_keywords else 0.0
        similarity_score = round(semantic_similarity(response, reference_response), 2) if reference_response else 1.0

    except Exception as e:
        print(f"Scoring error: {e}")

    return {
        "prompt": prompt,
        "response": response,
        "response_time_s": response_time,
        "matched_keywords": matched_keywords,
        "consistency_score": consistency_score,
        "similarity_score": similarity_score
    }