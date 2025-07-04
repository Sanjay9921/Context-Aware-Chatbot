# modules/llm_testing/keyword_cleaning.py

def clean_expected_keywords_list(raw_keywords):
    cleaned = []
    for kw in raw_keywords:
        if isinstance(kw, tuple):
            # Take first element if tuple
            kw = kw[0]
        # Convert to string just in case, and strip whitespace
        cleaned.append(str(kw).strip())
    return cleaned