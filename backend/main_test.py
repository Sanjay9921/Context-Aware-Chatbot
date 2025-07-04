from modules.llm_ops.qa_engine import generate_answer
from settings.config import Config
import pandas as pd
from modules.llm_testing.test_runner import run_and_save_test_suite

models = [Config.MODEL_NAME_1, Config.MODEL_NAME_2, Config.MODEL_NAME_3]
file_path = "./tests/sample_docs/Databricks_Prompt_Engineering_Steps.pdf"
df_test_suite = pd.read_excel("./tests/test_suite.xlsx", sheet_name="Test1")

print("Test started...", flush=True)

df_results = run_and_save_test_suite(
    df_test_suite=df_test_suite,
    models=models,
    file_path=file_path,
    output_csv_path="./tests/results/test.csv",
    generate_answer_fn=generate_answer,
    iterations=3,
    delay=12
)

print("Test completed successfully!")