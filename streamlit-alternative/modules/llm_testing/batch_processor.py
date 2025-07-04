# modules/llm_testing/batch_processor.py

import time
import pandas as pd
import ast
from modules.llm_testing.keyword_cleaning import clean_expected_keywords_list
from modules.llm_testing.scoring import generate_and_score_response

def process_batch(batch_df, model, iteration, context, generate_answer_fn, delay=10):
    results_df = pd.DataFrame()

    baseline_row = batch_df.iloc[0]
    variation_rows = batch_df.iloc[1:3]

    expected_keywords = baseline_row["expected_keywords"]
    try:
        expected_keywords = ast.literal_eval(expected_keywords) if isinstance(expected_keywords, str) else [expected_keywords]
    except Exception:
        expected_keywords = [expected_keywords]

    expected_keywords = clean_expected_keywords_list(expected_keywords)

    # Baseline
    result = generate_and_score_response(
        prompt=baseline_row["question"],
        model=model,
        expected_keywords=expected_keywords,
        generate_answer_fn=generate_answer_fn,
        context=context
    )
    result.update({
        "iteration": iteration,
        "model": model,
        "question_category": "baseline",
        "question_number": baseline_row["question_number"]
    })
    results_df = pd.concat([results_df, pd.DataFrame([result])], ignore_index=True)
    time.sleep(delay)

    # Variations
    reference_response = result["response"]
    for i, row in variation_rows.iterrows():
        variation_result = generate_and_score_response(
            prompt=row["question"],
            model=model,
            expected_keywords=expected_keywords,
            generate_answer_fn=generate_answer_fn,
            reference_response=reference_response,
            context=context
        )
        variation_result.update({
            "iteration": iteration,
            "model": model,
            "question_category": "variation",
            "question_number": row["question_number"]
        })
        results_df = pd.concat([results_df, pd.DataFrame([variation_result])], ignore_index=True)
        time.sleep(delay)

    return results_df