from modules.qa_engine import generate_answer
from config.settings import TOGETHER_API_KEY, MODEL_NAME_1, MODEL_NAME_2, MODEL_NAME_3
import pandas as pd
from modules.llm_testing.test_runner import run_and_save_test_suite

models = [MODEL_NAME_1, MODEL_NAME_2, MODEL_NAME_3]
file_path = "./tests/sample_docs/Databricks_Prompt_Engineering_Steps.pdf"
df_test_suite = pd.read_excel("./tests/test_suite.xlsx", sheet_name="Test1")

df_results = run_and_save_test_suite(
    df_test_suite=df_test_suite,
    models=models,
    file_path=file_path,
    output_csv_path="./tests/results/test3.csv",
    generate_answer_fn=generate_answer,
    iterations=3,
    delay=10
)
print("Test completed successfully!")