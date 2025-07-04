# modules/llm_testing/test_runner.py

import pandas as pd
import time
import logging
from .preprocessing import prepare_context
from .batch_processor import process_batch

def run_test_suite(df_test_suite, models, file_path, generate_answer_fn, iterations=3, delay=10):
    df_results = pd.DataFrame()

    for iteration in range(1, iterations + 1):

        # 1. Data Preprocessing
        full_context, metadata = prepare_context(file_path)
        logging.info(f"Chunking Metadata: {metadata}")

        df_curr_results = pd.DataFrame()
        logging.info(f"--- Iteration {iteration} ---")
        iter_start = time.time()

        print(f"Iteration: {iteration} has started.")

        # 2. Batch Processing
        for i in range(0, len(df_test_suite), 3):
            batch_df = df_test_suite.iloc[i:i + 3]
            for model in models:
                batch_results = process_batch(
                    batch_df=batch_df,
                    model=model,
                    iteration=iteration,
                    context=full_context,
                    generate_answer_fn=generate_answer_fn,
                    delay=delay
                )
                df_curr_results = pd.concat([df_curr_results, batch_results], ignore_index=True)

        # 3. Add metadata to current iteration
        iter_time = round(time.time() - iter_start, 2)
        logging.info(f"Iteration {iteration} completed in {iter_time} seconds.")

        df_curr_results["preprocessing_metadata"] = [metadata] * len(df_curr_results)
        df_curr_results["iteration_time_log"] = [iter_time] * len(df_curr_results)

        # 4. Append to full results
        df_results = pd.concat([df_results, df_curr_results], ignore_index=True)

        print(f"Iteration: {iteration} has completed.")
        print(f"Resulting Dataframe has a shape of: {df_results.shape}")

    return df_results

def run_and_save_test_suite(df_test_suite, models, file_path, output_csv_path, generate_answer_fn, iterations=3, delay=10):
    print("Test has started...")
    df_results = run_test_suite(df_test_suite, models, file_path, generate_answer_fn, iterations, delay)

    df_results["test_case"] = df_results.index + 1
    df_results.to_csv(output_csv_path, index=False)
    logging.info(f"Test results saved to {output_csv_path}")
    return df_results