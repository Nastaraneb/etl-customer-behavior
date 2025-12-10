from datetime import datetime
import sys
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook



sys.path.append("/opt/airflow/processor")
from preprocessing import CustomerBehaviorPreprocessor

# file paths inside the container
RAW_DATA_PATH = "/opt/airflow/data/raw/online_shoppers_intention.csv"
PROCESSED_DATA_PATH = "/opt/airflow/data/processed/online_shoppers_preprocessed.csv"

def run_preprocessing():
    """Run the OOP preprocessing pipeline."""
    processor = CustomerBehaviorPreprocessor(
        input_path=RAW_DATA_PATH,
        output_path=PROCESSED_DATA_PATH,
    )
    processor.run()

def load_processed_to_db():
    # 1) Read processed file
    df = pd.read_csv(PROCESSED_DATA_PATH)

    # 2) Connect to Postgres via Airflow Connection
    hook = PostgresHook(postgres_conn_id="etl_postgres")
    engine = hook.get_sqlalchemy_engine()

    # 3) Load into table
    table_name = "customer_behavior_clean"
    df.to_sql(table_name, engine, if_exists="replace", index=False)

    print(f"Loaded {len(df)} rows into {table_name}")

with DAG(
    dag_id="customer_behavior_etl",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["etl", "customer_behavior"],
) as dag:

    check_raw_file = BashOperator(
        task_id="check_raw_file",
        bash_command="echo 'Checking dataset...'",
    )

    preprocess_data = PythonOperator(
        task_id="preprocess_data",
        python_callable=run_preprocessing,
    )

    

    load_to_db = PythonOperator(
        task_id="load_to_db",
        python_callable=load_processed_to_db,
    )

    check_raw_file >> preprocess_data >> load_to_db
