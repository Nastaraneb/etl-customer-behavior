from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# placeholder function (empty for now)
def placeholder_task():
    pass

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
        python_callable=placeholder_task,
    )

    load_to_db = PythonOperator(
        task_id="load_to_db",
        python_callable=placeholder_task,
    )

    check_raw_file >> preprocess_data >> load_to_db
